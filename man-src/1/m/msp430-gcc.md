---
title: "msp430-gcc(1)"
name: "msp430-gcc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-gcc/"
description: "gcc – GNU project C and C++ compiler"
---
<h2 class="name">NAME</h2>
<p> gcc - <font SIZE="-1">GNU</font> project C and C<font SIZE="-2">++</font> compiler </p>
<h2>SYNOPSIS</h2>
<p> gcc [<code>-c</code>|<code>-S</code>|<code>-E</code>] [<code>-std=</code><i>standard</i>] <br />
&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>] <br />
&nbsp;<wbr>[<code>-W</code><i>warn</i>...]&nbsp;<wbr>[<code>-pedantic</code>] <br />
&nbsp;<wbr>[<code>-I</code><i>dir</i>...]&nbsp;<wbr>[<code>-L</code><i>dir</i>...] <br />
&nbsp;<wbr>[<code>-D</code><i>macro</i>[=<i>defn</i>]...]&nbsp;<wbr>[<code>-U</code><i>macro</i>] <br />
&nbsp;<wbr>[<code>-f</code><i>option</i>...]&nbsp;<wbr>[<code>-m</code><i>machine-option</i>...] <br />
&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr><i>infile</i>... </p>
<p> Only the most useful options are listed here; see below for the remainder. <code>g++</code> accepts mostly the same options as <code>gcc</code>.  </p>
<h2>DESCRIPTION</h2>
<p> When you invoke <font SIZE="-1">GCC</font>, it normally does preprocessing, compilation, assembly and linking. The ``overall options&#8217;&#8216; allow you to stop this process at an intermediate stage. For example, the <code>-c</code> option says not to run the linker. Then the output consists of object files output by the assembler. </p>
<p> Other options are passed on to one stage of processing. Some options control the preprocessor and others the compiler itself. Yet other options control the assembler and linker; most of these are not documented here, since you rarely need to use any of them. </p>
<p> Most of the command line options that you can use with <font SIZE="-1">GCC</font> are useful for C programs; when an option is only useful with another language (usually C<font SIZE="-2">++</font>), the explanation says so explicitly. If the description for a particular option does not mention a source language, you can use that option with all supported languages. </p>
<p> The <code>gcc</code> program accepts options and file names as operands. Many options have multi-letter names; therefore multiple single-letter options may <i>not</i> be grouped: <code>-dr</code> is very different from <code>-d -r</code>. </p>
<p> You can mix options and other arguments. For the most part, the order you use doesn&#8217;t matter. Order does matter when you use several options of the same kind; for example, if you specify <code>-L</code> more than once, the directories are searched in the order specified. </p>
<p> Many options have long names starting with <code>-f</code> or with <code>-W</code>---for example, <code>-fforce-mem</code>, <code>-fstrength-reduce</code>, <code>-Wformat</code> and so on. Most of these have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.  </p>
<h2>OPTIONS</h2>
<h2>Option Summary</h2>
<p> Here is a summary of all the options, grouped by type. Explanations are in the following sections. <br />
 </p>
<dl>
<dt><i>Overall Options</i></dt>
<dd> <p> <code>-c -S -E -o</code> <i>file</i> <code>-pipe -pass-exit-codes -x</code> <i>language</i> <code>-v -### --help --target-help --version</code> <br />
 </p>
 </dd>
<dt><i>C Language Options</i></dt>
<dd> <p> <code>-ansi -std=</code><i>standard</i> <code>-aux-info</code> <i>filename</i> <code>-fno-asm -fno-builtin -fno-builtin-</code><i>function</i> <code>-fhosted -ffreestanding -trigraphs -no-integrated-cpp -traditional -traditional-cpp -fallow-single-precision -fcond-mismatch -fsigned-bitfields -fsigned-char -funsigned-bitfields -funsigned-char -fwritable-strings</code> <br />
 </p>
 </dd>
<dt><i>C<font SIZE="-2">++</font> Language Options</i></dt>
<dd> <p> <code>-fno-access-control -fcheck-new -fconserve-space -fno-const-strings -fdollars-in-identifiers -fno-elide-constructors -fno-enforce-eh-specs -fexternal-templates -falt-external-templates -ffor-scope -fno-for-scope -fno-gnu-keywords -fno-implicit-templates -fno-implicit-inline-templates -fno-implement-inlines -fms-extensions -fno-nonansi-builtins -fno-operator-names -fno-optional-diags -fpermissive -frepo -fno-rtti -fstats -ftemplate-depth-</code><i>n</i> <code>-fuse-cxa-atexit -fvtable-gc -fno-weak -nostdinc++ -fno-default-inline -Wabi -Wctor-dtor-privacy -Wnon-virtual-dtor -Wreorder -Weffc++ -Wno-deprecated -Wno-non-template-friend -Wold-style-cast -Woverloaded-virtual -Wno-pmf-conversions -Wsign-promo -Wsynth</code> <br />
 </p>
 </dd>
<dt><i>Objective-C Language Options</i></dt>
<dd> <p> <code>-fconstant-string-class=</code><i>class-name</i> <code>-fgnu-runtime -fnext-runtime -gen-decls -Wno-protocol -Wselector</code> <br />
 </p>
 </dd>
<dt><i>Language Independent Options</i></dt>
<dd> <p> <code>-fmessage-length=</code><i>n</i> <code>-fdiagnostics-show-location=</code>[<code>once</code>|<code>every-line</code>] <br />
 </p>
 </dd>
<dt><i>Warning Options</i></dt>
<dd> <p> <code>-fsyntax-only -pedantic -pedantic-errors -w -W -Wall -Waggregate-return -Wcast-align -Wcast-qual -Wchar-subscripts -Wcomment -Wconversion -Wno-deprecated-declarations -Wdisabled-optimization -Wdiv-by-zero -Werror -Wfloat-equal -Wformat -Wformat=2 -Wformat-nonliteral -Wformat-security -Wimplicit -Wimplicit-int -Wimplicit-function-declaration -Werror-implicit-function-declaration -Wimport -Winline -Wlarger-than-</code><i>len</i> <code>-Wlong-long -Wmain -Wmissing-braces -Wmissing-format-attribute -Wmissing-noreturn -Wmultichar -Wno-format-extra-args -Wno-format-y2k -Wno-import -Wpacked -Wpadded -Wparentheses -Wpointer-arith -Wredundant-decls -Wreturn-type -Wsequence-point -Wshadow -Wsign-compare -Wswitch -Wsystem-headers -Wtrigraphs -Wundef -Wuninitialized -Wunknown-pragmas -Wunreachable-code -Wunused -Wunused-function -Wunused-label -Wunused-parameter -Wunused-value -Wunused-variable -Wwrite-strings</code> <br />
 </p>
 </dd>
<dt><i>C-only Warning Options</i></dt>
<dd> <p> <code>-Wbad-function-cast -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Wstrict-prototypes -Wtraditional</code> <br />
 </p>
 </dd>
<dt><i>Debugging Options</i></dt>
<dd> <p> <code>-d</code><i>letters</i> <code>-dumpspecs -dumpmachine -dumpversion -fdump-unnumbered -fdump-translation-unit</code>[<code>-</code><i>n</i>] <code>-fdump-class-hierarchy</code>[<code>-</code><i>n</i>] <code>-fdump-tree-original</code>[<code>-</code><i>n</i>] <code>-fdump-tree-optimized</code>[<code>-</code><i>n</i>] <code>-fdump-tree-inlined</code>[<code>-</code><i>n</i>] <code>-fmem-report -fpretend-float -fprofile-arcs -fsched-verbose=</code><i>n</i> <code>-ftest-coverage -ftime-report -g -g</code><i>level</i> <code>-gcoff -gdwarf -gdwarf-1 -gdwarf-1+ -gdwarf-2 -ggdb -gstabs -gstabs+ -gvms -gxcoff -gxcoff+ -p -pg -print-file-name=</code><i>library</i> <code>-print-libgcc-file-name -print-multi-directory -print-multi-lib -print-prog-name=</code><i>program</i> <code>-print-search-dirs -Q -save-temps -time</code> <br />
 </p>
 </dd>
<dt><i>Optimization Options</i></dt>
<dd> <p> <code>-falign-functions=</code><i>n</i> <code>-falign-jumps=</code><i>n</i> <code>-falign-labels=</code><i>n</i> <code>-falign-loops=</code><i>n</i> <code>-fbounds-check -fbranch-probabilities -fcaller-saves -fcprop-registers -fcse-follow-jumps -fcse-skip-blocks -fdata-sections -fdelayed-branch -fdelete-null-pointer-checks -fexpensive-optimizations -ffast-math -ffloat-store -fforce-addr -fforce-mem -ffunction-sections -fgcse -fgcse-lm -fgcse-sm -finline-functions -finline-limit=</code><i>n</i> <code>-fkeep-inline-functions -fkeep-static-consts -fmerge-constants -fmerge-all-constants -fmove-all-movables -fno-branch-count-reg -fno-default-inline -fno-defer-pop -fno-function-cse -fno-guess-branch-probability -fno-inline -fno-math-errno -fno-peephole -fno-peephole2 -funsafe-math-optimizations -fno-trapping-math -fomit-frame-pointer -foptimize-register-move -foptimize-sibling-calls -fprefetch-loop-arrays -freduce-all-givs -fregmove -frename-registers -frerun-cse-after-loop -frerun-loop-opt -fschedule-insns -fschedule-insns2 -fno-sched-interblock -fno-sched-spec -fsched-spec-load -fsched-spec-load-dangerous -fsingle-precision-constant -fssa -fssa-ccp -fssa-dce -fstrength-reduce -fstrict-aliasing -fthread-jumps -ftrapv -funroll-all-loops -funroll-loops --param</code> <i>name</i><code>=</code><i>value</i> <code>-O -O0 -O1 -O2 -O3 -Os</code> <br />
 </p>
 </dd>
<dt><i>Preprocessor Options</i></dt>
<dd> <p> <code>-$ -A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -dD -dI -dM -dN -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-E -H -idirafter</code> <i>dir</i> <code>-include</code> <i>file</i> <code>-imacros</code> <i>file</i> <code>-iprefix</code> <i>file</i> <code>-iwithprefix</code> <i>dir</i> <code>-iwithprefixbefore</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-M -MM -MF -MG -MP -MQ -MT -nostdinc -P -remap -trigraphs -undef -U</code><i>macro</i> <code>-Wp,</code><i>option</i> <br />
 </p>
 </dd>
<dt><i>Assembler Option</i></dt>
<dd> <p> <code>-Wa,</code><i>option</i> <br />
 </p>
 </dd>
<dt><i>Linker Options</i></dt>
<dd> <p> <i>object-file-name</i> <code>-l</code><i>library</i> <code>-nostartfiles -nodefaultlibs -nostdlib -s -static -static-libgcc -shared -shared-libgcc -symbolic -Wl,</code><i>option</i> <code>-Xlinker</code> <i>option</i> <code>-u</code> <i>symbol</i> <br />
 </p>
 </dd>
<dt><i>Directory Options</i></dt>
<dd> <p> <code>-B</code><i>prefix</i> <code>-I</code><i>dir</i> <code>-I- -L</code><i>dir</i> <code>-specs=</code><i>file</i> <br />
 </p>
 </dd>
<dt><i>Target Options</i></dt>
<dd> <p> <code>-b</code> <i>machine</i> <code>-V</code> <i>version</i> <br />
 </p>
 </dd>
<dt><i>Machine Dependent Options</i></dt>
<dd> <p> <i>M680x0 Options</i> </p>
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
<p> <code>-mbig-endian -mlittle-endian -mdensity -mno-density -mmac16 -mno-mac16 -mmul16 -mno-mul16 -mmul32 -mno-mul32 -mnsa -mno-nsa -mminmax -mno-minmax -msext -mno-sext -mbooleans -mno-booleans -mhard-float -msoft-float -mfused-madd -mno-fused-madd -mserialize-volatile -mno-serialize-volatile -mtext-section-literals -mno-text-section-literals -mtarget-align -mno-target-align -mlongcalls -mno-longcalls</code> <br />
 </p>
 </dd>
<dt><i>Code Generation Options</i></dt>
<dd> <p> <code>-fcall-saved-</code><i>reg</i> <code>-fcall-used-</code><i>reg</i> <code>-ffixed-</code><i>reg</i> <code>-fexceptions -fnon-call-exceptions -funwind-tables -fasynchronous-unwind-tables -finhibit-size-directive -finstrument-functions -fno-common -fno-ident -fno-gnu-linker -fpcc-struct-return -fpic -fPIC -freg-struct-return -fshared-data -fshort-enums -fshort-double -fshort-wchar -fvolatile -fvolatile-global -fvolatile-static -fverbose-asm -fpack-struct -fstack-check -fstack-limit-register=</code><i>reg</i> <code>-fstack-limit-symbol=</code><i>sym</i> <code>-fargument-alias -fargument-noalias -fargument-noalias-global -fleading-underscore</code> </p>
 </dd></dl>
<h2>Options Controlling the Kind of Output</h2>
<p> Compilation can involve up to four stages: preprocessing, compilation proper, assembly and linking, always in that order. The first three stages apply to an individual source file, and end by producing an object file; linking combines all the object files (those newly compiled, and those specified as input) into an executable file. </p>
<p> For any given input file, the file name suffix determines what kind of compilation is done: <br />
 </p>
<dl>
<dt><i>file</i><code>.c</code></dt>
<dd> <p> C source code which must be preprocessed. <br />
 </p>
 </dd>
<dt><i>file</i><code>.i</code></dt>
<dd> <p> C source code which should not be preprocessed. <br />
 </p>
 </dd>
<dt><i>file</i><code>.ii</code></dt>
<dd> <p> C<font SIZE="-2">++</font> source code which should not be preprocessed. <br />
 </p>
 </dd>
<dt><i>file</i><code>.m</code></dt>
<dd> <p> Objective-C source code. Note that you must link with the library <i>libobjc.a</i> to make an Objective-C program work. <br />
 </p>
 </dd>
<dt><i>file</i><code>.mi</code></dt>
<dd> <p> Objective-C source code which should not be preprocessed. <br />
 </p>
 </dd>
<dt><i>file</i><code>.h</code></dt>
<dd> <p> C header file (not to be compiled or linked). <br />
 </p>
 </dd>
<dt><i>file</i><code>.cc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.cp</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.cxx</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.cpp</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.c++</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.C</code></dt>
<dd> <p> C<font SIZE="-2">++</font> source code which must be preprocessed. Note that in <code>.cxx</code>, the last two letters must both be literally <code>x</code>. Likewise, <code>.C</code> refers to a literal capital C. <br />
 </p>
 </dd>
<dt><i>file</i><code>.f</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.for</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.FOR</code></dt>
<dd> <p> Fortran source code which should not be preprocessed. <br />
 </p>
 </dd>
<dt><i>file</i><code>.F</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.fpp</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><i>file</i><code>.FPP</code></dt>
<dd> <p> Fortran source code which must be preprocessed (with the traditional preprocessor). <br />
 </p>
 </dd>
<dt><i>file</i><code>.r</code></dt>
<dd> <p> Fortran source code which must be preprocessed with a <font SIZE="-1">RATFOR</font> preprocessor (not included with <font SIZE="-1">GCC</font>). <br />
 </p>
 </dd>
<dt><i>file</i><code>.ads</code></dt>
<dd> <p> Ada source code file which contains a library unit declaration (a declaration of a package, subprogram, or generic, or a generic instantiation), or a library unit renaming declaration (a package, generic, or subprogram renaming declaration). Such files are also called <i>specs</i>. <br />
 </p>
 </dd>
<dt><i>file</i><code>.adb</code></dt>
<dd> <p> Ada source code file containing a library unit body (a subprogram or package body). Such files are also called <i>bodies</i>. <br />
 </p>
 </dd>
<dt><i>file</i><code>.s</code></dt>
<dd> <p> Assembler code. <br />
 </p>
 </dd>
<dt><i>file</i><code>.S</code></dt>
<dd> <p> Assembler code which must be preprocessed. <br />
 </p>
 </dd>
<dt><i>other</i></dt>
<dd> <p> An object file to be fed straight into linking. Any file name with no recognized suffix is treated this way. </p>
 </dd></dl>
<p> You can specify the input language explicitly with the <code>-x</code> option: <br />
 </p>
<dl>
<dt><code>-x</code><i>language</i></dt>
<dd> <p> Specify explicitly the <i>language</i> for the following input files (rather than letting the compiler choose a default based on the file name suffix). This option applies to all following input files until the next <code>-x</code> option. Possible values for <i>language</i> are: </p>
<pre><code>        c c-header cpp-output
        c++ c++-cpp-output
        objective-c objc-cpp-output
        assembler assembler-with-cpp
        ada
        f77 f77-cpp-input ratfor
        java
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-x none</code></dt>
<dd> <p> Turn off any specification of a language, so that subsequent files are handled according to their file name suffixes (as they are if <code>-x</code> has not been used at all). <br />
 </p>
 </dd>
<dt><code>-pass-exit-codes</code></dt>
<dd> <p> Normally the <code>gcc</code> program will exit with the code of 1 if any phase of the compiler returns a non-success return code. If you specify <code>-pass-exit-codes</code>, the <code>gcc</code> program will instead return with numerically highest error produced by any phase that returned an error indication. </p>
 </dd></dl>
<p> If you only want some of the stages of compilation, you can use <code>-x</code> (or filename suffixes) to tell <code>gcc</code> where to start, and one of the options <code>-c</code>, <code>-S</code>, or <code>-E</code> to say where <code>gcc</code> is to stop. Note that some combinations (for example, <code>-x cpp-output -E</code>) instruct <code>gcc</code> to do nothing at all. <br />
 </p>
<dl>
<dt><code>-c</code></dt>
<dd> <p> Compile or assemble the source files, but do not link. The linking stage simply is not done. The ultimate output is in the form of an object file for each source file. </p>
<p> By default, the object file name for a source file is made by replacing the suffix <code>.c</code>, <code>.i</code>, <code>.s</code>, etc., with <code>.o</code>. </p>
<p> Unrecognized input files, not requiring compilation or assembly, are ignored. <br />
 </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Stop after the stage of compilation proper; do not assemble. The output is in the form of an assembler code file for each non-assembler input file specified. </p>
<p> By default, the assembler file name for a source file is made by replacing the suffix <code>.c</code>, <code>.i</code>, etc., with <code>.s</code>. </p>
<p> Input files that don&#8217;t require compilation are ignored. <br />
 </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Stop after the preprocessing stage; do not run the compiler proper. The output is in the form of preprocessed source code, which is sent to the standard output. </p>
<p> Input files which don&#8217;t require preprocessing are ignored. <br />
 </p>
 </dd>
<dt><code>-o</code><i>file</i></dt>
<dd> <p> Place output in file <i>file</i>. This applies regardless to whatever sort of output is being produced, whether it be an executable file, an object file, an assembler file or preprocessed C code. </p>
<p> Since only one output file can be specified, it does not make sense to use <code>-o</code> when compiling more than one input file, unless you are producing an executable file as output. </p>
<p> If <code>-o</code> is not specified, the default is to put an executable file in <i>a.out</i>, the object file for <i>source.suffix</i> in <i>source.o</i>, its assembler file in <i>source.s</i>, and all preprocessed C source on standard output. <br />
 </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print (on standard error output) the commands executed to run the stages of compilation. Also print the version number of the compiler driver program and of the preprocessor and the compiler proper. <br />
 </p>
 </dd>
<dt><code>-###</code></dt>
<dd> <p> Like <code>-v</code> except the commands are not executed and all command arguments are quoted. This is useful for shell scripts to capture the driver-generated command lines. <br />
 </p>
 </dd>
<dt><code>-pipe</code></dt>
<dd> <p> Use pipes rather than temporary files for communication between the various stages of compilation. This fails to work on some systems where the assembler is unable to read from a pipe; but the <font SIZE="-1">GNU</font> assembler has no trouble. <br />
 </p>
 </dd>
<dt><code>---help</code></dt>
<dd> <p> Print (on the standard output) a description of the command line options understood by <code>gcc</code>. If the <code>-v</code> option is also specified then <code>---help</code> will also be passed on to the various processes invoked by <code>gcc</code>, so that they can display the command line options they accept. If the <code>-W</code> option is also specified then command line options which have no documentation associated with them will also be displayed. <br />
 </p>
 </dd>
<dt><code>---target-help</code></dt>
<dd> <p> Print (on the standard output) a description of target specific command line options for each tool. <br />
 </p>
 </dd>
<dt><code>---version</code></dt>
<dd> <p> Display the version number and copyrights of the invoked <font SIZE="-1">GCC</font>. </p>
 </dd></dl>
<font SIZE="-2"></font><h2>Compiling C ++ Programs</h2>
<p> C<font SIZE="-2">++</font> source files conventionally use one of the suffixes <code>.C</code>, <code>.cc</code>, <code>.cpp</code>, <code>.c++</code>, <code>.cp</code>, or <code>.cxx</code>; preprocessed C<font SIZE="-2">++</font> files use the suffix <code>.ii</code>. <font SIZE="-1">GCC</font> recognizes files with these names and compiles them as C<font SIZE="-2">++</font> programs even if you call the compiler the same way as for compiling C programs (usually with the name <code>gcc</code>). </p>
<p> However, C<font SIZE="-2">++</font> programs often require class libraries as well as a compiler that understands the C<font SIZE="-2">++</font> language---and under some circumstances, you might want to compile programs from standard input, or otherwise without a suffix that flags them as C<font SIZE="-2">++</font> programs. <code>g++</code> is a program that calls <font SIZE="-1">GCC</font> with the default language set to C<font SIZE="-2">++</font>, and automatically specifies linking against the C<font SIZE="-2">++</font> library. On many systems, <code>g++</code> is also installed with the name <code>c++</code>. </p>
<p> When you compile C<font SIZE="-2">++</font> programs, you may specify many of the same command-line options that you use for compiling programs in any language; or command-line options meaningful for C and related languages; or options that are meaningful only for C<font SIZE="-2">++</font> programs.  </p>
<h2>Options Controlling C Dialect</h2>
<p> The following options control the dialect of C (or languages derived from C, such as C<font SIZE="-2">++</font> and Objective-C) that the compiler accepts: <br />
 </p>
<dl>
<dt><code>-ansi</code></dt>
<dd> <p> In C mode, support all <font SIZE="-1">ISO</font> C89 programs. In C<font SIZE="-2">++</font> mode, remove <font SIZE="-1">GNU</font> extensions that conflict with <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>. </p>
<p> This turns off certain features of <font SIZE="-1">GCC</font> that are incompatible with <font SIZE="-1">ISO</font> C89 (when compiling C code), or of standard C<font SIZE="-2">++</font> (when compiling C<font SIZE="-2">++</font> code), such as the <code>&quot;asm&quot;</code> and <code>&quot;typeof&quot;</code> keywords, and predefined macros such as <code>&quot;unix&quot;</code> and <code>&quot;vax&quot;</code> that identify the type of system you are using. It also enables the undesirable and rarely used <font SIZE="-1">ISO</font> trigraph feature. For the C compiler, it disables recognition of C<font SIZE="-2">++</font> style <code>//</code> comments as well as the <code>&quot;inline&quot;</code> keyword. </p>
<p> The alternate keywords <code>&quot;__asm__&quot;</code>, <code>&quot;__extension__&quot;</code>, <code>&quot;__inline__&quot;</code> and <code>&quot;__typeof__&quot;</code> continue to work despite <code>-ansi</code>. You would not want to use them in an <font SIZE="-1">ISO</font> C program, of course, but it is useful to put them in header files that might be included in compilations done with <code>-ansi</code>. Alternate predefined macros such as <code>&quot;__unix__&quot;</code> and <code>&quot;__vax__&quot;</code> are also available, with or without <code>-ansi</code>. </p>
<p> The <code>-ansi</code> option does not cause non-ISO programs to be rejected gratuitously. For that, <code>-pedantic</code> is required in addition to <code>-ansi</code>. </p>
<p> The macro <code>&quot;__STRICT_ANSI__&quot;</code> is predefined when the <code>-ansi</code> option is used. Some header files may notice this macro and refrain from declaring certain functions or defining certain macros that the <font SIZE="-1">ISO</font> standard doesn&#8217;t call for; this is to avoid interfering with any programs that might use these names for other things. </p>
<p> Functions which would normally be built in but do not have semantics defined by <font SIZE="-1">ISO</font> C (such as <code>&quot;alloca&quot;</code> and <code>&quot;ffs&quot;</code>) are not built-in functions with <code>-ansi</code> is used. <br />
 </p>
 </dd>
<dt><code>-std=</code></dt>
<dd> <p> Determine the language standard. This option is currently only supported when compiling C. A value for this option must be provided; possible values are </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>c89</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:1990</code></dt>
<dd> <p> <font SIZE="-1">ISO</font> C89 (same as <code>-ansi</code>). <br />
 </p>
 </dd>
<dt><code>iso9899:199409</code></dt>
<dd> <p> <font SIZE="-1">ISO</font> C89 as modified in amendment 1. <br />
 </p>
 </dd>
<dt><code>c99</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c9x</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:1999</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:199x</code></dt>
<dd> <p> <font SIZE="-1">ISO</font> C99. Note that this standard is not yet fully supported; see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/gcc-3.1/c99status.html">http://gcc.gnu.org/gcc-3.1/c99status.html</a></code>&gt; for more information. The names <code>c9x</code> and <code>iso9899:199x</code> are deprecated. <br />
 </p>
 </dd>
<dt><code>gnu89</code></dt>
<dd> <p> Default, <font SIZE="-1">ISO</font> C89 plus <font SIZE="-1">GNU</font> extensions (including some C99 features). <br />
 </p>
 </dd>
<dt><code>gnu99</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>gnu9x</code></dt>
<dd> <p> <font SIZE="-1">ISO</font> C99 plus <font SIZE="-1">GNU</font> extensions. When <font SIZE="-1">ISO</font> C99 is fully implemented in <font SIZE="-1">GCC</font>, this will become the default. The name <code>gnu9x</code> is deprecated. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Even when this option is not specified, you can still use some of the features of newer standards in so far as they do not conflict with previous C standards. For example, you may use <code>&quot;__restrict__&quot;</code> even when <code>-std=c99</code> is not specified. </p>
<p> The <code>-std</code> options specifying some version of <font SIZE="-1">ISO</font> C have the same effects as <code>-ansi</code>, except that features that were not in <font SIZE="-1">ISO</font> C89 but are in the specified version (for example, <code>//</code> comments and the <code>&quot;inline&quot;</code> keyword in <font SIZE="-1">ISO</font> C99) are not disabled. </p>
 </dd></dl>
<p> <br />
 </p>
<dt><code>-aux-info</code><i>filename</i></dt>
<dd> <p> Output to the given filename prototyped declarations for all functions declared and/or defined in a translation unit, including those in header files. This option is silently ignored in any language other than C. </p>
<p> Besides declarations, the file indicates, in comments, the origin of each declaration (source file and line), whether the declaration was implicit, prototyped or unprototyped (<code>I</code>, <code>N</code> for new or <code>O</code> for old, respectively, in the first character after the line number and the colon), and whether it came from a declaration or a definition (<code>C</code> or <code>F</code>, respectively, in the following character). In the case of function definitions, a K&amp;R-style list of arguments followed by their declarations is also provided, inside comments, after the declaration. <br />
 </p>
 </dd>
<dt><code>-fno-asm</code></dt>
<dd> <p> Do not recognize <code>&quot;asm&quot;</code>, <code>&quot;inline&quot;</code> or <code>&quot;typeof&quot;</code> as a keyword, so that code can use these words as identifiers. You can use the keywords <code>&quot;__asm__&quot;</code>, <code>&quot;__inline__&quot;</code> and <code>&quot;__typeof__&quot;</code> instead. <code>-ansi</code> implies <code>-fno-asm</code>. </p>
<p> In C<font SIZE="-2">++</font>, this switch only affects the <code>&quot;typeof&quot;</code> keyword, since <code>&quot;asm&quot;</code> and <code>&quot;inline&quot;</code> are standard keywords. You may want to use the <code>-fno-gnu-keywords</code> flag instead, which has the same effect. In C99 mode (<code>-std=c99</code> or <code>-std=gnu99</code>), this switch only affects the <code>&quot;asm&quot;</code> and <code>&quot;typeof&quot;</code> keywords, since <code>&quot;inline&quot;</code> is a standard keyword in <font SIZE="-1">ISO</font> C99. <br />
 </p>
 </dd>
<dt><code>-fno-builtin</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fno-builtin-</code><i>function</i>(C and Objective-C only)</dt>
<dd> <p> Don&#8217;t recognize built-in functions that do not begin with <code>__builtin_</code> as prefix. </p>
<p> <font SIZE="-1">GCC</font> normally generates special code to handle certain built-in functions more efficiently; for instance, calls to <code>&quot;alloca&quot;</code> may become single instructions that adjust the stack directly, and calls to <code>&quot;memcpy&quot;</code> may become inline copy loops. The resulting code is often both smaller and faster, but since the function calls no longer appear as such, you cannot set a breakpoint on those calls, nor can you change the behavior of the functions by linking with a different library. </p>
<p> In C<font SIZE="-2">++</font>, <code>-fno-builtin</code> is always in effect. The <code>-fbuiltin</code> option has no effect. Therefore, in C<font SIZE="-2">++</font>, the only way to get the optimization benefits of built-in functions is to call the function using the <code>__builtin_</code> prefix. The <font SIZE="-1">GNU</font> C<font SIZE="-2">++</font> Standard Library uses built-in functions to implement many functions (like <code>&quot;std::strchr&quot;</code>), so that you automatically get efficient code. </p>
<p> With the <code>-fno-builtin-</code><i>function</i> option, not available when compiling C<font SIZE="-2">++</font>, only the built-in function <i>function</i> is disabled. <i>function</i> must not begin with <code>__builtin_</code>. If a function is named this is not built-in in this version of <font SIZE="-1">GCC</font>, this option is ignored. There is no corresponding <code>-fbuiltin-</code><i>function</i> option; if you wish to enable built-in functions selectively when using <code>-fno-builtin</code> or <code>-ffreestanding</code>, you may define macros such as: </p>
<pre><code>        #defineabs(n) __builtin_abs ((n))
        #define strcpy(d, s) __builtin_strcpy ((d), (s))
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-fhosted</code></dt>
<dd> <p> Assert that compilation takes place in a hosted environment. This implies <code>-fbuiltin</code>. A hosted environment is one in which the entire standard library is available, and in which <code>&quot;main&quot;</code> has a return type of <code>&quot;int&quot;</code>. Examples are nearly everything except a kernel. This is equivalent to <code>-fno-freestanding</code>. <br />
 </p>
 </dd>
<dt><code>-ffreestanding</code></dt>
<dd> <p> Assert that compilation takes place in a freestanding environment. This implies <code>-fno-builtin</code>. A freestanding environment is one in which the standard library may not exist, and program startup may not necessarily be at <code>&quot;main&quot;</code>. The most obvious example is an <font SIZE="-1">OS</font> kernel. This is equivalent to <code>-fno-hosted</code>. <br />
 </p>
 </dd>
<dt><code>-trigraphs</code></dt>
<dd> <p> Support <font SIZE="-1">ISO</font> C trigraphs. The <code>-ansi</code> option (and <code>-std</code> options for strict <font SIZE="-1">ISO</font> C conformance) implies <code>-trigraphs</code>. <br />
 </p>
 </dd>
<dt><code>-no-integrated-cpp</code></dt>
<dd> <p> Invoke the external cpp during compilation. The default is to use the integrated cpp (internal cpp). This option also allows a user-supplied cpp via the <code>-B</code> option. This flag is applicable in both C and C<font SIZE="-2">++</font> modes. </p>
<p> We do not guarantee to retain this option in future, and we may change its semantics. <br />
 </p>
 </dd>
<dt><code>-traditional</code></dt>
<dd> <p> Attempt to support some aspects of traditional C compilers. Specifically: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>*</dt>
<dd> <p> All <code>&quot;extern&quot;</code> declarations take effect globally even if they are written inside of a function definition. This includes implicit declarations of functions. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> The newer keywords <code>&quot;typeof&quot;</code>, <code>&quot;inline&quot;</code>, <code>&quot;signed&quot;</code>, <code>&quot;const&quot;</code> and <code>&quot;volatile&quot;</code> are not recognized. (You can still use the alternative keywords such as <code>&quot;__typeof__&quot;</code>, <code>&quot;__inline__&quot;</code>, and so on.) <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Comparisons between pointers and integers are always allowed. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Integer types <code>&quot;unsigned short&quot;</code> and <code>&quot;unsigned char&quot;</code> promote to <code>&quot;unsigned int&quot;</code>. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Out-of-range floating point literals are not an error. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Certain constructs which <font SIZE="-1">ISO</font> regards as a single invalid preprocessing number, such as <code>0xe-0xd</code>, are treated as expressions instead. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> String ``constants&#8217;&#8216; are not necessarily constant; they are stored in writable space, and identical looking constants are allocated separately. (This is the same as the effect of <code>-fwritable-strings</code>.) <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> All automatic variables not declared <code>&quot;register&quot;</code> are preserved by <code>&quot;longjmp&quot;</code>. Ordinarily, <font SIZE="-1">GNU</font> C follows <font SIZE="-1">ISO</font> C: automatic variables not declared <code>&quot;volatile&quot;</code> may be clobbered. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> The character escape sequences <code>\x</code> and <code>\a</code> evaluate as the literal characters <code>x</code> and <code>a</code> respectively. Without <code>-traditional</code>, <code>\x</code> is a prefix for the hexadecimal representation of a character, and <code>\a</code> produces a bell. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> This option is deprecated and may be removed. </p>
<p> You may wish to use <code>-fno-builtin</code> as well as <code>-traditional</code> if your program uses names that are normally <font SIZE="-1">GNU</font> C built-in functions for other purposes of its own. </p>
<p> You cannot use <code>-traditional</code> if you include any header files that rely on <font SIZE="-1">ISO</font> C features. Some vendors are starting to ship systems with <font SIZE="-1">ISO</font> C header files and you cannot use <code>-traditional</code> on such systems to compile files that include any system headers. </p>
<p> The <code>-traditional</code> option also enables <code>-traditional-cpp</code>. </p>
 </dd></dl>
<p> <br />
 </p>
<dt><code>-traditional-cpp</code></dt>
<dd> <p> Attempt to support some aspects of traditional C preprocessors. See the <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font> manual for details. <br />
 </p>
 </dd>
<dt><code>-fcond-mismatch</code></dt>
<dd> <p> Allow conditional expressions with mismatched types in the second and third arguments. The value of such an expression is void. This option is not supported for C<font SIZE="-2">++</font>. <br />
 </p>
 </dd>
<dt><code>-funsigned-char</code></dt>
<dd> <p> Let the type <code>&quot;char&quot;</code> be unsigned, like <code>&quot;unsigned char&quot;</code>. </p>
<p> Each kind of machine has a default for what <code>&quot;char&quot;</code> should be. It is either like <code>&quot;unsigned char&quot;</code> by default or like <code>&quot;signed char&quot;</code> by default. </p>
<p> Ideally, a portable program should always use <code>&quot;signed char&quot;</code> or <code>&quot;unsigned char&quot;</code> when it depends on the signedness of an object. But many programs have been written to use plain <code>&quot;char&quot;</code> and expect it to be signed, or expect it to be unsigned, depending on the machines they were written for. This option, and its inverse, let you make such a program work with the opposite default. </p>
<p> The type <code>&quot;char&quot;</code> is always a distinct type from each of <code>&quot;signed char&quot;</code> or <code>&quot;unsigned char&quot;</code>, even though its behavior is always just like one of those two. <br />
 </p>
 </dd>
<dt><code>-fsigned-char</code></dt>
<dd> <p> Let the type <code>&quot;char&quot;</code> be signed, like <code>&quot;signed char&quot;</code>. </p>
<p> Note that this is equivalent to <code>-fno-unsigned-char</code>, which is the negative form of <code>-funsigned-char</code>. Likewise, the option <code>-fno-signed-char</code> is equivalent to <code>-funsigned-char</code>. <br />
 </p>
 </dd>
<dt><code>-fsigned-bitfields</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-funsigned-bitfields</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fno-signed-bitfields</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fno-unsigned-bitfields</code></dt>
<dd> <p> These options control whether a bit-field is signed or unsigned, when the declaration does not use either <code>&quot;signed&quot;</code> or <code>&quot;unsigned&quot;</code>. By default, such a bit-field is signed, because this is consistent: the basic integer types such as <code>&quot;int&quot;</code> are signed types. </p>
<p> However, when <code>-traditional</code> is used, bit-fields are all unsigned no matter what. <br />
 </p>
 </dd>
<dt><code>-fwritable-strings</code></dt>
<dd> <p> Store string constants in the writable data segment and don&#8217;t uniquize them. This is for compatibility with old programs which assume they can write into string constants. The option <code>-traditional</code> also has this effect. </p>
<p> Writing into string constants is a very bad idea; ``constants&#8217;&#8216; should be constant. <br />
 </p>
 </dd>
<dt><code>-fallow-single-precision</code></dt>
<dd> <p> Do not promote single precision math operations to double precision, even when compiling with <code>-traditional</code>. </p>
<p> Traditional K&amp;R C promotes all floating point operations to double precision, regardless of the sizes of the operands. On the architecture for which you are compiling, single precision may be faster than double precision. If you must use <code>-traditional</code>, but want to use single precision operations when the operands are single precision, use this option. This option has no effect when compiling with <font SIZE="-1">ISO</font> or <font SIZE="-1">GNU</font> C conventions (the default). </p>
 </dd></dl>
<font SIZE="-2"></font><h2>Options Controlling C ++ Dialect</h2>
<p> This section describes the command-line options that are only meaningful for C<font SIZE="-2">++</font> programs; but you can also use most of the <font SIZE="-1">GNU</font> compiler options regardless of what language your program is in. For example, you might compile a file <code>&quot;firstClass.C&quot;</code> like this: </p>
<pre><code>        g++ -g -frepo -O -c firstClass.C
</code></pre>
<p> In this example, only <code>-frepo</code> is an option meant only for C<font SIZE="-2">++</font> programs; you can use the other options with any language supported by <font SIZE="-1">GCC</font>. </p>
<p> Here is a list of options that are <i>only</i> for compiling C<font SIZE="-2">++</font> programs: <br />
 </p>
<dl>
<dt><code>-fno-access-control</code></dt>
<dd> <p> Turn off all access checking. This switch is mainly useful for working around bugs in the access control code. <br />
 </p>
 </dd>
<dt><code>-fcheck-new</code></dt>
<dd> <p> Check that the pointer returned by <code>&quot;operator new&quot;</code> is non-null before attempting to modify the storage allocated. The current Working Paper requires that <code>&quot;operator new&quot;</code> never return a null pointer, so this check is normally unnecessary. </p>
<p> An alternative to using this option is to specify that your <code>&quot;operator new&quot;</code> does not throw any exceptions; if you declare it throw(), G++ will check the return value. See also <code>new (nothrow)</code>. <br />
 </p>
 </dd>
<dt><code>-fconserve-space</code></dt>
<dd> <p> Put uninitialized or runtime-initialized global variables into the common segment, as C does. This saves space in the executable at the cost of not diagnosing duplicate definitions. If you compile with this flag and your program mysteriously crashes after <code>&quot;main()&quot;</code> has completed, you may have an object that is being destroyed twice because two definitions were merged. </p>
<p> This option is no longer useful on most targets, now that support has been added for putting variables into <font SIZE="-1">BSS</font> without making them common. <br />
 </p>
 </dd>
<dt><code>-fno-const-strings</code></dt>
<dd> <p> Give string constants type <code>&quot;char *&quot;</code> instead of type <code>&quot;const char *&quot;</code>. By default, G++ uses type <code>&quot;const char *&quot;</code> as required by the standard. Even if you use <code>-fno-const-strings</code>, you cannot actually modify the value of a string constant, unless you also use <code>-fwritable-strings</code>. </p>
<p> This option might be removed in a future release of G++. For maximum portability, you should structure your code so that it works with string constants that have type <code>&quot;const char *&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-fdollars-in-identifiers</code></dt>
<dd> <p> Accept <code>$</code> in identifiers. You can also explicitly prohibit use of <code>$</code> with the option <code>-fno-dollars-in-identifiers</code>. (<font SIZE="-1">GNU</font> C allows <code>$</code> by default on most target systems, but there are a few exceptions.) Traditional C allowed the character <code>$</code> to form part of identifiers. However, <font SIZE="-1">ISO</font> C and C<font SIZE="-2">++</font> forbid <code>$</code> in identifiers. <br />
 </p>
 </dd>
<dt><code>-fno-elide-constructors</code></dt>
<dd> <p> The C<font SIZE="-2">++</font> standard allows an implementation to omit creating a temporary which is only used to initialize another object of the same type. Specifying this option disables that optimization, and forces G++ to call the copy constructor in all cases. <br />
 </p>
 </dd>
<dt><code>-fno-enforce-eh-specs</code></dt>
<dd> <p> Don&#8217;t check for violation of exception specifications at runtime. This option violates the C<font SIZE="-2">++</font> standard, but may be useful for reducing code size in production builds, much like defining <font SIZE="-1"><code>NDEBUG</code></font>. The compiler will still optimize based on the exception specifications. <br />
 </p>
 </dd>
<dt><code>-fexternal-templates</code></dt>
<dd> <p> Cause <code>#pragma interface</code> and <code>implementation</code> to apply to template instantiation; template instances are emitted or not according to the location of the template definition. </p>
<p> This option is deprecated. <br />
 </p>
 </dd>
<dt><code>-falt-external-templates</code></dt>
<dd> <p> Similar to <code>-fexternal-templates</code>, but template instances are emitted or not according to the place where they are first instantiated. </p>
<p> This option is deprecated. <br />
 </p>
 </dd>
<dt><code>-ffor-scope</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fno-for-scope</code></dt>
<dd> <p> If <code>-ffor-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> is limited to the <code>for</code> loop itself, as specified by the C<font SIZE="-2">++</font> standard. If <code>-fno-for-scope</code> is specified, the scope of variables declared in a <i>for-init-statement</i> extends to the end of the enclosing scope, as was the case in old versions of G++, and other (traditional) implementations of C<font SIZE="-2">++</font>. </p>
<p> The default if neither flag is given to follow the standard, but to allow and give a warning for old-style code that would otherwise be invalid, or have different behavior. <br />
 </p>
 </dd>
<dt><code>-fno-gnu-keywords</code></dt>
<dd> <p> Do not recognize <code>&quot;typeof&quot;</code> as a keyword, so that code can use this word as an identifier. You can use the keyword <code>&quot;__typeof__&quot;</code> instead. <code>-ansi</code> implies <code>-fno-gnu-keywords</code>. <br />
 </p>
 </dd>
<dt><code>-fno-implicit-templates</code></dt>
<dd> <p> Never emit code for non-inline templates which are instantiated implicitly (i.e. by use); only emit code for explicit instantiations. <br />
 </p>
 </dd>
<dt><code>-fno-implicit-inline-templates</code></dt>
<dd> <p> Don&#8217;t emit code for implicit instantiations of inline templates, either. The default is to handle inlines differently so that compiles with and without optimization will need the same set of explicit instantiations. <br />
 </p>
 </dd>
<dt><code>-fno-implement-inlines</code></dt>
<dd> <p> To save space, do not emit out-of-line copies of inline functions controlled by <code>#pragma implementation</code>. This will cause linker errors if these functions are not inlined everywhere they are called. <br />
 </p>
 </dd>
<dt><code>-fms-extensions</code></dt>
<dd> <p> Disable pedantic warnings about constructs used in <font SIZE="-1">MFC</font>, such as implicit int and getting a pointer to member function via non-standard syntax. <br />
 </p>
 </dd>
<dt><code>-fno-nonansi-builtins</code></dt>
<dd> <p> Disable built-in declarations of functions that are not mandated by <font SIZE="-1">ANSI/ISO</font> C. These include <code>&quot;ffs&quot;</code>, <code>&quot;alloca&quot;</code>, <code>&quot;_exit&quot;</code>, <code>&quot;index&quot;</code>, <code>&quot;bzero&quot;</code>, <code>&quot;conjf&quot;</code>, and other related functions. <br />
 </p>
 </dd>
<dt><code>-fno-operator-names</code></dt>
<dd> <p> Do not treat the operator name keywords <code>&quot;and&quot;</code>, <code>&quot;bitand&quot;</code>, <code>&quot;bitor&quot;</code>, <code>&quot;compl&quot;</code>, <code>&quot;not&quot;</code>, <code>&quot;or&quot;</code> and <code>&quot;xor&quot;</code> as synonyms as keywords. <br />
 </p>
 </dd>
<dt><code>-fno-optional-diags</code></dt>
<dd> <p> Disable diagnostics that the standard says a compiler does not need to issue. Currently, the only such diagnostic issued by G++ is the one for a name having multiple meanings within a class. <br />
 </p>
 </dd>
<dt><code>-fpermissive</code></dt>
<dd> <p> Downgrade messages about nonconformant code from errors to warnings. By default, G++ effectively sets <code>-pedantic-errors</code> without <code>-pedantic</code>; this option reverses that. This behavior and this option are superseded by <code>-pedantic</code>, which works as it does for <font SIZE="-1">GNU</font> C. <br />
 </p>
 </dd>
<dt><code>-frepo</code></dt>
<dd> <p> Enable automatic template instantiation at link time. This option also implies <code>-fno-implicit-templates</code>. <br />
 </p>
 </dd>
<dt><code>-fno-rtti</code></dt>
<dd> <p> Disable generation of information about every class with virtual functions for use by the C<font SIZE="-2">++</font> runtime type identification features (<code>dynamic_cast</code> and <code>typeid</code>). If you don&#8217;t use those parts of the language, you can save some space by using this flag. Note that exception handling uses the same information, but it will generate it as needed. <br />
 </p>
 </dd>
<dt><code>-fstats</code></dt>
<dd> <p> Emit statistics about front-end processing at the end of the compilation. This information is generally only useful to the G++ development team. <br />
 </p>
 </dd>
<dt><code>-ftemplate-depth-</code><i>n</i></dt>
<dd> <p> Set the maximum instantiation depth for template classes to <i>n</i>. A limit on the template instantiation depth is needed to detect endless recursions during template class instantiation. <font SIZE="-1">ANSI/ISO</font> C<font SIZE="-2">++</font> conforming programs must not rely on a maximum depth greater than 17. <br />
 </p>
 </dd>
<dt><code>-fuse-cxa-atexit</code></dt>
<dd> <p> Register destructors for objects with static storage duration with the <code>&quot;__cxa_atexit&quot;</code> function rather than the <code>&quot;atexit&quot;</code> function. This option is required for fully standards-compliant handling of static destructors, but will only work if your C library supports <code>&quot;__cxa_atexit&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-fvtable-gc</code></dt>
<dd> <p> Emit special relocations for vtables and virtual function references so that the linker can identify unused virtual functions and zero out vtable slots that refer to them. This is most useful with <code>-ffunction-sections</code> and <code>-Wl,--gc-sections</code>, in order to also discard the functions themselves. </p>
<p> This optimization requires <font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld. Not all systems support this option. <code>-Wl,--gc-sections</code> is ignored without <code>-static</code>. <br />
 </p>
 </dd>
<dt><code>-fno-weak</code></dt>
<dd> <p> Do not use weak symbol support, even if it is provided by the linker. By default, G++ will use weak symbols if they are available. This option exists only for testing, and should not be used by end-users; it will result in inferior code and has no benefits. This option may be removed in a future release of G++. <br />
 </p>
 </dd>
<dt><code>-nostdinc++</code></dt>
<dd> <p> Do not search for header files in the standard directories specific to C<font SIZE="-2">++</font>, but do still search the other standard directories. (This option is used when building the C<font SIZE="-2">++</font> library.) </p>
 </dd></dl>
<p> In addition, these optimization, warning, and code generation options have meanings only for C<font SIZE="-2">++</font> programs: <br />
 </p>
<dl>
<dt><code>-fno-default-inline</code></dt>
<dd> <p> Do not assume <code>inline</code> for functions defined inside a class scope. <br />
&nbsp;<wbr>&nbsp;<wbr>Note that these functions will have linkage like inline functions; they just won&#8217;t be inlined by default. <br />
 </p>
 </dd>
<dt><code>-Wabi</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when G++ generates code that is probably not compatible with the vendor-neutral C<font SIZE="-2">++</font> <font SIZE="-1">ABI</font>. Although an effort has been made to warn about all such cases, there are probably some cases that are not warned about, even though G++ is generating incompatible code. There may also be cases where warnings are emitted even though the code that is generated will be compatible. </p>
<p> You should rewrite your code to avoid these warnings if you are concerned about the fact that code generated by G++ may not be binary compatible with code generated by other compilers. </p>
<p> The known incompatibilites at this point include: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>*</dt>
<dd> <p> Incorrect handling of tail-padding for bit-fields. G++ may attempt to pack data into the same byte as a base class. For example: </p>
<pre><code>        struct A { virtual void f(); int f1 : 1; };
        struct B : public A { int f2 : 1; };
</code></pre>
<p> In this case, G++ will place <code>&quot;B::f2&quot;</code> into the same byte as <code>&quot;A::f1&quot;</code>; other compilers will not. You can avoid this problem by explicitly padding <code>&quot;A&quot;</code> so that its size is a multiple of the byte size on your platform; that will cause G++ and other compilers to layout <code>&quot;B&quot;</code> identically. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Incorrect handling of tail-padding for virtual bases. G++ does not use tail padding when laying out virtual bases. For example: </p>
<pre><code>        struct A { virtual void f(); char c1; };
        struct B { B(); char c2; };
        struct C : public A, public virtual B {};
</code></pre>
<p> In this case, G++ will not place <code>&quot;B&quot;</code> into the tail-padding for <code>&quot;A&quot;</code>; other compilers will. You can avoid this problem by explicitly padding <code>&quot;A&quot;</code> so that its size is a multiple of its alignment (ignoring virtual base classes); that will cause G++ and other compilers to layout <code>&quot;C&quot;</code> identically. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-Wctor-dtor-privacy</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when a class seems unusable, because all the constructors or destructors in a class are private and the class has no friends or public static member functions. <br />
 </p>
 </dd>
<dt><code>-Wnon-virtual-dtor</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when a class declares a non-virtual destructor that should probably be virtual, because it looks like the class will be used polymorphically. <br />
 </p>
 </dd>
<dt><code>-Wreorder</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when the order of member initializers given in the code does not match the order in which they must be executed. For instance: </p>
<pre><code>        struct A {
          int i;
          int j;
          A(): j (0), i (1) { }
        };
</code></pre>
<p> Here the compiler will warn that the member initializers for <code>i</code> and <code>j</code> will be rearranged to match the declaration order of the members. </p>
 </dd></dl>
<p> The following <code>-W...</code> options are not affected by <code>-Wall</code>. <br />
 </p>
<dl>
<dt><code>-Weffc++</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn about violations of the following style guidelines from Scott Meyers&#8217; <i>Effective C<font SIZE="-2">++</font></i> book: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>*</dt>
<dd> <p> Item 11: Define a copy constructor and an assignment operator for classes with dynamically allocated memory. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Item 12: Prefer initialization to assignment in constructors. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Item 14: Make destructors virtual in base classes. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Item 15: Have <code>&quot;operator=&quot;</code> return a reference to <code>&quot;*this&quot;</code>. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Item 23: Don&#8217;t try to return a reference when you must return an object. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> and about violations of the following style guidelines from Scott Meyers&#8217; <i>More Effective C<font SIZE="-2">++</font></i> book: </p>
 </dd>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dl>
<dt>*</dt>
<dd> <p> Item 6: Distinguish between prefix and postfix forms of increment and decrement operators. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Item 7: Never overload <code>&quot;&amp;&amp;&quot;</code>, <code>&quot;||&quot;</code>, or <code>&quot;,&quot;</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> If you use this option, you should be aware that the standard library headers do not obey all of these guidelines; you can use <code>grep -v</code> to filter out those warnings. </p>
 </dd></dl>
<p> <br />
 </p>
<dt><code>-Wno-deprecated</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Do not warn about usage of deprecated features. <br />
 </p>
 </dd>
<dt><code>-Wno-non-template-friend</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Disable warnings when non-templatized friend functions are declared within a template. With the advent of explicit template specification support in G++, if the name of the friend is an unqualified-id (i.e., <code>friend foo(int)</code>), the C<font SIZE="-2">++</font> language specification demands that the friend declare or define an ordinary, nontemplate function. (Section 14.5.3). Before G++ implemented explicit specification, unqualified-ids could be interpreted as a particular specialization of a templatized function. Because this non-conforming behavior is no longer the default behavior for G++, <code>-Wnon-template-friend</code> allows the compiler to check existing code for potential trouble spots, and is on by default. This new compiler behavior can be turned off with <code>-Wno-non-template-friend</code> which keeps the conformant compiler code but disables the helpful warning. <br />
 </p>
 </dd>
<dt><code>-Wold-style-cast</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn if an old-style (C-style) cast to a non-void type is used within a C<font SIZE="-2">++</font> program. The new-style casts (<code>static_cast</code>, <code>reinterpret_cast</code>, and <code>const_cast</code>) are less vulnerable to unintended effects, and much easier to grep for. <br />
 </p>
 </dd>
<dt><code>-Woverloaded-virtual</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when a function declaration hides virtual functions from a base class. For example, in: </p>
<pre><code>        struct A {
          virtual void f();
        };
</code></pre>
<pre><code>        struct B: public A {
          void f(int);
        };
</code></pre>
<p> the <code>&quot;A&quot;</code> class version of <code>&quot;f&quot;</code> is hidden in <code>&quot;B&quot;</code>, and code like this: </p>
<pre><code>        B* b;
        b-&gt;f();
</code></pre>
<p> will fail to compile. <br />
 </p>
 </dd>
<dt><code>-Wno-pmf-conversions</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Disable the diagnostic for converting a bound pointer to member function to a plain pointer. <br />
 </p>
 </dd>
<dt><code>-Wsign-promo</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when overload resolution chooses a promotion from unsigned or enumeral type to a signed type over a conversion to an unsigned type of the same size. Previous versions of G++ would try to preserve unsignedness, but the standard mandates the current behavior. <br />
 </p>
 </dd>
<dt><code>-Wsynth</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when G++&#8216;s synthesis behavior does not match that of cfront. For instance: </p>
<pre><code>        struct A {
          operator int ();
          A&amp; operator = (int);
        };
</code></pre>
<pre><code>        main ()
        {
          A a,b;
          a = b;
        }
</code></pre>
<p> In this example, G++ will synthesize a default <code>A&amp; operator = (const A&amp;);</code>, while cfront will use the user-defined <code>operator =</code>. </p>
 </dd></dl>
<h2>Options Controlling Objective-C Dialect</h2>
<p> This section describes the command-line options that are only meaningful for Objective-C programs; but you can also use most of the <font SIZE="-1">GNU</font> compiler options regardless of what language your program is in. For example, you might compile a file <code>&quot;some_class.m&quot;</code> like this: </p>
<pre><code>        gcc -g -fgnu-runtime -O -c some_class.m
</code></pre>
<p> In this example, only <code>-fgnu-runtime</code> is an option meant only for Objective-C programs; you can use the other options with any language supported by <font SIZE="-1">GCC</font>. </p>
<p> Here is a list of options that are <i>only</i> for compiling Objective-C programs: <br />
 </p>
<dl>
<dt><code>-fconstant-string-class=</code><i>class-name</i></dt>
<dd> <p> Use <i>class-name</i> as the name of the class to instantiate for each literal string specified with the syntax <code>&quot;@&quot;...&quot;&quot;</code>. The default class name is <code>&quot;NXConstantString&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-fgnu-runtime</code></dt>
<dd> <p> Generate object code compatible with the standard <font SIZE="-1">GNU</font> Objective-C runtime. This is the default for most types of systems. <br />
 </p>
 </dd>
<dt><code>-fnext-runtime</code></dt>
<dd> <p> Generate output compatible with the NeXT runtime. This is the default for NeXT-based systems, including Darwin and Mac <font SIZE="-1">OS</font> X. <br />
 </p>
 </dd>
<dt><code>-gen-decls</code></dt>
<dd> <p> Dump interface declarations for all classes seen in the source file to a file named <i>sourcename.decl</i>. <br />
 </p>
 </dd>
<dt><code>-Wno-protocol</code></dt>
<dd> <p> Do not warn if methods required by a protocol are not implemented in the class adopting it. <br />
 </p>
 </dd>
<dt><code>-Wselector</code></dt>
<dd> <p> Warn if a selector has multiple methods of different types defined. </p>
 </dd></dl>
<h2>Options to Control Diagnostic Messages Formatting</h2>
<p> Traditionally, diagnostic messages have been formatted irrespective of the output device&#8217;s aspect (e.g. its width, ...). The options described below can be used to control the diagnostic messages formatting algorithm, e.g. how many characters per line, how often source location information should be reported. Right now, only the C<font SIZE="-2">++</font> front end can honor these options. However it is expected, in the near future, that the remaining front ends would be able to digest them correctly. <br />
 </p>
<dl>
<dt><code>-fmessage-length=</code><i>n</i></dt>
<dd> <p> Try to format error messages so that they fit on lines of about <i>n</i> characters. The default is 72 characters for <code>g++</code> and 0 for the rest of the front ends supported by <font SIZE="-1">GCC</font>. If <i>n</i> is zero, then no line-wrapping will be done; each error message will appear on a single line. <br />
 </p>
 </dd>
<dt><code>-fdiagnostics-show-location=once</code></dt>
<dd> <p> Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit <i>once</i> source location information; that is, in case the message is too long to fit on a single physical line and has to be wrapped, the source location won&#8217;t be emitted (as prefix) again, over and over, in subsequent continuation lines. This is the default behavior. <br />
 </p>
 </dd>
<dt><code>-fdiagnostics-show-location=every-line</code></dt>
<dd> <p> Only meaningful in line-wrapping mode. Instructs the diagnostic messages reporter to emit the same source location information (as prefix) for physical lines that result from the process of breaking a message which is too long to fit on a single line. </p>
 </dd></dl>
<h2>Options to Request or Suppress Warnings</h2>
<p> Warnings are diagnostic messages that report constructions which are not inherently erroneous but which are risky or suggest there may have been an error. </p>
<p> You can request many specific warnings with options beginning <code>-W</code>, for example <code>-Wimplicit</code> to request warnings on implicit declarations. Each of these specific warning options also has a negative form beginning <code>-Wno-</code> to turn off warnings; for example, <code>-Wno-implicit</code>. This manual lists only one of the two forms, whichever is not the default. </p>
<p> The following options control the amount and kinds of warnings produced by <font SIZE="-1">GCC</font>; for further, language-specific options also refer to <code>@ref</code>{C<font SIZE="-2">++</font> Dialect Options} and <code>@ref</code>{Objective-C Dialect Options}. <br />
 </p>
<dl>
<dt><code>-fsyntax-only</code></dt>
<dd> <p> Check the code for syntax errors, but don&#8217;t do anything beyond that. <br />
 </p>
 </dd>
<dt><code>-pedantic</code></dt>
<dd> <p> Issue all the warnings demanded by strict <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>; reject all programs that use forbidden extensions, and some other programs that do not follow <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font>. For <font SIZE="-1">ISO</font> C, follows the version of the <font SIZE="-1">ISO</font> C standard specified by any <code>-std</code> option used. </p>
<p> Valid <font SIZE="-1">ISO</font> C and <font SIZE="-1">ISO</font> C<font SIZE="-2">++</font> programs should compile properly with or without this option (though a rare few will require <code>-ansi</code> or a <code>-std</code> option specifying the required version of <font SIZE="-1">ISO</font> C). However, without this option, certain <font SIZE="-1">GNU</font> extensions and traditional C and C<font SIZE="-2">++</font> features are supported as well. With this option, they are rejected. </p>
<p> <code>-pedantic</code> does not cause warning messages for use of the alternate keywords whose names begin and end with <code>__</code>. Pedantic warnings are also disabled in the expression that follows <code>&quot;__extension__&quot;</code>. However, only system header files should use these escape routes; application programs should avoid them. </p>
<p> Some users try to use <code>-pedantic</code> to check programs for strict <font SIZE="-1">ISO</font> C conformance. They soon find that it does not do quite what they want: it finds some non-ISO practices, but not all---only those for which <font SIZE="-1">ISO</font> C <i>requires</i> a diagnostic, and some others for which diagnostics have been added. </p>
<p> A feature to report any failure to conform to <font SIZE="-1">ISO</font> C might be useful in some instances, but would require considerable additional work and would be quite different from <code>-pedantic</code>. We don&#8217;t have plans to support such a feature in the near future. </p>
<p> Where the standard specified with <code>-std</code> represents a <font SIZE="-1">GNU</font> extended dialect of C, such as <code>gnu89</code> or <code>gnu99</code>, there is a corresponding <i>base standard</i>, the version of <font SIZE="-1">ISO</font> C on which the <font SIZE="-1">GNU</font> extended dialect is based. Warnings from <code>-pedantic</code> are given where they are required by the base standard. (It would not make sense for such warnings to be given only for features not in the specified <font SIZE="-1">GNU</font> C dialect, since by definition the <font SIZE="-1">GNU</font> dialects of C include all features the compiler supports with the given option, and there would be nothing to warn about.) <br />
 </p>
 </dd>
<dt><code>-pedantic-errors</code></dt>
<dd> <p> Like <code>-pedantic</code>, except that errors are produced rather than warnings. <br />
 </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Inhibit all warning messages. <br />
 </p>
 </dd>
<dt><code>-Wno-import</code></dt>
<dd> <p> Inhibit warning messages about the use of <code>#import</code>. <br />
 </p>
 </dd>
<dt><code>-Wchar-subscripts</code></dt>
<dd> <p> Warn if an array subscript has type <code>&quot;char&quot;</code>. This is a common cause of error, as programmers often forget that this type is signed on some machines. <br />
 </p>
 </dd>
<dt><code>-Wcomment</code></dt>
<dd> <p> Warn whenever a comment-start sequence <code>/*</code> appears in a <code>/*</code> comment, or whenever a Backslash-Newline appears in a <code>//</code> comment. <br />
 </p>
 </dd>
<dt><code>-Wformat</code></dt>
<dd> <p> Check calls to <code>&quot;printf&quot;</code> and <code>&quot;scanf&quot;</code>, etc., to make sure that the arguments supplied have types appropriate to the format string specified, and that the conversions specified in the format string make sense. This includes standard functions, and others specified by format attributes, in the <code>&quot;printf&quot;</code>, <code>&quot;scanf&quot;</code>, <code>&quot;strftime&quot;</code> and <code>&quot;strfmon&quot;</code> (an X/Open extension, not in the C standard) families. </p>
<p> The formats are checked against the format features supported by <font SIZE="-1">GNU</font> libc version 2.2. These include all <font SIZE="-1">ISO</font> C89 and C99 features, as well as features from the Single Unix Specification and some <font SIZE="-1">BSD</font> and <font SIZE="-1">GNU</font> extensions. Other library implementations may not support all these features; <font SIZE="-1">GCC</font> does not support warning about features that go beyond a particular library&#8217;s limitations. However, if <code>-pedantic</code> is used with <code>-Wformat</code>, warnings will be given about format features not in the selected standard version (but not for <code>&quot;strfmon&quot;</code> formats, since those are not in any version of the C standard). </p>
<p> <code>-Wformat</code> is included in <code>-Wall</code>. For more control over some aspects of format checking, the options <code>-Wno-format-y2k</code>, <code>-Wno-format-extra-args</code>, <code>-Wformat-nonliteral</code>, <code>-Wformat-security</code> and <code>-Wformat=2</code> are available, but are not included in <code>-Wall</code>. <br />
 </p>
 </dd>
<dt><code>-Wno-format-y2k</code></dt>
<dd> <p> If <code>-Wformat</code> is specified, do not warn about <code>&quot;strftime&quot;</code> formats which may yield only a two-digit year. <br />
 </p>
 </dd>
<dt><code>-Wno-format-extra-args</code></dt>
<dd> <p> If <code>-Wformat</code> is specified, do not warn about excess arguments to a <code>&quot;printf&quot;</code> or <code>&quot;scanf&quot;</code> format function. The C standard specifies that such arguments are ignored. </p>
<p> Where the unused arguments lie between used arguments that are specified with <code>$</code> operand number specifications, normally warnings are still given, since the implementation could not know what type to pass to <code>&quot;va_arg&quot;</code> to skip the unused arguments. However, in the case of <code>&quot;scanf&quot;</code> formats, this option will suppress the warning if the unused arguments are all pointers, since the Single Unix Specification says that such unused arguments are allowed. <br />
 </p>
 </dd>
<dt><code>-Wformat-nonliteral</code></dt>
<dd> <p> If <code>-Wformat</code> is specified, also warn if the format string is not a string literal and so cannot be checked, unless the format function takes its format arguments as a <code>&quot;va_list&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-Wformat-security</code></dt>
<dd> <p> If <code>-Wformat</code> is specified, also warn about uses of format functions that represent possible security problems. At present, this warns about calls to <code>&quot;printf&quot;</code> and <code>&quot;scanf&quot;</code> functions where the format string is not a string literal and there are no format arguments, as in <code>&quot;printf (foo);&quot;</code>. This may be a security hole if the format string came from untrusted input and contains <code>%n</code>. (This is currently a subset of what <code>-Wformat-nonliteral</code> warns about, but in future warnings may be added to <code>-Wformat-security</code> that are not included in <code>-Wformat-nonliteral</code>.) <br />
 </p>
 </dd>
<dt><code>-Wformat=2</code></dt>
<dd> <p> Enable <code>-Wformat</code> plus format checks not included in <code>-Wformat</code>. Currently equivalent to <code>-Wformat -Wformat-nonliteral -Wformat-security</code>. <br />
 </p>
 </dd>
<dt><code>-Wimplicit-int</code></dt>
<dd> <p> Warn when a declaration does not specify a type. <br />
 </p>
 </dd>
<dt><code>-Wimplicit-function-declaration</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-Werror-implicit-function-declaration</code></dt>
<dd> <p> Give a warning (or error) whenever a function is used before being declared. <br />
 </p>
 </dd>
<dt><code>-Wimplicit</code></dt>
<dd> <p> Same as <code>-Wimplicit-int</code> and <code>-Wimplicit-function-declaration</code>. <br />
 </p>
 </dd>
<dt><code>-Wmain</code></dt>
<dd> <p> Warn if the type of <code>main</code> is suspicious. <code>main</code> should be a function with external linkage, returning int, taking either zero arguments, two, or three arguments of appropriate types. <br />
 </p>
 </dd>
<dt><code>-Wmissing-braces</code></dt>
<dd> <p> Warn if an aggregate or union initializer is not fully bracketed. In the following example, the initializer for <code>a</code> is not fully bracketed, but that for <code>b</code> is fully bracketed. </p>
<pre><code>        int a[2][2] = { 0, 1, 2, 3 };
        int b[2][2] = { { 0, 1 }, { 2, 3 } };
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-Wparentheses</code></dt>
<dd> <p> Warn if parentheses are omitted in certain contexts, such as when there is an assignment in a context where a truth value is expected, or when operators are nested whose precedence people often get confused about. </p>
<p> Also warn about constructions where there may be confusion to which <code>&quot;if&quot;</code> statement an <code>&quot;else&quot;</code> branch belongs. Here is an example of such a case: </p>
<pre><code>        {
          if (a)
            if (b)
              foo ();
          else
            bar ();
        }
</code></pre>
<p> In C, every <code>&quot;else&quot;</code> branch belongs to the innermost possible <code>&quot;if&quot;</code> statement, which in this example is <code>&quot;if (b)&quot;</code>. This is often not what the programmer expected, as illustrated in the above example by indentation the programmer chose. When there is the potential for this confusion, <font SIZE="-1">GCC</font> will issue a warning when this flag is specified. To eliminate the warning, add explicit braces around the innermost <code>&quot;if&quot;</code> statement so there is no way the <code>&quot;else&quot;</code> could belong to the enclosing <code>&quot;if&quot;</code>. The resulting code would look like this: </p>
<pre><code>        {
          if (a)
            {
              if (b)
                foo ();
              else
                bar ();
            }
        }
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-Wsequence-point</code></dt>
<dd> <p> Warn about code that may have undefined semantics because of violations of sequence point rules in the C standard. </p>
<p> The C standard defines the order in which expressions in a C program are evaluated in terms of <i>sequence points</i>, which represent a partial ordering between the execution of parts of the program: those executed before the sequence point, and those executed after it. These occur after the evaluation of a full expression (one which is not part of a larger expression), after the evaluation of the first operand of a <code>&quot;&amp;&amp;&quot;</code>, <code>&quot;||&quot;</code>, <code>&quot;? :&quot;</code> or <code>&quot;,&quot;</code> (comma) operator, before a function is called (but after the evaluation of its arguments and the expression denoting the called function), and in certain other places. Other than as expressed by the sequence point rules, the order of evaluation of subexpressions of an expression is not specified. All these rules describe only a partial order rather than a total order, since, for example, if two functions are called within one expression with no sequence point between them, the order in which the functions are called is not specified. However, the standards committee have ruled that function calls do not overlap. </p>
<p> It is not specified when between sequence points modifications to the values of objects take effect. Programs whose behavior depends on this have undefined behavior; the C standard specifies that ``Between the previous and next sequence point an object shall have its stored value modified at most once by the evaluation of an expression. Furthermore, the prior value shall be read only to determine the value to be stored.&#8216;&#8216;. If a program breaks these rules, the results on any particular implementation are entirely unpredictable. </p>
<p> Examples of code with undefined behavior are <code>&quot;a = a++;&quot;</code>, <code>&quot;a[n] = b[n++]&quot;</code> and <code>&quot;a[i++] = i;&quot;</code>. Some more complicated cases are not diagnosed by this option, and it may give an occasional false positive result, but in general it has been found fairly effective at detecting this sort of problem in programs. </p>
<p> The present implementation of this option only works for C programs. A future implementation may also work for C<font SIZE="-2">++</font> programs. </p>
<p> The C standard is worded confusingly, therefore there is some debate over the precise meaning of the sequence point rules in subtle cases. Links to discussions of the problem, including proposed formal definitions, may be found on our readings page, at &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/readings.html">http://gcc.gnu.org/readings.html</a></code>&gt;. <br />
 </p>
 </dd>
<dt><code>-Wreturn-type</code></dt>
<dd> <p> Warn whenever a function is defined with a return-type that defaults to <code>&quot;int&quot;</code>. Also warn about any <code>&quot;return&quot;</code> statement with no return-value in a function whose return-type is not <code>&quot;void&quot;</code>. </p>
<p> For C<font SIZE="-2">++</font>, a function without return type always produces a diagnostic message, even when <code>-Wno-return-type</code> is specified. The only exceptions are <code>main</code> and functions defined in system headers. <br />
 </p>
 </dd>
<dt><code>-Wswitch</code></dt>
<dd> <p> Warn whenever a <code>&quot;switch&quot;</code> statement has an index of enumeral type and lacks a <code>&quot;case&quot;</code> for one or more of the named codes of that enumeration. (The presence of a <code>&quot;default&quot;</code> label prevents this warning.) <code>&quot;case&quot;</code> labels outside the enumeration range also provoke warnings when this option is used. <br />
 </p>
 </dd>
<dt><code>-Wtrigraphs</code></dt>
<dd> <p> Warn if any trigraphs are encountered that might change the meaning of the program (trigraphs within comments are not warned about). <br />
 </p>
 </dd>
<dt><code>-Wunused-function</code></dt>
<dd> <p> Warn whenever a static function is declared but not defined or a non\-inline static function is unused. <br />
 </p>
 </dd>
<dt><code>-Wunused-label</code></dt>
<dd> <p> Warn whenever a label is declared but not used. </p>
<p> To suppress this warning use the <code>unused</code> attribute. <br />
 </p>
 </dd>
<dt><code>-Wunused-parameter</code></dt>
<dd> <p> Warn whenever a function parameter is unused aside from its declaration. </p>
<p> To suppress this warning use the <code>unused</code> attribute. <br />
 </p>
 </dd>
<dt><code>-Wunused-variable</code></dt>
<dd> <p> Warn whenever a local variable or non-constant static variable is unused aside from its declaration </p>
<p> To suppress this warning use the <code>unused</code> attribute. <br />
 </p>
 </dd>
<dt><code>-Wunused-value</code></dt>
<dd> <p> Warn whenever a statement computes a result that is explicitly not used. </p>
<p> To suppress this warning cast the expression to <code>void</code>. <br />
 </p>
 </dd>
<dt><code>-Wunused</code></dt>
<dd> <p> All all the above <code>-Wunused</code> options combined. </p>
<p> In order to get a warning about an unused function parameter, you must either specify <code>-W -Wunused</code> or separately specify <code>-Wunused-parameter</code>. <br />
 </p>
 </dd>
<dt><code>-Wuninitialized</code></dt>
<dd> <p> Warn if an automatic variable is used without first being initialized or if a variable may be clobbered by a <code>&quot;setjmp&quot;</code> call. </p>
<p> These warnings are possible only in optimizing compilation, because they require data flow information that is computed only when optimizing. If you don&#8217;t specify <code>-O</code>, you simply won&#8217;t get these warnings. </p>
<p> These warnings occur only for variables that are candidates for register allocation. Therefore, they do not occur for a variable that is declared <code>&quot;volatile&quot;</code>, or whose address is taken, or whose size is other than 1, 2, 4 or 8 bytes. Also, they do not occur for structures, unions or arrays, even when they are in registers. </p>
<p> Note that there may be no warning about a variable that is used only to compute a value that itself is never used, because such computations may be deleted by data flow analysis before the warnings are printed. </p>
<p> These warnings are made optional because <font SIZE="-1">GCC</font> is not smart enough to see all the reasons why the code might be correct despite appearing to have an error. Here is one example of how this can happen: </p>
<pre><code>        {
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
        }
</code></pre>
<p> If the value of <code>&quot;y&quot;</code> is always 1, 2 or 3, then <code>&quot;x&quot;</code> is always initialized, but <font SIZE="-1">GCC</font> doesn&#8217;t know this. Here is another common case: </p>
<pre><code>        {
          int save_y;
          if (change_y) save_y = y, y = new_y;
          ...
          if (change_y) y = save_y;
        }
</code></pre>
<p> This has no bug because <code>&quot;save_y&quot;</code> is used only if it is set. </p>
<p> This option also warns when a non-volatile automatic variable might be changed by a call to <code>&quot;longjmp&quot;</code>. These warnings as well are possible only in optimizing compilation. </p>
<p> The compiler sees only the calls to <code>&quot;setjmp&quot;</code>. It cannot know where <code>&quot;longjmp&quot;</code> will be called; in fact, a signal handler could call it at any point in the code. As a result, you may get a warning even when there is in fact no problem because <code>&quot;longjmp&quot;</code> cannot in fact be called at the place which would cause a problem. </p>
<p> Some spurious warnings can be avoided if you declare all the functions you use that never return as <code>&quot;noreturn&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-Wreorder</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Warn when the order of member initializers given in the code does not match the order in which they must be executed. For instance: <br />
 </p>
 </dd>
<dt><code>-Wunknown-pragmas</code></dt>
<dd> <p> Warn when a #pragma directive is encountered which is not understood by <font SIZE="-1">GCC</font>. If this command line option is used, warnings will even be issued for unknown pragmas in system header files. This is not the case if the warnings were only enabled by the <code>-Wall</code> command line option. <br />
 </p>
 </dd>
<dt><code>-Wall</code></dt>
<dd> <p> All of the above <code>-W</code> options combined. This enables all the warnings about constructions that some users consider questionable, and that are easy to avoid (or modify to prevent the warning), even in conjunction with macros. <br />
 </p>
 </dd>
<dt><code>-Wdiv-by-zero</code></dt>
<dd> <p> Warn about compile-time integer division by zero. This is default. To inhibit the warning messages, use <code>-Wno-div-by-zero</code>. Floating point division by zero is not warned about, as it can be a legitimate way of obtaining infinities and NaNs. <br />
 </p>
 </dd>
<dt><code>-Wmultichar</code></dt>
<dd> <p> Warn if a multicharacter constant (<code>&#8216;</code><font SIZE="-1"><code>FOOF</code></font><code>&#8216;</code>) is used. This is default. To inhibit the warning messages, use <code>-Wno-multichar</code>. Usually they indicate a typo in the user&#8217;s code, as they have implementation-defined values, and should not be used in portable code. <br />
 </p>
 </dd>
<dt><code>-Wsystem-headers</code></dt>
<dd> <p> Print warning messages for constructs found in system header files. Warnings from system headers are normally suppressed, on the assumption that they usually do not indicate real problems and would only make the compiler output harder to read. Using this command line option tells <font SIZE="-1">GCC</font> to emit warnings from system headers as if they occurred in user code. However, note that using <code>-Wall</code> in conjunction with this option will <i>not</i> warn about unknown pragmas in system headers---for that, <code>-Wunknown-pragmas</code> must also be used. </p>
 </dd></dl>
<p> The following <code>-W...</code> options are not implied by <code>-Wall</code>. Some of them warn about constructions that users generally do not consider questionable, but which occasionally you might wish to check for; others warn about constructions that are necessary or hard to avoid in some cases, and there is no simple way to modify the code to suppress the warning. <br />
 </p>
<dl>
<dt><code>-W</code></dt>
<dd> <p> Print extra warning messages for these events: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>*</dt>
<dd> <p> A function can return either with or without a value. (Falling off the end of the function body is considered returning without a value.) For example, this function would evoke such a warning: </p>
<pre><code>        foo (a)
        {
          if (a &gt; 0)
            return a;
        }
</code></pre>
<p> <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> An expression-statement or the left-hand side of a comma expression contains no side effects. To suppress the warning, cast the unused expression to void. For example, an expression such as <code>x[i,j]</code> will cause a warning, but <code>x[(void)i,j]</code> will not. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> An unsigned value is compared against zero with <code>&lt;</code> or <code>&lt;=</code>. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> A comparison like <code>x&lt;=y&lt;=z</code> appears; this is equivalent to <code>(x&lt;=y ? 1 : 0) &lt;= z</code>, which is a different interpretation from that of ordinary mathematical notation. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Storage-class specifiers like <code>&quot;static&quot;</code> are not the first things in a declaration. According to the C Standard, this usage is obsolescent. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> The return type of a function has a type qualifier such as <code>&quot;const&quot;</code>. Such a type qualifier has no effect, since the value returned by a function is not an lvalue. (But don&#8217;t warn about the <font SIZE="-1">GNU</font> extension of <code>&quot;volatile void&quot;</code> return types. That extension will be warned about if <code>-pedantic</code> is specified.) <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> If <code>-Wall</code> or <code>-Wunused</code> is also specified, warn about unused arguments. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> A comparison between signed and unsigned values could produce an incorrect result when the signed value is converted to unsigned. (But don&#8217;t warn if <code>-Wno-sign-compare</code> is also specified.) <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> An aggregate has a partly bracketed initializer. For example, the following code would evoke such a warning, because braces are missing around the initializer for <code>&quot;x.h&quot;</code>: </p>
<pre><code>        struct s { int f, g; };
        struct t { struct s h; int i; };
        struct t x = { 1, 2, 3 };
</code></pre>
<p> <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> An aggregate has an initializer which does not initialize all members. For example, the following code would cause such a warning, because <code>&quot;x.h&quot;</code> would be implicitly initialized to zero: </p>
<pre><code>        struct s { int f, g, h; };
        struct s x = { 3, 4 };
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-Wfloat-equal</code></dt>
<dd> <p> Warn if floating point values are used in equality comparisons. </p>
<p> The idea behind this is that sometimes it is convenient (for the programmer) to consider floating-point values as approximations to infinitely precise real numbers. If you are doing this, then you need to compute (by analysing the code, or in some other way) the maximum or likely maximum error that the computation introduces, and allow for it when performing comparisons (and when producing output, but that&#8217;s a different problem). In particular, instead of testing for equality, you would check to see whether the two values have ranges that overlap; and this is done with the relational operators, so equality comparisons are probably mistaken. <br />
 </p>
 </dd>
<dt><code>-Wtraditional</code> (C only)</dt>
<dd> <p> Warn about certain constructs that behave differently in traditional and <font SIZE="-1">ISO</font> C. Also warn about <font SIZE="-1">ISO</font> C constructs that have no traditional C equivalent, and/or problematic constructs which should be avoided. </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>*</dt>
<dd> <p> Macro parameters that appear within string literals in the macro body. In traditional C macro replacement takes place within string literals, but does not in <font SIZE="-1">ISO</font> C. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> In traditional C, some preprocessor directives did not exist. Traditional preprocessors would only consider a line to be a directive if the <code>#</code> appeared in column 1 on the line. Therefore <code>-Wtraditional</code> warns about directives that traditional C understands but would ignore because the <code>#</code> does not appear as the first character on the line. It also suggests you hide directives like <code>#pragma</code> not understood by traditional C by indenting them. Some traditional implementations would not recognize <code>#elif</code>, so it suggests avoiding it altogether. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> A function-like macro that appears without arguments. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> The unary plus operator. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> The <code>U</code> integer constant suffix, or the <code>F</code> or <code>L</code> floating point constant suffixes. (Traditional C does support the <code>L</code> suffix on integer constants.) Note, these suffixes appear in macros defined in the system headers of most modern systems, e.g. the <code>_MIN</code>/<code>_MAX</code> macros in <code>&quot;&lt;<a href="file:/usr/include/limits.h">limits.h</a>&gt;&quot;</code>. Use of these macros in user code might normally lead to spurious warnings, however gcc&#8217;s integrated preprocessor has enough context to avoid warning in these cases. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> A function declared external in one block and then used after the end of the block. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> A <code>&quot;switch&quot;</code> statement has an operand of type <code>&quot;long&quot;</code>. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> A non-<code>&quot;static&quot;</code> function declaration follows a <code>&quot;static&quot;</code> one. This construct is not accepted by some traditional C compilers. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> The <font SIZE="-1">ISO</font> type of an integer constant has a different width or signedness from its traditional type. This warning is only issued if the base of the constant is ten. I.e. hexadecimal or octal values, which typically represent bit patterns, are not warned about. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Usage of <font SIZE="-1">ISO</font> string concatenation is detected. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Initialization of automatic aggregates. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Identifier conflicts with labels. Traditional C lacks a separate namespace for labels. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Initialization of unions. If the initializer is zero, the warning is omitted. This is done under the assumption that the zero initializer in user code appears conditioned on e.g. <code>&quot;__STDC__&quot;</code> to avoid missing initializer warnings and relies on default initialization to zero in the traditional C case. <br />
 </p>
 </dd>
<dt>*</dt>
<dd> <p> Conversions by prototypes between fixed/floating point values and vice versa. The absence of these prototypes when compiling with traditional C would cause serious problems. This is a subset of the possible conversion warnings, for the full set use <code>-Wconversion</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-Wundef</code></dt>
<dd> <p> Warn if an undefined identifier is evaluated in an <code>#if</code> directive. <br />
 </p>
 </dd>
<dt><code>-Wshadow</code></dt>
<dd> <p> Warn whenever a local variable shadows another local variable, parameter or global variable or whenever a built-in function is shadowed. <br />
 </p>
 </dd>
<dt><code>-Wlarger-than-</code><i>len</i></dt>
<dd> <p> Warn whenever an object of larger than <i>len</i> bytes is defined. <br />
 </p>
 </dd>
<dt><code>-Wpointer-arith</code></dt>
<dd> <p> Warn about anything that depends on the ``size of&#8217;&#8216; a function type or of <code>&quot;void&quot;</code>. <font SIZE="-1">GNU</font> C assigns these types a size of 1, for convenience in calculations with <code>&quot;void *&quot;</code> pointers and pointers to functions. <br />
 </p>
 </dd>
<dt><code>-Wbad-function-cast</code> (C only)</dt>
<dd> <p> Warn whenever a function call is cast to a non-matching type. For example, warn if <code>&quot;int malloc()&quot;</code> is cast to <code>&quot;anything *&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-Wcast-qual</code></dt>
<dd> <p> Warn whenever a pointer is cast so as to remove a type qualifier from the target type. For example, warn if a <code>&quot;const char *&quot;</code> is cast to an ordinary <code>&quot;char *&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-Wcast-align</code></dt>
<dd> <p> Warn whenever a pointer is cast such that the required alignment of the target is increased. For example, warn if a <code>&quot;char *&quot;</code> is cast to an <code>&quot;int *&quot;</code> on machines where integers can only be accessed at two- or four-byte boundaries. <br />
 </p>
 </dd>
<dt><code>-Wwrite-strings</code></dt>
<dd> <p> When compiling C, give string constants the type <code>&quot;const char[</code>length <code>]&quot;</code> so that copying the address of one into a non-<code>&quot;const&quot;</code> <code>&quot;char *&quot;</code> pointer will get a warning; when compiling C<font SIZE="-2">++</font>, warn about the deprecated conversion from string constants to <code>&quot;char *&quot;</code>. These warnings will help you find at compile time code that can try to write into a string constant, but only if you have been very careful about using <code>&quot;const&quot;</code> in declarations and prototypes. Otherwise, it will just be a nuisance; this is why we did not make <code>-Wall</code> request these warnings. <br />
 </p>
 </dd>
<dt><code>-Wconversion</code></dt>
<dd> <p> Warn if a prototype causes a type conversion that is different from what would happen to the same argument in the absence of a prototype. This includes conversions of fixed point to floating and vice versa, and conversions changing the width or signedness of a fixed point argument except when the same as the default promotion. </p>
<p> Also, warn if a negative integer constant expression is implicitly converted to an unsigned type. For example, warn about the assignment <code>&quot;x = -1&quot;</code> if <code>&quot;x&quot;</code> is unsigned. But do not warn about explicit casts like <code>&quot;(unsigned) -1&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-Wsign-compare</code></dt>
<dd> <p> Warn when a comparison between signed and unsigned values could produce an incorrect result when the signed value is converted to unsigned. This warning is also enabled by <code>-W</code>; to get the other warnings of <code>-W</code> without this warning, use <code>-W -Wno-sign-compare</code>. <br />
 </p>
 </dd>
<dt><code>-Waggregate-return</code></dt>
<dd> <p> Warn if any functions that return structures or unions are defined or called. (In languages where you can return an array, this also elicits a warning.) <br />
 </p>
 </dd>
<dt><code>-Wstrict-prototypes</code> (C only)</dt>
<dd> <p> Warn if a function is declared or defined without specifying the argument types. (An old-style function definition is permitted without a warning if preceded by a declaration which specifies the argument types.) <br />
 </p>
 </dd>
<dt><code>-Wmissing-prototypes</code> (C only)</dt>
<dd> <p> Warn if a global function is defined without a previous prototype declaration. This warning is issued even if the definition itself provides a prototype. The aim is to detect global functions that fail to be declared in header files. <br />
 </p>
 </dd>
<dt><code>-Wmissing-declarations</code></dt>
<dd> <p> Warn if a global function is defined without a previous declaration. Do so even if the definition itself provides a prototype. Use this option to detect global functions that are not declared in header files. <br />
 </p>
 </dd>
<dt><code>-Wmissing-noreturn</code></dt>
<dd> <p> Warn about functions which might be candidates for attribute <code>&quot;noreturn&quot;</code>. Note these are only possible candidates, not absolute ones. Care should be taken to manually verify functions actually do not ever return before adding the <code>&quot;noreturn&quot;</code> attribute, otherwise subtle code generation bugs could be introduced. You will not get a warning for <code>&quot;main&quot;</code> in hosted C environments. <br />
 </p>
 </dd>
<dt><code>-Wmissing-format-attribute</code></dt>
<dd> <p> If <code>-Wformat</code> is enabled, also warn about functions which might be candidates for <code>&quot;format&quot;</code> attributes. Note these are only possible candidates, not absolute ones. <font SIZE="-1">GCC</font> will guess that <code>&quot;format&quot;</code> attributes might be appropriate for any function that calls a function like <code>&quot;vprintf&quot;</code> or <code>&quot;vscanf&quot;</code>, but this might not always be the case, and some functions for which <code>&quot;format&quot;</code> attributes are appropriate may not be detected. This option has no effect unless <code>-Wformat</code> is enabled (possibly by <code>-Wall</code>). <br />
 </p>
 </dd>
<dt><code>-Wno-deprecated-declarations</code></dt>
<dd> <p> Do not warn about uses of functions, variables, and types marked as deprecated by using the <code>&quot;deprecated&quot;</code> attribute. (@pxref{Function Attributes}, <code>@pxref</code>{Variable Attributes}, <code>@pxref</code>{Type Attributes}.) <br />
 </p>
 </dd>
<dt><code>-Wpacked</code></dt>
<dd> <p> Warn if a structure is given the packed attribute, but the packed attribute has no effect on the layout or size of the structure. Such structures may be mis-aligned for little benefit. For instance, in this code, the variable <code>&quot;f.x&quot;</code> in <code>&quot;struct bar&quot;</code> will be misaligned even though <code>&quot;struct bar&quot;</code> does not itself have the packed attribute: </p>
<pre><code>        struct foo {
          int x;
          char a, b, c, d;
        } __attribute__((packed));
        struct bar {
          char z;
          struct foo f;
        };
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-Wpadded</code></dt>
<dd> <p> Warn if padding is included in a structure, either to align an element of the structure or to align the whole structure. Sometimes when this happens it is possible to rearrange the fields of the structure to reduce the padding and so make the structure smaller. <br />
 </p>
 </dd>
<dt><code>-Wredundant-decls</code></dt>
<dd> <p> Warn if anything is declared more than once in the same scope, even in cases where multiple declaration is valid and changes nothing. <br />
 </p>
 </dd>
<dt><code>-Wnested-externs</code> (C only)</dt>
<dd> <p> Warn if an <code>&quot;extern&quot;</code> declaration is encountered within a function. <br />
 </p>
 </dd>
<dt><code>-Wunreachable-code</code></dt>
<dd> <p> Warn if the compiler detects that code will never be executed. </p>
<p> This option is intended to warn when the compiler detects that at least a whole line of source code will never be executed, because some condition is never satisfied or because it is after a procedure that never returns. </p>
<p> It is possible for this option to produce a warning even though there are circumstances under which part of the affected line can be executed, so care should be taken when removing apparently-unreachable code. </p>
<p> For instance, when a function is inlined, a warning may mean that the line is unreachable in only one inlined copy of the function. </p>
<p> This option is not made part of <code>-Wall</code> because in a debugging version of a program there is often substantial code which checks correct functioning of the program and is, hopefully, unreachable because the program does work. Another common use of unreachable code is to provide behavior which is selectable at compile-time. <br />
 </p>
 </dd>
<dt><code>-Winline</code></dt>
<dd> <p> Warn if a function can not be inlined and it was declared as inline. <br />
 </p>
 </dd>
<dt><code>-Wlong-long</code></dt>
<dd> <p> Warn if <code>long long</code> type is used. This is default. To inhibit the warning messages, use <code>-Wno-long-long</code>. Flags <code>-Wlong-long</code> and <code>-Wno-long-long</code> are taken into account only when <code>-pedantic</code> flag is used. <br />
 </p>
 </dd>
<dt><code>-Wdisabled-optimization</code></dt>
<dd> <p> Warn if a requested optimization pass is disabled. This warning does not generally indicate that there is anything wrong with your code; it merely indicates that <font SIZE="-1">GCC</font>&#8216;s optimizers were unable to handle the code effectively. Often, the problem is that your code is too big or too complex; <font SIZE="-1">GCC</font> will refuse to optimize programs when the optimization itself is likely to take inordinate amounts of time. <br />
 </p>
 </dd>
<dt><code>-Werror</code></dt>
<dd> <p> Make all warnings into errors. </p>
 </dd></dl>
<font SIZE="-1"></font><h2>Options for Debugging Your Program or GCC</h2>
<p> <font SIZE="-1">GCC</font> has various special options that are used for debugging either your program or <font SIZE="-1">GCC:</font> <br />
 </p>
<dl>
<dt><code>-g</code></dt>
<dd> <p> Produce debugging information in the operating system&#8217;s native format (stabs, <font SIZE="-1">COFF</font>, <font SIZE="-1">XCOFF</font>, or <font SIZE="-1">DWARF</font>). <font SIZE="-1">GDB</font> can work with this debugging information. </p>
<p> On most systems that use stabs format, <code>-g</code> enables use of extra debugging information that only <font SIZE="-1">GDB</font> can use; this extra information makes debugging work better in <font SIZE="-1">GDB</font> but will probably make other debuggers crash or refuse to read the program. If you want to control for certain whether to generate the extra information, use <code>-gstabs+</code>, <code>-gstabs</code>, <code>-gxcoff+</code>, <code>-gxcoff</code>, <code>-gdwarf-1+</code>, <code>-gdwarf-1</code>, or <code>-gvms</code> (see below). </p>
<p> Unlike most other C compilers, <font SIZE="-1">GCC</font> allows you to use <code>-g</code> with <code>-O</code>. The shortcuts taken by optimized code may occasionally produce surprising results: some variables you declared may not exist at all; flow of control may briefly move where you did not expect it; some statements may not be executed because they compute constant results or their values were already at hand; some statements may execute in different places because they were moved out of loops. </p>
<p> Nevertheless it proves possible to debug optimized output. This makes it reasonable to use the optimizer for programs that might have bugs. </p>
<p> The following options are useful when <font SIZE="-1">GCC</font> is generated with the capability for more than one debugging format. <br />
 </p>
 </dd>
<dt><code>-ggdb</code></dt>
<dd> <p> Produce debugging information for use by <font SIZE="-1">GDB</font>. This means to use the most expressive format available (<font SIZE="-1">DWARF</font> 2, stabs, or the native format if neither of those are supported), including <font SIZE="-1">GDB</font> extensions if at all possible. <br />
 </p>
 </dd>
<dt><code>-gstabs</code></dt>
<dd> <p> Produce debugging information in stabs format (if that is supported), without <font SIZE="-1">GDB</font> extensions. This is the format used by <font SIZE="-1">DBX</font> on most <font SIZE="-1">BSD</font> systems. On <font SIZE="-1">MIPS</font>, Alpha and System V Release 4 systems this option produces stabs debugging output which is not understood by <font SIZE="-1">DBX</font> or <font SIZE="-1">SDB</font>. On System V Release 4 systems this option requires the <font SIZE="-1">GNU</font> assembler. <br />
 </p>
 </dd>
<dt><code>-gstabs+</code></dt>
<dd> <p> Produce debugging information in stabs format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program. <br />
 </p>
 </dd>
<dt><code>-gcoff</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">COFF</font> format (if that is supported). This is the format used by <font SIZE="-1">SDB</font> on most System V systems prior to System V Release 4. <br />
 </p>
 </dd>
<dt><code>-gxcoff</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">XCOFF</font> format (if that is supported). This is the format used by the <font SIZE="-1">DBX</font> debugger on <font SIZE="-1">IBM</font> <font SIZE="-1">RS/6000</font> systems. <br />
 </p>
 </dd>
<dt><code>-gxcoff+</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">XCOFF</font> format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program, and may cause assemblers other than the <font SIZE="-1">GNU</font> assembler (<font SIZE="-1">GAS</font>) to fail with an error. <br />
 </p>
 </dd>
<dt><code>-gdwarf</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">DWARF</font> version 1 format (if that is supported). This is the format used by <font SIZE="-1">SDB</font> on most System V Release 4 systems. <br />
 </p>
 </dd>
<dt><code>-gdwarf+</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">DWARF</font> version 1 format (if that is supported), using <font SIZE="-1">GNU</font> extensions understood only by the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>). The use of these extensions is likely to make other debuggers crash or refuse to read the program. <br />
 </p>
 </dd>
<dt><code>-gdwarf-2</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">DWARF</font> version 2 format (if that is supported). This is the format used by <font SIZE="-1">DBX</font> on <font SIZE="-1">IRIX</font> 6. <br />
 </p>
 </dd>
<dt><code>-gvms</code></dt>
<dd> <p> Produce debugging information in <font SIZE="-1">VMS</font> debug format (if that is supported). This is the format used by <font SIZE="-1">DEBUG</font> on <font SIZE="-1">VMS</font> systems. <br />
 </p>
 </dd>
<dt><code>-g</code><i>level</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-ggdb</code><i>level</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-gstabs</code><i>level</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-gcoff</code><i>level</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-gxcoff</code><i>level</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-gvms</code><i>level</i></dt>
<dd> <p> Request debugging information and also use <i>level</i> to specify how much information. The default level is 2. </p>
<p> Level 1 produces minimal information, enough for making backtraces in parts of the program that you don&#8217;t plan to debug. This includes descriptions of functions and external variables, but no information about local variables and no line numbers. </p>
<p> Level 3 includes extra information, such as all the macro definitions present in the program. Some debuggers support macro expansion when you use <code>-g3</code>. </p>
<p> Note that in order to avoid confusion between <font SIZE="-1">DWARF1</font> debug level 2, and <font SIZE="-1">DWARF2</font>, neither <code>-gdwarf</code> nor <code>-gdwarf-2</code> accept a concatenated debug level. Instead use an additional <code>-g</code><i>level</i> option to change the debug level for <font SIZE="-1">DWARF1</font> or <font SIZE="-1">DWARF2</font>. <br />
 </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Generate extra code to write profile information suitable for the analysis program <code>&quot;prof&quot;</code>. You must use this option when compiling the source files you want data about, and you must also use it when linking. <br />
 </p>
 </dd>
<dt><code>-pg</code></dt>
<dd> <p> Generate extra code to write profile information suitable for the analysis program <code>&quot;gprof&quot;</code>. You must use this option when compiling the source files you want data about, and you must also use it when linking. <br />
 </p>
 </dd>
<dt><code>-Q</code></dt>
<dd> <p> Makes the compiler print out each function name as it is compiled, and print some statistics about each pass when it finishes. <br />
 </p>
 </dd>
<dt><code>-ftime-report</code></dt>
<dd> <p> Makes the compiler print some statistics about the time consumed by each pass when it finishes. <br />
 </p>
 </dd>
<dt><code>-fmem-report</code></dt>
<dd> <p> Makes the compiler print some statistics about permanent memory allocation when it finishes. <br />
 </p>
 </dd>
<dt><code>-fprofile-arcs</code></dt>
<dd> <p> Instrument <i>arcs</i> during compilation to generate coverage data or for profile-directed block ordering. During execution the program records how many times each branch is executed and how many times it is taken. When the compiled program exits it saves this data to a file called <i>sourcename.da</i> for each source file. </p>
<p> For profile-directed block ordering, compile the program with <code>-fprofile-arcs</code> plus optimization and code generation options, generate the arc profile information by running the program on a selected workload, and then compile the program again with the same optimization and code generation options plus <code>-fbranch-probabilities</code>. </p>
<p> The other use of <code>-fprofile-arcs</code> is for use with <code>&quot;gcov&quot;</code>, when it is used with the <code>-ftest-coverage</code> option. </p>
<p> With <code>-fprofile-arcs</code>, for each function of your program <font SIZE="-1">GCC</font> creates a program flow graph, then finds a spanning tree for the graph. Only arcs that are not on the spanning tree have to be instrumented: the compiler adds code to count the number of times that these arcs are executed. When an arc is the only exit or only entrance to a block, the instrumentation code can be added to the block; otherwise, a new basic block must be created to hold the instrumentation code. <br />
 </p>
 </dd>
<dt><code>-ftest-coverage</code></dt>
<dd> <p> Create data files for the <code>gcov</code> code-coverage utility. The data file names begin with the name of your source file: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><i>sourcename</i><code>.bb</code></dt>
<dd> <p> A mapping from basic blocks to line numbers, which <code>&quot;gcov&quot;</code> uses to associate basic block execution counts with line numbers. <br />
 </p>
 </dd>
<dt><i>sourcename</i><code>.bbg</code></dt>
<dd> <p> A list of all arcs in the program flow graph. This allows <code>&quot;gcov&quot;</code> to reconstruct the program flow graph, so that it can compute all basic block and arc execution counts from the information in the <code>&quot;</code>sourcename <code>.da&quot;</code> file. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Use <code>-ftest-coverage</code> with <code>-fprofile-arcs</code>; the latter option adds instrumentation to the program, which then writes execution counts to another data file: </p>
 </dd>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dl>
<dt><i>sourcename</i><code>.da</code></dt>
<dd> <p> Runtime arc execution counts, used in conjunction with the arc information in the file <code>&quot;</code>sourcename <code>.bbg&quot;</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Coverage data will map better to the source files if <code>-ftest-coverage</code> is used without optimization. </p>
 </dd></dl>
<p> <br />
 </p>
<dt><code>-d</code><i>letters</i></dt>
<dd> <p> Says to make debugging dumps during compilation at times specified by <i>letters</i>. This is used for debugging the compiler. The file names for most of the dumps are made by appending a pass number and a word to the source file name (e.g. <i>foo.c.00.rtl</i> or <i>foo.c.01.sibling</i>). Here are the possible letters for use in <i>letters</i>, and their meanings: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>A</code></dt>
<dd> <p> Annotate the assembler output with miscellaneous debugging information. <br />
 </p>
 </dd>
<dt><code>b</code></dt>
<dd> <p> Dump after computing branch probabilities, to <i>file.14.bp</i>. <br />
 </p>
 </dd>
<dt><code>B</code></dt>
<dd> <p> Dump after block reordering, to <i>file.29.bbro</i>. <br />
 </p>
 </dd>
<dt><code>c</code></dt>
<dd> <p> Dump after instruction combination, to the file <i>file.16.combine</i>. <br />
 </p>
 </dd>
<dt><code>C</code></dt>
<dd> <p> Dump after the first if conversion, to the file <i>file.17.ce</i>. <br />
 </p>
 </dd>
<dt><code>d</code></dt>
<dd> <p> Dump after delayed branch scheduling, to <i>file.31.dbr</i>. <br />
 </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Dump all macro definitions, at the end of preprocessing, in addition to normal output. <br />
 </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Dump after <font SIZE="-1">SSA</font> optimizations, to <i>file.04.ssa</i> and <i>file.07.ussa</i>. <br />
 </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> Dump after the second if conversion, to <i>file.26.ce2</i>. <br />
 </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> Dump after life analysis, to <i>file.15.life</i>. <br />
 </p>
 </dd>
<dt><code>F</code></dt>
<dd> <p> Dump after purging <code>&quot;ADDRESSOF&quot;</code> codes, to <i>file.09.addressof</i>. <br />
 </p>
 </dd>
<dt><code>g</code></dt>
<dd> <p> Dump after global register allocation, to <i>file.21.greg</i>. <br />
 </p>
 </dd>
<dt><code>h</code></dt>
<dd> <p> Dump after finalization of <font SIZE="-1">EH</font> handling code, to <i>file.02.eh</i>. <br />
 </p>
 </dd>
<dt><code>k</code></dt>
<dd> <p> Dump after reg-to-stack conversion, to <i>file.28.stack</i>. <br />
 </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Dump after post-reload optimizations, to <i>file.22.postreload</i>. <br />
 </p>
 </dd>
<dt><code>G</code></dt>
<dd> <p> Dump after <font SIZE="-1">GCSE</font>, to <i>file.10.gcse</i>. <br />
 </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Dump after sibling call optimizations, to <i>file.01.sibling</i>. <br />
 </p>
 </dd>
<dt><code>j</code></dt>
<dd> <p> Dump after the first jump optimization, to <i>file.03.jump</i>. <br />
 </p>
 </dd>
<dt><code>k</code></dt>
<dd> <p> Dump after conversion from registers to stack, to <i>file.32.stack</i>. <br />
 </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> Dump after local register allocation, to <i>file.20.lreg</i>. <br />
 </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> Dump after loop optimization, to <i>file.11.loop</i>. <br />
 </p>
 </dd>
<dt><code>M</code></dt>
<dd> <p> Dump after performing the machine dependent reorganisation pass, to <i>file.30.mach</i>. <br />
 </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> Dump after register renumbering, to <i>file.25.rnreg</i>. <br />
 </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> Dump after the register move pass, to <i>file.18.regmove</i>. <br />
 </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Dump after <font SIZE="-1">RTL</font> generation, to <i>file.00.rtl</i>. <br />
 </p>
 </dd>
<dt><code>R</code></dt>
<dd> <p> Dump after the second scheduling pass, to <i>file.27.sched2</i>. <br />
 </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> Dump after <font SIZE="-1">CSE</font> (including the jump optimization that sometimes follows <font SIZE="-1">CSE</font>), to <i>file.08.cse</i>. <br />
 </p>
 </dd>
<dt><code>S</code></dt>
<dd> <p> Dump after the first scheduling pass, to <i>file.19.sched</i>. <br />
 </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> Dump after the second <font SIZE="-1">CSE</font> pass (including the jump optimization that sometimes follows <font SIZE="-1">CSE</font>), to <i>file.12.cse2</i>. <br />
 </p>
 </dd>
<dt><code>w</code></dt>
<dd> <p> Dump after the second flow pass, to <i>file.23.flow2</i>. <br />
 </p>
 </dd>
<dt><code>X</code></dt>
<dd> <p> Dump after <font SIZE="-1">SSA</font> dead code elimination, to <i>file.06.ssadce</i>. <br />
 </p>
 </dd>
<dt><code>z</code></dt>
<dd> <p> Dump after the peephole pass, to <i>file.24.peephole2</i>. <br />
 </p>
 </dd>
<dt><code>a</code></dt>
<dd> <p> Produce all the dumps listed above. <br />
 </p>
 </dd>
<dt><code>m</code></dt>
<dd> <p> Print statistics on memory usage, at the end of the run, to standard error. <br />
 </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Annotate the assembler output with a comment indicating which pattern and alternative was used. The length of each instruction is also printed. <br />
 </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> Dump the <font SIZE="-1">RTL</font> in the assembler output as a comment before each instruction. Also turns on <code>-dp</code> annotation. <br />
 </p>
 </dd>
<dt><code>v</code></dt>
<dd> <p> For each of the other indicated dump files (except for <i>file.00.rtl</i>), dump a representation of the control flow graph suitable for viewing with <font SIZE="-1">VCG</font> to <i>file.pass.vcg</i>. <br />
 </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> Just generate <font SIZE="-1">RTL</font> for a function instead of compiling it. Usually used with <code>r</code>. <br />
 </p>
 </dd>
<dt><code>y</code></dt>
<dd> <p> Dump debugging information during parsing, to standard error. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-fdump-unnumbered</code></dt>
<dd> <p> When doing debugging dumps (see <code>-d</code> option above), suppress instruction numbers and line number note output. This makes it more feasible to use diff on debugging dumps for compiler invocations with different options, in particular with and without <code>-g</code>. <br />
 </p>
 </dd>
<dt><code>-fdump-translation-unit</code> (C and C<font SIZE="-2">++</font> only)</dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fdump-translation-unit-</code><i>options</i>(C and C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Dump a representation of the tree structure for the entire translation unit to a file. The file name is made by appending <i>.tu</i> to the source file name. If the <code>-</code><i>options</i> form is used, <i>options</i> controls the details of the dump as described for the <code>-fdump-tree</code> options. <br />
 </p>
 </dd>
<dt><code>-fdump-class-hierarchy</code> (C<font SIZE="-2">++</font> only)</dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fdump-class-hierarchy-</code><i>options</i>(C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Dump a representation of each class&#8217;s hierarchy and virtual function table layout to a file. The file name is made by appending <i>.class</i> to the source file name. If the <code>-</code><i>options</i> form is used, <i>options</i> controls the details of the dump as described for the <code>-fdump-tree</code> options. <br />
 </p>
 </dd>
<dt><code>-fdump-tree-</code><i>switch</i>(C<font SIZE="-2">++</font> only)</dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fdump-tree-</code><i>switch</i><code>-</code><i>options</i>(C<font SIZE="-2">++</font> only)</dt>
<dd> <p> Control the dumping at various stages of processing the intermediate language tree to a file. The file name is generated by appending a switch specific suffix to the source file name. If the <code>-</code><i>options</i> form is used, <i>options</i> is a list of <code>-</code> separated options that control the details of the dump. Not all options are applicable to all dumps, those which are not meaningful will be ignored. The following options are available </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>address</code></dt>
<dd> <p> Print the address of each node. Usually this is not meaningful as it changes according to the environment and source file. Its primary use is for tying up a dump file with a debug environment. <br />
 </p>
 </dd>
<dt><code>slim</code></dt>
<dd> <p> Inhibit dumping of members of a scope or body of a function merely because that scope has been reached. Only dump such items when they are directly reachable by some other path. <br />
 </p>
 </dd>
<dt><code>all</code></dt>
<dd> <p> Turn on all options. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> The following tree dumps are possible: </p>
 </dd>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dl>
<dt><code>original</code></dt>
<dd> <p> Dump before any tree based optimization, to <i>file.original</i>. <br />
 </p>
 </dd>
<dt><code>optimized</code></dt>
<dd> <p> Dump after all tree based optimization, to <i>file.optimized</i>. <br />
 </p>
 </dd>
<dt><code>inlined</code></dt>
<dd> <p> Dump after function inlining, to <i>file.inlined</i>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-fsched-verbose=</code><i>n</i></dt>
<dd> <p> On targets that use instruction scheduling, this option controls the amount of debugging output the scheduler prints. This information is written to standard error, unless <code>-dS</code> or <code>-dR</code> is specified, in which case it is output to the usual dump listing file, <i>.sched</i> or <i>.sched2</i> respectively. However for <i>n</i> greater than nine, the output is always printed to standard error. </p>
<p> For <i>n</i> greater than zero, <code>-fsched-verbose</code> outputs the same information as <code>-dRS</code>. For <i>n</i> greater than one, it also output basic block probabilities, detailed ready list information and unit/insn info. For <i>n</i> greater than two, it includes <font SIZE="-1">RTL</font> at abort point, control-flow and regions info. And for <i>n</i> over four, <code>-fsched-verbose</code> also includes dependence info. <br />
 </p>
 </dd>
<dt><code>-fpretend-float</code></dt>
<dd> <p> When running a cross-compiler, pretend that the target machine uses the same floating point format as the host machine. This causes incorrect output of the actual floating constants, but the actual instruction sequence will probably be the same as <font SIZE="-1">GCC</font> would make when running on the target machine. <br />
 </p>
 </dd>
<dt><code>-save-temps</code></dt>
<dd> <p> Store the usual ``temporary&#8217;&#8216; intermediate files permanently; place them in the current directory and name them based on the source file. Thus, compiling <i>foo.c</i> with <code>-c -save-temps</code> would produce files <i>foo.i</i> and <i>foo.s</i>, as well as <i>foo.o</i>. This creates a preprocessed <i>foo.i</i> output file even though the compiler now normally uses an integrated preprocessor. <br />
 </p>
 </dd>
<dt><code>-time</code></dt>
<dd> <p> Report the <font SIZE="-1">CPU</font> time taken by each subprocess in the compilation sequence. For C source files, this is the compiler proper and assembler (plus the linker if linking is done). The output looks like this: </p>
<pre><code>        # cc1 0.12 0.01
        # as 0.00 0.01
</code></pre>
<p> The first number on each line is the ``user time,&#8216;&#8216; that is time spent executing the program itself. The second number is ``system time,&#8216;&#8216; time spent executing operating system routines on behalf of the program. Both numbers are in seconds. <br />
 </p>
 </dd>
<dt><code>-print-file-name=</code><i>library</i></dt>
<dd> <p> Print the full absolute name of the library file <i>library</i> that would be used when linking---and don&#8217;t do anything else. With this option, <font SIZE="-1">GCC</font> does not compile or link anything; it just prints the file name. <br />
 </p>
 </dd>
<dt><code>-print-multi-directory</code></dt>
<dd> <p> Print the directory name corresponding to the multilib selected by any other switches present in the command line. This directory is supposed to exist in <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. <br />
 </p>
 </dd>
<dt><code>-print-multi-lib</code></dt>
<dd> <p> Print the mapping from multilib directory names to compiler switches that enable them. The directory name is separated from the switches by <code>;</code>, and each switch starts with an <code>@} instead of the </code>@samp <code>{-</code>, without spaces between multiple switches. This is supposed to ease shell-processing. <br />
 </p>
 </dd>
<dt><code>-print-prog-name=</code><i>program</i></dt>
<dd> <p> Like <code>-print-file-name</code>, but searches for a program such as <code>cpp</code>. <br />
 </p>
 </dd>
<dt><code>-print-libgcc-file-name</code></dt>
<dd> <p> Same as <code>-print-file-name=libgcc.a</code>. </p>
<p> This is useful when you use <code>-nostdlib</code> or <code>-nodefaultlibs</code> but you do want to link with <i>libgcc.a</i>. You can do </p>
<pre><code>        gcc -nostdlib &lt;files&gt;... `gcc -print-libgcc-file-name`
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-print-search-dirs</code></dt>
<dd> <p> Print the name of the configured installation directory and a list of program and library directories gcc will search---and don&#8217;t do anything else. </p>
<p> This is useful when gcc prints the error message <code>installation problem, cannot exec cpp0: No such file or directory</code>. To resolve this you either need to put <i>cpp0</i> and the other compiler components where gcc expects to find them, or you can set the environment variable <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> to the directory where you installed them. Don&#8217;t forget the trailing &#8216;/&#8216;. <br />
 </p>
 </dd>
<dt><code>-dumpmachine</code></dt>
<dd> <p> Print the compiler&#8217;s target machine (for example, <code>i686-pc-linux-gnu</code>)---and don&#8217;t do anything else. <br />
 </p>
 </dd>
<dt><code>-dumpversion</code></dt>
<dd> <p> Print the compiler version (for example, <code>3.0</code>)---and don&#8217;t do anything else. <br />
 </p>
 </dd>
<dt><code>-dumpspecs</code></dt>
<dd> <p> Print the compiler&#8217;s built-in specs---and don&#8217;t do anything else. (This is used when <font SIZE="-1">GCC</font> itself is being built.) </p>
 </dd></dl>
<h2>Options That Control Optimization</h2>
<p> These options control various sorts of optimizations: <br />
 </p>
<dl>
<dt><code>-O</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-O1</code></dt>
<dd> <p> Optimize. Optimizing compilation takes somewhat more time, and a lot more memory for a large function. </p>
<p> Without <code>-O</code>, the compiler&#8217;s goal is to reduce the cost of compilation and to make debugging produce the expected results. Statements are independent: if you stop the program with a breakpoint between statements, you can then assign a new value to any variable or change the program counter to any other statement in the function and get exactly the results you would expect from the source code. </p>
<p> With <code>-O</code>, the compiler tries to reduce code size and execution time, without performing any optimizations that take a great deal of compilation time. <br />
 </p>
 </dd>
<dt><code>-O2</code></dt>
<dd> <p> Optimize even more. <font SIZE="-1">GCC</font> performs nearly all supported optimizations that do not involve a space-speed tradeoff. The compiler does not perform loop unrolling or function inlining when you specify <code>-O2</code>. As compared to <code>-O</code>, this option increases both compilation time and the performance of the generated code. </p>
<p> <code>-O2</code> turns on all optional optimizations except for loop unrolling, function inlining, and register renaming. It also turns on the <code>-fforce-mem</code> option on all machines and frame pointer elimination on machines where doing so does not interfere with debugging. </p>
<p> Please note the warning under <code>-fgcse</code> about invoking <code>-O2</code> on programs that use computed gotos. <br />
 </p>
 </dd>
<dt><code>-O3</code></dt>
<dd> <p> Optimize yet more. <code>-O3</code> turns on all optimizations specified by <code>-O2</code> and also turns on the <code>-finline-functions</code> and <code>-frename-registers</code> options. <br />
 </p>
 </dd>
<dt><code>-O0</code></dt>
<dd> <p> Do not optimize. <br />
 </p>
 </dd>
<dt><code>-Os</code></dt>
<dd> <p> Optimize for size. <code>-Os</code> enables all <code>-O2</code> optimizations that do not typically increase code size. It also performs further optimizations designed to reduce code size. </p>
<p> If you use multiple <code>-O</code> options, with or without level numbers, the last such option is the one that is effective. </p>
 </dd></dl>
<p> Options of the form <code>-f</code><i>flag</i> specify machine-independent flags. Most flags have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. In the table below, only one of the forms is listed---the one which is not the default. You can figure out the other form by either removing <code>no-</code> or adding it. <br />
 </p>
<dl>
<dt><code>-ffloat-store</code></dt>
<dd> <p> Do not store floating point variables in registers, and inhibit other options that might change whether a floating point value is taken from a register or memory. </p>
<p> This option prevents undesirable excess precision on machines such as the 68000 where the floating registers (of the 68881) keep more precision than a <code>&quot;double&quot;</code> is supposed to have. Similarly for the x86 architecture. For most programs, the excess precision does only good, but a few programs rely on the precise definition of <font SIZE="-1">IEEE</font> floating point. Use <code>-ffloat-store</code> for such programs, after modifying them to store all pertinent intermediate computations into variables. <br />
 </p>
 </dd>
<dt><code>-fno-default-inline</code></dt>
<dd> <p> Do not make member functions inline by default merely because they are defined inside the class scope (C<font SIZE="-2">++</font> only). Otherwise, when you specify <code>-O</code>, member functions defined inside class scope are compiled inline by default; i.e., you don&#8217;t need to add <code>inline</code> in front of the member function name. <br />
 </p>
 </dd>
<dt><code>-fno-defer-pop</code></dt>
<dd> <p> Always pop the arguments to each function call as soon as that function returns. For machines which must pop arguments after a function call, the compiler normally lets arguments accumulate on the stack for several function calls and pops them all at once. <br />
 </p>
 </dd>
<dt><code>-fforce-mem</code></dt>
<dd> <p> Force memory operands to be copied into registers before doing arithmetic on them. This produces better code by making all memory references potential common subexpressions. When they are not common subexpressions, instruction combination should eliminate the separate register-load. The <code>-O2</code> option turns on this option. <br />
 </p>
 </dd>
<dt><code>-fforce-addr</code></dt>
<dd> <p> Force memory address constants to be copied into registers before doing arithmetic on them. This may produce better code just as <code>-fforce-mem</code> may. <br />
 </p>
 </dd>
<dt><code>-fomit-frame-pointer</code></dt>
<dd> <p> Don&#8217;t keep the frame pointer in a register for functions that don&#8217;t need one. This avoids the instructions to save, set up and restore frame pointers; it also makes an extra register available in many functions. <code>It also makes debugging impossible on some machines.</code> </p>
<p> On some machines, such as the <font SIZE="-1">VAX</font>, this flag has no effect, because the standard calling sequence automatically handles the frame pointer and nothing is saved by pretending it doesn&#8217;t exist. The machine-description macro <code>&quot;FRAME_POINTER_REQUIRED&quot;</code> controls whether a target machine supports this flag. <br />
 </p>
 </dd>
<dt><code>-foptimize-sibling-calls</code></dt>
<dd> <p> Optimize sibling and tail recursive calls. <br />
 </p>
 </dd>
<dt><code>-ftrapv</code></dt>
<dd> <p> This option generates traps for signed overflow on addition, subtraction, multiplication operations. <br />
 </p>
 </dd>
<dt><code>-fno-inline</code></dt>
<dd> <p> Don&#8217;t pay attention to the <code>&quot;inline&quot;</code> keyword. Normally this option is used to keep the compiler from expanding any functions inline. Note that if you are not optimizing, no functions can be expanded inline. <br />
 </p>
 </dd>
<dt><code>-finline-functions</code></dt>
<dd> <p> Integrate all simple functions into their callers. The compiler heuristically decides which functions are simple enough to be worth integrating in this way. </p>
<p> If all calls to a given function are integrated, and the function is declared <code>&quot;static&quot;</code>, then the function is normally not output as assembler code in its own right. <br />
 </p>
 </dd>
<dt><code>-finline-limit=</code><i>n</i></dt>
<dd> <p> By default, gcc limits the size of functions that can be inlined. This flag allows the control of this limit for functions that are explicitly marked as inline (ie marked with the inline keyword or defined within the class definition in c++). <i>n</i> is the size of functions that can be inlined in number of pseudo instructions (not counting parameter handling). The default value of <i>n</i> is 600. Increasing this value can result in more inlined code at the cost of compilation time and memory consumption. Decreasing usually makes the compilation faster and less code will be inlined (which presumably means slower programs). This option is particularly useful for programs that use inlining heavily such as those based on recursive templates with C<font SIZE="-2">++</font>. </p>
<p> <i>Note:</i> pseudo instruction represents, in this particular context, an abstract measurement of function&#8217;s size. In no way, it represents a count of assembly instructions and as such its exact meaning might change from one release to an another. <br />
 </p>
 </dd>
<dt><code>-fkeep-inline-functions</code></dt>
<dd> <p> Even if all calls to a given function are integrated, and the function is declared <code>&quot;static&quot;</code>, nevertheless output a separate run-time callable version of the function. This switch does not affect <code>&quot;extern inline&quot;</code> functions. <br />
 </p>
 </dd>
<dt><code>-fkeep-static-consts</code></dt>
<dd> <p> Emit variables declared <code>&quot;static const&quot;</code> when optimization isn&#8217;t turned on, even if the variables aren&#8217;t referenced. </p>
<p> <font SIZE="-1">GCC</font> enables this option by default. If you want to force the compiler to check if the variable was referenced, regardless of whether or not optimization is turned on, use the <code>-fno-keep-static-consts</code> option. <br />
 </p>
 </dd>
<dt><code>-fmerge-constants</code></dt>
<dd> <p> Attempt to merge identical constants (string constants and floating point constants) accross compilation units. </p>
<p> This option is default for optimized compilation if assembler and linker support it. Use <code>-fno-merge-constants</code> to inhibit this behavior. <br />
 </p>
 </dd>
<dt><code>-fmerge-all-constants</code></dt>
<dd> <p> Attempt to merge identical constants and identical variables. </p>
<p> This option implies <code>-fmerge-constants</code>. In addition to <code>-fmerge-constants</code> this considers e.g. even constant initialized arrays or initialized constant variables with integral or floating point types. Languages like C or C<font SIZE="-2">++</font> require each non-automatic variable to have distinct location, so using this option will result in non-conforming behavior. <br />
 </p>
 </dd>
<dt><code>-fno-branch-count-reg</code></dt>
<dd> <p> Do not use ``decrement and branch&#8217;&#8216; instructions on a count register, but instead generate a sequence of instructions that decrement a register, compare it against zero, then branch based upon the result. This option is only meaningful on architectures that support such instructions, which include x86, PowerPC, <font SIZE="-1">IA-64</font> and S/390. <br />
 </p>
 </dd>
<dt><code>-fno-function-cse</code></dt>
<dd> <p> Do not put function addresses in registers; make each instruction that calls a constant function contain the function&#8217;s address explicitly. </p>
<p> This option results in less efficient code, but some strange hacks that alter the assembler output may be confused by the optimizations performed when this option is not used. <br />
 </p>
 </dd>
<dt><code>-ffast-math</code></dt>
<dd> <p> Sets <code>-fno-math-errno</code>, <code>-funsafe-math-optimizations</code>, and <code>-fno-trapping-math</code>. </p>
<p> This option causes the preprocessor macro <code>&quot;__FAST_MATH__&quot;</code> to be defined. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. <br />
 </p>
 </dd>
<dt><code>-fno-math-errno</code></dt>
<dd> <p> Do not set <font SIZE="-1">ERRNO</font> after calling math functions that are executed with a single instruction, e.g., sqrt. A program that relies on <font SIZE="-1">IEEE</font> exceptions for math error handling may want to use this flag for speed while maintaining <font SIZE="-1">IEEE</font> arithmetic compatibility. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-fmath-errno</code>. <br />
 </p>
 </dd>
<dt><code>-funsafe-math-optimizations</code></dt>
<dd> <p> Allow optimizations for floating-point arithmetic that (a) assume that arguments and results are valid and (b) may violate <font SIZE="-1">IEEE</font> or <font SIZE="-1">ANSI</font> standards. When used at link-time, it may include libraries or startup files that change the default <font SIZE="-1">FPU</font> control word or other similar optimizations. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-fno-unsafe-math-optimizations</code>. <br />
 </p>
 </dd>
<dt><code>-fno-trapping-math</code></dt>
<dd> <p> Compile code assuming that floating-point operations cannot generate user-visible traps. Setting this option may allow faster code if one relies on ``non-stop&#8217;&#8216; <font SIZE="-1">IEEE</font> arithmetic, for example. </p>
<p> This option should never be turned on by any <code>-O</code> option since it can result in incorrect output for programs which depend on an exact implementation of <font SIZE="-1">IEEE</font> or <font SIZE="-1">ISO</font> rules/specifications for math functions. </p>
<p> The default is <code>-ftrapping-math</code>. <br />
 </p>
 </dd>
<dt><code>-fbounds-check</code></dt>
<dd> <p> For front-ends that support it, generate additional code to check that indices used to access arrays are within the declared range. This is currenly only supported by the Java and Fortran 77 front-ends, where this option defaults to true and false respectively. </p>
 </dd></dl>
<p> The following options control specific optimizations. The <code>-O2</code> option turns on all of these optimizations except <code>-funroll-loops</code> and <code>-funroll-all-loops</code>. On most machines, the <code>-O</code> option turns on the <code>-fthread-jumps</code> and <code>-fdelayed-branch</code> options, but specific machines may handle it differently. </p>
<p> You can use the following flags in the rare cases when ``fine-tuning&#8217;&#8216; of optimizations to be performed is desired. </p>
<p> Not all of the optimizations performed by <font SIZE="-1">GCC</font> have <code>-f</code> options to control them. <br />
 </p>
<dl>
<dt><code>-fstrength-reduce</code></dt>
<dd> <p> Perform the optimizations of loop strength reduction and elimination of iteration variables. <br />
 </p>
 </dd>
<dt><code>-fthread-jumps</code></dt>
<dd> <p> Perform optimizations where we check to see if a jump branches to a location where another comparison subsumed by the first is found. If so, the first branch is redirected to either the destination of the second branch or a point immediately following it, depending on whether the condition is known to be true or false. <br />
 </p>
 </dd>
<dt><code>-fcse-follow-jumps</code></dt>
<dd> <p> In common subexpression elimination, scan through jump instructions when the target of the jump is not reached by any other path. For example, when <font SIZE="-1">CSE</font> encounters an <code>&quot;if&quot;</code> statement with an <code>&quot;else&quot;</code> clause, <font SIZE="-1">CSE</font> will follow the jump when the condition tested is false. <br />
 </p>
 </dd>
<dt><code>-fcse-skip-blocks</code></dt>
<dd> <p> This is similar to <code>-fcse-follow-jumps</code>, but causes <font SIZE="-1">CSE</font> to follow jumps which conditionally skip over blocks. When <font SIZE="-1">CSE</font> encounters a simple <code>&quot;if&quot;</code> statement with no else clause, <code>-fcse-skip-blocks</code> causes <font SIZE="-1">CSE</font> to follow the jump around the body of the <code>&quot;if&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-frerun-cse-after-loop</code></dt>
<dd> <p> Re-run common subexpression elimination after loop optimizations has been performed. <br />
 </p>
 </dd>
<dt><code>-frerun-loop-opt</code></dt>
<dd> <p> Run the loop optimizer twice. <br />
 </p>
 </dd>
<dt><code>-fgcse</code></dt>
<dd> <p> Perform a global common subexpression elimination pass. This pass also performs global constant and copy propagation. </p>
<p> <i>Note:</i> When compiling a program using computed gotos, a <font SIZE="-1">GCC</font> extension, you may get better runtime performance if you disable the global common subexpression elmination pass by adding <code>-fno-gcse</code> to the command line. <br />
 </p>
 </dd>
<dt><code>-fgcse-lm</code></dt>
<dd> <p> When <code>-fgcse-lm</code> is enabled, global common subexpression elimination will attempt to move loads which are only killed by stores into themselves. This allows a loop containing a load/store sequence to be changed to a load outside the loop, and a copy/store within the loop. <br />
 </p>
 </dd>
<dt><code>-fgcse-sm</code></dt>
<dd> <p> When <code>-fgcse-sm</code> is enabled, A store motion pass is run after global common subexpression elimination. This pass will attempt to move stores out of loops. When used in conjunction with <code>-fgcse-lm</code>, loops containing a load/store sequence can be changed to a load before the loop and a store after the loop. <br />
 </p>
 </dd>
<dt><code>-fdelete-null-pointer-checks</code></dt>
<dd> <p> Use global dataflow analysis to identify and eliminate useless checks for null pointers. The compiler assumes that dereferencing a null pointer would have halted the program. If a pointer is checked after it has already been dereferenced, it cannot be null. </p>
<p> In some environments, this assumption is not true, and programs can safely dereference null pointers. Use <code>-fno-delete-null-pointer-checks</code> to disable this optimization for programs which depend on that behavior. <br />
 </p>
 </dd>
<dt><code>-fexpensive-optimizations</code></dt>
<dd> <p> Perform a number of minor optimizations that are relatively expensive. <br />
 </p>
 </dd>
<dt><code>-foptimize-register-move</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fregmove</code></dt>
<dd> <p> Attempt to reassign register numbers in move instructions and as operands of other simple instructions in order to maximize the amount of register tying. This is especially helpful on machines with two-operand instructions. <font SIZE="-1">GCC</font> enables this optimization by default with <code>-O2</code> or higher. </p>
<p> Note <code>-fregmove</code> and <code>-foptimize-register-move</code> are the same optimization. <br />
 </p>
 </dd>
<dt><code>-fdelayed-branch</code></dt>
<dd> <p> If supported for the target machine, attempt to reorder instructions to exploit instruction slots available after delayed branch instructions. <br />
 </p>
 </dd>
<dt><code>-fschedule-insns</code></dt>
<dd> <p> If supported for the target machine, attempt to reorder instructions to eliminate execution stalls due to required data being unavailable. This helps machines that have slow floating point or memory load instructions by allowing other instructions to be issued until the result of the load or floating point instruction is required. <br />
 </p>
 </dd>
<dt><code>-fschedule-insns2</code></dt>
<dd> <p> Similar to <code>-fschedule-insns</code>, but requests an additional pass of instruction scheduling after register allocation has been done. This is especially useful on machines with a relatively small number of registers and where memory load instructions take more than one cycle. <br />
 </p>
 </dd>
<dt><code>-fno-sched-interblock</code></dt>
<dd> <p> Don&#8217;t schedule instructions across basic blocks. This is normally enabled by default when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher. <br />
 </p>
 </dd>
<dt><code>-fno-sched-spec</code></dt>
<dd> <p> Don&#8217;t allow speculative motion of non-load instructions. This is normally enabled by default when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher. <br />
 </p>
 </dd>
<dt><code>-fsched-spec-load</code></dt>
<dd> <p> Allow speculative motion of some load instructions. This only makes sense when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher. <br />
 </p>
 </dd>
<dt><code>-fsched-spec-load-dangerous</code></dt>
<dd> <p> Allow speculative motion of more load instructions. This only makes sense when scheduling before register allocation, i.e. with <code>-fschedule-insns</code> or at <code>-O2</code> or higher. <br />
 </p>
 </dd>
<dt><code>-ffunction-sections</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fdata-sections</code></dt>
<dd> <p> Place each function or data item into its own section in the output file if the target supports arbitrary sections. The name of the function or the name of the data item determines the section&#8217;s name in the output file. </p>
<p> Use these options on systems where the linker can perform optimizations to improve locality of reference in the instruction space. <font SIZE="-1">HPPA</font> processors running <font SIZE="-1">HP-UX</font> and Sparc processors running Solaris 2 have linkers with such optimizations. Other systems using the <font SIZE="-1">ELF</font> object format as well as <font SIZE="-1">AIX</font> may have these optimizations in the future. </p>
<p> Only use these options when there are significant benefits from doing so. When you specify these options, the assembler and linker will create larger object and executable files and will also be slower. You will not be able to use <code>&quot;gprof&quot;</code> on all systems if you specify this option and you may have problems with debugging if you specify both this option and <code>-g</code>. <br />
 </p>
 </dd>
<dt><code>-fcaller-saves</code></dt>
<dd> <p> Enable values to be allocated in registers that will be clobbered by function calls, by emitting extra instructions to save and restore the registers around such calls. Such allocation is done only when it seems to result in better code than would otherwise be produced. </p>
<p> This option is always enabled by default on certain machines, usually those which have no call-preserved registers to use instead. </p>
<p> For all machines, optimization level 2 and higher enables this flag by default. <br />
 </p>
 </dd>
<dt><code>-funroll-loops</code></dt>
<dd> <p> Unroll loops whose number of iterations can be determined at compile time or upon entry to the loop. <code>-funroll-loops</code> implies both <code>-fstrength-reduce</code> and <code>-frerun-cse-after-loop</code>. This option makes code larger, and may or may not make it run faster. <br />
 </p>
 </dd>
<dt><code>-funroll-all-loops</code></dt>
<dd> <p> Unroll all loops, even if their number of iterations is uncertain when the loop is entered. This usually makes programs run more slowly. <code>-funroll-all-loops</code> implies the same options as <code>-funroll-loops</code>, <br />
 </p>
 </dd>
<dt><code>-fprefetch-loop-arrays</code></dt>
<dd> <p> If supported by the target machine, generate instructions to prefetch memory to improve the performance of loops that access large arrays. <br />
 </p>
 </dd>
<dt><code>-fmove-all-movables</code></dt>
<dd> <p> Forces all invariant computations in loops to be moved outside the loop. <br />
 </p>
 </dd>
<dt><code>-freduce-all-givs</code></dt>
<dd> <p> Forces all general-induction variables in loops to be strength-reduced. </p>
<p> <i>Note:</i> When compiling programs written in Fortran, <code>-fmove-all-movables</code> and <code>-freduce-all-givs</code> are enabled by default when you use the optimizer. </p>
<p> These options may generate better or worse code; results are highly dependent on the structure of loops within the source code. </p>
<p> These two options are intended to be removed someday, once they have helped determine the efficacy of various approaches to improving loop optimizations. </p>
<p> Please let us (&lt;<code>gcc [at] gcc.gnu.org</code>&gt; and &lt;<code>fortran [at] gnu.org</code>&gt;) know how use of these options affects the performance of your production code. We&#8217;re very interested in code that runs <i>slower</i> when these options are <i>enabled</i>. <br />
 </p>
 </dd>
<dt><code>-fno-peephole</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fno-peephole2</code></dt>
<dd> <p> Disable any machine-specific peephole optimizations. The difference between <code>-fno-peephole</code> and <code>-fno-peephole2</code> is in how they are implemented in the compiler; some targets use one, some use the other, a few use both. <br />
 </p>
 </dd>
<dt><code>-fbranch-probabilities</code></dt>
<dd> <p> After running a program compiled with <code>-fprofile-arcs</code>, you can compile it a second time using <code>-fbranch-probabilities</code>, to improve optimizations based on the number of times each branch was taken. When the program compiled with <code>-fprofile-arcs</code> exits it saves arc execution counts to a file called <i>sourcename.da</i> for each source file The information in this data file is very dependent on the structure of the generated code, so you must use the same source code and the same optimization options for both compilations. </p>
<p> With <code>-fbranch-probabilities</code>, <font SIZE="-1">GCC</font> puts a <font SIZE="-1"><code>REG_EXEC_COUNT</code></font> note on the first instruction of each basic block, and a <font SIZE="-1"><code>REG_BR_PROB</code></font> note on each <font SIZE="-1"><code>JUMP_INSN</code></font> and <font SIZE="-1"><code>CALL_INSN</code></font>. These can be used to improve optimization. Currently, they are only used in one place: in <i>reorg.c</i>, instead of guessing which path a branch is mostly to take, the <font SIZE="-1"><code>REG_BR_PROB</code></font> values are used to exactly determine which path is taken more often. <br />
 </p>
 </dd>
<dt><code>-fno-guess-branch-probability</code></dt>
<dd> <p> Do not guess branch probabilities using a randomized model. </p>
<p> Sometimes gcc will opt to use a randomized model to guess branch probabilities, when none are available from either profiling feedback (<code>-fprofile-arcs</code>) or <code>__builtin_expect</code>. This means that different runs of the compiler on the same program may produce different object code. </p>
<p> In a hard real-time system, people don&#8217;t want different runs of the compiler to produce code that has different behavior; minimizing non-determinism is of paramount import. This switch allows users to reduce non-determinism, possibly at the expense of inferior optimization. <br />
 </p>
 </dd>
<dt><code>-fstrict-aliasing</code></dt>
<dd> <p> Allows the compiler to assume the strictest aliasing rules applicable to the language being compiled. For C (and C<font SIZE="-2">++</font>), this activates optimizations based on the type of expressions. In particular, an object of one type is assumed never to reside at the same address as an object of a different type, unless the types are almost the same. For example, an <code>&quot;unsigned int&quot;</code> can alias an <code>&quot;int&quot;</code>, but not a <code>&quot;void*&quot;</code> or a <code>&quot;double&quot;</code>. A character type may alias any other type. </p>
<p> Pay special attention to code like this: </p>
<pre><code>        union a_union {
          int i;
          double d;
        };
</code></pre>
<pre><code>        int f() {
          a_union t;
          t.d = 3.0;
          return t.i;
        }
</code></pre>
<p> The practice of reading from a different union member than the one most recently written to (called ``type-punning&#8217;&#8216;) is common. Even with <code>-fstrict-aliasing</code>, type-punning is allowed, provided the memory is accessed through the union type. So, the code above will work as expected. However, this code might not: </p>
<pre><code>        int f() {
          a_union t;
          int* ip;
          t.d = 3.0;
          ip = &amp;t.i;
          return *ip;
        }
</code></pre>
<p> Every language that wishes to perform language-specific alias analysis should define a function that computes, given an <code>&quot;tree&quot;</code> node, an alias set for the node. Nodes in different alias sets are not allowed to alias. For an example, see the C front-end function <code>&quot;c_get_alias_set&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-falign-functions</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-falign-functions=</code><i>n</i></dt>
<dd> <p> Align the start of functions to the next power-of-two greater than <i>n</i>, skipping up to <i>n</i> bytes. For instance, <code>-falign-functions=32</code> aligns functions to the next 32-byte boundary, but <code>-falign-functions=24</code> would align to the next 32-byte boundary only if this can be done by skipping 23 bytes or less. </p>
<p> <code>-fno-align-functions</code> and <code>-falign-functions=1</code> are equivalent and mean that functions will not be aligned. </p>
<p> Some assemblers only support this flag when <i>n</i> is a power of two; in that case, it is rounded up. </p>
<p> If <i>n</i> is not specified, use a machine-dependent default. <br />
 </p>
 </dd>
<dt><code>-falign-labels</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-falign-labels=</code><i>n</i></dt>
<dd> <p> Align all branch targets to a power-of-two boundary, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. This option can easily make code slower, because it must insert dummy operations for when the branch target is reached in the usual flow of the code. </p>
<p> If <code>-falign-loops</code> or <code>-falign-jumps</code> are applicable and are greater than this value, then their values are used instead. </p>
<p> If <i>n</i> is not specified, use a machine-dependent default which is very likely to be <code>1</code>, meaning no alignment. <br />
 </p>
 </dd>
<dt><code>-falign-loops</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-falign-loops=</code><i>n</i></dt>
<dd> <p> Align loops to a power-of-two boundary, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. The hope is that the loop will be executed many times, which will make up for any execution of the dummy operations. </p>
<p> If <i>n</i> is not specified, use a machine-dependent default. <br />
 </p>
 </dd>
<dt><code>-falign-jumps</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-falign-jumps=</code><i>n</i></dt>
<dd> <p> Align branch targets to a power-of-two boundary, for branch targets where the targets can only be reached by jumping, skipping up to <i>n</i> bytes like <code>-falign-functions</code>. In this case, no dummy operations need be executed. </p>
<p> If <i>n</i> is not specified, use a machine-dependent default. <br />
 </p>
 </dd>
<dt><code>-fssa</code></dt>
<dd> <p> Perform optimizations in static single assignment form. Each function&#8217;s flow graph is translated into <font SIZE="-1">SSA</font> form, optimizations are performed, and the flow graph is translated back from <font SIZE="-1">SSA</font> form. Users should not specify this option, since it is not yet ready for production use. <br />
 </p>
 </dd>
<dt><code>-fssa-ccp</code></dt>
<dd> <p> Perform Sparse Conditional Constant Propagation in <font SIZE="-1">SSA</font> form. Requires <code>-fssa</code>. Like <code>-fssa</code>, this is an experimental feature. <br />
 </p>
 </dd>
<dt><code>-fssa-dce</code></dt>
<dd> <p> Perform aggressive dead-code elimination in <font SIZE="-1">SSA</font> form. Requires <code>-fssa</code>. Like <code>-fssa</code>, this is an experimental feature. <br />
 </p>
 </dd>
<dt><code>-fsingle-precision-constant</code></dt>
<dd> <p> Treat floating point constant as single precision constant instead of implicitly converting it to double precision constant. <br />
 </p>
 </dd>
<dt><code>-frename-registers</code></dt>
<dd> <p> Attempt to avoid false dependencies in scheduled code by making use of registers left over after register allocation. This optimization will most benefit processors with lots of registers. It can, however, make debugging impossible, since variables will no longer stay in a ``home register&#8217;&#8216;. <br />
 </p>
 </dd>
<dt><code>-fno-cprop-registers</code></dt>
<dd> <p> After register allocation and post-register allocation instruction splitting, we perform a copy-propagation pass to try to reduce scheduling dependencies and occasionally eliminate the copy. <br />
 </p>
 </dd>
<dt><code>---param</code><i>name</i><code>=</code><i>value</i></dt>
<dd> <p> In some places, <font SIZE="-1">GCC</font> uses various constants to control the amount of optimization that is done. For example, <font SIZE="-1">GCC</font> will not inline functions that contain more that a certain number of instructions. You can control some of these constants on the command-line using the <code>---param</code> option. </p>
<p> In each case, the <i>value</i> is an integer. The allowable choices for <i>name</i> are given in the following table: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>max-delay-slot-insn-search</code></dt>
<dd> <p> The maximum number of instructions to consider when looking for an instruction to fill a delay slot. If more than this arbitrary number of instructions is searched, the time savings from filling the delay slot will be minimal so stop searching. Increasing values mean more aggressive optimization, making the compile time increase with probably small improvement in executable run time. <br />
 </p>
 </dd>
<dt><code>max-delay-slot-live-search</code></dt>
<dd> <p> When trying to fill delay slots, the maximum number of instructions to consider when searching for a block with valid live register information. Increasing this arbitrarily chosen value means more aggressive optimization, increasing the compile time. This parameter should be removed when the delay slot code is rewritten to maintain the control-flow graph. <br />
 </p>
 </dd>
<dt><code>max-gcse-memory</code></dt>
<dd> <p> The approximate maximum amount of memory that will be allocated in order to perform the global common subexpression elimination optimization. If more memory than specified is required, the optimization will not be done. <br />
 </p>
 </dd>
<dt><code>max-gcse-passes</code></dt>
<dd> <p> The maximum number of passes of <font SIZE="-1">GCSE</font> to run. <br />
 </p>
 </dd>
<dt><code>max-pending-list-length</code></dt>
<dd> <p> The maximum number of pending dependencies scheduling will allow before flushing the current state and starting over. Large functions with few branches or calls can create excessively large lists which needlessly consume memory and resources. <br />
 </p>
 </dd>
<dt><code>max-inline-insns</code></dt>
<dd> <p> If an function contains more than this many instructions, it will not be inlined. This option is precisely equivalent to <code>-finline-limit</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Options Controlling the Preprocessor</h2>
<p> These options control the C preprocessor, which is run on each C source file before actual compilation. </p>
<p> If you use the <code>-E</code> option, nothing is done except preprocessing. Some of these options make sense only together with <code>-E</code> because they cause the preprocessor output to be unsuitable for actual compilation. </p>
<p> You can use <code>-Wp,</code><i>option</i> to bypass the compiler driver and pass <i>option</i> directly through to the preprocessor. If <i>option</i> contains commas, it is split into multiple options at the commas. However, many options are modified, translated or interpreted by the compiler driver before being passed to the preprocessor, and <code>-Wp</code> forcibly bypasses this phase. The preprocessor&#8217;s direct interface is undocumented and subject to change, so whenever possible you should avoid using <code>-Wp</code> and let the driver handle the options instead. <br />
 </p>
<dl>
<dt><code>-D</code><i>name</i></dt>
<dd> <p> Predefine <i>name</i> as a macro, with definition <code>&quot;1&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-D</code><i>name</i><code>=</code><i>definition</i></dt>
<dd> <p> Predefine <i>name</i> as a macro, with definition <i>definition</i>. There are no restrictions on the contents of <i>definition</i>, but if you are invoking the preprocessor from a shell or shell-like program you may need to use the shell&#8217;s quoting syntax to protect characters such as spaces that have a meaning in the shell syntax. </p>
<p> If you wish to define a function-like macro on the command line, write its argument list with surrounding parentheses before the equals sign (if any). Parentheses are meaningful to most shells, so you will need to quote the option. With <code>sh</code> and <code>csh</code>, <code>-D&#8217;</code><i>name</i><code>(</code><i>args...</i><code>)=</code><i>definition</i><code>&#8216;</code> works. </p>
<p> <code>-D</code> and <code>-U</code> options are processed in the order they are given on the command line. All <code>-imacros</code> <i>file</i> and <code>-include</code> <i>file</i> options are processed after all <code>-D</code> and <code>-U</code> options. <br />
 </p>
 </dd>
<dt><code>-U</code><i>name</i></dt>
<dd> <p> Cancel any previous definition of <i>name</i>, either built in or provided with a <code>-D</code> option. <br />
 </p>
 </dd>
<dt><code>-undef</code></dt>
<dd> <p> Do not predefine any system-specific macros. The common predefined macros remain defined. <br />
 </p>
 </dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> <p> Add the directory <i>dir</i> to the list of directories to be searched for header files. Directories named by <code>-I</code> are searched before the standard system include directories. </p>
<p> It is dangerous to specify a standard system include directory in an <code>-I</code> option. This defeats the special treatment of system headers . It can also defeat the repairs to buggy system headers which <font SIZE="-1">GCC</font> makes when it is installed. <br />
 </p>
 </dd>
<dt><code>-o</code><i>file</i></dt>
<dd> <p> Write output to <i>file</i>. This is the same as specifying <i>file</i> as the second non-option argument to <code>cpp</code>. <code>gcc</code> has a different interpretation of a second non-option argument, so you must use <code>-o</code> to specify the output file. <br />
 </p>
 </dd>
<dt><code>-Wall</code></dt>
<dd> <p> Turns on all optional warnings which are desirable for normal code. At present this is <code>-Wcomment</code> and <code>-Wtrigraphs</code>. Note that many of the preprocessor&#8217;s warnings are on by default and have no options to control them. <br />
 </p>
 </dd>
<dt><code>-Wcomment</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-Wcomments</code></dt>
<dd> <p> Warn whenever a comment-start sequence <code>/*</code> appears in a <code>/*</code> comment, or whenever a backslash-newline appears in a <code>//</code> comment. (Both forms have the same effect.) <br />
 </p>
 </dd>
<dt><code>-Wtrigraphs</code></dt>
<dd> <p> Warn if any trigraphs are encountered. This option used to take effect only if <code>-trigraphs</code> was also specified, but now works independently. Warnings are not given for trigraphs within comments, as they do not affect the meaning of the program. <br />
 </p>
 </dd>
<dt><code>-Wtraditional</code></dt>
<dd> <p> Warn about certain constructs that behave differently in traditional and <font SIZE="-1">ISO</font> C. Also warn about <font SIZE="-1">ISO</font> C constructs that have no traditional C equivalent, and problematic constructs which should be avoided. <br />
 </p>
 </dd>
<dt><code>-Wimport</code></dt>
<dd> <p> Warn the first time <code>#import</code> is used. <br />
 </p>
 </dd>
<dt><code>-Wundef</code></dt>
<dd> <p> Warn whenever an identifier which is not a macro is encountered in an <code>#if</code> directive, outside of <code>defined</code>. Such identifiers are replaced with zero. <br />
 </p>
 </dd>
<dt><code>-Werror</code></dt>
<dd> <p> Make all warnings into hard errors. Source code which triggers warnings will be rejected. <br />
 </p>
 </dd>
<dt><code>-Wsystem-headers</code></dt>
<dd> <p> Issue warnings for code in system headers. These are normally unhelpful in finding bugs in your own code, therefore suppressed. If you are responsible for the system library, you may want to see them. <br />
 </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Suppress all warnings, including those which <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font> issues by default. <br />
 </p>
 </dd>
<dt><code>-pedantic</code></dt>
<dd> <p> Issue all the mandatory diagnostics listed in the C standard. Some of them are left out by default, since they trigger frequently on harmless code. <br />
 </p>
 </dd>
<dt><code>-pedantic-errors</code></dt>
<dd> <p> Issue all the mandatory diagnostics, and make all mandatory diagnostics into errors. This includes mandatory diagnostics that <font SIZE="-1">GCC</font> issues without <code>-pedantic</code> but treats as warnings. <br />
 </p>
 </dd>
<dt><code>-M</code></dt>
<dd> <p> Instead of outputting the result of preprocessing, output a rule suitable for <code>make</code> describing the dependencies of the main source file. The preprocessor outputs one <code>make</code> rule containing the object file name for that source file, a colon, and the names of all the included files, including those coming from <code>-include</code> or <code>-imacros</code> command line options. </p>
<p> Unless specified explicitly (with <code>-MT</code> or <code>-MQ</code>), the object file name consists of the basename of the source file with any suffix replaced with object file suffix. If there are many included files then the rule is split into several lines using <code>\</code>-newline. The rule has no commands. </p>
<p> This option does not suppress the preprocessor&#8217;s debug output, such as <code>-dM</code>. To avoid mixing such debug output with the dependency rules you should explicitly specify the dependency output file with <code>-MF</code>, or use an environment variable like <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font>. Debug output will still be sent to the regular output stream as normal. </p>
<p> Passing <code>-M</code> to the driver implies <code>-E</code>. <br />
 </p>
 </dd>
<dt><code>-MM</code></dt>
<dd> <p> Like <code>-M</code> but do not mention header files that are found in system header directories, nor header files that are included, directly or indirectly, from such a header. </p>
<p> This implies that the choice of angle brackets or double quotes in an <code>#include</code> directive does not in itself determine whether that header will appear in <code>-MM</code> dependency output. This is a slight change in semantics from <font SIZE="-1">GCC</font> versions 3.0 and earlier. <br />
 </p>
 </dd>
<dt><code>-MF</code><i>file</i></dt>
<dd> <p> @anchor{-MF} When used with <code>-M</code> or <code>-MM</code>, specifies a file to write the dependencies to. If no <code>-MF</code> switch is given the preprocessor sends the rules to the same place it would have sent preprocessed output. </p>
<p> When used with the driver options <code>-MD</code> or <code>-MMD</code>, <code>-MF</code> overrides the default dependency output file. <br />
 </p>
 </dd>
<dt><code>-MG</code></dt>
<dd> <p> When used with <code>-M</code> or <code>-MM</code>, <code>-MG</code> says to treat missing header files as generated files and assume they live in the same directory as the source file. It suppresses preprocessed output, as a missing header file is ordinarily an error. </p>
<p> This feature is used in automatic updating of makefiles. <br />
 </p>
 </dd>
<dt><code>-MP</code></dt>
<dd> <p> This option instructs <font SIZE="-1">CPP</font> to add a phony target for each dependency other than the main file, causing each to depend on nothing. These dummy rules work around errors <code>make</code> gives if you remove header files without updating the <i>Makefile</i> to match. </p>
<p> This is typical output: </p>
<pre><code>        test.o: test.c test.h
</code></pre>
<pre><code>        test.h:
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-MT</code><i>target</i></dt>
<dd> <p> Change the target of the rule emitted by dependency generation. By default <font SIZE="-1">CPP</font> takes the name of the main input file, including any path, deletes any file suffix such as <code>.c</code>, and appends the platform&#8217;s usual object suffix. The result is the target. </p>
<p> An <code>-MT</code> option will set the target to be exactly the string you specify. If you want multiple targets, you can specify them as a single argument to <code>-MT</code>, or use multiple <code>-MT</code> options. </p>
<p> For example, <code>-MT&nbsp;<wbr>&#8216;$(objpfx)foo.o&#8217;</code> might give </p>
<pre><code>        $(objpfx)foo.o: foo.c
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-MQ</code><i>target</i></dt>
<dd> <p> Same as <code>-MT</code>, but it quotes any characters which are special to Make. <code>-MQ&nbsp;<wbr>&#8216;$(objpfx)foo.o&#8217;</code> gives </p>
<pre><code>        $$(objpfx)foo.o: foo.c
</code></pre>
<p> The default target is automatically quoted, as if it were given with <code>-MQ</code>. <br />
 </p>
 </dd>
<dt><code>-MD</code></dt>
<dd> <p> <code>-MD</code> is equivalent to <code>-M -MF</code> <i>file</i>, except that <code>-E</code> is not implied. The driver determines <i>file</i> based on whether an <code>-o</code> option is given. If it is, the driver uses its argument but with a suffix of <i>.d</i>, otherwise it take the basename of the input file and applies a <i>.d</i> suffix. </p>
<p> If <code>-MD</code> is used in conjunction with <code>-E</code>, any <code>-o</code> switch is understood to specify the dependency output file (but <code>@pxref</code>{-MF}), but if used without <code>-E</code>, each <code>-o</code> is understood to specify a target object file. </p>
<p> Since <code>-E</code> is not implied, <code>-MD</code> can be used to generate a dependency output file as a side-effect of the compilation process. <br />
 </p>
 </dd>
<dt><code>-MMD</code></dt>
<dd> <p> Like <code>-MD</code> except mention only user header files, not system -header files. <br />
 </p>
 </dd>
<dt><code>-x c</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-x c++</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-x objective-c</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-x assembler-with-cpp</code></dt>
<dd> <p> Specify the source language: C, C<font SIZE="-2">++</font>, Objective-C, or assembly. This has nothing to do with standards conformance or extensions; it merely selects which base syntax to expect. If you give none of these options, cpp will deduce the language from the extension of the source file: <code>.c</code>, <code>.cc</code>, <code>.m</code>, or <code>.S</code>. Some other common extensions for C<font SIZE="-2">++</font> and assembly are also recognized. If cpp does not recognize the extension, it will treat the file as C; this is the most generic mode. </p>
<p> <code>Note:</code> Previous versions of cpp accepted a <code>-lang</code> option which selected both the language and the standards conformance level. This option has been removed, because it conflicts with the <code>-l</code> option. <br />
 </p>
 </dd>
<dt><code>-std=</code><i>standard</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-ansi</code></dt>
<dd> <p> Specify the standard to which the code should conform. Currently cpp only knows about the standards for C; other language standards will be added in the future. </p>
<p> <i>standard</i> may be one of: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>iso9899:1990</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:1990</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c89</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c89</code></dt>
<dd> <p> The <font SIZE="-1">ISO</font> C standard from 1990. <code>c89</code> is the customary shorthand for this version of the standard. </p>
<p> The <code>-ansi</code> option is equivalent to <code>-std=c89</code>. <br />
 </p>
 </dd>
<dt><code>iso9899:199409</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:199409</code></dt>
<dd> <p> The 1990 C standard, as amended in 1994. <br />
 </p>
 </dd>
<dt><code>iso9899:1999</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:1999</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c99</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c99</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:199x</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>iso9899:199x</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c9x</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>c9x</code></dt>
<dd> <p> The revised <font SIZE="-1">ISO</font> C standard, published in December 1999. Before publication, this was known as C9X. <br />
 </p>
 </dd>
<dt><code>gnu89</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>gnu89</code></dt>
<dd> <p> The 1990 C standard plus <font SIZE="-1">GNU</font> extensions. This is the default. <br />
 </p>
 </dd>
<dt><code>gnu99</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>gnu99</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>gnu9x</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>gnu9x</code></dt>
<dd> <p> The 1999 C standard plus <font SIZE="-1">GNU</font> extensions. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-I-</code></dt>
<dd> <p> Split the include path. Any directories specified with <code>-I</code> options before <code>-I-</code> are searched only for headers requested with <code>&quot;#include&nbsp;<wbr>&quot;</code>file <code>&quot;&quot;</code>; they are not searched for <code>&quot;#include&nbsp;<wbr>&lt;</code>file <code>&gt;&quot;</code>. If additional directories are specified with <code>-I</code> options after the <code>-I-</code>, those directories are searched for all <code>#include</code> directives. </p>
<p> In addition, <code>-I-</code> inhibits the use of the directory of the current file directory as the first search directory for <code>&quot;#include&nbsp;<wbr>&quot;</code>file <code>&quot;&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-nostdinc</code></dt>
<dd> <p> Do not search the standard system directories for header files. Only the directories you have specified with <code>-I</code> options (and the directory of the current file, if appropriate) are searched. <br />
 </p>
 </dd>
<dt><code>-nostdinc++</code></dt>
<dd> <p> Do not search for header files in the C<font SIZE="-2">++</font>-specific standard directories, but do still search the other standard directories. (This option is used when building the C<font SIZE="-2">++</font> library.) <br />
 </p>
 </dd>
<dt><code>-include</code><i>file</i></dt>
<dd> <p> Process <i>file</i> as if <code>&quot;#include &quot;file&quot;&quot;</code> appeared as the first line of the primary source file. However, the first directory searched for <i>file</i> is the preprocessor&#8217;s working directory <i>instead of</i> the directory containing the main source file. If not found there, it is searched for in the remainder of the <code>&quot;#include &quot;...&quot;&quot;</code> search chain as normal. </p>
<p> If multiple <code>-include</code> options are given, the files are included in the order they appear on the command line. <br />
 </p>
 </dd>
<dt><code>-imacros</code><i>file</i></dt>
<dd> <p> Exactly like <code>-include</code>, except that any output produced by scanning <i>file</i> is thrown away. Macros it defines remain defined. This allows you to acquire all the macros from a header without also processing its declarations. </p>
<p> All files specified by <code>-imacros</code> are processed before all files specified by <code>-include</code>. <br />
 </p>
 </dd>
<dt><code>-idirafter</code><i>dir</i></dt>
<dd> <p> Search <i>dir</i> for header files, but do it <i>after</i> all directories specified with <code>-I</code> and the standard system directories have been exhausted. <i>dir</i> is treated as a system include directory. <br />
 </p>
 </dd>
<dt><code>-iprefix</code><i>prefix</i></dt>
<dd> <p> Specify <i>prefix</i> as the prefix for subsequent <code>-iwithprefix</code> options. If the prefix represents a directory, you should include the final <code>/</code>. <br />
 </p>
 </dd>
<dt><code>-iwithprefix</code><i>dir</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-iwithprefixbefore</code><i>dir</i></dt>
<dd> <p> Append <i>dir</i> to the prefix specified previously with <code>-iprefix</code>, and add the resulting directory to the include search path. <code>-iwithprefixbefore</code> puts it in the same place <code>-I</code> would; <code>-iwithprefix</code> puts it where <code>-idirafter</code> would. </p>
<p> Use of these options is discouraged. <br />
 </p>
 </dd>
<dt><code>-isystem</code><i>dir</i></dt>
<dd> <p> Search <i>dir</i> for header files, after all directories specified by <code>-I</code> but before the standard system directories. Mark it as a system directory, so that it gets the same special treatment as is applied to the standard system directories. <br />
 </p>
 </dd>
<dt><code>-fpreprocessed</code></dt>
<dd> <p> Indicate to the preprocessor that the input file has already been preprocessed. This suppresses things like macro expansion, trigraph conversion, escaped newline splicing, and processing of most directives. The preprocessor still recognizes and removes comments, so that you can pass a file preprocessed with <code>-C</code> to the compiler without problems. In this mode the integrated preprocessor is little more than a tokenizer for the front ends. </p>
<p> <code>-fpreprocessed</code> is implicit if the input file has one of the extensions <code>.i</code>, <code>.ii</code> or <code>.mi</code>. These are the extensions that <font SIZE="-1">GCC</font> uses for preprocessed files created by <code>-save-temps</code>. <br />
 </p>
 </dd>
<dt><code>-ftabstop=</code><i>width</i></dt>
<dd> <p> Set the distance between tab stops. This helps the preprocessor report correct column numbers in warnings or errors, even if tabs appear on the line. If the value is less than 1 or greater than 100, the option is ignored. The default is 8. <br />
 </p>
 </dd>
<dt><code>-fno-show-column</code></dt>
<dd> <p> Do not print column numbers in diagnostics. This may be necessary if diagnostics are being scanned by a program that does not understand the column numbers, such as <code>dejagnu</code>. <br />
 </p>
 </dd>
<dt><code>-A</code><i>predicate</i><code>=</code><i>answer</i></dt>
<dd> <p> Make an assertion with the predicate <i>predicate</i> and answer <i>answer</i>. This form is preferred to the older form <code>-A</code> <i>predicate</i><code>(</code><i>answer</i><code>)</code>, which is still supported, because it does not use shell special characters. <br />
 </p>
 </dd>
<dt><code>-A -</code><i>predicate</i><code>=</code><i>answer</i></dt>
<dd> <p> Cancel an assertion with the predicate <i>predicate</i> and answer <i>answer</i>. <br />
 </p>
 </dd>
<dt><code>-A-</code></dt>
<dd> <p> Cancel all predefined assertions and all assertions preceding it on the command line. Also, undefine all predefined macros and all macros preceding it on the command line. (This is a historical wart and may change in the future.) <br />
 </p>
 </dd>
<dt><code>-dCHARS</code></dt>
<dd> <p> <i></i><font SIZE="-1"><i>CHARS</i></font><i></i> is a sequence of one or more of the following characters, and must not be preceded by a space. Other characters are interpreted by the compiler proper, or reserved for future versions of <font SIZE="-1">GCC</font>, and so are silently ignored. If you specify characters whose behavior conflicts, the result is undefined. </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>M</code></dt>
<dd> <p> Instead of the normal output, generate a list of <code>#define</code> directives for all the macros defined during the execution of the preprocessor, including predefined macros. This gives you a way of finding out what is predefined in your version of the preprocessor. Assuming you have no file <i>foo.h</i>, the command </p>
<pre><code>        touch foo.h; cpp -dM foo.h
</code></pre>
<p> will show all the predefined macros. <br />
 </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Like <code>M</code> except in two respects: it does <i>not</i> include the predefined macros, and it outputs <i>both</i> the <code>#define</code> directives and the result of preprocessing. Both kinds of output go to the standard output file. <br />
 </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> Like <code>D</code>, but emit only the macro names, not their expansions. <br />
 </p>
 </dd>
<dt><code>I</code></dt>
<dd> <p> Output <code>#include</code> directives in addition to the result of preprocessing. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-P</code></dt>
<dd> <p> Inhibit generation of linemarkers in the output from the preprocessor. This might be useful when running the preprocessor on something that is not C code, and will be sent to a program which might be confused by the linemarkers. <br />
 </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Do not discard comments. All comments are passed through to the output file, except for comments in processed directives, which are deleted along with the directive. </p>
<p> You should be prepared for side effects when using <code>-C</code>; it causes the preprocessor to treat comments as tokens in their own right. For example, comments appearing at the start of what would be a directive line have the effect of turning that line into an ordinary source line, since the first token on the line is no longer a <code>#</code>. <br />
 </p>
 </dd>
<dt><code>-gcc</code></dt>
<dd> <p> Define the macros __GNUC__, __GNUC_MINOR__ and __GNUC_PATCHLEVEL__. These are defined automatically when you use <code>gcc -E</code>; you can turn them off in that case with <code>-no-gcc</code>. <br />
 </p>
 </dd>
<dt><code>-traditional</code></dt>
<dd> <p> Try to imitate the behavior of old-fashioned C, as opposed to <font SIZE="-1">ISO</font> C. <br />
 </p>
 </dd>
<dt><code>-trigraphs</code></dt>
<dd> <p> Process trigraph sequences. These are three-character sequences, all starting with <code>??</code>, that are defined by <font SIZE="-1">ISO</font> C to stand for single characters. For example, <code>??/</code> stands for <code>\</code>, so <code>&#8216;??/n&#8217;</code> is a character constant for a newline. By default, <font SIZE="-1">GCC</font> ignores trigraphs, but in standard-conforming modes it converts them. See the <code>-std</code> and <code>-ansi</code> options. </p>
<p> The nine trigraphs and their replacements are </p>
<pre><code>        Trigraph: ??( ??) ??&lt; ??&gt; ??= ??/ ??' ??! ??-
        Replacement: [ ] { } # \ ^ | ~
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-remap</code></dt>
<dd> <p> Enable special code to work around file systems which only permit very short file names, such as <font SIZE="-1">MS-DOS</font>. <br />
 </p>
 </dd>
<dt><code>-$</code></dt>
<dd> <p> Forbid the use of <code>$</code> in identifiers. The C standard allows implementations to define extra characters that can appear in identifiers. By default <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font> permits <code>$</code>, a common extension. <br />
 </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>---help</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>---target-help</code></dt>
<dd> <p> Print text describing all the command line options instead of preprocessing anything. <br />
 </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Verbose mode. Print out <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font>&#8216;s version number at the beginning of execution, and report the final form of the include path. <br />
 </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> Print the name of each header file used, in addition to other normal activities. Each name is indented to show how deep in the <code>#include</code> stack it is. <br />
 </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>---version</code></dt>
<dd> <p> Print out <font SIZE="-1">GNU</font> <font SIZE="-1">CPP</font>&#8216;s version number. With one dash, proceed to preprocess as normal. With two dashes, exit immediately. </p>
 </dd></dl>
<h2>Passing Options to the Assembler</h2>
<p> You can pass options to the assembler. <br />
 </p>
<dl>
<dt><code>-Wa,</code><i>option</i></dt>
<dd> <p> Pass <i>option</i> as an option to the assembler. If <i>option</i> contains commas, it is split into multiple options at the commas. </p>
 </dd></dl>
<h2>Options for Linking</h2>
<p> These options come into play when the compiler links object files into an executable output file. They are meaningless if the compiler is not doing a link step. <br />
 </p>
<dl>
<dt><i>object-file-name</i></dt>
<dd> <p> A file name that does not end in a special recognized suffix is considered to name an object file or library. (Object files are distinguished from libraries by the linker according to the file contents.) If linking is done, these object files are used as input to the linker. <br />
 </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> If any of these options is used, then the linker is not run, and object file names should not be used as arguments. <br />
 </p>
 </dd>
<dt><code>-l</code><i>library</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-l</code><i>library</i></dt>
<dd> <p> Search the library named <i>library</i> when linking. (The second alternative with the library as a separate argument is only for <font SIZE="-1">POSIX</font> compliance and is not recommended.) </p>
<p> It makes a difference where in the command you write this option; the linker searches and processes libraries and object files in the order they are specified. Thus, <code>foo.o -lz bar.o</code> searches library <code>z</code> after file <i>foo.o</i> but before <i>bar.o</i>. If <i>bar.o</i> refers to functions in <code>z</code>, those functions may not be loaded. </p>
<p> The linker searches a standard list of directories for the library, which is actually a file named <i>liblibrary.a</i>. The linker then uses this file as if it had been specified precisely by name. </p>
<p> The directories searched include several standard system directories plus any that you specify with <code>-L</code>. </p>
<p> Normally the files found this way are library files---archive files whose members are object files. The linker handles an archive file by scanning through it for members which define symbols that have so far been referenced but not defined. But if the file that is found is an ordinary object file, it is linked in the usual fashion. The only difference between using an <code>-l</code> option and specifying a file name is that <code>-l</code> surrounds <i>library</i> with <code>lib</code> and <code>.a</code> and searches several directories. <br />
 </p>
 </dd>
<dt><code>-lobjc</code></dt>
<dd> <p> You need this special case of the <code>-l</code> option in order to link an Objective-C program. <br />
 </p>
 </dd>
<dt><code>-nostartfiles</code></dt>
<dd> <p> Do not use the standard system startup files when linking. The standard system libraries are used normally, unless <code>-nostdlib</code> or <code>-nodefaultlibs</code> is used. <br />
 </p>
 </dd>
<dt><code>-nodefaultlibs</code></dt>
<dd> <p> Do not use the standard system libraries when linking. Only the libraries you specify will be passed to the linker. The standard startup files are used normally, unless <code>-nostartfiles</code> is used. The compiler may generate calls to memcmp, memset, and memcpy for System V (and <font SIZE="-1">ISO</font> C) environments or to bcopy and bzero for <font SIZE="-1">BSD</font> environments. These entries are usually resolved by entries in libc. These entry points should be supplied through some other mechanism when this option is specified. <br />
 </p>
 </dd>
<dt><code>-nostdlib</code></dt>
<dd> <p> Do not use the standard system startup files or libraries when linking. No startup files and only the libraries you specify will be passed to the linker. The compiler may generate calls to memcmp, memset, and memcpy for System V (and <font SIZE="-1">ISO</font> C) environments or to bcopy and bzero for <font SIZE="-1">BSD</font> environments. These entries are usually resolved by entries in libc. These entry points should be supplied through some other mechanism when this option is specified. </p>
<p> One of the standard libraries bypassed by <code>-nostdlib</code> and <code>-nodefaultlibs</code> is <i>libgcc.a</i>, a library of internal subroutines that <font SIZE="-1">GCC</font> uses to overcome shortcomings of particular machines, or special needs for some languages. </p>
<p> In most cases, you need <i>libgcc.a</i> even when you want to avoid other standard libraries. In other words, when you specify <code>-nostdlib</code> or <code>-nodefaultlibs</code> you should usually specify <code>-lgcc</code> as well. This ensures that you have no unresolved references to internal <font SIZE="-1">GCC</font> library subroutines. (For example, <code>__main</code>, used to ensure C<font SIZE="-2">++</font> constructors will be called.) <br />
 </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Remove all symbol table and relocation information from the executable. <br />
 </p>
 </dd>
<dt><code>-static</code></dt>
<dd> <p> On systems that support dynamic linking, this prevents linking with the shared libraries. On other systems, this option has no effect. <br />
 </p>
 </dd>
<dt><code>-shared</code></dt>
<dd> <p> Produce a shared object which can then be linked with other objects to form an executable. Not all systems support this option. For predictable results, you must also specify the same set of options that were used to generate code (<code>-fpic</code>, <code>-fPIC</code>, or model suboptions) when you specify this option.[1] <br />
 </p>
 </dd>
<dt><code>-shared-libgcc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-static-libgcc</code></dt>
<dd> <p> On systems that provide <i>libgcc</i> as a shared library, these options force the use of either the shared or static version respectively. If no shared version of <i>libgcc</i> was built when the compiler was configured, these options have no effect. </p>
<p> There are several situations in which an application should use the shared <i>libgcc</i> instead of the static version. The most common of these is when the application wishes to throw and catch exceptions across different shared libraries. In that case, each of the libraries as well as the application itself should use the shared <i>libgcc</i>. </p>
<p> Therefore, the G++ and <font SIZE="-1">GCJ</font> drivers automatically add <code>-shared-libgcc</code> whenever you build a shared library or a main executable, because C<font SIZE="-2">++</font> and Java programs typically use exceptions, so this is the right thing to do. </p>
<p> If, instead, you use the <font SIZE="-1">GCC</font> driver to create shared libraries, you may find that they will not always be linked with the shared <i>libgcc</i>. If <font SIZE="-1">GCC</font> finds, at its configuration time, that you have a <font SIZE="-1">GNU</font> linker that does not support option <code>---eh-frame-hdr</code>, it will link the shared version of <i>libgcc</i> into shared libraries by default. Otherwise, it will take advantage of the linker and optimize away the linking with the shared version of <i>libgcc</i>, linking with the static version of libgcc by default. This allows exceptions to propagate through such shared libraries, without incurring relocation costs at library load time. </p>
<p> However, if a library or main executable is supposed to throw or catch exceptions, you must link it using the G++ or <font SIZE="-1">GCJ</font> driver, as appropriate for the languages used in the program, or using the option <code>-shared-libgcc</code>, such that it is linked with the shared <i>libgcc</i>. <br />
 </p>
 </dd>
<dt><code>-symbolic</code></dt>
<dd> <p> Bind references to global symbols when building a shared object. Warn about any unresolved references (unless overridden by the link editor option <code>-Xlinker -z -Xlinker defs</code>). Only a few systems support this option. <br />
 </p>
 </dd>
<dt><code>-Xlinker</code><i>option</i></dt>
<dd> <p> Pass <i>option</i> as an option to the linker. You can use this to supply system-specific linker options which <font SIZE="-1">GCC</font> does not know how to recognize. </p>
<p> If you want to pass an option that takes an argument, you must use <code>-Xlinker</code> twice, once for the option and once for the argument. For example, to pass <code>-assert definitions</code>, you must write <code>-Xlinker -assert -Xlinker definitions</code>. It does not work to write <code>-Xlinker ``-assert definitions&#8217;&#8216;</code>, because this passes the entire string as a single argument, which is not what the linker expects. <br />
 </p>
 </dd>
<dt><code>-Wl,</code><i>option</i></dt>
<dd> <p> Pass <i>option</i> as an option to the linker. If <i>option</i> contains commas, it is split into multiple options at the commas. <br />
 </p>
 </dd>
<dt><code>-u</code><i>symbol</i></dt>
<dd> <p> Pretend the symbol <i>symbol</i> is undefined, to force linking of library modules to define it. You can use <code>-u</code> multiple times with different symbols to force loading of additional library modules. </p>
 </dd></dl>
<h2>Options for Directory Search</h2>
<p> These options specify directories to search for header files, for libraries and for parts of the compiler: <br />
 </p>
<dl>
<dt><code>-I</code><i>dir</i></dt>
<dd> <p> Add the directory <i>dir</i> to the head of the list of directories to be searched for header files. This can be used to override a system header file, substituting your own version, since these directories are searched before the system header file directories. However, you should not use this option to add directories that contain vendor-supplied system header files (use <code>-isystem</code> for that). If you use more than one <code>-I</code> option, the directories are scanned in left-to-right order; the standard system directories come after. </p>
<p> If a standard system include directory, or a directory specified with <code>-isystem</code>, is also specified with <code>-I</code>, the <code>-I</code> option will be ignored. The directory will still be searched but as a system directory at its normal position in the system include chain. This is to ensure that <font SIZE="-1">GCC</font>&#8216;s procedure to fix buggy system headers and the ordering for the include_next directive are not inadvertantly changed. If you really need to change the search order for system directories, use the <code>-nostdinc</code> and/or <code>-isystem</code> options. <br />
 </p>
 </dd>
<dt><code>-I-</code></dt>
<dd> <p> Any directories you specify with <code>-I</code> options before the <code>-I-</code> option are searched only for the case of <code>#include &quot;</code><i>file</i><code>&quot;</code>; they are not searched for <code>#include &lt;</code><i>file</i><code>&gt;</code>. </p>
<p> If additional directories are specified with <code>-I</code> options after the <code>-I-</code>, these directories are searched for all <code>#include</code> directives. (Ordinarily <i>all</i> <code>-I</code> directories are used this way.) </p>
<p> In addition, the <code>-I-</code> option inhibits the use of the current directory (where the current input file came from) as the first search directory for <code>#include &quot;</code><i>file</i><code>&quot;</code>. There is no way to override this effect of <code>-I-</code>. With <code>-I.</code> you can specify searching the directory which was current when the compiler was invoked. That is not exactly the same as what the preprocessor does by default, but it is often satisfactory. </p>
<p> <code>-I-</code> does not inhibit the use of the standard system directories for header files. Thus, <code>-I-</code> and <code>-nostdinc</code> are independent. <br />
 </p>
 </dd>
<dt><code>-L</code><i>dir</i></dt>
<dd> <p> Add directory <i>dir</i> to the list of directories to be searched for <code>-l</code>. <br />
 </p>
 </dd>
<dt><code>-B</code><i>prefix</i></dt>
<dd> <p> This option specifies where to find the executables, libraries, include files, and data files of the compiler itself. </p>
<p> The compiler driver program runs one or more of the subprograms <i>cpp</i>, <i>cc1</i>, <i>as</i> and <i>ld</i>. It tries <i>prefix</i> as a prefix for each program it tries to run, both with and without <i>machine</i><code>/</code><i>version</i><code>/</code>. </p>
<p> For each subprogram to be run, the compiler driver first tries the <code>-B</code> prefix, if any. If that name is not found, or if <code>-B</code> was not specified, the driver tries two standard prefixes, which are <i>/usr/lib/gcc/</i> and <i>/usr/local/lib/gcc-lib/</i>. If neither of those results in a file name that is found, the unmodified program name is searched for using the directories specified in your <font SIZE="-1"><code>PATH</code></font> environment variable. </p>
<p> The compiler will check to see if the path provided by the <code>-B</code> refers to a directory, and if necessary it will add a directory separator character at the end of the path. </p>
<p> <code>-B</code> prefixes that effectively specify directory names also apply to libraries in the linker, because the compiler translates these options into <code>-L</code> options for the linker. They also apply to includes files in the preprocessor, because the compiler translates these options into <code>-isystem</code> options for the preprocessor. In this case, the compiler appends <code>include</code> to the prefix. </p>
<p> The run-time support file <i>libgcc.a</i> can also be searched for using the <code>-B</code> prefix, if needed. If it is not found there, the two standard prefixes above are tried, and that is all. The file is left out of the link if it is not found by those means. </p>
<p> Another way to specify a prefix much like the <code>-B</code> prefix is to use the environment variable <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. </p>
<p> As a special kludge, if the path provided by <code>-B</code> is <i>[dir/]stageN/</i>, where <i>N</i> is a number in the range 0 to 9, then it will be replaced by <i>[dir/]include</i>. This is to help with boot-strapping the compiler. <br />
 </p>
 </dd>
<dt><code>-specs=</code><i>file</i></dt>
<dd> <p> Process <i>file</i> after the compiler reads in the standard <i>specs</i> file, in order to override the defaults that the <i>gcc</i> driver program uses when determining what switches to pass to <i>cc1</i>, <i>cc1plus</i>, <i>as</i>, <i>ld</i>, etc. More than one <code>-specs=</code><i>file</i> can be specified on the command line, and they are processed in order, from left to right. </p>
 </dd></dl>
<h2>Specifying Target Machine and Compiler Version</h2>
<p> By default, <font SIZE="-1">GCC</font> compiles code for the same type of machine that you are using. However, it can also be installed as a cross-compiler, to compile for some other type of machine. In fact, several different configurations of <font SIZE="-1">GCC</font>, for different target machines, can be installed side by side. Then you specify which one to use with the <code>-b</code> option. </p>
<p> In addition, older and newer versions of <font SIZE="-1">GCC</font> can be installed side by side. One of them (probably the newest) will be the default, but you may sometimes wish to use another. <br />
 </p>
<dl>
<dt><code>-b</code><i>machine</i></dt>
<dd> <p> The argument <i>machine</i> specifies the target machine for compilation. This is useful when you have installed <font SIZE="-1">GCC</font> as a cross-compiler. </p>
<p> The value to use for <i>machine</i> is the same as was specified as the machine type when configuring <font SIZE="-1">GCC</font> as a cross-compiler. For example, if a cross-compiler was configured with <code>configure i386v</code>, meaning to compile for an 80386 running System V, then you would specify <code>-b i386v</code> to run that cross compiler. </p>
<p> When you do not specify <code>-b</code>, it normally means to compile for the same type of machine that you are using. <br />
 </p>
 </dd>
<dt><code>-V</code><i>version</i></dt>
<dd> <p> The argument <i>version</i> specifies which version of <font SIZE="-1">GCC</font> to run. This is useful when multiple versions are installed. For example, <i>version</i> might be <code>2.0</code>, meaning to run <font SIZE="-1">GCC</font> version 2.0. </p>
<p> The default version, when you do not specify <code>-V</code>, is the last version of <font SIZE="-1">GCC</font> that you installed. </p>
 </dd></dl>
<p> The <code>-b</code> and <code>-V</code> options actually work by controlling part of the file name used for the executable files and libraries used for compilation. A given version of <font SIZE="-1">GCC</font>, for a given target machine, is normally kept in the directory <i>/usr/local/lib/gcc-lib/machine/version</i>. </p>
<p> Thus, sites can customize the effect of <code>-b</code> or <code>-V</code> either by changing the names of these directories or adding alternate names (or symbolic links). If in directory <i>/usr/local/lib/gcc-lib/</i> the file <i>80386</i> is a link to the file <i>i386v</i>, then <code>-b 80386</code> becomes an alias for <code>-b i386v</code>. </p>
<p> In one respect, the <code>-b</code> or <code>-V</code> do not completely change to a different compiler: the top-level driver program <code>gcc</code> that you originally invoked continues to run and invoke the other executables (preprocessor, compiler per se, assembler and linker) that do the real work. However, since no real work is done in the driver program, it usually does not matter that the driver program in use is not the one for the specified target. It is common for the interface to the other executables to change incompatibly between compiler versions, so unless the version specified is very close to that of the driver (for example, <code>-V 3.0</code> with a driver program from <font SIZE="-1">GCC</font> version 3.0.1), use of <code>-V</code> may not work; for example, using <code>-V 2.95.2</code> will not work with a driver program from <font SIZE="-1">GCC</font> 3.0. </p>
<p> The only way that the driver program depends on the target machine is in the parsing and handling of special machine-specific options. However, this is controlled by a file which is found, along with the other executables, in the directory for the specified version and target machine. As a result, a single installed driver program adapts to any specified target machine, and sufficiently similar compiler versions. </p>
<p> The driver program executable does control one significant thing, however: the default version and target machine. Therefore, you can install different instances of the driver program, compiled for different targets or versions, under different names. </p>
<p> For example, if the driver for version 2.0 is installed as <code>ogcc</code> and that for version 2.1 is installed as <code>gcc</code>, then the command <code>gcc</code> will use version 2.1 by default, while <code>ogcc</code> will use 2.0 by default. However, you can choose either version with either command with the <code>-V</code> option.  </p>
<h2>Hardware Models and Configurations</h2>
<p> Earlier we discussed the standard option <code>-b</code> which chooses among different installed compilers for completely different target machines, such as <font SIZE="-1">VAX</font> vs. 68000 vs. 80386. </p>
<p> In addition, each of these target machine types can have its own special options, starting with <code>-m</code>, to choose among various hardware models or configurations---for example, 68010 vs 68020, floating coprocessor or none. A single installed version of the compiler can compile for any model or configuration, according to the options specified. </p>
<p> Some configurations of the compiler also support additional special options, usually for compatibility with other compilers on the same platform. </p>
<p> These options are defined by the macro <code>&quot;TARGET_SWITCHES&quot;</code> in the machine description. The default for the options is also defined by that macro, which enables you to change the defaults. </p>
<p> <i>M680x0 Options</i>  </p>
<p> These are the <code>-m</code> options defined for the 68000 series. The default values for these options depends on which style of 68000 was selected when the compiler was configured; the defaults for the most common choices are given below. <br />
 </p>
<dl>
<dt><code>-m68000</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mc68000</code></dt>
<dd> <p> Generate output for a 68000. This is the default when the compiler is configured for 68000-based systems. </p>
<p> Use this option for microcontrollers with a 68000 or <font SIZE="-1">EC000</font> core, including the 68008, 68302, 68306, 68307, 68322, 68328 and 68356. <br />
 </p>
 </dd>
<dt><code>-m68020</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mc68020</code></dt>
<dd> <p> Generate output for a 68020. This is the default when the compiler is configured for 68020-based systems. <br />
 </p>
 </dd>
<dt><code>-m68881</code></dt>
<dd> <p> Generate output containing 68881 instructions for floating point. This is the default for most 68020 systems unless <code>---nfp</code> was specified when the compiler was configured. <br />
 </p>
 </dd>
<dt><code>-m68030</code></dt>
<dd> <p> Generate output for a 68030. This is the default when the compiler is configured for 68030-based systems. <br />
 </p>
 </dd>
<dt><code>-m68040</code></dt>
<dd> <p> Generate output for a 68040. This is the default when the compiler is configured for 68040-based systems. </p>
<p> This option inhibits the use of 68881/68882 instructions that have to be emulated by software on the 68040. Use this option if your 68040 does not have code to emulate those instructions. <br />
 </p>
 </dd>
<dt><code>-m68060</code></dt>
<dd> <p> Generate output for a 68060. This is the default when the compiler is configured for 68060-based systems. </p>
<p> This option inhibits the use of 68020 and 68881/68882 instructions that have to be emulated by software on the 68060. Use this option if your 68060 does not have code to emulate those instructions. <br />
 </p>
 </dd>
<dt><code>-mcpu32</code></dt>
<dd> <p> Generate output for a <font SIZE="-1">CPU32</font>. This is the default when the compiler is configured for CPU32-based systems. </p>
<p> Use this option for microcontrollers with a <font SIZE="-1">CPU32</font> or <font SIZE="-1">CPU32+</font> core, including the 68330, 68331, 68332, 68333, 68334, 68336, 68340, 68341, 68349 and 68360. <br />
 </p>
 </dd>
<dt><code>-m5200</code></dt>
<dd> <p> Generate output for a 520X ``coldfire&#8217;&#8216; family cpu. This is the default when the compiler is configured for 520X-based systems. </p>
<p> Use this option for microcontroller with a 5200 core, including the <font SIZE="-1">MCF5202</font>, <font SIZE="-1">MCF5203</font>, <font SIZE="-1">MCF5204</font> and <font SIZE="-1">MCF5202</font>. <br />
 </p>
 </dd>
<dt><code>-m68020-40</code></dt>
<dd> <p> Generate output for a 68040, without using any of the new instructions. This results in code which can run relatively efficiently on either a 68020/68881 or a 68030 or a 68040. The generated code does use the 68881 instructions that are emulated on the 68040. <br />
 </p>
 </dd>
<dt><code>-m68020-60</code></dt>
<dd> <p> Generate output for a 68060, without using any of the new instructions. This results in code which can run relatively efficiently on either a 68020/68881 or a 68030 or a 68040. The generated code does use the 68881 instructions that are emulated on the 68060. <br />
 </p>
 </dd>
<dt><code>-mfpa</code></dt>
<dd> <p> Generate output containing Sun <font SIZE="-1">FPA</font> instructions for floating point. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all m68k targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded targets <code>m68k-*-aout</code> and <code>m68k-*-coff</code> do provide software floating point support. <br />
 </p>
 </dd>
<dt><code>-mshort</code></dt>
<dd> <p> Consider type <code>&quot;int&quot;</code> to be 16 bits wide, like <code>&quot;short int&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mnobitfield</code></dt>
<dd> <p> Do not use the bit-field instructions. The <code>-m68000</code>, <code>-mcpu32</code> and <code>-m5200</code> options imply <code>-mnobitfield</code>. <br />
 </p>
 </dd>
<dt><code>-mbitfield</code></dt>
<dd> <p> Do use the bit-field instructions. The <code>-m68020</code> option implies <code>-mbitfield</code>. This is the default if you use a configuration designed for a 68020. <br />
 </p>
 </dd>
<dt><code>-mrtd</code></dt>
<dd> <p> Use a different function-calling convention, in which functions that take a fixed number of arguments return with the <code>&quot;rtd&quot;</code> instruction, which pops their arguments while returning. This saves one instruction in the caller since there is no need to pop the arguments there. </p>
<p> This calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <code>&quot;printf&quot;</code>); otherwise incorrect code will be generated for calls to those functions. </p>
<p> In addition, seriously incorrect code will result if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.) </p>
<p> The <code>&quot;rtd&quot;</code> instruction is supported by the 68010, 68020, 68030, 68040, 68060 and <font SIZE="-1">CPU32</font> processors, but not by the 68000 or 5200. <br />
 </p>
 </dd>
<dt><code>-malign-int</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-align-int</code></dt>
<dd> <p> Control whether <font SIZE="-1">GCC</font> aligns <code>&quot;int&quot;</code>, <code>&quot;long&quot;</code>, <code>&quot;long long&quot;</code>, <code>&quot;float&quot;</code>, <code>&quot;double&quot;</code>, and <code>&quot;long double&quot;</code> variables on a 32-bit boundary (<code>-malign-int</code>) or a 16-bit boundary (<code>-mno-align-int</code>). Aligning variables on 32-bit boundaries produces code that runs somewhat faster on processors with 32-bit busses at the expense of more memory. </p>
<p> <code>Warning:</code> if you use the <code>-malign-int</code> switch, <font SIZE="-1">GCC</font> will align structures containing the above types differently than most published application binary interface specifications for the m68k. <br />
 </p>
 </dd>
<dt><code>-mpcrel</code></dt>
<dd> <p> Use the pc-relative addressing mode of the 68000 directly, instead of using a global offset table. At present, this option implies <code>-fpic</code>, allowing at most a 16-bit offset for pc-relative addressing. <code>-fPIC</code> is not presently supported with <code>-mpcrel</code>, though this could be supported for 68020 and higher processors. <br />
 </p>
 </dd>
<dt><code>-mno-strict-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mstrict-align</code></dt>
<dd> <p> Do not (do) assume that unaligned memory references will be handled by the system. </p>
 </dd></dl>
<p> <i>M68hc1x Options</i>  </p>
<p> These are the <code>-m</code> options defined for the 68hc11 and 68hc12 microcontrollers. The default values for these options depends on which style of microcontroller was selected when the compiler was configured; the defaults for the most common choices are given below. <br />
 </p>
<dl>
<dt><code>-m6811</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m68hc11</code></dt>
<dd> <p> Generate output for a 68HC11. This is the default when the compiler is configured for 68HC11-based systems. <br />
 </p>
 </dd>
<dt><code>-m6812</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m68hc12</code></dt>
<dd> <p> Generate output for a 68HC12. This is the default when the compiler is configured for 68HC12-based systems. <br />
 </p>
 </dd>
<dt><code>-mauto-incdec</code></dt>
<dd> <p> Enable the use of 68HC12 pre and post auto-increment and auto-decrement addressing modes. <br />
 </p>
 </dd>
<dt><code>-mshort</code></dt>
<dd> <p> Consider type <code>&quot;int&quot;</code> to be 16 bits wide, like <code>&quot;short int&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-msoft-reg-count=</code><i>count</i></dt>
<dd> <p> Specify the number of pseudo-soft registers which are used for the code generation. The maximum number is 32. Using more pseudo-soft register may or may not result in better code depending on the program. The default is 4 for 68HC11 and 2 for 68HC12. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>VAX</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">VAX:</font> <br />
 </p>
<dl>
<dt><code>-munix</code></dt>
<dd> <p> Do not output certain jump instructions (<code>&quot;aobleq&quot;</code> and so on) that the Unix assembler for the <font SIZE="-1">VAX</font> cannot handle across long ranges. <br />
 </p>
 </dd>
<dt><code>-mgnu</code></dt>
<dd> <p> Do output those jump instructions, on the assumption that you will assemble with the <font SIZE="-1">GNU</font> assembler. <br />
 </p>
 </dd>
<dt><code>-mg</code></dt>
<dd> <p> Output code for g-format floating point numbers instead of d-format. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>SPARC</i></font><i> Options</i>  </p>
<p> These <code>-m</code> switches are supported on the <font SIZE="-1">SPARC:</font> <br />
 </p>
<dl>
<dt><code>-mno-app-regs</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mapp-regs</code></dt>
<dd> <p> Specify <code>-mapp-regs</code> to generate output using the global registers 2 through 4, which the <font SIZE="-1">SPARC</font> <font SIZE="-1">SVR4</font> <font SIZE="-1">ABI</font> reserves for applications. This is the default. </p>
<p> To be fully <font SIZE="-1">SVR4</font> <font SIZE="-1">ABI</font> compliant at the cost of some performance loss, specify <code>-mno-app-regs</code>. You should compile libraries and system software with this option. <br />
 </p>
 </dd>
<dt><code>-mfpu</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mhard-float</code></dt>
<dd> <p> Generate output containing floating point instructions. This is the default. <br />
 </p>
 </dd>
<dt><code>-mno-fpu</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">SPARC</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded targets <code>sparc-*-aout</code> and <code>sparclite-*-*</code> do provide software floating point support. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC</font>, with <code>-msoft-float</code> in order for this to work. <br />
 </p>
 </dd>
<dt><code>-mhard-quad-float</code></dt>
<dd> <p> Generate output containing quad-word (long double) floating point instructions. <br />
 </p>
 </dd>
<dt><code>-msoft-quad-float</code></dt>
<dd> <p> Generate output containing library calls for quad-word (long double) floating point instructions. The functions called are those specified in the <font SIZE="-1">SPARC</font> <font SIZE="-1">ABI</font>. This is the default. </p>
<p> As of this writing, there are no sparc implementations that have hardware support for the quad-word floating point instructions. They all invoke a trap handler for one of these instructions, and then the trap handler emulates the effect of the instruction. Because of the trap handler overhead, this is much slower than calling the <font SIZE="-1">ABI</font> library routines. Thus the <code>-msoft-quad-float</code> option is the default. <br />
 </p>
 </dd>
<dt><code>-mno-flat</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mflat</code></dt>
<dd> <p> With <code>-mflat</code>, the compiler does not generate save/restore instructions and will use a ``flat&#8217;&#8216; or single register window calling convention. This model uses <code>%i7</code> as the frame pointer and is compatible with the normal register window model. Code from either may be intermixed. The local registers and the input registers (0---5) are still treated as ``call saved&#8217;&#8216; registers and will be saved on the stack as necessary. </p>
<p> With <code>-mno-flat</code> (the default), the compiler emits save/restore instructions (except for leaf functions) and is the normal mode of operation. <br />
 </p>
 </dd>
<dt><code>-mno-unaligned-doubles</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-munaligned-doubles</code></dt>
<dd> <p> Assume that doubles have 8 byte alignment. This is the default. </p>
<p> With <code>-munaligned-doubles</code>, <font SIZE="-1">GCC</font> assumes that doubles have 8 byte alignment only if they are contained in another type, or if they have an absolute address. Otherwise, it assumes they have 4 byte alignment. Specifying this option avoids some rare compatibility problems with code generated by other compilers. It is not the default because it results in a performance loss, especially for floating point code. <br />
 </p>
 </dd>
<dt><code>-mno-faster-structs</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mfaster-structs</code></dt>
<dd> <p> With <code>-mfaster-structs</code>, the compiler assumes that structures should have 8 byte alignment. This enables the use of pairs of <code>&quot;ldd&quot;</code> and <code>&quot;std&quot;</code> instructions for copies in structure assignment, in place of twice as many <code>&quot;ld&quot;</code> and <code>&quot;st&quot;</code> pairs. However, the use of this changed alignment directly violates the Sparc <font SIZE="-1">ABI</font>. Thus, it&#8217;s intended only for use on targets where the developer acknowledges that their resulting code will not be directly in line with the rules of the <font SIZE="-1">ABI</font>. <br />
 </p>
 </dd>
<dt><code>-mv8</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msparclite</code></dt>
<dd> <p> These two options select variations on the <font SIZE="-1">SPARC</font> architecture. </p>
<p> By default (unless specifically configured for the Fujitsu SPARClite), <font SIZE="-1">GCC</font> generates code for the v7 variant of the <font SIZE="-1">SPARC</font> architecture. </p>
<p> <code>-mv8</code> will give you <font SIZE="-1">SPARC</font> v8 code. The only difference from v7 code is that the compiler emits the integer multiply and integer divide instructions which exist in <font SIZE="-1">SPARC</font> v8 but not in <font SIZE="-1">SPARC</font> v7. </p>
<p> <code>-msparclite</code> will give you SPARClite code. This adds the integer multiply, integer divide step and scan (<code>&quot;ffs&quot;</code>) instructions which exist in SPARClite but not in <font SIZE="-1">SPARC</font> v7. </p>
<p> These options are deprecated and will be deleted in a future <font SIZE="-1">GCC</font> release. They have been replaced with <code>-mcpu=xxx</code>. <br />
 </p>
 </dd>
<dt><code>-mcypress</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msupersparc</code></dt>
<dd> <p> These two options select the processor for which the code is optimized. </p>
<p> With <code>-mcypress</code> (the default), the compiler optimizes code for the Cypress <font SIZE="-1">CY7C602</font> chip, as used in the SparcStation/SparcServer 3xx series. This is also appropriate for the older SparcStation 1, 2, <font SIZE="-1">IPX</font> etc. </p>
<p> With <code>-msupersparc</code> the compiler optimizes code for the SuperSparc cpu, as used in the SparcStation 10, 1000 and 2000 series. This flag also enables use of the full <font SIZE="-1">SPARC</font> v8 instruction set. </p>
<p> These options are deprecated and will be deleted in a future <font SIZE="-1">GCC</font> release. They have been replaced with <code>-mcpu=xxx</code>. <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>cpu_type</i></dt>
<dd> <p> Set the instruction set, register set, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>v7</code>, <code>cypress</code>, <code>v8</code>, <code>supersparc</code>, <code>sparclite</code>, <code>hypersparc</code>, <code>sparclite86x</code>, <code>f930</code>, <code>f934</code>, <code>sparclet</code>, <code>tsc701</code>, <code>v9</code>, and <code>ultrasparc</code>. </p>
<p> Default instruction scheduling parameters are used for values that select an architecture and not an implementation. These are <code>v7</code>, <code>v8</code>, <code>sparclite</code>, <code>sparclet</code>, <code>v9</code>. </p>
<p> Here is a list of each supported architecture and their supported implementations. </p>
<pre><code>            v7: cypress
            v8: supersparc, hypersparc
            sparclite: f930, f934, sparclite86x
            sparclet: tsc701
            v9: ultrasparc
</code></pre>
<p> <br />
 </p>
 </dd>
<dt><code>-mtune=</code><i>cpu_type</i></dt>
<dd> <p> Set the instruction scheduling parameters for machine type <i>cpu_type</i>, but do not set the instruction set or register set that the option <code>-mcpu=</code><i>cpu_type</i> would. </p>
<p> The same values for <code>-mcpu=</code><i>cpu_type</i> can be used for <code>-mtune=</code><i>cpu_type</i>, but the only useful values are those that select a particular cpu implementation. Those are <code>cypress</code>, <code>supersparc</code>, <code>hypersparc</code>, <code>f930</code>, <code>f934</code>, <code>sparclite86x</code>, <code>tsc701</code>, and <code>ultrasparc</code>. </p>
 </dd></dl>
<p> These <code>-m</code> switches are supported in addition to the above on the <font SIZE="-1">SPARCLET</font> processor. <br />
 </p>
<dl>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> Generate code for a processor running in little-endian mode. <br />
 </p>
 </dd>
<dt><code>-mlive-g0</code></dt>
<dd> <p> Treat register <code>&quot;%g0&quot;</code> as a normal register. <font SIZE="-1">GCC</font> will continue to clobber it as necessary but will not assume it always reads as 0. <br />
 </p>
 </dd>
<dt><code>-mbroken-saverestore</code></dt>
<dd> <p> Generate code that does not use non-trivial forms of the <code>&quot;save&quot;</code> and <code>&quot;restore&quot;</code> instructions. Early versions of the <font SIZE="-1">SPARCLET</font> processor do not correctly handle <code>&quot;save&quot;</code> and <code>&quot;restore&quot;</code> instructions used with arguments. They correctly handle them used without arguments. A <code>&quot;save&quot;</code> instruction used without arguments increments the current window pointer but does not allocate a new stack frame. It is assumed that the window overflow trap handler will properly handle this case as will interrupt handlers. </p>
 </dd></dl>
<p> These <code>-m</code> switches are supported in addition to the above on <font SIZE="-1">SPARC</font> V9 processors in 64-bit environments. <br />
 </p>
<dl>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> Generate code for a processor running in little-endian mode. <br />
 </p>
 </dd>
<dt><code>-m32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m64</code></dt>
<dd> <p> Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits. <br />
 </p>
 </dd>
<dt><code>-mcmodel=medlow</code></dt>
<dd> <p> Generate code for the Medium/Low code model: the program must be linked in the low 32 bits of the address space. Pointers are 64 bits. Programs can be statically or dynamically linked. <br />
 </p>
 </dd>
<dt><code>-mcmodel=medmid</code></dt>
<dd> <p> Generate code for the Medium/Middle code model: the program must be linked in the low 44 bits of the address space, the text segment must be less than 2G bytes, and data segment must be within 2G of the text segment. Pointers are 64 bits. <br />
 </p>
 </dd>
<dt><code>-mcmodel=medany</code></dt>
<dd> <p> Generate code for the Medium/Anywhere code model: the program may be linked anywhere in the address space, the text segment must be less than 2G bytes, and data segment must be within 2G of the text segment. Pointers are 64 bits. <br />
 </p>
 </dd>
<dt><code>-mcmodel=embmedany</code></dt>
<dd> <p> Generate code for the Medium/Anywhere code model for embedded systems: assume a 32-bit text and a 32-bit data segment, both starting anywhere (determined at link time). Register <code>%g4</code> points to the base of the data segment. Pointers are still 64 bits. Programs are statically linked, <font SIZE="-1">PIC</font> is not supported. <br />
 </p>
 </dd>
<dt><code>-mstack-bias</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-stack-bias</code></dt>
<dd> <p> With <code>-mstack-bias</code>, <font SIZE="-1">GCC</font> assumes that the stack pointer, and frame pointer if present, are offset by -2047 which must be added back when making stack frame references. Otherwise, assume no such offset is present. </p>
 </dd></dl>
<p> <i>Convex Options</i>  </p>
<p> These <code>-m</code> options are defined for Convex: <br />
 </p>
<dl>
<dt><code>-mc1</code></dt>
<dd> <p> Generate output for C1. The code will run on any Convex machine. The preprocessor symbol <code>&quot;__convex__c1__&quot;</code> is defined. <br />
 </p>
 </dd>
<dt><code>-mc2</code></dt>
<dd> <p> Generate output for C2. Uses instructions not available on C1. Scheduling and other optimizations are chosen for max performance on C2. The preprocessor symbol <code>&quot;__convex_c2__&quot;</code> is defined. <br />
 </p>
 </dd>
<dt><code>-mc32</code></dt>
<dd> <p> Generate output for C32xx. Uses instructions not available on C1. Scheduling and other optimizations are chosen for max performance on C32. The preprocessor symbol <code>&quot;__convex_c32__&quot;</code> is defined. <br />
 </p>
 </dd>
<dt><code>-mc34</code></dt>
<dd> <p> Generate output for C34xx. Uses instructions not available on C1. Scheduling and other optimizations are chosen for max performance on C34. The preprocessor symbol <code>&quot;__convex_c34__&quot;</code> is defined. <br />
 </p>
 </dd>
<dt><code>-mc38</code></dt>
<dd> <p> Generate output for C38xx. Uses instructions not available on C1. Scheduling and other optimizations are chosen for max performance on C38. The preprocessor symbol <code>&quot;__convex_c38__&quot;</code> is defined. <br />
 </p>
 </dd>
<dt><code>-margcount</code></dt>
<dd> <p> Generate code which puts an argument count in the word preceding each argument list. This is compatible with regular <font SIZE="-1">CC</font>, and a few programs may need the argument count word. <font SIZE="-1">GDB</font> and other source-level debuggers do not need it; this info is in the symbol table. <br />
 </p>
 </dd>
<dt><code>-mnoargcount</code></dt>
<dd> <p> Omit the argument count word. This is the default. <br />
 </p>
 </dd>
<dt><code>-mvolatile-cache</code></dt>
<dd> <p> Allow volatile references to be cached. This is the default. <br />
 </p>
 </dd>
<dt><code>-mvolatile-nocache</code></dt>
<dd> <p> Volatile references bypass the data cache, going all the way to memory. This is only needed for multi-processor code that does not use standard synchronization instructions. Making non-volatile references to volatile locations will not necessarily work. <br />
 </p>
 </dd>
<dt><code>-mlong32</code></dt>
<dd> <p> Type long is 32 bits, the same as type int. This is the default. <br />
 </p>
 </dd>
<dt><code>-mlong64</code></dt>
<dd> <p> Type long is 64 bits, the same as type long long. This option is useless, because no library support exists for it. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>AMD29K</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">AMD</font> Am29000: <br />
 </p>
<dl>
<dt><code>-mdw</code></dt>
<dd> <p> Generate code that assumes the <code>&quot;DW&quot;</code> bit is set, i.e., that byte and halfword operations are directly supported by the hardware. This is the default. <br />
 </p>
 </dd>
<dt><code>-mndw</code></dt>
<dd> <p> Generate code that assumes the <code>&quot;DW&quot;</code> bit is not set. <br />
 </p>
 </dd>
<dt><code>-mbw</code></dt>
<dd> <p> Generate code that assumes the system supports byte and halfword write operations. This is the default. <br />
 </p>
 </dd>
<dt><code>-mnbw</code></dt>
<dd> <p> Generate code that assumes the systems does not support byte and halfword write operations. <code>-mnbw</code> implies <code>-mndw</code>. <br />
 </p>
 </dd>
<dt><code>-msmall</code></dt>
<dd> <p> Use a small memory model that assumes that all function addresses are either within a single 256 <font SIZE="-1">KB</font> segment or at an absolute address of less than 256k. This allows the <code>&quot;call&quot;</code> instruction to be used instead of a <code>&quot;const&quot;</code>, <code>&quot;consth&quot;</code>, <code>&quot;calli&quot;</code> sequence. <br />
 </p>
 </dd>
<dt><code>-mnormal</code></dt>
<dd> <p> Use the normal memory model: Generate <code>&quot;call&quot;</code> instructions only when calling functions in the same file and <code>&quot;calli&quot;</code> instructions otherwise. This works if each file occupies less than 256 <font SIZE="-1">KB</font> but allows the entire executable to be larger than 256 <font SIZE="-1">KB</font>. This is the default. <br />
 </p>
 </dd>
<dt><code>-mlarge</code></dt>
<dd> <p> Always use <code>&quot;calli&quot;</code> instructions. Specify this option if you expect a single file to compile into more than 256 <font SIZE="-1">KB</font> of code. <br />
 </p>
 </dd>
<dt><code>-m29050</code></dt>
<dd> <p> Generate code for the Am29050. <br />
 </p>
 </dd>
<dt><code>-m29000</code></dt>
<dd> <p> Generate code for the Am29000. This is the default. <br />
 </p>
 </dd>
<dt><code>-mkernel-registers</code></dt>
<dd> <p> Generate references to registers <code>&quot;gr64-gr95&quot;</code> instead of to registers <code>&quot;gr96-gr127&quot;</code>. This option can be used when compiling kernel code that wants a set of global registers disjoint from that used by user-mode code. </p>
<p> Note that when this option is used, register names in <code>-f</code> flags must use the normal, user-mode, names. <br />
 </p>
 </dd>
<dt><code>-muser-registers</code></dt>
<dd> <p> Use the normal set of global registers, <code>&quot;gr96-gr127&quot;</code>. This is the default. <br />
 </p>
 </dd>
<dt><code>-mstack-check</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-stack-check</code></dt>
<dd> <p> Insert (or do not insert) a call to <code>&quot;__msp_check&quot;</code> after each stack adjustment. This is often used for kernel code. <br />
 </p>
 </dd>
<dt><code>-mstorem-bug</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-storem-bug</code></dt>
<dd> <p> <code>-mstorem-bug</code> handles 29k processors which cannot handle the separation of a mtsrim insn and a storem instruction (most 29000 chips to date, but not the 29050). <br />
 </p>
 </dd>
<dt><code>-mno-reuse-arg-regs</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mreuse-arg-regs</code></dt>
<dd> <p> <code>-mno-reuse-arg-regs</code> tells the compiler to only use incoming argument registers for copying out arguments. This helps detect calling a function with fewer arguments than it was declared with. <br />
 </p>
 </dd>
<dt><code>-mno-impure-text</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mimpure-text</code></dt>
<dd> <p> <code>-mimpure-text</code>, used in addition to <code>-shared</code>, tells the compiler to not pass <code>-assert pure-text</code> to the linker when linking a shared object. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not part of <font SIZE="-1">GCC</font>. Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. <br />
 </p>
 </dd>
<dt><code>-mno-multm</code></dt>
<dd> <p> Do not generate multm or multmu instructions. This is useful for some embedded systems which do not have trap handlers for these instructions. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>ARM</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for Advanced <font SIZE="-1">RISC</font> Machines (<font SIZE="-1">ARM</font>) architectures: <br />
 </p>
<dl>
<dt><code>-mapcs-frame</code></dt>
<dd> <p> Generate a stack frame that is compliant with the <font SIZE="-1">ARM</font> Procedure Call Standard for all functions, even if this is not strictly necessary for correct execution of the code. Specifying <code>-fomit-frame-pointer</code> with this option will cause the stack frames not to be generated for leaf functions. The default is <code>-mno-apcs-frame</code>. <br />
 </p>
 </dd>
<dt><code>-mapcs</code></dt>
<dd> <p> This is a synonym for <code>-mapcs-frame</code>. <br />
 </p>
 </dd>
<dt><code>-mapcs-26</code></dt>
<dd> <p> Generate code for a processor running with a 26-bit program counter, and conforming to the function calling standards for the <font SIZE="-1">APCS</font> 26-bit option. This option replaces the <code>-m2</code> and <code>-m3</code> options of previous releases of the compiler. <br />
 </p>
 </dd>
<dt><code>-mapcs-32</code></dt>
<dd> <p> Generate code for a processor running with a 32-bit program counter, and conforming to the function calling standards for the <font SIZE="-1">APCS</font> 32-bit option. This option replaces the <code>-m6</code> option of previous releases of the compiler. <br />
 </p>
 </dd>
<dt><code>-mthumb-interwork</code></dt>
<dd> <p> Generate code which supports calling between the <font SIZE="-1">ARM</font> and Thumb instruction sets. Without this option the two instruction sets cannot be reliably used inside one program. The default is <code>-mno-thumb-interwork</code>, since slightly larger code is generated when <code>-mthumb-interwork</code> is specified. <br />
 </p>
 </dd>
<dt><code>-mno-sched-prolog</code></dt>
<dd> <p> Prevent the reordering of instructions in the function prolog, or the merging of those instruction with the instructions in the function&#8217;s body. This means that all functions will start with a recognizable set of instructions (or in fact one of a choice from a small set of different function prologues), and this information can be used to locate the start if functions inside an executable piece of code. The default is <code>-msched-prolog</code>. <br />
 </p>
 </dd>
<dt><code>-mhard-float</code></dt>
<dd> <p> Generate output containing floating point instructions. This is the default. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">ARM</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC</font>, with <code>-msoft-float</code> in order for this to work. <br />
 </p>
 </dd>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> Generate code for a processor running in little-endian mode. This is the default for all standard configurations. <br />
 </p>
 </dd>
<dt><code>-mbig-endian</code></dt>
<dd> <p> Generate code for a processor running in big-endian mode; the default is to compile code for a little-endian processor. <br />
 </p>
 </dd>
<dt><code>-mwords-little-endian</code></dt>
<dd> <p> This option only applies when generating code for big-endian processors. Generate code for a little-endian word order but a big-endian byte order. That is, a byte order of the form <code>32107654</code>. Note: this option should only be used if you require compatibility with code for big-endian <font SIZE="-1">ARM</font> processors generated by versions of the compiler prior to 2.8. <br />
 </p>
 </dd>
<dt><code>-malignment-traps</code></dt>
<dd> <p> Generate code that will not trap if the <font SIZE="-1">MMU</font> has alignment traps enabled. On <font SIZE="-1">ARM</font> architectures prior to ARMv4, there were no instructions to access half-word objects stored in memory. However, when reading from memory a feature of the <font SIZE="-1">ARM</font> architecture allows a word load to be used, even if the address is unaligned, and the processor core will rotate the data as it is being loaded. This option tells the compiler that such misaligned accesses will cause a <font SIZE="-1">MMU</font> trap and that it should instead synthesise the access as a series of byte accesses. The compiler can still use word accesses to load half-word data if it knows that the address is aligned to a word boundary. </p>
<p> This option is ignored when compiling for <font SIZE="-1">ARM</font> architecture 4 or later, since these processors have instructions to directly access half-word objects in memory. <br />
 </p>
 </dd>
<dt><code>-mno-alignment-traps</code></dt>
<dd> <p> Generate code that assumes that the <font SIZE="-1">MMU</font> will not trap unaligned accesses. This produces better code when the target instruction set does not have half-word memory operations (i.e. implementations prior to ARMv4). </p>
<p> Note that you cannot use this option to access unaligned word objects, since the processor will only fetch one 32-bit aligned object from memory. </p>
<p> The default setting for most targets is <code>-mno-alignment-traps</code>, since this produces better code when there are no half-word memory instructions available. <br />
 </p>
 </dd>
<dt><code>-mshort-load-bytes</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-short-load-words</code></dt>
<dd> <p> These are deprecated aliases for <code>-malignment-traps</code>. <br />
 </p>
 </dd>
<dt><code>-mno-short-load-bytes</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mshort-load-words</code></dt>
<dd> <p> This are deprecated aliases for <code>-mno-alignment-traps</code>. <br />
 </p>
 </dd>
<dt><code>-mbsd</code></dt>
<dd> <p> This option only applies to <font SIZE="-1">RISC</font> iX. Emulate the native BSD-mode compiler. This is the default if <code>-ansi</code> is not specified. <br />
 </p>
 </dd>
<dt><code>-mxopen</code></dt>
<dd> <p> This option only applies to <font SIZE="-1">RISC</font> iX. Emulate the native X/Open-mode compiler. <br />
 </p>
 </dd>
<dt><code>-mno-symrename</code></dt>
<dd> <p> This option only applies to <font SIZE="-1">RISC</font> iX. Do not run the assembler post-processor, <code>symrename</code>, after code has been assembled. Normally it is necessary to modify some of the standard symbols in preparation for linking with the <font SIZE="-1">RISC</font> iX C library; this option suppresses this pass. The post-processor is never run when the compiler is built for cross-compilation. <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>name</i></dt>
<dd> <p> This specifies the name of the target <font SIZE="-1">ARM</font> processor. <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. Permissible names are: <code>arm2</code>, <code>arm250</code>, <code>arm3</code>, <code>arm6</code>, <code>arm60</code>, <code>arm600</code>, <code>arm610</code>, <code>arm620</code>, <code>arm7</code>, <code>arm7m</code>, <code>arm7d</code>, <code>arm7dm</code>, <code>arm7di</code>, <code>arm7dmi</code>, <code>arm70</code>, <code>arm700</code>, <code>arm700i</code>, <code>arm710</code>, <code>arm710c</code>, <code>arm7100</code>, <code>arm7500</code>, <code>arm7500fe</code>, <code>arm7tdmi</code>, <code>arm8</code>, <code>strongarm</code>, <code>strongarm110</code>, <code>strongarm1100</code>, <code>arm8</code>, <code>arm810</code>, <code>arm9</code>, <code>arm9e</code>, <code>arm920</code>, <code>arm920t</code>, <code>arm940t</code>, <code>arm9tdmi</code>, <code>arm10tdmi</code>, <code>arm1020t</code>, <code>xscale</code>. <br />
 </p>
 </dd>
<dt><code>-mtune=</code><i>name</i></dt>
<dd> <p> This option is very similar to the <code>-mcpu=</code> option, except that instead of specifying the actual target processor type, and hence restricting which instructions can be used, it specifies that <font SIZE="-1">GCC</font> should tune the performance of the code as if the target were of the type specified in this option, but still choosing the instructions that it will generate based on the cpu specified by a <code>-mcpu=</code> option. For some <font SIZE="-1">ARM</font> implementations better performance can be obtained by using this option. <br />
 </p>
 </dd>
<dt><code>-march=</code><i>name</i></dt>
<dd> <p> This specifies the name of the target <font SIZE="-1">ARM</font> architecture. <font SIZE="-1">GCC</font> uses this name to determine what kind of instructions it can emit when generating assembly code. This option can be used in conjunction with or instead of the <code>-mcpu=</code> option. Permissible names are: <code>armv2</code>, <code>armv2a</code>, <code>armv3</code>, <code>armv3m</code>, <code>armv4</code>, <code>armv4t</code>, <code>armv5</code>, <code>armv5t</code>, <code>armv5te</code>. <br />
 </p>
 </dd>
<dt><code>-mfpe=</code><i>number</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mfp=</code><i>number</i></dt>
<dd> <p> This specifies the version of the floating point emulation available on the target. Permissible values are 2 and 3. <code>-mfp=</code> is a synonym for <code>-mfpe=</code>, for compatibility with older versions of <font SIZE="-1">GCC</font>. <br />
 </p>
 </dd>
<dt><code>-mstructure-size-boundary=</code><i>n</i></dt>
<dd> <p> The size of all structures and unions will be rounded up to a multiple of the number of bits set by this option. Permissible values are 8 and 32. The default value varies for different toolchains. For the <font SIZE="-1">COFF</font> targeted toolchain the default value is 8. Specifying the larger number can produce faster, more efficient code, but can also increase the size of the program. The two values are potentially incompatible. Code compiled with one value cannot necessarily expect to work with code or libraries compiled with the other value, if they exchange information using structures or unions. <br />
 </p>
 </dd>
<dt><code>-mabort-on-noreturn</code></dt>
<dd> <p> Generate a call to the function <code>&quot;abort&quot;</code> at the end of a <code>&quot;noreturn&quot;</code> function. It will be executed if the function tries to return. <br />
 </p>
 </dd>
<dt><code>-mlong-calls</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-long-calls</code></dt>
<dd> <p> Tells the compiler to perform function calls by first loading the address of the function into a register and then performing a subroutine call on this register. This switch is needed if the target function will lie outside of the 64 megabyte addressing range of the offset based version of subroutine call instruction. </p>
<p> Even if this switch is enabled, not all function calls will be turned into long calls. The heuristic is that static functions, functions which have the <code>short-call</code> attribute, functions that are inside the scope of a <code>#pragma no_long_calls</code> directive and functions whose definitions have already been compiled within the current compilation unit, will not be turned into long calls. The exception to this rule is that weak function definitions, functions with the <code>long-call</code> attribute or the <code>section</code> attribute, and functions that are within the scope of a <code>#pragma long_calls</code> directive, will always be turned into long calls. </p>
<p> This feature is not enabled by default. Specifying <code>-mno-long-calls</code> will restore the default behavior, as will placing the function calls within the scope of a <code>#pragma long_calls_off</code> directive. Note these switches have no effect on how the compiler generates code to handle function calls via function pointers. <br />
 </p>
 </dd>
<dt><code>-mnop-fun-dllimport</code></dt>
<dd> <p> Disable support for the <code>&quot;dllimport&quot;</code> attribute. <br />
 </p>
 </dd>
<dt><code>-msingle-pic-base</code></dt>
<dd> <p> Treat the register used for <font SIZE="-1">PIC</font> addressing as read-only, rather than loading it in the prologue for each function. The run-time system is responsible for initializing this register with an appropriate value before execution begins. <br />
 </p>
 </dd>
<dt><code>-mpic-register=</code><i>reg</i></dt>
<dd> <p> Specify the register to be used for <font SIZE="-1">PIC</font> addressing. The default is R10 unless stack-checking is enabled, when R9 is used. <br />
 </p>
 </dd>
<dt><code>-mpoke-function-name</code></dt>
<dd> <p> Write the name of each function into the text section, directly preceding the function prologue. The generated code is similar to this: </p>
<pre><code>             t0
                 .ascii &quot;arm_poke_function_name&quot;, 0
                 .align
             t1
                 .word 0xff000000 + (t1 - t0)
             arm_poke_function_name
                 mov ip, sp
                 stmfd sp!, {fp, ip, lr, pc}
                 sub fp, ip, #4
</code></pre>
<p> When performing a stack backtrace, code can inspect the value of <code>&quot;pc&quot;</code> stored at <code>&quot;fp + 0&quot;</code>. If the trace function then looks at location <code>&quot;pc - 12&quot;</code> and the top 8 bits are set, then we know that there is a function name embedded immediately preceding this location and has length <code>&quot;((pc[-3]) &amp; 0xff000000)&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mthumb</code></dt>
<dd> <p> Generate code for the 16-bit Thumb instruction set. The default is to use the 32-bit <font SIZE="-1">ARM</font> instruction set. <br />
 </p>
 </dd>
<dt><code>-mtpcs-frame</code></dt>
<dd> <p> Generate a stack frame that is compliant with the Thumb Procedure Call Standard for all non-leaf functions. (A leaf function is one that does not call any other functions.) The default is <code>-mno-tpcs-frame</code>. <br />
 </p>
 </dd>
<dt><code>-mtpcs-leaf-frame</code></dt>
<dd> <p> Generate a stack frame that is compliant with the Thumb Procedure Call Standard for all leaf functions. (A leaf function is one that does not call any other functions.) The default is <code>-mno-apcs-leaf-frame</code>. <br />
 </p>
 </dd>
<dt><code>-mcallee-super-interworking</code></dt>
<dd> <p> Gives all externally visible functions in the file being compiled an <font SIZE="-1">ARM</font> instruction set header which switches to Thumb mode before executing the rest of the function. This allows these functions to be called from non-interworking code. <br />
 </p>
 </dd>
<dt><code>-mcaller-super-interworking</code></dt>
<dd> <p> Allows calls via function pointers (including virtual functions) to execute correctly regardless of whether the target code has been compiled for interworking or not. There is a small overhead in the cost of executing a function pointer if this option is enabled. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>MN10200</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for Matsushita <font SIZE="-1">MN10200</font> architectures: <br />
 </p>
<dl>
<dt><code>-mrelax</code></dt>
<dd> <p> Indicate to the linker that it should perform a relaxation optimization pass to shorten branches, calls and absolute memory addresses. This option only has an effect when used on the command line for the final link step. </p>
<p> This option makes symbolic debugging impossible. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>MN10300</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for Matsushita <font SIZE="-1">MN10300</font> architectures: <br />
 </p>
<dl>
<dt><code>-mmult-bug</code></dt>
<dd> <p> Generate code to avoid bugs in the multiply instructions for the <font SIZE="-1">MN10300</font> processors. This is the default. <br />
 </p>
 </dd>
<dt><code>-mno-mult-bug</code></dt>
<dd> <p> Do not generate code to avoid bugs in the multiply instructions for the <font SIZE="-1">MN10300</font> processors. <br />
 </p>
 </dd>
<dt><code>-mam33</code></dt>
<dd> <p> Generate code which uses features specific to the <font SIZE="-1">AM33</font> processor. <br />
 </p>
 </dd>
<dt><code>-mno-am33</code></dt>
<dd> <p> Do not generate code which uses features specific to the <font SIZE="-1">AM33</font> processor. This is the default. <br />
 </p>
 </dd>
<dt><code>-mno-crt0</code></dt>
<dd> <p> Do not link in the C run-time initialization object file. <br />
 </p>
 </dd>
<dt><code>-mrelax</code></dt>
<dd> <p> Indicate to the linker that it should perform a relaxation optimization pass to shorten branches, calls and absolute memory addresses. This option only has an effect when used on the command line for the final link step. </p>
<p> This option makes symbolic debugging impossible. </p>
 </dd></dl>
<p> <i>M32R/D Options</i>  </p>
<p> These <code>-m</code> options are defined for Mitsubishi M32R/D architectures: <br />
 </p>
<dl>
<dt><code>-m32rx</code></dt>
<dd> <p> Generate code for the M32R/X. <br />
 </p>
 </dd>
<dt><code>-m32r</code></dt>
<dd> <p> Generate code for the M32R. This is the default. <br />
 </p>
 </dd>
<dt><code>-mcode-model=small</code></dt>
<dd> <p> Assume all objects live in the lower 16MB of memory (so that their addresses can be loaded with the <code>&quot;ld24&quot;</code> instruction), and assume all subroutines are reachable with the <code>&quot;bl&quot;</code> instruction. This is the default. </p>
<p> The addressability of a particular object can be set with the <code>&quot;model&quot;</code> attribute. <br />
 </p>
 </dd>
<dt><code>-mcode-model=medium</code></dt>
<dd> <p> Assume objects may be anywhere in the 32-bit address space (the compiler will generate <code>&quot;seth/add3&quot;</code> instructions to load their addresses), and assume all subroutines are reachable with the <code>&quot;bl&quot;</code> instruction. <br />
 </p>
 </dd>
<dt><code>-mcode-model=large</code></dt>
<dd> <p> Assume objects may be anywhere in the 32-bit address space (the compiler will generate <code>&quot;seth/add3&quot;</code> instructions to load their addresses), and assume subroutines may not be reachable with the <code>&quot;bl&quot;</code> instruction (the compiler will generate the much slower <code>&quot;seth/add3/jl&quot;</code> instruction sequence). <br />
 </p>
 </dd>
<dt><code>-msdata=none</code></dt>
<dd> <p> Disable use of the small data area. Variables will be put into one of <code>.data</code>, <code>bss</code>, or <code>.rodata</code> (unless the <code>&quot;section&quot;</code> attribute has been specified). This is the default. </p>
<p> The small data area consists of sections <code>.sdata</code> and <code>.sbss</code>. Objects may be explicitly put in the small data area with the <code>&quot;section&quot;</code> attribute using one of these sections. <br />
 </p>
 </dd>
<dt><code>-msdata=sdata</code></dt>
<dd> <p> Put small global and static data in the small data area, but do not generate special code to reference them. <br />
 </p>
 </dd>
<dt><code>-msdata=use</code></dt>
<dd> <p> Put small global and static data in the small data area, and generate special instructions to reference them. <br />
 </p>
 </dd>
<dt><code>-G</code><i>num</i></dt>
<dd> <p> Put global and static objects less than or equal to <i>num</i> bytes into the small data or bss sections instead of the normal data or bss sections. The default value of <i>num</i> is 8. The <code>-msdata</code> option must be set to one of <code>sdata</code> or <code>use</code> for this option to have any effect. </p>
<p> All modules should be compiled with the same <code>-G</code> <i>num</i> value. Compiling with different values of <i>num</i> may or may not work; if it doesn&#8217;t the linker will give an error message---incorrect code will not be generated. </p>
 </dd></dl>
<p> <i>M88K Options</i>  </p>
<p> These <code>-m</code> options are defined for Motorola 88k architectures: <br />
 </p>
<dl>
<dt><code>-m88000</code></dt>
<dd> <p> Generate code that works well on both the m88100 and the m88110. <br />
 </p>
 </dd>
<dt><code>-m88100</code></dt>
<dd> <p> Generate code that works best for the m88100, but that also runs on the m88110. <br />
 </p>
 </dd>
<dt><code>-m88110</code></dt>
<dd> <p> Generate code that works best for the m88110, and may not run on the m88100. <br />
 </p>
 </dd>
<dt><code>-mbig-pic</code></dt>
<dd> <p> Obsolete option to be removed from the next revision. Use <code>-fPIC</code>. <br />
 </p>
 </dd>
<dt><code>-midentify-revision</code></dt>
<dd> <p> Include an <code>&quot;ident&quot;</code> directive in the assembler output recording the source file name, compiler name and version, timestamp, and compilation flags used. <br />
 </p>
 </dd>
<dt><code>-mno-underscores</code></dt>
<dd> <p> In assembler output, emit symbol names without adding an underscore character at the beginning of each name. The default is to use an underscore as prefix on each name. <br />
 </p>
 </dd>
<dt><code>-mocs-debug-info</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-ocs-debug-info</code></dt>
<dd> <p> Include (or omit) additional debugging information (about registers used in each stack frame) as specified in the 88open Object Compatibility Standard, ``<font SIZE="-1">OCS</font>&#8216;&#8216;. This extra information allows debugging of code that has had the frame pointer eliminated. The default for <font SIZE="-1">DG/UX</font>, SVr4, and Delta 88 SVr3.2 is to include this information; other 88k configurations omit this information by default. <br />
 </p>
 </dd>
<dt><code>-mocs-frame-position</code></dt>
<dd> <p> When emitting <font SIZE="-1">COFF</font> debugging information for automatic variables and parameters stored on the stack, use the offset from the canonical frame address, which is the stack pointer (register 31) on entry to the function. The <font SIZE="-1">DG/UX</font>, SVr4, Delta88 SVr3.2, and <font SIZE="-1">BCS</font> configurations use <code>-mocs-frame-position</code>; other 88k configurations have the default <code>-mno-ocs-frame-position</code>. <br />
 </p>
 </dd>
<dt><code>-mno-ocs-frame-position</code></dt>
<dd> <p> When emitting <font SIZE="-1">COFF</font> debugging information for automatic variables and parameters stored on the stack, use the offset from the frame pointer register (register 30). When this option is in effect, the frame pointer is not eliminated when debugging information is selected by the -g switch. <br />
 </p>
 </dd>
<dt><code>-moptimize-arg-area</code></dt>
<dd> <p> Save space by reorganizing the stack frame. This option generates code that does not agree with the 88open specifications, but uses less memory. <br />
 </p>
 </dd>
<dt><code>-mno-optimize-arg-area</code></dt>
<dd> <p> Do not reorganize the stack frame to save space. This is the default. The generated conforms to the specification, but uses more memory. <br />
 </p>
 </dd>
<dt><code>-mshort-data-</code><i>num</i></dt>
<dd> <p> Generate smaller data references by making them relative to <code>&quot;r0&quot;</code>, which allows loading a value using a single instruction (rather than the usual two). You control which data references are affected by specifying <i>num</i> with this option. For example, if you specify <code>-mshort-data-512</code>, then the data references affected are those involving displacements of less than 512 bytes. <code>-mshort-data-</code><i>num</i> is not effective for <i>num</i> greater than 64k. <br />
 </p>
 </dd>
<dt><code>-mserialize-volatile</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-serialize-volatile</code></dt>
<dd> <p> Do, or don&#8217;t, generate code to guarantee sequential consistency of volatile memory references. By default, consistency is guaranteed. </p>
<p> The order of memory references made by the <font SIZE="-1">MC88110</font> processor does not always match the order of the instructions requesting those references. In particular, a load instruction may execute before a preceding store instruction. Such reordering violates sequential consistency of volatile memory references, when there are multiple processors. When consistency must be guaranteed, <font SIZE="-1">GCC</font> generates special instructions, as needed, to force execution in the proper order. </p>
<p> The <font SIZE="-1">MC88100</font> processor does not reorder memory references and so always provides sequential consistency. However, by default, <font SIZE="-1">GCC</font> generates the special instructions to guarantee consistency even when you use <code>-m88100</code>, so that the code may be run on an <font SIZE="-1">MC88110</font> processor. If you intend to run your code only on the <font SIZE="-1">MC88100</font> processor, you may use <code>-mno-serialize-volatile</code>. </p>
<p> The extra code generated to guarantee consistency may affect the performance of your application. If you know that you can safely forgo this guarantee, you may use <code>-mno-serialize-volatile</code>. <br />
 </p>
 </dd>
<dt><code>-msvr4</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msvr3</code></dt>
<dd> <p> Turn on (<code>-msvr4</code>) or off (<code>-msvr3</code>) compiler extensions related to System V release 4 (SVr4). This controls the following: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>1.</dt>
<dd> <p> Which variant of the assembler syntax to emit. <br />
 </p>
 </dd>
<dt>2.</dt>
<dd> <p> <code>-msvr4</code> makes the C preprocessor recognize <code>#pragma weak</code> that is used on System V release 4. <br />
 </p>
 </dd>
<dt>3.</dt>
<dd> <p> <code>-msvr4</code> makes <font SIZE="-1">GCC</font> issue additional declaration directives used in SVr4. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> <code>-msvr4</code> is the default for the m88k-motorola-sysv4 and m88k-dg-dgux m88k configurations. <code>-msvr3</code> is the default for all other m88k configurations. </p>
 </dd></dl>
<p> <br />
 </p>
<dt><code>-mversion-03.00</code></dt>
<dd> <p> This option is obsolete, and is ignored. <br />
 </p>
 </dd>
<dt><code>-mno-check-zero-division</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mcheck-zero-division</code></dt>
<dd> <p> Do, or don&#8217;t, generate code to guarantee that integer division by zero will be detected. By default, detection is guaranteed. </p>
<p> Some models of the <font SIZE="-1">MC88100</font> processor fail to trap upon integer division by zero under certain conditions. By default, when compiling code that might be run on such a processor, <font SIZE="-1">GCC</font> generates code that explicitly checks for zero-valued divisors and traps with exception number 503 when one is detected. Use of <code>-mno-check-zero-division</code> suppresses such checking for code generated to run on an <font SIZE="-1">MC88100</font> processor. </p>
<p> <font SIZE="-1">GCC</font> assumes that the <font SIZE="-1">MC88110</font> processor correctly detects all instances of integer division by zero. When <code>-m88110</code> is specified, no explicit checks for zero-valued divisors are generated, and both <code>-mcheck-zero-division</code> and <code>-mno-check-zero-division</code> are ignored. <br />
 </p>
 </dd>
<dt><code>-muse-div-instruction</code></dt>
<dd> <p> Use the div instruction for signed integer division on the <font SIZE="-1">MC88100</font> processor. By default, the div instruction is not used. </p>
<p> On the <font SIZE="-1">MC88100</font> processor the signed integer division instruction div) traps to the operating system on a negative operand. The operating system transparently completes the operation, but at a large cost in execution time. By default, when compiling code that might be run on an <font SIZE="-1">MC88100</font> processor, <font SIZE="-1">GCC</font> emulates signed integer division using the unsigned integer division instruction divu), thereby avoiding the large penalty of a trap to the operating system. Such emulation has its own, smaller, execution cost in both time and space. To the extent that your code&#8217;s important signed integer division operations are performed on two nonnegative operands, it may be desirable to use the div instruction directly. </p>
<p> On the <font SIZE="-1">MC88110</font> processor the div instruction (also known as the divs instruction) processes negative operands without trapping to the operating system. When <code>-m88110</code> is specified, <code>-muse-div-instruction</code> is ignored, and the div instruction is used for signed integer division. </p>
<p> Note that the result of dividing <code>&quot;INT_MIN&quot;</code> by -1 is undefined. In particular, the behavior of such a division with and without <code>-muse-div-instruction</code> may differ. <br />
 </p>
 </dd>
<dt><code>-mtrap-large-shift</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mhandle-large-shift</code></dt>
<dd> <p> Include code to detect bit-shifts of more than 31 bits; respectively, trap such shifts or emit code to handle them properly. By default <font SIZE="-1">GCC</font> makes no special provision for large bit shifts. <br />
 </p>
 </dd>
<dt><code>-mwarn-passed-structs</code></dt>
<dd> <p> Warn when a function passes a struct as an argument or result. Structure-passing conventions have changed during the evolution of the C language, and are often the source of portability problems. By default, <font SIZE="-1">GCC</font> issues no such warning. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>IBM</i></font><i> </i><font SIZE="-1"><i>RS/6000</i></font><i> and PowerPC Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">IBM</font> <font SIZE="-1">RS/6000</font> and PowerPC: <br />
 </p>
<dl>
<dt><code>-mpower</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-power</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpower2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-power2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpowerpc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-powerpc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpowerpc-gpopt</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-powerpc-gpopt</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpowerpc-gfxopt</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-powerpc-gfxopt</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpowerpc64</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-powerpc64</code></dt>
<dd> <p> <font SIZE="-1">GCC</font> supports two related instruction set architectures for the <font SIZE="-1">RS/6000</font> and PowerPC. The <i></i><font SIZE="-1"><i>POWER</i></font><i></i> instruction set are those instructions supported by the <code>rios</code> chip set used in the original <font SIZE="-1">RS/6000</font> systems and the <i>PowerPC</i> instruction set is the architecture of the Motorola MPC5xx, MPC6xx, MPC8xx microprocessors, and the <font SIZE="-1">IBM</font> 4xx microprocessors. </p>
<p> Neither architecture is a subset of the other. However there is a large common subset of instructions supported by both. An <font SIZE="-1">MQ</font> register is included in processors supporting the <font SIZE="-1">POWER</font> architecture. </p>
<p> You use these options to specify which instructions are available on the processor you are using. The default value of these options is determined when configuring <font SIZE="-1">GCC</font>. Specifying the <code>-mcpu=</code><i>cpu_type</i> overrides the specification of these options. We recommend you use the <code>-mcpu=</code><i>cpu_type</i> option rather than the options listed above. </p>
<p> The <code>-mpower</code> option allows <font SIZE="-1">GCC</font> to generate instructions that are found only in the <font SIZE="-1">POWER</font> architecture and to use the <font SIZE="-1">MQ</font> register. Specifying <code>-mpower2</code> implies <code>-power</code> and also allows <font SIZE="-1">GCC</font> to generate instructions that are present in the <font SIZE="-1">POWER2</font> architecture but not the original <font SIZE="-1">POWER</font> architecture. </p>
<p> The <code>-mpowerpc</code> option allows <font SIZE="-1">GCC</font> to generate instructions that are found only in the 32-bit subset of the PowerPC architecture. Specifying <code>-mpowerpc-gpopt</code> implies <code>-mpowerpc</code> and also allows <font SIZE="-1">GCC</font> to use the optional PowerPC architecture instructions in the General Purpose group, including floating-point square root. Specifying <code>-mpowerpc-gfxopt</code> implies <code>-mpowerpc</code> and also allows <font SIZE="-1">GCC</font> to use the optional PowerPC architecture instructions in the Graphics group, including floating-point select. </p>
<p> The <code>-mpowerpc64</code> option allows <font SIZE="-1">GCC</font> to generate the additional 64-bit instructions that are found in the full PowerPC64 architecture and to treat GPRs as 64-bit, doubleword quantities. <font SIZE="-1">GCC</font> defaults to <code>-mno-powerpc64</code>. </p>
<p> If you specify both <code>-mno-power</code> and <code>-mno-powerpc</code>, <font SIZE="-1">GCC</font> will use only the instructions in the common subset of both architectures plus some special <font SIZE="-1">AIX</font> common-mode calls, and will not use the <font SIZE="-1">MQ</font> register. Specifying both <code>-mpower</code> and <code>-mpowerpc</code> permits <font SIZE="-1">GCC</font> to use any instruction from either architecture and to allow use of the <font SIZE="-1">MQ</font> register; specify this for the Motorola <font SIZE="-1">MPC601</font>. <br />
 </p>
 </dd>
<dt><code>-mnew-mnemonics</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mold-mnemonics</code></dt>
<dd> <p> Select which mnemonics to use in the generated assembler code. With <code>-mnew-mnemonics</code>, <font SIZE="-1">GCC</font> uses the assembler mnemonics defined for the PowerPC architecture. With <code>-mold-mnemonics</code> it uses the assembler mnemonics defined for the <font SIZE="-1">POWER</font> architecture. Instructions defined in only one architecture have only one mnemonic; <font SIZE="-1">GCC</font> uses that mnemonic irrespective of which of these options is specified. </p>
<p> <font SIZE="-1">GCC</font> defaults to the mnemonics appropriate for the architecture in use. Specifying <code>-mcpu=</code><i>cpu_type</i> sometimes overrides the value of these option. Unless you are building a cross-compiler, you should normally not specify either <code>-mnew-mnemonics</code> or <code>-mold-mnemonics</code>, but should instead accept the default. <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>cpu_type</i></dt>
<dd> <p> Set architecture type, register usage, choice of mnemonics, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>rios</code>, <code>rios1</code>, <code>rsc</code>, <code>rios2</code>, <code>rs64a</code>, <code>601</code>, <code>602</code>, <code>603</code>, <code>603e</code>, <code>604</code>, <code>604e</code>, <code>620</code>, <code>630</code>, <code>740</code>, <code>7400</code>, <code>7450</code>, <code>750</code>, <code>power</code>, <code>power2</code>, <code>powerpc</code>, <code>403</code>, <code>505</code>, <code>801</code>, <code>821</code>, <code>823</code>, and <code>860</code> and <code>common</code>. </p>
<p> <code>-mcpu=common</code> selects a completely generic processor. Code generated under this option will run on any <font SIZE="-1">POWER</font> or PowerPC processor. <font SIZE="-1">GCC</font> will use only the instructions in the common subset of both architectures, and will not use the <font SIZE="-1">MQ</font> register. <font SIZE="-1">GCC</font> assumes a generic processor model for scheduling purposes. </p>
<p> <code>-mcpu=power</code>, <code>-mcpu=power2</code>, <code>-mcpu=powerpc</code>, and <code>-mcpu=powerpc64</code> specify generic <font SIZE="-1">POWER</font>, <font SIZE="-1">POWER2</font>, pure 32-bit PowerPC (i.e., not <font SIZE="-1">MPC601</font>), and 64-bit PowerPC architecture machine types, with an appropriate, generic processor model assumed for scheduling purposes. </p>
<p> The other options specify a specific processor. Code generated under those options will run best on that processor, and may not run at all on others. </p>
<p> The <code>-mcpu</code> options automatically enable or disable other <code>-m</code> options as follows: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>common</code></dt>
<dd> <p> <code>-mno-power</code>, <code>-mno-powerc</code> <br />
 </p>
 </dd>
<dt><code>power</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>power2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>rios1</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>rios2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>rsc</code></dt>
<dd> <p> <code>-mpower</code>, <code>-mno-powerpc</code>, <code>-mno-new-mnemonics</code> <br />
 </p>
 </dd>
<dt><code>powerpc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>rs64a</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>602</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>603</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>603e</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>604</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>620</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>630</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>740</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>7400</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>7450</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>750</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>505</code></dt>
<dd> <p> <code>-mno-power</code>, <code>-mpowerpc</code>, <code>-mnew-mnemonics</code> <br />
 </p>
 </dd>
<dt><code>601</code></dt>
<dd> <p> <code>-mpower</code>, <code>-mpowerpc</code>, <code>-mnew-mnemonics</code> <br />
 </p>
 </dd>
<dt><code>403</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>821</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>860</code></dt>
<dd> <p> <code>-mno-power</code>, <code>-mpowerpc</code>, <code>-mnew-mnemonics</code>, <code>-msoft-float</code> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-mtune=</code><i>cpu_type</i></dt>
<dd> <p> Set the instruction scheduling parameters for machine type <i>cpu_type</i>, but do not set the architecture type, register usage, or choice of mnemonics, as <code>-mcpu=</code><i>cpu_type</i> would. The same values for <i>cpu_type</i> are used for <code>-mtune</code> as for <code>-mcpu</code>. If both are specified, the code generated will use the architecture, registers, and mnemonics set by <code>-mcpu</code>, but the scheduling parameters set by <code>-mtune</code>. <br />
 </p>
 </dd>
<dt><code>-maltivec</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-altivec</code></dt>
<dd> <p> These switches enable or disable the use of built-in functions that allow access to the AltiVec instruction set. You may also need to set <code>-mabi=altivec</code> to adjust the current <font SIZE="-1">ABI</font> with AltiVec <font SIZE="-1">ABI</font> enhancements. <br />
 </p>
 </dd>
<dt><code>-mfull-toc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fp-in-toc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-sum-in-toc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mminimal-toc</code></dt>
<dd> <p> Modify generation of the <font SIZE="-1">TOC</font> (Table Of Contents), which is created for every executable file. The <code>-mfull-toc</code> option is selected by default. In that case, <font SIZE="-1">GCC</font> will allocate at least one <font SIZE="-1">TOC</font> entry for each unique non-automatic variable reference in your program. <font SIZE="-1">GCC</font> will also place floating-point constants in the <font SIZE="-1">TOC</font>. However, only 16,384 entries are available in the <font SIZE="-1">TOC</font>. </p>
<p> If you receive a linker error message that saying you have overflowed the available <font SIZE="-1">TOC</font> space, you can reduce the amount of <font SIZE="-1">TOC</font> space used with the <code>-mno-fp-in-toc</code> and <code>-mno-sum-in-toc</code> options. <code>-mno-fp-in-toc</code> prevents <font SIZE="-1">GCC</font> from putting floating-point constants in the <font SIZE="-1">TOC</font> and <code>-mno-sum-in-toc</code> forces <font SIZE="-1">GCC</font> to generate code to calculate the sum of an address and a constant at run-time instead of putting that sum into the <font SIZE="-1">TOC</font>. You may specify one or both of these options. Each causes <font SIZE="-1">GCC</font> to produce very slightly slower and larger code at the expense of conserving <font SIZE="-1">TOC</font> space. </p>
<p> If you still run out of space in the <font SIZE="-1">TOC</font> even when you specify both of these options, specify <code>-mminimal-toc</code> instead. This option causes <font SIZE="-1">GCC</font> to make only one <font SIZE="-1">TOC</font> entry for every file. When you specify this option, <font SIZE="-1">GCC</font> will produce code that is slower and larger but which uses extremely little <font SIZE="-1">TOC</font> space. You may wish to use this option only on files that contain less frequently executed code. <br />
 </p>
 </dd>
<dt><code>-maix64</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-maix32</code></dt>
<dd> <p> Enable 64-bit <font SIZE="-1">AIX</font> <font SIZE="-1">ABI</font> and calling convention: 64-bit pointers, 64-bit <code>&quot;long&quot;</code> type, and the infrastructure needed to support them. Specifying <code>-maix64</code> implies <code>-mpowerpc64</code> and <code>-mpowerpc</code>, while <code>-maix32</code> disables the 64-bit <font SIZE="-1">ABI</font> and implies <code>-mno-powerpc64</code>. <font SIZE="-1">GCC</font> defaults to <code>-maix32</code>. <br />
 </p>
 </dd>
<dt><code>-mxl-call</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-xl-call</code></dt>
<dd> <p> On <font SIZE="-1">AIX</font>, pass floating-point arguments to prototyped functions beyond the register save area (<font SIZE="-1">RSA</font>) on the stack in addition to argument FPRs. The <font SIZE="-1">AIX</font> calling convention was extended but not initially documented to handle an obscure K&amp;R C case of calling a function that takes the address of its arguments with fewer arguments than declared. <font SIZE="-1">AIX</font> <font SIZE="-1">XL</font> compilers access floating point arguments which do not fit in the <font SIZE="-1">RSA</font> from the stack when a subroutine is compiled without optimization. Because always storing floating-point arguments on the stack is inefficient and rarely needed, this option is not enabled by default and only is necessary when calling subroutines compiled by <font SIZE="-1">AIX</font> <font SIZE="-1">XL</font> compilers without optimization. <br />
 </p>
 </dd>
<dt><code>-mpe</code></dt>
<dd> <p> Support <i></i><font SIZE="-1"><i>IBM</i></font><i> </i><font SIZE="-1"><i>RS/6000</i></font><i> </i><font SIZE="-1"><i>SP</i></font><i></i> <i>Parallel Environment</i> (<font SIZE="-1">PE</font>). Link an application written to use message passing with special startup code to enable the application to run. The system must have <font SIZE="-1">PE</font> installed in the standard location (<i>/usr/lpp/ppe.poe/</i>), or the <i>specs</i> file must be overridden with the <code>-specs=</code> option to specify the appropriate directory location. The Parallel Environment does not support threads, so the <code>-mpe</code> option and the <code>-pthread</code> option are incompatible. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mhard-float</code></dt>
<dd> <p> Generate code that does not use (uses) the floating-point register set. Software floating point emulation is provided if you use the <code>-msoft-float</code> option, and pass the option to <font SIZE="-1">GCC</font> when linking. <br />
 </p>
 </dd>
<dt><code>-mmultiple</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-multiple</code></dt>
<dd> <p> Generate code that uses (does not use) the load multiple word instructions and the store multiple word instructions. These instructions are generated by default on <font SIZE="-1">POWER</font> systems, and not generated on PowerPC systems. Do not use <code>-mmultiple</code> on little endian PowerPC systems, since those instructions do not work when the processor is in little endian mode. The exceptions are <font SIZE="-1">PPC740</font> and <font SIZE="-1">PPC750</font> which permit the instructions usage in little endian mode. <br />
 </p>
 </dd>
<dt><code>-mstring</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-string</code></dt>
<dd> <p> Generate code that uses (does not use) the load string instructions and the store string word instructions to save multiple registers and do small block moves. These instructions are generated by default on <font SIZE="-1">POWER</font> systems, and not generated on PowerPC systems. Do not use <code>-mstring</code> on little endian PowerPC systems, since those instructions do not work when the processor is in little endian mode. The exceptions are <font SIZE="-1">PPC740</font> and <font SIZE="-1">PPC750</font> which permit the instructions usage in little endian mode. <br />
 </p>
 </dd>
<dt><code>-mupdate</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-update</code></dt>
<dd> <p> Generate code that uses (does not use) the load or store instructions that update the base register to the address of the calculated memory location. These instructions are generated by default. If you use <code>-mno-update</code>, there is a small window between the time that the stack pointer is updated and the address of the previous frame is stored, which means code that walks the stack frame across interrupts or signals may get corrupted data. <br />
 </p>
 </dd>
<dt><code>-mfused-madd</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fused-madd</code></dt>
<dd> <p> Generate code that uses (does not use) the floating point multiply and accumulate instructions. These instructions are generated by default if hardware floating is used. <br />
 </p>
 </dd>
<dt><code>-mno-bit-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mbit-align</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems do not (do) force structures and unions that contain bit-fields to be aligned to the base type of the bit-field. </p>
<p> For example, by default a structure containing nothing but 8 <code>&quot;unsigned&quot;</code> bit-fields of length 1 would be aligned to a 4 byte boundary and have a size of 4 bytes. By using <code>-mno-bit-align</code>, the structure would be aligned to a 1 byte boundary and be one byte in size. <br />
 </p>
 </dd>
<dt><code>-mno-strict-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mstrict-align</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems do not (do) assume that unaligned memory references will be handled by the system. <br />
 </p>
 </dd>
<dt><code>-mrelocatable</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-relocatable</code></dt>
<dd> <p> On embedded PowerPC systems generate code that allows (does not allow) the program to be relocated to a different address at runtime. If you use <code>-mrelocatable</code> on any module, all objects linked together must be compiled with <code>-mrelocatable</code> or <code>-mrelocatable-lib</code>. <br />
 </p>
 </dd>
<dt><code>-mrelocatable-lib</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-relocatable-lib</code></dt>
<dd> <p> On embedded PowerPC systems generate code that allows (does not allow) the program to be relocated to a different address at runtime. Modules compiled with <code>-mrelocatable-lib</code> can be linked with either modules compiled without <code>-mrelocatable</code> and <code>-mrelocatable-lib</code> or with modules compiled with the <code>-mrelocatable</code> options. <br />
 </p>
 </dd>
<dt><code>-mno-toc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mtoc</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems do not (do) assume that register 2 contains a pointer to a global area pointing to the addresses used in the program. <br />
 </p>
 </dd>
<dt><code>-mlittle</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code for the processor in little endian mode. The <code>-mlittle-endian</code> option is the same as <code>-mlittle</code>. <br />
 </p>
 </dd>
<dt><code>-mbig</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mbig-endian</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code for the processor in big endian mode. The <code>-mbig-endian</code> option is the same as <code>-mbig</code>. <br />
 </p>
 </dd>
<dt><code>-mcall-sysv</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code using calling conventions that adheres to the March 1995 draft of the System V Application Binary Interface, PowerPC processor supplement. This is the default unless you configured <font SIZE="-1">GCC</font> using <code>powerpc-*-eabiaix</code>. <br />
 </p>
 </dd>
<dt><code>-mcall-sysv-eabi</code></dt>
<dd> <p> Specify both <code>-mcall-sysv</code> and <code>-meabi</code> options. <br />
 </p>
 </dd>
<dt><code>-mcall-sysv-noeabi</code></dt>
<dd> <p> Specify both <code>-mcall-sysv</code> and <code>-mno-eabi</code> options. <br />
 </p>
 </dd>
<dt><code>-mcall-aix</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code using calling conventions that are similar to those used on <font SIZE="-1">AIX</font>. This is the default if you configured <font SIZE="-1">GCC</font> using <code>powerpc-*-eabiaix</code>. <br />
 </p>
 </dd>
<dt><code>-mcall-solaris</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code for the Solaris operating system. <br />
 </p>
 </dd>
<dt><code>-mcall-linux</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code for the Linux-based <font SIZE="-1">GNU</font> system. <br />
 </p>
 </dd>
<dt><code>-mcall-gnu</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code for the Hurd-based <font SIZE="-1">GNU</font> system. <br />
 </p>
 </dd>
<dt><code>-mcall-netbsd</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems compile code for the NetBSD operating system. <br />
 </p>
 </dd>
<dt><code>-maix-struct-return</code></dt>
<dd> <p> Return all structures in memory (as specified by the <font SIZE="-1">AIX</font> <font SIZE="-1">ABI</font>). <br />
 </p>
 </dd>
<dt><code>-msvr4-struct-return</code></dt>
<dd> <p> Return structures smaller than 8 bytes in registers (as specified by the <font SIZE="-1">SVR4</font> <font SIZE="-1">ABI</font>). <br />
 </p>
 </dd>
<dt><code>-mabi=altivec</code></dt>
<dd> <p> Extend the current <font SIZE="-1">ABI</font> with AltiVec <font SIZE="-1">ABI</font> extensions. This does not change the default <font SIZE="-1">ABI</font>, instead it adds the AltiVec <font SIZE="-1">ABI</font> extensions to the current <font SIZE="-1">ABI</font>. <br />
 </p>
 </dd>
<dt><code>-mabi=no-altivec</code></dt>
<dd> <p> Disable AltiVec <font SIZE="-1">ABI</font> extensions for the current <font SIZE="-1">ABI</font>. <br />
 </p>
 </dd>
<dt><code>-mprototype</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-prototype</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems assume that all calls to variable argument functions are properly prototyped. Otherwise, the compiler must insert an instruction before every non prototyped call to set or clear bit 6 of the condition code register (<i></i><font SIZE="-1"><i>CR</i></font><i></i>) to indicate whether floating point values were passed in the floating point registers in case the function takes a variable arguments. With <code>-mprototype</code>, only calls to prototyped variable argument functions will set or clear the bit. <br />
 </p>
 </dd>
<dt><code>-msim</code></dt>
<dd> <p> On embedded PowerPC systems, assume that the startup module is called <i>sim-crt0.o</i> and that the standard C libraries are <i>libsim.a</i> and <i>libc.a</i>. This is the default for <code>powerpc-*-eabisim</code>. configurations. <br />
 </p>
 </dd>
<dt><code>-mmvme</code></dt>
<dd> <p> On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libmvme.a</i> and <i>libc.a</i>. <br />
 </p>
 </dd>
<dt><code>-mads</code></dt>
<dd> <p> On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libads.a</i> and <i>libc.a</i>. <br />
 </p>
 </dd>
<dt><code>-myellowknife</code></dt>
<dd> <p> On embedded PowerPC systems, assume that the startup module is called <i>crt0.o</i> and the standard C libraries are <i>libyk.a</i> and <i>libc.a</i>. <br />
 </p>
 </dd>
<dt><code>-mvxworks</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems, specify that you are compiling for a VxWorks system. <br />
 </p>
 </dd>
<dt><code>-memb</code></dt>
<dd> <p> On embedded PowerPC systems, set the <i></i><font SIZE="-1"><i>PPC_EMB</i></font><i></i> bit in the <font SIZE="-1">ELF</font> flags header to indicate that <code>eabi</code> extended relocations are used. <br />
 </p>
 </dd>
<dt><code>-meabi</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-eabi</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems do (do not) adhere to the Embedded Applications Binary Interface (eabi) which is a set of modifications to the System V.4 specifications. Selecting <code>-meabi</code> means that the stack is aligned to an 8 byte boundary, a function <code>&quot;__eabi&quot;</code> is called to from <code>&quot;main&quot;</code> to set up the eabi environment, and the <code>-msdata</code> option can use both <code>&quot;r2&quot;</code> and <code>&quot;r13&quot;</code> to point to two separate small data areas. Selecting <code>-mno-eabi</code> means that the stack is aligned to a 16 byte boundary, do not call an initialization function from <code>&quot;main&quot;</code>, and the <code>-msdata</code> option will only use <code>&quot;r13&quot;</code> to point to a single small data area. The <code>-meabi</code> option is on by default if you configured <font SIZE="-1">GCC</font> using one of the <code>powerpc*-*-eabi*</code> options. <br />
 </p>
 </dd>
<dt><code>-msdata=eabi</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems, put small initialized <code>&quot;const&quot;</code> global and static data in the <code>.sdata2</code> section, which is pointed to by register <code>&quot;r2&quot;</code>. Put small initialized non-<code>&quot;const&quot;</code> global and static data in the <code>.sdata</code> section, which is pointed to by register <code>&quot;r13&quot;</code>. Put small uninitialized global and static data in the <code>.sbss</code> section, which is adjacent to the <code>.sdata</code> section. The <code>-msdata=eabi</code> option is incompatible with the <code>-mrelocatable</code> option. The <code>-msdata=eabi</code> option also sets the <code>-memb</code> option. <br />
 </p>
 </dd>
<dt><code>-msdata=sysv</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems, put small global and static data in the <code>.sdata</code> section, which is pointed to by register <code>&quot;r13&quot;</code>. Put small uninitialized global and static data in the <code>.sbss</code> section, which is adjacent to the <code>.sdata</code> section. The <code>-msdata=sysv</code> option is incompatible with the <code>-mrelocatable</code> option. <br />
 </p>
 </dd>
<dt><code>-msdata=default</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msdata</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems, if <code>-meabi</code> is used, compile code the same as <code>-msdata=eabi</code>, otherwise compile code the same as <code>-msdata=sysv</code>. <br />
 </p>
 </dd>
<dt><code>-msdata-data</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems, put small global and static data in the <code>.sdata</code> section. Put small uninitialized global and static data in the <code>.sbss</code> section. Do not use register <code>&quot;r13&quot;</code> to address small data however. This is the default behavior unless other <code>-msdata</code> options are used. <br />
 </p>
 </dd>
<dt><code>-msdata=none</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-sdata</code></dt>
<dd> <p> On embedded PowerPC systems, put all initialized global and static data in the <code>.data</code> section, and all uninitialized data in the <code>.bss</code> section. <br />
 </p>
 </dd>
<dt><code>-G</code><i>num</i></dt>
<dd> <p> On embedded PowerPC systems, put global and static items less than or equal to <i>num</i> bytes into the small data or bss sections instead of the normal data or bss section. By default, <i>num</i> is 8. The <code>-G</code> <i>num</i> switch is also passed to the linker. All modules should be compiled with the same <code>-G</code> <i>num</i> value. <br />
 </p>
 </dd>
<dt><code>-mregnames</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-regnames</code></dt>
<dd> <p> On System V.4 and embedded PowerPC systems do (do not) emit register names in the assembly language output using symbolic forms. <br />
 </p>
 </dd>
<dt><code>-pthread</code></dt>
<dd> <p> Adds support for multithreading with the <i>pthreads</i> library. This option sets flags for both the preprocessor and linker. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>IBM</i></font><i> </i><font SIZE="-1"><i>RT</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">IBM</font> <font SIZE="-1">RT</font> <font SIZE="-1">PC:</font> <br />
 </p>
<dl>
<dt><code>-min-line-mul</code></dt>
<dd> <p> Use an in-line code sequence for integer multiplies. This is the default. <br />
 </p>
 </dd>
<dt><code>-mcall-lib-mul</code></dt>
<dd> <p> Call <code>&quot;lmul$$&quot;</code> for integer multiples. <br />
 </p>
 </dd>
<dt><code>-mfull-fp-blocks</code></dt>
<dd> <p> Generate full-size floating point data blocks, including the minimum amount of scratch space recommended by <font SIZE="-1">IBM</font>. This is the default. <br />
 </p>
 </dd>
<dt><code>-mminimum-fp-blocks</code></dt>
<dd> <p> Do not include extra scratch space in floating point data blocks. This results in smaller code, but slower execution, since scratch space must be allocated dynamically. <br />
 </p>
 </dd>
<dt><code>-mfp-arg-in-fpregs</code></dt>
<dd> <p> Use a calling sequence incompatible with the <font SIZE="-1">IBM</font> calling convention in which floating point arguments are passed in floating point registers. Note that <code>&quot;varargs.h&quot;</code> and <code>&quot;stdarg.h&quot;</code> will not work with floating point operands if this option is specified. <br />
 </p>
 </dd>
<dt><code>-mfp-arg-in-gregs</code></dt>
<dd> <p> Use the normal calling convention for floating point arguments. This is the default. <br />
 </p>
 </dd>
<dt><code>-mhc-struct-return</code></dt>
<dd> <p> Return structures of more than one word in memory, rather than in a register. This provides compatibility with the MetaWare HighC (hc) compiler. Use the option <code>-fpcc-struct-return</code> for compatibility with the Portable C Compiler (pcc). <br />
 </p>
 </dd>
<dt><code>-mnohc-struct-return</code></dt>
<dd> <p> Return some structures of more than one word in registers, when convenient. This is the default. For compatibility with the IBM-supplied compilers, use the option <code>-fpcc-struct-return</code> or the option <code>-mhc-struct-return</code>. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>MIPS</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">MIPS</font> family of computers: <br />
 </p>
<dl>
<dt><code>-march=</code><i>cpu-type</i></dt>
<dd> <p> Assume the defaults for the machine type <i>cpu-type</i> when generating instructions. The choices for <i>cpu-type</i> are <code>r2000</code>, <code>r3000</code>, <code>r3900</code>, <code>r4000</code>, <code>r4100</code>, <code>r4300</code>, <code>r4400</code>, <code>r4600</code>, <code>r4650</code>, <code>r5000</code>, <code>r6000</code>, <code>r8000</code>, and <code>orion</code>. Additionally, the <code>r2000</code>, <code>r3000</code>, <code>r4000</code>, <code>r5000</code>, and <code>r6000</code> can be abbreviated as <code>r2k</code> (or <code>r2K</code>), <code>r3k</code>, etc. <br />
 </p>
 </dd>
<dt><code>-mtune=</code><i>cpu-type</i></dt>
<dd> <p> Assume the defaults for the machine type <i>cpu-type</i> when scheduling instructions. The choices for <i>cpu-type</i> are <code>r2000</code>, <code>r3000</code>, <code>r3900</code>, <code>r4000</code>, <code>r4100</code>, <code>r4300</code>, <code>r4400</code>, <code>r4600</code>, <code>r4650</code>, <code>r5000</code>, <code>r6000</code>, <code>r8000</code>, and <code>orion</code>. Additionally, the <code>r2000</code>, <code>r3000</code>, <code>r4000</code>, <code>r5000</code>, and <code>r6000</code> can be abbreviated as <code>r2k</code> (or <code>r2K</code>), <code>r3k</code>, etc. While picking a specific <i>cpu-type</i> will schedule things appropriately for that particular chip, the compiler will not generate any code that does not meet level 1 of the <font SIZE="-1">MIPS</font> <font SIZE="-1">ISA</font> (instruction set architecture) without a <code>-mipsX</code> or <code>-mabi</code> switch being used. <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>cpu-type</i></dt>
<dd> <p> This is identical to specifying both <code>-march</code> and <code>-mtune</code>. <br />
 </p>
 </dd>
<dt><code>-mips1</code></dt>
<dd> <p> Issue instructions from level 1 of the <font SIZE="-1">MIPS</font> <font SIZE="-1">ISA</font>. This is the default. <code>r3000</code> is the default <i>cpu-type</i> at this <font SIZE="-1">ISA</font> level. <br />
 </p>
 </dd>
<dt><code>-mips2</code></dt>
<dd> <p> Issue instructions from level 2 of the <font SIZE="-1">MIPS</font> <font SIZE="-1">ISA</font> (branch likely, square root instructions). <code>r6000</code> is the default <i>cpu-type</i> at this <font SIZE="-1">ISA</font> level. <br />
 </p>
 </dd>
<dt><code>-mips3</code></dt>
<dd> <p> Issue instructions from level 3 of the <font SIZE="-1">MIPS</font> <font SIZE="-1">ISA</font> (64-bit instructions). <code>r4000</code> is the default <i>cpu-type</i> at this <font SIZE="-1">ISA</font> level. <br />
 </p>
 </dd>
<dt><code>-mips4</code></dt>
<dd> <p> Issue instructions from level 4 of the <font SIZE="-1">MIPS</font> <font SIZE="-1">ISA</font> (conditional move, prefetch, enhanced <font SIZE="-1">FPU</font> instructions). <code>r8000</code> is the default <i>cpu-type</i> at this <font SIZE="-1">ISA</font> level. <br />
 </p>
 </dd>
<dt><code>-mfp32</code></dt>
<dd> <p> Assume that 32 32-bit floating point registers are available. This is the default. <br />
 </p>
 </dd>
<dt><code>-mfp64</code></dt>
<dd> <p> Assume that 32 64-bit floating point registers are available. This is the default when the <code>-mips3</code> option is used. <br />
 </p>
 </dd>
<dt><code>-mfused-madd</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fused-madd</code></dt>
<dd> <p> Generate code that uses (does not use) the floating point multiply and accumulate instructions, when they are available. These instructions are generated by default if they are available, but this may be undesirable if the extra precision causes problems or on certain chips in the mode where denormals are rounded to zero where denormals generated by multiply and accumulate instructions cause exceptions anyway. <br />
 </p>
 </dd>
<dt><code>-mgp32</code></dt>
<dd> <p> Assume that 32 32-bit general purpose registers are available. This is the default. <br />
 </p>
 </dd>
<dt><code>-mgp64</code></dt>
<dd> <p> Assume that 32 64-bit general purpose registers are available. This is the default when the <code>-mips3</code> option is used. <br />
 </p>
 </dd>
<dt><code>-mint64</code></dt>
<dd> <p> Force int and long types to be 64 bits wide. See <code>-mlong32</code> for an explanation of the default, and the width of pointers. <br />
 </p>
 </dd>
<dt><code>-mlong64</code></dt>
<dd> <p> Force long types to be 64 bits wide. See <code>-mlong32</code> for an explanation of the default, and the width of pointers. <br />
 </p>
 </dd>
<dt><code>-mlong32</code></dt>
<dd> <p> Force long, int, and pointer types to be 32 bits wide. </p>
<p> If none of <code>-mlong32</code>, <code>-mlong64</code>, or <code>-mint64</code> are set, the size of ints, longs, and pointers depends on the <font SIZE="-1">ABI</font> and <font SIZE="-1">ISA</font> chosen. For <code>-mabi=32</code>, and <code>-mabi=n32</code>, ints and longs are 32 bits wide. For <code>-mabi=64</code>, ints are 32 bits, and longs are 64 bits wide. For <code>-mabi=eabi</code> and either <code>-mips1</code> or <code>-mips2</code>, ints and longs are 32 bits wide. For <code>-mabi=eabi</code> and higher ISAs, ints are 32 bits, and longs are 64 bits wide. The width of pointer types is the smaller of the width of longs or the width of general purpose registers (which in turn depends on the <font SIZE="-1">ISA</font>). <br />
 </p>
 </dd>
<dt><code>-mabi=32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mabi=o64</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mabi=n32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mabi=64</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mabi=eabi</code></dt>
<dd> <p> Generate code for the indicated <font SIZE="-1">ABI</font>. The default instruction level is <code>-mips1</code> for <code>32</code>, <code>-mips3</code> for <code>n32</code>, and <code>-mips4</code> otherwise. Conversely, with <code>-mips1</code> or <code>-mips2</code>, the default <font SIZE="-1">ABI</font> is <code>32</code>; otherwise, the default <font SIZE="-1">ABI</font> is <code>64</code>. <br />
 </p>
 </dd>
<dt><code>-mmips-as</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">MIPS</font> assembler, and invoke <i>mips-tfile</i> to add normal debug information. This is the default for all platforms except for the <font SIZE="-1">OSF/1</font> reference platform, using the OSF/rose object format. If the either of the <code>-gstabs</code> or <code>-gstabs+</code> switches are used, the <i>mips-tfile</i> program will encapsulate the stabs within <font SIZE="-1">MIPS</font> <font SIZE="-1">ECOFF</font>. <br />
 </p>
 </dd>
<dt><code>-mgas</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">GNU</font> assembler. This is the default on the <font SIZE="-1">OSF/1</font> reference platform, using the OSF/rose object format. Also, this is the default if the configure option <code>---with-gnu-as</code> is used. <br />
 </p>
 </dd>
<dt><code>-msplit-addresses</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-split-addresses</code></dt>
<dd> <p> Generate code to load the high and low parts of address constants separately. This allows <font SIZE="-1">GCC</font> to optimize away redundant loads of the high order bits of addresses. This optimization requires <font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld. This optimization is enabled by default for some embedded targets where <font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld are standard. <br />
 </p>
 </dd>
<dt><code>-mrnames</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-rnames</code></dt>
<dd> <p> The <code>-mrnames</code> switch says to output code using the <font SIZE="-1">MIPS</font> software names for the registers, instead of the hardware names (ie, <i>a0</i> instead of <i>$4</i>). The only known assembler that supports this option is the Algorithmics assembler. <br />
 </p>
 </dd>
<dt><code>-mgpopt</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-gpopt</code></dt>
<dd> <p> The <code>-mgpopt</code> switch says to write all of the data declarations before the instructions in the text section, this allows the <font SIZE="-1">MIPS</font> assembler to generate one word memory references instead of using two words for short global or static data items. This is on by default if optimization is selected. <br />
 </p>
 </dd>
<dt><code>-mstats</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-stats</code></dt>
<dd> <p> For each non-inline function processed, the <code>-mstats</code> switch causes the compiler to emit one line to the standard error file to print statistics about the program (number of registers saved, stack size, etc.). <br />
 </p>
 </dd>
<dt><code>-mmemcpy</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-memcpy</code></dt>
<dd> <p> The <code>-mmemcpy</code> switch makes all block moves call the appropriate string function (<code>memcpy</code> or <code>bcopy</code>) instead of possibly generating inline code. <br />
 </p>
 </dd>
<dt><code>-mmips-tfile</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mips-tfile</code></dt>
<dd> <p> The <code>-mno-mips-tfile</code> switch causes the compiler not postprocess the object file with the <i>mips-tfile</i> program, after the <font SIZE="-1">MIPS</font> assembler has generated it to add debug support. If <i>mips-tfile</i> is not run, then no local variables will be available to the debugger. In addition, <i>stage2</i> and <i>stage3</i> objects will have the temporary file names passed to the assembler embedded in the object file, which means the objects will not compare the same. The <code>-mno-mips-tfile</code> switch should only be used when there are bugs in the <i>mips-tfile</i> program that prevents compilation. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not part of <font SIZE="-1">GCC</font>. Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. <br />
 </p>
 </dd>
<dt><code>-mhard-float</code></dt>
<dd> <p> Generate output containing floating point instructions. This is the default if you use the unmodified sources. <br />
 </p>
 </dd>
<dt><code>-mabicalls</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-abicalls</code></dt>
<dd> <p> Emit (or do not emit) the pseudo operations <code>.abicalls</code>, <code>.cpload</code>, and <code>.cprestore</code> that some System V.4 ports use for position independent code. <br />
 </p>
 </dd>
<dt><code>-mlong-calls</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-long-calls</code></dt>
<dd> <p> Do all calls with the <font SIZE="-1"><code>JALR</code></font> instruction, which requires loading up a function&#8217;s address into a register before the call. You need to use this switch, if you call outside of the current 512 megabyte segment to functions that are not through pointers. <br />
 </p>
 </dd>
<dt><code>-mhalf-pic</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-half-pic</code></dt>
<dd> <p> Put pointers to extern references into the data section and load them up, rather than put the references in the text section. <br />
 </p>
 </dd>
<dt><code>-membedded-pic</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-embedded-pic</code></dt>
<dd> <p> Generate <font SIZE="-1">PIC</font> code suitable for some embedded systems. All calls are made using <font SIZE="-1">PC</font> relative address, and all data is addressed using the <code>$gp</code> register. No more than 65536 bytes of global data may be used. This requires <font SIZE="-1">GNU</font> as and <font SIZE="-1">GNU</font> ld which do most of the work. This currently only works on targets which use <font SIZE="-1">ECOFF</font>; it does not work with <font SIZE="-1">ELF</font>. <br />
 </p>
 </dd>
<dt><code>-membedded-data</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-embedded-data</code></dt>
<dd> <p> Allocate variables to the read-only data section first if possible, then next in the small data section if possible, otherwise in data. This gives slightly slower code than the default, but reduces the amount of <font SIZE="-1">RAM</font> required when executing, and thus may be preferred for some embedded systems. <br />
 </p>
 </dd>
<dt><code>-muninit-const-in-rodata</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-uninit-const-in-rodata</code></dt>
<dd> <p> When used together with <code>-membedded-data</code>, it will always store uninitialized const variables in the read-only data section. <br />
 </p>
 </dd>
<dt><code>-msingle-float</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mdouble-float</code></dt>
<dd> <p> The <code>-msingle-float</code> switch tells gcc to assume that the floating point coprocessor only supports single precision operations, as on the <code>r4650</code> chip. The <code>-mdouble-float</code> switch permits gcc to use double precision operations. This is the default. <br />
 </p>
 </dd>
<dt><code>-mmad</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mad</code></dt>
<dd> <p> Permit use of the <code>mad</code>, <code>madu</code> and <code>mul</code> instructions, as on the <code>r4650</code> chip. <br />
 </p>
 </dd>
<dt><code>-m4650</code></dt>
<dd> <p> Turns on <code>-msingle-float</code>, <code>-mmad</code>, and, at least for now, <code>-mcpu=r4650</code>. <br />
 </p>
 </dd>
<dt><code>-mips16</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mips16</code></dt>
<dd> <p> Enable 16-bit instructions. <br />
 </p>
 </dd>
<dt><code>-mentry</code></dt>
<dd> <p> Use the entry and exit pseudo ops. This option can only be used with <code>-mips16</code>. <br />
 </p>
 </dd>
<dt><code>-EL</code></dt>
<dd> <p> Compile code for the processor in little endian mode. The requisite libraries are assumed to exist. <br />
 </p>
 </dd>
<dt><code>-EB</code></dt>
<dd> <p> Compile code for the processor in big endian mode. The requisite libraries are assumed to exist. <br />
 </p>
 </dd>
<dt><code>-G</code><i>num</i></dt>
<dd> <p> Put global and static items less than or equal to <i>num</i> bytes into the small data or bss sections instead of the normal data or bss section. This allows the assembler to emit one word memory reference instructions based on the global pointer (<i>gp</i> or <i>$28</i>), instead of the normal two words used. By default, <i>num</i> is 8 when the <font SIZE="-1">MIPS</font> assembler is used, and 0 when the <font SIZE="-1">GNU</font> assembler is used. The <code>-G</code> <i>num</i> switch is also passed to the assembler and linker. All modules should be compiled with the same <code>-G</code> <i>num</i> value. <br />
 </p>
 </dd>
<dt><code>-nocpp</code></dt>
<dd> <p> Tell the <font SIZE="-1">MIPS</font> assembler to not run its preprocessor over user assembler files (with a <code>.s</code> suffix) when assembling them. <br />
 </p>
 </dd>
<dt><code>-mfix7000</code></dt>
<dd> <p> Pass an option to gas which will cause nops to be inserted if the read of the destination register of an mfhi or mflo instruction occurs in the following two instructions. <br />
 </p>
 </dd>
<dt><code>-no-crt0</code></dt>
<dd> <p> Do not include the default crt0. <br />
 </p>
 </dd>
<dt><code>-mflush-func=</code><i>func</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-flush-func</code></dt>
<dd> <p> Specifies the function to call to flush the I and D caches, or to not call any such function. If called, the function must take the same arguments as the common <code>&quot;_flush_func()&quot;</code>, that is, the address of the memory range for which the cache is being flushed, the size of the memory range, and the number 3 (to flush both caches). The default depends on the target gcc was configured for, but commonly is either <code>_flush_func</code> or <code>__cpu_flush</code>. </p>
 </dd></dl>
<p> These options are defined by the macro <code>&quot;TARGET_SWITCHES&quot;</code> in the machine description. The default for the options is also defined by that macro, which enables you to change the defaults. </p>
<p> <i>Intel 386 and </i><font SIZE="-1"><i>AMD</i></font><i> x86-64 Options</i>  </p>
<p> These <code>-m</code> options are defined for the i386 and x86-64 family of computers: <br />
 </p>
<dl>
<dt><code>-mcpu=</code><i>cpu-type</i></dt>
<dd> <p> Tune to <i>cpu-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The choices for <i>cpu-type</i> are <code>i386</code>, <code>i486</code>, <code>i586</code>, <code>i686</code>, <code>pentium</code>, <code>pentium-mmx</code>, <code>pentiumpro</code>, <code>pentium2</code>, <code>pentium3</code>, <code>pentium4</code>, <code>k6</code>, <code>k6-2</code>, <code>k6-3</code>, <code>athlon</code>, <code>athlon-tbird</code>, <code>athlon-4</code>, <code>athlon-xp</code> and <code>athlon-mp</code>. </p>
<p> While picking a specific <i>cpu-type</i> will schedule things appropriately for that particular chip, the compiler will not generate any code that does not run on the i386 without the <code>-march=</code><i>cpu-type</i> option being used. <code>i586</code> is equivalent to <code>pentium</code> and <code>i686</code> is equivalent to <code>pentiumpro</code>. <code>k6</code> and <code>athlon</code> are the <font SIZE="-1">AMD</font> chips as opposed to the Intel ones. <br />
 </p>
 </dd>
<dt><code>-march=</code><i>cpu-type</i></dt>
<dd> <p> Generate instructions for the machine type <i>cpu-type</i>. The choices for <i>cpu-type</i> are the same as for <code>-mcpu</code>. Moreover, specifying <code>-march=</code><i>cpu-type</i> implies <code>-mcpu=</code><i>cpu-type</i>. <br />
 </p>
 </dd>
<dt><code>-m386</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m486</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpentium</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpentiumpro</code></dt>
<dd> <p> These options are synonyms for <code>-mcpu=i386</code>, <code>-mcpu=i486</code>, <code>-mcpu=pentium</code>, and <code>-mcpu=pentiumpro</code> respectively. These synonyms are deprecated. <br />
 </p>
 </dd>
<dt><code>-mfpmath=</code><i>unit</i></dt>
<dd> <p> generate floating point arithmetics for selected unit <i>unit</i>. the choices for <i>unit</i> are: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>387</code></dt>
<dd> <p> Use the standard 387 floating point coprocessor present majority of chips and emulated otherwise. Code compiled with this option will run almost everywhere. The temporary results are computed in 80bit precesion instead of precision specified by the type resulting in slightly different results compared to most of other chips. See <code>-ffloat-store</code> for more detailed description. </p>
<p> This is the default choice for i386 compiler. <br />
 </p>
 </dd>
<dt><code>sse</code></dt>
<dd> <p> Use scalar floating point instructions present in the <font SIZE="-1">SSE</font> instruction set. This instruction set is supported by Pentium3 and newer chips, in the <font SIZE="-1">AMD</font> line by Athlon-4, Athlon-xp and Athlon-mp chips. The earlier version of <font SIZE="-1">SSE</font> instruction set supports only single precision arithmetics, thus the double and extended precision arithmetics is still done using 387. Later version, present only in Pentium4 and the future <font SIZE="-1">AMD</font> x86-64 chips supports double precision arithmetics too. </p>
<p> For i387 you need to use <code>-march=</code><i>cpu-type</i>, <code>-msse</code> or <code>-msse2</code> switches to enable <font SIZE="-1">SSE</font> extensions and make this option effective. For x86-64 compiler, these extensions are enabled by default. </p>
<p> The resulting code should be considerably faster in majority of cases and avoid the numerical instability problems of 387 code, but may break some existing code that expects temporaries to be 80bit. </p>
<p> This is the default choice for x86-64 compiler. <br />
 </p>
 </dd>
<dt><code>sse,387</code></dt>
<dd> <p> Attempt to utilize both instruction sets at once. This effectivly double the amount of available registers and on chips with separate execution units for 387 and <font SIZE="-1">SSE</font> the execution resources too. Use this option with care, as it is still experimental, because gcc register allocator does not model separate functional units well resulting in instable performance. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-masm=</code><i>dialect</i></dt>
<dd> <p> Output asm instructions using selected <i>dialect</i>. Supported choices are <code>intel</code> or <code>att</code> (the default one). <br />
 </p>
 </dd>
<dt><code>-mieee-fp</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-ieee-fp</code></dt>
<dd> <p> Control whether or not the compiler uses <font SIZE="-1">IEEE</font> floating point comparisons. These handle correctly the case where the result of a comparison is unordered. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not part of <font SIZE="-1">GCC</font>. Normally the facilities of the machine&#8217;s usual C compiler are used, but this can&#8217;t be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. </p>
<p> On machines where a function returns floating point results in the 80387 register stack, some floating point opcodes may be emitted even if <code>-msoft-float</code> is used. <br />
 </p>
 </dd>
<dt><code>-mno-fp-ret-in-387</code></dt>
<dd> <p> Do not use the <font SIZE="-1">FPU</font> registers for return values of functions. </p>
<p> The usual calling convention has functions return values of types <code>&quot;float&quot;</code> and <code>&quot;double&quot;</code> in an <font SIZE="-1">FPU</font> register, even if there is no <font SIZE="-1">FPU</font>. The idea is that the operating system should emulate an <font SIZE="-1">FPU</font>. </p>
<p> The option <code>-mno-fp-ret-in-387</code> causes such values to be returned in ordinary <font SIZE="-1">CPU</font> registers instead. <br />
 </p>
 </dd>
<dt><code>-mno-fancy-math-387</code></dt>
<dd> <p> Some 387 emulators do not support the <code>&quot;sin&quot;</code>, <code>&quot;cos&quot;</code> and <code>&quot;sqrt&quot;</code> instructions for the 387. Specify this option to avoid generating those instructions. This option is the default on FreeBSD, OpenBSD and NetBSD. This option is overridden when <code>-march</code> indicates that the target cpu will always have an <font SIZE="-1">FPU</font> and so the instruction will not need emulation. As of revision 2.6.1, these instructions are not generated unless you also use the <code>-funsafe-math-optimizations</code> switch. <br />
 </p>
 </dd>
<dt><code>-malign-double</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-align-double</code></dt>
<dd> <p> Control whether <font SIZE="-1">GCC</font> aligns <code>&quot;double&quot;</code>, <code>&quot;long double&quot;</code>, and <code>&quot;long long&quot;</code> variables on a two word boundary or a one word boundary. Aligning <code>&quot;double&quot;</code> variables on a two word boundary will produce code that runs somewhat faster on a <code>Pentium</code> at the expense of more memory. </p>
<p> <code>Warning:</code> if you use the <code>-malign-double</code> switch, structures containing the above types will be aligned differently than the published application binary interface specifications for the 386 and will not be binary compatible with structures in code compiled without that switch. <br />
 </p>
 </dd>
<dt><code>-m128bit-long-double</code></dt>
<dd> <p> Control the size of <code>&quot;long double&quot;</code> type. i386 application binary interface specify the size to be 12 bytes, while modern architectures (Pentium and newer) prefer <code>&quot;long double&quot;</code> aligned to 8 or 16 byte boundary. This is impossible to reach with 12 byte long doubles in the array accesses. </p>
<p> <code>Warning:</code> if you use the <code>-m128bit-long-double</code> switch, the structures and arrays containing <code>&quot;long double&quot;</code> will change their size as well as function calling convention for function taking <code>&quot;long double&quot;</code> will be modified. <br />
 </p>
 </dd>
<dt><code>-m96bit-long-double</code></dt>
<dd> <p> Set the size of <code>&quot;long double&quot;</code> to 96 bits as required by the i386 application binary interface. This is the default. <br />
 </p>
 </dd>
<dt><code>-msvr3-shlib</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-svr3-shlib</code></dt>
<dd> <p> Control whether <font SIZE="-1">GCC</font> places uninitialized local variables into the <code>&quot;bss&quot;</code> or <code>&quot;data&quot;</code> segments. <code>-msvr3-shlib</code> places them into <code>&quot;bss&quot;</code>. These options are meaningful only on System V Release 3. <br />
 </p>
 </dd>
<dt><code>-mrtd</code></dt>
<dd> <p> Use a different function-calling convention, in which functions that take a fixed number of arguments return with the <code>&quot;ret&quot;</code> <i>num</i> instruction, which pops their arguments while returning. This saves one instruction in the caller since there is no need to pop the arguments there. </p>
<p> You can specify that an individual function is called with this calling sequence with the function attribute <code>stdcall</code>. You can also override the <code>-mrtd</code> option by using the function attribute <code>cdecl</code>. </p>
<p> <code>Warning:</code> this calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <code>&quot;printf&quot;</code>); otherwise incorrect code will be generated for calls to those functions. </p>
<p> In addition, seriously incorrect code will result if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.) <br />
 </p>
 </dd>
<dt><code>-mregparm=</code><i>num</i></dt>
<dd> <p> Control how many registers are used to pass integer arguments. By default, no registers are used to pass arguments, and at most 3 registers can be used. You can control this behavior for a specific function by using the function attribute <code>regparm</code>. </p>
<p> <code>Warning:</code> if you use this switch, and <i>num</i> is nonzero, then you must build all modules with the same value, including any libraries. This includes the system libraries and startup modules. <br />
 </p>
 </dd>
<dt><code>-mpreferred-stack-boundary=</code><i>num</i></dt>
<dd> <p> Attempt to keep the stack boundary aligned to a 2 raised to <i>num</i> byte boundary. If <code>-mpreferred-stack-boundary</code> is not specified, the default is 4 (16 bytes or 128 bits), except when optimizing for code size (<code>-Os</code>), in which case the default is the minimum correct alignment (4 bytes for x86, and 8 bytes for x86-64). </p>
<p> On Pentium and PentiumPro, <code>&quot;double&quot;</code> and <code>&quot;long double&quot;</code> values should be aligned to an 8 byte boundary (see <code>-malign-double</code>) or suffer significant run time performance penalties. On Pentium <font SIZE="-1">III</font>, the Streaming <font SIZE="-1">SIMD</font> Extension (<font SIZE="-1">SSE</font>) data type <code>&quot;__m128&quot;</code> suffers similar penalties if it is not 16 byte aligned. </p>
<p> To ensure proper alignment of this values on the stack, the stack boundary must be as aligned as that required by any value stored on the stack. Further, every function must be generated such that it keeps the stack aligned. Thus calling a function compiled with a higher preferred stack boundary from a function compiled with a lower preferred stack boundary will most likely misalign the stack. It is recommended that libraries that use callbacks always use the default setting. </p>
<p> This extra alignment does consume extra stack space, and generally increases code size. Code that is sensitive to stack space usage, such as embedded systems and operating system kernels, may want to reduce the preferred alignment to <code>-mpreferred-stack-boundary=2</code>. <br />
 </p>
 </dd>
<dt><code>-mmmx</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mmx</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msse</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-sse</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msse2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-sse2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m3dnow</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-3dnow</code></dt>
<dd> <p> These switches enable or disable the use of built-in functions that allow direct access to the <font SIZE="-1">MMX</font>, <font SIZE="-1">SSE</font> and 3Dnow extensions of the instruction set. </p>
<p> To have <font SIZE="-1">SSE/SSE2</font> instructions generated automatically from floating-point code, see <code>-mfpmath=sse</code>. <br />
 </p>
 </dd>
<dt><code>-mpush-args</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-push-args</code></dt>
<dd> <p> Use <font SIZE="-1">PUSH</font> operations to store outgoing parameters. This method is shorter and usually equally fast as method using <font SIZE="-1">SUB/MOV</font> operations and is enabled by default. In some cases disabling it may improve performance because of improved scheduling and reduced dependencies. <br />
 </p>
 </dd>
<dt><code>-maccumulate-outgoing-args</code></dt>
<dd> <p> If enabled, the maximum amount of space required for outgoing arguments will be computed in the function prologue. This is faster on most modern CPUs because of reduced dependencies, improved scheduling and reduced stack usage when preferred stack boundary is not equal to 2. The drawback is a notable increase in code size. This switch implies <code>-mno-push-args</code>. <br />
 </p>
 </dd>
<dt><code>-mthreads</code></dt>
<dd> <p> Support thread-safe exception handling on <code>Mingw32</code>. Code that relies on thread-safe exception handling must compile and link all code with the <code>-mthreads</code> option. When compiling, <code>-mthreads</code> defines <code>-D_MT</code>; when linking, it links in a special thread helper library <code>-lmingwthrd</code> which cleans up per thread exception handling data. <br />
 </p>
 </dd>
<dt><code>-mno-align-stringops</code></dt>
<dd> <p> Do not align destination of inlined string operations. This switch reduces code size and improves performance in case the destination is already aligned, but gcc don&#8217;t know about it. <br />
 </p>
 </dd>
<dt><code>-minline-all-stringops</code></dt>
<dd> <p> By default <font SIZE="-1">GCC</font> inlines string operations only when destination is known to be aligned at least to 4 byte boundary. This enables more inlining, increase code size, but may improve performance of code that depends on fast memcpy, strlen and memset for short lengths. <br />
 </p>
 </dd>
<dt><code>-momit-leaf-frame-pointer</code></dt>
<dd> <p> Don&#8217;t keep the frame pointer in a register for leaf functions. This avoids the instructions to save, set up and restore frame pointers and makes an extra register available in leaf functions. The option <code>-fomit-frame-pointer</code> removes the frame pointer for all functions which might make debugging harder. </p>
 </dd></dl>
<p> These <code>-m</code> switches are supported in addition to the above on <font SIZE="-1">AMD</font> x86-64 processors in 64-bit environments. <br />
 </p>
<dl>
<dt><code>-m32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m64</code></dt>
<dd> <p> Generate code for a 32-bit or 64-bit environment. The 32-bit environment sets int, long and pointer to 32 bits and generates code that runs on any i386 system. The 64-bit environment sets int to 32 bits and long and pointer to 64 bits and generates code for <font SIZE="-1">AMD</font>&#8216;s x86-64 architecture. <br />
 </p>
 </dd>
<dt><code>-mno-red-zone</code></dt>
<dd> <p> Do not use a so called red zone for x86-64 code. The red zone is mandated by the x86-64 <font SIZE="-1">ABI</font>, it is a 128-byte area beyond the location of the stack pointer that will not be modified by signal or interrupt handlers and therefore can be used for temporary data without adjusting the stack pointer. The flag <code>-mno-red-zone</code> disables this red zone. <br />
 </p>
 </dd>
<dt><code>-mcmodel=small</code></dt>
<dd> <p> Generate code for the small code model: the program and its symbols must be linked in the lower 2 <font SIZE="-1">GB</font> of the address space. Pointers are 64 bits. Programs can be statically or dynamically linked. This is the default code model. <br />
 </p>
 </dd>
<dt><code>-mcmodel=kernel</code></dt>
<dd> <p> Generate code for the kernel code model. The kernel runs in the negative 2 <font SIZE="-1">GB</font> of the address space. This model has to be used for Linux kernel code. <br />
 </p>
 </dd>
<dt><code>-mcmodel=medium</code></dt>
<dd> <p> Generate code for the medium model: The program is linked in the lower 2 <font SIZE="-1">GB</font> of the address space but symbols can be located anywhere in the address space. Programs can be statically or dynamically linked, but building of shared libraries are not supported with the medium model. <br />
 </p>
 </dd>
<dt><code>-mcmodel=large</code></dt>
<dd> <p> Generate code for the large model: This model makes no assumptions about addresses and sizes of sections. Currently <font SIZE="-1">GCC</font> does not implement this model. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>HPPA</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">HPPA</font> family of computers: <br />
 </p>
<dl>
<dt><code>-march=</code><i>architecture-type</i></dt>
<dd> <p> Generate code for the specified architecture. The choices for <i>architecture-type</i> are <code>1.0</code> for <font SIZE="-1">PA</font> 1.0, <code>1.1</code> for <font SIZE="-1">PA</font> 1.1, and <code>2.0</code> for <font SIZE="-1">PA</font> 2.0 processors. Refer to <i>/usr/lib/sched.models</i> on an <font SIZE="-1">HP-UX</font> system to determine the proper architecture option for your machine. Code compiled for lower numbered architectures will run on higher numbered architectures, but not the other way around. </p>
<p> <font SIZE="-1">PA</font> 2.0 support currently requires gas snapshot 19990413 or later. The next release of binutils (current is 2.9.1) will probably contain <font SIZE="-1">PA</font> 2.0 support. <br />
 </p>
 </dd>
<dt><code>-mpa-risc-1-0</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpa-risc-1-1</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mpa-risc-2-0</code></dt>
<dd> <p> Synonyms for <code>-march=1.0</code>, <code>-march=1.1</code>, and <code>-march=2.0</code> respectively. <br />
 </p>
 </dd>
<dt><code>-mbig-switch</code></dt>
<dd> <p> Generate code suitable for big switch tables. Use this option only if the assembler/linker complain about out of range branches within a switch table. <br />
 </p>
 </dd>
<dt><code>-mjump-in-delay</code></dt>
<dd> <p> Fill delay slots of function calls with unconditional jump instructions by modifying the return pointer for the function call to be the target of the conditional jump. <br />
 </p>
 </dd>
<dt><code>-mdisable-fpregs</code></dt>
<dd> <p> Prevent floating point registers from being used in any manner. This is necessary for compiling kernels which perform lazy context switching of floating point registers. If you use this option and attempt to perform floating point operations, the compiler will abort. <br />
 </p>
 </dd>
<dt><code>-mdisable-indexing</code></dt>
<dd> <p> Prevent the compiler from using indexing address modes. This avoids some rather obscure problems when compiling <font SIZE="-1">MIG</font> generated code under <font SIZE="-1">MACH</font>. <br />
 </p>
 </dd>
<dt><code>-mno-space-regs</code></dt>
<dd> <p> Generate code that assumes the target has no space registers. This allows <font SIZE="-1">GCC</font> to generate faster indirect calls and use unscaled index address modes. </p>
<p> Such code is suitable for level 0 <font SIZE="-1">PA</font> systems and kernels. <br />
 </p>
 </dd>
<dt><code>-mfast-indirect-calls</code></dt>
<dd> <p> Generate code that assumes calls never cross space boundaries. This allows <font SIZE="-1">GCC</font> to emit code which performs faster indirect calls. </p>
<p> This option will not work in the presence of shared libraries or nested functions. <br />
 </p>
 </dd>
<dt><code>-mlong-load-store</code></dt>
<dd> <p> Generate 3-instruction load and store sequences as sometimes required by the <font SIZE="-1">HP-UX</font> 10 linker. This is equivalent to the <code>+k</code> option to the <font SIZE="-1">HP</font> compilers. <br />
 </p>
 </dd>
<dt><code>-mportable-runtime</code></dt>
<dd> <p> Use the portable calling conventions proposed by <font SIZE="-1">HP</font> for <font SIZE="-1">ELF</font> systems. <br />
 </p>
 </dd>
<dt><code>-mgas</code></dt>
<dd> <p> Enable the use of assembler directives only <font SIZE="-1">GAS</font> understands. <br />
 </p>
 </dd>
<dt><code>-mschedule=</code><i>cpu-type</i></dt>
<dd> <p> Schedule code according to the constraints for the machine type <i>cpu-type</i>. The choices for <i>cpu-type</i> are <code>700</code> <code>7100</code>, <code>7100LC</code>, <code>7200</code>, and <code>8000</code>. Refer to <i>/usr/lib/sched.models</i> on an <font SIZE="-1">HP-UX</font> system to determine the proper scheduling option for your machine. <br />
 </p>
 </dd>
<dt><code>-mlinker-opt</code></dt>
<dd> <p> Enable the optimization pass in the <font SIZE="-1">HPUX</font> linker. Note this makes symbolic debugging impossible. It also triggers a bug in the <font SIZE="-1">HPUX</font> 8 and <font SIZE="-1">HPUX</font> 9 linkers in which they give bogus error messages when linking some programs. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries are not available for all <font SIZE="-1">HPPA</font> targets. Normally the facilities of the machine&#8217;s usual C compiler are used, but this cannot be done directly in cross-compilation. You must make your own arrangements to provide suitable library functions for cross-compilation. The embedded target <code>hppa1.1-*-pro</code> does provide software floating point support. </p>
<p> <code>-msoft-float</code> changes the calling convention in the output file; therefore, it is only useful if you compile <i>all</i> of a program with this option. In particular, you need to compile <i>libgcc.a</i>, the library that comes with <font SIZE="-1">GCC</font>, with <code>-msoft-float</code> in order for this to work. </p>
 </dd></dl>
<p> <i>Intel 960 Options</i>  </p>
<p> These <code>-m</code> options are defined for the Intel 960 implementations: <br />
 </p>
<dl>
<dt><code>-m</code><i>cpu-type</i></dt>
<dd> <p> Assume the defaults for the machine type <i>cpu-type</i> for some of the other options, including instruction scheduling, floating point support, and addressing modes. The choices for <i>cpu-type</i> are <code>ka</code>, <code>kb</code>, <code>mc</code>, <code>ca</code>, <code>cf</code>, <code>sa</code>, and <code>sb</code>. The default is <code>kb</code>. <br />
 </p>
 </dd>
<dt><code>-mnumerics</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> The <code>-mnumerics</code> option indicates that the processor does support floating-point instructions. The <code>-msoft-float</code> option indicates that floating-point support should not be assumed. <br />
 </p>
 </dd>
<dt><code>-mleaf-procedures</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-leaf-procedures</code></dt>
<dd> <p> Do (or do not) attempt to alter leaf procedures to be callable with the <code>&quot;bal&quot;</code> instruction as well as <code>&quot;call&quot;</code>. This will result in more efficient code for explicit calls when the <code>&quot;bal&quot;</code> instruction can be substituted by the assembler or linker, but less efficient code in other cases, such as calls via function pointers, or using a linker that doesn&#8217;t support this optimization. <br />
 </p>
 </dd>
<dt><code>-mtail-call</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-tail-call</code></dt>
<dd> <p> Do (or do not) make additional attempts (beyond those of the machine-independent portions of the compiler) to optimize tail-recursive calls into branches. You may not want to do this because the detection of cases where this is not valid is not totally complete. The default is <code>-mno-tail-call</code>. <br />
 </p>
 </dd>
<dt><code>-mcomplex-addr</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-complex-addr</code></dt>
<dd> <p> Assume (or do not assume) that the use of a complex addressing mode is a win on this implementation of the i960. Complex addressing modes may not be worthwhile on the K-series, but they definitely are on the C-series. The default is currently <code>-mcomplex-addr</code> for all processors except the <font SIZE="-1">CB</font> and <font SIZE="-1">CC</font>. <br />
 </p>
 </dd>
<dt><code>-mcode-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-code-align</code></dt>
<dd> <p> Align code to 8-byte boundaries for faster fetching (or don&#8217;t bother). Currently turned on by default for C-series implementations only. <br />
 </p>
 </dd>
<dt><code>-mic-compat</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mic2.0-compat</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mic3.0-compat</code></dt>
<dd> <p> Enable compatibility with iC960 v2.0 or v3.0. <br />
 </p>
 </dd>
<dt><code>-masm-compat</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mintel-asm</code></dt>
<dd> <p> Enable compatibility with the iC960 assembler. <br />
 </p>
 </dd>
<dt><code>-mstrict-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-strict-align</code></dt>
<dd> <p> Do not permit (do permit) unaligned accesses. <br />
 </p>
 </dd>
<dt><code>-mold-align</code></dt>
<dd> <p> Enable structure-alignment compatibility with Intel&#8217;s gcc release version 1.3 (based on gcc 1.37). This option implies <code>-mstrict-align</code>. <br />
 </p>
 </dd>
<dt><code>-mlong-double-64</code></dt>
<dd> <p> Implement type <code>long double</code> as 64-bit floating point numbers. Without the option <code>long double</code> is implemented by 80-bit floating point numbers. The only reason we have it because there is no 128-bit <code>long double</code> support in <code>fp-bit.c</code> yet. So it is only useful for people using soft-float targets. Otherwise, we should recommend against use of it. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">DEC</font> Alpha implementations: <br />
 </p>
<dl>
<dt><code>-mno-soft-float</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Use (do not use) the hardware floating-point instructions for floating-point operations. When <code>-msoft-float</code> is specified, functions in <i>libgcc.a</i> will be used to perform floating-point operations. Unless they are replaced by routines that emulate the floating-point operations, or compiled in such a way as to call such emulations routines, these routines will issue floating-point operations. If you are compiling for an Alpha without floating-point operations, you must ensure that the library is built so as not to call them. </p>
<p> Note that Alpha implementations without floating-point operations are required to have floating-point registers. <br />
 </p>
 </dd>
<dt><code>-mfp-reg</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fp-regs</code></dt>
<dd> <p> Generate code that uses (does not use) the floating-point register set. <code>-mno-fp-regs</code> implies <code>-msoft-float</code>. If the floating-point register set is not used, floating point operands are passed in integer registers as if they were integers and floating-point results are passed in <code>&quot;$0&quot;</code> instead of <code>&quot;$f0&quot;</code>. This is a non-standard calling sequence, so any function with a floating-point argument or return value called by code compiled with <code>-mno-fp-regs</code> must also be compiled with that option. </p>
<p> A typical use of this option is building a kernel that does not use, and hence need not save and restore, any floating-point registers. <br />
 </p>
 </dd>
<dt><code>-mieee</code></dt>
<dd> <p> The Alpha architecture implements floating-point hardware optimized for maximum performance. It is mostly compliant with the <font SIZE="-1">IEEE</font> floating point standard. However, for full compliance, software assistance is required. This option generates code fully <font SIZE="-1">IEEE</font> compliant code <i>except</i> that the <i>inexact-flag</i> is not maintained (see below). If this option is turned on, the preprocessor macro <code>&quot;_IEEE_FP&quot;</code> is defined during compilation. The resulting code is less efficient but is able to correctly support denormalized numbers and exceptional <font SIZE="-1">IEEE</font> values such as not-a-number and plus/minus infinity. Other Alpha compilers call this option <code>-ieee_with_no_inexact</code>. <br />
 </p>
 </dd>
<dt><code>-mieee-with-inexact</code></dt>
<dd> <p> This is like <code>-mieee</code> except the generated code also maintains the <font SIZE="-1">IEEE</font> <i>inexact-flag</i>. Turning on this option causes the generated code to implement fully-compliant <font SIZE="-1">IEEE</font> math. In addition to <code>&quot;_IEEE_FP&quot;</code>, <code>&quot;_IEEE_FP_EXACT&quot;</code> is defined as a preprocessor macro. On some Alpha implementations the resulting code may execute significantly slower than the code generated by default. Since there is very little code that depends on the <i>inexact-flag</i>, you should normally not specify this option. Other Alpha compilers call this option <code>-ieee_with_inexact</code>. <br />
 </p>
 </dd>
<dt><code>-mfp-trap-mode=</code><i>trap-mode</i></dt>
<dd> <p> This option controls what floating-point related traps are enabled. Other Alpha compilers call this option <code>-fptm</code> <i>trap-mode</i>. The trap mode can be set to one of four values: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>n</code></dt>
<dd> <p> This is the default (normal) setting. The only traps that are enabled are the ones that cannot be disabled in software (e.g., division by zero trap). <br />
 </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> In addition to the traps enabled by <code>n</code>, underflow traps are enabled as well. <br />
 </p>
 </dd>
<dt><code>su</code></dt>
<dd> <p> Like <code>su</code>, but the instructions are marked to be safe for software completion (see Alpha architecture manual for details). <br />
 </p>
 </dd>
<dt><code>sui</code></dt>
<dd> <p> Like <code>su</code>, but inexact traps are enabled as well. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-mfp-rounding-mode=</code><i>rounding-mode</i></dt>
<dd> <p> Selects the <font SIZE="-1">IEEE</font> rounding mode. Other Alpha compilers call this option <code>-fprm</code> <i>rounding-mode</i>. The <i>rounding-mode</i> can be one of: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>n</code></dt>
<dd> <p> Normal <font SIZE="-1">IEEE</font> rounding mode. Floating point numbers are rounded towards the nearest machine number or towards the even machine number in case of a tie. <br />
 </p>
 </dd>
<dt><code>m</code></dt>
<dd> <p> Round towards minus infinity. <br />
 </p>
 </dd>
<dt><code>c</code></dt>
<dd> <p> Chopped rounding mode. Floating point numbers are rounded towards zero. <br />
 </p>
 </dd>
<dt><code>d</code></dt>
<dd> <p> Dynamic rounding mode. A field in the floating point control register (<i>fpcr</i>, see Alpha architecture reference manual) controls the rounding mode in effect. The C library initializes this register for rounding towards plus infinity. Thus, unless your program modifies the <i>fpcr</i>, <code>d</code> corresponds to round towards plus infinity. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-mtrap-precision=</code><i>trap-precision</i></dt>
<dd> <p> In the Alpha architecture, floating point traps are imprecise. This means without software assistance it is impossible to recover from a floating trap and program execution normally needs to be terminated. <font SIZE="-1">GCC</font> can generate code that can assist operating system trap handlers in determining the exact location that caused a floating point trap. Depending on the requirements of an application, different levels of precisions can be selected: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>p</code></dt>
<dd> <p> Program precision. This option is the default and means a trap handler can only identify which program caused a floating point exception. <br />
 </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> Function precision. The trap handler can determine the function that caused a floating point exception. <br />
 </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Instruction precision. The trap handler can determine the exact instruction that caused a floating point exception. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Other Alpha compilers provide the equivalent options called <code>-scope_safe</code> and <code>-resumption_safe</code>. </p>
 </dd></dl>
<p> <br />
 </p>
<dt><code>-mieee-conformant</code></dt>
<dd> <p> This option marks the generated code as <font SIZE="-1">IEEE</font> conformant. You must not use this option unless you also specify <code>-mtrap-precision=i</code> and either <code>-mfp-trap-mode=su</code> or <code>-mfp-trap-mode=sui</code>. Its only effect is to emit the line <code>.eflag 48</code> in the function prologue of the generated assembly file. Under <font SIZE="-1">DEC</font> Unix, this has the effect that IEEE-conformant math library routines will be linked in. <br />
 </p>
 </dd>
<dt><code>-mbuild-constants</code></dt>
<dd> <p> Normally <font SIZE="-1">GCC</font> examines a 32- or 64-bit integer constant to see if it can construct it from smaller constants in two or three instructions. If it cannot, it will output the constant as a literal and generate code to load it from the data segment at runtime. </p>
<p> Use this option to require <font SIZE="-1">GCC</font> to construct <i>all</i> integer constants using code, even if it takes more instructions (the maximum is six). </p>
<p> You would typically use this option to build a shared library dynamic loader. Itself a shared library, it must relocate itself in memory before it can find the variables and constants in its own data segment. <br />
 </p>
 </dd>
<dt><code>-malpha-as</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mgas</code></dt>
<dd> <p> Select whether to generate code to be assembled by the vendor-supplied assembler (<code>-malpha-as</code>) or by the <font SIZE="-1">GNU</font> assembler <code>-mgas</code>. <br />
 </p>
 </dd>
<dt><code>-mbwx</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-bwx</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mcix</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-cix</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mfix</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fix</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mmax</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-max</code></dt>
<dd> <p> Indicate whether <font SIZE="-1">GCC</font> should generate code to use the optional <font SIZE="-1">BWX</font>, <font SIZE="-1">CIX</font>, <font SIZE="-1">FIX</font> and <font SIZE="-1">MAX</font> instruction sets. The default is to use the instruction sets supported by the <font SIZE="-1">CPU</font> type specified via <code>-mcpu=</code> option or that of the <font SIZE="-1">CPU</font> on which <font SIZE="-1">GCC</font> was built if none was specified. <br />
 </p>
 </dd>
<dt><code>-mfloat-vax</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mfloat-ieee</code></dt>
<dd> <p> Generate code that uses (does not use) <font SIZE="-1">VAX</font> F and G floating point arithmetic instead of <font SIZE="-1">IEEE</font> single and double precision. <br />
 </p>
 </dd>
<dt><code>-mexplicit-relocs</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-explicit-relocs</code></dt>
<dd> <p> Older Alpha assemblers provided no way to generate symbol relocations except via assembler macros. Use of these macros does not allow optimial instruction scheduling. <font SIZE="-1">GNU</font> binutils as of version 2.12 supports a new syntax that allows the compiler to explicitly mark which relocations should apply to which instructions. This option is mostly useful for debugging, as <font SIZE="-1">GCC</font> detects the capabilities of the assembler when it is built and sets the default accordingly. <br />
 </p>
 </dd>
<dt><code>-msmall-data</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mlarge-data</code></dt>
<dd> <p> When <code>-mexplicit-relocs</code> is in effect, static data is accessed via <i>gp-relative</i> relocations. When <code>-msmall-data</code> is used, objects 8 bytes long or smaller are placed in a <i>small data area</i> (the <code>&quot;.sdata&quot;</code> and <code>&quot;.sbss&quot;</code> sections) and are accessed via 16-bit relocations off of the <code>&quot;$gp&quot;</code> register. This limits the size of the small data area to 64KB, but allows the variables to be directly accessed via a single instruction. </p>
<p> The default is <code>-mlarge-data</code>. With this option the data area is limited to just below 2GB. Programs that require more than 2GB of data must use <code>&quot;malloc&quot;</code> or <code>&quot;mmap&quot;</code> to allocate the data in the heap instead of in the program&#8217;s data segment. </p>
<p> When generating code for shared libraries, <code>-fpic</code> implies <code>-msmall-data</code> and <code>-fPIC</code> implies <code>-mlarge-data</code>. <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>cpu_type</i></dt>
<dd> <p> Set the instruction set and instruction scheduling parameters for machine type <i>cpu_type</i>. You can specify either the <font SIZE="-1"><code>EV</code></font> style name or the corresponding chip number. <font SIZE="-1">GCC</font> supports scheduling parameters for the <font SIZE="-1">EV4</font>, <font SIZE="-1">EV5</font> and <font SIZE="-1">EV6</font> family of processors and will choose the default values for the instruction set from the processor you specify. If you do not specify a processor type, <font SIZE="-1">GCC</font> will default to the processor on which the compiler was built. </p>
<p> Supported values for <i>cpu_type</i> are </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>ev4</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>ev45</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21064</code></dt>
<dd> <p> Schedules as an <font SIZE="-1">EV4</font> and has no instruction set extensions. <br />
 </p>
 </dd>
<dt><code>ev5</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21164</code></dt>
<dd> <p> Schedules as an <font SIZE="-1">EV5</font> and has no instruction set extensions. <br />
 </p>
 </dd>
<dt><code>ev56</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21164a</code></dt>
<dd> <p> Schedules as an <font SIZE="-1">EV5</font> and supports the <font SIZE="-1">BWX</font> extension. <br />
 </p>
 </dd>
<dt><code>pca56</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21164pc</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21164PC</code></dt>
<dd> <p> Schedules as an <font SIZE="-1">EV5</font> and supports the <font SIZE="-1">BWX</font> and <font SIZE="-1">MAX</font> extensions. <br />
 </p>
 </dd>
<dt><code>ev6</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21264</code></dt>
<dd> <p> Schedules as an <font SIZE="-1">EV6</font> and supports the <font SIZE="-1">BWX</font>, <font SIZE="-1">FIX</font>, and <font SIZE="-1">MAX</font> extensions. <br />
 </p>
 </dd>
<dt><code>ev67</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>21264a</code></dt>
<dd> <p> Schedules as an <font SIZE="-1">EV6</font> and supports the <font SIZE="-1">BWX</font>, <font SIZE="-1">CIX</font>, <font SIZE="-1">FIX</font>, and <font SIZE="-1">MAX</font> extensions. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<p> <br />
 </p>
<dt><code>-mtune=</code><i>cpu_type</i></dt>
<dd> <p> Set only the instruction scheduling parameters for machine type <i>cpu_type</i>. The instruction set is not changed. <br />
 </p>
 </dd>
<dt><code>-mmemory-latency=</code><i>time</i></dt>
<dd> <p> Sets the latency the scheduler should assume for typical memory references as seen by the application. This number is highly dependent on the memory access patterns used by the application and the size of the external cache on the machine. </p>
<p> Valid options for <i>time</i> are </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><i>number</i></dt>
<dd> <p> A decimal number representing clock cycles. <br />
 </p>
 </dd>
<dt><code>L1</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>L2</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>L3</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>main</code></dt>
<dd> <p> The compiler contains estimates of the number of clock cycles for ``typical&#8217;&#8216; <font SIZE="-1">EV4</font> &amp; <font SIZE="-1">EV5</font> hardware for the Level 1, 2 &amp; 3 caches (also called Dcache, Scache, and Bcache), as well as to main memory. Note that L3 is only valid for <font SIZE="-1">EV5</font>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<p> <i></i><font SIZE="-1"><i>DEC</i></font><i> Alpha/VMS Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">DEC</font> Alpha/VMS implementations: <br />
 </p>
<dl>
<dt><code>-mvms-return-codes</code></dt>
<dd> <p> Return <font SIZE="-1">VMS</font> condition codes from main. The default is to return <font SIZE="-1">POSIX</font> style condition (e.g. error) codes. </p>
 </dd></dl>
<p> <i>Clipper Options</i>  </p>
<p> These <code>-m</code> options are defined for the Clipper implementations: <br />
 </p>
<dl>
<dt><code>-mc300</code></dt>
<dd> <p> Produce code for a C300 Clipper processor. This is the default. <br />
 </p>
 </dd>
<dt><code>-mc400</code></dt>
<dd> <p> Produce code for a C400 Clipper processor, i.e. use floating point registers f8---f15. </p>
 </dd></dl>
<p> <i>H8/300 Options</i>  </p>
<p> These <code>-m</code> options are defined for the H8/300 implementations: <br />
 </p>
<dl>
<dt><code>-mrelax</code></dt>
<dd> <p> Shorten some address references at link time, when possible; uses the linker option <code>-relax</code>. <br />
 </p>
 </dd>
<dt><code>-mh</code></dt>
<dd> <p> Generate code for the H8/300H. <br />
 </p>
 </dd>
<dt><code>-ms</code></dt>
<dd> <p> Generate code for the H8/S. <br />
 </p>
 </dd>
<dt><code>-ms2600</code></dt>
<dd> <p> Generate code for the H8/S2600. This switch must be used with <code>-ms</code>. <br />
 </p>
 </dd>
<dt><code>-mint32</code></dt>
<dd> <p> Make <code>&quot;int&quot;</code> data 32 bits by default. <br />
 </p>
 </dd>
<dt><code>-malign-300</code></dt>
<dd> <p> On the H8/300H and H8/S, use the same alignment rules as for the H8/300. The default for the H8/300H and H8/S is to align longs and floats on 4 byte boundaries. <code>-malign-300</code> causes them to be aligned on 2 byte boundaries. This option has no effect on the H8/300. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>SH</i></font><i> Options</i>  </p>
<p> These <code>-m</code> options are defined for the <font SIZE="-1">SH</font> implementations: <br />
 </p>
<dl>
<dt><code>-m1</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH1</font>. <br />
 </p>
 </dd>
<dt><code>-m2</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH2</font>. <br />
 </p>
 </dd>
<dt><code>-m3</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH3</font>. <br />
 </p>
 </dd>
<dt><code>-m3e</code></dt>
<dd> <p> Generate code for the SH3e. <br />
 </p>
 </dd>
<dt><code>-m4-nofpu</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH4</font> without a floating-point unit. <br />
 </p>
 </dd>
<dt><code>-m4-single-only</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH4</font> with a floating-point unit that only supports single-precision arithmetic. <br />
 </p>
 </dd>
<dt><code>-m4-single</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH4</font> assuming the floating-point unit is in single-precision mode by default. <br />
 </p>
 </dd>
<dt><code>-m4</code></dt>
<dd> <p> Generate code for the <font SIZE="-1">SH4</font>. <br />
 </p>
 </dd>
<dt><code>-mb</code></dt>
<dd> <p> Compile code for the processor in big endian mode. <br />
 </p>
 </dd>
<dt><code>-ml</code></dt>
<dd> <p> Compile code for the processor in little endian mode. <br />
 </p>
 </dd>
<dt><code>-mdalign</code></dt>
<dd> <p> Align doubles at 64-bit boundaries. Note that this changes the calling conventions, and thus some functions from the standard C library will not work unless you recompile it first with <code>-mdalign</code>. <br />
 </p>
 </dd>
<dt><code>-mrelax</code></dt>
<dd> <p> Shorten some address references at link time, when possible; uses the linker option <code>-relax</code>. <br />
 </p>
 </dd>
<dt><code>-mbigtable</code></dt>
<dd> <p> Use 32-bit offsets in <code>&quot;switch&quot;</code> tables. The default is to use 16-bit offsets. <br />
 </p>
 </dd>
<dt><code>-mfmovd</code></dt>
<dd> <p> Enable the use of the instruction <code>&quot;fmovd&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mhitachi</code></dt>
<dd> <p> Comply with the calling conventions defined by Hitachi. <br />
 </p>
 </dd>
<dt><code>-mnomacsave</code></dt>
<dd> <p> Mark the <code>&quot;MAC&quot;</code> register as call-clobbered, even if <code>-mhitachi</code> is given. <br />
 </p>
 </dd>
<dt><code>-mieee</code></dt>
<dd> <p> Increase IEEE-compliance of floating-point code. <br />
 </p>
 </dd>
<dt><code>-misize</code></dt>
<dd> <p> Dump instruction size and location in the assembly code. <br />
 </p>
 </dd>
<dt><code>-mpadstruct</code></dt>
<dd> <p> This option is deprecated. It pads structures to multiple of 4 bytes, which is incompatible with the <font SIZE="-1">SH</font> <font SIZE="-1">ABI</font>. <br />
 </p>
 </dd>
<dt><code>-mspace</code></dt>
<dd> <p> Optimize for space instead of speed. Implied by <code>-Os</code>. <br />
 </p>
 </dd>
<dt><code>-mprefergot</code></dt>
<dd> <p> When generating position-independent code, emit function calls using the Global Offset Table instead of the Procedure Linkage Table. <br />
 </p>
 </dd>
<dt><code>-musermode</code></dt>
<dd> <p> Generate a library function call to invalidate instruction cache entries, after fixing up a trampoline. This library function call doesn&#8217;t assume it can write to the whole memory address space. This is the default when the target is <code>&quot;sh-*-linux*&quot;</code>. </p>
 </dd></dl>
<p> <i>Options for System V</i>  </p>
<p> These additional options are available on System V Release 4 for compatibility with other compilers on those systems: <br />
 </p>
<dl>
<dt><code>-G</code></dt>
<dd> <p> Create a shared object. It is recommended that <code>-symbolic</code> or <code>-shared</code> be used instead. <br />
 </p>
 </dd>
<dt><code>-Qy</code></dt>
<dd> <p> Identify the versions of each tool used by the compiler, in a <code>&quot;.ident&quot;</code> assembler directive in the output. <br />
 </p>
 </dd>
<dt><code>-Qn</code></dt>
<dd> <p> Refrain from adding <code>&quot;.ident&quot;</code> directives to the output file (this is the default). <br />
 </p>
 </dd>
<dt><code>-YP,</code><i>dirs</i></dt>
<dd> <p> Search the directories <i>dirs</i>, and no others, for libraries specified with <code>-l</code>. <br />
 </p>
 </dd>
<dt><code>-Ym,</code><i>dir</i></dt>
<dd> <p> Look in the directory <i>dir</i> to find the M4 preprocessor. The assembler uses this option. </p>
 </dd></dl>
<p> <i>TMS320C3x/C4x Options</i>  </p>
<p> These <code>-m</code> options are defined for TMS320C3x/C4x implementations: <br />
 </p>
<dl>
<dt><code>-mcpu=</code><i>cpu_type</i></dt>
<dd> <p> Set the instruction set, register set, and instruction scheduling parameters for machine type <i>cpu_type</i>. Supported values for <i>cpu_type</i> are <code>c30</code>, <code>c31</code>, <code>c32</code>, <code>c40</code>, and <code>c44</code>. The default is <code>c40</code> to generate code for the <font SIZE="-1">TMS320C40</font>. <br />
 </p>
 </dd>
<dt><code>-mbig-memory</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mbig</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msmall-memory</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msmall</code></dt>
<dd> <p> Generates code for the big or small memory model. The small memory model assumed that all data fits into one 64K word page. At run-time the data page (<font SIZE="-1">DP</font>) register must be set to point to the 64K page containing the .bss and .data program sections. The big memory model is the default and requires reloading of the <font SIZE="-1">DP</font> register for every direct memory access. <br />
 </p>
 </dd>
<dt><code>-mbk</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-bk</code></dt>
<dd> <p> Allow (disallow) allocation of general integer operands into the block count register <font SIZE="-1">BK</font>. <br />
 </p>
 </dd>
<dt><code>-mdb</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-db</code></dt>
<dd> <p> Enable (disable) generation of code using decrement and branch, <i>DBcond</i>(D), instructions. This is enabled by default for the C4x. To be on the safe side, this is disabled for the C3x, since the maximum iteration count on the C3x is 2^{23 + 1} (but who iterates loops more than 2^{23} times on the C3x?). Note that <font SIZE="-1">GCC</font> will try to reverse a loop so that it can utilise the decrement and branch instruction, but will give up if there is more than one memory reference in the loop. Thus a loop where the loop counter is decremented can generate slightly more efficient code, in cases where the <font SIZE="-1">RPTB</font> instruction cannot be utilised. <br />
 </p>
 </dd>
<dt><code>-mdp-isr-reload</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mparanoid</code></dt>
<dd> <p> Force the <font SIZE="-1">DP</font> register to be saved on entry to an interrupt service routine (<font SIZE="-1">ISR</font>), reloaded to point to the data section, and restored on exit from the <font SIZE="-1">ISR</font>. This should not be required unless someone has violated the small memory model by modifying the <font SIZE="-1">DP</font> register, say within an object library. <br />
 </p>
 </dd>
<dt><code>-mmpyi</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mpyi</code></dt>
<dd> <p> For the C3x use the 24-bit <font SIZE="-1">MPYI</font> instruction for integer multiplies instead of a library call to guarantee 32-bit results. Note that if one of the operands is a constant, then the multiplication will be performed using shifts and adds. If the <code>-mmpyi</code> option is not specified for the C3x, then squaring operations are performed inline instead of a library call. <br />
 </p>
 </dd>
<dt><code>-mfast-fix</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fast-fix</code></dt>
<dd> <p> The C3x/C4x <font SIZE="-1">FIX</font> instruction to convert a floating point value to an integer value chooses the nearest integer less than or equal to the floating point value rather than to the nearest integer. Thus if the floating point number is negative, the result will be incorrectly truncated an additional code is necessary to detect and correct this case. This option can be used to disable generation of the additional code required to correct the result. <br />
 </p>
 </dd>
<dt><code>-mrptb</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-rptb</code></dt>
<dd> <p> Enable (disable) generation of repeat block sequences using the <font SIZE="-1">RPTB</font> instruction for zero overhead looping. The <font SIZE="-1">RPTB</font> construct is only used for innermost loops that do not call functions or jump across the loop boundaries. There is no advantage having nested <font SIZE="-1">RPTB</font> loops due to the overhead required to save and restore the <font SIZE="-1">RC</font>, <font SIZE="-1">RS</font>, and <font SIZE="-1">RE</font> registers. This is enabled by default with <code>-O2</code>. <br />
 </p>
 </dd>
<dt><code>-mrpts=</code><i>count</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-rpts</code></dt>
<dd> <p> Enable (disable) the use of the single instruction repeat instruction <font SIZE="-1">RPTS</font>. If a repeat block contains a single instruction, and the loop count can be guaranteed to be less than the value <i>count</i>, <font SIZE="-1">GCC</font> will emit a <font SIZE="-1">RPTS</font> instruction instead of a <font SIZE="-1">RPTB</font>. If no value is specified, then a <font SIZE="-1">RPTS</font> will be emitted even if the loop count cannot be determined at compile time. Note that the repeated instruction following <font SIZE="-1">RPTS</font> does not have to be reloaded from memory each iteration, thus freeing up the <font SIZE="-1">CPU</font> buses for operands. However, since interrupts are blocked by this instruction, it is disabled by default. <br />
 </p>
 </dd>
<dt><code>-mloop-unsigned</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-loop-unsigned</code></dt>
<dd> <p> The maximum iteration count when using <font SIZE="-1">RPTS</font> and <font SIZE="-1">RPTB</font> (and <font SIZE="-1">DB</font> on the C40) is 2^{31 + 1} since these instructions test if the iteration count is negative to terminate the loop. If the iteration count is unsigned there is a possibility than the 2^{31 + 1} maximum iteration count may be exceeded. This switch allows an unsigned iteration count. <br />
 </p>
 </dd>
<dt><code>-mti</code></dt>
<dd> <p> Try to emit an assembler syntax that the <font SIZE="-1">TI</font> assembler (asm30) is happy with. This also enforces compatibility with the <font SIZE="-1">API</font> employed by the <font SIZE="-1">TI</font> C3x C compiler. For example, long doubles are passed as structures rather than in floating point registers. <br />
 </p>
 </dd>
<dt><code>-mregparm</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mmemparm</code></dt>
<dd> <p> Generate code that uses registers (stack) for passing arguments to functions. By default, arguments are passed in registers where possible rather than by pushing arguments on to the stack. <br />
 </p>
 </dd>
<dt><code>-mparallel-insns</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-parallel-insns</code></dt>
<dd> <p> Allow the generation of parallel instructions. This is enabled by default with <code>-O2</code>. <br />
 </p>
 </dd>
<dt><code>-mparallel-mpy</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-parallel-mpy</code></dt>
<dd> <p> Allow the generation of MPY||ADD and MPY||SUB parallel instructions, provided <code>-mparallel-insns</code> is also specified. These instructions have tight register constraints which can pessimize the code generation of large functions. </p>
 </dd></dl>
<p> <i>V850 Options</i>  </p>
<p> These <code>-m</code> options are defined for V850 implementations: <br />
 </p>
<dl>
<dt><code>-mlong-calls</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-long-calls</code></dt>
<dd> <p> Treat all calls as being far away (near). If calls are assumed to be far away, the compiler will always load the functions address up into a register, and call indirect through the pointer. <br />
 </p>
 </dd>
<dt><code>-mno-ep</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mep</code></dt>
<dd> <p> Do not optimize (do optimize) basic blocks that use the same index pointer 4 or more times to copy pointer into the <code>&quot;ep&quot;</code> register, and use the shorter <code>&quot;sld&quot;</code> and <code>&quot;sst&quot;</code> instructions. The <code>-mep</code> option is on by default if you optimize. <br />
 </p>
 </dd>
<dt><code>-mno-prolog-function</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mprolog-function</code></dt>
<dd> <p> Do not use (do use) external functions to save and restore registers at the prolog and epilog of a function. The external functions are slower, but use less code space if more than one function saves the same number of registers. The <code>-mprolog-function</code> option is on by default if you optimize. <br />
 </p>
 </dd>
<dt><code>-mspace</code></dt>
<dd> <p> Try to make the code as small as possible. At present, this just turns on the <code>-mep</code> and <code>-mprolog-function</code> options. <br />
 </p>
 </dd>
<dt><code>-mtda=</code><i>n</i></dt>
<dd> <p> Put static or global variables whose size is <i>n</i> bytes or less into the tiny data area that register <code>&quot;ep&quot;</code> points to. The tiny data area can hold up to 256 bytes in total (128 bytes for byte references). <br />
 </p>
 </dd>
<dt><code>-msda=</code><i>n</i></dt>
<dd> <p> Put static or global variables whose size is <i>n</i> bytes or less into the small data area that register <code>&quot;gp&quot;</code> points to. The small data area can hold up to 64 kilobytes. <br />
 </p>
 </dd>
<dt><code>-mzda=</code><i>n</i></dt>
<dd> <p> Put static or global variables whose size is <i>n</i> bytes or less into the first 32 kilobytes of memory. <br />
 </p>
 </dd>
<dt><code>-mv850</code></dt>
<dd> <p> Specify that the target processor is the V850. <br />
 </p>
 </dd>
<dt><code>-mbig-switch</code></dt>
<dd> <p> Generate code suitable for big switch tables. Use this option only if the assembler/linker complain about out of range branches within a switch table. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>ARC</i></font><i> Options</i>  </p>
<p> These options are defined for <font SIZE="-1">ARC</font> implementations: <br />
 </p>
<dl>
<dt><code>-EL</code></dt>
<dd> <p> Compile code for little endian mode. This is the default. <br />
 </p>
 </dd>
<dt><code>-EB</code></dt>
<dd> <p> Compile code for big endian mode. <br />
 </p>
 </dd>
<dt><code>-mmangle-cpu</code></dt>
<dd> <p> Prepend the name of the cpu to all public symbol names. In multiple-processor systems, there are many <font SIZE="-1">ARC</font> variants with different instruction and register set characteristics. This flag prevents code compiled for one cpu to be linked with code compiled for another. No facility exists for handling variants that are ``almost identical&#8217;&#8216;. This is an all or nothing option. <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>cpu</i></dt>
<dd> <p> Compile code for <font SIZE="-1">ARC</font> variant <i>cpu</i>. Which variants are supported depend on the configuration. All variants support <code>-mcpu=base</code>, this is the default. <br />
 </p>
 </dd>
<dt><code>-mtext=</code><i>text-section</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mdata=</code><i>data-section</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mrodata=</code><i>readonly-data-section</i></dt>
<dd> <p> Put functions, data, and readonly data in <i>text-section</i>, <i>data-section</i>, and <i>readonly-data-section</i> respectively by default. This can be overridden with the <code>&quot;section&quot;</code> attribute. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>NS32K</i></font><i> Options</i>  </p>
<p> These are the <code>-m</code> options defined for the 32000 series. The default values for these options depends on which style of 32000 was selected when the compiler was configured; the defaults for the most common choices are given below. <br />
 </p>
<dl>
<dt><code>-m32032</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m32032</code></dt>
<dd> <p> Generate output for a 32032. This is the default when the compiler is configured for 32032 and 32016 based systems. <br />
 </p>
 </dd>
<dt><code>-m32332</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m32332</code></dt>
<dd> <p> Generate output for a 32332. This is the default when the compiler is configured for 32332-based systems. <br />
 </p>
 </dd>
<dt><code>-m32532</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m32532</code></dt>
<dd> <p> Generate output for a 32532. This is the default when the compiler is configured for 32532-based systems. <br />
 </p>
 </dd>
<dt><code>-m32081</code></dt>
<dd> <p> Generate output containing 32081 instructions for floating point. This is the default for all systems. <br />
 </p>
 </dd>
<dt><code>-m32381</code></dt>
<dd> <p> Generate output containing 32381 instructions for floating point. This also implies <code>-m32081</code>. The 32381 is only compatible with the 32332 and 32532 cpus. This is the default for the pc532-netbsd configuration. <br />
 </p>
 </dd>
<dt><code>-mmulti-add</code></dt>
<dd> <p> Try and generate multiply-add floating point instructions <code>&quot;polyF&quot;</code> and <code>&quot;dotF&quot;</code>. This option is only available if the <code>-m32381</code> option is in effect. Using these instructions requires changes to register allocation which generally has a negative impact on performance. This option should only be enabled when compiling code particularly likely to make heavy use of multiply-add instructions. <br />
 </p>
 </dd>
<dt><code>-mnomulti-add</code></dt>
<dd> <p> Do not try and generate multiply-add floating point instructions <code>&quot;polyF&quot;</code> and <code>&quot;dotF&quot;</code>. This is the default on all platforms. <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Generate output containing library calls for floating point. <code>Warning:</code> the requisite libraries may not be available. <br />
 </p>
 </dd>
<dt><code>-mnobitfield</code></dt>
<dd> <p> Do not use the bit-field instructions. On some machines it is faster to use shifting and masking operations. This is the default for the pc532. <br />
 </p>
 </dd>
<dt><code>-mbitfield</code></dt>
<dd> <p> Do use the bit-field instructions. This is the default for all platforms except the pc532. <br />
 </p>
 </dd>
<dt><code>-mrtd</code></dt>
<dd> <p> Use a different function-calling convention, in which functions that take a fixed number of arguments return pop their arguments on return with the <code>&quot;ret&quot;</code> instruction. </p>
<p> This calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. </p>
<p> Also, you must provide function prototypes for all functions that take variable numbers of arguments (including <code>&quot;printf&quot;</code>); otherwise incorrect code will be generated for calls to those functions. </p>
<p> In addition, seriously incorrect code will result if you call a function with too many arguments. (Normally, extra arguments are harmlessly ignored.) </p>
<p> This option takes its name from the 680x0 <code>&quot;rtd&quot;</code> instruction. <br />
 </p>
 </dd>
<dt><code>-mregparam</code></dt>
<dd> <p> Use a different function-calling convention where the first two arguments are passed in registers. </p>
<p> This calling convention is incompatible with the one normally used on Unix, so you cannot use it if you need to call libraries compiled with the Unix compiler. <br />
 </p>
 </dd>
<dt><code>-mnoregparam</code></dt>
<dd> <p> Do not pass any arguments in registers. This is the default for all targets. <br />
 </p>
 </dd>
<dt><code>-msb</code></dt>
<dd> <p> It is <font SIZE="-1">OK</font> to use the sb as an index register which is always loaded with zero. This is the default for the pc532-netbsd target. <br />
 </p>
 </dd>
<dt><code>-mnosb</code></dt>
<dd> <p> The sb register is not available for use or has not been initialized to zero by the run time system. This is the default for all targets except the pc532-netbsd. It is also implied whenever <code>-mhimem</code> or <code>-fpic</code> is set. <br />
 </p>
 </dd>
<dt><code>-mhimem</code></dt>
<dd> <p> Many ns32000 series addressing modes use displacements of up to 512MB. If an address is above 512MB then displacements from zero can not be used. This option causes code to be generated which can be loaded above 512MB. This may be useful for operating systems or <font SIZE="-1">ROM</font> code. <br />
 </p>
 </dd>
<dt><code>-mnohimem</code></dt>
<dd> <p> Assume code will be loaded in the first 512MB of virtual address space. This is the default for all platforms. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>AVR</i></font><i> Options</i>  </p>
<p> These options are defined for <font SIZE="-1">AVR</font> implementations: <br />
 </p>
<dl>
<dt><code>-mmcu=</code><i>mcu</i></dt>
<dd> <p> Specify <font SIZE="-1">ATMEL</font> <font SIZE="-1">AVR</font> instruction set or <font SIZE="-1">MCU</font> type. </p>
<p> Instruction set avr1 is for the minimal <font SIZE="-1">AVR</font> core, not supported by the C compiler, only for assembler programs (<font SIZE="-1">MCU</font> types: at90s1200, attiny10, attiny11, attiny12, attiny15, attiny28). </p>
<p> Instruction set avr2 (default) is for the classic <font SIZE="-1">AVR</font> core with up to 8K program memory space (<font SIZE="-1">MCU</font> types: at90s2313, at90s2323, attiny22, at90s2333, at90s2343, at90s4414, at90s4433, at90s4434, at90s8515, at90c8534, at90s8535). </p>
<p> Instruction set avr3 is for the classic <font SIZE="-1">AVR</font> core with up to 128K program memory space (<font SIZE="-1">MCU</font> types: atmega103, atmega603, at43usb320, at76c711). </p>
<p> Instruction set avr4 is for the enhanced <font SIZE="-1">AVR</font> core with up to 8K program memory space (<font SIZE="-1">MCU</font> types: atmega8, atmega83, atmega85). </p>
<p> Instruction set avr5 is for the enhanced <font SIZE="-1">AVR</font> core with up to 128K program memory space (<font SIZE="-1">MCU</font> types: atmega16, atmega161, atmega163, atmega32, atmega323, atmega64, atmega128, at43usb355, at94k). <br />
 </p>
 </dd>
<dt><code>-msize</code></dt>
<dd> <p> Output instruction sizes to the asm file. <br />
 </p>
 </dd>
<dt><code>-minit-stack=</code><i>N</i></dt>
<dd> <p> Specify the initial stack address, which may be a symbol or numeric value, <code>__stack</code> is the default. <br />
 </p>
 </dd>
<dt><code>-mno-interrupts</code></dt>
<dd> <p> Generated code is not compatible with hardware interrupts. Code size will be smaller. <br />
 </p>
 </dd>
<dt><code>-mcall-prologues</code></dt>
<dd> <p> Functions prologues/epilogues expanded as call to appropriate subroutines. Code size will be smaller. <br />
 </p>
 </dd>
<dt><code>-mno-tablejump</code></dt>
<dd> <p> Do not generate tablejump insns which sometimes increase code size. <br />
 </p>
 </dd>
<dt><code>-mtiny-stack</code></dt>
<dd> <p> Change only the low 8 bits of the stack pointer. </p>
 </dd></dl>
<p> <i>MCore Options</i>  </p>
<p> These are the <code>-m</code> options defined for the Motorola M*Core processors. <br />
 </p>
<dl>
<dt><code>-mhardlit</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mhardlit</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-hardlit</code></dt>
<dd> <p> Inline constants into the code stream if it can be done in two instructions or less. <br />
 </p>
 </dd>
<dt><code>-mdiv</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mdiv</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-div</code></dt>
<dd> <p> Use the divide instruction. (Enabled by default). <br />
 </p>
 </dd>
<dt><code>-mrelax-immediate</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mrelax-immediate</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-relax-immediate</code></dt>
<dd> <p> Allow arbitrary sized immediates in bit operations. <br />
 </p>
 </dd>
<dt><code>-mwide-bitfields</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mwide-bitfields</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-wide-bitfields</code></dt>
<dd> <p> Always treat bit-fields as int-sized. <br />
 </p>
 </dd>
<dt><code>-m4byte-functions</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m4byte-functions</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-4byte-functions</code></dt>
<dd> <p> Force all functions to be aligned to a four byte boundary. <br />
 </p>
 </dd>
<dt><code>-mcallgraph-data</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mcallgraph-data</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-callgraph-data</code></dt>
<dd> <p> Emit callgraph information. <br />
 </p>
 </dd>
<dt><code>-mslow-bytes</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mslow-bytes</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-slow-bytes</code></dt>
<dd> <p> Prefer word access when reading byte quantities. <br />
 </p>
 </dd>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mbig-endian</code></dt>
<dd> <p> Generate code for a little endian target. <br />
 </p>
 </dd>
<dt><code>-m210</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m210</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m340</code></dt>
<dd> <p> Generate code for the 210 processor. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>IA-64</i></font><i> Options</i>  </p>
<p> These are the <code>-m</code> options defined for the Intel <font SIZE="-1">IA-64</font> architecture. <br />
 </p>
<dl>
<dt><code>-mbig-endian</code></dt>
<dd> <p> Generate code for a big endian target. This is the default for <font SIZE="-1">HPUX</font>. <br />
 </p>
 </dd>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> Generate code for a little endian target. This is the default for <font SIZE="-1">AIX5</font> and Linux. <br />
 </p>
 </dd>
<dt><code>-mgnu-as</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-gnu-as</code></dt>
<dd> <p> Generate (or don&#8217;t) code for the <font SIZE="-1">GNU</font> assembler. This is the default. <br />
 </p>
 </dd>
<dt><code>-mgnu-ld</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-gnu-ld</code></dt>
<dd> <p> Generate (or don&#8217;t) code for the <font SIZE="-1">GNU</font> linker. This is the default. <br />
 </p>
 </dd>
<dt><code>-mno-pic</code></dt>
<dd> <p> Generate code that does not use a global pointer register. The result is not position independent code, and violates the <font SIZE="-1">IA-64</font> <font SIZE="-1">ABI</font>. <br />
 </p>
 </dd>
<dt><code>-mvolatile-asm-stop</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-volatile-asm-stop</code></dt>
<dd> <p> Generate (or don&#8217;t) a stop bit immediately before and after volatile asm statements. <br />
 </p>
 </dd>
<dt><code>-mb-step</code></dt>
<dd> <p> Generate code that works around Itanium B step errata. <br />
 </p>
 </dd>
<dt><code>-mregister-names</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-register-names</code></dt>
<dd> <p> Generate (or don&#8217;t) <code>in</code>, <code>loc</code>, and <code>out</code> register names for the stacked registers. This may make assembler output more readable. <br />
 </p>
 </dd>
<dt><code>-mno-sdata</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msdata</code></dt>
<dd> <p> Disable (or enable) optimizations that use the small data section. This may be useful for working around optimizer bugs. <br />
 </p>
 </dd>
<dt><code>-mconstant-gp</code></dt>
<dd> <p> Generate code that uses a single constant global pointer value. This is useful when compiling kernel code. <br />
 </p>
 </dd>
<dt><code>-mauto-pic</code></dt>
<dd> <p> Generate code that is self-relocatable. This implies <code>-mconstant-gp</code>. This is useful when compiling firmware code. <br />
 </p>
 </dd>
<dt><code>-minline-divide-min-latency</code></dt>
<dd> <p> Generate code for inline divides using the minimum latency algorithm. <br />
 </p>
 </dd>
<dt><code>-minline-divide-max-throughput</code></dt>
<dd> <p> Generate code for inline divides using the maximum throughput algorithm. <br />
 </p>
 </dd>
<dt><code>-mno-dwarf2-asm</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mdwarf2-asm</code></dt>
<dd> <p> Don&#8217;t (or do) generate assembler code for the <font SIZE="-1">DWARF2</font> line number debugging info. This may be useful when not using the <font SIZE="-1">GNU</font> assembler. <br />
 </p>
 </dd>
<dt><code>-mfixed-range=</code><i>register-range</i></dt>
<dd> <p> Generate code treating the given register range as fixed registers. A fixed register is one that the register allocator can not use. This is useful when compiling kernel code. A register range is specified as two registers separated by a dash. Multiple register ranges can be specified separated by a comma. </p>
 </dd></dl>
<p> <i>D30V Options</i>  </p>
<p> These <code>-m</code> options are defined for D30V implementations: <br />
 </p>
<dl>
<dt><code>-mextmem</code></dt>
<dd> <p> Link the <code>.text</code>, <code>.data</code>, <code>.bss</code>, <code>.strings</code>, <code>.rodata</code>, <code>.rodata1</code>, <code>.data1</code> sections into external memory, which starts at location <code>&quot;0x80000000&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mextmemory</code></dt>
<dd> <p> Same as the <code>-mextmem</code> switch. <br />
 </p>
 </dd>
<dt><code>-monchip</code></dt>
<dd> <p> Link the <code>.text</code> section into onchip text memory, which starts at location <code>&quot;0x0&quot;</code>. Also link <code>.data</code>, <code>.bss</code>, <code>.strings</code>, <code>.rodata</code>, <code>.rodata1</code>, <code>.data1</code> sections into onchip data memory, which starts at location <code>&quot;0x20000000&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mno-asm-optimize</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-masm-optimize</code></dt>
<dd> <p> Disable (enable) passing <code>-O</code> to the assembler when optimizing. The assembler uses the <code>-O</code> option to automatically parallelize adjacent short instructions where possible. <br />
 </p>
 </dd>
<dt><code>-mbranch-cost=</code><i>n</i></dt>
<dd> <p> Increase the internal costs of branches to <i>n</i>. Higher costs means that the compiler will issue more instructions to avoid doing a branch. The default is 2. <br />
 </p>
 </dd>
<dt><code>-mcond-exec=</code><i>n</i></dt>
<dd> <p> Specify the maximum number of conditionally executed instructions that replace a branch. The default is 4. </p>
 </dd></dl>
<p> <i>S/390 and zSeries Options</i>  </p>
<p> These are the <code>-m</code> options defined for the S/390 and zSeries architecture. <br />
 </p>
<dl>
<dt><code>-mhard-float</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Use (do not use) the hardware floating-point instructions and registers for floating-point operations. When <code>-msoft-float</code> is specified, functions in <i>libgcc.a</i> will be used to perform floating-point operations. When <code>-mhard-float</code> is specified, the compiler generates <font SIZE="-1">IEEE</font> floating-point instructions. This is the default. <br />
 </p>
 </dd>
<dt><code>-mbackchain</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-backchain</code></dt>
<dd> <p> Generate (or do not generate) code which maintains an explicit backchain within the stack frame that points to the caller&#8217;s frame. This is currently needed to allow debugging. The default is to generate the backchain. <br />
 </p>
 </dd>
<dt><code>-msmall-exec</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-small-exec</code></dt>
<dd> <p> Generate (or do not generate) code using the <code>&quot;bras&quot;</code> instruction to do subroutine calls. This only works reliably if the total executable size does not exceed 64k. The default is to use the <code>&quot;basr&quot;</code> instruction instead, which does not have this limitation. <br />
 </p>
 </dd>
<dt><code>-m64</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m31</code></dt>
<dd> <p> When <code>-m31</code> is specified, generate code compliant to the Linux for S/390 <font SIZE="-1">ABI</font>. When <code>-m64</code> is specified, generate code compliant to the Linux for zSeries <font SIZE="-1">ABI</font>. This allows <font SIZE="-1">GCC</font> in particular to generate 64-bit instructions. For the <code>s390</code> targets, the default is <code>-m31</code>, while the <code>s390x</code> targets default to <code>-m64</code>. <br />
 </p>
 </dd>
<dt><code>-mmvcle</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mvcle</code></dt>
<dd> <p> Generate (or do not generate) code using the <code>&quot;mvcle&quot;</code> instruction to perform block moves. When <code>-mno-mvcle</code> is specifed, use a <code>&quot;mvc&quot;</code> loop instead. This is the default. <br />
 </p>
 </dd>
<dt><code>-mdebug</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-debug</code></dt>
<dd> <p> Print (or do not print) additional debug information when compiling. The default is to not print debug information. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>CRIS</i></font><i> Options</i>  </p>
<p> These options are defined specifically for the <font SIZE="-1">CRIS</font> ports. <br />
 </p>
<dl>
<dt><code>-march=</code><i>architecture-type</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mcpu=</code><i>architecture-type</i></dt>
<dd> <p> Generate code for the specified architecture. The choices for <i>architecture-type</i> are <code>v3</code>, <code>v8</code> and <code>v10</code> for respectively <font SIZE="-1">ETRAX</font>&nbsp;<wbr>4, <font SIZE="-1">ETRAX</font>&nbsp;<wbr>100, and <font SIZE="-1">ETRAX</font>&nbsp;<wbr>100&nbsp;<wbr><font SIZE="-1">LX</font>. Default is <code>v0</code> except for cris-axis-linux-gnu, where the default is <code>v10</code>. <br />
 </p>
 </dd>
<dt><code>-mtune=</code><i>architecture-type</i></dt>
<dd> <p> Tune to <i>architecture-type</i> everything applicable about the generated code, except for the <font SIZE="-1">ABI</font> and the set of available instructions. The choices for <i>architecture-type</i> are the same as for <code>-march=</code><i>architecture-type</i>. <br />
 </p>
 </dd>
<dt><code>-mmax-stack-frame=</code><i>n</i></dt>
<dd> <p> Warn when the stack frame of a function exceeds <i>n</i> bytes. <br />
 </p>
 </dd>
<dt><code>-melinux-stacksize=</code><i>n</i></dt>
<dd> <p> Only available with the <code>cris-axis-aout</code> target. Arranges for indications in the program to the kernel loader that the stack of the program should be set to <i>n</i> bytes. <br />
 </p>
 </dd>
<dt><code>-metrax4</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-metrax100</code></dt>
<dd> <p> The options <code>-metrax4</code> and <code>-metrax100</code> are synonyms for <code>-march=v3</code> and <code>-march=v8</code> respectively. <br />
 </p>
 </dd>
<dt><code>-mpdebug</code></dt>
<dd> <p> Enable CRIS-specific verbose debug-related information in the assembly code. This option also has the effect to turn off the <code>#NO_APP</code> formatted-code indicator to the assembler at the beginning of the assembly file. <br />
 </p>
 </dd>
<dt><code>-mcc-init</code></dt>
<dd> <p> Do not use condition-code results from previous instruction; always emit compare and test instructions before use of condition codes. <br />
 </p>
 </dd>
<dt><code>-mno-side-effects</code></dt>
<dd> <p> Do not emit instructions with side-effects in addressing modes other than post-increment. <br />
 </p>
 </dd>
<dt><code>-mstack-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-stack-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mdata-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-data-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mconst-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-const-align</code></dt>
<dd> <p> These options (no-options) arranges (eliminate arrangements) for the stack-frame, individual data and constants to be aligned for the maximum single data access size for the chosen <font SIZE="-1">CPU</font> model. The default is to arrange for 32-bit alignment. <font SIZE="-1">ABI</font> details such as structure layout are not affected by these options. <br />
 </p>
 </dd>
<dt><code>-m32-bit</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m16-bit</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-m8-bit</code></dt>
<dd> <p> Similar to the stack- data- and const-align options above, these options arrange for stack-frame, writable data and constants to all be 32-bit, 16-bit or 8-bit aligned. The default is 32-bit alignment. <br />
 </p>
 </dd>
<dt><code>-mno-prologue-epilogue</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mprologue-epilogue</code></dt>
<dd> <p> With <code>-mno-prologue-epilogue</code>, the normal function prologue and epilogue that sets up the stack-frame are omitted and no return instructions or return sequences are generated in the code. Use this option only together with visual inspection of the compiled code: no warnings or errors are generated when call-saved registers must be saved, or storage for local variable needs to be allocated. <br />
 </p>
 </dd>
<dt><code>-mno-gotplt</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mgotplt</code></dt>
<dd> <p> With <code>-fpic</code> and <code>-fPIC</code>, don&#8217;t generate (do generate) instruction sequences that load addresses for functions from the <font SIZE="-1">PLT</font> part of the <font SIZE="-1">GOT</font> rather than (traditional on other architectures) calls to the <font SIZE="-1">PLT</font>. The default is <code>-mgotplt</code>. <br />
 </p>
 </dd>
<dt><code>-maout</code></dt>
<dd> <p> Legacy no-op option only recognized with the cris-axis-aout target. <br />
 </p>
 </dd>
<dt><code>-melf</code></dt>
<dd> <p> Legacy no-op option only recognized with the cris-axis-elf and cris-axis-linux-gnu targets. <br />
 </p>
 </dd>
<dt><code>-melinux</code></dt>
<dd> <p> Only recognized with the cris-axis-aout target, where it selects a GNU/linux-like multilib, include files and instruction set for <code>-march=v8</code>. <br />
 </p>
 </dd>
<dt><code>-mlinux</code></dt>
<dd> <p> Legacy no-op option only recognized with the cris-axis-linux-gnu target. <br />
 </p>
 </dd>
<dt><code>-sim</code></dt>
<dd> <p> This option, recognized for the cris-axis-aout and cris-axis-elf arranges to link with input-output functions from a simulator library. Code, initialized data and zero-initialized data are allocated consecutively. <br />
 </p>
 </dd>
<dt><code>-sim2</code></dt>
<dd> <p> Like <code>-sim</code>, but pass linker options to locate initialized data at 0x40000000 and zero-initialized data at 0x80000000. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>MMIX</i></font><i> Options</i>  </p>
<p> These options are defined for the <font SIZE="-1">MMIX:</font> <br />
 </p>
<dl>
<dt><code>-mlibfuncs</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-libfuncs</code></dt>
<dd> <p> Specify that intrinsic library functions are being compiled, passing all values in registers, no matter the size. <br />
 </p>
 </dd>
<dt><code>-mepsilon</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-epsilon</code></dt>
<dd> <p> Generate floating-point comparison instructions that compare with respect to the <code>&quot;rE&quot;</code> epsilon register. <br />
 </p>
 </dd>
<dt><code>-mabi=mmixware</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mabi=gnu</code></dt>
<dd> <p> Generate code that passes function parameters and return values that (in the called function) are seen as registers <code>&quot;$0&quot;</code> and up, as opposed to the <font SIZE="-1">GNU</font> <font SIZE="-1">ABI</font> which uses global registers <code>&quot;$231&quot;</code> and up. <br />
 </p>
 </dd>
<dt><code>-mzero-extend</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-zero-extend</code></dt>
<dd> <p> When reading data from memory in sizes shorter than 64 bits, use (do not use) zero-extending load instructions by default, rather than sign-extending ones. <br />
 </p>
 </dd>
<dt><code>-mknuthdiv</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-knuthdiv</code></dt>
<dd> <p> Make the result of a division yielding a remainder have the same sign as the divisor. With the default, <code>-mno-knuthdiv</code>, the sign of the remainder follows the sign of the dividend. Both methods are arithmetically valid, the latter being almost exclusively used. <br />
 </p>
 </dd>
<dt><code>-mtoplevel-symbols</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-toplevel-symbols</code></dt>
<dd> <p> Prepend (do not prepend) a <code>:</code> to all global symbols, so the assembly code can be used with the <code>&quot;PREFIX&quot;</code> assembly directive. <br />
 </p>
 </dd>
<dt><code>-melf</code></dt>
<dd> <p> Generate an executable in the <font SIZE="-1">ELF</font> format, rather than the default <code>mmo</code> format used by the <code>mmix</code> simulator. <br />
 </p>
 </dd>
<dt><code>-mbranch-predict</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-branch-predict</code></dt>
<dd> <p> Use (do not use) the probable-branch instructions, when static branch prediction indicates a probable branch. <br />
 </p>
 </dd>
<dt><code>-mbase-addresses</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-base-addresses</code></dt>
<dd> <p> Generate (do not generate) code that uses <i>base addresses</i>. Using a base address automatically generates a request (handled by the assembler and the linker) for a constant to be set up in a global register. The register is used for one or more base address requests within the range 0 to 255 from the value held in the register. The generally leads to short and fast code, but the number of different data items that can be addressed is limited. This means that a program that uses lots of static data may require <code>-mno-base-addresses</code>. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>PDP-11</i></font><i> Options</i>  </p>
<p> These options are defined for the <font SIZE="-1">PDP-11:</font> <br />
 </p>
<dl>
<dt><code>-mfpu</code></dt>
<dd> <p> Use hardware <font SIZE="-1">FPP</font> floating point. This is the default. (<font SIZE="-1">FIS</font> floating point on the <font SIZE="-1">PDP-11/40</font> is not supported.) <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Do not use hardware floating point. <br />
 </p>
 </dd>
<dt><code>-mac0</code></dt>
<dd> <p> Return floating-point results in ac0 (fr0 in Unix assembler syntax). <br />
 </p>
 </dd>
<dt><code>-mno-ac0</code></dt>
<dd> <p> Return floating-point results in memory. This is the default. <br />
 </p>
 </dd>
<dt><code>-m40</code></dt>
<dd> <p> Generate code for a <font SIZE="-1">PDP-11/40</font>. <br />
 </p>
 </dd>
<dt><code>-m45</code></dt>
<dd> <p> Generate code for a <font SIZE="-1">PDP-11/45</font>. This is the default. <br />
 </p>
 </dd>
<dt><code>-m10</code></dt>
<dd> <p> Generate code for a <font SIZE="-1">PDP-11/10</font>. <br />
 </p>
 </dd>
<dt><code>-mbcopy-builtin</code></dt>
<dd> <p> Use inline <code>&quot;movstrhi&quot;</code> patterns for copying memory. This is the default. <br />
 </p>
 </dd>
<dt><code>-mbcopy</code></dt>
<dd> <p> Do not use inline <code>&quot;movstrhi&quot;</code> patterns for copying memory. <br />
 </p>
 </dd>
<dt><code>-mint16</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-int32</code></dt>
<dd> <p> Use 16-bit <code>&quot;int&quot;</code>. This is the default. <br />
 </p>
 </dd>
<dt><code>-mint32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-int16</code></dt>
<dd> <p> Use 32-bit <code>&quot;int&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mfloat64</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-float32</code></dt>
<dd> <p> Use 64-bit <code>&quot;float&quot;</code>. This is the default. <br />
 </p>
 </dd>
<dt><code>-mfloat32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-float64</code></dt>
<dd> <p> Use 32-bit <code>&quot;float&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-mabshi</code></dt>
<dd> <p> Use <code>&quot;abshi2&quot;</code> pattern. This is the default. <br />
 </p>
 </dd>
<dt><code>-mno-abshi</code></dt>
<dd> <p> Do not use <code>&quot;abshi2&quot;</code> pattern. <br />
 </p>
 </dd>
<dt><code>-mbranch-expensive</code></dt>
<dd> <p> Pretend that branches are expensive. This is for experimenting with code generation only. <br />
 </p>
 </dd>
<dt><code>-mbranch-cheap</code></dt>
<dd> <p> Do not pretend that branches are expensive. This is the default. <br />
 </p>
 </dd>
<dt><code>-msplit</code></dt>
<dd> <p> Generate code for a system with split I&amp;D. <br />
 </p>
 </dd>
<dt><code>-mno-split</code></dt>
<dd> <p> Generate code for a system without split I&amp;D. This is the default. <br />
 </p>
 </dd>
<dt><code>-munix-asm</code></dt>
<dd> <p> Use Unix assembler syntax. This is the default when configured for <code>pdp11-*-bsd</code>. <br />
 </p>
 </dd>
<dt><code>-mdec-asm</code></dt>
<dd> <p> Use <font SIZE="-1">DEC</font> assembler syntax. This is the default when configured for any <font SIZE="-1">PDP-11</font> target other than <code>pdp11-*-bsd</code>. </p>
 </dd></dl>
<p> <i>Xstormy16 Options</i>  </p>
<p> These options are defined for Xstormy16: <br />
 </p>
<dl>
<dt><code>-msim</code></dt>
<dd> <p> Choose startup files and linker script suitable for the simulator. </p>
 </dd></dl>
<p> <i>Xtensa Options</i>  </p>
<p> The Xtensa architecture is designed to support many different configurations. The compiler&#8217;s default options can be set to match a particular Xtensa configuration by copying a configuration file into the <font SIZE="-1">GCC</font> sources when building <font SIZE="-1">GCC</font>. The options below may be used to override the default options. <br />
 </p>
<dl>
<dt><code>-mbig-endian</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mlittle-endian</code></dt>
<dd> <p> Specify big-endian or little-endian byte ordering for the target Xtensa processor. <br />
 </p>
 </dd>
<dt><code>-mdensity</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-density</code></dt>
<dd> <p> Enable or disable use of the optional Xtensa code density instructions. <br />
 </p>
 </dd>
<dt><code>-mmac16</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mac16</code></dt>
<dd> <p> Enable or disable use of the Xtensa <font SIZE="-1">MAC16</font> option. When enabled, <font SIZE="-1">GCC</font> will generate <font SIZE="-1">MAC16</font> instructions from standard C code, with the limitation that it will use neither the <font SIZE="-1">MR</font> register file nor any instruction that operates on the <font SIZE="-1">MR</font> registers. When this option is disabled, <font SIZE="-1">GCC</font> will translate 16-bit multiply/accumulate operations to a combination of core instructions and library calls, depending on whether any other multiplier options are enabled. <br />
 </p>
 </dd>
<dt><code>-mmul16</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mul16</code></dt>
<dd> <p> Enable or disable use of the 16-bit integer multiplier option. When enabled, the compiler will generate 16-bit multiply instructions for multiplications of 16 bits or smaller in standard C code. When this option is disabled, the compiler will either use 32-bit multiply or <font SIZE="-1">MAC16</font> instructions if they are available or generate library calls to perform the multiply operations using shifts and adds. <br />
 </p>
 </dd>
<dt><code>-mmul32</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-mul32</code></dt>
<dd> <p> Enable or disable use of the 32-bit integer multiplier option. When enabled, the compiler will generate 32-bit multiply instructions for multiplications of 32 bits or smaller in standard C code. When this option is disabled, the compiler will generate library calls to perform the multiply operations using either shifts and adds or 16-bit multiply instructions if they are available. <br />
 </p>
 </dd>
<dt><code>-mnsa</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-nsa</code></dt>
<dd> <p> Enable or disable use of the optional normalization shift amount (<code>&quot;NSA&quot;</code>) instructions to implement the built-in <code>&quot;ffs&quot;</code> function. <br />
 </p>
 </dd>
<dt><code>-mminmax</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-minmax</code></dt>
<dd> <p> Enable or disable use of the optional minimum and maximum value instructions. <br />
 </p>
 </dd>
<dt><code>-msext</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-sext</code></dt>
<dd> <p> Enable or disable use of the optional sign extend (<code>&quot;SEXT&quot;</code>) instruction. <br />
 </p>
 </dd>
<dt><code>-mbooleans</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-booleans</code></dt>
<dd> <p> Enable or disable support for the boolean register file used by Xtensa coprocessors. This is not typically useful by itself but may be required for other options that make use of the boolean registers (e.g., the floating-point option). <br />
 </p>
 </dd>
<dt><code>-mhard-float</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-msoft-float</code></dt>
<dd> <p> Enable or disable use of the floating-point option. When enabled, <font SIZE="-1">GCC</font> generates floating-point instructions for 32-bit <code>&quot;float&quot;</code> operations. When this option is disabled, <font SIZE="-1">GCC</font> generates library calls to emulate 32-bit floating-point operations using integer instructions. Regardless of this option, 64-bit <code>&quot;double&quot;</code> operations are always emulated with calls to library functions. <br />
 </p>
 </dd>
<dt><code>-mfused-madd</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-fused-madd</code></dt>
<dd> <p> Enable or disable use of fused multiply/add and multiply/subtract instructions in the floating-point option. This has no effect if the floating-point option is not also enabled. Disabling fused multiply/add and multiply/subtract instructions forces the compiler to use separate instructions for the multiply and add/subtract operations. This may be desirable in some cases where strict <font SIZE="-1">IEEE</font> 754-compliant results are required: the fused multiply add/subtract instructions do not round the intermediate result, thereby producing results with <i>more</i> bits of precision than specified by the <font SIZE="-1">IEEE</font> standard. Disabling fused multiply add/subtract instructions also ensures that the program output is not sensitive to the compiler&#8217;s ability to combine multiply and add/subtract operations. <br />
 </p>
 </dd>
<dt><code>-mserialize-volatile</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-serialize-volatile</code></dt>
<dd> <p> When this option is enabled, <font SIZE="-1">GCC</font> inserts <code>&quot;MEMW&quot;</code> instructions before <code>&quot;volatile&quot;</code> memory references to guarantee sequential consistency. The default is <code>-mserialize-volatile</code>. Use <code>-mno-serialize-volatile</code> to omit the <code>&quot;MEMW&quot;</code> instructions. <br />
 </p>
 </dd>
<dt><code>-mtext-section-literals</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-text-section-literals</code></dt>
<dd> <p> Control the treatment of literal pools. The default is <code>-mno-text-section-literals</code>, which places literals in a separate section in the output file. This allows the literal pool to be placed in a data <font SIZE="-1">RAM/ROM</font>, and it also allows the linker to combine literal pools from separate object files to remove redundant literals and improve code size. With <code>-mtext-section-literals</code>, the literals are interspersed in the text section in order to keep them as close as possible to their references. This may be necessary for large assembly files. <br />
 </p>
 </dd>
<dt><code>-mtarget-align</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-target-align</code></dt>
<dd> <p> When this option is enabled, <font SIZE="-1">GCC</font> instructs the assembler to automatically align instructions to reduce branch penalties at the expense of some code density. The assembler attempts to widen density instructions to align branch targets and the instructions following call instructions. If there are not enough preceding safe density instructions to align a target, no widening will be performed. The default is <code>-mtarget-align</code>. These options do not affect the treatment of auto-aligned instructions like <code>&quot;LOOP&quot;</code>, which the assembler will always align, either by widening density instructions or by inserting no-op instructions. <br />
 </p>
 </dd>
<dt><code>-mlongcalls</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-mno-longcalls</code></dt>
<dd> <p> When this option is enabled, <font SIZE="-1">GCC</font> instructs the assembler to translate direct calls to indirect calls unless it can determine that the target of a direct call is in the range allowed by the call instruction. This translation typically occurs for calls to functions in other source files. Specifically, the assembler translates a direct <code>&quot;CALL&quot;</code> instruction into an <code>&quot;L32R&quot;</code> followed by a <code>&quot;CALLX&quot;</code> instruction. The default is <code>-mno-longcalls</code>. This option should be used in programs where the call target can potentially be out of range. This option is implemented in the assembler, not the compiler, so the assembly code generated by <font SIZE="-1">GCC</font> will still show direct call instructions---look at the disassembled object code to see the actual instructions. Note that the assembler will use an indirect call for every cross-file call, not just those that really will be out of range. </p>
 </dd></dl>
<h2>Options for Code Generation Conventions</h2>
<p> These machine-independent options control the interface conventions used in code generation. </p>
<p> Most of them have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. In the table below, only one of the forms is listed---the one which is not the default. You can figure out the other form by either removing <code>no-</code> or adding it. <br />
 </p>
<dl>
<dt><code>-fexceptions</code></dt>
<dd> <p> Enable exception handling. Generates extra code needed to propagate exceptions. For some targets, this implies <font SIZE="-1">GCC</font> will generate frame unwind information for all functions, which can produce significant data size overhead, although it does not affect execution. If you do not specify this option, <font SIZE="-1">GCC</font> will enable it by default for languages like C<font SIZE="-2">++</font> which normally require exception handling, and disable it for languages like C that do not normally require it. However, you may need to enable this option when compiling C code that needs to interoperate properly with exception handlers written in C<font SIZE="-2">++</font>. You may also wish to disable this option if you are compiling older C<font SIZE="-2">++</font> programs that don&#8217;t use exception handling. <br />
 </p>
 </dd>
<dt><code>-fnon-call-exceptions</code></dt>
<dd> <p> Generate code that allows trapping instructions to throw exceptions. Note that this requires platform-specific runtime support that does not exist everywhere. Moreover, it only allows <i>trapping</i> instructions to throw exceptions, i.e. memory references or floating point instructions. It does not allow exceptions to be thrown from arbitrary signal handlers such as <code>&quot;SIGALRM&quot;</code>. <br />
 </p>
 </dd>
<dt><code>-funwind-tables</code></dt>
<dd> <p> Similar to <code>-fexceptions</code>, except that it will just generate any needed static data, but will not affect the generated code in any other way. You will normally not enable this option; instead, a language processor that needs this handling would enable it on your behalf. <br />
 </p>
 </dd>
<dt><code>-fasynchronous-unwind-tables</code></dt>
<dd> <p> Generate unwind table in dwarf2 format, if supported by target machine. The table is exact at each instruction boundary, so it can be used for stack unwinding from asynchronous events (such as debugger or garbage collector). <br />
 </p>
 </dd>
<dt><code>-fpcc-struct-return</code></dt>
<dd> <p> Return ``short&#8217;&#8216; <code>&quot;struct&quot;</code> and <code>&quot;union&quot;</code> values in memory like longer ones, rather than in registers. This convention is less efficient, but it has the advantage of allowing intercallability between GCC-compiled files and files compiled with other compilers, particularly the Portable C Compiler (pcc). </p>
<p> The precise convention for returning structures in memory depends on the target configuration macros. </p>
<p> Short structures and unions are those whose size and alignment match that of some integer type. </p>
<p> <code>Warning:</code> code compiled with the <code>-fpcc-struct-return</code> switch is not binary compatible with code compiled with the <code>-freg-struct-return</code> switch. Use it to conform to a non-default application binary interface. <br />
 </p>
 </dd>
<dt><code>-freg-struct-return</code></dt>
<dd> <p> Return <code>&quot;struct&quot;</code> and <code>&quot;union&quot;</code> values in registers when possible. This is more efficient for small structures than <code>-fpcc-struct-return</code>. </p>
<p> If you specify neither <code>-fpcc-struct-return</code> nor <code>-freg-struct-return</code>, <font SIZE="-1">GCC</font> defaults to whichever convention is standard for the target. If there is no standard convention, <font SIZE="-1">GCC</font> defaults to <code>-fpcc-struct-return</code>, except on targets where <font SIZE="-1">GCC</font> is the principal compiler. In those cases, we can choose the standard, and we chose the more efficient register return alternative. </p>
<p> <code>Warning:</code> code compiled with the <code>-freg-struct-return</code> switch is not binary compatible with code compiled with the <code>-fpcc-struct-return</code> switch. Use it to conform to a non-default application binary interface. <br />
 </p>
 </dd>
<dt><code>-fshort-enums</code></dt>
<dd> <p> Allocate to an <code>&quot;enum&quot;</code> type only as many bytes as it needs for the declared range of possible values. Specifically, the <code>&quot;enum&quot;</code> type will be equivalent to the smallest integer type which has enough room. </p>
<p> <code>Warning:</code> the <code>-fshort-enums</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface. <br />
 </p>
 </dd>
<dt><code>-fshort-double</code></dt>
<dd> <p> Use the same size for <code>&quot;double&quot;</code> as for <code>&quot;float&quot;</code>. </p>
<p> <code>Warning:</code> the <code>-fshort-double</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface. <br />
 </p>
 </dd>
<dt><code>-fshort-wchar</code></dt>
<dd> <p> Override the underlying type for <code>wchar_t</code> to be <code>short unsigned int</code> instead of the default for the target. This option is useful for building programs to run under <font SIZE="-1">WINE</font>. </p>
<p> <code>Warning:</code> the <code>-fshort-wchar</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface. <br />
 </p>
 </dd>
<dt><code>-fshared-data</code></dt>
<dd> <p> Requests that the data and non-<code>&quot;const&quot;</code> variables of this compilation be shared data rather than private data. The distinction makes sense only on certain operating systems, where shared data is shared between processes running the same program, while private data exists in one copy per process. <br />
 </p>
 </dd>
<dt><code>-fno-common</code></dt>
<dd> <p> In C, allocate even uninitialized global variables in the data section of the object file, rather than generating them as common blocks. This has the effect that if the same variable is declared (without <code>&quot;extern&quot;</code>) in two different compilations, you will get an error when you link them. The only reason this might be useful is if you wish to verify that the program will work on other systems which always work this way. <br />
 </p>
 </dd>
<dt><code>-fno-ident</code></dt>
<dd> <p> Ignore the <code>#ident</code> directive. <br />
 </p>
 </dd>
<dt><code>-fno-gnu-linker</code></dt>
<dd> <p> Do not output global initializations (such as C<font SIZE="-2">++</font> constructors and destructors) in the form used by the <font SIZE="-1">GNU</font> linker (on systems where the <font SIZE="-1">GNU</font> linker is the standard method of handling them). Use this option when you want to use a non-GNU linker, which also requires using the <code>collect2</code> program to make sure the system linker includes constructors and destructors. (<code>collect2</code> is included in the <font SIZE="-1">GCC</font> distribution.) For systems which <i>must</i> use <code>collect2</code>, the compiler driver <code>gcc</code> is configured to do this automatically. <br />
 </p>
 </dd>
<dt><code>-finhibit-size-directive</code></dt>
<dd> <p> Don&#8217;t output a <code>&quot;.size&quot;</code> assembler directive, or anything else that would cause trouble if the function is split in the middle, and the two halves are placed at locations far apart in memory. This option is used when compiling <i>crtstuff.c</i>; you should not need to use it for anything else. <br />
 </p>
 </dd>
<dt><code>-fverbose-asm</code></dt>
<dd> <p> Put extra commentary information in the generated assembly code to make it more readable. This option is generally only of use to those who actually need to read the generated assembly code (perhaps while debugging the compiler itself). </p>
<p> <code>-fno-verbose-asm</code>, the default, causes the extra information to be omitted and is useful when comparing two assembler files. <br />
 </p>
 </dd>
<dt><code>-fvolatile</code></dt>
<dd> <p> Consider all memory references through pointers to be volatile. <br />
 </p>
 </dd>
<dt><code>-fvolatile-global</code></dt>
<dd> <p> Consider all memory references to extern and global data items to be volatile. <font SIZE="-1">GCC</font> does not consider static data items to be volatile because of this switch. <br />
 </p>
 </dd>
<dt><code>-fvolatile-static</code></dt>
<dd> <p> Consider all memory references to static data to be volatile. <br />
 </p>
 </dd>
<dt><code>-fpic</code></dt>
<dd> <p> Generate position-independent code (<font SIZE="-1">PIC</font>) suitable for use in a shared library, if supported for the target machine. Such code accesses all constant addresses through a global offset table (<font SIZE="-1">GOT</font>). The dynamic loader resolves the <font SIZE="-1">GOT</font> entries when the program starts (the dynamic loader is not part of <font SIZE="-1">GCC</font>; it is part of the operating system). If the <font SIZE="-1">GOT</font> size for the linked executable exceeds a machine-specific maximum size, you get an error message from the linker indicating that <code>-fpic</code> does not work; in that case, recompile with <code>-fPIC</code> instead. (These maximums are 16k on the m88k, 8k on the Sparc, and 32k on the m68k and <font SIZE="-1">RS/6000</font>. The 386 has no such limit.) </p>
<p> Position-independent code requires special support, and therefore works only on certain machines. For the 386, <font SIZE="-1">GCC</font> supports <font SIZE="-1">PIC</font> for System V but not for the Sun 386i. Code generated for the <font SIZE="-1">IBM</font> <font SIZE="-1">RS/6000</font> is always position-independent. <br />
 </p>
 </dd>
<dt><code>-fPIC</code></dt>
<dd> <p> If supported for the target machine, emit position-independent code, suitable for dynamic linking and avoiding any limit on the size of the global offset table. This option makes a difference on the m68k, m88k, and the Sparc. </p>
<p> Position-independent code requires special support, and therefore works only on certain machines. <br />
 </p>
 </dd>
<dt><code>-ffixed-</code><i>reg</i></dt>
<dd> <p> Treat the register named <i>reg</i> as a fixed register; generated code should never refer to it (except perhaps as a stack pointer, frame pointer or in some other fixed role). </p>
<p> <i>reg</i> must be the name of a register. The register names accepted are machine-specific and are defined in the <code>&quot;REGISTER_NAMES&quot;</code> macro in the machine description macro file. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice. <br />
 </p>
 </dd>
<dt><code>-fcall-used-</code><i>reg</i></dt>
<dd> <p> Treat the register named <i>reg</i> as an allocable register that is clobbered by function calls. It may be allocated for temporaries or variables that do not live across a call. Functions compiled this way will not save and restore the register <i>reg</i>. </p>
<p> It is an error to used this flag with the frame pointer or stack pointer. Use of this flag for other registers that have fixed pervasive roles in the machine&#8217;s execution model will produce disastrous results. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice. <br />
 </p>
 </dd>
<dt><code>-fcall-saved-</code><i>reg</i></dt>
<dd> <p> Treat the register named <i>reg</i> as an allocable register saved by functions. It may be allocated even for temporaries or variables that live across a call. Functions compiled this way will save and restore the register <i>reg</i> if they use it. </p>
<p> It is an error to used this flag with the frame pointer or stack pointer. Use of this flag for other registers that have fixed pervasive roles in the machine&#8217;s execution model will produce disastrous results. </p>
<p> A different sort of disaster will result from the use of this flag for a register in which function values may be returned. </p>
<p> This flag does not have a negative form, because it specifies a three-way choice. <br />
 </p>
 </dd>
<dt><code>-fpack-struct</code></dt>
<dd> <p> Pack all structure members together without holes. </p>
<p> <code>Warning:</code> the <code>-fpack-struct</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Additionally, it makes the code suboptimial. Use it to conform to a non-default application binary interface. <br />
 </p>
 </dd>
<dt><code>-finstrument-functions</code></dt>
<dd> <p> Generate instrumentation calls for entry and exit to functions. Just after function entry and just before function exit, the following profiling functions will be called with the address of the current function and its call site. (On some platforms, <code>&quot;__builtin_return_address&quot;</code> does not work beyond the current function, so the call site information may not be available to the profiling functions otherwise.) </p>
<pre><code>        void __cyg_profile_func_enter (void *this_fn,
                                       void *call_site);
        void __cyg_profile_func_exit (void *this_fn,
                                       void *call_site);
</code></pre>
<p> The first argument is the address of the start of the current function, which may be looked up exactly in the symbol table. </p>
<p> This instrumentation is also done for functions expanded inline in other functions. The profiling calls will indicate where, conceptually, the inline function is entered and exited. This means that addressable versions of such functions must be available. If all your uses of a function are expanded inline, this may mean an additional expansion of code size. If you use <code>extern inline</code> in your C code, an addressable version of such functions must be provided. (This is normally the case anyways, but if you get lucky and the optimizer always expands the functions inline, you might have gotten away without providing static copies.) </p>
<p> A function may be given the attribute <code>&quot;no_instrument_function&quot;</code>, in which case this instrumentation will not be done. This can be used, for example, for the profiling functions listed above, high-priority interrupt routines, and any functions from which the profiling functions cannot safely be called (perhaps signal handlers, if the profiling routines generate output or allocate memory). <br />
 </p>
 </dd>
<dt><code>-fstack-check</code></dt>
<dd> <p> Generate code to verify that you do not go beyond the boundary of the stack. You should specify this flag if you are running in an environment with multiple threads, but only rarely need to specify it in a single-threaded environment since stack overflow is automatically detected on nearly all systems if there is only one stack. </p>
<p> Note that this switch does not actually cause checking to be done; the operating system must do that. The switch causes generation of code to ensure that the operating system sees the stack being extended. <br />
 </p>
 </dd>
<dt><code>-fstack-limit-register=</code><i>reg</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fstack-limit-symbol=</code><i>sym</i></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fno-stack-limit</code></dt>
<dd> <p> Generate code to ensure that the stack does not grow beyond a certain value, either the value of a register or the address of a symbol. If the stack would grow beyond the value, a signal is raised. For most targets, the signal is raised before the stack overruns the boundary, so it is possible to catch the signal without taking special precautions. </p>
<p> For instance, if the stack starts at absolute address <code>0x80000000</code> and grows downwards, you can use the flags <code>-fstack-limit-symbol=__stack_limit</code> and <code>-Wl,--defsym,__stack_limit=0x7ffe0000</code> to enforce a stack limit of 128KB. Note that this may only work with the <font SIZE="-1">GNU</font> linker. <br />
 </p>
 </dd>
<dt><code>-fargument-alias</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fargument-noalias</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>-fargument-noalias-global</code></dt>
<dd> <p> Specify the possible relationships among parameters and between parameters and global data. </p>
<p> <code>-fargument-alias</code> specifies that arguments (parameters) may alias each other and may alias global storage.<code>-fargument-noalias</code> specifies that arguments do not alias each other, but may alias global storage.<code>-fargument-noalias-global</code> specifies that arguments do not alias each other and do not alias global storage. </p>
<p> Each language will automatically use whatever option is required by the language standard. You should not need to use these options yourself. <br />
 </p>
 </dd>
<dt><code>-fleading-underscore</code></dt>
<dd> <p> This option and its counterpart, <code>-fno-leading-underscore</code>, forcibly change the way C symbols are represented in the object file. One use is to help link with legacy assembly code. </p>
<p> <code>Warning:</code> the <code>-fleading-underscore</code> switch causes <font SIZE="-1">GCC</font> to generate code that is not binary compatible with code generated without that switch. Use it to conform to a non-default application binary interface. Not all targets provide complete support for this switch. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> This section describes several environment variables that affect how <font SIZE="-1">GCC</font> operates. Some of them work by specifying directories or prefixes to use when searching for various kinds of files. Some are used to specify other aspects of the compilation environment. </p>
<p> Note that you can also specify places to search using options such as <code>-B</code>, <code>-I</code> and <code>-L</code>. These take precedence over places specified using environment variables, which in turn take precedence over those specified by the configuration of <font SIZE="-1">GCC</font>. <br />
 </p>
<dl>
<dt><font SIZE="-1"><code>LANG</code></font></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>LC_CTYPE</code></font></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>LC_MESSAGES</code></font></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>LC_ALL</code></font></dt>
<dd> <p> These environment variables control the way that <font SIZE="-1">GCC</font> uses localization information that allow <font SIZE="-1">GCC</font> to work with different national conventions. <font SIZE="-1">GCC</font> inspects the locale categories <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font> if it has been configured to do so. These locale categories can be set to any value supported by your installation. A typical value is <code>en_UK</code> for English in the United Kingdom. </p>
<p> The <font SIZE="-1"><code>LC_CTYPE</code></font> environment variable specifies character classification. <font SIZE="-1">GCC</font> uses it to determine the character boundaries in a string; this is needed for some multibyte encodings that contain quote and escape characters that would otherwise be interpreted as a string end or escape. </p>
<p> The <font SIZE="-1"><code>LC_MESSAGES</code></font> environment variable specifies the language to use in diagnostic messages. </p>
<p> If the <font SIZE="-1"><code>LC_ALL</code></font> environment variable is set, it overrides the value of <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font>; otherwise, <font SIZE="-1"><code>LC_CTYPE</code></font> and <font SIZE="-1"><code>LC_MESSAGES</code></font> default to the value of the <font SIZE="-1"><code>LANG</code></font> environment variable. If none of these variables are set, <font SIZE="-1">GCC</font> defaults to traditional C English behavior. <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>TMPDIR</code></font></dt>
<dd> <p> If <font SIZE="-1"><code>TMPDIR</code></font> is set, it specifies the directory to use for temporary files. <font SIZE="-1">GCC</font> uses temporary files to hold the output of one stage of compilation which is to be used as input to the next stage: for example, the output of the preprocessor, which is the input to the compiler proper. <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font></dt>
<dd> <p> If <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is set, it specifies a prefix to use in the names of the subprograms executed by the compiler. No slash is added when this prefix is combined with the name of a subprogram, but you can specify a prefix that ends with a slash if you wish. </p>
<p> If <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is not set, <font SIZE="-1">GCC</font> will attempt to figure out an appropriate prefix to use based on the pathname it was invoked with. </p>
<p> If <font SIZE="-1">GCC</font> cannot find the subprogram using the specified prefix, it tries looking in the usual places for the subprogram. </p>
<p> The default value of <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font> is <i>prefix/lib/gcc-lib/</i> where <i>prefix</i> is the value of <code>&quot;prefix&quot;</code> when you ran the <i>configure</i> script. </p>
<p> Other prefixes specified with <code>-B</code> take precedence over this prefix. </p>
<p> This prefix is also used for finding files such as <i>crt0.o</i> that are used for linking. </p>
<p> In addition, the prefix is used in an unusual way in finding the directories to search for header files. For each of the standard directories whose name normally begins with <code>/usr/local/lib/gcc-lib</code> (more precisely, with the value of <font SIZE="-1"><code>GCC_INCLUDE_DIR</code></font>), <font SIZE="-1">GCC</font> tries replacing that beginning with the specified prefix to produce an alternate directory name. Thus, with <code>-Bfoo/</code>, <font SIZE="-1">GCC</font> will search <i>foo/bar</i> where it would normally search <i>/usr/local/lib/bar</i>. These alternate directories are searched first; the standard directories come next. <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>COMPILER_PATH</code></font></dt>
<dd> <p> The value of <font SIZE="-1"><code>COMPILER_PATH</code></font> is a colon-separated list of directories, much like <font SIZE="-1"><code>PATH</code></font>. <font SIZE="-1">GCC</font> tries the directories thus specified when searching for subprograms, if it can&#8217;t find the subprograms using <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>LIBRARY_PATH</code></font></dt>
<dd> <p> The value of <font SIZE="-1"><code>LIBRARY_PATH</code></font> is a colon-separated list of directories, much like <font SIZE="-1"><code>PATH</code></font>. When configured as a native compiler, <font SIZE="-1">GCC</font> tries the directories thus specified when searching for special linker files, if it can&#8217;t find them using <font SIZE="-1"><code>GCC_EXEC_PREFIX</code></font>. Linking using <font SIZE="-1">GCC</font> also uses these directories when searching for ordinary libraries for the <code>-l</code> option (but directories specified with <code>-L</code> come first). <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>LANG</code></font></dt>
<dd> <p> This variable is used to pass locale information to the compiler. One way in which this information is used is to determine the character set to be used when character literals, string literals and comments are parsed in C and C<font SIZE="-2">++</font>. When the compiler is configured to allow multibyte characters, the following values for <font SIZE="-1"><code>LANG</code></font> are recognized: </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt><code>C-JIS</code></dt>
<dd> <p> Recognize <font SIZE="-1">JIS</font> characters. <br />
 </p>
 </dd>
<dt><code>C-SJIS</code></dt>
<dd> <p> Recognize <font SIZE="-1">SJIS</font> characters. <br />
 </p>
 </dd>
<dt><code>C-EUCJP</code></dt>
<dd> <p> Recognize <font SIZE="-1">EUCJP</font> characters. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> If <font SIZE="-1"><code>LANG</code></font> is not defined, or if it has some other value, then the compiler will use mblen and mbtowc as defined by the default locale to recognize and translate multibyte characters. </p>
 </dd></dl>
</dl>
<p> Some additional environments variables affect the behavior of the preprocessor. <br />
 </p>
<dl>
<dt><font SIZE="-1"><code>CPATH</code></font></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><code>C_INCLUDE_PATH</code></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>CPLUS_INCLUDE_PATH</code></font></dt>
<dd> <p> <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>OBJC_INCLUDE_PATH</code></font></dt>
<dd> <p> Each variable&#8217;s value is a list of directories separated by a special character, much like <font SIZE="-1"><code>PATH</code></font>, in which to look for header files. The special character, <code>&quot;PATH_SEPARATOR&quot;</code>, is target-dependent and determined at <font SIZE="-1">GCC</font> build time. For Windows-based targets it is a semicolon, and for almost all other targets it is a colon. </p>
<p> <font SIZE="-1"><code>CPATH</code></font> specifies a list of directories to be searched as if specified with <code>-I</code>, but after any paths given with <code>-I</code> options on the command line. The environment variable is used regardless of which language is being preprocessed. </p>
<p> The remaining environment variables apply only when preprocessing the particular language indicated. Each specifies a list of directories to be searched as if specified with <code>-isystem</code>, but after any paths given with <code>-isystem</code> options on the command line. <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font></dt>
<dd> <p> @anchor{<font SIZE="-1">DEPENDENCIES_OUTPUT</font>} If this variable is set, its value specifies how to output dependencies for Make based on the non-system header files processed by the compiler. System header files are ignored in the dependency output. </p>
<p> The value of <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font> can be just a file name, in which case the Make rules are written to that file, guessing the target name from the source file name. Or the value can have the form <i>file</i><i>target</i>, in which case the rules are written to file <i>file</i> using <i>target</i> as the target name. </p>
<p> In other words, this environment variable is equivalent to combining the options <code>-MM</code> and <code>-MF</code>, with an optional <code>-MT</code> switch too. <br />
 </p>
 </dd>
<dt><font SIZE="-1"><code>SUNPRO_DEPENDENCIES</code></font></dt>
<dd> <p> This variable is the same as the environment variable <font SIZE="-1"><code>DEPENDENCIES_OUTPUT</code></font>, except that system header files are not ignored, so it implies <code>-M</code> rather than <code>-MM</code>. However, the dependence on the main input file is omitted. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> For instructions on reporting bugs, see &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/bugs.html">http://gcc.gnu.org/bugs.html</a></code>&gt;. Use of the <code>gccbug</code> script to report bugs is recommended.  </p>
<h2>FOOTNOTES</h2>
<p> <br />
 </p>
<dl>
<dt>1.</dt>
<dd> <p> On some systems, <code>gcc -shared</code> needs to build supplementary stub code for constructors to work. On multi-libbed systems, <code>gcc -shared</code> must select the correct support libraries to link against. Failing to supply the correct flags may lead to subtle defects. Supplying them in cases where they are not necessary is innocuous. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <i>gpl</i>(7), <i>gfdl</i>(7), <i>fsf-funding</i>(7), <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1), <i><a href="/docs/linux/man/1-gcov/">gcov</a></i>(1), <i>g77</i>(1), <i><a href="/docs/linux/man/1-as/">as</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), <i><a href="/docs/linux/man/1-gdb/">gdb</a></i>(1), <i>adb</i>(1), <i>dbx</i>(1), <i>sdb</i>(1) and the Info entries for <i>gcc</i>, <i>cpp</i>, <i>g77</i>, <i>as</i>, <i>ld</i>, <i>binutils</i> and <i>gdb</i>.  </p>
<h2>AUTHOR</h2>
<p> See the Info entry for <code>gcc</code>, or &lt;<code><a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/gcc/Contributors.html">http://gcc.gnu.org/onlinedocs/gcc/Contributors.html</a></code>&gt;, for contributors to <font SIZE="-1">GCC</font>.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1988, 1989, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with the Invariant Sections being ``<font SIZE="-1">GNU</font> General Public License&#8217;&#8216; and ``Funding Free Software&#8217;&#8216;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i>gfdl</i>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre><code>     A GNU Manual
</code></pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre><code>     You have freedom to copy and modify this GNU Manual, like GNU
     software. Copies published by the Free Software Foundation raise
     funds for GNU development.
</code></pre>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Option Summary</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Options Controlling the Kind of Output</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Compiling C<font SIZE="-2">++</font> Programs</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">Options Controlling C Dialect</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">Options Controlling C<font SIZE="-2">++</font> Dialect</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">Options Controlling Objective-C Dialect</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Options to Control Diagnostic Messages Formatting</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">Options to Request or Suppress Warnings</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">Options for Debugging Your Program or <font SIZE="-1">GCC</font></a></dt>
<dd>  </dd>
<dt><a href="#lbAO">Options That Control Optimization</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">Options Controlling the Preprocessor</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">Passing Options to the Assembler</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">Options for Linking</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">Options for Directory Search</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">Specifying Target Machine and Compiler Version</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">Hardware Models and Configurations</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">Options for Code Generation Conventions</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">ENVIRONMENT</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">FOOTNOTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">AUTHOR</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">COPYRIGHT</a></dt>
<dd>  </dd></dl>
