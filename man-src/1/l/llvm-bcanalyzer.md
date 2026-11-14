---
title: "llvm-bcanalyzer(1)"
name: "llvm-bcanalyzer"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-bcanalyzer/"
description: "llvm-bcanalyzer – LLVM bitcode analyzer"
---

<h2 class="name">NAME</h2>
<p> llvm-bcanalyzer &#8211; LLVM bitcode analyzer </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-bcanalyzer</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-bcanalyzer</code> command is a small utility for analyzing bitcode files. The tool reads a bitcode file (such as generated with the <code>llvm-as</code> tool) and produces a statistical report on the contents of the bitcode file. The tool can also dump a low level but human readable version of the bitcode file. This tool is probably not of much interest or utility except for those working directly with the bitcode file format. Most <font SIZE="-1">LLVM</font> users can just ignore this tool. </p>
<p> If <i>filename</i> is omitted or is <tt>&quot;-&quot;</tt>, then <code>llvm-bcanalyzer</code> reads its input from standard input. This is useful for combining the tool into a pipeline. Output is written to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-nodetails</code></p>
<dd> Causes <code>llvm-bcanalyzer</code> to abbreviate its output by writing out only a module level summary. The details for individual functions are not displayed.</p>
<dt><code>-dump</code></p>
<dd> Causes <code>llvm-bcanalyzer</code> to dump the bitcode in a human readable format. This format is significantly different from <font SIZE="-1">LLVM</font> assembly and provides details about the encoding of the bitcode file.</p>
<dt><code>-verify</code></p>
<dd> Causes <code>llvm-bcanalyzer</code> to verify the module produced by reading the bitcode. This ensures that the statistics generated are based on a consistent module.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-bcanalyzer</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value, usually 1.</p>
<h2>SUMMARY OUTPUT DEFINITIONS</h2>
<p> The following items are always printed by llvm-bcanalyzer. They comprize the summary output.</p>
<dl>
<dt><code>Bitcode Analysis Of Module</code></p>
<dd> This just provides the name of the module for which bitcode analysis is being generated.</p>
<dt><code>Bitcode Version Number</code></p>
<dd> The bitcode version (not <font SIZE="-1">LLVM</font> version) of the file read by the analyzer.</p>
<dt><code>File Size</code></p>
<dd> The size, in bytes, of the entire bitcode file.</p>
<dt><code>Module Bytes</code></p>
<dd> The size, in bytes, of the module block. Percentage is relative to File Size.</p>
<dt><code>Function Bytes</code></p>
<dd> The size, in bytes, of all the function blocks. Percentage is relative to File Size.</p>
<dt><code>Global Types Bytes</code></p>
<dd> The size, in bytes, of the Global Types Pool. Percentage is relative to File Size. This is the size of the definitions of all types in the bitcode file.</p>
<dt><code>Constant Pool Bytes</code></p>
<dd> The size, in bytes, of the Constant Pool Blocks Percentage is relative to File Size.</p>
<dt><code>Module Globals Bytes</code></p>
<dd> Ths size, in bytes, of the Global Variable Definitions and their initializers. Percentage is relative to File Size.</p>
<dt><code>Instruction List Bytes</code></p>
<dd> The size, in bytes, of all the instruction lists in all the functions. Percentage is relative to File Size. Note that this value is also included in the Function Bytes.</p>
<dt><code>Compaction Table Bytes</code></p>
<dd> The size, in bytes, of all the compaction tables in all the functions. Percentage is relative to File Size. Note that this value is also included in the Function Bytes.</p>
<dt><code>Symbol Table Bytes</code></p>
<dd> The size, in bytes, of all the symbol tables in all the functions. Percentage is relative to File Size. Note that this value is also included in the Function Bytes.</p>
<dt><code>Dependent Libraries Bytes</code></p>
<dd> The size, in bytes, of the list of dependent libraries in the module. Percentage is relative to File Size. Note that this value is also included in the Module Global Bytes.</p>
<dt><code>Number Of Bitcode Blocks</code></p>
<dd> The total number of blocks of any kind in the bitcode file.</p>
<dt><code>Number Of Functions</code></p>
<dd> The total number of function definitions in the bitcode file.</p>
<dt><code>Number Of Types</code></p>
<dd> The total number of types defined in the Global Types Pool.</p>
<dt><code>Number Of Constants</code></p>
<dd> The total number of constants (of any type) defined in the Constant Pool.</p>
<dt><code>Number Of Basic Blocks</code></p>
<dd> The total number of basic blocks defined in all functions in the bitcode file.</p>
<dt><code>Number Of Instructions</code></p>
<dd> The total number of instructions defined in all functions in the bitcode file.</p>
<dt><code>Number Of Long Instructions</code></p>
<dd> The total number of long instructions defined in all functions in the bitcode file. Long instructions are those taking greater than 4 bytes. Typically long instructions are GetElementPtr with several indices, <font SIZE="-1">PHI</font> nodes, and calls to functions with large numbers of arguments.</p>
<dt><code>Number Of Operands</code></p>
<dd> The total number of operands used in all instructions in the bitcode file.</p>
<dt><code>Number Of Compaction Tables</code></p>
<dd> The total number of compaction tables in all functions in the bitcode file.</p>
<dt><code>Number Of Symbol Tables</code></p>
<dd> The total number of symbol tables in all functions in the bitcode file.</p>
<dt><code>Number Of Dependent Libs</code></p>
<dd> The total number of dependent libraries found in the bitcode file.</p>
<dt><code>Total Instruction Size</code></p>
<dd> The total size of the instructions in all functions in the bitcode file.</p>
<dt><code>Average Instruction Size</code></p>
<dd> The average number of bytes per instruction across all functions in the bitcode file. This value is computed by dividing Total Instruction Size by Number Of Instructions.</p>
<dt><code>Maximum Type Slot Number</code></p>
<dd> The maximum value used for a type&#8217;s slot number. Larger slot number values take more bytes to encode.</p>
<dt><code>Maximum Value Slot Number</code></p>
<dd> The maximum value used for a value&#8217;s slot number. Larger slot number values take more bytes to encode.</p>
<dt><code>Bytes Per Value</code></p>
<dd> The average size of a Value definition (of any type). This is computed by dividing File Size by the total number of values of any type.</p>
<dt><code>Bytes Per Global</code></p>
<dd> The average size of a global definition (constants and global variables).</p>
<dt><code>Bytes Per Function</code></p>
<dd> The average number of bytes per function definition. This is computed by dividing Function Bytes by Number Of Functions.</p>
<dt><code># of </code><font SIZE="-1"><code>VBR</code></font><code> 32-bit Integers</code></p>
<dd> The total number of 32-bit integers encoded using the Variable Bit Rate encoding scheme.</p>
<dt><code># of </code><font SIZE="-1"><code>VBR</code></font><code> 64-bit Integers</code></p>
<dd> The total number of 64-bit integers encoded using the Variable Bit Rate encoding scheme.</p>
<dt><code># of </code><font SIZE="-1"><code>VBR</code></font><code> Compressed Bytes</code></p>
<dd> The total number of bytes consumed by the 32-bit and 64-bit integers that use the Variable Bit Rate encoding scheme.</p>
<dt><code># of </code><font SIZE="-1"><code>VBR</code></font><code> Expanded Bytes</code></p>
<dd> The total number of bytes that would have been consumed by the 32-bit and 64-bit integers had they not been compressed with the Variable Bit Rage encoding scheme.</p>
<dt><code>Bytes Saved With </code><font SIZE="-1"><code>VBR</code></font></p>
<dd> The total number of bytes saved by using the Variable Bit Rate encoding scheme. The percentage is relative to # of <font SIZE="-1">VBR</font> Expanded Bytes.</dl>
<h2>DETAILED OUTPUT DEFINITIONS</h2>
<p> The following definitions occur only if the -nodetails option was not given. The detailed output provides additional information on a per-function basis.</p>
<dl>
<dt><code>Type</code></p>
<dd> The type signature of the function.</p>
<dt><code>Byte Size</code></p>
<dd> The total number of bytes in the function&#8217;s block.</p>
<dt><code>Basic Blocks</code></p>
<dd> The number of basic blocks defined by the function.</p>
<dt><code>Instructions</code></p>
<dd> The number of instructions defined by the function.</p>
<dt><code>Long Instructions</code></p>
<dd> The number of instructions using the long instruction format in the function.</p>
<dt><code>Operands</code></p>
<dd> The number of operands used by all instructions in the function.</p>
<dt><code>Instruction Size</code></p>
<dd> The number of bytes consumed by instructions in the function.</p>
<dt><code>Average Instruction Size</code></p>
<dd> The average number of bytes consumed by the instructions in the funtion. This value is computed by dividing Instruction Size by Instructions.</p>
<dt><code>Bytes Per Instruction</code></p>
<dd> The average number of bytes used by the function per instruction. This value is computed by dividing Byte Size by Instructions. Note that this is not the same as Average Instruction Size. It computes a number relative to the total function size not just the size of the instruction list.</p>
<dt><code>Number of </code><font SIZE="-1"><code>VBR</code></font><code> 32-bit Integers</code></p>
<dd> The total number of 32-bit integers found in this function (for any use).</p>
<dt><code>Number of </code><font SIZE="-1"><code>VBR</code></font><code> 64-bit Integers</code></p>
<dd> The total number of 64-bit integers found in this function (for any use).</p>
<dt><code>Number of </code><font SIZE="-1"><code>VBR</code></font><code> Compressed Bytes</code></p>
<dd> The total number of bytes in this function consumed by the 32-bit and 64-bit integers that use the Variable Bit Rate encoding scheme.</p>
<dt><code>Number of </code><font SIZE="-1"><code>VBR</code></font><code> Expanded Bytes</code></p>
<dd> The total number of bytes in this function that would have been consumed by the 32-bit and 64-bit integers had they not been compressed with the Variable Bit Rate encoding scheme.</p>
<dt><code>Bytes Saved With </code><font SIZE="-1"><code>VBR</code></font></p>
<dd> The total number of bytes saved in this function by using the Variable Bit Rate encoding scheme. The percentage is relative to # of <font SIZE="-1">VBR</font> Expanded Bytes.</dl>
<h2>SEE ALSO</h2>
<p> llvm-dis, &lt;<a rel="nofollow" href="http://llvm.org/docs/BitCodeFormat.html">http://llvm.org/docs/BitCodeFormat.html</a>&gt;</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
