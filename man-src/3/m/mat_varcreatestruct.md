---
title: "mat_varcreatestruct(3)"
name: "mat_varcreatestruct"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varcreatestruct/"
description: "Mat_VarCreateStruct – Creates a structure variable."
---

<p><code>Mat_VarCreateStruct</code> &#8211; Creates a structure variable.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarCreateStruct Fa const char *name Fa int rank Fa size_t *dims Fa const char **fields Fa unsigned nfields Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarCreateStruct function creates a structure variable named Fa name that can be written to a MAT file.</p>
<h2>Return Values</h2>
<p>If the structure variable was successfully created, a pointer to the variable is returned. Otherwise NULL is returned. The structure variable pointer should be free&#8217;d when no longer needed using Mat_VarFree3 . The names of the fields are copied in the function, and thus should be released after calling the function if necessary.</p>
<h2>Examples</h2>
<p>This example program opens a MAT file named by the first argument to the program, and writes a structure named <i>a</i> to the file. </p>
<pre>#include &quot;matio.h&quot;
int
main(int argc,char **argv)
{
 mat_t *matfp;
 matvar_t *matvar;
 matvar_t *field;
 const char *fields[2] = {&quot;field1&quot;,&quot;field2&quot;};
 double data1 = 1, data2 = 2;
 size_t dims[2] = {1, 1};
 matfp = Mat_Open(argv[1],MAT_ACC_RDWR);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error opening MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 dims[0] = 1; dims[1] = 1;
 matvar = Mat_VarCreateStruct(&quot;a&quot;,2,dims,fields,2);
 if ( NULL == matvar ) {
 Mat_Close(matfp);
 return EXIT_FAILURE;
 }
 field = Mat_VarCreate(NULL,MAT_C_DOUBLE,MAT_T_DOUBLE,2,dims,&amp;data1,
 MAT_F_DONT_COPY_DATA);
 Mat_VarSetStructFieldByName(matvar, &quot;field1&quot;, 0, field);
 field = Mat_VarCreate(NULL,MAT_C_DOUBLE,MAT_T_DOUBLE,2,dims,&amp;data2,
 MAT_F_DONT_COPY_DATA);
 Mat_VarSetStructFieldByName(matvar, &quot;field2&quot;, 0, field);
 Mat_VarWrite(matfp,matvar,MAT_COMPRESSION_NONE);
 Mat_VarFree(matvar);
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_VarCreate3, Mat_VarSetStructFieldByName3</p>
