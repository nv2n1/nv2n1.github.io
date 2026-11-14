---
title: "gpt-build(8)"
name: "gpt-build"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-build/"
description: "gpt-build – Builds and installs GPT source packages and bundles."
---

<p><code>gpt-build</code> &#8211; Builds and installs <font SIZE="-1">GPT</font> source packages and bundles.</p>
<h2>Synopsis</h2>
<p><code>gpt-build</code> [options] [macros] [source packages] flavors &#8230; </p>
<pre> Options:
 -verbose Print copious output
 -help Print usage
 -man Print man page.
 -version Print GPT version.
 -installdir=path_to_installation Override $GLOBUS_LOCATION
 -builddir=path_to_build directory Directory to unpack tarfiles
 -logdir=log_file_directory Directory for package logs
 -srcdir=source_directory Directory containing a source package
 -static Build static executables
 -force Force rebuilds
 -update Rebuild if newer
 -disable-version-checking Ignore versions in package dependencies.
 -std-flavors Build all std flavors.
 -all-flavors Build all of the flavors
 -coresrc Override installed globus_core pkg
 -nosrc Only install the flavors
 [macro=value] Macro definitions
 [list of flavors to build] Flavors that define the build options
 [list of source packages] Tarfiles of source bundles or packages</pre>
<h2>Description</h2>
<p><code>gpt-build</code> Builds and installs software from source distributions. The script reads the build instructions for each source distribution from a package metadata file called pkg_data_src.gpt. If no instructions are found the script uses the default instructions described in <i>Grid::GPT::PkgMngmt::Build</i>. </p>
<p> Multiple packages can be built by passing in multiple <i>-srcdir</i> arguments or multiple source packages and or bundles. For now these have to be passed in in dependent order ie. if package foo needs package fee&#8217;s headers to build then fee should come first. </p>
<p> gpt-build does not create binary packages as globus-build does. This is done by a seperate script called <i>gpt-pkg</i>.</p>
<h2>Flavors</h2>
<p>Build flavors are character string labels that represent a set of compiler and linker options defined during the building of the globus_core package. Predefined flavors can be listed by using the <code>gpt-flavor-configuration</code> script. Packages can be built with any installed flavor. globus_core can only be built with pre-defined flavors. globus_core needs to be built by hand (i.e. ./configure|make|make install) to install a custom build flavor.</p>
<h2>Files In Pgm Packages</h2>
<p>Installed files such as executables that are found in pgm and ptm_static packages will overwrite one another when multiple flavors of the same package are built. Thus only the files from the last flavor built will be present after a gpt-build run. To preserve multiple flavors of these files, they are automatically copied into flavored subdirectories. For example, the program <tt>$GLOBUS_LOCATION</tt>/bin/foo will be copied into the location <tt>$GLOBUS_LOCATION</tt>/bin/gcc32/shared if it was built with dynamically with the gcc32 flavor. These files are retrieved by <i>gpt-pkg</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-srcdir</code></p>
<dd>Specifies the where the source directory is. This is used by developers to build out of a repository..</p>
<dt><code>-installdir</code></p>
<dd>Specifies the where the install directory is. This directory will be where the targets are installed before being archived. Note that this directory needs contain the installation targets of all of the packages which satisfy build dependencies in addition to the installation targets of the package being built. Because of this, installation targets are not removed after the package is archived. Because different flavors of program packages conflict with each other, the last flavor built is the flavor of the installed files. For each flavor, gpt-build makes a copy of each installed file in a program package and puts the copy in a flavored subdirectory.</p>
<dt><code>-builddir</code></p>
<dd>Specifies the where the source tar files should be untarred and the code is built.</p>
<dt><code>-force</code></p>
<dd>Tells <code>gpt-build</code> to rebuild a package even if it is already installed. The default behavior is to skip any packages that have been built before.</p>
<dt><code>-update</code></p>
<dd>Tells <code>gpt-build</code> to build even if an older version is installed.</p>
<dt><code>-verbose</code></p>
<dd>Prints out all of the build messages.</p>
<dt><code>-std-flavors</code></p>
<dd>Build the globus_core package with all of the flavor choices marked as standard in the flavor configuration file. All of the other packages will be built with all of the flavors sucessfully installed by globus_core.</p>
<dt><code>-all-flavors</code></p>
<dd>Build the globus_core package with all of the flavor choices marked as standard in the flavor configuration file. All of the other packages will be built with all of the flavors sucessfully installed by globus_core.</p>
<dt><code>-nosrc</code></p>
<dd>Just install the listed flavors. Don&#8217;t build any source code.</p>
<dt><code>-coresrc</code></p>
<dd>Use this version of globus_core source rather than the one found in <tt>$GPT_LOCATION</tt>/share/globus/globus_core-src.tar.gz.</p>
<dt><code>-disable-version-checking</code></p>
<dd><font SIZE="-1">GPT</font> 1.x scripts neglected to check the version numbers of packages during dependency checks. Because of this <font SIZE="-1">GPT</font> bundles were released that have errors in their dependency data. This flag is provided so that these packages can still be used. <font SIZE="-1"><code>NOTE</code></font> that once this flag is used, the version checking is disabled <code>permanently</code> for the installation pointed to by <tt>$GLOBUS_LOCATION</tt>. This condition can only be removed by deleting the file <tt>$GLOBUS_LOCATION</tt>/share/globus/disable_version_checking.</p>
<dt><code>-flavor-cfg=FILE</code></p>
<dd>Use the flavor configurations found in <font SIZE="-1">FILE</font>. The default configuration file is <tt>$GPT_LOCATION</tt>/share/globus/globus_flavor_labels.conf</p>
<dt><code>-logdir=DIRECTORY</code></p>
<dd>Store package logs of build messages in <font SIZE="-1">DIRECTORY</font>. This option also sets -verbose. The default directory is ./logs.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</dl>
<h2>Macros</h2>
<p>Build macros are perl routines and variables that are used by gpt-build while building packages. These macros are embedded in the build instructions part of the package&#8217;s metadata file. Some of these macros can be set from the command line using the following format: </p>
<pre> &lt;NAME&gt;_GPTMACRO='new value'</pre>
<p>Note that even though this feature seems extremely flexible, it has not been thoroughly tested mainly because the authors have not been able to figure out what people will want to do with these macros. Further details are found in the <code>Grid::GPT::PkgMngmt::BuildMacros</code> manpage.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-gpt-pkg/">gpt-pkg</a></i>(8) <i><a href="/docs/linux/man/8-gpt-bundle/">gpt-bundle</a></i>(8) <i><a href="/docs/linux/man/8-gpt-install/">gpt-install</a></i>(8) <i><a href="/docs/linux/man/3-buildmacros/">BuildMacros</a></i>(3)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;blau.mcs.anl.gov&gt;</p>
