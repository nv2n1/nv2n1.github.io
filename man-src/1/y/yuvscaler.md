---
title: "yuvscaler(1)"
name: "yuvscaler"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvscaler/"
description: "yuvscaler – UPscales or DOWNscales a YUV4MPEG2 stream to a specified format"
---

<h2 class="name">NAME</h2>
<p> yuvscaler &#8211; UPscales or DOWNscales a YUV4MPEG2 stream to a specified format</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvscaler </code> [<code>-I</code> <i>input_keyword</i>] [<code>-M</code> <i>mode_keyword</i>] [<code>-O</code> <i>output_keyword</i>] [<code>-n p</code>|<code>s</code>|<code>n</code>] [<code>-v 0</code>&#8211;<code>2</code>] [<code>-h</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvscaler</code> is a general (UP or DOWN) scaling utility that is provided to allow conversion between different video formats. It reads in a YUV4MPEG2 format stream from stdin (such as that produced by <code>lav2yuv</code>) and outputs such stream to stdout (e.g. to be consumed by <code>mpeg2enc</code>). The most common use of yuvscaler is to generate input suitable for MPEG encoding to VCD or SVCD formats using <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1). </p>
<p> <code>yuvscaler</code> will automatically take into account PAL/SECAM and NTSC format, as well as widescreen (16:9) format and interlacing. Use of yuvscaler was designed to be straightforward. </p>
<h2>EXAMPLES</h2>
<p> <code>VCD encoding:</code><br />
 lav2yuv my-file.avi | yuvscaler -O VCD | mpeg2enc -f 1 -o vcd.%d.m1v </p>
<p> <code>SVCD encoding:</code><br />
 lav2yuv my-file.qt | yuvscaler -O SVCD | mpeg2enc -f 4 -o svcd.%d.m2v </p>
<p> <code>Encoding anamorphic 16:9 as letterboxed VCD:</code><br />
 lav2yuv my-ana16-9.eli | yuvscaler -M WIDE2VCD | mpeg2enc -f 1 -o letterbox_vcd.%d.m1v </p>
<p> <code>Encoding anamorphic 16:9 as letterboxed SVCD:</code><br />
 lav2yuv my-ana16-9.eli | yuvscaler -M WIDE2STD -O SVCD | mpeg2enc -f 4 -o letterbox_svcd.%d.m2v </p>
<p> <code>Encoding anamorphic 16:9 as letterboxed DVD:</code><br />
 lav2yuv my-ana16-9.eli | yuvscaler -M WIDE2STD -O DVD | mpeg2enc -f 8 -o letterbox_dvd.%d.m2v </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-I </code><i>input_keyword</i></p>
