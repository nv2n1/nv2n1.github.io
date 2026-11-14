---
title: "wvgain(1)"
name: "wvgain"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wvgain/"
description: "wvgain – adds ReplayGain information to wavpack files"
---

<h2 class="name">NAME</h2>
<p> wvgain &#8211; adds ReplayGain information to wavpack files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>wvgain</code> [<i>-options</i>] <i>INFILE</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<p> <code>wvgain</code></p>
<dd>perceptually analyzes WavPack audio files for volume, calculates ReplayGain information based on this, and adds the appropriate APEv2 tag fields. ReplayGain-enabled players will use this information to produce the same perceived loudness on all tracks. Both individual track and whole album ReplayGain information can be calculated.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> album mode (all files scanned are considered an album)</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> clean ReplayGain values from all files</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> display calculated values only (no files are modified)</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> ignore .wvc file (forces hybrid lossy)</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> new files only (skip files with track info, or album info if album mode specified)</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> show stored values only (no analysis)</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> quiet (keep console output to a minimum)</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wavpack/">wavpack</a></code>(1), <code><a href="/docs/linux/man/1-wvunpack/">wvunpack</a></code>(1) </p>
<p> Please visit <a rel="nofollow" href="http://www.wavpack.com">www.wavpack.com</a> for more information</p>
<h2>COPYRIGHT</h2>
<p> This manual page was written by Sebastian Dröge &lt;slomo [at] debian.org&gt; and David Bryant &lt;david [at] wavpack.com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the BSD License.</p>
<h2>AUTHORS</h2>
<p> <code>Sebastian Dröge</code> &lt;slomo [at] debian.org&gt; </p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>David Bryant</code> &lt;david [at] wavpack.com&gt; </p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Sebastian Dröge<br />
 Copyright &#169; 2009 David Bryant </p>
<h2>Index</h2>
