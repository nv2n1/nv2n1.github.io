---
title: "mat_varreadnextinfo(3)"
name: "mat_varreadnextinfo"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varreadnextinfo/"
description: "Mat_VarReadNextInfo – Reads the information for the next variable in a MATLAB MAT file."
---

<p><code>Mat_VarReadNextInfo</code> &#8211; Reads the information for the next variable in a MATLAB MAT file.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarReadNextInfo Fa mat_t *mat Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarReadNextInfo function reads the information for the next variable stored in the open MAT file.</p>
<h2>Return Values</h2>
<p>If there is another variable in the MAT file and is read successfully, a pointer to the MATLAB variable structure is returned. If there are no more variables, or there was an error reading the variable, NULL is returned.</p>
<h2>Examples</h2>
<p>This example program opens a MAT file named by the first argument to the program, and uses Fn Mat_VarReadNextInfo to read the information about each variable in the file. For each variable read,the name, size, and class are printed in a format similar to the MATLAB whos command. </p>
<pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;matio.h&quot;
static char *mxclass[16] = {&quot;cell&quot;, &quot;struct&quot;, &quot;object&quot;,&quot;char&quot;,&quot;sparse&quot;,
 &quot;double&quot;,&quot;single&quot;,&quot;int8&quot;, &quot;uint8&quot;,&quot;int16&quot;,&quot;uint16&quot;,
 &quot;int32&quot;,&quot;uint32&quot;,&quot;int64&quot;,&quot;uint64&quot;,&quot;function&quot;
 };
int
main(int argc,char **argv)
{
 mat_t *matfp;
 matvar_t *matvar;
 size_t nbytes;
 int i;
 char size[32] = {'&nbsp;<wbr>',};
 matfp = Mat_Open(argv[1],MAT_ACC_RDONLY);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error opening MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 printf(&quot;%-20s %-10s %-10s %-18sn&quot;,&quot;Name&quot;,&quot;Size&quot;,&quot;Bytes&quot;,
 &quot;Class&quot;);
 while ( NULL != (matvar = Mat_VarReadNextInfo(matfp)) ) {
 printf(&quot;%-20s&quot;, matvar-&gt;name);
 if ( matvar-&gt;rank &gt; 0 ) {
 int cnt = 0;
 printf(&quot;%8d&quot;, matvar-&gt;dims[0]);
 for ( i = 1; i &lt; matvar-&gt;rank; i++ ) {
 if ( ceil(log10(matvar-&gt;dims[i]))+1 &lt; 32 )
 cnt += sprintf(size+cnt,&quot;x%d&quot;, matvar-&gt;dims[i]);
 }
 printf(&quot;%-10s&quot;,size);
 } else {
 printf(&quot; &quot;);
 }
 printf(&quot; %-18s,mxclass[matvar-&gt;class_type-1]);
 Mat_VarFree(matvar);
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_VarRead3, Mat_VarReadNextInfo3,</p>
