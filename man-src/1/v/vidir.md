---

title: "vidir(1)"
name: "vidir"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vidir/"
description: "vidir – edit directories and filenames"
---

<p> vidir &#8211; edit directories and filenames </p>
<h2>SYNOPSIS</h2>
<p> <code>vidir</code> [<code>&#8211;verbose</code>] [<i>directory</i>|<i>file</i>|<code>&#8211;</code>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>vidir</code> allows editing of directories and filenames in a text editor. If no <i>directory</i> is specified, the filenames of the current directory are edited. </p>
<p> When editing a directory, each item in the directory will appear on its own numbered line. These numbers are how vidir keeps track of what items are changed. Delete lines to remove files from the directory, or edit filenames to rename files. You can also switch pairs of numbers to swap filenames. </p>
<p> Filenames to be edited may be given any combination of <i>directory</i>s (which will be expanded to the non-recursive list of all files within <i>directory</i>), <i>file</i>s, or <i>&#8211;</i>. If the latter is specified, <code>vidir</code> reads a list of filenames from stdin and displays those for editing.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-v, &#8211;verbose</dt>
<dd> Verbosely display the actions taken by the program.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>vidir</dt>
<dd>
</dd><dt>vidir *.jpeg</dt>
<dd> Typical uses.</dd>
<dt>find | vidir &#8211;</dt>
<dd> Edit subdirectory contents too. To delete subdirectories, delete all their contents and the subdirectory itself in the editor.</dd>
<dt>find -type f | vidir &#8211;</dt>
<dd> Edit all files under the current directory and subdirectories.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>EDITOR</dt>
<dd> Editor to use.</dd>
<dt>VISUAL</dt>
<dd> Also supported to determine what editor to use.</dd></dl>
<h2>AUTHOR</h2>
<p> Copyright 2006 by Joey Hess &lt;id [at] joeyh.name&gt; </p>
<p> Licensed under the GNU GPL. </p>
