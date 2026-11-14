---
title: "dpkg-scanpackages(1)"
name: "dpkg-scanpackages"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-scanpackages/"
description: "dpkg-scanpackages – create Packages index files"
---

<h2 class="name">NAME</h2>
<p> dpkg-scanpackages &#8211; create Packages index files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-scanpackages</code> [<i>option</i>&#8230;] <i>binary-path</i> [<i>override-file</i> [<i>path-prefix</i>]] <code>&gt;</code> <i>Packages</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-scanpackages</code> sorts through a tree of Debian binary packages and creates a Packages file, used by <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8), <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1), etc, to tell the user what packages are available for installation. These Packages files are the same as those found on Debian archive sites and CD-ROMs. You might use <code>dpkg-scanpackages</code> yourself if making a directory of local packages to install on a cluster of machines. </p>
<p> <code>Note:</code> If you want to access the generated Packages file with <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) you will probably need to compress the file with <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) (generating a Packages.xz file), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) (generating a Packages.bz2 file) or <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) (generating a Packages.gz file). <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) ignores uncompressed Packages files except on local access (i.e. <code>file://</code> sources). </p>
<p> <i>binary-path</i> is the name of the tree of the binary packages to process (for example, <code>contrib/binary-i386</code>). It is best to make this relative to the root of the Debian archive, because every Filename field in the new Packages file will start with this string. </p>
<p> <i>override-file</i> is the name of a file to read which contains information about how the package fits into the distribution (the file can be compressed since dpkg 1.15.5); see <code><a href="/docs/linux/man/5-deb-override/">deb-override</a></code>(5). </p>
<p> <i>path-prefix</i> is an optional string to be prepended to the Filename fields. </p>
<p> If more than one version of a package is found only the newest one is included in the output. If they have the same version and only differ in architecture only the first one found is used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code>, <code>&#8211;type</code> <i>type</i></p>
<dd> Scan for *.<i>type</i> packages, instead of *.deb.</p>
<dt><code>-e</code>, <code>&#8211;extra-override</code> <i>file</i></p>
<dd> Scan <i>file</i> to find supplementary overrides (the file can be compressed since dpkg 1.15.5). See <code><a href="/docs/linux/man/5-deb-extra-override/">deb-extra-override</a></code>(5) for more information on its format.</p>
<dt><code>-a</code>, <code>&#8211;arch</code> <i>arch</i></p>
<dd> Use a pattern consisting of <i>*_all.deb</i> and <i>*_arch.deb</i> instead of scanning for all debs.</p>
<dt><code>-h</code>, <code>&#8211;hash</code> <i>hash-list</i></p>
<dd> Only generate file hashes for the comma-specified list specified (since dpkg 1.17.14). The default is to generate all currently supported hashes. Supported values: <code>md5</code>, <code>sha1</code>, <code>sha256</code>.</p>
<dt><code>-m</code>, <code>&#8211;multiversion</code></p>
<dd> Include all found packages in the output.</p>
<dt><code>-M</code>, <code>&#8211;medium</code> <i>id-string</i></p>
<dd> Add an <code>X-Medium</code> field containing the value <i>id-string</i> (since dpkg 1.15.5). This field is required if you want to generate <code>Packages.cd</code> files for use by the multicd access method of dselect.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>dpkg-scanpackages</code> outputs the usual self-explanatory errors. It also warns about packages that are in the wrong subdirectory, are duplicated, have a Filename field in their control file, are missing from the override file, or have maintainer substitutions which do not take effect.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1), <code><a href="/docs/linux/man/5-deb-override/">deb-override</a></code>(5), <code><a href="/docs/linux/man/5-deb-extra-override/">deb-extra-override</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-scansources/">dpkg-scansources</a></code>(1). </p>
<h2>Index</h2>
