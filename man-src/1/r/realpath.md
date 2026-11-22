---

title: "realpath(1)"
name: "realpath"
section: "1"
letter: "r"
url: "/docs/linux/man/1-realpath/"
description: "realpath – print the resolved path"
---

<p> realpath &#8211; print the resolved path </p>
<h2>SYNOPSIS</h2>
<p> <code>realpath</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print the resolved absolute file name; all but the last component must exist</p>
<dl>
<dt><code>-e</code>, <code>&#8211;canonicalize-existing</code></dt>
<dd> all components of the path must exist</dd>
<dt><code>-m</code>, <code>&#8211;canonicalize-missing</code></dt>
<dd> no path components need exist or be a directory</dd>
<dt><code>-L</code>, <code>&#8211;logical</code></dt>
<dd> resolve &#8216;..&#8217; components before symlinks</dd>
<dt><code>-P</code>, <code>&#8211;physical</code></dt>
<dd> resolve symlinks as encountered (default)</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> suppress most error messages</dd>
<dt><code>&#8211;relative-to</code>=<i>,DIR/</i></dt>
<dd> print the resolved path relative to DIR</dd>
<dt><code>&#8211;relative-base</code>=<i>,DIR/</i></dt>
<dd> print absolute paths unless paths below DIR</dd>
<dt><code>-s</code>, <code>&#8211;strip</code>, <code>&#8211;no-symlinks</code></dt>
<dd> don&#8217;t expand symlinks</dd>
<dt><code>-z</code>, <code>&#8211;zero</code></dt>
<dd> end each output line with NUL, not newline</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Padraig Brady.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-readlink/">readlink</a>(1), <a href="/docs/linux/man/2-readlink/">readlink</a>(2), <a href="/docs/linux/man/3-realpath/">realpath</a>(3) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/realpath">https://www.gnu.org/software/coreutils/realpath</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) realpath invocation&#8217; </p>
