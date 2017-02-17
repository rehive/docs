# pylint: disable=C0111
# Missing docstring


from nose import tools

from version import Version
from script_exception import ScriptException

class Base(object):
    def __init__(self):
        pass

    @staticmethod
    def assert_raises(error_type,
                      error_message,
                      function_to_call,
                      *args,
                      **kwargs
                     ):
        with tools.assert_raises(error_type) as context_mgr:                        # pylint: disable=E1101
            ignore_result = function_to_call(*args, **kwargs)

        exception = context_mgr.exception
        tools.assert_equal(exception.message,                                       # pylint: disable=E1101
                           error_message,
                          )


class TestVersion(Base):
    def __init__(self):
        Base.__init__(self)

    @staticmethod
    def version_string_identity(version_string):
        version = Version(version_string)
        tools.assert_equal(version_string,                                          # pylint: disable=E1101
                           version.build_version_string(),
                          )

    @staticmethod
    def version_identity(version_string):
        v1 = Version(version_string)
        v2 = Version(version_string)
        tools.assert_equal(v1,                                                      # pylint: disable=E1101
                           v2,
                          )

    def test_build_version_string1(self):
        self.version_string_identity('1.2.3a4')

    def test_build_version_string2(self):
        self.version_string_identity('10.2.3')

    def test_build_version_string3(self):
        self.version_string_identity('0.20.0b0')

    def test_build_version_string4(self):
        self.version_string_identity('7.2.180')

    def test_identity1(self):
        self.version_identity('3.4.55')

    def test_identity2(self):
        self.version_identity('0.2.0')

    def test_identity3(self):
        self.version_identity('6.41.1c3')

    def test_identity4(self):
        self.version_identity('7.0.0a1')

    def test_identity5(self):
        self.version_identity('7.0.0a0')

    def test_parse_validation1(self):
        self.assert_raises(ScriptException,
                           'Error in parsing version string 00.4.55. Result 0.4.55.',
                           self.version_identity,
                           '00.4.55',
                          )

    def test_parse_validation2(self):
        self.assert_raises(ScriptException,
                           "Invalid version string '18.10.20X32'  Result: '18.10.20'",
                           self.version_identity,
                           '18.10.20X32',
                          )

    def test_parse_validation3(self):
        self.assert_raises(ScriptException,
                           'Error in parsing version string 10.0.00. Result 10.0.0.',
                           self.version_identity,
                           '10.0.00',
                          )

    def test_parse_validation4(self):
        self.assert_raises(ScriptException,
                           'Error in parsing version string 6.41.01. Result 6.41.1.',
                           self.version_identity,
                           '6.41.01',
                          )

    def test_parse_validation5(self):
        self.assert_raises(ScriptException,
                           "Invalid version string 0.2",
                           self.version_identity,
                           '0.2',
                          )

    def test_parse_validation6(self):
        self.assert_raises(ScriptException,
                           'Error in parsing version string 6.41.01a5. Result 6.41.1a5.',
                           self.version_identity,
                           '6.41.01a5',
                          )

    def test_parse_validation7(self):
        self.assert_raises(ScriptException,
                           "Invalid version string 0.2b2",
                           self.version_identity,
                           '0.2b2',
                          )

    def test_parse_validation8(self):
        self.assert_raises(ScriptException,
                           "Invalid version string '6.41.01A5'  Result: '6.41.01'",
                           self.version_identity,
                           '6.41.01A5',
                          )

    def test_parse_validation9(self):
        self.assert_raises(ScriptException,
                           "Invalid version string 0.2B12",
                           self.version_identity,
                           '0.2B12',
                          )

