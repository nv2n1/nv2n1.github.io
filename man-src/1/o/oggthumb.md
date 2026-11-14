---
title: "oggthumb(1)"
name: "oggthumb"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggthumb/"
description: "oggThumb – creates thumbnails from an ogg video file"
---

<p>oggThumb &#8211; creates thumbnails from an ogg video file</p>
<h2>Synopsis</h2>
<p><code>oggThumb [options] file1.ogv [ file2.ogv [ file3.ogv [&#8230;] ] ] </code></p>
<h2>Description</h2>
<p><code>oggThumb</code> creates Thumbnails from one or more ogg video files, at a given time position or a given frame number. It is also possible to create a series of thumbnails at different time or frame positions. The pictures can be created in JPG or PNG format and can be resized to any given size. </p>
<p> The naming of each thumbnail series follows the following rule: </p>
<p> <i>&lt;filename_without_extension&gt;_x.&lt;picture_extension&gt;</i> </p>
<p> Where x starts with 0 and is incremented with every created thumbnail. So the thumbnails are successivly numbered by the appearence order. This is even valid, if time positions and frame numbers are mixed.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-t</p>
<dd>Time at which a thumbnail should be created. More than one thumbnail time can be concatenated by komas. The times can be set by integer or floating point values in seconds. If the time is not exactly matching, the next frame is used. The times don&#8217;t have to be sorted incrementally. </p>
<p> <i>Example: -t 12.4,14.157,13.23</i> </p>
<dt>-f</p>
<dd>Number of a frame that should be created as a thumbnail. More than one thumbnail frame can be concatenated by komas. The frame numbers must be an integers. The frame numbers don&#8217;t have to be sorted incrementally. </p>
<p> <i>Example: -f 12000,13000,11000</i> </p>
<dt>-s</p>
<dd>Picture output size. The thumbnail is created in the size given as &lt;width&gt;x&lt;height&gt;. If you want to include the thumbnails into your webpage and you need to have a fixed width but dynamic height, you can set the dynamic axis to 0. So the aspect ratio of the video frame is kept. This is the same for setting width or height to 0. </p>
<p> <i>Example: -s 0x100 </i> </p>
<dt>-o</p>
<dd>Output format. This can be png or jpg. The default is jpg. </p>
<p> <i>Example: -o png</i></dl>
<h2>Example</h2>
<p><i>oggThumb -t 10.3,22.4,31.9,43.4,59.4 -f 1200 -s 0x100 myFile.ogv</i> </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oggcut/">oggCut</a></code>(1), <code><a href="/docs/linux/man/1-oggcat/">oggCat</a></code>(1), <code><a href="/docs/linux/man/1-oggjoin/">oggJoin</a></code>(1), <code><a href="/docs/linux/man/1-oggsplit/">oggSplit</a></code>(1), <code><a href="/docs/linux/man/1-oggresize/">oggResize</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
