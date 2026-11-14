---
title: "mat_createver(3)"
name: "mat_createver"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_createver/"
description: "Mat_CreateVer Mat_Create – Create a MATLAB .mat file"
---

<p><code>Mat_CreateVer</code> <code>Mat_Create</code> &#8211; Create a MATLAB .mat file</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft mat_t * Fo Mat_CreateVer Fa const char *matname Fa const char *hdr_str Fa enum mat_ft mat_file_ver Fc Ft mat_t * Fo Mat_Create Fa const char *matname Fa const char *hdr_str Fc</p>
<h2>Description</h2>
<p>The Fn Mat_CreateVer function creates a MATLAB .mat file opened for write access. The <i>hdr_str</i> is a string written in the file header of MAT version 5 and 7.3 (HDF) files. Only the first 128 bytes of the string is written. If <i>hdr_str</i> is NULL, then a default string is written that contains the platform, date, matio library version. </p>
<p> The <i>mat_file_ver</i> argument specifies the MAT file version to create. The matio library can write version 5 files (MAT_FT_MAT5), and an HDF5 file format introduced in MATLAB version 7.3 (MAT_FT_MAT73). </p>
<p> The Fn Mat_Create function is equivalent to calling Fn Mat_CreateVer with MAT_FT_DEFAULT as the file version.</p>
<h2>Examples</h2>
<pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;matio.h&quot;
int main(int argc,char **argv)
{
 mat_t *matfp;
 matfp = Mat_CreateVer(argv[1],NULL,MAT_FT_73);
 if ( NULL == matfp ) {
 fprintf(stderr,&quot;Error creating MAT file %s,argv[1]);
 return EXIT_FAILURE;
 }
 Mat_Close(matfp);
 return EXIT_SUCCESS;
}</pre>
<h2>See Also</h2>
<p>Mat_Create3, Mat_CreateVer3, Mat_Close3</p>
