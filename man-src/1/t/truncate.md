---
title: "truncate(1)"
name: "truncate"
section: "1"
letter: "t"
url: "/docs/linux/man/1-truncate/"
description: "truncate – shrink or extend the size of a file to the specified size"
---

<h2 class="name">NAME</h2>
<p> truncate &#8211; shrink or extend the size of a file to the specified size </p>
<h2>SYNOPSIS</h2>
<p> <code>truncate</code> <i>,OPTION/</i>&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Shrink or extend the size of each FILE to the specified size </p>
<p> A FILE argument that does not exist is created. </p>
<p> If a FILE is larger than the specified size, the extra data is lost. If a FILE is shorter, it is extended and the sparse extended part (hole) reads as zero bytes. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;no-create</code></p>
<dd> do not create any files</p>
<dt><code>-o</code>, <code>&#8211;io-blocks</code></p>
<dd> treat SIZE as number of IO blocks instead of bytes</p>
<dt><code>-r</code>, <code>&#8211;reference</code>=<i>,RFILE/</i></p>
<dd> base size on RFILE</p>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>,SIZE/</i></p>
<dd> set or adjust the file size by SIZE bytes</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The SIZE argument is an integer and optional unit (example: 10K is 10*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,&#8230; (powers of 1000). Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> SIZE may also be prefixed by one of the following modifying characters: &#8216;+&#8217; extend by, &#8216;-&#8216; reduce by, &#8216;&lt;&#8216; at most, &#8216;&gt;&#8217; at least, &#8216;/&#8217; round down to multiple of, &#8216;%&#8217; round up to multiple of.</p>
<h2>AUTHOR</h2>
<p> Written by Padraig Brady.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dd/">dd</a>(1), <a href="/docs/linux/man/2-truncate/">truncate</a>(2), <a href="/docs/linux/man/2-ftruncate/">ftruncate</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/truncate">https://www.gnu.org/software/coreutils/truncate</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) truncate invocation&#8217; </p>
<h2>Index</h2>
