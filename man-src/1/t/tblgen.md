---
title: "tblgen(1)"
name: "tblgen"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tblgen/"
description: "tblgen – Target Description To C++ Code Generator"
---

<h2 class="name">NAME</h2>
<p> tblgen &#8211; Target Description To C++ Code Generator </p>
<h2>SYNOPSIS</h2>
<p> <code>tblgen</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>tblgen</code> translates from target description (.td) files into C<font SIZE="-2">++</font> code that can be included in the definition of an <font SIZE="-1">LLVM</font> target library. Most users of <font SIZE="-1">LLVM</font> will not need to use this program. It is only for assisting with writing an <font SIZE="-1">LLVM</font> target backend. </p>
<p> The input and output of <code>tblgen</code> is beyond the scope of this short introduction. Please see the <i>CodeGeneration</i> page in the <font SIZE="-1">LLVM</font> documentation. </p>
<p> The <i>filename</i> argument specifies the name of a Target Description (.td) file to read as input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></dt>
<dd> Print a summary of command line options.</dd>
<dt><code>-o</code> <i>filename</i></dt>
<dd> Specify the output file name. If <i>filename</i> is <tt>&quot;-&quot;</tt>, then <code>tblgen</code> sends its output to standard output.</dd>
<dt><code>-I</code> <i>directory</i></dt>
<dd> Specify where to find other target description files for inclusion. The <i>directory</i> value should be a full or partial path to a directory that contains target description files.</dd>
<dt><code>-asmwriternum</code> <i>N</i></dt>
<dd> Make -gen-asm-writer emit assembly writer number <i>N</i>.</dd>
<dt><code>-class</code> <i>class Name</i></dt>
<dd> Print the enumeration list for this class.</dd>
<dt><code>-print-records</code></dt>
<dd> Print all records to standard output (default).</dd>
<dt><code>-print-enums</code></dt>
<dd> Print enumeration values for a class</dd>
<dt><code>-gen-emitter</code></dt>
<dd> Generate machine code emitter.</dd>
<dt><code>-gen-register-enums</code></dt>
<dd> Generate the enumeration values for all registers.</dd>
<dt><code>-gen-register-desc</code></dt>
<dd> Generate a register info description for each register.</dd>
<dt><code>-gen-register-desc-header</code></dt>
<dd> Generate a register info description header for each register.</dd>
<dt><code>-gen-instr-enums</code></dt>
<dd> Generate enumeration values for instructions.</dd>
<dt><code>-gen-instr-desc</code></dt>
<dd> Generate instruction descriptions.</dd>
<dt><code>-gen-asm-writer</code></dt>
<dd> Generate the assembly writer.</dd>
<dt><code>-gen-dag-isel</code></dt>
<dd> Generate a <font SIZE="-1">DAG</font> (Directed Acycle Graph) instruction selector.</dd>
<dt><code>-gen-subtarget</code></dt>
<dd> Generate subtarget enumerations.</dd>
<dt><code>-gen-intrinsic</code></dt>
<dd> Generate intrinsic information.</dd>
<dt><code>-version</code></dt>
<dd> Show the version number of this program.</dd></dl>
<h2>EXIT STATUS</h2>
<p> If <code>tblgen</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHORS</h2>
<p> Maintained by The <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
