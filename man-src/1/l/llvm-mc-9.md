---
title: "llvm-mc-9(1)"
name: "llvm-mc-9"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-mc-9/"
description: "llvm-mc – manual page for llvm-mc 9"
---

<h2 class="name">NAME</h2>
<p> llvm-mc &#8211; manual page for llvm-mc 9 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm machine code playground </p>
<p> USAGE: llvm-mc [options] &lt;input file&gt; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dt></dl>
<dd>General options:</dd>
<dl>
<dt> <code>-I=</code>&lt;directory&gt; &#8211; Directory of include files</dt>
<dt> <code>&#8211;aarch64-neon-syntax=</code>&lt;value&gt; &#8211; Choose style of NEON code to emit from AArch64 backend:</dt>
<dt>=generic</dt>
<dd> &#8211; Emit generic NEON assembly</dd>
<dt>=apple</dt>
<dd> &#8211; Emit Apple-style NEON assembly</dd>
<dt> <code>&#8211;amdgpu-disable-loop-alignment</code> &#8211; Do not align and prefetch loops</dt>
<dt> <code>&#8211;amdgpu-disable-power-sched</code> &#8211; Disable scheduling to minimize mAI power bursts</dt>
<dt> <code>&#8211;amdgpu-dpp-combine</code> &#8211; Enable DPP combiner</dt>
<dt> <code>&#8211;amdgpu-dump-hsa-metadata</code> &#8211; Dump AMDGPU HSA Metadata</dt>
<dt> <code>&#8211;amdgpu-enable-global-sgpr-addr</code> &#8211; Enable use of SGPR regs for GLOBAL LOAD/STORE instructions</dt>
<dt> <code>&#8211;amdgpu-enable-merge-m0</code> &#8211; Merge and hoist M0 initializations</dt>
<dt> <code>&#8211;amdgpu-sdwa-peephole</code> &#8211; Enable SDWA peepholer</dt>
<dt> <code>&#8211;amdgpu-spill-sgpr-to-smem</code> &#8211; Use scalar stores to spill SGPRs if supported by subtarget</dt>
<dt> <code>&#8211;amdgpu-verify-hsa-metadata</code> &#8211; Verify AMDGPU HSA Metadata</dt>
<dt> <code>&#8211;amdgpu-vgpr-index-mode</code> &#8211; Use GPR indexing mode instead of movrel for vector indexing</dt>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; Target arch to assemble for, see <code>-version</code> for available targets</dt>
<dt> <code>&#8211;arm-add-build-attributes</code> &#8211;</dt>
<dt> <code>&#8211;arm-implicit-it=</code>&lt;value&gt; &#8211; Allow conditional instructions outdside of an IT block</dt>
<dt>=always</dt>
<dd> &#8211; Accept in both ISAs, emit implicit ITs in Thumb</dd>
<dt>=never</dt>
<dd> &#8211; Warn in ARM, reject in Thumb</dd>
<dt>=arm</dt>
<dd> &#8211; Accept in ARM, reject in Thumb</dd>
<dt>=thumb</dt>
<dd> &#8211; Warn in ARM, emit implicit ITs in Thumb</dd>
<dt> <code>&#8211;asm-show-inst</code> &#8211; Emit internal instruction representation to assembly file</dt>
<dt><code>&#8211;atomic-counter-update-promoted</code> &#8211; Do counter update using atomic fetch add</dt>
<dd>
</dd><dd>for promoted counters only</dd>
<dt> <code>&#8211;bounds-checking-single-trap</code> &#8211; Use one trap block per function</dt>
<dt> <code>&#8211;compress-debug-sections=</code>&lt;value&gt; &#8211; Choose DWARF debug sections compression:</dt>
<dt>=none</dt>
<dd> &#8211; No compression</dd>
<dt>=zlib</dt>
<dd> &#8211; Use zlib compression</dd>
<dt>=zlib-gnu</dt>
<dd> &#8211; Use zlib-gnu compression (deprecated)</dd>
<dt> <code>&#8211;cost-kind=</code>&lt;value&gt; &#8211; Target cost kind</dt>
<dt>=throughput</dt>
<dd> &#8211; Reciprocal throughput</dd>
<dt>=latency</dt>
<dd> &#8211; Instruction latency</dd>
<dt>=code-size</dt>
<dd> &#8211; Code size</dd>
<dt> <code>&#8211;cvp-dont-add-nowrap-flags</code> &#8211;</dt>
<dt> <code>&#8211;defsym=</code>&lt;string&gt; &#8211; Defines a symbol to be an integer constant</dt>
<dt> <code>&#8211;disable-promote-alloca-to-lds</code> &#8211; Disable promote alloca to LDS</dt>
<dt> <code>&#8211;disable-promote-alloca-to-vector</code> &#8211; Disable promote alloca to vector</dt>
<dd>Action to perform:</dd>
<dt> <code>&#8211;as-lex</code> &#8211; Lex tokens from a .s file</dt>
<dt> <code>&#8211;assemble</code> &#8211; Assemble a .s file (default)</dt>
<dt> <code>&#8211;disassemble</code> &#8211; Disassemble strings of hex bytes</dt>
<dt> <code>&#8211;mdis</code> &#8211; Marked up disassembly of strings of hex bytes</dt>
<dt> <code>&#8211;do-counter-promotion</code> &#8211; Do counter register promotion</dt>
<dt> <code>&#8211;dwarf-version=</code>&lt;int&gt; &#8211; Dwarf version</dt>
<dt> <code>&#8211;emscripten-cxx-exceptions-whitelist=</code>&lt;string&gt; &#8211; The list of function names in which Emscripten-style exception handling is enabled (see emscripten EMSCRIPTEN_CATCHING_WHITELIST options)</dt>
<dt> <code>&#8211;enable-cse-in-irtranslator</code> &#8211; Should enable CSE in irtranslator</dt>
<dt> <code>&#8211;enable-cse-in-legalizer</code> &#8211; Should enable CSE in Legalizer</dt>
<dt> <code>&#8211;enable-emscripten-cxx-exceptions</code> &#8211; WebAssembly Emscripten-style exception handling</dt>
<dt> <code>&#8211;enable-emscripten-sjlj</code> &#8211; WebAssembly Emscripten-style setjmp/longjmp handling</dt>
<dt> <code>&#8211;enable-gvn-memdep</code> &#8211;</dt>
<dt> <code>&#8211;enable-load-pre</code> &#8211;</dt>
<dt> <code>&#8211;enable-loop-simplifycfg-term-folding</code> &#8211;</dt>
<dt> <code>&#8211;enable-name-compression</code> &#8211; Enable name string compression</dt>
<dt> <code>&#8211;expensive-combines</code> &#8211; Enable expensive instruction combines</dt>
<dt> <code>&#8211;fatal-warnings</code> &#8211; Treat warnings as errors</dt>
<dt> <code>&#8211;fdebug-compilation-dir=</code>&lt;string&gt; &#8211; Specifies the debug info&#8217;s compilation dir</dt>
<dt> <code>&#8211;fdebug-prefix-map=</code>&lt;= separated key-value pairs&gt; &#8211; Map file source paths in debug info</dt>
<dt> <code>&#8211;filetype=</code>&lt;value&gt; &#8211; Choose an output file type:</dt>
<dt>=asm</dt>
<dd> &#8211; Emit an assembly (&#8216;.s&#8217;) file</dd>
<dt>=null</dt>
<dd> &#8211; Don&#8217;t emit anything (for timing purposes)</dd>
<dt>=obj</dt>
<dd> &#8211; Emit a native object (&#8216;.o&#8217;) file</dd>
<dt> <code>-g</code> &#8211; Generate dwarf debugging info for assembly source files</dt>
<dt><code>&#8211;gpsize=</code>&lt;uint&gt; &#8211; Global Pointer Addressing Size.</dt>
<dd>
</dd><dd>The default size is 8.</dd>
<dt> <code>&#8211;hash-based-counter-split</code> &#8211; Rename counter variable of a comdat function based on cfg hash</dt>
<dt> <code>&#8211;import-all-index</code> &#8211; Import all external functions in index.</dt>
<dt> <code>&#8211;incremental-linker-compatible</code> &#8211; When used with filetype=obj, emit an object file which can be used with an incremental linker</dt>
<dt> <code>&#8211;instcombine-code-sinking</code> &#8211; Enable code sinking</dt>
<dt> <code>&#8211;instcombine-guard-widening-window=</code>&lt;uint&gt; &#8211; How wide an instruction window to bypass looking for another guard</dt>
<dt> <code>&#8211;instcombine-max-num-phis=</code>&lt;uint&gt; &#8211; Maximum number phis to handle in intptr/ptrint folding</dt>
<dt> <code>&#8211;instcombine-maxarray-size=</code>&lt;uint&gt; &#8211; Maximum array size considered when doing a combine</dt>
<dt> <code>&#8211;instrprof-atomic-counter-update-all</code> &#8211; Make all profile counter updates atomic (for testing only)</dt>
<dt> <code>&#8211;internalize-public-api-file=</code>&lt;filename&gt; &#8211; A file containing list of symbol names to preserve</dt>
<dt> <code>&#8211;internalize-public-api-list=</code>&lt;list&gt; &#8211; A list of symbol names to preserve</dt>
<dt> <code>&#8211;iterative-counter-promotion</code> &#8211; Allow counter promotion across the whole loop nest.</dt>
<dt> <code>&#8211;large-code-model</code> &#8211; Create cfi directives that assume the code might be more than 2gb away</dt>
<dt> <code>&#8211;lto-pass-remarks-filter=</code>&lt;regex&gt; &#8211; Only record optimization remarks from passes whose names match the given regular expression</dt>
<dt> <code>&#8211;lto-pass-remarks-format=</code>&lt;format&gt; &#8211; The format used for serializing remarks (default: YAML)</dt>
<dt> <code>&#8211;lto-pass-remarks-output=</code>&lt;filename&gt; &#8211; Output filename for pass remarks</dt>
<dt> <code>&#8211;main-file-name=</code>&lt;string&gt; &#8211; Specifies the name we should consider the input file</dt>
<dt> <code>&#8211;masm-integers</code> &#8211; Enable binary and hex masm integers (0b110 and 0ABCh)</dt>
<dt> <code>&#8211;mattr=</code>&lt;a1,+a2,-a3,&#8230;&gt; &#8211; Target specific attributes (<code>-mattr</code>=<i>,help/</i> for details)</dt>
<dt> <code>&#8211;max-counter-promotions=</code>&lt;int&gt; &#8211; Max number of allowed counter promotions</dt>
<dt> <code>&#8211;max-counter-promotions-per-loop=</code>&lt;uint&gt; &#8211; Max number counter promotions per loop to avoid increasing register pressure too much</dt>
<dt> <code>&#8211;mc-relax-all</code> &#8211; When used with filetype=obj, relax all fixups in the emitted object file</dt>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</dt>
<dt> <code>&#8211;memop-size-large=</code>&lt;uint&gt; &#8211; Set large value thresthold in memory intrinsic size profiling. Value of 0 disables the large value profiling.</dt>
<dt> <code>&#8211;memop-size-range=</code>&lt;string&gt; &#8211; Set the range of size in memory intrinsic calls to be profiled precisely, in a format of &lt;start_val&gt;:&lt;end_val&gt;</dt>
<dt> <code>&#8211;merror-missing-parenthesis</code> &#8211; Error for missing parenthesis around predicate registers</dt>
<dt> <code>&#8211;merror-noncontigious-register</code> &#8211; Error for register names that aren&#8217;t contigious</dt>
<dt> <code>&#8211;mhvx</code> &#8211; Enable Hexagon Vector eXtensions</dt>
<dt> <code>&#8211;mhvx=</code>&lt;value&gt; &#8211; Enable Hexagon Vector eXtensions</dt>
<dt>=v60</dt>
<dd> &#8211; Build for HVX v60</dd>
<dt>=v62</dt>
<dd> &#8211; Build for HVX v62</dd>
<dt>=v65</dt>
<dd> &#8211; Build for HVX v65</dd>
<dt>=v66</dt>
<dd> &#8211; Build for HVX v66</dd>
<dt> <code>&#8211;mips-compact-branches=</code>&lt;value&gt; &#8211; MIPS Specific: Compact branch policy.</dt>
<dt>=never</dt>
<dd> &#8211; Do not use compact branches if possible.</dd>
<dt>=optimal</dt>
<dd> &#8211; Use compact branches where appropiate (default).</dd>
<dt>=always</dt>
<dd> &#8211; Always use compact branches if possible.</dd>
<dt> <code>&#8211;mips16-constant-islands</code> &#8211; Enable mips16 constant islands.</dt>
<dt> <code>&#8211;mips16-hard-float</code> &#8211; Enable mips16 hard float.</dt>
<dt> <code>&#8211;mno-compound</code> &#8211; Disable looking for compound instructions for Hexagon</dt>
<dt> <code>&#8211;mno-fixup</code> &#8211; Disable fixing up resolved relocations for Hexagon</dt>
<dt> <code>&#8211;mno-ldc1-sdc1</code> &#8211; Expand double precision loads and stores to their single precision counterparts</dt>
<dt> <code>&#8211;mno-pairing</code> &#8211; Disable looking for duplex instructions for Hexagon</dt>
<dt> <code>&#8211;mwarn-missing-parenthesis</code> &#8211; Warn for missing parenthesis around predicate registers</dt>
<dt> <code>&#8211;mwarn-noncontigious-register</code> &#8211; Warn for register names that arent contigious</dt>
<dt> <code>&#8211;mwarn-sign-mismatch</code> &#8211; Warn for mismatching a signed and unsigned value</dt>
<dt> <code>-n</code> &#8211; Don&#8217;t assume assembly file starts in the text section</dt>
<dt> <code>&#8211;no-deprecated-warn</code> &#8211; Suppress all deprecated warnings</dt>
<dt> <code>&#8211;no-discriminators</code> &#8211; Disable generation of discriminator information.</dt>
<dt> <code>&#8211;no-exec-stack</code> &#8211; File doesn&#8217;t need an exec stack</dt>
<dt> <code>&#8211;no-warn</code> &#8211; Suppress all warnings</dt>
<dt> <code>&#8211;nvptx-sched4reg</code> &#8211; NVPTX Specific: schedule for register pressue</dt>
<dt> <code>-o=</code>&lt;filename&gt; &#8211; Output filename</dt>
<dt> <code>&#8211;output-asm-variant=</code>&lt;uint&gt; &#8211; Syntax variant to use for output printing</dt>
<dt> <code>&#8211;pie-copy-relocations</code> &#8211; PIE Copy Relocations</dt>
<dt> <code>&#8211;poison-checking-function-local</code> &#8211; Check that returns are non-poison (for testing)</dt>
<dt> <code>&#8211;position-independent</code> &#8211; Position independent</dt>
<dt> <code>&#8211;preserve-comments</code> &#8211; Preserve Comments in outputted assembly</dt>
<dt> <code>&#8211;print-imm-hex</code> &#8211; Prefer hex format for immediate values</dt>
<dt> <code>&#8211;r600-ir-structurize</code> &#8211; Use StructurizeCFG IR pass</dt>
<dt> <code>&#8211;rdf-dump</code> &#8211;</dt>
<dt> <code>&#8211;rdf-limit=</code>&lt;uint&gt; &#8211;</dt>
<dt> <code>&#8211;relax-relocations</code> &#8211; Emit R_X86_64_GOTPCRELX instead of R_X86_64_GOTPCREL</dt>
<dt> <code>&#8211;remarks-section</code> &#8211; Emit a section containing remark diagnostics metadata</dt>
<dt> <code>&#8211;safepoint-ir-verifier-print-only</code> &#8211;</dt>
<dt> <code>&#8211;sample-profile-check-record-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of records in the input profile are matched to the IR.</dt>
<dt> <code>&#8211;sample-profile-check-sample-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of samples in the input profile are matched to the IR.</dt>
<dt> <code>&#8211;sample-profile-max-propagate-iterations=</code>&lt;uint&gt; &#8211; Maximum number of iterations to go through when propagating sample block/edge weights through the CFG.</dt>
<dt> <code>&#8211;save-temp-labels</code> &#8211; Don&#8217;t discard temporary labels</dt>
<dt> <code>&#8211;show-encoding</code> &#8211; Show instruction encodings</dt>
<dt> <code>&#8211;show-inst</code> &#8211; Show internal instruction representation</dt>
<dt> <code>&#8211;show-inst-operands</code> &#8211; Show instructions operands as parsed</dt>
<dt><code>&#8211;speculative-counter-promotion-max-exiting=</code>&lt;uint&gt; &#8211; The max number of exiting blocks of a loop to allow</dt>
<dd>
</dd><dd>speculative counter promotion</dd>
<dt><code>&#8211;speculative-counter-promotion-to-loop</code> &#8211; When the option is false, if the target block is in a loop, the promotion will be disallowed unless the promoted counter</dt>
<dd> update can be further/iteratively promoted into an acyclic region.</dd>
<dt> <code>&#8211;split-dwarf-file=</code>&lt;filename&gt; &#8211; DWO output filename</dt>
<dt> <code>&#8211;summary-file=</code>&lt;string&gt; &#8211; The summary file to use for function importing.</dt>
<dt> <code>&#8211;threads=</code>&lt;int&gt; &#8211;</dt>
<dt> <code>&#8211;time-trace-granularity=</code>&lt;uint&gt; &#8211; Minimum time granularity (in microseconds) traced by time profiler</dt>
<dt> <code>&#8211;triple=</code>&lt;string&gt; &#8211; Target triple to assemble for, see <code>-version</code> for available targets</dt>
<dt> <code>&#8211;verify-region-info</code> &#8211; Verify region info (time consuming)</dt>
<dt> <code>&#8211;vp-counters-per-site=</code>&lt;number&gt; &#8211; The average number of profile counters allocated per value profiling site.</dt>
<dt> <code>&#8211;vp-static-alloc</code> &#8211; Do static counter allocation for value profiler</dt></dl>
<dd>Generic Options:</dd>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</dt>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</dt>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program </dt>
</dl>
