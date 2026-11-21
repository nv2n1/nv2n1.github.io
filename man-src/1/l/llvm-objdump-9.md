---
title: "llvm-objdump-9(1)"
name: "llvm-objdump-9"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-objdump-9/"
description: "llvm-objdump – manual page for llvm-objdump 9"
---

<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm object file dumper </p>
<p> USAGE: llvm-objdump [options] &lt;input object files&gt; </p>
<p> OPTIONS: </p>
<p> Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</dt>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</dt>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dt></dl>
<dd>llvm-objdump MachO Specific Options:</dd>
<dl>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; architecture(s) from a Mach-O file to dump</dt>
<dt> <code>&#8211;archive-member-offsets</code> &#8211; Print the offset to each archive member for Mach-O archives (requires <code>-macho</code> and <code>-archive-headers</code>)</dt>
<dt> <code>&#8211;bind</code> &#8211; Display mach-o binding info</dt>
<dt> <code>&#8211;data-in-code</code> &#8211; Print the data in code table for Mach-O objects (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;dis-symname=</code>&lt;string&gt; &#8211; disassemble just this symbol&#8217;s instructions (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;dsym=</code>&lt;string&gt; &#8211; Use .dSYM file for debug info</dt>
<dt> <code>&#8211;dylib-id</code> &#8211; Print the shared library&#8217;s id for the dylib Mach-O file (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;dylibs-used</code> &#8211; Print the shared libraries used for linked Mach-O files (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;exports-trie</code> &#8211; Display mach-o exported symbols</dt>
<dt> <code>&#8211;full-leading-addr</code> &#8211; Print full leading address</dt>
<dt> <code>-g</code> &#8211; Print line information from debug info if available</dt>
<dt> <code>&#8211;indirect-symbols</code> &#8211; Print indirect symbol table for Mach-O objects (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;info-plist</code> &#8211; Print the info plist section as strings for Mach-O objects (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;lazy-bind</code> &#8211; Display mach-o lazy binding info</dt>
<dt> <code>&#8211;link-opt-hints</code> &#8211; Print the linker optimization hints for Mach-O objects (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;no-leading-headers</code> &#8211; Print no leading headers</dt>
<dt> <code>&#8211;no-symbolic-operands</code> &#8211; do not symbolic operands when disassembling (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;non-verbose</code> &#8211; Print the info for Mach-O objects in non-verbose or numeric form (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;objc-meta-data</code> &#8211; Print the Objective-C runtime meta data for Mach-O files (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;private-header</code> &#8211; Display only the first format specific file header</dt>
<dt> <code>&#8211;rebase</code> &#8211; Display mach-o rebasing info</dt>
<dt> <code>&#8211;universal-headers</code> &#8211; Print Mach-O universal headers (requires <code>-macho</code>)</dt>
<dt> <code>&#8211;weak-bind</code> &#8211; Display mach-o weak binding info</dt></dl>
<dd>llvm-objdump Options:</dd>
<dl>
<dt> <code>-C</code> &#8211; Alias for <code>&#8211;demangle</code></dt>
<dt> <code>-D</code> &#8211; Alias for <code>&#8211;disassemble-all</code></dt>
<dt> <code>-M</code> &#8211; Alias for <code>&#8211;disassembler-options</code></dt>
<dt> <code>-R</code> &#8211; Alias for <code>&#8211;dynamic-reloc</code></dt>
<dt> <code>-S</code> &#8211; Alias for <code>-source</code></dt>
<dt> <code>-a</code> &#8211; Alias for <code>&#8211;archive-headers</code></dt>
<dt> <code>&#8211;adjust-vma=</code>&lt;offset&gt; &#8211; Increase the displayed address by the specified offset</dt>
<dt> <code>&#8211;all-headers</code> &#8211; Display all available header information</dt>
<dt> <code>&#8211;arch-name=</code>&lt;string&gt; &#8211; Target arch to disassemble for, see <code>-version</code> for available targets</dt>
<dt> <code>&#8211;archive-headers</code> &#8211; Display archive header information</dt>
<dt> <code>-d</code> &#8211; Alias for <code>&#8211;disassemble</code></dt>
<dt> <code>&#8211;demangle</code> &#8211; Demangle symbols names</dt>
<dt> <code>&#8211;disassemble</code> &#8211; Display assembler mnemonics for the machine instructions</dt>
<dt> <code>&#8211;disassemble-all</code> &#8211; Display assembler mnemonics for the machine instructions</dt>
<dt> <code>&#8211;disassemble-functions=</code>&lt;string&gt; &#8211; List of functions to disassemble. Accept demangled names when <code>&#8211;demangle</code> is specified, otherwise accept mangled names</dt>
<dt> <code>&#8211;disassemble-zeroes</code> &#8211; Do not skip blocks of zeroes when disassembling</dt>
<dt> <code>&#8211;disassembler-options=</code>&lt;options&gt; &#8211; Pass target specific disassembler options</dt>
<dt> <code>&#8211;dwarf=</code>&lt;value&gt; &#8211; Dump of dwarf debug sections:</dt>
<dt>=frames</dt>
<dd> &#8211; .debug_frame</dd>
<dt> <code>&#8211;dynamic-reloc</code> &#8211; Display the dynamic relocation entries in the file</dt>
<dt> <code>-f</code> &#8211; Alias for <code>&#8211;file-headers</code></dt>
<dt> <code>&#8211;fault-map-section</code> &#8211; Display contents of faultmap section</dt>
<dt> <code>&#8211;file-headers</code> &#8211; Display the contents of the overall file header</dt>
<dt> <code>&#8211;full-contents</code> &#8211; Display the content of each section</dt>
<dt> <code>-h</code> &#8211; Alias for <code>&#8211;section-headers</code></dt>
<dt> <code>&#8211;headers</code> &#8211; Alias for <code>&#8211;section-headers</code></dt>
<dt> <code>-j</code> &#8211; Alias for <code>&#8211;section</code></dt>
<dt> <code>-l</code> &#8211; Alias for <code>&#8211;line-numbers</code></dt>
<dt> <code>&#8211;line-numbers</code> &#8211; Display source line numbers with disassembly. Implies disassemble object</dt>
<dt> <code>-m</code> &#8211; Alias for <code>&#8211;macho</code></dt>
<dt> <code>&#8211;macho</code> &#8211; Use MachO specific object file parser</dt>
<dt> <code>&#8211;mattr=</code>&lt;a1,+a2,-a3,&#8230;&gt; &#8211; Target specific attributes</dt>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</dt>
<dt> <code>&#8211;no-leading-addr</code> &#8211; Print no leading address</dt>
<dt> <code>&#8211;no-show-raw-insn</code> &#8211; When disassembling instructions, do not print the instruction bytes.</dt>
<dt> <code>-p</code> &#8211; Alias for <code>&#8211;private-headers</code></dt>
<dt> <code>&#8211;print-imm-hex</code> &#8211; Use hex format for immediate values</dt>
<dt> <code>&#8211;private-headers</code> &#8211; Display format specific file headers</dt>
<dt> <code>-r</code> &#8211; Alias for <code>&#8211;reloc</code></dt>
<dt> <code>&#8211;raw-clang-ast</code> &#8211; Dump the raw binary contents of the clang AST section</dt>
<dt> <code>&#8211;reloc</code> &#8211; Display the relocation entries in the file</dt>
<dt> <code>-s</code> &#8211; Alias for <code>&#8211;full-contents</code></dt>
<dt> <code>&#8211;section=</code>&lt;string&gt; &#8211; Operate on the specified sections only. With <code>-macho</code> dump segment,section</dt>
<dt> <code>&#8211;section-headers</code> &#8211; Display summaries of the headers for each section.</dt>
<dt> <code>&#8211;show-lma</code> &#8211; Display LMA column when dumping ELF section headers</dt>
<dt> <code>&#8211;source</code> &#8211; Display source inlined with disassembly. Implies disassemble object</dt>
<dt> <code>&#8211;start-address=</code>&lt;address&gt; &#8211; Disassemble beginning at address</dt>
<dt> <code>&#8211;stop-address=</code>&lt;address&gt; &#8211; Stop disassembly at address</dt>
<dt> <code>&#8211;syms</code> &#8211; Display the symbol table</dt>
<dt> <code>-t</code> &#8211; Alias for <code>&#8211;syms</code></dt>
<dt> <code>&#8211;triple=</code>&lt;string&gt; &#8211; Target triple to disassemble for, see <code>-version</code> for available targets</dt>
<dt> <code>-u</code> &#8211; Alias for <code>&#8211;unwind-info</code></dt>
<dt> <code>&#8211;unwind-info</code> &#8211; Display unwind information</dt>
<dt> <code>&#8211;wide</code> &#8211; Ignored for compatibility with GNU objdump</dt>
<dt> <code>-x</code> &#8211; Alias for <code>&#8211;all-headers</code></dt>
<dt> <code>-z</code> &#8211; Alias for <code>&#8211;disassemble-zeroes</code></dt></dl>
<dd>Pass @FILE as argument to read options from FILE. </dd>
