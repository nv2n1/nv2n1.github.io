---
title: "alsabat(1)"
name: "alsabat"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsabat/"
description: "alsabat – command-line sound tester for ALSA sound card driver"
---

<h2 class="name">NAME</h2>
<p> alsabat &#8211; command-line sound tester for ALSA sound card driver</p>
<h2>SYNOPSIS</h2>
<p> <code>alsabat</code> [<i>flags</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>ALSABAT(ALSA Basic Audio Tester)</code> is a simple command-line utility intended to help automate audio driver and sound server testing with little human interaction. ALSABAT can be used to test audio quality, stress test features and test audio before and after PM state changes. </p>
<p> ALSABAT&#8217;s design is relatively simple. ALSABAT plays an audio stream and captures the same stream in either a digital or analog loop back. It then compares the captured stream using a FFT to the original to determine if the test case passes or fails. </p>
<p> ALSABAT can either run wholly on the target machine being tested (standalone mode) or can run as a client/server mode where by alsabat client runs on the target and runs as a server on a separate tester machine. The client/server mode still requires some manual interaction for synchronization, but this is actively being developed for future releases. </p>
<p> The hardware testing configuration may require the use of an analog cable connecting target to tester machines or a cable to create an analog loopback if no loopback mode is available on the sound hardware that is being tested. An analog loopback cable can be used to connect the &quot;line in&quot; to &quot;line out&quot; jacks to create a loopback. If only headphone and mic jacks (or combo jack) are available then the following simple circuit can be used to create an analog loopback :- </p>
<p> <a rel="nofollow" href="https://source.android.com/devices/audio/loopback.html">https://source.android.com/devices/audio/loopback.html</a> </p>
<p> If tinyalsa is installed in system, user can choose tinyalsa as backend lib of alsabat, with configure option &quot;&#8211;enable-alsabat-backend-tiny&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd> Help: show syntax.</p>
<dt><i>-D</i></p>
<dd> Select sound card to be tested by name.</p>
<dt><i>-P</i></p>
<dd> Select the playback PCM device.</p>
<dt><i>-C</i></p>
<dd> Select the capture PCM device.</p>
<dt><i>-f</i></p>
<dd> Sample format<br />
 Recognized sample formats are: U8 S16_LE S24_3LE S32_LE<br />
 Some of these may not be available on selected hardware<br />
 The available format shortcuts are: </p>
<pre><code>
- f cd(16 bit little endian, 44100, stereo)[-f S16_LE - c2 - r44100] - f dat(16 bit little endian, 48000, stereo)[-f S16_LE - c2 - r48000]
</code></pre>
<p> If no format is given S16_LE is used.</p>
<dt><i>-c</i></p>
<dd> The number of channels. The default is one channel. Valid values at the moment are 1 or 2.</p>
<dt><i>-r</i></p>
<dd> Sampling rate in Hertz. The default rate is 44100 Hertz. Valid values depends on hardware support.</p>
<dt><i>-n</i></p>
<dd> Duration of generated signal. The value could be either of the two forms:<br />
 1. Decimal integer, means number of frames;<br />
 2. Floating point with suffix &#8216;s&#8217;, means number of seconds.<br />
 The default is 2 seconds.</p>
<dt><i>-k</i></p>
<dd> Sigma k value for analysis.<br />
 The analysis function reads data from WAV file, run FFT against the data to get magnitude of frequency vectors, and then calculates the average value and standard deviation of frequency vectors. After that, we define a threshold:<br />
 threshold = k * standard_deviation + mean_value<br />
 Frequencies with amplitude larger than threshold will be recognized as a peak, and the frequency with largest peak value will be recognized as a detected frequency.<br />
 ALSABAT then compares the detected frequency to target frequency, to decide if the detecting passes or fails.<br />
 The default value is 3.0.</p>
<dt><i>-F</i></p>
<dd> Target frequency for signal generation and analysis, in Hertz. The default is 997.0 Hertz. Valid range is (DC_THRESHOLD, 40% * Sampling rate).</p>
<dt><i>-p</i></p>
<dd> Total number of periods to play or capture.</p>
<dt><i>&#8211;log=#</i></p>
<dd> Write stderr and stdout output to this log file.</p>
<dt><i>&#8211;file=#</i></p>
<dd> Input WAV file for playback.</p>
<dt><i>&#8211;saveplay=#</i></p>
<dd> Target WAV file to save capture test content.</p>
<dt><i>&#8211;local</i></p>
<dd> Internal loopback mode. Playback, capture and analysis internal to ALSABAT only. This is intended for developers to test new ALSABAT features as no audio is routed outside of ALSABAT.</p>
<dt><i>&#8211;standalone</i></p>
<dd> Add support for standalone mode where ALSABAT will run on a different machine to the one being tested. In standalone mode, the sound data can be generated, playback and captured just like in normal mode, but will not be analyzed. The ALSABAT being built without libfftw3 support is always in standalone mode. The ALSABAT in normal mode can also bypass data analysis using option &quot;&#8211;standalone&quot;.</p>
<dt><i>&#8211;roundtriplatency</i></p>
<dd> Round trip latency test. Audio latency is the time delay as an audio signal passes through a system. There are many kinds of audio latency metrics. One useful metric is the round trip latency, which is the sum of output latency and input latency.</p>
<dt><i>&#8211;snr-db=#</i></p>
<dd> Noise detection threshold in SNR (dB). 26dB indicates 5% noise in amplitude. ALSABAT will return error if signal SNR is smaller than the threshold.</p>
<dt><i>&#8211;snr-pc=#</i></p>
<dd> Noise detection threshold in percentage of noise amplitude (%). ALSABAT will return error if the noise amplitude is larger than the threshold. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>alsabat -P plughw:0,0 -C plughw:0,0 -c 2 -f S32_LE -F 250</code></p>
<dd> Generate and play a sine wave of 250 Hertz with 2 channel and S32_LE format, and then capture and analyze. </p>
<dt><code>alsabat -P plughw:0,0 -C plughw:0,0 &#8211;file 500Hz.wav</code></p>
<dd> Play the RIFF WAV file &quot;500Hz.wav&quot; which contains 500 Hertz waveform LPCM data, and then capture and analyze. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> On success, returns 0.<br />
 If no peak be detected, returns -1001;<br />
 If only DC be detected, returns -1002;<br />
 If peak frequency does not match with the target frequency, returns -1003. </p>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-aplay/">aplay</a>(1) </code> </p>
<h2>BUGS</h2>
<p> Currently only support RIFF WAV format with PCM data. Please report any bugs to the alsa-devel mailing list. </p>
<h2>AUTHOR</h2>
<p> <code>alsabat</code> is by Liam Girdwood &lt;liam.r.girdwood [at] linux.intel.com&gt;, Bernard Gautier &lt;bernard.gautier [at] intel.com&gt; and Han Lu &lt;han.lu [at] intel.com&gt;. This document is by Liam Girdwood &lt;liam.r.girdwood [at] linux.intel.com&gt; and Han Lu &lt;han.lu [at] intel.com&gt;. </p>
<h2>Index</h2>
