---
title: "y4mscaler(1)"
name: "y4mscaler"
section: "1"
letter: "y"
url: "/docs/linux/man/1-y4mscaler/"
description: "y4mscaler – Scale/crop/translate a YUV4MPEG2 stream"
---

<h2 class="name">NAME</h2>
<p> y4mscaler &#8211; Scale/crop/translate a YUV4MPEG2 stream</p>
<h2>SYNOPSIS</h2>
<p> <code>y4mscaler</code> [<i>options</i>] <i>&lt; Y4Mstream &gt; Y4Mstream</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>y4mscaler</code> is a general-purpose video scaler which operates on YUV4MPEG2 streams, as produced and consumed by the MJPEGtools such as <code>lav2yuv</code> and <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1). </p>
<p> <code>y4mscaler</code> is meant to be used in a pipeline. Thus, input is from stdin, and output is to stdout. </p>
<p> The essential function of <code>y4mscaler</code> is to scale a specified &quot;active&quot; region of the input stream (the source) into a specified active region of the output stream (the target). Pixels outside of the active region of the source are ignored; pixels outside of the active region of the target are filled with a background color. The source may additionally have a matte applied to it; pixels outside the source matte are set to a separately specified background color. </p>
<p> <code>y4mscaler</code> correctly handles chroma subsampling, and thus it can also perform chroma subsampling conversions. The YUV4MPEG2 stream format supports three varieties of 4:2:0 subsampling, as well as 4:1:1, 4:2:2, 4:4:4, a 4:4:4 modes with an alpha channel, and a monochrome luma-only mode. (See &quot;NOTES ON CHROMA MODES AND SUBSAMPLING&quot;.) </p>
<p> <code>y4mscaler</code> can perform simple interlacing conversions: switching from top-field-first to bottom-field-first and vice-versa (by lossily discarding the first field), and creating a progressive stream from interlaced by discarding every other field (effectively halving the vertical resolution). </p>
<p> The source and target are defined by many, many parameters, but <code>y4mscaler</code> has many, many heuristics built-in to automagically set them appropriately. Most source parameters are taken from the input stream header. Remaining source and target parameters which are not specified by the user are guessed in a sane manner. </p>
<p> <code>y4mscaler</code> includes preset parameters for a number of common target streams: DVD, VideoCD (VCD), SuperVCD (SVCD), associated still image formats, and DV. </p>
<h2>EXAMPLES</h2>
<p> To create a stream appropriate for use in an SVCD: </p>
<dl>
<dt>
<dd> y4mscaler -O preset=svcd</dl>
<p> To create a stream for a VideoCD (a non-interlaced format), from a DV source (an interlaced format), shifting the input frame 4 pixels to the left: </p>
<dl>
<dt>
<dd> y4mscaler -I ilace=bottom-only -I active=-4+0cc -O preset=vcd</dl>
<p> To take a widescreen NTSC DV source, and convert it to a letterboxed stream, with blue bars on the top and bottom: </p>
<dl>
<dt>
<dd> y4mscaler -O sar=ntsc -O bg=RGB:0,0,255</dl>
<p> To take a widescreen NTSC DV source, and convert it to a &quot;fullscreen&quot; stream (i.e. the sides are clipped, just like on TV): </p>
<dl>
<dt>
<dd> y4mscaler -O sar=ntsc -O infer=clip</dl>
<p> To take a centered, letterboxed NTSC source, and convert it to a widescreen (16:9) format stream for DVD, with the black bars removed: </p>
<dl>
<dt>
<dd> y4mscaler -O preset=dvd -O sar=ntsc_wide -O infer=clip</dl>
<p> To take the center 100&#215;100 pixel chunk of an NTSC DV stream, surround it with a 20-pixel blue border, and blow that up to a full-screen SuperVCD stream: </p>
<dl>
<dt>
<dd> y4mscaler -I active=140&#215;140+0+0cc -I matte=100&#215;100+0+0cc -I bg=RGB:0,0,255 -O preset=svcd</dl>
<h2>OPTIONS</h2>
<p> The first three options, -v, -V, and -h, are simple straightforward options which take either no arguments or one numeric argument.</p>
<dl>
<dt><code>-v</code><i> [0,1,2]</i></p>
<dd> Set verbosity level.<br />
&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>warnings and errors only.<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>add informative messages, too&nbsp;<wbr>(default).<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>add chatty debugging message, too. </p>
<dt><code>-V</code></p>
<dd> Show version information and exit. </p>
<dt><code>-h</code></p>
<dd> Show a help message (synopsis of options). </p>
</dl>
<p> The -I, -O, and -S options each take one argument of the form <i>parameter=value,</i> which specify parameters for the input, output, and scaling, respectively. These options can be used repeatedly to specify multiple parameters. The parameter names and values are not case-sensitive. Definitions of the form &quot;parameter=[AAA|BBB|CCC]&quot; mean that only one of the listed keywords AAA, BBB, or CCC may be chosen. Succeeding options will override earlier ones. </p>
<dl>
<dt><code>-I</code><i> input_parameter</i></p>
<dd>
<dl>
<dt>
<dd> Specify parameters for the source/input stream. All &#8216;-I&#8217; arguments are evaluated in order, and later arguments on the command-line will override earlier ones. All &#8216;-I&#8217; arguments are evaluated before any &#8216;-O&#8217; arguments.</p>
<dl>
<dt><code>active=</code><i>WxH+X+Yaa</i></p>
<dd> Specify the active region of the source frame, which is scaled to fit the active region of the target frame. The default is the full frame. (The &quot;WxH&quot; may be omitted, and the region size defaults to the size of of the source frame.) W and H are width and height. X and Y are the offset of the anchor point. &quot;aa&quot; is the anchor mode (default: TL); see &quot;NOTES ON REGION GEOMETRY&quot; for details.<br />
 Example: active=200&#215;180+30+24cc</p>
