---
title: "captoinfo(1)"
name: "captoinfo"
section: "1"
letter: "c"
url: "/docs/linux/man/1-captoinfo/"
description: "captoinfo – convert a termcap description into a terminfo description"
---

<h2 class="name">NAME</h2>
<p> <code>captoinfo</code> &#8211; convert a <i>termcap</i> description into a <i>terminfo</i> description </p>
<h2>SYNOPSIS</h2>
<p> <code>captoinfo</code> [<code>-v</code><i>n</i> <i>width</i>] [<code>-V</code>] [<code>-1</code>] [<code>-w</code> <i>width</i>] <i>file</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>captoinfo</code> looks in each given text <i>file</i> for <code>termcap</code> descriptions. For each one found, an equivalent <code>terminfo</code> description is written to standard output. Termcap <code>tc</code> capabilities are translated directly to terminfo <code>use</code> capabilities. </p>
<p> If no <i>file</i> is given, then the environment variable <code>TERMCAP</code> is used for the filename or entry. If <code>TERMCAP</code> is a full pathname to a file, only the terminal whose name is specified in the environment variable <code>TERM</code> is extracted from that file. If the environment variable <code>TERMCAP</code> is not set, then the file <code>/etc/terminfo</code> is read.</p>
<dl>
<dt><code>-v</code></p>
<dd> print out tracing information on standard error as the program runs.</p>
<dt><code>-V</code></p>
<dd> print out the version of the program in use on standard error and exit.</p>
<dt><code>-1</code></p>
<dd> cause the fields to print out one to a line. Otherwise, the fields will be printed several to a line to a maximum width of 60 characters.</p>
<dt><code>-w</code></p>
<dd> change the output to <i>width</i> characters.</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/terminfo</p>
<dd> Compiled terminal description database.</dl>
<h2>TRANSLATIONS FROM NONSTANDARD CAPABILITIES</h2>
<p> Some obsolete nonstandard capabilities will automatically be translated into standard (SVr4/XSI Curses) terminfo capabilities by <code>captoinfo</code>. Whenever one of these automatic translations is done, the program will issue an notification to stderr, inviting the user to check that it has not mistakenly translated a completely unknown and random capability and/or syntax error. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>Nonstd</td>
<td ALIGN=center>Std</td>
<td ALIGN=center>From</td>
<td ALIGN=center>Terminfo
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>name</td>
<td ALIGN=center>name</td>
<td ALIGN=center></td>
<td ALIGN=center>capability
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>BO</td>
<td>mr</td>
<td>AT&amp;T</td>
<td>enter_reverse_mode
</td>
</tr>
<tr VALIGN=top>
<td>CI</td>
<td>vi</td>
<td>AT&amp;T</td>
<td>cursor_invisible
</td>
</tr>
<tr VALIGN=top>
<td>CV</td>
<td>ve</td>
<td>AT&amp;T</td>
<td>cursor_normal
</td>
</tr>
<tr VALIGN=top>
<td>DS</td>
<td>mh</td>
<td>AT&amp;T</td>
<td>enter_dim_mode
</td>
</tr>
<tr VALIGN=top>
<td>EE</td>
<td>me</td>
<td>AT&amp;T</td>
<td>exit_attribute_mode
</td>
</tr>
<tr VALIGN=top>
<td>FE</td>
<td>LF</td>
<td>AT&amp;T</td>
<td>label_on
</td>
</tr>
<tr VALIGN=top>
<td>FL</td>
<td>LO</td>
<td>AT&amp;T</td>
<td>label_off
</td>
</tr>
<tr VALIGN=top>
<td>XS</td>
<td>mk</td>
<td>AT&amp;T</td>
<td>enter_secure_mode
</td>
</tr>
<tr VALIGN=top>
<td>EN</td>
<td>@7</td>
<td>XENIX</td>
<td>key_end
</td>
</tr>
<tr VALIGN=top>
<td>GE</td>
<td>ae</td>
<td>XENIX</td>
<td>exit_alt_charset_mode
</td>
</tr>
<tr VALIGN=top>
<td>GS</td>
<td>as</td>
<td>XENIX</td>
<td>enter_alt_charset_mode
</td>
</tr>
<tr VALIGN=top>
<td>HM</td>
<td>kh</td>
<td>XENIX</td>
<td>key_home
</td>
</tr>
<tr VALIGN=top>
<td>LD</td>
<td>kL</td>
<td>XENIX</td>
<td>key_dl
</td>
</tr>
<tr VALIGN=top>
<td>PD</td>
<td>kN</td>
<td>XENIX</td>
<td>key_npage
</td>
</tr>
<tr VALIGN=top>
<td>PN</td>
<td>po</td>
<td>XENIX</td>
<td>prtr_off
</td>
</tr>
<tr VALIGN=top>
<td>PS</td>
<td>pf</td>
<td>XENIX</td>
<td>prtr_on
</td>
</tr>
<tr VALIGN=top>
<td>PU</td>
<td>kP</td>
<td>XENIX</td>
<td>key_ppage
</td>
</tr>
<tr VALIGN=top>
<td>RT</td>
<td>@8</td>
<td>XENIX</td>
<td>kent
</td>
</tr>
<tr VALIGN=top>
<td>UP</td>
<td>ku</td>
<td>XENIX</td>
<td>kcuu1
</td>
</tr>
<tr VALIGN=top>
<td>KA</td>
<td>k;</td>
<td>Tek</td>
<td>key_f10
</td>
</tr>
<tr VALIGN=top>
<td>KB</td>
<td>F1</td>
<td>Tek</td>
<td>key_f11
</td>
</tr>
<tr VALIGN=top>
<td>KC</td>
<td>F2</td>
<td>Tek</td>
<td>key_f12
</td>
</tr>
<tr VALIGN=top>
<td>KD</td>
<td>F3</td>
<td>Tek</td>
<td>key_f13
</td>
</tr>
<tr VALIGN=top>
<td>KE</td>
<td>F4</td>
<td>Tek</td>
<td>key_f14
</td>
</tr>
<tr VALIGN=top>
<td>KF</td>
<td>F5</td>
<td>Tek</td>
<td>key_f15
</td>
</tr>
<tr VALIGN=top>
<td>BC</td>
<td>Sb</td>
<td>Tek</td>
<td>set_background
</td>
</tr>
<tr VALIGN=top>
<td>FC</td>
<td>Sf</td>
<td>Tek</td>
<td>set_foreground
</td>
</tr>
<tr VALIGN=top>
<td>HS</td>
<td>mh</td>
<td>Iris</td>
<td>enter_dim_mode
</td>
</tr>
</table>
<p> XENIX termcap also used to have a set of extension capabilities for forms drawing, designed to take advantage of the IBM PC high-half graphics. They were as follows: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>Cap</td>
<td ALIGN=center>Graphic
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>G2</td>
<td>upper left
</td>
</tr>
<tr VALIGN=top>
<td>G3</td>
<td>lower left
</td>
</tr>
<tr VALIGN=top>
<td>G1</td>
<td>upper right
</td>
</tr>
<tr VALIGN=top>
<td>G4</td>
<td>lower right
</td>
</tr>
<tr VALIGN=top>
<td>GR</td>
<td>pointing right
</td>
</tr>
<tr VALIGN=top>
<td>GL</td>
<td>pointing left
</td>
</tr>
<tr VALIGN=top>
<td>GU</td>
<td>pointing up
</td>
</tr>
<tr VALIGN=top>
<td>GD</td>
<td>pointing down
</td>
</tr>
<tr VALIGN=top>
<td>GH</td>
<td>horizontal line
</td>
</tr>
<tr VALIGN=top>
<td>GV</td>
<td>vertical line
</td>
</tr>
<tr VALIGN=top>
<td>GC</td>
<td>intersection
</td>
</tr>
<tr VALIGN=top>
<td>G6</td>
<td>upper left
</td>
</tr>
<tr VALIGN=top>
<td>G7</td>
<td>lower left
</td>
</tr>
<tr VALIGN=top>
<td>G5</td>
<td>upper right
</td>
</tr>
<tr VALIGN=top>
<td>G8</td>
<td>lower right
</td>
</tr>
<tr VALIGN=top>
<td>Gr</td>
<td>tee pointing right
</td>
</tr>
<tr VALIGN=top>
<td>Gr</td>
<td>tee pointing left
</td>
</tr>
<tr VALIGN=top>
<td>Gu</td>
<td>tee pointing up
</td>
</tr>
<tr VALIGN=top>
<td>Gd</td>
<td>tee pointing down
</td>
</tr>
<tr VALIGN=top>
<td>Gh</td>
<td>horizontal line
</td>
</tr>
<tr VALIGN=top>
<td>Gv</td>
<td>vertical line
</td>
</tr>
<tr VALIGN=top>
<td>Gc</td>
<td>intersection
</td>
</tr>
<tr VALIGN=top>
<td>GG</td>
<td>acs magic cookie count
</td>
</tr>
</table>
<p> If the single-line capabilities occur in an entry, they will automatically be composed into an <code>acsc</code> string. The double-line capabilities and <code>GG</code> are discarded with a warning message. </p>
<p> IBM&#8217;s AIX has a terminfo facility descended from SVr1 terminfo but incompatible with the SVr4 format. The following AIX extensions are automatically translated: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>IBM</td>
<td ALIGN=center>XSI
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ksel</td>
<td>kslt
</td>
</tr>
<tr VALIGN=top>
<td>kbtab</td>
<td>kcbt
</td>
</tr>
<tr VALIGN=top>
<td>font0</td>
<td>s0ds
</td>
</tr>
<tr VALIGN=top>
<td>font1</td>
<td>s1ds
</td>
</tr>
<tr VALIGN=top>
<td>font2</td>
<td>s2ds
</td>
</tr>
<tr VALIGN=top>
<td>font3</td>
<td>s3ds
</td>
</tr>
</table>
<p> Additionally, the AIX <i>box1</i> capability will be automatically translated to an <code>acsc</code> string. </p>
<p> Hewlett-Packard&#8217;s terminfo library supports two nonstandard terminfo capabilities <code>meml</code> (memory lock) and <code>memu</code> (memory unlock). These will be discarded with a warning message.</p>
<h2>NOTES</h2>
<p> This utility is actually a link to <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1), running in <i>-I</i> mode. You can use other <code>tic</code> options such as <code>-f</code> and <code>-x</code>. </p>
<p> The verbose option is not identical to SVr4&#8217;s. Under SVr4, instead of following the <code>-v</code> with a trace level n, you repeat it n times.</p>
<h2>PORTABILITY</h2>
<p> X/Open Curses, Issue 7 (2009) describes <code>tic</code> briefly, but omits this program. SVr4 systems provide <code>captoinfo</code> as a separate application from <code>tic</code>. </p>
<p> NetBSD does not provide this application.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1), <code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] snark.thyrsus.com&gt; and<br />
 Thomas E. Dickey &lt;dickey [at] invisible-island.net&gt; </p>
<h2>Index</h2>