class TestVersionIncrement(Base):

    ERROR_MESSAGES = {
        'ERR1' : "Must specify an increment type (major, minor, micro) when incrementing a non-development build to a development build.",
        'ERR2' : "Can not specify a development version of a normal release.",
        'ERR3' : "Can't go from beta to alpha of the same version. Specify an increment type (major, minor, micro).",
        'ERR4' : "Can't go from release candidate to alpha of the same version. Specify an increment type (major, minor, micro).",
        'ERR5' : "Can't go from release candidate to beta of the same version. Specify an increment type (major, minor, micro).",
    }

    def __init__(self):
        Base.__init__(self)

    @staticmethod
    def try_increment(version_object,
                      increment_type,
                      release_type,
                      expected_incremented_version_string,
                     ):
        incremented_object = version_object.increment_and_return_new(increment_type,
                                                                     release_type,
                                                                    )

        version_object.increment_in_place(increment_type,
                                          release_type,
                                         )

        tools.assert_equal(version_object, incremented_object)                                          # pylint: disable=E1101

        version_object_string = str(version_object)
        incremented_object_string = str(incremented_object)

        tools.assert_equal(version_object_string, expected_incremented_version_string)                  # pylint: disable=E1101
        tools.assert_equal(incremented_object_string, expected_incremented_version_string)              # pylint: disable=E1101


    def test_all_version_increments(self):
        increment_types = (Version.MAJOR_VERSION,              # 10
                           Version.MINOR_VERSION,              # 20
                           Version.MICRO_VERSION,              # 30
                           Version.DEVELOPMENT_VERSION,        # 40
                          )

        release_types = (Version.ALPHA_RELEASE,                # 50
                         Version.BETA_RELEASE,                 # 60
                         Version.CANDIDATE_RELEASE,            # 70
                         Version.NORMAL_RELEASE,               # 80
                        )

        test_table = (
            ('3.1.0',
             (
                ('4.0.0a1',     '4.0.0b1',      '4.0.0c1',      '4.0.0'     ),
                ('3.2.0a1',     '3.2.0b1',      '3.2.0c1',      '3.2.0'     ),
                ('3.1.1a1',     '3.1.1b1',      '3.1.1c1',      '3.1.1'     ),
                ('ERR1',        'ERR1',         'ERR1',         'ERR2'      ),
             )
            ),
            ('4.6.1a2',
             (
                ('5.0.0a1',     '5.0.0b1',      '5.0.0c1',      '5.0.0'     ),
                ('4.7.0a1',     '4.7.0b1',      '4.7.0c1',      '4.7.0'     ),
                ('4.6.2a1',     '4.6.2b1',      '4.6.2c1',      '4.6.2'     ),
                ('4.6.1a3',     '4.6.1b1',      '4.6.1c1',      '4.6.1'     ),
             )
            ),
            ('4.6.1b2',
             (
                ('5.0.0a1',     '5.0.0b1',      '5.0.0c1',      '5.0.0'     ),
                ('4.7.0a1',     '4.7.0b1',      '4.7.0c1',      '4.7.0'     ),
                ('4.6.2a1',     '4.6.2b1',      '4.6.2c1',      '4.6.2'     ),
                ('ERR3',        '4.6.1b3',      '4.6.1c1',      '4.6.1'     ),
             )
            ),
            ('4.6.1c2',
             (
                ('5.0.0a1',     '5.0.0b1',      '5.0.0c1',      '5.0.0'     ),
                ('4.7.0a1',     '4.7.0b1',      '4.7.0c1',      '4.7.0'     ),
                ('4.6.2a1',     '4.6.2b1',      '4.6.2c1',      '4.6.2'     ),
                ('ERR4',        'ERR5',         '4.6.1c3',      '4.6.1'     ),
             )
            ),
            ('0.0.0',
             (
                ('1.0.0a1',     '1.0.0b1',      '1.0.0c1',      '1.0.0'     ),
                ('0.1.0a1',     '0.1.0b1',      '0.1.0c1',      '0.1.0'     ),
                ('0.0.1a1',     '0.0.1b1',      '0.0.1c1',      '0.0.1'     ),
                ('ERR1',        'ERR1',         'ERR1',         'ERR2'      ),
             )
            ),
            ('18.21.0',
             (
                ('19.0.0a1',    '19.0.0b1',     '19.0.0c1',     '19.0.0'    ),
                ('18.22.0a1',   '18.22.0b1',    '18.22.0c1',    '18.22.0'   ),
                ('18.21.1a1',   '18.21.1b1',    '18.21.1c1',    '18.21.1'   ),
                ('ERR1',        'ERR1',         'ERR1',         'ERR2'      ),
             )
            ),
            ('8.9.1c32',
             (
                ('9.0.0a1',     '9.0.0b1',      '9.0.0c1',      '9.0.0'     ),
                ('8.10.0a1',    '8.10.0b1',     '8.10.0c1',     '8.10.0'    ),
                ('8.9.2a1',     '8.9.2b1',      '8.9.2c1',      '8.9.2'     ),
                ('ERR4',        'ERR5',         '8.9.1c33',     '8.9.1'     ),
             )
            ),
        )

        for version_number, result_table in test_table:
            for i in range(len(increment_types)):
                for j in range(len(release_types)):
                    increment_type = increment_types[i]
                    release_type = release_types[j]
                    expected_result = result_table[i][j]
                    yield (
                        self.run_allow_error,
                        version_number,
                        increment_type,
                        release_type,
                        expected_result,
                    )

    def run_allow_error(self,
                        version_number,
                        increment_type,
                        release_type,
                        expected_result,
                       ):
        if expected_result.startswith('ERR'):
            #print
            #print "Expected Result"
            #print expected_result
            expected_error = self.ERROR_MESSAGES[expected_result]
            self.assert_raises(
                ScriptException,
                expected_error,
                self.try_increment,
                Version(version_number),
                increment_type,
                release_type,
                expected_result,
            )
        else:
            self.try_increment(
                Version(version_number),
                increment_type,
                release_type,
                expected_result,
            )