<dt><code>matte=</code><i>WxH+X+Y</i></p>
<dd> Specify a matte region for the source frame. All pixels outside of this region are set to the source background color. The default matte is the full frame. (The &quot;WxH&quot; may be omitted, and the region size defaults to the size of of the source frame.) W and H are width and height. X and Y are the offset of the anchor point. &quot;aa&quot; is the anchor mode (default: TL); see &quot;NOTES ON REGION GEOMETRY&quot; for details.<br />
 Example: matte=200&#215;180+30+24cc</dl>
<p> <code>bg=</code><i>RGB:r,g,b</i><br />
 <code>bg=</code><i>YCBCR:y,cb,cr</i><br />
 <code>bg=</code><i>RGBA:r,g,b,a</i><br />
 <code>bg=</code><i>YCBCRA:y,cb,cr,a</i></p>
<dl>
<dt>
<dd> Set the source background color. Pixels outside of the source&#8217;s matte region are set to this color. One can specify the color as either a R&#8217;G&#8217;B&#8217; or Y&#8217;CbCr triplet. For example, the default color is black, specified as &quot;bg=YCBCR:16,128,128&quot; or &quot;bg=RGB:0,0,0&quot;. The &#8216;A&#8217; versions will set the alpha (transparency) value of the color. The alpha range is [0,255] for RGBA and [16,235] for YCBCRA. The default is fully-opaque (255 for RGBA, 235 for YCBCRA).</dl>
<dl>
<dt><code>norm=</code>[<code>NTSC</code>|<code>PAL</code>|<code>SECAM</code>]</p>
<dd> Specify the &quot;norm&quot; of the source stream. This is normally inferred from the stream header.</p>
<dt><code>ilace=</code>[<code>NONE</code>|<code>TOP_FIRST</code>|<code>BOTTOM_FIRST</code>|<code>TOP_ONLY</code>|<code>BOTTOM_ONLY</code>]</p>
<dd> Specify the interlacing used by the source stream. NONE, TOP_FIRST, and BOTTOM_FIRST correspond to non-interlaced, top-field-first, and bottom-field-first. These values are normally inferred from the stream header; specifying them will override the stream header.<br />
 TOP_ONLY and BOTTOM_ONLY specify that only the top or bottom field of each frame should be used; the other field is discarded. These options can only be used with an interlaced input, and cause the interlaced stream to be treated as a progressive stream with half the height. (This is particularly useful in creating a VCD from a full-size interlaced input stream.) These two special options can only be used when the source is a pure progressive stream (as opposed to a YUV4MPEG2 &quot;mixed-mode&quot; stream).</p>
