---
title: "rdf2com(1)"
name: "rdf2com"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdf2com/"
description: "rdf2bin, rdf2com – convert an RDOFF object file to flat binary"
---

<h2>NAME</h2>
<p> rdf2bin, rdf2com &#8211; convert an RDOFF object file to flat binary</p>
<h2>SYNOPSIS</h2>
<p> <code>rdf2bin</code> [-o <i>relocation-origin</i>] [-p <i>segment-alignment</i>] [-f <i>format</i>] <i>input-file</i> <i>output-file</i><br />
 <code>rdf2com</code> [-p <i>segment-alignment</i>] <i>input-file</i> <i>output-file</i><br />
 <code>rdf2ith</code> [-o <i>relocation-origin</i>] [-p <i>segment-alignment</i>] <i>input-file</i> <i>output-file</i><br />
 <code>rdf2srec</code> [-o <i>relocation-origin</i>] [-p <i>segment-alignment</i>] <i>input-file</i> <i>output-file</i></p>
<h2>OPTIONS</h2>
<dl>
<dt>-o <i>relocation-origin</i></p>
<dd> Relocate at origin <i>relocation-origin</i>. If invoked as <code>rdf2com</code>, the default relocation origin will be 0x100. Else, the default origin is 0.</p>
<dt>-p <i>segment-alignment</i></p>
<dd> Pad segments until their size is a multiple of <i>segment-alignment</i>. By default, 16 is used.</p>
<dt>-f <i>format</i></p>
<dd> Specify the output format. The currently supported formats are binary (<i>bin</i>), DOS COM (binary with origin 0x100) (<i>com</i>) Intel hex (<i>ith</i> or <i>ihx</i>), and Motorola S-Records (<i>srec</i>). If not specified, the format is set by the command name.</dl>
<h2>AUTHORS</h2>
<p> Julian Hall &lt;jules [at] earthcorp.com&gt;, H. Peter Anvin &lt;hpa [at] zytor.com&gt;. </p>
<p> This manual page was written by Matej Vela &lt;vela [at] debian.org&gt;.</p>
<h2>BUGS</h2>
<p> This utility currently only supports the classic segments <i>.text</i>, <i>.data</i> and <i>.bss</i>. </p>
<h2>Index</h2>
