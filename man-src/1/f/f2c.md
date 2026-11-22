---

title: "f2c(1)"
name: "f2c"
section: "1"
letter: "f"
url: "/docs/linux/man/1-f2c/"
description: "f2c – Convert Fortran 77 to C or C++"
---

<p> f2c - Convert Fortran 77 to C or C++ </p>
<h2>SYNOPSIS</h2>
<p> <code>f2c</code> [ <i>option ...</i> ] <i>file ...</i>  </p>
<h2>DESCRIPTION</h2>
<p> <i>F2c</i> converts Fortran 77 source code in <i>files</i> with names ending in or to C (or C++) source files in the current directory, with substituted for the final or `.F&#8217;. If no Fortran files are named, <i>f2c</i> reads Fortran from standard input and writes C on standard output. <i>File</i> names that end with or are taken to be prototype files, as produced by option `-P&#8217;, and are read first. </p>
<p> The following options have the same meaning as in <i><a href="/docs/linux/man/1-f77/">f77</a></i>(1). </p>
<dl>
<dt><code>-C</code></dt>
<dd> <p> Compile code to check that subscripts are within declared array bounds. </p>
 </dd>
<dt><code>-I2</code></dt>
<dd> <p> Render INTEGER and LOGICAL as short, INTEGER*4 as long int. Assume the default <i>libF77</i> and <i>libI77</i>: allow only INTEGER*4 (and no LOGICAL) variables in INQUIREs. Option confirms the default rendering of INTEGER as long int. </p>
 </dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> <p> Look for a non-absolute include file first in the directory of the current input file, then in directories specified by <code>-I</code> options (one directory per option). Options <code>-I2</code> and <code>-I4</code> have precedence, so, e.g., a directory named <code>2</code> should be specified by <code>-I./2</code> . </p>
 </dd>
<dt><code>-onetrip</code></dt>
<dd> <p> Compile DO loops that are performed at least once if reached. (Fortran 77 DO loops are not performed at all if the upper limit is smaller than the lower limit.) </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> Honor the case of variable and external names. Fortran keywords must be in <i>lower</i> case. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Make the default type of a variable `undefined&#8217; rather than using the default Fortran rules. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Suppress all warning messages, or, if the option is `-w66&#8217;, just Fortran 66 compatibility warnings. </p>
 </dd></dl>
<p> The following options are peculiar to <i>f2c</i>. </p>
<dl>
<dt><code>-A</code></dt>
<dd> <p> Produce ANSI C (default, starting 20020621). For old-style C, use option <code>-K</code>. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Make local variables automatic rather than static unless they appear in a DATA, EQUIVALENCE, NAMELIST, or SAVE statement. </p>
 </dd>
<dt><code>-C++</code></dt>
<dd> <p> Output C++ code. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Include original Fortran source as comments. </p>
 </dd>
<dt><code>-cd</code></dt>
<dd> <p> Do not recognize cdabs, cdcos, cdexp, cdlog, cdsin, and cdsqrt as synonyms for the double complex intrinsics zabs, zcos, zexp, zlog, zsin, and zsqrt, respectively, nor dreal as a synonym for dble. </p>
 </dd>
<dt><code>-d</code><i>dir</i></dt>
<dd> <p> Write files in directory <i>dir</i> instead of the current directory. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Declare uninitialized COMMON to be <code>Extern</code> (overridably defined in as <code>extern).</code> </p>
 </dd>
<dt><code>-ec</code></dt>
<dd> <p> Place uninitialized COMMON blocks in separate files: <code>COMMON /ABC/</code> appears in file <code>abc_com.c</code>. Option `-e1c&#8217; bundles the separate files into the output file, with comments that give an unbundling <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) script. </p>
 </dd>
<dt><code>-ext</code></dt>
<dd> <p> Complain about <i><a href="/docs/linux/man/1-f77/">f77</a></i>(1) extensions. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Assume free-format input: accept text after column 72 and do not pad fixed-format lines shorter than 72 characters with blanks. </p>
 </dd>
<dt><code>-72</code></dt>
<dd> <p> Treat text appearing after column 72 as an error. </p>
 </dd>
<dt><code>-g</code></dt>
<dd> <p> Include original Fortran line numbers in <code>#line</code> lines. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Emulate Fortran 66&#8217;s treatment of Hollerith: try to align character strings on word (or, if the option is `-hd&#8217;, on double-word) boundaries. </p>
 </dd>
<dt><code>-i2</code></dt>
<dd> <p> Similar to <code>-I2</code>, but assume a modified <i>libF77</i> and <i>libI77</i> (compiled with <code>-Df2c_i2</code>), so INTEGER and LOGICAL variables may be assigned by INQUIRE and array lengths are stored in short ints. </p>
 </dd>
<dt><code>-i90</code></dt>
<dd> <p> Do not recognize the Fortran 90 bit-manipulation intrinsics btest, iand, ibclr, ibits, ibset, ieor, ior, ishft, and ishftc. </p>
 </dd>
