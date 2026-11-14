---
title: "stdbuf(1)"
name: "stdbuf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stdbuf/"
description: "stdbuf – Run COMMAND, with modified buffering operations for its standard streams."
---

<h2 class="name">NAME</h2>
<p> stdbuf &#8211; Run COMMAND, with modified buffering operations for its standard streams. </p>
<h2>SYNOPSIS</h2>
<p> <code>stdbuf</code> <i>,OPTION/</i>&#8230; <i>,COMMAND/</i></p>
<h2>DESCRIPTION</h2>
<p> Run COMMAND, with modified buffering operations for its standard streams. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>,MODE/</i></p>
<dd> adjust standard input stream buffering</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,MODE/</i></p>
<dd> adjust standard output stream buffering</p>
<dt><code>-e</code>, <code>&#8211;error</code>=<i>,MODE/</i></p>
<dd> adjust standard error stream buffering</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If MODE is &#8216;L&#8217; the corresponding stream will be line buffered. This option is invalid with standard input. </p>
<p> If MODE is &#8216;0&#8217; the corresponding stream will be unbuffered. </p>
<p> Otherwise MODE is a number which may be followed by one of the following: KB 1000, K 1024, MB 1000*1000, M 1024*1024, and so on for G, T, P, E, Z, Y. Binary prefixes can be used, too: KiB=K, MiB=M, and so on. In this case the corresponding stream will be fully buffered with the buffer size set to MODE bytes. </p>
<p> NOTE: If COMMAND adjusts the buffering of its standard streams (&#8216;tee&#8217; does for example) then that will override corresponding changes by &#8216;stdbuf&#8217;. Also some filters (like &#8216;dd&#8217; and &#8216;cat&#8217; etc.) don&#8217;t use streams for I/O, and are thus unaffected by &#8216;stdbuf&#8217; settings.</p>
<h2>EXAMPLES</h2>
<p> <code>tail -f access.log | stdbuf -oL cut -d &#8216; &#8216; -f1 | uniq</code><br />
 This will immediately display unique entries from access.log</p>
<h2>BUGS</h2>
<p> On GLIBC platforms, specifying a buffer size, i.e., using fully buffered mode will result in undefined operation.</p>
<h2>AUTHOR</h2>
<p> Written by Padraig Brady.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/stdbuf">https://www.gnu.org/software/coreutils/stdbuf</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) stdbuf invocation&#8217; </p>
<h2>Index</h2>
