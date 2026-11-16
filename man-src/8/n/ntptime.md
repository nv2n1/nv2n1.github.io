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
</dd><dl>
<dt><code>-c</code></dt>
<dd>Display the execution time of <code>ntptime</code> itself.</dd>
<dt><code>-e </code><i>est_error</i></dt>
<dd>Specify estimated error, in microseconds.</dd>
<dt><code>-f </code><i>frequency</i></dt>
<dd>Specify frequency offset, in parts per million.</dd>
<dt><code>-h</code></dt>
<dd>Display help information.</dd>
<dt><code>-m </code><i>max_error</i></dt>
<dd>Specify max possible errors, in microseconds.</dd>
<dt><code>-o </code><i>offset</i></dt>
<dd>Specify clock offset, in microseconds.</dd>
<dt><code>-r</code></dt>
<dd>Display Unix and NTP times in raw format.</dd>
<dt><code>-s </code><i>status</i></dt>
<dd>Specify clock status. Better know what you are doing.</dd>
<dt><code>-t </code><i>time_constant</i></dt>
<dd>Specify time constant, an integer in the range 0-10.</dd>
<dt><code>-M</code></dt>
<dd>Switch to microsecond mode.</dd>
<dt><code>-N</code></dt>
<dd>Switch to nanosecond mode.</dd>
<dt><code>-T </code><i>tai_offset</i></dt>
<dd>Set TAI offset.</dd></dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8), <a href="/docs/linux/man/8-ntpdate/">ntpdate</a>(8) The official HTML documentation. This file was automatically generated from HTML source. </p>