<dt><code>chromass=</code>[<code>420JPEG</code>|<code>420MPEG2</code>|<code>420PALDV</code>|<code>444</code>|<code>422</code>|<code>411</code>|<code>mono</code>|<code>444alpha</code>]</p>
<dd> Specify the chroma subsampling mode used in the source stream. This parameter is inferred from the stream header, so this keyword should almost never be used in a source specification. The only useful reason to specify this keyword is to override one variety of 4:2:0 with another. Any other use will cause processing to fail.</dl>
<p> <code>sar=</code><i>N:D</i><br />
 <code>sar=</code>[<code>NTSC</code>|<code>PAL</code>|<code>NTSC_WIDE</code>|<code>PAL_WIDE</code>]</p>
<dl>
<dt>
<dd> Specify the sample-aspect-ratio of the source stream. The value can either be or numeric ratio (such as &quot;10:11&quot;) or one of the keywords, which correspond to the CCIR-601 values for 4:3 or 16:9 displays, respectively. This parameter is usually inferred from the stream header.</dl>
</dl>
<dt><code>-O</code><i> output_parameter</i></p>
<dd>
<dl>
<dt>
<dd> Specify parameters for the destination/output stream. All &#8216;-O&#8217; arguments are evaluated in order, and later arguments on the command-line will override earlier ones. All &#8216;-O&#8217; arguments are evaluated after any &#8216;-I&#8217; arguments. </p>
<p> <code>size=</code><i>WxH</i><br />
 <code>size=SRC</code></p>
<dl>
<dt>
<dd> Set the output/target frame size, as width W and height H in pixels. Use the keyword <code>SRC</code> to specify that the target frame size should match the source frame size.</dl>
<dl>
<dt><code>active=</code><i>WxH+X+Yaa</i></p>
<dd> Specify the active region of the target frame, into which the active region of the source frame is scaled. The default is the full target frame. (The &quot;WxH&quot; may be omitted, and the region size defaults to the size of of the target frame.) W and H are width and height. X and Y are the offset of the anchor point. &quot;aa&quot; is the anchor mode (default: TL); see &quot;NOTES ON REGION GEOMETRY&quot; for details.<br />
 Example: active=200&#215;180+30+24cc</dl>
<p> <code>bg=</code><i>RGB:r,g,b</i><br />
 <code>bg=</code><i>YCBCR:y,cb,cr</i><br />
 <code>bg=</code><i>RGBA:r,g,b,a</i><br />
 <code>bg=</code><i>YCBCRA:y,cb,cr,a</i></p>
<dl>
<dt>
<dd> Set the target background color. Pixels outside of the target&#8217;s active region are set to this color. One can specify the color as either a R&#8217;G&#8217;B&#8217; or Y&#8217;CbCr triplet. For example, the default color is black, specified as &quot;bg=YCBCR:16,128,128&quot; or &quot;bg=RGB:0,0,0&quot;. The &#8216;A&#8217; versions will set the alpha (transparency) value of the color. The alpha range is [0,255] for RGBA and [16,235] for YCBCRA. The default is fully-opaque (255 for RGBA, 235 for YCBCRA).</dl>
<dl>
<dt><code>ilace=</code>[<code>NONE</code>|<code>TOP_FIRST</code>|<code>BOTTOM_FIRST</code>]</p>
<dd> Specify the interlacing used by the target stream. NONE, TOP_FIRST, and BOTTOM_FIRST correspond to non-interlaced, top-field-first, and bottom-field-first. The default if to match the source stream.<br />
 If the source and target are both interlaced, but with different modes (i.e. one is bottom-first, and the other is top-first), then <code>y4mscaler</code> will convert one mode to the other by dropping the first source field.</p>
