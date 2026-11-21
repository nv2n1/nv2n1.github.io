---

title: "faldisass(1)"
name: "faldisass"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faldisass/"
description: "faldissass – The Falcon disassembler"
---

<h2>NAME</h2>
<p> faldissass &#8211; The Falcon disassembler </p>
<p> <code>faldissass [options]</code> <i>module_file.fam</i> </p>
<p> The <code>faldissass</code> command line tool disassembles a compiled .fam Falcon module. The output human-readable Falcon Virtual Machine assembly is sent to the standard output. </p>
<p> The tool has mainly two working modes. The standard mode procues an assembly dump containing the PC counter address that will be associated with each instruction in the VM. This allows to see exactly on which VM instruction an error was raised (as the PC at error raisal is always shown in error dumps), or to debug the VM by following the PC register in step-by-step mode. </p>
<p> The isomorphic mode creates a compilable assembly source that can the be feed into the falcon assembler to obtain a compiled module. In example, this can be used for VM level hand-made finetuning optimizations. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-d</dt>
<dd> Dump the dependency table (list of load directives). </dd>
<dt>-h</dt>
<dd> Show version and a short help. </dd>
<dt>-i</dt>
<dd> Create an isomorphic version of the original assembly. </dd>
<dt>-l</dt>
<dd> add line informations. </dd>
<dt>-s</dt>
<dd> Dump the string table. </dd>
<dt>-S</dt>
<dd> Write the strings inline instead of using #strid </dd>
<dt>-y</dt>
<dd> Dump the symbol table. </dd>
</dl>
<h2>FILES</h2>
<p> <i>/usr/lib/libfalcon_engine.so</i></p>
<dl>
<dt>
</dt><dd> Default location of the Falcon Engine loadable module.</dd></dl>
<h2>AUTHOR</h2>
<p> Giancarlo Niccolai &lt;gc [at] falconpl.org&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-falcon/">falcon</a></code>(1) <code><a href="/docs/linux/man/1-falrun/">falrun</a></code>(1) </p>
<h2>LICENSE</h2>
<p> This document is released under the &quot;GNU Free Documentation License, version 1.2&quot;. On Debian systems, the complete text of the Free Documentation License, version 1.2, can be found in /usr/share/common-licenses/. </p>
