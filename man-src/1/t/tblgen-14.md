---
title: "tblgen-14(1)"
name: "tblgen-14"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tblgen-14/"
description: "tblgen – Description to C++ Code"
---

<h2 class="name">NAME</h2>
<p> tblgen &#8211; Description to C++ Code </p>
<h2>SYNOPSIS</h2>
<p> <code>clang-tblgen</code> [<i>options</i>] [<i>filename</i>] </p>
<p> <code>lldb-tblgen</code> [<i>options</i>] [<i>filename</i>] </p>
<p> <code>llvm-tblgen</code> [<i>options</i>] [<i>filename</i>] </p>
<p> <code>mlir-tblgen</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>*-tblgen</code> is a family of programs that translates target description (<code>.td</code>) files into C++ code and other output formats. Most users of LLVM will not need to use this program. It is used only for writing parts of the compiler, debugger, and LLVM target backends. </p>
<p> The details of the input and output of the <code>*-tblgen</code> programs is beyond the scope of this short introduction; please see the TableGen Overview for an introduction and for references to additional TableGen documents. </p>
<p> The <i>filename</i> argument specifies the name of the Target Description (<code>.td</code>) file that TableGen processes.</p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-help</code></dt>
<dd> Print a description of the command line options.</dd>
<dt><code>-help-list</code></dt>
<dd> Print a description of the command line options in a simple list format.</dd>
<dt><code>-D=macroname</code></dt>
<dd> Specify the name of a macro to be defined. The name is defined, but it has no particular value.</dd>
<dt><code>-d=filename</code></dt>
<dd> Specify the name of the dependency filename.</dd>
<dt><code>-debug</code></dt>
<dd> Enable debug output.</dd>
<dt><code>-dump-json</code></dt>
<dd> Print a JSON representation of all records, suitable for further automated processing.</dd>
<dt><code>-I directory</code></dt>
<dd> Specify where to find other target description files for inclusion. The <code>directory</code> value should be a full or partial path to a directory that contains target description files.</dd>
<dt><code>-null-backend</code></dt>
<dd> Parse the source files and build the records, but do not run any backend. This is useful for timing the frontend.</dd>
<dt><code>-o filename</code></dt>
<dd> Specify the output file name. If <code>filename</code> is <code>&#8211;</code>, then <code>*-tblgen</code> sends its output to standard output.</dd>
<dt><code>-print-records</code></dt>
<dd> Print all classes and records to standard output (default backend option).</dd>
<dt><code>-print-detailed-records</code></dt>
<dd> Print a detailed report of all global variables, classes, and records to standard output.</dd>
<dt><code>-stats</code></dt>
<dd> Print a report with any statistics collected by the backend.</dd>
<dt><code>-time-phases</code></dt>
<dd> Time the parser and backend phases and print a report.</dd>
<dt><code>-version</code></dt>
<dd> Show the version number of the program.</dd>
<dt><code>-write-if-changed</code></dt>
<dd> Write the output file only if it is new or has changed.</dd></dl>
<h3>clang-tblgen Options</h3>
<dl>
<dt><code>-gen-clang-attr-classes</code></dt>
<dd> Generate Clang attribute clases.</dd>
<dt><code>-gen-clang-attr-parser-string-switches</code></dt>
<dd> Generate all parser-related attribute string switches.</dd>
<dt><code>-gen-clang-attr-subject-match-rules-parser-string-switches</code></dt>
<dd> Generate all parser-related attribute subject match rule string switches.</dd>
<dt><code>-gen-clang-attr-impl</code></dt>
<dd> Generate Clang attribute implementations.</dd>
<dt><code>-gen-clang-attr-list</code></dt>
<dd> Generate a Clang attribute list.</dd>
<dt><code>-gen-clang-attr-subject-match-rule-list</code></dt>
<dd> Generate a Clang attribute subject match rule list.</dd>
<dt><code>-gen-clang-attr-pch-read</code></dt>
<dd> Generate Clang PCH attribute reader.</dd>
<dt><code>-gen-clang-attr-pch-write</code></dt>
<dd> Generate Clang PCH attribute writer.</dd>
<dt><code>-gen-clang-attr-has-attribute-impl</code></dt>
<dd> Generate a Clang attribute spelling list.</dd>
<dt><code>-gen-clang-attr-spelling-index</code></dt>
<dd> Generate a Clang attribute spelling index.</dd>
<dt><code>-gen-clang-attr-ast-visitor</code></dt>
<dd> Generate a recursive AST visitor for Clang attributes.</dd>
<dt><code>-gen-clang-attr-template-instantiate</code></dt>
<dd> Generate a Clang template instantiate code.</dd>
<dt><code>-gen-clang-attr-parsed-attr-list</code></dt>
<dd> Generate a Clang parsed attribute list.</dd>
<dt><code>-gen-clang-attr-parsed-attr-impl</code></dt>
<dd> Generate the Clang parsed attribute helpers.</dd>
<dt><code>-gen-clang-attr-parsed-attr-kinds</code></dt>
<dd> Generate a Clang parsed attribute kinds.</dd>
<dt><code>-gen-clang-attr-text-node-dump</code></dt>
<dd> Generate Clang attribute text node dumper.</dd>
<dt><code>-gen-clang-attr-node-traverse</code></dt>
<dd> Generate Clang attribute traverser.</dd>
<dt><code>-gen-clang-diags-defs</code></dt>
<dd> Generate Clang diagnostics definitions.</dd>
<dt><code>-clang-component component</code></dt>
<dd> Only use warnings from specified component.</dd>
<dt><code>-gen-clang-diag-groups</code></dt>
<dd> Generate Clang diagnostic groups.</dd>
<dt><code>-gen-clang-diags-index-name</code></dt>
<dd> Generate Clang diagnostic name index.</dd>
<dt><code>-gen-clang-basic-reader</code></dt>
<dd> Generate Clang BasicReader classes.</dd>
<dt><code>-gen-clang-basic-writer</code></dt>
<dd> Generate Clang BasicWriter classes.</dd>
<dt><code>-gen-clang-comment-nodes</code></dt>
<dd> Generate Clang AST comment nodes.</dd>
<dt><code>-gen-clang-decl-nodes</code></dt>
<dd> Generate Clang AST declaration nodes.</dd>
<dt><code>-gen-clang-stmt-nodes</code></dt>
<dd> Generate Clang AST statement nodes.</dd>
<dt><code>-gen-clang-type-nodes</code></dt>
<dd> Generate Clang AST type nodes.</dd>
<dt><code>-gen-clang-type-reader</code></dt>
<dd> Generate Clang AbstractTypeReader class.</dd>
<dt><code>-gen-clang-type-writer</code></dt>
<dd> Generate Clang AbstractTypeWriter class.</dd>
<dt><code>-gen-clang-opcodes</code></dt>
<dd> Generate Clang constexpr interpreter opcodes.</dd>
<dt><code>-gen-clang-sa-checkers</code></dt>
<dd> Generate Clang static analyzer checkers.</dd>
<dt><code>-gen-clang-comment-html-tags</code></dt>
<dd> Generate efficient matchers for HTML tag names that are used in documentation comments.</dd>
<dt><code>-gen-clang-comment-html-tags-properties</code></dt>
<dd> Generate efficient matchers for HTML tag properties.</dd>
<dt><code>-gen-clang-comment-html-named-character-references</code></dt>
<dd> Generate function to translate named character references to UTF-8 sequences.</dd>
<dt><code>-gen-clang-comment-command-info</code></dt>
<dd> Generate command properties for commands that are used in documentation comments.</dd>
<dt><code>-gen-clang-comment-command-list</code></dt>
<dd> Generate list of commands that are used in documentation comments.</dd>
<dt><code>-gen-clang-opencl-builtins</code></dt>
<dd> Generate OpenCL builtin declaration handlers.</dd>
<dt><code>-gen-arm-neon</code></dt>
<dd> Generate <code>arm_neon.h</code> for Clang.</dd>
<dt><code>-gen-arm-fp16</code></dt>
<dd> Generate <code>arm_fp16.h</code> for Clang.</dd>
<dt><code>-gen-arm-bf16</code></dt>
<dd> Generate <code>arm_bf16.h</code> for Clang.</dd>
<dt><code>-gen-arm-neon-sema</code></dt>
<dd> Generate ARM NEON sema support for Clang.</dd>
<dt><code>-gen-arm-neon-test</code></dt>
<dd> Generate ARM NEON tests for Clang.</dd>
<dt><code>-gen-arm-sve-header</code></dt>
<dd> Generate <code>arm_sve.h</code> for Clang.</dd>
<dt><code>-gen-arm-sve-builtins</code></dt>
<dd> Generate <code>arm_sve_builtins.inc</code> for Clang.</dd>
<dt><code>-gen-arm-sve-builtin-codegen</code></dt>
<dd> Generate <code>arm_sve_builtin_cg_map.inc</code> for Clang.</dd>
<dt><code>-gen-arm-sve-typeflags</code></dt>
<dd> Generate <code>arm_sve_typeflags.inc</code> for Clang.</dd>
<dt><code>-gen-arm-sve-sema-rangechecks</code></dt>
<dd> Generate <code>arm_sve_sema_rangechecks.inc</code> for Clang.</dd>
<dt><code>-gen-arm-mve-header</code></dt>
<dd> Generate <code>arm_mve.h</code> for Clang.</dd>
<dt><code>-gen-arm-mve-builtin-def</code></dt>
<dd> Generate ARM MVE builtin definitions for Clang.</dd>
<dt><code>-gen-arm-mve-builtin-sema</code></dt>
<dd> Generate ARM MVE builtin sema checks for Clang.</dd>
<dt><code>-gen-arm-mve-builtin-codegen</code></dt>
<dd> Generate ARM MVE builtin code-generator for Clang.</dd>
<dt><code>-gen-arm-mve-builtin-aliases</code></dt>
<dd> Generate list of valid ARM MVE builtin aliases for Clang.</dd>
<dt><code>-gen-arm-cde-header</code></dt>
<dd> Generate <code>arm_cde.h</code> for Clang.</dd>
<dt><code>-gen-arm-cde-builtin-def</code></dt>
<dd> Generate ARM CDE builtin definitions for Clang.</dd>
<dt><code>-gen-arm-cde-builtin-sema</code></dt>
<dd> Generate ARM CDE builtin sema checks for Clang.</dd>
<dt><code>-gen-arm-cde-builtin-codegen</code></dt>
<dd> Generate ARM CDE builtin code-generator for Clang.</dd>
<dt><code>-gen-arm-cde-builtin-aliases</code></dt>
<dd> Generate list of valid ARM CDE builtin aliases for Clang.</dd>
<dt><code>-gen-riscv-vector-header</code></dt>
<dd> Generate <code>riscv_vector.h</code> for Clang.</dd>
<dt><code>-gen-riscv-vector-builtins</code></dt>
<dd> Generate <code>riscv_vector_builtins.inc</code> for Clang.</dd>
<dt><code>-gen-riscv-vector-builtin-codegen</code></dt>
<dd> Generate <code>riscv_vector_builtin_cg.inc</code> for Clang.</dd>
<dt><code>-gen-attr-docs</code></dt>
<dd> Generate attribute documentation.</dd>
<dt><code>-gen-diag-docs</code></dt>
<dd> Generate diagnostic documentation.</dd>
<dt><code>-gen-opt-docs</code></dt>
<dd> Generate option documentation.</dd>
<dt><code>-gen-clang-data-collectors</code></dt>
<dd> Generate data collectors for AST nodes.</dd>
<dt><code>-gen-clang-test-pragma-attribute-supported-attributes</code></dt>
<dd> Generate a list of attributes supported by <code>#pragma</code> Clang attribute for testing purposes.</dd></dl>
<h3>lldb-tblgen Options</h3>
<dl>
<dt><code>gen-lldb-option-defs</code></dt>
<dd> Generate lldb OptionDefinition values.</dd>
<dt><code>gen-lldb-property-defs</code></dt>
<dd> Generate lldb PropertyDefinition values.</dd>
<dt><code>gen-lldb-property-enum-defs</code></dt>
<dd> Generate lldb PropertyDefinition enum values.</dd></dl>
<h3>llvm-tblgen Options</h3>
<dl>
<dt><code>-gen-asm-matcher</code></dt>
<dd> Generate assembly instruction matcher.</dd>
<dt><code>-match-prefix=prefix</code></dt>
<dd> Make -gen-asm-matcher match only instructions with the given <i>prefix</i>.</dd>
<dt><code>-gen-asm-parser</code></dt>
<dd> Generate assembly instruction parser.</dd>
<dt><code>-asmparsernum=n</code></dt>
<dd> Make -gen-asm-parser emit assembly parser number <i>n</i>.</dd>
<dt><code>-gen-asm-writer</code></dt>
<dd> Generate assembly writer.</dd>
<dt><code>-asmwriternum=n</code></dt>
<dd> Make -gen-asm-writer emit assembly writer number <i>n</i>.</dd>
<dt><code>-gen-attrs</code></dt>
<dd> Generate attributes.</dd>
<dt><code>-gen-automata</code></dt>
<dd> Generate generic automata.</dd>
<dt><code>-gen-callingconv</code></dt>
<dd> Generate calling convention descriptions.</dd>
<dt><code>-gen-compress-inst-emitter</code></dt>
<dd> Generate RISC-V compressed instructions.</dd>
<dt><code>-gen-ctags</code></dt>
<dd> Generate ctags-compatible index.</dd>
<dt><code>-gen-dag-isel</code></dt>
<dd> Generate a DAG (directed acyclic graph) instruction selector.</dd>
<dt><code>-instrument-coverage</code></dt>
<dd> Make -gen-dag-isel generate tables to help identify the patterns matched.</dd>
<dt><code>-omit-comments</code></dt>
<dd> Make -gen-dag-isel omit comments. The default is false.</dd>
<dt><code>-gen-dfa-packetizer</code></dt>
<dd> Generate DFA Packetizer for VLIW targets.</dd>
<dt><code>-gen-directive-decl</code></dt>
<dd> Generate directive related declaration code (header file).</dd>
<dt><code>-gen-directive-gen</code></dt>
<dd> Generate directive related implementation code part.</dd>
<dt><code>-gen-directive-impl</code></dt>
<dd> Generate directive related implementation code.</dd>
<dt><code>-gen-disassembler</code></dt>
<dd> Generate disassembler.</dd>
<dt><code>-gen-emitter</code></dt>
<dd> Generate machine code emitter.</dd>
<dt><code>-gen-exegesis</code></dt>
<dd> Generate llvm-exegesis tables.</dd>
<dt><code>-gen-fast-isel</code></dt>
<dd> Generate a “fast” instruction selector.</dd>
<dt><code>-gen-global-isel</code></dt>
<dd> Generate GlobalISel selector.</dd>
<dt><code>-gisel-coverage-file=filename</code></dt>
<dd> Specify the file from which to retrieve coverage information.</dd>
<dt><code>-instrument-gisel-coverage</code></dt>
<dd> Make -gen-global-isel generate coverage instrumentation.</dd>
<dt><code>-optimize-match-table</code></dt>
<dd> Make -gen-global-isel generate an optimized version of the match table.</dd>
<dt><code>-warn-on-skipped-patterns</code></dt>
<dd> Make -gen-global-isel explain why a pattern was skipped for inclusion.</dd>
<dt><code>-gen-global-isel-combiner</code></dt>
<dd> Generate GlobalISel combiner.</dd>
<dt><code>-combiners=list</code></dt>
<dd> Make -gen-global-isel-combiner emit the specified combiners.</dd>
<dt><code>-gicombiner-show-expansions</code></dt>
<dd> Make -gen-global-isel-combiner use C++ comments to indicate occurrences of code expansion.</dd>
<dt><code>-gicombiner-stop-after-build</code></dt>
<dd> Make -gen-global-isel-combiner stop processing after building the match tree.</dd>
<dt><code>-gicombiner-stop-after-parse</code></dt>
<dd> Make -gen-global-isel-combiner stop processing after parsing rules and dump state.</dd>
<dt><code>-gen-instr-info</code></dt>
<dd> Generate instruction descriptions.</dd>
<dt><code>-gen-instr-docs</code></dt>
<dd> Generate instruction documentation.</dd>
<dt><code>-gen-intrinsic-enums</code></dt>
<dd> Generate intrinsic enums.</dd>
<dt><code>-intrinsic-prefix=prefix</code></dt>
<dd> Make -gen-intrinsic-enums generate intrinsics with this target <i>prefix</i>.</dd>
<dt><code>-gen-intrinsic-impl</code></dt>
<dd> Generate intrinsic information.</dd>
<dt><code>-gen-opt-parser-defs</code></dt>
<dd> Generate options definitions.</dd>
<dt><code>-gen-opt-rst</code></dt>
<dd> Generate option RST.</dd>
<dt><code>-gen-pseudo-lowering</code></dt>
<dd> Generate pseudo instruction lowering.</dd>
<dt><code>-gen-register-bank</code></dt>
<dd> Generate register bank descriptions.</dd>
<dt><code>-gen-register-info</code></dt>
<dd> Generate registers and register classes info.</dd>
<dt><code>-register-info-debug</code></dt>
<dd> Make -gen-register-info dump register information for debugging.</dd>
<dt><code>-gen-searchable-tables</code></dt>
<dd> Generate generic searchable tables. See TableGen BackEnds for a detailed description.</dd>
<dt><code>-gen-subtarget</code></dt>
<dd> Generate subtarget enumerations.</dd>
<dt><code>-gen-x86-EVEX2VEX-tables</code></dt>
<dd> Generate X86 EVEX to VEX compress tables.</dd>
<dt><code>-gen-x86-fold-tables</code></dt>
<dd> Generate X86 fold tables.</dd>
<dt><code>-long-string-literals</code></dt>
<dd> When emitting large string tables, prefer string literals over comma-separated char literals. This can be a readability and compile-time performance win, but upsets some compilers.</dd>
<dt><code>-print-enums</code></dt>
<dd> Print enumeration values for a class.</dd>
<dt><code>-class=classname</code></dt>
<dd> Make -print-enums print the enumeration list for the specified class.</dd>
<dt><code>-print-sets</code></dt>
<dd> Print expanded sets for testing DAG exprs.</dd></dl>
<h3>mlir-tblgen Options</h3>
<dl>
<dt><code>-gen-avail-interface-decls</code></dt>
<dd> Generate availability interface declarations.</dd>
<dt><code>-gen-avail-interface-defs</code></dt>
<dd> Generate op interface definitions.</dd>
<dt><code>-gen-dialect-doc</code></dt>
<dd> Generate dialect documentation.</dd>
<dt><code>-dialect</code></dt>
<dd> The dialect to generate.</dd>
<dt><code>-gen-directive-decl</code></dt>
<dd> Generate declarations for directives (OpenMP, etc.).</dd>
<dt><code>-gen-enum-decls</code></dt>
<dd> Generate enum utility declarations.</dd>
<dt><code>-gen-enum-defs</code></dt>
<dd> Generate enum utility definitions.</dd>
<dt><code>-gen-enum-from-llvmir-conversions</code></dt>
<dd> Generate conversions of EnumAttrs from LLVM IR.</dd>
<dt><code>-gen-enum-to-llvmir-conversions</code></dt>
<dd> Generate conversions of EnumAttrs to LLVM IR.</dd>
<dt><code>-gen-llvmir-conversions</code></dt>
<dd> Generate LLVM IR conversions.</dd>
<dt><code>-gen-llvmir-intrinsics</code></dt>
<dd> Generate LLVM IR intrinsics.</dd>
<dt><code>-llvmir-intrinsics-filter</code></dt>
<dd> Only keep the intrinsics with the specified substring in their record name.</dd>
<dt><code>-dialect-opclass-base</code></dt>
<dd> The base class for the ops in the dialect we are to emit.</dd>
<dt><code>-gen-op-decls</code></dt>
<dd> Generate operation declarations.</dd>
<dt><code>-gen-op-defs</code></dt>
<dd> Generate operation definitions.</dd>
<dt><code>-asmformat-error-is-fatal</code></dt>
<dd> Emit a fatal error if format parsing fails.</dd>
<dt><code>-op-exclude-regex</code></dt>
<dd> Regular expression of name of ops to exclude (no filter if empty).</dd>
<dt><code>-op-include-regex</code></dt>
<dd> Regular expression of name of ops to include (no filter if empty).</dd>
<dt><code>-gen-op-doc</code></dt>
<dd> Generate operation documentation.</dd>
<dt><code>-gen-pass-decls</code></dt>
<dd> Generate operation documentation.</dd>
<dt><code>-name namestring</code></dt>
<dd> The name of this group of passes.</dd>
<dt><code>-gen-pass-doc</code></dt>
<dd> Generate pass documentation.</dd>
<dt><code>-gen-rewriters</code></dt>
<dd> Generate pattern rewriters.</dd>
<dt><code>-gen-spirv-avail-impls</code></dt>
<dd> Generate SPIR-V operation utility definitions.</dd>
<dt><code>-gen-spirv-capability-implication</code></dt>
<dd> Generate utility function to return implied capabilities for a given capability.</dd>
<dt><code>-gen-spirv-enum-avail-decls</code></dt>
<dd> Generate SPIR-V enum availability declarations.</dd>
<dt><code>-gen-spirv-enum-avail-defs</code></dt>
<dd> Generate SPIR-V enum availability definitions.</dd>
<dt><code>-gen-spirv-op-utils</code></dt>
<dd> Generate SPIR-V operation utility definitions.</dd>
<dt><code>-gen-spirv-serialization</code></dt>
<dd> Generate SPIR-V (de)serialization utilities and functions.</dd>
<dt><code>-gen-struct-attr-decls</code></dt>
<dd> Generate struct utility declarations.</dd>
<dt><code>-gen-struct-attr-defs</code></dt>
<dd> Generate struct utility definitions.</dd>
<dt><code>-gen-typedef-decls</code></dt>
<dd> Generate TypeDef declarations.</dd>
<dt><code>-gen-typedef-defs</code></dt>
<dd> Generate TypeDef definitions.</dd>
<dt><code>-typedefs-dialect name</code></dt>
<dd> Generate types for this dialect.</dd></dl>
<h2>EXIT STATUS</h2>
<p> If <code>*-tblgen</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
