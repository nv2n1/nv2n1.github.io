---
title: "mup(1)"
name: "mup"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mup/"
description: "mup – music publisher"
---

<h2>NAME</h2>
<p> mup &#8211; music publisher</p>
<h2>SYNOPSIS</h2>
<p> <code>mup</code> [<code>-c</code><i>N</i>] [-C] [<code>-d</code><i>N</i>] [<code>-D</code> <i>MACRO[=macro_def</i>]] [<code>-e</code> <i>errfile</i>] [-E] [<code>-f</code> <i>outfile</i>] [<code>-F</code>] [<code>-l</code>] [<code>-m</code> <i>midifile</i>] [<code>-M</code>] [<code>-o</code> <i>pagelist</i>] [<code>-p</code><i>N</i>] [<code>-v</code>] [<code>-x</code> <i>N</i>[,<i>M</i>] [<i>file&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Mup is a program for producing printed music. There is an optional companion program called Mupmate that provides a more graphical user interface on top of Mup, but this manual page describes the command line interface. The Mup User&#8217;s Guide should be consulted for details of the format of the input file. Options include:</p>
<dl>
<dt><code>-c</code> <i>N</i></p>
<dd> Combine consecutive measures of all rests or spaces into multirests (multiple measures of rest printed as a single measure, with the number of measures of rest printed above the staff). Any time there are <i>N</i> or more measures in a row that consist entirely of rests or spaces, they will be replaced by a multirest. The combining of measures stops when there is a visible staff that contains notes, lyrics, or other musical symbols, when there are parameter changes on a visible staff or in score context, or when there is a bar line other than an ordinary or invisible bar. This option is most likely to be useful when printing a subset of staffs, where the particular staff(s) you are printing have long periods of rests. (See the -s option.)</p>
<dt><code>-C</code></p>
<dd> This option is only used in connection with the -E option. It specifies that comments are to be passed through rather than deleted.</p>
<dt><code>-d</code> <i>N</i></p>
<dd> Print debugging information. <i>N</i> is a bitmap.</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> parse phase information</p>
<dt>2</p>
<dd> high level parse phase tracing</p>
<dt>4</p>
<dd> low level parse phase tracing</p>
<dt>8</p>
<dd> reserved</p>
<dt>16</p>
<dd> high level placement phase tracing</p>
<dt>32</p>
<dd> low level placement phase tracing</p>
<dt>64</p>
<dd> reserved</p>
<dt>128</p>
<dd> contents of the main internal list</p>
<dt>256</p>
<dd> high level print phase tracing</p>
<dt>512</p>
<dd> low level print phase tracing</dl>
</dl>
<dt>
<dd> <i>N</i> can be specified in decimal, octal (by using a leading zero), or hex (by using a leading 0x). This information is intended for debugging of <code>Mup</code> itself and thus is not likely to be of use to the average user.</p>
<dt><code>-D</code> <i>MACRO[=macro_def]</i></p>
<dd> Define the macro <i>MACRO</i>. The macro name must consist of upper case letters, digits, and underscores, beginning with an upper case letter. The <i>macro_def</i> is optional, and gives the text of the macro. If it contains any white space or other special characters, it must be quoted (if quoting is supported by your operating system or shell).</p>
<dt><code>-e</code> <i>errfile</i></p>
<dd> Place error messages into <i>errfile</i> instead of writing them to the standard error output stream.</p>
<dt><code>-E</code></p>
<dd> Rather than produce PostScript or MIDI output, just expand macros and includes, and write the result to the standard output stream. Comments in the input are deleted, unless the -C option is also specified.</p>
<dt><code>-f</code> <i>outfile</i></p>
<dd> Place the output into <i>outfile</i> instead of writing it to the standard output.</p>
<dt><code>-F</code></p>
<dd> This is like the <code>-f</code> option, except the name of the output file is derived from the name of the Mup input file. If the name of the Mup input file ends with a &quot;.mup&quot; suffix, the generated PostScript output file will end with a &quot;.ps&quot; suffix instead. If the name of the Mup input file ends with a &quot;.MUP&quot; suffix, the PostScript file will end with a &quot;.PS&quot; suffix. Otherwise, a &quot;.ps&quot; suffix will be appended to the end of the Mup input file name. If multiple input files are listed, the last is used. If none are specified (input is read from standard input), the name &quot;stdin.ps&quot; will be used for the output file.</p>
<dt><code>-l</code></p>
<dd> Print the Mup license and exit.</p>
<dt><code>-m</code> <i>midifile</i></p>
<dd> Instead of generating PostScript output, generate standard MIDI (Musical Instrument Digital Interface) output, and put it in <i>midifile</i>. This option also causes the macro &quot;MIDI&quot; to become defined.</p>
<dt><code>-M</code></p>
<dd> This is like the <code>-m</code> option, except the name of the MIDI file is derived from the name of the Mup input file. If the name of the Mup input file ends with a &quot;.mup&quot; suffix, the generated MIDI file will end with a &quot;.mid&quot; suffix instead. If the name of the Mup input file ends with a &quot;.MUP&quot; suffix, the MIDI file will end with a &quot;.MID&quot; suffix. Otherwise, a &quot;.mid&quot; suffix will be appended to the end of the Mup input file name. If multiple input files are listed, the last is used. If none are specified (input is read from standard input), the name &quot;stdin.mid&quot; will be used for the MIDI file.</p>
<dt><code>-o</code> <i>pagelist</i></p>
<dd> Print only the pages given in <i>pagelist</i>. The <i>pagelist</i> can be a comma-separated list of numbers or ranges, where a range is two numbers separated by a dash. For example, -o1,7-9,12-14 would print pages 1, 7, 8, 9, 12, 13, and 14. Pages will be printed in the order given. They need not be in order, and a page number may be included more than once. Alternately, the <i>pagelist</i> can be the special keyword &quot;odd&quot; or &quot;even&quot; which will cause all odd or even numbered pages to be printed. This may be useful if you have a printer that only makes single-sided copies, but you wish to print Mup output double-sided. You could print odd-numbered pages, then turn the paper over and feed the pages through again for the even-numbered pages.</p>
<dt><code>-p</code><i>N</i></p>
<dd> Start numbering pages at <i>N</i> instead of at 1. If <code>-o</code> and <code>-p</code> are used together, the page numbers given in the <code>-o</code><i>pagelist</i> must be the printed page numbers. For example, if you use -p10 and want to print just the second page, you would need to specify -o11.</p>
<dt><code>-s</code><i>stafflist</i></p>
<dd> Only print the staffs that are included in <i>stafflist</i>. This can be a comma-separated list of staff numbers or ranges, such as &quot;1,5&quot; or &quot;1-3,7-8&quot; To further restrict to a single voice on a staff, add <code>v</code><i>N</i> where <i>N</i> is the voice number (1, 2, or 3), after the staff, as in &quot;2v1,5v2&quot; You can&#8217;t specify a list or range for voices; if you only want to make two out of three voices visible, you have to specify them separately, like &quot;1v2,1v3&quot;. No spaces are allowed in the list.</p>
<dt><code>-v</code></p>
<dd> Print the Mup version number and exit. This manual page is for version 6.5.</p>
<dt><code>-x</code><i>M,N</i></p>
<dd> Extract measures <i>M</i> through <i>N</i> of the song. This allows you to print or play a part of a song. The comma and second value are optional; if not specified, the default is to go to the end of the piece. Positive values specify the number of measures from the beginning of the piece, while negative values are relative to the end, with -1 referring to the last measure of the song. So -x1,-1 means the entire song, if the song doesn&#8217;t have a pickup measure. If the song has a pickup measure, that is specified by 0. So for a song with a pickup, -x0,-1 would mean the entire song, and -x0,0 would mean just the pickup measure. As other examples, -x-1,-1 means just the final measure of the song, -x2 means starting after the first full measure, -x3,4 means only measures 3 and 4, and -x6,6 means just measure 6. The starting measure is not allowed to be inside an ending. A common use for this option might be to generate a MIDI file for just a few measures. For example, if you were trying to tweak tempo values for a ritard in the last 2 measures of a song, you could use -x-2 to listen to just those measures.</dl>
<p> The options, if any, can be followed by one or more <i>files</i> in Mup format. If no <i>files</i> are specified, standard input is read. If several <i>files</i> are listed, they are effectively concatenated together and treated as one big file. Since there are some things (such as header and footer) that are only allowed to occur once, if you have several independent pieces, mup should be called on each individually rather than trying to print them all with one command. If a specified file does not exist, and its name does not already end with .mup or .MUP, then Mup will append .mup to the specified name and attempt to open that. </p>
<p> On most systems, the environment variable MUPPATH can be set to a list of paths in which to look for &#8216;include&#8217; files. The components are separated by a colon on Unix or Linux systems, and by a semicolon on systems with DOS-like file naming conventions. </p>
<p> For more debugging, in addition to the -d option, if the environment variable MUP_BB is set to &quot;bcfghnsu&quot; or any subset of those letters, the generated output will include &quot;bounding boxes&quot; for the things Mup internally calls bars (b), chords (c), feeds (f), grpsyls (g), header/footer and top/bottom (h), notes (n), staffs (s), and stuff (u). While this is intended for use in debugging Mup itself, it may also help you understand why Mup places things the way it does, since in general, Mup only allows bounding boxes to overlap according to specific rules. If viewed with a color PostScript viewer (not mupdisp), these boxes will be in color.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-mkmupfnt/">mkmupfnt</a>(1), <a href="/docs/linux/man/1-mupdisp/">mupdisp</a>(1), <a href="/docs/linux/man/1-mupmate/">mupmate</a>(1), <a href="/docs/linux/man/1-mupprnt/">mupprnt</a>(1).<br />
 Mup &#8212; Music Publisher User&#8217;s Guide </p>
<h2>Index</h2>
