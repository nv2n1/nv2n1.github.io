---
title: "tailf(1)"
name: "tailf"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tailf/"
description: "tailf – follow the growth of a log file"
---

<h2>NAME</h2>
<p> tailf &#8211; follow the growth of a log file</p>
<h2>SYNOPSIS</h2>
<p> <code>tailf</code> [<i>OPTION</i>] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tailf</code> will print out the last 10 lines of a file and then wait for the file to grow. It is similar to <code>tail -f</code> but does not access the file when it is not growing. This has the side effect of not updating the access time for the file, so a filesystem flush does not occur periodically when no log activity is happening. </p>
<p> <code>tailf</code> is extremely useful for monitoring log files on a laptop when logging is infrequent and the user desires that the hard disk spin down to conserve battery life. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;lines</code>=<i>N</i>, <code>-N</code></p>
<dd> output the last <i>N</i> lines, instead of the last 10.</p>
<dt><code>-V</code>, <code>&#8211;version</p>
<dd> Output version information and exit.</p>
<dt>-h</code>, <code>&#8211;help</p>
<dd> Display help and exit. </p>
</dl>
<p> </code></p>
<h2>AUTHOR</h2>
<p> This program was originally written by Rik Faith (faith [at] acm.org) and may be freely distributed under the terms of the X11/MIT License. There is ABSOLUTELY NO WARRANTY for this program. </p>
<p> The latest inotify based implementation was written by Karel Zak (kzak [at] redhat.com).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1), <code><a href="/docs/linux/man/1-less/">less</a></code>(1)</p>
<h2>AVAILABILITY</h2>
<p> The tailf command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a> </p>
<h2>Index</h2>
