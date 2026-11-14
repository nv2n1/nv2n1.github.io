---
title: "dubdv(1)"
name: "dubdv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dubdv/"
description: "dubdv – insert audio into a digital video stream"
---

<h2>NAME</h2>
<p> dubdv &#8211; insert audio into a digital video stream</p>
<h2>SYNOPSIS</h2>
<p> <code>dubdv</code> [ <code>options</code> ] <i>audio_inputfR [ filename or &#8211; for stdin ]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dubdv</code> reads the audio from a WAV file or the OSS DSP device and overwrites the existing audio in a raw DV file or stream.</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show dubdv version number.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> show encoder statistics / status information.</p>
<dt><code>-a</code>, <code>&#8211;audio-input</code>=<i>filter-name</i></p>
<dd> Choose audio-input-filter: [none, &gt;wav&lt;, dsp] WAV is the default <i>audio_input</i> format.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>filter-name</i></p>
<dd> Choose output-filter: [&gt;raw&lt;]</p>
<dt><code>-t</code>, <code>&#8211;truncate</code></p>
<dd> truncate output at end of DV input.</p>
<dt><code>-r</code>, <code>&#8211;repeat</code>=<i>count</i></p>
<dd> repeat the first video frame <i>count</i> times. This option does not dub audio into the repeated frame.</dl>
<p> Help Options</p>
<dl>
<dt>&#8211;<code>?</code>, <code>&#8211;help</code></p>
<dd> Show help message.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-playdv/">playdv</a></code>(1),<code><a href="/docs/linux/man/1-dvconnect/">dvconnect</a></code>(1),<code><a href="/docs/linux/man/1-encodedv/">encodedv</a></code>(1).</p>
<h2>AVAILABILITY</h2>
<p> See <a rel="nofollow" href="http://libdv.sourceforge.net/">http://libdv.sourceforge.net/</a> for the latest version.</p>
<h2>AUTHORS</h2>
<p> <code>dubdv</code> was written by James Bowman &lt;jamesb [at] excamera.com&gt; and Peter Schlaile &lt;udbz [at] rz.uni-karlsruhe.de&gt;. </p>
<p> This manual page is based on dubdv&#8217;s help message and was written by Dan Dennedy &lt;dan [at] dennedy.org&gt;. </p>
<h2>Index</h2>
