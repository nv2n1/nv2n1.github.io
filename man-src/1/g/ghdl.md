---
title: "ghdl(1)"
name: "ghdl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ghdl/"
description: "ghdl – VHDL compiler/simulator"
---

<h2>NAME</h2>
<p> ghdl &#8211; VHDL compiler/simulator</p>
<h2>SYNOPSIS</h2>
<p> <code>ghdl</code> [<i>command</i>]<i> </i>[<i>options</i>]<i> files</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ghdl</code> command. This manual page was written for user of man, but is not as complete as the reference documentation. </p>
<p> Instead, users should read the GHDL texinfo manual</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of the main modes and options is included below. For a complete description, refer to the GHDL texinfo manual. </p>
<p> Basic commands:</p>
<dl>
<dt><code>-a</code></p>
<dd> Analysis, i.e. <i>ghdl -a file.vhdl</i></p>
<dt><code>-e</code></p>
<dd> Elabortation, i.e. <i>ghdl -e unit_name</i></p>
<dt><code>-r</code></p>
<dd> Run: run the simulation, i.e. <i>ghdl -r unit_name</i></p>
<dt><code>-s</code></p>
<dd> Syntax-check, i.e. <i>ghdl -s file.vhdl</i></p>
<dt><code>&#8211;clean</code></p>
<dd> Clean: remove generated files, i.e. <i>ghdl &#8211;clean</i></p>
<dt><code>-h, &#8211;help</code></p>
<dd> Help, i.e. <i>ghdl &#8211;help</i></p>
<dt><code>&#8211;version</code></p>
<dd> Version, i.e. <i>ghdl &#8211;version</i></dl>
<p> Basic options:</p>
<dl>
<dt><code>&#8211;work=NAME</code></p>
<dd> Name of the WORK library, i.e. <i> ghdl -a &#8211;work=foo foo.vhdl</i></p>
<dt><code>&#8211;std=STD</code></p>
<dd> Which VHDL standard (87|93|93c|00|02), i.e. <i>ghdl -a &#8211;std=87 old.vhdl</i></p>
<dt><code>&#8211;ieee=VER</code></p>
<dd> Which IEEE library (none|standard|synopsys|mentor), i.e. <i>ghdl -a &#8211;ieee=synopsys broken.vhdl</i></p>
<dt><code>&#8211;no-vital-checks</code></p>
<dd> Disable VITAL restriction checking, i.e. <i>ghdl -a &#8211;no-vital-checks unsupported_vital.vhdl</i></dl>
<p> There are many more modes and options; please consult the documentation. </p>
<p> Executables created by GHDL have addition simulation options. The most important ones are listed below:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show options for simulation and execution.</p>
<dt><code>&#8211;assert-level=LEVEL</code></p>
<dd> Assert level at which to stop simulation (none|note|warning|error|failure), i.e. <i>./touchy_design &#8211;assert-level=note</i><code></p>
<dt>&#8211;stop-time=TIME</code></p>
<dd> Stop simuation after TIME, i.e. <i>./design &#8211;stop-time=50ns</p>
<dt></i><code>&#8211;vcd=FILENAME</code></p>
<dd> Dump VCD to FILENAME (a waveform dump, viewable with&#8211;for instance&#8211;<code>gtkwave</code>), i.e. <i>./design &#8211;vcd=design.vcd</p>
<dt></i><code>&#8211;sdf=[TYPE=]PATH=FILENAME</code></p>
<dd> Back annotate SDF onto design using TYPE (min|typ|max), instance PATH, and SDF file FILENAME, i.e. <i>./sdf_design &#8211;sdf=typ=top/inst=inst.sdf</i> </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code>gtkwave (1)</code></p>
<dd></dl>
<p> The texinfo manual fully documents GHDL. You may also browse it at <code>&lt;<a rel="nofollow" href="http://ghdl.free.fr/ghdl/index.html">http://ghdl.free.fr/ghdl/index.html</a>&gt;</code>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Wesley J. Landaker &lt;wjl [at] icecavern.net&gt;, for the Debian project (but may be used by others). It is released under the same terms as GHDL, i.e. the GNU General Public License. It was modified by Tristan Gingold to include it in the GHDL sources. </p>
<h2>Index</h2>
