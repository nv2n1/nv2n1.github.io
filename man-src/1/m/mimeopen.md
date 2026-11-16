---
title: "mimeopen(1)"
name: "mimeopen"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimeopen/"
description: "mimeopen – Open files by mimetype"
---

<h2 class="name">NAME</h2>
<p> mimeopen &#8211; Open files by mimetype </p>
<h2>SYNOPSIS</h2>
<p> mimeopen [options] [-] files</p>
<h2>DESCRIPTION</h2>
<p> This script tries to determine the mimetype of a file and open it with the default desktop application. If no default application is configured the user is prompted with an &#8220;open with&#8221; menu in the terminal. </p>
<p> To use this script you need the freedesktop mime-info database and the freedesktop desktop-file-utils package. See <i>File::MimeInfo::Applications</i>(3) for more details.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;ask</code></dt>
<dd> Do not execute the default application but ask which application to run. This does not change the default application.</dd>
<dt><code>-d</code>, <code>&#8211;ask-default</code></dt>
<dd> Let the user choose a new default program for given files.</dd>
<dt><code>-n</code>, <code>&#8211;no-ask</code></dt>
<dd> Don&#8217;t ask the user which program to use. Choose the default program or the first program known to handle the file mimetype. This does not set the default application.</dd>
<dt><code>-M</code>, <code>&#8211;magic-only</code></dt>
<dd> Do not check for extensions, globs or inode type, only look at the content of the file. This is particularly useful if for some reason you don&#8217;t trust the name or the extension a file has.</dd>
<dt><code>&#8211;database</code>=<i>mimedir</i>:<i>mimedir</i>:&#8230;</dt>
<dd> Force the program to look in these directories for the shared mime-info database. The directories specified by the basedir specification are ignored.</dd>
<dt><code>-D</code>, <code>&#8211;debug</code></dt>
<dd> Print debug information about how the mimetype was determined.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
</dd><dt><code>-u</code>, <code>&#8211;usage</code></dt>
<dd> Print a help message and exits.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Print the version of the program and exit.</dd></dl>
<h2>DEPRECATED OPTIONS</h2>
<dl>
<dt><code>-L</code>, <code>&#8211;dereference</code></dt>
<dd> Follow symbolic links. Deprecated because this is the logical default for this command. Ignored silently.</dd></dl>
<h2>BUGS</h2>
<p> No known bugs, please mail the author if you find one. </p>
<p> See <i>File::MimeInfo::Applications</i>(3) and <i>File::DesktopEntry</i>(3) for some limitations.</p>
<h2>AUTHOR</h2>
<p> Jaap Karssenberg &lt;pardus [at] cpan.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002, 2012 Jaap G Karssenberg. All rights reserved. This program is free software; you can redistribute it and/or modify it under the same terms as Perl. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mimetype/">mimetype</a></i>(1), <i><a href="/docs/linux/man/1-update-mime-database/">update-mime-database</a></i>(1), <i><a href="/docs/linux/man/1-update-desktop-database/">update-desktop-database</a></i>(1), <i>File::MimeInfo</i>(3), <i>File::MimeInfo::Applications</i>(3) </p>
<h2>Index</h2>
