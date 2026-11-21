---

title: "cacaview(1)"
name: "cacaview"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cacaview/"
description: "cacaview – ASCII image browser"
---

<h2>NAME</h2>
<p> cacaview &#8211; ASCII image browser</p>
<p> <code>cacaview [FILE&#8230;]</code></p>
<p> <code>cacaview</code> is a lightweight text mode image viewer. It renders images using colour ASCII characters. It is a powerful add-on to famous console programs such as the mutt email client, the slrn newsreader and the links or w3m web browsers. </p>
<p> <code>cacaview</code> can load the most widespread image formats: PNG, JPEG, GIF, PNG, BMP etc. </p>
<p> You can zoom and scroll the image around for more details, and choose four different dithering modes. All commands are accessible through a single key press.</p>
<h2>KEYS</h2>
<dl>
<dt><code>?</code></dt>
<dd> show the help screen</dd>
<dt><code>n, p</code></dt>
<dd> switch to next image, previous image</dd>
<dt><code>Left, Right, Up, Down or h, l, k, j</code></dt>
<dd> scroll the image around</dd>
<dt><code>+, &#8211;</code></dt>
<dd> zoom in and out</dd>
<dt><code>z</code></dt>
<dd> reset the zoom level to normal</dd>
<dt><code>f</code></dt>
<dd> switch fullscreen mode (hide/show menu and status bars)</dd>
<dt><code>d</code></dt>
<dd> toggle the dithering mode (no dithering, 4&#215;4 ordered dithering, 8&#215;8 ordered dithering and random dithering)</dd>
<dt><code>q</code></dt>
<dd> exit the program</dd></dl>
<h2>EXAMPLE</h2>
<p> cacaview /usr/share/pixmaps/*.*</p>
<h2>BUGS</h2>
<p> There is no support for aspect ratio yet. Also, since there is no way yet to load an image from <code>cacaview</code> it is completely useless when run without an argument.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-img2txt/">img2txt</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sam Hocevar &lt;sam [at] hocevar.net&gt;. </p>
