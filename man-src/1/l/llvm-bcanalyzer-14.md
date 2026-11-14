---
title: "llvm-bcanalyzer-14(1)"
name: "llvm-bcanalyzer-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-bcanalyzer-14/"
description: "llvm-bcanalyzer – LLVM bitcode analyzer"
---

<h2 class="name">NAME</h2>
<p> llvm-bcanalyzer &#8211; LLVM bitcode analyzer </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-bcanalyzer</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-bcanalyzer</code> command is a small utility for analyzing bitcode files. The tool reads a bitcode file (such as generated with the <code>llvm-as</code> tool) and produces a statistical report on the contents of the bitcode file. The tool can also dump a low level but human readable version of the bitcode file. This tool is probably not of much interest or utility except for those working directly with the bitcode file format. Most LLVM users can just ignore this tool. </p>
<p> If <i>filename</i> is omitted or is <code>&#8211;</code>, then <code>llvm-bcanalyzer</code> reads its input from standard input. This is useful for combining the tool into a pipeline. Output is written to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-nodetails</code></p>
<dd> Causes <code>llvm-bcanalyzer</code> to abbreviate its output by writing out only a module level summary. The details for individual functions are not displayed.</p>
<dt><code>-dump</code></p>
<dd> Causes <code>llvm-bcanalyzer</code> to dump the bitcode in a human readable format. This format is significantly different from LLVM assembly and provides details about the encoding of the bitcode file.</p>
<dt><code>-verify</code></p>
<dd> Causes <code>llvm-bcanalyzer</code> to verify the module produced by reading the bitcode. This ensures that the statistics generated are based on a consistent module.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-bcanalyzer</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value, usually 1.</p>
<h2>SUMMARY OUTPUT DEFINITIONS</h2>
<p> The following items are always printed by llvm-bcanalyzer. They comprize the summary output. </p>
<p> <code>Bitcode Analysis Of Module</code> This just provides the name of the module for which bitcode analysis is being generated. </p>
<p> <code>Bitcode Version Number</code> The bitcode version (not LLVM version) of the file read by the analyzer. </p>
<p> <code>File Size</code> The size, in bytes, of the entire bitcode file. </p>
<p> <code>Module Bytes</code> The size, in bytes, of the module block. Percentage is relative to File Size. </p>
<p> <code>Function Bytes</code> The size, in bytes, of all the function blocks. Percentage is relative to File Size. </p>
<p> <code>Global Types Bytes</code> The size, in bytes, of the Global Types Pool. Percentage is relative to File Size. This is the size of the definitions of all types in the bitcode file. </p>
<p> <code>Constant Pool Bytes</code> The size, in bytes, of the Constant Pool Blocks Percentage is relative to File Size. </p>
<p> <code>Module Globals Bytes</code> Ths size, in bytes, of the Global Variable Definitions and their initializers. Percentage is relative to File Size. </p>
<p> <code>Instruction List Bytes</code> The size, in bytes, of all the instruction lists in all the functions. Percentage is relative to File Size. Note that this value is also included in the Function Bytes. </p>
<p> <code>Compaction Table Bytes</code> The size, in bytes, of all the compaction tables in all the functions. Percentage is relative to File Size. Note that this value is also included in the Function Bytes. </p>
<p> <code>Symbol Table Bytes</code> The size, in bytes, of all the symbol tables in all the functions. Percentage is relative to File Size. Note that this value is also included in the Function Bytes. </p>
<p> <code>Dependent Libraries Bytes</code> The size, in bytes, of the list of dependent libraries in the module. Percentage is relative to File Size. Note that this value is also included in the Module Global Bytes. </p>
<p> <code>Number Of Bitcode Blocks</code> The total number of blocks of any kind in the bitcode file. </p>
<p> <code>Number Of Functions</code> The total number of function definitions in the bitcode file. </p>
<p> <code>Number Of Types</code> The total number of types defined in the Global Types Pool. </p>
<p> <code>Number Of Constants</code> The total number of constants (of any type) defined in the Constant Pool. </p>
<p> <code>Number Of Basic Blocks</code> The total number of basic blocks defined in all functions in the bitcode file. </p>
<p> <code>Number Of Instructions</code> The total number of instructions defined in all functions in the bitcode file. </p>
<p> <code>Number Of Long Instructions</code> The total number of long instructions defined in all functions in the bitcode file. Long instructions are those taking greater than 4 bytes. Typically long instructions are GetElementPtr with several indices, PHI nodes, and calls to functions with large numbers of arguments. </p>
<p> <code>Number Of Operands</code> The total number of operands used in all instructions in the bitcode file. </p>
<p> <code>Number Of Compaction Tables</code> The total number of compaction tables in all functions in the bitcode file. </p>
<p> <code>Number Of Symbol Tables</code> The total number of symbol tables in all functions in the bitcode file. </p>
<p> <code>Number Of Dependent Libs</code> The total number of dependent libraries found in the bitcode file. </p>
<p> <code>Total Instruction Size</code> The total size of the instructions in all functions in the bitcode file. </p>
<p> <code>Average Instruction Size</code> The average number of bytes per instruction across all functions in the bitcode file. This value is computed by dividing Total Instruction Size by Number Of Instructions. </p>
<p> <code>Maximum Type Slot Number</code> The maximum value used for a type’s slot number. Larger slot number values take more bytes to encode. </p>
<p> <code>Maximum Value Slot Number</code> The maximum value used for a value’s slot number. Larger slot number values take more bytes to encode. </p>
<p> <code>Bytes Per Value</code> The average size of a Value definition (of any type). This is computed by dividing File Size by the total number of values of any type. </p>
<p> <code>Bytes Per Global</code> The average size of a global definition (constants and global variables). </p>
<p> <code>Bytes Per Function</code> The average number of bytes per function definition. This is computed by dividing Function Bytes by Number Of Functions. </p>
<p> <code># of VBR 32-bit Integers</code> The total number of 32-bit integers encoded using the Variable Bit Rate encoding scheme. </p>
<p> <code># of VBR 64-bit Integers</code> The total number of 64-bit integers encoded using the Variable Bit Rate encoding scheme. </p>
<p> <code># of VBR Compressed Bytes</code> The total number of bytes consumed by the 32-bit and 64-bit integers that use the Variable Bit Rate encoding scheme. </p>
<p> <code># of VBR Expanded Bytes</code> The total number of bytes that would have been consumed by the 32-bit and 64-bit integers had they not been compressed with the Variable Bit Rage encoding scheme. </p>
<p> <code>Bytes Saved With VBR</code> The total number of bytes saved by using the Variable Bit Rate encoding scheme. The percentage is relative to # of VBR Expanded Bytes.</p>
<h2>DETAILED OUTPUT DEFINITIONS</h2>
<p> The following definitions occur only if the -nodetails option was not given. The detailed output provides additional information on a per-function basis. </p>
<p> <code>Type</code> The type signature of the function. </p>
<p> <code>Byte Size</code> The total number of bytes in the function’s block. </p>
<p> <code>Basic Blocks</code> The number of basic blocks defined by the function. </p>
<p> <code>Instructions</code> The number of instructions defined by the function. </p>
<p> <code>Long Instructions</code> The number of instructions using the long instruction format in the function. </p>
<p> <code>Operands</code> The number of operands used by all instructions in the function. </p>
<p> <code>Instruction Size</code> The number of bytes consumed by instructions in the function. </p>
<p> <code>Average Instruction Size</code> The average number of bytes consumed by the instructions in the function. This value is computed by dividing Instruction Size by Instructions. </p>
<p> <code>Bytes Per Instruction</code> The average number of bytes used by the function per instruction. This value is computed by dividing Byte Size by Instructions. Note that this is not the same as Average Instruction Size. It computes a number relative to the total function size not just the size of the instruction list. </p>
<p> <code>Number of VBR 32-bit Integers</code> The total number of 32-bit integers found in this function (for any use). </p>
<p> <code>Number of VBR 64-bit Integers</code> The total number of 64-bit integers found in this function (for any use). </p>
<p> <code>Number of VBR Compressed Bytes</code> The total number of bytes in this function consumed by the 32-bit and 64-bit integers that use the Variable Bit Rate encoding scheme. </p>
<p> <code>Number of VBR Expanded Bytes</code> The total number of bytes in this function that would have been consumed by the 32-bit and 64-bit integers had they not been compressed with the Variable Bit Rate encoding scheme. </p>
<p> <code>Bytes Saved With VBR</code> The total number of bytes saved in this function by using the Variable Bit Rate encoding scheme. The percentage is relative to # of VBR Expanded Bytes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-dis/">llvm-dis</a>(1)</code>, /BitCodeFormat</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
