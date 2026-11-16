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
<dt>-help</dt>
<dd> Shows help about command line options.</dd>
<dt>-info</dt>
<dd> Outputs software version, build date, GLE_TOP, GLE_BIN, etc..</dd>
<dt>-verbosity</dt>
<dd> Sets the verbosity level of GLE console output.</dd>
<dt>-device</dt>
<dd> Selects output device(s).</dd>
<dt>-resolution</dt>
<dd> Sets the resolution for bitmap and PDF output.</dd>
<dt>-fullpage</dt>
<dd> Selects full page output.</dd>
<dt>-output</dt>
<dd> Specifies the name of the output file.</dd>
<dt>-preview</dt>
<dd> Previews the output with QGLE.</dd>
<dt>-gs</dt>
<dd> Previews the output with GhostScript.</dd>
<dt>-version</dt>
<dd> Selects a GLE version to run.</dd>
<dt>-compatibility</dt>
<dd> Selects a GLE compatibility mode.</dd>
<dt>-calc</dt>
<dd> Runs GLE in &quot;calculator&quot; mode.</dd>
<dt>-tex</dt>
<dd> Indicates that the script includes LaTeX expressions.</dd>
<dt>-inc</dt>
<dd> Creates an .inc file with LaTeX code.</dd>
<dt>-texincprefix</dt>
<dd> Adds the given subdirectory to the path in the .inc file.</dd>
<dt>-mkinittex</dt>
<dd> Creates &quot;inittex.ini&quot; from &quot;init.tex&quot;.</dd>
<dt>-nocolor</dt>
<dd> Forces grayscale output.</dd>
<dt>-transparent</dt>
<dd> Creates transparent output (with -d png).</dd>
<dt>-noctrl-d</dt>
<dd> Excludes CTRL-D from the PostScript output.</dd>
<dt>-nomaxpath</dt>
<dd> Disables the upper-bound on the drawing path complexity.</dd>
<dt>-safemode</dt>
<dd> Disables reading/writing to the file system.</dd>
<dt>-allowread</dt>
<dd> Allows reading from the given path.</dd>
<dt>-allowwrite</dt>
<dd> Allows writing to the given path.</dd></dl>
<h2>FILES</h2>
<p> <i>/usr/share/gle-graphics/4.2.1/glerc</i></p>
<dl>
<dt>
</dt><dd> The system wide configuration file.</dd></dl>
<p> <i>~/.glerc</i></p>
<dl>
<dt>
</dt><dd> Per user configuration file.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>GLE_USRLIB</dt>
<dd> The search path for include files.</dd>
<dt>GLE_TOP</dt>
<dd> The location of the fonts and other resources. </dd>
</dl>
<h2>Index</h2>
