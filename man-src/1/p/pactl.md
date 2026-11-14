---
title: "pactl(1)"
name: "pactl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pactl/"
description: "pactl – Control a running PulseAudio sound server"
---

<h2 class="name">NAME</h2>
<p> pactl &#8211; Control a running PulseAudio sound server </p>
<h2>SYNOPSIS</h2>
<p> <code>pactl [</code><i>options</i><code>] </code><i>COMMAND</i><code> [</code><i>ARGS &#8230;</i><code>] </p>
<p> pactl &#8211;help </p>
<p> pactl &#8211;version </code></p>
<h2>DESCRIPTION</h2>
<p> <i>pactl</i> can be used to issue control commands to the PulseAudio sound server. </p>
<p> <i>pactl</i> only exposes a subset of the available operations. For the full set use the <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-s | &#8211;server</code><i>=SERVER</i></p>
<dd> Choose the server to connect to.</p>
<dt><code>-f | &#8211;format</code><i>=FORMAT</i></p>
<dd> Choose output format, available options are &quot;text&quot; or &quot;json&quot;.</p>
<dt><code>-n | &#8211;client-name</code><i>=NAME</i></p>
<dd> Specify the client name <i>pactl</i> shall pass to the server when connecting.</dl>
<h2>COMMANDS</h2>
<p> When supplied as arguments to the commands below, the special names @DEFAULT_SINK@, @DEFAULT_SOURCE@ and @DEFAULT_MONITOR@ can be used to specify the default sink, source and monitor respectively.</p>
<dl>
<dt><code>stat</code></p>
<dd> Dump a few statistics about the memory usage of the PulseAudio daemon.</p>
<dt><code>info</code></p>
<dd> Dump some info about the PulseAudio daemon.</p>
<dt><code>list</code> [<i>short</i>] [<i>TYPE</i>]</p>
<dd> Dump all currently loaded modules, available sinks, sources, streams, etc. <i>TYPE</i> must be one of: modules, sinks, sources, sink-inputs, source-outputs, clients, samples, cards, message-handlers. If not specified, all info is listed with the exception of the message-handlers. If short is given, output is in a tabular format, for easy parsing by scripts.</p>
<dt><code>exit</code></p>
<dd> Asks the PulseAudio server to terminate.</p>
<dt><code>upload-sample</code> <i>FILENAME</i> [<i>NAME</i>]</p>
<dd> Upload a sound from the specified audio file into the sample cache. The file types supported are those understood by <i>libsndfile</i>. The sample in the cache is named after the audio file, unless the name is explicitly specified.</p>
<dt><code>play-sample</code> <i>NAME</i> [<i>SINK</i>]</p>
<dd> Play the specified sample from the sample cache. It is played on the default sink, unless the symbolic name or the numerical index of the sink to play it on is specified.</p>
<dt><code>remove-sample</code> <i>NAME</i></p>
<dd> Remove the specified sample from the sample cache.</p>
<dt><code>load-module</code> <i>NAME</i> [<i>ARGUMENTS &#8230;</i>]</p>
<dd> Load the specified module with the specified arguments into the running sound server. Prints the numeric index of the module just loaded to STDOUT. You can use it to unload the module later.</p>
<dt><code>unload-module</code> <i>ID|NAME</i></p>
<dd> Unload the module instance identified by the specified numeric index or unload all modules by the specified name.</p>
<dt><code>move-sink-input</code> <i>ID</i> <i>SINK</i></p>
<dd> Move the specified playback stream (identified by its numerical index) to the specified sink (identified by its symbolic name or numerical index).</p>
<dt><code>move-source-output</code> <i>ID</i> <i>SOURCE</i></p>
<dd> Move the specified recording stream (identified by its numerical index) to the specified source (identified by its symbolic name or numerical index).</p>
<dt><code>suspend-sink</code> <i>SINK</i> <i>true|false</i></p>
<dd> Suspend or resume the specified sink (which may be specified either by its symbolic name or numerical index), depending whether true (suspend) or false (resume) is passed as last argument. Suspending a sink will pause all playback. Depending on the module implementing the sink this might have the effect that the underlying device is closed, making it available for other applications to use. The exact behaviour depends on the module.</p>
<dt><code>suspend-source</code> <i>SOURCE</i> <i>true|false</i></p>
<dd> Suspend or resume the specified source (which may be specified either by its symbolic name or numerical index), depending whether true (suspend) or false (resume) is passed as last argument. Suspending a source will pause all capturing. Depending on the module implementing the source this might have the effect that the underlying device is closed, making it available for other applications to use. The exact behaviour depends on the module.</p>
<dt><code>set-card-profile</code> <i>CARD</i> <i>PROFILE</i></p>
<dd> Set the specified card (identified by its symbolic name or numerical index) to the specified profile (identified by its symbolic name).</p>
<dt><code>get-default-sink</code></p>
<dd> Returns the symbolic name of the default sink.</p>
<dt><code>set-default-sink</code> <i>SINK</i></p>
<dd> Make the specified sink (identified by its symbolic name or numerical index) the default sink.</p>
<dt><code>set-sink-port</code> <i>SINK</i> <i>PORT</i></p>
<dd> Set the specified sink (identified by its symbolic name or numerical index) to the specified port (identified by its symbolic name).</p>
<dt><code>get-default-source</code></p>
<dd> Returns the symbolic name of the default source.</p>
<dt><code>set-default-source</code> <i>SOURCE</i></p>
<dd> Make the specified source (identified by its symbolic name or numerical index) the default source.</p>
<dt><code>set-source-port</code> <i>SOURCE</i> <i>PORT</i></p>
<dd> Set the specified source (identified by its symbolic name or numerical index) to the specified port (identified by its symbolic name).</p>
<dt><code>set-port-latency-offset</code> <i>CARD</i> <i>PORT</i> <i>OFFSET</i></p>
<dd> Set a latency offset to a specified port (identified by its symbolic name) that belongs to a card (identified by its symbolic name or numerical index). <i>OFFSET</i> is a number which represents the latency offset in microseconds</p>
<dt><code>get-sink-volume</code> <i>SINK</i></p>
<dd> Get the volume of the specified sink (identified by its symbolic name or numerical index) displayed in the same format as the `info` command.</p>
<dt><code>set-sink-volume</code> <i>SINK</i> <i>VOLUME [VOLUME &#8230;]</i></p>
<dd> Set the volume of the specified sink (identified by its symbolic name or numerical index). <i>VOLUME</i> can be specified as an integer (e.g. 2000, 16384), a linear factor (e.g. 0.4, 1.100), a percentage (e.g. 10%, 100%) or a decibel value (e.g. 0dB, 20dB). If the volume specification start with a + or &#8211; the volume adjustment will be relative to the current sink volume. A single volume value affects all channels; if multiple volume values are given their number has to match the sink&#8217;s number of channels.</p>
<dt><code>get-source-volume</code> <i>SOURCE</i></p>
<dd> &#8220;` Get the volume of the specified source (identified by its symbolic name or numerical index) displayed in the same format as the `info` command.</p>
<dt><code>set-source-volume</code> <i>SOURCE</i> <i>VOLUME [VOLUME &#8230;]</i></p>
<dd> Set the volume of the specified source (identified by its symbolic name or numerical index). <i>VOLUME</i> can be specified as an integer (e.g. 2000, 16384), a linear factor (e.g. 0.4, 1.100), a percentage (e.g. 10%, 100%) or a decibel value (e.g. 0dB, 20dB). If the volume specification start with a + or &#8211; the volume adjustment will be relative to the current source volume. A single volume value affects all channels; if multiple volume values are given their number has to match the source&#8217;s number of channels.</p>
<dt><code>set-sink-input-volume</code> <i>INPUT</i> <i>VOLUME [VOLUME &#8230;]</i></p>
<dd> Set the volume of the specified sink input (identified by its numerical index). <i>VOLUME</i> can be specified as an integer (e.g. 2000, 16384), a linear factor (e.g. 0.4, 1.100), a percentage (e.g. 10%, 100%) or a decibel value (e.g. 0dB, 20dB). If the volume specification start with a + or &#8211; the volume adjustment will be relative to the current sink input volume. A single volume value affects all channels; if multiple volume values are given their number has to match the sink input&#8217;s number of channels.</p>
<dt><code>set-source-output-volume</code> <i>OUTPUT</i> <i>VOLUME [VOLUME &#8230;]</i></p>
<dd> Set the volume of the specified source output (identified by its numerical index). <i>VOLUME</i> can be specified as an integer (e.g. 2000, 16384), a linear factor (e.g. 0.4, 1.100), a percentage (e.g. 10%, 100%) or a decibel value (e.g. 0dB, 20dB). If the volume specification start with a + or &#8211; the volume adjustment will be relative to the current source output volume. A single volume value affects all channels; if multiple volume values are given their number has to match the source output&#8217;s number of channels.</p>
<dt><code>get-sink-mute</code> <i>SINK</i></p>
<dd> Get the mute status of the specified sink (identified by its symbolic name or numerical index).</p>
<dt><code>set-sink-mute</code> <i>SINK</i> <i>1|0|toggle</i></p>
<dd> Set the mute status of the specified sink (identified by its symbolic name or numerical index).</p>
<dt><code>get-source-mute</code> <i>SOURCE</i></p>
<dd> Get the mute status of the specified source (identified by its symbolic name or numerical index).</p>
<dt><code>set-source-mute</code> <i>SOURCE</i> <i>1|0|toggle</i></p>
<dd> Set the mute status of the specified source (identified by its symbolic name or numerical index).</p>
<dt><code>set-sink-input-mute</code> <i>INPUT</i> <i>1|0|toggle</i></p>
<dd> Set the mute status of the specified sink input (identified by its numerical index).</p>
<dt><code>set-source-output-mute</code> <i>OUTPUT</i> <i>1|0|toggle</i></p>
<dd> Set the mute status of the specified source output (identified by its numerical index).</p>
<dt><code>set-sink-formats</code> <i>SINK</i> <i>FORMATS</i></p>
<dd> Set the supported formats of the specified sink (identified by its numerical index) if supported by the sink. <i>FORMATS</i> is specified as a semi-colon (;) separated list of formats in the form &#8216;encoding[, key1=value1, key2=value2, &#8230;]&#8217; (for example, AC3 at 32000, 44100 and 48000 Hz would be specified as &#8216;ac3-iec61937, format.rate = &quot;[ 32000, 44100, 48000 ]&quot;&#8217;). See <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SupportedAudioFormats/">https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SupportedAudioFormats/</a> for possible encodings.</p>
<dt><code>send-message</code> <i>RECIPIENT</i> <i>MESSAGE</i> <i>MESSAGE_PARAMETERS</i></p>
<dd> Send a message to the specified recipient object. If applicable an additional string containing message parameters can be specified. A string is returned as a response to the message. For available messages see <a rel="nofollow" href="https://cgit.freedesktop.org/pulseaudio/pulseaudio/tree/doc/messaging_api.txt.">https://cgit.freedesktop.org/pulseaudio/pulseaudio/tree/doc/messaging_api.txt.</a></p>
<dt><code>subscribe</code></p>
<dd> Subscribe to events, pactl does not exit by itself, but keeps waiting for new events.</dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> </p>
<h2>Index</h2>
