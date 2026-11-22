---

title: "uname(1)"
name: "uname"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uname/"
description: "uname – print system information"
---

<p> uname &#8211; print system information </p>
<h2>SYNOPSIS</h2>
<p> <code>uname</code> [<i>,OPTION/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print certain system information. With no OPTION, same as <code>-s</code>.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> print all information, in the following order, except omit <code>-p</code> and <code>-i</code> if unknown:</dd>
<dt><code>-s</code>, <code>&#8211;kernel-name</code></dt>
<dd> print the kernel name</dd>
<dt><code>-n</code>, <code>&#8211;nodename</code></dt>
<dd> print the network node hostname</dd>
<dt><code>-r</code>, <code>&#8211;kernel-release</code></dt>
<dd> print the kernel release</dd>
<dt><code>-v</code>, <code>&#8211;kernel-version</code></dt>
<dd> print the kernel version</dd>
<dt><code>-m</code>, <code>&#8211;machine</code></dt>
<dd> print the machine hardware name</dd>
<dt><code>-p</code>, <code>&#8211;processor</code></dt>
<dd> print the processor type (non-portable)</dd>
<dt><code>-i</code>, <code>&#8211;hardware-platform</code></dt>
<dd> print the hardware platform (non-portable)</dd>
<dt><code>-o</code>, <code>&#8211;operating-system</code></dt>
<dd> print the operating system</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-arch/">arch</a>(1), <a href="/docs/linux/man/2-uname/">uname</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/uname">https://www.gnu.org/software/coreutils/uname</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) uname invocation&#8217; </p>
