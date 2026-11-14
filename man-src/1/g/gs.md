---
title: "gs(1)"
name: "gs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gs/"
description: "gs – Ghostscript (PostScript and PDF language interpreter and previewer)"
---

<h2 class="name">NAME</h2>
<p> gs &#8211; Ghostscript (PostScript and PDF language interpreter and previewer) </p>
<h2>SYNOPSIS</h2>
<p> <code>gs</code> [ <i>options</i> ] [ <i>files</i> ] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>gs</code> command invokes <code>Ghostscript</code>, an interpreter of Adobe Systems&#8217; <code>PostScript</code>(tm) and <code>Portable Document Format</code> (PDF) languages. <code>gs</code> reads &quot;files&quot; in sequence and executes them as Ghostscript programs. After doing this, it reads further input from the standard input stream (normally the keyboard), interpreting each line separately and output to an output device (may be a file or an X11 window preview, see below). The interpreter exits gracefully when it encounters the &quot;quit&quot; command (either in a file or from the keyboard), at end-of-file, or at an interrupt signal (such as Control-C at the keyboard). </p>
<p> The interpreter recognizes many option switches, some of which are described below. Please see the usage documentation for complete information. Switches may appear anywhere in the command line and apply to all files thereafter. Invoking Ghostscript with the <code>-h</code> or <code>-?</code> switch produces a message which shows several useful switches, all the devices known to that executable, and the search path for fonts; on Unix it also shows the location of detailed documentation. </p>
<p> Ghostscript may be built to use many different output devices. To see which devices your executable includes, run &quot;<code>gs -h</code>&quot;. </p>
<p> Unless you specify a particular device, Ghostscript normally opens the first one of those and directs output to it. </p>
<p> If you have installed the ghostscript-x Debian package and are under X, the default device is an X11 window (previewer), else ghostscript will use the bbox device and print on stdout the dimension of the postscript file. </p>
<p> So if the first one in the list is the one you want to use, just issue the command </p>
<pre>
        gs myfile.ps
</pre>
<p> You can also check the set of available devices from within Ghostscript: invoke Ghostscript and type </p>
<pre>
        devicenames ==
</pre>
<p> but the first device on the resulting list may not be the default device you determine with &quot;<code>gs -h</code>&quot;. To specify &quot;AbcXyz&quot; as the initial output device, include the switch </p>
<pre>
        -sDEVICE=AbcXyz
</pre>
<p> For example, for output to an Epson printer you might use the command </p>
<pre>
        gs -sDEVICE=epson myfile.ps
</pre>
<p> The &quot;-sDEVICE=&quot; switch must precede the first mention of a file to print, and only the switch&#8217;s first use has any effect. </p>
<p> Finally, you can specify a default device in the environment variable <code>GS_DEVICE</code>. The order of precedence for these alternatives from highest to lowest (Ghostscript uses the device defined highest in the list) is: </p>
<p> Some devices can support different resolutions (densities). To specify the resolution on such a printer, use the &quot;-r&quot; switch: </p>
<pre>
        gs -sDEVICE=&lt;device&gt; -r&lt;xres&gt;x&lt;yres&gt;
</pre>
<p> For example, on a 9-pin Epson-compatible printer, you get the lowest-density (fastest) mode with </p>
<pre>
        gs -sDEVICE=epson -r60x72
</pre>
<p> and the highest-density (best output quality) mode with </p>
<pre>
        gs -sDEVICE=epson -r240x72.
</pre>
<p> If you select a printer as the output device, Ghostscript also allows you to choose where Ghostscript sends the output &#8212; on Unix systems, usually to a temporary file. To send the output to a file &quot;foo.xyz&quot;, use the switch </p>
<pre>
        -sOutputFile=foo.xyz
</pre>
<p> You might want to print each page separately. To do this, send the output to a series of files &quot;foo1.xyz, foo2.xyz, &#8230;&quot; using the &quot;-sOutputFile=&quot; switch with &quot;%d&quot; in a filename template: </p>
<pre>
        -sOutputFile=foo%d.xyz
