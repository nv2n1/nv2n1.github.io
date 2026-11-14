---
title: "f2c(1)"
name: "f2c"
section: "1"
letter: "f"
url: "/docs/linux/man/1-f2c/"
description: "f2c – Convert Fortran 77 to C or C++"
---

<h2 class="name">NAME</h2>
<p> f2c &#8211; Convert Fortran 77 to C or C++ </p>
<h2>SYNOPSIS</h2>
<p> <code>f2c</code> [ <i>option &#8230;</i> ] <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>F2c</i> converts Fortran 77 source code in <i>files</i> with names ending in or to C (or C++) source files in the current directory, with substituted for the final or `.F&#8217;. If no Fortran files are named, <i>f2c</i> reads Fortran from standard input and writes C on standard output. <i>File</i> names that end with or are taken to be prototype files, as produced by option `-P&#8217;, and are read first. </p>
<p> The following options have the same meaning as in <i><a href="/docs/linux/man/1-f77/">f77</a></i>(1).</p>
<dl>
<dt><code>-C</code></p>
<dd> Compile code to check that subscripts are within declared array bounds.</p>
<dt><code>-I2</code></p>
<dd> Render INTEGER and LOGICAL as short, INTEGER*4 as long int. Assume the default <i>libF77</i> and <i>libI77</i>: allow only INTEGER*4 (and no LOGICAL) variables in INQUIREs. Option confirms the default rendering of INTEGER as long int.</p>
<dt><code>-I</code><i>dir</i></p>
<dd> Look for a non-absolute include file first in the directory of the current input file, then in directories specified by <tt>-I</tt> options (one directory per option). Options <tt>-I2</tt> and <tt>-I4</tt> have precedence, so, e.g., a directory named <tt>2</tt> should be specified by <tt>-I./2</tt> .</p>
<dt><code>-onetrip</code></p>
<dd> Compile DO loops that are performed at least once if reached. (Fortran 77 DO loops are not performed at all if the upper limit is smaller than the lower limit.)</p>
<dt><code>-U</code></p>
<dd> Honor the case of variable and external names. Fortran keywords must be in <i>lower</i> case.</p>
<dt><code>-u</code></p>
<dd> Make the default type of a variable `undefined&#8217; rather than using the default Fortran rules.</p>
<dt><code>-w</code></p>
<dd> Suppress all warning messages, or, if the option is `-w66&#8242;, just Fortran 66 compatibility warnings.</dl>
<p> The following options are peculiar to <i>f2c</i>.</p>
<dl>
<dt><code>-A</code></p>
<dd> Produce <font SIZE="-1">ANSI</font> C (default, starting 20020621). For old-style C, use option <tt>-K</tt>.</p>
<dt><code>-a</code></p>
<dd> Make local variables automatic rather than static unless they appear in a <font SIZE="-1">DATA, EQUIVALENCE, NAMELIST,</font> or <font SIZE="-1">SAVE</font> statement.</p>
<dt><code>-C++</code></p>
<dd> Output C++ code.</p>
<dt><code>-c</code></p>
<dd> Include original Fortran source as comments.</p>
<dt><code>-cd</code></p>
<dd> Do not recognize cdabs, cdcos, cdexp, cdlog, cdsin, and cdsqrt as synonyms for the double complex intrinsics zabs, zcos, zexp, zlog, zsin, and zsqrt, respectively, nor dreal as a synonym for dble.</p>
<dt><code>-d</code><i>dir</i></p>
<dd> Write files in directory <i>dir</i> instead of the current directory.</p>
<dt><code>-E</code></p>
<dd> Declare uninitialized <font SIZE="-1">COMMON</font> to be <code>Extern</code> (overridably defined in as <code>extern).</code></p>
<dt><code>-ec</code></p>
<dd> Place uninitialized <font SIZE="-1">COMMON</font> blocks in separate files: <code>COMMON /ABC/</code> appears in file <code>abc_com.c</code>. Option `-e1c&#8217; bundles the separate files into the output file, with comments that give an unbundling <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) script.</p>
<dt><code>-ext</code></p>
<dd> Complain about <i><a href="/docs/linux/man/1-f77/">f77</a></i>(1) extensions.</p>
<dt><code>-f</code></p>
<dd> Assume free-format input: accept text after column 72 and do not pad fixed-format lines shorter than 72 characters with blanks.</p>
<dt><code>-72</code></p>
<dd> Treat text appearing after column 72 as an error.</p>
<dt><code>-g</code></p>
<dd> Include original Fortran line numbers in <tt>#line</tt> lines.</p>
<dt><code>-h</code></p>
<dd> Emulate Fortran 66&#8217;s treatment of Hollerith: try to align character strings on word (or, if the option is `-hd&#8217;, on double-word) boundaries.</p>
<dt><code>-i2</code></p>
<dd> Similar to <code>-I2</code>, but assume a modified <i>libF77</i> and <i>libI77</i> (compiled with <code>-Df2c_i2</code>), so <font SIZE="-1">INTEGER</font> and <font SIZE="-1">LOGICAL</font> variables may be assigned by <font SIZE="-1">INQUIRE</font> and array lengths are stored in short ints.</p>
<dt><code>-i90</code></p>
<dd> Do not recognize the Fortran 90 bit-manipulation intrinsics btest, iand, ibclr, ibits, ibset, ieor, ior, ishft, and ishftc.</p>
<dt><code>-kr</code></p>
<dd> Use temporary values to enforce Fortran expression evaluation where K&amp;R (first edition) parenthesization rules allow rearrangement. If the option is `-krd&#8217;, use double precision temporaries even for single-precision operands.</p>
<dt><code>-P</code></p>
<dd> Write a <i>file</i><code>.P</code> of ANSI (or C++) prototypes for definitions in each input <i>file</i><code>.f</code> or <i>file</i><code>.F</code><i>.</i> When reading Fortran from standard input, write prototypes at the beginning of standard output. Option <code>-Ps</code> implies <code>-P</code> and gives exit status 4 if rerunning <i>f2c</i> may change prototypes or declarations.</p>
<dt><code>-p</code></p>
<dd> Supply preprocessor definitions to make common-block members look like local variables.</p>
<dt><code>-R</code></p>
<dd> Do not promote <font SIZE="-1">REAL</font> functions and operations to <font SIZE="-1">DOUBLE PRECISION.</font> Option confirms the default, which imitates <i>f77</i>.</p>
<dt><code>-r</code></p>
<dd> Cast REAL arguments of intrinsic functions and values of REAL functions (including intrinsics) to REAL.</p>
<dt><code>-r8</code></p>
<dd> Promote <font SIZE="-1">REAL</font> to <font SIZE="-1">DOUBLE PRECISION, COMPLEX</font> to <font SIZE="-1">DOUBLE COMPLEX.</font></p>
<dt><code>-s</code></p>
<dd> Preserve multidimensional subscripts. Suppressed by option .</p>
<dt><code>-T</code><i>dir</i></p>
<dd> Put temporary files in directory <i>dir.</i></p>
<dt><code>-trapuv</code></p>
<dd> Dynamically initialize local variables, except those appearing in <font SIZE="-1">SAVE</font> or <font SIZE="-1">DATA</font> statements, with values that may help find references to uninitialized variables. For example, with IEEE arithmetic, initialize local floating-point variables to signaling NaNs.</p>
<dt><code>-w8</code></p>
<dd> Suppress warnings when <font SIZE="-1">COMMON</font> or <font SIZE="-1">EQUIVALENCE</font> forces odd-word alignment of doubles.</p>
<dt><code>-W</code><i>n</i></p>
<dd> Assume <i>n</i> characters/word (default 4) when initializing numeric variables with character data.</p>
<dt><code>-z</code></p>
<dd> Do not implicitly recognize <font SIZE="-1">DOUBLE COMPLEX.</font></p>
<dt><code>-!bs</code></p>
<dd> Do not recognize <i>b</i>ack<i>s</i>lash escapes (\&quot;, \&#8217;, 
