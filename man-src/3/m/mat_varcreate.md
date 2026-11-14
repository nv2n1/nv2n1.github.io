---
title: "mat_varcreate(3)"
name: "mat_varcreate"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varcreate/"
description: "Mat_VarCreate – Creates a MAT variable structure."
---

<p><code>Mat_VarCreate</code> &#8211; Creates a MAT variable structure.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarCreate Fa const char *name Fa enum matio_classes class_type Fa enum matio_types data_type Fa int rank Fa size_t *dims Fa void *data Fa int opt Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarCreate function creates a MAT structure variable named Fa name that can be written to a MAT file. The Fa class_type argument specifies the class of the variable, and the Fa data_type argument specifies the type of the data. For example, a double-precision class would use <code>MAT_C_DOUBLE</code> for the class type and <code>MAT_T_DOUBLE</code> for the data type. In some instances, the data type may not match the class type. For exmaple, an array of integers can be written in the double-precision class by using <code>MAT_T_INT32</code> for Fa data_type. </p>
<p> The Fa rank argument specifies how many dimensions the data has. The minimum rank is 2. The number of elements in each dimension is specified in the array Fa dims. </p>
<p> The Fa data argument is a pointer to the variable data. The pointer is typically a pointer to a numeric array (e.g. double, float, int, etc.) for real variables. For complex variables, the pointer is a pointer to a Vt mat_complex_split_t which contains pointers to the real and imaginary data as fields of the structure. For sparse variables, the pointer should be a Vt mat_sparse_t *. </p>
<h2>Return Values</h2>
<p>If the variable was successfully created, a pointer to the variable is returned. Otherwise NULL is returned. The variable should be free&#8217;d when no longer needed using Mat_VarFree.</p>
<h2>Examples</h2>
<p>The example program below creates a MAT file named <i>test.mat,</i> and writes two real numeric variables <i>x</i> and <i>y</i> and a complex variable <i>z</i> to the file. </p>
<pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;matio.h&quot;
int
main(int argc,char **argv)
{
 mat_t *matfp;
 matvar_t *matvar;
 size_t dims[2] = {10,1};
 double x[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9,10},
 y[10] = {11,12,13,14,15,16,17,18,19,20};
 struct mat_complex_split_t z = {x,y};
 matfp = Mat_CreateVer(&quot;test.mat&quot;,NULL,MAT_FT_DEFAULT);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error creating MAT file return EXIT_FAILURE;
 }
 matvar = Mat_VarCreate(&quot;x&quot;,MAT_C_DOUBLE,MAT_T_DOUBLE,2,dims,x,0);
 if ( NULL == matvar ) {
 fprintf(stderr,&quot;Error creating variable for 'x');
 } else {
 Mat_VarWrite(matfp,matvar,COMPRESSION_NONE);
 Mat_VarFree(matvar);
 }
 matvar = Mat_VarCreate(&quot;y&quot;,MAT_C_DOUBLE,MAT_T_DOUBLE,2,dims,y,0);
 if ( NULL == matvar ) {
 fprintf(stderr,&quot;Error creating variable for 'y');
 } else {
 Mat_VarWrite(matfp,matvar,COMPRESSION_NONE);
 Mat_VarFree(matvar);
 }
 matvar = Mat_VarCreate(&quot;z&quot;,MAT_C_DOUBLE,MAT_T_DOUBLE,2,dims,&amp;z,
 MAT_F_COMPLEX);
 if ( NULL == matvar ) {
 fprintf(stderr,&quot;Error creating variable for 'z');
 } else {
 Mat_VarWrite(matfp,matvar,COMPRESSION_NONE);
 Mat_VarFree(matvar);
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_VarCreateStruct3, Mat_VarFree3, Mat_VarWrite3</p>
