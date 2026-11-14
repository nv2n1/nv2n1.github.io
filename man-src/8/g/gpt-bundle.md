---
title: "gpt-bundle(8)"
name: "gpt-bundle"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-bundle/"
description: "gpt-bundle – Creates binary or source bundles from an installation or a collection of source packages."
---

<p><code>gpt-bundle</code> &#8211; Creates binary or source bundles from an installation or a collection of source packages.</p>
<h2>Synopsis</h2>
<p><code>gpt-bundle</code> [options] packages </p>
<pre> Options:
 -verbose Print copious output
 -help Print usage
 -man Print man page.
 -version Print GPT version.
 -srcdir=PATH Directory containing source packages
 -tmpdir=PATH Directory used to create binary packages
 -installdir=PATH Directory containing an installation
 -bn=NAME Name of the bundle
 -bv=MAJOR.MINOR Version of the bundle
 -bs=STABILITY Stability of the bundle contents
 -bl=VERSION Version Label of the bundle
 -native Create bundles of native pkgs (RPMs only).
 -all Bundle everything in the package directory..
 -nodeps Don't include any dependent packages.
 -nosetups Don't include dependent setup packages.
 -template Outputs empty Bundle Def XML file. 
 -bundledef=FILE Outputs XML file with command line values. 
 -exclude=PACKAGE Don't include PACKAGE in bundle
 -config=FILE Use bundle options stored in FILE
 -xml=FILE XML bundle description file
 -output=FILE Name of the bundle file,
 -rpmprefix=PATH Absolute path encoded in the RPM.
 -buildnumber=NUMBER Build number used for pgm_static packages
 -rpmlicense=LABEL License Label added to the RPM header
 [packages] List of packages to be bundled</pre>
