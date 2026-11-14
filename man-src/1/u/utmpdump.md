---
title: "utmpdump(1)"
name: "utmpdump"
section: "1"
letter: "u"
url: "/docs/linux/man/1-utmpdump/"
description: "utmpdump – dump UTMP and WTMP files in raw format"
---

<h2 class="name">NAME</h2>
<p> utmpdump &#8211; dump UTMP and WTMP files in raw format </p>
<h2>SYNOPSIS</h2>
<p> <code>utmpdump</code> [options] <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>utmpdump</code> is a simple program to dump UTMP and WTMP files in raw format, so they can be examined. <code>utmpdump</code> reads from stdin unless a <i>filename</i> is passed.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;follow</code></p>
<dl>
<dt>
<dd> Output appended data as the file grows.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write command output to <i>file</i> instead of standard output.</dl>
<p> <code>-r</code>, <code>&#8211;reverse</code></p>
<dl>
<dt>
<dd> Undump, write back edited login information into the utmp or wtmp files.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>NOTES</h2>
<p> <code>utmpdump</code> can be useful in cases of corrupted utmp or wtmp entries. It can dump out utmp/wtmp to an ASCII file, which can then be edited to remove bogus entries, and reintegrated using:</p>
<dl>
<dt>
<dd>
<p> <code>utmpdump -r &lt; ascii_file &gt; wtmp</code>
</dl>
<p> But be warned, <code>utmpdump</code> was written for debugging purposes only.</p>
<h3>File formats</h3>
<p> Only the binary version of the <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5) is standardised. Textual dumps may become incompatible in future. </p>
<p> The version 2.28 was the last one that printed text output using <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) timestamp format. Newer dumps use millisecond precision ISO-8601 timestamp format in UTC-0 timezone. Conversion from former timestamp format can be made to binary, although attempt to do so can lead the timestamps to drift amount of timezone offset.</p>
<h2>BUGS</h2>
<p> You may <code>not</code> use the <code>-r</code> option, as the format for the utmp/wtmp files strongly depends on the input format. This tool was <code>not</code> written for normal use, but for debugging only.</p>
<h2>AUTHORS</h2>
<p> Michael Krapp</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-last/">last</a></code>(1), <code><a href="/docs/linux/man/1-w/">w</a></code>(1), <code><a href="/docs/linux/man/1-who/">who</a></code>(1), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>utmpdump</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
