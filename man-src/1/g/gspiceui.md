---
title: "gspiceui(1)"
name: "gspiceui"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gspiceui/"
description: "gspiceui – GUI frontend for various electronic circuit simulation engines"
---

<h2>NAME</h2>
<p> gspiceui &#8211; GUI frontend for various electronic circuit simulation engines </p>
<h2>SYNOPSIS</h2>
<p> <code>gspiceui</code> [-v] [-h] [-r RCFILE] [-s SIMENG] [-a ANA] [-g [PROC]] [-w VIEWER] [FILE/S] </p>
<h2>DESCRIPTION</h2>
<p> GNU Spice GUI (gSpiceUI) is intended to provide a GUI for various freely available electronic circuit simulation engines ie. GNU-Cap and NG-Spice. It uses gNetList to convert schematic files to net list files and gWave or Gaw to display simulation results. gSchem is the preferred schematic capture tool. </p>
<h2>OPTIONS</h2>
<p> <i>gspiceui</i> accepts the following options : </p>
<dl>
<dt><code>-v</code></p>
<dd> Print version information. </p>
<dt><code>-h</code></p>
<dd> Print usage information. </p>
<dt><code>-r RCFILE</code></p>
<dd> Specify a configuration file. </p>
<dt><code>-s SIMENG</code></p>
<dd> Specify the simulation engine to be used. </p>
<dt><code>-a ANA</code></p>
<dd> Specify the analysis page to be displayed. </p>
<dt><code>-g [PROC]</code></p>
<dd> Specify the guile procedure which is executed to create the netlist. </p>
<dt><code>-w VIEWER</code></p>
<dd> Specify the waveform viewer to be used. </p>
<dt><code>FILE/S</code></p>
<dd> Specify a circuit description file to load or schematic file/s to import. If multiple schematics files are specified they are read sequentially and parsed with the assumption that they are all part of the same design. Any file/s must be specified at the end of the command line.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;m.waters [at] bom.gov.au&gt;. </p>
<h2>AUTHOR</h2>
<p> Written by Michael Waters </p>
<h2>SEE ALSO</h2>
<p> <code>gschem</code> (1), <code>gnetlist</code> (1), <code>ngspice</code> (1), <code>gnucap</code> (1), <code>gwave</code> (1), <code>gaw</code> (1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2009 Mike Waters </p>
<p> This document can be freely redistributed according to the terms of the GNU General Public License version 2.0 </p>
<h2>Index</h2>
