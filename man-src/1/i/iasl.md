---
title: "iasl(1)"
name: "iasl"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iasl/"
description: "iasl – ACPI Source Language compiler/decompiler"
---

<h2 class="name">NAME</h2>
<p> iasl &#8211; ACPI Source Language compiler/decompiler </p>
<h2>SYNOPSIS</h2>
<p> <code>iasl</code> [<i>&lt;option&gt;</i>&#8230;<i>]</i> &lt;input-file&gt; <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>iasl</code> command. The option list is taken from the iasl interactive help. </p>
<p> <code>iasl</code> is an ASL compiler and decompiler. This command provides both the ability to translate one or more ASL source files to their corresponding AML binary files, and the ability to translate AML binary files back to readable ASL source. </p>
<p> Much more detailed documentation may be found at <a rel="nofollow" href="http://www.acpica.org/documentation/.">http://www.acpica.org/documentation/.</a> </p>
<h2>OPTIONS</h2>
<h3>Global</h3>
<dl>
<dt><code>-@ &lt;file&gt;</code></p>
<dd> Specify command file</p>
<dt><code>-I &lt;dir&gt;</code></p>
<dd> Specify additional include directory</p>
<dt><code>-T &lt;sig&gt;|ALL|*</code></p>
<dd> Create table template file for ACPI &lt;sig&gt;</p>
<dt><code>-v</code></p>
<dd> Display compiler version </p>
</dl>
<h3>Preprocessor</h3>
<dl>
<dt><code>-D &lt;symbol&gt;</code></p>
<dd> Define sybol for preprocessor use</p>
<dt><code>-li</code></p>
<dd> Create prepocessed output file (*.i)</p>
<dt><code>-P</code></p>
<dd> Preprocess only and create preprocessor output file (*.i)</p>
<dt><code>-Pn</code></p>
<dd> Disable preprocessor </p>
</dl>
<h3>General Output</h3>
<dl>
<dt><code>-p &lt;prefix&gt;</code></p>
<dd> Specify path/filename prefix for all output files</p>
<dt><code>-va</code></p>
<dd> Disable all errors and warnings (summary only)</p>
<dt><code>-vi</code></p>
<dd> Less verbose errors and warnings for use with IDEs</p>
<dt><code>-vo</code></p>
<dd> Enable optimization comments</p>
<dt><code>-vr</code></p>
<dd> Disable remarks</p>
<dt><code>-vs</code></p>
<dd> Disable signon</p>
<dt><code>-w{1|2|3}</code></p>
<dd> Set warning reporting level</p>
<dt><code>-we</code></p>
<dd> Report warnings as errors </p>
</dl>
<h3>AML and Data Output Files</h3>
<dl>
<dt><code>-s{a|c}</code></p>
<dd> Create assembler or C source file (*.asm or *.c)</p>
<dt><code>-i{a|c}</code></p>
<dd> Create assembler or C include file (*.inc or *.h)</p>
<dt><code>-t{a|c|s}</code></p>
<dd> Create assembler, C, or ASL hex table (*.hex) </p>
</dl>
<h3>AML Code Generation</h3>
<dl>
<dt><code>-oa</code></p>
<dd> Disable all optimizations (compatibility mode)</p>
<dt><code>-of</code></p>
<dd> Disable constant folding</p>
<dt><code>-oi</code></p>
<dd> Disable integer optimization to Zero/One/Ones</p>
<dt><code>-on</code></p>
<dd> Disable named reference string optimization</p>
<dt><code>-cr</code></p>
<dd> Disable Resource Descriptor error checking</p>
<dt><code>-in</code></p>
<dd> Ignore NoOp operators</p>
<dt><code>-r &lt;revision&gt;</code></p>
<dd> Override table header Revision (1-255) </p>
</dl>
<h3>ASL Listing Files</h3>
<dl>
<dt><code>-l</code></p>
<dd> Create mixed listing file (ASL source and AML) (*.lst)</p>
<dt><code>-ln</code></p>
<dd> Create namespace file (*.nsp)</p>
<dt><code>-ls</code></p>
<dd> Create combined source file (expanded includes) (*.src) </p>
</dl>
<h3>ACPI Data Tables</h3>
<dl>
<dt><code>-G</code></p>
<dd> Compile custom table containing generic operators</p>
<dt><code>-vt</code></p>
<dd> Create verbose templates (full disassembly) </p>
</dl>
<h3>AML Disassembler</h3>
<dl>
<dt><code>-d [&lt;file&gt;]</code></p>
<dd> Disassemble AML to ASL source code file (*.dsl)</p>
<dt><code>-da [&lt;file1&gt;,&lt;file2&gt;]</code></p>
<dd> Disassemble multiple tables from single namespace</p>
<dt><code>-db</code></p>
<dd> Do not translate Buffers to Resource Templates</p>
<dt><code>-dc [&lt;file&gt;]</code></p>
<dd> Disassemble AML and immediately compile it<br />
 (Obtain DSDT from current system if no input file)</p>
<dt><code>-e [&lt;file1&gt;,&lt;file2&gt;]</code></p>
<dd> Include ACPI table(s) for external symbol resolution</p>
<dt><code>-g</code></p>
<dd> Get ACPI tables and write to files (*.dat)</p>
<dt><code>-in</code></p>
<dd> Ignore NoOp opcodes</p>
<dt><code>-vt</code></p>
<dd> Dump binary table date in hex format within output file </p>
</dl>
<h3>Help</h3>
<dl>
<dt><code>-h</code></p>
<dd> Additional help and compiler debug options</p>
<dt><code>-hc</code></p>
<dd> Display operators allowed in constant expressions</p>
<dt><code>-hf</code></p>
<dd> Display help for output file name generation</p>
<dt><code>-hr</code></p>
<dd> Display ACPI reserved method names</p>
<dt><code>-ht</code></p>
<dd> Display currently supported ACPI table names </p>
</dl>
<h3>Debug</h3>
<dl>
<dt><code>-b{f|t}</code></p>
<dd> Create debug file (full or parse tree only) (*.txt)</p>
<dt><code>-f</code></p>
<dd> Ignore errors, force creation of AML output file(s)</p>
<dt><code>-n</code></p>
<dd> Parse only, no output generation</p>
<dt><code>-ot</code></p>
<dd> Display compiles times and statistics</p>
<dt><code>-x &lt;level&gt;</code></p>
<dd> Set debug level for trace output</p>
<dt><code>-z</code></p>
<dd> Do not insert new compiler ID for DataTables </p>
</dl>
<h2>AUTHOR</h2>
<p> iasl was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Mattia Dongili &lt;malattia [at] debian.org&gt;, for the Debian project (but may be used by others). It was updated for the Fedora project by Al Stone &lt;ahs3 [at] redhat.com&gt; (and may also be used by others). </p>
<h2>Index</h2>
