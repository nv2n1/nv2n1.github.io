---
title: "oggcat(1)"
name: "oggcat"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggcat/"
description: "oggCat – concatenates two ogg video files (.ogv, .ogg or oga)"
---

<p>oggCat &#8211; concatenates two ogg video files (.ogv, .ogg or oga)</p>
<h2>Synopsis</h2>
<p><code>oggCat outfile.ogv file1.ogv file2.ogv [ file3.ogv [&#8230;] ]</code></p>
<h2>Description</h2>
<p><code>oggCat</code> concatenates two or more ogg files. </p>
<p> The first ogg file defines the outline of the newly created file (with the numbers of parallel streams). The other files are mapped to this outline. So oggCat tries to find a matching stream (video and audio) and complains if there were not enough matches found in a file. In that case this file is omitted and is not inserted into the new file. </p>
<p> The video streams must match in size and framerate. </p>
<p> The audio streams must match in number of channels, samplerate and datarate. </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt; <code><a href="/docs/linux/man/1-oggcut/">oggCut</a></code>(1), <code><a href="/docs/linux/man/1-oggjoin/">oggJoin</a></code>(1), <code><a href="/docs/linux/man/1-oggsplit/">oggSplit</a></code>(1), <code><a href="/docs/linux/man/1-oggresize/">oggResize</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggthumb/">oggThumb</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
