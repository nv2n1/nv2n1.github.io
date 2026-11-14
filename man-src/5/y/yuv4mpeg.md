---
title: "yuv4mpeg(5)"
name: "yuv4mpeg"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yuv4mpeg/"
description: "YUV4MPEG2 – video stream format used by pipe-based MJPEGtools"
---

<p>YUV4MPEG2 &#8211; video stream format used by pipe-based MJPEGtools</p>
<h2>Description</h2>
<p>Many of the MJPEGtools communicate via pipes and act as filters (or sources or sinks). The format of video data used in the pipes is referred to as &quot;YUV4MPEG&quot;, or, more precisely, &quot;YUV4MPEG2&quot;. (The format was extended and codified during v1.5.x of the tools.) The basic structure is a stream header followed by an unlimited number of frames. Each frame itself consists of a header followed by video data. The headers are vaguely human-readable ASCII, but the video data is simple byte-size binary. The MJPEGtools distribution has a C library (libmjpegutils) which contains functions for manipulating YUV4MPEG2 streams. We recommend that you use this library rather than writing your own code if possible. See the header file &quot;yuv4mpeg.h&quot; for a description of these functions. Design Goals:</p>
<dl>
<dt>o</p>
<dd>Easy to parse both via C or sh.</p>
<dt>o</p>
<dd>Extensible; easy to add new parameters while maintaining backwards compatibility.</p>
<dt>o</p>
<dd>Simple upgrade from original &quot;YUV4MPEG&quot; format.</dl>
<p> Drawbacks:</p>
<dl>
<dt>o</p>
<dd>Frame headers do not have constant size, so streams are not seekable. </p>
<h2>Grammar</h2>
<p>The precise description of the the YUV4MPEG2 stream format is as follows: </p>
<p> <i>STREAM</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd>one <i>STREAM-HEADER</i></p>
<dt>&#8211;</p>
<dd>unlimited number of <i>FRAME</i>s</dl>
<p> <i>STREAM-HEADER</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd>magic string &quot;YUV4MPEG2&quot;</p>
<dt>&#8211;</p>
<dd>unlimited number of <i>TAGGED-FIELD</i>s, each preceeded by a &#8216;&nbsp;<wbr>&#8216; (single space) separator</p>
<dt>&#8211;</p>
<dd>single &#8216;
&#8217; line terminator </p>
</dl>
<p> <i>FRAME</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd>one <i>FRAME-HEADER</i></p>
<dt>&#8211;</p>
<dd>&quot;length&quot; octets of planar YCbCr 4:2:0 image data (If the stream is interlaced, then the two fields per frame are interleaved, with proper spatial ordering.)</dl>
<p> <i>FRAME-HEADER</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd>magic string &quot;FRAME&quot;</p>
<dt>&#8211;</p>
<dd>unlimited number of <i>TAGGED-FIELD</i>s, each preceeded by a &#8216;&nbsp;<wbr>&#8216; (single space) separator</p>
<dt>&#8211;</p>
<dd>single &#8216;
&#8217; line terminator </p>
</dl>
<p> <i>TAGGED-FIELD</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd>single ASCII character tag</p>
<dt>&#8211;</p>
<dd><i>VALUE</i> (which does not contain whitespace)</dl>
<p> <i>VALUE</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd><i>RATIO</i>, <code>or</code></p>
<dt>&#8211;</p>
<dd>integer (base 10 ASCII representation), <code>or</code></p>
<dt>&#8211;</p>
<dd>single ascii character, <code>or</code></p>
<dt>&#8211;</p>
<dd>string (multiple ASCII characters) </p>
</dl>
<p> <i>RATIO</i> consists of</p>
<dl>
<dt>&#8211;</p>
<dd>numerator (base 10 ASCII integer)</p>
<dt>&#8211;</p>
<dd>&#8216;:&#8217; (a colon)</p>
<dt>&#8211;</p>
<dd>denominator (base 10 ASCII integer) </p>
</dl>
<p> Header tags fall into three categories: <code>optional</code>, <code>required</code> and <code>has-default</code>. Optional tags are completely optional and may be omitted from a header. Required tags must be present in a header. Has-Default tags have a default value which is implied if the tag is not present. Independent of these categories, some tags allow an &quot;unknown&quot; value and some do not. </p>
<p> The supported tags for the <i>STREAM-HEADER</i>:</p>
<dl>
<dd>
<dl>
<dd>W[integer]&nbsp;<wbr>&#8211; frame width in pixels, must be &gt; 0 (<code>required</code>)</p>
<dd>H[integer]&nbsp;<wbr>&#8211; frame height in pixels, must be &gt; 0 (<code>required</code>)</p>
<dd>C[string]&nbsp;<wbr>&#8211; chroma subsampling, image data format (<code>has default</code>)</p>
<dl>
<dd>&nbsp;<wbr>420jpeg&nbsp;<wbr>&nbsp;<wbr>&#8211; 4:2:0 with JPEG/MPEG-1 siting&nbsp;<wbr>(default)<br />
&nbsp;<wbr>420mpeg2 &#8211; 4:2:0 with MPEG-2 siting<br />
&nbsp;<wbr>420paldv &#8211; 4:2:0 with PAL-DV siting<br />
&nbsp;<wbr>411&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 4:1:1, cosited<br />
&nbsp;<wbr>422&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 4:2:2, cosited<br />
&nbsp;<wbr>444&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 4:4:4&nbsp;<wbr>(no subsampling)<br />
&nbsp;<wbr>444alpha &#8211; 4:4:4 with an alpha channel<br />
&nbsp;<wbr>mono&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; luma&nbsp;<wbr>(Y&#8217;)&nbsp;<wbr>plane only</dl>
<dd>I[char]&nbsp;<wbr>&#8211; interlacing specification: (<code>has default</code>)</p>
<dl>
<dd>&nbsp;<wbr>?&nbsp;<wbr>&#8211; unknown&nbsp;<wbr>(default)<br />
&nbsp;<wbr>p &#8211; progressive/none<br />
&nbsp;<wbr>t &#8211; top-field-first<br />
&nbsp;<wbr>b &#8211; bottom-field-first<br />
&nbsp;<wbr>m &#8211; mixed-mode: refer to&nbsp;<wbr>&#8216;I&#8217;&nbsp;<wbr>tag in frame header</dl>
<dd>F[ratio]&nbsp;<wbr>&#8211; frame-rate (<code>has default</code> of 0:0 == unknown)</p>
<dd>A[ratio]&nbsp;<wbr>&#8211; sample aspect ratio (<code>has default</code> of 0:0 == unknown)</p>
<dd>X[string]&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;metadata&#8217; (<code>optional</code>; unparsed, but passed around)</dl>
</dl>
<p> The currently supported tags for the <i>FRAME-HEADER</i>:</p>
<dl>
<dd>
<dl>
<dd>I[string]&nbsp;<wbr>&#8211; framing and sampling (<code>required if-and-only-if</code> Im is present in stream header). Value is a string of three characters &quot;xyz&quot; which have the following meanings:</p>
<dl>
<dd>&nbsp;<wbr>x: frame presentation<br />
&nbsp;<wbr>t &#8211; top-field-first<br />
&nbsp;<wbr>T &#8211; top-field-first and repeat<br />
&nbsp;<wbr>b &#8211; bottom-field-first<br />
&nbsp;<wbr>B &#8211; bottom-field-first and repeat<br />
&nbsp;<wbr>1 &#8211; single progressive frame<br />
&nbsp;<wbr>2 &#8211; double progressive frame&nbsp;<wbr>(repeat)<br />
&nbsp;<wbr>3 &#8211; triple progressive frame&nbsp;<wbr>(repeat)<br />
&nbsp;<wbr>y: frame temporal sampling<br />
&nbsp;<wbr>p &#8211; progressive&nbsp;<wbr>(fields sampled at same time)<br />
&nbsp;<wbr>i &#8211; interlaced&nbsp;<wbr>(fields sampled at different times)<br />
&nbsp;<wbr>z: frame chroma-subsampling<br />
&nbsp;<wbr>p &#8211; progressive&nbsp;<wbr>(subsampling over whole frame)<br />
&nbsp;<wbr>i &#8211; interlaced&nbsp;<wbr>(each field subsampled independently)<br />
&nbsp;<wbr>?&nbsp;<wbr>&#8211; unknown&nbsp;<wbr>(allowed only for non-4:2:0 subsampling)</dl>
<dd>X[string]&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;metadata&#8217; (<code>optional</code>; unparsed, but passed around)</dl>
</dl>
<p> Note that a filter application must faithfully forward all &quot;X&quot; tags from input pipe to output pipe (unless it uses one of those tags, of course). The supplied library will do this automatically if the functions y4m_copy_stream_info() and y4m_copy_frame_info() are used appropriately.</p>
<h2>Notes On Image Data</h2>
<p>All image data is in the CCIR-601 Y&#8217;CbCr colorspace, presented plane-by-plane in row-major order. Each sample within each plane is one octet (8-bits) in size. When all planes are present, they are transmitted in the order Y&#8217;, Cb, Cr, potentially followed by an alpha/transparency mask plane (for the <code>444alpha</code> chroma format). The alpha channel data is follows the same range as the Y&#8217; luma channel: full transparency is at 16 and full opacity is at 235. </p>
<p> All Y&#8217; and alpha planes consist of (height X width) octets. The size of the chroma planes depends on the subsampling mode:</p>
<dl>
<dt>&#8211;</p>
<dd>4:4:4 &#8211; (height X width) octets</p>
<dt>&#8211;</p>
<dd>4:2:2 &#8211; (height X width)&nbsp;<wbr>/&nbsp;<wbr>2 octets</p>
<dt>&#8211;</p>
<dd>4:1:1 &#8211; (height X width)&nbsp;<wbr>/&nbsp;<wbr>4 octets</p>
<dt>&#8211;</p>
<dd>4:2:0 &#8211; (height X width)&nbsp;<wbr>/&nbsp;<wbr>4 octets </p>
</dl>
<h2>Notes On Framing</h2>
<p>(More to come here.)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), yuv4mpeg.h </p>
<h2>Author</h2>
<p>This manual page Copyright 2004 Matthew J. Marjanovic.</p>