</pre>
<p> Each resulting file receives one page of output, and the files are numbered in sequence. &quot;%d&quot; is a printf format specification; you can also use a variant like &quot;%02d&quot;. </p>
<p> You can also send output to a pipe. For example, to pipe output to the &quot;<code>lpr</code>&quot; command (which, on many Unix systems, directs it to a printer), use the option </p>
<pre>
        -sOutputFile=%pipe%lpr
</pre>
<p> You can also send output to standard output: </p>
<pre>
        -sOutputFile=-
</pre>
<p> or </p>
<pre>
        -sOutputFile=%stdout%
</pre>
<p> In this case you must also use the <code>-q</code> switch, to prevent Ghostscript from writing messages to standard output. </p>
<p> To select a specific paper size, use the command line switch </p>
<pre>
        -sPAPERSIZE=&lt;paper_size&gt;
</pre>
<p> for instance </p>
<pre>
        -sPAPERSIZE=a4
</pre>
<p> or </p>
<pre>
        -sPAPERSIZE=legal
</pre>
<p> Most ISO and US paper sizes are recognized. See the usage documentation for a full list, or the definitions in the initialization file &quot;gs_statd.ps&quot;. </p>
<p> Ghostscript can do many things other than print or view PostScript and PDF files. For example, if you want to know the bounding box of a PostScript (or EPS) file, Ghostscript provides a special &quot;device&quot; that just prints out this information. </p>
<p> For example, using one of the example files distributed with Ghostscript, </p>
<pre>
        gs -sDEVICE=bbox golfer.ps
