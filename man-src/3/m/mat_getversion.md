---
title: "mat_getversion(3)"
name: "mat_getversion"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_getversion/"
description: "Mat_GetVersion – Returns the filename of a MATLAB .mat file given a MAT file structure"
---

<p><code>Mat_GetVersion</code> &#8211; Returns the filename of a MATLAB .mat file given a MAT file structure</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft enum mat_ft Fo Mat_GetVersion Fa mat_t *matfp Fc</p>
<h2>Description</h2>
<p>The Fn Mat_GetVersion function returns the version of the MATLAB .mat file given by the MAT file structure. The return value is one of the following: </p>
<ul>
<li> <code>MAT_FT_MAT73</code> if the file is an HDF5 MAT file.
<li> <code>MAT_FT_MAT5</code> if the file is a level 5 MAT file.
<li> <code>MAT_FT_MAT4</code> if the file is a level 4 MAT file. </ul>
<h2>See Also</h2>
<p>Mat_Create3, Mat_CreateVer3, Mat_Open3 Mat_GetFilename3</p>
