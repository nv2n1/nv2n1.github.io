---
title: "oggjoin(1)"
name: "oggjoin"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggjoin/"
description: "oggJOIN – multiplexes ogg streams (.ogv, .ogg or oga)"
---

<p>oggJOIN &#8211; multiplexes ogg streams (.ogv, .ogg or oga)</p>
<h2>Synopsis</h2>
<p><code>oggJoin outfile.ogv file1.ogv file2.ogg</code></p>
<h2>Description</h2>
<p><code>oggJoin</code> merges ogg audio (vorbis) and ogg video (theora) files into one single ogg file. This is often also called multiplexing. </p>
<p> The first file given with the command is the output file. The following files are the files (usually a video and an audio stream) that should be placed into the new file as parallel streams. This is done on a per page basis and is very efficient and fast. </p>
<p> As oggJoin uses it&#8217;s own timestamp creation method, both streams start exactly at start time &#8216;0&#8217;. This is always the case even if the original files started at a different time (due to internal timing information). So the video and audio streams are always synchronized. This helps using files from different live stream sources or cuted material. </p>
<p> In case of unknown stream types (other than theora or vorbis), there is actually (as of version 0.8) no timing interpreter available. So you can not use these streams for multiplexing. </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oggcut/">oggCut</a></code>(1), <code><a href="/docs/linux/man/1-oggcat/">oggCat</a></code>(1), <code><a href="/docs/linux/man/1-oggsplit/">oggSplit</a></code>(1), <code><a href="/docs/linux/man/1-oggresize/">oggResize</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggthumb/">oggThumb</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
