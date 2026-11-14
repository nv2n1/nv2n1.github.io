---
title: "hd(1)"
name: "hd"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hd/"
description: "hexdump – display file contents in hexadecimal, decimal, octal, or ascii"
---

<h2 class="name">NAME</h2>
<p> hexdump &#8211; display file contents in hexadecimal, decimal, octal, or ascii </p>
<p> <code>hexdump</code> <i>options file</i> &#8230; </p>
<p> <code>hd</code> <i>options file</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>hexdump</code> utility is a filter which displays the specified files, or standard input if no files are specified, in a user-specified format.</p>
<h2>OPTIONS</h2>
<p> Below, the <i>length</i> and <i>offset</i> arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;), or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-b</code>, <code>&#8211;one-byte-octal</code></p>
<dl>
<dt>
<dd> <i>One-byte octal display</i>. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, zero-filled bytes of input data, in octal, per line.</dl>
<p> <code>-c</code>, <code>&#8211;one-byte-char</code></p>
<dl>
<dt>
<dd> <i>One-byte character display</i>. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, space-filled characters of input data per line.</dl>
<p> <code>-C</code>, <code>&#8211;canonical</code></p>
<dl>
<dt>
<dd> <i>Canonical hex+ASCII display</i>. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes, followed by the same sixteen bytes in <code>%_p</code> format enclosed in &#8216;<code>|</code>&#8216; characters. Invoking the program as <code>hd</code> implies this option.</dl>
<p> <code>-d</code>, <code>&#8211;two-bytes-decimal</code></p>
<dl>
<dt>
<dd> <i>Two-byte decimal display</i>. Display the input offset in hexadecimal, followed by eight space-separated, five-column, zero-filled, two-byte units of input data, in unsigned decimal, per line.</dl>
<p> <code>-e</code>, <code>&#8211;format</code> <i>format_string</i></p>
<dl>
<dt>
<dd> Specify a format string to be used for displaying data.</dl>
<p> <code>-f</code>, <code>&#8211;format-file</code> <i>file</i></p>
<dl>
<dt>
<dd> Specify a file that contains one or more newline-separated format strings. Empty lines and lines whose first non-blank character is a hash mark (#) are ignored.</dl>
<p> <code>-L</code>, <code>&#8211;color</code>[=<i>when</i>]</p>
<dl>
<dt>
<dd> Accept color units for the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled; for the current built-in default see the <code>&#8211;help</code> output. See also the <code>Colors</code> subsection and the <code>COLORS</code> section below.</dl>
<p> <code>-n</code>, <code>&#8211;length</code> <i>length</i></p>
<dl>
<dt>
<dd> Interpret only <i>length</i> bytes of input.</dl>
<p> <code>-o</code>, <code>&#8211;two-bytes-octal</code></p>
<dl>
<dt>
<dd> <i>Two-byte octal display</i>. Display the input offset in hexadecimal, followed by eight space-separated, six-column, zero-filled, two-byte quantities of input data, in octal, per line.</dl>
<p> <code>-s</code>, <code>&#8211;skip</code> <i>offset</i></p>
<dl>
<dt>
<dd> Skip <i>offset</i> bytes from the beginning of the input.</dl>
<p> <code>-v</code>, <code>&#8211;no-squeezing</code></p>
<dl>
<dt>
<dd> The <code>-v</code> option causes <code>hexdump</code> to display all input data. Without the <code>-v</code> option, any number of groups of output lines which would be identical to the immediately preceding group of output lines (except for the input offsets), are replaced with a line comprised of a single asterisk.</dl>
<p> <code>-x</code>, <code>&#8211;two-bytes-hex</code></p>
<dl>
<dt>
<dd> <i>Two-byte hexadecimal display</i>. Display the input offset in hexadecimal, followed by eight space-separated, four-column, zero-filled, two-byte quantities of input data, in hexadecimal, per line.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> For each input file, <code>hexdump</code> sequentially copies the input to standard output, transforming the data according to the format strings specified by the <code>-e</code> and <code>-f</code> options, in the order that they were specified.</p>
<h2>FORMATS</h2>
<p> A format string contains any number of format units, separated by whitespace. A format unit contains up to three items: an iteration count, a byte count, and a format. </p>
<p> The iteration count is an optional positive integer, which defaults to one. Each format is applied iteration count times. </p>
<p> The byte count is an optional positive integer. If specified it defines the number of bytes to be interpreted by each iteration of the format. </p>
<p> If an iteration count and/or a byte count is specified, a single slash must be placed after the iteration count and/or before the byte count to disambiguate them. Any whitespace before or after the slash is ignored. </p>
<p> The format is required and must be surrounded by double quote (&quot; &quot;) marks. It is interpreted as a fprintf-style format string (see <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), with the following exceptions: </p>
<p> 1.</p>
<dl>
<dt>
<dd> An asterisk (*) may not be used as a field width or precision.</dl>
<p> 2.</p>
<dl>
<dt>
<dd> A byte count or field precision <i>is</i> required for each <code>s</code> conversion character (unlike the fprintf3 default which prints the entire string if the precision is unspecified).</dl>
<p> 3.</p>
<dl>
<dt>
<dd> The conversion characters <code>h</code>, <code>l</code>, <code>n</code>, <code>p</code>, and <code>q</code> are not supported.</dl>
<p> 4.</p>
<dl>
<dt>
<dd> The single character escape sequences described in the C standard are supported:</dl>
<dl>
<dt>
<dd>
<table BORDER>
<tr VALIGN=top>
<td>
<p> NULL </td>
<td>
<p> 
