---
title: "nroff(1)"
name: "nroff"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nroff/"
description: "nroff – use groff to format documents for TTY devices"
---

<h2 class="name">NAME</h2>
<p> nroff &#8211; use groff to format documents for TTY devices </p>
<h2>SYNOPSIS</h2>
<p> [<code>-CchipStUv</code>] [<code>-d</code><i>cs</i>] [<code>-M</code><i>dir</i>] [<code>-m</code><i>name</i>] [<code>-n</code><i>num</i>] [<code>-o</code><i>list</i>] [<code>-r</code><i>cn</i>] [<code>-T</code><i>name</i>] [<code>-W</code><i>warning</i>] [<code>-w</code><i>warning</i>] [<i>file</i> &#8230;] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>nroff</i> formats documents written in the <i><a href="/docs/linux/man/7-roff/">roff</a></i>(7) language for typewriter-like devices such as terminal emulators. </p>
<p> GNU <i>nroff</i> emulates the traditional Unix <i>nroff</i> command using <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1). <i>nroff</i> generates output via <i><a href="/docs/linux/man/1-grotty/">grotty</a></i>(1), <i>groff</i>&#8216;s TTY output device, which needs to know the character encoding scheme used by the terminal. Consequently, acceptable arguments to the <code>-T</code> option are <code>ascii</code>, <code>latin1</code>, <code>utf8</code>, and <code>cp1047</code>; any others are ignored. If neither the <i>GROFF_TYPESETTER</i> environment variable nor the <code>-T</code> command-line option (which overrides the environment variable) specifies a (valid) device, <i>nroff</i> consults the locale to select an appropriate output device. It first tries the <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) program, then checks several locale-related environment variables; see &#8220;ENVIRONMENT&#8221;, below. If all of the foregoing fail, <code>-Tascii</code> is implied. </p>
<p> Whitespace is not permitted between an option and its argument. The <code>-h</code> and <code>-c</code> options are equivalent to <i>grotty</i>&#8216;s options <code>-h</code> (using tabs in the output) and <code>-c</code> (using the old output scheme instead of SGR escape sequences). The <code>-d</code>, <code>-C</code>, <code>-i</code>, <code>-M</code>, <code>-m</code>, <code>-n</code>, <code>-o</code>, <code>-r</code>, <code>-w</code>, and <code>-W</code> options have the effect described in <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). In addition, <i>nroff</i> ignores <code>-e</code>, <code>-q</code>, and <code>-s</code> (which are not implemented in <i>troff</i>). The options <code>-p</code> (pic), <code>-t</code> (tbl), <code>-S</code> (safer), and <code>-U</code> (unsafe) are passed to <i>groff</i>. <code>-v</code> and <code>&#8211;version</code> show version information, while <code>&#8211;help</code> displays a usage message; all exit afterward.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_TYPESETTER</i></p>
<dd> specifies the default output device for <i>groff</i>.</p>
<dt><i>GROFF_BIN_PATH</i></p>
<dd> is a colon-separated list of directories in which to search for the <i>groff</i> executable before searching in <i>PATH</i>. If unset, <i>/usr/bin</i> is used.</p>
<dt><i>LC_ALL</i></p>
<dd> <i>LC_CTYPE</i> <i>LANG</i> <i>LESSCHARSET</i> are pattern-matched in this order for standard character encodings supported by <i>groff</i> in the event no <code>-T</code> option is given and <i>GROFF_TYPESETTER</i> is unset.</dl>
<h2>NOTES</h2>
<p> Character definitions in the file <i>/usr/share/groff/1.22.4/tmac/tty-char.tmac</i> are loaded to replace unrepresentable glyphs.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1), <i><a href="/docs/linux/man/1-grotty/">grotty</a></i>(1), <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1), <i><a href="/docs/linux/man/7-roff/">roff</a></i>(7) </p>
<h2>Index</h2>
