---
title: "hd(1)"
name: "hd"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hd/"
description: "hexdump – display file contents in hexadecimal, decimal, octal, or ascii"
---
<h2 class="name">NAME</h2>
<p> hexdump - display file contents in hexadecimal, decimal, octal, or ascii </p>
<p> <code>hexdump</code> <i>options file</i> ... </p>
<p> <code>hd</code> <i>options file</i> ... </p>
<h2>DESCRIPTION</h2>
<p> The <code>hexdump</code> utility is a filter which displays the specified files, or standard input if no files are specified, in a user-specified format.  </p>
<h2>OPTIONS</h2>
<p> Below, the <i>length</i> and <i>offset</i> arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;), or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-b</code>, <code>--one-byte-octal</code> </p>
<dl>
<dd> <p> <i>One-byte octal display</i>. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, zero-filled bytes of input data, in octal, per line. </p>
 </dd></dl>
<p> <code>-c</code>, <code>--one-byte-char</code> </p>
<dl>
<dd> <p> <i>One-byte character display</i>. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, space-filled characters of input data per line. </p>
 </dd></dl>
<p> <code>-C</code>, <code>--canonical</code> </p>
<dl>
<dd> <p> <i>Canonical hex+ASCII display</i>. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes, followed by the same sixteen bytes in <code>%_p</code> format enclosed in &#8216;<code>|</code>&#8216; characters. Invoking the program as <code>hd</code> implies this option. </p>
 </dd></dl>
<p> <code>-d</code>, <code>--two-bytes-decimal</code> </p>
<dl>
<dd> <p> <i>Two-byte decimal display</i>. Display the input offset in hexadecimal, followed by eight space-separated, five-column, zero-filled, two-byte units of input data, in unsigned decimal, per line. </p>
 </dd></dl>
<p> <code>-e</code>, <code>--format</code> <i>format_string</i> </p>
<dl>
<dd> <p> Specify a format string to be used for displaying data. </p>
 </dd></dl>
