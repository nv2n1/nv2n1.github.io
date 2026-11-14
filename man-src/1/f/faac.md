---
title: "faac(1)"
name: "faac"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faac/"
description: "faac – open source MPEG-4 and MPEG-2 AAC encoder"
---

<h2 class="name">NAME</h2>
<p> faac &#8211; open source MPEG-4 and MPEG-2 AAC encoder</p>
<h2>SYNOPSIS</h2>
<p> <code>faac</code> [<i>options</i>] [-o&nbsp;<wbr><i>outfile</i>] <i>infiles</i> &#8230; </p>
<p> &lt;<i>infiles</i>&gt; and/or &lt;<i>outfile</i>&gt; can be &quot;-&quot;, which means stdin/stdout. </p>
<h2>DESCRIPTION</h2>
<p> <code>FAAC</code> is an open source MPEG-4 and MPEG-2 AAC encoder, it is licensed under the LGPL license. Note that the quality of <code>FAAC</code> is not up to par with the currently best AAC encoders available. </p>
<h2>FEATURES</h2>
<dl>
<dt>* Portable</p>
<dd>
<dt>* Reasonably fast</p>
<dd>
<dt>* LC, Main, LTP support</p>
<dd>
<dt>* DRM support through DreaM (optional)</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q&nbsp;<wbr></code>&lt;<i>quality</i>&gt;</p>
<dd> Set default variable bitrate (VBR) quantizer quality in percent (default: 100).</p>
<dt><code>-b&nbsp;<wbr></code>&lt;<i>bitrate</i>&gt;</p>
<dd> Set average bitrate (ABR, lower quality mode) to approximately <i>bitrate</i> kbps.</p>
<dt><code>-c&nbsp;<wbr></code>&lt;<i>freq</i>&gt;</p>
<dd> Set the bandwidth in Hz (default: automatic).</p>
<dt><code>-o&nbsp;<wbr></code><i>X</i></p>
<dd> Set output file to <i>X</i> (only for one input file).</p>
<dt><code>-r</code></p>
<dd> Use RAW AAC output file.</p>
<dt><code>-P</code></p>
<dd> Raw PCM input mode (default: 44100Hz 16bit stereo).</p>
<dt><code>-R</code></p>
<dd> Raw PCM input rate.</p>
<dt><code>-B</code></p>
<dd> Raw PCM input sample size (8, 16 [default], 24 or 32bits).</p>
<dt><code>-C</code></p>
<dd> Raw PCM input channels.</p>
<dt><code>-X</code></p>
<dd> Raw PCM swap input bytes</p>
<dt><code>-I&nbsp;<wbr></code>&lt;<i>C</i>,<i>LF</i>&gt;</p>
<dd> Input channel config (default: 3,4 [which means Center is third and LFE is fourth]). </p>
</dl>
<h2>MP4-SPECIFIC OPTIONS (if built with MP4V2)</h2>
<dl>
<dt><code>-w</code></p>
<dd> Wrap AAC data in MP4 container (default for *.mp4 and *.m4a).</p>
<dt><code>-s</code></p>
<dd> Optimize MP4 container layout after encoding.</p>
<dt><code>&#8211;artist&nbsp;<wbr></code><i>X</i></p>
<dd> Set artist to <i>X</i></p>
<dt><code>&#8211;writer&nbsp;<wbr></code><i>X</i></p>
<dd> Set writer to <i>X</i></p>
<dt><code>&#8211;title&nbsp;<wbr></code><i>X</i></p>
<dd> Set title to <i>X</i></p>
<dt><code>&#8211;genre&nbsp;<wbr></code><i>X</i></p>
<dd> Set genre to <i>X</i></p>
<dt><code>&#8211;album&nbsp;<wbr></code><i>X</i></p>
<dd> Set album to <i>X</i></p>
<dt><code>&#8211;compilation</code></p>
<dd> Set compilation</p>
<dt><code>&#8211;track&nbsp;<wbr></code><i>X</i></p>
<dd> Set track to <i>X</i> (number/total)</p>
<dt><code>&#8211;disc&nbsp;<wbr></code><i>X</i></p>
<dd> Set disc to <i>X</i> (number/total)</p>
<dt><code>&#8211;year&nbsp;<wbr></code><i>X</i></p>
<dd> Set year to <i>X</i></p>
<dt><code>&#8211;cover-art&nbsp;<wbr></code><i>X</i></p>
<dd> Read cover art from file <i>X</i></p>
<dt><code>&#8211;comment&nbsp;<wbr></code><i>X</i></p>
<dd> Set comment to <i>X</i> </p>
</dl>
<h2>DOCUMENTATION</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> for short help on using FAAC.</p>
<dt><code>&#8211;long-help</code></p>
<dd> for a description of all options for FAAC.</p>
<dt><code>&#8211;license</code></p>
<dd> for the license terms for FAAC. </p>
</dl>
<h2>AUTHORS</h2>
<p> <code>FAAC</code> was written by M. Bakker &lt;menno [at] audiocoding.com&gt;. </p>
<p> This manpage was written by Fabian Greffrath &lt;fabian [at] debian-unofficial.org&gt; for the Debian Unofficial project (but may be used by others, of course). </p>
<h2>Index</h2>
