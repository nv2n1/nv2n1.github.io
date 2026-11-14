---
title: "dpkg-distaddfile(1)"
name: "dpkg-distaddfile"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-distaddfile/"
description: "dpkg-distaddfile – add entries to debian/files"
---

<h2 class="name">NAME</h2>
<p> dpkg-distaddfile &#8211; add entries to debian/files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-distaddfile</code> [<i>option</i>&#8230;] <i>filename section priority</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-distaddfile</code> adds an entry for a named file to <code>debian/files</code>. </p>
<p> It takes three non-option arguments, the filename and the section and priority for the <code>.changes</code> file. </p>
<p> The filename should be specified relative to the directory where <code>dpkg-genchanges</code> will expect to find the files, usually <code>..</code>, rather than being a pathname relative to the current directory when <code>dpkg-distaddfile</code> is run.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i>files-list-file</i></p>
<dd> Read or write the list of files to be uploaded here, rather than using <code>debian/files</code>.</p>
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
<dt><code>debian/files</code></p>
<dd> The list of generated files which are part of the upload being prepared. <code>dpkg-distaddfile</code> can be used to add additional files.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-src-files/">deb-src-files</a></code>(5). </p>
<h2>Index</h2>
