---
title: "clear(1)"
name: "clear"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clear/"
description: "clear – clear the terminal screen"
---

<h2 class="name">NAME</h2>
<p> <code>clear</code> &#8211; clear the terminal screen </p>
<h2>SYNOPSIS</h2>
<p> <code>clear</code> [<code>-T</code><i>type</i>] [<code>-V</code>] [<code>-x</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>clear</code> clears your screen if this is possible, including its scrollback buffer (if the extended &#8220;E3&#8221; capability is defined). <code>clear</code> looks in the environment for the terminal type given by the environment variable <code>TERM</code>, and then in the <code>terminfo</code> database to determine how to clear the screen. </p>
<p> <code>clear</code> writes to the standard output. You can redirect the standard output to a file (which prevents <code>clear</code> from actually clearing the screen), and later <code>cat</code> the file to the screen, clearing it at that point.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-T </code><i>type</i></p>
<dd> indicates the <i>type</i> of terminal. Normally this option is unnecessary, because the default is taken from the environment variable <code>TERM</code>. If <code>-T</code> is specified, then the shell variables <code>LINES</code> and <code>COLUMNS</code> will also be ignored.</p>
<dt><code>-V</code></p>
<dd> reports the version of ncurses which was used in this program, and exits. The options are as follows:</p>
<dt><code>-x</code></p>
<dd> do not attempt to clear the terminal&#8217;s scrollback buffer using the extended &#8220;E3&#8221; capability.</dl>
<h2>HISTORY</h2>
<p> A <code>clear</code> command appeared in 2.79BSD dated February 24, 1979. Later that was provided in Unix 8th edition (1985). </p>
<p> AT&amp;T adapted a different BSD program (<code>tset</code>) to make a new command (<code>tput</code>), and used this to replace the <code>clear</code> command with a shell script which calls <code>tput clear</code>, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
/usr/bin/tput ${1:+-T$1} clear 2&gt; /dev/null
exit
</pre>
<p>&nbsp;.in -4 </p>
<p> In 1989, when Keith Bostic revised the BSD <code>tput</code> command to make it similar to the AT&amp;T <code>tput</code>, he added a shell script for the <code>clear</code> command:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
exec tput clear
</pre>
<p>&nbsp;.in -4 </p>
<p> The remainder of the script in each case is a copyright notice. </p>
<p> The ncurses <code>clear</code> command began in 1995 by adapting the original BSD <code>clear</code> command (with terminfo, of course). </p>
<p> The <code>E3</code> extension came later:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In June 1999, xterm provided an extension to the standard control sequence for clearing the screen. Rather than clearing just the visible part of the screen using<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
printf '[2J'
</pre>
<p>&nbsp;.in -4</p>
<dl>
<dt>
<dd> one could clear the <i>scrollback</i> using<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
printf '[<code>3</code>J'
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> This is documented in <i>XTerm Control Sequences</i> as a feature originating with xterm.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 A few other terminal developers adopted the feature, e.g., PuTTY in 2006.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In April 2011, a Red Hat developer submitted a patch to the Linux kernel, modifying its console driver to do the same thing. The Linux change, part of the 3.0 release, did not mention xterm, although it was cited in the Red Hat bug report (#683733) which led to the change.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Again, a few other terminal developers adopted the feature. But the next relevant step was a change to the <code>clear</code> program in 2013 to incorporate this extension.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In 2013, the <code>E3</code> extension was overlooked in <code>tput</code> with the &#8220;clear&#8221; parameter. That was addressed in 2016 by reorganizing <code>tput</code> to share its logic with <code>clear</code> and <code>tset</code>.</dl>
<h2>PORTABILITY</h2>
<p> Neither IEEE Std 1003.1/The Open Group Base Specifications Issue 7 (POSIX.1-2008) nor X/Open Curses Issue 7 documents tset or reset. </p>
<p> The latter documents <code>tput</code>, which could be used to replace this utility either via a shell script or by an alias (such as a symbolic link) to run <code>tput</code> as <code>clear</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tput/">tput</a></code>(1), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
<h2>Index</h2>
