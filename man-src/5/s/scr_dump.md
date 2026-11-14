---
title: "scr_dump(5)"
name: "scr_dump"
section: "5"
letter: "s"
url: "/docs/linux/man/5-scr_dump/"
description: "scr_dump – format of curses screen-dumps."
---

<p>scr_dump &#8211; format of curses screen-dumps.</p>
<h2>Synopsis</h2>
<p><code>scr_dump</code></p>
<h2>Description</h2>
<p>The curses library provides applications with the ability to write the contents of a window to an external file using <code>scr_dump</code> or <code>putwin</code>, and read it back using <code>scr_restore</code> or <code>getwin</code>. </p>
<p> The <code>putwin</code> and <code>getwin</code> functions do the work; while <code>scr_dump</code> and <code>scr_restore</code> conveniently save and restore the whole screen, i.e., <code>stdscr</code>.</p>
<h3>ncurses6</h3>
<p>A longstanding implementation of screen-dump was revised with ncurses6 to remedy problems with the earlier approach:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 A &#8220;magic number&#8221; is written to the beginning of the dump file, allowing applications (such as <code><a href="/docs/linux/man/1-file/">file</a></code>(1)) to recognize curses dump files.</p>
<dl>
<dd>Because ncurses6 uses a new format, that requires a new magic number was unused by other applications. This 16-bit number was unused:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>0x8888 (octal ``\210\210'')</pre>
<p>&nbsp;.in -4</p>
<dd>but to be more certain, this 32-bit number was chosen:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>0x88888888 (octal ``\210\210\210\210'')</pre>
<p>&nbsp;.in -4</p>
<dd>This is the pattern submitted to the maintainers of the <code>file</code> program:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>#
# ncurses5 (and before) did not use a magic number,
# making screen dumps &quot;data&quot;.
#
# ncurses6 (2015) uses this format, ignoring byte-order
0 string \210\210\210\210ncurses ncurses6 screen image
#</pre>
<p>&nbsp;.in -4<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The screen dumps are written in textual form, so that internal data sizes are not directly related to the dump-format, and enabling the library to read dumps from either narrow- or wide-character- configurations.</p>
<dd>The <i>narrow</i> library configuration holds characters and video attributes in a 32-bit <code>chtype</code>, while the <i>wide-character</i> library stores this information in the <code>cchar_t</code> structure, which is much larger than 32-bits.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 It is possible to read a screen dump into a terminal with a different screen-size, because the library truncates or fills the screen as necessary.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The ncurses6 <code>getwin</code> reads the legacy screen dumps from ncurses5.</dl>
<h3>ncurses5 (legacy)</h3>
<p>The screen-dump feature was added to ncurses in June 1995. While there were fixes and improvements in succeeding years, the basic scheme was unchanged:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>WINDOW</code> structure was written in binary form.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>WINDOW</code> structure refers to lines of data, which were written as an array of binary data following the <code>WINDOW</code>.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 When <code>getwin</code> restored the window, it would keep track of offsets into the array of line-data and adjust the <code>WINDOW</code> structure which was read back into memory. </p>
<p> This is similar to Unix SystemV, but does not write a &#8220;magic number&#8221; to identify the file format.</p>
<h2>Portability</h2>
<p>There is no standard format for <code>putwin</code>. This section gives a brief description of the existing formats.</p>
<h3>X/Open Curses</h3>
<p>Refer to <i>X/Open Curses, Issue 7</i> (2009). </p>
<p> X/Open&#8217;s documentation for <i>enhanced curses</i> says only:</p>
<dl>
<dd>The <i>getwin(&nbsp;) </i>function reads window-related data stored in the file by <i>putwin(&nbsp;)</i>. The function then creates and initializes a new window using that data. </p>
<p> The <i>putwin(&nbsp;)</i> function writes all data associated with <i>win</i> into the <i>stdio</i> stream to which <i>filep</i> points, using an <code>unspecified format</code>. This information can be retrieved later using <i>getwin(&nbsp;)</i>.</dl>
<p> In the mid-1990s when the X/Open Curses document was written, there were still systems using older, less capable curses libraries (aside from the BSD curses library which was not relevant to X/Open because it did not meet the criteria for <i>base curses</i>). The document explained the term &#8220;enhanced&#8221; as follows:</p>
<dl>
<dd>&nbsp;.IP&nbsp;&bull;&nbsp;4 Shading is used to identify <i>X/Open Enhanced Curses</i> material, relating to interfaces included to provide enhanced capabilities for applications originally written to be compiled on systems based on the UNIX operating system. Therefore, the features described may not be present on systems that conform to <code>XPG4 or to earlier XPG releases</code>. The relevant reference pages may provide additional or more specific portability warnings about use of the material.</dl>
<p> In the foregoing, emphasis was added to <code>unspecified format</code> and to <code>XPG4 or to earlier XPG releases</code>, for clarity.</p>
<h3>Unix SystemV</h3>
<p>Unix SystemV curses identified the file format by writing a &#8220;magic number&#8221; at the beginning of the dump. The <code>WINDOW</code> data and the lines of text follow, all in binary form. </p>
<p> The Solaris curses source has these definitions:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>/* terminfo magic number */
#define MAGNUM 0432
/* curses screen dump magic number */
#define SVR2_DUMP_MAGIC_NUMBER 0433
#define SVR3_DUMP_MAGIC_NUMBER 0434</pre>
<p>&nbsp;.in -4 </p>
<p> That is, the feature was likely introduced in SVr2 (1984), and improved in SVr3 (1987). The Solaris curses source has no magic number for SVr4 (1989). Other operating systems (AIX and HPUX) use a magic number which would correspond to this definition:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>/* curses screen dump magic number */
#define SVR4_DUMP_MAGIC_NUMBER 0435</pre>
<p>&nbsp;.in -4 </p>
<p> That octal number in bytes is 001, 035. Because most Unix vendors use big-endian hardware, the magic number is written with the high-order byte first, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>&nbsp;01 35</pre>
<p>&nbsp;.in -4 </p>
<p> After the magic number, the <code>WINDOW</code> structure and line-data are written in binary format. While the magic number used by the Unix systems can be seen using <code><a href="/docs/linux/man/1-od/">od</a></code>(1), none of the Unix systems documents the format used for screen-dumps. </p>
<p> The Unix systems do not use identical formats. While collecting information for for this manual page, the <i>savescreen</i> test-program produced dumps of different size (all on 64-bit hardware, on 40&#215;80 screens):<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 AIX (51817 bytes)<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 HPUX (90093 bytes)<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Solaris 10 (13273 bytes)<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 ncurses5 (12888 bytes)</p>
<h3>Solaris</h3>
<p>As noted above, Solaris curses has no magic number corresponding to SVr4 curses. This is odd since Solaris was the first operating system to pass the SVr4 guidelines. Solaris has two versions of curses:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The default curses library uses the SVr3 magic number.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 There is an alternate curses library in <code>/usr/xpg4</code>. This uses a textual format with no magic number.</p>
<dl>
<dd>According to the copyright notice, the <i>xpg4</i> Solaris curses library was developed by MKS (Mortice Kern Systems) from 1990 to 1995.</p>
<dd>Like ncurses6, there is a file-header with parameters. Unlike ncurses6, the contents of the window are written piecemeal, with coordinates and attributes for each chunk of text rather than writing the whole window from top to bottom.</dl>
<h3>PDCurses</h3>
<p>PDCurses added support for screen dumps in version 2.7 (2005). Like Unix SystemV and ncurses5, it writes the <code>WINDOW</code> structure in binary, but begins the file with its three-byte identifier &#8220;PDC&#8221;, followed by a one-byte version, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre> ``PDC''</pre>
<p>&nbsp;.in -4</p>
<h3>NetBSD</h3>
<p>As of April 2017, NetBSD curses does not support <code>scr_dump</code> and <code>scr_restore</code> (or <code>scr_init</code>, <code>scr_set</code>), although it has <code>putwin</code> and <code>getwin</code>. </p>
<p> Like ncurses5, NetBSD <code>putwin</code> does not identify its dumps with a useful magic number. It writes<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the curses shared library major and minor versions as the first two bytes (e.g., 7 and 1),<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 followed by a binary dump of the <code>WINDOW</code>,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 some data for wide-characters referenced by the <code>WINDOW</code> structure, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 finally, lines as done by other implementations.</p>
<h2>Example</h2>
<pre><code>Given a simple program which writes text to the screen
(and for the sake of example, limiting the screen-size to 10x20):


 .sp


 .in +4

#include &lt;curses.h&gt;

int
main(void)
{
    putenv(&quot;LINES=10&quot;);
    putenv(&quot;COLUMNS=20&quot;);
    initscr();
    start_color();
    init_pair(1, COLOR_WHITE, COLOR_BLUE);
    init_pair(2, COLOR_RED, COLOR_BLACK);
    bkgd(COLOR_PAIR(1));
    move(4, 5);
    attron(A_BOLD);
    addstr(&quot;Hello&quot;);
    move(5, 5);
    attroff(A_BOLD);
    attrset(A_REVERSE | COLOR_PAIR(2));
    addstr(&quot;World!&quot;);
    refresh();
    scr_dump(&quot;foo.out&quot;);
    endwin();
    return 0;
}

.in - 4</code></pre>
<p> When run using ncurses6, the output looks like this:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>\210\210\210\210ncurses 6.0.20170415
_cury=5
_curx=11
_maxy=9
_maxx=19
_flags=14
_attrs=\{REVERSE|C2}
flag=_idcok
_delay=-1
_regbottom=9
_bkgrnd=\{NORMAL|C1}\s
rows:
1:\{NORMAL|C1}\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
2:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
3:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
4:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
5:\s\s\s\s\s\{BOLD}Hello\{NORMAL}\s\s\s\s\s\s\s\s\s\s
6:\s\s\s\s\s\{REVERSE|C2}World!\{NORMAL|C1}\s\s\s\s\s\s\s\s\s
7:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
8:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
9:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
10:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s</pre>
<p>&nbsp;.in -4 The first four octal escapes are actually nonprinting characters, while the remainder of the file is printable text. You may notice:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The actual color pair values are not written to the file.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 All characters are shown in printable form; spaces are &#8220;\s&#8221; to ensure they are not overlooked.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Attributes are written in escaped curly braces, e.g., &#8220;\{BOLD}&#8221;, and may include a color-pair (C1 or C2 in this example).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The parameters in the header are written out only if they are nonzero. When reading back, order does not matter. Running the same program with Solaris <i>xpg4</i> curses gives this dump:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>MAX=10,20
BEG=0,0
SCROLL=0,10
VMIN=1
VTIME=0
FLAGS=0x1000
FG=0,0
BG=0,0,
0,0,0,1,
0,19,0,0,
1,0,0,1,
1,19,0,0,
2,0,0,1,
2,19,0,0,
3,0,0,1,
3,19,0,0,
4,0,0,1,
4,5,0x20,0,Hello
4,10,0,1,
4,19,0,0,
5,0,0,1,
5,5,0x4,2,World!
5,11,0,1,
5,19,0,0,
6,0,0,1,
6,19,0,0,
7,0,0,1,
7,19,0,0,
8,0,0,1,
8,19,0,0,
9,0,0,1,
9,19,0,0,
CUR=11,5</pre>
<p>&nbsp;.in -4 Solaris <code>getwin</code> requires that all parameters are present, and in the same order. The <i>xpg4</i> curses library does not know about the <code>bce</code> (back color erase) capability, and does not color the window background. On the other hand, the SVr4 curses library does know about the background color. However, its screen dumps are in binary. Here is the corresponding dump (using &#8220;od -t x1&#8221;):<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>0000000 1c 01 c3 d6 f3 58 05 00 0b 00 0a 00 14 00 00 00
0000020 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00
0000040 00 00 b8 1a 06 08 cc 1a 06 08 00 00 09 00 10 00
0000060 00 00 00 80 00 00 20 00 00 00 ff ff ff ff 00 00
0000100 ff ff ff ff 00 00 00 00 20 80 00 00 20 80 00 00
0000120 20 80 00 00 20 80 00 00 20 80 00 00 20 80 00 00
*
0000620 20 80 00 00 20 80 00 00 20 80 00 00 48 80 00 04
0000640 65 80 00 04 6c 80 00 04 6c 80 00 04 6f 80 00 04
0000660 20 80 00 00 20 80 00 00 20 80 00 00 20 80 00 00
*
0000740 20 80 00 00 20 80 00 00 20 80 00 00 57 00 81 00
0000760 6f 00 81 00 72 00 81 00 6c 00 81 00 64 00 81 00
0001000 21 00 81 00 20 80 00 00 20 80 00 00 20 80 00 00
0001020 20 80 00 00 20 80 00 00 20 80 00 00 20 80 00 00
*
0001540 20 80 00 00 20 80 00 00 00 00 f6 d1 01 00 f6 d1
0001560 08 00 00 00 40 00 00 00 00 00 00 00 00 00 00 07
0001600 00 04 00 01 00 01 00 00 00 01 00 00 00 00 00 00
0001620 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
*
0002371</pre>
<p>&nbsp;.in -4</p>
<h2>See Also</h2>
<p><code>scr_dump</code>(3NCURSES), <code>util</code>(3NCURSES).</p>
<h2>Authors</h2>
<p>Thomas E. Dickey<br />
 extended screen-dump format for ncurses 6.0 (2015) </p>
<p> Eric S. Raymond<br />
 screen dump feature in ncurses 1.9.2d (1995)</p>
