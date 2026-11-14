---
title: "llvm-rtdyld-10(1)"
name: "llvm-rtdyld-10"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-rtdyld-10/"
description: "llvm-rtdyld – manual page for llvm-rtdyld 10"
---

<h2 class="name">NAME</h2>
<p> llvm-rtdyld &#8211; manual page for llvm-rtdyld 10 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm MC-JIT tool </p>
<p> USAGE: llvm-rtdyld [options] &lt;input files&gt; <code>&#8211;args</code> &lt;program arguments&gt;&#8230; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dl>
<dd>General options:</p>
<dl>
<dt> <code>&#8211;aarch64-neon-syntax=</code>&lt;value&gt; &#8211; Choose style of NEON code to emit from AArch64 backend:</p>
<dt>=generic</p>
<dd> &#8211; Emit generic NEON assembly</p>
<dt>=apple</p>
<dd> &#8211; Emit Apple-style NEON assembly</p>
<dt> <code>&#8211;amdgpu-disable-loop-alignment</code> &#8211; Do not align and prefetch loops</p>
<dt> <code>&#8211;amdgpu-disable-power-sched</code> &#8211; Disable scheduling to minimize mAI power bursts</p>
<dt> <code>&#8211;amdgpu-dpp-combine</code> &#8211; Enable DPP combiner</p>
<dt> <code>&#8211;amdgpu-dump-hsa-metadata</code> &#8211; Dump AMDGPU HSA Metadata</p>
<dt> <code>&#8211;amdgpu-enable-global-sgpr-addr</code> &#8211; Enable use of SGPR regs for GLOBAL LOAD/STORE instructions</p>
<dt> <code>&#8211;amdgpu-enable-merge-m0</code> &#8211; Merge and hoist M0 initializations</p>
<dt> <code>&#8211;amdgpu-sdwa-peephole</code> &#8211; Enable SDWA peepholer</p>
<dt> <code>&#8211;amdgpu-verify-hsa-metadata</code> &#8211; Verify AMDGPU HSA Metadata</p>
<dt> <code>&#8211;amdgpu-vgpr-index-mode</code> &#8211; Use GPR indexing mode instead of movrel for vector indexing</p>
<dt> <code>&#8211;args</code> &lt;string&gt;&#8230; &#8211; &lt;program arguments&gt;&#8230;</p>
<dt> <code>&#8211;arm-add-build-attributes</code> &#8211;</p>
<dt> <code>&#8211;arm-implicit-it=</code>&lt;value&gt; &#8211; Allow conditional instructions outdside of an IT block</p>
<dt>=always</p>
<dd> &#8211; Accept in both ISAs, emit implicit ITs in Thumb</p>
<dt>=never</p>
<dd> &#8211; Warn in ARM, reject in Thumb</p>
<dt>=arm</p>
<dd> &#8211; Accept in ARM, reject in Thumb</p>
<dt>=thumb</p>
<dd> &#8211; Warn in ARM, emit implicit ITs in Thumb</p>
<dt><code>&#8211;atomic-counter-update-promoted</code> &#8211; Do counter update using atomic fetch add</p>
<dd>
<dd>for promoted counters only</p>
<dt> <code>&#8211;bounds-checking-single-trap</code> &#8211; Use one trap block per function</p>
<dt> <code>&#8211;check=</code>&lt;string&gt; &#8211; File containing RuntimeDyld verifier checks.</p>
<dt> <code>&#8211;cost-kind=</code>&lt;value&gt; &#8211; Target cost kind</p>
<dt>=throughput</p>
<dd> &#8211; Reciprocal throughput</p>
<dt>=latency</p>
<dd> &#8211; Instruction latency</p>
<dt>=code-size</p>
<dd> &#8211; Code size</p>
<dt> <code>&#8211;cvp-dont-add-nowrap-flags</code> &#8211;</p>
<dt> <code>&#8211;debugify-quiet</code> &#8211; Suppress verbose debugify output</p>
<dt> <code>&#8211;disable-promote-alloca-to-lds</code> &#8211; Disable promote alloca to LDS</p>
<dt> <code>&#8211;disable-promote-alloca-to-vector</code> &#8211; Disable promote alloca to vector</p>
<dt> <code>&#8211;do-counter-promotion</code> &#8211; Do counter register promotion</p>
<dt> <code>&#8211;dylib=</code>&lt;string&gt; &#8211; Add library.</p>
<dt> <code>&#8211;emscripten-cxx-exceptions-whitelist=</code>&lt;string&gt; &#8211; The list of function names in which Emscripten-style exception handling is enabled (see emscripten EMSCRIPTEN_CATCHING_WHITELIST options)</p>
<dt> <code>&#8211;enable-cse-in-irtranslator</code> &#8211; Should enable CSE in irtranslator</p>
<dt> <code>&#8211;enable-cse-in-legalizer</code> &#8211; Should enable CSE in Legalizer</p>
<dt> <code>&#8211;enable-emscripten-cxx-exceptions</code> &#8211; WebAssembly Emscripten-style exception handling</p>
<dt> <code>&#8211;enable-emscripten-sjlj</code> &#8211; WebAssembly Emscripten-style setjmp/longjmp handling</p>
<dt> <code>&#8211;enable-gvn-memdep</code> &#8211;</p>
<dt> <code>&#8211;enable-load-pre</code> &#8211;</p>
<dt> <code>&#8211;enable-loop-simplifycfg-term-folding</code> &#8211;</p>
<dt> <code>&#8211;enable-name-compression</code> &#8211; Enable name string compression</p>
<dt> <code>&#8211;entry=</code>&lt;string&gt; &#8211; Function to call as entry point.</p>
<dt>
<dd>
<dd>Action to perform:</p>
<dt> <code>&#8211;execute</code> &#8211; Load, link, and execute the inputs.</p>
<dt> <code>&#8211;printline</code> &#8211; Load, link, and print line information for each function.</p>
<dt> <code>&#8211;printdebugline</code> &#8211; Load, link, and print line information for each function using the debug object</p>
<dt> <code>&#8211;printobjline</code> &#8211; Like <code>-printlineinfo</code> but does not load the object first</p>
<dt> <code>&#8211;verify</code> &#8211; Load, link and verify the resulting memory image.</p>
<dt> <code>&#8211;expensive-combines</code> &#8211; Enable expensive instruction combines</p>
<dt><code>&#8211;gpsize=</code>&lt;uint&gt; &#8211; Global Pointer Addressing Size.</p>
<dd>
<dd>The default size is 8.</p>
<dt> <code>&#8211;hash-based-counter-split</code> &#8211; Rename counter variable of a comdat function based on cfg hash</p>
<dt> <code>&#8211;import-all-index</code> &#8211; Import all external functions in index.</p>
<dt> <code>&#8211;instcombine-code-sinking</code> &#8211; Enable code sinking</p>
<dt> <code>&#8211;instcombine-guard-widening-window=</code>&lt;uint&gt; &#8211; How wide an instruction window to bypass looking for another guard</p>
<dt> <code>&#8211;instcombine-max-iterations=</code>&lt;uint&gt; &#8211; Limit the maximum number of instruction combining iterations</p>
<dt> <code>&#8211;instcombine-max-num-phis=</code>&lt;uint&gt; &#8211; Maximum number phis to handle in intptr/ptrint folding</p>
<dt> <code>&#8211;instcombine-maxarray-size=</code>&lt;uint&gt; &#8211; Maximum array size considered when doing a combine</p>
<dt> <code>&#8211;instrprof-atomic-counter-update-all</code> &#8211; Make all profile counter updates atomic (for testing only)</p>
<dt> <code>&#8211;internalize-public-api-file=</code>&lt;filename&gt; &#8211; A file containing list of symbol names to preserve</p>
<dt> <code>&#8211;internalize-public-api-list=</code>&lt;list&gt; &#8211; A list of symbol names to preserve</p>
<dt> <code>&#8211;iterative-counter-promotion</code> &#8211; Allow counter promotion across the whole loop nest.</p>
<dt> <code>&#8211;lto-embed-bitcode</code> &#8211; Embed LLVM bitcode in object files produced by LTO</p>
<dt> <code>&#8211;lto-pass-remarks-filter=</code>&lt;regex&gt; &#8211; Only record optimization remarks from passes whose names match the given regular expression</p>
<dt> <code>&#8211;lto-pass-remarks-format=</code>&lt;format&gt; &#8211; The format used for serializing remarks (default: YAML)</p>
<dt> <code>&#8211;lto-pass-remarks-output=</code>&lt;filename&gt; &#8211; Output filename for pass remarks</p>
<dt> <code>&#8211;matrix-propagate-shape</code> &#8211;</p>
<dt> <code>&#8211;max-counter-promotions=</code>&lt;int&gt; &#8211; Max number of allowed counter promotions</p>
<dt> <code>&#8211;max-counter-promotions-per-loop=</code>&lt;uint&gt; &#8211; Max number counter promotions per loop to avoid increasing register pressure too much</p>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;memop-size-large=</code>&lt;uint&gt; &#8211; Set large value thresthold in memory intrinsic size profiling. Value of 0 disables the large value profiling.</p>
<dt> <code>&#8211;memop-size-range=</code>&lt;string&gt; &#8211; Set the range of size in memory intrinsic calls to be profiled precisely, in a format of &lt;start_val&gt;:&lt;end_val&gt;</p>
<dt> <code>&#8211;merror-missing-parenthesis</code> &#8211; Error for missing parenthesis around predicate registers</p>
<dt> <code>&#8211;merror-noncontigious-register</code> &#8211; Error for register names that aren&#8217;t contigious</p>
<dt> <code>&#8211;mhvx</code> &#8211; Enable Hexagon Vector eXtensions</p>
<dt> <code>&#8211;mhvx=</code>&lt;value&gt; &#8211; Enable Hexagon Vector eXtensions</p>
<dt>=v60</p>
<dd> &#8211; Build for HVX v60</p>
<dt>=v62</p>
<dd> &#8211; Build for HVX v62</p>
<dt>=v65</p>
<dd> &#8211; Build for HVX v65</p>
<dt>=v66</p>
<dd> &#8211; Build for HVX v66</p>
<dt> <code>&#8211;mips-compact-branches=</code>&lt;value&gt; &#8211; MIPS Specific: Compact branch policy.</p>
<dt>=never</p>
<dd> &#8211; Do not use compact branches if possible.</p>
<dt>=optimal</p>
<dd> &#8211; Use compact branches where appropiate (default).</p>
<dt>=always</p>
<dd> &#8211; Always use compact branches if possible.</p>
<dt> <code>&#8211;mips16-constant-islands</code> &#8211; Enable mips16 constant islands.</p>
<dt> <code>&#8211;mips16-hard-float</code> &#8211; Enable mips16 hard float.</p>
<dt> <code>&#8211;mno-compound</code> &#8211; Disable looking for compound instructions for Hexagon</p>
<dt> <code>&#8211;mno-fixup</code> &#8211; Disable fixing up resolved relocations for Hexagon</p>
<dt> <code>&#8211;mno-ldc1-sdc1</code> &#8211; Expand double precision loads and stores to their single precision counterparts</p>
<dt> <code>&#8211;mno-pairing</code> &#8211; Disable looking for duplex instructions for Hexagon</p>
<dt> <code>&#8211;mwarn-missing-parenthesis</code> &#8211; Warn for missing parenthesis around predicate registers</p>
<dt> <code>&#8211;mwarn-noncontigious-register</code> &#8211; Warn for register names that arent contigious</p>
<dt> <code>&#8211;mwarn-sign-mismatch</code> &#8211; Warn for mismatching a signed and unsigned value</p>
<dt> <code>&#8211;no-discriminators</code> &#8211; Disable generation of discriminator information.</p>
<dt> <code>&#8211;nvptx-sched4reg</code> &#8211; NVPTX Specific: schedule for register pressue</p>
<dt> <code>&#8211;poison-checking-function-local</code> &#8211; Check that returns are non-poison (for testing)</p>
<dt> <code>&#8211;preallocate=</code>&lt;ulong&gt; &#8211; Allocate memory upfront rather than on-demand</p>
<dt> <code>&#8211;r600-ir-structurize</code> &#8211; Use StructurizeCFG IR pass</p>
<dt> <code>&#8211;rdf-dump</code> &#8211;</p>
<dt> <code>&#8211;rdf-limit=</code>&lt;uint&gt; &#8211;</p>
<dt> <code>&#8211;safepoint-ir-verifier-print-only</code> &#8211;</p>
<dt> <code>&#8211;sample-profile-check-record-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of records in the input profile are matched to the IR.</p>
<dt> <code>&#8211;sample-profile-check-sample-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of samples in the input profile are matched to the IR.</p>
<dt> <code>&#8211;sample-profile-max-propagate-iterations=</code>&lt;uint&gt; &#8211; Maximum number of iterations to go through when propagating sample block/edge weights through the CFG.</p>
<dt> <code>&#8211;show-times</code> &#8211; Show times for llvm-rtdyld phases</p>
<dt><code>&#8211;speculative-counter-promotion-max-exiting=</code>&lt;uint&gt; &#8211; The max number of exiting blocks of a loop to allow</p>
<dd>
<dd>speculative counter promotion</p>
<dt><code>&#8211;speculative-counter-promotion-to-loop</code> &#8211; When the option is false, if the target block is in a loop, the promotion will be disallowed unless the promoted counter</p>
<dd> update can be further/iteratively promoted into an acyclic region.</p>
<dt> <code>&#8211;summary-file=</code>&lt;string&gt; &#8211; The summary file to use for function importing.</p>
<dt> <code>&#8211;threads=</code>&lt;int&gt; &#8211;</p>
<dt> <code>&#8211;triple=</code>&lt;string&gt; &#8211; Target triple for disassembler</p>
<dt> <code>&#8211;verify-region-info</code> &#8211; Verify region info (time consuming)</p>
<dt> <code>&#8211;vp-counters-per-site=</code>&lt;number&gt; &#8211; The average number of profile counters allocated per value profiling site.</p>
<dt> <code>&#8211;vp-static-alloc</code> &#8211; Do static counter allocation for value profiler</p>
<dt> <code>&#8211;x86-align-branch=</code>&lt;(plus separated list of types)&gt; &#8211; Specify types of branches to align. The branches&#8217;s types are combination of jcc, fused, jmp, call, ret, indirect. jcc indicates conditional jumps, fused indicates fused conditional jumps, jmp indicates unconditional jumps, call indicates direct and indirect calls, ret indicates rets, indirect indicates indirect jumps.</p>
<dt> <code>&#8211;x86-align-branch-boundary=</code>&lt;uint&gt; &#8211; Control how the assembler should align branches with NOP. If the boundary&#8217;s size is not 0, it should be a power of 2 and no less than 32. Branches will be aligned to prevent from being across or against the boundary of specified size. The default value 0 does not align branches.</p>
<dt><code>&#8211;x86-branches-within-32B-boundaries</code> &#8211; Align selected instructions to mitigate negative performance impact of Intel&#8217;s micro code update for errata skx102.</p>
<dd>
<dd>May break assumptions about labels corresponding to particular instructions, and should be used with caution.</dl>
<p> Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program </p>
</dl>
<h2>Index</h2>
