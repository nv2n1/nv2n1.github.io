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
<dt><code>-@ &lt;file&gt;</code></dt>
<dd> Specify command file</dd>
<dt><code>-I &lt;dir&gt;</code></dt>
<dd> Specify additional include directory</dd>
<dt><code>-T &lt;sig&gt;|ALL|*</code></dt>
<dd> Create table template file for ACPI &lt;sig&gt;</dd>
<dt><code>-v</code></dt>
<dd> Display compiler version </dd>
</dl>
<h3>Preprocessor</h3>
<dl>
<dt><code>-D &lt;symbol&gt;</code></dt>
<dd> Define sybol for preprocessor use</dd>
<dt><code>-li</code></dt>
<dd> Create prepocessed output file (*.i)</dd>
<dt><code>-P</code></dt>
<dd> Preprocess only and create preprocessor output file (*.i)</dd>
<dt><code>-Pn</code></dt>
<dd> Disable preprocessor </dd>
</dl>
<h3>General Output</h3>
<dl>
<dt><code>-p &lt;prefix&gt;</code></dt>
<dd> Specify path/filename prefix for all output files</dd>
<dt><code>-va</code></dt>
<dd> Disable all errors and warnings (summary only)</dd>
<dt><code>-vi</code></dt>
<dd> Less verbose errors and warnings for use with IDEs</dd>
<dt><code>-vo</code></dt>
<dd> Enable optimization comments</dd>
<dt><code>-vr</code></dt>
<dd> Disable remarks</dd>
<dt><code>-vs</code></dt>
<dd> Disable signon</dd>
<dt><code>-w{1|2|3}</code></dt>
<dd> Set warning reporting level</dd>
<dt><code>-we</code></dt>
<dd> Report warnings as errors </dd>
</dl>
<h3>AML and Data Output Files</h3>
<dl>
<dt><code>-s{a|c}</code></dt>
<dd> Create assembler or C source file (*.asm or *.c)</dd>
<dt><code>-i{a|c}</code></dt>
<dd> Create assembler or C include file (*.inc or *.h)</dd>
<dt><code>-t{a|c|s}</code></dt>
<dd> Create assembler, C, or ASL hex table (*.hex) </dd>
</dl>
<h3>AML Code Generation</h3>
<dl>
<dt><code>-oa</code></dt>
<dd> Disable all optimizations (compatibility mode)</dd>
<dt><code>-of</code></dt>
<dd> Disable constant folding</dd>
<dt><code>-oi</code></dt>
<dd> Disable integer optimization to Zero/One/Ones</dd>
<dt><code>-on</code></dt>
<dd> Disable named reference string optimization</dd>
<dt><code>-cr</code></dt>
<dd> Disable Resource Descriptor error checking</dd>
<dt><code>-in</code></dt>
<dd> Ignore NoOp operators</dd>
<dt><code>-r &lt;revision&gt;</code></dt>
<dd> Override table header Revision (1-255) </dd>
</dl>
<h3>ASL Listing Files</h3>
<dl>
<dt><code>-l</code></dt>
<dd> Create mixed listing file (ASL source and AML) (*.lst)</dd>
<dt><code>-ln</code></dt>
<dd> Create namespace file (*.nsp)</dd>
<dt><code>-ls</code></dt>
<dd> Create combined source file (expanded includes) (*.src) </dd>
</dl>
<h3>ACPI Data Tables</h3>
<dl>
<dt><code>-G</code></dt>
<dd> Compile custom table containing generic operators</dd>
<dt><code>-vt</code></dt>
<dd> Create verbose templates (full disassembly) </dd>
</dl>
<h3>AML Disassembler</h3>
<dl>
<dt><code>-d [&lt;file&gt;]</code></dt>
<dd> Disassemble AML to ASL source code file (*.dsl)</dd>
<dt><code>-da [&lt;file1&gt;,&lt;file2&gt;]</code></dt>
<dd> Disassemble multiple tables from single namespace</dd>
<dt><code>-db</code></dt>
<dd> Do not translate Buffers to Resource Templates</dd>
<dt><code>-dc [&lt;file&gt;]</code></dt>
<dd> Disassemble AML and immediately compile it<br />
 (Obtain DSDT from current system if no input file)</dd>
<dt><code>-e [&lt;file1&gt;,&lt;file2&gt;]</code></dt>
<dd> Include ACPI table(s) for external symbol resolution</dd>
<dt><code>-g</code></dt>
<dd> Get ACPI tables and write to files (*.dat)</dd>
<dt><code>-in</code></dt>
<dd> Ignore NoOp opcodes</dd>
<dt><code>-vt</code></dt>
<dd> Dump binary table date in hex format within output file </dd>
</dl>
<h3>Help</h3>
<dl>
<dt><code>-h</code></dt>
<dd> Additional help and compiler debug options</dd>
<dt><code>-hc</code></dt>
<dd> Display operators allowed in constant expressions</dd>
<dt><code>-hf</code></dt>
<dd> Display help for output file name generation</dd>
<dt><code>-hr</code></dt>
<dd> Display ACPI reserved method names</dd>
<dt><code>-ht</code></dt>
<dd> Display currently supported ACPI table names </dd>
</dl>
<h3>Debug</h3>
<dl>
<dt><code>-b{f|t}</code></dt>
<dd> Create debug file (full or parse tree only) (*.txt)</dd>
<dt><code>-f</code></dt>
<dd> Ignore errors, force creation of AML output file(s)</dd>
<dt><code>-n</code></dt>
<dd> Parse only, no output generation</dd>
<dt><code>-ot</code></dt>
<dd> Display compiles times and statistics</dd>
<dt><code>-x &lt;level&gt;</code></dt>
<dd> Set debug level for trace output</dd>
<dt><code>-z</code></dt>
<dd> Do not insert new compiler ID for DataTables </dd>
</dl>
<h2>AUTHOR</h2>
<p> iasl was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Mattia Dongili &lt;malattia [at] debian.org&gt;, for the Debian project (but may be used by others). It was updated for the Fedora project by Al Stone &lt;ahs3 [at] redhat.com&gt; (and may also be used by others). </p>
<h2>Index</h2>