<dt><code>chromass=</code>[<code>420JPEG</code>|<code>420MPEG2</code>|<code>420PALDV</code>|<code>444</code>|<code>422</code>|<code>411</code>|<code>mono</code>|<code>444alpha</code>]</p>
<dd> Specify the chroma subsampling mode to be used in the target stream. The default is to match the source mode. See &quot;NOTES ON CHROMA MODES AND SUBSAMPLING&quot; for more information.</dl>
<p> <code>sar=</code><i>N:D</i><br />
 <code>sar=</code>[<code>SRC</code>|<code>NTSC</code>|<code>PAL</code>|<code>NTSC_WIDE</code>|<code>PAL_WIDE</code>]</p>
<dl>
<dt>
<dd> Specify the sample-aspect-ratio of the source stream. The value can either be or numeric ratio (such as &quot;10:11&quot;) or one of the keywords, which correspond to the CCIR-601 values for 4:3 or 16:9 displays, respectively. The keyword <code>SRC</code> specifies that the target SAR should match the source.</dl>
<p> <code>scale=</code><i>N/D</i><br />
 <code>Xscale=</code><i>N/D</i><br />
 <code>Yscale=</code><i>N/D</i></p>
<dl>
<dt>
<dd> Set the scaling ratios, as a fraction; for example, scale=1/2. &quot;scale=&quot; sets both X and Y factors simultaneously. &quot;Xscale=&quot; and &quot;Yscale=&quot; can be used to set them independently.</dl>
<dl>
<dt><code>infer=</code>[<code>PAD</code>|<code>CLIP</code>|<code>PRESERVE_X</code>|<code>PRESERVE_Y</code>]</p>
<dd> Set the mode used to infer scaling ratios from active regions and SAR&#8217;s. The keywords are mutually exclusive. The default is PAD.</p>
<dt><code>infer=</code>[<code>SIMPLIFY</code>|<code>EXACT</code>]</p>
<dd> Set whether the above heuristic uses exact ratios, or whether it is allowed to slightly adjust active regions to simplify the scaling ratios. The keywords are mutually exclusive. The default is SIMPLIFY.</p>
<dt><code>align=</code>[<code>TL</code>|<code>TC</code>|<code>TR</code>|<code>CL</code>|<code>CC</code>|<code>CR</code>|<code>BL</code>|<code>BC</code>|<code>BR</code>]</p>
<dd> Set the alignment point between the source and target active regions. The keywords specify &quot;top-left&quot;, &quot;top-center&quot;, &quot;top-right&quot;, etc. The specified corner or point from the source region will be mapped to the same spot in the target region; and cropping or padding which is applied to the active regions will preserve this mapping. The default is CC, for &quot;center-center&quot;, i.e. the source and target regions are mutually centered. The keywords are mutually exclusive. The default is CC. See &quot;NOTES ON SOURCE AND TARGET ALIGNMENT&quot; for details.</dl>
<p> <code>preset=</code>[<code>VCD</code>|<code>CVD</code>|<code>SVCD</code>|<code>DVD</code>|<code>DVD_WIDE</code>|<code>DV</code>|<code>DV_WIDE</code>|<br />
 <code>SVCD_STILL_HI</code>|<code>SVCD_STILL_LO</code>|<code>VCD_STILL_HI</code>|<code>VCD_STILL_LO</code>|<br />
 <code>ATSC_720P</code>|<code>ATSC_1080I</code>|<code>ATSC_1080P</code>] </p>
