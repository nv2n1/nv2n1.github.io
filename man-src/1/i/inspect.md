---
title: "inspect(1)"
name: "inspect"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inspect/"
description: "inspect – Boost code inspection tool"
---

<h2 class="name">NAME</h2>
<p> inspect &#8211; Boost code inspection tool </p>
<h2>SYNOPSIS</h2>
<p> <code>inspect</code> [<i>-cvs</i>] [<i>-text</i>] [<i>-brief</i>] [<i>options</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> It is not uncommon for various common errors or guideline violations to creep into the Boost libraries. The <code>inspect </code> program detects and reports several common problems. It can be used to scan a proposed Boost submission to identify various failures. </p>
<p> The program is run in the directory to be scanned for errors. Sub-directories are also included in the scan. </p>
<p> If the first program argument is -cvs, only files and directories in the CVS tree of the current directory are scanned. Otherwise all files and sub-directories are included in the scan.</p>
<dl>
<dt>
<dd> Options:</p>
<dt> <code>-license</code></p>
<dt> <code>-copyright</code></p>
<dt> <code>-crlf</code></p>
<dt> <code>-link</code></p>
<dt> <code>-path_name</code></p>
<dt> <code>-tab</code></p>
<dt> <code>-ascii</code></p>
<dt> <code>-minmax</code></p>
<dt> <code>-unnamed</code></p>
<dt>
<dd>
<dd>The default is to have all checks on; otherwise options specify desired checks.</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>inspect</code> is maintained in HTML; see /usr/share/doc/libboostX.Y-doc/HTML/tools/inspect/index.html </p>
<h2>Index</h2>
