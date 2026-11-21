---

title: "lli-9(1)"
name: "lli-9"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lli-9/"
description: "lli – manual page for lli 9"
---

<p> lli &#8211; manual page for lli 9 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm interpreter &amp; dynamic compiler </p>
<p> USAGE: lli [options] &lt;input bitcode&gt; &lt;program arguments&gt;&#8230; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dt></dl>
<dd>General options:</dd>
<dl>
<dt> <code>-O=</code>&lt;char&gt; &#8211; Optimization level. [-O0, <code>-O1</code>, <code>-O2</code>, or <code>-O3]</code> (default = &#8216;-O2&#8217;)</dt>
<dt> <code>&#8211;aarch64-neon-syntax=</code>&lt;value&gt; &#8211; Choose style of NEON code to emit from AArch64 backend:</dt>
<dt>=generic</dt>
<dd> &#8211; Emit generic NEON assembly</dd>
<dt>=apple</dt>
<dd> &#8211; Emit Apple-style NEON assembly</dd>
<dt> <code>&#8211;addrsig</code> &#8211; Emit an address-significance table</dt>
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
<dt> <code>&#8211;code-model=</code>&lt;value&gt; &#8211; Choose code model</dt>
<dt>=tiny</dt>
<dd> &#8211; Tiny code model</dd>
<dt>=small</dt>
<dd> &#8211; Small code model</dd>
<dt>=kernel</dt>
<dd> &#8211; Kernel code model</dd>
<dt>=medium</dt>
<dd> &#8211; Medium code model</dd>
<dt>=large</dt>
<dd> &#8211; Large code model</dd>
<dt> <code>&#8211;compile-threads=</code>&lt;uint&gt; &#8211; Choose the number of compile threads (jit-kind=orc-lazy only)</dt>
<dt> <code>&#8211;cost-kind=</code>&lt;value&gt; &#8211; Target cost kind</dt>
<dt>=throughput</dt>
<dd> &#8211; Reciprocal throughput</dd>
<dt>=latency</dt>
<dd> &#8211; Instruction latency</dd>
<dt>=code-size</dt>
<dd> &#8211; Code size</dd>
<dt> <code>&#8211;cvp-dont-add-nowrap-flags</code> &#8211;</dt>
<dt> <code>&#8211;data-sections</code> &#8211; Emit data into separate sections</dt>
<dt> <code>&#8211;debug-entry-values</code> &#8211; Emit debug info about parameter&#8217;s entry values</dt>
<dt> <code>&#8211;debugger-tune=</code>&lt;value&gt; &#8211; Tune debug info for a particular debugger</dt>
<dt>=gdb</dt>
<dd> &#8211; gdb</dd>
<dt>=lldb</dt>
<dd> &#8211; lldb</dd>
<dt>=sce</dt>
<dd> &#8211; SCE targets (e.g. PS4)</dd>
<dt> <code>&#8211;denormal-fp-math=</code>&lt;value&gt; &#8211; Select which denormal numbers the code is permitted to require</dt>
<dt>=ieee</dt>
<dd> &#8211; IEEE 754 denormal numbers</dd>
<dt>=preserve-sign</dt>
<dd> &#8211; the sign of a flushed-to-zero number is preserved in the sign of 0</dd>
<dt>=positive-zero</dt>
<dd> &#8211; denormals are flushed to positive zero</dd>
<dt> <code>&#8211;disable-lazy-compilation</code> &#8211; Disable JIT lazy compilation</dt>
<dt> <code>&#8211;disable-promote-alloca-to-lds</code> &#8211; Disable promote alloca to LDS</dt>
<dt> <code>&#8211;disable-promote-alloca-to-vector</code> &#8211; Disable promote alloca to vector</dt>
<dt> <code>&#8211;disable-tail-calls</code> &#8211; Never emit tail calls</dt>
<dt> <code>&#8211;do-counter-promotion</code> &#8211; Do counter register promotion</dt>
<dt> <code>&#8211;dwarf-version=</code>&lt;int&gt; &#8211; Dwarf version</dt>
<dt> <code>&#8211;emscripten-cxx-exceptions-whitelist=</code>&lt;string&gt; &#8211; The list of function names in which Emscripten-style exception handling is enabled (see emscripten EMSCRIPTEN_CATCHING_WHITELIST options)</dt>
<dt> <code>&#8211;emulated-tls</code> &#8211; Use emulated TLS model</dt>
<dt> <code>&#8211;enable-cache-manager</code> &#8211; Use cache manager to save/load modules</dt>
<dt> <code>&#8211;enable-cse-in-irtranslator</code> &#8211; Should enable CSE in irtranslator</dt>
<dt> <code>&#8211;enable-cse-in-legalizer</code> &#8211; Should enable CSE in Legalizer</dt>
<dt> <code>&#8211;enable-emscripten-cxx-exceptions</code> &#8211; WebAssembly Emscripten-style exception handling</dt>
<dt> <code>&#8211;enable-emscripten-sjlj</code> &#8211; WebAssembly Emscripten-style setjmp/longjmp handling</dt>
<dt> <code>&#8211;enable-gvn-memdep</code> &#8211;</dt>
<dt> <code>&#8211;enable-load-pre</code> &#8211;</dt>
<dt> <code>&#8211;enable-loop-simplifycfg-term-folding</code> &#8211;</dt>
<dt> <code>&#8211;enable-name-compression</code> &#8211; Enable name string compression</dt>
<dt> <code>&#8211;enable-no-infs-fp-math</code> &#8211; Enable FP math optimizations that assume no +-Infs</dt>
<dt> <code>&#8211;enable-no-nans-fp-math</code> &#8211; Enable FP math optimizations that assume no NaNs</dt>
<dt> <code>&#8211;enable-no-signed-zeros-fp-math</code> &#8211; Enable FP math optimizations that assume the sign of 0 is insignificant</dt>
<dt> <code>&#8211;enable-no-trapping-fp-math</code> &#8211; Enable setting the FP exceptions build attribute not to use exceptions</dt>
<dt> <code>&#8211;enable-unsafe-fp-math</code> &#8211; Enable optimizations that may decrease FP precision</dt>
<dt> <code>&#8211;entry-function=</code>&lt;function&gt; &#8211; Specify the entry function (default = &#8216;main&#8217;) of the executable</dt>
<dt> <code>&#8211;exception-model=</code>&lt;value&gt; &#8211; exception model</dt>
<dt>=default</dt>
<dd> &#8211; default exception handling model</dd>
<dt>=dwarf</dt>
<dd> &#8211; DWARF-like CFI based exception handling</dd>
<dt>=sjlj</dt>
<dd> &#8211; SjLj exception handling</dd>
<dt>=arm</dt>
<dd> &#8211; ARM EHABI exceptions</dd>
<dt>=wineh</dt>
<dd> &#8211; Windows exception model</dd>
<dt>=wasm</dt>
<dd> &#8211; WebAssembly exception handling</dd>
<dt> <code>&#8211;expensive-combines</code> &#8211; Enable expensive instruction combines</dt>
<dt> <code>&#8211;extra-archive=</code>&lt;input archive&gt; &#8211; Extra archive files to be loaded</dt>
<dt> <code>&#8211;extra-module=</code>&lt;input bitcode&gt; &#8211; Extra modules to be loaded</dt>
<dt> <code>&#8211;extra-object=</code>&lt;input object&gt; &#8211; Extra object files to be loaded</dt>
<dt> <code>&#8211;fake-argv0=</code>&lt;executable&gt; &#8211; Override the &#8216;argv[0]&#8217; value passed into the executing program</dt>
<dt> <code>&#8211;fatal-warnings</code> &#8211; Treat warnings as errors</dt>
<dt> <code>&#8211;filetype=</code>&lt;value&gt; &#8211; Choose a file type (not all types are supported by all targets):</dt>
<dt>=asm</dt>
<dd> &#8211; Emit an assembly (&#8216;.s&#8217;) file</dd>
<dt>=obj</dt>
<dd> &#8211; Emit a native object (&#8216;.o&#8217;) file</dd>
<dt>=null</dt>
<dd> &#8211; Emit nothing, for performance testing</dd>
<dt> <code>&#8211;float-abi=</code>&lt;value&gt; &#8211; Choose float ABI type</dt>
<dt>=default</dt>
<dd> &#8211; Target default float ABI type</dd>
<dt>=soft</dt>
<dd> &#8211; Soft float ABI (implied by <code>-soft-float</code>)</dd>
<dt>=hard</dt>
<dd> &#8211; Hard float ABI (uses FP registers)</dd>
<dt> <code>&#8211;force-interpreter</code> &#8211; Force interpretation: disable JIT</dt>
<dt> <code>&#8211;fp-contract=</code>&lt;value&gt; &#8211; Enable aggressive formation of fused FP ops</dt>
<dt>=fast</dt>
<dd> &#8211; Fuse FP ops whenever profitable</dd>
<dt>=on</dt>
<dd> &#8211; Only fuse &#8216;blessed&#8217; FP ops.</dd>
<dt>=off</dt>
<dd> &#8211; Only fuse FP ops when the result won&#8217;t be affected.</dd>
<dt> <code>&#8211;frame-pointer=</code>&lt;value&gt; &#8211; Specify frame pointer elimination optimization</dt>
<dt>=all</dt>
<dd> &#8211; Disable frame pointer elimination</dd>
<dt>=non-leaf</dt>
<dd> &#8211; Disable frame pointer elimination for non-leaf frame</dd>
<dt>=none</dt>
<dd> &#8211; Enable frame pointer elimination</dd>
<dt> <code>&#8211;function-sections</code> &#8211; Emit functions into separate sections</dt>
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
<dt> <code>&#8211;jd=</code>&lt;string&gt; &#8211; Specifies the JITDylib to be used for any subsequent <code>-extra-module</code> arguments.</dt>
<dt> <code>&#8211;jit-kind=</code>&lt;value&gt; &#8211; Choose underlying JIT kind.</dt>
<dt>=mcjit</dt>
<dd> &#8211; MCJIT</dd>
<dt>=orc-mcjit</dt>
<dd> &#8211; Orc-based MCJIT replacement (deprecated)</dd>
<dt>=orc-lazy</dt>
<dd> &#8211; Orc-based lazy JIT.</dd>
<dt> <code>&#8211;load=</code>&lt;pluginfilename&gt; &#8211; Load the specified plugin</dt>
<dt> <code>&#8211;lto-pass-remarks-filter=</code>&lt;regex&gt; &#8211; Only record optimization remarks from passes whose names match the given regular expression</dt>
<dt> <code>&#8211;lto-pass-remarks-format=</code>&lt;format&gt; &#8211; The format used for serializing remarks (default: YAML)</dt>
<dt> <code>&#8211;lto-pass-remarks-output=</code>&lt;filename&gt; &#8211; Output filename for pass remarks</dt>
<dt> <code>&#8211;march=</code>&lt;string&gt; &#8211; Architecture to generate code for (see <code>&#8211;version</code>)</dt>
<dt> <code>&#8211;mattr=</code>&lt;a1,+a2,-a3,&#8230;&gt; &#8211; Target specific attributes (<code>-mattr</code>=<i>,help/</i> for details)</dt>
<dt> <code>&#8211;max-counter-promotions=</code>&lt;int&gt; &#8211; Max number of allowed counter promotions</dt>
<dt> <code>&#8211;max-counter-promotions-per-loop=</code>&lt;uint&gt; &#8211; Max number counter promotions per loop to avoid increasing register pressure too much</dt>
<dt> <code>&#8211;mc-relax-all</code> &#8211; When used with filetype=obj, relax all fixups in the emitted object file</dt>
<dt><code>&#8211;mcjit-remote-process=</code>&lt;filename&gt; &#8211; Specify the filename of the process to launch for remote MCJIT execution.</dt>
<dd>
</dd><dd>If none is specified, remote execution will be simulated in-process.</dd>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</dt>
<dt> <code>&#8211;meabi=</code>&lt;value&gt; &#8211; Set EABI type (default depends on triple):</dt>
<dt>=default</dt>
<dd> &#8211; Triple default EABI version</dd>
<dt>=4</dt>
<dd> &#8211; EABI version 4</dd>
<dt>=5</dt>
<dd> &#8211; EABI version 5</dd>
<dt>=gnu</dt>
<dd> &#8211; EABI GNU</dd>
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
<dt> <code>&#8211;mtriple=</code>&lt;string&gt; &#8211; Override target triple for module</dt>
<dt> <code>&#8211;mwarn-missing-parenthesis</code> &#8211; Warn for missing parenthesis around predicate registers</dt>
<dt> <code>&#8211;mwarn-noncontigious-register</code> &#8211; Warn for register names that arent contigious</dt>
<dt> <code>&#8211;mwarn-sign-mismatch</code> &#8211; Warn for mismatching a signed and unsigned value</dt>
<dt> <code>&#8211;no-deprecated-warn</code> &#8211; Suppress all deprecated warnings</dt>
<dt> <code>&#8211;no-discriminators</code> &#8211; Disable generation of discriminator information.</dt>
<dt> <code>&#8211;no-warn</code> &#8211; Suppress all warnings</dt>
<dt> <code>&#8211;nozero-initialized-in-bss</code> &#8211; Don&#8217;t place zero-initialized symbols into bss section</dt>
<dt> <code>&#8211;nvptx-sched4reg</code> &#8211; NVPTX Specific: schedule for register pressue</dt>
<dt> <code>&#8211;object-cache-dir=</code>&lt;string&gt; &#8211; Directory to store cached object files (must be user writable)</dt>
<dt> <code>&#8211;per-module-lazy</code> &#8211; Performs lazy compilation on whole module boundaries rather than individual functions</dt>
<dt> <code>&#8211;pie-copy-relocations</code> &#8211; PIE Copy Relocations</dt>
<dt> <code>&#8211;poison-checking-function-local</code> &#8211; Check that returns are non-poison (for testing)</dt>
<dt> <code>&#8211;r600-ir-structurize</code> &#8211; Use StructurizeCFG IR pass</dt>
<dt> <code>&#8211;rdf-dump</code> &#8211;</dt>
<dt> <code>&#8211;rdf-limit=</code>&lt;uint&gt; &#8211;</dt>
<dt> <code>&#8211;relax-elf-relocations</code> &#8211; Emit GOTPCRELX/REX_GOTPCRELX instead of GOTPCREL on x86-64 ELF</dt>
<dt> <code>&#8211;relocation-model=</code>&lt;value&gt; &#8211; Choose relocation model</dt>
<dt>=static</dt>
<dd> &#8211; Non-relocatable code</dd>
<dt>=pic</dt>
<dd> &#8211; Fully relocatable, position independent code</dd>
<dt>=dynamic-no-pic</dt>
<dd> &#8211; Relocatable external references, non-relocatable code</dd>
<dt>=ropi</dt>
<dd> &#8211; Code and read-only data relocatable, accessed PC-relative</dd>
<dt>=rwpi</dt>
<dd> &#8211; Read-write data relocatable, accessed relative to static base</dd>
<dt>=ropi-rwpi</dt>
<dd> &#8211; Combination of ropi and rwpi</dd>
<dt> <code>&#8211;remarks-section</code> &#8211; Emit a section containing remark diagnostics metadata</dt>
<dt> <code>&#8211;remote-mcjit</code> &#8211; Execute MCJIT&#8217;ed code in a separate process.</dt>
<dt> <code>&#8211;safepoint-ir-verifier-print-only</code> &#8211;</dt>
<dt> <code>&#8211;sample-profile-check-record-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of records in the input profile are matched to the IR.</dt>
<dt> <code>&#8211;sample-profile-check-sample-coverage=</code>&lt;N&gt; &#8211; Emit a warning if less than N% of samples in the input profile are matched to the IR.</dt>
<dt> <code>&#8211;sample-profile-max-propagate-iterations=</code>&lt;uint&gt; &#8211; Maximum number of iterations to go through when propagating sample block/edge weights through the CFG.</dt>
<dt> <code>&#8211;soft-float</code> &#8211; Generate software floating point library calls</dt>
<dt><code>&#8211;speculative-counter-promotion-max-exiting=</code>&lt;uint&gt; &#8211; The max number of exiting blocks of a loop to allow</dt>
<dd>
</dd><dd>speculative counter promotion</dd>
<dt><code>&#8211;speculative-counter-promotion-to-loop</code> &#8211; When the option is false, if the target block is in a loop, the promotion will be disallowed unless the promoted counter</dt>
<dd> update can be further/iteratively promoted into an acyclic region.</dd>
<dt> <code>&#8211;stack-alignment=</code>&lt;uint&gt; &#8211; Override default stack alignment</dt>
<dt> <code>&#8211;stack-size-section</code> &#8211; Emit a section containing stack size metadata</dt>
<dt> <code>&#8211;stack-symbol-ordering</code> &#8211; Order local stack symbols.</dt>
<dt> <code>&#8211;stackrealign</code> &#8211; Force align the stack to the minimum alignment</dt>
<dt> <code>&#8211;summary-file=</code>&lt;string&gt; &#8211; The summary file to use for function importing.</dt>
<dt> <code>&#8211;tailcallopt</code> &#8211; Turn fastcc calls into tail calls by (potentially) changing ABI.</dt>
<dt> <code>&#8211;thread-entry=</code>&lt;string&gt; &#8211; calls the given entry-point on a new thread (jit-kind=orc-lazy only)</dt>
<dt> <code>&#8211;thread-model=</code>&lt;value&gt; &#8211; Choose threading model</dt>
<dt>=posix</dt>
<dd> &#8211; POSIX thread model</dd>
<dt>=single</dt>
<dd> &#8211; Single thread model</dd>
<dt> <code>&#8211;threads=</code>&lt;int&gt; &#8211;</dt>
<dt> <code>&#8211;time-trace-granularity=</code>&lt;uint&gt; &#8211; Minimum time granularity (in microseconds) traced by time profiler</dt>
<dt> <code>&#8211;unique-section-names</code> &#8211; Give unique names to every section</dt>
<dt> <code>&#8211;use-ctors</code> &#8211; Use .ctors instead of .init_array.</dt>
<dt> <code>&#8211;verify-region-info</code> &#8211; Verify region info (time consuming)</dt>
<dt> <code>&#8211;vp-counters-per-site=</code>&lt;number&gt; &#8211; The average number of profile counters allocated per value profiling site.</dt>
<dt> <code>&#8211;vp-static-alloc</code> &#8211; Do static counter allocation for value profiler</dt></dl>
<dd>Generic Options:</dd>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</dt>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</dt>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program </dt>
</dl>
