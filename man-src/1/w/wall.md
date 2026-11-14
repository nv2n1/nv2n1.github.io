---
title: "wall(1)"
name: "wall"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wall/"
description: "wall – write a message to all users"
---

<h2 class="name">NAME</h2>
<p> wall &#8211; write a message to all users </p>
<h2>SYNOPSIS</h2>
<p> <code>wall</code> [<code>-n</code>] [<code>-t</code> <i>timeout</i>] [<code>-g</code> <i>group</i>] [<i>message</i> | <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>wall</code> displays a <i>message</i>, or the contents of a <i>file</i>, or otherwise its standard input, on the terminals of all currently logged in users. The command will wrap lines that are longer than 79 characters. Short lines are whitespace padded to have 79 characters. The command will always put a carriage return and new line at the end of each line. </p>
<p> Only the superuser can write on the terminals of users who have chosen to deny messages or are using a program which automatically denies messages. </p>
<p> Reading from a <i>file</i> is refused when the invoker is not superuser and the program is set-user-ID or set-group-ID.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>&#8211;nobanner</code></p>
<dl>
<dt>
<dd> Suppress the banner.</dl>
<p> <code>-t</code>, <code>&#8211;timeout</code> <i>timeout</i></p>
<dl>
<dt>
<dd> Abandon the write attempt to the terminals after <i>timeout</i> seconds. This <i>timeout</i> must be a positive integer. The default value is 300 seconds, which is a legacy from the time when people ran terminals over modem lines.</dl>
<p> <code>-g</code>, <code>&#8211;group</code> <i>group</i></p>
<dl>
<dt>
<dd> Limit printing message to members of group defined as a <i>group</i> argument. The argument can be group name or GID.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>NOTES</h2>
<p> Some sessions, such as <code><a href="//www.systutorials.com/docs/linux/man/1x-wdm/">wdm</a></code>(1x), that have in the beginning of <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5) ut_type data a &#8216;:&#8217; character will not get the message from <code>wall</code>. This is done to avoid write errors.</p>
<h2>HISTORY</h2>
<p> A <code>wall</code> command appeared in Version 7 AT&amp;T UNIX.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mesg/">mesg</a></code>(1), <code><a href="/docs/linux/man/1-talk/">talk</a></code>(1), <code><a href="/docs/linux/man/1-write/">write</a></code>(1), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>wall</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
