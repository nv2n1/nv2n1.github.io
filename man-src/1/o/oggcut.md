---
title: "oggcut(1)"
name: "oggcut"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggcut/"
description: "oggCut – extracts parts of an ogg file (.ogv, .ogg and .oga)"
---

<p>oggCut &#8211; extracts parts of an ogg file (.ogv, .ogg and .oga)</p>
<h2>Synopsis</h2>
<p><code>oggCut [options] inputfile outputfile</code></p>
<h2>Description</h2>
<p><code>oggCut</code> creates a new ogg file named <code>outputfile</code> as a subpart of the original file named <code>inputfile</code> </p>
<p> oggCut is able to cut video (theora) only files, audio (vorbis) only files or files with both video and audio streams. </p>
<p> The start and end time for the cut area must be given in milliseconds with the options -s and -e. </p>
<p> As a video stream consists of I-frames (which are full pictures) and P-frames (which are delta pictures to the leading I-frame) the oggCut algorithm searches for the first I-frame. If a video file would start with a p-frame, the player is not able to interpret this picture, as the leading I-frame (on where it is based) is not available. oggCut starts the I-frame search at the start time given by the -s option. So expect a shorter video time than the calculated seconds for the new file. </p>
<p> oggCut does not do any reencoding, therefore the output quality is completely the same as from the input file. </p>
<p> For those involved into the ogg container format: The file is cut on packet basis, not on page basis. </p>
<p> There is another tool called oggCut out in the internet with a different synopis. This one has not been written by the author of this tool you are actually using. </p>
<h2>Options</h2>
<dl COMPACT>
<dt>-s</p>
<dd>Cut start position in ms. If the input file is a video file, the cut area starts with the next keyframe found. Default: 0 </p>
<p> <i>Example: -s 5000 </i> </p>
<dt>-l</p>
<dd>Length of the cut area in ms. If -e is also given, the length is ignored. </p>
<p> <i>Example: -l 10000</i> </p>
<dt>-e</p>
<dd>Cut end position in ms. If -l is also used, the end position is prefered. If the end position is set to -1, the end of the stream is assumed. </p>
<p> Default: -1 </p>
<p> <i>Example: -e 20000</i> </p>
</dl>
<h2>Example</h2>
<p><i>oggCut -s 1000 -e 21000 myVideo.ogv myOutput.ogv</i> </p>
<p> Creates a new video called myOutput.ogv from the video myVideo.ogv starting after 1 second ending after 21 seconds </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt; </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oggcat/">oggCat</a></code>(1), <code><a href="/docs/linux/man/1-oggjoin/">oggJoin</a></code>(1), <code><a href="/docs/linux/man/1-oggsplit/">oggSplit</a></code>(1), <code><a href="/docs/linux/man/1-oggresize/">oggResize</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggthumb/">oggThumb</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
