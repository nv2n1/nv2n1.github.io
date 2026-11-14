---
title: "dpkg-scansources(1)"
name: "dpkg-scansources"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-scansources/"
description: "dpkg-scansources – create Sources index files"
---

<h2 class="name">NAME</h2>
<p> dpkg-scansources &#8211; create Sources index files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-scansources</code> [<i>option</i>&#8230;] <i>binary-dir</i> [<i>override-file</i> [<i>path-prefix</i>]] <code>&gt;</code> <i>Sources</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-scansources</code> scans the given <i>binary-dir</i> for <i>.dsc</i> files. These are used to create a Debian source index, which is output to stdout. </p>
<p> The <i>override-file</i>, if given, is used to set priorities in the resulting index records and to override the maintainer field given in the <i>.dsc</i> files. The file can be compressed (since dpkg 1.15.5). See <code><a href="/docs/linux/man/5-deb-override/">deb-override</a></code>(5) for the format of this file. </p>
<p> <code>Note:</code> Since the override file is indexed by binary, not source packages, there&#8217;s a bit of a problem here. The current implementation uses the highest priority of all the binary packages produced by a <i>.dsc</i> file for the priority of the source package, and the override entry for the first binary package listed in the <i>.dsc</i> file to modify maintainer information. This might change. </p>
<p> The <i>path-prefix</i>, if given, is prepended to the directory field in the generated source index. You generally use this to make the directory fields contain the path from the top of the Debian archive hierarchy. </p>
<p> <code>Note:</code> If you want to access the generated Sources file with <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) you will probably need to compress the file with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) (generating a Sources.gz file). <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) ignores uncompressed Sources files except on local access (i.e. <code>file://</code> sources).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-sort</code></p>
<dd> Don&#8217;t sort the index records. Normally they are sorted by source package name.</p>
<dt><code>-e</code>, <code>&#8211;extra-override</code> <i>file</i></p>
<dd> Scan <i>file</i> to find supplementary overrides (since dpkg 1.15.4; the file can be compressed since dpkg 1.15.5). See <code><a href="/docs/linux/man/5-deb-extra-override/">deb-extra-override</a></code>(5) for more information on its format.</p>
<dt><code>-s</code>, <code>&#8211;source-override</code> <i>file</i></p>
<dd> Use <i>file</i> as the source override file (the file can be compressed since dpkg 1.15.5). The default is the name of the override file you specified with <i>.src</i> appended. </p>
<p> The source override file is in a different format from the binary override file. It contains only two whitespace separated fields, the first is the source package name and the second is the section. Blank lines and comment lines are ignored in the normal manner. If a package appears in both files the source override takes precedence for setting the section.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn debugging on.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-override/">deb-override</a></code>(5), <code><a href="/docs/linux/man/5-deb-extra-override/">deb-extra-override</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1). </p>
<h2>Index</h2>
