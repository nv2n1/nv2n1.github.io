---
title: "udo(1)"
name: "udo"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udo/"
description: "udo – convert files from UDO into different formats"
---

<h2 class="name">NAME</h2>
<p> udo &#8211; convert files from UDO into different formats</p>
<h2>SYNOPSIS</h2>
<p> udo [-adDghHilmnpqrstvwWxy] source file<br />
 udo [-adDghHilmnpqrstvwWxy] -o destination file source file </p>
<h2>DESCRIPTION</h2>
<p> <code>UDO</code> converts files from the UDO format into Apple-QuickView, ASCII, HTML, Texinfo, Linuxdoc-SGML, Manualpage, Pure-C-Help, Rich Text Format, ST-Guide, LaTeX, Turbo Vision Help or Windows Help. </p>
<p> Using the first method UDO prints the destination format to the standard output (STDOUT) and error messages to the standard error output (STDERR). Using the second method UDO writes the destination format to the destination file and error messages to a log file with the suffix .ul?. </p>
<p> You have to pass single options to <code>UDO</code> : -al isn&#8217;t the same as -a -l! </p>
<p> The name of the source file has to be the last option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;ascii</code></p>
<dd> The source file will be converted to ASCII.</p>
<dt><code>&#8211;amg</code></p>
<dd> The source file will be converted to AmigaGuide.</p>
<dt><code>&#8211;aqv, &#8211;quickview</code></p>
<dd> The source file will be converted to Apple QuickView.</p>
<dt><code>-c, &#8211;c</code></p>
<dd> A C sourcecode will be generated from the source file. Normal text becomes comment, the content of the sourcecode environment becomes C code.</p>
<dt><code>&#8211;check</code></p>
<dd> Additional checkings will be activated.</p>
<dt><code>-d, &#8211;no-idxfile</code></p>
<dd> Suppresse the generation of index files.</p>
<dt><code>&#8211;drc</code></p>
<dd> The source file will be converted to David&#8217;s Readme Compiler format.</p>
<dt><code>-D symbol</code></p>
<dd> Set the symbol `symbol&#8217; which can be tested in the source file with <i>!ifset</i></p>
<dt><code>&#8211;force-long</code></p>
<dd> Force files with long file names.</p>
<dt><code>&#8211;force-short</code></p>
<dd> Force files with short file names (8+3).</p>
<dt><code>-f, &#8211;pdflatex</code></p>
<dd> The source file will be converted to PDFLaTeX sourcecode.</p>
<dt><code>-g, &#8211;helptag</code></p>
<dd> The source file will be converted to HP Helptag SGML.</p>
<dt><code>&#8211;help</code></p>
<dd> Outputs a help page and quits.</p>
<dt><code>-h, &#8211;html</code></p>
<dd> The source file will be converted to HTML.</p>
<dt><code>-hh, &#8211;htmlhelp</code></p>
<dd> The source file will be converted to HTML-Help.</p>
<dt><code>-H, &#8211;hold</code></p>
<dd> You have to press a key before <code>UDO</code> finishes.</p>
<dt><code>-i, &#8211;info</code></p>
<dd> The source file will be converted to GNU Texinfo.</p>
<dt><code>&#8211;ipf</code></p>
<dd> The source file will be converted to OS/2 IPF format.</p>
<dt><code>&#8211;lyx</code></p>
<dd> The source file will be converted to LyX.</p>
<dt><code>-l, &#8211;no-logfile</code></p>
<dd> When using the Option -o <code>UDO</code> doesn&#8217;t save a log file.</p>
<dt><code>-m, &#8211;man</code></p>
<dd> The source file will be converted to a manualpage.</p>
<dt><code>&#8211;map</code></p>
<dd> Generate a C header file with jump id&#8217;s for the WinHelp format.</p>
<dt><code>&#8211;map-gfa</code></p>
<dd> Generate a GFA Basic header file with jump id&#8217;s for the WinHelp format.</p>
<dt><code>&#8211;map-pas</code></p>
<dd> Generate a Pascal header file with jump id&#8217;s for the WinHelp format.</p>
<dt><code>&#8211;map-vb</code></p>
<dd> Generate a VisualBasic header file with jump id&#8217;s for the WinHelp format.</p>
<dt><code>-n, &#8211;nroff</code></p>
<dd> The source file will be converted to Nroff.</p>
<dt><code>-o F, &#8211;outfile F</code></p>
<dd> <code>UDO</code> writes the output into the file named &quot;F&quot;.</p>
<dt><code>-P, &#8211;pascal</code></p>
<dd> A Pascal sourcecode will be generated from the source file. Normal text becomes comment, the content of the sourcecode environment becomes Pascal code.</p>
<dt><code>-p, &#8211;pchelp</code></p>
<dd> The source file will be converted to Pure C Help.</p>
<dt><code>&#8211;ps</code></p>
<dd> The source file will be converted to PostScript.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> <code>UDO</code> won&#8217;t print anything to STDOUT or STDERR.</p>
<dt><code>-r, &#8211;rtf</code></p>
<dd> The source file will be converted to RTF.</p>
<dt><code>&#8211;save-upr</code></p>
<dd> Generate an additional project filr (.upr). There information about outfiles, infiles, nodes and index entries are listed.</p>
<dt><code>-s, &#8211;stg</code></p>
<dd> The source file will be converted to ST-Guide.</p>
<dt><code>&#8211;test</code></p>
<dd> When using this option <code>UDO</code> won&#8217;t save a destination file.</p>
<dt><code>-t, &#8211;tex</code></p>
<dd> The source file will be converted to LaTeX.</p>
<dt><code>&#8211;tree</code></p>
<dd> When using this option <code>UDO</code> will save a file with the suffix .ut?. In this file you will see a tree with all files your source file includes.</p>
<dt><code>-u, &#8211;udo</code></p>
<dd> Generate one file in udo format containing all included source files. This allows one to put all source files into one udo file.</p>
<dt><code>&#8211;verbose</code></p>
<dd> <code>UDO</code> will print some status information wile converting the source file.</p>
<dt><code>&#8211;version</code></p>
<dd> Outputs version information and quits <code>UDO</code></p>
<dt><code>-v, &#8211;vision</code></p>
<dd> The source file will be converted to Turbo Vision Help.</p>
<dt><code>-w, &#8211;win</code></p>
<dd> The source file will be converted to Windows Help.</p>
<dt><code>-w4, &#8211;win4</code></p>
<dd> The source file will be converted to Windows Help 4.</p>
<dt><code>-W, &#8211;no-warnings</code></p>
<dd> Warnings will be suppressed. Error messages will still be printed.</p>
<dt><code>-x, &#8211;linuxdoc</code></p>
<dd> The source file will be converted to Linuxdoc-SGML.</p>
<dt><code>-y, &#8211;no-hypfile</code></p>
<dd> <code>UDO</code> doesn&#8217;t save a file with syllabification hints (.uh?) when using the option -o.</p>
<dt><code>-@ F</code></p>
<dd> <code>UDO</code> will read the options from the file named &quot;F&quot;.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>udo file.u</code></p>
<dd>
<p> Convert the source file `file.u&#8217; to ASCII (default) and print the output to the standard output and error messages to the standard error output.</p>
<dt><code>udo &#8211;tex -o output.tex file.u</code></p>
<dd>
<p> Convert the source file `file.u&#8217; to LaTeX and write the output to the file named `output.tex&#8217;. Warnings, error messages and additional information will be written to the log file named `output.ult&#8217;.</p>
<dt><code>udo -s -y -l -o ! file.u</code></p>
<dd>
<p> Convert the source file `file.u&#8217; to ST-Guide and write the output to `file.stg&#8217;. UDO won&#8217;t save a log file or a file with syllabification patterns.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> UDO looks for the file udo.ini in your home directory if </p>
<p> <code>UDOPATH</code> doesn&#8217;t exist.</p>
<dt><code>LANG</code></p>
<dd> Sets the language UDO shall use for error messages if neither <code>LC_ALL</code> nor <code>LC_MESSAGES</code> exists.</p>
<dt><code>LC_ALL</code></p>
<dd> If this is set to `german&#8217; <code>UDO</code> prints German messages. If this variable doesn&#8217;t exist <code>LC_MESSAGES</code> it tested instead.</p>
<dt><code>LC_MESSAGES</code></p>
<dd> See <code>LC_ALL</code> If this variable doesn&#8217;t exist, too, </p>
<p> <code>LANG</code> is tested instead.</p>
<dt><code>UDOPATH</code></p>
<dd> <code>UDO</code> looks for the file udo.ini in the directory defined by this variable. If <code>UDOPATH</code> doesn&#8217;t exist <code>HOME</code> is tested instead.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Everything was OK.</p>
<dt><code>&gt;0</code></p>
<dd> An error has appeared.</dl>
<h2>AUTHOR</h2>
<p> Copyright (c) 1995, 1996, 1997 by<br />
 Dirk Hagedorn (Dirk Hagedorn @ MK2, DirkHage [at] aol.com) </p>
<h2>Index</h2>
