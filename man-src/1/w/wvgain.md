---

title: "wvgain(1)"
name: "wvgain"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wvgain/"
description: "wvgain – adds ReplayGain information to wavpack files"
---

<p> wvgain &#8211; adds ReplayGain information to wavpack files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>wvgain</code> [<i>-options</i>] <i>INFILE</i>&#8230;</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>wvgain</code></p>
<dd>perceptually analyzes WavPack audio files for volume, calculates ReplayGain information based on this, and adds the appropriate APEv2 tag fields. ReplayGain-enabled players will use this information to produce the same perceived loudness on all tracks. Both individual track and whole album ReplayGain information can be calculated.</dd>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
</dt><dd> album mode (all files scanned are considered an album)</dd></dl>
<p> <code>-c</code></p>
<dl>
<dt>
</dt><dd> clean ReplayGain values from all files</dd></dl>
<p> <code>-d</code></p>
<dl>
<dt>
</dt><dd> display calculated values only (no files are modified)</dd></dl>
<p> <code>-i</code></p>
<dl>
<dt>
</dt><dd> ignore .wvc file (forces hybrid lossy)</dd></dl>
<p> <code>-n</code></p>
<dl>
<dt>
</dt><dd> new files only (skip files with track info, or album info if album mode specified)</dd></dl>
<p> <code>-s</code></p>
<dl>
<dt>
</dt><dd> show stored values only (no analysis)</dd></dl>
<p> <code>-q</code></p>
<dl>
<dt>
</dt><dd> quiet (keep console output to a minimum)</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wavpack/">wavpack</a></code>(1), <code><a href="/docs/linux/man/1-wvunpack/">wvunpack</a></code>(1) </p>
<p> Please visit <a rel="nofollow" href="http://www.wavpack.com">www.wavpack.com</a> for more information</p>
<h2>COPYRIGHT</h2>
<p> This manual page was written by Sebastian Dröge &lt;slomo [at] debian.org&gt; and David Bryant &lt;david [at] wavpack.com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the BSD License.</p>
<h2>AUTHORS</h2>
<p> <code>Sebastian Dröge</code> &lt;slomo [at] debian.org&gt; </p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>David Bryant</code> &lt;david [at] wavpack.com&gt; </p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Sebastian Dröge<br />
 Copyright &#169; 2009 David Bryant </p>
