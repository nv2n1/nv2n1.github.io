---
title: "pg(1)"
name: "pg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg/"
description: "pg – browse pagewise through text files"
---

<h2 class="name">NAME</h2>
<p> pg &#8211; browse pagewise through text files </p>
<h2>SYNOPSIS</h2>
<p> <code>pg</code> [<code>&#8211;</code><i>number</i>] [<code>-p</code> <i>string</i>] [<code>-cefnrs</code>] [<code>+</code><i>line</i>] [<code>+/</code><i>pattern</i>/] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pg</code> displays a text file on a <font SIZE="-1">CRT</font> one screenful at once. After each page, a prompt is displayed. The user may then either press the newline key to view the next page or one of the keys described below. </p>
<p> If no filename is given on the command line, <code>pg</code> reads from standard input. If standard output is not a terminal, <code>pg</code> acts like <i><a href="/docs/linux/man/1-cat/">cat</a></i>(1) but precedes each file with its name if there is more than one. </p>
<p> If input comes from a pipe, <code>pg</code> stores the data in a buffer file while reading to make navigation possible.</p>
<h2>OPTIONS</h2>
<p> <code>pg</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;</code><i>number</i></p>
<dd> The number of lines per page. Usually, this is the number of <font SIZE="-1">CRT</font> lines minus one.</p>
<dt><code>-c</code></p>
<dd> Clear the screen before a page is displayed, if the terminfo entry for the terminal provides this capability.</p>
<dt><code>-e</code></p>
<dd> Do not pause and display <font SIZE="-1">(EOF)</font> at the end of a file.</p>
<dt><code>-f</code></p>
<dd> Do not split long lines.</p>
<dt><code>-n</code></p>
<dd> Without this option, commands must be terminated by a newline character. With this option, <code>pg</code> advances once a command letter is entered.</p>
<dt><code>-p</code><i>&nbsp;<wbr>string</i></p>
<dd> Instead of the normal prompt <i>:</i>, <i>string</i> is displayed. If <i>string</i> contains <i>%d</i>, its first occurrence is replaced by the number of the current page.</p>
<dt><code>-r</code></p>
<dd> Disallow the shell escape.</p>
<dt><code>-s</code></p>
<dd> Print messages in <i>standout</i> mode, if the terminfo entry for the terminal provides this capability.</p>
<dt><code>+</code><i>number</i></p>
<dd> Start at the given line.</p>
<dt><code>+/</code><i>pattern</i><code>/</code></p>
<dd> Start at the line containing the Basic Regular Expression <i>pattern</i> given.</dl>
<h2>USAGE</h2>
<p> The following commands may be entered at the prompt. Commands preceded by <i>i</i> in this document accept a number as argument, positive or negative. If this argument starts with <i>+</i> or <i>-,</i> it is interpreted relative to the current position in the input file, otherwise relative to the beginning.</p>
<dl>
<dt><i>i</i><code>&lt;newline&gt;</code></p>
<dd> Display the next or the indicated page.</p>
<dt><i>i</i><code>d</code> or <code>^D</code></p>
<dd> Display the next halfpage. If <i>i</i> is given, it is always interpreted relative to the current position.</p>
<dt><i>i</i><code>l</code></p>
<dd> Display the next or the indicated line.</p>
<dt><i>i</i><code>f</code></p>
<dd> Skip a page forward. <i>i</i> must be a positive number and is always interpreted relative to the current position.</p>
<dt><i>i</i><code>w</code> or <i>i</i><code>z</code></p>
<dd> Behave as <i>&lt;newline&gt;</i> except that <i>i</i> becomes the new page size.</p>
<dt><code>.</code> or <code>^L</code></p>
<dd> Redraw the screen.</p>
<dt><code>$</code></p>
<dd> Advance to the last line of the input file.</p>
<dt><i>i</i><code>/</code><i>pattern</i><code>/</code></p>
<dd> Search forward until the first or the <i>i</i>-th occurrence of the Basic Regular Expression <i>pattern</i> is found. The search starts after the current page and stops at the end of the file. No wrap-around is performed. <i>i</i> must be a positive number.</p>
<dt><i>i</i><code>?</code><i>pattern</i><code>?</code> or <i>i</i><code>^</code><i>pattern</i><code>^</code></p>
<dd> Search backward until the first or the <i>i</i>-th occurrence of the Basic Regular Expression <i>pattern</i> is found. The search starts before the current page and stops at the beginning of the file. No wrap-around is performed. <i>i</i> must be a positive number.</dl>
<p> The search commands accept an added letter. If <code>t</code> is given, the line containing the pattern is displayed at the top of the screen, which is the default. <code>m</code> selects the middle and <code>b</code> the bottom of the screen. The selected position is used in following searches, too.</p>
<dl>
<dt><i>i</i><code>n</code></p>
<dd> Advance to the next file or <i>i</i> files forward.</p>
<dt><i>i</i><code>p</code></p>
<dd> Reread the previous file or <i>i</i> files backward.</p>
<dt><code>s</code><i>&nbsp;<wbr>filename</i></p>
<dd> Save the current file to the given <i>filename.</i></p>
<dt><code>h</code></p>
<dd> Display a command summary.</p>
<dt><code>!</code><i>command</i></p>
<dd> Execute <i>command</i> using the shell.</p>
<dt><code>q</code> or <code>Q</code></p>
<dd> Quit.</dl>
<p> If the user presses the interrupt or quit key while <code>pg</code> reads from the input file or writes on the terminal, <code>pg</code> will immediately display the prompt. In all other situations these keys will terminate <code>pg</code>.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables affect the behaviour of <code>pg</code>:</p>
<dl>
<dt><code>COLUMNS</code></p>
<dd> Overrides the system-supplied number of columns if set.</p>
<dt><code>LANG</code>,&nbsp;<wbr><code>LC_ALL</code>,&nbsp;<wbr><code>LC_COLLATE</code>,&nbsp;<wbr><code>LC_CTYPE</code>,&nbsp;<wbr><code>LC_MESSAGES</code></p>
<dd> See <i><a href="/docs/linux/man/7-locale/">locale</a></i>(7).</p>
<dt><code>LINES</code></p>
<dd> Overrides the system-supplied number of lines if set.</p>
<dt><code>SHELL</code></p>
<dd> Used by the <code>!</code> command.</p>
<dt><code>TERM</code></p>
<dd> Determines the terminal type.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/1-more/">more</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-term/">term</a></code>(7)</p>
<h2>NOTES</h2>
<p> <code>pg</code> expects the terminal tabulators to be set every eight positions. </p>
<p> Files that include <font SIZE="-1">NUL</font> characters cannot be displayed by <code>pg</code>.</p>
<h2>AVAILABILITY</h2>
<p> The pg command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a> </p>
<h2>Index</h2>
