---

title: "parecord(1)"
name: "parecord"
section: "1"
letter: "p"
url: "/docs/linux/man/1-parecord/"
description: "pacat – Play back or record raw or encoded audio streams on a PulseAudio sound server"
---

<p> <code>paplay [</code><i>options</i><code>] [</code><i>FILE</i><code>] </p>
<p> parecord [</code><i>options</i><code>] [</code><i>FILE</i><code>] </p>
<p> pacat [</code><i>options</i><code>] [</code><i>FILE</i><code>] </p>
<p> parec [</code><i>options</i><code>] [</code><i>FILE</i><code>] </p>
<p> pamon [</code><i>options</i><code>] [</code><i>FILE</i><code>] </p>
<p> pacat &#8211;help </p>
<p> pacat &#8211;version </code></p>
<p> <i>pacat</i> is a simple tool for playing back or capturing raw or encoded audio files on a PulseAudio sound server. It understands all audio file formats supported by <i>libsndfile</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version information.</dd>
<dt><code>-r | &#8211;record</code></dt>
<dd> Capture audio data and write it to the specified file or to STDOUT if none is specified. If the tool is called under the name <i>parec</i> this is the default.</dd>
<dt><code>-p | &#8211;playback</code></dt>
<dd> Read audio data from the specified file or STDIN if none is specified, and play it back. If the tool is called under the name <i>pacat</i> this is the default.</dd>
<dt><code>-v | &#8211;verbose</code></dt>
<dd> Enable verbose operation. Dumps the current playback time to STDERR during playback/capturing.</dd>
<dt><code>-s | &#8211;server</code><i>=SERVER</i></dt>
<dd> Choose the server to connect to.</dd>
<dt><code>-d | &#8211;device</code><i>=SINKORSOURCE</i></dt>
<dd> Specify the symbolic name of the sink/source to play/record this stream on/from. The special names , and can be used to specify the default sink, source and monitor respectively.</dd>
<dt><code>&#8211;monitor-stream</code><i>=INDEX</i></dt>
<dd> Record from the sink input with index INDEX.</dd>
<dt><code>-n | &#8211;client-name</code><i>=NAME</i></dt>
<dd> Specify the client name <i>paplay</i> shall pass to the server when connecting.</dd>
<dt><code>&#8211;stream-name</code><i>=NAME</i></dt>
<dd> Specify the stream name <i>paplay</i> shall pass to the server when creating the stream.</dd>
<dt><code>&#8211;volume</code><i>=VOLUME</i></dt>
<dd> Specify the initial playback volume to use. Choose a value between 0 (silent) and 65536 (100% volume).</dd>
<dt><code>&#8211;rate</code><i>=SAMPLERATE</i></dt>
<dd> Capture or play back audio with the specified sample rate. Defaults to 44100 Hz.</dd>
<dt><code>&#8211;format</code><i>=FORMAT</i></dt>
<dd> Capture or play back audio with the specified sample format. See <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SupportedAudioFormats/">https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SupportedAudioFormats/</a> for supported values. Defaults to s16ne.</dd>
<dt><code>&#8211;channels</code><i>=CHANNELS</i></dt>
<dd> Capture or play back audio with the specified number of channels. If more than two channels are used it is recommended to use the <code>&#8211;channel-map</code> option below. Defaults to 2.</dd>
<dt><code>&#8211;channel-map</code><i>=CHANNELMAP</i></dt>
<dd> Explicitly choose a channel map when playing back this stream. The argument should be a comma separated list of channel names: <code>front-left</code>, <code>front-right</code>, <code>mono</code>, <code>front-center</code>, <code>rear-left</code>, <code>rear-right</code>, <code>rear-center</code>, <code>lfe</code>, <code>front-left-of-center</code>, <code>front-right-of-center</code>, <code>side-left</code>, <code>side-right</code>, <code>top-center</code>, <code>top-front-center</code>, <code>top-front-left</code>, <code>top-front-right</code>, <code>top-rear-left</code>, <code>top-rear-right</code>, <code>top-rear-center</code>, or any of the 32 auxiliary channel names <code>aux0</code> to <code>aux31</code>.</dd>
<dt><code>&#8211;fix-format</code></dt>
<dd> If passed, the sample format of the stream is changed to the native format of the sink the stream is connected to.</dd>
<dt><code>&#8211;fix-rate</code></dt>
<dd> If passed, the sampling rate of the stream is changed to the native rate of the sink the stream is connected to.</dd>
<dt><code>&#8211;fix-channels</code></dt>
<dd> If passed, the number of channels and the channel map of the stream is changed to the native number of channels and the native channel map of the sink the stream is connected to.</dd>
<dt><code>&#8211;no-remix</code></dt>
<dd> Never upmix or downmix channels.</dd>
<dt><code>&#8211;no-remap</code></dt>
<dd> Never remap channels. Instead of mapping channels by their name this will match them solely by their index/order.</dd>
<dt><code>&#8211;latency</code><i>=BYTES</i></dt>
<dd> Explicitly configure the latency, with a time specified in bytes in the selected sample format. If left out the server will pick the latency, usually relatively high for power saving reasons. Use either this option or <code>&#8211;latency-msec</code>, but not both.</dd>
<dt><code>&#8211;latency-msec</code><i>=MSEC</i></dt>
<dd> Explicitly configure the latency, with a time specified in milliseconds. If left out the server will pick the latency, usually relatively high for power saving reasons. Use either this option or <code>&#8211;latency</code>, but not both.</dd>
<dt><code>&#8211;process-time</code><i>=BYTES</i></dt>
<dd> Explicitly configure the process time, with a time specified in bytes in the selected sample format. If left out the server will pick the process time. Use either this option or <code>&#8211;process-time-msec</code>, but not both.</dd>
<dt><code>&#8211;process-time-msec</code><i>=MSEC</i></dt>
<dd> Explicitly configure the process time, with a time specified in milliseconds. If left out the server will pick the process time. Use either this option or <code>&#8211;process-time</code>, but not both.</dd>
<dt><code>&#8211;property</code><i>=PROPERTY=VALUE</i></dt>
<dd> Attach a property to the client and stream. May be used multiple times</dd>
<dt><code>&#8211;raw</code></dt>
<dd> Play/record raw audio data. This is the default if this program is invoked as <i>pacat</i>, <i>parec</i> or <i>pamon</i>.</dd>
<dt><code>&#8211;file-format</code><i>[=FFORMAT]</i></dt>
<dd> Play/record encoded audio data in the file format specified. This is the default if this program is invoked as <i>paplay</i> and <i>parecord</i>.</dd>
<dt><code>&#8211;list-file-formats</code></dt>
<dd> List supported file formats.</dd></dl>
<h2>LIMITATIONS</h2>
<p> Due to a limitation in <i>libsndfile</i> <i>paplay</i> currently does not always set the correct channel mapping for playback of multichannel (i.e. surround) audio files, even if the channel mapping information is available in the audio file.</p>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pactl/">pactl</a>(1)</code> </p>
