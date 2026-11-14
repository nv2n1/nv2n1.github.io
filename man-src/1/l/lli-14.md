---
title: "lli-14(1)"
name: "lli-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lli-14/"
description: "lli – manual page for lli 14"
---

<h2 class="name">NAME</h2>
<p> lli &#8211; manual page for lli 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm interpreter &amp; dynamic compiler </p>
<p> USAGE: lli [options] &lt;input bitcode&gt; &lt;program arguments&gt;&#8230; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dl>
<dd>General options:</p>
<dl>
<dt> <code>-O=</code>&lt;char&gt; &#8211; Optimization level. [-O0, <code>-O1</code>, <code>-O2</code>, or <code>-O3]</code> (default = &#8216;-O2&#8217;)</p>
<dt> <code>&#8211;aarch64-neon-syntax=</code>&lt;value&gt; &#8211; Choose style of NEON code to emit from AArch64 backend:</p>
<dt>=generic</p>
<dd> &#8211; Emit generic NEON assembly</p>
<dt>=apple</p>
<dd> &#8211; Emit Apple-style NEON assembly</p>
<dt> <code>&#8211;aarch64-use-aa</code> &#8211; Enable the use of AA during codegen.</p>
<dt> <code>&#8211;abort-on-max-devirt-iterations-reached</code> &#8211; Abort when the max iterations for devirtualization CGSCC repeat pass is reached</p>
<dt> <code>&#8211;addrsig</code> &#8211; Emit an address-significance table</p>
<dt> <code>&#8211;align-loops=</code>&lt;uint&gt; &#8211; Default alignment for loops</p>
<dt> <code>&#8211;allow-ginsert-as-artifact</code> &#8211; Allow G_INSERT to be considered an artifact. Hack around AMDGPU test infinite loops.</p>
<dt> <code>&#8211;amdgpu-bypass-slow-div</code> &#8211; Skip 64-bit divide for dynamic 32-bit values</p>
<dt> <code>&#8211;amdgpu-disable-loop-alignment</code> &#8211; Do not align and prefetch loops</p>
<dt> <code>&#8211;amdgpu-disable-power-sched</code> &#8211; Disable scheduling to minimize mAI power bursts</p>
<dt> <code>&#8211;amdgpu-dpp-combine</code> &#8211; Enable DPP combiner</p>
<dt> <code>&#8211;amdgpu-dump-hsa-metadata</code> &#8211; Dump AMDGPU HSA Metadata</p>
<dt> <code>&#8211;amdgpu-enable-flat-scratch</code> &#8211; Use flat scratch instructions</p>
<dt> <code>&#8211;amdgpu-enable-merge-m0</code> &#8211; Merge and hoist M0 initializations</p>
<dt> <code>&#8211;amdgpu-promote-alloca-to-vector-limit=</code>&lt;uint&gt; &#8211; Maximum byte size to consider promote alloca to vector</p>
<dt> <code>&#8211;amdgpu-sdwa-peephole</code> &#8211; Enable SDWA peepholer</p>
<dt> <code>&#8211;amdgpu-use-aa-in-codegen</code> &#8211; Enable the use of AA during codegen.</p>
<dt> <code>&#8211;amdgpu-verify-hsa-metadata</code> &#8211; Verify AMDGPU HSA Metadata</p>
<dt> <code>&#8211;amdgpu-vgpr-index-mode</code> &#8211; Use GPR indexing mode instead of movrel for vector indexing</p>
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
<dt> <code>&#8211;asm-show-inst</code> &#8211; Emit internal instruction representation to assembly file</p>
<dt><code>&#8211;atomic-counter-update-promoted</code> &#8211; Do counter update using atomic fetch add</p>
<dd>
<dd>for promoted counters only</p>
<dt> <code>&#8211;atomic-first-counter</code> &#8211; Use atomic fetch add for first counter in a function (usually the entry counter)</p>
<dt> <code>&#8211;basic-block-sections=</code>&lt;all | &lt;function list (file)&gt; | labels | none&gt; &#8211; Emit basic blocks into separate sections</p>
<dt> <code>&#8211;bounds-checking-single-trap</code> &#8211; Use one trap block per function</p>
<dt> <code>&#8211;cfg-hide-cold-paths=</code>&lt;number&gt; &#8211; Hide blocks with relative frequency below the given value</p>
<dt> <code>&#8211;cfg-hide-deoptimize-paths</code> &#8211;</p>
<dt> <code>&#8211;cfg-hide-unreachable-paths</code> &#8211;</p>
<dt> <code>&#8211;code-model=</code>&lt;value&gt; &#8211; Choose code model</p>
<dt>=tiny</p>
<dd> &#8211; Tiny code model</p>
<dt>=small</p>
<dd> &#8211; Small code model</p>
<dt>=kernel</p>
<dd> &#8211; Kernel code model</p>
<dt>=medium</p>
<dd> &#8211; Medium code model</p>
<dt>=large</p>
<dd> &#8211; Large code model</p>
<dt> <code>&#8211;compile-threads=</code>&lt;uint&gt; &#8211; Choose the number of compile threads (jit-kind=orc-lazy only)</p>
<dt> <code>&#8211;cost-kind=</code>&lt;value&gt; &#8211; Target cost kind</p>
<dt>=throughput</p>
<dd> &#8211; Reciprocal throughput</p>
<dt>=latency</p>
<dd> &#8211; Instruction latency</p>
<dt>=code-size</p>
<dd> &#8211; Code size</p>
<dt>=size-latency</p>
<dd> &#8211; Code size and latency</p>
<dt> <code>&#8211;data-sections</code> &#8211; Emit data into separate sections</p>
<dt> <code>&#8211;debug-entry-values</code> &#8211; Enable debug info for the debug entry values.</p>
<dt> <code>&#8211;debug-info-correlate</code> &#8211; Use debug info to correlate profiles.</p>
<dt> <code>&#8211;debugger-tune=</code>&lt;value&gt; &#8211; Tune debug info for a particular debugger</p>
<dt>=gdb</p>
<dd> &#8211; gdb</p>
<dt>=lldb</p>
<dd> &#8211; lldb</p>
<dt>=dbx</p>
<dd> &#8211; dbx</p>
<dt>=sce</p>
<dd> &#8211; SCE targets (e.g. PS4)</p>
<dt> <code>&#8211;debugify-level=</code>&lt;value&gt; &#8211; Kind of debug info to add</p>
<dt>=locations</p>
<dd> &#8211; Locations only</p>
<dt>=location+variables</p>
<dd> &#8211; Locations and Variables</p>
<dt> <code>&#8211;debugify-quiet</code> &#8211; Suppress verbose debugify output</p>
<dt> <code>&#8211;denormal-fp-math=</code>&lt;value&gt; &#8211; Select which denormal numbers the code is permitted to require</p>
<dt>=ieee</p>
<dd> &#8211; IEEE 754 denormal numbers</p>
<dt>=preserve-sign</p>
<dd> &#8211; the sign of a flushed-to-zero number is preserved in the sign of 0</p>
<dt>=positive-zero</p>
<dd> &#8211; denormals are flushed to positive zero</p>
<dt> <code>&#8211;denormal-fp-math-f32=</code>&lt;value&gt; &#8211; Select which denormal numbers the code is permitted to require for float</p>
<dt>=ieee</p>
<dd> &#8211; IEEE 754 denormal numbers</p>
<dt>=preserve-sign</p>
<dd> &#8211; the sign of a flushed-to-zero number is preserved in the sign of 0</p>
<dt>=positive-zero</p>
<dd> &#8211; denormals are flushed to positive zero</p>
<dt> <code>&#8211;disable-i2p-p2i-opt</code> &#8211; Disables inttoptr/ptrtoint roundtrip optimization</p>
<dt> <code>&#8211;disable-lazy-compilation</code> &#8211; Disable JIT lazy compilation</p>
<dt> <code>&#8211;disable-promote-alloca-to-lds</code> &#8211; Disable promote alloca to LDS</p>
<dt> <code>&#8211;disable-promote-alloca-to-vector</code> &#8211; Disable promote alloca to vector</p>
<dt> <code>&#8211;disable-tail-calls</code> &#8211; Never emit tail calls</p>
<dt> <code>&#8211;dlopen=</code>&lt;string&gt; &#8211; Dynamic libraries to load before linking</p>
<dt> <code>&#8211;do-counter-promotion</code> &#8211; Do counter register promotion</p>
<dt> <code>&#8211;dot-cfg-mssa=</code>&lt;file name for generated dot file&gt; &#8211; file name for generated dot file</p>
<dt> <code>&#8211;dwarf-version=</code>&lt;int&gt; &#8211; Dwarf version</p>
<dt> <code>&#8211;dwarf64</code> &#8211; Generate debugging info in the 64-bit DWARF format</p>
<dt> <code>&#8211;emit-call-site-info</code> &#8211; Emit call site debug information, if debug information is enabled.</p>
<dt> <code>&#8211;emscripten-cxx-exceptions-allowed=</code>&lt;string&gt; &#8211; The list of function names in which Emscripten-style exception handling is enabled (see emscripten EMSCRIPTEN_CATCHING_ALLOWED options)</p>
<dt> <code>&#8211;emulated-tls</code> &#8211; Use emulated TLS model</p>
<dt> <code>&#8211;enable-cache-manager</code> &#8211; Use cache manager to save/load modules</p>
<dt> <code>&#8211;enable-cse-in-irtranslator</code> &#8211; Should enable CSE in irtranslator</p>
<dt> <code>&#8211;enable-cse-in-legalizer</code> &#8211; Should enable CSE in Legalizer</p>
<dt> <code>&#8211;enable-emscripten-cxx-exceptions</code> &#8211; WebAssembly Emscripten-style exception handling</p>
<dt> <code>&#8211;enable-emscripten-sjlj</code> &#8211; WebAssembly Emscripten-style setjmp/longjmp handling</p>
<dt> <code>&#8211;enable-gvn-hoist</code> &#8211; Enable the GVN hoisting pass (default = off)</p>
<dt> <code>&#8211;enable-gvn-memdep</code> &#8211;</p>
<dt> <code>&#8211;enable-gvn-sink</code> &#8211; Enable the GVN sinking pass (default = off)</p>
<dt> <code>&#8211;enable-load-in-loop-pre</code> &#8211;</p>
<dt> <code>&#8211;enable-load-pre</code> &#8211;</p>
<dt> <code>&#8211;enable-loop-simplifycfg-term-folding</code> &#8211;</p>
<dt> <code>&#8211;enable-name-compression</code> &#8211; Enable name/filename string compression</p>
<dt> <code>&#8211;enable-no-infs-fp-math</code> &#8211; Enable FP math optimizations that assume no +-Infs</p>
<dt> <code>&#8211;enable-no-nans-fp-math</code> &#8211; Enable FP math optimizations that assume no NaNs</p>
<dt> <code>&#8211;enable-no-signed-zeros-fp-math</code> &#8211; Enable FP math optimizations that assume the sign of 0 is insignificant</p>
<dt> <code>&#8211;enable-no-trapping-fp-math</code> &#8211; Enable setting the FP exceptions build attribute not to use exceptions</p>
<dt> <code>&#8211;enable-split-backedge-in-load-pre</code> &#8211;</p>
<dt> <code>&#8211;enable-unsafe-fp-math</code> &#8211; Enable optimizations that may decrease FP precision</p>
<dt> <code>&#8211;entry-function=</code>&lt;function&gt; &#8211; Specify the entry function (default = &#8216;main&#8217;) of the executable</p>
<dt> <code>&#8211;exception-model=</code>&lt;value&gt; &#8211; exception model</p>
<dt>=default</p>
<dd> &#8211; default exception handling model</p>
<dt>=dwarf</p>
<dd> &#8211; DWARF-like CFI based exception handling</p>
<dt>=sjlj</p>
<dd> &#8211; SjLj exception handling</p>
<dt>=arm</p>
<dd> &#8211; ARM EHABI exceptions</p>
<dt>=wineh</p>
<dd> &#8211; Windows exception model</p>
<dt>=wasm</p>
<dd> &#8211; WebAssembly exception handling</p>
<dt> <code>&#8211;experimental-debug-variable-locations</code> &#8211; Use experimental new value-tracking variable locations</p>
<dt> <code>&#8211;extra-archive=</code>&lt;input archive&gt; &#8211; Extra archive files to be loaded</p>
<dt> <code>&#8211;extra-module=</code>&lt;input bitcode&gt; &#8211; Extra modules to be loaded</p>
<dt> <code>&#8211;extra-object=</code>&lt;input object&gt; &#8211; Extra object files to be loaded</p>
<dt> <code>&#8211;fake-argv0=</code>&lt;executable&gt; &#8211; Override the &#8216;argv[0]&#8217; value passed into the executing program</p>
<dt> <code>&#8211;fatal-warnings</code> &#8211; Treat warnings as errors</p>
<dt> <code>&#8211;filetype=</code>&lt;value&gt; &#8211; Choose a file type (not all types are supported by all targets):</p>
<dt>=asm</p>
<dd> &#8211; Emit an assembly (&#8216;.s&#8217;) file</p>
<dt>=obj</p>
<dd> &#8211; Emit a native object (&#8216;.o&#8217;) file</p>
<dt>=null</p>
<dd> &#8211; Emit nothing, for performance testing</p>
<dt> <code>&#8211;float-abi=</code>&lt;value&gt; &#8211; Choose float ABI type</p>
<dt>=default</p>
<dd> &#8211; Target default float ABI type</p>
<dt>=soft</p>
<dd> &#8211; Soft float ABI (implied by <code>-soft-float</code>)</p>
<dt>=hard</p>
<dd> &#8211; Hard float ABI (uses FP registers)</p>
<dt> <code>&#8211;force-dwarf-frame-section</code> &#8211; Always emit a debug frame section.</p>
<dt> <code>&#8211;force-interpreter</code> &#8211; Force interpretation: disable JIT</p>
<dt> <code>&#8211;fp-contract=</code>&lt;value&gt; &#8211; Enable aggressive formation of fused FP ops</p>
<dt>=fast</p>
<dd> &#8211; Fuse FP ops whenever profitable</p>
<dt>=on</p>
<dd> &#8211; Only fuse &#8216;blessed&#8217; FP ops.</p>
<dt>=off</p>
<dd> &#8211; Only fuse FP ops when the result won&#8217;t be affected.</p>
<dt> <code>&#8211;frame-pointer=</code>&lt;value&gt; &#8211; Specify frame pointer elimination optimization</p>
<dt>=all</p>
<dd> &#8211; Disable frame pointer elimination</p>
<dt>=non-leaf</p>
<dd> &#8211; Disable frame pointer elimination for non-leaf frame</p>
<dt>=none</p>
<dd> &#8211; Enable frame pointer elimination</p>
<dt><code>&#8211;fs-profile-debug-bw-threshold=</code>&lt;uint&gt; &#8211; Only show debug message if the source branch weight is greater</p>
<dd>
<dd>than this value.</p>
<dt> <code>&#8211;fs-profile-debug-prob-diff-threshold=</code>&lt;uint&gt; &#8211; Only show debug message if the branch probility is greater than this value (in percentage).</p>
<dt> <code>&#8211;function-sections</code> &#8211; Emit functions into separate sections</p>
<dt> <code>&#8211;generate-merged-base-profiles</code> &#8211; When generating nested context-sensitive profiles, always generate extra base profile for function with all its context profiles merged into it.</p>
<dt><code>&#8211;gpsize=</code>&lt;uint&gt; &#8211; Global Pointer Addressing Size.</p>
<dd>
<dd>The default size is 8.</p>
<dt> <code>&#8211;hash-based-counter-split</code> &#8211; Rename counter variable of a comdat function based on cfg hash</p>
<dt> <code>&#8211;hot-cold-split</code> &#8211; Enable hot-cold splitting pass</p>
<dt> <code>&#8211;ignore-xcoff-visibility</code> &#8211; Not emit the visibility attribute for asm in AIX OS or give all symbols &#8216;unspecified&#8217; visibility in XCOFF object file</p>
<dt> <code>&#8211;import-all-index</code> &#8211; Import all external functions in index.</p>
<dt> <code>&#8211;incremental-linker-compatible</code> &#8211; When used with filetype=obj, emit an object file which can be used with an incremental linker</p>
<dt> <code>&#8211;instcombine-code-sinking</code> &#8211; Enable code sinking</p>
<dt> <code>&#8211;instcombine-guard-widening-window=</code>&lt;uint&gt; &#8211; How wide an instruction window to bypass looking for another guard</p>
<dt> <code>&#8211;instcombine-max-iterations=</code>&lt;uint&gt; &#8211; Limit the maximum number of instruction combining iterations</p>
<dt> <code>&#8211;instcombine-max-num-phis=</code>&lt;uint&gt; &#8211; Maximum number phis to handle in intptr/ptrint folding</p>
<dt> <code>&#8211;instcombine-maxarray-size=</code>&lt;uint&gt; &#8211; Maximum array size considered when doing a combine</p>
<dt> <code>&#8211;instcombine-negator-enabled</code> &#8211; Should we attempt to sink negations?</p>
<dt> <code>&#8211;instcombine-negator-max-depth=</code>&lt;uint&gt; &#8211; What is the maximal lookup depth when trying to check for viability of negation sinking.</p>
<dt> <code>&#8211;instrprof-atomic-counter-update-all</code> &#8211; Make all profile counter updates atomic (for testing only)</p>
<dt> <code>&#8211;internalize-public-api-file=</code>&lt;filename&gt; &#8211; A file containing list of symbol names to preserve</p>
<dt> <code>&#8211;internalize-public-api-list=</code>&lt;list&gt; &#8211; A list of symbol names to preserve</p>
<dt> <code>&#8211;iterative-counter-promotion</code> &#8211; Allow counter promotion across the whole loop nest.</p>
<dt> <code>&#8211;jd=</code>&lt;string&gt; &#8211; Specifies the JITDylib to be used for any subsequent <code>-extra-module</code> arguments.</p>
<dt> <code>&#8211;jit-kind=</code>&lt;value&gt; &#8211; Choose underlying JIT kind.</p>
<dt>=mcjit</p>
<dd> &#8211; MCJIT</p>
<dt>=orc</p>
<dd> &#8211; Orc JIT</p>
<dt>=orc-lazy</p>
<dd> &#8211; Orc-based lazy JIT.</p>
<dt> <code>&#8211;jit-linker=</code>&lt;value&gt; &#8211; Choose the dynamic linker/loader.</p>
<dt>=default</p>
<dd> &#8211; Default for platform and JIT-kind</p>
<dt>=rtdyld</p>
<dd> &#8211; RuntimeDyld</p>
<dt>=jitlink</p>
<dd> &#8211; Orc-specific linker</p>
<dt> <code>&#8211;load=</code>&lt;pluginfilename&gt; &#8211; Load the specified plugin</p>
<dt> <code>&#8211;lto-embed-bitcode=</code>&lt;value&gt; &#8211; Embed LLVM bitcode in object files produced by LTO</p>
<dt>=none</p>
<dd> &#8211; Do not embed</p>
<dt>=optimized</p>
<dd> &#8211; Embed after all optimization passes</p>
<dt>=post-merge-pre-opt</p>
<dd> &#8211; Embed post merge, but before optimizations</p>
<dt> <code>&#8211;lto-pass-remarks-filter=</code>&lt;regex&gt; &#8211; Only record optimization remarks from passes whose names match the given regular expression</p>
<dt> <code>&#8211;lto-pass-remarks-format=</code>&lt;format&gt; &#8211; The format used for serializing remarks (default: YAML)</p>
<dt> <code>&#8211;lto-pass-remarks-output=</code>&lt;filename&gt; &#8211; Output filename for pass remarks</p>
<dt> <code>&#8211;march=</code>&lt;string&gt; &#8211; Architecture to generate code for (see <code>&#8211;version</code>)</p>
<dt> <code>&#8211;matrix-default-layout=</code>&lt;value&gt; &#8211; Sets the default matrix layout</p>
<dt>=column-major</p>
<dd> &#8211; Use column-major layout</p>
<dt>=row-major</p>
<dd> &#8211; Use row-major layout</p>
<dt> <code>&#8211;mattr=</code>&lt;a1,+a2,-a3,&#8230;&gt; &#8211; Target specific attributes (<code>-mattr</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;max-counter-promotions=</code>&lt;int&gt; &#8211; Max number of allowed counter promotions</p>
<dt> <code>&#8211;max-counter-promotions-per-loop=</code>&lt;uint&gt; &#8211; Max number counter promotions per loop to avoid increasing register pressure too much</p>
<dt> <code>&#8211;mc-relax-all</code> &#8211; When used with filetype=obj, relax all fixups in the emitted object file</p>
<dt> <code>&#8211;mcabac</code> &#8211; tbd</p>
<dt><code>&#8211;mcjit-remote-process=</code>&lt;filename&gt; &#8211; Specify the filename of the process to launch for remote MCJIT execution.</p>
<dd>
<dd>If none is specified, remote execution will be simulated in-process.</p>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;meabi=</code>&lt;value&gt; &#8211; Set EABI type (default depends on triple):</p>
<dt>=default</p>
<dd> &#8211; Triple default EABI version</p>
<dt>=4</p>
<dd> &#8211; EABI version 4</p>
<dt>=5</p>
<dd> &#8211; EABI version 5</p>
<dt>=gnu</p>
<dd> &#8211; EABI GNU</p>
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
<dt>=v67</p>
<dd> &#8211; Build for HVX v67</p>
<dt>=v68</p>
<dd> &#8211; Build for HVX v68</p>
<dt>=v69</p>
<dd> &#8211; Build for HVX v69</p>
<dt> <code>&#8211;mips-compact-branches=</code>&lt;value&gt; &#8211; MIPS Specific: Compact branch policy.</p>
<dt>=never</p>
<dd> &#8211; Do not use compact branches if possible.</p>
<dt>=optimal</p>
<dd> &#8211; Use compact branches where appropriate (default).</p>
<dt>=always</p>
<dd> &#8211; Always use compact branches if possible.</p>
<dt> <code>&#8211;mips16-constant-islands</code> &#8211; Enable mips16 constant islands.</p>
<dt> <code>&#8211;mips16-hard-float</code> &#8211; Enable mips16 hard float.</p>
<dt> <code>&#8211;mir-strip-debugify-only</code> &#8211; Should mir-strip-debug only strip debug info from debugified modules by default</p>
<dt> <code>&#8211;mno-compound</code> &#8211; Disable looking for compound instructions for Hexagon</p>
<dt> <code>&#8211;mno-fixup</code> &#8211; Disable fixing up resolved relocations for Hexagon</p>
<dt> <code>&#8211;mno-ldc1-sdc1</code> &#8211; Expand double precision loads and stores to their single precision counterparts</p>
<dt> <code>&#8211;mno-pairing</code> &#8211; Disable looking for duplex instructions for Hexagon</p>
<dt> <code>&#8211;mtriple=</code>&lt;string&gt; &#8211; Override target triple for module</p>
<dt> <code>&#8211;mwarn-missing-parenthesis</code> &#8211; Warn for missing parenthesis around predicate registers</p>
<dt> <code>&#8211;mwarn-noncontigious-register</code> &#8211; Warn for register names that arent contigious</p>
<dt> <code>&#8211;mwarn-sign-mismatch</code> &#8211; Warn for mismatching a signed and unsigned value</p>
<dt> <code>&#8211;no-deprecated-warn</code> &#8211; Suppress all deprecated warnings</p>
<dt> <code>&#8211;no-discriminators</code> &#8211; Disable generation of discriminator information.</p>
<dt> <code>&#8211;no-process-syms</code> &#8211; Do not resolve lli process symbols in JIT&#8217;d code</p>
<dt> <code>&#8211;no-type-check</code> &#8211; Suppress type errors (Wasm)</p>
<dt> <code>&#8211;no-warn</code> &#8211; Suppress all warnings</p>
<dt> <code>&#8211;no-xray-index</code> &#8211; Don&#8217;t emit xray_fn_idx section</p>
<dt> <code>&#8211;nozero-initialized-in-bss</code> &#8211; Don&#8217;t place zero-initialized symbols into bss section</p>
<dt> <code>&#8211;nvptx-sched4reg</code> &#8211; NVPTX Specific: schedule for register pressue</p>
<dt> <code>&#8211;object-cache-dir=</code>&lt;string&gt; &#8211; Directory to store cached object files (must be user writable)</p>
<dt> <code>&#8211;opaque-pointers</code> &#8211; Use opaque pointers</p>
<dt> <code>&#8211;per-module-lazy</code> &#8211; Performs lazy compilation on whole module boundaries rather than individual functions</p>
<dt> <code>&#8211;poison-checking-function-local</code> &#8211; Check that returns are non-poison (for testing)</p>
<dt> <code>&#8211;print-pipeline-passes</code> &#8211; Print a &#8216;-passes&#8217; compatible string describing the pipeline (best-effort only).</p>
<dt> <code>&#8211;r600-ir-structurize</code> &#8211; Use StructurizeCFG IR pass</p>
<dt> <code>&#8211;rdf-dump</code> &#8211;</p>
<dt> <code>&#8211;rdf-limit=</code>&lt;uint&gt; &#8211;</p>
<dt> <code>&#8211;relax-elf-relocations</code> &#8211; Emit GOTPCRELX/REX_GOTPCRELX instead of GOTPCREL on x86-64 ELF</p>
<dt> <code>&#8211;relocation-model=</code>&lt;value&gt; &#8211; Choose relocation model</p>
<dt>=static</p>
<dd> &#8211; Non-relocatable code</p>
<dt>=pic</p>
<dd> &#8211; Fully relocatable, position independent code</p>
<dt>=dynamic-no-pic</p>
<dd> &#8211; Relocatable external references, non-relocatable code</p>
<dt>=ropi</p>
<dd> &#8211; Code and read-only data relocatable, accessed PC-relative</p>
<dt>=rwpi</p>
<dd> &#8211; Read-write data relocatable, accessed relative to static base</p>
<dt>=ropi-rwpi</p>
<dd> &#8211; Combination of ropi and rwpi</p>
<dt> <code>&#8211;remote-mcjit</code> &#8211; Execute MCJIT&#8217;ed code in a separate process.</p>
<dt> <code>&#8211;runtime-counter-relocation</code> &#8211; Enable relocating counters at runtime.</p>
<dt> <code>&#8211;safepoint-ir-verifier-print-only</code> &#8211;</p>
<dt> <code>&#8211;sample-profile-check-record-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of records in the input profile are matched to the IR.</p>
<dt> <code>&#8211;sample-profile-check-sample-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of samples in the input profile are matched to the IR.</p>
<dt> <code>&#8211;sample-profile-max-propagate-iterations=</code>&lt;uint&gt; &#8211; Maximum number of iterations to go through when propagating sample block/edge weights through the CFG.</p>
<dt> <code>&#8211;skip-ret-exit-block</code> &#8211; Suppress counter promotion if exit blocks contain ret.</p>
<dt> <code>&#8211;soft-float</code> &#8211; Generate software floating point library calls</p>
<dt><code>&#8211;speculative-counter-promotion-max-exiting=</code>&lt;uint&gt; &#8211; The max number of exiting blocks of a loop to allow</p>
<dd>
<dd>speculative counter promotion</p>
<dt><code>&#8211;speculative-counter-promotion-to-loop</code> &#8211; When the option is false, if the target block is in a loop, the promotion will be disallowed unless the promoted counter</p>
<dd> update can be further/iteratively promoted into an acyclic region.</p>
<dt> <code>&#8211;split-machine-functions</code> &#8211; Split out cold basic blocks from machine functions based on profile information</p>
<dt> <code>&#8211;stack-size-section</code> &#8211; Emit a section containing stack size metadata</p>
<dt> <code>&#8211;stack-symbol-ordering</code> &#8211; Order local stack symbols.</p>
<dt> <code>&#8211;stackrealign</code> &#8211; Force align the stack to the minimum alignment</p>
<dt> <code>&#8211;strict-dwarf</code> &#8211; use strict dwarf</p>
<dt> <code>&#8211;summary-file=</code>&lt;string&gt; &#8211; The summary file to use for function importing.</p>
<dt> <code>&#8211;swift-async-fp=</code>&lt;value&gt; &#8211; Determine when the Swift async frame pointer should be set</p>
<dt>=auto</p>
<dd> &#8211; Determine based on deployment target</p>
<dt>=always</p>
<dd> &#8211; Always set the bit</p>
<dt>=never</p>
<dd> &#8211; Never set the bit</p>
<dt> <code>&#8211;tail-predication=</code>&lt;value&gt; &#8211; MVE tail-predication pass options</p>
<dt>=disabled</p>
<dd> &#8211; Don&#8217;t tail-predicate loops</p>
<dt>=enabled-no-reductions</p>
<dd> &#8211; Enable tail-predication, but not for reduction loops</p>
<dt>=enabled</p>
<dd> &#8211; Enable tail-predication, including reduction loops</p>
<dt>=force-enabled-no-reductions</p>
<dd> &#8211; Enable tail-predication, but not for reduction loops, and force this which might be unsafe</p>
<dt>=force-enabled</p>
<dd> &#8211; Enable tail-predication, including reduction loops, and force this which might be unsafe</p>
<dt> <code>&#8211;tailcallopt</code> &#8211; Turn fastcc calls into tail calls by (potentially) changing ABI.</p>
<dt> <code>&#8211;thinlto-assume-merged</code> &#8211; Assume the input has already undergone ThinLTO function importing and the other pre-optimization pipeline changes.</p>
<dt> <code>&#8211;thread-entry=</code>&lt;string&gt; &#8211; calls the given entry-point on a new thread (jit-kind=orc-lazy only)</p>
<dt> <code>&#8211;thread-model=</code>&lt;value&gt; &#8211; Choose threading model</p>
<dt>=posix</p>
<dd> &#8211; POSIX thread model</p>
<dt>=single</p>
<dd> &#8211; Single thread model</p>
<dt> <code>&#8211;threads=</code>&lt;int&gt; &#8211;</p>
<dt> <code>&#8211;tls-size=</code>&lt;uint&gt; &#8211; Bit size of immediate TLS offsets</p>
<dt> <code>&#8211;unique-basic-block-section-names</code> &#8211; Give unique names to every basic block section</p>
<dt> <code>&#8211;unique-section-names</code> &#8211; Give unique names to every section</p>
<dt> <code>&#8211;use-ctors</code> &#8211; Use .ctors instead of .init_array.</p>
<dt> <code>&#8211;vec-extabi</code> &#8211; Enable the AIX Extended Altivec ABI.</p>
<dt> <code>&#8211;verify-region-info</code> &#8211; Verify region info (time consuming)</p>
<dt> <code>&#8211;vp-counters-per-site=</code>&lt;number&gt; &#8211; The average number of profile counters allocated per value profiling site.</p>
<dt> <code>&#8211;vp-static-alloc</code> &#8211; Do static counter allocation for value profiler</p>
<dt> <code>&#8211;wasm-enable-eh</code> &#8211; WebAssembly exception handling</p>
<dt> <code>&#8211;wasm-enable-sjlj</code> &#8211; WebAssembly setjmp/longjmp handling</p>
<dt><code>&#8211;x86-align-branch=</code>&lt;string&gt; &#8211; Specify types of branches to align (plus separated list of types):</p>
<dd>
<dd>jcc indicates conditional jumps fused indicates fused conditional jumps jmp indicates direct unconditional jumps call indicates direct and indirect calls ret indicates rets indirect indicates indirect unconditional jumps</p>
<dt> <code>&#8211;x86-align-branch-boundary=</code>&lt;uint&gt; &#8211; Control how the assembler should align branches with NOP. If the boundary&#8217;s size is not 0, it should be a power of 2 and no less than 32. Branches will be aligned to prevent from being across or against the boundary of specified size. The default value 0 does not align branches.</p>
<dt><code>&#8211;x86-branches-within-32B-boundaries</code> &#8211; Align selected instructions to mitigate negative performance impact of Intel&#8217;s micro code update for errata skx102.</p>
<dd>
<dd>May break assumptions about labels corresponding to particular instructions, and should be used with caution.</p>
<dt> <code>&#8211;x86-pad-max-prefix-size=</code>&lt;uint&gt; &#8211; Maximum number of prefixes to use for padding</p>
<dt> <code>&#8211;xcoff-traceback-table</code> &#8211; Emit the XCOFF traceback table</dl>
<dd>Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dl>
<dd>Polly Options: Configure the polly loop optimizer</p>
<dl>
<dt> <code>&#8211;polly</code> &#8211; Enable the polly optimizer (with <code>-O1</code>, <code>-O2</code> or <code>-O3</code>)</p>
<dt> <code>&#8211;polly-2nd-level-tiling</code> &#8211; Enable a 2nd level loop of loop tiling</p>
<dt> <code>&#8211;polly-ast-print-accesses</code> &#8211; Print memory access functions</p>
<dt> <code>&#8211;polly-context=</code>&lt;isl parameter set&gt; &#8211; Provide additional constraints on the context parameters</p>
<dt> <code>&#8211;polly-dce-precise-steps=</code>&lt;int&gt; &#8211; The number of precise steps between two approximating iterations. (A value of <code>-1</code> schedules another approximation stage before the actual dead code elimination.</p>
<dt> <code>&#8211;polly-delicm-max-ops=</code>&lt;int&gt; &#8211; Maximum number of isl operations to invest for lifetime analysis; 0=no limit</p>
<dt> <code>&#8211;polly-detect-full-functions</code> &#8211; Allow the detection of full functions</p>
<dt> <code>&#8211;polly-dump-after</code> &#8211; Dump module after Polly transformations into a file suffixed with &quot;-after&quot;</p>
<dt> <code>&#8211;polly-dump-after-file=</code>&lt;string&gt; &#8211; Dump module after Polly transformations to the given file</p>
<dt> <code>&#8211;polly-dump-before</code> &#8211; Dump module before Polly transformations into a file suffixed with &quot;-before&quot;</p>
<dt> <code>&#8211;polly-dump-before-file=</code>&lt;string&gt; &#8211; Dump module before Polly transformations to the given file</p>
<dt> <code>&#8211;polly-enable-simplify</code> &#8211; Simplify SCoP after optimizations</p>
<dt> <code>&#8211;polly-ignore-func=</code>&lt;string&gt; &#8211; Ignore functions that match a regex. Multiple regexes can be comma separated. Scop detection will ignore all functions that match ANY of the regexes provided.</p>
<dt> <code>&#8211;polly-isl-arg=</code>&lt;argument&gt; &#8211; Option passed to ISL</p>
<dt> <code>&#8211;polly-on-isl-error-abort</code> &#8211; Abort if an isl error is encountered</p>
<dt> <code>&#8211;polly-only-func=</code>&lt;string&gt; &#8211; Only run on functions that match a regex. Multiple regexes can be comma separated. Scop detection will run on all functions that match ANY of the regexes provided.</p>
<dt> <code>&#8211;polly-only-region=</code>&lt;identifier&gt; &#8211; Only run on certain regions (The provided identifier must appear in the name of the region&#8217;s entry block</p>
<dt> <code>&#8211;polly-only-scop-detection</code> &#8211; Only run scop detection, but no other optimizations</p>
<dt> <code>&#8211;polly-optimized-scops</code> &#8211; Polly &#8211; Dump polyhedral description of Scops optimized with the isl scheduling optimizer and the set of post-scheduling transformations is applied on the schedule tree</p>
<dt> <code>&#8211;polly-parallel</code> &#8211; Generate thread parallel code (isl codegen only)</p>
<dt> <code>&#8211;polly-parallel-force</code> &#8211; Force generation of thread parallel code ignoring any cost model</p>
<dt> <code>&#8211;polly-pattern-matching-based-opts</code> &#8211; Perform optimizations based on pattern matching</p>
<dt> <code>&#8211;polly-postopts</code> &#8211; Apply post-rescheduling optimizations such as tiling (requires <code>-polly-reschedule</code>)</p>
<dt> <code>&#8211;polly-pragma-based-opts</code> &#8211; Apply user-directed transformation from metadata</p>
<dt> <code>&#8211;polly-pragma-ignore-depcheck</code> &#8211; Skip the dependency check for pragma-based transformations</p>
<dt> <code>&#8211;polly-process-unprofitable</code> &#8211; Process scops that are unlikely to benefit from Polly optimizations.</p>
<dt> <code>&#8211;polly-register-tiling</code> &#8211; Enable register tiling</p>
<dt> <code>&#8211;polly-report</code> &#8211; Print information about the activities of Polly</p>
<dt> <code>&#8211;polly-reschedule</code> &#8211; Optimize SCoPs using ISL</p>
<dt> <code>&#8211;polly-show</code> &#8211; Highlight the code regions that will be optimized in a (CFG BBs and LLVM-IR instructions)</p>
<dt> <code>&#8211;polly-show-only</code> &#8211; Highlight the code regions that will be optimized in a (CFG only BBs)</p>
<dt> <code>&#8211;polly-stmt-granularity=</code>&lt;value&gt; &#8211; Algorithm to use for splitting basic blocks into multiple statements</p>
<dt>=bb</p>
<dd> &#8211; One statement per basic block</p>
<dt>=scalar-indep</p>
<dd> &#8211; Scalar independence heuristic</p>
<dt>=store</p>
<dd> &#8211; Store-level granularity</p>
<dt> <code>&#8211;polly-target=</code>&lt;value&gt; &#8211; The hardware to target</p>
<dt>=cpu</p>
<dd> &#8211; generate CPU code</p>
<dt> <code>&#8211;polly-tiling</code> &#8211; Enable loop tiling</p>
<dt> <code>&#8211;polly-vectorizer=</code>&lt;value&gt; &#8211; Select the vectorization strategy</p>
<dt>=none</p>
<dd> &#8211; No Vectorization</p>
<dt>=polly</p>
<dd> &#8211; Polly internal vectorizer</p>
<dt>=stripmine</p>
<dd> &#8211; Strip-mine outer loops for the loop-vectorizer to trigger </p>
</dl>
<h2>Index</h2>
