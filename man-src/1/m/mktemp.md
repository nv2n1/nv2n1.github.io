---
title: "mktemp(1)"
name: "mktemp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mktemp/"
description: "mktemp – create a temporary file or directory"
---

<h2 class="name">NAME</h2>
<p> mktemp &#8211; create a temporary file or directory </p>
<h2>SYNOPSIS</h2>
<p> <code>mktemp</code> [<i>,OPTION/</i>]&#8230; [<i>,TEMPLATE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Create a temporary file or directory, safely, and print its name. TEMPLATE must contain at least 3 consecutive &#8216;X&#8217;s in last component. If TEMPLATE is not specified, use tmp.XXXXXXXXXX, and <code>&#8211;tmpdir</code> is implied. Files are created u+rw, and directories u+rwx, minus umask restrictions.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;directory</code></p>
<dd> create a directory, not a file</p>
<dt><code>-u</code>, <code>&#8211;dry-run</code></p>
<dd> do not create anything; merely print a name (unsafe)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress diagnostics about file/dir-creation failure</p>
<dt><code>&#8211;suffix</code>=<i>,SUFF/</i></p>
<dd> append SUFF to TEMPLATE; SUFF must not contain a slash. This option is implied if TEMPLATE does not end in X</p>
<dt><code>-p</code> DIR, <code>&#8211;tmpdir</code>[=<i>,DIR/</i>]</p>
<dd> interpret TEMPLATE relative to DIR; if DIR is not specified, use $TMPDIR if set, else <i>,/tmp/</i>. With this option, TEMPLATE must not be an absolute name; unlike with <code>-t</code>, TEMPLATE may contain slashes, but mktemp creates only the final component</p>
<dt><code>-t</code></p>
<dd> interpret TEMPLATE as a single file name component, relative to a directory: $TMPDIR, if set; else the directory specified via <code>-p</code>; else <i>,/tmp/</i> [deprecated]</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Jim Meyering and Eric Blake.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3), <a href="/docs/linux/man/3-mkdtemp/">mkdtemp</a>(3), <a href="/docs/linux/man/3-mktemp/">mktemp</a>(3) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/mktemp">https://www.gnu.org/software/coreutils/mktemp</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) mktemp invocation&#8217; </p>
<h2>Index</h2>
