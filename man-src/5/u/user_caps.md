---
title: "user_caps(5)"
name: "user_caps"
section: "5"
letter: "u"
url: "/docs/linux/man/5-user_caps/"
description: "user_caps – user-defined terminfo capabilities"
---

<p>user_caps &#8211; user-defined terminfo capabilities</p>
<h2>Synopsis</h2>
<p><code>tic -x, infocmp -x</code></p>
<h2>Description</h2>
<h3>Background</h3>
<p>Before ncurses 5.0, terminfo databases used a <i>fixed repertoire</i> of terminal capabilities designed for the SVr2 terminal database in 1984, and extended in stages through SVr4 (1989), and standardized in the Single Unix Specification beginning in 1995. Most of the <i>extensions</i> in this fixed repertoire were additions to the tables of boolean, numeric and string capabilities. Rather than change the meaning of an existing capability, a new name was added. The terminfo database uses a binary format; binary compatibility was ensured by using a header which gave the number of items in the tables for each type of capability. The standardization was incomplete:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <i>binary format</i> itself is not described in the X/Open Curses documentation. Only the <i>source format</i> is described.</p>
<dl>
<dd>Library developers rely upon the SVr4 documentation, and reverse-engineering the compiled terminfo files to match the binary format.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Lacking a standard for the binary format, most implementations copy the SVr2 binary format, which uses 16-bit signed integers, and is limited to 4096-byte entries.</p>
<dd>The format cannot represent very large numeric capabilities, nor can it represent large numbers of special keyboard definitions.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The tables of capability names differ between implementations.</p>
<dd>Although they <i>may</i> provide all of the standard capability names, the position in the tables differs because some features were added as needed, while others were added (out of order) to comply with X/Open Curses.</p>
<dd>While ncurses&#8217; repertoire of predefined capabilities is closest to Solaris, Solaris&#8217;s terminfo database has a few differences from the list published by X/Open Curses. For example, ncurses can be configured with tables which match the terminal databases for AIX, HP-UX or OSF/1, rather than the default Solaris-like configuration.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In SVr4 curses and ncurses, the terminal database is defined at compile-time using a text file which lists the different terminal capabilities.</p>
<dd>In principle, the text-file can be extended, but doing this requires recompiling and reinstalling the library. The text-file used in ncurses for terminal capabilities includes details for various systems past the documented X/Open Curses features. For example, ncurses supports these capabilities in each configuration:</p>
<dl>
<dd>
<dl>
<dt>memory_lock</p>
<dd>(meml) lock memory above cursor</p>
<dt>memory_unlock</p>
<dd>(memu) unlock memory</p>
<dt>box_chars_1</p>
<dd>(box1) box characters primary set</dl>
</dl>
<dd>The memory lock/unlock capabilities were included because they were used in the X11R6 terminal description for <code>xterm</code>. The <i>box1</i> capability is used in tic to help with terminal descriptions written for AIX.</dl>
<p> During the 1990s, some users were reluctant to use terminfo in spite of its performance advantages over termcap:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The fixed repertoire prevented users from adding features for unanticipated terminal improvements (or required them to reuse existing capabilities as a workaround).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The limitation to 16-bit signed integers was also mentioned. Because termcap stores everything as a string, it could represent larger numbers. Although termcap&#8217;s extensibility was rarely used (it was never the <i>speaker</i> who had actually used the feature), the criticism had a point. ncurses 5.0 provided a way to detect nonstandard capabilities, determine their type and optionally store and retrieve them in a way which did not interfere with other applications. These are referred to as <i>user-defined capabilities</i> because no modifications to the toolset&#8217;s predefined capability names are needed. The ncurses utilities <code>tic</code> and <code>infocmp</code> have a command-line option &#8220;-x&#8221; to control whether the nonstandard capabilities are stored or retrieved. A library function <code>use_extended_names</code> is provided for the same purpose. When compiling a terminal database, if &#8220;-x&#8221; is set, <code>tic</code> will store a user-defined capability if the capability name is not one of the predefined names. Because ncurses provides a termcap library interface, these user-defined capabilities may be visible to termcap applications:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The termcap interface (like all implementations of termcap) requires that the capability names are 2-characters.</p>
<dl>
<dd>When the capability is simple enough for use in a termcap application, it is provided as a 2-character name.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 There are other user-defined capabilities which refer to features not usable in termcap, e.g., parameterized strings that use more than two parameters or use more than the trivial expression support provided by termcap. For these, the terminfo database should have only capability names with 3 or more characters.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Some terminals can send distinct strings for special keys (cursor-, keypad- or function-keys) depending on modifier keys (shift, control, etc.). While terminfo and termcap have a set of 60 predefined function-key names, to which a series of keys can be assigned, that is insufficient for more than a dozen keys multiplied by more than a couple of modifier combinations. The ncurses database uses a convention based on <code>xterm</code> to provide extended special-key names.</p>
<dd>Fitting that into termcap&#8217;s limitation of 2-character names would be pointless. These extended keys are available only with terminfo.</dl>
<h3>Recognized capabilities</h3>
<p>The ncurses library uses the user-definable capabilities. While the terminfo database may have other extensions, ncurses makes explicit checks for these:</p>
<dl>
<dd>
<dl>
<dt>AX</p>
<dd><i>boolean</i>, asserts that the terminal interprets SGR 39 and SGR 49 by resetting the foreground and background color, respectively, to the default.</p>
<dd>This is a feature recognized by the <code>screen</code> program as well.</p>
<dt>E3</p>
<dd><i>string</i>, tells how to clear the terminal&#8217;s scrollback buffer. When present, the <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1) program sends this before clearing the terminal.</p>
<dd>The command &#8220;<code>tput clear</code>&#8221; does the same thing.</p>
<dt>RGB</p>
<dd><i>boolean</i>, <i>number</i> <code>or</code> <i>string</i>, to assert that the <code>set_a_foreground</code> and <code>set_a_background</code> capabilities correspond to <i>direct colors</i>, using an RGB (red/green/blue) convention. This capability allows the <code>color_content</code> function to return appropriate values without requiring the application to initialize colors using <code>init_color</code>.</p>
<dd>The capability type determines the values which ncurses sees:</p>
<dl>
<dd>
<dl>
<dt><i>boolean</i></p>
<dd>implies that the number of bits for red, green and blue are the same. Using the maximum number of colors, ncurses adds two, divides that sum by three, and assigns the result to red, green and blue in that order.</p>
<dd>If the number of bits needed for the number of colors is not a multiple of three, the blue (and green) components lose in comparison to red.</p>
<dt><i>number</i></p>
<dd>tells ncurses what result to add to red, green and blue. If ncurses runs out of bits, blue (and green) lose just as in the <i>boolean</i> case.</p>
<dt><i>string</i></p>
<dd>explicitly list the number of bits used for red, green and blue components as a slash-separated list of decimal integers.</dl>
</dl>
<dd>Because there are several RGB encodings in use, applications which make assumptions about the number of bits per color are unlikely to work reliably. As a trivial case, for example, one could define <code>RGB#1</code> to represent the standard eight ANSI colors, i.e., one bit per color.</p>
<dt>U8</p>
<dd><i>number</i>, asserts that ncurses must use Unicode values for line-drawing characters, and that it should ignore the alternate character set capabilities when the locale uses UTF-8 encoding. For more information, see the discussion of <code>NCURSES_NO_UTF8_ACS</code> in <code><a href="//www.systutorials.com/docs/linux/man/3X-ncurses/">ncurses</a></code>(3X).</p>
<dd>Set this capability to a nonzero value to enable it.</p>
<dt>XM</p>
<dd><i>string</i>, override ncurses&#8217;s built-in string which enables/disables <code>xterm</code> mouse mode.</p>
<dd>ncurses sends a character sequence to the terminal to initialize mouse mode, and when the user clicks the mouse buttons or (in certain modes) moves the mouse, handles the characters sent back by the terminal to tell it what was done with the mouse.</p>
<dd>The mouse protocol is enabled when the <i>mask</i> passed in the <code>mousemask</code> function is nonzero. By default, ncurses handles the responses for the X11 xterm mouse protocol. It also knows about the <i>SGR 1006</i> xterm mouse protocol, but must to be told to look for this specifically. It will not be able to guess which mode is used, because the responses are enough alike that only confusion would result.</p>
<dd>The <code>XM</code> capability has a single parameter. If nonzero, the mouse protocol should be enabled. If zero, the mouse protocol should be disabled. ncurses inspects this capability if it is present, to see whether the 1006 protocol is used. If so, it expects the responses to use the <i>SGR 1006</i> xterm mouse protocol.</p>
<dd>The xterm mouse protocol is used by other terminal emulators. The terminal database uses building-blocks for the various xterm mouse protocols which can be used in customized terminal descriptions.</p>
<dd>The terminal database building blocks for this mouse feature also have an experimental capability <i>xm</i>. The &#8220;xm&#8221; capability describes the mouse response. Currently there is no interpreter which would use this information to make the mouse support completely data-driven.</p>
<dd><i>xm</i> shows the format of the mouse responses. In this experimental capability, the parameters are</p>
<dl>
<dd>
<dl>
<dt><i>p1</i></p>
<dd>y-ordinate</p>
<dt><i>p2</i></p>
<dd>x-ordinate</p>
<dt><i>p3</i></p>
<dd>button</p>
<dt><i>p4</i></p>
<dd>state, e.g., pressed or released</p>
<dt><i>p5</i></p>
<dd>y-ordinate starting region</p>
<dt><i>p6</i></p>
<dd>x-ordinate starting region</p>
<dt><i>p7</i></p>
<dd>y-ordinate ending region</p>
<dt><i>p8</i></p>
<dd>x-ordinate ending region</dl>
</dl>
<dd>Here are examples from the terminal database for the most commonly used xterm mouse protocols:</p>
<dd>
<pre> xterm+x11mouse|X11 xterm mouse protocol,
 kmous=\E[M, XM=\E[?1000%?%p1%{1}%=%th%el%;,
 xm=\E[M
 %?%p4%t%p3%e%{3}%;%'&nbsp;'%+%c
 %p2%'!'%+%c
 %p1%'!'%+%c,
 xterm+sm+1006|xterm SGR-mouse,
 kmous=\E[&lt;, XM=\E[?1006;1000%?%p1%{1}%=%th%el%;,
 xm=\E[&lt;%i%p3%d;
 %p1%d;
 %p2%d;
 %?%p4%tM%em%;,</pre>
</dl>
</dl>
<h3>Extended key-definitions</h3>
<p>Several terminals provide the ability to send distinct strings for combinations of modified special keys. There is no standard for what those keys can send. Since 1999, <code>xterm</code> has supported <i>shift</i>, <i>control</i>, <i>alt</i>, and <i>meta</i> modifiers which produce distinct special-key strings. In a terminal description, ncurses has no special knowledge of the modifiers used. Applications can use the <i>naming convention</i> established for <code>xterm</code> to find these special keys in the terminal description. Starting with the curses convention that <i>key names</i> begin with &#8220;k&#8221; and that shifted special keys are an uppercase name, ncurses&#8217; terminal database defines these names to which a suffix is added:</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><i>Name</i></td>
<td><i>Description</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>kDC</td>
<td>special form of kdch1 (delete character)
</td>
</tr>
<tr VALIGN=top>
<td>kDN</td>
<td>special form of kcud1 (cursor down)
</td>
</tr>
<tr VALIGN=top>
<td>kEND</td>
<td>special form of kend (End)
</td>
</tr>
<tr VALIGN=top>
<td>kHOM</td>
<td>special form of khome (Home)
</td>
</tr>
<tr VALIGN=top>
<td>kLFT</td>
<td>special form of kcub1 (cursor-left or cursor-back)
</td>
</tr>
<tr VALIGN=top>
<td>kNXT</td>
<td>special form of knext (Next, or Page-Down)
</td>
</tr>
<tr VALIGN=top>
<td>kPRV</td>
<td>special form of kprev (Prev, or Page-Up)
</td>
</tr>
<tr VALIGN=top>
<td>kRIT</td>
<td>special form of kcuf1 (cursor-right, or cursor-forward)
</td>
</tr>
<tr VALIGN=top>
<td>kUP</td>
<td>special form of kcuu1 (cursor-up)
</td>
</tr>
</table>
</dl>
<p> These are the suffixes used to denote the modifiers:</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><i>Value</i></td>
<td><i>Description</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Shift
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>Alt
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>Shift + Alt
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>Control
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>Shift + Control
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>Alt + Control
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>Shift + Alt + Control
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>Meta
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>Meta + Shift
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>Meta + Alt
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td>Meta + Alt + Shift
</td>
</tr>
<tr VALIGN=top>
<td>13</td>
<td>Meta + Ctrl
</td>
</tr>
<tr VALIGN=top>
<td>14</td>
<td>Meta + Ctrl + Shift
</td>
</tr>
<tr VALIGN=top>
<td>15</td>
<td>Meta + Ctrl + Alt
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td>Meta + Ctrl + Alt + Shift
</td>
</tr>
</table>
</dl>
<p> None of these are predefined; terminal descriptions can refer to <i>names</i> which ncurses will allocate at runtime to <i>key-codes</i>. To use these keys in an ncurses program, an application could do this:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 using a list of extended key <i>names</i>, ask <code><a href="//www.systutorials.com/docs/linux/man/3X-tigetstr/">tigetstr</a></code>(3X) for their values, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 given the list of values, ask <code><a href="//www.systutorials.com/docs/linux/man/3X-key_defined/">key_defined</a></code>(3X) for the <i>key-code</i> which would be returned for those keys by <code><a href="//www.systutorials.com/docs/linux/man/3X-wgetch/">wgetch</a></code>(3X). </p>
<h2>Portability</h2>
<p>The &#8220;-x&#8221; extension feature of <code>tic</code> and <code>infocmp</code> has been adopted in NetBSD curses. That implementation stores user-defined capabilities, but makes no use of these capabilities itself.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1), <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1). </p>
<p> The terminal database section <i>NCURSES USER-DEFINABLE CAPABILITIES</i> summarizes commonly-used user-defined capabilities which are used in the terminal descriptions. Some of those features are mentioned in <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) or <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1). </p>
<p> <i>XTerm Control Sequences</i> provides further information on the <code>xterm</code> features which are used in these extended capabilities.</p>
<h2>Authors</h2>
<p>Thomas E. Dickey<br />
 beginning with ncurses 5.0 (1999)</p>
