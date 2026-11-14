---
title: "mat_open(3)"
name: "mat_open"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_open/"
description: "Mat_Open – Open a MATLAB .mat file"
---

<p><code>Mat_Open</code> &#8211; Open a MATLAB .mat file</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft mat_t Fo Mat_Open Fa const char *matname Fa int mode Fc</p>
<h2>Description</h2>
<p>The Fn Mat_Open function opens a MATLAB .mat file for read only or read-write access.</p>
<h2>Examples</h2>
<pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;matio.h&quot;
int main(int argc,char **argv)
{
 mat_t *matfp;
 matfp = Mat_Open(argv[1],MAT_ACC_RDONLY);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error opening MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_Create3, Mat_CreateVer3, Mat_Close3</p>