<p> <code>-f</code>, <code>--format-file</code> <i>file</i> </p>
<dl>
<dd> <p> Specify a file that contains one or more newline-separated format strings. Empty lines and lines whose first non-blank character is a hash mark (#) are ignored. </p>
 </dd></dl>
<p> <code>-L</code>, <code>--color</code>[=<i>when</i>] </p>
<dl>
<dd> <p> Accept color units for the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled; for the current built-in default see the <code>--help</code> output. See also the <code>Colors</code> subsection and the <code>COLORS</code> section below. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--length</code> <i>length</i> </p>
<dl>
<dd> <p> Interpret only <i>length</i> bytes of input. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--two-bytes-octal</code> </p>
<dl>
<dd> <p> <i>Two-byte octal display</i>. Display the input offset in hexadecimal, followed by eight space-separated, six-column, zero-filled, two-byte quantities of input data, in octal, per line. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--skip</code> <i>offset</i> </p>
<dl>
<dd> <p> Skip <i>offset</i> bytes from the beginning of the input. </p>
 </dd></dl>
<p> <code>-v</code>, <code>--no-squeezing</code> </p>
<dl>
<dd> <p> The <code>-v</code> option causes <code>hexdump</code> to display all input data. Without the <code>-v</code> option, any number of groups of output lines which would be identical to the immediately preceding group of output lines (except for the input offsets), are replaced with a line comprised of a single asterisk. </p>
 </dd></dl>
<p> <code>-x</code>, <code>--two-bytes-hex</code> </p>
<dl>
<dd> <p> <i>Two-byte hexadecimal display</i>. Display the input offset in hexadecimal, followed by eight space-separated, four-column, zero-filled, two-byte quantities of input data, in hexadecimal, per line. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<p> For each input file, <code>hexdump</code> sequentially copies the input to standard output, transforming the data according to the format strings specified by the <code>-e</code> and <code>-f</code> options, in the order that they were specified.  </p>
<h2>FORMATS</h2>
<p> A format string contains any number of format units, separated by whitespace. A format unit contains up to three items: an iteration count, a byte count, and a format. </p>
<p> The iteration count is an optional positive integer, which defaults to one. Each format is applied iteration count times. </p>
<p> The byte count is an optional positive integer. If specified it defines the number of bytes to be interpreted by each iteration of the format. </p>
<p> If an iteration count and/or a byte count is specified, a single slash must be placed after the iteration count and/or before the byte count to disambiguate them. Any whitespace before or after the slash is ignored. </p>
<p> The format is required and must be surrounded by double quote (&quot; &quot;) marks. It is interpreted as a fprintf-style format string (see <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), with the following exceptions: </p>
<p> 1. </p>
<dl>
<dd> <p> An asterisk (*) may not be used as a field width or precision. </p>
 </dd></dl>
<p> 2. </p>
<dl>
<dd> <p> A byte count or field precision <i>is</i> required for each <code>s</code> conversion character (unlike the fprintf3 default which prints the entire string if the precision is unspecified). </p>
 </dd></dl>
<p> 3. </p>
<dl>
<dd> <p> The conversion characters <code>h</code>, <code>l</code>, <code>n</code>, <code>p</code>, and <code>q</code> are not supported. </p>
 </dd></dl>
<p> 4. </p>
<dl>
<dd> <p> The single character escape sequences described in the C standard are supported: </p>
 </dd></dl>
<dl>
<dd> <table BORDER>
<tr VALIGN=top>
<td>  NULL </td>
<td>  \0 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;alert character&gt; </td>
<td>  \a 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;backspace&gt; </td>
<td>  \b 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;form-feed&gt; </td>
<td>  \f 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;newline&gt; </td>
<td>  \n 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;carriage return&gt; </td>
<td>  \r 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;tab&gt; </td>
<td>  \t 
</td>
</tr>
<tr VALIGN=top>
<td>  &lt;vertical tab&gt; </td>
<td>  \v 
</td>
</tr>
</table>
<p> <br />
 </p>
 </dd></dl>
<h3>Conversion strings</h3>
<p> The <code>hexdump</code> utility also supports the following additional conversion strings. </p>
<p> <code>_a[dox]</code> </p>
<dl>
<dd> <p> Display the input offset, cumulative across input files, of the next byte to be displayed. The appended characters <code>d</code>, <code>o</code>, and <code>x</code> specify the display base as decimal, octal or hexadecimal respectively. </p>
 </dd></dl>
<p> <code>_A[dox]</code> </p>
<dl>
<dd> <p> Identical to the <code>_a</code> conversion string except that it is only performed once, when all of the input data has been processed. </p>
 </dd></dl>
<p> <code>_c</code> </p>
<dl>
<dd> <p> Output characters in the default character set. Non-printing characters are displayed in three-character, zero-padded octal, except for those representable by standard escape notation (see above), which are displayed as two-character strings. </p>
 </dd></dl>
<p> <code>_p</code> </p>
<dl>
<dd> <p> Output characters in the default character set. Non-printing characters are displayed as a single &#8216;<code>.</code>&#8216;. </p>
 </dd></dl>
<p> <code>_u</code> </p>
<dl>
<dd> <p> Output US ASCII characters, with the exception that control characters are displayed using the following, lower-case, names. Characters greater than 0xff, hexadecimal, are displayed as hexadecimal strings. </p>
 </dd></dl>
<dl>
<dd> <table BORDER>
<tr VALIGN=top>
<td>  000 nul </td>
<td>  001 soh </td>
<td>  002 stx </td>
<td>  003 etx </td>
<td>  004 eot </td>
<td>  005 enq 
</td>
</tr>
<tr VALIGN=top>
<td>  006 ack </td>
<td>  007 bel </td>
<td>  008 bs </td>
<td>  009 ht </td>
<td>  00A lf </td>
<td>  00B vt 
</td>
</tr>
<tr VALIGN=top>
<td>  00C ff </td>
<td>  00D cr </td>
<td>  00E so </td>
<td>  00F si </td>
<td>  010 dle </td>
<td>  011 dc1 
</td>
</tr>
<tr VALIGN=top>
<td>  012 dc2 </td>
<td>  013 dc3 </td>
<td>  014 dc4 </td>
<td>  015 nak </td>
<td>  016 syn </td>
<td>  017 etb 
</td>
</tr>
<tr VALIGN=top>
<td>  018 can </td>
<td>  019 em </td>
<td>  01A sub </td>
<td>  01B esc </td>
<td>  01C fs </td>
<td>  01D gs 
</td>
</tr>
<tr VALIGN=top>
<td>  01E rs </td>
<td>  01F us </td>
<td>  0FF del </td>
<td> <p> <br />
 </p>
 </dd></dl>
<h3>Colors</h3>
<p> When put at the end of a format specifier, hexdump highlights the respective string with the color specified. Conditions, if present, are evaluated prior to highlighting. </p>
<p> <code>_L[color_unit_1,color_unit_2,...,color_unit_n]</code> </p>
<p> The full syntax of a color unit is as follows: </p>
<p> <code>[!]COLOR[:VALUE][@OFFSET_START[-END]]</code> </p>
<p> <code>!</code> </p>
<dl>
<dd> <p> Negate the condition. Please note that it only makes sense to negate a unit if both a value/string and an offset are specified. In that case the respective output string will be highlighted if and only if the value/string does not match the one at the offset. </p>
 </dd></dl>
<p> <code>COLOR</code> </p>
<dl>
<dd> <p> One of the 8 basic shell colors. </p>
 </dd></dl>
<p> <code>VALUE</code> </p>
<dl>
<dd> <p> A value to be matched specified in hexadecimal, or octal base, or as a string. Please note that the usual C escape sequences are not interpreted by hexdump inside the color_units. </p>
 </dd></dl>
<p> <code>OFFSET</code> </p>
<dl>
<dd> <p> An offset or an offset range at which to check for a match. Please note that lone OFFSET_START uses the same value as END offset. </p>
 </dd></dl>
<h3>Counters</h3>
<p> The default and supported byte counts for the conversion characters are as follows: </p>
<p> <code>%_c</code>, <code>%_p</code>, <code>%_u</code>, <code>%c</code> </p>
<dl>
<dd> <p> One byte counts only. </p>
 </dd></dl>
<p> <code>%d</code>, <code>%i</code>, <code>%o</code>, <code>%u</code>, <code>%X</code>, <code>%x</code> </p>
<dl>
<dd> <p> Four byte default, one, two and four byte counts supported. </p>
 </dd></dl>
<p> <code>%E</code>, <code>%e</code>, <code>%f</code>, <code>%G</code>, <code>%g</code> </p>
<dl>
<dd> <p> Eight byte default, four byte counts supported. </p>
 </dd></dl>
<p> The amount of data interpreted by each format string is the sum of the data required by each format unit, which is the iteration count times the byte count, or the iteration count times the number of bytes required by the format if the byte count is not specified. </p>
<p> The input is manipulated in <i>blocks</i>, where a block is defined as the largest amount of data specified by any format string. Format strings interpreting less than an input block&#8217;s worth of data, whose last format unit both interprets some number of bytes and does not have a specified iteration count, have the iteration count incremented until the entire input block has been processed or there is not enough data remaining in the block to satisfy the format string. </p>
<p> If, either as a result of user specification or <code>hexdump</code> modifying the iteration count as described above, an iteration count is greater than one, no trailing whitespace characters are output during the last iteration. </p>
<p> It is an error to specify a byte count as well as multiple conversion characters or strings unless all but one of the conversion characters or strings is <code>_a</code> or <code>_A</code>. </p>
<p> If, as a result of the specification of the <code>-n</code> option or end-of-file being reached, input data only partially satisfies a format string, the input block is zero-padded sufficiently to display all available data (i.e., any format units overlapping the end of data will display some number of the zero bytes). </p>
<p> Further output by such format strings is replaced by an equivalent number of spaces. An equivalent number of spaces is defined as the number of spaces output by an <code>s</code> conversion character with the same field width and precision as the original conversion character or conversion string but with any &#8216;<code>+</code>&#8216;, &#8216; &#8216;, &#8216;<code>#</code>&#8216; conversion flag characters removed, and referencing a NULL string. </p>
<p> If no format strings are specified, the default display is very similar to the <code>-x</code> output format (the <code>-x</code> option causes more space to be used between format units than in the default output).  </p>
<h2>EXIT STATUS</h2>
<p> <code>hexdump</code> exits 0 on success and &gt; 0 if an error occurred.  </p>
<h2>CONFORMING TO</h2>
<p> The <code>hexdump</code> utility is expected to be IEEE Std 1003.2 (&quot;POSIX.2&quot;) compatible.  </p>
<h2>EXAMPLES</h2>
<p> Display the input in perusal format: </p>
<dl>
<dd> <pre><code>   &quot;%06.6_ao &quot; 12/1 &quot;%3_u &quot;
   &quot;\t&quot; &quot;%_p &quot;
   &quot;\n&quot;
</code></pre>
 </dd></dl>
<p> Implement the <code>-x</code> option: </p>
<dl>
<dd> <pre><code>   &quot;%07.7_Ax\n&quot;
   &quot;%07.7_ax &quot; 8/2 &quot;%04x &quot; &quot;\n&quot;
</code></pre>
 </dd></dl>
<p> MBR Boot Signature example: Highlight the addresses cyan and the bytes at offsets 510 and 511 green if their value is 0xAA55, red otherwise. </p>
<dl>
<dd> <pre><code>   &quot;%07.7_Ax_L[cyan]\n&quot;
   &quot;%07.7_ax_L[cyan] &quot; 8/2 &quot; %04x_L[green:0xAA55 [at] 510-511,!red:0xAA55 [at] 510-511] &quot; &quot;\n&quot;
</code></pre>
 </dd></dl>
<h2>COLORS</h2>
<p> Implicit coloring can be disabled by an empty file <i>/etc/terminal-colors.d/hexdump.disable</i>. </p>
<p> See <code>terminal-colors.d</code>(5) for more details about colorization configuration.  </p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p> The <code>hexdump</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">FORMATS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAF">Conversion strings</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Colors</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Counters</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAI">EXIT STATUS</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">CONFORMING TO</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">COLORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">REPORTING BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">AVAILABILITY</a></dt>
<dd>  </dd></dl>
