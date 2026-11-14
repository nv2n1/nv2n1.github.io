---
title: "x86_64-linux-gnu-as(1)"
name: "x86_64-linux-gnu-as"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-as/"
description: "AS – the portable GNU assembler."
---

<h2 class="name">NAME</h2>
<p> AS &#8211; the portable GNU assembler. </p>
<h2>SYNOPSIS</h2>
<p> as [<code>-a</code>[<code>cdghlns</code>][=<i>file</i>]] [<code>&#8211;alternate</code>] [<code>-D</code>]<br />
&nbsp;[<code>&#8211;compress-debug-sections</code>]&nbsp;<wbr>&nbsp;[<code>&#8211;nocompress-debug-sections</code>]<br />
&nbsp;[<code>&#8211;debug-prefix-map</code>&nbsp;<i>old</i>=<i>new</i>]<br />
&nbsp;[<code>&#8211;defsym</code>&nbsp;<i>sym</i>=<i>val</i>]&nbsp;[<code>-f</code>]&nbsp;[<code>-g</code>]&nbsp;[<code>&#8211;gstabs</code>]<br />
&nbsp;[<code>&#8211;gstabs+</code>]&nbsp;[<code>&#8211;gdwarf-&lt;N&gt;</code>]&nbsp;[<code>&#8211;gdwarf-sections</code>]<br />
&nbsp;[<code>&#8211;gdwarf-cie-version</code>=<i></i><font SIZE="-1"><i>VERSION</i></font><i></i>]<br />
&nbsp;[<code>&#8211;help</code>]&nbsp;[<code>-I</code>&nbsp;<i>dir</i>]&nbsp;[<code>-J</code>]<br />
&nbsp;[<code>-K</code>]&nbsp;[<code>-L</code>]&nbsp;[<code>&#8211;listing-lhs-width</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]<br />
&nbsp;[<code>&#8211;listing-lhs-width2</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]&nbsp;[<code>&#8211;listing-rhs-width</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]<br />
&nbsp;[<code>&#8211;listing-cont-lines</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]&nbsp;[<code>&#8211;keep-locals</code>]<br />
&nbsp;[<code>&#8211;no-pad-sections</code>]<br />
&nbsp;[<code>-o</code>&nbsp;<i>objfile</i>]&nbsp;[<code>-R</code>]<br />
&nbsp;[<code>&#8211;statistics</code>]<br />
&nbsp;[<code>-v</code>]&nbsp;[<code>-version</code>]&nbsp;[<code>&#8211;version</code>]<br />
&nbsp;[<code>-W</code>]&nbsp;[<code>&#8211;warn</code>]&nbsp;[<code>&#8211;fatal-warnings</code>]&nbsp;[<code>-w</code>]&nbsp;[<code>-x</code>]<br />
&nbsp;[<code>-Z</code>]&nbsp;[<code>@</code><i></i><font SIZE="-1"><i>FILE</i></font><i></i>]<br />
&nbsp;[<code>&#8211;sectname-subst</code>]&nbsp;[<code>&#8211;size-check=[error|warning]</code>]<br />
&nbsp;[<code>&#8211;elf-stt-common=[no|yes]</code>]<br />
&nbsp;[<code>&#8211;generate-missing-build-notes=[no|yes]</code>]<br />
&nbsp;[<code>&#8211;multibyte-handling=[allow|warn|warn-sym-only]</code>]<br />
&nbsp;[<code>&#8211;target-help</code>]&nbsp;[<i>target-options</i>]<br />
&nbsp;[<code>&#8212;</code>|<i>files</i>&nbsp;&#8230;]</p>
<h2>TARGET</h2>
<p> <i>Target AArch64 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EB</code>|<code>-EL</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mabi</code>=<i></i><font SIZE="-1"><i>ABI</i></font><i></i>] </p>
<p> <i>Target Alpha options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m</code><i>cpu</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdebug</code>&nbsp;|&nbsp;<code>-no-mdebug</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-replace</code>&nbsp;|&nbsp;<code>-noreplace</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-relax</code>]&nbsp;[<code>-g</code>]&nbsp;[<code>-G</code><i>size</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-F</code>]&nbsp;[<code>-32addr</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>ARC</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcpu=</code><i>cpu</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mA6</code>|<code>-mARC600</code>|<code>-mARC601</code>|<code>-mA7</code>|<code>-mARC700</code>|<code>-mEM</code>|<code>-mHS</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcode-density</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mrelax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EB</code>|<code>-EL</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>ARM</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcpu</code>=<i>processor</i>[+<i>extension</i>&#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march</code>=<i>architecture</i>[+<i>extension</i>&#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfpu</code>=<i>floating-point-format</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfloat-abi</code>=<i>abi</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-meabi</code>=<i>ver</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mthumb</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EB</code>|<code>-EL</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mapcs-32</code>|<code>-mapcs-26</code>|<code>-mapcs-float</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-mapcs-reentrant</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mthumb-interwork</code>]&nbsp;[<code>-k</code>] </p>
<p> <i>Target Blackfin options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcpu</code>=<i>processor</i>[-<i>sirevision</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfdpic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mno-fdpic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mnopic</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>BPF</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EL</code>]&nbsp;[<code>-EB</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>CRIS</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;underscore</code>&nbsp;|&nbsp;<code>&#8211;no-underscore</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;pic</code>]&nbsp;[<code>-N</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;emulation=criself</code>&nbsp;|&nbsp;<code>&#8211;emulation=crisaout</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;march=v0_v10</code>&nbsp;|&nbsp;<code>&#8211;march=v10</code>&nbsp;|&nbsp;<code>&#8211;march=v32</code>&nbsp;|&nbsp;<code>&#8211;march=common_v10_v32</code>] </p>
<p> <i>Target C-SKY options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march=</code><i>arch</i>]&nbsp;[<code>-mcpu=</code><i>cpu</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EL</code>]&nbsp;[<code>-mlittle-endian</code>]&nbsp;[<code>-EB</code>]&nbsp;[<code>-mbig-endian</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-fpic</code>]&nbsp;[<code>-pic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mljump</code>]&nbsp;[<code>-mno-ljump</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-force2bsr</code>]&nbsp;[<code>-mforce2bsr</code>]&nbsp;[<code>-no-force2bsr</code>]&nbsp;[<code>-mno-force2bsr</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-jsri2bsr</code>]&nbsp;[<code>-mjsri2bsr</code>]&nbsp;[<code>-no-jsri2bsr</code>&nbsp;]&nbsp;[<code>-mno-jsri2bsr</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mnolrw</code>&nbsp;]&nbsp;[<code>-mno-lrw</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-melrw</code>]&nbsp;[<code>-mno-elrw</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mlaf</code>&nbsp;]&nbsp;[<code>-mliterals-after-func</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mno-laf</code>]&nbsp;[<code>-mno-literals-after-func</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mlabr</code>]&nbsp;[<code>-mliterals-after-br</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mno-labr</code>]&nbsp;[<code>-mnoliterals-after-br</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mistack</code>]&nbsp;[<code>-mno-istack</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mhard-float</code>]&nbsp;[<code>-mmp</code>]&nbsp;[<code>-mcp</code>]&nbsp;[<code>-mcache</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-msecurity</code>]&nbsp;[<code>-mtrust</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdsp</code>]&nbsp;[<code>-medsp</code>]&nbsp;[<code>-mvdsp</code>] </p>
<p> <i>Target D10V options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-O</code>] </p>
<p> <i>Target D30V options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-O</code>|<code>-n</code>|<code>-N</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>EPIPHANY</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mepiphany</code>|<code>-mepiphany16</code>] </p>
<p> <i>Target H8/300 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[-h-tick-hex] </p>
<p> <i>Target i386 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;32</code>|<code>&#8211;x32</code>|<code>&#8211;64</code>]&nbsp;[<code>-n</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>[+<i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i>&#8230;]]&nbsp;[<code>-mtune</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>] </p>
<p> <i>Target </i><font SIZE="-1"><i>IA-64</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mconstant-gp</code>|<code>-mauto-pic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-milp32</code>|<code>-milp64</code>|<code>-mlp64</code>|<code>-mp64</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mle</code>|<code>mbe</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mtune=itanium1</code>|<code>-mtune=itanium2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-munwind-check=warning</code>|<code>-munwind-check=error</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mhint.b=ok</code>|<code>-mhint.b=warning</code>|<code>-mhint.b=error</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-x</code>|<code>-xexplicit</code>]&nbsp;[<code>-xauto</code>]&nbsp;[<code>-xdebug</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>IP2K</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mip2022</code>|<code>-mip2022ext</code>] </p>
<p> <i>Target M32C options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m32c</code>|<code>-m16c</code>]&nbsp;[-relax]&nbsp;[-h-tick-hex] </p>
<p> <i>Target M32R options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;m32rx</code>|<code>&#8211;[no-]warn-explicit-parallel-conflicts</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;W[n]p</code>] </p>
<p> <i>Target M680X0 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>]&nbsp;[<code>-m68000</code>|<code>-m68010</code>|<code>-m68020</code>|&#8230;] </p>
<p> <i>Target M68HC11 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m68hc11</code>|<code>-m68hc12</code>|<code>-m68hcs12</code>|<code>-mm9s12x</code>|<code>-mm9s12xg</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mshort</code>|<code>-mlong</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mshort-double</code>|<code>-mlong-double</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;force-long-branches</code>]&nbsp;[<code>&#8211;short-branches</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;strict-direct-mode</code>]&nbsp;[<code>&#8211;print-insn-syntax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;print-opcodes</code>]&nbsp;[<code>&#8211;generate-example</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MCORE</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-jsri2bsr</code>]&nbsp;[<code>-sifilter</code>]&nbsp;[<code>-relax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcpu=[210|340]</code>] </p>
<p> <i>Target Meta options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcpu=</code><i>cpu</i>]&nbsp;[<code>-mfpu=</code><i>cpu</i>]&nbsp;[<code>-mdsp=</code><i>cpu</i>] <i>Target </i><font SIZE="-1"><i>MICROBLAZE</i></font><i> options:</i> </p>
<p> <i>Target </i><font SIZE="-1"><i>MIPS</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-nocpp</code>]&nbsp;[<code>-EL</code>]&nbsp;[<code>-EB</code>]&nbsp;[<code>-O</code>[<i>optimization level</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>[<i>debug level</i>]]&nbsp;[<code>-G</code>&nbsp;<i>num</i>]&nbsp;[<code>-KPIC</code>]&nbsp;[<code>-call_shared</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-non_shared</code>]&nbsp;[<code>-xgot</code>&nbsp;[<code>-mvxworks-pic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mabi</code>=<i></i><font SIZE="-1"><i>ABI</i></font><i></i>]&nbsp;[<code>-32</code>]&nbsp;[<code>-n32</code>]&nbsp;[<code>-64</code>]&nbsp;[<code>-mfp32</code>]&nbsp;[<code>-mgp32</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfp64</code>]&nbsp;[<code>-mgp64</code>]&nbsp;[<code>-mfpxx</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-modd-spreg</code>]&nbsp;[<code>-mno-odd-spreg</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;[<code>-mtune</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;[<code>-mips1</code>]&nbsp;[<code>-mips2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mips3</code>]&nbsp;[<code>-mips4</code>]&nbsp;[<code>-mips5</code>]&nbsp;[<code>-mips32</code>]&nbsp;[<code>-mips32r2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mips32r3</code>]&nbsp;[<code>-mips32r5</code>]&nbsp;[<code>-mips32r6</code>]&nbsp;[<code>-mips64</code>]&nbsp;[<code>-mips64r2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mips64r3</code>]&nbsp;[<code>-mips64r5</code>]&nbsp;[<code>-mips64r6</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-construct-floats</code>]&nbsp;[<code>-no-construct-floats</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mignore-branch-isa</code>]&nbsp;[<code>-mno-ignore-branch-isa</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mnan=</code><i>encoding</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-trap</code>]&nbsp;[<code>-no-break</code>]&nbsp;[<code>-break</code>]&nbsp;[<code>-no-trap</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mips16</code>]&nbsp;[<code>-no-mips16</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mmips16e2</code>]&nbsp;[<code>-mno-mips16e2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mmicromips</code>]&nbsp;[<code>-mno-micromips</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-msmartmips</code>]&nbsp;[<code>-mno-smartmips</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mips3d</code>]&nbsp;[<code>-no-mips3d</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdmx</code>]&nbsp;[<code>-no-mdmx</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdsp</code>]&nbsp;[<code>-mno-dsp</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdspr2</code>]&nbsp;[<code>-mno-dspr2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdspr3</code>]&nbsp;[<code>-mno-dspr3</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mmsa</code>]&nbsp;[<code>-mno-msa</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mxpa</code>]&nbsp;[<code>-mno-xpa</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mmt</code>]&nbsp;[<code>-mno-mt</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mmcu</code>]&nbsp;[<code>-mno-mcu</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mcrc</code>]&nbsp;[<code>-mno-crc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mginv</code>]&nbsp;[<code>-mno-ginv</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mloongson-mmi</code>]&nbsp;[<code>-mno-loongson-mmi</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mloongson-cam</code>]&nbsp;[<code>-mno-loongson-cam</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mloongson-ext</code>]&nbsp;[<code>-mno-loongson-ext</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mloongson-ext2</code>]&nbsp;[<code>-mno-loongson-ext2</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-minsn32</code>]&nbsp;[<code>-mno-insn32</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfix7000</code>]&nbsp;[<code>-mno-fix7000</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfix-rm7000</code>]&nbsp;[<code>-mno-fix-rm7000</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfix-vr4120</code>]&nbsp;[<code>-mno-fix-vr4120</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfix-vr4130</code>]&nbsp;[<code>-mno-fix-vr4130</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfix-r5900</code>]&nbsp;[<code>-mno-fix-r5900</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdebug</code>]&nbsp;[<code>-no-mdebug</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mpdr</code>]&nbsp;[<code>-mno-pdr</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MMIX</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;fixed-special-register-names</code>]&nbsp;[<code>&#8211;globalize-symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;gnu-syntax</code>]&nbsp;[<code>&#8211;relax</code>]&nbsp;[<code>&#8211;no-predefined-symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;no-expand</code>]&nbsp;[<code>&#8211;no-merge-gregs</code>]&nbsp;[<code>-x</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;linker-allocated-gregs</code>] </p>
<p> <i>Target Nios </i><font SIZE="-1"><i>II</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-relax-all</code>]&nbsp;[<code>-relax-section</code>]&nbsp;[<code>-no-relax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EB</code>]&nbsp;[<code>-EL</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>NDS32</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EL</code>]&nbsp;[<code>-EB</code>]&nbsp;[<code>-O</code>]&nbsp;[<code>-Os</code>]&nbsp;[<code>-mcpu=</code><i>cpu</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-misa=</code><i>isa</i>]&nbsp;[<code>-mabi=</code><i>abi</i>]&nbsp;[<code>-mall-ext</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m[no-]16-bit</code>]&nbsp;<wbr>&nbsp;[<code>-m[no-]perf-ext</code>]&nbsp;[<code>-m[no-]perf2-ext</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m[no-]string-ext</code>]&nbsp;[<code>-m[no-]dsp-ext</code>]&nbsp;[<code>-m[no-]mac</code>]&nbsp;[<code>-m[no-]div</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m[no-]audio-isa-ext</code>]&nbsp;[<code>-m[no-]fpu-sp-ext</code>]&nbsp;[<code>-m[no-]fpu-dp-ext</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m[no-]fpu-fma</code>]&nbsp;[<code>-mfpu-freg=</code><i></i><font SIZE="-1"><i>FREG</i></font><i></i>]&nbsp;[<code>-mreduced-regs</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mfull-regs</code>]&nbsp;[<code>-m[no-]dx-regs</code>]&nbsp;[<code>-mpic</code>]&nbsp;[<code>-mno-relax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mb2bb</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>PDP11</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mpic</code>|<code>-mno-pic</code>]&nbsp;[<code>-mall</code>]&nbsp;[<code>-mno-extensions</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m</code><i>extension</i>|<code>-mno-</code><i>extension</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m</code><i>cpu</i>]&nbsp;[<code>-m</code><i>machine</i>] </p>
<p> <i>Target picoJava options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mb</code>|<code>-me</code>] </p>
<p> <i>Target PowerPC options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-a32</code>|<code>-a64</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mpwrx</code>|<code>-mpwr2</code>|<code>-mpwr</code>|<code>-m601</code>|<code>-mppc</code>|<code>-mppc32</code>|<code>-m603</code>|<code>-m604</code>|<code>-m403</code>|<code>-m405</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-m440</code>|<code>-m464</code>|<code>-m476</code>|<code>-m7400</code>|<code>-m7410</code>|<code>-m7450</code>|<code>-m7455</code>|<code>-m750cl</code>|<code>-mgekko</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-mbroadway</code>|<code>-mppc64</code>|<code>-m620</code>|<code>-me500</code>|<code>-e500x2</code>|<code>-me500mc</code>|<code>-me500mc64</code>|<code>-me5500</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-me6500</code>|<code>-mppc64bridge</code>|<code>-mbooke</code>|<code>-mpower4</code>|<code>-mpwr4</code>|<code>-mpower5</code>|<code>-mpwr5</code>|<code>-mpwr5x</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-mpower6</code>|<code>-mpwr6</code>|<code>-mpower7</code>|<code>-mpwr7</code>|<code>-mpower8</code>|<code>-mpwr8</code>|<code>-mpower9</code>|<code>-mpwr9</code><code>-ma2</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-mcell</code>|<code>-mspe</code>|<code>-mspe2</code>|<code>-mtitan</code>|<code>-me300</code>|<code>-mcom</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-many</code>]&nbsp;[<code>-maltivec</code>|<code>-mvsx</code>|<code>-mhtm</code>|<code>-mvle</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mregnames</code>|<code>-mno-regnames</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mrelocatable</code>|<code>-mrelocatable-lib</code>|<code>-K&nbsp;</code><font SIZE="-1"><code>PIC</code></font>]&nbsp;[<code>-memb</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mlittle</code>|<code>-mlittle-endian</code>|<code>-le</code>|<code>-mbig</code>|<code>-mbig-endian</code>|<code>-be</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-msolaris</code>|<code>-mno-solaris</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-nops=</code><i>count</i>] </p>
<p> <i>Target </i><font SIZE="-1"><i>PRU</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-link-relax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mnolink-relax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mno-warn-regname-label</code>] </p>
<p> <i>Target RISC-V options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-fpic</code>|<code>-fPIC</code>|<code>-fno-pic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march</code>=<i></i><font SIZE="-1"><i>ISA</i></font><i></i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mabi</code>=<i></i><font SIZE="-1"><i>ABI</i></font><i></i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mlittle-endian</code>|<code>-mbig-endian</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>RL78</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mg10</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m32bit-doubles</code>|<code>-m64bit-doubles</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>RX</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mlittle-endian</code>|<code>-mbig-endian</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m32bit-doubles</code>|<code>-m64bit-doubles</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-muse-conventional-section-names</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-msmall-data-limit</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mpid</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mrelax</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mint-register=</code><i>number</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mgcc-abi</code>|<code>-mrx-abi</code>] </p>
<p> <i>Target s390 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m31</code>|<code>-m64</code>]&nbsp;[<code>-mesa</code>|<code>-mzarch</code>]&nbsp;[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mregnames</code>|<code>-mno-regnames</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mwarn-areg-zero</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>SCORE</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EB</code>][<code>-EL</code>][<code>-FIXDD</code>][<code>-NWARN</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-SCORE5</code>][<code>-SCORE5U</code>][<code>-SCORE7</code>][<code>-SCORE3</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march=score7</code>][<code>-march=score3</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-USE_R1</code>][<code>-KPIC</code>][<code>-O0</code>][<code>-G</code>&nbsp;<i>num</i>][<code>-V</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>SPARC</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-Av6</code>|<code>-Av7</code>|<code>-Av8</code>|<code>-Aleon</code>|<code>-Asparclet</code>|<code>-Asparclite</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-Av8plus</code>|<code>-Av8plusa</code>|<code>-Av8plusb</code>|<code>-Av8plusc</code>|<code>-Av8plusd</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-Av8plusv</code>|<code>-Av8plusm</code>|<code>-Av9</code>|<code>-Av9a</code>|<code>-Av9b</code>|<code>-Av9c</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-Av9d</code>|<code>-Av9e</code>|<code>-Av9v</code>|<code>-Av9m</code>|<code>-Asparc</code>|<code>-Asparcvis</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-Asparcvis2</code>|<code>-Asparcfmaf</code>|<code>-Asparcima</code>|<code>-Asparcvis3</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-Asparcvisr</code>|<code>-Asparc5</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-xarch=v8plus</code>|<code>-xarch=v8plusa</code>]|<code>-xarch=v8plusb</code>|<code>-xarch=v8plusc</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-xarch=v8plusd</code>|<code>-xarch=v8plusv</code>|<code>-xarch=v8plusm</code>|<code>-xarch=v9</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-xarch=v9a</code>|<code>-xarch=v9b</code>|<code>-xarch=v9c</code>|<code>-xarch=v9d</code>|<code>-xarch=v9e</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-xarch=v9v</code>|<code>-xarch=v9m</code>|<code>-xarch=sparc</code>|<code>-xarch=sparcvis</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-xarch=sparcvis2</code>|<code>-xarch=sparcfmaf</code>|<code>-xarch=sparcima</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-xarch=sparcvis3</code>|<code>-xarch=sparcvisr</code>|<code>-xarch=sparc5</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-bump</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-32</code>|<code>-64</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;enforce-aligned-data</code>][<code>&#8211;dcti-couples-detect</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>TIC54X</i></font><i> options:</i><br />
&nbsp;[<code>-mcpu=54[123589]</code>|<code>-mcpu=54[56]lp</code>]&nbsp;[<code>-mfar-mode</code>|<code>-mf</code>]<br />
&nbsp;[<code>-merrors-to-file</code>&nbsp;<i>&lt;filename&gt;</i>|<code>-me</code>&nbsp;<i>&lt;filename&gt;</i>] </p>
<p> <i>Target </i><font SIZE="-1"><i>TIC6X</i></font><i> options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-march=</code><i>arch</i>]&nbsp;[<code>-mbig-endian</code>|<code>-mlittle-endian</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mdsbt</code>|<code>-mno-dsbt</code>]&nbsp;[<code>-mpid=no</code>|<code>-mpid=near</code>|<code>-mpid=far</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mpic</code>|<code>-mno-pic</code>] </p>
<p> <i>Target TILE-Gx options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m32</code>|<code>-m64</code>][<code>-EB</code>][<code>-EL</code>] </p>
<p> <i>Target Visium options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-mtune=</code><i>arch</i>] </p>
<p> <i>Target Xtensa options:</i><br />
&nbsp;[<code>&#8211;[no-]text-section-literals</code>]&nbsp;[<code>&#8211;[no-]auto-litpools</code>]<br />
&nbsp;[<code>&#8211;[no-]absolute-literals</code>]<br />
&nbsp;[<code>&#8211;[no-]target-align</code>]&nbsp;[<code>&#8211;[no-]longcalls</code>]<br />
&nbsp;[<code>&#8211;[no-]transform</code>]<br />
&nbsp;[<code>&#8211;rename-section</code>&nbsp;<i>oldname</i>=<i>newname</i>]<br />
&nbsp;[<code>&#8211;[no-]trampolines</code>]<br />
&nbsp;[<code>&#8211;abi-windowed</code>|<code>&#8211;abi-call0</code>] </p>
<p> <i>Target Z80 options:</i><br />
&nbsp;<wbr>&nbsp;[<code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i><i>[-EXT]</i><i>[+EXT]</i>]<br />
&nbsp;<wbr>&nbsp;[<code>-local-prefix=</code><i></i><font SIZE="-1"><i>PREFIX</i></font><i></i>]<br />
&nbsp;<wbr>&nbsp;[<code>-colonless</code>]<br />
&nbsp;<wbr>&nbsp;[<code>-sdcc</code>]<br />
&nbsp;<wbr>&nbsp;[<code>-fp-s=</code><i></i><font SIZE="-1"><i>FORMAT</i></font><i></i>]<br />
&nbsp;<wbr>&nbsp;[<code>-fp-d=</code><i></i><font SIZE="-1"><i>FORMAT</i></font><i></i>]</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU</font> <code>as</code> is really a family of assemblers. If you use (or have used) the <font SIZE="-1">GNU</font> assembler on one architecture, you should find a fairly similar environment when you use it on another architecture. Each version has much in common with the others, including object file formats, most assembler directives (often called <i>pseudo-ops</i>) and assembler syntax. </p>
<p> <code>as</code> is primarily intended to assemble the output of the <font SIZE="-1">GNU C</font> compiler <tt>&quot;gcc&quot;</tt> for use by the linker <tt>&quot;ld&quot;</tt>. Nevertheless, we&#8217;ve tried to make <code>as</code> assemble correctly everything that other assemblers for the same machine would assemble. Any exceptions are documented explicitly. This doesn&#8217;t mean <code>as</code> always uses the same syntax as another assembler for the same architecture; for example, we know of several incompatible versions of 680&#215;0 assembly language syntax. </p>
<p> Each time you run <code>as</code> it assembles exactly one source program. The source program is made up of one or more files. (The standard input is also a file.) </p>
<p> You give <code>as</code> a command line that has zero or more input file names. The input files are read (from left file name to right). A command-line argument (in any position) that has no special meaning is taken to be an input file name. </p>
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
<dd> Compress <font SIZE="-1">DWARF</font> debug sections using zlib with <font SIZE="-1">SHF_COMPRESSED</font> from the <font SIZE="-1">ELF ABI.</font> The resulting object file may not be compatible with older linkers and object file utilities. Note if compression would make a given section <i>larger</i> then it is not compressed.</p>
<dt><code>&#8211;compress-debug-sections=none</code></p>
<dd>
<dt><code>&#8211;compress-debug-sections=zlib</code></p>
<dd>
<dt><code>&#8211;compress-debug-sections=zlib-gnu</code></p>
<dd>
<dt><code>&#8211;compress-debug-sections=zlib-gabi</code></p>
<dd> These options control how <font SIZE="-1">DWARF</font> debug sections are compressed. <code>&#8211;compress-debug-sections=none</code> is equivalent to <code>&#8211;nocompress-debug-sections</code>. <code>&#8211;compress-debug-sections=zlib</code> and <code>&#8211;compress-debug-sections=zlib-gabi</code> are equivalent to <code>&#8211;compress-debug-sections</code>. <code>&#8211;compress-debug-sections=zlib-gnu</code> compresses <font SIZE="-1">DWARF</font> debug sections using zlib. The debug sections are renamed to begin with <code>.zdebug</code>. Note if compression would make a given section <i>larger</i> then it is not compressed nor renamed.</p>
<dt><code>&#8211;nocompress-debug-sections</code></p>
<dd> Do not compress <font SIZE="-1">DWARF</font> debug sections. This is usually the default for all targets except the x86/x86_64, but a configure time option can be used to override this.</p>
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
<dd> Generate debugging information for each assembler source line using whichever debug format is preferred by the target. This currently means either <font SIZE="-1">STABS, ECOFF</font> or <font SIZE="-1">DWARF2.</font> When the debug format is <font SIZE="-1">DWARF</font> then a <tt>&quot;.debug_info&quot;</tt> and <tt>&quot;.debug_line&quot;</tt> section is only emitted when the assembly file doesn&#8217;t generate one itself.</p>
<dt><code>&#8211;gstabs</code></p>
<dd> Generate stabs debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.</p>
<dt><code>&#8211;gstabs+</code></p>
<dd> Generate stabs debugging information for each assembler line, with <font SIZE="-1">GNU</font> extensions that probably only gdb can handle, and that could make other debuggers crash or refuse to read your program. This may help debugging assembler code. Currently the only <font SIZE="-1">GNU</font> extension is the location of the current working directory at assembling time.</p>
<dt><code>&#8211;gdwarf-2</code></p>
<dd> Generate <font SIZE="-1">DWARF2</font> debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it. Note&#8212;this option is only supported by some targets, not all of them.</p>
<dt><code>&#8211;gdwarf-3</code></p>
<dd> This option is the same as the <code>&#8211;gdwarf-2</code> option, except that it allows for the possibility of the generation of extra debug information as per version 3 of the <font SIZE="-1">DWARF</font> specification. Note &#8211; enabling this option does not guarantee the generation of any extra information, the choice to do so is on a per target basis.</p>
<dt><code>&#8211;gdwarf-4</code></p>
<dd> This option is the same as the <code>&#8211;gdwarf-2</code> option, except that it allows for the possibility of the generation of extra debug information as per version 4 of the <font SIZE="-1">DWARF</font> specification. Note &#8211; enabling this option does not guarantee the generation of any extra information, the choice to do so is on a per target basis.</p>
<dt><code>&#8211;gdwarf-5</code></p>
<dd> This option is the same as the <code>&#8211;gdwarf-2</code> option, except that it allows for the possibility of the generation of extra debug information as per version 5 of the <font SIZE="-1">DWARF</font> specification. Note &#8211; enabling this option does not guarantee the generation of any extra information, the choice to do so is on a per target basis.</p>
<dt><code>&#8211;gdwarf-sections</code></p>
<dd> Instead of creating a .debug_line section, create a series of .debug_line.<i>foo</i> sections where <i>foo</i> is the name of the corresponding code section. For example a code section called <i>.text.func</i> will have its dwarf line number information placed into a section called <i>.debug_line.text.func</i>. If the code section is just called <i>.text</i> then debug line section will still be called just <i>.debug_line</i> without any suffix.</p>
<dt><code>&#8211;gdwarf-cie-version=</code><i>version</i></p>
<dd> Control which version of <font SIZE="-1">DWARF</font> Common Information Entries (CIEs) are produced. When this flag is not specificed the default is version 1, though some targets can modify this default. Other possible values for <i>version</i> are 3 or 4.</p>
<dt><code>&#8211;size-check=error</code></p>
<dd>
<dt><code>&#8211;size-check=warning</code></p>
<dd> Issue an error or warning for invalid <font SIZE="-1">ELF</font> .size directive.</p>
<dt><code>&#8211;elf-stt-common=no</code></p>
<dd>
<dt><code>&#8211;elf-stt-common=yes</code></p>
<dd> These options control whether the <font SIZE="-1">ELF</font> assembler should generate common symbols with the <tt>&quot;STT_COMMON&quot;</tt> type. The default can be controlled by a configure option <code>&#8211;enable-elf-stt-common</code>.</p>
<dt><code>&#8211;generate-missing-build-notes=yes</code></p>
<dd>
<dt><code>&#8211;generate-missing-build-notes=no</code></p>
<dd> These options control whether the <font SIZE="-1">ELF</font> assembler should generate <font SIZE="-1">GNU</font> Build attribute notes if none are present in the input sources. The default can be controlled by the <code>&#8211;enable-generate-build-notes</code> configure option.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the command-line options and exit.</p>
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
<dt><code>&#8211;multibyte-handling=allow</code></p>
<dd>
<dt><code>&#8211;multibyte-handling=warn</code></p>
<dd>
<dt><code>&#8211;multibyte-handling=warn-sym-only</code></p>
<dd> Controls how the assembler handles multibyte characters in the input. The default (which can be restored by using the <code>allow</code> argument) is to allow such characters without complaint. Using the <code>warn</code> argument will make the assembler generate a warning message whenever any multibyte character is encountered. Using the <code>warn-sym-only</code> argument will only cause a warning to be generated when a symbol is defined with a name that contains multibyte characters. (References to undefined symbols will not generate a warning).</p>
<dt><code>&#8211;no-pad-sections</code></p>
<dd> Stop the assembler for padding the ends of output sections to the alignment of that section. The default is to pad the sections, but this can waste space which might be needed on targets which have tight memory constraints.</p>
<dt><code>-o</code> <i>objfile</i></p>
<dd> Name the object-file output from <code>as</code> <i>objfile</i>.</p>
<dt><code>-R</code></p>
<dd> Fold the data section into the text section.</p>
<dt><code>&#8211;sectname-subst</code></p>
<dd> Honor substitution sequences in section names.</p>
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
<dd> This option specifies the target processor. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target processor. The following processor names are recognized: <tt>&quot;cortex-a34&quot;</tt>, <tt>&quot;cortex-a35&quot;</tt>, <tt>&quot;cortex-a53&quot;</tt>, <tt>&quot;cortex-a55&quot;</tt>, <tt>&quot;cortex-a57&quot;</tt>, <tt>&quot;cortex-a65&quot;</tt>, <tt>&quot;cortex-a65ae&quot;</tt>, <tt>&quot;cortex-a72&quot;</tt>, <tt>&quot;cortex-a73&quot;</tt>, <tt>&quot;cortex-a75&quot;</tt>, <tt>&quot;cortex-a76&quot;</tt>, <tt>&quot;cortex-a76ae&quot;</tt>, <tt>&quot;cortex-a77&quot;</tt>, <tt>&quot;cortex-a78&quot;</tt>, <tt>&quot;cortex-a78ae&quot;</tt>, <tt>&quot;cortex-a78c&quot;</tt>, <tt>&quot;cortex-a510&quot;</tt>, <tt>&quot;cortex-a710&quot;</tt>, <tt>&quot;ares&quot;</tt>, <tt>&quot;exynos-m1&quot;</tt>, <tt>&quot;falkor&quot;</tt>, <tt>&quot;neoverse-n1&quot;</tt>, <tt>&quot;neoverse-n2&quot;</tt>, <tt>&quot;neoverse-e1&quot;</tt>, <tt>&quot;neoverse-v1&quot;</tt>, <tt>&quot;qdf24xx&quot;</tt>, <tt>&quot;saphira&quot;</tt>, <tt>&quot;thunderx&quot;</tt>, <tt>&quot;vulcan&quot;</tt>, <tt>&quot;xgene1&quot;</tt> <tt>&quot;xgene2&quot;</tt>, <tt>&quot;cortex-r82&quot;</tt>, <tt>&quot;cortex-x1&quot;</tt>, and <tt>&quot;cortex-x2&quot;</tt>. The special name <tt>&quot;all&quot;</tt> may be used to allow the assembler to accept instructions valid for any supported processor, including all optional extensions. </p>
<p> In addition to the basic instruction set, the assembler can be told to accept, or restrict, various extension mnemonics that extend the processor. </p>
<p> If some implementations of a particular processor can have an extension, then then those extensions are automatically enabled. Consequently, you will not normally have to specify any additional extensions.</p>
<dt><code>-march=</code><i>architecture</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> This option specifies the target architecture. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target architecture. The following architecture names are recognized: <tt>&quot;armv8-a&quot;</tt>, <tt>&quot;armv8.1-a&quot;</tt>, <tt>&quot;armv8.2-a&quot;</tt>, <tt>&quot;armv8.3-a&quot;</tt>, <tt>&quot;armv8.4-a&quot;</tt> <tt>&quot;armv8.5-a&quot;</tt>, <tt>&quot;armv8.6-a&quot;</tt>, <tt>&quot;armv8.7-a&quot;</tt>, <tt>&quot;armv8.8-a&quot;</tt>, <tt>&quot;armv8-r&quot;</tt>, <tt>&quot;armv9-a&quot;</tt>, <tt>&quot;armv9.1-a&quot;</tt>, <tt>&quot;armv9.2-a&quot;</tt>, and <tt>&quot;armv9.3-a&quot;</tt>. </p>
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
<dt><code>-mcpu=</code><i>cpu</i></p>
<dd> This option selects the core processor variant.</p>
<dt><code>-EB | -EL</code></p>
<dd> Select either big-endian (-EB) or little-endian (-EL) output.</p>
<dt><code>-mcode-density</code></p>
<dd> Enable Code Density extension instructions.</dl>
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
<p> The following options are available when as is configured for the Linux kernel <font SIZE="-1">BPF</font> processor family. </p>
<p> <tt>@chapter</tt> <font SIZE="-1">BPF</font> Dependent Features</p>
<h3>Options</h3>
<dl>
<dt><code>-EB</code></p>
<dd> This option specifies that the assembler should emit big-endian eBPF.</p>
<dt><code>-EL</code></p>
<dd> This option specifies that the assembler should emit little-endian eBPF.</dl>
<p> Note that if no endianness option is specified in the command line, the host endianness is used. See the info pages for documentation of the CRIS-specific options. </p>
<p> The following options are available when as is configured for the C-SKY processor family.</p>
<dl>
<dt><code>-march=</code><i>archname</i></p>
<dd> Assemble for architecture <i>archname</i>. The <code>&#8211;help</code> option lists valid values for <i>archname</i>.</p>
<dt><code>-mcpu=</code><i>cpuname</i></p>
<dd> Assemble for architecture <i>cpuname</i>. The <code>&#8211;help</code> option lists valid values for <i>cpuname</i>.</p>
<dt><code>-EL</code></p>
<dd>
<dt><code>-mlittle-endian</code></p>
<dd> Generate little-endian output.</p>
<dt><code>-EB</code></p>
<dd>
<dt><code>-mbig-endian</code></p>
<dd> Generate big-endian output.</p>
<dt><code>-fpic</code></p>
<dd>
<dt><code>-pic</code></p>
<dd> Generate position-independent code.</p>
<dt><code>-mljump</code></p>
<dd>
<dt><code>-mno-ljump</code></p>
<dd> Enable/disable transformation of the short branch instructions <tt>&quot;jbf&quot;</tt>, <tt>&quot;jbt&quot;</tt>, and <tt>&quot;jbr&quot;</tt> to <tt>&quot;jmpi&quot;</tt>. This option is for V2 processors only. It is ignored on <font SIZE="-1">CK801</font> and <font SIZE="-1">CK802</font> targets, which do not support the <tt>&quot;jmpi&quot;</tt> instruction, and is enabled by default for other processors.</p>
<dt><code>-mbranch-stub</code></p>
<dd>
<dt><code>-mno-branch-stub</code></p>
<dd> Pass through <tt>&quot;R_CKCORE_PCREL_IMM26BY2&quot;</tt> relocations for <tt>&quot;bsr&quot;</tt> instructions to the linker. </p>
<p> This option is only available for bare-metal C-SKY V2 <font SIZE="-1">ELF</font> targets, where it is enabled by default. It cannot be used in code that will be dynamically linked against shared libraries.</p>
<dt><code>-force2bsr</code></p>
<dd>
<dt><code>-mforce2bsr</code></p>
<dd>
<dt><code>-no-force2bsr</code></p>
<dd>
<dt><code>-mno-force2bsr</code></p>
<dd> Enable/disable transformation of <tt>&quot;jbsr&quot;</tt> instructions to <tt>&quot;bsr&quot;</tt>. This option is always enabled (and <code>-mno-force2bsr</code> is ignored) for <font SIZE="-1">CK801/CK802</font> targets. It is also always enabled when <code>-mbranch-stub</code> is in effect.</p>
<dt><code>-jsri2bsr</code></p>
<dd>
<dt><code>-mjsri2bsr</code></p>
<dd>
<dt><code>-no-jsri2bsr</code></p>
<dd>
<dt><code>-mno-jsri2bsr</code></p>
<dd> Enable/disable transformation of <tt>&quot;jsri&quot;</tt> instructions to <tt>&quot;bsr&quot;</tt>. This option is enabled by default.</p>
<dt><code>-mnolrw</code></p>
<dd>
<dt><code>-mno-lrw</code></p>
<dd> Enable/disable transformation of <tt>&quot;lrw&quot;</tt> instructions into a <tt>&quot;movih&quot;</tt>/<tt>&quot;ori&quot;</tt> pair.</p>
<dt><code>-melrw</code></p>
<dd>
<dt><code>-mno-elrw</code></p>
<dd> Enable/disable extended <tt>&quot;lrw&quot;</tt> instructions. This option is enabled by default for CK800-series processors.</p>
<dt><code>-mlaf</code></p>
<dd>
<dt><code>-mliterals-after-func</code></p>
<dd>
<dt><code>-mno-laf</code></p>
<dd>
<dt><code>-mno-literals-after-func</code></p>
<dd> Enable/disable placement of literal pools after each function.</p>
<dt><code>-mlabr</code></p>
<dd>
<dt><code>-mliterals-after-br</code></p>
<dd>
<dt><code>-mno-labr</code></p>
<dd>
<dt><code>-mnoliterals-after-br</code></p>
<dd> Enable/disable placement of literal pools after unconditional branches. This option is enabled by default.</p>
<dt><code>-mistack</code></p>
<dd>
<dt><code>-mno-istack</code></p>
<dd> Enable/disable interrupt stack instructions. This option is enabled by default on <font SIZE="-1">CK801, CK802,</font> and <font SIZE="-1">CK802</font> processors.</dl>
<p> The following options explicitly enable certain optional instructions. These features are also enabled implicitly by using <tt>&quot;-mcpu=&quot;</tt> to specify a processor that supports it.</p>
<dl>
<dt><code>-mhard-float</code></p>
<dd> Enable hard float instructions.</p>
<dt><code>-mmp</code></p>
<dd> Enable multiprocessor instructions.</p>
<dt><code>-mcp</code></p>
<dd> Enable coprocessor instructions.</p>
<dt><code>-mcache</code></p>
<dd> Enable cache prefetch instruction.</p>
<dt><code>-msecurity</code></p>
<dd> Enable C-SKY security instructions.</p>
<dt><code>-mtrust</code></p>
<dd> Enable C-SKY trust instructions.</p>
<dt><code>-mdsp</code></p>
<dd> Enable <font SIZE="-1">DSP</font> instructions.</p>
<dt><code>-medsp</code></p>
<dd> Enable enhanced <font SIZE="-1">DSP</font> instructions.</p>
<dt><code>-mvdsp</code></p>
<dd> Enable vector <font SIZE="-1">DSP</font> instructions.</dl>
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
<dd> Support H&#8217;00 style hex constants in addition to 0x00 style.</p>
<dt><code>-mach=</code><i>name</i></p>
<dd> Sets the H8300 machine variant. The following machine names are recognised: <tt>&quot;h8300h&quot;</tt>, <tt>&quot;h8300hn&quot;</tt>, <tt>&quot;h8300s&quot;</tt>, <tt>&quot;h8300sn&quot;</tt>, <tt>&quot;h8300sx&quot;</tt> and <tt>&quot;h8300sxn&quot;</tt>.</dl>
<p> The following options are available when as is configured for an i386 processor.</p>
<dl>
<dt><code>&#8211;32 | &#8211;x32 | &#8211;64</code></p>
<dd> Select the word size, either 32 bits or 64 bits. <code>&#8211;32</code> implies Intel i386 architecture, while <code>&#8211;x32</code> and <code>&#8211;64</code> imply <font SIZE="-1">AMD</font> x86-64 architecture with 32-bit or 64-bit word-size respectively. </p>
<p> These options are only available with the <font SIZE="-1">ELF</font> object file format, and require that the necessary <font SIZE="-1">BFD</font> support has been included (on a 32-bit platform you have to add &#8211;enable-64-bit-bfd to configure enable 64-bit usage and use x86-64 as target platform).</p>
<dt><code>-n</code></p>
<dd> By default, x86 <font SIZE="-1">GAS</font> replaces multiple nop instructions used for alignment within code sections with multi-byte nop instructions such as leal 0(%esi,1),%esi. This switch disables the optimization if a single byte nop (0x90) is explicitly specified as the fill byte for alignment.</p>
<dt><code>&#8211;divide</code></p>
<dd> On SVR4-derived platforms, the character <code>/</code> is treated as a comment character, which means that it cannot be used in expressions. The <code>&#8211;divide</code> option turns <code>/</code> into a normal character. This does not disable <code>/</code> at the beginning of a line starting a comment, or affect using <code>#</code> for starting a comment.</p>
<dt><code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i><code>[+</code><i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i><code>&#8230;]</code></p>
<dd> This option specifies the target processor. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target processor. The following processor names are recognized: <tt>&quot;i8086&quot;</tt>, <tt>&quot;i186&quot;</tt>, <tt>&quot;i286&quot;</tt>, <tt>&quot;i386&quot;</tt>, <tt>&quot;i486&quot;</tt>, <tt>&quot;i586&quot;</tt>, <tt>&quot;i686&quot;</tt>, <tt>&quot;pentium&quot;</tt>, <tt>&quot;pentiumpro&quot;</tt>, <tt>&quot;pentiumii&quot;</tt>, <tt>&quot;pentiumiii&quot;</tt>, <tt>&quot;pentium4&quot;</tt>, <tt>&quot;prescott&quot;</tt>, <tt>&quot;nocona&quot;</tt>, <tt>&quot;core&quot;</tt>, <tt>&quot;core2&quot;</tt>, <tt>&quot;corei7&quot;</tt>, <tt>&quot;l1om&quot;</tt>, <tt>&quot;k1om&quot;</tt>, <tt>&quot;iamcu&quot;</tt>, <tt>&quot;k6&quot;</tt>, <tt>&quot;k6_2&quot;</tt>, <tt>&quot;athlon&quot;</tt>, <tt>&quot;opteron&quot;</tt>, <tt>&quot;k8&quot;</tt>, <tt>&quot;amdfam10&quot;</tt>, <tt>&quot;bdver1&quot;</tt>, <tt>&quot;bdver2&quot;</tt>, <tt>&quot;bdver3&quot;</tt>, <tt>&quot;bdver4&quot;</tt>, <tt>&quot;znver1&quot;</tt>, <tt>&quot;znver2&quot;</tt>, <tt>&quot;znver3&quot;</tt>, <tt>&quot;btver1&quot;</tt>, <tt>&quot;btver2&quot;</tt>, <tt>&quot;generic32&quot;</tt> and <tt>&quot;generic64&quot;</tt>. </p>
<p> In addition to the basic instruction set, the assembler can be told to accept various extension mnemonics. For example, <tt>&quot;-march=i686+sse4+vmx&quot;</tt> extends <i>i686</i> with <i>sse4</i> and <i>vmx</i>. The following extensions are currently supported: <tt>8087</tt>, <tt>287</tt>, <tt>387</tt>, <tt>687</tt>, <tt>&quot;no87&quot;</tt>, <tt>&quot;no287&quot;</tt>, <tt>&quot;no387&quot;</tt>, <tt>&quot;no687&quot;</tt>, <tt>&quot;cmov&quot;</tt>, <tt>&quot;nocmov&quot;</tt>, <tt>&quot;fxsr&quot;</tt>, <tt>&quot;nofxsr&quot;</tt>, <tt>&quot;mmx&quot;</tt>, <tt>&quot;nommx&quot;</tt>, <tt>&quot;sse&quot;</tt>, <tt>&quot;sse2&quot;</tt>, <tt>&quot;sse3&quot;</tt>, <tt>&quot;sse4a&quot;</tt>, <tt>&quot;ssse3&quot;</tt>, <tt>&quot;sse4.1&quot;</tt>, <tt>&quot;sse4.2&quot;</tt>, <tt>&quot;sse4&quot;</tt>, <tt>&quot;nosse&quot;</tt>, <tt>&quot;nosse2&quot;</tt>, <tt>&quot;nosse3&quot;</tt>, <tt>&quot;nosse4a&quot;</tt>, <tt>&quot;nossse3&quot;</tt>, <tt>&quot;nosse4.1&quot;</tt>, <tt>&quot;nosse4.2&quot;</tt>, <tt>&quot;nosse4&quot;</tt>, <tt>&quot;avx&quot;</tt>, <tt>&quot;avx2&quot;</tt>, <tt>&quot;noavx&quot;</tt>, <tt>&quot;noavx2&quot;</tt>, <tt>&quot;adx&quot;</tt>, <tt>&quot;rdseed&quot;</tt>, <tt>&quot;prfchw&quot;</tt>, <tt>&quot;smap&quot;</tt>, <tt>&quot;mpx&quot;</tt>, <tt>&quot;sha&quot;</tt>, <tt>&quot;rdpid&quot;</tt>, <tt>&quot;ptwrite&quot;</tt>, <tt>&quot;cet&quot;</tt>, <tt>&quot;gfni&quot;</tt>, <tt>&quot;vaes&quot;</tt>, <tt>&quot;vpclmulqdq&quot;</tt>, <tt>&quot;prefetchwt1&quot;</tt>, <tt>&quot;clflushopt&quot;</tt>, <tt>&quot;se1&quot;</tt>, <tt>&quot;clwb&quot;</tt>, <tt>&quot;movdiri&quot;</tt>, <tt>&quot;movdir64b&quot;</tt>, <tt>&quot;enqcmd&quot;</tt>, <tt>&quot;serialize&quot;</tt>, <tt>&quot;tsxldtrk&quot;</tt>, <tt>&quot;kl&quot;</tt>, <tt>&quot;nokl&quot;</tt>, <tt>&quot;widekl&quot;</tt>, <tt>&quot;nowidekl&quot;</tt>, <tt>&quot;hreset&quot;</tt>, <tt>&quot;avx512f&quot;</tt>, <tt>&quot;avx512cd&quot;</tt>, <tt>&quot;avx512er&quot;</tt>, <tt>&quot;avx512pf&quot;</tt>, <tt>&quot;avx512vl&quot;</tt>, <tt>&quot;avx512bw&quot;</tt>, <tt>&quot;avx512dq&quot;</tt>, <tt>&quot;avx512ifma&quot;</tt>, <tt>&quot;avx512vbmi&quot;</tt>, <tt>&quot;avx512_4fmaps&quot;</tt>, <tt>&quot;avx512_4vnniw&quot;</tt>, <tt>&quot;avx512_vpopcntdq&quot;</tt>, <tt>&quot;avx512_vbmi2&quot;</tt>, <tt>&quot;avx512_vnni&quot;</tt>, <tt>&quot;avx512_bitalg&quot;</tt>, <tt>&quot;avx512_vp2intersect&quot;</tt>, <tt>&quot;tdx&quot;</tt>, <tt>&quot;avx512_bf16&quot;</tt>, <tt>&quot;avx_vnni&quot;</tt>, <tt>&quot;avx512_fp16&quot;</tt>, <tt>&quot;noavx512f&quot;</tt>, <tt>&quot;noavx512cd&quot;</tt>, <tt>&quot;noavx512er&quot;</tt>, <tt>&quot;noavx512pf&quot;</tt>, <tt>&quot;noavx512vl&quot;</tt>, <tt>&quot;noavx512bw&quot;</tt>, <tt>&quot;noavx512dq&quot;</tt>, <tt>&quot;noavx512ifma&quot;</tt>, <tt>&quot;noavx512vbmi&quot;</tt>, <tt>&quot;noavx512_4fmaps&quot;</tt>, <tt>&quot;noavx512_4vnniw&quot;</tt>, <tt>&quot;noavx512_vpopcntdq&quot;</tt>, <tt>&quot;noavx512_vbmi2&quot;</tt>, <tt>&quot;noavx512_vnni&quot;</tt>, <tt>&quot;noavx512_bitalg&quot;</tt>, <tt>&quot;noavx512_vp2intersect&quot;</tt>, <tt>&quot;notdx&quot;</tt>, <tt>&quot;noavx512_bf16&quot;</tt>, <tt>&quot;noavx_vnni&quot;</tt>, <tt>&quot;noavx512_fp16&quot;</tt>, <tt>&quot;noenqcmd&quot;</tt>, <tt>&quot;noserialize&quot;</tt>, <tt>&quot;notsxldtrk&quot;</tt>, <tt>&quot;amx_int8&quot;</tt>, <tt>&quot;noamx_int8&quot;</tt>, <tt>&quot;amx_bf16&quot;</tt>, <tt>&quot;noamx_bf16&quot;</tt>, <tt>&quot;amx_tile&quot;</tt>, <tt>&quot;noamx_tile&quot;</tt>, <tt>&quot;nouintr&quot;</tt>, <tt>&quot;nohreset&quot;</tt>, <tt>&quot;vmx&quot;</tt>, <tt>&quot;vmfunc&quot;</tt>, <tt>&quot;smx&quot;</tt>, <tt>&quot;xsave&quot;</tt>, <tt>&quot;xsaveopt&quot;</tt>, <tt>&quot;xsavec&quot;</tt>, <tt>&quot;xsaves&quot;</tt>, <tt>&quot;aes&quot;</tt>, <tt>&quot;pclmul&quot;</tt>, <tt>&quot;fsgsbase&quot;</tt>, <tt>&quot;rdrnd&quot;</tt>, <tt>&quot;f16c&quot;</tt>, <tt>&quot;bmi2&quot;</tt>, <tt>&quot;fma&quot;</tt>, <tt>&quot;movbe&quot;</tt>, <tt>&quot;ept&quot;</tt>, <tt>&quot;lzcnt&quot;</tt>, <tt>&quot;popcnt&quot;</tt>, <tt>&quot;hle&quot;</tt>, <tt>&quot;rtm&quot;</tt>, <tt>&quot;invpcid&quot;</tt>, <tt>&quot;clflush&quot;</tt>, <tt>&quot;mwaitx&quot;</tt>, <tt>&quot;clzero&quot;</tt>, <tt>&quot;wbnoinvd&quot;</tt>, <tt>&quot;pconfig&quot;</tt>, <tt>&quot;waitpkg&quot;</tt>, <tt>&quot;uintr&quot;</tt>, <tt>&quot;cldemote&quot;</tt>, <tt>&quot;rdpru&quot;</tt>, <tt>&quot;mcommit&quot;</tt>, <tt>&quot;sev_es&quot;</tt>, <tt>&quot;lwp&quot;</tt>, <tt>&quot;fma4&quot;</tt>, <tt>&quot;xop&quot;</tt>, <tt>&quot;cx16&quot;</tt>, <tt>&quot;syscall&quot;</tt>, <tt>&quot;rdtscp&quot;</tt>, <tt>&quot;3dnow&quot;</tt>, <tt>&quot;3dnowa&quot;</tt>, <tt>&quot;sse4a&quot;</tt>, <tt>&quot;sse5&quot;</tt>, <tt>&quot;snp&quot;</tt>, <tt>&quot;invlpgb&quot;</tt>, <tt>&quot;tlbsync&quot;</tt>, <tt>&quot;svme&quot;</tt> and <tt>&quot;padlock&quot;</tt>. Note that rather than extending a basic instruction set, the extension mnemonics starting with <tt>&quot;no&quot;</tt> revoke the respective functionality. </p>
<p> When the <tt>&quot;.arch&quot;</tt> directive is used with <code>-march</code>, the <tt>&quot;.arch&quot;</tt> directive will take precedent.</p>
<dt><code>-mtune=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i></p>
<dd> This option specifies a processor to optimize for. When used in conjunction with the <code>-march</code> option, only instructions of the processor specified by the <code>-march</code> option will be generated. </p>
<p> Valid <i></i><font SIZE="-1"><i>CPU</i></font><i></i> values are identical to the processor list of <code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i>.</p>
<dt><code>-msse2avx</code></p>
<dd> This option specifies that the assembler should encode <font SIZE="-1">SSE</font> instructions with <font SIZE="-1">VEX</font> prefix.</p>
<dt><code>-muse-unaligned-vector-move</code></p>
<dd> This option specifies that the assembler should encode aligned vector move as unaligned vector move.</p>
<dt><code>-msse-check=</code><i>none</i></p>
<dd>
<dt><code>-msse-check=</code><i>warning</i></p>
<dd>
<dt><code>-msse-check=</code><i>error</i></p>
<dd> These options control if the assembler should check <font SIZE="-1">SSE</font> instructions. <code>-msse-check=</code><i>none</i> will make the assembler not to check <font SIZE="-1">SSE</font> instructions, which is the default. <code>-msse-check=</code><i>warning</i> will make the assembler issue a warning for any <font SIZE="-1">SSE</font> instruction. <code>-msse-check=</code><i>error</i> will make the assembler issue an error for any <font SIZE="-1">SSE</font> instruction.</p>
<dt><code>-mavxscalar=</code><i>128</i></p>
<dd>
<dt><code>-mavxscalar=</code><i>256</i></p>
<dd> These options control how the assembler should encode scalar <font SIZE="-1">AVX</font> instructions. <code>-mavxscalar=</code><i>128</i> will encode scalar <font SIZE="-1">AVX</font> instructions with 128bit vector length, which is the default. <code>-mavxscalar=</code><i>256</i> will encode scalar <font SIZE="-1">AVX</font> instructions with 256bit vector length. </p>
<p> <font SIZE="-1">WARNING:</font> Don&#8217;t use this for production code &#8211; due to <font SIZE="-1">CPU</font> errata the resulting code may not work on certain models.</p>
<dt><code>-mvexwig=</code><i>0</i></p>
<dd>
<dt><code>-mvexwig=</code><i>1</i></p>
<dd> These options control how the assembler should encode <font SIZE="-1">VEX</font>.W-ignored (<font SIZE="-1">WIG</font>) <font SIZE="-1">VEX</font> instructions. <code>-mvexwig=</code><i>0</i> will encode <font SIZE="-1">WIG VEX</font> instructions with vex.w = 0, which is the default. <code>-mvexwig=</code><i>1</i> will encode <font SIZE="-1">WIG EVEX</font> instructions with vex.w = 1. </p>
<p> <font SIZE="-1">WARNING:</font> Don&#8217;t use this for production code &#8211; due to <font SIZE="-1">CPU</font> errata the resulting code may not work on certain models.</p>
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
<dd> This option specifies that registers don&#8217;t require a <code>%</code> prefix. The <tt>&quot;.att_syntax&quot;</tt> and <tt>&quot;.intel_syntax&quot;</tt> directives will take precedent.</p>
<dt><code>-madd-bnd-prefix</code></p>
<dd> This option forces the assembler to add <font SIZE="-1">BND</font> prefix to all branches, even if such prefix was not explicitly specified in the source code.</p>
<dt><code>-mno-shared</code></p>
<dd> On <font SIZE="-1">ELF</font> target, the assembler normally optimizes out non-PLT relocations against defined non-weak global branch targets with default visibility. The <code>-mshared</code> option tells the assembler to generate code which may go into a shared library where all non-weak global branch targets with default visibility can be preempted. The resulting code is slightly bigger. This option only affects the handling of branch instructions.</p>
<dt><code>-mbig-obj</code></p>
<dd> On <font SIZE="-1">PE/COFF</font> target this option forces the use of big object file format, which allows more than 32768 sections.</p>
<dt><code>-momit-lock-prefix=</code><i>no</i></p>
<dd>
<dt><code>-momit-lock-prefix=</code><i>yes</i></p>
<dd> These options control how the assembler should encode lock prefix. This option is intended as a workaround for processors, that fail on lock prefix. This option can only be safely used with single-core, single-thread computers <code>-momit-lock-prefix=</code><i>yes</i> will omit all lock prefixes. <code>-momit-lock-prefix=</code><i>no</i> will encode lock prefix as usual, which is the default.</p>
<dt><code>-mfence-as-lock-add=</code><i>no</i></p>
<dd>
<dt><code>-mfence-as-lock-add=</code><i>yes</i></p>
<dd> These options control how the assembler should encode lfence, mfence and sfence. <code>-mfence-as-lock-add=</code><i>yes</i> will encode lfence, mfence and sfence as <code>lock addl </code>$0x0<code>, (%rsp)</code> in 64-bit mode and <code>lock addl </code>$0x0<code>, (%esp)</code> in 32-bit mode. <code>-mfence-as-lock-add=</code><i>no</i> will encode lfence, mfence and sfence as usual, which is the default.</p>
<dt><code>-mrelax-relocations=</code><i>no</i></p>
<dd>
<dt><code>-mrelax-relocations=</code><i>yes</i></p>
<dd> These options control whether the assembler should generate relax relocations, R_386_GOT32X, in 32-bit mode, or R_X86_64_GOTPCRELX and R_X86_64_REX_GOTPCRELX, in 64-bit mode. <code>-mrelax-relocations=</code><i>yes</i> will generate relax relocations. <code>-mrelax-relocations=</code><i>no</i> will not generate relax relocations. The default can be controlled by a configure option <code>&#8211;enable-x86-relax-relocations</code>.</p>
<dt><code>-malign-branch-boundary=</code><i></i><font SIZE="-1"><i>NUM</i></font><i></i></p>
<dd> This option controls how the assembler should align branches with segment prefixes or <font SIZE="-1">NOP.</font> <i></i><font SIZE="-1"><i>NUM</i></font><i></i> must be a power of 2. It should be 0 or no less than 16. Branches will be aligned within <i></i><font SIZE="-1"><i>NUM</i></font><i></i> byte boundary. <code>-malign-branch-boundary=0</code>, which is the default, doesn&#8217;t align branches.</p>
<dt><code>-malign-branch=</code><i></i><font SIZE="-1"><i>TYPE</i></font><i></i><code>[+</code><i></i><font SIZE="-1"><i>TYPE</i></font><i></i><code>&#8230;]</code></p>
<dd> This option specifies types of branches to align. <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> is combination of <code>jcc</code>, which aligns conditional jumps, <code>fused</code>, which aligns fused conditional jumps, <code>jmp</code>, which aligns unconditional jumps, <code>call</code> which aligns calls, <code>ret</code>, which aligns rets, <code>indirect</code>, which aligns indirect jumps and calls. The default is <code>-malign-branch=jcc+fused+jmp</code>.</p>
<dt><code>-malign-branch-prefix-size=</code><i></i><font SIZE="-1"><i>NUM</i></font><i></i></p>
<dd> This option specifies the maximum number of prefixes on an instruction to align branches. <i></i><font SIZE="-1"><i>NUM</i></font><i></i> should be between 0 and 5. The default <i></i><font SIZE="-1"><i>NUM</i></font><i></i> is 5.</p>
<dt><code>-mbranches-within-32B-boundaries</code></p>
<dd> This option aligns conditional jumps, fused conditional jumps and unconditional jumps within 32 byte boundary with up to 5 segment prefixes on an instruction. It is equivalent to <code>-malign-branch-boundary=32</code> <code>-malign-branch=jcc+fused+jmp</code> <code>-malign-branch-prefix-size=5</code>. The default doesn&#8217;t align branches.</p>
<dt><code>-mlfence-after-load=</code><i>no</i></p>
<dd>
<dt><code>-mlfence-after-load=</code><i>yes</i></p>
<dd> These options control whether the assembler should generate lfence after load instructions. <code>-mlfence-after-load=</code><i>yes</i> will generate lfence. <code>-mlfence-after-load=</code><i>no</i> will not generate lfence, which is the default.</p>
<dt><code>-mlfence-before-indirect-branch=</code><i>none</i></p>
<dd>
<dt><code>-mlfence-before-indirect-branch=</code><i>all</i></p>
<dd>
<dt><code>-mlfence-before-indirect-branch=</code><i>register</i></p>
<dd>
<dt><code>-mlfence-before-indirect-branch=</code><i>memory</i></p>
<dd> These options control whether the assembler should generate lfence before indirect near branch instructions. <code>-mlfence-before-indirect-branch=</code><i>all</i> will generate lfence before indirect near branch via register and issue a warning before indirect near branch via memory. It also implicitly sets <code>-mlfence-before-ret=</code><i>shl</i> when there&#8217;s no explicit <code>-mlfence-before-ret=</code>. <code>-mlfence-before-indirect-branch=</code><i>register</i> will generate lfence before indirect near branch via register. <code>-mlfence-before-indirect-branch=</code><i>memory</i> will issue a warning before indirect near branch via memory. <code>-mlfence-before-indirect-branch=</code><i>none</i> will not generate lfence nor issue warning, which is the default. Note that lfence won&#8217;t be generated before indirect near branch via register with <code>-mlfence-after-load=</code><i>yes</i> since lfence will be generated after loading branch target register.</p>
<dt><code>-mlfence-before-ret=</code><i>none</i></p>
<dd>
<dt><code>-mlfence-before-ret=</code><i>shl</i></p>
<dd>
<dt><code>-mlfence-before-ret=</code><i>or</i></p>
<dd>
<dt><code>-mlfence-before-ret=</code><i>yes</i></p>
<dd>
<dt><code>-mlfence-before-ret=</code><i>not</i></p>
<dd> These options control whether the assembler should generate lfence before ret. <code>-mlfence-before-ret=</code><i>or</i> will generate generate or instruction with lfence. <code>-mlfence-before-ret=</code><i>shl/yes</i> will generate shl instruction with lfence. <code>-mlfence-before-ret=</code><i>not</i> will generate not instruction with lfence. <code>-mlfence-before-ret=</code><i>none</i> will not generate lfence, which is the default.</p>
<dt><code>-mx86-used-note=</code><i>no</i></p>
<dd>
<dt><code>-mx86-used-note=</code><i>yes</i></p>
<dd> These options control whether the assembler should generate <font SIZE="-1">GNU_PROPERTY_X86_ISA_1_USED</font> and <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_2_USED GNU</font> property notes. The default can be controlled by the <code>&#8211;enable-x86-used-note</code> configure option.</p>
<dt><code>-mevexrcig=</code><i>rne</i></p>
<dd>
<dt><code>-mevexrcig=</code><i>rd</i></p>
<dd>
<dt><code>-mevexrcig=</code><i>ru</i></p>
<dd>
<dt><code>-mevexrcig=</code><i>rz</i></p>
<dd> These options control how the assembler should encode SAE-only <font SIZE="-1">EVEX</font> instructions. <code>-mevexrcig=</code><i>rne</i> will encode <font SIZE="-1">RC</font> bits of <font SIZE="-1">EVEX</font> instruction with 00, which is the default. <code>-mevexrcig=</code><i>rd</i>, <code>-mevexrcig=</code><i>ru</i> and <code>-mevexrcig=</code><i>rz</i> will encode SAE-only <font SIZE="-1">EVEX</font> instructions with 01, 10 and 11 <font SIZE="-1">RC</font> bits, respectively.</p>
<dt><code>-mamd64</code></p>
<dd>
<dt><code>-mintel64</code></p>
<dd> This option specifies that the assembler should accept only <font SIZE="-1">AMD64</font> or Intel64 <font SIZE="-1">ISA</font> in 64-bit mode. The default is to accept common, Intel64 only and <font SIZE="-1">AMD64</font> ISAs.</p>
<dt><code>-O0 | -O | -O1 | -O2 | -Os</code></p>
<dd> Optimize instruction encoding with smaller instruction size. <code>-O</code> and <code>-O1</code> encode 64-bit register load instructions with 64-bit immediate as 32-bit register load instructions with 31-bit or 32-bits immediates, encode 64-bit register clearing instructions with 32-bit register clearing instructions, encode 256-bit/512-bit <font SIZE="-1">VEX/EVEX</font> vector register clearing instructions with 128-bit <font SIZE="-1">VEX</font> vector register clearing instructions, encode 128-bit/256-bit <font SIZE="-1">EVEX</font> vector register load/store instructions with <font SIZE="-1">VEX</font> vector register load/store instructions, and encode 128-bit/256-bit <font SIZE="-1">EVEX</font> packed integer logical instructions with 128-bit/256-bit <font SIZE="-1">VEX</font> packed integer logical. </p>
<p> <code>-O2</code> includes <code>-O1</code> optimization plus encodes 256-bit/512-bit <font SIZE="-1">EVEX</font> vector register clearing instructions with 128-bit <font SIZE="-1">EVEX</font> vector register clearing instructions. In 64-bit mode <font SIZE="-1">VEX</font> encoded instructions with commutative source operands will also have their source operands swapped if this allows using the 2-byte <font SIZE="-1">VEX</font> prefix form instead of the 3-byte one. Certain forms of <font SIZE="-1">AND</font> as well as <font SIZE="-1">OR</font> with the same (register) operand specified twice will also be changed to <font SIZE="-1">TEST.</font> </p>
<p> <code>-Os</code> includes <code>-O2</code> optimization plus encodes 16-bit, 32-bit and 64-bit register tests with immediate as 8-bit register test with immediate. <code>-O0</code> turns off this optimization.</dl>
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
<dd> Generate little-endian output. This is the default.</p>
<dt><code>-march=</code><i>architecture</i></p>
<dd> This option specifies the target architecture. The assembler issues an error message if an attempt is made to assemble an instruction which will not execute on the target architecture. The following architecture names are recognized: <tt>&quot;r1&quot;</tt>, <tt>&quot;r2&quot;</tt>. The default is <tt>&quot;r1&quot;</tt>.</dl>
<p> The following options are available when as is configured for a <font SIZE="-1">PRU</font> processor.</p>
<dl>
<dt><code>-mlink-relax</code></p>
<dd> Assume that <font SIZE="-1">LD</font> would optimize <font SIZE="-1">LDI32</font> instructions by checking the upper 16 bits of the <i>expression</i>. If they are all zeros, then <font SIZE="-1">LD</font> would shorten the <font SIZE="-1">LDI32</font> instruction to a single <font SIZE="-1">LDI.</font> In such case <tt>&quot;as&quot;</tt> will output <font SIZE="-1">DIFF</font> relocations for diff expressions.</p>
<dt><code>-mno-link-relax</code></p>
<dd> Assume that <font SIZE="-1">LD</font> would not optimize <font SIZE="-1">LDI32</font> instructions. As a consequence, <font SIZE="-1">DIFF</font> relocations will not be emitted.</p>
<dt><code>-mno-warn-regname-label</code></p>
<dd> Do not warn if a label name matches a register name. Usually assembler programmers will want this warning to be emitted. C compilers may want to turn this off.</dl>
<p> The following options are available when as is configured for a <font SIZE="-1">MIPS</font> processor.</p>
<dl>
<dt><code>-G</code> <i>num</i></p>
<dd> This option sets the largest size of an object that can be referenced implicitly with the <tt>&quot;gp&quot;</tt> register. It is only accepted for targets that use <font SIZE="-1">ECOFF</font> format, such as a DECstation running Ultrix. The default value is 8.</p>
<dt><code>-EB</code></p>
<dd> Generate &#8220;big endian&#8221; format output.</p>
<dt><code>-EL</code></p>
<dd> Generate &#8220;little endian&#8221; format output.</p>
<dt><code>-mips1</code></p>
<dd>
<dt><code>-mips2</code></p>
<dd>
<dt><code>-mips3</code></p>
<dd>
<dt><code>-mips4</code></p>
<dd>
<dt><code>-mips5</code></p>
<dd>
<dt><code>-mips32</code></p>
<dd>
<dt><code>-mips32r2</code></p>
<dd>
<dt><code>-mips32r3</code></p>
<dd>
<dt><code>-mips32r5</code></p>
<dd>
<dt><code>-mips32r6</code></p>
<dd>
<dt><code>-mips64</code></p>
<dd>
<dt><code>-mips64r2</code></p>
<dd>
<dt><code>-mips64r3</code></p>
<dd>
<dt><code>-mips64r5</code></p>
<dd>
<dt><code>-mips64r6</code></p>
<dd> Generate code for a particular <font SIZE="-1">MIPS</font> Instruction Set Architecture level. <code>-mips1</code> is an alias for <code>-march=r3000</code>, <code>-mips2</code> is an alias for <code>-march=r6000</code>, <code>-mips3</code> is an alias for <code>-march=r4000</code> and <code>-mips4</code> is an alias for <code>-march=r8000</code>. <code>-mips5</code>, <code>-mips32</code>, <code>-mips32r2</code>, <code>-mips32r3</code>, <code>-mips32r5</code>, <code>-mips32r6</code>, <code>-mips64</code>, <code>-mips64r2</code>, <code>-mips64r3</code>, <code>-mips64r5</code>, and <code>-mips64r6</code> correspond to generic <font SIZE="-1">MIPS V, MIPS32, MIPS32</font> Release 2, <font SIZE="-1">MIPS32</font> Release 3, <font SIZE="-1">MIPS32</font> Release 5, <font SIZE="-1">MIPS32</font> Release 6, <font SIZE="-1">MIPS64, MIPS64</font> Release 2, <font SIZE="-1">MIPS64</font> Release 3, <font SIZE="-1">MIPS64</font> Release 5, and <font SIZE="-1">MIPS64</font> Release 6 <font SIZE="-1">ISA</font> processors, respectively.</p>
<dt><code>-march=</code><i>cpu</i></p>
<dd> Generate code for a particular <font SIZE="-1">MIPS CPU.</font></p>
<dt><code>-mtune=</code><i>cpu</i></p>
<dd> Schedule and tune for a particular <font SIZE="-1">MIPS CPU.</font></p>
<dt><code>-mfix7000</code></p>
<dd>
<dt><code>-mno-fix7000</code></p>
<dd> Cause nops to be inserted if the read of the destination register of an mfhi or mflo instruction occurs in the following two instructions.</p>
<dt><code>-mfix-rm7000</code></p>
<dd>
<dt><code>-mno-fix-rm7000</code></p>
<dd> Cause nops to be inserted if a dmult or dmultu instruction is followed by a load instruction.</p>
<dt><code>-mfix-r5900</code></p>
<dd>
<dt><code>-mno-fix-r5900</code></p>
<dd> Do not attempt to schedule the preceding instruction into the delay slot of a branch instruction placed at the end of a short loop of six instructions or fewer and always schedule a <tt>&quot;nop&quot;</tt> instruction there instead. The short loop bug under certain conditions causes loops to execute only once or twice, due to a hardware bug in the R5900 chip.</p>
<dt><code>-mdebug</code></p>
<dd>
<dt><code>-no-mdebug</code></p>
<dd> Cause stabs-style debugging output to go into an ECOFF-style .mdebug section instead of the standard <font SIZE="-1">ELF</font> .stabs sections.</p>
<dt><code>-mpdr</code></p>
<dd>
<dt><code>-mno-pdr</code></p>
<dd> Control generation of <tt>&quot;.pdr&quot;</tt> sections.</p>
<dt><code>-mgp32</code></p>
<dd>
<dt><code>-mfp32</code></p>
<dd> The register sizes are normally inferred from the <font SIZE="-1">ISA</font> and <font SIZE="-1">ABI,</font> but these flags force a certain group of registers to be treated as 32 bits wide at all times. <code>-mgp32</code> controls the size of general-purpose registers and <code>-mfp32</code> controls the size of floating-point registers.</p>
<dt><code>-mgp64</code></p>
<dd>
<dt><code>-mfp64</code></p>
<dd> The register sizes are normally inferred from the <font SIZE="-1">ISA</font> and <font SIZE="-1">ABI,</font> but these flags force a certain group of registers to be treated as 64 bits wide at all times. <code>-mgp64</code> controls the size of general-purpose registers and <code>-mfp64</code> controls the size of floating-point registers.</p>
<dt><code>-mfpxx</code></p>
<dd> The register sizes are normally inferred from the <font SIZE="-1">ISA</font> and <font SIZE="-1">ABI,</font> but using this flag in combination with <code>-mabi=32</code> enables an <font SIZE="-1">ABI</font> variant which will operate correctly with floating-point registers which are 32 or 64 bits wide.</p>
<dt><code>-modd-spreg</code></p>
<dd>
<dt><code>-mno-odd-spreg</code></p>
<dd> Enable use of floating-point operations on odd-numbered single-precision registers when supported by the <font SIZE="-1">ISA.</font> <code>-mfpxx</code> implies <code>-mno-odd-spreg</code>, otherwise the default is <code>-modd-spreg</code>.</p>
<dt><code>-mips16</code></p>
<dd>
<dt><code>-no-mips16</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS 16</font> processor. This is equivalent to putting <tt>&quot;.module mips16&quot;</tt> at the start of the assembly file. <code>-no-mips16</code> turns off this option.</p>
<dt><code>-mmips16e2</code></p>
<dd>
<dt><code>-mno-mips16e2</code></p>
<dd> Enable the use of MIPS16e2 instructions in <font SIZE="-1">MIPS16</font> mode. This is equivalent to putting <tt>&quot;.module mips16e2&quot;</tt> at the start of the assembly file. <code>-mno-mips16e2</code> turns off this option.</p>
<dt><code>-mmicromips</code></p>
<dd>
<dt><code>-mno-micromips</code></p>
<dd> Generate code for the microMIPS processor. This is equivalent to putting <tt>&quot;.module micromips&quot;</tt> at the start of the assembly file. <code>-mno-micromips</code> turns off this option. This is equivalent to putting <tt>&quot;.module nomicromips&quot;</tt> at the start of the assembly file.</p>
<dt><code>-msmartmips</code></p>
<dd>
<dt><code>-mno-smartmips</code></p>
<dd> Enables the SmartMIPS extension to the <font SIZE="-1">MIPS32</font> instruction set. This is equivalent to putting <tt>&quot;.module smartmips&quot;</tt> at the start of the assembly file. <code>-mno-smartmips</code> turns off this option.</p>
<dt><code>-mips3d</code></p>
<dd>
<dt><code>-no-mips3d</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS-3D</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MIPS-3D</font> instructions. <code>-no-mips3d</code> turns off this option.</p>
<dt><code>-mdmx</code></p>
<dd>
<dt><code>-no-mdmx</code></p>
<dd> Generate code for the <font SIZE="-1">MDMX</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MDMX</font> instructions. <code>-no-mdmx</code> turns off this option.</p>
<dt><code>-mdsp</code></p>
<dd>
<dt><code>-mno-dsp</code></p>
<dd> Generate code for the <font SIZE="-1">DSP</font> Release 1 Application Specific Extension. This tells the assembler to accept <font SIZE="-1">DSP</font> Release 1 instructions. <code>-mno-dsp</code> turns off this option.</p>
<dt><code>-mdspr2</code></p>
<dd>
<dt><code>-mno-dspr2</code></p>
<dd> Generate code for the <font SIZE="-1">DSP</font> Release 2 Application Specific Extension. This option implies <code>-mdsp</code>. This tells the assembler to accept <font SIZE="-1">DSP</font> Release 2 instructions. <code>-mno-dspr2</code> turns off this option.</p>
<dt><code>-mdspr3</code></p>
<dd>
<dt><code>-mno-dspr3</code></p>
<dd> Generate code for the <font SIZE="-1">DSP</font> Release 3 Application Specific Extension. This option implies <code>-mdsp</code> and <code>-mdspr2</code>. This tells the assembler to accept <font SIZE="-1">DSP</font> Release 3 instructions. <code>-mno-dspr3</code> turns off this option.</p>
<dt><code>-mmsa</code></p>
<dd>
<dt><code>-mno-msa</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS SIMD</font> Architecture Extension. This tells the assembler to accept <font SIZE="-1">MSA</font> instructions. <code>-mno-msa</code> turns off this option.</p>
<dt><code>-mxpa</code></p>
<dd>
<dt><code>-mno-xpa</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS</font> eXtended Physical Address (<font SIZE="-1">XPA</font>) Extension. This tells the assembler to accept <font SIZE="-1">XPA</font> instructions. <code>-mno-xpa</code> turns off this option.</p>
<dt><code>-mmt</code></p>
<dd>
<dt><code>-mno-mt</code></p>
<dd> Generate code for the <font SIZE="-1">MT</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MT</font> instructions. <code>-mno-mt</code> turns off this option.</p>
<dt><code>-mmcu</code></p>
<dd>
<dt><code>-mno-mcu</code></p>
<dd> Generate code for the <font SIZE="-1">MCU</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MCU</font> instructions. <code>-mno-mcu</code> turns off this option.</p>
<dt><code>-mcrc</code></p>
<dd>
<dt><code>-mno-crc</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS</font> cyclic redundancy check (<font SIZE="-1">CRC</font>) Application Specific Extension. This tells the assembler to accept <font SIZE="-1">CRC</font> instructions. <code>-mno-crc</code> turns off this option.</p>
<dt><code>-mginv</code></p>
<dd>
<dt><code>-mno-ginv</code></p>
<dd> Generate code for the Global INValidate (<font SIZE="-1">GINV</font>) Application Specific Extension. This tells the assembler to accept <font SIZE="-1">GINV</font> instructions. <code>-mno-ginv</code> turns off this option.</p>
<dt><code>-mloongson-mmi</code></p>
<dd>
<dt><code>-mno-loongson-mmi</code></p>
<dd> Generate code for the Loongson MultiMedia extensions Instructions (<font SIZE="-1">MMI</font>) Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MMI</font> instructions. <code>-mno-loongson-mmi</code> turns off this option.</p>
<dt><code>-mloongson-cam</code></p>
<dd>
<dt><code>-mno-loongson-cam</code></p>
<dd> Generate code for the Loongson Content Address Memory (<font SIZE="-1">CAM</font>) instructions. This tells the assembler to accept Loongson <font SIZE="-1">CAM</font> instructions. <code>-mno-loongson-cam</code> turns off this option.</p>
<dt><code>-mloongson-ext</code></p>
<dd>
<dt><code>-mno-loongson-ext</code></p>
<dd> Generate code for the Loongson EXTensions (<font SIZE="-1">EXT</font>) instructions. This tells the assembler to accept Loongson <font SIZE="-1">EXT</font> instructions. <code>-mno-loongson-ext</code> turns off this option.</p>
<dt><code>-mloongson-ext2</code></p>
<dd>
<dt><code>-mno-loongson-ext2</code></p>
<dd> Generate code for the Loongson EXTensions R2 (<font SIZE="-1">EXT2</font>) instructions. This option implies <code>-mloongson-ext</code>. This tells the assembler to accept Loongson <font SIZE="-1">EXT2</font> instructions. <code>-mno-loongson-ext2</code> turns off this option.</p>
<dt><code>-minsn32</code></p>
<dd>
<dt><code>-mno-insn32</code></p>
<dd> Only use 32-bit instruction encodings when generating code for the microMIPS processor. This option inhibits the use of any 16-bit instructions. This is equivalent to putting <tt>&quot;.set insn32&quot;</tt> at the start of the assembly file. <code>-mno-insn32</code> turns off this option. This is equivalent to putting <tt>&quot;.set noinsn32&quot;</tt> at the start of the assembly file. By default <code>-mno-insn32</code> is selected, allowing all instructions to be used.</p>
<dt><code>&#8211;construct-floats</code></p>
<dd>
<dt><code>&#8211;no-construct-floats</code></p>
<dd> The <code>&#8211;no-construct-floats</code> option disables the construction of double width floating point constants by loading the two halves of the value into the two single width floating point registers that make up the double width register. By default <code>&#8211;construct-floats</code> is selected, allowing construction of these floating point constants.</p>
<dt><code>&#8211;relax-branch</code></p>
<dd>
<dt><code>&#8211;no-relax-branch</code></p>
<dd> The <code>&#8211;relax-branch</code> option enables the relaxation of out-of-range branches. By default <code>&#8211;no-relax-branch</code> is selected, causing any out-of-range branches to produce an error.</p>
<dt><code>-mignore-branch-isa</code></p>
<dd>
<dt><code>-mno-ignore-branch-isa</code></p>
<dd> Ignore branch checks for invalid transitions between <font SIZE="-1">ISA</font> modes. The semantics of branches does not provide for an <font SIZE="-1">ISA</font> mode switch, so in most cases the <font SIZE="-1">ISA</font> mode a branch has been encoded for has to be the same as the <font SIZE="-1">ISA</font> mode of the branch&#8217;s target label. Therefore <font SIZE="-1">GAS</font> has checks implemented that verify in branch assembly that the two <font SIZE="-1">ISA</font> modes match. <code>-mignore-branch-isa</code> disables these checks. By default <code>-mno-ignore-branch-isa</code> is selected, causing any invalid branch requiring a transition between <font SIZE="-1">ISA</font> modes to produce an error.</p>
<dt><code>-mnan=</code><i>encoding</i></p>
<dd> Select between the <font SIZE="-1">IEEE 754-2008</font> (<code>-mnan=2008</code>) or the legacy (<code>-mnan=legacy</code>) NaN encoding format. The latter is the default.</p>
<dt><code>&#8211;emulation=</code><i>name</i></p>
<dd> This option was formerly used to switch between <font SIZE="-1">ELF</font> and <font SIZE="-1">ECOFF</font> output on targets like <font SIZE="-1">IRIX 5</font> that supported both. <font SIZE="-1">MIPS ECOFF</font> support was removed in <font SIZE="-1">GAS 2.24,</font> so the option now serves little purpose. It is retained for backwards compatibility. </p>
<p> The available configuration names are: <code>mipself</code>, <code>mipslelf</code> and <code>mipsbelf</code>. Choosing <code>mipself</code> now has no effect, since the output is always <font SIZE="-1">ELF.</font> <code>mipslelf</code> and <code>mipsbelf</code> select little- and big-endian output respectively, but <code>-EL</code> and <code>-EB</code> are now the preferred options instead.</p>
<dt><code>-nocpp</code></p>
<dd> <code>as</code> ignores this option. It is accepted for compatibility with the native tools.</p>
<dt><code>&#8211;trap</code></p>
<dd>
<dt><code>&#8211;no-trap</code></p>
<dd>
<dt><code>&#8211;break</code></p>
<dd>
<dt><code>&#8211;no-break</code></p>
<dd> Control how to deal with multiplication overflow and division by zero. <code>&#8211;trap</code> or <code>&#8211;no-break</code> (which are synonyms) take a trap exception (and only work for Instruction Set Architecture level 2 and higher); <code>&#8211;break</code> or <code>&#8211;no-trap</code> (also synonyms, and the default) take a break exception.</p>
<dt><code>-n</code></p>
<dd> When this option is used, <code>as</code> will issue a warning every time it generates a nop instruction from a macro.</dl>
<p> The following options are available when as is configured for a LoongArch processor.</p>
<dl>
<dt><code>-fpic</code></p>
<dd>
<dt><code>-fPIC</code></p>
<dd> Generate position-independent code</p>
<dt><code>-fno-pic</code></p>
<dd> Don&#8217;t generate position-independent code (default)</dl>
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
<dt>&quot;-mfpu-freg=<i>FREG</i>&quot;</p>
<dd> Specify a <font SIZE="-1">FPU</font> configuration.</p>
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
<dt>&quot;-mabi=<i>abi</i>&quot;</p>
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
<dd> Enable/Disable Reduced Register configuration (<font SIZE="-1">GPR16</font>) option</p>
<dt>&quot;-m[no-]audio-isa-ext&quot;</p>
<dd> Enable/Disable <font SIZE="-1">AUDIO ISA</font> extension</p>
<dt>&quot;-m[no-]fpu-sp-ext&quot;</p>
<dd> Enable/Disable <font SIZE="-1">FPU SP</font> extension</p>
<dt>&quot;-m[no-]fpu-dp-ext&quot;</p>
<dd> Enable/Disable <font SIZE="-1">FPU DP</font> extension</p>
<dt>&quot;-m[no-]fpu-fma&quot;</p>
<dd> Enable/Disable <font SIZE="-1">FPU</font> fused-multiply-add instructions</p>
<dt>&quot;-mall-ext&quot;</p>
<dd> Turn on all extensions and instructions support</dl>
<p> The following options are available when as is configured for a PowerPC processor.</p>
<dl>
<dt><code>-a32</code></p>
<dd> Generate <font SIZE="-1">ELF32</font> or <font SIZE="-1">XCOFF32.</font></p>
<dt><code>-a64</code></p>
<dd> Generate <font SIZE="-1">ELF64</font> or <font SIZE="-1">XCOFF64.</font></p>
<dt><code>-K </code><font SIZE="-1"><code>PIC</code></font></p>
<dd> Set <font SIZE="-1">EF_PPC_RELOCATABLE_LIB</font> in <font SIZE="-1">ELF</font> flags.</p>
<dt><code>-mpwrx | -mpwr2</code></p>
<dd> Generate code for <font SIZE="-1">POWER/2</font> (<font SIZE="-1">RIOS2</font>).</p>
<dt><code>-mpwr</code></p>
<dd> Generate code for <font SIZE="-1">POWER</font> (<font SIZE="-1">RIOS1</font>)</p>
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
<dt><code>-m750cl, -mgekko, -mbroadway</code></p>
<dd> Generate code for PowerPC 750CL/Gekko/Broadway.</p>
<dt><code>-m821, -m850, -m860</code></p>
<dd> Generate code for PowerPC 821/850/860.</p>
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
<dt><code>-mspe2</code></p>
<dd> Generate code for Freescale <font SIZE="-1">SPE2</font> instructions.</p>
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
<dt><code>-mpower9, -mpwr9</code></p>
<dd> Generate code for Power9 architecture.</p>
<dt><code>-mpower10, -mpwr10</code></p>
<dd> Generate code for Power10 architecture.</p>
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
<p> The following options are available when as is configured for a RISC-V processor.</p>
<dl>
<dt><code>-fpic</code></p>
<dd>
<dt><code>-fPIC</code></p>
<dd> Generate position-independent code</p>
<dt><code>-fno-pic</code></p>
<dd> Don&#8217;t generate position-independent code (default)</p>
<dt><code>-march=ISA</code></p>
<dd> Select the base isa, as specified by <font SIZE="-1">ISA.</font> For example -march=rv32ima. If this option and the architecture attributes aren&#8217;t set, then assembler will check the default configure setting &#8211;with-arch=ISA.</p>
<dt><code>-misa-spec=ISAspec</code></p>
<dd> Select the default isa spec version. If the version of <font SIZE="-1">ISA</font> isn&#8217;t set by -march, then assembler helps to set the version according to the default chosen spec. If this option isn&#8217;t set, then assembler will check the default configure setting &#8211;with-isa-spec=ISAspec.</p>
<dt><code>-mpriv-spec=PRIVspec</code></p>
<dd> Select the privileged spec version. We can decide whether the <font SIZE="-1">CSR</font> is valid or not according to the chosen spec. If this option and the privilege attributes aren&#8217;t set, then assembler will check the default configure setting &#8211;with-priv-spec=PRIVspec.</p>
<dt><code>-mabi=ABI</code></p>
<dd> Selects the <font SIZE="-1">ABI,</font> which is either &#8220;ilp32&#8221; or &#8220;lp64&#8221;, optionally followed by &#8220;f&#8221;, &#8220;d&#8221;, or &#8220;q&#8221; to indicate single-precision, double-precision, or quad-precision floating-point calling convention, or none to indicate the soft-float calling convention. Also, &#8220;ilp32&#8221; can optionally be followed by &#8220;e&#8221; to indicate the <font SIZE="-1">RVE ABI,</font> which is always soft-float.</p>
<dt><code>-mrelax</code></p>
<dd> Take advantage of linker relaxations to reduce the number of instructions required to materialize symbol addresses. (default)</p>
<dt><code>-mno-relax</code></p>
<dd> Don&#8217;t do linker relaxations.</p>
<dt><code>-march-attr</code></p>
<dd> Generate the default contents for the riscv elf attribute section if the .attribute directives are not set. This section is used to record the information that a linker or runtime loader needs to check compatibility. This information includes <font SIZE="-1">ISA</font> string, stack alignment requirement, unaligned memory accesses, and the major, minor and revision version of privileged specification.</p>
<dt><code>-mno-arch-attr</code></p>
<dd> Don&#8217;t generate the default riscv elf attribute section if the .attribute directives are not set.</p>
<dt><code>-mcsr-check</code></p>
<dd> Enable the <font SIZE="-1">CSR</font> checking for the ISA-dependent <font SIZE="-1">CRS</font> and the read-only <font SIZE="-1">CSR.</font> The ISA-dependent <font SIZE="-1">CSR</font> are only valid when the specific <font SIZE="-1">ISA</font> is set. The read-only <font SIZE="-1">CSR</font> can not be written by the <font SIZE="-1">CSR</font> instructions.</p>
<dt><code>-mno-csr-check</code></p>
<dd> Don&#8217;t do <font SIZE="-1">CSR</font> checking.</p>
<dt><code>-mlittle-endian</code></p>
<dd> Generate code for a little endian machine.</p>
<dt><code>-mbig-endian</code></p>
<dd> Generate code for a big endian machine.</dl>
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
<dd> Specify which s390 processor variant is the target, <code>g5</code> (or <code>arch3</code>), <code>g6</code>, <code>z900</code> (or <code>arch5</code>), <code>z990</code> (or <code>arch6</code>), <code>z9-109</code>, <code>z9-ec</code> (or <code>arch7</code>), <code>z10</code> (or <code>arch8</code>), <code>z196</code> (or <code>arch9</code>), <code>zEC12</code> (or <code>arch10</code>), <code>z13</code> (or <code>arch11</code>), <code>z14</code> (or <code>arch12</code>), <code>z15</code> (or <code>arch13</code>), or <code>z16</code> (or <code>arch14</code>).</p>
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
<p> The following option is available when as is configured for a Visium processor.</p>
<dl>
<dt><code>-mtune=</code><i>arch</i></p>
<dd> This option specifies the target architecture. If an attempt is made to assemble an instruction that will not execute on the target architecture, the assembler will issue an error message. </p>
<p> The following names are recognized: <tt>&quot;mcm24&quot;</tt> <tt>&quot;mcm&quot;</tt> <tt>&quot;gr5&quot;</tt> <tt>&quot;gr6&quot;</tt></dl>
<p> The following options are available when as is configured for an Xtensa processor.</p>
<dl>
<dt><code>&#8211;text-section-literals | &#8211;no-text-section-literals</code></p>
<dd> Control the treatment of literal pools. The default is <code>&#8211;no-text-section-literals</code>, which places literals in separate sections in the output file. This allows the literal pool to be placed in a data <font SIZE="-1">RAM/ROM.</font> With <code>&#8211;text-section-literals</code>, the literals are interspersed in the text section in order to keep them as close as possible to their references. This may be necessary for large assembly files, where the literals would otherwise be out of range of the <tt>&quot;L32R&quot;</tt> instructions in the text section. Literals are grouped into pools following <tt>&quot;.literal_position&quot;</tt> directives or preceding <tt>&quot;ENTRY&quot;</tt> instructions. These options only affect literals referenced via PC-relative <tt>&quot;L32R&quot;</tt> instructions; literals for absolute mode <tt>&quot;L32R&quot;</tt> instructions are handled separately.</p>
<dt><code>&#8211;auto-litpools | &#8211;no-auto-litpools</code></p>
<dd> Control the treatment of literal pools. The default is <code>&#8211;no-auto-litpools</code>, which in the absence of <code>&#8211;text-section-literals</code> places literals in separate sections in the output file. This allows the literal pool to be placed in a data <font SIZE="-1">RAM/ROM.</font> With <code>&#8211;auto-litpools</code>, the literals are interspersed in the text section in order to keep them as close as possible to their references, explicit <tt>&quot;.literal_position&quot;</tt> directives are not required. This may be necessary for very large functions, where single literal pool at the beginning of the function may not be reachable by <tt>&quot;L32R&quot;</tt> instructions at the end. These options only affect literals referenced via PC-relative <tt>&quot;L32R&quot;</tt> instructions; literals for absolute mode <tt>&quot;L32R&quot;</tt> instructions are handled separately. When used together with <code>&#8211;text-section-literals</code>, <code>&#8211;auto-litpools</code> takes precedence.</p>
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
<dd> Enable or disable transformation of jump instructions to allow jumps across a greater range of addresses. This option should be used when jump targets can potentially be out of range. In the absence of such jumps this option does not affect code size or performance. The default is <code>&#8211;trampolines</code>.</p>
<dt><code>&#8211;abi-windowed | &#8211;abi-call0</code></p>
<dd> Choose <font SIZE="-1">ABI</font> tag written to the <tt>&quot;.xtensa.info&quot;</tt> section. <font SIZE="-1">ABI</font> tag indicates <font SIZE="-1">ABI</font> of the assembly code. A warning is issued by the linker on an attempt to link object files with inconsistent <font SIZE="-1">ABI</font> tags. Default <font SIZE="-1">ABI</font> is chosen by the Xtensa core configuration.</dl>
<p> The following options are available when as is configured for an Z80 processor. </p>
<p> <tt>@chapter</tt> Z80 Dependent Features</p>
<h3>Command-line Options</h3>
<dl>
<dt><code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i><code>[-</code><i></i><font SIZE="-1"><i>EXT</i></font><i></i><code>&#8230;][+</code><i></i><font SIZE="-1"><i>EXT</i></font><i></i><code>&#8230;]</code></p>
<dd> This option specifies the target processor. The assembler will issue an error message if an attempt is made to assemble an instruction which will not execute on the target processor. The following processor names are recognized: <tt>&quot;z80&quot;</tt>, <tt>&quot;z180&quot;</tt>, <tt>&quot;ez80&quot;</tt>, <tt>&quot;gbz80&quot;</tt>, <tt>&quot;z80n&quot;</tt>, <tt>&quot;r800&quot;</tt>. In addition to the basic instruction set, the assembler can be told to accept some extention mnemonics. For example, <tt>&quot;-march=z180+sli+infc&quot;</tt> extends <i>z180</i> with <i></i><font SIZE="-1"><i>SLI</i></font><i></i> instructions and <i></i><font SIZE="-1"><i>IN F,</i></font><i>(C)</i>. The following extentions are currently supported: <tt>&quot;full&quot;</tt> (all known instructions), <tt>&quot;adl&quot;</tt> (<font SIZE="-1">ADL CPU</font> mode by default, eZ80 only), <tt>&quot;sli&quot;</tt> (instruction known as <i></i><font SIZE="-1"><i>SLI</i></font><i></i>, <i></i><font SIZE="-1"><i>SLL</i></font><i></i> or <i></i><font SIZE="-1"><i>SL1</i></font><i></i>), <tt>&quot;xyhl&quot;</tt> (instructions with halves of index registers: <i></i><font SIZE="-1"><i>IXL</i></font><i></i>, <i></i><font SIZE="-1"><i>IXH</i></font><i></i>, <i></i><font SIZE="-1"><i>IYL</i></font><i></i>, <i></i><font SIZE="-1"><i>IYH</i></font><i></i>), <tt>&quot;xdcb&quot;</tt> (instructions like <i>RotOp (II+d),R</i> and <i>BitOp n,(II+d),R</i>), <tt>&quot;infc&quot;</tt> (instruction <i></i><font SIZE="-1"><i>IN F,</i></font><i>(C)</i> or <i></i><font SIZE="-1"><i>IN</i></font><i> (C)</i>), <tt>&quot;outc0&quot;</tt> (instruction <i></i><font SIZE="-1"><i>OUT</i></font><i> (C),0</i>). Note that rather than extending a basic instruction set, the extention mnemonics starting with <tt>&quot;-&quot;</tt> revoke the respective functionality: <tt>&quot;-march=z80-full+xyhl&quot;</tt> first removes all default extentions and adds support for index registers halves only. </p>
<p> If this option is not specified then <tt>&quot;-march=z80+xyhl+infc&quot;</tt> is assumed.</p>
<dt><code>-local-prefix=</code><i>prefix</i></p>
<dd> Mark all labels with specified prefix as local. But such label can be marked global explicitly in the code. This option do not change default local label prefix <tt>&quot;.L&quot;</tt>, it is just adds new one.</p>
<dt><code>-colonless</code></p>
<dd> Accept colonless labels. All symbols at line begin are treated as labels.</p>
<dt><code>-sdcc</code></p>
<dd> Accept assembler code produced by <font SIZE="-1">SDCC.</font></p>
<dt><code>-fp-s=</code><i></i><font SIZE="-1"><i>FORMAT</i></font><i></i></p>
<dd> Single precision floating point numbers format. Default: ieee754 (32 bit).</p>
<dt><code>-fp-d=</code><i></i><font SIZE="-1"><i>FORMAT</i></font><i></i></p>
<dd> Double precision floating point numbers format. Default: ieee754 (64 bit).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1), and the Info entries for <i>binutils</i> and <i>ld</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
