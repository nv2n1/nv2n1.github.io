---
title: "gnuplot-qt(1)"
name: "gnuplot-qt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnuplot-qt/"
description: "gnuplot – an interactive plotting program"
---

<h2 class="name">NAME</h2>
<p> gnuplot &#8211; an interactive plotting program </p>
<h2>SYNOPSIS</h2>
<p> <code>gnuplot</code> [X11 options] [options] [file &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>Gnuplot</code> is a command-driven interactive plotting program. </p>
<p> If file names are given on the command line, gnuplot loads and executes each file in the order specified, and exits after the last file is processed. If no files are given, <code>gnuplot</code> prompts for interactive commands. </p>
<p> Here are some of its features: </p>
<p> Plots any number of functions, built up of C operators, C math library functions, and some things C doesn&#8217;t have like **, sgn(), etc. </p>
<p> User-defined constants and functions. </p>
<p> All computations performed in the complex domain. Just the real part is plotted by default, but functions like imag() and abs() and arg() are available to override this. </p>
<p> Many presentation styles for plotting user data from files, including surface-fitting, error bars, boxplots, histograms, heat maps, and simple manipulation of image data. There is an on-line demo collection at<br />
 <i><a rel="nofollow" href="http://gnuplot.info/demo">http://gnuplot.info/demo</a></i> </p>
<p> Nonlinear least-squares fitting. </p>
<p> 2D and 3D plots with mouse-controlled zooming, rotation, and hypertext. </p>
<p> Shell escapes and command line substitution. </p>
<p> Load and save capability. </p>
<p> Support for a huge variety of output devices and file formats.</p>
<h2>OPTIONS</h2>
<p> <code>-p, &#8211;persist</code> lets plot windows survive after main gnuplot program exits. </p>
<p> <code>-c scriptname ARG1 ARG2 &#8230;, load script using gnuplot&#8217;s &quot;call&quot; mechanism and pass it the remainder of the command line as arguments </p>
<p> -d, &#8211;default</code> settings. Do not read from gnuplotrc or ~/.gnuplot on entry. </p>
<p> <code>-e &quot;command list&quot;</code> executes the requested commands before loading the next input file. </p>
<p> <code>-s, &#8211;slow</code> wait for slow font initialization rather than continuing with an error. </p>
<p> <code>-h, &#8211;help</code> print summary of usage </p>
<p> <code>-V</code> show current version</p>
<h2>X11 OPTIONS</h2>
<p> For terminal type x11, <i>gnuplot</i> accepts the standard X Toolkit options and resources such as geometry, font, and background. See the <a href="/docs/linux/man/1-x/">X</a>(1) man page for a description of common options. For additional X options specific to gnuplot, type <i>help x11</i> on the gnuplot command line. These options have no effect on other terminal types.</p>
<h2>ENVIRONMENT</h2>
<p> A number of shell environment variables are understood by gnuplot. None of these are required.</p>
<dl>
<dt><code>GNUTERM</code></p>
<dd> The name of the terminal type to be used by default. This can be overridden by the gnuplotrc or .gnuplot start-up files and, of course, by later explicit &quot;set terminal&quot; commands.</p>
<dt><code>GNUHELP </code></p>
<dd> The pathname of the HELP file (gnuplot.gih).</p>
<dt><code>HOME</code></p>
<dd> The name of a directory to search for a .gnuplot file.</p>
<dt><code>PAGER</code></p>
<dd> An output filter for help messages.</p>
<dt><code>SHELL</code></p>
<dd> The program used for the &quot;shell&quot; command.</p>
<dt><code>FIT_SCRIPT</code></p>
<dd> Specifies a gnuplot command to be executed when a fit is interrupted&#8212;see &quot;help fit&quot;.</p>
<dt><code>FIT_LOG</code></p>
<dd> The name of the logfile maintained by fit.</p>
<dt><code>GNUPLOT_LIB</code></p>
<dd> Additional search directories for data and command files. The variable may contain a single directory name, or a list of directories separated by &#8216;:&#8217;. The contents of GNUPLOT_LIB are appended to the &quot;loadpath&quot; variable, but not saved with the &quot;save&quot; and &quot;save set&quot; commands.</p>
<dt><code>GDFONTPATH</code></p>
<dd> Several gnuplot terminal drivers access TrueType fonts via the gd library. This variable gives the font search path for these drivers.</p>
<dt><code>GNUPLOT_DEFAULT_GDFONT</code></p>
<dd> The default font for the terminal drivers that access TrueType fonts via the gd library.</p>
<dt><code>GNUPLOT_FONTPATH</code></p>
<dd> The font search path used by the postscript terminal. The format is the same as for GNUPLOT_LIB. The contents of GNUPLOT_FONTPATH are appended to the &quot;fontpath&quot; variable, but not saved with the &quot;save&quot; and &quot;save set&quot; commands.</p>
<dt><code>GNUPLOT_PS_DIR</code></p>
<dd> Used by the postscript driver to locate external prologue files. Depending on the build process, gnuplot contains either a builtin copy of those files or simply a default hardcoded path. Use this variable to test the postscript terminal with custom prologue files. See &quot;help postscript prologue&quot;.</dl>
<h2>FILES</h2>
<dl>
<dt><i>gnuplotrc</i></p>
<dd> When gnuplot is run, it first looks for a system-wide initialization file named gnuplotrc. The standard location of this file expected by the program is reported by the &quot;show loadpath&quot; command.</p>
<dt><i>.gnuplot</i></p>
<dd> After loading the system-wide initialization file, if any, Gnuplot looks for a private initialization file in the HOME directory. It may contain any legal gnuplot commands, but typically they are limited to setting the preferred terminal and line types and defining frequently-used functions or variables.</p>
<dt><i>fit.log</i></p>
<dd> The default name of the logfile output by the &quot;fit&quot; command.</dl>
<h2>AUTHORS</h2>
<p> Original authors: Thomas Williams and Colin Kelley. Starting with gnuplot version 3.8, the project source is cooperatively maintained on SourceForge by a large number of contributors.</p>
<h2>BUGS</h2>
<p> Please report bugs using the project bug tracker on SourceForge.</p>
<h2>SEE ALSO</h2>
<p> See the printed manual or the on-line help for details on specific commands. Project web site at <a rel="nofollow" href="http://gnuplot.info">http://gnuplot.info</a> </p>
<h2>Index</h2>
