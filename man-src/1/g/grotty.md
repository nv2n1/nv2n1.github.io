---
title: "grotty(1)"
name: "grotty"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grotty/"
description: "grotty – groff driver for typewriter-like devices"
---

<h2 class="name">NAME</h2>
<p> grotty &#8211; groff driver for typewriter-like devices </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-bBcdfhioruUv</code> ] [ <code>-F </code><i>dir</i> ] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>grotty</code> translates the output of GNU <code>troff</code> into a form suitable for typewriter-like devices. Normally <code>grotty</code> should be invoked by using the <code>groff</code> command with a <code>-Tascii</code>, <code>-Tlatin1</code> or <code>-Tutf8</code> option on ASCII based systems, and with <code>-Tcp1047</code> and <code>-Tutf8</code> on EBCDIC based hosts. If no files are given, <code>grotty</code> reads the standard input. A filename of <code>&#8211;</code> also causes <code>grotty</code> to read the standard input. Output is written to the standard output. </p>
<p> By default, <code>grotty</code> emits SGR escape sequences (from ISO 6429, also called ANSI color escapes) to change text attributes (bold, italic, colors). This makes it possible to have eight different background and foreground colors; additionally, bold and italic attributes can be used at the same time (by using the BI font). </p>
<p> The following colors are defined in <code>tty.tmac</code>: black, white, red, green, blue, yellow, magenta, cyan. Unknown colors are mapped to the default color (which is dependent on the settings of the terminal; in most cases, this is black for the foreground and white for the background). </p>
<p> Use the <code>-c</code> switch to revert to the old behaviour, printing a bold character <i>c</i> with the sequence &#8220;<i>c</i> BACKSPACE <i>c</i>&#8221; and an italic character <i>c</i> by the sequence &#8220;<code>_</code> BACKSPACE <i>c</i>&#8220;. At the same time, color output is disabled. The same effect can be achieved by setting either the <i>GROFF_NO_SGR</i> environment variable or using the &#8216;sgr&#8217; X command (see below). </p>
<p> (Debian-specific: The old behaviour is the default when using the <code>man</code> and <code>mdoc</code> macro packages, because most pagers either fail to cope with SGR escape sequences or need special options to do so. SGR output can be re-enabled permanently by editing <i>/etc/groff/man.local</i> and <i>/etc/groff/mdoc.local</i>, or temporarily by setting the <i>GROFF_SGR</i> environment variable to something non-empty.) </p>
<p> For SGR support, it is necessary to use the <code>-R</code> option of <code><a href="/docs/linux/man/1-less/">less</a></code>(1) to disable the interpretation of <code>grotty</code>&#8216;s old output format. Consequently, all programs which use <code>less</code> as the pager program have to pass this option to it. For <code><a href="/docs/linux/man/1-man/">man</a></code>(1) in particular, either add <code>-R</code> to the <i>PAGER</i> environment variable, e.g.</p>
<dl>
<dt>
<dd>
<p> <code>PAGER=/usr/bin/less -R</code><br />
 <code>export PAGER</code></dl>
