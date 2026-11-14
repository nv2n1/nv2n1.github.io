---
title: "funimagerowput(3)"
name: "funimagerowput"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funimagerowput/"
description: "FunImageRowPut – put row(s) of an image"
---

<h2>NAME</h2>
<p> <code>FunImageRowPut &#8211; put row(s) of an image</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>void *FunImageRowPut(Fun fun, void *buf, int rstart, int rstop,<br />
                     int dim1, int dim2, int bitpix, char *plist)</p>
<h2>DESCRIPTION</h2>
<p> The FunImageRowPut() routine writes one or more image rows to the specified <font SIZE="-1">FITS</font> image file. The first argument is the Funtools handle returned by <i>FunOpen()</i>. The second <code>buf</code> argument is a pointer to the row data buffer, while the third and fourth arguments specify the starting and ending rows to write. Valid rows values range from 1 to dim2, i.e., row is one-valued. </p>
<p> The <code>dim1</code>and <code>dim2</code> arguments that follow specify the dimensions, where dim1 corresponds to naxis1 and dim2 corresponds to naxis2. The <code>bitpix</code> argument data type of the image and can have the following FITS-standard values:</p>
<dl>
<dt>*</p>
<dd> 8 unsigned char</p>
<dt>*</p>
<dd> 16 short</p>
<dt>*</p>
<dd> 32 int</p>
<dt>*</p>
<dd> -32 float</p>
<dt>*</p>
<dd> -64 double</dl>
<p> For example: </p>
<pre><code>
double *drow;
Fun fun, fun2;
... open files...
    /* get section dimensions */
    FunInfoGet(fun, FUN_SECT_DIM1, &amp;dim1, FUN_SECT_DIM2, &amp;dim2, 0);
/* allocate one line's worth */
drow = malloc(dim1 * sizeof(double));
/* retrieve and process each input row (starting at 1) */
for (i = 1; i &lt;= dim2; i++) {
    if (!FunImageRowGet(fun, drow, i, i, "bitpix=-64"))
        gerror(stderr, "can't FunImageRowGet: %d %s
", i, iname);
    ... process drow... if (!FunImageRowPut(fun2, drow, i, i, 64, NULL))
        gerror(stderr, "can't FunImageRowPut: %d %s
", i, oname);
}
...
</code></pre>
<p> The data are assumed to be in the native machine format and will automatically be swapped to big-endian <font SIZE="-1">FITS</font> format if necessary. This behavior can be over-ridden with the <code>convert=[true|false]</code> keyword in the <code>plist</code> param list string. </p>
<p> When you are finished writing the image, you should call <i>FunFlush()</i> to write out the <font SIZE="-1">FITS</font> image padding. However, this is not necessary if you subsequently call <i>FunClose()</i> without doing any other I/O to the <font SIZE="-1">FITS</font> file.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