<dl>
<dt>
<dd> Use preset target parameters for several common output formats. Individual parameters can be overridden by following with more &quot;-O&quot; settings. These keywords are mutually exclusive. For the details of what settings these preset keywords imply, see &quot;NOTES ON TARGET PRESETS&quot;.</p>
<dl>
<dt><code>VCD</code> &#8211; 352-wide VideoCD, progressive</p>
<dd>
<dt><code>CVD</code> &#8211; 352-wide (full-height) ChinaVideoDisc</p>
<dd>
<dt><code>SVCD</code> &#8211; 480-wide SuperVCD</p>
<dd>
<dt><code>DVD</code> &#8211; 720-wide DVD</p>
<dd>
<dt><code>DVD_WIDE</code> &#8211; 720-wide DVD, anamorphic pixels</p>
<dd>
<dt><code>DV</code> &#8211; 720-wide DV (bottom-field-first, 4:1:1)</p>
<dd>
<dt><code>DV_WIDE</code> &#8211; 720-wide DV, anamorphic pixels</p>
<dd>
<dt><code>SVCD_STILL_HI</code> &#8211; high-resolution SVCD still image</p>
<dd>
<dt><code>SVCD_STILL_LO</code> &#8211; low-resolution SVCD still image</p>
<dd>
<dt><code>VCD_STILL_HI</code> &#8211; high-resolution VCD still image</p>
<dd>
<dt><code>VCD_STILL_LO</code> &#8211; low-resolution SVCD still image</p>
<dd>
<dt><code>ATSC_720P</code> &#8211; ATSC 720p (progressive HDTV)</p>
<dd>
<dt><code>ATSC_1080I</code> &#8211; ATSC 1080i (interlaced HDTV)</p>
<dd>
<dt><code>ATSC_1080P</code> &#8211; ATSC 1080p (HDTV)</p>
<dd></dl>
</dl>
</dl>
<dt><code>-S</code><i> scaling_parameter</i></p>
<dd>
<dl>
<dt>
<dd> Specify parameters for the scaling engine. All &#8216;-S&#8217; arguments are evaluated in order, and later arguments on the command-line will override earlier ones.</p>
<dl>
<dt><code>mode=MONO</code></p>
<dd> Request monochrome scaling. The source is treated as monochrome and its chroma channels are ignored. The chroma channels of the output stream will be zeroed to yield a grayscale output.</p>
<dt><code>mode=LINESWITCH</code></p>
<dd> Request line swapping. Effectively, the top and bottom fields within each frame will be swapped. This may help with malformed streams that have a messed up spatial order. This option is only effective on interlaced streams.</p>
<dt><code>scaler=</code><i>scaler-name</i></p>
<dd> Use a particular scaling engine. The available engines are:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&#8216;default&#8217;&nbsp;<wbr>&#8211; Matto&#8217;s Generic Scaler&nbsp;<wbr>(the default)</dl>
<dt><code>option=</code><i>scaler-option</i></p>
<dd> Specify an option for the chosen scaling engine. To see all the available options, use &quot;option=help&quot;.</p>
<dl>
<dt>
<dd>
<p> For the default engine, the available <i>scaler-option</i>s select the filter kernel:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>box</code> &#8211; box filter</p>
<dd>
<dt><code>linear</code> &#8211; linear interpolation</p>
<dd>
<dt><code>quadratic</code> &#8211; quadratic interpolation</p>
<dd>
<dt><code>cubic</code> &#8211; cubic interpolation, Mitchell-Netravali spline</p>
<dd>
<dt><code>cubicCR</code> &#8211; cubic interpolation, Catmull-Rom spline</p>
<dd>
<dt><code>cubicB</code> &#8211; cubic interpolation, B-spline</p>
<dd>
<dt><code>cubicK4</code> &#8211; Keys 4th-order cubic</p>
<dd>
<dt><code>sinc:N</code> &#8211; sinc with Lanczos window, N cycles</p>
<dd></dl>
</dl>
<p> To select kernels for the x and y scaling directions independently, use two kernel names separated by a comma, e.g. <i>option=box,quadratic</i>. </p>
<p> <code>sinc:N</code> will give the best quality results (least aliasing), but is the slowest. The quality improves with larger values of N, as does processing time. <code>cubic</code> is generally regarded in the graphics world as the 3rd-order cubic spline with the best trade-off between smoothing and aliasing. <code>box</code> yields the worst quality results (most aliasing), but is the fastest. The default kernel is <code>cubicK4</code>, which has a flatter passband and sharper cutoff than <code>cubic</code>. (It requires the same computational power as <code>sinc:4</code>, but produces less ringing artifacts.)</dl>
</dl>
</dl>
</dl>
<h2>NOTES ON TARGET PRESETS</h2>
<p> The following table details the settings provided by the various target &quot;preset=&quot; keywords. When two values are given the primary is for NTSC streams; the value in {braces} is for PAL streams. If interlace value is unspecified, it is inherited from the source, otherwise the indicated target interlacing is required. </p>
<pre><code>
Preset Frame Size Interlace SAR Subsampling-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -VCD 352x240 {288} none 10 : 11
{
    59 : 54
}
4 : 2 : 0 - JPEG
                CVD 352x480
{
    576
}
-- -20 : 11
{
    59 : 27
}
4 : 2 : 0 - MPEG2
                SVCD 480x480
{
    576
}
-- -15 : 11
{
    59 : 36
}
4 : 2 : 0 - MPEG2
                DVD 720x480
{
    576
}
-- -10 : 11
{
    59 : 54
}
4 : 2 : 0 - MPEG2
                DVD_WIDE 720x480
{
    576
}
-- -40 : 33
{
    118 : 81
}
4 : 2 : 0 - MPEG2 DV 720x480 {576} bottom - first 10 : 11
{
    59 : 54
}
4 : 1 : 1 DV_WIDE 720x480 {576} bottom - first 40 : 33
{
    118 : 81
}
4 : 1 : 1 SVCD_STILL_HI 704x480 {576} none 10 : 11
{
    59 : 54
}
4 : 2 : 0 - MPEG2
                SVCD_STILL_LO 480x480 {576} none 15 : 11
{
    59 : 36
}
4 : 2 : 0 - MPEG2
                VCD_STILL_HI 704x480 {576} none 10 : 11
{
    59 : 54
}
4 : 2 : 0 - JPEG
                VCD_STILL_LO 352x240 {288} none 10 : 11
{
    59 : 54
}
4 : 2 : 0 - JPEG ATSC_720p 1280x720 none 1 : 1 4 : 2 : 0 - MPEG2 ATSC_1080i 1920x1080(required)1 : 1 4 : 2 : 0 - MPEG2 ATSC_1080p 1920x1080 none 1 : 1 4 : 2 : 0 - MPEG2
</code></pre>
<h2>NOTES ON REGION GEOMETRY</h2>
<p> Active and matte regions are specified using a geometry string of the form &quot;WxH+X+Yaa&quot;. The &quot;WxH&quot; part specifies the size of the region, as a Width and Height in pixels. (In some cases, the &quot;WxH&quot; may be omitted, and the region size defaults to the full frame size.) The &quot;+X+Y&quot; specifies the position of the region, as an offset relative to the anchor point specified by &quot;aa&quot;. </p>
<p> The &quot;aa&quot; code can be one of <code>TL</code>, <code>TC</code>, <code>TR</code>, <code>CL</code>, <code>CC</code>, <code>CR</code>, <code>BL</code>, <code>BC</code>, or <code>BR</code>. These stand for &quot;top-left&quot;, &quot;top-center&quot;, &#8230;, &quot;bottom-center&quot;, &quot;bottom-right&quot;. These codes are not case-sensitive. </p>
<p> The &quot;+X+Y&quot; specifies the offset of the region&#8217;s anchor point from the frame&#8217;s anchor point. For example, &quot;+20+30TL&quot; means that the top-left corner of the region will be offset 20 pixels to the right and 30 pixels down from the top-left corner of the frame. </p>
<p> The offset values can also be negative. For example, &quot;-4+0CC&quot; means that the center (vertical and horizontal) of the region is offset 4 pixels to the left of the center of the frame. </p>
<p> The default anchoring point for geometry strings is <code>TL</code>, i.e. the top-left corner. </p>
<h2>NOTES ON SOURCE AND TARGET ALIGNMENT</h2>
<p> Often, the source and target active regions do not match exactly. This happens when, using the given or calculated scaling ratios, the source region scales to a different size or shape than the target region. In this case, the source and target regions are mutually clipped, so that only the portion of the source which fits will be scaled into the target. </p>
<p> Before any clipping or padding, the source and target regions are aligned so that the points specified via the &quot;align=aa&quot; parameter coincide. The &quot;aa&quot; code specifies an anchor point as described above. </p>
<p> For example, &quot;align=BC&quot; specifies that the bottom-center of the source region should get mapped to the bottom-center of the target region. In other words, the source region will be horizontally centered and vertically aligned to the bottom of the target region before clipping: </p>
<p>&#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;source | abcdefghijklmn |<br />
    &#8212; &#8211; | opqrstuvwxyz01 | &#8212; -target&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; | | 234567890ABCDE | | | 234567890ABCDE |<br />
    | | FGHIJKLMNOPQRS | | | FGHIJKLMNOPQRS |<br />
    | | TUVWXYZabcdefg | | | TUVWXYZabcdefg |<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Before Mutually Clipped</p>
