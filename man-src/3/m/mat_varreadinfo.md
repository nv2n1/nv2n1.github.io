---
title: "mat_varreadinfo(3)"
name: "mat_varreadinfo"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varreadinfo/"
description: "Mat_VarReadInfo – Read the information for a specific variable in a MATLAB MAT file."
---

<p><code>Mat_VarReadInfo</code> &#8211; Read the information for a specific variable in a MATLAB MAT file.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarReadInfo Fa mat_t *mat Fa const char *name Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarReadInfo function reads the information for the variable Fa name in the open MAT file.</p>
<h2>Return Values</h2>
<p>If the variable was found in the MAT file and the information about the variable successfully read, a pointer to the MATLAB variable structure is returned. If the variable was not found, or there was an error reading the variable information, NULL is returned.</p>
<h2>Examples</h2>
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
 matvar = Mat_VarReadInfo(matfp,&quot;x&quot;);
 if ( NULL != matvar ) {
 Mat_VarPrint(matvar);
 Mat_VarFree(matvar);
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_VarRead3, Mat_VarReadNextInfo3</p>
