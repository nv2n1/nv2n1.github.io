---
title: "mat_varread(3)"
name: "mat_varread"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varread/"
description: "Mat_VarRead – Reads the information and data for a specific variable in a MATLAB MAT file."
---

<p><code>Mat_VarRead</code> &#8211; Reads the information and data for a specific variable in a MATLAB MAT file.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarRead Fa mat_t *mat Fa const char *name Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarRead function reads the information and data for the variable Fa name in the open MAT file.</p>
<h2>Return Values</h2>
<p>If the variable was found in the MAT file and successfully read, a pointer to the MATLAB variable structure is returned. If the variable was not found, or there was an error reading the variable, NULL is returned.</p>
<h2>Examples</h2>
<p>This example program opens a MAT file named by the first argument to the program, and reads a variable named <i>x</i> from the file. The MATIO function Mat_VarPrint is used to print the information and data from the file. </p>
<pre>#include &quot;matio.h&quot;
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
 matvar = Mat_VarRead(matfp,&quot;x&quot;);
 if ( NULL != matvar ) {
 Mat_VarPrint(matvar);
 Mat_VarFree(matvar);
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_VarReadInfo3, Mat_VarReadNext3, Mat_VarPrint3</p>
