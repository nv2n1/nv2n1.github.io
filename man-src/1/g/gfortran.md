---
title: "gfortran(1)"
name: "gfortran"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfortran/"
description: "gfortran – GNU Fortran compiler"
---

<h2 class="name">NAME</h2>
<p> gfortran &#8211; GNU Fortran compiler </p>
<h2>SYNOPSIS</h2>
<p> gfortran [<code>-c</code>|<code>-S</code>|<code>-E</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>]&nbsp;[<code>-pg</code>]&nbsp;[<code>-O</code><i>level</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-W</code><i>warn</i>&#8230;]&nbsp;[<code>-pedantic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-I</code><i>dir</i>&#8230;]&nbsp;[<code>-L</code><i>dir</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-D</code><i>macro</i>[=<i>defn</i>]&#8230;]&nbsp;[<code>-U</code><i>macro</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code><i>option</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m</code><i>machine-option</i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-o</code>&nbsp;<i>outfile</i>]&nbsp;<i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder.</p>
<h2>DESCRIPTION</h2>
<p> The <code>gfortran</code> command supports all the options supported by the <code>gcc</code> command. Only options specific to <font SIZE="-1">GNU</font> Fortran are documented here. </p>
<p> All <font SIZE="-1">GCC</font> and <font SIZE="-1">GNU</font> Fortran options are accepted both by <code>gfortran</code> and by <code>gcc</code> (as well as any other drivers built at the same time, such as <code>g++</code>), since adding <font SIZE="-1">GNU</font> Fortran to the <font SIZE="-1">GCC</font> distribution enables acceptance of <font SIZE="-1">GNU</font> Fortran options by all of the relevant drivers. </p>
<p> In some cases, options have positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.</p>
<h2>OPTIONS</h2>
<p> Here is a summary of all the options specific to <font SIZE="-1">GNU</font> Fortran, grouped by type. Explanations are in the following sections.</p>
<dl>
<dt><i>Fortran Language Options</i></p>
<dd> <code>-fall-intrinsics -fallow-argument-mismatch -fallow-invalid-boz -fbackslash -fcray-pointer -fd-lines-as-code -fd-lines-as-comments -fdec -fdec-char-conversions -fdec-structure -fdec-intrinsic-ints -fdec-static -fdec-math -fdec-include -fdec-format-defaults -fdec-blank-format-item -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -fdefault-real-10 -fdefault-real-16 -fdollar-ok -ffixed-line-length-</code><i>n</i> <code>-ffixed-line-length-none -fpad-source -ffree-form -ffree-line-length-</code><i>n</i> <code>-ffree-line-length-none -fimplicit-none -finteger-4-integer-8 -fmax-identifier-length -fmodule-private -ffixed-form -fno-range-check -fopenacc -fopenmp -freal-4-real-10 -freal-4-real-16 -freal-4-real-8 -freal-8-real-10 -freal-8-real-16 -freal-8-real-4 -std=</code><i>std</i> <code>-ftest-forall-temp</code></p>
<dt><i>Preprocessing Options</i></p>
<dd> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-A</code><i>question</i><code>=</code><i>answer</i> <code>-C -CC -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-H -P -U</code><i>macro</i> <code>-cpp -dD -dI -dM -dN -dU -fworking-directory -imultilib</code> <i>dir</i> <code>-iprefix</code> <i>file</i> <code>-iquote -isysroot</code> <i>dir</i> <code>-isystem</code> <i>dir</i> <code>-nocpp -nostdinc -undef</code></p>
<dt><i>Error and Warning Options</i></p>
<dd> <code>-Waliasing -Wall -Wampersand -Warray-bounds -Wc-binding-type -Wcharacter-truncation -Wconversion -Wdo-subscript -Wfunction-elimination -Wimplicit-interface -Wimplicit-procedure -Wintrinsic-shadow -Wuse-without-only -Wintrinsics-std -Wline-truncation -Wno-align-commons -Wno-overwrite-recursive -Wno-tabs -Wreal-q-constant -Wsurprising -Wunderflow -Wunused-parameter -Wrealloc-lhs -Wrealloc-lhs-all -Wfrontend-loop-interchange -Wtarget-lifetime -fmax-errors=</code><i>n</i> <code>-fsyntax-only -pedantic -pedantic-errors</code></p>
<dt><i>Debugging Options</i></p>
<dd> <code>-fbacktrace -fdump-fortran-optimized -fdump-fortran-original -fdebug-aux-vars -fdump-fortran-global -fdump-parse-tree -ffpe-trap=</code><i>list</i> <code>-ffpe-summary=</code><i>list</i></p>
<dt><i>Directory Options</i></p>
<dd> <code>-I</code><i>dir</i> <code>-J</code><i>dir</i> <code>-fintrinsic-modules-path</code> <i>dir</i></p>
<dt><i>Link Options</i></p>
<dd> <code>-static-libgfortran</code></p>
<dt><i>Runtime Options</i></p>
<dd> <code>-fconvert=</code><i>conversion</i> <code>-fmax-subrecord-length=</code><i>length</i> <code>-frecord-marker=</code><i>length</i> <code>-fsign-zero</code></p>
<dt><i>Interoperability Options</i></p>
<dd> <code>-fc-prototypes -fc-prototypes-external</code></p>
<dt><i>Code Generation Options</i></p>
<dd> <code>-faggressive-function-elimination -fblas-matmul-limit=</code><i>n</i> <code>-fbounds-check -ftail-call-workaround -ftail-call-workaround=</code><i>n</i> <code>-fcheck-array-temporaries -fcheck=</code><i>&lt;all|array-temps|bits|bounds|do|mem|pointer|recursion&gt;</i> <code>-fcoarray=</code><i>&lt;none|single|lib&gt;</i> <code>-fexternal-blas -ff2c -ffrontend-loop-interchange -ffrontend-optimize -finit-character=</code><i>n</i> <code>-finit-integer=</code><i>n</i> <code>-finit-local-zero -finit-derived -finit-logical=</code><i>&lt;true|false&gt;</i> <code>-finit-real=</code><i>&lt;zero|inf|-inf|nan|snan&gt;</i> <code>-finline-matmul-limit=</code><i>n</i> <code>-finline-arg-packing -fmax-array-constructor=</code><i>n</i> <code>-fmax-stack-var-size=</code><i>n</i> <code>-fno-align-commons -fno-automatic -fno-protect-parens -fno-underscoring -fsecond-underscore -fpack-derived -frealloc-lhs -frecursive -frepack-arrays -fshort-enums -fstack-arrays</code></dl>
<h3>Options controlling Fortran dialect</h3>
<p> The following options control the details of the Fortran dialect accepted by the compiler:</p>
<dl>
<dt><code>-ffree-form</code></p>
<dd>
<dt><code>-ffixed-form</code></p>
<dd> Specify the layout used by the source file. The free form layout was introduced in Fortran 90. Fixed form was traditionally used in older Fortran programs. When neither option is specified, the source form is determined by the file extension.</p>
<dt><code>-fall-intrinsics</code></p>
<dd> This option causes all intrinsic procedures (including the GNU-specific extensions) to be accepted. This can be useful with <code>-std=f95</code> to force standard-compliance but get access to the full range of intrinsics available with <code>gfortran</code>. As a consequence, <code>-Wintrinsics-std</code> will be ignored and no user-defined procedure with the same name as any intrinsic will be called except when it is explicitly declared <tt>&quot;EXTERNAL&quot;</tt>.</p>
<dt><code>-fallow-argument-mismatch</code></p>
<dd> Some code contains calls to external procedures with mismatches between the calls and the procedure definition, or with mismatches between different calls. Such code is non-conforming, and will usually be flagged with an error. This options degrades the error to a warning, which can only be disabled by disabling all warnings via <code>-w</code>. Only a single occurrence per argument is flagged by this warning. <code>-fallow-argument-mismatch</code> is implied by <code>-std=legacy</code>. </p>
<p> Using this option is <i>strongly</i> discouraged. It is possible to provide standard-conforming code which allows different types of arguments by using an explicit interface and <tt>TYPE(*)</tt>.</p>
<dt><code>-fallow-invalid-boz</code></p>
<dd> A <font SIZE="-1">BOZ</font> literal constant can occur in a limited number of contexts in standard conforming Fortran. This option degrades an error condition to a warning, and allows a <font SIZE="-1">BOZ</font> literal constant to appear where the Fortran standard would otherwise prohibit its use.</p>
<dt><code>-fd-lines-as-code</code></p>
<dd>
<dt><code>-fd-lines-as-comments</code></p>
<dd> Enable special treatment for lines beginning with <tt>&quot;d&quot;</tt> or <tt>&quot;D&quot;</tt> in fixed form sources. If the <code>-fd-lines-as-code</code> option is given they are treated as if the first column contained a blank. If the <code>-fd-lines-as-comments</code> option is given, they are treated as comment lines.</p>
<dt><code>-fdec</code></p>
<dd> <font SIZE="-1">DEC</font> compatibility mode. Enables extensions and other features that mimic the default behavior of older compilers (such as <font SIZE="-1">DEC</font>). These features are non-standard and should be avoided at all costs. For details on <font SIZE="-1">GNU</font> Fortran&#8217;s implementation of these extensions see the full documentation. </p>
<p> Other flags enabled by this switch are: <code>-fdollar-ok</code> <code>-fcray-pointer</code> <code>-fdec-char-conversions</code> <code>-fdec-structure</code> <code>-fdec-intrinsic-ints</code> <code>-fdec-static</code> <code>-fdec-math</code> <code>-fdec-include</code> <code>-fdec-blank-format-item</code> <code>-fdec-format-defaults</code> </p>
<p> If <code>-fd-lines-as-code</code>/<code>-fd-lines-as-comments</code> are unset, then <code>-fdec</code> also sets <code>-fd-lines-as-comments</code>.</p>
<dt><code>-fdec-char-conversions</code></p>
<dd> Enable the use of character literals in assignments and <tt>&quot;DATA&quot;</tt> statements for non-character variables.</p>
<dt><code>-fdec-structure</code></p>
<dd> Enable <font SIZE="-1">DEC</font> <tt>&quot;STRUCTURE&quot;</tt> and <tt>&quot;RECORD&quot;</tt> as well as <tt>&quot;UNION&quot;</tt>, <tt>&quot;MAP&quot;</tt>, and dot (&#8216;.&#8217;) as a member separator (in addition to &#8216;%&#8217;). This is provided for compatibility only; Fortran 90 derived types should be used instead where possible.</p>
<dt><code>-fdec-intrinsic-ints</code></p>
<dd> Enable B/I/J/K kind variants of existing integer functions (e.g. <font SIZE="-1">BIAND, IIAND, JIAND,</font> etc&#8230;). For a complete list of intrinsics see the full documentation.</p>
<dt><code>-fdec-math</code></p>
<dd> Enable legacy math intrinsics such as <font SIZE="-1">COTAN</font> and degree-valued trigonometric functions (e.g. <font SIZE="-1">TAND, ATAND,</font> etc&#8230;) for compatability with older code.</p>
<dt><code>-fdec-static</code></p>
<dd> Enable DEC-style <font SIZE="-1">STATIC</font> and <font SIZE="-1">AUTOMATIC</font> attributes to explicitly specify the storage of variables and other objects.</p>
<dt><code>-fdec-include</code></p>
<dd> Enable parsing of <font SIZE="-1">INCLUDE</font> as a statement in addition to parsing it as <font SIZE="-1">INCLUDE</font> line. When parsed as <font SIZE="-1">INCLUDE</font> statement, <font SIZE="-1">INCLUDE</font> does not have to be on a single line and can use line continuations.</p>
<dt><code>-fdec-format-defaults</code></p>
<dd> Enable format specifiers F, G and I to be used without width specifiers, default widths will be used instead.</p>
<dt><code>-fdec-blank-format-item</code></p>
<dd> Enable a blank format item at the end of a format specification i.e. nothing following the final comma.</p>
<dt><code>-fdollar-ok</code></p>
<dd> Allow <code>$</code> as a valid non-first character in a symbol name. Symbols that start with <code>$</code> are rejected since it is unclear which rules to apply to implicit typing as different vendors implement different rules. Using <code>$</code> in <tt>&quot;IMPLICIT&quot;</tt> statements is also rejected.</p>
<dt><code>-fbackslash</code></p>
<dd> Change the interpretation of backslashes in string literals from a single backslash character to &#8220;C-style&#8221; escape characters. The following combinations are expanded <tt>&quot;&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;
&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;	&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;\&quot;</tt>, and <tt>&quot;
