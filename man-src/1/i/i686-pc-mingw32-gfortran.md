---
title: "i686-pc-mingw32-gfortran(1)"
name: "i686-pc-mingw32-gfortran"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-pc-mingw32-gfortran/"
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
<dd> <code>-fall-intrinsics -ffree-form -fno-fixed-form -fdollar-ok -fimplicit-none -fmax-identifier-length -std=</code><i>std</i> <code>-fd-lines-as-code -fd-lines-as-comments -ffixed-line-length-</code><i>n</i> <code>-ffixed-line-length-none -ffree-line-length-</code><i>n</i> <code>-ffree-line-length-none -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -fcray-pointer -fopenmp -fno-range-check -fbackslash -fmodule-private</code></p>
<dt><i>Preprocessing Options</i></p>
<dd> <code>-cpp -dD -dI -dM -dN -dU -fworking-directory -imultilib</code> <i>dir</i> <code>-iprefix</code> <i>file</i> <code>-isysroot</code> <i>dir</i> <code>-iquote -isystem</code> <i>dir</i> <code>-nocpp -nostdinc -undef -A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -CC -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-U</code><i>macro</i> <code>-H -P</code></p>
<dt><i>Error and Warning Options</i></p>
<dd> <code>-fmax-errors=</code><i>n</i> <code>-fsyntax-only -pedantic -pedantic-errors -Wall -Waliasing -Wampersand -Warray-bounds -Wcharacter-truncation -Wconversion -Wimplicit-interface -Wline-truncation -Wintrinsics-std -Wsurprising -Wno-tabs -Wunderflow -Wunused-parameter -Wintrinsics-shadow -Wno-align-commons</code></p>
<dt><i>Debugging Options</i></p>
<dd> <code>-fdump-parse-tree -ffpe-trap=</code><i>list</i> <code>-fdump-core -fbacktrace</code></p>
<dt><i>Directory Options</i></p>
<dd> <code>-I</code><i>dir</i> <code>-J</code><i>dir</i> <code>-M</code><i>dir</i> <code>-fintrinsic-modules-path</code> <i>dir</i></p>
<dt><i>Link Options</i></p>
<dd> <code>-static-libgfortran</code></p>
<dt><i>Runtime Options</i></p>
<dd> <code>-fconvert=</code><i>conversion</i> <code>-fno-range-check -frecord-marker=</code><i>length</i> <code>-fmax-subrecord-length=</code><i>length</i> <code>-fsign-zero</code></p>
<dt><i>Code Generation Options</i></p>
<dd> <code>-fno-automatic -ff2c -fno-underscoring -fsecond-underscore -fbounds-check -fcheck-array-temporaries -fmax-array-constructor =</code><i>n</i> <code>-fmax-stack-var-size=</code><i>n</i> <code>-fpack-derived -frepack-arrays -fshort-enums -fexternal-blas -fblas-matmul-limit=</code><i>n</i> <code>-frecursive -finit-local-zero -finit-integer=</code><i>n</i> <code>-finit-real=</code><i>&lt;zero|inf|-inf|nan&gt;</i> <code>-finit-logical=</code><i>&lt;true|false&gt;</i> <code>-finit-character=</code><i>n</i> <code>-fno-align-commons</code></dl>
<h2>Options controlling Fortran dialect</h2>
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
<dt><code>-fdefault-double-8</code></p>
<dd> Set the <tt>&quot;DOUBLE PRECISION&quot;</tt> type to an 8 byte wide type. If <code>-fdefault-real-8</code> is given, <tt>&quot;DOUBLE PRECISION&quot;</tt> would instead be promoted to 16 bytes if possible, and <code>-fdefault-double-8</code> can be used to prevent this. The kind of real constants like <tt>&quot;1.d0&quot;</tt> will not be changed by <code>-fdefault-real-8</code> though, so also <code>-fdefault-double-8</code> does not affect it.</p>
<dt><code>-fdefault-integer-8</code></p>
<dd> Set the default integer and logical types to an 8 byte wide type. Do nothing if this is already the default. This option also affects the kind of integer constants like <tt>42</tt>.</p>
<dt><code>-fdefault-real-8</code></p>
<dd> Set the default real type to an 8 byte wide type. Do nothing if this is already the default. This option also affects the kind of non-double real constants like <tt>1.0</tt>, and does promote the default width of <tt>&quot;DOUBLE PRECISION&quot;</tt> to 16 bytes if possible, unless <tt>&quot;-fdefault-double-8&quot;</tt> is given, too.</p>
<dt><code>-fdollar-ok</code></p>
<dd> Allow <code>$</code> as a valid character in a symbol name.</p>
<dt><code>-fbackslash</code></p>
<dd> Change the interpretation of backslashes in string literals from a single backslash character to &#8220;C-style&#8221; escape characters. The following combinations are expanded <tt>&quot;&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;
&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;	&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;\&quot;</tt>, and <tt>&quot;
