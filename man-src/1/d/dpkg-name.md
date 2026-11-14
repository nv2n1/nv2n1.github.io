---
title: "dpkg-name(1)"
name: "dpkg-name"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-name/"
description: "dpkg-name – rename Debian packages to full package names"
---

<h2 class="name">NAME</h2>
<p> dpkg-name &#8211; rename Debian packages to full package names </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-name</code> [<i>option</i>&#8230;] [<code>&#8212;</code>] <i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>dpkg-name</code> program which provides an easy way to rename <code>Debian</code> packages into their full package names. A full package name consists of <i>package</i><code>_</code><i>version</i><code>_</code><i>architecture</i><code>.</code><i>package-type</i> as specified in the control file of the package. The <i>version</i> part of the filename consists of the upstream version information optionally followed by a hyphen and the revision information. The <i>package-type</i> part comes from that field if present or fallbacks to <code>deb</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;no-architecture</code></p>
<dd> The destination filename will not have the architecture information.</p>
<dt><code>-k</code>, <code>&#8211;symlink</code></p>
<dd> Create a symlink, instead of moving.</p>
<dt><code>-o</code>, <code>&#8211;overwrite</code></p>
<dd> Existing files will be overwritten if they have the same name as the destination filename.</p>
<dt><code>-s</code>, <code>&#8211;subdir</code> [<i>dir</i>]</p>
<dd> Files will be moved into a subdirectory. If the directory given as argument exists the files will be moved into that directory otherwise the name of the target directory is extracted from the section field in the control part of the package. The target directory will be &laquo;unstable/binary-<i>architecture</i>/<i>section</i>&raquo;. If the section is not found in the control, then <code>no-section</code> is assumed, and in this case, as well as for sections <code>non-free</code> and <code>contrib</code> the target directory is &laquo;<i>section</i>/binary-<i>architecture</i>&raquo;. The section field is not required so a lot of packages will find their way to the <code>no-section</code> area. </p>
<p> <code>Warning:</code> <i>Use this option with care, it is messy.</i></p>
<dt><code>-c</code>, <code>&#8211;create-dir</code></p>
<dd> This option can used together with the <code>-s</code> option. If a target directory isn&#8217;t found it will be created automatically. </p>
<p> <code>Warning:</code> <i>Use this option with care.</i></p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>BUGS</h2>
<p> Some packages don&#8217;t follow the name structure <i>package</i><code>_</code><i>version</i><code>_</code><i>architecture</i><code>.deb</code>. Packages renamed by <code>dpkg-name</code> will follow this structure. Generally this will have no impact on how packages are installed by <code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1)/<code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), but other installation tools might depend on this naming structure.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>dpkg-name bar-foo.deb</code></p>
<dd> The file <code>bar-foo.deb</code> will be renamed to bar-foo_1.0-2_i386.deb or something similar (depending on whatever information is in the control part of <code>bar-foo.deb</code>).</p>
<dt><code>find /root/debian/ -name &#8216;*.deb&#8217; | xargs -n 1 dpkg-name -a</code></p>
<dd> All files with the extension <code>deb</code> in the directory /root/debian and its subdirectory&#8217;s will be renamed by <code>dpkg-name</code> if required into names with no architecture information.</p>
<dt><code>find -name &#8216;*.deb&#8217; | xargs -n 1 dpkg-name -a -o -s -c</code></p>
<dd> <code>Don&#8217;t do this.</code> Your archive will be messed up completely because a lot of packages don&#8217;t come with section information. <code>Don&#8217;t do this.</code></p>
<dt><code>dpkg-deb &#8211;build debian-tmp &amp;&amp; dpkg-name -o -s .. debian-tmp.deb</code></p>
<dd> This can be used when building new packages.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5), <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1). </p>
<h2>Index</h2>
