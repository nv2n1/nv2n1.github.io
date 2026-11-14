---
title: "speaker-test(1)"
name: "speaker-test"
section: "1"
letter: "s"
url: "/docs/linux/man/1-speaker-test/"
description: "speaker-test – command-line speaker test tone generator for ALSA"
---

<h2 class="name">NAME</h2>
<p> speaker-test &#8211; command-line speaker test tone generator for ALSA </p>
<h2>SYNOPSIS</h2>
<p> <code>speaker-test [-options]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>speaker-test</code> generates a tone that can be used to test the speakers of a computer. </p>
<p> <code>speaker-test</code> by default will test the <i>default</i> device. If you want to test another sound device you will have first to get a list of all of the sound cards in your system and the devices associated with those cards. Notice that there might be for example, one device for analog sound, one for digital sound and one for HDMI sound. To get the list of available cards and devices you can run <code>aplay -L</code>. </p>
<pre>
$ aplay -L
null
    Discard all samples (playback) or generate zero samples (capture)
default:CARD=ICH5
    Intel ICH5, Intel ICH5
    Default Audio Device
front:CARD=ICH5,DEV=0
    Intel ICH5, Intel ICH5
    Front speakers
surround40:CARD=ICH5,DEV=0
    Intel ICH5, Intel ICH5
    4.0 Surround output to Front and Rear speakers
(...)
</pre>
<p> in the above example, there are four devices listed: null, default, front and surround40. So, if you want to test the last device you can run <code>speaker-test -Dsurround40:ICH5 -c 6</code>. The <code>-c</code> option will indicate that the six audio channels in the device have to be tested. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> | <code>&#8211;channels</code> <i>NUM</i></p>
<dd> <i>NUM</i> channels in stream </p>
<dt><code>-D</code> | <code>&#8211;device</code> <i>NAME</i></p>
<dd> PCM device name <i>NAME</i> </p>
<dt><code>-f</code> | <code>&#8211;frequency</code> <i>FREQ</i></p>
<dd> sine wave of <i>FREQ</i> Hz </p>
<dt><code>&#8211;help</code></p>
<dd> Print usage help </p>
<dt><code>-b</code> | <code>&#8211;buffer</code> <i>TIME</i></p>
<dd> Use buffer size of <i>TIME</i> microseconds. When 0 is given, use the maximal buffer size. The default value is 0. </p>
<dt><code>-p</code> | <code>&#8211;period</code> <i>TIME</i></p>
<dd> Use period size of <i>TIME</i> microseconds. When 0 is given, the periods given by <code>-P</code> option is used. The default value is 0. </p>
<dt><code>-P</code> | <code>&#8211;nperiods</code> <i>PERIODS</i></p>
<dd> Use number of periods. The default value is 4. </p>
<dt><code>-r</code> | <code>&#8211;rate</code> <i>RATE</i></p>
<dd> stream of <i>RATE</i> Hz </p>
<dt><code>-t</code> | <code>&#8211;test</code> <code>pink</code>|<code>sine</code>|<code>wav</code></p>
<dd> <code>-t pink</code> means use pink noise (default). </p>
<p> Pink noise is perceptually uniform noise &#8212; that is, it sounds like every frequency at once. If you can hear any tone it may indicate resonances in your speaker system or room. </p>
<p> <code>-t sine</code> means to use sine wave. </p>
<p> <code>-t wav</code> means to play WAV files, either pre-defined files or given via <code>-w</code> option. </p>
<p> You can pass the number from 1 to 3 as a backward compatibility. </p>
<dt><code>-l</code> | <code>&#8211;nloops</code> <i>COUNT</i></p>
<dd>
<p> Specifies the number of loops. Zero means to run infinitely. </p>
<p> When <code>-s</code> option below with a valid channel is given, <code>speaker-test</code> will perform always a single-shot without looping. </p>
<dt><code>-s</code> | <code>&#8211;speaker</code> <i>CHANNEL</i></p>
<dd> Do a single-shot speaker test for the given channel. The channel number starts from 1. The channel number corresponds to left, right, rear-left, rear-right, center, LFE, side-left, side-right, and so on. </p>
<p> For example, when 1 is passed, it tests the left channel only once rather than both channels with looping. </p>
<dt><code>-w</code> | <code>&#8211;wavfile</code> <i>FILE</i></p>
<dd> Use the given WAV file for the playback instead of pre-defined WAV files. </p>
<dt><code>-W</code> | <code>&#8211;wavdir</code> <i>DIRECTORY</i></p>
<dd> Specify the directory containing WAV files for playback. The default path is <i>/usr/share/sounds/alsa</i>. </p>
<dt><code>-m</code> | <code>&#8211;chmap</code> <i>MAP</i></p>
<dd> Pass the channel map to override. If the playback in a specific channel order or channel positions is required, pass the channel position strings to this option. </p>
<dt><code>-X</code> | <code>&#8211;force-frequency</code></p>
<dd> Allow supplied <i>FREQ</i> to be outside the default range of 30-8000Hz. A minimum of 1Hz is still enforced. </p>
</dl>
<h2>USAGE EXAMPLES</h2>
<p> Produce stereo sound from one stereo jack:</p>
<dl>
<dt>
<dd>
<pre>
  speaker-test -Dplug:front -c2
</pre>
</dl>
<p> Produce 4 speaker sound from two stereo jacks:</p>
<dl>
<dt>
<dd>
<pre>
  speaker-test -Dplug:surround40 -c4
</pre>
</dl>
<p> Produce 5.1 speaker sound from three stereo jacks:</p>
<dl>
<dt>
<dd>
<pre>
  speaker-test -Dplug:surround51 -c6
</pre>
</dl>
<p> To send a nice low 75Hz tone to the Woofer and then exit without touching any other speakers:</p>
<dl>
<dt>
<dd>
<pre>
  speaker-test -Dplug:surround51 -c6 -s1 -f75
</pre>
</dl>
<p> To do a 2-speaker test using the spdif (coax or optical) output:</p>
<dl>
<dt>
<dd>
<pre>
  speaker-test -Dplug:spdif -c2
</pre>
</dl>
<p> Play in the order of front-right and front-left from the front PCM</p>
<dl>
<dt>
<dd>
<pre>
  speaker-test -Dplug:front -c2 -mFR,FL
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aplay/">aplay</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> The speaker-test program was written by James Courtier-Dutton. Pink noise support was added by Nathan Hurst. Further extensions by Takashi Iwai. </p>
<h2>Index</h2>
