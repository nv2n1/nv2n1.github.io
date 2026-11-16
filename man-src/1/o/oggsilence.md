---
title: "oggsilence(1)"
name: "oggsilence"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggsilence/"
description: "oggSilence – creates a silence period in vorbis format"
---

<p>oggSilence &#8211; creates a silence period in vorbis format</p>
<h2>Synopsis</h2>
<p><code>oggSilence [options] outfile.ogg</code></p>
<h2>Description</h2>
<p><code>oggSilence</code> creates a vorbis file with a silence duration which length is specified by the -l option.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-l</dt>
<dd>Duration of the silence in ms. Default: 60000 </dd>
<p> <i>Example: -l 5000 </i> </p>
<dt>-r</dt>
<dd>Sample rate of the output file in Hz. Default: 44100 </dd>
<p> <i>Example: -r 16000</i> </p>
<dt>-d</dt>
<dd>Data rate of the silence file in bit/s. Default: 64000 </dd>
<p> <i>Example: -d 64000</i> </p>
<dt>-n</dt>
<dd>Number of output channels. Default: 2 </dd>
<p> <i>Example: -n 2</i></dl>
<h2>Example</h2>
<p><i>oggSilence -d 32000 -r 16000 -n 2 -l 10000 silence.ogg</i> </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oggcut/">oggCut</a></code>(1), <code><a href="/docs/linux/man/1-oggcat/">oggCat</a></code>(1), <code><a href="/docs/linux/man/1-oggjoin/">oggJoin</a></code>(1), <code><a href="/docs/linux/man/1-oggsplit/">oggSplit</a></code>(1), <code><a href="/docs/linux/man/1-oggresize/">oggResize</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggthumb/">oggThumb</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
</p>