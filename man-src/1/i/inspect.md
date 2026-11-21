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
</dt><dd> Options:</dd>
<dt> <code>-license</code></dt>
<dt> <code>-copyright</code></dt>
<dt> <code>-crlf</code></dt>
<dt> <code>-link</code></dt>
<dt> <code>-path_name</code></dt>
<dt> <code>-tab</code></dt>
<dt> <code>-ascii</code></dt>
<dt> <code>-minmax</code></dt>
<dt> <code>-unnamed</code></dt>
<dd>The default is to have all checks on; otherwise options specify desired checks.</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>inspect</code> is maintained in HTML; see /usr/share/doc/libboostX.Y-doc/HTML/tools/inspect/index.html </p>
