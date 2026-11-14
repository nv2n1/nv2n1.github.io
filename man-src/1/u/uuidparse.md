---
title: "uuidparse(1)"
name: "uuidparse"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uuidparse/"
description: "uuidparse – a utility to parse unique identifiers"
---

<h2 class="name">NAME</h2>
<p> uuidparse &#8211; a utility to parse unique identifiers </p>
<h2>SYNOPSIS</h2>
<p> <code>uuidparse</code> [options] <i>uuid</i></p>
<h2>DESCRIPTION</h2>
<p> This command will parse unique identifier inputs from either command line arguments or standard input. The inputs are white-space separated.</p>
<h2>OUTPUT</h2>
<h3>Variants</h3>
<table BORDER>
<tr VALIGN=top>
<td>
<p> NCS </td>
<td>
<p> Network Computing System identifier. These were the original UUIDs.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> DCE </td>
<td>
<p> The Open Software Foundation&#8217;s (OSF) Distributed Computing Environment UUIDs.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Microsoft </td>
<td>
<p> Microsoft Windows platform globally unique identifier (GUID).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> other </td>
<td>
<p> Unknown variant. Usually invalid input data.
</td>
</tr>
</table>
<h3>Types</h3>
<table BORDER>
<tr VALIGN=top>
<td>
<p> nil </td>
<td>
<p> Special type for zero in type file.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> time-based </td>
<td>
<p> The DCE time based.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> DCE </td>
<td>
<p> The DCE time and MAC Address.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> name-based </td>
<td>
<p> RFC 4122 md5sum hash.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> random </td>
<td>
<p> RFC 4122 random.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sha1-based </td>
<td>
<p> RFC 4122 sha-1 hash.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> unknown </td>
<td>
<p> Unknown type. Usually invalid input data.
</td>
</tr>
</table>
<h2>OPTIONS</h2>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dt>
<dd> Use JSON output format.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dt>
<dd> Do not print a header line.</dl>
<p> <code>-o</code>, <code>&#8211;output</code></p>
<dl>
<dt>
<dd> Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Use the raw output format.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-uuidgen/">uuidgen</a></code>(1), <code><a href="/docs/linux/man/3-libuuid/">libuuid</a></code>(3), <i>RFC 4122</i> &lt;<a rel="nofollow" href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>uuidparse</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