<dd>
<dt>
<dd> Specifies input processing options. Input options may be combined by using multiple <code>-I</code> flags. Possible <i>input_keyword</i>s are: </p>
<dt>
<dd> <code>USE_WidthxHeight+WidthOffset+HeightOffset</code> to select a useful area of the input frame (all multiple of 2, Height and HeightOffset multiple of 4 if interlaced), the rest of the image being discarded</p>
<dt>
<dd> <code>ACTIVE_WidthxHeight+WidthOffset+HeightOffset</code> to select an active area of the input frame (all multiple of 2, Height and HeightOffset multiple of 4 if interlaced), the rest of the image being made black </p>
<dt><code>-M </code><i>mode_keyword</i></p>
<dd>
<dt>
<dd> Sets the scaling mode options. Scaling mode options can be combined by giving several <code>-M</code> flags. Possible are: </p>
<dt>
<dd> <code>BICUBIC</code> &#8211; to use the (Mitchell-Netravalli) high-quality bicubic upsacling and/or downscaling algorithm</p>
<dt>
<dd> <code>RESAMPLE</code> &#8211; to use a classical resampling algorithm -only for downscaling- that goes much faster than bicubic. For coherence reason, <code>yuvscaler</code> will use RESAMPLE if only downscaling is necessary, BICUBIC if not.</p>
<dt>
<dd> <code>WIDE2STD</code> &#8211; convert widescreen anamorphic (16:9) input video into letterboxed (4:3), generating necessary black lines. Note that for MPEG applications if your <i>player</i> can properly decode anamorphic video you may wish to leave the video unscaled and simply specify the approprate format during MPEG encoding (see <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1)).</p>
<dt>
<dd> <code>RATIO_WidthIn_WidthOut_HeightIn_HeightOut</code> to specified scaling ratios of WidthIn/WidthOut for width and HeightIN/HeightOut for height to be applied to the useful area. The output frames that result from scaling can have a different format than the output format specified using <code>-O</code> options(s). In this case, <code>yuvscaler</code> automatically generate necessary black lines and columns and/or skips necessary lines and columns to center the scaled image in the output frame.</p>
<dt>
<dd> <code>WIDE2VCD</code> to scale anamorphic widescreen (16:9) frames into letterboxed VCD format (equivalent to -M WIDE2STD -O VCD).</p>
<dt>
<dd> <code>FASTVCD</code> to transcode full sized frames to VCD (equivalent to -M RATIO_2_1_2_1 -O VCD, see below).</p>
<dt>
<dd> <code>FAST_WIDE2VCD</code> to transcode full-sized anamorphic (16:9) frames to letter-boxed VCD (equivalent to -M WIDE2STD -M RATIO_2_1_2_1 -O VCD, see below).</p>
<dt>
<dd> <code>NO_HEADER</code> to suppress stream header generation on output</p>
<dt>
<dd> <code>MMX</code> to use MMX functions for BICUBIC scaling (experimental feature!!)</p>
<dt>
<dd>
<dt><code>-O </code><i>output_keyword</i></p>
<dd>
<dt>
<dd> Sets the output frame format options. Output format options can be combined by giving several <code>-O</code> flags. By default, output frames size will be the same as input frame sizes, as well as output frames interlacing if coherent with output keyword specification which prevails, top_first if not. </p>
<dt>
<dd> <code>MONOCHROME</code> to generate monochrome frames on output. Chrominance information for the scaled pixels is set neutral (white). MPEG encoding of black and white video will be both inefficient <i>and</i> show annonying chrominance artifacts unless this is done.</p>
<dt>
<dd> <code>VCD</code> to generate VCD compliant frames on output (taking care of PAL and NTSC standards). Non-interlaced output.</p>
<dt>
<dd> <code>SVCD</code> to generate SVCD compliant frames on output (taking care of PAL and NTSC standards). Top-field-first interlaced frames.</p>
<dt>
<dd> <code>DVD</code> to generate DVD compliant frames on output (taking care of PAL and NTSC standards). Top-field-first interlaced frames.</p>
<dt>
<dd> <code>SIZE_WidthxHeight</code> to generate frames of size WidthxHeight on output (multiple of 4)</p>
<dt>
<dd> If VCD, SVCD or DVD keywords are not used, output interlacing is taken of the same type as input. By default, output frames size will be the same as input frame size.</p>
<dt>
<dd>
<dt><code>-n p|s|n</code></p>
<dd> (usually not necessary) if norm could not be determined from data flux, specifies the OUTPUT norm for VCD/SVCD (p=pal,s=secam,n=ntsc). </p>
<dt><code>-v 0|1|2</code></p>
<dd> Specifies the degree of verbosity: 0=quiet, 1=normal, 2=verbose/debug </p>
<dt><code>-h</code></p>
<dd> Prints a summary of command line syntax. </p>
</dl>
<p> <code>Note:</code> The most useful downscaling ratios are handled using dedicated optimised scaling routines. They are:</p>
<dl>
<dt>
<dd> RATIO_WidthIn_WidthOut_2_1 =&gt; Full-sized frame to VCD downscaling</p>
<dt>
<dd> RATIO_3_2_1_1 =&gt; Full-sized frame to SVCD downscaling</p>
<dt>
<dd> RATIO_1_1_4_3 =&gt; WIDE2STD downscaling mode</p>
<dt>
<dd> RATIO_WidthIn_WidthOut_1_1 =&gt; downscaling only concerns width, not height</p>
<dt>
<dd> RATIO_1_1_HeightIn_HeightOut =&gt; downscaling only concerns height, not width</p>
<dt>
<dd> RATIO_2_1_2_1 =&gt; FASTVCD, slightly width distorted (real ratio 45 to 22) but faster full-sized frame to VCD downscaling (-M RATIO_2_1_2_1 -O VCD)</p>
<dt>
<dd> RATIO_WidthIn_WidthOut_8_3 =&gt; specific to WIDE2VCD downscaling (-M WIDE2STD -O VCD)</p>
<dt>
<dd> RATIO_2_1_8_3 =&gt; specific to (slighly distorted) FAST_WIDE2VCD downscaling (-M WIDE2STD -M RATIO_2_1_2_1 -O VCD)</p>
<dt>
<dd> RATIO_1_1_1_1 =&gt; copy useful input part of possible several files into output frames </p>
</dl>
<h2>AUTHOR</h2>
<p> This man page was written by Xavier Biquard et al.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lavpipe/">lavpipe</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1) <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1) </p>
<h2>Index</h2>
