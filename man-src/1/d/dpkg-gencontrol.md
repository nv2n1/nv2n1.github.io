---
title: "dpkg-gencontrol(1)"
name: "dpkg-gencontrol"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-gencontrol/"
description: "dpkg-gencontrol – generate Debian control files"
---

<h2 class="name">NAME</h2>
<p> dpkg-gencontrol &#8211; generate Debian control files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-gencontrol</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-gencontrol</code> reads information from an unpacked Debian source tree and generates a binary package control file (which defaults to debian/tmp/DEBIAN/control); during this process it will simplify the relation fields. </p>
<p> Thus <code>Pre-Depends</code>, <code>Depends</code>, <code>Recommends</code> and <code>Suggests</code> are simplified in this order by removing dependencies which are known to be true according to the stronger dependencies already parsed. It will also remove any self-dependency (in fact it will remove any dependency which evaluates to true given the current version of the package as installed). Logically it keeps the intersection of multiple dependencies on the same package. The order of dependencies is preserved as best as possible: if any dependency must be discarded due to another dependency appearing further in the field, the superseding dependency will take the place of the discarded one. </p>
<p> The other relation fields (<code>Enhances</code>, <code>Conflicts</code>, <code>Breaks</code>, <code>Replaces</code> and <code>Provides</code>) are also simplified individually by computing the union of the various dependencies when a package is listed multiple times in the field. </p>
<p> <code>dpkg-gencontrol</code> also adds an entry for the binary package to <code>debian/files</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code><i>version</i></p>
<dd> Sets the version number of the binary package which will be generated.</p>
<dt><code>-V</code><i>name</i><code>=</code><i>value</i></p>
<dd> Set an output substitution variable. See <code><a href="/docs/linux/man/5-deb-substvars/">deb-substvars</a></code>(5) for discussion of output substitution.</p>
<dt><code>-T</code><i>substvars-file</i></p>
<dd> Read substitution variables in <i>substvars-file</i>; the default is <code>debian/substvars</code>. This option can be used multiple times to read substitution variables from multiple files (since dpkg 1.15.6).</p>
<dt><code>-D</code><i>field</i><code>=</code><i>value</i></p>
<dd> Override or add an output control file field.</p>
<dt><code>-U</code><i>field</i></p>
<dd> Remove an output control file field.</p>
<dt><code>-c</code><i>control-file</i></p>
<dd> Specifies the main source control file to read information from. The default is <code>debian/control</code>.</p>
<dt><code>-l</code><i>changelog-file</i></p>
<dd> Specifies the changelog file to read information from. The default is <code>debian/changelog</code>.</p>
<dt><code>-f</code><i>files-list-file</i></p>
<dd> Read or write the list of files to be uploaded here, rather than using <code>debian/files</code>.</p>
<dt><code>-F</code><i>changelog-format</i></p>
<dd> Specifies the format of the changelog. See <code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1) for information about alternative formats.</p>
<dt><code>-p</code><i>package</i></p>
<dd> Generate information for the binary package <i>package</i>. If the source control file lists only one binary package then this option may be omitted; otherwise it is essential to select which binary package&#8217;s information to generate.</p>
<dt><code>-n</code><i>filename</i></p>
<dd> Assume the filename of the package will be <i>filename</i> instead of the normal package_version_arch.deb filename.</p>
<dt><code>-is</code>, <code>-ip</code>, <code>-isp</code></p>
<dd> These options are ignored for compatibility with older versions of the dpkg build scripts but are now deprecated. Previously they were used to tell <code>dpkg-gencontrol</code> to include the Section and Priority fields in the control file. This is now the default behaviour. If you want to get the old behaviour you can use the <code>-U</code> option to delete the fields from the control file.</p>
<dt><code>-P</code><i>package-build-dir</i></p>
<dd> Scan <i>package-build-dir</i> instead of <code>debian/tmp</code>. This value is used to find the default value of the <code>Installed-Size</code> substitution variable and control file field, and for the default location of the output file.</p>
<dt><code>-O</code>[<i>filename</i>]</p>
<dd> Print the control file to standard output (or <i>filename</i> if specified, since dpkg 1.17.2), rather than to <code>debian/tmp/DEBIAN/control</code> (or <i>package-build-dir</i><code>/DEBIAN/control</code> if <code>-P</code> was used).</p>
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
<h2>FILES</h2>
<dl>
<dt><code>debian/control</code></p>
<dd> The main source control information file, giving version-independent information about the source package and the binary packages it can produce.</p>
<dt><code>debian/files</code></p>
<dd> The list of generated files which are part of the upload being prepared. <code>dpkg-gencontrol</code> adds the presumed filenames of binary packages whose control files it generates here.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-substvars/">deb-substvars</a></code>(5), <code><a href="/docs/linux/man/5-deb-src-control/">deb-src-control</a></code>(5), <code><a href="/docs/linux/man/5-deb-changelog/">deb-changelog</a></code>(5), <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5). </p>
<h2>Index</h2>
