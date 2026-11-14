---
title: "gpt-pkg(8)"
name: "gpt-pkg"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-pkg/"
description: "gpt-pkg – Creates flavored binary packages out of an installation"
---

<p><code>gpt-pkg</code> &#8211; Creates flavored binary packages out of an installation</p>
<h2>Synopsis</h2>
<p><code>gpt-pkg</code> [options] packages </p>
<pre> Options:
 -verbose Print copious output
 -help Print usage
 -man Print man page.
 -version Print GPT version.
 -native Create native pkgs as well as GPT pkgs (RPMs only).
 -all Archive everything in the package directory..
 -installdir=PATH Override $GLOBUS_LOCATION
 -pkgdir=PATH Directory to put the packages
 -rpmprefix=PATH Absolute path encoded in the RPM.
 -buildnumber=NUMBER Build number used for pgm_static packages
 -rpmlicense=LABEL License Label added to the RPM header
 [packages] List of packages to be archived</pre>
<h2>Description</h2>
<p><code>gpt-pkg</code> Creates binary packages from an installation. The installation needs to contain <font SIZE="-1">GPT</font> packaging data files. An installation is created by running <i>gpt-build</i> on a collection of source packages or bundles.</p>
<h2>Files In Pgm Packages</h2>
<p>Installed files such as executables that are found in pgm and ptm_static packages will overwrite one another when multiple flavors of the same package are built by gpt-build. To preserve multiple flavors of these files, gpt-build copies them into flavored subdirectories. For example, the program <tt>$GLOBUS_LOCATION</tt>/bin/foo will be copied into the location <tt>$GLOBUS_LOCATION</tt>/bin/gcc32/shared if it was built with dynamically with the gcc32 flavor. <code>gpt-pkg</code> retrieves these files and copies them back to their proper location before packaging them. Thus gpt-pkg will also overwrite these files as it archives the different flavors of a pgm package.</p>
<h2>Options</h2>
<dl>
<dt><code>-installdir</code></p>
<dd>Specify the directory in which the installed files currently live. If this argument is not supplied, the value of the environment variable <font SIZE="-1">GLOBUS_LOCATION</font> is used instead.</p>
<dt><code>-all</code></p>
<dd>Packages all of the binaries in an installation.</p>
<dt><code>-native</code></p>
<dd>Creates a package in the native packaging format. Currently only rpm is supported.</p>
<dt><code>-rpmprefix=&lt;path_to_installation</code>&gt;</p>
<dd>This should be set to the path to your <font SIZE="-1">GLOBUS_LOCATION</font>. <font SIZE="-1">GPT</font> will use a value of &#8220;/usr/grid&#8221; if this option is not specified.</p>
<dt><code>-rpmlicense=&lt;label</code>&gt;</p>
<dd>Provides an alternate copyright label for the rpms. The default is whatever <font SIZE="-1">GPT</font> was configured with.</p>
<dt><code>-verbose</code></p>
<dd>Prints out all of the build messages.</p>
<dt><code>-log=FILE</code></p>
<dd>Appends all of the build messages to <font SIZE="-1">FILE</font>. This option also sets -verbose.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</dl>
<h2>pgm and pgm_static packages</h2>
<p>gpt-build copies the files for these packages in a flavored location because different flavors of these types of packages will conflict with each other. <code>gpt-pkg</code> restores these files when it packages pgm and pgm_static types.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-gpt-bundle/">gpt-bundle</a></i>(8) <i><a href="/docs/linux/man/8-gpt-install/">gpt-install</a></i>(8) <i><a href="/docs/linux/man/8-gpt-build/">gpt-build</a></i>(8)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;blau.mcs.anl.gov&gt;</p>
