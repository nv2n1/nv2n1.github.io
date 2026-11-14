---
title: "ffmpeg2theora(1)"
name: "ffmpeg2theora"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg2theora/"
description: "ffmpeg2theora – command-line converter to create Ogg Theora and Ogg Vorbis files."
---

<h2 class="name">NAME</h2>
<p> ffmpeg2theora &#8211; command-line converter to create Ogg Theora and Ogg Vorbis files. </p>
<h2>SYNOPSIS</h2>
<p> <code>ffmpeg2theora</code> [<i>options</i>]<i> inputfile</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ffmpeg2theora</code> command. </p>
<p> <code>ffmpeg2theora</code> is a program that converts any media file that ffmpeg can decode to Ogg Theora for video and Ogg Vorbis for audio.</p>
<h2>OPTIONS</h2>
<p> To read from standard input, specify `-&#8216; as the input filename. </p>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<h3>General output options:</h3>
<dl>
<dt><code>-o, &#8211;output</code></p>
<dd> Specify the output filename. If no output filename is specified, output will be written to <i>inputfile</i>.ogv. To output to standard output, specify /dev/stdout as the output file.</p>
<dt><code>&#8211;no-skeleton</code></p>
<dd> Disables Ogg Skeleton metadata output.</p>
<dt><code>&#8211;seek-index</code></p>
<dd> Enables keyframe index in skeleton track.</p>
<dt><code>-s, &#8211;starttime</code></p>
<dd> Start encoding at this time (in seconds).</p>
<dt><code>-e, &#8211;endtime</code></p>
<dd> End encoding at this time (in seconds).</p>
<dt><code>-p, &#8211;preset</code></p>
<dd> Encode file with v2v preset. Right now, there is preview, pro and videobin. Run &#8220;ffmpeg2theora -p info&#8221; for more information.</dl>
<h3>Video output options:</h3>
<dl>
<dt><code>-v, &#8211;videoquality</code></p>
<dd> [0 to 10] Set encoding quality for video (default: 6).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use higher values for better quality</p>
<dt><code>-V, &#8211;videobitrate</code></p>
<dd> Set encoding bitrate for video (in kb/s).</p>
<dt><code>&#8211;soft-target</code></p>
<dd> Use a large reservoir and treat the rate as a soft target; rate control is less strict but resulting quality is usually higher/smoother overall. Soft target also allows an optional -v setting to specify a minimum allowed quality.</p>
<dt><code>&#8211;two-pass</code></p>
<dd> Compress input using two-pass rate control. This option requires that the input to the to the encoder is seekable and performs both passes automatically.</p>
<dt><code>&#8211;first-pass &lt;filename&gt;</code></p>
<dd> Perform first-pass of a two-pass rate controlled encoding, saving pass data to &lt;filename&gt; for a later second pass</p>
<dt><code>&#8211;second-pass &lt;filename&gt;</code></p>
<dd> Perform second-pass of a two-pass rate controlled encoding, reading first-pass data from &lt;filename&gt;. The first pass data must come from a first encoding pass using identical input video to work properly. </p>
<dt><code>&#8211;optimize</code></p>
<dd> Optimize output Theora video, using a full search for motion vectors instead of a hierarchical one. This can reduce video bitrate about 5%, but it is slower and therefore is disabled by default.</p>
<dt><code>&#8211;speedlevel</code></p>
<dd> encoding is faster with higher values the cost is quality and bandwidth (default 1) available values depend on the version of libtheora check ffmpeg2theora &#8211;help for supported values.</p>
<dt><code>-x, &#8211;width</code></p>
<dd> Scale to given width (in pixels).</p>
<dt><code>-y, &#8211;height</code></p>
<dd> Scale to given height (in pixels).</p>
<dt><code>&#8211;aspect</code></p>
<dd> Define frame aspect ratio (e.g. 4:3, 16:9).</p>
<dt><code>&#8211;pixel-aspect</code></p>
<dd> Define pixel aspect ratio (e.g. 1:1, 4:3).</p>
<dt><code>-F, &#8211;framerate </code></p>
<dd> output framerate e.g 25:2 or 16</p>
<dt><code>&#8211;croptop, &#8211;cropbottom, &#8211;cropleft, &#8211;cropright</code></p>
<dd> Crop input by given pixels before resizing.</p>
<dt><code>-K, &#8211;keyint</code></p>
<dd> [8 to 2147483647] Set keyframe interval (default: 64).</p>
<dt><code>-d, &#8211;buf-delay</code></p>
<dd> Buffer delay (in frames). Longer delays allow smoother rate adaptation and provide better overall quality, but require more client side buffering and add latency. The default value is the keyframe interval for one-pass encoding (or somewhat larger if &#8211;soft-target is used) and infinite for two-pass encoding. (only works in bitrate mode)</p>
<dt><code>&#8211;no-upscaling</code></p>
<dd> only scale video or resample audio if input is bigger than provided parameter</dl>
<h3>Video transfer options:</h3>
<dl>
<dt><code>&#8211;pp</code></p>
<dd> Video Postprocessing, denoise, deblock, deinterlacer use &#8211;pp help for a list of available filters.</p>
<dt><code>-C, &#8211;contrast</code></p>
<dd> [0.1 to 10.0] contrast correction (default: 1.0). Note: lower values make the video darker.</p>
<dt><code>-B, &#8211;brightness </code></p>
<dd> [-1.0 to 1.0] brightness correction (default: 0.0). Note: lower values make the video darker.</p>
<dt><code>-G, &#8211;gamma </code></p>
<dd> [0.1 to 10.0] gamma correction (default: 1.0). Note: lower values make the video darker.</p>
<dt><code>-P, &#8211;saturation </code></p>
<dd> [0.1 to 10.0] saturation correction (default: 1.0). Note: lower values make the video grey.</dl>
<h3>Audio output options:</h3>
<dl>
<dt><code>-a, &#8211;audioquality</code></p>
<dd> [-2 to 10] Set encoding quality for audio (default: 1).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use higher values for better quality</p>
<dt><code>-A, &#8211;audiobitrate</code></p>
<dd> [32 to 500] Set encoding bitrate for audio (in kb/s).</p>
<dt><code>-c, &#8211;channels</code></p>
<dd> Set number of output channels.</p>
<dt><code>-H, &#8211;samplerate</code></p>
<dd> Set output samplerate (in Hz).</dl>
<h3>Input options:</h3>
<dl>
<dt><code>&#8211;noaudio</code></p>
<dd> Disable audio from input.</p>
<dt><code>&#8211;novideo</code></p>
<dd> Disable video from input.</p>
<dt><code>&#8211;deinterlace</code></p>
<dd> Force deinterlace. Otherwise only material marked as interlaced will be deinterlaced.</p>
<dt><code>&#8211;no-deinterlace</code></p>
<dd> Force deinterlace off.</p>
<dt><code>&#8211;vhook</code></p>
<dd> you can use ffmpeg&#8217;s vhook system, example:<br />
&nbsp;<wbr>ffmpeg2theora &#8211;vhook&nbsp;<wbr>&#8216;/path/watermark.so -f wm.gif&#8217;&nbsp;<wbr>input.dv</p>
<dt><code>-f, &#8211;format</code></p>
<dd> Specify input format.</p>
<dt><code>&#8211;inputfps</code></p>
<dd> Override input fps.</p>
<dt><code>&#8211;audiostream id</code></p>
<dd> By default the first audio stream is selected, use this to select another audio stream.</p>
<dt><code>&#8211;videostream id</code></p>
<dd> By default the first video stream is selected, use this to select another audio stream.</p>
<dt><code>&#8211;sync</code></p>
<dd> Use A/V sync from input container. Since this does not work with all input format you have to manualy enable it if you have issues with A/V sync.</dl>
<h3>Subtitles options:</h3>
<dl>
<dt><code>&#8211;subtitles</code></p>
<dd> Encode subtitles from the given file to a multiplexed Kate stream. The input file should be in SubRip (.srt) format, encoded in UTF-8, unless the &#8211;subtitles-encoding option is also given.</p>
<dt><code>&#8211;subtitles-encoding encoding</code></p>
<dd> Assumes the corresponding subtitles file is encoded in the given encoding. If ffmpeg2theora was built with iconv support, all encodings supported by iconv may be used. Otherwise, UTF-8 and ISO-8859-1 (aka latin1) are supported. The default is UTF-8.</p>
<dt><code>&#8211;subtitles-language language</code></p>
<dd> Sets the language of the corresponding subtitles stream. This will be set in the corresponding Kate stream so a video player may make this available to the user for language selection. Language is an ISO 639-1 or RFC 3066 ASCII string and is limited to 15 characters.</p>
<dt><code>&#8211;subtitles-category category</code></p>
<dd> Sets the category of the corresponding subtitles stream. This will be set in the corresponding Kate stream so a video player may make this available to the user for selection. The default category is &quot;subtitles&quot;. Suggested other categories may include &quot;transcript&quot;, &quot;commentary&quot;, &quot;lyrics&quot;, etc. Category is an ASCII string and is limited to 15 characters</p>
<dt><code>&#8211;subtitles-ignore-non-utf8</code></p>
<dd> When reading an UTF-8 subtitles text file, any invalid UTF-8 sequence will be ignored. This may be useful if there are stray sequences in an otherwise UTF-8 file. Note that, since those invalid sequences will be removed from the output, this option is not a substitute to converting a non UTF-8 file to UTF-8.</p>
<dt><code>&#8211;nosubtitles</code></p>
<dd> Disables subtitles from input. Note that subtitles explicitely loaded from external files will still be used.</p>
<dt><code>&#8211;subtitle-types</code></p>
<dd> Selects which subtitle types to include from the input file. Allowed types are: none, all, text, spu (spu being the image based subtitles found on DVD). By default, only text based subtitles will be included. Note that subtitles explicitely loaded from external files will still be used.</dl>
<h3>Metadata options:</h3>
<dl>
<dt><code>&#8211;artist</code></p>
<dd> Name of artist (director).</p>
<dt><code>&#8211;title</code></p>
<dd> Title.</p>
<dt><code>&#8211;date</code></p>
<dd> Date.</p>
<dt><code>&#8211;location</code></p>
<dd> Location.</p>
<dt><code>&#8211;organization</code></p>
<dd> Name of organization (studio).</p>
<dt><code>&#8211;copyright</code></p>
<dd> Copyright.</p>
<dt><code>&#8211;license</code></p>
<dd> License.</p>
<dt><code>&#8211;contact</code></p>
<dd> Contact link.</p>
<dt><code>&#8211;nometadata</code></p>
<dd> disables metadata from input</p>
<dt><code>&#8211;no-oshash</code></p>
<dd> do not include oshash of source file(SOURCE_OSHASH) </p>
</dl>
<h3>Keyframe indexing options:</h3>
<dl>
<dt><code>&#8211;index-interval &lt;n&gt;</code></p>
<dd> set minimum distance between indexed keyframes to &lt;n&gt; ms (default: 2000)</p>
<dt><code>&#8211;theora-index-reserve &lt;n&gt;</code></p>
<dd> reserve &lt;n&gt; bytes for theora keyframe index</p>
<dt><code>&#8211;vorbis-index-reserve &lt;n&gt;</code></p>
<dd> reserve &lt;n&gt; bytes for vorbis keyframe index</p>
<dt><code>&#8211;kate-index-reserve &lt;n&gt;</code></p>
<dd> reserve &lt;n&gt; bytes for kate keyframe index </p>
</dl>
<h3>Other options:</h3>
<dl>
<dt><code>&#8211;nice n</code></p>
<dd> Set niceness to n.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Output a help message.</p>
<dt><code>&#8211;info</code></p>
<dd> Output json info about input file, use -o to save json to file.</p>
<dt><code>&#8211;frontend</code></p>
<dd> print status information in json, one json dict per line</dl>
<h2>EXAMPLES</h2>
<p> Encode Videos:<br />
&nbsp;<wbr>&nbsp;<wbr>ffmpeg2theora videoclip.avi&nbsp;<wbr>(will write output to videoclip.ogv)<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>cat something.dv | ffmpeg2theora -f dv -o output.ogv &#8211; </p>
<p> Encode a series of images:<br />
&nbsp;<wbr>&nbsp;<wbr>ffmpeg2theora frame%06d.png -o output.ogv </p>
<p> Live streaming from V4L Device:<br />
&nbsp;<wbr>&nbsp;<wbr>ffmpeg2theora &#8211;no-skeleton&nbsp;<wbr>/dev/video0 -f video4linux&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;inputfps 15 -x 160 -y 128&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o &#8211; | oggfwd icast2server 8000 password&nbsp;<wbr>/theora.ogv </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(you might have to use video4linux2 depending on your hardware)<br />
&nbsp;<wbr>&nbsp;<wbr> Live encoding from a DV camcorder (needs a fast machine):<br />
&nbsp;<wbr>&nbsp;<wbr>dvgrab &#8211; | ffmpeg2theora -f dv -x 352 -y 288 -o output.ogv &#8211; </p>
<p> Live encoding and streaming to icecast server:<br />
&nbsp;<wbr>&nbsp;<wbr>dvgrab &#8211;format raw &#8211;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>| ffmpeg2theora &#8211;no-skeleton -f dv -x 160 -y 128 -o&nbsp;<wbr>/dev/stdout &#8211;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>| oggfwd icast2server 8000 password&nbsp;<wbr>/theora.ogv </p>
<h2>AUTHOR</h2>
<p> ffmpeg2theora was written by jan gerber &lt;j@v2v.cc&gt;. </p>
<p> This manual page was written by Hubert Chan &lt;hubert [at] uhoreg.ca&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
