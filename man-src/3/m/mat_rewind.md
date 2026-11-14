---
title: "mat_rewind(3)"
name: "mat_rewind"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_rewind/"
description: "Mat_Rewind – Rewind an open .mat file to the beginning"
---

<p><code>Mat_Rewind</code> &#8211; Rewind an open .mat file to the beginning</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft int Fo Mat_Rewind Fa mat_t *matfp Fc</p>
<h2>Description</h2>
<p>Rewinds an open .mat file so that Mat_VarReadNext3 or Mat_VarReadNextInfo3 reads the first variable in the file.</p>
<h2>Return Values</h2>
<p>The function returns 0 on success, or -1 on failure.</p>
<h2>Examples</h2>
<p>The following example shows a list of variables in the MAT file, and prompts the user for the index of the variale to read. If the index is valid, the file is reset to the beginning, and variables read until the selected index is reached. </p>
<pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;matio.h&quot;
int
main(int argc,char **argv)
{
 mat_t *matfp;
 matvar_t *matvar;
 int idx, num_variables;
 matfp = Mat_Open(argv[1],MAT_ACC_RDONLY);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error opening MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 idx = 0;
 while ( NULL != (matvar = Mat_VarReadNextInfo(matfp)) ) {
 idx++;
 printf(&quot;%3d. %s,idx,matvar-&gt;name);
 Mat_VarFree(matvar);
 }
 num_variables = idx;
 if ( num_variables &gt; 0 ) {
 printf(&quot;Which variable would you like to read? &quot;);
 if ( 0 == fscanf(stdin,&quot;%d&quot;,&amp;idx) ) {
 printf(&quot;Invalid variable selection!);
 } else if ( idx &lt; 1 || idx &gt; num_variables ) {
 fprintf(stderr,&quot;That is an invalid variable index!);
 } else {
 int k;
 Mat_Rewind(matfp);
 for ( k = 1; k &lt; idx; k++ ) {
 matvar = Mat_VarReadNextInfo(matfp);
 Mat_VarFree(matvar);
 }
 matvar = Mat_VarReadNext(matfp);
 Mat_VarPrint(matvar,1);
 Mat_VarFree(matvar);
 }
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_Open3, Mat_Close3, Mat_VarReadNext3, Mat_VarReadNextInfo3</p>
