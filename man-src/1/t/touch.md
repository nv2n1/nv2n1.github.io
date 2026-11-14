---
title: "touch(1)"
name: "touch"
section: "1"
letter: "t"
url: "/docs/linux/man/1-touch/"
description: "touch – change file timestamps"
---

<h2 class="name">NAME</h2>
<p> touch &#8211; change file timestamps </p>
<h2>SYNOPSIS</h2>
<p> <code>touch</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Update the access and modification times of each FILE to the current time. </p>
<p> A FILE argument that does not exist is created empty, unless <code>-c</code> or <code>-h</code> is supplied. </p>
<p> A FILE argument string of &#8211; is handled specially and causes touch to change the times of the file associated with standard output. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code></p>
<dd> change only the access time</p>
<dt><code>-c</code>, <code>&#8211;no-create</code></p>
<dd> do not create any files</p>
<dt><code>-d</code>, <code>&#8211;date</code>=<i>,STRING/</i></p>
<dd> parse STRING and use it instead of current time</p>
<dt><code>-f</code></p>
<dd> (ignored)</p>
<dt><code>-h</code>, <code>&#8211;no-dereference</code></p>
<dd> affect each symbolic link instead of any referenced file (useful only on systems that can change the timestamps of a symlink)</p>
<dt><code>-m</code></p>
<dd> change only the modification time</p>
<dt><code>-r</code>, <code>&#8211;reference</code>=<i>,FILE/</i></p>
<dd> use this file&#8217;s times instead of current time</p>
<dt><code>-t</code> STAMP</p>
<dd> use [[CC]YY]MMDDhhmm[.ss] instead of current time</p>
<dt><code>&#8211;time</code>=<i>,WORD/</i></p>
<dd> change the specified time: WORD is access, atime, or use: equivalent to <code>-a</code> WORD is modify or mtime: equivalent to <code>-m</code></p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Note that the <code>-d</code> and <code>-t</code> options accept different time-date formats.</p>
<h2>DATE STRING</h2>
<p> The &#8211;date=STRING is a mostly free format human readable date string such as &quot;Sun, 29 Feb 2004 16:21:42 -0800&quot; or &quot;2004-02-29 16:21:42&quot; or even &quot;next Thursday&quot;. A date string may contain items indicating calendar date, time of day, time zone, day of week, relative time, relative date, and numbers. An empty string indicates the beginning of the day. The date string format is more complex than is easily documented here but is fully described in the info documentation.</p>
<h2>AUTHOR</h2>
<p> Written by Paul Rubin, Arnold Robbins, Jim Kingdon, David MacKenzie, and Randy Smith.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/touch">https://www.gnu.org/software/coreutils/touch</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) touch invocation&#8217; </p>
<h2>Index</h2>