#
#                  R E L E A S E   T Y P E
#
#        3.1.0     alpha       beta        candidate   normal
#
# I      major     4.0.0a1     4.0.0b1     4.0.0c1     4.0.0
# N
# C  T   minor     3.2.0a1     3.2.0b1     3.2.0c1     3.2.0
# R  Y
# E  P   micro     3.1.1a1     3.1.1b1     3.1.1c1     3.1.1
# M  E
# E      dev       error       error       error       error - When you specify a development increment, you can't
# N                  |           |           |                 go from one normal release to another.
# T                  |           |           |
#                  Must specify an increment type when incrementing a
#                  non-development build to a development build. Can't
#                  go from 3.1.0 to 3.1.0a1 (that's going backwards)
#
#
#        4.6.1a2   alpha       beta        candidate   normal
#
#        major     5.0.0a1     5.0.0b1     5.0.0c1     5.0.0
#
#        minor     4.7.0a1     4.7.0b1     4.7.0c1     4.7.0
#
#        micro     4.6.2a1     4.6.2b1     4.6.2c1     4.6.2
#
#        dev       4.6.1a3     4.6.1b1     4.6.1c1     4.6.1
#
#
#
#        4.6.1b2   alpha       beta        candidate   normal
#
#        major     5.0.0a1     5.0.0b1     5.0.0c1     5.0.0
#
#        minor     4.7.0a1     4.7.0b1     4.7.0c1     4.7.0
#
#        micro     4.6.2a1     4.6.2b1     4.6.2c1     4.6.2
#
#        dev       error       4.6.1b3     4.6.1c1     4.6.1
#                    |
#                    |
#                  Can't go from beta to alpha of the same version
#
#
#        4.6.1c2   alpha       beta        candidate   normal
#
#        major     5.0.0a1     5.0.0b1     5.0.0c1     5.0.0
#
#        minor     4.7.0a1     4.7.0b1     4.7.0c1     4.7.0
#
#        micro     4.6.2a1     4.6.2b1     4.6.2c1     4.6.2
#
#        dev       error       error       4.6.1c3     4.6.1
#                    |           |
#                    |           |
#                    |         Can't go from candidate to beta of the same version
#                    |
#                  Can't go from candidate to alpha of the same version










#
