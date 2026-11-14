---
title: "playdv(1)"
name: "playdv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-playdv/"
description: "playdv – display digital video streams on screen"
---

<h2>NAME</h2>
<p> playdv &#8211; display digital video streams on screen</p>
<h2>SYNOPSIS</h2>
<p> <code>playdv</code> [ <code>options</code> ] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>playdv</code> reads in DV-encoded video data from <i>file</i> and displays it on screen.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show playdv version number.</p>
<dt><code>&#8211;disable-audio</code></p>
<dd> skip audio decoding.</p>
<dt><code>&#8211;disable-video</code></p>
<dd> skip video decoding.</p>
<dt><code>-n</code>, <code>&#8211;num-frames</code>=<i>count</i></p>
<dd> stop playing after <i>count</i> frames.</p>
<dt><code>&#8211;dump-frames</code>=<i>pattern</i></p>
<dd> save a PPM image of each frame to an individual file. <i>pattern</i> determines the file names and may be given in <i>printf</i>-style taking one numeric argument that gets replaced with the current frame number. Like capture%05d.ppm for files capture00001.ppm, capture00002.ppm, etc. Use <i>&#8211;</i> to stream the frames to stdout.</p>
<dt><code>&#8211;no-mmap</code></p>
<dd> don&#8217;t use mmap for reading (useful for pipes).</p>
<dt><code>-l</code>, <code>&#8211;loop-count</code>=<i>count</i></p>
<dd> loop playback <i>count=</i> times, 0 for infinite.</dl>
<p> Audio Output Options</p>
<dl>
<dt><code>&#8211;audio-device</code>=<i>devicename</i></p>
<dd> target audio device; e.g. /dev/dsp, which is also the default.</p>
<dt><code>&#8211;audio-file</code>=<i>file</i></p>
<dd> send raw decoded audio stream to <i>file</i>, skipping audio ioctls.</p>
<dt><code>&#8211;audio-mix</code>=<i>(-16 .. 16)</i></p>
<dd> mixing level of 4 channel audio for 32KHz 12bit. 0 [default]. -16 selects second channel, 16 selects first channel.</dl>
<p> Video Output Options</p>
<dl>
<dt><code>-d</code>, <code>&#8211;display=</code>(0|1|2|3)</p>
<dd> method used to display video data on screen: 0=autoselect [default], 1=gtk, 2=Xv, 3=SDL. Xv is usually the fastest but requires XFree86 version 4.0 or higher with XVideo extensions.</p>
<dt><code>&#8211;aspect</code>=(n|w|normal|wide)</p>
<dd> video display aspect ratio (for Xv only): n=normal 4:3, w=wide 16:9 . Not all window manager support resizing at fixed aspect ratio. If they do, resizing is done at fixed aspect ratio.</p>
<dt><code>&#8211;size</code>=(10 .. 100)</p>
<dd> initial scaleing percentage (for Xv only): 10 &lt;= n &lt;= 100.</dl>
<p> Decoder Options</p>
<dl>
<dt><code>-V</code>, <code>&#8211;video-system</code>=(0|1|2|3)</p>
<dd> sets the video standard of the incoming DV data: 0=autoselect [default], 1=525/60 4:1:1 (NTSC), 2=625/50 4:2:0 (PAL,IEC 61834 DV), 3=625/50 4:1:1 (PAL,SMPTE 314M DV). Autoselect usually works fine. Only use this option if you know what you are doing.</dl>
<p> Video Decode Options</p>
<dl>
<dt><code>-q</code>, <code>&#8211;quality=</code>(1|2|3)</p>
<dd> quality level of desired video decoding. The process of decoding DV data is split into several steps. Each additional step enhances output quality, but of course also slows down decoding. If your machine is too slow to keep up an interactive frame rate, you might want to decrease this number: 1=DC and no ACs, 2=DC and single-pass for ACs, 3=DC and multi-pass for ACs [default].</p>
<dt><code>-m</code>, <code>&#8211;monochrome</code></p>
<dd> skip decoding of color blocks. Another way to speed up the decoding process.</dl>
<p> Audio Decode Options</p>
<dl>
<dt><code>-f</code>, <code>&#8211;frequency=</code>(0|1|2|3)</p>
<dd> frequency of audio data in the input stream: 0=autodetect [default], 1=32 kHz, 2=44.1 kHz, 3=48 kHz.</p>
<dt><code>-Q</code>, <code>&#8211;quantization=</code>(0|1|2)</p>
<dd> dynamic range of audio data in the input stream: 0=autodetect [default], 1=12 bit, 2=16bit.</p>
<dt><code>-e</code>, <code>&#8211;emphasis=</code>(0|1|2)</p>
<dd> first-order preemphasis of 50/15 us: 0=autodetect [default], 1=on, 2=off.</dl>
<p> Help Options</p>
<dl>
<dt>&#8211;<code>?</code>, <code>&#8211;help</code></p>
<dd> Show help message. Use this command to get a brief description of available options.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvconnect/">dvconnect</a></code>(1),<code><a href="/docs/linux/man/1-dubdv/">dubdv</a></code>(1),<code><a href="/docs/linux/man/1-encodedv/">encodedv</a></code>(1).</p>
<h2>AVAILABILITY</h2>
<p> See <a rel="nofollow" href="http://libdv.sourceforge.net/">http://libdv.sourceforge.net/</a> for the latest version.</p>
<h2>AUTHORS</h2>
<p> <code>playdv</code> was written by Charles &#8216;Buck&#8217; Krasic &lt;krasic [at] acm.org&gt; and Erik Walthinsen &lt;omega [at] cse.ogi.edu&gt;. </p>
<p> This manual page is based on playdv&#8217;s help message and was written by Daniel Kobras &lt;kobras [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