<p> or use the <code>-P</code> option of <code>man</code> to set the pager executable and its options, or modify the configuration file of <code>man</code> in a similar fashion. Note that with some <code><a href="/docs/linux/man/1-man/">man</a></code>(1) versions, you have to use the <i>MANPAGER</i> environment variable instead. </p>
<p> <code>grotty</code>&#8216;s old output format can be displayed on a terminal by piping through <code><a href="/docs/linux/man/1-ul/">ul</a></code>(1). Pagers such as <code><a href="/docs/linux/man/1-more/">more</a></code>(1) or <code><a href="/docs/linux/man/1-less/">less</a></code>(1) are also able to display these sequences. Use either <code>-B</code> or <code>-U</code> when piping into <code><a href="/docs/linux/man/1-less/">less</a></code>(1); use <code>-b</code> when piping into <code><a href="/docs/linux/man/1-more/">more</a></code>(1). There is no need to filter the output through <code><a href="/docs/linux/man/1-col/">col</a></code>(1) since <code>grotty</code> never outputs reverse line feeds. </p>
<p> The font description file may contain a command</p>
<dl>
<dt>
<dd> <code>internalname&nbsp;</code><i>n</i></dl>
<p> where <i>n</i> is a decimal integer. If the 01 bit in <i>n</i> is set, then the font is treated as an italic font; if the 02 bit is set, then it is treated as a bold font. The code field in the font description field gives the code which is used to output the character. This code can also be used in the <code>\N</code> escape sequence in <code>troff</code>. </p>
<p> If the <i>DESC</i> file contains the keyword <code>unicode</code>, <code>grotty</code> emits Unicode characters in UTF-8 encoding. Otherwise, it emits characters in a single-byte encoding depending on the data in the font description files. See the <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) man page for more details.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-b</code></p>
<dd> Suppress the use of overstriking for bold characters. Ignored if <code>-c</code> isn&#8217;t used.</p>
<dt><code>-B</code></p>
<dd> Use only overstriking for bold-italic characters. Ignored if <code>-c</code> isn&#8217;t used.</p>
<dt><code>-c</code></p>
<dd> Use <code>grotty</code>&#8216;s old output format (see above). This also disables color output. (Debian-specific: This option is enabled by default when using the <code>man</code> and <code>mdoc</code> macro packages. It can be disabled by default permanently by editing <i>/etc/groff/man.local</i> and <i>/etc/groff/mdoc.local</i>, or temporarily by setting the <i>GROFF_SGR</i> environment variable to something non-empty.)</p>
<dt><code>-d</code></p>
<dd> Ignore all <code>\D</code> commands. Without this <code>grotty</code> renders <code>\D&#8217;l&#8230;&#8217;</code> commands that have at least one zero argument (and so are either horizontal or vertical) using <code>&#8211;</code>, <code>|</code>, and <code>+</code> characters. In a similar way, <code>grotty</code> handles <code>\D&#8217;p&#8230;&#8217;</code> commands which consist entirely of horizontal and vertical lines.</p>
<dt><code>-f</code></p>
<dd> Use form feeds in the output. A form feed is output at the end of each page that has no output on its last line.</p>
<dt><code>-F</code><i>dir</i></p>
<dd> Prepend directory dir<i>/dev</i>name to the search path for font and device description files; <i>name</i> is the name of the device, usually <code>ascii</code>, <code>latin1</code>, <code>utf8</code>, or <code>cp1047</code>.</p>
<dt><code>-h</code></p>
<dd> Use horizontal tabs in the output. Tabs are assumed to be set every 8 columns.</p>
<dt><code>-i</code></p>
<dd> Use escape sequences to set the italic text attribute instead of the underline attribute for italic fonts (&#8216;I&#8217; and &#8216;BI&#8217;). Note that most terminals (including xterm) don&#8217;t support this. Ignored if <code>-c</code> is active.</p>
<dt><code>-o</code></p>
<dd> Suppress overstriking (other than for bold or underlined characters in case the old output format has been activated with <code>-c</code>).</p>
<dt><code>-r</code></p>
<dd> Use escape sequences to set the reverse text attribute instead of the underline attribute for italic fonts (&#8216;I&#8217; and &#8216;BI&#8217;). Ignored if <code>-c</code> is active.</p>
<dt><code>-u</code></p>
<dd> Suppress the use of underlining for italic characters. Ignored if <code>-c</code> isn&#8217;t used.</p>
<dt><code>-U</code></p>
<dd> Use only underlining for bold-italic characters. Ignored if <code>-c</code> isn&#8217;t used.</p>
<dt><code>-v</code></p>
<dd> Print the version number.</dl>
<h2>USAGE</h2>
<p> <code>grotty</code> understands a single X command produced using the <code>\X</code> escape sequence.</p>
<dl>
<dt><code>\X&#8217;tty: sgr&nbsp;</code><i>n</i><code>&#8216;</code></p>
<dd> If <i>n</i> is non-zero or missing, enable SGR output (this is the default), otherwise use the old drawing scheme for bold and underline.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_NO_SGR</i></p>
<dd> If set, the old drawing scheme for bold and underline (using the backspace character) is active. Colors are disabled.</p>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A list of directories in which to search for the <i>dev</i>name directory in addition to the default ones. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more details.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/groff/1.22.4/font/devascii/DESC</i></p>
<dd> Device description file for the <code>ascii</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devascii/</i>F</p>
<dd> Font description file for font <i>F</i> of the <code>ascii</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devlatin1/DESC</i></p>
<dd> Device description file for the <code>latin1</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devlatin1/</i>F</p>
<dd> Font description file for font <i>F</i> of the <code>latin1</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devutf8/DESC</i></p>
<dd> Device description file for the <code>utf8</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devutf8/</i>F</p>
<dd> Font description file for font <i>F</i> of the <code>utf8</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devcp1047/DESC</i></p>
<dd> Device description file for the <code>cp1047</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/font/devcp1047/</i>F</p>
<dd> Font description file for font <i>F</i> of the <code>cp1047</code> device.</p>
<dt><i>/usr/share/groff/1.22.4/tmac/tty.tmac</i></p>
<dd> Macros for use with <code>grotty</code>.</p>
<dt><i>/usr/share/groff/1.22.4/tmac/tty-char.tmac</i></p>
<dd> Additional character definitions for use with <code>grotty</code>.</dl>
<p> Note that on EBCDIC hosts, only files for the <code>cp1047</code> device is installed.</p>
<h2>BUGS</h2>
<p> <code>grotty</code> is intended only for simple documents. </p>
<p> There is no support for fractional horizontal or vertical motions. </p>
<p> There is no support for <code>\D</code> commands other than horizontal and vertical lines. </p>
<p> Characters above the first line (i.e. with a vertical position of~0) cannot be printed. </p>
<p> Color handling differs from <code><a href="/docs/linux/man/1-grops/">grops</a></code>(1). <code>\M</code> doesn&#8217;t set the fill color for closed graphic objects (which <code>grotty</code> doesn&#8217;t support anyway) but changes the background color of the character cell, affecting all subsequent operations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7), <code><a href="/docs/linux/man/1-ul/">ul</a></code>(1), <code><a href="/docs/linux/man/1-more/">more</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-less/">less</a></code>(1) </p>
<h2>Index</h2>
