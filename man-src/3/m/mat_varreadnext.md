---
title: "mat_varreadnext(3)"
name: "mat_varreadnext"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varreadnext/"
description: "Mat_VarReadNext – Reads the information and data for the next variable in a MATLAB MAT file."
---

<p><code>Mat_VarReadNext</code> &#8211; Reads the information and data for the next variable in a MATLAB MAT file.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarReadNext Fa mat_t *mat Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarReadNext function reads the information and data for the next variable stored in the open MAT file.</p>
<h2>Return Values</h2>
<p>If there is another variable in the MAT file and is read successfully, a pointer to the MATLAB variable structure is returned. If there are no more variables, or there was an error reading the variable, NULL is returned.</p>
<h2>Examples</h2>
<p>This example program opens a MAT file named by the first argument to the program, and uses Fn Mat_VarReadNext to read each variable in the file. For each variable read, the Mat_VarPrint3 function is used to display the information and data of the variable. </p>
<pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;matio.h&quot;
int
main(int argc,char **argv)
{
 mat_t *matfp;
 matvar_t *matvar;
 matfp = Mat_Open(argv[1],MAT_ACC_RDONLY);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error opening MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 while ( NULL != (matvar = Mat_VarReadNext(matfp)) ) {
 Mat_VarPrint(matvar,1);
 Mat_VarFree(matvar);
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_VarRead3, Mat_VarReadNextInfo3,</p>
