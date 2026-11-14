---
title: "oggsplit(1)"
name: "oggsplit"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggsplit/"
description: "oggSplit – demultiplexes ogv files"
---

<p>oggSplit &#8211; demultiplexes ogv files</p>
<h2>Synopsis</h2>
<p><code>oggSplit outfile.ogv </code></p>
<h2>Description</h2>
<p><code>oggSplit</code> demultiplexes a multiplexed ogg file into several files with one stream each.<br />
&nbsp;<wbr> An ogg video file (with extension .ogv) usually consist of an audio and a video stream. The command line tool oggSplit disjoins these streams into seperate files. This is also often called demultiplexing. </p>
<p> After that you have all embedded files of this input file with the following naming: </p>
<p> <i>theora_&lt;ID&gt;.ogv:</i> This is the video stream encoded with the theora codec. The &lt;ID&gt; is the stream ID that is created by the encoder to uniquely identify this stream. </p>
<p> <i>vorbis_&lt;ID&gt;.oga:</i> This is the audio stream encoded with the vorbis codec. The &lt;ID&gt; is the stream ID that is created by the encoder to uniquely identify this stream. </p>
<p> <i>unknown_&lt;ID&gt;.ogv:</i> This is an unknown stream, that could not be interpreted.The &lt;ID&gt; is the stream ID that is created by the encoder to uniquely identify this stream. </p>
<p> All files are fully playable with your favoured video or audio player (except the streams, that are uninterpreted). </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt; </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oggcut/">oggCut</a></code>(1), <code><a href="/docs/linux/man/1-oggcat/">oggCat</a></code>(1), <code><a href="/docs/linux/man/1-oggjoin/">oggJoin</a></code>(1), <code><a href="/docs/linux/man/1-oggresize/">oggResize</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggthumb/">oggThumb</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
