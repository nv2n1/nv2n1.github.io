---
title: "webpmux(1)"
name: "webpmux"
section: "1"
letter: "w"
url: "/docs/linux/man/1-webpmux/"
description: "webpmux – command line tool to create WebP Mux/container file."
---

<h2>NAME</h2>
<p> webpmux &#8211; command line tool to create WebP Mux/container file.</p>
<h2>SYNOPSIS</h2>
<p> <code>webpmux -get</code> <i>GET_OPTIONS</i> <i>INPUT</i> <code>-o</code> <i>OUTPUT</i><br />
 <code>webpmux -set</code> <i>SET_OPTIONS</i> <i>INPUT</i> <code>-o</code> <i>OUTPUT</i><br />
 <code>webpmux -strip</code> <i>STRIP_OPTIONS</i> <i>INPUT</i> <code>-o</code> <i>OUTPUT</i><br />
 <code>webpmux -frame</code> <i>FRAME_OPTIONS</i> <code>[ -frame &#8230; ] [ -loop</code> <i>LOOP_COUNT</i> <code>]</code> </p>
<dl>
<dt>
<dd> <code>[ -bgcolor</code> <i>BACKGROUND_COLOR</i> <code>] -o</code> <i>OUTPUT</i></dl>
<p> <code>webpmux -info</code> <i>INPUT</i><br />
 <code>webpmux [-h|-help]</code><br />
 <code>webpmux -version</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>webpmux</code> command. </p>
<p> <code>webpmux</code> can be used to create a WebP container file and extract/strip relevant data from the container file.</p>
<h2>OPTIONS</h2>
<h3>GET_OPTIONS (-get):</h3>
<dl>
<dt><code>icc</code></p>
<dd> Get ICC profile.</p>
<dt><code>exif</code></p>
<dd> Get EXIF metadata.</p>
<dt><code>xmp</code></p>
<dd> Get XMP metadata.</p>
<dt><code>frame</code><i> n</i></p>
<dd> Get nth frame. </p>
</dl>
<h3>SET_OPTIONS (-set)</h3>
<dl>
<dt><code>icc</code><i> file.icc</i></p>
<dd> Set ICC profile.</dl>
<p> Where: &#8216;file.icc&#8217; contains the ICC profile to be set.</p>
<dl>
<dt><code>exif</code><i> file.exif</i></p>
<dd> Set EXIF metadata.</dl>
<p> Where: &#8216;file.exif&#8217; contains the EXIF metadata to be set.</p>
<dl>
<dt><code>xmp</code><i> file.xmp</i></p>
<dd> Set XMP metadata.</dl>
<p> Where: &#8216;file.xmp&#8217; contains the XMP metadata to be set. </p>
<h3>STRIP_OPTIONS (-strip)</h3>
<dl>
<dt><code>icc</code></p>
<dd> Strip ICC profile.</p>
<dt><code>exif</code></p>
<dd> Strip EXIF metadata.</p>
<dt><code>xmp</code></p>
<dd> Strip XMP metadata. </p>
</dl>
<h3>FRAME_OPTIONS (-frame)</h3>
<dl>
<dt><i>file_i +di[+xi+yi[+mi]]</i></p>
<dd> Where: &#8216;file_i&#8217; is the i&#8217;th frame (WebP format), &#8216;xi&#8217;,&#8217;yi&#8217; specify the image offset for this frame, &#8216;di&#8217; is the pause duration before next frame and &#8216;mi&#8217; is the dispose method for this frame (0 for NONE or 1 for BACKGROUND). Additionally, if &#8216;mi&#8217; is ommitted then&#8217;xi&#8217; and &#8216;yi&#8217; can be omitted and will default to +0+0.</p>
<dt><code>-loop</code><i> n</i></p>
<dd> Loop the frames n number of times. 0 indicates the frames should loop forever. Valid range is 0 to 65535 [Default: 0 (infinite)].</p>
<dt><code>-bgcolor</code><i> A,R,G,B</i></p>
<dd> Background color of the canvas.<br />
 where: &#8216;A&#8217;, &#8216;R&#8217;, &#8216;G&#8217; and &#8216;B&#8217; are integers in the range 0 to 255 specifying the Alpha, Red, Green and Blue component values respectively [Default: 255,255,255,255]. </p>
</dl>
<h3>INPUT</h3>
<dl>
<dt>Input file in WebP format.</p>
<dd>
</dl>
<h3>OUTPUT (-o)</h3>
<dl>
<dt>Output file in WebP format.</p>
<dd>
</dl>
<h3>Note:</h3>
<dl>
<dt>The nature of EXIF, XMP and ICC data is not checked and is assumed to be valid.</p>
<dd>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to our issue tracker: <a rel="nofollow" href="http://code.google.com/p/webp/issues">http://code.google.com/p/webp/issues</a><br />
 Patches welcome! See this page to get started: <a rel="nofollow" href="http://www.webmproject.org/code/contribute/submitting-patches/">http://www.webmproject.org/code/contribute/submitting-patches/</a> </p>
<h2>EXAMPLES</h2>
<p> webpmux -set icc image_profile.icc in.webp -o icc_container.webp<br />
 webpmux -get icc icc_container.webp -o image_profile.icc<br />
 webpmux -strip icc icc_container.webp -o without_icc.webp<br />
 webpmux -set xmp image_metadata.xmp in.webp -o xmp_container.webp<br />
 webpmux -get xmp xmp_container.webp -o image_metadata.xmp<br />
 webpmux -strip xmp xmp_container.webp -o without_xmp.webp<br />
 webpmux -set exif image_metadata.exif in.webp -o exif_container.webp<br />
 webpmux -get exif exif_container.webp -o image_metadata.exif<br />
 webpmux -strip exif exif_container.webp -o without_exif.webp<br />
 webpmux -frame anim_1.webp +100 -frame anim_2.webp +100+50+50 -loop 10 </p>
<dl>
<dt>
<dd> -bgcolor 255,255,255,255 -o anim_container.webp</dl>
<p> webpmux -get frame 2 anim_container.webp -o frame_2.webp </p>
<h2>AUTHORS</h2>
<p> <code>webpmux</code> is written by the WebP team.<br />
 The latest source tree is available at <a rel="nofollow" href="http://www.webmproject.org/code">http://www.webmproject.org/code</a> </p>
<p> This manual page was written by Vikas Arora &lt;vikaas.arora [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dwebp/">dwebp</a></code>(1), <code><a href="/docs/linux/man/1-cwebp/">cwebp</a></code>(1), <code><a href="/docs/linux/man/1-gif2webp/">gif2webp</a></code>(1).<br />
 Please refer to <a rel="nofollow" href="http://developers.google.com/speed/webp/">http://developers.google.com/speed/webp/</a> for additional information. </p>
<h2>Index</h2>
