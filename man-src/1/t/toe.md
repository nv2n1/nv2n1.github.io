---
title: "toe(1)"
name: "toe"
section: "1"
letter: "t"
url: "/docs/linux/man/1-toe/"
description: "toe – table of (terminfo) entries"
---

<h2 class="name">NAME</h2>
<p> <code>toe</code> &#8211; table of (terminfo) entries </p>
<h2>SYNOPSIS</h2>
<p> <code>toe</code> [<code>-v</code>[<i>n</i>]] [<code>-ahsuUV</code>] <i>file&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> With no options, <code>toe</code> lists all available terminal types by primary name with descriptions. File arguments specify the directories to be scanned; if no such arguments are given, your default terminfo directory is scanned. If you also specify the <code>-h</code> option, a directory header will be issued as each directory is entered. </p>
<p> There are other options intended for use by terminfo file maintainers:</p>
<dl>
<dt><code>-a</code></p>
<dd> report on all of the terminal databases which ncurses would search, rather than only the first one that it finds.</p>
<dt>
<dd> If the <code>-s</code> is also given, <code>toe</code> adds a column to the report, showing (like <code><a href="/docs/linux/man/1-conflict/">conflict</a></code>(1)) which entries which belong to a given terminal database. An &quot;*&quot; marks entries which differ, and &quot;+&quot; marks equivalent entries.</p>
<dt>
<dd> Without the <code>-s</code> option, <code>toe</code> does not attempt to merge duplicates in its report</p>
<dt><code>-s</code></p>
<dd> sort the output by the entry names.</p>
<dt><code>-u</code> <i>file</i></p>
<dd> says to write a report to the standard output, listing dependencies in the given terminfo/termcap source file. The report condenses the &#8220;use&#8221; relation: each line consists of the primary name of a terminal that has use capabilities, followed by a colon, followed by the whitespace-separated primary names of all terminals which occur in those use capabilities, followed by a newline</p>
<dt><code>-U</code> <i>file</i></p>
<dd> says to write a report to the standard output, listing reverse dependencies in the given terminfo/termcap source file. The report reverses the &#8220;use&#8221; relation: each line consists of the primary name of a terminal that occurs in use capabilities, followed by a colon, followed by the whitespace-separated primary names of all terminals which depend on it, followed by a newline.</p>
<dt><code>-v</code><i>n</i></p>
<dd> specifies that (verbose) output be written to standard error, showing <code>toe</code>&#8216;s progress.</p>
<dt>
<dd> The optional parameter <i>n</i> is a number from 1 to 10, interpreted as for <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1). If ncurses is built without tracing support, the optional parameter is ignored.</p>
<dt><code>-V</code></p>
<dd> reports the version of ncurses which was used in this program, and exits.</dl>
<h2>EXAMPLES</h2>
<p> Without sorting, the <code>-a</code> option reports all of the names found in all of the terminal databases found by the <code>TERMINFO</code> and <code>TERMINFO_DIRS</code> environment variables:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
MtxOrb162       16x2 Matrix Orbital LCD display
MtxOrb204       20x4 Matrix Orbital LCD display
MtxOrb          Generic Matrix Orbital LCD display
qvt101+         qume qvt 101 PLUS product
qvt119+-25      QVT 119 PLUS with 25 data lines
qansi-g         QNX ANSI
qvt103          qume qvt 103
qnxw            QNX4 windows
qansi-w         QNX ansi for windows
qnxm            QNX4 with mouse events
qvt203-25-w     QVT 203 PLUS with 25 by 132 columns
qansi-t         QNX ansi without console writes
. . .
</pre>
<p>&nbsp;.in -4 </p>
<p> Use the <code>-a</code> and <code>-s</code> options together to show where each terminal description was found:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre><code>
--&gt; /usr/local/ncurses/share/terminfo
----&gt; /usr/share/terminfo
*-+-:   9term           Plan9 terminal emulator for X
*---:   Eterm           Eterm with xterm-style color support (X Window System)
*-*-:   Eterm-256color  Eterm with xterm 256-colors
*-*-:   Eterm-88color   Eterm with 88 colors
*-+-:   MtxOrb          Generic Matrix Orbital LCD display
*-+-:   MtxOrb162       16x2 Matrix Orbital LCD display
*-+-:   MtxOrb204       20x4 Matrix Orbital LCD display
*-*-:   NCR260VT300WPP  NCR 2900_260 vt300 wide mode pc+  kybd
*-+-:   aaa             ann arbor ambassador/30 lines
*-+-:   aaa+dec         ann arbor ambassador in dec vt100 mode
*-+-:   aaa+rv          ann arbor ambassador in reverse video
. . .
</code></pre>
<p>&nbsp;.in -4</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/terminfo/?/*</code></p>
<dd> Compiled terminal description database.</dl>
<h2>HISTORY</h2>
<p> This utility is not provided by other implementations. There is no relevant X/Open or POSIX standard for <code>toe</code>. </p>
<p> The program name refers to a developer&#8217;s pun:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>tic</code>,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>tac</code> (now <code>tack</code>),<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>toe</code>. </p>
<p> It replaced a <code>-T</code> option which was briefly supported by the ncurses <code>infocmp</code> utility in 1995. </p>
<p> The <code>-a</code> and <code>-s</code> options were added to <code>toe</code> several years later (2006 and 2011, respectively).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-captoinfo/">captoinfo</a></code>(1), <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1), <code><a href="/docs/linux/man/1-infotocap/">infotocap</a></code>(1), <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1), <code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5). </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
<h2>Index</h2>
