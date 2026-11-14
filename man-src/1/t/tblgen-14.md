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
<dt><code>-help</code></p>
<dd> Print a description of the command line options.</p>
<dt><code>-help-list</code></p>
<dd> Print a description of the command line options in a simple list format.</p>
<dt><code>-D=macroname</code></p>
<dd> Specify the name of a macro to be defined. The name is defined, but it has no particular value.</p>
<dt><code>-d=filename</code></p>
<dd> Specify the name of the dependency filename.</p>
<dt><code>-debug</code></p>
<dd> Enable debug output.</p>
<dt><code>-dump-json</code></p>
<dd> Print a JSON representation of all records, suitable for further automated processing.</p>
<dt><code>-I directory</code></p>
<dd> Specify where to find other target description files for inclusion. The <code>directory</code> value should be a full or partial path to a directory that contains target description files.</p>
<dt><code>-null-backend</code></p>
<dd> Parse the source files and build the records, but do not run any backend. This is useful for timing the frontend.</p>
<dt><code>-o filename</code></p>
<dd> Specify the output file name. If <code>filename</code> is <code>&#8211;</code>, then <code>*-tblgen</code> sends its output to standard output.</p>
<dt><code>-print-records</code></p>
<dd> Print all classes and records to standard output (default backend option).</p>
<dt><code>-print-detailed-records</code></p>
<dd> Print a detailed report of all global variables, classes, and records to standard output.</p>
<dt><code>-stats</code></p>
<dd> Print a report with any statistics collected by the backend.</p>
<dt><code>-time-phases</code></p>
<dd> Time the parser and backend phases and print a report.</p>
<dt><code>-version</code></p>
<dd> Show the version number of the program.</p>
<dt><code>-write-if-changed</code></p>
<dd> Write the output file only if it is new or has changed.</dl>
<h3>clang-tblgen Options</h3>
<dl>
<dt><code>-gen-clang-attr-classes</code></p>
<dd> Generate Clang attribute clases.</p>
<dt><code>-gen-clang-attr-parser-string-switches</code></p>
<dd> Generate all parser-related attribute string switches.</p>
<dt><code>-gen-clang-attr-subject-match-rules-parser-string-switches</code></p>
<dd> Generate all parser-related attribute subject match rule string switches.</p>
<dt><code>-gen-clang-attr-impl</code></p>
<dd> Generate Clang attribute implementations.</p>
<dt><code>-gen-clang-attr-list</code></p>
<dd> Generate a Clang attribute list.</p>
<dt><code>-gen-clang-attr-subject-match-rule-list</code></p>
<dd> Generate a Clang attribute subject match rule list.</p>
<dt><code>-gen-clang-attr-pch-read</code></p>
<dd> Generate Clang PCH attribute reader.</p>
<dt><code>-gen-clang-attr-pch-write</code></p>
<dd> Generate Clang PCH attribute writer.</p>
<dt><code>-gen-clang-attr-has-attribute-impl</code></p>
<dd> Generate a Clang attribute spelling list.</p>
<dt><code>-gen-clang-attr-spelling-index</code></p>
<dd> Generate a Clang attribute spelling index.</p>
<dt><code>-gen-clang-attr-ast-visitor</code></p>
<dd> Generate a recursive AST visitor for Clang attributes.</p>
<dt><code>-gen-clang-attr-template-instantiate</code></p>
<dd> Generate a Clang template instantiate code.</p>
<dt><code>-gen-clang-attr-parsed-attr-list</code></p>
<dd> Generate a Clang parsed attribute list.</p>
<dt><code>-gen-clang-attr-parsed-attr-impl</code></p>
<dd> Generate the Clang parsed attribute helpers.</p>
<dt><code>-gen-clang-attr-parsed-attr-kinds</code></p>
<dd> Generate a Clang parsed attribute kinds.</p>
<dt><code>-gen-clang-attr-text-node-dump</code></p>
<dd> Generate Clang attribute text node dumper.</p>
<dt><code>-gen-clang-attr-node-traverse</code></p>
<dd> Generate Clang attribute traverser.</p>
<dt><code>-gen-clang-diags-defs</code></p>
<dd> Generate Clang diagnostics definitions.</p>
<dt><code>-clang-component component</code></p>
<dd> Only use warnings from specified component.</p>
<dt><code>-gen-clang-diag-groups</code></p>
<dd> Generate Clang diagnostic groups.</p>
<dt><code>-gen-clang-diags-index-name</code></p>
<dd> Generate Clang diagnostic name index.</p>
<dt><code>-gen-clang-basic-reader</code></p>
<dd> Generate Clang BasicReader classes.</p>
<dt><code>-gen-clang-basic-writer</code></p>
<dd> Generate Clang BasicWriter classes.</p>
<dt><code>-gen-clang-comment-nodes</code></p>
<dd> Generate Clang AST comment nodes.</p>
<dt><code>-gen-clang-decl-nodes</code></p>
<dd> Generate Clang AST declaration nodes.</p>
<dt><code>-gen-clang-stmt-nodes</code></p>
<dd> Generate Clang AST statement nodes.</p>
<dt><code>-gen-clang-type-nodes</code></p>
<dd> Generate Clang AST type nodes.</p>
<dt><code>-gen-clang-type-reader</code></p>
<dd> Generate Clang AbstractTypeReader class.</p>
<dt><code>-gen-clang-type-writer</code></p>
<dd> Generate Clang AbstractTypeWriter class.</p>
<dt><code>-gen-clang-opcodes</code></p>
<dd> Generate Clang constexpr interpreter opcodes.</p>
<dt><code>-gen-clang-sa-checkers</code></p>
<dd> Generate Clang static analyzer checkers.</p>
<dt><code>-gen-clang-comment-html-tags</code></p>
<dd> Generate efficient matchers for HTML tag names that are used in documentation comments.</p>
<dt><code>-gen-clang-comment-html-tags-properties</code></p>
<dd> Generate efficient matchers for HTML tag properties.</p>
<dt><code>-gen-clang-comment-html-named-character-references</code></p>
<dd> Generate function to translate named character references to UTF-8 sequences.</p>
<dt><code>-gen-clang-comment-command-info</code></p>
<dd> Generate command properties for commands that are used in documentation comments.</p>
<dt><code>-gen-clang-comment-command-list</code></p>
<dd> Generate list of commands that are used in documentation comments.</p>
<dt><code>-gen-clang-opencl-builtins</code></p>
<dd> Generate OpenCL builtin declaration handlers.</p>
<dt><code>-gen-arm-neon</code></p>
<dd> Generate <code>arm_neon.h</code> for Clang.</p>
<dt><code>-gen-arm-fp16</code></p>
<dd> Generate <code>arm_fp16.h</code> for Clang.</p>
<dt><code>-gen-arm-bf16</code></p>
<dd> Generate <code>arm_bf16.h</code> for Clang.</p>
<dt><code>-gen-arm-neon-sema</code></p>
<dd> Generate ARM NEON sema support for Clang.</p>
<dt><code>-gen-arm-neon-test</code></p>
<dd> Generate ARM NEON tests for Clang.</p>
<dt><code>-gen-arm-sve-header</code></p>
<dd> Generate <code>arm_sve.h</code> for Clang.</p>
<dt><code>-gen-arm-sve-builtins</code></p>
<dd> Generate <code>arm_sve_builtins.inc</code> for Clang.</p>
<dt><code>-gen-arm-sve-builtin-codegen</code></p>
<dd> Generate <code>arm_sve_builtin_cg_map.inc</code> for Clang.</p>
<dt><code>-gen-arm-sve-typeflags</code></p>
<dd> Generate <code>arm_sve_typeflags.inc</code> for Clang.</p>
<dt><code>-gen-arm-sve-sema-rangechecks</code></p>
<dd> Generate <code>arm_sve_sema_rangechecks.inc</code> for Clang.</p>
<dt><code>-gen-arm-mve-header</code></p>
<dd> Generate <code>arm_mve.h</code> for Clang.</p>
<dt><code>-gen-arm-mve-builtin-def</code></p>
<dd> Generate ARM MVE builtin definitions for Clang.</p>
<dt><code>-gen-arm-mve-builtin-sema</code></p>
<dd> Generate ARM MVE builtin sema checks for Clang.</p>
<dt><code>-gen-arm-mve-builtin-codegen</code></p>
<dd> Generate ARM MVE builtin code-generator for Clang.</p>
<dt><code>-gen-arm-mve-builtin-aliases</code></p>
<dd> Generate list of valid ARM MVE builtin aliases for Clang.</p>
<dt><code>-gen-arm-cde-header</code></p>
<dd> Generate <code>arm_cde.h</code> for Clang.</p>
<dt><code>-gen-arm-cde-builtin-def</code></p>
<dd> Generate ARM CDE builtin definitions for Clang.</p>
<dt><code>-gen-arm-cde-builtin-sema</code></p>
<dd> Generate ARM CDE builtin sema checks for Clang.</p>
<dt><code>-gen-arm-cde-builtin-codegen</code></p>
<dd> Generate ARM CDE builtin code-generator for Clang.</p>
<dt><code>-gen-arm-cde-builtin-aliases</code></p>
<dd> Generate list of valid ARM CDE builtin aliases for Clang.</p>
<dt><code>-gen-riscv-vector-header</code></p>
<dd> Generate <code>riscv_vector.h</code> for Clang.</p>
<dt><code>-gen-riscv-vector-builtins</code></p>
<dd> Generate <code>riscv_vector_builtins.inc</code> for Clang.</p>
<dt><code>-gen-riscv-vector-builtin-codegen</code></p>
<dd> Generate <code>riscv_vector_builtin_cg.inc</code> for Clang.</p>
<dt><code>-gen-attr-docs</code></p>
<dd> Generate attribute documentation.</p>
<dt><code>-gen-diag-docs</code></p>
<dd> Generate diagnostic documentation.</p>
<dt><code>-gen-opt-docs</code></p>
<dd> Generate option documentation.</p>
<dt><code>-gen-clang-data-collectors</code></p>
<dd> Generate data collectors for AST nodes.</p>
<dt><code>-gen-clang-test-pragma-attribute-supported-attributes</code></p>
<dd> Generate a list of attributes supported by <code>#pragma</code> Clang attribute for testing purposes.</dl>
<h3>lldb-tblgen Options</h3>
<dl>
<dt><code>gen-lldb-option-defs</code></p>
<dd> Generate lldb OptionDefinition values.</p>
<dt><code>gen-lldb-property-defs</code></p>
<dd> Generate lldb PropertyDefinition values.</p>
<dt><code>gen-lldb-property-enum-defs</code></p>
<dd> Generate lldb PropertyDefinition enum values.</dl>
<h3>llvm-tblgen Options</h3>
<dl>
<dt><code>-gen-asm-matcher</code></p>
<dd> Generate assembly instruction matcher.</p>
<dt><code>-match-prefix=prefix</code></p>
<dd> Make -gen-asm-matcher match only instructions with the given <i>prefix</i>.</p>
<dt><code>-gen-asm-parser</code></p>
<dd> Generate assembly instruction parser.</p>
<dt><code>-asmparsernum=n</code></p>
<dd> Make -gen-asm-parser emit assembly parser number <i>n</i>.</p>
<dt><code>-gen-asm-writer</code></p>
<dd> Generate assembly writer.</p>
<dt><code>-asmwriternum=n</code></p>
<dd> Make -gen-asm-writer emit assembly writer number <i>n</i>.</p>
<dt><code>-gen-attrs</code></p>
<dd> Generate attributes.</p>
<dt><code>-gen-automata</code></p>
<dd> Generate generic automata.</p>
<dt><code>-gen-callingconv</code></p>
<dd> Generate calling convention descriptions.</p>
<dt><code>-gen-compress-inst-emitter</code></p>
<dd> Generate RISC-V compressed instructions.</p>
<dt><code>-gen-ctags</code></p>
<dd> Generate ctags-compatible index.</p>
<dt><code>-gen-dag-isel</code></p>
<dd> Generate a DAG (directed acyclic graph) instruction selector.</p>
<dt><code>-instrument-coverage</code></p>
<dd> Make -gen-dag-isel generate tables to help identify the patterns matched.</p>
<dt><code>-omit-comments</code></p>
<dd> Make -gen-dag-isel omit comments. The default is false.</p>
<dt><code>-gen-dfa-packetizer</code></p>
<dd> Generate DFA Packetizer for VLIW targets.</p>
<dt><code>-gen-directive-decl</code></p>
<dd> Generate directive related declaration code (header file).</p>
<dt><code>-gen-directive-gen</code></p>
<dd> Generate directive related implementation code part.</p>
<dt><code>-gen-directive-impl</code></p>
<dd> Generate directive related implementation code.</p>
<dt><code>-gen-disassembler</code></p>
<dd> Generate disassembler.</p>
<dt><code>-gen-emitter</code></p>
<dd> Generate machine code emitter.</p>
<dt><code>-gen-exegesis</code></p>
<dd> Generate llvm-exegesis tables.</p>
<dt><code>-gen-fast-isel</code></p>
<dd> Generate a “fast” instruction selector.</p>
<dt><code>-gen-global-isel</code></p>
<dd> Generate GlobalISel selector.</p>
<dt><code>-gisel-coverage-file=filename</code></p>
<dd> Specify the file from which to retrieve coverage information.</p>
<dt><code>-instrument-gisel-coverage</code></p>
<dd> Make -gen-global-isel generate coverage instrumentation.</p>
<dt><code>-optimize-match-table</code></p>
<dd> Make -gen-global-isel generate an optimized version of the match table.</p>
<dt><code>-warn-on-skipped-patterns</code></p>
<dd> Make -gen-global-isel explain why a pattern was skipped for inclusion.</p>
<dt><code>-gen-global-isel-combiner</code></p>
<dd> Generate GlobalISel combiner.</p>
<dt><code>-combiners=list</code></p>
<dd> Make -gen-global-isel-combiner emit the specified combiners.</p>
<dt><code>-gicombiner-show-expansions</code></p>
<dd> Make -gen-global-isel-combiner use C++ comments to indicate occurrences of code expansion.</p>
<dt><code>-gicombiner-stop-after-build</code></p>
<dd> Make -gen-global-isel-combiner stop processing after building the match tree.</p>
<dt><code>-gicombiner-stop-after-parse</code></p>
<dd> Make -gen-global-isel-combiner stop processing after parsing rules and dump state.</p>
<dt><code>-gen-instr-info</code></p>
<dd> Generate instruction descriptions.</p>
<dt><code>-gen-instr-docs</code></p>
<dd> Generate instruction documentation.</p>
<dt><code>-gen-intrinsic-enums</code></p>
<dd> Generate intrinsic enums.</p>
<dt><code>-intrinsic-prefix=prefix</code></p>
<dd> Make -gen-intrinsic-enums generate intrinsics with this target <i>prefix</i>.</p>
<dt><code>-gen-intrinsic-impl</code></p>
<dd> Generate intrinsic information.</p>
<dt><code>-gen-opt-parser-defs</code></p>
<dd> Generate options definitions.</p>
<dt><code>-gen-opt-rst</code></p>
<dd> Generate option RST.</p>
<dt><code>-gen-pseudo-lowering</code></p>
<dd> Generate pseudo instruction lowering.</p>
<dt><code>-gen-register-bank</code></p>
<dd> Generate register bank descriptions.</p>
<dt><code>-gen-register-info</code></p>
<dd> Generate registers and register classes info.</p>
<dt><code>-register-info-debug</code></p>
<dd> Make -gen-register-info dump register information for debugging.</p>
<dt><code>-gen-searchable-tables</code></p>
<dd> Generate generic searchable tables. See TableGen BackEnds for a detailed description.</p>
<dt><code>-gen-subtarget</code></p>
<dd> Generate subtarget enumerations.</p>
<dt><code>-gen-x86-EVEX2VEX-tables</code></p>
<dd> Generate X86 EVEX to VEX compress tables.</p>
<dt><code>-gen-x86-fold-tables</code></p>
<dd> Generate X86 fold tables.</p>
<dt><code>-long-string-literals</code></p>
<dd> When emitting large string tables, prefer string literals over comma-separated char literals. This can be a readability and compile-time performance win, but upsets some compilers.</p>
<dt><code>-print-enums</code></p>
<dd> Print enumeration values for a class.</p>
<dt><code>-class=classname</code></p>
<dd> Make -print-enums print the enumeration list for the specified class.</p>
<dt><code>-print-sets</code></p>
<dd> Print expanded sets for testing DAG exprs.</dl>
<h3>mlir-tblgen Options</h3>
<dl>
<dt><code>-gen-avail-interface-decls</code></p>
<dd> Generate availability interface declarations.</p>
<dt><code>-gen-avail-interface-defs</code></p>
<dd> Generate op interface definitions.</p>
<dt><code>-gen-dialect-doc</code></p>
<dd> Generate dialect documentation.</p>
<dt><code>-dialect</code></p>
<dd> The dialect to generate.</p>
<dt><code>-gen-directive-decl</code></p>
<dd> Generate declarations for directives (OpenMP, etc.).</p>
<dt><code>-gen-enum-decls</code></p>
<dd> Generate enum utility declarations.</p>
<dt><code>-gen-enum-defs</code></p>
<dd> Generate enum utility definitions.</p>
<dt><code>-gen-enum-from-llvmir-conversions</code></p>
<dd> Generate conversions of EnumAttrs from LLVM IR.</p>
<dt><code>-gen-enum-to-llvmir-conversions</code></p>
<dd> Generate conversions of EnumAttrs to LLVM IR.</p>
<dt><code>-gen-llvmir-conversions</code></p>
<dd> Generate LLVM IR conversions.</p>
<dt><code>-gen-llvmir-intrinsics</code></p>
<dd> Generate LLVM IR intrinsics.</p>
<dt><code>-llvmir-intrinsics-filter</code></p>
<dd> Only keep the intrinsics with the specified substring in their record name.</p>
<dt><code>-dialect-opclass-base</code></p>
<dd> The base class for the ops in the dialect we are to emit.</p>
<dt><code>-gen-op-decls</code></p>
<dd> Generate operation declarations.</p>
<dt><code>-gen-op-defs</code></p>
<dd> Generate operation definitions.</p>
<dt><code>-asmformat-error-is-fatal</code></p>
<dd> Emit a fatal error if format parsing fails.</p>
<dt><code>-op-exclude-regex</code></p>
<dd> Regular expression of name of ops to exclude (no filter if empty).</p>
<dt><code>-op-include-regex</code></p>
<dd> Regular expression of name of ops to include (no filter if empty).</p>
<dt><code>-gen-op-doc</code></p>
<dd> Generate operation documentation.</p>
<dt><code>-gen-pass-decls</code></p>
<dd> Generate operation documentation.</p>
<dt><code>-name namestring</code></p>
<dd> The name of this group of passes.</p>
<dt><code>-gen-pass-doc</code></p>
<dd> Generate pass documentation.</p>
<dt><code>-gen-rewriters</code></p>
<dd> Generate pattern rewriters.</p>
<dt><code>-gen-spirv-avail-impls</code></p>
<dd> Generate SPIR-V operation utility definitions.</p>
<dt><code>-gen-spirv-capability-implication</code></p>
<dd> Generate utility function to return implied capabilities for a given capability.</p>
<dt><code>-gen-spirv-enum-avail-decls</code></p>
<dd> Generate SPIR-V enum availability declarations.</p>
<dt><code>-gen-spirv-enum-avail-defs</code></p>
<dd> Generate SPIR-V enum availability definitions.</p>
<dt><code>-gen-spirv-op-utils</code></p>
<dd> Generate SPIR-V operation utility definitions.</p>
<dt><code>-gen-spirv-serialization</code></p>
<dd> Generate SPIR-V (de)serialization utilities and functions.</p>
<dt><code>-gen-struct-attr-decls</code></p>
<dd> Generate struct utility declarations.</p>
<dt><code>-gen-struct-attr-defs</code></p>
<dd> Generate struct utility definitions.</p>
<dt><code>-gen-typedef-decls</code></p>
<dd> Generate TypeDef declarations.</p>
<dt><code>-gen-typedef-defs</code></p>
<dd> Generate TypeDef definitions.</p>
<dt><code>-typedefs-dialect name</code></p>
<dd> Generate types for this dialect.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>*-tblgen</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
