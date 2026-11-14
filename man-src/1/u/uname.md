---
title: "uname(1)"
name: "uname"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uname/"
description: "uname – print system information"
---

<h2 class="name">NAME</h2>
<p> uname &#8211; print system information </p>
<h2>SYNOPSIS</h2>
<p> <code>uname</code> [<i>,OPTION/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print certain system information. With no OPTION, same as <code>-s</code>.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> print all information, in the following order, except omit <code>-p</code> and <code>-i</code> if unknown:</p>
<dt><code>-s</code>, <code>&#8211;kernel-name</code></p>
<dd> print the kernel name</p>
<dt><code>-n</code>, <code>&#8211;nodename</code></p>
<dd> print the network node hostname</p>
<dt><code>-r</code>, <code>&#8211;kernel-release</code></p>
<dd> print the kernel release</p>
<dt><code>-v</code>, <code>&#8211;kernel-version</code></p>
<dd> print the kernel version</p>
<dt><code>-m</code>, <code>&#8211;machine</code></p>
<dd> print the machine hardware name</p>
<dt><code>-p</code>, <code>&#8211;processor</code></p>
<dd> print the processor type (non-portable)</p>
<dt><code>-i</code>, <code>&#8211;hardware-platform</code></p>
<dd> print the hardware platform (non-portable)</p>
<dt><code>-o</code>, <code>&#8211;operating-system</code></p>
<dd> print the operating system</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-arch/">arch</a>(1), <a href="/docs/linux/man/2-uname/">uname</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/uname">https://www.gnu.org/software/coreutils/uname</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) uname invocation&#8217; </p>
<h2>Index</h2>
