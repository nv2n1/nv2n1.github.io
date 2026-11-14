---
title: "msp430-gcc(1)"
name: "msp430-gcc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-gcc/"
description: "gcc – GNU project C and C++ compiler"
---

<h2 class="name">NAME</h2>
<p> gcc &#8211; <font SIZE="-1">GNU</font> project C and C<font SIZE="-2">++</font> compiler </p>
<h2>SYNOPSIS</h2>
<p> gcc [<code>-c</code>|<code>-S</code>|<code>-E</code>] [<code>-std=</code><i>standard</i>]<br />
&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>]<br />
&nbsp;<wbr>[<code>-W</code><i>warn</i>&#8230;]&nbsp;<wbr>[<code>-pedantic</code>]<br />
&nbsp;<wbr>[<code>-I</code><i>dir</i>&#8230;]&nbsp;<wbr>[<code>-L</code><i>dir</i>&#8230;]<br />
&nbsp;<wbr>[<code>-D</code><i>macro</i>[=<i>defn</i>]&#8230;]&nbsp;<wbr>[<code>-U</code><i>macro</i>]<br />
&nbsp;<wbr>[<code>-f</code><i>option</i>&#8230;]&nbsp;<wbr>[<code>-m</code><i>machine-option</i>&#8230;]<br />
&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr><i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder. <code>g++</code> accepts mostly the same options as <code>gcc</code>.</p>
<h2>DESCRIPTION</h2>
<p> When you invoke <font SIZE="-1">GCC</font>, it normally does preprocessing, compilation, assembly and linking. The &#8220;overall options&#8221; allow you to stop this process at an intermediate stage. For example, the <code>-c</code> option says not to run the linker. Then the output consists of object files output by the assembler. </p>
<p> Other options are passed on to one stage of processing. Some options control the preprocessor and others the compiler itself. Yet other options control the assembler and linker; most of these are not documented here, since you rarely need to use any of them. </p>
<p> Most of the command line options that you can use with <font SIZE="-1">GCC</font> are useful for C programs; when an option is only useful with another language (usually C<font SIZE="-2">++</font>), the explanation says so explicitly. If the description for a particular option does not mention a source language, you can use that option with all supported languages. </p>
<p> The <code>gcc</code> program accepts options and file names as operands. Many options have multi-letter names; therefore multiple single-letter options may <i>not</i> be grouped: <code>-dr</code> is very different from <code>-d -r</code>. </p>
<p> You can mix options and other arguments. For the most part, the order you use doesn&#8217;t matter. Order does matter when you use several options of the same kind; for example, if you specify <code>-L</code> more than once, the directories are searched in the order specified. </p>
<p> Many options have long names starting with <code>-f</code> or with <code>-W</code>&#8212;for example, <code>-fforce-mem</code>, <code>-fstrength-reduce</code>, <code>-Wformat</code> and so on. Most of these have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.</p>
<h2>OPTIONS</h2>
<h2>Option Summary</h2>
<p> Here is a summary of all the options, grouped by type. Explanations are in the following sections. </p>
<dl>
<dt><i>Overall Options</i></p>
<dd> <code>-c -S -E -o</code> <i>file</i> <code>-pipe -pass-exit-codes -x</code> <i>language</i> <code>-v -### &#8211;help &#8211;target-help &#8211;version</code> </p>
<dt><i>C Language Options</i></p>
<dd> <code>-ansi -std=</code><i>standard</i> <code>-aux-info</code> <i>filename</i> <code>-fno-asm -fno-builtin -fno-builtin-</code><i>function</i> <code>-fhosted -ffreestanding -trigraphs -no-integrated-cpp -traditional -traditional-cpp -fallow-single-precision -fcond-mismatch -fsigned-bitfields -fsigned-char -funsigned-bitfields -funsigned-char -fwritable-strings</code> </p>
<dt><i>C<font SIZE="-2">++</font> Language Options</i></p>
<dd> <code>-fno-access-control -fcheck-new -fconserve-space -fno-const-strings -fdollars-in-identifiers -fno-elide-constructors -fno-enforce-eh-specs -fexternal-templates -falt-external-templates -ffor-scope -fno-for-scope -fno-gnu-keywords -fno-implicit-templates -fno-implicit-inline-templates -fno-implement-inlines -fms-extensions -fno-nonansi-builtins -fno-operator-names -fno-optional-diags -fpermissive -frepo -fno-rtti -fstats -ftemplate-depth-</code><i>n</i> <code>-fuse-cxa-atexit -fvtable-gc -fno-weak -nostdinc++ -fno-default-inline -Wabi -Wctor-dtor-privacy -Wnon-virtual-dtor -Wreorder -Weffc++ -Wno-deprecated -Wno-non-template-friend -Wold-style-cast -Woverloaded-virtual -Wno-pmf-conversions -Wsign-promo -Wsynth</code> </p>
<dt><i>Objective-C Language Options</i></p>
<dd> <code>-fconstant-string-class=</code><i>class-name</i> <code>-fgnu-runtime -fnext-runtime -gen-decls -Wno-protocol -Wselector</code> </p>
<dt><i>Language Independent Options</i></p>
<dd> <code>-fmessage-length=</code><i>n</i> <code>-fdiagnostics-show-location=</code>[<code>once</code>|<code>every-line</code>] </p>
<dt><i>Warning Options</i></p>
<dd> <code>-fsyntax-only -pedantic -pedantic-errors -w -W -Wall -Waggregate-return -Wcast-align -Wcast-qual -Wchar-subscripts -Wcomment -Wconversion -Wno-deprecated-declarations -Wdisabled-optimization -Wdiv-by-zero -Werror -Wfloat-equal -Wformat -Wformat=2 -Wformat-nonliteral -Wformat-security -Wimplicit -Wimplicit-int -Wimplicit-function-declaration -Werror-implicit-function-declaration -Wimport -Winline -Wlarger-than-</code><i>len</i> <code>-Wlong-long -Wmain -Wmissing-braces -Wmissing-format-attribute -Wmissing-noreturn -Wmultichar -Wno-format-extra-args -Wno-format-y2k -Wno-import -Wpacked -Wpadded -Wparentheses -Wpointer-arith -Wredundant-decls -Wreturn-type -Wsequence-point -Wshadow -Wsign-compare -Wswitch -Wsystem-headers -Wtrigraphs -Wundef -Wuninitialized -Wunknown-pragmas -Wunreachable-code -Wunused -Wunused-function -Wunused-label -Wunused-parameter -Wunused-value -Wunused-variable -Wwrite-strings</code> </p>
<dt><i>C-only Warning Options</i></p>
<dd> <code>-Wbad-function-cast -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Wstrict-prototypes -Wtraditional</code> </p>
<dt><i>Debugging Options</i></p>
<dd> <code>-d</code><i>letters</i> <code>-dumpspecs -dumpmachine -dumpversion -fdump-unnumbered -fdump-translation-unit</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-class-hierarchy</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-original</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-optimized</code>[<code>&#8211;</code><i>n</i>] <code>-fdump-tree-inlined</code>[<code>&#8211;</code><i>n</i>] <code>-fmem-report -fpretend-float -fprofile-arcs -fsched-verbose=</code><i>n</i> <code>-ftest-coverage -ftime-report -g -g</code><i>level</i> <code>-gcoff -gdwarf -gdwarf-1 -gdwarf-1+ -gdwarf-2 -ggdb -gstabs -gstabs+ -gvms -gxcoff -gxcoff+ -p -pg -print-file-name=</code><i>library</i> <code>-print-libgcc-file-name -print-multi-directory -print-multi-lib -print-prog-name=</code><i>program</i> <code>-print-search-dirs -Q -save-temps -time</code> </p>
<dt><i>Optimization Options</i></p>
<dd> <code>-falign-functions=</code><i>n</i> <code>-falign-jumps=</code><i>n</i> <code>-falign-labels=</code><i>n</i> <code>-falign-loops=</code><i>n</i> <code>-fbounds-check -fbranch-probabilities -fcaller-saves -fcprop-registers -fcse-follow-jumps -fcse-skip-blocks -fdata-sections -fdelayed-branch -fdelete-null-pointer-checks -fexpensive-optimizations -ffast-math -ffloat-store -fforce-addr -fforce-mem -ffunction-sections -fgcse -fgcse-lm -fgcse-sm -finline-functions -finline-limit=</code><i>n</i> <code>-fkeep-inline-functions -fkeep-static-consts -fmerge-constants -fmerge-all-constants -fmove-all-movables -fno-branch-count-reg -fno-default-inline -fno-defer-pop -fno-function-cse -fno-guess-branch-probability -fno-inline -fno-math-errno -fno-peephole -fno-peephole2 -funsafe-math-optimizations -fno-trapping-math -fomit-frame-pointer -foptimize-register-move -foptimize-sibling-calls -fprefetch-loop-arrays -freduce-all-givs -fregmove -frename-registers -frerun-cse-after-loop -frerun-loop-opt -fschedule-insns -fschedule-insns2 -fno-sched-interblock -fno-sched-spec -fsched-spec-load -fsched-spec-load-dangerous -fsingle-precision-constant -fssa -fssa-ccp -fssa-dce -fstrength-reduce -fstrict-aliasing -fthread-jumps -ftrapv -funroll-all-loops -funroll-loops &#8211;param</code> <i>name</i><code>=</code><i>value</i> <code>-O -O0 -O1 -O2 -O3 -Os</code> </p>
<dt><i>Preprocessor Options</i></p>
<dd> <code>-$ -A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -dD -dI -dM -dN -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-E -H -idirafter</code> <i>dir</i> <code>-include</code> <i>file</i> <code>-imacros</code> <i>file</i> <code>-iprefix</code> <i>file</i> <code>-iwithprefix</code> <i>dir</i> <code>-iwithprefixbefore</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-M -MM -MF -MG -MP -MQ -MT -nostdinc -P -remap -trigraphs -undef -U</code><i>macro</i> <code>-Wp,</code><i>option</i> </p>
<dt><i>Assembler Option</i></p>
<dd> <code>-Wa,</code><i>option</i> </p>
<dt><i>Linker Options</i></p>
<dd> <i>object-file-name</i> <code>-l</code><i>library</i> <code>-nostartfiles -nodefaultlibs -nostdlib -s -static -static-libgcc -shared -shared-libgcc -symbolic -Wl,</code><i>option</i> <code>-Xlinker</code> <i>option</i> <code>-u</code> <i>symbol</i> </p>
<dt><i>Directory Options</i></p>
<dd> <code>-B</code><i>prefix</i> <code>-I</code><i>dir</i> <code>-I- -L</code><i>dir</i> <code>-specs=</code><i>file</i> </p>
<dt><i>Target Options</i></p>
<dd> <code>-b</code> <i>machine</i> <code>-V</code> <i>version</i> </p>
<dt><i>Machine Dependent Options</i></p>
<dd> <i>M680x0 Options</i> </p>
<p> <code>-m68000 -m68020 -m68020-40 -m68020-60 -m68030 -m68040 -m68060 -mcpu32 -m5200 -m68881 -mbitfield -mc68000 -mc68020 -mfpa -mnobitfield -mrtd -mshort -msoft-float -mpcrel -malign-int -mstrict-align</code> </p>
<p> <i>M68hc1x Options</i> </p>
<p> <code>-m6811 -m6812 -m68hc11 -m68hc12 -mauto-incdec -mshort -msoft-reg-count=</code><i>count</i> </p>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i> </p>
<p> <code>-mg -mgnu -munix</code> </p>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i> </p>
<p> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mcmodel=</code><i>code-model</i> <code>-m32 -m64 -mapp-regs -mbroken-saverestore -mcypress -mfaster-structs -mflat -mfpu -mhard-float -mhard-quad-float -mimpure-text -mlive-g0 -mno-app-regs -mno-faster-structs -mno-flat -mno-fpu -mno-impure-text -mno-stack-bias -mno-unaligned-doubles -msoft-float -msoft-quad-float -msparclite -mstack-bias -msupersparc -munaligned-doubles -mv8</code> </p>
<p> <i>Convex Options</i> </p>
<p> <code>-mc1 -mc2 -mc32 -mc34 -mc38 -margcount -mnoargcount -mlong32 -mlong64 -mvolatile-cache -mvolatile-nocache</code> </p>
<p> <i></i><font SIZE="-1"><i>AMD29K</i></font><i> Options</i> </p>
<p> <code>-m29000 -m29050 -mbw -mnbw -mdw -mndw -mlarge -mnormal -msmall -mkernel-registers -mno-reuse-arg-regs -mno-stack-check -mno-storem-bug -mreuse-arg-regs -msoft-float -mstack-check -mstorem-bug -muser-registers</code> </p>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i> </p>
<p> <code>-mapcs-frame -mno-apcs-frame -mapcs-26 -mapcs-32 -mapcs-stack-check -mno-apcs-stack-check -mapcs-float -mno-apcs-float -mapcs-reentrant -mno-apcs-reentrant -msched-prolog -mno-sched-prolog -mlittle-endian -mbig-endian -mwords-little-endian -malignment-traps -mno-alignment-traps -msoft-float -mhard-float -mfpe -mthumb-interwork -mno-thumb-interwork -mcpu=</code><i>name</i> <code>-march=</code><i>name</i> <code>-mfpe=</code><i>name</i> <code>-mstructure-size-boundary=</code><i>n</i> <code>-mbsd -mxopen -mno-symrename -mabort-on-noreturn -mlong-calls -mno-long-calls -msingle-pic-base -mno-single-pic-base -mpic-register=</code><i>reg</i> <code>-mnop-fun-dllimport -mpoke-function-name -mthumb -marm -mtpcs-frame -mtpcs-leaf-frame -mcaller-super-interworking -mcallee-super-interworking</code> </p>
<p> <i></i><font SIZE="-1"><i>MN10200</i></font><i> Options</i> </p>
<p> <code>-mrelax</code> </p>
<p> <i></i><font SIZE="-1"><i>MN10300</i></font><i> Options</i> </p>
<p> <code>-mmult-bug -mno-mult-bug -mam33 -mno-am33 -mno-crt0 -mrelax</code> </p>
<p> <i>M32R/D Options</i> </p>
<p> <code>-m32rx -m32r -mcode-model=</code><i>model-type</i> <code>-msdata=</code><i>sdata-type</i> <code>-G</code> <i>num</i> </p>
<p> <i>M88K Options</i> </p>
<p> <code>-m88000 -m88100 -m88110 -mbig-pic -mcheck-zero-division -mhandle-large-shift -midentify-revision -mno-check-zero-division -mno-ocs-debug-info -mno-ocs-frame-position -mno-optimize-arg-area -mno-serialize-volatile -mno-underscores -mocs-debug-info -mocs-frame-position -moptimize-arg-area -mserialize-volatile -mshort-data-</code><i>num</i> <code>-msvr3 -msvr4 -mtrap-large-shift -muse-div-instruction -mversion-03.00 -mwarn-passed-structs</code> </p>
<p> <i></i><font SIZE="-1"><i>RS/6000</i></font><i> and PowerPC Options</i> </p>
<p> <code>-mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mpower -mno-power -mpower2 -mno-power2 -mpowerpc -mpowerpc64 -mno-powerpc -maltivec -mno-altivec -mpowerpc-gpopt -mno-powerpc-gpopt -mpowerpc-gfxopt -mno-powerpc-gfxopt -mnew-mnemonics -mold-mnemonics -mfull-toc -mminimal-toc -mno-fp-in-toc -mno-sum-in-toc -m64 -m32 -mxl-call -mno-xl-call -mpe -msoft-float -mhard-float -mmultiple -mno-multiple -mstring -mno-string -mupdate -mno-update -mfused-madd -mno-fused-madd -mbit-align -mno-bit-align -mstrict-align -mno-strict-align -mrelocatable -mno-relocatable -mrelocatable-lib -mno-relocatable-lib -mtoc -mno-toc -mlittle -mlittle-endian -mbig -mbig-endian -mcall-aix -mcall-sysv -mcall-netbsd -maix-struct-return -msvr4-struct-return -mabi=altivec -mabi=no-altivec -mprototype -mno-prototype -msim -mmvme -mads -myellowknife -memb -msdata -msdata=</code><i>opt</i> <code>-mvxworks -G</code> <i>num</i> <code>-pthread</code> </p>
<p> <i></i><font SIZE="-1"><i>RT</i></font><i> Options</i> </p>
<p> <code>-mcall-lib-mul -mfp-arg-in-fpregs -mfp-arg-in-gregs -mfull-fp-blocks -mhc-struct-return -min-line-mul -mminimum-fp-blocks -mnohc-struct-return</code> </p>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i> </p>
<p> <code>-mabicalls -march=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu=type</i> <code>-mcpu=</code><i>cpu-type</i> <code>-membedded-data -muninit-const-in-rodata -membedded-pic -mfp32 -mfp64 -mfused-madd -mno-fused-madd -mgas -mgp32 -mgp64 -mgpopt -mhalf-pic -mhard-float -mint64 -mips1 -mips2 -mips3 -mips4 -mlong64 -mlong32 -mlong-calls -mmemcpy -mmips-as -mmips-tfile -mno-abicalls -mno-embedded-data -mno-uninit-const-in-rodata -mno-embedded-pic -mno-gpopt -mno-long-calls -mno-memcpy -mno-mips-tfile -mno-rnames -mno-stats -mrnames -msoft-float -m4650 -msingle-float -mmad -mstats -EL -EB -G</code> <i>num</i> <code>-nocpp -mabi=32 -mabi=n32 -mabi=64 -mabi=eabi -mfix7000 -mno-crt0 -mflush-func=</code><i>func</i> <code>-mno-flush-func</code> </p>
<p> <i>i386 and x86-64 Options</i> </p>
<p> <code>-mcpu=</code><i>cpu-type</i> <code>-march=</code><i>cpu-type</i> <code>-mfpmath=</code><i>unit</i> <code>-masm=</code><i>dialect</i> <code>-mno-fancy-math-387 -mno-fp-ret-in-387 -msoft-float -msvr3-shlib -mno-wide-multiply -mrtd -malign-double -mpreferred-stack-boundary=</code><i>num</i> <code>-mmmx -msse -msse2 -m3dnow -mthreads -mno-align-stringops -minline-all-stringops -mpush-args -maccumulate-outgoing-args -m128bit-long-double -m96bit-long-double -mregparm=</code><i>num</i> <code>-momit-leaf-frame-pointer -mno-red-zone -mcmodel=</code><i>code-model</i> <code>-m32 -m64</code> </p>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i> </p>
<p> <code>-march=</code><i>architecture-type</i> <code>-mbig-switch -mdisable-fpregs -mdisable-indexing -mfast-indirect-calls -mgas -mjump-in-delay -mlong-load-store -mno-big-switch -mno-disable-fpregs -mno-disable-indexing -mno-fast-indirect-calls -mno-gas -mno-jump-in-delay -mno-long-load-store -mno-portable-runtime -mno-soft-float -mno-space-regs -msoft-float -mpa-risc-1-0 -mpa-risc-1-1 -mpa-risc-2-0 -mportable-runtime -mschedule=</code><i>cpu-type</i> <code>-mspace-regs</code> </p>
<p> <i>Intel 960 Options</i> </p>
<p> <code>-m</code><i>cpu-type</i> <code>-masm-compat -mclean-linkage -mcode-align -mcomplex-addr -mleaf-procedures -mic-compat -mic2.0-compat -mic3.0-compat -mintel-asm -mno-clean-linkage -mno-code-align -mno-complex-addr -mno-leaf-procedures -mno-old-align -mno-strict-align -mno-tail-call -mnumerics -mold-align -msoft-float -mstrict-align -mtail-call</code> </p>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha Options</i> </p>
<p> <code>-mno-fp-regs -msoft-float -malpha-as -mgas -mieee -mieee-with-inexact -mieee-conformant -mfp-trap-mode=</code><i>mode</i> <code>-mfp-rounding-mode=</code><i>mode</i> <code>-mtrap-precision=</code><i>mode</i> <code>-mbuild-constants -mcpu=</code><i>cpu-type</i> <code>-mtune=</code><i>cpu-type</i> <code>-mbwx -mmax -mfix -mcix -mfloat-vax -mfloat-ieee -mexplicit-relocs -msmall-data -mlarge-data -mmemory-latency=</code><i>time</i> </p>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha/VMS Options</i> </p>
<p> <code>-mvms-return-codes</code> </p>
<p> <i>Clipper Options</i> </p>
<p> <code>-mc300 -mc400</code> </p>
<p> <i>H8/300 Options</i> </p>
<p> <code>-mrelax -mh -ms -mint32 -malign-300</code> </p>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i> </p>
<p> <code>-m1 -m2 -m3 -m3e -m4-nofpu -m4-single-only -m4-single -m4 -m5-64media -m5-64media-nofpu -m5-32media -m5-32media-nofpu -m5-compact -m5-compact-nofpu -mb -ml -mdalign -mrelax -mbigtable -mfmovd -mhitachi -mnomacsave -mieee -misize -mpadstruct -mspace -mprefergot -musermode</code> </p>
<p> <i>System V Options</i> </p>
<p> <code>-Qy -Qn -YP,</code><i>paths</i> <code>-Ym,</code><i>dir</i> </p>
<p> <i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i> </p>
<p> <code>-EB -EL -mmangle-cpu -mcpu=</code><i>cpu</i> <code>-mtext=</code><i>text-section</i> <code>-mdata=</code><i>data-section</i> <code>-mrodata=</code><i>readonly-data-section</i> </p>
<p> <i>TMS320C3x/C4x Options</i> </p>
<p> <code>-mcpu=</code><i>cpu</i> <code>-mbig -msmall -mregparm -mmemparm -mfast-fix -mmpyi -mbk -mti -mdp-isr-reload -mrpts=</code><i>count</i> <code>-mrptb -mdb -mloop-unsigned -mparallel-insns -mparallel-mpy -mpreserve-float</code> </p>
<p> <i>V850 Options</i> </p>
<p> <code>-mlong-calls -mno-long-calls -mep -mno-ep -mprolog-function -mno-prolog-function -mspace -mtda=</code><i>n</i> <code>-msda=</code><i>n</i> <code>-mzda=</code><i>n</i> <code>-mv850 -mbig-switch</code> </p>
<p> <i></i><font SIZE="-1"><i>NS32K</i></font><i> Options</i> </p>
<p> <code>-m32032 -m32332 -m32532 -m32081 -m32381 -mmult-add -mnomult-add -msoft-float -mrtd -mnortd -mregparam -mnoregparam -msb -mnosb -mbitfield -mnobitfield -mhimem -mnohimem</code> </p>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i> </p>
<p> <code>-mmcu=</code><i>mcu</i> <code>-msize -minit-stack=</code><i>n</i> <code>-mno-interrupts -mcall-prologues -mno-tablejump -mtiny-stack</code> </p>
<p> <i>MCore Options</i> </p>
<p> <code>-mhardlit -mno-hardlit -mdiv -mno-div -mrelax-immediates -mno-relax-immediates -mwide-bitfields -mno-wide-bitfields -m4byte-functions -mno-4byte-functions -mcallgraph-data -mno-callgraph-data -mslow-bytes -mno-slow-bytes -mno-lsim -mlittle-endian -mbig-endian -m210 -m340 -mstack-increment</code> </p>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i> </p>
<p> <code>-mlibfuncs -mno-libfuncs -mepsilon -mno-epsilon -mabi=gnu -mabi=mmixware -mzero-extend -mknuthdiv -mtoplevel-symbols -melf -mbranch-predict -mno-branch-predict -mbase-addresses -mno-base-addresses</code> </p>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i> </p>
<p> <code>-mbig-endian -mlittle-endian -mgnu-as -mgnu-ld -mno-pic -mvolatile-asm-stop -mb-step -mregister-names -mno-sdata -mconstant-gp -mauto-pic -minline-divide-min-latency -minline-divide-max-throughput -mno-dwarf2-asm -mfixed-range=</code><i>register-range</i> </p>
<p> <i>D30V Options</i> </p>
<p> <code>-mextmem -mextmemory -monchip -mno-asm-optimize -masm-optimize -mbranch-cost=</code><i>n</i> <code>-mcond-exec=</code><i>n</i> </p>
<p> <i>S/390 and zSeries Options</i> </p>
<p> <code>-mhard-float -msoft-float -mbackchain -mno-backchain -msmall-exec -mno-small-exec -mmvcle -mno-mvcle -m64 -m31 -mdebug -mno-debug</code> </p>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i> </p>
<p> <code>-mcpu=</code><i>cpu</i> <code>-march=</code><i>cpu</i> <code>-mtune=</code><i>cpu</i> <code>-mmax-stack-frame=</code><i>n</i> <code>-melinux-stacksize=</code><i>n</i> <code>-metrax4 -metrax100 -mpdebug -mcc-init -mno-side-effects -mstack-align -mdata-align -mconst-align -m32-bit -m16-bit -m8-bit -mno-prologue-epilogue -mno-gotplt -melf -maout -melinux -mlinux -sim -sim2</code> </p>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i> </p>
<p> <code>-mfpu -msoft-float -mac0 -mno-ac0 -m40 -m45 -m10 -mbcopy -mbcopy-builtin -mint32 -mno-int16 -mint16 -mno-int32 -mfloat32 -mno-float64 -mfloat64 -mno-float32 -mabshi -mno-abshi -mbranch-expensive -mbranch-cheap -msplit -mno-split -munix-asm -mdec-asm</code> </p>
<p> <i>Xstormy16 Options</i> </p>
<p> <code>-msim</code> </p>
<p> <i>Xtensa Options</i> </p>
<p> <code>-mbig-endian -mlittle-endian -mdensity -mno-density -mmac16 -mno-mac16 -mmul16 -mno-mul16 -mmul32 -mno-mul32 -mnsa -mno-nsa -mminmax -mno-minmax -msext -mno-sext -mbooleans -mno-booleans -mhard-float -msoft-float -mfused-madd -mno-fused-madd -mserialize-volatile -mno-serialize-volatile -mtext-section-literals -mno-text-section-literals -mtarget-align -mno-target-align -mlongcalls -mno-longcalls</code> </p>
<dt><i>Code Generation Options</i></p>
<dd> <code>-fcall-saved-</code><i>reg</i> <code>-fcall-used-</code><i>reg</i> <code>-ffixed-</code><i>reg</i> <code>-fexceptions -fnon-call-exceptions -funwind-tables -fasynchronous-unwind-tables -finhibit-size-directive -finstrument-functions -fno-common -fno-ident -fno-gnu-linker -fpcc-struct-return -fpic -fPIC -freg-struct-return -fshared-data -fshort-enums -fshort-double -fshort-wchar -fvolatile -fvolatile-global -fvolatile-static -fverbose-asm -fpack-struct -fstack-check -fstack-limit-register=</code><i>reg</i> <code>-fstack-limit-symbol=</code><i>sym</i> <code>-fargument-alias -fargument-noalias -fargument-noalias-global -fleading-underscore</code></dl>
<h2>Options Controlling the Kind of Output</h2>
<p> Compilation can involve up to four stages: preprocessing, compilation proper, assembly and linking, always in that order. The first three stages apply to an individual source file, and end by producing an object file; linking combines all the object files (those newly compiled, and those specified as input) into an executable file. </p>
<p> For any given input file, the file name suffix determines what kind of compilation is done: </p>
<dl>
<dt><i>file</i><code>.c</code></p>
<dd> C source code which must be preprocessed. </p>
<dt><i>file</i><code>.i</code></p>
<dd> C source code which should not be preprocessed. </p>
<dt><i>file</i><code>.ii</code></p>
<dd> C<font SIZE="-2">++</font> source code which should not be preprocessed. </p>
<dt><i>file</i><code>.m</code></p>
<dd> Objective-C source code. Note that you must link with the library <i>libobjc.a</i> to make an Objective-C program work. </p>
<dt><i>file</i><code>.mi</code></p>
<dd> Objective-C source code which should not be preprocessed. </p>
<dt><i>file</i><code>.h</code></p>
<dd> C header file (not to be compiled or linked). </p>
<dt><i>file</i><code>.cc</code></p>
<dd>
<dt><i>file</i><code>.cp</code></p>
<dd>
<dt><i>file</i><code>.cxx</code></p>
<dd>
<dt><i>file</i><code>.cpp</code></p>
<dd>
<dt><i>file</i><code>.c++</code></p>
<dd>
<dt><i>file</i><code>.C</code></p>
<dd> C<font SIZE="-2">++</font> source code which must be preprocessed. Note that in <code>.cxx</code>, the last two letters must both be literally <code>x</code>. Likewise, <code>.C</code> refers to a literal capital C. </p>
<dt><i>file</i><code>.f</code></p>
<dd>
<dt><i>file</i><code>.for</code></p>
<dd>
<dt><i>file</i><code>.FOR</code></p>
<dd> Fortran source code which should not be preprocessed. </p>
<dt><i>file</i><code>.F</code></p>
<dd>
<dt><i>file</i><code>.fpp</code></p>
<dd>
<dt><i>file</i><code>.FPP</code></p>
<dd> Fortran source code which must be preprocessed (with the traditional preprocessor). </p>
<dt><i>file</i><code>.r</code></p>
<dd> Fortran source code which must be preprocessed with a <font SIZE="-1">RATFOR</font> preprocessor (not included with <font SIZE="-1">GCC</font>). </p>
<dt><i>file</i><code>.ads</code></p>
<dd> Ada source code file which contains a library unit declaration (a declaration of a package, subprogram, or generic, or a generic instantiation), or a library unit renaming declaration (a package, generic, or subprogram renaming declaration). Such files are also called <i>specs</i>. </p>
<dt><i>file</i><code>.adb</code></p>
<dd> Ada source code file containing a library unit body (a subprogram or package body). Such files are also called <i>bodies</i>. </p>
<dt><i>file</i><code>.s</code></p>
<dd> Assembler code. </p>
<dt><i>file</i><code>.S</code></p>
<dd> Assembler code which must be preprocessed. </p>
<dt><i>other</i></p>
<dd> An object file to be fed straight into linking. Any file name with no recognized suffix is treated this way.</dl>
<p> You can specify the input language explicitly with the <code>-x</code> option: </p>
<dl>
<dt><code>-x</code> <i>language</i></p>
<dd> Specify explicitly the <i>language</i> for the following input files (rather than letting the compiler choose a default based on the file name suffix). This option applies to all following input files until the next <code>-x</code> option. Possible values for <i>language</i> are: </p>
<pre>
        c  c-header  cpp-output
        c++  c++-cpp-output
        objective-c  objc-cpp-output
        assembler  assembler-with-cpp
        ada
        f77  f77-cpp-input  ratfor
        java
</pre>
<dt><code>-x none</code></p>
<dd> Turn off any specification of a language, so that subsequent files are handled according to their file name suffixes (as they are if <code>-x</code> has not been used at all). </p>
<dt><code>-pass-exit-codes</code></p>
<dd> Normally the <code>gcc</code> program will exit with the code of 1 if any phase of the compiler returns a non-success return code. If you specify <code>-pass-exit-codes</code>, the <code>gcc</code> program will instead return with numerically highest error produced by any phase that returned an error indication.</dl>
<p> If you only want some of the stages of compilation, you can use <code>-x</code> (or filename suffixes) to tell <code>gcc</code> where to start, and one of the options <code>-c</code>, <code>-S</code>, or <code>-E</code> to say where <code>gcc</code> is to stop. Note that some combinations (for example, <code>-x cpp-output -E</code>) instruct <code>gcc</code> to do nothing at all. </p>
<dl>
<dt><code>-c</code></p>
<dd> Compile or assemble the source files, but do not link. The linking stage simply is not done. The ultimate output is in the form of an object file for each source file. </p>
<p> By default, the object file name for a source file is made by replacing the suffix <code>.c</code>, <code>.i</code>, <code>.s</code>, etc., with <code>.o</code>. </p>
<p> Unrecognized input files, not requiring compilation or assembly, are ignored. </p>
<dt><code>-S</code></p>
<dd> Stop after the stage of compilation proper; do not assemble. The output is in the form of an assembler code file for each non-assembler input file specified. </p>
<p> By default, the assembler file name for a source file is made by replacing the suffix <code>.c</code>, <code>.i</code>, etc., with <code>.s</code>. </p>
<p> Input files that don&#8217;t require compilation are ignored. </p>
<dt><code>-E</code></p>
<dd> Stop after the preprocessing stage; do not run the compiler proper. The output is in the form of preprocessed source code, which is sent to the standard output. </p>
<p> Input files which don&#8217;t require preprocessing are ignored. </p>
<dt><code>-o</code> <i>file</i></p>
<dd> Place output in file <i>file</i>. This applies regardless to whatever sort of output is being produced, whether it be an executable file, an object file, an assembler file or preprocessed C code. </p>
<p> Since only one output file can be specified, it does not make sense to use <code>-o</code> when compiling more than one input file, unless you are producing an executable file as output. </p>
<p> If <code>-o</code> is not specified, the default is to put an executable file in <i>a.out</i>, the object file for <i>source.suffix</i> in <i>source.o</i>, its assembler file in <i>source.s</i>, and all preprocessed C source on standard output. </p>
<dt><code>-v</code></p>
<dd> Print (on standard error output) the commands executed to run the stages of compilation. Also print the version number of the compiler driver program and of the preprocessor and the compiler proper. </p>
<dt><code>-###</code></p>
<dd> Like <code>-v</code> except the commands are not executed and all command arguments are quoted. This is useful for shell scripts to capture the driver-generated command lines. </p>
<dt><code>-pipe</code></p>
<dd> Use pipes rather than temporary files for communication between the various stages of compilation. This fails to work on some systems where the assembler is unable to read from a pipe; but the <font SIZE="-1">GNU</font> assembler has no trouble. </p>
<dt><code>&#8212;help</code></p>
<dd> Print (on the standard output) a description of the command line options understood by <code>gcc</code>. If the <code>-v</code> option is also specified then <code>&#8212;help</code> will also be passed on to the various processes invoked by <code>gcc</code>, so that they can display the command line options they accept. If the <code>-W</code> option is also specified then command line options which have no documentation associated with them will also be displayed. </p>
<dt><code>&#8212;target-help</code></p>
<dd> Print (on the standard output) a description of target specific command line options for each tool. </p>
<dt><code>&#8212;version</code></p>
<dd> Display the version number and copyrights of the invoked <font SIZE="-1">GCC</font>.</dl>
<h2>Compiling C<font SIZE="-2">++</font> Programs</h2>
<p> C<font SIZE="-2">++</font> source files conventionally use one of the suffixes <code>.C</code>, <code>.cc</code>, <code>.cpp</code>, <code>.c++</code>, <code>.cp</code>, or <code>.cxx</code>; preprocessed C<font SIZE="-2">++</font> files use the suffix <code>.ii</code>. <font SIZE="-1">GCC</font> recognizes files with these names and compiles them as C<font SIZE="-2">++</font> programs even if you call the compiler the same way as for compiling C programs (usually with the name <code>gcc</code>). </p>
<p> However, C<font SIZE="-2">++</font> programs often require class libraries as well as a compiler that understands the C<font SIZE="-2">++</font> language&#8212;and under some circumstances, you might want to compile programs from standard input, or otherwise without a suffix that flags them as C<font SIZE="-2">++</font> programs. <code>g++</code> is a program that calls <font SIZE="-1">GCC</font> with the default language set to C<font SIZE="-2">++</font>, and automatically specifies linking against the C<font SIZE="-2">++</font> library. On many systems, <code>g++</code> is also installed with the name <code>c++</code>. </p>
<p> When you compile C<font SIZE="-2">++</font> programs, you may specify many of the same command-line options that you use for compiling programs in any language; or command-line options meaningful for C and related languages; or options that are meaningful only for C<font SIZE="-2">++</font> programs.</p>
<h2>Options Controlling C Dialect</h2>
<p> The following options control the dialect of C (or languages derived from C, such as C<font SIZE="-2">++</font> and Objective-C) that the compiler accepts: </p>
<dl>
<dt><code>-ansi</code></p>
<dd> In C mode, support all <font SIZE="-1">ISO</font> C89 programs. In C<font SIZE="-2">++</font> mode, remove <font SIZE="-1">GNU</font> extensions that conflict with <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>. </p>
<p> This turns off certain features of <font SIZE="-1">GCC</font> that are incompatible with <font SIZE="-1">ISO</font> C89 (when compiling C code), or of standard C<font SIZE="-2">++</font> (when compiling C<font SIZE="-2">++</font> code), such as the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, and predefined macros such as <tt>&quot;unix&quot;</tt> and <tt>&quot;vax&quot;</tt> that identify the type of system you are using. It also enables the undesirable and rarely used <font SIZE="-1">ISO</font> trigraph feature. For the C compiler, it disables recognition of C<font SIZE="-2">++</font> style <code>//</code> comments as well as the <tt>&quot;inline&quot;</tt> keyword. </p>
<p> The alternate keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__extension__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> continue to work despite <code>-ansi</code>. You would not want to use them in an <font SIZE="-1">ISO</font> C program, of course, but it is useful to put them in header files that might be included in compilations done with <code>-ansi</code>. Alternate predefined macros such as <tt>&quot;__unix__&quot;</tt> and <tt>&quot;__vax__&quot;</tt> are also available, with or without <code>-ansi</code>. </p>
<p> The <code>-ansi</code> option does not cause non-ISO programs to be rejected gratuitously. For that, <code>-pedantic</code> is required in addition to <code>-ansi</code>. </p>
<p> The macro <tt>&quot;__STRICT_ANSI__&quot;</tt> is predefined when the <code>-ansi</code> option is used. Some header files may notice this macro and refrain from declaring certain functions or defining certain macros that the <font SIZE="-1">ISO</font> standard doesn&#8217;t call for; this is to avoid interfering with any programs that might use these names for other things. </p>
<p> Functions which would normally be built in but do not have semantics defined by <font SIZE="-1">ISO</font> C (such as <tt>&quot;alloca&quot;</tt> and <tt>&quot;ffs&quot;</tt>) are not built-in functions with <code>-ansi</code> is used. </p>
<dt><code>-std=</code></p>
<dd> Determine the language standard. This option is currently only supported when compiling C. A value for this option must be provided; possible values are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c89</code></p>
<dd>
<dt><code>iso9899:1990</code></p>
<dd> <font SIZE="-1">ISO</font> C89 (same as <code>-ansi</code>). </p>
<dt><code>iso9899:199409</code></p>
<dd> <font SIZE="-1">ISO</font> C89 as modified in amendment 1. </p>
<dt><code>c99</code></p>
<dd>
<dt><code>c9x</code></p>
<dd>
<dt><code>iso9899:1999</code></p>
<dd>
<dt><code>iso9899:199x</code></p>
<dd> <font SIZE="-1">ISO</font> C99. Note that this standard is not yet fully supported; see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/gcc-3.1/c99status.html">http://gcc.gnu.org/gcc-3.1/c99status.html</a></code>&gt; for more information. The names <code>c9x</code> and <code>iso9899:199x</code> are deprecated. </p>
<dt><code>gnu89</code></p>
<dd> Default, <font SIZE="-1">ISO</font> C89 plus <font SIZE="-1">GNU</font> extensions (including some C99 features). </p>
<dt><code>gnu99</code></p>
<dd>
<dt><code>gnu9x</code></p>
<dd> <font SIZE="-1">ISO</font> C99 plus <font SIZE="-1">GNU</font> extensions. When <font SIZE="-1">ISO</font> C99 is fully implemented in <font SIZE="-1">GCC</font>, this will become the default. The name <code>gnu9x</code> is deprecated.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Even when this option is not specified, you can still use some of the features of newer standards in so far as they do not conflict with previous C standards. For example, you may use <tt>&quot;__restrict__&quot;</tt> even when <code>-std=c99</code> is not specified. </p>
<p> The <code>-std</code> options specifying some version of <font SIZE="-1">ISO</font> C have the same effects as <code>-ansi</code>, except that features that were not in <font SIZE="-1">ISO</font> C89 but are in the specified version (for example, <code>//</code> comments and the <tt>&quot;inline&quot;</tt> keyword in <font SIZE="-1">ISO</font> C99) are not disabled.</dl>
<dt><code>-aux-info</code> <i>filename</i></p>
<dd> Output to the given filename prototyped declarations for all functions declared and/or defined in a translation unit, including those in header files. This option is silently ignored in any language other than C. </p>
<p> Besides declarations, the file indicates, in comments, the origin of each declaration (source file and line), whether the declaration was implicit, prototyped or unprototyped (<code>I</code>, <code>N</code> for new or <code>O</code> for old, respectively, in the first character after the line number and the colon), and whether it came from a declaration or a definition (<code>C</code> or <code>F</code>, respectively, in the following character). In the case of function definitions, a K&amp;R-style list of arguments followed by their declarations is also provided, inside comments, after the declaration. </p>
<dt><code>-fno-asm</code></p>
<dd> Do not recognize <tt>&quot;asm&quot;</tt>, <tt>&quot;inline&quot;</tt> or <tt>&quot;typeof&quot;</tt> as a keyword, so that code can use these words as identifiers. You can use the keywords <tt>&quot;__asm__&quot;</tt>, <tt>&quot;__inline__&quot;</tt> and <tt>&quot;__typeof__&quot;</tt> instead. <code>-ansi</code> implies <code>-fno-asm</code>. </p>
<p> In C<font SIZE="-2">++</font>, this switch only affects the <tt>&quot;typeof&quot;</tt> keyword, since <tt>&quot;asm&quot;</tt> and <tt>&quot;inline&quot;</tt> are standard keywords. You may want to use the <code>-fno-gnu-keywords</code> flag instead, which has the same effect. In C99 mode (<code>-std=c99</code> or <code>-std=gnu99</code>), this switch only affects the <tt>&quot;asm&quot;</tt> and <tt>&quot;typeof&quot;</tt> keywords, since <tt>&quot;inline&quot;</tt> is a standard keyword in <font SIZE="-1">ISO</font> C99. </p>
<dt><code>-fno-builtin</code></p>
<dd>
<dt><code>-fno-builtin-</code><i>function</i>(C and Objective-C only)</p>
<dd> Don&#8217;t recognize built-in functions that do not begin with <code>__builtin_</code> as prefix. </p>
<p> <font SIZE="-1">GCC</font> normally generates special code to handle certain built-in functions more efficiently; for instance, calls to <tt>&quot;alloca&quot;</tt> may become single instructions that adjust the stack directly, and calls to <tt>&quot;memcpy&quot;</tt> may become inline copy loops. The resulting code is often both smaller and faster, but since the function calls no longer appear as such, you cannot set a breakpoint on those calls, nor can you change the behavior of the functions by linking with a different library. </p>
<p> In C<font SIZE="-2">++</font>, <code>-fno-builtin</code> is always in effect. The <code>-fbuiltin</code> option has no effect. Therefore, in C<font SIZE="-2">++</font>, the only way to get the optimization benefits of built-in functions is to call the function using the <code>__builtin_</code> prefix. The <font SIZE="-1">GNU</font> C<font SIZE="-2">++</font> Standard Library uses built-in functions to implement many functions (like <tt>&quot;std::strchr&quot;</tt>), so that you automatically get efficient code. </p>
<p> With the <code>-fno-builtin-</code><i>function</i> option, not available when compiling C<font SIZE="-2">++</font>, only the built-in function <i>function</i> is disabled. <i>function</i> must not begin with <code>__builtin_</code>. If a function is named this is not built-in in this version of <font SIZE="-1">GCC</font>, this option is ignored. There is no corresponding <code>-fbuiltin-</code><i>function</i> option; if you wish to enable built-in functions selectively when using <code>-fno-builtin</code> or <code>-ffreestanding</code>, you may define macros such as: </p>
<pre><code>
#define abs(n) __builtin_abs((n))
#define strcpy(d, s) __builtin_strcpy((d), (s))
</code></pre>
<dt><code>-fhosted</code></p>
<dd> Assert that compilation takes place in a hosted environment. This implies <code>-fbuiltin</code>. A hosted environment is one in which the entire standard library is available, and in which <tt>&quot;main&quot;</tt> has a return type of <tt>&quot;int&quot;</tt>. Examples are nearly everything except a kernel. This is equivalent to <code>-fno-freestanding</code>. </p>
<dt><code>-ffreestanding</code></p>
<dd> Assert that compilation takes place in a freestanding environment. This implies <code>-fno-builtin</code>. A freestanding environment is one in which the standard library may not exist, and program startup may not necessarily be at <tt>&quot;main&quot;</tt>. The most obvious example is an <font SIZE="-1">OS</font> kernel. This is equivalent to <code>-fno-hosted</code>. </p>
<dt><code>-trigraphs</code></p>
<dd> Support <font SIZE="-1">ISO</font> C trigraphs. The <code>-ansi</code> option (and <code>-std</code> options for strict <font SIZE="-1">ISO</font> C conformance) implies <code>-trigraphs</code>. </p>
<dt><code>-no-integrated-cpp</code></p>
<dd> Invoke the external cpp during compilation. The default is to use the integrated cpp (internal cpp). This option also allows a user-supplied cpp via the <code>-B</code> option. This flag is applicable in both C and C<font SIZE="-2">++</font> modes. </p>
<p> We do not guarantee to retain this option in future, and we may change its semantics. </p>
<dt><code>-traditional</code></p>
<dd> Attempt to support some aspects of traditional C compilers. Specifically:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> All <tt>&quot;extern&quot;</tt> declarations take effect globally even if they are written inside of a function definition. This includes implicit declarations of functions. </p>
<dt>*</p>
<dd> The newer keywords <tt>&quot;typeof&quot;</tt>, <tt>&quot;inline&quot;</tt>, <tt>&quot;signed&quot;</tt>, <tt>&quot;const&quot;</tt> and <tt>&quot;volatile&quot;</tt> are not recognized. (You can still use the alternative keywords such as <tt>&quot;__typeof__&quot;</tt>, <tt>&quot;__inline__&quot;</tt>, and so on.) </p>
<dt>*</p>
<dd> Comparisons between pointers and integers are always allowed. </p>
<dt>*</p>
<dd> Integer types <tt>&quot;unsigned short&quot;</tt> and <tt>&quot;unsigned char&quot;</tt> promote to <tt>&quot;unsigned int&quot;</tt>. </p>
<dt>*</p>
<dd> Out-of-range floating point literals are not an error. </p>
<dt>*</p>
<dd> Certain constructs which <font SIZE="-1">ISO</font> regards as a single invalid preprocessing number, such as <code>0xe-0xd</code>, are treated as expressions instead. </p>
<dt>*</p>
<dd> String &#8220;constants&#8221; are not necessarily constant; they are stored in writable space, and identical looking constants are allocated separately. (This is the same as the effect of <code>-fwritable-strings</code>.) </p>
<dt>*</p>
<dd> All automatic variables not declared <tt>&quot;register&quot;</tt> are preserved by <tt>&quot;longjmp&quot;</tt>. Ordinarily, <font SIZE="-1">GNU</font> C follows <font SIZE="-1">ISO</font> C: automatic variables not declared <tt>&quot;volatile&quot;</tt> may be clobbered. </p>
<dt>*</p>
<dd> The character escape sequences <code>
