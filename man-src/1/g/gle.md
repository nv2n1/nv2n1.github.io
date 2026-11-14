---
title: "gle(1)"
name: "gle"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gle/"
description: "gle – Graphics Layout Engine"
---

<h2>NAME</h2>
<p> gle &#8211; Graphics Layout Engine</p>
<h2>SYNOPSIS</h2>
<p> <code>gle</code> [options] <i>file.gle</i> <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> GLE (Graphics Layout Engine) is a graphics scripting language designed for creating publication quality graphs, plots, diagrams, figures and slides. GLE supports various graph types (function plots, histograms, bar graphs, scatter plots, contour lines, color maps, surface plots, &#8230;) through a simple but flexible set of graphing commands. More complex output can be created by relying on GLE&#8217;s scripting language, which is full featured with subroutines, variables, and logic control. GLE relies on LaTeX for text output and supports mathematical formulea in graphs and figures. GLE&#8217;s output formats include EPS, PS, PDF, JPEG, and PNG.</p>
<h2>DOCUMENTATION</h2>
<p> GLE&#8217;s documentation is distrubuted in PDF format and can be found at the GLE website: &lt;<a rel="nofollow" href="http://www.gle-graphics.org">http://www.gle-graphics.org</a>&gt;</p>
<h2>OPTIONS</h2>
<dl>
<dt>-help</p>
<dd> Shows help about command line options.</p>
<dt>-info</p>
<dd> Outputs software version, build date, GLE_TOP, GLE_BIN, etc..</p>
<dt>-verbosity</p>
<dd> Sets the verbosity level of GLE console output.</p>
<dt>-device</p>
<dd> Selects output device(s).</p>
<dt>-resolution</p>
<dd> Sets the resolution for bitmap and PDF output.</p>
<dt>-fullpage</p>
<dd> Selects full page output.</p>
<dt>-output</p>
<dd> Specifies the name of the output file.</p>
<dt>-preview</p>
<dd> Previews the output with QGLE.</p>
<dt>-gs</p>
<dd> Previews the output with GhostScript.</p>
<dt>-version</p>
<dd> Selects a GLE version to run.</p>
<dt>-compatibility</p>
<dd> Selects a GLE compatibility mode.</p>
<dt>-calc</p>
<dd> Runs GLE in &quot;calculator&quot; mode.</p>
<dt>-tex</p>
<dd> Indicates that the script includes LaTeX expressions.</p>
<dt>-inc</p>
<dd> Creates an .inc file with LaTeX code.</p>
<dt>-texincprefix</p>
<dd> Adds the given subdirectory to the path in the .inc file.</p>
<dt>-mkinittex</p>
<dd> Creates &quot;inittex.ini&quot; from &quot;init.tex&quot;.</p>
<dt>-nocolor</p>
<dd> Forces grayscale output.</p>
<dt>-transparent</p>
<dd> Creates transparent output (with -d png).</p>
<dt>-noctrl-d</p>
<dd> Excludes CTRL-D from the PostScript output.</p>
<dt>-nomaxpath</p>
<dd> Disables the upper-bound on the drawing path complexity.</p>
<dt>-safemode</p>
<dd> Disables reading/writing to the file system.</p>
<dt>-allowread</p>
<dd> Allows reading from the given path.</p>
<dt>-allowwrite</p>
<dd> Allows writing to the given path.</dl>
<h2>FILES</h2>
<p> <i>/usr/share/gle-graphics/4.2.1/glerc</i></p>
<dl>
<dt>
<dd> The system wide configuration file.</dl>
<p> <i>~/.glerc</i></p>
<dl>
<dt>
<dd> Per user configuration file.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>GLE_USRLIB</p>
<dd> The search path for include files.</p>
<dt>GLE_TOP</p>
<dd> The location of the fonts and other resources. </p>
</dl>
<h2>Index</h2>
