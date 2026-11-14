---
title: "x86_64-linux-gnu-ld-gold(1)"
name: "x86_64-linux-gnu-ld-gold"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-ld-gold/"
description: "gold – The GNU ELF linker"
---

<p>gold &#8211; The GNU ELF linker </p>
<h2>Synopsis</h2>
<p><code>ld.gold</code> [<i>,options/</i>] <i>,file/</i>&#8230;</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>&#8211;help</code></p>
<dd>Report usage information</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Report version information</p>
<dt><code>-V</code></p>
<dd>Report version and target information</p>
<dt><code>&#8211;add-needed</code></p>
<dd>Not supported</p>
<dt><code>&#8211;no-add-needed</code></p>
<dd>Do not copy DT_NEEDED tags from shared libraries (default)</p>
<dt> <code>&#8211;allow-multiple-definition</code> Allow multiple definitions of symbols</p>
<dt><code>&#8211;no-allow-multiple-definition</code></p>
<dd>
<dd>Do not allow multiple definitions (default)</p>
<dt><code>&#8211;allow-shlib-undefined</code></p>
<dd>Allow unresolved references in shared libraries</p>
<dt><code>&#8211;no-allow-shlib-undefined</code></p>
<dd>Do not allow unresolved references in shared libraries (default)</p>
<dt><code>&#8211;apply-dynamic-relocs</code></p>
<dd>Apply link-time values for dynamic relocations (default)</p>
<dt><code>&#8211;no-apply-dynamic-relocs</code></p>
<dd>(aarch64 only) Do not apply link-time values for dynamic relocations</p>
<dt><code>&#8211;as-needed</code></p>
<dd>Use DT_NEEDED only for shared libraries that are used</p>
<dt><code>&#8211;no-as-needed</code></p>
<dd>Use DT_NEEDED for all shared libraries (default)</p>
<dt><code>-assert</code> [ignored]</p>
<dd>Ignored</p>
<dt><code>-b</code> [elf,binary], <code>&#8211;format</code> [elf,binary]</p>
<dd>Set input format</p>
<dt><code>&#8211;be8</code></p>
<dd>Output BE8 format image</p>
<dt><code>&#8211;build-id</code> [=STYLE]</p>
<dd>Generate build ID note</p>
<dt><code>&#8211;build-id-chunk-size-for-treehash</code> SIZE</p>
<dd>Chunk size for &#8216;&#8211;build-id=tree&#8217;</p>
<dt><code>&#8211;build-id-min-file-size-for-treehash</code> SIZE</p>
<dd>Minimum output file size for &#8216;&#8211;build-id=tree&#8217; to work differently than &#8216;&#8211;build-id=sha1&#8217;</p>
<dt> <code>-Bdynamic</code> <code>-l</code> searches for shared libraries (default)</p>
<dt> <code>-Bstatic</code> <code>-l</code> does not search for shared libraries</p>
<dt><code>-dy</code></p>
<dd>
<dd>alias for <code>-Bdynamic</code> (default)</p>
<dt><code>-dn</code></p>
<dd>alias for <code>-Bstatic</code></p>
<dt><code>-Bgroup</code></p>
<dd>Use group name lookup rules for shared library</p>
<dt><code>-Bshareable</code></p>
<dd>Generate shared library (alias for <code>-G</code>/-shared)</p>
<dt><code>-Bno-symbolic</code></p>
<dd>Don&#8217;t bind default visibility defined symbols locally for <code>-shared</code> (default)</p>
<dt><code>-Bsymbolic-functions</code></p>
<dd>Bind default visibility defined function symbols locally for <code>-shared</code></p>
<dt><code>-Bsymbolic</code></p>
<dd>Bind default visibility defined symbols locally for <code>-shared</code></p>
<dt><code>&#8211;check-sections</code></p>
<dd>Check segment addresses for overlaps (default)</p>
<dt><code>&#8211;no-check-sections</code></p>
<dd>Do not check segment addresses for overlaps</p>
<dt><code>&#8211;compress-debug-sections</code> [none,zlib,zlib-gnu,zlib-gabi]</p>
<dd>Compress .debug_* sections in the output file</p>
<dt><code>&#8211;copy-dt-needed-entries</code></p>
<dd>Not supported</p>
<dt> <code>&#8211;no-copy-dt-needed-entries</code> Do not copy DT_NEEDED tags from shared libraries (default)</p>
<dt><code>&#8211;cref</code></p>
<dd>
<dd>Output cross reference table</p>
<dt><code>&#8211;no-cref</code></p>
<dd>Do not output cross reference table (default)</p>
<dt><code>&#8211;ctors-in-init-array</code></p>
<dd>Use DT_INIT_ARRAY for all constructors (default)</p>
<dt><code>&#8211;no-ctors-in-init-array</code></p>
<dd>Handle constructors as directed by compiler</p>
<dt><code>-d</code>, <code>&#8211;define-common</code></p>
<dd>Define common symbols</p>
<dt><code>&#8211;no-define-common</code></p>
<dd>Do not define common symbols in relocatable output (default)</p>
<dt><code>-dc</code></p>
<dd>Alias for <code>-d</code></p>
<dt><code>-dp</code></p>
<dd>Alias for <code>-d</code></p>
<dt><code>&#8211;debug</code> [all,files,script,task][,&#8230;]</p>
<dd>Turn on debugging</p>
<dt><code>&#8211;defsym</code> SYMBOL=EXPRESSION</p>
<dd>Define a symbol</p>
<dt><code>&#8211;demangle</code> [=STYLE]</p>
<dd>Demangle C++ symbols in log messages</p>
<dt><code>&#8211;no-demangle</code></p>
<dd>Do not demangle C++ symbols in log messages</p>
<dt><code>&#8211;dependency-file</code> FILE</p>
<dd>Write a dependency file listing all files read</p>
<dt><code>&#8211;detect-odr-violations</code></p>
<dd>Look for violations of the C++ One Definition Rule</p>
<dt><code>&#8211;no-detect-odr-violations</code></p>
<dd>Do not look for violations of the C++ One Definition Rule (default)</p>
<dt><code>&#8211;dynamic-list-data</code></p>
<dd>Add data symbols to dynamic symbols</p>
<dt><code>&#8211;dynamic-list-cpp-new</code></p>
<dd>Add C++ operator new/delete to dynamic symbols</p>
<dt> <code>&#8211;dynamic-list-cpp-typeinfo</code> Add C++ typeinfo to dynamic symbols</p>
<dt><code>&#8211;dynamic-list</code> FILE</p>
<dd>
<dd>Read a list of dynamic symbols</p>
<dt><code>&#8211;emit-stub-syms</code></p>
<dd>(PowerPC only) Label linker stubs with a symbol (default)</p>
<dt><code>&#8211;no-emit-stub-syms</code></p>
<dd>(PowerPC only) Do not label linker stubs with a symbol</p>
<dt> <code>-e</code> ADDRESS, <code>&#8211;entry</code> ADDRESS Set program start address</p>
<dt><code>&#8211;eh-frame-hdr</code></p>
<dd>
<dd>Create exception frame header</p>
<dt><code>&#8211;no-eh-frame-hdr</code></p>
<dd>Do not create exception frame header (default)</p>
<dt><code>&#8211;enable-new-dtags</code></p>
<dd>Enable use of DT_RUNPATH (default)</p>
<dt><code>&#8211;disable-new-dtags</code></p>
<dd>Disable use of DT_RUNPATH</p>
<dt><code>&#8211;no-enum-size-warning</code></p>
<dd>(ARM only) Do not warn about objects with incompatible enum sizes</p>
<dt><code>&#8211;exclude-libs</code> lib,lib &#8230;</p>
<dd>Exclude libraries from automatic export</p>
<dt><code>-E</code>, <code>&#8211;export-dynamic</code></p>
<dd>Export all dynamic symbols</p>
<dt><code>&#8211;no-export-dynamic</code></p>
<dd>Do not export all dynamic symbols (default)</p>
<dt><code>&#8211;export-dynamic-symbol</code> SYMBOL</p>
<dd>Export SYMBOL to dynamic symbol table</p>
<dt><code>-EB</code></p>
<dd>Link big-endian objects.</p>
<dt><code>-EL</code></p>
<dd>Link little-endian objects.</p>
<dt> <code>-f</code> SHLIB, <code>&#8211;auxiliary</code> SHLIB Auxiliary filter for shared object symbol table</p>
<dt><code>-F</code> SHLIB, <code>&#8211;filter</code> SHLIB</p>
<dd>
<dd>Filter for shared object symbol table</p>
<dt><code>&#8211;fatal-warnings</code></p>
<dd>Treat warnings as errors</p>
<dt><code>&#8211;no-fatal-warnings</code></p>
<dd>Do not treat warnings as errors (default)</p>
<dt><code>-fini</code> SYMBOL</p>
<dd>Call SYMBOL at unload-time</p>
<dt><code>&#8211;fix-arm1176</code></p>
<dd>(ARM only) Fix binaries for ARM1176 erratum (default)</p>
<dt><code>&#8211;no-fix-arm1176</code></p>
<dd>(ARM only) Do not fix binaries for ARM1176 erratum</p>
<dt><code>&#8211;fix-cortex-a8</code></p>
<dd>(ARM only) Fix binaries for Cortex-A8 erratum</p>
<dt><code>&#8211;no-fix-cortex-a8</code></p>
<dd>(ARM only) Do not fix binaries for Cortex-A8 erratum (default)</p>
<dt><code>&#8211;fix-cortex-a53-843419</code></p>
<dd>(AArch64 only) Fix Cortex-A53 erratum 843419</p>
<dt><code>&#8211;no-fix-cortex-a53-843419</code></p>
<dd>(AArch64 only) Do not fix Cortex-A53 erratum 843419 (default)</p>
<dt><code>&#8211;fix-cortex-a53-835769</code></p>
<dd>(AArch64 only) Fix Cortex-A53 erratum 835769</p>
<dt><code>&#8211;no-fix-cortex-a53-835769</code></p>
<dd>(AArch64 only) Do not fix Cortex-A53 erratum 835769 (default)</p>
<dt><code>&#8211;fix-v4bx</code></p>
<dd>(ARM only) Rewrite BX rn as MOV pc, rn for ARMv4</p>
<dt><code>&#8211;fix-v4bx-interworking</code></p>
<dd>(ARM only) Rewrite BX rn branch to ARMv4 interworking veneer</p>
<dt><code>-fuse-ld</code> [gold,bfd]</p>
<dd>Ignored for GCC linker option compatibility</p>
<dt><code>-g</code></p>
<dd>Ignored</p>
<dt><code>&#8211;gc-sections</code></p>
<dd>Remove unused sections</p>
<dt><code>&#8211;no-gc-sections</code></p>
<dd>Don&#8217;t remove unused sections (default)</p>
<dt><code>&#8211;gdb-index</code></p>
<dd>Generate .gdb_index section</p>
<dt><code>&#8211;no-gdb-index</code></p>
<dd>Do not generate .gdb_index section (default)</p>
<dt><code>&#8211;gnu-unique</code></p>
<dd>Enable STB_GNU_UNIQUE symbol binding (default)</p>
<dt><code>&#8211;no-gnu-unique</code></p>
<dd>Disable STB_GNU_UNIQUE symbol binding</p>
<dt><code>-G</code>, <code>-shared</code></p>
<dd>Generate shared library</p>
<dt><code>-h</code> FILENAME, <code>-soname</code> FILENAME</p>
<dd>Set shared library name</p>
<dt><code>&#8211;hash-bucket-empty-fraction</code> FRACTION</p>
<dd>Min fraction of empty buckets in dynamic hash</p>
<dt><code>&#8211;hash-style</code> [sysv,gnu,both]</p>
<dd>Dynamic hash style</p>
<dt><code>-i</code></p>
<dd>Alias for <code>-r</code></p>
<dt><code>&#8211;icf</code> [none,all,safe]</p>
<dd>Identical Code Folding. &#8216;&#8211;icf=safe&#8217; Folds ctors, dtors and functions whose pointers are definitely not taken</p>
<dt><code>&#8211;icf-iterations</code> COUNT</p>
<dd>Number of iterations of ICF (default 3)</p>
<dt><code>&#8211;incremental</code></p>
<dd>Do an incremental link if possible; otherwise, do a full link and prepare output for incremental linking</p>
<dt><code>&#8211;no-incremental</code></p>
<dd>Do a full link (default)</p>
<dt><code>&#8211;incremental-full</code></p>
<dd>Do a full link and prepare output for incremental linking</p>
<dt><code>&#8211;incremental-update</code></p>
<dd>Do an incremental link; exit if not possible</p>
<dt><code>&#8211;incremental-base</code> FILE</p>
<dd>Set base file for incremental linking (default is output file)</p>
<dt><code>&#8211;incremental-changed</code></p>
<dd>Assume files changed</p>
<dt><code>&#8211;incremental-unchanged</code></p>
<dd>Assume files didn&#8217;t change</p>
<dt><code>&#8211;incremental-unknown</code></p>
<dd>Use timestamps to check files (default)</p>
<dt><code>&#8211;incremental-startup-unchanged</code></p>
<dd>Assume startup files unchanged (files preceding this option)</p>
<dt> <code>&#8211;incremental-patch</code> PERCENT Amount of extra space to allocate for patches (default 10)</p>
<dt><code>-init</code> SYMBOL</p>
<dd>
<dd>Call SYMBOL at load-time</p>
<dt><code>-I</code> PROGRAM, <code>&#8211;dynamic-linker</code> PROGRAM</p>
<dd>Set dynamic linker path</p>
<dt><code>&#8211;just-symbols</code> FILE</p>
<dd>Read only symbol values from FILE</p>
<dt><code>&#8211;keep-files-mapped</code></p>
<dd>Keep files mapped across passes (default)</p>
<dt><code>&#8211;no-keep-files-mapped</code></p>
<dd>Release mapped files after each pass</p>
<dt><code>&#8211;keep-unique</code> SYMBOL</p>
<dd>Do not fold this symbol during ICF</p>
<dt><code>-l</code> LIBNAME, <code>&#8211;library</code> LIBNAME</p>
<dd>Search for library LIBNAME</p>
<dt><code>&#8211;ld-generated-unwind-info</code></p>
<dd>Generate unwind information for PLT (default)</p>
<dt><code>&#8211;no-ld-generated-unwind-info</code></p>
<dd>Do not generate unwind information for PLT</p>
<dt><code>-L</code> DIR, <code>&#8211;library-path</code> DIR</p>
<dd>Add directory to search path</p>
<dt><code>&#8211;long-plt</code></p>
<dd>(ARM only) Generate long PLT entries</p>
<dt><code>&#8211;no-long-plt</code></p>
<dd>(ARM only) Do not generate long PLT entries (default)</p>
<dt><code>-m</code> EMULATION</p>
<dd>Set GNU linker emulation; obsolete</p>
<dt><code>&#8211;map-whole-files</code></p>
<dd>Map whole files to memory (default)</p>
<dt><code>&#8211;no-map-whole-files</code></p>
<dd>Map relevant file parts to memory</p>
<dt><code>&#8211;merge-exidx-entries</code></p>
<dd>(ARM only) Merge exidx entries in debuginfo (default)</p>
<dt><code>&#8211;no-merge-exidx-entries</code></p>
<dd>(ARM only) Do not merge exidx entries in debuginfo</p>
<dt><code>&#8211;mmap-output-file</code></p>
<dd>Map the output file for writing (default)</p>
<dt><code>&#8211;no-mmap-output-file</code></p>
<dd>Do not map the output file for writing</p>
<dt><code>-M</code>, <code>&#8211;print-map</code></p>
<dd>Write map file on standard output</p>
<dt><code>-Map</code> MAPFILENAME</p>
<dd>Write map file</p>
<dt><code>-n</code>, <code>&#8211;nmagic</code></p>
<dd>Do not page align data</p>
<dt><code>-N</code>, <code>&#8211;omagic</code></p>
<dd>Do not page align data, do not make text readonly</p>
<dt><code>&#8211;no-omagic</code></p>
<dd>Page align data, make text readonly (default)</p>
<dt><code>&#8211;no-keep-memory</code></p>
<dd>Use less memory and more disk I/O (included only for compatibility with GNU ld)</p>
<dt><code>&#8211;no-undefined</code></p>
<dd>Report undefined symbols (even with <code>&#8211;shared</code>)</p>
<dt><code>&#8211;noinhibit-exec</code></p>
<dd>Create an output file even if errors occur</p>
<dt><code>-nostdlib</code></p>
<dd>Only search directories specified on the command line</p>
<dt><code>-o</code> FILE, <code>&#8211;output</code> FILE</p>
<dd>Set output file name</p>
<dt><code>&#8211;oformat</code> [binary]</p>
<dd>Set output format</p>
<dt><code>-O</code> LEVEL, <code>-optimize</code> LEVEL</p>
<dd>Optimize output file size</p>
<dt><code>&#8211;orphan-handling</code> [place,discard,warn,error]</p>
<dd>Orphan section handling</p>
<dt><code>-p</code></p>
<dd>Ignored for ARM compatibility</p>
<dt><code>-pie</code></p>
<dd>Create a position independent executable</p>
<dt><code>-no-pie</code></p>
<dd>Do not create a position independent executable (default)</p>
<dt><code>&#8211;pic-executable</code></p>
<dd>Create a position independent executable</p>
<dt><code>&#8211;no-pic-executable</code></p>
<dd>Do not create a position independent executable (default)</p>
<dt><code>&#8211;pic-veneer</code></p>
<dd>Force PIC sequences for ARM/Thumb interworking veneers</p>
<dt><code>-no-pipeline-knowledge</code></p>
<dd>(ARM only) Ignore for backward compatibility (default)</p>
<dt><code>&#8211;plt-align</code> [=P2ALIGN]</p>
<dd>(PowerPC only) Align PLT call stubs to fit cache lines</p>
<dt><code>&#8211;plt-localentry</code></p>
<dd>(PowerPC64 only) Optimize calls to ELFv2 localentry:0 functions</p>
<dt><code>&#8211;no-plt-localentry</code></p>
<dd>(PowerPC64 only) Don&#8217;t optimize ELFv2 calls (default)</p>
<dt><code>&#8211;plt-static-chain</code></p>
<dd>(PowerPC64 only) PLT call stubs should load r11</p>
<dt><code>&#8211;no-plt-static-chain</code></p>
<dd>(PowerPC64 only) PLT call stubs should not load r11 (default)</p>
<dt><code>&#8211;plt-thread-safe</code></p>
<dd>(PowerPC64 only) PLT call stubs with load-load barrier</p>
<dt><code>&#8211;no-plt-thread-safe</code></p>
<dd>(PowerPC64 only) PLT call stubs without barrier (default)</p>
<dt><code>&#8211;plugin</code> PLUGIN</p>
<dd>Load a plugin library</p>
<dt><code>&#8211;plugin-opt</code> OPTION</p>
<dd>Pass an option to the plugin</p>
<dt><code>&#8211;posix-fallocate</code></p>
<dd>Use posix_fallocate to reserve space in the output file (default)</p>
<dt><code>&#8211;no-posix-fallocate</code></p>
<dd>Use fallocate or ftruncate to reserve space</p>
<dt><code>&#8211;power10-stubs</code> [=auto,no,yes]</p>
<dd>(PowerPC64 only) stubs use power10 insns</p>
<dt><code>&#8211;no-power10-stubs</code></p>
<dd>(PowerPC64 only) stubs do not use power10 insns</p>
<dt><code>&#8211;preread-archive-symbols</code></p>
<dd>Preread archive symbols when multi-threaded</p>
<dt><code>&#8211;print-gc-sections</code></p>
<dd>List removed unused sections on stderr</p>
<dt><code>&#8211;no-print-gc-sections</code></p>
<dd>Do not list removed unused sections (default)</p>
<dt><code>&#8211;print-icf-sections</code></p>
<dd>List folded identical sections on stderr</p>
<dt><code>&#8211;no-print-icf-sections</code></p>
<dd>Do not list folded identical sections (default)</p>
<dt><code>&#8211;print-output-format</code></p>
<dd>Print default output format</p>
<dt><code>&#8211;print-symbol-counts</code> FILENAME</p>
<dd>Print symbols defined and used for each input</p>
<dt><code>&#8211;push-state</code></p>
<dd>Save the state of flags related to input files</p>
<dt><code>&#8211;pop-state</code></p>
<dd>Restore the state of flags related to input files</p>
<dt><code>-q</code>, <code>&#8211;emit-relocs</code></p>
<dd>Generate relocations in output</p>
<dt><code>-Qy</code></p>
<dd>Ignored for SVR4 compatibility</p>
<dt><code>-r</code>, <code>-relocatable</code></p>
<dd>Generate relocatable output</p>
<dt><code>&#8211;relax</code></p>
<dd>Relax branches on certain targets</p>
<dt><code>&#8211;no-relax</code></p>
<dd>Do not relax branches (default)</p>
<dt><code>&#8211;retain-symbols-file</code> FILE</p>
<dd>keep only symbols listed in this file</p>
<dt><code>&#8211;rosegment</code></p>
<dd>Put read-only non-executable sections in their own segment</p>
<dt><code>&#8211;no-rosegment</code></p>
<dd>Do not put read-only non-executable sections in their own segment (default)</p>
<dt><code>&#8211;rosegment-gap</code> OFFSET</p>
<dd>Set offset between executable and read-only segments</p>
<dt><code>-R</code> DIR</p>
<dd>Add DIR to runtime search path</p>
<dt><code>-rpath</code> DIR</p>
<dd>Add DIR to runtime search path</p>
<dt><code>&#8211;rpath-link</code> DIR</p>
<dd>Add DIR to link time shared library search path</p>
<dt><code>-s</code>, <code>&#8211;strip-all</code></p>
<dd>Strip all symbols</p>
<dt><code>-S</code>, <code>&#8211;strip-debug</code></p>
<dd>Strip debugging information</p>
<dt><code>&#8211;strip-debug-non-line</code></p>
<dd>Emit only debug line number information</p>
<dt><code>&#8211;strip-debug-gdb</code></p>
<dd>Strip debug symbols that are unused by gdb (at least versions &lt;= 7.4)</p>
<dt><code>&#8211;strip-lto-sections</code></p>
<dd>Strip LTO intermediate code sections (default)</p>
<dt><code>&#8211;section-ordering-file</code> FILENAME</p>
<dd>Layout sections in the order specified</p>
<dt><code>&#8211;section-start</code> SECTION=ADDRESS</p>
<dd>Set address of section</p>
<dt><code>&#8211;secure-plt</code></p>
<dd>(PowerPC only) Use new-style PLT (default)</p>
<dt><code>&#8211;sort-common</code> [={ascending,descending}]</p>
<dd>Sort common symbols by alignment</p>
<dt><code>&#8211;sort-section</code> [none,name]</p>
<dd>Sort sections by name. &#8216;&#8211;no-text-reorder&#8217; will override &#8216;&#8211;sort-section=name&#8217; for .text</p>
<dt><code>&#8211;spare-dynamic-tags</code> COUNT</p>
<dd>Dynamic tag slots to reserve (default 5)</p>
<dt><code>&#8211;stub-group-size</code> SIZE</p>
<dd>(ARM, PowerPC only) The maximum distance from instructions in a group of sections to their stubs. Negative values mean stubs are always after the group. 1 means use default size</p>
<dt><code>&#8211;stub-group-multi</code></p>
<dd>(PowerPC only) Allow a group of stubs to serve multiple output sections (default)</p>
<dt><code>&#8211;no-stub-group-multi</code></p>
<dd>(PowerPC only) Each output section has its own stubs</p>
<dt><code>&#8211;split-stack-adjust-size</code> SIZE</p>
<dd>Stack size when <code>-fsplit-stack</code> function calls non-split</p>
<dt><code>-static</code></p>
<dd>Do not link against shared libraries</p>
<dt><code>&#8211;start-lib</code></p>
<dd>Start a library</p>
<dt><code>&#8211;end-lib</code></p>
<dd>End a library</p>
<dt><code>&#8211;stats</code></p>
<dd>Print resource usage statistics</p>
<dt><code>&#8211;sysroot</code> DIR</p>
<dd>Set target system root directory</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd>Print the name of each input file</p>
<dt><code>&#8211;target1-abs</code></p>
<dd>(ARM only) Force R_ARM_TARGET1 type to R_ARM_ABS32</p>
<dt><code>&#8211;target1-rel</code></p>
<dd>(ARM only) Force R_ARM_TARGET1 type to R_ARM_REL32</p>
<dt><code>&#8211;target2</code> [rel, abs, got-rel</p>
<dd>(ARM only) Set R_ARM_TARGET2 relocation type</p>
<dt><code>&#8211;text-reorder</code></p>
<dd>Enable text section reordering for GCC section names (default)</p>
<dt><code>&#8211;no-text-reorder</code></p>
<dd>Disable text section reordering for GCC section names</p>
<dt><code>&#8211;threads</code></p>
<dd>Run the linker multi-threaded</p>
<dt><code>&#8211;no-threads</code></p>
<dd>Do not run the linker multi-threaded (default)</p>
<dt><code>&#8211;thread-count</code> COUNT</p>
<dd>Number of threads to use</p>
<dt><code>&#8211;thread-count-initial</code> COUNT</p>
<dd>Number of threads to use in initial pass</p>
<dt> <code>&#8211;thread-count-middle</code> COUNT Number of threads to use in middle pass</p>
<dt><code>&#8211;thread-count-final</code> COUNT</p>
<dd>
<dd>Number of threads to use in final pass</p>
<dt><code>&#8211;tls-optimize</code></p>
<dd>(PowerPC/64 only) Optimize GD/LD/IE code to IE/LE (default)</p>
<dt><code>&#8211;no-tls-optimize</code></p>
<dd>(PowerPC/64 only) Don&#8221;&#8217;t try to optimize TLS accesses</p>
<dt><code>&#8211;tls-get-addr-optimize</code></p>
<dd>(PowerPC/64 only) Use a special __tls_get_addr call (default)</p>
<dt><code>&#8211;no-tls-get-addr-optimize</code></p>
<dd>(PowerPC/64 only) Don&#8217;t use a special __tls_get_addr call</p>
<dt><code>&#8211;toc-optimize</code></p>
<dd>(PowerPC64 only) Optimize TOC code sequences (default)</p>
<dt><code>&#8211;no-toc-optimize</code></p>
<dd>(PowerPC64 only) Don&#8217;t optimize TOC code sequences</p>
<dt><code>&#8211;toc-sort</code></p>
<dd>(PowerPC64 only) Sort TOC and GOT sections (default)</p>
<dt><code>&#8211;no-toc-sort</code></p>
<dd>(PowerPC64 only) Don&#8217;t sort TOC and GOT sections</p>
<dt><code>-T</code> FILE, <code>&#8211;script</code> FILE</p>
<dd>Read linker script</p>
<dt><code>-Tbss</code> ADDRESS</p>
<dd>Set the address of the bss segment</p>
<dt><code>-Tdata</code> ADDRESS</p>
<dd>Set the address of the data segment</p>
<dt><code>-Ttext</code> ADDRESS</p>
<dd>Set the address of the text segment</p>
<dt><code>-Ttext-segment</code> ADDRESS</p>
<dd>Set the address of the text segment</p>
<dt><code>-Trodata-segment</code> ADDRESS</p>
<dd>Set the address of the rodata segment</p>
<dt><code>-u</code> SYMBOL, <code>&#8211;undefined</code> SYMBOL</p>
<dd>Create undefined reference to SYMBOL</p>
<dt><code>&#8211;unresolved-symbols</code> ignore-all,report-all,ignore-in-object-files,ignore-in-shared-libs</p>
<dd>How to handle unresolved symbols</p>
<dt><code>&#8211;verbose</code></p>
<dd>Alias for <code>&#8211;debug</code>=<i>,files/</i></p>
<dt><code>&#8211;version-script</code> FILE</p>
<dd>Read version script</p>
<dt><code>&#8211;warn-common</code></p>
<dd>Warn about duplicate common symbols</p>
<dt><code>&#8211;no-warn-common</code></p>
<dd>Do not warn about duplicate common symbols (default)</p>
<dt><code>&#8211;warn-constructors</code></p>
<dd>Ignored</p>
<dt><code>&#8211;no-warn-constructors</code></p>
<dd>Ignored</p>
<dt><code>&#8211;warn-drop-version</code></p>
<dd>Warn when discarding version information</p>
<dt><code>&#8211;no-warn-drop-version</code></p>
<dd>Do not warn when discarding version information (default)</p>
<dt><code>&#8211;warn-execstack</code></p>
<dd>Warn if the stack is executable</p>
<dt><code>&#8211;no-warn-execstack</code></p>
<dd>Do not warn if the stack is executable (default)</p>
<dt><code>&#8211;no-warn-mismatch</code></p>
<dd>Don&#8217;t warn about mismatched input files</p>
<dt><code>&#8211;warn-multiple-gp</code></p>
<dd>Ignored</p>
<dt><code>&#8211;warn-search-mismatch</code></p>
<dd>Warn when skipping an incompatible library (default)</p>
<dt><code>&#8211;no-warn-search-mismatch</code></p>
<dd>Don&#8217;t warn when skipping an incompatible library</p>
<dt><code>&#8211;warn-shared-textrel</code></p>
<dd>Warn if text segment is not shareable</p>
<dt><code>&#8211;no-warn-shared-textrel</code></p>
<dd>Do not warn if text segment is not shareable (default)</p>
<dt><code>&#8211;warn-unresolved-symbols</code></p>
<dd>Report unresolved symbols as warnings</p>
<dt><code>&#8211;error-unresolved-symbols</code></p>
<dd>Report unresolved symbols as errors (default)</p>
<dt><code>-z</code> buildd</p>
<dd>Dummy z option</p>
<dt><code>&#8211;no-wchar-size-warning</code></p>
<dd>(ARM only) Do not warn about objects with incompatible wchar_t sizes</p>
<dt><code>&#8211;weak-unresolved-symbols</code></p>
<dd>Convert unresolved symbols to weak references</p>
<dt><code>&#8211;whole-archive</code></p>
<dd>Include all archive contents</p>
<dt><code>&#8211;no-whole-archive</code></p>
<dd>Include only needed archive contents (default)</p>
<dt><code>&#8211;wrap</code> SYMBOL</p>
<dd>Use wrapper functions for SYMBOL</p>
<dt><code>-x</code>, <code>&#8211;discard-all</code></p>
<dd>Delete all local symbols</p>
<dt><code>-X</code>, <code>&#8211;discard-locals</code></p>
<dd>Delete all temporary local symbols</p>
<dt><code>&#8211;discard-none</code></p>
<dd>Keep all local symbols</p>
<dt><code>-y</code> SYMBOL, <code>&#8211;trace-symbol</code> SYMBOL</p>
<dd>Trace references to symbol</p>
<dt><code>&#8211;undefined-version</code></p>
<dd>Allow unused version in script (default)</p>
<dt><code>&#8211;no-undefined-version</code></p>
<dd>Do not allow unused version in script</p>
<dt><code>-Y</code> PATH</p>
<dd>Default search path for Solaris compatibility</p>
<dt>-(, <code>&#8211;start-group</code></p>
<dd>Start a library search group</p>
<dt>-), <code>&#8211;end-group</code></p>
<dd>End a library search group</p>
<dt><code>-z</code> bndplt</p>
<dd>(x86-64 only) Generate a BND PLT for Intel MPX</p>
<dt><code>-z</code> nobndplt</p>
<dd>Generate a regular PLT (default)</p>
<dt><code>-z</code> combreloc</p>
<dd>Sort dynamic relocs (default)</p>
<dt><code>-z</code> nocombreloc</p>
<dd>Do not sort dynamic relocs</p>
<dt><code>-z</code> common-page-size=SIZE</p>
<dd>Set common page size to SIZE</p>
<dt><code>-z</code> defs</p>
<dd>Report undefined symbols (even with <code>&#8211;shared</code>)</p>
<dt><code>-z</code> execstack</p>
<dd>Mark output as requiring executable stack</p>
<dt><code>-z</code> global</p>
<dd>Make symbols in DSO available for subsequently loaded objects</p>
<dt><code>-z</code> initfirst</p>
<dd>Mark DSO to be initialized first at runtime</p>
<dt><code>-z</code> interpose</p>
<dd>Mark object to interpose all DSOs but executable</p>
<dt><code>-z</code> unique</p>
<dd>Mark DSO to be loaded at most once, and only in the main namespace</p>
<dt><code>-z</code> nounique</p>
<dd>Do not mark the DSO as one to be loaded only in the main namespace (default)</p>
<dt><code>-z</code> lazy</p>
<dd>Mark object for lazy runtime binding (default)</p>
<dt><code>-z</code> loadfltr</p>
<dd>Mark object requiring immediate process</p>
<dt><code>-z</code> max-page-size=SIZE</p>
<dd>Set maximum page size to SIZE</p>
<dt><code>-z</code> muldefs</p>
<dd>Allow multiple definitions of symbols</p>
<dt><code>-z</code> nocopyreloc</p>
<dd>Do not create copy relocs</p>
<dt><code>-z</code> nodefaultlib</p>
<dd>Mark object not to use default search paths</p>
<dt><code>-z</code> nodelete</p>
<dd>Mark DSO non-deletable at runtime</p>
<dt><code>-z</code> nodlopen</p>
<dd>Mark DSO not available to dlopen</p>
<dt><code>-z</code> nodump</p>
<dd>Mark DSO not available to dldump</p>
<dt><code>-z</code> noexecstack</p>
<dd>Mark output as not requiring executable stack</p>
<dt><code>-z</code> now</p>
<dd>Mark object for immediate function binding</p>
<dt><code>-z</code> origin</p>
<dd>Mark DSO to indicate that needs immediate $ORIGIN processing at runtime</p>
<dt><code>-z</code> relro</p>
<dd>Where possible mark variables read-only after relocation (default)</p>
<dt><code>-z</code> norelro</p>
<dd>Don&#8217;t mark variables read-only after relocation</p>
<dt><code>-z</code> stack-size=SIZE</p>
<dd>Set PT_GNU_STACK segment p_memsz to SIZE</p>
<dt><code>-z</code> start-stop-visibility=[default,internal,hidden,protected]</p>
<dd>ELF symbol visibility for synthesized __start_* and __stop_* symbols</p>
<dt><code>-z</code> text</p>
<dd>Do not permit relocations in read-only segments</p>
<dt><code>-z</code> notext</p>
<dd>Permit relocations in read-only segments (default)</p>
<dt><code>-z</code> textoff</p>
<dd>Permit relocations in read-only segments (default)</p>
<dt><code>-z</code> text-unlikely-segment</p>
<dd>Move .text.unlikely sections to a separate segment.</p>
<dt><code>-z</code> notext-unlikely-segment</p>
<dd>Do not move .text.unlikely sections to a separate segment. (default)</p>
<dt> <code>-z</code> keep-text-section-prefix Keep .text.hot, .text.startup, .text.exit and .text.unlikely as separate sections in the final binary.</p>
<dt><code>-z</code> nokeep-text-section-prefix</p>
<dd>
<dd>Merge all .text.* prefix sections. (default)</dl>
<p> debian/tmp/usr/bin/ld.gold: supported targets: elf32-x86-64 elf32-x86-64-freebsd elf32-x86-64-nacl elf64-x86-64 elf64-x86-64-freebsd elf64-x86-64-nacl elf32-iamcu elf32-i386 elf32-i386-freebsd elf32-i386-nacl debian/tmp/usr/bin/ld.gold: supported emulations: elf32_x86_64 elf32_x86_64_nacl elf_x86_64 elf_x86_64_nacl elf_iamcu elf_i386 elf_i386_nacl</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="https://sourceware.org/bugzilla/">https://sourceware.org/bugzilla/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2022 Free Software Foundation, Inc. This program is free software; you may redistribute it under the terms of the GNU General Public License version 3 or (at your option) a later version. This program has absolutely no warranty.</p>
