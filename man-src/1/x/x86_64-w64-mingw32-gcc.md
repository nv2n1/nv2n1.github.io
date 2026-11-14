---
title: "x86_64-w64-mingw32-gcc(1)"
name: "x86_64-w64-mingw32-gcc"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-w64-mingw32-gcc/"
description: "gcc – GNU project C and C++ compiler"
---

<p>gcc &#8211; GNU project C and C++ compiler </p>
<h2>Synopsis</h2>
<p>gcc [<code>-c</code>|<code>-S</code>|<code>-E</code>] [<code>-std=</code><i>standard</i>]<br />
&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>]<br />
&nbsp;<wbr>[<code>-W</code><i>warn</i>&#8230;]&nbsp;<wbr>[<code>-Wpedantic</code>]<br />
&nbsp;<wbr>[<code>-I</code><i>dir</i>&#8230;]&nbsp;<wbr>[<code>-L</code><i>dir</i>&#8230;]<br />
&nbsp;<wbr>[<code>-D</code><i>macro</i>[=<i>defn</i>]&#8230;]&nbsp;<wbr>[<code>-U</code><i>macro</i>]<br />
&nbsp;<wbr>[<code>-f</code><i>option</i>&#8230;]&nbsp;<wbr>[<code>-m</code><i>machine-option</i>&#8230;]<br />
&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr>[@<i>file</i>]&nbsp;<wbr><i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder. <code>g++</code> accepts mostly the same options as <code>gcc</code>.</p>
<h2>Description</h2>
<p>When you invoke <font SIZE="-1">GCC,</font> it normally does preprocessing, compilation, assembly and linking. The &#8220;overall options&#8221; allow you to stop this process at an intermediate stage. For example, the <code>-c</code> option says not to run the linker. Then the output consists of object files output by the assembler. </p>
<p> Other options are passed on to one stage of processing. Some options control the preprocessor and others the compiler itself. Yet other options control the assembler and linker; most of these are not documented here, since you rarely need to use any of them. </p>
<p> Most of the command-line options that you can use with <font SIZE="-1">GCC</font> are useful for C programs; when an option is only useful with another language (usually C<font SIZE="-2">++</font>), the explanation says so explicitly. If the description for a particular option does not mention a source language, you can use that option with all supported languages. </p>
<p> The <code>gcc</code> program accepts options and file names as operands. Many options have multi-letter names; therefore multiple single-letter options may <i>not</i> be grouped: <code>-dv</code> is very different from <code>-d -v</code>. </p>
<p> You can mix options and other arguments. For the most part, the order you use doesn&#8217;t matter. Order does matter when you use several options of the same kind; for example, if you specify <code>-L</code> more than once, the directories are searched in the order specified. Also, the placement of the <code>-l</code> option is significant. </p>
<p> Many options have long names starting with <code>-f</code> or with <code>-W</code>&#8212;for example, <code>-fmove-loop-invariants</code>, <code>-Wformat</code> and so on. Most of these have both positive and negative forms; the negative form of <code>-ffoo</code> is <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.</p>
<h2>Options</h2>
<h3>Option Summary</h3>
<p>Here is a summary of all the options, grouped by type. Explanations are in the following sections.</p>
<dl COMPACT>
<dt><i>Overall Options</i></p>
<dd><code>-c -S -E -o</code> <i>file</i> <code>-no-canonical-prefixes -pipe -pass-exit-codes -x</code> <i>language</i> <code>-v -### &#8211;help</code>[<code>=</code><i>class</i>[<code>,&#8230;</code>]] <code>&#8211;target-help &#8211;version -wrapper @</code><i>file</i> <code>-fplugin=</code><i>file</i> <code>-fplugin-arg-</code><i>name</i><code>=</code><i>arg</i> <code>-fdump-ada-spec</code>[<code>-slim</code>] <code>-fada-spec-parent=</code><i>unit</i> <code>-fdump-go-spec=</code><i>file</i></p>
<dt><i>C Language Options</i></p>
<dd><code>-ansi -std=</code><i>standard</i> <code>-fgnu89-inline -aux-info</code> <i>filename</i> <code>-fallow-parameterless-variadic-functions -fno-asm -fno-builtin -fno-builtin-</code><i>function</i> <code>-fhosted -ffreestanding -fopenmp -fopenmp-simd -fms-extensions -fplan9-extensions -trigraphs -traditional -traditional-cpp -fallow-single-precision -fcond-mismatch -flax-vector-conversions -fsigned-bitfields -fsigned-char -funsigned-bitfields -funsigned-char</code></p>
<dt><i>C<font SIZE="-2">++</font> Language Options</i></p>
<dd><code>-fabi-version=</code><i>n</i> <code>-fno-access-control -fcheck-new -fconstexpr-depth=</code><i>n</i> <code>-ffriend-injection -fno-elide-constructors -fno-enforce-eh-specs -ffor-scope -fno-for-scope -fno-gnu-keywords -fno-implicit-templates -fno-implicit-inline-templates -fno-implement-inlines -fms-extensions -fno-nonansi-builtins -fnothrow-opt -fno-operator-names -fno-optional-diags -fpermissive -fno-pretty-templates -frepo -fno-rtti -fstats -ftemplate-backtrace-limit=</code><i>n</i> <code>-ftemplate-depth=</code><i>n</i> <code>-fno-threadsafe-statics -fuse-cxa-atexit -fno-weak -nostdinc++ -fvisibility-inlines-hidden -fvtable-verify=</code><i>std|preinit|none</i> <code>-fvtv-counts -fvtv-debug -fvisibility-ms-compat -fext-numeric-literals -Wabi -Wconversion-null -Wctor-dtor-privacy -Wdelete-non-virtual-dtor -Wliteral-suffix -Wnarrowing -Wnoexcept -Wnon-virtual-dtor -Wreorder -Weffc++ -Wstrict-null-sentinel -Wno-non-template-friend -Wold-style-cast -Woverloaded-virtual -Wno-pmf-conversions -Wsign-promo</code></p>
<dt><i>Objective-C and Objective-C<font SIZE="-2">++</font> Language Options</i></p>
<dd><code>-fconstant-string-class=</code><i>class-name</i> <code>-fgnu-runtime -fnext-runtime -fno-nil-receivers -fobjc-abi-version=</code><i>n</i> <code>-fobjc-call-cxx-cdtors -fobjc-direct-dispatch -fobjc-exceptions -fobjc-gc -fobjc-nilcheck -fobjc-std=objc1 -freplace-objc-classes -fzero-link -gen-decls -Wassign-intercept -Wno-protocol -Wselector -Wstrict-selector-match -Wundeclared-selector</code></p>
<dt><i>Language Independent Options</i></p>
<dd><code>-fmessage-length=</code><i>n</i> <code>-fdiagnostics-show-location=</code>[<code>once</code>|<code>every-line</code>] <code>-fdiagnostics-color=</code>[<code>auto</code>|<code>never</code>|<code>always</code>] <code>-fno-diagnostics-show-option -fno-diagnostics-show-caret</code></p>
<dt><i>Warning Options</i></p>
<dd><code>-fsyntax-only -fmax-errors=</code><i>n</i> <code>-Wpedantic -pedantic-errors -w -Wextra -Wall -Waddress -Waggregate-return -Waggressive-loop-optimizations -Warray-bounds -Wno-attributes -Wno-builtin-macro-redefined -Wc++-compat -Wc++11-compat -Wcast-align -Wcast-qual -Wchar-subscripts -Wclobbered -Wcomment -Wconditionally-supported -Wconversion -Wcoverage-mismatch -Wdate-time -Wdelete-incomplete -Wno-cpp -Wno-deprecated -Wno-deprecated-declarations -Wdisabled-optimization -Wno-div-by-zero -Wdouble-promotion -Wempty-body -Wenum-compare -Wno-endif-labels -Werror -Werror=* -Wfatal-errors -Wfloat-equal -Wformat -Wformat=2 -Wno-format-contains-nul -Wno-format-extra-args -Wformat-nonliteral -Wformat-security -Wformat-y2k -Wframe-larger-than=</code><i>len</i> <code>-Wno-free-nonheap-object -Wjump-misses-init -Wignored-qualifiers -Wimplicit -Wimplicit-function-declaration -Wimplicit-int -Winit-self -Winline -Wmaybe-uninitialized -Wno-int-to-pointer-cast -Wno-invalid-offsetof -Winvalid-pch -Wlarger-than=</code><i>len</i> <code>-Wunsafe-loop-optimizations -Wlogical-op -Wlong-long -Wmain -Wmaybe-uninitialized -Wmissing-braces -Wmissing-field-initializers -Wmissing-include-dirs -Wno-multichar -Wnonnull -Wno-overflow -Wopenmp-simd -Woverlength-strings -Wpacked -Wpacked-bitfield-compat -Wpadded -Wparentheses -Wpedantic-ms-format -Wno-pedantic-ms-format -Wpointer-arith -Wno-pointer-to-int-cast -Wredundant-decls -Wno-return-local-addr -Wreturn-type -Wsequence-point -Wshadow -Wsign-compare -Wsign-conversion -Wfloat-conversion -Wsizeof-pointer-memaccess -Wstack-protector -Wstack-usage=</code><i>len</i> <code>-Wstrict-aliasing -Wstrict-aliasing=n -Wstrict-overflow -Wstrict-overflow=</code><i>n</i> <code>-Wsuggest-attribute=</code>[<code>pure</code>|<code>const</code>|<code>noreturn</code>|<code>format</code>] <code>-Wmissing-format-attribute -Wswitch -Wswitch-default -Wswitch-enum -Wsync-nand -Wsystem-headers -Wtrampolines -Wtrigraphs -Wtype-limits -Wundef -Wuninitialized -Wunknown-pragmas -Wno-pragmas -Wunsuffixed-float-constants -Wunused -Wunused-function -Wunused-label -Wunused-local-typedefs -Wunused-parameter -Wno-unused-result -Wunused-value -Wunused-variable -Wunused-but-set-parameter -Wunused-but-set-variable -Wuseless-cast -Wvariadic-macros -Wvector-operation-performance -Wvla -Wvolatile-register-var -Wwrite-strings -Wzero-as-null-pointer-constant</code></p>
<dt><i>C and Objective-C-only Warning Options</i></p>
<dd><code>-Wbad-function-cast -Wmissing-declarations -Wmissing-parameter-type -Wmissing-prototypes -Wnested-externs -Wold-style-declaration -Wold-style-definition -Wstrict-prototypes -Wtraditional -Wtraditional-conversion -Wdeclaration-after-statement -Wpointer-sign</code></p>
<dt><i>Debugging Options</i></p>
<dd><code>-d</code><i>letters</i> <code>-dumpspecs -dumpmachine -dumpversion -fsanitize=</code><i>style</i> <code>-fdbg-cnt-list -fdbg-cnt=</code><i>counter-value-list</i> <code>-fdisable-ipa-</code><i>pass_name</i> <code>-fdisable-rtl-</code><i>pass_name</i> <code>-fdisable-rtl-</code><i>pass-name</i><code>=</code><i>range-list</i> <code>-fdisable-tree-</code><i>pass_name</i> <code>-fdisable-tree-</code><i>pass-name</i><code>=</code><i>range-list</i> <code>-fdump-noaddr -fdump-unnumbered -fdump-unnumbered-links -fdump-translation-unit</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-class-hierarchy</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-ipa-all -fdump-ipa-cgraph -fdump-ipa-inline -fdump-passes -fdump-statistics -fdump-tree-all -fdump-tree-original</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-optimized</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-cfg -fdump-tree-alias -fdump-tree-ch -fdump-tree-ssa</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-pre</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-ccp</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-dce</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-gimple</code>[<code>-raw</code>] <code>-fdump-tree-dom</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-dse</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-phiprop</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-phiopt</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-forwprop</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-copyrename</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-nrv -fdump-tree-vect -fdump-tree-sink -fdump-tree-sra</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-forwprop</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-fre</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-vtable-verify -fdump-tree-vrp</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-storeccp</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-final-insns=</code><i>file</i> <code>-fcompare-debug</code>[<code>=</code><i>opts</i>] <code>-fcompare-debug-second -feliminate-dwarf2-dups -fno-eliminate-unused-debug-types -feliminate-unused-debug-symbols -femit-class-debug-always -fenable-</code><i>kind</i><code>&#8211;</code><i>pass</i> <code>-fenable-</code><i>kind</i><code>&#8211;</code><i>pass</i><code>=</code><i>range-list</i> <code>-fdebug-types-section -fmem-report-wpa -fmem-report -fpre-ipa-mem-report -fpost-ipa-mem-report -fprofile-arcs -fopt-info -fopt-info-</code><i>options</i>[<code>=</code><i>file</i>] <code>-frandom-seed=</code><i>string</i> <code>-fsched-verbose=</code><i>n</i> <code>-fsel-sched-verbose -fsel-sched-dump-cfg -fsel-sched-pipelining-verbose -fstack-usage -ftest-coverage -ftime-report -fvar-tracking -fvar-tracking-assignments -fvar-tracking-assignments-toggle -g -g</code><i>level</i> <code>-gtoggle -gcoff -gdwarf-</code><i>version</i> <code>-ggdb -grecord-gcc-switches -gno-record-gcc-switches -gstabs -gstabs+ -gstrict-dwarf -gno-strict-dwarf -gvms -gxcoff -gxcoff+ -fno-merge-debug-strings -fno-dwarf2-cfi-asm -fdebug-prefix-map=</code><i>old</i><code>=</code><i>new</i> <code>-femit-struct-debug-baseonly -femit-struct-debug-reduced -femit-struct-debug-detailed</code>[<code>=</code><i>spec-list</i>] <code>-p -pg -print-file-name=</code><i>library</i> <code>-print-libgcc-file-name -print-multi-directory -print-multi-lib -print-multi-os-directory -print-prog-name=</code><i>program</i> <code>-print-search-dirs -Q -print-sysroot -print-sysroot-headers-suffix -save-temps -save-temps=cwd -save-temps=obj -time</code>[<code>=</code><i>file</i>]</p>
<dt><i>Optimization Options</i></p>
<dd><code>-faggressive-loop-optimizations -falign-functions[=</code><i>n</i><code>] -falign-jumps[=</code><i>n</i><code>] -falign-labels[=</code><i>n</i><code>] -falign-loops[=</code><i>n</i><code>] -fassociative-math -fauto-inc-dec -fbranch-probabilities -fbranch-target-load-optimize -fbranch-target-load-optimize2 -fbtr-bb-exclusive -fcaller-saves -fcheck-data-deps -fcombine-stack-adjustments -fconserve-stack -fcompare-elim -fcprop-registers -fcrossjumping -fcse-follow-jumps -fcse-skip-blocks -fcx-fortran-rules -fcx-limited-range -fdata-sections -fdce -fdelayed-branch -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively -fdse -fearly-inlining -fipa-sra -fexpensive-optimizations -ffat-lto-objects -ffast-math -ffinite-math-only -ffloat-store -fexcess-precision=</code><i>style</i> <code>-fforward-propagate -ffp-contract=</code><i>style</i> <code>-ffunction-sections -fgcse -fgcse-after-reload -fgcse-las -fgcse-lm -fgraphite-identity -fgcse-sm -fhoist-adjacent-loads -fif-conversion -fif-conversion2 -findirect-inlining -finline-functions -finline-functions-called-once -finline-limit=</code><i>n</i> <code>-finline-small-functions -fipa-cp -fipa-cp-clone -fipa-pta -fipa-profile -fipa-pure-const -fipa-reference -fira-algorithm=</code><i>algorithm</i> <code>-fira-region=</code><i>region</i> <code>-fira-hoist-pressure -fira-loop-pressure -fno-ira-share-save-slots -fno-ira-share-spill-slots -fira-verbose=</code><i>n</i> <code>-fisolate-erroneous-paths-dereference -fisolate-erroneous-paths-attribute -fivopts -fkeep-inline-functions -fkeep-static-consts -flive-range-shrinkage -floop-block -floop-interchange -floop-strip-mine -floop-nest-optimize -floop-parallelize-all -flto -flto-compression-level -flto-partition=</code><i>alg</i> <code>-flto-report -flto-report-wpa -fmerge-all-constants -fmerge-constants -fmodulo-sched -fmodulo-sched-allow-regmoves -fmove-loop-invariants -fno-branch-count-reg -fno-defer-pop -fno-function-cse -fno-guess-branch-probability -fno-inline -fno-math-errno -fno-peephole -fno-peephole2 -fno-sched-interblock -fno-sched-spec -fno-signed-zeros -fno-toplevel-reorder -fno-trapping-math -fno-zero-initialized-in-bss -fomit-frame-pointer -foptimize-sibling-calls -fpartial-inlining -fpeel-loops -fpredictive-commoning -fprefetch-loop-arrays -fprofile-report -fprofile-correction -fprofile-dir=</code><i>path</i> <code>-fprofile-generate -fprofile-generate=</code><i>path</i> <code>-fprofile-use -fprofile-use=</code><i>path</i> <code>-fprofile-values -fprofile-reorder-functions -freciprocal-math -free -frename-registers -freorder-blocks -freorder-blocks-and-partition -freorder-functions -frerun-cse-after-loop -freschedule-modulo-scheduled-loops -frounding-math -fsched2-use-superblocks -fsched-pressure -fsched-spec-load -fsched-spec-load-dangerous -fsched-stalled-insns-dep[=</code><i>n</i><code>] -fsched-stalled-insns[=</code><i>n</i><code>] -fsched-group-heuristic -fsched-critical-path-heuristic -fsched-spec-insn-heuristic -fsched-rank-heuristic -fsched-last-insn-heuristic -fsched-dep-count-heuristic -fschedule-insns -fschedule-insns2 -fsection-anchors -fselective-scheduling -fselective-scheduling2 -fsel-sched-pipelining -fsel-sched-pipelining-outer-loops -fshrink-wrap -fsignaling-nans -fsingle-precision-constant -fsplit-ivs-in-unroller -fsplit-wide-types -fstack-protector -fstack-protector-all -fstack-protector-strong -fstrict-aliasing -fstrict-overflow -fthread-jumps -ftracer -ftree-bit-ccp -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-inline-vars -ftree-coalesce-vars -ftree-copy-prop -ftree-copyrename -ftree-dce -ftree-dominator-opts -ftree-dse -ftree-forwprop -ftree-fre -ftree-loop-if-convert -ftree-loop-if-convert-stores -ftree-loop-im -ftree-phiprop -ftree-loop-distribution -ftree-loop-distribute-patterns -ftree-loop-ivcanon -ftree-loop-linear -ftree-loop-optimize -ftree-loop-vectorize -ftree-parallelize-loops=</code><i>n</i> <code>-ftree-pre -ftree-partial-pre -ftree-pta -ftree-reassoc -ftree-sink -ftree-slsr -ftree-sra -ftree-switch-conversion -ftree-tail-merge -ftree-ter -ftree-vectorize -ftree-vrp -funit-at-a-time -funroll-all-loops -funroll-loops -funsafe-loop-optimizations -funsafe-math-optimizations -funswitch-loops -fvariable-expansion-in-unroller -fvect-cost-model -fvpt -fweb -fwhole-program -fwpa -fuse-ld=</code><i>linker</i> <code>-fuse-linker-plugin &#8211;param</code> <i>name</i><code>=</code><i>value</i> <code>-O -O0 -O1 -O2 -O3 -Os -Ofast -Og</code></p>
<dt><i>Preprocessor Options</i></p>
<dd><code>-A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -dD -dI -dM -dN -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-E -H -idirafter</code> <i>dir</i> <code>-include</code> <i>file</i> <code>-imacros</code> <i>file</i> <code>-iprefix</code> <i>file</i> <code>-iwithprefix</code> <i>dir</i> <code>-iwithprefixbefore</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-imultilib</code> <i>dir</i> <code>-isysroot</code> <i>dir</i> <code>-M -MM -MF -MG -MP -MQ -MT -nostdinc -P -fdebug-cpp -ftrack-macro-expansion -fworking-directory -remap -trigraphs -undef -U</code><i>macro</i> <code>-Wp,</code><i>option</i> <code>-Xpreprocessor</code> <i>option</i> <code>-no-integrated-cpp</code></p>
<dt><i>Assembler Option</i></p>
<dd><code>-Wa,</code><i>option</i> <code>-Xassembler</code> <i>option</i></p>
<dt><i>Linker Options</i></p>
<dd><i>object-file-name</i> <code>-l</code><i>library</i> <code>-nostartfiles -nodefaultlibs -nostdlib -pie -rdynamic -s -static -static-libgcc -static-libstdc++ -static-libasan -static-libtsan -static-liblsan -static-libubsan -shared -shared-libgcc -symbolic -T</code> <i>script</i> <code>-Wl,</code><i>option</i> <code>-Xlinker</code> <i>option</i> <code>-u</code> <i>symbol</i></p>
<dt><i>Directory Options</i></p>
<dd><code>-B</code><i>prefix</i> <code>-I</code><i>dir</i> <code>-iplugindir=</code><i>dir</i> <code>-iquote</code><i>dir</i> <code>-L</code><i>dir</i> <code>-specs=</code><i>file</i> <code>-I- &#8211;sysroot=</code><i>dir</i> <code>&#8211;no-sysroot-suffix</code></p>
<dt><i>Machine Dependent Options</i></p>
<dd><i>AArch64 Options</i> <code>-mabi=</code><i>name</i> <code>-mbig-endian -mlittle-endian -mgeneral-regs-only -mcmodel=tiny -mcmodel=small -mcmodel=large -mstrict-align -momit-leaf-frame-pointer -mno-omit-leaf-frame-pointer -mtls-dialect=desc -mtls-dialect=traditional -mfix-cortex-a53-835769 -mno-fix-cortex-a53-835769 -mfix-cortex-a53-843419 -mno-fix-cortex-a53-843419 -march=</code><i>name</i> <code>-mcpu=</code><i>name</i> <code>-mtune=</code><i>name</i> </p>
<p> <i>Adapteva Epiphany Options</i> <code>-mhalf-reg-file -mprefer-short-insn-regs -mbranch-cost=</code><i>num</i> <code>-mcmove -mnops=</code><i>num</i> <code>-msoft-cmpsf -msplit-lohi -mpost-inc -mpost-modify -mstack-offset=</code><i>num</i> <code>-mround-nearest -mlong-calls -mshort-calls -msmall16 -mfp-mode=</code><i>mode</i> <code>-mvect-double -max-vect-align=</code><i>num</i> <code>-msplit-vecmove-early -m1reg-</code><i>reg</i> </p>
<p> <i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i> <code>-mbarrel-shifter -mcpu=</code><i>cpu</i> <code>-mA6 -mARC600 -mA7 -mARC700 -mdpfp -mdpfp-compact -mdpfp-fast -mno-dpfp-lrsr -mea -mno-mpy -mmul32x16 -mmul64 -mnorm -mspfp -mspfp-compact -mspfp-fast -msimd -msoft-float -mswap -mcrc -mdsp-packa -mdvbf -mlock -mmac-d16 -mmac-24 -mrtsc -mswape -mtelephony -mxy -misize -mannotate-align -marclinux -marclinux_prof -mepilogue-cfi -mlong-calls -mmedium-calls -msdata -mucb-mcount -mvolatile-cache -malign-call -mauto-modify-reg -mbbit-peephole -mno-brcc -mcase-vector-pcrel -mcompact-casesi -mno-cond-exec -mearly-cbranchsi -mexpand-adddi -mindexed-loads -mlra -mlra-priority-none -mlra-priority-compact mlra-priority-noncompact -mno-millicode -mmixed-code -mq-class -mRcq -mRcw -msize-level=</code><i>level</i> <code>-mtune=</code><i>cpu</i> <code>-mmultcost=</code><i>num</i> <code>-munalign-prob-threshold=</code><i>probability</i> </p>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i> <code>-mapcs-frame -mno-apcs-frame -mabi=</code><i>name</i> <code>-mapcs-stack-check -mno-apcs-stack-check -mapcs-float -mno-apcs-float -mapcs-reentrant -mno-apcs-reentrant -msched-prolog -mno-sched-prolog -mlittle-endian -mbig-endian -mwords-little-endian -mfloat-abi=</code><i>name</i> <code>-mfp16-format=</code><i>name</i> <code>-mthumb-interwork -mno-thumb-interwork -mcpu=</code><i>name</i> <code>-march=</code><i>name</i> <code>-mfpu=</code><i>name</i> <code>-mstructure-size-boundary=</code><i>n</i> <code>-mabort-on-noreturn -mlong-calls -mno-long-calls -msingle-pic-base -mno-single-pic-base -mpic-register=</code><i>reg</i> <code>-mnop-fun-dllimport -mpoke-function-name -mthumb -marm -mtpcs-frame -mtpcs-leaf-frame -mcaller-super-interworking -mcallee-super-interworking -mtp=</code><i>name</i> <code>-mtls-dialect=</code><i>dialect</i> <code>-mword-relocations -mfix-cortex-m3-ldrd -munaligned-access -mneon-for-64bits -mslow-flash-data -mrestrict-it</code> </p>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i> <code>-mmcu=</code><i>mcu</i> <code>-maccumulate-args -mbranch-cost=</code><i>cost</i> <code>-mcall-prologues -mint8 -mno-interrupts -mrelax -mstrict-X -mtiny-stack -Waddr-space-convert</code> </p>
<p> <i>Blackfin Options</i> <code>-mcpu=</code><i>cpu</i>[<code>&#8211;</code><i>sirevision</i>] <code>-msim -momit-leaf-frame-pointer -mno-omit-leaf-frame-pointer -mspecld-anomaly -mno-specld-anomaly -mcsync-anomaly -mno-csync-anomaly -mlow-64k -mno-low64k -mstack-check-l1 -mid-shared-library -mno-id-shared-library -mshared-library-id=</code><i>n</i> <code>-mleaf-id-shared-library -mno-leaf-id-shared-library -msep-data -mno-sep-data -mlong-calls -mno-long-calls -mfast-fp -minline-plt -mmulticore -mcorea -mcoreb -msdram -micplb</code> </p>
<p> <i>C6X Options</i> <code>-mbig-endian -mlittle-endian -march=</code><i>cpu</i> <code>-msim -msdata=</code><i>sdata-type</i> </p>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i> <code>-mcpu=</code><i>cpu</i> <code>-march=</code><i>cpu</i> <code>-mtune=</code><i>cpu</i> <code>-mmax-stack-frame=</code><i>n</i> <code>-melinux-stacksize=</code><i>n</i> <code>-metrax4 -metrax100 -mpdebug -mcc-init -mno-side-effects -mstack-align -mdata-align -mconst-align -m32-bit -m16-bit -m8-bit -mno-prologue-epilogue -mno-gotplt -melf -maout -melinux -mlinux -sim -sim2 -mmul-bug-workaround -mno-mul-bug-workaround</code> </p>
<p> <i></i><font SIZE="-1"><i>CR16</i></font><i> Options</i> <code>-mmac -mcr16cplus -mcr16c -msim -mint32 -mbit-ops -mdata-model=</code><i>model</i> </p>
<p> <i>Darwin Options</i> <code>-all_load -allowable_client -arch -arch_errors_fatal -arch_only -bind_at_load -bundle -bundle_loader -client_name -compatibility_version -current_version -dead_strip -dependency-file -dylib_file -dylinker_install_name -dynamic -dynamiclib -exported_symbols_list -filelist -flat_namespace -force_cpusubtype_ALL -force_flat_namespace -headerpad_max_install_names -iframework -image_base -init -install_name -keep_private_externs -multi_module -multiply_defined -multiply_defined_unused -noall_load -no_dead_strip_inits_and_terms -nofixprebinding -nomultidefs -noprebind -noseglinkedit -pagezero_size -prebind -prebind_all_twolevel_modules -private_bundle -read_only_relocs -sectalign -sectobjectsymbols -whyload -seg1addr -sectcreate -sectobjectsymbols -sectorder -segaddr -segs_read_only_addr -segs_read_write_addr -seg_addr_table -seg_addr_table_filename -seglinkedit -segprot -segs_read_only_addr -segs_read_write_addr -single_module -static -sub_library -sub_umbrella -twolevel_namespace -umbrella -undefined -unexported_symbols_list -weak_reference_mismatches -whatsloaded -F -gused -gfull -mmacosx-version-min=</code><i>version</i> <code>-mkernel -mone-byte-bool</code> </p>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha Options</i> <code>-mno-fp-regs -msoft-float -mieee -mieee-with-inexact -mieee-conformant -mfp-trap-mode=</code><i>mode</i> <code>-mfp-rounding-mode=</code><i>mode</i> <code>-mtrap-precision=</code><i>mode</i> <code>-mbuild-constants -mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mbwx -mmax -mfix -mcix -mfloat-vax -mfloat-ieee -mexplicit-relocs -msmall-data -mlarge-data -msmall-text -mlarge-text -mmemory-latency=</code><i>time</i> </p>
<p> <i></i><font SIZE="-1"><i>FR30</i></font><i> Options</i> <code>-msmall-model -mno-lsim</code> </p>
<p> <i></i><font SIZE="-1"><i>FRV</i></font><i> Options</i> <code>-mgpr-32 -mgpr-64 -mfpr-32 -mfpr-64 -mhard-float -msoft-float -malloc-cc -mfixed-cc -mdword -mno-dword -mdouble -mno-double -mmedia -mno-media -mmuladd -mno-muladd -mfdpic -minline-plt -mgprel-ro -multilib-library-pic -mlinked-fp -mlong-calls -malign-labels -mlibrary-pic -macc-4 -macc-8 -mpack -mno-pack -mno-eflags -mcond-move -mno-cond-move -moptimize-membar -mno-optimize-membar -mscc -mno-scc -mcond-exec -mno-cond-exec -mvliw-branch -mno-vliw-branch -mmulti-cond-exec -mno-multi-cond-exec -mnested-cond-exec -mno-nested-cond-exec -mtomcat-stats -mTLS -mtls -mcpu=</code><i>cpu</i> </p>
<p> <i>GNU/Linux Options</i> <code>-mglibc -muclibc -mbionic -mandroid -tno-android-cc -tno-android-ld</code> </p>
<p> <i>H8/300 Options</i> <code>-mrelax -mh -ms -mn -mexr -mno-exr -mint32 -malign-300</code> </p>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i> <code>-march=</code><i>architecture-type</i> <code>-mdisable-fpregs -mdisable-indexing -mfast-indirect-calls -mgas -mgnu-ld -mhp-ld -mfixed-range=</code><i>register-range</i> <code>-mjump-in-delay -mlinker-opt -mlong-calls -mlong-load-store -mno-disable-fpregs -mno-disable-indexing -mno-fast-indirect-calls -mno-gas -mno-jump-in-delay -mno-long-load-store -mno-portable-runtime -mno-soft-float -mno-space-regs -msoft-float -mpa-risc-1-0 -mpa-risc-1-1 -mpa-risc-2-0 -mportable-runtime -mschedule=</code><i>cpu-type</i> <code>-mspace-regs -msio -mwsio -munix=</code><i>unix-std</i> <code>-nolibdld -static -threads</code> </p>
<p> <i>i386 and x86-64 Options</i> <code>-mtune=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mtune-ctrl=</code><i>feature-list</i> <code>-mdump-tune-features -mno-default -mfpmath=</code><i>unit</i> <code>-masm=</code><i>dialect</i> <code>-mno-fancy-math-387 -mno-fp-ret-in-387 -msoft-float -mno-wide-multiply -mrtd -malign-double -mpreferred-stack-boundary=</code><i>num</i> <code>-mincoming-stack-boundary=</code><i>num</i> <code>-mcld -mcx16 -msahf -mmovbe -mcrc32 -mrecip -mrecip=</code><i>opt</i> <code>-mvzeroupper -mprefer-avx128 -mmmx -msse -msse2 -msse3 -mssse3 -msse4.1 -msse4.2 -msse4 -mavx -mavx2 -mavx512f -mavx512pf -mavx512er -mavx512cd -msha -maes -mpclmul -mfsgsbase -mrdrnd -mf16c -mfma -mprefetchwt1 -msse4a -m3dnow -mpopcnt -mabm -mbmi -mtbm -mfma4 -mxop -mlzcnt -mbmi2 -mfxsr -mxsave -mxsaveopt -mrtm -mlwp -mthreads -mno-align-stringops -minline-all-stringops -minline-stringops-dynamically -mstringop-strategy=</code><i>alg</i> <code>-mmemcpy-strategy=</code><i>strategy</i> <code>-mmemset-strategy=</code><i>strategy</i> <code>-mpush-args -maccumulate-outgoing-args -m128bit-long-double -m96bit-long-double -mlong-double-64 -mlong-double-80 -mlong-double-128 -mregparm=</code><i>num</i> <code>-msseregparm -mveclibabi=</code><i>type</i> <code>-mvect8-ret-in-mem -mpc32 -mpc64 -mpc80 -mstackrealign -momit-leaf-frame-pointer -mno-red-zone -mno-tls-direct-seg-refs -mcmodel=</code><i>code-model</i> <code>-mabi=</code><i>name</i> <code>-maddress-mode=</code><i>mode</i> <code>-m32 -m64 -mx32 -m16 -mlarge-data-threshold=</code><i>num</i> <code>-msse2avx -mfentry -m8bit-idiv -mavx256-split-unaligned-load -mavx256-split-unaligned-store -mstack-protector-guard=</code><i>guard</i> </p>
<p> <i>i386 and x86-64 Windows Options</i> <code>-mconsole -mcygwin -mno-cygwin -mdll -mnop-fun-dllimport -mthread -municode -mwin32 -mwindows -fno-set-stack-executable</code> </p>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i> <code>-mbig-endian -mlittle-endian -mgnu-as -mgnu-ld -mno-pic -mvolatile-asm-stop -mregister-names -msdata -mno-sdata -mconstant-gp -mauto-pic -mfused-madd -minline-float-divide-min-latency -minline-float-divide-max-throughput -mno-inline-float-divide -minline-int-divide-min-latency -minline-int-divide-max-throughput -mno-inline-int-divide -minline-sqrt-min-latency -minline-sqrt-max-throughput -mno-inline-sqrt -mdwarf2-asm -mearly-stop-bits -mfixed-range=</code><i>register-range</i> <code>-mtls-size=</code><i>tls-size</i> <code>-mtune=</code><i>cpu-type</i> <code>-milp32 -mlp64 -msched-br-data-spec -msched-ar-data-spec -msched-control-spec -msched-br-in-data-spec -msched-ar-in-data-spec -msched-in-control-spec -msched-spec-ldc -msched-spec-control-ldc -msched-prefer-non-data-spec-insns -msched-prefer-non-control-spec-insns -msched-stop-bits-after-every-cycle -msched-count-spec-in-critical-path -msel-sched-dont-check-control-spec -msched-fp-mem-deps-zero-cost -msched-max-memory-insns-hard-limit -msched-max-memory-insns=</code><i>max-insns</i> </p>
<p> <i></i><font SIZE="-1"><i>LM32</i></font><i> Options</i> <code>-mbarrel-shift-enabled -mdivide-enabled -mmultiply-enabled -msign-extend-enabled -muser-enabled</code> </p>
<p> <i>M32R/D Options</i> <code>-m32r2 -m32rx -m32r -mdebug -malign-loops -mno-align-loops -missue-rate=</code><i>number</i> <code>-mbranch-cost=</code><i>number</i> <code>-mmodel=</code><i>code-size-model-type</i> <code>-msdata=</code><i>sdata-type</i> <code>-mno-flush-func -mflush-func=</code><i>name</i> <code>-mno-flush-trap -mflush-trap=</code><i>number</i> <code>-G</code> <i>num</i> </p>
<p> <i>M32C Options</i> <code>-mcpu=</code><i>cpu</i> <code>-msim -memregs=</code><i>number</i> </p>
<p> <i>M680x0 Options</i> <code>-march=</code><i>arch</i> <code>-mcpu=</code><i>cpu</i> <code>-mtune=</code><i>tune</i> <code>-m68000 -m68020 -m68020-40 -m68020-60 -m68030 -m68040 -m68060 -mcpu32 -m5200 -m5206e -m528x -m5307 -m5407 -mcfv4e -mbitfield -mno-bitfield -mc68000 -mc68020 -mnobitfield -mrtd -mno-rtd -mdiv -mno-div -mshort -mno-short -mhard-float -m68881 -msoft-float -mpcrel -malign-int -mstrict-align -msep-data -mno-sep-data -mshared-library-id=n -mid-shared-library -mno-id-shared-library -mxgot -mno-xgot</code> </p>
<p> <i>MCore Options</i> <code>-mhardlit -mno-hardlit -mdiv -mno-div -mrelax-immediates -mno-relax-immediates -mwide-bitfields -mno-wide-bitfields -m4byte-functions -mno-4byte-functions -mcallgraph-data -mno-callgraph-data -mslow-bytes -mno-slow-bytes -mno-lsim -mlittle-endian -mbig-endian -m210 -m340 -mstack-increment</code> </p>
<p> <i>MeP Options</i> <code>-mabsdiff -mall-opts -maverage -mbased=</code><i>n</i> <code>-mbitops -mc=</code><i>n</i> <code>-mclip -mconfig=</code><i>name</i> <code>-mcop -mcop32 -mcop64 -mivc2 -mdc -mdiv -meb -mel -mio-volatile -ml -mleadz -mm -mminmax -mmult -mno-opts -mrepeat -ms -msatur -msdram -msim -msimnovec -mtf -mtiny=</code><i>n</i> </p>
<p> <i>MicroBlaze Options</i> <code>-msoft-float -mhard-float -msmall-divides -mcpu=</code><i>cpu</i> <code>-mmemcpy -mxl-soft-mul -mxl-soft-div -mxl-barrel-shift -mxl-pattern-compare -mxl-stack-check -mxl-gp-opt -mno-clearbss -mxl-multiply-high -mxl-float-convert -mxl-float-sqrt -mbig-endian -mlittle-endian -mxl-reorder -mxl-mode-</code><i>app-model</i> </p>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i> <code>-EL -EB -march=</code><i>arch</i> <code>-mtune=</code><i>arch</i> <code>-mips1 -mips2 -mips3 -mips4 -mips32 -mips32r2 -mips64 -mips64r2 -mips16 -mno-mips16 -mflip-mips16 -minterlink-compressed -mno-interlink-compressed -minterlink-mips16 -mno-interlink-mips16 -mabi=</code><i>abi</i> <code>-mabicalls -mno-abicalls -mshared -mno-shared -mplt -mno-plt -mxgot -mno-xgot -mgp32 -mgp64 -mfp32 -mfp64 -mhard-float -msoft-float -mno-float -msingle-float -mdouble-float -mabs=</code><i>mode</i> <code>-mnan=</code><i>encoding</i> <code>-mdsp -mno-dsp -mdspr2 -mno-dspr2 -mmcu -mmno-mcu -meva -mno-eva -mvirt -mno-virt -mmicromips -mno-micromips -mfpu=</code><i>fpu-type</i> <code>-msmartmips -mno-smartmips -mpaired-single -mno-paired-single -mdmx -mno-mdmx -mips3d -mno-mips3d -mmt -mno-mt -mllsc -mno-llsc -mlong64 -mlong32 -msym32 -mno-sym32 -G</code><i>num</i> <code>-mlocal-sdata -mno-local-sdata -mextern-sdata -mno-extern-sdata -mgpopt -mno-gopt -membedded-data -mno-embedded-data -muninit-const-in-rodata -mno-uninit-const-in-rodata -mcode-readable=</code><i>setting</i> <code>-msplit-addresses -mno-split-addresses -mexplicit-relocs -mno-explicit-relocs -mcheck-zero-division -mno-check-zero-division -mdivide-traps -mdivide-breaks -mmemcpy -mno-memcpy -mlong-calls -mno-long-calls -mmad -mno-mad -mimadd -mno-imadd -mfused-madd -mno-fused-madd -nocpp -mfix-24k -mno-fix-24k -mfix-r4000 -mno-fix-r4000 -mfix-r4400 -mno-fix-r4400 -mfix-r10000 -mno-fix-r10000 -mfix-rm7000 -mno-fix-rm7000 -mfix-vr4120 -mno-fix-vr4120 -mfix-vr4130 -mno-fix-vr4130 -mfix-sb1 -mno-fix-sb1 -mflush-func=</code><i>func</i> <code>-mno-flush-func -mbranch-cost=</code><i>num</i> <code>-mbranch-likely -mno-branch-likely -mfp-exceptions -mno-fp-exceptions -mvr4130-align -mno-vr4130-align -msynci -mno-synci -mrelax-pic-calls -mno-relax-pic-calls -mmcount-ra-address</code> </p>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i> <code>-mlibfuncs -mno-libfuncs -mepsilon -mno-epsilon -mabi=gnu -mabi=mmixware -mzero-extend -mknuthdiv -mtoplevel-symbols -melf -mbranch-predict -mno-branch-predict -mbase-addresses -mno-base-addresses -msingle-exit -mno-single-exit</code> </p>
<p> <i></i><font SIZE="-1"><i>MN10300</i></font><i> Options</i> <code>-mmult-bug -mno-mult-bug -mno-am33 -mam33 -mam33-2 -mam34 -mtune=</code><i>cpu-type</i> <code>-mreturn-pointer-on-d0 -mno-crt0 -mrelax -mliw -msetlb</code> </p>
<p> <i>Moxie Options</i> <code>-meb -mel -mno-crt0</code> </p>
<p> <i></i><font SIZE="-1"><i>MSP430</i></font><i> Options</i> <code>-msim -masm-hex -mmcu= -mcpu= -mlarge -msmall -mrelax -mhwmult= -minrt</code> </p>
<p> <i></i><font SIZE="-1"><i>NDS32</i></font><i> Options</i> <code>-mbig-endian -mlittle-endian -mreduced-regs -mfull-regs -mcmov -mno-cmov -mperf-ext -mno-perf-ext -mv3push -mno-v3push -m16bit -mno-16bit -mgp-direct -mno-gp-direct -misr-vector-size=</code><i>num</i> <code>-mcache-block-size=</code><i>num</i> <code>-march=</code><i>arch</i> <code>-mforce-fp-as-gp -mforbid-fp-as-gp -mex9 -mctor-dtor -mrelax</code> </p>
<p> <i>Nios </i><font SIZE="-1"><i>II</i></font><i> Options</i> <code>-G</code> <i>num</i> <code>-mgpopt -mno-gpopt -mel -meb -mno-bypass-cache -mbypass-cache -mno-cache-volatile -mcache-volatile -mno-fast-sw-div -mfast-sw-div -mhw-mul -mno-hw-mul -mhw-mulx -mno-hw-mulx -mno-hw-div -mhw-div -mcustom-</code><i>insn</i><code>=</code><i>N</i> <code>-mno-custom-</code><i>insn</i> <code>-mcustom-fpu-cfg=</code><i>name</i> <code>-mhal -msmallc -msys-crt0=</code><i>name</i> <code>-msys-lib=</code><i>name</i> </p>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i> <code>-mfpu -msoft-float -mac0 -mno-ac0 -m40 -m45 -m10 -mbcopy -mbcopy-builtin -mint32 -mno-int16 -mint16 -mno-int32 -mfloat32 -mno-float64 -mfloat64 -mno-float32 -mabshi -mno-abshi -mbranch-expensive -mbranch-cheap -munix-asm -mdec-asm</code> </p>
<p> <i>picoChip Options</i> <code>-mae=</code><i>ae_type</i> <code>-mvliw-lookahead=</code><i>N</i> <code>-msymbol-as-address -mno-inefficient-warnings</code> </p>
<p> <i>PowerPC Options</i> See <font SIZE="-1">RS/6000</font> and PowerPC Options. </p>
<p> <i></i><font SIZE="-1"><i>RL78</i></font><i> Options</i> <code>-msim -mmul=none -mmul=g13 -mmul=rl78</code> </p>
<p> <i></i><font SIZE="-1"><i>RS/6000</i></font><i> and PowerPC Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mcmodel=</code><i>code-model</i> <code>-mpowerpc64 -maltivec -mno-altivec -mpowerpc-gpopt -mno-powerpc-gpopt -mpowerpc-gfxopt -mno-powerpc-gfxopt -mmfcrf -mno-mfcrf -mpopcntb -mno-popcntb -mpopcntd -mno-popcntd -mfprnd -mno-fprnd -mcmpb -mno-cmpb -mmfpgpr -mno-mfpgpr -mhard-dfp -mno-hard-dfp -mfull-toc -mminimal-toc -mno-fp-in-toc -mno-sum-in-toc -m64 -m32 -mxl-compat -mno-xl-compat -mpe -malign-power -malign-natural -msoft-float -mhard-float -mmultiple -mno-multiple -msingle-float -mdouble-float -msimple-fpu -mstring -mno-string -mupdate -mno-update -mavoid-indexed-addresses -mno-avoid-indexed-addresses -mfused-madd -mno-fused-madd -mbit-align -mno-bit-align -mstrict-align -mno-strict-align -mrelocatable -mno-relocatable -mrelocatable-lib -mno-relocatable-lib -mtoc -mno-toc -mlittle -mlittle-endian -mbig -mbig-endian -mdynamic-no-pic -maltivec -mswdiv -msingle-pic-base -mprioritize-restricted-insns=</code><i>priority</i> <code>-msched-costly-dep=</code><i>dependence_type</i> <code>-minsert-sched-nops=</code><i>scheme</i> <code>-mcall-sysv -mcall-netbsd -maix-struct-return -msvr4-struct-return -mabi=</code><i>abi-type</i> <code>-msecure-plt -mbss-plt -mblock-move-inline-limit=</code><i>num</i> <code>-misel -mno-isel -misel=yes -misel=no -mspe -mno-spe -mspe=yes -mspe=no -mpaired -mgen-cell-microcode -mwarn-cell-microcode -mvrsave -mno-vrsave -mmulhw -mno-mulhw -mdlmzb -mno-dlmzb -mfloat-gprs=yes -mfloat-gprs=no -mfloat-gprs=single -mfloat-gprs=double -mprototype -mno-prototype -msim -mmvme -mads -myellowknife -memb -msdata -msdata=</code><i>opt</i> <code>-mvxworks -G</code> <i>num</i> <code>-pthread -mrecip -mrecip=</code><i>opt</i> <code>-mno-recip -mrecip-precision -mno-recip-precision -mveclibabi=</code><i>type</i> <code>-mfriz -mno-friz -mpointers-to-nested-functions -mno-pointers-to-nested-functions -msave-toc-indirect -mno-save-toc-indirect -mpower8-fusion -mno-mpower8-fusion -mpower8-vector -mno-power8-vector -mcrypto -mno-crypto -mdirect-move -mno-direct-move -mquad-memory -mno-quad-memory -mquad-memory-atomic -mno-quad-memory-atomic -mcompat-align-parm -mno-compat-align-parm</code> </p>
<p> <i></i><font SIZE="-1"><i>RX</i></font><i> Options</i> <code>-m64bit-doubles -m32bit-doubles -fpu -nofpu -mcpu= -mbig-endian-data -mlittle-endian-data -msmall-data -msim -mno-sim -mas100-syntax -mno-as100-syntax -mrelax -mmax-constant-size= -mint-register= -mpid -mno-warn-multiple-fast-interrupts -msave-acc-in-interrupts</code> </p>
<p> <i>S/390 and zSeries Options</i> <code>-mtune=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mhard-float -msoft-float -mhard-dfp -mno-hard-dfp -mlong-double-64 -mlong-double-128 -mbackchain -mno-backchain -mpacked-stack -mno-packed-stack -msmall-exec -mno-small-exec -mmvcle -mno-mvcle -m64 -m31 -mdebug -mno-debug -mesa -mzarch -mtpf-trace -mno-tpf-trace -mfused-madd -mno-fused-madd -mwarn-framesize -mwarn-dynamicstack -mstack-size -mstack-guard -mhotpatch=</code><i>halfwords</i><code>,</code><i>halfwords</i> </p>
<p> <i>Score Options</i> <code>-meb -mel -mnhwloop -muls -mmac -mscore5 -mscore5u -mscore7 -mscore7d</code> </p>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i> <code>-m1 -m2 -m2e -m2a-nofpu -m2a-single-only -m2a-single -m2a -m3 -m3e -m4-nofpu -m4-single-only -m4-single -m4 -m4a-nofpu -m4a-single-only -m4a-single -m4a -m4al -m5-64media -m5-64media-nofpu -m5-32media -m5-32media-nofpu -m5-compact -m5-compact-nofpu -mb -ml -mdalign -mrelax -mbigtable -mfmovd -mhitachi -mrenesas -mno-renesas -mnomacsave -mieee -mno-ieee -mbitops -misize -minline-ic_invalidate -mpadstruct -mspace -mprefergot -musermode -multcost=</code><i>number</i> <code>-mdiv=</code><i>strategy</i> <code>-mdivsi3_libfunc=</code><i>name</i> <code>-mfixed-range=</code><i>register-range</i> <code>-mindexed-addressing -mgettrcost=</code><i>number</i> <code>-mpt-fixed -maccumulate-outgoing-args -minvalid-symbols -matomic-model=</code><i>atomic-model</i> <code>-mbranch-cost=</code><i>num</i> <code>-mzdcbranch -mno-zdcbranch -mfused-madd -mno-fused-madd -mfsca -mno-fsca -mfsrra -mno-fsrra -mpretend-cmove -mtas</code> </p>
<p> <i>Solaris 2 Options</i> <code>-mclear-hwcap -mno-clear-hwcap -mimpure-text -mno-impure-text -pthreads -pthread</code> </p>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mcmodel=</code><i>code-model</i> <code>-mmemory-model=</code><i>mem-model</i> <code>-m32 -m64 -mapp-regs -mno-app-regs -mfaster-structs -mno-faster-structs -mflat -mno-flat -mfpu -mno-fpu -mhard-float -msoft-float -mhard-quad-float -msoft-quad-float -mstack-bias -mno-stack-bias -munaligned-doubles -mno-unaligned-doubles -muser-mode -mno-user-mode -mv8plus -mno-v8plus -mvis -mno-vis -mvis2 -mno-vis2 -mvis3 -mno-vis3 -mcbcond -mno-cbcond -mfmaf -mno-fmaf -mpopc -mno-popc -mfix-at697f -mfix-ut699</code> </p>
<p> <i></i><font SIZE="-1"><i>SPU</i></font><i> Options</i> <code>-mwarn-reloc -merror-reloc -msafe-dma -munsafe-dma -mbranch-hints -msmall-mem -mlarge-mem -mstdmain -mfixed-range=</code><i>register-range</i> <code>-mea32 -mea64 -maddress-space-conversion -mno-address-space-conversion -mcache-size=</code><i>cache-size</i> <code>-matomic-updates -mno-atomic-updates</code> </p>
<p> <i>System V Options</i> <code>-Qy -Qn -YP,</code><i>paths</i> <code>-Ym,</code><i>dir</i> </p>
<p> <i>TILE-Gx Options</i> <code>-mcpu=CPU -m32 -m64 -mbig-endian -mlittle-endian -mcmodel=</code><i>code-model</i> </p>
<p> <i>TILEPro Options</i> <code>-mcpu=</code><i>cpu</i> <code>-m32</code> </p>
<p> <i>V850 Options</i> <code>-mlong-calls -mno-long-calls -mep -mno-ep -mprolog-function -mno-prolog-function -mspace -mtda=</code><i>n</i> <code>-msda=</code><i>n</i> <code>-mzda=</code><i>n</i> <code>-mapp-regs -mno-app-regs -mdisable-callt -mno-disable-callt -mv850e2v3 -mv850e2 -mv850e1 -mv850es -mv850e -mv850 -mv850e3v5 -mloop -mrelax -mlong-jumps -msoft-float -mhard-float -mgcc-abi -mrh850-abi -mbig-switch</code> </p>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i> <code>-mg -mgnu -munix</code> </p>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i> Options</i> <code>-mvms-return-codes -mdebug-main=</code><i>prefix</i> <code>-mmalloc64 -mpointer-size=</code><i>size</i> </p>
<p> <i>VxWorks Options</i> <code>-mrtp -non-static -Bstatic -Bdynamic -Xbind-lazy -Xbind-now</code> </p>
<p> <i>x86-64 Options</i> See i386 and x86-64 Options. </p>
<p> <i>Xstormy16 Options</i> <code>-msim</code> </p>
<p> <i>Xtensa Options</i> <code>-mconst16 -mno-const16 -mfused-madd -mno-fused-madd -mforce-no-pic -mserialize-volatile -mno-serialize-volatile -mtext-section-literals -mno-text-section-literals -mtarget-align -mno-target-align -mlongcalls -mno-longcalls</code> </p>
<p> <i>zSeries Options</i> See S/390 and zSeries Options.</p>
<dt><i>Code Generation Options</i></p>
<dd><code>-fcall-saved-</code><i>reg</i> <code>-fcall-used-</code><i>reg</i> <code>-ffixed-</code><i>reg</i> <code>-fexceptions -fnon-call-exceptions -fdelete-dead-exceptions -funwind-tables -fasynchronous-unwind-tables -fno-gnu-unique -finhibit-size-directive -finstrument-functions -finstrument-functions-exclude-function-list=</code><i>sym</i><code>,</code><i>sym</i><code>,&#8230; -finstrument-functions-exclude-file-list=</code><i>file</i><code>,</code><i>file</i><code>,&#8230; -fno-common -fno-ident -fpcc-struct-return -fpic -fPIC -fpie -fPIE -fno-jump-tables -frecord-gcc-switches -freg-struct-return -fshort-enums -fshort-double -fshort-wchar -fverbose-asm -fpack-struct[=</code><i>n</i><code>] -fstack-check -fstack-limit-register=</code><i>reg</i> <code>-fstack-limit-symbol=</code><i>sym</i> <code>-fno-stack-limit -fsplit-stack -fleading-underscore -ftls-model=</code><i>model</i> <code>-fstack-reuse=</code><i>reuse_level</i> <code>-ftrapv -fwrapv -fbounds-check -fvisibility -fstrict-volatile-bitfields -fsync-libcalls</code></dl>
<h3>Options Controlling the Kind of Output</h3>
<p>Compilation can involve up to four stages: preprocessing, compilation proper, assembly and linking, always in that order. <font SIZE="-1">GCC</font> is capable of preprocessing and compiling several files either into several assembler input files, or into one assembler input file; then each assembler input file produces an object file, and linking combines all the object files (those newly compiled, and those specified as input) into an executable file. </p>
<p> For any given input file, the file name suffix determines what kind of compilation is done:</p>
<dl COMPACT>
<dt><i>file</i><code>.c</code></p>
<dd>C source code that must be preprocessed.</p>
<dt><i>file</i><code>.i</code></p>
<dd>C source code that should not be preprocessed.</p>
<dt><i>file</i><code>.ii</code></p>
<dd>C<font SIZE="-2">++</font> source code that should not be preprocessed.</p>
<dt><i>file</i><code>.m</code></p>
<dd>Objective-C source code. Note that you must link with the <i>libobjc</i> library to make an Objective-C program work.</p>
<dt><i>file</i><code>.mi</code></p>
<dd>Objective-C source code that should not be preprocessed.</p>
<dt><i>file</i><code>.mm</code></p>
<dd>
<dt><i>file</i><code>.M</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code. Note that you must link with the <i>libobjc</i> library to make an Objective-C<font SIZE="-2">++</font> program work. Note that <code>.M</code> refers to a literal capital M.</p>
<dt><i>file</i><code>.mii</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code that should not be preprocessed.</p>
<dt><i>file</i><code>.h</code></p>
<dd>C, C<font SIZE="-2">++</font>, Objective-C or Objective-C<font SIZE="-2">++</font> header file to be turned into a precompiled header (default), or C, C<font SIZE="-2">++</font> header file to be turned into an Ada spec (via the <code>-fdump-ada-spec</code> switch).</p>
<dt><i>file</i><code>.cc</code></p>
<dd>
<dt><i>file</i><code>.cp</code></p>
<dd>
<dt><i>file</i><code>.cxx</code></p>
<dd>
<dt><i>file</i><code>.cpp</code></p>
<dd>
<dt><i>file</i><code>.CPP</code></p>
<dd>
<dt><i>file</i><code>.c++</code></p>
<dd>
<dt><i>file</i><code>.C</code></p>
<dd>C<font SIZE="-2">++</font> source code that must be preprocessed. Note that in <code>.cxx</code>, the last two letters must both be literally <code>x</code>. Likewise, <code>.C</code> refers to a literal capital C.</p>
<dt><i>file</i><code>.mm</code></p>
<dd>
<dt><i>file</i><code>.M</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code that must be preprocessed.</p>
<dt><i>file</i><code>.mii</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code that should not be preprocessed.</p>
<dt><i>file</i><code>.hh</code></p>
<dd>
<dt><i>file</i><code>.H</code></p>
<dd>
<dt><i>file</i><code>.hp</code></p>
<dd>
<dt><i>file</i><code>.hxx</code></p>
<dd>
<dt><i>file</i><code>.hpp</code></p>
<dd>
<dt><i>file</i><code>.HPP</code></p>
<dd>
<dt><i>file</i><code>.h++</code></p>
<dd>
<dt><i>file</i><code>.tcc</code></p>
<dd>C<font SIZE="-2">++</font> header file to be turned into a precompiled header or Ada spec.</p>
<dt><i>file</i><code>.f</code></p>
<dd>
<dt><i>file</i><code>.for</code></p>
<dd>
<dt><i>file</i><code>.ftn</code></p>
<dd>Fixed form Fortran source code that should not be preprocessed.</p>
<dt><i>file</i><code>.F</code></p>
<dd>
<dt><i>file</i><code>.FOR</code></p>
<dd>
<dt><i>file</i><code>.fpp</code></p>
<dd>
<dt><i>file</i><code>.FPP</code></p>
<dd>
<dt><i>file</i><code>.FTN</code></p>
<dd>Fixed form Fortran source code that must be preprocessed (with the traditional preprocessor).</p>
<dt><i>file</i><code>.f90</code></p>
<dd>
<dt><i>file</i><code>.f95</code></p>
<dd>
<dt><i>file</i><code>.f03</code></p>
<dd>
<dt><i>file</i><code>.f08</code></p>
<dd>Free form Fortran source code that should not be preprocessed.</p>
<dt><i>file</i><code>.F90</code></p>
<dd>
<dt><i>file</i><code>.F95</code></p>
<dd>
<dt><i>file</i><code>.F03</code></p>
<dd>
<dt><i>file</i><code>.F08</code></p>
<dd>Free form Fortran source code that must be preprocessed (with the traditional preprocessor).</p>
<dt><i>file</i><code>.go</code></p>
<dd>Go source code.</p>
<dt><i>file</i><code>.ads</code></p>
<dd>Ada source code file that contains a library unit declaration (a declaration of a package, subprogram, or generic, or a generic instantiation), or a library unit renaming declaration (a package, generic, or subprogram renaming declaration). Such files are also called <i>specs</i>.</p>
<dt><i>file</i><code>.adb</code></p>
<dd>Ada source code file containing a library unit body (a subprogram or package body). Such files are also called <i>bodies</i>.</p>
<dt><i>file</i><code>.s</code></p>
<dd>Assembler code.</p>
<dt><i>file</i><code>.S</code></p>
<dd>
<dt><i>file</i><code>.sx</code></p>
<dd>Assembler code that must be preprocessed.</p>
<dt><i>other</i></p>
<dd>An object file to be fed straight into linking. Any file name with no recognized suffix is treated this way.</dl>
<p> You can specify the input language explicitly with the <code>-x</code> option:</p>
<dl COMPACT>
<dt><code>-x</code> <i>language</i></p>
<dd>Specify explicitly the <i>language</i> for the following input files (rather than letting the compiler choose a default based on the file name suffix). This option applies to all following input files until the next <code>-x</code> option. Possible values for <i>language</i> are: </p>
<pre> c c-header cpp-output
 c++ c++-header c++-cpp-output
 objective-c objective-c-header objective-c-cpp-output
 objective-c++ objective-c++-header objective-c++-cpp-output
 assembler assembler-with-cpp
 ada
 f77 f77-cpp-input f95 f95-cpp-input
 go
 java</pre>
<dt><code>-x none</code></p>
<dd>Turn off any specification of a language, so that subsequent files are handled according to their file name suffixes (as they are if <code>-x</code> has not been used at all).</p>
<dt><code>-pass-exit-codes</code></p>
<dd>Normally the <code>gcc</code> program exits with the code of 1 if any phase of the compiler returns a non-success return code. If you specify <code>-pass-exit-codes</code>, the <code>gcc</code> program instead returns with the numerically highest error produced by any phase returning an error indication. The C, C<font SIZE="-2">++</font>, and Fortran front ends return 4 if an internal compiler error is encountered.</dl>
<p> If you only want some of the stages of compilation, you can use <code>-x</code> (or filename suffixes) to tell <code>gcc</code> where to start, and one of the options <code>-c</code>, <code>-S</code>, or <code>-E</code> to say where <code>gcc</code> is to stop. Note that some combinations (for example, <code>-x cpp-output -E</code>) instruct <code>gcc</code> to do nothing at all.</p>
<dl COMPACT>
<dt><code>-c</code></p>
<dd>Compile or assemble the source files, but do not link. The linking stage simply is not done. The ultimate output is in the form of an object file for each source file. </p>
<p> By default, the object file name for a source file is made by replacing the suffix <code>.c</code>, <code>.i</code>, <code>.s</code>, etc., with <code>.o</code>. </p>
<p> Unrecognized input files, not requiring compilation or assembly, are ignored.</p>
<dt><code>-S</code></p>
<dd>Stop after the stage of compilation proper; do not assemble. The output is in the form of an assembler code file for each non-assembler input file specified. </p>
<p> By default, the assembler file name for a source file is made by replacing the suffix <code>.c</code>, <code>.i</code>, etc., with <code>.s</code>. </p>
<p> Input files that don&#8217;t require compilation are ignored.</p>
<dt><code>-E</code></p>
<dd>Stop after the preprocessing stage; do not run the compiler proper. The output is in the form of preprocessed source code, which is sent to the standard output. </p>
<p> Input files that don&#8217;t require preprocessing are ignored.</p>
<dt><code>-o</code> <i>file</i></p>
<dd>Place output in file <i>file</i>. This applies to whatever sort of output is being produced, whether it be an executable file, an object file, an assembler file or preprocessed C code. </p>
<p> If <code>-o</code> is not specified, the default is to put an executable file in <i>a.out</i>, the object file for <i>source.suffix</i> in <i>source.o</i>, its assembler file in <i>source.s</i>, a precompiled header file in <i>source.suffix.gch</i>, and all preprocessed C source on standard output.</p>
<dt><code>-v</code></p>
<dd>Print (on standard error output) the commands executed to run the stages of compilation. Also print the version number of the compiler driver program and of the preprocessor and the compiler proper.</p>
<dt><code>-###</code></p>
<dd>Like <code>-v</code> except the commands are not executed and arguments are quoted unless they contain only alphanumeric characters or <tt>&quot;./-_&quot;</tt>. This is useful for shell scripts to capture the driver-generated command lines.</p>
<dt><code>-pipe</code></p>
<dd>Use pipes rather than temporary files for communication between the various stages of compilation. This fails to work on some systems where the assembler is unable to read from a pipe; but the <font SIZE="-1">GNU</font> assembler has no trouble.</p>
<dt><code>&#8211;help</code></p>
<dd>Print (on the standard output) a description of the command-line options understood by <code>gcc</code>. If the <code>-v</code> option is also specified then <code>&#8211;help</code> is also passed on to the various processes invoked by <code>gcc</code>, so that they can display the command-line options they accept. If the <code>-Wextra</code> option has also been specified (prior to the <code>&#8211;help</code> option), then command-line options that have no documentation associated with them are also displayed.</p>
<dt><code>&#8211;target-help</code></p>
<dd>Print (on the standard output) a description of target-specific command-line options for each tool. For some targets extra target-specific information may also be printed.</p>
<dt><code>&#8211;help={</code><i>class</i>|[<code>^</code>]<i>qualifier</i><code>}</code>[<code>,&#8230;</code>]</p>
<dd>Print (on the standard output) a description of the command-line options understood by the compiler that fit into all specified classes and qualifiers. These are the supported classes:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>optimizers</code></p>
<dd>Display all of the optimization options supported by the compiler.</p>
<dt><code>warnings</code></p>
<dd>Display all of the options controlling warning messages produced by the compiler.</p>
<dt><code>target</code></p>
<dd>Display target-specific options. Unlike the <code>&#8211;target-help</code> option however, target-specific options of the linker and assembler are not displayed. This is because those tools do not currently support the extended <code>&#8211;help=</code> syntax.</p>
<dt><code>params</code></p>
<dd>Display the values recognized by the <code>&#8211;param</code> option.</p>
<dt><i>language</i></p>
<dd>Display the options supported for <i>language</i>, where <i>language</i> is the name of one of the languages supported in this version of <font SIZE="-1">GCC.</font></p>
<dt><code>common</code></p>
<dd>Display the options that are common to all languages.</dl>
</dl>
<dl COMPACT>
<dd>These are the supported qualifiers:</p>
<dl COMPACT>
<dt><code>undocumented</code></p>
<dd>Display only those options that are undocumented.</p>
<dt><code>joined</code></p>
<dd>Display options taking an argument that appears after an equal sign in the same continuous piece of text, such as: <code>&#8211;help=target</code>.</p>
<dt><code>separate</code></p>
<dd>Display options taking an argument that appears as a separate word following the original option, such as: <code>-o output-file</code>.</dl>
</dl>
<dl COMPACT>
<dd>Thus for example to display all the undocumented target-specific switches supported by the compiler, use: </p>
<pre> --help=target,undocumented</pre>
<p>The sense of a qualifier can be inverted by prefixing it with the <code>^</code> character, so for example to display all binary warning options (i.e., ones that are either on or off and that do not take an argument) that have a description, use: </p>
<pre> --help=warnings,^joined,^undocumented</pre>
<p>The argument to <code>&#8211;help=</code> should not consist solely of inverted qualifiers. </p>
<p> Combining several classes is possible, although this usually restricts the output so much that there is nothing to display. One case where it does work, however, is when one of the classes is <i>target</i>. For example, to display all the target-specific optimization options, use: </p>
<pre> --help=target,optimizers</pre>
<p>The <code>&#8211;help=</code> option can be repeated on the command line. Each successive use displays its requested class of options, skipping those that have already been displayed. </p>
<p> If the <code>-Q</code> option appears on the command line before the <code>&#8211;help=</code> option, then the descriptive text displayed by <code>&#8211;help=</code> is changed. Instead of describing the displayed options, an indication is given as to whether the option is enabled, disabled or set to a specific value (assuming that the compiler knows this at the point where the <code>&#8211;help=</code> option is used). </p>
<p> Here is a truncated example from the <font SIZE="-1">ARM</font> port of <code>gcc</code>: </p>
<pre> % gcc -Q -mabi=2 --help=target -c
 The following options are target specific:
 -mabi= 2
 -mabort-on-noreturn [disabled]
 -mapcs [disabled]</pre>
<p>The output is sensitive to the effects of previous command-line options, so for example it is possible to find out which optimizations are enabled at <code>-O2</code> by using: </p>
<pre> -Q -O2 --help=optimizers</pre>
<p>Alternatively you can discover which binary optimizations are enabled by <code>-O3</code> by using: </p>
<pre> gcc -c -Q -O3 --help=optimizers &gt; /tmp/O3-opts
 gcc -c -Q -O2 --help=optimizers &gt; /tmp/O2-opts
 diff /tmp/O2-opts /tmp/O3-opts | grep enabled</pre>
</dl>
<dt><code>-no-canonical-prefixes</code></p>
<dd>Do not expand any symbolic links, resolve references to <code>/../</code> or <code>/./</code>, or make the path absolute when generating a relative prefix.</p>
<dt><code>&#8211;version</code></p>
<dd>Display the version number and copyrights of the invoked <font SIZE="-1">GCC.</font></p>
<dt><code>-wrapper</code></p>
<dd>Invoke all subcommands under a wrapper program. The name of the wrapper program and its parameters are passed as a comma separated list. </p>
<pre> gcc -c t.c -wrapper gdb,--args</pre>
<p>This invokes all subprograms of <code>gcc</code> under <code>gdb &#8211;args</code>, thus the invocation of <code>cc1</code> is <code>gdb &#8211;args cc1 &#8230;</code>.</p>
<dt><code>-fplugin=</code><i>name</i><code>.so</code></p>
<dd>Load the plugin code in file <i>name</i>.so, assumed to be a shared object to be dlopen&#8217;d by the compiler. The base name of the shared object file is used to identify the plugin for the purposes of argument parsing (See <code>-fplugin-arg-</code><i>name</i><code>&#8211;</code><i>key</i><code>=</code><i>value</i> below). Each plugin should define the callback functions specified in the Plugins <font SIZE="-1">API.</font></p>
<dt><code>-fplugin-arg-</code><i>name</i><code>&#8211;</code><i>key</i><code>=</code><i>value</i></p>
<dd>Define an argument called <i>key</i> with a value of <i>value</i> for the plugin called <i>name</i>.</p>
<dt><code>-fdump-ada-spec</code>[<code>-slim</code>]</p>
<dd>For C and C<font SIZE="-2">++</font> source and include files, generate corresponding Ada specs.</p>
<dt><code>-fada-spec-parent=</code><i>unit</i></p>
<dd>In conjunction with <code>-fdump-ada-spec</code>[<code>-slim</code>] above, generate Ada specs as child units of parent <i>unit</i>.</p>
<dt><code>-fdump-go-spec=</code><i>file</i></p>
<dd>For input files in any language, generate corresponding Go declarations in <i>file</i>. This generates Go <tt>&quot;const&quot;</tt>, <tt>&quot;type&quot;</tt>, <tt>&quot;var&quot;</tt>, and <tt>&quot;func&quot;</tt> declarations which may be a useful way to start writing a Go interface to code written in some other language.</p>
<dt><code>@</code><i>file</i></p>
<dd>Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h3>Compiling C<font SIZE="-2">++</font> Programs</h3>
<p>C<font SIZE="-2">++</font> source files conventionally use one of the suffixes <code>.C</code>, <code>.cc</code>, <code>.cpp</code>, <code>.CPP</code>, <code>.c++</code>, <code>.cp</code>, or <code>.cxx</code>; C<font SIZE="-2">++</font> header files often use <code>.hh</code>, <code>.hpp</code>, <code>.H</code>, or (for shared template code) <code>.tcc</code>; and preprocessed C<font SIZE="-2">++</font> files use the suffix <code>.ii</code>. <font SIZE="-1">GCC</font> recognizes files with these names and compiles them as C<font SIZE="-2">++</font> programs even if you call the compiler the same way as for compiling C programs (usually with the name <code>gcc</code>). </p>
<p> However, the use of <code>gcc</code> does not add the C<font SIZE="-2">++</font> library. <code>g++</code> is a program that calls <font SIZE="-1">GCC</font> and automatically specifies linking against the C<font SIZE="-2">++</font> library. It treats <code>.c</code>, <code>.h</code> and <code>.i</code> files as C<font SIZE="-2">++</font> source files instead of C source files unless <code>-x</code> is used. This program is also useful when precompiling a C header file with a <code>.h</code> extension for use in C<font SIZE="-2">++</font> compilations. On many systems, <code>g++</code> is also installed with the name <code>c++</code>. </p>
<p> When you compile C<font SIZE="-2">++</font> programs, you may specify many of the same command-line options that you use for compiling programs in any language; or command-line options meaningful for C and related languages; or options that are meaningful only for C<font SIZE="-2">++</font> programs.</p>
<h3>Options Controlling C Dialect</h3>
<p>The following options control the dialect of C (or languages derived from C, such as C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font>) that the compiler accepts:</p>
<dl COMPACT>
<dt><code>-ansi</code></p>
<dd>In C mode, this is equivalent to <code>-std=c90</code>. In C<font SIZE="-2">++</font> mode, it is equivalent to <code>-std=c++98</code>. </p>
<p> This turns off certain features of <font SIZE="-1">GCC</font> that are incompatible with <font SIZE="-1">ISO C90 </font>(when compiling C code), or of standard C<font SIZE="-2">++</font> (when compiling C<font SIZE="-2">++</font> code), such as the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, and predefined macros such as <tt>&quot;unix&quot;</tt> and <tt>&quot;vax&quot;</tt> that identify the type of system you are using. It also enables the undesirable and rarely used <font SIZE="-1">ISO</font> trigraph feature. For the C compiler, it disables recognition of C<font SIZE="-2">++</font> style <code>//</code> comments as well as the <tt>&quot;inline&quot;</tt> keyword. </p>
<p> The alternate keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__extension__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> continue to work despite <code>-ansi</code>. You would not want to use them in an <font SIZE="-1">ISO C</font> program, of course, but it is useful to put them in header files that might be included in compilations done with <code>-ansi</code>. Alternate predefined macros such as <tt>&quot;__unix__&quot;</tt> and <tt>&quot;__vax__&quot;</tt> are also available, with or without <code>-ansi</code>. </p>
<p> The <code>-ansi</code> option does not cause non-ISO programs to be rejected gratuitously. For that, <code>-Wpedantic</code> is required in addition to <code>-ansi</code>. </p>
<p> The macro <tt>&quot;__STRICT_ANSI__&quot;</tt> is predefined when the <code>-ansi</code> option is used. Some header files may notice this macro and refrain from declaring certain functions or defining certain macros that the <font SIZE="-1">ISO</font> standard doesn&#8217;t call for; this is to avoid interfering with any programs that might use these names for other things. </p>
<p> Functions that are normally built in but do not have semantics defined by <font SIZE="-1">ISO C </font>(such as <tt>&quot;alloca&quot;</tt> and <tt>&quot;ffs&quot;</tt>) are not built-in functions when <code>-ansi</code> is used.</p>
<dt><code>-std=</code></p>
<dd>Determine the language standard. This option is currently only supported when compiling C or C<font SIZE="-2">++</font>. </p>
<p> The compiler can accept several base standards, such as <code>c90</code> or <code>c++98</code>, and <font SIZE="-1">GNU</font> dialects of those standards, such as <code>gnu90</code> or <code>gnu++98</code>. When a base standard is specified, the compiler accepts all programs following that standard plus those using <font SIZE="-1">GNU</font> extensions that do not contradict it. For example, <code>-std=c90</code> turns off certain features of <font SIZE="-1">GCC</font> that are incompatible with <font SIZE="-1">ISO C90,</font> such as the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, but not other <font SIZE="-1">GNU</font> extensions that do not have a meaning in <font SIZE="-1">ISO C90,</font> such as omitting the middle term of a <tt>&quot;?:&quot;</tt> expression. On the other hand, when a <font SIZE="-1">GNU</font> dialect of a standard is specified, all features supported by the compiler are enabled, even when those features change the meaning of the base standard. As a result, some strict-conforming programs may be rejected. The particular standard is used by <code>-Wpedantic</code> to identify which features are <font SIZE="-1">GNU</font> extensions given that version of the standard. For example <code>-std=gnu90 -Wpedantic</code> warns about C<font SIZE="-2">++</font> style <code>//</code> comments, while <code>-std=gnu99 -Wpedantic</code> does not. </p>
<p> A value for this option must be provided; possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>c90</code></p>
<dd>
<dt><code>c89</code></p>
<dd>
<dt><code>iso9899:1990</code></p>
<dd>Support all <font SIZE="-1">ISO C90</font> programs (certain <font SIZE="-1">GNU</font> extensions that conflict with <font SIZE="-1">ISO C90</font> are disabled). Same as <code>-ansi</code> for C code.</p>
<dt><code>iso9899:199409</code></p>
<dd><font SIZE="-1">ISO C90</font> as modified in amendment 1.</p>
<dt><code>c99</code></p>
<dd>
<dt><code>c9x</code></p>
<dd>
<dt><code>iso9899:1999</code></p>
<dd>
<dt><code>iso9899:199x</code></p>
<dd><font SIZE="-1">ISO C99. </font> This standard is substantially completely supported, modulo bugs, extended identifiers (supported except for corner cases when <code>-fextended-identifiers</code> is used) and floating-point issues (mainly but not entirely relating to optional C99 features from Annexes F and G). See &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/c99status.html">http://gcc.gnu.org/c99status.html</a></code>&gt; for more information. The names <code>c9x</code> and <code>iso9899:199x</code> are deprecated.</p>
<dt><code>c11</code></p>
<dd>
<dt><code>c1x</code></p>
<dd>
<dt><code>iso9899:2011</code></p>
<dd><font SIZE="-1">ISO C11,</font> the 2011 revision of the <font SIZE="-1">ISO C</font> standard. This standard is substantially completely supported, modulo bugs, extended identifiers (supported except for corner cases when <code>-fextended-identifiers</code> is used), floating-point issues (mainly but not entirely relating to optional C11 features from Annexes F and G) and the optional Annexes K (Bounds-checking interfaces) and L (Analyzability). The name <code>c1x</code> is deprecated.</p>
<dt><code>gnu90</code></p>
<dd>
<dt><code>gnu89</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C90 </font>(including some C99 features). This is the default for C code.</p>
<dt><code>gnu99</code></p>
<dd>
<dt><code>gnu9x</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C99. </font> The name <code>gnu9x</code> is deprecated.</p>
<dt><code>gnu11</code></p>
<dd>
<dt><code>gnu1x</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C11. </font> This is intended to become the default in a future release of <font SIZE="-1">GCC. </font> The name <code>gnu1x</code> is deprecated.</p>
<dt><code>c++98</code></p>
<dd>
<dt><code>c++03</code></p>
<dd>The 1998 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus the 2003 technical corrigendum and some additional defect reports. Same as <code>-ansi</code> for C<font SIZE="-2">++</font> code.</p>
<dt><code>gnu++98</code></p>
<dd>
<dt><code>gnu++03</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++98</code>. This is the default for C<font SIZE="-2">++</font> code.</p>
<dt><code>c++11</code></p>
<dd>
<dt><code>c++0x</code></p>
<dd>The 2011 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus amendments. The name <code>c++0x</code> is deprecated.</p>
<dt><code>gnu++11</code></p>
<dd>
<dt><code>gnu++0x</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++11</code>. The name <code>gnu++0x</code> is deprecated.</p>
<dt><code>c++1y</code></p>
<dd>The next revision of the <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard, tentatively planned for 2014. Support is highly experimental, and will almost certainly change in incompatible ways in future releases.</p>
<dt><code>gnu++1y</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++1y</code>. Support is highly experimental, and will almost certainly change in incompatible ways in future releases.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fgnu89-inline</code></p>
<dd>The option <code>-fgnu89-inline</code> tells <font SIZE="-1">GCC</font> to use the traditional <font SIZE="-1">GNU</font> semantics for <tt>&quot;inline&quot;</tt> functions when in C99 mode.<br />
&nbsp;<wbr>&nbsp;<wbr>This option is accepted and ignored by <font SIZE="-1">GCC</font> versions 4.1.3 up to but not including 4.3. In <font SIZE="-1">GCC</font> versions 4.3 and later it changes the behavior of <font SIZE="-1">GCC</font> in C99 mode. Using this option is roughly equivalent to adding the <tt>&quot;gnu_inline&quot;</tt> function attribute to all inline functions. </p>
<p> The option <code>-fno-gnu89-inline</code> explicitly tells <font SIZE="-1">GCC</font> to use the C99 semantics for <tt>&quot;inline&quot;</tt> when in C99 or gnu99 mode (i.e., it specifies the default behavior). This option was first supported in <font SIZE="-1">GCC 4.3. </font> This option is not supported in <code>-std=c90</code> or <code>-std=gnu90</code> mode. </p>
<p> The preprocessor macros <tt>&quot;__GNUC_GNU_INLINE__&quot;</tt> and <tt>&quot;__GNUC_STDC_INLINE__&quot;</tt> may be used to check which semantics are in effect for <tt>&quot;inline&quot;</tt> functions.</p>
<dt><code>-aux-info</code> <i>filename</i></p>
<dd>Output to the given filename prototyped declarations for all functions declared and/or defined in a translation unit, including those in header files. This option is silently ignored in any language other than C. </p>
<p> Besides declarations, the file indicates, in comments, the origin of each declaration (source file and line), whether the declaration was implicit, prototyped or unprototyped (<code>I</code>, <code>N</code> for new or <code>O</code> for old, respectively, in the first character after the line number and the colon), and whether it came from a declaration or a definition (<code>C</code> or <code>F</code>, respectively, in the following character). In the case of function definitions, a K&amp;R-style list of arguments followed by their declarations is also provided, inside comments, after the declaration.</p>
<dt><code>-fallow-parameterless-variadic-functions</code></p>
<dd>Accept variadic functions without named parameters. </p>
<p> Although it is possible to define such a function, this is not very useful as it is not possible to read the arguments. This is only supported for C as this construct is allowed by C<font SIZE="-2">++</font>.</p>
<dt><code>-fno-asm</code></p>
<dd>Do not recognize <tt>&quot;asm&quot;</tt>, <tt>&quot;inline&quot;</tt> or <tt>&quot;typeof&quot;</tt> as a keyword, so that code can use these words as identifiers. You can use the keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> instead. <code>-ansi</code> implies <code>-fno-asm</code>. </p>
<p> In C<font SIZE="-2">++</font>, this switch only affects the <tt>&quot;typeof&quot;</tt> keyword, since <tt>&quot;asm&quot;</tt> and <tt>&quot;inline&quot;</tt> are standard keywords. You may want to use the <code>-fno-gnu-keywords</code> flag instead, which has the same effect. In C99 mode (<code>-std=c99</code> or <code>-std=gnu99</code>), this switch only affects the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, since <tt>&quot;inline&quot;</tt> is a standard keyword in <font SIZE="-1">ISO C99.</font></p>
<dt><code>-fno-builtin</code></p>
<dd>
<dt><code>-fno-builtin-</code><i>function</i></p>
<dd>Don&#8217;t recognize built-in functions that do not begin with <code>__builtin_</code> as prefix. </p>
<p> <font SIZE="-1">GCC</font> normally generates special code to handle certain built-in functions more efficiently; for instance, calls to <tt>&quot;alloca&quot;</tt> may become single instructions which adjust the stack directly, and calls to <tt>&quot;memcpy&quot;</tt> may become inline copy loops. The resulting code is often both smaller and faster, but since the function calls no longer appear as such, you cannot set a breakpoint on those calls, nor can you change the behavior of the functions by linking with a different library. In addition, when a function is recognized as a built-in function, <font SIZE="-1">GCC</font> may use information about that function to warn about problems with calls to that function, or to generate more efficient code, even if the resulting code still contains calls to that function. For example, warnings are given with <code>-Wformat</code> for bad calls to <tt>&quot;printf&quot;</tt> when <tt>&quot;printf&quot;</tt> is built in and <tt>&quot;strlen&quot;</tt> is known not to modify global memory. </p>
<p> With the <code>-fno-builtin-</code><i>function</i> option only the built-in function <i>function</i> is disabled. <i>function</i> must not begin with <code>__builtin_</code>. If a function is named that is not built-in in this version of <font SIZE="-1">GCC,</font> this option is ignored. There is no corresponding <code>-fbuiltin-</code><i>function</i> option; if you wish to enable built-in functions selectively when using <code>-fno-builtin</code> or <code>-ffreestanding</code>, you may define macros such as: </p>
<pre> #define <a href="//www.systutorials.com/docs/linux/man/n-abs/">abs</a>(n) __builtin_abs ((n))
 #define strcpy(d, s) __builtin_strcpy ((d), (s))</pre>
<dt><code>-fhosted</code></p>
<dd>Assert that compilation targets a hosted environment. This implies <code>-fbuiltin</code>. A hosted environment is one in which the entire standard library is available, and in which <tt>&quot;main&quot;</tt> has a return type of <tt>&quot;int&quot;</tt>. Examples are nearly everything except a kernel. This is equivalent to <code>-fno-freestanding</code>.</p>
<dt><code>-ffreestanding</code></p>
<dd>Assert that compilation targets a freestanding environment. This implies <code>-fno-builtin</code>. A freestanding environment is one in which the standard library may not exist, and program startup may not necessarily be at <tt>&quot;main&quot;</tt>. The most obvious example is an <font SIZE="-1">OS</font> kernel. This is equivalent to <code>-fno-hosted</code>.</p>
<dt><code>-fopenmp</code></p>
<dd>Enable handling of OpenMP directives <tt>&quot;#pragma omp&quot;</tt> in C/C<font SIZE="-2">++</font> and <tt>&quot;!$omp&quot;</tt> in Fortran. When <code>-fopenmp</code> is specified, the compiler generates parallel code according to the OpenMP Application Program Interface v4.0 &lt;<code><a rel="nofollow" href="http://www.openmp.org/">http://www.openmp.org/</a></code>&gt;. This option implies <code>-pthread</code>, and thus is only supported on targets that have support for <code>-pthread</code>. <code>-fopenmp</code> implies <code>-fopenmp-simd</code>.</p>
<dt><code>-fopenmp-simd</code></p>
<dd>Enable handling of OpenMP&#8217;s <font SIZE="-1">SIMD</font> directives with <tt>&quot;#pragma omp&quot;</tt> in C/C<font SIZE="-2">++</font> and <tt>&quot;!$omp&quot;</tt> in Fortran. Other OpenMP directives are ignored.</p>
<dt><code>-fcilkplus</code></p>
<dd>Enable the usage of Cilk Plus language extension features for C/C<font SIZE="-2">++</font>. When the option <code>-fcilkplus</code> is specified, enable the usage of the Cilk Plus Language extension features for C/C<font SIZE="-2">++</font>. The present implementation follows <font SIZE="-1">ABI</font> version 1.2. This is an experimental feature that is only partially complete, and whose interface may change in future versions of <font SIZE="-1">GCC</font> as the official specification changes. Currently, all features but <tt>&quot;_Cilk_for&quot;</tt> have been implemented.</p>
<dt><code>-fgnu-tm</code></p>
<dd>When the option <code>-fgnu-tm</code> is specified, the compiler generates code for the Linux variant of Intel&#8217;s current Transactional Memory <font SIZE="-1">ABI</font> specification document (Revision 1.1, May 6 2009). This is an experimental feature whose interface may change in future versions of <font SIZE="-1">GCC,</font> as the official specification changes. Please note that not all architectures are supported for this feature. </p>
<p> For more information on <font SIZE="-1">GCC</font>&#8216;s support for transactional memory, </p>
<p> Note that the transactional memory feature is not supported with non-call exceptions (<code>-fnon-call-exceptions</code>).</p>
<dt><code>-fms-extensions</code></p>
<dd>Accept some non-standard constructs used in Microsoft header files. </p>
<p> In C<font SIZE="-2">++</font> code, this allows member names in structures to be similar to previous types declarations. </p>
<pre> typedef int UOW;
 struct ABC {
 UOW UOW;
 };</pre>
<p>Some cases of unnamed fields in structures and unions are only accepted with this option. </p>
<p> Note that this option is off for all targets but i?86 and x86_64 targets using ms-abi.</p>
<dt><code>-fplan9-extensions</code></p>
<dd>Accept some non-standard constructs used in Plan 9 code. </p>
<p> This enables <code>-fms-extensions</code>, permits passing pointers to structures with anonymous fields to functions that expect pointers to elements of the type of the field, and permits referring to anonymous fields declared using a typedef. This is only supported for C, not C<font SIZE="-2">++</font>.</p>
<dt><code>-trigraphs</code></p>
<dd>Support <font SIZE="-1">ISO C</font> trigraphs. The <code>-ansi</code> option (and <code>-std</code> options for strict <font SIZE="-1">ISO C</font> conformance) implies <code>-trigraphs</code>.</p>
<dt><code>-traditional</code></p>
<dd>
<dt><code>-traditional-cpp</code></p>
<dd>Formerly, these options caused <font SIZE="-1">GCC</font> to attempt to emulate a pre-standard C compiler. They are now only supported with the <code>-E</code> switch. The preprocessor continues to support a pre-standard mode. See the <font SIZE="-1">GNU CPP</font> manual for details.</p>
<dt><code>-fcond-mismatch</code></p>
<dd>Allow conditional expressions with mismatched types in the second and third arguments. The value of such an expression is void. This option is not supported for C<font SIZE="-2">++</font>.</p>
<dt><code>-flax-vector-conversions</code></p>
<dd>Allow implicit conversions between vectors with differing numbers of elements and/or incompatible element types. This option should not be used for new code.</p>
<dt><code>-funsigned-char</code></p>
<dd>Let the type <tt>&quot;char&quot;</tt> be unsigned, like <tt>&quot;unsigned char&quot;</tt>. </p>
<p> Each kind of machine has a default for what <tt>&quot;char&quot;</tt> should be. It is either like <tt>&quot;unsigned char&quot;</tt> by default or like <tt>&quot;signed char&quot;</tt> by default. </p>
<p> Ideally, a portable program should always use <tt>&quot;signed char&quot;</tt> or <tt>&quot;unsigned char&quot;</tt> when it depends on the signedness of an object. But many programs have been written to use plain <tt>&quot;char&quot;</tt> and expect it to be signed, or expect it to be unsigned, depending on the machines they were written for. This option, and its inverse, let you make such a program work with the opposite default. </p>
<p> The type <tt>&quot;char&quot;</tt> is always a distinct type from each of <tt>&quot;signed char&quot;</tt> or <tt>&quot;unsigned char&quot;</tt>, even though its behavior is always just like one of those two.</p>
<dt><code>-fsigned-char</code></p>
<dd>Let the type <tt>&quot;char&quot;</tt> be signed, like <tt>&quot;signed char&quot;</tt>. </p>
<p> Note that this is equivalent to <code>-fno-unsigned-char</code>, which is the negative form of <code>-funsigned-char</code>. Likewise, the option <code>-fno-signed-char</code> is equivalent to <code>-funsigned-char</code>.</p>
<dt><code>-fsigned-bitfields</code></p>
<dd>
<dt><code>-funsigned-bitfields</code></p>
<dd>
<dt><code>-fno-signed-bitfields</code></p>
<dd>
<dt><code>-fno-unsigned-bitfields</code></p>
<dd>These options control whether a bit-field is signed or unsigned, when the declaration does not use either <tt>&quot;signed&quot;</tt> or <tt>&quot;unsigned&quot;</tt>. By default, such a bit-field is signed, because this is consistent: the basic integer types such as <tt>&quot;int&quot;</tt> are signed types.</dl>
<h3>Options Controlling C<font SIZE="-2">++</font> Dialect</h3>
<p>This section describes the command-line options that are only meaningful for C<font SIZE="-2">++</font> programs. You can also use most of the <font SIZE="-1">GNU</font> compiler options regardless of what language your program is in. For example, you might compile a file <tt>&quot;firstClass.C&quot;</tt> like this: </p>
<pre> g++ -g -frepo -O -c firstClass.C</pre>
<p>In this example, only <code>-frepo</code> is an option meant only for C<font SIZE="-2">++</font> programs; you can use the other options with any language supported by <font SIZE="-1">GCC.</font> </p>
<p> Here is a list of options that are <i>only</i> for compiling C<font SIZE="-2">++</font> programs:</p>
<dl COMPACT>
<dt><code>-fabi-version=</code><i>n</i></p>
<dd>Use version <i>n</i> of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI. </font> The default is version 2. </p>
<p> Version 0 refers to the version conforming most closely to the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> specification. Therefore, the <font SIZE="-1">ABI</font> obtained using version 0 will change in different versions of G++ as <font SIZE="-1">ABI</font> bugs are fixed. </p>
<p> Version 1 is the version of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> that first appeared in G++ 3.2. </p>
<p> Version 2 is the version of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> that first appeared in G++ 3.4. </p>
<p> Version 3 corrects an error in mangling a constant address as a template argument. </p>
<p> Version 4, which first appeared in G++ 4.5, implements a standard mangling for vector types. </p>
<p> Version 5, which first appeared in G++ 4.6, corrects the mangling of attribute const/volatile on function pointer types, decltype of a plain decl, and use of a function parameter in the declaration of another parameter. </p>
<p> Version 6, which first appeared in G++ 4.7, corrects the promotion behavior of C<font SIZE="-2">++</font>11 scoped enums and the mangling of template argument packs, const/static_cast, prefix ++ and &#8211;, and a class scope function used as a template argument. </p>
<p> See also <code>-Wabi</code>.</p>
<dt><code>-fno-access-control</code></p>
<dd>Turn off all access checking. This switch is mainly useful for working around bugs in the access control code.</p>
<dt><code>-fcheck-new</code></p>
<dd>Check that the pointer returned by <tt>&quot;operator new&quot;</tt> is non-null before attempting to modify the storage allocated. This check is normally unnecessary because the C<font SIZE="-2">++</font> standard specifies that <tt>&quot;operator new&quot;</tt> only returns <tt>0</tt> if it is declared throw(), in which case the compiler always checks the return value even without this option. In all other cases, when <tt>&quot;operator new&quot;</tt> has a non-empty exception specification, memory exhaustion is signalled by throwing <tt>&quot;std::bad_alloc&quot;</tt>. See also <code>new (nothrow)</code>.</p>
<dt><code>-fconstexpr-depth=</code><i>n</i></p>
<dd>Set the maximum nested evaluation depth for C<font SIZE="-2">++</font>11 constexpr functions to <i>n</i>. A limit is needed to detect endless recursion during constant expression evaluation. The minimum specified by the standard is 512.</p>
<dt><code>-fdeduce-init-list</code></p>
<dd>Enable deduction of a template type parameter as <tt>&quot;std::initializer_list&quot;</tt> from a brace-enclosed initializer list, i.e. </p>
<pre> template &lt;class T&gt; auto forward(T t) -&gt; decltype (realfn (t))
 {
 return realfn (t);
 }
 
 void f()
 {
 forward({1,2}); // call forward&lt;std::initializer_list&lt;int&gt;&gt;
 }</pre>
<p>This deduction was implemented as a possible extension to the originally proposed semantics for the C<font SIZE="-2">++</font>11 standard, but was not part of the final standard, so it is disabled by default. This option is deprecated, and may be removed in a future version of G++.</p>
<dt><code>-ffriend-injection</code></p>
<dd>Inject friend functions into the enclosing namespace, so that they are visible outside the scope of the class in which they are declared. Friend functions were documented to work this way in the old Annotated C<font SIZE="-2">++</font> Reference Manual, and versions of G++ before 4.1 always worked that way. However, in <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> a friend function that is not declared in an enclosing scope can only be found using argument dependent lookup. This option causes friends to be injected as they were in earlier releases. </p>
<p> This option is for compatibility, and may be removed in a future release of G++.</p>
<dt><code>-fno-elide-constructors</code></p>
<dd>The C<font SIZE="-2">++</font> standard allows an implementation to omit creating a temporary that is only used to initialize another object of the same type. Specifying this option disables that optimization, and forces G++ to call the copy constructor in all cases.</p>
<dt><code>-fno-enforce-eh-specs</code></p>
<dd>Don&#8217;t generate code to check for violation of exception specifications at run time. This option violates the C<font SIZE="-2">++</font> standard, but may be useful for reducing code size in production builds, much like defining <font SIZE="-1"><code>NDEBUG</code></font>. This does not give user code permission to throw exceptions in violation of the exception specifications; the compiler still optimizes based on the specifications, so throwing an unexpected exception results in undefined behavior at run time.</p>
<dt><code>-fextern-tls-init</code></p>
<dd>
<dt><code>-fno-extern-tls-init</code></p>
<dd>The C<font SIZE="-2">++</font>11 and OpenMP standards allow <code>thread_local</code> and <code>threadprivate</code> variables to have dynamic (runtime) initialization. To support this, any use of such a variable goes through a wrapper function that performs any necessary initialization. When the use and definition of the variable are in the same translation unit, this overhead can be optimized away, but when the use is in a different translation unit there is significant overhead even if the variable doesn&#8217;t actually need dynamic initialization. If the programmer can be sure that no use of the variable in a non-defining <font SIZE="-1">TU</font> needs to trigger dynamic initialization (either because the variable is statically initialized, or a use of the variable in the defining <font SIZE="-1">TU</font> will be executed before any uses in another <font SIZE="-1">TU</font>), they can avoid this overhead with the <code>-fno-extern-tls-init</code> option. </p>
<p> On targets that support symbol aliases, the default is <code>-fextern-tls-init</code>. On targets that do not support symbol aliases, the default is <code>-fno-extern-tls-init</code>.</p>
<dt><code>-ffor-scope</code></p>
<dd>
<dt><code>-fno-for-scope</code></p>
<dd>If <code>-ffor-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> is limited to the <code>for</code> loop itself, as specified by the C<font SIZE="-2">++</font> standard. If <code>-fno-for-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> extends to the end of the enclosing scope, as was the case in old versions of G++, and other (traditional) implementations of C<font SIZE="-2">++</font>. </p>
<p> If neither flag is given, the default is to follow the standard, but to allow and give a warning for old-style code that would otherwise be invalid, or have different behavior.</p>
<dt><code>-fno-gnu-keywords</code></p>
<dd>Do not recognize <tt>&quot;typeof&quot;</tt> as a keyword, so that code can use this word as an identifier. You can use the keyword <tt>&quot;__typeof__&quot;</tt> instead. <code>-ansi</code> implies <code>-fno-gnu-keywords</code>.</p>
<dt><code>-fno-implicit-templates</code></p>
<dd>Never emit code for non-inline templates that are instantiated implicitly (i.e. by use); only emit code for explicit instantiations.</p>
<dt><code>-fno-implicit-inline-templates</code></p>
<dd>Don&#8217;t emit code for implicit instantiations of inline templates, either. The default is to handle inlines differently so that compiles with and without optimization need the same set of explicit instantiations.</p>
<dt><code>-fno-implement-inlines</code></p>
<dd>To save space, do not emit out-of-line copies of inline functions controlled by <code>#pragma implementation</code>. This causes linker errors if these functions are not inlined everywhere they are called.</p>
<dt><code>-fms-extensions</code></p>
<dd>Disable Wpedantic warnings about constructs used in <font SIZE="-1">MFC,</font> such as implicit int and getting a pointer to member function via non-standard syntax.</p>
<dt><code>-fno-nonansi-builtins</code></p>
<dd>Disable built-in declarations of functions that are not mandated by <font SIZE="-1">ANSI/ISO C. </font> These include <tt>&quot;ffs&quot;</tt>, <tt>&quot;alloca&quot;</tt>, <tt>&quot;_exit&quot;</tt>, <tt>&quot;index&quot;</tt>, <tt>&quot;bzero&quot;</tt>, <tt>&quot;conjf&quot;</tt>, and other related functions.</p>
<dt><code>-fnothrow-opt</code></p>
<dd>Treat a <tt>&quot;throw()&quot;</tt> exception specification as if it were a <tt>&quot;noexcept&quot;</tt> specification to reduce or eliminate the text size overhead relative to a function with no exception specification. If the function has local variables of types with non-trivial destructors, the exception specification actually makes the function smaller because the <font SIZE="-1">EH</font> cleanups for those variables can be optimized away. The semantic effect is that an exception thrown out of a function with such an exception specification results in a call to <tt>&quot;terminate&quot;</tt> rather than <tt>&quot;unexpected&quot;</tt>.</p>
<dt><code>-fno-operator-names</code></p>
<dd>Do not treat the operator name keywords <tt>&quot;and&quot;</tt>, <tt>&quot;bitand&quot;</tt>, <tt>&quot;bitor&quot;</tt>, <tt>&quot;compl&quot;</tt>, <tt>&quot;not&quot;</tt>, <tt>&quot;or&quot;</tt> and <tt>&quot;xor&quot;</tt> as synonyms as keywords.</p>
<dt><code>-fno-optional-diags</code></p>
<dd>Disable diagnostics that the standard says a compiler does not need to issue. Currently, the only such diagnostic issued by G++ is the one for a name having multiple meanings within a class.</p>
<dt><code>-fpermissive</code></p>
<dd>Downgrade some diagnostics about nonconformant code from errors to warnings. Thus, using <code>-fpermissive</code> allows some nonconforming code to compile.</p>
<dt><code>-fno-pretty-templates</code></p>
<dd>When an error message refers to a specialization of a function template, the compiler normally prints the signature of the template followed by the template arguments and any typedefs or typenames in the signature (e.g. <tt>&quot;void f(T) [with T = int]&quot;</tt> rather than <tt>&quot;void f(int)&quot;</tt>) so that it&#8217;s clear which template is involved. When an error message refers to a specialization of a class template, the compiler omits any template arguments that match the default template arguments for that template. If either of these behaviors make it harder to understand the error message rather than easier, you can use <code>-fno-pretty-templates</code> to disable them.</p>
<dt><code>-frepo</code></p>
<dd>Enable automatic template instantiation at link time. This option also implies <code>-fno-implicit-templates</code>.</p>
<dt><code>-fno-rtti</code></p>
<dd>Disable generation of information about every class with virtual functions for use by the C<font SIZE="-2">++</font> run-time type identification features (<code>dynamic_cast</code> and <code>typeid</code>). If you don&#8217;t use those parts of the language, you can save some space by using this flag. Note that exception handling uses the same information, but G++ generates it as needed. The <code>dynamic_cast</code> operator can still be used for casts that do not require run-time type information, i.e. casts to <tt>&quot;void *&quot;</tt> or to unambiguous base classes.</p>
<dt><code>-fstats</code></p>
<dd>Emit statistics about front-end processing at the end of the compilation. This information is generally only useful to the G++ development team.</p>
<dt><code>-fstrict-enums</code></p>
<dd>Allow the compiler to optimize using the assumption that a value of enumerated type can only be one of the values of the enumeration (as defined in the C<font SIZE="-2">++</font> standard; basically, a value that can be represented in the minimum number of bits needed to represent all the enumerators). This assumption may not be valid if the program uses a cast to convert an arbitrary integer value to the enumerated type.</p>
<dt><code>-ftemplate-backtrace-limit=</code><i>n</i></p>
<dd>Set the maximum number of template instantiation notes for a single warning or error to <i>n</i>. The default value is 10.</p>
<dt><code>-ftemplate-depth=</code><i>n</i></p>
<dd>Set the maximum instantiation depth for template classes to <i>n</i>. A limit on the template instantiation depth is needed to detect endless recursions during template class instantiation. <font SIZE="-1">ANSI/ISO C<font SIZE="-2">++</font></font> conforming programs must not rely on a maximum depth greater than 17 (changed to 1024 in C<font SIZE="-2">++</font>11). The default value is 900, as the compiler can run out of stack space before hitting 1024 in some situations.</p>
<dt><code>-fno-threadsafe-statics</code></p>
<dd>Do not emit the extra code to use the routines specified in the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> for thread-safe initialization of local statics. You can use this option to reduce code size slightly in code that doesn&#8217;t need to be thread-safe.</p>
<dt><code>-fuse-cxa-atexit</code></p>
<dd>Register destructors for objects with static storage duration with the <tt>&quot;__cxa_atexit&quot;</tt> function rather than the <tt>&quot;atexit&quot;</tt> function. This option is required for fully standards-compliant handling of static destructors, but only works if your C library supports <tt>&quot;__cxa_atexit&quot;</tt>.</p>
<dt><code>-fno-use-cxa-get-exception-ptr</code></p>
<dd>Don&#8217;t use the <tt>&quot;__cxa_get_exception_ptr&quot;</tt> runtime routine. This causes <tt>&quot;std::uncaught_exception&quot;</tt> to be incorrect, but is necessary if the runtime routine is not available.</p>
<dt><code>-fvisibility-inlines-hidden</code></p>
<dd>This switch declares that the user does not attempt to compare pointers to inline functions or methods where the addresses of the two functions are taken in different shared objects. </p>
<p> The effect of this is that <font SIZE="-1">GCC</font> may, effectively, mark inline methods with <tt>&quot;__attribute__ ((visibility (&quot;hidden&quot;)))&quot;</tt> so that they do not appear in the export table of a <font SIZE="-1">DSO</font> and do not require a <font SIZE="-1">PLT</font> indirection when used within the <font SIZE="-1">DSO. </font> Enabling this option can have a dramatic effect on load and link times of a <font SIZE="-1">DSO</font> as it massively reduces the size of the dynamic export table when the library makes heavy use of templates. </p>
<p> The behavior of this switch is not quite the same as marking the methods as hidden directly, because it does not affect static variables local to the function or cause the compiler to deduce that the function is defined in only one shared object. </p>
<p> You may mark a method as having a visibility explicitly to negate the effect of the switch for that method. For example, if you do want to compare pointers to a particular inline method, you might mark it as having default visibility. Marking the enclosing class with explicit visibility has no effect. </p>
<p> Explicitly instantiated inline methods are unaffected by this option as their linkage might otherwise cross a shared library boundary.</p>
<dt><code>-fvisibility-ms-compat</code></p>
<dd>This flag attempts to use visibility settings to make <font SIZE="-1">GCC</font>&#8216;s C<font SIZE="-2">++</font> linkage model compatible with that of Microsoft Visual Studio. </p>
<p> The flag makes these changes to <font SIZE="-1">GCC</font>&#8216;s linkage model:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1.</p>
<dd>It sets the default visibility to <tt>&quot;hidden&quot;</tt>, like <code>-fvisibility=hidden</code>.</p>
<dt>2.</p>
<dd>Types, but not their members, are not hidden by default.</p>
<dt>3.</p>
<dd>The One Definition Rule is relaxed for types without explicit visibility specifications that are defined in more than one shared object: those declarations are permitted if they are permitted when this option is not used.</dl>
</dl>
<dl COMPACT>
<dd>In new code it is better to use <code>-fvisibility=hidden</code> and export those classes that are intended to be externally visible. Unfortunately it is possible for code to rely, perhaps accidentally, on the Visual Studio behavior. </p>
<p> Among the consequences of these changes are that static data members of the same type with the same name but defined in different shared objects are different, so changing one does not change the other; and that pointers to function members defined in different shared objects may not compare equal. When this flag is given, it is a violation of the <font SIZE="-1">ODR</font> to define types with the same name differently.</dl>
<dt><code>-fvtable-verify=</code><i>std|preinit|none</i></p>
<dd>Turn on (or off, if using <code>-fvtable-verify=none</code>) the security feature that verifies at runtime, for every virtual call that is made, that the vtable pointer through which the call is made is valid for the type of the object, and has not been corrupted or overwritten. If an invalid vtable pointer is detected (at runtime), an error is reported and execution of the program is immediately halted. </p>
<p> This option causes runtime data structures to be built, at program start up, for verifying the vtable pointers. The options <tt>&quot;std&quot;</tt> and <tt>&quot;preinit&quot;</tt> control the timing of when these data structures are built. In both cases the data structures are built before execution reaches &#8216;main&#8217;. The <code>-fvtable-verify=std</code> causes these data structure to be built after the shared libraries have been loaded and initialized. <code>-fvtable-verify=preinit</code> causes them to be built before the shared libraries have been loaded and initialized. </p>
<p> If this option appears multiple times in the compiler line, with different values specified, &#8216;none&#8217; will take highest priority over both &#8216;std&#8217; and &#8216;preinit&#8217;; &#8216;preinit&#8217; will take priority over &#8216;std&#8217;.</p>
<dt><code>-fvtv-debug</code></p>
<dd>Causes debug versions of the runtime functions for the vtable verification feature to be called. This assumes the <code>-fvtable-verify=std</code> or <code>-fvtable-verify=preinit</code> has been used. This flag will also cause the compiler to keep track of which vtable pointers it found for each class, and record that information in the file &#8220;vtv_set_ptr_data.log&#8221;, in the dump file directory on the user&#8217;s machine. </p>
<p> Note: This feature <font SIZE="-1">APPENDS</font> data to the log file. If you want a fresh log file, be sure to delete any existing one.</p>
<dt><code>-fvtv-counts</code></p>
<dd>This is a debugging flag. When used in conjunction with <code>-fvtable-verify=std</code> or <code>-fvtable-verify=preinit</code>, this causes the compiler to keep track of the total number of virtual calls it encountered and the number of verifications it inserted. It also counts the number of calls to certain runtime library functions that it inserts. This information, for each compilation unit, is written to a file named &#8220;vtv_count_data.log&#8221;, in the dump_file directory on the user&#8217;s machine. It also counts the size of the vtable pointer sets for each class, and writes this information to &#8220;vtv_class_set_sizes.log&#8221; in the same directory. </p>
<p> Note: This feature <font SIZE="-1">APPENDS</font> data to the log files. To get a fresh log files, be sure to delete any existing ones.</p>
<dt><code>-fno-weak</code></p>
<dd>Do not use weak symbol support, even if it is provided by the linker. By default, G++ uses weak symbols if they are available. This option exists only for testing, and should not be used by end-users; it results in inferior code and has no benefits. This option may be removed in a future release of G++.</p>
<dt><code>-nostdinc++</code></p>
<dd>Do not search for header files in the standard directories specific to C<font SIZE="-2">++</font>, but do still search the other standard directories. (This option is used when building the C<font SIZE="-2">++</font> library.)</dl>
<p> In addition, these optimization, warning, and code generation options have meanings only for C<font SIZE="-2">++</font> programs:</p>
<dl COMPACT>
<dt><code>-Wabi</code> (C, Objective-C, C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when G++ generates code that is probably not compatible with the vendor-neutral C<font SIZE="-2">++</font> <font SIZE="-1">ABI. </font> Although an effort has been made to warn about all such cases, there are probably some cases that are not warned about, even though G++ is generating incompatible code. There may also be cases where warnings are emitted even though the code that is generated is compatible. </p>
<p> You should rewrite your code to avoid these warnings if you are concerned about the fact that code generated by G++ may not be binary compatible with code generated by other compilers. </p>
<p> The known incompatibilities in <code>-fabi-version=2</code> (the default) include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>A template with a non-type template parameter of reference type is mangled incorrectly: </p>
<pre> extern int N;
 template &lt;int &amp;&gt; struct S {};
 void n (S&lt;N&gt;) {2}</pre>
<p>This is fixed in <code>-fabi-version=3</code>.</p>
<dt>&bull;</p>
<dd><font SIZE="-1">SIMD</font> vector types declared using <tt>&quot;__attribute ((vector_size))&quot;</tt> are mangled in a non-standard way that does not allow for overloading of functions taking vectors of different sizes. </p>
<p> The mangling is changed in <code>-fabi-version=4</code>.</dl>
</dl>
<dl COMPACT>
<dd>The known incompatibilities in <code>-fabi-version=1</code> include:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Incorrect handling of tail-padding for bit-fields. G++ may attempt to pack data into the same byte as a base class. For example: </p>
<pre> struct A { virtual void f(); int f1 : 1; };
 struct B : public A { int f2 : 1; };</pre>
<p>In this case, G++ places <tt>&quot;B::f2&quot;</tt> into the same byte as <tt>&quot;A::f1&quot;</tt>; other compilers do not. You can avoid this problem by explicitly padding <tt>&quot;A&quot;</tt> so that its size is a multiple of the byte size on your platform; that causes G++ and other compilers to lay out <tt>&quot;B&quot;</tt> identically.</p>
<dt>&bull;</p>
<dd>Incorrect handling of tail-padding for virtual bases. G++ does not use tail padding when laying out virtual bases. For example: </p>
<pre> struct A { virtual void f(); char c1; };
 struct B { B(); char c2; };
 struct C : public A, public virtual B {};</pre>
<p>In this case, G++ does not place <tt>&quot;B&quot;</tt> into the tail-padding for <tt>&quot;A&quot;</tt>; other compilers do. You can avoid this problem by explicitly padding <tt>&quot;A&quot;</tt> so that its size is a multiple of its alignment (ignoring virtual base classes); that causes G++ and other compilers to lay out <tt>&quot;C&quot;</tt> identically.</p>
<dt>&bull;</p>
<dd>Incorrect handling of bit-fields with declared widths greater than that of their underlying types, when the bit-fields appear in a union. For example: </p>
<pre> union U { int i : 4096; };</pre>
<p>Assuming that an <tt>&quot;int&quot;</tt> does not have 4096 bits, G++ makes the union too small by the number of bits in an <tt>&quot;int&quot;</tt>.</p>
<dt>&bull;</p>
<dd>Empty classes can be placed at incorrect offsets. For example: </p>
<pre> struct A {};
 
 struct B {
 A a;
 virtual void f ();
 };
 
 struct C : public B, public A {};</pre>
<p>G++ places the <tt>&quot;A&quot;</tt> base class of <tt>&quot;C&quot;</tt> at a nonzero offset; it should be placed at offset zero. G++ mistakenly believes that the <tt>&quot;A&quot;</tt> data member of <tt>&quot;B&quot;</tt> is already at offset zero.</p>
<dt>&bull;</p>
<dd>Names of template functions whose types involve <tt>&quot;typename&quot;</tt> or template template parameters can be mangled incorrectly. </p>
<pre> template &lt;typename Q&gt;
 void f(typename Q::X) {}
 
 template &lt;template &lt;typename&gt; class Q&gt;
 void f(typename Q&lt;int&gt;::X) {}</pre>
<p>Instantiations of these templates may be mangled incorrectly.</dl>
</dl>
<dl COMPACT>
<dd>It also warns about psABI-related changes. The known psABI changes at this point include:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>For SysV/x86-64, unions with <tt>&quot;long double&quot;</tt> members are passed in memory as specified in psABI. For example: </p>
<pre> union U {
 long double ld;
 int i;
 };</pre>
<p><tt>&quot;union U&quot;</tt> is always passed in memory.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wctor-dtor-privacy</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class seems unusable because all the constructors or destructors in that class are private, and it has neither friends nor public static member functions. Also warn if there are no non-private methods, and there&#8217;s at least one private member function that isn&#8217;t a constructor or destructor.</p>
<dt><code>-Wdelete-non-virtual-dtor</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when <code>delete</code> is used to destroy an instance of a class that has virtual functions and non-virtual destructor. It is unsafe to delete an instance of a derived class through a pointer to a base class if the base class does not have a virtual destructor. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wliteral-suffix</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a string or character literal is followed by a ud-suffix which does not begin with an underscore. As a conforming extension, <font SIZE="-1">GCC</font> treats such suffixes as separate preprocessing tokens in order to maintain backwards compatibility with code that uses formatting macros from <tt>&quot;&lt;inttypes.h&gt;&quot;</tt>. For example: </p>
<pre> #define __STDC_FORMAT_MACROS
 #include &lt;inttypes.h&gt;
 #include &lt;stdio.h&gt;
 
 int main() {
 int64_t i64 = 123;
 printf(&quot;My int64: %&quot;PRId64&quot;
&quot;, i64);
 }</pre>
<p>In this case, <tt>&quot;PRId64&quot;</tt> is treated as a separate preprocessing token. </p>
<p> This warning is enabled by default.</p>
<dt><code>-Wnarrowing</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a narrowing conversion prohibited by C<font SIZE="-2">++</font>11 occurs within <code>{ }</code>, e.g. </p>
<pre> int i = { 2.2 }; // error: narrowing from double to int</pre>
<p>This flag is included in <code>-Wall</code> and <code>-Wc++11-compat</code>. </p>
<p> With <code>-std=c++11</code>, <code>-Wno-narrowing</code> suppresses the diagnostic required by the standard. Note that this does not affect the meaning of well-formed code; narrowing conversions are still considered ill-formed in <font SIZE="-1">SFINAE</font> context.</p>
<dt><code>-Wnoexcept</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a noexcept-expression evaluates to false because of a call to a function that does not have a non-throwing exception specification (i.e. throw() or <code>noexcept</code>) but is known by the compiler to never throw an exception.</p>
<dt><code>-Wnon-virtual-dtor</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class has virtual functions and an accessible non-virtual destructor itself or in an accessible polymorphic base class, in which case it is possible but unsafe to delete an instance of a derived class through a pointer to the class itself or base class. This warning is automatically enabled if <code>-Weffc++</code> is specified.</p>
<dt><code>-Wreorder</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when the order of member initializers given in the code does not match the order in which they must be executed. For instance: </p>
<pre> struct A {
 int i;
 int j;
 A(): j (0), i (1) { }
 };</pre>
<p>The compiler rearranges the member initializers for <code>i</code> and <code>j</code> to match the declaration order of the members, emitting a warning to that effect. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-fext-numeric-literals</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Accept imaginary, fixed-point, or machine-defined literal number suffixes as <font SIZE="-1">GNU</font> extensions. When this option is turned off these suffixes are treated as C<font SIZE="-2">++</font>11 user-defined literal numeric suffixes. This is on by default for all pre-C<font SIZE="-2">++</font>11 dialects and all <font SIZE="-1">GNU</font> dialects: <code>-std=c++98</code>, <code>-std=gnu++98</code>, <code>-std=gnu++11</code>, <code>-std=gnu++1y</code>. This option is off by default for <font SIZE="-1">ISO C<font SIZE="-2">++</font>11</font> onwards (<code>-std=c++11</code>, &#8230;).</dl>
<p> The following <code>-W&#8230;</code> options are not affected by <code>-Wall</code>.</p>
<dl COMPACT>
<dt><code>-Weffc++</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about violations of the following style guidelines from Scott Meyers&#8217; <i>Effective C<font SIZE="-2">++</font></i> series of books:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Define a copy constructor and an assignment operator for classes with dynamically-allocated memory.</p>
<dt>&bull;</p>
<dd>Prefer initialization to assignment in constructors.</p>
<dt>&bull;</p>
<dd>Have <tt>&quot;operator=&quot;</tt> return a reference to <tt>*this</tt>.</p>
<dt>&bull;</p>
<dd>Don&#8217;t try to return a reference when you must return an object.</p>
<dt>&bull;</p>
<dd>Distinguish between prefix and postfix forms of increment and decrement operators.</p>
<dt>&bull;</p>
<dd>Never overload <tt>&quot;&amp;&amp;&quot;</tt>, <tt>&quot;||&quot;</tt>, or <tt>&quot;,&quot;</tt>.</dl>
</dl>
<dl COMPACT>
<dd>This option also enables <code>-Wnon-virtual-dtor</code>, which is also one of the effective C<font SIZE="-2">++</font> recommendations. However, the check is extended to warn about the lack of virtual destructor in accessible non-polymorphic bases classes too. </p>
<p> When selecting this option, be aware that the standard library headers do not obey all of these guidelines; use <code>grep -v</code> to filter out those warnings.</dl>
<dt><code>-Wstrict-null-sentinel</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about the use of an uncasted <tt>&quot;NULL&quot;</tt> as sentinel. When compiling only with <font SIZE="-1">GCC</font> this is a valid sentinel, as <tt>&quot;NULL&quot;</tt> is defined to <tt>&quot;__null&quot;</tt>. Although it is a null pointer constant rather than a null pointer, it is guaranteed to be of the same size as a pointer. But this use is not portable across different compilers.</p>
<dt><code>-Wno-non-template-friend</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Disable warnings when non-templatized friend functions are declared within a template. Since the advent of explicit template specification support in G++, if the name of the friend is an unqualified-id (i.e., <code>friend foo(int)</code>), the C<font SIZE="-2">++</font> language specification demands that the friend declare or define an ordinary, nontemplate function. (Section 14.5.3). Before G++ implemented explicit specification, unqualified-ids could be interpreted as a particular specialization of a templatized function. Because this non-conforming behavior is no longer the default behavior for G++, <code>-Wnon-template-friend</code> allows the compiler to check existing code for potential trouble spots and is on by default. This new compiler behavior can be turned off with <code>-Wno-non-template-friend</code>, which keeps the conformant compiler code but disables the helpful warning.</p>
<dt><code>-Wold-style-cast</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if an old-style (C-style) cast to a non-void type is used within a C<font SIZE="-2">++</font> program. The new-style casts (<code>dynamic_cast</code>, <code>static_cast</code>, <code>reinterpret_cast</code>, and <code>const_cast</code>) are less vulnerable to unintended effects and much easier to search for.</p>
<dt><code>-Woverloaded-virtual</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a function declaration hides virtual functions from a base class. For example, in: </p>
<pre> struct A {
 virtual void f();
 };
 
 struct B: public A {
 void f(int);
 };</pre>
<p>the <tt>&quot;A&quot;</tt> class version of <tt>&quot;f&quot;</tt> is hidden in <tt>&quot;B&quot;</tt>, and code like: </p>
<pre> B* b;
 b-&gt;f();</pre>
<p>fails to compile.</p>
<dt><code>-Wno-pmf-conversions</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Disable the diagnostic for converting a bound pointer to member function to a plain pointer.</p>
<dt><code>-Wsign-promo</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when overload resolution chooses a promotion from unsigned or enumerated type to a signed type, over a conversion to an unsigned type of the same size. Previous versions of G++ tried to preserve unsignedness, but the standard mandates the current behavior.</dl>
<h3>Options Controlling Objective-C and Objective-C<font SIZE="-2">++</font> Dialects</h3>
<p>(<font SIZE="-1">NOTE:</font> This manual does not describe the Objective-C and Objective-C<font SIZE="-2">++</font> languages themselves. </p>
<p> This section describes the command-line options that are only meaningful for Objective-C and Objective-C<font SIZE="-2">++</font> programs. You can also use most of the language-independent <font SIZE="-1">GNU</font> compiler options. For example, you might compile a file <tt>&quot;some_class.m&quot;</tt> like this: </p>
<pre> gcc -g -fgnu-runtime -O -c some_class.m</pre>
<p>In this example, <code>-fgnu-runtime</code> is an option meant only for Objective-C and Objective-C<font SIZE="-2">++</font> programs; you can use the other options with any language supported by <font SIZE="-1">GCC.</font> </p>
<p> Note that since Objective-C is an extension of the C language, Objective-C compilations may also use options specific to the C front-end (e.g., <code>-Wtraditional</code>). Similarly, Objective-C<font SIZE="-2">++</font> compilations may use C<font SIZE="-2">++</font>-specific options (e.g., <code>-Wabi</code>). </p>
<p> Here is a list of options that are <i>only</i> for compiling Objective-C and Objective-C<font SIZE="-2">++</font> programs:</p>
<dl COMPACT>
<dt><code>-fconstant-string-class=</code><i>class-name</i></p>
<dd>Use <i>class-name</i> as the name of the class to instantiate for each literal string specified with the syntax <tt>&quot;@&quot;...&quot;&quot;</tt>. The default class name is <tt>&quot;NXConstantString&quot;</tt> if the <font SIZE="-1">GNU</font> runtime is being used, and <tt>&quot;NSConstantString&quot;</tt> if the NeXT runtime is being used (see below). The <code>-fconstant-cfstrings</code> option, if also present, overrides the <code>-fconstant-string-class</code> setting and cause <tt>&quot;@&quot;...&quot;&quot;</tt> literals to be laid out as constant CoreFoundation strings.</p>
<dt><code>-fgnu-runtime</code></p>
<dd>Generate object code compatible with the standard <font SIZE="-1">GNU</font> Objective-C runtime. This is the default for most types of systems.</p>
<dt><code>-fnext-runtime</code></p>
<dd>Generate output compatible with the NeXT runtime. This is the default for NeXT-based systems, including Darwin and Mac <font SIZE="-1">OS X. </font> The macro <tt>&quot;__NEXT_RUNTIME__&quot;</tt> is predefined if (and only if) this option is used.</p>
<dt><code>-fno-nil-receivers</code></p>
<dd>Assume that all Objective-C message dispatches (<tt>&quot;[receiver message:arg]&quot;</tt>) in this translation unit ensure that the receiver is not <tt>&quot;nil&quot;</tt>. This allows for more efficient entry points in the runtime to be used. This option is only available in conjunction with the NeXT runtime and <font SIZE="-1">ABI</font> version 0 or 1.</p>
<dt><code>-fobjc-abi-version=</code><i>n</i></p>
<dd>Use version <i>n</i> of the Objective-C <font SIZE="-1">ABI</font> for the selected runtime. This option is currently supported only for the NeXT runtime. In that case, Version 0 is the traditional (32-bit) <font SIZE="-1">ABI</font> without support for properties and other Objective-C 2.0 additions. Version 1 is the traditional (32-bit) <font SIZE="-1">ABI</font> with support for properties and other Objective-C 2.0 additions. Version 2 is the modern (64-bit) <font SIZE="-1">ABI. </font> If nothing is specified, the default is Version 0 on 32-bit target machines, and Version 2 on 64-bit target machines.</p>
<dt><code>-fobjc-call-cxx-cdtors</code></p>
<dd>For each Objective-C class, check if any of its instance variables is a C<font SIZE="-2">++</font> object with a non-trivial default constructor. If so, synthesize a special <tt>&quot;- (id) .cxx_construct&quot;</tt> instance method which runs non-trivial default constructors on any such instance variables, in order, and then return <tt>&quot;self&quot;</tt>. Similarly, check if any instance variable is a C<font SIZE="-2">++</font> object with a non-trivial destructor, and if so, synthesize a special <tt>&quot;- (void) .cxx_destruct&quot;</tt> method which runs all such default destructors, in reverse order. </p>
<p> The <tt>&quot;- (id) .cxx_construct&quot;</tt> and <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods thusly generated only operate on instance variables declared in the current Objective-C class, and not those inherited from superclasses. It is the responsibility of the Objective-C runtime to invoke all such methods in an object&#8217;s inheritance hierarchy. The <tt>&quot;- (id) .cxx_construct&quot;</tt> methods are invoked by the runtime immediately after a new object instance is allocated; the <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods are invoked immediately before the runtime deallocates an object instance. </p>
<p> As of this writing, only the NeXT runtime on Mac <font SIZE="-1">OS X 10.4</font> and later has support for invoking the <tt>&quot;- (id) .cxx_construct&quot;</tt> and <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods.</p>
<dt><code>-fobjc-direct-dispatch</code></p>
<dd>Allow fast jumps to the message dispatcher. On Darwin this is accomplished via the comm page.</p>
<dt><code>-fobjc-exceptions</code></p>
<dd>Enable syntactic support for structured exception handling in Objective-C, similar to what is offered by C<font SIZE="-2">++</font> and Java. This option is required to use the Objective-C keywords <tt>@try</tt>, <tt>@throw</tt>, <tt>@catch</tt>, <tt>@finally</tt> and <tt>@synchronized</tt>. This option is available with both the <font SIZE="-1">GNU</font> runtime and the NeXT runtime (but not available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS X 10.2</font> and earlier).</p>
<dt><code>-fobjc-gc</code></p>
<dd>Enable garbage collection (<font SIZE="-1">GC</font>) in Objective-C and Objective-C<font SIZE="-2">++</font> programs. This option is only available with the NeXT runtime; the <font SIZE="-1">GNU</font> runtime has a different garbage collection implementation that does not require special compiler flags.</p>
<dt><code>-fobjc-nilcheck</code></p>
<dd>For the NeXT runtime with version 2 of the <font SIZE="-1">ABI,</font> check for a nil receiver in method invocations before doing the actual method call. This is the default and can be disabled using <code>-fno-objc-nilcheck</code>. Class methods and super calls are never checked for nil in this way no matter what this flag is set to. Currently this flag does nothing when the <font SIZE="-1">GNU</font> runtime, or an older version of the NeXT runtime <font SIZE="-1">ABI,</font> is used.</p>
<dt><code>-fobjc-std=objc1</code></p>
<dd>Conform to the language syntax of Objective-C 1.0, the language recognized by <font SIZE="-1">GCC 4.0. </font> This only affects the Objective-C additions to the C/C<font SIZE="-2">++</font> language; it does not affect conformance to C/C<font SIZE="-2">++</font> standards, which is controlled by the separate C/C<font SIZE="-2">++</font> dialect option flags. When this option is used with the Objective-C or Objective-C<font SIZE="-2">++</font> compiler, any Objective-C syntax that is not recognized by <font SIZE="-1">GCC 4.0</font> is rejected. This is useful if you need to make sure that your Objective-C code can be compiled with older versions of <font SIZE="-1">GCC.</font></p>
<dt><code>-freplace-objc-classes</code></p>
<dd>Emit a special marker instructing <a href="/docs/linux/man/1-ld/">ld</a><code>(1)</code> not to statically link in the resulting object file, and allow <a href="/docs/linux/man/1-dyld/">dyld</a><code>(1)</code> to load it in at run time instead. This is used in conjunction with the Fix-and-Continue debugging mode, where the object file in question may be recompiled and dynamically reloaded in the course of program execution, without the need to restart the program itself. Currently, Fix-and-Continue functionality is only available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS X 10.3</font> and later.</p>
<dt><code>-fzero-link</code></p>
<dd>When compiling for the NeXT runtime, the compiler ordinarily replaces calls to <tt>&quot;objc_getClass(&quot;...&quot;)&quot;</tt> (when the name of the class is known at compile time) with static class references that get initialized at load time, which improves run-time performance. Specifying the <code>-fzero-link</code> flag suppresses this behavior and causes calls to <tt>&quot;objc_getClass(&quot;...&quot;)&quot;</tt> to be retained. This is useful in Zero-Link debugging mode, since it allows for individual class implementations to be modified during program execution. The <font SIZE="-1">GNU</font> runtime currently always retains calls to <tt>&quot;objc_get_class(&quot;...&quot;)&quot;</tt> regardless of command-line options.</p>
<dt><code>-gen-decls</code></p>
<dd>Dump interface declarations for all classes seen in the source file to a file named <i>sourcename.decl</i>.</p>
<dt><code>-Wassign-intercept</code> (Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn whenever an Objective-C assignment is being intercepted by the garbage collector.</p>
<dt><code>-Wno-protocol</code> (Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>If a class is declared to implement a protocol, a warning is issued for every method in the protocol that is not implemented by the class. The default behavior is to issue a warning for every method not explicitly implemented in the class, even if a method implementation is inherited from the superclass. If you use the <code>-Wno-protocol</code> option, then methods inherited from the superclass are considered to be implemented, and no warning is issued for them.</p>
<dt><code>-Wselector</code> (Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if multiple methods of different types for the same selector are found during compilation. The check is performed on the list of methods in the final stage of compilation. Additionally, a check is performed for each selector appearing in a <tt>&quot;@selector(...)&quot;</tt> expression, and a corresponding method for that selector has been found during compilation. Because these checks scan the method table only at the end of compilation, these warnings are not produced if the final stage of compilation is not reached, for example because an error is found during compilation, or because the <code>-fsyntax-only</code> option is being used.</p>
<dt><code>-Wstrict-selector-match</code> (Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if multiple methods with differing argument and/or return types are found for a given selector when attempting to send a message using this selector to a receiver of type <tt>&quot;id&quot;</tt> or <tt>&quot;Class&quot;</tt>. When this flag is off (which is the default behavior), the compiler omits such warnings if any differences found are confined to types that share the same size and alignment.</p>
<dt><code>-Wundeclared-selector</code> (Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if a <tt>&quot;@selector(...)&quot;</tt> expression referring to an undeclared selector is found. A selector is considered undeclared if no method with that name has been declared before the <tt>&quot;@selector(...)&quot;</tt> expression, either explicitly in an <tt>@interface</tt> or <tt>@protocol</tt> declaration, or implicitly in an <tt>@implementation</tt> section. This option always performs its checks as soon as a <tt>&quot;@selector(...)&quot;</tt> expression is found, while <code>-Wselector</code> only performs its checks in the final stage of compilation. This also enforces the coding style convention that methods and selectors must be declared before being used.</p>
<dt><code>-print-objc-runtime-info</code></p>
<dd>Generate C header describing the largest structure that is passed by value, if any.</dl>
<h3>Options to Control Diagnostic Messages Formatting</h3>
<p>Traditionally, diagnostic messages have been formatted irrespective of the output device&#8217;s aspect (e.g. its width, &#8230;). You can use the options described below to control the formatting algorithm for diagnostic messages, e.g. how many characters per line, how often source location information should be reported. Note that some language front ends may not honor these options.</p>
<dl COMPACT>
<dt><code>-fmessage-length=</code><i>n</i></p>
<dd>Try to format error messages so that they fit on lines of about <i>n</i> characters. The default is 72 characters for <code>g++</code> and 0 for the rest of the front ends supported by <font SIZE="-1">GCC. </font> If <i>n</i> is zero, then no line-wrapping is done; each error message appears on a single line.</p>
<dt><code>-fdiagnostics-show-location=once</code></p>
<dd>Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit source location information <i>once</i>; that is, in case the message is too long to fit on a single physical line and has to be wrapped, the source location won&#8217;t be emitted (as prefix) again, over and over, in subsequent continuation lines. This is the default behavior.</p>
<dt><code>-fdiagnostics-show-location=every-line</code></p>
<dd>Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit the same source location information (as prefix) for physical lines that result from the process of breaking a message which is too long to fit on a single line.</p>
<dt><code>-fdiagnostics-color[=</code><i></i><font SIZE="-1"><i>WHEN</i></font><i></i><code>]</code></p>
<dd>
<dt><code>-fno-diagnostics-color</code></p>
<dd>Use color in diagnostics. <i></i><font SIZE="-1"><i>WHEN</i></font><i></i> is <code>never</code>, <code>always</code>, or <code>auto</code>. The default is <code>never</code> if <font SIZE="-1"><code>GCC_COLORS</code></font> environment variable isn&#8217;t present in the environment, and <code>auto</code> otherwise. <code>auto</code> means to use color only when the standard error is a terminal. The forms <code>-fdiagnostics-color</code> and <code>-fno-diagnostics-color</code> are aliases for <code>-fdiagnostics-color=always</code> and <code>-fdiagnostics-color=never</code>, respectively. </p>
<p> The colors are defined by the environment variable <font SIZE="-1"><code>GCC_COLORS</code></font>. Its value is a colon-separated list of capabilities and Select Graphic Rendition (<font SIZE="-1">SGR</font>) substrings. <font SIZE="-1">SGR</font> commands are interpreted by the terminal or terminal emulator. (See the section in the documentation of your text terminal for permitted values and their meanings as character attributes.) These substring values are integers in decimal representation and can be concatenated with semicolons. Common values to concatenate include <code>1</code> for bold, <code>4</code> for underline, <code>5</code> for blink, <code>7</code> for inverse, <code>39</code> for default foreground color, <code>30</code> to <code>37</code> for foreground colors, <code>90</code> to <code>97</code> for 16-color mode foreground colors, <code>38;5;0</code> to <code>38;5;255</code> for 88-color and 256-color modes foreground colors, <code>49</code> for default background color, <code>40</code> to <code>47</code> for background colors, <code>100</code> to <code>107</code> for 16-color mode background colors, and <code>48;5;0</code> to <code>48;5;255</code> for 88-color and 256-color modes background colors. </p>
<p> The default <font SIZE="-1"><code>GCC_COLORS</code></font> is <code>error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01</code> where <code>01;31</code> is bold red, <code>01;35</code> is bold magenta, <code>01;36</code> is bold cyan, <code>01;32</code> is bold green and <code>01</code> is bold. Setting <font SIZE="-1"><code>GCC_COLORS</code></font> to the empty string disables colors. Supported capabilities are as follows.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&quot;error=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for error: markers.</p>
<dt>&quot;warning=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for warning: markers.</p>
<dt>&quot;note=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for note: markers.</p>
<dt>&quot;caret=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for caret line.</p>
<dt>&quot;locus=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for location information, <code>file:line</code> or <code>file:line:column</code> etc.</p>
<dt>&quot;quote=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for information printed within quotes.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fno-diagnostics-show-option</code></p>
<dd>By default, each diagnostic emitted includes text indicating the command-line option that directly controls the diagnostic (if such an option is known to the diagnostic machinery). Specifying the <code>-fno-diagnostics-show-option</code> flag suppresses that behavior.</p>
<dt><code>-fno-diagnostics-show-caret</code></p>
<dd>By default, each diagnostic emitted includes the original source line and a caret &#8216;^&#8217; indicating the column. This option suppresses this information.</dl>
<h3>Options to Request or Suppress Warnings</h3>
<p>Warnings are diagnostic messages that report constructions that are not inherently erroneous but that are risky or suggest there may have been an error. </p>
<p> The following language-independent options do not enable specific warnings but control the kinds of diagnostics produced by <font SIZE="-1">GCC.</font></p>
<dl COMPACT>
<dt><code>-fsyntax-only</code></p>
<dd>Check the code for syntax errors, but don&#8217;t do anything beyond that.</p>
<dt><code>-fmax-errors=</code><i>n</i></p>
<dd>Limits the maximum number of error messages to <i>n</i>, at which point <font SIZE="-1">GCC</font> bails out rather than attempting to continue processing the source code. If <i>n</i> is 0 (the default), there is no limit on the number of error messages produced. If <code>-Wfatal-errors</code> is also specified, then <code>-Wfatal-errors</code> takes precedence over this option.</p>
<dt><code>-w</code></p>
<dd>Inhibit all warning messages.</p>
<dt><code>-Werror</code></p>
<dd>Make all warnings into errors.</p>
<dt><code>-Werror=</code></p>
<dd>Make the specified warning into an error. The specifier for a warning is appended; for example <code>-Werror=switch</code> turns the warnings controlled by <code>-Wswitch</code> into errors. This switch takes a negative form, to be used to negate <code>-Werror</code> for specific warnings; for example <code>-Wno-error=switch</code> makes <code>-Wswitch</code> warnings not be errors, even when <code>-Werror</code> is in effect. </p>
<p> The warning message for each controllable warning includes the option that controls the warning. That option can then be used with <code>-Werror=</code> and <code>-Wno-error=</code> as described above. (Printing of the option in the warning message can be disabled using the <code>-fno-diagnostics-show-option</code> flag.) </p>
<p> Note that specifying <code>-Werror=</code><i>foo</i> automatically implies <code>-W</code><i>foo</i>. However, <code>-Wno-error=</code><i>foo</i> does not imply anything.</p>
<dt><code>-Wfatal-errors</code></p>
<dd>This option causes the compiler to abort compilation on the first error occurred rather than trying to keep going and printing further error messages.</dl>
<p> You can request many specific warnings with options beginning with <code>-W</code>, for example <code>-Wimplicit</code> to request warnings on implicit declarations. Each of these specific warning options also has a negative form beginning <code>-Wno-</code> to turn off warnings; for example, <code>-Wno-implicit</code>. This manual lists only one of the two forms, whichever is not the default. For further language-specific options also refer to <code>C<font SIZE="-2">++</font> Dialect Options</code> and <code>Objective-C and Objective-C<font SIZE="-2">++</font> Dialect Options</code>. </p>
<p> When an unrecognized warning option is requested (e.g., <code>-Wunknown-warning</code>), <font SIZE="-1">GCC</font> emits a diagnostic stating that the option is not recognized. However, if the <code>-Wno-</code> form is used, the behavior is slightly different: no diagnostic is produced for <code>-Wno-unknown-warning</code> unless other diagnostics are being produced. This allows the use of new <code>-Wno-</code> options with old compilers, but if something goes wrong, the compiler warns that an unrecognized option is present.</p>
<dl COMPACT>
<dt><code>-Wpedantic</code></p>
<dd>
<dt><code>-pedantic</code></p>
<dd>Issue all the warnings demanded by strict <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font></font>; reject all programs that use forbidden extensions, and some other programs that do not follow <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font>. </font> For <font SIZE="-1">ISO C,</font> follows the version of the <font SIZE="-1">ISO C</font> standard specified by any <code>-std</code> option used. </p>
<p> Valid <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> programs should compile properly with or without this option (though a rare few require <code>-ansi</code> or a <code>-std</code> option specifying the required version of <font SIZE="-1">ISO C</font>). However, without this option, certain <font SIZE="-1">GNU</font> extensions and traditional C and C<font SIZE="-2">++</font> features are supported as well. With this option, they are rejected. </p>
<p> <code>-Wpedantic</code> does not cause warning messages for use of the alternate keywords whose names begin and end with <code>__</code>. Pedantic warnings are also disabled in the expression that follows <tt>&quot;__extension__&quot;</tt>. However, only system header files should use these escape routes; application programs should avoid them. </p>
<p> Some users try to use <code>-Wpedantic</code> to check programs for strict <font SIZE="-1">ISO C</font> conformance. They soon find that it does not do quite what they want: it finds some non-ISO practices, but not all&#8212;only those for which <font SIZE="-1">ISO C </font><i>requires</i> a diagnostic, and some others for which diagnostics have been added. </p>
<p> A feature to report any failure to conform to <font SIZE="-1">ISO C</font> might be useful in some instances, but would require considerable additional work and would be quite different from <code>-Wpedantic</code>. We don&#8217;t have plans to support such a feature in the near future. </p>
<p> Where the standard specified with <code>-std</code> represents a <font SIZE="-1">GNU</font> extended dialect of C, such as <code>gnu90</code> or <code>gnu99</code>, there is a corresponding <i>base standard</i>, the version of <font SIZE="-1">ISO C</font> on which the <font SIZE="-1">GNU</font> extended dialect is based. Warnings from <code>-Wpedantic</code> are given where they are required by the base standard. (It does not make sense for such warnings to be given only for features not in the specified <font SIZE="-1">GNU C</font> dialect, since by definition the <font SIZE="-1">GNU</font> dialects of C include all features the compiler supports with the given option, and there would be nothing to warn about.)</p>
<dt><code>-pedantic-errors</code></p>
<dd>Like <code>-Wpedantic</code>, except that errors are produced rather than warnings.</p>
<dt><code>-Wall</code></p>
<dd>This enables all the warnings about constructions that some users consider questionable, and that are easy to avoid (or modify to prevent the warning), even in conjunction with macros. This also enables some language-specific warnings described in <code>C<font SIZE="-2">++</font> Dialect Options</code> and <code>Objective-C and Objective-C<font SIZE="-2">++</font> Dialect Options</code>. </p>
<p> <code>-Wall</code> turns on the following warning flags: </p>
<p> <code>-Waddress -Warray-bounds</code> (only with<code>-O2</code>) <code>-Wc++11-compat -Wchar-subscripts -Wenum-compare</code> (in C/ObjC; this is on by default in C<font SIZE="-2">++</font>) <code>-Wimplicit-int</code> (C and Objective-C only) <code>-Wimplicit-function-declaration</code> (C and Objective-C only) <code>-Wcomment -Wformat -Wmain</code> (only for C/ObjC and unless<code>-ffreestanding</code>) <code>-Wmaybe-uninitialized -Wmissing-braces</code> (only for C/ObjC) <code>-Wnonnull -Wopenmp-simd -Wparentheses -Wpointer-sign -Wreorder -Wreturn-type -Wsequence-point -Wsign-compare</code> (only in C<font SIZE="-2">++</font>) <code>-Wstrict-aliasing -Wstrict-overflow=1 -Wswitch -Wtrigraphs -Wuninitialized -Wunknown-pragmas -Wunused-function -Wunused-label -Wunused-value -Wunused-variable -Wvolatile-register-var</code> </p>
<p> Note that some warning flags are not implied by <code>-Wall</code>. Some of them warn about constructions that users generally do not consider questionable, but which occasionally you might wish to check for; others warn about constructions that are necessary or hard to avoid in some cases, and there is no simple way to modify the code to suppress the warning. Some of them are enabled by <code>-Wextra</code> but many of them must be enabled individually.</p>
<dt><code>-Wextra</code></p>
<dd>This enables some extra warning flags that are not enabled by <code>-Wall</code>. (This option used to be called <code>-W</code>. The older name is still supported, but the newer name is more descriptive.) </p>
<p> <code>-Wclobbered -Wempty-body -Wignored-qualifiers -Wmissing-field-initializers -Wmissing-parameter-type</code> (C only) <code>-Wold-style-declaration</code> (C only) <code>-Woverride-init -Wsign-compare -Wtype-limits -Wuninitialized -Wunused-parameter</code> (only with<code>-Wunused</code>or<code>-Wall</code>) <code>-Wunused-but-set-parameter</code> (only with<code>-Wunused</code>or<code>-Wall</code>) </p>
<p> The option <code>-Wextra</code> also prints warning messages for the following cases:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>A pointer is compared against integer zero with <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, or <code>&gt;=</code>.</p>
<dt>&bull;</p>
<dd>(C<font SIZE="-2">++</font> only) An enumerator and a non-enumerator both appear in a conditional expression.</p>
<dt>&bull;</p>
<dd>(C<font SIZE="-2">++</font> only) Ambiguous virtual bases.</p>
<dt>&bull;</p>
<dd>(C<font SIZE="-2">++</font> only) Subscripting an array that has been declared <code>register</code>.</p>
<dt>&bull;</p>
<dd>(C<font SIZE="-2">++</font> only) Taking the address of a variable that has been declared <code>register</code>.</p>
<dt>&bull;</p>
<dd>(C<font SIZE="-2">++</font> only) A base class is not initialized in a derived class&#8217;s copy constructor.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wchar-subscripts</code></p>
<dd>Warn if an array subscript has type <tt>&quot;char&quot;</tt>. This is a common cause of error, as programmers often forget that this type is signed on some machines. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wcomment</code></p>
<dd>Warn whenever a comment-start sequence <code>/*</code> appears in a <code>/*</code> comment, or whenever a Backslash-Newline appears in a <code>//</code> comment. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wno-coverage-mismatch</code></p>
<dd>Warn if feedback profiles do not match when using the <code>-fprofile-use</code> option. If a source file is changed between compiling with <code>-fprofile-gen</code> and with <code>-fprofile-use</code>, the files with the profile feedback can fail to match the source file and <font SIZE="-1">GCC</font> cannot use the profile feedback information. By default, this warning is enabled and is treated as an error. <code>-Wno-coverage-mismatch</code> can be used to disable the warning or <code>-Wno-error=coverage-mismatch</code> can be used to disable the error. Disabling the error for this warning can result in poorly optimized code and is useful only in the case of very minor changes such as bug fixes to an existing code-base. Completely disabling the warning is not recommended.</p>
<dt><code>-Wno-cpp</code></p>
<dd>(C, Objective-C, C<font SIZE="-2">++</font>, Objective-C<font SIZE="-2">++</font> and Fortran only) </p>
<p> Suppress warning messages emitted by <tt>&quot;#warning&quot;</tt> directives.</p>
<dt><code>-Wdouble-promotion</code> (C, C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Give a warning when a value of type <tt>&quot;float&quot;</tt> is implicitly promoted to <tt>&quot;double&quot;</tt>. CPUs with a 32-bit &#8220;single-precision&#8221; floating-point unit implement <tt>&quot;float&quot;</tt> in hardware, but emulate <tt>&quot;double&quot;</tt> in software. On such a machine, doing computations using <tt>&quot;double&quot;</tt> values is much more expensive because of the overhead required for software emulation. </p>
<p> It is easy to accidentally do computations with <tt>&quot;double&quot;</tt> because floating-point literals are implicitly of type <tt>&quot;double&quot;</tt>. For example, in: </p>
<pre> float area(float radius)
 {
 return 3.14159 * radius * radius;
 }</pre>
<p>the compiler performs the entire computation with <tt>&quot;double&quot;</tt> because the floating-point literal is a <tt>&quot;double&quot;</tt>.</p>
<dt><code>-Wformat</code></p>
<dd>
<dt><code>-Wformat=</code><i>n</i></p>
<dd>Check calls to <tt>&quot;printf&quot;</tt> and <tt>&quot;scanf&quot;</tt>, etc., to make sure that the arguments supplied have types appropriate to the format string specified, and that the conversions specified in the format string make sense. This includes standard functions, and others specified by format attributes, in the <tt>&quot;printf&quot;</tt>, <tt>&quot;scanf&quot;</tt>, <tt>&quot;strftime&quot;</tt> and <tt>&quot;strfmon&quot;</tt> (an X/Open extension, not in the C standard) families (or other target-specific families). Which functions are checked without format attributes having been specified depends on the standard version selected, and such checks of functions without the attribute specified are disabled by <code>-ffreestanding</code> or <code>-fno-builtin</code>. </p>
<p> The formats are checked against the format features supported by <font SIZE="-1">GNU</font> libc version 2.2. These include all <font SIZE="-1">ISO C90</font> and C99 features, as well as features from the Single Unix Specification and some <font SIZE="-1">BSD</font> and <font SIZE="-1">GNU</font> extensions. Other library implementations may not support all these features; <font SIZE="-1">GCC</font> does not support warning about features that go beyond a particular library&#8217;s limitations. However, if <code>-Wpedantic</code> is used with <code>-Wformat</code>, warnings are given about format features not in the selected standard version (but not for <tt>&quot;strfmon&quot;</tt> formats, since those are not in any version of the C standard).</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-Wformat=1</code></p>
<dd>
<dt><code>-Wformat</code></p>
<dd>Option <code>-Wformat</code> is equivalent to <code>-Wformat=1</code>, and <code>-Wno-format</code> is equivalent to <code>-Wformat=0</code>. Since <code>-Wformat</code> also checks for null format arguments for several functions, <code>-Wformat</code> also implies <code>-Wnonnull</code>. Some aspects of this level of format checking can be disabled by the options: <code>-Wno-format-contains-nul</code>, <code>-Wno-format-extra-args</code>, and <code>-Wno-format-zero-length</code>. <code>-Wformat</code> is enabled by <code>-Wall</code>.</p>
<dt><code>-Wno-format-contains-nul</code></p>
<dd>If <code>-Wformat</code> is specified, do not warn about format strings that contain <font SIZE="-1">NUL</font> bytes.</p>
<dt><code>-Wno-format-extra-args</code></p>
<dd>If <code>-Wformat</code> is specified, do not warn about excess arguments to a <tt>&quot;printf&quot;</tt> or <tt>&quot;scanf&quot;</tt> format function. The C standard specifies that such arguments are ignored. </p>
<p> Where the unused arguments lie between used arguments that are specified with <code>$</code> operand number specifications, normally warnings are still given, since the implementation could not know what type to pass to <tt>&quot;va_arg&quot;</tt> to skip the unused arguments. However, in the case of <tt>&quot;scanf&quot;</tt> formats, this option suppresses the warning if the unused arguments are all pointers, since the Single Unix Specification says that such unused arguments are allowed.</p>
<dt><code>-Wno-format-zero-length</code></p>
<dd>If <code>-Wformat</code> is specified, do not warn about zero-length formats. The C standard specifies that zero-length formats are allowed.</p>
<dt><code>-Wformat=2</code></p>
<dd>Enable <code>-Wformat</code> plus additional format checks. Currently equivalent to <code>-Wformat -Wformat-nonliteral -Wformat-security -Wformat-y2k</code>.</p>
<dt><code>-Wformat-nonliteral</code></p>
<dd>If <code>-Wformat</code> is specified, also warn if the format string is not a string literal and so cannot be checked, unless the format function takes its format arguments as a <tt>&quot;va_list&quot;</tt>.</p>
<dt><code>-Wformat-security</code></p>
<dd>If <code>-Wformat</code> is specified, also warn about uses of format functions that represent possible security problems. At present, this warns about calls to <tt>&quot;printf&quot;</tt> and <tt>&quot;scanf&quot;</tt> functions where the format string is not a string literal and there are no format arguments, as in <tt>&quot;printf (foo);&quot;</tt>. This may be a security hole if the format string came from untrusted input and contains %n. (This is currently a subset of what <code>-Wformat-nonliteral</code> warns about, but in future warnings may be added to <code>-Wformat-security</code> that are not included in <code>-Wformat-nonliteral</code>.)</p>
<dt><code>-Wformat-y2k</code></p>
<dd>If <code>-Wformat</code> is specified, also warn about <tt>&quot;strftime&quot;</tt> formats that may yield only a two-digit year.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wnonnull</code></p>
<dd>Warn about passing a null pointer for arguments marked as requiring a non-null value by the <tt>&quot;nonnull&quot;</tt> function attribute. </p>
<p> <code>-Wnonnull</code> is included in <code>-Wall</code> and <code>-Wformat</code>. It can be disabled with the <code>-Wno-nonnull</code> option.</p>
<dt><code>-Winit-self</code> (C, C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about uninitialized variables that are initialized with themselves. Note this option can only be used with the <code>-Wuninitialized</code> option. </p>
<p> For example, <font SIZE="-1">GCC</font> warns about <tt>&quot;i&quot;</tt> being uninitialized in the following snippet only when <code>-Winit-self</code> has been specified: </p>
<pre> int f()
 {
 int i = i;
 return i;
 }</pre>
<p>This warning is enabled by <code>-Wall</code> in C<font SIZE="-2">++</font>.</p>
<dt><code>-Wimplicit-int</code> (C and Objective-C only)</p>
<dd>Warn when a declaration does not specify a type. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wimplicit-function-declaration</code> (C and Objective-C only)</p>
<dd>Give a warning whenever a function is used before being declared. In C99 mode (<code>-std=c99</code> or <code>-std=gnu99</code>), this warning is enabled by default and it is made into an error by <code>-pedantic-errors</code>. This warning is also enabled by <code>-Wall</code>.</p>
<dt><code>-Wimplicit</code> (C and Objective-C only)</p>
<dd>Same as <code>-Wimplicit-int</code> and <code>-Wimplicit-function-declaration</code>. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wignored-qualifiers</code> (C and C<font SIZE="-2">++</font> only)</p>
<dd>Warn if the return type of a function has a type qualifier such as <tt>&quot;const&quot;</tt>. For <font SIZE="-1">ISO C</font> such a type qualifier has no effect, since the value returned by a function is not an lvalue. For C<font SIZE="-2">++</font>, the warning is only emitted for scalar types or <tt>&quot;void&quot;</tt>. <font SIZE="-1">ISO C</font> prohibits qualified <tt>&quot;void&quot;</tt> return types on function definitions, so such return types always receive a warning even without this option. </p>
<p> This warning is also enabled by <code>-Wextra</code>.</p>
<dt><code>-Wmain</code></p>
<dd>Warn if the type of <code>main</code> is suspicious. <code>main</code> should be a function with external linkage, returning int, taking either zero arguments, two, or three arguments of appropriate types. This warning is enabled by default in C<font SIZE="-2">++</font> and is enabled by either <code>-Wall</code> or <code>-Wpedantic</code>.</p>
<dt><code>-Wmissing-braces</code></p>
<dd>Warn if an aggregate or union initializer is not fully bracketed. In the following example, the initializer for <code>a</code> is not fully bracketed, but that for <code>b</code> is fully bracketed. This warning is enabled by <code>-Wall</code> in C. </p>
<pre> int a[2][2] = { 0, 1, 2, 3 };
 int b[2][2] = { { 0, 1 }, { 2, 3 } };</pre>
<p>This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wmissing-include-dirs</code> (C, C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if a user-supplied include directory does not exist.</p>
<dt><code>-Wparentheses</code></p>
<dd>Warn if parentheses are omitted in certain contexts, such as when there is an assignment in a context where a truth value is expected, or when operators are nested whose precedence people often get confused about. </p>
<p> Also warn if a comparison like <code>x&lt;=y&lt;=z</code> appears; this is equivalent to <code>(x&lt;=y ? 1 : 0) &lt;= z</code>, which is a different interpretation from that of ordinary mathematical notation. </p>
<p> Also warn about constructions where there may be confusion to which <tt>&quot;if&quot;</tt> statement an <tt>&quot;else&quot;</tt> branch belongs. Here is an example of such a case: </p>
<pre> {
 if (a)
 if (b)
 foo ();
 else
 bar ();
 }</pre>
<p>In C/C<font SIZE="-2">++</font>, every <tt>&quot;else&quot;</tt> branch belongs to the innermost possible <tt>&quot;if&quot;</tt> statement, which in this example is <tt>&quot;if (b)&quot;</tt>. This is often not what the programmer expected, as illustrated in the above example by indentation the programmer chose. When there is the potential for this confusion, <font SIZE="-1">GCC</font> issues a warning when this flag is specified. To eliminate the warning, add explicit braces around the innermost <tt>&quot;if&quot;</tt> statement so there is no way the <tt>&quot;else&quot;</tt> can belong to the enclosing <tt>&quot;if&quot;</tt>. The resulting code looks like this: </p>
<pre> {
 if (a)
 {
 if (b)
 foo ();
 else
 bar ();
 }
 }</pre>
<p>Also warn for dangerous uses of the <font SIZE="-1">GNU</font> extension to <tt>&quot;?:&quot;</tt> with omitted middle operand. When the condition in the <tt>&quot;?&quot;</tt>: operator is a boolean expression, the omitted value is always 1. Often programmers expect it to be a value computed inside the conditional expression instead. </p>
<p> This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wsequence-point</code></p>
<dd>Warn about code that may have undefined semantics because of violations of sequence point rules in the C and C<font SIZE="-2">++</font> standards. </p>
<p> The C and C<font SIZE="-2">++</font> standards define the order in which expressions in a C/C<font SIZE="-2">++</font> program are evaluated in terms of <i>sequence points</i>, which represent a partial ordering between the execution of parts of the program: those executed before the sequence point, and those executed after it. These occur after the evaluation of a full expression (one which is not part of a larger expression), after the evaluation of the first operand of a <tt>&quot;&amp;&amp;&quot;</tt>, <tt>&quot;||&quot;</tt>, <tt>&quot;? :&quot;</tt> or <tt>&quot;,&quot;</tt> (comma) operator, before a function is called (but after the evaluation of its arguments and the expression denoting the called function), and in certain other places. Other than as expressed by the sequence point rules, the order of evaluation of subexpressions of an expression is not specified. All these rules describe only a partial order rather than a total order, since, for example, if two functions are called within one expression with no sequence point between them, the order in which the functions are called is not specified. However, the standards committee have ruled that function calls do not overlap. </p>
<p> It is not specified when between sequence points modifications to the values of objects take effect. Programs whose behavior depends on this have undefined behavior; the C and C<font SIZE="-2">++</font> standards specify that &#8220;Between the previous and next sequence point an object shall have its stored value modified at most once by the evaluation of an expression. Furthermore, the prior value shall be read only to determine the value to be stored.&#8221;. If a program breaks these rules, the results on any particular implementation are entirely unpredictable. </p>
<p> Examples of code with undefined behavior are <tt>&quot;a = a++;&quot;</tt>, <tt>&quot;a[n] = b[n++]&quot;</tt> and <tt>&quot;a[i++] = i;&quot;</tt>. Some more complicated cases are not diagnosed by this option, and it may give an occasional false positive result, but in general it has been found fairly effective at detecting this sort of problem in programs. </p>
<p> The standard is worded confusingly, therefore there is some debate over the precise meaning of the sequence point rules in subtle cases. Links to discussions of the problem, including proposed formal definitions, may be found on the <font SIZE="-1">GCC</font> readings page, at &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/readings.html">http://gcc.gnu.org/readings.html</a></code>&gt;. </p>
<p> This warning is enabled by <code>-Wall</code> for C and C<font SIZE="-2">++</font>.</p>
<dt><code>-Wno-return-local-addr</code></p>
<dd>Do not warn about returning a pointer (or in C<font SIZE="-2">++</font>, a reference) to a variable that goes out of scope after the function returns.</p>
<dt><code>-Wreturn-type</code></p>
<dd>Warn whenever a function is defined with a return type that defaults to <tt>&quot;int&quot;</tt>. Also warn about any <tt>&quot;return&quot;</tt> statement with no return value in a function whose return type is not <tt>&quot;void&quot;</tt> (falling off the end of the function body is considered returning without a value), and about a <tt>&quot;return&quot;</tt> statement with an expression in a function whose return type is <tt>&quot;void&quot;</tt>. </p>
<p> For C<font SIZE="-2">++</font>, a function without return type always produces a diagnostic message, even when <code>-Wno-return-type</code> is specified. The only exceptions are <code>main</code> and functions defined in system headers. </p>
<p> This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wswitch</code></p>
<dd>Warn whenever a <tt>&quot;switch&quot;</tt> statement has an index of enumerated type and lacks a <tt>&quot;case&quot;</tt> for one or more of the named codes of that enumeration. (The presence of a <tt>&quot;default&quot;</tt> label prevents this warning.) <tt>&quot;case&quot;</tt> labels outside the enumeration range also provoke warnings when this option is used (even if there is a <tt>&quot;default&quot;</tt> label). This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wswitch-default</code></p>
<dd>Warn whenever a <tt>&quot;switch&quot;</tt> statement does not have a <tt>&quot;default&quot;</tt> case.</p>
<dt><code>-Wswitch-enum</code></p>
<dd>Warn whenever a <tt>&quot;switch&quot;</tt> statement has an index of enumerated type and lacks a <tt>&quot;case&quot;</tt> for one or more of the named codes of that enumeration. <tt>&quot;case&quot;</tt> labels outside the enumeration range also provoke warnings when this option is used. The only difference between <code>-Wswitch</code> and this option is that this option gives a warning about an omitted enumeration code even if there is a <tt>&quot;default&quot;</tt> label.</p>
<dt><code>-Wsync-nand</code> (C and C<font SIZE="-2">++</font> only)</p>
<dd>Warn when <tt>&quot;__sync_fetch_and_nand&quot;</tt> and <tt>&quot;__sync_nand_and_fetch&quot;</tt> built-in functions are used. These functions changed semantics in <font SIZE="-1">GCC 4.4.</font></p>
<dt><code>-Wtrigraphs</code></p>
<dd>Warn if any trigraphs are encountered that might change the meaning of the program (trigraphs within comments are not warned about). This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused-but-set-parameter</code></p>
<dd>Warn whenever a function parameter is assigned to, but otherwise unused (aside from its declaration). </p>
<p> To suppress this warning use the <code>unused</code> attribute. </p>
<p> This warning is also enabled by <code>-Wunused</code> together with <code>-Wextra</code>.</p>
<dt><code>-Wunused-but-set-variable</code></p>
<dd>Warn whenever a local variable is assigned to, but otherwise unused (aside from its declaration). This warning is enabled by <code>-Wall</code>. </p>
<p> To suppress this warning use the <code>unused</code> attribute. </p>
<p> This warning is also enabled by <code>-Wunused</code>, which is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused-function</code></p>
<dd>Warn whenever a static function is declared but not defined or a non-inline static function is unused. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused-label</code></p>
<dd>Warn whenever a label is declared but not used. This warning is enabled by <code>-Wall</code>. </p>
<p> To suppress this warning use the <code>unused</code> attribute.</p>
<dt><code>-Wunused-local-typedefs</code> (C, Objective-C, C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a typedef locally defined in a function is not used. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused-parameter</code></p>
<dd>Warn whenever a function parameter is unused aside from its declaration. </p>
<p> To suppress this warning use the <code>unused</code> attribute.</p>
<dt><code>-Wno-unused-result</code></p>
<dd>Do not warn if a caller of a function marked with attribute <tt>&quot;warn_unused_result&quot;</tt> does not use its return value. The default is <code>-Wunused-result</code>.</p>
<dt><code>-Wunused-variable</code></p>
<dd>Warn whenever a local variable or non-constant static variable is unused aside from its declaration. This warning is enabled by <code>-Wall</code>. </p>
<p> To suppress this warning use the <code>unused</code> attribute.</p>
<dt><code>-Wunused-value</code></p>
<dd>Warn whenever a statement computes a result that is explicitly not used. To suppress this warning cast the unused expression to <code>void</code>. This includes an expression-statement or the left-hand side of a comma expression that contains no side effects. For example, an expression such as <code>x[i,j]</code> causes a warning, while <code>x[(void)i,j]</code> does not. </p>
<p> This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused</code></p>
<dd>All the above <code>-Wunused</code> options combined. </p>
<p> In order to get a warning about an unused function parameter, you must either specify <code>-Wextra -Wunused</code> (note that <code>-Wall</code> implies <code>-Wunused</code>), or separately specify <code>-Wunused-parameter</code>.</p>
<dt><code>-Wuninitialized</code></p>
<dd>Warn if an automatic variable is used without first being initialized or if a variable may be clobbered by a <tt>&quot;setjmp&quot;</tt> call. In C<font SIZE="-2">++</font>, warn if a non-static reference or non-static <code>const</code> member appears in a class without constructors. </p>
<p> If you want to warn about code that uses the uninitialized value of the variable in its own initializer, use the <code>-Winit-self</code> option. </p>
<p> These warnings occur for individual uninitialized or clobbered elements of structure, union or array variables as well as for variables that are uninitialized or clobbered as a whole. They do not occur for variables or elements declared <tt>&quot;volatile&quot;</tt>. Because these warnings depend on optimization, the exact variables or elements for which there are warnings depends on the precise optimization options and version of <font SIZE="-1">GCC</font> used. </p>
<p> Note that there may be no warning about a variable that is used only to compute a value that itself is never used, because such computations may be deleted by data flow analysis before the warnings are printed.</p>
<dt><code>-Wmaybe-uninitialized</code></p>
<dd>For an automatic variable, if there exists a path from the function entry to a use of the variable that is initialized, but there exist some other paths for which the variable is not initialized, the compiler emits a warning if it cannot prove the uninitialized paths are not executed at run time. These warnings are made optional because <font SIZE="-1">GCC</font> is not smart enough to see all the reasons why the code might be correct in spite of appearing to have an error. Here is one example of how this can happen: </p>
<pre> {
 int x;
 switch (y)
 {
 case 1: x = 1;
 break;
 case 2: x = 4;
 break;
 case 3: x = 5;
 }
 foo (x);
 }</pre>
<p>If the value of <tt>&quot;y&quot;</tt> is always 1, 2 or 3, then <tt>&quot;x&quot;</tt> is always initialized, but <font SIZE="-1">GCC</font> doesn&#8217;t know this. To suppress the warning, you need to provide a default case with <i>assert</i>(0) or similar code. </p>
<p> This option also warns when a non-volatile automatic variable might be changed by a call to <tt>&quot;longjmp&quot;</tt>. These warnings as well are possible only in optimizing compilation. </p>
<p> The compiler sees only the calls to <tt>&quot;setjmp&quot;</tt>. It cannot know where <tt>&quot;longjmp&quot;</tt> will be called; in fact, a signal handler could call it at any point in the code. As a result, you may get a warning even when there is in fact no problem because <tt>&quot;longjmp&quot;</tt> cannot in fact be called at the place that would cause a problem. </p>
<p> Some spurious warnings can be avoided if you declare all the functions you use that never return as <tt>&quot;noreturn&quot;</tt>. </p>
<p> This warning is enabled by <code>-Wall</code> or <code>-Wextra</code>.</p>
<dt><code>-Wunknown-pragmas</code></p>
<dd>Warn when a <tt>&quot;#pragma&quot;</tt> directive is encountered that is not understood by <font SIZE="-1">GCC. </font> If this command-line option is used, warnings are even issued for unknown pragmas in system header files. This is not the case if the warnings are only enabled by the <code>-Wall</code> command-line option.</p>
<dt><code>-Wno-pragmas</code></p>
<dd>Do not warn about misuses of pragmas, such as incorrect parameters, invalid syntax, or conflicts between pragmas. See also <code>-Wunknown-pragmas</code>.</p>
<dt><code>-Wstrict-aliasing</code></p>
<dd>This option is only active when <code>-fstrict-aliasing</code> is active. It warns about code that might break the strict aliasing rules that the compiler is using for optimization. The warning does not catch all cases, but does attempt to catch the more common pitfalls. It is included in <code>-Wall</code>. It is equivalent to <code>-Wstrict-aliasing=3</code></p>
<dt><code>-Wstrict-aliasing=n</code></p>
<dd>This option is only active when <code>-fstrict-aliasing</code> is active. It warns about code that might break the strict aliasing rules that the compiler is using for optimization. Higher levels correspond to higher accuracy (fewer false positives). Higher levels also correspond to more effort, similar to the way <code>-O</code> works. <code>-Wstrict-aliasing</code> is equivalent to <code>-Wstrict-aliasing=3</code>. </p>
<p> Level 1: Most aggressive, quick, least accurate. Possibly useful when higher levels do not warn but <code>-fstrict-aliasing</code> still breaks the code, as it has very few false negatives. However, it has many false positives. Warns for all pointer conversions between possibly incompatible types, even if never dereferenced. Runs in the front end only. </p>
<p> Level 2: Aggressive, quick, not too precise. May still have many false positives (not as many as level 1 though), and few false negatives (but possibly more than level 1). Unlike level 1, it only warns when an address is taken. Warns about incomplete types. Runs in the front end only. </p>
<p> Level 3 (default for <code>-Wstrict-aliasing</code>): Should have very few false positives and few false negatives. Slightly slower than levels 1 or 2 when optimization is enabled. Takes care of the common pun+dereference pattern in the front end: <tt>&quot;*(int*)&amp;some_float&quot;</tt>. If optimization is enabled, it also runs in the back end, where it deals with multiple statement cases using flow-sensitive points-to information. Only warns when the converted pointer is dereferenced. Does not warn about incomplete types.</p>
<dt><code>-Wstrict-overflow</code></p>
<dd>
<dt><code>-Wstrict-overflow=</code><i>n</i></p>
<dd>This option is only active when <code>-fstrict-overflow</code> is active. It warns about cases where the compiler optimizes based on the assumption that signed overflow does not occur. Note that it does not warn about all cases where the code might overflow: it only warns about cases where the compiler implements some optimization. Thus this warning depends on the optimization level. </p>
<p> An optimization that assumes that signed overflow does not occur is perfectly safe if the values of the variables involved are such that overflow never does, in fact, occur. Therefore this warning can easily give a false positive: a warning about code that is not actually a problem. To help focus on important issues, several warning levels are defined. No warnings are issued for the use of undefined signed overflow when estimating how many iterations a loop requires, in particular when determining whether a loop will be executed at all.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-Wstrict-overflow=1</code></p>
<dd>Warn about cases that are both questionable and easy to avoid. For example, with <code>-fstrict-overflow</code>, the compiler simplifies <tt>&quot;x + 1 &gt; x&quot;</tt> to <tt>1</tt>. This level of <code>-Wstrict-overflow</code> is enabled by <code>-Wall</code>; higher levels are not, and must be explicitly requested.</p>
<dt><code>-Wstrict-overflow=2</code></p>
<dd>Also warn about other cases where a comparison is simplified to a constant. For example: <tt>&quot;abs (x) &gt;= 0&quot;</tt>. This can only be simplified when <code>-fstrict-overflow</code> is in effect, because <tt>&quot;abs (INT_MIN)&quot;</tt> overflows to <tt>&quot;INT_MIN&quot;</tt>, which is less than zero. <code>-Wstrict-overflow</code> (with no level) is the same as <code>-Wstrict-overflow=2</code>.</p>
<dt><code>-Wstrict-overflow=3</code></p>
<dd>Also warn about other cases where a comparison is simplified. For example: <tt>&quot;x + 1 &gt; 1&quot;</tt> is simplified to <tt>&quot;x &gt; 0&quot;</tt>.</p>
<dt><code>-Wstrict-overflow=4</code></p>
<dd>Also warn about other simplifications not covered by the above cases. For example: <tt>&quot;(x * 10) / 5&quot;</tt> is simplified to <tt>&quot;x * 2&quot;</tt>.</p>
<dt><code>-Wstrict-overflow=5</code></p>
<dd>Also warn about cases where the compiler reduces the magnitude of a constant involved in a comparison. For example: <tt>&quot;x + 2 &gt; y&quot;</tt> is simplified to <tt>&quot;x + 1 &gt;= y&quot;</tt>. This is reported only at the highest warning level because this simplification applies to many comparisons, so this warning level gives a very large number of false positives.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wsuggest-attribute=</code>[<code>pure</code>|<code>const</code>|<code>noreturn</code>|<code>format</code>]</p>
<dd>Warn for cases where adding an attribute may be beneficial. The attributes currently supported are listed below.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-Wsuggest-attribute=pure</code></p>
<dd>
<dt><code>-Wsuggest-attribute=const</code></p>
<dd>
<dt><code>-Wsuggest-attribute=noreturn</code></p>
<dd>Warn about functions that might be candidates for attributes <tt>&quot;pure&quot;</tt>, <tt>&quot;const&quot;</tt> or <tt>&quot;noreturn&quot;</tt>. The compiler only warns for functions visible in other compilation units or (in the case of <tt>&quot;pure&quot;</tt> and <tt>&quot;const&quot;</tt>) if it cannot prove that the function returns normally. A function returns normally if it doesn&#8217;t contain an infinite loop or return abnormally by throwing, calling <tt>&quot;abort()&quot;</tt> or trapping. This analysis requires option <code>-fipa-pure-const</code>, which is enabled by default at <code>-O</code> and higher. Higher optimization levels improve the accuracy of the analysis.</p>
<dt><code>-Wsuggest-attribute=format</code></p>
<dd>
<dt><code>-Wmissing-format-attribute</code></p>
<dd>Warn about function pointers that might be candidates for <tt>&quot;format&quot;</tt> attributes. Note these are only possible candidates, not absolute ones. <font SIZE="-1">GCC</font> guesses that function pointers with <tt>&quot;format&quot;</tt> attributes that are used in assignment, initialization, parameter passing or return statements should have a corresponding <tt>&quot;format&quot;</tt> attribute in the resulting type. I.e. the left-hand side of the assignment or initialization, the type of the parameter variable, or the return type of the containing function respectively should also have a <tt>&quot;format&quot;</tt> attribute to avoid the warning. </p>
<p> <font SIZE="-1">GCC</font> also warns about function definitions that might be candidates for <tt>&quot;format&quot;</tt> attributes. Again, these are only possible candidates. <font SIZE="-1">GCC</font> guesses that <tt>&quot;format&quot;</tt> attributes might be appropriate for any function that calls a function like <tt>&quot;vprintf&quot;</tt> or <tt>&quot;vscanf&quot;</tt>, but this might not always be the case, and some functions for which <tt>&quot;format&quot;</tt> attributes are appropriate may not be detected.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Warray-bounds</code></p>
<dd>This option is only active when <code>-ftree-vrp</code> is active (default for <code>-O2</code> and above). It warns about subscripts to arrays that are always out of bounds. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wno-div-by-zero</code></p>
<dd>Do not warn about compile-time integer division by zero. Floating-point division by zero is not warned about, as it can be a legitimate way of obtaining infinities and NaNs.</p>
<dt><code>-Wsystem-headers</code></p>
<dd>Print warning messages for constructs found in system header files. Warnings from system headers are normally suppressed, on the assumption that they usually do not indicate real problems and would only make the compiler output harder to read. Using this command-line option tells <font SIZE="-1">GCC</font> to emit warnings from system headers as if they occurred in user code. However, note that using <code>-Wall</code> in conjunction with this option does <i>not</i> warn about unknown pragmas in system headers&#8212;for that, <code>-Wunknown-pragmas</code> must also be used.</p>
<dt><code>-Wtrampolines</code></p>
<dd>
<pre> Warn about trampolines generated for pointers to nested functions.
 A trampoline is a small piece of data or code that is created at run
 time on the stack when the address of a nested function is taken, and
 is used to call the nested function indirectly. For some targets, it
 is made up of data only and thus requires no special treatment. But,
 for most targets, it is made up of code and thus requires the stack
 to be made executable in order for the program to work properly.</pre>
<dt><code>-Wfloat-equal</code></p>
<dd>Warn if floating-point values are used in equality comparisons. </p>
<p> The idea behind this is that sometimes it is convenient (for the programmer) to consider floating-point values as approximations to infinitely precise real numbers. If you are doing this, then you need to compute (by analyzing the code, or in some other way) the maximum or likely maximum error that the computation introduces, and allow for it when performing comparisons (and when producing output, but that&#8217;s a different problem). In particular, instead of testing for equality, you should check to see whether the two values have ranges that overlap; and this is done with the relational operators, so equality comparisons are probably mistaken.</p>
<dt><code>-Wtraditional</code> (C and Objective-C only)</p>
<dd>Warn about certain constructs that behave differently in traditional and <font SIZE="-1">ISO C. </font> Also warn about <font SIZE="-1">ISO C</font> constructs that have no traditional C equivalent, and/or problematic constructs that should be avoided.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Macro parameters that appear within string literals in the macro body. In traditional C macro replacement takes place within string literals, but in <font SIZE="-1">ISO C</font> it does not.</p>
<dt>&bull;</p>
<dd>In traditional C, some preprocessor directives did not exist. Traditional preprocessors only considered a line to be a directive if the <code>#</code> appeared in column 1 on the line. Therefore <code>-Wtraditional</code> warns about directives that traditional C understands but ignores because the <code>#</code> does not appear as the first character on the line. It also suggests you hide directives like <code>#pragma</code> not understood by traditional C by indenting them. Some traditional implementations do not recognize <code>#elif</code>, so this option suggests avoiding it altogether.</p>
<dt>&bull;</p>
<dd>A function-like macro that appears without arguments.</p>
<dt>&bull;</p>
<dd>The unary plus operator.</p>
<dt>&bull;</p>
<dd>The <code>U</code> integer constant suffix, or the <code>F</code> or <code>L</code> floating-point constant suffixes. (Traditional C does support the <code>L</code> suffix on integer constants.) Note, these suffixes appear in macros defined in the system headers of most modern systems, e.g. the <code>_MIN</code>/<code>_MAX</code> macros in <tt>&quot;&lt;limits.h&gt;&quot;</tt>. Use of these macros in user code might normally lead to spurious warnings, however <font SIZE="-1">GCC</font>&#8216;s integrated preprocessor has enough context to avoid warning in these cases.</p>
<dt>&bull;</p>
<dd>A function declared external in one block and then used after the end of the block.</p>
<dt>&bull;</p>
<dd>A <tt>&quot;switch&quot;</tt> statement has an operand of type <tt>&quot;long&quot;</tt>.</p>
<dt>&bull;</p>
<dd>A non-<tt>&quot;static&quot;</tt> function declaration follows a <tt>&quot;static&quot;</tt> one. This construct is not accepted by some traditional C compilers.</p>
<dt>&bull;</p>
<dd>The <font SIZE="-1">ISO</font> type of an integer constant has a different width or signedness from its traditional type. This warning is only issued if the base of the constant is ten. I.e. hexadecimal or octal values, which typically represent bit patterns, are not warned about.</p>
<dt>&bull;</p>
<dd>Usage of <font SIZE="-1">ISO</font> string concatenation is detected.</p>
<dt>&bull;</p>
<dd>Initialization of automatic aggregates.</p>
<dt>&bull;</p>
<dd>Identifier conflicts with labels. Traditional C lacks a separate namespace for labels.</p>
<dt>&bull;</p>
<dd>Initialization of unions. If the initializer is zero, the warning is omitted. This is done under the assumption that the zero initializer in user code appears conditioned on e.g. <tt>&quot;__STDC__&quot;</tt> to avoid missing initializer warnings and relies on default initialization to zero in the traditional C case.</p>
<dt>&bull;</p>
<dd>Conversions by prototypes between fixed/floating-point values and vice versa. The absence of these prototypes when compiling with traditional C causes serious problems. This is a subset of the possible conversion warnings; for the full set use <code>-Wtraditional-conversion</code>.</p>
<dt>&bull;</p>
<dd>Use of <font SIZE="-1">ISO C</font> style function definitions. This warning intentionally is <i>not</i> issued for prototype declarations or variadic functions because these <font SIZE="-1">ISO C</font> features appear in your code when using libiberty&#8217;s traditional C compatibility macros, <tt>&quot;PARAMS&quot;</tt> and <tt>&quot;VPARAMS&quot;</tt>. This warning is also bypassed for nested functions because that feature is already a <font SIZE="-1">GCC</font> extension and thus not relevant to traditional C compatibility.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wtraditional-conversion</code> (C and Objective-C only)</p>
<dd>Warn if a prototype causes a type conversion that is different from what would happen to the same argument in the absence of a prototype. This includes conversions of fixed point to floating and vice versa, and conversions changing the width or signedness of a fixed-point argument except when the same as the default promotion.</p>
<dt><code>-Wdeclaration-after-statement</code> (C and Objective-C only)</p>
<dd>Warn when a declaration is found after a statement in a block. This construct, known from C<font SIZE="-2">++</font>, was introduced with <font SIZE="-1">ISO C99</font> and is by default allowed in <font SIZE="-1">GCC. </font> It is not supported by <font SIZE="-1">ISO C90</font> and was not supported by <font SIZE="-1">GCC</font> versions before <font SIZE="-1">GCC 3.0. </font></p>
<dt><code>-Wundef</code></p>
<dd>Warn if an undefined identifier is evaluated in an <code>#if</code> directive.</p>
<dt><code>-Wno-endif-labels</code></p>
<dd>Do not warn whenever an <code>#else</code> or an <code>#endif</code> are followed by text.</p>
<dt><code>-Wshadow</code></p>
<dd>Warn whenever a local variable or type declaration shadows another variable, parameter, type, or class member (in C<font SIZE="-2">++</font>), or whenever a built-in function is shadowed. Note that in C<font SIZE="-2">++</font>, the compiler warns if a local variable shadows an explicit typedef, but not if it shadows a struct/class/enum.</p>
<dt><code>-Wlarger-than=</code><i>len</i></p>
<dd>Warn whenever an object of larger than <i>len</i> bytes is defined.</p>
<dt><code>-Wframe-larger-than=</code><i>len</i></p>
<dd>Warn if the size of a function frame is larger than <i>len</i> bytes. The computation done to determine the stack frame size is approximate and not conservative. The actual requirements may be somewhat greater than <i>len</i> even if you do not get a warning. In addition, any space allocated via <tt>&quot;alloca&quot;</tt>, variable-length arrays, or related constructs is not included by the compiler when determining whether or not to issue a warning.</p>
<dt><code>-Wno-free-nonheap-object</code></p>
<dd>Do not warn when attempting to free an object that was not allocated on the heap.</p>
<dt><code>-Wstack-usage=</code><i>len</i></p>
<dd>Warn if the stack usage of a function might be larger than <i>len</i> bytes. The computation done to determine the stack usage is conservative. Any space allocated via <tt>&quot;alloca&quot;</tt>, variable-length arrays, or related constructs is included by the compiler when determining whether or not to issue a warning. </p>
<p> The message is in keeping with the output of <code>-fstack-usage</code>.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>If the stack usage is fully static but exceeds the specified amount, it&#8217;s: </p>
<pre> warning: stack usage is 1120 bytes</pre>
<dt>&bull;</p>
<dd>If the stack usage is (partly) dynamic but bounded, it&#8217;s: </p>
<pre> warning: stack usage might be 1648 bytes</pre>
<dt>&bull;</p>
<dd>If the stack usage is (partly) dynamic and not bounded, it&#8217;s: </p>
<pre> warning: stack usage might be unbounded</pre>
</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wunsafe-loop-optimizations</code></p>
<dd>Warn if the loop cannot be optimized because the compiler cannot assume anything on the bounds of the loop indices. With <code>-funsafe-loop-optimizations</code> warn if the compiler makes such assumptions.</p>
<dt><code>-Wno-pedantic-ms-format</code> (MinGW targets only)</p>
<dd>When used in combination with <code>-Wformat</code> and <code>-pedantic</code> without <font SIZE="-1">GNU</font> extensions, this option disables the warnings about non-ISO <tt>&quot;printf&quot;</tt> / <tt>&quot;scanf&quot;</tt> format width specifiers <tt>&quot;I32&quot;</tt>, <tt>&quot;I64&quot;</tt>, and <tt>&quot;I&quot;</tt> used on Windows targets, which depend on the <font SIZE="-1">MS</font> runtime.</p>
<dt><code>-Wpointer-arith</code></p>
<dd>Warn about anything that depends on the &#8220;size of&#8221; a function type or of <tt>&quot;void&quot;</tt>. <font SIZE="-1">GNU C</font> assigns these types a size of 1, for convenience in calculations with <tt>&quot;void *&quot;</tt> pointers and pointers to functions. In C<font SIZE="-2">++</font>, warn also when an arithmetic operation involves <tt>&quot;NULL&quot;</tt>. This warning is also enabled by <code>-Wpedantic</code>.</p>
<dt><code>-Wtype-limits</code></p>
<dd>Warn if a comparison is always true or always false due to the limited range of the data type, but do not warn for constant expressions. For example, warn if an unsigned variable is compared against zero with <code>&lt;</code> or <code>&gt;=</code>. This warning is also enabled by <code>-Wextra</code>.</p>
<dt><code>-Wbad-function-cast</code> (C and Objective-C only)</p>
<dd>Warn whenever a function call is cast to a non-matching type. For example, warn if <tt>&quot;int malloc()&quot;</tt> is cast to <tt>&quot;anything *&quot;</tt>.</p>
<dt><code>-Wc++-compat</code> (C and Objective-C only)</p>
<dd>Warn about <font SIZE="-1">ISO C</font> constructs that are outside of the common subset of <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font>,</font> e.g. request for implicit conversion from <tt>&quot;void *&quot;</tt> to a pointer to non-<tt>&quot;void&quot;</tt> type.</p>
<dt><code>-Wc++11-compat</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about C<font SIZE="-2">++</font> constructs whose meaning differs between <font SIZE="-1">ISO C<font SIZE="-2">++</font> 1998</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font> 2011,</font> e.g., identifiers in <font SIZE="-1">ISO C<font SIZE="-2">++</font> 1998</font> that are keywords in <font SIZE="-1">ISO C<font SIZE="-2">++</font> 2011. </font> This warning turns on <code>-Wnarrowing</code> and is enabled by <code>-Wall</code>.</p>
<dt><code>-Wcast-qual</code></p>
<dd>Warn whenever a pointer is cast so as to remove a type qualifier from the target type. For example, warn if a <tt>&quot;const char *&quot;</tt> is cast to an ordinary <tt>&quot;char *&quot;</tt>. </p>
<p> Also warn when making a cast that introduces a type qualifier in an unsafe way. For example, casting <tt>&quot;char **&quot;</tt> to <tt>&quot;const char **&quot;</tt> is unsafe, as in this example: </p>
<pre> /* p is char ** value. */
 const char **q = (const char **) p;
 /* Assignment of readonly string to const char * is OK. */
 *q = &quot;string&quot;;
 /* Now char** pointer points to read-only memory. */
 **p = 'b';</pre>
<dt><code>-Wcast-align</code></p>
<dd>Warn whenever a pointer is cast such that the required alignment of the target is increased. For example, warn if a <tt>&quot;char *&quot;</tt> is cast to an <tt>&quot;int *&quot;</tt> on machines where integers can only be accessed at two- or four-byte boundaries.</p>
<dt><code>-Wwrite-strings</code></p>
<dd>When compiling C, give string constants the type <tt>&quot;const char[</tt>length<tt>]&quot;</tt> so that copying the address of one into a non-<tt>&quot;const&quot;</tt> <tt>&quot;char *&quot;</tt> pointer produces a warning. These warnings help you find at compile time code that can try to write into a string constant, but only if you have been very careful about using <tt>&quot;const&quot;</tt> in declarations and prototypes. Otherwise, it is just a nuisance. This is why we did not make <code>-Wall</code> request these warnings. </p>
<p> When compiling C<font SIZE="-2">++</font>, warn about the deprecated conversion from string literals to <tt>&quot;char *&quot;</tt>. This warning is enabled by default for C<font SIZE="-2">++</font> programs.</p>
<dt><code>-Wclobbered</code></p>
<dd>Warn for variables that might be changed by <code>longjmp</code> or <code>vfork</code>. This warning is also enabled by <code>-Wextra</code>.</p>
<dt><code>-Wconditionally-supported</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn for conditionally-supported (C<font SIZE="-2">++</font>11 [intro.defs]) constructs.</p>
<dt><code>-Wconversion</code></p>
<dd>Warn for implicit conversions that may alter a value. This includes conversions between real and integer, like <tt>&quot;abs (x)&quot;</tt> when <tt>&quot;x&quot;</tt> is <tt>&quot;double&quot;</tt>; conversions between signed and unsigned, like <tt>&quot;unsigned ui = -1&quot;</tt>; and conversions to smaller types, like <tt>&quot;sqrtf (M_PI)&quot;</tt>. Do not warn for explicit casts like <tt>&quot;abs ((int) x)&quot;</tt> and <tt>&quot;ui = (unsigned) -1&quot;</tt>, or if the value is not changed by the conversion like in <tt>&quot;abs (2.0)&quot;</tt>. Warnings about conversions between signed and unsigned integers can be disabled by using <code>-Wno-sign-conversion</code>. </p>
<p> For C<font SIZE="-2">++</font>, also warn for confusing overload resolution for user-defined conversions; and conversions that never use a type conversion operator: conversions to <tt>&quot;void&quot;</tt>, the same type, a base class or a reference to them. Warnings about conversions between signed and unsigned integers are disabled by default in C<font SIZE="-2">++</font> unless <code>-Wsign-conversion</code> is explicitly enabled.</p>
<dt><code>-Wno-conversion-null</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Do not warn for conversions between <tt>&quot;NULL&quot;</tt> and non-pointer types. <code>-Wconversion-null</code> is enabled by default.</p>
<dt><code>-Wzero-as-null-pointer-constant</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a literal &#8216;0&#8217; is used as null pointer constant. This can be useful to facilitate the conversion to <tt>&quot;nullptr&quot;</tt> in C<font SIZE="-2">++</font>11.</p>
<dt><code>-Wdate-time</code></p>
<dd>Warn when macros <tt>&quot;__TIME__&quot;</tt>, <tt>&quot;__DATE__&quot;</tt> or <tt>&quot;__TIMESTAMP__&quot;</tt> are encountered as they might prevent bit-wise-identical reproducible compilations.</p>
<dt><code>-Wdelete-incomplete</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when deleting a pointer to incomplete type, which may cause undefined behavior at runtime. This warning is enabled by default.</p>
<dt><code>-Wuseless-cast</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when an expression is casted to its own type.</p>
<dt><code>-Wempty-body</code></p>
<dd>Warn if an empty body occurs in an <code>if</code>, <code>else</code> or <code>do while</code> statement. This warning is also enabled by <code>-Wextra</code>.</p>
<dt><code>-Wenum-compare</code></p>
<dd>Warn about a comparison between values of different enumerated types. In C<font SIZE="-2">++</font> enumeral mismatches in conditional expressions are also diagnosed and the warning is enabled by default. In C this warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wjump-misses-init</code> (C, Objective-C only)</p>
<dd>Warn if a <tt>&quot;goto&quot;</tt> statement or a <tt>&quot;switch&quot;</tt> statement jumps forward across the initialization of a variable, or jumps backward to a label after the variable has been initialized. This only warns about variables that are initialized when they are declared. This warning is only supported for C and Objective-C; in C<font SIZE="-2">++</font> this sort of branch is an error in any case. </p>
<p> <code>-Wjump-misses-init</code> is included in <code>-Wc++-compat</code>. It can be disabled with the <code>-Wno-jump-misses-init</code> option.</p>
<dt><code>-Wsign-compare</code></p>
<dd>Warn when a comparison between signed and unsigned values could produce an incorrect result when the signed value is converted to unsigned. This warning is also enabled by <code>-Wextra</code>; to get the other warnings of <code>-Wextra</code> without this warning, use <code>-Wextra -Wno-sign-compare</code>.</p>
<dt><code>-Wsign-conversion</code></p>
<dd>Warn for implicit conversions that may change the sign of an integer value, like assigning a signed integer expression to an unsigned integer variable. An explicit cast silences the warning. In C, this option is enabled also by <code>-Wconversion</code>.</p>
<dt><code>-Wfloat-conversion</code></p>
<dd>Warn for implicit conversions that reduce the precision of a real value. This includes conversions from real to integer, and from higher precision real to lower precision real values. This option is also enabled by <code>-Wconversion</code>.</p>
<dt><code>-Wsizeof-pointer-memaccess</code></p>
<dd>Warn for suspicious length parameters to certain string and memory built-in functions if the argument uses <tt>&quot;sizeof&quot;</tt>. This warning warns e.g. about <tt>&quot;memset (ptr, 0, sizeof (ptr));&quot;</tt> if <tt>&quot;ptr&quot;</tt> is not an array, but a pointer, and suggests a possible fix, or about <tt>&quot;memcpy (&amp;foo, ptr, sizeof (&amp;foo));&quot;</tt>. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Waddress</code></p>
<dd>Warn about suspicious uses of memory addresses. These include using the address of a function in a conditional expression, such as <tt>&quot;void func(void); if (func)&quot;</tt>, and comparisons against the memory address of a string literal, such as <tt>&quot;if (x == &quot;abc&quot;)&quot;</tt>. Such uses typically indicate a programmer error: the address of a function always evaluates to true, so their use in a conditional usually indicate that the programmer forgot the parentheses in a function call; and comparisons against string literals result in unspecified behavior and are not portable in C, so they usually indicate that the programmer intended to use <tt>&quot;strcmp&quot;</tt>. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wlogical-op</code></p>
<dd>Warn about suspicious uses of logical operators in expressions. This includes using logical operators in contexts where a bit-wise operator is likely to be expected.</p>
<dt><code>-Waggregate-return</code></p>
<dd>Warn if any functions that return structures or unions are defined or called. (In languages where you can return an array, this also elicits a warning.)</p>
<dt><code>-Wno-aggressive-loop-optimizations</code></p>
<dd>Warn if in a loop with constant number of iterations the compiler detects undefined behavior in some statement during one or more of the iterations.</p>
<dt><code>-Wno-attributes</code></p>
<dd>Do not warn if an unexpected <tt>&quot;__attribute__&quot;</tt> is used, such as unrecognized attributes, function attributes applied to variables, etc. This does not stop errors for incorrect use of supported attributes.</p>
<dt><code>-Wno-builtin-macro-redefined</code></p>
<dd>Do not warn if certain built-in macros are redefined. This suppresses warnings for redefinition of <tt>&quot;__TIMESTAMP__&quot;</tt>, <tt>&quot;__TIME__&quot;</tt>, <tt>&quot;__DATE__&quot;</tt>, <tt>&quot;__FILE__&quot;</tt>, and <tt>&quot;__BASE_FILE__&quot;</tt>.</p>
<dt><code>-Wstrict-prototypes</code> (C and Objective-C only)</p>
<dd>Warn if a function is declared or defined without specifying the argument types. (An old-style function definition is permitted without a warning if preceded by a declaration that specifies the argument types.)</p>
<dt><code>-Wold-style-declaration</code> (C and Objective-C only)</p>
<dd>Warn for obsolescent usages, according to the C Standard, in a declaration. For example, warn if storage-class specifiers like <tt>&quot;static&quot;</tt> are not the first things in a declaration. This warning is also enabled by <code>-Wextra</code>.</p>
<dt><code>-Wold-style-definition</code> (C and Objective-C only)</p>
<dd>Warn if an old-style function definition is used. A warning is given even if there is a previous prototype.</p>
<dt><code>-Wmissing-parameter-type</code> (C and Objective-C only)</p>
<dd>A function parameter is declared without a type specifier in K&amp;R-style functions: </p>
<pre> void foo(bar) { }</pre>
<p>This warning is also enabled by <code>-Wextra</code>.</p>
<dt><code>-Wmissing-prototypes</code> (C and Objective-C only)</p>
<dd>Warn if a global function is defined without a previous prototype declaration. This warning is issued even if the definition itself provides a prototype. Use this option to detect global functions that do not have a matching prototype declaration in a header file. This option is not valid for C<font SIZE="-2">++</font> because all function declarations provide prototypes and a non-matching declaration will declare an overload rather than conflict with an earlier declaration. Use <code>-Wmissing-declarations</code> to detect missing declarations in C<font SIZE="-2">++</font>.</p>
<dt><code>-Wmissing-declarations</code></p>
<dd>Warn if a global function is defined without a previous declaration. Do so even if the definition itself provides a prototype. Use this option to detect global functions that are not declared in header files. In C, no warnings are issued for functions with previous non-prototype declarations; use <code>-Wmissing-prototype</code> to detect missing prototypes. In C<font SIZE="-2">++</font>, no warnings are issued for function templates, or for inline functions, or for functions in anonymous namespaces.</p>
<dt><code>-Wmissing-field-initializers</code></p>
<dd>Warn if a structure&#8217;s initializer has some fields missing. For example, the following code causes such a warning, because <tt>&quot;x.h&quot;</tt> is implicitly zero: </p>
<pre> struct s { int f, g, h; };
 struct s x = { 3, 4 };</pre>
<p>This option does not warn about designated initializers, so the following modification does not trigger a warning: </p>
<pre> struct s { int f, g, h; };
 struct s x = { .f = 3, .g = 4 };</pre>
<p>This warning is included in <code>-Wextra</code>. To get other <code>-Wextra</code> warnings without this one, use <code>-Wextra -Wno-missing-field-initializers</code>.</p>
<dt><code>-Wno-multichar</code></p>
<dd>Do not warn if a multicharacter constant (<code>&#8216;</code><font SIZE="-1"><code>FOOF</code></font><code>&#8216;</code>) is used. Usually they indicate a typo in the user&#8217;s code, as they have implementation-defined values, and should not be used in portable code.</p>
<dt><code>-Wnormalized=&lt;none|id|nfc|nfkc&gt;</code></p>
<dd>In <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font>,</font> two identifiers are different if they are different sequences of characters. However, sometimes when characters outside the basic <font SIZE="-1">ASCII</font> character set are used, you can have two different character sequences that look the same. To avoid confusion, the <font SIZE="-1">ISO 10646</font> standard sets out some <i>normalization rules</i> which when applied ensure that two sequences that look the same are turned into the same sequence. <font SIZE="-1">GCC</font> can warn you if you are using identifiers that have not been normalized; this option controls that warning. </p>
<p> There are four levels of warning supported by <font SIZE="-1">GCC. </font> The default is <code>-Wnormalized=nfc</code>, which warns about any identifier that is not in the <font SIZE="-1">ISO 10646 &#8220;C&#8221;</font> normalized form, <i></i><font SIZE="-1"><i>NFC</i></font><i></i>. <font SIZE="-1">NFC</font> is the recommended form for most uses. </p>
<p> Unfortunately, there are some characters allowed in identifiers by <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> that, when turned into <font SIZE="-1">NFC,</font> are not allowed in identifiers. That is, there&#8217;s no way to use these symbols in portable <font SIZE="-1">ISO C</font> or C<font SIZE="-2">++</font> and have all your identifiers in <font SIZE="-1">NFC. </font><code>-Wnormalized=id</code> suppresses the warning for these characters. It is hoped that future versions of the standards involved will correct this, which is why this option is not the default. </p>
<p> You can switch the warning off for all characters by writing <code>-Wnormalized=none</code>. You should only do this if you are using some other normalization scheme (like &#8220;D&#8221;), because otherwise you can easily create bugs that are literally impossible to see. </p>
<p> Some characters in <font SIZE="-1">ISO 10646</font> have distinct meanings but look identical in some fonts or display methodologies, especially once formatting has been applied. For instance <tt>&quot;ⁿ&quot;</tt>, &#8220;<font SIZE="-1">SUPERSCRIPT LATIN SMALL LETTER N&#8221;,</font> displays just like a regular <tt>&quot;n&quot;</tt> that has been placed in a superscript. <font SIZE="-1">ISO 10646</font> defines the <i></i><font SIZE="-1"><i>NFKC</i></font><i></i> normalization scheme to convert all these into a standard form as well, and <font SIZE="-1">GCC</font> warns if your code is not in <font SIZE="-1">NFKC</font> if you use <code>-Wnormalized=nfkc</code>. This warning is comparable to warning about every identifier that contains the letter O because it might be confused with the digit 0, and so is not the default, but may be useful as a local coding convention if the programming environment cannot be fixed to display these characters distinctly.</p>
<dt><code>-Wno-deprecated</code></p>
<dd>Do not warn about usage of deprecated features.</p>
<dt><code>-Wno-deprecated-declarations</code></p>
<dd>Do not warn about uses of functions, variables, and types marked as deprecated by using the <tt>&quot;deprecated&quot;</tt> attribute.</p>
<dt><code>-Wno-overflow</code></p>
<dd>Do not warn about compile-time overflow in constant expressions.</p>
<dt><code>-Wopenmp-simd</code></p>
<dd>Warn if the vectorizer cost model overrides the OpenMP or the Cilk Plus simd directive set by user. The <code>-fsimd-cost-model=unlimited</code> can be used to relax the cost model.</p>
<dt><code>-Woverride-init</code> (C and Objective-C only)</p>
<dd>Warn if an initialized field without side effects is overridden when using designated initializers. </p>
<p> This warning is included in <code>-Wextra</code>. To get other <code>-Wextra</code> warnings without this one, use <code>-Wextra -Wno-override-init</code>.</p>
<dt><code>-Wpacked</code></p>
<dd>Warn if a structure is given the packed attribute, but the packed attribute has no effect on the layout or size of the structure. Such structures may be mis-aligned for little benefit. For instance, in this code, the variable <tt>&quot;f.x&quot;</tt> in <tt>&quot;struct bar&quot;</tt> is misaligned even though <tt>&quot;struct bar&quot;</tt> does not itself have the packed attribute: </p>
<pre> struct foo {
 int x;
 char a, b, c, d;
 } __attribute__((packed));
 struct bar {
 char z;
 struct foo f;
 };</pre>
<dt><code>-Wpacked-bitfield-compat</code></p>
<dd>The 4.1, 4.2 and 4.3 series of <font SIZE="-1">GCC</font> ignore the <tt>&quot;packed&quot;</tt> attribute on bit-fields of type <tt>&quot;char&quot;</tt>. This has been fixed in <font SIZE="-1">GCC 4.4</font> but the change can lead to differences in the structure layout. <font SIZE="-1">GCC</font> informs you when the offset of such a field has changed in <font SIZE="-1">GCC 4.4.</font> For example there is no longer a 4-bit padding between field <tt>&quot;a&quot;</tt> and <tt>&quot;b&quot;</tt> in this structure: </p>
<pre> struct foo
 {
 char a:4;
 char b:8;
 } __attribute__ ((packed));</pre>
<p>This warning is enabled by default. Use <code>-Wno-packed-bitfield-compat</code> to disable this warning.</p>
<dt><code>-Wpadded</code></p>
<dd>Warn if padding is included in a structure, either to align an element of the structure or to align the whole structure. Sometimes when this happens it is possible to rearrange the fields of the structure to reduce the padding and so make the structure smaller.</p>
<dt><code>-Wredundant-decls</code></p>
<dd>Warn if anything is declared more than once in the same scope, even in cases where multiple declaration is valid and changes nothing.</p>
<dt><code>-Wnested-externs</code> (C and Objective-C only)</p>
<dd>Warn if an <tt>&quot;extern&quot;</tt> declaration is encountered within a function.</p>
<dt><code>-Wno-inherited-variadic-ctor</code></p>
<dd>Suppress warnings about use of C<font SIZE="-2">++</font>11 inheriting constructors when the base class inherited from has a C variadic constructor; the warning is on by default because the ellipsis is not inherited.</p>
<dt><code>-Winline</code></p>
<dd>Warn if a function that is declared as inline cannot be inlined. Even with this option, the compiler does not warn about failures to inline functions declared in system headers. </p>
<p> The compiler uses a variety of heuristics to determine whether or not to inline a function. For example, the compiler takes into account the size of the function being inlined and the amount of inlining that has already been done in the current function. Therefore, seemingly insignificant changes in the source program can cause the warnings produced by <code>-Winline</code> to appear or disappear.</p>
<dt><code>-Wno-invalid-offsetof</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Suppress warnings from applying the <code>offsetof</code> macro to a non-POD type. According to the 1998 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard, applying <code>offsetof</code> to a non-POD type is undefined. In existing C<font SIZE="-2">++</font> implementations, however, <code>offsetof</code> typically gives meaningful results even when applied to certain kinds of non-POD types (such as a simple <code>struct</code> that fails to be a <font SIZE="-1">POD</font> type only by virtue of having a constructor). This flag is for users who are aware that they are writing nonportable code and who have deliberately chosen to ignore the warning about it. </p>
<p> The restrictions on <code>offsetof</code> may be relaxed in a future version of the C<font SIZE="-2">++</font> standard.</p>
<dt><code>-Wno-int-to-pointer-cast</code></p>
<dd>Suppress warnings from casts to pointer type of an integer of a different size. In C<font SIZE="-2">++</font>, casting to a pointer type of smaller size is an error. <code>Wint-to-pointer-cast</code> is enabled by default.</p>
<dt><code>-Wno-pointer-to-int-cast</code> (C and Objective-C only)</p>
<dd>Suppress warnings from casts from a pointer to an integer type of a different size.</p>
<dt><code>-Winvalid-pch</code></p>
<dd>Warn if a precompiled header is found in the search path but can&#8217;t be used.</p>
<dt><code>-Wlong-long</code></p>
<dd>Warn if <code>long long</code> type is used. This is enabled by either <code>-Wpedantic</code> or <code>-Wtraditional</code> in <font SIZE="-1">ISO C90</font> and C<font SIZE="-2">++</font>98 modes. To inhibit the warning messages, use <code>-Wno-long-long</code>.</p>
<dt><code>-Wvariadic-macros</code></p>
<dd>Warn if variadic macros are used in pedantic <font SIZE="-1">ISO C90</font> mode, or the <font SIZE="-1">GNU</font> alternate syntax when in pedantic <font SIZE="-1">ISO C99</font> mode. This is default. To inhibit the warning messages, use <code>-Wno-variadic-macros</code>.</p>
<dt><code>-Wvarargs</code></p>
<dd>Warn upon questionable usage of the macros used to handle variable arguments like <code>va_start</code>. This is default. To inhibit the warning messages, use <code>-Wno-varargs</code>.</p>
<dt><code>-Wvector-operation-performance</code></p>
<dd>Warn if vector operation is not implemented via <font SIZE="-1">SIMD</font> capabilities of the architecture. Mainly useful for the performance tuning. Vector operation can be implemented <tt>&quot;piecewise&quot;</tt>, which means that the scalar operation is performed on every vector element; <tt>&quot;in parallel&quot;</tt>, which means that the vector operation is implemented using scalars of wider type, which normally is more performance efficient; and <tt>&quot;as a single scalar&quot;</tt>, which means that vector fits into a scalar type.</p>
<dt><code>-Wno-virtual-move-assign</code></p>
<dd>Suppress warnings about inheriting from a virtual base with a non-trivial C<font SIZE="-2">++</font>11 move assignment operator. This is dangerous because if the virtual base is reachable along more than one path, it will be moved multiple times, which can mean both objects end up in the moved-from state. If the move assignment operator is written to avoid moving from a moved-from object, this warning can be disabled.</p>
<dt><code>-Wvla</code></p>
<dd>Warn if variable length array is used in the code. <code>-Wno-vla</code> prevents the <code>-Wpedantic</code> warning of the variable length array.</p>
<dt><code>-Wvolatile-register-var</code></p>
<dd>Warn if a register variable is declared volatile. The volatile modifier does not inhibit all optimizations that may eliminate reads and/or writes to register variables. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wdisabled-optimization</code></p>
<dd>Warn if a requested optimization pass is disabled. This warning does not generally indicate that there is anything wrong with your code; it merely indicates that <font SIZE="-1">GCC</font>&#8216;s optimizers are unable to handle the code effectively. Often, the problem is that your code is too big or too complex; <font SIZE="-1">GCC</font> refuses to optimize programs when the optimization itself is likely to take inordinate amounts of time.</p>
<dt><code>-Wpointer-sign</code> (C and Objective-C only)</p>
<dd>Warn for pointer argument passing or assignment with different signedness. This option is only supported for C and Objective-C. It is implied by <code>-Wall</code> and by <code>-Wpedantic</code>, which can be disabled with <code>-Wno-pointer-sign</code>.</p>
<dt><code>-Wstack-protector</code></p>
<dd>This option is only active when <code>-fstack-protector</code> is active. It warns about functions that are not protected against stack smashing.</p>
<dt><code>-Woverlength-strings</code></p>
<dd>Warn about string constants that are longer than the &#8220;minimum maximum&#8221; length specified in the C standard. Modern compilers generally allow string constants that are much longer than the standard&#8217;s minimum limit, but very portable programs should avoid using longer strings. </p>
<p> The limit applies <i>after</i> string constant concatenation, and does not count the trailing <font SIZE="-1">NUL. </font> In C90, the limit was 509 characters; in C99, it was raised to 4095. C<font SIZE="-2">++</font>98 does not specify a normative minimum maximum, so we do not diagnose overlength strings in C<font SIZE="-2">++</font>. </p>
<p> This option is implied by <code>-Wpedantic</code>, and can be disabled with <code>-Wno-overlength-strings</code>.</p>
<dt><code>-Wunsuffixed-float-constants</code> (C and Objective-C only)</p>
<dd>Issue a warning for any floating constant that does not have a suffix. When used together with <code>-Wsystem-headers</code> it warns about such constants in system header files. This can be useful when preparing code to use with the <tt>&quot;FLOAT_CONST_DECIMAL64&quot;</tt> pragma from the decimal floating-point extension to C99.</dl>
<h3>Options for Debugging Your Program or <font SIZE="-1">GCC</font></h3>
<p><font SIZE="-1">GCC</font> has various special options that are used for debugging either your program or <font SIZE="-1">GCC:</font></p>
<dl COMPACT>
<dt><code>-g</code></p>
<dd>Produce debugging information in the operating system&#8217;s native format (stabs, <font SIZE="-1">COFF, XCOFF,</font> or <font SIZE="-1">DWARF 2</font>). <font SIZE="-1">GDB</font> can work with this debugging information. </p>
<p> On most systems that use stabs format, <code>-g</code> enables use of extra debugging information that only <font SIZE="-1">GDB</font> can use; this extra information makes debugging work better in <font SIZE="-1">GDB</font> but probably makes other debuggers crash or refuse to read the program. If you want to control for certain whether to generate the extra information, use <code>-gstabs+</code>, <code>-gstabs</code>, <code>-gxcoff+</code>, <code>-gxcoff</code>, or <code>-gvms</code> (see below). </p>
<p> <font SIZE="-1">GCC</font> allows you to use <code>-g</code> with <code>-O</code>. The shortcuts taken by optimized code may occasionally produce surprising results: some variables you declared may not exist at all; flow of control may briefly move where you did not expect it; some statements may not be executed because they compute constant results or their values are already at hand; some statements may execute in different places because they have been moved out of loops. </p>
<p> Nevertheless it proves possible to debug optimized output. This makes it reasonable to use the optimizer for programs that might have bugs. </p>
<p> The following options are useful when <font SIZE="-1">GCC</font> is generated with the capability for more than one debugging format.</p>
<dt><code>-gsplit-dwarf</code></p>
<dd>Separate as much dwarf debugging information as possible into a separate output file with the extension .dwo. This option allows the build system to avoid linking files with debug information. To be useful, this option requires a debugger capable of reading .dwo files.</p>
<dt><code>-ggdb</code></p>
<dd>Produce debugging information for use by <font SIZE="-1">GDB. </font> This means to use the most expressive format available (<font SIZE="-1">DWARF 2,</font> stabs, or the native format if neither of those are supported), including <font SIZE="-1">GDB</font> extensions if at all possible.</p>
<dt><code>-gpubnames</code></p>
<dd>Generate dwarf .debug_pubnames and .debug_pubtypes sections.</p>
<dt><code>-ggnu-pubnames</code></p>
<dd>Generate .debug_pubnames and .debug_pubtypes sections in a format suitable for conversion into a <font SIZE="-1">GDB</font> index. This option is only useful with a linker that can produce <font SIZE="-1">GDB</font> index version 7.</p>
<dt><code>-gstabs</code></p>
<dd>Produce debugging information in stabs format (if that is supported), without <font SIZE="-1">GDB</font> extensions. This is the format used by <font SIZE="-1">DBX</font> on most <font SIZE="-1">BSD</font> systems. On <font SIZE="-1">MIPS,</font> Alpha and System V Release 4 systems this option produces stabs debugging output that is not understood by <font SIZE="-1">DBX</font> or <font SIZE="-1">SDB.</font> On System V Release 4 systems this option requires the <font SIZE="-1">GNU</font> assembler.</p>
<dt><code>-feliminate-unused-debug-symbols</code></p>
<dd>Produce debugging information in stabs format (if that is supported), for only symbols that are actually used.</p>
<dt><code>-femit-class-debug-always</code></p>
<dd>Instead of emitting debugging information for a C<font SIZE="-2">++</font> class in only one object file, emit it in all object files using the class. This option should be used only with debuggers that are unable to handle the way <font SIZE="-1">GCC</font> normally emits debugging information for classes because using this option increases the size of debugging information by as much as a factor of two.</p>
<dt><code>-fdebug-types-section</code></p>
<dd>When using <font SIZE="-1">DWARF</font> Version 4 or higher, type DIEs can be put into their own <tt>&quot;.debug_types&quot;</tt> section instead of making them part of the <tt>&quot;.debug_info&quot;</tt> section. It is more efficient to put them in a separate comdat sections since the linker can then remove duplicates. But not all <font SIZE="-1">DWARF</font> consumers support <tt>&quot;.debug_types&quot;</tt> sections yet and on some objects <tt>&quot;.debug_types&quot;</tt> produces larger instead of smaller debugging information.</p>
<dt><code>-gstabs+</code></p>
<dd>Produce debugging information in stabs format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program.</p>
<dt><code>-gcoff</code></p>
<dd>Produce debugging information in <font SIZE="-1">COFF</font> format (if that is supported). This is the format used by <font SIZE="-1">SDB</font> on most System V systems prior to System V Release 4.</p>
<dt><code>-gxcoff</code></p>
<dd>Produce debugging information in <font SIZE="-1">XCOFF</font> format (if that is supported). This is the format used by the <font SIZE="-1">DBX</font> debugger on <font SIZE="-1">IBM RS/6000</font> systems.</p>
<dt><code>-gxcoff+</code></p>
<dd>Produce debugging information in <font SIZE="-1">XCOFF</font> format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program, and may cause assemblers other than the <font SIZE="-1">GNU</font> assembler (<font SIZE="-1">GAS</font>) to fail with an error.</p>
<dt><code>-gdwarf-</code><i>version</i></p>
<dd>Produce debugging information in <font SIZE="-1">DWARF</font> format (if that is supported). The value of <i>version</i> may be either 2, 3 or 4; the default version for most targets is 4. </p>
<p> Note that with <font SIZE="-1">DWARF</font> Version 2, some ports require and always use some non-conflicting <font SIZE="-1">DWARF 3</font> extensions in the unwind tables. </p>
<p> Version 4 may require <font SIZE="-1">GDB 7.0</font> and <code>-fvar-tracking-assignments</code> for maximum benefit.</p>
<dt><code>-grecord-gcc-switches</code></p>
<dd>This switch causes the command-line options used to invoke the compiler that may affect code generation to be appended to the DW_AT_producer attribute in <font SIZE="-1">DWARF</font> debugging information. The options are concatenated with spaces separating them from each other and from the compiler version. See also <code>-frecord-gcc-switches</code> for another way of storing compiler options into the object file. This is the default.</p>
<dt><code>-gno-record-gcc-switches</code></p>
<dd>Disallow appending command-line options to the DW_AT_producer attribute in <font SIZE="-1">DWARF</font> debugging information.</p>
<dt><code>-gstrict-dwarf</code></p>
<dd>Disallow using extensions of later <font SIZE="-1">DWARF</font> standard version than selected with <code>-gdwarf-</code><i>version</i>. On most targets using non-conflicting <font SIZE="-1">DWARF</font> extensions from later standard versions is allowed.</p>
<dt><code>-gno-strict-dwarf</code></p>
<dd>Allow using extensions of later <font SIZE="-1">DWARF</font> standard version than selected with <code>-gdwarf-</code><i>version</i>.</p>
<dt><code>-gvms</code></p>
<dd>Produce debugging information in Alpha/VMS debug format (if that is supported). This is the format used by <font SIZE="-1">DEBUG</font> on Alpha/VMS systems.</p>
<dt><code>-g</code><i>level</i></p>
<dd>
<dt><code>-ggdb</code><i>level</i></p>
<dd>
<dt><code>-gstabs</code><i>level</i></p>
<dd>
<dt><code>-gcoff</code><i>level</i></p>
<dd>
<dt><code>-gxcoff</code><i>level</i></p>
<dd>
<dt><code>-gvms</code><i>level</i></p>
<dd>Request debugging information and also use <i>level</i> to specify how much information. The default level is 2. </p>
<p> Level 0 produces no debug information at all. Thus, <code>-g0</code> negates <code>-g</code>. </p>
<p> Level 1 produces minimal information, enough for making backtraces in parts of the program that you don&#8217;t plan to debug. This includes descriptions of functions and external variables, and line number tables, but no information about local variables. </p>
<p> Level 3 includes extra information, such as all the macro definitions present in the program. Some debuggers support macro expansion when you use <code>-g3</code>. </p>
<p> <code>-gdwarf-2</code> does not accept a concatenated debug level, because <font SIZE="-1">GCC</font> used to support an option <code>-gdwarf</code> that meant to generate debug information in version 1 of the <font SIZE="-1">DWARF</font> format (which is very different from version 2), and it would have been too confusing. That debug format is long obsolete, but the option cannot be changed now. Instead use an additional <code>-g</code><i>level</i> option to change the debug level for <font SIZE="-1">DWARF.</font></p>
<dt><code>-gtoggle</code></p>
<dd>Turn off generation of debug info, if leaving out this option generates it, or turn it on at level 2 otherwise. The position of this argument in the command line does not matter; it takes effect after all other options are processed, and it does so only once, no matter how many times it is given. This is mainly intended to be used with <code>-fcompare-debug</code>.</p>
<dt><code>-fsanitize=address</code></p>
<dd>Enable AddressSanitizer, a fast memory error detector. Memory access instructions will be instrumented to detect out-of-bounds and use-after-free bugs. See &lt;<code><a rel="nofollow" href="http://code.google.com/p/address-sanitizer/">http://code.google.com/p/address-sanitizer/</a></code>&gt; for more details. The run-time behavior can be influenced using the <font SIZE="-1"><code>ASAN_OPTIONS</code></font> environment variable; see &lt;<code><a rel="nofollow" href="https://code.google.com/p/address-sanitizer/wiki/Flags#Run-time_flags">https://code.google.com/p/address-sanitizer/wiki/Flags#Run-time_flags</a></code>&gt; for a list of supported options.</p>
<dt><code>-fsanitize=kernel-address</code></p>
<dd>Enable AddressSanitizer for Linux kernel. See &lt;<code><a rel="nofollow" href="http://code.google.com/p/address-sanitizer/wiki/AddressSanitizerForKernel">http://code.google.com/p/address-sanitizer/wiki/AddressSanitizerForKernel</a></code>&gt; for more details.</p>
<dt><code>-fsanitize=thread</code></p>
<dd>Enable ThreadSanitizer, a fast data race detector. Memory access instructions will be instrumented to detect data race bugs. See &lt;<code><a rel="nofollow" href="http://code.google.com/p/thread-sanitizer/">http://code.google.com/p/thread-sanitizer/</a></code>&gt; for more details. The run-time behavior can be influenced using the <font SIZE="-1"><code>TSAN_OPTIONS</code></font> environment variable; see &lt;<code><a rel="nofollow" href="https://code.google.com/p/thread-sanitizer/wiki/Flags">https://code.google.com/p/thread-sanitizer/wiki/Flags</a></code>&gt; for a list of supported options.</p>
<dt><code>-fsanitize=leak</code></p>
<dd>Enable LeakSanitizer, a memory leak detector. This option only matters for linking of executables and if neither <code>-fsanitize=address</code> nor <code>-fsanitize=thread</code> is used. In that case it will link the executable against a library that overrides <tt>&quot;malloc&quot;</tt> and other allocator functions. See &lt;<code><a rel="nofollow" href="https://code.google.com/p/address-sanitizer/wiki/LeakSanitizer">https://code.google.com/p/address-sanitizer/wiki/LeakSanitizer</a></code>&gt; for more details. The run-time behavior can be influenced using the <font SIZE="-1"><code>LSAN_OPTIONS</code></font> environment variable.</p>
<dt><code>-fsanitize=undefined</code></p>
<dd>Enable UndefinedBehaviorSanitizer, a fast undefined behavior detector. Various computations will be instrumented to detect undefined behavior at runtime. Current suboptions are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-fsanitize=shift</code></p>
<dd>This option enables checking that the result of a shift operation is not undefined. Note that what exactly is considered undefined differs slightly between C and C<font SIZE="-2">++</font>, as well as between <font SIZE="-1">ISO C90</font> and C99, etc.</p>
<dt><code>-fsanitize=integer-divide-by-zero</code></p>
<dd>Detect integer division by zero as well as <tt>&quot;INT_MIN / -1&quot;</tt> division.</p>
<dt><code>-fsanitize=unreachable</code></p>
<dd>With this option, the compiler will turn the <tt>&quot;__builtin_unreachable&quot;</tt> call into a diagnostics message call instead. When reaching the <tt>&quot;__builtin_unreachable&quot;</tt> call, the behavior is undefined.</p>
<dt><code>-fsanitize=vla-bound</code></p>
<dd>This option instructs the compiler to check that the size of a variable length array is positive. This option does not have any effect in <code>-std=c++1y</code> mode, as the standard requires the exception be thrown instead.</p>
<dt><code>-fsanitize=null</code></p>
<dd>This option enables pointer checking. Particularly, the application built with this option turned on will issue an error message when it tries to dereference a <font SIZE="-1">NULL</font> pointer, or if a reference (possibly an rvalue reference) is bound to a <font SIZE="-1">NULL</font> pointer.</p>
<dt><code>-fsanitize=return</code></p>
<dd>This option enables return statement checking. Programs built with this option turned on will issue an error message when the end of a non-void function is reached without actually returning a value. This option works in C<font SIZE="-2">++</font> only.</p>
<dt><code>-fsanitize=signed-integer-overflow</code></p>
<dd>This option enables signed integer overflow checking. We check that the result of <tt>&quot;+&quot;</tt>, <tt>&quot;*&quot;</tt>, and both unary and binary <tt>&quot;-&quot;</tt> does not overflow in the signed arithmetics. Note, integer promotion rules must be taken into account. That is, the following is not an overflow: </p>
<pre> signed char a = SCHAR_MAX;
 a++;</pre>
</dl>
</dl>
<dl COMPACT>
<dd>While <code>-ftrapv</code> causes traps for signed overflows to be emitted, <code>-fsanitize=undefined</code> gives a diagnostic message. This currently works only for the C family of languages.</dl>
<dt><code>-fdump-final-insns</code>[<code>=</code><i>file</i>]</p>
<dd>Dump the final internal representation (<font SIZE="-1">RTL</font>) to <i>file</i>. If the optional argument is omitted (or if <i>file</i> is <tt>&quot;.&quot;</tt>), the name of the dump file is determined by appending <tt>&quot;.gkd&quot;</tt> to the compilation output file name.</p>
<dt><code>-fcompare-debug</code>[<code>=</code><i>opts</i>]</p>
<dd>If no error occurs during compilation, run the compiler a second time, adding <i>opts</i> and <code>-fcompare-debug-second</code> to the arguments passed to the second compilation. Dump the final internal representation in both compilations, and print an error if they differ. </p>
<p> If the equal sign is omitted, the default <code>-gtoggle</code> is used. </p>
<p> The environment variable <font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font>, if defined, non-empty and nonzero, implicitly enables <code>-fcompare-debug</code>. If <font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font> is defined to a string starting with a dash, then it is used for <i>opts</i>, otherwise the default <code>-gtoggle</code> is used. </p>
<p> <code>-fcompare-debug=</code>, with the equal sign but without <i>opts</i>, is equivalent to <code>-fno-compare-debug</code>, which disables the dumping of the final representation and the second compilation, preventing even <font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font> from taking effect. </p>
<p> To verify full coverage during <code>-fcompare-debug</code> testing, set <font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font> to say <code>-fcompare-debug-not-overridden</code>, which <font SIZE="-1">GCC</font> rejects as an invalid option in any actual compilation (rather than preprocessing, assembly or linking). To get just a warning, setting <font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font> to <code>-w%n-fcompare-debug not overridden</code> will do.</p>
<dt><code>-fcompare-debug-second</code></p>
<dd>This option is implicitly passed to the compiler for the second compilation requested by <code>-fcompare-debug</code>, along with options to silence warnings, and omitting other options that would cause side-effect compiler outputs to files or to the standard output. Dump files and preserved temporary files are renamed so as to contain the <tt>&quot;.gk&quot;</tt> additional extension during the second compilation, to avoid overwriting those generated by the first. </p>
<p> When this option is passed to the compiler driver, it causes the <i>first</i> compilation to be skipped, which makes it useful for little other than debugging the compiler proper.</p>
<dt><code>-feliminate-dwarf2-dups</code></p>
<dd>Compress <font SIZE="-1">DWARF 2</font> debugging information by eliminating duplicated information about each symbol. This option only makes sense when generating <font SIZE="-1">DWARF 2</font> debugging information with <code>-gdwarf-2</code>.</p>
<dt><code>-femit-struct-debug-baseonly</code></p>
<dd>Emit debug information for struct-like types only when the base name of the compilation source file matches the base name of file in which the struct is defined. </p>
<p> This option substantially reduces the size of debugging information, but at significant potential loss in type information to the debugger. See <code>-femit-struct-debug-reduced</code> for a less aggressive option. See <code>-femit-struct-debug-detailed</code> for more detailed control. </p>
<p> This option works only with <font SIZE="-1">DWARF 2.</font></p>
<dt><code>-femit-struct-debug-reduced</code></p>
<dd>Emit debug information for struct-like types only when the base name of the compilation source file matches the base name of file in which the type is defined, unless the struct is a template or defined in a system header. </p>
<p> This option significantly reduces the size of debugging information, with some potential loss in type information to the debugger. See <code>-femit-struct-debug-baseonly</code> for a more aggressive option. See <code>-femit-struct-debug-detailed</code> for more detailed control. </p>
<p> This option works only with <font SIZE="-1">DWARF 2.</font></p>
<dt><code>-femit-struct-debug-detailed</code>[<code>=</code><i>spec-list</i>]</p>
<dd>Specify the struct-like types for which the compiler generates debug information. The intent is to reduce duplicate struct debug information between different object files within the same program. </p>
<p> This option is a detailed version of <code>-femit-struct-debug-reduced</code> and <code>-femit-struct-debug-baseonly</code>, which serves for most needs. </p>
<p> A specification has the syntax[<code>dir:</code>|<code>ind:</code>][<code>ord:</code>|<code>gen:</code>](<code>any</code>|<code>sys</code>|<code>base</code>|<code>none</code>) </p>
<p> The optional first word limits the specification to structs that are used directly (<code>dir:</code>) or used indirectly (<code>ind:</code>). A struct type is used directly when it is the type of a variable, member. Indirect uses arise through pointers to structs. That is, when use of an incomplete struct is valid, the use is indirect. An example is <code>struct one direct; struct two * indirect;</code>. </p>
<p> The optional second word limits the specification to ordinary structs (<code>ord:</code>) or generic structs (<code>gen:</code>). Generic structs are a bit complicated to explain. For C<font SIZE="-2">++</font>, these are non-explicit specializations of template classes, or non-template classes within the above. Other programming languages have generics, but <code>-femit-struct-debug-detailed</code> does not yet implement them. </p>
<p> The third word specifies the source files for those structs for which the compiler should emit debug information. The values <code>none</code> and <code>any</code> have the normal meaning. The value <code>base</code> means that the base of name of the file in which the type declaration appears must match the base of the name of the main compilation file. In practice, this means that when compiling <i>foo.c</i>, debug information is generated for types declared in that file and <i>foo.h</i>, but not other header files. The value <code>sys</code> means those types satisfying <code>base</code> or declared in system or compiler headers. </p>
<p> You may need to experiment to determine the best settings for your application. </p>
<p> The default is <code>-femit-struct-debug-detailed=all</code>. </p>
<p> This option works only with <font SIZE="-1">DWARF 2.</font></p>
<dt><code>-fno-merge-debug-strings</code></p>
<dd>Direct the linker to not merge together strings in the debugging information that are identical in different object files. Merging is not supported by all assemblers or linkers. Merging decreases the size of the debug information in the output file at the cost of increasing link processing time. Merging is enabled by default.</p>
<dt><code>-fdebug-prefix-map=</code><i>old</i><code>=</code><i>new</i></p>
<dd>When compiling files in directory <i>old</i>, record debugging information describing them as in <i>new</i> instead.</p>
<dt><code>-fno-dwarf2-cfi-asm</code></p>
<dd>Emit <font SIZE="-1">DWARF 2</font> unwind info as compiler generated <tt>&quot;.eh_frame&quot;</tt> section instead of using <font SIZE="-1">GAS </font><tt>&quot;.cfi_*&quot;</tt> directives.</p>
<dt><code>-p</code></p>
<dd>Generate extra code to write profile information suitable for the analysis program <code>prof</code>. You must use this option when compiling the source files you want data about, and you must also use it when linking.</p>
<dt><code>-pg</code></p>
<dd>Generate extra code to write profile information suitable for the analysis program <code>gprof</code>. You must use this option when compiling the source files you want data about, and you must also use it when linking.</p>
<dt><code>-Q</code></p>
<dd>Makes the compiler print out each function name as it is compiled, and print some statistics about each pass when it finishes.</p>
<dt><code>-ftime-report</code></p>
<dd>Makes the compiler print some statistics about the time consumed by each pass when it finishes.</p>
<dt><code>-fmem-report</code></p>
<dd>Makes the compiler print some statistics about permanent memory allocation when it finishes.</p>
<dt><code>-fmem-report-wpa</code></p>
<dd>Makes the compiler print some statistics about permanent memory allocation for the <font SIZE="-1">WPA</font> phase only.</p>
<dt><code>-fpre-ipa-mem-report</code></p>
<dd>
<dt><code>-fpost-ipa-mem-report</code></p>
<dd>Makes the compiler print some statistics about permanent memory allocation before or after interprocedural optimization.</p>
<dt><code>-fprofile-report</code></p>
<dd>Makes the compiler print some statistics about consistency of the (estimated) profile and effect of individual passes.</p>
<dt><code>-fstack-usage</code></p>
<dd>Makes the compiler output stack usage information for the program, on a per-function basis. The filename for the dump is made by appending <i>.su</i> to the <i>auxname</i>. <i>auxname</i> is generated from the name of the output file, if explicitly specified and it is not an executable, otherwise it is the basename of the source file. An entry is made up of three fields:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>The name of the function.</p>
<dt>&bull;</p>
<dd>A number of bytes.</p>
<dt>&bull;</p>
<dd>One or more qualifiers: <tt>&quot;static&quot;</tt>, <tt>&quot;dynamic&quot;</tt>, <tt>&quot;bounded&quot;</tt>.</dl>
</dl>
<dl COMPACT>
<dd>The qualifier <tt>&quot;static&quot;</tt> means that the function manipulates the stack statically: a fixed number of bytes are allocated for the frame on function entry and released on function exit; no stack adjustments are otherwise made in the function. The second field is this fixed number of bytes. </p>
<p> The qualifier <tt>&quot;dynamic&quot;</tt> means that the function manipulates the stack dynamically: in addition to the static allocation described above, stack adjustments are made in the body of the function, for example to push/pop arguments around function calls. If the qualifier <tt>&quot;bounded&quot;</tt> is also present, the amount of these adjustments is bounded at compile time and the second field is an upper bound of the total amount of stack used by the function. If it is not present, the amount of these adjustments is not bounded at compile time and the second field only represents the bounded part.</dl>
<dt><code>-fprofile-arcs</code></p>
<dd>Add code so that program flow <i>arcs</i> are instrumented. During execution the program records how many times each branch and call is executed and how many times it is taken or returns. When the compiled program exits it saves this data to a file called <i>auxname.gcda</i> for each source file. The data may be used for profile-directed optimizations (<code>-fbranch-probabilities</code>), or for test coverage analysis (<code>-ftest-coverage</code>). Each object file&#8217;s <i>auxname</i> is generated from the name of the output file, if explicitly specified and it is not the final executable, otherwise it is the basename of the source file. In both cases any suffix is removed (e.g. <i>foo.gcda</i> for input file <i>dir/foo.c</i>, or <i>dir/foo.gcda</i> for output file specified as <code>-o dir/foo.o</code>).</p>
<dt><code>&#8211;coverage</code></p>
<dd>This option is used to compile and link code instrumented for coverage analysis. The option is a synonym for <code>-fprofile-arcs</code> <code>-ftest-coverage</code> (when compiling) and <code>-lgcov</code> (when linking). See the documentation for those options for more details.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Compile the source files with <code>-fprofile-arcs</code> plus optimization and code generation options. For test coverage analysis, use the additional <code>-ftest-coverage</code> option. You do not need to profile every source file in a program.</p>
<dt>&bull;</p>
<dd>Link your object files with <code>-lgcov</code> or <code>-fprofile-arcs</code> (the latter implies the former).</p>
<dt>&bull;</p>
<dd>Run the program on a representative workload to generate the arc profile information. This may be repeated any number of times. You can run concurrent instances of your program, and provided that the file system supports locking, the data files will be correctly updated. Also <tt>&quot;fork&quot;</tt> calls are detected and correctly handled (double counting will not happen).</p>
<dt>&bull;</p>
<dd>For profile-directed optimizations, compile the source files again with the same optimization and code generation options plus <code>-fbranch-probabilities</code>.</p>
<dt>&bull;</p>
<dd>For test coverage analysis, use <code>gcov</code> to produce human readable information from the <i>.gcno</i> and <i>.gcda</i> files. Refer to the <code>gcov</code> documentation for further information.</dl>
</dl>
<dl COMPACT>
<dd>With <code>-fprofile-arcs</code>, for each function of your program <font SIZE="-1">GCC</font> creates a program flow graph, then finds a spanning tree for the graph. Only arcs that are not on the spanning tree have to be instrumented: the compiler adds code to count the number of times that these arcs are executed. When an arc is the only exit or only entrance to a block, the instrumentation code can be added to the block; otherwise, a new basic block must be created to hold the instrumentation code.</dl>
<dt><code>-ftest-coverage</code></p>
<dd>Produce a notes file that the <code>gcov</code> code-coverage utility can use to show program coverage. Each source file&#8217;s note file is called <i>auxname.gcno</i>. Refer to the <code>-fprofile-arcs</code> option above for a description of <i>auxname</i> and instructions on how to generate test coverage data. Coverage data matches the source files more closely if you do not optimize.</p>
<dt><code>-fdbg-cnt-list</code></p>
<dd>Print the name and the counter upper bound for all debug counters.</p>
<dt><code>-fdbg-cnt=</code><i>counter-value-list</i></p>
<dd>Set the internal debug counter upper bound. <i>counter-value-list</i> is a comma-separated list of <i>name</i>:<i>value</i> pairs which sets the upper bound of each debug counter <i>name</i> to <i>value</i>. All debug counters have the initial upper bound of <tt>&quot;UINT_MAX&quot;</tt>; thus <tt>&quot;dbg_cnt()&quot;</tt> returns true always unless the upper bound is set by this option. For example, with <code>-fdbg-cnt=dce:10,tail_call:0</code>, <tt>&quot;dbg_cnt(dce)&quot;</tt> returns true only for first 10 invocations.</p>
<dt><code>-fenable-</code><i>kind</i><code>&#8211;</code><i>pass</i></p>
<dd>
<dt><code>-fdisable-</code><i>kind</i><code>&#8211;</code><i>pass</i><code>=</code><i>range-list</i></p>
<dd>This is a set of options that are used to explicitly disable/enable optimization passes. These options are intended for use for debugging <font SIZE="-1">GCC.</font> Compiler users should use regular options for enabling/disabling passes instead.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-fdisable-ipa-</code><i>pass</i></p>
<dd>Disable <font SIZE="-1">IPA</font> pass <i>pass</i>. <i>pass</i> is the pass name. If the same pass is statically invoked in the compiler multiple times, the pass name should be appended with a sequential number starting from 1.</p>
<dt><code>-fdisable-rtl-</code><i>pass</i></p>
<dd>
<dt><code>-fdisable-rtl-</code><i>pass</i><code>=</code><i>range-list</i></p>
<dd>Disable <font SIZE="-1">RTL</font> pass <i>pass</i>. <i>pass</i> is the pass name. If the same pass is statically invoked in the compiler multiple times, the pass name should be appended with a sequential number starting from 1. <i>range-list</i> is a comma-separated list of function ranges or assembler names. Each range is a number pair separated by a colon. The range is inclusive in both ends. If the range is trivial, the number pair can be simplified as a single number. If the function&#8217;s call graph node&#8217;s <i>uid</i> falls within one of the specified ranges, the <i>pass</i> is disabled for that function. The <i>uid</i> is shown in the function header of a dump file, and the pass names can be dumped by using option <code>-fdump-passes</code>.</p>
<dt><code>-fdisable-tree-</code><i>pass</i></p>
<dd>
<dt><code>-fdisable-tree-</code><i>pass</i><code>=</code><i>range-list</i></p>
<dd>Disable tree pass <i>pass</i>. See <code>-fdisable-rtl</code> for the description of option arguments.</p>
<dt><code>-fenable-ipa-</code><i>pass</i></p>
<dd>Enable <font SIZE="-1">IPA</font> pass <i>pass</i>. <i>pass</i> is the pass name. If the same pass is statically invoked in the compiler multiple times, the pass name should be appended with a sequential number starting from 1.</p>
<dt><code>-fenable-rtl-</code><i>pass</i></p>
<dd>
<dt><code>-fenable-rtl-</code><i>pass</i><code>=</code><i>range-list</i></p>
<dd>Enable <font SIZE="-1">RTL</font> pass <i>pass</i>. See <code>-fdisable-rtl</code> for option argument description and examples.</p>
<dt><code>-fenable-tree-</code><i>pass</i></p>
<dd>
<dt><code>-fenable-tree-</code><i>pass</i><code>=</code><i>range-list</i></p>
<dd>Enable tree pass <i>pass</i>. See <code>-fdisable-rtl</code> for the description of option arguments.</dl>
</dl>
<dl COMPACT>
<dd>Here are some examples showing uses of these options. </p>
<pre> # disable ccp1 for all functions
 -fdisable-tree-ccp1
 # disable complete unroll for function whose cgraph node uid is 1
 -fenable-tree-cunroll=1
 # disable gcse2 for functions at the following ranges [1,1],
 # [300,400], and [400,1000]
 # disable gcse2 for functions foo and foo2
 -fdisable-rtl-gcse2=foo,foo2
 # disable early inlining
 -fdisable-tree-einline
 # disable ipa inlining
 -fdisable-ipa-inline
 # enable tree full unroll
 -fenable-tree-unroll</pre>
</dl>
<dt><code>-d</code><i>letters</i></p>
<dd>
<dt><code>-fdump-rtl-</code><i>pass</i></p>
<dd>
<dt><code>-fdump-rtl-</code><i>pass</i><code>=</code><i>filename</i></p>
<dd>Says to make debugging dumps during compilation at times specified by <i>letters</i>. This is used for debugging the RTL-based passes of the compiler. The file names for most of the dumps are made by appending a pass number and a word to the <i>dumpname</i>, and the files are created in the directory of the output file. In case of <code>=</code><i>filename</i> option, the dump is output on the given file instead of the pass numbered dump files. Note that the pass number is computed statically as passes get registered into the pass manager. Thus the numbering is not related to the dynamic order of execution of passes. In particular, a pass installed by a plugin could have a number over 200 even if it executed quite early. <i>dumpname</i> is generated from the name of the output file, if explicitly specified and it is not an executable, otherwise it is the basename of the source file. These switches may have different effects when <code>-E</code> is used for preprocessing. </p>
<p> Debug dumps can be enabled with a <code>-fdump-rtl</code> switch or some <code>-d</code> option <i>letters</i>. Here are the possible letters for use in <i>pass</i> and <i>letters</i>, and their meanings:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-fdump-rtl-alignments</code></p>
<dd>Dump after branch alignments have been computed.</p>
<dt><code>-fdump-rtl-asmcons</code></p>
<dd>Dump after fixing rtl statements that have unsatisfied in/out constraints.</p>
<dt><code>-fdump-rtl-auto_inc_dec</code></p>
<dd>Dump after auto-inc-dec discovery. This pass is only run on architectures that have auto inc or auto dec instructions.</p>
<dt><code>-fdump-rtl-barriers</code></p>
<dd>Dump after cleaning up the barrier instructions.</p>
<dt><code>-fdump-rtl-bbpart</code></p>
<dd>Dump after partitioning hot and cold basic blocks.</p>
<dt><code>-fdump-rtl-bbro</code></p>
<dd>Dump after block reordering.</p>
<dt><code>-fdump-rtl-btl1</code></p>
<dd>
<dt><code>-fdump-rtl-btl2</code></p>
<dd><code>-fdump-rtl-btl1</code> and <code>-fdump-rtl-btl2</code> enable dumping after the two branch target load optimization passes.</p>
<dt><code>-fdump-rtl-bypass</code></p>
<dd>Dump after jump bypassing and control flow optimizations.</p>
<dt><code>-fdump-rtl-combine</code></p>
<dd>Dump after the <font SIZE="-1">RTL</font> instruction combination pass.</p>
<dt><code>-fdump-rtl-compgotos</code></p>
<dd>Dump after duplicating the computed gotos.</p>
<dt><code>-fdump-rtl-ce1</code></p>
<dd>
<dt><code>-fdump-rtl-ce2</code></p>
<dd>
<dt><code>-fdump-rtl-ce3</code></p>
<dd><code>-fdump-rtl-ce1</code>, <code>-fdump-rtl-ce2</code>, and <code>-fdump-rtl-ce3</code> enable dumping after the three if conversion passes.</p>
<dt><code>-fdump-rtl-cprop_hardreg</code></p>
<dd>Dump after hard register copy propagation.</p>
<dt><code>-fdump-rtl-csa</code></p>
<dd>Dump after combining stack adjustments.</p>
<dt><code>-fdump-rtl-cse1</code></p>
<dd>
<dt><code>-fdump-rtl-cse2</code></p>
<dd><code>-fdump-rtl-cse1</code> and <code>-fdump-rtl-cse2</code> enable dumping after the two common subexpression elimination passes.</p>
<dt><code>-fdump-rtl-dce</code></p>
<dd>Dump after the standalone dead code elimination passes.</p>
<dt><code>-fdump-rtl-dbr</code></p>
<dd>Dump after delayed branch scheduling.</p>
<dt><code>-fdump-rtl-dce1</code></p>
<dd>
<dt><code>-fdump-rtl-dce2</code></p>
<dd><code>-fdump-rtl-dce1</code> and <code>-fdump-rtl-dce2</code> enable dumping after the two dead store elimination passes.</p>
<dt><code>-fdump-rtl-eh</code></p>
<dd>Dump after finalization of <font SIZE="-1">EH</font> handling code.</p>
<dt><code>-fdump-rtl-eh_ranges</code></p>
<dd>Dump after conversion of <font SIZE="-1">EH</font> handling range regions.</p>
<dt><code>-fdump-rtl-expand</code></p>
<dd>Dump after <font SIZE="-1">RTL</font> generation.</p>
<dt><code>-fdump-rtl-fwprop1</code></p>
<dd>
<dt><code>-fdump-rtl-fwprop2</code></p>
<dd><code>-fdump-rtl-fwprop1</code> and <code>-fdump-rtl-fwprop2</code> enable dumping after the two forward propagation passes.</p>
<dt><code>-fdump-rtl-gcse1</code></p>
<dd>
<dt><code>-fdump-rtl-gcse2</code></p>
<dd><code>-fdump-rtl-gcse1</code> and <code>-fdump-rtl-gcse2</code> enable dumping after global common subexpression elimination.</p>
<dt><code>-fdump-rtl-init-regs</code></p>
<dd>Dump after the initialization of the registers.</p>
<dt><code>-fdump-rtl-initvals</code></p>
<dd>Dump after the computation of the initial value sets.</p>
<dt><code>-fdump-rtl-into_cfglayout</code></p>
<dd>Dump after converting to cfglayout mode.</p>
<dt><code>-fdump-rtl-ira</code></p>
<dd>Dump after iterated register allocation.</p>
<dt><code>-fdump-rtl-jump</code></p>
<dd>Dump after the second jump optimization.</p>
<dt><code>-fdump-rtl-loop2</code></p>
<dd><code>-fdump-rtl-loop2</code> enables dumping after the rtl loop optimization passes.</p>
<dt><code>-fdump-rtl-mach</code></p>
<dd>Dump after performing the machine dependent reorganization pass, if that pass exists.</p>
<dt><code>-fdump-rtl-mode_sw</code></p>
<dd>Dump after removing redundant mode switches.</p>
<dt><code>-fdump-rtl-rnreg</code></p>
<dd>Dump after register renumbering.</p>
<dt><code>-fdump-rtl-outof_cfglayout</code></p>
<dd>Dump after converting from cfglayout mode.</p>
<dt><code>-fdump-rtl-peephole2</code></p>
<dd>Dump after the peephole pass.</p>
<dt><code>-fdump-rtl-postreload</code></p>
<dd>Dump after post-reload optimizations.</p>
<dt><code>-fdump-rtl-pro_and_epilogue</code></p>
<dd>Dump after generating the function prologues and epilogues.</p>
<dt><code>-fdump-rtl-sched1</code></p>
<dd>
<dt><code>-fdump-rtl-sched2</code></p>
<dd><code>-fdump-rtl-sched1</code> and <code>-fdump-rtl-sched2</code> enable dumping after the basic block scheduling passes.</p>
<dt><code>-fdump-rtl-ree</code></p>
<dd>Dump after sign/zero extension elimination.</p>
<dt><code>-fdump-rtl-seqabstr</code></p>
<dd>Dump after common sequence discovery.</p>
<dt><code>-fdump-rtl-shorten</code></p>
<dd>Dump after shortening branches.</p>
<dt><code>-fdump-rtl-sibling</code></p>
<dd>Dump after sibling call optimizations.</p>
<dt><code>-fdump-rtl-split1</code></p>
<dd>
<dt><code>-fdump-rtl-split2</code></p>
<dd>
<dt><code>-fdump-rtl-split3</code></p>
<dd>
<dt><code>-fdump-rtl-split4</code></p>
<dd>
<dt><code>-fdump-rtl-split5</code></p>
<dd><code>-fdump-rtl-split1</code>, <code>-fdump-rtl-split2</code>, <code>-fdump-rtl-split3</code>, <code>-fdump-rtl-split4</code> and <code>-fdump-rtl-split5</code> enable dumping after five rounds of instruction splitting.</p>
<dt><code>-fdump-rtl-sms</code></p>
<dd>Dump after modulo scheduling. This pass is only run on some architectures.</p>
<dt><code>-fdump-rtl-stack</code></p>
<dd>Dump after conversion from <font SIZE="-1">GCC</font>&#8216;s &#8220;flat register file&#8221; registers to the x87&#8217;s stack-like registers. This pass is only run on x86 variants.</p>
<dt><code>-fdump-rtl-subreg1</code></p>
<dd>
<dt><code>-fdump-rtl-subreg2</code></p>
<dd><code>-fdump-rtl-subreg1</code> and <code>-fdump-rtl-subreg2</code> enable dumping after the two subreg expansion passes.</p>
<dt><code>-fdump-rtl-unshare</code></p>
<dd>Dump after all rtl has been unshared.</p>
<dt><code>-fdump-rtl-vartrack</code></p>
<dd>Dump after variable tracking.</p>
<dt><code>-fdump-rtl-vregs</code></p>
<dd>Dump after converting virtual registers to hard registers.</p>
<dt><code>-fdump-rtl-web</code></p>
<dd>Dump after live range splitting.</p>
<dt><code>-fdump-rtl-regclass</code></p>
<dd>
<dt><code>-fdump-rtl-subregs_of_mode_init</code></p>
<dd>
<dt><code>-fdump-rtl-subregs_of_mode_finish</code></p>
<dd>
<dt><code>-fdump-rtl-dfinit</code></p>
<dd>
<dt><code>-fdump-rtl-dfinish</code></p>
<dd>These dumps are defined but always produce empty files.</p>
<dt><code>-da</code></p>
<dd>
<dt><code>-fdump-rtl-all</code></p>
<dd>Produce all the dumps listed above.</p>
<dt><code>-dA</code></p>
<dd>Annotate the assembler output with miscellaneous debugging information.</p>
<dt><code>-dD</code></p>
<dd>Dump all macro definitions, at the end of preprocessing, in addition to normal output.</p>
<dt><code>-dH</code></p>
<dd>Produce a core dump whenever an error occurs.</p>
<dt><code>-dp</code></p>
<dd>Annotate the assembler output with a comment indicating which pattern and alternative is used. The length of each instruction is also printed.</p>
<dt><code>-dP</code></p>
<dd>Dump the <font SIZE="-1">RTL</font> in the assembler output as a comment before each instruction. Also turns on <code>-dp</code> annotation.</p>
<dt><code>-dx</code></p>
<dd>Just generate <font SIZE="-1">RTL</font> for a function instead of compiling it. Usually used with <code>-fdump-rtl-expand</code>.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fdump-noaddr</code></p>
<dd>When doing debugging dumps, suppress address output. This makes it more feasible to use diff on debugging dumps for compiler invocations with different compiler binaries and/or different text / bss / data / heap / stack / dso start locations.</p>
<dt><code>-fdump-unnumbered</code></p>
<dd>When doing debugging dumps, suppress instruction numbers and address output. This makes it more feasible to use diff on debugging dumps for compiler invocations with different options, in particular with and without <code>-g</code>.</p>
<dt><code>-fdump-unnumbered-links</code></p>
<dd>When doing debugging dumps (see <code>-d</code> option above), suppress instruction numbers for the links to the previous and next instructions in a sequence.</p>
<dt><code>-fdump-translation-unit</code> (C<font SIZE="-2">++</font> only)</p>
<dd>
<dt><code>-fdump-translation-unit-</code><i>options</i>(C<font SIZE="-2">++</font> only)</p>
<dd>Dump a representation of the tree structure for the entire translation unit to a file. The file name is made by appending <i>.tu</i> to the source file name, and the file is created in the same directory as the output file. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> controls the details of the dump as described for the <code>-fdump-tree</code> options.</p>
<dt><code>-fdump-class-hierarchy</code> (C<font SIZE="-2">++</font> only)</p>
<dd>
<dt><code>-fdump-class-hierarchy-</code><i>options</i>(C<font SIZE="-2">++</font> only)</p>
<dd>Dump a representation of each class&#8217;s hierarchy and virtual function table layout to a file. The file name is made by appending <i>.class</i> to the source file name, and the file is created in the same directory as the output file. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> controls the details of the dump as described for the <code>-fdump-tree</code> options.</p>
<dt><code>-fdump-ipa-</code><i>switch</i></p>
<dd>Control the dumping at various stages of inter-procedural analysis language tree to a file. The file name is generated by appending a switch specific suffix to the source file name, and the file is created in the same directory as the output file. The following dumps are possible:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>all</code></p>
<dd>Enables all inter-procedural analysis dumps.</p>
<dt><code>cgraph</code></p>
<dd>Dumps information about call-graph optimization, unused function removal, and inlining decisions.</p>
<dt><code>inline</code></p>
<dd>Dump after function inlining.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fdump-passes</code></p>
<dd>Dump the list of optimization passes that are turned on and off by the current command-line options.</p>
<dt><code>-fdump-statistics-</code><i>option</i></p>
<dd>Enable and control dumping of pass statistics in a separate file. The file name is generated by appending a suffix ending in <code>.statistics</code> to the source file name, and the file is created in the same directory as the output file. If the <code>&#8211;</code><i>option</i> form is used, <code>-stats</code> causes counters to be summed over the whole compilation unit while <code>-details</code> dumps every event as the passes generate them. The default with no option is to sum counters for each function compiled.</p>
<dt><code>-fdump-tree-</code><i>switch</i></p>
<dd>
<dt><code>-fdump-tree-</code><i>switch</i><code>&#8211;</code><i>options</i></p>
<dd>
<dt><code>-fdump-tree-</code><i>switch</i><code>&#8211;</code><i>options</i><code>=</code><i>filename</i></p>
<dd>Control the dumping at various stages of processing the intermediate language tree to a file. The file name is generated by appending a switch-specific suffix to the source file name, and the file is created in the same directory as the output file. In case of <code>=</code><i>filename</i> option, the dump is output on the given file instead of the auto named dump files. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> is a list of <code>&#8211;</code> separated options which control the details of the dump. Not all options are applicable to all dumps; those that are not meaningful are ignored. The following options are available</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>address</code></p>
<dd>Print the address of each node. Usually this is not meaningful as it changes according to the environment and source file. Its primary use is for tying up a dump file with a debug environment.</p>
<dt><code>asmname</code></p>
<dd>If <tt>&quot;DECL_ASSEMBLER_NAME&quot;</tt> has been set for a given decl, use that in the dump instead of <tt>&quot;DECL_NAME&quot;</tt>. Its primary use is ease of use working backward from mangled names in the assembly file.</p>
<dt><code>slim</code></p>
<dd>When dumping front-end intermediate representations, inhibit dumping of members of a scope or body of a function merely because that scope has been reached. Only dump such items when they are directly reachable by some other path. </p>
<p> When dumping pretty-printed trees, this option inhibits dumping the bodies of control structures. </p>
<p> When dumping <font SIZE="-1">RTL,</font> print the <font SIZE="-1">RTL</font> in slim (condensed) form instead of the default LISP-like representation.</p>
<dt><code>raw</code></p>
<dd>Print a raw representation of the tree. By default, trees are pretty-printed into a C-like representation.</p>
<dt><code>details</code></p>
<dd>Enable more detailed dumps (not honored by every dump option). Also include information from the optimization passes.</p>
<dt><code>stats</code></p>
<dd>Enable dumping various statistics about the pass (not honored by every dump option).</p>
<dt><code>blocks</code></p>
<dd>Enable showing basic block boundaries (disabled in raw dumps).</p>
<dt><code>graph</code></p>
<dd>For each of the other indicated dump files (<code>-fdump-rtl-</code><i>pass</i>), dump a representation of the control flow graph suitable for viewing with GraphViz to <i>file.passid.pass.dot</i>. Each function in the file is pretty-printed as a subgraph, so that GraphViz can render them all in a single plot. </p>
<p> This option currently only works for <font SIZE="-1">RTL</font> dumps, and the <font SIZE="-1">RTL</font> is always dumped in slim form.</p>
<dt><code>vops</code></p>
<dd>Enable showing virtual operands for every statement.</p>
<dt><code>lineno</code></p>
<dd>Enable showing line numbers for statements.</p>
<dt><code>uid</code></p>
<dd>Enable showing the unique <font SIZE="-1">ID </font>(<tt>&quot;DECL_UID&quot;</tt>) for each variable.</p>
<dt><code>verbose</code></p>
<dd>Enable showing the tree dump for each statement.</p>
<dt><code>eh</code></p>
<dd>Enable showing the <font SIZE="-1">EH</font> region number holding each statement.</p>
<dt><code>scev</code></p>
<dd>Enable showing scalar evolution analysis details.</p>
<dt><code>optimized</code></p>
<dd>Enable showing optimization information (only available in certain passes).</p>
<dt><code>missed</code></p>
<dd>Enable showing missed optimization information (only available in certain passes).</p>
<dt><code>notes</code></p>
<dd>Enable other detailed optimization information (only available in certain passes).</p>
<dt><code>=</code><i>filename</i></p>
<dd>Instead of an auto named dump file, output into the given file name. The file names <i>stdout</i> and <i>stderr</i> are treated specially and are considered already open standard streams. For example, </p>
<pre> gcc -O2 -ftree-vectorize -fdump-tree-vect-blocks=foo.dump
 -fdump-tree-pre=stderr file.c</pre>
<p>outputs vectorizer dump into <i>foo.dump</i>, while the <font SIZE="-1">PRE</font> dump is output on to <i>stderr</i>. If two conflicting dump filenames are given for the same pass, then the latter option overrides the earlier one.</p>
<dt><code>all</code></p>
<dd>Turn on all options, except <code>raw</code>, <code>slim</code>, <code>verbose</code> and <code>lineno</code>.</p>
<dt><code>optall</code></p>
<dd>Turn on all optimization options, i.e., <code>optimized</code>, <code>missed</code>, and <code>note</code>.</dl>
</dl>
<dl COMPACT>
<dd>The following tree dumps are possible:</p>
<dl COMPACT>
<dt><code>original</code></p>
<dd>Dump before any tree based optimization, to <i>file.original</i>.</p>
<dt><code>optimized</code></p>
<dd>Dump after all tree based optimization, to <i>file.optimized</i>.</p>
<dt><code>gimple</code></p>
<dd>Dump each function before and after the gimplification pass to a file. The file name is made by appending <i>.gimple</i> to the source file name.</p>
<dt><code>cfg</code></p>
<dd>Dump the control flow graph of each function to a file. The file name is made by appending <i>.cfg</i> to the source file name.</p>
<dt><code>ch</code></p>
<dd>Dump each function after copying loop headers. The file name is made by appending <i>.ch</i> to the source file name.</p>
<dt><code>ssa</code></p>
<dd>Dump <font SIZE="-1">SSA</font> related information to a file. The file name is made by appending <i>.ssa</i> to the source file name.</p>
<dt><code>alias</code></p>
<dd>Dump aliasing information for each function. The file name is made by appending <i>.alias</i> to the source file name.</p>
<dt><code>ccp</code></p>
<dd>Dump each function after <font SIZE="-1">CCP. </font> The file name is made by appending <i>.ccp</i> to the source file name.</p>
<dt><code>storeccp</code></p>
<dd>Dump each function after STORE-CCP. The file name is made by appending <i>.storeccp</i> to the source file name.</p>
<dt><code>pre</code></p>
<dd>Dump trees after partial redundancy elimination. The file name is made by appending <i>.pre</i> to the source file name.</p>
<dt><code>fre</code></p>
<dd>Dump trees after full redundancy elimination. The file name is made by appending <i>.fre</i> to the source file name.</p>
<dt><code>copyprop</code></p>
<dd>Dump trees after copy propagation. The file name is made by appending <i>.copyprop</i> to the source file name.</p>
<dt><code>store_copyprop</code></p>
<dd>Dump trees after store copy-propagation. The file name is made by appending <i>.store_copyprop</i> to the source file name.</p>
<dt><code>dce</code></p>
<dd>Dump each function after dead code elimination. The file name is made by appending <i>.dce</i> to the source file name.</p>
<dt><code>sra</code></p>
<dd>Dump each function after performing scalar replacement of aggregates. The file name is made by appending <i>.sra</i> to the source file name.</p>
<dt><code>sink</code></p>
<dd>Dump each function after performing code sinking. The file name is made by appending <i>.sink</i> to the source file name.</p>
<dt><code>dom</code></p>
<dd>Dump each function after applying dominator tree optimizations. The file name is made by appending <i>.dom</i> to the source file name.</p>
<dt><code>dse</code></p>
<dd>Dump each function after applying dead store elimination. The file name is made by appending <i>.dse</i> to the source file name.</p>
<dt><code>phiopt</code></p>
<dd>Dump each function after optimizing <font SIZE="-1">PHI</font> nodes into straightline code. The file name is made by appending <i>.phiopt</i> to the source file name.</p>
<dt><code>forwprop</code></p>
<dd>Dump each function after forward propagating single use variables. The file name is made by appending <i>.forwprop</i> to the source file name.</p>
<dt><code>copyrename</code></p>
<dd>Dump each function after applying the copy rename optimization. The file name is made by appending <i>.copyrename</i> to the source file name.</p>
<dt><code>nrv</code></p>
<dd>Dump each function after applying the named return value optimization on generic trees. The file name is made by appending <i>.nrv</i> to the source file name.</p>
<dt><code>vect</code></p>
<dd>Dump each function after applying vectorization of loops. The file name is made by appending <i>.vect</i> to the source file name.</p>
<dt><code>slp</code></p>
<dd>Dump each function after applying vectorization of basic blocks. The file name is made by appending <i>.slp</i> to the source file name.</p>
<dt><code>vrp</code></p>
<dd>Dump each function after Value Range Propagation (<font SIZE="-1">VRP</font>). The file name is made by appending <i>.vrp</i> to the source file name.</p>
<dt><code>all</code></p>
<dd>Enable all the available tree dumps with the flags provided in this option.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fopt-info</code></p>
<dd>
<dt><code>-fopt-info-</code><i>options</i></p>
<dd>
<dt><code>-fopt-info-</code><i>options</i><code>=</code><i>filename</i></p>
<dd>Controls optimization dumps from various optimization passes. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> is a list of <code>&#8211;</code> separated options to select the dump details and optimizations. If <i>options</i> is not specified, it defaults to <code>optimized</code> for details and <code>optall</code> for optimization groups. If the <i>filename</i> is not specified, it defaults to <i>stderr</i>. Note that the output <i>filename</i> will be overwritten in case of multiple translation units. If a combined output from multiple translation units is desired, <i>stderr</i> should be used instead. </p>
<p> The options can be divided into two groups, 1) options describing the verbosity of the dump, and 2) options describing which optimizations should be included. The options from both the groups can be freely mixed as they are non-overlapping. However, in case of any conflicts, the latter options override the earlier options on the command line. Though multiple -fopt-info options are accepted, only one of them can have <code>=filename</code>. If other filenames are provided then all but the first one are ignored. </p>
<p> The dump verbosity has the following options</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>optimized</code></p>
<dd>Print information when an optimization is successfully applied. It is up to a pass to decide which information is relevant. For example, the vectorizer passes print the source location of loops which got successfully vectorized.</p>
<dt><code>missed</code></p>
<dd>Print information about missed optimizations. Individual passes control which information to include in the output. For example, </p>
<pre> gcc -O2 -ftree-vectorize -fopt-info-vec-missed</pre>
<p>will print information about missed optimization opportunities from vectorization passes on stderr.</p>
<dt><code>note</code></p>
<dd>Print verbose information about optimizations, such as certain transformations, more detailed messages about decisions etc.</p>
<dt><code>all</code></p>
<dd>Print detailed optimization information. This includes <i>optimized</i>, <i>missed</i>, and <i>note</i>.</dl>
</dl>
<dl COMPACT>
<dd>The second set of options describes a group of optimizations and may include one or more of the following.</p>
<dl COMPACT>
<dt><code>ipa</code></p>
<dd>Enable dumps from all interprocedural optimizations.</p>
<dt><code>loop</code></p>
<dd>Enable dumps from all loop optimizations.</p>
<dt><code>inline</code></p>
<dd>Enable dumps from all inlining optimizations.</p>
<dt><code>vec</code></p>
<dd>Enable dumps from all vectorization optimizations.</p>
<dt><code>optall</code></p>
<dd>Enable dumps from all optimizations. This is a superset of the optimization groups listed above.</dl>
</dl>
<dl COMPACT>
<dd>For example, </p>
<pre> gcc -O3 -fopt-info-missed=missed.all</pre>
<p>outputs missed optimization report from all the passes into <i>missed.all</i>. </p>
<p> As another example, </p>
<pre> gcc -O3 -fopt-info-inline-optimized-missed=inline.txt</pre>
<p>will output information about missed optimizations as well as optimized locations from all the inlining passes into <i>inline.txt</i>. </p>
<p> If the <i>filename</i> is provided, then the dumps from all the applicable optimizations are concatenated into the <i>filename</i>. Otherwise the dump is output onto <i>stderr</i>. If <i>options</i> is omitted, it defaults to <code>all-optall</code>, which means dump all available optimization info from all the passes. In the following example, all optimization info is output on to <i>stderr</i>. </p>
<pre> gcc -O3 -fopt-info</pre>
<p>Note that <code>-fopt-info-vec-missed</code> behaves the same as <code>-fopt-info-missed-vec</code>. </p>
<p> As another example, consider </p>
<pre> gcc -fopt-info-vec-missed=vec.miss -fopt-info-loop-optimized=loop.opt</pre>
<p>Here the two output filenames <i>vec.miss</i> and <i>loop.opt</i> are in conflict since only one output file is allowed. In this case, only the first option takes effect and the subsequent options are ignored. Thus only the <i>vec.miss</i> is produced which contains dumps from the vectorizer about missed opportunities.</dl>
<dt><code>-frandom-seed=</code><i>string</i></p>
<dd>This option provides a seed that <font SIZE="-1">GCC</font> uses in place of random numbers in generating certain symbol names that have to be different in every compiled file. It is also used to place unique stamps in coverage data files and the object files that produce them. You can use the <code>-frandom-seed</code> option to produce reproducibly identical object files. </p>
<p> The <i>string</i> should be different for every file you compile.</p>
<dt><code>-fsched-verbose=</code><i>n</i></p>
<dd>On targets that use instruction scheduling, this option controls the amount of debugging output the scheduler prints. This information is written to standard error, unless <code>-fdump-rtl-sched1</code> or <code>-fdump-rtl-sched2</code> is specified, in which case it is output to the usual dump listing file, <i>.sched1</i> or <i>.sched2</i> respectively. However for <i>n</i> greater than nine, the output is always printed to standard error. </p>
<p> For <i>n</i> greater than zero, <code>-fsched-verbose</code> outputs the same information as <code>-fdump-rtl-sched1</code> and <code>-fdump-rtl-sched2</code>. For <i>n</i> greater than one, it also output basic block probabilities, detailed ready list information and unit/insn info. For <i>n</i> greater than two, it includes <font SIZE="-1">RTL</font> at abort point, control-flow and regions info. And for <i>n</i> over four, <code>-fsched-verbose</code> also includes dependence info.</p>
<dt><code>-save-temps</code></p>
<dd>
<dt><code>-save-temps=cwd</code></p>
<dd>Store the usual &#8220;temporary&#8221; intermediate files permanently; place them in the current directory and name them based on the source file. Thus, compiling <i>foo.c</i> with <code>-c -save-temps</code> produces files <i>foo.i</i> and <i>foo.s</i>, as well as <i>foo.o</i>. This creates a preprocessed <i>foo.i</i> output file even though the compiler now normally uses an integrated preprocessor. </p>
<p> When used in combination with the <code>-x</code> command-line option, <code>-save-temps</code> is sensible enough to avoid over writing an input source file with the same extension as an intermediate file. The corresponding intermediate file may be obtained by renaming the source file before using <code>-save-temps</code>. </p>
<p> If you invoke <font SIZE="-1">GCC</font> in parallel, compiling several different source files that share a common base name in different subdirectories or the same source file compiled for multiple output destinations, it is likely that the different parallel compilers will interfere with each other, and overwrite the temporary files. For instance: </p>
<pre> gcc -save-temps -o outdir1/foo.o indir1/foo.c&amp;
 gcc -save-temps -o outdir2/foo.o indir2/foo.c&amp;</pre>
<p>may result in <i>foo.i</i> and <i>foo.o</i> being written to simultaneously by both compilers.</p>
<dt><code>-save-temps=obj</code></p>
<dd>Store the usual &#8220;temporary&#8221; intermediate files permanently. If the <code>-o</code> option is used, the temporary files are based on the object file. If the <code>-o</code> option is not used, the <code>-save-temps=obj</code> switch behaves like <code>-save-temps</code>. </p>
<p> For example: </p>
<pre> gcc -save-temps=obj -c foo.c
 gcc -save-temps=obj -c bar.c -o dir/xbar.o
 gcc -save-temps=obj foobar.c -o dir2/yfoobar</pre>
<p>creates <i>foo.i</i>, <i>foo.s</i>, <i>dir/xbar.i</i>, <i>dir/xbar.s</i>, <i>dir2/yfoobar.i</i>, <i>dir2/yfoobar.s</i>, and <i>dir2/yfoobar.o</i>.</p>
<dt><code>-time</code>[<code>=</code><i>file</i>]</p>
<dd>Report the <font SIZE="-1">CPU</font> time taken by each subprocess in the compilation sequence. For C source files, this is the compiler proper and assembler (plus the linker if linking is done). </p>
<p> Without the specification of an output file, the output looks like this: </p>
<pre> # cc1 0.12 0.01
 # as 0.00 0.01</pre>
<p>The first number on each line is the &#8220;user time&#8221;, that is time spent executing the program itself. The second number is &#8220;system time&#8221;, time spent executing operating system routines on behalf of the program. Both numbers are in seconds. </p>
<p> With the specification of an output file, the output is appended to the named file, and it looks like this: </p>
<pre> 0.12 0.01 cc1 &lt;options&gt;
 0.00 0.01 as &lt;options&gt;</pre>
<p>The &#8220;user time&#8221; and the &#8220;system time&#8221; are moved before the program name, and the options passed to the program are displayed, so that one can later tell what file was being compiled, and with which options.</p>
<dt><code>-fvar-tracking</code></p>
<dd>Run variable tracking pass. It computes where variables are stored at each position in code. Better debugging information is then generated (if the debugging information format supports this information). </p>
<p> It is enabled by default when compiling with optimization (<code>-Os</code>, <code>-O</code>, <code>-O2</code>, &#8230;), debugging information (<code>-g</code>) and the debug info format supports it.</p>
<dt><code>-fvar-tracking-assignments</code></p>
<dd>Annotate assignments to user variables early in the compilation and attempt to carry the annotations over throughout the compilation all the way to the end, in an attempt to improve debug information while optimizing. Use of <code>-gdwarf-4</code> is recommended along with it. </p>
<p> It can be enabled even if var-tracking is disabled, in which case annotations are created and maintained, but discarded at the end.</p>
<dt><code>-fvar-tracking-assignments-toggle</code></p>
<dd>Toggle <code>-fvar-tracking-assignments</code>, in the same way that <code>-gtoggle</code> toggles <code>-g</code>.</p>
<dt><code>-print-file-name=</code><i>library</i></p>
<dd>Print the full absolute name of the library file <i>library</i> that would be used when linking&#8212;and don&#8217;t do anything else. With this option, <font SIZE="-1">GCC</font> does not compile or link anything; it just prints the file name.</p>
<dt><code>-print-multi-directory</code></p>
<dd>Print the directory name corresponding to the multilib selected by any other switches present in the command line. This directory is supposed to exist in <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>.</p>
<dt><code>-print-multi-lib</code></p>
<dd>Print the mapping from multilib directory names to compiler switches that enable them. The directory name is separated from the switches by <code>;</code>, and each switch starts with an <code>@</code> instead of the <code>&#8211;</code>, without spaces between multiple switches. This is supposed to ease shell processing.</p>
<dt><code>-print-multi-os-directory</code></p>
<dd>Print the path to <font SIZE="-1">OS</font> libraries for the selected multilib, relative to some <i>lib</i> subdirectory. If <font SIZE="-1">OS</font> libraries are present in the <i>lib</i> subdirectory and no multilibs are used, this is usually just <i>.</i>, if <font SIZE="-1">OS</font> libraries are present in <i>libsuffix</i> sibling directories this prints e.g. <i>../lib64</i>, <i>../lib</i> or <i>../lib32</i>, or if <font SIZE="-1">OS</font> libraries are present in <i>lib/subdir</i> subdirectories it prints e.g. <i>amd64</i>, <i>sparcv9</i> or <i>ev6</i>.</p>
<dt><code>-print-multiarch</code></p>
<dd>Print the path to <font SIZE="-1">OS</font> libraries for the selected multiarch, relative to some <i>lib</i> subdirectory.</p>
<dt><code>-print-prog-name=</code><i>program</i></p>
<dd>Like <code>-print-file-name</code>, but searches for a program such as <code>cpp</code>.</p>
<dt><code>-print-libgcc-file-name</code></p>
<dd>Same as <code>-print-file-name=libgcc.a</code>. </p>
<p> This is useful when you use <code>-nostdlib</code> or <code>-nodefaultlibs</code> but you do want to link with <i>libgcc.a</i>. You can do: </p>
<pre> gcc -nostdlib &lt;files&gt;... `gcc -print-libgcc-file-name`</pre>
<dt><code>-print-search-dirs</code></p>
<dd>Print the name of the configured installation directory and a list of program and library directories <code>gcc</code> searches&#8212;and don&#8217;t do anything else. </p>
<p> This is useful when <code>gcc</code> prints the error message <code>installation problem, cannot exec cpp0: No such file or directory</code>. To resolve this you either need to put <i>cpp0</i> and the other compiler components where <code>gcc</code> expects to find them, or you can set the environment variable <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> to the directory where you installed them. Don&#8217;t forget the trailing <code>/</code>.</p>
<dt><code>-print-sysroot</code></p>
<dd>Print the target sysroot directory that is used during compilation. This is the target sysroot specified either at configure time or using the <code>&#8211;sysroot</code> option, possibly with an extra suffix that depends on compilation options. If no target sysroot is specified, the option prints nothing.</p>
<dt><code>-print-sysroot-headers-suffix</code></p>
<dd>Print the suffix added to the target sysroot when searching for headers, or give an error if the compiler is not configured with such a suffix&#8212;and don&#8217;t do anything else.</p>
<dt><code>-dumpmachine</code></p>
<dd>Print the compiler&#8217;s target machine (for example, <code>i686-pc-linux-gnu</code>)&#8212;and don&#8217;t do anything else.</p>
<dt><code>-dumpversion</code></p>
<dd>Print the compiler version (for example, <code>3.0</code>)&#8212;and don&#8217;t do anything else.</p>
<dt><code>-dumpspecs</code></p>
<dd>Print the compiler&#8217;s built-in specs&#8212;and don&#8217;t do anything else. (This is used when <font SIZE="-1">GCC</font> itself is being built.)</p>
<dt><code>-fno-eliminate-unused-debug-types</code></p>
<dd>Normally, when producing <font SIZE="-1">DWARF 2</font> output, <font SIZE="-1">GCC</font> avoids producing debug symbol output for types that are nowhere used in the source file being compiled. Sometimes it is useful to have <font SIZE="-1">GCC</font> emit debugging information for all types declared in a compilation unit, regardless of whether or not they are actually used in that compilation unit, for example if, in the debugger, you want to cast a value to a type that is not actually used in your program (but is declared). More often, however, this results in a significant amount of wasted space.</dl>
<h3>Options That Control Optimization</h3>
<p>These options control various sorts of optimizations. </p>
<p> Without any optimization option, the compiler&#8217;s goal is to reduce the cost of compilation and to make debugging produce the expected results. Statements are independent: if you stop the program with a breakpoint between statements, you can then assign a new value to any variable or change the program counter to any other statement in the function and get exactly the results you expect from the source code. </p>
<p> Turning on optimization flags makes the compiler attempt to improve the performance and/or code size at the expense of compilation time and possibly the ability to debug the program. </p>
<p> The compiler performs optimization based on the knowledge it has of the program. Compiling multiple files at once to a single output file mode allows the compiler to use information gained from all of the files when compiling each of them. </p>
<p> Not all optimizations are controlled directly by a flag. Only optimizations that have a flag are listed in this section. </p>
<p> Most optimizations are only enabled if an <code>-O</code> level is set on the command line. Otherwise they are disabled, even if individual optimization flags are specified. </p>
<p> Depending on the target and how <font SIZE="-1">GCC</font> was configured, a slightly different set of optimizations may be enabled at each <code>-O</code> level than those listed here. You can invoke <font SIZE="-1">GCC</font> with <code>-Q &#8211;help=optimizers</code> to find out the exact set of optimizations that are enabled at each level.</p>
<dl COMPACT>
<dt><code>-O</code></p>
<dd>
<dt><code>-O1</code></p>
<dd>Optimize. Optimizing compilation takes somewhat more time, and a lot more memory for a large function. </p>
<p> With <code>-O</code>, the compiler tries to reduce code size and execution time, without performing any optimizations that take a great deal of compilation time. </p>
<p> <code>-O</code> turns on the following optimization flags: </p>
<p> <code>-fauto-inc-dec -fcompare-elim -fcprop-registers -fdce -fdefer-pop -fdelayed-branch -fdse -fguess-branch-probability -fif-conversion2 -fif-conversion -fipa-pure-const -fipa-profile -fipa-reference -fmerge-constants -fsplit-wide-types -ftree-bit-ccp -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-copyrename -ftree-dce -ftree-dominator-opts -ftree-dse -ftree-forwprop -ftree-fre -ftree-phiprop -ftree-slsr -ftree-sra -ftree-pta -ftree-ter -funit-at-a-time</code> </p>
<p> <code>-O</code> also turns on <code>-fomit-frame-pointer</code> on machines where doing so does not interfere with debugging.</p>
<dt><code>-O2</code></p>
<dd>Optimize even more. <font SIZE="-1">GCC</font> performs nearly all supported optimizations that do not involve a space-speed tradeoff. As compared to <code>-O</code>, this option increases both compilation time and the performance of the generated code. </p>
<p> <code>-O2</code> turns on all optimization flags specified by <code>-O</code>. It also turns on the following optimization flags: <code>-fthread-jumps -falign-functions -falign-jumps -falign-loops -falign-labels -fcaller-saves -fcrossjumping -fcse-follow-jumps -fcse-skip-blocks -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively -fexpensive-optimizations -fgcse -fgcse-lm -fhoist-adjacent-loads -finline-small-functions -findirect-inlining -fipa-sra -fisolate-erroneous-paths-dereference -foptimize-sibling-calls -fpartial-inlining -fpeephole2 -freorder-blocks -freorder-functions -frerun-cse-after-loop -fsched-interblock -fsched-spec -fschedule-insns -fschedule-insns2 -fstrict-aliasing -fstrict-overflow -ftree-switch-conversion -ftree-tail-merge -ftree-pre -ftree-vrp</code> </p>
<p> Please note the warning under <code>-fgcse</code> about invoking <code>-O2</code> on programs that use computed gotos.</p>
<dt><code>-O3</code></p>
<dd>Optimize yet more. <code>-O3</code> turns on all optimizations specified by <code>-O2</code> and also turns on the <code>-finline-functions</code>, <code>-funswitch-loops</code>, <code>-fpredictive-commoning</code>, <code>-fgcse-after-reload</code>, <code>-ftree-loop-vectorize</code>, <code>-ftree-slp-vectorize</code>, <code>-fvect-cost-model</code>, <code>-ftree-partial-pre</code> and <code>-fipa-cp-clone</code> options.</p>
<dt><code>-O0</code></p>
<dd>Reduce compilation time and make debugging produce the expected results. This is the default.</p>
<dt><code>-Os</code></p>
<dd>Optimize for size. <code>-Os</code> enables all <code>-O2</code> optimizations that do not typically increase code size. It also performs further optimizations designed to reduce code size. </p>
<p> <code>-Os</code> disables the following optimization flags: <code>-falign-functions -falign-jumps -falign-loops -falign-labels -freorder-blocks -freorder-blocks-and-partition -fprefetch-loop-arrays</code></p>
<dt><code>-Ofast</code></p>
<dd>Disregard strict standards compliance. <code>-Ofast</code> enables all <code>-O3</code> optimizations. It also enables optimizations that are not valid for all standard-compliant programs. It turns on <code>-ffast-math</code> and the Fortran-specific <code>-fno-protect-parens</code> and <code>-fstack-arrays</code>.</p>
<dt><code>-Og</code></p>
<dd>Optimize debugging experience. <code>-Og</code> enables optimizations that do not interfere with debugging. It should be the optimization level of choice for the standard edit-compile-debug cycle, offering a reasonable level of optimization while maintaining fast compilation and a good debugging experience. </p>
<p> If you use multiple <code>-O</code> options, with or without level numbers, the last such option is the one that is effective.</dl>
<p> Options of the form <code>-f</code><i>flag</i> specify machine-independent flags. Most flags have both positive and negative forms; the negative form of <code>-ffoo</code> is <code>-fno-foo</code>. In the table below, only one of the forms is listed&#8212;the one you typically use. You can figure out the other form by either removing <code>no-</code> or adding it. </p>
<p> The following options control specific optimizations. They are either activated by <code>-O</code> options or are related to ones that are. You can use the following flags in the rare cases when &#8220;fine-tuning&#8221; of optimizations to be performed is desired.</p>
<dl COMPACT>
<dt><code>-fno-defer-pop</code></p>
<dd>Always pop the arguments to each function call as soon as that function returns. For machines that must pop arguments after a function call, the compiler normally lets arguments accumulate on the stack for several function calls and pops them all at once. </p>
<p> Disabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fforward-propagate</code></p>
<dd>Perform a forward propagation pass on <font SIZE="-1">RTL. </font> The pass tries to combine two instructions and checks if the result can be simplified. If loop unrolling is active, two passes are performed and the second is scheduled after loop unrolling. </p>
<p> This option is enabled by default at optimization levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-ffp-contract=</code><i>style</i></p>
<dd><code>-ffp-contract=off</code> disables floating-point expression contraction. <code>-ffp-contract=fast</code> enables floating-point expression contraction such as forming of fused multiply-add operations if the target has native support for them. <code>-ffp-contract=on</code> enables floating-point expression contraction if allowed by the language standard. This is currently not implemented and treated equal to <code>-ffp-contract=off</code>. </p>
<p> The default is <code>-ffp-contract=fast</code>.</p>
<dt><code>-fomit-frame-pointer</code></p>
<dd>Don&#8217;t keep the frame pointer in a register for functions that don&#8217;t need one. This avoids the instructions to save, set up and restore frame pointers; it also makes an extra register available in many functions. <code>It also makes debugging impossible on some machines.</code> </p>
<p> On some machines, such as the <font SIZE="-1">VAX,</font> this flag has no effect, because the standard calling sequence automatically handles the frame pointer and nothing is saved by pretending it doesn&#8217;t exist. The machine-description macro <tt>&quot;FRAME_POINTER_REQUIRED&quot;</tt> controls whether a target machine supports this flag. </p>
<p> Starting with <font SIZE="-1">GCC</font> version 4.6, the default setting (when not optimizing for size) for 32-bit GNU/Linux x86 and 32-bit Darwin x86 targets has been changed to <code>-fomit-frame-pointer</code>. The default can be reverted to <code>-fno-omit-frame-pointer</code> by configuring <font SIZE="-1">GCC</font> with the <code>&#8211;enable-frame-pointer</code> configure option. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-foptimize-sibling-calls</code></p>
<dd>Optimize sibling and tail recursive calls. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-inline</code></p>
<dd>Do not expand any functions inline apart from those marked with the <tt>&quot;always_inline&quot;</tt> attribute. This is the default when not optimizing. </p>
<p> Single functions can be exempted from inlining by marking them with the <tt>&quot;noinline&quot;</tt> attribute.</p>
<dt><code>-finline-small-functions</code></p>
<dd>Integrate functions into their callers when their body is smaller than expected function call code (so overall size of program gets smaller). The compiler heuristically decides which functions are simple enough to be worth integrating in this way. This inlining applies to all functions, even those not declared inline. </p>
<p> Enabled at level <code>-O2</code>.</p>
<dt><code>-findirect-inlining</code></p>
<dd>Inline also indirect calls that are discovered to be known at compile time thanks to previous inlining. This option has any effect only when inlining itself is turned on by the <code>-finline-functions</code> or <code>-finline-small-functions</code> options. </p>
<p> Enabled at level <code>-O2</code>.</p>
<dt><code>-finline-functions</code></p>
<dd>Consider all functions for inlining, even if they are not declared inline. The compiler heuristically decides which functions are worth integrating in this way. </p>
<p> If all calls to a given function are integrated, and the function is declared <tt>&quot;static&quot;</tt>, then the function is normally not output as assembler code in its own right. </p>
<p> Enabled at level <code>-O3</code>.</p>
<dt><code>-finline-functions-called-once</code></p>
<dd>Consider all <tt>&quot;static&quot;</tt> functions called once for inlining into their caller even if they are not marked <tt>&quot;inline&quot;</tt>. If a call to a given function is integrated, then the function is not output as assembler code in its own right. </p>
<p> Enabled at levels <code>-O1</code>, <code>-O2</code>, <code>-O3</code> and <code>-Os</code>.</p>
<dt><code>-fearly-inlining</code></p>
<dd>Inline functions marked by <tt>&quot;always_inline&quot;</tt> and functions whose body seems smaller than the function call overhead early before doing <code>-fprofile-generate</code> instrumentation and real inlining pass. Doing so makes profiling significantly cheaper and usually inlining faster on programs having large chains of nested wrapper functions. </p>
<p> Enabled by default.</p>
<dt><code>-fipa-sra</code></p>
<dd>Perform interprocedural scalar replacement of aggregates, removal of unused parameters and replacement of parameters passed by reference by parameters passed by value. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code> and <code>-Os</code>.</p>
<dt><code>-finline-limit=</code><i>n</i></p>
<dd>By default, <font SIZE="-1">GCC</font> limits the size of functions that can be inlined. This flag allows coarse control of this limit. <i>n</i> is the size of functions that can be inlined in number of pseudo instructions. </p>
<p> Inlining is actually controlled by a number of parameters, which may be specified individually by using <code>&#8211;param</code> <i>name</i><code>=</code><i>value</i>. The <code>-finline-limit=</code><i>n</i> option sets some of these parameters as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>max-inline-insns-single</code></p>
<dd>is set to <i>n</i>/2.</p>
<dt><code>max-inline-insns-auto</code></p>
<dd>is set to <i>n</i>/2.</dl>
</dl>
<dl COMPACT>
<dd>See below for a documentation of the individual parameters controlling inlining and for the defaults of these parameters. </p>
<p> <i>Note:</i> there may be no value to <code>-finline-limit</code> that results in default behavior. </p>
<p> <i>Note:</i> pseudo instruction represents, in this particular context, an abstract measurement of function&#8217;s size. In no way does it represent a count of assembly instructions and as such its exact meaning might change from one release to an another.</dl>
<dt><code>-fno-keep-inline-dllexport</code></p>
<dd>This is a more fine-grained version of <code>-fkeep-inline-functions</code>, which applies only to functions that are declared using the <tt>&quot;dllexport&quot;</tt> attribute or declspec</p>
<dt><code>-fkeep-inline-functions</code></p>
<dd>In C, emit <tt>&quot;static&quot;</tt> functions that are declared <tt>&quot;inline&quot;</tt> into the object file, even if the function has been inlined into all of its callers. This switch does not affect functions using the <tt>&quot;extern inline&quot;</tt> extension in <font SIZE="-1">GNU C90. </font> In C<font SIZE="-2">++</font>, emit any and all inline functions into the object file.</p>
<dt><code>-fkeep-static-consts</code></p>
<dd>Emit variables declared <tt>&quot;static const&quot;</tt> when optimization isn&#8217;t turned on, even if the variables aren&#8217;t referenced. </p>
<p> <font SIZE="-1">GCC</font> enables this option by default. If you want to force the compiler to check if a variable is referenced, regardless of whether or not optimization is turned on, use the <code>-fno-keep-static-consts</code> option.</p>
<dt><code>-fmerge-constants</code></p>
<dd>Attempt to merge identical constants (string constants and floating-point constants) across compilation units. </p>
<p> This option is the default for optimized compilation if the assembler and linker support it. Use <code>-fno-merge-constants</code> to inhibit this behavior. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fmerge-all-constants</code></p>
<dd>Attempt to merge identical constants and identical variables. </p>
<p> This option implies <code>-fmerge-constants</code>. In addition to <code>-fmerge-constants</code> this considers e.g. even constant initialized arrays or initialized constant variables with integral or floating-point types. Languages like C or C<font SIZE="-2">++</font> require each variable, including multiple instances of the same variable in recursive calls, to have distinct locations, so using this option results in non-conforming behavior.</p>
<dt><code>-fmodulo-sched</code></p>
<dd>Perform swing modulo scheduling immediately before the first scheduling pass. This pass looks at innermost loops and reorders their instructions by overlapping different iterations.</p>
<dt><code>-fmodulo-sched-allow-regmoves</code></p>
<dd>Perform more aggressive SMS-based modulo scheduling with register moves allowed. By setting this flag certain anti-dependences edges are deleted, which triggers the generation of reg-moves based on the life-range analysis. This option is effective only with <code>-fmodulo-sched</code> enabled.</p>
<dt><code>-fno-branch-count-reg</code></p>
<dd>Do not use &#8220;decrement and branch&#8221; instructions on a count register, but instead generate a sequence of instructions that decrement a register, compare it against zero, then branch based upon the result. This option is only meaningful on architectures that support such instructions, which include x86, PowerPC, <font SIZE="-1">IA-64</font> and S/390. </p>
<p> The default is <code>-fbranch-count-reg</code>.</p>
<dt><code>-fno-function-cse</code></p>
<dd>Do not put function addresses in registers; make each instruction that calls a constant function contain the function&#8217;s address explicitly. </p>
<p> This option results in less efficient code, but some strange hacks that alter the assembler output may be confused by the optimizations performed when this option is not used. </p>
<p> The default is <code>-ffunction-cse</code></p>
<dt><code>-fno-zero-initialized-in-bss</code></p>
<dd>If the target supports a <font SIZE="-1">BSS</font> section, <font SIZE="-1">GCC</font> by default puts variables that are initialized to zero into <font SIZE="-1">BSS. </font> This can save space in the resulting code. </p>
<p> This option turns off this behavior because some programs explicitly rely on variables going to the data section&#8212;e.g., so that the resulting executable can find the beginning of that section and/or make assumptions based on that. </p>
<p> The default is <code>-fzero-initialized-in-bss</code>.</p>
<dt><code>-fthread-jumps</code></p>
<dd>Perform optimizations that check to see if a jump branches to a location where another comparison subsumed by the first is found. If so, the first branch is redirected to either the destination of the second branch or a point immediately following it, depending on whether the condition is known to be true or false. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fsplit-wide-types</code></p>
<dd>When using a type that occupies multiple registers, such as <tt>&quot;long long&quot;</tt> on a 32-bit system, split the registers apart and allocate them independently. This normally generates better code for those types, but may make debugging more difficult. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fcse-follow-jumps</code></p>
<dd>In common subexpression elimination (<font SIZE="-1">CSE</font>), scan through jump instructions when the target of the jump is not reached by any other path. For example, when <font SIZE="-1">CSE</font> encounters an <tt>&quot;if&quot;</tt> statement with an <tt>&quot;else&quot;</tt> clause, <font SIZE="-1">CSE</font> follows the jump when the condition tested is false. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fcse-skip-blocks</code></p>
<dd>This is similar to <code>-fcse-follow-jumps</code>, but causes <font SIZE="-1">CSE</font> to follow jumps that conditionally skip over blocks. When <font SIZE="-1">CSE</font> encounters a simple <tt>&quot;if&quot;</tt> statement with no else clause, <code>-fcse-skip-blocks</code> causes <font SIZE="-1">CSE</font> to follow the jump around the body of the <tt>&quot;if&quot;</tt>. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-frerun-cse-after-loop</code></p>
<dd>Re-run common subexpression elimination after loop optimizations are performed. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fgcse</code></p>
<dd>Perform a global common subexpression elimination pass. This pass also performs global constant and copy propagation. </p>
<p> <i>Note:</i> When compiling a program using computed gotos, a <font SIZE="-1">GCC</font> extension, you may get better run-time performance if you disable the global common subexpression elimination pass by adding <code>-fno-gcse</code> to the command line. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fgcse-lm</code></p>
<dd>When <code>-fgcse-lm</code> is enabled, global common subexpression elimination attempts to move loads that are only killed by stores into themselves. This allows a loop containing a load/store sequence to be changed to a load outside the loop, and a copy/store within the loop. </p>
<p> Enabled by default when <code>-fgcse</code> is enabled.</p>
<dt><code>-fgcse-sm</code></p>
<dd>When <code>-fgcse-sm</code> is enabled, a store motion pass is run after global common subexpression elimination. This pass attempts to move stores out of loops. When used in conjunction with <code>-fgcse-lm</code>, loops containing a load/store sequence can be changed to a load before the loop and a store after the loop. </p>
<p> Not enabled at any optimization level.</p>
<dt><code>-fgcse-las</code></p>
<dd>When <code>-fgcse-las</code> is enabled, the global common subexpression elimination pass eliminates redundant loads that come after stores to the same memory location (both partial and full redundancies). </p>
<p> Not enabled at any optimization level.</p>
<dt><code>-fgcse-after-reload</code></p>
<dd>When <code>-fgcse-after-reload</code> is enabled, a redundant load elimination pass is performed after reload. The purpose of this pass is to clean up redundant spilling.</p>
<dt><code>-faggressive-loop-optimizations</code></p>
<dd>This option tells the loop optimizer to use language constraints to derive bounds for the number of iterations of a loop. This assumes that loop code does not invoke undefined behavior by for example causing signed integer overflows or out-of-bound array accesses. The bounds for the number of iterations of a loop are used to guide loop unrolling and peeling and loop exit test optimizations. This option is enabled by default.</p>
<dt><code>-funsafe-loop-optimizations</code></p>
<dd>This option tells the loop optimizer to assume that loop indices do not overflow, and that loops with nontrivial exit condition are not infinite. This enables a wider range of loop optimizations even if the loop optimizer itself cannot prove that these assumptions are valid. If you use <code>-Wunsafe-loop-optimizations</code>, the compiler warns you if it finds this kind of loop.</p>
<dt><code>-fcrossjumping</code></p>
<dd>Perform cross-jumping transformation. This transformation unifies equivalent code and saves code size. The resulting code may or may not perform better than without cross-jumping. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fauto-inc-dec</code></p>
<dd>Combine increments or decrements of addresses with memory accesses. This pass is always skipped on architectures that do not have instructions to support this. Enabled by default at <code>-O</code> and higher on architectures that support this.</p>
<dt><code>-fdce</code></p>
<dd>Perform dead code elimination (<font SIZE="-1">DCE</font>) on <font SIZE="-1">RTL.</font> Enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fdse</code></p>
<dd>Perform dead store elimination (<font SIZE="-1">DSE</font>) on <font SIZE="-1">RTL.</font> Enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fif-conversion</code></p>
<dd>Attempt to transform conditional jumps into branch-less equivalents. This includes use of conditional moves, min, max, set flags and abs instructions, and some tricks doable by standard arithmetics. The use of conditional execution on chips where it is available is controlled by <tt>&quot;if-conversion2&quot;</tt>. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fif-conversion2</code></p>
<dd>Use conditional execution (where available) to transform conditional jumps into branch-less equivalents. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fdeclone-ctor-dtor</code></p>
<dd>The C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> requires multiple entry points for constructors and destructors: one for a base subobject, one for a complete object, and one for a virtual destructor that calls operator delete afterwards. For a hierarchy with virtual bases, the base and complete variants are clones, which means two copies of the function. With this option, the base and complete variants are changed to be thunks that call a common implementation. </p>
<p> Enabled by <code>-Os</code>.</p>
<dt><code>-fdelete-null-pointer-checks</code></p>
<dd>Assume that programs cannot safely dereference null pointers, and that no code or data element resides there. This enables simple constant folding optimizations at all optimization levels. In addition, other optimization passes in <font SIZE="-1">GCC</font> use this flag to control global dataflow analyses that eliminate useless checks for null pointers; these assume that if a pointer is checked after it has already been dereferenced, it cannot be null. </p>
<p> Note however that in some environments this assumption is not true. Use <code>-fno-delete-null-pointer-checks</code> to disable this optimization for programs that depend on that behavior. </p>
<p> Some targets, especially embedded ones, disable this option at all levels. Otherwise it is enabled at all levels: <code>-O0</code>, <code>-O1</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>. Passes that use the information are enabled independently at different optimization levels.</p>
<dt><code>-fdevirtualize</code></p>
<dd>Attempt to convert calls to virtual functions to direct calls. This is done both within a procedure and interprocedurally as part of indirect inlining (<tt>&quot;-findirect-inlining&quot;</tt>) and interprocedural constant propagation (<code>-fipa-cp</code>). Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fdevirtualize-speculatively</code></p>
<dd>Attempt to convert calls to virtual functions to speculative direct calls. Based on the analysis of the type inheritance graph, determine for a given call the set of likely targets. If the set is small, preferably of size 1, change the call into an conditional deciding on direct and indirect call. The speculative calls enable more optimizations, such as inlining. When they seem useless after further optimization, they are converted back into original form.</p>
<dt><code>-fexpensive-optimizations</code></p>
<dd>Perform a number of minor optimizations that are relatively expensive. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-free</code></p>
<dd>Attempt to remove redundant extension instructions. This is especially helpful for the x86-64 architecture, which implicitly zero-extends in 64-bit registers after writing to their lower 32-bit half. </p>
<p> Enabled for Alpha, AArch64 and x86 at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-lifetime-dse</code></p>
<dd>In C<font SIZE="-2">++</font> the value of an object is only affected by changes within its lifetime: when the constructor begins, the object has an indeterminate value, and any changes during the lifetime of the object are dead when the object is destroyed. Normally dead store elimination will take advantage of this; if your code relies on the value of the object storage persisting beyond the lifetime of the object, you can use this flag to disable this optimization.</p>
<dt><code>-flive-range-shrinkage</code></p>
<dd>Attempt to decrease register pressure through register live range shrinkage. This is helpful for fast processors with small or moderate size register sets.</p>
<dt><code>-fira-algorithm=</code><i>algorithm</i></p>
<dd>Use the specified coloring algorithm for the integrated register allocator. The <i>algorithm</i> argument can be <code>priority</code>, which specifies Chow&#8217;s priority coloring, or <font SIZE="-1"><code>CB</code></font>, which specifies Chaitin-Briggs coloring. Chaitin-Briggs coloring is not implemented for all architectures, but for those targets that do support it, it is the default because it generates better code.</p>
<dt><code>-fira-region=</code><i>region</i></p>
<dd>Use specified regions for the integrated register allocator. The <i>region</i> argument should be one of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>all</code></p>
<dd>Use all loops as register allocation regions. This can give the best results for machines with a small and/or irregular register set.</p>
<dt><code>mixed</code></p>
<dd>Use all loops except for loops with small register pressure as the regions. This value usually gives the best results in most cases and for most architectures, and is enabled by default when compiling with optimization for speed (<code>-O</code>, <code>-O2</code>, &#8230;).</p>
<dt><code>one</code></p>
<dd>Use all functions as a single region. This typically results in the smallest code size, and is enabled by default for <code>-Os</code> or <code>-O0</code>.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fira-hoist-pressure</code></p>
<dd>Use <font SIZE="-1">IRA</font> to evaluate register pressure in the code hoisting pass for decisions to hoist expressions. This option usually results in smaller code, but it can slow the compiler down. </p>
<p> This option is enabled at level <code>-Os</code> for all targets.</p>
<dt><code>-fira-loop-pressure</code></p>
<dd>Use <font SIZE="-1">IRA</font> to evaluate register pressure in loops for decisions to move loop invariants. This option usually results in generation of faster and smaller code on machines with large register files (&gt;= 32 registers), but it can slow the compiler down. </p>
<p> This option is enabled at level <code>-O3</code> for some targets.</p>
<dt><code>-fno-ira-share-save-slots</code></p>
<dd>Disable sharing of stack slots used for saving call-used hard registers living through a call. Each hard register gets a separate stack slot, and as a result function stack frames are larger.</p>
<dt><code>-fno-ira-share-spill-slots</code></p>
<dd>Disable sharing of stack slots allocated for pseudo-registers. Each pseudo-register that does not get a hard register gets a separate stack slot, and as a result function stack frames are larger.</p>
<dt><code>-fira-verbose=</code><i>n</i></p>
<dd>Control the verbosity of the dump file for the integrated register allocator. The default value is 5. If the value <i>n</i> is greater or equal to 10, the dump output is sent to stderr using the same format as <i>n</i> minus 10.</p>
<dt><code>-fdelayed-branch</code></p>
<dd>If supported for the target machine, attempt to reorder instructions to exploit instruction slots available after delayed branch instructions. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fschedule-insns</code></p>
<dd>If supported for the target machine, attempt to reorder instructions to eliminate execution stalls due to required data being unavailable. This helps machines that have slow floating point or memory load instructions by allowing other instructions to be issued until the result of the load or floating-point instruction is required. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-fschedule-insns2</code></p>
<dd>Similar to <code>-fschedule-insns</code>, but requests an additional pass of instruction scheduling after register allocation has been done. This is especially useful on machines with a relatively small number of registers and where memory load instructions take more than one cycle. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-sched-interblock</code></p>
<dd>Don&#8217;t schedule instructions across basic blocks. This is normally enabled by default when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fno-sched-spec</code></p>
<dd>Don&#8217;t allow speculative motion of non-load instructions. This is normally enabled by default when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-pressure</code></p>
<dd>Enable register pressure sensitive insn scheduling before register allocation. This only makes sense when scheduling before register allocation is enabled, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher. Usage of this option can improve the generated code and decrease its size by preventing register pressure increase above the number of available hard registers and subsequent spills in register allocation.</p>
<dt><code>-fsched-spec-load</code></p>
<dd>Allow speculative motion of some load instructions. This only makes sense when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-spec-load-dangerous</code></p>
<dd>Allow speculative motion of more load instructions. This only makes sense when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-stalled-insns</code></p>
<dd>
<dt><code>-fsched-stalled-insns=</code><i>n</i></p>
<dd>Define how many insns (if any) can be moved prematurely from the queue of stalled insns into the ready list during the second scheduling pass. <code>-fno-sched-stalled-insns</code> means that no insns are moved prematurely, <code>-fsched-stalled-insns=0</code> means there is no limit on how many queued insns can be moved prematurely. <code>-fsched-stalled-insns</code> without a value is equivalent to <code>-fsched-stalled-insns=1</code>.</p>
<dt><code>-fsched-stalled-insns-dep</code></p>
<dd>
<dt><code>-fsched-stalled-insns-dep=</code><i>n</i></p>
<dd>Define how many insn groups (cycles) are examined for a dependency on a stalled insn that is a candidate for premature removal from the queue of stalled insns. This has an effect only during the second scheduling pass, and only if <code>-fsched-stalled-insns</code> is used. <code>-fno-sched-stalled-insns-dep</code> is equivalent to <code>-fsched-stalled-insns-dep=0</code>. <code>-fsched-stalled-insns-dep</code> without a value is equivalent to <code>-fsched-stalled-insns-dep=1</code>.</p>
<dt><code>-fsched2-use-superblocks</code></p>
<dd>When scheduling after register allocation, use superblock scheduling. This allows motion across basic block boundaries, resulting in faster schedules. This option is experimental, as not all machine descriptions used by <font SIZE="-1">GCC</font> model the <font SIZE="-1">CPU</font> closely enough to avoid unreliable results from the algorithm. </p>
<p> This only makes sense when scheduling after register allocation, i.e. with <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-group-heuristic</code></p>
<dd>Enable the group heuristic in the scheduler. This heuristic favors the instruction that belongs to a schedule group. This is enabled by default when scheduling is enabled, i.e. with <code>-fschedule-insns</code> or <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-critical-path-heuristic</code></p>
<dd>Enable the critical-path heuristic in the scheduler. This heuristic favors instructions on the critical path. This is enabled by default when scheduling is enabled, i.e. with <code>-fschedule-insns</code> or <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-spec-insn-heuristic</code></p>
<dd>Enable the speculative instruction heuristic in the scheduler. This heuristic favors speculative instructions with greater dependency weakness. This is enabled by default when scheduling is enabled, i.e. with <code>-fschedule-insns</code> or <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-rank-heuristic</code></p>
<dd>Enable the rank heuristic in the scheduler. This heuristic favors the instruction belonging to a basic block with greater size or frequency. This is enabled by default when scheduling is enabled, i.e. with <code>-fschedule-insns</code> or <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-last-insn-heuristic</code></p>
<dd>Enable the last-instruction heuristic in the scheduler. This heuristic favors the instruction that is less dependent on the last instruction scheduled. This is enabled by default when scheduling is enabled, i.e. with <code>-fschedule-insns</code> or <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-dep-count-heuristic</code></p>
<dd>Enable the dependent-count heuristic in the scheduler. This heuristic favors the instruction that has more instructions depending on it. This is enabled by default when scheduling is enabled, i.e. with <code>-fschedule-insns</code> or <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-freschedule-modulo-scheduled-loops</code></p>
<dd>Modulo scheduling is performed before traditional scheduling. If a loop is modulo scheduled, later scheduling passes may change its schedule. Use this option to control that behavior.</p>
<dt><code>-fselective-scheduling</code></p>
<dd>Schedule instructions using selective scheduling algorithm. Selective scheduling runs instead of the first scheduler pass.</p>
<dt><code>-fselective-scheduling2</code></p>
<dd>Schedule instructions using selective scheduling algorithm. Selective scheduling runs instead of the second scheduler pass.</p>
<dt><code>-fsel-sched-pipelining</code></p>
<dd>Enable software pipelining of innermost loops during selective scheduling. This option has no effect unless one of <code>-fselective-scheduling</code> or <code>-fselective-scheduling2</code> is turned on.</p>
<dt><code>-fsel-sched-pipelining-outer-loops</code></p>
<dd>When pipelining loops during selective scheduling, also pipeline outer loops. This option has no effect unless <code>-fsel-sched-pipelining</code> is turned on.</p>
<dt><code>-fshrink-wrap</code></p>
<dd>Emit function prologues only before parts of the function that need it, rather than at the top of the function. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fcaller-saves</code></p>
<dd>Enable allocation of values to registers that are clobbered by function calls, by emitting extra instructions to save and restore the registers around such calls. Such allocation is done only when it seems to result in better code. </p>
<p> This option is always enabled by default on certain machines, usually those which have no call-preserved registers to use instead. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fcombine-stack-adjustments</code></p>
<dd>Tracks stack adjustments (pushes and pops) and stack memory references and then tries to find ways to combine them. </p>
<p> Enabled by default at <code>-O1</code> and higher.</p>
<dt><code>-fconserve-stack</code></p>
<dd>Attempt to minimize stack usage. The compiler attempts to use less stack space, even if that makes the program slower. This option implies setting the <code>large-stack-frame</code> parameter to 100 and the <code>large-stack-frame-growth</code> parameter to 400.</p>
<dt><code>-ftree-reassoc</code></p>
<dd>Perform reassociation on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-pre</code></p>
<dd>Perform partial redundancy elimination (<font SIZE="-1">PRE</font>) on trees. This flag is enabled by default at <code>-O2</code> and <code>-O3</code>.</p>
<dt><code>-ftree-partial-pre</code></p>
<dd>Make partial redundancy elimination (<font SIZE="-1">PRE</font>) more aggressive. This flag is enabled by default at <code>-O3</code>.</p>
<dt><code>-ftree-forwprop</code></p>
<dd>Perform forward propagation on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-fre</code></p>
<dd>Perform full redundancy elimination (<font SIZE="-1">FRE</font>) on trees. The difference between <font SIZE="-1">FRE</font> and <font SIZE="-1">PRE</font> is that <font SIZE="-1">FRE</font> only considers expressions that are computed on all paths leading to the redundant computation. This analysis is faster than <font SIZE="-1">PRE,</font> though it exposes fewer redundancies. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-phiprop</code></p>
<dd>Perform hoisting of loads from conditional pointers on trees. This pass is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fhoist-adjacent-loads</code></p>
<dd>Speculatively hoist loads from both branches of an if-then-else if the loads are from adjacent locations in the same structure and the target architecture has a conditional move instruction. This flag is enabled by default at <code>-O2</code> and higher.</p>
<dt><code>-ftree-copy-prop</code></p>
<dd>Perform copy propagation on trees. This pass eliminates unnecessary copy operations. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fipa-pure-const</code></p>
<dd>Discover which functions are pure or constant. Enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fipa-reference</code></p>
<dd>Discover which static variables do not escape the compilation unit. Enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fipa-pta</code></p>
<dd>Perform interprocedural pointer analysis and interprocedural modification and reference analysis. This option can cause excessive memory and compile-time usage on large compilation units. It is not enabled by default at any optimization level.</p>
<dt><code>-fipa-profile</code></p>
<dd>Perform interprocedural profile propagation. The functions called only from cold functions are marked as cold. Also functions executed once (such as <tt>&quot;cold&quot;</tt>, <tt>&quot;noreturn&quot;</tt>, static constructors or destructors) are identified. Cold functions and loop less parts of functions executed once are then optimized for size. Enabled by default at <code>-O</code> and higher.</p>
<dt><code>-fipa-cp</code></p>
<dd>Perform interprocedural constant propagation. This optimization analyzes the program to determine when values passed to functions are constants and then optimizes accordingly. This optimization can substantially increase performance if the application has constants passed to functions. This flag is enabled by default at <code>-O2</code>, <code>-Os</code> and <code>-O3</code>.</p>
<dt><code>-fipa-cp-clone</code></p>
<dd>Perform function cloning to make interprocedural constant propagation stronger. When enabled, interprocedural constant propagation performs function cloning when externally visible function can be called with constant arguments. Because this optimization can create multiple copies of functions, it may significantly increase code size (see <code>&#8211;param ipcp-unit-growth=</code><i>value</i>). This flag is enabled by default at <code>-O3</code>.</p>
<dt><code>-fisolate-erroneous-paths-dereference</code></p>
<dd>Detect paths which trigger erroneous or undefined behaviour due to dereferencing a <font SIZE="-1">NULL</font> pointer. Isolate those paths from the main control flow and turn the statement with erroneous or undefined behaviour into a trap.</p>
<dt><code>-fisolate-erroneous-paths-attribute</code></p>
<dd>Detect paths which trigger erroneous or undefined behaviour due a <font SIZE="-1">NULL</font> value being used in a way which is forbidden by a <tt>&quot;returns_nonnull&quot;</tt> or <tt>&quot;nonnull&quot;</tt> attribute. Isolate those paths from the main control flow and turn the statement with erroneous or undefined behaviour into a trap. This is not currently enabled, but may be enabled by <tt>&quot;-O2&quot;</tt> in the future.</p>
<dt><code>-ftree-sink</code></p>
<dd>Perform forward store motion on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-bit-ccp</code></p>
<dd>Perform sparse conditional bit constant propagation on trees and propagate pointer alignment information. This pass only operates on local scalar variables and is enabled by default at <code>-O</code> and higher. It requires that <code>-ftree-ccp</code> is enabled.</p>
<dt><code>-ftree-ccp</code></p>
<dd>Perform sparse conditional constant propagation (<font SIZE="-1">CCP</font>) on trees. This pass only operates on local scalar variables and is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-switch-conversion</code></p>
<dd>Perform conversion of simple initializations in a switch to initializations from a scalar array. This flag is enabled by default at <code>-O2</code> and higher.</p>
<dt><code>-ftree-tail-merge</code></p>
<dd>Look for identical code sequences. When found, replace one with a jump to the other. This optimization is known as tail merging or cross jumping. This flag is enabled by default at <code>-O2</code> and higher. The compilation time in this pass can be limited using <code>max-tail-merge-comparisons</code> parameter and <code>max-tail-merge-iterations</code> parameter.</p>
<dt><code>-ftree-dce</code></p>
<dd>Perform dead code elimination (<font SIZE="-1">DCE</font>) on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-builtin-call-dce</code></p>
<dd>Perform conditional dead code elimination (<font SIZE="-1">DCE</font>) for calls to built-in functions that may set <tt>&quot;errno&quot;</tt> but are otherwise side-effect free. This flag is enabled by default at <code>-O2</code> and higher if <code>-Os</code> is not also specified.</p>
<dt><code>-ftree-dominator-opts</code></p>
<dd>Perform a variety of simple scalar cleanups (constant/copy propagation, redundancy elimination, range propagation and expression simplification) based on a dominator tree traversal. This also performs jump threading (to reduce jumps to jumps). This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-dse</code></p>
<dd>Perform dead store elimination (<font SIZE="-1">DSE</font>) on trees. A dead store is a store into a memory location that is later overwritten by another store without any intervening loads. In this case the earlier store can be deleted. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-ch</code></p>
<dd>Perform loop header copying on trees. This is beneficial since it increases effectiveness of code motion optimizations. It also saves one jump. This flag is enabled by default at <code>-O</code> and higher. It is not enabled for <code>-Os</code>, since it usually increases code size.</p>
<dt><code>-ftree-loop-optimize</code></p>
<dd>Perform loop optimizations on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-loop-linear</code></p>
<dd>Perform loop interchange transformations on tree. Same as <code>-floop-interchange</code>. To use this code transformation, <font SIZE="-1">GCC</font> has to be configured with <code>&#8211;with-ppl</code> and <code>&#8211;with-cloog</code> to enable the Graphite loop transformation infrastructure.</p>
<dt><code>-floop-interchange</code></p>
<dd>Perform loop interchange transformations on loops. Interchanging two nested loops switches the inner and outer loops. For example, given a loop like: </p>
<pre> DO J = 1, M
 DO I = 1, N
 A(J, I) = A(J, I) * C
 ENDDO
 ENDDO</pre>
<p>loop interchange transforms the loop as if it were written: </p>
<pre> DO I = 1, N
 DO J = 1, M
 A(J, I) = A(J, I) * C
 ENDDO
 ENDDO</pre>
<p>which can be beneficial when <tt>&quot;N&quot;</tt> is larger than the caches, because in Fortran, the elements of an array are stored in memory contiguously by column, and the original loop iterates over rows, potentially creating at each access a cache miss. This optimization applies to all the languages supported by <font SIZE="-1">GCC</font> and is not limited to Fortran. To use this code transformation, <font SIZE="-1">GCC</font> has to be configured with <code>&#8211;with-ppl</code> and <code>&#8211;with-cloog</code> to enable the Graphite loop transformation infrastructure.</p>
<dt><code>-floop-strip-mine</code></p>
<dd>Perform loop strip mining transformations on loops. Strip mining splits a loop into two nested loops. The outer loop has strides equal to the strip size and the inner loop has strides of the original loop within a strip. The strip length can be changed using the <code>loop-block-tile-size</code> parameter. For example, given a loop like: </p>
<pre> DO I = 1, N
 A(I) = A(I) + C
 ENDDO</pre>
<p>loop strip mining transforms the loop as if it were written: </p>
<pre> DO II = 1, N, 51
 DO I = II, min (II + 50, N)
 A(I) = A(I) + C
 ENDDO
 ENDDO</pre>
<p>This optimization applies to all the languages supported by <font SIZE="-1">GCC</font> and is not limited to Fortran. To use this code transformation, <font SIZE="-1">GCC</font> has to be configured with <code>&#8211;with-ppl</code> and <code>&#8211;with-cloog</code> to enable the Graphite loop transformation infrastructure.</p>
<dt><code>-floop-block</code></p>
<dd>Perform loop blocking transformations on loops. Blocking strip mines each loop in the loop nest such that the memory accesses of the element loops fit inside caches. The strip length can be changed using the <code>loop-block-tile-size</code> parameter. For example, given a loop like: </p>
<pre> DO I = 1, N
 DO J = 1, M
 A(J, I) = B(I) + C(J)
 ENDDO
 ENDDO</pre>
<p>loop blocking transforms the loop as if it were written: </p>
<pre> DO II = 1, N, 51
 DO JJ = 1, M, 51
 DO I = II, min (II + 50, N)
 DO J = JJ, min (JJ + 50, M)
 A(J, I) = B(I) + C(J)
 ENDDO
 ENDDO
 ENDDO
 ENDDO</pre>
<p>which can be beneficial when <tt>&quot;M&quot;</tt> is larger than the caches, because the innermost loop iterates over a smaller amount of data which can be kept in the caches. This optimization applies to all the languages supported by <font SIZE="-1">GCC</font> and is not limited to Fortran. To use this code transformation, <font SIZE="-1">GCC</font> has to be configured with <code>&#8211;with-ppl</code> and <code>&#8211;with-cloog</code> to enable the Graphite loop transformation infrastructure.</p>
<dt><code>-fgraphite-identity</code></p>
<dd>Enable the identity transformation for graphite. For every SCoP we generate the polyhedral representation and transform it back to gimple. Using <code>-fgraphite-identity</code> we can check the costs or benefits of the <font SIZE="-1">GIMPLE &#8211;</font>&gt; <font SIZE="-1">GRAPHITE &#8211;</font>&gt; <font SIZE="-1">GIMPLE</font> transformation. Some minimal optimizations are also performed by the code generator CLooG, like index splitting and dead code elimination in loops.</p>
<dt><code>-floop-nest-optimize</code></p>
<dd>Enable the <font SIZE="-1">ISL</font> based loop nest optimizer. This is a generic loop nest optimizer based on the Pluto optimization algorithms. It calculates a loop structure optimized for data-locality and parallelism. This option is experimental.</p>
<dt><code>-floop-parallelize-all</code></p>
<dd>Use the Graphite data dependence analysis to identify loops that can be parallelized. Parallelize all the loops that can be analyzed to not contain loop carried dependences without checking that it is profitable to parallelize the loops.</p>
<dt><code>-fcheck-data-deps</code></p>
<dd>Compare the results of several data dependence analyzers. This option is used for debugging the data dependence analyzers.</p>
<dt><code>-ftree-loop-if-convert</code></p>
<dd>Attempt to transform conditional jumps in the innermost loops to branch-less equivalents. The intent is to remove control-flow from the innermost loops in order to improve the ability of the vectorization pass to handle these loops. This is enabled by default if vectorization is enabled.</p>
<dt><code>-ftree-loop-if-convert-stores</code></p>
<dd>Attempt to also if-convert conditional jumps containing memory writes. This transformation can be unsafe for multi-threaded programs as it transforms conditional memory writes into unconditional memory writes. For example, </p>
<pre> for (i = 0; i &lt; N; i++)
 if (cond)
 A[i] = expr;</pre>
<p>is transformed to </p>
<pre> for (i = 0; i &lt; N; i++)
 A[i] = cond ? expr : A[i];</pre>
<p>potentially producing data races.</p>
<dt><code>-ftree-loop-distribution</code></p>
<dd>Perform loop distribution. This flag can improve cache performance on big loop bodies and allow further loop optimizations, like parallelization or vectorization, to take place. For example, the loop </p>
<pre> DO I = 1, N
 A(I) = B(I) + C
 D(I) = E(I) * F
 ENDDO</pre>
<p>is transformed to </p>
<pre> DO I = 1, N
 A(I) = B(I) + C
 ENDDO
 DO I = 1, N
 D(I) = E(I) * F
 ENDDO</pre>
<dt><code>-ftree-loop-distribute-patterns</code></p>
<dd>Perform loop distribution of patterns that can be code generated with calls to a library. This flag is enabled by default at <code>-O3</code>. </p>
<p> This pass distributes the initialization loops and generates a call to memset zero. For example, the loop </p>
<pre> DO I = 1, N
 A(I) = 0
 B(I) = A(I) + I
 ENDDO</pre>
<p>is transformed to </p>
<pre> DO I = 1, N
 A(I) = 0
 ENDDO
 DO I = 1, N
 B(I) = A(I) + I
 ENDDO</pre>
<p>and the initialization loop is transformed into a call to memset zero.</p>
<dt><code>-ftree-loop-im</code></p>
<dd>Perform loop invariant motion on trees. This pass moves only invariants that are hard to handle at <font SIZE="-1">RTL</font> level (function calls, operations that expand to nontrivial sequences of insns). With <code>-funswitch-loops</code> it also moves operands of conditions that are invariant out of the loop, so that we can use just trivial invariantness analysis in loop unswitching. The pass also includes store motion.</p>
<dt><code>-ftree-loop-ivcanon</code></p>
<dd>Create a canonical counter for number of iterations in loops for which determining number of iterations requires complicated analysis. Later optimizations then may determine the number easily. Useful especially in connection with unrolling.</p>
<dt><code>-fivopts</code></p>
<dd>Perform induction variable optimizations (strength reduction, induction variable merging and induction variable elimination) on trees.</p>
<dt><code>-ftree-parallelize-loops=n</code></p>
<dd>Parallelize loops, i.e., split their iteration space to run in n threads. This is only possible for loops whose iterations are independent and can be arbitrarily reordered. The optimization is only profitable on multiprocessor machines, for loops that are CPU-intensive, rather than constrained e.g. by memory bandwidth. This option implies <code>-pthread</code>, and thus is only supported on targets that have support for <code>-pthread</code>.</p>
<dt><code>-ftree-pta</code></p>
<dd>Perform function-local points-to analysis on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-sra</code></p>
<dd>Perform scalar replacement of aggregates. This pass replaces structure references with scalars to prevent committing structures to memory too early. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-copyrename</code></p>
<dd>Perform copy renaming on trees. This pass attempts to rename compiler temporaries to other variables at copy locations, usually resulting in variable names which more closely resemble the original variables. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-coalesce-inlined-vars</code></p>
<dd>Tell the copyrename pass (see <code>-ftree-copyrename</code>) to attempt to combine small user-defined variables too, but only if they were inlined from other functions. It is a more limited form of <code>-ftree-coalesce-vars</code>. This may harm debug information of such inlined variables, but it will keep variables of the inlined-into function apart from each other, such that they are more likely to contain the expected values in a debugging session. This was the default in <font SIZE="-1">GCC</font> versions older than 4.7.</p>
<dt><code>-ftree-coalesce-vars</code></p>
<dd>Tell the copyrename pass (see <code>-ftree-copyrename</code>) to attempt to combine small user-defined variables too, instead of just compiler temporaries. This may severely limit the ability to debug an optimized program compiled with <code>-fno-var-tracking-assignments</code>. In the negated form, this flag prevents <font SIZE="-1">SSA</font> coalescing of user variables, including inlined ones. This option is enabled by default.</p>
<dt><code>-ftree-ter</code></p>
<dd>Perform temporary expression replacement during the <font SIZE="-1">SSA-</font>&gt;normal phase. Single use/single def temporaries are replaced at their use location with their defining expression. This results in non-GIMPLE code, but gives the expanders much more complex trees to work on resulting in better <font SIZE="-1">RTL</font> generation. This is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-slsr</code></p>
<dd>Perform straight-line strength reduction on trees. This recognizes related expressions involving multiplications and replaces them by less expensive calculations when possible. This is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-vectorize</code></p>
<dd>Perform vectorization on trees. This flag enables <code>-ftree-loop-vectorize</code> and <code>-ftree-slp-vectorize</code> if not explicitly specified.</p>
<dt><code>-ftree-loop-vectorize</code></p>
<dd>Perform loop vectorization on trees. This flag is enabled by default at <code>-O3</code> and when <code>-ftree-vectorize</code> is enabled.</p>
<dt><code>-ftree-slp-vectorize</code></p>
<dd>Perform basic block vectorization on trees. This flag is enabled by default at <code>-O3</code> and when <code>-ftree-vectorize</code> is enabled.</p>
<dt><code>-fvect-cost-model=</code><i>model</i></p>
<dd>Alter the cost model used for vectorization. The <i>model</i> argument should be one of <tt>&quot;unlimited&quot;</tt>, <tt>&quot;dynamic&quot;</tt> or <tt>&quot;cheap&quot;</tt>. With the <tt>&quot;unlimited&quot;</tt> model the vectorized code-path is assumed to be profitable while with the <tt>&quot;dynamic&quot;</tt> model a runtime check will guard the vectorized code-path to enable it only for iteration counts that will likely execute faster than when executing the original scalar loop. The <tt>&quot;cheap&quot;</tt> model will disable vectorization of loops where doing so would be cost prohibitive for example due to required runtime checks for data dependence or alignment but otherwise is equal to the <tt>&quot;dynamic&quot;</tt> model. The default cost model depends on other optimization flags and is either <tt>&quot;dynamic&quot;</tt> or <tt>&quot;cheap&quot;</tt>.</p>
<dt><code>-fsimd-cost-model=</code><i>model</i></p>
<dd>Alter the cost model used for vectorization of loops marked with the OpenMP or Cilk Plus simd directive. The <i>model</i> argument should be one of <tt>&quot;unlimited&quot;</tt>, <tt>&quot;dynamic&quot;</tt>, <tt>&quot;cheap&quot;</tt>. All values of <i>model</i> have the same meaning as described in <code>-fvect-cost-model</code> and by default a cost model defined with <code>-fvect-cost-model</code> is used.</p>
<dt><code>-ftree-vrp</code></p>
<dd>Perform Value Range Propagation on trees. This is similar to the constant propagation pass, but instead of values, ranges of values are propagated. This allows the optimizers to remove unnecessary range checks like array bound checks and null pointer checks. This is enabled by default at <code>-O2</code> and higher. Null pointer check elimination is only done if <code>-fdelete-null-pointer-checks</code> is enabled.</p>
<dt><code>-ftracer</code></p>
<dd>Perform tail duplication to enlarge superblock size. This transformation simplifies the control flow of the function allowing other optimizations to do a better job.</p>
<dt><code>-funroll-loops</code></p>
<dd>Unroll loops whose number of iterations can be determined at compile time or upon entry to the loop. <code>-funroll-loops</code> implies <code>-frerun-cse-after-loop</code>. This option makes code larger, and may or may not make it run faster.</p>
<dt><code>-funroll-all-loops</code></p>
<dd>Unroll all loops, even if their number of iterations is uncertain when the loop is entered. This usually makes programs run more slowly. <code>-funroll-all-loops</code> implies the same options as <code>-funroll-loops</code>,</p>
<dt><code>-fsplit-ivs-in-unroller</code></p>
<dd>Enables expression of values of induction variables in later iterations of the unrolled loop using the value in the first iteration. This breaks long dependency chains, thus improving efficiency of the scheduling passes. </p>
<p> A combination of <code>-fweb</code> and <font SIZE="-1">CSE</font> is often sufficient to obtain the same effect. However, that is not reliable in cases where the loop body is more complicated than a single basic block. It also does not work at all on some architectures due to restrictions in the <font SIZE="-1">CSE</font> pass. </p>
<p> This optimization is enabled by default.</p>
<dt><code>-fvariable-expansion-in-unroller</code></p>
<dd>With this option, the compiler creates multiple copies of some local variables when unrolling a loop, which can result in superior code.</p>
<dt><code>-fpartial-inlining</code></p>
<dd>Inline parts of functions. This option has any effect only when inlining itself is turned on by the <code>-finline-functions</code> or <code>-finline-small-functions</code> options. </p>
<p> Enabled at level <code>-O2</code>.</p>
<dt><code>-fpredictive-commoning</code></p>
<dd>Perform predictive commoning optimization, i.e., reusing computations (especially memory loads and stores) performed in previous iterations of loops. </p>
<p> This option is enabled at level <code>-O3</code>.</p>
<dt><code>-fprefetch-loop-arrays</code></p>
<dd>If supported by the target machine, generate instructions to prefetch memory to improve the performance of loops that access large arrays. </p>
<p> This option may generate better or worse code; results are highly dependent on the structure of loops within the source code. </p>
<p> Disabled at level <code>-Os</code>.</p>
<dt><code>-fno-peephole</code></p>
<dd>
<dt><code>-fno-peephole2</code></p>
<dd>Disable any machine-specific peephole optimizations. The difference between <code>-fno-peephole</code> and <code>-fno-peephole2</code> is in how they are implemented in the compiler; some targets use one, some use the other, a few use both. </p>
<p> <code>-fpeephole</code> is enabled by default. <code>-fpeephole2</code> enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-guess-branch-probability</code></p>
<dd>Do not guess branch probabilities using heuristics. </p>
<p> <font SIZE="-1">GCC</font> uses heuristics to guess branch probabilities if they are not provided by profiling feedback (<code>-fprofile-arcs</code>). These heuristics are based on the control flow graph. If some branch probabilities are specified by <code>__builtin_expect</code>, then the heuristics are used to guess branch probabilities for the rest of the control flow graph, taking the <code>__builtin_expect</code> info into account. The interactions between the heuristics and <code>__builtin_expect</code> can be complex, and in some cases, it may be useful to disable the heuristics so that the effects of <code>__builtin_expect</code> are easier to understand. </p>
<p> The default is <code>-fguess-branch-probability</code> at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-freorder-blocks</code></p>
<dd>Reorder basic blocks in the compiled function in order to reduce number of taken branches and improve code locality. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-freorder-blocks-and-partition</code></p>
<dd>In addition to reordering basic blocks in the compiled function, in order to reduce number of taken branches, partitions hot and cold basic blocks into separate sections of the assembly and .o files, to improve paging and cache locality performance. </p>
<p> This optimization is automatically turned off in the presence of exception handling, for linkonce sections, for functions with a user-defined section attribute and on any architecture that does not support named sections. </p>
<p> Enabled for x86 at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-freorder-functions</code></p>
<dd>Reorder functions in the object file in order to improve code locality. This is implemented by using special subsections <tt>&quot;.text.hot&quot;</tt> for most frequently executed functions and <tt>&quot;.text.unlikely&quot;</tt> for unlikely executed functions. Reordering is done by the linker so object file format must support named sections and linker must place them in a reasonable way. </p>
<p> Also profile feedback must be available to make this option effective. See <code>-fprofile-arcs</code> for details. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fstrict-aliasing</code></p>
<dd>Allow the compiler to assume the strictest aliasing rules applicable to the language being compiled. For C (and C<font SIZE="-2">++</font>), this activates optimizations based on the type of expressions. In particular, an object of one type is assumed never to reside at the same address as an object of a different type, unless the types are almost the same. For example, an <tt>&quot;unsigned int&quot;</tt> can alias an <tt>&quot;int&quot;</tt>, but not a <tt>&quot;void*&quot;</tt> or a <tt>&quot;double&quot;</tt>. A character type may alias any other type. </p>
<p> Pay special attention to code like this: </p>
<pre> union a_union {
 int i;
 double d;
 };
 
 int f() {
 union a_union t;
 t.d = 3.0;
 return t.i;
 }</pre>
<p>The practice of reading from a different union member than the one most recently written to (called &#8220;type-punning&#8221;) is common. Even with <code>-fstrict-aliasing</code>, type-punning is allowed, provided the memory is accessed through the union type. So, the code above works as expected. However, this code might not: </p>
<pre> int f() {
 union a_union t;
 int* ip;
 t.d = 3.0;
 ip = &amp;t.i;
 return *ip;
 }</pre>
<p>Similarly, access by taking the address, casting the resulting pointer and dereferencing the result has undefined behavior, even if the cast uses a union type, e.g.: </p>
<pre> int f() {
 double d = 3.0;
 return ((union a_union *) &amp;d)-&gt;i;
 }</pre>
<p>The <code>-fstrict-aliasing</code> option is enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fstrict-overflow</code></p>
<dd>Allow the compiler to assume strict signed overflow rules, depending on the language being compiled. For C (and C<font SIZE="-2">++</font>) this means that overflow when doing arithmetic with signed numbers is undefined, which means that the compiler may assume that it does not happen. This permits various optimizations. For example, the compiler assumes that an expression like <tt>&quot;i + 10 &gt; i&quot;</tt> is always true for signed <tt>&quot;i&quot;</tt>. This assumption is only valid if signed overflow is undefined, as the expression is false if <tt>&quot;i + 10&quot;</tt> overflows when using twos complement arithmetic. When this option is in effect any attempt to determine whether an operation on signed numbers overflows must be written carefully to not actually involve overflow. </p>
<p> This option also allows the compiler to assume strict pointer semantics: given a pointer to an object, if adding an offset to that pointer does not produce a pointer to the same object, the addition is undefined. This permits the compiler to conclude that <tt>&quot;p + u &gt; p&quot;</tt> is always true for a pointer <tt>&quot;p&quot;</tt> and unsigned integer <tt>&quot;u&quot;</tt>. This assumption is only valid because pointer wraparound is undefined, as the expression is false if <tt>&quot;p + u&quot;</tt> overflows using twos complement arithmetic. </p>
<p> See also the <code>-fwrapv</code> option. Using <code>-fwrapv</code> means that integer signed overflow is fully defined: it wraps. When <code>-fwrapv</code> is used, there is no difference between <code>-fstrict-overflow</code> and <code>-fno-strict-overflow</code> for integers. With <code>-fwrapv</code> certain types of overflow are permitted. For example, if the compiler gets an overflow when doing arithmetic on constants, the overflowed value can still be used with <code>-fwrapv</code>, but not otherwise. </p>
<p> The <code>-fstrict-overflow</code> option is enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-falign-functions</code></p>
<dd>
<dt><code>-falign-functions=</code><i>n</i></p>
<dd>Align the start of functions to the next power-of-two greater than <i>n</i>, skipping up to <i>n</i> bytes. For instance, <code>-falign-functions=32</code> aligns functions to the next 32-byte boundary, but <code>-falign-functions=24</code> aligns to the next 32-byte boundary only if this can be done by skipping 23 bytes or less. </p>
<p> <code>-fno-align-functions</code> and <code>-falign-functions=1</code> are equivalent and mean that functions are not aligned. </p>
<p> Some assemblers only support this flag when <i>n</i> is a power of two; in that case, it is rounded up. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-falign-labels</code></p>
<dd>
<dt><code>-falign-labels=</code><i>n</i></p>
<dd>Align all branch targets to a power-of-two boundary, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. This option can easily make code slower, because it must insert dummy operations for when the branch target is reached in the usual flow of the code. </p>
<p> <code>-fno-align-labels</code> and <code>-falign-labels=1</code> are equivalent and mean that labels are not aligned. </p>
<p> If <code>-falign-loops</code> or <code>-falign-jumps</code> are applicable and are greater than this value, then their values are used instead. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default which is very likely to be <code>1</code>, meaning no alignment. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-falign-loops</code></p>
<dd>
<dt><code>-falign-loops=</code><i>n</i></p>
<dd>Align loops to a power-of-two boundary, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. If the loops are executed many times, this makes up for any execution of the dummy operations. </p>
<p> <code>-fno-align-loops</code> and <code>-falign-loops=1</code> are equivalent and mean that loops are not aligned. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-falign-jumps</code></p>
<dd>
<dt><code>-falign-jumps=</code><i>n</i></p>
<dd>Align branch targets to a power-of-two boundary, for branch targets where the targets can only be reached by jumping, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. In this case, no dummy operations need be executed. </p>
<p> <code>-fno-align-jumps</code> and <code>-falign-jumps=1</code> are equivalent and mean that loops are not aligned. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-funit-at-a-time</code></p>
<dd>This option is left for compatibility reasons. <code>-funit-at-a-time</code> has no effect, while <code>-fno-unit-at-a-time</code> implies <code>-fno-toplevel-reorder</code> and <code>-fno-section-anchors</code>. </p>
<p> Enabled by default.</p>
<dt><code>-fno-toplevel-reorder</code></p>
<dd>Do not reorder top-level functions, variables, and <tt>&quot;asm&quot;</tt> statements. Output them in the same order that they appear in the input file. When this option is used, unreferenced static variables are not removed. This option is intended to support existing code that relies on a particular ordering. For new code, it is better to use attributes when possible. </p>
<p> Enabled at level <code>-O0</code>. When disabled explicitly, it also implies <code>-fno-section-anchors</code>, which is otherwise enabled at <code>-O0</code> on some targets.</p>
<dt><code>-fweb</code></p>
<dd>Constructs webs as commonly used for register allocation purposes and assign each web individual pseudo register. This allows the register allocation pass to operate on pseudos directly, but also strengthens several other optimization passes, such as <font SIZE="-1">CSE,</font> loop optimizer and trivial dead code remover. It can, however, make debugging impossible, since variables no longer stay in a &#8220;home register&#8221;. </p>
<p> Enabled by default with <code>-funroll-loops</code>.</p>
<dt><code>-fwhole-program</code></p>
<dd>Assume that the current compilation unit represents the whole program being compiled. All public functions and variables with the exception of <tt>&quot;main&quot;</tt> and those merged by attribute <tt>&quot;externally_visible&quot;</tt> become static functions and in effect are optimized more aggressively by interprocedural optimizers. </p>
<p> This option should not be used in combination with <tt>&quot;-flto&quot;</tt>. Instead relying on a linker plugin should provide safer and more precise information.</p>
<dt><code>-flto[=</code><i>n</i><code>]</code></p>
<dd>This option runs the standard link-time optimizer. When invoked with source code, it generates <font SIZE="-1">GIMPLE </font>(one of <font SIZE="-1">GCC</font>&#8216;s internal representations) and writes it to special <font SIZE="-1">ELF</font> sections in the object file. When the object files are linked together, all the function bodies are read from these <font SIZE="-1">ELF</font> sections and instantiated as if they had been part of the same translation unit. </p>
<p> To use the link-time optimizer, <code>-flto</code> and optimization options should be specified at compile time and during the final link. For example: </p>
<pre> gcc -c -O2 -flto foo.c
 gcc -c -O2 -flto bar.c
 gcc -o myprog -flto -O2 foo.o bar.o</pre>
<p>The first two invocations to <font SIZE="-1">GCC</font> save a bytecode representation of <font SIZE="-1">GIMPLE</font> into special <font SIZE="-1">ELF</font> sections inside <i>foo.o</i> and <i>bar.o</i>. The final invocation reads the <font SIZE="-1">GIMPLE</font> bytecode from <i>foo.o</i> and <i>bar.o</i>, merges the two files into a single internal image, and compiles the result as usual. Since both <i>foo.o</i> and <i>bar.o</i> are merged into a single image, this causes all the interprocedural analyses and optimizations in <font SIZE="-1">GCC</font> to work across the two files as if they were a single one. This means, for example, that the inliner is able to inline functions in <i>bar.o</i> into functions in <i>foo.o</i> and vice-versa. </p>
<p> Another (simpler) way to enable link-time optimization is: </p>
<pre> gcc -o myprog -flto -O2 foo.c bar.c</pre>
<p>The above generates bytecode for <i>foo.c</i> and <i>bar.c</i>, merges them together into a single <font SIZE="-1">GIMPLE</font> representation and optimizes them as usual to produce <i>myprog</i>. </p>
<p> The only important thing to keep in mind is that to enable link-time optimizations you need to use the <font SIZE="-1">GCC</font> driver to perform the link-step. <font SIZE="-1">GCC</font> then automatically performs link-time optimization if any of the objects involved were compiled with the <code>-flto</code>. You generally should specify the optimization options to be used for link-time optimization though <font SIZE="-1">GCC</font> will try to be clever at guessing an optimization level to use from the options used at compile-time if you fail to specify one at link-time. You can always override the automatic decision to do link-time optimization at link-time by passing <code>-fno-lto</code> to the link command. </p>
<p> To make whole program optimization effective, it is necessary to make certain whole program assumptions. The compiler needs to know what functions and variables can be accessed by libraries and runtime outside of the link-time optimized unit. When supported by the linker, the linker plugin (see <code>-fuse-linker-plugin</code>) passes information to the compiler about used and externally visible symbols. When the linker plugin is not available, <code>-fwhole-program</code> should be used to allow the compiler to make these assumptions, which leads to more aggressive optimization decisions. </p>
<p> When <code>-fuse-linker-plugin</code> is not enabled then, when a file is compiled with <code>-flto</code>, the generated object file is larger than a regular object file because it contains <font SIZE="-1">GIMPLE</font> bytecodes and the usual final code (see <code>-ffat-lto-objects</code>. This means that object files with <font SIZE="-1">LTO</font> information can be linked as normal object files; if <code>-fno-lto</code> is passed to the linker, no interprocedural optimizations are applied. Note that when <code>-fno-fat-lto-objects</code> is enabled the compile-stage is faster but you cannot perform a regular, non-LTO link on them. </p>
<p> Additionally, the optimization flags used to compile individual files are not necessarily related to those used at link time. For instance, </p>
<pre> gcc -c -O0 -ffat-lto-objects -flto foo.c
 gcc -c -O0 -ffat-lto-objects -flto bar.c
 gcc -o myprog -O3 foo.o bar.o</pre>
<p>This produces individual object files with unoptimized assembler code, but the resulting binary <i>myprog</i> is optimized at <code>-O3</code>. If, instead, the final binary is generated with <code>-fno-lto</code>, then <i>myprog</i> is not optimized. </p>
<p> When producing the final binary, <font SIZE="-1">GCC</font> only applies link-time optimizations to those files that contain bytecode. Therefore, you can mix and match object files and libraries with <font SIZE="-1">GIMPLE</font> bytecodes and final object code. <font SIZE="-1">GCC</font> automatically selects which files to optimize in <font SIZE="-1">LTO</font> mode and which files to link without further processing. </p>
<p> There are some code generation flags preserved by <font SIZE="-1">GCC</font> when generating bytecodes, as they need to be used during the final link stage. Generally options specified at link-time override those specified at compile-time. </p>
<p> If you do not specify an optimization level option <code>-O</code> at link-time then <font SIZE="-1">GCC</font> will compute one based on the optimization levels used when compiling the object files. The highest optimization level will win here. </p>
<p> Currently, the following options and their setting are take from the first object file that explicitely specified it: <code>-fPIC</code>, <code>-fpic</code>, <code>-fpie</code>, <code>-fcommon</code>, <code>-fexceptions</code>, <code>-fnon-call-exceptions</code>, <code>-fgnu-tm</code> and all the <code>-m</code> target flags. </p>
<p> Certain <font SIZE="-1">ABI</font> changing flags are required to match in all compilation-units and trying to override this at link-time with a conflicting value is ignored. This includes options such as <code>-freg-struct-return</code> and <code>-fpcc-struct-return</code>. </p>
<p> Other options such as <code>-ffp-contract</code>, <code>-fno-strict-overflow</code>, <code>-fwrapv</code>, <code>-fno-trapv</code> or <code>-fno-strict-aliasing</code> are passed through to the link stage and merged conservatively for conflicting translation units. Specifically <code>-fno-strict-overflow</code>, <code>-fwrapv</code> and <code>-fno-trapv</code> take precedence and for example <code>-ffp-contract=off</code> takes precedence over <code>-ffp-contract=fast</code>. You can override them at linke-time. </p>
<p> It is recommended that you compile all the files participating in the same link with the same options and also specify those options at link time. </p>
<p> If <font SIZE="-1">LTO</font> encounters objects with C linkage declared with incompatible types in separate translation units to be linked together (undefined behavior according to <font SIZE="-1">ISO C99 6.2.7</font>), a non-fatal diagnostic may be issued. The behavior is still undefined at run time. Similar diagnostics may be raised for other languages. </p>
<p> Another feature of <font SIZE="-1">LTO</font> is that it is possible to apply interprocedural optimizations on files written in different languages: </p>
<pre> gcc -c -flto foo.c
 g++ -c -flto bar.cc
 gfortran -c -flto baz.f90
 g++ -o myprog -flto -O3 foo.o bar.o baz.o -lgfortran</pre>
<p>Notice that the final link is done with <code>g++</code> to get the C<font SIZE="-2">++</font> runtime libraries and <code>-lgfortran</code> is added to get the Fortran runtime libraries. In general, when mixing languages in <font SIZE="-1">LTO</font> mode, you should use the same link command options as when mixing languages in a regular (non-LTO) compilation. </p>
<p> If object files containing <font SIZE="-1">GIMPLE</font> bytecode are stored in a library archive, say <i>libfoo.a</i>, it is possible to extract and use them in an <font SIZE="-1">LTO</font> link if you are using a linker with plugin support. To create static libraries suitable for <font SIZE="-1">LTO,</font> use <code>gcc-ar</code> and <code>gcc-ranlib</code> instead of <code>ar</code> and <tt>&quot;ranlib&quot;</tt>; to show the symbols of object files with <font SIZE="-1">GIMPLE</font> bytecode, use <code>gcc-nm</code>. Those commands require that <code>ar</code>, <code>ranlib</code> and <code>nm</code> have been compiled with plugin support. At link time, use the the flag <code>-fuse-linker-plugin</code> to ensure that the library participates in the <font SIZE="-1">LTO</font> optimization process: </p>
<pre> gcc -o myprog -O2 -flto -fuse-linker-plugin a.o b.o -lfoo</pre>
<p>With the linker plugin enabled, the linker extracts the needed <font SIZE="-1">GIMPLE</font> files from <i>libfoo.a</i> and passes them on to the running <font SIZE="-1">GCC</font> to make them part of the aggregated <font SIZE="-1">GIMPLE</font> image to be optimized. </p>
<p> If you are not using a linker with plugin support and/or do not enable the linker plugin, then the objects inside <i>libfoo.a</i> are extracted and linked as usual, but they do not participate in the <font SIZE="-1">LTO</font> optimization process. In order to make a static library suitable for both <font SIZE="-1">LTO</font> optimization and usual linkage, compile its object files with <code>-flto</code> <tt>&quot;-ffat-lto-objects&quot;</tt>. </p>
<p> Link-time optimizations do not require the presence of the whole program to operate. If the program does not require any symbols to be exported, it is possible to combine <code>-flto</code> and <code>-fwhole-program</code> to allow the interprocedural optimizers to use more aggressive assumptions which may lead to improved optimization opportunities. Use of <code>-fwhole-program</code> is not needed when linker plugin is active (see <code>-fuse-linker-plugin</code>). </p>
<p> The current implementation of <font SIZE="-1">LTO</font> makes no attempt to generate bytecode that is portable between different types of hosts. The bytecode files are versioned and there is a strict version check, so bytecode files generated in one version of <font SIZE="-1">GCC</font> will not work with an older or newer version of <font SIZE="-1">GCC.</font> </p>
<p> Link-time optimization does not work well with generation of debugging information. Combining <code>-flto</code> with <code>-g</code> is currently experimental and expected to produce unexpected results. </p>
<p> If you specify the optional <i>n</i>, the optimization and code generation done at link time is executed in parallel using <i>n</i> parallel jobs by utilizing an installed <code>make</code> program. The environment variable <font SIZE="-1"><code>MAKE</code></font> may be used to override the program used. The default value for <i>n</i> is 1. </p>
<p> You can also specify <code>-flto=jobserver</code> to use <font SIZE="-1">GNU</font> make&#8217;s job server mode to determine the number of parallel jobs. This is useful when the Makefile calling <font SIZE="-1">GCC</font> is already executing in parallel. You must prepend a <code>+</code> to the command recipe in the parent Makefile for this to work. This option likely only works if <font SIZE="-1"><code>MAKE</code></font> is <font SIZE="-1">GNU</font> make.</p>
<dt><code>-flto-partition=</code><i>alg</i></p>
<dd>Specify the partitioning algorithm used by the link-time optimizer. The value is either <tt>&quot;1to1&quot;</tt> to specify a partitioning mirroring the original source files or <tt>&quot;balanced&quot;</tt> to specify partitioning into equally sized chunks (whenever possible) or <tt>&quot;max&quot;</tt> to create new partition for every symbol where possible. Specifying <tt>&quot;none&quot;</tt> as an algorithm disables partitioning and streaming completely. The default value is <tt>&quot;balanced&quot;</tt>. While <tt>&quot;1to1&quot;</tt> can be used as an workaround for various code ordering issues, the <tt>&quot;max&quot;</tt> partitioning is intended for internal testing only.</p>
<dt><code>-flto-compression-level=</code><i>n</i></p>
<dd>This option specifies the level of compression used for intermediate language written to <font SIZE="-1">LTO</font> object files, and is only meaningful in conjunction with <font SIZE="-1">LTO</font> mode (<code>-flto</code>). Valid values are 0 (no compression) to 9 (maximum compression). Values outside this range are clamped to either 0 or 9. If the option is not given, a default balanced compression setting is used.</p>
<dt><code>-flto-report</code></p>
<dd>Prints a report with internal details on the workings of the link-time optimizer. The contents of this report vary from version to version. It is meant to be useful to <font SIZE="-1">GCC</font> developers when processing object files in <font SIZE="-1">LTO</font> mode (via <code>-flto</code>). </p>
<p> Disabled by default.</p>
<dt><code>-flto-report-wpa</code></p>
<dd>Like <code>-flto-report</code>, but only print for the <font SIZE="-1">WPA</font> phase of Link Time Optimization.</p>
<dt><code>-fuse-linker-plugin</code></p>
<dd>Enables the use of a linker plugin during link-time optimization. This option relies on plugin support in the linker, which is available in gold or in <font SIZE="-1">GNU</font> ld 2.21 or newer. </p>
<p> This option enables the extraction of object files with <font SIZE="-1">GIMPLE</font> bytecode out of library archives. This improves the quality of optimization by exposing more code to the link-time optimizer. This information specifies what symbols can be accessed externally (by non-LTO object or during dynamic linking). Resulting code quality improvements on binaries (and shared libraries that use hidden visibility) are similar to <tt>&quot;-fwhole-program&quot;</tt>. See <code>-flto</code> for a description of the effect of this flag and how to use it. </p>
<p> This option is enabled by default when <font SIZE="-1">LTO</font> support in <font SIZE="-1">GCC</font> is enabled and <font SIZE="-1">GCC</font> was configured for use with a linker supporting plugins (<font SIZE="-1">GNU</font> ld 2.21 or newer or gold).</p>
<dt><code>-ffat-lto-objects</code></p>
<dd>Fat <font SIZE="-1">LTO</font> objects are object files that contain both the intermediate language and the object code. This makes them usable for both <font SIZE="-1">LTO</font> linking and normal linking. This option is effective only when compiling with <code>-flto</code> and is ignored at link time. </p>
<p> <code>-fno-fat-lto-objects</code> improves compilation time over plain <font SIZE="-1">LTO,</font> but requires the complete toolchain to be aware of <font SIZE="-1">LTO.</font> It requires a linker with linker plugin support for basic functionality. Additionally, <code>nm</code>, <code>ar</code> and <code>ranlib</code> need to support linker plugins to allow a full-featured build environment (capable of building static libraries etc). <font SIZE="-1">GCC</font> provides the <code>gcc-ar</code>, <code>gcc-nm</code>, <code>gcc-ranlib</code> wrappers to pass the right options to these tools. With non fat <font SIZE="-1">LTO</font> makefiles need to be modified to use them. </p>
<p> The default is <code>-fno-fat-lto-objects</code> on targets with linker plugin support.</p>
<dt><code>-fcompare-elim</code></p>
<dd>After register allocation and post-register allocation instruction splitting, identify arithmetic instructions that compute processor flags similar to a comparison operation based on that arithmetic. If possible, eliminate the explicit comparison operation. </p>
<p> This pass only applies to certain targets that cannot explicitly represent the comparison operation before register allocation is complete. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fuse-ld=bfd</code></p>
<dd>Use the <code>bfd</code> linker instead of the default linker.</p>
<dt><code>-fuse-ld=gold</code></p>
<dd>Use the <code>gold</code> linker instead of the default linker.</p>
<dt><code>-fcprop-registers</code></p>
<dd>After register allocation and post-register allocation instruction splitting, perform a copy-propagation pass to try to reduce scheduling dependencies and occasionally eliminate the copy. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fprofile-correction</code></p>
<dd>Profiles collected using an instrumented binary for multi-threaded programs may be inconsistent due to missed counter updates. When this option is specified, <font SIZE="-1">GCC</font> uses heuristics to correct or smooth out such inconsistencies. By default, <font SIZE="-1">GCC</font> emits an error message when an inconsistent profile is detected.</p>
<dt><code>-fprofile-dir=</code><i>path</i></p>
<dd>Set the directory to search for the profile data files in to <i>path</i>. This option affects only the profile data generated by <code>-fprofile-generate</code>, <code>-ftest-coverage</code>, <code>-fprofile-arcs</code> and used by <code>-fprofile-use</code> and <code>-fbranch-probabilities</code> and its related options. Both absolute and relative paths can be used. By default, <font SIZE="-1">GCC</font> uses the current directory as <i>path</i>, thus the profile data file appears in the same directory as the object file.</p>
<dt><code>-fprofile-generate</code></p>
<dd>
<dt><code>-fprofile-generate=</code><i>path</i></p>
<dd>Enable options usually used for instrumenting application to produce profile useful for later recompilation with profile feedback based optimization. You must use <code>-fprofile-generate</code> both when compiling and when linking your program. </p>
<p> The following options are enabled: <tt>&quot;-fprofile-arcs&quot;</tt>, <tt>&quot;-fprofile-values&quot;</tt>, <tt>&quot;-fvpt&quot;</tt>. </p>
<p> If <i>path</i> is specified, <font SIZE="-1">GCC</font> looks at the <i>path</i> to find the profile feedback data files. See <code>-fprofile-dir</code>.</p>
<dt><code>-fprofile-use</code></p>
<dd>
<dt><code>-fprofile-use=</code><i>path</i></p>
<dd>Enable profile feedback directed optimizations, and optimizations generally profitable only with profile feedback available. </p>
<p> The following options are enabled: <tt>&quot;-fbranch-probabilities&quot;</tt>, <tt>&quot;-fvpt&quot;</tt>, <tt>&quot;-funroll-loops&quot;</tt>, <tt>&quot;-fpeel-loops&quot;</tt>, <tt>&quot;-ftracer&quot;</tt>, <tt>&quot;-ftree-vectorize&quot;</tt>, <tt>&quot;ftree-loop-distribute-patterns&quot;</tt> </p>
<p> By default, <font SIZE="-1">GCC</font> emits an error message if the feedback profiles do not match the source code. This error can be turned into a warning by using <code>-Wcoverage-mismatch</code>. Note this may result in poorly optimized code. </p>
<p> If <i>path</i> is specified, <font SIZE="-1">GCC</font> looks at the <i>path</i> to find the profile feedback data files. See <code>-fprofile-dir</code>.</dl>
<p> The following options control compiler behavior regarding floating-point arithmetic. These options trade off between speed and correctness. All must be specifically enabled.</p>
<dl COMPACT>
<dt><code>-ffloat-store</code></p>
<dd>Do not store floating-point variables in registers, and inhibit other options that might change whether a floating-point value is taken from a register or memory. </p>
<p> This option prevents undesirable excess precision on machines such as the 68000 where the floating registers (of the 68881) keep more precision than a <tt>&quot;double&quot;</tt> is supposed to have. Similarly for the x86 architecture. For most programs, the excess precision does only good, but a few programs rely on the precise definition of <font SIZE="-1">IEEE</font> floating point. Use <code>-ffloat-store</code> for such programs, after modifying them to store all pertinent intermediate computations into variables.</p>
<dt><code>-fexcess-precision=</code><i>style</i></p>
<dd>This option allows further control over excess precision on machines where floating-point registers have more precision than the <font SIZE="-1">IEEE </font><tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt> types and the processor does not support operations rounding to those types. By default, <code>-fexcess-precision=fast</code> is in effect; this means that operations are carried out in the precision of the registers and that it is unpredictable when rounding to the types specified in the source code takes place. When compiling C, if <code>-fexcess-precision=standard</code> is specified then excess precision follows the rules specified in <font SIZE="-1">ISO C99</font>; in particular, both casts and assignments cause values to be rounded to their semantic types (whereas <code>-ffloat-store</code> only affects assignments). This option is enabled by default for C if a strict conformance option such as <code>-std=c99</code> is used. </p>
<p> <code>-fexcess-precision=standard</code> is not implemented for languages other than C, and has no effect if <code>-funsafe-math-optimizations</code> or <code>-ffast-math</code> is specified. On the x86, it also has no effect if <code>-mfpmath=sse</code> or <code>-mfpmath=sse+387</code> is specified; in the former case, <font SIZE="-1">IEEE</font> semantics apply without excess precision, and in the latter, rounding is unpredictable.</p>
<dt><code>-ffast-math</code></p>
<dd>Sets <code>-fno-math-errno</code>, <code>-funsafe-math-optimizations</code>, <code>-ffinite-math-only</code>, <code>-fno-rounding-math</code>, <code>-fno-signaling-nans</code> and <code>-fcx-limited-range</code>. </p>
<p> This option causes the preprocessor macro <tt>&quot;__FAST_MATH__&quot;</tt> to be defined. </p>
<p> This option is not turned on by any <code>-O</code> option besides <code>-Ofast</code> since it can result in incorrect output for programs that depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. It may, however, yield faster code for programs that do not require the guarantees of these specifications.</p>
<dt><code>-fno-math-errno</code></p>
<dd>Do not set <tt>&quot;errno&quot;</tt> after calling math functions that are executed with a single instruction, e.g., <tt>&quot;sqrt&quot;</tt>. A program that relies on <font SIZE="-1">IEEE</font> exceptions for math error handling may want to use this flag for speed while maintaining <font SIZE="-1">IEEE</font> arithmetic compatibility. </p>
<p> This option is not turned on by any <code>-O</code> option since it can result in incorrect output for programs that depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. It may, however, yield faster code for programs that do not require the guarantees of these specifications. </p>
<p> The default is <code>-fmath-errno</code>. </p>
<p> On Darwin systems, the math library never sets <tt>&quot;errno&quot;</tt>. There is therefore no reason for the compiler to consider the possibility that it might, and <code>-fno-math-errno</code> is the default.</p>
<dt><code>-funsafe-math-optimizations</code></p>
<dd>Allow optimizations for floating-point arithmetic that (a) assume that arguments and results are valid and (b) may violate <font SIZE="-1">IEEE</font> or <font SIZE="-1">ANSI</font> standards. When used at link-time, it may include libraries or startup files that change the default <font SIZE="-1">FPU</font> control word or other similar optimizations. </p>
<p> This option is not turned on by any <code>-O</code> option since it can result in incorrect output for programs that depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. It may, however, yield faster code for programs that do not require the guarantees of these specifications. Enables <code>-fno-signed-zeros</code>, <code>-fno-trapping-math</code>, <code>-fassociative-math</code> and <code>-freciprocal-math</code>. </p>
<p> The default is <code>-fno-unsafe-math-optimizations</code>.</p>
<dt><code>-fassociative-math</code></p>
<dd>Allow re-association of operands in series of floating-point operations. This violates the <font SIZE="-1">ISO C</font> and C<font SIZE="-2">++</font> language standard by possibly changing computation result. <font SIZE="-1">NOTE:</font> re-ordering may change the sign of zero as well as ignore NaNs and inhibit or create underflow or overflow (and thus cannot be used on code that relies on rounding behavior like <tt>&quot;(x + 2**52) - 2**52&quot;</tt>. May also reorder floating-point comparisons and thus may not be used when ordered comparisons are required. This option requires that both <code>-fno-signed-zeros</code> and <code>-fno-trapping-math</code> be in effect. Moreover, it doesn&#8217;t make much sense with <code>-frounding-math</code>. For Fortran the option is automatically enabled when both <code>-fno-signed-zeros</code> and <code>-fno-trapping-math</code> are in effect. </p>
<p> The default is <code>-fno-associative-math</code>.</p>
<dt><code>-freciprocal-math</code></p>
<dd>Allow the reciprocal of a value to be used instead of dividing by the value if this enables optimizations. For example <tt>&quot;x / y&quot;</tt> can be replaced with <tt>&quot;x * (1/y)&quot;</tt>, which is useful if <tt>&quot;(1/y)&quot;</tt> is subject to common subexpression elimination. Note that this loses precision and increases the number of flops operating on the value. </p>
<p> The default is <code>-fno-reciprocal-math</code>.</p>
<dt><code>-ffinite-math-only</code></p>
<dd>Allow optimizations for floating-point arithmetic that assume that arguments and results are not NaNs or +-Infs. </p>
<p> This option is not turned on by any <code>-O</code> option since it can result in incorrect output for programs that depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. It may, however, yield faster code for programs that do not require the guarantees of these specifications. </p>
<p> The default is <code>-fno-finite-math-only</code>.</p>
<dt><code>-fno-signed-zeros</code></p>
<dd>Allow optimizations for floating-point arithmetic that ignore the signedness of zero. <font SIZE="-1">IEEE</font> arithmetic specifies the behavior of distinct +0.0 and -0.0 values, which then prohibits simplification of expressions such as x+0.0 or 0.0*x (even with <code>-ffinite-math-only</code>). This option implies that the sign of a zero result isn&#8217;t significant. </p>
<p> The default is <code>-fsigned-zeros</code>.</p>
<dt><code>-fno-trapping-math</code></p>
<dd>Compile code assuming that floating-point operations cannot generate user-visible traps. These traps include division by zero, overflow, underflow, inexact result and invalid operation. This option requires that <code>-fno-signaling-nans</code> be in effect. Setting this option may allow faster code if one relies on &#8220;non-stop&#8221; <font SIZE="-1">IEEE</font> arithmetic, for example. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs that depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-ftrapping-math</code>.</p>
<dt><code>-frounding-math</code></p>
<dd>Disable transformations and optimizations that assume default floating-point rounding behavior. This is round-to-zero for all floating point to integer conversions, and round-to-nearest for all other arithmetic truncations. This option should be specified for programs that change the <font SIZE="-1">FP</font> rounding mode dynamically, or that may be executed with a non-default rounding mode. This option disables constant folding of floating-point expressions at compile time (which may be affected by rounding mode) and arithmetic transformations that are unsafe in the presence of sign-dependent rounding modes. </p>
<p> The default is <code>-fno-rounding-math</code>. </p>
<p> This option is experimental and does not currently guarantee to disable all <font SIZE="-1">GCC</font> optimizations that are affected by rounding mode. Future versions of <font SIZE="-1">GCC</font> may provide finer control of this setting using C99&#8217;s <tt>&quot;FENV_ACCESS&quot;</tt> pragma. This command-line option will be used to specify the default state for <tt>&quot;FENV_ACCESS&quot;</tt>.</p>
<dt><code>-fsignaling-nans</code></p>
<dd>Compile code assuming that <font SIZE="-1">IEEE</font> signaling NaNs may generate user-visible traps during floating-point operations. Setting this option disables optimizations that may change the number of exceptions visible with signaling NaNs. This option implies <code>-ftrapping-math</code>. </p>
<p> This option causes the preprocessor macro <tt>&quot;__SUPPORT_SNAN__&quot;</tt> to be defined. </p>
<p> The default is <code>-fno-signaling-nans</code>. </p>
<p> This option is experimental and does not currently guarantee to disable all <font SIZE="-1">GCC</font> optimizations that affect signaling NaN behavior.</p>
<dt><code>-fsingle-precision-constant</code></p>
<dd>Treat floating-point constants as single precision instead of implicitly converting them to double-precision constants.</p>
<dt><code>-fcx-limited-range</code></p>
<dd>When enabled, this option states that a range reduction step is not needed when performing complex division. Also, there is no checking whether the result of a complex multiplication or division is <tt>&quot;NaN + I*NaN&quot;</tt>, with an attempt to rescue the situation in that case. The default is <code>-fno-cx-limited-range</code>, but is enabled by <code>-ffast-math</code>. </p>
<p> This option controls the default setting of the <font SIZE="-1">ISO C99 </font><tt>&quot;CX_LIMITED_RANGE&quot;</tt> pragma. Nevertheless, the option applies to all languages.</p>
<dt><code>-fcx-fortran-rules</code></p>
<dd>Complex multiplication and division follow Fortran rules. Range reduction is done as part of complex division, but there is no checking whether the result of a complex multiplication or division is <tt>&quot;NaN + I*NaN&quot;</tt>, with an attempt to rescue the situation in that case. </p>
<p> The default is <code>-fno-cx-fortran-rules</code>.</dl>
<p> The following options control optimizations that may improve performance, but are not enabled by any <code>-O</code> options. This section includes experimental options that may produce broken code.</p>
<dl COMPACT>
<dt><code>-fbranch-probabilities</code></p>
<dd>After running a program compiled with <code>-fprofile-arcs</code>, you can compile it a second time using <code>-fbranch-probabilities</code>, to improve optimizations based on the number of times each branch was taken. When a program compiled with <code>-fprofile-arcs</code> exits, it saves arc execution counts to a file called <i>sourcename.gcda</i> for each source file. The information in this data file is very dependent on the structure of the generated code, so you must use the same source code and the same optimization options for both compilations. </p>
<p> With <code>-fbranch-probabilities</code>, <font SIZE="-1">GCC</font> puts a <font SIZE="-1"><code>REG_BR_PROB</code></font> note on each <font SIZE="-1"><code>JUMP_INSN</code></font> and <font SIZE="-1"><code>CALL_INSN</code></font>. These can be used to improve optimization. Currently, they are only used in one place: in <i>reorg.c</i>, instead of guessing which path a branch is most likely to take, the <font SIZE="-1"><code>REG_BR_PROB</code></font> values are used to exactly determine which path is taken more often.</p>
<dt><code>-fprofile-values</code></p>
<dd>If combined with <code>-fprofile-arcs</code>, it adds code so that some data about values of expressions in the program is gathered. </p>
<p> With <code>-fbranch-probabilities</code>, it reads back the data gathered from profiling values of expressions for usage in optimizations. </p>
<p> Enabled with <code>-fprofile-generate</code> and <code>-fprofile-use</code>.</p>
<dt><code>-fprofile-reorder-functions</code></p>
<dd>Function reordering based on profile instrumentation collects first time of execution of a function and orders these functions in ascending order. </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-fvpt</code></p>
<dd>If combined with <code>-fprofile-arcs</code>, this option instructs the compiler to add code to gather information about values of expressions. </p>
<p> With <code>-fbranch-probabilities</code>, it reads back the data gathered and actually performs the optimizations based on them. Currently the optimizations include specialization of division operations using the knowledge about the value of the denominator.</p>
<dt><code>-frename-registers</code></p>
<dd>Attempt to avoid false dependencies in scheduled code by making use of registers left over after register allocation. This optimization most benefits processors with lots of registers. Depending on the debug information format adopted by the target, however, it can make debugging impossible, since variables no longer stay in a &#8220;home register&#8221;. </p>
<p> Enabled by default with <code>-funroll-loops</code> and <code>-fpeel-loops</code>.</p>
<dt><code>-ftracer</code></p>
<dd>Perform tail duplication to enlarge superblock size. This transformation simplifies the control flow of the function allowing other optimizations to do a better job. </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-funroll-loops</code></p>
<dd>Unroll loops whose number of iterations can be determined at compile time or upon entry to the loop. <code>-funroll-loops</code> implies <code>-frerun-cse-after-loop</code>, <code>-fweb</code> and <code>-frename-registers</code>. It also turns on complete loop peeling (i.e. complete removal of loops with a small constant number of iterations). This option makes code larger, and may or may not make it run faster. </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-funroll-all-loops</code></p>
<dd>Unroll all loops, even if their number of iterations is uncertain when the loop is entered. This usually makes programs run more slowly. <code>-funroll-all-loops</code> implies the same options as <code>-funroll-loops</code>.</p>
<dt><code>-fpeel-loops</code></p>
<dd>Peels loops for which there is enough information that they do not roll much (from profile feedback). It also turns on complete loop peeling (i.e. complete removal of loops with small constant number of iterations). </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-fmove-loop-invariants</code></p>
<dd>Enables the loop invariant motion pass in the <font SIZE="-1">RTL</font> loop optimizer. Enabled at level <code>-O1</code></p>
<dt><code>-funswitch-loops</code></p>
<dd>Move branches with loop invariant conditions out of the loop, with duplicates of the loop on both branches (modified according to result of the condition).</p>
<dt><code>-ffunction-sections</code></p>
<dd>
<dt><code>-fdata-sections</code></p>
<dd>Place each function or data item into its own section in the output file if the target supports arbitrary sections. The name of the function or the name of the data item determines the section&#8217;s name in the output file. </p>
<p> Use these options on systems where the linker can perform optimizations to improve locality of reference in the instruction space. Most systems using the <font SIZE="-1">ELF</font> object format and <font SIZE="-1">SPARC</font> processors running Solaris 2 have linkers with such optimizations. <font SIZE="-1">AIX</font> may have these optimizations in the future. </p>
<p> Only use these options when there are significant benefits from doing so. When you specify these options, the assembler and linker create larger object and executable files and are also slower. You cannot use <tt>&quot;gprof&quot;</tt> on all systems if you specify this option, and you may have problems with debugging if you specify both this option and <code>-g</code>.</p>
<dt><code>-fbranch-target-load-optimize</code></p>
<dd>Perform branch target register load optimization before prologue / epilogue threading. The use of target registers can typically be exposed only during reload, thus hoisting loads out of loops and doing inter-block scheduling needs a separate optimization pass.</p>
<dt><code>-fbranch-target-load-optimize2</code></p>
<dd>Perform branch target register load optimization after prologue / epilogue threading.</p>
<dt><code>-fbtr-bb-exclusive</code></p>
<dd>When performing branch target register load optimization, don&#8217;t reuse branch target registers within any basic block.</p>
<dt><code>-fstack-protector</code></p>
<dd>Emit extra code to check for buffer overflows, such as stack smashing attacks. This is done by adding a guard variable to functions with vulnerable objects. This includes functions that call <tt>&quot;alloca&quot;</tt>, and functions with buffers larger than 8 bytes. The guards are initialized when a function is entered and then checked when the function exits. If a guard check fails, an error message is printed and the program exits.</p>
<dt><code>-fstack-protector-all</code></p>
<dd>Like <code>-fstack-protector</code> except that all functions are protected.</p>
<dt><code>-fstack-protector-strong</code></p>
<dd>Like <code>-fstack-protector</code> but includes additional functions to be protected &#8212; those that have local array definitions, or have references to local frame addresses.</p>
<dt><code>-fsection-anchors</code></p>
<dd>Try to reduce the number of symbolic address calculations by using shared &#8220;anchor&#8221; symbols to address nearby objects. This transformation can help to reduce the number of <font SIZE="-1">GOT</font> entries and <font SIZE="-1">GOT</font> accesses on some targets. </p>
<p> For example, the implementation of the following function <tt>&quot;foo&quot;</tt>: </p>
<pre> static int a, b, c;
 int foo (void) { return a + b + c; }</pre>
<p>usually calculates the addresses of all three variables, but if you compile it with <code>-fsection-anchors</code>, it accesses the variables from a common anchor point instead. The effect is similar to the following pseudocode (which isn&#8217;t valid C): </p>
<pre> int foo (void)
 {
 register int *xr = &amp;x;
 return xr[&amp;a - &amp;x] + xr[&amp;b - &amp;x] + xr[&amp;c - &amp;x];
 }</pre>
<p>Not all targets support this option.</p>
<dt><code>&#8211;param</code> <i>name</i><code>=</code><i>value</i></p>
<dd>In some places, <font SIZE="-1">GCC</font> uses various constants to control the amount of optimization that is done. For example, <font SIZE="-1">GCC</font> does not inline functions that contain more than a certain number of instructions. You can control some of these constants on the command line using the <code>&#8211;param</code> option. </p>
<p> The names of specific parameters, and the meaning of the values, are tied to the internals of the compiler, and are subject to change without notice in future releases. </p>
<p> In each case, the <i>value</i> is an integer. The allowable choices for <i>name</i> are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>predictable-branch-outcome</code></p>
<dd>When branch is predicted to be taken with probability lower than this threshold (in percent), then it is considered well predictable. The default is 10.</p>
<dt><code>max-crossjump-edges</code></p>
<dd>The maximum number of incoming edges to consider for cross-jumping. The algorithm used by <code>-fcrossjumping</code> is O(N^2) in the number of edges incoming to each block. Increasing values mean more aggressive optimization, making the compilation time increase with probably small improvement in executable size.</p>
<dt><code>min-crossjump-insns</code></p>
<dd>The minimum number of instructions that must be matched at the end of two blocks before cross-jumping is performed on them. This value is ignored in the case where all instructions in the block being cross-jumped from are matched. The default value is 5.</p>
<dt><code>max-grow-copy-bb-insns</code></p>
<dd>The maximum code size expansion factor when copying basic blocks instead of jumping. The expansion is relative to a jump instruction. The default value is 8.</p>
<dt><code>max-goto-duplication-insns</code></p>
<dd>The maximum number of instructions to duplicate to a block that jumps to a computed goto. To avoid O(N^2) behavior in a number of passes, <font SIZE="-1">GCC</font> factors computed gotos early in the compilation process, and unfactors them as late as possible. Only computed jumps at the end of a basic blocks with no more than max-goto-duplication-insns are unfactored. The default value is 8.</p>
<dt><code>max-delay-slot-insn-search</code></p>
<dd>The maximum number of instructions to consider when looking for an instruction to fill a delay slot. If more than this arbitrary number of instructions are searched, the time savings from filling the delay slot are minimal, so stop searching. Increasing values mean more aggressive optimization, making the compilation time increase with probably small improvement in execution time.</p>
<dt><code>max-delay-slot-live-search</code></p>
<dd>When trying to fill delay slots, the maximum number of instructions to consider when searching for a block with valid live register information. Increasing this arbitrarily chosen value means more aggressive optimization, increasing the compilation time. This parameter should be removed when the delay slot code is rewritten to maintain the control-flow graph.</p>
<dt><code>max-gcse-memory</code></p>
<dd>The approximate maximum amount of memory that can be allocated in order to perform the global common subexpression elimination optimization. If more memory than specified is required, the optimization is not done.</p>
<dt><code>max-gcse-insertion-ratio</code></p>
<dd>If the ratio of expression insertions to deletions is larger than this value for any expression, then <font SIZE="-1">RTL PRE</font> inserts or removes the expression and thus leaves partially redundant computations in the instruction stream. The default value is 20.</p>
<dt><code>max-pending-list-length</code></p>
<dd>The maximum number of pending dependencies scheduling allows before flushing the current state and starting over. Large functions with few branches or calls can create excessively large lists which needlessly consume memory and resources.</p>
<dt><code>max-modulo-backtrack-attempts</code></p>
<dd>The maximum number of backtrack attempts the scheduler should make when modulo scheduling a loop. Larger values can exponentially increase compilation time.</p>
<dt><code>max-inline-insns-single</code></p>
<dd>Several parameters control the tree inliner used in <font SIZE="-1">GCC.</font> This number sets the maximum number of instructions (counted in <font SIZE="-1">GCC</font>&#8216;s internal representation) in a single function that the tree inliner considers for inlining. This only affects functions declared inline and methods implemented in a class declaration (C<font SIZE="-2">++</font>). The default value is 400.</p>
<dt><code>max-inline-insns-auto</code></p>
<dd>When you use <code>-finline-functions</code> (included in <code>-O3</code>), a lot of functions that would otherwise not be considered for inlining by the compiler are investigated. To those functions, a different (more restrictive) limit compared to functions declared inline can be applied. The default value is 40.</p>
<dt><code>inline-min-speedup</code></p>
<dd>When estimated performance improvement of caller + callee runtime exceeds this threshold (in precent), the function can be inlined regardless the limit on <code>&#8211;param max-inline-insns-single</code> and <code>&#8211;param max-inline-insns-auto</code>.</p>
<dt><code>large-function-insns</code></p>
<dd>The limit specifying really large functions. For functions larger than this limit after inlining, inlining is constrained by <code>&#8211;param large-function-growth</code>. This parameter is useful primarily to avoid extreme compilation time caused by non-linear algorithms used by the back end. The default value is 2700.</p>
<dt><code>large-function-growth</code></p>
<dd>Specifies maximal growth of large function caused by inlining in percents. The default value is 100 which limits large function growth to 2.0 times the original size.</p>
<dt><code>large-unit-insns</code></p>
<dd>The limit specifying large translation unit. Growth caused by inlining of units larger than this limit is limited by <code>&#8211;param inline-unit-growth</code>. For small units this might be too tight. For example, consider a unit consisting of function A that is inline and B that just calls A three times. If B is small relative to A, the growth of unit is 300\% and yet such inlining is very sane. For very large units consisting of small inlineable functions, however, the overall unit growth limit is needed to avoid exponential explosion of code size. Thus for smaller units, the size is increased to <code>&#8211;param large-unit-insns</code> before applying <code>&#8211;param inline-unit-growth</code>. The default is 10000.</p>
<dt><code>inline-unit-growth</code></p>
<dd>Specifies maximal overall growth of the compilation unit caused by inlining. The default value is 30 which limits unit growth to 1.3 times the original size.</p>
<dt><code>ipcp-unit-growth</code></p>
<dd>Specifies maximal overall growth of the compilation unit caused by interprocedural constant propagation. The default value is 10 which limits unit growth to 1.1 times the original size.</p>
<dt><code>large-stack-frame</code></p>
<dd>The limit specifying large stack frames. While inlining the algorithm is trying to not grow past this limit too much. The default value is 256 bytes.</p>
<dt><code>large-stack-frame-growth</code></p>
<dd>Specifies maximal growth of large stack frames caused by inlining in percents. The default value is 1000 which limits large stack frame growth to 11 times the original size.</p>
<dt><code>max-inline-insns-recursive</code></p>
<dd>
<dt><code>max-inline-insns-recursive-auto</code></p>
<dd>Specifies the maximum number of instructions an out-of-line copy of a self-recursive inline function can grow into by performing recursive inlining. </p>
<p> For functions declared inline, <code>&#8211;param max-inline-insns-recursive</code> is taken into account. For functions not declared inline, recursive inlining happens only when <code>-finline-functions</code> (included in <code>-O3</code>) is enabled and <code>&#8211;param max-inline-insns-recursive-auto</code> is used. The default value is 450.</p>
<dt><code>max-inline-recursive-depth</code></p>
<dd>
<dt><code>max-inline-recursive-depth-auto</code></p>
<dd>Specifies the maximum recursion depth used for recursive inlining. </p>
<p> For functions declared inline, <code>&#8211;param max-inline-recursive-depth</code> is taken into account. For functions not declared inline, recursive inlining happens only when <code>-finline-functions</code> (included in <code>-O3</code>) is enabled and <code>&#8211;param max-inline-recursive-depth-auto</code> is used. The default value is 8.</p>
<dt><code>min-inline-recursive-probability</code></p>
<dd>Recursive inlining is profitable only for function having deep recursion in average and can hurt for function having little recursion depth by increasing the prologue size or complexity of function body to other optimizers. </p>
<p> When profile feedback is available (see <code>-fprofile-generate</code>) the actual recursion depth can be guessed from probability that function recurses via a given call expression. This parameter limits inlining only to call expressions whose probability exceeds the given threshold (in percents). The default value is 10.</p>
<dt><code>early-inlining-insns</code></p>
<dd>Specify growth that the early inliner can make. In effect it increases the amount of inlining for code having a large abstraction penalty. The default value is 10.</p>
<dt><code>max-early-inliner-iterations</code></p>
<dd>
<dt><code>max-early-inliner-iterations</code></p>
<dd>Limit of iterations of the early inliner. This basically bounds the number of nested indirect calls the early inliner can resolve. Deeper chains are still handled by late inlining.</p>
<dt><code>comdat-sharing-probability</code></p>
<dd>
<dt><code>comdat-sharing-probability</code></p>
<dd>Probability (in percent) that C<font SIZE="-2">++</font> inline function with comdat visibility are shared across multiple compilation units. The default value is 20.</p>
<dt><code>min-vect-loop-bound</code></p>
<dd>The minimum number of iterations under which loops are not vectorized when <code>-ftree-vectorize</code> is used. The number of iterations after vectorization needs to be greater than the value specified by this option to allow vectorization. The default value is 0.</p>
<dt><code>gcse-cost-distance-ratio</code></p>
<dd>Scaling factor in calculation of maximum distance an expression can be moved by <font SIZE="-1">GCSE</font> optimizations. This is currently supported only in the code hoisting pass. The bigger the ratio, the more aggressive code hoisting is with simple expressions, i.e., the expressions that have cost less than <code>gcse-unrestricted-cost</code>. Specifying 0 disables hoisting of simple expressions. The default value is 10.</p>
<dt><code>gcse-unrestricted-cost</code></p>
<dd>Cost, roughly measured as the cost of a single typical machine instruction, at which <font SIZE="-1">GCSE</font> optimizations do not constrain the distance an expression can travel. This is currently supported only in the code hoisting pass. The lesser the cost, the more aggressive code hoisting is. Specifying 0 allows all expressions to travel unrestricted distances. The default value is 3.</p>
<dt><code>max-hoist-depth</code></p>
<dd>The depth of search in the dominator tree for expressions to hoist. This is used to avoid quadratic behavior in hoisting algorithm. The value of 0 does not limit on the search, but may slow down compilation of huge functions. The default value is 30.</p>
<dt><code>max-tail-merge-comparisons</code></p>
<dd>The maximum amount of similar bbs to compare a bb with. This is used to avoid quadratic behavior in tree tail merging. The default value is 10.</p>
<dt><code>max-tail-merge-iterations</code></p>
<dd>The maximum amount of iterations of the pass over the function. This is used to limit compilation time in tree tail merging. The default value is 2.</p>
<dt><code>max-unrolled-insns</code></p>
<dd>The maximum number of instructions that a loop may have to be unrolled. If a loop is unrolled, this parameter also determines how many times the loop code is unrolled.</p>
<dt><code>max-average-unrolled-insns</code></p>
<dd>The maximum number of instructions biased by probabilities of their execution that a loop may have to be unrolled. If a loop is unrolled, this parameter also determines how many times the loop code is unrolled.</p>
<dt><code>max-unroll-times</code></p>
<dd>The maximum number of unrollings of a single loop.</p>
<dt><code>max-peeled-insns</code></p>
<dd>The maximum number of instructions that a loop may have to be peeled. If a loop is peeled, this parameter also determines how many times the loop code is peeled.</p>
<dt><code>max-peel-times</code></p>
<dd>The maximum number of peelings of a single loop.</p>
<dt><code>max-peel-branches</code></p>
<dd>The maximum number of branches on the hot path through the peeled sequence.</p>
<dt><code>max-completely-peeled-insns</code></p>
<dd>The maximum number of insns of a completely peeled loop.</p>
<dt><code>max-completely-peel-times</code></p>
<dd>The maximum number of iterations of a loop to be suitable for complete peeling.</p>
<dt><code>max-completely-peel-loop-nest-depth</code></p>
<dd>The maximum depth of a loop nest suitable for complete peeling.</p>
<dt><code>max-unswitch-insns</code></p>
<dd>The maximum number of insns of an unswitched loop.</p>
<dt><code>max-unswitch-level</code></p>
<dd>The maximum number of branches unswitched in a single loop.</p>
<dt><code>lim-expensive</code></p>
<dd>The minimum cost of an expensive expression in the loop invariant motion.</p>
<dt><code>iv-consider-all-candidates-bound</code></p>
<dd>Bound on number of candidates for induction variables, below which all candidates are considered for each use in induction variable optimizations. If there are more candidates than this, only the most relevant ones are considered to avoid quadratic time complexity.</p>
<dt><code>iv-max-considered-uses</code></p>
<dd>The induction variable optimizations give up on loops that contain more induction variable uses.</p>
<dt><code>iv-always-prune-cand-set-bound</code></p>
<dd>If the number of candidates in the set is smaller than this value, always try to remove unnecessary ivs from the set when adding a new one.</p>
<dt><code>scev-max-expr-size</code></p>
<dd>Bound on size of expressions used in the scalar evolutions analyzer. Large expressions slow the analyzer.</p>
<dt><code>scev-max-expr-complexity</code></p>
<dd>Bound on the complexity of the expressions in the scalar evolutions analyzer. Complex expressions slow the analyzer.</p>
<dt><code>omega-max-vars</code></p>
<dd>The maximum number of variables in an Omega constraint system. The default value is 128.</p>
<dt><code>omega-max-geqs</code></p>
<dd>The maximum number of inequalities in an Omega constraint system. The default value is 256.</p>
<dt><code>omega-max-eqs</code></p>
<dd>The maximum number of equalities in an Omega constraint system. The default value is 128.</p>
<dt><code>omega-max-wild-cards</code></p>
<dd>The maximum number of wildcard variables that the Omega solver is able to insert. The default value is 18.</p>
<dt><code>omega-hash-table-size</code></p>
<dd>The size of the hash table in the Omega solver. The default value is 550.</p>
<dt><code>omega-max-keys</code></p>
<dd>The maximal number of keys used by the Omega solver. The default value is 500.</p>
<dt><code>omega-eliminate-redundant-constraints</code></p>
<dd>When set to 1, use expensive methods to eliminate all redundant constraints. The default value is 0.</p>
<dt><code>vect-max-version-for-alignment-checks</code></p>
<dd>The maximum number of run-time checks that can be performed when doing loop versioning for alignment in the vectorizer.</p>
<dt><code>vect-max-version-for-alias-checks</code></p>
<dd>The maximum number of run-time checks that can be performed when doing loop versioning for alias in the vectorizer.</p>
<dt><code>vect-max-peeling-for-alignment</code></p>
<dd>The maximum number of loop peels to enhance access alignment for vectorizer. Value -1 means &#8216;no limit&#8217;.</p>
<dt><code>max-iterations-to-track</code></p>
<dd>The maximum number of iterations of a loop the brute-force algorithm for analysis of the number of iterations of the loop tries to evaluate.</p>
<dt><code>hot-bb-count-ws-permille</code></p>
<dd>A basic block profile count is considered hot if it contributes to the given permillage (i.e. 0&#8230;1000) of the entire profiled execution.</p>
<dt><code>hot-bb-frequency-fraction</code></p>
<dd>Select fraction of the entry block frequency of executions of basic block in function given basic block needs to have to be considered hot.</p>
<dt><code>max-predicted-iterations</code></p>
<dd>The maximum number of loop iterations we predict statically. This is useful in cases where a function contains a single loop with known bound and another loop with unknown bound. The known number of iterations is predicted correctly, while the unknown number of iterations average to roughly 10. This means that the loop without bounds appears artificially cold relative to the other one.</p>
<dt><code>builtin-expect-probability</code></p>
<dd>Control the probability of the expression having the specified value. This parameter takes a percentage (i.e. 0 &#8230; 100) as input. The default probability of 90 is obtained empirically.</p>
<dt><code>align-threshold</code></p>
<dd>Select fraction of the maximal frequency of executions of a basic block in a function to align the basic block.</p>
<dt><code>align-loop-iterations</code></p>
<dd>A loop expected to iterate at least the selected number of iterations is aligned.</p>
<dt><code>tracer-dynamic-coverage</code></p>
<dd>
<dt><code>tracer-dynamic-coverage-feedback</code></p>
<dd>This value is used to limit superblock formation once the given percentage of executed instructions is covered. This limits unnecessary code size expansion. </p>
<p> The <code>tracer-dynamic-coverage-feedback</code> is used only when profile feedback is available. The real profiles (as opposed to statically estimated ones) are much less balanced allowing the threshold to be larger value.</p>
<dt><code>tracer-max-code-growth</code></p>
<dd>Stop tail duplication once code growth has reached given percentage. This is a rather artificial limit, as most of the duplicates are eliminated later in cross jumping, so it may be set to much higher values than is the desired code growth.</p>
<dt><code>tracer-min-branch-ratio</code></p>
<dd>Stop reverse growth when the reverse probability of best edge is less than this threshold (in percent).</p>
<dt><code>tracer-min-branch-ratio</code></p>
<dd>
<dt><code>tracer-min-branch-ratio-feedback</code></p>
<dd>Stop forward growth if the best edge has probability lower than this threshold. </p>
<p> Similarly to <code>tracer-dynamic-coverage</code> two values are present, one for compilation for profile feedback and one for compilation without. The value for compilation with profile feedback needs to be more conservative (higher) in order to make tracer effective.</p>
<dt><code>max-cse-path-length</code></p>
<dd>The maximum number of basic blocks on path that <font SIZE="-1">CSE</font> considers. The default is 10.</p>
<dt><code>max-cse-insns</code></p>
<dd>The maximum number of instructions <font SIZE="-1">CSE</font> processes before flushing. The default is 1000.</p>
<dt><code>ggc-min-expand</code></p>
<dd><font SIZE="-1">GCC</font> uses a garbage collector to manage its own memory allocation. This parameter specifies the minimum percentage by which the garbage collector&#8217;s heap should be allowed to expand between collections. Tuning this may improve compilation speed; it has no effect on code generation. </p>
<p> The default is 30% + 70% * (<font SIZE="-1">RAM/1GB</font>) with an upper bound of 100% when <font SIZE="-1">RAM </font>&gt;= 1GB. If <tt>&quot;getrlimit&quot;</tt> is available, the notion of &#8220;<font SIZE="-1">RAM&#8221;</font> is the smallest of actual <font SIZE="-1">RAM</font> and <tt>&quot;RLIMIT_DATA&quot;</tt> or <tt>&quot;RLIMIT_AS&quot;</tt>. If <font SIZE="-1">GCC</font> is not able to calculate <font SIZE="-1">RAM</font> on a particular platform, the lower bound of 30% is used. Setting this parameter and <code>ggc-min-heapsize</code> to zero causes a full collection to occur at every opportunity. This is extremely slow, but can be useful for debugging.</p>
<dt><code>ggc-min-heapsize</code></p>
<dd>Minimum size of the garbage collector&#8217;s heap before it begins bothering to collect garbage. The first collection occurs after the heap expands by <code>ggc-min-expand</code>% beyond <code>ggc-min-heapsize</code>. Again, tuning this may improve compilation speed, and has no effect on code generation. </p>
<p> The default is the smaller of <font SIZE="-1">RAM/8, RLIMIT_RSS,</font> or a limit that tries to ensure that <font SIZE="-1">RLIMIT_DATA</font> or <font SIZE="-1">RLIMIT_AS</font> are not exceeded, but with a lower bound of 4096 (four megabytes) and an upper bound of 131072 (128 megabytes). If <font SIZE="-1">GCC</font> is not able to calculate <font SIZE="-1">RAM</font> on a particular platform, the lower bound is used. Setting this parameter very large effectively disables garbage collection. Setting this parameter and <code>ggc-min-expand</code> to zero causes a full collection to occur at every opportunity.</p>
<dt><code>max-reload-search-insns</code></p>
<dd>The maximum number of instruction reload should look backward for equivalent register. Increasing values mean more aggressive optimization, making the compilation time increase with probably slightly better performance. The default value is 100.</p>
<dt><code>max-cselib-memory-locations</code></p>
<dd>The maximum number of memory locations cselib should take into account. Increasing values mean more aggressive optimization, making the compilation time increase with probably slightly better performance. The default value is 500.</p>
<dt><code>reorder-blocks-duplicate</code></p>
<dd>
<dt><code>reorder-blocks-duplicate-feedback</code></p>
<dd>Used by the basic block reordering pass to decide whether to use unconditional branch or duplicate the code on its destination. Code is duplicated when its estimated size is smaller than this value multiplied by the estimated size of unconditional jump in the hot spots of the program. </p>
<p> The <code>reorder-block-duplicate-feedback</code> is used only when profile feedback is available. It may be set to higher values than <code>reorder-block-duplicate</code> since information about the hot spots is more accurate.</p>
<dt><code>max-sched-ready-insns</code></p>
<dd>The maximum number of instructions ready to be issued the scheduler should consider at any given time during the first scheduling pass. Increasing values mean more thorough searches, making the compilation time increase with probably little benefit. The default value is 100.</p>
<dt><code>max-sched-region-blocks</code></p>
<dd>The maximum number of blocks in a region to be considered for interblock scheduling. The default value is 10.</p>
<dt><code>max-pipeline-region-blocks</code></p>
<dd>The maximum number of blocks in a region to be considered for pipelining in the selective scheduler. The default value is 15.</p>
<dt><code>max-sched-region-insns</code></p>
<dd>The maximum number of insns in a region to be considered for interblock scheduling. The default value is 100.</p>
<dt><code>max-pipeline-region-insns</code></p>
<dd>The maximum number of insns in a region to be considered for pipelining in the selective scheduler. The default value is 200.</p>
<dt><code>min-spec-prob</code></p>
<dd>The minimum probability (in percents) of reaching a source block for interblock speculative scheduling. The default value is 40.</p>
<dt><code>max-sched-extend-regions-iters</code></p>
<dd>The maximum number of iterations through <font SIZE="-1">CFG</font> to extend regions. A value of 0 (the default) disables region extensions.</p>
<dt><code>max-sched-insn-conflict-delay</code></p>
<dd>The maximum conflict delay for an insn to be considered for speculative motion. The default value is 3.</p>
<dt><code>sched-spec-prob-cutoff</code></p>
<dd>The minimal probability of speculation success (in percents), so that speculative insns are scheduled. The default value is 40.</p>
<dt><code>sched-spec-state-edge-prob-cutoff</code></p>
<dd>The minimum probability an edge must have for the scheduler to save its state across it. The default value is 10.</p>
<dt><code>sched-mem-true-dep-cost</code></p>
<dd>Minimal distance (in <font SIZE="-1">CPU</font> cycles) between store and load targeting same memory locations. The default value is 1.</p>
<dt><code>selsched-max-lookahead</code></p>
<dd>The maximum size of the lookahead window of selective scheduling. It is a depth of search for available instructions. The default value is 50.</p>
<dt><code>selsched-max-sched-times</code></p>
<dd>The maximum number of times that an instruction is scheduled during selective scheduling. This is the limit on the number of iterations through which the instruction may be pipelined. The default value is 2.</p>
<dt><code>selsched-max-insns-to-rename</code></p>
<dd>The maximum number of best instructions in the ready list that are considered for renaming in the selective scheduler. The default value is 2.</p>
<dt><code>sms-min-sc</code></p>
<dd>The minimum value of stage count that swing modulo scheduler generates. The default value is 2.</p>
<dt><code>max-last-value-rtl</code></p>
<dd>The maximum size measured as number of RTLs that can be recorded in an expression in combiner for a pseudo register as last known value of that register. The default is 10000.</p>
<dt><code>integer-share-limit</code></p>
<dd>Small integer constants can use a shared data structure, reducing the compiler&#8217;s memory usage and increasing its speed. This sets the maximum value of a shared integer constant. The default value is 256.</p>
<dt><code>ssp-buffer-size</code></p>
<dd>The minimum size of buffers (i.e. arrays) that receive stack smashing protection when <code>-fstack-protection</code> is used.</p>
<dt><code>min-size-for-stack-sharing</code></p>
<dd>The minimum size of variables taking part in stack slot sharing when not optimizing. The default value is 32.</p>
<dt><code>max-jump-thread-duplication-stmts</code></p>
<dd>Maximum number of statements allowed in a block that needs to be duplicated when threading jumps.</p>
<dt><code>max-fields-for-field-sensitive</code></p>
<dd>Maximum number of fields in a structure treated in a field sensitive manner during pointer analysis. The default is zero for <code>-O0</code> and <code>-O1</code>, and 100 for <code>-Os</code>, <code>-O2</code>, and <code>-O3</code>.</p>
<dt><code>prefetch-latency</code></p>
<dd>Estimate on average number of instructions that are executed before prefetch finishes. The distance prefetched ahead is proportional to this constant. Increasing this number may also lead to less streams being prefetched (see <code>simultaneous-prefetches</code>).</p>
<dt><code>simultaneous-prefetches</code></p>
<dd>Maximum number of prefetches that can run at the same time.</p>
<dt><code>l1-cache-line-size</code></p>
<dd>The size of cache line in L1 cache, in bytes.</p>
<dt><code>l1-cache-size</code></p>
<dd>The size of L1 cache, in kilobytes.</p>
<dt><code>l2-cache-size</code></p>
<dd>The size of L2 cache, in kilobytes.</p>
<dt><code>min-insn-to-prefetch-ratio</code></p>
<dd>The minimum ratio between the number of instructions and the number of prefetches to enable prefetching in a loop.</p>
<dt><code>prefetch-min-insn-to-mem-ratio</code></p>
<dd>The minimum ratio between the number of instructions and the number of memory references to enable prefetching in a loop.</p>
<dt><code>use-canonical-types</code></p>
<dd>Whether the compiler should use the &#8220;canonical&#8221; type system. By default, this should always be 1, which uses a more efficient internal mechanism for comparing types in C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font>. However, if bugs in the canonical type system are causing compilation failures, set this value to 0 to disable canonical types.</p>
<dt><code>switch-conversion-max-branch-ratio</code></p>
<dd>Switch initialization conversion refuses to create arrays that are bigger than <code>switch-conversion-max-branch-ratio</code> times the number of branches in the switch.</p>
<dt><code>max-partial-antic-length</code></p>
<dd>Maximum length of the partial antic set computed during the tree partial redundancy elimination optimization (<code>-ftree-pre</code>) when optimizing at <code>-O3</code> and above. For some sorts of source code the enhanced partial redundancy elimination optimization can run away, consuming all of the memory available on the host machine. This parameter sets a limit on the length of the sets that are computed, which prevents the runaway behavior. Setting a value of 0 for this parameter allows an unlimited set length.</p>
<dt><code>sccvn-max-scc-size</code></p>
<dd>Maximum size of a strongly connected component (<font SIZE="-1">SCC</font>) during <font SIZE="-1">SCCVN</font> processing. If this limit is hit, <font SIZE="-1">SCCVN</font> processing for the whole function is not done and optimizations depending on it are disabled. The default maximum <font SIZE="-1">SCC</font> size is 10000.</p>
<dt><code>sccvn-max-alias-queries-per-access</code></p>
<dd>Maximum number of alias-oracle queries we perform when looking for redundancies for loads and stores. If this limit is hit the search is aborted and the load or store is not considered redundant. The number of queries is algorithmically limited to the number of stores on all paths from the load to the function entry. The default maxmimum number of queries is 1000.</p>
<dt><code>ira-max-loops-num</code></p>
<dd><font SIZE="-1">IRA</font> uses regional register allocation by default. If a function contains more loops than the number given by this parameter, only at most the given number of the most frequently-executed loops form regions for regional register allocation. The default value of the parameter is 100.</p>
<dt><code>ira-max-conflict-table-size</code></p>
<dd>Although <font SIZE="-1">IRA</font> uses a sophisticated algorithm to compress the conflict table, the table can still require excessive amounts of memory for huge functions. If the conflict table for a function could be more than the size in <font SIZE="-1">MB</font> given by this parameter, the register allocator instead uses a faster, simpler, and lower-quality algorithm that does not require building a pseudo-register conflict table. The default value of the parameter is 2000.</p>
<dt><code>ira-loop-reserved-regs</code></p>
<dd><font SIZE="-1">IRA</font> can be used to evaluate more accurate register pressure in loops for decisions to move loop invariants (see <code>-O3</code>). The number of available registers reserved for some other purposes is given by this parameter. The default value of the parameter is 2, which is the minimal number of registers needed by typical instructions. This value is the best found from numerous experiments.</p>
<dt><code>loop-invariant-max-bbs-in-loop</code></p>
<dd>Loop invariant motion can be very expensive, both in compilation time and in amount of needed compile-time memory, with very large loops. Loops with more basic blocks than this parameter won&#8217;t have loop invariant motion optimization performed on them. The default value of the parameter is 1000 for <code>-O1</code> and 10000 for <code>-O2</code> and above.</p>
<dt><code>loop-max-datarefs-for-datadeps</code></p>
<dd>Building data dapendencies is expensive for very large loops. This parameter limits the number of data references in loops that are considered for data dependence analysis. These large loops are no handled by the optimizations using loop data dependencies. The default value is 1000.</p>
<dt><code>max-vartrack-size</code></p>
<dd>Sets a maximum number of hash table slots to use during variable tracking dataflow analysis of any function. If this limit is exceeded with variable tracking at assignments enabled, analysis for that function is retried without it, after removing all debug insns from the function. If the limit is exceeded even without debug insns, var tracking analysis is completely disabled for the function. Setting the parameter to zero makes it unlimited.</p>
<dt><code>max-vartrack-expr-depth</code></p>
<dd>Sets a maximum number of recursion levels when attempting to map variable names or debug temporaries to value expressions. This trades compilation time for more complete debug information. If this is set too low, value expressions that are available and could be represented in debug information may end up not being used; setting this higher may enable the compiler to find more complex debug expressions, but compile time and memory use may grow. The default is 12.</p>
<dt><code>min-nondebug-insn-uid</code></p>
<dd>Use uids starting at this parameter for nondebug insns. The range below the parameter is reserved exclusively for debug insns created by <code>-fvar-tracking-assignments</code>, but debug insns may get (non-overlapping) uids above it if the reserved range is exhausted.</p>
<dt><code>ipa-sra-ptr-growth-factor</code></p>
<dd>IPA-SRA replaces a pointer to an aggregate with one or more new parameters only when their cumulative size is less or equal to <code>ipa-sra-ptr-growth-factor</code> times the size of the original pointer parameter.</p>
<dt><code>tm-max-aggregate-size</code></p>
<dd>When making copies of thread-local variables in a transaction, this parameter specifies the size in bytes after which variables are saved with the logging functions as opposed to save/restore code sequence pairs. This option only applies when using <code>-fgnu-tm</code>.</p>
<dt><code>graphite-max-nb-scop-params</code></p>
<dd>To avoid exponential effects in the Graphite loop transforms, the number of parameters in a Static Control Part (SCoP) is bounded. The default value is 10 parameters. A variable whose value is unknown at compilation time and defined outside a SCoP is a parameter of the SCoP.</p>
<dt><code>graphite-max-bbs-per-function</code></p>
<dd>To avoid exponential effects in the detection of SCoPs, the size of the functions analyzed by Graphite is bounded. The default value is 100 basic blocks.</p>
<dt><code>loop-block-tile-size</code></p>
<dd>Loop blocking or strip mining transforms, enabled with <code>-floop-block</code> or <code>-floop-strip-mine</code>, strip mine each loop in the loop nest by a given number of iterations. The strip length can be changed using the <code>loop-block-tile-size</code> parameter. The default value is 51 iterations.</p>
<dt><code>ipa-cp-value-list-size</code></p>
<dd>IPA-CP attempts to track all possible values and types passed to a function&#8217;s parameter in order to propagate them and perform devirtualization. <code>ipa-cp-value-list-size</code> is the maximum number of values and types it stores per one formal parameter of a function.</p>
<dt><code>ipa-cp-eval-threshold</code></p>
<dd>IPA-CP calculates its own score of cloning profitability heuristics and performs those cloning opportunities with scores that exceed <code>ipa-cp-eval-threshold</code>.</p>
<dt><code>ipa-max-agg-items</code></p>
<dd>IPA-CP is also capable to propagate a number of scalar values passed in an aggregate. <code>ipa-max-agg-items</code> controls the maximum number of such values per one parameter.</p>
<dt><code>ipa-cp-loop-hint-bonus</code></p>
<dd>When IPA-CP determines that a cloning candidate would make the number of iterations of a loop known, it adds a bonus of <code>ipa-cp-loop-hint-bonus</code> bonus to the profitability score of the candidate.</p>
<dt><code>ipa-cp-array-index-hint-bonus</code></p>
<dd>When IPA-CP determines that a cloning candidate would make the index of an array access known, it adds a bonus of <code>ipa-cp-array-index-hint-bonus</code> bonus to the profitability score of the candidate.</p>
<dt><code>lto-partitions</code></p>
<dd>Specify desired number of partitions produced during <font SIZE="-1">WHOPR</font> compilation. The number of partitions should exceed the number of CPUs used for compilation. The default value is 32.</p>
<dt><code>lto-minpartition</code></p>
<dd>Size of minimal partition for <font SIZE="-1">WHOPR </font>(in estimated instructions). This prevents expenses of splitting very small programs into too many partitions.</p>
<dt><code>cxx-max-namespaces-for-diagnostic-help</code></p>
<dd>The maximum number of namespaces to consult for suggestions when C<font SIZE="-2">++</font> name lookup fails for an identifier. The default is 1000.</p>
<dt><code>sink-frequency-threshold</code></p>
<dd>The maximum relative execution frequency (in percents) of the target block relative to a statement&#8217;s original block to allow statement sinking of a statement. Larger numbers result in more aggressive statement sinking. The default value is 75. A small positive adjustment is applied for statements with memory operands as those are even more profitable so sink.</p>
<dt><code>max-stores-to-sink</code></p>
<dd>The maximum number of conditional stores paires that can be sunk. Set to 0 if either vectorization (<code>-ftree-vectorize</code>) or if-conversion (<code>-ftree-loop-if-convert</code>) is disabled. The default is 2.</p>
<dt><code>allow-load-data-races</code></p>
<dd>Allow optimizers to introduce new data races on loads. Set to 1 to allow, otherwise to 0. This option is enabled by default unless implicitly set by the <code>-fmemory-model=</code> option.</p>
<dt><code>allow-store-data-races</code></p>
<dd>Allow optimizers to introduce new data races on stores. Set to 1 to allow, otherwise to 0. This option is enabled by default unless implicitly set by the <code>-fmemory-model=</code> option.</p>
<dt><code>allow-packed-load-data-races</code></p>
<dd>Allow optimizers to introduce new data races on packed data loads. Set to 1 to allow, otherwise to 0. This option is enabled by default unless implicitly set by the <code>-fmemory-model=</code> option.</p>
<dt><code>allow-packed-store-data-races</code></p>
<dd>Allow optimizers to introduce new data races on packed data stores. Set to 1 to allow, otherwise to 0. This option is enabled by default unless implicitly set by the <code>-fmemory-model=</code> option.</p>
<dt><code>case-values-threshold</code></p>
<dd>The smallest number of different values for which it is best to use a jump-table instead of a tree of conditional branches. If the value is 0, use the default for the machine. The default is 0.</p>
<dt><code>tree-reassoc-width</code></p>
<dd>Set the maximum number of instructions executed in parallel in reassociated tree. This parameter overrides target dependent heuristics used by default if has non zero value.</p>
<dt><code>sched-pressure-algorithm</code></p>
<dd>Choose between the two available implementations of <code>-fsched-pressure</code>. Algorithm 1 is the original implementation and is the more likely to prevent instructions from being reordered. Algorithm 2 was designed to be a compromise between the relatively conservative approach taken by algorithm 1 and the rather aggressive approach taken by the default scheduler. It relies more heavily on having a regular register file and accurate register pressure classes. See <i>haifa-sched.c</i> in the <font SIZE="-1">GCC</font> sources for more details. </p>
<p> The default choice depends on the target.</p>
<dt><code>max-slsr-cand-scan</code></p>
<dd>Set the maximum number of existing candidates that will be considered when seeking a basis for a new straight-line strength reduction candidate.</p>
<dt><code>asan-globals</code></p>
<dd>Enable buffer overflow detection for global objects. This kind of protection is enabled by default if you are using <code>-fsanitize=address</code> option. To disable global objects protection use <code>&#8211;param asan-globals=0</code>.</p>
<dt><code>asan-stack</code></p>
<dd>Enable buffer overflow detection for stack objects. This kind of protection is enabled by default when using<code>-fsanitize=address</code>. To disable stack protection use <code>&#8211;param asan-stack=0</code> option.</p>
<dt><code>asan-instrument-reads</code></p>
<dd>Enable buffer overflow detection for memory reads. This kind of protection is enabled by default when using <code>-fsanitize=address</code>. To disable memory reads protection use <code>&#8211;param asan-instrument-reads=0</code>.</p>
<dt><code>asan-instrument-writes</code></p>
<dd>Enable buffer overflow detection for memory writes. This kind of protection is enabled by default when using <code>-fsanitize=address</code>. To disable memory writes protection use <code>&#8211;param asan-instrument-writes=0</code> option.</p>
<dt><code>asan-memintrin</code></p>
<dd>Enable detection for built-in functions. This kind of protection is enabled by default when using <code>-fsanitize=address</code>. To disable built-in functions protection use <code>&#8211;param asan-memintrin=0</code>.</p>
<dt><code>asan-use-after-return</code></p>
<dd>Enable detection of use-after-return. This kind of protection is enabled by default when using <code>-fsanitize=address</code> option. To disable use-after-return detection use <code>&#8211;param asan-use-after-return=0</code>.</p>
<dt><code>asan-instrumentation-with-call-threshold</code></p>
<dd>If number of memory accesses in function being instrumented is greater or equal to this number, use callbacks instead of inline checks. E.g. to disable inline code use <code>&#8211;param asan-instrumentation-with-call-threshold=0</code>.</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>Options Controlling the Preprocessor</h3>
<p>These options control the C preprocessor, which is run on each C source file before actual compilation. </p>
<p> If you use the <code>-E</code> option, nothing is done except preprocessing. Some of these options make sense only together with <code>-E</code> because they cause the preprocessor output to be unsuitable for actual compilation.</p>
<dl COMPACT>
<dt><code>-Wp,</code><i>option</i></p>
<dd>You can use <code>-Wp,</code><i>option</i> to bypass the compiler driver and pass <i>option</i> directly through to the preprocessor. If <i>option</i> contains commas, it is split into multiple options at the commas. However, many options are modified, translated or interpreted by the compiler driver before being passed to the preprocessor, and <code>-Wp</code> forcibly bypasses this phase. The preprocessor&#8217;s direct interface is undocumented and subject to change, so whenever possible you should avoid using <code>-Wp</code> and let the driver handle the options instead.</p>
<dt><code>-Xpreprocessor</code> <i>option</i></p>
<dd>Pass <i>option</i> as an option to the preprocessor. You can use this to supply system-specific preprocessor options that <font SIZE="-1">GCC</font> does not recognize. </p>
<p> If you want to pass an option that takes an argument, you must use <code>-Xpreprocessor</code> twice, once for the option and once for the argument.</p>
<dt><code>-no-integrated-cpp</code></p>
<dd>Perform preprocessing as a separate pass before compilation. By default, <font SIZE="-1">GCC</font> performs preprocessing as an integrated part of input tokenization and parsing. If this option is provided, the appropriate language front end (<code>cc1</code>, <code>cc1plus</code>, or <code>cc1obj</code> for C, C<font SIZE="-2">++</font>, and Objective-C, respectively) is instead invoked twice, once for preprocessing only and once for actual compilation of the preprocessed input. This option may be useful in conjunction with the <code>-B</code> or <code>-wrapper</code> options to specify an alternate preprocessor or perform additional processing of the program source between normal preprocessing and compilation.</p>
<dt><code>-D</code> <i>name</i></p>
<dd>Predefine <i>name</i> as a macro, with definition <tt>1</tt>.</p>
<dt><code>-D</code> <i>name</i><code>=</code><i>definition</i></p>
<dd>The contents of <i>definition</i> are tokenized and processed as if they appeared during translation phase three in a <code>#define</code> directive. In particular, the definition will be truncated by embedded newline characters. </p>
<p> If you are invoking the preprocessor from a shell or shell-like program you may need to use the shell&#8217;s quoting syntax to protect characters such as spaces that have a meaning in the shell syntax. </p>
<p> If you wish to define a function-like macro on the command line, write its argument list with surrounding parentheses before the equals sign (if any). Parentheses are meaningful to most shells, so you will need to quote the option. With <code>sh</code> and <code>csh</code>, <code>-D&#8217;</code><i>name</i><code>(</code><i>args&#8230;</i><code>)=</code><i>definition</i><code>&#8216;</code> works. </p>
<p> <code>-D</code> and <code>-U</code> options are processed in the order they are given on the command line. All <code>-imacros</code> <i>file</i> and <code>-include</code> <i>file</i> options are processed after all <code>-D</code> and <code>-U</code> options.</p>
<dt><code>-U</code> <i>name</i></p>
<dd>Cancel any previous definition of <i>name</i>, either built in or provided with a <code>-D</code> option.</p>
<dt><code>-undef</code></p>
<dd>Do not predefine any system-specific or GCC-specific macros. The standard predefined macros remain defined.</p>
<dt><code>-I</code> <i>dir</i></p>
<dd>Add the directory <i>dir</i> to the list of directories to be searched for header files. Directories named by <code>-I</code> are searched before the standard system include directories. If the directory <i>dir</i> is a standard system include directory, the option is ignored to ensure that the default search order for system directories and the special treatment of system headers are not defeated . If <i>dir</i> begins with <tt>&quot;=&quot;</tt>, then the <tt>&quot;=&quot;</tt> will be replaced by the sysroot prefix; see <code>&#8211;sysroot</code> and <code>-isysroot</code>.</p>
<dt><code>-o</code> <i>file</i></p>
<dd>Write output to <i>file</i>. This is the same as specifying <i>file</i> as the second non-option argument to <code>cpp</code>. <code>gcc</code> has a different interpretation of a second non-option argument, so you must use <code>-o</code> to specify the output file.</p>
<dt><code>-Wall</code></p>
<dd>Turns on all optional warnings which are desirable for normal code. At present this is <code>-Wcomment</code>, <code>-Wtrigraphs</code>, <code>-Wmultichar</code> and a warning about integer promotion causing a change of sign in <tt>&quot;#if&quot;</tt> expressions. Note that many of the preprocessor&#8217;s warnings are on by default and have no options to control them.</p>
<dt><code>-Wcomment</code></p>
<dd>
<dt><code>-Wcomments</code></p>
<dd>Warn whenever a comment-start sequence <code>/*</code> appears in a <code>/*</code> comment, or whenever a backslash-newline appears in a <code>//</code> comment. (Both forms have the same effect.)</p>
<dt><code>-Wtrigraphs</code></p>
<dd>Most trigraphs in comments cannot affect the meaning of the program. However, a trigraph that would form an escaped newline (<code>??/</code> at the end of a line) can, by changing where the comment begins or ends. Therefore, only trigraphs that would form escaped newlines produce warnings inside a comment. </p>
<p> This option is implied by <code>-Wall</code>. If <code>-Wall</code> is not given, this option is still enabled unless trigraphs are enabled. To get trigraph conversion without warnings, but get the other <code>-Wall</code> warnings, use <code>-trigraphs -Wall -Wno-trigraphs</code>.</p>
<dt><code>-Wtraditional</code></p>
<dd>Warn about certain constructs that behave differently in traditional and <font SIZE="-1">ISO C. </font> Also warn about <font SIZE="-1">ISO C</font> constructs that have no traditional C equivalent, and problematic constructs which should be avoided.</p>
<dt><code>-Wundef</code></p>
<dd>Warn whenever an identifier which is not a macro is encountered in an <code>#if</code> directive, outside of <code>defined</code>. Such identifiers are replaced with zero.</p>
<dt><code>-Wunused-macros</code></p>
<dd>Warn about macros defined in the main file that are unused. A macro is <i>used</i> if it is expanded or tested for existence at least once. The preprocessor will also warn if the macro has not been used at the time it is redefined or undefined. </p>
<p> Built-in macros, macros defined on the command line, and macros defined in include files are not warned about. </p>
<p> <i>Note:</i> If a macro is actually used, but only used in skipped conditional blocks, then <font SIZE="-1">CPP</font> will report it as unused. To avoid the warning in such a case, you might improve the scope of the macro&#8217;s definition by, for example, moving it into the first skipped block. Alternatively, you could provide a dummy use with something like: </p>
<pre> #if defined the_macro_causing_the_warning
 #endif</pre>
<dt><code>-Wendif-labels</code></p>
<dd>Warn whenever an <code>#else</code> or an <code>#endif</code> are followed by text. This usually happens in code of the form </p>
<pre> #if FOO
 ...
 #else FOO
 ...
 #endif FOO</pre>
<p>The second and third <tt>&quot;FOO&quot;</tt> should be in comments, but often are not in older programs. This warning is on by default.</p>
<dt><code>-Werror</code></p>
<dd>Make all warnings into hard errors. Source code which triggers warnings will be rejected.</p>
<dt><code>-Wsystem-headers</code></p>
<dd>Issue warnings for code in system headers. These are normally unhelpful in finding bugs in your own code, therefore suppressed. If you are responsible for the system library, you may want to see them.</p>
<dt><code>-w</code></p>
<dd>Suppress all warnings, including those which <font SIZE="-1">GNU CPP</font> issues by default.</p>
<dt><code>-pedantic</code></p>
<dd>Issue all the mandatory diagnostics listed in the C standard. Some of them are left out by default, since they trigger frequently on harmless code.</p>
<dt><code>-pedantic-errors</code></p>
<dd>Issue all the mandatory diagnostics, and make all mandatory diagnostics into errors. This includes mandatory diagnostics that <font SIZE="-1">GCC</font> issues without <code>-pedantic</code> but treats as warnings.</p>
<dt><code>-M</code></p>
<dd>Instead of outputting the result of preprocessing, output a rule suitable for <code>make</code> describing the dependencies of the main source file. The preprocessor outputs one <code>make</code> rule containing the object file name for that source file, a colon, and the names of all the included files, including those coming from <code>-include</code> or <code>-imacros</code> command line options. </p>
<p> Unless specified explicitly (with <code>-MT</code> or <code>-MQ</code>), the object file name consists of the name of the source file with any suffix replaced with object file suffix and with any leading directory parts removed. If there are many included files then the rule is split into several lines using <code>\</code>-newline. The rule has no commands. </p>
<p> This option does not suppress the preprocessor&#8217;s debug output, such as <code>-dM</code>. To avoid mixing such debug output with the dependency rules you should explicitly specify the dependency output file with <code>-MF</code>, or use an environment variable like <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font>. Debug output will still be sent to the regular output stream as normal. </p>
<p> Passing <code>-M</code> to the driver implies <code>-E</code>, and suppresses warnings with an implicit <code>-w</code>.</p>
<dt><code>-MM</code></p>
<dd>Like <code>-M</code> but do not mention header files that are found in system header directories, nor header files that are included, directly or indirectly, from such a header. </p>
<p> This implies that the choice of angle brackets or double quotes in an <code>#include</code> directive does not in itself determine whether that header will appear in <code>-MM</code> dependency output. This is a slight change in semantics from <font SIZE="-1">GCC</font> versions 3.0 and earlier.</p>
<dt><code>-MF</code> <i>file</i></p>
<dd>When used with <code>-M</code> or <code>-MM</code>, specifies a file to write the dependencies to. If no <code>-MF</code> switch is given the preprocessor sends the rules to the same place it would have sent preprocessed output. </p>
<p> When used with the driver options <code>-MD</code> or <code>-MMD</code>, <code>-MF</code> overrides the default dependency output file.</p>
<dt><code>-MG</code></p>
<dd>In conjunction with an option such as <code>-M</code> requesting dependency generation, <code>-MG</code> assumes missing header files are generated files and adds them to the dependency list without raising an error. The dependency filename is taken directly from the <tt>&quot;#include&quot;</tt> directive without prepending any path. <code>-MG</code> also suppresses preprocessed output, as a missing header file renders this useless. </p>
<p> This feature is used in automatic updating of makefiles.</p>
<dt><code>-MP</code></p>
<dd>This option instructs <font SIZE="-1">CPP</font> to add a phony target for each dependency other than the main file, causing each to depend on nothing. These dummy rules work around errors <code>make</code> gives if you remove header files without updating the <i>Makefile</i> to match. </p>
<p> This is typical output: </p>
<pre> test.o: test.c test.h
 
 test.h:</pre>
<dt><code>-MT</code> <i>target</i></p>
<dd>Change the target of the rule emitted by dependency generation. By default <font SIZE="-1">CPP</font> takes the name of the main input file, deletes any directory components and any file suffix such as <code>.c</code>, and appends the platform&#8217;s usual object suffix. The result is the target. </p>
<p> An <code>-MT</code> option will set the target to be exactly the string you specify. If you want multiple targets, you can specify them as a single argument to <code>-MT</code>, or use multiple <code>-MT</code> options. </p>
<p> For example, <code>-MT&nbsp;<wbr>&#8216;$(objpfx)foo.o&#8217;</code> might give </p>
<pre> $(objpfx)foo.o: foo.c</pre>
<dt><code>-MQ</code> <i>target</i></p>
<dd>Same as <code>-MT</code>, but it quotes any characters which are special to Make. <code>-MQ&nbsp;<wbr>&#8216;$(objpfx)foo.o&#8217;</code> gives </p>
<pre> $$(objpfx)foo.o: foo.c</pre>
<p>The default target is automatically quoted, as if it were given with <code>-MQ</code>.</p>
<dt><code>-MD</code></p>
<dd><code>-MD</code> is equivalent to <code>-M -MF</code> <i>file</i>, except that <code>-E</code> is not implied. The driver determines <i>file</i> based on whether an <code>-o</code> option is given. If it is, the driver uses its argument but with a suffix of <i>.d</i>, otherwise it takes the name of the input file, removes any directory components and suffix, and applies a <i>.d</i> suffix. </p>
<p> If <code>-MD</code> is used in conjunction with <code>-E</code>, any <code>-o</code> switch is understood to specify the dependency output file, but if used without <code>-E</code>, each <code>-o</code> is understood to specify a target object file. </p>
<p> Since <code>-E</code> is not implied, <code>-MD</code> can be used to generate a dependency output file as a side-effect of the compilation process.</p>
<dt><code>-MMD</code></p>
<dd>Like <code>-MD</code> except mention only user header files, not system header files.</p>
<dt><code>-fpch-deps</code></p>
<dd>When using precompiled headers, this flag will cause the dependency-output flags to also list the files from the precompiled header&#8217;s dependencies. If not specified only the precompiled header would be listed and not the files that were used to create it because those files are not consulted when a precompiled header is used.</p>
<dt><code>-fpch-preprocess</code></p>
<dd>This option allows use of a precompiled header together with <code>-E</code>. It inserts a special <tt>&quot;#pragma&quot;</tt>, <tt>&quot;#pragma GCC pch_preprocess &quot;</tt>filename<tt>&quot;&quot;</tt> in the output to mark the place where the precompiled header was found, and its <i>filename</i>. When <code>-fpreprocessed</code> is in use, <font SIZE="-1">GCC</font> recognizes this <tt>&quot;#pragma&quot;</tt> and loads the <font SIZE="-1">PCH.</font> </p>
<p> This option is off by default, because the resulting preprocessed output is only really suitable as input to <font SIZE="-1">GCC. </font> It is switched on by <code>-save-temps</code>. </p>
<p> You should not write this <tt>&quot;#pragma&quot;</tt> in your own code, but it is safe to edit the filename if the <font SIZE="-1">PCH</font> file is available in a different location. The filename may be absolute or it may be relative to <font SIZE="-1">GCC</font>&#8216;s current directory.</p>
<dt><code>-x c</code></p>
<dd>
<dt><code>-x c++</code></p>
<dd>
<dt><code>-x objective-c</code></p>
<dd>
<dt><code>-x assembler-with-cpp</code></p>
<dd>Specify the source language: C, C<font SIZE="-2">++</font>, Objective-C, or assembly. This has nothing to do with standards conformance or extensions; it merely selects which base syntax to expect. If you give none of these options, cpp will deduce the language from the extension of the source file: <code>.c</code>, <code>.cc</code>, <code>.m</code>, or <code>.S</code>. Some other common extensions for C<font SIZE="-2">++</font> and assembly are also recognized. If cpp does not recognize the extension, it will treat the file as C; this is the most generic mode. </p>
<p> <i>Note:</i> Previous versions of cpp accepted a <code>-lang</code> option which selected both the language and the standards conformance level. This option has been removed, because it conflicts with the <code>-l</code> option.</p>
<dt><code>-std=</code><i>standard</i></p>
<dd>
<dt><code>-ansi</code></p>
<dd>Specify the standard to which the code should conform. Currently <font SIZE="-1">CPP</font> knows about C and C<font SIZE="-2">++</font> standards; others may be added in the future. </p>
<p> <i>standard</i> may be one of:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&quot;c90&quot;</p>
<dd>
<dt>&quot;c89&quot;</p>
<dd>
<dt>&quot;iso9899:1990&quot;</p>
<dd>The <font SIZE="-1">ISO C</font> standard from 1990. <code>c90</code> is the customary shorthand for this version of the standard. </p>
<p> The <code>-ansi</code> option is equivalent to <code>-std=c90</code>.</p>
<dt>&quot;iso9899:199409&quot;</p>
<dd>The 1990 C standard, as amended in 1994.</p>
<dt>&quot;iso9899:1999&quot;</p>
<dd>
<dt>&quot;c99&quot;</p>
<dd>
<dt>&quot;iso9899:199x&quot;</p>
<dd>
<dt>&quot;c9x&quot;</p>
<dd>The revised <font SIZE="-1">ISO C</font> standard, published in December 1999. Before publication, this was known as C9X.</p>
<dt>&quot;iso9899:2011&quot;</p>
<dd>
<dt>&quot;c11&quot;</p>
<dd>
<dt>&quot;c1x&quot;</p>
<dd>The revised <font SIZE="-1">ISO C</font> standard, published in December 2011. Before publication, this was known as C1X.</p>
<dt>&quot;gnu90&quot;</p>
<dd>
<dt>&quot;gnu89&quot;</p>
<dd>The 1990 C standard plus <font SIZE="-1">GNU</font> extensions. This is the default.</p>
<dt>&quot;gnu99&quot;</p>
<dd>
<dt>&quot;gnu9x&quot;</p>
<dd>The 1999 C standard plus <font SIZE="-1">GNU</font> extensions.</p>
<dt>&quot;gnu11&quot;</p>
<dd>
<dt>&quot;gnu1x&quot;</p>
<dd>The 2011 C standard plus <font SIZE="-1">GNU</font> extensions.</p>
<dt>&quot;c++98&quot;</p>
<dd>The 1998 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus amendments.</p>
<dt>&quot;gnu++98&quot;</p>
<dd>The same as <code>-std=c++98</code> plus <font SIZE="-1">GNU</font> extensions. This is the default for C<font SIZE="-2">++</font> code.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-I-</code></p>
<dd>Split the include path. Any directories specified with <code>-I</code> options before <code>-I-</code> are searched only for headers requested with <tt>&quot;#include&nbsp;<wbr>&quot;</tt>file<tt>&quot;&quot;</tt>; they are not searched for <tt>&quot;#include&nbsp;<wbr>&lt;</tt>file<tt>&gt;&quot;</tt>. If additional directories are specified with <code>-I</code> options after the <code>-I-</code>, those directories are searched for all <code>#include</code> directives. </p>
<p> In addition, <code>-I-</code> inhibits the use of the directory of the current file directory as the first search directory for <tt>&quot;#include&nbsp;<wbr>&quot;</tt>file<tt>&quot;&quot;</tt>. This option has been deprecated.</p>
<dt><code>-nostdinc</code></p>
<dd>Do not search the standard system directories for header files. Only the directories you have specified with <code>-I</code> options (and the directory of the current file, if appropriate) are searched.</p>
<dt><code>-nostdinc++</code></p>
<dd>Do not search for header files in the C<font SIZE="-2">++</font>-specific standard directories, but do still search the other standard directories. (This option is used when building the C<font SIZE="-2">++</font> library.)</p>
<dt><code>-include</code> <i>file</i></p>
<dd>Process <i>file</i> as if <tt>&quot;#include &quot;file&quot;&quot;</tt> appeared as the first line of the primary source file. However, the first directory searched for <i>file</i> is the preprocessor&#8217;s working directory <i>instead of</i> the directory containing the main source file. If not found there, it is searched for in the remainder of the <tt>&quot;#include &quot;...&quot;&quot;</tt> search chain as normal. </p>
<p> If multiple <code>-include</code> options are given, the files are included in the order they appear on the command line.</p>
<dt><code>-imacros</code> <i>file</i></p>
<dd>Exactly like <code>-include</code>, except that any output produced by scanning <i>file</i> is thrown away. Macros it defines remain defined. This allows you to acquire all the macros from a header without also processing its declarations. </p>
<p> All files specified by <code>-imacros</code> are processed before all files specified by <code>-include</code>.</p>
<dt><code>-idirafter</code> <i>dir</i></p>
<dd>Search <i>dir</i> for header files, but do it <i>after</i> all directories specified with <code>-I</code> and the standard system directories have been exhausted. <i>dir</i> is treated as a system include directory. If <i>dir</i> begins with <tt>&quot;=&quot;</tt>, then the <tt>&quot;=&quot;</tt> will be replaced by the sysroot prefix; see <code>&#8211;sysroot</code> and <code>-isysroot</code>.</p>
<dt><code>-iprefix</code> <i>prefix</i></p>
<dd>Specify <i>prefix</i> as the prefix for subsequent <code>-iwithprefix</code> options. If the prefix represents a directory, you should include the final <code>/</code>.</p>
<dt><code>-iwithprefix</code> <i>dir</i></p>
<dd>
<dt><code>-iwithprefixbefore</code> <i>dir</i></p>
<dd>Append <i>dir</i> to the prefix specified previously with <code>-iprefix</code>, and add the resulting directory to the include search path. <code>-iwithprefixbefore</code> puts it in the same place <code>-I</code> would; <code>-iwithprefix</code> puts it where <code>-idirafter</code> would.</p>
<dt><code>-isysroot</code> <i>dir</i></p>
<dd>This option is like the <code>&#8211;sysroot</code> option, but applies only to header files (except for Darwin targets, where it applies to both header files and libraries). See the <code>&#8211;sysroot</code> option for more information.</p>
<dt><code>-imultilib</code> <i>dir</i></p>
<dd>Use <i>dir</i> as a subdirectory of the directory containing target-specific C<font SIZE="-2">++</font> headers.</p>
<dt><code>-isystem</code> <i>dir</i></p>
<dd>Search <i>dir</i> for header files, after all directories specified by <code>-I</code> but before the standard system directories. Mark it as a system directory, so that it gets the same special treatment as is applied to the standard system directories. If <i>dir</i> begins with <tt>&quot;=&quot;</tt>, then the <tt>&quot;=&quot;</tt> will be replaced by the sysroot prefix; see <code>&#8211;sysroot</code> and <code>-isysroot</code>.</p>
<dt><code>-iquote</code> <i>dir</i></p>
<dd>Search <i>dir</i> only for header files requested with <tt>&quot;#include&nbsp;<wbr>&quot;</tt>file<tt>&quot;&quot;</tt>; they are not searched for <tt>&quot;#include&nbsp;<wbr>&lt;</tt>file<tt>&gt;&quot;</tt>, before all directories specified by <code>-I</code> and before the standard system directories. If <i>dir</i> begins with <tt>&quot;=&quot;</tt>, then the <tt>&quot;=&quot;</tt> will be replaced by the sysroot prefix; see <code>&#8211;sysroot</code> and <code>-isysroot</code>.</p>
<dt><code>-fdirectives-only</code></p>
<dd>When preprocessing, handle directives, but do not expand macros. </p>
<p> The option&#8217;s behavior depends on the <code>-E</code> and <code>-fpreprocessed</code> options. </p>
<p> With <code>-E</code>, preprocessing is limited to the handling of directives such as <tt>&quot;#define&quot;</tt>, <tt>&quot;#ifdef&quot;</tt>, and <tt>&quot;#error&quot;</tt>. Other preprocessor operations, such as macro expansion and trigraph conversion are not performed. In addition, the <code>-dD</code> option is implicitly enabled. </p>
<p> With <code>-fpreprocessed</code>, predefinition of command line and most builtin macros is disabled. Macros such as <tt>&quot;__LINE__&quot;</tt>, which are contextually dependent, are handled normally. This enables compilation of files previously preprocessed with <tt>&quot;-E -fdirectives-only&quot;</tt>. </p>
<p> With both <code>-E</code> and <code>-fpreprocessed</code>, the rules for <code>-fpreprocessed</code> take precedence. This enables full preprocessing of files previously preprocessed with <tt>&quot;-E -fdirectives-only&quot;</tt>.</p>
<dt><code>-fdollars-in-identifiers</code></p>
<dd>Accept <code>$</code> in identifiers.</p>
<dt><code>-fextended-identifiers</code></p>
<dd>Accept universal character names in identifiers. This option is experimental; in a future version of <font SIZE="-1">GCC,</font> it will be enabled by default for C99 and C<font SIZE="-2">++</font>.</p>
<dt><code>-fno-canonical-system-headers</code></p>
<dd>When preprocessing, do not shorten system header paths with canonicalization.</p>
<dt><code>-fpreprocessed</code></p>
<dd>Indicate to the preprocessor that the input file has already been preprocessed. This suppresses things like macro expansion, trigraph conversion, escaped newline splicing, and processing of most directives. The preprocessor still recognizes and removes comments, so that you can pass a file preprocessed with <code>-C</code> to the compiler without problems. In this mode the integrated preprocessor is little more than a tokenizer for the front ends. </p>
<p> <code>-fpreprocessed</code> is implicit if the input file has one of the extensions <code>.i</code>, <code>.ii</code> or <code>.mi</code>. These are the extensions that <font SIZE="-1">GCC</font> uses for preprocessed files created by <code>-save-temps</code>.</p>
<dt><code>-ftabstop=</code><i>width</i></p>
<dd>Set the distance between tab stops. This helps the preprocessor report correct column numbers in warnings or errors, even if tabs appear on the line. If the value is less than 1 or greater than 100, the option is ignored. The default is 8.</p>
<dt><code>-fdebug-cpp</code></p>
<dd>This option is only useful for debugging <font SIZE="-1">GCC. </font> When used with <code>-E</code>, dumps debugging information about location maps. Every token in the output is preceded by the dump of the map its location belongs to. The dump of the map holding the location of a token would be: </p>
<pre> {&quot;P&quot;:F&lt;/file/path&gt;;&quot;F&quot;:F&lt;/includer/path&gt;;&quot;L&quot;:&lt;line_num&gt;;&quot;C&quot;:&lt;col_num&gt;;&quot;S&quot;:&lt;system_header_p&gt;;&quot;M&quot;:&lt;map_address&gt;;&quot;E&quot;:&lt;macro_expansion_p&gt;,&quot;loc&quot;:&lt;location&gt;}</pre>
<p>When used without <code>-E</code>, this option has no effect.</p>
<dt><code>-ftrack-macro-expansion</code>[<code>=</code><i>level</i>]</p>
<dd>Track locations of tokens across macro expansions. This allows the compiler to emit diagnostic about the current macro expansion stack when a compilation error occurs in a macro expansion. Using this option makes the preprocessor and the compiler consume more memory. The <i>level</i> parameter can be used to choose the level of precision of token location tracking thus decreasing the memory consumption if necessary. Value <code>0</code> of <i>level</i> de-activates this option just as if no <code>-ftrack-macro-expansion</code> was present on the command line. Value <code>1</code> tracks tokens locations in a degraded mode for the sake of minimal memory overhead. In this mode all tokens resulting from the expansion of an argument of a function-like macro have the same location. Value <code>2</code> tracks tokens locations completely. This value is the most memory hungry. When this option is given no argument, the default parameter value is <code>2</code>. </p>
<p> Note that -ftrack-macro-expansion=2 is activated by default.</p>
<dt><code>-fexec-charset=</code><i>charset</i></p>
<dd>Set the execution character set, used for string and character constants. The default is <font SIZE="-1">UTF-8. </font><i>charset</i> can be any encoding supported by the system&#8217;s <tt>&quot;iconv&quot;</tt> library routine.</p>
<dt><code>-fwide-exec-charset=</code><i>charset</i></p>
<dd>Set the wide execution character set, used for wide string and character constants. The default is <font SIZE="-1">UTF-32</font> or <font SIZE="-1">UTF-16,</font> whichever corresponds to the width of <tt>&quot;wchar_t&quot;</tt>. As with <code>-fexec-charset</code>, <i>charset</i> can be any encoding supported by the system&#8217;s <tt>&quot;iconv&quot;</tt> library routine; however, you will have problems with encodings that do not fit exactly in <tt>&quot;wchar_t&quot;</tt>.</p>
<dt><code>-finput-charset=</code><i>charset</i></p>
<dd>Set the input character set, used for translation from the character set of the input file to the source character set used by <font SIZE="-1">GCC. </font> If the locale does not specify, or <font SIZE="-1">GCC</font> cannot get this information from the locale, the default is <font SIZE="-1">UTF-8. </font> This can be overridden by either the locale or this command line option. Currently the command line option takes precedence if there&#8217;s a conflict. <i>charset</i> can be any encoding supported by the system&#8217;s <tt>&quot;iconv&quot;</tt> library routine.</p>
<dt><code>-fworking-directory</code></p>
<dd>Enable generation of linemarkers in the preprocessor output that will let the compiler know the current working directory at the time of preprocessing. When this option is enabled, the preprocessor will emit, after the initial linemarker, a second linemarker with the current working directory followed by two slashes. <font SIZE="-1">GCC</font> will use this directory, when it&#8217;s present in the preprocessed input, as the directory emitted as the current working directory in some debugging information formats. This option is implicitly enabled if debugging information is enabled, but this can be inhibited with the negated form <code>-fno-working-directory</code>. If the <code>-P</code> flag is present in the command line, this option has no effect, since no <tt>&quot;#line&quot;</tt> directives are emitted whatsoever.</p>
<dt><code>-fno-show-column</code></p>
<dd>Do not print column numbers in diagnostics. This may be necessary if diagnostics are being scanned by a program that does not understand the column numbers, such as <code>dejagnu</code>.</p>
<dt><code>-A</code> <i>predicate</i><code>=</code><i>answer</i></p>
<dd>Make an assertion with the predicate <i>predicate</i> and answer <i>answer</i>. This form is preferred to the older form <code>-A</code> <i>predicate</i><code>(</code><i>answer</i><code>)</code>, which is still supported, because it does not use shell special characters.</p>
<dt><code>-A &#8211;</code><i>predicate</i><code>=</code><i>answer</i></p>
<dd>Cancel an assertion with the predicate <i>predicate</i> and answer <i>answer</i>.</p>
<dt><code>-dCHARS</code></p>
<dd><i></i><font SIZE="-1"><i>CHARS</i></font><i></i> is a sequence of one or more of the following characters, and must not be preceded by a space. Other characters are interpreted by the compiler proper, or reserved for future versions of <font SIZE="-1">GCC,</font> and so are silently ignored. If you specify characters whose behavior conflicts, the result is undefined.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>M</code></p>
<dd>Instead of the normal output, generate a list of <code>#define</code> directives for all the macros defined during the execution of the preprocessor, including predefined macros. This gives you a way of finding out what is predefined in your version of the preprocessor. Assuming you have no file <i>foo.h</i>, the command </p>
<pre> touch foo.h; cpp -dM foo.h</pre>
<p>will show all the predefined macros. </p>
<p> If you use <code>-dM</code> without the <code>-E</code> option, <code>-dM</code> is interpreted as a synonym for <code>-fdump-rtl-mach</code>.</p>
<dt><code>D</code></p>
<dd>Like <code>M</code> except in two respects: it does <i>not</i> include the predefined macros, and it outputs <i>both</i> the <code>#define</code> directives and the result of preprocessing. Both kinds of output go to the standard output file.</p>
<dt><code>N</code></p>
<dd>Like <code>D</code>, but emit only the macro names, not their expansions.</p>
<dt><code>I</code></p>
<dd>Output <code>#include</code> directives in addition to the result of preprocessing.</p>
<dt><code>U</code></p>
<dd>Like <code>D</code> except that only macros that are expanded, or whose definedness is tested in preprocessor directives, are output; the output is delayed until the use or test of the macro; and <code>#undef</code> directives are also output for macros tested but undefined at the time.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-P</code></p>
<dd>Inhibit generation of linemarkers in the output from the preprocessor. This might be useful when running the preprocessor on something that is not C code, and will be sent to a program which might be confused by the linemarkers.</p>
<dt><code>-C</code></p>
<dd>Do not discard comments. All comments are passed through to the output file, except for comments in processed directives, which are deleted along with the directive. </p>
<p> You should be prepared for side effects when using <code>-C</code>; it causes the preprocessor to treat comments as tokens in their own right. For example, comments appearing at the start of what would be a directive line have the effect of turning that line into an ordinary source line, since the first token on the line is no longer a <code>#</code>.</p>
<dt><code>-CC</code></p>
<dd>Do not discard comments, including during macro expansion. This is like <code>-C</code>, except that comments contained within macros are also passed through to the output file where the macro is expanded. </p>
<p> In addition to the side-effects of the <code>-C</code> option, the <code>-CC</code> option causes all C<font SIZE="-2">++</font>-style comments inside a macro to be converted to C-style comments. This is to prevent later use of that macro from inadvertently commenting out the remainder of the source line. </p>
<p> The <code>-CC</code> option is generally used to support lint comments.</p>
<dt><code>-traditional-cpp</code></p>
<dd>Try to imitate the behavior of old-fashioned C preprocessors, as opposed to <font SIZE="-1">ISO C</font> preprocessors.</p>
<dt><code>-trigraphs</code></p>
<dd>Process trigraph sequences. These are three-character sequences, all starting with <code>??</code>, that are defined by <font SIZE="-1">ISO C</font> to stand for single characters. For example, <code>??/</code> stands for <code>\</code>, so <code>&#8216;??/n&#8217;</code> is a character constant for a newline. By default, <font SIZE="-1">GCC</font> ignores trigraphs, but in standard-conforming modes it converts them. See the <code>-std</code> and <code>-ansi</code> options. </p>
<p> The nine trigraphs and their replacements are </p>
<pre> Trigraph: ??( ??) ??&lt; ??&gt; ??= ??/ ??' ??! ??-
 Replacement: [ ] { } # \ ^ | ~</pre>
<dt><code>-remap</code></p>
<dd>Enable special code to work around file systems which only permit very short file names, such as MS-DOS.</p>
<dt><code>&#8211;help</code></p>
<dd>
<dt><code>&#8211;target-help</code></p>
<dd>Print text describing all the command line options instead of preprocessing anything.</p>
<dt><code>-v</code></p>
<dd>Verbose mode. Print out <font SIZE="-1">GNU CPP</font>&#8216;s version number at the beginning of execution, and report the final form of the include path.</p>
<dt><code>-H</code></p>
<dd>Print the name of each header file used, in addition to other normal activities. Each name is indented to show how deep in the <code>#include</code> stack it is. Precompiled header files are also printed, even if they are found to be invalid; an invalid precompiled header file is printed with <code>&#8230;x</code> and a valid one with <code>&#8230;!</code> .</p>
<dt><code>-version</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Print out <font SIZE="-1">GNU CPP</font>&#8216;s version number. With one dash, proceed to preprocess as normal. With two dashes, exit immediately.</dl>
<h3>Passing Options to the Assembler</h3>
<p>You can pass options to the assembler.</p>
<dl COMPACT>
<dt><code>-Wa,</code><i>option</i></p>
<dd>Pass <i>option</i> as an option to the assembler. If <i>option</i> contains commas, it is split into multiple options at the commas.</p>
<dt><code>-Xassembler</code> <i>option</i></p>
<dd>Pass <i>option</i> as an option to the assembler. You can use this to supply system-specific assembler options that <font SIZE="-1">GCC</font> does not recognize. </p>
<p> If you want to pass an option that takes an argument, you must use <code>-Xassembler</code> twice, once for the option and once for the argument.</dl>
<h3>Options for Linking</h3>
<p>These options come into play when the compiler links object files into an executable output file. They are meaningless if the compiler is not doing a link step.</p>
<dl COMPACT>
<dt><i>object-file-name</i></p>
<dd>A file name that does not end in a special recognized suffix is considered to name an object file or library. (Object files are distinguished from libraries by the linker according to the file contents.) If linking is done, these object files are used as input to the linker.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>-S</code></p>
<dd>
<dt><code>-E</code></p>
<dd>If any of these options is used, then the linker is not run, and object file names should not be used as arguments.</p>
<dt><code>-l</code><i>library</i></p>
<dd>
<dt><code>-l</code> <i>library</i></p>
<dd>Search the library named <i>library</i> when linking. (The second alternative with the library as a separate argument is only for <font SIZE="-1">POSIX</font> compliance and is not recommended.) </p>
<p> It makes a difference where in the command you write this option; the linker searches and processes libraries and object files in the order they are specified. Thus, <code>foo.o -lz bar.o</code> searches library <code>z</code> after file <i>foo.o</i> but before <i>bar.o</i>. If <i>bar.o</i> refers to functions in <code>z</code>, those functions may not be loaded. </p>
<p> The linker searches a standard list of directories for the library, which is actually a file named <i>liblibrary.a</i>. The linker then uses this file as if it had been specified precisely by name. </p>
<p> The directories searched include several standard system directories plus any that you specify with <code>-L</code>. </p>
<p> Normally the files found this way are library files&#8212;archive files whose members are object files. The linker handles an archive file by scanning through it for members which define symbols that have so far been referenced but not defined. But if the file that is found is an ordinary object file, it is linked in the usual fashion. The only difference between using an <code>-l</code> option and specifying a file name is that <code>-l</code> surrounds <i>library</i> with <code>lib</code> and <code>.a</code> and searches several directories.</p>
<dt><code>-lobjc</code></p>
<dd>You need this special case of the <code>-l</code> option in order to link an Objective-C or Objective-C<font SIZE="-2">++</font> program.</p>
<dt><code>-nostartfiles</code></p>
<dd>Do not use the standard system startup files when linking. The standard system libraries are used normally, unless <code>-nostdlib</code> or <code>-nodefaultlibs</code> is used.</p>
<dt><code>-nodefaultlibs</code></p>
<dd>Do not use the standard system libraries when linking. Only the libraries you specify are passed to the linker, and options specifying linkage of the system libraries, such as <tt>&quot;-static-libgcc&quot;</tt> or <tt>&quot;-shared-libgcc&quot;</tt>, are ignored. The standard startup files are used normally, unless <code>-nostartfiles</code> is used. </p>
<p> The compiler may generate calls to <tt>&quot;memcmp&quot;</tt>, <tt>&quot;memset&quot;</tt>, <tt>&quot;memcpy&quot;</tt> and <tt>&quot;memmove&quot;</tt>. These entries are usually resolved by entries in libc. These entry points should be supplied through some other mechanism when this option is specified.</p>
<dt><code>-nostdlib</code></p>
<dd>Do not use the standard system startup files or libraries when linking. No startup files and only the libraries you specify are passed to the linker, and options specifying linkage of the system libraries, such as <tt>&quot;-static-libgcc&quot;</tt> or <tt>&quot;-shared-libgcc&quot;</tt>, are ignored. </p>
<p> The compiler may generate calls to <tt>&quot;memcmp&quot;</tt>, <tt>&quot;memset&quot;</tt>, <tt>&quot;memcpy&quot;</tt> and <tt>&quot;memmove&quot;</tt>. These entries are usually resolved by entries in libc. These entry points should be supplied through some other mechanism when this option is specified. </p>
<p> One of the standard libraries bypassed by <code>-nostdlib</code> and <code>-nodefaultlibs</code> is <i>libgcc.a</i>, a library of internal subroutines which <font SIZE="-1">GCC</font> uses to overcome shortcomings of particular machines, or special needs for some languages. </p>
<p> In most cases, you need <i>libgcc.a</i> even when you want to avoid other standard libraries. In other words, when you specify <code>-nostdlib</code> or <code>-nodefaultlibs</code> you should usually specify <code>-lgcc</code> as well. This ensures that you have no unresolved references to internal <font SIZE="-1">GCC</font> library subroutines. (An example of such an internal subroutine is <code>__main</code>, used to ensure C<font SIZE="-2">++</font> constructors are called.)</p>
<dt><code>-pie</code></p>
<dd>Produce a position independent executable on targets that support it. For predictable results, you must also specify the same set of options used for compilation (<code>-fpie</code>, <code>-fPIE</code>, or model suboptions) when you specify this linker option.</p>
<dt><code>-rdynamic</code></p>
<dd>Pass the flag <code>-export-dynamic</code> to the <font SIZE="-1">ELF</font> linker, on targets that support it. This instructs the linker to add all symbols, not only used ones, to the dynamic symbol table. This option is needed for some uses of <tt>&quot;dlopen&quot;</tt> or to allow obtaining backtraces from within a program.</p>
<dt><code>-s</code></p>
<dd>Remove all symbol table and relocation information from the executable.</p>
<dt><code>-static</code></p>
<dd>On systems that support dynamic linking, this prevents linking with the shared libraries. On other systems, this option has no effect.</p>
<dt><code>-shared</code></p>
<dd>Produce a shared object which can then be linked with other objects to form an executable. Not all systems support this option. For predictable results, you must also specify the same set of options used for compilation (<code>-fpic</code>, <code>-fPIC</code>, or model suboptions) when you specify this linker option.[1]</p>
<dt><code>-shared-libgcc</code></p>
<dd>
<dt><code>-static-libgcc</code></p>
<dd>On systems that provide <i>libgcc</i> as a shared library, these options force the use of either the shared or static version, respectively. If no shared version of <i>libgcc</i> was built when the compiler was configured, these options have no effect. </p>
<p> There are several situations in which an application should use the shared <i>libgcc</i> instead of the static version. The most common of these is when the application wishes to throw and catch exceptions across different shared libraries. In that case, each of the libraries as well as the application itself should use the shared <i>libgcc</i>. </p>
<p> Therefore, the G++ and <font SIZE="-1">GCJ</font> drivers automatically add <code>-shared-libgcc</code> whenever you build a shared library or a main executable, because C<font SIZE="-2">++</font> and Java programs typically use exceptions, so this is the right thing to do. </p>
<p> If, instead, you use the <font SIZE="-1">GCC</font> driver to create shared libraries, you may find that they are not always linked with the shared <i>libgcc</i>. If <font SIZE="-1">GCC</font> finds, at its configuration time, that you have a non-GNU linker or a <font SIZE="-1">GNU</font> linker that does not support option <code>&#8211;eh-frame-hdr</code>, it links the shared version of <i>libgcc</i> into shared libraries by default. Otherwise, it takes advantage of the linker and optimizes away the linking with the shared version of <i>libgcc</i>, linking with the static version of libgcc by default. This allows exceptions to propagate through such shared libraries, without incurring relocation costs at library load time. </p>
<p> However, if a library or main executable is supposed to throw or catch exceptions, you must link it using the G++ or <font SIZE="-1">GCJ</font> driver, as appropriate for the languages used in the program, or using the option <code>-shared-libgcc</code>, such that it is linked with the shared <i>libgcc</i>.</p>
<dt><code>-static-libasan</code></p>
<dd>When the <code>-fsanitize=address</code> option is used to link a program, the <font SIZE="-1">GCC</font> driver automatically links against <code>libasan</code>. If <i>libasan</i> is available as a shared library, and the <code>-static</code> option is not used, then this links against the shared version of <i>libasan</i>. The <code>-static-libasan</code> option directs the <font SIZE="-1">GCC</font> driver to link <i>libasan</i> statically, without necessarily linking other libraries statically.</p>
<dt><code>-static-libtsan</code></p>
<dd>When the <code>-fsanitize=thread</code> option is used to link a program, the <font SIZE="-1">GCC</font> driver automatically links against <code>libtsan</code>. If <i>libtsan</i> is available as a shared library, and the <code>-static</code> option is not used, then this links against the shared version of <i>libtsan</i>. The <code>-static-libtsan</code> option directs the <font SIZE="-1">GCC</font> driver to link <i>libtsan</i> statically, without necessarily linking other libraries statically.</p>
<dt><code>-static-liblsan</code></p>
<dd>When the <code>-fsanitize=leak</code> option is used to link a program, the <font SIZE="-1">GCC</font> driver automatically links against <code>liblsan</code>. If <i>liblsan</i> is available as a shared library, and the <code>-static</code> option is not used, then this links against the shared version of <i>liblsan</i>. The <code>-static-liblsan</code> option directs the <font SIZE="-1">GCC</font> driver to link <i>liblsan</i> statically, without necessarily linking other libraries statically.</p>
<dt><code>-static-libubsan</code></p>
<dd>When the <code>-fsanitize=undefined</code> option is used to link a program, the <font SIZE="-1">GCC</font> driver automatically links against <code>libubsan</code>. If <i>libubsan</i> is available as a shared library, and the <code>-static</code> option is not used, then this links against the shared version of <i>libubsan</i>. The <code>-static-libubsan</code> option directs the <font SIZE="-1">GCC</font> driver to link <i>libubsan</i> statically, without necessarily linking other libraries statically.</p>
<dt><code>-static-libstdc++</code></p>
<dd>When the <code>g++</code> program is used to link a C<font SIZE="-2">++</font> program, it normally automatically links against <code>libstdc++</code>. If <i>libstdc++</i> is available as a shared library, and the <code>-static</code> option is not used, then this links against the shared version of <i>libstdc++</i>. That is normally fine. However, it is sometimes useful to freeze the version of <i>libstdc++</i> used by the program without going all the way to a fully static link. The <code>-static-libstdc++</code> option directs the <code>g++</code> driver to link <i>libstdc++</i> statically, without necessarily linking other libraries statically.</p>
<dt><code>-symbolic</code></p>
<dd>Bind references to global symbols when building a shared object. Warn about any unresolved references (unless overridden by the link editor option <code>-Xlinker -z -Xlinker defs</code>). Only a few systems support this option.</p>
<dt><code>-T</code> <i>script</i></p>
<dd>Use <i>script</i> as the linker script. This option is supported by most systems using the <font SIZE="-1">GNU</font> linker. On some targets, such as bare-board targets without an operating system, the <code>-T</code> option may be required when linking to avoid references to undefined symbols.</p>
<dt><code>-Xlinker</code> <i>option</i></p>
<dd>Pass <i>option</i> as an option to the linker. You can use this to supply system-specific linker options that <font SIZE="-1">GCC</font> does not recognize. </p>
<p> If you want to pass an option that takes a separate argument, you must use <code>-Xlinker</code> twice, once for the option and once for the argument. For example, to pass <code>-assert definitions</code>, you must write <code>-Xlinker -assert -Xlinker definitions</code>. It does not work to write <code>-Xlinker &#8220;-assert definitions&#8221;</code>, because this passes the entire string as a single argument, which is not what the linker expects. </p>
<p> When using the <font SIZE="-1">GNU</font> linker, it is usually more convenient to pass arguments to linker options using the <i>option</i><code>=</code><i>value</i> syntax than as separate arguments. For example, you can specify <code>-Xlinker -Map=output.map</code> rather than <code>-Xlinker -Map -Xlinker output.map</code>. Other linkers may not support this syntax for command-line options.</p>
<dt><code>-Wl,</code><i>option</i></p>
<dd>Pass <i>option</i> as an option to the linker. If <i>option</i> contains commas, it is split into multiple options at the commas. You can use this syntax to pass an argument to the option. For example, <code>-Wl,-Map,output.map</code> passes <code>-Map output.map</code> to the linker. When using the <font SIZE="-1">GNU</font> linker, you can also get the same effect with <code>-Wl,-Map=output.map</code>.</p>
<dt><code>-u</code> <i>symbol</i></p>
<dd>Pretend the symbol <i>symbol</i> is undefined, to force linking of library modules to define it. You can use <code>-u</code> multiple times with different symbols to force loading of additional library modules.</dl>
<h3>Options for Directory Search</h3>
<p>These options specify directories to search for header files, for libraries and for parts of the compiler:</p>
<dl COMPACT>
<dt><code>-I</code><i>dir</i></p>
<dd>Add the directory <i>dir</i> to the head of the list of directories to be searched for header files. This can be used to override a system header file, substituting your own version, since these directories are searched before the system header file directories. However, you should not use this option to add directories that contain vendor-supplied system header files (use <code>-isystem</code> for that). If you use more than one <code>-I</code> option, the directories are scanned in left-to-right order; the standard system directories come after. </p>
<p> If a standard system include directory, or a directory specified with <code>-isystem</code>, is also specified with <code>-I</code>, the <code>-I</code> option is ignored. The directory is still searched but as a system directory at its normal position in the system include chain. This is to ensure that <font SIZE="-1">GCC</font>&#8216;s procedure to fix buggy system headers and the ordering for the <tt>&quot;include_next&quot;</tt> directive are not inadvertently changed. If you really need to change the search order for system directories, use the <code>-nostdinc</code> and/or <code>-isystem</code> options.</p>
<dt><code>-iplugindir=</code><i>dir</i></p>
<dd>Set the directory to search for plugins that are passed by <code>-fplugin=</code><i>name</i> instead of <code>-fplugin=</code><i>path</i><code>/</code><i>name</i><code>.so</code>. This option is not meant to be used by the user, but only passed by the driver.</p>
<dt><code>-iquote</code><i>dir</i></p>
<dd>Add the directory <i>dir</i> to the head of the list of directories to be searched for header files only for the case of <code>#include &quot;</code><i>file</i><code>&quot;</code>; they are not searched for <code>#include &lt;</code><i>file</i><code>&gt;</code>, otherwise just like <code>-I</code>.</p>
<dt><code>-L</code><i>dir</i></p>
<dd>Add directory <i>dir</i> to the list of directories to be searched for <code>-l</code>.</p>
<dt><code>-B</code><i>prefix</i></p>
<dd>This option specifies where to find the executables, libraries, include files, and data files of the compiler itself. </p>
<p> The compiler driver program runs one or more of the subprograms <code>cpp</code>, <code>cc1</code>, <code>as</code> and <code>ld</code>. It tries <i>prefix</i> as a prefix for each program it tries to run, both with and without <i>machine</i><code>/</code><i>version</i><code>/</code>. </p>
<p> For each subprogram to be run, the compiler driver first tries the <code>-B</code> prefix, if any. If that name is not found, or if <code>-B</code> is not specified, the driver tries two standard prefixes, <i>/usr/lib/gcc/</i> and <i>/usr/local/lib/gcc/</i>. If neither of those results in a file name that is found, the unmodified program name is searched for using the directories specified in your <font SIZE="-1"><code>PATH</code></font> environment variable. </p>
<p> The compiler checks to see if the path provided by the <code>-B</code> refers to a directory, and if necessary it adds a directory separator character at the end of the path. </p>
<p> <code>-B</code> prefixes that effectively specify directory names also apply to libraries in the linker, because the compiler translates these options into <code>-L</code> options for the linker. They also apply to include files in the preprocessor, because the compiler translates these options into <code>-isystem</code> options for the preprocessor. In this case, the compiler appends <code>include</code> to the prefix. </p>
<p> The runtime support file <i>libgcc.a</i> can also be searched for using the <code>-B</code> prefix, if needed. If it is not found there, the two standard prefixes above are tried, and that is all. The file is left out of the link if it is not found by those means. </p>
<p> Another way to specify a prefix much like the <code>-B</code> prefix is to use the environment variable <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. </p>
<p> As a special kludge, if the path provided by <code>-B</code> is <i>[dir/]stageN/</i>, where <i>N</i> is a number in the range 0 to 9, then it is replaced by <i>[dir/]include</i>. This is to help with boot-strapping the compiler.</p>
<dt><code>-specs=</code><i>file</i></p>
<dd>Process <i>file</i> after the compiler reads in the standard <i>specs</i> file, in order to override the defaults which the <code>gcc</code> driver program uses when determining what switches to pass to <code>cc1</code>, <code>cc1plus</code>, <code>as</code>, <code>ld</code>, etc. More than one <code>-specs=</code><i>file</i> can be specified on the command line, and they are processed in order, from left to right.</p>
<dt><code>&#8211;sysroot=</code><i>dir</i></p>
<dd>Use <i>dir</i> as the logical root directory for headers and libraries. For example, if the compiler normally searches for headers in <i>/usr/include</i> and libraries in <i>/usr/lib</i>, it instead searches <i>dir/usr/include</i> and <i>dir/usr/lib</i>. </p>
<p> If you use both this option and the <code>-isysroot</code> option, then the <code>&#8211;sysroot</code> option applies to libraries, but the <code>-isysroot</code> option applies to header files. </p>
<p> The <font SIZE="-1">GNU</font> linker (beginning with version 2.16) has the necessary support for this option. If your linker does not support this option, the header file aspect of <code>&#8211;sysroot</code> still works, but the library aspect does not.</p>
<dt><code>&#8211;no-sysroot-suffix</code></p>
<dd>For some targets, a suffix is added to the root directory specified with <code>&#8211;sysroot</code>, depending on the other options used, so that headers may for example be found in <i>dir/suffix/usr/include</i> instead of <i>dir/usr/include</i>. This option disables the addition of such a suffix.</p>
<dt><code>-I-</code></p>
<dd>This option has been deprecated. Please use <code>-iquote</code> instead for <code>-I</code> directories before the <code>-I-</code> and remove the <code>-I-</code>. Any directories you specify with <code>-I</code> options before the <code>-I-</code> option are searched only for the case of <code>#include &quot;</code><i>file</i><code>&quot;</code>; they are not searched for <code>#include &lt;</code><i>file</i><code>&gt;</code>. </p>
<p> If additional directories are specified with <code>-I</code> options after the <code>-I-</code>, these directories are searched for all <code>#include</code> directives. (Ordinarily <i>all</i> <code>-I</code> directories are used this way.) </p>
<p> In addition, the <code>-I-</code> option inhibits the use of the current directory (where the current input file came from) as the first search directory for <code>#include &quot;</code><i>file</i><code>&quot;</code>. There is no way to override this effect of <code>-I-</code>. With <code>-I.</code> you can specify searching the directory that is current when the compiler is invoked. That is not exactly the same as what the preprocessor does by default, but it is often satisfactory. </p>
<p> <code>-I-</code> does not inhibit the use of the standard system directories for header files. Thus, <code>-I-</code> and <code>-nostdinc</code> are independent.</dl>
<h3>Specifying Target Machine and Compiler Version</h3>
<p>The usual way to run <font SIZE="-1">GCC</font> is to run the executable called <code>gcc</code>, or <i>machine</i><code>-gcc</code> when cross-compiling, or <i>machine</i><code>-gcc-</code><i>version</i> to run a version other than the one that was installed last.</p>
<h3>Hardware Models and Configurations</h3>
<p>Each target machine types can have its own special options, starting with <code>-m</code>, to choose among various hardware models or configurations&#8212;for example, 68010 vs 68020, floating coprocessor or none. A single installed version of the compiler can compile for any model or configuration, according to the options specified. </p>
<p> Some configurations of the compiler also support additional special options, usually for compatibility with other compilers on the same platform. </p>
<p> <i>AArch64 Options</i> </p>
<p> These options are defined for AArch64 implementations:</p>
<dl COMPACT>
<dt><code>-mabi=</code><i>name</i></p>
<dd>Generate code for the specified data model. Permissible values are <code>ilp32</code> for SysV-like data model where int, long int and pointer are 32-bit, and <code>lp64</code> for SysV-like data model where int is 32-bit, but long int and pointer are 64-bit. </p>
<p> The default depends on the specific target configuration. Note that the <font SIZE="-1">LP64</font> and <font SIZE="-1">ILP32</font> ABIs are not link-compatible; you must compile your entire program with the same <font SIZE="-1">ABI,</font> and link with a compatible set of libraries.</p>
<dt><code>-mbig-endian</code></p>
<dd>Generate big-endian code. This is the default when <font SIZE="-1">GCC</font> is configured for an <code>aarch64_be-*-*</code> target.</p>
<dt><code>-mgeneral-regs-only</code></p>
<dd>Generate code which uses only the general registers.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate little-endian code. This is the default when <font SIZE="-1">GCC</font> is configured for an <code>aarch64-*-*</code> but not an <code>aarch64_be-*-*</code> target.</p>
<dt><code>-mcmodel=tiny</code></p>
<dd>Generate code for the tiny code model. The program and its statically defined symbols must be within 1GB of each other. Pointers are 64 bits. Programs can be statically or dynamically linked. This model is not fully implemented and mostly treated as <code>small</code>.</p>
<dt><code>-mcmodel=small</code></p>
<dd>Generate code for the small code model. The program and its statically defined symbols must be within 4GB of each other. Pointers are 64 bits. Programs can be statically or dynamically linked. This is the default code model.</p>
<dt><code>-mcmodel=large</code></p>
<dd>Generate code for the large code model. This makes no assumptions about addresses and sizes of sections. Pointers are 64 bits. Programs can be statically linked only.</p>
<dt><code>-mstrict-align</code></p>
<dd>Do not assume that unaligned memory references will be handled by the system.</p>
<dt><code>-momit-leaf-frame-pointer</code></p>
<dd>
<dt><code>-mno-omit-leaf-frame-pointer</code></p>
<dd>Omit or keep the frame pointer in leaf functions. The former behaviour is the default.</p>
<dt><code>-mtls-dialect=desc</code></p>
<dd>Use <font SIZE="-1">TLS</font> descriptors as the thread-local storage mechanism for dynamic accesses of <font SIZE="-1">TLS</font> variables. This is the default.</p>
<dt><code>-mtls-dialect=traditional</code></p>
<dd>Use traditional <font SIZE="-1">TLS</font> as the thread-local storage mechanism for dynamic accesses of <font SIZE="-1">TLS</font> variables.</p>
<dt><code>-mfix-cortex-a53-835769</code></p>
<dd>
<dt><code>-mno-fix-cortex-a53-835769</code></p>
<dd>Enable or disable the workaround for the <font SIZE="-1">ARM</font> Cortex-A53 erratum number 835769. This will involve inserting a <font SIZE="-1">NOP</font> instruction between memory instructions and 64-bit integer multiply-accumulate instructions.</p>
<dt><code>-mfix-cortex-a53-843419</code></p>
<dd>
<dt><code>-mno-fix-cortex-a53-843419</code></p>
<dd>Enable or disable the workaround for the <font SIZE="-1">ARM</font> Cortex-A53 erratum number 843419. This erratum workaround is made at link time and this will only pass the corresponding flag to the linker.</p>
<dt><code>-march=</code><i>name</i></p>
<dd>Specify the name of the target architecture, optionally suffixed by one or more feature modifiers. This option has the form <code>-march=</code><i>arch</i>{<code>+</code>[<code>no</code>]<i>feature</i>}*, where the only permissible value for <i>arch</i> is <code>armv8-a</code>. The permissible values for <i>feature</i> are documented in the sub-section below. </p>
<p> Where conflicting feature modifiers are specified, the right-most feature is used. </p>
<p> <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. </p>
<p> Where <code>-march</code> is specified without either of <code>-mtune</code> or <code>-mcpu</code> also being specified, the code will be tuned to perform well across a range of target processors implementing the target architecture.</p>
<dt><code>-mtune=</code><i>name</i></p>
<dd>Specify the name of the target processor for which <font SIZE="-1">GCC</font> should tune the performance of the code. Permissible values for this option are: <code>generic</code>, <code>cortex-a53</code>, <code>cortex-a57</code>. </p>
<p> Additionally, this option can specify that <font SIZE="-1">GCC</font> should tune the performance of the code for a big.LITTLE system. The only permissible value is <code>cortex-a57.cortex-a53</code>. </p>
<p> Where none of <code>-mtune=</code>, <code>-mcpu=</code> or <code>-march=</code> are specified, the code will be tuned to perform well across a range of target processors. </p>
<p> This option cannot be suffixed by feature modifiers.</p>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>Specify the name of the target processor, optionally suffixed by one or more feature modifiers. This option has the form <code>-mcpu=</code><i>cpu</i>{<code>+</code>[<code>no</code>]<i>feature</i>}*, where the permissible values for <i>cpu</i> are the same as those available for <code>-mtune</code>. </p>
<p> The permissible values for <i>feature</i> are documented in the sub-section below. </p>
<p> Where conflicting feature modifiers are specified, the right-most feature is used. </p>
<p> <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code (as if by <code>-march</code>) and to determine the target processor for which to tune for performance (as if by <code>-mtune</code>). Where this option is used in conjunction with <code>-march</code> or <code>-mtune</code>, those options take precedence over the appropriate part of this option.</dl>
<p> <code>-march</code> and <code>-mcpu</code> feature modifiers </p>
<p> Feature modifiers used with <code>-march</code> and <code>-mcpu</code> can be one the following:</p>
<dl COMPACT>
<dt><code>crc</code></p>
<dd>Enable <font SIZE="-1">CRC</font> extension.</p>
<dt><code>crypto</code></p>
<dd>Enable Crypto extension. This implies Advanced <font SIZE="-1">SIMD</font> is enabled.</p>
<dt><code>fp</code></p>
<dd>Enable floating-point instructions.</p>
<dt><code>simd</code></p>
<dd>Enable Advanced <font SIZE="-1">SIMD</font> instructions. This implies floating-point instructions are enabled. This is the default for all current possible values for options <code>-march</code> and <code>-mcpu=</code>.</dl>
<p> <i>Adapteva Epiphany Options</i> </p>
<p> These <code>-m</code> options are defined for Adapteva Epiphany:</p>
<dl COMPACT>
<dt><code>-mhalf-reg-file</code></p>
<dd>Don&#8217;t allocate any register in the range <tt>&quot;r32&quot;</tt>&#8230;<tt>&quot;r63&quot;</tt>. That allows code to run on hardware variants that lack these registers.</p>
<dt><code>-mprefer-short-insn-regs</code></p>
<dd>Preferrentially allocate registers that allow short instruction generation. This can result in increased instruction count, so this may either reduce or increase overall code size.</p>
<dt><code>-mbranch-cost=</code><i>num</i></p>
<dd>Set the cost of branches to roughly <i>num</i> &#8220;simple&#8221; instructions. This cost is only a heuristic and is not guaranteed to produce consistent results across releases.</p>
<dt><code>-mcmove</code></p>
<dd>Enable the generation of conditional moves.</p>
<dt><code>-mnops=</code><i>num</i></p>
<dd>Emit <i>num</i> NOPs before every other generated instruction.</p>
<dt><code>-mno-soft-cmpsf</code></p>
<dd>For single-precision floating-point comparisons, emit an <tt>&quot;fsub&quot;</tt> instruction and test the flags. This is faster than a software comparison, but can get incorrect results in the presence of NaNs, or when two different small numbers are compared such that their difference is calculated as zero. The default is <code>-msoft-cmpsf</code>, which uses slower, but IEEE-compliant, software comparisons.</p>
<dt><code>-mstack-offset=</code><i>num</i></p>
<dd>Set the offset between the top of the stack and the stack pointer. E.g., a value of 8 means that the eight bytes in the range <tt>&quot;sp+0...sp+7&quot;</tt> can be used by leaf functions without stack allocation. Values other than <code>8</code> or <code>16</code> are untested and unlikely to work. Note also that this option changes the <font SIZE="-1">ABI</font>; compiling a program with a different stack offset than the libraries have been compiled with generally does not work. This option can be useful if you want to evaluate if a different stack offset would give you better code, but to actually use a different stack offset to build working programs, it is recommended to configure the toolchain with the appropriate <code>&#8211;with-stack-offset=</code><i>num</i> option.</p>
<dt><code>-mno-round-nearest</code></p>
<dd>Make the scheduler assume that the rounding mode has been set to truncating. The default is <code>-mround-nearest</code>.</p>
<dt><code>-mlong-calls</code></p>
<dd>If not otherwise specified by an attribute, assume all calls might be beyond the offset range of the <tt>&quot;b&quot;</tt> / <tt>&quot;bl&quot;</tt> instructions, and therefore load the function address into a register before performing a (otherwise direct) call. This is the default.</p>
<dt><code>-mshort-calls</code></p>
<dd>If not otherwise specified by an attribute, assume all direct calls are in the range of the <tt>&quot;b&quot;</tt> / <tt>&quot;bl&quot;</tt> instructions, so use these instructions for direct calls. The default is <code>-mlong-calls</code>.</p>
<dt><code>-msmall16</code></p>
<dd>Assume addresses can be loaded as 16-bit unsigned values. This does not apply to function addresses for which <code>-mlong-calls</code> semantics are in effect.</p>
<dt><code>-mfp-mode=</code><i>mode</i></p>
<dd>Set the prevailing mode of the floating-point unit. This determines the floating-point mode that is provided and expected at function call and return time. Making this mode match the mode you predominantly need at function start can make your programs smaller and faster by avoiding unnecessary mode switches. </p>
<p> <i>mode</i> can be set to one the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>caller</code></p>
<dd>Any mode at function entry is valid, and retained or restored when the function returns, and when it calls other functions. This mode is useful for compiling libraries or other compilation units you might want to incorporate into different programs with different prevailing <font SIZE="-1">FPU</font> modes, and the convenience of being able to use a single object file outweighs the size and speed overhead for any extra mode switching that might be needed, compared with what would be needed with a more specific choice of prevailing <font SIZE="-1">FPU</font> mode.</p>
<dt><code>truncate</code></p>
<dd>This is the mode used for floating-point calculations with truncating (i.e. round towards zero) rounding mode. That includes conversion from floating point to integer.</p>
<dt><code>round-nearest</code></p>
<dd>This is the mode used for floating-point calculations with round-to-nearest-or-even rounding mode.</p>
<dt><code>int</code></p>
<dd>This is the mode used to perform integer calculations in the <font SIZE="-1">FPU,</font> e.g. integer multiply, or integer multiply-and-accumulate.</dl>
</dl>
<dl COMPACT>
<dd>The default is <code>-mfp-mode=caller</code></dl>
<dt><code>-mnosplit-lohi</code></p>
<dd>
<dt><code>-mno-postinc</code></p>
<dd>
<dt><code>-mno-postmodify</code></p>
<dd>Code generation tweaks that disable, respectively, splitting of 32-bit loads, generation of post-increment addresses, and generation of post-modify addresses. The defaults are <code>msplit-lohi</code>, <code>-mpost-inc</code>, and <code>-mpost-modify</code>.</p>
<dt><code>-mnovect-double</code></p>
<dd>Change the preferred <font SIZE="-1">SIMD</font> mode to SImode. The default is <code>-mvect-double</code>, which uses DImode as preferred <font SIZE="-1">SIMD</font> mode.</p>
<dt><code>-max-vect-align=</code><i>num</i></p>
<dd>The maximum alignment for <font SIZE="-1">SIMD</font> vector mode types. <i>num</i> may be 4 or 8. The default is 8. Note that this is an <font SIZE="-1">ABI</font> change, even though many library function interfaces are unaffected if they don&#8217;t use <font SIZE="-1">SIMD</font> vector modes in places that affect size and/or alignment of relevant types.</p>
<dt><code>-msplit-vecmove-early</code></p>
<dd>Split vector moves into single word moves before reload. In theory this can give better register allocation, but so far the reverse seems to be generally the case.</p>
<dt><code>-m1reg-</code><i>reg</i></p>
<dd>Specify a register to hold the constant -1, which makes loading small negative constants and certain bitmasks faster. Allowable values for <i>reg</i> are <code>r43</code> and <code>r63</code>, which specify use of that register as a fixed register, and <code>none</code>, which means that no register is used for this purpose. The default is <code>-m1reg-none</code>.</dl>
<p> <i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i> </p>
<p> The following options control the architecture variant for which code is being compiled:</p>
<dl COMPACT>
<dt><code>-mbarrel-shifter</code></p>
<dd>Generate instructions supported by barrel shifter. This is the default unless <code>-mcpu=ARC601</code> is in effect.</p>
<dt><code>-mcpu=</code><i>cpu</i></p>
<dd>Set architecture type, register usage, and instruction scheduling parameters for <i>cpu</i>. There are also shortcut alias options available for backward compatibility and convenience. Supported values for <i>cpu</i> are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1"><code>ARC600</code></font></p>
<dd>Compile for <font SIZE="-1">ARC600. </font> Aliases: <code>-mA6</code>, <code>-mARC600</code>.</p>
<dt><font SIZE="-1"><code>ARC601</code></font></p>
<dd>Compile for <font SIZE="-1">ARC601. </font> Alias: <code>-mARC601</code>.</p>
<dt><font SIZE="-1"><code>ARC700</code></font></p>
<dd>Compile for <font SIZE="-1">ARC700. </font> Aliases: <code>-mA7</code>, <code>-mARC700</code>. This is the default when configured with <code>&#8211;with-cpu=arc700</code>.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mdpfp</code></p>
<dd>
<dt><code>-mdpfp-compact</code></p>
<dd><font SIZE="-1">FPX:</font> Generate Double Precision <font SIZE="-1">FPX</font> instructions, tuned for the compact implementation.</p>
<dt><code>-mdpfp-fast</code></p>
<dd><font SIZE="-1">FPX:</font> Generate Double Precision <font SIZE="-1">FPX</font> instructions, tuned for the fast implementation.</p>
<dt><code>-mno-dpfp-lrsr</code></p>
<dd>Disable <font SIZE="-1">LR</font> and <font SIZE="-1">SR</font> instructions from using <font SIZE="-1">FPX</font> extension aux registers.</p>
<dt><code>-mea</code></p>
<dd>Generate Extended arithmetic instructions. Currently only <tt>&quot;divaw&quot;</tt>, <tt>&quot;adds&quot;</tt>, <tt>&quot;subs&quot;</tt>, and <tt>&quot;sat16&quot;</tt> are supported. This is always enabled for <code>-mcpu=ARC700</code>.</p>
<dt><code>-mno-mpy</code></p>
<dd>Do not generate mpy instructions for <font SIZE="-1">ARC700.</font></p>
<dt><code>-mmul32x16</code></p>
<dd>Generate 32&#215;16 bit multiply and mac instructions.</p>
<dt><code>-mmul64</code></p>
<dd>Generate mul64 and mulu64 instructions. Only valid for <code>-mcpu=ARC600</code>.</p>
<dt><code>-mnorm</code></p>
<dd>Generate norm instruction. This is the default if <code>-mcpu=ARC700</code> is in effect.</p>
<dt><code>-mspfp</code></p>
<dd>
<dt><code>-mspfp-compact</code></p>
<dd><font SIZE="-1">FPX:</font> Generate Single Precision <font SIZE="-1">FPX</font> instructions, tuned for the compact implementation.</p>
<dt><code>-mspfp-fast</code></p>
<dd><font SIZE="-1">FPX:</font> Generate Single Precision <font SIZE="-1">FPX</font> instructions, tuned for the fast implementation.</p>
<dt><code>-msimd</code></p>
<dd>Enable generation of <font SIZE="-1">ARC SIMD</font> instructions via target-specific builtins. Only valid for <code>-mcpu=ARC700</code>.</p>
<dt><code>-msoft-float</code></p>
<dd>This option ignored; it is provided for compatibility purposes only. Software floating point code is emitted by default, and this default can overridden by <font SIZE="-1">FPX</font> options; <code>mspfp</code>, <code>mspfp-compact</code>, or <code>mspfp-fast</code> for single precision, and <code>mdpfp</code>, <code>mdpfp-compact</code>, or <code>mdpfp-fast</code> for double precision.</p>
<dt><code>-mswap</code></p>
<dd>Generate swap instructions.</dl>
<p> The following options are passed through to the assembler, and also define preprocessor macro symbols.</p>
<dl COMPACT>
<dt><code>-mdsp-packa</code></p>
<dd>Passed down to the assembler to enable the <font SIZE="-1">DSP</font> Pack A extensions. Also sets the preprocessor symbol <tt>&quot;__Xdsp_packa&quot;</tt>.</p>
<dt><code>-mdvbf</code></p>
<dd>Passed down to the assembler to enable the dual viterbi butterfly extension. Also sets the preprocessor symbol <tt>&quot;__Xdvbf&quot;</tt>.</p>
<dt><code>-mlock</code></p>
<dd>Passed down to the assembler to enable the Locked Load/Store Conditional extension. Also sets the preprocessor symbol <tt>&quot;__Xlock&quot;</tt>.</p>
<dt><code>-mmac-d16</code></p>
<dd>Passed down to the assembler. Also sets the preprocessor symbol <tt>&quot;__Xxmac_d16&quot;</tt>.</p>
<dt><code>-mmac-24</code></p>
<dd>Passed down to the assembler. Also sets the preprocessor symbol <tt>&quot;__Xxmac_24&quot;</tt>.</p>
<dt><code>-mrtsc</code></p>
<dd>Passed down to the assembler to enable the 64-bit Time-Stamp Counter extension instruction. Also sets the preprocessor symbol <tt>&quot;__Xrtsc&quot;</tt>.</p>
<dt><code>-mswape</code></p>
<dd>Passed down to the assembler to enable the swap byte ordering extension instruction. Also sets the preprocessor symbol <tt>&quot;__Xswape&quot;</tt>.</p>
<dt><code>-mtelephony</code></p>
<dd>Passed down to the assembler to enable dual and single operand instructions for telephony. Also sets the preprocessor symbol <tt>&quot;__Xtelephony&quot;</tt>.</p>
<dt><code>-mxy</code></p>
<dd>Passed down to the assembler to enable the <font SIZE="-1">XY</font> Memory extension. Also sets the preprocessor symbol <tt>&quot;__Xxy&quot;</tt>.</dl>
<p> The following options control how the assembly code is annotated:</p>
<dl COMPACT>
<dt><code>-misize</code></p>
<dd>Annotate assembler instructions with estimated addresses.</p>
<dt><code>-mannotate-align</code></p>
<dd>Explain what alignment considerations lead to the decision to make an instruction short or long.</dl>
<p> The following options are passed through to the linker:</p>
<dl COMPACT>
<dt><code>-marclinux</code></p>
<dd>Passed through to the linker, to specify use of the <tt>&quot;arclinux&quot;</tt> emulation. This option is enabled by default in tool chains built for <tt>&quot;arc-linux-uclibc&quot;</tt> and <tt>&quot;arceb-linux-uclibc&quot;</tt> targets when profiling is not requested.</p>
<dt><code>-marclinux_prof</code></p>
<dd>Passed through to the linker, to specify use of the <tt>&quot;arclinux_prof&quot;</tt> emulation. This option is enabled by default in tool chains built for <tt>&quot;arc-linux-uclibc&quot;</tt> and <tt>&quot;arceb-linux-uclibc&quot;</tt> targets when profiling is requested.</dl>
<p> The following options control the semantics of generated code:</p>
<dl COMPACT>
<dt><code>-mepilogue-cfi</code></p>
<dd>Enable generation of call frame information for epilogues.</p>
<dt><code>-mno-epilogue-cfi</code></p>
<dd>Disable generation of call frame information for epilogues.</p>
<dt><code>-mlong-calls</code></p>
<dd>Generate call insns as register indirect calls, thus providing access to the full 32-bit address range.</p>
<dt><code>-mmedium-calls</code></p>
<dd>Don&#8217;t use less than 25 bit addressing range for calls, which is the offset available for an unconditional branch-and-link instruction. Conditional execution of function calls is suppressed, to allow use of the 25-bit range, rather than the 21-bit range with conditional branch-and-link. This is the default for tool chains built for <tt>&quot;arc-linux-uclibc&quot;</tt> and <tt>&quot;arceb-linux-uclibc&quot;</tt> targets.</p>
<dt><code>-mno-sdata</code></p>
<dd>Do not generate sdata references. This is the default for tool chains built for <tt>&quot;arc-linux-uclibc&quot;</tt> and <tt>&quot;arceb-linux-uclibc&quot;</tt> targets.</p>
<dt><code>-mucb-mcount</code></p>
<dd>Instrument with mcount calls as used in <font SIZE="-1">UCB</font> code. I.e. do the counting in the callee, not the caller. By default <font SIZE="-1">ARC</font> instrumentation counts in the caller.</p>
<dt><code>-mvolatile-cache</code></p>
<dd>Use ordinarily cached memory accesses for volatile references. This is the default.</p>
<dt><code>-mno-volatile-cache</code></p>
<dd>Enable cache bypass for volatile references.</dl>
<p> The following options fine tune code generation:</p>
<dl COMPACT>
<dt><code>-malign-call</code></p>
<dd>Do alignment optimizations for call instructions.</p>
<dt><code>-mauto-modify-reg</code></p>
<dd>Enable the use of pre/post modify with register displacement.</p>
<dt><code>-mbbit-peephole</code></p>
<dd>Enable bbit peephole2.</p>
<dt><code>-mno-brcc</code></p>
<dd>This option disables a target-specific pass in <i>arc_reorg</i> to generate <tt>&quot;BRcc&quot;</tt> instructions. It has no effect on <tt>&quot;BRcc&quot;</tt> generation driven by the combiner pass.</p>
<dt><code>-mcase-vector-pcrel</code></p>
<dd>Use pc-relative switch case tables &#8211; this enables case table shortening. This is the default for <code>-Os</code>.</p>
<dt><code>-mcompact-casesi</code></p>
<dd>Enable compact casesi pattern. This is the default for <code>-Os</code>.</p>
<dt><code>-mno-cond-exec</code></p>
<dd>Disable ARCompact specific pass to generate conditional execution instructions. Due to delay slot scheduling and interactions between operand numbers, literal sizes, instruction lengths, and the support for conditional execution, the target-independent pass to generate conditional execution is often lacking, so the <font SIZE="-1">ARC</font> port has kept a special pass around that tries to find more conditional execution generating opportunities after register allocation, branch shortening, and delay slot scheduling have been done. This pass generally, but not always, improves performance and code size, at the cost of extra compilation time, which is why there is an option to switch it off. If you have a problem with call instructions exceeding their allowable offset range because they are conditionalized, you should consider using <code>-mmedium-calls</code> instead.</p>
<dt><code>-mearly-cbranchsi</code></p>
<dd>Enable pre-reload use of the cbranchsi pattern.</p>
<dt><code>-mexpand-adddi</code></p>
<dd>Expand <tt>&quot;adddi3&quot;</tt> and <tt>&quot;subdi3&quot;</tt> at rtl generation time into <tt>&quot;add.f&quot;</tt>, <tt>&quot;adc&quot;</tt> etc.</p>
<dt><code>-mindexed-loads</code></p>
<dd>Enable the use of indexed loads. This can be problematic because some optimizers will then assume the that indexed stores exist, which is not the case.</p>
<dt><code>-mlra</code></p>
<dd>Enable Local Register Allocation. This is still experimental for <font SIZE="-1">ARC,</font> so by default the compiler uses standard reload (i.e. <code>-mno-lra</code>).</p>
<dt><code>-mlra-priority-none</code></p>
<dd>Don&#8217;t indicate any priority for target registers.</p>
<dt><code>-mlra-priority-compact</code></p>
<dd>Indicate target register priority for r0..r3 / r12..r15.</p>
<dt><code>-mlra-priority-noncompact</code></p>
<dd>Reduce target regsiter priority for r0..r3 / r12..r15.</p>
<dt><code>-mno-millicode</code></p>
<dd>When optimizing for size (using <code>-Os</code>), prologues and epilogues that have to save or restore a large number of registers are often shortened by using call to a special function in libgcc; this is referred to as a <i>millicode</i> call. As these calls can pose performance issues, and/or cause linking issues when linking in a nonstandard way, this option is provided to turn off millicode call generation.</p>
<dt><code>-mmixed-code</code></p>
<dd>Tweak register allocation to help 16-bit instruction generation. This generally has the effect of decreasing the average instruction size while increasing the instruction count.</p>
<dt><code>-mq-class</code></p>
<dd>Enable &#8216;q&#8217; instruction alternatives. This is the default for <code>-Os</code>.</p>
<dt><code>-mRcq</code></p>
<dd>Enable Rcq constraint handling &#8211; most short code generation depends on this. This is the default.</p>
<dt><code>-mRcw</code></p>
<dd>Enable Rcw constraint handling &#8211; ccfsm condexec mostly depends on this. This is the default.</p>
<dt><code>-msize-level=</code><i>level</i></p>
<dd>Fine-tune size optimization with regards to instruction lengths and alignment. The recognized values for <i>level</i> are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>0</code></p>
<dd>No size optimization. This level is deprecated and treated like <code>1</code>.</p>
<dt><code>1</code></p>
<dd>Short instructions are used opportunistically.</p>
<dt><code>2</code></p>
<dd>In addition, alignment of loops and of code after barriers are dropped.</p>
<dt><code>3</code></p>
<dd>In addition, optional data alignment is dropped, and the option <code>Os</code> is enabled.</dl>
</dl>
<dl COMPACT>
<dd>This defaults to <code>3</code> when <code>-Os</code> is in effect. Otherwise, the behavior when this is not set is equivalent to level <code>1</code>.</dl>
<dt><code>-mtune=</code><i>cpu</i></p>
<dd>Set instruction scheduling parameters for <i>cpu</i>, overriding any implied by <code>-mcpu=</code>. </p>
<p> Supported values for <i>cpu</i> are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1"><code>ARC600</code></font></p>
<dd>Tune for <font SIZE="-1">ARC600</font> cpu.</p>
<dt><font SIZE="-1"><code>ARC601</code></font></p>
<dd>Tune for <font SIZE="-1">ARC601</font> cpu.</p>
<dt><font SIZE="-1"><code>ARC700</code></font></p>
<dd>Tune for <font SIZE="-1">ARC700</font> cpu with standard multiplier block.</p>
<dt><code>ARC700-xmac</code></p>
<dd>Tune for <font SIZE="-1">ARC700</font> cpu with <font SIZE="-1">XMAC</font> block.</p>
<dt><font SIZE="-1"><code>ARC725D</code></font></p>
<dd>Tune for <font SIZE="-1">ARC725D</font> cpu.</p>
<dt><font SIZE="-1"><code>ARC750D</code></font></p>
<dd>Tune for <font SIZE="-1">ARC750D</font> cpu.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mmultcost=</code><i>num</i></p>
<dd>Cost to assume for a multiply instruction, with <code>4</code> being equal to a normal instruction.</p>
<dt><code>-munalign-prob-threshold=</code><i>probability</i></p>
<dd>Set probability threshold for unaligning branches. When tuning for <font SIZE="-1"><code>ARC700</code></font> and optimizing for speed, branches without filled delay slot are preferably emitted unaligned and long, unless profiling indicates that the probability for the branch to be taken is below <i>probability</i>. The default is (<font SIZE="-1">REG_BR_PROB_BASE/2</font>), i.e. 5000.</dl>
<p> The following options are maintained for backward compatibility, but are now deprecated and will be removed in a future release:</p>
<dl COMPACT>
<dt><code>-margonaut</code></p>
<dd>Obsolete <font SIZE="-1">FPX.</font></p>
<dt><code>-mbig-endian</code></p>
<dd>
<dt><code>-EB</code></p>
<dd>Compile code for big endian targets. Use of these options is now deprecated. Users wanting big-endian code, should use the <tt>&quot;arceb-elf32&quot;</tt> and <tt>&quot;arceb-linux-uclibc&quot;</tt> targets when building the tool chain, for which big-endian is the default.</p>
<dt><code>-mlittle-endian</code></p>
<dd>
<dt><code>-EL</code></p>
<dd>Compile code for little endian targets. Use of these options is now deprecated. Users wanting little-endian code should use the <tt>&quot;arc-elf32&quot;</tt> and <tt>&quot;arc-linux-uclibc&quot;</tt> targets when building the tool chain, for which little-endian is the default.</p>
<dt><code>-mbarrel_shifter</code></p>
<dd>Replaced by <code>-mbarrel-shifter</code></p>
<dt><code>-mdpfp_compact</code></p>
<dd>Replaced by <code>-mdpfp-compact</code></p>
<dt><code>-mdpfp_fast</code></p>
<dd>Replaced by <code>-mdpfp-fast</code></p>
<dt><code>-mdsp_packa</code></p>
<dd>Replaced by <code>-mdsp-packa</code></p>
<dt><code>-mEA</code></p>
<dd>Replaced by <code>-mea</code></p>
<dt><code>-mmac_24</code></p>
<dd>Replaced by <code>-mmac-24</code></p>
<dt><code>-mmac_d16</code></p>
<dd>Replaced by <code>-mmac-d16</code></p>
<dt><code>-mspfp_compact</code></p>
<dd>Replaced by <code>-mspfp-compact</code></p>
<dt><code>-mspfp_fast</code></p>
<dd>Replaced by <code>-mspfp-fast</code></p>
<dt><code>-mtune=</code><i>cpu</i></p>
<dd>Values <code>arc600</code>, <code>arc601</code>, <code>arc700</code> and <code>arc700-xmac</code> for <i>cpu</i> are replaced by <font SIZE="-1"><code>ARC600</code></font>, <font SIZE="-1"><code>ARC601</code></font>, <font SIZE="-1"><code>ARC700</code></font> and <code>ARC700-xmac</code> respectively</p>
<dt><code>-multcost=</code><i>num</i></p>
<dd>Replaced by <code>-mmultcost</code>.</dl>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for Advanced <font SIZE="-1">RISC</font> Machines (<font SIZE="-1">ARM</font>) architectures:</p>
<dl COMPACT>
<dt><code>-mabi=</code><i>name</i></p>
<dd>Generate code for the specified <font SIZE="-1">ABI. </font> Permissible values are: <code>apcs-gnu</code>, <code>atpcs</code>, <code>aapcs</code>, <code>aapcs-linux</code> and <code>iwmmxt</code>.</p>
<dt><code>-mapcs-frame</code></p>
<dd>Generate a stack frame that is compliant with the <font SIZE="-1">ARM</font> Procedure Call Standard for all functions, even if this is not strictly necessary for correct execution of the code. Specifying <code>-fomit-frame-pointer</code> with this option causes the stack frames not to be generated for leaf functions. The default is <code>-mno-apcs-frame</code>.</p>
<dt><code>-mapcs</code></p>
<dd>This is a synonym for <code>-mapcs-frame</code>.</p>
<dt><code>-mthumb-interwork</code></p>
<dd>Generate code that supports calling between the <font SIZE="-1">ARM</font> and Thumb instruction sets. Without this option, on pre-v5 architectures, the two instruction sets cannot be reliably used inside one program. The default is <code>-mno-thumb-interwork</code>, since slightly larger code is generated when <code>-mthumb-interwork</code> is specified. In <font SIZE="-1">AAPCS</font> configurations this option is meaningless.</p>
<dt><code>-mno-sched-prolog</code></p>
<dd>Prevent the reordering of instructions in the function prologue, or the merging of those instruction with the instructions in the function&#8217;s body. This means that all functions start with a recognizable set of instructions (or in fact one of a choice from a small set of different function prologues), and this information can be used to locate the start of functions inside an executable piece of code. The default is <code>-msched-prolog</code>.</p>
<dt><code>-mfloat-abi=</code><i>name</i></p>
<dd>Specifies which floating-point <font SIZE="-1">ABI</font> to use. Permissible values are: <code>soft</code>, <code>softfp</code> and <code>hard</code>. </p>
<p> Specifying <code>soft</code> causes <font SIZE="-1">GCC</font> to generate output containing library calls for floating-point operations. <code>softfp</code> allows the generation of code using hardware floating-point instructions, but still uses the soft-float calling conventions. <code>hard</code> allows generation of floating-point instructions and uses FPU-specific calling conventions. </p>
<p> The default depends on the specific target configuration. Note that the hard-float and soft-float ABIs are not link-compatible; you must compile your entire program with the same <font SIZE="-1">ABI,</font> and link with a compatible set of libraries.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a processor running in little-endian mode. This is the default for all standard configurations.</p>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a processor running in big-endian mode; the default is to compile code for a little-endian processor.</p>
<dt><code>-mwords-little-endian</code></p>
<dd>This option only applies when generating code for big-endian processors. Generate code for a little-endian word order but a big-endian byte order. That is, a byte order of the form <code>32107654</code>. Note: this option should only be used if you require compatibility with code for big-endian <font SIZE="-1">ARM</font> processors generated by versions of the compiler prior to 2.8. This option is now deprecated.</p>
<dt><code>-march=</code><i>name</i></p>
<dd>This specifies the name of the target <font SIZE="-1">ARM</font> architecture. <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. This option can be used in conjunction with or instead of the <code>-mcpu=</code> option. Permissible names are: <code>armv2</code>, <code>armv2a</code>, <code>armv3</code>, <code>armv3m</code>, <code>armv4</code>, <code>armv4t</code>, <code>armv5</code>, <code>armv5t</code>, <code>armv5e</code>, <code>armv5te</code>, <code>armv6</code>, <code>armv6j</code>, <code>armv6t2</code>, <code>armv6z</code>, <code>armv6zk</code>, <code>armv6-m</code>, <code>armv7</code>, <code>armv7-a</code>, <code>armv7-r</code>, <code>armv7-m</code>, <code>armv7e-m</code>, <code>armv7ve</code>, <code>armv8-a</code>, <code>armv8-a+crc</code>, <code>iwmmxt</code>, <code>iwmmxt2</code>, <code>ep9312</code>. </p>
<p> <code>-march=armv7ve</code> is the armv7-a architecture with virtualization extensions. </p>
<p> <code>-march=armv8-a+crc</code> enables code generation for the ARMv8-A architecture together with the optional <font SIZE="-1">CRC32</font> extensions. </p>
<p> <code>-march=native</code> causes the compiler to auto-detect the architecture of the build computer. At present, this feature is only supported on GNU/Linux, and not all architectures are recognized. If the auto-detect is unsuccessful the option has no effect.</p>
<dt><code>-mtune=</code><i>name</i></p>
<dd>This option specifies the name of the target <font SIZE="-1">ARM</font> processor for which <font SIZE="-1">GCC</font> should tune the performance of the code. For some <font SIZE="-1">ARM</font> implementations better performance can be obtained by using this option. Permissible names are: <code>arm2</code>, <code>arm250</code>, <code>arm3</code>, <code>arm6</code>, <code>arm60</code>, <code>arm600</code>, <code>arm610</code>, <code>arm620</code>, <code>arm7</code>, <code>arm7m</code>, <code>arm7d</code>, <code>arm7dm</code>, <code>arm7di</code>, <code>arm7dmi</code>, <code>arm70</code>, <code>arm700</code>, <code>arm700i</code>, <code>arm710</code>, <code>arm710c</code>, <code>arm7100</code>, <code>arm720</code>, <code>arm7500</code>, <code>arm7500fe</code>, <code>arm7tdmi</code>, <code>arm7tdmi-s</code>, <code>arm710t</code>, <code>arm720t</code>, <code>arm740t</code>, <code>strongarm</code>, <code>strongarm110</code>, <code>strongarm1100</code>, <code>strongarm1110</code>, <code>arm8</code>, <code>arm810</code>, <code>arm9</code>, <code>arm9e</code>, <code>arm920</code>, <code>arm920t</code>, <code>arm922t</code>, <code>arm946e-s</code>, <code>arm966e-s</code>, <code>arm968e-s</code>, <code>arm926ej-s</code>, <code>arm940t</code>, <code>arm9tdmi</code>, <code>arm10tdmi</code>, <code>arm1020t</code>, <code>arm1026ej-s</code>, <code>arm10e</code>, <code>arm1020e</code>, <code>arm1022e</code>, <code>arm1136j-s</code>, <code>arm1136jf-s</code>, <code>mpcore</code>, <code>mpcorenovfp</code>, <code>arm1156t2-s</code>, <code>arm1156t2f-s</code>, <code>arm1176jz-s</code>, <code>arm1176jzf-s</code>, <code>cortex-a5</code>, <code>cortex-a7</code>, <code>cortex-a8</code>, <code>cortex-a9</code>, <code>cortex-a12</code>, <code>cortex-a15</code>, <code>cortex-a53</code>, <code>cortex-a57</code>, <code>cortex-r4</code>, <code>cortex-r4f</code>, <code>cortex-r5</code>, <code>cortex-r7</code>, <code>cortex-m4</code>, <code>cortex-m3</code>, <code>cortex-m1</code>, <code>cortex-m0</code>, <code>cortex-m0plus</code>, <code>marvell-pj4</code>, <code>xscale</code>, <code>iwmmxt</code>, <code>iwmmxt2</code>, <code>ep9312</code>, <code>fa526</code>, <code>fa626</code>, <code>fa606te</code>, <code>fa626te</code>, <code>fmp626</code>, <code>fa726te</code>. </p>
<p> Additionally, this option can specify that <font SIZE="-1">GCC</font> should tune the performance of the code for a big.LITTLE system. Permissible names are: <code>cortex-a15.cortex-a7</code>, <code>cortex-a57.cortex-a53</code>. </p>
<p> <code>-mtune=generic-</code><i>arch</i> specifies that <font SIZE="-1">GCC</font> should tune the performance for a blend of processors within architecture <i>arch</i>. The aim is to generate code that run well on the current most popular processors, balancing between optimizations that benefit some CPUs in the range, and avoiding performance pitfalls of other CPUs. The effects of this option may change in future <font SIZE="-1">GCC</font> versions as <font SIZE="-1">CPU</font> models come and go. </p>
<p> <code>-mtune=native</code> causes the compiler to auto-detect the <font SIZE="-1">CPU</font> of the build computer. At present, this feature is only supported on GNU/Linux, and not all architectures are recognized. If the auto-detect is unsuccessful the option has no effect.</p>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>This specifies the name of the target <font SIZE="-1">ARM</font> processor. <font SIZE="-1">GCC</font> uses this name to derive the name of the target <font SIZE="-1">ARM</font> architecture (as if specified by <code>-march</code>) and the <font SIZE="-1">ARM</font> processor type for which to tune for performance (as if specified by <code>-mtune</code>). Where this option is used in conjunction with <code>-march</code> or <code>-mtune</code>, those options take precedence over the appropriate part of this option. </p>
<p> Permissible names for this option are the same as those for <code>-mtune</code>. </p>
<p> <code>-mcpu=generic-</code><i>arch</i> is also permissible, and is equivalent to <code>-march=</code><i>arch</i> <code>-mtune=generic-</code><i>arch</i>. See <code>-mtune</code> for more information. </p>
<p> <code>-mcpu=native</code> causes the compiler to auto-detect the <font SIZE="-1">CPU</font> of the build computer. At present, this feature is only supported on GNU/Linux, and not all architectures are recognized. If the auto-detect is unsuccessful the option has no effect.</p>
<dt><code>-mfpu=</code><i>name</i></p>
<dd>This specifies what floating-point hardware (or hardware emulation) is available on the target. Permissible names are: <code>vfp</code>, <code>vfpv3</code>, <code>vfpv3-fp16</code>, <code>vfpv3-d16</code>, <code>vfpv3-d16-fp16</code>, <code>vfpv3xd</code>, <code>vfpv3xd-fp16</code>, <code>neon</code>, <code>neon-fp16</code>, <code>vfpv4</code>, <code>vfpv4-d16</code>, <code>fpv4-sp-d16</code>, <code>neon-vfpv4</code>, <code>fp-armv8</code>, <code>neon-fp-armv8</code>, and <code>crypto-neon-fp-armv8</code>. </p>
<p> If <code>-msoft-float</code> is specified this specifies the format of floating-point values. </p>
<p> If the selected floating-point hardware includes the <font SIZE="-1">NEON</font> extension (e.g. <code>-mfpu</code>=<code>neon</code>), note that floating-point operations are not generated by <font SIZE="-1">GCC</font>&#8216;s auto-vectorization pass unless <code>-funsafe-math-optimizations</code> is also specified. This is because <font SIZE="-1">NEON</font> hardware does not fully implement the <font SIZE="-1">IEEE 754</font> standard for floating-point arithmetic (in particular denormal values are treated as zero), so the use of <font SIZE="-1">NEON</font> instructions may lead to a loss of precision.</p>
<dt><code>-mfp16-format=</code><i>name</i></p>
<dd>Specify the format of the <tt>&quot;__fp16&quot;</tt> half-precision floating-point type. Permissible names are <code>none</code>, <code>ieee</code>, and <code>alternative</code>; the default is <code>none</code>, in which case the <tt>&quot;__fp16&quot;</tt> type is not defined.</p>
<dt><code>-mstructure-size-boundary=</code><i>n</i></p>
<dd>The sizes of all structures and unions are rounded up to a multiple of the number of bits set by this option. Permissible values are 8, 32 and 64. The default value varies for different toolchains. For the <font SIZE="-1">COFF</font> targeted toolchain the default value is 8. A value of 64 is only allowed if the underlying <font SIZE="-1">ABI</font> supports it. </p>
<p> Specifying a larger number can produce faster, more efficient code, but can also increase the size of the program. Different values are potentially incompatible. Code compiled with one value cannot necessarily expect to work with code or libraries compiled with another value, if they exchange information using structures or unions.</p>
<dt><code>-mabort-on-noreturn</code></p>
<dd>Generate a call to the function <tt>&quot;abort&quot;</tt> at the end of a <tt>&quot;noreturn&quot;</tt> function. It is executed if the function tries to return.</p>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Tells the compiler to perform function calls by first loading the address of the function into a register and then performing a subroutine call on this register. This switch is needed if the target function lies outside of the 64-megabyte addressing range of the offset-based version of subroutine call instruction. </p>
<p> Even if this switch is enabled, not all function calls are turned into long calls. The heuristic is that static functions, functions that have the <code>short-call</code> attribute, functions that are inside the scope of a <code>#pragma no_long_calls</code> directive, and functions whose definitions have already been compiled within the current compilation unit are not turned into long calls. The exceptions to this rule are that weak function definitions, functions with the <code>long-call</code> attribute or the <code>section</code> attribute, and functions that are within the scope of a <code>#pragma long_calls</code> directive are always turned into long calls. </p>
<p> This feature is not enabled by default. Specifying <code>-mno-long-calls</code> restores the default behavior, as does placing the function calls within the scope of a <code>#pragma long_calls_off</code> directive. Note these switches have no effect on how the compiler generates code to handle function calls via function pointers.</p>
<dt><code>-msingle-pic-base</code></p>
<dd>Treat the register used for <font SIZE="-1">PIC</font> addressing as read-only, rather than loading it in the prologue for each function. The runtime system is responsible for initializing this register with an appropriate value before execution begins.</p>
<dt><code>-mpic-register=</code><i>reg</i></p>
<dd>Specify the register to be used for <font SIZE="-1">PIC</font> addressing. For standard <font SIZE="-1">PIC</font> base case, the default will be any suitable register determined by compiler. For single <font SIZE="-1">PIC</font> base case, the default is <code>R9</code> if target is <font SIZE="-1">EABI</font> based or stack-checking is enabled, otherwise the default is <code>R10</code>.</p>
<dt><code>-mpic-data-is-text-relative</code></p>
<dd>Assume that each data segments are relative to text segment at load time. Therefore, it permits addressing data using PC-relative operations. This option is on by default for targets other than VxWorks <font SIZE="-1">RTP.</font></p>
<dt><code>-mpoke-function-name</code></p>
<dd>Write the name of each function into the text section, directly preceding the function prologue. The generated code is similar to this: </p>
<pre> t0
 .ascii &quot;arm_poke_function_name&quot;, 0
 .align
 t1
 .word 0xff000000 + (t1 - t0)
 arm_poke_function_name
 mov ip, sp
 stmfd sp!, {fp, ip, lr, pc}
 sub fp, ip, #4</pre>
<p>When performing a stack backtrace, code can inspect the value of <tt>&quot;pc&quot;</tt> stored at <tt>&quot;fp + 0&quot;</tt>. If the trace function then looks at location <tt>&quot;pc - 12&quot;</tt> and the top 8 bits are set, then we know that there is a function name embedded immediately preceding this location and has length <tt>&quot;((pc[-3]) &amp; 0xff000000)&quot;</tt>.</p>
<dt><code>-mthumb</code></p>
<dd>
<dt><code>-marm</code></p>
<dd>Select between generating code that executes in <font SIZE="-1">ARM</font> and Thumb states. The default for most configurations is to generate code that executes in <font SIZE="-1">ARM</font> state, but the default can be changed by configuring <font SIZE="-1">GCC</font> with the <code>&#8211;with-mode=</code><i>state</i> configure option.</p>
<dt><code>-mtpcs-frame</code></p>
<dd>Generate a stack frame that is compliant with the Thumb Procedure Call Standard for all non-leaf functions. (A leaf function is one that does not call any other functions.) The default is <code>-mno-tpcs-frame</code>.</p>
<dt><code>-mtpcs-leaf-frame</code></p>
<dd>Generate a stack frame that is compliant with the Thumb Procedure Call Standard for all leaf functions. (A leaf function is one that does not call any other functions.) The default is <code>-mno-apcs-leaf-frame</code>.</p>
<dt><code>-mcallee-super-interworking</code></p>
<dd>Gives all externally visible functions in the file being compiled an <font SIZE="-1">ARM</font> instruction set header which switches to Thumb mode before executing the rest of the function. This allows these functions to be called from non-interworking code. This option is not valid in <font SIZE="-1">AAPCS</font> configurations because interworking is enabled by default.</p>
<dt><code>-mcaller-super-interworking</code></p>
<dd>Allows calls via function pointers (including virtual functions) to execute correctly regardless of whether the target code has been compiled for interworking or not. There is a small overhead in the cost of executing a function pointer if this option is enabled. This option is not valid in <font SIZE="-1">AAPCS</font> configurations because interworking is enabled by default.</p>
<dt><code>-mtp=</code><i>name</i></p>
<dd>Specify the access model for the thread local storage pointer. The valid models are <code>soft</code>, which generates calls to <tt>&quot;__aeabi_read_tp&quot;</tt>, <code>cp15</code>, which fetches the thread pointer from <tt>&quot;cp15&quot;</tt> directly (supported in the arm6k architecture), and <code>auto</code>, which uses the best available method for the selected processor. The default setting is <code>auto</code>.</p>
<dt><code>-mtls-dialect=</code><i>dialect</i></p>
<dd>Specify the dialect to use for accessing thread local storage. Two <i>dialect</i>s are supported&#8212;<code>gnu</code> and <code>gnu2</code>. The <code>gnu</code> dialect selects the original <font SIZE="-1">GNU</font> scheme for supporting local and global dynamic <font SIZE="-1">TLS</font> models. The <code>gnu2</code> dialect selects the <font SIZE="-1">GNU</font> descriptor scheme, which provides better performance for shared libraries. The <font SIZE="-1">GNU</font> descriptor scheme is compatible with the original scheme, but does require new assembler, linker and library support. Initial and local exec <font SIZE="-1">TLS</font> models are unaffected by this option and always use the original scheme.</p>
<dt><code>-mword-relocations</code></p>
<dd>Only generate absolute relocations on word-sized values (i.e. R_ARM_ABS32). This is enabled by default on targets (uClinux, SymbianOS) where the runtime loader imposes this restriction, and when <code>-fpic</code> or <code>-fPIC</code> is specified.</p>
<dt><code>-mfix-cortex-m3-ldrd</code></p>
<dd>Some Cortex-M3 cores can cause data corruption when <tt>&quot;ldrd&quot;</tt> instructions with overlapping destination and base registers are used. This option avoids generating these instructions. This option is enabled by default when <code>-mcpu=cortex-m3</code> is specified.</p>
<dt><code>-munaligned-access</code></p>
<dd>
<dt><code>-mno-unaligned-access</code></p>
<dd>Enables (or disables) reading and writing of 16- and 32- bit values from addresses that are not 16- or 32- bit aligned. By default unaligned access is disabled for all pre-ARMv6 and all ARMv6-M architectures, and enabled for all other architectures. If unaligned access is not enabled then words in packed data structures will be accessed a byte at a time. </p>
<p> The <font SIZE="-1">ARM</font> attribute <tt>&quot;Tag_CPU_unaligned_access&quot;</tt> will be set in the generated object file to either true or false, depending upon the setting of this option. If unaligned access is enabled then the preprocessor symbol <tt>&quot;__ARM_FEATURE_UNALIGNED&quot;</tt> will also be defined.</p>
<dt><code>-mneon-for-64bits</code></p>
<dd>Enables using Neon to handle scalar 64-bits operations. This is disabled by default since the cost of moving data from core registers to Neon is high.</p>
<dt><code>-mslow-flash-data</code></p>
<dd>Assume loading data from flash is slower than fetching instruction. Therefore literal load is minimized for better performance. This option is only supported when compiling for ARMv7 M-profile and off by default.</p>
<dt><code>-mrestrict-it</code></p>
<dd>Restricts generation of <font SIZE="-1">IT</font> blocks to conform to the rules of ARMv8. <font SIZE="-1">IT</font> blocks can only contain a single 16-bit instruction from a select set of instructions. This option is on by default for ARMv8 Thumb mode.</dl>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i> </p>
<p> These options are defined for <font SIZE="-1">AVR</font> implementations:</p>
<dl COMPACT>
<dt><code>-mmcu=</code><i>mcu</i></p>
<dd>Specify Atmel <font SIZE="-1">AVR</font> instruction set architectures (<font SIZE="-1">ISA</font>) or <font SIZE="-1">MCU</font> type. </p>
<p> The default for this option is@tie{}<tt>&quot;avr2&quot;</tt>. </p>
<p> <font SIZE="-1">GCC</font> supports the following <font SIZE="-1">AVR</font> devices and ISAs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&quot;avr2&quot;</p>
<dd>&#8220;Classic&#8221; devices with up to 8@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;attiny22&quot;</tt>, <tt>&quot;attiny26&quot;</tt>, <tt>&quot;at90c8534&quot;</tt>, <tt>&quot;at90s2313&quot;</tt>, <tt>&quot;at90s2323&quot;</tt>, <tt>&quot;at90s2333&quot;</tt>, <tt>&quot;at90s2343&quot;</tt>, <tt>&quot;at90s4414&quot;</tt>, <tt>&quot;at90s4433&quot;</tt>, <tt>&quot;at90s4434&quot;</tt>, <tt>&quot;at90s8515&quot;</tt>, <tt>&quot;at90s8535&quot;</tt>.</p>
<dt>&quot;avr25&quot;</p>
<dd>&#8220;Classic&#8221; devices with up to 8@tie{}KiB of program memory and with the <tt>&quot;MOVW&quot;</tt> instruction. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;ata5272&quot;</tt>, <tt>&quot;ata6289&quot;</tt>, <tt>&quot;attiny13&quot;</tt>, <tt>&quot;attiny13a&quot;</tt>, <tt>&quot;attiny2313&quot;</tt>, <tt>&quot;attiny2313a&quot;</tt>, <tt>&quot;attiny24&quot;</tt>, <tt>&quot;attiny24a&quot;</tt>, <tt>&quot;attiny25&quot;</tt>, <tt>&quot;attiny261&quot;</tt>, <tt>&quot;attiny261a&quot;</tt>, <tt>&quot;attiny43u&quot;</tt>, <tt>&quot;attiny4313&quot;</tt>, <tt>&quot;attiny44&quot;</tt>, <tt>&quot;attiny44a&quot;</tt>, <tt>&quot;attiny45&quot;</tt>, <tt>&quot;attiny461&quot;</tt>, <tt>&quot;attiny461a&quot;</tt>, <tt>&quot;attiny48&quot;</tt>, <tt>&quot;attiny84&quot;</tt>, <tt>&quot;attiny84a&quot;</tt>, <tt>&quot;attiny85&quot;</tt>, <tt>&quot;attiny861&quot;</tt>, <tt>&quot;attiny861a&quot;</tt>, <tt>&quot;attiny87&quot;</tt>, <tt>&quot;attiny88&quot;</tt>, <tt>&quot;at86rf401&quot;</tt>.</p>
<dt>&quot;avr3&quot;</p>
<dd>&#8220;Classic&#8221; devices with 16@tie{}KiB up to 64@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;at43usb355&quot;</tt>, <tt>&quot;at76c711&quot;</tt>.</p>
<dt>&quot;avr31&quot;</p>
<dd>&#8220;Classic&#8221; devices with 128@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atmega103&quot;</tt>, <tt>&quot;at43usb320&quot;</tt>.</p>
<dt>&quot;avr35&quot;</p>
<dd>&#8220;Classic&#8221; devices with 16@tie{}KiB up to 64@tie{}KiB of program memory and with the <tt>&quot;MOVW&quot;</tt> instruction. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;ata5505&quot;</tt>, <tt>&quot;atmega16u2&quot;</tt>, <tt>&quot;atmega32u2&quot;</tt>, <tt>&quot;atmega8u2&quot;</tt>, <tt>&quot;attiny1634&quot;</tt>, <tt>&quot;attiny167&quot;</tt>, <tt>&quot;at90usb162&quot;</tt>, <tt>&quot;at90usb82&quot;</tt>.</p>
<dt>&quot;avr4&quot;</p>
<dd>&#8220;Enhanced&#8221; devices with up to 8@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;ata6285&quot;</tt>, <tt>&quot;ata6286&quot;</tt>, <tt>&quot;atmega48&quot;</tt>, <tt>&quot;atmega48a&quot;</tt>, <tt>&quot;atmega48p&quot;</tt>, <tt>&quot;atmega48pa&quot;</tt>, <tt>&quot;atmega8&quot;</tt>, <tt>&quot;atmega8a&quot;</tt>, <tt>&quot;atmega8hva&quot;</tt>, <tt>&quot;atmega8515&quot;</tt>, <tt>&quot;atmega8535&quot;</tt>, <tt>&quot;atmega88&quot;</tt>, <tt>&quot;atmega88a&quot;</tt>, <tt>&quot;atmega88p&quot;</tt>, <tt>&quot;atmega88pa&quot;</tt>, <tt>&quot;at90pwm1&quot;</tt>, <tt>&quot;at90pwm2&quot;</tt>, <tt>&quot;at90pwm2b&quot;</tt>, <tt>&quot;at90pwm3&quot;</tt>, <tt>&quot;at90pwm3b&quot;</tt>, <tt>&quot;at90pwm81&quot;</tt>.</p>
<dt>&quot;avr5&quot;</p>
<dd>&#8220;Enhanced&#8221; devices with 16@tie{}KiB up to 64@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;ata5790&quot;</tt>, <tt>&quot;ata5790n&quot;</tt>, <tt>&quot;ata5795&quot;</tt>, <tt>&quot;atmega16&quot;</tt>, <tt>&quot;atmega16a&quot;</tt>, <tt>&quot;atmega16hva&quot;</tt>, <tt>&quot;atmega16hva2&quot;</tt>, <tt>&quot;atmega16hvb&quot;</tt>, <tt>&quot;atmega16hvbrevb&quot;</tt>, <tt>&quot;atmega16m1&quot;</tt>, <tt>&quot;atmega16u4&quot;</tt>, <tt>&quot;atmega161&quot;</tt>, <tt>&quot;atmega162&quot;</tt>, <tt>&quot;atmega163&quot;</tt>, <tt>&quot;atmega164a&quot;</tt>, <tt>&quot;atmega164p&quot;</tt>, <tt>&quot;atmega164pa&quot;</tt>, <tt>&quot;atmega165&quot;</tt>, <tt>&quot;atmega165a&quot;</tt>, <tt>&quot;atmega165p&quot;</tt>, <tt>&quot;atmega165pa&quot;</tt>, <tt>&quot;atmega168&quot;</tt>, <tt>&quot;atmega168a&quot;</tt>, <tt>&quot;atmega168p&quot;</tt>, <tt>&quot;atmega168pa&quot;</tt>, <tt>&quot;atmega169&quot;</tt>, <tt>&quot;atmega169a&quot;</tt>, <tt>&quot;atmega169p&quot;</tt>, <tt>&quot;atmega169pa&quot;</tt>, <tt>&quot;atmega26hvg&quot;</tt>, <tt>&quot;atmega32&quot;</tt>, <tt>&quot;atmega32a&quot;</tt>, <tt>&quot;atmega32c1&quot;</tt>, <tt>&quot;atmega32hvb&quot;</tt>, <tt>&quot;atmega32hvbrevb&quot;</tt>, <tt>&quot;atmega32m1&quot;</tt>, <tt>&quot;atmega32u4&quot;</tt>, <tt>&quot;atmega32u6&quot;</tt>, <tt>&quot;atmega323&quot;</tt>, <tt>&quot;atmega324a&quot;</tt>, <tt>&quot;atmega324p&quot;</tt>, <tt>&quot;atmega324pa&quot;</tt>, <tt>&quot;atmega325&quot;</tt>, <tt>&quot;atmega325a&quot;</tt>, <tt>&quot;atmega325p&quot;</tt>, <tt>&quot;atmega3250&quot;</tt>, <tt>&quot;atmega3250a&quot;</tt>, <tt>&quot;atmega3250p&quot;</tt>, <tt>&quot;atmega3250pa&quot;</tt>, <tt>&quot;atmega328&quot;</tt>, <tt>&quot;atmega328p&quot;</tt>, <tt>&quot;atmega329&quot;</tt>, <tt>&quot;atmega329a&quot;</tt>, <tt>&quot;atmega329p&quot;</tt>, <tt>&quot;atmega329pa&quot;</tt>, <tt>&quot;atmega3290&quot;</tt>, <tt>&quot;atmega3290a&quot;</tt>, <tt>&quot;atmega3290p&quot;</tt>, <tt>&quot;atmega3290pa&quot;</tt>, <tt>&quot;atmega406&quot;</tt>, <tt>&quot;atmega48hvf&quot;</tt>, <tt>&quot;atmega64&quot;</tt>, <tt>&quot;atmega64a&quot;</tt>, <tt>&quot;atmega64c1&quot;</tt>, <tt>&quot;atmega64hve&quot;</tt>, <tt>&quot;atmega64m1&quot;</tt>, <tt>&quot;atmega64rfa2&quot;</tt>, <tt>&quot;atmega64rfr2&quot;</tt>, <tt>&quot;atmega640&quot;</tt>, <tt>&quot;atmega644&quot;</tt>, <tt>&quot;atmega644a&quot;</tt>, <tt>&quot;atmega644p&quot;</tt>, <tt>&quot;atmega644pa&quot;</tt>, <tt>&quot;atmega645&quot;</tt>, <tt>&quot;atmega645a&quot;</tt>, <tt>&quot;atmega645p&quot;</tt>, <tt>&quot;atmega6450&quot;</tt>, <tt>&quot;atmega6450a&quot;</tt>, <tt>&quot;atmega6450p&quot;</tt>, <tt>&quot;atmega649&quot;</tt>, <tt>&quot;atmega649a&quot;</tt>, <tt>&quot;atmega649p&quot;</tt>, <tt>&quot;atmega6490&quot;</tt>, <tt>&quot;atmega6490a&quot;</tt>, <tt>&quot;atmega6490p&quot;</tt>, <tt>&quot;at90can32&quot;</tt>, <tt>&quot;at90can64&quot;</tt>, <tt>&quot;at90pwm161&quot;</tt>, <tt>&quot;at90pwm216&quot;</tt>, <tt>&quot;at90pwm316&quot;</tt>, <tt>&quot;at90scr100&quot;</tt>, <tt>&quot;at90usb646&quot;</tt>, <tt>&quot;at90usb647&quot;</tt>, <tt>&quot;at94k&quot;</tt>, <tt>&quot;m3000&quot;</tt>.</p>
<dt>&quot;avr51&quot;</p>
<dd>&#8220;Enhanced&#8221; devices with 128@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atmega128&quot;</tt>, <tt>&quot;atmega128a&quot;</tt>, <tt>&quot;atmega128rfa1&quot;</tt>, <tt>&quot;atmega1280&quot;</tt>, <tt>&quot;atmega1281&quot;</tt>, <tt>&quot;atmega1284&quot;</tt>, <tt>&quot;atmega1284p&quot;</tt>, <tt>&quot;at90can128&quot;</tt>, <tt>&quot;at90usb1286&quot;</tt>, <tt>&quot;at90usb1287&quot;</tt>.</p>
<dt>&quot;avr6&quot;</p>
<dd>&#8220;Enhanced&#8221; devices with 3-byte <font SIZE="-1">PC,</font> i.e. with more than 128@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atmega2560&quot;</tt>, <tt>&quot;atmega2561&quot;</tt>.</p>
<dt>&quot;avrxmega2&quot;</p>
<dd>&#8220;<font SIZE="-1">XMEGA&#8221;</font> devices with more than 8@tie{}KiB and up to 64@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atmxt112sl&quot;</tt>, <tt>&quot;atmxt224&quot;</tt>, <tt>&quot;atmxt224e&quot;</tt>, <tt>&quot;atmxt336s&quot;</tt>, <tt>&quot;atxmega16a4&quot;</tt>, <tt>&quot;atxmega16a4u&quot;</tt>, <tt>&quot;atxmega16c4&quot;</tt>, <tt>&quot;atxmega16d4&quot;</tt>, <tt>&quot;atxmega32a4&quot;</tt>, <tt>&quot;atxmega32a4u&quot;</tt>, <tt>&quot;atxmega32c4&quot;</tt>, <tt>&quot;atxmega32d4&quot;</tt>, <tt>&quot;atxmega32e5&quot;</tt>, <tt>&quot;atxmega32x1&quot;</tt>.</p>
<dt>&quot;avrxmega4&quot;</p>
<dd>&#8220;<font SIZE="-1">XMEGA&#8221;</font> devices with more than 64@tie{}KiB and up to 128@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atxmega64a3&quot;</tt>, <tt>&quot;atxmega64a3u&quot;</tt>, <tt>&quot;atxmega64a4u&quot;</tt>, <tt>&quot;atxmega64b1&quot;</tt>, <tt>&quot;atxmega64b3&quot;</tt>, <tt>&quot;atxmega64c3&quot;</tt>, <tt>&quot;atxmega64d3&quot;</tt>, <tt>&quot;atxmega64d4&quot;</tt>.</p>
<dt>&quot;avrxmega5&quot;</p>
<dd>&#8220;<font SIZE="-1">XMEGA&#8221;</font> devices with more than 64@tie{}KiB and up to 128@tie{}KiB of program memory and more than 64@tie{}KiB of <font SIZE="-1">RAM. </font><i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atxmega64a1&quot;</tt>, <tt>&quot;atxmega64a1u&quot;</tt>.</p>
<dt>&quot;avrxmega6&quot;</p>
<dd>&#8220;<font SIZE="-1">XMEGA&#8221;</font> devices with more than 128@tie{}KiB of program memory. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atmxt540s&quot;</tt>, <tt>&quot;atmxt540sreva&quot;</tt>, <tt>&quot;atxmega128a3&quot;</tt>, <tt>&quot;atxmega128a3u&quot;</tt>, <tt>&quot;atxmega128b1&quot;</tt>, <tt>&quot;atxmega128b3&quot;</tt>, <tt>&quot;atxmega128c3&quot;</tt>, <tt>&quot;atxmega128d3&quot;</tt>, <tt>&quot;atxmega128d4&quot;</tt>, <tt>&quot;atxmega192a3&quot;</tt>, <tt>&quot;atxmega192a3u&quot;</tt>, <tt>&quot;atxmega192c3&quot;</tt>, <tt>&quot;atxmega192d3&quot;</tt>, <tt>&quot;atxmega256a3&quot;</tt>, <tt>&quot;atxmega256a3b&quot;</tt>, <tt>&quot;atxmega256a3bu&quot;</tt>, <tt>&quot;atxmega256a3u&quot;</tt>, <tt>&quot;atxmega256c3&quot;</tt>, <tt>&quot;atxmega256d3&quot;</tt>, <tt>&quot;atxmega384c3&quot;</tt>, <tt>&quot;atxmega384d3&quot;</tt>.</p>
<dt>&quot;avrxmega7&quot;</p>
<dd>&#8220;<font SIZE="-1">XMEGA&#8221;</font> devices with more than 128@tie{}KiB of program memory and more than 64@tie{}KiB of <font SIZE="-1">RAM. </font><i>mcu</i><tt>@tie</tt>{}= <tt>&quot;atxmega128a1&quot;</tt>, <tt>&quot;atxmega128a1u&quot;</tt>, <tt>&quot;atxmega128a4u&quot;</tt>.</p>
<dt>&quot;avr1&quot;</p>
<dd>This <font SIZE="-1">ISA</font> is implemented by the minimal <font SIZE="-1">AVR</font> core and supported for assembler only. <i>mcu</i><tt>@tie</tt>{}= <tt>&quot;attiny11&quot;</tt>, <tt>&quot;attiny12&quot;</tt>, <tt>&quot;attiny15&quot;</tt>, <tt>&quot;attiny28&quot;</tt>, <tt>&quot;at90s1200&quot;</tt>.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-maccumulate-args</code></p>
<dd>Accumulate outgoing function arguments and acquire/release the needed stack space for outgoing function arguments once in function prologue/epilogue. Without this option, outgoing arguments are pushed before calling a function and popped afterwards. </p>
<p> Popping the arguments after the function call can be expensive on <font SIZE="-1">AVR</font> so that accumulating the stack space might lead to smaller executables because arguments need not to be removed from the stack after such a function call. </p>
<p> This option can lead to reduced code size for functions that perform several calls to functions that get their arguments on the stack like calls to printf-like functions.</p>
<dt><code>-mbranch-cost=</code><i>cost</i></p>
<dd>Set the branch costs for conditional branch instructions to <i>cost</i>. Reasonable values for <i>cost</i> are small, non-negative integers. The default branch cost is 0.</p>
<dt><code>-mcall-prologues</code></p>
<dd>Functions prologues/epilogues are expanded as calls to appropriate subroutines. Code size is smaller.</p>
<dt><code>-mint8</code></p>
<dd>Assume <tt>&quot;int&quot;</tt> to be 8-bit integer. This affects the sizes of all types: a <tt>&quot;char&quot;</tt> is 1 byte, an <tt>&quot;int&quot;</tt> is 1 byte, a <tt>&quot;long&quot;</tt> is 2 bytes, and <tt>&quot;long long&quot;</tt> is 4 bytes. Please note that this option does not conform to the C standards, but it results in smaller code size.</p>
<dt><code>-mno-interrupts</code></p>
<dd>Generated code is not compatible with hardware interrupts. Code size is smaller.</p>
<dt><code>-mrelax</code></p>
<dd>Try to replace <tt>&quot;CALL&quot;</tt> resp. <tt>&quot;JMP&quot;</tt> instruction by the shorter <tt>&quot;RCALL&quot;</tt> resp. <tt>&quot;RJMP&quot;</tt> instruction if applicable. Setting <tt>&quot;-mrelax&quot;</tt> just adds the <tt>&quot;--relax&quot;</tt> option to the linker command line when the linker is called. </p>
<p> Jump relaxing is performed by the linker because jump offsets are not known before code is located. Therefore, the assembler code generated by the compiler is the same, but the instructions in the executable may differ from instructions in the assembler code. </p>
<p> Relaxing must be turned on if linker stubs are needed, see the section on <tt>&quot;EIND&quot;</tt> and linker stubs below.</p>
<dt><code>-msp8</code></p>
<dd>Treat the stack pointer register as an 8-bit register, i.e. assume the high byte of the stack pointer is zero. In general, you don&#8217;t need to set this option by hand. </p>
<p> This option is used internally by the compiler to select and build multilibs for architectures <tt>&quot;avr2&quot;</tt> and <tt>&quot;avr25&quot;</tt>. These architectures mix devices with and without <tt>&quot;SPH&quot;</tt>. For any setting other than <tt>&quot;-mmcu=avr2&quot;</tt> or <tt>&quot;-mmcu=avr25&quot;</tt> the compiler driver will add or remove this option from the compiler proper&#8217;s command line, because the compiler then knows if the device or architecture has an 8-bit stack pointer and thus no <tt>&quot;SPH&quot;</tt> register or not.</p>
<dt><code>-mstrict-X</code></p>
<dd>Use address register <tt>&quot;X&quot;</tt> in a way proposed by the hardware. This means that <tt>&quot;X&quot;</tt> is only used in indirect, post-increment or pre-decrement addressing. </p>
<p> Without this option, the <tt>&quot;X&quot;</tt> register may be used in the same way as <tt>&quot;Y&quot;</tt> or <tt>&quot;Z&quot;</tt> which then is emulated by additional instructions. For example, loading a value with <tt>&quot;X+const&quot;</tt> addressing with a small non-negative <tt>&quot;const &lt; 64&quot;</tt> to a register <i>Rn</i> is performed as </p>
<pre> adiw r26, const ; X += const
 ld &lt;Rn&gt;, X ; &lt;Rn&gt; = *X
 sbiw r26, const ; X -= const</pre>
<dt><code>-mtiny-stack</code></p>
<dd>Only change the lower 8@tie{}bits of the stack pointer.</p>
<dt><code>-Waddr-space-convert</code></p>
<dd>Warn about conversions between address spaces in the case where the resulting address space is not contained in the incoming address space.</dl>
<p> <tt>&quot;EIND&quot;</tt> and Devices with more than 128 Ki Bytes of Flash </p>
<p> Pointers in the implementation are 16@tie{}bits wide. The address of a function or label is represented as word address so that indirect jumps and calls can target any code address in the range of 64@tie{}Ki words. </p>
<p> In order to facilitate indirect jump on devices with more than 128@tie{}Ki bytes of program memory space, there is a special function register called <tt>&quot;EIND&quot;</tt> that serves as most significant part of the target address when <tt>&quot;EICALL&quot;</tt> or <tt>&quot;EIJMP&quot;</tt> instructions are used. </p>
<p> Indirect jumps and calls on these devices are handled as follows by the compiler and are subject to some limitations:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The compiler never sets <tt>&quot;EIND&quot;</tt>.</p>
<dt>&bull;</p>
<dd>The compiler uses <tt>&quot;EIND&quot;</tt> implicitely in <tt>&quot;EICALL&quot;</tt>/<tt>&quot;EIJMP&quot;</tt> instructions or might read <tt>&quot;EIND&quot;</tt> directly in order to emulate an indirect call/jump by means of a <tt>&quot;RET&quot;</tt> instruction.</p>
<dt>&bull;</p>
<dd>The compiler assumes that <tt>&quot;EIND&quot;</tt> never changes during the startup code or during the application. In particular, <tt>&quot;EIND&quot;</tt> is not saved/restored in function or interrupt service routine prologue/epilogue.</p>
<dt>&bull;</p>
<dd>For indirect calls to functions and computed goto, the linker generates <i>stubs</i>. Stubs are jump pads sometimes also called <i>trampolines</i>. Thus, the indirect call/jump jumps to such a stub. The stub contains a direct jump to the desired address.</p>
<dt>&bull;</p>
<dd>Linker relaxation must be turned on so that the linker will generate the stubs correctly an all situaltion. See the compiler option <tt>&quot;-mrelax&quot;</tt> and the linler option <tt>&quot;--relax&quot;</tt>. There are corner cases where the linker is supposed to generate stubs but aborts without relaxation and without a helpful error message.</p>
<dt>&bull;</p>
<dd>The default linker script is arranged for code with <tt>&quot;EIND = 0&quot;</tt>. If code is supposed to work for a setup with <tt>&quot;EIND != 0&quot;</tt>, a custom linker script has to be used in order to place the sections whose name start with <tt>&quot;.trampolines&quot;</tt> into the segment where <tt>&quot;EIND&quot;</tt> points to.</p>
<dt>&bull;</p>
<dd>The startup code from libgcc never sets <tt>&quot;EIND&quot;</tt>. Notice that startup code is a blend of code from libgcc and AVR-LibC. For the impact of AVR-LibC on <tt>&quot;EIND&quot;</tt>, see the AVR-LibC user manual (<tt>&quot;<a rel="nofollow" href="http://nongnu.org/avr-libc/user-manual/">http://nongnu.org/avr-libc/user-manual/</a>&quot;</tt>).</p>
<dt>&bull;</p>
<dd>It is legitimate for user-specific startup code to set up <tt>&quot;EIND&quot;</tt> early, for example by means of initialization code located in section <tt>&quot;.init3&quot;</tt>. Such code runs prior to general startup code that initializes <font SIZE="-1">RAM</font> and calls constructors, but after the bit of startup code from AVR-LibC that sets <tt>&quot;EIND&quot;</tt> to the segment where the vector table is located. </p>
<pre> #include &lt;avr/io.h&gt;
 
 static void
 __attribute__((section(&quot;.init3&quot;),naked,used,no_instrument_function))
 init3_set_eind (void)
 {
 __asm volatile (&quot;ldi r24,pm_hh8(__trampolines_start)
	&quot;
 &quot;out %i0,r24&quot; :: &quot;n&quot; (&amp;EIND) : &quot;r24&quot;,&quot;memory&quot;);
 }</pre>
<p>The <tt>&quot;__trampolines_start&quot;</tt> symbol is defined in the linker script.</p>
<dt>&bull;</p>
<dd>Stubs are generated automatically by the linker if the following two conditions are met:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>-&lt;The address of a label is taken by means of the &quot;gs&quot; modifier&gt;</p>
<dd>(short for <i>generate stubs</i>) like so: </p>
<pre> LDI r24, lo8(gs(&lt;func&gt;))
 LDI r25, hi8(gs(&lt;func&gt;))</pre>
<dt>-&lt;The final location of that label is in a code segment&gt;</p>
<dd><i>outside</i> the segment where the stubs are located.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>&bull;</p>
<dd>The compiler emits such <tt>&quot;gs&quot;</tt> modifiers for code labels in the following situations:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>-&lt;Taking address of a function or code label.&gt;</p>
<dd>
<dt>-&lt;Computed goto.&gt;</p>
<dd>
<dt>-&lt;If prologue-save function is used, see <code>-mcall-prologues</code>&gt;</p>
<dd>command-line option.</p>
<dt>-&lt;Switch/case dispatch tables. If you do not want such dispatch&gt;</p>
<dd>tables you can specify the <code>-fno-jump-tables</code> command-line option.</p>
<dt>-&lt;C and C<font SIZE="-2">++</font> constructors/destructors called during startup/shutdown.&gt;</p>
<dd>
<dt>-&lt;If the tools hit a &quot;gs()&quot; modifier explained above.&gt;</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>&bull;</p>
<dd>Jumping to non-symbolic addresses like so is <i>not</i> supported: </p>
<pre> int main (void)
 {
 /* Call function at word address 0x2 */
 return ((int(*)(void)) 0x2)();
 }</pre>
<p>Instead, a stub has to be set up, i.e. the function has to be called through a symbol (<tt>&quot;func_4&quot;</tt> in the example): </p>
<pre> int main (void)
 {
 extern int func_4 (void);
 
 /* Call function at byte address 0x4 */
 return func_4();
 }</pre>
<p>and the application be linked with <tt>&quot;-Wl,--defsym,func_4=0x4&quot;</tt>. Alternatively, <tt>&quot;func_4&quot;</tt> can be defined in the linker script.</dl>
<p> Handling of the <tt>&quot;RAMPD&quot;</tt>, <tt>&quot;RAMPX&quot;</tt>, <tt>&quot;RAMPY&quot;</tt> and <tt>&quot;RAMPZ&quot;</tt> Special Function Registers </p>
<p> Some <font SIZE="-1">AVR</font> devices support memories larger than the 64@tie{}KiB range that can be accessed with 16-bit pointers. To access memory locations outside this 64@tie{}KiB range, the contentent of a <tt>&quot;RAMP&quot;</tt> register is used as high part of the address: The <tt>&quot;X&quot;</tt>, <tt>&quot;Y&quot;</tt>, <tt>&quot;Z&quot;</tt> address register is concatenated with the <tt>&quot;RAMPX&quot;</tt>, <tt>&quot;RAMPY&quot;</tt>, <tt>&quot;RAMPZ&quot;</tt> special function register, respectively, to get a wide address. Similarly, <tt>&quot;RAMPD&quot;</tt> is used together with direct addressing.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The startup code initializes the <tt>&quot;RAMP&quot;</tt> special function registers with zero.</p>
<dt>&bull;</p>
<dd>If a <font SIZE="-1"><code>AVR</code></font><code> Named Address Spaces,named address space</code> other than generic or <tt>&quot;__flash&quot;</tt> is used, then <tt>&quot;RAMPZ&quot;</tt> is set as needed before the operation.</p>
<dt>&bull;</p>
<dd>If the device supports <font SIZE="-1">RAM</font> larger than 64@tie{}KiB and the compiler needs to change <tt>&quot;RAMPZ&quot;</tt> to accomplish an operation, <tt>&quot;RAMPZ&quot;</tt> is reset to zero after the operation.</p>
<dt>&bull;</p>
<dd>If the device comes with a specific <tt>&quot;RAMP&quot;</tt> register, the <font SIZE="-1">ISR</font> prologue/epilogue saves/restores that <font SIZE="-1">SFR</font> and initializes it with zero in case the <font SIZE="-1">ISR</font> code might (implicitly) use it.</p>
<dt>&bull;</p>
<dd><font SIZE="-1">RAM</font> larger than 64@tie{}KiB is not supported by <font SIZE="-1">GCC</font> for <font SIZE="-1">AVR</font> targets. If you use inline assembler to read from locations outside the 16-bit address range and change one of the <tt>&quot;RAMP&quot;</tt> registers, you must reset it to zero after the access.</dl>
<p> <font SIZE="-1">AVR</font> Built-in Macros </p>
<p> <font SIZE="-1">GCC</font> defines several built-in macros so that the user code can test for the presence or absence of features. Almost any of the following built-in macros are deduced from device capabilities and thus triggered by the <tt>&quot;-mmcu=&quot;</tt> command-line option. </p>
<p> For even more AVR-specific built-in macros see <font SIZE="-1"><code>AVR</code></font><code> Named Address Spaces</code> and <font SIZE="-1"><code>AVR</code></font><code> Built-in Functions</code>.</p>
<dl COMPACT>
<dt>&quot;__AVR_ARCH__&quot;</p>
<dd>Build-in macro that resolves to a decimal number that identifies the architecture and depends on the <tt>&quot;-mmcu=</tt>mcu<tt>&quot;</tt> option. Possible values are: </p>
<p> <tt>2</tt>, <tt>25</tt>, <tt>3</tt>, <tt>31</tt>, <tt>35</tt>, <tt>4</tt>, <tt>5</tt>, <tt>51</tt>, <tt>6</tt>, <tt>102</tt>, <tt>104</tt>, <tt>105</tt>, <tt>106</tt>, <tt>107</tt> </p>
<p> for <i>mcu</i>=<tt>&quot;avr2&quot;</tt>, <tt>&quot;avr25&quot;</tt>, <tt>&quot;avr3&quot;</tt>, <tt>&quot;avr31&quot;</tt>, <tt>&quot;avr35&quot;</tt>, <tt>&quot;avr4&quot;</tt>, <tt>&quot;avr5&quot;</tt>, <tt>&quot;avr51&quot;</tt>, <tt>&quot;avr6&quot;</tt>, <tt>&quot;avrxmega2&quot;</tt>, <tt>&quot;avrxmega4&quot;</tt>, <tt>&quot;avrxmega5&quot;</tt>, <tt>&quot;avrxmega6&quot;</tt>, <tt>&quot;avrxmega7&quot;</tt>, respectively. If <i>mcu</i> specifies a device, this built-in macro is set accordingly. For example, with <tt>&quot;-mmcu=atmega8&quot;</tt> the macro will be defined to <tt>4</tt>.</p>
<dt>&quot;__AVR_Device<tt>__&quot;</p>
<dd>Setting &quot;-mmcu=</tt>device<tt>&quot;</tt> defines this built-in macro which reflects the device&#8217;s name. For example, <tt>&quot;-mmcu=atmega8&quot;</tt> defines the built-in macro <tt>&quot;__AVR_ATmega8__&quot;</tt>, <tt>&quot;-mmcu=attiny261a&quot;</tt> defines <tt>&quot;__AVR_ATtiny261A__&quot;</tt>, etc. </p>
<p> The built-in macros&#8217; names follow the scheme <tt>&quot;__AVR_</tt>Device<tt>__&quot;</tt> where <i>Device</i> is the device name as from the <font SIZE="-1">AVR</font> user manual. The difference between <i>Device</i> in the built-in macro and <i>device</i> in <tt>&quot;-mmcu=</tt>device<tt>&quot;</tt> is that the latter is always lowercase. </p>
<p> If <i>device</i> is not a device but only a core architecture like <tt>&quot;avr51&quot;</tt>, this macro will not be defined.</p>
<dt>&quot;__AVR_XMEGA__&quot;</p>
<dd>The device / architecture belongs to the <font SIZE="-1">XMEGA</font> family of devices.</p>
<dt>&quot;__AVR_HAVE_ELPM__&quot;</p>
<dd>The device has the the <tt>&quot;ELPM&quot;</tt> instruction.</p>
<dt>&quot;__AVR_HAVE_ELPMX__&quot;</p>
<dd>The device has the <tt>&quot;ELPM R</tt>n<tt>,Z&quot;</tt> and <tt>&quot;ELPM R</tt>n<tt>,Z+&quot;</tt> instructions.</p>
<dt>&quot;__AVR_HAVE_MOVW__&quot;</p>
<dd>The device has the <tt>&quot;MOVW&quot;</tt> instruction to perform 16-bit register-register moves.</p>
<dt>&quot;__AVR_HAVE_LPMX__&quot;</p>
<dd>The device has the <tt>&quot;LPM R</tt>n<tt>,Z&quot;</tt> and <tt>&quot;LPM R</tt>n<tt>,Z+&quot;</tt> instructions.</p>
<dt>&quot;__AVR_HAVE_MUL__&quot;</p>
<dd>The device has a hardware multiplier.</p>
<dt>&quot;__AVR_HAVE_JMP_CALL__&quot;</p>
<dd>The device has the <tt>&quot;JMP&quot;</tt> and <tt>&quot;CALL&quot;</tt> instructions. This is the case for devices with at least 16@tie{}KiB of program memory.</p>
<dt>&quot;__AVR_HAVE_EIJMP_EICALL__&quot;</p>
<dd>
<dt>&quot;__AVR_3_BYTE_PC__&quot;</p>
<dd>The device has the <tt>&quot;EIJMP&quot;</tt> and <tt>&quot;EICALL&quot;</tt> instructions. This is the case for devices with more than 128@tie{}KiB of program memory. This also means that the program counter (<font SIZE="-1">PC</font>) is 3@tie{}bytes wide.</p>
<dt>&quot;__AVR_2_BYTE_PC__&quot;</p>
<dd>The program counter (<font SIZE="-1">PC</font>) is 2@tie{}bytes wide. This is the case for devices with up to 128@tie{}KiB of program memory.</p>
<dt>&quot;__AVR_HAVE_8BIT_SP__&quot;</p>
<dd>
<dt>&quot;__AVR_HAVE_16BIT_SP__&quot;</p>
<dd>The stack pointer (<font SIZE="-1">SP</font>) register is treated as 8-bit respectively 16-bit register by the compiler. The definition of these macros is affected by <tt>&quot;-mtiny-stack&quot;</tt>.</p>
<dt>&quot;__AVR_HAVE_SPH__&quot;</p>
<dd>
<dt>&quot;__AVR_SP8__&quot;</p>
<dd>The device has the <font SIZE="-1">SPH </font>(high part of stack pointer) special function register or has an 8-bit stack pointer, respectively. The definition of these macros is affected by <tt>&quot;-mmcu=&quot;</tt> and in the cases of <tt>&quot;-mmcu=avr2&quot;</tt> and <tt>&quot;-mmcu=avr25&quot;</tt> also by <tt>&quot;-msp8&quot;</tt>.</p>
<dt>&quot;__AVR_HAVE_RAMPD__&quot;</p>
<dd>
<dt>&quot;__AVR_HAVE_RAMPX__&quot;</p>
<dd>
<dt>&quot;__AVR_HAVE_RAMPY__&quot;</p>
<dd>
<dt>&quot;__AVR_HAVE_RAMPZ__&quot;</p>
<dd>The device has the <tt>&quot;RAMPD&quot;</tt>, <tt>&quot;RAMPX&quot;</tt>, <tt>&quot;RAMPY&quot;</tt>, <tt>&quot;RAMPZ&quot;</tt> special function register, respectively.</p>
<dt>&quot;__NO_INTERRUPTS__&quot;</p>
<dd>This macro reflects the <tt>&quot;-mno-interrupts&quot;</tt> command line option.</p>
<dt>&quot;__AVR_ERRATA_SKIP__&quot;</p>
<dd>
<dt>&quot;__AVR_ERRATA_SKIP_JMP_CALL__&quot;</p>
<dd>Some <font SIZE="-1">AVR</font> devices (<font SIZE="-1">AT90S8515,</font> ATmega103) must not skip 32-bit instructions because of a hardware erratum. Skip instructions are <tt>&quot;SBRS&quot;</tt>, <tt>&quot;SBRC&quot;</tt>, <tt>&quot;SBIS&quot;</tt>, <tt>&quot;SBIC&quot;</tt> and <tt>&quot;CPSE&quot;</tt>. The second macro is only defined if <tt>&quot;__AVR_HAVE_JMP_CALL__&quot;</tt> is also set.</p>
<dt>&quot;__AVR_ISA_RMW__&quot;</p>
<dd>The device has Read-Modify-Write instructions (<font SIZE="-1">XCH, LAC, LAS</font> and <font SIZE="-1">LAT</font>).</p>
<dt>&quot;__AVR_SFR_OFFSET__=offset<tt>&quot;</p>
<dd>Instructions that can address I/O special function registers directly like &quot;IN&quot;</tt>, <tt>&quot;OUT&quot;</tt>, <tt>&quot;SBI&quot;</tt>, etc. may use a different address as if addressed by an instruction to access <font SIZE="-1">RAM</font> like <tt>&quot;LD&quot;</tt> or <tt>&quot;STS&quot;</tt>. This offset depends on the device architecture and has to be subtracted from the <font SIZE="-1">RAM</font> address in order to get the respective I/O@tie{}address.</p>
<dt>&quot;__WITH_AVRLIBC__&quot;</p>
<dd>The compiler is configured to be used together with AVR-Libc. See the <tt>&quot;--with-avrlibc&quot;</tt> configure option.</dl>
<p> <i>Blackfin Options</i></p>
<dl COMPACT>
<dt><code>-mcpu=</code><i>cpu</i>[<code>&#8211;</code><i>sirevision</i>]</p>
<dd>Specifies the name of the target Blackfin processor. Currently, <i>cpu</i> can be one of <code>bf512</code>, <code>bf514</code>, <code>bf516</code>, <code>bf518</code>, <code>bf522</code>, <code>bf523</code>, <code>bf524</code>, <code>bf525</code>, <code>bf526</code>, <code>bf527</code>, <code>bf531</code>, <code>bf532</code>, <code>bf533</code>, <code>bf534</code>, <code>bf536</code>, <code>bf537</code>, <code>bf538</code>, <code>bf539</code>, <code>bf542</code>, <code>bf544</code>, <code>bf547</code>, <code>bf548</code>, <code>bf549</code>, <code>bf542m</code>, <code>bf544m</code>, <code>bf547m</code>, <code>bf548m</code>, <code>bf549m</code>, <code>bf561</code>, <code>bf592</code>. </p>
<p> The optional <i>sirevision</i> specifies the silicon revision of the target Blackfin processor. Any workarounds available for the targeted silicon revision are enabled. If <i>sirevision</i> is <code>none</code>, no workarounds are enabled. If <i>sirevision</i> is <code>any</code>, all workarounds for the targeted processor are enabled. The <tt>&quot;__SILICON_REVISION__&quot;</tt> macro is defined to two hexadecimal digits representing the major and minor numbers in the silicon revision. If <i>sirevision</i> is <code>none</code>, the <tt>&quot;__SILICON_REVISION__&quot;</tt> is not defined. If <i>sirevision</i> is <code>any</code>, the <tt>&quot;__SILICON_REVISION__&quot;</tt> is defined to be <tt>0xffff</tt>. If this optional <i>sirevision</i> is not used, <font SIZE="-1">GCC</font> assumes the latest known silicon revision of the targeted Blackfin processor. </p>
<p> <font SIZE="-1">GCC</font> defines a preprocessor macro for the specified <i>cpu</i>. For the <code>bfin-elf</code> toolchain, this option causes the hardware <font SIZE="-1">BSP</font> provided by libgloss to be linked in if <code>-msim</code> is not given. </p>
<p> Without this option, <code>bf532</code> is used as the processor by default. </p>
<p> Note that support for <code>bf561</code> is incomplete. For <code>bf561</code>, only the preprocessor macro is defined.</p>
<dt><code>-msim</code></p>
<dd>Specifies that the program will be run on the simulator. This causes the simulator <font SIZE="-1">BSP</font> provided by libgloss to be linked in. This option has effect only for <code>bfin-elf</code> toolchain. Certain other options, such as <code>-mid-shared-library</code> and <code>-mfdpic</code>, imply <code>-msim</code>.</p>
<dt><code>-momit-leaf-frame-pointer</code></p>
<dd>Don&#8217;t keep the frame pointer in a register for leaf functions. This avoids the instructions to save, set up and restore frame pointers and makes an extra register available in leaf functions. The option <code>-fomit-frame-pointer</code> removes the frame pointer for all functions, which might make debugging harder.</p>
<dt><code>-mspecld-anomaly</code></p>
<dd>When enabled, the compiler ensures that the generated code does not contain speculative loads after jump instructions. If this option is used, <tt>&quot;__WORKAROUND_SPECULATIVE_LOADS&quot;</tt> is defined.</p>
<dt><code>-mno-specld-anomaly</code></p>
<dd>Don&#8217;t generate extra code to prevent speculative loads from occurring.</p>
<dt><code>-mcsync-anomaly</code></p>
<dd>When enabled, the compiler ensures that the generated code does not contain <font SIZE="-1">CSYNC</font> or <font SIZE="-1">SSYNC</font> instructions too soon after conditional branches. If this option is used, <tt>&quot;__WORKAROUND_SPECULATIVE_SYNCS&quot;</tt> is defined.</p>
<dt><code>-mno-csync-anomaly</code></p>
<dd>Don&#8217;t generate extra code to prevent <font SIZE="-1">CSYNC</font> or <font SIZE="-1">SSYNC</font> instructions from occurring too soon after a conditional branch.</p>
<dt><code>-mlow-64k</code></p>
<dd>When enabled, the compiler is free to take advantage of the knowledge that the entire program fits into the low 64k of memory.</p>
<dt><code>-mno-low-64k</code></p>
<dd>Assume that the program is arbitrarily large. This is the default.</p>
<dt><code>-mstack-check-l1</code></p>
<dd>Do stack checking using information placed into L1 scratchpad memory by the uClinux kernel.</p>
<dt><code>-mid-shared-library</code></p>
<dd>Generate code that supports shared libraries via the library <font SIZE="-1">ID</font> method. This allows for execute in place and shared libraries in an environment without virtual memory management. This option implies <code>-fPIC</code>. With a <code>bfin-elf</code> target, this option implies <code>-msim</code>.</p>
<dt><code>-mno-id-shared-library</code></p>
<dd>Generate code that doesn&#8217;t assume ID-based shared libraries are being used. This is the default.</p>
<dt><code>-mleaf-id-shared-library</code></p>
<dd>Generate code that supports shared libraries via the library <font SIZE="-1">ID</font> method, but assumes that this library or executable won&#8217;t link against any other <font SIZE="-1">ID</font> shared libraries. That allows the compiler to use faster code for jumps and calls.</p>
<dt><code>-mno-leaf-id-shared-library</code></p>
<dd>Do not assume that the code being compiled won&#8217;t link against any <font SIZE="-1">ID</font> shared libraries. Slower code is generated for jump and call insns.</p>
<dt><code>-mshared-library-id=n</code></p>
<dd>Specifies the identification number of the ID-based shared library being compiled. Specifying a value of 0 generates more compact code; specifying other values forces the allocation of that number to the current library but is no more space- or time-efficient than omitting this option.</p>
<dt><code>-msep-data</code></p>
<dd>Generate code that allows the data segment to be located in a different area of memory from the text segment. This allows for execute in place in an environment without virtual memory management by eliminating relocations against the text section.</p>
<dt><code>-mno-sep-data</code></p>
<dd>Generate code that assumes that the data segment follows the text segment. This is the default.</p>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Tells the compiler to perform function calls by first loading the address of the function into a register and then performing a subroutine call on this register. This switch is needed if the target function lies outside of the 24-bit addressing range of the offset-based version of subroutine call instruction. </p>
<p> This feature is not enabled by default. Specifying <code>-mno-long-calls</code> restores the default behavior. Note these switches have no effect on how the compiler generates code to handle function calls via function pointers.</p>
<dt><code>-mfast-fp</code></p>
<dd>Link with the fast floating-point library. This library relaxes some of the <font SIZE="-1">IEEE</font> floating-point standard&#8217;s rules for checking inputs against Not-a-Number (<font SIZE="-1">NAN</font>), in the interest of performance.</p>
<dt><code>-minline-plt</code></p>
<dd>Enable inlining of <font SIZE="-1">PLT</font> entries in function calls to functions that are not known to bind locally. It has no effect without <code>-mfdpic</code>.</p>
<dt><code>-mmulticore</code></p>
<dd>Build a standalone application for multicore Blackfin processors. This option causes proper start files and link scripts supporting multicore to be used, and defines the macro <tt>&quot;__BFIN_MULTICORE&quot;</tt>. It can only be used with <code>-mcpu=bf561</code>[<code>&#8211;</code><i>sirevision</i>]. </p>
<p> This option can be used with <code>-mcorea</code> or <code>-mcoreb</code>, which selects the one-application-per-core programming model. Without <code>-mcorea</code> or <code>-mcoreb</code>, the single-application/dual-core programming model is used. In this model, the main function of Core B should be named as <tt>&quot;coreb_main&quot;</tt>. </p>
<p> If this option is not used, the single-core application programming model is used.</p>
<dt><code>-mcorea</code></p>
<dd>Build a standalone application for Core A of <font SIZE="-1">BF561</font> when using the one-application-per-core programming model. Proper start files and link scripts are used to support Core A, and the macro <tt>&quot;__BFIN_COREA&quot;</tt> is defined. This option can only be used in conjunction with <code>-mmulticore</code>.</p>
<dt><code>-mcoreb</code></p>
<dd>Build a standalone application for Core B of <font SIZE="-1">BF561</font> when using the one-application-per-core programming model. Proper start files and link scripts are used to support Core B, and the macro <tt>&quot;__BFIN_COREB&quot;</tt> is defined. When this option is used, <tt>&quot;coreb_main&quot;</tt> should be used instead of <tt>&quot;main&quot;</tt>. This option can only be used in conjunction with <code>-mmulticore</code>.</p>
<dt><code>-msdram</code></p>
<dd>Build a standalone application for <font SIZE="-1">SDRAM.</font> Proper start files and link scripts are used to put the application into <font SIZE="-1">SDRAM,</font> and the macro <tt>&quot;__BFIN_SDRAM&quot;</tt> is defined. The loader should initialize <font SIZE="-1">SDRAM</font> before loading the application.</p>
<dt><code>-micplb</code></p>
<dd>Assume that ICPLBs are enabled at run time. This has an effect on certain anomaly workarounds. For Linux targets, the default is to assume ICPLBs are enabled; for standalone applications the default is off.</dl>
<p> <i>C6X Options</i></p>
<dl COMPACT>
<dt><code>-march=</code><i>name</i></p>
<dd>This specifies the name of the target architecture. <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. Permissible names are: <code>c62x</code>, <code>c64x</code>, <code>c64x+</code>, <code>c67x</code>, <code>c67x+</code>, <code>c674x</code>.</p>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a big-endian target.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a little-endian target. This is the default.</p>
<dt><code>-msim</code></p>
<dd>Choose startup files and linker script suitable for the simulator.</p>
<dt><code>-msdata=default</code></p>
<dd>Put small global and static data in the <code>.neardata</code> section, which is pointed to by register <tt>&quot;B14&quot;</tt>. Put small uninitialized global and static data in the <code>.bss</code> section, which is adjacent to the <code>.neardata</code> section. Put small read-only data into the <code>.rodata</code> section. The corresponding sections used for large pieces of data are <code>.fardata</code>, <code>.far</code> and <code>.const</code>.</p>
<dt><code>-msdata=all</code></p>
<dd>Put all data, not just small objects, into the sections reserved for small data, and use addressing relative to the <tt>&quot;B14&quot;</tt> register to access them.</p>
<dt><code>-msdata=none</code></p>
<dd>Make no use of the sections reserved for small data, and use absolute addresses to access all data. Put all initialized global and static data in the <code>.fardata</code> section, and all uninitialized data in the <code>.far</code> section. Put all constant data into the <code>.const</code> section.</dl>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i> </p>
<p> These options are defined specifically for the <font SIZE="-1">CRIS</font> ports.</p>
<dl COMPACT>
<dt><code>-march=</code><i>architecture-type</i></p>
<dd>
<dt><code>-mcpu=</code><i>architecture-type</i></p>
<dd>Generate code for the specified architecture. The choices for <i>architecture-type</i> are <code>v3</code>, <code>v8</code> and <code>v10</code> for respectively <font SIZE="-1">ETRAX</font>&nbsp;<wbr>4, <font SIZE="-1">ETRAX</font>&nbsp;<wbr>100, and <font SIZE="-1">ETRAX</font>&nbsp;<wbr>100&nbsp;<wbr><font SIZE="-1">LX.</font> Default is <code>v0</code> except for cris-axis-linux-gnu, where the default is <code>v10</code>.</p>
<dt><code>-mtune=</code><i>architecture-type</i></p>
<dd>Tune to <i>architecture-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The choices for <i>architecture-type</i> are the same as for <code>-march=</code><i>architecture-type</i>.</p>
<dt><code>-mmax-stack-frame=</code><i>n</i></p>
<dd>Warn when the stack frame of a function exceeds <i>n</i> bytes.</p>
<dt><code>-metrax4</code></p>
<dd>
<dt><code>-metrax100</code></p>
<dd>The options <code>-metrax4</code> and <code>-metrax100</code> are synonyms for <code>-march=v3</code> and <code>-march=v8</code> respectively.</p>
<dt><code>-mmul-bug-workaround</code></p>
<dd>
<dt><code>-mno-mul-bug-workaround</code></p>
<dd>Work around a bug in the <tt>&quot;muls&quot;</tt> and <tt>&quot;mulu&quot;</tt> instructions for <font SIZE="-1">CPU</font> models where it applies. This option is active by default.</p>
<dt><code>-mpdebug</code></p>
<dd>Enable CRIS-specific verbose debug-related information in the assembly code. This option also has the effect of turning off the <code>#NO_APP</code> formatted-code indicator to the assembler at the beginning of the assembly file.</p>
<dt><code>-mcc-init</code></p>
<dd>Do not use condition-code results from previous instruction; always emit compare and test instructions before use of condition codes.</p>
<dt><code>-mno-side-effects</code></p>
<dd>Do not emit instructions with side effects in addressing modes other than post-increment.</p>
<dt><code>-mstack-align</code></p>
<dd>
<dt><code>-mno-stack-align</code></p>
<dd>
<dt><code>-mdata-align</code></p>
<dd>
<dt><code>-mno-data-align</code></p>
<dd>
<dt><code>-mconst-align</code></p>
<dd>
<dt><code>-mno-const-align</code></p>
<dd>These options (<code>no-</code> options) arrange (eliminate arrangements) for the stack frame, individual data and constants to be aligned for the maximum single data access size for the chosen <font SIZE="-1">CPU</font> model. The default is to arrange for 32-bit alignment. <font SIZE="-1">ABI</font> details such as structure layout are not affected by these options.</p>
<dt><code>-m32-bit</code></p>
<dd>
<dt><code>-m16-bit</code></p>
<dd>
<dt><code>-m8-bit</code></p>
<dd>Similar to the stack- data- and const-align options above, these options arrange for stack frame, writable data and constants to all be 32-bit, 16-bit or 8-bit aligned. The default is 32-bit alignment.</p>
<dt><code>-mno-prologue-epilogue</code></p>
<dd>
<dt><code>-mprologue-epilogue</code></p>
<dd>With <code>-mno-prologue-epilogue</code>, the normal function prologue and epilogue which set up the stack frame are omitted and no return instructions or return sequences are generated in the code. Use this option only together with visual inspection of the compiled code: no warnings or errors are generated when call-saved registers must be saved, or storage for local variables needs to be allocated.</p>
<dt><code>-mno-gotplt</code></p>
<dd>
<dt><code>-mgotplt</code></p>
<dd>With <code>-fpic</code> and <code>-fPIC</code>, don&#8217;t generate (do generate) instruction sequences that load addresses for functions from the <font SIZE="-1">PLT</font> part of the <font SIZE="-1">GOT</font> rather than (traditional on other architectures) calls to the <font SIZE="-1">PLT. </font> The default is <code>-mgotplt</code>.</p>
<dt><code>-melf</code></p>
<dd>Legacy no-op option only recognized with the cris-axis-elf and cris-axis-linux-gnu targets.</p>
<dt><code>-mlinux</code></p>
<dd>Legacy no-op option only recognized with the cris-axis-linux-gnu target.</p>
<dt><code>-sim</code></p>
<dd>This option, recognized for the cris-axis-elf, arranges to link with input-output functions from a simulator library. Code, initialized data and zero-initialized data are allocated consecutively.</p>
<dt><code>-sim2</code></p>
<dd>Like <code>-sim</code>, but pass linker options to locate initialized data at 0x40000000 and zero-initialized data at 0x80000000.</dl>
<p> <i></i><font SIZE="-1"><i>CR16</i></font><i> Options</i> </p>
<p> These options are defined specifically for the <font SIZE="-1">CR16</font> ports.</p>
<dl COMPACT>
<dt><code>-mmac</code></p>
<dd>Enable the use of multiply-accumulate instructions. Disabled by default.</p>
<dt><code>-mcr16cplus</code></p>
<dd>
<dt><code>-mcr16c</code></p>
<dd>Generate code for <font SIZE="-1">CR16C</font> or <font SIZE="-1">CR16C+</font> architecture. <font SIZE="-1">CR16C+</font> architecture is default.</p>
<dt><code>-msim</code></p>
<dd>Links the library libsim.a which is in compatible with simulator. Applicable to <font SIZE="-1">ELF</font> compiler only.</p>
<dt><code>-mint32</code></p>
<dd>Choose integer type as 32-bit wide.</p>
<dt><code>-mbit-ops</code></p>
<dd>Generates <tt>&quot;sbit&quot;</tt>/<tt>&quot;cbit&quot;</tt> instructions for bit manipulations.</p>
<dt><code>-mdata-model=</code><i>model</i></p>
<dd>Choose a data model. The choices for <i>model</i> are <code>near</code>, <code>far</code> or <code>medium</code>. <code>medium</code> is default. However, <code>far</code> is not valid with <code>-mcr16c</code>, as the <font SIZE="-1">CR16C</font> architecture does not support the far data model.</dl>
<p> <i>Darwin Options</i> </p>
<p> These options are defined for all architectures running the Darwin operating system. </p>
<p> <font SIZE="-1">FSF GCC</font> on Darwin does not create &#8220;fat&#8221; object files; it creates an object file for the single architecture that <font SIZE="-1">GCC</font> was built to target. Apple&#8217;s <font SIZE="-1">GCC</font> on Darwin does create &#8220;fat&#8221; files if multiple <code>-arch</code> options are used; it does so by running the compiler or linker multiple times and joining the results together with <i>lipo</i>. </p>
<p> The subtype of the file created (like <code>ppc7400</code> or <code>ppc970</code> or <code>i686</code>) is determined by the flags that specify the <font SIZE="-1">ISA</font> that <font SIZE="-1">GCC</font> is targeting, like <code>-mcpu</code> or <code>-march</code>. The <code>-force_cpusubtype_ALL</code> option can be used to override this. </p>
<p> The Darwin tools vary in their behavior when presented with an <font SIZE="-1">ISA</font> mismatch. The assembler, <i>as</i>, only permits instructions to be used that are valid for the subtype of the file it is generating, so you cannot put 64-bit instructions in a <code>ppc750</code> object file. The linker for shared libraries, <i>/usr/bin/libtool</i>, fails and prints an error if asked to create a shared library with a less restrictive subtype than its input files (for instance, trying to put a <code>ppc970</code> object file in a <code>ppc7400</code> library). The linker for executables, <code>ld</code>, quietly gives the executable the most restrictive subtype of any of its input files.</p>
<dl COMPACT>
<dt><code>-F</code><i>dir</i></p>
<dd>Add the framework directory <i>dir</i> to the head of the list of directories to be searched for header files. These directories are interleaved with those specified by <code>-I</code> options and are scanned in a left-to-right order. </p>
<p> A framework directory is a directory with frameworks in it. A framework is a directory with a <i>Headers</i> and/or <i>PrivateHeaders</i> directory contained directly in it that ends in <i>.framework</i>. The name of a framework is the name of this directory excluding the <i>.framework</i>. Headers associated with the framework are found in one of those two directories, with <i>Headers</i> being searched first. A subframework is a framework directory that is in a framework&#8217;s <i>Frameworks</i> directory. Includes of subframework headers can only appear in a header of a framework that contains the subframework, or in a sibling subframework header. Two subframeworks are siblings if they occur in the same framework. A subframework should not have the same name as a framework; a warning is issued if this is violated. Currently a subframework cannot have subframeworks; in the future, the mechanism may be extended to support this. The standard frameworks can be found in <i>/System/Library/Frameworks</i> and <i>/Library/Frameworks</i>. An example include looks like <tt>&quot;#include &lt;Framework/header.h&gt;&quot;</tt>, where <i>Framework</i> denotes the name of the framework and <i>header.h</i> is found in the <i>PrivateHeaders</i> or <i>Headers</i> directory.</p>
<dt><code>-iframework</code><i>dir</i></p>
<dd>Like <code>-F</code> except the directory is a treated as a system directory. The main difference between this <code>-iframework</code> and <code>-F</code> is that with <code>-iframework</code> the compiler does not warn about constructs contained within header files found via <i>dir</i>. This option is valid only for the C family of languages.</p>
<dt><code>-gused</code></p>
<dd>Emit debugging information for symbols that are used. For stabs debugging format, this enables <code>-feliminate-unused-debug-symbols</code>. This is by default <font SIZE="-1">ON.</font></p>
<dt><code>-gfull</code></p>
<dd>Emit debugging information for all symbols and types.</p>
<dt><code>-mmacosx-version-min=</code><i>version</i></p>
<dd>The earliest version of MacOS X that this executable will run on is <i>version</i>. Typical values of <i>version</i> include <tt>10.1</tt>, <tt>10.2</tt>, and <tt>10.3.9</tt>. </p>
<p> If the compiler was built to use the system&#8217;s headers by default, then the default for this option is the system version on which the compiler is running, otherwise the default is to make choices that are compatible with as many systems and code bases as possible.</p>
<dt><code>-mkernel</code></p>
<dd>Enable kernel development mode. The <code>-mkernel</code> option sets <code>-static</code>, <code>-fno-common</code>, <code>-fno-use-cxa-atexit</code>, <code>-fno-exceptions</code>, <code>-fno-non-call-exceptions</code>, <code>-fapple-kext</code>, <code>-fno-weak</code> and <code>-fno-rtti</code> where applicable. This mode also sets <code>-mno-altivec</code>, <code>-msoft-float</code>, <code>-fno-builtin</code> and <code>-mlong-branch</code> for PowerPC targets.</p>
<dt><code>-mone-byte-bool</code></p>
<dd>Override the defaults for <code>bool</code> so that <code>sizeof(bool)==1</code>. By default <code>sizeof(bool)</code> is <code>4</code> when compiling for Darwin/PowerPC and <code>1</code> when compiling for Darwin/x86, so this option has no effect on x86. </p>
<p> <code>Warning:</code> The <code>-mone-byte-bool</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Using this switch may require recompiling all other modules in a program, including system libraries. Use this switch to conform to a non-default data model.</p>
<dt><code>-mfix-and-continue</code></p>
<dd>
<dt><code>-ffix-and-continue</code></p>
<dd>
<dt><code>-findirect-data</code></p>
<dd>Generate code suitable for fast turnaround development, such as to allow <font SIZE="-1">GDB</font> to dynamically load <tt>&quot;.o&quot;</tt> files into already-running programs. <code>-findirect-data</code> and <code>-ffix-and-continue</code> are provided for backwards compatibility.</p>
<dt><code>-all_load</code></p>
<dd>Loads all members of static archive libraries. See man <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) for more information.</p>
<dt><code>-arch_errors_fatal</code></p>
<dd>Cause the errors having to do with files that have the wrong architecture to be fatal.</p>
<dt><code>-bind_at_load</code></p>
<dd>Causes the output file to be marked such that the dynamic linker will bind all undefined references when the file is loaded or launched.</p>
<dt><code>-bundle</code></p>
<dd>Produce a Mach-o bundle format file. See man <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) for more information.</p>
<dt><code>-bundle_loader</code> <i>executable</i></p>
<dd>This option specifies the <i>executable</i> that will load the build output file being linked. See man <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) for more information.</p>
<dt><code>-dynamiclib</code></p>
<dd>When passed this option, <font SIZE="-1">GCC</font> produces a dynamic library instead of an executable when linking, using the Darwin <i>libtool</i> command.</p>
<dt><code>-force_cpusubtype_ALL</code></p>
<dd>This causes <font SIZE="-1">GCC</font>&#8216;s output file to have the <i></i><font SIZE="-1"><i>ALL</i></font><i></i> subtype, instead of one controlled by the <code>-mcpu</code> or <code>-march</code> option.</p>
<dt><code>-allowable_client</code> <i>client_name</i></p>
<dd>
<dt><code>-client_name</code></p>
<dd>
<dt><code>-compatibility_version</code></p>
<dd>
<dt><code>-current_version</code></p>
<dd>
<dt><code>-dead_strip</code></p>
<dd>
<dt><code>-dependency-file</code></p>
<dd>
<dt><code>-dylib_file</code></p>
<dd>
<dt><code>-dylinker_install_name</code></p>
<dd>
<dt><code>-dynamic</code></p>
<dd>
<dt><code>-exported_symbols_list</code></p>
<dd>
<dt><code>-filelist</code></p>
<dd>
<dt><code>-flat_namespace</code></p>
<dd>
<dt><code>-force_flat_namespace</code></p>
<dd>
<dt><code>-headerpad_max_install_names</code></p>
<dd>
<dt><code>-image_base</code></p>
<dd>
<dt><code>-init</code></p>
<dd>
<dt><code>-install_name</code></p>
<dd>
<dt><code>-keep_private_externs</code></p>
<dd>
<dt><code>-multi_module</code></p>
<dd>
<dt><code>-multiply_defined</code></p>
<dd>
<dt><code>-multiply_defined_unused</code></p>
<dd>
<dt><code>-noall_load</code></p>
<dd>
<dt><code>-no_dead_strip_inits_and_terms</code></p>
<dd>
<dt><code>-nofixprebinding</code></p>
<dd>
<dt><code>-nomultidefs</code></p>
<dd>
<dt><code>-noprebind</code></p>
<dd>
<dt><code>-noseglinkedit</code></p>
<dd>
<dt><code>-pagezero_size</code></p>
<dd>
<dt><code>-prebind</code></p>
<dd>
<dt><code>-prebind_all_twolevel_modules</code></p>
<dd>
<dt><code>-private_bundle</code></p>
<dd>
<dt><code>-read_only_relocs</code></p>
<dd>
<dt><code>-sectalign</code></p>
<dd>
<dt><code>-sectobjectsymbols</code></p>
<dd>
<dt><code>-whyload</code></p>
<dd>
<dt><code>-seg1addr</code></p>
<dd>
<dt><code>-sectcreate</code></p>
<dd>
<dt><code>-sectobjectsymbols</code></p>
<dd>
<dt><code>-sectorder</code></p>
<dd>
<dt><code>-segaddr</code></p>
<dd>
<dt><code>-segs_read_only_addr</code></p>
<dd>
<dt><code>-segs_read_write_addr</code></p>
<dd>
<dt><code>-seg_addr_table</code></p>
<dd>
<dt><code>-seg_addr_table_filename</code></p>
<dd>
<dt><code>-seglinkedit</code></p>
<dd>
<dt><code>-segprot</code></p>
<dd>
<dt><code>-segs_read_only_addr</code></p>
<dd>
<dt><code>-segs_read_write_addr</code></p>
<dd>
<dt><code>-single_module</code></p>
<dd>
<dt><code>-static</code></p>
<dd>
<dt><code>-sub_library</code></p>
<dd>
<dt><code>-sub_umbrella</code></p>
<dd>
<dt><code>-twolevel_namespace</code></p>
<dd>
<dt><code>-umbrella</code></p>
<dd>
<dt><code>-undefined</code></p>
<dd>
<dt><code>-unexported_symbols_list</code></p>
<dd>
<dt><code>-weak_reference_mismatches</code></p>
<dd>
<dt><code>-whatsloaded</code></p>
<dd>These options are passed to the Darwin linker. The Darwin linker man page describes them in detail.</dl>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">DEC</font> Alpha implementations:</p>
<dl COMPACT>
<dt><code>-mno-soft-float</code></p>
<dd>
<dt><code>-msoft-float</code></p>
<dd>Use (do not use) the hardware floating-point instructions for floating-point operations. When <code>-msoft-float</code> is specified, functions in <i>libgcc.a</i> are used to perform floating-point operations. Unless they are replaced by routines that emulate the floating-point operations, or compiled in such a way as to call such emulations routines, these routines issue floating-point operations. If you are compiling for an Alpha without floating-point operations, you must ensure that the library is built so as not to call them. </p>
<p> Note that Alpha implementations without floating-point operations are required to have floating-point registers.</p>
<dt><code>-mfp-reg</code></p>
<dd>
<dt><code>-mno-fp-regs</code></p>
<dd>Generate code that uses (does not use) the floating-point register set. <code>-mno-fp-regs</code> implies <code>-msoft-float</code>. If the floating-point register set is not used, floating-point operands are passed in integer registers as if they were integers and floating-point results are passed in <tt>$0</tt> instead of <tt>$f0</tt>. This is a non-standard calling sequence, so any function with a floating-point argument or return value called by code compiled with <code>-mno-fp-regs</code> must also be compiled with that option. </p>
<p> A typical use of this option is building a kernel that does not use, and hence need not save and restore, any floating-point registers.</p>
<dt><code>-mieee</code></p>
<dd>The Alpha architecture implements floating-point hardware optimized for maximum performance. It is mostly compliant with the <font SIZE="-1">IEEE</font> floating-point standard. However, for full compliance, software assistance is required. This option generates code fully IEEE-compliant code <i>except</i> that the <i>inexact-flag</i> is not maintained (see below). If this option is turned on, the preprocessor macro <tt>&quot;_IEEE_FP&quot;</tt> is defined during compilation. The resulting code is less efficient but is able to correctly support denormalized numbers and exceptional <font SIZE="-1">IEEE</font> values such as not-a-number and plus/minus infinity. Other Alpha compilers call this option <code>-ieee_with_no_inexact</code>.</p>
<dt><code>-mieee-with-inexact</code></p>
<dd>This is like <code>-mieee</code> except the generated code also maintains the <font SIZE="-1">IEEE </font><i>inexact-flag</i>. Turning on this option causes the generated code to implement fully-compliant <font SIZE="-1">IEEE</font> math. In addition to <tt>&quot;_IEEE_FP&quot;</tt>, <tt>&quot;_IEEE_FP_EXACT&quot;</tt> is defined as a preprocessor macro. On some Alpha implementations the resulting code may execute significantly slower than the code generated by default. Since there is very little code that depends on the <i>inexact-flag</i>, you should normally not specify this option. Other Alpha compilers call this option <code>-ieee_with_inexact</code>.</p>
<dt><code>-mfp-trap-mode=</code><i>trap-mode</i></p>
<dd>This option controls what floating-point related traps are enabled. Other Alpha compilers call this option <code>-fptm</code> <i>trap-mode</i>. The trap mode can be set to one of four values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>n</code></p>
<dd>This is the default (normal) setting. The only traps that are enabled are the ones that cannot be disabled in software (e.g., division by zero trap).</p>
<dt><code>u</code></p>
<dd>In addition to the traps enabled by <code>n</code>, underflow traps are enabled as well.</p>
<dt><code>su</code></p>
<dd>Like <code>u</code>, but the instructions are marked to be safe for software completion (see Alpha architecture manual for details).</p>
<dt><code>sui</code></p>
<dd>Like <code>su</code>, but inexact traps are enabled as well.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mfp-rounding-mode=</code><i>rounding-mode</i></p>
<dd>Selects the <font SIZE="-1">IEEE</font> rounding mode. Other Alpha compilers call this option <code>-fprm</code> <i>rounding-mode</i>. The <i>rounding-mode</i> can be one of:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>n</code></p>
<dd>Normal <font SIZE="-1">IEEE</font> rounding mode. Floating-point numbers are rounded towards the nearest machine number or towards the even machine number in case of a tie.</p>
<dt><code>m</code></p>
<dd>Round towards minus infinity.</p>
<dt><code>c</code></p>
<dd>Chopped rounding mode. Floating-point numbers are rounded towards zero.</p>
<dt><code>d</code></p>
<dd>Dynamic rounding mode. A field in the floating-point control register (<i>fpcr</i>, see Alpha architecture reference manual) controls the rounding mode in effect. The C library initializes this register for rounding towards plus infinity. Thus, unless your program modifies the <i>fpcr</i>, <code>d</code> corresponds to round towards plus infinity.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mtrap-precision=</code><i>trap-precision</i></p>
<dd>In the Alpha architecture, floating-point traps are imprecise. This means without software assistance it is impossible to recover from a floating trap and program execution normally needs to be terminated. <font SIZE="-1">GCC</font> can generate code that can assist operating system trap handlers in determining the exact location that caused a floating-point trap. Depending on the requirements of an application, different levels of precisions can be selected:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>p</code></p>
<dd>Program precision. This option is the default and means a trap handler can only identify which program caused a floating-point exception.</p>
<dt><code>f</code></p>
<dd>Function precision. The trap handler can determine the function that caused a floating-point exception.</p>
<dt><code>i</code></p>
<dd>Instruction precision. The trap handler can determine the exact instruction that caused a floating-point exception.</dl>
</dl>
<dl COMPACT>
<dd>Other Alpha compilers provide the equivalent options called <code>-scope_safe</code> and <code>-resumption_safe</code>.</dl>
<dt><code>-mieee-conformant</code></p>
<dd>This option marks the generated code as <font SIZE="-1">IEEE</font> conformant. You must not use this option unless you also specify <code>-mtrap-precision=i</code> and either <code>-mfp-trap-mode=su</code> or <code>-mfp-trap-mode=sui</code>. Its only effect is to emit the line <code>.eflag 48</code> in the function prologue of the generated assembly file.</p>
<dt><code>-mbuild-constants</code></p>
<dd>Normally <font SIZE="-1">GCC</font> examines a 32- or 64-bit integer constant to see if it can construct it from smaller constants in two or three instructions. If it cannot, it outputs the constant as a literal and generates code to load it from the data segment at run time. </p>
<p> Use this option to require <font SIZE="-1">GCC</font> to construct <i>all</i> integer constants using code, even if it takes more instructions (the maximum is six). </p>
<p> You typically use this option to build a shared library dynamic loader. Itself a shared library, it must relocate itself in memory before it can find the variables and constants in its own data segment.</p>
<dt><code>-mbwx</code></p>
<dd>
<dt><code>-mno-bwx</code></p>
<dd>
<dt><code>-mcix</code></p>
<dd>
<dt><code>-mno-cix</code></p>
<dd>
<dt><code>-mfix</code></p>
<dd>
<dt><code>-mno-fix</code></p>
<dd>
<dt><code>-mmax</code></p>
<dd>
<dt><code>-mno-max</code></p>
<dd>Indicate whether <font SIZE="-1">GCC</font> should generate code to use the optional <font SIZE="-1">BWX, CIX, FIX</font> and <font SIZE="-1">MAX</font> instruction sets. The default is to use the instruction sets supported by the <font SIZE="-1">CPU</font> type specified via <code>-mcpu=</code> option or that of the <font SIZE="-1">CPU</font> on which <font SIZE="-1">GCC</font> was built if none is specified.</p>
<dt><code>-mfloat-vax</code></p>
<dd>
<dt><code>-mfloat-ieee</code></p>
<dd>Generate code that uses (does not use) <font SIZE="-1">VAX F</font> and G floating-point arithmetic instead of <font SIZE="-1">IEEE</font> single and double precision.</p>
<dt><code>-mexplicit-relocs</code></p>
<dd>
<dt><code>-mno-explicit-relocs</code></p>
<dd>Older Alpha assemblers provided no way to generate symbol relocations except via assembler macros. Use of these macros does not allow optimal instruction scheduling. <font SIZE="-1">GNU</font> binutils as of version 2.12 supports a new syntax that allows the compiler to explicitly mark which relocations should apply to which instructions. This option is mostly useful for debugging, as <font SIZE="-1">GCC</font> detects the capabilities of the assembler when it is built and sets the default accordingly.</p>
<dt><code>-msmall-data</code></p>
<dd>
<dt><code>-mlarge-data</code></p>
<dd>When <code>-mexplicit-relocs</code> is in effect, static data is accessed via <i>gp-relative</i> relocations. When <code>-msmall-data</code> is used, objects 8 bytes long or smaller are placed in a <i>small data area</i> (the <tt>&quot;.sdata&quot;</tt> and <tt>&quot;.sbss&quot;</tt> sections) and are accessed via 16-bit relocations off of the <tt>$gp</tt> register. This limits the size of the small data area to 64KB, but allows the variables to be directly accessed via a single instruction. </p>
<p> The default is <code>-mlarge-data</code>. With this option the data area is limited to just below 2GB. Programs that require more than 2GB of data must use <tt>&quot;malloc&quot;</tt> or <tt>&quot;mmap&quot;</tt> to allocate the data in the heap instead of in the program&#8217;s data segment. </p>
<p> When generating code for shared libraries, <code>-fpic</code> implies <code>-msmall-data</code> and <code>-fPIC</code> implies <code>-mlarge-data</code>.</p>
<dt><code>-msmall-text</code></p>
<dd>
<dt><code>-mlarge-text</code></p>
<dd>When <code>-msmall-text</code> is used, the compiler assumes that the code of the entire program (or shared library) fits in 4MB, and is thus reachable with a branch instruction. When <code>-msmall-data</code> is used, the compiler can assume that all local symbols share the same <tt>$gp</tt> value, and thus reduce the number of instructions required for a function call from 4 to 1. </p>
<p> The default is <code>-mlarge-text</code>.</p>
<dt><code>-mcpu=</code><i>cpu_type</i></p>
<dd>Set the instruction set and instruction scheduling parameters for machine type <i>cpu_type</i>. You can specify either the <font SIZE="-1"><code>EV</code></font> style name or the corresponding chip number. <font SIZE="-1">GCC</font> supports scheduling parameters for the <font SIZE="-1">EV4, EV5</font> and <font SIZE="-1">EV6</font> family of processors and chooses the default values for the instruction set from the processor you specify. If you do not specify a processor type, <font SIZE="-1">GCC</font> defaults to the processor on which the compiler was built. </p>
<p> Supported values for <i>cpu_type</i> are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>ev4</code></p>
<dd>
<dt><code>ev45</code></p>
<dd>
<dt><code>21064</code></p>
<dd>Schedules as an <font SIZE="-1">EV4</font> and has no instruction set extensions.</p>
<dt><code>ev5</code></p>
<dd>
<dt><code>21164</code></p>
<dd>Schedules as an <font SIZE="-1">EV5</font> and has no instruction set extensions.</p>
<dt><code>ev56</code></p>
<dd>
<dt><code>21164a</code></p>
<dd>Schedules as an <font SIZE="-1">EV5</font> and supports the <font SIZE="-1">BWX</font> extension.</p>
<dt><code>pca56</code></p>
<dd>
<dt><code>21164pc</code></p>
<dd>
<dt><code>21164PC</code></p>
<dd>Schedules as an <font SIZE="-1">EV5</font> and supports the <font SIZE="-1">BWX</font> and <font SIZE="-1">MAX</font> extensions.</p>
<dt><code>ev6</code></p>
<dd>
<dt><code>21264</code></p>
<dd>Schedules as an <font SIZE="-1">EV6</font> and supports the <font SIZE="-1">BWX, FIX,</font> and <font SIZE="-1">MAX</font> extensions.</p>
<dt><code>ev67</code></p>
<dd>
<dt><code>21264a</code></p>
<dd>Schedules as an <font SIZE="-1">EV6</font> and supports the <font SIZE="-1">BWX, CIX, FIX,</font> and <font SIZE="-1">MAX</font> extensions.</dl>
</dl>
<dl COMPACT>
<dd>Native toolchains also support the value <code>native</code>, which selects the best architecture option for the host processor. <code>-mcpu=native</code> has no effect if <font SIZE="-1">GCC</font> does not recognize the processor.</dl>
<dt><code>-mtune=</code><i>cpu_type</i></p>
<dd>Set only the instruction scheduling parameters for machine type <i>cpu_type</i>. The instruction set is not changed. </p>
<p> Native toolchains also support the value <code>native</code>, which selects the best architecture option for the host processor. <code>-mtune=native</code> has no effect if <font SIZE="-1">GCC</font> does not recognize the processor.</p>
<dt><code>-mmemory-latency=</code><i>time</i></p>
<dd>Sets the latency the scheduler should assume for typical memory references as seen by the application. This number is highly dependent on the memory access patterns used by the application and the size of the external cache on the machine. </p>
<p> Valid options for <i>time</i> are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>number</i></p>
<dd>A decimal number representing clock cycles.</p>
<dt><code>L1</code></p>
<dd>
<dt><code>L2</code></p>
<dd>
<dt><code>L3</code></p>
<dd>
<dt><code>main</code></p>
<dd>The compiler contains estimates of the number of clock cycles for &#8220;typical&#8221; <font SIZE="-1">EV4 &amp; EV5</font> hardware for the Level 1, 2 &amp; 3 caches (also called Dcache, Scache, and Bcache), as well as to main memory. Note that L3 is only valid for <font SIZE="-1">EV5.</font></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<p> <i></i><font SIZE="-1"><i>FR30</i></font><i> Options</i> </p>
<p> These options are defined specifically for the <font SIZE="-1">FR30</font> port.</p>
<dl COMPACT>
<dt><code>-msmall-model</code></p>
<dd>Use the small address space model. This can produce smaller code, but it does assume that all symbolic values and addresses fit into a 20-bit range.</p>
<dt><code>-mno-lsim</code></p>
<dd>Assume that runtime support has been provided and so there is no need to include the simulator library (<i>libsim.a</i>) on the linker command line.</dl>
<p> <i></i><font SIZE="-1"><i>FRV</i></font><i> Options</i></p>
<dl COMPACT>
<dt><code>-mgpr-32</code></p>
<dd>Only use the first 32 general-purpose registers.</p>
<dt><code>-mgpr-64</code></p>
<dd>Use all 64 general-purpose registers.</p>
<dt><code>-mfpr-32</code></p>
<dd>Use only the first 32 floating-point registers.</p>
<dt><code>-mfpr-64</code></p>
<dd>Use all 64 floating-point registers.</p>
<dt><code>-mhard-float</code></p>
<dd>Use hardware instructions for floating-point operations.</p>
<dt><code>-msoft-float</code></p>
<dd>Use library routines for floating-point operations.</p>
<dt><code>-malloc-cc</code></p>
<dd>Dynamically allocate condition code registers.</p>
<dt><code>-mfixed-cc</code></p>
<dd>Do not try to dynamically allocate condition code registers, only use <tt>&quot;icc0&quot;</tt> and <tt>&quot;fcc0&quot;</tt>.</p>
<dt><code>-mdword</code></p>
<dd>Change <font SIZE="-1">ABI</font> to use double word insns.</p>
<dt><code>-mno-dword</code></p>
<dd>Do not use double word instructions.</p>
<dt><code>-mdouble</code></p>
<dd>Use floating-point double instructions.</p>
<dt><code>-mno-double</code></p>
<dd>Do not use floating-point double instructions.</p>
<dt><code>-mmedia</code></p>
<dd>Use media instructions.</p>
<dt><code>-mno-media</code></p>
<dd>Do not use media instructions.</p>
<dt><code>-mmuladd</code></p>
<dd>Use multiply and add/subtract instructions.</p>
<dt><code>-mno-muladd</code></p>
<dd>Do not use multiply and add/subtract instructions.</p>
<dt><code>-mfdpic</code></p>
<dd>Select the <font SIZE="-1">FDPIC ABI,</font> which uses function descriptors to represent pointers to functions. Without any PIC/PIE-related options, it implies <code>-fPIE</code>. With <code>-fpic</code> or <code>-fpie</code>, it assumes <font SIZE="-1">GOT</font> entries and small data are within a 12-bit range from the <font SIZE="-1">GOT</font> base address; with <code>-fPIC</code> or <code>-fPIE</code>, <font SIZE="-1">GOT</font> offsets are computed with 32 bits. With a <code>bfin-elf</code> target, this option implies <code>-msim</code>.</p>
<dt><code>-minline-plt</code></p>
<dd>Enable inlining of <font SIZE="-1">PLT</font> entries in function calls to functions that are not known to bind locally. It has no effect without <code>-mfdpic</code>. It&#8217;s enabled by default if optimizing for speed and compiling for shared libraries (i.e., <code>-fPIC</code> or <code>-fpic</code>), or when an optimization option such as <code>-O3</code> or above is present in the command line.</p>
<dt><code>-mTLS</code></p>
<dd>Assume a large <font SIZE="-1">TLS</font> segment when generating thread-local code.</p>
<dt><code>-mtls</code></p>
<dd>Do not assume a large <font SIZE="-1">TLS</font> segment when generating thread-local code.</p>
<dt><code>-mgprel-ro</code></p>
<dd>Enable the use of <tt>&quot;GPREL&quot;</tt> relocations in the <font SIZE="-1">FDPIC ABI</font> for data that is known to be in read-only sections. It&#8217;s enabled by default, except for <code>-fpic</code> or <code>-fpie</code>: even though it may help make the global offset table smaller, it trades 1 instruction for 4. With <code>-fPIC</code> or <code>-fPIE</code>, it trades 3 instructions for 4, one of which may be shared by multiple symbols, and it avoids the need for a <font SIZE="-1">GOT</font> entry for the referenced symbol, so it&#8217;s more likely to be a win. If it is not, <code>-mno-gprel-ro</code> can be used to disable it.</p>
<dt><code>-multilib-library-pic</code></p>
<dd>Link with the (library, not <font SIZE="-1">FD</font>) pic libraries. It&#8217;s implied by <code>-mlibrary-pic</code>, as well as by <code>-fPIC</code> and <code>-fpic</code> without <code>-mfdpic</code>. You should never have to use it explicitly.</p>
<dt><code>-mlinked-fp</code></p>
<dd>Follow the <font SIZE="-1">EABI</font> requirement of always creating a frame pointer whenever a stack frame is allocated. This option is enabled by default and can be disabled with <code>-mno-linked-fp</code>.</p>
<dt><code>-mlong-calls</code></p>
<dd>Use indirect addressing to call functions outside the current compilation unit. This allows the functions to be placed anywhere within the 32-bit address space.</p>
<dt><code>-malign-labels</code></p>
<dd>Try to align labels to an 8-byte boundary by inserting NOPs into the previous packet. This option only has an effect when <font SIZE="-1">VLIW</font> packing is enabled. It doesn&#8217;t create new packets; it merely adds NOPs to existing ones.</p>
<dt><code>-mlibrary-pic</code></p>
<dd>Generate position-independent <font SIZE="-1">EABI</font> code.</p>
<dt><code>-macc-4</code></p>
<dd>Use only the first four media accumulator registers.</p>
<dt><code>-macc-8</code></p>
<dd>Use all eight media accumulator registers.</p>
<dt><code>-mpack</code></p>
<dd>Pack <font SIZE="-1">VLIW</font> instructions.</p>
<dt><code>-mno-pack</code></p>
<dd>Do not pack <font SIZE="-1">VLIW</font> instructions.</p>
<dt><code>-mno-eflags</code></p>
<dd>Do not mark <font SIZE="-1">ABI</font> switches in e_flags.</p>
<dt><code>-mcond-move</code></p>
<dd>Enable the use of conditional-move instructions (default). </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mno-cond-move</code></p>
<dd>Disable the use of conditional-move instructions. </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mscc</code></p>
<dd>Enable the use of conditional set instructions (default). </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mno-scc</code></p>
<dd>Disable the use of conditional set instructions. </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mcond-exec</code></p>
<dd>Enable the use of conditional execution (default). </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mno-cond-exec</code></p>
<dd>Disable the use of conditional execution. </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mvliw-branch</code></p>
<dd>Run a pass to pack branches into <font SIZE="-1">VLIW</font> instructions (default). </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mno-vliw-branch</code></p>
<dd>Do not run a pass to pack branches into <font SIZE="-1">VLIW</font> instructions. </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mmulti-cond-exec</code></p>
<dd>Enable optimization of <tt>&quot;&amp;&amp;&quot;</tt> and <tt>&quot;||&quot;</tt> in conditional execution (default). </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mno-multi-cond-exec</code></p>
<dd>Disable optimization of <tt>&quot;&amp;&amp;&quot;</tt> and <tt>&quot;||&quot;</tt> in conditional execution. </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mnested-cond-exec</code></p>
<dd>Enable nested conditional execution optimizations (default). </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-mno-nested-cond-exec</code></p>
<dd>Disable nested conditional execution optimizations. </p>
<p> This switch is mainly for debugging the compiler and will likely be removed in a future version.</p>
<dt><code>-moptimize-membar</code></p>
<dd>This switch removes redundant <tt>&quot;membar&quot;</tt> instructions from the compiler-generated code. It is enabled by default.</p>
<dt><code>-mno-optimize-membar</code></p>
<dd>This switch disables the automatic removal of redundant <tt>&quot;membar&quot;</tt> instructions from the generated code.</p>
<dt><code>-mtomcat-stats</code></p>
<dd>Cause gas to print out tomcat statistics.</p>
<dt><code>-mcpu=</code><i>cpu</i></p>
<dd>Select the processor type for which to generate code. Possible values are <code>frv</code>, <code>fr550</code>, <code>tomcat</code>, <code>fr500</code>, <code>fr450</code>, <code>fr405</code>, <code>fr400</code>, <code>fr300</code> and <code>simple</code>.</dl>
<p> <i>GNU/Linux Options</i> </p>
<p> These <code>-m</code> options are defined for GNU/Linux targets:</p>
<dl COMPACT>
<dt><code>-mglibc</code></p>
<dd>Use the <font SIZE="-1">GNU C</font> library. This is the default except on <code>*-*-linux-*uclibc*</code> and <code>*-*-linux-*android*</code> targets.</p>
<dt><code>-muclibc</code></p>
<dd>Use uClibc C library. This is the default on <code>*-*-linux-*uclibc*</code> targets.</p>
<dt><code>-mbionic</code></p>
<dd>Use Bionic C library. This is the default on <code>*-*-linux-*android*</code> targets.</p>
<dt><code>-mandroid</code></p>
<dd>Compile code compatible with Android platform. This is the default on <code>*-*-linux-*android*</code> targets. </p>
<p> When compiling, this option enables <code>-mbionic</code>, <code>-fPIC</code>, <code>-fno-exceptions</code> and <code>-fno-rtti</code> by default. When linking, this option makes the <font SIZE="-1">GCC</font> driver pass Android-specific options to the linker. Finally, this option causes the preprocessor macro <tt>&quot;__ANDROID__&quot;</tt> to be defined.</p>
<dt><code>-tno-android-cc</code></p>
<dd>Disable compilation effects of <code>-mandroid</code>, i.e., do not enable <code>-mbionic</code>, <code>-fPIC</code>, <code>-fno-exceptions</code> and <code>-fno-rtti</code> by default.</p>
<dt><code>-tno-android-ld</code></p>
<dd>Disable linking effects of <code>-mandroid</code>, i.e., pass standard Linux linking options to the linker.</dl>
<p> <i>H8/300 Options</i> </p>
<p> These <code>-m</code> options are defined for the H8/300 implementations:</p>
<dl COMPACT>
<dt><code>-mrelax</code></p>
<dd>Shorten some address references at link time, when possible; uses the linker option <code>-relax</code>.</p>
<dt><code>-mh</code></p>
<dd>Generate code for the H8/300H.</p>
<dt><code>-ms</code></p>
<dd>Generate code for the H8S.</p>
<dt><code>-mn</code></p>
<dd>Generate code for the H8S and H8/300H in the normal mode. This switch must be used either with <code>-mh</code> or <code>-ms</code>.</p>
<dt><code>-ms2600</code></p>
<dd>Generate code for the H8S/2600. This switch must be used with <code>-ms</code>.</p>
<dt><code>-mexr</code></p>
<dd>Extended registers are stored on stack before execution of function with monitor attribute. Default option is <code>-mexr</code>. This option is valid only for H8S targets.</p>
<dt><code>-mno-exr</code></p>
<dd>Extended registers are not stored on stack before execution of function with monitor attribute. Default option is <code>-mno-exr</code>. This option is valid only for H8S targets.</p>
<dt><code>-mint32</code></p>
<dd>Make <tt>&quot;int&quot;</tt> data 32 bits by default.</p>
<dt><code>-malign-300</code></p>
<dd>On the H8/300H and H8S, use the same alignment rules as for the H8/300. The default for the H8/300H and H8S is to align longs and floats on 4-byte boundaries. <code>-malign-300</code> causes them to be aligned on 2-byte boundaries. This option has no effect on the H8/300.</dl>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">HPPA</font> family of computers:</p>
<dl COMPACT>
<dt><code>-march=</code><i>architecture-type</i></p>
<dd>Generate code for the specified architecture. The choices for <i>architecture-type</i> are <code>1.0</code> for <font SIZE="-1">PA 1.0, </font><code>1.1</code> for <font SIZE="-1">PA 1.1,</font> and <code>2.0</code> for <font SIZE="-1">PA 2.0</font> processors. Refer to <i>/usr/lib/sched.models</i> on an HP-UX system to determine the proper architecture option for your machine. Code compiled for lower numbered architectures runs on higher numbered architectures, but not the other way around.</p>
<dt><code>-mpa-risc-1-0</code></p>
<dd>
<dt><code>-mpa-risc-1-1</code></p>
<dd>
<dt><code>-mpa-risc-2-0</code></p>
<dd>Synonyms for <code>-march=1.0</code>, <code>-march=1.1</code>, and <code>-march=2.0</code> respectively.</p>
<dt><code>-mjump-in-delay</code></p>
<dd>Fill delay slots of function calls with unconditional jump instructions by modifying the return pointer for the function call to be the target of the conditional jump.</p>
<dt><code>-mdisable-fpregs</code></p>
<dd>Prevent floating-point registers from being used in any manner. This is necessary for compiling kernels that perform lazy context switching of floating-point registers. If you use this option and attempt to perform floating-point operations, the compiler aborts.</p>
<dt><code>-mdisable-indexing</code></p>
<dd>Prevent the compiler from using indexing address modes. This avoids some rather obscure problems when compiling <font SIZE="-1">MIG</font> generated code under <font SIZE="-1">MACH.</font></p>
<dt><code>-mno-space-regs</code></p>
<dd>Generate code that assumes the target has no space registers. This allows <font SIZE="-1">GCC</font> to generate faster indirect calls and use unscaled index address modes. </p>
<p> Such code is suitable for level 0 <font SIZE="-1">PA</font> systems and kernels.</p>
<dt><code>-mfast-indirect-calls</code></p>
<dd>Generate code that assumes calls never cross space boundaries. This allows <font SIZE="-1">GCC</font> to emit code that performs faster indirect calls. </p>
<p> This option does not work in the presence of shared libraries or nested functions.</p>
<dt><code>-mfixed-range=</code><i>register-range</i></p>
<dd>Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator cannot use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma.</p>
<dt><code>-mlong-load-store</code></p>
<dd>Generate 3-instruction load and store sequences as sometimes required by the HP-UX 10 linker. This is equivalent to the <code>+k</code> option to the <font SIZE="-1">HP</font> compilers.</p>
<dt><code>-mportable-runtime</code></p>
<dd>Use the portable calling conventions proposed by <font SIZE="-1">HP</font> for <font SIZE="-1">ELF</font> systems.</p>
<dt><code>-mgas</code></p>
<dd>Enable the use of assembler directives only <font SIZE="-1">GAS</font> understands.</p>
<dt><code>-mschedule=</code><i>cpu-type</i></p>
<dd>Schedule code according to the constraints for the machine type <i>cpu-type</i>. The choices for <i>cpu-type</i> are <code>700</code> <code>7100</code>, <code>7100LC</code>, <code>7200</code>, <code>7300</code> and <code>8000</code>. Refer to <i>/usr/lib/sched.models</i> on an HP-UX system to determine the proper scheduling option for your machine. The default scheduling is <code>8000</code>.</p>
<dt><code>-mlinker-opt</code></p>
<dd>Enable the optimization pass in the HP-UX linker. Note this makes symbolic debugging impossible. It also triggers a bug in the HP-UX 8 and HP-UX 9 linkers in which they give bogus error messages when linking some programs.</p>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">HPPA</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC,</font> with <code>-msoft-float</code> in order for this to work.</p>
<dt><code>-msio</code></p>
<dd>Generate the predefine, <tt>&quot;_SIO&quot;</tt>, for server <font SIZE="-1">IO. </font> The default is <code>-mwsio</code>. This generates the predefines, <tt>&quot;__hp9000s700&quot;</tt>, <tt>&quot;__hp9000s700__&quot;</tt> and <tt>&quot;_WSIO&quot;</tt>, for workstation <font SIZE="-1">IO. </font> These options are available under HP-UX and HI-UX.</p>
<dt><code>-mgnu-ld</code></p>
<dd>Use options specific to <font SIZE="-1">GNU </font><code>ld</code>. This passes <code>-shared</code> to <code>ld</code> when building a shared library. It is the default when <font SIZE="-1">GCC</font> is configured, explicitly or implicitly, with the <font SIZE="-1">GNU</font> linker. This option does not affect which <code>ld</code> is called; it only changes what parameters are passed to that <code>ld</code>. The <code>ld</code> that is called is determined by the <code>&#8211;with-ld</code> configure option, <font SIZE="-1">GCC</font>&#8216;s program search path, and finally by the user&#8217;s <font SIZE="-1"><code>PATH</code></font>. The linker used by <font SIZE="-1">GCC</font> can be printed using <code>which `gcc -print-prog-name=ld`</code>. This option is only available on the 64-bit HP-UX <font SIZE="-1">GCC,</font> i.e. configured with <code>hppa*64*-*-hpux*</code>.</p>
<dt><code>-mhp-ld</code></p>
<dd>Use options specific to <font SIZE="-1">HP </font><code>ld</code>. This passes <code>-b</code> to <code>ld</code> when building a shared library and passes <code>+Accept TypeMismatch</code> to <code>ld</code> on all links. It is the default when <font SIZE="-1">GCC</font> is configured, explicitly or implicitly, with the <font SIZE="-1">HP</font> linker. This option does not affect which <code>ld</code> is called; it only changes what parameters are passed to that <code>ld</code>. The <code>ld</code> that is called is determined by the <code>&#8211;with-ld</code> configure option, <font SIZE="-1">GCC</font>&#8216;s program search path, and finally by the user&#8217;s <font SIZE="-1"><code>PATH</code></font>. The linker used by <font SIZE="-1">GCC</font> can be printed using <code>which `gcc -print-prog-name=ld`</code>. This option is only available on the 64-bit HP-UX <font SIZE="-1">GCC,</font> i.e. configured with <code>hppa*64*-*-hpux*</code>.</p>
<dt><code>-mlong-calls</code></p>
<dd>Generate code that uses long call sequences. This ensures that a call is always able to reach linker generated stubs. The default is to generate long calls only when the distance from the call site to the beginning of the function or translation unit, as the case may be, exceeds a predefined limit set by the branch type being used. The limits for normal calls are 7,600,000 and 240,000 bytes, respectively for the <font SIZE="-1">PA 2.0</font> and <font SIZE="-1">PA 1.X</font> architectures. Sibcalls are always limited at 240,000 bytes. </p>
<p> Distances are measured from the beginning of functions when using the <code>-ffunction-sections</code> option, or when using the <code>-mgas</code> and <code>-mno-portable-runtime</code> options together under HP-UX with the <font SIZE="-1">SOM</font> linker. </p>
<p> It is normally not desirable to use this option as it degrades performance. However, it may be useful in large applications, particularly when partial linking is used to build the application. </p>
<p> The types of long calls used depends on the capabilities of the assembler and linker, and the type of code being generated. The impact on systems that support long absolute calls, and long pic symbol-difference or pc-relative calls should be relatively small. However, an indirect call is used on 32-bit <font SIZE="-1">ELF</font> systems in pic code and it is quite long.</p>
<dt><code>-munix=</code><i>unix-std</i></p>
<dd>Generate compiler predefines and select a startfile for the specified <font SIZE="-1">UNIX</font> standard. The choices for <i>unix-std</i> are <code>93</code>, <code>95</code> and <code>98</code>. <code>93</code> is supported on all HP-UX versions. <code>95</code> is available on HP-UX 10.10 and later. <code>98</code> is available on HP-UX 11.11 and later. The default values are <code>93</code> for HP-UX 10.00, <code>95</code> for HP-UX 10.10 though to 11.00, and <code>98</code> for HP-UX 11.11 and later. </p>
<p> <code>-munix=93</code> provides the same predefines as <font SIZE="-1">GCC 3.3</font> and 3.4. <code>-munix=95</code> provides additional predefines for <tt>&quot;XOPEN_UNIX&quot;</tt> and <tt>&quot;_XOPEN_SOURCE_EXTENDED&quot;</tt>, and the startfile <i>unix95.o</i>. <code>-munix=98</code> provides additional predefines for <tt>&quot;_XOPEN_UNIX&quot;</tt>, <tt>&quot;_XOPEN_SOURCE_EXTENDED&quot;</tt>, <tt>&quot;_INCLUDE__STDC_A1_SOURCE&quot;</tt> and <tt>&quot;_INCLUDE_XOPEN_SOURCE_500&quot;</tt>, and the startfile <i>unix98.o</i>. </p>
<p> It is <i>important</i> to note that this option changes the interfaces for various library routines. It also affects the operational behavior of the C library. Thus, <i>extreme</i> care is needed in using this option. </p>
<p> Library code that is intended to operate with more than one <font SIZE="-1">UNIX</font> standard must test, set and restore the variable <i>__xpg4_extended_mask</i> as appropriate. Most <font SIZE="-1">GNU</font> software doesn&#8217;t provide this capability.</p>
<dt><code>-nolibdld</code></p>
<dd>Suppress the generation of link options to search libdld.sl when the <code>-static</code> option is specified on HP-UX 10 and later.</p>
<dt><code>-static</code></p>
<dd>The HP-UX implementation of setlocale in libc has a dependency on libdld.sl. There isn&#8217;t an archive version of libdld.sl. Thus, when the <code>-static</code> option is specified, special link options are needed to resolve this dependency. </p>
<p> On HP-UX 10 and later, the <font SIZE="-1">GCC</font> driver adds the necessary options to link with libdld.sl when the <code>-static</code> option is specified. This causes the resulting binary to be dynamic. On the 64-bit port, the linkers generate dynamic binaries by default in any case. The <code>-nolibdld</code> option can be used to prevent the <font SIZE="-1">GCC</font> driver from adding these link options.</p>
<dt><code>-threads</code></p>
<dd>Add support for multithreading with the <i>dce thread</i> library under HP-UX. This option sets flags for both the preprocessor and linker.</dl>
<p> <i>Intel 386 and </i><font SIZE="-1"><i>AMD</i></font><i> x86-64 Options</i> </p>
<p> These <code>-m</code> options are defined for the i386 and x86-64 family of computers:</p>
<dl COMPACT>
<dt><code>-march=</code><i>cpu-type</i></p>
<dd>Generate instructions for the machine type <i>cpu-type</i>. In contrast to <code>-mtune=</code><i>cpu-type</i>, which merely tunes the generated code for the specified <i>cpu-type</i>, <code>-march=</code><i>cpu-type</i> allows <font SIZE="-1">GCC</font> to generate code that may not run at all on processors other than the one indicated. Specifying <code>-march=</code><i>cpu-type</i> implies <code>-mtune=</code><i>cpu-type</i>. </p>
<p> The choices for <i>cpu-type</i> are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>native</code></p>
<dd>This selects the <font SIZE="-1">CPU</font> to generate code for at compilation time by determining the processor type of the compiling machine. Using <code>-march=native</code> enables all instruction subsets supported by the local machine (hence the result might not run on different machines). Using <code>-mtune=native</code> produces code optimized for the local machine under the constraints of the selected instruction set.</p>
<dt><code>i386</code></p>
<dd>Original Intel i386 <font SIZE="-1">CPU.</font></p>
<dt><code>i486</code></p>
<dd>Intel i486 <font SIZE="-1">CPU. </font>(No scheduling is implemented for this chip.)</p>
<dt><code>i586</code></p>
<dd>
<dt><code>pentium</code></p>
<dd>Intel Pentium <font SIZE="-1">CPU</font> with no <font SIZE="-1">MMX</font> support.</p>
<dt><code>pentium-mmx</code></p>
<dd>Intel Pentium <font SIZE="-1">MMX CPU,</font> based on Pentium core with <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><code>pentiumpro</code></p>
<dd>Intel Pentium Pro <font SIZE="-1">CPU.</font></p>
<dt><code>i686</code></p>
<dd>When used with <code>-march</code>, the Pentium Pro instruction set is used, so the code runs on all i686 family chips. When used with <code>-mtune</code>, it has the same meaning as <code>generic</code>.</p>
<dt><code>pentium2</code></p>
<dd>Intel Pentium <font SIZE="-1">II CPU,</font> based on Pentium Pro core with <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><code>pentium3</code></p>
<dd>
<dt><code>pentium3m</code></p>
<dd>Intel Pentium <font SIZE="-1">III CPU,</font> based on Pentium Pro core with <font SIZE="-1">MMX</font> and <font SIZE="-1">SSE</font> instruction set support.</p>
<dt><code>pentium-m</code></p>
<dd>Intel Pentium M; low-power version of Intel Pentium <font SIZE="-1">III CPU</font> with <font SIZE="-1">MMX, SSE</font> and <font SIZE="-1">SSE2</font> instruction set support. Used by Centrino notebooks.</p>
<dt><code>pentium4</code></p>
<dd>
<dt><code>pentium4m</code></p>
<dd>Intel Pentium 4 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX, SSE</font> and <font SIZE="-1">SSE2</font> instruction set support.</p>
<dt><code>prescott</code></p>
<dd>Improved version of Intel Pentium 4 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX, SSE, SSE2</font> and <font SIZE="-1">SSE3</font> instruction set support.</p>
<dt><code>nocona</code></p>
<dd>Improved version of Intel Pentium 4 <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX, SSE, SSE2</font> and <font SIZE="-1">SSE3</font> instruction set support.</p>
<dt><code>core2</code></p>
<dd>Intel Core 2 <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX, SSE, SSE2, SSE3</font> and <font SIZE="-1">SSSE3</font> instruction set support.</p>
<dt><code>nehalem</code></p>
<dd>Intel Nehalem <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2</font> and <font SIZE="-1">POPCNT</font> instruction set support.</p>
<dt><code>westmere</code></p>
<dd>Intel Westmere <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, AES</font> and <font SIZE="-1">PCLMUL</font> instruction set support.</p>
<dt><code>sandybridge</code></p>
<dd>Intel Sandy Bridge <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, AVX, AES</font> and <font SIZE="-1">PCLMUL</font> instruction set support.</p>
<dt><code>ivybridge</code></p>
<dd>Intel Ivy Bridge <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, AVX, AES, PCLMUL, FSGSBASE, RDRND</font> and F16C instruction set support.</p>
<dt><code>haswell</code></p>
<dd>Intel Haswell <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MOVBE, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, AVX, AVX2, AES, PCLMUL, FSGSBASE, RDRND, FMA, BMI, BMI2</font> and F16C instruction set support.</p>
<dt><code>broadwell</code></p>
<dd>Intel Broadwell <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MOVBE, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, AVX, AVX2, AES, PCLMUL, FSGSBASE, RDRND, FMA, BMI, BMI2, F16C, RDSEED, ADCX</font> and <font SIZE="-1">PREFETCHW</font> instruction set support.</p>
<dt><code>bonnell</code></p>
<dd>Intel Bonnell <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MOVBE, MMX, SSE, SSE2, SSE3</font> and <font SIZE="-1">SSSE3</font> instruction set support.</p>
<dt><code>silvermont</code></p>
<dd>Intel Silvermont <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MOVBE, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, AES, PCLMUL</font> and <font SIZE="-1">RDRND</font> instruction set support.</p>
<dt><code>k6</code></p>
<dd><font SIZE="-1">AMD K6 CPU</font> with <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><code>k6-2</code></p>
<dd>
<dt><code>k6-3</code></p>
<dd>Improved versions of <font SIZE="-1">AMD K6 CPU</font> with <font SIZE="-1">MMX</font> and 3DNow! instruction set support.</p>
<dt><code>athlon</code></p>
<dd>
<dt><code>athlon-tbird</code></p>
<dd><font SIZE="-1">AMD</font> Athlon <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX,</font> 3dNOW!, enhanced 3DNow! and <font SIZE="-1">SSE</font> prefetch instructions support.</p>
<dt><code>athlon-4</code></p>
<dd>
<dt><code>athlon-xp</code></p>
<dd>
<dt><code>athlon-mp</code></p>
<dd>Improved <font SIZE="-1">AMD</font> Athlon <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX,</font> 3DNow!, enhanced 3DNow! and full <font SIZE="-1">SSE</font> instruction set support.</p>
<dt><code>k8</code></p>
<dd>
<dt><code>opteron</code></p>
<dd>
<dt><code>athlon64</code></p>
<dd>
<dt><code>athlon-fx</code></p>
<dd>Processors based on the <font SIZE="-1">AMD K8</font> core with x86-64 instruction set support, including the <font SIZE="-1">AMD</font> Opteron, Athlon 64, and Athlon 64 <font SIZE="-1">FX</font> processors. (This supersets <font SIZE="-1">MMX, SSE, SSE2,</font> 3DNow!, enhanced 3DNow! and 64-bit instruction set extensions.)</p>
<dt><code>k8-sse3</code></p>
<dd>
<dt><code>opteron-sse3</code></p>
<dd>
<dt><code>athlon64-sse3</code></p>
<dd>Improved versions of <font SIZE="-1">AMD K8</font> cores with <font SIZE="-1">SSE3</font> instruction set support.</p>
<dt><code>amdfam10</code></p>
<dd>
<dt><code>barcelona</code></p>
<dd>CPUs based on <font SIZE="-1">AMD</font> Family 10h cores with x86-64 instruction set support. (This supersets <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSE4A,</font> 3DNow!, enhanced 3DNow!, <font SIZE="-1">ABM</font> and 64-bit instruction set extensions.)</p>
<dt><code>bdver1</code></p>
<dd>CPUs based on <font SIZE="-1">AMD</font> Family 15h cores with x86-64 instruction set support. (This supersets <font SIZE="-1">FMA4, AVX, XOP, LWP, AES, PCL_MUL, CX16, MMX, SSE, SSE2, SSE3, SSE4A, SSSE3, SSE4.1, SSE4.2, ABM</font> and 64-bit instruction set extensions.)</p>
<dt><code>bdver2</code></p>
<dd><font SIZE="-1">AMD</font> Family 15h core based CPUs with x86-64 instruction set support. (This supersets <font SIZE="-1">BMI, TBM, F16C, FMA, FMA4, AVX, XOP, LWP, AES, PCL_MUL, CX16, MMX, SSE, SSE2, SSE3, SSE4A, SSSE3, SSE4.1, SSE4.2, ABM</font> and 64-bit instruction set extensions.)</p>
<dt><code>bdver3</code></p>
<dd><font SIZE="-1">AMD</font> Family 15h core based CPUs with x86-64 instruction set support. (This supersets <font SIZE="-1">BMI, TBM, F16C, FMA, FMA4, FSGSBASE, AVX, XOP, LWP, AES, PCL_MUL, CX16, MMX, SSE, SSE2, SSE3, SSE4A, SSSE3, SSE4.1, SSE4.2, ABM</font> and 64-bit instruction set extensions.</p>
<dt><code>bdver4</code></p>
<dd><font SIZE="-1">AMD</font> Family 15h core based CPUs with x86-64 instruction set support. (This supersets <font SIZE="-1">BMI, BMI2, TBM, F16C, FMA, FMA4, FSGSBASE, AVX, AVX2, XOP, LWP, AES, PCL_MUL, CX16, MOVBE, MMX, SSE, SSE2, SSE3, SSE4A, SSSE3, SSE4.1, SSE4.2, ABM</font> and 64-bit instruction set extensions.</p>
<dt><code>btver1</code></p>
<dd>CPUs based on <font SIZE="-1">AMD</font> Family 14h cores with x86-64 instruction set support. (This supersets <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSSE3, SSE4A, CX16, ABM</font> and 64-bit instruction set extensions.)</p>
<dt><code>btver2</code></p>
<dd>CPUs based on <font SIZE="-1">AMD</font> Family 16h cores with x86-64 instruction set support. This includes <font SIZE="-1">MOVBE, F16C, BMI, AVX, PCL_MUL, AES, SSE4.2, SSE4.1, CX16, ABM, SSE4A, SSSE3, SSE3, SSE2, SSE, MMX</font> and 64-bit instruction set extensions.</p>
<dt><code>winchip-c6</code></p>
<dd><font SIZE="-1">IDT</font> WinChip C6 <font SIZE="-1">CPU,</font> dealt in same way as i486 with additional <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><code>winchip2</code></p>
<dd><font SIZE="-1">IDT</font> WinChip 2 <font SIZE="-1">CPU,</font> dealt in same way as i486 with additional <font SIZE="-1">MMX</font> and 3DNow! instruction set support.</p>
<dt><code>c3</code></p>
<dd><font SIZE="-1">VIA C3 CPU</font> with <font SIZE="-1">MMX</font> and 3DNow! instruction set support. (No scheduling is implemented for this chip.)</p>
<dt><code>c3-2</code></p>
<dd><font SIZE="-1">VIA C3-2 </font>(Nehemiah/C5XL) <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font> and <font SIZE="-1">SSE</font> instruction set support. (No scheduling is implemented for this chip.)</p>
<dt><code>geode</code></p>
<dd><font SIZE="-1">AMD</font> Geode embedded processor with <font SIZE="-1">MMX</font> and 3DNow! instruction set support.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Tune to <i>cpu-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. While picking a specific <i>cpu-type</i> schedules things appropriately for that particular chip, the compiler does not generate any code that cannot run on the default machine type unless you use a <code>-march=</code><i>cpu-type</i> option. For example, if <font SIZE="-1">GCC</font> is configured for i686-pc-linux-gnu then <code>-mtune=pentium4</code> generates code that is tuned for Pentium 4 but still runs on i686 machines. </p>
<p> The choices for <i>cpu-type</i> are the same as for <code>-march</code>. In addition, <code>-mtune</code> supports 2 extra choices for <i>cpu-type</i>:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>generic</code></p>
<dd>Produce code optimized for the most common <font SIZE="-1">IA32/AMD64/EM64T</font> processors. If you know the <font SIZE="-1">CPU</font> on which your code will run, then you should use the corresponding <code>-mtune</code> or <code>-march</code> option instead of <code>-mtune=generic</code>. But, if you do not know exactly what <font SIZE="-1">CPU</font> users of your application will have, then you should use this option. </p>
<p> As new processors are deployed in the marketplace, the behavior of this option will change. Therefore, if you upgrade to a newer version of <font SIZE="-1">GCC,</font> code generation controlled by this option will change to reflect the processors that are most common at the time that version of <font SIZE="-1">GCC</font> is released. </p>
<p> There is no <code>-march=generic</code> option because <code>-march</code> indicates the instruction set the compiler can use, and there is no generic instruction set applicable to all processors. In contrast, <code>-mtune</code> indicates the processor (or, in this case, collection of processors) for which the code is optimized.</p>
<dt><code>intel</code></p>
<dd>Produce code optimized for the most current Intel processors, which are Haswell and Silvermont for this version of <font SIZE="-1">GCC. </font> If you know the <font SIZE="-1">CPU</font> on which your code will run, then you should use the corresponding <code>-mtune</code> or <code>-march</code> option instead of <code>-mtune=intel</code>. But, if you want your application performs better on both Haswell and Silvermont, then you should use this option. </p>
<p> As new Intel processors are deployed in the marketplace, the behavior of this option will change. Therefore, if you upgrade to a newer version of <font SIZE="-1">GCC,</font> code generation controlled by this option will change to reflect the most current Intel processors at the time that version of <font SIZE="-1">GCC</font> is released. </p>
<p> There is no <code>-march=intel</code> option because <code>-march</code> indicates the instruction set the compiler can use, and there is no common instruction set applicable to all processors. In contrast, <code>-mtune</code> indicates the processor (or, in this case, collection of processors) for which the code is optimized.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mcpu=</code><i>cpu-type</i></p>
<dd>A deprecated synonym for <code>-mtune</code>.</p>
<dt><code>-mfpmath=</code><i>unit</i></p>
<dd>Generate floating-point arithmetic for selected unit <i>unit</i>. The choices for <i>unit</i> are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>387</code></p>
<dd>Use the standard 387 floating-point coprocessor present on the majority of chips and emulated otherwise. Code compiled with this option runs almost everywhere. The temporary results are computed in 80-bit precision instead of the precision specified by the type, resulting in slightly different results compared to most of other chips. See <code>-ffloat-store</code> for more detailed description. </p>
<p> This is the default choice for i386 compiler.</p>
<dt><code>sse</code></p>
<dd>Use scalar floating-point instructions present in the <font SIZE="-1">SSE</font> instruction set. This instruction set is supported by Pentium <font SIZE="-1">III</font> and newer chips, and in the <font SIZE="-1">AMD</font> line by Athlon-4, Athlon <font SIZE="-1">XP</font> and Athlon <font SIZE="-1">MP</font> chips. The earlier version of the <font SIZE="-1">SSE</font> instruction set supports only single-precision arithmetic, thus the double and extended-precision arithmetic are still done using 387. A later version, present only in Pentium 4 and <font SIZE="-1">AMD</font> x86-64 chips, supports double-precision arithmetic too. </p>
<p> For the i386 compiler, you must use <code>-march=</code><i>cpu-type</i>, <code>-msse</code> or <code>-msse2</code> switches to enable <font SIZE="-1">SSE</font> extensions and make this option effective. For the x86-64 compiler, these extensions are enabled by default. </p>
<p> The resulting code should be considerably faster in the majority of cases and avoid the numerical instability problems of 387 code, but may break some existing code that expects temporaries to be 80 bits. </p>
<p> This is the default choice for the x86-64 compiler.</p>
<dt><code>sse,387</code></p>
<dd>
<dt><code>sse+387</code></p>
<dd>
<dt><code>both</code></p>
<dd>Attempt to utilize both instruction sets at once. This effectively doubles the amount of available registers, and on chips with separate execution units for 387 and <font SIZE="-1">SSE</font> the execution resources too. Use this option with care, as it is still experimental, because the <font SIZE="-1">GCC</font> register allocator does not model separate functional units well, resulting in unstable performance.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-masm=</code><i>dialect</i></p>
<dd>Output assembly instructions using selected <i>dialect</i>. Supported choices are <code>intel</code> or <code>att</code> (the default). Darwin does not support <code>intel</code>.</p>
<dt><code>-mieee-fp</code></p>
<dd>
<dt><code>-mno-ieee-fp</code></p>
<dd>Control whether or not the compiler uses <font SIZE="-1">IEEE</font> floating-point comparisons. These correctly handle the case where the result of a comparison is unordered.</p>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. </p>
<p> <code>Warning:</code> the requisite libraries are not part of <font SIZE="-1">GCC.</font> Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. </p>
<p> On machines where a function returns floating-point results in the 80387 register stack, some floating-point opcodes may be emitted even if <code>-msoft-float</code> is used.</p>
<dt><code>-mno-fp-ret-in-387</code></p>
<dd>Do not use the <font SIZE="-1">FPU</font> registers for return values of functions. </p>
<p> The usual calling convention has functions return values of types <tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt> in an <font SIZE="-1">FPU</font> register, even if there is no <font SIZE="-1">FPU. </font> The idea is that the operating system should emulate an <font SIZE="-1">FPU.</font> </p>
<p> The option <code>-mno-fp-ret-in-387</code> causes such values to be returned in ordinary <font SIZE="-1">CPU</font> registers instead.</p>
<dt><code>-mno-fancy-math-387</code></p>
<dd>Some 387 emulators do not support the <tt>&quot;sin&quot;</tt>, <tt>&quot;cos&quot;</tt> and <tt>&quot;sqrt&quot;</tt> instructions for the 387. Specify this option to avoid generating those instructions. This option is the default on FreeBSD, OpenBSD and NetBSD. This option is overridden when <code>-march</code> indicates that the target <font SIZE="-1">CPU</font> always has an <font SIZE="-1">FPU</font> and so the instruction does not need emulation. These instructions are not generated unless you also use the <code>-funsafe-math-optimizations</code> switch.</p>
<dt><code>-malign-double</code></p>
<dd>
<dt><code>-mno-align-double</code></p>
<dd>Control whether <font SIZE="-1">GCC</font> aligns <tt>&quot;double&quot;</tt>, <tt>&quot;long double&quot;</tt>, and <tt>&quot;long long&quot;</tt> variables on a two-word boundary or a one-word boundary. Aligning <tt>&quot;double&quot;</tt> variables on a two-word boundary produces code that runs somewhat faster on a Pentium at the expense of more memory. </p>
<p> On x86-64, <code>-malign-double</code> is enabled by default. </p>
<p> <code>Warning:</code> if you use the <code>-malign-double</code> switch, structures containing the above types are aligned differently than the published application binary interface specifications for the 386 and are not binary compatible with structures in code compiled without that switch.</p>
<dt><code>-m96bit-long-double</code></p>
<dd>
<dt><code>-m128bit-long-double</code></p>
<dd>These switches control the size of <tt>&quot;long double&quot;</tt> type. The i386 application binary interface specifies the size to be 96 bits, so <code>-m96bit-long-double</code> is the default in 32-bit mode. </p>
<p> Modern architectures (Pentium and newer) prefer <tt>&quot;long double&quot;</tt> to be aligned to an 8- or 16-byte boundary. In arrays or structures conforming to the <font SIZE="-1">ABI,</font> this is not possible. So specifying <code>-m128bit-long-double</code> aligns <tt>&quot;long double&quot;</tt> to a 16-byte boundary by padding the <tt>&quot;long double&quot;</tt> with an additional 32-bit zero. </p>
<p> In the x86-64 compiler, <code>-m128bit-long-double</code> is the default choice as its <font SIZE="-1">ABI</font> specifies that <tt>&quot;long double&quot;</tt> is aligned on 16-byte boundary. </p>
<p> Notice that neither of these options enable any extra precision over the x87 standard of 80 bits for a <tt>&quot;long double&quot;</tt>. </p>
<p> <code>Warning:</code> if you override the default value for your target <font SIZE="-1">ABI,</font> this changes the size of structures and arrays containing <tt>&quot;long double&quot;</tt> variables, as well as modifying the function calling convention for functions taking <tt>&quot;long double&quot;</tt>. Hence they are not binary-compatible with code compiled without that switch.</p>
<dt><code>-mlong-double-64</code></p>
<dd>
<dt><code>-mlong-double-80</code></p>
<dd>
<dt><code>-mlong-double-128</code></p>
<dd>These switches control the size of <tt>&quot;long double&quot;</tt> type. A size of 64 bits makes the <tt>&quot;long double&quot;</tt> type equivalent to the <tt>&quot;double&quot;</tt> type. This is the default for 32-bit Bionic C library. A size of 128 bits makes the <tt>&quot;long double&quot;</tt> type equivalent to the <tt>&quot;__float128&quot;</tt> type. This is the default for 64-bit Bionic C library. </p>
<p> <code>Warning:</code> if you override the default value for your target <font SIZE="-1">ABI,</font> this changes the size of structures and arrays containing <tt>&quot;long double&quot;</tt> variables, as well as modifying the function calling convention for functions taking <tt>&quot;long double&quot;</tt>. Hence they are not binary-compatible with code compiled without that switch.</p>
<dt><code>-mlarge-data-threshold=</code><i>threshold</i></p>
<dd>When <code>-mcmodel=medium</code> is specified, data objects larger than <i>threshold</i> are placed in the large data section. This value must be the same across all objects linked into the binary, and defaults to 65535.</p>
<dt><code>-mrtd</code></p>
<dd>Use a different function-calling convention, in which functions that take a fixed number of arguments return with the <tt>&quot;ret </tt>num<tt>&quot;</tt> instruction, which pops their arguments while returning. This saves one instruction in the caller since there is no need to pop the arguments there. </p>
<p> You can specify that an individual function is called with this calling sequence with the function attribute <code>stdcall</code>. You can also override the <code>-mrtd</code> option by using the function attribute <code>cdecl</code>. </p>
<p> <code>Warning:</code> this calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <tt>&quot;printf&quot;</tt>); otherwise incorrect code is generated for calls to those functions. </p>
<p> In addition, seriously incorrect code results if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.)</p>
<dt><code>-mregparm=</code><i>num</i></p>
<dd>Control how many registers are used to pass integer arguments. By default, no registers are used to pass arguments, and at most 3 registers can be used. You can control this behavior for a specific function by using the function attribute <code>regparm</code>. </p>
<p> <code>Warning:</code> if you use this switch, and <i>num</i> is nonzero, then you must build all modules with the same value, including any libraries. This includes the system libraries and startup modules.</p>
<dt><code>-msseregparm</code></p>
<dd>Use <font SIZE="-1">SSE</font> register passing conventions for float and double arguments and return values. You can control this behavior for a specific function by using the function attribute <code>sseregparm</code>. </p>
<p> <code>Warning:</code> if you use this switch then you must build all modules with the same value, including any libraries. This includes the system libraries and startup modules.</p>
<dt><code>-mvect8-ret-in-mem</code></p>
<dd>Return 8-byte vectors in memory instead of <font SIZE="-1">MMX</font> registers. This is the default on Solaris@tie{}8 and 9 and VxWorks to match the <font SIZE="-1">ABI</font> of the Sun Studio compilers until version 12. Later compiler versions (starting with Studio 12 Update@tie{}1) follow the <font SIZE="-1">ABI</font> used by other x86 targets, which is the default on Solaris@tie{}10 and later. <i>Only</i> use this option if you need to remain compatible with existing code produced by those previous compiler versions or older versions of <font SIZE="-1">GCC.</font></p>
<dt><code>-mpc32</code></p>
<dd>
<dt><code>-mpc64</code></p>
<dd>
<dt><code>-mpc80</code></p>
<dd>Set 80387 floating-point precision to 32, 64 or 80 bits. When <code>-mpc32</code> is specified, the significands of results of floating-point operations are rounded to 24 bits (single precision); <code>-mpc64</code> rounds the significands of results of floating-point operations to 53 bits (double precision) and <code>-mpc80</code> rounds the significands of results of floating-point operations to 64 bits (extended double precision), which is the default. When this option is used, floating-point operations in higher precisions are not available to the programmer without setting the <font SIZE="-1">FPU</font> control word explicitly. </p>
<p> Setting the rounding of floating-point operations to less than the default 80 bits can speed some programs by 2% or more. Note that some mathematical libraries assume that extended-precision (80-bit) floating-point operations are enabled by default; routines in such libraries could suffer significant loss of accuracy, typically through so-called &#8220;catastrophic cancellation&#8221;, when this option is used to set the precision to less than extended precision.</p>
<dt><code>-mstackrealign</code></p>
<dd>Realign the stack at entry. On the Intel x86, the <code>-mstackrealign</code> option generates an alternate prologue and epilogue that realigns the run-time stack if necessary. This supports mixing legacy codes that keep 4-byte stack alignment with modern codes that keep 16-byte stack alignment for <font SIZE="-1">SSE</font> compatibility. See also the attribute <tt>&quot;force_align_arg_pointer&quot;</tt>, applicable to individual functions.</p>
<dt><code>-mpreferred-stack-boundary=</code><i>num</i></p>
<dd>Attempt to keep the stack boundary aligned to a 2 raised to <i>num</i> byte boundary. If <code>-mpreferred-stack-boundary</code> is not specified, the default is 4 (16 bytes or 128 bits). </p>
<p> <code>Warning:</code> When generating code for the x86-64 architecture with <font SIZE="-1">SSE</font> extensions disabled, <code>-mpreferred-stack-boundary=3</code> can be used to keep the stack boundary aligned to 8 byte boundary. Since x86-64 <font SIZE="-1">ABI</font> require 16 byte stack alignment, this is <font SIZE="-1">ABI</font> incompatible and intended to be used in controlled environment where stack space is important limitation. This option will lead to wrong code when functions compiled with 16 byte stack alignment (such as functions from a standard library) are called with misaligned stack. In this case, <font SIZE="-1">SSE</font> instructions may lead to misaligned memory access traps. In addition, variable arguments will be handled incorrectly for 16 byte aligned objects (including x87 long double and __int128), leading to wrong results. You must build all modules with <code>-mpreferred-stack-boundary=3</code>, including any libraries. This includes the system libraries and startup modules.</p>
<dt><code>-mincoming-stack-boundary=</code><i>num</i></p>
<dd>Assume the incoming stack is aligned to a 2 raised to <i>num</i> byte boundary. If <code>-mincoming-stack-boundary</code> is not specified, the one specified by <code>-mpreferred-stack-boundary</code> is used. </p>
<p> On Pentium and Pentium Pro, <tt>&quot;double&quot;</tt> and <tt>&quot;long double&quot;</tt> values should be aligned to an 8-byte boundary (see <code>-malign-double</code>) or suffer significant run time performance penalties. On Pentium <font SIZE="-1">III,</font> the Streaming <font SIZE="-1">SIMD</font> Extension (<font SIZE="-1">SSE</font>) data type <tt>&quot;__m128&quot;</tt> may not work properly if it is not 16-byte aligned. </p>
<p> To ensure proper alignment of this values on the stack, the stack boundary must be as aligned as that required by any value stored on the stack. Further, every function must be generated such that it keeps the stack aligned. Thus calling a function compiled with a higher preferred stack boundary from a function compiled with a lower preferred stack boundary most likely misaligns the stack. It is recommended that libraries that use callbacks always use the default setting. </p>
<p> This extra alignment does consume extra stack space, and generally increases code size. Code that is sensitive to stack space usage, such as embedded systems and operating system kernels, may want to reduce the preferred alignment to <code>-mpreferred-stack-boundary=2</code>.</p>
<dt><code>-mmmx</code></p>
<dd>
<dt><code>-mno-mmx</code></p>
<dd>
<dt><code>-msse</code></p>
<dd>
<dt><code>-mno-sse</code></p>
<dd>
<dt><code>-msse2</code></p>
<dd>
<dt><code>-mno-sse2</code></p>
<dd>
<dt><code>-msse3</code></p>
<dd>
<dt><code>-mno-sse3</code></p>
<dd>
<dt><code>-mssse3</code></p>
<dd>
<dt><code>-mno-ssse3</code></p>
<dd>
<dt><code>-msse4.1</code></p>
<dd>
<dt><code>-mno-sse4.1</code></p>
<dd>
<dt><code>-msse4.2</code></p>
<dd>
<dt><code>-mno-sse4.2</code></p>
<dd>
<dt><code>-msse4</code></p>
<dd>
<dt><code>-mno-sse4</code></p>
<dd>
<dt><code>-mavx</code></p>
<dd>
<dt><code>-mno-avx</code></p>
<dd>
<dt><code>-mavx2</code></p>
<dd>
<dt><code>-mno-avx2</code></p>
<dd>
<dt><code>-mavx512f</code></p>
<dd>
<dt><code>-mno-avx512f</code></p>
<dd>
<dt><code>-mavx512pf</code></p>
<dd>
<dt><code>-mno-avx512pf</code></p>
<dd>
<dt><code>-mavx512er</code></p>
<dd>
<dt><code>-mno-avx512er</code></p>
<dd>
<dt><code>-mavx512cd</code></p>
<dd>
<dt><code>-mno-avx512cd</code></p>
<dd>
<dt><code>-msha</code></p>
<dd>
<dt><code>-mno-sha</code></p>
<dd>
<dt><code>-maes</code></p>
<dd>
<dt><code>-mno-aes</code></p>
<dd>
<dt><code>-mpclmul</code></p>
<dd>
<dt><code>-mno-pclmul</code></p>
<dd>
<dt><code>-mfsgsbase</code></p>
<dd>
<dt><code>-mno-fsgsbase</code></p>
<dd>
<dt><code>-mrdrnd</code></p>
<dd>
<dt><code>-mno-rdrnd</code></p>
<dd>
<dt><code>-mf16c</code></p>
<dd>
<dt><code>-mno-f16c</code></p>
<dd>
<dt><code>-mfma</code></p>
<dd>
<dt><code>-mno-fma</code></p>
<dd>
<dt><code>-mprefetchwt1</code></p>
<dd>
<dt><code>-mno-prefetchwt1</code></p>
<dd>
<dt><code>-msse4a</code></p>
<dd>
<dt><code>-mno-sse4a</code></p>
<dd>
<dt><code>-mfma4</code></p>
<dd>
<dt><code>-mno-fma4</code></p>
<dd>
<dt><code>-mxop</code></p>
<dd>
<dt><code>-mno-xop</code></p>
<dd>
<dt><code>-mlwp</code></p>
<dd>
<dt><code>-mno-lwp</code></p>
<dd>
<dt><code>-m3dnow</code></p>
<dd>
<dt><code>-mno-3dnow</code></p>
<dd>
<dt><code>-mpopcnt</code></p>
<dd>
<dt><code>-mno-popcnt</code></p>
<dd>
<dt><code>-mabm</code></p>
<dd>
<dt><code>-mno-abm</code></p>
<dd>
<dt><code>-mbmi</code></p>
<dd>
<dt><code>-mbmi2</code></p>
<dd>
<dt><code>-mno-bmi</code></p>
<dd>
<dt><code>-mno-bmi2</code></p>
<dd>
<dt><code>-mlzcnt</code></p>
<dd>
<dt><code>-mno-lzcnt</code></p>
<dd>
<dt><code>-mfxsr</code></p>
<dd>
<dt><code>-mxsave</code></p>
<dd>
<dt><code>-mxsaveopt</code></p>
<dd>
<dt><code>-mrtm</code></p>
<dd>
<dt><code>-mtbm</code></p>
<dd>
<dt><code>-mno-tbm</code></p>
<dd>These switches enable or disable the use of instructions in the <font SIZE="-1">MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, AVX, AVX2, AVX512F, AVX512PF, AVX512ER, AVX512CD, SHA, AES, PCLMUL, FSGSBASE, RDRND, F16C, FMA, SSE4A, FMA4, XOP, LWP, ABM, BMI, BMI2, FXSR, XSAVE, XSAVEOPT, LZCNT, RTM,</font> or 3DNow! extended instruction sets. These extensions are also available as built-in functions: see <code>X86 Built-in Functions</code>, for details of the functions enabled and disabled by these switches. </p>
<p> To generate <font SIZE="-1">SSE/SSE2</font> instructions automatically from floating-point code (as opposed to 387 instructions), see <code>-mfpmath=sse</code>. </p>
<p> <font SIZE="-1">GCC</font> depresses SSEx instructions when <code>-mavx</code> is used. Instead, it generates new <font SIZE="-1">AVX</font> instructions or <font SIZE="-1">AVX</font> equivalence for all SSEx instructions when needed. </p>
<p> These options enable <font SIZE="-1">GCC</font> to use these extended instructions in generated code, even without <code>-mfpmath=sse</code>. Applications that perform run-time <font SIZE="-1">CPU</font> detection must compile separate files for each supported architecture, using the appropriate flags. In particular, the file containing the <font SIZE="-1">CPU</font> detection code should be compiled without these options.</p>
<dt><code>-mdump-tune-features</code></p>
<dd>This option instructs <font SIZE="-1">GCC</font> to dump the names of the x86 performance tuning features and default settings. The names can be used in <code>-mtune-ctrl=</code><i>feature-list</i>.</p>
<dt><code>-mtune-ctrl=</code><i>feature-list</i></p>
<dd>This option is used to do fine grain control of x86 code generation features. <i>feature-list</i> is a comma separated list of <i>feature</i> names. See also <code>-mdump-tune-features</code>. When specified, the <i>feature</i> will be turned on if it is not preceded with <tt>&quot;^&quot;</tt>, otherwise, it will be turned off. <code>-mtune-ctrl=</code><i>feature-list</i> is intended to be used by <font SIZE="-1">GCC</font> developers. Using it may lead to code paths not covered by testing and can potentially result in compiler ICEs or runtime errors.</p>
<dt><code>-mno-default</code></p>
<dd>This option instructs <font SIZE="-1">GCC</font> to turn off all tunable features. See also <code>-mtune-ctrl=</code><i>feature-list</i> and <code>-mdump-tune-features</code>.</p>
<dt><code>-mcld</code></p>
<dd>This option instructs <font SIZE="-1">GCC</font> to emit a <tt>&quot;cld&quot;</tt> instruction in the prologue of functions that use string instructions. String instructions depend on the <font SIZE="-1">DF</font> flag to select between autoincrement or autodecrement mode. While the <font SIZE="-1">ABI</font> specifies the <font SIZE="-1">DF</font> flag to be cleared on function entry, some operating systems violate this specification by not clearing the <font SIZE="-1">DF</font> flag in their exception dispatchers. The exception handler can be invoked with the <font SIZE="-1">DF</font> flag set, which leads to wrong direction mode when string instructions are used. This option can be enabled by default on 32-bit x86 targets by configuring <font SIZE="-1">GCC</font> with the <code>&#8211;enable-cld</code> configure option. Generation of <tt>&quot;cld&quot;</tt> instructions can be suppressed with the <code>-mno-cld</code> compiler option in this case.</p>
<dt><code>-mvzeroupper</code></p>
<dd>This option instructs <font SIZE="-1">GCC</font> to emit a <tt>&quot;vzeroupper&quot;</tt> instruction before a transfer of control flow out of the function to minimize the <font SIZE="-1">AVX</font> to <font SIZE="-1">SSE</font> transition penalty as well as remove unnecessary <tt>&quot;zeroupper&quot;</tt> intrinsics.</p>
<dt><code>-mprefer-avx128</code></p>
<dd>This option instructs <font SIZE="-1">GCC</font> to use 128-bit <font SIZE="-1">AVX</font> instructions instead of 256-bit <font SIZE="-1">AVX</font> instructions in the auto-vectorizer.</p>
<dt><code>-mcx16</code></p>
<dd>This option enables <font SIZE="-1">GCC</font> to generate <tt>&quot;CMPXCHG16B&quot;</tt> instructions. <tt>&quot;CMPXCHG16B&quot;</tt> allows for atomic operations on 128-bit double quadword (or oword) data types. This is useful for high-resolution counters that can be updated by multiple processors (or cores). This instruction is generated as part of atomic built-in functions: see <code>__sync Builtins</code> or <code>__atomic Builtins</code> for details.</p>
<dt><code>-msahf</code></p>
<dd>This option enables generation of <tt>&quot;SAHF&quot;</tt> instructions in 64-bit code. Early Intel Pentium 4 CPUs with Intel 64 support, prior to the introduction of Pentium 4 G1 step in December 2005, lacked the <tt>&quot;LAHF&quot;</tt> and <tt>&quot;SAHF&quot;</tt> instructions which were supported by <font SIZE="-1">AMD64.</font> These are load and store instructions, respectively, for certain status flags. In 64-bit mode, the <tt>&quot;SAHF&quot;</tt> instruction is used to optimize <tt>&quot;fmod&quot;</tt>, <tt>&quot;drem&quot;</tt>, and <tt>&quot;remainder&quot;</tt> built-in functions; see <code>Other Builtins</code> for details.</p>
<dt><code>-mmovbe</code></p>
<dd>This option enables use of the <tt>&quot;movbe&quot;</tt> instruction to implement <tt>&quot;__builtin_bswap32&quot;</tt> and <tt>&quot;__builtin_bswap64&quot;</tt>.</p>
<dt><code>-mcrc32</code></p>
<dd>This option enables built-in functions <tt>&quot;__builtin_ia32_crc32qi&quot;</tt>, <tt>&quot;__builtin_ia32_crc32hi&quot;</tt>, <tt>&quot;__builtin_ia32_crc32si&quot;</tt> and <tt>&quot;__builtin_ia32_crc32di&quot;</tt> to generate the <tt>&quot;crc32&quot;</tt> machine instruction.</p>
<dt><code>-mrecip</code></p>
<dd>This option enables use of <tt>&quot;RCPSS&quot;</tt> and <tt>&quot;RSQRTSS&quot;</tt> instructions (and their vectorized variants <tt>&quot;RCPPS&quot;</tt> and <tt>&quot;RSQRTPS&quot;</tt>) with an additional Newton-Raphson step to increase precision instead of <tt>&quot;DIVSS&quot;</tt> and <tt>&quot;SQRTSS&quot;</tt> (and their vectorized variants) for single-precision floating-point arguments. These instructions are generated only when <code>-funsafe-math-optimizations</code> is enabled together with <code>-finite-math-only</code> and <code>-fno-trapping-math</code>. Note that while the throughput of the sequence is higher than the throughput of the non-reciprocal instruction, the precision of the sequence can be decreased by up to 2 ulp (i.e. the inverse of 1.0 equals 0.99999994). </p>
<p> Note that <font SIZE="-1">GCC</font> implements <tt>&quot;1.0f/sqrtf(</tt>x<tt>)&quot;</tt> in terms of <tt>&quot;RSQRTSS&quot;</tt> (or <tt>&quot;RSQRTPS&quot;</tt>) already with <code>-ffast-math</code> (or the above option combination), and doesn&#8217;t need <code>-mrecip</code>. </p>
<p> Also note that <font SIZE="-1">GCC</font> emits the above sequence with additional Newton-Raphson step for vectorized single-float division and vectorized <tt>&quot;sqrtf(</tt>x<tt>)&quot;</tt> already with <code>-ffast-math</code> (or the above option combination), and doesn&#8217;t need <code>-mrecip</code>.</p>
<dt><code>-mrecip=</code><i>opt</i></p>
<dd>This option controls which reciprocal estimate instructions may be used. <i>opt</i> is a comma-separated list of options, which may be preceded by a <code>!</code> to invert the option:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>all</code></p>
<dd>Enable all estimate instructions.</p>
<dt><code>default</code></p>
<dd>Enable the default instructions, equivalent to <code>-mrecip</code>.</p>
<dt><code>none</code></p>
<dd>Disable all estimate instructions, equivalent to <code>-mno-recip</code>.</p>
<dt><code>div</code></p>
<dd>Enable the approximation for scalar division.</p>
<dt><code>vec-div</code></p>
<dd>Enable the approximation for vectorized division.</p>
<dt><code>sqrt</code></p>
<dd>Enable the approximation for scalar square root.</p>
<dt><code>vec-sqrt</code></p>
<dd>Enable the approximation for vectorized square root.</dl>
</dl>
<dl COMPACT>
<dd>So, for example, <code>-mrecip=all,!sqrt</code> enables all of the reciprocal approximations, except for square root.</dl>
<dt><code>-mveclibabi=</code><i>type</i></p>
<dd>Specifies the <font SIZE="-1">ABI</font> type to use for vectorizing intrinsics using an external library. Supported values for <i>type</i> are <code>svml</code> for the Intel short vector math library and <code>acml</code> for the <font SIZE="-1">AMD</font> math core library. To use this option, both <code>-ftree-vectorize</code> and <code>-funsafe-math-optimizations</code> have to be enabled, and an <font SIZE="-1">SVML</font> or <font SIZE="-1">ACML </font> ABI-compatible library must be specified at link time. </p>
<p> <font SIZE="-1">GCC</font> currently emits calls to <tt>&quot;vmldExp2&quot;</tt>, <tt>&quot;vmldLn2&quot;</tt>, <tt>&quot;vmldLog102&quot;</tt>, <tt>&quot;vmldLog102&quot;</tt>, <tt>&quot;vmldPow2&quot;</tt>, <tt>&quot;vmldTanh2&quot;</tt>, <tt>&quot;vmldTan2&quot;</tt>, <tt>&quot;vmldAtan2&quot;</tt>, <tt>&quot;vmldAtanh2&quot;</tt>, <tt>&quot;vmldCbrt2&quot;</tt>, <tt>&quot;vmldSinh2&quot;</tt>, <tt>&quot;vmldSin2&quot;</tt>, <tt>&quot;vmldAsinh2&quot;</tt>, <tt>&quot;vmldAsin2&quot;</tt>, <tt>&quot;vmldCosh2&quot;</tt>, <tt>&quot;vmldCos2&quot;</tt>, <tt>&quot;vmldAcosh2&quot;</tt>, <tt>&quot;vmldAcos2&quot;</tt>, <tt>&quot;vmlsExp4&quot;</tt>, <tt>&quot;vmlsLn4&quot;</tt>, <tt>&quot;vmlsLog104&quot;</tt>, <tt>&quot;vmlsLog104&quot;</tt>, <tt>&quot;vmlsPow4&quot;</tt>, <tt>&quot;vmlsTanh4&quot;</tt>, <tt>&quot;vmlsTan4&quot;</tt>, <tt>&quot;vmlsAtan4&quot;</tt>, <tt>&quot;vmlsAtanh4&quot;</tt>, <tt>&quot;vmlsCbrt4&quot;</tt>, <tt>&quot;vmlsSinh4&quot;</tt>, <tt>&quot;vmlsSin4&quot;</tt>, <tt>&quot;vmlsAsinh4&quot;</tt>, <tt>&quot;vmlsAsin4&quot;</tt>, <tt>&quot;vmlsCosh4&quot;</tt>, <tt>&quot;vmlsCos4&quot;</tt>, <tt>&quot;vmlsAcosh4&quot;</tt> and <tt>&quot;vmlsAcos4&quot;</tt> for corresponding function type when <code>-mveclibabi=svml</code> is used, and <tt>&quot;__vrd2_sin&quot;</tt>, <tt>&quot;__vrd2_cos&quot;</tt>, <tt>&quot;__vrd2_exp&quot;</tt>, <tt>&quot;__vrd2_log&quot;</tt>, <tt>&quot;__vrd2_log2&quot;</tt>, <tt>&quot;__vrd2_log10&quot;</tt>, <tt>&quot;__vrs4_sinf&quot;</tt>, <tt>&quot;__vrs4_cosf&quot;</tt>, <tt>&quot;__vrs4_expf&quot;</tt>, <tt>&quot;__vrs4_logf&quot;</tt>, <tt>&quot;__vrs4_log2f&quot;</tt>, <tt>&quot;__vrs4_log10f&quot;</tt> and <tt>&quot;__vrs4_powf&quot;</tt> for the corresponding function type when <code>-mveclibabi=acml</code> is used.</p>
<dt><code>-mabi=</code><i>name</i></p>
<dd>Generate code for the specified calling convention. Permissible values are <code>sysv</code> for the <font SIZE="-1">ABI</font> used on GNU/Linux and other systems, and <code>ms</code> for the Microsoft <font SIZE="-1">ABI. </font> The default is to use the Microsoft <font SIZE="-1">ABI</font> when targeting Microsoft Windows and the SysV <font SIZE="-1">ABI</font> on all other systems. You can control this behavior for a specific function by using the function attribute <code>ms_abi</code>/<code>sysv_abi</code>.</p>
<dt><code>-mtls-dialect=</code><i>type</i></p>
<dd>Generate code to access thread-local storage using the <code>gnu</code> or <code>gnu2</code> conventions. <code>gnu</code> is the conservative default; <code>gnu2</code> is more efficient, but it may add compile- and run-time requirements that cannot be satisfied on all systems.</p>
<dt><code>-mpush-args</code></p>
<dd>
<dt><code>-mno-push-args</code></p>
<dd>Use <font SIZE="-1">PUSH</font> operations to store outgoing parameters. This method is shorter and usually equally fast as method using <font SIZE="-1">SUB/MOV</font> operations and is enabled by default. In some cases disabling it may improve performance because of improved scheduling and reduced dependencies.</p>
<dt><code>-maccumulate-outgoing-args</code></p>
<dd>If enabled, the maximum amount of space required for outgoing arguments is computed in the function prologue. This is faster on most modern CPUs because of reduced dependencies, improved scheduling and reduced stack usage when the preferred stack boundary is not equal to 2. The drawback is a notable increase in code size. This switch implies <code>-mno-push-args</code>.</p>
<dt><code>-mthreads</code></p>
<dd>Support thread-safe exception handling on MinGW. Programs that rely on thread-safe exception handling must compile and link all code with the <code>-mthreads</code> option. When compiling, <code>-mthreads</code> defines <tt>&quot;-D_MT&quot;</tt>; when linking, it links in a special thread helper library <code>-lmingwthrd</code> which cleans up per-thread exception-handling data.</p>
<dt><code>-mno-align-stringops</code></p>
<dd>Do not align the destination of inlined string operations. This switch reduces code size and improves performance in case the destination is already aligned, but <font SIZE="-1">GCC</font> doesn&#8217;t know about it.</p>
<dt><code>-minline-all-stringops</code></p>
<dd>By default <font SIZE="-1">GCC</font> inlines string operations only when the destination is known to be aligned to least a 4-byte boundary. This enables more inlining and increases code size, but may improve performance of code that depends on fast <tt>&quot;memcpy&quot;</tt>, <tt>&quot;strlen&quot;</tt>, and <tt>&quot;memset&quot;</tt> for short lengths.</p>
<dt><code>-minline-stringops-dynamically</code></p>
<dd>For string operations of unknown size, use run-time checks with inline code for small blocks and a library call for large blocks.</p>
<dt><code>-mstringop-strategy=</code><i>alg</i></p>
<dd>Override the internal decision heuristic for the particular algorithm to use for inlining string operations. The allowed values for <i>alg</i> are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>rep_byte</code></p>
<dd>
<dt><code>rep_4byte</code></p>
<dd>
<dt><code>rep_8byte</code></p>
<dd>Expand using i386 <tt>&quot;rep&quot;</tt> prefix of the specified size.</p>
<dt><code>byte_loop</code></p>
<dd>
<dt><code>loop</code></p>
<dd>
<dt><code>unrolled_loop</code></p>
<dd>Expand into an inline loop.</p>
<dt><code>libcall</code></p>
<dd>Always use a library call.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mmemcpy-strategy=</code><i>strategy</i></p>
<dd>Override the internal decision heuristic to decide if <tt>&quot;__builtin_memcpy&quot;</tt> should be inlined and what inline algorithm to use when the expected size of the copy operation is known. <i>strategy</i> is a comma-separated list of <i>alg</i>:<i>max_size</i>:<i>dest_align</i> triplets. <i>alg</i> is specified in <code>-mstringop-strategy</code>, <i>max_size</i> specifies the max byte size with which inline algorithm <i>alg</i> is allowed. For the last triplet, the <i>max_size</i> must be <tt>&quot;-1&quot;</tt>. The <i>max_size</i> of the triplets in the list must be specified in increasing order. The minimal byte size for <i>alg</i> is <tt>0</tt> for the first triplet and <tt>&quot;</tt>max_size<tt> + 1&quot;</tt> of the preceding range.</p>
<dt><code>-mmemset-strategy=</code><i>strategy</i></p>
<dd>The option is similar to <code>-mmemcpy-strategy=</code> except that it is to control <tt>&quot;__builtin_memset&quot;</tt> expansion.</p>
<dt><code>-momit-leaf-frame-pointer</code></p>
<dd>Don&#8217;t keep the frame pointer in a register for leaf functions. This avoids the instructions to save, set up, and restore frame pointers and makes an extra register available in leaf functions. The option <code>-fomit-leaf-frame-pointer</code> removes the frame pointer for leaf functions, which might make debugging harder.</p>
<dt><code>-mtls-direct-seg-refs</code></p>
<dd>
<dt><code>-mno-tls-direct-seg-refs</code></p>
<dd>Controls whether <font SIZE="-1">TLS</font> variables may be accessed with offsets from the <font SIZE="-1">TLS</font> segment register (<tt>%gs</tt> for 32-bit, <tt>%fs</tt> for 64-bit), or whether the thread base pointer must be added. Whether or not this is valid depends on the operating system, and whether it maps the segment to cover the entire <font SIZE="-1">TLS</font> area. </p>
<p> For systems that use the <font SIZE="-1">GNU C</font> Library, the default is on.</p>
<dt><code>-msse2avx</code></p>
<dd>
<dt><code>-mno-sse2avx</code></p>
<dd>Specify that the assembler should encode <font SIZE="-1">SSE</font> instructions with <font SIZE="-1">VEX</font> prefix. The option <code>-mavx</code> turns this on by default.</p>
<dt><code>-mfentry</code></p>
<dd>
<dt><code>-mno-fentry</code></p>
<dd>If profiling is active (<code>-pg</code>), put the profiling counter call before the prologue. Note: On x86 architectures the attribute <tt>&quot;ms_hook_prologue&quot;</tt> isn&#8217;t possible at the moment for <code>-mfentry</code> and <code>-pg</code>.</p>
<dt><code>-m8bit-idiv</code></p>
<dd>
<dt><code>-mno-8bit-idiv</code></p>
<dd>On some processors, like Intel Atom, 8-bit unsigned integer divide is much faster than 32-bit/64-bit integer divide. This option generates a run-time check. If both dividend and divisor are within range of 0 to 255, 8-bit unsigned integer divide is used instead of 32-bit/64-bit integer divide.</p>
<dt><code>-mavx256-split-unaligned-load</code></p>
<dd>
<dt><code>-mavx256-split-unaligned-store</code></p>
<dd>Split 32-byte <font SIZE="-1">AVX</font> unaligned load and store.</p>
<dt><code>-mstack-protector-guard=</code><i>guard</i></p>
<dd>Generate stack protection code using canary at <i>guard</i>. Supported locations are <code>global</code> for global canary or <code>tls</code> for per-thread canary in the <font SIZE="-1">TLS</font> block (the default). This option has effect only when <code>-fstack-protector</code> or <code>-fstack-protector-all</code> is specified.</dl>
<p> These <code>-m</code> switches are supported in addition to the above on x86-64 processors in 64-bit environments.</p>
<dl COMPACT>
<dt><code>-m32</code></p>
<dd>
<dt><code>-m64</code></p>
<dd>
<dt><code>-mx32</code></p>
<dd>
<dt><code>-m16</code></p>
<dd>Generate code for a 16-bit, 32-bit or 64-bit environment. The <code>-m32</code> option sets <tt>&quot;int&quot;</tt>, <tt>&quot;long&quot;</tt>, and pointer types to 32 bits, and generates code that runs on any i386 system. </p>
<p> The <code>-m64</code> option sets <tt>&quot;int&quot;</tt> to 32 bits and <tt>&quot;long&quot;</tt> and pointer types to 64 bits, and generates code for the x86-64 architecture. For Darwin only the <code>-m64</code> option also turns off the <code>-fno-pic</code> and <code>-mdynamic-no-pic</code> options. </p>
<p> The <code>-mx32</code> option sets <tt>&quot;int&quot;</tt>, <tt>&quot;long&quot;</tt>, and pointer types to 32 bits, and generates code for the x86-64 architecture. </p>
<p> The <code>-m16</code> option is the same as <code>-m32</code>, except for that it outputs the <tt>&quot;.code16gcc&quot;</tt> assembly directive at the beginning of the assembly output so that the binary can run in 16-bit mode.</p>
<dt><code>-mno-red-zone</code></p>
<dd>Do not use a so-called &#8220;red zone&#8221; for x86-64 code. The red zone is mandated by the x86-64 <font SIZE="-1">ABI</font>; it is a 128-byte area beyond the location of the stack pointer that is not modified by signal or interrupt handlers and therefore can be used for temporary data without adjusting the stack pointer. The flag <code>-mno-red-zone</code> disables this red zone.</p>
<dt><code>-mcmodel=small</code></p>
<dd>Generate code for the small code model: the program and its symbols must be linked in the lower 2 <font SIZE="-1">GB</font> of the address space. Pointers are 64 bits. Programs can be statically or dynamically linked. This is the default code model.</p>
<dt><code>-mcmodel=kernel</code></p>
<dd>Generate code for the kernel code model. The kernel runs in the negative 2 <font SIZE="-1">GB</font> of the address space. This model has to be used for Linux kernel code.</p>
<dt><code>-mcmodel=medium</code></p>
<dd>Generate code for the medium model: the program is linked in the lower 2 <font SIZE="-1">GB</font> of the address space. Small symbols are also placed there. Symbols with sizes larger than <code>-mlarge-data-threshold</code> are put into large data or <font SIZE="-1">BSS</font> sections and can be located above 2GB. Programs can be statically or dynamically linked.</p>
<dt><code>-mcmodel=large</code></p>
<dd>Generate code for the large model. This model makes no assumptions about addresses and sizes of sections.</p>
<dt><code>-maddress-mode=long</code></p>
<dd>Generate code for long address mode. This is only supported for 64-bit and x32 environments. It is the default address mode for 64-bit environments.</p>
<dt><code>-maddress-mode=short</code></p>
<dd>Generate code for short address mode. This is only supported for 32-bit and x32 environments. It is the default address mode for 32-bit and x32 environments.</dl>
<p> <i>i386 and x86-64 Windows Options</i> </p>
<p> These additional options are available for Microsoft Windows targets:</p>
<dl COMPACT>
<dt><code>-mconsole</code></p>
<dd>This option specifies that a console application is to be generated, by instructing the linker to set the <font SIZE="-1">PE</font> header subsystem type required for console applications. This option is available for Cygwin and MinGW targets and is enabled by default on those targets.</p>
<dt><code>-mdll</code></p>
<dd>This option is available for Cygwin and MinGW targets. It specifies that a DLL&#8212;a dynamic link library&#8212;is to be generated, enabling the selection of the required runtime startup object and entry point.</p>
<dt><code>-mnop-fun-dllimport</code></p>
<dd>This option is available for Cygwin and MinGW targets. It specifies that the <tt>&quot;dllimport&quot;</tt> attribute should be ignored.</p>
<dt><code>-mthread</code></p>
<dd>This option is available for MinGW targets. It specifies that MinGW-specific thread support is to be used.</p>
<dt><code>-municode</code></p>
<dd>This option is available for MinGW-w64 targets. It causes the <tt>&quot;UNICODE&quot;</tt> preprocessor macro to be predefined, and chooses Unicode-capable runtime startup code.</p>
<dt><code>-mwin32</code></p>
<dd>This option is available for Cygwin and MinGW targets. It specifies that the typical Microsoft Windows predefined macros are to be set in the pre-processor, but does not influence the choice of runtime library/startup code.</p>
<dt><code>-mwindows</code></p>
<dd>This option is available for Cygwin and MinGW targets. It specifies that a <font SIZE="-1">GUI</font> application is to be generated by instructing the linker to set the <font SIZE="-1">PE</font> header subsystem type appropriately.</p>
<dt><code>-fno-set-stack-executable</code></p>
<dd>This option is available for MinGW targets. It specifies that the executable flag for the stack used by nested functions isn&#8217;t set. This is necessary for binaries running in kernel mode of Microsoft Windows, as there the User32 <font SIZE="-1">API,</font> which is used to set executable privileges, isn&#8217;t available.</p>
<dt><code>-fwritable-relocated-rdata</code></p>
<dd>This option is available for MinGW and Cygwin targets. It specifies that relocated-data in read-only section is put into .data section. This is a necessary for older runtimes not supporting modification of .rdata sections for pseudo-relocation.</p>
<dt><code>-mpe-aligned-commons</code></p>
<dd>This option is available for Cygwin and MinGW targets. It specifies that the <font SIZE="-1">GNU</font> extension to the <font SIZE="-1">PE</font> file format that permits the correct alignment of <font SIZE="-1">COMMON</font> variables should be used when generating code. It is enabled by default if <font SIZE="-1">GCC</font> detects that the target assembler found during configuration supports the feature.</dl>
<p> See also under <code>i386 and x86-64 Options</code> for standard options. </p>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i> </p>
<p> These are the <code>-m</code> options defined for the Intel <font SIZE="-1">IA-64</font> architecture.</p>
<dl COMPACT>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a big-endian target. This is the default for HP-UX.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a little-endian target. This is the default for <font SIZE="-1">AIX5</font> and GNU/Linux.</p>
<dt><code>-mgnu-as</code></p>
<dd>
<dt><code>-mno-gnu-as</code></p>
<dd>Generate (or don&#8217;t) code for the <font SIZE="-1">GNU</font> assembler. This is the default.</p>
<dt><code>-mgnu-ld</code></p>
<dd>
<dt><code>-mno-gnu-ld</code></p>
<dd>Generate (or don&#8217;t) code for the <font SIZE="-1">GNU</font> linker. This is the default.</p>
<dt><code>-mno-pic</code></p>
<dd>Generate code that does not use a global pointer register. The result is not position independent code, and violates the <font SIZE="-1">IA-64 ABI.</font></p>
<dt><code>-mvolatile-asm-stop</code></p>
<dd>
<dt><code>-mno-volatile-asm-stop</code></p>
<dd>Generate (or don&#8217;t) a stop bit immediately before and after volatile asm statements.</p>
<dt><code>-mregister-names</code></p>
<dd>
<dt><code>-mno-register-names</code></p>
<dd>Generate (or don&#8217;t) <code>in</code>, <code>loc</code>, and <code>out</code> register names for the stacked registers. This may make assembler output more readable.</p>
<dt><code>-mno-sdata</code></p>
<dd>
<dt><code>-msdata</code></p>
<dd>Disable (or enable) optimizations that use the small data section. This may be useful for working around optimizer bugs.</p>
<dt><code>-mconstant-gp</code></p>
<dd>Generate code that uses a single constant global pointer value. This is useful when compiling kernel code.</p>
<dt><code>-mauto-pic</code></p>
<dd>Generate code that is self-relocatable. This implies <code>-mconstant-gp</code>. This is useful when compiling firmware code.</p>
<dt><code>-minline-float-divide-min-latency</code></p>
<dd>Generate code for inline divides of floating-point values using the minimum latency algorithm.</p>
<dt><code>-minline-float-divide-max-throughput</code></p>
<dd>Generate code for inline divides of floating-point values using the maximum throughput algorithm.</p>
<dt><code>-mno-inline-float-divide</code></p>
<dd>Do not generate inline code for divides of floating-point values.</p>
<dt><code>-minline-int-divide-min-latency</code></p>
<dd>Generate code for inline divides of integer values using the minimum latency algorithm.</p>
<dt><code>-minline-int-divide-max-throughput</code></p>
<dd>Generate code for inline divides of integer values using the maximum throughput algorithm.</p>
<dt><code>-mno-inline-int-divide</code></p>
<dd>Do not generate inline code for divides of integer values.</p>
<dt><code>-minline-sqrt-min-latency</code></p>
<dd>Generate code for inline square roots using the minimum latency algorithm.</p>
<dt><code>-minline-sqrt-max-throughput</code></p>
<dd>Generate code for inline square roots using the maximum throughput algorithm.</p>
<dt><code>-mno-inline-sqrt</code></p>
<dd>Do not generate inline code for <tt>&quot;sqrt&quot;</tt>.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Do (don&#8217;t) generate code that uses the fused multiply/add or multiply/subtract instructions. The default is to use these instructions.</p>
<dt><code>-mno-dwarf2-asm</code></p>
<dd>
<dt><code>-mdwarf2-asm</code></p>
<dd>Don&#8217;t (or do) generate assembler code for the <font SIZE="-1">DWARF 2</font> line number debugging info. This may be useful when not using the <font SIZE="-1">GNU</font> assembler.</p>
<dt><code>-mearly-stop-bits</code></p>
<dd>
<dt><code>-mno-early-stop-bits</code></p>
<dd>Allow stop bits to be placed earlier than immediately preceding the instruction that triggered the stop bit. This can improve instruction scheduling, but does not always do so.</p>
<dt><code>-mfixed-range=</code><i>register-range</i></p>
<dd>Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator cannot use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma.</p>
<dt><code>-mtls-size=</code><i>tls-size</i></p>
<dd>Specify bit size of immediate <font SIZE="-1">TLS</font> offsets. Valid values are 14, 22, and 64.</p>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Tune the instruction scheduling for a particular <font SIZE="-1">CPU,</font> Valid values are <code>itanium</code>, <code>itanium1</code>, <code>merced</code>, <code>itanium2</code>, and <code>mckinley</code>.</p>
<dt><code>-milp32</code></p>
<dd>
<dt><code>-mlp64</code></p>
<dd>Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits. These are HP-UX specific flags.</p>
<dt><code>-mno-sched-br-data-spec</code></p>
<dd>
<dt><code>-msched-br-data-spec</code></p>
<dd>(Dis/En)able data speculative scheduling before reload. This results in generation of <tt>&quot;ld.a&quot;</tt> instructions and the corresponding check instructions (<tt>&quot;ld.c&quot;</tt> / <tt>&quot;chk.a&quot;</tt>). The default is &#8216;disable&#8217;.</p>
<dt><code>-msched-ar-data-spec</code></p>
<dd>
<dt><code>-mno-sched-ar-data-spec</code></p>
<dd>(En/Dis)able data speculative scheduling after reload. This results in generation of <tt>&quot;ld.a&quot;</tt> instructions and the corresponding check instructions (<tt>&quot;ld.c&quot;</tt> / <tt>&quot;chk.a&quot;</tt>). The default is &#8216;enable&#8217;.</p>
<dt><code>-mno-sched-control-spec</code></p>
<dd>
<dt><code>-msched-control-spec</code></p>
<dd>(Dis/En)able control speculative scheduling. This feature is available only during region scheduling (i.e. before reload). This results in generation of the <tt>&quot;ld.s&quot;</tt> instructions and the corresponding check instructions <tt>&quot;chk.s&quot;</tt>. The default is &#8216;disable&#8217;.</p>
<dt><code>-msched-br-in-data-spec</code></p>
<dd>
<dt><code>-mno-sched-br-in-data-spec</code></p>
<dd>(En/Dis)able speculative scheduling of the instructions that are dependent on the data speculative loads before reload. This is effective only with <code>-msched-br-data-spec</code> enabled. The default is &#8216;enable&#8217;.</p>
<dt><code>-msched-ar-in-data-spec</code></p>
<dd>
<dt><code>-mno-sched-ar-in-data-spec</code></p>
<dd>(En/Dis)able speculative scheduling of the instructions that are dependent on the data speculative loads after reload. This is effective only with <code>-msched-ar-data-spec</code> enabled. The default is &#8216;enable&#8217;.</p>
<dt><code>-msched-in-control-spec</code></p>
<dd>
<dt><code>-mno-sched-in-control-spec</code></p>
<dd>(En/Dis)able speculative scheduling of the instructions that are dependent on the control speculative loads. This is effective only with <code>-msched-control-spec</code> enabled. The default is &#8216;enable&#8217;.</p>
<dt><code>-mno-sched-prefer-non-data-spec-insns</code></p>
<dd>
<dt><code>-msched-prefer-non-data-spec-insns</code></p>
<dd>If enabled, data-speculative instructions are chosen for schedule only if there are no other choices at the moment. This makes the use of the data speculation much more conservative. The default is &#8216;disable&#8217;.</p>
<dt><code>-mno-sched-prefer-non-control-spec-insns</code></p>
<dd>
<dt><code>-msched-prefer-non-control-spec-insns</code></p>
<dd>If enabled, control-speculative instructions are chosen for schedule only if there are no other choices at the moment. This makes the use of the control speculation much more conservative. The default is &#8216;disable&#8217;.</p>
<dt><code>-mno-sched-count-spec-in-critical-path</code></p>
<dd>
<dt><code>-msched-count-spec-in-critical-path</code></p>
<dd>If enabled, speculative dependencies are considered during computation of the instructions priorities. This makes the use of the speculation a bit more conservative. The default is &#8216;disable&#8217;.</p>
<dt><code>-msched-spec-ldc</code></p>
<dd>Use a simple data speculation check. This option is on by default.</p>
<dt><code>-msched-control-spec-ldc</code></p>
<dd>Use a simple check for control speculation. This option is on by default.</p>
<dt><code>-msched-stop-bits-after-every-cycle</code></p>
<dd>Place a stop bit after every cycle when scheduling. This option is on by default.</p>
<dt><code>-msched-fp-mem-deps-zero-cost</code></p>
<dd>Assume that floating-point stores and loads are not likely to cause a conflict when placed into the same instruction group. This option is disabled by default.</p>
<dt><code>-msel-sched-dont-check-control-spec</code></p>
<dd>Generate checks for control speculation in selective scheduling. This flag is disabled by default.</p>
<dt><code>-msched-max-memory-insns=</code><i>max-insns</i></p>
<dd>Limit on the number of memory insns per instruction group, giving lower priority to subsequent memory insns attempting to schedule in the same instruction group. Frequently useful to prevent cache bank conflicts. The default value is 1.</p>
<dt><code>-msched-max-memory-insns-hard-limit</code></p>
<dd>Makes the limit specified by <code>msched-max-memory-insns</code> a hard limit, disallowing more than that number in an instruction group. Otherwise, the limit is &#8220;soft&#8221;, meaning that non-memory operations are preferred when the limit is reached, but memory operations may still be scheduled.</dl>
<p> <i></i><font SIZE="-1"><i>LM32</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the LatticeMico32 architecture:</p>
<dl COMPACT>
<dt><code>-mbarrel-shift-enabled</code></p>
<dd>Enable barrel-shift instructions.</p>
<dt><code>-mdivide-enabled</code></p>
<dd>Enable divide and modulus instructions.</p>
<dt><code>-mmultiply-enabled</code></p>
<dd>Enable multiply instructions.</p>
<dt><code>-msign-extend-enabled</code></p>
<dd>Enable sign extend instructions.</p>
<dt><code>-muser-enabled</code></p>
<dd>Enable user-defined instructions.</dl>
<p> <i>M32C Options</i></p>
<dl COMPACT>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>Select the <font SIZE="-1">CPU</font> for which code is generated. <i>name</i> may be one of <code>r8c</code> for the R8C/Tiny series, <code>m16c</code> for the M16C (up to /60) series, <code>m32cm</code> for the M16C/80 series, or <code>m32c</code> for the M32C/80 series.</p>
<dt><code>-msim</code></p>
<dd>Specifies that the program will be run on the simulator. This causes an alternate runtime library to be linked in which supports, for example, file I/O. You must not use this option when generating programs that will run on real hardware; you must provide your own runtime library for whatever I/O functions are needed.</p>
<dt><code>-memregs=</code><i>number</i></p>
<dd>Specifies the number of memory-based pseudo-registers <font SIZE="-1">GCC</font> uses during code generation. These pseudo-registers are used like real registers, so there is a tradeoff between <font SIZE="-1">GCC</font>&#8216;s ability to fit the code into available registers, and the performance penalty of using memory instead of registers. Note that all modules in a program must be compiled with the same value for this option. Because of that, you must not use this option with <font SIZE="-1">GCC</font>&#8216;s default runtime libraries.</dl>
<p> <i>M32R/D Options</i> </p>
<p> These <code>-m</code> options are defined for Renesas M32R/D architectures:</p>
<dl COMPACT>
<dt><code>-m32r2</code></p>
<dd>Generate code for the M32R/2.</p>
<dt><code>-m32rx</code></p>
<dd>Generate code for the M32R/X.</p>
<dt><code>-m32r</code></p>
<dd>Generate code for the M32R. This is the default.</p>
<dt><code>-mmodel=small</code></p>
<dd>Assume all objects live in the lower 16MB of memory (so that their addresses can be loaded with the <tt>&quot;ld24&quot;</tt> instruction), and assume all subroutines are reachable with the <tt>&quot;bl&quot;</tt> instruction. This is the default. </p>
<p> The addressability of a particular object can be set with the <tt>&quot;model&quot;</tt> attribute.</p>
<dt><code>-mmodel=medium</code></p>
<dd>Assume objects may be anywhere in the 32-bit address space (the compiler generates <tt>&quot;seth/add3&quot;</tt> instructions to load their addresses), and assume all subroutines are reachable with the <tt>&quot;bl&quot;</tt> instruction.</p>
<dt><code>-mmodel=large</code></p>
<dd>Assume objects may be anywhere in the 32-bit address space (the compiler generates <tt>&quot;seth/add3&quot;</tt> instructions to load their addresses), and assume subroutines may not be reachable with the <tt>&quot;bl&quot;</tt> instruction (the compiler generates the much slower <tt>&quot;seth/add3/jl&quot;</tt> instruction sequence).</p>
<dt><code>-msdata=none</code></p>
<dd>Disable use of the small data area. Variables are put into one of <code>.data</code>, <code>.bss</code>, or <code>.rodata</code> (unless the <tt>&quot;section&quot;</tt> attribute has been specified). This is the default. </p>
<p> The small data area consists of sections <code>.sdata</code> and <code>.sbss</code>. Objects may be explicitly put in the small data area with the <tt>&quot;section&quot;</tt> attribute using one of these sections.</p>
<dt><code>-msdata=sdata</code></p>
<dd>Put small global and static data in the small data area, but do not generate special code to reference them.</p>
<dt><code>-msdata=use</code></p>
<dd>Put small global and static data in the small data area, and generate special instructions to reference them.</p>
<dt><code>-G</code> <i>num</i></p>
<dd>Put global and static objects less than or equal to <i>num</i> bytes into the small data or <font SIZE="-1">BSS</font> sections instead of the normal data or <font SIZE="-1">BSS</font> sections. The default value of <i>num</i> is 8. The <code>-msdata</code> option must be set to one of <code>sdata</code> or <code>use</code> for this option to have any effect. </p>
<p> All modules should be compiled with the same <code>-G</code> <i>num</i> value. Compiling with different values of <i>num</i> may or may not work; if it doesn&#8217;t the linker gives an error message&#8212;incorrect code is not generated.</p>
<dt><code>-mdebug</code></p>
<dd>Makes the M32R-specific code in the compiler display some statistics that might help in debugging programs.</p>
<dt><code>-malign-loops</code></p>
<dd>Align all loops to a 32-byte boundary.</p>
<dt><code>-mno-align-loops</code></p>
<dd>Do not enforce a 32-byte alignment for loops. This is the default.</p>
<dt><code>-missue-rate=</code><i>number</i></p>
<dd>Issue <i>number</i> instructions per cycle. <i>number</i> can only be 1 or 2.</p>
<dt><code>-mbranch-cost=</code><i>number</i></p>
<dd><i>number</i> can only be 1 or 2. If it is 1 then branches are preferred over conditional code, if it is 2, then the opposite applies.</p>
<dt><code>-mflush-trap=</code><i>number</i></p>
<dd>Specifies the trap number to use to flush the cache. The default is 12. Valid numbers are between 0 and 15 inclusive.</p>
<dt><code>-mno-flush-trap</code></p>
<dd>Specifies that the cache cannot be flushed by using a trap.</p>
<dt><code>-mflush-func=</code><i>name</i></p>
<dd>Specifies the name of the operating system function to call to flush the cache. The default is <i>_flush_cache</i>, but a function call is only used if a trap is not available.</p>
<dt><code>-mno-flush-func</code></p>
<dd>Indicates that there is no <font SIZE="-1">OS</font> function for flushing the cache.</dl>
<p> <i>M680x0 Options</i> </p>
<p> These are the <code>-m</code> options defined for M680x0 and ColdFire processors. The default settings depend on which architecture was selected when the compiler was configured; the defaults for the most common choices are given below.</p>
<dl COMPACT>
<dt><code>-march=</code><i>arch</i></p>
<dd>Generate code for a specific M680x0 or ColdFire instruction set architecture. Permissible values of <i>arch</i> for M680x0 architectures are: <code>68000</code>, <code>68010</code>, <code>68020</code>, <code>68030</code>, <code>68040</code>, <code>68060</code> and <code>cpu32</code>. ColdFire architectures are selected according to Freescale&#8217;s <font SIZE="-1">ISA</font> classification and the permissible values are: <code>isaa</code>, <code>isaaplus</code>, <code>isab</code> and <code>isac</code>. </p>
<p> <font SIZE="-1">GCC</font> defines a macro <code>__mcf</code><i>arch</i><code>__</code> whenever it is generating code for a ColdFire target. The <i>arch</i> in this macro is one of the <code>-march</code> arguments given above. </p>
<p> When used together, <code>-march</code> and <code>-mtune</code> select code that runs on a family of similar processors but that is optimized for a particular microarchitecture.</p>
<dt><code>-mcpu=</code><i>cpu</i></p>
<dd>Generate code for a specific M680x0 or ColdFire processor. The M680x0 <i>cpu</i>s are: <code>68000</code>, <code>68010</code>, <code>68020</code>, <code>68030</code>, <code>68040</code>, <code>68060</code>, <code>68302</code>, <code>68332</code> and <code>cpu32</code>. The ColdFire <i>cpu</i>s are given by the table below, which also classifies the CPUs into families:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Family : <code>-mcpu</code> arguments</p>
<dd>
<dt><code>51</code> : <code>51</code> <code>51ac</code> <code>51ag</code> <code>51cn</code> <code>51em</code> <code>51je</code> <code>51jf</code> <code>51jg</code> <code>51jm</code> <code>51mm</code> <code>51qe</code> <code>51qm</code></p>
<dd>
<dt><code>5206</code> : <code>5202</code> <code>5204</code> <code>5206</code></p>
<dd>
<dt><code>5206e</code> : <code>5206e</code></p>
<dd>
<dt><code>5208</code> : <code>5207</code> <code>5208</code></p>
<dd>
<dt><code>5211a</code> : <code>5210a</code> <code>5211a</code></p>
<dd>
<dt><code>5213</code> : <code>5211</code> <code>5212</code> <code>5213</code></p>
<dd>
<dt><code>5216</code> : <code>5214</code> <code>5216</code></p>
<dd>
<dt><code>52235</code> : <code>52230</code> <code>52231</code> <code>52232</code> <code>52233</code> <code>52234</code> <code>52235</code></p>
<dd>
<dt><code>5225</code> : <code>5224</code> <code>5225</code></p>
<dd>
<dt><code>52259</code> : <code>52252</code> <code>52254</code> <code>52255</code> <code>52256</code> <code>52258</code> <code>52259</code></p>
<dd>
<dt><code>5235</code> : <code>5232</code> <code>5233</code> <code>5234</code> <code>5235</code> <code>523x</code></p>
<dd>
<dt><code>5249</code> : <code>5249</code></p>
<dd>
<dt><code>5250</code> : <code>5250</code></p>
<dd>
<dt><code>5271</code> : <code>5270</code> <code>5271</code></p>
<dd>
<dt><code>5272</code> : <code>5272</code></p>
<dd>
<dt><code>5275</code> : <code>5274</code> <code>5275</code></p>
<dd>
<dt><code>5282</code> : <code>5280</code> <code>5281</code> <code>5282</code> <code>528x</code></p>
<dd>
<dt><code>53017</code> : <code>53011</code> <code>53012</code> <code>53013</code> <code>53014</code> <code>53015</code> <code>53016</code> <code>53017</code></p>
<dd>
<dt><code>5307</code> : <code>5307</code></p>
<dd>
<dt><code>5329</code> : <code>5327</code> <code>5328</code> <code>5329</code> <code>532x</code></p>
<dd>
<dt><code>5373</code> : <code>5372</code> <code>5373</code> <code>537x</code></p>
<dd>
<dt><code>5407</code> : <code>5407</code></p>
<dd>
<dt><code>5475</code> : <code>5470</code> <code>5471</code> <code>5472</code> <code>5473</code> <code>5474</code> <code>5475</code> <code>547x</code> <code>5480</code> <code>5481</code> <code>5482</code> <code>5483</code> <code>5484</code> <code>5485</code></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd><code>-mcpu=</code><i>cpu</i> overrides <code>-march=</code><i>arch</i> if <i>arch</i> is compatible with <i>cpu</i>. Other combinations of <code>-mcpu</code> and <code>-march</code> are rejected. </p>
<p> <font SIZE="-1">GCC</font> defines the macro <code>__mcf_cpu_</code><i>cpu</i> when ColdFire target <i>cpu</i> is selected. It also defines <code>__mcf_family_</code><i>family</i>, where the value of <i>family</i> is given by the table above.</dl>
<dt><code>-mtune=</code><i>tune</i></p>
<dd>Tune the code for a particular microarchitecture within the constraints set by <code>-march</code> and <code>-mcpu</code>. The M680x0 microarchitectures are: <code>68000</code>, <code>68010</code>, <code>68020</code>, <code>68030</code>, <code>68040</code>, <code>68060</code> and <code>cpu32</code>. The ColdFire microarchitectures are: <code>cfv1</code>, <code>cfv2</code>, <code>cfv3</code>, <code>cfv4</code> and <code>cfv4e</code>. </p>
<p> You can also use <code>-mtune=68020-40</code> for code that needs to run relatively well on 68020, 68030 and 68040 targets. <code>-mtune=68020-60</code> is similar but includes 68060 targets as well. These two options select the same tuning decisions as <code>-m68020-40</code> and <code>-m68020-60</code> respectively. </p>
<p> <font SIZE="-1">GCC</font> defines the macros <code>__mc</code><i>arch</i> and <code>__mc</code><i>arch</i><code>__</code> when tuning for 680&#215;0 architecture <i>arch</i>. It also defines <code>mc</code><i>arch</i> unless either <code>-ansi</code> or a non-GNU <code>-std</code> option is used. If <font SIZE="-1">GCC</font> is tuning for a range of architectures, as selected by <code>-mtune=68020-40</code> or <code>-mtune=68020-60</code>, it defines the macros for every architecture in the range. </p>
<p> <font SIZE="-1">GCC</font> also defines the macro <code>__m</code><i>uarch</i><code>__</code> when tuning for ColdFire microarchitecture <i>uarch</i>, where <i>uarch</i> is one of the arguments given above.</p>
<dt><code>-m68000</code></p>
<dd>
<dt><code>-mc68000</code></p>
<dd>Generate output for a 68000. This is the default when the compiler is configured for 68000-based systems. It is equivalent to <code>-march=68000</code>. </p>
<p> Use this option for microcontrollers with a 68000 or <font SIZE="-1">EC000</font> core, including the 68008, 68302, 68306, 68307, 68322, 68328 and 68356.</p>
<dt><code>-m68010</code></p>
<dd>Generate output for a 68010. This is the default when the compiler is configured for 68010-based systems. It is equivalent to <code>-march=68010</code>.</p>
<dt><code>-m68020</code></p>
<dd>
<dt><code>-mc68020</code></p>
<dd>Generate output for a 68020. This is the default when the compiler is configured for 68020-based systems. It is equivalent to <code>-march=68020</code>.</p>
<dt><code>-m68030</code></p>
<dd>Generate output for a 68030. This is the default when the compiler is configured for 68030-based systems. It is equivalent to <code>-march=68030</code>.</p>
<dt><code>-m68040</code></p>
<dd>Generate output for a 68040. This is the default when the compiler is configured for 68040-based systems. It is equivalent to <code>-march=68040</code>. </p>
<p> This option inhibits the use of 68881/68882 instructions that have to be emulated by software on the 68040. Use this option if your 68040 does not have code to emulate those instructions.</p>
<dt><code>-m68060</code></p>
<dd>Generate output for a 68060. This is the default when the compiler is configured for 68060-based systems. It is equivalent to <code>-march=68060</code>. </p>
<p> This option inhibits the use of 68020 and 68881/68882 instructions that have to be emulated by software on the 68060. Use this option if your 68060 does not have code to emulate those instructions.</p>
<dt><code>-mcpu32</code></p>
<dd>Generate output for a <font SIZE="-1">CPU32. </font> This is the default when the compiler is configured for CPU32-based systems. It is equivalent to <code>-march=cpu32</code>. </p>
<p> Use this option for microcontrollers with a <font SIZE="-1">CPU32</font> or <font SIZE="-1">CPU32+</font> core, including the 68330, 68331, 68332, 68333, 68334, 68336, 68340, 68341, 68349 and 68360.</p>
<dt><code>-m5200</code></p>
<dd>Generate output for a 520X ColdFire <font SIZE="-1">CPU. </font> This is the default when the compiler is configured for 520X-based systems. It is equivalent to <code>-mcpu=5206</code>, and is now deprecated in favor of that option. </p>
<p> Use this option for microcontroller with a 5200 core, including the <font SIZE="-1">MCF5202, MCF5203, MCF5204</font> and <font SIZE="-1">MCF5206.</font></p>
<dt><code>-m5206e</code></p>
<dd>Generate output for a 5206e ColdFire <font SIZE="-1">CPU. </font> The option is now deprecated in favor of the equivalent <code>-mcpu=5206e</code>.</p>
<dt><code>-m528x</code></p>
<dd>Generate output for a member of the ColdFire 528X family. The option is now deprecated in favor of the equivalent <code>-mcpu=528x</code>.</p>
<dt><code>-m5307</code></p>
<dd>Generate output for a ColdFire 5307 <font SIZE="-1">CPU. </font> The option is now deprecated in favor of the equivalent <code>-mcpu=5307</code>.</p>
<dt><code>-m5407</code></p>
<dd>Generate output for a ColdFire 5407 <font SIZE="-1">CPU. </font> The option is now deprecated in favor of the equivalent <code>-mcpu=5407</code>.</p>
<dt><code>-mcfv4e</code></p>
<dd>Generate output for a ColdFire V4e family <font SIZE="-1">CPU </font>(e.g. 547x/548x). This includes use of hardware floating-point instructions. The option is equivalent to <code>-mcpu=547x</code>, and is now deprecated in favor of that option.</p>
<dt><code>-m68020-40</code></p>
<dd>Generate output for a 68040, without using any of the new instructions. This results in code that can run relatively efficiently on either a 68020/68881 or a 68030 or a 68040. The generated code does use the 68881 instructions that are emulated on the 68040. </p>
<p> The option is equivalent to <code>-march=68020</code> <code>-mtune=68020-40</code>.</p>
<dt><code>-m68020-60</code></p>
<dd>Generate output for a 68060, without using any of the new instructions. This results in code that can run relatively efficiently on either a 68020/68881 or a 68030 or a 68040. The generated code does use the 68881 instructions that are emulated on the 68060. </p>
<p> The option is equivalent to <code>-march=68020</code> <code>-mtune=68020-60</code>.</p>
<dt><code>-mhard-float</code></p>
<dd>
<dt><code>-m68881</code></p>
<dd>Generate floating-point instructions. This is the default for 68020 and above, and for ColdFire devices that have an <font SIZE="-1">FPU. </font> It defines the macro <code>__HAVE_68881__</code> on M680x0 targets and <code>__mcffpu__</code> on ColdFire targets.</p>
<dt><code>-msoft-float</code></p>
<dd>Do not generate floating-point instructions; use library calls instead. This is the default for 68000, 68010, and 68832 targets. It is also the default for ColdFire devices that have no <font SIZE="-1">FPU.</font></p>
<dt><code>-mdiv</code></p>
<dd>
<dt><code>-mno-div</code></p>
<dd>Generate (do not generate) ColdFire hardware divide and remainder instructions. If <code>-march</code> is used without <code>-mcpu</code>, the default is &#8220;on&#8221; for ColdFire architectures and &#8220;off&#8221; for M680x0 architectures. Otherwise, the default is taken from the target <font SIZE="-1">CPU </font>(either the default <font SIZE="-1">CPU,</font> or the one specified by <code>-mcpu</code>). For example, the default is &#8220;off&#8221; for <code>-mcpu=5206</code> and &#8220;on&#8221; for <code>-mcpu=5206e</code>. </p>
<p> <font SIZE="-1">GCC</font> defines the macro <code>__mcfhwdiv__</code> when this option is enabled.</p>
<dt><code>-mshort</code></p>
<dd>Consider type <tt>&quot;int&quot;</tt> to be 16 bits wide, like <tt>&quot;short int&quot;</tt>. Additionally, parameters passed on the stack are also aligned to a 16-bit boundary even on targets whose <font SIZE="-1">API</font> mandates promotion to 32-bit.</p>
<dt><code>-mno-short</code></p>
<dd>Do not consider type <tt>&quot;int&quot;</tt> to be 16 bits wide. This is the default.</p>
<dt><code>-mnobitfield</code></p>
<dd>
<dt><code>-mno-bitfield</code></p>
<dd>Do not use the bit-field instructions. The <code>-m68000</code>, <code>-mcpu32</code> and <code>-m5200</code> options imply <code>-mnobitfield</code>.</p>
<dt><code>-mbitfield</code></p>
<dd>Do use the bit-field instructions. The <code>-m68020</code> option implies <code>-mbitfield</code>. This is the default if you use a configuration designed for a 68020.</p>
<dt><code>-mrtd</code></p>
<dd>Use a different function-calling convention, in which functions that take a fixed number of arguments return with the <tt>&quot;rtd&quot;</tt> instruction, which pops their arguments while returning. This saves one instruction in the caller since there is no need to pop the arguments there. </p>
<p> This calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <tt>&quot;printf&quot;</tt>); otherwise incorrect code is generated for calls to those functions. </p>
<p> In addition, seriously incorrect code results if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.) </p>
<p> The <tt>&quot;rtd&quot;</tt> instruction is supported by the 68010, 68020, 68030, 68040, 68060 and <font SIZE="-1">CPU32</font> processors, but not by the 68000 or 5200.</p>
<dt><code>-mno-rtd</code></p>
<dd>Do not use the calling conventions selected by <code>-mrtd</code>. This is the default.</p>
<dt><code>-malign-int</code></p>
<dd>
<dt><code>-mno-align-int</code></p>
<dd>Control whether <font SIZE="-1">GCC</font> aligns <tt>&quot;int&quot;</tt>, <tt>&quot;long&quot;</tt>, <tt>&quot;long long&quot;</tt>, <tt>&quot;float&quot;</tt>, <tt>&quot;double&quot;</tt>, and <tt>&quot;long double&quot;</tt> variables on a 32-bit boundary (<code>-malign-int</code>) or a 16-bit boundary (<code>-mno-align-int</code>). Aligning variables on 32-bit boundaries produces code that runs somewhat faster on processors with 32-bit busses at the expense of more memory. </p>
<p> <code>Warning:</code> if you use the <code>-malign-int</code> switch, <font SIZE="-1">GCC</font> aligns structures containing the above types differently than most published application binary interface specifications for the m68k.</p>
<dt><code>-mpcrel</code></p>
<dd>Use the pc-relative addressing mode of the 68000 directly, instead of using a global offset table. At present, this option implies <code>-fpic</code>, allowing at most a 16-bit offset for pc-relative addressing. <code>-fPIC</code> is not presently supported with <code>-mpcrel</code>, though this could be supported for 68020 and higher processors.</p>
<dt><code>-mno-strict-align</code></p>
<dd>
<dt><code>-mstrict-align</code></p>
<dd>Do not (do) assume that unaligned memory references are handled by the system.</p>
<dt><code>-msep-data</code></p>
<dd>Generate code that allows the data segment to be located in a different area of memory from the text segment. This allows for execute-in-place in an environment without virtual memory management. This option implies <code>-fPIC</code>.</p>
<dt><code>-mno-sep-data</code></p>
<dd>Generate code that assumes that the data segment follows the text segment. This is the default.</p>
<dt><code>-mid-shared-library</code></p>
<dd>Generate code that supports shared libraries via the library <font SIZE="-1">ID</font> method. This allows for execute-in-place and shared libraries in an environment without virtual memory management. This option implies <code>-fPIC</code>.</p>
<dt><code>-mno-id-shared-library</code></p>
<dd>Generate code that doesn&#8217;t assume ID-based shared libraries are being used. This is the default.</p>
<dt><code>-mshared-library-id=n</code></p>
<dd>Specifies the identification number of the ID-based shared library being compiled. Specifying a value of 0 generates more compact code; specifying other values forces the allocation of that number to the current library, but is no more space- or time-efficient than omitting this option.</p>
<dt><code>-mxgot</code></p>
<dd>
<dt><code>-mno-xgot</code></p>
<dd>When generating position-independent code for ColdFire, generate code that works if the <font SIZE="-1">GOT</font> has more than 8192 entries. This code is larger and slower than code generated without this option. On M680x0 processors, this option is not needed; <code>-fPIC</code> suffices. </p>
<p> <font SIZE="-1">GCC</font> normally uses a single instruction to load values from the <font SIZE="-1">GOT.</font> While this is relatively efficient, it only works if the <font SIZE="-1">GOT</font> is smaller than about 64k. Anything larger causes the linker to report an error such as: </p>
<pre> relocation truncated to fit: R_68K_GOT16O foobar</pre>
<p>If this happens, you should recompile your code with <code>-mxgot</code>. It should then work with very large GOTs. However, code generated with <code>-mxgot</code> is less efficient, since it takes 4 instructions to fetch the value of a global symbol. </p>
<p> Note that some linkers, including newer versions of the <font SIZE="-1">GNU</font> linker, can create multiple GOTs and sort <font SIZE="-1">GOT</font> entries. If you have such a linker, you should only need to use <code>-mxgot</code> when compiling a single object file that accesses more than 8192 <font SIZE="-1">GOT</font> entries. Very few do. </p>
<p> These options have no effect unless <font SIZE="-1">GCC</font> is generating position-independent code.</dl>
<p> <i>MCore Options</i> </p>
<p> These are the <code>-m</code> options defined for the Motorola M*Core processors.</p>
<dl COMPACT>
<dt><code>-mhardlit</code></p>
<dd>
<dt><code>-mno-hardlit</code></p>
<dd>Inline constants into the code stream if it can be done in two instructions or less.</p>
<dt><code>-mdiv</code></p>
<dd>
<dt><code>-mno-div</code></p>
<dd>Use the divide instruction. (Enabled by default).</p>
<dt><code>-mrelax-immediate</code></p>
<dd>
<dt><code>-mno-relax-immediate</code></p>
<dd>Allow arbitrary-sized immediates in bit operations.</p>
<dt><code>-mwide-bitfields</code></p>
<dd>
<dt><code>-mno-wide-bitfields</code></p>
<dd>Always treat bit-fields as <tt>&quot;int&quot;</tt>-sized.</p>
<dt><code>-m4byte-functions</code></p>
<dd>
<dt><code>-mno-4byte-functions</code></p>
<dd>Force all functions to be aligned to a 4-byte boundary.</p>
<dt><code>-mcallgraph-data</code></p>
<dd>
<dt><code>-mno-callgraph-data</code></p>
<dd>Emit callgraph information.</p>
<dt><code>-mslow-bytes</code></p>
<dd>
<dt><code>-mno-slow-bytes</code></p>
<dd>Prefer word access when reading byte quantities.</p>
<dt><code>-mlittle-endian</code></p>
<dd>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a little-endian target.</p>
<dt><code>-m210</code></p>
<dd>
<dt><code>-m340</code></p>
<dd>Generate code for the 210 processor.</p>
<dt><code>-mno-lsim</code></p>
<dd>Assume that runtime support has been provided and so omit the simulator library (<i>libsim.a)</i> from the linker command line.</p>
<dt><code>-mstack-increment=</code><i>size</i></p>
<dd>Set the maximum amount for a single stack increment operation. Large values can increase the speed of programs that contain functions that need a large amount of stack space, but they can also trigger a segmentation fault if the stack is extended too much. The default value is 0x1000.</dl>
<p> <i>MeP Options</i></p>
<dl COMPACT>
<dt><code>-mabsdiff</code></p>
<dd>Enables the <tt>&quot;abs&quot;</tt> instruction, which is the absolute difference between two registers.</p>
<dt><code>-mall-opts</code></p>
<dd>Enables all the optional instructions&#8212;average, multiply, divide, bit operations, leading zero, absolute difference, min/max, clip, and saturation.</p>
<dt><code>-maverage</code></p>
<dd>Enables the <tt>&quot;ave&quot;</tt> instruction, which computes the average of two registers.</p>
<dt><code>-mbased=</code><i>n</i></p>
<dd>Variables of size <i>n</i> bytes or smaller are placed in the <tt>&quot;.based&quot;</tt> section by default. Based variables use the <tt>$tp</tt> register as a base register, and there is a 128-byte limit to the <tt>&quot;.based&quot;</tt> section.</p>
<dt><code>-mbitops</code></p>
<dd>Enables the bit operation instructions&#8212;bit test (<tt>&quot;btstm&quot;</tt>), set (<tt>&quot;bsetm&quot;</tt>), clear (<tt>&quot;bclrm&quot;</tt>), invert (<tt>&quot;bnotm&quot;</tt>), and test-and-set (<tt>&quot;tas&quot;</tt>).</p>
<dt><code>-mc=</code><i>name</i></p>
<dd>Selects which section constant data is placed in. <i>name</i> may be <tt>&quot;tiny&quot;</tt>, <tt>&quot;near&quot;</tt>, or <tt>&quot;far&quot;</tt>.</p>
<dt><code>-mclip</code></p>
<dd>Enables the <tt>&quot;clip&quot;</tt> instruction. Note that <tt>&quot;-mclip&quot;</tt> is not useful unless you also provide <tt>&quot;-mminmax&quot;</tt>.</p>
<dt><code>-mconfig=</code><i>name</i></p>
<dd>Selects one of the built-in core configurations. Each MeP chip has one or more modules in it; each module has a core <font SIZE="-1">CPU</font> and a variety of coprocessors, optional instructions, and peripherals. The <tt>&quot;MeP-Integrator&quot;</tt> tool, not part of <font SIZE="-1">GCC,</font> provides these configurations through this option; using this option is the same as using all the corresponding command-line options. The default configuration is <tt>&quot;default&quot;</tt>.</p>
<dt><code>-mcop</code></p>
<dd>Enables the coprocessor instructions. By default, this is a 32-bit coprocessor. Note that the coprocessor is normally enabled via the <tt>&quot;-mconfig=&quot;</tt> option.</p>
<dt><code>-mcop32</code></p>
<dd>Enables the 32-bit coprocessor&#8217;s instructions.</p>
<dt><code>-mcop64</code></p>
<dd>Enables the 64-bit coprocessor&#8217;s instructions.</p>
<dt><code>-mivc2</code></p>
<dd>Enables <font SIZE="-1">IVC2</font> scheduling. <font SIZE="-1">IVC2</font> is a 64-bit <font SIZE="-1">VLIW</font> coprocessor.</p>
<dt><code>-mdc</code></p>
<dd>Causes constant variables to be placed in the <tt>&quot;.near&quot;</tt> section.</p>
<dt><code>-mdiv</code></p>
<dd>Enables the <tt>&quot;div&quot;</tt> and <tt>&quot;divu&quot;</tt> instructions.</p>
<dt><code>-meb</code></p>
<dd>Generate big-endian code.</p>
<dt><code>-mel</code></p>
<dd>Generate little-endian code.</p>
<dt><code>-mio-volatile</code></p>
<dd>Tells the compiler that any variable marked with the <tt>&quot;io&quot;</tt> attribute is to be considered volatile.</p>
<dt><code>-ml</code></p>
<dd>Causes variables to be assigned to the <tt>&quot;.far&quot;</tt> section by default.</p>
<dt><code>-mleadz</code></p>
<dd>Enables the <tt>&quot;leadz&quot;</tt> (leading zero) instruction.</p>
<dt><code>-mm</code></p>
<dd>Causes variables to be assigned to the <tt>&quot;.near&quot;</tt> section by default.</p>
<dt><code>-mminmax</code></p>
<dd>Enables the <tt>&quot;min&quot;</tt> and <tt>&quot;max&quot;</tt> instructions.</p>
<dt><code>-mmult</code></p>
<dd>Enables the multiplication and multiply-accumulate instructions.</p>
<dt><code>-mno-opts</code></p>
<dd>Disables all the optional instructions enabled by <tt>&quot;-mall-opts&quot;</tt>.</p>
<dt><code>-mrepeat</code></p>
<dd>Enables the <tt>&quot;repeat&quot;</tt> and <tt>&quot;erepeat&quot;</tt> instructions, used for low-overhead looping.</p>
<dt><code>-ms</code></p>
<dd>Causes all variables to default to the <tt>&quot;.tiny&quot;</tt> section. Note that there is a 65536-byte limit to this section. Accesses to these variables use the <tt>%gp</tt> base register.</p>
<dt><code>-msatur</code></p>
<dd>Enables the saturation instructions. Note that the compiler does not currently generate these itself, but this option is included for compatibility with other tools, like <tt>&quot;as&quot;</tt>.</p>
<dt><code>-msdram</code></p>
<dd>Link the SDRAM-based runtime instead of the default ROM-based runtime.</p>
<dt><code>-msim</code></p>
<dd>Link the simulator run-time libraries.</p>
<dt><code>-msimnovec</code></p>
<dd>Link the simulator runtime libraries, excluding built-in support for reset and exception vectors and tables.</p>
<dt><code>-mtf</code></p>
<dd>Causes all functions to default to the <tt>&quot;.far&quot;</tt> section. Without this option, functions default to the <tt>&quot;.near&quot;</tt> section.</p>
<dt><code>-mtiny=</code><i>n</i></p>
<dd>Variables that are <i>n</i> bytes or smaller are allocated to the <tt>&quot;.tiny&quot;</tt> section. These variables use the <tt>$gp</tt> base register. The default for this option is 4, but note that there&#8217;s a 65536-byte limit to the <tt>&quot;.tiny&quot;</tt> section.</dl>
<p> <i>MicroBlaze Options</i></p>
<dl COMPACT>
<dt><code>-msoft-float</code></p>
<dd>Use software emulation for floating point (default).</p>
<dt><code>-mhard-float</code></p>
<dd>Use hardware floating-point instructions.</p>
<dt><code>-mmemcpy</code></p>
<dd>Do not optimize block moves, use <tt>&quot;memcpy&quot;</tt>.</p>
<dt><code>-mno-clearbss</code></p>
<dd>This option is deprecated. Use <code>-fno-zero-initialized-in-bss</code> instead.</p>
<dt><code>-mcpu=</code><i>cpu-type</i></p>
<dd>Use features of, and schedule code for, the given <font SIZE="-1">CPU.</font> Supported values are in the format <code>v</code><i>X</i><code>.</code><i></i><font SIZE="-1"><i>YY</i></font><i></i><code>.</code><i>Z</i>, where <i>X</i> is a major version, <i></i><font SIZE="-1"><i>YY</i></font><i></i> is the minor version, and <i>Z</i> is compatibility code. Example values are <code>v3.00.a</code>, <code>v4.00.b</code>, <code>v5.00.a</code>, <code>v5.00.b</code>, <code>v5.00.b</code>, <code>v6.00.a</code>.</p>
<dt><code>-mxl-soft-mul</code></p>
<dd>Use software multiply emulation (default).</p>
<dt><code>-mxl-soft-div</code></p>
<dd>Use software emulation for divides (default).</p>
<dt><code>-mxl-barrel-shift</code></p>
<dd>Use the hardware barrel shifter.</p>
<dt><code>-mxl-pattern-compare</code></p>
<dd>Use pattern compare instructions.</p>
<dt><code>-msmall-divides</code></p>
<dd>Use table lookup optimization for small signed integer divisions.</p>
<dt><code>-mxl-stack-check</code></p>
<dd>This option is deprecated. Use <code>-fstack-check</code> instead.</p>
<dt><code>-mxl-gp-opt</code></p>
<dd>Use GP-relative <tt>&quot;.sdata&quot;</tt>/<tt>&quot;.sbss&quot;</tt> sections.</p>
<dt><code>-mxl-multiply-high</code></p>
<dd>Use multiply high instructions for high part of 32&#215;32 multiply.</p>
<dt><code>-mxl-float-convert</code></p>
<dd>Use hardware floating-point conversion instructions.</p>
<dt><code>-mxl-float-sqrt</code></p>
<dd>Use hardware floating-point square root instruction.</p>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a big-endian target.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a little-endian target.</p>
<dt><code>-mxl-reorder</code></p>
<dd>Use reorder instructions (swap and byte reversed load/store).</p>
<dt><code>-mxl-mode-</code><i>app-model</i></p>
<dd>Select application model <i>app-model</i>. Valid models are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>executable</code></p>
<dd>normal executable (default), uses startup code <i>crt0.o</i>.</p>
<dt><code>xmdstub</code></p>
<dd>for use with Xilinx Microprocessor Debugger (<font SIZE="-1">XMD</font>) based software intrusive debug agent called xmdstub. This uses startup file <i>crt1.o</i> and sets the start address of the program to 0x800.</p>
<dt><code>bootstrap</code></p>
<dd>for applications that are loaded using a bootloader. This model uses startup file <i>crt2.o</i> which does not contain a processor reset vector handler. This is suitable for transferring control on a processor reset to the bootloader rather than the application.</p>
<dt><code>novectors</code></p>
<dd>for applications that do not require any of the MicroBlaze vectors. This option may be useful for applications running within a monitoring application. This model uses <i>crt3.o</i> as a startup file.</dl>
</dl>
<dl COMPACT>
<dd>Option <code>-xl-mode-</code><i>app-model</i> is a deprecated alias for <code>-mxl-mode-</code><i>app-model</i>.</dl>
</dl>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i></p>
<dl COMPACT>
<dt><code>-EB</code></p>
<dd>Generate big-endian code.</p>
<dt><code>-EL</code></p>
<dd>Generate little-endian code. This is the default for <code>mips*el-*-*</code> configurations.</p>
<dt><code>-march=</code><i>arch</i></p>
<dd>Generate code that runs on <i>arch</i>, which can be the name of a generic <font SIZE="-1">MIPS ISA,</font> or the name of a particular processor. The <font SIZE="-1">ISA</font> names are: <code>mips1</code>, <code>mips2</code>, <code>mips3</code>, <code>mips4</code>, <code>mips32</code>, <code>mips32r2</code>, <code>mips64</code> and <code>mips64r2</code>. The processor names are: <code>4kc</code>, <code>4km</code>, <code>4kp</code>, <code>4ksc</code>, <code>4kec</code>, <code>4kem</code>, <code>4kep</code>, <code>4ksd</code>, <code>5kc</code>, <code>5kf</code>, <code>20kc</code>, <code>24kc</code>, <code>24kf2_1</code>, <code>24kf1_1</code>, <code>24kec</code>, <code>24kef2_1</code>, <code>24kef1_1</code>, <code>34kc</code>, <code>34kf2_1</code>, <code>34kf1_1</code>, <code>34kn</code>, <code>74kc</code>, <code>74kf2_1</code>, <code>74kf1_1</code>, <code>74kf3_2</code>, <code>1004kc</code>, <code>1004kf2_1</code>, <code>1004kf1_1</code>, <code>loongson2e</code>, <code>loongson2f</code>, <code>loongson3a</code>, <code>m4k</code>, <code>m14k</code>, <code>m14kc</code>, <code>m14ke</code>, <code>m14kec</code>, <code>octeon</code>, <code>octeon+</code>, <code>octeon2</code>, <code>orion</code>, <code>r2000</code>, <code>r3000</code>, <code>r3900</code>, <code>r4000</code>, <code>r4400</code>, <code>r4600</code>, <code>r4650</code>, <code>r4700</code>, <code>r6000</code>, <code>r8000</code>, <code>rm7000</code>, <code>rm9000</code>, <code>r10000</code>, <code>r12000</code>, <code>r14000</code>, <code>r16000</code>, <code>sb1</code>, <code>sr71000</code>, <code>vr4100</code>, <code>vr4111</code>, <code>vr4120</code>, <code>vr4130</code>, <code>vr4300</code>, <code>vr5000</code>, <code>vr5400</code>, <code>vr5500</code>, <code>xlr</code> and <code>xlp</code>. The special value <code>from-abi</code> selects the most compatible architecture for the selected <font SIZE="-1">ABI </font>(that is, <code>mips1</code> for 32-bit ABIs and <code>mips3</code> for 64-bit ABIs). </p>
<p> The native Linux/GNU toolchain also supports the value <code>native</code>, which selects the best architecture option for the host processor. <code>-march=native</code> has no effect if <font SIZE="-1">GCC</font> does not recognize the processor. </p>
<p> In processor names, a final <code>000</code> can be abbreviated as <code>k</code> (for example, <code>-march=r2k</code>). Prefixes are optional, and <code>vr</code> may be written <code>r</code>. </p>
<p> Names of the form <i>n</i><code>f2_1</code> refer to processors with FPUs clocked at half the rate of the core, names of the form <i>n</i><code>f1_1</code> refer to processors with FPUs clocked at the same rate as the core, and names of the form <i>n</i><code>f3_2</code> refer to processors with FPUs clocked a ratio of 3:2 with respect to the core. For compatibility reasons, <i>n</i><code>f</code> is accepted as a synonym for <i>n</i><code>f2_1</code> while <i>n</i><code>x</code> and <i>b</i><code>fx</code> are accepted as synonyms for <i>n</i><code>f1_1</code>. </p>
<p> <font SIZE="-1">GCC</font> defines two macros based on the value of this option. The first is <code>_MIPS_ARCH</code>, which gives the name of target architecture, as a string. The second has the form <code>_MIPS_ARCH_</code><i>foo</i>, where <i>foo</i> is the capitalized value of <code>_MIPS_ARCH</code>. For example, <code>-march=r2000</code> sets <code>_MIPS_ARCH</code> to <code>&#8220;r2000&#8221;</code> and defines the macro <code>_MIPS_ARCH_R2000</code>. </p>
<p> Note that the <code>_MIPS_ARCH</code> macro uses the processor names given above. In other words, it has the full prefix and does not abbreviate <code>000</code> as <code>k</code>. In the case of <code>from-abi</code>, the macro names the resolved architecture (either <code>&#8220;mips1&#8221;</code> or <code>&#8220;mips3&#8221;</code>). It names the default architecture when no <code>-march</code> option is given.</p>
<dt><code>-mtune=</code><i>arch</i></p>
<dd>Optimize for <i>arch</i>. Among other things, this option controls the way instructions are scheduled, and the perceived cost of arithmetic operations. The list of <i>arch</i> values is the same as for <code>-march</code>. </p>
<p> When this option is not used, <font SIZE="-1">GCC</font> optimizes for the processor specified by <code>-march</code>. By using <code>-march</code> and <code>-mtune</code> together, it is possible to generate code that runs on a family of processors, but optimize the code for one particular member of that family. </p>
<p> <code>-mtune</code> defines the macros <code>_MIPS_TUNE</code> and <code>_MIPS_TUNE_</code><i>foo</i>, which work in the same way as the <code>-march</code> ones described above.</p>
<dt><code>-mips1</code></p>
<dd>Equivalent to <code>-march=mips1</code>.</p>
<dt><code>-mips2</code></p>
<dd>Equivalent to <code>-march=mips2</code>.</p>
<dt><code>-mips3</code></p>
<dd>Equivalent to <code>-march=mips3</code>.</p>
<dt><code>-mips4</code></p>
<dd>Equivalent to <code>-march=mips4</code>.</p>
<dt><code>-mips32</code></p>
<dd>Equivalent to <code>-march=mips32</code>.</p>
<dt><code>-mips32r2</code></p>
<dd>Equivalent to <code>-march=mips32r2</code>.</p>
<dt><code>-mips64</code></p>
<dd>Equivalent to <code>-march=mips64</code>.</p>
<dt><code>-mips64r2</code></p>
<dd>Equivalent to <code>-march=mips64r2</code>.</p>
<dt><code>-mips16</code></p>
<dd>
<dt><code>-mno-mips16</code></p>
<dd>Generate (do not generate) <font SIZE="-1">MIPS16</font> code. If <font SIZE="-1">GCC</font> is targeting a <font SIZE="-1">MIPS32</font> or <font SIZE="-1">MIPS64</font> architecture, it makes use of the MIPS16e <font SIZE="-1">ASE.</font> </p>
<p> <font SIZE="-1">MIPS16</font> code generation can also be controlled on a per-function basis by means of <tt>&quot;mips16&quot;</tt> and <tt>&quot;nomips16&quot;</tt> attributes.</p>
<dt><code>-mflip-mips16</code></p>
<dd>Generate <font SIZE="-1">MIPS16</font> code on alternating functions. This option is provided for regression testing of mixed MIPS16/non-MIPS16 code generation, and is not intended for ordinary use in compiling user code.</p>
<dt><code>-minterlink-compressed</code></p>
<dd>
<dt><code>-mno-interlink-compressed</code></p>
<dd>Require (do not require) that code using the standard (uncompressed) <font SIZE="-1">MIPS ISA</font> be link-compatible with <font SIZE="-1">MIPS16</font> and microMIPS code, and vice versa. </p>
<p> For example, code using the standard <font SIZE="-1">ISA</font> encoding cannot jump directly to <font SIZE="-1">MIPS16</font> or microMIPS code; it must either use a call or an indirect jump. <code>-minterlink-compressed</code> therefore disables direct jumps unless <font SIZE="-1">GCC</font> knows that the target of the jump is not compressed.</p>
<dt><code>-minterlink-mips16</code></p>
<dd>
<dt><code>-mno-interlink-mips16</code></p>
<dd>Aliases of <code>-minterlink-compressed</code> and <code>-mno-interlink-compressed</code>. These options predate the microMIPS <font SIZE="-1">ASE</font> and are retained for backwards compatibility.</p>
<dt><code>-mabi=32</code></p>
<dd>
<dt><code>-mabi=o64</code></p>
<dd>
<dt><code>-mabi=n32</code></p>
<dd>
<dt><code>-mabi=64</code></p>
<dd>
<dt><code>-mabi=eabi</code></p>
<dd>Generate code for the given <font SIZE="-1">ABI.</font> </p>
<p> Note that the <font SIZE="-1">EABI</font> has a 32-bit and a 64-bit variant. <font SIZE="-1">GCC</font> normally generates 64-bit code when you select a 64-bit architecture, but you can use <code>-mgp32</code> to get 32-bit code instead. </p>
<p> For information about the O64 <font SIZE="-1">ABI,</font> see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/projects/mipso64-abi.html">http://gcc.gnu.org/projects/mipso64-abi.html</a></code>&gt;. </p>
<p> <font SIZE="-1">GCC</font> supports a variant of the o32 <font SIZE="-1">ABI</font> in which floating-point registers are 64 rather than 32 bits wide. You can select this combination with <code>-mabi=32</code> <code>-mfp64</code>. This <font SIZE="-1">ABI</font> relies on the <tt>&quot;mthc1&quot;</tt> and <tt>&quot;mfhc1&quot;</tt> instructions and is therefore only supported for <font SIZE="-1">MIPS32R2</font> processors. </p>
<p> The register assignments for arguments and return values remain the same, but each scalar value is passed in a single 64-bit register rather than a pair of 32-bit registers. For example, scalar floating-point values are returned in $f0 only, not a $f0/$f1 pair. The set of call-saved registers also remains the same, but all 64 bits are saved.</p>
<dt><code>-mabicalls</code></p>
<dd>
<dt><code>-mno-abicalls</code></p>
<dd>Generate (do not generate) code that is suitable for SVR4-style dynamic objects. <code>-mabicalls</code> is the default for SVR4-based systems.</p>
<dt><code>-mshared</code></p>
<dd>
<dt><code>-mno-shared</code></p>
<dd>Generate (do not generate) code that is fully position-independent, and that can therefore be linked into shared libraries. This option only affects <code>-mabicalls</code>. </p>
<p> All <code>-mabicalls</code> code has traditionally been position-independent, regardless of options like <code>-fPIC</code> and <code>-fpic</code>. However, as an extension, the <font SIZE="-1">GNU</font> toolchain allows executables to use absolute accesses for locally-binding symbols. It can also use shorter <font SIZE="-1">GP</font> initialization sequences and generate direct calls to locally-defined functions. This mode is selected by <code>-mno-shared</code>. </p>
<p> <code>-mno-shared</code> depends on binutils 2.16 or higher and generates objects that can only be linked by the <font SIZE="-1">GNU</font> linker. However, the option does not affect the <font SIZE="-1">ABI</font> of the final executable; it only affects the <font SIZE="-1">ABI</font> of relocatable objects. Using <code>-mno-shared</code> generally makes executables both smaller and quicker. </p>
<p> <code>-mshared</code> is the default.</p>
<dt><code>-mplt</code></p>
<dd>
<dt><code>-mno-plt</code></p>
<dd>Assume (do not assume) that the static and dynamic linkers support PLTs and copy relocations. This option only affects <code>-mno-shared -mabicalls</code>. For the n64 <font SIZE="-1">ABI,</font> this option has no effect without <code>-msym32</code>. </p>
<p> You can make <code>-mplt</code> the default by configuring <font SIZE="-1">GCC</font> with <code>&#8211;with-mips-plt</code>. The default is <code>-mno-plt</code> otherwise.</p>
<dt><code>-mxgot</code></p>
<dd>
<dt><code>-mno-xgot</code></p>
<dd>Lift (do not lift) the usual restrictions on the size of the global offset table. </p>
<p> <font SIZE="-1">GCC</font> normally uses a single instruction to load values from the <font SIZE="-1">GOT.</font> While this is relatively efficient, it only works if the <font SIZE="-1">GOT</font> is smaller than about 64k. Anything larger causes the linker to report an error such as: </p>
<pre> relocation truncated to fit: R_MIPS_GOT16 foobar</pre>
<p>If this happens, you should recompile your code with <code>-mxgot</code>. This works with very large GOTs, although the code is also less efficient, since it takes three instructions to fetch the value of a global symbol. </p>
<p> Note that some linkers can create multiple GOTs. If you have such a linker, you should only need to use <code>-mxgot</code> when a single object file accesses more than 64k&#8217;s worth of <font SIZE="-1">GOT</font> entries. Very few do. </p>
<p> These options have no effect unless <font SIZE="-1">GCC</font> is generating position independent code.</p>
<dt><code>-mgp32</code></p>
<dd>Assume that general-purpose registers are 32 bits wide.</p>
<dt><code>-mgp64</code></p>
<dd>Assume that general-purpose registers are 64 bits wide.</p>
<dt><code>-mfp32</code></p>
<dd>Assume that floating-point registers are 32 bits wide.</p>
<dt><code>-mfp64</code></p>
<dd>Assume that floating-point registers are 64 bits wide.</p>
<dt><code>-mhard-float</code></p>
<dd>Use floating-point coprocessor instructions.</p>
<dt><code>-msoft-float</code></p>
<dd>Do not use floating-point coprocessor instructions. Implement floating-point calculations using library calls instead.</p>
<dt><code>-mno-float</code></p>
<dd>Equivalent to <code>-msoft-float</code>, but additionally asserts that the program being compiled does not perform any floating-point operations. This option is presently supported only by some bare-metal <font SIZE="-1">MIPS</font> configurations, where it may select a special set of libraries that lack all floating-point support (including, for example, the floating-point <tt>&quot;printf&quot;</tt> formats). If code compiled with <tt>&quot;-mno-float&quot;</tt> accidentally contains floating-point operations, it is likely to suffer a link-time or run-time failure.</p>
<dt><code>-msingle-float</code></p>
<dd>Assume that the floating-point coprocessor only supports single-precision operations.</p>
<dt><code>-mdouble-float</code></p>
<dd>Assume that the floating-point coprocessor supports double-precision operations. This is the default.</p>
<dt><code>-mabs=2008</code></p>
<dd>
<dt><code>-mabs=legacy</code></p>
<dd>These options control the treatment of the special not-a-number (NaN) <font SIZE="-1">IEEE 754</font> floating-point data with the <tt>&quot;abs.</tt>fmt<tt>&quot;</tt> and <tt>&quot;neg.</tt>fmt<tt>&quot;</tt> machine instructions. </p>
<p> By default or when the <code>-mabs=legacy</code> is used the legacy treatment is selected. In this case these instructions are considered arithmetic and avoided where correct operation is required and the input operand might be a NaN. A longer sequence of instructions that manipulate the sign bit of floating-point datum manually is used instead unless the <code>-ffinite-math-only</code> option has also been specified. </p>
<p> The <code>-mabs=2008</code> option selects the <font SIZE="-1">IEEE 754-2008</font> treatment. In this case these instructions are considered non-arithmetic and therefore operating correctly in all cases, including in particular where the input operand is a NaN. These instructions are therefore always used for the respective operations.</p>
<dt><code>-mnan=2008</code></p>
<dd>
<dt><code>-mnan=legacy</code></p>
<dd>These options control the encoding of the special not-a-number (NaN) <font SIZE="-1">IEEE 754</font> floating-point data. </p>
<p> The <code>-mnan=legacy</code> option selects the legacy encoding. In this case quiet NaNs (qNaNs) are denoted by the first bit of their trailing significand field being 0, whereas signalling NaNs (sNaNs) are denoted by the first bit of their trailing significand field being 1. </p>
<p> The <code>-mnan=2008</code> option selects the <font SIZE="-1">IEEE 754-2008</font> encoding. In this case qNaNs are denoted by the first bit of their trailing significand field being 1, whereas sNaNs are denoted by the first bit of their trailing significand field being 0. </p>
<p> The default is <code>-mnan=legacy</code> unless <font SIZE="-1">GCC</font> has been configured with <code>&#8211;with-nan=2008</code>.</p>
<dt><code>-mllsc</code></p>
<dd>
<dt><code>-mno-llsc</code></p>
<dd>Use (do not use) <code>ll</code>, <code>sc</code>, and <code>sync</code> instructions to implement atomic memory built-in functions. When neither option is specified, <font SIZE="-1">GCC</font> uses the instructions if the target architecture supports them. </p>
<p> <code>-mllsc</code> is useful if the runtime environment can emulate the instructions and <code>-mno-llsc</code> can be useful when compiling for nonstandard ISAs. You can make either option the default by configuring <font SIZE="-1">GCC</font> with <code>&#8211;with-llsc</code> and <code>&#8211;without-llsc</code> respectively. <code>&#8211;with-llsc</code> is the default for some configurations; see the installation documentation for details.</p>
<dt><code>-mdsp</code></p>
<dd>
<dt><code>-mno-dsp</code></p>
<dd>Use (do not use) revision 1 of the <font SIZE="-1">MIPS DSP ASE.<br />
&nbsp;<wbr></font>&nbsp;<wbr>This option defines the preprocessor macro <code>__mips_dsp</code>. It also defines <code>__mips_dsp_rev</code> to 1.</p>
<dt><code>-mdspr2</code></p>
<dd>
<dt><code>-mno-dspr2</code></p>
<dd>Use (do not use) revision 2 of the <font SIZE="-1">MIPS DSP ASE.<br />
&nbsp;<wbr></font>&nbsp;<wbr>This option defines the preprocessor macros <code>__mips_dsp</code> and <code>__mips_dspr2</code>. It also defines <code>__mips_dsp_rev</code> to 2.</p>
<dt><code>-msmartmips</code></p>
<dd>
<dt><code>-mno-smartmips</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS</font> SmartMIPS <font SIZE="-1">ASE.</font></p>
<dt><code>-mpaired-single</code></p>
<dd>
<dt><code>-mno-paired-single</code></p>
<dd>Use (do not use) paired-single floating-point instructions.<br />
&nbsp;<wbr>&nbsp;<wbr>This option requires hardware floating-point support to be enabled.</p>
<dt><code>-mdmx</code></p>
<dd>
<dt><code>-mno-mdmx</code></p>
<dd>Use (do not use) <font SIZE="-1">MIPS</font> Digital Media Extension instructions. This option can only be used when generating 64-bit code and requires hardware floating-point support to be enabled.</p>
<dt><code>-mips3d</code></p>
<dd>
<dt><code>-mno-mips3d</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS-3D ASE. </font> The option <code>-mips3d</code> implies <code>-mpaired-single</code>.</p>
<dt><code>-mmicromips</code></p>
<dd>
<dt><code>-mno-micromips</code></p>
<dd>Generate (do not generate) microMIPS code. </p>
<p> MicroMIPS code generation can also be controlled on a per-function basis by means of <tt>&quot;micromips&quot;</tt> and <tt>&quot;nomicromips&quot;</tt> attributes.</p>
<dt><code>-mmt</code></p>
<dd>
<dt><code>-mno-mt</code></p>
<dd>Use (do not use) <font SIZE="-1">MT</font> Multithreading instructions.</p>
<dt><code>-mmcu</code></p>
<dd>
<dt><code>-mno-mcu</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS MCU ASE</font> instructions.</p>
<dt><code>-meva</code></p>
<dd>
<dt><code>-mno-eva</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS</font> Enhanced Virtual Addressing instructions.</p>
<dt><code>-mvirt</code></p>
<dd>
<dt><code>-mno-virt</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS</font> Virtualization Application Specific instructions.</p>
<dt><code>-mlong64</code></p>
<dd>Force <tt>&quot;long&quot;</tt> types to be 64 bits wide. See <code>-mlong32</code> for an explanation of the default and the way that the pointer size is determined.</p>
<dt><code>-mlong32</code></p>
<dd>Force <tt>&quot;long&quot;</tt>, <tt>&quot;int&quot;</tt>, and pointer types to be 32 bits wide. </p>
<p> The default size of <tt>&quot;int&quot;</tt>s, <tt>&quot;long&quot;</tt>s and pointers depends on the <font SIZE="-1">ABI. </font> All the supported ABIs use 32-bit <tt>&quot;int&quot;</tt>s. The n64 <font SIZE="-1">ABI</font> uses 64-bit <tt>&quot;long&quot;</tt>s, as does the 64-bit <font SIZE="-1">EABI</font>; the others use 32-bit <tt>&quot;long&quot;</tt>s. Pointers are the same size as <tt>&quot;long&quot;</tt>s, or the same size as integer registers, whichever is smaller.</p>
<dt><code>-msym32</code></p>
<dd>
<dt><code>-mno-sym32</code></p>
<dd>Assume (do not assume) that all symbols have 32-bit values, regardless of the selected <font SIZE="-1">ABI. </font> This option is useful in combination with <code>-mabi=64</code> and <code>-mno-abicalls</code> because it allows <font SIZE="-1">GCC</font> to generate shorter and faster references to symbolic addresses.</p>
<dt><code>-G</code> <i>num</i></p>
<dd>Put definitions of externally-visible data in a small data section if that data is no bigger than <i>num</i> bytes. <font SIZE="-1">GCC</font> can then generate more efficient accesses to the data; see <code>-mgpopt</code> for details. </p>
<p> The default <code>-G</code> option depends on the configuration.</p>
<dt><code>-mlocal-sdata</code></p>
<dd>
<dt><code>-mno-local-sdata</code></p>
<dd>Extend (do not extend) the <code>-G</code> behavior to local data too, such as to static variables in C. <code>-mlocal-sdata</code> is the default for all configurations. </p>
<p> If the linker complains that an application is using too much small data, you might want to try rebuilding the less performance-critical parts with <code>-mno-local-sdata</code>. You might also want to build large libraries with <code>-mno-local-sdata</code>, so that the libraries leave more room for the main program.</p>
<dt><code>-mextern-sdata</code></p>
<dd>
<dt><code>-mno-extern-sdata</code></p>
<dd>Assume (do not assume) that externally-defined data is in a small data section if the size of that data is within the <code>-G</code> limit. <code>-mextern-sdata</code> is the default for all configurations. </p>
<p> If you compile a module <i>Mod</i> with <code>-mextern-sdata</code> <code>-G</code> <i>num</i> <code>-mgpopt</code>, and <i>Mod</i> references a variable <i>Var</i> that is no bigger than <i>num</i> bytes, you must make sure that <i>Var</i> is placed in a small data section. If <i>Var</i> is defined by another module, you must either compile that module with a high-enough <code>-G</code> setting or attach a <tt>&quot;section&quot;</tt> attribute to <i>Var</i>&#8216;s definition. If <i>Var</i> is common, you must link the application with a high-enough <code>-G</code> setting. </p>
<p> The easiest way of satisfying these restrictions is to compile and link every module with the same <code>-G</code> option. However, you may wish to build a library that supports several different small data limits. You can do this by compiling the library with the highest supported <code>-G</code> setting and additionally using <code>-mno-extern-sdata</code> to stop the library from making assumptions about externally-defined data.</p>
<dt><code>-mgpopt</code></p>
<dd>
<dt><code>-mno-gpopt</code></p>
<dd>Use (do not use) GP-relative accesses for symbols that are known to be in a small data section; see <code>-G</code>, <code>-mlocal-sdata</code> and <code>-mextern-sdata</code>. <code>-mgpopt</code> is the default for all configurations. </p>
<p> <code>-mno-gpopt</code> is useful for cases where the <tt>$gp</tt> register might not hold the value of <tt>&quot;_gp&quot;</tt>. For example, if the code is part of a library that might be used in a boot monitor, programs that call boot monitor routines pass an unknown value in <tt>$gp</tt>. (In such situations, the boot monitor itself is usually compiled with <code>-G0</code>.) </p>
<p> <code>-mno-gpopt</code> implies <code>-mno-local-sdata</code> and <code>-mno-extern-sdata</code>.</p>
<dt><code>-membedded-data</code></p>
<dd>
<dt><code>-mno-embedded-data</code></p>
<dd>Allocate variables to the read-only data section first if possible, then next in the small data section if possible, otherwise in data. This gives slightly slower code than the default, but reduces the amount of <font SIZE="-1">RAM</font> required when executing, and thus may be preferred for some embedded systems.</p>
<dt><code>-muninit-const-in-rodata</code></p>
<dd>
<dt><code>-mno-uninit-const-in-rodata</code></p>
<dd>Put uninitialized <tt>&quot;const&quot;</tt> variables in the read-only data section. This option is only meaningful in conjunction with <code>-membedded-data</code>.</p>
<dt><code>-mcode-readable=</code><i>setting</i></p>
<dd>Specify whether <font SIZE="-1">GCC</font> may generate code that reads from executable sections. There are three possible settings:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-mcode-readable=yes</code></p>
<dd>Instructions may freely access executable sections. This is the default setting.</p>
<dt><code>-mcode-readable=pcrel</code></p>
<dd><font SIZE="-1">MIPS16</font> PC-relative load instructions can access executable sections, but other instructions must not do so. This option is useful on 4KSc and 4KSd processors when the code TLBs have the Read Inhibit bit set. It is also useful on processors that can be configured to have a dual instruction/data <font SIZE="-1">SRAM</font> interface and that, like the M4K, automatically redirect PC-relative loads to the instruction <font SIZE="-1">RAM.</font></p>
<dt><code>-mcode-readable=no</code></p>
<dd>Instructions must not access executable sections. This option can be useful on targets that are configured to have a dual instruction/data <font SIZE="-1">SRAM</font> interface but that (unlike the M4K) do not automatically redirect PC-relative loads to the instruction <font SIZE="-1">RAM.</font></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-msplit-addresses</code></p>
<dd>
<dt><code>-mno-split-addresses</code></p>
<dd>Enable (disable) use of the <tt>&quot;%hi()&quot;</tt> and <tt>&quot;%lo()&quot;</tt> assembler relocation operators. This option has been superseded by <code>-mexplicit-relocs</code> but is retained for backwards compatibility.</p>
<dt><code>-mexplicit-relocs</code></p>
<dd>
<dt><code>-mno-explicit-relocs</code></p>
<dd>Use (do not use) assembler relocation operators when dealing with symbolic addresses. The alternative, selected by <code>-mno-explicit-relocs</code>, is to use assembler macros instead. </p>
<p> <code>-mexplicit-relocs</code> is the default if <font SIZE="-1">GCC</font> was configured to use an assembler that supports relocation operators.</p>
<dt><code>-mcheck-zero-division</code></p>
<dd>
<dt><code>-mno-check-zero-division</code></p>
<dd>Trap (do not trap) on integer division by zero. </p>
<p> The default is <code>-mcheck-zero-division</code>.</p>
<dt><code>-mdivide-traps</code></p>
<dd>
<dt><code>-mdivide-breaks</code></p>
<dd><font SIZE="-1">MIPS</font> systems check for division by zero by generating either a conditional trap or a break instruction. Using traps results in smaller code, but is only supported on <font SIZE="-1">MIPS II</font> and later. Also, some versions of the Linux kernel have a bug that prevents trap from generating the proper signal (<tt>&quot;SIGFPE&quot;</tt>). Use <code>-mdivide-traps</code> to allow conditional traps on architectures that support them and <code>-mdivide-breaks</code> to force the use of breaks. </p>
<p> The default is usually <code>-mdivide-traps</code>, but this can be overridden at configure time using <code>&#8211;with-divide=breaks</code>. Divide-by-zero checks can be completely disabled using <code>-mno-check-zero-division</code>.</p>
<dt><code>-mmemcpy</code></p>
<dd>
<dt><code>-mno-memcpy</code></p>
<dd>Force (do not force) the use of <tt>&quot;memcpy()&quot;</tt> for non-trivial block moves. The default is <code>-mno-memcpy</code>, which allows <font SIZE="-1">GCC</font> to inline most constant-sized copies.</p>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Disable (do not disable) use of the <tt>&quot;jal&quot;</tt> instruction. Calling functions using <tt>&quot;jal&quot;</tt> is more efficient but requires the caller and callee to be in the same 256 megabyte segment. </p>
<p> This option has no effect on abicalls code. The default is <code>-mno-long-calls</code>.</p>
<dt><code>-mmad</code></p>
<dd>
<dt><code>-mno-mad</code></p>
<dd>Enable (disable) use of the <tt>&quot;mad&quot;</tt>, <tt>&quot;madu&quot;</tt> and <tt>&quot;mul&quot;</tt> instructions, as provided by the R4650 <font SIZE="-1">ISA.</font></p>
<dt><code>-mimadd</code></p>
<dd>
<dt><code>-mno-imadd</code></p>
<dd>Enable (disable) use of the <tt>&quot;madd&quot;</tt> and <tt>&quot;msub&quot;</tt> integer instructions. The default is <code>-mimadd</code> on architectures that support <tt>&quot;madd&quot;</tt> and <tt>&quot;msub&quot;</tt> except for the 74k architecture where it was found to generate slower code.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Enable (disable) use of the floating-point multiply-accumulate instructions, when they are available. The default is <code>-mfused-madd</code>. </p>
<p> On the R8000 <font SIZE="-1">CPU</font> when multiply-accumulate instructions are used, the intermediate product is calculated to infinite precision and is not subject to the <font SIZE="-1">FCSR</font> Flush to Zero bit. This may be undesirable in some circumstances. On other processors the result is numerically identical to the equivalent computation using separate multiply, add, subtract and negate instructions.</p>
<dt><code>-nocpp</code></p>
<dd>Tell the <font SIZE="-1">MIPS</font> assembler to not run its preprocessor over user assembler files (with a <code>.s</code> suffix) when assembling them.</p>
<dt><code>-mfix-24k</code></p>
<dd>
<dt><code>-mno-fix-24k</code></p>
<dd>Work around the 24K E48 (lost data on stores during refill) errata. The workarounds are implemented by the assembler rather than by <font SIZE="-1">GCC.</font></p>
<dt><code>-mfix-r4000</code></p>
<dd>
<dt><code>-mno-fix-r4000</code></p>
<dd>Work around certain R4000 <font SIZE="-1">CPU</font> errata:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>A double-word or a variable shift may give an incorrect result if executed immediately after starting an integer division.</p>
<dt>&#8211;</p>
<dd>A double-word or a variable shift may give an incorrect result if executed while an integer multiplication is in progress.</p>
<dt>&#8211;</p>
<dd>An integer division may give an incorrect result if started in a delay slot of a taken branch or a jump.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mfix-r4400</code></p>
<dd>
<dt><code>-mno-fix-r4400</code></p>
<dd>Work around certain R4400 <font SIZE="-1">CPU</font> errata:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>A double-word or a variable shift may give an incorrect result if executed immediately after starting an integer division.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mfix-r10000</code></p>
<dd>
<dt><code>-mno-fix-r10000</code></p>
<dd>Work around certain R10000 errata:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd><tt>&quot;ll&quot;</tt>/<tt>&quot;sc&quot;</tt> sequences may not behave atomically on revisions prior to 3.0. They may deadlock on revisions 2.6 and earlier.</dl>
</dl>
<dl COMPACT>
<dd>This option can only be used if the target architecture supports branch-likely instructions. <code>-mfix-r10000</code> is the default when <code>-march=r10000</code> is used; <code>-mno-fix-r10000</code> is the default otherwise.</dl>
<dt><code>-mfix-rm7000</code></p>
<dd>
<dt><code>-mno-fix-rm7000</code></p>
<dd>Work around the <font SIZE="-1">RM7000 </font><tt>&quot;dmult&quot;</tt>/<tt>&quot;dmultu&quot;</tt> errata. The workarounds are implemented by the assembler rather than by <font SIZE="-1">GCC.</font></p>
<dt><code>-mfix-vr4120</code></p>
<dd>
<dt><code>-mno-fix-vr4120</code></p>
<dd>Work around certain <font SIZE="-1">VR4120</font> errata:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd><tt>&quot;dmultu&quot;</tt> does not always produce the correct result.</p>
<dt>&#8211;</p>
<dd><tt>&quot;div&quot;</tt> and <tt>&quot;ddiv&quot;</tt> do not always produce the correct result if one of the operands is negative.</dl>
</dl>
<dl COMPACT>
<dd>The workarounds for the division errata rely on special functions in <i>libgcc.a</i>. At present, these functions are only provided by the <tt>&quot;mips64vr*-elf&quot;</tt> configurations. </p>
<p> Other <font SIZE="-1">VR4120</font> errata require a <font SIZE="-1">NOP</font> to be inserted between certain pairs of instructions. These errata are handled by the assembler, not by <font SIZE="-1">GCC</font> itself.</dl>
<dt><code>-mfix-vr4130</code></p>
<dd>Work around the <font SIZE="-1">VR4130 </font><tt>&quot;mflo&quot;</tt>/<tt>&quot;mfhi&quot;</tt> errata. The workarounds are implemented by the assembler rather than by <font SIZE="-1">GCC,</font> although <font SIZE="-1">GCC</font> avoids using <tt>&quot;mflo&quot;</tt> and <tt>&quot;mfhi&quot;</tt> if the <font SIZE="-1">VR4130 </font><tt>&quot;macc&quot;</tt>, <tt>&quot;macchi&quot;</tt>, <tt>&quot;dmacc&quot;</tt> and <tt>&quot;dmacchi&quot;</tt> instructions are available instead.</p>
<dt><code>-mfix-sb1</code></p>
<dd>
<dt><code>-mno-fix-sb1</code></p>
<dd>Work around certain <font SIZE="-1">SB-1 CPU</font> core errata. (This flag currently works around the <font SIZE="-1">SB-1</font> revision 2 &#8220;F1&#8221; and &#8220;F2&#8221; floating-point errata.)</p>
<dt><code>-mr10k-cache-barrier=</code><i>setting</i></p>
<dd>Specify whether <font SIZE="-1">GCC</font> should insert cache barriers to avoid the side-effects of speculation on R10K processors. </p>
<p> In common with many processors, the R10K tries to predict the outcome of a conditional branch and speculatively executes instructions from the &#8220;taken&#8221; branch. It later aborts these instructions if the predicted outcome is wrong. However, on the R10K, even aborted instructions can have side effects. </p>
<p> This problem only affects kernel stores and, depending on the system, kernel loads. As an example, a speculatively-executed store may load the target memory into cache and mark the cache line as dirty, even if the store itself is later aborted. If a <font SIZE="-1">DMA</font> operation writes to the same area of memory before the &#8220;dirty&#8221; line is flushed, the cached data overwrites the DMA-ed data. See the R10K processor manual for a full description, including other potential problems. </p>
<p> One workaround is to insert cache barrier instructions before every memory access that might be speculatively executed and that might have side effects even if aborted. <code>-mr10k-cache-barrier=</code><i>setting</i> controls <font SIZE="-1">GCC</font>&#8216;s implementation of this workaround. It assumes that aborted accesses to any byte in the following regions does not have side effects:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1.</p>
<dd>the memory occupied by the current function&#8217;s stack frame;</p>
<dt>2.</p>
<dd>the memory occupied by an incoming stack argument;</p>
<dt>3.</p>
<dd>the memory occupied by an object with a link-time-constant address.</dl>
</dl>
<dl COMPACT>
<dd>It is the kernel&#8217;s responsibility to ensure that speculative accesses to these regions are indeed safe. </p>
<p> If the input program contains a function declaration such as: </p>
<pre> void foo (void);</pre>
<p>then the implementation of <tt>&quot;foo&quot;</tt> must allow <tt>&quot;j foo&quot;</tt> and <tt>&quot;jal foo&quot;</tt> to be executed speculatively. <font SIZE="-1">GCC</font> honors this restriction for functions it compiles itself. It expects non-GCC functions (such as hand-written assembly code) to do the same. </p>
<p> The option has three forms:</p>
<dl COMPACT>
<dt><code>-mr10k-cache-barrier=load-store</code></p>
<dd>Insert a cache barrier before a load or store that might be speculatively executed and that might have side effects even if aborted.</p>
<dt><code>-mr10k-cache-barrier=store</code></p>
<dd>Insert a cache barrier before a store that might be speculatively executed and that might have side effects even if aborted.</p>
<dt><code>-mr10k-cache-barrier=none</code></p>
<dd>Disable the insertion of cache barriers. This is the default setting.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mflush-func=</code><i>func</i></p>
<dd>
<dt><code>-mno-flush-func</code></p>
<dd>Specifies the function to call to flush the I and D caches, or to not call any such function. If called, the function must take the same arguments as the common <tt>&quot;_flush_func()&quot;</tt>, that is, the address of the memory range for which the cache is being flushed, the size of the memory range, and the number 3 (to flush both caches). The default depends on the target <font SIZE="-1">GCC</font> was configured for, but commonly is either <code>_flush_func</code> or <code>__cpu_flush</code>.</p>
<dt><code>mbranch-cost=</code><i>num</i></p>
<dd>Set the cost of branches to roughly <i>num</i> &#8220;simple&#8221; instructions. This cost is only a heuristic and is not guaranteed to produce consistent results across releases. A zero cost redundantly selects the default, which is based on the <code>-mtune</code> setting.</p>
<dt><code>-mbranch-likely</code></p>
<dd>
<dt><code>-mno-branch-likely</code></p>
<dd>Enable or disable use of Branch Likely instructions, regardless of the default for the selected architecture. By default, Branch Likely instructions may be generated if they are supported by the selected architecture. An exception is for the <font SIZE="-1">MIPS32</font> and <font SIZE="-1">MIPS64</font> architectures and processors that implement those architectures; for those, Branch Likely instructions are not be generated by default because the <font SIZE="-1">MIPS32</font> and <font SIZE="-1">MIPS64</font> architectures specifically deprecate their use.</p>
<dt><code>-mfp-exceptions</code></p>
<dd>
<dt><code>-mno-fp-exceptions</code></p>
<dd>Specifies whether <font SIZE="-1">FP</font> exceptions are enabled. This affects how <font SIZE="-1">FP</font> instructions are scheduled for some processors. The default is that <font SIZE="-1">FP</font> exceptions are enabled. </p>
<p> For instance, on the <font SIZE="-1">SB-1,</font> if <font SIZE="-1">FP</font> exceptions are disabled, and we are emitting 64-bit code, then we can use both <font SIZE="-1">FP</font> pipes. Otherwise, we can only use one <font SIZE="-1">FP</font> pipe.</p>
<dt><code>-mvr4130-align</code></p>
<dd>
<dt><code>-mno-vr4130-align</code></p>
<dd>The <font SIZE="-1">VR4130</font> pipeline is two-way superscalar, but can only issue two instructions together if the first one is 8-byte aligned. When this option is enabled, <font SIZE="-1">GCC</font> aligns pairs of instructions that it thinks should execute in parallel. </p>
<p> This option only has an effect when optimizing for the <font SIZE="-1">VR4130.</font> It normally makes code faster, but at the expense of making it bigger. It is enabled by default at optimization level <code>-O3</code>.</p>
<dt><code>-msynci</code></p>
<dd>
<dt><code>-mno-synci</code></p>
<dd>Enable (disable) generation of <tt>&quot;synci&quot;</tt> instructions on architectures that support it. The <tt>&quot;synci&quot;</tt> instructions (if enabled) are generated when <tt>&quot;__builtin___clear_cache()&quot;</tt> is compiled. </p>
<p> This option defaults to <tt>&quot;-mno-synci&quot;</tt>, but the default can be overridden by configuring with <tt>&quot;--with-synci&quot;</tt>. </p>
<p> When compiling code for single processor systems, it is generally safe to use <tt>&quot;synci&quot;</tt>. However, on many multi-core (<font SIZE="-1">SMP</font>) systems, it does not invalidate the instruction caches on all cores and may lead to undefined behavior.</p>
<dt><code>-mrelax-pic-calls</code></p>
<dd>
<dt><code>-mno-relax-pic-calls</code></p>
<dd>Try to turn <font SIZE="-1">PIC</font> calls that are normally dispatched via register <tt>$25</tt> into direct calls. This is only possible if the linker can resolve the destination at link-time and if the destination is within range for a direct call. </p>
<p> <code>-mrelax-pic-calls</code> is the default if <font SIZE="-1">GCC</font> was configured to use an assembler and a linker that support the <tt>&quot;.reloc&quot;</tt> assembly directive and <tt>&quot;-mexplicit-relocs&quot;</tt> is in effect. With <tt>&quot;-mno-explicit-relocs&quot;</tt>, this optimization can be performed by the assembler and the linker alone without help from the compiler.</p>
<dt><code>-mmcount-ra-address</code></p>
<dd>
<dt><code>-mno-mcount-ra-address</code></p>
<dd>Emit (do not emit) code that allows <tt>&quot;_mcount&quot;</tt> to modify the calling function&#8217;s return address. When enabled, this option extends the usual <tt>&quot;_mcount&quot;</tt> interface with a new <i>ra-address</i> parameter, which has type <tt>&quot;intptr_t *&quot;</tt> and is passed in register <tt>$12</tt>. <tt>&quot;_mcount&quot;</tt> can then modify the return address by doing both of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Returning the new address in register <tt>$31</tt>.</p>
<dt>&bull;</p>
<dd>Storing the new address in <tt>&quot;*</tt>ra-address<tt>&quot;</tt>, if <i>ra-address</i> is nonnull.</dl>
</dl>
<dl COMPACT>
<dd>The default is <code>-mno-mcount-ra-address</code>.</dl>
</dl>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i> </p>
<p> These options are defined for the <font SIZE="-1">MMIX:</font></p>
<dl COMPACT>
<dt><code>-mlibfuncs</code></p>
<dd>
<dt><code>-mno-libfuncs</code></p>
<dd>Specify that intrinsic library functions are being compiled, passing all values in registers, no matter the size.</p>
<dt><code>-mepsilon</code></p>
<dd>
<dt><code>-mno-epsilon</code></p>
<dd>Generate floating-point comparison instructions that compare with respect to the <tt>&quot;rE&quot;</tt> epsilon register.</p>
<dt><code>-mabi=mmixware</code></p>
<dd>
<dt><code>-mabi=gnu</code></p>
<dd>Generate code that passes function parameters and return values that (in the called function) are seen as registers <tt>$0</tt> and up, as opposed to the <font SIZE="-1">GNU ABI</font> which uses global registers <tt>$231</tt> and up.</p>
<dt><code>-mzero-extend</code></p>
<dd>
<dt><code>-mno-zero-extend</code></p>
<dd>When reading data from memory in sizes shorter than 64 bits, use (do not use) zero-extending load instructions by default, rather than sign-extending ones.</p>
<dt><code>-mknuthdiv</code></p>
<dd>
<dt><code>-mno-knuthdiv</code></p>
<dd>Make the result of a division yielding a remainder have the same sign as the divisor. With the default, <code>-mno-knuthdiv</code>, the sign of the remainder follows the sign of the dividend. Both methods are arithmetically valid, the latter being almost exclusively used.</p>
<dt><code>-mtoplevel-symbols</code></p>
<dd>
<dt><code>-mno-toplevel-symbols</code></p>
<dd>Prepend (do not prepend) a <code>:</code> to all global symbols, so the assembly code can be used with the <tt>&quot;PREFIX&quot;</tt> assembly directive.</p>
<dt><code>-melf</code></p>
<dd>Generate an executable in the <font SIZE="-1">ELF</font> format, rather than the default <code>mmo</code> format used by the <code>mmix</code> simulator.</p>
<dt><code>-mbranch-predict</code></p>
<dd>
<dt><code>-mno-branch-predict</code></p>
<dd>Use (do not use) the probable-branch instructions, when static branch prediction indicates a probable branch.</p>
<dt><code>-mbase-addresses</code></p>
<dd>
<dt><code>-mno-base-addresses</code></p>
<dd>Generate (do not generate) code that uses <i>base addresses</i>. Using a base address automatically generates a request (handled by the assembler and the linker) for a constant to be set up in a global register. The register is used for one or more base address requests within the range 0 to 255 from the value held in the register. The generally leads to short and fast code, but the number of different data items that can be addressed is limited. This means that a program that uses lots of static data may require <code>-mno-base-addresses</code>.</p>
<dt><code>-msingle-exit</code></p>
<dd>
<dt><code>-mno-single-exit</code></p>
<dd>Force (do not force) generated code to have a single exit point in each function.</dl>
<p> <i></i><font SIZE="-1"><i>MN10300</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for Matsushita <font SIZE="-1">MN10300</font> architectures:</p>
<dl COMPACT>
<dt><code>-mmult-bug</code></p>
<dd>Generate code to avoid bugs in the multiply instructions for the <font SIZE="-1">MN10300</font> processors. This is the default.</p>
<dt><code>-mno-mult-bug</code></p>
<dd>Do not generate code to avoid bugs in the multiply instructions for the <font SIZE="-1">MN10300</font> processors.</p>
<dt><code>-mam33</code></p>
<dd>Generate code using features specific to the <font SIZE="-1">AM33</font> processor.</p>
<dt><code>-mno-am33</code></p>
<dd>Do not generate code using features specific to the <font SIZE="-1">AM33</font> processor. This is the default.</p>
<dt><code>-mam33-2</code></p>
<dd>Generate code using features specific to the <font SIZE="-1">AM33/2.0</font> processor.</p>
<dt><code>-mam34</code></p>
<dd>Generate code using features specific to the <font SIZE="-1">AM34</font> processor.</p>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Use the timing characteristics of the indicated <font SIZE="-1">CPU</font> type when scheduling instructions. This does not change the targeted processor type. The <font SIZE="-1">CPU</font> type must be one of <code>mn10300</code>, <code>am33</code>, <code>am33-2</code> or <code>am34</code>.</p>
<dt><code>-mreturn-pointer-on-d0</code></p>
<dd>When generating a function that returns a pointer, return the pointer in both <tt>&quot;a0&quot;</tt> and <tt>&quot;d0&quot;</tt>. Otherwise, the pointer is returned only in <tt>&quot;a0&quot;</tt>, and attempts to call such functions without a prototype result in errors. Note that this option is on by default; use <code>-mno-return-pointer-on-d0</code> to disable it.</p>
<dt><code>-mno-crt0</code></p>
<dd>Do not link in the C run-time initialization object file.</p>
<dt><code>-mrelax</code></p>
<dd>Indicate to the linker that it should perform a relaxation optimization pass to shorten branches, calls and absolute memory addresses. This option only has an effect when used on the command line for the final link step. </p>
<p> This option makes symbolic debugging impossible.</p>
<dt><code>-mliw</code></p>
<dd>Allow the compiler to generate <i>Long Instruction Word</i> instructions if the target is the <font SIZE="-1"><code>AM33</code></font> or later. This is the default. This option defines the preprocessor macro <code>__LIW__</code>.</p>
<dt><code>-mnoliw</code></p>
<dd>Do not allow the compiler to generate <i>Long Instruction Word</i> instructions. This option defines the preprocessor macro <code>__NO_LIW__</code>.</p>
<dt><code>-msetlb</code></p>
<dd>Allow the compiler to generate the <i></i><font SIZE="-1"><i>SETLB</i></font><i></i> and <i>Lcc</i> instructions if the target is the <font SIZE="-1"><code>AM33</code></font> or later. This is the default. This option defines the preprocessor macro <code>__SETLB__</code>.</p>
<dt><code>-mnosetlb</code></p>
<dd>Do not allow the compiler to generate <i></i><font SIZE="-1"><i>SETLB</i></font><i></i> or <i>Lcc</i> instructions. This option defines the preprocessor macro <code>__NO_SETLB__</code>.</dl>
<p> <i>Moxie Options</i></p>
<dl COMPACT>
<dt><code>-meb</code></p>
<dd>Generate big-endian code. This is the default for <code>moxie-*-*</code> configurations.</p>
<dt><code>-mel</code></p>
<dd>Generate little-endian code.</p>
<dt><code>-mno-crt0</code></p>
<dd>Do not link in the C run-time initialization object file.</dl>
<p> <i></i><font SIZE="-1"><i>MSP430</i></font><i> Options</i> </p>
<p> These options are defined for the <font SIZE="-1">MSP430:</font></p>
<dl COMPACT>
<dt><code>-masm-hex</code></p>
<dd>Force assembly output to always use hex constants. Normally such constants are signed decimals, but this option is available for testsuite and/or aesthetic purposes.</p>
<dt><code>-mmcu=</code></p>
<dd>Select the <font SIZE="-1">MCU</font> to target. This is used to create a C preprocessor symbol based upon the <font SIZE="-1">MCU</font> name, converted to upper case and pre- and post- fixed with <tt>&quot;__&quot;</tt>. This in turn will be used by the <tt>&quot;msp430.h&quot;</tt> header file to select an <font SIZE="-1">MCU</font> specific supplimentary header file. </p>
<p> The option also sets the <font SIZE="-1">ISA</font> to use. If the <font SIZE="-1">MCU</font> name is one that is known to only support the 430 <font SIZE="-1">ISA</font> then that is selected, otherwise the 430X <font SIZE="-1">ISA</font> is selected. A generic <font SIZE="-1">MCU</font> name of <tt>&quot;msp430&quot;</tt> can also be used to select the 430 <font SIZE="-1">ISA. </font> Similarly the generic <tt>&quot;msp430x&quot;</tt> <font SIZE="-1">MCU</font> name will select the 430X <font SIZE="-1">ISA.</font> </p>
<p> In addition an <font SIZE="-1">MCU</font> specific linker script will be added to the linker command line. The script&#8217;s name is the name of the <font SIZE="-1">MCU</font> with <tt>&quot;.ld&quot;</tt> appended. Thus specifying <code>-mmcu=xxx</code> on the gcc command line will define the C preprocessor symbol <tt>&quot;__XXX__&quot;</tt> and cause the linker to search for a script called <i>xxx.ld</i>. </p>
<p> This option is also passed on to the assembler.</p>
<dt><code>-mcpu=</code></p>
<dd>Specifies the <font SIZE="-1">ISA</font> to use. Accepted values are <tt>&quot;msp430&quot;</tt>, <tt>&quot;msp430x&quot;</tt> and <tt>&quot;msp430xv2&quot;</tt>. This option is deprecated. The <code>-mmcu=</code> option should be used to select the <font SIZE="-1">ISA.</font></p>
<dt><code>-msim</code></p>
<dd>Link to the simulator runtime libraries and linker script. Overrides any scripts that would be selected by the <code>-mmcu=</code> option.</p>
<dt><code>-mlarge</code></p>
<dd>Use large-model addressing (20-bit pointers, 32-bit <tt>&quot;size_t&quot;</tt>).</p>
<dt><code>-msmall</code></p>
<dd>Use small-model addressing (16-bit pointers, 16-bit <tt>&quot;size_t&quot;</tt>).</p>
<dt><code>-mrelax</code></p>
<dd>This option is passed to the assembler and linker, and allows the linker to perform certain optimizations that cannot be done until the final link.</p>
<dt><code>mhwmult=</code></p>
<dd>Describes the type of hardware multiply supported by the target. Accepted values are <tt>&quot;none&quot;</tt> for no hardware multiply, <tt>&quot;16bit&quot;</tt> for the original 16-bit-only multiply supported by early MCUs. <tt>&quot;32bit&quot;</tt> for the 16/32-bit multiply supported by later MCUs and <tt>&quot;f5series&quot;</tt> for the 16/32-bit multiply supported by F5-series MCUs. A value of <tt>&quot;auto&quot;</tt> can also be given. This tells <font SIZE="-1">GCC</font> to deduce the hardware multiply support based upon the <font SIZE="-1">MCU</font> name provided by the <code>-mmcu</code> option. If no <code>-mmcu</code> option is specified then <tt>&quot;32bit&quot;</tt> hardware multiply support is assumed. <tt>&quot;auto&quot;</tt> is the default setting. </p>
<p> Hardware multiplies are normally performed by calling a library routine. This saves space in the generated code. When compiling at <tt>&quot;-O3&quot;</tt> or higher however the hardware multiplier is invoked inline. This makes for bigger, but faster code. </p>
<p> The hardware multiply routines disable interrupts whilst running and restore the previous interrupt state when they finish. This makes them safe to use inside interrupt handlers as well as in normal code.</p>
<dt><code>-minrt</code></p>
<dd>Enable the use of a minimum runtime environment &#8211; no static initializers or constructors. This is intended for memory-constrained devices. The compiler will include special symbols in some objects that tell the linker and runtime which code fragments are required.</dl>
<p> <i></i><font SIZE="-1"><i>NDS32</i></font><i> Options</i> </p>
<p> These options are defined for <font SIZE="-1">NDS32</font> implementations:</p>
<dl COMPACT>
<dt><code>-mbig-endian</code></p>
<dd>Generate code in big-endian mode.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code in little-endian mode.</p>
<dt><code>-mreduced-regs</code></p>
<dd>Use reduced-set registers for register allocation.</p>
<dt><code>-mfull-regs</code></p>
<dd>Use full-set registers for register allocation.</p>
<dt><code>-mcmov</code></p>
<dd>Generate conditional move instructions.</p>
<dt><code>-mno-cmov</code></p>
<dd>Do not generate conditional move instructions.</p>
<dt><code>-mperf-ext</code></p>
<dd>Generate performance extension instructions.</p>
<dt><code>-mno-perf-ext</code></p>
<dd>Do not generate performance extension instructions.</p>
<dt><code>-mv3push</code></p>
<dd>Generate v3 push25/pop25 instructions.</p>
<dt><code>-mno-v3push</code></p>
<dd>Do not generate v3 push25/pop25 instructions.</p>
<dt><code>-m16-bit</code></p>
<dd>Generate 16-bit instructions.</p>
<dt><code>-mno-16-bit</code></p>
<dd>Do not generate 16-bit instructions.</p>
<dt><code>-mgp-direct</code></p>
<dd>Generate <font SIZE="-1">GP</font> base instructions directly.</p>
<dt><code>-mno-gp-direct</code></p>
<dd>Do no generate <font SIZE="-1">GP</font> base instructions directly.</p>
<dt><code>-misr-vector-size=</code><i>num</i></p>
<dd>Specify the size of each interrupt vector, which must be 4 or 16.</p>
<dt><code>-mcache-block-size=</code><i>num</i></p>
<dd>Specify the size of each cache block, which must be a power of 2 between 4 and 512.</p>
<dt><code>-march=</code><i>arch</i></p>
<dd>Specify the name of the target architecture.</p>
<dt><code>-mforce-fp-as-gp</code></p>
<dd>Prevent <tt>$fp</tt> being allocated during register allocation so that compiler is able to force performing fp-as-gp optimization.</p>
<dt><code>-mforbid-fp-as-gp</code></p>
<dd>Forbid using <tt>$fp</tt> to access static and global variables. This option strictly forbids fp-as-gp optimization regardless of <code>-mforce-fp-as-gp</code>.</p>
<dt><code>-mex9</code></p>
<dd>Use special directives to guide linker doing ex9 optimization.</p>
<dt><code>-mctor-dtor</code></p>
<dd>Enable constructor/destructor feature.</p>
<dt><code>-mrelax</code></p>
<dd>Guide linker to relax instructions.</dl>
<p> <i>Nios </i><font SIZE="-1"><i>II</i></font><i> Options</i> </p>
<p> These are the options defined for the Altera Nios <font SIZE="-1">II</font> processor.</p>
<dl COMPACT>
<dt><code>-G</code> <i>num</i></p>
<dd>Put global and static objects less than or equal to <i>num</i> bytes into the small data or <font SIZE="-1">BSS</font> sections instead of the normal data or <font SIZE="-1">BSS</font> sections. The default value of <i>num</i> is 8.</p>
<dt><code>-mgpopt</code></p>
<dd>
<dt><code>-mno-gpopt</code></p>
<dd>Generate (do not generate) GP-relative accesses for objects in the small data or <font SIZE="-1">BSS</font> sections. The default is <code>-mgpopt</code> except when <code>-fpic</code> or <code>-fPIC</code> is specified to generate position-independent code. Note that the Nios <font SIZE="-1">II ABI</font> does not permit GP-relative accesses from shared libraries. </p>
<p> You may need to specify <code>-mno-gpopt</code> explicitly when building programs that include large amounts of small data, including large <font SIZE="-1">GOT</font> data sections. In this case, the 16-bit offset for GP-relative addressing may not be large enough to allow access to the entire small data section.</p>
<dt><code>-mel</code></p>
<dd>
<dt><code>-meb</code></p>
<dd>Generate little-endian (default) or big-endian (experimental) code, respectively.</p>
<dt><code>-mbypass-cache</code></p>
<dd>
<dt><code>-mno-bypass-cache</code></p>
<dd>Force all load and store instructions to always bypass cache by using I/O variants of the instructions. The default is not to bypass the cache.</p>
<dt><code>-mno-cache-volatile</code></p>
<dd>
<dt><code>-mcache-volatile</code></p>
<dd>Volatile memory access bypass the cache using the I/O variants of the load and store instructions. The default is not to bypass the cache.</p>
<dt><code>-mno-fast-sw-div</code></p>
<dd>
<dt><code>-mfast-sw-div</code></p>
<dd>Do not use table-based fast divide for small numbers. The default is to use the fast divide at <code>-O3</code> and above.</p>
<dt><code>-mno-hw-mul</code></p>
<dd>
<dt><code>-mhw-mul</code></p>
<dd>
<dt><code>-mno-hw-mulx</code></p>
<dd>
<dt><code>-mhw-mulx</code></p>
<dd>
<dt><code>-mno-hw-div</code></p>
<dd>
<dt><code>-mhw-div</code></p>
<dd>Enable or disable emitting <tt>&quot;mul&quot;</tt>, <tt>&quot;mulx&quot;</tt> and <tt>&quot;div&quot;</tt> family of instructions by the compiler. The default is to emit <tt>&quot;mul&quot;</tt> and not emit <tt>&quot;div&quot;</tt> and <tt>&quot;mulx&quot;</tt>.</p>
<dt><code>-mcustom-</code><i>insn</i><code>=</code><i>N</i></p>
<dd>
<dt><code>-mno-custom-</code><i>insn</i></p>
<dd>Each <code>-mcustom-</code><i>insn</i><code>=</code><i>N</i> option enables use of a custom instruction with encoding <i>N</i> when generating code that uses <i>insn</i>. For example, <tt>&quot;-mcustom-fadds=253&quot;</tt> generates custom instruction 253 for single-precision floating-point add operations instead of the default behavior of using a library call. </p>
<p> The following values of <i>insn</i> are supported. Except as otherwise noted, floating-point operations are expected to be implemented with normal <font SIZE="-1">IEEE 754</font> semantics and correspond directly to the C operators or the equivalent <font SIZE="-1">GCC</font> built-in functions. </p>
<p> Single-precision floating point:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>fadds</code>, <code>fsubs</code>, <code>fdivs</code>, <code>fmuls</code></p>
<dd>Binary arithmetic operations.</p>
<dt><code>fnegs</code></p>
<dd>Unary negation.</p>
<dt><code>fabss</code></p>
<dd>Unary absolute value.</p>
<dt><code>fcmpeqs</code>, <code>fcmpges</code>, <code>fcmpgts</code>, <code>fcmples</code>, <code>fcmplts</code>, <code>fcmpnes</code></p>
<dd>Comparison operations.</p>
<dt><code>fmins</code>, <code>fmaxs</code></p>
<dd>Floating-point minimum and maximum. These instructions are only generated if <code>-ffinite-math-only</code> is specified.</p>
<dt><code>fsqrts</code></p>
<dd>Unary square root operation.</p>
<dt><code>fcoss</code>, <code>fsins</code>, <code>ftans</code>, <code>fatans</code>, <code>fexps</code>, <code>flogs</code></p>
<dd>Floating-point trigonometric and exponential functions. These instructions are only generated if <code>-funsafe-math-optimizations</code> is also specified.</dl>
</dl>
<dl COMPACT>
<dd>Double-precision floating point:</p>
<dl COMPACT>
<dt><code>faddd</code>, <code>fsubd</code>, <code>fdivd</code>, <code>fmuld</code></p>
<dd>Binary arithmetic operations.</p>
<dt><code>fnegd</code></p>
<dd>Unary negation.</p>
<dt><code>fabsd</code></p>
<dd>Unary absolute value.</p>
<dt><code>fcmpeqd</code>, <code>fcmpged</code>, <code>fcmpgtd</code>, <code>fcmpled</code>, <code>fcmpltd</code>, <code>fcmpned</code></p>
<dd>Comparison operations.</p>
<dt><code>fmind</code>, <code>fmaxd</code></p>
<dd>Double-precision minimum and maximum. These instructions are only generated if <code>-ffinite-math-only</code> is specified.</p>
<dt><code>fsqrtd</code></p>
<dd>Unary square root operation.</p>
<dt><code>fcosd</code>, <code>fsind</code>, <code>ftand</code>, <code>fatand</code>, <code>fexpd</code>, <code>flogd</code></p>
<dd>Double-precision trigonometric and exponential functions. These instructions are only generated if <code>-funsafe-math-optimizations</code> is also specified.</dl>
</dl>
<dl COMPACT>
<dd>Conversions:</p>
<dl COMPACT>
<dt><code>fextsd</code></p>
<dd>Conversion from single precision to double precision.</p>
<dt><code>ftruncds</code></p>
<dd>Conversion from double precision to single precision.</p>
<dt><code>fixsi</code>, <code>fixsu</code>, <code>fixdi</code>, <code>fixdu</code></p>
<dd>Conversion from floating point to signed or unsigned integer types, with truncation towards zero.</p>
<dt><code>floatis</code>, <code>floatus</code>, <code>floatid</code>, <code>floatud</code></p>
<dd>Conversion from signed or unsigned integer types to floating-point types.</dl>
</dl>
<dl COMPACT>
<dd>In addition, all of the following transfer instructions for internal registers X and Y must be provided to use any of the double-precision floating-point instructions. Custom instructions taking two double-precision source operands expect the first operand in the 64-bit register X. The other operand (or only operand of a unary operation) is given to the custom arithmetic instruction with the least significant half in source register <i>src1</i> and the most significant half in <i>src2</i>. A custom instruction that returns a double-precision result returns the most significant 32 bits in the destination register and the other half in 32-bit register Y. <font SIZE="-1">GCC</font> automatically generates the necessary code sequences to write register X and/or read register Y when double-precision floating-point instructions are used.</p>
<dl COMPACT>
<dt><code>fwrx</code></p>
<dd>Write <i>src1</i> into the least significant half of X and <i>src2</i> into the most significant half of X.</p>
<dt><code>fwry</code></p>
<dd>Write <i>src1</i> into Y.</p>
<dt><code>frdxhi</code>, <code>frdxlo</code></p>
<dd>Read the most or least (respectively) significant half of X and store it in <i>dest</i>.</p>
<dt><code>frdy</code></p>
<dd>Read the value of Y and store it into <i>dest</i>.</dl>
</dl>
<dl COMPACT>
<dd>Note that you can gain more local control over generation of Nios <font SIZE="-1">II</font> custom instructions by using the <tt>&quot;target(&quot;custom-</tt>insn<tt>=</tt>N<tt>&quot;)&quot;</tt> and <tt>&quot;target(&quot;no-custom-</tt>insn<tt>&quot;)&quot;</tt> function attributes or pragmas.</dl>
<dt><code>-mcustom-fpu-cfg=</code><i>name</i></p>
<dd>This option enables a predefined, named set of custom instruction encodings (see <code>-mcustom-</code><i>insn</i> above). Currently, the following sets are defined: </p>
<p> <code>-mcustom-fpu-cfg=60-1</code> is equivalent to: <code>-mcustom-fmuls=252 -mcustom-fadds=253 -mcustom-fsubs=254 -fsingle-precision-constant</code> </p>
<p> <code>-mcustom-fpu-cfg=60-2</code> is equivalent to: <code>-mcustom-fmuls=252 -mcustom-fadds=253 -mcustom-fsubs=254 -mcustom-fdivs=255 -fsingle-precision-constant</code> </p>
<p> <code>-mcustom-fpu-cfg=72-3</code> is equivalent to: <code>-mcustom-floatus=243 -mcustom-fixsi=244 -mcustom-floatis=245 -mcustom-fcmpgts=246 -mcustom-fcmples=249 -mcustom-fcmpeqs=250 -mcustom-fcmpnes=251 -mcustom-fmuls=252 -mcustom-fadds=253 -mcustom-fsubs=254 -mcustom-fdivs=255 -fsingle-precision-constant</code> </p>
<p> Custom instruction assignments given by individual <code>-mcustom-</code><i>insn</i><code>=</code> options override those given by <code>-mcustom-fpu-cfg=</code>, regardless of the order of the options on the command line. </p>
<p> Note that you can gain more local control over selection of a <font SIZE="-1">FPU</font> configuration by using the <tt>&quot;target(&quot;custom-fpu-cfg=</tt>name<tt>&quot;)&quot;</tt> function attribute or pragma.</dl>
<p> These additional <code>-m</code> options are available for the Altera Nios <font SIZE="-1">II ELF </font>(bare-metal) target:</p>
<dl COMPACT>
<dt><code>-mhal</code></p>
<dd>Link with <font SIZE="-1">HAL BSP. </font> This suppresses linking with the GCC-provided C runtime startup and termination code, and is typically used in conjunction with <code>-msys-crt0=</code> to specify the location of the alternate startup code provided by the <font SIZE="-1">HAL BSP.</font></p>
<dt><code>-msmallc</code></p>
<dd>Link with a limited version of the C library, <code>-lsmallc</code>, rather than Newlib.</p>
<dt><code>-msys-crt0=</code><i>startfile</i></p>
<dd><i>startfile</i> is the file name of the startfile (crt0) to use when linking. This option is only useful in conjunction with <code>-mhal</code>.</p>
<dt><code>-msys-lib=</code><i>systemlib</i></p>
<dd><i>systemlib</i> is the library name of the library that provides low-level system calls required by the C library, e.g. <tt>&quot;read&quot;</tt> and <tt>&quot;write&quot;</tt>. This option is typically used to link with a library provided by a <font SIZE="-1">HAL BSP.</font></dl>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i> </p>
<p> These options are defined for the <font SIZE="-1">PDP-11:</font></p>
<dl COMPACT>
<dt><code>-mfpu</code></p>
<dd>Use hardware <font SIZE="-1">FPP</font> floating point. This is the default. (<font SIZE="-1">FIS</font> floating point on the <font SIZE="-1">PDP-11/40</font> is not supported.)</p>
<dt><code>-msoft-float</code></p>
<dd>Do not use hardware floating point.</p>
<dt><code>-mac0</code></p>
<dd>Return floating-point results in ac0 (fr0 in Unix assembler syntax).</p>
<dt><code>-mno-ac0</code></p>
<dd>Return floating-point results in memory. This is the default.</p>
<dt><code>-m40</code></p>
<dd>Generate code for a <font SIZE="-1">PDP-11/40.</font></p>
<dt><code>-m45</code></p>
<dd>Generate code for a <font SIZE="-1">PDP-11/45. </font> This is the default.</p>
<dt><code>-m10</code></p>
<dd>Generate code for a <font SIZE="-1">PDP-11/10.</font></p>
<dt><code>-mbcopy-builtin</code></p>
<dd>Use inline <tt>&quot;movmemhi&quot;</tt> patterns for copying memory. This is the default.</p>
<dt><code>-mbcopy</code></p>
<dd>Do not use inline <tt>&quot;movmemhi&quot;</tt> patterns for copying memory.</p>
<dt><code>-mint16</code></p>
<dd>
<dt><code>-mno-int32</code></p>
<dd>Use 16-bit <tt>&quot;int&quot;</tt>. This is the default.</p>
<dt><code>-mint32</code></p>
<dd>
<dt><code>-mno-int16</code></p>
<dd>Use 32-bit <tt>&quot;int&quot;</tt>.</p>
<dt><code>-mfloat64</code></p>
<dd>
<dt><code>-mno-float32</code></p>
<dd>Use 64-bit <tt>&quot;float&quot;</tt>. This is the default.</p>
<dt><code>-mfloat32</code></p>
<dd>
<dt><code>-mno-float64</code></p>
<dd>Use 32-bit <tt>&quot;float&quot;</tt>.</p>
<dt><code>-mabshi</code></p>
<dd>Use <tt>&quot;abshi2&quot;</tt> pattern. This is the default.</p>
<dt><code>-mno-abshi</code></p>
<dd>Do not use <tt>&quot;abshi2&quot;</tt> pattern.</p>
<dt><code>-mbranch-expensive</code></p>
<dd>Pretend that branches are expensive. This is for experimenting with code generation only.</p>
<dt><code>-mbranch-cheap</code></p>
<dd>Do not pretend that branches are expensive. This is the default.</p>
<dt><code>-munix-asm</code></p>
<dd>Use Unix assembler syntax. This is the default when configured for <code>pdp11-*-bsd</code>.</p>
<dt><code>-mdec-asm</code></p>
<dd>Use <font SIZE="-1">DEC</font> assembler syntax. This is the default when configured for any <font SIZE="-1">PDP-11</font> target other than <code>pdp11-*-bsd</code>.</dl>
<p> <i>picoChip Options</i> </p>
<p> These <code>-m</code> options are defined for picoChip implementations:</p>
<dl COMPACT>
<dt><code>-mae=</code><i>ae_type</i></p>
<dd>Set the instruction set, register set, and instruction scheduling parameters for array element type <i>ae_type</i>. Supported values for <i>ae_type</i> are <font SIZE="-1"><code>ANY</code></font>, <font SIZE="-1"><code>MUL</code></font>, and <font SIZE="-1"><code>MAC</code></font>. </p>
<p> <code>-mae=ANY</code> selects a completely generic <font SIZE="-1">AE</font> type. Code generated with this option runs on any of the other <font SIZE="-1">AE</font> types. The code is not as efficient as it would be if compiled for a specific <font SIZE="-1">AE</font> type, and some types of operation (e.g., multiplication) do not work properly on all types of <font SIZE="-1">AE.</font> </p>
<p> <code>-mae=MUL</code> selects a <font SIZE="-1">MUL AE</font> type. This is the most useful <font SIZE="-1">AE</font> type for compiled code, and is the default. </p>
<p> <code>-mae=MAC</code> selects a DSP-style <font SIZE="-1">MAC AE. </font> Code compiled with this option may suffer from poor performance of byte (char) manipulation, since the <font SIZE="-1">DSP AE</font> does not provide hardware support for byte load/stores.</p>
<dt><code>-msymbol-as-address</code></p>
<dd>Enable the compiler to directly use a symbol name as an address in a load/store instruction, without first loading it into a register. Typically, the use of this option generates larger programs, which run faster than when the option isn&#8217;t used. However, the results vary from program to program, so it is left as a user option, rather than being permanently enabled.</p>
<dt><code>-mno-inefficient-warnings</code></p>
<dd>Disables warnings about the generation of inefficient code. These warnings can be generated, for example, when compiling code that performs byte-level memory operations on the <font SIZE="-1">MAC AE</font> type. The <font SIZE="-1">MAC AE</font> has no hardware support for byte-level memory operations, so all byte load/stores must be synthesized from word load/store operations. This is inefficient and a warning is generated to indicate that you should rewrite the code to avoid byte operations, or to target an <font SIZE="-1">AE</font> type that has the necessary hardware support. This option disables these warnings.</dl>
<p> <i>PowerPC Options</i> </p>
<p> These are listed under </p>
<p> <i></i><font SIZE="-1"><i>RL78</i></font><i> Options</i></p>
<dl COMPACT>
<dt><code>-msim</code></p>
<dd>Links in additional target libraries to support operation within a simulator.</p>
<dt><code>-mmul=none</code></p>
<dd>
<dt><code>-mmul=g13</code></p>
<dd>
<dt><code>-mmul=rl78</code></p>
<dd>Specifies the type of hardware multiplication support to be used. The default is <tt>&quot;none&quot;</tt>, which uses software multiplication functions. The <tt>&quot;g13&quot;</tt> option is for the hardware multiply/divide peripheral only on the <font SIZE="-1">RL78/G13</font> targets. The <tt>&quot;rl78&quot;</tt> option is for the standard hardware multiplication defined in the <font SIZE="-1">RL78</font> software manual.</dl>
<p> <i></i><font SIZE="-1"><i>IBM RS/6000</i></font><i> and PowerPC Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">IBM RS/6000</font> and PowerPC:</p>
<dl COMPACT>
<dt><code>-mpowerpc-gpopt</code></p>
<dd>
<dt><code>-mno-powerpc-gpopt</code></p>
<dd>
<dt><code>-mpowerpc-gfxopt</code></p>
<dd>
<dt><code>-mno-powerpc-gfxopt</code></p>
<dd>
<dt><code>-mpowerpc64</code></p>
<dd>
<dt><code>-mno-powerpc64</code></p>
<dd>
<dt><code>-mmfcrf</code></p>
<dd>
<dt><code>-mno-mfcrf</code></p>
<dd>
<dt><code>-mpopcntb</code></p>
<dd>
<dt><code>-mno-popcntb</code></p>
<dd>
<dt><code>-mpopcntd</code></p>
<dd>
<dt><code>-mno-popcntd</code></p>
<dd>
<dt><code>-mfprnd</code></p>
<dd>
<dt><code>-mno-fprnd</code></p>
<dd>
<dt><code>-mcmpb</code></p>
<dd>
<dt><code>-mno-cmpb</code></p>
<dd>
<dt><code>-mmfpgpr</code></p>
<dd>
<dt><code>-mno-mfpgpr</code></p>
<dd>
<dt><code>-mhard-dfp</code></p>
<dd>
<dt><code>-mno-hard-dfp</code></p>
<dd>You use these options to specify which instructions are available on the processor you are using. The default value of these options is determined when configuring <font SIZE="-1">GCC. </font> Specifying the <code>-mcpu=</code><i>cpu_type</i> overrides the specification of these options. We recommend you use the <code>-mcpu=</code><i>cpu_type</i> option rather than the options listed above. </p>
<p> Specifying <code>-mpowerpc-gpopt</code> allows <font SIZE="-1">GCC</font> to use the optional PowerPC architecture instructions in the General Purpose group, including floating-point square root. Specifying <code>-mpowerpc-gfxopt</code> allows <font SIZE="-1">GCC</font> to use the optional PowerPC architecture instructions in the Graphics group, including floating-point select. </p>
<p> The <code>-mmfcrf</code> option allows <font SIZE="-1">GCC</font> to generate the move from condition register field instruction implemented on the <font SIZE="-1">POWER4</font> processor and other processors that support the PowerPC V2.01 architecture. The <code>-mpopcntb</code> option allows <font SIZE="-1">GCC</font> to generate the popcount and double-precision <font SIZE="-1">FP</font> reciprocal estimate instruction implemented on the <font SIZE="-1">POWER5</font> processor and other processors that support the PowerPC V2.02 architecture. The <code>-mpopcntd</code> option allows <font SIZE="-1">GCC</font> to generate the popcount instruction implemented on the <font SIZE="-1">POWER7</font> processor and other processors that support the PowerPC V2.06 architecture. The <code>-mfprnd</code> option allows <font SIZE="-1">GCC</font> to generate the <font SIZE="-1">FP</font> round to integer instructions implemented on the <font SIZE="-1">POWER5+</font> processor and other processors that support the PowerPC V2.03 architecture. The <code>-mcmpb</code> option allows <font SIZE="-1">GCC</font> to generate the compare bytes instruction implemented on the <font SIZE="-1">POWER6</font> processor and other processors that support the PowerPC V2.05 architecture. The <code>-mmfpgpr</code> option allows <font SIZE="-1">GCC</font> to generate the <font SIZE="-1">FP</font> move to/from general-purpose register instructions implemented on the <font SIZE="-1">POWER6X</font> processor and other processors that support the extended PowerPC V2.05 architecture. The <code>-mhard-dfp</code> option allows <font SIZE="-1">GCC</font> to generate the decimal floating-point instructions implemented on some <font SIZE="-1">POWER</font> processors. </p>
<p> The <code>-mpowerpc64</code> option allows <font SIZE="-1">GCC</font> to generate the additional 64-bit instructions that are found in the full PowerPC64 architecture and to treat GPRs as 64-bit, doubleword quantities. <font SIZE="-1">GCC</font> defaults to <code>-mno-powerpc64</code>.</p>
<dt><code>-mcpu=</code><i>cpu_type</i></p>
<dd>Set architecture type, register usage, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>401</code>, <code>403</code>, <code>405</code>, <code>405fp</code>, <code>440</code>, <code>440fp</code>, <code>464</code>, <code>464fp</code>, <code>476</code>, <code>476fp</code>, <code>505</code>, <code>601</code>, <code>602</code>, <code>603</code>, <code>603e</code>, <code>604</code>, <code>604e</code>, <code>620</code>, <code>630</code>, <code>740</code>, <code>7400</code>, <code>7450</code>, <code>750</code>, <code>801</code>, <code>821</code>, <code>823</code>, <code>860</code>, <code>970</code>, <code>8540</code>, <code>a2</code>, <code>e300c2</code>, <code>e300c3</code>, <code>e500mc</code>, <code>e500mc64</code>, <code>e5500</code>, <code>e6500</code>, <code>ec603e</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>titan</code>, <code>power3</code>, <code>power4</code>, <code>power5</code>, <code>power5+</code>, <code>power6</code>, <code>power6x</code>, <code>power7</code>, <code>power8</code>, <code>powerpc</code>, <code>powerpc64</code>, <code>powerpc64le</code>, and <code>rs64</code>. </p>
<p> <code>-mcpu=powerpc</code>, <code>-mcpu=powerpc64</code>, and <code>-mcpu=powerpc64le</code> specify pure 32-bit PowerPC (either endian), 64-bit big endian PowerPC and 64-bit little endian PowerPC architecture machine types, with an appropriate, generic processor model assumed for scheduling purposes. </p>
<p> The other options specify a specific processor. Code generated under those options runs best on that processor, and may not run at all on others. </p>
<p> The <code>-mcpu</code> options automatically enable or disable the following options: </p>
<p> <code>-maltivec -mfprnd -mhard-float -mmfcrf -mmultiple -mpopcntb -mpopcntd -mpowerpc64 -mpowerpc-gpopt -mpowerpc-gfxopt -msingle-float -mdouble-float -msimple-fpu -mstring -mmulhw -mdlmzb -mmfpgpr -mvsx -mcrypto -mdirect-move -mpower8-fusion -mpower8-vector -mquad-memory -mquad-memory-atomic</code> </p>
<p> The particular options set for any particular <font SIZE="-1">CPU</font> varies between compiler versions, depending on what setting seems to produce optimal code for that <font SIZE="-1">CPU</font>; it doesn&#8217;t necessarily reflect the actual hardware&#8217;s capabilities. If you wish to set an individual option to a particular value, you may specify it after the <code>-mcpu</code> option, like <code>-mcpu=970 -mno-altivec</code>. </p>
<p> On <font SIZE="-1">AIX,</font> the <code>-maltivec</code> and <code>-mpowerpc64</code> options are not enabled or disabled by the <code>-mcpu</code> option at present because <font SIZE="-1">AIX</font> does not have full support for these options. You may still enable or disable them individually if you&#8217;re sure it&#8217;ll work in your environment.</p>
<dt><code>-mtune=</code><i>cpu_type</i></p>
<dd>Set the instruction scheduling parameters for machine type <i>cpu_type</i>, but do not set the architecture type or register usage, as <code>-mcpu=</code><i>cpu_type</i> does. The same values for <i>cpu_type</i> are used for <code>-mtune</code> as for <code>-mcpu</code>. If both are specified, the code generated uses the architecture and registers set by <code>-mcpu</code>, but the scheduling parameters set by <code>-mtune</code>.</p>
<dt><code>-mcmodel=small</code></p>
<dd>Generate PowerPC64 code for the small model: The <font SIZE="-1">TOC</font> is limited to 64k.</p>
<dt><code>-mcmodel=medium</code></p>
<dd>Generate PowerPC64 code for the medium model: The <font SIZE="-1">TOC</font> and other static data may be up to a total of 4G in size.</p>
<dt><code>-mcmodel=large</code></p>
<dd>Generate PowerPC64 code for the large model: The <font SIZE="-1">TOC</font> may be up to 4G in size. Other data and code is only limited by the 64-bit address space.</p>
<dt><code>-maltivec</code></p>
<dd>
<dt><code>-mno-altivec</code></p>
<dd>Generate code that uses (does not use) AltiVec instructions, and also enable the use of built-in functions that allow more direct access to the AltiVec instruction set. You may also need to set <code>-mabi=altivec</code> to adjust the current <font SIZE="-1">ABI</font> with AltiVec <font SIZE="-1">ABI</font> enhancements. </p>
<p> When <code>-maltivec</code> is used, rather than <code>-maltivec=le</code> or <code>-maltivec=be</code>, the element order for Altivec intrinsics such as <tt>&quot;vec_splat&quot;</tt>, <tt>&quot;vec_extract&quot;</tt>, and <tt>&quot;vec_insert&quot;</tt> will match array element order corresponding to the endianness of the target. That is, element zero identifies the leftmost element in a vector register when targeting a big-endian platform, and identifies the rightmost element in a vector register when targeting a little-endian platform.</p>
<dt><code>-maltivec=be</code></p>
<dd>Generate Altivec instructions using big-endian element order, regardless of whether the target is big- or little-endian. This is the default when targeting a big-endian platform. </p>
<p> The element order is used to interpret element numbers in Altivec intrinsics such as <tt>&quot;vec_splat&quot;</tt>, <tt>&quot;vec_extract&quot;</tt>, and <tt>&quot;vec_insert&quot;</tt>. By default, these will match array element order corresponding to the endianness for the target.</p>
<dt><code>-maltivec=le</code></p>
<dd>Generate Altivec instructions using little-endian element order, regardless of whether the target is big- or little-endian. This is the default when targeting a little-endian platform. This option is currently ignored when targeting a big-endian platform. </p>
<p> The element order is used to interpret element numbers in Altivec intrinsics such as <tt>&quot;vec_splat&quot;</tt>, <tt>&quot;vec_extract&quot;</tt>, and <tt>&quot;vec_insert&quot;</tt>. By default, these will match array element order corresponding to the endianness for the target.</p>
<dt><code>-mvrsave</code></p>
<dd>
<dt><code>-mno-vrsave</code></p>
<dd>Generate <font SIZE="-1">VRSAVE</font> instructions when generating AltiVec code.</p>
<dt><code>-mgen-cell-microcode</code></p>
<dd>Generate Cell microcode instructions.</p>
<dt><code>-mwarn-cell-microcode</code></p>
<dd>Warn when a Cell microcode instruction is emitted. An example of a Cell microcode instruction is a variable shift.</p>
<dt><code>-msecure-plt</code></p>
<dd>Generate code that allows <code>ld</code> and <code>ld.so</code> to build executables and shared libraries with non-executable <tt>&quot;.plt&quot;</tt> and <tt>&quot;.got&quot;</tt> sections. This is a PowerPC 32-bit <font SIZE="-1">SYSV ABI</font> option.</p>
<dt><code>-mbss-plt</code></p>
<dd>Generate code that uses a <font SIZE="-1">BSS </font><tt>&quot;.plt&quot;</tt> section that <code>ld.so</code> fills in, and requires <tt>&quot;.plt&quot;</tt> and <tt>&quot;.got&quot;</tt> sections that are both writable and executable. This is a PowerPC 32-bit <font SIZE="-1">SYSV ABI</font> option.</p>
<dt><code>-misel</code></p>
<dd>
<dt><code>-mno-isel</code></p>
<dd>This switch enables or disables the generation of <font SIZE="-1">ISEL</font> instructions.</p>
<dt><code>-misel=</code><i>yes/no</i></p>
<dd>This switch has been deprecated. Use <code>-misel</code> and <code>-mno-isel</code> instead.</p>
<dt><code>-mspe</code></p>
<dd>
<dt><code>-mno-spe</code></p>
<dd>This switch enables or disables the generation of <font SIZE="-1">SPE</font> simd instructions.</p>
<dt><code>-mpaired</code></p>
<dd>
<dt><code>-mno-paired</code></p>
<dd>This switch enables or disables the generation of <font SIZE="-1">PAIRED</font> simd instructions.</p>
<dt><code>-mspe=</code><i>yes/no</i></p>
<dd>This option has been deprecated. Use <code>-mspe</code> and <code>-mno-spe</code> instead.</p>
<dt><code>-mvsx</code></p>
<dd>
<dt><code>-mno-vsx</code></p>
<dd>Generate code that uses (does not use) vector/scalar (<font SIZE="-1">VSX</font>) instructions, and also enable the use of built-in functions that allow more direct access to the <font SIZE="-1">VSX</font> instruction set.</p>
<dt><code>-mcrypto</code></p>
<dd>
<dt><code>-mno-crypto</code></p>
<dd>Enable the use (disable) of the built-in functions that allow direct access to the cryptographic instructions that were added in version 2.07 of the PowerPC <font SIZE="-1">ISA.</font></p>
<dt><code>-mdirect-move</code></p>
<dd>
<dt><code>-mno-direct-move</code></p>
<dd>Generate code that uses (does not use) the instructions to move data between the general purpose registers and the vector/scalar (<font SIZE="-1">VSX</font>) registers that were added in version 2.07 of the PowerPC <font SIZE="-1">ISA.</font></p>
<dt><code>-mpower8-fusion</code></p>
<dd>
<dt><code>-mno-power8-fusion</code></p>
<dd>Generate code that keeps (does not keeps) some integer operations adjacent so that the instructions can be fused together on power8 and later processors.</p>
<dt><code>-mpower8-vector</code></p>
<dd>
<dt><code>-mno-power8-vector</code></p>
<dd>Generate code that uses (does not use) the vector and scalar instructions that were added in version 2.07 of the PowerPC <font SIZE="-1">ISA. </font> Also enable the use of built-in functions that allow more direct access to the vector instructions.</p>
<dt><code>-mquad-memory</code></p>
<dd>
<dt><code>-mno-quad-memory</code></p>
<dd>Generate code that uses (does not use) the non-atomic quad word memory instructions. The <code>-mquad-memory</code> option requires use of 64-bit mode.</p>
<dt><code>-mquad-memory-atomic</code></p>
<dd>
<dt><code>-mno-quad-memory-atomic</code></p>
<dd>Generate code that uses (does not use) the atomic quad word memory instructions. The <code>-mquad-memory-atomic</code> option requires use of 64-bit mode.</p>
<dt><code>-mfloat-gprs=</code><i>yes/single/double/no</i></p>
<dd>
<dt><code>-mfloat-gprs</code></p>
<dd>This switch enables or disables the generation of floating-point operations on the general-purpose registers for architectures that support it. </p>
<p> The argument <i>yes</i> or <i>single</i> enables the use of single-precision floating-point operations. </p>
<p> The argument <i>double</i> enables the use of single and double-precision floating-point operations. </p>
<p> The argument <i>no</i> disables floating-point operations on the general-purpose registers. </p>
<p> This option is currently only available on the MPC854x.</p>
<dt><code>-m32</code></p>
<dd>
<dt><code>-m64</code></p>
<dd>Generate code for 32-bit or 64-bit environments of Darwin and <font SIZE="-1">SVR4</font> targets (including GNU/Linux). The 32-bit environment sets int, long and pointer to 32 bits and generates code that runs on any PowerPC variant. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits, and generates code for PowerPC64, as for <code>-mpowerpc64</code>.</p>
<dt><code>-mfull-toc</code></p>
<dd>
<dt><code>-mno-fp-in-toc</code></p>
<dd>
<dt><code>-mno-sum-in-toc</code></p>
<dd>
<dt><code>-mminimal-toc</code></p>
<dd>Modify generation of the <font SIZE="-1">TOC </font>(Table Of Contents), which is created for every executable file. The <code>-mfull-toc</code> option is selected by default. In that case, <font SIZE="-1">GCC</font> allocates at least one <font SIZE="-1">TOC</font> entry for each unique non-automatic variable reference in your program. <font SIZE="-1">GCC</font> also places floating-point constants in the <font SIZE="-1">TOC. </font> However, only 16,384 entries are available in the <font SIZE="-1">TOC.</font> </p>
<p> If you receive a linker error message that saying you have overflowed the available <font SIZE="-1">TOC</font> space, you can reduce the amount of <font SIZE="-1">TOC</font> space used with the <code>-mno-fp-in-toc</code> and <code>-mno-sum-in-toc</code> options. <code>-mno-fp-in-toc</code> prevents <font SIZE="-1">GCC</font> from putting floating-point constants in the <font SIZE="-1">TOC</font> and <code>-mno-sum-in-toc</code> forces <font SIZE="-1">GCC</font> to generate code to calculate the sum of an address and a constant at run time instead of putting that sum into the <font SIZE="-1">TOC. </font> You may specify one or both of these options. Each causes <font SIZE="-1">GCC</font> to produce very slightly slower and larger code at the expense of conserving <font SIZE="-1">TOC</font> space. </p>
<p> If you still run out of space in the <font SIZE="-1">TOC</font> even when you specify both of these options, specify <code>-mminimal-toc</code> instead. This option causes <font SIZE="-1">GCC</font> to make only one <font SIZE="-1">TOC</font> entry for every file. When you specify this option, <font SIZE="-1">GCC</font> produces code that is slower and larger but which uses extremely little <font SIZE="-1">TOC</font> space. You may wish to use this option only on files that contain less frequently-executed code.</p>
<dt><code>-maix64</code></p>
<dd>
<dt><code>-maix32</code></p>
<dd>Enable 64-bit <font SIZE="-1">AIX ABI</font> and calling convention: 64-bit pointers, 64-bit <tt>&quot;long&quot;</tt> type, and the infrastructure needed to support them. Specifying <code>-maix64</code> implies <code>-mpowerpc64</code>, while <code>-maix32</code> disables the 64-bit <font SIZE="-1">ABI</font> and implies <code>-mno-powerpc64</code>. <font SIZE="-1">GCC</font> defaults to <code>-maix32</code>.</p>
<dt><code>-mxl-compat</code></p>
<dd>
<dt><code>-mno-xl-compat</code></p>
<dd>Produce code that conforms more closely to <font SIZE="-1">IBM XL</font> compiler semantics when using AIX-compatible <font SIZE="-1">ABI. </font> Pass floating-point arguments to prototyped functions beyond the register save area (<font SIZE="-1">RSA</font>) on the stack in addition to argument FPRs. Do not assume that most significant double in 128-bit long double value is properly rounded when comparing values and converting to double. Use <font SIZE="-1">XL</font> symbol names for long double support routines. </p>
<p> The <font SIZE="-1">AIX</font> calling convention was extended but not initially documented to handle an obscure K&amp;R C case of calling a function that takes the address of its arguments with fewer arguments than declared. <font SIZE="-1">IBM XL</font> compilers access floating-point arguments that do not fit in the <font SIZE="-1">RSA</font> from the stack when a subroutine is compiled without optimization. Because always storing floating-point arguments on the stack is inefficient and rarely needed, this option is not enabled by default and only is necessary when calling subroutines compiled by <font SIZE="-1">IBM XL</font> compilers without optimization.</p>
<dt><code>-mpe</code></p>
<dd>Support <i></i><font SIZE="-1"><i>IBM RS/6000 SP</i></font><i></i> <i>Parallel Environment</i> (<font SIZE="-1">PE</font>). Link an application written to use message passing with special startup code to enable the application to run. The system must have <font SIZE="-1">PE</font> installed in the standard location (<i>/usr/lpp/ppe.poe/</i>), or the <i>specs</i> file must be overridden with the <code>-specs=</code> option to specify the appropriate directory location. The Parallel Environment does not support threads, so the <code>-mpe</code> option and the <code>-pthread</code> option are incompatible.</p>
<dt><code>-malign-natural</code></p>
<dd>
<dt><code>-malign-power</code></p>
<dd>On <font SIZE="-1">AIX,</font> 32-bit Darwin, and 64-bit PowerPC GNU/Linux, the option <code>-malign-natural</code> overrides the ABI-defined alignment of larger types, such as floating-point doubles, on their natural size-based boundary. The option <code>-malign-power</code> instructs <font SIZE="-1">GCC</font> to follow the ABI-specified alignment rules. <font SIZE="-1">GCC</font> defaults to the standard alignment defined in the <font SIZE="-1">ABI.</font> </p>
<p> On 64-bit Darwin, natural alignment is the default, and <code>-malign-power</code> is not supported.</p>
<dt><code>-msoft-float</code></p>
<dd>
<dt><code>-mhard-float</code></p>
<dd>Generate code that does not use (uses) the floating-point register set. Software floating-point emulation is provided if you use the <code>-msoft-float</code> option, and pass the option to <font SIZE="-1">GCC</font> when linking.</p>
<dt><code>-msingle-float</code></p>
<dd>
<dt><code>-mdouble-float</code></p>
<dd>Generate code for single- or double-precision floating-point operations. <code>-mdouble-float</code> implies <code>-msingle-float</code>.</p>
<dt><code>-msimple-fpu</code></p>
<dd>Do not generate <tt>&quot;sqrt&quot;</tt> and <tt>&quot;div&quot;</tt> instructions for hardware floating-point unit.</p>
<dt><code>-mfpu=</code><i>name</i></p>
<dd>Specify type of floating-point unit. Valid values for <i>name</i> are <code>sp_lite</code> (equivalent to <code>-msingle-float -msimple-fpu</code>), <code>dp_lite</code> (equivalent to <code>-mdouble-float -msimple-fpu</code>), <code>sp_full</code> (equivalent to <code>-msingle-float</code>), and <code>dp_full</code> (equivalent to <code>-mdouble-float</code>).</p>
<dt><code>-mxilinx-fpu</code></p>
<dd>Perform optimizations for the floating-point unit on Xilinx <font SIZE="-1">PPC 405/440.</font></p>
<dt><code>-mmultiple</code></p>
<dd>
<dt><code>-mno-multiple</code></p>
<dd>Generate code that uses (does not use) the load multiple word instructions and the store multiple word instructions. These instructions are generated by default on <font SIZE="-1">POWER</font> systems, and not generated on PowerPC systems. Do not use <code>-mmultiple</code> on little-endian PowerPC systems, since those instructions do not work when the processor is in little-endian mode. The exceptions are <font SIZE="-1">PPC740</font> and <font SIZE="-1">PPC750</font> which permit these instructions in little-endian mode.</p>
<dt><code>-mstring</code></p>
<dd>
<dt><code>-mno-string</code></p>
<dd>Generate code that uses (does not use) the load string instructions and the store string word instructions to save multiple registers and do small block moves. These instructions are generated by default on <font SIZE="-1">POWER</font> systems, and not generated on PowerPC systems. Do not use <code>-mstring</code> on little-endian PowerPC systems, since those instructions do not work when the processor is in little-endian mode. The exceptions are <font SIZE="-1">PPC740</font> and <font SIZE="-1">PPC750</font> which permit these instructions in little-endian mode.</p>
<dt><code>-mupdate</code></p>
<dd>
<dt><code>-mno-update</code></p>
<dd>Generate code that uses (does not use) the load or store instructions that update the base register to the address of the calculated memory location. These instructions are generated by default. If you use <code>-mno-update</code>, there is a small window between the time that the stack pointer is updated and the address of the previous frame is stored, which means code that walks the stack frame across interrupts or signals may get corrupted data.</p>
<dt><code>-mavoid-indexed-addresses</code></p>
<dd>
<dt><code>-mno-avoid-indexed-addresses</code></p>
<dd>Generate code that tries to avoid (not avoid) the use of indexed load or store instructions. These instructions can incur a performance penalty on Power6 processors in certain situations, such as when stepping through large arrays that cross a 16M boundary. This option is enabled by default when targeting Power6 and disabled otherwise.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Generate code that uses (does not use) the floating-point multiply and accumulate instructions. These instructions are generated by default if hardware floating point is used. The machine-dependent <code>-mfused-madd</code> option is now mapped to the machine-independent <code>-ffp-contract=fast</code> option, and <code>-mno-fused-madd</code> is mapped to <code>-ffp-contract=off</code>.</p>
<dt><code>-mmulhw</code></p>
<dd>
<dt><code>-mno-mulhw</code></p>
<dd>Generate code that uses (does not use) the half-word multiply and multiply-accumulate instructions on the <font SIZE="-1">IBM 405, 440, 464</font> and 476 processors. These instructions are generated by default when targeting those processors.</p>
<dt><code>-mdlmzb</code></p>
<dd>
<dt><code>-mno-dlmzb</code></p>
<dd>Generate code that uses (does not use) the string-search <code>dlmzb</code> instruction on the <font SIZE="-1">IBM 405, 440, 464</font> and 476 processors. This instruction is generated by default when targeting those processors.</p>
<dt><code>-mno-bit-align</code></p>
<dd>
<dt><code>-mbit-align</code></p>
<dd>On System V.4 and embedded PowerPC systems do not (do) force structures and unions that contain bit-fields to be aligned to the base type of the bit-field. </p>
<p> For example, by default a structure containing nothing but 8 <tt>&quot;unsigned&quot;</tt> bit-fields of length 1 is aligned to a 4-byte boundary and has a size of 4 bytes. By using <code>-mno-bit-align</code>, the structure is aligned to a 1-byte boundary and is 1 byte in size.</p>
<dt><code>-mno-strict-align</code></p>
<dd>
<dt><code>-mstrict-align</code></p>
<dd>On System V.4 and embedded PowerPC systems do not (do) assume that unaligned memory references are handled by the system.</p>
<dt><code>-mrelocatable</code></p>
<dd>
<dt><code>-mno-relocatable</code></p>
<dd>Generate code that allows (does not allow) a static executable to be relocated to a different address at run time. A simple embedded PowerPC system loader should relocate the entire contents of <tt>&quot;.got2&quot;</tt> and 4-byte locations listed in the <tt>&quot;.fixup&quot;</tt> section, a table of 32-bit addresses generated by this option. For this to work, all objects linked together must be compiled with <code>-mrelocatable</code> or <code>-mrelocatable-lib</code>. <code>-mrelocatable</code> code aligns the stack to an 8-byte boundary.</p>
<dt><code>-mrelocatable-lib</code></p>
<dd>
<dt><code>-mno-relocatable-lib</code></p>
<dd>Like <code>-mrelocatable</code>, <code>-mrelocatable-lib</code> generates a <tt>&quot;.fixup&quot;</tt> section to allow static executables to be relocated at run time, but <code>-mrelocatable-lib</code> does not use the smaller stack alignment of <code>-mrelocatable</code>. Objects compiled with <code>-mrelocatable-lib</code> may be linked with objects compiled with any combination of the <code>-mrelocatable</code> options.</p>
<dt><code>-mno-toc</code></p>
<dd>
<dt><code>-mtoc</code></p>
<dd>On System V.4 and embedded PowerPC systems do not (do) assume that register 2 contains a pointer to a global area pointing to the addresses used in the program.</p>
<dt><code>-mlittle</code></p>
<dd>
<dt><code>-mlittle-endian</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the processor in little-endian mode. The <code>-mlittle-endian</code> option is the same as <code>-mlittle</code>.</p>
<dt><code>-mbig</code></p>
<dd>
<dt><code>-mbig-endian</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the processor in big-endian mode. The <code>-mbig-endian</code> option is the same as <code>-mbig</code>.</p>
<dt><code>-mdynamic-no-pic</code></p>
<dd>On Darwin and Mac <font SIZE="-1">OS X</font> systems, compile code so that it is not relocatable, but that its external references are relocatable. The resulting code is suitable for applications, but not shared libraries.</p>
<dt><code>-msingle-pic-base</code></p>
<dd>Treat the register used for <font SIZE="-1">PIC</font> addressing as read-only, rather than loading it in the prologue for each function. The runtime system is responsible for initializing this register with an appropriate value before execution begins.</p>
<dt><code>-mprioritize-restricted-insns=</code><i>priority</i></p>
<dd>This option controls the priority that is assigned to dispatch-slot restricted instructions during the second scheduling pass. The argument <i>priority</i> takes the value <code>0</code>, <code>1</code>, or <code>2</code> to assign no, highest, or second-highest (respectively) priority to dispatch-slot restricted instructions.</p>
<dt><code>-msched-costly-dep=</code><i>dependence_type</i></p>
<dd>This option controls which dependences are considered costly by the target during instruction scheduling. The argument <i>dependence_type</i> takes one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>no</code></p>
<dd>No dependence is costly.</p>
<dt><code>all</code></p>
<dd>All dependences are costly.</p>
<dt><code>true_store_to_load</code></p>
<dd>A true dependence from store to load is costly.</p>
<dt><code>store_to_load</code></p>
<dd>Any dependence from store to load is costly.</p>
<dt><i>number</i></p>
<dd>Any dependence for which the latency is greater than or equal to <i>number</i> is costly.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-minsert-sched-nops=</code><i>scheme</i></p>
<dd>This option controls which <font SIZE="-1">NOP</font> insertion scheme is used during the second scheduling pass. The argument <i>scheme</i> takes one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>no</code></p>
<dd>Don&#8217;t insert NOPs.</p>
<dt><code>pad</code></p>
<dd>Pad with NOPs any dispatch group that has vacant issue slots, according to the scheduler&#8217;s grouping.</p>
<dt><code>regroup_exact</code></p>
<dd>Insert NOPs to force costly dependent insns into separate groups. Insert exactly as many NOPs as needed to force an insn to a new group, according to the estimated processor grouping.</p>
<dt><i>number</i></p>
<dd>Insert NOPs to force costly dependent insns into separate groups. Insert <i>number</i> NOPs to force an insn to a new group.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mcall-sysv</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code using calling conventions that adhere to the March 1995 draft of the System V Application Binary Interface, PowerPC processor supplement. This is the default unless you configured <font SIZE="-1">GCC</font> using <code>powerpc-*-eabiaix</code>.</p>
<dt><code>-mcall-sysv-eabi</code></p>
<dd>
<dt><code>-mcall-eabi</code></p>
<dd>Specify both <code>-mcall-sysv</code> and <code>-meabi</code> options.</p>
<dt><code>-mcall-sysv-noeabi</code></p>
<dd>Specify both <code>-mcall-sysv</code> and <code>-mno-eabi</code> options.</p>
<dt><code>-mcall-aixdesc</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the <font SIZE="-1">AIX</font> operating system.</p>
<dt><code>-mcall-linux</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the Linux-based <font SIZE="-1">GNU</font> system.</p>
<dt><code>-mcall-freebsd</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the FreeBSD operating system.</p>
<dt><code>-mcall-netbsd</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the NetBSD operating system.</p>
<dt><code>-mcall-openbsd</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the OpenBSD operating system.</p>
<dt><code>-maix-struct-return</code></p>
<dd>Return all structures in memory (as specified by the <font SIZE="-1">AIX ABI</font>).</p>
<dt><code>-msvr4-struct-return</code></p>
<dd>Return structures smaller than 8 bytes in registers (as specified by the <font SIZE="-1">SVR4 ABI</font>).</p>
<dt><code>-mabi=</code><i>abi-type</i></p>
<dd>Extend the current <font SIZE="-1">ABI</font> with a particular extension, or remove such extension. Valid values are <i>altivec</i>, <i>no-altivec</i>, <i>spe</i>, <i>no-spe</i>, <i>ibmlongdouble</i>, <i>ieeelongdouble</i>, <i>elfv1</i>, <i>elfv2</i>.</p>
<dt><code>-mabi=spe</code></p>
<dd>Extend the current <font SIZE="-1">ABI</font> with <font SIZE="-1">SPE ABI</font> extensions. This does not change the default <font SIZE="-1">ABI,</font> instead it adds the <font SIZE="-1">SPE ABI</font> extensions to the current <font SIZE="-1">ABI.</font></p>
<dt><code>-mabi=no-spe</code></p>
<dd>Disable Book-E <font SIZE="-1">SPE ABI</font> extensions for the current <font SIZE="-1">ABI.</font></p>
<dt><code>-mabi=ibmlongdouble</code></p>
<dd>Change the current <font SIZE="-1">ABI</font> to use <font SIZE="-1">IBM</font> extended-precision long double. This is a PowerPC 32-bit <font SIZE="-1">SYSV ABI</font> option.</p>
<dt><code>-mabi=ieeelongdouble</code></p>
<dd>Change the current <font SIZE="-1">ABI</font> to use <font SIZE="-1">IEEE</font> extended-precision long double. This is a PowerPC 32-bit Linux <font SIZE="-1">ABI</font> option.</p>
<dt><code>-mabi=elfv1</code></p>
<dd>Change the current <font SIZE="-1">ABI</font> to use the ELFv1 <font SIZE="-1">ABI.</font> This is the default <font SIZE="-1">ABI</font> for big-endian PowerPC 64-bit Linux. Overriding the default <font SIZE="-1">ABI</font> requires special system support and is likely to fail in spectacular ways.</p>
<dt><code>-mabi=elfv2</code></p>
<dd>Change the current <font SIZE="-1">ABI</font> to use the ELFv2 <font SIZE="-1">ABI.</font> This is the default <font SIZE="-1">ABI</font> for little-endian PowerPC 64-bit Linux. Overriding the default <font SIZE="-1">ABI</font> requires special system support and is likely to fail in spectacular ways.</p>
<dt><code>-mprototype</code></p>
<dd>
<dt><code>-mno-prototype</code></p>
<dd>On System V.4 and embedded PowerPC systems assume that all calls to variable argument functions are properly prototyped. Otherwise, the compiler must insert an instruction before every non-prototyped call to set or clear bit 6 of the condition code register (<i></i><font SIZE="-1"><i>CR</i></font><i></i>) to indicate whether floating-point values are passed in the floating-point registers in case the function takes variable arguments. With <code>-mprototype</code>, only calls to prototyped variable argument functions set or clear the bit.</p>
<dt><code>-msim</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>sim-crt0.o</i> and that the standard C libraries are <i>libsim.a</i> and <i>libc.a</i>. This is the default for <code>powerpc-*-eabisim</code> configurations.</p>
<dt><code>-mmvme</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libmvme.a</i> and <i>libc.a</i>.</p>
<dt><code>-mads</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libads.a</i> and <i>libc.a</i>.</p>
<dt><code>-myellowknife</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libyk.a</i> and <i>libc.a</i>.</p>
<dt><code>-mvxworks</code></p>
<dd>On System V.4 and embedded PowerPC systems, specify that you are compiling for a VxWorks system.</p>
<dt><code>-memb</code></p>
<dd>On embedded PowerPC systems, set the <i></i><font SIZE="-1"><i>PPC_EMB</i></font><i></i> bit in the <font SIZE="-1">ELF</font> flags header to indicate that <code>eabi</code> extended relocations are used.</p>
<dt><code>-meabi</code></p>
<dd>
<dt><code>-mno-eabi</code></p>
<dd>On System V.4 and embedded PowerPC systems do (do not) adhere to the Embedded Applications Binary Interface (<font SIZE="-1">EABI</font>), which is a set of modifications to the System V.4 specifications. Selecting <code>-meabi</code> means that the stack is aligned to an 8-byte boundary, a function <tt>&quot;__eabi&quot;</tt> is called from <tt>&quot;main&quot;</tt> to set up the <font SIZE="-1">EABI</font> environment, and the <code>-msdata</code> option can use both <tt>&quot;r2&quot;</tt> and <tt>&quot;r13&quot;</tt> to point to two separate small data areas. Selecting <code>-mno-eabi</code> means that the stack is aligned to a 16-byte boundary, no <font SIZE="-1">EABI</font> initialization function is called from <tt>&quot;main&quot;</tt>, and the <code>-msdata</code> option only uses <tt>&quot;r13&quot;</tt> to point to a single small data area. The <code>-meabi</code> option is on by default if you configured <font SIZE="-1">GCC</font> using one of the <code>powerpc*-*-eabi*</code> options.</p>
<dt><code>-msdata=eabi</code></p>
<dd>On System V.4 and embedded PowerPC systems, put small initialized <tt>&quot;const&quot;</tt> global and static data in the <code>.sdata2</code> section, which is pointed to by register <tt>&quot;r2&quot;</tt>. Put small initialized non-<tt>&quot;const&quot;</tt> global and static data in the <code>.sdata</code> section, which is pointed to by register <tt>&quot;r13&quot;</tt>. Put small uninitialized global and static data in the <code>.sbss</code> section, which is adjacent to the <code>.sdata</code> section. The <code>-msdata=eabi</code> option is incompatible with the <code>-mrelocatable</code> option. The <code>-msdata=eabi</code> option also sets the <code>-memb</code> option.</p>
<dt><code>-msdata=sysv</code></p>
<dd>On System V.4 and embedded PowerPC systems, put small global and static data in the <code>.sdata</code> section, which is pointed to by register <tt>&quot;r13&quot;</tt>. Put small uninitialized global and static data in the <code>.sbss</code> section, which is adjacent to the <code>.sdata</code> section. The <code>-msdata=sysv</code> option is incompatible with the <code>-mrelocatable</code> option.</p>
<dt><code>-msdata=default</code></p>
<dd>
<dt><code>-msdata</code></p>
<dd>On System V.4 and embedded PowerPC systems, if <code>-meabi</code> is used, compile code the same as <code>-msdata=eabi</code>, otherwise compile code the same as <code>-msdata=sysv</code>.</p>
<dt><code>-msdata=data</code></p>
<dd>On System V.4 and embedded PowerPC systems, put small global data in the <code>.sdata</code> section. Put small uninitialized global data in the <code>.sbss</code> section. Do not use register <tt>&quot;r13&quot;</tt> to address small data however. This is the default behavior unless other <code>-msdata</code> options are used.</p>
<dt><code>-msdata=none</code></p>
<dd>
<dt><code>-mno-sdata</code></p>
<dd>On embedded PowerPC systems, put all initialized global and static data in the <code>.data</code> section, and all uninitialized data in the <code>.bss</code> section.</p>
<dt><code>-mblock-move-inline-limit=</code><i>num</i></p>
<dd>Inline all block moves (such as calls to <tt>&quot;memcpy&quot;</tt> or structure copies) less than or equal to <i>num</i> bytes. The minimum value for <i>num</i> is 32 bytes on 32-bit targets and 64 bytes on 64-bit targets. The default value is target-specific.</p>
<dt><code>-G</code> <i>num</i></p>
<dd>On embedded PowerPC systems, put global and static items less than or equal to <i>num</i> bytes into the small data or <font SIZE="-1">BSS</font> sections instead of the normal data or <font SIZE="-1">BSS</font> section. By default, <i>num</i> is 8. The <code>-G</code> <i>num</i> switch is also passed to the linker. All modules should be compiled with the same <code>-G</code> <i>num</i> value.</p>
<dt><code>-mregnames</code></p>
<dd>
<dt><code>-mno-regnames</code></p>
<dd>On System V.4 and embedded PowerPC systems do (do not) emit register names in the assembly language output using symbolic forms.</p>
<dt><code>-mlongcall</code></p>
<dd>
<dt><code>-mno-longcall</code></p>
<dd>By default assume that all calls are far away so that a longer and more expensive calling sequence is required. This is required for calls farther than 32 megabytes (33,554,432 bytes) from the current location. A short call is generated if the compiler knows the call cannot be that far away. This setting can be overridden by the <tt>&quot;shortcall&quot;</tt> function attribute, or by <tt>&quot;#pragma longcall(0)&quot;</tt>. </p>
<p> Some linkers are capable of detecting out-of-range calls and generating glue code on the fly. On these systems, long calls are unnecessary and generate slower code. As of this writing, the <font SIZE="-1">AIX</font> linker can do this, as can the <font SIZE="-1">GNU</font> linker for PowerPC/64. It is planned to add this feature to the <font SIZE="-1">GNU</font> linker for 32-bit PowerPC systems as well. </p>
<p> On Darwin/PPC systems, <tt>&quot;#pragma longcall&quot;</tt> generates <tt>&quot;jbsr callee, L42&quot;</tt>, plus a <i>branch island</i> (glue code). The two target addresses represent the callee and the branch island. The Darwin/PPC linker prefers the first address and generates a <tt>&quot;bl callee&quot;</tt> if the <font SIZE="-1">PPC </font><tt>&quot;bl&quot;</tt> instruction reaches the callee directly; otherwise, the linker generates <tt>&quot;bl L42&quot;</tt> to call the branch island. The branch island is appended to the body of the calling function; it computes the full 32-bit address of the callee and jumps to it. </p>
<p> On Mach-O (Darwin) systems, this option directs the compiler emit to the glue for every direct call, and the Darwin linker decides whether to use or discard it. </p>
<p> In the future, <font SIZE="-1">GCC</font> may ignore all longcall specifications when the linker is known to generate glue.</p>
<dt><code>-mtls-markers</code></p>
<dd>
<dt><code>-mno-tls-markers</code></p>
<dd>Mark (do not mark) calls to <tt>&quot;__tls_get_addr&quot;</tt> with a relocation specifying the function argument. The relocation allows the linker to reliably associate function call with argument setup instructions for <font SIZE="-1">TLS</font> optimization, which in turn allows <font SIZE="-1">GCC</font> to better schedule the sequence.</p>
<dt><code>-pthread</code></p>
<dd>Adds support for multithreading with the <i>pthreads</i> library. This option sets flags for both the preprocessor and linker.</p>
<dt><code>-mrecip</code></p>
<dd>
<dt><code>-mno-recip</code></p>
<dd>This option enables use of the reciprocal estimate and reciprocal square root estimate instructions with additional Newton-Raphson steps to increase precision instead of doing a divide or square root and divide for floating-point arguments. You should use the <code>-ffast-math</code> option when using <code>-mrecip</code> (or at least <code>-funsafe-math-optimizations</code>, <code>-finite-math-only</code>, <code>-freciprocal-math</code> and <code>-fno-trapping-math</code>). Note that while the throughput of the sequence is generally higher than the throughput of the non-reciprocal instruction, the precision of the sequence can be decreased by up to 2 ulp (i.e. the inverse of 1.0 equals 0.99999994) for reciprocal square roots.</p>
<dt><code>-mrecip=</code><i>opt</i></p>
<dd>This option controls which reciprocal estimate instructions may be used. <i>opt</i> is a comma-separated list of options, which may be preceded by a <tt>&quot;!&quot;</tt> to invert the option: <tt>&quot;all&quot;</tt>: enable all estimate instructions, <tt>&quot;default&quot;</tt>: enable the default instructions, equivalent to <code>-mrecip</code>, <tt>&quot;none&quot;</tt>: disable all estimate instructions, equivalent to <code>-mno-recip</code>; <tt>&quot;div&quot;</tt>: enable the reciprocal approximation instructions for both single and double precision; <tt>&quot;divf&quot;</tt>: enable the single-precision reciprocal approximation instructions; <tt>&quot;divd&quot;</tt>: enable the double-precision reciprocal approximation instructions; <tt>&quot;rsqrt&quot;</tt>: enable the reciprocal square root approximation instructions for both single and double precision; <tt>&quot;rsqrtf&quot;</tt>: enable the single-precision reciprocal square root approximation instructions; <tt>&quot;rsqrtd&quot;</tt>: enable the double-precision reciprocal square root approximation instructions; </p>
<p> So, for example, <code>-mrecip=all,!rsqrtd</code> enables all of the reciprocal estimate instructions, except for the <tt>&quot;FRSQRTE&quot;</tt>, <tt>&quot;XSRSQRTEDP&quot;</tt>, and <tt>&quot;XVRSQRTEDP&quot;</tt> instructions which handle the double-precision reciprocal square root calculations.</p>
<dt><code>-mrecip-precision</code></p>
<dd>
<dt><code>-mno-recip-precision</code></p>
<dd>Assume (do not assume) that the reciprocal estimate instructions provide higher-precision estimates than is mandated by the PowerPC <font SIZE="-1">ABI. </font> Selecting <code>-mcpu=power6</code>, <code>-mcpu=power7</code> or <code>-mcpu=power8</code> automatically selects <code>-mrecip-precision</code>. The double-precision square root estimate instructions are not generated by default on low-precision machines, since they do not provide an estimate that converges after three steps.</p>
<dt><code>-mveclibabi=</code><i>type</i></p>
<dd>Specifies the <font SIZE="-1">ABI</font> type to use for vectorizing intrinsics using an external library. The only type supported at present is <tt>&quot;mass&quot;</tt>, which specifies to use <font SIZE="-1">IBM</font>&#8216;s Mathematical Acceleration Subsystem (<font SIZE="-1">MASS</font>) libraries for vectorizing intrinsics using external libraries. <font SIZE="-1">GCC</font> currently emits calls to <tt>&quot;acosd2&quot;</tt>, <tt>&quot;acosf4&quot;</tt>, <tt>&quot;acoshd2&quot;</tt>, <tt>&quot;acoshf4&quot;</tt>, <tt>&quot;asind2&quot;</tt>, <tt>&quot;asinf4&quot;</tt>, <tt>&quot;asinhd2&quot;</tt>, <tt>&quot;asinhf4&quot;</tt>, <tt>&quot;atan2d2&quot;</tt>, <tt>&quot;atan2f4&quot;</tt>, <tt>&quot;atand2&quot;</tt>, <tt>&quot;atanf4&quot;</tt>, <tt>&quot;atanhd2&quot;</tt>, <tt>&quot;atanhf4&quot;</tt>, <tt>&quot;cbrtd2&quot;</tt>, <tt>&quot;cbrtf4&quot;</tt>, <tt>&quot;cosd2&quot;</tt>, <tt>&quot;cosf4&quot;</tt>, <tt>&quot;coshd2&quot;</tt>, <tt>&quot;coshf4&quot;</tt>, <tt>&quot;erfcd2&quot;</tt>, <tt>&quot;erfcf4&quot;</tt>, <tt>&quot;erfd2&quot;</tt>, <tt>&quot;erff4&quot;</tt>, <tt>&quot;exp2d2&quot;</tt>, <tt>&quot;exp2f4&quot;</tt>, <tt>&quot;expd2&quot;</tt>, <tt>&quot;expf4&quot;</tt>, <tt>&quot;expm1d2&quot;</tt>, <tt>&quot;expm1f4&quot;</tt>, <tt>&quot;hypotd2&quot;</tt>, <tt>&quot;hypotf4&quot;</tt>, <tt>&quot;lgammad2&quot;</tt>, <tt>&quot;lgammaf4&quot;</tt>, <tt>&quot;log10d2&quot;</tt>, <tt>&quot;log10f4&quot;</tt>, <tt>&quot;log1pd2&quot;</tt>, <tt>&quot;log1pf4&quot;</tt>, <tt>&quot;log2d2&quot;</tt>, <tt>&quot;log2f4&quot;</tt>, <tt>&quot;logd2&quot;</tt>, <tt>&quot;logf4&quot;</tt>, <tt>&quot;powd2&quot;</tt>, <tt>&quot;powf4&quot;</tt>, <tt>&quot;sind2&quot;</tt>, <tt>&quot;sinf4&quot;</tt>, <tt>&quot;sinhd2&quot;</tt>, <tt>&quot;sinhf4&quot;</tt>, <tt>&quot;sqrtd2&quot;</tt>, <tt>&quot;sqrtf4&quot;</tt>, <tt>&quot;tand2&quot;</tt>, <tt>&quot;tanf4&quot;</tt>, <tt>&quot;tanhd2&quot;</tt>, and <tt>&quot;tanhf4&quot;</tt> when generating code for power7. Both <code>-ftree-vectorize</code> and <code>-funsafe-math-optimizations</code> must also be enabled. The <font SIZE="-1">MASS</font> libraries must be specified at link time.</p>
<dt><code>-mfriz</code></p>
<dd>
<dt><code>-mno-friz</code></p>
<dd>Generate (do not generate) the <tt>&quot;friz&quot;</tt> instruction when the <code>-funsafe-math-optimizations</code> option is used to optimize rounding of floating-point values to 64-bit integer and back to floating point. The <tt>&quot;friz&quot;</tt> instruction does not return the same value if the floating-point number is too large to fit in an integer.</p>
<dt><code>-mpointers-to-nested-functions</code></p>
<dd>
<dt><code>-mno-pointers-to-nested-functions</code></p>
<dd>Generate (do not generate) code to load up the static chain register (<i>r11</i>) when calling through a pointer on <font SIZE="-1">AIX</font> and 64-bit Linux systems where a function pointer points to a 3-word descriptor giving the function address, <font SIZE="-1">TOC</font> value to be loaded in register <i>r2</i>, and static chain value to be loaded in register <i>r11</i>. The <code>-mpointers-to-nested-functions</code> is on by default. You cannot call through pointers to nested functions or pointers to functions compiled in other languages that use the static chain if you use the <code>-mno-pointers-to-nested-functions</code>.</p>
<dt><code>-msave-toc-indirect</code></p>
<dd>
<dt><code>-mno-save-toc-indirect</code></p>
<dd>Generate (do not generate) code to save the <font SIZE="-1">TOC</font> value in the reserved stack location in the function prologue if the function calls through a pointer on <font SIZE="-1">AIX</font> and 64-bit Linux systems. If the <font SIZE="-1">TOC</font> value is not saved in the prologue, it is saved just before the call through the pointer. The <code>-mno-save-toc-indirect</code> option is the default.</p>
<dt><code>-mcompat-align-parm</code></p>
<dd>
<dt><code>-mno-compat-align-parm</code></p>
<dd>Generate (do not generate) code to pass structure parameters with a maximum alignment of 64 bits, for compatibility with older versions of <font SIZE="-1">GCC.</font> </p>
<p> Older versions of <font SIZE="-1">GCC </font>(prior to 4.9.0) incorrectly did not align a structure parameter on a 128-bit boundary when that structure contained a member requiring 128-bit alignment. This is corrected in more recent versions of <font SIZE="-1">GCC. </font> This option may be used to generate code that is compatible with functions compiled with older versions of <font SIZE="-1">GCC.</font> </p>
<p> The <code>-mno-compat-align-parm</code> option is the default.</dl>
<p> <i></i><font SIZE="-1"><i>RX</i></font><i> Options</i> </p>
<p> These command-line options are defined for <font SIZE="-1">RX</font> targets:</p>
<dl COMPACT>
<dt><code>-m64bit-doubles</code></p>
<dd>
<dt><code>-m32bit-doubles</code></p>
<dd>Make the <tt>&quot;double&quot;</tt> data type be 64 bits (<code>-m64bit-doubles</code>) or 32 bits (<code>-m32bit-doubles</code>) in size. The default is <code>-m32bit-doubles</code>. <i>Note</i> <font SIZE="-1">RX</font> floating-point hardware only works on 32-bit values, which is why the default is <code>-m32bit-doubles</code>.</p>
<dt><code>-fpu</code></p>
<dd>
<dt><code>-nofpu</code></p>
<dd>Enables (<code>-fpu</code>) or disables (<code>-nofpu</code>) the use of <font SIZE="-1">RX</font> floating-point hardware. The default is enabled for the <i></i><font SIZE="-1"><i>RX600</i></font><i></i> series and disabled for the <i></i><font SIZE="-1"><i>RX200</i></font><i></i> series. </p>
<p> Floating-point instructions are only generated for 32-bit floating-point values, however, so the <font SIZE="-1">FPU</font> hardware is not used for doubles if the <code>-m64bit-doubles</code> option is used. </p>
<p> <i>Note</i> If the <code>-fpu</code> option is enabled then <code>-funsafe-math-optimizations</code> is also enabled automatically. This is because the <font SIZE="-1">RX FPU</font> instructions are themselves unsafe.</p>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>Selects the type of <font SIZE="-1">RX CPU</font> to be targeted. Currently three types are supported, the generic <i></i><font SIZE="-1"><i>RX600</i></font><i></i> and <i></i><font SIZE="-1"><i>RX200</i></font><i></i> series hardware and the specific <i></i><font SIZE="-1"><i>RX610</i></font><i></i> <font SIZE="-1">CPU. </font> The default is <i></i><font SIZE="-1"><i>RX600</i></font><i></i>. </p>
<p> The only difference between <i></i><font SIZE="-1"><i>RX600</i></font><i></i> and <i></i><font SIZE="-1"><i>RX610</i></font><i></i> is that the <i></i><font SIZE="-1"><i>RX610</i></font><i></i> does not support the <tt>&quot;MVTIPL&quot;</tt> instruction. </p>
<p> The <i></i><font SIZE="-1"><i>RX200</i></font><i></i> series does not have a hardware floating-point unit and so <code>-nofpu</code> is enabled by default when this type is selected.</p>
<dt><code>-mbig-endian-data</code></p>
<dd>
<dt><code>-mlittle-endian-data</code></p>
<dd>Store data (but not code) in the big-endian format. The default is <code>-mlittle-endian-data</code>, i.e. to store data in the little-endian format.</p>
<dt><code>-msmall-data-limit=</code><i>N</i></p>
<dd>Specifies the maximum size in bytes of global and static variables which can be placed into the small data area. Using the small data area can lead to smaller and faster code, but the size of area is limited and it is up to the programmer to ensure that the area does not overflow. Also when the small data area is used one of the <font SIZE="-1">RX</font>&#8216;s registers (usually <tt>&quot;r13&quot;</tt>) is reserved for use pointing to this area, so it is no longer available for use by the compiler. This could result in slower and/or larger code if variables are pushed onto the stack instead of being held in this register. </p>
<p> Note, common variables (variables that have not been initialized) and constants are not placed into the small data area as they are assigned to other sections in the output executable. </p>
<p> The default value is zero, which disables this feature. Note, this feature is not enabled by default with higher optimization levels (<code>-O2</code> etc) because of the potentially detrimental effects of reserving a register. It is up to the programmer to experiment and discover whether this feature is of benefit to their program. See the description of the <code>-mpid</code> option for a description of how the actual register to hold the small data area pointer is chosen.</p>
<dt><code>-msim</code></p>
<dd>
<dt><code>-mno-sim</code></p>
<dd>Use the simulator runtime. The default is to use the libgloss board-specific runtime.</p>
<dt><code>-mas100-syntax</code></p>
<dd>
<dt><code>-mno-as100-syntax</code></p>
<dd>When generating assembler output use a syntax that is compatible with Renesas&#8217;s <font SIZE="-1">AS100</font> assembler. This syntax can also be handled by the <font SIZE="-1">GAS</font> assembler, but it has some restrictions so it is not generated by default.</p>
<dt><code>-mmax-constant-size=</code><i>N</i></p>
<dd>Specifies the maximum size, in bytes, of a constant that can be used as an operand in a <font SIZE="-1">RX</font> instruction. Although the <font SIZE="-1">RX</font> instruction set does allow constants of up to 4 bytes in length to be used in instructions, a longer value equates to a longer instruction. Thus in some circumstances it can be beneficial to restrict the size of constants that are used in instructions. Constants that are too big are instead placed into a constant pool and referenced via register indirection. </p>
<p> The value <i>N</i> can be between 0 and 4. A value of 0 (the default) or 4 means that constants of any size are allowed.</p>
<dt><code>-mrelax</code></p>
<dd>Enable linker relaxation. Linker relaxation is a process whereby the linker attempts to reduce the size of a program by finding shorter versions of various instructions. Disabled by default.</p>
<dt><code>-mint-register=</code><i>N</i></p>
<dd>Specify the number of registers to reserve for fast interrupt handler functions. The value <i>N</i> can be between 0 and 4. A value of 1 means that register <tt>&quot;r13&quot;</tt> is reserved for the exclusive use of fast interrupt handlers. A value of 2 reserves <tt>&quot;r13&quot;</tt> and <tt>&quot;r12&quot;</tt>. A value of 3 reserves <tt>&quot;r13&quot;</tt>, <tt>&quot;r12&quot;</tt> and <tt>&quot;r11&quot;</tt>, and a value of 4 reserves <tt>&quot;r13&quot;</tt> through <tt>&quot;r10&quot;</tt>. A value of 0, the default, does not reserve any registers.</p>
<dt><code>-msave-acc-in-interrupts</code></p>
<dd>Specifies that interrupt handler functions should preserve the accumulator register. This is only necessary if normal code might use the accumulator register, for example because it performs 64-bit multiplications. The default is to ignore the accumulator as this makes the interrupt handlers faster.</p>
<dt><code>-mpid</code></p>
<dd>
<dt><code>-mno-pid</code></p>
<dd>Enables the generation of position independent data. When enabled any access to constant data is done via an offset from a base address held in a register. This allows the location of constant data to be determined at run time without requiring the executable to be relocated, which is a benefit to embedded applications with tight memory constraints. Data that can be modified is not affected by this option. </p>
<p> Note, using this feature reserves a register, usually <tt>&quot;r13&quot;</tt>, for the constant data base address. This can result in slower and/or larger code, especially in complicated functions. </p>
<p> The actual register chosen to hold the constant data base address depends upon whether the <code>-msmall-data-limit</code> and/or the <code>-mint-register</code> command-line options are enabled. Starting with register <tt>&quot;r13&quot;</tt> and proceeding downwards, registers are allocated first to satisfy the requirements of <code>-mint-register</code>, then <code>-mpid</code> and finally <code>-msmall-data-limit</code>. Thus it is possible for the small data area register to be <tt>&quot;r8&quot;</tt> if both <code>-mint-register=4</code> and <code>-mpid</code> are specified on the command line. </p>
<p> By default this feature is not enabled. The default can be restored via the <code>-mno-pid</code> command-line option.</p>
<dt><code>-mno-warn-multiple-fast-interrupts</code></p>
<dd>
<dt><code>-mwarn-multiple-fast-interrupts</code></p>
<dd>Prevents <font SIZE="-1">GCC</font> from issuing a warning message if it finds more than one fast interrupt handler when it is compiling a file. The default is to issue a warning for each extra fast interrupt handler found, as the <font SIZE="-1">RX</font> only supports one such interrupt.</dl>
<p> <i>Note:</i> The generic <font SIZE="-1">GCC</font> command-line option <code>-ffixed-</code><i>reg</i> has special significance to the <font SIZE="-1">RX</font> port when used with the <tt>&quot;interrupt&quot;</tt> function attribute. This attribute indicates a function intended to process fast interrupts. <font SIZE="-1">GCC</font> ensures that it only uses the registers <tt>&quot;r10&quot;</tt>, <tt>&quot;r11&quot;</tt>, <tt>&quot;r12&quot;</tt> and/or <tt>&quot;r13&quot;</tt> and only provided that the normal use of the corresponding registers have been restricted via the <code>-ffixed-</code><i>reg</i> or <code>-mint-register</code> command-line options. </p>
<p> <i>S/390 and zSeries Options</i> </p>
<p> These are the <code>-m</code> options defined for the S/390 and zSeries architecture.</p>
<dl COMPACT>
<dt><code>-mhard-float</code></p>
<dd>
<dt><code>-msoft-float</code></p>
<dd>Use (do not use) the hardware floating-point instructions and registers for floating-point operations. When <code>-msoft-float</code> is specified, functions in <i>libgcc.a</i> are used to perform floating-point operations. When <code>-mhard-float</code> is specified, the compiler generates <font SIZE="-1">IEEE</font> floating-point instructions. This is the default.</p>
<dt><code>-mhard-dfp</code></p>
<dd>
<dt><code>-mno-hard-dfp</code></p>
<dd>Use (do not use) the hardware decimal-floating-point instructions for decimal-floating-point operations. When <code>-mno-hard-dfp</code> is specified, functions in <i>libgcc.a</i> are used to perform decimal-floating-point operations. When <code>-mhard-dfp</code> is specified, the compiler generates decimal-floating-point hardware instructions. This is the default for <code>-march=z9-ec</code> or higher.</p>
<dt><code>-mlong-double-64</code></p>
<dd>
<dt><code>-mlong-double-128</code></p>
<dd>These switches control the size of <tt>&quot;long double&quot;</tt> type. A size of 64 bits makes the <tt>&quot;long double&quot;</tt> type equivalent to the <tt>&quot;double&quot;</tt> type. This is the default.</p>
<dt><code>-mbackchain</code></p>
<dd>
<dt><code>-mno-backchain</code></p>
<dd>Store (do not store) the address of the caller&#8217;s frame as backchain pointer into the callee&#8217;s stack frame. A backchain may be needed to allow debugging using tools that do not understand <font SIZE="-1">DWARF 2</font> call frame information. When <code>-mno-packed-stack</code> is in effect, the backchain pointer is stored at the bottom of the stack frame; when <code>-mpacked-stack</code> is in effect, the backchain is placed into the topmost word of the 96/160 byte register save area. </p>
<p> In general, code compiled with <code>-mbackchain</code> is call-compatible with code compiled with <code>-mmo-backchain</code>; however, use of the backchain for debugging purposes usually requires that the whole binary is built with <code>-mbackchain</code>. Note that the combination of <code>-mbackchain</code>, <code>-mpacked-stack</code> and <code>-mhard-float</code> is not supported. In order to build a linux kernel use <code>-msoft-float</code>. </p>
<p> The default is to not maintain the backchain.</p>
<dt><code>-mpacked-stack</code></p>
<dd>
<dt><code>-mno-packed-stack</code></p>
<dd>Use (do not use) the packed stack layout. When <code>-mno-packed-stack</code> is specified, the compiler uses the all fields of the 96/160 byte register save area only for their default purpose; unused fields still take up stack space. When <code>-mpacked-stack</code> is specified, register save slots are densely packed at the top of the register save area; unused space is reused for other purposes, allowing for more efficient use of the available stack space. However, when <code>-mbackchain</code> is also in effect, the topmost word of the save area is always used to store the backchain, and the return address register is always saved two words below the backchain. </p>
<p> As long as the stack frame backchain is not used, code generated with <code>-mpacked-stack</code> is call-compatible with code generated with <code>-mno-packed-stack</code>. Note that some non-FSF releases of <font SIZE="-1">GCC 2.95</font> for S/390 or zSeries generated code that uses the stack frame backchain at run time, not just for debugging purposes. Such code is not call-compatible with code compiled with <code>-mpacked-stack</code>. Also, note that the combination of <code>-mbackchain</code>, <code>-mpacked-stack</code> and <code>-mhard-float</code> is not supported. In order to build a linux kernel use <code>-msoft-float</code>. </p>
<p> The default is to not use the packed stack layout.</p>
<dt><code>-msmall-exec</code></p>
<dd>
<dt><code>-mno-small-exec</code></p>
<dd>Generate (or do not generate) code using the <tt>&quot;bras&quot;</tt> instruction to do subroutine calls. This only works reliably if the total executable size does not exceed 64k. The default is to use the <tt>&quot;basr&quot;</tt> instruction instead, which does not have this limitation.</p>
<dt><code>-m64</code></p>
<dd>
<dt><code>-m31</code></p>
<dd>When <code>-m31</code> is specified, generate code compliant to the GNU/Linux for S/390 <font SIZE="-1">ABI. </font> When <code>-m64</code> is specified, generate code compliant to the GNU/Linux for zSeries <font SIZE="-1">ABI. </font> This allows <font SIZE="-1">GCC</font> in particular to generate 64-bit instructions. For the <code>s390</code> targets, the default is <code>-m31</code>, while the <code>s390x</code> targets default to <code>-m64</code>.</p>
<dt><code>-mzarch</code></p>
<dd>
<dt><code>-mesa</code></p>
<dd>When <code>-mzarch</code> is specified, generate code using the instructions available on z/Architecture. When <code>-mesa</code> is specified, generate code using the instructions available on <font SIZE="-1">ESA/390. </font> Note that <code>-mesa</code> is not possible with <code>-m64</code>. When generating code compliant to the GNU/Linux for S/390 <font SIZE="-1">ABI,</font> the default is <code>-mesa</code>. When generating code compliant to the GNU/Linux for zSeries <font SIZE="-1">ABI,</font> the default is <code>-mzarch</code>.</p>
<dt><code>-mmvcle</code></p>
<dd>
<dt><code>-mno-mvcle</code></p>
<dd>Generate (or do not generate) code using the <tt>&quot;mvcle&quot;</tt> instruction to perform block moves. When <code>-mno-mvcle</code> is specified, use a <tt>&quot;mvc&quot;</tt> loop instead. This is the default unless optimizing for size.</p>
<dt><code>-mdebug</code></p>
<dd>
<dt><code>-mno-debug</code></p>
<dd>Print (or do not print) additional debug information when compiling. The default is to not print debug information.</p>
<dt><code>-march=</code><i>cpu-type</i></p>
<dd>Generate code that runs on <i>cpu-type</i>, which is the name of a system representing a certain processor type. Possible values for <i>cpu-type</i> are <code>g5</code>, <code>g6</code>, <code>z900</code>, <code>z990</code>, <code>z9-109</code>, <code>z9-ec</code>, <code>z10</code>, <code>z196</code>, and <code>zEC12</code>. When generating code using the instructions available on z/Architecture, the default is <code>-march=z900</code>. Otherwise, the default is <code>-march=g5</code>.</p>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Tune to <i>cpu-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The list of <i>cpu-type</i> values is the same as for <code>-march</code>. The default is the value used for <code>-march</code>.</p>
<dt><code>-mtpf-trace</code></p>
<dd>
<dt><code>-mno-tpf-trace</code></p>
<dd>Generate code that adds (does not add) in <font SIZE="-1">TPF OS</font> specific branches to trace routines in the operating system. This option is off by default, even when compiling for the <font SIZE="-1">TPF OS.</font></p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Generate code that uses (does not use) the floating-point multiply and accumulate instructions. These instructions are generated by default if hardware floating point is used.</p>
<dt><code>-mwarn-framesize=</code><i>framesize</i></p>
<dd>Emit a warning if the current function exceeds the given frame size. Because this is a compile-time check it doesn&#8217;t need to be a real problem when the program runs. It is intended to identify functions that most probably cause a stack overflow. It is useful to be used in an environment with limited stack size e.g. the linux kernel.</p>
<dt><code>-mwarn-dynamicstack</code></p>
<dd>Emit a warning if the function calls <tt>&quot;alloca&quot;</tt> or uses dynamically-sized arrays. This is generally a bad idea with a limited stack size.</p>
<dt><code>-mstack-guard=</code><i>stack-guard</i></p>
<dd>
<dt><code>-mstack-size=</code><i>stack-size</i></p>
<dd>If these options are provided the S/390 back end emits additional instructions in the function prologue that trigger a trap if the stack size is <i>stack-guard</i> bytes above the <i>stack-size</i> (remember that the stack on S/390 grows downward). If the <i>stack-guard</i> option is omitted the smallest power of 2 larger than the frame size of the compiled function is chosen. These options are intended to be used to help debugging stack overflow problems. The additionally emitted code causes only little overhead and hence can also be used in production-like systems without greater performance degradation. The given values have to be exact powers of 2 and <i>stack-size</i> has to be greater than <i>stack-guard</i> without exceeding 64k. In order to be efficient the extra code makes the assumption that the stack starts at an address aligned to the value given by <i>stack-size</i>. The <i>stack-guard</i> option can only be used in conjunction with <i>stack-size</i>.</p>
<dt><code>-mhotpatch=</code><i>pre-halfwords</i><code>,</code><i>post-halfwords</i></p>
<dd>If the hotpatch option is enabled, a &#8220;hot-patching&#8221; function prologue is generated for all functions in the compilation unit. The funtion label is prepended with the given number of two-byte <font SIZE="-1">NOP</font> instructions (<i>pre-halfwords</i>, maximum 1000000). After the label, 2 * <i>post-halfwords</i> bytes are appended, using the largest <font SIZE="-1">NOP</font> like instructions the architecture allows (maximum 1000000). </p>
<p> If both arguments are zero, hotpatching is disabled. </p>
<p> This option can be overridden for individual functions with the <tt>&quot;hotpatch&quot;</tt> attribute.</dl>
<p> <i>Score Options</i> </p>
<p> These options are defined for Score implementations:</p>
<dl COMPACT>
<dt><code>-meb</code></p>
<dd>Compile code for big-endian mode. This is the default.</p>
<dt><code>-mel</code></p>
<dd>Compile code for little-endian mode.</p>
<dt><code>-mnhwloop</code></p>
<dd>Disable generation of <tt>&quot;bcnz&quot;</tt> instructions.</p>
<dt><code>-muls</code></p>
<dd>Enable generation of unaligned load and store instructions.</p>
<dt><code>-mmac</code></p>
<dd>Enable the use of multiply-accumulate instructions. Disabled by default.</p>
<dt><code>-mscore5</code></p>
<dd>Specify the <font SIZE="-1">SCORE5</font> as the target architecture.</p>
<dt><code>-mscore5u</code></p>
<dd>Specify the <font SIZE="-1">SCORE5U</font> of the target architecture.</p>
<dt><code>-mscore7</code></p>
<dd>Specify the <font SIZE="-1">SCORE7</font> as the target architecture. This is the default.</p>
<dt><code>-mscore7d</code></p>
<dd>Specify the <font SIZE="-1">SCORE7D</font> as the target architecture.</dl>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">SH</font> implementations:</p>
<dl COMPACT>
<dt><code>-m1</code></p>
<dd>Generate code for the <font SIZE="-1">SH1.</font></p>
<dt><code>-m2</code></p>
<dd>Generate code for the <font SIZE="-1">SH2.</font></p>
<dt><code>-m2e</code></p>
<dd>Generate code for the SH2e.</p>
<dt><code>-m2a-nofpu</code></p>
<dd>Generate code for the SH2a without <font SIZE="-1">FPU,</font> or for a SH2a-FPU in such a way that the floating-point unit is not used.</p>
<dt><code>-m2a-single-only</code></p>
<dd>Generate code for the SH2a-FPU, in such a way that no double-precision floating-point operations are used.</p>
<dt><code>-m2a-single</code></p>
<dd>Generate code for the SH2a-FPU assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m2a</code></p>
<dd>Generate code for the SH2a-FPU assuming the floating-point unit is in double-precision mode by default.</p>
<dt><code>-m3</code></p>
<dd>Generate code for the <font SIZE="-1">SH3.</font></p>
<dt><code>-m3e</code></p>
<dd>Generate code for the SH3e.</p>
<dt><code>-m4-nofpu</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font> without a floating-point unit.</p>
<dt><code>-m4-single-only</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font> with a floating-point unit that only supports single-precision arithmetic.</p>
<dt><code>-m4-single</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font> assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m4</code></p>
<dd>Generate code for the <font SIZE="-1">SH4.</font></p>
<dt><code>-m4-100</code></p>
<dd>Generate code for <font SIZE="-1">SH4-100.</font></p>
<dt><code>-m4-100-nofpu</code></p>
<dd>Generate code for <font SIZE="-1">SH4-100</font> in such a way that the floating-point unit is not used.</p>
<dt><code>-m4-100-single</code></p>
<dd>Generate code for <font SIZE="-1">SH4-100</font> assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m4-100-single-only</code></p>
<dd>Generate code for <font SIZE="-1">SH4-100</font> in such a way that no double-precision floating-point operations are used.</p>
<dt><code>-m4-200</code></p>
<dd>Generate code for <font SIZE="-1">SH4-200.</font></p>
<dt><code>-m4-200-nofpu</code></p>
<dd>Generate code for <font SIZE="-1">SH4-200</font> without in such a way that the floating-point unit is not used.</p>
<dt><code>-m4-200-single</code></p>
<dd>Generate code for <font SIZE="-1">SH4-200</font> assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m4-200-single-only</code></p>
<dd>Generate code for <font SIZE="-1">SH4-200</font> in such a way that no double-precision floating-point operations are used.</p>
<dt><code>-m4-300</code></p>
<dd>Generate code for <font SIZE="-1">SH4-300.</font></p>
<dt><code>-m4-300-nofpu</code></p>
<dd>Generate code for <font SIZE="-1">SH4-300</font> without in such a way that the floating-point unit is not used.</p>
<dt><code>-m4-300-single</code></p>
<dd>Generate code for <font SIZE="-1">SH4-300</font> in such a way that no double-precision floating-point operations are used.</p>
<dt><code>-m4-300-single-only</code></p>
<dd>Generate code for <font SIZE="-1">SH4-300</font> in such a way that no double-precision floating-point operations are used.</p>
<dt><code>-m4-340</code></p>
<dd>Generate code for <font SIZE="-1">SH4-340 </font>(no <font SIZE="-1">MMU,</font> no <font SIZE="-1">FPU</font>).</p>
<dt><code>-m4-500</code></p>
<dd>Generate code for <font SIZE="-1">SH4-500 </font>(no <font SIZE="-1">FPU</font>). Passes <code>-isa=sh4-nofpu</code> to the assembler.</p>
<dt><code>-m4a-nofpu</code></p>
<dd>Generate code for the SH4al-dsp, or for a SH4a in such a way that the floating-point unit is not used.</p>
<dt><code>-m4a-single-only</code></p>
<dd>Generate code for the SH4a, in such a way that no double-precision floating-point operations are used.</p>
<dt><code>-m4a-single</code></p>
<dd>Generate code for the SH4a assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m4a</code></p>
<dd>Generate code for the SH4a.</p>
<dt><code>-m4al</code></p>
<dd>Same as <code>-m4a-nofpu</code>, except that it implicitly passes <code>-dsp</code> to the assembler. <font SIZE="-1">GCC</font> doesn&#8217;t generate any <font SIZE="-1">DSP</font> instructions at the moment.</p>
<dt><code>-m5-32media</code></p>
<dd>Generate 32-bit code for SHmedia.</p>
<dt><code>-m5-32media-nofpu</code></p>
<dd>Generate 32-bit code for SHmedia in such a way that the floating-point unit is not used.</p>
<dt><code>-m5-64media</code></p>
<dd>Generate 64-bit code for SHmedia.</p>
<dt><code>-m5-64media-nofpu</code></p>
<dd>Generate 64-bit code for SHmedia in such a way that the floating-point unit is not used.</p>
<dt><code>-m5-compact</code></p>
<dd>Generate code for SHcompact.</p>
<dt><code>-m5-compact-nofpu</code></p>
<dd>Generate code for SHcompact in such a way that the floating-point unit is not used.</p>
<dt><code>-mb</code></p>
<dd>Compile code for the processor in big-endian mode.</p>
<dt><code>-ml</code></p>
<dd>Compile code for the processor in little-endian mode.</p>
<dt><code>-mdalign</code></p>
<dd>Align doubles at 64-bit boundaries. Note that this changes the calling conventions, and thus some functions from the standard C library do not work unless you recompile it first with <code>-mdalign</code>.</p>
<dt><code>-mrelax</code></p>
<dd>Shorten some address references at link time, when possible; uses the linker option <code>-relax</code>.</p>
<dt><code>-mbigtable</code></p>
<dd>Use 32-bit offsets in <tt>&quot;switch&quot;</tt> tables. The default is to use 16-bit offsets.</p>
<dt><code>-mbitops</code></p>
<dd>Enable the use of bit manipulation instructions on <font SIZE="-1">SH2A.</font></p>
<dt><code>-mfmovd</code></p>
<dd>Enable the use of the instruction <tt>&quot;fmovd&quot;</tt>. Check <code>-mdalign</code> for alignment constraints.</p>
<dt><code>-mrenesas</code></p>
<dd>Comply with the calling conventions defined by Renesas.</p>
<dt><code>-mno-renesas</code></p>
<dd>Comply with the calling conventions defined for <font SIZE="-1">GCC</font> before the Renesas conventions were available. This option is the default for all targets of the <font SIZE="-1">SH</font> toolchain.</p>
<dt><code>-mnomacsave</code></p>
<dd>Mark the <tt>&quot;MAC&quot;</tt> register as call-clobbered, even if <code>-mrenesas</code> is given.</p>
<dt><code>-mieee</code></p>
<dd>
<dt><code>-mno-ieee</code></p>
<dd>Control the <font SIZE="-1">IEEE</font> compliance of floating-point comparisons, which affects the handling of cases where the result of a comparison is unordered. By default <code>-mieee</code> is implicitly enabled. If <code>-ffinite-math-only</code> is enabled <code>-mno-ieee</code> is implicitly set, which results in faster floating-point greater-equal and less-equal comparisons. The implcit settings can be overridden by specifying either <code>-mieee</code> or <code>-mno-ieee</code>.</p>
<dt><code>-minline-ic_invalidate</code></p>
<dd>Inline code to invalidate instruction cache entries after setting up nested function trampolines. This option has no effect if <code>-musermode</code> is in effect and the selected code generation option (e.g. <code>-m4</code>) does not allow the use of the <tt>&quot;icbi&quot;</tt> instruction. If the selected code generation option does not allow the use of the <tt>&quot;icbi&quot;</tt> instruction, and <code>-musermode</code> is not in effect, the inlined code manipulates the instruction cache address array directly with an associative write. This not only requires privileged mode at run time, but it also fails if the cache line had been mapped via the <font SIZE="-1">TLB</font> and has become unmapped.</p>
<dt><code>-misize</code></p>
<dd>Dump instruction size and location in the assembly code.</p>
<dt><code>-mpadstruct</code></p>
<dd>This option is deprecated. It pads structures to multiple of 4 bytes, which is incompatible with the <font SIZE="-1">SH ABI.</font></p>
<dt><code>-matomic-model=</code><i>model</i></p>
<dd>Sets the model of atomic operations and additional parameters as a comma separated list. For details on the atomic built-in functions see <code>__atomic Builtins</code>. The following models and parameters are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>none</code></p>
<dd>Disable compiler generated atomic sequences and emit library calls for atomic operations. This is the default if the target is not <tt>&quot;sh*-*-linux*&quot;</tt>.</p>
<dt><code>soft-gusa</code></p>
<dd>Generate GNU/Linux compatible gUSA software atomic sequences for the atomic built-in functions. The generated atomic sequences require additional support from the interrupt/exception handling code of the system and are only suitable for SH3* and SH4* single-core systems. This option is enabled by default when the target is <tt>&quot;sh*-*-linux*&quot;</tt> and SH3* or SH4*. When the target is <font SIZE="-1">SH4A,</font> this option will also partially utilize the hardware atomic instructions <tt>&quot;movli.l&quot;</tt> and <tt>&quot;movco.l&quot;</tt> to create more efficient code, unless <code>strict</code> is specified.</p>
<dt><code>soft-tcb</code></p>
<dd>Generate software atomic sequences that use a variable in the thread control block. This is a variation of the gUSA sequences which can also be used on SH1* and SH2* targets. The generated atomic sequences require additional support from the interrupt/exception handling code of the system and are only suitable for single-core systems. When using this model, the <code>gbr-offset=</code> parameter has to be specified as well.</p>
<dt><code>soft-imask</code></p>
<dd>Generate software atomic sequences that temporarily disable interrupts by setting <tt>&quot;SR.IMASK = 1111&quot;</tt>. This model works only when the program runs in privileged mode and is only suitable for single-core systems. Additional support from the interrupt/exception handling code of the system is not required. This model is enabled by default when the target is <tt>&quot;sh*-*-linux*&quot;</tt> and SH1* or SH2*.</p>
<dt><code>hard-llcs</code></p>
<dd>Generate hardware atomic sequences using the <tt>&quot;movli.l&quot;</tt> and <tt>&quot;movco.l&quot;</tt> instructions only. This is only available on <font SIZE="-1">SH4A</font> and is suitable for multi-core systems. Since the hardware instructions support only 32 bit atomic variables access to 8 or 16 bit variables is emulated with 32 bit accesses. Code compiled with this option will also be compatible with other software atomic model interrupt/exception handling systems if executed on an <font SIZE="-1">SH4A</font> system. Additional support from the interrupt/exception handling code of the system is not required for this model.</p>
<dt><code>gbr-offset=</code></p>
<dd>This parameter specifies the offset in bytes of the variable in the thread control block structure that should be used by the generated atomic sequences when the <code>soft-tcb</code> model has been selected. For other models this parameter is ignored. The specified value must be an integer multiple of four and in the range 0-1020.</p>
<dt><code>strict</code></p>
<dd>This parameter prevents mixed usage of multiple atomic models, even though they would be compatible, and will make the compiler generate atomic sequences of the specified model only.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mtas</code></p>
<dd>Generate the <tt>&quot;tas.b&quot;</tt> opcode for <tt>&quot;__atomic_test_and_set&quot;</tt>. Notice that depending on the particular hardware and software configuration this can degrade overall performance due to the operand cache line flushes that are implied by the <tt>&quot;tas.b&quot;</tt> instruction. On multi-core <font SIZE="-1">SH4A</font> processors the <tt>&quot;tas.b&quot;</tt> instruction must be used with caution since it can result in data corruption for certain cache configurations.</p>
<dt><code>-mprefergot</code></p>
<dd>When generating position-independent code, emit function calls using the Global Offset Table instead of the Procedure Linkage Table.</p>
<dt><code>-musermode</code></p>
<dd>
<dt><code>-mno-usermode</code></p>
<dd>Don&#8217;t allow (allow) the compiler generating privileged mode code. Specifying <code>-musermode</code> also implies <code>-mno-inline-ic_invalidate</code> if the inlined code would not work in user mode. <code>-musermode</code> is the default when the target is <tt>&quot;sh*-*-linux*&quot;</tt>. If the target is SH1* or SH2* <code>-musermode</code> has no effect, since there is no user mode.</p>
<dt><code>-multcost=</code><i>number</i></p>
<dd>Set the cost to assume for a multiply insn.</p>
<dt><code>-mdiv=</code><i>strategy</i></p>
<dd>Set the division strategy to be used for integer division operations. For SHmedia <i>strategy</i> can be one of:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>fp</code></p>
<dd>Performs the operation in floating point. This has a very high latency, but needs only a few instructions, so it might be a good choice if your code has enough easily-exploitable <font SIZE="-1">ILP</font> to allow the compiler to schedule the floating-point instructions together with other instructions. Division by zero causes a floating-point exception.</p>
<dt><code>inv</code></p>
<dd>Uses integer operations to calculate the inverse of the divisor, and then multiplies the dividend with the inverse. This strategy allows <font SIZE="-1">CSE</font> and hoisting of the inverse calculation. Division by zero calculates an unspecified result, but does not trap.</p>
<dt><code>inv:minlat</code></p>
<dd>A variant of <code>inv</code> where, if no <font SIZE="-1">CSE</font> or hoisting opportunities have been found, or if the entire operation has been hoisted to the same place, the last stages of the inverse calculation are intertwined with the final multiply to reduce the overall latency, at the expense of using a few more instructions, and thus offering fewer scheduling opportunities with other code.</p>
<dt><code>call</code></p>
<dd>Calls a library function that usually implements the <code>inv:minlat</code> strategy. This gives high code density for <tt>&quot;m5-*media-nofpu&quot;</tt> compilations.</p>
<dt><code>call2</code></p>
<dd>Uses a different entry point of the same library function, where it assumes that a pointer to a lookup table has already been set up, which exposes the pointer load to <font SIZE="-1">CSE</font> and code hoisting optimizations.</p>
<dt><code>inv:call</code></p>
<dd>
<dt><code>inv:call2</code></p>
<dd>
<dt><code>inv:fp</code></p>
<dd>Use the <code>inv</code> algorithm for initial code generation, but if the code stays unoptimized, revert to the <code>call</code>, <code>call2</code>, or <code>fp</code> strategies, respectively. Note that the potentially-trapping side effect of division by zero is carried by a separate instruction, so it is possible that all the integer instructions are hoisted out, but the marker for the side effect stays where it is. A recombination to floating-point operations or a call is not possible in that case.</p>
<dt><code>inv20u</code></p>
<dd>
<dt><code>inv20l</code></p>
<dd>Variants of the <code>inv:minlat</code> strategy. In the case that the inverse calculation is not separated from the multiply, they speed up division where the dividend fits into 20 bits (plus sign where applicable) by inserting a test to skip a number of operations in this case; this test slows down the case of larger dividends. <code>inv20u</code> assumes the case of a such a small dividend to be unlikely, and <code>inv20l</code> assumes it to be likely.</dl>
</dl>
<dl COMPACT>
<dd>For targets other than SHmedia <i>strategy</i> can be one of:</p>
<dl COMPACT>
<dt><code>call-div1</code></p>
<dd>Calls a library function that uses the single-step division instruction <tt>&quot;div1&quot;</tt> to perform the operation. Division by zero calculates an unspecified result and does not trap. This is the default except for <font SIZE="-1">SH4, SH2A</font> and SHcompact.</p>
<dt><code>call-fp</code></p>
<dd>Calls a library function that performs the operation in double precision floating point. Division by zero causes a floating-point exception. This is the default for SHcompact with <font SIZE="-1">FPU. </font> Specifying this for targets that do not have a double precision <font SIZE="-1">FPU</font> will default to <tt>&quot;call-div1&quot;</tt>.</p>
<dt><code>call-table</code></p>
<dd>Calls a library function that uses a lookup table for small divisors and the <tt>&quot;div1&quot;</tt> instruction with case distinction for larger divisors. Division by zero calculates an unspecified result and does not trap. This is the default for <font SIZE="-1">SH4. </font> Specifying this for targets that do not have dynamic shift instructions will default to <tt>&quot;call-div1&quot;</tt>.</dl>
</dl>
<dl COMPACT>
<dd>When a division strategy has not been specified the default strategy will be selected based on the current target. For <font SIZE="-1">SH2A</font> the default strategy is to use the <tt>&quot;divs&quot;</tt> and <tt>&quot;divu&quot;</tt> instructions instead of library function calls.</dl>
<dt><code>-maccumulate-outgoing-args</code></p>
<dd>Reserve space once for outgoing arguments in the function prologue rather than around each call. Generally beneficial for performance and size. Also needed for unwinding to avoid changing the stack frame around conditional code.</p>
<dt><code>-mdivsi3_libfunc=</code><i>name</i></p>
<dd>Set the name of the library function used for 32-bit signed division to <i>name</i>. This only affects the name used in the <code>call</code> and <code>inv:call</code> division strategies, and the compiler still expects the same sets of input/output/clobbered registers as if this option were not present.</p>
<dt><code>-mfixed-range=</code><i>register-range</i></p>
<dd>Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator can not use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma.</p>
<dt><code>-mindexed-addressing</code></p>
<dd>Enable the use of the indexed addressing mode for SHmedia32/SHcompact. This is only safe if the hardware and/or <font SIZE="-1">OS</font> implement 32-bit wrap-around semantics for the indexed addressing mode. The architecture allows the implementation of processors with 64-bit <font SIZE="-1">MMU,</font> which the <font SIZE="-1">OS</font> could use to get 32-bit addressing, but since no current hardware implementation supports this or any other way to make the indexed addressing mode safe to use in the 32-bit <font SIZE="-1">ABI,</font> the default is <code>-mno-indexed-addressing</code>.</p>
<dt><code>-mgettrcost=</code><i>number</i></p>
<dd>Set the cost assumed for the <tt>&quot;gettr&quot;</tt> instruction to <i>number</i>. The default is 2 if <code>-mpt-fixed</code> is in effect, 100 otherwise.</p>
<dt><code>-mpt-fixed</code></p>
<dd>Assume <tt>&quot;pt*&quot;</tt> instructions won&#8217;t trap. This generally generates better-scheduled code, but is unsafe on current hardware. The current architecture definition says that <tt>&quot;ptabs&quot;</tt> and <tt>&quot;ptrel&quot;</tt> trap when the target anded with 3 is 3. This has the unintentional effect of making it unsafe to schedule these instructions before a branch, or hoist them out of a loop. For example, <tt>&quot;__do_global_ctors&quot;</tt>, a part of <i>libgcc</i> that runs constructors at program startup, calls functions in a list which is delimited by -1. With the <code>-mpt-fixed</code> option, the <tt>&quot;ptabs&quot;</tt> is done before testing against -1. That means that all the constructors run a bit more quickly, but when the loop comes to the end of the list, the program crashes because <tt>&quot;ptabs&quot;</tt> loads -1 into a target register. </p>
<p> Since this option is unsafe for any hardware implementing the current architecture specification, the default is <code>-mno-pt-fixed</code>. Unless specified explicitly with <code>-mgettrcost</code>, <code>-mno-pt-fixed</code> also implies <code>-mgettrcost=100</code>; this deters register allocation from using target registers for storing ordinary integers.</p>
<dt><code>-minvalid-symbols</code></p>
<dd>Assume symbols might be invalid. Ordinary function symbols generated by the compiler are always valid to load with <tt>&quot;movi&quot;</tt>/<tt>&quot;shori&quot;</tt>/<tt>&quot;ptabs&quot;</tt> or <tt>&quot;movi&quot;</tt>/<tt>&quot;shori&quot;</tt>/<tt>&quot;ptrel&quot;</tt>, but with assembler and/or linker tricks it is possible to generate symbols that cause <tt>&quot;ptabs&quot;</tt> or <tt>&quot;ptrel&quot;</tt> to trap. This option is only meaningful when <code>-mno-pt-fixed</code> is in effect. It prevents cross-basic-block <font SIZE="-1">CSE,</font> hoisting and most scheduling of symbol loads. The default is <code>-mno-invalid-symbols</code>.</p>
<dt><code>-mbranch-cost=</code><i>num</i></p>
<dd>Assume <i>num</i> to be the cost for a branch instruction. Higher numbers make the compiler try to generate more branch-free code if possible. If not specified the value is selected depending on the processor type that is being compiled for.</p>
<dt><code>-mzdcbranch</code></p>
<dd>
<dt><code>-mno-zdcbranch</code></p>
<dd>Assume (do not assume) that zero displacement conditional branch instructions <tt>&quot;bt&quot;</tt> and <tt>&quot;bf&quot;</tt> are fast. If <code>-mzdcbranch</code> is specified, the compiler will try to prefer zero displacement branch code sequences. This is enabled by default when generating code for <font SIZE="-1">SH4</font> and <font SIZE="-1">SH4A. </font> It can be explicitly disabled by specifying <code>-mno-zdcbranch</code>.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Generate code that uses (does not use) the floating-point multiply and accumulate instructions. These instructions are generated by default if hardware floating point is used. The machine-dependent <code>-mfused-madd</code> option is now mapped to the machine-independent <code>-ffp-contract=fast</code> option, and <code>-mno-fused-madd</code> is mapped to <code>-ffp-contract=off</code>.</p>
<dt><code>-mfsca</code></p>
<dd>
<dt><code>-mno-fsca</code></p>
<dd>Allow or disallow the compiler to emit the <tt>&quot;fsca&quot;</tt> instruction for sine and cosine approximations. The option <tt>&quot;-mfsca&quot;</tt> must be used in combination with <tt>&quot;-funsafe-math-optimizations&quot;</tt>. It is enabled by default when generating code for <font SIZE="-1">SH4A. </font> Using <tt>&quot;-mno-fsca&quot;</tt> disables sine and cosine approximations even if <tt>&quot;-funsafe-math-optimizations&quot;</tt> is in effect.</p>
<dt><code>-mfsrra</code></p>
<dd>
<dt><code>-mno-fsrra</code></p>
<dd>Allow or disallow the compiler to emit the <tt>&quot;fsrra&quot;</tt> instruction for reciprocal square root approximations. The option <tt>&quot;-mfsrra&quot;</tt> must be used in combination with <tt>&quot;-funsafe-math-optimizations&quot;</tt> and <tt>&quot;-ffinite-math-only&quot;</tt>. It is enabled by default when generating code for <font SIZE="-1">SH4A. </font> Using <tt>&quot;-mno-fsrra&quot;</tt> disables reciprocal square root approximations even if <tt>&quot;-funsafe-math-optimizations&quot;</tt> and <tt>&quot;-ffinite-math-only&quot;</tt> are in effect.</p>
<dt><code>-mpretend-cmove</code></p>
<dd>Prefer zero-displacement conditional branches for conditional move instruction patterns. This can result in faster code on the <font SIZE="-1">SH4</font> processor.</dl>
<p> <i>Solaris 2 Options</i> </p>
<p> These <code>-m</code> options are supported on Solaris 2:</p>
<dl COMPACT>
<dt><code>-mclear-hwcap</code></p>
<dd><code>-mclear-hwcap</code> tells the compiler to remove the hardware capabilities generated by the Solaris assembler. This is only necessary when object files use <font SIZE="-1">ISA</font> extensions not supported by the current machine, but check at runtime whether or not to use them.</p>
<dt><code>-mimpure-text</code></p>
<dd><code>-mimpure-text</code>, used in addition to <code>-shared</code>, tells the compiler to not pass <code>-z text</code> to the linker when linking a shared object. Using this option, you can link position-dependent code into a shared object. </p>
<p> <code>-mimpure-text</code> suppresses the &#8220;relocations remain against allocatable but non-writable sections&#8221; linker error message. However, the necessary relocations trigger copy-on-write, and the shared object is not actually shared across processes. Instead of using <code>-mimpure-text</code>, you should compile all source code with <code>-fpic</code> or <code>-fPIC</code>.</dl>
<p> These switches are supported in addition to the above on Solaris 2:</p>
<dl COMPACT>
<dt><code>-pthreads</code></p>
<dd>Add support for multithreading using the <font SIZE="-1">POSIX</font> threads library. This option sets flags for both the preprocessor and linker. This option does not affect the thread safety of object code produced by the compiler or that of libraries supplied with it.</p>
<dt><code>-pthread</code></p>
<dd>This is a synonym for <code>-pthreads</code>.</dl>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are supported on the <font SIZE="-1">SPARC:</font></p>
<dl COMPACT>
<dt><code>-mno-app-regs</code></p>
<dd>
<dt><code>-mapp-regs</code></p>
<dd>Specify <code>-mapp-regs</code> to generate output using the global registers 2 through 4, which the <font SIZE="-1">SPARC SVR4 ABI</font> reserves for applications. Like the global register 1, each global register 2 through 4 is then treated as an allocable register that is clobbered by function calls. This is the default. </p>
<p> To be fully <font SIZE="-1">SVR4</font> ABI-compliant at the cost of some performance loss, specify <code>-mno-app-regs</code>. You should compile libraries and system software with this option.</p>
<dt><code>-mflat</code></p>
<dd>
<dt><code>-mno-flat</code></p>
<dd>With <code>-mflat</code>, the compiler does not generate save/restore instructions and uses a &#8220;flat&#8221; or single register window model. This model is compatible with the regular register window model. The local registers and the input registers (0&#8211;5) are still treated as &#8220;call-saved&#8221; registers and are saved on the stack as needed. </p>
<p> With <code>-mno-flat</code> (the default), the compiler generates save/restore instructions (except for leaf functions). This is the normal operating mode.</p>
<dt><code>-mfpu</code></p>
<dd>
<dt><code>-mhard-float</code></p>
<dd>Generate output containing floating-point instructions. This is the default.</p>
<dt><code>-mno-fpu</code></p>
<dd>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">SPARC</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded targets <code>sparc-*-aout</code> and <code>sparclite-*-*</code> do provide software floating-point support. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC,</font> with <code>-msoft-float</code> in order for this to work.</p>
<dt><code>-mhard-quad-float</code></p>
<dd>Generate output containing quad-word (long double) floating-point instructions.</p>
<dt><code>-msoft-quad-float</code></p>
<dd>Generate output containing library calls for quad-word (long double) floating-point instructions. The functions called are those specified in the <font SIZE="-1">SPARC ABI. </font> This is the default. </p>
<p> As of this writing, there are no <font SIZE="-1">SPARC</font> implementations that have hardware support for the quad-word floating-point instructions. They all invoke a trap handler for one of these instructions, and then the trap handler emulates the effect of the instruction. Because of the trap handler overhead, this is much slower than calling the <font SIZE="-1">ABI</font> library routines. Thus the <code>-msoft-quad-float</code> option is the default.</p>
<dt><code>-mno-unaligned-doubles</code></p>
<dd>
<dt><code>-munaligned-doubles</code></p>
<dd>Assume that doubles have 8-byte alignment. This is the default. </p>
<p> With <code>-munaligned-doubles</code>, <font SIZE="-1">GCC</font> assumes that doubles have 8-byte alignment only if they are contained in another type, or if they have an absolute address. Otherwise, it assumes they have 4-byte alignment. Specifying this option avoids some rare compatibility problems with code generated by other compilers. It is not the default because it results in a performance loss, especially for floating-point code.</p>
<dt><code>-muser-mode</code></p>
<dd>
<dt><code>-mno-user-mode</code></p>
<dd>Do not generate code that can only run in supervisor mode. This is relevant only for the <tt>&quot;casa&quot;</tt> instruction emitted for the <font SIZE="-1">LEON3</font> processor. The default is <code>-mno-user-mode</code>.</p>
<dt><code>-mno-faster-structs</code></p>
<dd>
<dt><code>-mfaster-structs</code></p>
<dd>With <code>-mfaster-structs</code>, the compiler assumes that structures should have 8-byte alignment. This enables the use of pairs of <tt>&quot;ldd&quot;</tt> and <tt>&quot;std&quot;</tt> instructions for copies in structure assignment, in place of twice as many <tt>&quot;ld&quot;</tt> and <tt>&quot;st&quot;</tt> pairs. However, the use of this changed alignment directly violates the <font SIZE="-1">SPARC ABI. </font> Thus, it&#8217;s intended only for use on targets where the developer acknowledges that their resulting code is not directly in line with the rules of the <font SIZE="-1">ABI.</font></p>
<dt><code>-mcpu=</code><i>cpu_type</i></p>
<dd>Set the instruction set, register set, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>v7</code>, <code>cypress</code>, <code>v8</code>, <code>supersparc</code>, <code>hypersparc</code>, <code>leon</code>, <code>leon3</code>, <code>leon3v7</code>, <code>sparclite</code>, <code>f930</code>, <code>f934</code>, <code>sparclite86x</code>, <code>sparclet</code>, <code>tsc701</code>, <code>v9</code>, <code>ultrasparc</code>, <code>ultrasparc3</code>, <code>niagara</code>, <code>niagara2</code>, <code>niagara3</code> and <code>niagara4</code>. </p>
<p> Native Solaris and GNU/Linux toolchains also support the value <code>native</code>, which selects the best architecture option for the host processor. <code>-mcpu=native</code> has no effect if <font SIZE="-1">GCC</font> does not recognize the processor. </p>
<p> Default instruction scheduling parameters are used for values that select an architecture and not an implementation. These are <code>v7</code>, <code>v8</code>, <code>sparclite</code>, <code>sparclet</code>, <code>v9</code>. </p>
<p> Here is a list of each supported architecture and their supported implementations.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>v7</p>
<dd>cypress, leon3v7</p>
<dt>v8</p>
<dd>supersparc, hypersparc, leon, leon3</p>
<dt>sparclite</p>
<dd>f930, f934, sparclite86x</p>
<dt>sparclet</p>
<dd>tsc701</p>
<dt>v9</p>
<dd>ultrasparc, ultrasparc3, niagara, niagara2, niagara3, niagara4</dl>
</dl>
<dl COMPACT>
<dd>By default (unless configured otherwise), <font SIZE="-1">GCC</font> generates code for the V7 variant of the <font SIZE="-1">SPARC</font> architecture. With <code>-mcpu=cypress</code>, the compiler additionally optimizes it for the Cypress <font SIZE="-1">CY7C602</font> chip, as used in the SPARCStation/SPARCServer 3xx series. This is also appropriate for the older SPARCStation 1, 2, <font SIZE="-1">IPX</font> etc. </p>
<p> With <code>-mcpu=v8</code>, <font SIZE="-1">GCC</font> generates code for the V8 variant of the <font SIZE="-1">SPARC</font> architecture. The only difference from V7 code is that the compiler emits the integer multiply and integer divide instructions which exist in <font SIZE="-1">SPARC-V8</font> but not in <font SIZE="-1">SPARC-V7. </font> With <code>-mcpu=supersparc</code>, the compiler additionally optimizes it for the SuperSPARC chip, as used in the SPARCStation 10, 1000 and 2000 series. </p>
<p> With <code>-mcpu=sparclite</code>, <font SIZE="-1">GCC</font> generates code for the SPARClite variant of the <font SIZE="-1">SPARC</font> architecture. This adds the integer multiply, integer divide step and scan (<tt>&quot;ffs&quot;</tt>) instructions which exist in SPARClite but not in <font SIZE="-1">SPARC-V7.</font> With <code>-mcpu=f930</code>, the compiler additionally optimizes it for the Fujitsu <font SIZE="-1">MB86930</font> chip, which is the original SPARClite, with no <font SIZE="-1">FPU. </font> With <code>-mcpu=f934</code>, the compiler additionally optimizes it for the Fujitsu <font SIZE="-1">MB86934</font> chip, which is the more recent SPARClite with <font SIZE="-1">FPU.</font> </p>
<p> With <code>-mcpu=sparclet</code>, <font SIZE="-1">GCC</font> generates code for the SPARClet variant of the <font SIZE="-1">SPARC</font> architecture. This adds the integer multiply, multiply/accumulate, integer divide step and scan (<tt>&quot;ffs&quot;</tt>) instructions which exist in SPARClet but not in <font SIZE="-1">SPARC-V7. </font> With <code>-mcpu=tsc701</code>, the compiler additionally optimizes it for the <font SIZE="-1">TEMIC</font> SPARClet chip. </p>
<p> With <code>-mcpu=v9</code>, <font SIZE="-1">GCC</font> generates code for the V9 variant of the <font SIZE="-1">SPARC</font> architecture. This adds 64-bit integer and floating-point move instructions, 3 additional floating-point condition code registers and conditional move instructions. With <code>-mcpu=ultrasparc</code>, the compiler additionally optimizes it for the Sun UltraSPARC I/II/IIi chips. With <code>-mcpu=ultrasparc3</code>, the compiler additionally optimizes it for the Sun UltraSPARC III/III+/IIIi/IIIi+/IV/IV+ chips. With <code>-mcpu=niagara</code>, the compiler additionally optimizes it for Sun UltraSPARC T1 chips. With <code>-mcpu=niagara2</code>, the compiler additionally optimizes it for Sun UltraSPARC T2 chips. With <code>-mcpu=niagara3</code>, the compiler additionally optimizes it for Sun UltraSPARC T3 chips. With <code>-mcpu=niagara4</code>, the compiler additionally optimizes it for Sun UltraSPARC T4 chips.</dl>
<dt><code>-mtune=</code><i>cpu_type</i></p>
<dd>Set the instruction scheduling parameters for machine type <i>cpu_type</i>, but do not set the instruction set or register set that the option <code>-mcpu=</code><i>cpu_type</i> does. </p>
<p> The same values for <code>-mcpu=</code><i>cpu_type</i> can be used for <code>-mtune=</code><i>cpu_type</i>, but the only useful values are those that select a particular <font SIZE="-1">CPU</font> implementation. Those are <code>cypress</code>, <code>supersparc</code>, <code>hypersparc</code>, <code>leon</code>, <code>leon3</code>, <code>leon3v7</code>, <code>f930</code>, <code>f934</code>, <code>sparclite86x</code>, <code>tsc701</code>, <code>ultrasparc</code>, <code>ultrasparc3</code>, <code>niagara</code>, <code>niagara2</code>, <code>niagara3</code> and <code>niagara4</code>. With native Solaris and GNU/Linux toolchains, <code>native</code> can also be used.</p>
<dt><code>-mv8plus</code></p>
<dd>
<dt><code>-mno-v8plus</code></p>
<dd>With <code>-mv8plus</code>, <font SIZE="-1">GCC</font> generates code for the <font SIZE="-1">SPARC-V8+ ABI. </font> The difference from the V8 <font SIZE="-1">ABI</font> is that the global and out registers are considered 64 bits wide. This is enabled by default on Solaris in 32-bit mode for all <font SIZE="-1">SPARC-V9</font> processors.</p>
<dt><code>-mvis</code></p>
<dd>
<dt><code>-mno-vis</code></p>
<dd>With <code>-mvis</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of the UltraSPARC Visual Instruction Set extensions. The default is <code>-mno-vis</code>.</p>
<dt><code>-mvis2</code></p>
<dd>
<dt><code>-mno-vis2</code></p>
<dd>With <code>-mvis2</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of version 2.0 of the UltraSPARC Visual Instruction Set extensions. The default is <code>-mvis2</code> when targeting a cpu that supports such instructions, such as UltraSPARC-III and later. Setting <code>-mvis2</code> also sets <code>-mvis</code>.</p>
<dt><code>-mvis3</code></p>
<dd>
<dt><code>-mno-vis3</code></p>
<dd>With <code>-mvis3</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of version 3.0 of the UltraSPARC Visual Instruction Set extensions. The default is <code>-mvis3</code> when targeting a cpu that supports such instructions, such as niagara-3 and later. Setting <code>-mvis3</code> also sets <code>-mvis2</code> and <code>-mvis</code>.</p>
<dt><code>-mcbcond</code></p>
<dd>
<dt><code>-mno-cbcond</code></p>
<dd>With <code>-mcbcond</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of compare-and-branch instructions, as defined in the Sparc Architecture 2011. The default is <code>-mcbcond</code> when targeting a cpu that supports such instructions, such as niagara-4 and later.</p>
<dt><code>-mpopc</code></p>
<dd>
<dt><code>-mno-popc</code></p>
<dd>With <code>-mpopc</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of the UltraSPARC population count instruction. The default is <code>-mpopc</code> when targeting a cpu that supports such instructions, such as Niagara-2 and later.</p>
<dt><code>-mfmaf</code></p>
<dd>
<dt><code>-mno-fmaf</code></p>
<dd>With <code>-mfmaf</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of the UltraSPARC Fused Multiply-Add Floating-point extensions. The default is <code>-mfmaf</code> when targeting a cpu that supports such instructions, such as Niagara-3 and later.</p>
<dt><code>-mfix-at697f</code></p>
<dd>Enable the documented workaround for the single erratum of the Atmel <font SIZE="-1">AT697F</font> processor (which corresponds to erratum #13 of the <font SIZE="-1">AT697E</font> processor).</p>
<dt><code>-mfix-ut699</code></p>
<dd>Enable the documented workarounds for the floating-point errata and the data cache nullify errata of the <font SIZE="-1">UT699</font> processor.</dl>
<p> These <code>-m</code> options are supported in addition to the above on <font SIZE="-1">SPARC-V9</font> processors in 64-bit environments:</p>
<dl COMPACT>
<dt><code>-m32</code></p>
<dd>
<dt><code>-m64</code></p>
<dd>Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits.</p>
<dt><code>-mcmodel=</code><i>which</i></p>
<dd>Set the code model to one of</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>medlow</code></p>
<dd>The Medium/Low code model: 64-bit addresses, programs must be linked in the low 32 bits of memory. Programs can be statically or dynamically linked.</p>
<dt><code>medmid</code></p>
<dd>The Medium/Middle code model: 64-bit addresses, programs must be linked in the low 44 bits of memory, the text and data segments must be less than 2GB in size and the data segment must be located within 2GB of the text segment.</p>
<dt><code>medany</code></p>
<dd>The Medium/Anywhere code model: 64-bit addresses, programs may be linked anywhere in memory, the text and data segments must be less than 2GB in size and the data segment must be located within 2GB of the text segment.</p>
<dt><code>embmedany</code></p>
<dd>The Medium/Anywhere code model for embedded systems: 64-bit addresses, the text and data segments must be less than 2GB in size, both starting anywhere in memory (determined at link time). The global register <tt>%g4</tt> points to the base of the data segment. Programs are statically linked and <font SIZE="-1">PIC</font> is not supported.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-mmemory-model=</code><i>mem-model</i></p>
<dd>Set the memory model in force on the processor to one of</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>default</code></p>
<dd>The default memory model for the processor and operating system.</p>
<dt><code>rmo</code></p>
<dd>Relaxed Memory Order</p>
<dt><code>pso</code></p>
<dd>Partial Store Order</p>
<dt><code>tso</code></p>
<dd>Total Store Order</p>
<dt><code>sc</code></p>
<dd>Sequential Consistency</dl>
</dl>
<dl COMPACT>
<dd>These memory models are formally defined in Appendix D of the Sparc V9 architecture manual, as set in the processor&#8217;s <tt>&quot;PSTATE.MM&quot;</tt> field.</dl>
<dt><code>-mstack-bias</code></p>
<dd>
<dt><code>-mno-stack-bias</code></p>
<dd>With <code>-mstack-bias</code>, <font SIZE="-1">GCC</font> assumes that the stack pointer, and frame pointer if present, are offset by -2047 which must be added back when making stack frame references. This is the default in 64-bit mode. Otherwise, assume no such offset is present.</dl>
<p> <i></i><font SIZE="-1"><i>SPU</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are supported on the <font SIZE="-1">SPU:</font></p>
<dl COMPACT>
<dt><code>-mwarn-reloc</code></p>
<dd>
<dt><code>-merror-reloc</code></p>
<dd>The loader for <font SIZE="-1">SPU</font> does not handle dynamic relocations. By default, <font SIZE="-1">GCC</font> gives an error when it generates code that requires a dynamic relocation. <code>-mno-error-reloc</code> disables the error, <code>-mwarn-reloc</code> generates a warning instead.</p>
<dt><code>-msafe-dma</code></p>
<dd>
<dt><code>-munsafe-dma</code></p>
<dd>Instructions that initiate or test completion of <font SIZE="-1">DMA</font> must not be reordered with respect to loads and stores of the memory that is being accessed. With <code>-munsafe-dma</code> you must use the <tt>&quot;volatile&quot;</tt> keyword to protect memory accesses, but that can lead to inefficient code in places where the memory is known to not change. Rather than mark the memory as volatile, you can use <code>-msafe-dma</code> to tell the compiler to treat the <font SIZE="-1">DMA</font> instructions as potentially affecting all memory.</p>
<dt><code>-mbranch-hints</code></p>
<dd>By default, <font SIZE="-1">GCC</font> generates a branch hint instruction to avoid pipeline stalls for always-taken or probably-taken branches. A hint is not generated closer than 8 instructions away from its branch. There is little reason to disable them, except for debugging purposes, or to make an object a little bit smaller.</p>
<dt><code>-msmall-mem</code></p>
<dd>
<dt><code>-mlarge-mem</code></p>
<dd>By default, <font SIZE="-1">GCC</font> generates code assuming that addresses are never larger than 18 bits. With <code>-mlarge-mem</code> code is generated that assumes a full 32-bit address.</p>
<dt><code>-mstdmain</code></p>
<dd>By default, <font SIZE="-1">GCC</font> links against startup code that assumes the SPU-style main function interface (which has an unconventional parameter list). With <code>-mstdmain</code>, <font SIZE="-1">GCC</font> links your program against startup code that assumes a C99-style interface to <tt>&quot;main&quot;</tt>, including a local copy of <tt>&quot;argv&quot;</tt> strings.</p>
<dt><code>-mfixed-range=</code><i>register-range</i></p>
<dd>Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator cannot use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma.</p>
<dt><code>-mea32</code></p>
<dd>
<dt><code>-mea64</code></p>
<dd>Compile code assuming that pointers to the <font SIZE="-1">PPU</font> address space accessed via the <tt>&quot;__ea&quot;</tt> named address space qualifier are either 32 or 64 bits wide. The default is 32 bits. As this is an ABI-changing option, all object code in an executable must be compiled with the same setting.</p>
<dt><code>-maddress-space-conversion</code></p>
<dd>
<dt><code>-mno-address-space-conversion</code></p>
<dd>Allow/disallow treating the <tt>&quot;__ea&quot;</tt> address space as superset of the generic address space. This enables explicit type casts between <tt>&quot;__ea&quot;</tt> and generic pointer as well as implicit conversions of generic pointers to <tt>&quot;__ea&quot;</tt> pointers. The default is to allow address space pointer conversions.</p>
<dt><code>-mcache-size=</code><i>cache-size</i></p>
<dd>This option controls the version of libgcc that the compiler links to an executable and selects a software-managed cache for accessing variables in the <tt>&quot;__ea&quot;</tt> address space with a particular cache size. Possible options for <i>cache-size</i> are <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code> and <code>128</code>. The default cache size is 64KB.</p>
<dt><code>-matomic-updates</code></p>
<dd>
<dt><code>-mno-atomic-updates</code></p>
<dd>This option controls the version of libgcc that the compiler links to an executable and selects whether atomic updates to the software-managed cache of PPU-side variables are used. If you use atomic updates, changes to a <font SIZE="-1">PPU</font> variable from <font SIZE="-1">SPU</font> code using the <tt>&quot;__ea&quot;</tt> named address space qualifier do not interfere with changes to other <font SIZE="-1">PPU</font> variables residing in the same cache line from <font SIZE="-1">PPU</font> code. If you do not use atomic updates, such interference may occur; however, writing back cache lines is more efficient. The default behavior is to use atomic updates.</p>
<dt><code>-mdual-nops</code></p>
<dd>
<dt><code>-mdual-nops=</code><i>n</i></p>
<dd>By default, <font SIZE="-1">GCC</font> inserts nops to increase dual issue when it expects it to increase performance. <i>n</i> can be a value from 0 to 10. A smaller <i>n</i> inserts fewer nops. 10 is the default, 0 is the same as <code>-mno-dual-nops</code>. Disabled with <code>-Os</code>.</p>
<dt><code>-mhint-max-nops=</code><i>n</i></p>
<dd>Maximum number of nops to insert for a branch hint. A branch hint must be at least 8 instructions away from the branch it is affecting. <font SIZE="-1">GCC</font> inserts up to <i>n</i> nops to enforce this, otherwise it does not generate the branch hint.</p>
<dt><code>-mhint-max-distance=</code><i>n</i></p>
<dd>The encoding of the branch hint instruction limits the hint to be within 256 instructions of the branch it is affecting. By default, <font SIZE="-1">GCC</font> makes sure it is within 125.</p>
<dt><code>-msafe-hints</code></p>
<dd>Work around a hardware bug that causes the <font SIZE="-1">SPU</font> to stall indefinitely. By default, <font SIZE="-1">GCC</font> inserts the <tt>&quot;hbrp&quot;</tt> instruction to make sure this stall won&#8217;t happen.</dl>
<p> <i>Options for System V</i> </p>
<p> These additional options are available on System V Release 4 for compatibility with other compilers on those systems:</p>
<dl COMPACT>
<dt><code>-G</code></p>
<dd>Create a shared object. It is recommended that <code>-symbolic</code> or <code>-shared</code> be used instead.</p>
<dt><code>-Qy</code></p>
<dd>Identify the versions of each tool used by the compiler, in a <tt>&quot;.ident&quot;</tt> assembler directive in the output.</p>
<dt><code>-Qn</code></p>
<dd>Refrain from adding <tt>&quot;.ident&quot;</tt> directives to the output file (this is the default).</p>
<dt><code>-YP,</code><i>dirs</i></p>
<dd>Search the directories <i>dirs</i>, and no others, for libraries specified with <code>-l</code>.</p>
<dt><code>-Ym,</code><i>dir</i></p>
<dd>Look in the directory <i>dir</i> to find the M4 preprocessor. The assembler uses this option.</dl>
<p> <i>TILE-Gx Options</i> </p>
<p> These <code>-m</code> options are supported on the TILE-Gx:</p>
<dl COMPACT>
<dt><code>-mcmodel=small</code></p>
<dd>Generate code for the small model. The distance for direct calls is limited to 500M in either direction. PC-relative addresses are 32 bits. Absolute addresses support the full address range.</p>
<dt><code>-mcmodel=large</code></p>
<dd>Generate code for the large model. There is no limitation on call distance, pc-relative addresses, or absolute addresses.</p>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>Selects the type of <font SIZE="-1">CPU</font> to be targeted. Currently the only supported type is <code>tilegx</code>.</p>
<dt><code>-m32</code></p>
<dd>
<dt><code>-m64</code></p>
<dd>Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long, and pointer to 32 bits. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits.</p>
<dt><code>-mbig-endian</code></p>
<dd>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code in big/little endian mode, respectively.</dl>
<p> <i>TILEPro Options</i> </p>
<p> These <code>-m</code> options are supported on the TILEPro:</p>
<dl COMPACT>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>Selects the type of <font SIZE="-1">CPU</font> to be targeted. Currently the only supported type is <code>tilepro</code>.</p>
<dt><code>-m32</code></p>
<dd>Generate code for a 32-bit environment, which sets int, long, and pointer to 32 bits. This is the only supported behavior so the flag is essentially ignored.</dl>
<p> <i>V850 Options</i> </p>
<p> These <code>-m</code> options are defined for V850 implementations:</p>
<dl COMPACT>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Treat all calls as being far away (near). If calls are assumed to be far away, the compiler always loads the function&#8217;s address into a register, and calls indirect through the pointer.</p>
<dt><code>-mno-ep</code></p>
<dd>
<dt><code>-mep</code></p>
<dd>Do not optimize (do optimize) basic blocks that use the same index pointer 4 or more times to copy pointer into the <tt>&quot;ep&quot;</tt> register, and use the shorter <tt>&quot;sld&quot;</tt> and <tt>&quot;sst&quot;</tt> instructions. The <code>-mep</code> option is on by default if you optimize.</p>
<dt><code>-mno-prolog-function</code></p>
<dd>
<dt><code>-mprolog-function</code></p>
<dd>Do not use (do use) external functions to save and restore registers at the prologue and epilogue of a function. The external functions are slower, but use less code space if more than one function saves the same number of registers. The <code>-mprolog-function</code> option is on by default if you optimize.</p>
<dt><code>-mspace</code></p>
<dd>Try to make the code as small as possible. At present, this just turns on the <code>-mep</code> and <code>-mprolog-function</code> options.</p>
<dt><code>-mtda=</code><i>n</i></p>
<dd>Put static or global variables whose size is <i>n</i> bytes or less into the tiny data area that register <tt>&quot;ep&quot;</tt> points to. The tiny data area can hold up to 256 bytes in total (128 bytes for byte references).</p>
<dt><code>-msda=</code><i>n</i></p>
<dd>Put static or global variables whose size is <i>n</i> bytes or less into the small data area that register <tt>&quot;gp&quot;</tt> points to. The small data area can hold up to 64 kilobytes.</p>
<dt><code>-mzda=</code><i>n</i></p>
<dd>Put static or global variables whose size is <i>n</i> bytes or less into the first 32 kilobytes of memory.</p>
<dt><code>-mv850</code></p>
<dd>Specify that the target processor is the V850.</p>
<dt><code>-mv850e3v5</code></p>
<dd>Specify that the target processor is the V850E3V5. The preprocessor constant <code>__v850e3v5__</code> is defined if this option is used.</p>
<dt><code>-mv850e2v4</code></p>
<dd>Specify that the target processor is the V850E3V5. This is an alias for the <code>-mv850e3v5</code> option.</p>
<dt><code>-mv850e2v3</code></p>
<dd>Specify that the target processor is the V850E2V3. The preprocessor constant <code>__v850e2v3__</code> is defined if this option is used.</p>
<dt><code>-mv850e2</code></p>
<dd>Specify that the target processor is the V850E2. The preprocessor constant <code>__v850e2__</code> is defined if this option is used.</p>
<dt><code>-mv850e1</code></p>
<dd>Specify that the target processor is the V850E1. The preprocessor constants <code>__v850e1__</code> and <code>__v850e__</code> are defined if this option is used.</p>
<dt><code>-mv850es</code></p>
<dd>Specify that the target processor is the V850ES. This is an alias for the <code>-mv850e1</code> option.</p>
<dt><code>-mv850e</code></p>
<dd>Specify that the target processor is the V850E. The preprocessor constant <code>__v850e__</code> is defined if this option is used. </p>
<p> If neither <code>-mv850</code> nor <code>-mv850e</code> nor <code>-mv850e1</code> nor <code>-mv850e2</code> nor <code>-mv850e2v3</code> nor <code>-mv850e3v5</code> are defined then a default target processor is chosen and the relevant <code>__v850*__</code> preprocessor constant is defined. </p>
<p> The preprocessor constants <code>__v850</code> and <code>__v851__</code> are always defined, regardless of which processor variant is the target.</p>
<dt><code>-mdisable-callt</code></p>
<dd>
<dt><code>-mno-disable-callt</code></p>
<dd>This option suppresses generation of the <tt>&quot;CALLT&quot;</tt> instruction for the v850e, v850e1, v850e2, v850e2v3 and v850e3v5 flavors of the v850 architecture. </p>
<p> This option is enabled by default when the <font SIZE="-1">RH850 ABI</font> is in use (see <code>-mrh850-abi</code>), and disabled by default when the <font SIZE="-1">GCC ABI</font> is in use. If <tt>&quot;CALLT&quot;</tt> instructions are being generated then the C preprocessor symbol <tt>&quot;__V850_CALLT__&quot;</tt> will be defined.</p>
<dt><code>-mrelax</code></p>
<dd>
<dt><code>-mno-relax</code></p>
<dd>Pass on (or do not pass on) the <code>-mrelax</code> command line option to the assembler.</p>
<dt><code>-mlong-jumps</code></p>
<dd>
<dt><code>-mno-long-jumps</code></p>
<dd>Disable (or re-enable) the generation of PC-relative jump instructions.</p>
<dt><code>-msoft-float</code></p>
<dd>
<dt><code>-mhard-float</code></p>
<dd>Disable (or re-enable) the generation of hardware floating point instructions. This option is only significant when the target architecture is <code>V850E2V3</code> or higher. If hardware floating point instructions are being generated then the C preprocessor symbol <tt>&quot;__FPU_OK__&quot;</tt> will be defined, otherwise the symbol <tt>&quot;__NO_FPU__&quot;</tt> will be defined.</p>
<dt><code>-mloop</code></p>
<dd>Enables the use of the e3v5 <font SIZE="-1">LOOP</font> instruction. The use of this instruction is not enabled by default when the e3v5 architecture is selected because its use is still experimental.</p>
<dt><code>-mrh850-abi</code></p>
<dd>
<dt><code>-mghs</code></p>
<dd>Enables support for the <font SIZE="-1">RH850</font> version of the V850 <font SIZE="-1">ABI. </font> This is the default. With this version of the <font SIZE="-1">ABI</font> the following rules apply:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Integer sized structures and unions are returned via a memory pointer rather than a register.</p>
<dt>&bull;</p>
<dd>Large structures and unions (more than 8 bytes in size) are passed by value.</p>
<dt>&bull;</p>
<dd>Functions are aligned to 16-bit boundaries.</p>
<dt>&bull;</p>
<dd>The <code>-m8byte-align</code> command line option is supported.</p>
<dt>&bull;</p>
<dd>The <code>-mdisable-callt</code> command line option is enabled by default. The <code>-mno-disable-callt</code> command line option is not supported.</dl>
</dl>
<dl COMPACT>
<dd>When this version of the <font SIZE="-1">ABI</font> is enabled the C preprocessor symbol <tt>&quot;__V850_RH850_ABI__&quot;</tt> is defined.</dl>
<dt><code>-mgcc-abi</code></p>
<dd>Enables support for the old <font SIZE="-1">GCC</font> version of the V850 <font SIZE="-1">ABI. </font> With this version of the <font SIZE="-1">ABI</font> the following rules apply:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Integer sized structures and unions are returned in register <tt>&quot;r10&quot;</tt>.</p>
<dt>&bull;</p>
<dd>Large structures and unions (more than 8 bytes in size) are passed by reference.</p>
<dt>&bull;</p>
<dd>Functions are aligned to 32-bit boundaries, unless optimizing for size.</p>
<dt>&bull;</p>
<dd>The <code>-m8byte-align</code> command line option is not supported.</p>
<dt>&bull;</p>
<dd>The <code>-mdisable-callt</code> command line option is supported but not enabled by default.</dl>
</dl>
<dl COMPACT>
<dd>When this version of the <font SIZE="-1">ABI</font> is enabled the C preprocessor symbol <tt>&quot;__V850_GCC_ABI__&quot;</tt> is defined.</dl>
<dt><code>-m8byte-align</code></p>
<dd>
<dt><code>-mno-8byte-align</code></p>
<dd>Enables support for <tt>&quot;doubles&quot;</tt> and <tt>&quot;long long&quot;</tt> types to be aligned on 8-byte boundaries. The default is to restrict the alignment of all objects to at most 4-bytes. When <code>-m8byte-align</code> is in effect the C preprocessor symbol <tt>&quot;__V850_8BYTE_ALIGN__&quot;</tt> will be defined.</p>
<dt><code>-mbig-switch</code></p>
<dd>Generate code suitable for big switch tables. Use this option only if the assembler/linker complain about out of range branches within a switch table.</p>
<dt><code>-mapp-regs</code></p>
<dd>This option causes r2 and r5 to be used in the code generated by the compiler. This setting is the default.</p>
<dt><code>-mno-app-regs</code></p>
<dd>This option causes r2 and r5 to be treated as fixed registers.</dl>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">VAX:</font></p>
<dl COMPACT>
<dt><code>-munix</code></p>
<dd>Do not output certain jump instructions (<tt>&quot;aobleq&quot;</tt> and so on) that the Unix assembler for the <font SIZE="-1">VAX</font> cannot handle across long ranges.</p>
<dt><code>-mgnu</code></p>
<dd>Do output those jump instructions, on the assumption that the <font SIZE="-1">GNU</font> assembler is being used.</p>
<dt><code>-mg</code></p>
<dd>Output code for G-format floating-point numbers instead of D-format.</dl>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">VMS</font> implementations:</p>
<dl COMPACT>
<dt><code>-mvms-return-codes</code></p>
<dd>Return <font SIZE="-1">VMS</font> condition codes from <tt>&quot;main&quot;</tt>. The default is to return POSIX-style condition (e.g. error) codes.</p>
<dt><code>-mdebug-main=</code><i>prefix</i></p>
<dd>Flag the first routine whose name starts with <i>prefix</i> as the main routine for the debugger.</p>
<dt><code>-mmalloc64</code></p>
<dd>Default to 64-bit memory allocation routines.</p>
<dt><code>-mpointer-size=</code><i>size</i></p>
<dd>Set the default size of pointers. Possible options for <i>size</i> are <code>32</code> or <code>short</code> for 32 bit pointers, <code>64</code> or <code>long</code> for 64 bit pointers, and <code>no</code> for supporting only 32 bit pointers. The later option disables <tt>&quot;pragma pointer_size&quot;</tt>.</dl>
<p> <i>VxWorks Options</i> </p>
<p> The options in this section are defined for all VxWorks targets. Options specific to the target hardware are listed with the other options for that target.</p>
<dl COMPACT>
<dt><code>-mrtp</code></p>
<dd><font SIZE="-1">GCC</font> can generate code for both VxWorks kernels and real time processes (RTPs). This option switches from the former to the latter. It also defines the preprocessor macro <tt>&quot;__RTP__&quot;</tt>.</p>
<dt><code>-non-static</code></p>
<dd>Link an <font SIZE="-1">RTP</font> executable against shared libraries rather than static libraries. The options <code>-static</code> and <code>-shared</code> can also be used for RTPs; <code>-static</code> is the default.</p>
<dt><code>-Bstatic</code></p>
<dd>
<dt><code>-Bdynamic</code></p>
<dd>These options are passed down to the linker. They are defined for compatibility with Diab.</p>
<dt><code>-Xbind-lazy</code></p>
<dd>Enable lazy binding of function calls. This option is equivalent to <code>-Wl,-z,now</code> and is defined for compatibility with Diab.</p>
<dt><code>-Xbind-now</code></p>
<dd>Disable lazy binding of function calls. This option is the default and is defined for compatibility with Diab.</dl>
<p> <i>x86-64 Options</i> </p>
<p> These are listed under </p>
<p> <i>Xstormy16 Options</i> </p>
<p> These options are defined for Xstormy16:</p>
<dl COMPACT>
<dt><code>-msim</code></p>
<dd>Choose startup files and linker script suitable for the simulator.</dl>
<p> <i>Xtensa Options</i> </p>
<p> These options are supported for Xtensa targets:</p>
<dl COMPACT>
<dt><code>-mconst16</code></p>
<dd>
<dt><code>-mno-const16</code></p>
<dd>Enable or disable use of <tt>&quot;CONST16&quot;</tt> instructions for loading constant values. The <tt>&quot;CONST16&quot;</tt> instruction is currently not a standard option from Tensilica. When enabled, <tt>&quot;CONST16&quot;</tt> instructions are always used in place of the standard <tt>&quot;L32R&quot;</tt> instructions. The use of <tt>&quot;CONST16&quot;</tt> is enabled by default only if the <tt>&quot;L32R&quot;</tt> instruction is not available.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Enable or disable use of fused multiply/add and multiply/subtract instructions in the floating-point option. This has no effect if the floating-point option is not also enabled. Disabling fused multiply/add and multiply/subtract instructions forces the compiler to use separate instructions for the multiply and add/subtract operations. This may be desirable in some cases where strict <font SIZE="-1">IEEE</font> 754-compliant results are required: the fused multiply add/subtract instructions do not round the intermediate result, thereby producing results with <i>more</i> bits of precision than specified by the <font SIZE="-1">IEEE</font> standard. Disabling fused multiply add/subtract instructions also ensures that the program output is not sensitive to the compiler&#8217;s ability to combine multiply and add/subtract operations.</p>
<dt><code>-mserialize-volatile</code></p>
<dd>
<dt><code>-mno-serialize-volatile</code></p>
<dd>When this option is enabled, <font SIZE="-1">GCC</font> inserts <tt>&quot;MEMW&quot;</tt> instructions before <tt>&quot;volatile&quot;</tt> memory references to guarantee sequential consistency. The default is <code>-mserialize-volatile</code>. Use <code>-mno-serialize-volatile</code> to omit the <tt>&quot;MEMW&quot;</tt> instructions.</p>
<dt><code>-mforce-no-pic</code></p>
<dd>For targets, like GNU/Linux, where all user-mode Xtensa code must be position-independent code (<font SIZE="-1">PIC</font>), this option disables <font SIZE="-1">PIC</font> for compiling kernel code.</p>
<dt><code>-mtext-section-literals</code></p>
<dd>
<dt><code>-mno-text-section-literals</code></p>
<dd>Control the treatment of literal pools. The default is <code>-mno-text-section-literals</code>, which places literals in a separate section in the output file. This allows the literal pool to be placed in a data <font SIZE="-1">RAM/ROM,</font> and it also allows the linker to combine literal pools from separate object files to remove redundant literals and improve code size. With <code>-mtext-section-literals</code>, the literals are interspersed in the text section in order to keep them as close as possible to their references. This may be necessary for large assembly files.</p>
<dt><code>-mtarget-align</code></p>
<dd>
<dt><code>-mno-target-align</code></p>
<dd>When this option is enabled, <font SIZE="-1">GCC</font> instructs the assembler to automatically align instructions to reduce branch penalties at the expense of some code density. The assembler attempts to widen density instructions to align branch targets and the instructions following call instructions. If there are not enough preceding safe density instructions to align a target, no widening is performed. The default is <code>-mtarget-align</code>. These options do not affect the treatment of auto-aligned instructions like <tt>&quot;LOOP&quot;</tt>, which the assembler always aligns, either by widening density instructions or by inserting <font SIZE="-1">NOP</font> instructions.</p>
<dt><code>-mlongcalls</code></p>
<dd>
<dt><code>-mno-longcalls</code></p>
<dd>When this option is enabled, <font SIZE="-1">GCC</font> instructs the assembler to translate direct calls to indirect calls unless it can determine that the target of a direct call is in the range allowed by the call instruction. This translation typically occurs for calls to functions in other source files. Specifically, the assembler translates a direct <tt>&quot;CALL&quot;</tt> instruction into an <tt>&quot;L32R&quot;</tt> followed by a <tt>&quot;CALLX&quot;</tt> instruction. The default is <code>-mno-longcalls</code>. This option should be used in programs where the call target can potentially be out of range. This option is implemented in the assembler, not the compiler, so the assembly code generated by <font SIZE="-1">GCC</font> still shows direct call instructions&#8212;look at the disassembled object code to see the actual instructions. Note that the assembler uses an indirect call for every cross-file call, not just those that really are out of range.</dl>
<p> <i>zSeries Options</i> </p>
<p> These are listed under</p>
<h3>Options for Code Generation Conventions</h3>
<p>These machine-independent options control the interface conventions used in code generation. </p>
<p> Most of them have both positive and negative forms; the negative form of <code>-ffoo</code> is <code>-fno-foo</code>. In the table below, only one of the forms is listed&#8212;the one that is not the default. You can figure out the other form by either removing <code>no-</code> or adding it.</p>
<dl COMPACT>
<dt><code>-fbounds-check</code></p>
<dd>For front ends that support it, generate additional code to check that indices used to access arrays are within the declared range. This is currently only supported by the Java and Fortran front ends, where this option defaults to true and false respectively.</p>
<dt><code>-fstack-reuse=</code><i>reuse-level</i></p>
<dd>This option controls stack space reuse for user declared local/auto variables and compiler generated temporaries. <i>reuse_level</i> can be <code>all</code>, <code>named_vars</code>, or <code>none</code>. <code>all</code> enables stack reuse for all local variables and temporaries, <code>named_vars</code> enables the reuse only for user defined local variables with names, and <code>none</code> disables stack reuse completely. The default value is <code>all</code>. The option is needed when the program extends the lifetime of a scoped local variable or a compiler generated temporary beyond the end point defined by the language. When a lifetime of a variable ends, and if the variable lives in memory, the optimizing compiler has the freedom to reuse its stack space with other temporaries or scoped local variables whose live range does not overlap with it. Legacy code extending local lifetime will likely to break with the stack reuse optimization. </p>
<p> For example, </p>
<pre> int *p;
 {
 int local1;
 
 p = &amp;local1;
 local1 = 10;
 ....
 }
 {
 int local2;
 local2 = 20;
 ...
 }
 
 if (*p == 10) // out of scope use of local1
 {
 
 }</pre>
<p>Another example: </p>
<pre> struct A
 {
 A(int k) : i(k), j(k) { }
 int i;
 int j;
 };
 
 A *ap;
 
 void foo(const A&amp; ar)
 {
 ap = &amp;ar;
 }
 
 void bar()
 {
 foo(A(10)); // temp object's lifetime ends when foo returns
 
 {
 A a(20);
 ....
 }
 ap-&gt;i+= 10; // ap references out of scope temp whose space
 // is reused with a. What is the value of ap-&gt;i?
 }</pre>
<p>The lifetime of a compiler generated temporary is well defined by the C<font SIZE="-2">++</font> standard. When a lifetime of a temporary ends, and if the temporary lives in memory, the optimizing compiler has the freedom to reuse its stack space with other temporaries or scoped local variables whose live range does not overlap with it. However some of the legacy code relies on the behavior of older compilers in which temporaries&#8217; stack space is not reused, the aggressive stack reuse can lead to runtime errors. This option is used to control the temporary stack reuse optimization.</p>
<dt><code>-ftrapv</code></p>
<dd>This option generates traps for signed overflow on addition, subtraction, multiplication operations.</p>
<dt><code>-fwrapv</code></p>
<dd>This option instructs the compiler to assume that signed arithmetic overflow of addition, subtraction and multiplication wraps around using twos-complement representation. This flag enables some optimizations and disables others. This option is enabled by default for the Java front end, as required by the Java language specification.</p>
<dt><code>-fexceptions</code></p>
<dd>Enable exception handling. Generates extra code needed to propagate exceptions. For some targets, this implies <font SIZE="-1">GCC</font> generates frame unwind information for all functions, which can produce significant data size overhead, although it does not affect execution. If you do not specify this option, <font SIZE="-1">GCC</font> enables it by default for languages like C<font SIZE="-2">++</font> that normally require exception handling, and disables it for languages like C that do not normally require it. However, you may need to enable this option when compiling C code that needs to interoperate properly with exception handlers written in C<font SIZE="-2">++</font>. You may also wish to disable this option if you are compiling older C<font SIZE="-2">++</font> programs that don&#8217;t use exception handling.</p>
<dt><code>-fnon-call-exceptions</code></p>
<dd>Generate code that allows trapping instructions to throw exceptions. Note that this requires platform-specific runtime support that does not exist everywhere. Moreover, it only allows <i>trapping</i> instructions to throw exceptions, i.e. memory references or floating-point instructions. It does not allow exceptions to be thrown from arbitrary signal handlers such as <tt>&quot;SIGALRM&quot;</tt>.</p>
<dt><code>-fdelete-dead-exceptions</code></p>
<dd>Consider that instructions that may throw exceptions but don&#8217;t otherwise contribute to the execution of the program can be optimized away. This option is enabled by default for the Ada front end, as permitted by the Ada language specification. Optimization passes that cause dead exceptions to be removed are enabled independently at different optimization levels.</p>
<dt><code>-funwind-tables</code></p>
<dd>Similar to <code>-fexceptions</code>, except that it just generates any needed static data, but does not affect the generated code in any other way. You normally do not need to enable this option; instead, a language processor that needs this handling enables it on your behalf.</p>
<dt><code>-fasynchronous-unwind-tables</code></p>
<dd>Generate unwind table in <font SIZE="-1">DWARF 2</font> format, if supported by target machine. The table is exact at each instruction boundary, so it can be used for stack unwinding from asynchronous events (such as debugger or garbage collector).</p>
<dt><code>-fno-gnu-unique</code></p>
<dd>On systems with recent <font SIZE="-1">GNU</font> assembler and C library, the C<font SIZE="-2">++</font> compiler uses the <tt>&quot;STB_GNU_UNIQUE&quot;</tt> binding to make sure that definitions of template static data members and static local variables in inline functions are unique even in the presence of <tt>&quot;RTLD_LOCAL&quot;</tt>; this is necessary to avoid problems with a library used by two different <tt>&quot;RTLD_LOCAL&quot;</tt> plugins depending on a definition in one of them and therefore disagreeing with the other one about the binding of the symbol. But this causes <tt>&quot;dlclose&quot;</tt> to be ignored for affected DSOs; if your program relies on reinitialization of a <font SIZE="-1">DSO</font> via <tt>&quot;dlclose&quot;</tt> and <tt>&quot;dlopen&quot;</tt>, you can use <code>-fno-gnu-unique</code>.</p>
<dt><code>-fpcc-struct-return</code></p>
<dd>Return &#8220;short&#8221; <tt>&quot;struct&quot;</tt> and <tt>&quot;union&quot;</tt> values in memory like longer ones, rather than in registers. This convention is less efficient, but it has the advantage of allowing intercallability between GCC-compiled files and files compiled with other compilers, particularly the Portable C Compiler (pcc). </p>
<p> The precise convention for returning structures in memory depends on the target configuration macros. </p>
<p> Short structures and unions are those whose size and alignment match that of some integer type. </p>
<p> <code>Warning:</code> code compiled with the <code>-fpcc-struct-return</code> switch is not binary compatible with code compiled with the <code>-freg-struct-return</code> switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-freg-struct-return</code></p>
<dd>Return <tt>&quot;struct&quot;</tt> and <tt>&quot;union&quot;</tt> values in registers when possible. This is more efficient for small structures than <code>-fpcc-struct-return</code>. </p>
<p> If you specify neither <code>-fpcc-struct-return</code> nor <code>-freg-struct-return</code>, <font SIZE="-1">GCC</font> defaults to whichever convention is standard for the target. If there is no standard convention, <font SIZE="-1">GCC</font> defaults to <code>-fpcc-struct-return</code>, except on targets where <font SIZE="-1">GCC</font> is the principal compiler. In those cases, we can choose the standard, and we chose the more efficient register return alternative. </p>
<p> <code>Warning:</code> code compiled with the <code>-freg-struct-return</code> switch is not binary compatible with code compiled with the <code>-fpcc-struct-return</code> switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fshort-enums</code></p>
<dd>Allocate to an <tt>&quot;enum&quot;</tt> type only as many bytes as it needs for the declared range of possible values. Specifically, the <tt>&quot;enum&quot;</tt> type is equivalent to the smallest integer type that has enough room. </p>
<p> <code>Warning:</code> the <code>-fshort-enums</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fshort-double</code></p>
<dd>Use the same size for <tt>&quot;double&quot;</tt> as for <tt>&quot;float&quot;</tt>. </p>
<p> <code>Warning:</code> the <code>-fshort-double</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fshort-wchar</code></p>
<dd>Override the underlying type for <code>wchar_t</code> to be <code>short unsigned int</code> instead of the default for the target. This option is useful for building programs to run under <font SIZE="-1">WINE.</font> </p>
<p> <code>Warning:</code> the <code>-fshort-wchar</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fno-common</code></p>
<dd>In C code, controls the placement of uninitialized global variables. Unix C compilers have traditionally permitted multiple definitions of such variables in different compilation units by placing the variables in a common block. This is the behavior specified by <code>-fcommon</code>, and is the default for <font SIZE="-1">GCC</font> on most targets. On the other hand, this behavior is not required by <font SIZE="-1">ISO C,</font> and on some targets may carry a speed or code size penalty on variable references. The <code>-fno-common</code> option specifies that the compiler should place uninitialized global variables in the data section of the object file, rather than generating them as common blocks. This has the effect that if the same variable is declared (without <tt>&quot;extern&quot;</tt>) in two different compilations, you get a multiple-definition error when you link them. In this case, you must compile with <code>-fcommon</code> instead. Compiling with <code>-fno-common</code> is useful on targets for which it provides better performance, or if you wish to verify that the program will work on other systems that always treat uninitialized variable declarations this way.</p>
<dt><code>-fno-ident</code></p>
<dd>Ignore the <code>#ident</code> directive.</p>
<dt><code>-finhibit-size-directive</code></p>
<dd>Don&#8217;t output a <tt>&quot;.size&quot;</tt> assembler directive, or anything else that would cause trouble if the function is split in the middle, and the two halves are placed at locations far apart in memory. This option is used when compiling <i>crtstuff.c</i>; you should not need to use it for anything else.</p>
<dt><code>-fverbose-asm</code></p>
<dd>Put extra commentary information in the generated assembly code to make it more readable. This option is generally only of use to those who actually need to read the generated assembly code (perhaps while debugging the compiler itself). </p>
<p> <code>-fno-verbose-asm</code>, the default, causes the extra information to be omitted and is useful when comparing two assembler files.</p>
<dt><code>-frecord-gcc-switches</code></p>
<dd>This switch causes the command line used to invoke the compiler to be recorded into the object file that is being created. This switch is only implemented on some targets and the exact format of the recording is target and binary file format dependent, but it usually takes the form of a section containing <font SIZE="-1">ASCII</font> text. This switch is related to the <code>-fverbose-asm</code> switch, but that switch only records information in the assembler output file as comments, so it never reaches the object file. See also <code>-grecord-gcc-switches</code> for another way of storing compiler options into the object file.</p>
<dt><code>-fpic</code></p>
<dd>Generate position-independent code (<font SIZE="-1">PIC</font>) suitable for use in a shared library, if supported for the target machine. Such code accesses all constant addresses through a global offset table (<font SIZE="-1">GOT</font>). The dynamic loader resolves the <font SIZE="-1">GOT</font> entries when the program starts (the dynamic loader is not part of <font SIZE="-1">GCC</font>; it is part of the operating system). If the <font SIZE="-1">GOT</font> size for the linked executable exceeds a machine-specific maximum size, you get an error message from the linker indicating that <code>-fpic</code> does not work; in that case, recompile with <code>-fPIC</code> instead. (These maximums are 8k on the <font SIZE="-1">SPARC</font> and 32k on the m68k and <font SIZE="-1">RS/6000. </font> The 386 has no such limit.) </p>
<p> Position-independent code requires special support, and therefore works only on certain machines. For the 386, <font SIZE="-1">GCC</font> supports <font SIZE="-1">PIC</font> for System V but not for the Sun 386i. Code generated for the <font SIZE="-1">IBM RS/6000</font> is always position-independent. </p>
<p> When this flag is set, the macros <tt>&quot;__pic__&quot;</tt> and <tt>&quot;__PIC__&quot;</tt> are defined to 1.</p>
<dt><code>-fPIC</code></p>
<dd>If supported for the target machine, emit position-independent code, suitable for dynamic linking and avoiding any limit on the size of the global offset table. This option makes a difference on the m68k, PowerPC and <font SIZE="-1">SPARC.</font> </p>
<p> Position-independent code requires special support, and therefore works only on certain machines. </p>
<p> When this flag is set, the macros <tt>&quot;__pic__&quot;</tt> and <tt>&quot;__PIC__&quot;</tt> are defined to 2.</p>
<dt><code>-fpie</code></p>
<dd>
<dt><code>-fPIE</code></p>
<dd>These options are similar to <code>-fpic</code> and <code>-fPIC</code>, but generated position independent code can be only linked into executables. Usually these options are used when <code>-pie</code> <font SIZE="-1">GCC</font> option is used during linking. </p>
<p> <code>-fpie</code> and <code>-fPIE</code> both define the macros <tt>&quot;__pie__&quot;</tt> and <tt>&quot;__PIE__&quot;</tt>. The macros have the value 1 for <code>-fpie</code> and 2 for <code>-fPIE</code>.</p>
<dt><code>-fno-jump-tables</code></p>
<dd>Do not use jump tables for switch statements even where it would be more efficient than other code generation strategies. This option is of use in conjunction with <code>-fpic</code> or <code>-fPIC</code> for building code that forms part of a dynamic linker and cannot reference the address of a jump table. On some targets, jump tables do not require a <font SIZE="-1">GOT</font> and this option is not needed.</p>
<dt><code>-ffixed-</code><i>reg</i></p>
<dd>Treat the register named <i>reg</i> as a fixed register; generated code should never refer to it (except perhaps as a stack pointer, frame pointer or in some other fixed role). </p>
<p> <i>reg</i> must be the name of a register. The register names accepted are machine-specific and are defined in the <tt>&quot;REGISTER_NAMES&quot;</tt> macro in the machine description macro file. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice.</p>
<dt><code>-fcall-used-</code><i>reg</i></p>
<dd>Treat the register named <i>reg</i> as an allocable register that is clobbered by function calls. It may be allocated for temporaries or variables that do not live across a call. Functions compiled this way do not save and restore the register <i>reg</i>. </p>
<p> It is an error to use this flag with the frame pointer or stack pointer. Use of this flag for other registers that have fixed pervasive roles in the machine&#8217;s execution model produces disastrous results. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice.</p>
<dt><code>-fcall-saved-</code><i>reg</i></p>
<dd>Treat the register named <i>reg</i> as an allocable register saved by functions. It may be allocated even for temporaries or variables that live across a call. Functions compiled this way save and restore the register <i>reg</i> if they use it. </p>
<p> It is an error to use this flag with the frame pointer or stack pointer. Use of this flag for other registers that have fixed pervasive roles in the machine&#8217;s execution model produces disastrous results. </p>
<p> A different sort of disaster results from the use of this flag for a register in which function values may be returned. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice.</p>
<dt><code>-fpack-struct[=</code><i>n</i><code>]</code></p>
<dd>Without a value specified, pack all structure members together without holes. When a value is specified (which must be a small power of two), pack structure members according to this value, representing the maximum alignment (that is, objects with default alignment requirements larger than this are output potentially unaligned at the next fitting location. </p>
<p> <code>Warning:</code> the <code>-fpack-struct</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Additionally, it makes the code suboptimal. Use it to conform to a non-default application binary interface.</p>
<dt><code>-finstrument-functions</code></p>
<dd>Generate instrumentation calls for entry and exit to functions. Just after function entry and just before function exit, the following profiling functions are called with the address of the current function and its call site. (On some platforms, <tt>&quot;__builtin_return_address&quot;</tt> does not work beyond the current function, so the call site information may not be available to the profiling functions otherwise.) </p>
<pre> void __cyg_profile_func_enter (void *this_fn,
 void *call_site);
 void __cyg_profile_func_exit (void *this_fn,
 void *call_site);</pre>
<p>The first argument is the address of the start of the current function, which may be looked up exactly in the symbol table. </p>
<p> This instrumentation is also done for functions expanded inline in other functions. The profiling calls indicate where, conceptually, the inline function is entered and exited. This means that addressable versions of such functions must be available. If all your uses of a function are expanded inline, this may mean an additional expansion of code size. If you use <code>extern inline</code> in your C code, an addressable version of such functions must be provided. (This is normally the case anyway, but if you get lucky and the optimizer always expands the functions inline, you might have gotten away without providing static copies.) </p>
<p> A function may be given the attribute <tt>&quot;no_instrument_function&quot;</tt>, in which case this instrumentation is not done. This can be used, for example, for the profiling functions listed above, high-priority interrupt routines, and any functions from which the profiling functions cannot safely be called (perhaps signal handlers, if the profiling routines generate output or allocate memory).</p>
<dt><code>-finstrument-functions-exclude-file-list=</code><i>file</i><code>,</code><i>file</i><code>,&#8230;</code></p>
<dd>Set the list of functions that are excluded from instrumentation (see the description of <tt>&quot;-finstrument-functions&quot;</tt>). If the file that contains a function definition matches with one of <i>file</i>, then that function is not instrumented. The match is done on substrings: if the <i>file</i> parameter is a substring of the file name, it is considered to be a match. </p>
<p> For example: </p>
<pre> -finstrument-functions-exclude-file-list=/bits/stl,include/sys</pre>
<p>excludes any inline function defined in files whose pathnames contain <tt>&quot;/bits/stl&quot;</tt> or <tt>&quot;include/sys&quot;</tt>. </p>
<p> If, for some reason, you want to include letter <tt>','</tt> in one of <i>sym</i>, write <tt>','</tt>. For example, <tt>&quot;-finstrument-functions-exclude-file-list=',,tmp'&quot;</tt> (note the single quote surrounding the option).</p>
<dt><code>-finstrument-functions-exclude-function-list=</code><i>sym</i><code>,</code><i>sym</i><code>,&#8230;</code></p>
<dd>This is similar to <tt>&quot;-finstrument-functions-exclude-file-list&quot;</tt>, but this option sets the list of function names to be excluded from instrumentation. The function name to be matched is its user-visible name, such as <tt>&quot;vector&lt;int&gt; blah(const vector&lt;int&gt; &amp;)&quot;</tt>, not the internal mangled name (e.g., <tt>&quot;_Z4blahRSt6vectorIiSaIiEE&quot;</tt>). The match is done on substrings: if the <i>sym</i> parameter is a substring of the function name, it is considered to be a match. For C99 and C<font SIZE="-2">++</font> extended identifiers, the function name must be given in <font SIZE="-1">UTF-8,</font> not using universal character names.</p>
<dt><code>-fstack-check</code></p>
<dd>Generate code to verify that you do not go beyond the boundary of the stack. You should specify this flag if you are running in an environment with multiple threads, but you only rarely need to specify it in a single-threaded environment since stack overflow is automatically detected on nearly all systems if there is only one stack. </p>
<p> Note that this switch does not actually cause checking to be done; the operating system or the language runtime must do that. The switch causes generation of code to ensure that they see the stack being extended. </p>
<p> You can additionally specify a string parameter: <tt>&quot;no&quot;</tt> means no checking, <tt>&quot;generic&quot;</tt> means force the use of old-style checking, <tt>&quot;specific&quot;</tt> means use the best checking method and is equivalent to bare <code>-fstack-check</code>. </p>
<p> Old-style checking is a generic mechanism that requires no specific target support in the compiler but comes with the following drawbacks:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1.</p>
<dd>Modified allocation strategy for large objects: they are always allocated dynamically if their size exceeds a fixed threshold.</p>
<dt>2.</p>
<dd>Fixed limit on the size of the static frame of functions: when it is topped by a particular function, stack checking is not reliable and a warning is issued by the compiler.</p>
<dt>3.</p>
<dd>Inefficiency: because of both the modified allocation strategy and the generic implementation, code performance is hampered.</dl>
</dl>
<dl COMPACT>
<dd>Note that old-style stack checking is also the fallback method for <tt>&quot;specific&quot;</tt> if no target support has been added in the compiler.</dl>
<dt><code>-fstack-limit-register=</code><i>reg</i></p>
<dd>
<dt><code>-fstack-limit-symbol=</code><i>sym</i></p>
<dd>
<dt><code>-fno-stack-limit</code></p>
<dd>Generate code to ensure that the stack does not grow beyond a certain value, either the value of a register or the address of a symbol. If a larger stack is required, a signal is raised at run time. For most targets, the signal is raised before the stack overruns the boundary, so it is possible to catch the signal without taking special precautions. </p>
<p> For instance, if the stack starts at absolute address <code>0x80000000</code> and grows downwards, you can use the flags <code>-fstack-limit-symbol=__stack_limit</code> and <code>-Wl,&#8211;defsym,__stack_limit=0x7ffe0000</code> to enforce a stack limit of 128KB. Note that this may only work with the <font SIZE="-1">GNU</font> linker.</p>
<dt><code>-fsplit-stack</code></p>
<dd>Generate code to automatically split the stack before it overflows. The resulting program has a discontiguous stack which can only overflow if the program is unable to allocate any more memory. This is most useful when running threaded programs, as it is no longer necessary to calculate a good stack size to use for each thread. This is currently only implemented for the i386 and x86_64 back ends running GNU/Linux. </p>
<p> When code compiled with <code>-fsplit-stack</code> calls code compiled without <code>-fsplit-stack</code>, there may not be much stack space available for the latter code to run. If compiling all code, including library code, with <code>-fsplit-stack</code> is not an option, then the linker can fix up these calls so that the code compiled without <code>-fsplit-stack</code> always has a large stack. Support for this is implemented in the gold linker in <font SIZE="-1">GNU</font> binutils release 2.21 and later.</p>
<dt><code>-fleading-underscore</code></p>
<dd>This option and its counterpart, <code>-fno-leading-underscore</code>, forcibly change the way C symbols are represented in the object file. One use is to help link with legacy assembly code. </p>
<p> <code>Warning:</code> the <code>-fleading-underscore</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface. Not all targets provide complete support for this switch.</p>
<dt><code>-ftls-model=</code><i>model</i></p>
<dd>Alter the thread-local storage model to be used. The <i>model</i> argument should be one of <tt>&quot;global-dynamic&quot;</tt>, <tt>&quot;local-dynamic&quot;</tt>, <tt>&quot;initial-exec&quot;</tt> or <tt>&quot;local-exec&quot;</tt>. Note that the choice is subject to optimization: the compiler may use a more efficient model for symbols not visible outside of the translation unit, or if <code>-fpic</code> is not given on the command line. </p>
<p> The default without <code>-fpic</code> is <tt>&quot;initial-exec&quot;</tt>; with <code>-fpic</code> the default is <tt>&quot;global-dynamic&quot;</tt>.</p>
<dt><code>-fvisibility=</code><i>default|internal|hidden|protected</i></p>
<dd>Set the default <font SIZE="-1">ELF</font> image symbol visibility to the specified option&#8212;all symbols are marked with this unless overridden within the code. Using this feature can very substantially improve linking and load times of shared object libraries, produce more optimized code, provide near-perfect <font SIZE="-1">API</font> export and prevent symbol clashes. It is <code>strongly</code> recommended that you use this in any shared objects you distribute. </p>
<p> Despite the nomenclature, <tt>&quot;default&quot;</tt> always means public; i.e., available to be linked against from outside the shared object. <tt>&quot;protected&quot;</tt> and <tt>&quot;internal&quot;</tt> are pretty useless in real-world usage so the only other commonly used option is <tt>&quot;hidden&quot;</tt>. The default if <code>-fvisibility</code> isn&#8217;t specified is <tt>&quot;default&quot;</tt>, i.e., make every symbol public&#8212;this causes the same behavior as previous versions of <font SIZE="-1">GCC.</font> </p>
<p> A good explanation of the benefits offered by ensuring <font SIZE="-1">ELF</font> symbols have the correct visibility is given by &#8220;How To Write Shared Libraries&#8221; by Ulrich Drepper (which can be found at &lt;<code><a rel="nofollow" href="http://people.redhat.com/~drepper/">http://people.redhat.com/~drepper/</a></code>&gt;)&#8212;however a superior solution made possible by this option to marking things hidden when the default is public is to make the default hidden and mark things public. This is the norm with DLLs on Windows and with <code>-fvisibility=hidden</code> and <tt>&quot;__attribute__ ((visibility(&quot;default&quot;)))&quot;</tt> instead of <tt>&quot;__declspec(dllexport)&quot;</tt> you get almost identical semantics with identical syntax. This is a great boon to those working with cross-platform projects. </p>
<p> For those adding visibility support to existing code, you may find <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility</code> of use. This works by you enclosing the declarations you wish to set visibility for with (for example) <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility push(hidden)</code> and <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility pop</code>. Bear in mind that symbol visibility should be viewed <code>as part of the </code><font SIZE="-1"><code>API</code></font><code> interface contract</code> and thus all new code should always specify visibility when it is not the default; i.e., declarations only for use within the local <font SIZE="-1">DSO</font> should <code>always</code> be marked explicitly as hidden as so to avoid <font SIZE="-1">PLT</font> indirection overheads&#8212;making this abundantly clear also aids readability and self-documentation of the code. Note that due to <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> specification requirements, <tt>&quot;operator new&quot;</tt> and <tt>&quot;operator delete&quot;</tt> must always be of default visibility. </p>
<p> Be aware that headers from outside your project, in particular system headers and headers from any other library you use, may not be expecting to be compiled with visibility other than the default. You may need to explicitly say <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility push(default)</code> before including any such headers. </p>
<p> <code>extern</code> declarations are not affected by <code>-fvisibility</code>, so a lot of code can be recompiled with <code>-fvisibility=hidden</code> with no modifications. However, this means that calls to <tt>&quot;extern&quot;</tt> functions with no explicit visibility use the <font SIZE="-1">PLT,</font> so it is more effective to use <tt>&quot;__attribute ((visibility))&quot;</tt> and/or <tt>&quot;#pragma GCC visibility&quot;</tt> to tell the compiler which <tt>&quot;extern&quot;</tt> declarations should be treated as hidden. </p>
<p> Note that <code>-fvisibility</code> does affect C<font SIZE="-2">++</font> vague linkage entities. This means that, for instance, an exception class that is be thrown between DSOs must be explicitly marked with default visibility so that the <code>type_info</code> nodes are unified between the DSOs. </p>
<p> An overview of these techniques, their benefits and how to use them is at &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/wiki/Visibility">http://gcc.gnu.org/wiki/Visibility</a></code>&gt;.</p>
<dt><code>-fstrict-volatile-bitfields</code></p>
<dd>This option should be used if accesses to volatile bit-fields (or other structure fields, although the compiler usually honors those types anyway) should use a single access of the width of the field&#8217;s type, aligned to a natural alignment if possible. For example, targets with memory-mapped peripheral registers might require all such accesses to be 16 bits wide; with this flag you can declare all peripheral bit-fields as <tt>&quot;unsigned short&quot;</tt> (assuming short is 16 bits on these targets) to force <font SIZE="-1">GCC</font> to use 16-bit accesses instead of, perhaps, a more efficient 32-bit access. </p>
<p> If this option is disabled, the compiler uses the most efficient instruction. In the previous example, that might be a 32-bit load instruction, even though that accesses bytes that do not contain any portion of the bit-field, or memory-mapped registers unrelated to the one being updated. </p>
<p> In some cases, such as when the <tt>&quot;packed&quot;</tt> attribute is applied to a structure field, it may not be possible to access the field with a single read or write that is correctly aligned for the target machine. In this case <font SIZE="-1">GCC</font> falls back to generating multiple accesses rather than code that will fault or truncate the result at run time. </p>
<p> Note: Due to restrictions of the C/C<font SIZE="-2">++</font>11 memory model, write accesses are not allowed to touch non bit-field members. It is therefore recommended to define all bits of the field&#8217;s type as bit-field members. </p>
<p> The default value of this option is determined by the application binary interface for the target processor.</p>
<dt><code>-fsync-libcalls</code></p>
<dd>This option controls whether any out-of-line instance of the <tt>&quot;__sync&quot;</tt> family of functions may be used to implement the C<font SIZE="-2">++</font>11 <tt>&quot;__atomic&quot;</tt> family of functions. </p>
<p> The default value of this option is enabled, thus the only useful form of the option is <code>-fno-sync-libcalls</code>. This option is used in the implementation of the <i>libatomic</i> runtime library.</dl>
<h2>Environment</h2>
<p>This section describes several environment variables that affect how <font SIZE="-1">GCC</font> operates. Some of them work by specifying directories or prefixes to use when searching for various kinds of files. Some are used to specify other aspects of the compilation environment. </p>
<p> Note that you can also specify places to search using options such as <code>-B</code>, <code>-I</code> and <code>-L</code>. These take precedence over places specified using environment variables, which in turn take precedence over those specified by the configuration of <font SIZE="-1">GCC.</font></p>
<dl COMPACT>
<dt><font SIZE="-1"><code>LANG</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LC_CTYPE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LC_MESSAGES</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LC_ALL</code></font></p>
<dd>These environment variables control the way that <font SIZE="-1">GCC</font> uses localization information which allows <font SIZE="-1">GCC</font> to work with different national conventions. <font SIZE="-1">GCC</font> inspects the locale categories <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font> if it has been configured to do so. These locale categories can be set to any value supported by your installation. A typical value is <code>en_GB.UTF-8</code> for English in the United Kingdom encoded in <font SIZE="-1">UTF-8.</font> </p>
<p> The <font SIZE="-1"><code>LC_CTYPE</code></font> environment variable specifies character classification. <font SIZE="-1">GCC</font> uses it to determine the character boundaries in a string; this is needed for some multibyte encodings that contain quote and escape characters that are otherwise interpreted as a string end or escape. </p>
<p> The <font SIZE="-1"><code>LC_MESSAGES</code></font> environment variable specifies the language to use in diagnostic messages. </p>
<p> If the <font SIZE="-1"><code>LC_ALL</code></font> environment variable is set, it overrides the value of <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font>; otherwise, <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font> default to the value of the <font SIZE="-1"><code>LANG</code></font> environment variable. If none of these variables are set, <font SIZE="-1">GCC</font> defaults to traditional C English behavior.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd>If <font SIZE="-1"><code>TMPDIR</code></font> is set, it specifies the directory to use for temporary files. <font SIZE="-1">GCC</font> uses temporary files to hold the output of one stage of compilation which is to be used as input to the next stage: for example, the output of the preprocessor, which is the input to the compiler proper.</p>
<dt><font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font></p>
<dd>Setting <font SIZE="-1"><code>GCC_COMPARE_DEBUG</code></font> is nearly equivalent to passing <code>-fcompare-debug</code> to the compiler driver. See the documentation of this option for more details.</p>
<dt><font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font></p>
<dd>If <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is set, it specifies a prefix to use in the names of the subprograms executed by the compiler. No slash is added when this prefix is combined with the name of a subprogram, but you can specify a prefix that ends with a slash if you wish. </p>
<p> If <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is not set, <font SIZE="-1">GCC</font> attempts to figure out an appropriate prefix to use based on the pathname it is invoked with. </p>
<p> If <font SIZE="-1">GCC</font> cannot find the subprogram using the specified prefix, it tries looking in the usual places for the subprogram. </p>
<p> The default value of <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is <i>prefix/lib/gcc/</i> where <i>prefix</i> is the prefix to the installed compiler. In many cases <i>prefix</i> is the value of <tt>&quot;prefix&quot;</tt> when you ran the <i>configure</i> script. </p>
<p> Other prefixes specified with <code>-B</code> take precedence over this prefix. </p>
<p> This prefix is also used for finding files such as <i>crt0.o</i> that are used for linking. </p>
<p> In addition, the prefix is used in an unusual way in finding the directories to search for header files. For each of the standard directories whose name normally begins with <code>/usr/local/lib/gcc</code> (more precisely, with the value of <font SIZE="-1"><code>GCC_INCLUDE_DIR</code></font>), <font SIZE="-1">GCC</font> tries replacing that beginning with the specified prefix to produce an alternate directory name. Thus, with <code>-Bfoo/</code>, <font SIZE="-1">GCC</font> searches <i>foo/bar</i> just before it searches the standard directory <i>/usr/local/lib/bar</i>. If a standard directory begins with the configured <i>prefix</i> then the value of <i>prefix</i> is replaced by <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> when looking for header files.</p>
<dt><font SIZE="-1"><code>COMPILER_PATH</code></font></p>
<dd>The value of <font SIZE="-1"><code>COMPILER_PATH</code></font> is a colon-separated list of directories, much like <font SIZE="-1"><code>PATH</code></font>. <font SIZE="-1">GCC</font> tries the directories thus specified when searching for subprograms, if it can&#8217;t find the subprograms using <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>.</p>
<dt><font SIZE="-1"><code>LIBRARY_PATH</code></font></p>
<dd>The value of <font SIZE="-1"><code>LIBRARY_PATH</code></font> is a colon-separated list of directories, much like <font SIZE="-1"><code>PATH</code></font>. When configured as a native compiler, <font SIZE="-1">GCC</font> tries the directories thus specified when searching for special linker files, if it can&#8217;t find them using <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. Linking using <font SIZE="-1">GCC</font> also uses these directories when searching for ordinary libraries for the <code>-l</code> option (but directories specified with <code>-L</code> come first).</p>
<dt><font SIZE="-1"><code>LANG</code></font></p>
<dd>This variable is used to pass locale information to the compiler. One way in which this information is used is to determine the character set to be used when character literals, string literals and comments are parsed in C and C<font SIZE="-2">++</font>. When the compiler is configured to allow multibyte characters, the following values for <font SIZE="-1"><code>LANG</code></font> are recognized:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>C-JIS</code></p>
<dd>Recognize <font SIZE="-1">JIS</font> characters.</p>
<dt><code>C-SJIS</code></p>
<dd>Recognize <font SIZE="-1">SJIS</font> characters.</p>
<dt><code>C-EUCJP</code></p>
<dd>Recognize <font SIZE="-1">EUCJP</font> characters.</dl>
</dl>
<dl COMPACT>
<dd>If <font SIZE="-1"><code>LANG</code></font> is not defined, or if it has some other value, then the compiler uses <tt>&quot;mblen&quot;</tt> and <tt>&quot;mbtowc&quot;</tt> as defined by the default locale to recognize and translate multibyte characters.</dl>
</dl>
<p> Some additional environment variables affect the behavior of the preprocessor.</p>
<dl COMPACT>
<dt><font SIZE="-1"><code>CPATH</code></font></p>
<dd>
<dt><code>C_INCLUDE_PATH</code></p>
<dd>
<dt><font SIZE="-1"><code>CPLUS_INCLUDE_PATH</code></font></p>
<dd>
<dt><font SIZE="-1"><code>OBJC_INCLUDE_PATH</code></font></p>
<dd>Each variable&#8217;s value is a list of directories separated by a special character, much like <font SIZE="-1"><code>PATH</code></font>, in which to look for header files. The special character, <tt>&quot;PATH_SEPARATOR&quot;</tt>, is target-dependent and determined at <font SIZE="-1">GCC</font> build time. For Microsoft Windows-based targets it is a semicolon, and for almost all other targets it is a colon. </p>
<p> <font SIZE="-1"><code>CPATH</code></font> specifies a list of directories to be searched as if specified with <code>-I</code>, but after any paths given with <code>-I</code> options on the command line. This environment variable is used regardless of which language is being preprocessed. </p>
<p> The remaining environment variables apply only when preprocessing the particular language indicated. Each specifies a list of directories to be searched as if specified with <code>-isystem</code>, but after any paths given with <code>-isystem</code> options on the command line. </p>
<p> In all these variables, an empty element instructs the compiler to search its current working directory. Empty elements can appear at the beginning or end of a path. For instance, if the value of <font SIZE="-1"><code>CPATH</code></font> is <tt>&quot;:/special/include&quot;</tt>, that has the same effect as <code>-I. -I/special/include</code>.</p>
<dt><font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font></p>
<dd>If this variable is set, its value specifies how to output dependencies for Make based on the non-system header files processed by the compiler. System header files are ignored in the dependency output. </p>
<p> The value of <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font> can be just a file name, in which case the Make rules are written to that file, guessing the target name from the source file name. Or the value can have the form <i>file</i><i>target</i>, in which case the rules are written to file <i>file</i> using <i>target</i> as the target name. </p>
<p> In other words, this environment variable is equivalent to combining the options <code>-MM</code> and <code>-MF</code>, with an optional <code>-MT</code> switch too.</p>
<dt><font SIZE="-1"><code>SUNPRO_DEPENDENCIES</code></font></p>
<dd>This variable is the same as <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font> (see above), except that system header files are not ignored, so it implies <code>-M</code> rather than <code>-MM</code>. However, the dependence on the main input file is omitted.</dl>
<h2>Bugs</h2>
<p>For instructions on reporting bugs, see &lt;<code><a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla">http://bugzilla.redhat.com/bugzilla</a></code>&gt;.</p>
<h2>Footnotes</h2>
<dl COMPACT>
<dt>1.</p>
<dd>On some systems, <code>gcc -shared</code> needs to build supplementary stub code for constructors to work. On multi-libbed systems, <code>gcc -shared</code> must select the correct support libraries to link against. Failing to supply the correct flags may lead to subtle defects. Supplying them in cases where they are not necessary is innocuous.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-gpl/">gpl</a></i>(7), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), <i><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></i>(7), <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1), <i><a href="/docs/linux/man/1-gcov/">gcov</a></i>(1), <i><a href="/docs/linux/man/1-as/">as</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), <i><a href="/docs/linux/man/1-gdb/">gdb</a></i>(1), <i><a href="/docs/linux/man/1-adb/">adb</a></i>(1), <i><a href="/docs/linux/man/1-dbx/">dbx</a></i>(1), <i><a href="/docs/linux/man/1-sdb/">sdb</a></i>(1) and the Info entries for <i>gcc</i>, <i>cpp</i>, <i>as</i>, <i>ld</i>, <i>binutils</i> and <i>gdb</i>.</p>
<h2>Author</h2>
<p>See the Info entry for <code>gcc</code>, or &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/gcc/Contributors.html">http://gcc.gnu.org/onlinedocs/gcc/Contributors.html</a></code>&gt;, for contributors to <font SIZE="-1">GCC.</font></p>
<h2>Copyright</h2>
<p>Copyright (c) 1988-2015 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre> A GNU Manual</pre>
<p>(b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre> You have freedom to copy and modify this GNU Manual, like GNU
 software. Copies published by the Free Software Foundation raise
 funds for GNU development.</pre>
