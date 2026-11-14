---
title: "fig2ps(1)"
name: "fig2ps"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fig2ps/"
description: "fig2ps, fig2eps,fig2pdf – Convert xfig files in ps|pdf, processing all the text marked as special with LaTeX."
---

<h2 class="name">NAME</h2>
<p> fig2ps, fig2eps,fig2pdf &#8211; Convert xfig files in ps|pdf, processing all the text marked as special with LaTeX.</p>
<h2>SYNOPSIS</h2>
<p> <code>fig2ps </code>[<code>-h</code>|<code>&#8211;help</code>] </p>
<p> <code>fig2ps </code> [<i> options </i>] <i>file1.fig </i>[<i>file2.fig &#8230;</i>] </p>
<p> <code>fig2pdf</code> [<i> options </i>] <i>file1.fig </i>[<i>file2.fig &#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>fig2ps </code> converts figures produced by XFig into postscript or PDF, processing the text with LaTeX. It takes advantage of the <i>pstex</i> and <i>pstext_t</i> export formats of <code>fig2dev</code>. </p>
<p> <code>fig2ps</code> converts successively all the files given as arguments. It&#8217;s behaviour is governed by quite a few options. In all the options, the <code>=</code> sign is optional, so that </p>
<p> <i>fig2ps &#8211;bbox=dvips file.fig</i> </p>
<p> and </p>
<p> <i>fig2ps &#8211;bbox dvips file.fig</i> </p>
<p> are equivalent. </p>
<h2>EXAMPLES</h2>
<p> To convert <i>file.fig</i> to PS: </p>
<p> <i>fig2ps file.fig</i> </p>
<p> To convert it to PDF: </p>
<p> <i>fig2pdf file.fig</i> </p>
<p> or </p>
<p> <i>fig2ps &#8211;pdf file.fig</i> </p>
<p> If the XFig file you want to convert to PDF contains included images, you might want to try: </p>
<p> <i>fig2pdf &#8211;manual-ps2pdf file.fig</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;gv, &#8211;nogv</code></p>
<dd> If on, <code>fig2ps</code> runs <code>gv</code> on every file just after they are produced. On by default if <code>fig2ps</code> thinks it is talking to a terminal (ie not from a pipe). You might want to switch that off when processing lots of files. </p>
<dt><code>&#8211;xpdf</code></p>
<dd> Views produced files with <code>xpdf</code> rather than <code>gv</code>. Obviously, that won&#8217;t be really useful if you are producing PS files, you&#8217;ve been warned. </p>
<dt><code>&#8211;viewer</code><i>=command</i></p>
<dd> Runs <i>command</i> rather than <code>gv</code> on the produced files. </p>
<dt><code>&#8211;keep</code></p>
<dd> Tells <code>fig2ps</code> to keep the temporary directory in which temporary files are created. Useful for debugging. If this option is on, <code>fig2ps</code> prints the name of the directory when it has finished its job, so you know where to look. </p>
<dt><code>&#8211;packages</code><i>=pack1,pack2,&#8230;</i></p>
<dd> Sets the package list to be used to <i>pack1,pack2,&#8230;</i>. Resets any package given by the <code>&#8211;add</code> command-line option. For more information about packages, see the section <code>PREAMBLE</code> below. </p>
<dt><code>&#8211;add</code><i>=pack1,pack2,&#8230;</i></p>
<dd> Adds <i>pack1,pack2,&#8230;</i> to the existing list of packages. See the section <code>PREAMBLE</code> below. This option is cumulative. </p>
<dt><code>&#8211;bbox</code><i>=dvips|gs|a,b,c,d</i></p>
<dd> Chooses the method to determine the bounding box of the files. See the section <code>BOUNDING BOX</code> below for more information. </p>
<dt><code>&#8211;input</code><i>=file</i></p>
<dd> Uses file as a template for the LaTeX file. More information about that can be found in the section <code>PREAMBLE</code> below. This option was written for a private use, though you can of course profit from it. However, most of the times, what you really want is <i>&#8211;add=file</i>. <i>file</i> will be looked for using <code>kpsewhich</code>. </p>
<dt><code>&#8211;pdf, &#8211;nopdf</code></p>
<dd> Whether the final output of <code>fig2ps </code> will be PDF or postscript. This option is automatically when called as <code>fig2pdf</code>. Note that in any case, <code>fig2ps</code> has to go through Postscript output to produce a PDF file. </p>
<dt><code>&#8211;eps</code></p>
<dd> Change the output default extension from <i>.ps </i> to <i>.eps</i>. This is on by default when the program is called as <code>fig2eps</code>. It has no other effects. </p>
<dt><code>&#8211;manual-ps2pdf</code></p>
<dd> When producing PDF files, <code>fig2ps</code> uses <code>epstopdf</code> to perform the conversion. This may lead to bad quality output with embedded pictures. The use of this option disables PDF production by <code>epstopdf</code> and lets <code>ps2pdf</code> produce the final output PDF (but after tweaking the PS file using <code>epstopdf</code>). In general, this produces much better results. </p>
<dt><code>&#8211;ps2pdf-options</code></p>
<dd> When <i>&#8211;manual-ps2pdf</i> does not produce output of decent quality, you can use this option to manually feed options to <code>ps2pdf</code>. The use of this option implies <i>&#8211;manual-ps2pdf</i>. </p>
<dt><code>&#8211;keepps</code></p>
<dd> When producing a PDF file, asks <code>fig2ps</code> to keep the intermediary Postscript file. </p>
<dt><code>&#8211;forcespecial, &#8211;noforcespecial</code></p>
<dd> <code>fig2ps </code> only processes with LaTeX text which is marked as <i>special</i> in the Fig file. When this option is on, all text is treated as if it was marked with the <i>special</i> flag. </p>
<dt><code>&#8211;dvips</code><i>=string</i></p>
<dd> Passes <i>string</i> as options for <code>dvips</code>. </p>
<dt><code>&#8211;fig2dev</code><i>=string</i></p>
<dd> Passes <i>string</i> as options for <code>fig2dev</code>. </p>
<dt><code>&#8211;preamble</code><i>=string</i></p>
<dd> Adds <i>string</i> in the preamble of the LaTeX file generated, just before the <i>egin{document}</i> stanza. Effects are cumulative. </p>
<dt><code>-V</code>, <code> &#8211;version</code></p>
<dd> Prints the version of <code>fig2ps</code> and exits. </p>
</dl>
<h2>CONFIGURATION FILES</h2>
<p> Many of the command-line options can be set in either the system-wide (in <i>/etc</i>) or the user configuration file (in the user&#8217;s home directory). Some more details can be configured in the configuration files. Global configuration is overridden by users&#8217; configuration which in turn is overridden by the command line options. Here is a list of the variables you can define: </p>
<dl>
<dt><code>PACKAGES</code><i>=pack1,pack2&#8230;</i></p>
<dd> Defines the basic list of packages. See the <code>PREAMBLE</code> section. </p>
<dt><code>ADD</code><i>=pack1,pack2</i></p>
<dd> Has the same effect as the <code>&#8211;add </code> command-line option. Does not make too much sense in the global configuration file, but you might want to use it in a personal one. </p>
<dt><code>DOC_CLASS</code><i>=class</i></p>
<dd> Sets the document class used by LaTeX. </p>
<dt><code>DOC_OPTIONS</code><i>=Ioptions </i></p>
<dd> Sets the options for the document class. </p>
<dt><code>FORCE_SPECIAL</code><i>=0</i>|<i>1</i></p>
<dd> Sets the default for option <code>&#8211;forcespecial</code>. </p>
<dt><code>GV</code><i>=0</i>|<i>1</i></p>
<dd> Sets the default for option <code>&#8211;gv</code>. </p>
<dt><code>GV</code><i>=file</i></p>
<dd> Has the same effect as the <code>&#8211;input</code> command-line option. </p>
<dt><code>PREAMBLE</code><i>=string</i></p>
<dd> Identical to the <code>&#8211;preamble</code> option, with the slight difference that the in configuration files, it is not cumulative: the last assignment seen is the only taken into account. </p>
<dt><code>KEEP_PS</code><i>=0</i>|<i>1</i></p>
<dd> Sets the default for option <code>&#8211;keepps</code>. </p>
</dl>
<h2>PREAMBLE</h2>
<p> The preamble of the LaTeX file is built as such: </p>
<dl>
<dt><code>*</code></p>
<dd> if a <code>&#8211;input</code> file is specified, it will be used directly with a <i>\input</i> statement. A <i>\documentclass</i> statement will be added if the input file does not contain any.</p>
<dt><code>*</code></p>
<dd> else, a preamble is made based on the values of <code>DOC_CLASS</code>, <code>DOC_OPTIONS</code>, and <code>PACKAGES</code> (the latter is overridden by the <code>&#8211;packages</code> command-line option). See below for the format of the package variables. </p>
</dl>
<p> Then, the packages specified using the <code>ADD</code> variable and the <code>&#8211;add</code> command-line options are added to the preamble, followed by the <i>geometry</i> package that deals with setting the size of the output (tweaked for <code>fig2ps</code>&#8216;s purposes) and finally the contents of the <code>PREAMBLE</code> variable and the <code>&#8211;preamble</code> command-line options. </p>
<p> The <code>&#8211;packages</code> and <code>&#8211;add</code> options, and the corresponding variables, take a comma separated list of packages. Options for the packages can be specified in two ways: </p>
<dl>
<dt><i>[option]package</i></p>
<dd> in which you can only specify one option;</p>
<dt><i>option1:option2:&#8230;:package</i></p>
<dd> in which you can specify an arbitrary number of options, as long as you don&#8217;t need a comma inside an option. Should the need arise, use <code>&#8211;preamble</code>. </p>
</dl>
<h2>BOUNDING BOX</h2>
<p> One of the delicate jobs of <code>fig2ps</code> is to set the bounding box of the produced file, that is the rectangle that holds the figure. There are basically three ways for <code>fig2ps</code> to get them: </p>
<dl>
<dt><i>dvips</i></p>
<dd> In this mode, <code>fig2ps</code> runs <code>dvips</code> with the <i>-E</i> option. It works reasonably fine most of the time, but it will produce incorrect results if you have rotated text near the edge of the graph. </p>
<dt><i>gs</i></p>
<dd> Asks <code>gs</code> to tell the bounding box of the figure. It used to produce systematically perfect results, but the quality has degraded somehow recently. It still works in most of the cases, and that is why it is the default. It fails on very large pictures. </p>
<dt><i>a,b,c,d</i></p>
<dd> Specify your bounding box by hand. </p>
</dl>
<p> The benefits of using the last two methods is that <code>fig2ps</code> tells you how big the picture is (in centimeters). </p>
<h2>FILES</h2>
<p> <i>/etc/fig2ps/fig2ps.rc</i>, <i>$HOME/.fig2ps.rc</i> </p>
<p> The <i>examples/</i> directory in the source tarball contains some examples. Check <code>fig2ps</code> on them to see if it works fine, but keep in mind that <code>fig2ps</code> will choke on <i>examples/Large-example.fig</i> ! </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xfig/">xfig</a></code>(1), <code><a href="/docs/linux/man/1-fig2dev/">fig2dev</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1), <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-kpsewhich/">kpsewhich</a></code>(1) </p>
<p> The Sourceforge project page at: </p>
<p> <i><a rel="nofollow" href="http://sourceforce.net/projects/fig2ps">http://sourceforce.net/projects/fig2ps</a></i> </p>
<h2>AUTHOR</h2>
<p> This script was written by Vincent Fourmond, from an original idea of Seb Desreux (the first script is for private use, and used the eepic export of xfig, which is severely limitated), improved by a few others&#8230; </p>
<h2>BUG REPORT AND FEATURE REQUESTS</h2>
<p> Please use the tracker from the Sourceforge project page: </p>
<p> <i><a rel="nofollow" href="https://sourceforge.net/tracker/?group_id=125824">https://sourceforge.net/tracker/?group_id=125824</a></i> </p>
<h2>Index</h2>
