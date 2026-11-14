---
title: "i686-w64-mingw32-as(1)"
name: "i686-w64-mingw32-as"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-w64-mingw32-as/"
description: "AS – the portable GNU assembler."
---

<h2 class="name">NAME</h2>
<p> AS &#8211; the portable GNU assembler. </p>
<h2>SYNOPSIS</h2>
<p> as [<code>-a</code>[<code>cdghlns</code>][=<i>file</i>]] [<code>&#8211;alternate</code>] [<code>-D</code>]<br />
&nbsp;<wbr>[<code>&#8211;compress-debug-sections</code>]&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;nocompress-debug-sections</code>]<br />
&nbsp;<wbr>[<code>&#8211;debug-prefix-map</code>&nbsp;<wbr><i>old</i>=<i>new</i>]<br />
&nbsp;<wbr>[<code>&#8211;defsym</code>&nbsp;<wbr><i>sym</i>=<i>val</i>]&nbsp;<wbr>[<code>-f</code>]&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>&#8211;gstabs</code>]<br />
&nbsp;<wbr>[<code>&#8211;gstabs+</code>]&nbsp;<wbr>[<code>&#8211;gdwarf-2</code>]&nbsp;<wbr>[<code>&#8211;gdwarf-sections</code>]<br />
&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>[<code>-I</code>&nbsp;<wbr><i>dir</i>]&nbsp;<wbr>[<code>-J</code>]<br />
&nbsp;<wbr>[<code>-K</code>]&nbsp;<wbr>[<code>-L</code>]&nbsp;<wbr>[<code>&#8211;listing-lhs-width</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]<br />
&nbsp;<wbr>[<code>&#8211;listing-lhs-width2</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]&nbsp;<wbr>[<code>&#8211;listing-rhs-width</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]<br />
&nbsp;<wbr>[<code>&#8211;listing-cont-lines</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]&nbsp;<wbr>[<code>&#8211;keep-locals</code>]&nbsp;<wbr>[<code>-o</code><br />
&nbsp;<wbr><i>objfile</i>]&nbsp;<wbr>[<code>-R</code>]&nbsp;<wbr>[<code>&#8211;reduce-memory-overheads</code>]&nbsp;<wbr>[<code>&#8211;statistics</code>]<br />
&nbsp;<wbr>[<code>-v</code>]&nbsp;<wbr>[<code>-version</code>]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>-W</code>]&nbsp;<wbr>[<code>&#8211;warn</code>]<br />
&nbsp;<wbr>[<code>&#8211;fatal-warnings</code>]&nbsp;<wbr>[<code>-w</code>]&nbsp;<wbr>[<code>-x</code>]&nbsp;<wbr>[<code>-Z</code>]&nbsp;<wbr>[<code>@</code><i></i><font SIZE="-1"><i>FILE</i></font><i></i>]<br />
&nbsp;<wbr>[<code>&#8211;size-check=[error|warning]</code>]<br />
&nbsp;<wbr>[<code>&#8211;target-help</code>]&nbsp;<wbr>[<i>target-options</i>]<br />
&nbsp;<wbr>[<code>&#8212;</code>|<i>files</i>&nbsp;<wbr>&#8230;] </p>
<p> <i>Target AArch64 options:</i><br />
[<code>-EB</code>|<code>-EL</code>]<br />
[<code>-mabi</code>=<i></i><font SIZE="-1"><i>ABI</i></font><i></i>] </p>
<p> <i>Target Alpha options:</i><br />
[<code>-m</code><i>cpu</i>]<br />
[<code>-mdebug</code>&nbsp;<wbr>|&nbsp;<wbr><code>-no-mdebug</code>]<br />
[<code>-replace</code>&nbsp;<wbr>|&nbsp;<wbr><code>-noreplace</code>]<br />
[<code>-relax</code>]&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-G</code><i>size</i>]<br />
[<code>-F</code>]&nbsp;<wbr>[<code>-32addr</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>ARC</i></font><i> options:</i><br />
[<code>-marc[5|6|7|8]</code>]<br />
[<code>-EB</code>|<code>-EL</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>ARM</i></font><i> options:</i><br />
[<code>-mcpu</code>=<i>processor</i>[+<i>extension</i>&#8230;]]<br />
[<code>-march</code>=<i>architecture</i>[+<i>extension</i>&#8230;]]<br />
[<code>-mfpu</code>=<i>floating-point-format</i>]<br />
[<code>-mfloat-abi</code>=<i>abi</i>]<br />
[<code>-meabi</code>=<i>ver</i>]<br />
[<code>-mthumb</code>]<br />
[<code>-EB</code>|<code>-EL</code>]<br />
[<code>-mapcs-32</code>|<code>-mapcs-26</code>|<code>-mapcs-float</code>|<br />
&nbsp;<wbr><code>-mapcs-reentrant</code>]<br />
[<code>-mthumb-interwork</code>]&nbsp;<wbr>[<code>-k</code>] </p>
<p> <i>Target Blackfin options:</i><br />
[<code>-mcpu</code>=<i>processor</i>[-<i>sirevision</i>]]<br />
[<code>-mfdpic</code>]<br />
[<code>-mno-fdpic</code>]<br />
[<code>-mnopic</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>CRIS</i></font><i> options:</i><br />
[<code>&#8211;underscore</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;no-underscore</code>]<br />
[<code>&#8211;pic</code>]&nbsp;<wbr>[<code>-N</code>]<br />
[<code>&#8211;emulation=criself</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;emulation=crisaout</code>]<br />
[<code>&#8211;march=v0_v10</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;march=v10</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;march=v32</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;march=common_v10_v32</code>] </p>
<p> <i>Target D10V options:</i><br />
[<code>-O</code>] </p>
<p> <i>Target D30V options:</i><br />
[<code>-O</code>|<code>-n</code>|<code>-N</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>EPIPHANY</i></font><i> options:</i><br />
[<code>-mepiphany</code>|<code>-mepiphany16</code>] </p>
<p> <i>Target H8/300 options:</i><br />
[-h-tick-hex] </p>
<p> <i>Target i386 options:</i><br />
[<code>&#8211;32</code>|<code>&#8211;x32</code>|<code>&#8211;64</code>]&nbsp;<wbr>[<code>-n</code>]<br />
[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>[+<i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i>&#8230;]]&nbsp;<wbr>[<code>-mtune</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>] </p>
<p> <i>Target i960 options:</i><br />
[<code>-ACA</code>|<code>-ACA_A</code>|<code>-ACB</code>|<code>-ACC</code>|<code>-AKA</code>|<code>-AKB</code>|<br />
&nbsp;<wbr><code>-AKC</code>|<code>-AMC</code>]<br />
[<code>-b</code>]&nbsp;<wbr>[<code>-no-relax</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>IA-64</i></font><i> options:</i><br />
[<code>-mconstant-gp</code>|<code>-mauto-pic</code>]<br />
[<code>-milp32</code>|<code>-milp64</code>|<code>-mlp64</code>|<code>-mp64</code>]<br />
[<code>-mle</code>|<code>mbe</code>]<br />
[<code>-mtune=itanium1</code>|<code>-mtune=itanium2</code>]<br />
[<code>-munwind-check=warning</code>|<code>-munwind-check=error</code>]<br />
[<code>-mhint.b=ok</code>|<code>-mhint.b=warning</code>|<code>-mhint.b=error</code>]<br />
[<code>-x</code>|<code>-xexplicit</code>]&nbsp;<wbr>[<code>-xauto</code>]&nbsp;<wbr>[<code>-xdebug</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>IP2K</i></font><i> options:</i><br />
[<code>-mip2022</code>|<code>-mip2022ext</code>] </p>
<p> <i>Target M32C options:</i><br />
[<code>-m32c</code>|<code>-m16c</code>]&nbsp;<wbr>[-relax]&nbsp;<wbr>[-h-tick-hex] </p>
<p> <i>Target M32R options:</i><br />
[<code>&#8211;m32rx</code>|<code>&#8211;[no-]warn-explicit-parallel-conflicts</code>|<br />
<code>&#8211;W[n]p</code>] </p>
<p> <i>Target M680X0 options:</i><br />
[<code>-l</code>]&nbsp;<wbr>[<code>-m68000</code>|<code>-m68010</code>|<code>-m68020</code>|&#8230;] </p>
<p> <i>Target M68HC11 options:</i><br />
[<code>-m68hc11</code>|<code>-m68hc12</code>|<code>-m68hcs12</code>|<code>-mm9s12x</code>|<code>-mm9s12xg</code>]<br />
[<code>-mshort</code>|<code>-mlong</code>]<br />
[<code>-mshort-double</code>|<code>-mlong-double</code>]<br />
[<code>&#8211;force-long-branches</code>]&nbsp;<wbr>[<code>&#8211;short-branches</code>]<br />
[<code>&#8211;strict-direct-mode</code>]&nbsp;<wbr>[<code>&#8211;print-insn-syntax</code>]<br />
[<code>&#8211;print-opcodes</code>]&nbsp;<wbr>[<code>&#8211;generate-example</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MCORE</i></font><i> options:</i><br />
[<code>-jsri2bsr</code>]&nbsp;<wbr>[<code>-sifilter</code>]&nbsp;<wbr>[<code>-relax</code>]<br />
[<code>-mcpu=[210|340]</code>] </p>
<p> <i>Target Meta options:</i><br />
[<code>-mcpu=</code><i>cpu</i>]&nbsp;<wbr>[<code>-mfpu=</code><i>cpu</i>]&nbsp;<wbr>[<code>-mdsp=</code><i>cpu</i>] <i>Target </i><font SIZE="-1"><i>MICROBLAZE</i></font><i> options:</i> </p>
<p> <i>Target </i><font SIZE="-1"><i>MIPS</i></font><i> options:</i><br />
[<code>-nocpp</code>]&nbsp;<wbr>[<code>-EL</code>]&nbsp;<wbr>[<code>-EB</code>]&nbsp;<wbr>[<code>-O</code>[<i>optimization level</i>]]<br />
[<code>-g</code>[<i>debug level</i>]]&nbsp;<wbr>[<code>-G</code>&nbsp;<wbr><i>num</i>]&nbsp;<wbr>[<code>-KPIC</code>]&nbsp;<wbr>[<code>-call_shared</code>]<br />
[<code>-non_shared</code>]&nbsp;<wbr>[<code>-xgot</code>&nbsp;<wbr>[<code>-mvxworks-pic</code>]<br />
[<code>-mabi</code>=<i></i><font SIZE="-1"><i>ABI</i></font><i></i>]&nbsp;<wbr>[<code>-32</code>]&nbsp;<wbr>[<code>-n32</code>]&nbsp;<wbr>[<code>-64</code>]&nbsp;<wbr>[<code>-mfp32</code>]&nbsp;<wbr>[<code>-mgp32</code>]<br />
[<code>-mfp64</code>]&nbsp;<wbr>[<code>-mgp64</code>]&nbsp;<wbr>[<code>-mfpxx</code>]<br />
[<code>-modd-spreg</code>]&nbsp;<wbr>[<code>-mno-odd-spreg</code>]<br />
[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;<wbr>[<code>-mtune</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;<wbr>[<code>-mips1</code>]&nbsp;<wbr>[<code>-mips2</code>]<br />
[<code>-mips3</code>]&nbsp;<wbr>[<code>-mips4</code>]&nbsp;<wbr>[<code>-mips5</code>]&nbsp;<wbr>[<code>-mips32</code>]&nbsp;<wbr>[<code>-mips32r2</code>]<br />
[<code>-mips32r3</code>]&nbsp;<wbr>[<code>-mips32r5</code>]&nbsp;<wbr>[<code>-mips32r6</code>]&nbsp;<wbr>[<code>-mips64</code>]&nbsp;<wbr>[<code>-mips64r2</code>]<br />
[<code>-mips64r3</code>]&nbsp;<wbr>[<code>-mips64r5</code>]&nbsp;<wbr>[<code>-mips64r6</code>]<br />
[<code>-construct-floats</code>]&nbsp;<wbr>[<code>-no-construct-floats</code>]<br />
[<code>-mnan=</code><i>encoding</i>]<br />
[<code>-trap</code>]&nbsp;<wbr>[<code>-no-break</code>]&nbsp;<wbr>[<code>-break</code>]&nbsp;<wbr>[<code>-no-trap</code>]<br />
[<code>-mips16</code>]&nbsp;<wbr>[<code>-no-mips16</code>]<br />
[<code>-mmicromips</code>]&nbsp;<wbr>[<code>-mno-micromips</code>]<br />
[<code>-msmartmips</code>]&nbsp;<wbr>[<code>-mno-smartmips</code>]<br />
[<code>-mips3d</code>]&nbsp;<wbr>[<code>-no-mips3d</code>]<br />
[<code>-mdmx</code>]&nbsp;<wbr>[<code>-no-mdmx</code>]<br />
[<code>-mdsp</code>]&nbsp;<wbr>[<code>-mno-dsp</code>]<br />
[<code>-mdspr2</code>]&nbsp;<wbr>[<code>-mno-dspr2</code>]<br />
[<code>-mmsa</code>]&nbsp;<wbr>[<code>-mno-msa</code>]<br />
[<code>-mxpa</code>]&nbsp;<wbr>[<code>-mno-xpa</code>]<br />
[<code>-mmt</code>]&nbsp;<wbr>[<code>-mno-mt</code>]<br />
[<code>-mmcu</code>]&nbsp;<wbr>[<code>-mno-mcu</code>]<br />
[<code>-minsn32</code>]&nbsp;<wbr>[<code>-mno-insn32</code>]<br />
[<code>-mfix7000</code>]&nbsp;<wbr>[<code>-mno-fix7000</code>]<br />
[<code>-mfix-rm7000</code>]&nbsp;<wbr>[<code>-mno-fix-rm7000</code>]<br />
[<code>-mfix-vr4120</code>]&nbsp;<wbr>[<code>-mno-fix-vr4120</code>]<br />
[<code>-mfix-vr4130</code>]&nbsp;<wbr>[<code>-mno-fix-vr4130</code>]<br />
[<code>-mdebug</code>]&nbsp;<wbr>[<code>-no-mdebug</code>]<br />
[<code>-mpdr</code>]&nbsp;<wbr>[<code>-mno-pdr</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MMIX</i></font><i> options:</i><br />
[<code>&#8211;fixed-special-register-names</code>]&nbsp;<wbr>[<code>&#8211;globalize-symbols</code>]<br />
[<code>&#8211;gnu-syntax</code>]&nbsp;<wbr>[<code>&#8211;relax</code>]&nbsp;<wbr>[<code>&#8211;no-predefined-symbols</code>]<br />
[<code>&#8211;no-expand</code>]&nbsp;<wbr>[<code>&#8211;no-merge-gregs</code>]&nbsp;<wbr>[<code>-x</code>]<br />
[<code>&#8211;linker-allocated-gregs</code>] </p>
<p> <i>Target Nios </i><font SIZE="-1"><i>II</i></font><i> options:</i><br />
[<code>-relax-all</code>]&nbsp;<wbr>[<code>-relax-section</code>]&nbsp;<wbr>[<code>-no-relax</code>]<br />
[<code>-EB</code>]&nbsp;<wbr>[<code>-EL</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>NDS32</i></font><i> options:</i><br />
&nbsp;<wbr>[<code>-EL</code>]&nbsp;<wbr>[<code>-EB</code>]&nbsp;<wbr>[<code>-O</code>]&nbsp;<wbr>[<code>-Os</code>]&nbsp;<wbr>[<code>-mcpu=</code><i>cpu</i>]<br />
&nbsp;<wbr>[<code>-misa=</code><i>isa</i>]&nbsp;<wbr>[<code>-mabi=</code><i>abi</i>]&nbsp;<wbr>[<code>-mall-ext</code>]<br />
&nbsp;<wbr>[<code>-m[no-]16-bit</code>]&nbsp;<wbr>&nbsp;<wbr>[<code>-m[no-]perf-ext</code>]&nbsp;<wbr>[<code>-m[no-]perf2-ext</code>]<br />
&nbsp;<wbr>[<code>-m[no-]string-ext</code>]&nbsp;<wbr>[<code>-m[no-]dsp-ext</code>]&nbsp;<wbr>[<code>-m[no-]mac</code>]&nbsp;<wbr>[<code>-m[no-]div</code>]<br />
&nbsp;<wbr>[<code>-m[no-]audio-isa-ext</code>]&nbsp;<wbr>[<code>-m[no-]fpu-sp-ext</code>]&nbsp;<wbr>[<code>-m[no-]fpu-dp-ext</code>]<br />
&nbsp;<wbr>[<code>-m[no-]fpu-fma</code>]&nbsp;<wbr>[<code>-mfpu-freg=</code><i></i><font SIZE="-1"><i>FREG</i></font><i></i>]&nbsp;<wbr>[<code>-mreduced-regs</code>]<br />
&nbsp;<wbr>[<code>-mfull-regs</code>]&nbsp;<wbr>[<code>-m[no-]dx-regs</code>]&nbsp;<wbr>[<code>-mpic</code>]&nbsp;<wbr>[<code>-mno-relax</code>]<br />
&nbsp;<wbr>[<code>-mb2bb</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>PDP11</i></font><i> options:</i><br />
[<code>-mpic</code>|<code>-mno-pic</code>]&nbsp;<wbr>[<code>-mall</code>]&nbsp;<wbr>[<code>-mno-extensions</code>]<br />
[<code>-m</code><i>extension</i>|<code>-mno-</code><i>extension</i>]<br />
[<code>-m</code><i>cpu</i>]&nbsp;<wbr>[<code>-m</code><i>machine</i>] </p>
<p> <i>Target picoJava options:</i><br />
[<code>-mb</code>|<code>-me</code>] </p>
<p> <i>Target PowerPC options:</i><br />
[<code>-a32</code>|<code>-a64</code>]<br />
[<code>-mpwrx</code>|<code>-mpwr2</code>|<code>-mpwr</code>|<code>-m601</code>|<code>-mppc</code>|<code>-mppc32</code>|<code>-m603</code>|<code>-m604</code>|<code>-m403</code>|<code>-m405</code>|<br />
&nbsp;<wbr><code>-m440</code>|<code>-m464</code>|<code>-m476</code>|<code>-m7400</code>|<code>-m7410</code>|<code>-m7450</code>|<code>-m7455</code>|<code>-m750cl</code>|<code>-mppc64</code>|<br />
&nbsp;<wbr><code>-m620</code>|<code>-me500</code>|<code>-e500x2</code>|<code>-me500mc</code>|<code>-me500mc64</code>|<code>-me5500</code>|<code>-me6500</code>|<code>-mppc64bridge</code>|<br />
&nbsp;<wbr><code>-mbooke</code>|<code>-mpower4</code>|<code>-mpwr4</code>|<code>-mpower5</code>|<code>-mpwr5</code>|<code>-mpwr5x</code>|<code>-mpower6</code>|<code>-mpwr6</code>|<br />
&nbsp;<wbr><code>-mpower7</code>|<code>-mpwr7</code>|<code>-mpower8</code>|<code>-mpwr8</code>|<code>-ma2</code>|<code>-mcell</code>|<code>-mspe</code>|<code>-mtitan</code>|<code>-me300</code>|<code>-mcom</code>]<br />
[<code>-many</code>]&nbsp;<wbr>[<code>-maltivec</code>|<code>-mvsx</code>|<code>-mhtm</code>|<code>-mvle</code>]<br />
[<code>-mregnames</code>|<code>-mno-regnames</code>]<br />
[<code>-mrelocatable</code>|<code>-mrelocatable-lib</code>|<code>-K&nbsp;<wbr></code><font SIZE="-1"><code>PIC</code></font>]&nbsp;<wbr>[<code>-memb</code>]<br />
[<code>-mlittle</code>|<code>-mlittle-endian</code>|<code>-le</code>|<code>-mbig</code>|<code>-mbig-endian</code>|<code>-be</code>]<br />
[<code>-msolaris</code>|<code>-mno-solaris</code>]<br />
[<code>-nops=</code><i>count</i>] </p>
<p> <i>Target </i><font SIZE="-1"><i>RL78</i></font><i> options:</i><br />
[<code>-mg10</code>]<br />
[<code>-m32bit-doubles</code>|<code>-m64bit-doubles</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>RX</i></font><i> options:</i><br />
[<code>-mlittle-endian</code>|<code>-mbig-endian</code>]<br />
[<code>-m32bit-doubles</code>|<code>-m64bit-doubles</code>]<br />
[<code>-muse-conventional-section-names</code>]<br />
[<code>-msmall-data-limit</code>]<br />
[<code>-mpid</code>]<br />
[<code>-mrelax</code>]<br />
[<code>-mint-register=</code><i>number</i>]<br />
[<code>-mgcc-abi</code>|<code>-mrx-abi</code>] </p>
<p> <i>Target s390 options:</i><br />
[<code>-m31</code>|<code>-m64</code>]&nbsp;<wbr>[<code>-mesa</code>|<code>-mzarch</code>]&nbsp;<wbr>[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]<br />
[<code>-mregnames</code>|<code>-mno-regnames</code>]<br />
[<code>-mwarn-areg-zero</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>SCORE</i></font><i> options:</i><br />
[<code>-EB</code>][<code>-EL</code>][<code>-FIXDD</code>][<code>-NWARN</code>]<br />
[<code>-SCORE5</code>][<code>-SCORE5U</code>][<code>-SCORE7</code>][<code>-SCORE3</code>]<br />
[<code>-march=score7</code>][<code>-march=score3</code>]<br />
[<code>-USE_R1</code>][<code>-KPIC</code>][<code>-O0</code>][<code>-G</code>&nbsp;<wbr><i>num</i>][<code>-V</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>SPARC</i></font><i> options:</i><br />
[<code>-Av6</code>|<code>-Av7</code>|<code>-Av8</code>|<code>-Asparclet</code>|<code>-Asparclite</code><br />
&nbsp;<wbr><code>-Av8plus</code>|<code>-Av8plusa</code>|<code>-Av9</code>|<code>-Av9a</code>]<br />
[<code>-xarch=v8plus</code>|<code>-xarch=v8plusa</code>]&nbsp;<wbr>[<code>-bump</code>]<br />
[<code>-32</code>|<code>-64</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>TIC54X</i></font><i> options:</i><br />
&nbsp;<wbr>[<code>-mcpu=54[123589]</code>|<code>-mcpu=54[56]lp</code>]&nbsp;<wbr>[<code>-mfar-mode</code>|<code>-mf</code>]<br />
&nbsp;<wbr>[<code>-merrors-to-file</code>&nbsp;<wbr><i>&lt;filename&gt;</i>|<code>-me</code>&nbsp;<wbr><i>&lt;filename&gt;</i>] </p>
<p> <i>Target </i><font SIZE="-1"><i>TIC6X</i></font><i> options:</i><br />
[<code>-march=</code><i>arch</i>]&nbsp;<wbr>[<code>-mbig-endian</code>|<code>-mlittle-endian</code>]<br />
[<code>-mdsbt</code>|<code>-mno-dsbt</code>]&nbsp;<wbr>[<code>-mpid=no</code>|<code>-mpid=near</code>|<code>-mpid=far</code>]<br />
[<code>-mpic</code>|<code>-mno-pic</code>] </p>
<p> <i>Target TILE-Gx options:</i><br />
[<code>-m32</code>|<code>-m64</code>][<code>-EB</code>][<code>-EL</code>] </p>
<p> <i>Target Xtensa options:</i><br />
&nbsp;<wbr>[<code>&#8211;[no-]text-section-literals</code>]&nbsp;<wbr>[<code>&#8211;[no-]absolute-literals</code>]<br />
&nbsp;<wbr>[<code>&#8211;[no-]target-align</code>]&nbsp;<wbr>[<code>&#8211;[no-]longcalls</code>]<br />
&nbsp;<wbr>[<code>&#8211;[no-]transform</code>]<br />
&nbsp;<wbr>[<code>&#8211;rename-section</code>&nbsp;<wbr><i>oldname</i>=<i>newname</i>]<br />
&nbsp;<wbr>[<code>&#8211;[no-]trampolines</code>] </p>
<p> <i>Target Z80 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-z80</code>]&nbsp;<wbr>[<code>-r800</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-ignore-undocumented-instructions</code>]&nbsp;<wbr>[<code>-Wnud</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-ignore-unportable-instructions</code>]&nbsp;<wbr>[<code>-Wnup</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-warn-undocumented-instructions</code>]&nbsp;<wbr>[<code>-Wud</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-warn-unportable-instructions</code>]&nbsp;<wbr>[<code>-Wup</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-forbid-undocumented-instructions</code>]&nbsp;<wbr>[<code>-Fud</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-forbid-unportable-instructions</code>]&nbsp;<wbr>[<code>-Fup</code>]</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU </font><code>as</code> is really a family of assemblers. If you use (or have used) the <font SIZE="-1">GNU</font> assembler on one architecture, you should find a fairly similar environment when you use it on another architecture. Each version has much in common with the others, including object file formats, most assembler directives (often called <i>pseudo-ops</i>) and assembler syntax. </p>
<p> <code>as</code> is primarily intended to assemble the output of the <font SIZE="-1">GNU C</font> compiler <tt>&quot;gcc&quot;</tt> for use by the linker <tt>&quot;ld&quot;</tt>. Nevertheless, we&#8217;ve tried to make <code>as</code> assemble correctly everything that other assemblers for the same machine would assemble. Any exceptions are documented explicitly. This doesn&#8217;t mean <code>as</code> always uses the same syntax as another assembler for the same architecture; for example, we know of several incompatible versions of 680&#215;0 assembly language syntax. </p>
<p> Each time you run <code>as</code> it assembles exactly one source program. The source program is made up of one or more files. (The standard input is also a file.) </p>
<p> You give <code>as</code> a command line that has zero or more input file names. The input files are read (from left file name to right). A command line argument (in any position) that has no special meaning is taken to be an input file name. </p>
<p> If you give <code>as</code> no file names it attempts to read one input file from the <code>as</code> standard input, which is normally your terminal. You may have to type <code>ctl-D</code> to tell <code>as</code> there is no more program to assemble. </p>
<p> Use <code>&#8212;</code> if you need to explicitly name the standard input file in your command line. </p>
<p> If the source is empty, <code>as</code> produces a small, empty object file. </p>
<p> <code>as</code> may write warnings and error messages to the standard error file (usually your terminal). This should not happen when a compiler runs <code>as</code> automatically. Warnings report an assumption made so that <code>as</code> could keep assembling a flawed program; errors report a grave problem that stops the assembly. </p>
<p> If you are invoking <code>as</code> via the <font SIZE="-1">GNU C</font> compiler, you can use the <code>-Wa</code> option to pass arguments through to the assembler. The assembler arguments must be separated from each other (and the <code>-Wa</code>) by commas. For example: </p>
<pre>
        gcc -c -g -O -Wa,-alh,-L file.c
</pre>
<p> This passes two options to the assembler: <code>-alh</code> (emit a listing to standard output with high-level and assembly source) and <code>-L</code> (retain local symbols in the symbol table). </p>
<p> Usually you do not need to use this <code>-Wa</code> mechanism, since many compiler command-line options are automatically passed to the assembler by the compiler. (You can call the <font SIZE="-1">GNU</font> compiler driver with the <code>-v</code> option to see precisely what options it passes to each compilation pass, including the assembler.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</p>
<dt><code>-a[cdghlmns]</code></p>
<dd> Turn on listings, in any of a variety of ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-ac</code></p>
<dd> omit false conditionals</p>
<dt><code>-ad</code></p>
<dd> omit debugging directives</p>
<dt><code>-ag</code></p>
<dd> include general information, like as version and options passed</p>
<dt><code>-ah</code></p>
<dd> include high-level source</p>
<dt><code>-al</code></p>
<dd> include assembly</p>
<dt><code>-am</code></p>
<dd> include macro expansions</p>
<dt><code>-an</code></p>
<dd> omit forms processing</p>
<dt><code>-as</code></p>
<dd> include symbols</p>
<dt><code>=file</code></p>
<dd> set the name of the listing file</dl>
</dl>
<dl>
<dt>
<dd>
<p> You may combine these options; for example, use <code>-aln</code> for assembly listing without forms processing. The <code>=file</code> option, if used, must be the last one. By itself, <code>-a</code> defaults to <code>-ahls</code>.</dl>
<dt><code>&#8211;alternate</code></p>
<dd> Begin in alternate macro mode.</p>
<dt><code>&#8211;compress-debug-sections</code></p>
<dd> Compress <font SIZE="-1">DWARF</font> debug sections using zlib. The debug sections are renamed to begin with <code>.zdebug</code>, and the resulting object file may not be compatible with older linkers and object file utilities.</p>
<dt><code>&#8211;nocompress-debug-sections</code></p>
<dd> Do not compress <font SIZE="-1">DWARF</font> debug sections. This is the default.</p>
<dt><code>-D</code></p>
<dd> Ignored. This option is accepted for script compatibility with calls to other assemblers.</p>
<dt><code>&#8211;debug-prefix-map</code> <i>old</i><code>=</code><i>new</i></p>
<dd> When assembling files in directory <i>old</i>, record debugging information describing them as in <i>new</i> instead.</p>
<dt><code>&#8211;defsym</code> <i>sym</i><code>=</code><i>value</i></p>
<dd> Define the symbol <i>sym</i> to be <i>value</i> before assembling the input file. <i>value</i> must be an integer constant. As in C, a leading <code>0x</code> indicates a hexadecimal value, and a leading <code>0</code> indicates an octal value. The value of the symbol can be overridden inside a source file via the use of a <tt>&quot;.set&quot;</tt> pseudo-op.</p>
<dt><code>-f</code></p>
<dd> &#8220;fast&#8221;&#8212;skip whitespace and comment preprocessing (assume source is compiler output).</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;gen-debug</code></p>
<dd> Generate debugging information for each assembler source line using whichever debug format is preferred by the target. This currently means either <font SIZE="-1">STABS, ECOFF</font> or <font SIZE="-1">DWARF2.</font></p>
<dt><code>&#8211;gstabs</code></p>
<dd> Generate stabs debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.</p>
<dt><code>&#8211;gstabs+</code></p>
<dd> Generate stabs debugging information for each assembler line, with <font SIZE="-1">GNU</font> extensions that probably only gdb can handle, and that could make other debuggers crash or refuse to read your program. This may help debugging assembler code. Currently the only <font SIZE="-1">GNU</font> extension is the location of the current working directory at assembling time.</p>
<dt><code>&#8211;gdwarf-2</code></p>
<dd> Generate <font SIZE="-1">DWARF2</font> debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it. Note&#8212;this option is only supported by some targets, not all of them.</p>
<dt><code>&#8211;gdwarf-sections</code></p>
<dd> Instead of creating a .debug_line section, create a series of .debug_line.<i>foo</i> sections where <i>foo</i> is the name of the corresponding code section. For example a code section called <i>.text.func</i> will have its dwarf line number information placed into a section called <i>.debug_line.text.func</i>. If the code section is just called <i>.text</i> then debug line section will still be called just <i>.debug_line</i> without any suffix.</p>
<dt><code>&#8211;size-check=error</code></p>
<dd>
<dt><code>&#8211;size-check=warning</code></p>
<dd> Issue an error or warning for invalid <font SIZE="-1">ELF </font>.size directive.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the command line options and exit.</p>
<dt><code>&#8211;target-help</code></p>
<dd> Print a summary of all target specific options and exit.</p>
<dt><code>-I</code> <i>dir</i></p>
<dd> Add directory <i>dir</i> to the search list for <tt>&quot;.include&quot;</tt> directives.</p>
<dt><code>-J</code></p>
<dd> Don&#8217;t warn about signed overflow.</p>
<dt><code>-K</code></p>
<dd> Issue warnings when difference tables altered for long displacements.</p>
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;keep-locals</code></p>
<dd> Keep (in the symbol table) local symbols. These symbols start with system-specific local label prefixes, typically <code>.L</code> for <font SIZE="-1">ELF</font> systems or <code>L</code> for traditional a.out systems.</p>
<dt><code>&#8211;listing-lhs-width=</code><i>number</i></p>
<dd> Set the maximum width, in words, of the output data column for an assembler listing to <i>number</i>.</p>
<dt><code>&#8211;listing-lhs-width2=</code><i>number</i></p>
<dd> Set the maximum width, in words, of the output data column for continuation lines in an assembler listing to <i>number</i>.</p>
<dt><code>&#8211;listing-rhs-width=</code><i>number</i></p>
<dd> Set the maximum width of an input source line, as displayed in a listing, to <i>number</i> bytes.</p>
<dt><code>&#8211;listing-cont-lines=</code><i>number</i></p>
<dd> Set the maximum number of lines printed in a listing for a single line of input to <i>number</i> + 1.</p>
<dt><code>-o</code> <i>objfile</i></p>
<dd> Name the object-file output from <code>as</code> <i>objfile</i>.</p>
<dt><code>-R</code></p>
<dd> Fold the data section into the text section. </p>
<p> Set the default size of <font SIZE="-1">GAS</font>&#8216;s hash tables to a prime number close to <i>number</i>. Increasing this value can reduce the length of time it takes the assembler to perform its tasks, at the expense of increasing the assembler&#8217;s memory requirements. Similarly reducing this value can reduce the memory requirements at the expense of speed.</p>
<dt><code>&#8211;reduce-memory-overheads</code></p>
<dd> This option reduces <font SIZE="-1">GAS</font>&#8216;s memory requirements, at the expense of making the assembly processes slower. Currently this switch is a synonym for <code>&#8211;hash-size=4051</code>, but in the future it may have other effects as well.</p>
<dt><code>&#8211;statistics</code></p>
<dd> Print the maximum space (in bytes) and total time (in seconds) used by assembly.</p>
<dt><code>&#8211;strip-local-absolute</code></p>
<dd> Remove local absolute symbols from the outgoing symbol table.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>-version</code></p>
<dd> Print the <code>as</code> version.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the <code>as</code> version and exit.</p>
<dt><code>-W</code></p>
<dd>
<dt><code>&#8211;no-warn</code></p>
<dd> Suppress warning messages.</p>
<dt><code>&#8211;fatal-warnings</code></p>
<dd> Treat warnings as errors.</p>
<dt><code>&#8211;warn</code></p>
<dd> Don&#8217;t suppress warning messages or treat them as errors.</p>
<dt><code>-w</code></p>
<dd> Ignored.</p>
<dt><code>-x</code></p>
<dd> Ignored.</p>
<dt><code>-Z</code></p>
<dd> Generate an object file even after errors.</p>
<dt><code>&#8212; |</code> <i>files</i> <code>&#8230;</code></p>
<dd> Standard input, or source files to assemble.</dl>
<p> The following options are available when as is configured for the 64-bit mode of the <font SIZE="-1">ARM</font> Architecture (AArch64).</p>
<dl>
<dt><code>-EB</code></p>
<dd> This option specifies that the output generated by the assembler should be marked as being encoded for a big-endian processor.</p>
<dt><code>-EL</code></p>
<dd> This option specifies that the output generated by the assembler should be marked as being encoded for a little-endian processor.</p>
<dt><code>-mabi=</code><i>abi</i></p>
<dd> Specify which <font SIZE="-1">ABI</font> the source code uses. The recognized arguments are: <tt>&quot;ilp32&quot;</tt> and <tt>&quot;lp64&quot;</tt>, which decides the generated object file in <font SIZE="-1">ELF32</font> and <font SIZE="-1">ELF64</font> format respectively. The default is <tt>&quot;lp64&quot;</tt>.</p>
<dt><code>-mcpu=</code><i>processor</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> This option specifies the target processor. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target processor. The following processor names are recognized: <tt>&quot;cortex-a53&quot;</tt>, <tt>&quot;cortex-a57&quot;</tt>, <tt>&quot;xgene1&quot;</tt>, and <tt>&quot;xgene2&quot;</tt>. The special name <tt>&quot;all&quot;</tt> may be used to allow the assembler to accept instructions valid for any supported processor, including all optional extensions. </p>
<p> In addition to the basic instruction set, the assembler can be told to accept, or restrict, various extension mnemonics that extend the processor. </p>
<p> If some implementations of a particular processor can have an extension, then then those extensions are automatically enabled. Consequently, you will not normally have to specify any additional extensions.</p>
<dt><code>-march=</code><i>architecture</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> This option specifies the target architecture. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target architecture. The only value for <i>architecture</i> is <tt>&quot;armv8-a&quot;</tt>. </p>
<p> If both <code>-mcpu</code> and <code>-march</code> are specified, the assembler will use the setting for <code>-mcpu</code>. If neither are specified, the assembler will default to <code>-mcpu=all</code>. </p>
<p> The architecture option can be extended with the same instruction set extension options as the <code>-mcpu</code> option. Unlike <code>-mcpu</code>, extensions are not always enabled by default,</p>
<dt><code>-mverbose-error</code></p>
<dd> This option enables verbose error messages for AArch64 gas. This option is enabled by default.</p>
<dt><code>-mno-verbose-error</code></p>
<dd> This option disables verbose error messages in AArch64 gas.</dl>
<p> The following options are available when as is configured for an Alpha processor.</p>
<dl>
<dt><code>-m</code><i>cpu</i></p>
<dd> This option specifies the target processor. If an attempt is made to assemble an instruction which will not execute on the target processor, the assembler may either expand the instruction as a macro or issue an error message. This option is equivalent to the <tt>&quot;.arch&quot;</tt> directive. </p>
<p> The following processor names are recognized: <tt>21064</tt>, <tt>&quot;21064a&quot;</tt>, <tt>21066</tt>, <tt>21068</tt>, <tt>21164</tt>, <tt>&quot;21164a&quot;</tt>, <tt>&quot;21164pc&quot;</tt>, <tt>21264</tt>, <tt>&quot;21264a&quot;</tt>, <tt>&quot;21264b&quot;</tt>, <tt>&quot;ev4&quot;</tt>, <tt>&quot;ev5&quot;</tt>, <tt>&quot;lca45&quot;</tt>, <tt>&quot;ev5&quot;</tt>, <tt>&quot;ev56&quot;</tt>, <tt>&quot;pca56&quot;</tt>, <tt>&quot;ev6&quot;</tt>, <tt>&quot;ev67&quot;</tt>, <tt>&quot;ev68&quot;</tt>. The special name <tt>&quot;all&quot;</tt> may be used to allow the assembler to accept instructions valid for any Alpha processor. </p>
<p> In order to support existing practice in <font SIZE="-1">OSF/1</font> with respect to <tt>&quot;.arch&quot;</tt>, and existing practice within <font SIZE="-1"><code>MILO</code></font> (the Linux <font SIZE="-1">ARC</font> bootloader), the numbered processor names (e.g. 21064) enable the processor-specific PALcode instructions, while the &#8220;electro-vlasic&#8221; names (e.g. <tt>&quot;ev4&quot;</tt>) do not.</p>
<dt><code>-mdebug</code></p>
<dd>
<dt><code>-no-mdebug</code></p>
<dd> Enables or disables the generation of <tt>&quot;.mdebug&quot;</tt> encapsulation for stabs directives and procedure descriptors. The default is to automatically enable <tt>&quot;.mdebug&quot;</tt> when the first stabs directive is seen.</p>
<dt><code>-relax</code></p>
<dd> This option forces all relocations to be put into the object file, instead of saving space and resolving some relocations at assembly time. Note that this option does not propagate all symbol arithmetic into the object file, because not all symbol arithmetic can be represented. However, the option can still be useful in specific applications.</p>
<dt><code>-replace</code></p>
<dd>
<dt><code>-noreplace</code></p>
<dd> Enables or disables the optimization of procedure calls, both at assemblage and at link time. These options are only available for <font SIZE="-1">VMS</font> targets and <tt>&quot;-replace&quot;</tt> is the default. See section 1.4.1 of the OpenVMS Linker Utility Manual.</p>
<dt><code>-g</code></p>
<dd> This option is used when the compiler generates debug information. When <code>gcc</code> is using <code>mips-tfile</code> to generate debug information for <font SIZE="-1">ECOFF,</font> local labels must be passed through to the object file. Otherwise this option has no effect.</p>
<dt><code>-G</code><i>size</i></p>
<dd> A local common symbol larger than <i>size</i> is placed in <tt>&quot;.bss&quot;</tt>, while smaller symbols are placed in <tt>&quot;.sbss&quot;</tt>.</p>
<dt><code>-F</code></p>
<dd>
<dt><code>-32addr</code></p>
<dd> These options are ignored for backward compatibility.</dl>
<p> The following options are available when as is configured for an <font SIZE="-1">ARC</font> processor.</p>
<dl>
<dt><code>-marc[5|6|7|8]</code></p>
<dd> This option selects the core processor variant.</p>
<dt><code>-EB | -EL</code></p>
<dd> Select either big-endian (-EB) or little-endian (-EL) output.</dl>
<p> The following options are available when as is configured for the <font SIZE="-1">ARM</font> processor family.</p>
<dl>
<dt><code>-mcpu=</code><i>processor</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> Specify which <font SIZE="-1">ARM</font> processor variant is the target.</p>
<dt><code>-march=</code><i>architecture</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> Specify which <font SIZE="-1">ARM</font> architecture variant is used by the target.</p>
<dt><code>-mfpu=</code><i>floating-point-format</i></p>
<dd> Select which Floating Point architecture is the target.</p>
<dt><code>-mfloat-abi=</code><i>abi</i></p>
<dd> Select which floating point <font SIZE="-1">ABI</font> is in use.</p>
<dt><code>-mthumb</code></p>
<dd> Enable Thumb only instruction decoding.</p>
<dt><code>-mapcs-32 | -mapcs-26 | -mapcs-float | -mapcs-reentrant</code></p>
<dd> Select which procedure calling convention is in use.</p>
<dt><code>-EB | -EL</code></p>
<dd> Select either big-endian (-EB) or little-endian (-EL) output.</p>
<dt><code>-mthumb-interwork</code></p>
<dd> Specify that the code has been generated with interworking between Thumb and <font SIZE="-1">ARM</font> code in mind.</p>
<dt><code>-mccs</code></p>
<dd> Turns on CodeComposer Studio assembly syntax compatibility mode.</p>
<dt><code>-k</code></p>
<dd> Specify that <font SIZE="-1">PIC</font> code has been generated.</dl>
<p> The following options are available when as is configured for the Blackfin processor family.</p>
<dl>
<dt><code>-mcpu=</code><i>processor</i>[<code>&#8211;</code><i>sirevision</i>]</p>
<dd> This option specifies the target processor. The optional <i>sirevision</i> is not used in assembler. It&#8217;s here such that <font SIZE="-1">GCC</font> can easily pass down its <tt>&quot;-mcpu=&quot;</tt> option. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target processor. The following processor names are recognized: <tt>&quot;bf504&quot;</tt>, <tt>&quot;bf506&quot;</tt>, <tt>&quot;bf512&quot;</tt>, <tt>&quot;bf514&quot;</tt>, <tt>&quot;bf516&quot;</tt>, <tt>&quot;bf518&quot;</tt>, <tt>&quot;bf522&quot;</tt>, <tt>&quot;bf523&quot;</tt>, <tt>&quot;bf524&quot;</tt>, <tt>&quot;bf525&quot;</tt>, <tt>&quot;bf526&quot;</tt>, <tt>&quot;bf527&quot;</tt>, <tt>&quot;bf531&quot;</tt>, <tt>&quot;bf532&quot;</tt>, <tt>&quot;bf533&quot;</tt>, <tt>&quot;bf534&quot;</tt>, <tt>&quot;bf535&quot;</tt> (not implemented yet), <tt>&quot;bf536&quot;</tt>, <tt>&quot;bf537&quot;</tt>, <tt>&quot;bf538&quot;</tt>, <tt>&quot;bf539&quot;</tt>, <tt>&quot;bf542&quot;</tt>, <tt>&quot;bf542m&quot;</tt>, <tt>&quot;bf544&quot;</tt>, <tt>&quot;bf544m&quot;</tt>, <tt>&quot;bf547&quot;</tt>, <tt>&quot;bf547m&quot;</tt>, <tt>&quot;bf548&quot;</tt>, <tt>&quot;bf548m&quot;</tt>, <tt>&quot;bf549&quot;</tt>, <tt>&quot;bf549m&quot;</tt>, <tt>&quot;bf561&quot;</tt>, and <tt>&quot;bf592&quot;</tt>.</p>
<dt><code>-mfdpic</code></p>
<dd> Assemble for the <font SIZE="-1">FDPIC ABI.</font></p>
<dt><code>-mno-fdpic</code></p>
<dd>
<dt><code>-mnopic</code></p>
<dd> Disable -mfdpic.</dl>
<p> See the info pages for documentation of the CRIS-specific options. </p>
<p> The following options are available when as is configured for a D10V processor.</p>
<dl>
<dt><code>-O</code></p>
<dd> Optimize output by parallelizing instructions.</dl>
<p> The following options are available when as is configured for a D30V processor.</p>
<dl>
<dt><code>-O</code></p>
<dd> Optimize output by parallelizing instructions.</p>
<dt><code>-n</code></p>
<dd> Warn when nops are generated.</p>
<dt><code>-N</code></p>
<dd> Warn when a nop after a 32-bit multiply instruction is generated.</dl>
<p> The following options are available when as is configured for an Epiphany processor.</p>
<dl>
<dt><code>-mepiphany</code></p>
<dd> Specifies that the both 32 and 16 bit instructions are allowed. This is the default behavior.</p>
<dt><code>-mepiphany16</code></p>
<dd> Restricts the permitted instructions to just the 16 bit set.</dl>
<p> The following options are available when as is configured for an H8/300 processor. <tt>@chapter</tt> H8/300 Dependent Features</p>
<h3>Options</h3>
<p> The Renesas H8/300 version of <tt>&quot;as&quot;</tt> has one machine-dependent option:</p>
<dl>
<dt><code>-h-tick-hex</code></p>
<dd> Support H&#8217;00 style hex constants in addition to 0x00 style.</dl>
<p> The following options are available when as is configured for an i386 processor.</p>
<dl>
<dt><code>&#8211;32 | &#8211;x32 | &#8211;64</code></p>
<dd> Select the word size, either 32 bits or 64 bits. <code>&#8211;32</code> implies Intel i386 architecture, while <code>&#8211;x32</code> and <code>&#8211;64</code> imply <font SIZE="-1">AMD</font> x86-64 architecture with 32-bit or 64-bit word-size respectively. </p>
<p> These options are only available with the <font SIZE="-1">ELF</font> object file format, and require that the necessary <font SIZE="-1">BFD</font> support has been included (on a 32-bit platform you have to add &#8211;enable-64-bit-bfd to configure enable 64-bit usage and use x86-64 as target platform).</p>
<dt><code>-n</code></p>
<dd> By default, x86 <font SIZE="-1">GAS</font> replaces multiple nop instructions used for alignment within code sections with multi-byte nop instructions such as leal 0(%esi,1),%esi. This switch disables the optimization.</p>
<dt><code>&#8211;divide</code></p>
<dd> On SVR4-derived platforms, the character <code>/</code> is treated as a comment character, which means that it cannot be used in expressions. The <code>&#8211;divide</code> option turns <code>/</code> into a normal character. This does not disable <code>/</code> at the beginning of a line starting a comment, or affect using <code>#</code> for starting a comment.</p>
<dt><code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i><code>[+</code><i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i><code>&#8230;]</code></p>
<dd> This option specifies the target processor. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target processor. The following processor names are recognized: <tt>&quot;i8086&quot;</tt>, <tt>&quot;i186&quot;</tt>, <tt>&quot;i286&quot;</tt>, <tt>&quot;i386&quot;</tt>, <tt>&quot;i486&quot;</tt>, <tt>&quot;i586&quot;</tt>, <tt>&quot;i686&quot;</tt>, <tt>&quot;pentium&quot;</tt>, <tt>&quot;pentiumpro&quot;</tt>, <tt>&quot;pentiumii&quot;</tt>, <tt>&quot;pentiumiii&quot;</tt>, <tt>&quot;pentium4&quot;</tt>, <tt>&quot;prescott&quot;</tt>, <tt>&quot;nocona&quot;</tt>, <tt>&quot;core&quot;</tt>, <tt>&quot;core2&quot;</tt>, <tt>&quot;corei7&quot;</tt>, <tt>&quot;l1om&quot;</tt>, <tt>&quot;k1om&quot;</tt>, <tt>&quot;k6&quot;</tt>, <tt>&quot;k6_2&quot;</tt>, <tt>&quot;athlon&quot;</tt>, <tt>&quot;opteron&quot;</tt>, <tt>&quot;k8&quot;</tt>, <tt>&quot;amdfam10&quot;</tt>, <tt>&quot;bdver1&quot;</tt>, <tt>&quot;bdver2&quot;</tt>, <tt>&quot;bdver3&quot;</tt>, <tt>&quot;bdver4&quot;</tt>, <tt>&quot;btver1&quot;</tt>, <tt>&quot;btver2&quot;</tt>, <tt>&quot;generic32&quot;</tt> and <tt>&quot;generic64&quot;</tt>. </p>
<p> In addition to the basic instruction set, the assembler can be told to accept various extension mnemonics. For example, <tt>&quot;-march=i686+sse4+vmx&quot;</tt> extends <i>i686</i> with <i>sse4</i> and <i>vmx</i>. The following extensions are currently supported: <tt>8087</tt>, <tt>287</tt>, <tt>387</tt>, <tt>&quot;no87&quot;</tt>, <tt>&quot;mmx&quot;</tt>, <tt>&quot;nommx&quot;</tt>, <tt>&quot;sse&quot;</tt>, <tt>&quot;sse2&quot;</tt>, <tt>&quot;sse3&quot;</tt>, <tt>&quot;ssse3&quot;</tt>, <tt>&quot;sse4.1&quot;</tt>, <tt>&quot;sse4.2&quot;</tt>, <tt>&quot;sse4&quot;</tt>, <tt>&quot;nosse&quot;</tt>, <tt>&quot;avx&quot;</tt>, <tt>&quot;avx2&quot;</tt>, <tt>&quot;adx&quot;</tt>, <tt>&quot;rdseed&quot;</tt>, <tt>&quot;prfchw&quot;</tt>, <tt>&quot;smap&quot;</tt>, <tt>&quot;mpx&quot;</tt>, <tt>&quot;sha&quot;</tt>, <tt>&quot;prefetchwt1&quot;</tt>, <tt>&quot;clflushopt&quot;</tt>, <tt>&quot;se1&quot;</tt>, <tt>&quot;clwb&quot;</tt>, <tt>&quot;pcommit&quot;</tt>, <tt>&quot;avx512f&quot;</tt>, <tt>&quot;avx512cd&quot;</tt>, <tt>&quot;avx512er&quot;</tt>, <tt>&quot;avx512pf&quot;</tt>, <tt>&quot;avx512vl&quot;</tt>, <tt>&quot;avx512bw&quot;</tt>, <tt>&quot;avx512dq&quot;</tt>, <tt>&quot;avx512ifma&quot;</tt>, <tt>&quot;avx512vbmi&quot;</tt>, <tt>&quot;noavx&quot;</tt>, <tt>&quot;vmx&quot;</tt>, <tt>&quot;vmfunc&quot;</tt>, <tt>&quot;smx&quot;</tt>, <tt>&quot;xsave&quot;</tt>, <tt>&quot;xsaveopt&quot;</tt>, <tt>&quot;xsavec&quot;</tt>, <tt>&quot;xsaves&quot;</tt>, <tt>&quot;aes&quot;</tt>, <tt>&quot;pclmul&quot;</tt>, <tt>&quot;fsgsbase&quot;</tt>, <tt>&quot;rdrnd&quot;</tt>, <tt>&quot;f16c&quot;</tt>, <tt>&quot;bmi2&quot;</tt>, <tt>&quot;fma&quot;</tt>, <tt>&quot;movbe&quot;</tt>, <tt>&quot;ept&quot;</tt>, <tt>&quot;lzcnt&quot;</tt>, <tt>&quot;hle&quot;</tt>, <tt>&quot;rtm&quot;</tt>, <tt>&quot;invpcid&quot;</tt>, <tt>&quot;clflush&quot;</tt>, <tt>&quot;lwp&quot;</tt>, <tt>&quot;fma4&quot;</tt>, <tt>&quot;xop&quot;</tt>, <tt>&quot;cx16&quot;</tt>, <tt>&quot;syscall&quot;</tt>, <tt>&quot;rdtscp&quot;</tt>, <tt>&quot;3dnow&quot;</tt>, <tt>&quot;3dnowa&quot;</tt>, <tt>&quot;sse4a&quot;</tt>, <tt>&quot;sse5&quot;</tt>, <tt>&quot;svme&quot;</tt>, <tt>&quot;abm&quot;</tt> and <tt>&quot;padlock&quot;</tt>. Note that rather than extending a basic instruction set, the extension mnemonics starting with <tt>&quot;no&quot;</tt> revoke the respective functionality. </p>
<p> When the <tt>&quot;.arch&quot;</tt> directive is used with <code>-march</code>, the <tt>&quot;.arch&quot;</tt> directive will take precedent.</p>
<dt><code>-mtune=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i></p>
<dd> This option specifies a processor to optimize for. When used in conjunction with the <code>-march</code> option, only instructions of the processor specified by the <code>-march</code> option will be generated. </p>
<p> Valid <i></i><font SIZE="-1"><i>CPU</i></font><i></i> values are identical to the processor list of <code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i>.</p>
<dt><code>-msse2avx</code></p>
<dd> This option specifies that the assembler should encode <font SIZE="-1">SSE</font> instructions with <font SIZE="-1">VEX</font> prefix.</p>
<dt><code>-msse-check=</code><i>none</i></p>
<dd>
<dt><code>-msse-check=</code><i>warning</i></p>
<dd>
<dt><code>-msse-check=</code><i>error</i></p>
<dd> These options control if the assembler should check <font SIZE="-1">SSE</font> instructions. <code>-msse-check=</code><i>none</i> will make the assembler not to check <font SIZE="-1">SSE</font> instructions, which is the default. <code>-msse-check=</code><i>warning</i> will make the assembler issue a warning for any <font SIZE="-1">SSE</font> instruction. <code>-msse-check=</code><i>error</i> will make the assembler issue an error for any <font SIZE="-1">SSE</font> instruction.</p>
<dt><code>-mavxscalar=</code><i>128</i></p>
<dd>
<dt><code>-mavxscalar=</code><i>256</i></p>
<dd> These options control how the assembler should encode scalar <font SIZE="-1">AVX</font> instructions. <code>-mavxscalar=</code><i>128</i> will encode scalar <font SIZE="-1">AVX</font> instructions with 128bit vector length, which is the default. <code>-mavxscalar=</code><i>256</i> will encode scalar <font SIZE="-1">AVX</font> instructions with 256bit vector length.</p>
<dt><code>-mevexlig=</code><i>128</i></p>
<dd>
<dt><code>-mevexlig=</code><i>256</i></p>
<dd>
<dt><code>-mevexlig=</code><i>512</i></p>
<dd> These options control how the assembler should encode length-ignored (<font SIZE="-1">LIG</font>) <font SIZE="-1">EVEX</font> instructions. <code>-mevexlig=</code><i>128</i> will encode <font SIZE="-1">LIG EVEX</font> instructions with 128bit vector length, which is the default. <code>-mevexlig=</code><i>256</i> and <code>-mevexlig=</code><i>512</i> will encode <font SIZE="-1">LIG EVEX</font> instructions with 256bit and 512bit vector length, respectively.</p>
<dt><code>-mevexwig=</code><i>0</i></p>
<dd>
<dt><code>-mevexwig=</code><i>1</i></p>
<dd> These options control how the assembler should encode w-ignored (<font SIZE="-1">WIG</font>) <font SIZE="-1">EVEX</font> instructions. <code>-mevexwig=</code><i>0</i> will encode <font SIZE="-1">WIG EVEX</font> instructions with evex.w = 0, which is the default. <code>-mevexwig=</code><i>1</i> will encode <font SIZE="-1">WIG EVEX</font> instructions with evex.w = 1.</p>
<dt><code>-mmnemonic=</code><i>att</i></p>
<dd>
<dt><code>-mmnemonic=</code><i>intel</i></p>
<dd> This option specifies instruction mnemonic for matching instructions. The <tt>&quot;.att_mnemonic&quot;</tt> and <tt>&quot;.intel_mnemonic&quot;</tt> directives will take precedent.</p>
<dt><code>-msyntax=</code><i>att</i></p>
<dd>
<dt><code>-msyntax=</code><i>intel</i></p>
<dd> This option specifies instruction syntax when processing instructions. The <tt>&quot;.att_syntax&quot;</tt> and <tt>&quot;.intel_syntax&quot;</tt> directives will take precedent.</p>
<dt><code>-mnaked-reg</code></p>
<dd> This opetion specifies that registers don&#8217;t require a <code>%</code> prefix. The <tt>&quot;.att_syntax&quot;</tt> and <tt>&quot;.intel_syntax&quot;</tt> directives will take precedent.</p>
<dt><code>-madd-bnd-prefix</code></p>
<dd> This option forces the assembler to add <font SIZE="-1">BND</font> prefix to all branches, even if such prefix was not explicitly specified in the source code.</p>
<dt><code>-mbig-obj</code></p>
<dd> On x86-64 <font SIZE="-1">PE/COFF</font> target this option forces the use of big object file format, which allows more than 32768 sections.</p>
<dt><code>-momit-lock-prefix=</code><i>no</i></p>
<dd>
<dt><code>-momit-lock-prefix=</code><i>yes</i></p>
<dd> These options control how the assembler should encode lock prefix. This option is intended as a workaround for processors, that fail on lock prefix. This option can only be safely used with single-core, single-thread computers <code>-momit-lock-prefix=</code><i>yes</i> will omit all lock prefixes. <code>-momit-lock-prefix=</code><i>no</i> will encode lock prefix as usual, which is the default.</p>
<dt><code>-mevexrcig=</code><i>rne</i></p>
<dd>
<dt><code>-mevexrcig=</code><i>rd</i></p>
<dd>
<dt><code>-mevexrcig=</code><i>ru</i></p>
<dd>
<dt><code>-mevexrcig=</code><i>rz</i></p>
<dd> These options control how the assembler should encode SAE-only <font SIZE="-1">EVEX</font> instructions. <code>-mevexrcig=</code><i>rne</i> will encode <font SIZE="-1">RC</font> bits of <font SIZE="-1">EVEX</font> instruction with 00, which is the default. <code>-mevexrcig=</code><i>rd</i>, <code>-mevexrcig=</code><i>ru</i> and <code>-mevexrcig=</code><i>rz</i> will encode SAE-only <font SIZE="-1">EVEX</font> instructions with 01, 10 and 11 <font SIZE="-1">RC</font> bits, respectively.</dl>
<p> The following options are available when as is configured for the Intel 80960 processor.</p>
<dl>
<dt><code>-ACA | -ACA_A | -ACB | -ACC | -AKA | -AKB | -AKC | -AMC</code></p>
<dd> Specify which variant of the 960 architecture is the target.</p>
<dt><code>-b</code></p>
<dd> Add code to collect statistics about branches taken.</p>
<dt><code>-no-relax</code></p>
<dd> Do not alter compare-and-branch instructions for long displacements; error if necessary.</dl>
<p> The following options are available when as is configured for the Ubicom <font SIZE="-1">IP2K</font> series.</p>
<dl>
<dt><code>-mip2022ext</code></p>
<dd> Specifies that the extended <font SIZE="-1">IP2022</font> instructions are allowed.</p>
<dt><code>-mip2022</code></p>
<dd> Restores the default behaviour, which restricts the permitted instructions to just the basic <font SIZE="-1">IP2022</font> ones.</dl>
<p> The following options are available when as is configured for the Renesas M32C and M16C processors.</p>
<dl>
<dt><code>-m32c</code></p>
<dd> Assemble M32C instructions.</p>
<dt><code>-m16c</code></p>
<dd> Assemble M16C instructions (the default).</p>
<dt><code>-relax</code></p>
<dd> Enable support for link-time relaxations.</p>
<dt><code>-h-tick-hex</code></p>
<dd> Support H&#8217;00 style hex constants in addition to 0x00 style.</dl>
<p> The following options are available when as is configured for the Renesas M32R (formerly Mitsubishi M32R) series.</p>
<dl>
<dt><code>&#8211;m32rx</code></p>
<dd> Specify which processor in the M32R family is the target. The default is normally the M32R, but this option changes it to the M32RX.</p>
<dt><code>&#8211;warn-explicit-parallel-conflicts or &#8211;Wp</code></p>
<dd> Produce warning messages when questionable parallel constructs are encountered.</p>
<dt><code>&#8211;no-warn-explicit-parallel-conflicts or &#8211;Wnp</code></p>
<dd> Do not produce warning messages when questionable parallel constructs are encountered.</dl>
<p> The following options are available when as is configured for the Motorola 68000 series.</p>
<dl>
<dt><code>-l</code></p>
<dd> Shorten references to undefined symbols, to one word instead of two.</p>
<dt><code>-m68000 | -m68008 | -m68010 | -m68020 | -m68030</code></p>
<dd>
<dt><code>| -m68040 | -m68060 | -m68302 | -m68331 | -m68332</code></p>
<dd>
<dt><code>| -m68333 | -m68340 | -mcpu32 | -m5200</code></p>
<dd> Specify what processor in the 68000 family is the target. The default is normally the 68020, but this can be changed at configuration time.</p>
<dt><code>-m68881 | -m68882 | -mno-68881 | -mno-68882</code></p>
<dd> The target machine does (or does not) have a floating-point coprocessor. The default is to assume a coprocessor for 68020, 68030, and cpu32. Although the basic 68000 is not compatible with the 68881, a combination of the two can be specified, since it&#8217;s possible to do emulation of the coprocessor instructions with the main processor.</p>
<dt><code>-m68851 | -mno-68851</code></p>
<dd> The target machine does (or does not) have a memory-management unit coprocessor. The default is to assume an <font SIZE="-1">MMU</font> for 68020 and up.</dl>
<p> The following options are available when as is configured for an Altera Nios <font SIZE="-1">II</font> processor.</p>
<dl>
<dt><code>-relax-section</code></p>
<dd> Replace identified out-of-range branches with PC-relative <tt>&quot;jmp&quot;</tt> sequences when possible. The generated code sequences are suitable for use in position-independent code, but there is a practical limit on the extended branch range because of the length of the sequences. This option is the default.</p>
<dt><code>-relax-all</code></p>
<dd> Replace branch instructions not determinable to be in range and all call instructions with <tt>&quot;jmp&quot;</tt> and <tt>&quot;callr&quot;</tt> sequences (respectively). This option generates absolute relocations against the target symbols and is not appropriate for position-independent code.</p>
<dt><code>-no-relax</code></p>
<dd> Do not replace any branches or calls.</p>
<dt><code>-EB</code></p>
<dd> Generate big-endian output.</p>
<dt><code>-EL</code></p>
<dd> Generate little-endian output. This is the default.</dl>
<p> The following options are available when as is configured for a Meta processor.</p>
<dl>
<dt>&quot;-mcpu=metac11&quot;</p>
<dd> Generate code for Meta 1.1.</p>
<dt>&quot;-mcpu=metac12&quot;</p>
<dd> Generate code for Meta 1.2.</p>
<dt>&quot;-mcpu=metac21&quot;</p>
<dd> Generate code for Meta 2.1.</p>
<dt>&quot;-mfpu=metac21&quot;</p>
<dd> Allow code to use <font SIZE="-1">FPU</font> hardware of Meta 2.1.</dl>
<p> See the info pages for documentation of the MMIX-specific options. </p>
<p> The following options are available when as is configured for a <font SIZE="-1">NDS32</font> processor.</p>
<dl>
<dt>&quot;-O1&quot;</p>
<dd> Optimize for performance.</p>
<dt>&quot;-Os&quot;</p>
<dd> Optimize for space.</p>
<dt>&quot;-EL&quot;</p>
<dd> Produce little endian data output.</p>
<dt>&quot;-EB&quot;</p>
<dd> Produce little endian data output.</p>
<dt>&quot;-mpic&quot;</p>
<dd> Generate <font SIZE="-1">PIC.</font></p>
<dt>&quot;-mno-fp-as-gp-relax&quot;</p>
<dd> Suppress fp-as-gp relaxation for this file.</p>
<dt>&quot;-mb2bb-relax&quot;</p>
<dd> Back-to-back branch optimization.</p>
<dt>&quot;-mno-all-relax&quot;</p>
<dd> Suppress all relaxation for this file.</p>
<dt>&quot;-march=&lt;arch name&gt;&quot;</p>
<dd> Assemble for architecture &lt;arch name&gt; which could be v3, v3j, v3m, v3f, v3s, v2, v2j, v2f, v2s.</p>
<dt>&quot;-mbaseline=&lt;baseline&gt;&quot;</p>
<dd> Assemble for baseline &lt;baseline&gt; which could be v2, v3, v3m.</p>
<dt>&quot;-mfpu-freg=FREG<tt>&quot;</p>
<dd> Specify a </tt><font SIZE="-1"><tt>FPU</tt></font><tt> configuration.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;0 8 SP / 4 DP registers&quot;</p>
<dd>
<dt>&quot;1 16 SP / 8 DP registers&quot;</p>
<dd>
<dt>&quot;2 32 SP / 16 DP registers&quot;</p>
<dd>
<dt>&quot;3 32 SP / 32 DP registers&quot;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&quot;-mabi=</tt>abi<tt>&quot;</p>
<dd> Specify a abi version &lt;abi&gt; could be v1, v2, v2fp, v2fpp.</p>
<dt>&quot;-m[no-]mac&quot;</p>
<dd> Enable/Disable Multiply instructions support.</p>
<dt>&quot;-m[no-]div&quot;</p>
<dd> Enable/Disable Divide instructions support.</p>
<dt>&quot;-m[no-]16bit-ext&quot;</p>
<dd> Enable/Disable 16-bit extension</p>
<dt>&quot;-m[no-]dx-regs&quot;</p>
<dd> Enable/Disable d0/d1 registers</p>
<dt>&quot;-m[no-]perf-ext&quot;</p>
<dd> Enable/Disable Performance extension</p>
<dt>&quot;-m[no-]perf2-ext&quot;</p>
<dd> Enable/Disable Performance extension 2</p>
<dt>&quot;-m[no-]string-ext&quot;</p>
<dd> Enable/Disable String extension</p>
<dt>&quot;-m[no-]reduced-regs&quot;</p>
<dd> Enable/Disable Reduced Register configuration (</tt><font SIZE="-1"><tt>GPR16</tt></font><tt>) option</p>
<dt>&quot;-m[no-]audio-isa-ext&quot;</p>
<dd> Enable/Disable </tt><font SIZE="-1"><tt>AUDIO ISA</tt></font><tt> extension</p>
<dt>&quot;-m[no-]fpu-sp-ext&quot;</p>
<dd> Enable/Disable </tt><font SIZE="-1"><tt>FPU SP</tt></font><tt> extension</p>
<dt>&quot;-m[no-]fpu-dp-ext&quot;</p>
<dd> Enable/Disable </tt><font SIZE="-1"><tt>FPU DP</tt></font><tt> extension</p>
<dt>&quot;-m[no-]fpu-fma&quot;</p>
<dd> Enable/Disable </tt><font SIZE="-1"><tt>FPU</tt></font><tt> fused-multiply-add instructions</p>
<dt>&quot;-mall-ext&quot;</p>
<dd> Turn on all extensions and instructions support</dl>
<p> The following options are available when as is configured for a PowerPC processor.</p>
<dl>
<dt></tt><code>-a32</code></p>
<dd> Generate <font SIZE="-1">ELF32</font> or <font SIZE="-1">XCOFF32.</font></p>
<dt><code>-a64</code></p>
<dd> Generate <font SIZE="-1">ELF64</font> or <font SIZE="-1">XCOFF64.</font></p>
<dt><code>-K </code><font SIZE="-1"><code>PIC</code></font></p>
<dd> Set <font SIZE="-1">EF_PPC_RELOCATABLE_LIB</font> in <font SIZE="-1">ELF</font> flags.</p>
<dt><code>-mpwrx | -mpwr2</code></p>
<dd> Generate code for <font SIZE="-1">POWER/2 </font>(<font SIZE="-1">RIOS2</font>).</p>
<dt><code>-mpwr</code></p>
<dd> Generate code for <font SIZE="-1">POWER </font>(<font SIZE="-1">RIOS1</font>)</p>
<dt><code>-m601</code></p>
<dd> Generate code for PowerPC 601.</p>
<dt><code>-mppc, -mppc32, -m603, -m604</code></p>
<dd> Generate code for PowerPC 603/604.</p>
<dt><code>-m403, -m405</code></p>
<dd> Generate code for PowerPC 403/405.</p>
<dt><code>-m440</code></p>
<dd> Generate code for PowerPC 440. BookE and some 405 instructions.</p>
<dt><code>-m464</code></p>
<dd> Generate code for PowerPC 464.</p>
<dt><code>-m476</code></p>
<dd> Generate code for PowerPC 476.</p>
<dt><code>-m7400, -m7410, -m7450, -m7455</code></p>
<dd> Generate code for PowerPC 7400/7410/7450/7455.</p>
<dt><code>-m750cl</code></p>
<dd> Generate code for PowerPC 750CL.</p>
<dt><code>-mppc64, -m620</code></p>
<dd> Generate code for PowerPC 620/625/630.</p>
<dt><code>-me500, -me500x2</code></p>
<dd> Generate code for Motorola e500 core complex.</p>
<dt><code>-me500mc</code></p>
<dd> Generate code for Freescale e500mc core complex.</p>
<dt><code>-me500mc64</code></p>
<dd> Generate code for Freescale e500mc64 core complex.</p>
<dt><code>-me5500</code></p>
<dd> Generate code for Freescale e5500 core complex.</p>
<dt><code>-me6500</code></p>
<dd> Generate code for Freescale e6500 core complex.</p>
<dt><code>-mspe</code></p>
<dd> Generate code for Motorola <font SIZE="-1">SPE</font> instructions.</p>
<dt><code>-mtitan</code></p>
<dd> Generate code for AppliedMicro Titan core complex.</p>
<dt><code>-mppc64bridge</code></p>
<dd> Generate code for PowerPC 64, including bridge insns.</p>
<dt><code>-mbooke</code></p>
<dd> Generate code for 32-bit BookE.</p>
<dt><code>-ma2</code></p>
<dd> Generate code for A2 architecture.</p>
<dt><code>-me300</code></p>
<dd> Generate code for PowerPC e300 family.</p>
<dt><code>-maltivec</code></p>
<dd> Generate code for processors with AltiVec instructions.</p>
<dt><code>-mvle</code></p>
<dd> Generate code for Freescale PowerPC <font SIZE="-1">VLE</font> instructions.</p>
<dt><code>-mvsx</code></p>
<dd> Generate code for processors with Vector-Scalar (<font SIZE="-1">VSX</font>) instructions.</p>
<dt><code>-mhtm</code></p>
<dd> Generate code for processors with Hardware Transactional Memory instructions.</p>
<dt><code>-mpower4, -mpwr4</code></p>
<dd> Generate code for Power4 architecture.</p>
<dt><code>-mpower5, -mpwr5, -mpwr5x</code></p>
<dd> Generate code for Power5 architecture.</p>
<dt><code>-mpower6, -mpwr6</code></p>
<dd> Generate code for Power6 architecture.</p>
<dt><code>-mpower7, -mpwr7</code></p>
<dd> Generate code for Power7 architecture.</p>
<dt><code>-mpower8, -mpwr8</code></p>
<dd> Generate code for Power8 architecture.</p>
<dt><code>-mcell</code></p>
<dd>
<dt><code>-mcell</code></p>
<dd> Generate code for Cell Broadband Engine architecture.</p>
<dt><code>-mcom</code></p>
<dd> Generate code Power/PowerPC common instructions.</p>
<dt><code>-many</code></p>
<dd> Generate code for any architecture (<font SIZE="-1">PWR/PWRX/PPC</font>).</p>
<dt><code>-mregnames</code></p>
<dd> Allow symbolic names for registers.</p>
<dt><code>-mno-regnames</code></p>
<dd> Do not allow symbolic names for registers.</p>
<dt><code>-mrelocatable</code></p>
<dd> Support for <font SIZE="-1">GCC</font>&#8216;s -mrelocatable option.</p>
<dt><code>-mrelocatable-lib</code></p>
<dd> Support for <font SIZE="-1">GCC</font>&#8216;s -mrelocatable-lib option.</p>
<dt><code>-memb</code></p>
<dd> Set <font SIZE="-1">PPC_EMB</font> bit in <font SIZE="-1">ELF</font> flags.</p>
<dt><code>-mlittle, -mlittle-endian, -le</code></p>
<dd> Generate code for a little endian machine.</p>
<dt><code>-mbig, -mbig-endian, -be</code></p>
<dd> Generate code for a big endian machine.</p>
<dt><code>-msolaris</code></p>
<dd> Generate code for Solaris.</p>
<dt><code>-mno-solaris</code></p>
<dd> Do not generate code for Solaris.</p>
<dt><code>-nops=</code><i>count</i></p>
<dd> If an alignment directive inserts more than <i>count</i> nops, put a branch at the beginning to skip execution of the nops.</dl>
<p> See the info pages for documentation of the RX-specific options. </p>
<p> The following options are available when as is configured for the s390 processor family.</p>
<dl>
<dt><code>-m31</code></p>
<dd>
<dt><code>-m64</code></p>
<dd> Select the word size, either 31/32 bits or 64 bits.</p>
<dt><code>-mesa</code></p>
<dd>
<dt><code>-mzarch</code></p>
<dd> Select the architecture mode, either the Enterprise System Architecture (esa) or the z/Architecture mode (zarch).</p>
<dt><code>-march=</code><i>processor</i></p>
<dd> Specify which s390 processor variant is the target, <code>g6</code>, <code>g6</code>, <code>z900</code>, <code>z990</code>, <code>z9-109</code>, <code>z9-ec</code>, <code>z10</code>, <code>z196</code>, or <code>zEC12</code>.</p>
<dt><code>-mregnames</code></p>
<dd>
<dt><code>-mno-regnames</code></p>
<dd> Allow or disallow symbolic names for registers.</p>
<dt><code>-mwarn-areg-zero</code></p>
<dd> Warn whenever the operand for a base or index register has been specified but evaluates to zero.</dl>
<p> The following options are available when as is configured for a <font SIZE="-1">TMS320C6000</font> processor.</p>
<dl>
<dt><code>-march=</code><i>arch</i></p>
<dd> Enable (only) instructions from architecture <i>arch</i>. By default, all instructions are permitted. </p>
<p> The following values of <i>arch</i> are accepted: <tt>&quot;c62x&quot;</tt>, <tt>&quot;c64x&quot;</tt>, <tt>&quot;c64x+&quot;</tt>, <tt>&quot;c67x&quot;</tt>, <tt>&quot;c67x+&quot;</tt>, <tt>&quot;c674x&quot;</tt>.</p>
<dt><code>-mdsbt</code></p>
<dd>
<dt><code>-mno-dsbt</code></p>
<dd> The <code>-mdsbt</code> option causes the assembler to generate the <tt>&quot;Tag_ABI_DSBT&quot;</tt> attribute with a value of 1, indicating that the code is using <font SIZE="-1">DSBT</font> addressing. The <code>-mno-dsbt</code> option, the default, causes the tag to have a value of 0, indicating that the code does not use <font SIZE="-1">DSBT</font> addressing. The linker will emit a warning if objects of different type (<font SIZE="-1">DSBT</font> and non-DSBT) are linked together.</p>
<dt><code>-mpid=no</code></p>
<dd>
<dt><code>-mpid=near</code></p>
<dd>
<dt><code>-mpid=far</code></p>
<dd> The <code>-mpid=</code> option causes the assembler to generate the <tt>&quot;Tag_ABI_PID&quot;</tt> attribute with a value indicating the form of data addressing used by the code. <code>-mpid=no</code>, the default, indicates position-dependent data addressing, <code>-mpid=near</code> indicates position-independent addressing with <font SIZE="-1">GOT</font> accesses using near <font SIZE="-1">DP</font> addressing, and <code>-mpid=far</code> indicates position-independent addressing with <font SIZE="-1">GOT</font> accesses using far <font SIZE="-1">DP</font> addressing. The linker will emit a warning if objects built with different settings of this option are linked together.</p>
<dt><code>-mpic</code></p>
<dd>
<dt><code>-mno-pic</code></p>
<dd> The <code>-mpic</code> option causes the assembler to generate the <tt>&quot;Tag_ABI_PIC&quot;</tt> attribute with a value of 1, indicating that the code is using position-independent code addressing, The <tt>&quot;-mno-pic&quot;</tt> option, the default, causes the tag to have a value of 0, indicating position-dependent code addressing. The linker will emit a warning if objects of different type (position-dependent and position-independent) are linked together.</p>
<dt><code>-mbig-endian</code></p>
<dd>
<dt><code>-mlittle-endian</code></p>
<dd> Generate code for the specified endianness. The default is little-endian.</dl>
<p> The following options are available when as is configured for a TILE-Gx processor.</p>
<dl>
<dt><code>-m32 | -m64</code></p>
<dd> Select the word size, either 32 bits or 64 bits.</p>
<dt><code>-EB | -EL</code></p>
<dd> Select the endianness, either big-endian (-EB) or little-endian (-EL).</dl>
<p> The following options are available when as is configured for an Xtensa processor.</p>
<dl>
<dt><code>&#8211;text-section-literals | &#8211;no-text-section-literals</code></p>
<dd> Control the treatment of literal pools. The default is <code>&#8211;no-text-section-literals</code>, which places literals in separate sections in the output file. This allows the literal pool to be placed in a data <font SIZE="-1">RAM/ROM. </font> With <code>&#8211;text-section-literals</code>, the literals are interspersed in the text section in order to keep them as close as possible to their references. This may be necessary for large assembly files, where the literals would otherwise be out of range of the <tt>&quot;L32R&quot;</tt> instructions in the text section. These options only affect literals referenced via PC-relative <tt>&quot;L32R&quot;</tt> instructions; literals for absolute mode <tt>&quot;L32R&quot;</tt> instructions are handled separately.</p>
<dt><code>&#8211;absolute-literals | &#8211;no-absolute-literals</code></p>
<dd> Indicate to the assembler whether <tt>&quot;L32R&quot;</tt> instructions use absolute or PC-relative addressing. If the processor includes the absolute addressing option, the default is to use absolute <tt>&quot;L32R&quot;</tt> relocations. Otherwise, only the PC-relative <tt>&quot;L32R&quot;</tt> relocations can be used.</p>
<dt><code>&#8211;target-align | &#8211;no-target-align</code></p>
<dd> Enable or disable automatic alignment to reduce branch penalties at some expense in code size. This optimization is enabled by default. Note that the assembler will always align instructions like <tt>&quot;LOOP&quot;</tt> that have fixed alignment requirements.</p>
<dt><code>&#8211;longcalls | &#8211;no-longcalls</code></p>
<dd> Enable or disable transformation of call instructions to allow calls across a greater range of addresses. This option should be used when call targets can potentially be out of range. It may degrade both code size and performance, but the linker can generally optimize away the unnecessary overhead when a call ends up within range. The default is <code>&#8211;no-longcalls</code>.</p>
<dt><code>&#8211;transform | &#8211;no-transform</code></p>
<dd> Enable or disable all assembler transformations of Xtensa instructions, including both relaxation and optimization. The default is <code>&#8211;transform</code>; <code>&#8211;no-transform</code> should only be used in the rare cases when the instructions must be exactly as specified in the assembly source. Using <code>&#8211;no-transform</code> causes out of range instruction operands to be errors.</p>
<dt><code>&#8211;rename-section</code> <i>oldname</i><code>=</code><i>newname</i></p>
<dd> Rename the <i>oldname</i> section to <i>newname</i>. This option can be used multiple times to rename multiple sections.</p>
<dt><code>&#8211;trampolines | &#8211;no-trampolines</code></p>
<dd> Enable or disable transformation of jump instructions to allow jumps across a greater range of addresses. This option should be used when jump targets can potentially be out of range. In the absence of such jumps this option does not affect code size or performance. The default is <code>&#8211;trampolines</code>.</dl>
<p> The following options are available when as is configured for a Z80 family processor.</p>
<dl>
<dt><code>-z80</code></p>
<dd> Assemble for Z80 processor.</p>
<dt><code>-r800</code></p>
<dd> Assemble for R800 processor.</p>
<dt><code>-ignore-undocumented-instructions</code></p>
<dd>
<dt><code>-Wnud</code></p>
<dd> Assemble undocumented Z80 instructions that also work on R800 without warning.</p>
<dt><code>-ignore-unportable-instructions</code></p>
<dd>
<dt><code>-Wnup</code></p>
<dd> Assemble all undocumented Z80 instructions without warning.</p>
<dt><code>-warn-undocumented-instructions</code></p>
<dd>
<dt><code>-Wud</code></p>
<dd> Issue a warning for undocumented Z80 instructions that also work on R800.</p>
<dt><code>-warn-unportable-instructions</code></p>
<dd>
<dt><code>-Wup</code></p>
<dd> Issue a warning for undocumented Z80 instructions that do not work on R800.</p>
<dt><code>-forbid-undocumented-instructions</code></p>
<dd>
<dt><code>-Fud</code></p>
<dd> Treat all undocumented instructions as errors.</p>
<dt><code>-forbid-unportable-instructions</code></p>
<dd>
<dt><code>-Fup</code></p>
<dd> Treat undocumented Z80 instructions that do not work on R800 as errors.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), and the Info entries for <i>binutils</i> and <i>ld</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
