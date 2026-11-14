---
title: "funimageput(3)"
name: "funimageput"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funimageput/"
description: "FunImagePut – put an image to a Funtools file"
---

<h2>NAME</h2>
<p> <code>FunImagePut &#8211; put an image to a Funtools file</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>int FunImagePut(Fun fun, void *buf, int dim1, int dim2, int bitpix,<br />
                char *plist)</p>
<h2>DESCRIPTION</h2>
<p> The FunImagePut() routine outputs an image array to a <font SIZE="-1">FITS</font> file. The image is written either as a primary header/data unit or as an image extension, depending on whether other data have already been written to the file. That is, if the current file position is at the beginning of the file, a primary <font SIZE="-1">HDU</font> is written. Otherwise, an image extension is written. </p>
<p> The first argument is the Funtools handle returned by <i>FunOpen()</i>. The second <code>buf</code> argument is a pointer to a data buffer to write. The <code>dim1</code>and <code>dim2</code> arguments that follow specify the dimensions of the image, where dim1 corresponds to naxis1 and dim2 corresponds to naxis2. The <code>bitpix</code> argument specifies the data type of the image and can have the following FITS-standard values:</p>
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
<p> When <i>FunTableRowPut()</i> is first called for a given image, Funtools checks to see if the primary header has already been written (by having previously written an image or a binary table.) If not, this image is written to the primary <font SIZE="-1">HDU</font>. Otherwise, it is written to an image extension. </p>
<p> Thus, a simple program to generate a <font SIZE="-1">FITS</font> image might look like this: </p>
<pre><code>
int i;
int dim1 = 512, dim2 = 512;
double *dbuf;
Fun fun;
dbuf = malloc(dim1 * dim2 * sizeof(double));
/* open the output FITS image, preparing to copy input params */
if (!(fun = FunOpen(argv[1], "w", NULL)))
    gerror(stderr, "could not FunOpen output file: %s
", argv[1]);
for (i = 0; i &lt; (dim1 * dim2); i++) {
    ... fill dbuf...
}
/* put the image (header will be generated automatically */
if (!FunImagePut(fun, buf, dim1, dim2, -64, NULL))
    gerror(stderr, "could not FunImagePut: %s
", argv[1]);
FunClose(fun);
free(dbuf);
</code></pre>
<p> In addition, if a Funtools reference handle was specified when this table was opened, the parameters from this Funtools reference handle are merged into the new image header. Furthermore, if a reference image was specified during <i>FunOpen()</i>, the values of <code>dim1</code>, <code>dim2</code>, and <code>bitpix</code> in the calling sequence can all be set to 0. In this case, default values are taken from the reference image section. This is useful if you are reading an image section in its native data format, processing it, and then writing that section to a new <font SIZE="-1">FITS</font> file. See the imblank example code. </p>
<p> The data are assumed to be in the native machine format and will automatically be swapped to <font SIZE="-1">FITS</font> big-endian format if necessary. This behavior can be over-ridden with the <code>convert=[true|false]</code> keyword in the <code>plist</code> param list string. </p>
<p> When you are finished writing the image, you should call <i>FunFlush()</i> to write out the <font SIZE="-1">FITS</font> image padding. However, this is not necessary if you subsequently call <i>FunClose()</i> without doing any other I/O to the <font SIZE="-1">FITS</font> file.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
