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
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> Specify the output file name. If <i>filename</i> is <tt>&quot;-&quot;</tt>, then <code>tblgen</code> sends its output to standard output.</p>
<dt><code>-I</code> <i>directory</i></p>
<dd> Specify where to find other target description files for inclusion. The <i>directory</i> value should be a full or partial path to a directory that contains target description files.</p>
<dt><code>-asmwriternum</code> <i>N</i></p>
<dd> Make -gen-asm-writer emit assembly writer number <i>N</i>.</p>
<dt><code>-class</code> <i>class Name</i></p>
<dd> Print the enumeration list for this class.</p>
<dt><code>-print-records</code></p>
<dd> Print all records to standard output (default).</p>
<dt><code>-print-enums</code></p>
<dd> Print enumeration values for a class</p>
<dt><code>-gen-emitter</code></p>
<dd> Generate machine code emitter.</p>
<dt><code>-gen-register-enums</code></p>
<dd> Generate the enumeration values for all registers.</p>
<dt><code>-gen-register-desc</code></p>
<dd> Generate a register info description for each register.</p>
<dt><code>-gen-register-desc-header</code></p>
<dd> Generate a register info description header for each register.</p>
<dt><code>-gen-instr-enums</code></p>
<dd> Generate enumeration values for instructions.</p>
<dt><code>-gen-instr-desc</code></p>
<dd> Generate instruction descriptions.</p>
<dt><code>-gen-asm-writer</code></p>
<dd> Generate the assembly writer.</p>
<dt><code>-gen-dag-isel</code></p>
<dd> Generate a <font SIZE="-1">DAG</font> (Directed Acycle Graph) instruction selector.</p>
<dt><code>-gen-subtarget</code></p>
<dd> Generate subtarget enumerations.</p>
<dt><code>-gen-intrinsic</code></p>
<dd> Generate intrinsic information.</p>
<dt><code>-version</code></p>
<dd> Show the version number of this program.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>tblgen</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHORS</h2>
<p> Maintained by The <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
