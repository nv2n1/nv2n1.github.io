---
title: "streamer(1)"
name: "streamer"
section: "1"
letter: "s"
url: "/docs/linux/man/1-streamer/"
description: "streamer – record audio and/or video"
---

<h2>NAME</h2>
<p> streamer &#8211; record audio and/or video</p>
<h2>SYNOPSIS</h2>
<p> <code>streamer [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>streamer</code> reads audio and/or video data from /dev/video0 and /dev/dsp and writes the data to the disk. Various output formats are supported. Start streamer with &#8216;-h&#8217; for a list of options and supported output formats. </p>
<p> streamer will use the file extention of the output file name to figure which format to use. You need the -f/-F options only if the extention allows more than one format. If you get the &quot;neither audio nor video format specified/found&quot; message and don&#8217;t know why, you can enable the debug output (-d switch) to see what is going on. </p>
<p> You can safely stop the recording at any time with Ctrl+C. streamer will catch the signal and stop recording correctly (i.e. write movie file headers) before exiting.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>streamer -o foobar.jpeg</code></p>
<dd> write a single jpeg file.</p>
<dt><code>streamer -o quicktime.mov -f yuv2 -F stereo -r 12 -t 0:10</code></p>
<dd> record a short quicktime movie.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-v4lctl/">v4lctl</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
