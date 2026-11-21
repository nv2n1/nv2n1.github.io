---

title: "faac(1)"
name: "faac"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faac/"
description: "faac – open source MPEG-4 and MPEG-2 AAC encoder"
---

<p> <code>faac</code> [<i>options</i>] [-o&nbsp;<wbr><i>outfile</i>] <i>infiles</i> &#8230; </p>
<p> &lt;<i>infiles</i>&gt; and/or &lt;<i>outfile</i>&gt; can be &quot;-&quot;, which means stdin/stdout. </p>
<p> <code>FAAC</code> is an open source MPEG-4 and MPEG-2 AAC encoder, it is licensed under the LGPL license. Note that the quality of <code>FAAC</code> is not up to par with the currently best AAC encoders available. </p>
<h2>FEATURES</h2>
<dl>
<dt>* Portable</dt>
<dd>
</dd><dt>* Reasonably fast</dt>
<dd>
</dd><dt>* LC, Main, LTP support</dt>
<dd>
</dd><dt>* DRM support through DreaM (optional)</dt>
<dd>
</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q&nbsp;<wbr></code>&lt;<i>quality</i>&gt;</dt>
<dd> Set default variable bitrate (VBR) quantizer quality in percent (default: 100).</dd>
<dt><code>-b&nbsp;<wbr></code>&lt;<i>bitrate</i>&gt;</dt>
<dd> Set average bitrate (ABR, lower quality mode) to approximately <i>bitrate</i> kbps.</dd>
<dt><code>-c&nbsp;<wbr></code>&lt;<i>freq</i>&gt;</dt>
<dd> Set the bandwidth in Hz (default: automatic).</dd>
<dt><code>-o&nbsp;<wbr></code><i>X</i></dt>
<dd> Set output file to <i>X</i> (only for one input file).</dd>
<dt><code>-r</code></dt>
<dd> Use RAW AAC output file.</dd>
<dt><code>-P</code></dt>
<dd> Raw PCM input mode (default: 44100Hz 16bit stereo).</dd>
<dt><code>-R</code></dt>
<dd> Raw PCM input rate.</dd>
<dt><code>-B</code></dt>
<dd> Raw PCM input sample size (8, 16 [default], 24 or 32bits).</dd>
<dt><code>-C</code></dt>
<dd> Raw PCM input channels.</dd>
<dt><code>-X</code></dt>
<dd> Raw PCM swap input bytes</dd>
<dt><code>-I&nbsp;<wbr></code>&lt;<i>C</i>,<i>LF</i>&gt;</dt>
<dd> Input channel config (default: 3,4 [which means Center is third and LFE is fourth]). </dd>
</dl>
<h2>MP4-SPECIFIC OPTIONS (if built with MP4V2)</h2>
<dl>
<dt><code>-w</code></dt>
<dd> Wrap AAC data in MP4 container (default for *.mp4 and *.m4a).</dd>
<dt><code>-s</code></dt>
<dd> Optimize MP4 container layout after encoding.</dd>
<dt><code>&#8211;artist&nbsp;<wbr></code><i>X</i></dt>
<dd> Set artist to <i>X</i></dd>
<dt><code>&#8211;writer&nbsp;<wbr></code><i>X</i></dt>
<dd> Set writer to <i>X</i></dd>
<dt><code>&#8211;title&nbsp;<wbr></code><i>X</i></dt>
<dd> Set title to <i>X</i></dd>
<dt><code>&#8211;genre&nbsp;<wbr></code><i>X</i></dt>
<dd> Set genre to <i>X</i></dd>
<dt><code>&#8211;album&nbsp;<wbr></code><i>X</i></dt>
<dd> Set album to <i>X</i></dd>
<dt><code>&#8211;compilation</code></dt>
<dd> Set compilation</dd>
<dt><code>&#8211;track&nbsp;<wbr></code><i>X</i></dt>
<dd> Set track to <i>X</i> (number/total)</dd>
<dt><code>&#8211;disc&nbsp;<wbr></code><i>X</i></dt>
<dd> Set disc to <i>X</i> (number/total)</dd>
<dt><code>&#8211;year&nbsp;<wbr></code><i>X</i></dt>
<dd> Set year to <i>X</i></dd>
<dt><code>&#8211;cover-art&nbsp;<wbr></code><i>X</i></dt>
<dd> Read cover art from file <i>X</i></dd>
<dt><code>&#8211;comment&nbsp;<wbr></code><i>X</i></dt>
<dd> Set comment to <i>X</i> </dd>
</dl>
<h2>DOCUMENTATION</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> for short help on using FAAC.</dd>
<dt><code>&#8211;long-help</code></dt>
<dd> for a description of all options for FAAC.</dd>
<dt><code>&#8211;license</code></dt>
<dd> for the license terms for FAAC. </dd>
</dl>
<h2>AUTHORS</h2>
<p> <code>FAAC</code> was written by M. Bakker &lt;menno [at] audiocoding.com&gt;. </p>
<p> This manpage was written by Fabian Greffrath &lt;fabian [at] debian-unofficial.org&gt; for the Debian Unofficial project (but may be used by others, of course). </p>
