---
title: "gst-launch-1-0(1)"
name: "gst-launch-1-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-launch-1-0/"
description: "gst-launch-1.0 – build and run a GStreamer pipeline"
---

<p>gst-launch-1.0 &#8211; build and run a GStreamer pipeline </p>
<h2>Synopsis</h2>
<p><code>gst-launch-1.0</code> <i>[OPTION&#8230;]</i> PIPELINE-DESCRIPTION</p>
<h2>Description</h2>
<p><i>gst-launch-1.0</i> is a tool that builds and runs basic <i>GStreamer</i> pipelines. </p>
<p> In simple form, a PIPELINE-DESCRIPTION is a list of elements separated by exclamation marks (!). Properties may be appended to elements, in the form <i>property=value</i>. A &quot;preset&quot; can also be set using the <i>@preset=&lt;preset name&gt;</i> syntax. </p>
<p> For a complete description of possible PIPELINE-DESCRIPTIONS see the section <i>pipeline description</i> below or consult the GStreamer documentation. </p>
<p> Please note that <i>gst-launch-1.0</i> is primarily a debugging tool for developers and users. You should not build applications on top of it. For applications, use the gst_parse_launch() function of the GStreamer API as an easy way to construct pipelines from pipeline descriptions.</p>
<h2>Options</h2>
<p><i>gst-launch-1.0</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print help synopsis and available FLAGS</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Output status information and property notifications</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Do not print any progress information</p>
<dt><code>-m, &#8211;messages</code></p>
<dd>Output messages posted on the pipeline&#8217;s bus</p>
<dt><code>-t, &#8211;tags</code></p>
<dd>Output tags (also known as metadata)</p>
<dt><code>-e, &#8211;eos-on-shutdown</code></p>
<dd>Force an EOS event on sources before shutting the pipeline down. This is useful to make sure muxers create readable files when a muxing pipeline is shut down forcefully via Control-C.</p>
<dt><code>-i, &#8211;index</code></p>
<dd>Gather and print index statistics. This is mostly useful for playback or recording pipelines.</p>
<dt><code>-f, &#8211;no-fault</code></p>
<dd>Do not install a fault handler</p>
<dt><code>-T, &#8211;trace</code></p>
<dd>Print memory allocation traces. The feature must be enabled at compile time to work.</p>
<dt><code>&#8211;no-position</code></p>
<dd>Do not print current position of pipeline. If this option is unspecified, the position will be printed when stdout is a TTY. To enable printing position when stdout is not a TTY, use &quot;force-position&quot; option.</p>
<dt><code>&#8211;force-position</code></p>
<dd>Allow printing current position of pipeline even if stdout is not a TTY. This option has no effect if the &quot;no-position&quot; option is specified.</p>
<dd></dl>
<h2>Gstreamer Options</h2>
<p><i>gst-launch-1.0</i> also accepts the following options that are common to all GStreamer applications:</p>
<dl>
<dt><code>&#8211;gst-version</code></p>
<dd>Prints the version string of the <i>GStreamer</i> core library.</p>
<dt><code>&#8211;gst-fatal-warnings</code></p>
<dd>Causes <i>GStreamer</i> to abort if a warning message occurs. This is equivalent to setting the environment variable G_DEBUG to &#8216;fatal_warnings&#8217; (see the section <i>environment variables</i> below for further information).</p>
<dt><code>&#8211;gst-debug=STRING</code></p>
<dd>A comma separated list of category_name:level pairs to specify debugging levels for each category. Level is in the range 0-9 where 0 will show no messages, and 9 will show all messages. The wildcard * can be used to match category names. Note that the order of categories and levels is important, wildcards at the end may override levels set earlier. The log levels are: 1=ERROR, 2=WARNING, 3=FIXME, 4=INFO, 5=DEBUG, 6=LOG, 7=TRACE, 9=MEMDUMP. Since GStreamer 1.2 one can also use the debug level names, e.g. &#8211;gst-debug=*sink:LOG. A full description of the various debug levels can be found in the GStreamer core library API documentation, in the &quot;Running GStreamer Applications&quot; section. </p>
<p> Use &#8211;gst-debug-help to show category names </p>
<p> Example: GST_CAT:5,GST_ELEMENT_*:3,oggdemux:5 </p>
<dt><code>&#8211;gst-debug-level=LEVEL</code></p>
<dd>Sets the threshold for printing debugging messages. A higher level will print more messages. The useful range is 0-9, with the default being 0. Level 6 (LOG level) will show all information that is usually required for debugging purposes. Higher levels are only useful in very specific cases. See above for the full list of levels.</p>
<dt><code>&#8211;gst-debug-no-color</code></p>
<dd><i>GStreamer</i> normally prints debugging messages so that the messages are color-coded when printed to a terminal that handles ANSI escape sequences. Using this option causes <i>GStreamer</i> to print messages without color. Setting the <code>GST_DEBUG_NO_COLOR</code> environment variable will achieve the same thing.</p>
<dt><code>&#8211;gst-debug-color-mode</code></p>
<dd><i>GStreamer</i> normally prints debugging messages so that the messages are color-coded when printed to a terminal that handles ANSI escape sequences (on *nix), or uses W32 console API to color the messages printed into a console (on W32). Using this option causes <i>GStreamer</i> to print messages without color (&#8216;off&#8217; or &#8216;disable&#8217;), print messages with default colors (&#8216;on&#8217; or &#8216;auto&#8217;), or print messages using ANSI escape sequences for coloring (&#8216;unix&#8217;). Setting the <code>GST_DEBUG_COLOR_MODE</code> environment variable will achieve the same thing.</p>
<dt><code>&#8211;gst-debug-disable</code></p>
<dd>Disables debugging.</p>
<dt><code>&#8211;gst-debug-help</code></p>
<dd>Prints a list of available debug categories and their default debugging level.</p>
<dt><code>&#8211;gst-plugin-spew</code></p>
<dd><i>GStreamer</i> info flags to set Enable printout of errors while loading <i>GStreamer</i> plugins</p>
<dt><code>&#8211;gst-plugin-path=PATH</code></p>
<dd>Add directories separated with &#8216;:&#8217; to the plugin search path</p>
<dt><code>&#8211;gst-plugin-load=PLUGINS</code></p>
<dd>Preload plugins specified in a comma-separated list. Another way to specify plugins to preload is to use the environment variable GST_PLUGIN_PATH </p>
</dl>
<h2>Pipeline Description</h2>
<p>A pipeline consists <i>elements</i> and <i>links</i>. <i>Elements</i> can be put into <i>bins</i> of different sorts. <i>Elements</i>, <i>links</i> and <i>bins</i> can be specified in a pipeline description in any order. </p>
<p> <code>Elements</code> </p>
<p> ELEMENTTYPE <i>[PROPERTY1 &#8230;]</i> </p>
<p> Creates an element of type ELEMENTTYPE and sets the PROPERTIES. </p>
<p> <code>Properties</code> </p>
<p> PROPERTY=VALUE &#8230; </p>
<p> Sets the property to the specified value. You can use <code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1) to find out about properties and allowed values of different elements.<br />
 Enumeration properties can be set by name, nick or value. </p>
<p> <code>Presets</code> </p>
<p> @preset=&lt;preset name&gt; &#8230; </p>
<p> Sets the preset on the element. you can use <a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a>(1) to find out what presets are available for a specific element. </p>
<p> <code>Bins</code> </p>
<p> <i>[BINTYPE.]</i> ( <i>[PROPERTY1 &#8230;]</i> PIPELINE-DESCRIPTION ) </p>
<p> Specifies that a bin of type BINTYPE is created and the given properties are set. Every element between the braces is put into the bin. Please note the dot that has to be used after the BINTYPE. You will almost never need this functionality, it is only really useful for applications using the gst_launch_parse() API with &#8216;bin&#8217; as bintype. That way it is possible to build partial pipelines instead of a full-fledged top-level pipeline. </p>
<p> <code>Links</code> </p>
<p> <i>[[SRCELEMENT].[PAD1,&#8230;]]</i> ! <i>[[SINKELEMENT].[PAD1,&#8230;]]</i> <i>[[SRCELEMENT].[PAD1,&#8230;]]</i> ! CAPS ! <i>[[SINKELEMENT].[PAD1,&#8230;]]</i> <i>[[SRCELEMENT].[PAD1,&#8230;]]</i> : <i>[[SINKELEMENT].[PAD1,&#8230;]]</i> <i>[[SRCELEMENT].[PAD1,&#8230;]]</i> : CAPS : <i>[[SINKELEMENT].[PAD1,&#8230;]]</i> </p>
<p> Links the element with name SRCELEMENT to the element with name SINKELEMENT, using the caps specified in CAPS as a filter. Names can be set on elements with the name property. If the name is omitted, the element that was specified directly in front of or after the link is used. This works across bins. If a padname is given, the link is done with these pads. If no pad names are given all possibilities are tried and a matching pad is used. If multiple padnames are given, both sides must have the same number of pads specified and multiple links are done in the given order.<br />
 So the simplest link is a simple exclamation mark, that links the element to the left of it to the element right of it.<br />
 Linking using the : operator attempts to link all possible pads between the elements </p>
<p> <code>Caps</code> </p>
<p> MEDIATYPE <i>[, PROPERTY[, PROPERTY &#8230;]]]</i> <i>[; CAPS[; CAPS &#8230;]]</i> </p>
<p> Creates a capability with the given media type and optionally with given properties. The media type can be escaped using &quot; or &#8216;. If you want to chain caps, you can add more caps in the same format afterwards. </p>
<p> <code>Properties</code> </p>
<p> NAME=<i>[(TYPE)]</i>VALUE<br />
 in lists and ranges: <i>[(TYPE)]</i>VALUE </p>
<p> Sets the requested property in capabilities. The name is an alphanumeric value and the type can have the following case-insensitive values:<br />
 &#8211; <code>i</code> or <code>int</code> for integer values or ranges<br />
 &#8211; <code>f</code> or <code>float</code> for float values or ranges<br />
 &#8211; <code>b</code>, <code>bool</code> or <code>boolean</code> for boolean values<br />
 &#8211; <code>s</code>, <code>str</code> or <code>string</code> for strings<br />
 &#8211; <code>fraction</code> for fractions (framerate, pixel-aspect-ratio)<br />
 &#8211; <code>l</code> or <code>list</code> for lists<br />
 If no type was given, the following order is tried: integer, float, boolean, string.<br />
 Integer values must be parsable by <code>strtol()</code>, floats by <code>strtod()</code>. FOURCC values may either be integers or strings. Boolean values are (case insensitive) <i>yes</i>, <i>no</i>, <i>true</i> or <i>false</i> and may like strings be escaped with &quot; or &#8216;.<br />
 Ranges are in this format: [ VALUE, VALUE ]<br />
 Lists use this format: { VALUE <i>[, VALUE &#8230;]</i> } </p>
<h2>Pipeline Examples</h2>
<p>The examples below assume that you have the correct plug-ins available. In general, &quot;pulsesink&quot; can be substituted with another audio output plug-in such as &quot;alsasink&quot; or &quot;osxaudiosink&quot; Likewise, &quot;xvimagesink&quot; can be substituted with &quot;ximagesink&quot;, &quot;glimagesink&quot;, or &quot;osxvideosink&quot;. Keep in mind though that different sinks might accept different formats and even the same sink might accept different formats on different machines, so you might need to add converter elements like audioconvert and audioresample (for audio) or videoconvert (for video) in front of the sink to make things work. </p>
<p> <code>Audio playback</code> </p>
<p> Play the mp3 music file &quot;music.mp3&quot; using a libmpg123-based plug-in and output to an Pulseaudio device<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.mp3&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Play an Ogg Vorbis format file<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.ogg&nbsp;!&nbsp;oggdemux&nbsp;!&nbsp;vorbisdec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Play an mp3 file or an http stream using GIO<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 giosrc location=music.mp3&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;pulsesink</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 giosrc location=<a rel="nofollow" href="http://domain.com/music.mp3">http://domain.com/music.mp3</a>&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Use GIO to play an mp3 file located on an SMB server<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 giosrc location=<a href="smb://computer/music.mp3">smb://computer/music.mp3</a>&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> <code>Format conversion</code> </p>
<p> Convert an mp3 music file to an Ogg Vorbis file<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.mp3&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;vorbisenc&nbsp;!&nbsp;oggmux&nbsp;!&nbsp;filesink location=music.ogg</code> </p>
<p> Convert to the FLAC format<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.mp3&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;flacenc&nbsp;!&nbsp;filesink location=test.flac</code> </p>
<p> <code>Other</code> </p>
<p> Plays a .WAV file that contains raw audio data (PCM).<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.wav&nbsp;!&nbsp;wavparse&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Convert a .WAV file containing raw audio data into an Ogg Vorbis or mp3 file<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.wav&nbsp;!&nbsp;wavparse&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;vorbisenc&nbsp;!&nbsp;oggmux&nbsp;!&nbsp;filesink location=music.ogg</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=music.wav&nbsp;!&nbsp;wavparse&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;lamemp3enc&nbsp;!&nbsp;filesink location=music.mp3</code> </p>
<p> Rips all tracks from compact disc and convert them into a single mp3 file<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 cdparanoiasrc mode=continuous&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;lamemp3enc&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;id3v2mux&nbsp;!&nbsp;filesink location=cd.mp3</code> </p>
<p> Rips track 5 from the CD and converts it into a single mp3 file<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 cdparanoiasrc track=5&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;lamemp3enc&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;id3v2mux&nbsp;!&nbsp;filesink location=track5.mp3</code> </p>
<p> Using <code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), it is possible to discover settings like the above for cdparanoiasrc that will tell it to rip the entire cd or only tracks of it. Alternatively, you can use an URI and gst-launch-1.0 will find an element (such as cdparanoia) that supports that protocol for you, e.g.: <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0&nbsp;<a href="cdda://5">cdda://5</a>&nbsp;!&nbsp;lamemp3enc vbr=new vbr-quality=6&nbsp;!&nbsp;filesink location=track5.mp3</code> </p>
<p> Records sound from your audio input and encodes it into an ogg file<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 pulsesrc&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;vorbisenc&nbsp;!&nbsp;oggmux&nbsp;!&nbsp;filesink location=input.ogg</code> </p>
<p> <code>Video</code> </p>
<p> Display only the video portion of an MPEG-1 video file, outputting to an X display window<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=JB_FF9_TheGravityOfLove.mpg&nbsp;!&nbsp;dvddemux&nbsp;!&nbsp;mpegvideoparse&nbsp;!&nbsp;mpeg2dec&nbsp;!&nbsp;xvimagesink</code> </p>
<p> Display the video portion of a .vob file (used on DVDs), outputting to an SDL window<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=/flflfj.vob&nbsp;!&nbsp;dvddemux&nbsp;!&nbsp;mpegvideoparse&nbsp;!&nbsp;mpeg2dec&nbsp;!&nbsp;sdlvideosink</code> </p>
<p> Play both video and audio portions of an MPEG movie<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=movie.mpg&nbsp;!&nbsp;dvddemux name=demuxer&nbsp;<wbr>&nbsp;demuxer.&nbsp;!&nbsp;queue&nbsp;!&nbsp;mpegvideoparse&nbsp;!&nbsp;mpeg2dec&nbsp;!&nbsp;sdlvideosink&nbsp;<wbr>&nbsp;demuxer.&nbsp;!&nbsp;queue&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Play an AVI movie with an external text subtitle stream<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=movie.mpg&nbsp;!&nbsp;mpegdemux name=demuxer demuxer.&nbsp;!&nbsp;queue&nbsp;!&nbsp;mpegvideoparse&nbsp;!&nbsp;mpeg2dec&nbsp;!&nbsp;videoconvert&nbsp;!&nbsp;sdlvideosink&nbsp;<wbr>&nbsp;<wbr>&nbsp;demuxer.&nbsp;!&nbsp;queue&nbsp;!&nbsp;mpegaudioparse&nbsp;!&nbsp;mpg123audiodec&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> This example also shows how to refer to specific pads by name if an element (here: textoverlay) has multiple sink or source pads.<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 textoverlay name=overlay&nbsp;!&nbsp;videoconvert&nbsp;!&nbsp;videoscale&nbsp;!&nbsp;<wbr>&nbsp;autovideosink&nbsp;<wbr>&nbsp;<wbr>&nbsp;filesrc location=movie.avi&nbsp;!&nbsp;decodebin&nbsp;!&nbsp;videoconvert&nbsp;!&nbsp;overlay.video_sink&nbsp;<wbr>&nbsp;<wbr>&nbsp;filesrc location=movie.srt&nbsp;!&nbsp;subparse&nbsp;!&nbsp;overlay.text_sink</code> </p>
<p> Play an AVI movie with an external text subtitle stream using playbin<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 playbin uri=file:///path/to/movie.avi suburi=file:///path/to/movie.srt</code> </p>
<p> <code>Network streaming</code> </p>
<p> Stream video using RTP and network elements. </p>
<p> This command would be run on the transmitter<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 v4l2src&nbsp;!&nbsp;video/x-raw,width=128,height=96,format=UYVY&nbsp;!&nbsp;videoconvert&nbsp;!&nbsp;ffenc_h263&nbsp;!&nbsp;video/x-h263&nbsp;!&nbsp;rtph263ppay pt=96&nbsp;!&nbsp;udpsink host=192.168.1.1 port=5000</code> </p>
<p> Use this command on the receiver<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 udpsrc port=5000&nbsp;!&nbsp;application/x-rtp, clock-rate=90000,payload=96&nbsp;!&nbsp;rtph263pdepay queue-delay=0&nbsp;!&nbsp;ffdec_h263&nbsp;!&nbsp;xvimagesink</code> </p>
<p> <code>Diagnostic</code> </p>
<p> Generate a null stream and ignore it (and print out details).<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 -v fakesrc num-buffers=16&nbsp;!&nbsp;fakesink</code> </p>
<p> Generate a pure sine tone to test the audio output<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 audiotestsrc&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Generate a familiar test pattern to test the video output<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 videotestsrc&nbsp;!&nbsp;xvimagesink</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 videotestsrc&nbsp;!&nbsp;ximagesink</code> </p>
<p> <code>Automatic linking</code> </p>
<p> You can use the decodebin element to automatically select the right elements to get a working pipeline. </p>
<p> Play any supported audio format<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=musicfile&nbsp;!&nbsp;decodebin&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink</code> </p>
<p> Play any supported video format with video and audio output. Threads are used automatically. To make this even easier, you can use the playbin element:<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 filesrc location=videofile&nbsp;!&nbsp;decodebin name=decoder decoder.&nbsp;!&nbsp;queue&nbsp;!&nbsp;audioconvert&nbsp;!&nbsp;audioresample&nbsp;!&nbsp;pulsesink&nbsp;<wbr>&nbsp;<wbr>&nbsp;decoder.&nbsp;!&nbsp;<wbr>&nbsp;videoconvert&nbsp;!&nbsp;xvimagesink</code><br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 playbin uri=file:///home/joe/foo.avi</code> </p>
<p> <code>Filtered connections</code> </p>
<p> These examples show you how to use filtered caps. </p>
<p> Show a test image and use the YUY2 or YV12 video format for this.<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 videotestsrc&nbsp;!&nbsp;&#8216;video/x-raw,format=YUY2;video/x-raw,format=YV12&#8217;&nbsp;!&nbsp;xvimagesink</code> </p>
<p> Record audio and write it to a .wav file. Force usage of signed 16 to 32 bit samples and a sample rate between 32kHz and 64KHz.<br />
 <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gst-launch-1.0 pulsesrc&nbsp;!&nbsp;<wbr>&nbsp;&#8216;audio/x-raw,rate=[32000,64000],format={S16LE,S24LE,S32LE}&#8217;&nbsp;!&nbsp;wavenc&nbsp;!&nbsp;filesink location=recording.wav</code> </p>
<h2>Environment Variables</h2>
<dl>
<dt><code>GST_DEBUG</code></p>
<dd>Comma-separated list of debug categories and levels (e.g. GST_DEBUG=totem:4,typefind:5). &#8216;*&#8217; is allowed as a wildcard as part of debug category names (e.g. GST_DEBUG=*sink:6,*audio*:6). Since 1.2.0 it is also possible to specify the log level by name (1=ERROR, 2=WARN, 3=FIXME, 4=INFO, 5=DEBUG, 6=LOG, 7=TRACE, 9=MEMDUMP) (e.g. GST_DEBUG=*audio*:LOG)</p>
<dt><code>GST_DEBUG_NO_COLOR</code></p>
<dd>When this environment variable is set, coloured debug output is disabled.</p>
<dt><code>GST_DEBUG_DUMP_DOT_DIR</code></p>
<dd>When set to a filesystem path, store &#8216;dot&#8217; files of pipeline graphs there. These can then later be converted into an image using the &#8216;dot&#8217; utility from the graphviz set of tools, like this: dot foo.dot -Tsvg -o foo.svg (png or jpg are also possible as output format). There is also a utility called &#8216;xdot&#8217; which allows you to view the .dot file directly without converting it first.<br />
 When the pipeline changes state through NULL to PLAYING and back to NULL, a dot file is generated on each state change. To write a snapshot of the pipeline state, send a SIGHUP to the process.</p>
<dt><code>GST_REGISTRY</code></p>
<dd>Path of the plugin registry file. Default is ~/.cache/gstreamer-1.0/registry-CPU.bin where CPU is the machine/cpu type GStreamer was compiled for, e.g. &#8216;i486&#8217;, &#8216;i686&#8217;, &#8216;x86-64&#8217;, &#8216;ppc&#8217;, etc. (check the output of &quot;uname -i&quot; and &quot;uname -m&quot; for details).</p>
<dt><code>GST_REGISTRY_UPDATE</code></p>
<dd>Set to &quot;no&quot; to force GStreamer to assume that no plugins have changed, been added or been removed. This will make GStreamer skip the initial check whether a rebuild of the registry cache is required or not. This may be useful in embedded environments where the installed plugins never change. Do not use this option in any other setup.</p>
<dt><code>GST_PLUGIN_PATH</code></p>
<dd>Specifies a list of directories to scan for additional plugins. These take precedence over the system plugins.</p>
<dt><code>GST_PLUGIN_SYSTEM_PATH</code></p>
<dd>Specifies a list of plugins that are always loaded by default. If not set, this defaults to the system-installed path, and the plugins installed in the user&#8217;s home directory</p>
<dt><code>GST_DEBUG_FILE</code></p>
<dd>Set this variable to a file path to redirect all GStreamer debug messages to this file. If left unset, debug messages with be output unto the standard error.</p>
<dt><code>ORC_CODE</code></p>
<dd>Useful Orc environment variable. Set ORC_CODE=debug to enable debuggers such as gdb to create useful backtraces from Orc-generated code. Set ORC_CODE=backup or ORC_CODE=emulate if you suspect Orc&#8217;s SIMD code generator is producing incorrect code. (Quite a few important GStreamer plugins like videotestsrc, audioconvert or audioresample use Orc).</p>
<dt><code>G_DEBUG</code></p>
<dd>Useful GLib environment variable. Set G_DEBUG=fatal_warnings to make GStreamer programs abort when a critical warning such as an assertion failure occurs. This is useful if you want to find out which part of the code caused that warning to be triggered and under what circumstances. Simply set G_DEBUG as mentioned above and run the program in gdb (or let it core dump). Then get a stack trace in the usual way.</dl>
<h2>Files</h2>
<dl>
<dt>~/.cache/gstreamer-1.0/registry-*.bin</p>
<dd>The plugin cache; can be deleted at any time, will be re-created automatically when it does not exist yet or plugins change. Based on XDG_CACHE_DIR, so may be in a different location than the one suggested.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1),</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
