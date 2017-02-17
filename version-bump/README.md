version-bump
============

Simple python module to increment version numbers.


### Usage ###

```python
from version import Version

current_version = Version(version_string = '1.2.9')
new_version = current_version.increment_and_return_new(Version.MINOR_VERSION,
                                                       Version.NORMAL_RELEASE,
                                                      )

print('Current version string {}'.format(current_version))
print('Bumped version string {}'.format(new_version))

# Prints this
#   Current version string 1.2.9
#   Bumped version string 1.3.0
```

### Examples ###

When incrementing a version, you must specify what part of the version to increment
* Major
* Minor
* Micro
* Development

You must also specify what kind of release it is
* Alpha
* Beta
* Candidate
* Normal

Here are some examples of how these options work.

```
3.1.0     alpha       beta        candidate   normal

major     4.0.0a1     4.0.0b1     4.0.0c1     4.0.0

minor     3.2.0a1     3.2.0b1     3.2.0c1     3.2.0

micro     3.1.1a1     3.1.1b1     3.1.1c1     3.1.1

dev       error       error       error       error - When you specify a development increment, you can't
            |           |           |                 go from one normal release to another.
            |           |           |
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
```
