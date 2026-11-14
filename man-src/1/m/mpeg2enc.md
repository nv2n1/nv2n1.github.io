---
title: "mpeg2enc(1)"
name: "mpeg2enc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpeg2enc/"
description: "mpeg2enc – MPEG-1/2 encoder"
---

<h2 class="name">NAME</h2>
<p> mpeg2enc &#8211; MPEG-1/2 encoder</p>
<h2>SYNOPSIS</h2>
<p> <code>mpeg2enc</code> [<code>-v</code>|<code>&#8211;verbose</code> <i>num</i>] [<code>-M</code>|<code>&#8211;multi-thread</code> <i>num_CPU</i>] [<code>-f</code>|<code>&#8211;format</code> <i>mpeg_profile</i>] [<code>-l</code>|<code>&#8211;level</code>]<code>h</code>|<code>high</code>|<code>m</code>|<code>main</code> [<code>-b</code>|<code>&#8211;video-bitrate</code> <i>bitrate_kbps</i>] [<code>-V</code>|<code>&#8211;video-buffer</code> <i>video_buf_size_kB</i>] [<code>-T</code>|<code>&#8211;target-still-size</code> <i>still_size_kB</i>] [<code>-q</code>|<code>&#8211;quantisation</code> <i>quantisation</i>] [<code>-r</code>|<code>&#8211;motion-search-radius</code> <i>motion_search_radius</i>] [<code>-Q</code>|<code>&#8211;quantisation-reduction</code> <i>-4.0..5.0</i>] [<code>-X</code>|<code>&#8211;quant-reduction-max-var</code> <i>0.0</i>..<i>2500.0]</i> [<code>-p</code>|<code>&#8211;3-2-pulldown</code>] [<code>-I</code>|<code>&#8211;interlace-mode</code> <i>0|1|2</i>] [<code>-s</code>|<code>&#8211;sequence-header-every-gop</code>] [<code>-g</code>|<code>&#8211;min-gop-size</code> <i>min_gop_size</i>] [<code>-G</code>|<code>&#8211;max-gop-size</code> <i>max_gop_size</i>] [<code>-P</code>|<code>&#8211;force-b-b-p</code>] [<code>-n</code>|<code>&#8211;video-norm</code> <i>n|p|s</i>] [<code>-F</code>|<code>&#8211;frame-rate</code> <i>frame_rate_code</i>] [<code>-x</code>|<code>&#8211;display-hsize]</code> <i>32</i>..<i>38383</i>] [<code>-y</code>|<code>&#8211;display-vsize]</code> <i>32</i>..<i>38383</i>] [<code>-a</code>|<code>&#8211;aspect</code> <i>aspect_ratio_code</i>] [<code>-z</code>|<code>&#8211;playback-field-order</code> <i>b|t</i>] [<code>-4</code>|<code>&#8211;reduction-4&#215;4</code> <i>1..4</i>] [<code>-2</code>|<code>&#8211;reduction-2&#215;2</code> <i>1..4</i>] [<code>-S</code>|<code>&#8211;sequence-length</code> <i>size_MB</i>] [<code>-B</code>|<code>&#8211;nonvideo-bitrate</code> <i>bitrate_kbps</i>] [<code>-N</code>|<code>&#8211;reduce-hf</code> <i>0.0..2.0</i>] [<code>-D</code>|<code>&#8211;intra_dc_prec</code> <i>8..11</i>] [<code>-H</code>|<code>&#8211;keep-hf</code>] [<code>-d</code>|<code>&#8211;no-dummy-svcd-SOF</code>] [<code>-C</code>|<code>&#8211;correct-svcd-hds</code>] [<code>&#8211;no-constraints</code>] [<code>-K</code>|<code>&#8211;custom-quant-matrices</code> <i>kvcd|tmpgenc|default|hi-res|file=inputfile|help</i>] [<code>-E</code>|<code>&#8211;unit-coeff-elim</code> <i>-40..40</i>] [<code>-R</code>|<code>&#8211;b-per-refframe</code> <i>0..2</i>] [<code>&#8211;no-altscan-mpeg2</code>] [<code>&#8211;dualprime-mpeg2</code>] [<code>-A</code>|<code>&#8211;ratecontroller</code> <i>0..1</i>] [<code>-u</code>|<code>&#8211;cbr</code>] [<code>&#8211;chapters</code> <i>frame,&#8230;</i>] [<code>-?</code>|<code>&#8211;help</code>] <code>-o|&#8211;output</code> <i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> mpeg2enc is heavily enhanced derivative of the MPEG Software Simulation Group&#8217;s MPEG-2 reference encoder. It accepts streams in a simple planar YUV format &quot;YUV4MPEG&quot; produced by the <code>lav2yuv</code> and related filters (e.g. <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1)) from the <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) package. An output plug-in to the <code><a href="/docs/linux/man/1-mpeg2dec/">mpeg2dec</a></code>(1) MPEG decoder is available to permit its use in transcoding applications. The encoder currently fully supports the generation of elementary MPEG-1, progressive and interlaced frame MPEG-2 streams. Field encoded MPEG-2 is also possible but is not currently maintained or supported. </p>
<p> For most purposes this elementary stream output will need to be multiplexed with one or more audio streams into a program/systems stream using the <code><a href="/docs/linux/man/1-mplex/">mplex</a></code>(1) tool. </p>
<p> Note that although this manual page aims to explain how mpeg2enc can be used effectively it is not intended as an introduction to MPEG-1/2 video which is a fairly complex topic in its own right. The MPEG video format is a somewhat baroque standard with many many options, not all of which necessarily easy to explain or even particular useful in the context of a software encoder. </p>
<p> Much useful practical information for novices can be found in the mjpeg-HOWTO document that should have been installed with <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) package. Further information and useful supporting software can be found on the mjpegtools web-site: </p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></code> </p>
</dl>
<h2>SELECTING THE MPEG PROFILE</h2>
<p> Set the MPEG profile to use. The MPEG standards support a vast number of options. In practice, different applications of the MPEG format place additional constraints of the form the MPEG stream. Setting this flag selects the kind of stream to produce. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>0<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generic MPEG1. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>A basic MPEG-1 profile that lets most parameters<br />
&nbsp;<wbr>&nbsp;<wbr>be adjusted for particular applications using the other flags.<br />
&nbsp;<wbr>&nbsp;<wbr>Typical applications would be to produce a variable bitrate MPEG-1<br />
&nbsp;<wbr>&nbsp;<wbr>stream with big buffers and a high data-rate software playback<br />
&nbsp;<wbr>&nbsp;<wbr>on a computer. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>1<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Standard VCD. </p>
<p> An MPEG1 profile exactly to the VCD2.0 specification. Flag settings that would result in a non-standard stream structure are simply ignored. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>2<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>User VCD. </p>
<p> As for profile 2 but bitrate and video buffer size can be set to non-standard values. Frame size may also be non-standard. Bit-rate and buffer sizes default to those for standard VCD. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>3<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generic MPEG2. </p>
<p> A basic MPEG-2 profile that lets most parameters be adjusted for particular applications using the other flags. Typical applications would be to produce a MPEG-2 stream with big buffers and long GOP&#8217;s for software playback on a computer. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>4<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Standard SVCD. </p>
<p> An MPEG-2 profile exactly to the SVCD2.0 specification. Flag settings that would result in a non-standard stream structure are simply ignored. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>5<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Non-standard SVCD. </p>
<p> As for profile 4 but bitrate, video buffer size, GOP sizes and structure can be set to non-standard values. Frame size may also be non-standard. Bit-rate and buffer sizes default to those for standard SVCD. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>6<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>VCD Stills sequence. </p>
<p> Encodes the special style of MPEG stream used for still images on VCDs. To use this profile you must set the target size you wish to compress the images to using the -T flag. Reasonable values are around 35KB for standard resolution stills (352 wide) and 120KB for high resolution stills (704 wide). </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>7<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SVCD Stills sequence. </p>
<p> Encodes the special style of MPEG stream used for still images on SVCDs. Both standard (480 wide) and high resolution (704 wide) images are supported. As with VCD stills you select how big each compressed still should be using the -T flag. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>8<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DVD MPEG-2 for&nbsp;<wbr>&#8216;dvdauthor&#8217; </p>
<p> This version adds special dummy navigation packets into the output stream that the dvdauthor tool fills in to make a proper .VOB for authoring. Bit-rate defaults to 7500kbps, buffer sizes to the maximum permitted by the DVD specification. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>9<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DVD MPEG-2.&nbsp;<wbr> </p>
<p> Just a very basic implementation. Useful with DXR2 board and similar hardware that can decode MPEG-2 only if it is presented in a DVD like form. Bit-rate defaults to 7500kbps, buffer sizes to the maximum permitted by the DVD specification. </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>10<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ATSC 480i&nbsp;<wbr> </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>11<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ATSC 480p </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>12<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ATSC 720p </p>
<p> <code>-f|&#8211;format</code>&nbsp;<wbr>13<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ATSC 1080i </p>
<h2>GENERAL FUNCTION LETTERS</h2>
<p> <code>-v|&#8211;verbose</code>&nbsp;<wbr>num </p>
<p> Set verbosity level to num. 0 = warnings and errors only, 1 = information as well, 2=really verbose. </p>
<p> <code>-K|&#8211;custom-quant-matrices</code><code>kvcd</code><code>|</code><code>tmpgenc</code><code>|</code><br />
&nbsp;<wbr><code>default</code>&nbsp;<wbr>|&nbsp;<wbr><code>hi-res</code>&nbsp;<wbr>|&nbsp;<wbr><code>file=</code>inputfile |&nbsp;<wbr><code>help</code> </p>
<p> Specify which quantisation matrices to use instead of the defaults (which can be specified by using &quot;-K default&quot;). Using &quot;-K hi-res&quot; is identical to using the -H option. The value kvcd uses the Kvcd.Net matrices from <a rel="nofollow" href="http://www.kvcd.net/;">http://www.kvcd.net/;</a> the value tmpgenc invokes the TMPGEnc matrices from <a rel="nofollow" href="http://www.tmpgenc.net/e_main.html.">http://www.tmpgenc.net/e_main.html.</a> On average (this depends on the source material), the tmpgenc tables reduce the average bitrate by about 10% and the kvcd tables reduce bitrate by about 16% (compared to the default tables). </p>
<p> <code>-E|&#8211;unit-coeff-elim</code>&nbsp;<wbr>-40..40 </p>
<p> Specify when a special &#8216;unit coefficient elimination&#8217; algorithm should be applied to the encoded picture blocks. Basically, this procedure forces blocks of a type that don&#8217;t carry much information but are expensive to encode to be simply skipped. The larger the number the more potentially visible this skipping is likely to be but the more compression is boosted. A negative value means that all coefficients are zeroed, positive means only texture but not base intensity coefficients are zeroed. Values of around 10 or -10 seem to work well with high quality source material. For noisier material it might be worth trying 20 or -20. </p>
<p> <code>-R|&#8211;b-per-refframe</code>&nbsp;<wbr>0..2 </p>
<p> Specify how many bi-directionally (B type) difference-encoded frames should be encoded between reference (I or P) frames. The default is 0 except for VCD encoding where it is 2 B frames as required by the standard. Experts differ on how much using B frames improves compression. In practice unless you have really clean material they tend to be fairly useless and sometimes even harmful. Encoding is significantly faster and uses less memory if no B frames are encoded and compression is rarely more than marginally worse. </p>
<p> <code>-?|&#8211;help</code> </p>
<p> Display a synopsis of the command syntax.</p>
<h2>FUNCTION LETTERS ADJUSTING THE SELECTED PROFILE</h2>
<p> N.b. If the profile you have selected sets particular values for these parameters it will over-ride these adjustment flags. In particular, there is almost <i>nothing</i> that can be adjusted for the standard VCD and SVCD profiles. </p>
<p> <code>-b|&#8211;video-bitrate</code>&nbsp;<wbr>num </p>
<p> The bitrate of the output video stream in kBits/sec. The default is exactly the bitrate required for VCD streams. If variable bitrate (VBR) mode has been selected (see the -q option) this is the <i>maximum</i> bitrate of the stream. <code>NOTE:</code> By default MPEG-2 streams (<code>-f</code> 3, 4, 5, 8 and 9 are VBR. Use the <code>&#8211;cbr</code> option for generating CBR (Constant Bit Rate) streams. </p>
<p> <code>-A|&#8211;ratecontroller</code>&nbsp;<wbr>0..1 </p>
<p> Specify which of the rate control algorithms to use. Default is 0. </p>
<p> <code>-V|&#8211;video-buffer</code>&nbsp;<wbr>num </p>
<p> The maximum video buffer usage required to decode the stream in KBytes. The default is 46KB the (tiny) size specified for VCD. The size to use for SVCD is the (more reasonable) 230KB. If you are encoding for a half-decent software decoder it makes sense to push this up to 500K or more. </p>
<p> <code>-T|&#8211;target-still-size</code>&nbsp;<wbr>num </p>
<p> Set the target size for (S)VCD still images in KB. </p>
<p> <code>-s|&#8211;sequence-header-every-gop</code> </p>
<p> This flag forces the encoder to generate a &quot;sequence header&quot; at the start of every group-of-pictures. This is needed by some player hardware to support fast forward/rewind/random access functions but is a waste of bits otherwise. </p>
<p> <code>-d|&#8211;no-dummy-svcd-SOF</code> </p>
<p> The SVCD MPEG-2 profile demands that special &quot;Scan OFfset&quot; which are (in effect) pointers to the place on the final SVCD disk where the video for 0.5 and around 5-10 seconds behind and ahead in the stream is located. The intended use of this information is to support&quot;Fast forward/Rewind&quot; functions. Unfortunately, at the time mpeg2enc encodes the video it doesn&#8217;t know where the video is going to finally end up. So special dummy &quot;Scan OFfset&quot; values are written which are intended to be filled in during the creation of the SVCD image. Currently the GNU vcdimager tool handles this task. However, in some circumstances the dummy offsets can cause problems. This flags stops mpeg2enc generating them. </p>
<p> <code>&#8211;correct-svcd-hds</code> </p>
<p> In the official SVCD standards the field in the MPEG-2 header information that passes on the encoders &quot;recommended&quot; horizontal resolution to decode the stream to is supposed to take the values 540 (for 4:3 sequences) or 720 (for 16:9 sequences). In practice many players don&#8217;t work unless the value is 480. This flag, forces mpeg2enc to follow the official standard. It is worth trying if 16:9 sequences play at 4:3 aspect ratio. </p>
<p> <code>&#8211;no-constraints</code> </p>
<p> This flag deactivates all constraints for the maximum video samplerate or video resolution. Its purpose is to allow the encoding of unusual resolutions of MPEG-video (e.g. 2200 x 576, 160 degrees FOV VR-theatre MPEG movies), but should be used with care: It can possible circumvent a number of other security checks, and untested settings can cause mpeg2enc to crash in this mode. <code>-l</code>|&#8211;level h|high|m|main </p>
<p> This flag allows the MPEG-2 implementation level against which the coding parameters are checked to be set. You may need to set this to &#8216;high&#8217; if you&#8217;re encoding HDTV material. </p>
<p> <code>&#8211;no-altscan-mpeg2</code> </p>
<p> This flag deactivates the use of the &#8216;alternate&#8217; macroblock scan pattern for MPEG2 encoding. Normally this pattern is used but a few elderly software decoders had bugs relating to this feature. You should never need to use this flag. </p>
<p> <code>&#8211;dualprime-mpeg2</code> </p>
<p> MPEG-2 supports a special motion estimation mode (DPME, Dual Prime Motion Estimation) for I/P-frame only streams that can somewhat improve compression. A number of players (both hardware and software) do not support this mode. Those players may or may not be MPEG-2 compliant depending if DPME is an option or not in the MPEG-2 specs. If you need to generate content for such players (e.g. Ogle or Apple&#8217;s DVD player application) you should NOT turn on dualprime-mpeg2! Surprisingly at least one hardware/set-top player is known to be allergic to DPME being used. </p>
<p> <code>-z|&#8211;playback-field-order</code>&nbsp;<wbr>b|t </p>
<p> This flag overrides the field-order specified in the interlacing tag of the input stream header. (If you need this option, it indicates a problem in the capturing/encoding process where the temporal order of the two fields in each frame has been mislabeled. The effect of this is weird &quot;juddering&quot; when playing back the stream on a TV. Check the mjpeg-howto for more information about interlacing problems.) </p>
<h2>OPTION LETTERS CONTROLLING VIDEO PARAMETERS</h2>
<p> <code>-n|&#8211;video-norm</code>&nbsp;<wbr>n|p|s </p>
<p> Force the input stream to be treated as NTSC|PAL|SECAM regardless of what the stream header might suggest. Basically this just sets the defaults for a bunch of other options. </p>
<p> <code>-F|&#8211;frame-rate</code>&nbsp;<wbr>num </p>
<p> Set the frame-rate of the output-stream. By default, this value is inferred from the input header. Currently only the standard MPEG rates are supported. Eventually more-or-less arbitrary rates will be possible. </p>
<p>&nbsp;<wbr>0 &#8211; illegal </p>
<p>&nbsp;<wbr>1 &#8211; 24000.0/1001.0&nbsp;<wbr>(NTSC 3:2 pulldown converted FILM) </p>
<p>&nbsp;<wbr>2 &#8211; 24.0&nbsp;<wbr>(NATIVE FILM) </p>
<p>&nbsp;<wbr>3 &#8211; 25.0&nbsp;<wbr>(PAL/SECAM VIDEO&nbsp;<wbr>/&nbsp;<wbr>converted FILM) </p>
<p>&nbsp;<wbr>4 &#8211; 30000.0/1001.0&nbsp;<wbr>(NTSC VIDEO) </p>
<p>&nbsp;<wbr>5 &#8211; 30.0 </p>
<p>&nbsp;<wbr>6 &#8211; 50.0&nbsp;<wbr>(PAL FIELD RATE) </p>
<p>&nbsp;<wbr>7 &#8211; 60000.0/1001.0&nbsp;<wbr>(NTSC FIELD RATE) </p>
<p>&nbsp;<wbr>8 &#8211; 60.0 </p>
<p> <code>-a|&#8211;aspect</code>&nbsp;<wbr>num </p>
<p> Set the playback aspect ratio code of the encoded video. By default, this value is inferred from the input header. </p>
<p>&nbsp;<wbr>1 &#8211; 1&nbsp;<wbr>&nbsp;<wbr>&#8211; 1:1 display </p>
<p>&nbsp;<wbr>2 &#8211; 2&nbsp;<wbr>&nbsp;<wbr>&#8211; 4:3 display </p>
<p>&nbsp;<wbr>3 &#8211; 3&nbsp;<wbr>&nbsp;<wbr>&#8211; 16:9 display </p>
<p>&nbsp;<wbr>4 &#8211; 4&nbsp;<wbr>&nbsp;<wbr>&#8211; 2.21:1 display</p>
<dl>
<dt>
<dd> For MPEG-2 the specified aspect ratios are used directly. For MPEG-1 mpeg2enc infers the MPEG-1 pixel aspect code from the video norm specified and the specified playback aspect ratio.</dl>
<p> <code>-x|&#8211;display-hsize</code>&nbsp;<wbr>num </p>
<p> <code>-y|&#8211;display-vsize</code>&nbsp;<wbr>num </p>
<p> These set the display-horizontal-size and display-vertical-size hints in the MPEG-2. By default these are simply the encode frame dimensions. However, if they are set to different values the player gets a hint that the appropriate &#8216;black bars&#8217; or cropping/scaling should be performed. The main use for these parameters is to set a display-vertical-size of 1080 for HDTV 1080i or 1080p material. Here, since the frame height has to be a multiple of 16, the encoded frame height is forced to be 1088, even though HDTV standards specify only 1080 lines of picture content. Standards committees &#8230; love&#8217; em. </p>
<p> <code>-p|&#8211;3-2-pulldown</code> </p>
<p> Setting -p only makes sense for 24frame/sec Movie source material. It sets flags in the output stream that tell the decoder to play the movie as NTSC 60field/sec video using &quot;3:2 pulldown&quot;. This is vastly more efficient than encoding as 60field/sec video. The classic application is to transcode a PAL-encoded movie (24fps played too fast at 25 fps!) into NTSC (see the -f flag). </p>
<h2>OPTION LETTERS FOR CONTROLLING COMPRESSION AND SPEED</h2>
<p> <code>-M|&#8211;multi-thread</code>&nbsp;<wbr>num_CPU </p>
<p> MPEG encoding is a task that can be split over a small number of CPU&#8217;s quite efficiently. Mpeg2enc can be internally set to split major processing tasks between a number of concurrent threads. This flag adjusts the multi-threading to the optimum to utilise the specified number of CPU&#8217;s. </p>
<p> It should be noted that even with 1 CPU present <i>some</i> multi-threading is performed: frame input takes place in parallel with encoding. The default -M value is 1. This allows good performance to be achieved when when a seperate machine is being used for pre-processing (decoding from MJPEG, scaling, denoising etc) with the final result pipe to mpeg2enc (e.g. using rsh or ssh). </p>
<p> Setting -M 0 disables all multithreading. This is sometimes useful for debugging or to achieve maximum CPU efficiency on a shared machine. Setting -M 3 on a dual-CPU machine will produce slightly faster results than -M 2 at the price of slightly less CPU efficiency. This is useful if nothing else needs to be done on the encoding machine. In practice there is little point setting -M greater than 4 even if the CPU&#8217;s are available due to the fairly coarse-grained parallelism used. Indeed there is a hardcoded limit of 4 worker threads. </p>
<p> The default has been changed to be 0 instead of 1 to avoid the crash at end of encoding: </p>
<pre><code>
INFO : [mpeg2enc] Signaling last frame = 499 mpeg2enc : seqencoder.cc : 433 : void SeqEncoder::EncodeStream()
    : Assertion `pass1coded.size() == 0' failed. Abort
</code></pre>
<p> <code>-q|&#8211;quantisation</code>&nbsp;<wbr>1<code>..</code>31 </p>
<p> Minimum quantisation of the output stream. Quantisation controls the precision with which image information is encoded. The lower the number the higher the quality but the greater the required data-rate. <code>NOTE:</code> on IA32 systems it is possible to cause artifacting by setting the value too low (3 or less) due to arithmetic overflow/truncation in the DCT/iDCT routines. If this option is set a <i>variable bitrate </i> stream is produced. This is more efficient but variable bitrate MPEG-1 cannot be played by some hardware decoders and is rejected by some DVD authoring packages. If you intend to use a software decoder you&#8217;d be insane not to use variable bitrate. </p>
<p> If this option is set without a maximum bitrate being specified then quantisation is fixed at the specified value. It should be noted that not specifying a bitrate is probably an error and may produce unexpected results. </p>
<p> For MPEG-2 streams a default of 8 is used if <code>-q</code> is not explicitly given. To force constant bitrate streams use <code>&#8211;cbr</code> and <code>-b NOT -q</code>! </p>
<p> <code>-I|&#8211;interlace-mode</code>&nbsp;<wbr>0|1|2 </p>
<p> Set the sequence picture structure and block encoding type for MPEG-2 streams. By default, this value is inferred from the interlacing tag of the input stream. Setting 0 encodes frame-by-frame with support for interlaced video turned off, and specifies that progressive chroma subsampling has been used. Setting 1 encodes frame-by-frame with interlace-adapted motion compensation and block encoding, and specifies that interlaced chroma subsampling has been used. Setting 2 encodes interlaced material field-by-field, which will produce more accurate results for highly textured interlaced material with lots of motion, at the expense of generally less efficiency.</p>
<dl>
<dt>
<dd> This setting should match the interlaced-ness of the input stream, otherwise chroma artifacts may be generated when the MPEG stream is played back.</dl>
<p> <code>-g|&#8211;min-gop-size</code>&nbsp;<wbr>num </p>
<p> <code>-G|&#8211;max-gop-size</code>&nbsp;<wbr>num </p>
<p> These flags set the minimum and maximum group-of-picture (GOP) size for the output MPEG stream. The default values depend on the output format. </p>
<p> For MPEG-1 (for example VCD) the default is a fixed GOP size of 12 (-g and -G are both set to 12). </p>
<p> For MPEG-2 the default value of -G (max) is set according to the video system: -G 15 for 625 line (PAL) and 18 for 525 line (NTSC). If -g (min) has not been specified then the minimum GOP size is set to be one half of the maximum (-G). </p>
<p> To force a fixed GOP size specify both -g and -G with the same value. </p>
<p> If the minimum and maximum GOP sizes are <code>not</code> identical then mpeg2enc will start a <code>new</code> GOP if more than 60% of the macroblocks in a P or B frame are Intra encoded. This ensure big changes of image coincide with a fully-encoded I-frame by starting a new GOP. This can help prevent transient &quot;blockiness&quot;. </p>
<p> Reasonable minimum GOP sizes are 6 or 9. If a minimum is not specified but a maximum is given then the minimum will be set to one half the maximum. A larger GOP size can help reduce the bitrate required for a given quality. However, this really only applies to <code>high-quality</code> source material with <code>little noise</code> (e.g. digital video). For broadcast material there is little point setting GOP size much beyond 21 or 24. Even with good source material diminishing returns set in quite rapidly. Also it must be noted that specific MPEG-2 formats (such as for DVD) are constrained in the maximum allowable GOP size. </p>
<p> Note: mpeg2enc is currently hard-wired to produce 2 B frames between each I/P frame unless the GOP size forces less. This is reasonable for medium to high bitrates (&gt;= 1Mbps) but probably sub-optimal for low-bitrate encoding. </p>
<p> <code>-c|&#8211;closed-GOPs</code> </p>
<p> Setting this flag causes the encoder to generate only &quot;closed&quot; GOPs (Groups of Pictures) that can be decoded without reference to their predecessor. This is useful for streams that are supposed to be used in multi-angle DVD&#8217;s and applications where more easily edittable MPEG is required. </p>
<p> <code>-P|&#8211;force-b-b-p</code> </p>
<p> This flag forces the GOP size selection to choose sizes that ensure 2 B frames appear between adjacent I/P frames. Several common MPEG-1 decoders can&#8217;t handle streams where less than 2 B-frames appear between I/P frames. </p>
<p> <code>-Q|&#8211;quantisation-reduction</code>&nbsp;<wbr>-4.0..5.0 </p>
<p> This flag sets the amount quantisation is reduced for blocks containing large amounts of sharp image detail. Large values produces efficient use of bits but may cause visible artifacting around detailed sections. With noisy source material this option may cause a &quot;swimming&quot; effect on textured backgrounds as the noise cause the quantisation of blocks to be boosted at random. The default is 0.0 (off). See also the -X option. </p>
<p> <code>-X|&#8211;quant-reduction-max-var</code>&nbsp;<wbr>0.0..2500.0 </p>
<p> Luma variance below which quantisation boost (-Q) is activated. </p>
<p> <code>-r|&#8211;motion-search-radius</code>&nbsp;<wbr>num </p>
<p> This flag sets the motion estimation search radius. For most purposes the default (16) should be just fine. For high-resolution MPEG-2 and active scenes it may be worth bumping it up. However, this will make encoding significantly slower. There is little point reducing the radius. Speed gains are not huge and the impact on quality can be marked. </p>
<p> <code>-4|&#8211;reduction-4&#215;4</code>&nbsp;<wbr>1..4 </p>
<p> <code>-2|&#8211;reduction-2&#215;2</code>&nbsp;<wbr>1..4 </p>
<p> These options control how radical the encoder is in throwing away apparently poor candidate estimates during motion estimation. A setting of 1 means very few blocks are discarded early which makes for slow encoding but quality as good as it gets. A setting of 4 makes for fast encoding but can impact quality. The -4 flag controls discarding during the initial 4*4 sub-sampled search stage, the -2 flag controls discarding during the secondary 2*2 sub-sampled stage.</p>
<dl>
<dt>
<dd> These flags are useful as the speed quality trade-off is markedly different depending on which CPU you have. On modern machines the impact on speed is around a factor 2 on older machines a factor 3. The impact on quality is around 10% quantisation (0.2 of a bit of precision in encoding textures). For most purposes the default settings will be fine. However on P-III Katmai etc -4 2 -2 1 gives a good near-optimum quality setting with reasonably speed.</dl>
<p> <code>-N|&#8211;reduce-hf</code>&nbsp;<wbr>num </p>
<p> Setting this flag adjusts the way texture detail is quantised to reduce the precision with which of high-frequency information encoded. This is very useful for <i>mildly</i> noisy sources. If you have really noisy material the filtering tools available in mjpegtools are a much better bet. The specified number must be in the range 0.0 to 2.0 gives the maxium quantisation boost. A useful number to use would be 1.5 or 1.0. </p>
<p> <code>-H|&#8211;keep-hf</code> </p>
<p> Setting this flag makes the encoder encode as much high-frequency information as possible. This is a good setting for maximising quality at VCD resolution with good quality low-noise source material. It can also help with &quot;swimmy&quot; material if you can spare the bitrate! </p>
<p> <code>-D|</code>&#8211;intra_dc_prec<code>&nbsp;<wbr>num</code> </p>
<p> Specifies the precision of the DC component. The default is 9. Most commercial DVDs use 10. Using 9 instead saves a few bits. Using 10 might help to avoid looking larger areas of nearly the same color blocky. A value of 11 is only valid at the next MPEG-2 profile/level so it&#8217;s not a currently meaningful value to use. </p>
<h2>OPTION LETTERS FOR CHUNKING THE OUTPUT STREAM</h2>
<p> <code>-S|&#8211;sequence-length</code>&nbsp;<wbr>num </p>
<p> This flag allows the target size of individual sequences in the final multiplexed stream to be set in MBytes. If set mpeg2enc keeps track of how large the eventual stream is getting and inserts a sequence split (actually: sequence end / sequence start) into the output stream each time it reaches the specified limit. The multiplexer <code><a href="/docs/linux/man/1-mplex/">mplex</a></code>(1) can recognise these splits and start a new multiplexed output file each time it encounters one. In this way it is easy to automatically ensure each component sequence file can be burnt onto a CD-R and still be played as a stand-alone MPEG sequence. For the SVCD and VCD profiles the default target sequence length is 700M bytes. For other profiles the default is that sequence length is unlimited. </p>
<p> <code>-B|&#8211;nonvideo-bitrate</code>&nbsp;<wbr>num </p>
<p> Since mpeg2enc can&#8217;t read minds it cannot know in advance what other material will be multiplexed with the output video stream. Thus to get its calculations of where to insert split point right it needs to be told the combined data-rate of the other material that is eventually to be multiplexed with the video. This flag allows this rate to be specified in K bits/sec. </p>
<p> A good rule of thumb is to use the total rate of all the other streams plus 1% of the total rate including video. </p>
<p> <code>-u|&#8211;cbr</code> </p>
<p> Force the use of Constant Bit Rate encoding. Less than optimal (and inefficient in almost all cases) but some folks insist on it. <code>NOTE:</code> this <code>disables</code> (overrides) the use of the <code>-q</code> option! </p>
<p> It is an error to use this option and not specify a bitrate using <code>-b</code> since a constant bitrate of 0 makes no sense. </p>
<p> <code>&#8211;chapters</code>&nbsp;<wbr>frame,&#8230; </p>
<p> This flag allows you to define chapter points within the mpeg stream. This is most useful when generating DVD video. Each chapter point is specified by frame number, with the first frame being number 0. Every chapter point defined will end up at the beginning of a closed GOP as an I frame.</p>
<h2>SSE, 3D-Now!, MMX!</h2>
<p> mpeg2enc makes extensive use of these SIMD instruction set extension on x86 family CPU&#8217;s. The routines used are determined dynamically at run-time. It should be noted that using SSE requires operating system support. Old 2.2.x Linux kernels (unless patched ones like RedHat) do not have this and so SSE, although physically present, won&#8217;t be activated.</p>
<h2>BUGS</h2>
<p> There should be an option to force GOP sizes that permit 2 B frames between I/P frames. Some decoders (even software) can&#8217;t handle the case where I/P frames come back to back or with only 1 B frame between them. </p>
<p> There needs to be a facility for writing dummy user-data fields so that the multiplexer/imager can insert forward/backward pointers when muxing/imaging an SVCD.</p>
<h2>AUTHOR</h2>
<p> This man page was written by Andrew Stevens. If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at<br />
&nbsp;<wbr>&nbsp;<wbr><i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a> </p>
<p> </i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mplex/">mplex</a></code>(1), <code><a href="/docs/linux/man/1-mp2enc/">mp2enc</a></code>(1), <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-lav2wav/">lav2wav</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-y4mdenoise/">y4mdenoise</a></code>(1), <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) </p>
<h2>Index</h2>
