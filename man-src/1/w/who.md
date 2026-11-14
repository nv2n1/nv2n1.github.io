---
title: "who(1)"
name: "who"
section: "1"
letter: "w"
url: "/docs/linux/man/1-who/"
description: "who – show who is logged on"
---

<h2 class="name">NAME</h2>
<p> who &#8211; show who is logged on </p>
<h2>SYNOPSIS</h2>
<p> <code>who</code> [<i>,OPTION/</i>]&#8230; [ <i>,FILE | ARG1 ARG2 /</i>]</p>
<h2>DESCRIPTION</h2>
<p> Print information about users who are currently logged in.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> same as <code>-b</code> <code>-d</code> <code>&#8211;login</code> <code>-p</code> <code>-r</code> <code>-t</code> <code>-T</code> <code>-u</code></p>
<dt><code>-b</code>, <code>&#8211;boot</code></p>
<dd> time of last system boot</p>
<dt><code>-d</code>, <code>&#8211;dead</code></p>
<dd> print dead processes</p>
<dt><code>-H</code>, <code>&#8211;heading</code></p>
<dd> print line of column headings</p>
<dt><code>&#8211;ips</code></p>
<dd> print ips instead of hostnames. with <code>&#8211;lookup</code>, canonicalizes based on stored IP, if available, rather than stored hostname</p>
<dt><code>-l</code>, <code>&#8211;login</code></p>
<dd> print system login processes</p>
<dt><code>&#8211;lookup</code></p>
<dd> attempt to canonicalize hostnames via DNS</p>
<dt><code>-m</code></p>
<dd> only hostname and user associated with stdin</p>
<dt><code>-p</code>, <code>&#8211;process</code></p>
<dd> print active processes spawned by init</p>
<dt><code>-q</code>, <code>&#8211;count</code></p>
<dd> all login names and number of users logged on</p>
<dt><code>-r</code>, <code>&#8211;runlevel</code></p>
<dd> print current runlevel</p>
<dt><code>-s</code>, <code>&#8211;short</code></p>
<dd> print only name, line, and time (default)</p>
<dt><code>-t</code>, <code>&#8211;time</code></p>
<dd> print last system clock change</p>
<dt><code>-T</code>, <code>-w</code>, <code>&#8211;mesg</code></p>
<dd> add user&#8217;s message status as +, &#8211; or ?</p>
<dt><code>-u</code>, <code>&#8211;users</code></p>
<dd> list users logged in</p>
<dt><code>&#8211;message</code></p>
<dd> same as <code>-T</code></p>
<dt><code>&#8211;writable</code></p>
<dd> same as <code>-T</code></p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If FILE is not specified, use <i>,/var/run/utmp/</i>. <i>,/var/log/wtmp/</i> as FILE is common. If ARG1 ARG2 given, <code>-m</code> presumed: &#8216;am i&#8217; or &#8216;mom likes&#8217; are usual.</p>
<h2>AUTHOR</h2>
<p> Written by Joseph Arceneaux, David MacKenzie, and Michael Stone.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/who">https://www.gnu.org/software/coreutils/who</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) who invocation&#8217; </p>
<h2>Index</h2>
