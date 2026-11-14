---
title: "prg2lout(1)"
name: "prg2lout"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prg2lout/"
description: "prg2lout – convert computer program text into Lout"
---

<h2>NAME</h2>
<p> prg2lout &#8211; convert computer program text into Lout</p>
<h2>SYNOPSIS</h2>
<p> <code>prg2lout</code> -l <i>language</i> [ <i>options</i> ] <i>files</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Reformat computer program text for input to the Lout document formatting system, taking care of comments, character strings, tab characters, etc. </p>
<p> <code>prg2lout</code> reads the named program source files and produces output suitable for input to <code>lout -s</code>. Thus, </p>
<dl>
<dt>
<dd> <code>prg2lout -l C foo.c | lout -s | lpr</code></dl>
<p> will print the C program <code>foo.c</code> on a PostScript printer. Each file will start on a new page, preceded by its name in bold.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-llanguage</code></p>
<dd> (Compulsory.) Files are written in this programmming language. Run <i>prg2lout -u</i> to see the list of languages available.</p>
<dt><code>-pfixed</code></p>
<dd> Use a fixed width font (the default for C).</p>
<dt><code>-pvarying</code></p>
<dd> Use a varying-width italic font with non-italic bold keywords (the default for Eiffel).</p>
<dt><code>-psymbol</code></p>
<dd> Use a varying-width italic font with mathematical symbols and non-italic bold keywords.</p>
<dt><code>-n</code></p>
<dd> Do not print the file name before each source file.</p>
<dt><code>-f</code><i> font</i></p>
<dd> Select a font family. The default is <code>-fCourier</code> for <code>-pfixed</code>, and <code>-fTimes</code> for <code>-pvarying</code> and <code>-psymbol</code>.</p>
<dt><code>-s</code><i> size</i></p>
<dd> Select a Lout font size. The default is <code>-s9p</code> (meaning 9 points) for <code>-pfixed</code>, and <code>-s10p</code> for <code>-pvarying</code> and <code>-psymbol</code>. These work well with 80-character-wide programs.</p>
<dt><code>-v</code><i> vsize</i></p>
<dd> Select a Lout vertical inter-line gap. The default is <code>-v1.1fx</code> meaning 1.1 times the font size measured from baseline to baseline.</p>
<dt><code>-b</code><i> num</i></p>
<dd> Select a blank line scale factor. The default is <code>-b1.0</code> meaning no scaling. A good alternative is 0.6.</p>
<dt><code>-t</code><i> num</i></p>
<dd> Set the tab interval to <i>num</i> characters (default is <code>-t8</code>).</p>
<dt><code>-T</code><i> width</i></p>
<dd> Without this option, <code>prg2lout</code> simulates tabs with spaces. With this option, <code>prg2lout</code> simulates tabs with Lout tabulation operators; <i>width</i> is the width of one tab interval in the final print, measured in Lout units. This guarantees alignment of characters following tabs even with varying-width fonts, provided <i>width</i> is sufficiently large. For example, <code>-T0.5i</code> produces half-inch tab intervals.</p>
<dt><code>-L</code><i> number</i></p>
<dd> Attach line numbers to the program text, beginning with <i>number</i> or 1 if number is not given. You may need to give the 1 anyway to prevent .I prg2lout from taking a following file name as a number.</p>
<dt><code>-N</code></p>
<dd> Do not print line numbers on blank lines.</p>
<dt><code>-M</code></p>
<dd> Like -N but do not assign line numbers to blank lines.</p>
<dt><code>-S</code><i> filename</i></p>
<dd> Use <i>filename</i> as the setup file instead of the system default setup file. The setup file determines the value of all formatting options not given to <i>prg2lout</i> as command line arguments.</p>
<dt><code>-u</code></p>
<dd> Print usage information on stderr, including available languages, and exit.</p>
<dt><code>-V</code></p>
<dd> Print version information on stderr and exit.</dl>
<h3>Raw Mode</h3>
<p> There is a &#8220;raw mode&#8221; usage of <code>prg2lout</code> invoked by a <code>-r</code> flag (must be the first argument). This converts one program file into Lout-readable source without any heading or trailing information. Synopsis: </p>
<dl>
<dt>
<dd> <code>prg2lout</code> <code>-r</code> <code>-i</code><i>&nbsp;<wbr>infile</i> <code>-o</code><i>&nbsp;<wbr>out</i> <code>-e</code><i>&nbsp;<wbr>err</i> <code>-t</code><i>&nbsp;<wbr>num</i> <code>-T</code><i>&nbsp;<wbr>width</i></dl>
<p> Users should never need this mode; it is invoked automatically from within Lout by symbols supplied with the standard configuration (see reference).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lout/">lout</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-ghostview/">ghostview</a></code>(1).</p>
<h2>REFERENCES</h2>
<p> Jeffrey H. Kingston, <i>&#8220;A User&#8217;s Guide to the Lout Document Formatting System&#8221;</i>, Chapter 11.</p>
<h2>AUTHOR</h2>
<p> Jeffrey H. Kingston </p>
<h2>Index</h2>
