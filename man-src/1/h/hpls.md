---
title: "hpls(1)"
name: "hpls"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpls/"
description: "hpls — list the contents of a directory on an HFS+ volume"
---

<h2>NAME</h2>
<p> hpls &#8212; list the contents of a directory on an HFS+ volume</p>
<h2>SYNOPSIS</h2>
<p> <code>hpls</code> [<code>options</code>] [<i>hfs-path &#8230;</i>]</p>
<h2>Description</h2>
<p> <code>hpls</code> is used to list files and directories on an HFS+ volume. If one or more arguments are given, each file or directory is shown; otherwise, the contents of the current working directory are displayed.<br />
&nbsp;</p>
<h2>Options</h2>
<dl>
<dt><code>-1</code></dt>
<dd> Each entry appears on a line by itself. This is the default if standard output is not a terminal.<br />
&nbsp;</dd>
<dt><code>-a</code></dt>
<dd> All entries are shown, including &quot;invisible&quot; files. The default is to omit invisible files.<br />
&nbsp;</dd>
<dt><code>-c</code></dt>
<dd> Sort and display entries by their creation date, rather than their modification date.<br />
&nbsp;</dd>
<dt><code>-d</code></dt>
<dd> List directory entries themselves rather than their contents. Normally the contents are shown for named directories on the command-line.<br />
&nbsp;</dd>
<dt><code>-i</code></dt>
<dd> Show the catalogue ID for each entry. Every file and directory on an HFS+ volume has a unique catalogue ID.<br />
&nbsp;</dd>
<dt><code>-l</code></dt>
<dd> Display entries in long format. This format shows the entry type (&quot;d&quot; for directory, &quot;f&quot; for file, &quot;F&quot; for locked file), flags (&quot;i&quot; for invisible), type and creator (four-character strings) for files only, size (number of items in a directory or resource and data bytes of a file, respectively), date of last modification (or creation if the <code>-c</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> flag is given), and name. </dd>
<p>&nbsp;</p>
<dt><code>-m</code></dt>
<dd> Display entries in a continuous format separated by commas.<br />
&nbsp;</dd>
<dt><code>-q</code></dt>
<dd> Replace special and non-printable characters in displayed filenames with question marks (?). This is the default when standard output is a terminal.<br />
&nbsp;</dd>
<dt><code>-r</code></dt>
<dd> Sort entries in reverse order before displaying.<br />
&nbsp;</dd>
<dt><code>-s</code></dt>
<dd> Show the file size for each entry in 1K block units. The size includes blocks used for both data and resource forks.<br />
&nbsp;</dd>
<dt><code>-t</code></dt>
<dd> Sort and display entries by time. Normally files will be sorted by name. This option uses the last modification date to sort unless <code>-c</code> is also specified.<br />
&nbsp;</dd>
<dt><code>-x</code></dt>
<dd> Display entries in column format like <code>-C</code>, but sorted horizontally into rows rather than columns.<br />
&nbsp;</dd>
<dt><code>-w</code> <i>width</i></dt>
<dd> Format output lines suitable for display in the given width. Normally the width will be determined from your terminal, from the environment variable COLUMNS, or from a default value of 80.<br />
&nbsp;</dd>
<dt><code>-C</code></dt>
<dd> Display entries in column format with entries sorted vertically. This is the default output format when standard output is a terminal.<br />
&nbsp;</dd>
<dt><code>-F</code></dt>
<dd> Cause certain output filenames to be followed by a single-character flag indicating the nature of the entry; directories are followed by a slash &quot;/&quot; and executable Macintosh applications are followed by an asterisk &quot;*&quot;.<br />
&nbsp;</dd>
<dt><code>-N</code></dt>
<dd> Cause all filenames to be output verbatim without question-mark substitution.<br />
&nbsp;</dd>
<dt><code>-R</code></dt>
<dd> For each directory that is encountered in a listing, recursively descend into and display its contents.<br />
&nbsp;</dd></dl>
<h2>See also</h2>
<p> <a href="/docs/linux/man/7-hfsplus/">hfsplus</a>(7), <a href="/docs/linux/man/1-hpmount/">hpmount</a>(1), <a href="/docs/linux/man/1-hpcd/">hpcd</a>(1), <a href="/docs/linux/man/1-hppwd/">hppwd</a>(1), <a href="/docs/linux/man/1-hprm/">hprm</a>(1), <a href="/docs/linux/man/1-hpmkdir/">hpmkdir</a>(1), <a href="/docs/linux/man/1-hpcopy/">hpcopy</a>(1), <a href="/docs/linux/man/1-hpumount/">hpumount</a>(1), <a href="/docs/linux/man/1-hpfsck/">hpfsck</a>(1).<br />
&nbsp;</p>
<h2>Author</h2>
<p> This manual page was written by Jens Schmalzing &lt;jensen [at] debian.org&gt; for <code>Debian GNU/Linux</code> using the manual page by Klaus Halfmann &lt;halfmann [at] libra.de&gt; that comes with the source code and documentation from the <code>Tech Info Library</code>.<br />
&nbsp; </p>
<h2>Index</h2>