</pre>
<p> prints out </p>
<pre>
        %%BoundingBox: 0 25 583 732
        %%HiResBoundingBox: 0.808497 25.009496 582.994503 731.809445
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8212;</code><i> filename arg1 &#8230;</i></p>
<dd> Takes the next argument as a file name as usual, but takes all remaining arguments (even if they have the syntactic form of switches) and defines the name &quot;ARGUMENTS&quot; in &quot;userdict&quot; (not &quot;systemdict&quot;) as an array of those strings, <code>before</code> running the file. When Ghostscript finishes executing the file, it exits back to the shell.</p>
<dt><code>-D</code><i>name</i><code>=</code><i>token</i></p>
<dd>
<dt> <code>-d</code><i>name</i><code>=</code><i>token</i></p>
<dd>Define a name in &quot;systemdict&quot; with the given definition. The token must be exactly one token (as defined by the &quot;token&quot; operator) and may contain no whitespace.</p>
<dt><code>-D</code><i>name</i></p>
<dd>
<dt> <code>-d</code><i>name</i></p>
<dd>Define a name in &quot;systemdict&quot; with value=null.</p>
<dt><code>-S</code><i>name</i><code>=</code><i>string</i></p>
<dd>
<dt> <code>-s</code><i>name</i><code>=</code><i>string</i></p>
<dd>Define a name in &quot;systemdict&quot; with a given string as value. This is different from <code>-d</code>. For example, <code>-dname=35</code> is equivalent to the program fragment<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/name 35 def</p>
<p> whereas <code>-sname=35</code> is equivalent to<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/name (35) def</p>
<dt><code>-P</code></p>
<dd> Makes Ghostscript to look first in the current directory for library files. By default, Ghostscript no longer looks in the current directory, unless, of course, the first explicitly supplied directory is &quot;.&quot; in <code>-I</code>. See also the <code>INITIALIZATION FILES</code> section below, and bundled <code>Use.htm</code> for detailed discussion on search paths and how Ghostcript finds files.</p>
<dt><code>-q</code></p>
<dd> Quiet startup: suppress normal startup messages, and also do the equivalent of <code>-dQUIET</code>.</p>
<dt><code>-g</code><i>number1</i><code>x</code><i>number2</i></p>
<dd> Equivalent to <code>-dDEVICEWIDTH=</code><i>number1</i> and <code>-dDEVICEHEIGHT=</code><i>number2</i>. This is for the benefit of devices (such as X11 windows) that require (or allow) width and height to be specified.</p>
<dt><code>-r</code><i>number</i></p>
<dd>
<dt> <code>-r</code><i>number1</i><code>x</code><i>number2</i></p>
<dd>Equivalent to <code>-dDEVICEXRESOLUTION=</code><i>number1</i> and <code>-dDEVICEYRESOLUTION=</code><i>number2</i>. This is for the benefit of devices such as printers that support multiple X and Y resolutions. If only one number is given, it is used for both X and Y resolutions.</p>
<dt><code>-I</code><i>directories</i></p>
<dd> Adds the designated list of directories at the head of the search path for library files.</p>
<dt><code>&#8211;</code></p>
<dd> This is not really a switch, but indicates to Ghostscript that standard input is coming from a file or a pipe and not interactively from the command line. Ghostscript reads from standard input until it reaches end-of-file, executing it like any other file, and then continues with processing the command line. When the command line has been entirely processed, Ghostscript exits rather than going into its interactive mode.</dl>
<p> Note that the normal initialization file &quot;gs_init.ps&quot; makes &quot;systemdict&quot; read-only, so the values of names defined with <code>-D</code>, <code>-d</code>, <code>-S</code>, or <code>-s</code> cannot be changed (although, of course, they can be superseded by definitions in &quot;userdict&quot; or other dictionaries.)</p>
<h2>SPECIAL NAMES</h2>
<dl>
<dt><code>-dNOCACHE</code></p>
<dd> Disables character caching. Useful only for debugging.</p>
<dt><code>-dNOBIND</code></p>
<dd> Disables the &quot;bind&quot; operator. Useful only for debugging.</p>
<dt><code>-dNODISPLAY</code></p>
<dd> Suppresses the normal initialization of the output device. This may be useful when debugging.</p>
<dt><code>-dNOPAUSE</code></p>
<dd> Disables the prompt and pause at the end of each page. This may be desirable for applications where another program is driving Ghostscript.</p>
<dt><code>-dNOPLATFONTS</code></p>
<dd> Disables the use of fonts supplied by the underlying platform (for instance X Windows). This may be needed if the platform fonts look undesirably different from the scalable fonts.</p>
<dt><code>-dSAFER</code></p>
<dd> Restricts file operations the job can perform. Now the default mode of operation.</p>
<dt><code>-dWRITESYSTEMDICT</code></p>
<dd> Leaves &quot;systemdict&quot; writable. This is necessary when running special utility programs, but is strongly discouraged as it bypasses normal Postscript security measures.</p>
<dt><code>-sDEVICE=</code><i>device</i></p>
<dd> Selects an alternate initial output device, as described above.</p>
<dt><code>-sOutputFile=</code><i>filename</i></p>
<dd> Selects an alternate output file (or pipe) for the initial output device, as described above.</dl>
<h2>SAFER MODE</h2>
<p> The <code>-dSAFER</code> option restricts file system accesses to those files and directories allowed by the relevant environment variables (such as GS_LIB) or by the command line parameters (see <a rel="nofollow" href="https://ghostscript.com/doc/current/Use.htm">https://ghostscript.com/doc/current/Use.htm</a> for details). </p>
<p> SAFER mode is now the default mode of operation. Thus when running programs that need to open files or set restricted parameters you should pass the <code>-dNOSAFER</code> command line option or its synonym <code>-dDELAYSAFER</code>. </p>
<p> Running with NOSAFER/DELAYSAFER (as the same suggests) loosens the security and is thus recommended ONLY for debugging or in VERY controlled workflows, and strongly NOT recommended in any other circumstances.</p>
<h2>FILES</h2>
<p> The locations of many Ghostscript run-time files are compiled into the executable when it is built. Run &quot;<code>gs -h</code>&quot; to find the location of Ghostscript documentation on your system, from which you can get more details. On a Debian system they are in <code>/usr</code>.</p>
<dl>
<dt><code>/usr/share/ghostscript/[0-9]*.[0.9]*/*</code></p>
<dd> Startup files, utilities, and basic font definitions (where [0-9]*.[0.9]* is the ghostscript version)</p>
<dt><code>/usr/share/fonts/type1/gsfonts/*</code></p>
<dd> More font definitions from the gsfonts package</p>
<dt><code>/usr/share/doc/ghostscript/examples/*</code></p>
<dd> Ghostscript demonstration files (if ghostscript-doc package is installed)</p>
<dt><code>/usr/share/doc/ghostscript/*</code></p>
<dd> Diverse document files (may need to install ghostscript-doc package)</dl>
<h2>INITIALIZATION FILES</h2>
<p> When looking for the initialization files &quot;gs_*.ps&quot;, the files related to fonts, or the file for the &quot;run&quot; operator, Ghostscript first tries to open the file with the name as given, using the current working directory if no directory is specified. If this fails, and the file name doesn&#8217;t specify an explicit directory or drive (for instance, doesn&#8217;t contain &quot;/&quot; on Unix systems), Ghostscript tries directories in this order:</p>
<dl>
<dt>1.</p>
<dd> the directories specified by the <code>-I</code> switches in the command line (see below), if any;</p>
<dt>2.</p>
<dd> the directories specified by the <code>GS_LIB</code> environment variable, if any;</p>
<dt>3.</p>
<dd> the directories specified by the <code>GS_LIB_DEFAULT</code> macro in the Ghostscript makefile when the executable was built. <code>GS_LIB_DEFAULT</code> is &quot;/usr/share/ghostscript/[0-9]*.[0-9]*/lib&quot; on a Debian system where &quot;[0-9]*.[0-9]*&quot; represents the Ghostscript version number</dl>
<p> Each of these (<code>GS_LIB_DEFAULT</code>, <code>GS_LIB</code>, and <code>-I</code> parameter) may be either a single directory or a list of directories separated by &quot;:&quot;.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GS_OPTIONS</code></p>
<dd> String of options to be processed before the command line options</p>
<dt><code>GS_DEVICE</code></p>
<dd> Used to specify an output device</p>
<dt><code>GS_FONTPATH</code></p>
<dd> Path names used to search for fonts</p>
<dt><code>GS_LIB</code></p>
<dd> Path names for initialization files and fonts</p>
<dt><code>TEMP</code></p>
<dd> Where temporary files are made</dl>
<h2>X RESOURCES</h2>
<p> Ghostscript, or more properly the X11 display device, looks for the following resources under the program name &quot;Ghostscript&quot;:</p>
<dl>
<dt><code>borderWidth</code></p>
<dd> The border width in pixels (default = 1).</p>
<dt><code>borderColor</code></p>
<dd> The name of the border color (default = black).</p>
<dt><code>geometry</code></p>
<dd> The window size and placement, WxH+X+Y (default is NULL).</p>
<dt><code>xResolution</code></p>
<dd> The number of x pixels per inch (default is computed from <code>WidthOfScreen</code> and <code>WidthMMOfScreen</code>).</p>
<dt><code>yResolution</code></p>
<dd> The number of y pixels per inch (default is computed from <code>HeightOfScreen</code> and <code>HeightMMOfScreen</code>).</p>
<dt><code>useBackingPixmap</code></p>
<dd> Determines whether backing store is to be used for saving display window (default = true).</dl>
<p> See the usage document for a more complete list of resources. To set these resources on Unix, put them in a file such as &quot;~/.Xresources&quot; in the following form: </p>
<pre>
        Ghostscript*geometry:    612x792-0+0
        Ghostscript*xResolution: 72
        Ghostscript*yResolution: 72
</pre>
<p> Then merge these resources into the X server&#8217;s resource database: </p>
<pre>
        % xrdb -merge ~/.Xresources
</pre>
<h2>SEE ALSO</h2>
<p> The various Ghostscript document files (above), especially <code>Use.htm</code>. On Debian you may need to install ghostscript-doc before reading the documentation.</p>
<h2>BUGS</h2>
<p> See <a rel="nofollow" href="http://bugs.ghostscript.com/">http://bugs.ghostscript.com/</a> and the Usenet news group comp.lang.postscript.</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. Russell J. Lang, gsview at ghostgum.com.au, is the author of most of the MS Windows code in Ghostscript. </p>
<h2>Index</h2>
