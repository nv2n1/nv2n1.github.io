---
title: "i686-w64-mingw32-gfortran(1)"
name: "i686-w64-mingw32-gfortran"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-w64-mingw32-gfortran/"
description: "gfortran – GNU Fortran compiler"
---

<h2 class="name">NAME</h2>
<p> gfortran &#8211; GNU Fortran compiler </p>
<h2>SYNOPSIS</h2>
<p> gfortran [<code>-c</code>|<code>-S</code>|<code>-E</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-W</code><i>warn</i>&#8230;]&nbsp;<wbr>[<code>-pedantic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code><i>dir</i>&#8230;]&nbsp;<wbr>[<code>-L</code><i>dir</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code><i>macro</i>[=<i>defn</i>]&#8230;]&nbsp;<wbr>[<code>-U</code><i>macro</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code><i>option</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-m</code><i>machine-option</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr><i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder.</p>
<h2>DESCRIPTION</h2>
<p> The <code>gfortran</code> command supports all the options supported by the <code>gcc</code> command. Only options specific to <font SIZE="-1">GNU</font> Fortran are documented here. </p>
<p> All <font SIZE="-1">GCC</font> and <font SIZE="-1">GNU</font> Fortran options are accepted both by <code>gfortran</code> and by <code>gcc</code> (as well as any other drivers built at the same time, such as <code>g++</code>), since adding <font SIZE="-1">GNU</font> Fortran to the <font SIZE="-1">GCC</font> distribution enables acceptance of <font SIZE="-1">GNU</font> Fortran options by all of the relevant drivers. </p>
<p> In some cases, options have positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.</p>
<h2>OPTIONS</h2>
<p> Here is a summary of all the options specific to <font SIZE="-1">GNU</font> Fortran, grouped by type. Explanations are in the following sections.</p>
<dl>
<dt><i>Fortran Language Options</i></p>
<dd> <code>-fall-intrinsics -fbackslash -fcray-pointer -fd-lines-as-code -fd-lines-as-comments -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -fdollar-ok -ffixed-line-length-</code><i>n</i> <code>-ffixed-line-length-none -ffree-form -ffree-line-length-</code><i>n</i> <code>-ffree-line-length-none -fimplicit-none -finteger-4-integer-8 -fmax-identifier-length -fmodule-private -fno-fixed-form -fno-range-check -fopenmp -freal-4-real-10 -freal-4-real-16 -freal-4-real-8 -freal-8-real-10 -freal-8-real-16 -freal-8-real-4 -std=</code><i>std</i></p>
<dt><i>Preprocessing Options</i></p>
<dd> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-A</code><i>question</i><code>=</code><i>answer</i> <code>-C -CC -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-H -P -U</code><i>macro</i> <code>-cpp -dD -dI -dM -dN -dU -fworking-directory -imultilib</code> <i>dir</i> <code>-iprefix</code> <i>file</i> <code>-iquote -isysroot</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-nocpp -nostdinc -undef</code></p>
<dt><i>Error and Warning Options</i></p>
<dd> <code>-Waliasing -Wall -Wampersand -Warray-bounds -Wc-binding-type -Wcharacter-truncation -Wconversion -Wfunction-elimination -Wimplicit-interface -Wimplicit-procedure -Wintrinsic-shadow -Wintrinsics-std -Wline-truncation -Wno-align-commons -Wno-tabs -Wreal-q-constant -Wsurprising -Wunderflow -Wunused-parameter -Wrealloc-lhs -Wrealloc-lhs-all -Wtarget-lifetime -fmax-errors=</code><i>n</i> <code>-fsyntax-only -pedantic -pedantic-errors</code></p>
<dt><i>Debugging Options</i></p>
<dd> <code>-fbacktrace -fdump-fortran-optimized -fdump-fortran-original -fdump-parse-tree -ffpe-trap=</code><i>list</i> <code>-ffpe-summary=</code><i>list</i></p>
<dt><i>Directory Options</i></p>
<dd> <code>-I</code><i>dir</i> <code>-J</code><i>dir</i> <code>-fintrinsic-modules-path</code> <i>dir</i></p>
<dt><i>Link Options</i></p>
<dd> <code>-static-libgfortran</code></p>
<dt><i>Runtime Options</i></p>
<dd> <code>-fconvert=</code><i>conversion</i> <code>-fmax-subrecord-length=</code><i>length</i> <code>-frecord-marker=</code><i>length</i> <code>-fsign-zero</code></p>
<dt><i>Code Generation Options</i></p>
<dd> <code>-faggressive-function-elimination -fblas-matmul-limit=</code><i>n</i> <code>-fbounds-check -fcheck-array-temporaries -fcheck=</code><i>&lt;all|array-temps|bounds|do|mem|pointer|recursion&gt;</i> <code>-fcoarray=</code><i>&lt;none|single|lib&gt;</i> <code>-fexternal-blas -ff2c -ffrontend-optimize -finit-character=</code><i>n</i> <code>-finit-integer=</code><i>n</i> <code>-finit-local-zero -finit-logical=</code><i>&lt;true|false&gt;</i> <code>-finit-real=</code><i>&lt;zero|inf|-inf|nan|snan&gt;</i> <code>-fmax-array-constructor=</code><i>n</i> <code>-fmax-stack-var-size=</code><i>n</i> <code>-fno-align-commons -fno-automatic -fno-protect-parens -fno-underscoring -fsecond-underscore -fpack-derived -frealloc-lhs -frecursive -frepack-arrays -fshort-enums -fstack-arrays</code></dl>
<h3>Options controlling Fortran dialect</h3>
<p> The following options control the details of the Fortran dialect accepted by the compiler:</p>
<dl>
<dt><code>-ffree-form</code></p>
<dd>
<dt><code>-ffixed-form</code></p>
<dd> Specify the layout used by the source file. The free form layout was introduced in Fortran 90. Fixed form was traditionally used in older Fortran programs. When neither option is specified, the source form is determined by the file extension.</p>
<dt><code>-fall-intrinsics</code></p>
<dd> This option causes all intrinsic procedures (including the GNU-specific extensions) to be accepted. This can be useful with <code>-std=f95</code> to force standard-compliance but get access to the full range of intrinsics available with <code>gfortran</code>. As a consequence, <code>-Wintrinsics-std</code> will be ignored and no user-defined procedure with the same name as any intrinsic will be called except when it is explicitly declared <tt>&quot;EXTERNAL&quot;</tt>.</p>
<dt><code>-fd-lines-as-code</code></p>
<dd>
<dt><code>-fd-lines-as-comments</code></p>
<dd> Enable special treatment for lines beginning with <tt>&quot;d&quot;</tt> or <tt>&quot;D&quot;</tt> in fixed form sources. If the <code>-fd-lines-as-code</code> option is given they are treated as if the first column contained a blank. If the <code>-fd-lines-as-comments</code> option is given, they are treated as comment lines.</p>
<dt><code>-fdollar-ok</code></p>
<dd> Allow <code>$</code> as a valid non-first character in a symbol name. Symbols that start with <code>$</code> are rejected since it is unclear which rules to apply to implicit typing as different vendors implement different rules. Using <code>$</code> in <tt>&quot;IMPLICIT&quot;</tt> statements is also rejected.</p>
<dt><code>-fbackslash</code></p>
<dd> Change the interpretation of backslashes in string literals from a single backslash character to &#8220;C-style&#8221; escape characters. The following combinations are expanded <tt>&quot;&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;
&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;	&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;\&quot;</tt>, and <tt>&quot;
