---
title: "xvlistimageformats(3)"
name: "xvlistimageformats"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvlistimageformats/"
description: "XvListImageFormats – return list of image formats supported by a video port"
---

<p>XvListImageFormats &#8211; return list of image formats supported by a video port</p>
<h2>Syntax</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>XvImageFormatValues * XvListImageFormats (Display *</code><i>dpy</i><code>,</code>
<code> XvPortID </code><i>port</i><code>, int *</code><i>p_num_formats</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port whose adaptor is to be queried for its list of attributes.</p>
<dt><i>p_num_formats</i></p>
<dd>A pointer to where the number of formats returned in the array is written.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvlistimageformats/">XvListImageFormats</a></code>(3) returns the XvImageFormatValues supported by the specified port. This list should be freed with <code><a href="/docs/linux/man/3-xfree/">XFree</a></code>(3).</p>
<h2>Return Values</h2>
<p>XvImageFormatValues has the following structure: </p>
<p>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br />
int id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Unique descriptor for the format&nbsp;<wbr>*/<br />
int type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>XvRGB, XvYUV&nbsp;<wbr>*/<br />
int byte_order;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>LSBFirst, MSBFirst&nbsp;<wbr>*/<br />
char guid[16];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Globally Unique IDentifier&nbsp;<wbr>*/<br />
int bits_per_pixel;<br />
int format;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>XvPacked, XvPlanar&nbsp;<wbr>*/<br />
int num_planes; </p>
<p>/*&nbsp;<wbr>for RGB formats&nbsp;<wbr>*/<br />
int depth;<br />
unsigned int red_mask;<br />
unsigned int green_mask;<br />
unsigned int blue_mask; </p>
<p>/*&nbsp;<wbr>for YUV formats&nbsp;<wbr>*/<br />
unsigned int y_sample_bits;<br />
unsigned int u_sample_bits;<br />
unsigned int v_sample_bits;<br />
unsigned int horz_y_period;<br />
unsigned int horz_u_period;<br />
unsigned int horz_v_period;<br />
unsigned int vert_y_period;<br />
unsigned int vert_u_period;<br />
unsigned int vert_v_period;<br />
char component_order[32];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>eg. UYVY&nbsp;<wbr>*/<br />
int scanline_order;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>XvTopToBottom, XvBottomToTop&nbsp;<wbr>*/<br />
&nbsp;<wbr>}&nbsp;<wbr>XvImageFormatValues; </p>
<dl COMPACT>
<dt><i>id</i></p>
<dd>A unique descriptor for the format. This is often the FOURCC for the format, when applicable. This id is used to describe the format during XvImage creation.</p>
<dt><i>type</i></p>
<dd>XvRGB or XvYUV.</p>
<dt><i>byte_order</i></p>
<dd>The byte order of the image. It is either LSBFirst or MSBFirst.</p>
<dt><i>guid</i></p>
<dd>The Globally Unique IDentifier (also known as Universally Unique IDentifier). When not applicable, all characters are NULL.</p>
<dt><i>bits_per_pixel</i></p>
<dd>The bits taken up (but not necessarily used) by each pixel. Note that for some planar formats which have fractional bits per pixel (such as IF09) this number may be rounded _down_.</p>
<dt><i>format</i></p>
<dd>XvPacked or XvPlanar.</p>
<dt><i>num_planes</i></p>
<dd>The number of planes in planar formats.</p>
<dt><i>depth</i></p>
<dd>Significant bits per pixel.</p>
<dt><i>red_mask, green_mask, blue_mask</i></p>
<dd>The red, green and blue bitmasks (RGB formats only).</p>
<dt><i>?_sample_bits</i></p>
<dd>The size of each sample in bits (YUV formats only).</p>
<dt><i>horz_?_period, vert_?_period</i></p>
<dd>The period (in pixels) on which samples occur in the horizontal and vertical directions (YUV formats only).</p>
<dt><i>component_order</i></p>
<dd>Upper case ascii characters representing the order that samples are stored within packed formats. For planar formats this represents the ordering of the planes.</p>
<dt><i>scanline_order</i></p>
<dd>XvTopToBottom or XvBottomToTop.</dl>
<h2>Notes</h2>
<p>Since some formats (particularly some planar YUV formats) may not be completely defined by the parameters above, the guid, when available, should provide the most accurate description of the format.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvcreateimage/">XvCreateImage</a></code>(3), <code><a href="/docs/linux/man/3-xvcreateshmimage/">XvCreateShmImage</a></code>(3)</p>
