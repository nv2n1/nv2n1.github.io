---
title: "mat_close(3)"
name: "mat_close"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_close/"
description: "Mat_Close – Closes an open MATLAB .mat file"
---

<p><code>Mat_Close</code> &#8211; Closes an open MATLAB .mat file</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft int Fo Mat_Close Fa mat_t *matname Fc</p>
<h2>Description</h2>
<p>The Fn Mat_Close function closes a MATLAB .mat file opened with Fn Mat_Open or created with Fn Mat_CreateVer</p>
<h2>Examples</h2>
<pre>#include &quot;matio.h&quot;
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
<p>Mat_Open3, Mat_CreateVer3,</p>
