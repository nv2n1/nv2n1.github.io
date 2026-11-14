---
title: "wvunpack(1)"
name: "wvunpack"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wvunpack/"
description: "wvunpack – decodes wavpack encoded files"
---

<h2 class="name">NAME</h2>
<p> wvunpack &#8211; decodes wavpack encoded files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>wvunpack</code> [<i>-options</i>] <i>INFILE</i>&#8230; [<code>-o&nbsp;<wbr></code><i>OUTFILE</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>wvunpack</code></p>
<dd>decodes WavPack files back to their uncompressed wav or raw form using the options provided. Unless overridden with the <code>-o</code> switch, the resulting filename will be <i>source-name.wav</i> (or <i>source-name.raw</i> when <code>-r</code> used). Multiple WavPack input files may be specified resulting in multiple output files, and in that case <code>-o</code> may be used to specify an alternate target directory. <i>Stdin</i> and <i>stdout</i> may be specified with &#8220;-&#8220;. WavPack files are generally created with the <code>wavpack</code> program.</p>
<h2>OPTIONS</h2>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> blindly decode all stream blocks and ignore length info</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> do not decode audio but instead just extract cuesheet stored in APEv2 tag to <i>stdout</i> (equivalent to <code>-x </code><code>&#8220;cuesheet&#8221;</code>)</dl>
<p> <code>-cc</code></p>
<dl>
<dt>
<dd> extract cuesheet stored in APEv2 tag to <i>source-name.cue</i> file in same directory as decoded audio file (equivalent to <code>-xx </code><code>&#8220;cuesheet=%a.cue&#8221;</code>)</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> delete source file if successful (use with caution!)</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> display extended help</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> ignore .wvc file (forces hybrid lossy decompression)</dl>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> calculate and display MD5 signature; verify if lossless</dl>
<p> <code>&#8211;no-utf8-convert</code></p>
<dl>
<dt>
<dd> leave extracted text tags in UTF-8 encoding during extraction or display</dl>
<p> <code>-o </code><i>OUTFILE</i></p>
<dl>
<dt>
<dd> specify output filename (only if single source file) or target directory (must exist)</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> quiet (keep console output to a minimum)</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> force raw audio decode by skipping RIFF headers &amp; trailers, results in <i>source-name.raw</i></dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> do not decode audio but simply display summary information about WavPack file to <i>stdout</i></dl>
<p> <code>-ss</code></p>
<dl>
<dt>
<dd> do not decode audio but simply display summary and tag information about WavPack file to <i>stdout</i></dl>
<p> <code> &#8211;skip=[</code><i>sample</i><code>|</code><i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss.ss</i><code>] </code></p>
<dl>
<dt>
<dd> start decoding at specified sample or time index</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> copy input file&#8217;s time stamp to output file(s)</dl>
<p> <code> &#8211;until=[+|-][</code><i>sample</i><code>|</code><i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss.ss</i><code>] </code></p>
<dl>
<dt>
<dd> stop decoding at specified sample or time index, specifying a <code>+</code> causes sample/time to be relative to <code>&#8211;skip</code> point, specifying a <code>&#8211;</code> causes sample/time to be relative to EOF</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> verify source data only (no output file created)</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> regenerate fresh wav header (ingore RIFF data stored in WavPack file)</dl>
<p> <code>-x </code><code>&#8220;</code><i>Field</i>&#8221;</p>
<dl>
<dt>
<dd> do not decode audio but instead just extract the specified tag field to <i>stdout</i></dl>
<p> <code>-xx </code><code>&#8220;</code><i>Field</i>[=<i>file</i>]&#8221;</p>
<dl>
<dt>
<dd> extract the specified tag field to named file in same directory as decoded audio file; optional filename specification may contain <code>%a</code> which is replaced with the audio file base name, <code>%t</code> replaced with the tag field name (note: comes from data for binary tags) and <code>%e</code> replaced with the extension from the binary tag source file (or &#8220;txt&#8221; for text tag).</dl>
<p> <code>-y</code></p>
<dl>
<dt>
<dd> yes to overwrite warning (use with caution!)</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wavpack/">wavpack</a></code>(1), <code><a href="/docs/linux/man/1-wvgain/">wvgain</a></code>(1) </p>
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
