---
title: "arm-gp2x-linux-g(1)"
name: "arm-gp2x-linux-g"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-g/"
description: "gcc – GNU project C and C++ compiler"
---

<p>gcc &#8211; GNU project C and C++ compiler</p>
<h2>Synopsis</h2>
<p>gcc [<code>-c</code>|<code>-S</code>|<code>-E</code>] [<code>-std=</code><i>standard</i>]<br />
&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>]<br />
&nbsp;<wbr>[<code>-W</code><i>warn</i>&#8230;]&nbsp;<wbr>[<code>-pedantic</code>]<br />
&nbsp;<wbr>[<code>-I</code><i>dir</i>&#8230;]&nbsp;<wbr>[<code>-L</code><i>dir</i>&#8230;]<br />
&nbsp;<wbr>[<code>-D</code><i>macro</i>[=<i>defn</i>]&#8230;]&nbsp;<wbr>[<code>-U</code><i>macro</i>]<br />
&nbsp;<wbr>[<code>-f</code><i>option</i>&#8230;]&nbsp;<wbr>[<code>-m</code><i>machine-option</i>&#8230;]<br />
&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr><i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder. <code>g++</code> accepts mostly the same options as <code>gcc</code>.</p>
<h2>Description</h2>
<p>When you invoke <font SIZE="-1">GCC</font>, it normally does preprocessing, compilation, assembly and linking. The &#8220;overall options&#8221; allow you to stop this process at an intermediate stage. For example, the <code>-c</code> option says not to run the linker. Then the output consists of object files output by the assembler. </p>
<p> Other options are passed on to one stage of processing. Some options control the preprocessor and others the compiler itself. Yet other options control the assembler and linker; most of these are not documented here, since you rarely need to use any of them. </p>
<p> Most of the command line options that you can use with <font SIZE="-1">GCC</font> are useful for C programs; when an option is only useful with another language (usually C<font SIZE="-2">++</font>), the explanation says so explicitly. If the description for a particular option does not mention a source language, you can use that option with all supported languages. </p>
<p> The <code>gcc</code> program accepts options and file names as operands. Many options have multi-letter names; therefore multiple single-letter options may <i>not</i> be grouped: <code>-dr</code> is very different from <code>-d -r</code>. </p>
<p> You can mix options and other arguments. For the most part, the order you use doesn&#8217;t matter. Order does matter when you use several options of the same kind; for example, if you specify <code>-L</code> more than once, the directories are searched in the order specified. </p>
<p> Many options have long names starting with <code>-f</code> or with <code>-W</code>&#8212;for example, <code>-fstrength-reduce</code>, <code>-Wformat</code> and so on. Most of these have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.</p>
<h2>Options</h2>
<h2>Option Summary</h2>
<p>Here is a summary of all the options, grouped by type. Explanations are in the following sections.</p>
<dl>
<dt><i>Overall Options</i></p>
<dd><code>-c -S -E -o</code> <i>file</i> <code>-combine -pipe -pass-exit-codes -x</code> <i>language</i> <code>-v -### &#8211;help &#8211;target-help &#8211;version</code></p>
<dt><i>C Language Options</i></p>
<dd><code>-ansi -std=</code><i>standard</i> <code>-aux-info</code> <i>filename</i> <code>-fno-asm -fno-builtin -fno-builtin-</code><i>function</i> <code>-fhosted -ffreestanding -fms-extensions -trigraphs -no-integrated-cpp -traditional -traditional-cpp -fallow-single-precision -fcond-mismatch -fsigned-bitfields -fsigned-char -funsigned-bitfields -funsigned-char</code></p>
<dt><i>C<font SIZE="-2">++</font> Language Options</i></p>
<dd><code>-fabi-version=</code><i>n</i> <code>-fno-access-control -fcheck-new -fconserve-space -ffriend-injection -fno-const-strings -fno-elide-constructors -fno-enforce-eh-specs -ffor-scope -fno-for-scope -fno-gnu-keywords -fno-implicit-templates -fno-implicit-inline-templates -fno-implement-inlines -fms-extensions -fno-nonansi-builtins -fno-operator-names -fno-optional-diags -fpermissive -frepo -fno-rtti -fstats -ftemplate-depth-</code><i>n</i> <code>-fno-threadsafe-statics -fuse-cxa-atexit -fno-weak -nostdinc++ -fno-default-inline -fvisibility-inlines-hidden -Wabi -Wctor-dtor-privacy -Wnon-virtual-dtor -Wreorder -Weffc++ -Wno-deprecated -Wstrict-null-sentinel -Wno-non-template-friend -Wold-style-cast -Woverloaded-virtual -Wno-pmf-conversions -Wsign-promo</code></p>
<dt><i>Objective-C and Objective-C<font SIZE="-2">++</font> Language Options</i></p>
<dd><code>-fconstant-string-class=</code><i>class-name</i> <code>-fgnu-runtime -fnext-runtime -fno-nil-receivers -fobjc-call-cxx-cdtors -fobjc-direct-dispatch -fobjc-exceptions -fobjc-gc -freplace-objc-classes -fzero-link -gen-decls -Wassign-intercept -Wno-protocol -Wselector -Wstrict-selector-match -Wundeclared-selector</code></p>
<dt><i>Language Independent Options</i></p>
<dd><code>-fmessage-length=</code><i>n</i> <code>-fdiagnostics-show-location=</code>[<code>once</code>|<code>every-line</code>] -fdiagnostics-show-options</p>
<dt><i>Warning Options</i></p>
<dd><code>-fsyntax-only -pedantic -pedantic-errors -w -Wextra -Wall -Waggregate-return -Wno-attributes -Wc++-compat -Wcast-align -Wcast-qual -Wchar-subscripts -Wcomment -Wconversion -Wno-deprecated-declarations -Wdisabled-optimization -Wno-div-by-zero -Wno-endif-labels -Werror -Werror-implicit-function-declaration -Wfatal-errors -Wfloat-equal -Wformat -Wformat=2 -Wno-format-extra-args -Wformat-nonliteral -Wformat-security -Wformat-y2k -Wimplicit -Wimplicit-function-declaration -Wimplicit-int -Wimport -Wno-import -Winit-self -Winline -Wno-int-to-pointer-cast -Wno-invalid-offsetof -Winvalid-pch -Wlarger-than-</code><i>len</i> <code>-Wunsafe-loop-optimizations -Wlong-long -Wmain -Wmissing-braces -Wmissing-field-initializers -Wmissing-format-attribute -Wmissing-include-dirs -Wmissing-noreturn -Wno-multichar -Wnonnull -Wpacked -Wpadded -Wparentheses -Wpointer-arith -Wno-pointer-to-int-cast -Wredundant-decls -Wreturn-type -Wsequence-point -Wshadow -Wsign-compare -Wstack-protector -Wstrict-aliasing -Wstrict-aliasing=2 -Wswitch -Wswitch-default -Wswitch-enum -Wsystem-headers -Wtrigraphs -Wundef -Wuninitialized -Wunknown-pragmas -Wno-pragmas -Wunreachable-code -Wunused -Wunused-function -Wunused-label -Wunused-parameter -Wunused-value -Wunused-variable -Wvariadic-macros -Wvolatile-register-var -Wwrite-strings</code></p>
<dt><i>C-only Warning Options</i></p>
<dd><code>-Wbad-function-cast -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Wold-style-definition -Wstrict-prototypes -Wtraditional -Wdeclaration-after-statement -Wpointer-sign</code></p>
<dt><i>Debugging Options</i></p>
<dd><code>-d</code><i>letters</i> <code>-dumpspecs -dumpmachine -dumpversion -fdump-unnumbered -fdump-translation-unit</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-class-hierarchy</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-ipa-all -fdump-ipa-cgraph -fdump-tree-all -fdump-tree-original</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-optimized</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-inlined</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-cfg -fdump-tree-vcg -fdump-tree-alias -fdump-tree-ch -fdump-tree-ssa</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-pre</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-ccp</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-dce</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-gimple</code>[<code>-raw</code>] <code>-fdump-tree-mudflap</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-dom</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-dse</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-phiopt</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-forwprop</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-copyrename</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-nrv -fdump-tree-vect -fdump-tree-sink -fdump-tree-sra</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-salias -fdump-tree-fre</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-vrp</code>[<code>&#8211;</code><i>n</i>] <code>-ftree-vectorizer-verbose=</code><i>n</i> <code>-fdump-tree-storeccp</code>[<code>&#8211;</code><i>n</i>] <code>-feliminate-dwarf2-dups -feliminate-unused-debug-types -feliminate-unused-debug-symbols -fmem-report -fprofile-arcs -frandom-seed=</code><i>string</i> <code>-fsched-verbose=</code><i>n</i> <code>-ftest-coverage -ftime-report -fvar-tracking -g -g</code><i>level</i> <code>-gcoff -gdwarf-2 -ggdb -gstabs -gstabs+ -gvms -gxcoff -gxcoff+ -p -pg -print-file-name=</code><i>library</i> <code>-print-libgcc-file-name -print-multi-directory -print-multi-lib -print-prog-name=</code><i>program</i> <code>-print-search-dirs -Q -save-temps -time</code></p>
<dt><i>Optimization Options</i></p>
<dd><code>-falign-functions=</code><i>n</i> <code>-falign-jumps=</code><i>n</i> <code>-falign-labels=</code><i>n</i> <code>-falign-loops=</code><i>n</i> <code>-fbounds-check -fmudflap -fmudflapth -fmudflapir -fbranch-probabilities -fprofile-values -fvpt -fbranch-target-load-optimize -fbranch-target-load-optimize2 -fbtr-bb-exclusive -fcaller-saves -fcprop-registers -fcse-follow-jumps -fcse-skip-blocks -fcx-limited-range -fdata-sections -fdelayed-branch -fdelete-null-pointer-checks -fearly-inlining -fexpensive-optimizations -ffast-math -ffloat-store -fforce-addr -ffunction-sections -fgcse -fgcse-lm -fgcse-sm -fgcse-las -fgcse-after-reload -floop-optimize -fcrossjumping -fif-conversion -fif-conversion2 -finline-functions -finline-functions-called-once -finline-limit=</code><i>n</i> <code>-fkeep-inline-functions -fkeep-static-consts -fmerge-constants -fmerge-all-constants -fmodulo-sched -fno-branch-count-reg -fno-default-inline -fno-defer-pop -floop-optimize2 -fmove-loop-invariants -fno-function-cse -fno-guess-branch-probability -fno-inline -fno-math-errno -fno-peephole -fno-peephole2 -funsafe-math-optimizations -funsafe-loop-optimizations -ffinite-math-only -fno-trapping-math -fno-zero-initialized-in-bss -fomit-frame-pointer -foptimize-register-move -foptimize-sibling-calls -fprefetch-loop-arrays -fprofile-generate -fprofile-use -fregmove -frename-registers -freorder-blocks -freorder-blocks-and-partition -freorder-functions -frerun-cse-after-loop -frerun-loop-opt -frounding-math -fschedule-insns -fschedule-insns2 -fno-sched-interblock -fno-sched-spec -fsched-spec-load -fsched-spec-load-dangerous -fsched-stalled-insns=</code><i>n</i> <code>-fsched-stalled-insns-dep=</code><i>n</i> <code>-fsched2-use-superblocks -fsched2-use-traces -freschedule-modulo-scheduled-loops -fsignaling-nans -fsingle-precision-constant -fstack-protector -fstack-protector-all -fstrength-reduce -fstrict-aliasing -ftracer -fthread-jumps -funroll-all-loops -funroll-loops -fpeel-loops -fsplit-ivs-in-unroller -funswitch-loops -fvariable-expansion-in-unroller -ftree-pre -ftree-ccp -ftree-dce -ftree-loop-optimize -ftree-loop-linear -ftree-loop-im -ftree-loop-ivcanon -fivopts -ftree-dominator-opts -ftree-dse -ftree-copyrename -ftree-sink -ftree-ch -ftree-sra -ftree-ter -ftree-lrs -ftree-fre -ftree-vectorize -ftree-vect-loop-version -ftree-salias -fweb -ftree-copy-prop -ftree-store-ccp -ftree-store-copy-prop -fwhole-program &#8211;param</code> <i>name</i><code>=</code><i>value</i> <code>-O -O0 -O1 -O2 -O3 -Os</code></p>
<dt><i>Preprocessor Options</i></p>
<dd><code>-A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -dD -dI -dM -dN -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-E -H -idirafter</code> <i>dir</i> <code>-include</code> <i>file</i> <code>-imacros</code> <i>file</i> <code>-iprefix</code> <i>file</i> <code>-iwithprefix</code> <i>dir</i> <code>-iwithprefixbefore</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-isysroot</code> <i>dir</i> <code>-M -MM -MF -MG -MP -MQ -MT -nostdinc -P -fworking-directory -remap -trigraphs -undef -U</code><i>macro</i> <code>-Wp,</code><i>option</i> <code>-Xpreprocessor</code> <i>option</i></p>
<dt><i>Assembler Option</i></p>
<dd><code>-Wa,</code><i>option</i> <code>-Xassembler</code> <i>option</i></p>
<dt><i>Linker Options</i></p>
<dd><i>object-file-name</i> <code>-l</code><i>library</i> <code>-nostartfiles -nodefaultlibs -nostdlib -pie -rdynamic -s -static -static-libgcc -shared -shared-libgcc -symbolic -Wl,</code><i>option</i> <code>-Xlinker</code> <i>option</i> <code>-u</code> <i>symbol</i></p>
<dt><i>Directory Options</i></p>
<dd><code>-B</code><i>prefix</i> <code>-I</code><i>dir</i> <code>-iquote</code><i>dir</i> <code>-L</code><i>dir</i> <code>-specs=</code><i>file</i> <code>-I- &#8211;sysroot=</code><i>dir</i></p>
<dt><i>Target Options</i></p>
<dd><code>-V</code> <i>version</i> <code>-b</code> <i>machine</i></p>
<dt><i>Machine Dependent Options</i></p>
<dd><i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i> <code>-EB -EL -mmangle-cpu -mcpu=</code><i>cpu</i> <code>-mtext=</code><i>text-section</i> <code>-mdata=</code><i>data-section</i> <code>-mrodata=</code><i>readonly-data-section</i> </p>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i> <code>-mapcs-frame -mno-apcs-frame -mabi=</code><i>name</i> <code>-mapcs-stack-check -mno-apcs-stack-check -mapcs-float -mno-apcs-float -mapcs-reentrant -mno-apcs-reentrant -msched-prolog -mno-sched-prolog -mlittle-endian -mbig-endian -mwords-little-endian -mfloat-abi=</code><i>name</i> <code>-msoft-float -mhard-float -mfpe -mthumb-interwork -mno-thumb-interwork -mcpu=</code><i>name</i> <code>-march=</code><i>name</i> <code>-mfpu=</code><i>name</i> <code>-mstructure-size-boundary=</code><i>n</i> <code>-mabort-on-noreturn -mlong-calls -mno-long-calls -msingle-pic-base -mno-single-pic-base -mpic-register=</code><i>reg</i> <code>-mnop-fun-dllimport -mcirrus-fix-invalid-insns -mno-cirrus-fix-invalid-insns -mpoke-function-name -mthumb -marm -mtpcs-frame -mtpcs-leaf-frame -mcaller-super-interworking -mcallee-super-interworking -mtp=</code><i>name</i> </p>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i> <code>-mmcu=</code><i>mcu</i> <code>-msize -minit-stack=</code><i>n</i> <code>-mno-interrupts -mcall-prologues -mno-tablejump -mtiny-stack -mint8</code> </p>
<p> <i>Blackfin Options</i> <code>-momit-leaf-frame-pointer -mno-omit-leaf-frame-pointer -mspecld-anomaly -mno-specld-anomaly -mcsync-anomaly -mno-csync-anomaly -mlow-64k -mno-low64k -mid-shared-library -mno-id-shared-library -mshared-library-id=</code><i>n</i> <code>-mlong-calls -mno-long-calls</code> </p>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i> <code>-mcpu=</code><i>cpu</i> <code>-march=</code><i>cpu</i> <code>-mtune=</code><i>cpu</i> <code>-mmax-stack-frame=</code><i>n</i> <code>-melinux-stacksize=</code><i>n</i> <code>-metrax4 -metrax100 -mpdebug -mcc-init -mno-side-effects -mstack-align -mdata-align -mconst-align -m32-bit -m16-bit -m8-bit -mno-prologue-epilogue -mno-gotplt -melf -maout -melinux -mlinux -sim -sim2 -mmul-bug-workaround -mno-mul-bug-workaround</code> </p>
<p> <i></i><font SIZE="-1"><i>CRX</i></font><i> Options</i> <code>-mmac -mpush-args</code> </p>
<p> <i>Darwin Options</i> <code>-all_load -allowable_client -arch -arch_errors_fatal -arch_only -bind_at_load -bundle -bundle_loader -client_name -compatibility_version -current_version -dead_strip -dependency-file -dylib_file -dylinker_install_name -dynamic -dynamiclib -exported_symbols_list -filelist -flat_namespace -force_cpusubtype_ALL -force_flat_namespace -headerpad_max_install_names -image_base -init -install_name -keep_private_externs -multi_module -multiply_defined -multiply_defined_unused -noall_load -no_dead_strip_inits_and_terms -nofixprebinding -nomultidefs -noprebind -noseglinkedit -pagezero_size -prebind -prebind_all_twolevel_modules -private_bundle -read_only_relocs -sectalign -sectobjectsymbols -whyload -seg1addr -sectcreate -sectobjectsymbols -sectorder -segaddr -segs_read_only_addr -segs_read_write_addr -seg_addr_table -seg_addr_table_filename -seglinkedit -segprot -segs_read_only_addr -segs_read_write_addr -single_module -static -sub_library -sub_umbrella -twolevel_namespace -umbrella -undefined -unexported_symbols_list -weak_reference_mismatches -whatsloaded -F -gused -gfull -mmacosx-version-min=</code><i>version</i> <code>-mone-byte-bool</code> </p>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha Options</i> <code>-mno-fp-regs -msoft-float -malpha-as -mgas -mieee -mieee-with-inexact -mieee-conformant -mfp-trap-mode=</code><i>mode</i> <code>-mfp-rounding-mode=</code><i>mode</i> <code>-mtrap-precision=</code><i>mode</i> <code>-mbuild-constants -mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mbwx -mmax -mfix -mcix -mfloat-vax -mfloat-ieee -mexplicit-relocs -msmall-data -mlarge-data -msmall-text -mlarge-text -mmemory-latency=</code><i>time</i> </p>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha/VMS Options</i> <code>-mvms-return-codes</code> </p>
<p> <i></i><font SIZE="-1"><i>FRV</i></font><i> Options</i> <code>-mgpr-32 -mgpr-64 -mfpr-32 -mfpr-64 -mhard-float -msoft-float -malloc-cc -mfixed-cc -mdword -mno-dword -mdouble -mno-double -mmedia -mno-media -mmuladd -mno-muladd -mfdpic -minline-plt -mgprel-ro -multilib-library-pic -mlinked-fp -mlong-calls -malign-labels -mlibrary-pic -macc-4 -macc-8 -mpack -mno-pack -mno-eflags -mcond-move -mno-cond-move -moptimize-membar -mno-optimize-membar -mscc -mno-scc -mcond-exec -mno-cond-exec -mvliw-branch -mno-vliw-branch -mmulti-cond-exec -mno-multi-cond-exec -mnested-cond-exec -mno-nested-cond-exec -mtomcat-stats -mTLS -mtls -mcpu=</code><i>cpu</i> </p>
<p> <i>H8/300 Options</i> <code>-mrelax -mh -ms -mn -mint32 -malign-300</code> </p>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i> <code>-march=</code><i>architecture-type</i> <code>-mbig-switch -mdisable-fpregs -mdisable-indexing -mfast-indirect-calls -mgas -mgnu-ld -mhp-ld -mfixed-range=</code><i>register-range</i> <code>-mjump-in-delay -mlinker-opt -mlong-calls -mlong-load-store -mno-big-switch -mno-disable-fpregs -mno-disable-indexing -mno-fast-indirect-calls -mno-gas -mno-jump-in-delay -mno-long-load-store -mno-portable-runtime -mno-soft-float -mno-space-regs -msoft-float -mpa-risc-1-0 -mpa-risc-1-1 -mpa-risc-2-0 -mportable-runtime -mschedule=</code><i>cpu-type</i> <code>-mspace-regs -msio -mwsio -munix=</code><i>unix-std</i> <code>-nolibdld -static -threads</code> </p>
<p> <i>i386 and x86-64 Options</i> <code>-mtune=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mfpmath=</code><i>unit</i> <code>-masm=</code><i>dialect</i> <code>-mno-fancy-math-387 -mno-fp-ret-in-387 -msoft-float -msvr3-shlib -mno-wide-multiply -mrtd -malign-double -mpreferred-stack-boundary=</code><i>num</i> <code>-mmmx -msse -msse2 -msse3 -m3dnow -mthreads -mno-align-stringops -minline-all-stringops -mpush-args -maccumulate-outgoing-args -m128bit-long-double -m96bit-long-double -mregparm=</code><i>num</i> <code>-msseregparm -momit-leaf-frame-pointer -mno-red-zone -mno-tls-direct-seg-refs -mcmodel=</code><i>code-model</i> <code>-m32 -m64 -mlarge-data-threshold=</code><i>num</i> </p>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i> <code>-mbig-endian -mlittle-endian -mgnu-as -mgnu-ld -mno-pic -mvolatile-asm-stop -mregister-names -mno-sdata -mconstant-gp -mauto-pic -minline-float-divide-min-latency -minline-float-divide-max-throughput -minline-int-divide-min-latency -minline-int-divide-max-throughput -minline-sqrt-min-latency -minline-sqrt-max-throughput -mno-dwarf2-asm -mearly-stop-bits -mfixed-range=</code><i>register-range</i> <code>-mtls-size=</code><i>tls-size</i> <code>-mtune=</code><i>cpu-type</i> <code>-mt -pthread -milp32 -mlp64</code> </p>
<p> <i>M32R/D Options</i> <code>-m32r2 -m32rx -m32r -mdebug -malign-loops -mno-align-loops -missue-rate=</code><i>number</i> <code>-mbranch-cost=</code><i>number</i> <code>-mmodel=</code><i>code-size-model-type</i> <code>-msdata=</code><i>sdata-type</i> <code>-mno-flush-func -mflush-func=</code><i>name</i> <code>-mno-flush-trap -mflush-trap=</code><i>number</i> <code>-G</code> <i>num</i> </p>
<p> <i>M32C Options</i> <code>-mcpu=</code><i>cpu</i> <code>-msim -memregs=</code><i>number</i> </p>
<p> <i>M680x0 Options</i> <code>-m68000 -m68020 -m68020-40 -m68020-60 -m68030 -m68040 -m68060 -mcpu32 -m5200 -m68881 -mbitfield -mc68000 -mc68020 -mnobitfield -mrtd -mshort -msoft-float -mpcrel -malign-int -mstrict-align -msep-data -mno-sep-data -mshared-library-id=n -mid-shared-library -mno-id-shared-library</code> </p>
<p> <i>M68hc1x Options</i> <code>-m6811 -m6812 -m68hc11 -m68hc12 -m68hcs12 -mauto-incdec -minmax -mlong-calls -mshort -msoft-reg-count=</code><i>count</i> </p>
<p> <i>MCore Options</i> <code>-mhardlit -mno-hardlit -mdiv -mno-div -mrelax-immediates -mno-relax-immediates -mwide-bitfields -mno-wide-bitfields -m4byte-functions -mno-4byte-functions -mcallgraph-data -mno-callgraph-data -mslow-bytes -mno-slow-bytes -mno-lsim -mlittle-endian -mbig-endian -m210 -m340 -mstack-increment</code> </p>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i> <code>-EL -EB -march=</code><i>arch</i> <code>-mtune=</code><i>arch</i> <code>-mips1 -mips2 -mips3 -mips4 -mips32 -mips32r2 -mips64 -mips16 -mno-mips16 -mabi=</code><i>abi</i> <code>-mabicalls -mno-abicalls -mxgot -mno-xgot -mgp32 -mgp64 -mfp32 -mfp64 -mhard-float -msoft-float -msingle-float -mdouble-float -mdsp -mpaired-single -mips3d -mlong64 -mlong32 -msym32 -mno-sym32 -G</code><i>num</i> <code>-membedded-data -mno-embedded-data -muninit-const-in-rodata -mno-uninit-const-in-rodata -msplit-addresses -mno-split-addresses -mexplicit-relocs -mno-explicit-relocs -mcheck-zero-division -mno-check-zero-division -mdivide-traps -mdivide-breaks -mmemcpy -mno-memcpy -mlong-calls -mno-long-calls -mmad -mno-mad -mfused-madd -mno-fused-madd -nocpp -mfix-r4000 -mno-fix-r4000 -mfix-r4400 -mno-fix-r4400 -mfix-vr4120 -mno-fix-vr4120 -mfix-vr4130 -mfix-sb1 -mno-fix-sb1 -mflush-func=</code><i>func</i> <code>-mno-flush-func -mbranch-likely -mno-branch-likely -mfp-exceptions -mno-fp-exceptions -mvr4130-align -mno-vr4130-align</code> </p>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i> <code>-mlibfuncs -mno-libfuncs -mepsilon -mno-epsilon -mabi=gnu -mabi=mmixware -mzero-extend -mknuthdiv -mtoplevel-symbols -melf -mbranch-predict -mno-branch-predict -mbase-addresses -mno-base-addresses -msingle-exit -mno-single-exit</code> </p>
<p> <i></i><font SIZE="-1"><i>MN10300</i></font><i> Options</i> <code>-mmult-bug -mno-mult-bug -mam33 -mno-am33 -mam33-2 -mno-am33-2 -mreturn-pointer-on-d0 -mno-crt0 -mrelax</code> </p>
<p> <i></i><font SIZE="-1"><i>MT</i></font><i> Options</i> <code>-mno-crt0 -mbacc -msim -march=</code><i>cpu-type</i> </p>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i> <code>-mfpu -msoft-float -mac0 -mno-ac0 -m40 -m45 -m10 -mbcopy -mbcopy-builtin -mint32 -mno-int16 -mint16 -mno-int32 -mfloat32 -mno-float64 -mfloat64 -mno-float32 -mabshi -mno-abshi -mbranch-expensive -mbranch-cheap -msplit -mno-split -munix-asm -mdec-asm</code> </p>
<p> <i>PowerPC Options</i> See <font SIZE="-1">RS/6000</font> and PowerPC Options. </p>
<p> <i></i><font SIZE="-1"><i>RS/6000</i></font><i> and PowerPC Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mpower -mno-power -mpower2 -mno-power2 -mpowerpc -mpowerpc64 -mno-powerpc -maltivec -mno-altivec -mpowerpc-gpopt -mno-powerpc-gpopt -mpowerpc-gfxopt -mno-powerpc-gfxopt -mmfcrf -mno-mfcrf -mpopcntb -mno-popcntb -mfprnd -mno-fprnd -mnew-mnemonics -mold-mnemonics -mfull-toc -mminimal-toc -mno-fp-in-toc -mno-sum-in-toc -m64 -m32 -mxl-compat -mno-xl-compat -mpe -malign-power -malign-natural -msoft-float -mhard-float -mmultiple -mno-multiple -mstring -mno-string -mupdate -mno-update -mfused-madd -mno-fused-madd -mbit-align -mno-bit-align -mstrict-align -mno-strict-align -mrelocatable -mno-relocatable -mrelocatable-lib -mno-relocatable-lib -mtoc -mno-toc -mlittle -mlittle-endian -mbig -mbig-endian -mdynamic-no-pic -maltivec -mswdiv -mprioritize-restricted-insns=</code><i>priority</i> <code>-msched-costly-dep=</code><i>dependence_type</i> <code>-minsert-sched-nops=</code><i>scheme</i> <code>-mcall-sysv -mcall-netbsd -maix-struct-return -msvr4-struct-return -mabi=</code><i>abi-type</i> <code>-msecure-plt -mbss-plt -misel -mno-isel -misel=yes -misel=no -mspe -mno-spe -mspe=yes -mspe=no -mvrsave -mno-vrsave -mfloat-gprs=yes -mfloat-gprs=no -mfloat-gprs=single -mfloat-gprs=double -mprototype -mno-prototype -msim -mmvme -mads -myellowknife -memb -msdata -msdata=</code><i>opt</i> <code>-mvxworks -mwindiss -G</code> <i>num</i> <code>-pthread</code> </p>
<p> <i>S/390 and zSeries Options</i> <code>-mtune=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mhard-float -msoft-float -mlong-double-64 -mlong-double-128 -mbackchain -mno-backchain -mpacked-stack -mno-packed-stack -msmall-exec -mno-small-exec -mmvcle -mno-mvcle -m64 -m31 -mdebug -mno-debug -mesa -mzarch -mtpf-trace -mno-tpf-trace -mfused-madd -mno-fused-madd -mwarn-framesize -mwarn-dynamicstack -mstack-size -mstack-guard</code> </p>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i> <code>-m1 -m2 -m2e -m3 -m3e -m4-nofpu -m4-single-only -m4-single -m4 -m4a-nofpu -m4a-single-only -m4a-single -m4a -m4al -m5-64media -m5-64media-nofpu -m5-32media -m5-32media-nofpu -m5-compact -m5-compact-nofpu -mb -ml -mdalign -mrelax -mbigtable -mfmovd -mhitachi -mrenesas -mno-renesas -mnomacsave -mieee -misize -mpadstruct -mspace -mprefergot -musermode -multcost=</code><i>number</i> <code>-mdiv=</code><i>strategy</i> <code>-mdivsi3_libfunc=</code><i>name</i> <code>-madjust-unroll -mindexed-addressing -mgettrcost=</code><i>number</i> <code>-mpt-fixed<br />
&nbsp;<wbr>-minvalid-symbols</code> </p>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mcmodel=</code><i>code-model</i> <code>-m32 -m64 -mapp-regs -mno-app-regs -mfaster-structs -mno-faster-structs -mfpu -mno-fpu -mhard-float -msoft-float -mhard-quad-float -msoft-quad-float -mimpure-text -mno-impure-text -mlittle-endian -mstack-bias -mno-stack-bias -munaligned-doubles -mno-unaligned-doubles -mv8plus -mno-v8plus -mvis -mno-vis -threads -pthreads -pthread</code> </p>
<p> <i>System V Options</i> <code>-Qy -Qn -YP,</code><i>paths</i> <code>-Ym,</code><i>dir</i> </p>
<p> <i>TMS320C3x/C4x Options</i> <code>-mcpu=</code><i>cpu</i> <code>-mbig -msmall -mregparm -mmemparm -mfast-fix -mmpyi -mbk -mti -mdp-isr-reload -mrpts=</code><i>count</i> <code>-mrptb -mdb -mloop-unsigned -mparallel-insns -mparallel-mpy -mpreserve-float</code> </p>
<p> <i>V850 Options</i> <code>-mlong-calls -mno-long-calls -mep -mno-ep -mprolog-function -mno-prolog-function -mspace -mtda=</code><i>n</i> <code>-msda=</code><i>n</i> <code>-mzda=</code><i>n</i> <code>-mapp-regs -mno-app-regs -mdisable-callt -mno-disable-callt -mv850e1 -mv850e -mv850 -mbig-switch</code> </p>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i> <code>-mg -mgnu -munix</code> </p>
<p> <i>x86-64 Options</i> See i386 and x86-64 Options. </p>
<p> <i>Xstormy16 Options</i> <code>-msim</code> </p>
<p> <i>Xtensa Options</i> <code>-mconst16 -mno-const16 -mfused-madd -mno-fused-madd -mtext-section-literals -mno-text-section-literals -mtarget-align -mno-target-align -mlongcalls -mno-longcalls</code> </p>
<p> <i>zSeries Options</i> See S/390 and zSeries Options.</p>
<dt><i>Code Generation Options</i></p>
<dd><code>-fcall-saved-</code><i>reg</i> <code>-fcall-used-</code><i>reg</i> <code>-ffixed-</code><i>reg</i> <code>-fexceptions -fnon-call-exceptions -funwind-tables -fasynchronous-unwind-tables -finhibit-size-directive -finstrument-functions -fno-common -fno-ident -fpcc-struct-return -fpic -fPIC -fpie -fPIE -fno-jump-tables -freg-struct-return -fshared-data -fshort-enums -fshort-double -fshort-wchar -fverbose-asm -fpack-struct[=</code><i>n</i><code>] -fstack-check -fstack-limit-register=</code><i>reg</i> <code>-fstack-limit-symbol=</code><i>sym</i> <code>-fargument-alias -fargument-noalias -fargument-noalias-global -fleading-underscore -ftls-model=</code><i>model</i> <code>-ftrapv -fwrapv -fbounds-check -fvisibility</code></dl>
<h2>Options Controlling the Kind of Output</h2>
<p>Compilation can involve up to four stages: preprocessing, compilation proper, assembly and linking, always in that order. <font SIZE="-1">GCC</font> is capable of preprocessing and compiling several files either into several assembler input files, or into one assembler input file; then each assembler input file produces an object file, and linking combines all the object files (those newly compiled, and those specified as input) into an executable file. </p>
<p> For any given input file, the file name suffix determines what kind of compilation is done:</p>
<dl>
<dt><i>file</i><code>.c</code></p>
<dd>C source code which must be preprocessed.</p>
<dt><i>file</i><code>.i</code></p>
<dd>C source code which should not be preprocessed.</p>
<dt><i>file</i><code>.ii</code></p>
<dd>C<font SIZE="-2">++</font> source code which should not be preprocessed.</p>
<dt><i>file</i><code>.m</code></p>
<dd>Objective-C source code. Note that you must link with the <i>libobjc</i> library to make an Objective-C program work.</p>
<dt><i>file</i><code>.mi</code></p>
<dd>Objective-C source code which should not be preprocessed.</p>
<dt><i>file</i><code>.mm</code></p>
<dd>
<dt><i>file</i><code>.M</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code. Note that you must link with the <i>libobjc</i> library to make an Objective-C<font SIZE="-2">++</font> program work. Note that <code>.M</code> refers to a literal capital M.</p>
<dt><i>file</i><code>.mii</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code which should not be preprocessed.</p>
<dt><i>file</i><code>.h</code></p>
<dd>C, C<font SIZE="-2">++</font>, Objective-C or Objective-C<font SIZE="-2">++</font> header file to be turned into a precompiled header.</p>
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
<dd>C<font SIZE="-2">++</font> source code which must be preprocessed. Note that in <code>.cxx</code>, the last two letters must both be literally <code>x</code>. Likewise, <code>.C</code> refers to a literal capital C.</p>
<dt><i>file</i><code>.mm</code></p>
<dd>
<dt><i>file</i><code>.M</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code which must be preprocessed.</p>
<dt><i>file</i><code>.mii</code></p>
<dd>Objective-C<font SIZE="-2">++</font> source code which should not be preprocessed.</p>
<dt><i>file</i><code>.hh</code></p>
<dd>
<dt><i>file</i><code>.H</code></p>
<dd>C<font SIZE="-2">++</font> header file to be turned into a precompiled header.</p>
<dt><i>file</i><code>.f</code></p>
<dd>
<dt><i>file</i><code>.for</code></p>
<dd>
<dt><i>file</i><code>.FOR</code></p>
<dd>Fixed form Fortran source code which should not be preprocessed.</p>
<dt><i>file</i><code>.F</code></p>
<dd>
<dt><i>file</i><code>.fpp</code></p>
<dd>
<dt><i>file</i><code>.FPP</code></p>
<dd>Fixed form Fortran source code which must be preprocessed (with the traditional preprocessor).</p>
<dt><i>file</i><code>.f90</code></p>
<dd>
<dt><i>file</i><code>.f95</code></p>
<dd>Free form Fortran source code which should not be preprocessed.</p>
<dt><i>file</i><code>.F90</code></p>
<dd>
<dt><i>file</i><code>.F95</code></p>
<dd>Free form Fortran source code which must be preprocessed (with the traditional preprocessor).</p>
<dt><i>file</i><code>.ads</code></p>
<dd>Ada source code file which contains a library unit declaration (a declaration of a package, subprogram, or generic, or a generic instantiation), or a library unit renaming declaration (a package, generic, or subprogram renaming declaration). Such files are also called <i>specs</i>.</p>
<dt><i>file</i><code>.adb</code></p>
<dd>Ada source code file containing a library unit body (a subprogram or package body). Such files are also called <i>bodies</i>.</p>
<dt><i>file</i><code>.s</code></p>
<dd>Assembler code.</p>
<dt><i>file</i><code>.S</code></p>
<dd>Assembler code which must be preprocessed.</p>
<dt><i>other</i></p>
<dd>An object file to be fed straight into linking. Any file name with no recognized suffix is treated this way.</dl>
<p> You can specify the input language explicitly with the <code>-x</code> option:</p>
<dl>
<dt><code>-x</code> <i>language</i></p>
<dd>Specify explicitly the <i>language</i> for the following input files (rather than letting the compiler choose a default based on the file name suffix). This option applies to all following input files until the next <code>-x</code> option. Possible values for <i>language</i> are: </p>
<pre> c c-header c-cpp-output
 c++ c++-header c++-cpp-output
 objective-c objective-c-header objective-c-cpp-output
 objective-c++ objective-c++-header objective-c++-cpp-output
 assembler assembler-with-cpp
 ada
 f95 f95-cpp-input
 java
 treelang</pre>
<dt><code>-x none</code></p>
<dd>Turn off any specification of a language, so that subsequent files are handled according to their file name suffixes (as they are if <code>-x</code> has not been used at all).</p>
<dt><code>-pass-exit-codes</code></p>
<dd>Normally the <code>gcc</code> program will exit with the code of 1 if any phase of the compiler returns a non-success return code. If you specify <code>-pass-exit-codes</code>, the <code>gcc</code> program will instead return with numerically highest error produced by any phase that returned an error indication.</dl>
<p> If you only want some of the stages of compilation, you can use <code>-x</code> (or filename suffixes) to tell <code>gcc</code> where to start, and one of the options <code>-c</code>, <code>-S</code>, or <code>-E</code> to say where <code>gcc</code> is to stop. Note that some combinations (for example, <code>-x cpp-output -E</code>) instruct <code>gcc</code> to do nothing at all.</p>
<dl>
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
<p> Input files which don&#8217;t require preprocessing are ignored.</p>
<dt><code>-o</code> <i>file</i></p>
<dd>Place output in file <i>file</i>. This applies regardless to whatever sort of output is being produced, whether it be an executable file, an object file, an assembler file or preprocessed C code. </p>
<p> If <code>-o</code> is not specified, the default is to put an executable file in <i>a.out</i>, the object file for <i>source.suffix</i> in <i>source.o</i>, its assembler file in <i>source.s</i>, a precompiled header file in <i>source.suffix.gch</i>, and all preprocessed C source on standard output.</p>
<dt><code>-v</code></p>
<dd>Print (on standard error output) the commands executed to run the stages of compilation. Also print the version number of the compiler driver program and of the preprocessor and the compiler proper.</p>
<dt><code>-###</code></p>
<dd>Like <code>-v</code> except the commands are not executed and all command arguments are quoted. This is useful for shell scripts to capture the driver-generated command lines.</p>
<dt><code>-pipe</code></p>
<dd>Use pipes rather than temporary files for communication between the various stages of compilation. This fails to work on some systems where the assembler is unable to read from a pipe; but the <font SIZE="-1">GNU</font> assembler has no trouble.</p>
<dt><code>-combine</code></p>
<dd>If you are compiling multiple source files, this option tells the driver to pass all the source files to the compiler at once (for those languages for which the compiler can handle this). This will allow intermodule analysis (<font SIZE="-1">IMA</font>) to be performed by the compiler. Currently the only language for which this is supported is C. If you pass source files for multiple languages to the driver, using this option, the driver will invoke the compiler(s) that support <font SIZE="-1">IMA</font> once each, passing each compiler all the source files appropriate for it. For those languages that do not support <font SIZE="-1">IMA</font> this option will be ignored, and the compiler will be invoked once for each source file in that language. If you use this option in conjunction with <code>-save-temps</code>, the compiler will generate multiple pre-processed files (one for each source file), but only one (combined) <i>.o</i> or <i>.s</i> file.</p>
<dt><code>&#8211;help</code></p>
<dd>Print (on the standard output) a description of the command line options understood by <code>gcc</code>. If the <code>-v</code> option is also specified then <code>&#8211;help</code> will also be passed on to the various processes invoked by <code>gcc</code>, so that they can display the command line options they accept. If the <code>-Wextra</code> option is also specified then command line options which have no documentation associated with them will also be displayed.</p>
<dt><code>&#8211;target-help</code></p>
<dd>Print (on the standard output) a description of target specific command line options for each tool.</p>
<dt><code>&#8211;version</code></p>
<dd>Display the version number and copyrights of the invoked <font SIZE="-1">GCC</font>.</dl>
<h2>Compiling C<font SIZE="-2">++</font> Programs</h2>
<p>C<font SIZE="-2">++</font> source files conventionally use one of the suffixes <code>.C</code>, <code>.cc</code>, <code>.cpp</code>, <code>.CPP</code>, <code>.c++</code>, <code>.cp</code>, or <code>.cxx</code>; C<font SIZE="-2">++</font> header files often use <code>.hh</code> or <code>.H</code>; and preprocessed C<font SIZE="-2">++</font> files use the suffix <code>.ii</code>. <font SIZE="-1">GCC</font> recognizes files with these names and compiles them as C<font SIZE="-2">++</font> programs even if you call the compiler the same way as for compiling C programs (usually with the name <code>gcc</code>). </p>
<p> However, C<font SIZE="-2">++</font> programs often require class libraries as well as a compiler that understands the C<font SIZE="-2">++</font> language&#8212;and under some circumstances, you might want to compile programs or header files from standard input, or otherwise without a suffix that flags them as C<font SIZE="-2">++</font> programs. You might also like to precompile a C header file with a <code>.h</code> extension to be used in C<font SIZE="-2">++</font> compilations. <code>g++</code> is a program that calls <font SIZE="-1">GCC</font> with the default language set to C<font SIZE="-2">++</font>, and automatically specifies linking against the C<font SIZE="-2">++</font> library. On many systems, <code>g++</code> is also installed with the name <code>c++</code>. </p>
<p> When you compile C<font SIZE="-2">++</font> programs, you may specify many of the same command-line options that you use for compiling programs in any language; or command-line options meaningful for C and related languages; or options that are meaningful only for C<font SIZE="-2">++</font> programs.</p>
<h2>Options Controlling C Dialect</h2>
<p>The following options control the dialect of C (or languages derived from C, such as C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font>) that the compiler accepts:</p>
<dl>
<dt><code>-ansi</code></p>
<dd>In C mode, support all <font SIZE="-1">ISO</font> C90 programs. In C<font SIZE="-2">++</font> mode, remove <font SIZE="-1">GNU</font> extensions that conflict with <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>. </p>
<p> This turns off certain features of <font SIZE="-1">GCC</font> that are incompatible with <font SIZE="-1">ISO</font> C90 (when compiling C code), or of standard C<font SIZE="-2">++</font> (when compiling C<font SIZE="-2">++</font> code), such as the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, and predefined macros such as <tt>&quot;unix&quot;</tt> and <tt>&quot;vax&quot;</tt> that identify the type of system you are using. It also enables the undesirable and rarely used <font SIZE="-1">ISO</font> trigraph feature. For the C compiler, it disables recognition of C<font SIZE="-2">++</font> style <code>//</code> comments as well as the <tt>&quot;inline&quot;</tt> keyword. </p>
<p> The alternate keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__extension__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> continue to work despite <code>-ansi</code>. You would not want to use them in an <font SIZE="-1">ISO</font> C program, of course, but it is useful to put them in header files that might be included in compilations done with <code>-ansi</code>. Alternate predefined macros such as <tt>&quot;__unix__&quot;</tt> and <tt>&quot;__vax__&quot;</tt> are also available, with or without <code>-ansi</code>. </p>
<p> The <code>-ansi</code> option does not cause non-ISO programs to be rejected gratuitously. For that, <code>-pedantic</code> is required in addition to <code>-ansi</code>. </p>
<p> The macro <tt>&quot;__STRICT_ANSI__&quot;</tt> is predefined when the <code>-ansi</code> option is used. Some header files may notice this macro and refrain from declaring certain functions or defining certain macros that the <font SIZE="-1">ISO</font> standard doesn&#8217;t call for; this is to avoid interfering with any programs that might use these names for other things. </p>
<p> Functions which would normally be built in but do not have semantics defined by <font SIZE="-1">ISO</font> C (such as <tt>&quot;alloca&quot;</tt> and <tt>&quot;ffs&quot;</tt>) are not built-in functions with <code>-ansi</code> is used.</p>
<dt><code>-std=</code></p>
<dd>Determine the language standard. This option is currently only supported when compiling C or C<font SIZE="-2">++</font>. A value for this option must be provided; possible values are</p>
<dl>
<dd>
<dl>
<dt><code>c89</code></p>
<dd>
<dt><code>iso9899:1990</code></p>
<dd><font SIZE="-1">ISO</font> C90 (same as <code>-ansi</code>).</p>
<dt><code>iso9899:199409</code></p>
<dd><font SIZE="-1">ISO</font> C90 as modified in amendment 1.</p>
<dt><code>c99</code></p>
<dd>
<dt><code>c9x</code></p>
<dd>
<dt><code>iso9899:1999</code></p>
<dd>
<dt><code>iso9899:199x</code></p>
<dd><font SIZE="-1">ISO</font> C99. Note that this standard is not yet fully supported; see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/gcc-4.1/c99status.html">http://gcc.gnu.org/gcc-4.1/c99status.html</a></code>&gt; for more information. The names <code>c9x</code> and <code>iso9899:199x</code> are deprecated.</p>
<dt><code>gnu89</code></p>
<dd>Default, <font SIZE="-1">ISO</font> C90 plus <font SIZE="-1">GNU</font> extensions (including some C99 features).</p>
<dt><code>gnu99</code></p>
<dd>
<dt><code>gnu9x</code></p>
<dd><font SIZE="-1">ISO</font> C99 plus <font SIZE="-1">GNU</font> extensions. When <font SIZE="-1">ISO</font> C99 is fully implemented in <font SIZE="-1">GCC</font>, this will become the default. The name <code>gnu9x</code> is deprecated.</p>
<dt><code>c++98</code></p>
<dd>The 1998 <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> standard plus amendments.</p>
<dt><code>gnu++98</code></p>
<dd>The same as <code>-std=c++98</code> plus <font SIZE="-1">GNU</font> extensions. This is the default for C<font SIZE="-2">++</font> code.</dl>
</dl>
<dl>
<dd>Even when this option is not specified, you can still use some of the features of newer standards in so far as they do not conflict with previous C standards. For example, you may use <tt>&quot;__restrict__&quot;</tt> even when <code>-std=c99</code> is not specified. </p>
<p> The <code>-std</code> options specifying some version of <font SIZE="-1">ISO</font> C have the same effects as <code>-ansi</code>, except that features that were not in <font SIZE="-1">ISO</font> C90 but are in the specified version (for example, <code>//</code> comments and the <tt>&quot;inline&quot;</tt> keyword in <font SIZE="-1">ISO</font> C99) are not disabled.</dl>
<dt><code>-aux-info</code> <i>filename</i></p>
<dd>Output to the given filename prototyped declarations for all functions declared and/or defined in a translation unit, including those in header files. This option is silently ignored in any language other than C. </p>
<p> Besides declarations, the file indicates, in comments, the origin of each declaration (source file and line), whether the declaration was implicit, prototyped or unprototyped (<code>I</code>, <code>N</code> for new or <code>O</code> for old, respectively, in the first character after the line number and the colon), and whether it came from a declaration or a definition (<code>C</code> or <code>F</code>, respectively, in the following character). In the case of function definitions, a K&amp;R-style list of arguments followed by their declarations is also provided, inside comments, after the declaration.</p>
<dt><code>-fno-asm</code></p>
<dd>Do not recognize <tt>&quot;asm&quot;</tt>, <tt>&quot;inline&quot;</tt> or <tt>&quot;typeof&quot;</tt> as a keyword, so that code can use these words as identifiers. You can use the keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> instead. <code>-ansi</code> implies <code>-fno-asm</code>. </p>
<p> In C<font SIZE="-2">++</font>, this switch only affects the <tt>&quot;typeof&quot;</tt> keyword, since <tt>&quot;asm&quot;</tt> and <tt>&quot;inline&quot;</tt> are standard keywords. You may want to use the <code>-fno-gnu-keywords</code> flag instead, which has the same effect. In C99 mode (<code>-std=c99</code> or <code>-std=gnu99</code>), this switch only affects the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, since <tt>&quot;inline&quot;</tt> is a standard keyword in <font SIZE="-1">ISO</font> C99.</p>
<dt><code>-fno-builtin</code></p>
<dd>
<dt><code>-fno-builtin-</code><i>function</i></p>
<dd>Don&#8217;t recognize built-in functions that do not begin with <code>__builtin_</code> as prefix. </p>
<p> <font SIZE="-1">GCC</font> normally generates special code to handle certain built-in functions more efficiently; for instance, calls to <tt>&quot;alloca&quot;</tt> may become single instructions that adjust the stack directly, and calls to <tt>&quot;memcpy&quot;</tt> may become inline copy loops. The resulting code is often both smaller and faster, but since the function calls no longer appear as such, you cannot set a breakpoint on those calls, nor can you change the behavior of the functions by linking with a different library. In addition, when a function is recognized as a built-in function, <font SIZE="-1">GCC</font> may use information about that function to warn about problems with calls to that function, or to generate more efficient code, even if the resulting code still contains calls to that function. For example, warnings are given with <code>-Wformat</code> for bad calls to <tt>&quot;printf&quot;</tt>, when <tt>&quot;printf&quot;</tt> is built in, and <tt>&quot;strlen&quot;</tt> is known not to modify global memory. </p>
<p> With the <code>-fno-builtin-</code><i>function</i> option only the built-in function <i>function</i> is disabled. <i>function</i> must not begin with <code>__builtin_</code>. If a function is named this is not built-in in this version of <font SIZE="-1">GCC</font>, this option is ignored. There is no corresponding <code>-fbuiltin-</code><i>function</i> option; if you wish to enable built-in functions selectively when using <code>-fno-builtin</code> or <code>-ffreestanding</code>, you may define macros such as: </p>
<pre> #define <a href="//www.systutorials.com/docs/linux/man/n-abs/">abs</a>(n) __builtin_abs ((n))
 #define strcpy(d, s) __builtin_strcpy ((d), (s))</pre>
<dt><code>-fhosted</code></p>
<dd>Assert that compilation takes place in a hosted environment. This implies <code>-fbuiltin</code>. A hosted environment is one in which the entire standard library is available, and in which <tt>&quot;main&quot;</tt> has a return type of <tt>&quot;int&quot;</tt>. Examples are nearly everything except a kernel. This is equivalent to <code>-fno-freestanding</code>.</p>
<dt><code>-ffreestanding</code></p>
<dd>Assert that compilation takes place in a freestanding environment. This implies <code>-fno-builtin</code>. A freestanding environment is one in which the standard library may not exist, and program startup may not necessarily be at <tt>&quot;main&quot;</tt>. The most obvious example is an <font SIZE="-1">OS</font> kernel. This is equivalent to <code>-fno-hosted</code>.</p>
<dt><code>-fms-extensions</code></p>
<dd>Accept some non-standard constructs used in Microsoft header files. </p>
<p> Some cases of unnamed fields in structures and unions are only accepted with this option.</p>
<dt><code>-trigraphs</code></p>
<dd>Support <font SIZE="-1">ISO</font> C trigraphs. The <code>-ansi</code> option (and <code>-std</code> options for strict <font SIZE="-1">ISO</font> C conformance) implies <code>-trigraphs</code>.</p>
<dt><code>-no-integrated-cpp</code></p>
<dd>Performs a compilation in two passes: preprocessing and compiling. This option allows a user supplied &#8220;cc1&#8221;, &#8220;cc1plus&#8221;, or &#8220;cc1obj&#8221; via the <code>-B</code> option. The user supplied compilation step can then add in an additional preprocessing step after normal preprocessing but before compiling. The default is to use the integrated cpp (internal cpp) </p>
<p> The semantics of this option will change if &#8220;cc1&#8221;, &#8220;cc1plus&#8221;, and &#8220;cc1obj&#8221; are merged.</p>
<dt><code>-traditional</code></p>
<dd>
<dt><code>-traditional-cpp</code></p>
<dd>Formerly, these options caused <font SIZE="-1">GCC</font> to attempt to emulate a pre-standard C compiler. They are now only supported with the <code>-E</code> switch. The preprocessor continues to support a pre-standard mode. See the <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font> manual for details.</p>
<dt><code>-fcond-mismatch</code></p>
<dd>Allow conditional expressions with mismatched types in the second and third arguments. The value of such an expression is void. This option is not supported for C<font SIZE="-2">++</font>.</p>
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
<h2>Options Controlling C<font SIZE="-2">++</font> Dialect</h2>
<p>This section describes the command-line options that are only meaningful for C<font SIZE="-2">++</font> programs; but you can also use most of the <font SIZE="-1">GNU</font> compiler options regardless of what language your program is in. For example, you might compile a file <tt>&quot;firstClass.C&quot;</tt> like this: </p>
<pre> g++ -g -frepo -O -c firstClass.C</pre>
<p>In this example, only <code>-frepo</code> is an option meant only for C<font SIZE="-2">++</font> programs; you can use the other options with any language supported by <font SIZE="-1">GCC</font>. </p>
<p> Here is a list of options that are <i>only</i> for compiling C<font SIZE="-2">++</font> programs:</p>
<dl>
<dt><code>-fabi-version=</code><i>n</i></p>
<dd>Use version <i>n</i> of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font>. Version 2 is the version of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> that first appeared in G++ 3.4. Version 1 is the version of the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> that first appeared in G++ 3.2. Version 0 will always be the version that conforms most closely to the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> specification. Therefore, the <font SIZE="-1">ABI</font> obtained using version 0 will change as <font SIZE="-1">ABI</font> bugs are fixed. </p>
<p> The default is version 2.</p>
<dt><code>-fno-access-control</code></p>
<dd>Turn off all access checking. This switch is mainly useful for working around bugs in the access control code.</p>
<dt><code>-fcheck-new</code></p>
<dd>Check that the pointer returned by <tt>&quot;operator new&quot;</tt> is non-null before attempting to modify the storage allocated. This check is normally unnecessary because the C<font SIZE="-2">++</font> standard specifies that <tt>&quot;operator new&quot;</tt> will only return <tt>0</tt> if it is declared throw(), in which case the compiler will always check the return value even without this option. In all other cases, when <tt>&quot;operator new&quot;</tt> has a non-empty exception specification, memory exhaustion is signalled by throwing <tt>&quot;std::bad_alloc&quot;</tt>. See also <code>new (nothrow)</code>.</p>
<dt><code>-fconserve-space</code></p>
<dd>Put uninitialized or runtime-initialized global variables into the common segment, as C does. This saves space in the executable at the cost of not diagnosing duplicate definitions. If you compile with this flag and your program mysteriously crashes after <tt>&quot;main()&quot;</tt> has completed, you may have an object that is being destroyed twice because two definitions were merged. </p>
<p> This option is no longer useful on most targets, now that support has been added for putting variables into <font SIZE="-1">BSS</font> without making them common.</p>
<dt><code>-ffriend-injection</code></p>
<dd>Inject friend functions into the enclosing namespace, so that they are visible outside the scope of the class in which they are declared. Friend functions were documented to work this way in the old Annotated C<font SIZE="-2">++</font> Reference Manual, and versions of G++ before 4.1 always worked that way. However, in <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> a friend function which is not declared in an enclosing scope can only be found using argument dependent lookup. This option causes friends to be injected as they were in earlier releases. </p>
<p> This option is for compatibility, and may be removed in a future release of G++.</p>
<dt><code>-fno-const-strings</code></p>
<dd>Give string constants type <tt>&quot;char *&quot;</tt> instead of type <tt>&quot;const char *&quot;</tt>. By default, G++ uses type <tt>&quot;const char *&quot;</tt> as required by the standard. Even if you use <code>-fno-const-strings</code>, you cannot actually modify the value of a string constant. </p>
<p> This option might be removed in a future release of G++. For maximum portability, you should structure your code so that it works with string constants that have type <tt>&quot;const char *&quot;</tt>.</p>
<dt><code>-fno-elide-constructors</code></p>
<dd>The C<font SIZE="-2">++</font> standard allows an implementation to omit creating a temporary which is only used to initialize another object of the same type. Specifying this option disables that optimization, and forces G++ to call the copy constructor in all cases.</p>
<dt><code>-fno-enforce-eh-specs</code></p>
<dd>Don&#8217;t generate code to check for violation of exception specifications at runtime. This option violates the C<font SIZE="-2">++</font> standard, but may be useful for reducing code size in production builds, much like defining <font SIZE="-1"><code>NDEBUG</code></font>. This does not give user code permission to throw exceptions in violation of the exception specifications; the compiler will still optimize based on the specifications, so throwing an unexpected exception will result in undefined behavior.</p>
<dt><code>-ffor-scope</code></p>
<dd>
<dt><code>-fno-for-scope</code></p>
<dd>If <code>-ffor-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> is limited to the <code>for</code> loop itself, as specified by the C<font SIZE="-2">++</font> standard. If <code>-fno-for-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> extends to the end of the enclosing scope, as was the case in old versions of G++, and other (traditional) implementations of C<font SIZE="-2">++</font>. </p>
<p> The default if neither flag is given to follow the standard, but to allow and give a warning for old-style code that would otherwise be invalid, or have different behavior.</p>
<dt><code>-fno-gnu-keywords</code></p>
<dd>Do not recognize <tt>&quot;typeof&quot;</tt> as a keyword, so that code can use this word as an identifier. You can use the keyword <tt>&quot;__typeof__&quot;</tt> instead. <code>-ansi</code> implies <code>-fno-gnu-keywords</code>.</p>
<dt><code>-fno-implicit-templates</code></p>
<dd>Never emit code for non-inline templates which are instantiated implicitly (i.e. by use); only emit code for explicit instantiations.</p>
<dt><code>-fno-implicit-inline-templates</code></p>
<dd>Don&#8217;t emit code for implicit instantiations of inline templates, either. The default is to handle inlines differently so that compiles with and without optimization will need the same set of explicit instantiations.</p>
<dt><code>-fno-implement-inlines</code></p>
<dd>To save space, do not emit out-of-line copies of inline functions controlled by <code>#pragma implementation</code>. This will cause linker errors if these functions are not inlined everywhere they are called.</p>
<dt><code>-fms-extensions</code></p>
<dd>Disable pedantic warnings about constructs used in <font SIZE="-1">MFC</font>, such as implicit int and getting a pointer to member function via non-standard syntax.</p>
<dt><code>-fno-nonansi-builtins</code></p>
<dd>Disable built-in declarations of functions that are not mandated by <font SIZE="-1">ANSI/ISO</font> C. These include <tt>&quot;ffs&quot;</tt>, <tt>&quot;alloca&quot;</tt>, <tt>&quot;_exit&quot;</tt>, <tt>&quot;index&quot;</tt>, <tt>&quot;bzero&quot;</tt>, <tt>&quot;conjf&quot;</tt>, and other related functions.</p>
<dt><code>-fno-operator-names</code></p>
<dd>Do not treat the operator name keywords <tt>&quot;and&quot;</tt>, <tt>&quot;bitand&quot;</tt>, <tt>&quot;bitor&quot;</tt>, <tt>&quot;compl&quot;</tt>, <tt>&quot;not&quot;</tt>, <tt>&quot;or&quot;</tt> and <tt>&quot;xor&quot;</tt> as synonyms as keywords.</p>
<dt><code>-fno-optional-diags</code></p>
<dd>Disable diagnostics that the standard says a compiler does not need to issue. Currently, the only such diagnostic issued by G++ is the one for a name having multiple meanings within a class.</p>
<dt><code>-fpermissive</code></p>
<dd>Downgrade some diagnostics about nonconformant code from errors to warnings. Thus, using <code>-fpermissive</code> will allow some nonconforming code to compile.</p>
<dt><code>-frepo</code></p>
<dd>Enable automatic template instantiation at link time. This option also implies <code>-fno-implicit-templates</code>.</p>
<dt><code>-fno-rtti</code></p>
<dd>Disable generation of information about every class with virtual functions for use by the C<font SIZE="-2">++</font> runtime type identification features (<code>dynamic_cast</code> and <code>typeid</code>). If you don&#8217;t use those parts of the language, you can save some space by using this flag. Note that exception handling uses the same information, but it will generate it as needed.</p>
<dt><code>-fstats</code></p>
<dd>Emit statistics about front-end processing at the end of the compilation. This information is generally only useful to the G++ development team.</p>
<dt><code>-ftemplate-depth-</code><i>n</i></p>
<dd>Set the maximum instantiation depth for template classes to <i>n</i>. A limit on the template instantiation depth is needed to detect endless recursions during template class instantiation. <font SIZE="-1">ANSI/ISO</font> C<font SIZE="-2">++</font> conforming programs must not rely on a maximum depth greater than 17.</p>
<dt><code>-fno-threadsafe-statics</code></p>
<dd>Do not emit the extra code to use the routines specified in the C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font> for thread-safe initialization of local statics. You can use this option to reduce code size slightly in code that doesn&#8217;t need to be thread-safe.</p>
<dt><code>-fuse-cxa-atexit</code></p>
<dd>Register destructors for objects with static storage duration with the <tt>&quot;__cxa_atexit&quot;</tt> function rather than the <tt>&quot;atexit&quot;</tt> function. This option is required for fully standards-compliant handling of static destructors, but will only work if your C library supports <tt>&quot;__cxa_atexit&quot;</tt>.</p>
<dt><code>-fvisibility-inlines-hidden</code></p>
<dd>Causes all inlined methods to be marked with <tt>&quot;__attribute__ ((visibility (&quot;hidden&quot;)))&quot;</tt> so that they do not appear in the export table of a <font SIZE="-1">DSO</font> and do not require a <font SIZE="-1">PLT</font> indirection when used within the <font SIZE="-1">DSO</font>. Enabling this option can have a dramatic effect on load and link times of a <font SIZE="-1">DSO</font> as it massively reduces the size of the dynamic export table when the library makes heavy use of templates. While it can cause bloating through duplication of code within each <font SIZE="-1">DSO</font> where it is used, often the wastage is less than the considerable space occupied by a long symbol name in the export table which is typical when using templates and namespaces. For even more savings, combine with the <code>-fvisibility=hidden</code> switch.</p>
<dt><code>-fno-weak</code></p>
<dd>Do not use weak symbol support, even if it is provided by the linker. By default, G++ will use weak symbols if they are available. This option exists only for testing, and should not be used by end-users; it will result in inferior code and has no benefits. This option may be removed in a future release of G++.</p>
<dt><code>-nostdinc++</code></p>
<dd>Do not search for header files in the standard directories specific to C<font SIZE="-2">++</font>, but do still search the other standard directories. (This option is used when building the C<font SIZE="-2">++</font> library.)</dl>
<p> In addition, these optimization, warning, and code generation options have meanings only for C<font SIZE="-2">++</font> programs:</p>
<dl>
<dt><code>-fno-default-inline</code></p>
<dd>Do not assume <code>inline</code> for functions defined inside a class scope.<br />
&nbsp;<wbr>&nbsp;<wbr>Note that these functions will have linkage like inline functions; they just won&#8217;t be inlined by default.</p>
<dt><code>-Wabi</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn when G++ generates code that is probably not compatible with the vendor-neutral C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font>. Although an effort has been made to warn about all such cases, there are probably some cases that are not warned about, even though G++ is generating incompatible code. There may also be cases where warnings are emitted even though the code that is generated will be compatible. </p>
<p> You should rewrite your code to avoid these warnings if you are concerned about the fact that code generated by G++ may not be binary compatible with code generated by other compilers. </p>
<p> The known incompatibilities at this point include:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Incorrect handling of tail-padding for bit-fields. G++ may attempt to pack data into the same byte as a base class. For example: </p>
<pre> struct A { virtual void f(); int f1 : 1; };
 struct B : public A { int f2 : 1; };</pre>
<p>In this case, G++ will place <tt>&quot;B::f2&quot;</tt> into the same byte as<tt>&quot;A::f1&quot;</tt>; other compilers will not. You can avoid this problem by explicitly padding <tt>&quot;A&quot;</tt> so that its size is a multiple of the byte size on your platform; that will cause G++ and other compilers to layout <tt>&quot;B&quot;</tt> identically.</p>
<dt>*</p>
<dd>Incorrect handling of tail-padding for virtual bases. G++ does not use tail padding when laying out virtual bases. For example: </p>
<pre> struct A { virtual void f(); char c1; };
 struct B { B(); char c2; };
 struct C : public A, public virtual B {};</pre>
<p>In this case, G++ will not place <tt>&quot;B&quot;</tt> into the tail-padding for <tt>&quot;A&quot;</tt>; other compilers will. You can avoid this problem by explicitly padding <tt>&quot;A&quot;</tt> so that its size is a multiple of its alignment (ignoring virtual base classes); that will cause G++ and other compilers to layout <tt>&quot;C&quot;</tt> identically.</p>
<dt>*</p>
<dd>Incorrect handling of bit-fields with declared widths greater than that of their underlying types, when the bit-fields appear in a union. For example: </p>
<pre> union U { int i : 4096; };</pre>
<p>Assuming that an <tt>&quot;int&quot;</tt> does not have 4096 bits, G++ will make the union too small by the number of bits in an <tt>&quot;int&quot;</tt>.</p>
<dt>*</p>
<dd>Empty classes can be placed at incorrect offsets. For example: </p>
<pre> struct A {};</pre>
<pre> struct B {
 A a;
 virtual void f ();
 };</pre>
<pre> struct C : public B, public A {};</pre>
<p>G++ will place the <tt>&quot;A&quot;</tt> base class of <tt>&quot;C&quot;</tt> at a nonzero offset; it should be placed at offset zero. G++ mistakenly believes that the <tt>&quot;A&quot;</tt> data member of <tt>&quot;B&quot;</tt> is already at offset zero.</p>
<dt>*</p>
<dd>Names of template functions whose types involve <tt>&quot;typename&quot;</tt> or template template parameters can be mangled incorrectly. </p>
<pre> template &lt;typename Q&gt;
 void f(typename Q::X) {}</pre>
<pre> template &lt;template &lt;typename&gt; class Q&gt;
 void f(typename Q&lt;int&gt;::X) {}</pre>
<p>Instantiations of these templates may be mangled incorrectly.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-Wctor-dtor-privacy</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class seems unusable because all the constructors or destructors in that class are private, and it has neither friends nor public static member functions.</p>
<dt><code>-Wnon-virtual-dtor</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a class appears to be polymorphic, thereby requiring a virtual destructor, yet it declares a non-virtual one. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wreorder</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn when the order of member initializers given in the code does not match the order in which they must be executed. For instance: </p>
<pre> struct A {
 int i;
 int j;
 A(): j (0), i (1) { }
 };</pre>
<p>The compiler will rearrange the member initializers for <code>i</code> and <code>j</code> to match the declaration order of the members, emitting a warning to that effect. This warning is enabled by <code>-Wall</code>.</dl>
<p> The following <code>-W&#8230;</code> options are not affected by <code>-Wall</code>.</p>
<dl>
<dt><code>-Weffc++</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn about violations of the following style guidelines from Scott Meyers&#8217; <i>Effective C<font SIZE="-2">++</font></i> book:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Item 11: Define a copy constructor and an assignment operator for classes with dynamically allocated memory.</p>
<dt>*</p>
<dd>Item 12: Prefer initialization to assignment in constructors.</p>
<dt>*</p>
<dd>Item 14: Make destructors virtual in base classes.</p>
<dt>*</p>
<dd>Item 15: Have <tt>&quot;operator=&quot;</tt> return a reference to <tt>*this</tt>.</p>
<dt>*</p>
<dd>Item 23: Don&#8217;t try to return a reference when you must return an object.</dl>
</dl>
<dl>
<dd>Also warn about violations of the following style guidelines from Scott Meyers&#8217; <i>More Effective C<font SIZE="-2">++</font></i> book:</p>
<dl>
<dt>*</p>
<dd>Item 6: Distinguish between prefix and postfix forms of increment and decrement operators.</p>
<dt>*</p>
<dd>Item 7: Never overload <tt>&quot;&amp;&amp;&quot;</tt>, <tt>&quot;||&quot;</tt>, or <tt>&quot;,&quot;</tt>.</dl>
</dl>
<dl>
<dd>When selecting this option, be aware that the standard library headers do not obey all of these guidelines; use <code>grep -v</code> to filter out those warnings.</dl>
<dt><code>-Wno-deprecated</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Do not warn about usage of deprecated features.</p>
<dt><code>-Wstrict-null-sentinel</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn also about the use of an uncasted <tt>&quot;NULL&quot;</tt> as sentinel. When compiling only with <font SIZE="-1">GCC</font> this is a valid sentinel, as <tt>&quot;NULL&quot;</tt> is defined to <tt>&quot;__null&quot;</tt>. Although it is a null pointer constant not a null pointer, it is guaranteed to of the same size as a pointer. But this use is not portable across different compilers.</p>
<dt><code>-Wno-non-template-friend</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Disable warnings when non-templatized friend functions are declared within a template. Since the advent of explicit template specification support in G++, if the name of the friend is an unqualified-id (i.e., <code>friend foo(int)</code>), the C<font SIZE="-2">++</font> language specification demands that the friend declare or define an ordinary, nontemplate function. (Section 14.5.3). Before G++ implemented explicit specification, unqualified-ids could be interpreted as a particular specialization of a templatized function. Because this non-conforming behavior is no longer the default behavior for G++, <code>-Wnon-template-friend</code> allows the compiler to check existing code for potential trouble spots and is on by default. This new compiler behavior can be turned off with <code>-Wno-non-template-friend</code> which keeps the conformant compiler code but disables the helpful warning.</p>
<dt><code>-Wold-style-cast</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn if an old-style (C-style) cast to a non-void type is used within a C<font SIZE="-2">++</font> program. The new-style casts (<code>dynamic_cast</code>, <code>static_cast</code>, <code>reinterpret_cast</code>, and <code>const_cast</code>) are less vulnerable to unintended effects and much easier to search for.</p>
<dt><code>-Woverloaded-virtual</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn when a function declaration hides virtual functions from a base class. For example, in: </p>
<pre> struct A {
 virtual void f();
 };</pre>
<pre> struct B: public A {
 void f(int);
 };</pre>
<p>the <tt>&quot;A&quot;</tt> class version of <tt>&quot;f&quot;</tt> is hidden in <tt>&quot;B&quot;</tt>, and code like: </p>
<pre> B* b;
 b-&gt;f();</pre>
<p>will fail to compile.</p>
<dt><code>-Wno-pmf-conversions</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Disable the diagnostic for converting a bound pointer to member function to a plain pointer.</p>
<dt><code>-Wsign-promo</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Warn when overload resolution chooses a promotion from unsigned or enumerated type to a signed type, over a conversion to an unsigned type of the same size. Previous versions of G++ would try to preserve unsignedness, but the standard mandates the current behavior. </p>
<pre> struct A {
 operator int ();
 A&amp; operator = (int);
 };</pre>
<pre> main ()
 {
 A a,b;
 a = b;
 }</pre>
<p>In this example, G++ will synthesize a default <code>A&amp; operator = (const A&amp;);</code>, while cfront will use the user-defined <code>operator =</code>.</dl>
<h2>Options Controlling Objective-C and Objective-C<font SIZE="-2">++</font> Dialects</h2>
<p>(<font SIZE="-1">NOTE:</font> This manual does not describe the Objective-C and Objective-C<font SIZE="-2">++</font> languages themselves. See </p>
<p> This section describes the command-line options that are only meaningful for Objective-C and Objective-C<font SIZE="-2">++</font> programs, but you can also use most of the language-independent <font SIZE="-1">GNU</font> compiler options. For example, you might compile a file <tt>&quot;some_class.m&quot;</tt> like this: </p>
<pre> gcc -g -fgnu-runtime -O -c some_class.m</pre>
<p>In this example, <code>-fgnu-runtime</code> is an option meant only for Objective-C and Objective-C<font SIZE="-2">++</font> programs; you can use the other options with any language supported by <font SIZE="-1">GCC</font>. </p>
<p> Note that since Objective-C is an extension of the C language, Objective-C compilations may also use options specific to the C front-end (e.g., <code>-Wtraditional</code>). Similarly, Objective-C<font SIZE="-2">++</font> compilations may use C<font SIZE="-2">++</font>-specific options (e.g., <code>-Wabi</code>). </p>
<p> Here is a list of options that are <i>only</i> for compiling Objective-C and Objective-C<font SIZE="-2">++</font> programs:</p>
<dl>
<dt><code>-fconstant-string-class=</code><i>class-name</i></p>
<dd>Use <i>class-name</i> as the name of the class to instantiate for each literal string specified with the syntax <tt>&quot;@&quot;...&quot;&quot;</tt>. The default class name is <tt>&quot;NXConstantString&quot;</tt> if the <font SIZE="-1">GNU</font> runtime is being used, and <tt>&quot;NSConstantString&quot;</tt> if the NeXT runtime is being used (see below). The <code>-fconstant-cfstrings</code> option, if also present, will override the <code>-fconstant-string-class</code> setting and cause <tt>&quot;@&quot;...&quot;&quot;</tt> literals to be laid out as constant CoreFoundation strings.</p>
<dt><code>-fgnu-runtime</code></p>
<dd>Generate object code compatible with the standard <font SIZE="-1">GNU</font> Objective-C runtime. This is the default for most types of systems.</p>
<dt><code>-fnext-runtime</code></p>
<dd>Generate output compatible with the NeXT runtime. This is the default for NeXT-based systems, including Darwin and Mac <font SIZE="-1">OS</font> X. The macro <tt>&quot;__NEXT_RUNTIME__&quot;</tt> is predefined if (and only if) this option is used.</p>
<dt><code>-fno-nil-receivers</code></p>
<dd>Assume that all Objective-C message dispatches (e.g., <tt>&quot;[receiver message:arg]&quot;</tt>) in this translation unit ensure that the receiver is not <tt>&quot;nil&quot;</tt>. This allows for more efficient entry points in the runtime to be used. Currently, this option is only available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS</font> X 10.3 and later.</p>
<dt><code>-fobjc-call-cxx-cdtors</code></p>
<dd>For each Objective-C class, check if any of its instance variables is a C<font SIZE="-2">++</font> object with a non-trivial default constructor. If so, synthesize a special <tt>&quot;- (id) .cxx_construct&quot;</tt> instance method that will run non-trivial default constructors on any such instance variables, in order, and then return <tt>&quot;self&quot;</tt>. Similarly, check if any instance variable is a C<font SIZE="-2">++</font> object with a non-trivial destructor, and if so, synthesize a special <tt>&quot;- (void) .cxx_destruct&quot;</tt> method that will run all such default destructors, in reverse order. </p>
<p> The <tt>&quot;- (id) .cxx_construct&quot;</tt> and/or <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods thusly generated will only operate on instance variables declared in the current Objective-C class, and not those inherited from superclasses. It is the responsibility of the Objective-C runtime to invoke all such methods in an object&#8217;s inheritance hierarchy. The <tt>&quot;- (id) .cxx_construct&quot;</tt> methods will be invoked by the runtime immediately after a new object instance is allocated; the <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods will be invoked immediately before the runtime deallocates an object instance. </p>
<p> As of this writing, only the NeXT runtime on Mac <font SIZE="-1">OS</font> X 10.4 and later has support for invoking the <tt>&quot;- (id) .cxx_construct&quot;</tt> and <tt>&quot;- (void) .cxx_destruct&quot;</tt> methods.</p>
<dt><code>-fobjc-direct-dispatch</code></p>
<dd>Allow fast jumps to the message dispatcher. On Darwin this is accomplished via the comm page.</p>
<dt><code>-fobjc-exceptions</code></p>
<dd>Enable syntactic support for structured exception handling in Objective-C, similar to what is offered by C<font SIZE="-2">++</font> and Java. Currently, this option is only available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS</font> X 10.3 and later. </p>
<pre> @try {
 ...
 @throw expr;
 ...
 }
 @catch (AnObjCClass *exc) {
 ...
 @throw expr;
 ...
 @throw;
 ...
 }
 @catch (AnotherClass *exc) {
 ...
 }
 @catch (id allOthers) {
 ...
 }
 @finally {
 ...
 @throw expr;
 ...
 }</pre>
<p>The <tt>@throw</tt> statement may appear anywhere in an Objective-C or Objective-C<font SIZE="-2">++</font> program; when used inside of a <tt>@catch</tt> block, the <tt>@throw</tt> may appear without an argument (as shown above), in which case the object caught by the <tt>@catch</tt> will be rethrown. </p>
<p> Note that only (pointers to) Objective-C objects may be thrown and caught using this scheme. When an object is thrown, it will be caught by the nearest <tt>@catch</tt> clause capable of handling objects of that type, analogously to how <tt>&quot;catch&quot;</tt> blocks work in C<font SIZE="-2">++</font> and Java. A <tt>&quot;@catch(id ...)&quot;</tt> clause (as shown above) may also be provided to catch any and all Objective-C exceptions not caught by previous <tt>@catch</tt> clauses (if any). </p>
<p> The <tt>@finally</tt> clause, if present, will be executed upon exit from the immediately preceding <tt>&quot;@try ... @catch&quot;</tt> section. This will happen regardless of whether any exceptions are thrown, caught or rethrown inside the <tt>&quot;@try ... @catch&quot;</tt> section, analogously to the behavior of the <tt>&quot;finally&quot;</tt> clause in Java. </p>
<p> There are several caveats to using the new exception mechanism:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Although currently designed to be binary compatible with <tt>&quot;NS_HANDLER&quot;</tt>-style idioms provided by the <tt>&quot;NSException&quot;</tt> class, the new exceptions can only be used on Mac <font SIZE="-1">OS</font> X 10.3 (Panther) and later systems, due to additional functionality needed in the (NeXT) Objective-C runtime.</p>
<dt>*</p>
<dd>As mentioned above, the new exceptions do not support handling types other than Objective-C objects. Furthermore, when used from Objective-C<font SIZE="-2">++</font>, the Objective-C exception model does not interoperate with C<font SIZE="-2">++</font> exceptions at this time. This means you cannot <tt>@throw</tt> an exception from Objective-C and <tt>&quot;catch&quot;</tt> it in C<font SIZE="-2">++</font>, or vice versa (i.e., <tt>&quot;throw ... @catch&quot;</tt>).</dl>
</dl>
<dl>
<dd>The <code>-fobjc-exceptions</code> switch also enables the use of synchronization blocks for thread-safe execution: </p>
<pre> @synchronized (ObjCClass *guard) {
 ...
 }</pre>
<p>Upon entering the <tt>@synchronized</tt> block, a thread of execution shall first check whether a lock has been placed on the corresponding <tt>&quot;guard&quot;</tt> object by another thread. If it has, the current thread shall wait until the other thread relinquishes its lock. Once <tt>&quot;guard&quot;</tt> becomes available, the current thread will place its own lock on it, execute the code contained in the <tt>@synchronized</tt> block, and finally relinquish the lock (thereby making <tt>&quot;guard&quot;</tt> available to other threads). </p>
<p> Unlike Java, Objective-C does not allow for entire methods to be marked <tt>@synchronized</tt>. Note that throwing exceptions out of <tt>@synchronized</tt> blocks is allowed, and will cause the guarding object to be unlocked properly.</dl>
<dt><code>-fobjc-gc</code></p>
<dd>Enable garbage collection (<font SIZE="-1">GC</font>) in Objective-C and Objective-C<font SIZE="-2">++</font> programs.</p>
<dt><code>-freplace-objc-classes</code></p>
<dd>Emit a special marker instructing <a href="/docs/linux/man/1-ld/">ld</a><code>(1)</code> not to statically link in the resulting object file, and allow <a href="/docs/linux/man/1-dyld/">dyld</a><code>(1)</code> to load it in at run time instead. This is used in conjunction with the Fix-and-Continue debugging mode, where the object file in question may be recompiled and dynamically reloaded in the course of program execution, without the need to restart the program itself. Currently, Fix-and-Continue functionality is only available in conjunction with the NeXT runtime on Mac <font SIZE="-1">OS</font> X 10.3 and later.</p>
<dt><code>-fzero-link</code></p>
<dd>When compiling for the NeXT runtime, the compiler ordinarily replaces calls to <tt>&quot;objc_getClass(&quot;...&quot;)&quot;</tt> (when the name of the class is known at compile time) with static class references that get initialized at load time, which improves run-time performance. Specifying the <code>-fzero-link</code> flag suppresses this behavior and causes calls to <tt>&quot;objc_getClass(&quot;...&quot;)&quot;</tt> to be retained. This is useful in Zero-Link debugging mode, since it allows for individual class implementations to be modified during program execution.</p>
<dt><code>-gen-decls</code></p>
<dd>Dump interface declarations for all classes seen in the source file to a file named <i>sourcename.decl</i>.</p>
<dt><code>-Wassign-intercept</code></p>
<dd>Warn whenever an Objective-C assignment is being intercepted by the garbage collector.</p>
<dt><code>-Wno-protocol</code></p>
<dd>If a class is declared to implement a protocol, a warning is issued for every method in the protocol that is not implemented by the class. The default behavior is to issue a warning for every method not explicitly implemented in the class, even if a method implementation is inherited from the superclass. If you use the <code>-Wno-protocol</code> option, then methods inherited from the superclass are considered to be implemented, and no warning is issued for them.</p>
<dt><code>-Wselector</code></p>
<dd>Warn if multiple methods of different types for the same selector are found during compilation. The check is performed on the list of methods in the final stage of compilation. Additionally, a check is performed for each selector appearing in a <tt>&quot;@selector(...)&quot;</tt> expression, and a corresponding method for that selector has been found during compilation. Because these checks scan the method table only at the end of compilation, these warnings are not produced if the final stage of compilation is not reached, for example because an error is found during compilation, or because the <code>-fsyntax-only</code> option is being used.</p>
<dt><code>-Wstrict-selector-match</code></p>
<dd>Warn if multiple methods with differing argument and/or return types are found for a given selector when attempting to send a message using this selector to a receiver of type <tt>&quot;id&quot;</tt> or <tt>&quot;Class&quot;</tt>. When this flag is off (which is the default behavior), the compiler will omit such warnings if any differences found are confined to types which share the same size and alignment.</p>
<dt><code>-Wundeclared-selector</code></p>
<dd>Warn if a <tt>&quot;@selector(...)&quot;</tt> expression referring to an undeclared selector is found. A selector is considered undeclared if no method with that name has been declared before the <tt>&quot;@selector(...)&quot;</tt> expression, either explicitly in an <tt>@interface</tt> or <tt>@protocol</tt> declaration, or implicitly in an <tt>@implementation</tt> section. This option always performs its checks as soon as a <tt>&quot;@selector(...)&quot;</tt> expression is found, while <code>-Wselector</code> only performs its checks in the final stage of compilation. This also enforces the coding style convention that methods and selectors must be declared before being used.</p>
<dt><code>-print-objc-runtime-info</code></p>
<dd>Generate C header describing the largest structure that is passed by value, if any.</dl>
<h2>Options to Control Diagnostic Messages Formatting</h2>
<p>Traditionally, diagnostic messages have been formatted irrespective of the output device&#8217;s aspect (e.g. its width, &#8230;). The options described below can be used to control the diagnostic messages formatting algorithm, e.g. how many characters per line, how often source location information should be reported. Right now, only the C<font SIZE="-2">++</font> front end can honor these options. However it is expected, in the near future, that the remaining front ends would be able to digest them correctly.</p>
<dl>
<dt><code>-fmessage-length=</code><i>n</i></p>
<dd>Try to format error messages so that they fit on lines of about <i>n</i> characters. The default is 72 characters for <code>g++</code> and 0 for the rest of the front ends supported by <font SIZE="-1">GCC</font>. If <i>n</i> is zero, then no line-wrapping will be done; each error message will appear on a single line.</p>
<dt><code>-fdiagnostics-show-location=once</code></p>
<dd>Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit <i>once</i> source location information; that is, in case the message is too long to fit on a single physical line and has to be wrapped, the source location won&#8217;t be emitted (as prefix) again, over and over, in subsequent continuation lines. This is the default behavior.</p>
<dt><code>-fdiagnostics-show-location=every-line</code></p>
<dd>Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit the same source location information (as prefix) for physical lines that result from the process of breaking a message which is too long to fit on a single line.</p>
<dt><code>-fdiagnostics-show-options</code></p>
<dd>This option instructs the diagnostic machinery to add text to each diagnostic emitted, which indicates which command line option directly controls that diagnostic, when such an option is known to the diagnostic machinery.</dl>
<h2>Options to Request or Suppress Warnings</h2>
<p>Warnings are diagnostic messages that report constructions which are not inherently erroneous but which are risky or suggest there may have been an error. </p>
<p> You can request many specific warnings with options beginning <code>-W</code>, for example <code>-Wimplicit</code> to request warnings on implicit declarations. Each of these specific warning options also has a negative form beginning <code>-Wno-</code> to turn off warnings; for example, <code>-Wno-implicit</code>. This manual lists only one of the two forms, whichever is not the default. </p>
<p> The following options control the amount and kinds of warnings produced by <font SIZE="-1">GCC</font>; for further, language-specific options also refer to <code>C<font SIZE="-2">++</font> Dialect Options</code> and <code>Objective-C and Objective-C<font SIZE="-2">++</font> Dialect Options</code>.</p>
<dl>
<dt><code>-fsyntax-only</code></p>
<dd>Check the code for syntax errors, but don&#8217;t do anything beyond that.</p>
<dt><code>-pedantic</code></p>
<dd>Issue all the warnings demanded by strict <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>; reject all programs that use forbidden extensions, and some other programs that do not follow <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>. For <font SIZE="-1">ISO</font> C, follows the version of the <font SIZE="-1">ISO</font> C standard specified by any <code>-std</code> option used. </p>
<p> Valid <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> programs should compile properly with or without this option (though a rare few will require <code>-ansi</code> or a <code>-std</code> option specifying the required version of <font SIZE="-1">ISO</font> C). However, without this option, certain <font SIZE="-1">GNU</font> extensions and traditional C and C<font SIZE="-2">++</font> features are supported as well. With this option, they are rejected. </p>
<p> <code>-pedantic</code> does not cause warning messages for use of the alternate keywords whose names begin and end with <code>__</code>. Pedantic warnings are also disabled in the expression that follows <tt>&quot;__extension__&quot;</tt>. However, only system header files should use these escape routes; application programs should avoid them. </p>
<p> Some users try to use <code>-pedantic</code> to check programs for strict <font SIZE="-1">ISO</font> C conformance. They soon find that it does not do quite what they want: it finds some non-ISO practices, but not all&#8212;only those for which <font SIZE="-1">ISO</font> C <i>requires</i> a diagnostic, and some others for which diagnostics have been added. </p>
<p> A feature to report any failure to conform to <font SIZE="-1">ISO</font> C might be useful in some instances, but would require considerable additional work and would be quite different from <code>-pedantic</code>. We don&#8217;t have plans to support such a feature in the near future. </p>
<p> Where the standard specified with <code>-std</code> represents a <font SIZE="-1">GNU</font> extended dialect of C, such as <code>gnu89</code> or <code>gnu99</code>, there is a corresponding <i>base standard</i>, the version of <font SIZE="-1">ISO</font> C on which the <font SIZE="-1">GNU</font> extended dialect is based. Warnings from <code>-pedantic</code> are given where they are required by the base standard. (It would not make sense for such warnings to be given only for features not in the specified <font SIZE="-1">GNU</font> C dialect, since by definition the <font SIZE="-1">GNU</font> dialects of C include all features the compiler supports with the given option, and there would be nothing to warn about.)</p>
<dt><code>-pedantic-errors</code></p>
<dd>Like <code>-pedantic</code>, except that errors are produced rather than warnings.</p>
<dt><code>-w</code></p>
<dd>Inhibit all warning messages.</p>
<dt><code>-Wno-import</code></p>
<dd>Inhibit warning messages about the use of <code>#import</code>.</p>
<dt><code>-Wchar-subscripts</code></p>
<dd>Warn if an array subscript has type <tt>&quot;char&quot;</tt>. This is a common cause of error, as programmers often forget that this type is signed on some machines. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wcomment</code></p>
<dd>Warn whenever a comment-start sequence <code>/*</code> appears in a <code>/*</code> comment, or whenever a Backslash-Newline appears in a <code>//</code> comment. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wfatal-errors</code></p>
<dd>This option causes the compiler to abort compilation on the first error occurred rather than trying to keep going and printing further error messages.</p>
<dt><code>-Wformat</code></p>
<dd>Check calls to <tt>&quot;printf&quot;</tt> and <tt>&quot;scanf&quot;</tt>, etc., to make sure that the arguments supplied have types appropriate to the format string specified, and that the conversions specified in the format string make sense. This includes standard functions, and others specified by format attributes, in the <tt>&quot;printf&quot;</tt>, <tt>&quot;scanf&quot;</tt>, <tt>&quot;strftime&quot;</tt> and <tt>&quot;strfmon&quot;</tt> (an X/Open extension, not in the C standard) families (or other target-specific families). Which functions are checked without format attributes having been specified depends on the standard version selected, and such checks of functions without the attribute specified are disabled by <code>-ffreestanding</code> or <code>-fno-builtin</code>. </p>
<p> The formats are checked against the format features supported by <font SIZE="-1">GNU</font> libc version 2.2. These include all <font SIZE="-1">ISO</font> C90 and C99 features, as well as features from the Single Unix Specification and some <font SIZE="-1">BSD</font> and <font SIZE="-1">GNU</font> extensions. Other library implementations may not support all these features; <font SIZE="-1">GCC</font> does not support warning about features that go beyond a particular library&#8217;s limitations. However, if <code>-pedantic</code> is used with <code>-Wformat</code>, warnings will be given about format features not in the selected standard version (but not for <tt>&quot;strfmon&quot;</tt> formats, since those are not in any version of the C standard). </p>
<p> Since <code>-Wformat</code> also checks for null format arguments for several functions, <code>-Wformat</code> also implies <code>-Wnonnull</code>. </p>
<p> <code>-Wformat</code> is included in <code>-Wall</code>. For more control over some aspects of format checking, the options <code>-Wformat-y2k</code>, <code>-Wno-format-extra-args</code>, <code>-Wno-format-zero-length</code>, <code>-Wformat-nonliteral</code>, <code>-Wformat-security</code>, and <code>-Wformat=2</code> are available, but are not included in <code>-Wall</code>.</p>
<dt><code>-Wformat-y2k</code></p>
<dd>If <code>-Wformat</code> is specified, also warn about <tt>&quot;strftime&quot;</tt> formats which may yield only a two-digit year.</p>
<dt><code>-Wno-format-extra-args</code></p>
<dd>If <code>-Wformat</code> is specified, do not warn about excess arguments to a <tt>&quot;printf&quot;</tt> or <tt>&quot;scanf&quot;</tt> format function. The C standard specifies that such arguments are ignored. </p>
<p> Where the unused arguments lie between used arguments that are specified with <code>$</code> operand number specifications, normally warnings are still given, since the implementation could not know what type to pass to <tt>&quot;va_arg&quot;</tt> to skip the unused arguments. However, in the case of <tt>&quot;scanf&quot;</tt> formats, this option will suppress the warning if the unused arguments are all pointers, since the Single Unix Specification says that such unused arguments are allowed.</p>
<dt><code>-Wno-format-zero-length</code></p>
<dd>If <code>-Wformat</code> is specified, do not warn about zero-length formats. The C standard specifies that zero-length formats are allowed.</p>
<dt><code>-Wformat-nonliteral</code></p>
<dd>If <code>-Wformat</code> is specified, also warn if the format string is not a string literal and so cannot be checked, unless the format function takes its format arguments as a <tt>&quot;va_list&quot;</tt>.</p>
<dt><code>-Wformat-security</code></p>
<dd>If <code>-Wformat</code> is specified, also warn about uses of format functions that represent possible security problems. At present, this warns about calls to <tt>&quot;printf&quot;</tt> and <tt>&quot;scanf&quot;</tt> functions where the format string is not a string literal and there are no format arguments, as in <tt>&quot;printf (foo);&quot;</tt>. This may be a security hole if the format string came from untrusted input and contains <code>%n</code>. (This is currently a subset of what <code>-Wformat-nonliteral</code> warns about, but in future warnings may be added to <code>-Wformat-security</code> that are not included in <code>-Wformat-nonliteral</code>.)</p>
<dt><code>-Wformat=2</code></p>
<dd>Enable <code>-Wformat</code> plus format checks not included in <code>-Wformat</code>. Currently equivalent to <code>-Wformat -Wformat-nonliteral -Wformat-security -Wformat-y2k</code>.</p>
<dt><code>-Wnonnull</code></p>
<dd>Warn about passing a null pointer for arguments marked as requiring a non-null value by the <tt>&quot;nonnull&quot;</tt> function attribute. </p>
<p> <code>-Wnonnull</code> is included in <code>-Wall</code> and <code>-Wformat</code>. It can be disabled with the <code>-Wno-nonnull</code> option.</p>
<dt><code>-Winit-self</code> (C, C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn about uninitialized variables which are initialized with themselves. Note this option can only be used with the <code>-Wuninitialized</code> option, which in turn only works with <code>-O1</code> and above. </p>
<p> For example, <font SIZE="-1">GCC</font> will warn about <tt>&quot;i&quot;</tt> being uninitialized in the following snippet only when <code>-Winit-self</code> has been specified: </p>
<pre> int f()
 {
 int i = i;
 return i;
 }</pre>
<dt><code>-Wimplicit-int</code></p>
<dd>Warn when a declaration does not specify a type. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wimplicit-function-declaration</code></p>
<dd>
<dt><code>-Werror-implicit-function-declaration</code></p>
<dd>Give a warning (or error) whenever a function is used before being declared. The form <code>-Wno-error-implicit-function-declaration</code> is not supported. This warning is enabled by <code>-Wall</code> (as a warning, not an error).</p>
<dt><code>-Wimplicit</code></p>
<dd>Same as <code>-Wimplicit-int</code> and <code>-Wimplicit-function-declaration</code>. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wmain</code></p>
<dd>Warn if the type of <code>main</code> is suspicious. <code>main</code> should be a function with external linkage, returning int, taking either zero arguments, two, or three arguments of appropriate types. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wmissing-braces</code></p>
<dd>Warn if an aggregate or union initializer is not fully bracketed. In the following example, the initializer for <code>a</code> is not fully bracketed, but that for <code>b</code> is fully bracketed. </p>
<pre> int a[2][2] = { 0, 1, 2, 3 };
 int b[2][2] = { { 0, 1 }, { 2, 3 } };</pre>
<p>This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wmissing-include-dirs</code> (C, C<font SIZE="-2">++</font>, Objective-C and Objective-C<font SIZE="-2">++</font> only)</p>
<dd>Warn if a user-supplied include directory does not exist.</p>
<dt><code>-Wparentheses</code></p>
<dd>Warn if parentheses are omitted in certain contexts, such as when there is an assignment in a context where a truth value is expected, or when operators are nested whose precedence people often get confused about. Only the warning for an assignment used as a truth value is supported when compiling C<font SIZE="-2">++</font>; the other warnings are only supported when compiling C. </p>
<p> Also warn if a comparison like <code>x&lt;=y&lt;=z</code> appears; this is equivalent to <code>(x&lt;=y ? 1 : 0) &lt;= z</code>, which is a different interpretation from that of ordinary mathematical notation. </p>
<p> Also warn about constructions where there may be confusion to which <tt>&quot;if&quot;</tt> statement an <tt>&quot;else&quot;</tt> branch belongs. Here is an example of such a case: </p>
<pre> {
 if (a)
 if (b)
 foo ();
 else
 bar ();
 }</pre>
<p>In C, every <tt>&quot;else&quot;</tt> branch belongs to the innermost possible <tt>&quot;if&quot;</tt> statement, which in this example is <tt>&quot;if (b)&quot;</tt>. This is often not what the programmer expected, as illustrated in the above example by indentation the programmer chose. When there is the potential for this confusion, <font SIZE="-1">GCC</font> will issue a warning when this flag is specified. To eliminate the warning, add explicit braces around the innermost <tt>&quot;if&quot;</tt> statement so there is no way the <tt>&quot;else&quot;</tt> could belong to the enclosing <tt>&quot;if&quot;</tt>. The resulting code would look like this: </p>
<pre> {
 if (a)
 {
 if (b)
 foo ();
 else
 bar ();
 }
 }</pre>
<p>This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wsequence-point</code></p>
<dd>Warn about code that may have undefined semantics because of violations of sequence point rules in the C standard. </p>
<p> The C standard defines the order in which expressions in a C program are evaluated in terms of <i>sequence points</i>, which represent a partial ordering between the execution of parts of the program: those executed before the sequence point, and those executed after it. These occur after the evaluation of a full expression (one which is not part of a larger expression), after the evaluation of the first operand of a <tt>&quot;&amp;&amp;&quot;</tt>, <tt>&quot;||&quot;</tt>, <tt>&quot;? :&quot;</tt> or <tt>&quot;,&quot;</tt> (comma) operator, before a function is called (but after the evaluation of its arguments and the expression denoting the called function), and in certain other places. Other than as expressed by the sequence point rules, the order of evaluation of subexpressions of an expression is not specified. All these rules describe only a partial order rather than a total order, since, for example, if two functions are called within one expression with no sequence point between them, the order in which the functions are called is not specified. However, the standards committee have ruled that function calls do not overlap. </p>
<p> It is not specified when between sequence points modifications to the values of objects take effect. Programs whose behavior depends on this have undefined behavior; the C standard specifies that &#8220;Between the previous and next sequence point an object shall have its stored value modified at most once by the evaluation of an expression. Furthermore, the prior value shall be read only to determine the value to be stored.&#8221;. If a program breaks these rules, the results on any particular implementation are entirely unpredictable. </p>
<p> Examples of code with undefined behavior are <tt>&quot;a = a++;&quot;</tt>, <tt>&quot;a[n] = b[n++]&quot;</tt> and <tt>&quot;a[i++] = i;&quot;</tt>. Some more complicated cases are not diagnosed by this option, and it may give an occasional false positive result, but in general it has been found fairly effective at detecting this sort of problem in programs. </p>
<p> The present implementation of this option only works for C programs. A future implementation may also work for C<font SIZE="-2">++</font> programs. </p>
<p> The C standard is worded confusingly, therefore there is some debate over the precise meaning of the sequence point rules in subtle cases. Links to discussions of the problem, including proposed formal definitions, may be found on the <font SIZE="-1">GCC</font> readings page, at &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/readings.html">http://gcc.gnu.org/readings.html</a></code>&gt;. </p>
<p> This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wreturn-type</code></p>
<dd>Warn whenever a function is defined with a return-type that defaults to <tt>&quot;int&quot;</tt>. Also warn about any <tt>&quot;return&quot;</tt> statement with no return-value in a function whose return-type is not <tt>&quot;void&quot;</tt>. </p>
<p> For C, also warn if the return type of a function has a type qualifier such as <tt>&quot;const&quot;</tt>. Such a type qualifier has no effect, since the value returned by a function is not an lvalue. <font SIZE="-1">ISO</font> C prohibits qualified <tt>&quot;void&quot;</tt> return types on function definitions, so such return types always receive a warning even without this option. </p>
<p> For C<font SIZE="-2">++</font>, a function without return type always produces a diagnostic message, even when <code>-Wno-return-type</code> is specified. The only exceptions are <code>main</code> and functions defined in system headers. </p>
<p> This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wswitch</code></p>
<dd>Warn whenever a <tt>&quot;switch&quot;</tt> statement has an index of enumerated type and lacks a <tt>&quot;case&quot;</tt> for one or more of the named codes of that enumeration. (The presence of a <tt>&quot;default&quot;</tt> label prevents this warning.) <tt>&quot;case&quot;</tt> labels outside the enumeration range also provoke warnings when this option is used. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wswitch-default</code></p>
<dd>Warn whenever a <tt>&quot;switch&quot;</tt> statement does not have a <tt>&quot;default&quot;</tt> case.</p>
<dt><code>-Wswitch-enum</code></p>
<dd>Warn whenever a <tt>&quot;switch&quot;</tt> statement has an index of enumerated type and lacks a <tt>&quot;case&quot;</tt> for one or more of the named codes of that enumeration. <tt>&quot;case&quot;</tt> labels outside the enumeration range also provoke warnings when this option is used.</p>
<dt><code>-Wtrigraphs</code></p>
<dd>Warn if any trigraphs are encountered that might change the meaning of the program (trigraphs within comments are not warned about). This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused-function</code></p>
<dd>Warn whenever a static function is declared but not defined or a non-inline static function is unused. This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunused-label</code></p>
<dd>Warn whenever a label is declared but not used. This warning is enabled by <code>-Wall</code>. </p>
<p> To suppress this warning use the <code>unused</code> attribute.</p>
<dt><code>-Wunused-parameter</code></p>
<dd>Warn whenever a function parameter is unused aside from its declaration. </p>
<p> To suppress this warning use the <code>unused</code> attribute.</p>
<dt><code>-Wunused-variable</code></p>
<dd>Warn whenever a local variable or non-constant static variable is unused aside from its declaration. This warning is enabled by <code>-Wall</code>. </p>
<p> To suppress this warning use the <code>unused</code> attribute.</p>
<dt><code>-Wunused-value</code></p>
<dd>Warn whenever a statement computes a result that is explicitly not used. This warning is enabled by <code>-Wall</code>. </p>
<p> To suppress this warning cast the expression to <code>void</code>.</p>
<dt><code>-Wunused</code></p>
<dd>All the above <code>-Wunused</code> options combined. </p>
<p> In order to get a warning about an unused function parameter, you must either specify <code>-Wextra -Wunused</code> (note that <code>-Wall</code> implies <code>-Wunused</code>), or separately specify <code>-Wunused-parameter</code>.</p>
<dt><code>-Wuninitialized</code></p>
<dd>Warn if an automatic variable is used without first being initialized or if a variable may be clobbered by a <tt>&quot;setjmp&quot;</tt> call. </p>
<p> These warnings are possible only in optimizing compilation, because they require data flow information that is computed only when optimizing. If you don&#8217;t specify <code>-O</code>, you simply won&#8217;t get these warnings. </p>
<p> If you want to warn about code which uses the uninitialized value of the variable in its own initializer, use the <code>-Winit-self</code> option. </p>
<p> These warnings occur for individual uninitialized or clobbered elements of structure, union or array variables as well as for variables which are uninitialized or clobbered as a whole. They do not occur for variables or elements declared <tt>&quot;volatile&quot;</tt>. Because these warnings depend on optimization, the exact variables or elements for which there are warnings will depend on the precise optimization options and version of <font SIZE="-1">GCC</font> used. </p>
<p> Note that there may be no warning about a variable that is used only to compute a value that itself is never used, because such computations may be deleted by data flow analysis before the warnings are printed. </p>
<p> These warnings are made optional because <font SIZE="-1">GCC</font> is not smart enough to see all the reasons why the code might be correct despite appearing to have an error. Here is one example of how this can happen: </p>
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
<p>If the value of <tt>&quot;y&quot;</tt> is always 1, 2 or 3, then <tt>&quot;x&quot;</tt> is always initialized, but <font SIZE="-1">GCC</font> doesn&#8217;t know this. Here is another common case: </p>
<pre> {
 int save_y;
 if (change_y) save_y = y, y = new_y;
 ...
 if (change_y) y = save_y;
 }</pre>
<p>This has no bug because <tt>&quot;save_y&quot;</tt> is used only if it is set. </p>
<p> This option also warns when a non-volatile automatic variable might be changed by a call to <tt>&quot;longjmp&quot;</tt>. These warnings as well are possible only in optimizing compilation. </p>
<p> The compiler sees only the calls to <tt>&quot;setjmp&quot;</tt>. It cannot know where <tt>&quot;longjmp&quot;</tt> will be called; in fact, a signal handler could call it at any point in the code. As a result, you may get a warning even when there is in fact no problem because <tt>&quot;longjmp&quot;</tt> cannot in fact be called at the place which would cause a problem. </p>
<p> Some spurious warnings can be avoided if you declare all the functions you use that never return as <tt>&quot;noreturn&quot;</tt>. </p>
<p> This warning is enabled by <code>-Wall</code>.</p>
<dt><code>-Wunknown-pragmas</code></p>
<dd>Warn when a #pragma directive is encountered which is not understood by <font SIZE="-1">GCC</font>. If this command line option is used, warnings will even be issued for unknown pragmas in system header files. This is not the case if the warnings were only enabled by the <code>-Wall</code> command line option.</p>
<dt><code>-Wno-pragmas</code></p>
<dd>Do not warn about misuses of pragmas, such as incorrect parameters, invalid syntax, or conflicts between pragmas. See also <code>-Wunknown-pragmas</code>.</p>
<dt><code>-Wstrict-aliasing</code></p>
<dd>This option is only active when <code>-fstrict-aliasing</code> is active. It warns about code which might break the strict aliasing rules that the compiler is using for optimization. The warning does not catch all cases, but does attempt to catch the more common pitfalls. It is included in <code>-Wall</code>.</p>
<dt><code>-Wstrict-aliasing=2</code></p>
<dd>This option is only active when <code>-fstrict-aliasing</code> is active. It warns about code which might break the strict aliasing rules that the compiler is using for optimization. This warning catches more cases than <code>-Wstrict-aliasing</code>, but it will also give a warning for some ambiguous cases that are safe.</p>
<dt><code>-Wall</code></p>
<dd>All of the above <code>-W</code> options combined. This enables all the warnings about constructions that some users consider questionable, and that are easy to avoid (or modify to prevent the warning), even in conjunction with macros. This also enables some language-specific warnings described in <code>C<font SIZE="-2">++</font> Dialect Options</code> and <code>Objective-C and Objective-C<font SIZE="-2">++</font> Dialect Options</code>.</dl>
<p> The following <code>-W&#8230;</code> options are not implied by <code>-Wall</code>. Some of them warn about constructions that users generally do not consider questionable, but which occasionally you might wish to check for; others warn about constructions that are necessary or hard to avoid in some cases, and there is no simple way to modify the code to suppress the warning.</p>
<dl>
<dt><code>-Wextra</code></p>
<dd>(This option used to be called <code>-W</code>. The older name is still supported, but the newer name is more descriptive.) Print extra warning messages for these events:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>A function can return either with or without a value. (Falling off the end of the function body is considered returning without a value.) For example, this function would evoke such a warning: </p>
<pre> foo (a)
 {
 if (a &gt; 0)
 return a;
 }</pre>
<dt>*</p>
<dd>An expression-statement or the left-hand side of a comma expression contains no side effects. To suppress the warning, cast the unused expression to void. For example, an expression such as <code>x[i,j]</code> will cause a warning, but <code>x[(void)i,j]</code> will not.</p>
<dt>*</p>
<dd>An unsigned value is compared against zero with <code>&lt;</code> or <code>&gt;=</code>.</p>
<dt>*</p>
<dd>Storage-class specifiers like <tt>&quot;static&quot;</tt> are not the first things in a declaration. According to the C Standard, this usage is obsolescent.</p>
<dt>*</p>
<dd>If <code>-Wall</code> or <code>-Wunused</code> is also specified, warn about unused arguments.</p>
<dt>*</p>
<dd>A comparison between signed and unsigned values could produce an incorrect result when the signed value is converted to unsigned. (But don&#8217;t warn if <code>-Wno-sign-compare</code> is also specified.)</p>
<dt>*</p>
<dd>An aggregate has an initializer which does not initialize all members. This warning can be independently controlled by <code>-Wmissing-field-initializers</code>.</p>
<dt>*</p>
<dd>A function parameter is declared without a type specifier in K&amp;R-style functions: </p>
<pre> void foo(bar) { }</pre>
<dt>*</p>
<dd>An empty body occurs in an <code>if</code> or <code>else</code> statement.</p>
<dt>*</p>
<dd>A pointer is compared against integer zero with <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, or <code>&gt;=</code>.</p>
<dt>*</p>
<dd>A variable might be changed by <code>longjmp</code> or <code>vfork</code>.</p>
<dt>*</p>
<dd>Any of several floating-point events that often indicate errors, such as overflow, underflow, loss of precision, etc.</p>
<dt>*&lt;(C<font SIZE="-2">++</font> only)&gt;</p>
<dd>An enumerator and a non-enumerator both appear in a conditional expression.</p>
<dt>*&lt;(C<font SIZE="-2">++</font> only)&gt;</p>
<dd>A non-static reference or non-static <code>const</code> member appears in a class without constructors.</p>
<dt>*&lt;(C<font SIZE="-2">++</font> only)&gt;</p>
<dd>Ambiguous virtual bases.</p>
<dt>*&lt;(C<font SIZE="-2">++</font> only)&gt;</p>
<dd>Subscripting an array which has been declared <code>register</code>.</p>
<dt>*&lt;(C<font SIZE="-2">++</font> only)&gt;</p>
<dd>Taking the address of a variable which has been declared <code>register</code>.</p>
<dt>*&lt;(C<font SIZE="-2">++</font> only)&gt;</p>
<dd>A base class is not initialized in a derived class&#8217; copy constructor.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-Wno-div-by-zero</code></p>
<dd>Do not warn about compile-time integer division by zero. Floating point division by zero is not warned about, as it can be a legitimate way of obtaining infinities and NaNs.</p>
<dt><code>-Wsystem-headers</code></p>
<dd>Print warning messages for constructs found in system header files. Warnings from system headers are normally suppressed, on the assumption that they usually do not indicate real problems and would only make the compiler output harder to read. Using this command line option tells <font SIZE="-1">GCC</font> to emit warnings from system headers as if they occurred in user code. However, note that using <code>-Wall</code> in conjunction with this option will <i>not</i> warn about unknown pragmas in system headers&#8212;for that, <code>-Wunknown-pragmas</code> must also be used.</p>
<dt><code>-Wfloat-equal</code></p>
<dd>Warn if floating point values are used in equality comparisons. </p>
<p> The idea behind this is that sometimes it is convenient (for the programmer) to consider floating-point values as approximations to infinitely precise real numbers. If you are doing this, then you need to compute (by analyzing the code, or in some other way) the maximum or likely maximum error that the computation introduces, and allow for it when performing comparisons (and when producing output, but that&#8217;s a different problem). In particular, instead of testing for equality, you would check to see whether the two values have ranges that overlap; and this is done with the relational operators, so equality comparisons are probably mistaken.</p>
<dt><code>-Wtraditional</code> (C only)</p>
<dd>Warn about certain constructs that behave differently in traditional and <font SIZE="-1">ISO</font> C. Also warn about <font SIZE="-1">ISO</font> C constructs that have no traditional C equivalent, and/or problematic constructs which should be avoided.</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Macro parameters that appear within string literals in the macro body. In traditional C macro replacement takes place within string literals, but does not in <font SIZE="-1">ISO</font> C.</p>
<dt>*</p>
<dd>In traditional C, some preprocessor directives did not exist. Traditional preprocessors would only consider a line to be a directive if the <code>#</code> appeared in column 1 on the line. Therefore <code>-Wtraditional</code> warns about directives that traditional C understands but would ignore because the <code>#</code> does not appear as the first character on the line. It also suggests you hide directives like <code>#pragma</code> not understood by traditional C by indenting them. Some traditional implementations would not recognize <code>#elif</code>, so it suggests avoiding it altogether.</p>
<dt>*</p>
<dd>A function-like macro that appears without arguments.</p>
<dt>*</p>
<dd>The unary plus operator.</p>
<dt>*</p>
<dd>The <code>U</code> integer constant suffix, or the <code>F</code> or <code>L</code> floating point constant suffixes. (Traditional C does support the <code>L</code> suffix on integer constants.) Note, these suffixes appear in macros defined in the system headers of most modern systems, e.g. the <code>_MIN</code>/<code>_MAX</code> macros in <tt>&quot;&lt;<a href="file:/usr/include/limits.h">limits.h</a>&gt;&quot;</tt>. Use of these macros in user code might normally lead to spurious warnings, however <font SIZE="-1">GCC</font>&#8216;s integrated preprocessor has enough context to avoid warning in these cases.</p>
<dt>*</p>
<dd>A function declared external in one block and then used after the end of the block.</p>
<dt>*</p>
<dd>A <tt>&quot;switch&quot;</tt> statement has an operand of type <tt>&quot;long&quot;</tt>.</p>
<dt>*</p>
<dd>A non-<tt>&quot;static&quot;</tt> function declaration follows a <tt>&quot;static&quot;</tt> one. This construct is not accepted by some traditional C compilers.</p>
<dt>*</p>
<dd>The <font SIZE="-1">ISO</font> type of an integer constant has a different width or signedness from its traditional type. This warning is only issued if the base of the constant is ten. I.e. hexadecimal or octal values, which typically represent bit patterns, are not warned about.</p>
<dt>*</p>
<dd>Usage of <font SIZE="-1">ISO</font> string concatenation is detected.</p>
<dt>*</p>
<dd>Initialization of automatic aggregates.</p>
<dt>*</p>
<dd>Identifier conflicts with labels. Traditional C lacks a separate namespace for labels.</p>
<dt>*</p>
<dd>Initialization of unions. If the initializer is zero, the warning is omitted. This is done under the assumption that the zero initializer in user code appears conditioned on e.g. <tt>&quot;__STDC__&quot;</tt> to avoid missing initializer warnings and relies on default initialization to zero in the traditional C case.</p>
<dt>*</p>
<dd>Conversions by prototypes between fixed/floating point values and vice versa. The absence of these prototypes when compiling with traditional C would cause serious problems. This is a subset of the possible conversion warnings, for the full set use <code>-Wconversion</code>.</p>
<dt>*</p>
<dd>Use of <font SIZE="-1">ISO</font> C style function definitions. This warning intentionally is <i>not</i> issued for prototype declarations or variadic functions because these <font SIZE="-1">ISO</font> C features will appear in your code when using libiberty&#8217;s traditional C compatibility macros, <tt>&quot;PARAMS&quot;</tt> and <tt>&quot;VPARAMS&quot;</tt>. This warning is also bypassed for nested functions because that feature is already a <font SIZE="-1">GCC</font> extension and thus not relevant to traditional C compatibility.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-Wdeclaration-after-statement</code> (C only)</p>
<dd>Warn when a declaration is found after a statement in a block. This construct, known from C<font SIZE="-2">++</font>, was introduced with <font SIZE="-1">ISO</font> C99 and is by default allowed in <font SIZE="-1">GCC</font>. It is not supported by <font SIZE="-1">ISO</font> C90 and was not supported by <font SIZE="-1">GCC</font> versions before <font SIZE="-1">GCC</font> 3.0.</p>
<dt><code>-Wundef</code></p>
<dd>Warn if an undefined identifier is evaluated in an <code>#if</code> directive.</p>
<dt><code>-Wno-endif-labels</code></p>
<dd>Do not warn whenever an <code>#else</code> or an <code>#endif</code> are followed by text.</p>
<dt><code>-Wshadow</code></p>
<dd>Warn whenever a local variable shadows another local variable, parameter or global variable or whenever a built-in function is shadowed.</p>
<dt><code>-Wlarger-than-</code><i>len</i></p>
<dd>Warn whenever an object of larger than <i>len</i> bytes is defined.</p>
<dt><code>-Wunsafe-loop-optimizations</code></p>
<dd>Warn if the loop cannot be optimized because the compiler could not assume anything on the bounds of the loop indices. With <code>-funsafe-loop-optimizations</code> warn if the compiler made such assumptions.</p>
<dt><code>-Wpointer-arith</code></p>
<dd>Warn about anything that depends on the &#8220;size of&#8221; a function type or of <tt>&quot;void&quot;</tt>. <font SIZE="-1">GNU</font> C assigns these types a size of 1, for convenience in calculations with <tt>&quot;void *&quot;</tt> pointers and pointers to functions.</p>
<dt><code>-Wbad-function-cast</code> (C only)</p>
<dd>Warn whenever a function call is cast to a non-matching type. For example, warn if <tt>&quot;int malloc()&quot;</tt> is cast to <tt>&quot;anything *&quot;</tt>.</p>
<dt><code>-Wc++-compat</code></p>
<dd>Warn about <font SIZE="-1">ISO</font> C constructs that are outside of the common subset of <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>, e.g. request for implicit conversion from <tt>&quot;void *&quot;</tt> to a pointer to non-<tt>&quot;void&quot;</tt> type.</p>
<dt><code>-Wcast-qual</code></p>
<dd>Warn whenever a pointer is cast so as to remove a type qualifier from the target type. For example, warn if a <tt>&quot;const char *&quot;</tt> is cast to an ordinary <tt>&quot;char *&quot;</tt>.</p>
<dt><code>-Wcast-align</code></p>
<dd>Warn whenever a pointer is cast such that the required alignment of the target is increased. For example, warn if a <tt>&quot;char *&quot;</tt> is cast to an <tt>&quot;int *&quot;</tt> on machines where integers can only be accessed at two- or four-byte boundaries.</p>
<dt><code>-Wwrite-strings</code></p>
<dd>When compiling C, give string constants the type <tt>&quot;const char[</tt>length<tt>]&quot;</tt> so that copying the address of one into a non-<tt>&quot;const&quot;</tt> <tt>&quot;char *&quot;</tt> pointer will get a warning; when compiling C<font SIZE="-2">++</font>, warn about the deprecated conversion from string constants to <tt>&quot;char *&quot;</tt>. These warnings will help you find at compile time code that can try to write into a string constant, but only if you have been very careful about using <tt>&quot;const&quot;</tt> in declarations and prototypes. Otherwise, it will just be a nuisance; this is why we did not make <code>-Wall</code> request these warnings.</p>
<dt><code>-Wconversion</code></p>
<dd>Warn if a prototype causes a type conversion that is different from what would happen to the same argument in the absence of a prototype. This includes conversions of fixed point to floating and vice versa, and conversions changing the width or signedness of a fixed point argument except when the same as the default promotion. </p>
<p> Also, warn if a negative integer constant expression is implicitly converted to an unsigned type. For example, warn about the assignment <tt>&quot;x = -1&quot;</tt> if <tt>&quot;x&quot;</tt> is unsigned. But do not warn about explicit casts like <tt>&quot;(unsigned) -1&quot;</tt>.</p>
<dt><code>-Wsign-compare</code></p>
<dd>Warn when a comparison between signed and unsigned values could produce an incorrect result when the signed value is converted to unsigned. This warning is also enabled by <code>-Wextra</code>; to get the other warnings of <code>-Wextra</code> without this warning, use <code>-Wextra -Wno-sign-compare</code>.</p>
<dt><code>-Waggregate-return</code></p>
<dd>Warn if any functions that return structures or unions are defined or called. (In languages where you can return an array, this also elicits a warning.)</p>
<dt><code>-Wno-attributes</code></p>
<dd>Do not warn if an unexpected <tt>&quot;__attribute__&quot;</tt> is used, such as unrecognized attributes, function attributes applied to variables, etc. This will not stop errors for incorrect use of supported attributes.</p>
<dt><code>-Wstrict-prototypes</code> (C only)</p>
<dd>Warn if a function is declared or defined without specifying the argument types. (An old-style function definition is permitted without a warning if preceded by a declaration which specifies the argument types.)</p>
<dt><code>-Wold-style-definition</code> (C only)</p>
<dd>Warn if an old-style function definition is used. A warning is given even if there is a previous prototype.</p>
<dt><code>-Wmissing-prototypes</code> (C only)</p>
<dd>Warn if a global function is defined without a previous prototype declaration. This warning is issued even if the definition itself provides a prototype. The aim is to detect global functions that fail to be declared in header files.</p>
<dt><code>-Wmissing-declarations</code> (C only)</p>
<dd>Warn if a global function is defined without a previous declaration. Do so even if the definition itself provides a prototype. Use this option to detect global functions that are not declared in header files.</p>
<dt><code>-Wmissing-field-initializers</code></p>
<dd>Warn if a structure&#8217;s initializer has some fields missing. For example, the following code would cause such a warning, because <tt>&quot;x.h&quot;</tt> is implicitly zero: </p>
<pre> struct s { int f, g, h; };
 struct s x = { 3, 4 };</pre>
<p>This option does not warn about designated initializers, so the following modification would not trigger a warning: </p>
<pre> struct s { int f, g, h; };
 struct s x = { .f = 3, .g = 4 };</pre>
<p>This warning is included in <code>-Wextra</code>. To get other <code>-Wextra</code> warnings without this one, use <code>-Wextra -Wno-missing-field-initializers</code>.</p>
<dt><code>-Wmissing-noreturn</code></p>
<dd>Warn about functions which might be candidates for attribute <tt>&quot;noreturn&quot;</tt>. Note these are only possible candidates, not absolute ones. Care should be taken to manually verify functions actually do not ever return before adding the <tt>&quot;noreturn&quot;</tt> attribute, otherwise subtle code generation bugs could be introduced. You will not get a warning for <tt>&quot;main&quot;</tt> in hosted C environments.</p>
<dt><code>-Wmissing-format-attribute</code></p>
<dd>Warn about function pointers which might be candidates for <tt>&quot;format&quot;</tt> attributes. Note these are only possible candidates, not absolute ones. <font SIZE="-1">GCC</font> will guess that function pointers with <tt>&quot;format&quot;</tt> attributes that are used in assignment, initialization, parameter passing or return statements should have a corresponding <tt>&quot;format&quot;</tt> attribute in the resulting type. I.e. the left-hand side of the assignment or initialization, the type of the parameter variable, or the return type of the containing function respectively should also have a <tt>&quot;format&quot;</tt> attribute to avoid the warning. </p>
<p> <font SIZE="-1">GCC</font> will also warn about function definitions which might be candidates for <tt>&quot;format&quot;</tt> attributes. Again, these are only possible candidates. <font SIZE="-1">GCC</font> will guess that <tt>&quot;format&quot;</tt> attributes might be appropriate for any function that calls a function like <tt>&quot;vprintf&quot;</tt> or <tt>&quot;vscanf&quot;</tt>, but this might not always be the case, and some functions for which <tt>&quot;format&quot;</tt> attributes are appropriate may not be detected.</p>
<dt><code>-Wno-multichar</code></p>
<dd>Do not warn if a multicharacter constant (<code>&#8216;</code><font SIZE="-1"><code>FOOF</code></font><code>&#8216;</code>) is used. Usually they indicate a typo in the user&#8217;s code, as they have implementation-defined values, and should not be used in portable code.</p>
<dt><code>-Wnormalized=&lt;none|id|nfc|nfkc&gt;</code></p>
<dd>In <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>, two identifiers are different if they are different sequences of characters. However, sometimes when characters outside the basic <font SIZE="-1">ASCII</font> character set are used, you can have two different character sequences that look the same. To avoid confusion, the <font SIZE="-1">ISO</font> 10646 standard sets out some <i>normalization rules</i> which when applied ensure that two sequences that look the same are turned into the same sequence. <font SIZE="-1">GCC</font> can warn you if you are using identifiers which have not been normalized; this option controls that warning. </p>
<p> There are four levels of warning that <font SIZE="-1">GCC</font> supports. The default is <code>-Wnormalized=nfc</code>, which warns about any identifier which is not in the <font SIZE="-1">ISO</font> 10646 &#8220;C&#8221; normalized form, <i></i><font SIZE="-1"><i>NFC</i></font><i></i>. <font SIZE="-1">NFC</font> is the recommended form for most uses. </p>
<p> Unfortunately, there are some characters which <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> allow in identifiers that when turned into <font SIZE="-1">NFC</font> aren&#8217;t allowable as identifiers. That is, there&#8217;s no way to use these symbols in portable <font SIZE="-1">ISO</font> C or C<font SIZE="-2">++</font> and have all your identifiers in <font SIZE="-1">NFC</font>. <code>-Wnormalized=id</code> suppresses the warning for these characters. It is hoped that future versions of the standards involved will correct this, which is why this option is not the default. </p>
<p> You can switch the warning off for all characters by writing <code>-Wnormalized=none</code>. You would only want to do this if you were using some other normalization scheme (like &#8220;D&#8221;), because otherwise you can easily create bugs that are literally impossible to see. </p>
<p> Some characters in <font SIZE="-1">ISO</font> 10646 have distinct meanings but look identical in some fonts or display methodologies, especially once formatting has been applied. For instance <tt>&quot;ⁿ&quot;</tt>, &#8220;<font SIZE="-1">SUPERSCRIPT</font> <font SIZE="-1">LATIN</font> <font SIZE="-1">SMALL</font> <font SIZE="-1">LETTER</font> N&#8221;, will display just like a regular <tt>&quot;n&quot;</tt> which has been placed in a superscript. <font SIZE="-1">ISO</font> 10646 defines the <i></i><font SIZE="-1"><i>NFKC</i></font><i></i> normalisation scheme to convert all these into a standard form as well, and <font SIZE="-1">GCC</font> will warn if your code is not in <font SIZE="-1">NFKC</font> if you use <code>-Wnormalized=nfkc</code>. This warning is comparable to warning about every identifier that contains the letter O because it might be confused with the digit 0, and so is not the default, but may be useful as a local coding convention if the programming environment is unable to be fixed to display these characters distinctly.</p>
<dt><code>-Wno-deprecated-declarations</code></p>
<dd>Do not warn about uses of functions, variables, and types marked as deprecated by using the <tt>&quot;deprecated&quot;</tt> attribute. (@pxref{Function Attributes}, <tt>@pxref</tt>{Variable Attributes}, <tt>@pxref</tt>{Type Attributes}.)</p>
<dt><code>-Wpacked</code></p>
<dd>Warn if a structure is given the packed attribute, but the packed attribute has no effect on the layout or size of the structure. Such structures may be mis-aligned for little benefit. For instance, in this code, the variable <tt>&quot;f.x&quot;</tt> in <tt>&quot;struct bar&quot;</tt> will be misaligned even though <tt>&quot;struct bar&quot;</tt> does not itself have the packed attribute: </p>
<pre> struct foo {
 int x;
 char a, b, c, d;
 } __attribute__((packed));
 struct bar {
 char z;
 struct foo f;
 };</pre>
<dt><code>-Wpadded</code></p>
<dd>Warn if padding is included in a structure, either to align an element of the structure or to align the whole structure. Sometimes when this happens it is possible to rearrange the fields of the structure to reduce the padding and so make the structure smaller.</p>
<dt><code>-Wredundant-decls</code></p>
<dd>Warn if anything is declared more than once in the same scope, even in cases where multiple declaration is valid and changes nothing.</p>
<dt><code>-Wnested-externs</code> (C only)</p>
<dd>Warn if an <tt>&quot;extern&quot;</tt> declaration is encountered within a function.</p>
<dt><code>-Wunreachable-code</code></p>
<dd>Warn if the compiler detects that code will never be executed. </p>
<p> This option is intended to warn when the compiler detects that at least a whole line of source code will never be executed, because some condition is never satisfied or because it is after a procedure that never returns. </p>
<p> It is possible for this option to produce a warning even though there are circumstances under which part of the affected line can be executed, so care should be taken when removing apparently-unreachable code. </p>
<p> For instance, when a function is inlined, a warning may mean that the line is unreachable in only one inlined copy of the function. </p>
<p> This option is not made part of <code>-Wall</code> because in a debugging version of a program there is often substantial code which checks correct functioning of the program and is, hopefully, unreachable because the program does work. Another common use of unreachable code is to provide behavior which is selectable at compile-time.</p>
<dt><code>-Winline</code></p>
<dd>Warn if a function can not be inlined and it was declared as inline. Even with this option, the compiler will not warn about failures to inline functions declared in system headers. </p>
<p> The compiler uses a variety of heuristics to determine whether or not to inline a function. For example, the compiler takes into account the size of the function being inlined and the amount of inlining that has already been done in the current function. Therefore, seemingly insignificant changes in the source program can cause the warnings produced by <code>-Winline</code> to appear or disappear.</p>
<dt><code>-Wno-invalid-offsetof</code> (C<font SIZE="-2">++</font> only)</p>
<dd>Suppress warnings from applying the <code>offsetof</code> macro to a non-POD type. According to the 1998 <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> standard, applying <code>offsetof</code> to a non-POD type is undefined. In existing C<font SIZE="-2">++</font> implementations, however, <code>offsetof</code> typically gives meaningful results even when applied to certain kinds of non-POD types. (Such as a simple <code>struct</code> that fails to be a <font SIZE="-1">POD</font> type only by virtue of having a constructor.) This flag is for users who are aware that they are writing nonportable code and who have deliberately chosen to ignore the warning about it. </p>
<p> The restrictions on <code>offsetof</code> may be relaxed in a future version of the C<font SIZE="-2">++</font> standard.</p>
<dt><code>-Wno-int-to-pointer-cast</code> (C only)</p>
<dd>Suppress warnings from casts to pointer type of an integer of a different size.</p>
<dt><code>-Wno-pointer-to-int-cast</code> (C only)</p>
<dd>Suppress warnings from casts from a pointer to an integer type of a different size.</p>
<dt><code>-Winvalid-pch</code></p>
<dd>Warn if a precompiled header is found in the search path but can&#8217;t be used.</p>
<dt><code>-Wlong-long</code></p>
<dd>Warn if <code>long long</code> type is used. This is default. To inhibit the warning messages, use <code>-Wno-long-long</code>. Flags <code>-Wlong-long</code> and <code>-Wno-long-long</code> are taken into account only when <code>-pedantic</code> flag is used.</p>
<dt><code>-Wvariadic-macros</code></p>
<dd>Warn if variadic macros are used in pedantic <font SIZE="-1">ISO</font> C90 mode, or the <font SIZE="-1">GNU</font> alternate syntax when in pedantic <font SIZE="-1">ISO</font> C99 mode. This is default. To inhibit the warning messages, use <code>-Wno-variadic-macros</code>.</p>
<dt><code>-Wvolatile-register-var</code></p>
<dd>Warn if a register variable is declared volatile. The volatile modifier does not inhibit all optimizations that may eliminate reads and/or writes to register variables.</p>
<dt><code>-Wdisabled-optimization</code></p>
<dd>Warn if a requested optimization pass is disabled. This warning does not generally indicate that there is anything wrong with your code; it merely indicates that <font SIZE="-1">GCC</font>&#8216;s optimizers were unable to handle the code effectively. Often, the problem is that your code is too big or too complex; <font SIZE="-1">GCC</font> will refuse to optimize programs when the optimization itself is likely to take inordinate amounts of time.</p>
<dt><code>-Wpointer-sign</code></p>
<dd>Warn for pointer argument passing or assignment with different signedness. This option is only supported for C and Objective-C. It is implied by <code>-Wall</code> and by <code>-pedantic</code>, which can be disabled with <code>-Wno-pointer-sign</code>.</p>
<dt><code>-Werror</code></p>
<dd>Make all warnings into errors.</p>
<dt><code>-Wstack-protector</code></p>
<dd>This option is only active when <code>-fstack-protector</code> is active. It warns about functions that will not be protected against stack smashing.</dl>
<h2>Options for Debugging Your Program or <font SIZE="-1">GCC</font></h2>
<p><font SIZE="-1">GCC</font> has various special options that are used for debugging either your program or <font SIZE="-1">GCC:</font></p>
<dl>
<dt><code>-g</code></p>
<dd>Produce debugging information in the operating system&#8217;s native format (stabs, <font SIZE="-1">COFF</font>, <font SIZE="-1">XCOFF</font>, or <font SIZE="-1">DWARF</font> 2). <font SIZE="-1">GDB</font> can work with this debugging information. </p>
<p> On most systems that use stabs format, <code>-g</code> enables use of extra debugging information that only <font SIZE="-1">GDB</font> can use; this extra information makes debugging work better in <font SIZE="-1">GDB</font> but will probably make other debuggers crash or refuse to read the program. If you want to control for certain whether to generate the extra information, use <code>-gstabs+</code>, <code>-gstabs</code>, <code>-gxcoff+</code>, <code>-gxcoff</code>, or <code>-gvms</code> (see below). </p>
<p> <font SIZE="-1">GCC</font> allows you to use <code>-g</code> with <code>-O</code>. The shortcuts taken by optimized code may occasionally produce surprising results: some variables you declared may not exist at all; flow of control may briefly move where you did not expect it; some statements may not be executed because they compute constant results or their values were already at hand; some statements may execute in different places because they were moved out of loops. </p>
<p> Nevertheless it proves possible to debug optimized output. This makes it reasonable to use the optimizer for programs that might have bugs. </p>
<p> The following options are useful when <font SIZE="-1">GCC</font> is generated with the capability for more than one debugging format.</p>
<dt><code>-ggdb</code></p>
<dd>Produce debugging information for use by <font SIZE="-1">GDB</font>. This means to use the most expressive format available (<font SIZE="-1">DWARF</font> 2, stabs, or the native format if neither of those are supported), including <font SIZE="-1">GDB</font> extensions if at all possible.</p>
<dt><code>-gstabs</code></p>
<dd>Produce debugging information in stabs format (if that is supported), without <font SIZE="-1">GDB</font> extensions. This is the format used by <font SIZE="-1">DBX</font> on most <font SIZE="-1">BSD</font> systems. On <font SIZE="-1">MIPS</font>, Alpha and System V Release 4 systems this option produces stabs debugging output which is not understood by <font SIZE="-1">DBX</font> or <font SIZE="-1">SDB</font>. On System V Release 4 systems this option requires the <font SIZE="-1">GNU</font> assembler.</p>
<dt><code>-feliminate-unused-debug-symbols</code></p>
<dd>Produce debugging information in stabs format (if that is supported), for only symbols that are actually used.</p>
<dt><code>-gstabs+</code></p>
<dd>Produce debugging information in stabs format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program.</p>
<dt><code>-gcoff</code></p>
<dd>Produce debugging information in <font SIZE="-1">COFF</font> format (if that is supported). This is the format used by <font SIZE="-1">SDB</font> on most System V systems prior to System V Release 4.</p>
<dt><code>-gxcoff</code></p>
<dd>Produce debugging information in <font SIZE="-1">XCOFF</font> format (if that is supported). This is the format used by the <font SIZE="-1">DBX</font> debugger on <font SIZE="-1">IBM</font> <font SIZE="-1">RS/6000</font> systems.</p>
<dt><code>-gxcoff+</code></p>
<dd>Produce debugging information in <font SIZE="-1">XCOFF</font> format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program, and may cause assemblers other than the <font SIZE="-1">GNU</font> assembler (<font SIZE="-1">GAS</font>) to fail with an error.</p>
<dt><code>-gdwarf-2</code></p>
<dd>Produce debugging information in <font SIZE="-1">DWARF</font> version 2 format (if that is supported). This is the format used by <font SIZE="-1">DBX</font> on <font SIZE="-1">IRIX</font> 6. With this option, <font SIZE="-1">GCC</font> uses features of <font SIZE="-1">DWARF</font> version 3 when they are useful; version 3 is upward compatible with version 2, but may still cause problems for older debuggers.</p>
<dt><code>-gvms</code></p>
<dd>Produce debugging information in <font SIZE="-1">VMS</font> debug format (if that is supported). This is the format used by <font SIZE="-1">DEBUG</font> on <font SIZE="-1">VMS</font> systems.</p>
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
<p> Level 1 produces minimal information, enough for making backtraces in parts of the program that you don&#8217;t plan to debug. This includes descriptions of functions and external variables, but no information about local variables and no line numbers. </p>
<p> Level 3 includes extra information, such as all the macro definitions present in the program. Some debuggers support macro expansion when you use <code>-g3</code>. </p>
<p> <code>-gdwarf-2</code> does not accept a concatenated debug level, because <font SIZE="-1">GCC</font> used to support an option <code>-gdwarf</code> that meant to generate debug information in version 1 of the <font SIZE="-1">DWARF</font> format (which is very different from version 2), and it would have been too confusing. That debug format is long obsolete, but the option cannot be changed now. Instead use an additional <code>-g</code><i>level</i> option to change the debug level for <font SIZE="-1">DWARF2</font>.</p>
<dt><code>-feliminate-dwarf2-dups</code></p>
<dd>Compress <font SIZE="-1">DWARF2</font> debugging information by eliminating duplicated information about each symbol. This option only makes sense when generating <font SIZE="-1">DWARF2</font> debugging information with <code>-gdwarf-2</code>.</p>
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
<dt><code>-fprofile-arcs</code></p>
<dd>Add code so that program flow <i>arcs</i> are instrumented. During execution the program records how many times each branch and call is executed and how many times it is taken or returns. When the compiled program exits it saves this data to a file called <i>auxname.gcda</i> for each source file. The data may be used for profile-directed optimizations (<code>-fbranch-probabilities</code>), or for test coverage analysis (<code>-ftest-coverage</code>). Each object file&#8217;s <i>auxname</i> is generated from the name of the output file, if explicitly specified and it is not the final executable, otherwise it is the basename of the source file. In both cases any suffix is removed (e.g. <i>foo.gcda</i> for input file <i>dir/foo.c</i>, or <i>dir/foo.gcda</i> for output file specified as <code>-o dir/foo.o</code>).</p>
<dt><code>&#8211;coverage</code></p>
<dd>This option is used to compile and link code instrumented for coverage analysis. The option is a synonym for <code>-fprofile-arcs</code> <code>-ftest-coverage</code> (when compiling) and <code>-lgcov</code> (when linking). See the documentation for those options for more details.</p>
<dl>
<dd>
<dl>
<dt>@bullet</p>
<dd>Compile the source files with <code>-fprofile-arcs</code> plus optimization and code generation options. For test coverage analysis, use the additional <code>-ftest-coverage</code> option. You do not need to profile every source file in a program.</p>
<dt>@cvmmfu</p>
<dd>Link your object files with <code>-lgcov</code> or <code>-fprofile-arcs</code> (the latter implies the former).</p>
<dt>@dwnngv</p>
<dd>Run the program on a representative workload to generate the arc profile information. This may be repeated any number of times. You can run concurrent instances of your program, and provided that the file system supports locking, the data files will be correctly updated. Also <tt>&quot;fork&quot;</tt> calls are detected and correctly handled (double counting will not happen).</p>
<dt>@exoohw</p>
<dd>For profile-directed optimizations, compile the source files again with the same optimization and code generation options plus <code>-fbranch-probabilities</code>.</p>
<dt>@fyppix</p>
<dd>For test coverage analysis, use <code>gcov</code> to produce human readable information from the <i>.gcno</i> and <i>.gcda</i> files. Refer to the <code>gcov</code> documentation for further information.</dl>
</dl>
<dl>
<dd>With <code>-fprofile-arcs</code>, for each function of your program <font SIZE="-1">GCC</font> creates a program flow graph, then finds a spanning tree for the graph. Only arcs that are not on the spanning tree have to be instrumented: the compiler adds code to count the number of times that these arcs are executed. When an arc is the only exit or only entrance to a block, the instrumentation code can be added to the block; otherwise, a new basic block must be created to hold the instrumentation code.</dl>
<dt><code>-ftest-coverage</code></p>
<dd>Produce a notes file that the <code>gcov</code> code-coverage utility can use to show program coverage. Each source file&#8217;s note file is called <i>auxname.gcno</i>. Refer to the <code>-fprofile-arcs</code> option above for a description of <i>auxname</i> and instructions on how to generate test coverage data. Coverage data will match the source files more closely, if you do not optimize.</p>
<dt><code>-d</code><i>letters</i></p>
<dd>
<dt><code>-fdump-rtl-</code><i>pass</i></p>
<dd>Says to make debugging dumps during compilation at times specified by <i>letters</i>. This is used for debugging the RTL-based passes of the compiler. The file names for most of the dumps are made by appending a pass number and a word to the <i>dumpname</i>. <i>dumpname</i> is generated from the name of the output file, if explicitly specified and it is not an executable, otherwise it is the basename of the source file. </p>
<p> Most debug dumps can be enabled either passing a letter to the <code>-d</code> option, or with a long <code>-fdump-rtl</code> switch; here are the possible letters for use in <i>letters</i> and <i>pass</i>, and their meanings:</p>
<dl>
<dd>
<dl>
<dt><code>-dA</code></p>
<dd>Annotate the assembler output with miscellaneous debugging information.</p>
<dt><code>-db</code></p>
<dd>
<dt><code>-fdump-rtl-bp</code></p>
<dd>Dump after computing branch probabilities, to <i>file.09.bp</i>.</p>
<dt><code>-dB</code></p>
<dd>
<dt><code>-fdump-rtl-bbro</code></p>
<dd>Dump after block reordering, to <i>file.30.bbro</i>.</p>
<dt><code>-dc</code></p>
<dd>
<dt><code>-fdump-rtl-combine</code></p>
<dd>Dump after instruction combination, to the file <i>file.17.combine</i>.</p>
<dt><code>-dC</code></p>
<dd>
<dt><code>-fdump-rtl-ce1</code></p>
<dd>
<dt><code>-fdump-rtl-ce2</code></p>
<dd><code>-dC</code> and <code>-fdump-rtl-ce1</code> enable dumping after the first if conversion, to the file <i>file.11.ce1</i>. <code>-dC</code> and <code>-fdump-rtl-ce2</code> enable dumping after the second if conversion, to the file <i>file.18.ce2</i>.</p>
<dt><code>-dd</code></p>
<dd>
<dt><code>-fdump-rtl-btl</code></p>
<dd>
<dt><code>-fdump-rtl-dbr</code></p>
<dd><code>-dd</code> and <code>-fdump-rtl-btl</code> enable dumping after branch target load optimization, to <i>file.31.btl</i>. <code>-dd</code> and <code>-fdump-rtl-dbr</code> enable dumping after delayed branch scheduling, to <i>file.36.dbr</i>.</p>
<dt><code>-dD</code></p>
<dd>Dump all macro definitions, at the end of preprocessing, in addition to normal output.</p>
<dt><code>-dE</code></p>
<dd>
<dt><code>-fdump-rtl-ce3</code></p>
<dd>Dump after the third if conversion, to <i>file.28.ce3</i>.</p>
<dt><code>-df</code></p>
<dd>
<dt><code>-fdump-rtl-cfg</code></p>
<dd>
<dt><code>-fdump-rtl-life</code></p>
<dd><code>-df</code> and <code>-fdump-rtl-cfg</code> enable dumping after control and data flow analysis, to <i>file.08.cfg</i>. <code>-df</code> and <code>-fdump-rtl-cfg</code> enable dumping dump after life analysis, to <i>file.16.life</i>.</p>
<dt><code>-dg</code></p>
<dd>
<dt><code>-fdump-rtl-greg</code></p>
<dd>Dump after global register allocation, to <i>file.23.greg</i>.</p>
<dt><code>-dG</code></p>
<dd>
<dt><code>-fdump-rtl-gcse</code></p>
<dd>
<dt><code>-fdump-rtl-bypass</code></p>
<dd><code>-dG</code> and <code>-fdump-rtl-gcse</code> enable dumping after <font SIZE="-1">GCSE</font>, to <i>file.05.gcse</i>. <code>-dG</code> and <code>-fdump-rtl-bypass</code> enable dumping after jump bypassing and control flow optimizations, to <i>file.07.bypass</i>.</p>
<dt><code>-dh</code></p>
<dd>
<dt><code>-fdump-rtl-eh</code></p>
<dd>Dump after finalization of <font SIZE="-1">EH</font> handling code, to <i>file.02.eh</i>.</p>
<dt><code>-di</code></p>
<dd>
<dt><code>-fdump-rtl-sibling</code></p>
<dd>Dump after sibling call optimizations, to <i>file.01.sibling</i>.</p>
<dt><code>-dj</code></p>
<dd>
<dt><code>-fdump-rtl-jump</code></p>
<dd>Dump after the first jump optimization, to <i>file.03.jump</i>.</p>
<dt><code>-dk</code></p>
<dd>
<dt><code>-fdump-rtl-stack</code></p>
<dd>Dump after conversion from registers to stack, to <i>file.33.stack</i>.</p>
<dt><code>-dl</code></p>
<dd>
<dt><code>-fdump-rtl-lreg</code></p>
<dd>Dump after local register allocation, to <i>file.22.lreg</i>.</p>
<dt><code>-dL</code></p>
<dd>
<dt><code>-fdump-rtl-loop</code></p>
<dd>
<dt><code>-fdump-rtl-loop2</code></p>
<dd><code>-dL</code> and <code>-fdump-rtl-loop</code> enable dumping after the first loop optimization pass, to <i>file.06.loop</i>. <code>-dL</code> and <code>-fdump-rtl-loop2</code> enable dumping after the second pass, to <i>file.13.loop2</i>.</p>
<dt><code>-dm</code></p>
<dd>
<dt><code>-fdump-rtl-sms</code></p>
<dd>Dump after modulo scheduling, to <i>file.20.sms</i>.</p>
<dt><code>-dM</code></p>
<dd>
<dt><code>-fdump-rtl-mach</code></p>
<dd>Dump after performing the machine dependent reorganization pass, to <i>file.35.mach</i>.</p>
<dt><code>-dn</code></p>
<dd>
<dt><code>-fdump-rtl-rnreg</code></p>
<dd>Dump after register renumbering, to <i>file.29.rnreg</i>.</p>
<dt><code>-dN</code></p>
<dd>
<dt><code>-fdump-rtl-regmove</code></p>
<dd>Dump after the register move pass, to <i>file.19.regmove</i>.</p>
<dt><code>-do</code></p>
<dd>
<dt><code>-fdump-rtl-postreload</code></p>
<dd>Dump after post-reload optimizations, to <i>file.24.postreload</i>.</p>
<dt><code>-dr</code></p>
<dd>
<dt><code>-fdump-rtl-expand</code></p>
<dd>Dump after <font SIZE="-1">RTL</font> generation, to <i>file.00.expand</i>.</p>
<dt><code>-dR</code></p>
<dd>
<dt><code>-fdump-rtl-sched2</code></p>
<dd>Dump after the second scheduling pass, to <i>file.32.sched2</i>.</p>
<dt><code>-ds</code></p>
<dd>
<dt><code>-fdump-rtl-cse</code></p>
<dd>Dump after <font SIZE="-1">CSE</font> (including the jump optimization that sometimes follows <font SIZE="-1">CSE</font>), to <i>file.04.cse</i>.</p>
<dt><code>-dS</code></p>
<dd>
<dt><code>-fdump-rtl-sched</code></p>
<dd>Dump after the first scheduling pass, to <i>file.21.sched</i>.</p>
<dt><code>-dt</code></p>
<dd>
<dt><code>-fdump-rtl-cse2</code></p>
<dd>Dump after the second <font SIZE="-1">CSE</font> pass (including the jump optimization that sometimes follows <font SIZE="-1">CSE</font>), to <i>file.15.cse2</i>.</p>
<dt><code>-dT</code></p>
<dd>
<dt><code>-fdump-rtl-tracer</code></p>
<dd>Dump after running tracer, to <i>file.12.tracer</i>.</p>
<dt><code>-dV</code></p>
<dd>
<dt><code>-fdump-rtl-vpt</code></p>
<dd>
<dt><code>-fdump-rtl-vartrack</code></p>
<dd><code>-dV</code> and <code>-fdump-rtl-vpt</code> enable dumping after the value profile transformations, to <i>file.10.vpt</i>. <code>-dV</code> and <code>-fdump-rtl-vartrack</code> enable dumping after variable tracking, to <i>file.34.vartrack</i>.</p>
<dt><code>-dw</code></p>
<dd>
<dt><code>-fdump-rtl-flow2</code></p>
<dd>Dump after the second flow pass, to <i>file.26.flow2</i>.</p>
<dt><code>-dz</code></p>
<dd>
<dt><code>-fdump-rtl-peephole2</code></p>
<dd>Dump after the peephole pass, to <i>file.27.peephole2</i>.</p>
<dt><code>-dZ</code></p>
<dd>
<dt><code>-fdump-rtl-web</code></p>
<dd>Dump after live range splitting, to <i>file.14.web</i>.</p>
<dt><code>-da</code></p>
<dd>
<dt><code>-fdump-rtl-all</code></p>
<dd>Produce all the dumps listed above.</p>
<dt><code>-dH</code></p>
<dd>Produce a core dump whenever an error occurs.</p>
<dt><code>-dm</code></p>
<dd>Print statistics on memory usage, at the end of the run, to standard error.</p>
<dt><code>-dp</code></p>
<dd>Annotate the assembler output with a comment indicating which pattern and alternative was used. The length of each instruction is also printed.</p>
<dt><code>-dP</code></p>
<dd>Dump the <font SIZE="-1">RTL</font> in the assembler output as a comment before each instruction. Also turns on <code>-dp</code> annotation.</p>
<dt><code>-dv</code></p>
<dd>For each of the other indicated dump files (either with <code>-d</code> or <code>-fdump-rtl-</code><i>pass</i>), dump a representation of the control flow graph suitable for viewing with <font SIZE="-1">VCG</font> to <i>file.pass.vcg</i>.</p>
<dt><code>-dx</code></p>
<dd>Just generate <font SIZE="-1">RTL</font> for a function instead of compiling it. Usually used with <code>r</code> (<code>-fdump-rtl-expand</code>).</p>
<dt><code>-dy</code></p>
<dd>Dump debugging information during parsing, to standard error.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-fdump-unnumbered</code></p>
<dd>When doing debugging dumps (see <code>-d</code> option above), suppress instruction numbers and line number note output. This makes it more feasible to use diff on debugging dumps for compiler invocations with different options, in particular with and without <code>-g</code>.</p>
<dt><code>-fdump-translation-unit</code> (C<font SIZE="-2">++</font> only)</p>
<dd>
<dt><code>-fdump-translation-unit-</code><i>options</i>(C<font SIZE="-2">++</font> only)</p>
<dd>Dump a representation of the tree structure for the entire translation unit to a file. The file name is made by appending <i>.tu</i> to the source file name. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> controls the details of the dump as described for the <code>-fdump-tree</code> options.</p>
<dt><code>-fdump-class-hierarchy</code> (C<font SIZE="-2">++</font> only)</p>
<dd>
<dt><code>-fdump-class-hierarchy-</code><i>options</i>(C<font SIZE="-2">++</font> only)</p>
<dd>Dump a representation of each class&#8217;s hierarchy and virtual function table layout to a file. The file name is made by appending <i>.class</i> to the source file name. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> controls the details of the dump as described for the <code>-fdump-tree</code> options.</p>
<dt><code>-fdump-ipa-</code><i>switch</i></p>
<dd>Control the dumping at various stages of inter-procedural analysis language tree to a file. The file name is generated by appending a switch specific suffix to the source file name. The following dumps are possible:</p>
<dl>
<dd>
<dl>
<dt><code>all</code></p>
<dd>Enables all inter-procedural analysis dumps; currently the only produced dump is the <code>cgraph</code> dump.</p>
<dt><code>cgraph</code></p>
<dd>Dumps information about call-graph optimization, unused function removal, and inlining decisions.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-fdump-tree-</code><i>switch</i></p>
<dd>
<dt><code>-fdump-tree-</code><i>switch</i><code>&#8211;</code><i>options</i></p>
<dd>Control the dumping at various stages of processing the intermediate language tree to a file. The file name is generated by appending a switch specific suffix to the source file name. If the <code>&#8211;</code><i>options</i> form is used, <i>options</i> is a list of <code>&#8211;</code> separated options that control the details of the dump. Not all options are applicable to all dumps, those which are not meaningful will be ignored. The following options are available</p>
<dl>
<dd>
<dl>
<dt><code>address</code></p>
<dd>Print the address of each node. Usually this is not meaningful as it changes according to the environment and source file. Its primary use is for tying up a dump file with a debug environment.</p>
<dt><code>slim</code></p>
<dd>Inhibit dumping of members of a scope or body of a function merely because that scope has been reached. Only dump such items when they are directly reachable by some other path. When dumping pretty-printed trees, this option inhibits dumping the bodies of control structures.</p>
<dt><code>raw</code></p>
<dd>Print a raw representation of the tree. By default, trees are pretty-printed into a C-like representation.</p>
<dt><code>details</code></p>
<dd>Enable more detailed dumps (not honored by every dump option).</p>
<dt><code>stats</code></p>
<dd>Enable dumping various statistics about the pass (not honored by every dump option).</p>
<dt><code>blocks</code></p>
<dd>Enable showing basic block boundaries (disabled in raw dumps).</p>
<dt><code>vops</code></p>
<dd>Enable showing virtual operands for every statement.</p>
<dt><code>lineno</code></p>
<dd>Enable showing line numbers for statements.</p>
<dt><code>uid</code></p>
<dd>Enable showing the unique <font SIZE="-1">ID</font> (<tt>&quot;DECL_UID&quot;</tt>) for each variable.</p>
<dt><code>all</code></p>
<dd>Turn on all options, except <code>raw</code>, <code>slim</code> and <code>lineno</code>.</dl>
</dl>
<dl>
<dd>The following tree dumps are possible:</p>
<dl>
<dt><code>original</code></p>
<dd>Dump before any tree based optimization, to <i>file.original</i>.</p>
<dt><code>optimized</code></p>
<dd>Dump after all tree based optimization, to <i>file.optimized</i>.</p>
<dt><code>inlined</code></p>
<dd>Dump after function inlining, to <i>file.inlined</i>.</p>
<dt><code>gimple</code></p>
<dd>Dump each function before and after the gimplification pass to a file. The file name is made by appending <i>.gimple</i> to the source file name.</p>
<dt><code>cfg</code></p>
<dd>Dump the control flow graph of each function to a file. The file name is made by appending <i>.cfg</i> to the source file name.</p>
<dt><code>vcg</code></p>
<dd>Dump the control flow graph of each function to a file in <font SIZE="-1">VCG</font> format. The file name is made by appending <i>.vcg</i> to the source file name. Note that if the file contains more than one function, the generated file cannot be used directly by <font SIZE="-1">VCG</font>. You will need to cut and paste each function&#8217;s graph into its own separate file first.</p>
<dt><code>ch</code></p>
<dd>Dump each function after copying loop headers. The file name is made by appending <i>.ch</i> to the source file name.</p>
<dt><code>ssa</code></p>
<dd>Dump <font SIZE="-1">SSA</font> related information to a file. The file name is made by appending <i>.ssa</i> to the source file name.</p>
<dt><code>salias</code></p>
<dd>Dump structure aliasing variable information to a file. This file name is made by appending <i>.salias</i> to the source file name.</p>
<dt><code>alias</code></p>
<dd>Dump aliasing information for each function. The file name is made by appending <i>.alias</i> to the source file name.</p>
<dt><code>ccp</code></p>
<dd>Dump each function after <font SIZE="-1">CCP</font>. The file name is made by appending <i>.ccp</i> to the source file name.</p>
<dt><code>storeccp</code></p>
<dd>Dump each function after <font SIZE="-1">STORE-CCP</font>. The file name is made by appending <i>.storeccp</i> to the source file name.</p>
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
<dt><code>mudflap</code></p>
<dd>Dump each function after adding mudflap instrumentation. The file name is made by appending <i>.mudflap</i> to the source file name.</p>
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
<dt><code>vrp</code></p>
<dd>Dump each function after Value Range Propagation (<font SIZE="-1">VRP</font>). The file name is made by appending <i>.vrp</i> to the source file name.</p>
<dt><code>all</code></p>
<dd>Enable all the available tree dumps with the flags provided in this option.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-ftree-vectorizer-verbose=</code><i>n</i></p>
<dd>This option controls the amount of debugging output the vectorizer prints. This information is written to standard error, unless <code>-fdump-tree-all</code> or <code>-fdump-tree-vect</code> is specified, in which case it is output to the usual dump listing file, <i>.vect</i>.</p>
<dt><code>-frandom-seed=</code><i>string</i></p>
<dd>This option provides a seed that <font SIZE="-1">GCC</font> uses when it would otherwise use random numbers. It is used to generate certain symbol names that have to be different in every compiled file. It is also used to place unique stamps in coverage data files and the object files that produce them. You can use the <code>-frandom-seed</code> option to produce reproducibly identical object files. </p>
<p> The <i>string</i> should be different for every file you compile.</p>
<dt><code>-fsched-verbose=</code><i>n</i></p>
<dd>On targets that use instruction scheduling, this option controls the amount of debugging output the scheduler prints. This information is written to standard error, unless <code>-dS</code> or <code>-dR</code> is specified, in which case it is output to the usual dump listing file, <i>.sched</i> or <i>.sched2</i> respectively. However for <i>n</i> greater than nine, the output is always printed to standard error. </p>
<p> For <i>n</i> greater than zero, <code>-fsched-verbose</code> outputs the same information as <code>-dRS</code>. For <i>n</i> greater than one, it also output basic block probabilities, detailed ready list information and unit/insn info. For <i>n</i> greater than two, it includes <font SIZE="-1">RTL</font> at abort point, control-flow and regions info. And for <i>n</i> over four, <code>-fsched-verbose</code> also includes dependence info.</p>
<dt><code>-save-temps</code></p>
<dd>Store the usual &#8220;temporary&#8221; intermediate files permanently; place them in the current directory and name them based on the source file. Thus, compiling <i>foo.c</i> with <code>-c -save-temps</code> would produce files <i>foo.i</i> and <i>foo.s</i>, as well as <i>foo.o</i>. This creates a preprocessed <i>foo.i</i> output file even though the compiler now normally uses an integrated preprocessor. </p>
<p> When used in combination with the <code>-x</code> command line option, <code>-save-temps</code> is sensible enough to avoid over writing an input source file with the same extension as an intermediate file. The corresponding intermediate file may be obtained by renaming the source file before using <code>-save-temps</code>.</p>
<dt><code>-time</code></p>
<dd>Report the <font SIZE="-1">CPU</font> time taken by each subprocess in the compilation sequence. For C source files, this is the compiler proper and assembler (plus the linker if linking is done). The output looks like this: </p>
<pre> # cc1 0.12 0.01
 # as 0.00 0.01</pre>
<p>The first number on each line is the &#8220;user time&#8221;, that is time spent executing the program itself. The second number is &#8220;system time&#8221;, time spent executing operating system routines on behalf of the program. Both numbers are in seconds.</p>
<dt><code>-fvar-tracking</code></p>
<dd>Run variable tracking pass. It computes where variables are stored at each position in code. Better debugging information is then generated (if the debugging information format supports this information). </p>
<p> It is enabled by default when compiling with optimization (<code>-Os</code>, <code>-O</code>, <code>-O2</code>, &#8230;), debugging information (<code>-g</code>) and the debug info format supports it.</p>
<dt><code>-print-file-name=</code><i>library</i></p>
<dd>Print the full absolute name of the library file <i>library</i> that would be used when linking&#8212;and don&#8217;t do anything else. With this option, <font SIZE="-1">GCC</font> does not compile or link anything; it just prints the file name.</p>
<dt><code>-print-multi-directory</code></p>
<dd>Print the directory name corresponding to the multilib selected by any other switches present in the command line. This directory is supposed to exist in <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>.</p>
<dt><code>-print-multi-lib</code></p>
<dd>Print the mapping from multilib directory names to compiler switches that enable them. The directory name is separated from the switches by <code>;</code>, and each switch starts with an <code>@} instead of the </code>@samp<code>{-</code>, without spaces between multiple switches. This is supposed to ease shell-processing.</p>
<dt><code>-print-prog-name=</code><i>program</i></p>
<dd>Like <code>-print-file-name</code>, but searches for a program such as <code>cpp</code>.</p>
<dt><code>-print-libgcc-file-name</code></p>
<dd>Same as <code>-print-file-name=libgcc.a</code>. </p>
<p> This is useful when you use <code>-nostdlib</code> or <code>-nodefaultlibs</code> but you do want to link with <i>libgcc.a</i>. You can do </p>
<pre> gcc -nostdlib &lt;files&gt;... `gcc -print-libgcc-file-name`</pre>
<dt><code>-print-search-dirs</code></p>
<dd>Print the name of the configured installation directory and a list of program and library directories <code>gcc</code> will search&#8212;and don&#8217;t do anything else. </p>
<p> This is useful when <code>gcc</code> prints the error message <code>installation problem, cannot exec cpp0: No such file or directory</code>. To resolve this you either need to put <i>cpp0</i> and the other compiler components where <code>gcc</code> expects to find them, or you can set the environment variable <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> to the directory where you installed them. Don&#8217;t forget the trailing <code>/</code>.</p>
<dt><code>-dumpmachine</code></p>
<dd>Print the compiler&#8217;s target machine (for example, <code>i686-pc-linux-gnu</code>)&#8212;and don&#8217;t do anything else.</p>
<dt><code>-dumpversion</code></p>
<dd>Print the compiler version (for example, <code>3.0</code>)&#8212;and don&#8217;t do anything else.</p>
<dt><code>-dumpspecs</code></p>
<dd>Print the compiler&#8217;s built-in specs&#8212;and don&#8217;t do anything else. (This is used when <font SIZE="-1">GCC</font> itself is being built.)</p>
<dt><code>-feliminate-unused-debug-types</code></p>
<dd>Normally, when producing <font SIZE="-1">DWARF2</font> output, <font SIZE="-1">GCC</font> will emit debugging information for all types declared in a compilation unit, regardless of whether or not they are actually used in that compilation unit. Sometimes this is useful, such as if, in the debugger, you want to cast a value to a type that is not actually used in your program (but is declared). More often, however, this results in a significant amount of wasted space. With this option, <font SIZE="-1">GCC</font> will avoid producing debug symbol output for types that are nowhere used in the source file being compiled.</dl>
<h2>Options That Control Optimization</h2>
<p>These options control various sorts of optimizations. </p>
<p> Without any optimization option, the compiler&#8217;s goal is to reduce the cost of compilation and to make debugging produce the expected results. Statements are independent: if you stop the program with a breakpoint between statements, you can then assign a new value to any variable or change the program counter to any other statement in the function and get exactly the results you would expect from the source code. </p>
<p> Turning on optimization flags makes the compiler attempt to improve the performance and/or code size at the expense of compilation time and possibly the ability to debug the program. </p>
<p> The compiler performs optimization based on the knowledge it has of the program. Optimization levels <code>-O</code> and above, in particular, enable <i>unit-at-a-time</i> mode, which allows the compiler to consider information gained from later functions in the file when compiling a function. Compiling multiple files at once to a single output file in <i>unit-at-a-time</i> mode allows the compiler to use information gained from all of the files when compiling each of them. </p>
<p> Not all optimizations are controlled directly by a flag. Only optimizations that have a flag are listed.</p>
<dl>
<dt><code>-O</code></p>
<dd>
<dt><code>-O1</code></p>
<dd>Optimize. Optimizing compilation takes somewhat more time, and a lot more memory for a large function. </p>
<p> With <code>-O</code>, the compiler tries to reduce code size and execution time, without performing any optimizations that take a great deal of compilation time. </p>
<p> <code>-O</code> turns on the following optimization flags: <code>-fdefer-pop -fdelayed-branch -fguess-branch-probability -fcprop-registers -floop-optimize -fif-conversion -fif-conversion2 -ftree-ccp -ftree-dce -ftree-dominator-opts -ftree-dse -ftree-ter -ftree-lrs -ftree-sra -ftree-copyrename -ftree-fre -ftree-ch -funit-at-a-time -fmerge-constants</code> </p>
<p> <code>-O</code> also turns on <code>-fomit-frame-pointer</code> on machines where doing so does not interfere with debugging. </p>
<p> <code>-O</code> doesn&#8217;t turn on <code>-ftree-sra</code> for the Ada compiler. This option must be explicitly specified on the command line to be enabled for the Ada compiler.</p>
<dt><code>-O2</code></p>
<dd>Optimize even more. <font SIZE="-1">GCC</font> performs nearly all supported optimizations that do not involve a space-speed tradeoff. The compiler does not perform loop unrolling or function inlining when you specify <code>-O2</code>. As compared to <code>-O</code>, this option increases both compilation time and the performance of the generated code. </p>
<p> <code>-O2</code> turns on all optimization flags specified by <code>-O</code>. It also turns on the following optimization flags: <code>-fthread-jumps -fcrossjumping -foptimize-sibling-calls -fcse-follow-jumps -fcse-skip-blocks -fgcse -fgcse-lm -fexpensive-optimizations -fstrength-reduce -frerun-cse-after-loop -frerun-loop-opt -fcaller-saves -fpeephole2 -fschedule-insns -fschedule-insns2 -fsched-interblock -fsched-spec -fregmove -fstrict-aliasing -fdelete-null-pointer-checks -freorder-blocks -freorder-functions -falign-functions -falign-jumps -falign-loops -falign-labels -ftree-vrp -ftree-pre</code> </p>
<p> Please note the warning under <code>-fgcse</code> about invoking <code>-O2</code> on programs that use computed gotos.</p>
<dt><code>-O3</code></p>
<dd>Optimize yet more. <code>-O3</code> turns on all optimizations specified by <code>-O2</code> and also turns on the <code>-finline-functions</code>, <code>-funswitch-loops</code> and <code>-fgcse-after-reload</code> options.</p>
<dt><code>-O0</code></p>
<dd>Do not optimize. This is the default.</p>
<dt><code>-Os</code></p>
<dd>Optimize for size. <code>-Os</code> enables all <code>-O2</code> optimizations that do not typically increase code size. It also performs further optimizations designed to reduce code size. </p>
<p> <code>-Os</code> disables the following optimization flags: <code>-falign-functions -falign-jumps -falign-loops -falign-labels -freorder-blocks -freorder-blocks-and-partition -fprefetch-loop-arrays -ftree-vect-loop-version</code> </p>
<p> If you use multiple <code>-O</code> options, with or without level numbers, the last such option is the one that is effective.</dl>
<p> Options of the form <code>-f</code><i>flag</i> specify machine-independent flags. Most flags have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. In the table below, only one of the forms is listed&#8212;the one you typically will use. You can figure out the other form by either removing <code>no-</code> or adding it. </p>
<p> The following options control specific optimizations. They are either activated by <code>-O</code> options or are related to ones that are. You can use the following flags in the rare cases when &#8220;fine-tuning&#8221; of optimizations to be performed is desired.</p>
<dl>
<dt><code>-fno-default-inline</code></p>
<dd>Do not make member functions inline by default merely because they are defined inside the class scope (C<font SIZE="-2">++</font> only). Otherwise, when you specify <code>-O</code>, member functions defined inside class scope are compiled inline by default; i.e., you don&#8217;t need to add <code>inline</code> in front of the member function name.</p>
<dt><code>-fno-defer-pop</code></p>
<dd>Always pop the arguments to each function call as soon as that function returns. For machines which must pop arguments after a function call, the compiler normally lets arguments accumulate on the stack for several function calls and pops them all at once. </p>
<p> Disabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fforce-mem</code></p>
<dd>Force memory operands to be copied into registers before doing arithmetic on them. This produces better code by making all memory references potential common subexpressions. When they are not common subexpressions, instruction combination should eliminate the separate register-load. This option is now a nop and will be removed in 4.2.</p>
<dt><code>-fforce-addr</code></p>
<dd>Force memory address constants to be copied into registers before doing arithmetic on them.</p>
<dt><code>-fomit-frame-pointer</code></p>
<dd>Don&#8217;t keep the frame pointer in a register for functions that don&#8217;t need one. This avoids the instructions to save, set up and restore frame pointers; it also makes an extra register available in many functions. <code>It also makes debugging impossible on some machines.</code> </p>
<p> On some machines, such as the <font SIZE="-1">VAX</font>, this flag has no effect, because the standard calling sequence automatically handles the frame pointer and nothing is saved by pretending it doesn&#8217;t exist. The machine-description macro <tt>&quot;FRAME_POINTER_REQUIRED&quot;</tt> controls whether a target machine supports this flag. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-foptimize-sibling-calls</code></p>
<dd>Optimize sibling and tail recursive calls. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-inline</code></p>
<dd>Don&#8217;t pay attention to the <tt>&quot;inline&quot;</tt> keyword. Normally this option is used to keep the compiler from expanding any functions inline. Note that if you are not optimizing, no functions can be expanded inline.</p>
<dt><code>-finline-functions</code></p>
<dd>Integrate all simple functions into their callers. The compiler heuristically decides which functions are simple enough to be worth integrating in this way. </p>
<p> If all calls to a given function are integrated, and the function is declared <tt>&quot;static&quot;</tt>, then the function is normally not output as assembler code in its own right. </p>
<p> Enabled at level <code>-O3</code>.</p>
<dt><code>-finline-functions-called-once</code></p>
<dd>Consider all <tt>&quot;static&quot;</tt> functions called once for inlining into their caller even if they are not marked <tt>&quot;inline&quot;</tt>. If a call to a given function is integrated, then the function is not output as assembler code in its own right. </p>
<p> Enabled if <code>-funit-at-a-time</code> is enabled.</p>
<dt><code>-fearly-inlining</code></p>
<dd>Inline functions marked by <tt>&quot;always_inline&quot;</tt> and functions whose body seems smaller than the function call overhead early before doing <code>-fprofile-generate</code> instrumentation and real inlining pass. Doing so makes profiling significantly cheaper and usually inlining faster on programs having large chains of nested wrapper functions. </p>
<p> Enabled by default.</p>
<dt><code>-finline-limit=</code><i>n</i></p>
<dd>By default, <font SIZE="-1">GCC</font> limits the size of functions that can be inlined. This flag allows the control of this limit for functions that are explicitly marked as inline (i.e., marked with the inline keyword or defined within the class definition in c++). <i>n</i> is the size of functions that can be inlined in number of pseudo instructions (not counting parameter handling). The default value of <i>n</i> is 600. Increasing this value can result in more inlined code at the cost of compilation time and memory consumption. Decreasing usually makes the compilation faster and less code will be inlined (which presumably means slower programs). This option is particularly useful for programs that use inlining heavily such as those based on recursive templates with C<font SIZE="-2">++</font>. </p>
<p> Inlining is actually controlled by a number of parameters, which may be specified individually by using <code>&#8211;param</code> <i>name</i><code>=</code><i>value</i>. The <code>-finline-limit=</code><i>n</i> option sets some of these parameters as follows:</p>
<dl>
<dd>
<dl>
<dt><code>max-inline-insns-single</code></p>
<dd>
<pre> is set to I&lt;n&gt;/2.</pre>
<dt><code>max-inline-insns-auto</code></p>
<dd>
<pre> is set to I&lt;n&gt;/2.</pre>
<dt><code>min-inline-insns</code></p>
<dd>
<pre> is set to 130 or I&lt;n&gt;/4, whichever is smaller.</pre>
<dt><code>max-inline-insns-rtl</code></p>
<dd>
<pre> is set to I&lt;n&gt;.</pre>
</dl>
</dl>
<dl>
<dd>See below for a documentation of the individual parameters controlling inlining. </p>
<p> <i>Note:</i> pseudo instruction represents, in this particular context, an abstract measurement of function&#8217;s size. In no way does it represent a count of assembly instructions and as such its exact meaning might change from one release to an another.</dl>
<dt><code>-fkeep-inline-functions</code></p>
<dd>In C, emit <tt>&quot;static&quot;</tt> functions that are declared <tt>&quot;inline&quot;</tt> into the object file, even if the function has been inlined into all of its callers. This switch does not affect functions using the <tt>&quot;extern inline&quot;</tt> extension in <font SIZE="-1">GNU</font> C. In C<font SIZE="-2">++</font>, emit any and all inline functions into the object file.</p>
<dt><code>-fkeep-static-consts</code></p>
<dd>Emit variables declared <tt>&quot;static const&quot;</tt> when optimization isn&#8217;t turned on, even if the variables aren&#8217;t referenced. </p>
<p> <font SIZE="-1">GCC</font> enables this option by default. If you want to force the compiler to check if the variable was referenced, regardless of whether or not optimization is turned on, use the <code>-fno-keep-static-consts</code> option.</p>
<dt><code>-fmerge-constants</code></p>
<dd>Attempt to merge identical constants (string constants and floating point constants) across compilation units. </p>
<p> This option is the default for optimized compilation if the assembler and linker support it. Use <code>-fno-merge-constants</code> to inhibit this behavior. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fmerge-all-constants</code></p>
<dd>Attempt to merge identical constants and identical variables. </p>
<p> This option implies <code>-fmerge-constants</code>. In addition to <code>-fmerge-constants</code> this considers e.g. even constant initialized arrays or initialized constant variables with integral or floating point types. Languages like C or C<font SIZE="-2">++</font> require each non-automatic variable to have distinct location, so using this option will result in non-conforming behavior.</p>
<dt><code>-fmodulo-sched</code></p>
<dd>Perform swing modulo scheduling immediately before the first scheduling pass. This pass looks at innermost loops and reorders their instructions by overlapping different iterations.</p>
<dt><code>-fno-branch-count-reg</code></p>
<dd>Do not use &#8220;decrement and branch&#8221; instructions on a count register, but instead generate a sequence of instructions that decrement a register, compare it against zero, then branch based upon the result. This option is only meaningful on architectures that support such instructions, which include x86, PowerPC, <font SIZE="-1">IA-64</font> and S/390. </p>
<p> The default is <code>-fbranch-count-reg</code>, enabled when <code>-fstrength-reduce</code> is enabled.</p>
<dt><code>-fno-function-cse</code></p>
<dd>Do not put function addresses in registers; make each instruction that calls a constant function contain the function&#8217;s address explicitly. </p>
<p> This option results in less efficient code, but some strange hacks that alter the assembler output may be confused by the optimizations performed when this option is not used. </p>
<p> The default is <code>-ffunction-cse</code></p>
<dt><code>-fno-zero-initialized-in-bss</code></p>
<dd>If the target supports a <font SIZE="-1">BSS</font> section, <font SIZE="-1">GCC</font> by default puts variables that are initialized to zero into <font SIZE="-1">BSS</font>. This can save space in the resulting code. </p>
<p> This option turns off this behavior because some programs explicitly rely on variables going to the data section. E.g., so that the resulting executable can find the beginning of that section and/or make assumptions based on that. </p>
<p> The default is <code>-fzero-initialized-in-bss</code>.</p>
<dt><code>-fbounds-check</code></p>
<dd>For front-ends that support it, generate additional code to check that indices used to access arrays are within the declared range. This is currently only supported by the Java and Fortran front-ends, where this option defaults to true and false respectively.</p>
<dt><code>-fmudflap -fmudflapth -fmudflapir</code></p>
<dd>For front-ends that support it (C and C<font SIZE="-2">++</font>), instrument all risky pointer/array dereferencing operations, some standard library string/heap functions, and some other associated constructs with range/validity tests. Modules so instrumented should be immune to buffer overflows, invalid heap use, and some other classes of C/C<font SIZE="-2">++</font> programming errors. The instrumentation relies on a separate runtime library (<i>libmudflap</i>), which will be linked into a program if <code>-fmudflap</code> is given at link time. Run-time behavior of the instrumented program is controlled by the <font SIZE="-1"><code>MUDFLAP_OPTIONS</code></font> environment variable. See <tt>&quot;env MUDFLAP_OPTIONS=-help a.out&quot;</tt> for its options. </p>
<p> Use <code>-fmudflapth</code> instead of <code>-fmudflap</code> to compile and to link if your program is multi-threaded. Use <code>-fmudflapir</code>, in addition to <code>-fmudflap</code> or <code>-fmudflapth</code>, if instrumentation should ignore pointer reads. This produces less instrumentation (and therefore faster execution) and still provides some protection against outright memory corrupting writes, but allows erroneously read data to propagate within a program.</p>
<dt><code>-fstrength-reduce</code></p>
<dd>Perform the optimizations of loop strength reduction and elimination of iteration variables. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fthread-jumps</code></p>
<dd>Perform optimizations where we check to see if a jump branches to a location where another comparison subsumed by the first is found. If so, the first branch is redirected to either the destination of the second branch or a point immediately following it, depending on whether the condition is known to be true or false. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fcse-follow-jumps</code></p>
<dd>In common subexpression elimination, scan through jump instructions when the target of the jump is not reached by any other path. For example, when <font SIZE="-1">CSE</font> encounters an <tt>&quot;if&quot;</tt> statement with an <tt>&quot;else&quot;</tt> clause, <font SIZE="-1">CSE</font> will follow the jump when the condition tested is false. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fcse-skip-blocks</code></p>
<dd>This is similar to <code>-fcse-follow-jumps</code>, but causes <font SIZE="-1">CSE</font> to follow jumps which conditionally skip over blocks. When <font SIZE="-1">CSE</font> encounters a simple <tt>&quot;if&quot;</tt> statement with no else clause, <code>-fcse-skip-blocks</code> causes <font SIZE="-1">CSE</font> to follow the jump around the body of the <tt>&quot;if&quot;</tt>. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-frerun-cse-after-loop</code></p>
<dd>Re-run common subexpression elimination after loop optimizations has been performed. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-frerun-loop-opt</code></p>
<dd>Run the loop optimizer twice. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fgcse</code></p>
<dd>Perform a global common subexpression elimination pass. This pass also performs global constant and copy propagation. </p>
<p> <i>Note:</i> When compiling a program using computed gotos, a <font SIZE="-1">GCC</font> extension, you may get better runtime performance if you disable the global common subexpression elimination pass by adding <code>-fno-gcse</code> to the command line. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fgcse-lm</code></p>
<dd>When <code>-fgcse-lm</code> is enabled, global common subexpression elimination will attempt to move loads which are only killed by stores into themselves. This allows a loop containing a load/store sequence to be changed to a load outside the loop, and a copy/store within the loop. </p>
<p> Enabled by default when gcse is enabled.</p>
<dt><code>-fgcse-sm</code></p>
<dd>When <code>-fgcse-sm</code> is enabled, a store motion pass is run after global common subexpression elimination. This pass will attempt to move stores out of loops. When used in conjunction with <code>-fgcse-lm</code>, loops containing a load/store sequence can be changed to a load before the loop and a store after the loop. </p>
<p> Not enabled at any optimization level.</p>
<dt><code>-fgcse-las</code></p>
<dd>When <code>-fgcse-las</code> is enabled, the global common subexpression elimination pass eliminates redundant loads that come after stores to the same memory location (both partial and full redundancies). </p>
<p> Not enabled at any optimization level.</p>
<dt><code>-fgcse-after-reload</code></p>
<dd>When <code>-fgcse-after-reload</code> is enabled, a redundant load elimination pass is performed after reload. The purpose of this pass is to cleanup redundant spilling.</p>
<dt><code>-floop-optimize</code></p>
<dd>Perform loop optimizations: move constant expressions out of loops, simplify exit test conditions and optionally do strength-reduction as well. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-floop-optimize2</code></p>
<dd>Perform loop optimizations using the new loop optimizer. The optimizations (loop unrolling, peeling and unswitching, loop invariant motion) are enabled by separate flags.</p>
<dt><code>-funsafe-loop-optimizations</code></p>
<dd>If given, the loop optimizer will assume that loop indices do not overflow, and that the loops with nontrivial exit condition are not infinite. This enables a wider range of loop optimizations even if the loop optimizer itself cannot prove that these assumptions are valid. Using <code>-Wunsafe-loop-optimizations</code>, the compiler will warn you if it finds this kind of loop.</p>
<dt><code>-fcrossjumping</code></p>
<dd>Perform cross-jumping transformation. This transformation unifies equivalent code and save code size. The resulting code may or may not perform better than without cross-jumping. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fif-conversion</code></p>
<dd>Attempt to transform conditional jumps into branch-less equivalents. This include use of conditional moves, min, max, set flags and abs instructions, and some tricks doable by standard arithmetics. The use of conditional execution on chips where it is available is controlled by <tt>&quot;if-conversion2&quot;</tt>. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fif-conversion2</code></p>
<dd>Use conditional execution (where available) to transform conditional jumps into branch-less equivalents. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fdelete-null-pointer-checks</code></p>
<dd>Use global dataflow analysis to identify and eliminate useless checks for null pointers. The compiler assumes that dereferencing a null pointer would have halted the program. If a pointer is checked after it has already been dereferenced, it cannot be null. </p>
<p> In some environments, this assumption is not true, and programs can safely dereference null pointers. Use <code>-fno-delete-null-pointer-checks</code> to disable this optimization for programs which depend on that behavior. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fexpensive-optimizations</code></p>
<dd>Perform a number of minor optimizations that are relatively expensive. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-foptimize-register-move</code></p>
<dd>
<dt><code>-fregmove</code></p>
<dd>Attempt to reassign register numbers in move instructions and as operands of other simple instructions in order to maximize the amount of register tying. This is especially helpful on machines with two-operand instructions. </p>
<p> Note <code>-fregmove</code> and <code>-foptimize-register-move</code> are the same optimization. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fdelayed-branch</code></p>
<dd>If supported for the target machine, attempt to reorder instructions to exploit instruction slots available after delayed branch instructions. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fschedule-insns</code></p>
<dd>If supported for the target machine, attempt to reorder instructions to eliminate execution stalls due to required data being unavailable. This helps machines that have slow floating point or memory load instructions by allowing other instructions to be issued until the result of the load or floating point instruction is required. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fschedule-insns2</code></p>
<dd>Similar to <code>-fschedule-insns</code>, but requests an additional pass of instruction scheduling after register allocation has been done. This is especially useful on machines with a relatively small number of registers and where memory load instructions take more than one cycle. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-sched-interblock</code></p>
<dd>Don&#8217;t schedule instructions across basic blocks. This is normally enabled by default when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fno-sched-spec</code></p>
<dd>Don&#8217;t allow speculative motion of non-load instructions. This is normally enabled by default when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-spec-load</code></p>
<dd>Allow speculative motion of some load instructions. This only makes sense when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-spec-load-dangerous</code></p>
<dd>Allow speculative motion of more load instructions. This only makes sense when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched-stalled-insns=</code><i>n</i></p>
<dd>Define how many insns (if any) can be moved prematurely from the queue of stalled insns into the ready list, during the second scheduling pass.</p>
<dt><code>-fsched-stalled-insns-dep=</code><i>n</i></p>
<dd>Define how many insn groups (cycles) will be examined for a dependency on a stalled insn that is candidate for premature removal from the queue of stalled insns. Has an effect only during the second scheduling pass, and only if <code>-fsched-stalled-insns</code> is used and its value is not zero.</p>
<dt><code>-fsched2-use-superblocks</code></p>
<dd>When scheduling after register allocation, do use superblock scheduling algorithm. Superblock scheduling allows motion across basic block boundaries resulting on faster schedules. This option is experimental, as not all machine descriptions used by <font SIZE="-1">GCC</font> model the <font SIZE="-1">CPU</font> closely enough to avoid unreliable results from the algorithm. </p>
<p> This only makes sense when scheduling after register allocation, i.e. with <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-fsched2-use-traces</code></p>
<dd>Use <code>-fsched2-use-superblocks</code> algorithm when scheduling after register allocation and additionally perform code duplication in order to increase the size of superblocks using tracer pass. See <code>-ftracer</code> for details on trace formation. </p>
<p> This mode should produce faster but significantly longer programs. Also without <code>-fbranch-probabilities</code> the traces constructed may not match the reality and hurt the performance. This only makes sense when scheduling after register allocation, i.e. with <code>-fschedule-insns2</code> or at <code>-O2</code> or higher.</p>
<dt><code>-freschedule-modulo-scheduled-loops</code></p>
<dd>The modulo scheduling comes before the traditional scheduling, if a loop was modulo scheduled we may want to prevent the later scheduling passes from changing its schedule, we use this option to control that.</p>
<dt><code>-fcaller-saves</code></p>
<dd>Enable values to be allocated in registers that will be clobbered by function calls, by emitting extra instructions to save and restore the registers around such calls. Such allocation is done only when it seems to result in better code than would otherwise be produced. </p>
<p> This option is always enabled by default on certain machines, usually those which have no call-preserved registers to use instead. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-ftree-pre</code></p>
<dd>Perform Partial Redundancy Elimination (<font SIZE="-1">PRE</font>) on trees. This flag is enabled by default at <code>-O2</code> and <code>-O3</code>.</p>
<dt><code>-ftree-fre</code></p>
<dd>Perform Full Redundancy Elimination (<font SIZE="-1">FRE</font>) on trees. The difference between <font SIZE="-1">FRE</font> and <font SIZE="-1">PRE</font> is that <font SIZE="-1">FRE</font> only considers expressions that are computed on all paths leading to the redundant computation. This analysis faster than <font SIZE="-1">PRE</font>, though it exposes fewer redundancies. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-copy-prop</code></p>
<dd>Perform copy propagation on trees. This pass eliminates unnecessary copy operations. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-store-copy-prop</code></p>
<dd>Perform copy propagation of memory loads and stores. This pass eliminates unnecessary copy operations in memory references (structures, global variables, arrays, etc). This flag is enabled by default at <code>-O2</code> and higher.</p>
<dt><code>-ftree-salias</code></p>
<dd>Perform structural alias analysis on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-sink</code></p>
<dd>Perform forward store motion on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-ccp</code></p>
<dd>Perform sparse conditional constant propagation (<font SIZE="-1">CCP</font>) on trees. This pass only operates on local scalar variables and is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-store-ccp</code></p>
<dd>Perform sparse conditional constant propagation (<font SIZE="-1">CCP</font>) on trees. This pass operates on both local scalar variables and memory stores and loads (global variables, structures, arrays, etc). This flag is enabled by default at <code>-O2</code> and higher.</p>
<dt><code>-ftree-dce</code></p>
<dd>Perform dead code elimination (<font SIZE="-1">DCE</font>) on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-dominator-opts</code></p>
<dd>Perform a variety of simple scalar cleanups (constant/copy propagation, redundancy elimination, range propagation and expression simplification) based on a dominator tree traversal. This also performs jump threading (to reduce jumps to jumps). This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-ch</code></p>
<dd>Perform loop header copying on trees. This is beneficial since it increases effectiveness of code motion optimizations. It also saves one jump. This flag is enabled by default at <code>-O</code> and higher. It is not enabled for <code>-Os</code>, since it usually increases code size.</p>
<dt><code>-ftree-loop-optimize</code></p>
<dd>Perform loop optimizations on trees. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-loop-linear</code></p>
<dd>Perform linear loop transformations on tree. This flag can improve cache performance and allow further loop optimizations to take place.</p>
<dt><code>-ftree-loop-im</code></p>
<dd>Perform loop invariant motion on trees. This pass moves only invariants that would be hard to handle at <font SIZE="-1">RTL</font> level (function calls, operations that expand to nontrivial sequences of insns). With <code>-funswitch-loops</code> it also moves operands of conditions that are invariant out of the loop, so that we can use just trivial invariantness analysis in loop unswitching. The pass also includes store motion.</p>
<dt><code>-ftree-loop-ivcanon</code></p>
<dd>Create a canonical counter for number of iterations in the loop for that determining number of iterations requires complicated analysis. Later optimizations then may determine the number easily. Useful especially in connection with unrolling.</p>
<dt><code>-fivopts</code></p>
<dd>Perform induction variable optimizations (strength reduction, induction variable merging and induction variable elimination) on trees.</p>
<dt><code>-ftree-sra</code></p>
<dd>Perform scalar replacement of aggregates. This pass replaces structure references with scalars to prevent committing structures to memory too early. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-copyrename</code></p>
<dd>Perform copy renaming on trees. This pass attempts to rename compiler temporaries to other variables at copy locations, usually resulting in variable names which more closely resemble the original variables. This flag is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-ter</code></p>
<dd>Perform temporary expression replacement during the <font SIZE="-1">SSA-</font>&gt;normal phase. Single use/single def temporaries are replaced at their use location with their defining expression. This results in non-GIMPLE code, but gives the expanders much more complex trees to work on resulting in better <font SIZE="-1">RTL</font> generation. This is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-lrs</code></p>
<dd>Perform live range splitting during the <font SIZE="-1">SSA-</font>&gt;normal phase. Distinct live ranges of a variable are split into unique variables, allowing for better optimization later. This is enabled by default at <code>-O</code> and higher.</p>
<dt><code>-ftree-vectorize</code></p>
<dd>Perform loop vectorization on trees.</p>
<dt><code>-ftree-vect-loop-version</code></p>
<dd>Perform loop versioning when doing loop vectorization on trees. When a loop appears to be vectorizable except that data alignment or data dependence cannot be determined at compile time then vectorized and non-vectorized versions of the loop are generated along with runtime checks for alignment or dependence to control which version is executed. This option is enabled by default except at level <code>-Os</code> where it is disabled.</p>
<dt><code>-ftree-vrp</code></p>
<dd>Perform Value Range Propagation on trees. This is similar to the constant propagation pass, but instead of values, ranges of values are propagated. This allows the optimizers to remove unnecessary range checks like array bound checks and null pointer checks. This is enabled by default at <code>-O2</code> and higher. Null pointer check elimination is only done if <code>-fdelete-null-pointer-checks</code> is enabled.</p>
<dt><code>-ftracer</code></p>
<dd>Perform tail duplication to enlarge superblock size. This transformation simplifies the control flow of the function allowing other optimizations to do better job.</p>
<dt><code>-funroll-loops</code></p>
<dd>Unroll loops whose number of iterations can be determined at compile time or upon entry to the loop. <code>-funroll-loops</code> implies both <code>-fstrength-reduce</code> and <code>-frerun-cse-after-loop</code>. This option makes code larger, and may or may not make it run faster.</p>
<dt><code>-funroll-all-loops</code></p>
<dd>Unroll all loops, even if their number of iterations is uncertain when the loop is entered. This usually makes programs run more slowly. <code>-funroll-all-loops</code> implies the same options as <code>-funroll-loops</code>,</p>
<dt><code>-fsplit-ivs-in-unroller</code></p>
<dd>Enables expressing of values of induction variables in later iterations of the unrolled loop using the value in the first iteration. This breaks long dependency chains, thus improving efficiency of the scheduling passes. </p>
<p> Combination of <code>-fweb</code> and <font SIZE="-1">CSE</font> is often sufficient to obtain the same effect. However in cases the loop body is more complicated than a single basic block, this is not reliable. It also does not work at all on some of the architectures due to restrictions in the <font SIZE="-1">CSE</font> pass. </p>
<p> This optimization is enabled by default.</p>
<dt><code>-fvariable-expansion-in-unroller</code></p>
<dd>With this option, the compiler will create multiple copies of some local variables when unrolling a loop which can result in superior code.</p>
<dt><code>-fprefetch-loop-arrays</code></p>
<dd>If supported by the target machine, generate instructions to prefetch memory to improve the performance of loops that access large arrays. </p>
<p> These options may generate better or worse code; results are highly dependent on the structure of loops within the source code.</p>
<dt><code>-fno-peephole</code></p>
<dd>
<dt><code>-fno-peephole2</code></p>
<dd>Disable any machine-specific peephole optimizations. The difference between <code>-fno-peephole</code> and <code>-fno-peephole2</code> is in how they are implemented in the compiler; some targets use one, some use the other, a few use both. </p>
<p> <code>-fpeephole</code> is enabled by default. <code>-fpeephole2</code> enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fno-guess-branch-probability</code></p>
<dd>Do not guess branch probabilities using heuristics. </p>
<p> <font SIZE="-1">GCC</font> will use heuristics to guess branch probabilities if they are not provided by profiling feedback (<code>-fprofile-arcs</code>). These heuristics are based on the control flow graph. If some branch probabilities are specified by <code>__builtin_expect</code>, then the heuristics will be used to guess branch probabilities for the rest of the control flow graph, taking the <code>__builtin_expect</code> info into account. The interactions between the heuristics and <code>__builtin_expect</code> can be complex, and in some cases, it may be useful to disable the heuristics so that the effects of <code>__builtin_expect</code> are easier to understand. </p>
<p> The default is <code>-fguess-branch-probability</code> at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-freorder-blocks</code></p>
<dd>Reorder basic blocks in the compiled function in order to reduce number of taken branches and improve code locality. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-freorder-blocks-and-partition</code></p>
<dd>In addition to reordering basic blocks in the compiled function, in order to reduce number of taken branches, partitions hot and cold basic blocks into separate sections of the assembly and .o files, to improve paging and cache locality performance. </p>
<p> This optimization is automatically turned off in the presence of exception handling, for linkonce sections, for functions with a user-defined section attribute and on any architecture that does not support named sections.</p>
<dt><code>-freorder-functions</code></p>
<dd>Reorder functions in the object file in order to improve code locality. This is implemented by using special subsections <tt>&quot;.text.hot&quot;</tt> for most frequently executed functions and <tt>&quot;.text.unlikely&quot;</tt> for unlikely executed functions. Reordering is done by the linker so object file format must support named sections and linker must place them in a reasonable way. </p>
<p> Also profile feedback must be available in to make this option effective. See <code>-fprofile-arcs</code> for details. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fstrict-aliasing</code></p>
<dd>Allows the compiler to assume the strictest aliasing rules applicable to the language being compiled. For C (and C<font SIZE="-2">++</font>), this activates optimizations based on the type of expressions. In particular, an object of one type is assumed never to reside at the same address as an object of a different type, unless the types are almost the same. For example, an <tt>&quot;unsigned int&quot;</tt> can alias an <tt>&quot;int&quot;</tt>, but not a <tt>&quot;void*&quot;</tt> or a <tt>&quot;double&quot;</tt>. A character type may alias any other type. </p>
<p> Pay special attention to code like this: </p>
<pre> union a_union {
 int i;
 double d;
 };</pre>
<pre> int f() {
 a_union t;
 t.d = 3.0;
 return t.i;
 }</pre>
<p>The practice of reading from a different union member than the one most recently written to (called &#8220;type-punning&#8221;) is common. Even with <code>-fstrict-aliasing</code>, type-punning is allowed, provided the memory is accessed through the union type. So, the code above will work as expected. However, this code might not: </p>
<pre> int f() {
 a_union t;
 int* ip;
 t.d = 3.0;
 ip = &amp;t.i;
 return *ip;
 }</pre>
<p>Every language that wishes to perform language-specific alias analysis should define a function that computes, given an <tt>&quot;tree&quot;</tt> node, an alias set for the node. Nodes in different alias sets are not allowed to alias. For an example, see the C front-end function <tt>&quot;c_get_alias_set&quot;</tt>. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-falign-functions</code></p>
<dd>
<dt><code>-falign-functions=</code><i>n</i></p>
<dd>Align the start of functions to the next power-of-two greater than <i>n</i>, skipping up to <i>n</i> bytes. For instance, <code>-falign-functions=32</code> aligns functions to the next 32-byte boundary, but <code>-falign-functions=24</code> would align to the next 32-byte boundary only if this can be done by skipping 23 bytes or less. </p>
<p> <code>-fno-align-functions</code> and <code>-falign-functions=1</code> are equivalent and mean that functions will not be aligned. </p>
<p> Some assemblers only support this flag when <i>n</i> is a power of two; in that case, it is rounded up. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-falign-labels</code></p>
<dd>
<dt><code>-falign-labels=</code><i>n</i></p>
<dd>Align all branch targets to a power-of-two boundary, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. This option can easily make code slower, because it must insert dummy operations for when the branch target is reached in the usual flow of the code. </p>
<p> <code>-fno-align-labels</code> and <code>-falign-labels=1</code> are equivalent and mean that labels will not be aligned. </p>
<p> If <code>-falign-loops</code> or <code>-falign-jumps</code> are applicable and are greater than this value, then their values are used instead. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default which is very likely to be <code>1</code>, meaning no alignment. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-falign-loops</code></p>
<dd>
<dt><code>-falign-loops=</code><i>n</i></p>
<dd>Align loops to a power-of-two boundary, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. The hope is that the loop will be executed many times, which will make up for any execution of the dummy operations. </p>
<p> <code>-fno-align-loops</code> and <code>-falign-loops=1</code> are equivalent and mean that loops will not be aligned. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-falign-jumps</code></p>
<dd>
<dt><code>-falign-jumps=</code><i>n</i></p>
<dd>Align branch targets to a power-of-two boundary, for branch targets where the targets can only be reached by jumping, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. In this case, no dummy operations need be executed. </p>
<p> <code>-fno-align-jumps</code> and <code>-falign-jumps=1</code> are equivalent and mean that loops will not be aligned. </p>
<p> If <i>n</i> is not specified or is zero, use a machine-dependent default. </p>
<p> Enabled at levels <code>-O2</code>, <code>-O3</code>.</p>
<dt><code>-funit-at-a-time</code></p>
<dd>Parse the whole compilation unit before starting to produce code. This allows some extra optimizations to take place but consumes more memory (in general). There are some compatibility issues with <i>unit-at-at-time</i> mode:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>enabling <i>unit-at-a-time</i> mode may change the order in which functions, variables, and top-level <tt>&quot;asm&quot;</tt> statements are emitted, and will likely break code relying on some particular ordering. The majority of such top-level <tt>&quot;asm&quot;</tt> statements, though, can be replaced by <tt>&quot;section&quot;</tt> attributes.</p>
<dt>*</p>
<dd><i>unit-at-a-time</i> mode removes unreferenced static variables and functions. This may result in undefined references when an <tt>&quot;asm&quot;</tt> statement refers directly to variables or functions that are otherwise unused. In that case either the variable/function shall be listed as an operand of the <tt>&quot;asm&quot;</tt> statement operand or, in the case of top-level <tt>&quot;asm&quot;</tt> statements the attribute <tt>&quot;used&quot;</tt> shall be used on the declaration.</p>
<dt>*</p>
<dd>Static functions now can use non-standard passing conventions that may break <tt>&quot;asm&quot;</tt> statements calling functions directly. Again, attribute <tt>&quot;used&quot;</tt> will prevent this behavior.</dl>
</dl>
<dl>
<dd>As a temporary workaround, <code>-fno-unit-at-a-time</code> can be used, but this scheme may not be supported by future releases of <font SIZE="-1">GCC</font>. </p>
<p> Enabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</dl>
<dt><code>-fweb</code></p>
<dd>Constructs webs as commonly used for register allocation purposes and assign each web individual pseudo register. This allows the register allocation pass to operate on pseudos directly, but also strengthens several other optimization passes, such as <font SIZE="-1">CSE</font>, loop optimizer and trivial dead code remover. It can, however, make debugging impossible, since variables will no longer stay in a &#8220;home register&#8221;. </p>
<p> Enabled by default with <code>-funroll-loops</code>.</p>
<dt><code>-fwhole-program</code></p>
<dd>Assume that the current compilation unit represents whole program being compiled. All public functions and variables with the exception of <tt>&quot;main&quot;</tt> and those merged by attribute <tt>&quot;externally_visible&quot;</tt> become static functions and in a affect gets more aggressively optimized by interprocedural optimizers. While this option is equivalent to proper use of <tt>&quot;static&quot;</tt> keyword for programs consisting of single file, in combination with option <code>&#8211;combine</code> this flag can be used to compile most of smaller scale C programs since the functions and variables become local for the whole combined compilation unit, not for the single source file itself.</p>
<dt><code>-fno-cprop-registers</code></p>
<dd>After register allocation and post-register allocation instruction splitting, we perform a copy-propagation pass to try to reduce scheduling dependencies and occasionally eliminate the copy. </p>
<p> Disabled at levels <code>-O</code>, <code>-O2</code>, <code>-O3</code>, <code>-Os</code>.</p>
<dt><code>-fprofile-generate</code></p>
<dd>Enable options usually used for instrumenting application to produce profile useful for later recompilation with profile feedback based optimization. You must use <code>-fprofile-generate</code> both when compiling and when linking your program. </p>
<p> The following options are enabled: <tt>&quot;-fprofile-arcs&quot;</tt>, <tt>&quot;-fprofile-values&quot;</tt>, <tt>&quot;-fvpt&quot;</tt>.</p>
<dt><code>-fprofile-use</code></p>
<dd>Enable profile feedback directed optimizations, and optimizations generally profitable only with profile feedback available. </p>
<p> The following options are enabled: <tt>&quot;-fbranch-probabilities&quot;</tt>, <tt>&quot;-fvpt&quot;</tt>, <tt>&quot;-funroll-loops&quot;</tt>, <tt>&quot;-fpeel-loops&quot;</tt>, <tt>&quot;-ftracer&quot;</tt>, <tt>&quot;-fno-loop-optimize&quot;</tt>.</dl>
<p> The following options control compiler behavior regarding floating point arithmetic. These options trade off between speed and correctness. All must be specifically enabled.</p>
<dl>
<dt><code>-ffloat-store</code></p>
<dd>Do not store floating point variables in registers, and inhibit other options that might change whether a floating point value is taken from a register or memory. </p>
<p> This option prevents undesirable excess precision on machines such as the 68000 where the floating registers (of the 68881) keep more precision than a <tt>&quot;double&quot;</tt> is supposed to have. Similarly for the x86 architecture. For most programs, the excess precision does only good, but a few programs rely on the precise definition of <font SIZE="-1">IEEE</font> floating point. Use <code>-ffloat-store</code> for such programs, after modifying them to store all pertinent intermediate computations into variables.</p>
<dt><code>-ffast-math</code></p>
<dd>Sets <code>-fno-math-errno</code>, <code>-funsafe-math-optimizations</code>, <code>-fno-trapping-math</code>, <code>-ffinite-math-only</code>, <code>-fno-rounding-math</code>, <code>-fno-signaling-nans</code> and <code>fcx-limited-range</code>. </p>
<p> This option causes the preprocessor macro <tt>&quot;__FAST_MATH__&quot;</tt> to be defined. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions.</p>
<dt><code>-fno-math-errno</code></p>
<dd>Do not set <font SIZE="-1">ERRNO</font> after calling math functions that are executed with a single instruction, e.g., sqrt. A program that relies on <font SIZE="-1">IEEE</font> exceptions for math error handling may want to use this flag for speed while maintaining <font SIZE="-1">IEEE</font> arithmetic compatibility. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-fmath-errno</code>. </p>
<p> On Darwin systems, the math library never sets <tt>&quot;errno&quot;</tt>. There is therefore no reason for the compiler to consider the possibility that it might, and <code>-fno-math-errno</code> is the default.</p>
<dt><code>-funsafe-math-optimizations</code></p>
<dd>Allow optimizations for floating-point arithmetic that (a) assume that arguments and results are valid and (b) may violate <font SIZE="-1">IEEE</font> or <font SIZE="-1">ANSI</font> standards. When used at link-time, it may include libraries or startup files that change the default <font SIZE="-1">FPU</font> control word or other similar optimizations. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-fno-unsafe-math-optimizations</code>.</p>
<dt><code>-ffinite-math-only</code></p>
<dd>Allow optimizations for floating-point arithmetic that assume that arguments and results are not NaNs or +-Infs. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications. </p>
<p> The default is <code>-fno-finite-math-only</code>.</p>
<dt><code>-fno-trapping-math</code></p>
<dd>Compile code assuming that floating-point operations cannot generate user-visible traps. These traps include division by zero, overflow, underflow, inexact result and invalid operation. This option implies <code>-fno-signaling-nans</code>. Setting this option may allow faster code if one relies on &#8220;non-stop&#8221; <font SIZE="-1">IEEE</font> arithmetic, for example. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-ftrapping-math</code>.</p>
<dt><code>-frounding-math</code></p>
<dd>Disable transformations and optimizations that assume default floating point rounding behavior. This is round-to-zero for all floating point to integer conversions, and round-to-nearest for all other arithmetic truncations. This option should be specified for programs that change the <font SIZE="-1">FP</font> rounding mode dynamically, or that may be executed with a non-default rounding mode. This option disables constant folding of floating point expressions at compile-time (which may be affected by rounding mode) and arithmetic transformations that are unsafe in the presence of sign-dependent rounding modes. </p>
<p> The default is <code>-fno-rounding-math</code>. </p>
<p> This option is experimental and does not currently guarantee to disable all <font SIZE="-1">GCC</font> optimizations that are affected by rounding mode. Future versions of <font SIZE="-1">GCC</font> may provide finer control of this setting using C99&#8217;s <tt>&quot;FENV_ACCESS&quot;</tt> pragma. This command line option will be used to specify the default state for <tt>&quot;FENV_ACCESS&quot;</tt>.</p>
<dt><code>-fsignaling-nans</code></p>
<dd>Compile code assuming that <font SIZE="-1">IEEE</font> signaling NaNs may generate user-visible traps during floating-point operations. Setting this option disables optimizations that may change the number of exceptions visible with signaling NaNs. This option implies <code>-ftrapping-math</code>. </p>
<p> This option causes the preprocessor macro <tt>&quot;__SUPPORT_SNAN__&quot;</tt> to be defined. </p>
<p> The default is <code>-fno-signaling-nans</code>. </p>
<p> This option is experimental and does not currently guarantee to disable all <font SIZE="-1">GCC</font> optimizations that affect signaling NaN behavior.</p>
<dt><code>-fsingle-precision-constant</code></p>
<dd>Treat floating point constant as single precision constant instead of implicitly converting it to double precision constant.</p>
<dt><code>-fcx-limited-range</code></p>
<dd>
<dt><code>-fno-cx-limited-range</code></p>
<dd>When enabled, this option states that a range reduction step is not needed when performing complex division. The default is <code>-fno-cx-limited-range</code>, but is enabled by <code>-ffast-math</code>. </p>
<p> This option controls the default setting of the <font SIZE="-1">ISO</font> C99 <tt>&quot;CX_LIMITED_RANGE&quot;</tt> pragma. Nevertheless, the option applies to all languages.</dl>
<p> The following options control optimizations that may improve performance, but are not enabled by any <code>-O</code> options. This section includes experimental options that may produce broken code.</p>
<dl>
<dt><code>-fbranch-probabilities</code></p>
<dd>After running a program compiled with <code>-fprofile-arcs</code>, you can compile it a second time using <code>-fbranch-probabilities</code>, to improve optimizations based on the number of times each branch was taken. When the program compiled with <code>-fprofile-arcs</code> exits it saves arc execution counts to a file called <i>sourcename.gcda</i> for each source file The information in this data file is very dependent on the structure of the generated code, so you must use the same source code and the same optimization options for both compilations. </p>
<p> With <code>-fbranch-probabilities</code>, <font SIZE="-1">GCC</font> puts a <font SIZE="-1"><code>REG_BR_PROB</code></font> note on each <font SIZE="-1"><code>JUMP_INSN</code></font> and <font SIZE="-1"><code>CALL_INSN</code></font>. These can be used to improve optimization. Currently, they are only used in one place: in <i>reorg.c</i>, instead of guessing which path a branch is mostly to take, the <font SIZE="-1"><code>REG_BR_PROB</code></font> values are used to exactly determine which path is taken more often.</p>
<dt><code>-fprofile-values</code></p>
<dd>If combined with <code>-fprofile-arcs</code>, it adds code so that some data about values of expressions in the program is gathered. </p>
<p> With <code>-fbranch-probabilities</code>, it reads back the data gathered from profiling values of expressions and adds <font SIZE="-1"><code>REG_VALUE_PROFILE</code></font> notes to instructions for their later usage in optimizations. </p>
<p> Enabled with <code>-fprofile-generate</code> and <code>-fprofile-use</code>.</p>
<dt><code>-fvpt</code></p>
<dd>If combined with <code>-fprofile-arcs</code>, it instructs the compiler to add a code to gather information about values of expressions. </p>
<p> With <code>-fbranch-probabilities</code>, it reads back the data gathered and actually performs the optimizations based on them. Currently the optimizations include specialization of division operation using the knowledge about the value of the denominator.</p>
<dt><code>-frename-registers</code></p>
<dd>Attempt to avoid false dependencies in scheduled code by making use of registers left over after register allocation. This optimization will most benefit processors with lots of registers. Depending on the debug information format adopted by the target, however, it can make debugging impossible, since variables will no longer stay in a &#8220;home register&#8221;. </p>
<p> Enabled by default with <code>-funroll-loops</code>.</p>
<dt><code>-ftracer</code></p>
<dd>Perform tail duplication to enlarge superblock size. This transformation simplifies the control flow of the function allowing other optimizations to do better job. </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-funroll-loops</code></p>
<dd>Unroll loops whose number of iterations can be determined at compile time or upon entry to the loop. <code>-funroll-loops</code> implies <code>-frerun-cse-after-loop</code>, <code>-fweb</code> and <code>-frename-registers</code>. It also turns on complete loop peeling (i.e. complete removal of loops with small constant number of iterations). This option makes code larger, and may or may not make it run faster. </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-funroll-all-loops</code></p>
<dd>Unroll all loops, even if their number of iterations is uncertain when the loop is entered. This usually makes programs run more slowly. <code>-funroll-all-loops</code> implies the same options as <code>-funroll-loops</code>.</p>
<dt><code>-fpeel-loops</code></p>
<dd>Peels the loops for that there is enough information that they do not roll much (from profile feedback). It also turns on complete loop peeling (i.e. complete removal of loops with small constant number of iterations). </p>
<p> Enabled with <code>-fprofile-use</code>.</p>
<dt><code>-fmove-loop-invariants</code></p>
<dd>Enables the loop invariant motion pass in the new loop optimizer. Enabled at level <code>-O1</code></p>
<dt><code>-funswitch-loops</code></p>
<dd>Move branches with loop invariant conditions out of the loop, with duplicates of the loop on both branches (modified according to result of the condition).</p>
<dt><code>-fprefetch-loop-arrays</code></p>
<dd>If supported by the target machine, generate instructions to prefetch memory to improve the performance of loops that access large arrays. </p>
<p> Disabled at level <code>-Os</code>.</p>
<dt><code>-ffunction-sections</code></p>
<dd>
<dt><code>-fdata-sections</code></p>
<dd>Place each function or data item into its own section in the output file if the target supports arbitrary sections. The name of the function or the name of the data item determines the section&#8217;s name in the output file. </p>
<p> Use these options on systems where the linker can perform optimizations to improve locality of reference in the instruction space. Most systems using the <font SIZE="-1">ELF</font> object format and <font SIZE="-1">SPARC</font> processors running Solaris 2 have linkers with such optimizations. <font SIZE="-1">AIX</font> may have these optimizations in the future. </p>
<p> Only use these options when there are significant benefits from doing so. When you specify these options, the assembler and linker will create larger object and executable files and will also be slower. You will not be able to use <tt>&quot;gprof&quot;</tt> on all systems if you specify this option and you may have problems with debugging if you specify both this option and <code>-g</code>.</p>
<dt><code>-fbranch-target-load-optimize</code></p>
<dd>Perform branch target register load optimization before prologue / epilogue threading. The use of target registers can typically be exposed only during reload, thus hoisting loads out of loops and doing inter-block scheduling needs a separate optimization pass.</p>
<dt><code>-fbranch-target-load-optimize2</code></p>
<dd>Perform branch target register load optimization after prologue / epilogue threading.</p>
<dt><code>-fbtr-bb-exclusive</code></p>
<dd>When performing branch target register load optimization, don&#8217;t reuse branch target registers in within any basic block.</p>
<dt><code>-fstack-protector</code></p>
<dd>Emit extra code to check for buffer overflows, such as stack smashing attacks. This is done by adding a guard variable to functions with vulnerable objects. This includes functions that call alloca, and functions with buffers larger than 8 bytes. The guards are initialized when a function is entered and then checked when the function exits. If a guard check fails, an error message is printed and the program exits.</p>
<dt><code>-fstack-protector-all</code></p>
<dd>Like <code>-fstack-protector</code> except that all functions are protected.</p>
<dt><code>&#8211;param</code> <i>name</i><code>=</code><i>value</i></p>
<dd>In some places, <font SIZE="-1">GCC</font> uses various constants to control the amount of optimization that is done. For example, <font SIZE="-1">GCC</font> will not inline functions that contain more that a certain number of instructions. You can control some of these constants on the command-line using the <code>&#8211;param</code> option. </p>
<p> The names of specific parameters, and the meaning of the values, are tied to the internals of the compiler, and are subject to change without notice in future releases. </p>
<p> In each case, the <i>value</i> is an integer. The allowable choices for <i>name</i> are given in the following table:</p>
<dl>
<dd>
<dl>
<dt><code>salias-max-implicit-fields</code></p>
<dd>The maximum number of fields in a variable without direct structure accesses for which structure aliasing will consider trying to track each field. The default is 5</p>
<dt><code>sra-max-structure-size</code></p>
<dd>The maximum structure size, in bytes, at which the scalar replacement of aggregates (<font SIZE="-1">SRA</font>) optimization will perform block copies. The default value, 0, implies that <font SIZE="-1">GCC</font> will select the most appropriate size itself.</p>
<dt><code>sra-field-structure-ratio</code></p>
<dd>The threshold ratio (as a percentage) between instantiated fields and the complete structure size. We say that if the ratio of the number of bytes in instantiated fields to the number of bytes in the complete structure exceeds this parameter, then block copies are not used. The default is 75.</p>
<dt><code>max-crossjump-edges</code></p>
<dd>The maximum number of incoming edges to consider for crossjumping. The algorithm used by <code>-fcrossjumping</code> is O(N^2) in the number of edges incoming to each block. Increasing values mean more aggressive optimization, making the compile time increase with probably small improvement in executable size.</p>
<dt><code>min-crossjump-insns</code></p>
<dd>The minimum number of instructions which must be matched at the end of two blocks before crossjumping will be performed on them. This value is ignored in the case where all instructions in the block being crossjumped from are matched. The default value is 5.</p>
<dt><code>max-grow-copy-bb-insns</code></p>
<dd>The maximum code size expansion factor when copying basic blocks instead of jumping. The expansion is relative to a jump instruction. The default value is 8.</p>
<dt><code>max-goto-duplication-insns</code></p>
<dd>The maximum number of instructions to duplicate to a block that jumps to a computed goto. To avoid O(N^2) behavior in a number of passes, <font SIZE="-1">GCC</font> factors computed gotos early in the compilation process, and unfactors them as late as possible. Only computed jumps at the end of a basic blocks with no more than max-goto-duplication-insns are unfactored. The default value is 8.</p>
<dt><code>max-delay-slot-insn-search</code></p>
<dd>The maximum number of instructions to consider when looking for an instruction to fill a delay slot. If more than this arbitrary number of instructions is searched, the time savings from filling the delay slot will be minimal so stop searching. Increasing values mean more aggressive optimization, making the compile time increase with probably small improvement in executable run time.</p>
<dt><code>max-delay-slot-live-search</code></p>
<dd>When trying to fill delay slots, the maximum number of instructions to consider when searching for a block with valid live register information. Increasing this arbitrarily chosen value means more aggressive optimization, increasing the compile time. This parameter should be removed when the delay slot code is rewritten to maintain the control-flow graph.</p>
<dt><code>max-gcse-memory</code></p>
<dd>The approximate maximum amount of memory that will be allocated in order to perform the global common subexpression elimination optimization. If more memory than specified is required, the optimization will not be done.</p>
<dt><code>max-gcse-passes</code></p>
<dd>The maximum number of passes of <font SIZE="-1">GCSE</font> to run. The default is 1.</p>
<dt><code>max-pending-list-length</code></p>
<dd>The maximum number of pending dependencies scheduling will allow before flushing the current state and starting over. Large functions with few branches or calls can create excessively large lists which needlessly consume memory and resources.</p>
<dt><code>max-inline-insns-single</code></p>
<dd>Several parameters control the tree inliner used in gcc. This number sets the maximum number of instructions (counted in <font SIZE="-1">GCC</font>&#8216;s internal representation) in a single function that the tree inliner will consider for inlining. This only affects functions declared inline and methods implemented in a class declaration (C<font SIZE="-2">++</font>). The default value is 450.</p>
<dt><code>max-inline-insns-auto</code></p>
<dd>When you use <code>-finline-functions</code> (included in <code>-O3</code>), a lot of functions that would otherwise not be considered for inlining by the compiler will be investigated. To those functions, a different (more restrictive) limit compared to functions declared inline can be applied. The default value is 90.</p>
<dt><code>large-function-insns</code></p>
<dd>The limit specifying really large functions. For functions larger than this limit after inlining inlining is constrained by <code>&#8211;param large-function-growth</code>. This parameter is useful primarily to avoid extreme compilation time caused by non-linear algorithms used by the backend. This parameter is ignored when <code>-funit-at-a-time</code> is not used. The default value is 2700.</p>
<dt><code>large-function-growth</code></p>
<dd>Specifies maximal growth of large function caused by inlining in percents. This parameter is ignored when <code>-funit-at-a-time</code> is not used. The default value is 100 which limits large function growth to 2.0 times the original size.</p>
<dt><code>large-unit-insns</code></p>
<dd>The limit specifying large translation unit. Growth caused by inlining of units larger than this limit is limited by <code>&#8211;param inline-unit-growth</code>. For small units this might be too tight (consider unit consisting of function A that is inline and B that just calls A three time. If B is small relative to A, the growth of unit is 300\% and yet such inlining is very sane. For very large units consisting of small inlininable functions however the overall unit growth limit is needed to avoid exponential explosion of code size. Thus for smaller units, the size is increased to <code>&#8211;param large-unit-insns</code> before aplying <code>&#8211;param inline-unit-growth</code>. The default is 10000</p>
<dt><code>inline-unit-growth</code></p>
<dd>Specifies maximal overall growth of the compilation unit caused by inlining. This parameter is ignored when <code>-funit-at-a-time</code> is not used. The default value is 50 which limits unit growth to 1.5 times the original size.</p>
<dt><code>max-inline-insns-recursive</code></p>
<dd>
<dt><code>max-inline-insns-recursive-auto</code></p>
<dd>Specifies maximum number of instructions out-of-line copy of self recursive inline function can grow into by performing recursive inlining. </p>
<p> For functions declared inline <code>&#8211;param max-inline-insns-recursive</code> is taken into account. For function not declared inline, recursive inlining happens only when <code>-finline-functions</code> (included in <code>-O3</code>) is enabled and <code>&#8211;param max-inline-insns-recursive-auto</code> is used. The default value is 450.</p>
<dt><code>max-inline-recursive-depth</code></p>
<dd>
<dt><code>max-inline-recursive-depth-auto</code></p>
<dd>Specifies maximum recursion depth used by the recursive inlining. </p>
<p> For functions declared inline <code>&#8211;param max-inline-recursive-depth</code> is taken into account. For function not declared inline, recursive inlining happens only when <code>-finline-functions</code> (included in <code>-O3</code>) is enabled and <code>&#8211;param max-inline-recursive-depth-auto</code> is used. The default value is 450.</p>
<dt><code>min-inline-recursive-probability</code></p>
<dd>Recursive inlining is profitable only for function having deep recursion in average and can hurt for function having little recursion depth by increasing the prologue size or complexity of function body to other optimizers. </p>
<p> When profile feedback is available (see <code>-fprofile-generate</code>) the actual recursion depth can be guessed from probability that function will recurse via given call expression. This parameter limits inlining only to call expression whose probability exceeds given threshold (in percents). The default value is 10.</p>
<dt><code>inline-call-cost</code></p>
<dd>Specify cost of call instruction relative to simple arithmetics operations (having cost of 1). Increasing this cost disqualifies inlining of non-leaf functions and at the same time increases size of leaf function that is believed to reduce function size by being inlined. In effect it increases amount of inlining for code having large abstraction penalty (many functions that just pass the arguments to other functions) and decrease inlining for code with low abstraction penalty. The default value is 16.</p>
<dt><code>max-unrolled-insns</code></p>
<dd>The maximum number of instructions that a loop should have if that loop is unrolled, and if the loop is unrolled, it determines how many times the loop code is unrolled.</p>
<dt><code>max-average-unrolled-insns</code></p>
<dd>The maximum number of instructions biased by probabilities of their execution that a loop should have if that loop is unrolled, and if the loop is unrolled, it determines how many times the loop code is unrolled.</p>
<dt><code>max-unroll-times</code></p>
<dd>The maximum number of unrollings of a single loop.</p>
<dt><code>max-peeled-insns</code></p>
<dd>The maximum number of instructions that a loop should have if that loop is peeled, and if the loop is peeled, it determines how many times the loop code is peeled.</p>
<dt><code>max-peel-times</code></p>
<dd>The maximum number of peelings of a single loop.</p>
<dt><code>max-completely-peeled-insns</code></p>
<dd>The maximum number of insns of a completely peeled loop.</p>
<dt><code>max-completely-peel-times</code></p>
<dd>The maximum number of iterations of a loop to be suitable for complete peeling.</p>
<dt><code>max-unswitch-insns</code></p>
<dd>The maximum number of insns of an unswitched loop.</p>
<dt><code>max-unswitch-level</code></p>
<dd>The maximum number of branches unswitched in a single loop.</p>
<dt><code>lim-expensive</code></p>
<dd>The minimum cost of an expensive expression in the loop invariant motion.</p>
<dt><code>iv-consider-all-candidates-bound</code></p>
<dd>Bound on number of candidates for induction variables below that all candidates are considered for each use in induction variable optimizations. Only the most relevant candidates are considered if there are more candidates, to avoid quadratic time complexity.</p>
<dt><code>iv-max-considered-uses</code></p>
<dd>The induction variable optimizations give up on loops that contain more induction variable uses.</p>
<dt><code>iv-always-prune-cand-set-bound</code></p>
<dd>If number of candidates in the set is smaller than this value, we always try to remove unnecessary ivs from the set during its optimization when a new iv is added to the set.</p>
<dt><code>scev-max-expr-size</code></p>
<dd>Bound on size of expressions used in the scalar evolutions analyzer. Large expressions slow the analyzer.</p>
<dt><code>vect-max-version-checks</code></p>
<dd>The maximum number of runtime checks that can be performed when doing loop versioning in the vectorizer. See option ftree-vect-loop-version for more information.</p>
<dt><code>max-iterations-to-track</code></p>
<dd>The maximum number of iterations of a loop the brute force algorithm for analysis of # of iterations of the loop tries to evaluate.</p>
<dt><code>hot-bb-count-fraction</code></p>
<dd>Select fraction of the maximal count of repetitions of basic block in program given basic block needs to have to be considered hot.</p>
<dt><code>hot-bb-frequency-fraction</code></p>
<dd>Select fraction of the maximal frequency of executions of basic block in function given basic block needs to have to be considered hot</p>
<dt><code>max-predicted-iterations</code></p>
<dd>The maximum number of loop iterations we predict statically. This is useful in cases where function contain single loop with known bound and other loop with unknown. We predict the known number of iterations correctly, while the unknown number of iterations average to roughly 10. This means that the loop without bounds would appear artificially cold relative to the other one.</p>
<dt><code>tracer-dynamic-coverage</code></p>
<dd>
<dt><code>tracer-dynamic-coverage-feedback</code></p>
<dd>This value is used to limit superblock formation once the given percentage of executed instructions is covered. This limits unnecessary code size expansion. </p>
<p> The <code>tracer-dynamic-coverage-feedback</code> is used only when profile feedback is available. The real profiles (as opposed to statically estimated ones) are much less balanced allowing the threshold to be larger value.</p>
<dt><code>tracer-max-code-growth</code></p>
<dd>Stop tail duplication once code growth has reached given percentage. This is rather hokey argument, as most of the duplicates will be eliminated later in cross jumping, so it may be set to much higher values than is the desired code growth.</p>
<dt><code>tracer-min-branch-ratio</code></p>
<dd>Stop reverse growth when the reverse probability of best edge is less than this threshold (in percent).</p>
<dt><code>tracer-min-branch-ratio</code></p>
<dd>
<dt><code>tracer-min-branch-ratio-feedback</code></p>
<dd>Stop forward growth if the best edge do have probability lower than this threshold. </p>
<p> Similarly to <code>tracer-dynamic-coverage</code> two values are present, one for compilation for profile feedback and one for compilation without. The value for compilation with profile feedback needs to be more conservative (higher) in order to make tracer effective.</p>
<dt><code>max-cse-path-length</code></p>
<dd>Maximum number of basic blocks on path that cse considers. The default is 10.</p>
<dt><code>max-cse-insns</code></p>
<dd>The maximum instructions <font SIZE="-1">CSE</font> process before flushing. The default is 1000.</p>
<dt><code>global-var-threshold</code></p>
<dd>Counts the number of function calls (<i>n</i>) and the number of call-clobbered variables (<i>v</i>). If <i>n</i>x<i>v</i> is larger than this limit, a single artificial variable will be created to represent all the call-clobbered variables at function call sites. This artificial variable will then be made to alias every call-clobbered variable. (done as <tt>&quot;int * size_t&quot;</tt> on the host machine; beware overflow).</p>
<dt><code>max-aliased-vops</code></p>
<dd>Maximum number of virtual operands allowed to represent aliases before triggering the alias grouping heuristic. Alias grouping reduces compile times and memory consumption needed for aliasing at the expense of precision loss in alias information.</p>
<dt><code>ggc-min-expand</code></p>
<dd><font SIZE="-1">GCC</font> uses a garbage collector to manage its own memory allocation. This parameter specifies the minimum percentage by which the garbage collector&#8217;s heap should be allowed to expand between collections. Tuning this may improve compilation speed; it has no effect on code generation. </p>
<p> The default is 30% + 70% * (<font SIZE="-1">RAM/1GB</font>) with an upper bound of 100% when <font SIZE="-1">RAM</font> &gt;= 1GB. If <tt>&quot;getrlimit&quot;</tt> is available, the notion of &#8220;<font SIZE="-1">RAM</font>&#8221; is the smallest of actual <font SIZE="-1">RAM</font> and <tt>&quot;RLIMIT_DATA&quot;</tt> or <tt>&quot;RLIMIT_AS&quot;</tt>. If <font SIZE="-1">GCC</font> is not able to calculate <font SIZE="-1">RAM</font> on a particular platform, the lower bound of 30% is used. Setting this parameter and <code>ggc-min-heapsize</code> to zero causes a full collection to occur at every opportunity. This is extremely slow, but can be useful for debugging.</p>
<dt><code>ggc-min-heapsize</code></p>
<dd>Minimum size of the garbage collector&#8217;s heap before it begins bothering to collect garbage. The first collection occurs after the heap expands by <code>ggc-min-expand</code>% beyond <code>ggc-min-heapsize</code>. Again, tuning this may improve compilation speed, and has no effect on code generation. </p>
<p> The default is the smaller of <font SIZE="-1">RAM/8</font>, <font SIZE="-1">RLIMIT_RSS</font>, or a limit which tries to ensure that <font SIZE="-1">RLIMIT_DATA</font> or <font SIZE="-1">RLIMIT_AS</font> are not exceeded, but with a lower bound of 4096 (four megabytes) and an upper bound of 131072 (128 megabytes). If <font SIZE="-1">GCC</font> is not able to calculate <font SIZE="-1">RAM</font> on a particular platform, the lower bound is used. Setting this parameter very large effectively disables garbage collection. Setting this parameter and <code>ggc-min-expand</code> to zero causes a full collection to occur at every opportunity.</p>
<dt><code>max-reload-search-insns</code></p>
<dd>The maximum number of instruction reload should look backward for equivalent register. Increasing values mean more aggressive optimization, making the compile time increase with probably slightly better performance. The default value is 100.</p>
<dt><code>max-cselib-memory-location</code></p>
<dd>The maximum number of memory locations cselib should take into account. Increasing values mean more aggressive optimization, making the compile time increase with probably slightly better performance. The default value is 500.</p>
<dt><code>max-flow-memory-location</code></p>
<dd>Similar as <code>max-cselib-memory-location</code> but for dataflow liveness. The default value is 100.</p>
<dt><code>reorder-blocks-duplicate</code></p>
<dd>
<dt><code>reorder-blocks-duplicate-feedback</code></p>
<dd>Used by basic block reordering pass to decide whether to use unconditional branch or duplicate the code on its destination. Code is duplicated when its estimated size is smaller than this value multiplied by the estimated size of unconditional jump in the hot spots of the program. </p>
<p> The <code>reorder-block-duplicate-feedback</code> is used only when profile feedback is available and may be set to higher values than <code>reorder-block-duplicate</code> since information about the hot spots is more accurate.</p>
<dt><code>max-sched-region-blocks</code></p>
<dd>The maximum number of blocks in a region to be considered for interblock scheduling. The default value is 10.</p>
<dt><code>max-sched-region-insns</code></p>
<dd>The maximum number of insns in a region to be considered for interblock scheduling. The default value is 100.</p>
<dt><code>min-sched-prob</code></p>
<dd>The minimum probability of reaching a source block for interblock speculative scheduling. The default value is 40.</p>
<dt><code>max-last-value-rtl</code></p>
<dd>The maximum size measured as number of RTLs that can be recorded in an expression in combiner for a pseudo register as last known value of that register. The default is 10000.</p>
<dt><code>integer-share-limit</code></p>
<dd>Small integer constants can use a shared data structure, reducing the compiler&#8217;s memory usage and increasing its speed. This sets the maximum value of a shared integer constant&#8217;s. The default value is 256.</p>
<dt><code>min-virtual-mappings</code></p>
<dd>Specifies the minimum number of virtual mappings in the incremental <font SIZE="-1">SSA</font> updater that should be registered to trigger the virtual mappings heuristic defined by virtual-mappings-ratio. The default value is 100.</p>
<dt><code>virtual-mappings-ratio</code></p>
<dd>If the number of virtual mappings is virtual-mappings-ratio bigger than the number of virtual symbols to be updated, then the incremental <font SIZE="-1">SSA</font> updater switches to a full update for those symbols. The default ratio is 3.</p>
<dt><code>ssp-buffer-size</code></p>
<dd>The minimum size of buffers (i.e. arrays) that will receive stack smashing protection when <code>-fstack-protection</code> is used.</p>
<dt><code>max-jump-thread-duplication-stmts</code></p>
<dd>Maximum number of statements allowed in a block that needs to be duplicated when threading jumps.</p>
<dt><code>max-fields-for-field-sensitive</code></p>
<dd>Maximum number of fields in a structure we will treat in a field sensitive manner during pointer analysis.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>Options Controlling the Preprocessor</h2>
<p>These options control the C preprocessor, which is run on each C source file before actual compilation. </p>
<p> If you use the <code>-E</code> option, nothing is done except preprocessing. Some of these options make sense only together with <code>-E</code> because they cause the preprocessor output to be unsuitable for actual compilation. </p>
<dl>
<dd>You can use <code>-Wp,</code><i>option</i> to bypass the compiler driver and pass <i>option</i> directly through to the preprocessor. If <i>option</i> contains commas, it is split into multiple options at the commas. However, many options are modified, translated or interpreted by the compiler driver before being passed to the preprocessor, and <code>-Wp</code> forcibly bypasses this phase. The preprocessor&#8217;s direct interface is undocumented and subject to change, so whenever possible you should avoid using <code>-Wp</code> and let the driver handle the options instead.</dl>
<dl>
<dt><code>-Xpreprocessor</code> <i>option</i></p>
<dd>Pass <i>option</i> as an option to the preprocessor. You can use this to supply system-specific preprocessor options which <font SIZE="-1">GCC</font> does not know how to recognize. </p>
<p> If you want to pass an option that takes an argument, you must use <code>-Xpreprocessor</code> twice, once for the option and once for the argument.</p>
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
<dd>Add the directory <i>dir</i> to the list of directories to be searched for header files. Directories named by <code>-I</code> are searched before the standard system include directories. If the directory <i>dir</i> is a standard system include directory, the option is ignored to ensure that the default search order for system directories and the special treatment of system headers are not defeated .</p>
<dt><code>-o</code> <i>file</i></p>
<dd>Write output to <i>file</i>. This is the same as specifying <i>file</i> as the second non-option argument to <code>cpp</code>. <code>gcc</code> has a different interpretation of a second non-option argument, so you must use <code>-o</code> to specify the output file.</p>
<dt><code>-Wall</code></p>
<dd>Turns on all optional warnings which are desirable for normal code. At present this is <code>-Wcomment</code>, <code>-Wtrigraphs</code>, <code>-Wmultichar</code> and a warning about integer promotion causing a change of sign in <tt>&quot;#if&quot;</tt> expressions. Note that many of the preprocessor&#8217;s warnings are on by default and have no options to control them.</p>
<dt><code>-Wcomment</code></p>
<dd>
<dt><code>-Wcomments</code></p>
<dd>Warn whenever a comment-start sequence <code>/*</code> appears in a <code>/*</code> comment, or whenever a backslash-newline appears in a <code>//</code> comment. (Both forms have the same effect.)</p>
<dt><code>-Wtrigraphs</code></p>
<dd>@anchor{Wtrigraphs} Most trigraphs in comments cannot affect the meaning of the program. However, a trigraph that would form an escaped newline (<code>??/</code> at the end of a line) can, by changing where the comment begins or ends. Therefore, only trigraphs that would form escaped newlines produce warnings inside a comment. </p>
<p> This option is implied by <code>-Wall</code>. If <code>-Wall</code> is not given, this option is still enabled unless trigraphs are enabled. To get trigraph conversion without warnings, but get the other <code>-Wall</code> warnings, use <code>-trigraphs -Wall -Wno-trigraphs</code>.</p>
<dt><code>-Wtraditional</code></p>
<dd>Warn about certain constructs that behave differently in traditional and <font SIZE="-1">ISO</font> C. Also warn about <font SIZE="-1">ISO</font> C constructs that have no traditional C equivalent, and problematic constructs which should be avoided.</p>
<dt><code>-Wimport</code></p>
<dd>Warn the first time <code>#import</code> is used.</p>
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
<dd>Suppress all warnings, including those which <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font> issues by default.</p>
<dt><code>-pedantic</code></p>
<dd>Issue all the mandatory diagnostics listed in the C standard. Some of them are left out by default, since they trigger frequently on harmless code.</p>
<dt><code>-pedantic-errors</code></p>
<dd>Issue all the mandatory diagnostics, and make all mandatory diagnostics into errors. This includes mandatory diagnostics that <font SIZE="-1">GCC</font> issues without <code>-pedantic</code> but treats as warnings.</p>
<dt><code>-M</code></p>
<dd>Instead of outputting the result of preprocessing, output a rule suitable for <code>make</code> describing the dependencies of the main source file. The preprocessor outputs one <code>make</code> rule containing the object file name for that source file, a colon, and the names of all the included files, including those coming from <code>-include</code> or <code>-imacros</code> command line options. </p>
<p> Unless specified explicitly (with <code>-MT</code> or <code>-MQ</code>), the object file name consists of the basename of the source file with any suffix replaced with object file suffix. If there are many included files then the rule is split into several lines using <code>\</code>-newline. The rule has no commands. </p>
<p> This option does not suppress the preprocessor&#8217;s debug output, such as <code>-dM</code>. To avoid mixing such debug output with the dependency rules you should explicitly specify the dependency output file with <code>-MF</code>, or use an environment variable like <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font>. Debug output will still be sent to the regular output stream as normal. </p>
<p> Passing <code>-M</code> to the driver implies <code>-E</code>, and suppresses warnings with an implicit <code>-w</code>.</p>
<dt><code>-MM</code></p>
<dd>Like <code>-M</code> but do not mention header files that are found in system header directories, nor header files that are included, directly or indirectly, from such a header. </p>
<p> This implies that the choice of angle brackets or double quotes in an <code>#include</code> directive does not in itself determine whether that header will appear in <code>-MM</code> dependency output. This is a slight change in semantics from <font SIZE="-1">GCC</font> versions 3.0 and earlier. </p>
<p> @anchor{dashMF}</p>
<dt><code>-MF</code> <i>file</i></p>
<dd>When used with <code>-M</code> or <code>-MM</code>, specifies a file to write the dependencies to. If no <code>-MF</code> switch is given the preprocessor sends the rules to the same place it would have sent preprocessed output. </p>
<p> When used with the driver options <code>-MD</code> or <code>-MMD</code>, <code>-MF</code> overrides the default dependency output file.</p>
<dt><code>-MG</code></p>
<dd>In conjunction with an option such as <code>-M</code> requesting dependency generation, <code>-MG</code> assumes missing header files are generated files and adds them to the dependency list without raising an error. The dependency filename is taken directly from the <tt>&quot;#include&quot;</tt> directive without prepending any path. <code>-MG</code> also suppresses preprocessed output, as a missing header file renders this useless. </p>
<p> This feature is used in automatic updating of makefiles.</p>
<dt><code>-MP</code></p>
<dd>This option instructs <font SIZE="-1">CPP</font> to add a phony target for each dependency other than the main file, causing each to depend on nothing. These dummy rules work around errors <code>make</code> gives if you remove header files without updating the <i>Makefile</i> to match. </p>
<p> This is typical output: </p>
<pre> test.o: test.c test.h</pre>
<pre> test.h:</pre>
<dt><code>-MT</code> <i>target</i></p>
<dd>Change the target of the rule emitted by dependency generation. By default <font SIZE="-1">CPP</font> takes the name of the main input file, including any path, deletes any file suffix such as <code>.c</code>, and appends the platform&#8217;s usual object suffix. The result is the target. </p>
<p> An <code>-MT</code> option will set the target to be exactly the string you specify. If you want multiple targets, you can specify them as a single argument to <code>-MT</code>, or use multiple <code>-MT</code> options. </p>
<p> For example, <code>-MT&nbsp;<wbr>&#8216;$(objpfx)foo.o&#8217;</code> might give </p>
<pre> $(objpfx)foo.o: foo.c</pre>
<dt><code>-MQ</code> <i>target</i></p>
<dd>Same as <code>-MT</code>, but it quotes any characters which are special to Make. <code>-MQ&nbsp;<wbr>&#8216;$(objpfx)foo.o&#8217;</code> gives </p>
<pre> $$(objpfx)foo.o: foo.c</pre>
<p>The default target is automatically quoted, as if it were given with <code>-MQ</code>.</p>
<dt><code>-MD</code></p>
<dd><code>-MD</code> is equivalent to <code>-M -MF</code> <i>file</i>, except that <code>-E</code> is not implied. The driver determines <i>file</i> based on whether an <code>-o</code> option is given. If it is, the driver uses its argument but with a suffix of <i>.d</i>, otherwise it take the basename of the input file and applies a <i>.d</i> suffix. </p>
<p> If <code>-MD</code> is used in conjunction with <code>-E</code>, any <code>-o</code> switch is understood to specify the dependency output file (but <tt>@pxref</tt>{dashMF,,-MF}), but if used without <code>-E</code>, each <code>-o</code> is understood to specify a target object file. </p>
<p> Since <code>-E</code> is not implied, <code>-MD</code> can be used to generate a dependency output file as a side-effect of the compilation process.</p>
<dt><code>-MMD</code></p>
<dd>Like <code>-MD</code> except mention only user header files, not system header files.</p>
<dt><code>-fpch-deps</code></p>
<dd>When using precompiled headers, this flag will cause the dependency-output flags to also list the files from the precompiled header&#8217;s dependencies. If not specified only the precompiled header would be listed and not the files that were used to create it because those files are not consulted when a precompiled header is used.</p>
<dt><code>-fpch-preprocess</code></p>
<dd>This option allows use of a precompiled header together with <code>-E</code>. It inserts a special <tt>&quot;#pragma&quot;</tt>, <tt>&quot;#pragma GCC pch_preprocess &quot;&lt;filename&gt;&quot;&quot;</tt> in the output to mark the place where the precompiled header was found, and its filename. When <code>-fpreprocessed</code> is in use, <font SIZE="-1">GCC</font> recognizes this <tt>&quot;#pragma&quot;</tt> and loads the <font SIZE="-1">PCH</font>. </p>
<p> This option is off by default, because the resulting preprocessed output is only really suitable as input to <font SIZE="-1">GCC</font>. It is switched on by <code>-save-temps</code>. </p>
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
<dl>
<dd>
<dl>
<dt>iso9899:1990</p>
<dd>
<dt>c89</p>
<dd>The <font SIZE="-1">ISO</font> C standard from 1990. <code>c89</code> is the customary shorthand for this version of the standard. </p>
<p> The <code>-ansi</code> option is equivalent to <code>-std=c89</code>.</p>
<dt>iso9899:199409</p>
<dd>The 1990 C standard, as amended in 1994.</p>
<dt>iso9899:1999</p>
<dd>
<dt>c99</p>
<dd>
<dt>iso9899:199x</p>
<dd>
<dt>c9x</p>
<dd>The revised <font SIZE="-1">ISO</font> C standard, published in December 1999. Before publication, this was known as C9X.</p>
<dt>gnu89</p>
<dd>The 1990 C standard plus <font SIZE="-1">GNU</font> extensions. This is the default.</p>
<dt>gnu99</p>
<dd>
<dt>gnu9x</p>
<dd>The 1999 C standard plus <font SIZE="-1">GNU</font> extensions.</p>
<dt>c++98</p>
<dd>The 1998 <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> standard plus amendments.</p>
<dt>gnu++98</p>
<dd>The same as <code>-std=c++98</code> plus <font SIZE="-1">GNU</font> extensions. This is the default for C<font SIZE="-2">++</font> code.</dl>
</dl>
<dl>
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
<dd>Search <i>dir</i> for header files, but do it <i>after</i> all directories specified with <code>-I</code> and the standard system directories have been exhausted. <i>dir</i> is treated as a system include directory.</p>
<dt><code>-iprefix</code> <i>prefix</i></p>
<dd>Specify <i>prefix</i> as the prefix for subsequent <code>-iwithprefix</code> options. If the prefix represents a directory, you should include the final <code>/</code>.</p>
<dt><code>-iwithprefix</code> <i>dir</i></p>
<dd>
<dt><code>-iwithprefixbefore</code> <i>dir</i></p>
<dd>Append <i>dir</i> to the prefix specified previously with <code>-iprefix</code>, and add the resulting directory to the include search path. <code>-iwithprefixbefore</code> puts it in the same place <code>-I</code> would; <code>-iwithprefix</code> puts it where <code>-idirafter</code> would.</p>
<dt><code>-isysroot</code> <i>dir</i></p>
<dd>This option is like the <code>&#8211;sysroot</code> option, but applies only to header files. See the <code>&#8211;sysroot</code> option for more information.</p>
<dt><code>-isystem</code> <i>dir</i></p>
<dd>Search <i>dir</i> for header files, after all directories specified by <code>-I</code> but before the standard system directories. Mark it as a system directory, so that it gets the same special treatment as is applied to the standard system directories.</p>
<dt><code>-iquote</code> <i>dir</i></p>
<dd>Search <i>dir</i> only for header files requested with <tt>&quot;#include&nbsp;<wbr>&quot;</tt>file<tt>&quot;&quot;</tt>; they are not searched for <tt>&quot;#include&nbsp;<wbr>&lt;</tt>file<tt>&gt;&quot;</tt>, before all directories specified by <code>-I</code> and before the standard system directories.</p>
<dt><code>-fdollars-in-identifiers</code></p>
<dd>@anchor{fdollars-in-identifiers} Accept <code>$</code> in identifiers.</p>
<dt><code>-fextended-identifiers</code></p>
<dd>Accept universal character names in identifiers. This option is experimental; in a future version of <font SIZE="-1">GCC</font>, it will be enabled by default for C99 and C<font SIZE="-2">++</font>.</p>
<dt><code>-fpreprocessed</code></p>
<dd>Indicate to the preprocessor that the input file has already been preprocessed. This suppresses things like macro expansion, trigraph conversion, escaped newline splicing, and processing of most directives. The preprocessor still recognizes and removes comments, so that you can pass a file preprocessed with <code>-C</code> to the compiler without problems. In this mode the integrated preprocessor is little more than a tokenizer for the front ends. </p>
<p> <code>-fpreprocessed</code> is implicit if the input file has one of the extensions <code>.i</code>, <code>.ii</code> or <code>.mi</code>. These are the extensions that <font SIZE="-1">GCC</font> uses for preprocessed files created by <code>-save-temps</code>.</p>
<dt><code>-ftabstop=</code><i>width</i></p>
<dd>Set the distance between tab stops. This helps the preprocessor report correct column numbers in warnings or errors, even if tabs appear on the line. If the value is less than 1 or greater than 100, the option is ignored. The default is 8.</p>
<dt><code>-fexec-charset=</code><i>charset</i></p>
<dd>Set the execution character set, used for string and character constants. The default is <font SIZE="-1">UTF-8</font>. <i>charset</i> can be any encoding supported by the system&#8217;s <tt>&quot;iconv&quot;</tt> library routine.</p>
<dt><code>-fwide-exec-charset=</code><i>charset</i></p>
<dd>Set the wide execution character set, used for wide string and character constants. The default is <font SIZE="-1">UTF-32</font> or <font SIZE="-1">UTF-16</font>, whichever corresponds to the width of <tt>&quot;wchar_t&quot;</tt>. As with <code>-fexec-charset</code>, <i>charset</i> can be any encoding supported by the system&#8217;s <tt>&quot;iconv&quot;</tt> library routine; however, you will have problems with encodings that do not fit exactly in <tt>&quot;wchar_t&quot;</tt>.</p>
<dt><code>-finput-charset=</code><i>charset</i></p>
<dd>Set the input character set, used for translation from the character set of the input file to the source character set used by <font SIZE="-1">GCC</font>. If the locale does not specify, or <font SIZE="-1">GCC</font> cannot get this information from the locale, the default is <font SIZE="-1">UTF-8</font>. This can be overridden by either the locale or this command line option. Currently the command line option takes precedence if there&#8217;s a conflict. <i>charset</i> can be any encoding supported by the system&#8217;s <tt>&quot;iconv&quot;</tt> library routine.</p>
<dt><code>-fworking-directory</code></p>
<dd>Enable generation of linemarkers in the preprocessor output that will let the compiler know the current working directory at the time of preprocessing. When this option is enabled, the preprocessor will emit, after the initial linemarker, a second linemarker with the current working directory followed by two slashes. <font SIZE="-1">GCC</font> will use this directory, when it&#8217;s present in the preprocessed input, as the directory emitted as the current working directory in some debugging information formats. This option is implicitly enabled if debugging information is enabled, but this can be inhibited with the negated form <code>-fno-working-directory</code>. If the <code>-P</code> flag is present in the command line, this option has no effect, since no <tt>&quot;#line&quot;</tt> directives are emitted whatsoever.</p>
<dt><code>-fno-show-column</code></p>
<dd>Do not print column numbers in diagnostics. This may be necessary if diagnostics are being scanned by a program that does not understand the column numbers, such as <code>dejagnu</code>.</p>
<dt><code>-A</code> <i>predicate</i><code>=</code><i>answer</i></p>
<dd>Make an assertion with the predicate <i>predicate</i> and answer <i>answer</i>. This form is preferred to the older form <code>-A</code> <i>predicate</i><code>(</code><i>answer</i><code>)</code>, which is still supported, because it does not use shell special characters.</p>
<dt><code>-A &#8211;</code><i>predicate</i><code>=</code><i>answer</i></p>
<dd>Cancel an assertion with the predicate <i>predicate</i> and answer <i>answer</i>.</p>
<dt><code>-dCHARS</code></p>
<dd><i></i><font SIZE="-1"><i>CHARS</i></font><i></i> is a sequence of one or more of the following characters, and must not be preceded by a space. Other characters are interpreted by the compiler proper, or reserved for future versions of <font SIZE="-1">GCC</font>, and so are silently ignored. If you specify characters whose behavior conflicts, the result is undefined.</p>
<dl>
<dd>
<dl>
<dt><code>M</code></p>
<dd>Instead of the normal output, generate a list of <code>#define</code> directives for all the macros defined during the execution of the preprocessor, including predefined macros. This gives you a way of finding out what is predefined in your version of the preprocessor. Assuming you have no file <i>foo.h</i>, the command </p>
<pre> touch foo.h; cpp -dM foo.h</pre>
<p>will show all the predefined macros.</p>
<dt><code>D</code></p>
<dd>Like <code>M</code> except in two respects: it does <i>not</i> include the predefined macros, and it outputs <i>both</i> the <code>#define</code> directives and the result of preprocessing. Both kinds of output go to the standard output file.</p>
<dt><code>N</code></p>
<dd>Like <code>D</code>, but emit only the macro names, not their expansions.</p>
<dt><code>I</code></p>
<dd>Output <code>#include</code> directives in addition to the result of preprocessing.</dl>
</dl>
<dl>
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
<dd>Try to imitate the behavior of old-fashioned C preprocessors, as opposed to <font SIZE="-1">ISO</font> C preprocessors.</p>
<dt><code>-trigraphs</code></p>
<dd>Process trigraph sequences. These are three-character sequences, all starting with <code>??</code>, that are defined by <font SIZE="-1">ISO</font> C to stand for single characters. For example, <code>??/</code> stands for <code>\</code>, so <code>&#8216;??/n&#8217;</code> is a character constant for a newline. By default, <font SIZE="-1">GCC</font> ignores trigraphs, but in standard-conforming modes it converts them. See the <code>-std</code> and <code>-ansi</code> options. </p>
<p> The nine trigraphs and their replacements are </p>
<pre> Trigraph: ??( ??) ??&lt; ??&gt; ??= ??/ ??' ??! ??-
 Replacement: [ ] { } # \ ^ | ~</pre>
<dt><code>-remap</code></p>
<dd>Enable special code to work around file systems which only permit very short file names, such as <font SIZE="-1">MS-DOS</font>.</p>
<dt><code>&#8211;help</code></p>
<dd>
<dt><code>&#8211;target-help</code></p>
<dd>Print text describing all the command line options instead of preprocessing anything.</p>
<dt><code>-v</code></p>
<dd>Verbose mode. Print out <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font>&#8216;s version number at the beginning of execution, and report the final form of the include path.</p>
<dt><code>-H</code></p>
<dd>Print the name of each header file used, in addition to other normal activities. Each name is indented to show how deep in the <code>#include</code> stack it is. Precompiled header files are also printed, even if they are found to be invalid; an invalid precompiled header file is printed with <code>&#8230;x</code> and a valid one with <code>&#8230;!</code> .</p>
<dt><code>-version</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Print out <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font>&#8216;s version number. With one dash, proceed to preprocess as normal. With two dashes, exit immediately.</dl>
<h2>Passing Options to the Assembler</h2>
<p>You can pass options to the assembler.</p>
<dl>
<dt><code>-Wa,</code><i>option</i></p>
<dd>Pass <i>option</i> as an option to the assembler. If <i>option</i> contains commas, it is split into multiple options at the commas.</p>
<dt><code>-Xassembler</code> <i>option</i></p>
<dd>Pass <i>option</i> as an option to the assembler. You can use this to supply system-specific assembler options which <font SIZE="-1">GCC</font> does not know how to recognize. </p>
<p> If you want to pass an option that takes an argument, you must use <code>-Xassembler</code> twice, once for the option and once for the argument.</dl>
<h2>Options for Linking</h2>
<p>These options come into play when the compiler links object files into an executable output file. They are meaningless if the compiler is not doing a link step.</p>
<dl>
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
<dd>Do not use the standard system libraries when linking. Only the libraries you specify will be passed to the linker. The standard startup files are used normally, unless <code>-nostartfiles</code> is used. The compiler may generate calls to <tt>&quot;memcmp&quot;</tt>, <tt>&quot;memset&quot;</tt>, <tt>&quot;memcpy&quot;</tt> and <tt>&quot;memmove&quot;</tt>. These entries are usually resolved by entries in libc. These entry points should be supplied through some other mechanism when this option is specified.</p>
<dt><code>-nostdlib</code></p>
<dd>Do not use the standard system startup files or libraries when linking. No startup files and only the libraries you specify will be passed to the linker. The compiler may generate calls to <tt>&quot;memcmp&quot;</tt>, <tt>&quot;memset&quot;</tt>, <tt>&quot;memcpy&quot;</tt> and <tt>&quot;memmove&quot;</tt>. These entries are usually resolved by entries in libc. These entry points should be supplied through some other mechanism when this option is specified. </p>
<p> One of the standard libraries bypassed by <code>-nostdlib</code> and <code>-nodefaultlibs</code> is <i>libgcc.a</i>, a library of internal subroutines that <font SIZE="-1">GCC</font> uses to overcome shortcomings of particular machines, or special needs for some languages. </p>
<p> In most cases, you need <i>libgcc.a</i> even when you want to avoid other standard libraries. In other words, when you specify <code>-nostdlib</code> or <code>-nodefaultlibs</code> you should usually specify <code>-lgcc</code> as well. This ensures that you have no unresolved references to internal <font SIZE="-1">GCC</font> library subroutines. (For example, <code>__main</code>, used to ensure C<font SIZE="-2">++</font> constructors will be called.)</p>
<dt><code>-pie</code></p>
<dd>Produce a position independent executable on targets which support it. For predictable results, you must also specify the same set of options that were used to generate code (<code>-fpie</code>, <code>-fPIE</code>, or model suboptions) when you specify this option.</p>
<dt><code>-rdynamic</code></p>
<dd>Pass the flag <code>-export-dynamic</code> to the <font SIZE="-1">ELF</font> linker, on targets that support it. This instructs the linker to add all symbols, not only used ones, to the dynamic symbol table. This option is needed for some uses of <tt>&quot;dlopen&quot;</tt> or to allow obtaining backtraces from within a program.</p>
<dt><code>-s</code></p>
<dd>Remove all symbol table and relocation information from the executable.</p>
<dt><code>-static</code></p>
<dd>On systems that support dynamic linking, this prevents linking with the shared libraries. On other systems, this option has no effect.</p>
<dt><code>-shared</code></p>
<dd>Produce a shared object which can then be linked with other objects to form an executable. Not all systems support this option. For predictable results, you must also specify the same set of options that were used to generate code (<code>-fpic</code>, <code>-fPIC</code>, or model suboptions) when you specify this option.[1]</p>
<dt><code>-shared-libgcc</code></p>
<dd>
<dt><code>-static-libgcc</code></p>
<dd>On systems that provide <i>libgcc</i> as a shared library, these options force the use of either the shared or static version respectively. If no shared version of <i>libgcc</i> was built when the compiler was configured, these options have no effect. </p>
<p> There are several situations in which an application should use the shared <i>libgcc</i> instead of the static version. The most common of these is when the application wishes to throw and catch exceptions across different shared libraries. In that case, each of the libraries as well as the application itself should use the shared <i>libgcc</i>. </p>
<p> Therefore, the G++ and <font SIZE="-1">GCJ</font> drivers automatically add <code>-shared-libgcc</code> whenever you build a shared library or a main executable, because C<font SIZE="-2">++</font> and Java programs typically use exceptions, so this is the right thing to do. </p>
<p> If, instead, you use the <font SIZE="-1">GCC</font> driver to create shared libraries, you may find that they will not always be linked with the shared <i>libgcc</i>. If <font SIZE="-1">GCC</font> finds, at its configuration time, that you have a non-GNU linker or a <font SIZE="-1">GNU</font> linker that does not support option <code>&#8211;eh-frame-hdr</code>, it will link the shared version of <i>libgcc</i> into shared libraries by default. Otherwise, it will take advantage of the linker and optimize away the linking with the shared version of <i>libgcc</i>, linking with the static version of libgcc by default. This allows exceptions to propagate through such shared libraries, without incurring relocation costs at library load time. </p>
<p> However, if a library or main executable is supposed to throw or catch exceptions, you must link it using the G++ or <font SIZE="-1">GCJ</font> driver, as appropriate for the languages used in the program, or using the option <code>-shared-libgcc</code>, such that it is linked with the shared <i>libgcc</i>.</p>
<dt><code>-symbolic</code></p>
<dd>Bind references to global symbols when building a shared object. Warn about any unresolved references (unless overridden by the link editor option <code>-Xlinker -z -Xlinker defs</code>). Only a few systems support this option.</p>
<dt><code>-Xlinker</code> <i>option</i></p>
<dd>Pass <i>option</i> as an option to the linker. You can use this to supply system-specific linker options which <font SIZE="-1">GCC</font> does not know how to recognize. </p>
<p> If you want to pass an option that takes an argument, you must use <code>-Xlinker</code> twice, once for the option and once for the argument. For example, to pass <code>-assert definitions</code>, you must write <code>-Xlinker -assert -Xlinker definitions</code>. It does not work to write <code>-Xlinker &#8220;-assert definitions&#8221;</code>, because this passes the entire string as a single argument, which is not what the linker expects.</p>
<dt><code>-Wl,</code><i>option</i></p>
<dd>Pass <i>option</i> as an option to the linker. If <i>option</i> contains commas, it is split into multiple options at the commas.</p>
<dt><code>-u</code> <i>symbol</i></p>
<dd>Pretend the symbol <i>symbol</i> is undefined, to force linking of library modules to define it. You can use <code>-u</code> multiple times with different symbols to force loading of additional library modules.</dl>
<h2>Options for Directory Search</h2>
<p>These options specify directories to search for header files, for libraries and for parts of the compiler:</p>
<dl>
<dt><code>-I</code><i>dir</i></p>
<dd>Add the directory <i>dir</i> to the head of the list of directories to be searched for header files. This can be used to override a system header file, substituting your own version, since these directories are searched before the system header file directories. However, you should not use this option to add directories that contain vendor-supplied system header files (use <code>-isystem</code> for that). If you use more than one <code>-I</code> option, the directories are scanned in left-to-right order; the standard system directories come after. </p>
<p> If a standard system include directory, or a directory specified with <code>-isystem</code>, is also specified with <code>-I</code>, the <code>-I</code> option will be ignored. The directory will still be searched but as a system directory at its normal position in the system include chain. This is to ensure that <font SIZE="-1">GCC</font>&#8216;s procedure to fix buggy system headers and the ordering for the include_next directive are not inadvertently changed. If you really need to change the search order for system directories, use the <code>-nostdinc</code> and/or <code>-isystem</code> options.</p>
<dt><code>-iquote</code><i>dir</i></p>
<dd>Add the directory <i>dir</i> to the head of the list of directories to be searched for header files only for the case of <code>#include &quot;</code><i>file</i><code>&quot;</code>; they are not searched for <code>#include &lt;</code><i>file</i><code>&gt;</code>, otherwise just like <code>-I</code>.</p>
<dt><code>-L</code><i>dir</i></p>
<dd>Add directory <i>dir</i> to the list of directories to be searched for <code>-l</code>.</p>
<dt><code>-B</code><i>prefix</i></p>
<dd>This option specifies where to find the executables, libraries, include files, and data files of the compiler itself. </p>
<p> The compiler driver program runs one or more of the subprograms <i>cpp</i>, <i>cc1</i>, <i>as</i> and <i>ld</i>. It tries <i>prefix</i> as a prefix for each program it tries to run, both with and without <i>machine</i><code>/</code><i>version</i><code>/</code>. </p>
<p> For each subprogram to be run, the compiler driver first tries the <code>-B</code> prefix, if any. If that name is not found, or if <code>-B</code> was not specified, the driver tries two standard prefixes, which are <i>/usr/lib/gcc/</i> and <i>/usr/local/lib/gcc/</i>. If neither of those results in a file name that is found, the unmodified program name is searched for using the directories specified in your <font SIZE="-1"><code>PATH</code></font> environment variable. </p>
<p> The compiler will check to see if the path provided by the <code>-B</code> refers to a directory, and if necessary it will add a directory separator character at the end of the path. </p>
<p> <code>-B</code> prefixes that effectively specify directory names also apply to libraries in the linker, because the compiler translates these options into <code>-L</code> options for the linker. They also apply to includes files in the preprocessor, because the compiler translates these options into <code>-isystem</code> options for the preprocessor. In this case, the compiler appends <code>include</code> to the prefix. </p>
<p> The run-time support file <i>libgcc.a</i> can also be searched for using the <code>-B</code> prefix, if needed. If it is not found there, the two standard prefixes above are tried, and that is all. The file is left out of the link if it is not found by those means. </p>
<p> Another way to specify a prefix much like the <code>-B</code> prefix is to use the environment variable <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. </p>
<p> As a special kludge, if the path provided by <code>-B</code> is <i>[dir/]stageN/</i>, where <i>N</i> is a number in the range 0 to 9, then it will be replaced by <i>[dir/]include</i>. This is to help with boot-strapping the compiler.</p>
<dt><code>-specs=</code><i>file</i></p>
<dd>Process <i>file</i> after the compiler reads in the standard <i>specs</i> file, in order to override the defaults that the <i>gcc</i> driver program uses when determining what switches to pass to <i>cc1</i>, <i>cc1plus</i>, <i>as</i>, <i>ld</i>, etc. More than one <code>-specs=</code><i>file</i> can be specified on the command line, and they are processed in order, from left to right.</p>
<dt><code>&#8211;sysroot=</code><i>dir</i></p>
<dd>Use <i>dir</i> as the logical root directory for headers and libraries. For example, if the compiler would normally search for headers in <i>/usr/include</i> and libraries in <i>/usr/lib</i>, it will instead search <i>dir/usr/include</i> and <i>dir/usr/lib</i>. </p>
<p> If you use both this option and the <code>-isysroot</code> option, then the <code>&#8211;sysroot</code> option will apply to libraries, but the <code>-isysroot</code> option will apply to header files. </p>
<p> The <font SIZE="-1">GNU</font> linker (beginning with version 2.16) has the necessary support for this option. If your linker does not support this option, the header file aspect of <code>&#8211;sysroot</code> will still work, but the library aspect will not.</p>
<dt><code>-I-</code></p>
<dd>This option has been deprecated. Please use <code>-iquote</code> instead for <code>-I</code> directories before the <code>-I-</code> and remove the <code>-I-</code>. Any directories you specify with <code>-I</code> options before the <code>-I-</code> option are searched only for the case of <code>#include &quot;</code><i>file</i><code>&quot;</code>; they are not searched for <code>#include &lt;</code><i>file</i><code>&gt;</code>. </p>
<p> If additional directories are specified with <code>-I</code> options after the <code>-I-</code>, these directories are searched for all <code>#include</code> directives. (Ordinarily <i>all</i> <code>-I</code> directories are used this way.) </p>
<p> In addition, the <code>-I-</code> option inhibits the use of the current directory (where the current input file came from) as the first search directory for <code>#include &quot;</code><i>file</i><code>&quot;</code>. There is no way to override this effect of <code>-I-</code>. With <code>-I.</code> you can specify searching the directory which was current when the compiler was invoked. That is not exactly the same as what the preprocessor does by default, but it is often satisfactory. </p>
<p> <code>-I-</code> does not inhibit the use of the standard system directories for header files. Thus, <code>-I-</code> and <code>-nostdinc</code> are independent.</dl>
<h2>Specifying Target Machine and Compiler Version</h2>
<p>The usual way to run <font SIZE="-1">GCC</font> is to run the executable called <i>gcc</i>, or <i>&lt;machine&gt;-gcc</i> when cross-compiling, or <i>&lt;machine&gt;-gcc-&lt;version&gt;</i> to run a version other than the one that was installed last. Sometimes this is inconvenient, so <font SIZE="-1">GCC</font> provides options that will switch to another cross-compiler or version.</p>
<dl>
<dt><code>-b</code> <i>machine</i></p>
<dd>The argument <i>machine</i> specifies the target machine for compilation. </p>
<p> The value to use for <i>machine</i> is the same as was specified as the machine type when configuring <font SIZE="-1">GCC</font> as a cross-compiler. For example, if a cross-compiler was configured with <code>configure arm-elf</code>, meaning to compile for an arm processor with elf binaries, then you would specify <code>-b arm-elf</code> to run that cross compiler. Because there are other options beginning with <code>-b</code>, the configuration must contain a hyphen.</p>
<dt><code>-V</code> <i>version</i></p>
<dd>The argument <i>version</i> specifies which version of <font SIZE="-1">GCC</font> to run. This is useful when multiple versions are installed. For example, <i>version</i> might be <code>4.0</code>, meaning to run <font SIZE="-1">GCC</font> version 4.0.</dl>
<p> The <code>-V</code> and <code>-b</code> options work by running the <i>&lt;machine&gt;-gcc-&lt;version&gt;</i> executable, so there&#8217;s no real reason to use them if you can just run that directly.</p>
<h2>Hardware Models and Configurations</h2>
<p>Earlier we discussed the standard option <code>-b</code> which chooses among different installed compilers for completely different target machines, such as <font SIZE="-1">VAX</font> vs. 68000 vs. 80386. </p>
<p> In addition, each of these target machine types can have its own special options, starting with <code>-m</code>, to choose among various hardware models or configurations&#8212;for example, 68010 vs 68020, floating coprocessor or none. A single installed version of the compiler can compile for any model or configuration, according to the options specified. </p>
<p> Some configurations of the compiler also support additional special options, usually for compatibility with other compilers on the same platform. </p>
<p> <i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i> </p>
<p> These options are defined for <font SIZE="-1">ARC</font> implementations:</p>
<dl>
<dt><code>-EL</code></p>
<dd>Compile code for little endian mode. This is the default.</p>
<dt><code>-EB</code></p>
<dd>Compile code for big endian mode.</p>
<dt><code>-mmangle-cpu</code></p>
<dd>Prepend the name of the cpu to all public symbol names. In multiple-processor systems, there are many <font SIZE="-1">ARC</font> variants with different instruction and register set characteristics. This flag prevents code compiled for one cpu to be linked with code compiled for another. No facility exists for handling variants that are &#8220;almost identical&#8221;. This is an all or nothing option.</p>
<dt><code>-mcpu=</code><i>cpu</i></p>
<dd>Compile code for <font SIZE="-1">ARC</font> variant <i>cpu</i>. Which variants are supported depend on the configuration. All variants support <code>-mcpu=base</code>, this is the default.</p>
<dt><code>-mtext=</code><i>text-section</i></p>
<dd>
<dt><code>-mdata=</code><i>data-section</i></p>
<dd>
<dt><code>-mrodata=</code><i>readonly-data-section</i></p>
<dd>Put functions, data, and readonly data in <i>text-section</i>, <i>data-section</i>, and <i>readonly-data-section</i> respectively by default. This can be overridden with the <tt>&quot;section&quot;</tt> attribute.</dl>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for Advanced <font SIZE="-1">RISC</font> Machines (<font SIZE="-1">ARM</font>) architectures:</p>
<dl>
<dt><code>-mabi=</code><i>name</i></p>
<dd>Generate code for the specified <font SIZE="-1">ABI</font>. Permissible values are: <code>apcs-gnu</code>, <code>atpcs</code>, <code>aapcs</code>, <code>aapcs-linux</code> and <code>iwmmxt</code>.</p>
<dt><code>-mapcs-frame</code></p>
<dd>Generate a stack frame that is compliant with the <font SIZE="-1">ARM</font> Procedure Call Standard for all functions, even if this is not strictly necessary for correct execution of the code. Specifying <code>-fomit-frame-pointer</code> with this option will cause the stack frames not to be generated for leaf functions. The default is <code>-mno-apcs-frame</code>.</p>
<dt><code>-mapcs</code></p>
<dd>This is a synonym for <code>-mapcs-frame</code>.</p>
<dt><code>-mthumb-interwork</code></p>
<dd>Generate code which supports calling between the <font SIZE="-1">ARM</font> and Thumb instruction sets. Without this option the two instruction sets cannot be reliably used inside one program. The default is <code>-mno-thumb-interwork</code>, since slightly larger code is generated when <code>-mthumb-interwork</code> is specified.</p>
<dt><code>-mno-sched-prolog</code></p>
<dd>Prevent the reordering of instructions in the function prolog, or the merging of those instruction with the instructions in the function&#8217;s body. This means that all functions will start with a recognizable set of instructions (or in fact one of a choice from a small set of different function prologues), and this information can be used to locate the start if functions inside an executable piece of code. The default is <code>-msched-prolog</code>.</p>
<dt><code>-mhard-float</code></p>
<dd>Generate output containing floating point instructions. This is the default.</p>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">ARM</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC</font>, with <code>-msoft-float</code> in order for this to work.</p>
<dt><code>-mfloat-abi=</code><i>name</i></p>
<dd>Specifies which <font SIZE="-1">ABI</font> to use for floating point values. Permissible values are: <code>soft</code>, <code>softfp</code> and <code>hard</code>. </p>
<p> <code>soft</code> and <code>hard</code> are equivalent to <code>-msoft-float</code> and <code>-mhard-float</code> respectively. <code>softfp</code> allows the generation of floating point instructions, but still uses the soft-float calling conventions.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a processor running in little-endian mode. This is the default for all standard configurations.</p>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a processor running in big-endian mode; the default is to compile code for a little-endian processor.</p>
<dt><code>-mwords-little-endian</code></p>
<dd>This option only applies when generating code for big-endian processors. Generate code for a little-endian word order but a big-endian byte order. That is, a byte order of the form <code>32107654</code>. Note: this option should only be used if you require compatibility with code for big-endian <font SIZE="-1">ARM</font> processors generated by versions of the compiler prior to 2.8.</p>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>This specifies the name of the target <font SIZE="-1">ARM</font> processor. <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. Permissible names are: <code>arm2</code>, <code>arm250</code>, <code>arm3</code>, <code>arm6</code>, <code>arm60</code>, <code>arm600</code>, <code>arm610</code>, <code>arm620</code>, <code>arm7</code>, <code>arm7m</code>, <code>arm7d</code>, <code>arm7dm</code>, <code>arm7di</code>, <code>arm7dmi</code>, <code>arm70</code>, <code>arm700</code>, <code>arm700i</code>, <code>arm710</code>, <code>arm710c</code>, <code>arm7100</code>, <code>arm7500</code>, <code>arm7500fe</code>, <code>arm7tdmi</code>, <code>arm7tdmi-s</code>, <code>arm8</code>, <code>strongarm</code>, <code>strongarm110</code>, <code>strongarm1100</code>, <code>arm8</code>, <code>arm810</code>, <code>arm9</code>, <code>arm9e</code>, <code>arm920</code>, <code>arm920t</code>, <code>arm922t</code>, <code>arm946e-s</code>, <code>arm966e-s</code>, <code>arm968e-s</code>, <code>arm926ej-s</code>, <code>arm940t</code>, <code>arm9tdmi</code>, <code>arm10tdmi</code>, <code>arm1020t</code>, <code>arm1026ej-s</code>, <code>arm10e</code>, <code>arm1020e</code>, <code>arm1022e</code>, <code>arm1136j-s</code>, <code>arm1136jf-s</code>, <code>mpcore</code>, <code>mpcorenovfp</code>, <code>arm1176jz-s</code>, <code>arm1176jzf-s</code>, <code>xscale</code>, <code>iwmmxt</code>, <code>ep9312</code>.</p>
<dt><code>-mtune=</code><i>name</i></p>
<dd>This option is very similar to the <code>-mcpu=</code> option, except that instead of specifying the actual target processor type, and hence restricting which instructions can be used, it specifies that <font SIZE="-1">GCC</font> should tune the performance of the code as if the target were of the type specified in this option, but still choosing the instructions that it will generate based on the cpu specified by a <code>-mcpu=</code> option. For some <font SIZE="-1">ARM</font> implementations better performance can be obtained by using this option.</p>
<dt><code>-march=</code><i>name</i></p>
<dd>This specifies the name of the target <font SIZE="-1">ARM</font> architecture. <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. This option can be used in conjunction with or instead of the <code>-mcpu=</code> option. Permissible names are: <code>armv2</code>, <code>armv2a</code>, <code>armv3</code>, <code>armv3m</code>, <code>armv4</code>, <code>armv4t</code>, <code>armv5</code>, <code>armv5t</code>, <code>armv5te</code>, <code>armv6</code>, <code>armv6j</code>, <code>iwmmxt</code>, <code>ep9312</code>.</p>
<dt><code>-mfpu=</code><i>name</i></p>
<dd>
<dt><code>-mfpe=</code><i>number</i></p>
<dd>
<dt><code>-mfp=</code><i>number</i></p>
<dd>This specifies what floating point hardware (or hardware emulation) is available on the target. Permissible names are: <code>fpa</code>, <code>fpe2</code>, <code>fpe3</code>, <code>maverick</code>, <code>vfp</code>. <code>-mfp</code> and <code>-mfpe</code> are synonyms for <code>-mfpu</code>=<code>fpe</code><i>number</i>, for compatibility with older versions of <font SIZE="-1">GCC</font>. </p>
<p> If <code>-msoft-float</code> is specified this specifies the format of floating point values.</p>
<dt><code>-mstructure-size-boundary=</code><i>n</i></p>
<dd>The size of all structures and unions will be rounded up to a multiple of the number of bits set by this option. Permissible values are 8, 32 and 64. The default value varies for different toolchains. For the <font SIZE="-1">COFF</font> targeted toolchain the default value is 8. A value of 64 is only allowed if the underlying <font SIZE="-1">ABI</font> supports it. </p>
<p> Specifying the larger number can produce faster, more efficient code, but can also increase the size of the program. Different values are potentially incompatible. Code compiled with one value cannot necessarily expect to work with code or libraries compiled with another value, if they exchange information using structures or unions.</p>
<dt><code>-mabort-on-noreturn</code></p>
<dd>Generate a call to the function <tt>&quot;abort&quot;</tt> at the end of a <tt>&quot;noreturn&quot;</tt> function. It will be executed if the function tries to return.</p>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Tells the compiler to perform function calls by first loading the address of the function into a register and then performing a subroutine call on this register. This switch is needed if the target function will lie outside of the 64 megabyte addressing range of the offset based version of subroutine call instruction. </p>
<p> Even if this switch is enabled, not all function calls will be turned into long calls. The heuristic is that static functions, functions which have the <code>short-call</code> attribute, functions that are inside the scope of a <code>#pragma no_long_calls</code> directive and functions whose definitions have already been compiled within the current compilation unit, will not be turned into long calls. The exception to this rule is that weak function definitions, functions with the <code>long-call</code> attribute or the <code>section</code> attribute, and functions that are within the scope of a <code>#pragma long_calls</code> directive, will always be turned into long calls. </p>
<p> This feature is not enabled by default. Specifying <code>-mno-long-calls</code> will restore the default behavior, as will placing the function calls within the scope of a <code>#pragma long_calls_off</code> directive. Note these switches have no effect on how the compiler generates code to handle function calls via function pointers.</p>
<dt><code>-mnop-fun-dllimport</code></p>
<dd>Disable support for the <tt>&quot;dllimport&quot;</tt> attribute.</p>
<dt><code>-msingle-pic-base</code></p>
<dd>Treat the register used for <font SIZE="-1">PIC</font> addressing as read-only, rather than loading it in the prologue for each function. The run-time system is responsible for initializing this register with an appropriate value before execution begins.</p>
<dt><code>-mpic-register=</code><i>reg</i></p>
<dd>Specify the register to be used for <font SIZE="-1">PIC</font> addressing. The default is R10 unless stack-checking is enabled, when R9 is used.</p>
<dt><code>-mcirrus-fix-invalid-insns</code></p>
<dd>Insert NOPs into the instruction stream to in order to work around problems with invalid Maverick instruction combinations. This option is only valid if the <code>-mcpu=ep9312</code> option has been used to enable generation of instructions for the Cirrus Maverick floating point co-processor. This option is not enabled by default, since the problem is only present in older Maverick implementations. The default can be re-enabled by use of the <code>-mno-cirrus-fix-invalid-insns</code> switch.</p>
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
<dd>Generate code for the 16-bit Thumb instruction set. The default is to use the 32-bit <font SIZE="-1">ARM</font> instruction set.</p>
<dt><code>-mtpcs-frame</code></p>
<dd>Generate a stack frame that is compliant with the Thumb Procedure Call Standard for all non-leaf functions. (A leaf function is one that does not call any other functions.) The default is <code>-mno-tpcs-frame</code>.</p>
<dt><code>-mtpcs-leaf-frame</code></p>
<dd>Generate a stack frame that is compliant with the Thumb Procedure Call Standard for all leaf functions. (A leaf function is one that does not call any other functions.) The default is <code>-mno-apcs-leaf-frame</code>.</p>
<dt><code>-mcallee-super-interworking</code></p>
<dd>Gives all externally visible functions in the file being compiled an <font SIZE="-1">ARM</font> instruction set header which switches to Thumb mode before executing the rest of the function. This allows these functions to be called from non-interworking code.</p>
<dt><code>-mcaller-super-interworking</code></p>
<dd>Allows calls via function pointers (including virtual functions) to execute correctly regardless of whether the target code has been compiled for interworking or not. There is a small overhead in the cost of executing a function pointer if this option is enabled.</p>
<dt><code>-mtp=</code><i>name</i></p>
<dd>Specify the access model for the thread local storage pointer. The valid models are <code>soft</code>, which generates calls to <tt>&quot;__aeabi_read_tp&quot;</tt>, <code>cp15</code>, which fetches the thread pointer from <tt>&quot;cp15&quot;</tt> directly (supported in the arm6k architecture), and <code>auto</code>, which uses the best available method for the selected processor. The default setting is <code>auto</code>.</dl>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i> </p>
<p> These options are defined for <font SIZE="-1">AVR</font> implementations:</p>
<dl>
<dt><code>-mmcu=</code><i>mcu</i></p>
<dd>Specify <font SIZE="-1">ATMEL</font> <font SIZE="-1">AVR</font> instruction set or <font SIZE="-1">MCU</font> type. </p>
<p> Instruction set avr1 is for the minimal <font SIZE="-1">AVR</font> core, not supported by the C compiler, only for assembler programs (<font SIZE="-1">MCU</font> types: at90s1200, attiny10, attiny11, attiny12, attiny15, attiny28). </p>
<p> Instruction set avr2 (default) is for the classic <font SIZE="-1">AVR</font> core with up to 8K program memory space (<font SIZE="-1">MCU</font> types: at90s2313, at90s2323, attiny22, at90s2333, at90s2343, at90s4414, at90s4433, at90s4434, at90s8515, at90c8534, at90s8535). </p>
<p> Instruction set avr3 is for the classic <font SIZE="-1">AVR</font> core with up to 128K program memory space (<font SIZE="-1">MCU</font> types: atmega103, atmega603, at43usb320, at76c711). </p>
<p> Instruction set avr4 is for the enhanced <font SIZE="-1">AVR</font> core with up to 8K program memory space (<font SIZE="-1">MCU</font> types: atmega8, atmega83, atmega85). </p>
<p> Instruction set avr5 is for the enhanced <font SIZE="-1">AVR</font> core with up to 128K program memory space (<font SIZE="-1">MCU</font> types: atmega16, atmega161, atmega163, atmega32, atmega323, atmega64, atmega128, at43usb355, at94k).</p>
<dt><code>-msize</code></p>
<dd>Output instruction sizes to the asm file.</p>
<dt><code>-minit-stack=</code><i>N</i></p>
<dd>Specify the initial stack address, which may be a symbol or numeric value, <code>__stack</code> is the default.</p>
<dt><code>-mno-interrupts</code></p>
<dd>Generated code is not compatible with hardware interrupts. Code size will be smaller.</p>
<dt><code>-mcall-prologues</code></p>
<dd>Functions prologues/epilogues expanded as call to appropriate subroutines. Code size will be smaller.</p>
<dt><code>-mno-tablejump</code></p>
<dd>Do not generate tablejump insns which sometimes increase code size.</p>
<dt><code>-mtiny-stack</code></p>
<dd>Change only the low 8 bits of the stack pointer.</p>
<dt><code>-mint8</code></p>
<dd>Assume int to be 8 bit integer. This affects the sizes of all types: A char will be 1 byte, an int will be 1 byte, an long will be 2 bytes and long long will be 4 bytes. Please note that this option does not comply to the C standards, but it will provide you with smaller code size.</dl>
<p> <i>Blackfin Options</i></p>
<dl>
<dt><code>-momit-leaf-frame-pointer</code></p>
<dd>Don&#8217;t keep the frame pointer in a register for leaf functions. This avoids the instructions to save, set up and restore frame pointers and makes an extra register available in leaf functions. The option <code>-fomit-frame-pointer</code> removes the frame pointer for all functions which might make debugging harder.</p>
<dt><code>-mspecld-anomaly</code></p>
<dd>When enabled, the compiler will ensure that the generated code does not contain speculative loads after jump instructions. This option is enabled by default.</p>
<dt><code>-mno-specld-anomaly</code></p>
<dd>Don&#8217;t generate extra code to prevent speculative loads from occurring.</p>
<dt><code>-mcsync-anomaly</code></p>
<dd>When enabled, the compiler will ensure that the generated code does not contain <font SIZE="-1">CSYNC</font> or <font SIZE="-1">SSYNC</font> instructions too soon after conditional branches. This option is enabled by default.</p>
<dt><code>-mno-csync-anomaly</code></p>
<dd>Don&#8217;t generate extra code to prevent <font SIZE="-1">CSYNC</font> or <font SIZE="-1">SSYNC</font> instructions from occurring too soon after a conditional branch.</p>
<dt><code>-mlow-64k</code></p>
<dd>When enabled, the compiler is free to take advantage of the knowledge that the entire program fits into the low 64k of memory.</p>
<dt><code>-mno-low-64k</code></p>
<dd>Assume that the program is arbitrarily large. This is the default.</p>
<dt><code>-mid-shared-library</code></p>
<dd>Generate code that supports shared libraries via the library <font SIZE="-1">ID</font> method. This allows for execute in place and shared libraries in an environment without virtual memory management. This option implies <code>-fPIC</code>.</p>
<dt><code>-mno-id-shared-library</code></p>
<dd>Generate code that doesn&#8217;t assume <font SIZE="-1">ID</font> based shared libraries are being used. This is the default.</p>
<dt><code>-mshared-library-id=n</code></p>
<dd>Specified the identification number of the <font SIZE="-1">ID</font> based shared library being compiled. Specifying a value of 0 will generate more compact code, specifying other values will force the allocation of that number to the current library but is no more space or time efficient than omitting this option.</p>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Tells the compiler to perform function calls by first loading the address of the function into a register and then performing a subroutine call on this register. This switch is needed if the target function will lie outside of the 24 bit addressing range of the offset based version of subroutine call instruction. </p>
<p> This feature is not enabled by default. Specifying <code>-mno-long-calls</code> will restore the default behavior. Note these switches have no effect on how the compiler generates code to handle function calls via function pointers.</dl>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i> </p>
<p> These options are defined specifically for the <font SIZE="-1">CRIS</font> ports.</p>
<dl>
<dt><code>-march=</code><i>architecture-type</i></p>
<dd>
<dt><code>-mcpu=</code><i>architecture-type</i></p>
<dd>Generate code for the specified architecture. The choices for <i>architecture-type</i> are <code>v3</code>, <code>v8</code> and <code>v10</code> for respectively <font SIZE="-1">ETRAX</font>&nbsp;<wbr>4, <font SIZE="-1">ETRAX</font>&nbsp;<wbr>100, and <font SIZE="-1">ETRAX</font>&nbsp;<wbr>100&nbsp;<wbr><font SIZE="-1">LX</font>. Default is <code>v0</code> except for cris-axis-linux-gnu, where the default is <code>v10</code>.</p>
<dt><code>-mtune=</code><i>architecture-type</i></p>
<dd>Tune to <i>architecture-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The choices for <i>architecture-type</i> are the same as for <code>-march=</code><i>architecture-type</i>.</p>
<dt><code>-mmax-stack-frame=</code><i>n</i></p>
<dd>Warn when the stack frame of a function exceeds <i>n</i> bytes.</p>
<dt><code>-melinux-stacksize=</code><i>n</i></p>
<dd>Only available with the <code>cris-axis-aout</code> target. Arranges for indications in the program to the kernel loader that the stack of the program should be set to <i>n</i> bytes.</p>
<dt><code>-metrax4</code></p>
<dd>
<dt><code>-metrax100</code></p>
<dd>The options <code>-metrax4</code> and <code>-metrax100</code> are synonyms for <code>-march=v3</code> and <code>-march=v8</code> respectively.</p>
<dt><code>-mmul-bug-workaround</code></p>
<dd>
<dt><code>-mno-mul-bug-workaround</code></p>
<dd>Work around a bug in the <tt>&quot;muls&quot;</tt> and <tt>&quot;mulu&quot;</tt> instructions for <font SIZE="-1">CPU</font> models where it applies. This option is active by default.</p>
<dt><code>-mpdebug</code></p>
<dd>Enable CRIS-specific verbose debug-related information in the assembly code. This option also has the effect to turn off the <code>#NO_APP</code> formatted-code indicator to the assembler at the beginning of the assembly file.</p>
<dt><code>-mcc-init</code></p>
<dd>Do not use condition-code results from previous instruction; always emit compare and test instructions before use of condition codes.</p>
<dt><code>-mno-side-effects</code></p>
<dd>Do not emit instructions with side-effects in addressing modes other than post-increment.</p>
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
<dd>These options (no-options) arranges (eliminate arrangements) for the stack-frame, individual data and constants to be aligned for the maximum single data access size for the chosen <font SIZE="-1">CPU</font> model. The default is to arrange for 32-bit alignment. <font SIZE="-1">ABI</font> details such as structure layout are not affected by these options.</p>
<dt><code>-m32-bit</code></p>
<dd>
<dt><code>-m16-bit</code></p>
<dd>
<dt><code>-m8-bit</code></p>
<dd>Similar to the stack- data- and const-align options above, these options arrange for stack-frame, writable data and constants to all be 32-bit, 16-bit or 8-bit aligned. The default is 32-bit alignment.</p>
<dt><code>-mno-prologue-epilogue</code></p>
<dd>
<dt><code>-mprologue-epilogue</code></p>
<dd>With <code>-mno-prologue-epilogue</code>, the normal function prologue and epilogue that sets up the stack-frame are omitted and no return instructions or return sequences are generated in the code. Use this option only together with visual inspection of the compiled code: no warnings or errors are generated when call-saved registers must be saved, or storage for local variable needs to be allocated.</p>
<dt><code>-mno-gotplt</code></p>
<dd>
<dt><code>-mgotplt</code></p>
<dd>With <code>-fpic</code> and <code>-fPIC</code>, don&#8217;t generate (do generate) instruction sequences that load addresses for functions from the <font SIZE="-1">PLT</font> part of the <font SIZE="-1">GOT</font> rather than (traditional on other architectures) calls to the <font SIZE="-1">PLT</font>. The default is <code>-mgotplt</code>.</p>
<dt><code>-maout</code></p>
<dd>Legacy no-op option only recognized with the cris-axis-aout target.</p>
<dt><code>-melf</code></p>
<dd>Legacy no-op option only recognized with the cris-axis-elf and cris-axis-linux-gnu targets.</p>
<dt><code>-melinux</code></p>
<dd>Only recognized with the cris-axis-aout target, where it selects a GNU/linux-like multilib, include files and instruction set for <code>-march=v8</code>.</p>
<dt><code>-mlinux</code></p>
<dd>Legacy no-op option only recognized with the cris-axis-linux-gnu target.</p>
<dt><code>-sim</code></p>
<dd>This option, recognized for the cris-axis-aout and cris-axis-elf arranges to link with input-output functions from a simulator library. Code, initialized data and zero-initialized data are allocated consecutively.</p>
<dt><code>-sim2</code></p>
<dd>Like <code>-sim</code>, but pass linker options to locate initialized data at 0x40000000 and zero-initialized data at 0x80000000.</dl>
<p> <i></i><font SIZE="-1"><i>CRX</i></font><i> Options</i> </p>
<p> These options are defined specifically for the <font SIZE="-1">CRX</font> ports.</p>
<dl>
<dt><code>-mmac</code></p>
<dd>Enable the use of multiply-accumulate instructions. Disabled by default.</p>
<dt><code>-mpush-args</code></p>
<dd>Push instructions will be used to pass outgoing arguments when functions are called. Enabled by default.</dl>
<p> <i>Darwin Options</i> </p>
<p> These options are defined for all architectures running the Darwin operating system. </p>
<p> <font SIZE="-1">FSF</font> <font SIZE="-1">GCC</font> on Darwin does not create &#8220;fat&#8221; object files; it will create an object file for the single architecture that it was built to target. Apple&#8217;s <font SIZE="-1">GCC</font> on Darwin does create &#8220;fat&#8221; files if multiple <code>-arch</code> options are used; it does so by running the compiler or linker multiple times and joining the results together with <i>lipo</i>. </p>
<p> The subtype of the file created (like <code>ppc7400</code> or <code>ppc970</code> or <code>i686</code>) is determined by the flags that specify the <font SIZE="-1">ISA</font> that <font SIZE="-1">GCC</font> is targetting, like <code>-mcpu</code> or <code>-march</code>. The <code>-force_cpusubtype_ALL</code> option can be used to override this. </p>
<p> The Darwin tools vary in their behavior when presented with an <font SIZE="-1">ISA</font> mismatch. The assembler, <i>as</i>, will only permit instructions to be used that are valid for the subtype of the file it is generating, so you cannot put 64-bit instructions in an <code>ppc750</code> object file. The linker for shared libraries, <i>/usr/bin/libtool</i>, will fail and print an error if asked to create a shared library with a less restrictive subtype than its input files (for instance, trying to put a <code>ppc970</code> object file in a <code>ppc7400</code> library). The linker for executables, <i>ld</i>, will quietly give the executable the most restrictive subtype of any of its input files.</p>
<dl>
<dt><code>-F</code><i>dir</i></p>
<dd>Add the framework directory <i>dir</i> to the head of the list of directories to be searched for header files. These directories are interleaved with those specified by <code>-I</code> options and are scanned in a left-to-right order. </p>
<p> A framework directory is a directory with frameworks in it. A framework is a directory with a <code>&#8220;Headers&#8221;</code> and/or <code>&#8220;PrivateHeaders&#8221;</code> directory contained directly in it that ends in <code>&#8220;.framework&#8221;</code>. The name of a framework is the name of this directory excluding the <code>&#8220;.framework&#8221;</code>. Headers associated with the framework are found in one of those two directories, with <code>&#8220;Headers&#8221;</code> being searched first. A subframework is a framework directory that is in a framework&#8217;s <code>&#8220;Frameworks&#8221;</code> directory. Includes of subframework headers can only appear in a header of a framework that contains the subframework, or in a sibling subframework header. Two subframeworks are siblings if they occur in the same framework. A subframework should not have the same name as a framework, a warning will be issued if this is violated. Currently a subframework cannot have subframeworks, in the future, the mechanism may be extended to support this. The standard frameworks can be found in <code>&#8220;/System/Library/Frameworks&#8221;</code> and <code>&#8220;/Library/Frameworks&#8221;</code>. An example include looks like <tt>&quot;#include &lt;<a href="file:/usr/include/Framework/header.h">Framework/header.h</a>&gt;&quot;</tt>, where <code>Framework</code> denotes the name of the framework and header.h is found in the <code>&#8220;PrivateHeaders&#8221;</code> or <code>&#8220;Headers&#8221;</code> directory.</p>
<dt><code>-gused</code></p>
<dd>Emit debugging information for symbols that are used. For <font SIZE="-1">STABS</font> debugging format, this enables <code>-feliminate-unused-debug-symbols</code>. This is by default <font SIZE="-1">ON</font>.</p>
<dt><code>-gfull</code></p>
<dd>Emit debugging information for all symbols and types.</p>
<dt><code>-mmacosx-version-min=</code><i>version</i></p>
<dd>The earliest version of MacOS X that this executable will run on is <i>version</i>. Typical values of <i>version</i> include <tt>10.1</tt>, <tt>10.2</tt>, and <tt>10.3.9</tt>. </p>
<p> The default for this option is to make choices that seem to be most useful.</p>
<dt><code>-mone-byte-bool</code></p>
<dd>Override the defaults for <code>bool</code> so that <code>sizeof(bool)==1</code>. By default <code>sizeof(bool)</code> is <code>4</code> when compiling for Darwin/PowerPC and <code>1</code> when compiling for Darwin/x86, so this option has no effect on x86. </p>
<p> <code>Warning:</code> The <code>-mone-byte-bool</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Using this switch may require recompiling all other modules in a program, including system libraries. Use this switch to conform to a non-default data model.</p>
<dt><code>-mfix-and-continue</code></p>
<dd>
<dt><code>-ffix-and-continue</code></p>
<dd>
<dt><code>-findirect-data</code></p>
<dd>Generate code suitable for fast turn around development. Needed to enable gdb to dynamically load <tt>&quot;.o&quot;</tt> files into already running programs. <code>-findirect-data</code> and <code>-ffix-and-continue</code> are provided for backwards compatibility.</p>
<dt><code>-all_load</code></p>
<dd>Loads all members of static archive libraries. See man <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) for more information.</p>
<dt><code>-arch_errors_fatal</code></p>
<dd>Cause the errors having to do with files that have the wrong architecture to be fatal.</p>
<dt><code>-bind_at_load</code></p>
<dd>Causes the output file to be marked such that the dynamic linker will bind all undefined references when the file is loaded or launched.</p>
<dt><code>-bundle</code></p>
<dd>Produce a Mach-o bundle format file. See man <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) for more information.</p>
<dt><code>-bundle_loader</code> <i>executable</i></p>
<dd>This option specifies the <i>executable</i> that will be loading the build output file being linked. See man <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) for more information.</p>
<dt><code>-dynamiclib</code></p>
<dd>When passed this option, <font SIZE="-1">GCC</font> will produce a dynamic library instead of an executable when linking, using the Darwin <i>libtool</i> command.</p>
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
<dl>
<dt><code>-mno-soft-float</code></p>
<dd>
<dt><code>-msoft-float</code></p>
<dd>Use (do not use) the hardware floating-point instructions for floating-point operations. When <code>-msoft-float</code> is specified, functions in <i>libgcc.a</i> will be used to perform floating-point operations. Unless they are replaced by routines that emulate the floating-point operations, or compiled in such a way as to call such emulations routines, these routines will issue floating-point operations. If you are compiling for an Alpha without floating-point operations, you must ensure that the library is built so as not to call them. </p>
<p> Note that Alpha implementations without floating-point operations are required to have floating-point registers.</p>
<dt><code>-mfp-reg</code></p>
<dd>
<dt><code>-mno-fp-regs</code></p>
<dd>Generate code that uses (does not use) the floating-point register set. <code>-mno-fp-regs</code> implies <code>-msoft-float</code>. If the floating-point register set is not used, floating point operands are passed in integer registers as if they were integers and floating-point results are passed in <tt>$0</tt> instead of <tt>$f0</tt>. This is a non-standard calling sequence, so any function with a floating-point argument or return value called by code compiled with <code>-mno-fp-regs</code> must also be compiled with that option. </p>
<p> A typical use of this option is building a kernel that does not use, and hence need not save and restore, any floating-point registers.</p>
<dt><code>-mieee</code></p>
<dd>The Alpha architecture implements floating-point hardware optimized for maximum performance. It is mostly compliant with the <font SIZE="-1">IEEE</font> floating point standard. However, for full compliance, software assistance is required. This option generates code fully <font SIZE="-1">IEEE</font> compliant code <i>except</i> that the <i>inexact-flag</i> is not maintained (see below). If this option is turned on, the preprocessor macro <tt>&quot;_IEEE_FP&quot;</tt> is defined during compilation. The resulting code is less efficient but is able to correctly support denormalized numbers and exceptional <font SIZE="-1">IEEE</font> values such as not-a-number and plus/minus infinity. Other Alpha compilers call this option <code>-ieee_with_no_inexact</code>.</p>
<dt><code>-mieee-with-inexact</code></p>
<dd>This is like <code>-mieee</code> except the generated code also maintains the <font SIZE="-1">IEEE</font> <i>inexact-flag</i>. Turning on this option causes the generated code to implement fully-compliant <font SIZE="-1">IEEE</font> math. In addition to <tt>&quot;_IEEE_FP&quot;</tt>, <tt>&quot;_IEEE_FP_EXACT&quot;</tt> is defined as a preprocessor macro. On some Alpha implementations the resulting code may execute significantly slower than the code generated by default. Since there is very little code that depends on the <i>inexact-flag</i>, you should normally not specify this option. Other Alpha compilers call this option <code>-ieee_with_inexact</code>.</p>
<dt><code>-mfp-trap-mode=</code><i>trap-mode</i></p>
<dd>This option controls what floating-point related traps are enabled. Other Alpha compilers call this option <code>-fptm</code> <i>trap-mode</i>. The trap mode can be set to one of four values:</p>
<dl>
<dd>
<dl>
<dt><code>n</code></p>
<dd>This is the default (normal) setting. The only traps that are enabled are the ones that cannot be disabled in software (e.g., division by zero trap).</p>
<dt><code>u</code></p>
<dd>In addition to the traps enabled by <code>n</code>, underflow traps are enabled as well.</p>
<dt><code>su</code></p>
<dd>Like <code>su</code>, but the instructions are marked to be safe for software completion (see Alpha architecture manual for details).</p>
<dt><code>sui</code></p>
<dd>Like <code>su</code>, but inexact traps are enabled as well.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-mfp-rounding-mode=</code><i>rounding-mode</i></p>
<dd>Selects the <font SIZE="-1">IEEE</font> rounding mode. Other Alpha compilers call this option <code>-fprm</code> <i>rounding-mode</i>. The <i>rounding-mode</i> can be one of:</p>
<dl>
<dd>
<dl>
<dt><code>n</code></p>
<dd>Normal <font SIZE="-1">IEEE</font> rounding mode. Floating point numbers are rounded towards the nearest machine number or towards the even machine number in case of a tie.</p>
<dt><code>m</code></p>
<dd>Round towards minus infinity.</p>
<dt><code>c</code></p>
<dd>Chopped rounding mode. Floating point numbers are rounded towards zero.</p>
<dt><code>d</code></p>
<dd>Dynamic rounding mode. A field in the floating point control register (<i>fpcr</i>, see Alpha architecture reference manual) controls the rounding mode in effect. The C library initializes this register for rounding towards plus infinity. Thus, unless your program modifies the <i>fpcr</i>, <code>d</code> corresponds to round towards plus infinity.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-mtrap-precision=</code><i>trap-precision</i></p>
<dd>In the Alpha architecture, floating point traps are imprecise. This means without software assistance it is impossible to recover from a floating trap and program execution normally needs to be terminated. <font SIZE="-1">GCC</font> can generate code that can assist operating system trap handlers in determining the exact location that caused a floating point trap. Depending on the requirements of an application, different levels of precisions can be selected:</p>
<dl>
<dd>
<dl>
<dt><code>p</code></p>
<dd>Program precision. This option is the default and means a trap handler can only identify which program caused a floating point exception.</p>
<dt><code>f</code></p>
<dd>Function precision. The trap handler can determine the function that caused a floating point exception.</p>
<dt><code>i</code></p>
<dd>Instruction precision. The trap handler can determine the exact instruction that caused a floating point exception.</dl>
</dl>
<dl>
<dd>Other Alpha compilers provide the equivalent options called <code>-scope_safe</code> and <code>-resumption_safe</code>.</dl>
<dt><code>-mieee-conformant</code></p>
<dd>This option marks the generated code as <font SIZE="-1">IEEE</font> conformant. You must not use this option unless you also specify <code>-mtrap-precision=i</code> and either <code>-mfp-trap-mode=su</code> or <code>-mfp-trap-mode=sui</code>. Its only effect is to emit the line <code>.eflag 48</code> in the function prologue of the generated assembly file. Under <font SIZE="-1">DEC</font> Unix, this has the effect that IEEE-conformant math library routines will be linked in.</p>
<dt><code>-mbuild-constants</code></p>
<dd>Normally <font SIZE="-1">GCC</font> examines a 32- or 64-bit integer constant to see if it can construct it from smaller constants in two or three instructions. If it cannot, it will output the constant as a literal and generate code to load it from the data segment at runtime. </p>
<p> Use this option to require <font SIZE="-1">GCC</font> to construct <i>all</i> integer constants using code, even if it takes more instructions (the maximum is six). </p>
<p> You would typically use this option to build a shared library dynamic loader. Itself a shared library, it must relocate itself in memory before it can find the variables and constants in its own data segment.</p>
<dt><code>-malpha-as</code></p>
<dd>
<dt><code>-mgas</code></p>
<dd>Select whether to generate code to be assembled by the vendor-supplied assembler (<code>-malpha-as</code>) or by the <font SIZE="-1">GNU</font> assembler <code>-mgas</code>.</p>
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
<dd>Indicate whether <font SIZE="-1">GCC</font> should generate code to use the optional <font SIZE="-1">BWX</font>, <font SIZE="-1">CIX</font>, <font SIZE="-1">FIX</font> and <font SIZE="-1">MAX</font> instruction sets. The default is to use the instruction sets supported by the <font SIZE="-1">CPU</font> type specified via <code>-mcpu=</code> option or that of the <font SIZE="-1">CPU</font> on which <font SIZE="-1">GCC</font> was built if none was specified.</p>
<dt><code>-mfloat-vax</code></p>
<dd>
<dt><code>-mfloat-ieee</code></p>
<dd>Generate code that uses (does not use) <font SIZE="-1">VAX</font> F and G floating point arithmetic instead of <font SIZE="-1">IEEE</font> single and double precision.</p>
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
<dd>Set the instruction set and instruction scheduling parameters for machine type <i>cpu_type</i>. You can specify either the <font SIZE="-1"><code>EV</code></font> style name or the corresponding chip number. <font SIZE="-1">GCC</font> supports scheduling parameters for the <font SIZE="-1">EV4</font>, <font SIZE="-1">EV5</font> and <font SIZE="-1">EV6</font> family of processors and will choose the default values for the instruction set from the processor you specify. If you do not specify a processor type, <font SIZE="-1">GCC</font> will default to the processor on which the compiler was built. </p>
<p> Supported values for <i>cpu_type</i> are</p>
<dl>
<dd>
<dl>
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
<dd>Schedules as an <font SIZE="-1">EV6</font> and supports the <font SIZE="-1">BWX</font>, <font SIZE="-1">FIX</font>, and <font SIZE="-1">MAX</font> extensions.</p>
<dt><code>ev67</code></p>
<dd>
<dt><code>21264a</code></p>
<dd>Schedules as an <font SIZE="-1">EV6</font> and supports the <font SIZE="-1">BWX</font>, <font SIZE="-1">CIX</font>, <font SIZE="-1">FIX</font>, and <font SIZE="-1">MAX</font> extensions.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-mtune=</code><i>cpu_type</i></p>
<dd>Set only the instruction scheduling parameters for machine type <i>cpu_type</i>. The instruction set is not changed.</p>
<dt><code>-mmemory-latency=</code><i>time</i></p>
<dd>Sets the latency the scheduler should assume for typical memory references as seen by the application. This number is highly dependent on the memory access patterns used by the application and the size of the external cache on the machine. </p>
<p> Valid options for <i>time</i> are</p>
<dl>
<dd>
<dl>
<dt><i>number</i></p>
<dd>A decimal number representing clock cycles.</p>
<dt><code>L1</code></p>
<dd>
<dt><code>L2</code></p>
<dd>
<dt><code>L3</code></p>
<dd>
<dt><code>main</code></p>
<dd>The compiler contains estimates of the number of clock cycles for &#8220;typical&#8221; <font SIZE="-1">EV4</font> &amp; <font SIZE="-1">EV5</font> hardware for the Level 1, 2 &amp; 3 caches (also called Dcache, Scache, and Bcache), as well as to main memory. Note that L3 is only valid for <font SIZE="-1">EV5</font>.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha/VMS Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">DEC</font> Alpha/VMS implementations:</p>
<dl>
<dt><code>-mvms-return-codes</code></p>
<dd>Return <font SIZE="-1">VMS</font> condition codes from main. The default is to return <font SIZE="-1">POSIX</font> style condition (e.g. error) codes.</dl>
<p> <i></i><font SIZE="-1"><i>FRV</i></font><i> Options</i></p>
<dl>
<dt><code>-mgpr-32</code></p>
<dd>Only use the first 32 general purpose registers.</p>
<dt><code>-mgpr-64</code></p>
<dd>Use all 64 general purpose registers.</p>
<dt><code>-mfpr-32</code></p>
<dd>Use only the first 32 floating point registers.</p>
<dt><code>-mfpr-64</code></p>
<dd>Use all 64 floating point registers</p>
<dt><code>-mhard-float</code></p>
<dd>Use hardware instructions for floating point operations.</p>
<dt><code>-msoft-float</code></p>
<dd>Use library routines for floating point operations.</p>
<dt><code>-malloc-cc</code></p>
<dd>Dynamically allocate condition code registers.</p>
<dt><code>-mfixed-cc</code></p>
<dd>Do not try to dynamically allocate condition code registers, only use <tt>&quot;icc0&quot;</tt> and <tt>&quot;fcc0&quot;</tt>.</p>
<dt><code>-mdword</code></p>
<dd>Change <font SIZE="-1">ABI</font> to use double word insns.</p>
<dt><code>-mno-dword</code></p>
<dd>Do not use double word instructions.</p>
<dt><code>-mdouble</code></p>
<dd>Use floating point double instructions.</p>
<dt><code>-mno-double</code></p>
<dd>Do not use floating point double instructions.</p>
<dt><code>-mmedia</code></p>
<dd>Use media instructions.</p>
<dt><code>-mno-media</code></p>
<dd>Do not use media instructions.</p>
<dt><code>-mmuladd</code></p>
<dd>Use multiply and add/subtract instructions.</p>
<dt><code>-mno-muladd</code></p>
<dd>Do not use multiply and add/subtract instructions.</p>
<dt><code>-mfdpic</code></p>
<dd>Select the <font SIZE="-1">FDPIC</font> <font SIZE="-1">ABI</font>, that uses function descriptors to represent pointers to functions. Without any PIC/PIE-related options, it implies <code>-fPIE</code>. With <code>-fpic</code> or <code>-fpie</code>, it assumes <font SIZE="-1">GOT</font> entries and small data are within a 12-bit range from the <font SIZE="-1">GOT</font> base address; with <code>-fPIC</code> or <code>-fPIE</code>, <font SIZE="-1">GOT</font> offsets are computed with 32 bits.</p>
<dt><code>-minline-plt</code></p>
<dd>Enable inlining of <font SIZE="-1">PLT</font> entries in function calls to functions that are not known to bind locally. It has no effect without <code>-mfdpic</code>. It&#8217;s enabled by default if optimizing for speed and compiling for shared libraries (i.e., <code>-fPIC</code> or <code>-fpic</code>), or when an optimization option such as <code>-O3</code> or above is present in the command line.</p>
<dt><code>-mTLS</code></p>
<dd>Assume a large <font SIZE="-1">TLS</font> segment when generating thread-local code.</p>
<dt><code>-mtls</code></p>
<dd>Do not assume a large <font SIZE="-1">TLS</font> segment when generating thread-local code.</p>
<dt><code>-mgprel-ro</code></p>
<dd>Enable the use of <tt>&quot;GPREL&quot;</tt> relocations in the <font SIZE="-1">FDPIC</font> <font SIZE="-1">ABI</font> for data that is known to be in read-only sections. It&#8217;s enabled by default, except for <code>-fpic</code> or <code>-fpie</code>: even though it may help make the global offset table smaller, it trades 1 instruction for 4. With <code>-fPIC</code> or <code>-fPIE</code>, it trades 3 instructions for 4, one of which may be shared by multiple symbols, and it avoids the need for a <font SIZE="-1">GOT</font> entry for the referenced symbol, so it&#8217;s more likely to be a win. If it is not, <code>-mno-gprel-ro</code> can be used to disable it.</p>
<dt><code>-multilib-library-pic</code></p>
<dd>Link with the (library, not <font SIZE="-1">FD</font>) pic libraries. It&#8217;s implied by <code>-mlibrary-pic</code>, as well as by <code>-fPIC</code> and <code>-fpic</code> without <code>-mfdpic</code>. You should never have to use it explicitly.</p>
<dt><code>-mlinked-fp</code></p>
<dd>Follow the <font SIZE="-1">EABI</font> requirement of always creating a frame pointer whenever a stack frame is allocated. This option is enabled by default and can be disabled with <code>-mno-linked-fp</code>.</p>
<dt><code>-mlong-calls</code></p>
<dd>Use indirect addressing to call functions outside the current compilation unit. This allows the functions to be placed anywhere within the 32-bit address space.</p>
<dt><code>-malign-labels</code></p>
<dd>Try to align labels to an 8-byte boundary by inserting nops into the previous packet. This option only has an effect when <font SIZE="-1">VLIW</font> packing is enabled. It doesn&#8217;t create new packets; it merely adds nops to existing ones.</p>
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
<dd>This switch removes redundant <tt>&quot;membar&quot;</tt> instructions from the compiler generated code. It is enabled by default.</p>
<dt><code>-mno-optimize-membar</code></p>
<dd>This switch disables the automatic removal of redundant <tt>&quot;membar&quot;</tt> instructions from the generated code.</p>
<dt><code>-mtomcat-stats</code></p>
<dd>Cause gas to print out tomcat statistics.</p>
<dt><code>-mcpu=</code><i>cpu</i></p>
<dd>Select the processor type for which to generate code. Possible values are <code>frv</code>, <code>fr550</code>, <code>tomcat</code>, <code>fr500</code>, <code>fr450</code>, <code>fr405</code>, <code>fr400</code>, <code>fr300</code> and <code>simple</code>.</dl>
<p> <i>H8/300 Options</i> </p>
<p> These <code>-m</code> options are defined for the H8/300 implementations:</p>
<dl>
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
<dt><code>-mint32</code></p>
<dd>Make <tt>&quot;int&quot;</tt> data 32 bits by default.</p>
<dt><code>-malign-300</code></p>
<dd>On the H8/300H and H8S, use the same alignment rules as for the H8/300. The default for the H8/300H and H8S is to align longs and floats on 4 byte boundaries. <code>-malign-300</code> causes them to be aligned on 2 byte boundaries. This option has no effect on the H8/300.</dl>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">HPPA</font> family of computers:</p>
<dl>
<dt><code>-march=</code><i>architecture-type</i></p>
<dd>Generate code for the specified architecture. The choices for <i>architecture-type</i> are <code>1.0</code> for <font SIZE="-1">PA</font> 1.0, <code>1.1</code> for <font SIZE="-1">PA</font> 1.1, and <code>2.0</code> for <font SIZE="-1">PA</font> 2.0 processors. Refer to <i>/usr/lib/sched.models</i> on an HP-UX system to determine the proper architecture option for your machine. Code compiled for lower numbered architectures will run on higher numbered architectures, but not the other way around.</p>
<dt><code>-mpa-risc-1-0</code></p>
<dd>
<dt><code>-mpa-risc-1-1</code></p>
<dd>
<dt><code>-mpa-risc-2-0</code></p>
<dd>Synonyms for <code>-march=1.0</code>, <code>-march=1.1</code>, and <code>-march=2.0</code> respectively.</p>
<dt><code>-mbig-switch</code></p>
<dd>Generate code suitable for big switch tables. Use this option only if the assembler/linker complain about out of range branches within a switch table.</p>
<dt><code>-mjump-in-delay</code></p>
<dd>Fill delay slots of function calls with unconditional jump instructions by modifying the return pointer for the function call to be the target of the conditional jump.</p>
<dt><code>-mdisable-fpregs</code></p>
<dd>Prevent floating point registers from being used in any manner. This is necessary for compiling kernels which perform lazy context switching of floating point registers. If you use this option and attempt to perform floating point operations, the compiler will abort.</p>
<dt><code>-mdisable-indexing</code></p>
<dd>Prevent the compiler from using indexing address modes. This avoids some rather obscure problems when compiling <font SIZE="-1">MIG</font> generated code under <font SIZE="-1">MACH</font>.</p>
<dt><code>-mno-space-regs</code></p>
<dd>Generate code that assumes the target has no space registers. This allows <font SIZE="-1">GCC</font> to generate faster indirect calls and use unscaled index address modes. </p>
<p> Such code is suitable for level 0 <font SIZE="-1">PA</font> systems and kernels.</p>
<dt><code>-mfast-indirect-calls</code></p>
<dd>Generate code that assumes calls never cross space boundaries. This allows <font SIZE="-1">GCC</font> to emit code which performs faster indirect calls. </p>
<p> This option will not work in the presence of shared libraries or nested functions.</p>
<dt><code>-mfixed-range=</code><i>register-range</i></p>
<dd>Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator can not use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma.</p>
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
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">HPPA</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded target <code>hppa1.1-*-pro</code> does provide software floating point support. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC</font>, with <code>-msoft-float</code> in order for this to work.</p>
<dt><code>-msio</code></p>
<dd>Generate the predefine, <tt>&quot;_SIO&quot;</tt>, for server <font SIZE="-1">IO</font>. The default is <code>-mwsio</code>. This generates the predefines, <tt>&quot;__hp9000s700&quot;</tt>, <tt>&quot;__hp9000s700__&quot;</tt> and <tt>&quot;_WSIO&quot;</tt>, for workstation <font SIZE="-1">IO</font>. These options are available under HP-UX and <font SIZE="-1">HI-UX</font>.</p>
<dt><code>-mgnu-ld</code></p>
<dd>Use <font SIZE="-1">GNU</font> ld specific options. This passes <code>-shared</code> to ld when building a shared library. It is the default when <font SIZE="-1">GCC</font> is configured, explicitly or implicitly, with the <font SIZE="-1">GNU</font> linker. This option does not have any affect on which ld is called, it only changes what parameters are passed to that ld. The ld that is called is determined by the <code>&#8211;with-ld</code> configure option, <font SIZE="-1">GCC</font>&#8216;s program search path, and finally by the user&#8217;s <font SIZE="-1"><code>PATH</code></font>. The linker used by <font SIZE="-1">GCC</font> can be printed using <code>which `gcc -print-prog-name=ld`</code>. This option is only available on the 64 bit HP-UX <font SIZE="-1">GCC</font>, i.e. configured with <code>hppa*64*-*-hpux*</code>.</p>
<dt><code>-mhp-ld</code></p>
<dd>Use <font SIZE="-1">HP</font> ld specific options. This passes <code>-b</code> to ld when building a shared library and passes <code>+Accept TypeMismatch</code> to ld on all links. It is the default when <font SIZE="-1">GCC</font> is configured, explicitly or implicitly, with the <font SIZE="-1">HP</font> linker. This option does not have any affect on which ld is called, it only changes what parameters are passed to that ld. The ld that is called is determined by the <code>&#8211;with-ld</code> configure option, <font SIZE="-1">GCC</font>&#8216;s program search path, and finally by the user&#8217;s <font SIZE="-1"><code>PATH</code></font>. The linker used by <font SIZE="-1">GCC</font> can be printed using <code>which `gcc -print-prog-name=ld`</code>. This option is only available on the 64 bit HP-UX <font SIZE="-1">GCC</font>, i.e. configured with <code>hppa*64*-*-hpux*</code>.</p>
<dt><code>-mlong-calls</code></p>
<dd>Generate code that uses long call sequences. This ensures that a call is always able to reach linker generated stubs. The default is to generate long calls only when the distance from the call site to the beginning of the function or translation unit, as the case may be, exceeds a predefined limit set by the branch type being used. The limits for normal calls are 7,600,000 and 240,000 bytes, respectively for the <font SIZE="-1">PA</font> 2.0 and <font SIZE="-1">PA</font> 1.X architectures. Sibcalls are always limited at 240,000 bytes. </p>
<p> Distances are measured from the beginning of functions when using the <code>-ffunction-sections</code> option, or when using the <code>-mgas</code> and <code>-mno-portable-runtime</code> options together under HP-UX with the <font SIZE="-1">SOM</font> linker. </p>
<p> It is normally not desirable to use this option as it will degrade performance. However, it may be useful in large applications, particularly when partial linking is used to build the application. </p>
<p> The types of long calls used depends on the capabilities of the assembler and linker, and the type of code being generated. The impact on systems that support long absolute calls, and long pic symbol-difference or pc-relative calls should be relatively small. However, an indirect call is used on 32-bit <font SIZE="-1">ELF</font> systems in pic code and it is quite long.</p>
<dt><code>-munix=</code><i>unix-std</i></p>
<dd>Generate compiler predefines and select a startfile for the specified <font SIZE="-1">UNIX</font> standard. The choices for <i>unix-std</i> are <code>93</code>, <code>95</code> and <code>98</code>. <code>93</code> is supported on all HP-UX versions. <code>95</code> is available on HP-UX 10.10 and later. <code>98</code> is available on HP-UX 11.11 and later. The default values are <code>93</code> for HP-UX 10.00, <code>95</code> for HP-UX 10.10 though to 11.00, and <code>98</code> for HP-UX 11.11 and later. </p>
<p> <code>-munix=93</code> provides the same predefines as <font SIZE="-1">GCC</font> 3.3 and 3.4. <code>-munix=95</code> provides additional predefines for <tt>&quot;XOPEN_UNIX&quot;</tt> and <tt>&quot;_XOPEN_SOURCE_EXTENDED&quot;</tt>, and the startfile <i>unix95.o</i>. <code>-munix=98</code> provides additional predefines for <tt>&quot;_XOPEN_UNIX&quot;</tt>, <tt>&quot;_XOPEN_SOURCE_EXTENDED&quot;</tt>, <tt>&quot;_INCLUDE__STDC_A1_SOURCE&quot;</tt> and <tt>&quot;_INCLUDE_XOPEN_SOURCE_500&quot;</tt>, and the startfile <i>unix98.o</i>. </p>
<p> It is <i>important</i> to note that this option changes the interfaces for various library routines. It also affects the operational behavior of the C library. Thus, <i>extreme</i> care is needed in using this option. </p>
<p> Library code that is intended to operate with more than one <font SIZE="-1">UNIX</font> standard must test, set and restore the variable <i>__xpg4_extended_mask</i> as appropriate. Most <font SIZE="-1">GNU</font> software doesn&#8217;t provide this capability.</p>
<dt><code>-nolibdld</code></p>
<dd>Suppress the generation of link options to search libdld.sl when the <code>-static</code> option is specified on HP-UX 10 and later.</p>
<dt><code>-static</code></p>
<dd>The HP-UX implementation of setlocale in libc has a dependency on libdld.sl. There isn&#8217;t an archive version of libdld.sl. Thus, when the <code>-static</code> option is specified, special link options are needed to resolve this dependency. </p>
<p> On HP-UX 10 and later, the <font SIZE="-1">GCC</font> driver adds the necessary options to link with libdld.sl when the <code>-static</code> option is specified. This causes the resulting binary to be dynamic. On the 64-bit port, the linkers generate dynamic binaries by default in any case. The <code>-nolibdld</code> option can be used to prevent the <font SIZE="-1">GCC</font> driver from adding these link options.</p>
<dt><code>-threads</code></p>
<dd>Add support for multithreading with the <i>dce thread</i> library under <font SIZE="-1">HP-UX</font>. This option sets flags for both the preprocessor and linker.</dl>
<p> <i>Intel 386 and </i><font SIZE="-1"><i>AMD</i></font><i> x86-64 Options</i> </p>
<p> These <code>-m</code> options are defined for the i386 and x86-64 family of computers:</p>
<dl>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Tune to <i>cpu-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The choices for <i>cpu-type</i> are:</p>
<dl>
<dd>
<dl>
<dt><i>i386</i></p>
<dd>Original Intel&#8217;s i386 <font SIZE="-1">CPU</font>.</p>
<dt><i>i486</i></p>
<dd>Intel&#8217;s i486 <font SIZE="-1">CPU</font>. (No scheduling is implemented for this chip.)</p>
<dt><i>i586, pentium</i></p>
<dd>Intel Pentium <font SIZE="-1">CPU</font> with no <font SIZE="-1">MMX</font> support.</p>
<dt><i>pentium-mmx</i></p>
<dd>Intel PentiumMMX <font SIZE="-1">CPU</font> based on Pentium core with <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><i>i686, pentiumpro</i></p>
<dd>Intel PentiumPro <font SIZE="-1">CPU</font>.</p>
<dt><i>pentium2</i></p>
<dd>Intel Pentium2 <font SIZE="-1">CPU</font> based on PentiumPro core with <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><i>pentium3, pentium3m</i></p>
<dd>Intel Pentium3 <font SIZE="-1">CPU</font> based on PentiumPro core with <font SIZE="-1">MMX</font> and <font SIZE="-1">SSE</font> instruction set support.</p>
<dt><i>pentium-m</i></p>
<dd>Low power version of Intel Pentium3 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font> and <font SIZE="-1">SSE2</font> instruction set support. Used by Centrino notebooks.</p>
<dt><i>pentium4, pentium4m</i></p>
<dd>Intel Pentium4 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font> and <font SIZE="-1">SSE2</font> instruction set support.</p>
<dt><i>prescott</i></p>
<dd>Improved version of Intel Pentium4 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font>, <font SIZE="-1">SSE2</font> and <font SIZE="-1">SSE3</font> instruction set support.</p>
<dt><i>nocona</i></p>
<dd>Improved version of Intel Pentium4 <font SIZE="-1">CPU</font> with 64-bit extensions, <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font>, <font SIZE="-1">SSE2</font> and <font SIZE="-1">SSE3</font> instruction set support.</p>
<dt><i>k6</i></p>
<dd><font SIZE="-1">AMD</font> K6 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><i>k6-2, k6-3</i></p>
<dd>Improved versions of <font SIZE="-1">AMD</font> K6 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font> and 3dNOW! instruction set support.</p>
<dt><i>athlon, athlon-tbird</i></p>
<dd><font SIZE="-1">AMD</font> Athlon <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font>, 3dNOW!, enhanced 3dNOW! and <font SIZE="-1">SSE</font> prefetch instructions support.</p>
<dt><i>athlon-4, athlon-xp, athlon-mp</i></p>
<dd>Improved <font SIZE="-1">AMD</font> Athlon <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font>, 3dNOW!, enhanced 3dNOW! and full <font SIZE="-1">SSE</font> instruction set support.</p>
<dt><i>k8, opteron, athlon64, athlon-fx</i></p>
<dd><font SIZE="-1">AMD</font> K8 core based CPUs with x86-64 instruction set support. (This supersets <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font>, <font SIZE="-1">SSE2</font>, 3dNOW!, enhanced 3dNOW! and 64-bit instruction set extensions.)</p>
<dt><i>winchip-c6</i></p>
<dd><font SIZE="-1">IDT</font> Winchip C6 <font SIZE="-1">CPU</font>, dealt in same way as i486 with additional <font SIZE="-1">MMX</font> instruction set support.</p>
<dt><i>winchip2</i></p>
<dd><font SIZE="-1">IDT</font> Winchip2 <font SIZE="-1">CPU</font>, dealt in same way as i486 with additional <font SIZE="-1">MMX</font> and 3dNOW! instruction set support.</p>
<dt><i>c3</i></p>
<dd>Via C3 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font> and 3dNOW! instruction set support. (No scheduling is implemented for this chip.)</p>
<dt><i>c3-2</i></p>
<dd>Via C3-2 <font SIZE="-1">CPU</font> with <font SIZE="-1">MMX</font> and <font SIZE="-1">SSE</font> instruction set support. (No scheduling is implemented for this chip.)</dl>
</dl>
<dl>
<dd>While picking a specific <i>cpu-type</i> will schedule things appropriately for that particular chip, the compiler will not generate any code that does not run on the i386 without the <code>-march=</code><i>cpu-type</i> option being used.</dl>
<dt><code>-march=</code><i>cpu-type</i></p>
<dd>Generate instructions for the machine type <i>cpu-type</i>. The choices for <i>cpu-type</i> are the same as for <code>-mtune</code>. Moreover, specifying <code>-march=</code><i>cpu-type</i> implies <code>-mtune=</code><i>cpu-type</i>.</p>
<dt><code>-mcpu=</code><i>cpu-type</i></p>
<dd>A deprecated synonym for <code>-mtune</code>.</p>
<dt><code>-m386</code></p>
<dd>
<dt><code>-m486</code></p>
<dd>
<dt><code>-mpentium</code></p>
<dd>
<dt><code>-mpentiumpro</code></p>
<dd>These options are synonyms for <code>-mtune=i386</code>, <code>-mtune=i486</code>, <code>-mtune=pentium</code>, and <code>-mtune=pentiumpro</code> respectively. These synonyms are deprecated.</p>
<dt><code>-mfpmath=</code><i>unit</i></p>
<dd>Generate floating point arithmetics for selected unit <i>unit</i>. The choices for <i>unit</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>387</code></p>
<dd>Use the standard 387 floating point coprocessor present majority of chips and emulated otherwise. Code compiled with this option will run almost everywhere. The temporary results are computed in 80bit precision instead of precision specified by the type resulting in slightly different results compared to most of other chips. See <code>-ffloat-store</code> for more detailed description. </p>
<p> This is the default choice for i386 compiler.</p>
<dt><code>sse</code></p>
<dd>Use scalar floating point instructions present in the <font SIZE="-1">SSE</font> instruction set. This instruction set is supported by Pentium3 and newer chips, in the <font SIZE="-1">AMD</font> line by Athlon-4, Athlon-xp and Athlon-mp chips. The earlier version of <font SIZE="-1">SSE</font> instruction set supports only single precision arithmetics, thus the double and extended precision arithmetics is still done using 387. Later version, present only in Pentium4 and the future <font SIZE="-1">AMD</font> x86-64 chips supports double precision arithmetics too. </p>
<p> For the i386 compiler, you need to use <code>-march=</code><i>cpu-type</i>, <code>-msse</code> or <code>-msse2</code> switches to enable <font SIZE="-1">SSE</font> extensions and make this option effective. For the x86-64 compiler, these extensions are enabled by default. </p>
<p> The resulting code should be considerably faster in the majority of cases and avoid the numerical instability problems of 387 code, but may break some existing code that expects temporaries to be 80bit. </p>
<p> This is the default choice for the x86-64 compiler.</p>
<dt><code>sse,387</code></p>
<dd>Attempt to utilize both instruction sets at once. This effectively double the amount of available registers and on chips with separate execution units for 387 and <font SIZE="-1">SSE</font> the execution resources too. Use this option with care, as it is still experimental, because the <font SIZE="-1">GCC</font> register allocator does not model separate functional units well resulting in instable performance.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-masm=</code><i>dialect</i></p>
<dd>Output asm instructions using selected <i>dialect</i>. Supported choices are <code>intel</code> or <code>att</code> (the default one). Darwin does not support <code>intel</code>.</p>
<dt><code>-mieee-fp</code></p>
<dd>
<dt><code>-mno-ieee-fp</code></p>
<dd>Control whether or not the compiler uses <font SIZE="-1">IEEE</font> floating point comparisons. These handle correctly the case where the result of a comparison is unordered.</p>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not part of <font SIZE="-1">GCC</font>. Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. </p>
<p> On machines where a function returns floating point results in the 80387 register stack, some floating point opcodes may be emitted even if <code>-msoft-float</code> is used.</p>
<dt><code>-mno-fp-ret-in-387</code></p>
<dd>Do not use the <font SIZE="-1">FPU</font> registers for return values of functions. </p>
<p> The usual calling convention has functions return values of types <tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt> in an <font SIZE="-1">FPU</font> register, even if there is no <font SIZE="-1">FPU</font>. The idea is that the operating system should emulate an <font SIZE="-1">FPU</font>. </p>
<p> The option <code>-mno-fp-ret-in-387</code> causes such values to be returned in ordinary <font SIZE="-1">CPU</font> registers instead.</p>
<dt><code>-mno-fancy-math-387</code></p>
<dd>Some 387 emulators do not support the <tt>&quot;sin&quot;</tt>, <tt>&quot;cos&quot;</tt> and <tt>&quot;sqrt&quot;</tt> instructions for the 387. Specify this option to avoid generating those instructions. This option is the default on FreeBSD, OpenBSD and NetBSD. This option is overridden when <code>-march</code> indicates that the target cpu will always have an <font SIZE="-1">FPU</font> and so the instruction will not need emulation. As of revision 2.6.1, these instructions are not generated unless you also use the <code>-funsafe-math-optimizations</code> switch.</p>
<dt><code>-malign-double</code></p>
<dd>
<dt><code>-mno-align-double</code></p>
<dd>Control whether <font SIZE="-1">GCC</font> aligns <tt>&quot;double&quot;</tt>, <tt>&quot;long double&quot;</tt>, and <tt>&quot;long long&quot;</tt> variables on a two word boundary or a one word boundary. Aligning <tt>&quot;double&quot;</tt> variables on a two word boundary will produce code that runs somewhat faster on a <code>Pentium</code> at the expense of more memory. </p>
<p> On x86-64, <code>-malign-double</code> is enabled by default. </p>
<p> <code>Warning:</code> if you use the <code>-malign-double</code> switch, structures containing the above types will be aligned differently than the published application binary interface specifications for the 386 and will not be binary compatible with structures in code compiled without that switch.</p>
<dt><code>-m96bit-long-double</code></p>
<dd>
<dt><code>-m128bit-long-double</code></p>
<dd>These switches control the size of <tt>&quot;long double&quot;</tt> type. The i386 application binary interface specifies the size to be 96 bits, so <code>-m96bit-long-double</code> is the default in 32 bit mode. </p>
<p> Modern architectures (Pentium and newer) would prefer <tt>&quot;long double&quot;</tt> to be aligned to an 8 or 16 byte boundary. In arrays or structures conforming to the <font SIZE="-1">ABI</font>, this would not be possible. So specifying a <code>-m128bit-long-double</code> will align <tt>&quot;long double&quot;</tt> to a 16 byte boundary by padding the <tt>&quot;long double&quot;</tt> with an additional 32 bit zero. </p>
<p> In the x86-64 compiler, <code>-m128bit-long-double</code> is the default choice as its <font SIZE="-1">ABI</font> specifies that <tt>&quot;long double&quot;</tt> is to be aligned on 16 byte boundary. </p>
<p> Notice that neither of these options enable any extra precision over the x87 standard of 80 bits for a <tt>&quot;long double&quot;</tt>. </p>
<p> <code>Warning:</code> if you override the default value for your target <font SIZE="-1">ABI</font>, the structures and arrays containing <tt>&quot;long double&quot;</tt> variables will change their size as well as function calling convention for function taking <tt>&quot;long double&quot;</tt> will be modified. Hence they will not be binary compatible with arrays or structures in code compiled without that switch.</p>
<dt><code>-mmlarge-data-threshold=</code><i>number</i></p>
<dd>When <code>-mcmodel=medium</code> is specified, the data greater than <i>threshold</i> are placed in large data section. This value must be the same across all object linked into the binary and defaults to 65535.</p>
<dt><code>-msvr3-shlib</code></p>
<dd>
<dt><code>-mno-svr3-shlib</code></p>
<dd>Control whether <font SIZE="-1">GCC</font> places uninitialized local variables into the <tt>&quot;bss&quot;</tt> or <tt>&quot;data&quot;</tt> segments. <code>-msvr3-shlib</code> places them into <tt>&quot;bss&quot;</tt>. These options are meaningful only on System V Release 3.</p>
<dt><code>-mrtd</code></p>
<dd>Use a different function-calling convention, in which functions that take a fixed number of arguments return with the <tt>&quot;ret&quot;</tt> <i>num</i> instruction, which pops their arguments while returning. This saves one instruction in the caller since there is no need to pop the arguments there. </p>
<p> You can specify that an individual function is called with this calling sequence with the function attribute <code>stdcall</code>. You can also override the <code>-mrtd</code> option by using the function attribute <code>cdecl</code>. </p>
<p> <code>Warning:</code> this calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <tt>&quot;printf&quot;</tt>); otherwise incorrect code will be generated for calls to those functions. </p>
<p> In addition, seriously incorrect code will result if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.)</p>
<dt><code>-mregparm=</code><i>num</i></p>
<dd>Control how many registers are used to pass integer arguments. By default, no registers are used to pass arguments, and at most 3 registers can be used. You can control this behavior for a specific function by using the function attribute <code>regparm</code>. </p>
<p> <code>Warning:</code> if you use this switch, and <i>num</i> is nonzero, then you must build all modules with the same value, including any libraries. This includes the system libraries and startup modules.</p>
<dt><code>-msseregparm</code></p>
<dd>Use <font SIZE="-1">SSE</font> register passing conventions for float and double arguments and return values. You can control this behavior for a specific function by using the function attribute <code>sseregparm</code>. </p>
<p> <code>Warning:</code> if you use this switch then you must build all modules with the same value, including any libraries. This includes the system libraries and startup modules.</p>
<dt><code>-mpreferred-stack-boundary=</code><i>num</i></p>
<dd>Attempt to keep the stack boundary aligned to a 2 raised to <i>num</i> byte boundary. If <code>-mpreferred-stack-boundary</code> is not specified, the default is 4 (16 bytes or 128 bits). </p>
<p> On Pentium and PentiumPro, <tt>&quot;double&quot;</tt> and <tt>&quot;long double&quot;</tt> values should be aligned to an 8 byte boundary (see <code>-malign-double</code>) or suffer significant run time performance penalties. On Pentium <font SIZE="-1">III</font>, the Streaming <font SIZE="-1">SIMD</font> Extension (<font SIZE="-1">SSE</font>) data type <tt>&quot;__m128&quot;</tt> may not work properly if it is not 16 byte aligned. </p>
<p> To ensure proper alignment of this values on the stack, the stack boundary must be as aligned as that required by any value stored on the stack. Further, every function must be generated such that it keeps the stack aligned. Thus calling a function compiled with a higher preferred stack boundary from a function compiled with a lower preferred stack boundary will most likely misalign the stack. It is recommended that libraries that use callbacks always use the default setting. </p>
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
<dt><code>-m3dnow</code></p>
<dd>
<dt><code>-mno-3dnow</code></p>
<dd>These switches enable or disable the use of instructions in the <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font>, <font SIZE="-1">SSE2</font> or 3DNow! extended instruction sets. These extensions are also available as built-in functions: see <code>X86 Built-in Functions</code>, for details of the functions enabled and disabled by these switches. </p>
<p> To have <font SIZE="-1">SSE/SSE2</font> instructions generated automatically from floating-point code (as opposed to 387 instructions), see <code>-mfpmath=sse</code>. </p>
<p> These options will enable <font SIZE="-1">GCC</font> to use these extended instructions in generated code, even without <code>-mfpmath=sse</code>. Applications which perform runtime <font SIZE="-1">CPU</font> detection must compile separate files for each supported architecture, using the appropriate flags. In particular, the file containing the <font SIZE="-1">CPU</font> detection code should be compiled without these options.</p>
<dt><code>-mpush-args</code></p>
<dd>
<dt><code>-mno-push-args</code></p>
<dd>Use <font SIZE="-1">PUSH</font> operations to store outgoing parameters. This method is shorter and usually equally fast as method using <font SIZE="-1">SUB/MOV</font> operations and is enabled by default. In some cases disabling it may improve performance because of improved scheduling and reduced dependencies.</p>
<dt><code>-maccumulate-outgoing-args</code></p>
<dd>If enabled, the maximum amount of space required for outgoing arguments will be computed in the function prologue. This is faster on most modern CPUs because of reduced dependencies, improved scheduling and reduced stack usage when preferred stack boundary is not equal to 2. The drawback is a notable increase in code size. This switch implies <code>-mno-push-args</code>.</p>
<dt><code>-mthreads</code></p>
<dd>Support thread-safe exception handling on <code>Mingw32</code>. Code that relies on thread-safe exception handling must compile and link all code with the <code>-mthreads</code> option. When compiling, <code>-mthreads</code> defines <code>-D_MT</code>; when linking, it links in a special thread helper library <code>-lmingwthrd</code> which cleans up per thread exception handling data.</p>
<dt><code>-mno-align-stringops</code></p>
<dd>Do not align destination of inlined string operations. This switch reduces code size and improves performance in case the destination is already aligned, but <font SIZE="-1">GCC</font> doesn&#8217;t know about it.</p>
<dt><code>-minline-all-stringops</code></p>
<dd>By default <font SIZE="-1">GCC</font> inlines string operations only when destination is known to be aligned at least to 4 byte boundary. This enables more inlining, increase code size, but may improve performance of code that depends on fast memcpy, strlen and memset for short lengths.</p>
<dt><code>-momit-leaf-frame-pointer</code></p>
<dd>Don&#8217;t keep the frame pointer in a register for leaf functions. This avoids the instructions to save, set up and restore frame pointers and makes an extra register available in leaf functions. The option <code>-fomit-frame-pointer</code> removes the frame pointer for all functions which might make debugging harder.</p>
<dt><code>-mtls-direct-seg-refs</code></p>
<dd>
<dt><code>-mno-tls-direct-seg-refs</code></p>
<dd>Controls whether <font SIZE="-1">TLS</font> variables may be accessed with offsets from the <font SIZE="-1">TLS</font> segment register (<tt>%gs</tt> for 32-bit, <tt>%fs</tt> for 64-bit), or whether the thread base pointer must be added. Whether or not this is legal depends on the operating system, and whether it maps the segment to cover the entire <font SIZE="-1">TLS</font> area. </p>
<p> For systems that use <font SIZE="-1">GNU</font> libc, the default is on.</dl>
<p> These <code>-m</code> switches are supported in addition to the above on <font SIZE="-1">AMD</font> x86-64 processors in 64-bit environments.</p>
<dl>
<dt><code>-m32</code></p>
<dd>
<dt><code>-m64</code></p>
<dd>Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits and generates code that runs on any i386 system. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits and generates code for <font SIZE="-1">AMD</font>&#8216;s x86-64 architecture.</p>
<dt><code>-mno-red-zone</code></p>
<dd>Do not use a so called red zone for x86-64 code. The red zone is mandated by the x86-64 <font SIZE="-1">ABI</font>, it is a 128-byte area beyond the location of the stack pointer that will not be modified by signal or interrupt handlers and therefore can be used for temporary data without adjusting the stack pointer. The flag <code>-mno-red-zone</code> disables this red zone.</p>
<dt><code>-mcmodel=small</code></p>
<dd>Generate code for the small code model: the program and its symbols must be linked in the lower 2 <font SIZE="-1">GB</font> of the address space. Pointers are 64 bits. Programs can be statically or dynamically linked. This is the default code model.</p>
<dt><code>-mcmodel=kernel</code></p>
<dd>Generate code for the kernel code model. The kernel runs in the negative 2 <font SIZE="-1">GB</font> of the address space. This model has to be used for Linux kernel code.</p>
<dt><code>-mcmodel=medium</code></p>
<dd>Generate code for the medium model: The program is linked in the lower 2 <font SIZE="-1">GB</font> of the address space but symbols can be located anywhere in the address space. Programs can be statically or dynamically linked, but building of shared libraries are not supported with the medium model.</p>
<dt><code>-mcmodel=large</code></p>
<dd>Generate code for the large model: This model makes no assumptions about addresses and sizes of sections. Currently <font SIZE="-1">GCC</font> does not implement this model.</dl>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i> </p>
<p> These are the <code>-m</code> options defined for the Intel <font SIZE="-1">IA-64</font> architecture.</p>
<dl>
<dt><code>-mbig-endian</code></p>
<dd>Generate code for a big endian target. This is the default for <font SIZE="-1">HP-UX</font>.</p>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a little endian target. This is the default for <font SIZE="-1">AIX5</font> and GNU/Linux.</p>
<dt><code>-mgnu-as</code></p>
<dd>
<dt><code>-mno-gnu-as</code></p>
<dd>Generate (or don&#8217;t) code for the <font SIZE="-1">GNU</font> assembler. This is the default.</p>
<dt><code>-mgnu-ld</code></p>
<dd>
<dt><code>-mno-gnu-ld</code></p>
<dd>Generate (or don&#8217;t) code for the <font SIZE="-1">GNU</font> linker. This is the default.</p>
<dt><code>-mno-pic</code></p>
<dd>Generate code that does not use a global pointer register. The result is not position independent code, and violates the <font SIZE="-1">IA-64</font> <font SIZE="-1">ABI</font>.</p>
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
<dd>Generate code for inline divides of floating point values using the minimum latency algorithm.</p>
<dt><code>-minline-float-divide-max-throughput</code></p>
<dd>Generate code for inline divides of floating point values using the maximum throughput algorithm.</p>
<dt><code>-minline-int-divide-min-latency</code></p>
<dd>Generate code for inline divides of integer values using the minimum latency algorithm.</p>
<dt><code>-minline-int-divide-max-throughput</code></p>
<dd>Generate code for inline divides of integer values using the maximum throughput algorithm.</p>
<dt><code>-minline-sqrt-min-latency</code></p>
<dd>Generate code for inline square roots using the minimum latency algorithm.</p>
<dt><code>-minline-sqrt-max-throughput</code></p>
<dd>Generate code for inline square roots using the maximum throughput algorithm.</p>
<dt><code>-mno-dwarf2-asm</code></p>
<dd>
<dt><code>-mdwarf2-asm</code></p>
<dd>Don&#8217;t (or do) generate assembler code for the <font SIZE="-1">DWARF2</font> line number debugging info. This may be useful when not using the <font SIZE="-1">GNU</font> assembler.</p>
<dt><code>-mearly-stop-bits</code></p>
<dd>
<dt><code>-mno-early-stop-bits</code></p>
<dd>Allow stop bits to be placed earlier than immediately preceding the instruction that triggered the stop bit. This can improve instruction scheduling, but does not always do so.</p>
<dt><code>-mfixed-range=</code><i>register-range</i></p>
<dd>Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator can not use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma.</p>
<dt><code>-mtls-size=</code><i>tls-size</i></p>
<dd>Specify bit size of immediate <font SIZE="-1">TLS</font> offsets. Valid values are 14, 22, and 64.</p>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Tune the instruction scheduling for a particular <font SIZE="-1">CPU</font>, Valid values are itanium, itanium1, merced, itanium2, and mckinley.</p>
<dt><code>-mt</code></p>
<dd>
<dt><code>-pthread</code></p>
<dd>Add support for multithreading using the <font SIZE="-1">POSIX</font> threads library. This option sets flags for both the preprocessor and linker. It does not affect the thread safety of object code produced by the compiler or that of libraries supplied with it. These are HP-UX specific flags.</p>
<dt><code>-milp32</code></p>
<dd>
<dt><code>-mlp64</code></p>
<dd>Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits. These are HP-UX specific flags.</dl>
<p> <i>M32C Options</i></p>
<dl>
<dt><code>-mcpu=</code><i>name</i></p>
<dd>Select the <font SIZE="-1">CPU</font> for which code is generated. <i>name</i> may be one of <code>r8c</code> for the R8C/Tiny series, <code>m16c</code> for the M16C (up to /60) series, <code>m32cm</code> for the M16C/80 series, or <code>m32c</code> for the M32C/80 series.</p>
<dt><code>-msim</code></p>
<dd>Specifies that the program will be run on the simulator. This causes an alternate runtime library to be linked in which supports, for example, file I/O. You must not use this option when generating programs that will run on real hardware; you must provide your own runtime library for whatever I/O functions are needed.</p>
<dt><code>-memregs=</code><i>number</i></p>
<dd>Specifies the number of memory-based pseudo-registers <font SIZE="-1">GCC</font> will use during code generation. These pseudo-registers will be used like real registers, so there is a tradeoff between <font SIZE="-1">GCC</font>&#8216;s ability to fit the code into available registers, and the performance penalty of using memory instead of registers. Note that all modules in a program must be compiled with the same value for this option. Because of that, you must not use this option with the default runtime libraries gcc builds.</dl>
<p> <i>M32R/D Options</i> </p>
<p> These <code>-m</code> options are defined for Renesas M32R/D architectures:</p>
<dl>
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
<dd>Assume objects may be anywhere in the 32-bit address space (the compiler will generate <tt>&quot;seth/add3&quot;</tt> instructions to load their addresses), and assume all subroutines are reachable with the <tt>&quot;bl&quot;</tt> instruction.</p>
<dt><code>-mmodel=large</code></p>
<dd>Assume objects may be anywhere in the 32-bit address space (the compiler will generate <tt>&quot;seth/add3&quot;</tt> instructions to load their addresses), and assume subroutines may not be reachable with the <tt>&quot;bl&quot;</tt> instruction (the compiler will generate the much slower <tt>&quot;seth/add3/jl&quot;</tt> instruction sequence).</p>
<dt><code>-msdata=none</code></p>
<dd>Disable use of the small data area. Variables will be put into one of <code>.data</code>, <code>bss</code>, or <code>.rodata</code> (unless the <tt>&quot;section&quot;</tt> attribute has been specified). This is the default. </p>
<p> The small data area consists of sections <code>.sdata</code> and <code>.sbss</code>. Objects may be explicitly put in the small data area with the <tt>&quot;section&quot;</tt> attribute using one of these sections.</p>
<dt><code>-msdata=sdata</code></p>
<dd>Put small global and static data in the small data area, but do not generate special code to reference them.</p>
<dt><code>-msdata=use</code></p>
<dd>Put small global and static data in the small data area, and generate special instructions to reference them.</p>
<dt><code>-G</code> <i>num</i></p>
<dd>Put global and static objects less than or equal to <i>num</i> bytes into the small data or bss sections instead of the normal data or bss sections. The default value of <i>num</i> is 8. The <code>-msdata</code> option must be set to one of <code>sdata</code> or <code>use</code> for this option to have any effect. </p>
<p> All modules should be compiled with the same <code>-G</code> <i>num</i> value. Compiling with different values of <i>num</i> may or may not work; if it doesn&#8217;t the linker will give an error message&#8212;incorrect code will not be generated.</p>
<dt><code>-mdebug</code></p>
<dd>Makes the M32R specific code in the compiler display some statistics that might help in debugging programs.</p>
<dt><code>-malign-loops</code></p>
<dd>Align all loops to a 32-byte boundary.</p>
<dt><code>-mno-align-loops</code></p>
<dd>Do not enforce a 32-byte alignment for loops. This is the default.</p>
<dt><code>-missue-rate=</code><i>number</i></p>
<dd>Issue <i>number</i> instructions per cycle. <i>number</i> can only be 1 or 2.</p>
<dt><code>-mbranch-cost=</code><i>number</i></p>
<dd><i>number</i> can only be 1 or 2. If it is 1 then branches will be preferred over conditional code, if it is 2, then the opposite will apply.</p>
<dt><code>-mflush-trap=</code><i>number</i></p>
<dd>Specifies the trap number to use to flush the cache. The default is 12. Valid numbers are between 0 and 15 inclusive.</p>
<dt><code>-mno-flush-trap</code></p>
<dd>Specifies that the cache cannot be flushed by using a trap.</p>
<dt><code>-mflush-func=</code><i>name</i></p>
<dd>Specifies the name of the operating system function to call to flush the cache. The default is <i>_flush_cache</i>, but a function call will only be used if a trap is not available.</p>
<dt><code>-mno-flush-func</code></p>
<dd>Indicates that there is no <font SIZE="-1">OS</font> function for flushing the cache.</dl>
<p> <i>M680x0 Options</i> </p>
<p> These are the <code>-m</code> options defined for the 68000 series. The default values for these options depends on which style of 68000 was selected when the compiler was configured; the defaults for the most common choices are given below.</p>
<dl>
<dt><code>-m68000</code></p>
<dd>
<dt><code>-mc68000</code></p>
<dd>Generate output for a 68000. This is the default when the compiler is configured for 68000-based systems. </p>
<p> Use this option for microcontrollers with a 68000 or <font SIZE="-1">EC000</font> core, including the 68008, 68302, 68306, 68307, 68322, 68328 and 68356.</p>
<dt><code>-m68020</code></p>
<dd>
<dt><code>-mc68020</code></p>
<dd>Generate output for a 68020. This is the default when the compiler is configured for 68020-based systems.</p>
<dt><code>-m68881</code></p>
<dd>Generate output containing 68881 instructions for floating point. This is the default for most 68020 systems unless <code>&#8211;nfp</code> was specified when the compiler was configured.</p>
<dt><code>-m68030</code></p>
<dd>Generate output for a 68030. This is the default when the compiler is configured for 68030-based systems.</p>
<dt><code>-m68040</code></p>
<dd>Generate output for a 68040. This is the default when the compiler is configured for 68040-based systems. </p>
<p> This option inhibits the use of 68881/68882 instructions that have to be emulated by software on the 68040. Use this option if your 68040 does not have code to emulate those instructions.</p>
<dt><code>-m68060</code></p>
<dd>Generate output for a 68060. This is the default when the compiler is configured for 68060-based systems. </p>
<p> This option inhibits the use of 68020 and 68881/68882 instructions that have to be emulated by software on the 68060. Use this option if your 68060 does not have code to emulate those instructions.</p>
<dt><code>-mcpu32</code></p>
<dd>Generate output for a <font SIZE="-1">CPU32</font>. This is the default when the compiler is configured for CPU32-based systems. </p>
<p> Use this option for microcontrollers with a <font SIZE="-1">CPU32</font> or <font SIZE="-1">CPU32+</font> core, including the 68330, 68331, 68332, 68333, 68334, 68336, 68340, 68341, 68349 and 68360.</p>
<dt><code>-m5200</code></p>
<dd>Generate output for a 520X &#8220;coldfire&#8221; family cpu. This is the default when the compiler is configured for 520X-based systems. </p>
<p> Use this option for microcontroller with a 5200 core, including the <font SIZE="-1">MCF5202</font>, <font SIZE="-1">MCF5203</font>, <font SIZE="-1">MCF5204</font> and <font SIZE="-1">MCF5202</font>.</p>
<dt><code>-m68020-40</code></p>
<dd>Generate output for a 68040, without using any of the new instructions. This results in code which can run relatively efficiently on either a 68020/68881 or a 68030 or a 68040. The generated code does use the 68881 instructions that are emulated on the 68040.</p>
<dt><code>-m68020-60</code></p>
<dd>Generate output for a 68060, without using any of the new instructions. This results in code which can run relatively efficiently on either a 68020/68881 or a 68030 or a 68040. The generated code does use the 68881 instructions that are emulated on the 68060.</p>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all m68k targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded targets <code>m68k-*-aout</code> and <code>m68k-*-coff</code> do provide software floating point support.</p>
<dt><code>-mshort</code></p>
<dd>Consider type <tt>&quot;int&quot;</tt> to be 16 bits wide, like <tt>&quot;short int&quot;</tt>. Additionally, parameters passed on the stack are also aligned to a 16-bit boundary even on targets whose <font SIZE="-1">API</font> mandates promotion to 32-bit.</p>
<dt><code>-mnobitfield</code></p>
<dd>Do not use the bit-field instructions. The <code>-m68000</code>, <code>-mcpu32</code> and <code>-m5200</code> options imply <code>-mnobitfield</code>.</p>
<dt><code>-mbitfield</code></p>
<dd>Do use the bit-field instructions. The <code>-m68020</code> option implies <code>-mbitfield</code>. This is the default if you use a configuration designed for a 68020.</p>
<dt><code>-mrtd</code></p>
<dd>Use a different function-calling convention, in which functions that take a fixed number of arguments return with the <tt>&quot;rtd&quot;</tt> instruction, which pops their arguments while returning. This saves one instruction in the caller since there is no need to pop the arguments there. </p>
<p> This calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <tt>&quot;printf&quot;</tt>); otherwise incorrect code will be generated for calls to those functions. </p>
<p> In addition, seriously incorrect code will result if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.) </p>
<p> The <tt>&quot;rtd&quot;</tt> instruction is supported by the 68010, 68020, 68030, 68040, 68060 and <font SIZE="-1">CPU32</font> processors, but not by the 68000 or 5200.</p>
<dt><code>-malign-int</code></p>
<dd>
<dt><code>-mno-align-int</code></p>
<dd>Control whether <font SIZE="-1">GCC</font> aligns <tt>&quot;int&quot;</tt>, <tt>&quot;long&quot;</tt>, <tt>&quot;long long&quot;</tt>, <tt>&quot;float&quot;</tt>, <tt>&quot;double&quot;</tt>, and <tt>&quot;long double&quot;</tt> variables on a 32-bit boundary (<code>-malign-int</code>) or a 16-bit boundary (<code>-mno-align-int</code>). Aligning variables on 32-bit boundaries produces code that runs somewhat faster on processors with 32-bit busses at the expense of more memory. </p>
<p> <code>Warning:</code> if you use the <code>-malign-int</code> switch, <font SIZE="-1">GCC</font> will align structures containing the above types differently than most published application binary interface specifications for the m68k.</p>
<dt><code>-mpcrel</code></p>
<dd>Use the pc-relative addressing mode of the 68000 directly, instead of using a global offset table. At present, this option implies <code>-fpic</code>, allowing at most a 16-bit offset for pc-relative addressing. <code>-fPIC</code> is not presently supported with <code>-mpcrel</code>, though this could be supported for 68020 and higher processors.</p>
<dt><code>-mno-strict-align</code></p>
<dd>
<dt><code>-mstrict-align</code></p>
<dd>Do not (do) assume that unaligned memory references will be handled by the system.</p>
<dt><code>-msep-data</code></p>
<dd>Generate code that allows the data segment to be located in a different area of memory from the text segment. This allows for execute in place in an environment without virtual memory management. This option implies <code>-fPIC</code>.</p>
<dt><code>-mno-sep-data</code></p>
<dd>Generate code that assumes that the data segment follows the text segment. This is the default.</p>
<dt><code>-mid-shared-library</code></p>
<dd>Generate code that supports shared libraries via the library <font SIZE="-1">ID</font> method. This allows for execute in place and shared libraries in an environment without virtual memory management. This option implies <code>-fPIC</code>.</p>
<dt><code>-mno-id-shared-library</code></p>
<dd>Generate code that doesn&#8217;t assume <font SIZE="-1">ID</font> based shared libraries are being used. This is the default.</p>
<dt><code>-mshared-library-id=n</code></p>
<dd>Specified the identification number of the <font SIZE="-1">ID</font> based shared library being compiled. Specifying a value of 0 will generate more compact code, specifying other values will force the allocation of that number to the current library but is no more space or time efficient than omitting this option.</dl>
<p> <i>M68hc1x Options</i> </p>
<p> These are the <code>-m</code> options defined for the 68hc11 and 68hc12 microcontrollers. The default values for these options depends on which style of microcontroller was selected when the compiler was configured; the defaults for the most common choices are given below.</p>
<dl>
<dt><code>-m6811</code></p>
<dd>
<dt><code>-m68hc11</code></p>
<dd>Generate output for a 68HC11. This is the default when the compiler is configured for 68HC11-based systems.</p>
<dt><code>-m6812</code></p>
<dd>
<dt><code>-m68hc12</code></p>
<dd>Generate output for a 68HC12. This is the default when the compiler is configured for 68HC12-based systems.</p>
<dt><code>-m68S12</code></p>
<dd>
<dt><code>-m68hcs12</code></p>
<dd>Generate output for a 68HCS12.</p>
<dt><code>-mauto-incdec</code></p>
<dd>Enable the use of 68HC12 pre and post auto-increment and auto-decrement addressing modes.</p>
<dt><code>-minmax</code></p>
<dd>
<dt><code>-nominmax</code></p>
<dd>Enable the use of 68HC12 min and max instructions.</p>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Treat all calls as being far away (near). If calls are assumed to be far away, the compiler will use the <tt>&quot;call&quot;</tt> instruction to call a function and the <tt>&quot;rtc&quot;</tt> instruction for returning.</p>
<dt><code>-mshort</code></p>
<dd>Consider type <tt>&quot;int&quot;</tt> to be 16 bits wide, like <tt>&quot;short int&quot;</tt>.</p>
<dt><code>-msoft-reg-count=</code><i>count</i></p>
<dd>Specify the number of pseudo-soft registers which are used for the code generation. The maximum number is 32. Using more pseudo-soft register may or may not result in better code depending on the program. The default is 4 for 68HC11 and 2 for 68HC12.</dl>
<p> <i>MCore Options</i> </p>
<p> These are the <code>-m</code> options defined for the Motorola M*Core processors.</p>
<dl>
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
<dd>Allow arbitrary sized immediates in bit operations.</p>
<dt><code>-mwide-bitfields</code></p>
<dd>
<dt><code>-mno-wide-bitfields</code></p>
<dd>Always treat bit-fields as int-sized.</p>
<dt><code>-m4byte-functions</code></p>
<dd>
<dt><code>-mno-4byte-functions</code></p>
<dd>Force all functions to be aligned to a four byte boundary.</p>
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
<dd>Generate code for a little endian target.</p>
<dt><code>-m210</code></p>
<dd>
<dt><code>-m340</code></p>
<dd>Generate code for the 210 processor.</dl>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i></p>
<dl>
<dt><code>-EB</code></p>
<dd>Generate big-endian code.</p>
<dt><code>-EL</code></p>
<dd>Generate little-endian code. This is the default for <code>mips*el-*-*</code> configurations.</p>
<dt><code>-march=</code><i>arch</i></p>
<dd>Generate code that will run on <i>arch</i>, which can be the name of a generic <font SIZE="-1">MIPS</font> <font SIZE="-1">ISA</font>, or the name of a particular processor. The <font SIZE="-1">ISA</font> names are: <code>mips1</code>, <code>mips2</code>, <code>mips3</code>, <code>mips4</code>, <code>mips32</code>, <code>mips32r2</code>, and <code>mips64</code>. The processor names are: <code>4kc</code>, <code>4km</code>, <code>4kp</code>, <code>5kc</code>, <code>5kf</code>, <code>20kc</code>, <code>24k</code>, <code>24kc</code>, <code>24kf</code>, <code>24kx</code>, <code>m4k</code>, <code>orion</code>, <code>r2000</code>, <code>r3000</code>, <code>r3900</code>, <code>r4000</code>, <code>r4400</code>, <code>r4600</code>, <code>r4650</code>, <code>r6000</code>, <code>r8000</code>, <code>rm7000</code>, <code>rm9000</code>, <code>sb1</code>, <code>sr71000</code>, <code>vr4100</code>, <code>vr4111</code>, <code>vr4120</code>, <code>vr4130</code>, <code>vr4300</code>, <code>vr5000</code>, <code>vr5400</code> and <code>vr5500</code>. The special value <code>from-abi</code> selects the most compatible architecture for the selected <font SIZE="-1">ABI</font> (that is, <code>mips1</code> for 32-bit ABIs and <code>mips3</code> for 64-bit ABIs). </p>
<p> In processor names, a final <code>000</code> can be abbreviated as <code>k</code> (for example, <code>-march=r2k</code>). Prefixes are optional, and <code>vr</code> may be written <code>r</code>. </p>
<p> <font SIZE="-1">GCC</font> defines two macros based on the value of this option. The first is <code>_MIPS_ARCH</code>, which gives the name of target architecture, as a string. The second has the form <code>_MIPS_ARCH_</code><i>foo</i>, where <i>foo</i> is the capitalized value of <code>_MIPS_ARCH</code>. For example, <code>-march=r2000</code> will set <code>_MIPS_ARCH</code> to <code>&#8220;r2000&#8221;</code> and define the macro <code>_MIPS_ARCH_R2000</code>. </p>
<p> Note that the <code>_MIPS_ARCH</code> macro uses the processor names given above. In other words, it will have the full prefix and will not abbreviate <code>000</code> as <code>k</code>. In the case of <code>from-abi</code>, the macro names the resolved architecture (either <code>&#8220;mips1&#8221;</code> or <code>&#8220;mips3&#8221;</code>). It names the default architecture when no <code>-march</code> option is given.</p>
<dt><code>-mtune=</code><i>arch</i></p>
<dd>Optimize for <i>arch</i>. Among other things, this option controls the way instructions are scheduled, and the perceived cost of arithmetic operations. The list of <i>arch</i> values is the same as for <code>-march</code>. </p>
<p> When this option is not used, <font SIZE="-1">GCC</font> will optimize for the processor specified by <code>-march</code>. By using <code>-march</code> and <code>-mtune</code> together, it is possible to generate code that will run on a family of processors, but optimize the code for one particular member of that family. </p>
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
<dt><code>-mips16</code></p>
<dd>
<dt><code>-mno-mips16</code></p>
<dd>Generate (do not generate) <font SIZE="-1">MIPS16</font> code. If <font SIZE="-1">GCC</font> is targetting a <font SIZE="-1">MIPS32</font> or <font SIZE="-1">MIPS64</font> architecture, it will make use of the MIPS16e <font SIZE="-1">ASE</font>.</p>
<dt><code>-mabi=32</code></p>
<dd>
<dt><code>-mabi=o64</code></p>
<dd>
<dt><code>-mabi=n32</code></p>
<dd>
<dt><code>-mabi=64</code></p>
<dd>
<dt><code>-mabi=eabi</code></p>
<dd>Generate code for the given <font SIZE="-1">ABI</font>. </p>
<p> Note that the <font SIZE="-1">EABI</font> has a 32-bit and a 64-bit variant. <font SIZE="-1">GCC</font> normally generates 64-bit code when you select a 64-bit architecture, but you can use <code>-mgp32</code> to get 32-bit code instead. </p>
<p> For information about the O64 <font SIZE="-1">ABI</font>, see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/projects/mipso64-abi.html">http://gcc.gnu.org/projects/mipso64-abi.html</a></code>&gt;.</p>
<dt><code>-mabicalls</code></p>
<dd>
<dt><code>-mno-abicalls</code></p>
<dd>Generate (do not generate) SVR4-style position-independent code. <code>-mabicalls</code> is the default for SVR4-based systems.</p>
<dt><code>-mxgot</code></p>
<dd>
<dt><code>-mno-xgot</code></p>
<dd>Lift (do not lift) the usual restrictions on the size of the global offset table. </p>
<p> <font SIZE="-1">GCC</font> normally uses a single instruction to load values from the <font SIZE="-1">GOT</font>. While this is relatively efficient, it will only work if the <font SIZE="-1">GOT</font> is smaller than about 64k. Anything larger will cause the linker to report an error such as: </p>
<pre> relocation truncated to fit: R_MIPS_GOT16 foobar</pre>
<p>If this happens, you should recompile your code with <code>-mxgot</code>. It should then work with very large GOTs, although it will also be less efficient, since it will take three instructions to fetch the value of a global symbol. </p>
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
<dt><code>-msingle-float</code></p>
<dd>Assume that the floating-point coprocessor only supports single-precision operations.</p>
<dt><code>-mdouble-float</code></p>
<dd>Assume that the floating-point coprocessor supports double-precision operations. This is the default.</p>
<dt><code>-mdsp</code></p>
<dd>
<dt><code>-mno-dsp</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS</font> <font SIZE="-1">DSP</font> <font SIZE="-1">ASE</font>.</p>
<dt><code>-mpaired-single</code></p>
<dd>
<dt><code>-mno-paired-single</code></p>
<dd>Use (do not use) paired-single floating-point instructions.<br />
&nbsp;<wbr>&nbsp;<wbr>This option can only be used when generating 64-bit code and requires hardware floating-point support to be enabled.</p>
<dt><code>-mips3d</code></p>
<dd>
<dt><code>-mno-mips3d</code></p>
<dd>Use (do not use) the <font SIZE="-1">MIPS-3D</font> <font SIZE="-1">ASE</font>. The option <code>-mips3d</code> implies <code>-mpaired-single</code>.</p>
<dt><code>-mlong64</code></p>
<dd>Force <tt>&quot;long&quot;</tt> types to be 64 bits wide. See <code>-mlong32</code> for an explanation of the default and the way that the pointer size is determined.</p>
<dt><code>-mlong32</code></p>
<dd>Force <tt>&quot;long&quot;</tt>, <tt>&quot;int&quot;</tt>, and pointer types to be 32 bits wide. </p>
<p> The default size of <tt>&quot;int&quot;</tt>s, <tt>&quot;long&quot;</tt>s and pointers depends on the <font SIZE="-1">ABI</font>. All the supported ABIs use 32-bit <tt>&quot;int&quot;</tt>s. The n64 <font SIZE="-1">ABI</font> uses 64-bit <tt>&quot;long&quot;</tt>s, as does the 64-bit <font SIZE="-1">EABI</font>; the others use 32-bit <tt>&quot;long&quot;</tt>s. Pointers are the same size as <tt>&quot;long&quot;</tt>s, or the same size as integer registers, whichever is smaller.</p>
<dt><code>-msym32</code></p>
<dd>
<dt><code>-mno-sym32</code></p>
<dd>Assume (do not assume) that all symbols have 32-bit values, regardless of the selected <font SIZE="-1">ABI</font>. This option is useful in combination with <code>-mabi=64</code> and <code>-mno-abicalls</code> because it allows <font SIZE="-1">GCC</font> to generate shorter and faster references to symbolic addresses.</p>
<dt><code>-G</code> <i>num</i></p>
<dd>Put global and static items less than or equal to <i>num</i> bytes into the small data or bss section instead of the normal data or bss section. This allows the data to be accessed using a single instruction. </p>
<p> All modules should be compiled with the same <code>-G</code> <i>num</i> value.</p>
<dt><code>-membedded-data</code></p>
<dd>
<dt><code>-mno-embedded-data</code></p>
<dd>Allocate variables to the read-only data section first if possible, then next in the small data section if possible, otherwise in data. This gives slightly slower code than the default, but reduces the amount of <font SIZE="-1">RAM</font> required when executing, and thus may be preferred for some embedded systems.</p>
<dt><code>-muninit-const-in-rodata</code></p>
<dd>
<dt><code>-mno-uninit-const-in-rodata</code></p>
<dd>Put uninitialized <tt>&quot;const&quot;</tt> variables in the read-only data section. This option is only meaningful in conjunction with <code>-membedded-data</code>.</p>
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
<dd>Trap (do not trap) on integer division by zero. The default is <code>-mcheck-zero-division</code>.</p>
<dt><code>-mdivide-traps</code></p>
<dd>
<dt><code>-mdivide-breaks</code></p>
<dd><font SIZE="-1">MIPS</font> systems check for division by zero by generating either a conditional trap or a break instruction. Using traps results in smaller code, but is only supported on <font SIZE="-1">MIPS</font> <font SIZE="-1">II</font> and later. Also, some versions of the Linux kernel have a bug that prevents trap from generating the proper signal (<tt>&quot;SIGFPE&quot;</tt>). Use <code>-mdivide-traps</code> to allow conditional traps on architectures that support them and <code>-mdivide-breaks</code> to force the use of breaks. </p>
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
<dd>Enable (disable) use of the <tt>&quot;mad&quot;</tt>, <tt>&quot;madu&quot;</tt> and <tt>&quot;mul&quot;</tt> instructions, as provided by the R4650 <font SIZE="-1">ISA</font>.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Enable (disable) use of the floating point multiply-accumulate instructions, when they are available. The default is <code>-mfused-madd</code>. </p>
<p> When multiply-accumulate instructions are used, the intermediate product is calculated to infinite precision and is not subject to the <font SIZE="-1">FCSR</font> Flush to Zero bit. This may be undesirable in some circumstances.</p>
<dt><code>-nocpp</code></p>
<dd>Tell the <font SIZE="-1">MIPS</font> assembler to not run its preprocessor over user assembler files (with a <code>.s</code> suffix) when assembling them.</p>
<dt><code>-mfix-r4000</code></p>
<dd>
<dt><code>-mno-fix-r4000</code></p>
<dd>Work around certain R4000 <font SIZE="-1">CPU</font> errata:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>A double-word or a variable shift may give an incorrect result if executed immediately after starting an integer division.</p>
<dt>&#8211;</p>
<dd>A double-word or a variable shift may give an incorrect result if executed while an integer multiplication is in progress.</p>
<dt>&#8211;</p>
<dd>An integer division may give an incorrect result if started in a delay slot of a taken branch or a jump.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-mfix-r4400</code></p>
<dd>
<dt><code>-mno-fix-r4400</code></p>
<dd>Work around certain R4400 <font SIZE="-1">CPU</font> errata:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>A double-word or a variable shift may give an incorrect result if executed immediately after starting an integer division.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-mfix-vr4120</code></p>
<dd>
<dt><code>-mno-fix-vr4120</code></p>
<dd>Work around certain <font SIZE="-1">VR4120</font> errata:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd><tt>&quot;dmultu&quot;</tt> does not always produce the correct result.</p>
<dt>&#8211;</p>
<dd><tt>&quot;div&quot;</tt> and <tt>&quot;ddiv&quot;</tt> do not always produce the correct result if one of the operands is negative.</dl>
</dl>
<dl>
<dd>The workarounds for the division errata rely on special functions in <i>libgcc.a</i>. At present, these functions are only provided by the <tt>&quot;mips64vr*-elf&quot;</tt> configurations. </p>
<p> Other <font SIZE="-1">VR4120</font> errata require a nop to be inserted between certain pairs of instructions. These errata are handled by the assembler, not by <font SIZE="-1">GCC</font> itself.</dl>
<dt><code>-mfix-vr4130</code></p>
<dd>Work around the <font SIZE="-1">VR4130</font> <tt>&quot;mflo&quot;</tt>/<tt>&quot;mfhi&quot;</tt> errata. The workarounds are implemented by the assembler rather than by <font SIZE="-1">GCC</font>, although <font SIZE="-1">GCC</font> will avoid using <tt>&quot;mflo&quot;</tt> and <tt>&quot;mfhi&quot;</tt> if the <font SIZE="-1">VR4130</font> <tt>&quot;macc&quot;</tt>, <tt>&quot;macchi&quot;</tt>, <tt>&quot;dmacc&quot;</tt> and <tt>&quot;dmacchi&quot;</tt> instructions are available instead.</p>
<dt><code>-mfix-sb1</code></p>
<dd>
<dt><code>-mno-fix-sb1</code></p>
<dd>Work around certain <font SIZE="-1">SB-1</font> <font SIZE="-1">CPU</font> core errata. (This flag currently works around the <font SIZE="-1">SB-1</font> revision 2 &#8220;F1&#8221; and &#8220;F2&#8221; floating point errata.)</p>
<dt><code>-mflush-func=</code><i>func</i></p>
<dd>
<dt><code>-mno-flush-func</code></p>
<dd>Specifies the function to call to flush the I and D caches, or to not call any such function. If called, the function must take the same arguments as the common <tt>&quot;_flush_func()&quot;</tt>, that is, the address of the memory range for which the cache is being flushed, the size of the memory range, and the number 3 (to flush both caches). The default depends on the target <font SIZE="-1">GCC</font> was configured for, but commonly is either <code>_flush_func</code> or <code>__cpu_flush</code>.</p>
<dt><code>-mbranch-likely</code></p>
<dd>
<dt><code>-mno-branch-likely</code></p>
<dd>Enable or disable use of Branch Likely instructions, regardless of the default for the selected architecture. By default, Branch Likely instructions may be generated if they are supported by the selected architecture. An exception is for the <font SIZE="-1">MIPS32</font> and <font SIZE="-1">MIPS64</font> architectures and processors which implement those architectures; for those, Branch Likely instructions will not be generated by default because the <font SIZE="-1">MIPS32</font> and <font SIZE="-1">MIPS64</font> architectures specifically deprecate their use.</p>
<dt><code>-mfp-exceptions</code></p>
<dd>
<dt><code>-mno-fp-exceptions</code></p>
<dd>Specifies whether <font SIZE="-1">FP</font> exceptions are enabled. This affects how we schedule <font SIZE="-1">FP</font> instructions for some processors. The default is that <font SIZE="-1">FP</font> exceptions are enabled. </p>
<p> For instance, on the <font SIZE="-1">SB-1</font>, if <font SIZE="-1">FP</font> exceptions are disabled, and we are emitting 64-bit code, then we can use both <font SIZE="-1">FP</font> pipes. Otherwise, we can only use one <font SIZE="-1">FP</font> pipe.</p>
<dt><code>-mvr4130-align</code></p>
<dd>
<dt><code>-mno-vr4130-align</code></p>
<dd>The <font SIZE="-1">VR4130</font> pipeline is two-way superscalar, but can only issue two instructions together if the first one is 8-byte aligned. When this option is enabled, <font SIZE="-1">GCC</font> will align pairs of instructions that it thinks should execute in parallel. </p>
<p> This option only has an effect when optimizing for the <font SIZE="-1">VR4130</font>. It normally makes code faster, but at the expense of making it bigger. It is enabled by default at optimization level <code>-O3</code>.</dl>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i> </p>
<p> These options are defined for the <font SIZE="-1">MMIX:</font></p>
<dl>
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
<dd>Generate code that passes function parameters and return values that (in the called function) are seen as registers <tt>$0</tt> and up, as opposed to the <font SIZE="-1">GNU</font> <font SIZE="-1">ABI</font> which uses global registers <tt>$231</tt> and up.</p>
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
<dl>
<dt><code>-mmult-bug</code></p>
<dd>Generate code to avoid bugs in the multiply instructions for the <font SIZE="-1">MN10300</font> processors. This is the default.</p>
<dt><code>-mno-mult-bug</code></p>
<dd>Do not generate code to avoid bugs in the multiply instructions for the <font SIZE="-1">MN10300</font> processors.</p>
<dt><code>-mam33</code></p>
<dd>Generate code which uses features specific to the <font SIZE="-1">AM33</font> processor.</p>
<dt><code>-mno-am33</code></p>
<dd>Do not generate code which uses features specific to the <font SIZE="-1">AM33</font> processor. This is the default.</p>
<dt><code>-mreturn-pointer-on-d0</code></p>
<dd>When generating a function which returns a pointer, return the pointer in both <tt>&quot;a0&quot;</tt> and <tt>&quot;d0&quot;</tt>. Otherwise, the pointer is returned only in a0, and attempts to call such functions without a prototype would result in errors. Note that this option is on by default; use <code>-mno-return-pointer-on-d0</code> to disable it.</p>
<dt><code>-mno-crt0</code></p>
<dd>Do not link in the C run-time initialization object file.</p>
<dt><code>-mrelax</code></p>
<dd>Indicate to the linker that it should perform a relaxation optimization pass to shorten branches, calls and absolute memory addresses. This option only has an effect when used on the command line for the final link step. </p>
<p> This option makes symbolic debugging impossible.</dl>
<p> <i></i><font SIZE="-1"><i>MT</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for Morpho <font SIZE="-1">MT</font> architectures:</p>
<dl>
<dt><code>-march=</code><i>cpu-type</i></p>
<dd>Generate code that will run on <i>cpu-type</i>, which is the name of a system representing a certain processor type. Possible values for <i>cpu-type</i> are <code>ms1-64-001</code>, <code>ms1-16-002</code>, <code>ms1-16-003</code> and <code>ms2</code>. </p>
<p> When this option is not used, the default is <code>-march=ms1-16-002</code>.</p>
<dt><code>-mbacc</code></p>
<dd>Use byte loads and stores when generating code.</p>
<dt><code>-mno-bacc</code></p>
<dd>Do not use byte loads and stores when generating code.</p>
<dt><code>-msim</code></p>
<dd>Use simulator runtime</p>
<dt><code>-mno-crt0</code></p>
<dd>Do not link in the C run-time initialization object file <i>crti.o</i>. Other run-time initialization and termination files such as <i>startup.o</i> and <i>exit.o</i> are still included on the linker command line.</dl>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i> </p>
<p> These options are defined for the <font SIZE="-1">PDP-11:</font></p>
<dl>
<dt><code>-mfpu</code></p>
<dd>Use hardware <font SIZE="-1">FPP</font> floating point. This is the default. (<font SIZE="-1">FIS</font> floating point on the <font SIZE="-1">PDP-11/40</font> is not supported.)</p>
<dt><code>-msoft-float</code></p>
<dd>Do not use hardware floating point.</p>
<dt><code>-mac0</code></p>
<dd>Return floating-point results in ac0 (fr0 in Unix assembler syntax).</p>
<dt><code>-mno-ac0</code></p>
<dd>Return floating-point results in memory. This is the default.</p>
<dt><code>-m40</code></p>
<dd>Generate code for a <font SIZE="-1">PDP-11/40</font>.</p>
<dt><code>-m45</code></p>
<dd>Generate code for a <font SIZE="-1">PDP-11/45</font>. This is the default.</p>
<dt><code>-m10</code></p>
<dd>Generate code for a <font SIZE="-1">PDP-11/10</font>.</p>
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
<dt><code>-msplit</code></p>
<dd>Generate code for a system with split I&amp;D.</p>
<dt><code>-mno-split</code></p>
<dd>Generate code for a system without split I&amp;D. This is the default.</p>
<dt><code>-munix-asm</code></p>
<dd>Use Unix assembler syntax. This is the default when configured for <code>pdp11-*-bsd</code>.</p>
<dt><code>-mdec-asm</code></p>
<dd>Use <font SIZE="-1">DEC</font> assembler syntax. This is the default when configured for any <font SIZE="-1">PDP-11</font> target other than <code>pdp11-*-bsd</code>.</dl>
<p> <i>PowerPC Options</i> </p>
<p> These are listed under </p>
<p> <i></i><font SIZE="-1"><i>IBM</i></font><i> </i><font SIZE="-1"><i>RS/6000</i></font><i> and PowerPC Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">IBM</font> <font SIZE="-1">RS/6000</font> and PowerPC:</p>
<dl>
<dt><code>-mpower</code></p>
<dd>
<dt><code>-mno-power</code></p>
<dd>
<dt><code>-mpower2</code></p>
<dd>
<dt><code>-mno-power2</code></p>
<dd>
<dt><code>-mpowerpc</code></p>
<dd>
<dt><code>-mno-powerpc</code></p>
<dd>
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
<dt><code>-mfprnd</code></p>
<dd>
<dt><code>-mno-fprnd</code></p>
<dd><font SIZE="-1">GCC</font> supports two related instruction set architectures for the <font SIZE="-1">RS/6000</font> and PowerPC. The <i></i><font SIZE="-1"><i>POWER</i></font><i></i> instruction set are those instructions supported by the <code>rios</code> chip set used in the original <font SIZE="-1">RS/6000</font> systems and the <i>PowerPC</i> instruction set is the architecture of the Freescale MPC5xx, MPC6xx, MPC8xx microprocessors, and the <font SIZE="-1">IBM</font> 4xx, 6xx, and follow-on microprocessors. </p>
<p> Neither architecture is a subset of the other. However there is a large common subset of instructions supported by both. An <font SIZE="-1">MQ</font> register is included in processors supporting the <font SIZE="-1">POWER</font> architecture. </p>
<p> You use these options to specify which instructions are available on the processor you are using. The default value of these options is determined when configuring <font SIZE="-1">GCC</font>. Specifying the <code>-mcpu=</code><i>cpu_type</i> overrides the specification of these options. We recommend you use the <code>-mcpu=</code><i>cpu_type</i> option rather than the options listed above. </p>
<p> The <code>-mpower</code> option allows <font SIZE="-1">GCC</font> to generate instructions that are found only in the <font SIZE="-1">POWER</font> architecture and to use the <font SIZE="-1">MQ</font> register. Specifying <code>-mpower2</code> implies <code>-power</code> and also allows <font SIZE="-1">GCC</font> to generate instructions that are present in the <font SIZE="-1">POWER2</font> architecture but not the original <font SIZE="-1">POWER</font> architecture. </p>
<p> The <code>-mpowerpc</code> option allows <font SIZE="-1">GCC</font> to generate instructions that are found only in the 32-bit subset of the PowerPC architecture. Specifying <code>-mpowerpc-gpopt</code> implies <code>-mpowerpc</code> and also allows <font SIZE="-1">GCC</font> to use the optional PowerPC architecture instructions in the General Purpose group, including floating-point square root. Specifying <code>-mpowerpc-gfxopt</code> implies <code>-mpowerpc</code> and also allows <font SIZE="-1">GCC</font> to use the optional PowerPC architecture instructions in the Graphics group, including floating-point select. </p>
<p> The <code>-mmfcrf</code> option allows <font SIZE="-1">GCC</font> to generate the move from condition register field instruction implemented on the <font SIZE="-1">POWER4</font> processor and other processors that support the PowerPC V2.01 architecture. The <code>-mpopcntb</code> option allows <font SIZE="-1">GCC</font> to generate the popcount and double precision <font SIZE="-1">FP</font> reciprocal estimate instruction implemented on the <font SIZE="-1">POWER5</font> processor and other processors that support the PowerPC V2.02 architecture. The <code>-mfprnd</code> option allows <font SIZE="-1">GCC</font> to generate the <font SIZE="-1">FP</font> round to integer instructions implemented on the <font SIZE="-1">POWER5+</font> processor and other processors that support the PowerPC V2.03 architecture. </p>
<p> The <code>-mpowerpc64</code> option allows <font SIZE="-1">GCC</font> to generate the additional 64-bit instructions that are found in the full PowerPC64 architecture and to treat GPRs as 64-bit, doubleword quantities. <font SIZE="-1">GCC</font> defaults to <code>-mno-powerpc64</code>. </p>
<p> If you specify both <code>-mno-power</code> and <code>-mno-powerpc</code>, <font SIZE="-1">GCC</font> will use only the instructions in the common subset of both architectures plus some special <font SIZE="-1">AIX</font> common-mode calls, and will not use the <font SIZE="-1">MQ</font> register. Specifying both <code>-mpower</code> and <code>-mpowerpc</code> permits <font SIZE="-1">GCC</font> to use any instruction from either architecture and to allow use of the <font SIZE="-1">MQ</font> register; specify this for the Motorola <font SIZE="-1">MPC601</font>.</p>
<dt><code>-mnew-mnemonics</code></p>
<dd>
<dt><code>-mold-mnemonics</code></p>
<dd>Select which mnemonics to use in the generated assembler code. With <code>-mnew-mnemonics</code>, <font SIZE="-1">GCC</font> uses the assembler mnemonics defined for the PowerPC architecture. With <code>-mold-mnemonics</code> it uses the assembler mnemonics defined for the <font SIZE="-1">POWER</font> architecture. Instructions defined in only one architecture have only one mnemonic; <font SIZE="-1">GCC</font> uses that mnemonic irrespective of which of these options is specified. </p>
<p> <font SIZE="-1">GCC</font> defaults to the mnemonics appropriate for the architecture in use. Specifying <code>-mcpu=</code><i>cpu_type</i> sometimes overrides the value of these option. Unless you are building a cross-compiler, you should normally not specify either <code>-mnew-mnemonics</code> or <code>-mold-mnemonics</code>, but should instead accept the default.</p>
<dt><code>-mcpu=</code><i>cpu_type</i></p>
<dd>Set architecture type, register usage, choice of mnemonics, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>401</code>, <code>403</code>, <code>405</code>, <code>405fp</code>, <code>440</code>, <code>440fp</code>, <code>505</code>, <code>601</code>, <code>602</code>, <code>603</code>, <code>603e</code>, <code>604</code>, <code>604e</code>, <code>620</code>, <code>630</code>, <code>740</code>, <code>7400</code>, <code>7450</code>, <code>750</code>, <code>801</code>, <code>821</code>, <code>823</code>, <code>860</code>, <code>970</code>, <code>8540</code>, <code>ec603e</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>power</code>, <code>power2</code>, <code>power3</code>, <code>power4</code>, <code>power5</code>, <code>power5+</code>, <code>power6</code>, <code>common</code>, <code>powerpc</code>, <code>powerpc64</code>, <code>rios</code>, <code>rios1</code>, <code>rios2</code>, <code>rsc</code>, and <code>rs64</code>. </p>
<p> <code>-mcpu=common</code> selects a completely generic processor. Code generated under this option will run on any <font SIZE="-1">POWER</font> or PowerPC processor. <font SIZE="-1">GCC</font> will use only the instructions in the common subset of both architectures, and will not use the <font SIZE="-1">MQ</font> register. <font SIZE="-1">GCC</font> assumes a generic processor model for scheduling purposes. </p>
<p> <code>-mcpu=power</code>, <code>-mcpu=power2</code>, <code>-mcpu=powerpc</code>, and <code>-mcpu=powerpc64</code> specify generic <font SIZE="-1">POWER</font>, <font SIZE="-1">POWER2</font>, pure 32-bit PowerPC (i.e., not <font SIZE="-1">MPC601</font>), and 64-bit PowerPC architecture machine types, with an appropriate, generic processor model assumed for scheduling purposes. </p>
<p> The other options specify a specific processor. Code generated under those options will run best on that processor, and may not run at all on others. </p>
<p> The <code>-mcpu</code> options automatically enable or disable the following options: <code>-maltivec</code>, <code>-mfprnd</code>, <code>-mhard-float</code>, <code>-mmfcrf</code>, <code>-mmultiple</code>, <code>-mnew-mnemonics</code>, <code>-mpopcntb</code>, <code>-mpower</code>, <code>-mpower2</code>, <code>-mpowerpc64</code>, <code>-mpowerpc-gpopt</code>, <code>-mpowerpc-gfxopt</code>, <code>-mstring</code>. The particular options set for any particular <font SIZE="-1">CPU</font> will vary between compiler versions, depending on what setting seems to produce optimal code for that <font SIZE="-1">CPU</font>; it doesn&#8217;t necessarily reflect the actual hardware&#8217;s capabilities. If you wish to set an individual option to a particular value, you may specify it after the <code>-mcpu</code> option, like <code>-mcpu=970 -mno-altivec</code>. </p>
<p> On <font SIZE="-1">AIX</font>, the <code>-maltivec</code> and <code>-mpowerpc64</code> options are not enabled or disabled by the <code>-mcpu</code> option at present because <font SIZE="-1">AIX</font> does not have full support for these options. You may still enable or disable them individually if you&#8217;re sure it&#8217;ll work in your environment.</p>
<dt><code>-mtune=</code><i>cpu_type</i></p>
<dd>Set the instruction scheduling parameters for machine type <i>cpu_type</i>, but do not set the architecture type, register usage, or choice of mnemonics, as <code>-mcpu=</code><i>cpu_type</i> would. The same values for <i>cpu_type</i> are used for <code>-mtune</code> as for <code>-mcpu</code>. If both are specified, the code generated will use the architecture, registers, and mnemonics set by <code>-mcpu</code>, but the scheduling parameters set by <code>-mtune</code>.</p>
<dt><code>-mswdiv</code></p>
<dd>
<dt><code>-mno-swdiv</code></p>
<dd>Generate code to compute division as reciprocal estimate and iterative refinement, creating opportunities for increased throughput. This feature requires: optional PowerPC Graphics instruction set for single precision and <font SIZE="-1">FRE</font> instruction for double precision, assuming divides cannot generate user-visible traps, and the domain values not include Infinities, denormals or zero denominator.</p>
<dt><code>-maltivec</code></p>
<dd>
<dt><code>-mno-altivec</code></p>
<dd>Generate code that uses (does not use) AltiVec instructions, and also enable the use of built-in functions that allow more direct access to the AltiVec instruction set. You may also need to set <code>-mabi=altivec</code> to adjust the current <font SIZE="-1">ABI</font> with AltiVec <font SIZE="-1">ABI</font> enhancements.</p>
<dt><code>-mvrsave</code></p>
<dd>
<dt><code>-mno-vrsave</code></p>
<dd>Generate <font SIZE="-1">VRSAVE</font> instructions when generating AltiVec code.</p>
<dt><code>-msecure-plt</code></p>
<dd>Generate code that allows ld and ld.so to build executables and shared libraries with non-exec .plt and .got sections. This is a PowerPC 32-bit <font SIZE="-1">SYSV</font> <font SIZE="-1">ABI</font> option.</p>
<dt><code>-mbss-plt</code></p>
<dd>Generate code that uses a <font SIZE="-1">BSS</font> .plt section that ld.so fills in, and requires .plt and .got sections that are both writable and executable. This is a PowerPC 32-bit <font SIZE="-1">SYSV</font> <font SIZE="-1">ABI</font> option.</p>
<dt><code>-misel</code></p>
<dd>
<dt><code>-mno-isel</code></p>
<dd>This switch enables or disables the generation of <font SIZE="-1">ISEL</font> instructions.</p>
<dt><code>-misel=</code><i>yes/no</i></p>
<dd>This switch has been deprecated. Use <code>-misel</code> and <code>-mno-isel</code> instead.</p>
<dt><code>-mspe</code></p>
<dd>
<dt><code>-mno-isel</code></p>
<dd>This switch enables or disables the generation of <font SIZE="-1">SPE</font> simd instructions.</p>
<dt><code>-mspe=</code><i>yes/no</i></p>
<dd>This option has been deprecated. Use <code>-mspe</code> and <code>-mno-spe</code> instead.</p>
<dt><code>-mfloat-gprs=</code><i>yes/single/double/no</i></p>
<dd>
<dt><code>-mfloat-gprs</code></p>
<dd>This switch enables or disables the generation of floating point operations on the general purpose registers for architectures that support it. </p>
<p> The argument <i>yes</i> or <i>single</i> enables the use of single-precision floating point operations. </p>
<p> The argument <i>double</i> enables the use of single and double-precision floating point operations. </p>
<p> The argument <i>no</i> disables floating point operations on the general purpose registers. </p>
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
<dd>Modify generation of the <font SIZE="-1">TOC</font> (Table Of Contents), which is created for every executable file. The <code>-mfull-toc</code> option is selected by default. In that case, <font SIZE="-1">GCC</font> will allocate at least one <font SIZE="-1">TOC</font> entry for each unique non-automatic variable reference in your program. <font SIZE="-1">GCC</font> will also place floating-point constants in the <font SIZE="-1">TOC</font>. However, only 16,384 entries are available in the <font SIZE="-1">TOC</font>. </p>
<p> If you receive a linker error message that saying you have overflowed the available <font SIZE="-1">TOC</font> space, you can reduce the amount of <font SIZE="-1">TOC</font> space used with the <code>-mno-fp-in-toc</code> and <code>-mno-sum-in-toc</code> options. <code>-mno-fp-in-toc</code> prevents <font SIZE="-1">GCC</font> from putting floating-point constants in the <font SIZE="-1">TOC</font> and <code>-mno-sum-in-toc</code> forces <font SIZE="-1">GCC</font> to generate code to calculate the sum of an address and a constant at run-time instead of putting that sum into the <font SIZE="-1">TOC</font>. You may specify one or both of these options. Each causes <font SIZE="-1">GCC</font> to produce very slightly slower and larger code at the expense of conserving <font SIZE="-1">TOC</font> space. </p>
<p> If you still run out of space in the <font SIZE="-1">TOC</font> even when you specify both of these options, specify <code>-mminimal-toc</code> instead. This option causes <font SIZE="-1">GCC</font> to make only one <font SIZE="-1">TOC</font> entry for every file. When you specify this option, <font SIZE="-1">GCC</font> will produce code that is slower and larger but which uses extremely little <font SIZE="-1">TOC</font> space. You may wish to use this option only on files that contain less frequently executed code.</p>
<dt><code>-maix64</code></p>
<dd>
<dt><code>-maix32</code></p>
<dd>Enable 64-bit <font SIZE="-1">AIX</font> <font SIZE="-1">ABI</font> and calling convention: 64-bit pointers, 64-bit <tt>&quot;long&quot;</tt> type, and the infrastructure needed to support them. Specifying <code>-maix64</code> implies <code>-mpowerpc64</code> and <code>-mpowerpc</code>, while <code>-maix32</code> disables the 64-bit <font SIZE="-1">ABI</font> and implies <code>-mno-powerpc64</code>. <font SIZE="-1">GCC</font> defaults to <code>-maix32</code>.</p>
<dt><code>-mxl-compat</code></p>
<dd>
<dt><code>-mno-xl-compat</code></p>
<dd>Produce code that conforms more closely to <font SIZE="-1">IBM</font> <font SIZE="-1">XL</font> compiler semantics when using AIX-compatible <font SIZE="-1">ABI</font>. Pass floating-point arguments to prototyped functions beyond the register save area (<font SIZE="-1">RSA</font>) on the stack in addition to argument FPRs. Do not assume that most significant double in 128-bit long double value is properly rounded when comparing values and converting to double. Use <font SIZE="-1">XL</font> symbol names for long double support routines. </p>
<p> The <font SIZE="-1">AIX</font> calling convention was extended but not initially documented to handle an obscure K&amp;R C case of calling a function that takes the address of its arguments with fewer arguments than declared. <font SIZE="-1">IBM</font> <font SIZE="-1">XL</font> compilers access floating point arguments which do not fit in the <font SIZE="-1">RSA</font> from the stack when a subroutine is compiled without optimization. Because always storing floating-point arguments on the stack is inefficient and rarely needed, this option is not enabled by default and only is necessary when calling subroutines compiled by <font SIZE="-1">IBM</font> <font SIZE="-1">XL</font> compilers without optimization.</p>
<dt><code>-mpe</code></p>
<dd>Support <i></i><font SIZE="-1"><i>IBM</i></font><i> </i><font SIZE="-1"><i>RS/6000</i></font><i> </i><font SIZE="-1"><i>SP</i></font><i></i> <i>Parallel Environment</i> (<font SIZE="-1">PE</font>). Link an application written to use message passing with special startup code to enable the application to run. The system must have <font SIZE="-1">PE</font> installed in the standard location (<i>/usr/lpp/ppe.poe/</i>), or the <i>specs</i> file must be overridden with the <code>-specs=</code> option to specify the appropriate directory location. The Parallel Environment does not support threads, so the <code>-mpe</code> option and the <code>-pthread</code> option are incompatible.</p>
<dt><code>-malign-natural</code></p>
<dd>
<dt><code>-malign-power</code></p>
<dd>On <font SIZE="-1">AIX</font>, 32-bit Darwin, and 64-bit PowerPC GNU/Linux, the option <code>-malign-natural</code> overrides the ABI-defined alignment of larger types, such as floating-point doubles, on their natural size-based boundary. The option <code>-malign-power</code> instructs <font SIZE="-1">GCC</font> to follow the ABI-specified alignment rules. <font SIZE="-1">GCC</font> defaults to the standard alignment defined in the <font SIZE="-1">ABI</font>. </p>
<p> On 64-bit Darwin, natural alignment is the default, and <code>-malign-power</code> is not supported.</p>
<dt><code>-msoft-float</code></p>
<dd>
<dt><code>-mhard-float</code></p>
<dd>Generate code that does not use (uses) the floating-point register set. Software floating point emulation is provided if you use the <code>-msoft-float</code> option, and pass the option to <font SIZE="-1">GCC</font> when linking.</p>
<dt><code>-mmultiple</code></p>
<dd>
<dt><code>-mno-multiple</code></p>
<dd>Generate code that uses (does not use) the load multiple word instructions and the store multiple word instructions. These instructions are generated by default on <font SIZE="-1">POWER</font> systems, and not generated on PowerPC systems. Do not use <code>-mmultiple</code> on little endian PowerPC systems, since those instructions do not work when the processor is in little endian mode. The exceptions are <font SIZE="-1">PPC740</font> and <font SIZE="-1">PPC750</font> which permit the instructions usage in little endian mode.</p>
<dt><code>-mstring</code></p>
<dd>
<dt><code>-mno-string</code></p>
<dd>Generate code that uses (does not use) the load string instructions and the store string word instructions to save multiple registers and do small block moves. These instructions are generated by default on <font SIZE="-1">POWER</font> systems, and not generated on PowerPC systems. Do not use <code>-mstring</code> on little endian PowerPC systems, since those instructions do not work when the processor is in little endian mode. The exceptions are <font SIZE="-1">PPC740</font> and <font SIZE="-1">PPC750</font> which permit the instructions usage in little endian mode.</p>
<dt><code>-mupdate</code></p>
<dd>
<dt><code>-mno-update</code></p>
<dd>Generate code that uses (does not use) the load or store instructions that update the base register to the address of the calculated memory location. These instructions are generated by default. If you use <code>-mno-update</code>, there is a small window between the time that the stack pointer is updated and the address of the previous frame is stored, which means code that walks the stack frame across interrupts or signals may get corrupted data.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Generate code that uses (does not use) the floating point multiply and accumulate instructions. These instructions are generated by default if hardware floating is used.</p>
<dt><code>-mno-bit-align</code></p>
<dd>
<dt><code>-mbit-align</code></p>
<dd>On System V.4 and embedded PowerPC systems do not (do) force structures and unions that contain bit-fields to be aligned to the base type of the bit-field. </p>
<p> For example, by default a structure containing nothing but 8 <tt>&quot;unsigned&quot;</tt> bit-fields of length 1 would be aligned to a 4 byte boundary and have a size of 4 bytes. By using <code>-mno-bit-align</code>, the structure would be aligned to a 1 byte boundary and be one byte in size.</p>
<dt><code>-mno-strict-align</code></p>
<dd>
<dt><code>-mstrict-align</code></p>
<dd>On System V.4 and embedded PowerPC systems do not (do) assume that unaligned memory references will be handled by the system.</p>
<dt><code>-mrelocatable</code></p>
<dd>
<dt><code>-mno-relocatable</code></p>
<dd>On embedded PowerPC systems generate code that allows (does not allow) the program to be relocated to a different address at runtime. If you use <code>-mrelocatable</code> on any module, all objects linked together must be compiled with <code>-mrelocatable</code> or <code>-mrelocatable-lib</code>.</p>
<dt><code>-mrelocatable-lib</code></p>
<dd>
<dt><code>-mno-relocatable-lib</code></p>
<dd>On embedded PowerPC systems generate code that allows (does not allow) the program to be relocated to a different address at runtime. Modules compiled with <code>-mrelocatable-lib</code> can be linked with either modules compiled without <code>-mrelocatable</code> and <code>-mrelocatable-lib</code> or with modules compiled with the <code>-mrelocatable</code> options.</p>
<dt><code>-mno-toc</code></p>
<dd>
<dt><code>-mtoc</code></p>
<dd>On System V.4 and embedded PowerPC systems do not (do) assume that register 2 contains a pointer to a global area pointing to the addresses used in the program.</p>
<dt><code>-mlittle</code></p>
<dd>
<dt><code>-mlittle-endian</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the processor in little endian mode. The <code>-mlittle-endian</code> option is the same as <code>-mlittle</code>.</p>
<dt><code>-mbig</code></p>
<dd>
<dt><code>-mbig-endian</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the processor in big endian mode. The <code>-mbig-endian</code> option is the same as <code>-mbig</code>.</p>
<dt><code>-mdynamic-no-pic</code></p>
<dd>On Darwin and Mac <font SIZE="-1">OS</font> X systems, compile code so that it is not relocatable, but that its external references are relocatable. The resulting code is suitable for applications, but not shared libraries.</p>
<dt><code>-mprioritize-restricted-insns=</code><i>priority</i></p>
<dd>This option controls the priority that is assigned to dispatch-slot restricted instructions during the second scheduling pass. The argument <i>priority</i> takes the value <i>0/1/2</i> to assign <i>no/highest/second-highest</i> priority to dispatch slot restricted instructions.</p>
<dt><code>-msched-costly-dep=</code><i>dependence_type</i></p>
<dd>This option controls which dependences are considered costly by the target during instruction scheduling. The argument <i>dependence_type</i> takes one of the following values: <i>no</i>: no dependence is costly, <i>all</i>: all dependences are costly, <i>true_store_to_load</i>: a true dependence from store to load is costly, <i>store_to_load</i>: any dependence from store to load is costly, <i>number</i>: any dependence which latency &gt;= <i>number</i> is costly.</p>
<dt><code>-minsert-sched-nops=</code><i>scheme</i></p>
<dd>This option controls which nop insertion scheme will be used during the second scheduling pass. The argument <i>scheme</i> takes one of the following values: <i>no</i>: Don&#8217;t insert nops. <i>pad</i>: Pad with nops any dispatch group which has vacant issue slots, according to the scheduler&#8217;s grouping. <i>regroup_exact</i>: Insert nops to force costly dependent insns into separate groups. Insert exactly as many nops as needed to force an insn to a new group, according to the estimated processor grouping. <i>number</i>: Insert nops to force costly dependent insns into separate groups. Insert <i>number</i> nops to force an insn to a new group.</p>
<dt><code>-mcall-sysv</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code using calling conventions that adheres to the March 1995 draft of the System V Application Binary Interface, PowerPC processor supplement. This is the default unless you configured <font SIZE="-1">GCC</font> using <code>powerpc-*-eabiaix</code>.</p>
<dt><code>-mcall-sysv-eabi</code></p>
<dd>Specify both <code>-mcall-sysv</code> and <code>-meabi</code> options.</p>
<dt><code>-mcall-sysv-noeabi</code></p>
<dd>Specify both <code>-mcall-sysv</code> and <code>-mno-eabi</code> options.</p>
<dt><code>-mcall-solaris</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the Solaris operating system.</p>
<dt><code>-mcall-linux</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the Linux-based <font SIZE="-1">GNU</font> system.</p>
<dt><code>-mcall-gnu</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the Hurd-based <font SIZE="-1">GNU</font> system.</p>
<dt><code>-mcall-netbsd</code></p>
<dd>On System V.4 and embedded PowerPC systems compile code for the NetBSD operating system.</p>
<dt><code>-maix-struct-return</code></p>
<dd>Return all structures in memory (as specified by the <font SIZE="-1">AIX</font> <font SIZE="-1">ABI</font>).</p>
<dt><code>-msvr4-struct-return</code></p>
<dd>Return structures smaller than 8 bytes in registers (as specified by the <font SIZE="-1">SVR4</font> <font SIZE="-1">ABI</font>).</p>
<dt><code>-mabi=</code><i>abi-type</i></p>
<dd>Extend the current <font SIZE="-1">ABI</font> with a particular extension, or remove such extension. Valid values are <i>altivec</i>, <i>no-altivec</i>, <i>spe</i>, <i>no-spe</i>, <i>ibmlongdouble</i>, <i>ieeelongdouble</i>.</p>
<dt><code>-mabi=spe</code></p>
<dd>Extend the current <font SIZE="-1">ABI</font> with <font SIZE="-1">SPE</font> <font SIZE="-1">ABI</font> extensions. This does not change the default <font SIZE="-1">ABI</font>, instead it adds the <font SIZE="-1">SPE</font> <font SIZE="-1">ABI</font> extensions to the current <font SIZE="-1">ABI</font>.</p>
<dt><code>-mabi=no-spe</code></p>
<dd>Disable Booke <font SIZE="-1">SPE</font> <font SIZE="-1">ABI</font> extensions for the current <font SIZE="-1">ABI</font>.</p>
<dt><code>-mabi=ibmlongdouble</code></p>
<dd>Change the current <font SIZE="-1">ABI</font> to use <font SIZE="-1">IBM</font> extended precision long double. This is a PowerPC 32-bit <font SIZE="-1">SYSV</font> <font SIZE="-1">ABI</font> option.</p>
<dt><code>-mabi=ieeelongdouble</code></p>
<dd>Change the current <font SIZE="-1">ABI</font> to use <font SIZE="-1">IEEE</font> extended precision long double. This is a PowerPC 32-bit Linux <font SIZE="-1">ABI</font> option.</p>
<dt><code>-mprototype</code></p>
<dd>
<dt><code>-mno-prototype</code></p>
<dd>On System V.4 and embedded PowerPC systems assume that all calls to variable argument functions are properly prototyped. Otherwise, the compiler must insert an instruction before every non prototyped call to set or clear bit 6 of the condition code register (<i></i><font SIZE="-1"><i>CR</i></font><i></i>) to indicate whether floating point values were passed in the floating point registers in case the function takes a variable arguments. With <code>-mprototype</code>, only calls to prototyped variable argument functions will set or clear the bit.</p>
<dt><code>-msim</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>sim-crt0.o</i> and that the standard C libraries are <i>libsim.a</i> and <i>libc.a</i>. This is the default for <code>powerpc-*-eabisim</code>. configurations.</p>
<dt><code>-mmvme</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libmvme.a</i> and <i>libc.a</i>.</p>
<dt><code>-mads</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libads.a</i> and <i>libc.a</i>.</p>
<dt><code>-myellowknife</code></p>
<dd>On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libyk.a</i> and <i>libc.a</i>.</p>
<dt><code>-mvxworks</code></p>
<dd>On System V.4 and embedded PowerPC systems, specify that you are compiling for a VxWorks system.</p>
<dt><code>-mwindiss</code></p>
<dd>Specify that you are compiling for the WindISS simulation environment.</p>
<dt><code>-memb</code></p>
<dd>On embedded PowerPC systems, set the <i></i><font SIZE="-1"><i>PPC_EMB</i></font><i></i> bit in the <font SIZE="-1">ELF</font> flags header to indicate that <code>eabi</code> extended relocations are used.</p>
<dt><code>-meabi</code></p>
<dd>
<dt><code>-mno-eabi</code></p>
<dd>On System V.4 and embedded PowerPC systems do (do not) adhere to the Embedded Applications Binary Interface (eabi) which is a set of modifications to the System V.4 specifications. Selecting <code>-meabi</code> means that the stack is aligned to an 8 byte boundary, a function <tt>&quot;__eabi&quot;</tt> is called to from <tt>&quot;main&quot;</tt> to set up the eabi environment, and the <code>-msdata</code> option can use both <tt>&quot;r2&quot;</tt> and <tt>&quot;r13&quot;</tt> to point to two separate small data areas. Selecting <code>-mno-eabi</code> means that the stack is aligned to a 16 byte boundary, do not call an initialization function from <tt>&quot;main&quot;</tt>, and the <code>-msdata</code> option will only use <tt>&quot;r13&quot;</tt> to point to a single small data area. The <code>-meabi</code> option is on by default if you configured <font SIZE="-1">GCC</font> using one of the <code>powerpc*-*-eabi*</code> options.</p>
<dt><code>-msdata=eabi</code></p>
<dd>On System V.4 and embedded PowerPC systems, put small initialized <tt>&quot;const&quot;</tt> global and static data in the <code>.sdata2</code> section, which is pointed to by register <tt>&quot;r2&quot;</tt>. Put small initialized non-<tt>&quot;const&quot;</tt> global and static data in the <code>.sdata</code> section, which is pointed to by register <tt>&quot;r13&quot;</tt>. Put small uninitialized global and static data in the <code>.sbss</code> section, which is adjacent to the <code>.sdata</code> section. The <code>-msdata=eabi</code> option is incompatible with the <code>-mrelocatable</code> option. The <code>-msdata=eabi</code> option also sets the <code>-memb</code> option.</p>
<dt><code>-msdata=sysv</code></p>
<dd>On System V.4 and embedded PowerPC systems, put small global and static data in the <code>.sdata</code> section, which is pointed to by register <tt>&quot;r13&quot;</tt>. Put small uninitialized global and static data in the <code>.sbss</code> section, which is adjacent to the <code>.sdata</code> section. The <code>-msdata=sysv</code> option is incompatible with the <code>-mrelocatable</code> option.</p>
<dt><code>-msdata=default</code></p>
<dd>
<dt><code>-msdata</code></p>
<dd>On System V.4 and embedded PowerPC systems, if <code>-meabi</code> is used, compile code the same as <code>-msdata=eabi</code>, otherwise compile code the same as <code>-msdata=sysv</code>.</p>
<dt><code>-msdata-data</code></p>
<dd>On System V.4 and embedded PowerPC systems, put small global and static data in the <code>.sdata</code> section. Put small uninitialized global and static data in the <code>.sbss</code> section. Do not use register <tt>&quot;r13&quot;</tt> to address small data however. This is the default behavior unless other <code>-msdata</code> options are used.</p>
<dt><code>-msdata=none</code></p>
<dd>
<dt><code>-mno-sdata</code></p>
<dd>On embedded PowerPC systems, put all initialized global and static data in the <code>.data</code> section, and all uninitialized data in the <code>.bss</code> section.</p>
<dt><code>-G</code> <i>num</i></p>
<dd>On embedded PowerPC systems, put global and static items less than or equal to <i>num</i> bytes into the small data or bss sections instead of the normal data or bss section. By default, <i>num</i> is 8. The <code>-G</code> <i>num</i> switch is also passed to the linker. All modules should be compiled with the same <code>-G</code> <i>num</i> value.</p>
<dt><code>-mregnames</code></p>
<dd>
<dt><code>-mno-regnames</code></p>
<dd>On System V.4 and embedded PowerPC systems do (do not) emit register names in the assembly language output using symbolic forms.</p>
<dt><code>-mlongcall</code></p>
<dd>
<dt><code>-mno-longcall</code></p>
<dd>Default to making all function calls indirectly, using a register, so that functions which reside further than 32 megabytes (33,554,432 bytes) from the current location can be called. This setting can be overridden by the <tt>&quot;shortcall&quot;</tt> function attribute, or by <tt>&quot;#pragma longcall(0)&quot;</tt>. </p>
<p> Some linkers are capable of detecting out-of-range calls and generating glue code on the fly. On these systems, long calls are unnecessary and generate slower code. As of this writing, the <font SIZE="-1">AIX</font> linker can do this, as can the <font SIZE="-1">GNU</font> linker for PowerPC/64. It is planned to add this feature to the <font SIZE="-1">GNU</font> linker for 32-bit PowerPC systems as well. </p>
<p> On Darwin/PPC systems, <tt>&quot;#pragma longcall&quot;</tt> will generate &#8220;jbsr callee, L42&#8221;, plus a &#8220;branch island&#8221; (glue code). The two target addresses represent the callee and the &#8220;branch island&#8221;. The Darwin/PPC linker will prefer the first address and generate a &#8220;bl callee&#8221; if the <font SIZE="-1">PPC</font> &#8220;bl&#8221; instruction will reach the callee directly; otherwise, the linker will generate &#8220;bl L42&#8221; to call the &#8220;branch island&#8221;. The &#8220;branch island&#8221; is appended to the body of the calling function; it computes the full 32-bit address of the callee and jumps to it. </p>
<p> On Mach-O (Darwin) systems, this option directs the compiler emit to the glue for every direct call, and the Darwin linker decides whether to use or discard it. </p>
<p> In the future, we may cause <font SIZE="-1">GCC</font> to ignore all longcall specifications when the linker is known to generate glue.</p>
<dt><code>-pthread</code></p>
<dd>Adds support for multithreading with the <i>pthreads</i> library. This option sets flags for both the preprocessor and linker.</dl>
<p> <i>S/390 and zSeries Options</i> </p>
<p> These are the <code>-m</code> options defined for the S/390 and zSeries architecture.</p>
<dl>
<dt><code>-mhard-float</code></p>
<dd>
<dt><code>-msoft-float</code></p>
<dd>Use (do not use) the hardware floating-point instructions and registers for floating-point operations. When <code>-msoft-float</code> is specified, functions in <i>libgcc.a</i> will be used to perform floating-point operations. When <code>-mhard-float</code> is specified, the compiler generates <font SIZE="-1">IEEE</font> floating-point instructions. This is the default.</p>
<dt><code>-mlong-double-64</code></p>
<dd>
<dt><code>-mlong-double-128</code></p>
<dd>These switches control the size of <tt>&quot;long double&quot;</tt> type. A size of 64bit makes the <tt>&quot;long double&quot;</tt> type equivalent to the <tt>&quot;double&quot;</tt> type. This is the default.</p>
<dt><code>-mbackchain</code></p>
<dd>
<dt><code>-mno-backchain</code></p>
<dd>Store (do not store) the address of the caller&#8217;s frame as backchain pointer into the callee&#8217;s stack frame. A backchain may be needed to allow debugging using tools that do not understand <font SIZE="-1">DWARF-2</font> call frame information. When <code>-mno-packed-stack</code> is in effect, the backchain pointer is stored at the bottom of the stack frame; when <code>-mpacked-stack</code> is in effect, the backchain is placed into the topmost word of the 96/160 byte register save area. </p>
<p> In general, code compiled with <code>-mbackchain</code> is call-compatible with code compiled with <code>-mmo-backchain</code>; however, use of the backchain for debugging purposes usually requires that the whole binary is built with <code>-mbackchain</code>. Note that the combination of <code>-mbackchain</code>, <code>-mpacked-stack</code> and <code>-mhard-float</code> is not supported. In order to build a linux kernel use <code>-msoft-float</code>. </p>
<p> The default is to not maintain the backchain.</p>
<dt><code>-mpacked-stack</code></p>
<dd>
<dt><code>-mno-packed-stack</code></p>
<dd>Use (do not use) the packed stack layout. When <code>-mno-packed-stack</code> is specified, the compiler uses the all fields of the 96/160 byte register save area only for their default purpose; unused fields still take up stack space. When <code>-mpacked-stack</code> is specified, register save slots are densely packed at the top of the register save area; unused space is reused for other purposes, allowing for more efficient use of the available stack space. However, when <code>-mbackchain</code> is also in effect, the topmost word of the save area is always used to store the backchain, and the return address register is always saved two words below the backchain. </p>
<p> As long as the stack frame backchain is not used, code generated with <code>-mpacked-stack</code> is call-compatible with code generated with <code>-mno-packed-stack</code>. Note that some non-FSF releases of <font SIZE="-1">GCC</font> 2.95 for S/390 or zSeries generated code that uses the stack frame backchain at run time, not just for debugging purposes. Such code is not call-compatible with code compiled with <code>-mpacked-stack</code>. Also, note that the combination of <code>-mbackchain</code>, <code>-mpacked-stack</code> and <code>-mhard-float</code> is not supported. In order to build a linux kernel use <code>-msoft-float</code>. </p>
<p> The default is to not use the packed stack layout.</p>
<dt><code>-msmall-exec</code></p>
<dd>
<dt><code>-mno-small-exec</code></p>
<dd>Generate (or do not generate) code using the <tt>&quot;bras&quot;</tt> instruction to do subroutine calls. This only works reliably if the total executable size does not exceed 64k. The default is to use the <tt>&quot;basr&quot;</tt> instruction instead, which does not have this limitation.</p>
<dt><code>-m64</code></p>
<dd>
<dt><code>-m31</code></p>
<dd>When <code>-m31</code> is specified, generate code compliant to the GNU/Linux for S/390 <font SIZE="-1">ABI</font>. When <code>-m64</code> is specified, generate code compliant to the GNU/Linux for zSeries <font SIZE="-1">ABI</font>. This allows <font SIZE="-1">GCC</font> in particular to generate 64-bit instructions. For the <code>s390</code> targets, the default is <code>-m31</code>, while the <code>s390x</code> targets default to <code>-m64</code>.</p>
<dt><code>-mzarch</code></p>
<dd>
<dt><code>-mesa</code></p>
<dd>When <code>-mzarch</code> is specified, generate code using the instructions available on z/Architecture. When <code>-mesa</code> is specified, generate code using the instructions available on <font SIZE="-1">ESA/390</font>. Note that <code>-mesa</code> is not possible with <code>-m64</code>. When generating code compliant to the GNU/Linux for S/390 <font SIZE="-1">ABI</font>, the default is <code>-mesa</code>. When generating code compliant to the GNU/Linux for zSeries <font SIZE="-1">ABI</font>, the default is <code>-mzarch</code>.</p>
<dt><code>-mmvcle</code></p>
<dd>
<dt><code>-mno-mvcle</code></p>
<dd>Generate (or do not generate) code using the <tt>&quot;mvcle&quot;</tt> instruction to perform block moves. When <code>-mno-mvcle</code> is specified, use a <tt>&quot;mvc&quot;</tt> loop instead. This is the default unless optimizing for size.</p>
<dt><code>-mdebug</code></p>
<dd>
<dt><code>-mno-debug</code></p>
<dd>Print (or do not print) additional debug information when compiling. The default is to not print debug information.</p>
<dt><code>-march=</code><i>cpu-type</i></p>
<dd>Generate code that will run on <i>cpu-type</i>, which is the name of a system representing a certain processor type. Possible values for <i>cpu-type</i> are <code>g5</code>, <code>g6</code>, <code>z900</code>, and <code>z990</code>. When generating code using the instructions available on z/Architecture, the default is <code>-march=z900</code>. Otherwise, the default is <code>-march=g5</code>.</p>
<dt><code>-mtune=</code><i>cpu-type</i></p>
<dd>Tune to <i>cpu-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The list of <i>cpu-type</i> values is the same as for <code>-march</code>. The default is the value used for <code>-march</code>.</p>
<dt><code>-mtpf-trace</code></p>
<dd>
<dt><code>-mno-tpf-trace</code></p>
<dd>Generate code that adds (does not add) in <font SIZE="-1">TPF</font> <font SIZE="-1">OS</font> specific branches to trace routines in the operating system. This option is off by default, even when compiling for the <font SIZE="-1">TPF</font> <font SIZE="-1">OS</font>.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Generate code that uses (does not use) the floating point multiply and accumulate instructions. These instructions are generated by default if hardware floating point is used.</p>
<dt><code>-mwarn-framesize=</code><i>framesize</i></p>
<dd>Emit a warning if the current function exceeds the given frame size. Because this is a compile time check it doesn&#8217;t need to be a real problem when the program runs. It is intended to identify functions which most probably cause a stack overflow. It is useful to be used in an environment with limited stack size e.g. the linux kernel.</p>
<dt><code>-mwarn-dynamicstack</code></p>
<dd>Emit a warning if the function calls alloca or uses dynamically sized arrays. This is generally a bad idea with a limited stack size.</p>
<dt><code>-mstack-guard=</code><i>stack-guard</i></p>
<dd>
<dt><code>-mstack-size=</code><i>stack-size</i></p>
<dd>These arguments always have to be used in conjunction. If they are present the s390 back end emits additional instructions in the function prologue which trigger a trap if the stack size is <i>stack-guard</i> bytes above the <i>stack-size</i> (remember that the stack on s390 grows downward). These options are intended to be used to help debugging stack overflow problems. The additionally emitted code causes only little overhead and hence can also be used in production like systems without greater performance degradation. The given values have to be exact powers of 2 and <i>stack-size</i> has to be greater than <i>stack-guard</i> without exceeding 64k. In order to be efficient the extra code makes the assumption that the stack starts at an address aligned to the value given by <i>stack-size</i>.</dl>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">SH</font> implementations:</p>
<dl>
<dt><code>-m1</code></p>
<dd>Generate code for the <font SIZE="-1">SH1</font>.</p>
<dt><code>-m2</code></p>
<dd>Generate code for the <font SIZE="-1">SH2</font>.</p>
<dt><code>-m2e</code></p>
<dd>Generate code for the SH2e.</p>
<dt><code>-m3</code></p>
<dd>Generate code for the <font SIZE="-1">SH3</font>.</p>
<dt><code>-m3e</code></p>
<dd>Generate code for the SH3e.</p>
<dt><code>-m4-nofpu</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font> without a floating-point unit.</p>
<dt><code>-m4-single-only</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font> with a floating-point unit that only supports single-precision arithmetic.</p>
<dt><code>-m4-single</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font> assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m4</code></p>
<dd>Generate code for the <font SIZE="-1">SH4</font>.</p>
<dt><code>-m4a-nofpu</code></p>
<dd>Generate code for the SH4al-dsp, or for a SH4a in such a way that the floating-point unit is not used.</p>
<dt><code>-m4a-single-only</code></p>
<dd>Generate code for the SH4a, in such a way that no double-precision floating point operations are used.</p>
<dt><code>-m4a-single</code></p>
<dd>Generate code for the SH4a assuming the floating-point unit is in single-precision mode by default.</p>
<dt><code>-m4a</code></p>
<dd>Generate code for the SH4a.</p>
<dt><code>-m4al</code></p>
<dd>Same as <code>-m4a-nofpu</code>, except that it implicitly passes <code>-dsp</code> to the assembler. <font SIZE="-1">GCC</font> doesn&#8217;t generate any <font SIZE="-1">DSP</font> instructions at the moment.</p>
<dt><code>-mb</code></p>
<dd>Compile code for the processor in big endian mode.</p>
<dt><code>-ml</code></p>
<dd>Compile code for the processor in little endian mode.</p>
<dt><code>-mdalign</code></p>
<dd>Align doubles at 64-bit boundaries. Note that this changes the calling conventions, and thus some functions from the standard C library will not work unless you recompile it first with <code>-mdalign</code>.</p>
<dt><code>-mrelax</code></p>
<dd>Shorten some address references at link time, when possible; uses the linker option <code>-relax</code>.</p>
<dt><code>-mbigtable</code></p>
<dd>Use 32-bit offsets in <tt>&quot;switch&quot;</tt> tables. The default is to use 16-bit offsets.</p>
<dt><code>-mfmovd</code></p>
<dd>Enable the use of the instruction <tt>&quot;fmovd&quot;</tt>.</p>
<dt><code>-mhitachi</code></p>
<dd>Comply with the calling conventions defined by Renesas.</p>
<dt><code>-mrenesas</code></p>
<dd>Comply with the calling conventions defined by Renesas.</p>
<dt><code>-mno-renesas</code></p>
<dd>Comply with the calling conventions defined for <font SIZE="-1">GCC</font> before the Renesas conventions were available. This option is the default for all targets of the <font SIZE="-1">SH</font> toolchain except for <code>sh-symbianelf</code>.</p>
<dt><code>-mnomacsave</code></p>
<dd>Mark the <tt>&quot;MAC&quot;</tt> register as call-clobbered, even if <code>-mhitachi</code> is given.</p>
<dt><code>-mieee</code></p>
<dd>Increase IEEE-compliance of floating-point code. At the moment, this is equivalent to <code>-fno-finite-math-only</code>. When generating 16 bit <font SIZE="-1">SH</font> opcodes, getting IEEE-conforming results for comparisons of NANs / infinities incurs extra overhead in every floating point comparison, therefore the default is set to <code>-ffinite-math-only</code>.</p>
<dt><code>-misize</code></p>
<dd>Dump instruction size and location in the assembly code.</p>
<dt><code>-mpadstruct</code></p>
<dd>This option is deprecated. It pads structures to multiple of 4 bytes, which is incompatible with the <font SIZE="-1">SH</font> <font SIZE="-1">ABI</font>.</p>
<dt><code>-mspace</code></p>
<dd>Optimize for space instead of speed. Implied by <code>-Os</code>.</p>
<dt><code>-mprefergot</code></p>
<dd>When generating position-independent code, emit function calls using the Global Offset Table instead of the Procedure Linkage Table.</p>
<dt><code>-musermode</code></p>
<dd>Generate a library function call to invalidate instruction cache entries, after fixing up a trampoline. This library function call doesn&#8217;t assume it can write to the whole memory address space. This is the default when the target is <tt>&quot;sh-*-linux*&quot;</tt>.</p>
<dt><code>-multcost=</code><i>number</i></p>
<dd>Set the cost to assume for a multiply insn.</p>
<dt><code>-mdiv=</code><i>strategy</i></p>
<dd>Set the division strategy to use for SHmedia code. <i>strategy</i> must be one of: call, call2, fp, inv, inv:minlat, inv20u, inv20l, inv:call, inv:call2, inv:fp . &#8220;fp&#8221; performs the operation in floating point. This has a very high latency, but needs only a few instructions, so it might be a good choice if your code has enough easily exploitable <font SIZE="-1">ILP</font> to allow the compiler to schedule the floating point instructions together with other instructions. Division by zero causes a floating point exception. &#8220;inv&#8221; uses integer operations to calculate the inverse of the divisor, and then multiplies the dividend with the inverse. This strategy allows cse and hoisting of the inverse calculation. Division by zero calculates an unspecified result, but does not trap. &#8220;inv:minlat&#8221; is a variant of &#8220;inv&#8221; where if no cse / hoisting opportunities have been found, or if the entire operation has been hoisted to the same place, the last stages of the inverse calculation are intertwined with the final multiply to reduce the overall latency, at the expense of using a few more instructions, and thus offering fewer scheduling opportunities with other code. &#8220;call&#8221; calls a library function that usually implements the inv:minlat strategy. This gives high code density for m5-*media-nofpu compilations. &#8220;call2&#8221; uses a different entry point of the same library function, where it assumes that a pointer to a lookup table has already been set up, which exposes the pointer load to cse / code hoisting optimizations. &#8220;inv:call&#8221;, &#8220;inv:call2&#8221; and &#8220;inv:fp&#8221; all use the &#8220;inv&#8221; algorithm for initial code generation, but if the code stays unoptimized, revert to the &#8220;call&#8221;, &#8220;call2&#8221;, or &#8220;fp&#8221; strategies, respectively. Note that the potentially-trapping side effect of division by zero is carried by a separate instruction, so it is possible that all the integer instructions are hoisted out, but the marker for the side effect stays where it is. A recombination to fp operations or a call is not possible in that case. &#8220;inv20u&#8221; and &#8220;inv20l&#8221; are variants of the &#8220;inv:minlat&#8221; strategy. In the case that the inverse calculation was nor separated from the multiply, they speed up division where the dividend fits into 20 bits (plus sign where applicable), by inserting a test to skip a number of operations in this case; this test slows down the case of larger dividends. inv20u assumes the case of a such a small dividend to be unlikely, and inv20l assumes it to be likely.</p>
<dt><code>-mdivsi3_libfunc=</code><i>name</i></p>
<dd>Set the name of the library function used for 32 bit signed division to <i>name</i>. This only affect the name used in the call and inv:call division strategies, and the compiler will still expect the same sets of input/output/clobbered registers as if this option was not present.</p>
<dt><code>-madjust-unroll</code></p>
<dd>Throttle unrolling to avoid thrashing target registers. This option only has an effect if the gcc code base supports the <font SIZE="-1">TARGET_ADJUST_UNROLL_MAX</font> target hook.</p>
<dt><code>-mindexed-addressing</code></p>
<dd>Enable the use of the indexed addressing mode for SHmedia32/SHcompact. This is only safe if the hardware and/or <font SIZE="-1">OS</font> implement 32 bit wrap-around semantics for the indexed addressing mode. The architecture allows the implementation of processors with 64 bit <font SIZE="-1">MMU</font>, which the <font SIZE="-1">OS</font> could use to get 32 bit addressing, but since no current hardware implementation supports this or any other way to make the indexed addressing mode safe to use in the 32 bit <font SIZE="-1">ABI</font>, the default is -mno-indexed-addressing.</p>
<dt><code>-mgettrcost=</code><i>number</i></p>
<dd>Set the cost assumed for the gettr instruction to <i>number</i>. The default is 2 if <code>-mpt-fixed</code> is in effect, 100 otherwise.</p>
<dt><code>-mpt-fixed</code></p>
<dd>Assume pt* instructions won&#8217;t trap. This will generally generate better scheduled code, but is unsafe on current hardware. The current architecture definition says that ptabs and ptrel trap when the target anded with 3 is 3. This has the unintentional effect of making it unsafe to schedule ptabs / ptrel before a branch, or hoist it out of a loop. For example, __do_global_ctors, a part of libgcc that runs constructors at program startup, calls functions in a list which is delimited by -1. With the -mpt-fixed option, the ptabs will be done before testing against -1. That means that all the constructors will be run a bit quicker, but when the loop comes to the end of the list, the program crashes because ptabs loads -1 into a target register. Since this option is unsafe for any hardware implementing the current architecture specification, the default is -mno-pt-fixed. Unless the user specifies a specific cost with <code>-mgettrcost</code>, -mno-pt-fixed also implies <code>-mgettrcost=100</code>; this deters register allocation using target registers for storing ordinary integers.</p>
<dt><code>-minvalid-symbols</code></p>
<dd>Assume symbols might be invalid. Ordinary function symbols generated by the compiler will always be valid to load with movi/shori/ptabs or movi/shori/ptrel, but with assembler and/or linker tricks it is possible to generate symbols that will cause ptabs / ptrel to trap. This option is only meaningful when <code>-mno-pt-fixed</code> is in effect. It will then prevent cross-basic-block cse, hoisting and most scheduling of symbol loads. The default is <code>-mno-invalid-symbols</code>.</dl>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are supported on the <font SIZE="-1">SPARC:</font></p>
<dl>
<dt><code>-mno-app-regs</code></p>
<dd>
<dt><code>-mapp-regs</code></p>
<dd>Specify <code>-mapp-regs</code> to generate output using the global registers 2 through 4, which the <font SIZE="-1">SPARC</font> <font SIZE="-1">SVR4</font> <font SIZE="-1">ABI</font> reserves for applications. This is the default. </p>
<p> To be fully <font SIZE="-1">SVR4</font> <font SIZE="-1">ABI</font> compliant at the cost of some performance loss, specify <code>-mno-app-regs</code>. You should compile libraries and system software with this option.</p>
<dt><code>-mfpu</code></p>
<dd>
<dt><code>-mhard-float</code></p>
<dd>Generate output containing floating point instructions. This is the default.</p>
<dt><code>-mno-fpu</code></p>
<dd>
<dt><code>-msoft-float</code></p>
<dd>Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">SPARC</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded targets <code>sparc-*-aout</code> and <code>sparclite-*-*</code> do provide software floating point support. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC</font>, with <code>-msoft-float</code> in order for this to work.</p>
<dt><code>-mhard-quad-float</code></p>
<dd>Generate output containing quad-word (long double) floating point instructions.</p>
<dt><code>-msoft-quad-float</code></p>
<dd>Generate output containing library calls for quad-word (long double) floating point instructions. The functions called are those specified in the <font SIZE="-1">SPARC</font> <font SIZE="-1">ABI</font>. This is the default. </p>
<p> As of this writing, there are no <font SIZE="-1">SPARC</font> implementations that have hardware support for the quad-word floating point instructions. They all invoke a trap handler for one of these instructions, and then the trap handler emulates the effect of the instruction. Because of the trap handler overhead, this is much slower than calling the <font SIZE="-1">ABI</font> library routines. Thus the <code>-msoft-quad-float</code> option is the default.</p>
<dt><code>-mno-unaligned-doubles</code></p>
<dd>
<dt><code>-munaligned-doubles</code></p>
<dd>Assume that doubles have 8 byte alignment. This is the default. </p>
<p> With <code>-munaligned-doubles</code>, <font SIZE="-1">GCC</font> assumes that doubles have 8 byte alignment only if they are contained in another type, or if they have an absolute address. Otherwise, it assumes they have 4 byte alignment. Specifying this option avoids some rare compatibility problems with code generated by other compilers. It is not the default because it results in a performance loss, especially for floating point code.</p>
<dt><code>-mno-faster-structs</code></p>
<dd>
<dt><code>-mfaster-structs</code></p>
<dd>With <code>-mfaster-structs</code>, the compiler assumes that structures should have 8 byte alignment. This enables the use of pairs of <tt>&quot;ldd&quot;</tt> and <tt>&quot;std&quot;</tt> instructions for copies in structure assignment, in place of twice as many <tt>&quot;ld&quot;</tt> and <tt>&quot;st&quot;</tt> pairs. However, the use of this changed alignment directly violates the <font SIZE="-1">SPARC</font> <font SIZE="-1">ABI</font>. Thus, it&#8217;s intended only for use on targets where the developer acknowledges that their resulting code will not be directly in line with the rules of the <font SIZE="-1">ABI</font>.</p>
<dt><code>-mimpure-text</code></p>
<dd><code>-mimpure-text</code>, used in addition to <code>-shared</code>, tells the compiler to not pass <code>-z text</code> to the linker when linking a shared object. Using this option, you can link position-dependent code into a shared object. </p>
<p> <code>-mimpure-text</code> suppresses the &#8220;relocations remain against allocatable but non-writable sections&#8221; linker error message. However, the necessary relocations will trigger copy-on-write, and the shared object is not actually shared across processes. Instead of using <code>-mimpure-text</code>, you should compile all source code with <code>-fpic</code> or <code>-fPIC</code>. </p>
<p> This option is only available on SunOS and Solaris.</p>
<dt><code>-mcpu=</code><i>cpu_type</i></p>
<dd>Set the instruction set, register set, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>v7</code>, <code>cypress</code>, <code>v8</code>, <code>supersparc</code>, <code>sparclite</code>, <code>f930</code>, <code>f934</code>, <code>hypersparc</code>, <code>sparclite86x</code>, <code>sparclet</code>, <code>tsc701</code>, <code>v9</code>, <code>ultrasparc</code>, and <code>ultrasparc3</code>. </p>
<p> Default instruction scheduling parameters are used for values that select an architecture and not an implementation. These are <code>v7</code>, <code>v8</code>, <code>sparclite</code>, <code>sparclet</code>, <code>v9</code>. </p>
<p> Here is a list of each supported architecture and their supported implementations. </p>
<pre> v7: cypress
 v8: supersparc, hypersparc
 sparclite: f930, f934, sparclite86x
 sparclet: tsc701
 v9: ultrasparc, ultrasparc3</pre>
<p>By default (unless configured otherwise), <font SIZE="-1">GCC</font> generates code for the V7 variant of the <font SIZE="-1">SPARC</font> architecture. With <code>-mcpu=cypress</code>, the compiler additionally optimizes it for the Cypress <font SIZE="-1">CY7C602</font> chip, as used in the SPARCStation/SPARCServer 3xx series. This is also appropriate for the older SPARCStation 1, 2, <font SIZE="-1">IPX</font> etc. </p>
<p> With <code>-mcpu=v8</code>, <font SIZE="-1">GCC</font> generates code for the V8 variant of the <font SIZE="-1">SPARC</font> architecture. The only difference from V7 code is that the compiler emits the integer multiply and integer divide instructions which exist in <font SIZE="-1">SPARC-V8</font> but not in <font SIZE="-1">SPARC-V7</font>. With <code>-mcpu=supersparc</code>, the compiler additionally optimizes it for the SuperSPARC chip, as used in the SPARCStation 10, 1000 and 2000 series. </p>
<p> With <code>-mcpu=sparclite</code>, <font SIZE="-1">GCC</font> generates code for the SPARClite variant of the <font SIZE="-1">SPARC</font> architecture. This adds the integer multiply, integer divide step and scan (<tt>&quot;ffs&quot;</tt>) instructions which exist in SPARClite but not in <font SIZE="-1">SPARC-V7</font>. With <code>-mcpu=f930</code>, the compiler additionally optimizes it for the Fujitsu <font SIZE="-1">MB86930</font> chip, which is the original SPARClite, with no <font SIZE="-1">FPU</font>. With <code>-mcpu=f934</code>, the compiler additionally optimizes it for the Fujitsu <font SIZE="-1">MB86934</font> chip, which is the more recent SPARClite with <font SIZE="-1">FPU</font>. </p>
<p> With <code>-mcpu=sparclet</code>, <font SIZE="-1">GCC</font> generates code for the SPARClet variant of the <font SIZE="-1">SPARC</font> architecture. This adds the integer multiply, multiply/accumulate, integer divide step and scan (<tt>&quot;ffs&quot;</tt>) instructions which exist in SPARClet but not in <font SIZE="-1">SPARC-V7</font>. With <code>-mcpu=tsc701</code>, the compiler additionally optimizes it for the <font SIZE="-1">TEMIC</font> SPARClet chip. </p>
<p> With <code>-mcpu=v9</code>, <font SIZE="-1">GCC</font> generates code for the V9 variant of the <font SIZE="-1">SPARC</font> architecture. This adds 64-bit integer and floating-point move instructions, 3 additional floating-point condition code registers and conditional move instructions. With <code>-mcpu=ultrasparc</code>, the compiler additionally optimizes it for the Sun UltraSPARC I/II chips. With <code>-mcpu=ultrasparc3</code>, the compiler additionally optimizes it for the Sun UltraSPARC <font SIZE="-1">III</font> chip.</p>
<dt><code>-mtune=</code><i>cpu_type</i></p>
<dd>Set the instruction scheduling parameters for machine type <i>cpu_type</i>, but do not set the instruction set or register set that the option <code>-mcpu=</code><i>cpu_type</i> would. </p>
<p> The same values for <code>-mcpu=</code><i>cpu_type</i> can be used for <code>-mtune=</code><i>cpu_type</i>, but the only useful values are those that select a particular cpu implementation. Those are <code>cypress</code>, <code>supersparc</code>, <code>hypersparc</code>, <code>f930</code>, <code>f934</code>, <code>sparclite86x</code>, <code>tsc701</code>, <code>ultrasparc</code>, and <code>ultrasparc3</code>.</p>
<dt><code>-mv8plus</code></p>
<dd>
<dt><code>-mno-v8plus</code></p>
<dd>With <code>-mv8plus</code>, <font SIZE="-1">GCC</font> generates code for the <font SIZE="-1">SPARC-V8+</font> <font SIZE="-1">ABI</font>. The difference from the V8 <font SIZE="-1">ABI</font> is that the global and out registers are considered 64-bit wide. This is enabled by default on Solaris in 32-bit mode for all <font SIZE="-1">SPARC-V9</font> processors.</p>
<dt><code>-mvis</code></p>
<dd>
<dt><code>-mno-vis</code></p>
<dd>With <code>-mvis</code>, <font SIZE="-1">GCC</font> generates code that takes advantage of the UltraSPARC Visual Instruction Set extensions. The default is <code>-mno-vis</code>.</dl>
<p> These <code>-m</code> options are supported in addition to the above on <font SIZE="-1">SPARC-V9</font> processors in 64-bit environments:</p>
<dl>
<dt><code>-mlittle-endian</code></p>
<dd>Generate code for a processor running in little-endian mode. It is only available for a few configurations and most notably not on Solaris and Linux.</p>
<dt><code>-m32</code></p>
<dd>
<dt><code>-m64</code></p>
<dd>Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits.</p>
<dt><code>-mcmodel=medlow</code></p>
<dd>Generate code for the Medium/Low code model: 64-bit addresses, programs must be linked in the low 32 bits of memory. Programs can be statically or dynamically linked.</p>
<dt><code>-mcmodel=medmid</code></p>
<dd>Generate code for the Medium/Middle code model: 64-bit addresses, programs must be linked in the low 44 bits of memory, the text and data segments must be less than 2GB in size and the data segment must be located within 2GB of the text segment.</p>
<dt><code>-mcmodel=medany</code></p>
<dd>Generate code for the Medium/Anywhere code model: 64-bit addresses, programs may be linked anywhere in memory, the text and data segments must be less than 2GB in size and the data segment must be located within 2GB of the text segment.</p>
<dt><code>-mcmodel=embmedany</code></p>
<dd>Generate code for the Medium/Anywhere code model for embedded systems: 64-bit addresses, the text and data segments must be less than 2GB in size, both starting anywhere in memory (determined at link time). The global register <tt>%g4</tt> points to the base of the data segment. Programs are statically linked and <font SIZE="-1">PIC</font> is not supported.</p>
<dt><code>-mstack-bias</code></p>
<dd>
<dt><code>-mno-stack-bias</code></p>
<dd>With <code>-mstack-bias</code>, <font SIZE="-1">GCC</font> assumes that the stack pointer, and frame pointer if present, are offset by -2047 which must be added back when making stack frame references. This is the default in 64-bit mode. Otherwise, assume no such offset is present.</dl>
<p> These switches are supported in addition to the above on Solaris:</p>
<dl>
<dt><code>-threads</code></p>
<dd>Add support for multithreading using the Solaris threads library. This option sets flags for both the preprocessor and linker. This option does not affect the thread safety of object code produced by the compiler or that of libraries supplied with it.</p>
<dt><code>-pthreads</code></p>
<dd>Add support for multithreading using the <font SIZE="-1">POSIX</font> threads library. This option sets flags for both the preprocessor and linker. This option does not affect the thread safety of object code produced by the compiler or that of libraries supplied with it.</p>
<dt><code>-pthread</code></p>
<dd>This is a synonym for <code>-pthreads</code>.</dl>
<p> <i>Options for System V</i> </p>
<p> These additional options are available on System V Release 4 for compatibility with other compilers on those systems:</p>
<dl>
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
<p> <i>TMS320C3x/C4x Options</i> </p>
<p> These <code>-m</code> options are defined for TMS320C3x/C4x implementations:</p>
<dl>
<dt><code>-mcpu=</code><i>cpu_type</i></p>
<dd>Set the instruction set, register set, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>c30</code>, <code>c31</code>, <code>c32</code>, <code>c40</code>, and <code>c44</code>. The default is <code>c40</code> to generate code for the <font SIZE="-1">TMS320C40</font>.</p>
<dt><code>-mbig-memory</code></p>
<dd>
<dt><code>-mbig</code></p>
<dd>
<dt><code>-msmall-memory</code></p>
<dd>
<dt><code>-msmall</code></p>
<dd>Generates code for the big or small memory model. The small memory model assumed that all data fits into one 64K word page. At run-time the data page (<font SIZE="-1">DP</font>) register must be set to point to the 64K page containing the .bss and .data program sections. The big memory model is the default and requires reloading of the <font SIZE="-1">DP</font> register for every direct memory access.</p>
<dt><code>-mbk</code></p>
<dd>
<dt><code>-mno-bk</code></p>
<dd>Allow (disallow) allocation of general integer operands into the block count register <font SIZE="-1">BK</font>.</p>
<dt><code>-mdb</code></p>
<dd>
<dt><code>-mno-db</code></p>
<dd>Enable (disable) generation of code using decrement and branch, DBcond(D), instructions. This is enabled by default for the C4x. To be on the safe side, this is disabled for the C3x, since the maximum iteration count on the C3x is 2^{23 + 1} (but who iterates loops more than 2^{23} times on the C3x?). Note that <font SIZE="-1">GCC</font> will try to reverse a loop so that it can utilize the decrement and branch instruction, but will give up if there is more than one memory reference in the loop. Thus a loop where the loop counter is decremented can generate slightly more efficient code, in cases where the <font SIZE="-1">RPTB</font> instruction cannot be utilized.</p>
<dt><code>-mdp-isr-reload</code></p>
<dd>
<dt><code>-mparanoid</code></p>
<dd>Force the <font SIZE="-1">DP</font> register to be saved on entry to an interrupt service routine (<font SIZE="-1">ISR</font>), reloaded to point to the data section, and restored on exit from the <font SIZE="-1">ISR</font>. This should not be required unless someone has violated the small memory model by modifying the <font SIZE="-1">DP</font> register, say within an object library.</p>
<dt><code>-mmpyi</code></p>
<dd>
<dt><code>-mno-mpyi</code></p>
<dd>For the C3x use the 24-bit <font SIZE="-1">MPYI</font> instruction for integer multiplies instead of a library call to guarantee 32-bit results. Note that if one of the operands is a constant, then the multiplication will be performed using shifts and adds. If the <code>-mmpyi</code> option is not specified for the C3x, then squaring operations are performed inline instead of a library call.</p>
<dt><code>-mfast-fix</code></p>
<dd>
<dt><code>-mno-fast-fix</code></p>
<dd>The C3x/C4x <font SIZE="-1">FIX</font> instruction to convert a floating point value to an integer value chooses the nearest integer less than or equal to the floating point value rather than to the nearest integer. Thus if the floating point number is negative, the result will be incorrectly truncated an additional code is necessary to detect and correct this case. This option can be used to disable generation of the additional code required to correct the result.</p>
<dt><code>-mrptb</code></p>
<dd>
<dt><code>-mno-rptb</code></p>
<dd>Enable (disable) generation of repeat block sequences using the <font SIZE="-1">RPTB</font> instruction for zero overhead looping. The <font SIZE="-1">RPTB</font> construct is only used for innermost loops that do not call functions or jump across the loop boundaries. There is no advantage having nested <font SIZE="-1">RPTB</font> loops due to the overhead required to save and restore the <font SIZE="-1">RC</font>, <font SIZE="-1">RS</font>, and <font SIZE="-1">RE</font> registers. This is enabled by default with <code>-O2</code>.</p>
<dt><code>-mrpts=</code><i>count</i></p>
<dd>
<dt><code>-mno-rpts</code></p>
<dd>Enable (disable) the use of the single instruction repeat instruction <font SIZE="-1">RPTS</font>. If a repeat block contains a single instruction, and the loop count can be guaranteed to be less than the value <i>count</i>, <font SIZE="-1">GCC</font> will emit a <font SIZE="-1">RPTS</font> instruction instead of a <font SIZE="-1">RPTB</font>. If no value is specified, then a <font SIZE="-1">RPTS</font> will be emitted even if the loop count cannot be determined at compile time. Note that the repeated instruction following <font SIZE="-1">RPTS</font> does not have to be reloaded from memory each iteration, thus freeing up the <font SIZE="-1">CPU</font> buses for operands. However, since interrupts are blocked by this instruction, it is disabled by default.</p>
<dt><code>-mloop-unsigned</code></p>
<dd>
<dt><code>-mno-loop-unsigned</code></p>
<dd>The maximum iteration count when using <font SIZE="-1">RPTS</font> and <font SIZE="-1">RPTB</font> (and <font SIZE="-1">DB</font> on the C40) is 2^{31 + 1} since these instructions test if the iteration count is negative to terminate the loop. If the iteration count is unsigned there is a possibility than the 2^{31 + 1} maximum iteration count may be exceeded. This switch allows an unsigned iteration count.</p>
<dt><code>-mti</code></p>
<dd>Try to emit an assembler syntax that the <font SIZE="-1">TI</font> assembler (asm30) is happy with. This also enforces compatibility with the <font SIZE="-1">API</font> employed by the <font SIZE="-1">TI</font> C3x C compiler. For example, long doubles are passed as structures rather than in floating point registers.</p>
<dt><code>-mregparm</code></p>
<dd>
<dt><code>-mmemparm</code></p>
<dd>Generate code that uses registers (stack) for passing arguments to functions. By default, arguments are passed in registers where possible rather than by pushing arguments on to the stack.</p>
<dt><code>-mparallel-insns</code></p>
<dd>
<dt><code>-mno-parallel-insns</code></p>
<dd>Allow the generation of parallel instructions. This is enabled by default with <code>-O2</code>.</p>
<dt><code>-mparallel-mpy</code></p>
<dd>
<dt><code>-mno-parallel-mpy</code></p>
<dd>Allow the generation of MPY||ADD and MPY||SUB parallel instructions, provided <code>-mparallel-insns</code> is also specified. These instructions have tight register constraints which can pessimize the code generation of large functions.</dl>
<p> <i>V850 Options</i> </p>
<p> These <code>-m</code> options are defined for V850 implementations:</p>
<dl>
<dt><code>-mlong-calls</code></p>
<dd>
<dt><code>-mno-long-calls</code></p>
<dd>Treat all calls as being far away (near). If calls are assumed to be far away, the compiler will always load the functions address up into a register, and call indirect through the pointer.</p>
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
<dt><code>-mbig-switch</code></p>
<dd>Generate code suitable for big switch tables. Use this option only if the assembler/linker complain about out of range branches within a switch table.</p>
<dt><code>-mapp-regs</code></p>
<dd>This option will cause r2 and r5 to be used in the code generated by the compiler. This setting is the default.</p>
<dt><code>-mno-app-regs</code></p>
<dd>This option will cause r2 and r5 to be treated as fixed registers.</p>
<dt><code>-mv850e1</code></p>
<dd>Specify that the target processor is the V850E1. The preprocessor constants <code>__v850e1__</code> and <code>__v850e__</code> will be defined if this option is used.</p>
<dt><code>-mv850e</code></p>
<dd>Specify that the target processor is the V850E. The preprocessor constant <code>__v850e__</code> will be defined if this option is used. </p>
<p> If neither <code>-mv850</code> nor <code>-mv850e</code> nor <code>-mv850e1</code> are defined then a default target processor will be chosen and the relevant <code>__v850*__</code> preprocessor constant will be defined. </p>
<p> The preprocessor constants <code>__v850</code> and <code>__v851__</code> are always defined, regardless of which processor variant is the target.</p>
<dt><code>-mdisable-callt</code></p>
<dd>This option will suppress generation of the <font SIZE="-1">CALLT</font> instruction for the v850e and v850e1 flavors of the v850 architecture. The default is <code>-mno-disable-callt</code> which allows the <font SIZE="-1">CALLT</font> instruction to be used.</dl>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i> </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">VAX:</font></p>
<dl>
<dt><code>-munix</code></p>
<dd>Do not output certain jump instructions (<tt>&quot;aobleq&quot;</tt> and so on) that the Unix assembler for the <font SIZE="-1">VAX</font> cannot handle across long ranges.</p>
<dt><code>-mgnu</code></p>
<dd>Do output those jump instructions, on the assumption that you will assemble with the <font SIZE="-1">GNU</font> assembler.</p>
<dt><code>-mg</code></p>
<dd>Output code for g-format floating point numbers instead of d-format.</dl>
<p> <i>x86-64 Options</i> </p>
<p> These are listed under </p>
<p> <i>Xstormy16 Options</i> </p>
<p> These options are defined for Xstormy16:</p>
<dl>
<dt><code>-msim</code></p>
<dd>Choose startup files and linker script suitable for the simulator.</dl>
<p> <i>Xtensa Options</i> </p>
<p> These options are supported for Xtensa targets:</p>
<dl>
<dt><code>-mconst16</code></p>
<dd>
<dt><code>-mno-const16</code></p>
<dd>Enable or disable use of <tt>&quot;CONST16&quot;</tt> instructions for loading constant values. The <tt>&quot;CONST16&quot;</tt> instruction is currently not a standard option from Tensilica. When enabled, <tt>&quot;CONST16&quot;</tt> instructions are always used in place of the standard <tt>&quot;L32R&quot;</tt> instructions. The use of <tt>&quot;CONST16&quot;</tt> is enabled by default only if the <tt>&quot;L32R&quot;</tt> instruction is not available.</p>
<dt><code>-mfused-madd</code></p>
<dd>
<dt><code>-mno-fused-madd</code></p>
<dd>Enable or disable use of fused multiply/add and multiply/subtract instructions in the floating-point option. This has no effect if the floating-point option is not also enabled. Disabling fused multiply/add and multiply/subtract instructions forces the compiler to use separate instructions for the multiply and add/subtract operations. This may be desirable in some cases where strict <font SIZE="-1">IEEE</font> 754-compliant results are required: the fused multiply add/subtract instructions do not round the intermediate result, thereby producing results with <i>more</i> bits of precision than specified by the <font SIZE="-1">IEEE</font> standard. Disabling fused multiply add/subtract instructions also ensures that the program output is not sensitive to the compiler&#8217;s ability to combine multiply and add/subtract operations.</p>
<dt><code>-mtext-section-literals</code></p>
<dd>
<dt><code>-mno-text-section-literals</code></p>
<dd>Control the treatment of literal pools. The default is <code>-mno-text-section-literals</code>, which places literals in a separate section in the output file. This allows the literal pool to be placed in a data <font SIZE="-1">RAM/ROM</font>, and it also allows the linker to combine literal pools from separate object files to remove redundant literals and improve code size. With <code>-mtext-section-literals</code>, the literals are interspersed in the text section in order to keep them as close as possible to their references. This may be necessary for large assembly files.</p>
<dt><code>-mtarget-align</code></p>
<dd>
<dt><code>-mno-target-align</code></p>
<dd>When this option is enabled, <font SIZE="-1">GCC</font> instructs the assembler to automatically align instructions to reduce branch penalties at the expense of some code density. The assembler attempts to widen density instructions to align branch targets and the instructions following call instructions. If there are not enough preceding safe density instructions to align a target, no widening will be performed. The default is <code>-mtarget-align</code>. These options do not affect the treatment of auto-aligned instructions like <tt>&quot;LOOP&quot;</tt>, which the assembler will always align, either by widening density instructions or by inserting no-op instructions.</p>
<dt><code>-mlongcalls</code></p>
<dd>
<dt><code>-mno-longcalls</code></p>
<dd>When this option is enabled, <font SIZE="-1">GCC</font> instructs the assembler to translate direct calls to indirect calls unless it can determine that the target of a direct call is in the range allowed by the call instruction. This translation typically occurs for calls to functions in other source files. Specifically, the assembler translates a direct <tt>&quot;CALL&quot;</tt> instruction into an <tt>&quot;L32R&quot;</tt> followed by a <tt>&quot;CALLX&quot;</tt> instruction. The default is <code>-mno-longcalls</code>. This option should be used in programs where the call target can potentially be out of range. This option is implemented in the assembler, not the compiler, so the assembly code generated by <font SIZE="-1">GCC</font> will still show direct call instructions&#8212;look at the disassembled object code to see the actual instructions. Note that the assembler will use an indirect call for every cross-file call, not just those that really will be out of range.</dl>
<p> <i>zSeries Options</i> </p>
<p> These are listed under</p>
<h2>Options for Code Generation Conventions</h2>
<p>These machine-independent options control the interface conventions used in code generation. </p>
<p> Most of them have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. In the table below, only one of the forms is listed&#8212;the one which is not the default. You can figure out the other form by either removing <code>no-</code> or adding it.</p>
<dl>
<dt><code>-fbounds-check</code></p>
<dd>For front-ends that support it, generate additional code to check that indices used to access arrays are within the declared range. This is currently only supported by the Java and Fortran front-ends, where this option defaults to true and false respectively.</p>
<dt><code>-ftrapv</code></p>
<dd>This option generates traps for signed overflow on addition, subtraction, multiplication operations.</p>
<dt><code>-fwrapv</code></p>
<dd>This option instructs the compiler to assume that signed arithmetic overflow of addition, subtraction and multiplication wraps around using twos-complement representation. This flag enables some optimizations and disables others. This option is enabled by default for the Java front-end, as required by the Java language specification.</p>
<dt><code>-fexceptions</code></p>
<dd>Enable exception handling. Generates extra code needed to propagate exceptions. For some targets, this implies <font SIZE="-1">GCC</font> will generate frame unwind information for all functions, which can produce significant data size overhead, although it does not affect execution. If you do not specify this option, <font SIZE="-1">GCC</font> will enable it by default for languages like C<font SIZE="-2">++</font> which normally require exception handling, and disable it for languages like C that do not normally require it. However, you may need to enable this option when compiling C code that needs to interoperate properly with exception handlers written in C<font SIZE="-2">++</font>. You may also wish to disable this option if you are compiling older C<font SIZE="-2">++</font> programs that don&#8217;t use exception handling.</p>
<dt><code>-fnon-call-exceptions</code></p>
<dd>Generate code that allows trapping instructions to throw exceptions. Note that this requires platform-specific runtime support that does not exist everywhere. Moreover, it only allows <i>trapping</i> instructions to throw exceptions, i.e. memory references or floating point instructions. It does not allow exceptions to be thrown from arbitrary signal handlers such as <tt>&quot;SIGALRM&quot;</tt>.</p>
<dt><code>-funwind-tables</code></p>
<dd>Similar to <code>-fexceptions</code>, except that it will just generate any needed static data, but will not affect the generated code in any other way. You will normally not enable this option; instead, a language processor that needs this handling would enable it on your behalf.</p>
<dt><code>-fasynchronous-unwind-tables</code></p>
<dd>Generate unwind table in dwarf2 format, if supported by target machine. The table is exact at each instruction boundary, so it can be used for stack unwinding from asynchronous events (such as debugger or garbage collector).</p>
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
<dd>Allocate to an <tt>&quot;enum&quot;</tt> type only as many bytes as it needs for the declared range of possible values. Specifically, the <tt>&quot;enum&quot;</tt> type will be equivalent to the smallest integer type which has enough room. </p>
<p> <code>Warning:</code> the <code>-fshort-enums</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fshort-double</code></p>
<dd>Use the same size for <tt>&quot;double&quot;</tt> as for <tt>&quot;float&quot;</tt>. </p>
<p> <code>Warning:</code> the <code>-fshort-double</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fshort-wchar</code></p>
<dd>Override the underlying type for <code>wchar_t</code> to be <code>short unsigned int</code> instead of the default for the target. This option is useful for building programs to run under <font SIZE="-1">WINE</font>. </p>
<p> <code>Warning:</code> the <code>-fshort-wchar</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface.</p>
<dt><code>-fshared-data</code></p>
<dd>Requests that the data and non-<tt>&quot;const&quot;</tt> variables of this compilation be shared data rather than private data. The distinction makes sense only on certain operating systems, where shared data is shared between processes running the same program, while private data exists in one copy per process.</p>
<dt><code>-fno-common</code></p>
<dd>In C, allocate even uninitialized global variables in the data section of the object file, rather than generating them as common blocks. This has the effect that if the same variable is declared (without <tt>&quot;extern&quot;</tt>) in two different compilations, you will get an error when you link them. The only reason this might be useful is if you wish to verify that the program will work on other systems which always work this way.</p>
<dt><code>-fno-ident</code></p>
<dd>Ignore the <code>#ident</code> directive.</p>
<dt><code>-finhibit-size-directive</code></p>
<dd>Don&#8217;t output a <tt>&quot;.size&quot;</tt> assembler directive, or anything else that would cause trouble if the function is split in the middle, and the two halves are placed at locations far apart in memory. This option is used when compiling <i>crtstuff.c</i>; you should not need to use it for anything else.</p>
<dt><code>-fverbose-asm</code></p>
<dd>Put extra commentary information in the generated assembly code to make it more readable. This option is generally only of use to those who actually need to read the generated assembly code (perhaps while debugging the compiler itself). </p>
<p> <code>-fno-verbose-asm</code>, the default, causes the extra information to be omitted and is useful when comparing two assembler files.</p>
<dt><code>-fpic</code></p>
<dd>Generate position-independent code (<font SIZE="-1">PIC</font>) suitable for use in a shared library, if supported for the target machine. Such code accesses all constant addresses through a global offset table (<font SIZE="-1">GOT</font>). The dynamic loader resolves the <font SIZE="-1">GOT</font> entries when the program starts (the dynamic loader is not part of <font SIZE="-1">GCC</font>; it is part of the operating system). If the <font SIZE="-1">GOT</font> size for the linked executable exceeds a machine-specific maximum size, you get an error message from the linker indicating that <code>-fpic</code> does not work; in that case, recompile with <code>-fPIC</code> instead. (These maximums are 8k on the <font SIZE="-1">SPARC</font> and 32k on the m68k and <font SIZE="-1">RS/6000</font>. The 386 has no such limit.) </p>
<p> Position-independent code requires special support, and therefore works only on certain machines. For the 386, <font SIZE="-1">GCC</font> supports <font SIZE="-1">PIC</font> for System V but not for the Sun 386i. Code generated for the <font SIZE="-1">IBM</font> <font SIZE="-1">RS/6000</font> is always position-independent.</p>
<dt><code>-fPIC</code></p>
<dd>If supported for the target machine, emit position-independent code, suitable for dynamic linking and avoiding any limit on the size of the global offset table. This option makes a difference on the m68k, PowerPC and <font SIZE="-1">SPARC</font>. </p>
<p> Position-independent code requires special support, and therefore works only on certain machines.</p>
<dt><code>-fpie</code></p>
<dd>
<dt><code>-fPIE</code></p>
<dd>These options are similar to <code>-fpic</code> and <code>-fPIC</code>, but generated position independent code can be only linked into executables. Usually these options are used when <code>-pie</code> <font SIZE="-1">GCC</font> option will be used during linking.</p>
<dt><code>-fno-jump-tables</code></p>
<dd>Do not use jump tables for switch statements even where it would be more efficient than other code generation strategies. This option is of use in conjunction with <code>-fpic</code> or <code>-fPIC</code> for building code which forms part of a dynamic linker and cannot reference the address of a jump table. On some targets, jump tables do not require a <font SIZE="-1">GOT</font> and this option is not needed.</p>
<dt><code>-ffixed-</code><i>reg</i></p>
<dd>Treat the register named <i>reg</i> as a fixed register; generated code should never refer to it (except perhaps as a stack pointer, frame pointer or in some other fixed role). </p>
<p> <i>reg</i> must be the name of a register. The register names accepted are machine-specific and are defined in the <tt>&quot;REGISTER_NAMES&quot;</tt> macro in the machine description macro file. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice.</p>
<dt><code>-fcall-used-</code><i>reg</i></p>
<dd>Treat the register named <i>reg</i> as an allocable register that is clobbered by function calls. It may be allocated for temporaries or variables that do not live across a call. Functions compiled this way will not save and restore the register <i>reg</i>. </p>
<p> It is an error to used this flag with the frame pointer or stack pointer. Use of this flag for other registers that have fixed pervasive roles in the machine&#8217;s execution model will produce disastrous results. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice.</p>
<dt><code>-fcall-saved-</code><i>reg</i></p>
<dd>Treat the register named <i>reg</i> as an allocable register saved by functions. It may be allocated even for temporaries or variables that live across a call. Functions compiled this way will save and restore the register <i>reg</i> if they use it. </p>
<p> It is an error to used this flag with the frame pointer or stack pointer. Use of this flag for other registers that have fixed pervasive roles in the machine&#8217;s execution model will produce disastrous results. </p>
<p> A different sort of disaster will result from the use of this flag for a register in which function values may be returned. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice.</p>
<dt><code>-fpack-struct[=</code><i>n</i><code>]</code></p>
<dd>Without a value specified, pack all structure members together without holes. When a value is specified (which must be a small power of two), pack structure members according to this value, representing the maximum alignment (that is, objects with default alignment requirements larger than this will be output potentially unaligned at the next fitting location. </p>
<p> <code>Warning:</code> the <code>-fpack-struct</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Additionally, it makes the code suboptimal. Use it to conform to a non-default application binary interface.</p>
<dt><code>-finstrument-functions</code></p>
<dd>Generate instrumentation calls for entry and exit to functions. Just after function entry and just before function exit, the following profiling functions will be called with the address of the current function and its call site. (On some platforms, <tt>&quot;__builtin_return_address&quot;</tt> does not work beyond the current function, so the call site information may not be available to the profiling functions otherwise.) </p>
<pre> void __cyg_profile_func_enter (void *this_fn,
 void *call_site);
 void __cyg_profile_func_exit (void *this_fn,
 void *call_site);</pre>
<p>The first argument is the address of the start of the current function, which may be looked up exactly in the symbol table. </p>
<p> This instrumentation is also done for functions expanded inline in other functions. The profiling calls will indicate where, conceptually, the inline function is entered and exited. This means that addressable versions of such functions must be available. If all your uses of a function are expanded inline, this may mean an additional expansion of code size. If you use <code>extern inline</code> in your C code, an addressable version of such functions must be provided. (This is normally the case anyways, but if you get lucky and the optimizer always expands the functions inline, you might have gotten away without providing static copies.) </p>
<p> A function may be given the attribute <tt>&quot;no_instrument_function&quot;</tt>, in which case this instrumentation will not be done. This can be used, for example, for the profiling functions listed above, high-priority interrupt routines, and any functions from which the profiling functions cannot safely be called (perhaps signal handlers, if the profiling routines generate output or allocate memory).</p>
<dt><code>-fstack-check</code></p>
<dd>Generate code to verify that you do not go beyond the boundary of the stack. You should specify this flag if you are running in an environment with multiple threads, but only rarely need to specify it in a single-threaded environment since stack overflow is automatically detected on nearly all systems if there is only one stack. </p>
<p> Note that this switch does not actually cause checking to be done; the operating system must do that. The switch causes generation of code to ensure that the operating system sees the stack being extended.</p>
<dt><code>-fstack-limit-register=</code><i>reg</i></p>
<dd>
<dt><code>-fstack-limit-symbol=</code><i>sym</i></p>
<dd>
<dt><code>-fno-stack-limit</code></p>
<dd>Generate code to ensure that the stack does not grow beyond a certain value, either the value of a register or the address of a symbol. If the stack would grow beyond the value, a signal is raised. For most targets, the signal is raised before the stack overruns the boundary, so it is possible to catch the signal without taking special precautions. </p>
<p> For instance, if the stack starts at absolute address <code>0x80000000</code> and grows downwards, you can use the flags <code>-fstack-limit-symbol=__stack_limit</code> and <code>-Wl,&#8211;defsym,__stack_limit=0x7ffe0000</code> to enforce a stack limit of 128KB. Note that this may only work with the <font SIZE="-1">GNU</font> linker.</p>
<dt><code>-fargument-alias</code></p>
<dd>
<dt><code>-fargument-noalias</code></p>
<dd>
<dt><code>-fargument-noalias-global</code></p>
<dd>Specify the possible relationships among parameters and between parameters and global data. </p>
<p> <code>-fargument-alias</code> specifies that arguments (parameters) may alias each other and may alias global storage.<code>-fargument-noalias</code> specifies that arguments do not alias each other, but may alias global storage.<code>-fargument-noalias-global</code> specifies that arguments do not alias each other and do not alias global storage. </p>
<p> Each language will automatically use whatever option is required by the language standard. You should not need to use these options yourself.</p>
<dt><code>-fleading-underscore</code></p>
<dd>This option and its counterpart, <code>-fno-leading-underscore</code>, forcibly change the way C symbols are represented in the object file. One use is to help link with legacy assembly code. </p>
<p> <code>Warning:</code> the <code>-fleading-underscore</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface. Not all targets provide complete support for this switch.</p>
<dt><code>-ftls-model=</code><i>model</i></p>
<dd>Alter the thread-local storage model to be used. The <i>model</i> argument should be one of <tt>&quot;global-dynamic&quot;</tt>, <tt>&quot;local-dynamic&quot;</tt>, <tt>&quot;initial-exec&quot;</tt> or <tt>&quot;local-exec&quot;</tt>. </p>
<p> The default without <code>-fpic</code> is <tt>&quot;initial-exec&quot;</tt>; with <code>-fpic</code> the default is <tt>&quot;global-dynamic&quot;</tt>.</p>
<dt><code>-fvisibility=</code><i>default|internal|hidden|protected</i></p>
<dd>Set the default <font SIZE="-1">ELF</font> image symbol visibility to the specified option&#8212;all symbols will be marked with this unless overridden within the code. Using this feature can very substantially improve linking and load times of shared object libraries, produce more optimized code, provide near-perfect <font SIZE="-1">API</font> export and prevent symbol clashes. It is <code>strongly</code> recommended that you use this in any shared objects you distribute. </p>
<p> Despite the nomenclature, <tt>&quot;default&quot;</tt> always means public ie; available to be linked against from outside the shared object. <tt>&quot;protected&quot;</tt> and <tt>&quot;internal&quot;</tt> are pretty useless in real-world usage so the only other commonly used option will be <tt>&quot;hidden&quot;</tt>. The default if <code>-fvisibility</code> isn&#8217;t specified is <tt>&quot;default&quot;</tt>, i.e., make every symbol public&#8212;this causes the same behavior as previous versions of <font SIZE="-1">GCC</font>. </p>
<p> A good explanation of the benefits offered by ensuring <font SIZE="-1">ELF</font> symbols have the correct visibility is given by &#8220;How To Write Shared Libraries&#8221; by Ulrich Drepper (which can be found at &lt;<code><a rel="nofollow" href="http://people.redhat.com/~drepper/">http://people.redhat.com/~drepper/</a></code>&gt;)&#8212;however a superior solution made possible by this option to marking things hidden when the default is public is to make the default hidden and mark things public. This is the norm with <font SIZE="-1">DLL</font>&#8216;s on Windows and with <code>-fvisibility=hidden</code> and <tt>&quot;__attribute__ ((visibility(&quot;default&quot;)))&quot;</tt> instead of <tt>&quot;__declspec(dllexport)&quot;</tt> you get almost identical semantics with identical syntax. This is a great boon to those working with cross-platform projects. </p>
<p> For those adding visibility support to existing code, you may find <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility</code> of use. This works by you enclosing the declarations you wish to set visibility for with (for example) <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility push(hidden)</code> and <code>#pragma </code><font SIZE="-1"><code>GCC</code></font><code> visibility pop</code>. Bear in mind that symbol visibility should be viewed <code>as part of the </code><font SIZE="-1"><code>API</code></font><code> interface contract</code> and thus all new code should always specify visibility when it is not the default ie; declarations only for use within the local <font SIZE="-1">DSO</font> should <code>always</code> be marked explicitly as hidden as so to avoid <font SIZE="-1">PLT</font> indirection overheads&#8212;making this abundantly clear also aids readability and self-documentation of the code. Note that due to <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> specification requirements, operator new and operator delete must always be of default visibility. </p>
<p> An overview of these techniques, their benefits and how to use them is at &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/wiki/Visibility">http://gcc.gnu.org/wiki/Visibility</a></code>&gt;.</dl>
<h2>Environment</h2>
<p>This section describes several environment variables that affect how <font SIZE="-1">GCC</font> operates. Some of them work by specifying directories or prefixes to use when searching for various kinds of files. Some are used to specify other aspects of the compilation environment. </p>
<p> Note that you can also specify places to search using options such as <code>-B</code>, <code>-I</code> and <code>-L</code>. These take precedence over places specified using environment variables, which in turn take precedence over those specified by the configuration of <font SIZE="-1">GCC</font>.</p>
<dl>
<dt><font SIZE="-1"><code>LANG</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LC_CTYPE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LC_MESSAGES</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LC_ALL</code></font></p>
<dd>These environment variables control the way that <font SIZE="-1">GCC</font> uses localization information that allow <font SIZE="-1">GCC</font> to work with different national conventions. <font SIZE="-1">GCC</font> inspects the locale categories <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font> if it has been configured to do so. These locale categories can be set to any value supported by your installation. A typical value is <code>en_GB.UTF-8</code> for English in the United Kingdom encoded in <font SIZE="-1">UTF-8</font>. </p>
<p> The <font SIZE="-1"><code>LC_CTYPE</code></font> environment variable specifies character classification. <font SIZE="-1">GCC</font> uses it to determine the character boundaries in a string; this is needed for some multibyte encodings that contain quote and escape characters that would otherwise be interpreted as a string end or escape. </p>
<p> The <font SIZE="-1"><code>LC_MESSAGES</code></font> environment variable specifies the language to use in diagnostic messages. </p>
<p> If the <font SIZE="-1"><code>LC_ALL</code></font> environment variable is set, it overrides the value of <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font>; otherwise, <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font> default to the value of the <font SIZE="-1"><code>LANG</code></font> environment variable. If none of these variables are set, <font SIZE="-1">GCC</font> defaults to traditional C English behavior.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd>If <font SIZE="-1"><code>TMPDIR</code></font> is set, it specifies the directory to use for temporary files. <font SIZE="-1">GCC</font> uses temporary files to hold the output of one stage of compilation which is to be used as input to the next stage: for example, the output of the preprocessor, which is the input to the compiler proper.</p>
<dt><font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font></p>
<dd>If <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is set, it specifies a prefix to use in the names of the subprograms executed by the compiler. No slash is added when this prefix is combined with the name of a subprogram, but you can specify a prefix that ends with a slash if you wish. </p>
<p> If <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is not set, <font SIZE="-1">GCC</font> will attempt to figure out an appropriate prefix to use based on the pathname it was invoked with. </p>
<p> If <font SIZE="-1">GCC</font> cannot find the subprogram using the specified prefix, it tries looking in the usual places for the subprogram. </p>
<p> The default value of <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is <i>prefix/lib/gcc/</i> where <i>prefix</i> is the value of <tt>&quot;prefix&quot;</tt> when you ran the <i>configure</i> script. </p>
<p> Other prefixes specified with <code>-B</code> take precedence over this prefix. </p>
<p> This prefix is also used for finding files such as <i>crt0.o</i> that are used for linking. </p>
<p> In addition, the prefix is used in an unusual way in finding the directories to search for header files. For each of the standard directories whose name normally begins with <code>/usr/local/lib/gcc</code> (more precisely, with the value of <font SIZE="-1"><code>GCC_INCLUDE_DIR</code></font>), <font SIZE="-1">GCC</font> tries replacing that beginning with the specified prefix to produce an alternate directory name. Thus, with <code>-Bfoo/</code>, <font SIZE="-1">GCC</font> will search <i>foo/bar</i> where it would normally search <i>/usr/local/lib/bar</i>. These alternate directories are searched first; the standard directories come next.</p>
<dt><font SIZE="-1"><code>COMPILER_PATH</code></font></p>
<dd>The value of <font SIZE="-1"><code>COMPILER_PATH</code></font> is a colon-separated list of directories, much like <font SIZE="-1"><code>PATH</code></font>. <font SIZE="-1">GCC</font> tries the directories thus specified when searching for subprograms, if it can&#8217;t find the subprograms using <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>.</p>
<dt><font SIZE="-1"><code>LIBRARY_PATH</code></font></p>
<dd>The value of <font SIZE="-1"><code>LIBRARY_PATH</code></font> is a colon-separated list of directories, much like <font SIZE="-1"><code>PATH</code></font>. When configured as a native compiler, <font SIZE="-1">GCC</font> tries the directories thus specified when searching for special linker files, if it can&#8217;t find them using <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. Linking using <font SIZE="-1">GCC</font> also uses these directories when searching for ordinary libraries for the <code>-l</code> option (but directories specified with <code>-L</code> come first).</p>
<dt><font SIZE="-1"><code>LANG</code></font></p>
<dd>This variable is used to pass locale information to the compiler. One way in which this information is used is to determine the character set to be used when character literals, string literals and comments are parsed in C and C<font SIZE="-2">++</font>. When the compiler is configured to allow multibyte characters, the following values for <font SIZE="-1"><code>LANG</code></font> are recognized:</p>
<dl>
<dd>
<dl>
<dt><code>C-JIS</code></p>
<dd>Recognize <font SIZE="-1">JIS</font> characters.</p>
<dt><code>C-SJIS</code></p>
<dd>Recognize <font SIZE="-1">SJIS</font> characters.</p>
<dt><code>C-EUCJP</code></p>
<dd>Recognize <font SIZE="-1">EUCJP</font> characters.</dl>
</dl>
<dl>
<dd>If <font SIZE="-1"><code>LANG</code></font> is not defined, or if it has some other value, then the compiler will use mblen and mbtowc as defined by the default locale to recognize and translate multibyte characters.</dl>
</dl>
<p> Some additional environments variables affect the behavior of the preprocessor.</p>
<dl>
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
<p>For instructions on reporting bugs, see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/bugs.html">http://gcc.gnu.org/bugs.html</a></code>&gt;.</p>
<h2>Footnotes</h2>
<dl>
<dt>1.</p>
<dd>On some systems, <code>gcc -shared</code> needs to build supplementary stub code for constructors to work. On multi-libbed systems, <code>gcc -shared</code> must select the correct support libraries to link against. Failing to supply the correct flags may lead to subtle defects. Supplying them in cases where they are not necessary is innocuous.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-gpl/">gpl</a></i>(7), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), <i><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></i>(7), <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1), <i><a href="/docs/linux/man/1-gcov/">gcov</a></i>(1), <i><a href="/docs/linux/man/1-as/">as</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), <i><a href="/docs/linux/man/1-gdb/">gdb</a></i>(1), <i><a href="/docs/linux/man/1-adb/">adb</a></i>(1), <i><a href="/docs/linux/man/1-dbx/">dbx</a></i>(1), <i><a href="/docs/linux/man/1-sdb/">sdb</a></i>(1) and the Info entries for <i>gcc</i>, <i>cpp</i>, <i>as</i>, <i>ld</i>, <i>binutils</i> and <i>gdb</i>.</p>
<h2>Author</h2>
<p>See the Info entry for <code>gcc</code>, or &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/gcc/Contributors.html">http://gcc.gnu.org/onlinedocs/gcc/Contributors.html</a></code>&gt;, for contributors to <font SIZE="-1">GCC</font>.</p>
<h2>Copyright</h2>
<p>Copyright (c) 1988, 1989, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre> A GNU Manual</pre>
<p>(b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre> You have freedom to copy and modify this GNU Manual, like GNU
 software. Copies published by the Free Software Foundation raise
 funds for GNU development.</pre>
