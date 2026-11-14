---
title: "llvm-objdump-9(1)"
name: "llvm-objdump-9"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-objdump-9/"
description: "llvm-objdump – manual page for llvm-objdump 9"
---

<h2 class="name">NAME</h2>
<p> llvm-objdump &#8211; manual page for llvm-objdump 9 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm object file dumper </p>
<p> USAGE: llvm-objdump [options] &lt;input object files&gt; </p>
<p> OPTIONS: </p>
<p> Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dl>
<dd>llvm-objdump MachO Specific Options:</p>
<dl>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; architecture(s) from a Mach-O file to dump</p>
<dt> <code>&#8211;archive-member-offsets</code> &#8211; Print the offset to each archive member for Mach-O archives (requires <code>-macho</code> and <code>-archive-headers</code>)</p>
<dt> <code>&#8211;bind</code> &#8211; Display mach-o binding info</p>
<dt> <code>&#8211;data-in-code</code> &#8211; Print the data in code table for Mach-O objects (requires <code>-macho</code>)</p>
<dt> <code>&#8211;dis-symname=</code>&lt;string&gt; &#8211; disassemble just this symbol&#8217;s instructions (requires <code>-macho</code>)</p>
<dt> <code>&#8211;dsym=</code>&lt;string&gt; &#8211; Use .dSYM file for debug info</p>
<dt> <code>&#8211;dylib-id</code> &#8211; Print the shared library&#8217;s id for the dylib Mach-O file (requires <code>-macho</code>)</p>
<dt> <code>&#8211;dylibs-used</code> &#8211; Print the shared libraries used for linked Mach-O files (requires <code>-macho</code>)</p>
<dt> <code>&#8211;exports-trie</code> &#8211; Display mach-o exported symbols</p>
<dt> <code>&#8211;full-leading-addr</code> &#8211; Print full leading address</p>
<dt> <code>-g</code> &#8211; Print line information from debug info if available</p>
<dt> <code>&#8211;indirect-symbols</code> &#8211; Print indirect symbol table for Mach-O objects (requires <code>-macho</code>)</p>
<dt> <code>&#8211;info-plist</code> &#8211; Print the info plist section as strings for Mach-O objects (requires <code>-macho</code>)</p>
<dt> <code>&#8211;lazy-bind</code> &#8211; Display mach-o lazy binding info</p>
<dt> <code>&#8211;link-opt-hints</code> &#8211; Print the linker optimization hints for Mach-O objects (requires <code>-macho</code>)</p>
<dt> <code>&#8211;no-leading-headers</code> &#8211; Print no leading headers</p>
<dt> <code>&#8211;no-symbolic-operands</code> &#8211; do not symbolic operands when disassembling (requires <code>-macho</code>)</p>
<dt> <code>&#8211;non-verbose</code> &#8211; Print the info for Mach-O objects in non-verbose or numeric form (requires <code>-macho</code>)</p>
<dt> <code>&#8211;objc-meta-data</code> &#8211; Print the Objective-C runtime meta data for Mach-O files (requires <code>-macho</code>)</p>
<dt> <code>&#8211;private-header</code> &#8211; Display only the first format specific file header</p>
<dt> <code>&#8211;rebase</code> &#8211; Display mach-o rebasing info</p>
<dt> <code>&#8211;universal-headers</code> &#8211; Print Mach-O universal headers (requires <code>-macho</code>)</p>
<dt> <code>&#8211;weak-bind</code> &#8211; Display mach-o weak binding info</dl>
<dd>llvm-objdump Options:</p>
<dl>
<dt> <code>-C</code> &#8211; Alias for <code>&#8211;demangle</code></p>
<dt> <code>-D</code> &#8211; Alias for <code>&#8211;disassemble-all</code></p>
<dt> <code>-M</code> &#8211; Alias for <code>&#8211;disassembler-options</code></p>
<dt> <code>-R</code> &#8211; Alias for <code>&#8211;dynamic-reloc</code></p>
<dt> <code>-S</code> &#8211; Alias for <code>-source</code></p>
<dt> <code>-a</code> &#8211; Alias for <code>&#8211;archive-headers</code></p>
<dt> <code>&#8211;adjust-vma=</code>&lt;offset&gt; &#8211; Increase the displayed address by the specified offset</p>
<dt> <code>&#8211;all-headers</code> &#8211; Display all available header information</p>
<dt> <code>&#8211;arch-name=</code>&lt;string&gt; &#8211; Target arch to disassemble for, see <code>-version</code> for available targets</p>
<dt> <code>&#8211;archive-headers</code> &#8211; Display archive header information</p>
<dt> <code>-d</code> &#8211; Alias for <code>&#8211;disassemble</code></p>
<dt> <code>&#8211;demangle</code> &#8211; Demangle symbols names</p>
<dt> <code>&#8211;disassemble</code> &#8211; Display assembler mnemonics for the machine instructions</p>
<dt> <code>&#8211;disassemble-all</code> &#8211; Display assembler mnemonics for the machine instructions</p>
<dt> <code>&#8211;disassemble-functions=</code>&lt;string&gt; &#8211; List of functions to disassemble. Accept demangled names when <code>&#8211;demangle</code> is specified, otherwise accept mangled names</p>
<dt> <code>&#8211;disassemble-zeroes</code> &#8211; Do not skip blocks of zeroes when disassembling</p>
<dt> <code>&#8211;disassembler-options=</code>&lt;options&gt; &#8211; Pass target specific disassembler options</p>
<dt> <code>&#8211;dwarf=</code>&lt;value&gt; &#8211; Dump of dwarf debug sections:</p>
<dt>=frames</p>
<dd> &#8211; .debug_frame</p>
<dt> <code>&#8211;dynamic-reloc</code> &#8211; Display the dynamic relocation entries in the file</p>
<dt> <code>-f</code> &#8211; Alias for <code>&#8211;file-headers</code></p>
<dt> <code>&#8211;fault-map-section</code> &#8211; Display contents of faultmap section</p>
<dt> <code>&#8211;file-headers</code> &#8211; Display the contents of the overall file header</p>
<dt> <code>&#8211;full-contents</code> &#8211; Display the content of each section</p>
<dt> <code>-h</code> &#8211; Alias for <code>&#8211;section-headers</code></p>
<dt> <code>&#8211;headers</code> &#8211; Alias for <code>&#8211;section-headers</code></p>
<dt> <code>-j</code> &#8211; Alias for <code>&#8211;section</code></p>
<dt> <code>-l</code> &#8211; Alias for <code>&#8211;line-numbers</code></p>
<dt> <code>&#8211;line-numbers</code> &#8211; Display source line numbers with disassembly. Implies disassemble object</p>
<dt> <code>-m</code> &#8211; Alias for <code>&#8211;macho</code></p>
<dt> <code>&#8211;macho</code> &#8211; Use MachO specific object file parser</p>
<dt> <code>&#8211;mattr=</code>&lt;a1,+a2,-a3,&#8230;&gt; &#8211; Target specific attributes</p>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;no-leading-addr</code> &#8211; Print no leading address</p>
<dt> <code>&#8211;no-show-raw-insn</code> &#8211; When disassembling instructions, do not print the instruction bytes.</p>
<dt> <code>-p</code> &#8211; Alias for <code>&#8211;private-headers</code></p>
<dt> <code>&#8211;print-imm-hex</code> &#8211; Use hex format for immediate values</p>
<dt> <code>&#8211;private-headers</code> &#8211; Display format specific file headers</p>
<dt> <code>-r</code> &#8211; Alias for <code>&#8211;reloc</code></p>
<dt> <code>&#8211;raw-clang-ast</code> &#8211; Dump the raw binary contents of the clang AST section</p>
<dt> <code>&#8211;reloc</code> &#8211; Display the relocation entries in the file</p>
<dt> <code>-s</code> &#8211; Alias for <code>&#8211;full-contents</code></p>
<dt> <code>&#8211;section=</code>&lt;string&gt; &#8211; Operate on the specified sections only. With <code>-macho</code> dump segment,section</p>
<dt> <code>&#8211;section-headers</code> &#8211; Display summaries of the headers for each section.</p>
<dt> <code>&#8211;show-lma</code> &#8211; Display LMA column when dumping ELF section headers</p>
<dt> <code>&#8211;source</code> &#8211; Display source inlined with disassembly. Implies disassemble object</p>
<dt> <code>&#8211;start-address=</code>&lt;address&gt; &#8211; Disassemble beginning at address</p>
<dt> <code>&#8211;stop-address=</code>&lt;address&gt; &#8211; Stop disassembly at address</p>
<dt> <code>&#8211;syms</code> &#8211; Display the symbol table</p>
<dt> <code>-t</code> &#8211; Alias for <code>&#8211;syms</code></p>
<dt> <code>&#8211;triple=</code>&lt;string&gt; &#8211; Target triple to disassemble for, see <code>-version</code> for available targets</p>
<dt> <code>-u</code> &#8211; Alias for <code>&#8211;unwind-info</code></p>
<dt> <code>&#8211;unwind-info</code> &#8211; Display unwind information</p>
<dt> <code>&#8211;wide</code> &#8211; Ignored for compatibility with GNU objdump</p>
<dt> <code>-x</code> &#8211; Alias for <code>&#8211;all-headers</code></p>
<dt> <code>-z</code> &#8211; Alias for <code>&#8211;disassemble-zeroes</code></dl>
<dd>Pass @FILE as argument to read options from FILE. </p>
<h2>Index</h2>
