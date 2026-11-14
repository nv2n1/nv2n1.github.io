---
title: "mat_varwrite(3)"
name: "mat_varwrite"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varwrite/"
description: "Mat_VarWrite – Writes a MATLAB variable to a MATLAB MAT file."
---

<p><code>Mat_VarWrite</code> &#8211; Writes a MATLAB variable to a MATLAB MAT file.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft int Fo Mat_VarWrite Fa mat_t *mat Fa matvar_t *matvar Fa enum matio_compression compress Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarWrite function writes the MATLAB variable Fa matvar to the MAT file Fa mat which must be opened for writing. If the MAT file is a level 5 MAT file, the compress option allows the variable to be written using zlib compression if available. If compression is not available, the variable is written uncompressed.</p>
<h2>Return Values</h2>
<p>The function returns 0 if the variable was successfully written to the MAT file. otherwise, an error value is returned.</p>
<h2>Examples</h2>
<p>This example program creates a MAT file named by the first argument to the program, and writes the variable named <i>m_pi</i> to the file. </p>
<pre>#include &lt;math.h&gt;
#include &quot;matio.h&quot;
int
main(int argc,char **argv)
{
 mat_t *matfp;
 matvar_t *matvar;
 size_t dims[2] = {1,1};
 double m_pi = M_PI;
 matfp = Mat_CreateVer(argv[1],NULL,MAT_FT_DEFAULT);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error creating MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 matvar = Mat_VarCreate(&quot;m_pi&quot;,MAT_C_DOUBLE,MAT_T_DOUBLE,2,dims,&amp;m_pi,0);
 if ( NULL != matvar ) {
 Mat_VarWrite(matfp,matvar,MAT_COMPRESSION_ZLIB);
 Mat_VarFree(matvar);
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_CreateVer3, Mat_Open3, Mat_VarRead3</p>
