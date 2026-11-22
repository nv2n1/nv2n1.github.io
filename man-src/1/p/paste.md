---

title: "paste(1)"
name: "paste"
section: "1"
letter: "p"
url: "/docs/linux/man/1-paste/"
description: "paste – merge lines of files"
---

<p> paste &#8211; merge lines of files </p>
<h2>SYNOPSIS</h2>
<p> <code>paste</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Write lines consisting of the sequentially corresponding lines from each FILE, separated by TABs, to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;delimiters</code>=<i>,LIST/</i></dt>
<dd> reuse characters from LIST instead of TABs</dd>
<dt><code>-s</code>, <code>&#8211;serial</code></dt>
<dd> paste one file at a time instead of in parallel</dd>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></dt>
<dd> line delimiter is NUL, not newline</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by David M. Ihnat and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/paste">https://www.gnu.org/software/coreutils/paste</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) paste invocation&#8217; </p>
