---

title: "dc1394_multiview(1)"
name: "dc1394_multiview"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc1394_multiview/"
description: "dc1394_multiview – display format0 camera video"
---

<h2>NAME</h2>
<p> dc1394_multiview &#8211; display format0 camera video</p>
<p> <code>dc1394_multiview [</code><i>&#8211;fps=[1,3,15,30]</i>] [<i>&#8211;res=[0,1,2]</i>] [<i>&#8211;device=/dev/video1394/x</i>]</p>
<p> View format0-only camera video from one or more cameras.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;fps</code></dt>
<dd> frames per second. default is 7. The 30 fps setting is incompatible with the 640&#215;480 RGB8 resolution setting.</dd>
<dt><code>&#8211;res</code></dt>
<dd> resolution. 0 is 320&#215;240 (default), 1 = 640&#215;480 YUV4:1:1, 2 = 640&#215;480 RGB8</dd>
<dt><code>&#8211;device</code></dt>
<dd> specifies video1394 device to use (optional). default is /dev/video1394/&lt;port#&gt;</dd>
<dt><code>&#8211;help</code></dt>
<dd> print help message</dd></dl>
<h2>KEYBOARD CONTROLS</h2>
<dl>
<dt><code>q</code></dt>
<dd> quit</dd>
<dt><code>&lt; or ,</code></dt>
<dd> scale -50%</dd>
<dt><code>&gt; or .</code></dt>
<dd> scale +50%</dd>
<dt><code>0</code></dt>
<dd> pause</dd>
<dt><code>1</code></dt>
<dd> set framerate to 1.875 fps</dd>
<dt><code>2</code></dt>
<dd> set framerate to 3.75 fps</dd>
<dt><code>3</code></dt>
<dd> set framerate to 7.5 fps</dd>
<dt><code>4</code></dt>
<dd> set framerate to 15 fps</dd>
<dt><code>5</code></dt>
<dd> set framerate to 30 fps</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Peter De Schrijver &lt;p2 [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others) and added to upstream by Peter Antoniac &lt;theseinfeld [at] users.sf.net&gt;. </p>