<h2>Description</h2>
<p><code>gpt-bundle</code> Creates binary or source bundles from an installation or a collection of source packages. These bundles can then distributed be installed using <i>gpt-install</i> or <i>gpt-build</i>. A bundle consists of a collection of packages and a <font SIZE="-1">XML</font> formatted description file. The <font SIZE="-1">DTD</font> for this file is found in <i></i>$GPT_LOCATION<i>/share/dtd/gpt_bundle.dtd</i>. </p>
<p> The script accepts a list of packages from the command line or from an inputed bundle description file. It expands this list to include all of the packages that the listed packages depend on. It then uses this expanded list to create a new bundle description file which is then added to the collection of packages to form a bundle. </p>
<p> <code>gpt-bundle</code> assumes that all of the packages needed to create a source bundle are found in one subdirectory identified by the <i>-srcdir</i> switch. </p>
<p> <code>gpt-bundle</code> assumes that all of the packages need to create a binary bundle are installed in a location identified by the <i>-installdir</i> flag or <tt>$GLOBUS_LOCATION</tt>. </p>
<p> The list of packages that can be entered from the command line are of the form <i></i><font SIZE="-1"><i>NAME-FLAVOR-PACKAGE_TYPE</i></font><i></i>. The wildcard character &#8216;*&#8217; can also be used.</p>
<h2>Options</h2>
<dl>
<dt><code>-srcdir=PATH</code></p>
<dd>Specifies where the directory containing your source packages is. If this is used, a source bundle will be created. Note that this flag is required to create source bundles.</p>
<dt><code>-installdir=PATH</code></p>
<dd>Specifies where the installation used for creating binary bundles is. <tt>$GLOBUS_LOCATION</tt> is the default.</p>
<dt><code>-xml=FILE</code></p>
<dd>Specifies the input bundle description file. A new file will be generated using the contents of this file and included in the bundle.</p>
<dt><code>-bundlename=NAME</code></p>
<dd>The name of the bundle. This name is stored in the bundle description file and used as part of the bundle filename if <code>-output</code> is not specified.</p>
<dt><code>-bundleversion=MAJOR.MINOR</code></p>
<dd>This is the bundle version number. It is stored in the bundle description file and used for bundle updates. It is also used for the bundle filename if <code>-bundlelabel</code> is not specified.</p>
<dt><code>-bundlelabel=VERSION</code></p>
<dd>This is the bundle version label. It is stored in the bundle description file as a string and so can accomodate any versioning scheme. The label is used in user queries, and as part of the bundle filename.</p>
<dt><code>-bundlestability=STABILITY</code></p>
<dd>This is the bundle version stability. It is a field that is used to indicate the stability of this version of the bundle. The field can have values of <code>experimental</code>, <code>alpha</code>, <code>beta</code>, or <code>production</code>. The default vaule is experimental. The field is stored in the bundle description file and used for user queries.</p>
<dt><code>-tmpdir=PATH</code></p>
<dd>Specifies the where the directory is that <code>gpt-bundle</code> should use to store generated binary packages.</p>
<dt><code>-all</code></p>
<dd>Tells <code>gpt-bundle</code> to bundle all of the packages in the source package directory or installation.</p>
<dt><code>-native</code></p>
<dd>Tells <code>gpt-bundle</code> to also bundle packages that are in the native format of the operating system. Presently this only works for <font SIZE="-1">RPMS</font> on linux. <code>gpt-bundle</code> will output two bundle giving the native bundle a platform specific extension such as -rpm.</p>
<dt><code>-nodeps</code></p>
<dd>Tells <code>gpt-bundle</code> to only include the packages specified&#8212;do not check for or include dependencies.</p>
<dt><code>-nosetups</code></p>
<dd>Tells <code>gpt-bundle</code> to exclude any packages that are pulled in by a setup dependencies. Note that setup packages that are listed on the command line will still be added to the bundle..</p>
<dt><code>-exclude=package1,package2,&#8230;</code></p>
<dd>This option excludes the listed packages from the created bundle. It can be specified multiple times with the final listing used being an aggregate of all the listed packages. This option can be abbreviated as &#8216;-exclude=package1,package2,&#8230;&#8217;.</p>
<dt><code>-output=FILE</code></p>
<dd>This is an alternative way to specify the bundle name. The output file is put in the directory from which <code>gpt-bundle</code> was invoked if no path was given, in a directory relative it if a relative path was given, or in the absolute location, if given.</p>
<dt><code>-template</code></p>
<dd>Creates an empty Bundle <font SIZE="-1">XML</font> that can be modified and used to create a new bundle.</p>
<dt><code>-bundledef=FILE</code></p>
<dd>Creates an <font SIZE="-1">XML</font> file with name equal to <font SIZE="-1"><code>FILE</code></font>.gpt-bundle.xml. This file will contain a <font SIZE="-1">GPT</font> Bundle definition with values set to those passed in on the command line.</p>
<dt><code>-rpmprefix=&lt;path_to_installation</code>&gt;</p>
<dd>This should be set to the path to your <font SIZE="-1">GLOBUS_LOCATION</font>. <font SIZE="-1">GPT</font> will use a value of &#8220;/usr/grid&#8221; if this option is not specified.</p>
<dt><code>-rpmlicense=&lt;label</code>&gt;</p>
<dd>Provides an alternate copyright label for the rpms. The default is whatever <font SIZE="-1">GPT</font> was configured with.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-buildnumber=&lt;number</code>&gt;</p>
<dd>Build number used to version static packages.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</dl>
<h2>Bundle Definition File Overrides</h2>
<p>The <i>-bundle*</i> switches can be used to override content in the bundle definition file inputted by the <i>-xml</i> switch. The relationship between the switches and the bundle definition file contents is shown in the following table: </p>
<pre> I&lt;Switch&gt; I&lt;Element&gt; I&lt;Attribute&gt;
 -bundlename GPTBundleData Name
 -bundleversion BundleReleaseInfo Major, Minor
 -bundlelabel BundleReleaseInfo VersionLabel
 -bundlestability VersionStability Release</pre>
<h2>Bundle Names and Versions</h2>
<p><code>gpt-bundle</code> encourages a naming convention for bundle filenames. The convention can be overriden using the <i>-output</i> switch. The convention is as follows: </p>
<pre> NAME-VERSION-src_bundle.tar.gz for source bundles
 NAME-VERSION-ARCH-gpt.tar.gz for gpt binary bundles. ARCH is the platform ID.
 NAME-VERSION-ARCH-rpm.tar.gz for rpm binary bundles.</pre>
<p><font SIZE="-1">NAME</font> comes from the <i>-bundlename</i> switch. <font SIZE="-1">VERSION</font> comes from the <i>-bundlelabel</i> switch. If this switch is not used then <font SIZE="-1">VERSION</font> comes from the <i>-bundleversion</i> switch. </p>
<p> Unless overrided by the switches previously mentioned, the values for can also be extracted from the bundle definition file inputted by the <i>-xml</i> switch.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-gpt-build/">gpt-build</a></i>(8) <i><a href="/docs/linux/man/8-gpt-install/">gpt-install</a></i>(8) <i><a href="/docs/linux/man/8-gpt-pkg/">gpt-pkg</a></i>(8)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin [at] ncsa.uiuc.edu&gt;, Eric Blau &lt;blau [at] mcs.anl.gov&gt; and Patrick Duda &lt;pduda [at] ncsa.uiuc.edu&gt;</p>
