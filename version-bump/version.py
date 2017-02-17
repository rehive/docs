#!/usr/bin/env python

# The above shebang line is compatible with virtualenv.

"""
    version.py

    Provides the Version class, which stores and increments version numbers.
"""

# Pylint command line
# pylint --rcfile=/home/parts_admin/projects/pick_pack/wc/App/.pylintrc ~/projects/dev_utils/wc/python/version.py | o

import re

from script_exception import ScriptException

class Version(object):
    """
    Holder for version information
    """

    MAJOR_VERSION = 10
    MINOR_VERSION = 20
    MICRO_VERSION = 30
    DEVELOPMENT_VERSION = 40
    ALPHA_RELEASE = 50
    BETA_RELEASE = 60
    CANDIDATE_RELEASE = 70
    NORMAL_RELEASE = 80

    def __init__(self,
                 version_string = None,
                 version_object = None,
                ):
        if version_string is not None and version_object is not None:
            err_msg = "Can't supply both version_string and version_object."
            raise ScriptException(err_msg)
        elif version_string is not None:
            (self.major,
             self.minor,
             self.micro,
             self.release_type,
             self.release_version,
            ) = self.parse_version_string(version_string)
        elif version_object is not None:
            self.major = version_object.major
            self.minor = version_object.minor
            self.micro = version_object.micro
            self.release_type = version_object.release_type
            self.release_version = version_object.release_version
        else:
            self.major = 0
            self.minor = 0
            self.micro = 0
            self.release_type = self.NORMAL_RELEASE
            self.release_version = 1

        if self.major is None:
            err_msg = "Major version number is None."
            raise ScriptException(err_msg)
        if self.minor is None:
            err_msg = "Minor version number is None."
            raise ScriptException(err_msg)
        if self.micro is None:
            err_msg = "Micro version number is None."
            raise ScriptException(err_msg)
        if self.release_type is None:
            err_msg = "Release type is None."
            raise ScriptException(err_msg)
        if self.release_type not in (
            self.NORMAL_RELEASE,
            self.ALPHA_RELEASE,
            self.BETA_RELEASE,
            self.CANDIDATE_RELEASE,
        ):
            err_msg = "Unknown release type %s" % self.release_type
            raise ScriptException(err_msg)
        if self.release_version is None:
            err_msg = "Release version number is None."
            raise ScriptException(err_msg)

    def __eq__(self,
               other,
              ):
        return (self.major == other.major
                and self.minor == other.minor
                and self.micro == other.micro
                and self.release_type == other.release_type
                and self.release_version == other.release_version
               )

    def __ne__(self,
               other,
              ):
        return not self.__eq__(other)

    def __str__(self):
        return self.build_version_string()

    def build_version_string(self):
        """
        Return a string that represents the version.
        """
        return self._build_version_string(self.major,
                                          self.minor,
                                          self.micro,
                                          self.release_type,
                                          self.release_version,
                                         )

    def _build_version_string(self,
                              major,
                              minor,
                              micro,
                              release_type,
                              release_version,
                             ):
        if release_type == self.NORMAL_RELEASE:
            release_text = ""
        elif release_type == self.ALPHA_RELEASE:
            release_text = "a%s" % release_version
        elif release_type == self.BETA_RELEASE:
            release_text = "b%s" % release_version
        elif release_type == self.CANDIDATE_RELEASE:
            release_text = "c%s" % release_version
        else:
            err_msg = "Unknown release type '%s'" % release_type
            raise ScriptException(err_msg)

        return "%s.%s.%s%s" % (major,
                               minor,
                               micro,
                               release_text,
                              )

    def parse_version_string(self,
                             version_string,
                            ):
        """
        Regular expression to split up the components of a version string, such
        as 2.3.18b2.
        """
        version_regex = re.compile(r'^(?P<major>[0-9]+)\.(?P<minor>[0-9]+)\.(?P<micro>[0-9]+)(?P<release_type>[abc]?)(?P<release_version>[0-9]*)')
        match_obj = version_regex.match(version_string)
        if match_obj is None:
            err_msg = "Invalid version string %s" % version_string
            raise ScriptException(err_msg)

        # Make sure all the string was consumed
        groups = match_obj.groupdict()
        matched_string = "%s.%s.%s%s%s" % (groups['major'],
                                           groups['minor'],
                                           groups['micro'],
                                           groups['release_type'],
                                           groups['release_version'],
                                          )
        if  match_obj.string != version_string:
            err_msg = "String changed during match '%s' Result:  '%s'" % (match_obj.string,
                                                                          version_string,
                                                                         )
            raise ScriptException(err_msg)
        if matched_string != match_obj.string:
            err_msg = "Invalid version string '%s'  Result: '%s'" % (match_obj.string,
                                                                     matched_string,
                                                                    )
            raise ScriptException(err_msg)


        major = int(match_obj.group('major'))
        minor = int(match_obj.group('minor'))
        micro = int(match_obj.group('micro'))

        release_type = match_obj.group('release_type')
        if release_type == '':
            release_type_constant = self.NORMAL_RELEASE
        elif release_type == 'a':
            release_type_constant = self.ALPHA_RELEASE
        elif release_type == 'b':
            release_type_constant = self.BETA_RELEASE
        elif release_type == 'c':
            release_type_constant = self.CANDIDATE_RELEASE
        else:
            err_msg = "Unknown release type %s" % release_type
            raise ScriptException(err_msg)

        release_version = match_obj.group('release_version')
        if release_version == '':
            release_version = 1
        else:
            release_version = int(release_version)

        # Roudtrip check
        calculated_version_string = self._build_version_string(major,
                                                               minor,
                                                               micro,
                                                               release_type_constant,
                                                               release_version,
                                                              )
        if calculated_version_string != version_string:
            err_msg = "Error in parsing version string %s. Result %s." % (version_string,
                                                                          calculated_version_string,
                                                                         )
            raise ScriptException(err_msg)


        return (major,
                minor,
                micro,
                release_type_constant,
                release_version,
               )

    # pylint: disable=R0912
    # Too many branches
    def increment_in_place(self,
                           increment_type,
                           release_type,
                          ):
        """
        Increments the version in place, according to increment_type and
        release_type.

        Examples:

                  R E L E A S E   T Y P E

        3.1.0     alpha       beta        candidate   normal

 I      major     4.0.0a1     4.0.0b1     4.0.0c1     4.0.0
 N
 C  T   minor     3.2.0a1     3.2.0b1     3.2.0c1     3.2.0
 R  Y
 E  P   micro     3.1.1a1     3.1.1b1     3.1.1c1     3.1.1
 M  E
 E      dev       error       error       error       error - When you specify a development increment, you can't
 N                  |           |           |                 go from one normal release to another.
 T                  |           |           |
                  Must specify an increment type when incrementing a
                  non-development build to a development build. Can't
                  go from 3.1.0 to 3.1.0a1 (that's going backwards)


        4.6.1a2   alpha       beta        candidate   normal

        major     5.0.0a1     5.0.0b1     5.0.0c1     5.0.0

        minor     4.7.0a1     4.7.0b1     4.7.0c1     4.7.0

        micro     4.6.2a1     4.6.2b1     4.6.2c1     4.6.2

        dev       4.6.1a3     4.6.1b1     4.6.1c1     4.6.1



        4.6.1b2   alpha       beta        candidate   normal

        major     5.0.0a1     5.0.0b1     5.0.0c1     5.0.0

        minor     4.7.0a1     4.7.0b1     4.7.0c1     4.7.0

        micro     4.6.2a1     4.6.2b1     4.6.2c1     4.6.2

        dev       error       4.6.1b3     4.6.1c1     4.6.1
                    |
                    |
                  Can't go from beta to alpha of the same version


        4.6.1c2   alpha       beta        candidate   normal

        major     5.0.0a1     5.0.0b1     5.0.0c1     5.0.0

        minor     4.7.0a1     4.7.0b1     4.7.0c1     4.7.0

        micro     4.6.2a1     4.6.2b1     4.6.2c1     4.6.2

        dev       error       error       4.6.1c3     4.6.1
                    |           |
                    |           |
                    |         Can't go from candidate to beta of the same version
                    |
                  Can't go from candidate to alpha of the same version
        """

        # Validate arguments
        if increment_type not in (
            self.MAJOR_VERSION,
            self.MINOR_VERSION,
            self.MICRO_VERSION,
            self.DEVELOPMENT_VERSION,
        ):
            err_msg = "Invalid increment type %s" % increment_type
            raise ScriptException(err_msg)

        if release_type not in (
            self.NORMAL_RELEASE,
            self.ALPHA_RELEASE,
            self.BETA_RELEASE,
            self.CANDIDATE_RELEASE,
        ):
            err_msg = "Invalid release type %s" % release_type
            raise ScriptException(err_msg)

        # Flag invalid combinations
        if increment_type == self.DEVELOPMENT_VERSION:

            if self.release_type == self.NORMAL_RELEASE:
                if release_type == self.NORMAL_RELEASE:
                    err_msg = "Can not specify a development version of a normal release."
                    raise ScriptException(err_msg)
                else:
                    # Can't go from 3.1.0 to 3.1.0a1 (that's going backwards)
                    err_msg = "Must specify an increment type (major, minor, micro) when incrementing a non-development build to a development build."
                    raise ScriptException(err_msg)

            if (self.release_type == self.BETA_RELEASE and
                release_type == self.ALPHA_RELEASE
               ):
                err_msg = "Can't go from beta to alpha of the same version. Specify an increment type (major, minor, micro)."
                raise ScriptException(err_msg)

            if (self.release_type == self.CANDIDATE_RELEASE and
                release_type == self.ALPHA_RELEASE
               ):
                err_msg = "Can't go from release candidate to alpha of the same version. Specify an increment type (major, minor, micro)."
                raise ScriptException(err_msg)

            if (self.release_type == self.CANDIDATE_RELEASE and
                release_type == self.BETA_RELEASE
               ):
                err_msg = "Can't go from release candidate to beta of the same version. Specify an increment type (major, minor, micro)."
                raise ScriptException(err_msg)

        # Increment as needed
        if increment_type == self.MAJOR_VERSION:
            self.major += 1
            self.minor = 0
            self.micro = 0
            self.release_version = 1
        elif increment_type == self.MINOR_VERSION:
            self.minor += 1
            self.micro = 0
            self.release_version = 1
        elif increment_type == self.MICRO_VERSION:
            self.micro += 1
            self.release_version = 1
        elif increment_type == self.DEVELOPMENT_VERSION:
            if (self.release_type == release_type):
                # We are making another release of the same type (alpha, beta,
                # candidate). So, increment the release number.
                self.release_version += 1
            else:
                # We are moving to a more mature release type (e.g alpha to
                # beta). Reset the release number to 1. Note that attempts to
                # go in reverse (beta to alpha) would have rased an error
                # earlier.
                self.release_version = 1

        self.release_type = release_type

    def increment_and_return_new(self,
                                 increment_type,
                                 release_type,
                                ):
        """
        Creates a new Version object based on this one (self). Increments the
        new Version object according to increment_type and release_type. Returns
        the new Version object with the incremented values.
        """
        new_version = Version(version_object = self)
        new_version.increment_in_place(increment_type,
                                       release_type,
                                      )
        return new_version