<p> If instead &quot;align=TR&quot; were centered, the source would be clipped in a different place, and scaled into a different region of the target frame: </p>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- | | abcdefghijklmn | | abcdefghijklmn |
    | | opqrstuvwxyz01 | | opqrstuvwxyz01 |
    | | 234567890ABCDE | | 234567890ABCDE |
    -- -- -- | FGHIJKLMNOPQRS | -- -- -- -- -- -- -- --target | TUVWXYZabcdefg | source-- -- -- -- -- -- -- --Before Mutually Clipped
</code></pre>
<p> The default alignment mode is &quot;CC&quot;, that is, the source and target are mutually centered. </p>
<h2>NOTES ON SCALE FACTOR INFERENCE</h2>
<p> If the X and Y scaling factors are not explicitly provided, <code>y4mscaler</code> will infer the factors from the source and target active regions and sample aspect ratios (SAR&#8217;s). </p>
<p> If the active regions are not compatible shape-wise (given the SAR&#8217;s), the source and target regions will be clipped or padded according to one of four policies. The policy is selected using the &quot;infer=&quot; parameter and one of the keywords <code>PAD</code>, <code>CLIP</code>, <code>PRESERVE_X</code>, or <code>PRESERVE_Y</code>. (The default is <code>PAD</code>.)</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PAD</code></p>
<dd> Pick scaling factors which will pad the source, but ensure that all of the source image content ends up in the target.</p>
<dt><code>CLIP</code></p>
<dd> Pick scaling factors which will clip the source, but which will fill the target region as much as possible.</p>
<dt><code>PRESERVE_X</code></p>
<dd> Pick scaling factors which preserve as much of the horizontal source content as possible.</p>
<dt><code>PRESERVE_Y</code></p>
<dd> Pick scaling factors which preserve as much of the vertical source content as possible.</dl>
</dl>
<p> The policy is further affected by a choice of two other keywords, <code>SIMPLIFY</code>, or <code>EXACT</code>. (The default is <code>SIMPLIFY</code>.)</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>EXACT</code></p>
<dd> Calculate exact scaling factors.</p>
<dt><code>SIMPLIFY</code></p>
<dd> Adjust the active regions and scaling factors (within 10% or so), to simplify the ratios as much as possible. (For example, crop or pad slightly to achieve a ratio of 2/1 rather than 45/22.)</dl>
</dl>
<h2>NOTES ON CHROMA MODES AND SUBSAMPLING</h2>
<p> <code>y4mscaler</code> can convert streams from one chroma subsampling mode to another. Such conversions are always lossy operations, even if the overall frame is undergoing 1/1 scaling. </p>
<p> <code>y4mscaler</code> will infer the source&#8217;s subsampling mode from tags in the input stream header. The target presets (&quot;preset=XXX&quot;) will attempt to set the target subsampling mode appropriately. Otherwise, by default the target subsampling mode will match the source. One can explicitly set the subsampling mode for the source and/or the target by using the &quot;chromass=&quot; parameter. </p>
<p> <code>y4mscaler</code> is capable of reading and writing streams in the 4:4:4, 4:2:2, 4:1:1, and 4:2:0 (all three varieties) subsampling modes. The first three, however, are a relatively new addition to the YUV4MPEG2 standard, and many MJPEGtools will fail to process them correctly, if at all. smil2yuv and raw2yuv can produce native 4:1:1 streams from NTSC DV video, which can then be converted to 4:2:0 by <code>y4mscaler</code> before further processing by other tools. </p>
<p> If the source has an alpha-channel (i.e. 444ALPHA mode) and the target does not, the alpha channel will simply be discarded. On the other hand, if the target has an alpha-channel but the source does not, a constant alpha-channel will be created using the alpha-value of the target&#8217;s background color (as set by &quot;-O bg=&quot;). The default is fully-opaque. </p>
<p> Similarly, if the target has chroma channels but the source does not (i.e. a luma-only MONO stream), then the chroma channels in the output will be set according to the background color. </p>
<h2>NOTES ON ANOMALOUS INTERLACE MIXTURES</h2>
<p> The YUV4MPEG2 format allows for &quot;mixed-mode interlacing&quot; streams, which may contain a mixture of progressive and interlaced frames. Each frame is tagged as temporally interlaced or progressive, and vertically-subsampled frames (4:2:0 formats) are further tagged as spatially interlaced or not. Unfortunately, this allows for the possibility of <code>anomalous</code> frames, which happen to be temporally interlaced (fields sampled at different times) but spatially progressive (subsampling performed across entire frame), or vice-versa. The only reasonable thing to do with such anomalous frames is to vertically-upsample the chroma, essentially making to problem go away as quickly as possible. </p>
<p> <code>y4mscaler</code> will only process such frames if the target output format is non-vertically-subsampled (e.g. 4:4:4, 4:2:2, etc.) and no other vertical processing is required. Otherwise <code>y4mscaler</code> will bail on processing in midstream when it encounters an anomalous frame. If there is any possibility of encountering such an error, <code>y4mscaler</code> will print a warning when processing begins. </p>
<h2>EXIT STATUS</h2>
<dl>
<dt>0</p>
<dd> Successful program execution.</p>
<dt>1</p>
<dd> Usage, syntax, or operational error. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page is copyright 2005 by Matthew Marjanovic.<br />
 Feel free to direct any questions, remarks, problems, or bug reports concerning this tool to <i>&lt;dmg @ mir.com&gt;.</i> </p>
<dl>
<dt>For more info, see our website at:</p>
<dd> &lt;<a rel="nofollow" href="http://www.mir.com/DMG/">http://www.mir.com/DMG/</a>&gt; </p>
<dt>For more information on MJPEGtools, consult:</p>
<dd> &lt;<a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a>&gt; </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-ppmtoy4m/">ppmtoy4m</a></code>(1), <code><a href="/docs/linux/man/1-raw2yuv/">raw2yuv</a></code>(1), <code><a href="/docs/linux/man/1-smil2yuv/">smil2yuv</a></code>(1), <code><a href="/docs/linux/man/1-yuvplay/">yuvplay</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
