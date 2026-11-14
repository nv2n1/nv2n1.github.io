---
title: "gst-launch-0(1)"
name: "gst-launch-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-launch-0/"
description: "gst-launch – build and run a GStreamer pipeline"
---

<h2>NAME</h2>
<p> gst-launch &#8211; build and run a GStreamer pipeline</p>
<h2>SYNOPSIS</h2>
<p> <code>gst-launch</code> <i>[OPTION&#8230;]</i> PIPELINE-DESCRIPTION</p>
<h2>DESCRIPTION</h2>
<p> <i>gst-launch</i> is a tool that builds and runs basic <i>GStreamer</i> pipelines. </p>
<p> In simple form, a PIPELINE-DESCRIPTION is a list of elements separated by exclamation marks (!). Properties may be appended to elements, in the form <i>property=value</i>. </p>
<p> For a complete description of possible PIPELINE-DESCRIPTIONS see the section <i>pipeline description</i> below or consult the GStreamer documentation. </p>
<p> Please note that <i>gst-launch</i> is primarily a debugging tool for developers and users. You should not build applications on top of it. For applications, use the gst_parse_launch() function of the GStreamer API as an easy way to construct pipelines from pipeline descriptions.</p>
<h2>OPTIONS</h2>
<p> <i>gst-launch</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help synopsis and available FLAGS</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Output status information and property notifications</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Do not print any progress information</p>
<dt><code>-m, &#8211;messages</code></p>
<dd> Output messages posted on the pipeline&#8217;s bus</p>
<dt><code>-t, &#8211;tags</code></p>
<dd> Output tags (also known as metadata)</p>
<dt><code>-e, &#8211;eos-on-shutdown</code></p>
<dd> Force an EOS event on sources before shutting the pipeline down. This is useful to make sure muxers create readable files when a muxing pipeline is shut down forcefully via Control-C.</p>
<dt><code>-i, &#8211;index</code></p>
<dd> Gather and print index statistics. This is mostly useful for playback or recording pipelines.</p>
<dt><code>-o FILE, &#8211;output=FILE</code></p>
<dd> Save XML representation of pipeline to FILE and exit (DEPRECATED, DO NOT USE)</p>
<dt><code>-f, &#8211;no-fault</code></p>
<dd> Do not install a fault handler</p>
<dt><code>&#8211;no-sigusr-handler</code></p>
<dd> Do not install signal handlers for SIGUSR1 (play) and SIGUSR2 (stop)</p>
<dt><code>-T, &#8211;trace</code></p>
<dd> Print memory allocation traces. The feature must be enabled at compile time to work.</p>
<dt>
<dd></dl>
<h2>GSTREAMER OPTIONS</h2>
<p> <i>gst-launch</i> also accepts the following options that are common to all GStreamer applications:</p>
<dl>
<dt><code>&#8211;gst-version</code></p>
<dd> Prints the version string of the <i>GStreamer</i> core library.</p>
<dt><code>&#8211;gst-fatal-warnings</code></p>
<dd> Causes <i>GStreamer</i> to abort if a warning message occurs. This is equivalent to setting the environment variable G_DEBUG to &#8216;fatal_warnings&#8217; (see the section <i>environment variables</i> below for further information).</p>
<dt><code>&#8211;gst-debug=STRING</code></p>
<dd> A comma separated list of category_name:level pairs to specify debugging levels for each category. Level is in the range 0-5 where 0 will show no messages, and 5 will show all messages. The wildcard * can be used to match category names. </p>
<p> Use &#8211;gst-debug-help to show category names </p>
<p> Example: GST_CAT:5,GST_ELEMENT_*:3,oggdemux:5 </p>
<dt><code>&#8211;gst-debug-level=LEVEL</code></p>
<dd> Sets the threshold for printing debugging messages. A higher level will print more messages. The useful range is 0-5, with the default being 0.</p>
<dt><code>&#8211;gst-debug-no-color</code></p>
<dd> <i>GStreamer</i> normally prints debugging messages so that the messages are color-coded when printed to a terminal that handles ANSI escape sequences. Using this option causes <i>GStreamer</i> to print messages without color. Setting the <code>GST_DEBUG_NO_COLOR</code> environment variable will achieve the same thing.</p>
<dt><code>&#8211;gst-debug-disable</code></p>
<dd> Disables debugging.</p>
<dt><code>&#8211;gst-debug-help</code></p>
<dd> Prints a list of available debug categories and their default debugging level.</p>
<dt><code>&#8211;gst-plugin-spew</code></p>
<dd> <i>GStreamer</i> info flags to set Enable printout of errors while loading <i>GStreamer</i> plugins</p>
<dt><code>&#8211;gst-plugin-path=PATH</code></p>
<dd> Add directories separated with &#8216;:&#8217; to the plugin search path</p>
<dt><code>&#8211;gst-plugin-load=PLUGINS</code></p>
<dd> Preload plugins specified in a comma-separated list. Another way to specify plugins to preload is to use the environment variable GST_PLUGIN_PATH </p>
</dl>
<h2>PIPELINE DESCRIPTION</h2>
<p> A pipeline consists <i>elements</i> and <i>links</i>. <i>Elements</i> can be put into <i>bins</i> of different sorts. <i>Elements</i>, <i>links</i> and <i>bins</i> can be specified in a pipeline description in any order. </p>
<p> <code>Elements</code> </p>
<p> ELEMENTTYPE <i>[PROPERTY1 &#8230;]</i> </p>
<p> Creates an element of type ELEMENTTYPE and sets the PROPERTIES. </p>
<p> <code>Properties</code> </p>
<p> PROPERTY=VALUE &#8230; </p>
<p> Sets the property to the specified value. You can use <code><a href="/docs/linux/man/1-gst-inspect/">gst-inspect</a></code>(1) to find out about properties and allowed values of different elements.<br />
 Enumeration properties can be set by name, nick or value. </p>
<p> <code>Bins</code> </p>
<p> <i>[BINTYPE.]</i> ( <i>[PROPERTY1 &#8230;]</i> PIPELINE-DESCRIPTION ) </p>
<p> Specifies that a bin of type BINTYPE is created and the given properties are set. Every element between the braces is put into the bin. Please note the dot that has to be used after the BINTYPE. You will almost never need this functionality, it is only really useful for applications using the gst_launch_parse() API with &#8216;bin&#8217; as bintype. That way it is possible to build partial pipelines instead of a full-fledged top-level pipeline. </p>
<p> <code>Links</code> </p>
<p> <i>[[SRCELEMENT].[PAD1,&#8230;]]</i> ! <i>[[SINKELEMENT].[PAD1,&#8230;]]</i> <i>[[SRCELEMENT].[PAD1,&#8230;]]</i> ! CAPS ! <i>[[SINKELEMENT].[PAD1,&#8230;]]</i> </p>
<p> Links the element with name SRCELEMENT to the element with name SINKELEMENT, using the caps specified in CAPS as a filter. Names can be set on elements with the name property. If the name is omitted, the element that was specified directly in front of or after the link is used. This works across bins. If a padname is given, the link is done with these pads. If no pad names are given all possibilities are tried and a matching pad is used. If multiple padnames are given, both sides must have the same number of pads specified and multiple links are done in the given order.<br />
 So the simplest link is a simple exclamation mark, that links the element to the left of it to the element right of it. </p>
<p> <code>Caps</code> </p>
<p> MIMETYPE <i>[, PROPERTY[, PROPERTY &#8230;]]]</i> <i>[; CAPS[; CAPS &#8230;]]</i> </p>
<p> Creates a capability with the given mimetype and optionally with given properties. The mimetype can be escaped using &quot; or &#8216;. If you want to chain caps, you can add more caps in the same format afterwards. </p>
<p> <code>Properties</code> </p>
<p> NAME=<i>[(TYPE)]</i>VALUE<br />
 in lists and ranges: <i>[(TYPE)]</i>VALUE </p>
<p> Sets the requested property in capabilities. The name is an alphanumeric value and the type can have the following case-insensitive values:<br />
 &#8211; <code>i</code> or <code>int</code> for integer values or ranges<br />
 &#8211; <code>f</code> or <code>float</code> for float values or ranges<br />
 &#8211; <code>4</code> or <code>fourcc</code> for FOURCC values<br />
 &#8211; <code>b</code>, <code>bool</code> or <code>boolean</code> for boolean values<br />
 &#8211; <code>s</code>, <code>str</code> or <code>string</code> for strings<br />
 &#8211; <code>fraction</code> for fractions (framerate, pixel-aspect-ratio)<br />
 &#8211; <code>l</code> or <code>list</code> for lists<br />
 If no type was given, the following order is tried: integer, float, boolean, string.<br />
 Integer values must be parsable by <code>strtol()</code>, floats by <code>strtod()</code>. FOURCC values may either be integers or strings. Boolean values are (case insensitive) <i>yes</i>, <i>no</i>, <i>true</i> or <i>false</i> and may like strings be escaped with &quot; or &#8216;.<br />
 Ranges are in this format: [ VALUE, VALUE ]<br />
 Lists use this format: ( VALUE <i>[, VALUE &#8230;]</i> ) </p>
<h2>PIPELINE CONTROL</h2>
<p> A pipeline can be controlled by signals. SIGUSR2 will stop the pipeline (GST_STATE_NULL); SIGUSR1 will put it back to play (GST_STATE_PLAYING). By default, the pipeline will start in the playing state.<br />
 There are currently no signals defined to go into the ready or pause (GST_STATE_READY and GST_STATE_PAUSED) state explicitly. </p>
<h2>PIPELINE EXAMPLES</h2>
<p> The examples below assume that you have the correct plug-ins available. In general, &quot;osssink&quot; can be substituted with another audio output plug-in such as &quot;esdsink&quot;, &quot;alsasink&quot;, &quot;osxaudiosink&quot;, or &quot;artsdsink&quot;. Likewise, &quot;xvimagesink&quot; can be substituted with &quot;ximagesink&quot;, &quot;sdlvideosink&quot;, &quot;osxvideosink&quot;, or &quot;aasink&quot;. Keep in mind though that different sinks might accept different formats and even the same sink might accept different formats on different machines, so you might need to add converter elements like audioconvert and audioresample (for audio) or ffmpegcolorspace (for video) in front of the sink to make things work. </p>
<p> <code>Audio playback</code> </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.mp3&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Play the mp3 music file &quot;music.mp3&quot; using a libmad-based plug-in and output to an OSS device </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.ogg&nbsp;<wbr>!&nbsp;<wbr>oggdemux&nbsp;<wbr>!&nbsp;<wbr>vorbisdec&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Play an Ogg Vorbis format file </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch gnomevfssrc location=music.mp3&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch gnomevfssrc location=<a rel="nofollow" href="http://domain.com/music.mp3">http://domain.com/music.mp3</a>&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Play an mp3 file or an http stream using GNOME-VFS </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch gnomevfssrc location=<a href="smb://computer/music.mp3">smb://computer/music.mp3</a>&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Use GNOME-VFS to play an mp3 file located on an SMB server </p>
<p> <code>Format conversion</code> </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.mp3&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>vorbisenc&nbsp;<wbr>!&nbsp;<wbr>oggmux&nbsp;<wbr>!&nbsp;<wbr>filesink location=music.ogg</code><br />
 Convert an mp3 music file to an Ogg Vorbis file </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.mp3&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>flacenc&nbsp;<wbr>!&nbsp;<wbr>filesink location=test.flac</code><br />
 Convert to the FLAC format </p>
<p> <code>Other</code> </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.wav&nbsp;<wbr>!&nbsp;<wbr>wavparse&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Plays a .WAV file that contains raw audio data (PCM). </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.wav&nbsp;<wbr>!&nbsp;<wbr>wavparse&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>vorbisenc&nbsp;<wbr>!&nbsp;<wbr>oggmux&nbsp;<wbr>!&nbsp;<wbr>filesink location=music.ogg</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=music.wav&nbsp;<wbr>!&nbsp;<wbr>wavparse&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>lame&nbsp;<wbr>!&nbsp;<wbr>filesink location=music.mp3</code><br />
 Convert a .WAV file containing raw audio data into an Ogg Vorbis or mp3 file </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch cdparanoiasrc mode=continuous&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>lame&nbsp;<wbr>!&nbsp;<wbr>id3v2mux&nbsp;<wbr>!&nbsp;<wbr>filesink location=cd.mp3</code><br />
 rips all tracks from compact disc and convert them into a single mp3 file </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch cdparanoiasrc track=5&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>lame&nbsp;<wbr>!&nbsp;<wbr>id3v2mux&nbsp;<wbr>!&nbsp;<wbr>filesink location=track5.mp3</code><br />
 rips track 5 from the CD and converts it into a single mp3 file </p>
<p> Using <code><a href="/docs/linux/man/1-gst-inspect/">gst-inspect</a></code>(1), it is possible to discover settings like the above for cdparanoiasrc that will tell it to rip the entire cd or only tracks of it. Alternatively, you can use an URI and gst-launch-0.10 will find an element (such as cdparanoia) that supports that protocol for you, e.g.: <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch&nbsp;<wbr><a href="cdda://5">cdda://5</a>&nbsp;<wbr>!&nbsp;<wbr>lame vbr=new vbr-quality=6&nbsp;<wbr>!&nbsp;<wbr>filesink location=track5.mp3</code> </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch osssrc&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>vorbisenc&nbsp;<wbr>!&nbsp;<wbr>oggmux&nbsp;<wbr>!&nbsp;<wbr>filesink location=input.ogg</code><br />
 records sound from your audio input and encodes it into an ogg file </p>
<p> <code>Video</code> </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=JB_FF9_TheGravityOfLove.mpg&nbsp;<wbr>!&nbsp;<wbr>dvddemux&nbsp;<wbr>!&nbsp;<wbr>mpeg2dec&nbsp;<wbr>!&nbsp;<wbr>xvimagesink</code><br />
 Display only the video portion of an MPEG-1 video file, outputting to an X display window </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=/flflfj.vob&nbsp;<wbr>!&nbsp;<wbr>dvddemux&nbsp;<wbr>!&nbsp;<wbr>mpeg2dec&nbsp;<wbr>!&nbsp;<wbr>sdlvideosink</code><br />
 Display the video portion of a .vob file (used on DVDs), outputting to an SDL window </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=movie.mpg&nbsp;<wbr>!&nbsp;<wbr>dvddemux name=demuxer&nbsp;<wbr>&nbsp;<wbr>demuxer.&nbsp;<wbr>!&nbsp;<wbr>queue&nbsp;<wbr>!&nbsp;<wbr>mpeg2dec&nbsp;<wbr>!&nbsp;<wbr>sdlvideosink&nbsp;<wbr>&nbsp;<wbr>demuxer.&nbsp;<wbr>!&nbsp;<wbr>queue&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Play both video and audio portions of an MPEG movie </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=movie.mpg&nbsp;<wbr>!&nbsp;<wbr>mpegdemux name=demuxer&nbsp;<wbr>&nbsp;<wbr>demuxer.&nbsp;<wbr>!&nbsp;<wbr>queue&nbsp;<wbr>!&nbsp;<wbr>mpeg2dec&nbsp;<wbr>!&nbsp;<wbr>ffmpegcolorspace&nbsp;<wbr>!&nbsp;<wbr>sdlvideosink&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>demuxer.&nbsp;<wbr>!&nbsp;<wbr>queue&nbsp;<wbr>!&nbsp;<wbr>mad&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Play an AVI movie with an external text subtitle stream </p>
<p> This example also shows how to refer to specific pads by name if an element (here: textoverlay) has multiple sink or source pads. </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch textoverlay name=overlay&nbsp;<wbr>!&nbsp;<wbr>ffmpegcolorspace&nbsp;<wbr>!&nbsp;<wbr>videoscale&nbsp;<wbr>!&nbsp;<wbr>autovideosink&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filesrc location=movie.avi&nbsp;<wbr>!&nbsp;<wbr>decodebin2&nbsp;<wbr>!&nbsp;<wbr>ffmpegcolorspace&nbsp;<wbr>!&nbsp;<wbr>overlay.video_sink&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filesrc location=movie.srt&nbsp;<wbr>!&nbsp;<wbr>subparse&nbsp;<wbr>!&nbsp;<wbr>overlay.text_sink</code> </p>
<p> Play an AVI movie with an external text subtitle stream using playbin2 </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch playbin2 uri=file:///path/to/movie.avi suburi=file:///path/to/movie.srt</code> </p>
<p> <code>Network streaming</code> </p>
<p> Stream video using RTP and network elements. </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch v4l2src&nbsp;<wbr>!&nbsp;<wbr>video/x-raw-yuv,width=128,height=96,format='(fourcc)&#8217;UYVY&nbsp;<wbr>!&nbsp;<wbr>ffmpegcolorspace&nbsp;<wbr>!&nbsp;<wbr>ffenc_h263&nbsp;<wbr>!&nbsp;<wbr>video/x-h263&nbsp;<wbr>!&nbsp;<wbr>rtph263ppay pt=96&nbsp;<wbr>!&nbsp;<wbr>udpsink host=192.168.1.1 port=5000 sync=false</code><br />
 This command would be run on the transmitter </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch udpsrc port=5000&nbsp;<wbr>!&nbsp;<wbr>application/x-rtp, clock-rate=90000,payload=96&nbsp;<wbr>!&nbsp;<wbr>rtph263pdepay queue-delay=0&nbsp;<wbr>!&nbsp;<wbr>ffdec_h263&nbsp;<wbr>!&nbsp;<wbr>xvimagesink</code><br />
 Use this command on the receiver </p>
<p> <code>Diagnostic</code> </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch -v fakesrc num-buffers=16&nbsp;<wbr>!&nbsp;<wbr>fakesink</code><br />
 Generate a null stream and ignore it (and print out details). </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch audiotestsrc&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Generate a pure sine tone to test the audio output </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch videotestsrc&nbsp;<wbr>!&nbsp;<wbr>xvimagesink</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch videotestsrc&nbsp;<wbr>!&nbsp;<wbr>ximagesink</code><br />
 Generate a familiar test pattern to test the video output </p>
<p> <code>Automatic linking</code> </p>
<p> You can use the decodebin element to automatically select the right elements to get a working pipeline. </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=musicfile&nbsp;<wbr>!&nbsp;<wbr>decodebin&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink</code><br />
 Play any supported audio format </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch filesrc location=videofile&nbsp;<wbr>!&nbsp;<wbr>decodebin name=decoder&nbsp;<wbr>&nbsp;<wbr>decoder.&nbsp;<wbr>!&nbsp;<wbr>queue&nbsp;<wbr>!&nbsp;<wbr>audioconvert&nbsp;<wbr>!&nbsp;<wbr>audioresample&nbsp;<wbr>!&nbsp;<wbr>osssink&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>decoder.&nbsp;<wbr>!&nbsp;<wbr>ffmpegcolorspace&nbsp;<wbr>!&nbsp;<wbr>xvimagesink</code><br />
 Play any supported video format with video and audio output. Threads are used automatically. To make this even easier, you can use the playbin element: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch playbin uri=file:///home/joe/foo.avi</code> </p>
<p> <code>Filtered connections</code> </p>
<p> These examples show you how to use filtered caps. </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch videotestsrc&nbsp;<wbr>!&nbsp;<wbr>&#8216;video/x-raw-yuv,format=(fourcc)YUY2;video/x-raw-yuv,format=(fourcc)YV12&#8217;&nbsp;<wbr>!&nbsp;<wbr>xvimagesink</code><br />
 Show a test image and use the YUY2 or YV12 video format for this. </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gst-launch osssrc&nbsp;<wbr>!&nbsp;<wbr>&#8216;audio/x-raw-int,rate=[32000,64000],width=[16,32],depth={16,24,32},signed=(boolean)true&#8217;&nbsp;<wbr>!&nbsp;<wbr>wavenc&nbsp;<wbr>!&nbsp;<wbr>filesink location=recording.wav</code><br />
 record audio and write it to a .wav file. Force usage of signed 16 to 32 bit samples and a sample rate between 32kHz and 64KHz. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>GST_DEBUG</code></p>
<dd> Comma-separated list of debug categories and levels, e.g. GST_DEBUG=totem:4,typefind:5</p>
<dt><code>GST_DEBUG_NO_COLOR</code></p>
<dd> When this environment variable is set, coloured debug output is disabled.</p>
<dt><code>GST_DEBUG_DUMP_DOT_DIR</code></p>
<dd> When set to a filesystem path, store dot files of pipeline graphs there.</p>
<dt><code>GST_REGISTRY</code></p>
<dd> Path of the plugin registry file. Default is ~/.gstreamer-0.10/registry-CPU.xml where CPU is the machine/cpu type GStreamer was compiled for, e.g. &#8216;i486&#8217;, &#8216;i686&#8217;, &#8216;x86-64&#8217;, &#8216;ppc&#8217;, etc. (check the output of &quot;uname -i&quot; and &quot;uname -m&quot; for details).</p>
<dt><code>GST_REGISTRY_UPDATE</code></p>
<dd> Set to &quot;no&quot; to force GStreamer to assume that no plugins have changed, been added or been removed. This will make GStreamer skip the initial check whether a rebuild of the registry cache is required or not. This may be useful in embedded environments where the installed plugins never change. Do not use this option in any other setup.</p>
<dt><code>GST_PLUGIN_PATH</code></p>
<dd> Specifies a list of directories to scan for additional plugins. These take precedence over the system plugins.</p>
<dt><code>GST_PLUGIN_SYSTEM_PATH</code></p>
<dd> Specifies a list of plugins that are always loaded by default. If not set, this defaults to the system-installed path, and the plugins installed in the user&#8217;s home directory</p>
<dt><code>ORC_CODE</code></p>
<dd> Useful Orc environment variable. Set ORC_CODE=debug to enable debuggers such as gdb to create useful backtraces from Orc-generated code. Set ORC_CODE=backup or ORC_CODE=emulate if you suspect Orc&#8217;s SIMD code generator is producing incorrect code. (Quite a few important GStreamer plugins like videotestsrc, audioconvert or audioresample use Orc).</p>
<dt><code>G_DEBUG</code></p>
<dd> Useful GLib environment variable. Set G_DEBUG=fatal_warnings to make GStreamer programs abort when a critical warning such as an assertion failure occurs. This is useful if you want to find out which part of the code caused that warning to be triggered and under what circumstances. Simply set G_DEBUG as mentioned above and run the program in gdb (or let it core dump). Then get a stack trace in the usual way.</dl>
<h2>FILES</h2>
<dl>
<dt>~/.gstreamer-0.10/registry-*.xml</p>
<dd> The xml plugin database; can be deleted at any time, will be re-created automatically when it does not exist yet or plugins change.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gst-feedback/">gst-feedback</a></code>(1), <code><a href="/docs/linux/man/1-gst-inspect/">gst-inspect</a></code>(1), <code><a href="/docs/linux/man/1-gst-typefind/">gst-typefind</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a> </p>
<h2>Index</h2>
