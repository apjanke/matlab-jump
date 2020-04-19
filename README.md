# JUMP for Matlab

Matlab-JUMP is a tool that makes it easier to write custom Java code for use in a Matlab environment.

JUMP stands for "Java Uniform Provision for Matlab". (Yes, I see that the "MP" is backwards. Artistic license.)

JUMP provides:

* Maven POMs with dependencies on the third-party JARs shipped with Matlab
* A convenient redistribution of the Javadoc for those libraries

JUMP's target audience is Matlab developers who want to write custom Java code for use in their Matlab libraries or applications, or Java developers who wish to specifically support Matlab as a deployment environment.

## Features

Matlab supports the use of Java code through its External Interfaces API. Matlab developers can write custom Matlab code that runs inside Matlab. But Matlab also bundles a large number of third-party open source libraries, and these are loaded into the Matlab's embedded JVM which your custom code runs in. This means that if you want to use these libraries, too, you need to use the exact versions that are shipped with Matlab. And those versions are often quite old, so coding against the current versions of these libraries will cause compatibility problems.

JUMP addresses this problem by providing Maven POMs that have dependencies on the exact versions of the third-party Java libraries that ship with a particular version of Matlab. In your custom Java code, include the JUMP project for your target version of Matlab. It will pull in all the Matlab-bundled libraries as dependencies.

JUMP also distributes a tarball that combines the Javadocs for all of those third-party Java libraries. This is convenient to install locally and use as a reference. When you Google for the doco for these Java libraries, you'll often get the wrong version, because the versions Matlab bundles are so old.

## Security Note

Matlab ships old versions of the Java libraries it uses. Some of these have security vulnerabilities in them. You may see security warnings on this repo or in your development tools when using these libraries. Nothing I can do about that, since the versions Matlab ships are fixed.

## Matlab Version Support

JUMP currently supports Matlab R2019b.
I will add support for all future versions of Matlab.
I'll also add support for specific older versions of Matlab, if a user requests it.
It takes a few hours of work to add support for a Matlab version, so I don't want to do that unless there are actual have user requests.

## Related Projects

Matlab-JUMP is part of the [Janklab](https://github.com/apjanke/janklab) suite of Matlab libraries.

The list of Matlab's third-party Java libraries and their versions can be detected using [matlab-jarext-inspector](https://github.com/apjanke/matlab-jarext-inspector).

## Author and Support

Matlab-JUMP is written and maintained by [Andrew Janke](https://apjanke.net).

The various open source libraries redistributed with JUMP are written by various authors and covered under various licenses; see the LICENSE.md file for details.

The project home page is <https://github.com/apjanke/matlab-jump>. Bug reports and feature requests are welcome, and may be filed on the issue tracker there on the project GitHub page.
