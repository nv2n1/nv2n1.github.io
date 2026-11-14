---
title: "ncl_ncarg_cbind(3)"
name: "ncl_ncarg_cbind"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ncarg_cbind/"
description: "NCAR Graphics C-binding – Description of how to use the NCAR Graphics C-binding."
---

<p>NCAR Graphics C-binding &#8211; Description of how to use the NCAR Graphics C-binding.</p>
<h2>Synopsis</h2>
<p>The NCAR Graphics C-binding consists of a collection of C routines that allow you to call NCAR Graphics Fortran routines from a C program without having to worry about the C to Fortran interface yourself. For detailed information about the C-binding for a particular routine, please see the man page for the corresponding Fortran routine. A C-binding has been created for every user entry point in the NCAR Graphics utilities with the exception of some of the obsolete utilities listed below. A GKS level 0A C-binding has also been created which adheres to the ISO/IEC standard. </p>
<pre><code>From here on, a utility C-binding refers to a C-binding for the
NCAR Graphics utilities (AREAS, CONPACK, etc.).</code></pre>
<h2>Naming Convention</h2>
<p>For all of the utility user entry points, the name of the C-binding function is the same as the Fortran routine name with a &quot;c_&quot; prepended. For example, the name of the C-binding for the CONPACK routine <code>CPBACK</code> is <code>c_cpback</code>. This naming convention does not apply to the GKS C-bindings. Instead, the C-binding names are more descriptive, like <code>gset_fill_colr_ind</code> which is equivalent to the Fortran routine <code>GSFACI</code>. Please see the man page for ncarg_gks_cbind(3NCARG) the GKS Fortran routine to get the name of the corresponding GKS C-binding name. </p>
<p> The C programming language is case sensitive, so for convenience the utility C-binding names and their arguments are all in lower case. In this man page, the Fortran routines and their arguments will be referred to in upper-case.</p>
<h2>Argument Lists</h2>
<p>The argument list of each utility C-binding corresponds with the argument list of the corresponding Fortran routine except in some cases where multi-dimensioned arrays and/or character strings are involved. These exceptions will be described in separate sections. </p>
<p> The C-binding argument list being similar to the Fortran argument list makes using the C-bindings easier for people who already know the calling sequence of a particular Fortran routine. For example, the NCAR Graphics routine <code>PLCHHQ</code> has the following argument list: </p>
<pre>PLCHHQ(REAL X, REAL Y, CHARACTER CHRS, REAL SZ, REAL ANG, REAL CNTR)</pre>
<p>and the corresponding C-binding <code>c_plchhq</code> has the same type of argument list: </p>
<pre>c_plchhq(float x, float y, char *chrs, float sz, float ang, float cntr)</pre>
<h2>Arrays</h2>
<p>One of the exceptions to the utility C-binding argument lists has to do with multi-dimensioned arrays. In Fortran, arrays are stored in column-major order, while in C they are stored in row-major order. This means that the subscripts of a multi-dimensioned array need to be switched before passing the array to a Fortran routine from C. </p>
<p> As an example, the <code>CONPACK</code> routine <code>CPRECT</code> takes as one of its arguments a two-dimensional array, <i>ZDAT</i>. If the Fortran dimensions of <i>ZDAT</i> are to be 25 x 14, then in the C program you must dimension <i>ZDAT</i> to be 14 x 25 before calling the C-binding <code>c_cprect</code>. The next three arguments of <code>CPRECT</code> describe the array in question. The first of these three arguments, <i>KZDT</i>, is the first dimension of the array <i>ZDAT</i> as it is declared in the Fortran calling program. For <code>CPRECT</code> this value would be 25. For the C-binding <code>c_cprect</code>, however, this argument is the second dimension of the array as declared in the C program. This value would be 25 as well since the subscripts had to be switched in the C program. The second and third of these three arguments (<i>MZDT</i> and <i>NZDT</i>) specify the number of elements in each row and column (respectively) to be contoured. If you only want to contour 20 x 10 of the array <i>ZDAT</i>, then <i>MZDT</i> and <i>NZDT</i> should be 20 and 10 respectively in <code>CPRECT</code>. For <code>c_cprect</code>, these variables specify the columns and rows, so again, the values would be 20 and 10 (because the subscripts have to be switched).</p>
<h2>Character Strings</h2>
<p>Another exception to the argument lists for the utility C-bindings has to do with routines that return character strings. The NCAR Graphics routines that return strings through the parameter list do not have a string length as part of their argument lists, so you must pass an extra argument to the C-binding which specifies the maximum length of the string. Also, all input strings passed to the C-bindings must be null-terminated! </p>
<p> For example, in the routine <code>PCGETC</code>, you pass a parameter name and it returns the value of that parameter which in this case is a string. The two arguments to <code>PCGETC</code> are <i>WHCH</i> and <i>CVAL</i>, where <i>WHCH</i> is the parameter name and <i>CVAL</i> is the string to be returned. Since the C-binding <code>c_pcgetc</code> needs to know the length of <i>cval</i>, an extra argument of type &quot;int&quot; must be passed. Thus, the arguments for <code>c_pcgetc</code> would be <i>whch</i>, <i>cval</i>, and <i>len</i>, where <i>len</i> is the length of <i>cval</i> as it is declared in the C program. In any case of having to add an extra argument for the string length, the extra argument will always be the last one in the list. If more than one string length argument needs to be added, then each one should be added at the end of the argument list in the order that their corresponding strings appear. </p>
<p> There are some routines like <code>AGDSHN</code> which are defined as character strings themselves. In this case, the user does not need to pass a string length since it is already defined. But, the string that is returned is declared statically, thus it will go away once you call the routine again. If you need to save these character strings, be sure to copy them to your own local variable.</p>
<h2>Function Prototypes</h2>
<p>The C-bindings are intended to be ANSI C compliant. To get the correct function prototypes for the utility C-bindings, you can include &lt;ncarg/ncargC.h&gt;. For the GKS C-bindings, include &lt;ncarg/gks.h&gt;. In some cases, it may be necessary to typecast the arguments in the utility C-bindings to get the prototypes correct. For example, the C-bindings do not distinguish between singly and multiply dimensioned arrays, so if you are passing a multiply dimensioned float array, you may need to typecast it as a (float *) if this is not how it is declared in the main program.</p>
<h2>Compiling Your Program</h2>
<p>To compile your NCAR Graphics C program with the C-bindings, use the NCARG application <code>ncargcc</code>. <code>ncargcc</code> will take care of loading in the necessary C/Fortran interface libraries as well as the NCAR Graphics C and Fortran libraries. You will either need to set the NCARG_ROOT or the NCARG_BIN, NCARG_LIB, and NCARG_INCLUDE environment variables in order to run <code>ncargcc</code>. See &quot;man ncargintro&quot; for more information. </p>
<p> If you do not wish to use <code>ncargcc</code>, then you can just run it with no arguments to see what the necessary libraries are, and then put this information in your Makefile or whatever else you are using to compile and link your program. Note: if you have an ANSI C compiler, it is important that you define the macro <code>NeedFuncProto</code> on the compile line so that function prototyping is included.</p>
<h2>Examples</h2>
<p>A few examples of C programs that call the NCAR Graphics C-bindings have been provided for your convenience. You may be familiar with the output from these C programs as they were modeled after the Fortran programs that you can get with the <code>ncargex</code> command. To copy any one of these C programs in your directory, and then compile, link, and run it, type: <code>ncargex</code> <i>xxxx</i> where <i>xxxx</i> is the name of the example you wish to generate. To see a list of all the C examples, type: <code>ncargex -C -list</code> <code>ncargex</code> uses <code>ncargcc</code> to compile and link the C-binding example programs. </p>
<h2>Obsolete Routines</h2>
<p>C-bindings have not been provided for user entry points in the following obsolete utilities: </p>
<p> Conran_family, Conrec_family, Halftone, Isosrfhr, and Pwrite_family.</p>
<h2>See Also</h2>
<pre><code>Online : ncargcc(1NCARG),

         ncargex(1NCARG),

         ncarg_gks_cbind(3NCARG),

         ncargintro(5NCARG).Hardcopy : NCAR Graphics Fundamentals,
         UNIX Version;
User's Guide for NCAR GKS - 0A Graphics</code></pre>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement.</p>
