---
title: "pw-cat(1)"
name: "pw-cat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-cat/"
description: "pw-cat – Play and record media with PipeWire"
---

<h2 class="name">NAME</h2>
<p> pw-cat &#8211; Play and record media with PipeWire </p>
<h2>SYNOPSIS</h2>
<pre><code>
pw - cat[options][FILE] pw - play[options][FILE] pw - record[options][FILE] pw - midiplay[options][FILE] pw - midirecord[options][FILE]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pw-cat</code> is a simple tool for playing back or capturing raw or encoded media files on a PipeWire server. It understands all audio file formats supported by <code>libsndfile</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Verbose operation.</p>
<dt><code>-R | &#8211;remote=NAME</code></p>
<dd> The name the <i>remote</i> instance to connect to. If left unspecified, a connection is made to the default PipeWire instance.</p>
<dt><code>-p | &#8211;playback</code></p>
<dd> Playback mode. Read data from the specified file, and play it back. If the tool is called under the name <code>pw-play</code> or <code>pw-midiplay</code> this is the default.</p>
<dt><code>-r | &#8211;record</code></p>
<dd> Recording mode. Capture data and write it to the specified file. If the tool is called under the name <code>pw-record</code> or <code>pw-midirecord</code> this is the default.</p>
<dt><code>-m | &#8211;midi</code></p>
<dd> MIDI mode. <i>FILE</i> is a MIDI file. If the tool is called under the name <code>pw-midiplay</code> or <code>pw-midirecord</code> this is the default.</p>
<dt><code>&#8211;media-type=</code><i>VALUE</i></p>
<dd> Set the media type property (default Audio/Midi depending on mode). The media type is used by the session manager to select a suitable target to link to.</p>
<dt><code>&#8211;media-category=</code><i>VALUE</i></p>
<dd> Set the media category property (default Playback/Capture depending on mode). The media type is used by the session manager to select a suitable target to link to.</p>
<dt><code>&#8211;media-role=</code><i>VALUE</i></p>
<dd> Set the media role property (default Music). The media type is used by the session manager to select a suitable target to link to.</p>
<dt><code>&#8211;target=</code><i>VALUE</i></p>
<dd> Set a node target (default auto). The value can be:</p>
<dt><code>auto</code></p>
<dd> Automatically select (Default)</p>
<dt><code>0</code></p>
<dd> Don&#8217;t try to link this node</p>
<dt><code>&lt;id&gt;</code></p>
<dd> The id of a target node</p>
<dt><code>&#8211;latency=VALUE[</code><i>units</i>]</p>
<dd> Set the node latency (default 100ms) </p>
<p> The latency determines the minimum amount of time it takes for a sample to travel from application to device (playback) and from device to application (capture). </p>
<p> The latency determines the size of the buffers that the application will be able to fill. Lower latency means smaller buffers but higher overhead. Higher latency means larger buffers and lower overhead. </p>
<p> Units can be <code>s</code> for seconds, <code>ms</code> for milliseconds, <code>us</code> for microseconds, <code>ns</code> for nanoseconds. If no units are given, the latency value is samples with the samplerate of the file.</p>
<dt><code>&#8211;list-targets</code></p>
<dd> List the available targets for <code>&#8211;target</code></p>
<dt><code>-q | &#8211;quality=VALUE</code></p>
<dd> Resampler quality. When the samplerate of the source or destination file does not match the samplerate of the server, the data will be resampled. Higher quality uses more CPU. Values between 0 and 15 are allowed, the default quality is 4.</p>
<dt><code>&#8211;rate=</code><i>VALUE</i></p>
<dd> The sample rate, default 48000.</p>
<dt><code>&#8211;channels=</code><i>VALUE</i></p>
<dd> The number of channels, default 2.</p>
<dt><code>&#8211;channel-map=</code><i>VALUE</i></p>
<dd> The channelmap. Possible values include: <code>mono</code>, <code>stereo</code>, <code>surround-21</code>, <code>quad</code>, <code>surround-22</code>, <code>surround-40</code>, <code>surround-31</code>, <code>surround-41</code>, <code>surround-50</code>, <code>surround-51</code>, <code>surround-51r</code>, <code>surround-70</code>, <code>surround-71</code> or a comma separated list of channel names: <code>FL</code>, <code>FR</code>, <code>FC</code>, <code>LFE</code>, <code>SL</code>, <code>SR</code>, <code>FLC</code>, <code>FRC</code>, <code>RC</code>, <code>RL</code>, <code>RR</code>, <code>TC</code>, <code>TFL</code>, <code>TFC</code>, <code>TFR</code>, <code>TRL</code>, <code>TRC</code>, <code>TRR</code>, <code>RLC</code>, <code>RRC</code>, <code>FLW</code>, <code>FRW</code>, <code>LFE2</code>, <code>FLH</code>, <code>FCH</code>, <code>FRH</code>, <code>TFLC</code>, <code>TFRC</code>, <code>TSL</code>, <code>TSR</code>, <code>LLFR</code>, <code>RLFE</code>, <code>BC</code>, <code>BLC</code>, <code>BRC</code></p>
<dt><code>&#8211;format=</code><i>VALUE</i></p>
<dd> The sample format to use. One of: <code>s8</code>, <code>s16</code> (default), <code>s24</code>, <code>s32</code>, <code>f32</code>, <code>f64</code>.</p>
<dt><code>&#8211;volume=</code><i>VALUE</i></p>
<dd> The stream volume, default 1.000.</dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">PipeWire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-mon/">pw-mon</a>(1)</code>, </p>
<h2>Index</h2>
