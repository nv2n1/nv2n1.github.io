---
title: "troff(1)"
name: "troff"
section: "1"
letter: "t"
url: "/docs/linux/man/1-troff/"
description: "troff – the troff processor of the groff text formatting system"
---

<h2 class="name">NAME</h2>
<p> troff &#8211; the troff processor of the groff text formatting system </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-abcivzCERU</code> ] [ <code>-d </code><i>cs</i> ] [ <code>-f </code><i>fam</i> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-m </code><i>name</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-n </code><i>num</i> ] [ <code>-o </code><i>list</i> ] [ <code>-r </code><i>cn</i> ] [ <code>-T </code><i>name</i> ] [ <code>-w </code><i>name</i> ] [ <code>-W </code><i>name</i> ] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This manual page describes the GNU version of <code>troff</code>. It is part of the groff document formatting system. It is functionally compatible with Unix troff, but has many extensions, see <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7). Usually it should be invoked using the <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) command which will also run preprocessors and postprocessors in the appropriate order and with the appropriate options.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-a</code></p>
<dd> Generate an ASCII approximation of the typeset output.</p>
<dt><code>-b</code></p>
<dd> Print a backtrace with each warning or error message. This backtrace should help track down the cause of the error. The line numbers given in the backtrace may not always be correct, for <code>troff</code>&#8216;s idea of line numbers gets confused by <code>as</code> or <code>am</code> requests.</p>
<dt><code>-c</code></p>
<dd> Disable color output (always disabled in compatibility mode).</p>
<dt><code>-C</code></p>
<dd> Enable compatibility mode.</p>
<dt><code>-d</code><i>cs</i></p>
<dd> <code>-d</code><i>name</i><code>=</code><i>s</i> Define <i>c</i> or <i>name</i> to be a string <i>s</i>; <i>c</i> must be a one letter name.</p>
<dt><code>-E</code></p>
<dd> Inhibit all error messages of <code>troff</code>. Note that this doesn&#8217;t affect messages output to standard error by macro packages using the <code>tm</code> or <code>tm1</code> requests.</p>
<dt><code>-f</code><i>fam</i></p>
<dd> Use <i>fam</i> as the default font family.</p>
<dt><code>-F</code><i>dir</i></p>
<dd> Search in directory (or directory path) <i>dir</i> for subdirectories <i>dev</i>name (<i>name</i> is the name of the device) and there for the <i>DESC</i> file and font files. <i>dir</i> is scanned before all other font directories.</p>
<dt><code>-i</code></p>
<dd> Read the standard input after all the named input files have been processed.</p>
<dt><code>-I</code><i>dir</i></p>
<dd> This option may be used to add a directory to the search path for files (both those on the command line and those named in <code>.psbb</code> requests). The search path is initialized with the current directory. This option may be specified more than once; the directories are then searched in the order specified (but before the current directory). If you want to make the current directory be read before other directories, add <code>-I.</code> at the appropriate place.</p>
<dt>
<dd> No directory search is performed for files with an absolute file name.</p>
<dt><code>-m</code><i>name</i></p>
<dd> Read in the file name<i>.tmac</i>. If it isn&#8217;t found, try <i>tmac.</i>name instead. It will be first searched for in directories given with the <code>-M</code> command-line option, then in directories given in the <i>GROFF_TMAC_PATH</i> environment variable, then in the current directory (only if in unsafe mode), the home directory, <i>/usr/lib/groff/site-tmac</i>, <i>/usr/share/groff/site-tmac</i>, and <i>/usr/share/groff/1.22.4/tmac</i>.</p>
<dt><code>-M</code><i>dir</i></p>
<dd> Search directory (or directory path) <i>dir</i> for macro files. This is scanned before all other macro directories.</p>
<dt><code>-n</code><i>num</i></p>
<dd> Number the first page <i>num</i>.</p>
<dt><code>-o</code><i>list</i></p>
<dd> Output only pages in <i>list</i>, which is a comma-separated list of page ranges; <i>n</i> means print page <i>n</i>, <i>m</i><code>&#8211;</code><i>n</i> means print every page between <i>m</i> and <i>n</i>, <code>&#8211;</code><i>n</i> means print every page up to <i>n</i>, <i>n</i><code>&#8211;</code> means print every page from <i>n</i>. <code>troff</code> will exit after printing the last page in the list.</p>
<dt><code>-r</code><i>cn</i></p>
<dd> <code>-r</code><i>name</i><code>=</code><i>n</i> Set number register <i>c</i> or <i>name</i> to <i>n</i>; <i>c</i> must be a one character name; <i>n</i> can be any troff numeric expression.</p>
<dt><code>-R</code></p>
<dd> Don&#8217;t load <i>troffrc</i> and <i>troffrc-end</i>.</p>
<dt><code>-T</code><i>name</i></p>
<dd> Prepare output for device <i>name</i>, rather than the default <code>ps</code>; see <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) for a more detailed description.</p>
<dt><code>-U</code></p>
<dd> Unsafe mode. This will enable the following requests: <code>open</code>, <code>opena</code>, <code>pso</code>, <code>sy</code>, and <code>pi</code>. For security reasons, these potentially dangerous requests are disabled otherwise. It will also add the current directory to the macro search path.</p>
<dt><code>-v</code></p>
<dd> Print the version number.</p>
<dt><code>-w</code><i>name</i></p>
<dd> Enable warning <i>name</i>. Available warnings are described in section &#8220;Warnings&#8221; below. To enable most useful warnings use <code>-w</code> <code>all</code>. To enable absolutely all warnings use <code>-w w</code> instead. Multiple <code>-w</code> options are allowed.</p>
<dt><code>-W</code><i>name</i></p>
<dd> Inhibit warning <i>name</i>. Multiple <code>-W</code> options are allowed.</p>
<dt><code>-z</code></p>
<dd> Suppress formatted output.</dl>
<h2>WARNINGS</h2>
<p> The warnings that can be given by <code>troff</code> are divided into the following categories. The name associated with each warning is used by the <code>-w</code> and <code>-W</code> options; the number is used by the <code>warn</code> request, and by the <code>.warn</code> register; it is always a power of 2 to allow bitwise composition. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Bit</td>
<td ALIGN=center>Code</td>
<td ALIGN=center>Warning</td>
<td ALIGN=center>Bit</td>
<td ALIGN=center>Code</td>
<td ALIGN=center>Warning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>0</td>
<td ALIGN=right><i>1</i></td>
<td><code>char</code></td>
<td ALIGN=right>10</td>
<td ALIGN=right><i>1024</i></td>
<td><code>reg</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td ALIGN=right><i>2</i></td>
<td><code>number</code></td>
<td ALIGN=right>11</td>
<td ALIGN=right><i>2048</i></td>
<td><code>tab</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td ALIGN=right><i>4</i></td>
<td><code>break</code></td>
<td ALIGN=right>12</td>
<td ALIGN=right><i>4096</i></td>
<td><code>right-brace</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td ALIGN=right><i>8</i></td>
<td><code>delim</code></td>
<td ALIGN=right>13</td>
<td ALIGN=right><i>8192</i></td>
<td><code>missing</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td ALIGN=right><i>16</i></td>
<td><code>el</code></td>
<td ALIGN=right>14</td>
<td ALIGN=right><i>16384</i></td>
<td><code>input</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5</td>
<td ALIGN=right><i>32</i></td>
<td><code>scale</code></td>
<td ALIGN=right>15</td>
<td ALIGN=right><i>32768</i></td>
<td><code>escape</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6</td>
<td ALIGN=right><i>64</i></td>
<td><code>range</code></td>
<td ALIGN=right>16</td>
<td ALIGN=right><i>65536</i></td>
<td><code>space</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7</td>
<td ALIGN=right><i>128</i></td>
<td><code>syntax</code></td>
<td ALIGN=right>17</td>
<td ALIGN=right><i>131072</i></td>
<td><code>font</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8</td>
<td ALIGN=right><i>256</i></td>
<td><code>di</code></td>
<td ALIGN=right>18</td>
<td ALIGN=right><i>262144</i></td>
<td><code>ig</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9</td>
<td ALIGN=right><i>512</i></td>
<td><code>mac</code></td>
<td ALIGN=right>19</td>
<td ALIGN=right><i>524288</i></td>
<td><code>color</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right></td>
<td ALIGN=right><i></i></td>
<td></td>
<td ALIGN=right>20</td>
<td ALIGN=right><i>1048576</i></td>
<td><code>file</code>
</td>
</tr>
</table>
</table>
<p></center> </p>
<dl>
<dt><code>break</code> 4</p>
<dd> In fill mode, lines which could not be broken so that their length was less than the line length. This is enabled by default.</p>
<dt><code>char</code> 1</p>
<dd> Non-existent characters. This is enabled by default.</p>
<dt><code>color</code> 524288</p>
<dd> Color-related warnings.</p>
<dt><code>delim</code> 8</p>
<dd> Missing or mismatched closing delimiters.</p>
<dt><code>di</code> 256</p>
<dd> Use of <code>di</code> or <code>da</code> without an argument when there is no current diversion.</p>
<dt><code>el</code> 16</p>
<dd> Use of the <code>el</code> request with no matching <code>ie</code> request.</p>
<dt><code>escape</code> 32768</p>
<dd> Unrecognized escape sequences. When an unrecognized escape sequence is encountered, the escape character is ignored.</p>
<dt><code>file</code> 1048576</p>
<dd> Indicates a missing file for the <code>mso</code> request. Enabled by default.</p>
<dt><code>font</code> 131072</p>
<dd> Non-existent fonts. This is enabled by default.</p>
<dt><code>ig</code> 262144</p>
<dd> Invalid escapes in text ignored with the <code>ig</code> request. These are conditions that are errors when they do not occur in ignored text.</p>
<dt><code>input</code> 16384</p>
<dd> Invalid input characters.</p>
<dt><code>mac</code> 512</p>
<dd> Use of undefined strings, macros and diversions. When an undefined string, macro or diversion is used, that string is automatically defined as empty. So, in most cases, at most one warning will be given for each name.</p>
<dt><code>missing</code> 8192</p>
<dd> Requests that are missing non-optional arguments.</p>
<dt><code>number</code> 2</p>
<dd> Invalid numeric expressions. This is enabled by default.</p>
<dt><code>range</code> 64</p>
<dd> Out of range arguments.</p>
<dt><code>reg</code> 1024</p>
<dd> Use of undefined number registers. When an undefined number register is used, that register is automatically defined to have a value of~0. So, in most cases, at most one warning will be given for use of a particular name.</p>
<dt><code>right-brace</code> 4096</p>
<dd> Use of <code>\}</code> where a number was expected.</p>
<dt><code>scale</code> 32</p>
<dd> Meaningless scaling indicators.</p>
<dt><code>space</code> 65536</p>
<dd> Missing space between a request or macro and its argument. This warning will be given when an undefined name longer than two characters is encountered, and the first two characters of the name make a defined name. The request or macro will not be invoked. When this warning is given, no macro is automatically defined. This is enabled by default. This warning will never occur in compatibility mode.</p>
<dt><code>syntax</code> 128</p>
<dd> Dubious syntax in numeric expressions.</p>
<dt><code>tab</code> 2048</p>
<dd> Inappropriate use of a tab character. Either use of a tab character where a number was expected, or use of tab character in an unquoted macro argument.</dl>
<p> There are also names that can be used to refer to groups of warnings:</p>
<dl>
<dt><code>all</code></p>
<dd> All warnings except <code>di</code>, <code>mac</code>, and <code>reg</code>. It is intended that this covers all warnings that are useful with traditional macro packages.</p>
<dt><code>w</code></p>
<dd> All warnings.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_TMAC_PATH</i></p>
<dd> A colon separated list of directories in which to search for macro files. <code>troff</code> will scan directories given in the <code>-M</code> option before these, and in standard directories (current directory if in unsafe mode, home directory, <i>/usr/lib/groff/site-tmac</i>, <i>/usr/share/groff/site-tmac</i>, <i>/usr/share/groff/1.22.4/tmac</i>) after these.</p>
<dt><i>GROFF_TYPESETTER</i></p>
<dd> Default device.</p>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A colon separated list of directories in which to search for the <i>dev</i>name directory. <code>troff</code> will scan directories given in the <code>-F</code> option before these, and in standard directories (<i>/usr/share/groff/site-font</i>, <i>/usr/share/groff/1.22.4/font</i>, <i>/usr/lib/font</i>) after these.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/groff/1.22.4/tmac/troffrc</i></p>
<dd> Initialization file (called before any other macro package).</p>
<dt><i>/usr/share/groff/1.22.4/tmac/troffrc-end</i></p>
<dd> Initialization file (called after any other macro package).</p>
<dt><i>/usr/share/groff/1.22.4/tmac/</i>name<i>.tmac</i></p>
<dd> <i>/usr/share/groff/1.22.4/tmac/tmac.</i>name Macro files</p>
<dt><i>/usr/share/groff/1.22.4/font/dev</i>name<i>/DESC</i></p>
<dd> Device description file for device <i>name</i>.</p>
<dt><i>/usr/share/groff/1.22.4/font/dev</i>name<i>/</i>F</p>
<dd> Font file for font <i>F</i> of device <i>name</i>.</dl>
<p> Note that <i>troffrc</i> and <i>troffrc-end</i> are searched for neither in the current nor the home directory by default for security reasons (even if the <code>-U</code> option is given). Use the <code>-M</code> command-line option or the <i>GROFF_TMAC_PATH</i> environment variable to add these directories to the search path if necessary.</p>
<h2>AUTHORS</h2>
<p> The GNU version of <i>troff</i> was originally written by James Clark; he also wrote the original version of this document, which was modified by Werner Lemberg and Bernd Warken</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)</p>
<dd> The main program of the <i>groff</i> system, a wrapper around <i>troff</i>.</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd> A description of the <i>groff</i> language, including a short but complete reference of all predefined requests, registers, and escapes of plain <i>groff</i>. From the command line, this is called by</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>man 7 groff</code></dl>
</dl>
<dt><code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7)</p>
<dd> The differences of the <i>groff</i> language and the <i>classical troff</i> language. Currently, this is the most actual document of the <i>groff</i> system.</p>
<dt><code><a href="/docs/linux/man/7-roff/">roff</a></code>(7)</p>
<dd> An overview over <i>groff</i> and other <i>roff</i> systems, including pointers to further related documentation.</dl>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with &#8220;info groff&#8221;. </p>
<h2>Index</h2>
