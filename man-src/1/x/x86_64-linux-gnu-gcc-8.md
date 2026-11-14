---
title: "x86_64-linux-gnu-gcc-8(1)"
name: "x86_64-linux-gnu-gcc-8"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-gcc-8/"
description: "gcc – GNU project C and C++ compiler"
---

<p>gcc &#8211; GNU project C and C++ compiler </p>
<h2>Synopsis</h2>
<p>gcc [<code>-c</code>|<code>-S</code>|<code>-E</code>] [<code>-std=</code><i>standard</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>]&nbsp;[<code>-pg</code>]&nbsp;[<code>-O</code><i>level</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-W</code><i>warn</i>&#8230;]&nbsp;[<code>-Wpedantic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-I</code><i>dir</i>&#8230;]&nbsp;[<code>-L</code><i>dir</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-D</code><i>macro</i>[=<i>defn</i>]&#8230;]&nbsp;[<code>-U</code><i>macro</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code><i>option</i>&#8230;]&nbsp;[<code>-m</code><i>machine-option</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-o</code>&nbsp;<i>outfile</i>]&nbsp;[@<i>file</i>]&nbsp;<i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder. <code>g++</code> accepts mostly the same options as <code>gcc</code>.</p>
<h2>Description</h2>
<p>When you invoke <font SIZE="-1">GCC,</font> it normally does preprocessing, compilation, assembly and linking. The &#8220;overall options&#8221; allow you to stop this process at an intermediate stage. For example, the <code>-c</code> option says not to run the linker. Then the output consists of object files output by the assembler. </p>
<p> Other options are passed on to one or more stages of processing. Some options control the preprocessor and others the compiler itself. Yet other options control the assembler and linker; most of these are not documented here, since you rarely need to use any of them. </p>
<p> Most of the command-line options that you can use with <font SIZE="-1">GCC</font> are useful for C programs; when an option is only useful with another language (usually C<font SIZE="-2">++</font>), the explanation says so explicitly. If the description for a particular option does not mention a source language, you can use that option with all supported languages. </p>
<p> The usual way to run <font SIZE="-1">GCC</font> is to run the executable called <code>gcc</code>, or <i>machine</i><code>-gcc</code> when cross-compiling, or <i>machine</i><code>-gcc-</code><i>version</i> to run a specific version of <font SIZE="-1">GCC.</font> When you compile C<font SIZE="-2">++</font> programs, you should invoke <font SIZE="-1">GCC</font> as <code>g++</code> instead. </p>
<p> The <code>gcc</code> program accepts options and file names as operands. Many options have multi-letter names; therefore multiple single-letter options may <i>not</i> be grouped: <code>-dv</code> is very different from <code>-d -v</code>. </p>
<p> You can mix options and other arguments. For the most part, the order you use doesn&#8217;t matter. Order does matter when you use several options of the same kind; for example, if you specify <code>-L</code> more than once, the directories are searched in the order specified. Also, the placement of the <code>-l</code> option is significant. </p>
<p> Many options have long names starting with <code>-f</code> or with <code>-W</code>&#8212;for example, <code>-fmove-loop-invariants</code>, <code>-Wformat</code> and so on. Most of these have both positive and negative forms; the negative form of <code>-ffoo</code> is <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.</p>
<h2>Options</h2>
<h3>Option Summary</h3>
<p>Here is a summary of all the options, grouped by type. Explanations are in the following sections.</p>
<dl COMPACT>
<dt><i>Overall Options</i></p>
<dd><code>-c -S -E -o</code> <i>file</i> <code>-x</code> <i>language</i> <code>-v -### &#8211;help</code>[<code>=</code><i>class</i>[<code>,&#8230;</code>]] <code>&#8211;target-help &#8211;version -pass-exit-codes -pipe -specs=</code><i>file</i> <code>-wrapper @</code><i>file</i> <code>-ffile-prefix-map=</code><i>old</i><code>=</code><i>new</i> <code>-fplugin=</code><i>file</i> <code>-fplugin-arg-</code><i>name</i><code>=</code><i>arg</i> <code>-fdump-ada-spec</code>[<code>-slim</code>] <code>-fada-spec-parent=</code><i>unit</i> <code>-fdump-go-spec=</code><i>file</i></p>
<dt><i>C Language Options</i></p>
<dd><code>-ansi -std=</code><i>standard</i> <code>-fgnu89-inline -fpermitted-flt-eval-methods=</code><i>standard</i> <code>-aux-info</code> <i>filename</i> <code>-fallow-parameterless-variadic-functions -fno-asm -fno-builtin -fno-builtin-</code><i>function</i> <code>-fgimple -fhosted -ffreestanding -fopenacc -fopenmp -fopenmp-simd -fms-extensions -fplan9-extensions -fsso-struct=</code><i>endianness</i> <code>-fallow-single-precision -fcond-mismatch -flax-vector-conversions -fsigned-bitfields -fsigned-char -funsigned-bitfields -funsigned-char</code></p>
<dt><i>C<font SIZE="-2">++</font> Language Options</i></p>
<dd><code>-fabi-version=</code><i>n</i> <code>-fno-access-control -faligned-new=</code><i>n</i> <code>-fargs-in-order=</code><i>n</i> <code>-fcheck-new -fconstexpr-depth=</code><i>n</i> <code>-fconstexpr-loop-limit=</code><i>n</i> <code>-ffriend-injection -fno-elide-constructors -fno-enforce-eh-specs -ffor-scope -fno-for-scope -fno-gnu-keywords -fno-implicit-templates -fno-implicit-inline-templates -fno-implement-inlines -fms-extensions -fnew-inheriting-ctors -fnew-ttp-matching -fno-nonansi-builtins -fnothrow-opt -fno-operator-names -fno-optional-diags -fpermissive -fno-pretty-templates -frepo -fno-rtti -fsized-deallocation -ftemplate-backtrace-limit=</code><i>n</i> <code>-ftemplate-depth=</code><i>n</i> <code>-fno-threadsafe-statics -fuse-cxa-atexit -fno-weak -nostdinc++ -fvisibility-inlines-hidden -fvisibility-ms-compat -fext-numeric-literals -Wabi=</code><i>n</i> <code>-Wabi-tag -Wconversion-null -Wctor-dtor-privacy -Wdelete-non-virtual-dtor -Wliteral-suffix -Wmultiple-inheritance -Wnamespaces -Wnarrowing -Wnoexcept -Wnoexcept-type -Wclass-memaccess -Wnon-virtual-dtor -Wreorder -Wregister -Weffc++ -Wstrict-null-sentinel -Wtemplates -Wno-non-template-friend -Wold-style-cast -Woverloaded-virtual -Wno-pmf-conversions -Wsign-promo -Wvirtual-inheritance</code></p>
<dt><i>Objective-C and Objective-C<font SIZE="-2">++</font> Language Options</i></p>
<dd><code>-fconstant-string-class=</code><i>class-name</i> <code>-fgnu-runtime -fnext-runtime -fno-nil-receivers -fobjc-abi-version=</code><i>n</i> <code>-fobjc-call-cxx-cdtors -fobjc-direct-dispatch -fobjc-exceptions -fobjc-gc -fobjc-nilcheck -fobjc-std=objc1 -fno-local-ivars -fivar-visibility=</code>[<code>public</code>|<code>protected</code>|<code>private</code>|<code>package</code>] <code>-freplace-objc-classes -fzero-link -gen-decls -Wassign-intercept -Wno-protocol -Wselector -Wstrict-selector-match -Wundeclared-selector</code></p>
<dt><i>Diagnostic Message Formatting Options</i></p>
<dd><code>-fmessage-length=</code><i>n</i> <code>-fdiagnostics-show-location=</code>[<code>once</code>|<code>every-line</code>] <code>-fdiagnostics-color=</code>[<code>auto</code>|<code>never</code>|<code>always</code>] <code>-fno-diagnostics-show-option -fno-diagnostics-show-caret -fdiagnostics-parseable-fixits -fdiagnostics-generate-patch -fdiagnostics-show-template-tree -fno-elide-type -fno-show-column</code></p>
<dt><i>Warning Options</i></p>
<dd><code>-fsyntax-only -fmax-errors=</code><i>n</i> <code>-Wpedantic -pedantic-errors -w -Wextra -Wall -Waddress -Waggregate-return -Waligned-new -Walloc-zero -Walloc-size-larger-than=</code><i>n</i> <code>-Walloca -Walloca-larger-than=</code><i>n</i> <code>-Wno-aggressive-loop-optimizations -Warray-bounds -Warray-bounds=</code><i>n</i> <code>-Wno-attributes -Wbool-compare -Wbool-operation -Wno-builtin-declaration-mismatch -Wno-builtin-macro-redefined -Wc90-c99-compat -Wc99-c11-compat -Wc++-compat -Wc++11-compat -Wc++14-compat -Wcast-align -Wcast-align=strict -Wcast-function-type -Wcast-qual -Wchar-subscripts -Wchkp -Wcatch-value -Wcatch-value=</code><i>n</i> <code>-Wclobbered -Wcomment -Wconditionally-supported -Wconversion -Wcoverage-mismatch -Wno-cpp -Wdangling-else -Wdate-time -Wdelete-incomplete -Wno-deprecated -Wno-deprecated-declarations -Wno-designated-init -Wdisabled-optimization -Wno-discarded-qualifiers -Wno-discarded-array-qualifiers -Wno-div-by-zero -Wdouble-promotion -Wduplicated-branches -Wduplicated-cond -Wempty-body -Wenum-compare -Wno-endif-labels -Wexpansion-to-defined -Werror -Werror=* -Wextra-semi -Wfatal-errors -Wfloat-equal -Wformat -Wformat=2 -Wno-format-contains-nul -Wno-format-extra-args -Wformat-nonliteral -Wformat-overflow=</code><i>n</i> <code>-Wformat-security -Wformat-signedness -Wformat-truncation=</code><i>n</i> <code>-Wformat-y2k -Wframe-address -Wframe-larger-than=</code><i>len</i> <code>-Wno-free-nonheap-object -Wjump-misses-init -Wif-not-aligned -Wignored-qualifiers -Wignored-attributes -Wincompatible-pointer-types -Wimplicit -Wimplicit-fallthrough -Wimplicit-fallthrough=</code><i>n</i> <code>-Wimplicit-function-declaration -Wimplicit-int -Winit-self -Winline -Wno-int-conversion -Wint-in-bool-context -Wno-int-to-pointer-cast -Winvalid-memory-model -Wno-invalid-offsetof -Winvalid-pch -Wlarger-than=</code><i>len</i> <code>-Wlogical-op -Wlogical-not-parentheses -Wlong-long -Wmain -Wmaybe-uninitialized -Wmemset-elt-size -Wmemset-transposed-args -Wmisleading-indentation -Wmissing-attributes -Wmissing-braces -Wmissing-field-initializers -Wmissing-include-dirs -Wno-multichar -Wmultistatement-macros -Wnonnull -Wnonnull-compare -Wnormalized=</code>[<code>none</code>|<code>id</code>|<code>nfc</code>|<code>nfkc</code>] <code>-Wnull-dereference -Wodr -Wno-overflow -Wopenmp-simd -Woverride-init-side-effects -Woverlength-strings -Wpacked -Wpacked-bitfield-compat -Wpacked-not-aligned -Wpadded -Wparentheses -Wno-pedantic-ms-format -Wplacement-new -Wplacement-new=</code><i>n</i> <code>-Wpointer-arith -Wpointer-compare -Wno-pointer-to-int-cast -Wno-pragmas -Wredundant-decls -Wrestrict -Wno-return-local-addr -Wreturn-type -Wsequence-point -Wshadow -Wno-shadow-ivar -Wshadow=global, -Wshadow=local, -Wshadow=compatible-local -Wshift-overflow -Wshift-overflow=</code><i>n</i> <code>-Wshift-count-negative -Wshift-count-overflow -Wshift-negative-value -Wsign-compare -Wsign-conversion -Wfloat-conversion -Wno-scalar-storage-order -Wsizeof-pointer-div -Wsizeof-pointer-memaccess -Wsizeof-array-argument -Wstack-protector -Wstack-usage=</code><i>len</i> <code>-Wstrict-aliasing -Wstrict-aliasing=n -Wstrict-overflow -Wstrict-overflow=</code><i>n</i> <code>-Wstringop-overflow=</code><i>n</i> <code>-Wstringop-truncation -Wsuggest-attribute=</code>[<code>pure</code>|<code>const</code>|<code>noreturn</code>|<code>format</code>|<code>malloc</code>] <code>-Wsuggest-final-types -Wsuggest-final-methods -Wsuggest-override -Wmissing-format-attribute -Wsubobject-linkage -Wswitch -Wswitch-bool -Wswitch-default -Wswitch-enum -Wswitch-unreachable -Wsync-nand -Wsystem-headers -Wtautological-compare -Wtrampolines -Wtrigraphs -Wtype-limits -Wundef -Wuninitialized -Wunknown-pragmas -Wunsuffixed-float-constants -Wunused -Wunused-function -Wunused-label -Wunused-local-typedefs -Wunused-macros -Wunused-parameter -Wno-unused-result -Wunused-value -Wunused-variable -Wunused-const-variable -Wunused-const-variable=</code><i>n</i> <code>-Wunused-but-set-parameter -Wunused-but-set-variable -Wuseless-cast -Wvariadic-macros -Wvector-operation-performance -Wvla -Wvla-larger-than=</code><i>n</i> <code>-Wvolatile-register-var -Wwrite-strings -Wzero-as-null-pointer-constant -Whsa</code></p>
<dt><i>C and Objective-C-only Warning Options</i></p>
<dd><code>-Wbad-function-cast -Wmissing-declarations -Wmissing-parameter-type -Wmissing-prototypes -Wnested-externs -Wold-style-declaration -Wold-style-definition -Wstrict-prototypes -Wtraditional -Wtraditional-conversion -Wdeclaration-after-statement -Wpointer-sign</code></p>
<dt><i>Debugging Options</i></p>
<dd><code>-g -g</code><i>level</i> <code>-gdwarf -gdwarf-</code><i>version</i> <code>-ggdb -grecord-gcc-switches -gno-record-gcc-switches -gstabs -gstabs+ -gstrict-dwarf -gno-strict-dwarf -gas-loc-support -gno-as-loc-support -gas-locview-support -gno-as-locview-support -gcolumn-info -gno-column-info -gstatement-frontiers -gno-statement-frontiers -gvariable-location-views -gno-variable-location-views -ginternal-reset-location-views -gno-internal-reset-location-views -ginline-points -gno-inline-points -gvms -gxcoff -gxcoff+ -gz</code>[<code>=</code><i>type</i>] <code>-fdebug-prefix-map=</code><i>old</i><code>=</code><i>new</i> <code>-fdebug-types-section -fno-eliminate-unused-debug-types -femit-struct-debug-baseonly -femit-struct-debug-reduced -femit-struct-debug-detailed</code>[<code>=</code><i>spec-list</i>] <code>-feliminate-unused-debug-symbols -femit-class-debug-always -fno-merge-debug-strings -fno-dwarf2-cfi-asm -fvar-tracking -fvar-tracking-assignments</code></p>
<dt><i>Optimization Options</i></p>
<dd><code>-faggressive-loop-optimizations -falign-functions[=</code><i>n</i><code>] -falign-jumps[=</code><i>n</i><code>] -falign-labels[=</code><i>n</i><code>] -falign-loops[=</code><i>n</i><code>] -fassociative-math -fauto-profile -fauto-profile[=</code><i>path</i><code>] -fauto-inc-dec -fbranch-probabilities -fbranch-target-load-optimize -fbranch-target-load-optimize2 -fbtr-bb-exclusive -fcaller-saves -fcombine-stack-adjustments -fconserve-stack -fcompare-elim -fcprop-registers -fcrossjumping -fcse-follow-jumps -fcse-skip-blocks -fcx-fortran-rules -fcx-limited-range -fdata-sections -fdce -fdelayed-branch -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively -fdevirtualize-at-ltrans -fdse -fearly-inlining -fipa-sra -fexpensive-optimizations -ffat-lto-objects -ffast-math -ffinite-math-only -ffloat-store -fexcess-precision=</code><i>style</i> <code>-fforward-propagate -ffp-contract=</code><i>style</i> <code>-ffunction-sections -fgcse -fgcse-after-reload -fgcse-las -fgcse-lm -fgraphite-identity -fgcse-sm -fhoist-adjacent-loads -fif-conversion -fif-conversion2 -findirect-inlining -finline-functions -finline-functions-called-once -finline-limit=</code><i>n</i> <code>-finline-small-functions -fipa-cp -fipa-cp-clone -fipa-bit-cp -fipa-vrp -fipa-pta -fipa-profile -fipa-pure-const -fipa-reference -fipa-icf -fira-algorithm=</code><i>algorithm</i> <code>-fira-region=</code><i>region</i> <code>-fira-hoist-pressure -fira-loop-pressure -fno-ira-share-save-slots -fno-ira-share-spill-slots -fisolate-erroneous-paths-dereference -fisolate-erroneous-paths-attribute -fivopts -fkeep-inline-functions -fkeep-static-functions -fkeep-static-consts -flimit-function-alignment -flive-range-shrinkage -floop-block -floop-interchange -floop-strip-mine -floop-unroll-and-jam -floop-nest-optimize -floop-parallelize-all -flra-remat -flto -flto-compression-level -flto-partition=</code><i>alg</i> <code>-fmerge-all-constants -fmerge-constants -fmodulo-sched -fmodulo-sched-allow-regmoves -fmove-loop-invariants -fno-branch-count-reg -fno-defer-pop -fno-fp-int-builtin-inexact -fno-function-cse -fno-guess-branch-probability -fno-inline -fno-math-errno -fno-peephole -fno-peephole2 -fno-printf-return-value -fno-sched-interblock -fno-sched-spec -fno-signed-zeros -fno-toplevel-reorder -fno-trapping-math -fno-zero-initialized-in-bss -fomit-frame-pointer -foptimize-sibling-calls -fpartial-inlining -fpeel-loops -fpredictive-commoning -fprefetch-loop-arrays -fprofile-correction -fprofile-use -fprofile-use=</code><i>path</i> <code>-fprofile-values -fprofile-reorder-functions -freciprocal-math -free -frename-registers -freorder-blocks -freorder-blocks-algorithm=</code><i>algorithm</i> <code>-freorder-blocks-and-partition -freorder-functions -frerun-cse-after-loop -freschedule-modulo-scheduled-loops -frounding-math -fsched2-use-superblocks -fsched-pressure -fsched-spec-load -fsched-spec-load-dangerous -fsched-stalled-insns-dep[=</code><i>n</i><code>] -fsched-stalled-insns[=</code><i>n</i><code>] -fsched-group-heuristic -fsched-critical-path-heuristic -fsched-spec-insn-heuristic -fsched-rank-heuristic -fsched-last-insn-heuristic -fsched-dep-count-heuristic -fschedule-fusion -fschedule-insns -fschedule-insns2 -fsection-anchors -fselective-scheduling -fselective-scheduling2 -fsel-sched-pipelining -fsel-sched-pipelining-outer-loops -fsemantic-interposition -fshrink-wrap -fshrink-wrap-separate -fsignaling-nans -fsingle-precision-constant -fsplit-ivs-in-unroller -fsplit-loops -fsplit-paths -fsplit-wide-types -fssa-backprop -fssa-phiopt -fstdarg-opt -fstore-merging -fstrict-aliasing -fthread-jumps -ftracer -ftree-bit-ccp -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-vars -ftree-copy-prop -ftree-dce -ftree-dominator-opts -ftree-dse -ftree-forwprop -ftree-fre -fcode-hoisting -ftree-loop-if-convert -ftree-loop-im -ftree-phiprop -ftree-loop-distribution -ftree-loop-distribute-patterns -ftree-loop-ivcanon -ftree-loop-linear -ftree-loop-optimize -ftree-loop-vectorize -ftree-parallelize-loops=</code><i>n</i> <code>-ftree-pre -ftree-partial-pre -ftree-pta -ftree-reassoc -ftree-sink -ftree-slsr -ftree-sra -ftree-switch-conversion -ftree-tail-merge -ftree-ter -ftree-vectorize -ftree-vrp -funconstrained-commons -funit-at-a-time -funroll-all-loops -funroll-loops -funsafe-math-optimizations -funswitch-loops -fipa-ra -fvariable-expansion-in-unroller -fvect-cost-model -fvpt -fweb -fwhole-program -fwpa -fuse-linker-plugin &#8211;param</code> <i>name</i><code>=</code><i>value</i> <code>-O -O0 -O1 -O2 -O3 -Os -Ofast -Og</code></p>
<dt><i>Program Instrumentation Options</i></p>
<dd><code>-p -pg -fprofile-arcs &#8211;coverage -ftest-coverage -fprofile-abs-path -fprofile-dir=</code><i>path</i> <code>-fprofile-generate -fprofile-generate=</code><i>path</i> <code>-fsanitize=</code><i>style</i> <code>-fsanitize-recover -fsanitize-recover=</code><i>style</i> <code>-fasan-shadow-offset=</code><i>number</i> <code>-fsanitize-sections=</code><i>s1</i><code>,</code><i>s2</i><code>,&#8230; -fsanitize-undefined-trap-on-error -fbounds-check -fcheck-pointer-bounds -fchkp-check-incomplete-type -fchkp-first-field-has-own-bounds -fchkp-narrow-bounds -fchkp-narrow-to-innermost-array -fchkp-optimize -fchkp-use-fast-string-functions -fchkp-use-nochk-string-functions -fchkp-use-static-bounds -fchkp-use-static-const-bounds -fchkp-treat-zero-dynamic-size-as-infinite -fchkp-check-read -fchkp-check-read -fchkp-check-write -fchkp-store-bounds -fchkp-instrument-calls -fchkp-instrument-marked-only -fchkp-use-wrappers -fchkp-flexible-struct-trailing-arrays -fcf-protection=</code>[<code>full</code>|<code>branch</code>|<code>return</code>|<code>none</code>] <code>-fstack-protector -fstack-protector-all -fstack-protector-strong -fstack-protector-explicit -fstack-check -fstack-limit-register=</code><i>reg</i> <code>-fstack-limit-symbol=</code><i>sym</i> <code>-fno-stack-limit -fsplit-stack -fvtable-verify=</code>[<code>std</code>|<code>preinit</code>|<code>none</code>] <code>-fvtv-counts -fvtv-debug -finstrument-functions -finstrument-functions-exclude-function-list=</code><i>sym</i><code>,</code><i>sym</i><code>,&#8230; -finstrument-functions-exclude-file-list=</code><i>file</i><code>,</code><i>file</i><code>,&#8230;</code></p>
<dt><i>Preprocessor Options</i></p>
<dd><code>-A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -CC -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-dD -dI -dM -dN -dU -fdebug-cpp -fdirectives-only -fdollars-in-identifiers -fexec-charset=</code><i>charset</i> <code>-fextended-identifiers -finput-charset=</code><i>charset</i> <code>-fmacro-prefix-map=</code><i>old</i><code>=</code><i>new</i> <code>-fno-canonical-system-headers -fpch-deps -fpch-preprocess -fpreprocessed -ftabstop=</code><i>width</i> <code>-ftrack-macro-expansion -fwide-exec-charset=</code><i>charset</i> <code>-fworking-directory -H -imacros</code> <i>file</i> <code>-include</code> <i>file</i> <code>-M -MD -MF -MG -MM -MMD -MP -MQ -MT -no-integrated-cpp -P -pthread -remap -traditional -traditional-cpp -trigraphs -U</code><i>macro</i> <code>-undef -Wp,</code><i>option</i> <code>-Xpreprocessor</code> <i>option</i></p>
<dt><i>Assembler Options</i></p>
<dd><code>-Wa,</code><i>option</i> <code>-Xassembler</code> <i>option</i></p>
<dt><i>Linker Options</i></p>
<dd><i>object-file-name</i> <code>-fuse-ld=</code><i>linker</i> <code>-l</code><i>library</i> <code>-nostartfiles -nodefaultlibs -nostdlib -pie -pthread -rdynamic -s -static -static-pie -static-libgcc -static-libstdc++ -static-libasan -static-libtsan -static-liblsan -static-libubsan -static-libmpx -static-libmpxwrappers -shared -shared-libgcc -symbolic -T</code> <i>script</i> <code>-Wl,</code><i>option</i> <code>-Xlinker</code> <i>option</i> <code>-u</code> <i>symbol</i> <code>-z</code> <i>keyword</i></p>
<dt><i>Directory Options</i></p>
<dd><code>-B</code><i>prefix</i> <code>-I</code><i>dir</i> <code>-I- -idirafter</code> <i>dir</i> <code>-imacros</code> <i>file</i> <code>-imultilib</code> <i>dir</i> <code>-iplugindir=</code><i>dir</i> <code>-iprefix</code> <i>file</i> <code>-iquote</code> <i>dir</i> <code>-isysroot</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-iwithprefix</code> <i>dir</i> <code>-iwithprefixbefore</code> <i>dir</i> <code>-L</code><i>dir</i> <code>-no-canonical-prefixes &#8211;no-sysroot-suffix -nostdinc -nostdinc++ &#8211;sysroot=</code><i>dir</i></p>
<dt><i>Code Generation Options</i></p>
<dd><code>-fcall-saved-</code><i>reg</i> <code>-fcall-used-</code><i>reg</i> <code>-ffixed-</code><i>reg</i> <code>-fexceptions -fnon-call-exceptions -fdelete-dead-exceptions -funwind-tables -fasynchronous-unwind-tables -fno-gnu-unique -finhibit-size-directive -fno-common -fno-ident -fpcc-struct-return -fpic -fPIC -fpie -fPIE -fno-plt -fno-jump-tables -frecord-gcc-switches -freg-struct-return -fshort-enums -fshort-wchar -fverbose-asm -fpack-struct[=</code><i>n</i><code>] -fleading-underscore -ftls-model=</code><i>model</i> <code>-fstack-reuse=</code><i>reuse_level</i> <code>-ftrampolines -ftrapv -fwrapv -fvisibility=</code>[<code>default</code>|<code>internal</code>|<code>hidden</code>|<code>protected</code>] <code>-fstrict-volatile-bitfields -fsync-libcalls</code></p>
<dt><i>Developer Options</i></p>
<dd><code>-d</code><i>letters</i> <code>-dumpspecs -dumpmachine -dumpversion -dumpfullversion -fchecking -fchecking=</code><i>n</i> <code>-fdbg-cnt-list -fdbg-cnt=</code><i>counter-value-list</i> <code>-fdisable-ipa-</code><i>pass_name</i> <code>-fdisable-rtl-</code><i>pass_name</i> <code>-fdisable-rtl-</code><i>pass-name</i><code>=</code><i>range-list</i> <code>-fdisable-tree-</code><i>pass_name</i> <code>-fdisable-tree-</code><i>pass-name</i><code>=</code><i>range-list</i> <code>-fdump-noaddr -fdump-unnumbered -fdump-unnumbered-links -fdump-final-insns</code>[<code>=</code><i>file</i>] <code>-fdump-ipa-all -fdump-ipa-cgraph -fdump-ipa-inline -fdump-lang-all -fdump-lang-</code><i>switch</i> <code>-fdump-lang-</code><i>switch</i><code>&#8211;</code><i>options</i> <code>-fdump-lang-</code><i>switch</i><code>&#8211;</code><i>options</i><code>=</code><i>filename</i> <code>-fdump-passes -fdump-rtl-</code><i>pass</i> <code>-fdump-rtl-</code><i>pass</i><code>=</code><i>filename</i> <code>-fdump-statistics -fdump-tree-all -fdump-tree-</code><i>switch</i> <code>-fdump-tree-</code><i>switch</i><code>&#8211;</code><i>options</i> <code>-fdump-tree-</code><i>switch</i><code>&#8211;</code><i>options</i><code>=</code><i>filename</i> <code>-fcompare-debug</code>[<code>=</code><i>opts</i>] <code>-fcompare-debug-second -fenable-</code><i>kind</i><code>&#8211;</code><i>pass</i> <code>-fenable-</code><i>kind</i><code>&#8211;</code><i>pass</i><code>=</code><i>range-list</i> <code>-fira-verbose=</code><i>n</i> <code>-flto-report -flto-report-wpa -fmem-report-wpa -fmem-report -fpre-ipa-mem-report -fpost-ipa-mem-report -fopt-info -fopt-info-</code><i>options</i>[<code>=</code><i>file</i>] <code>-fprofile-report -frandom-seed=</code><i>string</i> <code>-fsched-verbose=</code><i>n</i> <code>-fsel-sched-verbose -fsel-sched-dump-cfg -fsel-sched-pipelining-verbose -fstats -fstack-usage -ftime-report -ftime-report-details -fvar-tracking-assignments-toggle -gtoggle -print-file-name=</code><i>library</i> <code>-print-libgcc-file-name -print-multi-directory -print-multi-lib -print-multi-os-directory -print-prog-name=</code><i>program</i> <code>-print-search-dirs -Q -print-sysroot -print-sysroot-headers-suffix -save-temps -save-temps=cwd -save-temps=obj -time</code>[<code>=</code><i>file</i>]</p>
<dt><i>Machine-Dependent Options</i></p>
<dd><i>AArch64 Options</i> <code>-mabi=</code><i>name</i> <code>-mbig-endian -mlittle-endian -mgeneral-regs-only -mcmodel=tiny -mcmodel=small -mcmodel=large -mstrict-align -momit-leaf-frame-pointer -mtls-dialect=desc -mtls-dialect=traditional -mtls-size=</code><i>size</i> <code>-mfix-cortex-a53-835769 -mfix-cortex-a53-843419 -mlow-precision-recip-sqrt -mlow-precision-sqrt -mlow-precision-div -mpc-relative-literal-loads -msign-return-address=</code><i>scope</i> <code>-march=</code><i>name</i> <code>-mcpu=</code><i>name</i> <code>-mtune=</code><i>name</i> <code>-moverride=</code><i>string</i> <code>-mverbose-cost-dump</code> </p>
<p> <i>Adapteva Epiphany Options</i> <code>-mhalf-reg-file -mprefer-short-insn-regs -mbranch-cost=</code><i>num</i> <code>-mcmove -mnops=</code><i>num</i> <code>-msoft-cmpsf -msplit-lohi -mpost-inc -mpost-modify -mstack-offset=</code><i>num</i> <code>-mround-nearest -mlong-calls -mshort-calls -msmall16 -mfp-mode=</code><i>mode</i> <code>-mvect-double -max-vect-align=</code><i>num</i> <code>-msplit-vecmove-early -m1reg-</code><i>reg</i> </p>
<p> <i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i> <code>-mbarrel-shifter -mjli-always -mcpu=</code><i>cpu</i> <code>-mA6 -mARC600 -mA7 -mARC700 -mdpfp -mdpfp-compact -mdpfp-fast -mno-dpfp-lrsr -mea -mno-mpy -mmul32x16 -mmul64 -matomic -mnorm -mspfp -mspfp-compact -mspfp-fast -msimd -msoft-float -mswap -mcrc -mdsp-packa -mdvbf -mlock -mmac-d16 -mmac-24 -mrtsc -mswape -mtelephony -mxy -misize -mannotate-align -marclinux -marclinux_prof -mlong-calls -mmedium-calls -msdata -mirq-ctrl-saved -mrgf-banked-regs -mlpc-width=</code><i>width</i> <code>-G</code> <i>num</i> <code>-mvolatile-cache -mtp-regno=</code><i>regno</i> <code>-malign-call -mauto-modify-reg -mbbit-peephole -mno-brcc -mcase-vector-pcrel -mcompact-casesi -mno-cond-exec -mearly-cbranchsi -mexpand-adddi -mindexed-loads -mlra -mlra-priority-none -mlra-priority-compact mlra-priority-noncompact -mno-millicode -mmixed-code -mq-class -mRcq -mRcw -msize-level=</code><i>level</i> <code>-mtune=</code><i>cpu</i> <code>-mmultcost=</code><i>num</i> <code>-munalign-prob-threshold=</code><i>probability</i> <code>-mmpy-option=</code><i>multo</i> <code>-mdiv-rem -mcode-density -mll64 -mfpu=</code><i>fpu</i> <code>-mrf16</code> </p>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i> <code>-mapcs-frame -mno-apcs-frame -mabi=</code><i>name</i> <code>-mapcs-stack-check -mno-apcs-stack-check -mapcs-reentrant -mno-apcs-reentrant -msched-prolog -mno-sched-prolog -mlittle-endian -mbig-endian -mbe8 -mbe32 -mfloat-abi=</code><i>name</i> <code>-mfp16-format=</code><i>name</i> <code>-mthumb-interwork -mno-thumb-interwork -mcpu=</code><i>name</i> <code>-march=</code><i>name</i> <code>-mfpu=</code><i>name</i> <code>-mtune=</code><i>name</i> <code>-mprint-tune-info -mstructure-size-boundary=</code><i>n</i> <code>-mabort-on-noreturn -mlong-calls -mno-long-calls -msingle-pic-base -mno-single-pic-base -mpic-register=</code><i>reg</i> <code>-mnop-fun-dllimport -mpoke-function-name -mthumb -marm -mflip-thumb -mtpcs-frame -mtpcs-leaf-frame -mcaller-super-interworking -mcallee-super-interworking -mtp=</code><i>name</i> <code>-mtls-dialect=</code><i>dialect</i> <code>-mword-relocations -mfix-cortex-m3-ldrd -munaligned-access -mneon-for-64bits -mslow-flash-data -masm-syntax-unified -mrestrict-it -mverbose-cost-dump -mpure-code -mcmse</code> </p>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i> <code>-mmcu=</code><i>mcu</i> <code>-mabsdata -maccumulate-args -mbranch-cost=</code><i>cost</i> <code>-mcall-prologues -mgas-isr-prologues -mint8 -mn_flash=</code><i>size</i> <code>-mno-interrupts -mmain-is-OS_task -mrelax -mrmw -mstrict-X -mtiny-stack -mfract-convert-truncate -mshort-calls -nodevicelib -nodevicespecs -Waddr-space-convert -Wmisspelled-isr</code> </p>
<p> <i>Blackfin Options</i> <code>-mcpu=</code><i>cpu</i>[<code>&#8211;</code><i>sirevision</i>] <code>-msim -momit-leaf-frame-pointer -mno-omit-leaf-frame-pointer -mspecld-anomaly -mno-specld-anomaly -mcsync-anomaly -mno-csync-anomaly -mlow-64k -mno-low64k -mstack-check-l1 -mid-shared-library -mno-id-shared-library -mshared-library-id=</code><i>n</i> <code>-mleaf-id-shared-library -mno-leaf-id-shared-library -msep-data -mno-sep-data -mlong-calls -mno-long-calls -mfast-fp -minline-plt -mmulticore -mcorea -mcoreb -msdram -micplb</code> </p>
<p> <i>C6X Options</i> <code>-mbig-endian -mlittle-endian -march=</code><i>cpu</i> <code>-msim -msdata=</code><i>sdata-type</i> </p>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i> <code>-mcpu=</code><i>cpu</i> <code>-march=</code><i>cpu</i> <code>-mtune=</code><i>cpu</i> <code>-mmax-stack-frame=</code><i>n</i> <code>-melinux-stacksize=</code><i>n</i> <code>-metrax4 -metrax100 -mpdebug -mcc-init -mno-side-effects -mstack-align -mdata-align -mconst-align -m32-bit -m16-bit -m8-bit -mno-prologue-epilogue -mno-gotplt -melf -maout -melinux -mlinux -sim -sim2 -mmul-bug-workaround -mno-mul-bug-workaround</code> </p>
<p> <i></i><font SIZE="-1"><i>CR16</i></font><i> Options</i> <code>-mmac -mcr16cplus -mcr16c -msim -mint32 -mbit-ops -mdata-model=</code><i>model</i> </p>
<p> <i>Darwin Options</i> <code>-all_load -allowable_client -arch -arch_errors_fatal -arch_only -bind_at_load -bundle -bundle_loader -client_name -compatibility_version -current_version -dead_strip -dependency-file -dylib_file -dylinker_install_name -dynamic -dynamiclib -exported_symbols_list -filelist -flat_namespace -force_cpusubtype_ALL -force_flat_namespace -headerpad_max_install_names -iframework -image_base -init -install_name -keep_private_externs -multi_module -multiply_defined -multiply_defined_unused -noall_load -no_dead_strip_inits_and_terms -nofixprebinding -nomultidefs -noprebind -noseglinkedit -pagezero_size -prebind -prebind_all_twolevel_modules -private_bundle -read_only_relocs -sectalign -sectobjectsymbols -whyload -seg1addr -sectcreate -sectobjectsymbols -sectorder -segaddr -segs_read_only_addr -segs_read_write_addr -seg_addr_table -seg_addr_table_filename -seglinkedit -segprot -segs_read_only_addr -segs_read_write_addr -single_module -static -sub_library -sub_umbrella -twolevel_namespace -umbrella -undefined -unexported_symbols_list -weak_reference_mismatches -whatsloaded -F -gused -gfull -mmacosx-version-min=</code><i>version</i> <code>-mkernel -mone-byte-bool</code> </p>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha Options</i> <code>-mno-fp-regs -msoft-float -mieee -mieee-with-inexact -mieee-conformant -mfp-trap-mode=</code><i>mode</i> <code>-mfp-rounding-mode=</code><i>mode</i> <code>-mtrap-precision=</code><i>mode</i> <code>-mbuild-constants -mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mbwx -mmax -mfix -mcix -mfloat-vax -mfloat-ieee -mexplicit-relocs -msmall-data -mlarge-data -msmall-text -mlarge-text -mmemory-latency=</code><i>time</i> </p>
<p> <i></i><font SIZE="-1"><i>FR30</i></font><i> Options</i> <code>-msmall-model -mno-lsim</code> </p>
<p> <i></i><font SIZE="-1"><i>FT32</i></font><i> Options</i> <code>-msim -mlra -mnodiv -mft32b -mcompress -mnopm</code> </p>
<p> <i></i><font SIZE="-1"><i>FRV</i></font><i> Options</i> <code>-mgpr-32 -mgpr-64 -mfpr-32 -mfpr-64 -mhard-float -msoft-float -malloc-cc -mfixed-cc -mdword -mno-dword -mdouble -mno-double -mmedia -mno-media -mmuladd -mno-muladd -mfdpic -minline-plt -mgprel-ro -multilib-library-pic -mlinked-fp -mlong-calls -malign-labels -mlibrary-pic -macc-4 -macc-8 -mpack -mno-pack -mno-eflags -mcond-move -mno-cond-move -moptimize-membar -mno-optimize-membar -mscc -mno-scc -mcond-exec -mno-cond-exec -mvliw-branch -mno-vliw-branch -mmulti-cond-exec -mno-multi-cond-exec -mnested-cond-exec -mno-nested-cond-exec -mtomcat-stats -mTLS -mtls -mcpu=</code><i>cpu</i> </p>
<p> <i>GNU/Linux Options</i> <code>-mglibc -muclibc -mmusl -mbionic -mandroid -tno-android-cc -tno-android-ld</code> </p>
<p> <i>H8/300 Options</i> <code>-mrelax -mh -ms -mn -mexr -mno-exr -mint32 -malign-300</code> </p>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i> <code>-march=</code><i>architecture-type</i> <code>-mcaller-copies -mdisable-fpregs -mdisable-indexing -mfast-indirect-calls -mgas -mgnu-ld -mhp-ld -mfixed-range=</code><i>register-range</i> <code>-mjump-in-delay -mlinker-opt -mlong-calls -mlong-load-store -mno-disable-fpregs -mno-disable-indexing -mno-fast-indirect-calls -mno-gas -mno-jump-in-delay -mno-long-load-store -mno-portable-runtime -mno-soft-float -mno-space-regs -msoft-float -mpa-risc-1-0 -mpa-risc-1-1 -mpa-risc-2-0 -mportable-runtime -mschedule=</code><i>cpu-type</i> <code>-mspace-regs -msio -mwsio -munix=</code><i>unix-std</i> <code>-nolibdld -static -threads</code> </p>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i> <code>-mbig-endian -mlittle-endian -mgnu-as -mgnu-ld -mno-pic -mvolatile-asm-stop -mregister-names -msdata -mno-sdata -mconstant-gp -mauto-pic -mfused-madd -minline-float-divide-min-latency -minline-float-divide-max-throughput -mno-inline-float-divide -minline-int-divide-min-latency -minline-int-divide-max-throughput -mno-inline-int-divide -minline-sqrt-min-latency -minline-sqrt-max-throughput -mno-inline-sqrt -mdwarf2-asm -mearly-stop-bits -mfixed-range=</code><i>register-range</i> <code>-mtls-size=</code><i>tls-size</i> <code>-mtune=</code><i>cpu-type</i> <code>-milp32 -mlp64 -msched-br-data-spec -msched-ar-data-spec -msched-control-spec -msched-br-in-data-spec -msched-ar-in-data-spec -msched-in-control-spec -msched-spec-ldc -msched-spec-control-ldc -msched-prefer-non-data-spec-insns -msched-prefer-non-control-spec-insns -msched-stop-bits-after-every-cycle -msched-count-spec-in-critical-path -msel-sched-dont-check-control-spec -msched-fp-mem-deps-zero-cost -msched-max-memory-insns-hard-limit -msched-max-memory-insns=</code><i>max-insns</i> </p>
<p> <i></i><font SIZE="-1"><i>LM32</i></font><i> Options</i> <code>-mbarrel-shift-enabled -mdivide-enabled -mmultiply-enabled -msign-extend-enabled -muser-enabled</code> </p>
<p> <i>M32R/D Options</i> <code>-m32r2 -m32rx -m32r -mdebug -malign-loops -mno-align-loops -missue-rate=</code><i>number</i> <code>-mbranch-cost=</code><i>number</i> <code>-mmodel=</code><i>code-size-model-type</i> <code>-msdata=</code><i>sdata-type</i> <code>-mno-flush-func -mflush-func=</code><i>name</i> <code>-mno-flush-trap -mflush-trap=</code><i>number</i> <code>-G</code> <i>num</i> </p>
<p> <i>M32C Options</i> <code>-mcpu=</code><i>cpu</i> <code>-msim -memregs=</code><i>number</i> </p>
<p> <i>M680x0 Options</i> <code>-march=</code><i>arch</i> <code>-mcpu=</code><i>cpu</i> <code>-mtune=</code><i>tune</i> <code>-m68000 -m68020 -m68020-40 -m68020-60 -m68030 -m68040 -m68060 -mcpu32 -m5200 -m5206e -m528x -m5307 -m5407 -mcfv4e -mbitfield -mno-bitfield -mc68000 -mc68020 -mnobitfield -mrtd -mno-rtd -mdiv -mno-div -mshort -mno-short -mhard-float -m68881 -msoft-float -mpcrel -malign-int -mstrict-align -msep-data -mno-sep-data -mshared-library-id=n -mid-shared-library -mno-id-shared-library -mxgot -mno-xgot -mlong-jump-table-offsets</code> </p>
<p> <i>MCore Options</i> <code>-mhardlit -mno-hardlit -mdiv -mno-div -mrelax-immediates -mno-relax-immediates -mwide-bitfields -mno-wide-bitfields -m4byte-functions -mno-4byte-functions -mcallgraph-data -mno-callgraph-data -mslow-bytes -mno-slow-bytes -mno-lsim -mlittle-endian -mbig-endian -m210 -m340 -mstack-increment</code> </p>
<p> <i>MeP Options</i> <code>-mabsdiff -mall-opts -maverage -mbased=</code><i>n</i> <code>-mbitops -mc=</code><i>n</i> <code>-mclip -mconfig=</code><i>name</i> <code>-mcop -mcop32 -mcop64 -mivc2 -mdc -mdiv -meb -mel -mio-volatile -ml -mleadz -mm -mminmax -mmult -mno-opts -mrepeat -ms -msatur -msdram -msim -msimnovec -mtf -mtiny=</code><i>n</i> </p>
<p> <i>MicroBlaze Options</i> <code>-msoft-float -mhard-float -msmall-divides -mcpu=</code><i>cpu</i> <code>-mmemcpy -mxl-soft-mul -mxl-soft-div -mxl-barrel-shift -mxl-pattern-compare -mxl-stack-check -mxl-gp-opt -mno-clearbss -mxl-multiply-high -mxl-float-convert -mxl-float-sqrt -mbig-endian -mlittle-endian -mxl-reorder -mxl-mode-</code><i>app-model</i> </p>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i> <code>-EL -EB -march=</code><i>arch</i> <code>-mtune=</code><i>arch</i> <code>-mips1 -mips2 -mips3 -mips4 -mips32 -mips32r2 -mips32r3 -mips32r5 -mips32r6 -mips64 -mips64r2 -mips64r3 -mips64r5 -mips64r6 -mips16 -mno-mips16 -mflip-mips16 -minterlink-compressed -mno-interlink-compressed -minterlink-mips16 -mno-interlink-mips16 -mabi=</code><i>abi</i> <code>-mabicalls -mno-abicalls -mshared -mno-shared -mplt -mno-plt -mxgot -mno-xgot -mgp32 -mgp64 -mfp32 -mfpxx -mfp64 -mhard-float -msoft-float -mno-float -msingle-float -mdouble-float -modd-spreg -mno-odd-spreg -mabs=</code><i>mode</i> <code>-mnan=</code><i>encoding</i> <code>-mdsp -mno-dsp -mdspr2 -mno-dspr2 -mmcu -mmno-mcu -meva -mno-eva -mvirt -mno-virt -mxpa -mno-xpa -mmicromips -mno-micromips -mmsa -mno-msa -mfpu=</code><i>fpu-type</i> <code>-msmartmips -mno-smartmips -mpaired-single -mno-paired-single -mdmx -mno-mdmx -mips3d -mno-mips3d -mmt -mno-mt -mllsc -mno-llsc -mlong64 -mlong32 -msym32 -mno-sym32 -G</code><i>num</i> <code>-mlocal-sdata -mno-local-sdata -mextern-sdata -mno-extern-sdata -mgpopt -mno-gopt -membedded-data -mno-embedded-data -muninit-const-in-rodata -mno-uninit-const-in-rodata -mcode-readable=</code><i>setting</i> <code>-msplit-addresses -mno-split-addresses -mexplicit-relocs -mno-explicit-relocs -mcheck-zero-division -mno-check-zero-division -mdivide-traps -mdivide-breaks -mload-store-pairs -mno-load-store-pairs -mmemcpy -mno-memcpy -mlong-calls -mno-long-calls -mmad -mno-mad -mimadd -mno-imadd -mfused-madd -mno-fused-madd -nocpp -mfix-24k -mno-fix-24k -mfix-r4000 -mno-fix-r4000 -mfix-r4400 -mno-fix-r4400 -mfix-r10000 -mno-fix-r10000 -mfix-rm7000 -mno-fix-rm7000 -mfix-vr4120 -mno-fix-vr4120 -mfix-vr4130 -mno-fix-vr4130 -mfix-sb1 -mno-fix-sb1 -mflush-func=</code><i>func</i> <code>-mno-flush-func -mbranch-cost=</code><i>num</i> <code>-mbranch-likely -mno-branch-likely -mcompact-branches=</code><i>policy</i> <code>-mfp-exceptions -mno-fp-exceptions -mvr4130-align -mno-vr4130-align -msynci -mno-synci -mlxc1-sxc1 -mno-lxc1-sxc1 -mmadd4 -mno-madd4 -mrelax-pic-calls -mno-relax-pic-calls -mmcount-ra-address -mframe-header-opt -mno-frame-header-opt</code> </p>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i> <code>-mlibfuncs -mno-libfuncs -mepsilon -mno-epsilon -mabi=gnu -mabi=mmixware -mzero-extend -mknuthdiv -mtoplevel-symbols -melf -mbranch-predict -mno-branch-predict -mbase-addresses -mno-base-addresses -msingle-exit -mno-single-exit</code> </p>
<p> <i></i><font SIZE="-1"><i>MN10300</i></font><i> Options</i> <code>-mmult-bug -mno-mult-bug -mno-am33 -mam33 -mam33-2 -mam34 -mtune=</code><i>cpu-type</i> <code>-mreturn-pointer-on-d0 -mno-crt0 -mrelax -mliw -msetlb</code> </p>
<p> <i>Moxie Options</i> <code>-meb -mel -mmul.x -mno-crt0</code> </p>
<p> <i></i><font SIZE="-1"><i>MSP430</i></font><i> Options</i> <code>-msim -masm-hex -mmcu= -mcpu= -mlarge -msmall -mrelax -mwarn-mcu -mcode-region= -mdata-region= -msilicon-errata= -msilicon-errata-warn= -mhwmult= -minrt</code> </p>
<p> <i></i><font SIZE="-1"><i>NDS32</i></font><i> Options</i> <code>-mbig-endian -mlittle-endian -mreduced-regs -mfull-regs -mcmov -mno-cmov -mext-perf -mno-ext-perf -mext-perf2 -mno-ext-perf2 -mext-string -mno-ext-string -mv3push -mno-v3push -m16bit -mno-16bit -misr-vector-size=</code><i>num</i> <code>-mcache-block-size=</code><i>num</i> <code>-march=</code><i>arch</i> <code>-mcmodel=</code><i>code-model</i> <code>-mctor-dtor -mrelax</code> </p>
<p> <i>Nios </i><font SIZE="-1"><i>II</i></font><i> Options</i> <code>-G</code> <i>num</i> <code>-mgpopt=</code><i>option</i> <code>-mgpopt -mno-gpopt -mgprel-sec=</code><i>regexp</i> <code>-mr0rel-sec=</code><i>regexp</i> <code>-mel -meb -mno-bypass-cache -mbypass-cache -mno-cache-volatile -mcache-volatile -mno-fast-sw-div -mfast-sw-div -mhw-mul -mno-hw-mul -mhw-mulx -mno-hw-mulx -mno-hw-div -mhw-div -mcustom-</code><i>insn</i><code>=</code><i>N</i> <code>-mno-custom-</code><i>insn</i> <code>-mcustom-fpu-cfg=</code><i>name</i> <code>-mhal -msmallc -msys-crt0=</code><i>name</i> <code>-msys-lib=</code><i>name</i> <code>-march=</code><i>arch</i> <code>-mbmx -mno-bmx -mcdx -mno-cdx</code> </p>
<p> <i>Nvidia </i><font SIZE="-1"><i>PTX</i></font><i> Options</i> <code>-m32 -m64 -mmainkernel -moptimize</code> </p>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i> <code>-mfpu -msoft-float -mac0 -mno-ac0 -m40 -m45 -m10 -mbcopy -mbcopy-builtin -mint32 -mno-int16 -mint16 -mno-int32 -mfloat32 -mno-float64 -mfloat64 -mno-float32 -mabshi -mno-abshi -mbranch-expensive -mbranch-cheap -munix-asm -mdec-asm</code> </p>
<p> <i>picoChip Options</i> <code>-mae=</code><i>ae_type</i> <code>-mvliw-lookahead=</code><i>N</i> <code>-msymbol-as-address -mno-inefficient-warnings</code> </p>
<p> <i>PowerPC Options</i> See <font SIZE="-1">RS/6000</font> and PowerPC Options. </p>
<p> <i>PowerPC </i><font SIZE="-1"><i>SPE</i></font><i> Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mmfcrf -mno-mfcrf -mpopcntb -mno-popcntb -mfull-toc -mminimal-toc -mno-fp-in-toc -mno-sum-in-toc -m32 -mxl-compat -mno-xl-compat -malign-power -malign-natural -msoft-float -mhard-float -mmultiple -mno-multiple -msingle-float -mdouble-float -mupdate -mno-update -mavoid-indexed-addresses -mno-avoid-indexed-addresses -mstrict-align -mno-strict-align -mrelocatable -mno-relocatable -mrelocatable-lib -mno-relocatable-lib -mtoc -mno-toc -mlittle -mlittle-endian -mbig -mbig-endian -msingle-pic-base -mprioritize-restricted-insns=</code><i>priority</i> <code>-msched-costly-dep=</code><i>dependence_type</i> <code>-minsert-sched-nops=</code><i>scheme</i> <code>-mcall-sysv -mcall-netbsd -maix-struct-return -msvr4-struct-return -mabi=</code><i>abi-type</i> <code>-msecure-plt -mbss-plt -mblock-move-inline-limit=</code><i>num</i> <code>-misel -mno-isel -misel=yes -misel=no -mspe -mno-spe -mspe=yes -mspe=no -mfloat-gprs=yes -mfloat-gprs=no -mfloat-gprs=single -mfloat-gprs=double -mprototype -mno-prototype -msim -mmvme -mads -myellowknife -memb -msdata -msdata=</code><i>opt</i> <code>-mvxworks -G</code> <i>num</i> <code>-mrecip -mrecip=</code><i>opt</i> <code>-mno-recip -mrecip-precision -mno-recip-precision -mpointers-to-nested-functions -mno-pointers-to-nested-functions -msave-toc-indirect -mno-save-toc-indirect -mcompat-align-parm -mno-compat-align-parm -mfloat128 -mno-float128 -mgnu-attribute -mno-gnu-attribute -mstack-protector-guard=</code><i>guard</i> <code>-mstack-protector-guard-reg=</code><i>reg</i> <code>-mstack-protector-guard-offset=</code><i>offset</i> </p>
<p> <i>RISC-V Options</i> <code>-mbranch-cost=</code><i>N-instruction</i> <code>-mplt -mno-plt -mabi=</code><i>ABI-string</i> <code>-mfdiv -mno-fdiv -mdiv -mno-div -march=</code><i>ISA-string</i> <code>-mtune=</code><i>processor-string</i> <code>-mpreferred-stack-boundary=</code><i>num</i> <code>-msmall-data-limit=</code><i>N-bytes</i> <code>-msave-restore -mno-save-restore -mstrict-align -mno-strict-align -mcmodel=medlow -mcmodel=medany -mexplicit-relocs -mno-explicit-relocs -mrelax -mno-relax</code> </p>
<p> <i></i><font SIZE="-1"><i>RL78</i></font><i> Options</i> <code>-msim -mmul=none -mmul=g13 -mmul=g14 -mallregs -mcpu=g10 -mcpu=g13 -mcpu=g14 -mg10 -mg13 -mg14 -m64bit-doubles -m32bit-doubles -msave-mduc-in-interrupts</code> </p>
<p> <i></i><font SIZE="-1"><i>RS/6000</i></font><i> and PowerPC Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mcmodel=</code><i>code-model</i> <code>-mpowerpc64 -maltivec -mno-altivec -mpowerpc-gpopt -mno-powerpc-gpopt -mpowerpc-gfxopt -mno-powerpc-gfxopt -mmfcrf -mno-mfcrf -mpopcntb -mno-popcntb -mpopcntd -mno-popcntd -mfprnd -mno-fprnd -mcmpb -mno-cmpb -mmfpgpr -mno-mfpgpr -mhard-dfp -mno-hard-dfp -mfull-toc -mminimal-toc -mno-fp-in-toc -mno-sum-in-toc -m64 -m32 -mxl-compat -mno-xl-compat -mpe -malign-power -malign-natural -msoft-float -mhard-float -mmultiple -mno-multiple -msingle-float -mdouble-float -msimple-fpu -mupdate -mno-update -mavoid-indexed-addresses -mno-avoid-indexed-addresses -mfused-madd -mno-fused-madd -mbit-align -mno-bit-align -mstrict-align -mno-strict-align -mrelocatable -mno-relocatable -mrelocatable-lib -mno-relocatable-lib -mtoc -mno-toc -mlittle -mlittle-endian -mbig -mbig-endian -mdynamic-no-pic -maltivec -mswdiv -msingle-pic-base -mprioritize-restricted-insns=</code><i>priority</i> <code>-msched-costly-dep=</code><i>dependence_type</i> <code>-minsert-sched-nops=</code><i>scheme</i> <code>-mcall-aixdesc -mcall-eabi -mcall-freebsd -mcall-linux -mcall-netbsd -mcall-openbsd -mcall-sysv -mcall-sysv-eabi -mcall-sysv-noeabi -mtraceback=</code><i>traceback_type</i> <code>-maix-struct-return -msvr4-struct-return -mabi=</code><i>abi-type</i> <code>-msecure-plt -mbss-plt -mblock-move-inline-limit=</code><i>num</i> <code>-mblock-compare-inline-limit=</code><i>num</i> <code>-mblock-compare-inline-loop-limit=</code><i>num</i> <code>-mstring-compare-inline-limit=</code><i>num</i> <code>-misel -mno-isel -misel=yes -misel=no -mpaired -mvrsave -mno-vrsave -mmulhw -mno-mulhw -mdlmzb -mno-dlmzb -mprototype -mno-prototype -msim -mmvme -mads -myellowknife -memb -msdata -msdata=</code><i>opt</i> <code>-mreadonly-in-sdata -mvxworks -G</code> <i>num</i> <code>-mrecip -mrecip=</code><i>opt</i> <code>-mno-recip -mrecip-precision -mno-recip-precision -mveclibabi=</code><i>type</i> <code>-mfriz -mno-friz -mpointers-to-nested-functions -mno-pointers-to-nested-functions -msave-toc-indirect -mno-save-toc-indirect -mpower8-fusion -mno-mpower8-fusion -mpower8-vector -mno-power8-vector -mcrypto -mno-crypto -mhtm -mno-htm -mquad-memory -mno-quad-memory -mquad-memory-atomic -mno-quad-memory-atomic -mcompat-align-parm -mno-compat-align-parm -mfloat128 -mno-float128 -mfloat128-hardware -mno-float128-hardware -mgnu-attribute -mno-gnu-attribute -mstack-protector-guard=</code><i>guard</i> <code>-mstack-protector-guard-reg=</code><i>reg</i> <code>-mstack-protector-guard-offset=</code><i>offset</i> </p>
<p> <i></i><font SIZE="-1"><i>RX</i></font><i> Options</i> <code>-m64bit-doubles -m32bit-doubles -fpu -nofpu -mcpu= -mbig-endian-data -mlittle-endian-data -msmall-data -msim -mno-sim -mas100-syntax -mno-as100-syntax -mrelax -mmax-constant-size= -mint-register= -mpid -mallow-string-insns -mno-allow-string-insns -mjsr -mno-warn-multiple-fast-interrupts -msave-acc-in-interrupts</code> </p>
<p> <i>S/390 and zSeries Options</i> <code>-mtune=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mhard-float -msoft-float -mhard-dfp -mno-hard-dfp -mlong-double-64 -mlong-double-128 -mbackchain -mno-backchain -mpacked-stack -mno-packed-stack -msmall-exec -mno-small-exec -mmvcle -mno-mvcle -m64 -m31 -mdebug -mno-debug -mesa -mzarch -mhtm -mvx -mzvector -mtpf-trace -mno-tpf-trace -mfused-madd -mno-fused-madd -mwarn-framesize -mwarn-dynamicstack -mstack-size -mstack-guard -mhotpatch=</code><i>halfwords</i><code>,</code><i>halfwords</i> </p>
<p> <i>Score Options</i> <code>-meb -mel -mnhwloop -muls -mmac -mscore5 -mscore5u -mscore7 -mscore7d</code> </p>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i> <code>-m1 -m2 -m2e -m2a-nofpu -m2a-single-only -m2a-single -m2a -m3 -m3e -m4-nofpu -m4-single-only -m4-single -m4 -m4a-nofpu -m4a-single-only -m4a-single -m4a -m4al -mb -ml -mdalign -mrelax -mbigtable -mfmovd -mrenesas -mno-renesas -mnomacsave -mieee -mno-ieee -mbitops -misize -minline-ic_invalidate -mpadstruct -mprefergot -musermode -multcost=</code><i>number</i> <code>-mdiv=</code><i>strategy</i> <code>-mdivsi3_libfunc=</code><i>name</i> <code>-mfixed-range=</code><i>register-range</i> <code>-maccumulate-outgoing-args -matomic-model=</code><i>atomic-model</i> <code>-mbranch-cost=</code><i>num</i> <code>-mzdcbranch -mno-zdcbranch -mcbranch-force-delay-slot -mfused-madd -mno-fused-madd -mfsca -mno-fsca -mfsrra -mno-fsrra -mpretend-cmove -mtas</code> </p>
<p> <i>Solaris 2 Options</i> <code>-mclear-hwcap -mno-clear-hwcap -mimpure-text -mno-impure-text -pthreads</code> </p>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mcmodel=</code><i>code-model</i> <code>-mmemory-model=</code><i>mem-model</i> <code>-m32 -m64 -mapp-regs -mno-app-regs -mfaster-structs -mno-faster-structs -mflat -mno-flat -mfpu -mno-fpu -mhard-float -msoft-float -mhard-quad-float -msoft-quad-float -mstack-bias -mno-stack-bias -mstd-struct-return -mno-std-struct-return -munaligned-doubles -mno-unaligned-doubles -muser-mode -mno-user-mode -mv8plus -mno-v8plus -mvis -mno-vis -mvis2 -mno-vis2 -mvis3 -mno-vis3 -mvis4 -mno-vis4 -mvis4b -mno-vis4b -mcbcond -mno-cbcond -mfmaf -mno-fmaf -mfsmuld -mno-fsmuld -mpopc -mno-popc -msubxc -mno-subxc -mfix-at697f -mfix-ut699 -mfix-ut700 -mfix-gr712rc -mlra -mno-lra</code> </p>
<p> <i></i><font SIZE="-1"><i>SPU</i></font><i> Options</i> <code>-mwarn-reloc -merror-reloc -msafe-dma -munsafe-dma -mbranch-hints -msmall-mem -mlarge-mem -mstdmain -mfixed-range=</code><i>register-range</i> <code>-mea32 -mea64 -maddress-space-conversion -mno-address-space-conversion -mcache-size=</code><i>cache-size</i> <code>-matomic-updates -mno-atomic-updates</code> </p>
<p> <i>System V Options</i> <code>-Qy -Qn -YP,</code><i>paths</i> <code>-Ym,</code><i>dir</i> </p>
<p> <i>TILE-Gx Options</i> <code>-mcpu=CPU -m32 -m64 -mbig-endian -mlittle-endian -mcmodel=</code><i>code-model</i> </p>
<p> <i>TILEPro Options</i> <code>-mcpu=</code><i>cpu</i> <code>-m32</code> </p>
<p> <i>V850 Options</i> <code>-mlong-calls -mno-long-calls -mep -mno-ep -mprolog-function -mno-prolog-function -mspace -mtda=</code><i>n</i> <code>-msda=</code><i>n</i> <code>-mzda=</code><i>n</i> <code>-mapp-regs -mno-app-regs -mdisable-callt -mno-disable-callt -mv850e2v3 -mv850e2 -mv850e1 -mv850es -mv850e -mv850 -mv850e3v5 -mloop -mrelax -mlong-jumps -msoft-float -mhard-float -mgcc-abi -mrh850-abi -mbig-switch</code> </p>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i> <code>-mg -mgnu -munix</code> </p>
<p> <i>Visium Options</i> <code>-mdebug -msim -mfpu -mno-fpu -mhard-float -msoft-float -mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-msv-mode -muser-mode</code> </p>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i> Options</i> <code>-mvms-return-codes -mdebug-main=</code><i>prefix</i> <code>-mmalloc64 -mpointer-size=</code><i>size</i> </p>
<p> <i>VxWorks Options</i> <code>-mrtp -non-static -Bstatic -Bdynamic -Xbind-lazy -Xbind-now</code> </p>
<p> <i>x86 Options</i> <code>-mtune=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mtune-ctrl=</code><i>feature-list</i> <code>-mdump-tune-features -mno-default -mfpmath=</code><i>unit</i> <code>-masm=</code><i>dialect</i> <code>-mno-fancy-math-387 -mno-fp-ret-in-387 -m80387 -mhard-float -msoft-float -mno-wide-multiply -mrtd -malign-double -mpreferred-stack-boundary=</code><i>num</i> <code>-mincoming-stack-boundary=</code><i>num</i> <code>-mcld -mcx16 -msahf -mmovbe -mcrc32 -mrecip -mrecip=</code><i>opt</i> <code>-mvzeroupper -mprefer-avx128 -mprefer-vector-width=</code><i>opt</i> <code>-mmmx -msse -msse2 -msse3 -mssse3 -msse4.1 -msse4.2 -msse4 -mavx -mavx2 -mavx512f -mavx512pf -mavx512er -mavx512cd -mavx512vl -mavx512bw -mavx512dq -mavx512ifma -mavx512vbmi -msha -maes -mpclmul -mfsgsbase -mrdrnd -mf16c -mfma -mpconfig -mwbnoinvd -mprefetchwt1 -mclflushopt -mclwb -mxsavec -mxsaves -msse4a -m3dnow -m3dnowa -mpopcnt -mabm -mbmi -mtbm -mfma4 -mxop -madx -mlzcnt -mbmi2 -mfxsr -mxsave -mxsaveopt -mrtm -mlwp -mmpx -mmwaitx -mclzero -mpku -mthreads -mgfni -mvaes -mshstk -mforce-indirect-call -mavx512vbmi2 -mvpclmulqdq -mavx512bitalg -mmovdiri -mmovdir64b -mavx512vpopcntdq -mavx5124fmaps -mavx512vnni -mavx5124vnniw -mprfchw -mrdpid -mrdseed -msgx -mms-bitfields -mno-align-stringops -minline-all-stringops -minline-stringops-dynamically -mstringop-strategy=</code><i>alg</i> <code>-mmemcpy-strategy=</code><i>strategy</i> <code>-mmemset-strategy=</code><i>strategy</i> <code>-mpush-args -maccumulate-outgoing-args -m128bit-long-double -m96bit-long-double -mlong-double-64 -mlong-double-80 -mlong-double-128 -mregparm=</code><i>num</i> <code>-msseregparm -mveclibabi=</code><i>type</i> <code>-mvect8-ret-in-mem -mpc32 -mpc64 -mpc80 -mstackrealign -momit-leaf-frame-pointer -mno-red-zone -mno-tls-direct-seg-refs -mcmodel=</code><i>code-model</i> <code>-mabi=</code><i>name</i> <code>-maddress-mode=</code><i>mode</i> <code>-m32 -m64 -mx32 -m16 -miamcu -mlarge-data-threshold=</code><i>num</i> <code>-msse2avx -mfentry -mrecord-mcount -mnop-mcount -m8bit-idiv -mavx256-split-unaligned-load -mavx256-split-unaligned-store -malign-data=</code><i>type</i> <code>-mstack-protector-guard=</code><i>guard</i> <code>-mstack-protector-guard-reg=</code><i>reg</i> <code>-mstack-protector-guard-offset=</code><i>offset</i> <code>-mstack-protector-guard-symbol=</code><i>symbol</i> <code>-mmitigate-rop -mgeneral-regs-only -mcall-ms2sysv-xlogues -mindirect-branch=</code><i>choice</i> <code>-mfunction-return=</code><i>choice</i> <code>-mindirect-branch-register</code> </p>
<p> <i>x86 Windows Options</i> <code>-mconsole -mcygwin -mno-cygwin -mdll -mnop-fun-dllimport -mthread -municode -mwin32 -mwindows -fno-set-stack-executable</code> </p>
<p> <i>Xstormy16 Options</i> <code>-msim</code> </p>
<p> <i>Xtensa Options</i> <code>-mconst16 -mno-const16 -mfused-madd -mno-fused-madd -mforce-no-pic -mserialize-volatile -mno-serialize-volatile -mtext-section-literals -mno-text-section-literals -mauto-litpools -mno-auto-litpools -mtarget-align -mno-target-align -mlongcalls -mno-longcalls</code> </p>
<p> <i>zSeries Options</i> See S/390 and zSeries Options.</dl>
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
<dt><i>file</i><code>.brig</code></p>
<dd><font SIZE="-1">BRIG</font> files (binary representation of <font SIZE="-1">HSAIL</font>).</p>
<dt><i>file</i><code>.d</code></p>
<dd>D source code.</p>
<dt><i>file</i><code>.di</code></p>
<dd>D interface file.</p>
<dt><i>file</i><code>.dd</code></p>
<dd>D documentation code (Ddoc).</p>
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
 d
 f77 f77-cpp-input f95 f95-cpp-input
 go
 brig</pre>
<dt><code>-x none</code></p>
<dd>Turn off any specification of a language, so that subsequent files are handled according to their file name suffixes (as they are if <code>-x</code> has not been used at all).</dl>
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
<dt><code>&#8211;version</code></p>
<dd>Display the version number and copyrights of the invoked <font SIZE="-1">GCC.</font></p>
<dt><code>-pass-exit-codes</code></p>
<dd>Normally the <code>gcc</code> program exits with the code of 1 if any phase of the compiler returns a non-success return code. If you specify <code>-pass-exit-codes</code>, the <code>gcc</code> program instead returns with the numerically highest error produced by any phase returning an error indication. The C, C<font SIZE="-2">++</font>, and Fortran front ends return 4 if an internal compiler error is encountered.</p>
<dt><code>-pipe</code></p>
<dd>Use pipes rather than temporary files for communication between the various stages of compilation. This fails to work on some systems where the assembler is unable to read from a pipe; but the <font SIZE="-1">GNU</font> assembler has no trouble.</p>
<dt><code>-specs=</code><i>file</i></p>
<dd>Process <i>file</i> after the compiler reads in the standard <i>specs</i> file, in order to override the defaults which the <code>gcc</code> driver program uses when determining what switches to pass to <code>cc1</code>, <code>cc1plus</code>, <code>as</code>, <code>ld</code>, etc. More than one <code>-specs=</code><i>file</i> can be specified on the command line, and they are processed in order, from left to right.</p>
<dt><code>-wrapper</code></p>
<dd>Invoke all subcommands under a wrapper program. The name of the wrapper program and its parameters are passed as a comma separated list. </p>
<pre> gcc -c t.c -wrapper gdb,--args</pre>
<p>This invokes all subprograms of <code>gcc</code> under <code>gdb &#8211;args</code>, thus the invocation of <code>cc1</code> is <code>gdb &#8211;args cc1 &#8230;</code>.</p>
<dt><code>-ffile-prefix-map=</code><i>old</i><code>=</code><i>new</i></p>
<dd>When compiling files residing in directory <i>old</i>, record any references to them in the result of the compilation as if the files resided in directory <i>new</i> instead. Specifying this option is equivalent to specifying all the individual <code>-f*-prefix-map</code> options. This can be used to make reproducible builds that are location independent. See also <code>-fmacro-prefix-map</code> and <code>-fdebug-prefix-map</code>.</p>
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
<p> This turns off certain features of <font SIZE="-1">GCC</font> that are incompatible with <font SIZE="-1">ISO C90</font> (when compiling C code), or of standard C<font SIZE="-2">++</font> (when compiling C<font SIZE="-2">++</font> code), such as the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, and predefined macros such as <tt>&quot;unix&quot;</tt> and <tt>&quot;vax&quot;</tt> that identify the type of system you are using. It also enables the undesirable and rarely used <font SIZE="-1">ISO</font> trigraph feature. For the C compiler, it disables recognition of C<font SIZE="-2">++</font> style <code>//</code> comments as well as the <tt>&quot;inline&quot;</tt> keyword. </p>
<p> The alternate keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__extension__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> continue to work despite <code>-ansi</code>. You would not want to use them in an <font SIZE="-1">ISO C</font> program, of course, but it is useful to put them in header files that might be included in compilations done with <code>-ansi</code>. Alternate predefined macros such as <tt>&quot;__unix__&quot;</tt> and <tt>&quot;__vax__&quot;</tt> are also available, with or without <code>-ansi</code>. </p>
<p> The <code>-ansi</code> option does not cause non-ISO programs to be rejected gratuitously. For that, <code>-Wpedantic</code> is required in addition to <code>-ansi</code>. </p>
<p> The macro <tt>&quot;__STRICT_ANSI__&quot;</tt> is predefined when the <code>-ansi</code> option is used. Some header files may notice this macro and refrain from declaring certain functions or defining certain macros that the <font SIZE="-1">ISO</font> standard doesn&#8217;t call for; this is to avoid interfering with any programs that might use these names for other things. </p>
<p> Functions that are normally built in but do not have semantics defined by <font SIZE="-1">ISO C</font> (such as <tt>&quot;alloca&quot;</tt> and <tt>&quot;ffs&quot;</tt>) are not built-in functions when <code>-ansi</code> is used.</p>
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
<dd><font SIZE="-1">ISO C99.</font> This standard is substantially completely supported, modulo bugs and floating-point issues (mainly but not entirely relating to optional C99 features from Annexes F and G). See &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/c99status.html">http://gcc.gnu.org/c99status.html</a></code>&gt; for more information. The names <code>c9x</code> and <code>iso9899:199x</code> are deprecated.</p>
<dt><code>c11</code></p>
<dd>
<dt><code>c1x</code></p>
<dd>
<dt><code>iso9899:2011</code></p>
<dd><font SIZE="-1">ISO C11,</font> the 2011 revision of the <font SIZE="-1">ISO C</font> standard. This standard is substantially completely supported, modulo bugs, floating-point issues (mainly but not entirely relating to optional C11 features from Annexes F and G) and the optional Annexes K (Bounds-checking interfaces) and L (Analyzability). The name <code>c1x</code> is deprecated.</p>
<dt><code>c17</code></p>
<dd>
<dt><code>c18</code></p>
<dd>
<dt><code>iso9899:2017</code></p>
<dd>
<dt><code>iso9899:2018</code></p>
<dd><font SIZE="-1">ISO C17,</font> the 2017 revision of the <font SIZE="-1">ISO C</font> standard (expected to be published in 2018). This standard is same as C11 except for corrections of defects (all of which are also applied with <code>-std=c11</code>) and a new value of <tt>&quot;__STDC_VERSION__&quot;</tt>, and so is supported to the same extent as C11.</p>
<dt><code>gnu90</code></p>
<dd>
<dt><code>gnu89</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C90</font> (including some C99 features).</p>
<dt><code>gnu99</code></p>
<dd>
<dt><code>gnu9x</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C99.</font> The name <code>gnu9x</code> is deprecated.</p>
<dt><code>gnu11</code></p>
<dd>
<dt><code>gnu1x</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C11.</font> The name <code>gnu1x</code> is deprecated.</p>
<dt><code>gnu17</code></p>
<dd>
<dt><code>gnu18</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <font SIZE="-1">ISO C17.</font> This is the default for C code.</p>
<dt><code>c++98</code></p>
<dd>
<dt><code>c++03</code></p>
<dd>The 1998 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus the 2003 technical corrigendum and some additional defect reports. Same as <code>-ansi</code> for C<font SIZE="-2">++</font> code.</p>
<dt><code>gnu++98</code></p>
<dd>
<dt><code>gnu++03</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++98</code>.</p>
<dt><code>c++11</code></p>
<dd>
<dt><code>c++0x</code></p>
<dd>The 2011 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus amendments. The name <code>c++0x</code> is deprecated.</p>
<dt><code>gnu++11</code></p>
<dd>
<dt><code>gnu++0x</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++11</code>. The name <code>gnu++0x</code> is deprecated.</p>
<dt><code>c++14</code></p>
<dd>
<dt><code>c++1y</code></p>
<dd>The 2014 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus amendments. The name <code>c++1y</code> is deprecated.</p>
<dt><code>gnu++14</code></p>
<dd>
<dt><code>gnu++1y</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++14</code>. This is the default for C<font SIZE="-2">++</font> code. The name <code>gnu++1y</code> is deprecated.</p>
<dt><code>c++17</code></p>
<dd>
<dt><code>c++1z</code></p>
<dd>The 2017 <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard plus amendments. The name <code>c++1z</code> is deprecated.</p>
<dt><code>gnu++17</code></p>
<dd>
<dt><code>gnu++1z</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++17</code>. The name <code>gnu++1z</code> is deprecated.</p>
<dt><code>c++2a</code></p>
<dd>The next revision of the <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> standard, tentatively planned for 2020. Support is highly experimental, and will almost certainly change in incompatible ways in future releases.</p>
<dt><code>gnu++2a</code></p>
<dd><font SIZE="-1">GNU</font> dialect of <code>-std=c++2a</code>. Support is highly experimental, and will almost certainly change in incompatible ways in future releases.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fgnu89-inline</code></p>
<dd>The option <code>-fgnu89-inline</code> tells <font SIZE="-1">GCC</font> to use the traditional <font SIZE="-1">GNU</font> semantics for <tt>&quot;inline&quot;</tt> functions when in C99 mode. </p>
<p> Using this option is roughly equivalent to adding the <tt>&quot;gnu_inline&quot;</tt> function attribute to all inline functions. </p>
<p> The option <code>-fno-gnu89-inline</code> explicitly tells <font SIZE="-1">GCC</font> to use the C99 semantics for <tt>&quot;inline&quot;</tt> when in C99 or gnu99 mode (i.e., it specifies the default behavior). This option is not supported in <code>-std=c90</code> or <code>-std=gnu90</code> mode. </p>
<p> The preprocessor macros <tt>&quot;__GNUC_GNU_INLINE__&quot;</tt> and <tt>&quot;__GNUC_STDC_INLINE__&quot;</tt> may be used to check which semantics are in effect for <tt>&quot;inline&quot;</tt> functions.</p>
<dt><code>-fpermitted-flt-eval-methods=</code><i>style</i></p>
<dd><font SIZE="-1">ISO/IEC TS 18661-3</font> defines new permissible values for <tt>&quot;FLT_EVAL_METHOD&quot;</tt> that indicate that operations and constants with a semantic type that is an interchange or extended format should be evaluated to the precision and range of that type. These new values are a superset of those permitted under C99/C11, which does not specify the meaning of other positive values of <tt>&quot;FLT_EVAL_METHOD&quot;</tt>. As such, code conforming to C11 may not have been written expecting the possibility of the new values. </p>
<p> <code>-fpermitted-flt-eval-methods</code> specifies whether the compiler should allow only the values of <tt>&quot;FLT_EVAL_METHOD&quot;</tt> specified in C99/C11, or the extended set of values specified in <font SIZE="-1">ISO/IEC TS 18661-3.</font> </p>
<p> <i>style</i> is either <tt>&quot;c11&quot;</tt> or <tt>&quot;ts-18661-3&quot;</tt> as appropriate. </p>
<p> The default when in a standards compliant mode (<code>-std=c11</code> or similar) is <code>-fpermitted-flt-eval-methods=c11</code>. The default when in a <font SIZE="-1">GNU</font> dialect (<code>-std=gnu11</code> or similar) is <code>-fpermitted-flt-eval-methods=ts-18661-3</code>.</p>
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
<dt><code>-fgimple</code></p>
<dd>Enable parsing of function definitions marked with <tt>&quot;__GIMPLE&quot;</tt>. This is an experimental feature that allows unit testing of <font SIZE="-1">GIMPLE</font> passes.</p>
<dt><code>-fhosted</code></p>
<dd>Assert that compilation targets a hosted environment. This implies <code>-fbuiltin</code>. A hosted environment is one in which the entire standard library is available, and in which <tt>&quot;main&quot;</tt> has a return type of <tt>&quot;int&quot;</tt>. Examples are nearly everything except a kernel. This is equivalent to <code>-fno-freestanding</code>.</p>
<dt><code>-ffreestanding</code></p>
<dd>Assert that compilation targets a freestanding environment. This implies <code>-fno-builtin</code>. A freestanding environment is one in which the standard library may not exist, and program startup may not necessarily be at <tt>&quot;main&quot;</tt>. The most obvious example is an <font SIZE="-1">OS</font> kernel. This is equivalent to <code>-fno-hosted</code>.</p>
<dt><code>-fopenacc</code></p>
<dd>Enable handling of OpenACC directives <tt>&quot;#pragma acc&quot;</tt> in C/C<font SIZE="-2">++</font> and <tt>&quot;!$acc&quot;</tt> in Fortran. When <code>-fopenacc</code> is specified, the compiler generates accelerated code according to the OpenACC Application Programming Interface v2.0 &lt;<code><a rel="nofollow" href="https://www.openacc.org">https://www.openacc.org</a></code>&gt;. This option implies <code>-pthread</code>, and thus is only supported on targets that have support for <code>-pthread</code>.</p>
<dt><code>-fopenacc-dim=</code><i>geom</i></p>
<dd>Specify default compute dimensions for parallel offload regions that do not explicitly specify. The <i>geom</i> value is a triple of &#8216;:&#8217;-separated sizes, in order &#8216;gang&#8217;, &#8216;worker&#8217; and, &#8216;vector&#8217;. A size can be omitted, to use a target-specific default value.</p>
<dt><code>-fopenmp</code></p>
<dd>Enable handling of OpenMP directives <tt>&quot;#pragma omp&quot;</tt> in C/C<font SIZE="-2">++</font> and <tt>&quot;!$omp&quot;</tt> in Fortran. When <code>-fopenmp</code> is specified, the compiler generates parallel code according to the OpenMP Application Program Interface v4.5 &lt;<code><a rel="nofollow" href="http://www.openmp.org/">http://www.openmp.org/</a></code>&gt;. This option implies <code>-pthread</code>, and thus is only supported on targets that have support for <code>-pthread</code>. <code>-fopenmp</code> implies <code>-fopenmp-simd</code>.</p>
<dt><code>-fopenmp-simd</code></p>
<dd>Enable handling of OpenMP&#8217;s <font SIZE="-1">SIMD</font> directives with <tt>&quot;#pragma omp&quot;</tt> in C/C<font SIZE="-2">++</font> and <tt>&quot;!$omp&quot;</tt> in Fortran. Other OpenMP directives are ignored.</p>
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
<p> Note that this option is off for all targets but x86 targets using ms-abi.</p>
<dt><code>-fplan9-extensions</code></p>
<dd>Accept some non-standard constructs used in Plan 9 code. </p>
<p> This enables <code>-fms-extensions</code>, permits passing pointers to structures with anonymous fields to functions that expect pointers to elements of the type of the field, and permits referring to anonymous fields declared using a typedef. This is only supported for C, not C<font SIZE="-2">++</font>.</p>
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
<dd>These options control whether a bit-field is signed or unsigned, when the declaration does not use either <tt>&quot;signed&quot;</tt> or <tt>&quot;unsigned&quot;</tt>. By default, such a bit-field is signed, because this is consistent: the basic integer types such as <tt>&quot;int&quot;</tt> are signed types.</p>
<dt><code>-fsso-struct=</code><i>endianness</i></p>
<dd>Set the default scalar storage order of structures and unions to the specified endianness. The accepted values are <code>big-endian</code>, <code>little-endian</code> and <code>native</code> for the native endianness of the target (the default). This option is not supported for C<font SIZE="-2">++</font>. </p>
<p> <code>Warning:</code> the <code>-fsso-struct</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without it if the specified endianness is not the native endianness of the target.</dl>
<h3>Options Controlling C<font SIZE="-2">++</font> Dialect</h3>
<p>This section describes the command-line options that are only meaningful for C<font SIZE="-2">++</font> programs. You can also use most of the <font SIZE="-1">GNU</font> compiler options regardless of what language your program is in. For example, you might compile a file <i>firstClass.C</i> like this: </p>
<pre> g++ -g -fstrict-enums -O -c firstClass.C</pre>
<p>In this example, only <code>-fstrict-enums</code> is an option meant only for C<font SIZE="-2">++</font> programs; you can use the other options with any language supported by <font SIZE="-1">GCC.</font> </p>
<p> Some options for compiling C programs, such as <code>-std</code>, are also relevant for C<font SIZE="-2">++</font> programs. </p>
<p> Here is a list of options that are <i>only</i> for compiling C<font SIZE="-2">++</font> programs:</p>
<dl COMPACT>
<dt><code>-fabi-version=</code><i>n</i></p>
<dd>Use version <i>n</i> of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI.</font> The default is version 0. </p>
<p> Version 0 refers to the version conforming most closely to the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> specification. Therefore, the <font SIZE="-1">ABI</font> obtained using version 0 will change in different versions of G++ as <font SIZE="-1">ABI</font> bugs are fixed. </p>
<p> Version 1 is the version of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> that first appeared in G++ 3.2. </p>
<p> Version 2 is the version of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> that first appeared in G++ 3.4, and was the default through G++ 4.9. </p>
<p> Version 3 corrects an error in mangling a constant address as a template argument. </p>
<p> Version 4, which first appeared in G++ 4.5, implements a standard mangling for vector types. </p>
<p> Version 5, which first appeared in G++ 4.6, corrects the mangling of attribute const/volatile on function pointer types, decltype of a plain decl, and use of a function parameter in the declaration of another parameter. </p>
<p> Version 6, which first appeared in G++ 4.7, corrects the promotion behavior of C<font SIZE="-2">++</font>11 scoped enums and the mangling of template argument packs, const/static_cast, prefix ++ and &#8211;, and a class scope function used as a template argument. </p>
<p> Version 7, which first appeared in G++ 4.8, that treats nullptr_t as a builtin type and corrects the mangling of lambdas in default argument scope. </p>
<p> Version 8, which first appeared in G++ 4.9, corrects the substitution behavior of function types with function-cv-qualifiers. </p>
<p> Version 9, which first appeared in G++ 5.2, corrects the alignment of <tt>&quot;nullptr_t&quot;</tt>. </p>
<p> Version 10, which first appeared in G++ 6.1, adds mangling of attributes that affect type identity, such as ia32 calling convention attributes (e.g. <code>stdcall</code>). </p>
<p> Version 11, which first appeared in G++ 7, corrects the mangling of sizeof&#8230; expressions and operator names. For multiple entities with the same name within a function, that are declared in different scopes, the mangling now changes starting with the twelfth occurrence. It also implies <code>-fnew-inheriting-ctors</code>. </p>
<p> Version 12, which first appeared in G++ 8, corrects the calling conventions for empty classes on the x86_64 target and for classes with only deleted copy/move constructors. It accidentally changes the calling convention for classes with a deleted copy constructor and a trivial move constructor. </p>
<p> Version 13, which first appeared in G++ 8.2, fixes the accidental change in version 12. </p>
<p> See also <code>-Wabi</code>.</p>
<dt><code>-fabi-compat-version=</code><i>n</i></p>
<dd>On targets that support strong aliases, G++ works around mangling changes by creating an alias with the correct mangled name when defining a symbol with an incorrect mangled name. This switch specifies which <font SIZE="-1">ABI</font> version to use for the alias. </p>
<p> With <code>-fabi-version=0</code> (the default), this defaults to 11 (<font SIZE="-1">GCC 7</font> compatibility). If another <font SIZE="-1">ABI</font> version is explicitly selected, this defaults to 0. For compatibility with <font SIZE="-1">GCC</font> versions 3.2 through 4.9, use <code>-fabi-compat-version=2</code>. </p>
<p> If this option is not provided but <code>-Wabi=</code><i>n</i> is, that version is used for compatibility aliases. If this option is provided along with <code>-Wabi</code> (without the version), the version from this option is used for the warning.</p>
<dt><code>-fno-access-control</code></p>
<dd>Turn off all access checking. This switch is mainly useful for working around bugs in the access control code.</p>
<dt><code>-faligned-new</code></p>
<dd>Enable support for C<font SIZE="-2">++</font>17 <tt>&quot;new&quot;</tt> of types that require more alignment than <tt>&quot;void* ::operator new(std::size_t)&quot;</tt> provides. A numeric argument such as <tt>&quot;-faligned-new=32&quot;</tt> can be used to specify how much alignment (in bytes) is provided by that function, but few users will need to override the default of <tt>&quot;alignof(std::max_align_t)&quot;</tt>. </p>
<p> This flag is enabled by default for <code>-std=c++17</code>.</p>
<dt><code>-fcheck-new</code></p>
<dd>Check that the pointer returned by <tt>&quot;operator new&quot;</tt> is non-null before attempting to modify the storage allocated. This check is normally unnecessary because the C<font SIZE="-2">++</font> standard specifies that <tt>&quot;operator new&quot;</tt> only returns <tt>0</tt> if it is declared <tt>&quot;throw()&quot;</tt>, in which case the compiler always checks the return value even without this option. In all other cases, when <tt>&quot;operator new&quot;</tt> has a non-empty exception specification, memory exhaustion is signalled by throwing <tt>&quot;std::bad_alloc&quot;</tt>. See also <code>new (nothrow)</code>.</p>
<dt><code>-fconcepts</code></p>
<dd>Enable support for the C<font SIZE="-2">++</font> Extensions for Concepts Technical Specification, <font SIZE="-1">ISO 19217</font> (2015), which allows code like </p>
<pre> template &lt;class T&gt; concept bool Addable = requires (T t) { t + t; };
 template &lt;Addable T&gt; T add (T a, T b) { return a + b; }</pre>
<dt><code>-fconstexpr-depth=</code><i>n</i></p>
<dd>Set the maximum nested evaluation depth for C<font SIZE="-2">++</font>11 constexpr functions to <i>n</i>. A limit is needed to detect endless recursion during constant expression evaluation. The minimum specified by the standard is 512.</p>
<dt><code>-fconstexpr-loop-limit=</code><i>n</i></p>
<dd>Set the maximum number of iterations for a loop in C<font SIZE="-2">++</font>14 constexpr functions to <i>n</i>. A limit is needed to detect infinite loops during constant expression evaluation. The default is 262144 (1&lt;&lt;18).</p>
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
<dd>Inject friend functions into the enclosing namespace, so that they are visible outside the scope of the class in which they are declared. Friend functions were documented to work this way in the old Annotated C<font SIZE="-2">++</font> Reference Manual. However, in <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> a friend function that is not declared in an enclosing scope can only be found using argument dependent lookup. <font SIZE="-1">GCC</font> defaults to the standard behavior. </p>
<p> This option is deprecated and will be removed.</p>
<dt><code>-fno-elide-constructors</code></p>
<dd>The C<font SIZE="-2">++</font> standard allows an implementation to omit creating a temporary that is only used to initialize another object of the same type. Specifying this option disables that optimization, and forces G++ to call the copy constructor in all cases. This option also causes G++ to call trivial member functions which otherwise would be expanded inline. </p>
<p> In C<font SIZE="-2">++</font>17, the compiler is required to omit these temporaries, but this option still affects trivial member functions.</p>
<dt><code>-fno-enforce-eh-specs</code></p>
<dd>Don&#8217;t generate code to check for violation of exception specifications at run time. This option violates the C<font SIZE="-2">++</font> standard, but may be useful for reducing code size in production builds, much like defining <tt>&quot;NDEBUG&quot;</tt>. This does not give user code permission to throw exceptions in violation of the exception specifications; the compiler still optimizes based on the specifications, so throwing an unexpected exception results in undefined behavior at run time.</p>
<dt><code>-fextern-tls-init</code></p>
<dd>
<dt><code>-fno-extern-tls-init</code></p>
<dd>The C<font SIZE="-2">++</font>11 and OpenMP standards allow <tt>&quot;thread_local&quot;</tt> and <tt>&quot;threadprivate&quot;</tt> variables to have dynamic (runtime) initialization. To support this, any use of such a variable goes through a wrapper function that performs any necessary initialization. When the use and definition of the variable are in the same translation unit, this overhead can be optimized away, but when the use is in a different translation unit there is significant overhead even if the variable doesn&#8217;t actually need dynamic initialization. If the programmer can be sure that no use of the variable in a non-defining <font SIZE="-1">TU</font> needs to trigger dynamic initialization (either because the variable is statically initialized, or a use of the variable in the defining <font SIZE="-1">TU</font> will be executed before any uses in another <font SIZE="-1">TU</font>), they can avoid this overhead with the <code>-fno-extern-tls-init</code> option. </p>
<p> On targets that support symbol aliases, the default is <code>-fextern-tls-init</code>. On targets that do not support symbol aliases, the default is <code>-fno-extern-tls-init</code>.</p>
<dt><code>-ffor-scope</code></p>
<dd>
<dt><code>-fno-for-scope</code></p>
<dd>If <code>-ffor-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> is limited to the <tt>&quot;for&quot;</tt> loop itself, as specified by the C<font SIZE="-2">++</font> standard. If <code>-fno-for-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> extends to the end of the enclosing scope, as was the case in old versions of G++, and other (traditional) implementations of C<font SIZE="-2">++</font>. </p>
<p> This option is deprecated and the associated non-standard functionality will be removed.</p>
<dt><code>-fno-gnu-keywords</code></p>
<dd>Do not recognize <tt>&quot;typeof&quot;</tt> as a keyword, so that code can use this word as an identifier. You can use the keyword <tt>&quot;__typeof__&quot;</tt> instead. This option is implied by the strict <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> dialects: <code>-ansi</code>, <code>-std=c++98</code>, <code>-std=c++11</code>, etc.</p>
<dt><code>-fno-implicit-templates</code></p>
<dd>Never emit code for non-inline templates that are instantiated implicitly (i.e. by use); only emit code for explicit instantiations.</p>
<dt><code>-fno-implicit-inline-templates</code></p>
<dd>Don&#8217;t emit code for implicit instantiations of inline templates, either. The default is to handle inlines differently so that compiles with and without optimization need the same set of explicit instantiations.</p>
<dt><code>-fno-implement-inlines</code></p>
<dd>To save space, do not emit out-of-line copies of inline functions controlled by <tt>&quot;#pragma implementation&quot;</tt>. This causes linker errors if these functions are not inlined everywhere they are called.</p>
<dt><code>-fms-extensions</code></p>
<dd>Disable Wpedantic warnings about constructs used in <font SIZE="-1">MFC,</font> such as implicit int and getting a pointer to member function via non-standard syntax.</p>
<dt><code>-fnew-inheriting-ctors</code></p>
<dd>Enable the P0136 adjustment to the semantics of C<font SIZE="-2">++</font>11 constructor inheritance. This is part of C<font SIZE="-2">++</font>17 but also considered to be a Defect Report against C<font SIZE="-2">++</font>11 and C<font SIZE="-2">++</font>14. This flag is enabled by default unless <code>-fabi-version=10</code> or lower is specified.</p>
<dt><code>-fnew-ttp-matching</code></p>
<dd>Enable the P0522 resolution to Core issue 150, template template parameters and default arguments: this allows a template with default template arguments as an argument for a template template parameter with fewer template parameters. This flag is enabled by default for <code>-std=c++17</code>.</p>
<dt><code>-fno-nonansi-builtins</code></p>
<dd>Disable built-in declarations of functions that are not mandated by <font SIZE="-1">ANSI/ISO C.</font> These include <tt>&quot;ffs&quot;</tt>, <tt>&quot;alloca&quot;</tt>, <tt>&quot;_exit&quot;</tt>, <tt>&quot;index&quot;</tt>, <tt>&quot;bzero&quot;</tt>, <tt>&quot;conjf&quot;</tt>, and other related functions.</p>
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
<dd>Disable generation of information about every class with virtual functions for use by the C<font SIZE="-2">++</font> run-time type identification features (<tt>&quot;dynamic_cast&quot;</tt> and <tt>&quot;typeid&quot;</tt>). If you don&#8217;t use those parts of the language, you can save some space by using this flag. Note that exception handling uses the same information, but G++ generates it as needed. The <tt>&quot;dynamic_cast&quot;</tt> operator can still be used for casts that do not require run-time type information, i.e. casts to <tt>&quot;void *&quot;</tt> or to unambiguous base classes.</p>
<dt><code>-fsized-deallocation</code></p>
<dd>Enable the built-in global declarations </p>
<pre> void operator delete (void *, std::size_t) noexcept;
 void operator delete[] (void *, std::size_t) noexcept;</pre>
<p>as introduced in C<font SIZE="-2">++</font>14. This is useful for user-defined replacement deallocation functions that, for example, use the size of the object to make deallocation faster. Enabled by default under <code>-std=c++14</code> and above. The flag <code>-Wsized-deallocation</code> warns about places that might want to add a definition.</p>
<dt><code>-fstrict-enums</code></p>
<dd>Allow the compiler to optimize using the assumption that a value of enumerated type can only be one of the values of the enumeration (as defined in the C<font SIZE="-2">++</font> standard; basically, a value that can be represented in the minimum number of bits needed to represent all the enumerators). This assumption may not be valid if the program uses a cast to convert an arbitrary integer value to the enumerated type.</p>
<dt><code>-fstrong-eval-order</code></p>
<dd>Evaluate member access, array subscripting, and shift expressions in left-to-right order, and evaluate assignment in right-to-left order, as adopted for C<font SIZE="-2">++</font>17. Enabled by default with <code>-std=c++17</code>. <code>-fstrong-eval-order=some</code> enables just the ordering of member access and shift expressions, and is the default without <code>-std=c++17</code>.</p>
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
<p> The effect of this is that <font SIZE="-1">GCC</font> may, effectively, mark inline methods with <tt>&quot;__attribute__ ((visibility (&quot;hidden&quot;)))&quot;</tt> so that they do not appear in the export table of a <font SIZE="-1">DSO</font> and do not require a <font SIZE="-1">PLT</font> indirection when used within the <font SIZE="-1">DSO.</font> Enabling this option can have a dramatic effect on load and link times of a <font SIZE="-1">DSO</font> as it massively reduces the size of the dynamic export table when the library makes heavy use of templates. </p>
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
<dt><code>-fno-weak</code></p>
<dd>Do not use weak symbol support, even if it is provided by the linker. By default, G++ uses weak symbols if they are available. This option exists only for testing, and should not be used by end-users; it results in inferior code and has no benefits. This option may be removed in a future release of G++.</p>
<dt><code>-nostdinc++</code></p>
<dd>Do not search for header files in the standard directories specific to C<font SIZE="-2">++</font>, but do still search the other standard directories. (This option is used when building the C<font SIZE="-2">++</font> library.)</dl>
<p> In addition, these optimization, warning, and code generation options have meanings only for C<font SIZE="-2">++</font> programs:</p>
<dl COMPACT>
<dt><code>-Wabi</code> (C, Objective-C, C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when G++ it generates code that is probably not compatible with the vendor-neutral C<font SIZE="-2">++</font> <font SIZE="-1">ABI.</font> Since G++ now defaults to updating the <font SIZE="-1">ABI</font> with each major release, normally <code>-Wabi</code> will warn only if there is a check added later in a release series for an <font SIZE="-1">ABI</font> issue discovered since the initial release. <code>-Wabi</code> will warn about more things if an older <font SIZE="-1">ABI</font> version is selected (with <code>-fabi-version=</code><i>n</i>). </p>
<p> <code>-Wabi</code> can also be used with an explicit version number to warn about compatibility with a particular <code>-fabi-version</code> level, e.g. <code>-Wabi=2</code> to warn about changes relative to <code>-fabi-version=2</code>. </p>
<p> If an explicit version number is provided and <code>-fabi-compat-version</code> is not specified, the version number from this option is used for compatibility aliases. If no explicit version number is provided with this option, but <code>-fabi-compat-version</code> is specified, that version number is used for <font SIZE="-1">ABI</font> warnings. </p>
<p> Although an effort has been made to warn about all such cases, there are probably some cases that are not warned about, even though G++ is generating incompatible code. There may also be cases where warnings are emitted even though the code that is generated is compatible. </p>
<p> You should rewrite your code to avoid these warnings if you are concerned about the fact that code generated by G++ may not be binary compatible with code generated by other compilers. </p>
<p> Known incompatibilities in <code>-fabi-version=2</code> (which was the default from <font SIZE="-1">GCC 3.4</font> to 4.9) include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>A template with a non-type template parameter of reference type was mangled incorrectly: </p>
<pre> extern int N;
 template &lt;int &amp;&gt; struct S {};
 void n (S&lt;N&gt;) {2}</pre>
<p>This was fixed in <code>-fabi-version=3</code>.</p>
<dt>*</p>
<dd><font SIZE="-1">SIMD</font> vector types declared using <tt>&quot;__attribute ((vector_size))&quot;</tt> were mangled in a non-standard way that does not allow for overloading of functions taking vectors of different sizes. </p>
<p> The mangling was changed in <code>-fabi-version=4</code>.</p>
<dt>*</p>
<dd><tt>&quot;__attribute ((const))&quot;</tt> and <tt>&quot;noreturn&quot;</tt> were mangled as type qualifiers, and <tt>&quot;decltype&quot;</tt> of a plain declaration was folded away. </p>
<p> These mangling issues were fixed in <code>-fabi-version=5</code>.</p>
<dt>*</p>
<dd>Scoped enumerators passed as arguments to a variadic function are promoted like unscoped enumerators, causing <tt>&quot;va_arg&quot;</tt> to complain. On most targets this does not actually affect the parameter passing <font SIZE="-1">ABI,</font> as there is no way to pass an argument smaller than <tt>&quot;int&quot;</tt>. </p>
<p> Also, the <font SIZE="-1">ABI</font> changed the mangling of template argument packs, <tt>&quot;const_cast&quot;</tt>, <tt>&quot;static_cast&quot;</tt>, prefix increment/decrement, and a class scope function used as a template argument. </p>
<p> These issues were corrected in <code>-fabi-version=6</code>.</p>
<dt>*</p>
<dd>Lambdas in default argument scope were mangled incorrectly, and the <font SIZE="-1">ABI</font> changed the mangling of <tt>&quot;nullptr_t&quot;</tt>. </p>
<p> These issues were corrected in <code>-fabi-version=7</code>.</p>
<dt>*</p>
<dd>When mangling a function type with function-cv-qualifiers, the un-qualified function type was incorrectly treated as a substitution candidate. </p>
<p> This was fixed in <code>-fabi-version=8</code>, the default for <font SIZE="-1">GCC 5.1.</font></p>
<dt>*</p>
<dd><tt>&quot;decltype(nullptr)&quot;</tt> incorrectly had an alignment of 1, leading to unaligned accesses. Note that this did not affect the <font SIZE="-1">ABI</font> of a function with a <tt>&quot;nullptr_t&quot;</tt> parameter, as parameters have a minimum alignment. </p>
<p> This was fixed in <code>-fabi-version=9</code>, the default for <font SIZE="-1">GCC 5.2.</font></p>
<dt>*</p>
<dd>Target-specific attributes that affect the identity of a type, such as ia32 calling conventions on a function type (stdcall, regparm, etc.), did not affect the mangled name, leading to name collisions when function pointers were used as template arguments. </p>
<p> This was fixed in <code>-fabi-version=10</code>, the default for <font SIZE="-1">GCC 6.1.</font></dl>
</dl>
<dl COMPACT>
<dd>It also warns about psABI-related changes. The known psABI changes at this point include:</p>
<dl COMPACT>
<dt>*</p>
<dd>For SysV/x86-64, unions with <tt>&quot;long double&quot;</tt> members are passed in memory as specified in psABI. For example: </p>
<pre> union U {
 long double ld;
 int i;
 };</pre>
<p><tt>&quot;union U&quot;</tt> is always passed in memory.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wabi-tag</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a type with an <font SIZE="-1">ABI</font> tag is used in a context that does not have that <font SIZE="-1">ABI</font> tag. See <code>C<font SIZE="-2">++</font> Attributes</code> for more information about <font SIZE="-1">ABI</font> tags.</p>
<dt><code>-Wctor-dtor-privacy</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class seems unusable because all the constructors or destructors in that class are private, and it has neither friends nor public static member functions. Also warn if there are no non-private methods, and there&#8217;s at least one private member function that isn&#8217;t a constructor or destructor.</p>
<dt><code>-Wdelete-non-virtual-dtor</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when <tt>&quot;delete&quot;</tt> is used to destroy an instance of a class that has virtual functions and non-virtual destructor. It is unsafe to delete an instance of a derived class through a pointer to a base class if the base class does not have a virtual destructor. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wliteral-suffix</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a string or character literal is followed by a ud-suffix which does not begin with an underscore. As a conforming extension, <font SIZE="-1">GCC</font> treats such suffixes as separate preprocessing tokens in order to maintain backwards compatibility with code that uses formatting macros from <tt>&quot;&lt;inttypes.h&gt;&quot;</tt>. For example: </p>
<pre> #define __STDC_FORMAT_MACROS
 #include &lt;inttypes.h&gt;
 #include &lt;stdio.h&gt;
 
 int main() {
 int64_t i64 = 123;
 printf(&quot;My int64: %&quot; PRId64&quot;
&quot;, i64);
 }</pre>
<p>In this case, <tt>&quot;PRId64&quot;</tt> is treated as a separate preprocessing token. </p>
<p> Additionally, warn when a user-defined literal operator is declared with a literal suffix identifier that doesn&#8217;t begin with an underscore. Literal suffix identifiers that don&#8217;t begin with an underscore are reserved for future standardization. </p>
<p> This warning is enabled by default.</p>
<dt><code>-Wlto-type-mismatch</code></p>
<dd>During the link-time optimization warn about type mismatches in global declarations from different compilation units. Requires <code>-flto</code> to be enabled. Enabled by default.</p>
<dt><code>-Wno-narrowing</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>For C<font SIZE="-2">++</font>11 and later standards, narrowing conversions are diagnosed by default, as required by the standard. A narrowing conversion from a constant produces an error, and a narrowing conversion from a non-constant produces a warning, but <code>-Wno-narrowing</code> suppresses the diagnostic. Note that this does not affect the meaning of well-formed code; narrowing conversions are still considered ill-formed in <font SIZE="-1">SFINAE</font> contexts. </p>
<p> With <code>-Wnarrowing</code> in C<font SIZE="-2">++</font>98, warn when a narrowing conversion prohibited by C<font SIZE="-2">++</font>11 occurs within <code>{ }</code>, e.g. </p>
<pre> int i = { 2.2 }; // error: narrowing from double to int</pre>
<p>This flag is included in <code>-Wall</code> and <code>-Wc++11-compat</code>.</p>
<dt><code>-Wnoexcept</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a noexcept-expression evaluates to false because of a call to a function that does not have a non-throwing exception specification (i.e. <tt>&quot;throw()&quot;</tt> or <tt>&quot;noexcept&quot;</tt>) but is known by the compiler to never throw an exception.</p>
<dt><code>-Wnoexcept-type</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if the C<font SIZE="-2">++</font>17 feature making <tt>&quot;noexcept&quot;</tt> part of a function type changes the mangled name of a symbol relative to C<font SIZE="-2">++</font>14. Enabled by <code>-Wabi</code> and <code>-Wc++17-compat</code>. </p>
<p> As an example: </p>
<pre> template &lt;class T&gt; void f(T t) { t(); };
 void g() noexcept;
 void h() { f(g); }</pre>
<p>In C<font SIZE="-2">++</font>14, <tt>&quot;f&quot;</tt> calls <tt>&quot;f&lt;void(*)()&gt;&quot;</tt>, but in C<font SIZE="-2">++</font>17 it calls <tt>&quot;f&lt;void(*)()noexcept&gt;&quot;</tt>.</p>
<dt><code>-Wclass-memaccess</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when the destination of a call to a raw memory function such as <tt>&quot;memset&quot;</tt> or <tt>&quot;memcpy&quot;</tt> is an object of class type, and when writing into such an object might bypass the class non-trivial or deleted constructor or copy assignment, violate const-correctness or encapsulation, or corrupt virtual table pointers. Modifying the representation of such objects may violate invariants maintained by member functions of the class. For example, the call to <tt>&quot;memset&quot;</tt> below is undefined because it modifies a non-trivial class object and is, therefore, diagnosed. The safe way to either initialize or clear the storage of objects of such types is by using the appropriate constructor or assignment operator, if one is available. </p>
<pre> std::string str = &quot;abc&quot;;
 memset (&amp;str, 0, sizeof str);</pre>
<p>The <code>-Wclass-memaccess</code> option is enabled by <code>-Wall</code>. Explicitly casting the pointer to the class object to <tt>&quot;void *&quot;</tt> or to a type that can be safely accessed by the raw memory function suppresses the warning.</p>
<dt><code>-Wnon-virtual-dtor</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class has virtual functions and an accessible non-virtual destructor itself or in an accessible polymorphic base class, in which case it is possible but unsafe to delete an instance of a derived class through a pointer to the class itself or base class. This warning is automatically enabled if <code>-Weffc++</code> is specified.</p>
<dt><code>-Wregister</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn on uses of the <tt>&quot;register&quot;</tt> storage class specifier, except when it is part of the <font SIZE="-1">GNU</font> <code>Explicit Register Variables</code> extension. The use of the <tt>&quot;register&quot;</tt> keyword as storage class specifier has been deprecated in C<font SIZE="-2">++</font>11 and removed in C<font SIZE="-2">++</font>17. Enabled by default with <code>-std=c++17</code>.</p>
<dt><code>-Wreorder</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when the order of member initializers given in the code does not match the order in which they must be executed. For instance: </p>
<pre> struct A {
 int i;
 int j;
 A(): j (0), i (1) { }
 };</pre>
<p>The compiler rearranges the member initializers for <tt>&quot;i&quot;</tt> and <tt>&quot;j&quot;</tt> to match the declaration order of the members, emitting a warning to that effect. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-fext-numeric-literals</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Accept imaginary, fixed-point, or machine-defined literal number suffixes as <font SIZE="-1">GNU</font> extensions. When this option is turned off these suffixes are treated as C<font SIZE="-2">++</font>11 user-defined literal numeric suffixes. This is on by default for all pre-C<font SIZE="-2">++</font>11 dialects and all <font SIZE="-1">GNU</font> dialects: <code>-std=c++98</code>, <code>-std=gnu++98</code>, <code>-std=gnu++11</code>, <code>-std=gnu++14</code>. This option is off by default for <font SIZE="-1">ISO C<font SIZE="-2">++</font>11</font> onwards (<code>-std=c++11</code>, &#8230;).</dl>
<p> The following <code>-W&#8230;</code> options are not affected by <code>-Wall</code>.</p>
<dl COMPACT>
<dt><code>-Weffc++</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about violations of the following style guidelines from Scott Meyers&#8217; <i>Effective C<font SIZE="-2">++</font></i> series of books:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Define a copy constructor and an assignment operator for classes with dynamically-allocated memory.</p>
<dt>*</p>
<dd>Prefer initialization to assignment in constructors.</p>
<dt>*</p>
<dd>Have <tt>&quot;operator=&quot;</tt> return a reference to <tt>*this</tt>.</p>
<dt>*</p>
<dd>Don&#8217;t try to return a reference when you must return an object.</p>
<dt>*</p>
<dd>Distinguish between prefix and postfix forms of increment and decrement operators.</p>
<dt>*</p>
<dd>Never overload <tt>&quot;&amp;&amp;&quot;</tt>, <tt>&quot;||&quot;</tt>, or <tt>&quot;,&quot;</tt>.</dl>
</dl>
<dl COMPACT>
<dd>This option also enables <code>-Wnon-virtual-dtor</code>, which is also one of the effective C<font SIZE="-2">++</font> recommendations. However, the check is extended to warn about the lack of virtual destructor in accessible non-polymorphic bases classes too. </p>
<p> When selecting this option, be aware that the standard library headers do not obey all of these guidelines; use <code>grep -v</code> to filter out those warnings.</dl>
<dt><code>-Wstrict-null-sentinel</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about the use of an uncasted <tt>&quot;NULL&quot;</tt> as sentinel. When compiling only with <font SIZE="-1">GCC</font> this is a valid sentinel, as <tt>&quot;NULL&quot;</tt> is defined to <tt>&quot;__null&quot;</tt>. Although it is a null pointer constant rather than a null pointer, it is guaranteed to be of the same size as a pointer. But this use is not portable across different compilers.</p>
<dt><code>-Wno-non-template-friend</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Disable warnings when non-template friend functions are declared within a template. In very old versions of <font SIZE="-1">GCC</font> that predate implementation of the <font SIZE="-1">ISO</font> standard, declarations such as <code>friend int foo(int)</code>, where the name of the friend is an unqualified-id, could be interpreted as a particular specialization of a template function; the warning exists to diagnose compatibility problems, and is enabled by default.</p>
<dt><code>-Wold-style-cast</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if an old-style (C-style) cast to a non-void type is used within a C<font SIZE="-2">++</font> program. The new-style casts (<tt>&quot;dynamic_cast&quot;</tt>, <tt>&quot;static_cast&quot;</tt>, <tt>&quot;reinterpret_cast&quot;</tt>, and <tt>&quot;const_cast&quot;</tt>) are less vulnerable to unintended effects and much easier to search for.</p>
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
<dd>Warn when overload resolution chooses a promotion from unsigned or enumerated type to a signed type, over a conversion to an unsigned type of the same size. Previous versions of G++ tried to preserve unsignedness, but the standard mandates the current behavior.</p>
<dt><code>-Wtemplates</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a primary template declaration is encountered. Some coding rules disallow templates, and this may be used to enforce that rule. The warning is inactive inside a system header file, such as the <font SIZE="-1">STL,</font> so one can still use the <font SIZE="-1">STL.</font> One may also instantiate or specialize templates.</p>
<dt><code>-Wmultiple-inheritance</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class is defined with multiple direct base classes. Some coding rules disallow multiple inheritance, and this may be used to enforce that rule. The warning is inactive inside a system header file, such as the <font SIZE="-1">STL,</font> so one can still use the <font SIZE="-1">STL.</font> One may also define classes that indirectly use multiple inheritance.</p>
<dt><code>-Wvirtual-inheritance</code></p>
<dd>Warn when a class is defined with a virtual direct base class. Some coding rules disallow multiple inheritance, and this may be used to enforce that rule. The warning is inactive inside a system header file, such as the <font SIZE="-1">STL,</font> so one can still use the <font SIZE="-1">STL.</font> One may also define classes that indirectly use virtual inheritance.</p>
<dt><code>-Wnamespaces</code></p>
<dd>Warn when a namespace definition is opened. Some coding rules disallow namespaces, and this may be used to enforce that rule. The warning is inactive inside a system header file, such as the <font SIZE="-1">STL,</font> so one can still use the <font SIZE="-1">STL.</font> One may also use using directives and qualified names.</p>
<dt><code>-Wno-terminate</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Disable the warning about a throw-expression that will immediately result in a call to <tt>&quot;terminate&quot;</tt>.</dl>
<h3>Options Controlling Objective-C and Objective-C<font SIZE="-2">++</font> Dialects</h3>
<p>(<font SIZE="-1">NOTE:</font> This manual does not describe the Objective-C and Objective-C<font SIZE="-2">++</font> languages themselves. </p>
<p> This section describes the command-line options that are only meaningful for Objective-C and Objective-C<font SIZE="-2">++</font> programs. You can also use most of the language-independent <font SIZE="-1">GNU</font> compiler options. For example, you might compile a file <i>some_class.m</i> like this: </p>
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
<dd>Generate output compatible with the NeXT runtime. This is the default for NeXT-based systems, including Darwin and Mac <font SIZE="-1">OS X.</font> The macro <tt>&quot;__NEXT_RUNTIME__&quot;</tt> is predefined if (and only if) this option is used.</p>
<dt><code>-fno-nil-receivers</code></p>
<dd>Assume that all Objective-C message dispatches (<tt>&quot;[receiver message:arg]&quot;</tt>) in this translation unit ensure that the receiver is not <tt>&quot;nil&quot;</tt>. This allows for more efficient entry points in the runtime to be used. This option is only available in conjunction with the NeXT runtime and <font SIZE="-1">ABI</font> version 0 or 1.</p>
<dt><code>-fobjc-abi-version=</code><i>n</i></p>
<dd>Use version <i>n</i> of the Objective-C <font SIZE="-1">ABI</font> for the selected runtime. This option is currently supported only for the NeXT runtime. In that case, Version 0 is the traditional (32-bit) <font SIZE="-1">ABI</font> without support for properties and other Objective-C 2.0 additions. Version 1 is the traditional (32-bit) <font SIZE="-1">ABI</font> with support for properties and other Objective-C 2.0 additions. Version 2 is the modern (64-bit) <font SIZE="-1">ABI.</font> If nothing is specified, the default is Version 0 on 32-bit target machines, and Version 2 on 64-bit target machines.</p>
<dt><code>-fobjc-call-cxx-cdtors</code></p>
<dd>For each Objective-C class, check if any of its instance variables is a C<font SIZE="-2">++</font> object with a non-trivial default constructor. If so, synthesize a special <tt>&quot;- (id) .cxx_construct&quot;</tt> instance method which runs non-trivial default constructors on any such instance variables, in order, and then return <tt>&quot;self&quot;</tt>. Similarly, check if any instance variable is a C<font SIZE="-2">++</font> object with a non-trivial destructor, and if so, synthesize a special <tt>&quot;- (void) .cxx_destruct&quot;</tt> method which runs all such default destructors, in reverse order. </p>
<p> The <tt>&quot;- (id) .cxx_construct&quot;</tt> and <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods thusly generated only operate on instance variables declared in the current Objective-C class, and not those inherited from superclasses. It is the responsibility of the Objective-C runtime to invoke all such methods in an object&#8217;s inheritance hierarchy. The <tt>&quot;- (id) .cxx_construct&quot;</tt> methods are invoked by the runtime immediately after a new object instance is allocated; the <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods are invoked immediately before the runtime deallocates an object instance. </p>
<p> As of this writing, only the NeXT runtime on Mac <font SIZE="-1">OS X 10.4</font> and later has support for invoking the <tt>&quot;- (id) .cxx_construct&quot;</tt> and <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods.</p>
<dt><code>-fobjc-direct-dispatch</code></p>
<dd>Allow fast jumps to the message dispatcher. On Darwin this is accomplished via the comm page.</p>
<dt><code>-fobjc-exceptions</code></p>
<dd>Enable syntactic support for structured exception handling in Objective-C, similar to what is offered by C<font SIZE="-2">++</font>. This option is required to use the Objective-C keywords <tt>@try</tt>, <tt>@throw</tt>, <tt>@catch</tt>, <tt>@finally</tt> and <tt>@synchronized</tt>. This option is available with both the <font SIZE="-1">GNU</font> runtime and the NeXT runtime (but not available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS X 10.2</font> and earlier).</p>
<dt><code>-fobjc-gc</code></p>
<dd>Enable garbage collection (<font SIZE="-1">GC</font>) in Objective-C and Objective-C<font SIZE="-2">++</font> programs. This option is only available with the NeXT runtime; the <font SIZE="-1">GNU</font> runtime has a different garbage collection implementation that does not require special compiler flags.</p>
<dt><code>-fobjc-nilcheck</code></p>
<dd>For the NeXT runtime with version 2 of the <font SIZE="-1">ABI,</font> check for a nil receiver in method invocations before doing the actual method call. This is the default and can be disabled using <code>-fno-objc-nilcheck</code>. Class methods and super calls are never checked for nil in this way no matter what this flag is set to. Currently this flag does nothing when the <font SIZE="-1">GNU</font> runtime, or an older version of the NeXT runtime <font SIZE="-1">ABI,</font> is used.</p>
<dt><code>-fobjc-std=objc1</code></p>
<dd>Conform to the language syntax of Objective-C 1.0, the language recognized by <font SIZE="-1">GCC 4.0.</font> This only affects the Objective-C additions to the C/C<font SIZE="-2">++</font> language; it does not affect conformance to C/C<font SIZE="-2">++</font> standards, which is controlled by the separate C/C<font SIZE="-2">++</font> dialect option flags. When this option is used with the Objective-C or Objective-C<font SIZE="-2">++</font> compiler, any Objective-C syntax that is not recognized by <font SIZE="-1">GCC 4.0</font> is rejected. This is useful if you need to make sure that your Objective-C code can be compiled with older versions of <font SIZE="-1">GCC.</font></p>
<dt><code>-freplace-objc-classes</code></p>
<dd>Emit a special marker instructing <code><a href="/docs/linux/man/1-ld/">ld</a>(1)</code> not to statically link in the resulting object file, and allow <code><a href="/docs/linux/man/1-dyld/">dyld</a>(1)</code> to load it in at run time instead. This is used in conjunction with the Fix-and-Continue debugging mode, where the object file in question may be recompiled and dynamically reloaded in the course of program execution, without the need to restart the program itself. Currently, Fix-and-Continue functionality is only available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS X 10.3</font> and later.</p>
<dt><code>-fzero-link</code></p>
<dd>When compiling for the NeXT runtime, the compiler ordinarily replaces calls to <tt>&quot;objc_getClass(&quot;...&quot;)&quot;</tt> (when the name of the class is known at compile time) with static class references that get initialized at load time, which improves run-time performance. Specifying the <code>-fzero-link</code> flag suppresses this behavior and causes calls to <tt>&quot;objc_getClass(&quot;...&quot;)&quot;</tt> to be retained. This is useful in Zero-Link debugging mode, since it allows for individual class implementations to be modified during program execution. The <font SIZE="-1">GNU</font> runtime currently always retains calls to <tt>&quot;objc_get_class(&quot;...&quot;)&quot;</tt> regardless of command-line options.</p>
<dt><code>-fno-local-ivars</code></p>
<dd>By default instance variables in Objective-C can be accessed as if they were local variables from within the methods of the class they&#8217;re declared in. This can lead to shadowing between instance variables and other variables declared either locally inside a class method or globally with the same name. Specifying the <code>-fno-local-ivars</code> flag disables this behavior thus avoiding variable shadowing issues.</p>
<dt><code>-fivar-visibility=</code>[<code>public</code>|<code>protected</code>|<code>private</code>|<code>package</code>]</p>
<dd>Set the default instance variable visibility to the specified option so that instance variables declared outside the scope of any access modifier directives default to the specified visibility.</p>
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
<dd>Try to format error messages so that they fit on lines of about <i>n</i> characters. If <i>n</i> is zero, then no line-wrapping is done; each error message appears on a single line. This is the default for all front ends.</p>
<dt><code>-fdiagnostics-show-location=once</code></p>
<dd>Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit source location information <i>once</i>; that is, in case the message is too long to fit on a single physical line and has to be wrapped, the source location won&#8217;t be emitted (as prefix) again, over and over, in subsequent continuation lines. This is the default behavior.</p>
<dt><code>-fdiagnostics-show-location=every-line</code></p>
<dd>Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit the same source location information (as prefix) for physical lines that result from the process of breaking a message which is too long to fit on a single line.</p>
<dt><code>-fdiagnostics-color[=</code><i></i><font SIZE="-1"><i>WHEN</i></font><i></i><code>]</code></p>
<dd>
<dt><code>-fno-diagnostics-color</code></p>
<dd>Use color in diagnostics. <i></i><font SIZE="-1"><i>WHEN</i></font><i></i> is <code>never</code>, <code>always</code>, or <code>auto</code>. The default depends on how the compiler has been configured, it can be any of the above <i></i><font SIZE="-1"><i>WHEN</i></font><i></i> options or also <code>never</code> if <font SIZE="-1"><code>GCC_COLORS</code></font> environment variable isn&#8217;t present in the environment, and <code>auto</code> otherwise. <code>auto</code> means to use color only when the standard error is a terminal. The forms <code>-fdiagnostics-color</code> and <code>-fno-diagnostics-color</code> are aliases for <code>-fdiagnostics-color=always</code> and <code>-fdiagnostics-color=never</code>, respectively. </p>
<p> The colors are defined by the environment variable <font SIZE="-1"><code>GCC_COLORS</code></font>. Its value is a colon-separated list of capabilities and Select Graphic Rendition (<font SIZE="-1">SGR</font>) substrings. <font SIZE="-1">SGR</font> commands are interpreted by the terminal or terminal emulator. (See the section in the documentation of your text terminal for permitted values and their meanings as character attributes.) These substring values are integers in decimal representation and can be concatenated with semicolons. Common values to concatenate include <code>1</code> for bold, <code>4</code> for underline, <code>5</code> for blink, <code>7</code> for inverse, <code>39</code> for default foreground color, <code>30</code> to <code>37</code> for foreground colors, <code>90</code> to <code>97</code> for 16-color mode foreground colors, <code>38;5;0</code> to <code>38;5;255</code> for 88-color and 256-color modes foreground colors, <code>49</code> for default background color, <code>40</code> to <code>47</code> for background colors, <code>100</code> to <code>107</code> for 16-color mode background colors, and <code>48;5;0</code> to <code>48;5;255</code> for 88-color and 256-color modes background colors. </p>
<p> The default <font SIZE="-1"><code>GCC_COLORS</code></font> is </p>
<pre> error=01;31:warning=01;35:note=01;36:range1=32:range2=34:locus=01:\
 quote=01:fixit-insert=32:fixit-delete=31:\
 diff-filename=01:diff-hunk=32:diff-delete=31:diff-insert=32:\
 type-diff=01;32</pre>
<p>where <code>01;31</code> is bold red, <code>01;35</code> is bold magenta, <code>01;36</code> is bold cyan, <code>32</code> is green, <code>34</code> is blue, <code>01</code> is bold, and <code>31</code> is red. Setting <font SIZE="-1"><code>GCC_COLORS</code></font> to the empty string disables colors. Supported capabilities are as follows.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&quot;error=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for error: markers.</p>
<dt>&quot;warning=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for warning: markers.</p>
<dt>&quot;note=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for note: markers.</p>
<dt>&quot;range1=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for first additional range.</p>
<dt>&quot;range2=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for second additional range.</p>
<dt>&quot;locus=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for location information, <code>file:line</code> or <code>file:line:column</code> etc.</p>
<dt>&quot;quote=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for information printed within quotes.</p>
<dt>&quot;fixit-insert=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for fix-it hints suggesting text to be inserted or replaced.</p>
<dt>&quot;fixit-delete=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for fix-it hints suggesting text to be deleted.</p>
<dt>&quot;diff-filename=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for filename headers within generated patches.</p>
<dt>&quot;diff-hunk=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for the starts of hunks within generated patches.</p>
<dt>&quot;diff-delete=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for deleted lines within generated patches.</p>
<dt>&quot;diff-insert=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for inserted lines within generated patches.</p>
<dt>&quot;type-diff=&quot;</p>
<dd><font SIZE="-1">SGR</font> substring for highlighting mismatching types within template arguments in the C<font SIZE="-2">++</font> frontend.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-fno-diagnostics-show-option</code></p>
<dd>By default, each diagnostic emitted includes text indicating the command-line option that directly controls the diagnostic (if such an option is known to the diagnostic machinery). Specifying the <code>-fno-diagnostics-show-option</code> flag suppresses that behavior.</p>
<dt><code>-fno-diagnostics-show-caret</code></p>
<dd>By default, each diagnostic emitted includes the original source line and a caret <code>^</code> indicating the column. This option suppresses this information. The source line is truncated to <i>n</i> characters, if the <code>-fmessage-length=n</code> option is given. When the output is done to the terminal, the width is limited to the width given by the <font SIZE="-1"><code>COLUMNS</code></font> environment variable or, if not set, to the terminal width.</p>
<dt><code>-fdiagnostics-parseable-fixits</code></p>
<dd>Emit fix-it hints in a machine-parseable format, suitable for consumption by IDEs. For each fix-it, a line will be printed after the relevant diagnostic, starting with the string &#8220;fix-it:&#8221;. For example: </p>
<pre> fix-it:&quot;test.c&quot;:{45:3-45:21}:&quot;gtk_widget_show_all&quot;</pre>
<p>The location is expressed as a half-open range, expressed as a count of bytes, starting at byte 1 for the initial column. In the above example, bytes 3 through 20 of line 45 of &#8220;test.c&#8221; are to be replaced with the given string: </p>
<pre> 00000000011111111112222222222
 12345678901234567890123456789
 gtk_widget_showall (dlg);
 ^^^^^^^^^^^^^^^^^^
 gtk_widget_show_all</pre>
<p>The filename and replacement string escape backslash as &#8220;\&#8221;, tab as &#8220;	&#8221;, newline as &#8220;
&#8221;, double quotes as &#8220;\&#8221;&#8220;, non-printable characters as octal (e.g. vertical tab as &#8221;&quot;). </p>
<p> An empty replacement string indicates that the given range is to be removed. An empty range (e.g. &#8220;45:3-45:3&#8221;) indicates that the string is to be inserted at the given position.</p>
<dt><code>-fdiagnostics-generate-patch</code></p>
<dd>Print fix-it hints to stderr in unified diff format, after any diagnostics are printed. For example: </p>
<pre> --- test.c
 +++ test.c
 @ -42,5 +42,5 @
 
 void show_cb(GtkDialog *dlg)
 {
 - gtk_widget_showall(dlg);
 + gtk_widget_show_all(dlg);
 }</pre>
<p>The diff may or may not be colorized, following the same rules as for diagnostics (see <code>-fdiagnostics-color</code>).</p>
<dt><code>-fdiagnostics-show-template-tree</code></p>
<dd>In the C<font SIZE="-2">++</font> frontend, when printing diagnostics showing mismatching template types, such as: </p>
<pre> could not convert 'std::map&lt;int, std::vector&lt;double&gt; &gt;()'
 from 'map&lt;[...],vector&lt;double&gt;&gt;' to 'map&lt;[...],vector&lt;float&gt;&gt;</pre>
<p>the <code>-fdiagnostics-show-template-tree</code> flag enables printing a tree-like structure showing the common and differing parts of the types, such as: </p>
<pre> map&lt;
 [...],
 vector&lt;
 [double != float]&gt;&gt;</pre>
<p>The parts that differ are highlighted with color (&#8220;double&#8221; and &#8220;float&#8221; in this case).</p>
<dt><code>-fno-elide-type</code></p>
<dd>By default when the C<font SIZE="-2">++</font> frontend prints diagnostics showing mismatching template types, common parts of the types are printed as &#8220;[&#8230;]&#8221; to simplify the error message. For example: </p>
<pre> could not convert 'std::map&lt;int, std::vector&lt;double&gt; &gt;()'
 from 'map&lt;[...],vector&lt;double&gt;&gt;' to 'map&lt;[...],vector&lt;float&gt;&gt;</pre>
<p>Specifying the <code>-fno-elide-type</code> flag suppresses that behavior. This flag also affects the output of the <code>-fdiagnostics-show-template-tree</code> flag.</p>
<dt><code>-fno-show-column</code></p>
<dd>Do not print column numbers in diagnostics. This may be necessary if diagnostics are being scanned by a program that does not understand the column numbers, such as <code>dejagnu</code>.</dl>
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
<p> Some options, such as <code>-Wall</code> and <code>-Wextra</code>, turn on other options, such as <code>-Wunused</code>, which may turn on further options, such as <code>-Wunused-value</code>. The combined effect of positive and negative forms is that more specific options have priority over less specific ones, independently of their position in the command-line. For options of the same specificity, the last one takes effect. Options enabled or disabled via pragmas take effect as if they appeared at the end of the command-line. </p>
<p> When an unrecognized warning option is requested (e.g., <code>-Wunknown-warning</code>), <font SIZE="-1">GCC</font> emits a diagnostic stating that the option is not recognized. However, if the <code>-Wno-</code> form is used, the behavior is slightly different: no diagnostic is produced for <code>-Wno-unknown-warning</code> unless other diagnostics are being produced. This allows the use of new <code>-Wno-</code> options with old compilers, but if something goes wrong, the compiler warns that an unrecognized option is present.</p>
<dl COMPACT>
<dt><code>-Wpedantic</code></p>
<dd>
<dt><code>-pedantic</code></p>
<dd>Issue all the warnings demanded by strict <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font></font>; reject all programs that use forbidden extensions, and some other programs that do not follow <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font>.</font> For <font SIZE="-1">ISO C,</font> follows the version of the <font SIZE="-1">ISO C</font> standard specified by any <code>-std</code> option used. </p>
<p> Valid <font SIZE="-1">ISO C</font> and <font SIZE="-1">ISO C<font SIZE="-2">++</font></font> programs should compile properly with or without this option (though a rare few require <code>-ansi</code> or a <code>-std</code> option specifying the required version of <font SIZE="-1">ISO C</font>). However, without this option, certain <font SIZE="-1">GNU</font> extensions and traditional C and C<font SIZE="-2">++</font> features are supported as well. With this option, they are rejected. </p>
<p> <code>-Wpedantic</code> does not cause warning messages for use of the alternate keywords whose names begin and end with <code>__</code>. Pedantic warnings are also disabled in the expression that follows <tt>&quot;__extension__&quot;</tt>. However, only system header files should use these escape routes; application programs should avoid them. </p>
<p> Some users try to use <code>-Wpedantic</code> to check programs for strict <font SIZE="-1">ISO C</font> conformance. They soon find that it does not do quite what they want: it finds some non-ISO practices, but not all&#8212;only those for which <font SIZE="-1">ISO C</font> <i>requires</i> a diagnostic, and some others for which diagnostics have been added. </p>
<p> A feature to report any failure to conform to <font SIZE="-1">ISO C</font> might be useful in some instances, but would require considerable additional work and would be quite different from <code>-Wpedantic</code>. We don&#8217;t have plans to support such a feature in the near future. </p>
<p> Where the standard specified with <code>-std</code> represents a <font SIZE="-1">GNU</font> extended dialect of C, such as <code>gnu90</code> or <code>gnu99</code>, there is a corresponding <i>base standard</i>, the version of <font SIZE="-1">ISO C</font> on which the <font SIZE="-1">GNU</font> extended dialect is based. Warnings from <code>-Wpedantic</code> are given where they are required by the base standard. (It does not make sense for such warnings to be given only for features not in the specified <font SIZE="-1">GNU C</font> dialect, since by definition the <font SIZE="-1">GNU</font> dialects of C include all features the compiler supports with the given option, and there would be nothing to warn about.)</p>
<dt><code>-pedantic-errors</code></p>
<dd>Give an error whenever the <i>base standard</i> (see <code>-Wpedantic</code>) requires a diagnostic, in some cases where there is undefined behavior at compile-time and in some other cases that do not prevent compilation of programs that are valid according to the standard. This is not equivalent to <code>-Werror=pedantic</code>, since there are errors enabled by this option and not enabled by the latter and vice versa.</p>
<dt><code>-Wall</code></p>
<dd>This enables all the warnings about constructions that some users consider questionable, and that are easy to avoid (or modify to prevent the warning), even in conjunction with macros. This also enables some language-specific warnings described in <code>C<font SIZE="-2">++</font> Dialect Options</code> and <code>Objective-C and Objective-C<font SIZE="-2">++</font> Dialect Options</code>. </p>
<p> <code>-Wall</code> turns on the following warning flags: </p>
<p> <code>-Waddress -Warray-bounds=1</code> (only with<code>-O2</code>) <code>-Wbool-compare -Wbool-operation -Wc++11-compat -Wc++14-compat -Wcatch-value</code> (C<font SIZE="-2">++</font> and Objective-C<font SIZE="-2">++</font> only) <code>-Wchar-subscripts -Wcomment -Wduplicate-decl-specifier</code> (C and Objective-C only) <code>-Wenum-compare</code> (in C/ObjC; this is on by default in C<font SIZE="-2">++</font>) <code>-Wformat -Wint-in-bool-context -Wimplicit</code> (C and Objective-C only) <code>-Wimplicit-int</code> (C and Objective-C only) <code>-Wimplicit-function-declaration</code> (C and Objective-C only) <code>-Winit-self</code> (only for C<font SIZE="-2">++</font>) <code>-Wlogical-not-parentheses -Wmain</code> (only for C/ObjC and unless<code>-ffreestanding</code>) <code>-Wmaybe-uninitialized -Wmemset-elt-size -Wmemset-transposed-args -Wmisleading-indentation</code> (only for C/C<font SIZE="-2">++</font>) <code>-Wmissing-attributes -Wmissing-braces</code> (only for C/ObjC) <code>-Wmultistatement-macros -Wnarrowing</code> (only for C<font SIZE="-2">++</font>) <code>-Wnonnull -Wnonnull-compare -Wopenmp-simd -Wparentheses -Wpointer-sign -Wreorder -Wrestrict -Wreturn-type -Wsequence-point -Wsign-compare</code> (only in C<font SIZE="-2">++</font>) <code>-Wsizeof-pointer-div -Wsizeof-pointer-memaccess -Wstrict-aliasing -Wstrict-overflow=1 -Wstringop-truncation -Wswitch -Wtautological-compare -Wtrigraphs -Wuninitialized -Wunknown-pragmas -Wunused-function -Wunused-label -Wunused-value -Wunused-variable -Wvolatile-register-var</code> </p>
<p> Note that some warning flags are not implied by <code>-Wall</code>. Some of them warn about constructions that users generally do not consider questionable, but which occasionally you might wish to check for; others warn about constructions that are necessary or hard to avoid in some cases, and there is no simple way to modify the code to suppress the warning. Some of them are enabled by <code>-Wextra</code> but many of them must be enabled individually.</p>
<dt><code>-Wextra</code></p>
<dd>This enables some extra warning flags that are not enabled by <code>-Wall</code>. (This option used to be called <code>-W</code>. The older name is still supported, but the newer name is more descriptive.) </p>
<p> <code>-Wclobbered -Wcast-function-type -Wempty-body -Wignored-qualifiers -Wimplicit-fallthrough=3 -Wmissing-field-initializers -Wmissing-parameter-type</code> (C only) <code>-Wold-style-declaration</code> (C only) <code>-Woverride-init -Wsign-compare</code> (C only) <code>-Wtype-limits -Wuninitialized -Wshift-negative-value</code> (in C<font SIZE="-2">++</font>03 and in C99 and newer) <code>-Wunused-parameter</code> (only with<code>-Wunused</code>or<code>-Wall</code>) <code>-Wunused-but-set-parameter</code> (only with<code>-Wunused</code>or<code>-Wall</code>) </p>
<p> The option <code>-Wextra</code> also prints warning messages for the following cases:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>A pointer is compared against integer zero with <tt>&quot;&lt;&quot;</tt>, <tt>&quot;&lt;=&quot;</tt>, <tt>&quot;&gt;&quot;</tt>, or <tt>&quot;&gt;=&quot;</tt>.</p>
<dt>*</p>
<dd>(C<font SIZE="-2">++</font> only) An enumerator and a non-enumerator both appear in a conditional expression.</p>
<dt>*</p>
<dd>(C<font SIZE="-2">++</font> only) Ambiguous virtual bases.</p>
<dt>*</p>
<dd>(C<font SIZE="-2">++</font> only) Subscripting an array that has been declared <tt>&quot;register&quot;</tt>.</p>
<dt>*</p>
<dd>(C<font SIZE="-2">++</font> only) Taking the address of a variable that has been declared <tt>&quot;register&quot;</tt>.</p>
<dt>*</p>
<dd>(C<font SIZE="-2">++</font> only) A base class is not initialized in the copy constructor of a derived class.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-Wchar-subscripts</code></p>
<dd>Warn if an array subscript has type <tt>&quot;char&quot;</tt>. This is a common cause of error, as programmers often forget that this type is signed on some machines. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wchkp</code></p>
<dd>Warn about an invalid memory access that is found by Pointer Bounds Checker (<code>-fcheck-pointer-bounds</code>).</p>
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
<dt><code>-Wduplicate-decl-specifier</code> (C and Objective-C only)</p>
<dd>Warn if a declaration has duplicate <tt>&quot;const&quot;</tt>, <tt>&quot;volatile&quot;</tt>, <tt>&quot;restrict&quot;</tt> or <tt>&quot;_Atomic&quot;</tt> specifier. This warning is enabled by <code>-Wall</code>.</p>
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
<dt><code>-Wformat-overflow</code></p>
<dd>
<dt><code>-Wformat-overflow=</code><i>level</i></p>
<dd>Warn about calls to formatted input/output functions such as <tt>&quot;sprintf&quot;</tt> and <tt>&quot;vsprintf&quot;</tt> that might overflow the destination buffer. When the exact number of bytes written by a format directive cannot be determined at compile-time it is estimated based on heuristics that depend on the <i>level</i> argument and on optimization. While enabling optimization will in most cases improve the accuracy of the warning, it may also result in false positives.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>-Wformat-overflow</code></p>
<dd>
<dt><code>-Wformat-overflow=1</code></p>
<dd>Level <i>1</i> of <code>-Wformat-overflow</code> enabled by <code>-Wformat</code> employs a conservative approach that warns only about calls that most likely overflow the buffer. At this level, numeric arguments to format directives with unknown values are assumed to have the value of one, and strings of unknown length to be empty. Numeric arguments that are known to be bounded to a subrange of their type, or string arguments whose output is bounded either by their directive&#8217;s precision or by a finite set of string literals, are assumed to take on the value within the range that results in the most bytes on output. For example, the call to <tt>&quot;sprintf&quot;</tt> below is diagnosed because even with both <i>a</i> and <i>b</i> equal to zero, the terminating <font SIZE="-1">NUL</font> character (<tt>'
