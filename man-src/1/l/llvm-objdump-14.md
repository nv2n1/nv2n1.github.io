---
title: "llvm-objdump-14(1)"
name: "llvm-objdump-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-objdump-14/"
description: "llvm-objdump – manual page for llvm-objdump 14"
---

<h2 class="name">NAME</h2>
<p> llvm-objdump &#8211; manual page for llvm-objdump 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm object file dumper </p>
<p> USAGE: llvm-objdump [options] &lt;input object files&gt;</p>
<h3>OPTIONS:</h3>
<dl>
<dt><code>&#8211;adjust-vma</code>=<i>,offset/</i></p>
<dd> Increase the displayed address by the specified offset</p>
<dt><code>&#8211;all-headers</code></p>
<dd> Display all available header information, relocation entries and the symbol table</p>
<dt><code>&#8211;arch-name=</code>&lt;value&gt;</p>
<dd> Target arch to disassemble for, see <code>&#8211;version</code> for available targets</p>
<dt><code>&#8211;archive-headers</code></p>
<dd> Display archive header information</p>
<dt><code>-a</code></p>
<dd> Alias for <code>&#8211;archive-headers</code></p>
<dt><code>-C</code></p>
<dd> Alias for <code>&#8211;demangle</code></p>
<dt><code>&#8211;debug-vars-indent=</code>&lt;value&gt;</p>
<dd> Distance to indent the source-level variable display, relative to the start of the disassembly</p>
<dt><code>&#8211;debug-vars=</code>&lt;value&gt;</p>
<dd> Print the locations (in registers or memory) of source-level variables alongside disassembly. Supported formats: ascii, unicode (default)</p>
<dt><code>&#8211;demangle</code></p>
<dd> Demangle symbol names</p>
<dt><code>&#8211;disassemble-all</code></p>
<dd> Disassemble all sections found in the input files</p>
<dt><code>&#8211;disassemble-symbols=</code>&lt;value&gt;</p>
<dd> List of symbols to disassemble. Accept demangled names when <code>&#8211;demangle</code> is specified, otherwise accept mangled names</p>
<dt><code>&#8211;disassemble-zeroes</code></p>
<dd> Do not skip blocks of zeroes when disassembling</p>
<dt><code>&#8211;disassembler-options</code>=<i>,options/</i></p>
<dd> Pass target specific disassembler options</p>
<dt><code>&#8211;disassemble</code></p>
<dd> Disassemble all executable sections found in the input files</p>
<dt><code>&#8211;dwarf=</code>&lt;value&gt;</p>
<dd> Dump the specified DWARF debug sections. The only supported value is &#8216;frames&#8217;</p>
<dt><code>&#8211;dynamic-reloc</code></p>
<dd> Display the dynamic relocation entries in the file</p>
<dt><code>&#8211;dynamic-syms</code></p>
<dd> Display the contents of the dynamic symbol table</p>
<dt><code>-D</code></p>
<dd> Alias for <code>&#8211;disassemble-all</code></p>
<dt><code>-d</code></p>
<dd> Alias for <code>&#8211;disassemble</code></p>
<dt><code>&#8211;fault-map-section</code></p>
<dd> Display the content of the fault map section</p>
<dt><code>&#8211;file-headers</code></p>
<dd> Display the contents of the overall file header</p>
<dt><code>&#8211;full-contents</code></p>
<dd> Display the content of each section</p>
<dt><code>-f</code></p>
<dd> Alias for <code>&#8211;file-headers</code></p>
<dt><code>&#8211;headers</code></p>
<dd> Alias for <code>&#8211;section-headers</code></p>
<dt><code>&#8211;help</code></p>
<dd> Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt><code>-h</code></p>
<dd> Alias for <code>&#8211;section-headers</code></p>
<dt><code>-j</code> &lt;value&gt;</p>
<dd> Alias for <code>&#8211;section</code></p>
<dt><code>&#8211;line-numbers</code></p>
<dd> When disassembling, display source line numbers. Implies <code>&#8211;disassemble</code></p>
<dt><code>-l</code></p>
<dd> Alias for <code>&#8211;line-numbers</code></p>
<dt><code>&#8211;macho</code></p>
<dd> Use MachO specific object file parser</p>
<dt><code>&#8211;mattr</code>=<i>,a1/</i>,+a2,-a3,&#8230;</p>
<dd> Target specific attributes (<code>&#8211;mattr</code>=<i>,help/</i> for details)</p>
<dt><code>&#8211;mcpu</code>=<i>,cpu-name/</i></p>
<dd> Target a specific cpu type (<code>&#8211;mcpu</code>=<i>,help/</i> for details)</p>
<dt><code>-M</code> &lt;value&gt;</p>
<dd> Alias for <code>&#8211;disassembler-options=</code></p>
<dt><code>-m</code></p>
<dd> Alias for <code>&#8211;macho</code></p>
<dt><code>&#8211;no-leading-addr</code></p>
<dd> When disassembling, do not print leading addresses</p>
<dt><code>&#8211;no-print-imm-hex</code></p>
<dd> Do not use hex format for immediate values (default)</p>
<dt><code>&#8211;no-show-raw-insn</code></p>
<dd> When disassembling instructions, do not print the instruction bytes.</p>
<dt><code>&#8211;prefix-strip</code>=<i>,prefix/</i></p>
<dd> Strip out initial directories from absolute paths. No effect without <code>&#8211;prefix</code></p>
<dt><code>&#8211;prefix</code>=<i>,prefix/</i></p>
<dd> Add prefix to absolute paths</p>
<dt><code>&#8211;print-imm-hex</code></p>
<dd> Use hex format for immediate values</p>
<dt><code>&#8211;private-headers</code></p>
<dd> Display format specific file headers</p>
<dt><code>-p</code></p>
<dd> Alias for <code>&#8211;private-headers</code></p>
<dt><code>&#8211;raw-clang-ast</code></p>
<dd> Dump the raw binary contents of the clang AST section</p>
<dt><code>&#8211;reloc</code></p>
<dd> Display the relocation entries in the file</p>
<dt><code>-R</code></p>
<dd> Alias for <code>&#8211;dynamic-reloc</code></p>
<dt><code>-r</code></p>
<dd> Alias for <code>&#8211;reloc</code></p>
<dt><code>&#8211;section-headers</code></p>
<dd> Display summaries of the headers for each section.</p>
<dt><code>&#8211;section=</code>&lt;value&gt;</p>
<dd> Operate on the specified sections only. With <code>&#8211;macho</code> dump segment,section</p>
<dt><code>&#8211;show-lma</code></p>
<dd> Display LMA column when dumping ELF section headers</p>
<dt><code>&#8211;source</code></p>
<dd> When disassembling, display source interleaved with the disassembly. Implies <code>&#8211;disassemble</code></p>
<dt> <code>&#8211;start-address</code>=<i>,address/</i> Set the start address for disassembling, printing relocations and printing symbols</p>
<dt><code>&#8211;stop-address</code>=<i>,address/</i></p>
<dd>
<dd>Set the stop address for disassembling, printing relocations and printing symbols</p>
<dt><code>&#8211;symbol-description</code></p>
<dd> Add symbol description for disassembly. This option is for XCOFF files only.</p>
<dt><code>&#8211;symbolize-operands</code></p>
<dd> Symbolize instruction operands when disassembling</p>
<dt><code>&#8211;syms</code></p>
<dd> Display the symbol table</p>
<dt><code>-S</code></p>
<dd> Alias for <code>&#8211;source</code></p>
<dt><code>-s</code></p>
<dd> Alias for <code>&#8211;full-contents</code></p>
<dt><code>&#8211;triple=</code>&lt;value&gt;</p>
<dd> Target triple to disassemble for, see <code>&#8211;version</code> for available targets</p>
<dt><code>-T</code></p>
<dd> Alias for <code>&#8211;dynamic-syms</code></p>
<dt><code>-t</code></p>
<dd> Alias for <code>&#8211;syms</code></p>
<dt><code>&#8211;unwind-info</code></p>
<dd> Display unwind information</p>
<dt><code>-u</code></p>
<dd> Alias for <code>&#8211;unwind-info</code></p>
<dt><code>&#8211;version</code></p>
<dd> Display the version of this program</p>
<dt><code>-v</code></p>
<dd> Alias for <code>&#8211;version</code></p>
<dt><code>&#8211;wide</code></p>
<dd> Ignored for compatibility with GNU objdump</p>
<dt><code>&#8211;x86-asm-syntax</code>=<i>,att/</i></p>
<dd> Emit AT&amp;T-style disassembly</p>
<dt><code>&#8211;x86-asm-syntax</code>=<i>,intel/</i></p>
<dd> Emit Intel-style disassembly</p>
<dt><code>-x</code></p>
<dd> Alias for <code>&#8211;all-headers</code></p>
<dt><code>-z</code></p>
<dd> Alias for <code>&#8211;disassemble-zeroes</code></dl>
<h3>llvm-objdump MachO Specific Options:</h3>
<dl>
<dt><code>&#8211;arch=</code>&lt;value&gt;</p>
<dd> architecture(s) from a Mach-O file to dump</p>
<dt><code>&#8211;archive-member-offsets</code></p>
<dd> Print the offset to each archive member for Mach-O archives (requires <code>&#8211;macho</code> and <code>&#8211;archive-headers</code>)</p>
<dt><code>&#8211;bind</code></p>
<dd> Display mach-o binding info</p>
<dt><code>&#8211;data-in-code</code></p>
<dd> Print the data in code table for Mach-O objects (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;dis-symname</code> &lt;value&gt;</p>
<dd> disassemble just this symbol&#8217;s instructions (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;dsym=</code>&lt;value&gt;</p>
<dd> Use .dSYM file for debug info</p>
<dt><code>&#8211;dylib-id</code></p>
<dd> Print the shared library&#8217;s id for the dylib Mach-O file (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;dylibs-used</code></p>
<dd> Print the shared libraries used for linked Mach-O files (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;exports-trie</code></p>
<dd> Display mach-o exported symbols</p>
<dt><code>&#8211;full-leading-addr</code></p>
<dd> Print full leading address</p>
<dt><code>&#8211;function-starts</code></p>
<dd> Print the function starts table for Mach-O objects (requires <code>&#8211;macho</code>)</p>
<dt><code>-g</code></p>
<dd> Print line information from debug info if available</p>
<dt><code>&#8211;indirect-symbols</code></p>
<dd> Print indirect symbol table for Mach-O objects (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;info-plist</code></p>
<dd> Print the info plist section as strings for Mach-O objects (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;lazy-bind</code></p>
<dd> Display mach-o lazy binding info</p>
<dt><code>&#8211;link-opt-hints</code></p>
<dd> Print the linker optimization hints for Mach-O objects (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;no-leading-headers</code></p>
<dd> Print no leading headers</p>
<dt> <code>&#8211;no-symbolic-operands</code> do not symbolic operands when disassembling (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;non-verbose</code></p>
<dd>
<dd>Print the info for Mach-O objects in non-verbose or numeric form (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;objc-meta-data</code></p>
<dd> Print the Objective-C runtime meta data for Mach-O files (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;private-header</code></p>
<dd> Display only the first format specific file header</p>
<dt><code>&#8211;rebase</code></p>
<dd> Display mach-o rebasing info</p>
<dt><code>&#8211;rpaths</code></p>
<dd> Print the runtime search paths for the Mach-O file (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;universal-headers</code></p>
<dd> Print Mach-O universal headers (requires <code>&#8211;macho</code>)</p>
<dt><code>&#8211;weak-bind</code></p>
<dd> Display mach-o weak binding info</dl>
<p> Pass @FILE as argument to read options from FILE. </p>
<h2>Index</h2>
