---
title: "ntptime(8)"
name: "ntptime"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntptime/"
description: "ntptime – read and set kernel time variables"
---

<p>ntptime &#8211; read and set kernel time variables</p>
<h2>&nbsp;<wbr></h2>
<h2>Synopsis</h2>
<p><code>ntptime [ -MNchr ] [ -e </code><i>est_error</i><code> ] [ -f </code><i>frequency</i><code> ] [ -m </code><i>max_error</i><code> ] [ -o </code><i>offset</i><code> ] [ -s </code><i>status</i><code> ] [ -t </code><i>time_constant</i><code>] [ -T </code><i>tai_offset</i><code> ]</code> </p>
<h2>Description</h2>
<p>This program is useful only with special kernels described in the A Kernel Model for Precision Timekeeping page. It reads and displays time-related kernel variables using the <code>ntp_gettime()</code> system call. A similar display can be obtained using the <code>ntpdc</code> program and <code>kerninfo</code> command. </p>
<h2>Options</h2>
<dl>
<dd>
<dl>
<dt><code>-c</code></p>
<dd>Display the execution time of <code>ntptime</code> itself.</p>
<dt><code>-e </code><i>est_error</i></p>
<dd>Specify estimated error, in microseconds.</p>
<dt><code>-f </code><i>frequency</i></p>
<dd>Specify frequency offset, in parts per million.</p>
<dt><code>-h</code></p>
<dd>Display help information.</p>
<dt><code>-m </code><i>max_error</i></p>
<dd>Specify max possible errors, in microseconds.</p>
<dt><code>-o </code><i>offset</i></p>
<dd>Specify clock offset, in microseconds.</p>
<dt><code>-r</code></p>
<dd>Display Unix and NTP times in raw format.</p>
<dt><code>-s </code><i>status</i></p>
<dd>Specify clock status. Better know what you are doing.</p>
<dt><code>-t </code><i>time_constant</i></p>
<dd>Specify time constant, an integer in the range 0-10.</p>
<dt><code>-M</code></p>
<dd>Switch to microsecond mode.</p>
<dt><code>-N</code></p>
<dd>Switch to nanosecond mode.</p>
<dt><code>-T </code><i>tai_offset</i></p>
<dd>Set TAI offset.</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8), <a href="/docs/linux/man/8-ntpdate/">ntpdate</a>(8) The official HTML documentation. This file was automatically generated from HTML source. </p>
