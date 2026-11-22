---

title: "ffmpeg2theora(1)"
name: "ffmpeg2theora"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg2theora/"
description: "ffmpeg2theora – command-line converter to create Ogg Theora and Ogg Vorbis files."
---

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
<dt><code>-o, &#8211;output</code></dt>
<dd> Specify the output filename. If no output filename is specified, output will be written to <i>inputfile</i>.ogv. To output to standard output, specify /dev/stdout as the output file.</dd>
<dt><code>&#8211;no-skeleton</code></dt>
<dd> Disables Ogg Skeleton metadata output.</dd>
<dt><code>&#8211;seek-index</code></dt>
<dd> Enables keyframe index in skeleton track.</dd>
<dt><code>-s, &#8211;starttime</code></dt>
<dd> Start encoding at this time (in seconds).</dd>
<dt><code>-e, &#8211;endtime</code></dt>
<dd> End encoding at this time (in seconds).</dd>
<dt><code>-p, &#8211;preset</code></dt>
<dd> Encode file with v2v preset. Right now, there is preview, pro and videobin. Run &#8220;ffmpeg2theora -p info&#8221; for more information.</dd></dl>
<h3>Video output options:</h3>
<dl>
<dt><code>-v, &#8211;videoquality</code></dt>
<dd> [0 to 10] Set encoding quality for video (default: 6).<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use higher values for better quality</dd>
<dt><code>-V, &#8211;videobitrate</code></dt>
<dd> Set encoding bitrate for video (in kb/s).</dd>
<dt><code>&#8211;soft-target</code></dt>
<dd> Use a large reservoir and treat the rate as a soft target; rate control is less strict but resulting quality is usually higher/smoother overall. Soft target also allows an optional -v setting to specify a minimum allowed quality.</dd>
<dt><code>&#8211;two-pass</code></dt>
<dd> Compress input using two-pass rate control. This option requires that the input to the to the encoder is seekable and performs both passes automatically.</dd>
<dt><code>&#8211;first-pass &lt;filename&gt;</code></dt>
<dd> Perform first-pass of a two-pass rate controlled encoding, saving pass data to &lt;filename&gt; for a later second pass</dd>
<dt><code>&#8211;second-pass &lt;filename&gt;</code></dt>
<dd> Perform second-pass of a two-pass rate controlled encoding, reading first-pass data from &lt;filename&gt;. The first pass data must come from a first encoding pass using identical input video to work properly. </dd>
<dt><code>&#8211;optimize</code></dt>
<dd> Optimize output Theora video, using a full search for motion vectors instead of a hierarchical one. This can reduce video bitrate about 5%, but it is slower and therefore is disabled by default.</dd>
<dt><code>&#8211;speedlevel</code></dt>
<dd> encoding is faster with higher values the cost is quality and bandwidth (default 1) available values depend on the version of libtheora check ffmpeg2theora &#8211;help for supported values.</dd>
<dt><code>-x, &#8211;width</code></dt>
<dd> Scale to given width (in pixels).</dd>
<dt><code>-y, &#8211;height</code></dt>
<dd> Scale to given height (in pixels).</dd>
<dt><code>&#8211;aspect</code></dt>
<dd> Define frame aspect ratio (e.g. 4:3, 16:9).</dd>
<dt><code>&#8211;pixel-aspect</code></dt>
<dd> Define pixel aspect ratio (e.g. 1:1, 4:3).</dd>
<dt><code>-F, &#8211;framerate </code></dt>
<dd> output framerate e.g 25:2 or 16</dd>
<dt><code>&#8211;croptop, &#8211;cropbottom, &#8211;cropleft, &#8211;cropright</code></dt>
<dd> Crop input by given pixels before resizing.</dd>
<dt><code>-K, &#8211;keyint</code></dt>
<dd> [8 to 2147483647] Set keyframe interval (default: 64).</dd>
<dt><code>-d, &#8211;buf-delay</code></dt>
<dd> Buffer delay (in frames). Longer delays allow smoother rate adaptation and provide better overall quality, but require more client side buffering and add latency. The default value is the keyframe interval for one-pass encoding (or somewhat larger if &#8211;soft-target is used) and infinite for two-pass encoding. (only works in bitrate mode)</dd>
<dt><code>&#8211;no-upscaling</code></dt>
<dd> only scale video or resample audio if input is bigger than provided parameter</dd></dl>
<h3>Video transfer options:</h3>
<dl>
<dt><code>&#8211;pp</code></dt>
<dd> Video Postprocessing, denoise, deblock, deinterlacer use &#8211;pp help for a list of available filters.</dd>
<dt><code>-C, &#8211;contrast</code></dt>
<dd> [0.1 to 10.0] contrast correction (default: 1.0). Note: lower values make the video darker.</dd>
<dt><code>-B, &#8211;brightness </code></dt>
<dd> [-1.0 to 1.0] brightness correction (default: 0.0). Note: lower values make the video darker.</dd>
<dt><code>-G, &#8211;gamma </code></dt>
<dd> [0.1 to 10.0] gamma correction (default: 1.0). Note: lower values make the video darker.</dd>
<dt><code>-P, &#8211;saturation </code></dt>
<dd> [0.1 to 10.0] saturation correction (default: 1.0). Note: lower values make the video grey.</dd></dl>
<h3>Audio output options:</h3>
<dl>
<dt><code>-a, &#8211;audioquality</code></dt>
<dd> [-2 to 10] Set encoding quality for audio (default: 1).<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use higher values for better quality</dd>
<dt><code>-A, &#8211;audiobitrate</code></dt>
<dd> [32 to 500] Set encoding bitrate for audio (in kb/s).</dd>
<dt><code>-c, &#8211;channels</code></dt>
<dd> Set number of output channels.</dd>
<dt><code>-H, &#8211;samplerate</code></dt>
<dd> Set output samplerate (in Hz).</dd></dl>
<h3>Input options:</h3>
<dl>
<dt><code>&#8211;noaudio</code></dt>
<dd> Disable audio from input.</dd>
<dt><code>&#8211;novideo</code></dt>
<dd> Disable video from input.</dd>
<dt><code>&#8211;deinterlace</code></dt>
<dd> Force deinterlace. Otherwise only material marked as interlaced will be deinterlaced.</dd>
<dt><code>&#8211;no-deinterlace</code></dt>
<dd> Force deinterlace off.</dd>
<dt><code>&#8211;vhook</code></dt>
<dd> you can use ffmpeg&#8217;s vhook system, example:<br/>
&nbsp;<wbr>ffmpeg2theora &#8211;vhook&nbsp;<wbr>&#8216;/path/watermark.so -f wm.gif&#8217;&nbsp;<wbr>input.dv</dd>
<dt><code>-f, &#8211;format</code></dt>
<dd> Specify input format.</dd>
<dt><code>&#8211;inputfps</code></dt>
<dd> Override input fps.</dd>
<dt><code>&#8211;audiostream id</code></dt>
<dd> By default the first audio stream is selected, use this to select another audio stream.</dd>
<dt><code>&#8211;videostream id</code></dt>
<dd> By default the first video stream is selected, use this to select another audio stream.</dd>
<dt><code>&#8211;sync</code></dt>
<dd> Use A/V sync from input container. Since this does not work with all input format you have to manualy enable it if you have issues with A/V sync.</dd></dl>
<h3>Subtitles options:</h3>
<dl>
<dt><code>&#8211;subtitles</code></dt>
<dd> Encode subtitles from the given file to a multiplexed Kate stream. The input file should be in SubRip (.srt) format, encoded in UTF-8, unless the &#8211;subtitles-encoding option is also given.</dd>
<dt><code>&#8211;subtitles-encoding encoding</code></dt>
<dd> Assumes the corresponding subtitles file is encoded in the given encoding. If ffmpeg2theora was built with iconv support, all encodings supported by iconv may be used. Otherwise, UTF-8 and ISO-8859-1 (aka latin1) are supported. The default is UTF-8.</dd>
<dt><code>&#8211;subtitles-language language</code></dt>
<dd> Sets the language of the corresponding subtitles stream. This will be set in the corresponding Kate stream so a video player may make this available to the user for language selection. Language is an ISO 639-1 or RFC 3066 ASCII string and is limited to 15 characters.</dd>
<dt><code>&#8211;subtitles-category category</code></dt>
<dd> Sets the category of the corresponding subtitles stream. This will be set in the corresponding Kate stream so a video player may make this available to the user for selection. The default category is &quot;subtitles&quot;. Suggested other categories may include &quot;transcript&quot;, &quot;commentary&quot;, &quot;lyrics&quot;, etc. Category is an ASCII string and is limited to 15 characters</dd>
<dt><code>&#8211;subtitles-ignore-non-utf8</code></dt>
<dd> When reading an UTF-8 subtitles text file, any invalid UTF-8 sequence will be ignored. This may be useful if there are stray sequences in an otherwise UTF-8 file. Note that, since those invalid sequences will be removed from the output, this option is not a substitute to converting a non UTF-8 file to UTF-8.</dd>
<dt><code>&#8211;nosubtitles</code></dt>
<dd> Disables subtitles from input. Note that subtitles explicitely loaded from external files will still be used.</dd>
<dt><code>&#8211;subtitle-types</code></dt>
<dd> Selects which subtitle types to include from the input file. Allowed types are: none, all, text, spu (spu being the image based subtitles found on DVD). By default, only text based subtitles will be included. Note that subtitles explicitely loaded from external files will still be used.</dd></dl>
<h3>Metadata options:</h3>
<dl>
<dt><code>&#8211;artist</code></dt>
<dd> Name of artist (director).</dd>
<dt><code>&#8211;title</code></dt>
<dd> Title.</dd>
<dt><code>&#8211;date</code></dt>
<dd> Date.</dd>
<dt><code>&#8211;location</code></dt>
<dd> Location.</dd>
<dt><code>&#8211;organization</code></dt>
<dd> Name of organization (studio).</dd>
<dt><code>&#8211;copyright</code></dt>
<dd> Copyright.</dd>
<dt><code>&#8211;license</code></dt>
<dd> License.</dd>
<dt><code>&#8211;contact</code></dt>
<dd> Contact link.</dd>
<dt><code>&#8211;nometadata</code></dt>
<dd> disables metadata from input</dd>
<dt><code>&#8211;no-oshash</code></dt>
<dd> do not include oshash of source file(SOURCE_OSHASH) </dd>
</dl>
<h3>Keyframe indexing options:</h3>
<dl>
<dt><code>&#8211;index-interval &lt;n&gt;</code></dt>
<dd> set minimum distance between indexed keyframes to &lt;n&gt; ms (default: 2000)</dd>
<dt><code>&#8211;theora-index-reserve &lt;n&gt;</code></dt>
<dd> reserve &lt;n&gt; bytes for theora keyframe index</dd>
<dt><code>&#8211;vorbis-index-reserve &lt;n&gt;</code></dt>
<dd> reserve &lt;n&gt; bytes for vorbis keyframe index</dd>
<dt><code>&#8211;kate-index-reserve &lt;n&gt;</code></dt>
<dd> reserve &lt;n&gt; bytes for kate keyframe index </dd>
</dl>
<h3>Other options:</h3>
<dl>
<dt><code>&#8211;nice n</code></dt>
<dd> Set niceness to n.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Output a help message.</dd>
<dt><code>&#8211;info</code></dt>
<dd> Output json info about input file, use -o to save json to file.</dd>
<dt><code>&#8211;frontend</code></dt>
<dd> print status information in json, one json dict per line</dd></dl>
<h2>EXAMPLES</h2>
<p> Encode Videos:<br/>
&nbsp;<wbr>&nbsp;<wbr>ffmpeg2theora videoclip.avi&nbsp;<wbr>(will write output to videoclip.ogv)<br/>
&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>&nbsp;<wbr>cat something.dv | ffmpeg2theora -f dv -o output.ogv &#8211; </p>
<p> Encode a series of images:<br/>
&nbsp;<wbr>&nbsp;<wbr>ffmpeg2theora frame%06d.png -o output.ogv </p>
<p> Live streaming from V4L Device:<br/>
&nbsp;<wbr>&nbsp;<wbr>ffmpeg2theora &#8211;no-skeleton&nbsp;<wbr>/dev/video0 -f video4linux&nbsp;<wbr>\<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;inputfps 15 -x 160 -y 128&nbsp;<wbr>\<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o &#8211; | oggfwd icast2server 8000 password&nbsp;<wbr>/theora.ogv </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(you might have to use video4linux2 depending on your hardware)<br/>
&nbsp;<wbr>&nbsp;<wbr> Live encoding from a DV camcorder (needs a fast machine):<br/>
&nbsp;<wbr>&nbsp;<wbr>dvgrab &#8211; | ffmpeg2theora -f dv -x 352 -y 288 -o output.ogv &#8211; </p>
<p> Live encoding and streaming to icecast server:<br/>
&nbsp;<wbr>&nbsp;<wbr>dvgrab &#8211;format raw &#8211;&nbsp;<wbr>\<br/>
&nbsp;<wbr>&nbsp;<wbr>| ffmpeg2theora &#8211;no-skeleton -f dv -x 160 -y 128 -o&nbsp;<wbr>/dev/stdout &#8211;&nbsp;<wbr>\<br/>
&nbsp;<wbr>&nbsp;<wbr>| oggfwd icast2server 8000 password&nbsp;<wbr>/theora.ogv </p>
<h2>AUTHOR</h2>
<p> ffmpeg2theora was written by jan gerber &lt;j@v2v.cc&gt;. </p>
<p> This manual page was written by Hubert Chan &lt;hubert [at] uhoreg.ca&gt;, for the Debian project (but may be used by others). </p>
