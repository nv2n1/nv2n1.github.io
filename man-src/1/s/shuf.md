---
title: "shuf(1)"
name: "shuf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shuf/"
description: "shuf – generate random permutations"
---

<h2 class="name">NAME</h2>
<p> shuf &#8211; generate random permutations </p>
<h2>SYNOPSIS</h2>
<p> <code>shuf</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]<br />
 <code>shuf</code> <i>,-e /</i>[<i>,OPTION/</i>]&#8230; [<i>,ARG/</i>]&#8230;<br />
 <code>shuf</code> <i>,-i LO-HI /</i>[<i>,OPTION/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Write a random permutation of the input lines to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-e</code>, <code>&#8211;echo</code></p>
<dd> treat each ARG as an input line</p>
<dt><code>-i</code>, <code>&#8211;input-range</code>=<i>,LO-HI/</i></p>
<dd> treat each number LO through HI as an input line</p>
<dt><code>-n</code>, <code>&#8211;head-count</code>=<i>,COUNT/</i></p>
<dd> output at most COUNT lines</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> write result to FILE instead of standard output</p>
<dt><code>&#8211;random-source</code>=<i>,FILE/</i></p>
<dd> get random bytes from FILE</p>
<dt><code>-r</code>, <code>&#8211;repeat</code></p>
<dd> output lines can be repeated</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Paul Eggert.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/shuf">https://www.gnu.org/software/coreutils/shuf</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) shuf invocation&#8217; </p>
<h2>Index</h2>
