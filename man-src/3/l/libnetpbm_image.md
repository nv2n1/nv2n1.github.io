---
title: "libnetpbm_image(3)"
name: "libnetpbm_image"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnetpbm_image/"
description: "libnetpbm_image – overview of netpbm image-processing functions"
---

<p>Table Of Contents</p>
<h2 class="name">NAME</h2>
<p> libnetpbm_image &#8211; overview of netpbm image-processing functions </p>
<h2>DESCRIPTION</h2>
<p> This reference manual covers functions in the <code>libnetpbm</code> library for processing images, using the Netpbm image formats and the <code>libnetpbm</code> in-memory image formats. </p>
<p> For historical reasons as well as to avoid clutter, it does not cover the largely obsolete PBM, PGM, PPM, and PNM classes of <code>libnetpbm</code> functions. For those, see <code>PBM</code> Function Manual (1) , <code>PGM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) , <code>PPM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) , and <code>PNM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) <code>te that you do </code><i>not</i> need those functions to process PBM, PGM, PPM, and PNM images. The functions in this manual are sufficient for that. </p>
<p> The PPM drawing functions are covered separately in <code>PPM</code>Drawing<code>Function</code><a href="/docs/linux/man/1-manual/">Manual</a><code>(1)</code> </p>
<p> For introductory and general information using <code>libnetpbm</code>, see <code>Libnetpbm</code>User&#8217;s<code><a href="/docs/linux/man/1-guide/">Guide</a></code>(1) </p>
<p> <code>libnetpbm</code> also contains functions that are not specifically oriented toward processing image data. Read about those in the <code>Libnetpbm</code>Utility<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) </p>
<p> To use these services, #include <code>pam.h</code>. </p>
<h2>Types</h2>
<p> Here are some important types that you use with <code>libnetpbm</code>: </p>
<dl>
<dt>sample</p>
<dd> A sample of a Netpbm image. See the format specifications &#8212; as an example, the red intensity of a particular pixel of a PPM image is a sample. This is an integer type. </p>
<dt>tuple</p>
<dd> A tuple from a PAM image or the PAM equivalent of a PNM image. See the PAM format specification &#8212; as an example, a pixel of a PPM image would be a tuple. A tuple is an array of samples. </p>
<dt>samplen</p>
<dd> Same as <code>sample</code>, except in normalized form. This is a floating point type with a value in the range 0..1. 0 corresponds to a PAM/PNM sample value of 0. 1 corresponds to a PAM/PNM sample value equal to the image&#8217;s maxval. </p>
<dt>tuplen</p>
<dd> The same as <code>tuple</code>, except composed of normalized samples (<code>samplen</code>) instead of regular samples (<code>sample</code>). </p>
</dl>
<p> The main argument to most of the PAM functions is the address of a <code>pam</code> structure, which is defined as follows: </p>
<p> <code>struct pam {</code> <code>int </code><i>size</i> <code>int </code><i>len</i> <code>FILE *</code><i>file </i> <code>int </code><i>format</i> <code>int </code><i>plainformat</i> <code>int </code><i>height</i> <code>int </code><i>width</i> <code>int </code><i>depth</i> <code>sample </code><i>maxval</i> <code>int </code><i>bytes_per_sample</i> <code>char </code><i>tuple_type</i><code>[256]</code> <code>int </code><i>allocation_depth</i> <code>char **</code><i>comment_p</i><code>;</code> <code>}</code> </p>
<p> See The Libnetbm User&#8217;s Guide for information on the <code>pam</code> structure. </p>
<h2>Macros</h2>
<p> <code>PNM_MAXMAXVAL</code> is the maximum maxval that Netpbm images could historically have: 255. Many programs aren&#8217;t capable of handling Netpbm images with a maxval larger than this. It&#8217;s named this way for backward compatibility &#8212; it had this name back when it was <i>the</i> maximum maxval. </p>
<p> <code>PNM_OVERALLMAXVAL</code> is the maximum maxval that Netpbm images can have today (65535). </p>
<p> <code>PBM_FORMAT</code>, <code>RPBM_FORMAT</code>, <code>PGM_FORMAT</code>, <code>RPGM_FORMAT</code>, <code>PPM_FORMAT</code>, <code>RPPM_FORMAT</code>, and <code>PAM_FORMAT</code> are the format codes of the various Netpbm formats. <code>RPBM_FORMAT</code> is the raw PBM format and <code>PBM_FORMAT</code> is the plain PBM format, and so on. See the <i>format</i> member of the <code>pam</code> structure . </p>
<p> <code>PAM_FORMAT_TYPE(</code><i>format</i><code>)</code> gives the type of a format, given the format code. The types of formats are PBM, PGM, PPM, and PAM and macros for the type codes are, respectively, PBM_TYPE, PGM_TYPE, PPM_TYPE, and PAM_TYPE. Note that there are more format codes then there are format types because there are different format codes for the plain and raw subformats of each format. </p>
<h2>Functions</h2>
<p> These interfaces are declared in <code>pam.h</code>. </p>
<h3>Memory Management</h3>
<p> <code>Synopsis</code> </p>
<p> <code>tuple ** pnm_allocpamarray(</code> <code>struct pam *</code><i>pamP</i><code>);</code> </p>
<p> <code>tuple * pnm_allocpamrow(</code> <code>struct pam *</code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_freepamarray(</code> <code>tuple **</code><i>tuplearray</i><code>,</code> <code>struct pam *</code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_freepamrow(</code> <code>tuple *</code><i>tuplerow</i><code>);</code> </p>
<p> <code>tuple * allocpamtuple(</code> <code>struct pam *</code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_freepamtuple(</code> <code>tuple </code><i>tuple</i> <code>);</code> </p>
<p> <code>tuplen * pnm_allocpamrown(</code> <code>struct pam *</code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_freepamrown(</code> <code>tuplen *</code><i>tuplenrow</i><code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pnm_allocpamarray()</code> allocates space for an array of tuples. <code>pnm_freepamarray()</code> frees an array space allocated by <code>pnm_allocpamarray()</code> or <code>pnm_readpam()</code>. </p>
<p> <code>pnm_allocpamrow() </code> allocates space for a row of a PAM image, in basic form. <code>pnm_freepamrow()</code> frees it. </p>
<p> <code>pnm_allocpamrown()</code> is the same as <code>pnm_allocpamrow()</code> except that it allocates space for a PAM row in the normalized form. <code>pnm_freepamrown()</code> is similarly like <code>pnm_freepamrow</code>. </p>
<h3>Reading Netpbm Files</h3>
<p> <code>Synopsis</code> </p>
<p> <code>void pnm_readpaminit(</code> <code>FILE *</code><i>file</i><code>,</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>int </code><i>size</i><code>);</code> </p>
<p> <code>void pnm_readpamrow(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>tuple *</code><i>tuplerow</i><code>);</code> </p>
<p> <code>tuple ** pnm_readpam(</code> <code>FILE *</code><i>file</i><code>,</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>int </code><i>size</i><code>);</code> </p>
<p> <code>void pnm_readpamrown(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>tuplen *</code><i>tuplenrow</i><code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pnm_readpaminit()</code> reads the header of a Netpbm image. </p>
<p> See above for a general description of the <i>pamP</i> argument. </p>
<p> <code>pnm_readpaminit()</code> returns the information from the header in the <code>*</code><i>pamP</i> structure. It does not require any members of <code>*</code><i>pamP</i> through <code>tuple_type</code> to be set at invocation, and sets all of those members. It expects all members after <code>tuple_type</code> to be meaningful. </p>
<p> <i>size</i> is the size of the <code>*</code><i>pamP</i> structure as understood by the program processing the image. <code>pnm_readpaminit()</code> does not attempt to use or set any members of the structure beyond that. The point of this argument is that the definition of the structure may change over time, with additional fields being added to the end. This argument allows <code>pnm_readpaminit</code> to distinguish between a new program that wants to exploit the additional features and an old program that cannot (or a new program that just doesn&#8217;t want to deal with the added complexity). At a minimum, this size must contain the members up through <code>tuple_type</code>. You should use the <code>PAM_STRUCT_SIZE</code> macro to compute this argument. E.g. <code>PAM_STRUCT_SIZE(tuple_type)</code>. </p>
<p> <code>PAM_STRUCT_SIZE</code> was introduced in Netpbm 10.23 (July 2004). In older Netpbm, you can just use sizeof(), but then your code is <i>not</i> forward compatible at the source code level with newer libnetpbm (because when you compile it with newer libnetpbm header files, you&#8217;ll be saying your structure contains all the new members that have been invented, but your code doesn&#8217;t actually initialize them). So you might want to compute a proper size yourself. </p>
<p> The function expects to find the image file positioned to the start of the header and leaves it positioned to the start of the raster. </p>
<p> <code>pnm_readpamrow()</code> reads a row of the raster from a Netpbm image file. It expects all of the members of the <code>*pamP</code> structure to be set upon invocation and does not modify any of them. It expects to find the file positioned to the start of the row in question in the raster and leaves it positioned just after it. It returns the row as the array of tuples <i>tuplerow</i>, which must already have its column pointers set up so that it forms a C 2-dimensional array. The leftmost tuple is Element 0 of this array. </p>
<p> <code>pnm_readpam()</code> reads an entire image from a PAM or PNM image file and allocates the space in which to return the raster. It expects to find the file positioned to the first byte of the image and leaves it positioned just after the image. </p>
<p>&nbsp;<wbr>The function does not require <code>*</code><i>pamP</i> to have any of its members set and sets them all. <i>size</i> is the storage size in bytes of the <code>*</code><i>pamP</i> structure, normally <code>sizeof(struct pam)</code>. </p>
<p> The return value is a newly allocated array of the rows of the image, with the top row being Element 0 of the array. Each row is represented as <code>pnm_readpamrow()</code> would return. </p>
<p> The return value is also effectively a 3-dimensional C array of samples, with the dimensions corresponding to the height, width, and depth of the image, in that order. </p>
<p> <code>pnm_readpam()</code> combines the functions of <code>pnm_allocpamarray()</code>, <code>pnm_readpaminit()</code>, and iterations of <code>pnm_readpamrow()</code>. It may require more dynamic storage than you can afford. </p>
<p> <code>pnm_readpamrown()</code> is like <code>pnm_readpamrow()</code> except that it returns the row contents in normalized form (composed of normalized tuples (<code>tuplen</code>) instead of basic form (<code>tuple</code>). </p>
<p> <code>pnm_readpaminit()</code> and <code>pnm_readpam</code> abort the program with a message to Standard Error if the PAM or PNM image header is not syntactically valid, including if it contains a number too large to be processed using the system&#8217;s normal data structures (to wit, a number that won&#8217;t fit in a C &#8216;int&#8217;). </p>
<h3>Writing Netpbm Files</h3>
<p> <code>Synopsis</code> </p>
<p> <code>void pnm_writepaminit(</code> <code>struct pam *</code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_writepamrow(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>const tuple *</code><i>tuplerow</i><code>);</code> </p>
<p> <code>void pnm_writepam(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>const tuple * const *</code><i>tuplearray</i><code>);</code> </p>
<p> <code>void pnm_writepamrown(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>const tuplen *</code><i>tuplerown</i><code>);</code> </p>
<p> <code>void pnm_formatpamrow(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>const tuple *</code><i>tuplerow</i> <code>unsigned char * const </code><i>outbuf</i><code>,</code> <code>unsigned int * const </code><i>rowSizeP</i> <code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pnm_writepaminit()</code> writes the header of a PAM or PNM image and computes some of the fields of the pam structure. </p>
<p> See above for a description of the <i>pamP</i> argument. </p>
<p> The following members of the <code>*</code><i>pamP</i> structure must be set upon invocation to tell the function how and what to write. <code>size</code>, <code>len</code>, <code>file</code>, <code>format</code>, <code>height</code>, <code>width</code>, <code>depth</code>, <code>maxval</code>. Furthermore, if <code>format</code> is <code>PAM_FORMAT</code>, <code>tuple_type</code> must be set. </p>
<p> <code>pnm_writepaminit()</code> sets the <code>plainformat</code> and <code>bytes_per_sample</code> members based on the information supplied. </p>
<p> <code>pnm_writepamrow()</code> writes a row of the raster into a PAM or PNM image file. It expects to find the file positioned where the row should start and leaves it positioned just after the row. The function requires all the elements of <code>*</code><i>pamP</i> to be set upon invocation and doesn&#8217;t modify them. </p>
<p> <i>tuplerow</i> is an array of tuples representing the row. The leftmost tuple is Element 0 of this array. </p>
<p> <code>pnm_writepam()</code> writes an entire PAM or PNM image to a PAM or PNM image file. It expects to find the file positioned to where the image should start and leaves it positioned just after the image. </p>
<p> The following members of the <code>*</code><i>pamP</i> structure must be set upon invocation to tell the function how and what to write: <code>size</code>, <code>len</code>, <code>file</code>, <code>format</code>, <code>height</code>, <code>width</code>, <code>depth</code>, <code>maxval</code>, <code>tuple_type</code>. </p>
<p> <code>pnm_writepam()</code> sets the <code>plainformat</code> and <code>bytes_per_sample</code> members based on the information supplied. </p>
<p> <i>tuplearray</i> is an array of rows such that you would pass to <code>pnm_writepamrow()</code>, with the top row being Element 0 of the array. </p>
<p> <code>pnm_writepam()</code> combines the functions of <code>pnm_writepaminit()</code>, and iterations of <code>pnm_writepamrow()</code>. Its raster input may be more storage than you can afford. </p>
<p> <code>pnm_writepamrown()</code> is like <code>pnm_writepamrow()</code> except that it takes the row contents in normalized form (composed of normalized tuples (<code>tuplen</code>) instead of basic form (<code>tuple</code>). </p>
<p> <code>pnm_formatpamrow()</code> is like <code>pnm_writepamrow()</code>, except that instead of writing a row to a file, it places the same bytes that would go in the file in a buffer you supply. There isn&#8217;t an equivalent function to construct an image header; i.e. there is no analog to <code>pnm_writepaminit()</code>. But the header format, particularly for PAM, is so simple that you can easily build it yourself with standard C library string functions. </p>
<p> <code>pnm_formatpamrow()</code> was new in Netpbm 10.25 (October 2004). </p>
<h3>Transforming Pixels</h3>
<p> <code>Synopsis</code> </p>
<p> <code>void pnm_YCbCrtuple(</code> <code>tuple </code><i>tuple</i><code>,</code> <code>double *</code><i>YP</i><code>,</code> <code>double *</code><i>CrP</i><code>,</code> <code>double *</code><i>CbP</i><code>);</code> </p>
<p> <code>void pnm_YCbCr_to_rgbtuple(</code> <code>const struct pam * const </code><i>pamP</i><code>,</code> <code>tuple const </code><i>tuple</i><code>,</code> <code>double const </code><i>Y</i><code>,</code> <code>double const </code><i>Cb</i><code>,</code> <code>double const </code><i>Cr</i><code>,</code> <code>int * const </code><i>overflowP</i><code>);</code> </p>
<p> <code>extern double pnm_lumin_factor[3];</code> </p>
<p> <code>void pnm_normalizetuple(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>tuple const </code><i>tuple</i><code>,</code> <code>tuplen const </code><i>tuplen</i><code>);</code> </p>
<p> <code>void pnm_unnormalizetuple(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>tuplen const </code><i>tuplen</i><code>,</code> <code>tuple const </code><i>tuple</i><code>);</code> </p>
<p> <code>void pnm_normalizeRow(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>const tuple * const </code><i>tuplerow</i><code>,</code> <code>pnm_transformMap * const </code><i>transform</i><code>,</code> <code>tuplen * const </code><i>tuplenrow</i><code>);</code> </p>
<p> <code>void pnm_unnormalizeRow(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>const tuplen * const </code><i>tuplenrow</i><code>,</code> <code>pnm_transformMap * const </code><i>transform</i><code>,</code> <code>tuple * const </code><i>tuplerow</i><code>);</code> </p>
<p> <code>void pnm_gammarown(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>tuplen * const </code><i>row</i><code>);</code> </p>
<p> <code>void pnm_ungammarown(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>tuplen * const </code><i>row</i><code>);</code> </p>
<p> <code>void pnm_applyopacityrown(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>tuplen * const </code><i>tuplenrow</i><code>);</code> </p>
<p> <code>void pnm_unapplyopacityrown(</code> <code>struct pam * const </code><i>pamP</i><code>,</code> <code>tuplen * const </code><i>tuplenrow</i><code>);</code> </p>
<p> <code>pnm_transformMap * pnm_creategammatransform(</code> <code>const struct pam * const </code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_freegammatransform(</code> <code>const pnm_transformMap * const </code><i>transform</i><code>,</code> <code>const struct pam * const </code><i>pamP</i><code>);</code> </p>
<p> <code>pnm_transformMap * pnm_createungammatransform(</code> <code>const struct pam * const </code><i>pamP</i><code>);</code> </p>
<p> <code>void pnm_freeungammatransform(</code> <code>const pnm_transformMap * const </code><i>transform</i><code>,</code> <code>const struct pam * const </code><i>pamP</i><code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pnm_YCbCrtuple()</code> returns the Y/Cb/Cr luminance/chrominance representation of the color represented by the input tuple, assuming that the tuple is an RGB color representation (which is the case if it was read from a PPM image). The output components are based on the same scale (maxval) as the input tuple, but are floating point nonetheless to avoid losing information due to rounding. Divide them by the maxval to get normalized [0..1] values. </p>
<p> <code>pnm_YCbCr_to_rgbtuple()</code> does the reverse. <i>pamP</i> indicates the maxval for the returned <i>tuple</i>, and the <i>Y</i>, <i>Cb</i>, and <i>Cr</i> arguments are of the same scale. </p>
<p> It is possible for <i>Y</i>, <i>Cb</i>, and <i>Cr</i> to describe a color that cannot be represented in RGB form. In that case, <code>pnm_YCbCr_to_rgbtuple()</code> chooses a color as close as possible (by clipping each component to 0 and the maxval) and sets *overflowP true. It otherwise sets *overflowP false. </p>
<p> <code>pnm_lumin_factor[]</code> is the factors (weights) one uses to compute the intensity of a color (according to some standard &#8212; I don&#8217;t know which). pnm_lumin_factor[0] is for the red component, [1] is for the green, and [2] is for the blue. They add up to 1. </p>
<p> <code>pnm_gammarown()</code> and <code>pnm_ungammarown()</code> apply and unapply gamma correction to a row of an image using the same transformation as <code>pm_gamma709()</code> and <code>pm_ungamma709()</code> . Note that these operate on a row of normalized tuples (<code>tuplen</code>, not <code>tuple</code>). </p>
<p> <code>pnm_applyopacityrown()</code> reduces the intensity of samples in accordance with the opacity plane of an image. The opacity plane, if it exists, tells how much of the light from that pixel should show when the image is composed with another image. You use <code>pnm_applyopacityrown()</code> in preparation for doing such a composition. For example, if the opacity plane says that the left half of the image is 50% opaque and the right half 100% opaque, <code>pnm_applyopacityrown()</code> will reduce the intensity of each sample of each tuple (pixel) in the left half of the image by 50%, and leave the rest alone. </p>
<p> If the image does not have an opacity plane (i.e. its tuple type is not one that <code>libnetpbm</code> recognizes as having an opacity plane), <code>pnm_applyopacityrown()</code> does nothing (which is the same as assuming opacity 100%). The tuple types that <code>libnetpbm</code> recognizes as having opacity are <code>RGB_ALPHA</code> and <code>GRAYSCALE_ALPHA</code>. </p>
<p> <code>pnm_unapplyopacityrown()</code> does the reverse. It assumes the intensities are already reduced according to the opacity plane, and raises back to normal. </p>
<p> <code>pnm_applyopacityrown()</code> works on (takes as input and produces as output) <i>normalized</i>, <i>intensity-proportional</i> tuples. That means you will typically read the row from the image file with <code>pnm_readpamrown()</code> and then gamma-correct it with <code>pnm_ungammarown()</code>, and then do <code>pnm_applyopacityrown()</code>. You then manipulate the row further (perhaps add it with other rows you&#8217;ve processed similarly), then do <code>pnm_unapplyopacityrown()</code>, then <code>pnm_gammarown()</code>, then <code>pnm_writepamrown()</code>. </p>
<p> <code>pnm_applyopacityrown()</code> and <code>pnm_unapplyopacityrown()</code> were new in Netpbm 10.25 (October 2004). </p>
<p> <code>pnm_normalizetuple()</code> and <code>pnm_unnormalizetuple()</code> convert between a <code>tuple</code> data type and a <code>tuplen</code> data type. The former represents a sample value using the same unsigned integer that is in the PAM image, while the latter represents a sample value as a number scaled by the maxval to the range 0..1. I.e. <code>pnm_normalizetuple()</code> divides every sample value by the maxval and <code>pnm_unnormalizetuple()</code> multiples every sample by the maxval. </p>
<p> <code>pnm_normalizeRow()</code> and <code>pnm_unnormalizeRow()</code> do the same thing on an entire tuple row, but also have an extra feature: You can specify a transform function to be applied in addition. Typically, this is a gamma transform function. You can of course more easily apply your transform function separately from normalizing, but doing it all at once is usually way faster. Why? Because you can use a lookup table that is indexed by an integer on one side and produces a floating point number on the other. To do it separately, you&#8217;d either have to do floating point arithmetic on the normalized value or do the transform on the integer values and lose a lot of precision. </p>
<p> If you don&#8217;t have any transformation to apply, just specify <code>NULL</code> for the <i>transform</i> argument and the function will just normalize (i.e. divide or multiply by the maxval). </p>
<p> Here&#8217;s an example of doing a transformation. The example composes two images together, something that has to be done with intensity-linear sample values. </p>
<pre><code>
pnm_transformMap *const transform1 = pnm_createungammatransform(&amp;inpam1);
pnm_transformMap *const transform2 = pnm_createungammatransform(&amp;inpam2);
pnm_transformMap *const transformOut = pnm_creategammatransform(&amp;outpam);
pnm_readpamrow(&amp;inpam1, inrow1);
pnm_readpamrow(&amp;inpam2, inrow2);
pnm_normalizeRow(&amp;inpam1, inrow1, transform1, normInrow1);
pnm_normalizeRow(&amp;inpam2, inrow2, transform2, normInrow2);
for (col = 0; col &lt; outpam.width; ++col)
    normOutrow[col] = (normInrow1[col] + normInrow2[col]) / 2;
pnm_unnormalizeRow(&amp;outpam, normOutrow, transformOut, outrow);
pnm_writepamrow(&amp;outpam, outrow);
</code></pre>
<p> To specify a transform, you must create a special <code>pnm_transformMap</code> object and pass it as the <i>transform</i> argument. Typically, your transform is a gamma transformation because you want to work in intensity-proportional sample values and the PAM image format uses gamma-adjusted ones. In that case, just use <code>pnm_creategammatransform()</code> and <code>pnm_createungammatransform()</code> to create this object and don&#8217;t worry about what&#8217;s inside it. </p>
<p> <code>pnm_creategammatransform()</code> and <code>pnm_createungammatransform()</code> create objects that you use with <code>pnm_normalizeRow()</code> and <code>pnm_unnormalizeRow()</code> as described above. The created object describes a transform that applies or reverses the ITU-R Recommendation BT.709 gamma adjustment that is used in PAM visual images and normalizes or unnormalizes the sample values. </p>
<p> <code>pnm_freegammatransform()</code> and <code>pnm_freeungammatransform()</code> destroy the objects. </p>
<h3>Miscellaneous</h3>
<p> <code>Synopsis</code> </p>
<p> <code>void pnm_checkpam(</code> <code>struct pam *</code><i>pamP</i><code>,</code> <code>const enum pm_check_type </code><i>check_type</i><code>,</code> <code>enum pm_check_code *</code><i>retvalP</i><code>);</code> </p>
<p> <code>void pnm_nextimage(</code> <code>FILE *</code><i>file</i><code>,</code> <code>int * const </code><i>eofP</i><code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pnm_checkpam()</code> checks for the common file integrity error where the file is the wrong size to contain the raster, according to the information in the header. </p>
<p> <code>pnm_nextimage()</code>positions a Netpbm image input file to the next image in it (so that a subsequent <code>pnm_readpaminit()</code> reads its header). </p>
<h2>Index</h2>
