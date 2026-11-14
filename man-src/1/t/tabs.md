---
title: "tabs(1)"
name: "tabs"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tabs/"
description: "tabs – set tabs on a terminal"
---

<h2 class="name">NAME</h2>
<p> <code>tabs</code> &#8211; set tabs on a terminal </p>
<h2>SYNOPSIS</h2>
<p> <code>tabs</code> [<i>options</i>]] <i>[tabstop-list]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>tabs</code> program clears and sets tab-stops on the terminal. This uses the terminfo <i>clear_all_tabs</i> and <i>set_tab</i> capabilities. If either is absent, <code>tabs</code> is unable to clear/set tab-stops. The terminal should be configured to use hard tabs, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
stty tab0
</pre>
<p>&nbsp;.in -4 </p>
<p> Like <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1), <code>tabs</code> writes to the standard output. You can redirect the standard output to a file (which prevents <code>tabs</code> from actually changing the tabstops), and later <code>cat</code> the file to the screen, setting tabstops at that point. </p>
<p> These are hardware tabs, which cannot be queried rapidly by applications running in the terminal, if at all. Curses and other full-screen applications may use hardware tabs in optimizing their output to the terminal. If the hardware tabstops differ from the information in the terminal database, the result is unpredictable. Before running curses programs, you should either reset tab-stops to the standard interval<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
tabs -8
</pre>
<p>&nbsp;.in -4 </p>
<p> or use the <code>reset</code> program, since the normal initialization sequences do not ensure that tab-stops are reset.</p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-T</code><i>name</i></p>
<dd> Tell <code>tabs</code> which terminal type to use. If this option is not given, <code>tabs</code> will use the <code>$TERM</code> environment variable. If that is not set, it will use the <i>ansi+tabs</i> entry.</p>
<dt><code>-d</code></p>
<dd> The debugging option shows a ruler line, followed by two data lines. The first data line shows the expected tab-stops marked with asterisks. The second data line shows the actual tab-stops, marked with asterisks.</p>
<dt><code>-n</code></p>
<dd> This option tells <code>tabs</code> to check the options and run any debugging option, but not to modify the terminal settings.</p>
<dt><code>-V</code></p>
<dd> reports the version of ncurses which was used in this program, and exits.</dl>
<p> The <code>tabs</code> program processes a single list of tab stops. The last option to be processed which defines a list is the one that determines the list to be processed.</p>
<h3>Implicit Lists</h3>
<p> Use a single number as an option, e.g., &#8220;<code>-5</code>&#8221; to set tabs at the given interval (in this case 1, 6, 11, 16, 21, etc.). Tabs are repeated up to the right margin of the screen. </p>
<p> Use &#8220;<code>-0</code>&#8221; to clear all tabs. </p>
<p> Use &#8220;<code>-8</code>&#8221; to set tabs to the standard interval.</p>
<h3>Explicit Lists</h3>
<p> An explicit list can be defined after the options (this does not use a &#8220;-&#8221;). The values in the list must be in increasing numeric order, and greater than zero. They are separated by a comma or a blank, for example,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
tabs 1,6,11,16,21
<br>
tabs 1 6 11 16 21
</pre>
<p>&nbsp;.in -4 </p>
<p> Use a &#8220;+&#8221; to treat a number as an increment relative to the previous value, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
tabs 1,+5,+5,+5,+5
</pre>
<p>&nbsp;.in -4 </p>
<p> which is equivalent to the 1,6,11,16,21 example.</p>
<h3>Predefined Tab-Stops</h3>
<p> POSIX defines several predefined lists of tab stops.</p>
<dl>
<dt><code>-a</code></p>
<dd> Assembler, IBM S/370, first format<br />
 1,10,16,36,72</p>
<dt><code>-a2</code></p>
<dd> Assembler, IBM S/370, second format<br />
 1,10,16,40,72</p>
<dt><code>-c</code></p>
<dd> COBOL, normal format<br />
 1,8,12,16,20,55</p>
<dt><code>-c2</code></p>
<dd> COBOL compact format<br />
 1,6,10,14,49</p>
<dt><code>-c3</code></p>
<dd> COBOL compact format extended<br />
 1,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,67</p>
<dt><code>-f</code></p>
<dd> FORTRAN<br />
 1,7,11,15,19,23</p>
<dt><code>-p</code></p>
<dd> PL/I<br />
 1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61</p>
<dt><code>-s</code></p>
<dd> SNOBOL<br />
 1,10,55</p>
<dt><code>-u</code></p>
<dd> UNIVAC 1100 Assembler<br />
 1,12,20,44</dl>
<h3>Margins</h3>
<p> A few terminals provide the capability for changing their left/right margins. The tabs program has an option to use this feature:</p>
<dl>
<dt><code>+m</code><i>&nbsp;margin</i></p>
<dd> The effect depends on whether the terminal has the margin capabilities:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the terminal provides the capability for setting the left margin, tabs uses this, and adjusts the available width for tab-stops.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the terminal does not provide the margin capabilities, tabs imitates the effect, putting the tab stops at the appropriate place on each line. The terminal&#8217;s left-margin is not modified.</dl>
<dt>
<dd> If the <i>margin</i> parameter is omitted, the default is 10. Use <code>+m0</code> to reset the left margin, i.e., to the left edge of the terminal&#8217;s display. Before setting a left-margin, tabs resets the margin to reduce problems which might arise on moving the cursor before the current left-margin.</dl>
<p> When setting or resetting the left-margin, tabs may reset the right-margin.</p>
<h2>PORTABILITY</h2>
<p> <i>IEEE Std 1003.1/The Open Group Base Specifications Issue 7</i> (POSIX.1-2008) describes a <code>tabs</code> utility. However<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 This standard describes a <code>+m</code> option, to set a terminal&#8217;s left-margin. Very few of the entries in the terminal database provide the <code>smgl</code> (<code>set_left_margin</code>) or <code>smglp</code> (<code>set_left_margin_parm</code>) capability needed to support the feature.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 There is no counterpart in X/Open Curses Issue 7 for this utility, unlike <code><a href="/docs/linux/man/1-tput/">tput</a></code>(1). </p>
<p> The <code>-d</code> (debug) and <code>-n</code> (no-op) options are extensions not provided by other implementations. </p>
<p> A <code>tabs</code> utility appeared in PWB/Unix 1.0 (1977). There was a reduced version of the <code>tabs</code> utility in Unix 7th edition and in 3BSD (1979). The latter supported a single &#8220;-n&#8221; option (to cause the first tab stop to be set on the left margin). That option is not documented by POSIX. </p>
<p> The PWB/Unix <code>tabs</code> utility, which was included in System III (1980), used built-in tables rather than the terminal database, to support a half-dozen hardcopy terminal (printer) types. It also had built-in logic to support the left-margin, as well as a feature for copying the tab settings from a file. </p>
<p> Later versions of Unix, e.g., SVr4, added support for the terminal database, but kept the tables to support the printers. In an earlier development effort, the tab-stop initialization provided by <code>tset</code> (1982) and incorporated into <code>tput</code> uses the terminal database, </p>
<p> The <code>+m</code> option was documented in the Base Specifications Issue 5 (Unix98, 1997), and omitted in Issue 6 (Unix03, 2004) without documenting the rationale, though an introductory comment <i>&#8220;and optionally adjusts the margin&#8221;</i> remains, overlooked in the removal. The documented <code>tabs</code> utility in Issues 6 and later has no mechanism for setting margins. The <code>+m</code> option in this implementation differs from the feature in SVr4 by using terminal capabilities rather than built-in tables. </p>
<p> POSIX documents no limits on the number of tab stops. Documentation for other implementations states that there is a limit on the number of tab stops (e.g., 20 in PWB/Unix&#8217;s <code>tabs</code> utility). While some terminals may not accept an arbitrary number of tab stops, this implementation will attempt to set tab stops up to the right margin of the screen, if the given list happens to be that long. </p>
<p> The <i>Rationale</i> section of the POSIX documentation goes into some detail about the ways the committee considered redesigning the <code>tabs</code> and <code>tput</code> utilities, without proposing an improved solution. It comments that</p>
<dl>
<dt>
<dd>
<p> no known historical version of tabs supports the capability of setting arbitrary tab stops.</dl>
<p> However, the <i>Explicit Lists</i> described in this manual page were implemented in PWB/Unix. Those provide the capability of setting abitrary tab stops.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1), <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1), <code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5). </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
<h2>Index</h2>