<dt><code>-kr</code></dt>
<dd> <p> Use temporary values to enforce Fortran expression evaluation where K&amp;R (first edition) parenthesization rules allow rearrangement. If the option is `-krd&#8217;, use double precision temporaries even for single-precision operands. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Write a <i>file</i><code>.P</code> of ANSI (or C++) prototypes for definitions in each input <i>file</i><code>.f</code> or <i>file</i><code>.F</code><i>.</i> When reading Fortran from standard input, write prototypes at the beginning of standard output. Option <code>-Ps</code> implies <code>-P</code> and gives exit status 4 if rerunning <i>f2c</i> may change prototypes or declarations. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Supply preprocessor definitions to make common-block members look like local variables. </p>
 </dd>
<dt><code>-R</code></dt>
<dd> <p> Do not promote REAL functions and operations to DOUBLE PRECISION. Option confirms the default, which imitates <i>f77</i>. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Cast REAL arguments of intrinsic functions and values of REAL functions (including intrinsics) to REAL. </p>
 </dd>
<dt><code>-r8</code></dt>
<dd> <p> Promote REAL to DOUBLE PRECISION, COMPLEX to DOUBLE COMPLEX. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Preserve multidimensional subscripts. Suppressed by option . </p>
 </dd>
<dt><code>-T</code><i>dir</i></dt>
<dd> <p> Put temporary files in directory <i>dir.</i> </p>
 </dd>
<dt><code>-trapuv</code></dt>
<dd> <p> Dynamically initialize local variables, except those appearing in SAVE or DATA statements, with values that may help find references to uninitialized variables. For example, with IEEE arithmetic, initialize local floating-point variables to signaling NaNs. </p>
 </dd>
<dt><code>-w8</code></dt>
<dd> <p> Suppress warnings when COMMON or EQUIVALENCE forces odd-word alignment of doubles. </p>
 </dd>
<dt><code>-W</code><i>n</i></dt>
<dd> <p> Assume <i>n</i> characters/word (default 4) when initializing numeric variables with character data. </p>
 </dd>
<dt><code>-z</code></dt>
<dd> <p> Do not implicitly recognize DOUBLE COMPLEX. </p>
 </dd>
<dt><code>-!bs</code></dt>
<dd> <p> Do not recognize <i>b</i>ack <i>s</i>lash escapes (\&quot;, \&#8216;, \0, \\, \b, \f, \n, \r, \t, \v) in character strings. </p>
 </dd>
<dt><code>-!c</code></dt>
<dd> <p> Inhibit C output, but produce <code>-P</code> output. </p>
 </dd>
<dt><code>-!I</code></dt>
<dd> <p> Reject <code>include</code> statements. </p>
 </dd>
<dt><code>-!i8</code></dt>
<dd> <p> Disallow INTEGER*8 , or, if the option is `-!i8const&#8217;, permit INTEGER*8 but do not promote integer constants to INTEGER*8 when they involve more than 32 bits. </p>
 </dd>
<dt><code>-!it</code></dt>
<dd> <p> Don&#8217;t infer types of untyped EXTERNAL procedures from use as parameters to previously defined or prototyped procedures. </p>
 </dd>
<dt><code>-!P</code></dt>
<dd> <p> Do not attempt to infer ANSI or C++ prototypes from usage. </p>
 </dd></dl>
<p> The resulting C invokes the support routines of <i>f77</i>; object code should be loaded by <i>f77</i> or with <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1) or <i><a href="/docs/linux/man/1-cc/">cc</a></i>(1) options <code>-lF77 -lI77 -lm</code>. Calling conventions are those of <i>f77</i>: see the reference below. <br/>
  </p>
<h2>FILES</h2>
<dl>
<dd> <p> <i>file</i><code>.[fF]</code> input file </p>
 </dd>
<dt><code>*.c</code></dt>
<dd> <p> output file </p>
 </dd>
<dd> <p> header file </p>
 </dd>
<dd> <p> intrinsic function library </p>
 </dd>
<dd> <p> Fortran I/O library </p>
 </dd>
<dd> <p> C library, see section 3 </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> S. I. Feldman and P. J. Weinberger, `A Portable Fortran 77 Compiler&#8217;, <i>UNIX Time Sharing System Programmer&#8217;s Manual</i>, Tenth Edition, Volume 2, AT&amp;T Bell Laboratories, 1990.  </p>
<h2>DIAGNOSTICS</h2>
<p> The diagnostics produced by <i>f2c</i> are intended to be self-explanatory.  </p>
<h2>BUGS</h2>
<p> Floating-point constant expressions are simplified in the floating-point arithmetic of the machine running <i>f2c</i>, so they are typically accurate to at most 16 or 17 decimal places. <br/>
 Untypable EXTERNAL functions are declared <code>int</code>. <br/>
 There is no notation for INTEGER*8 constants. <br/>
 Some intrinsic functions do not yet work with INTEGER*8 . </p>
