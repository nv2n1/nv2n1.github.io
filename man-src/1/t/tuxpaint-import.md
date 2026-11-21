---

title: "tuxpaint-import(1)"
name: "tuxpaint-import"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tuxpaint-import/"
description: "tuxpaint-import — Import image files into Tux Paint(1)"
---

<p> tuxpaint-import &#8212; Import image files into Tux Paint(1) </p>
<h2>SYNOPSYS</h2>
<dl>
<dt><code>tuxpaint-import [&#8211;help]</code></dt>
<dd>
</dd><dt><code>tuxpaint-import </code><i>filename(s)</i></dt>
<dd>
</dd></dl>
<h2>DESCRIPTION</h2>
<p> <i>tuxpaint-import</i> is a simple shell script which uses some <i>NetPBM</i> (<a href="/docs/linux/man/5-pnm/">pnm</a>(5)) tools (<i>anytopnm</i>, <i>pnmscale</i> and <i>pnmtopng</i>) along with <i><a href="/docs/linux/man/1-date/">date</a></i>(1) to convert an arbitrary image file (e.g., a JPEG, GIF, etc.) into a <i><a href="/docs/linux/man/5-png/">PNG</a></i>(5) file which can be used by the drawing program <i>Tux Paint</i> (<a href="/docs/linux/man/1-tuxpaint/">tuxpaint</a>(1)) and places it in the user&#8217;s Tux Paint saved-files directory (<i>$HOME/.tuxpaint/saved/</i>). </p>
<h2>EXAMPLE</h2>
<p> tuxpaint-import picture.jpg photo.png cartoon.gif </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>$HOME</code></dt>
<dd> to determine where the files should go so that they can be access within <i>Tux Paint</i> using its <i>Open</i> command. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.tuxpaint/saved</code></dt>
<dd> where new image files are stored, after being resized and converted into PNG format. </dd>
<dt><code>$HOME/.tuxpaint/saved/.thumbs</code></dt>
<dd> where thumbnail images are stored. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Bill Kendrick. &lt;bill [at] newbreedsoftware.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tuxpaint/">tuxpaint</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/5-png/">png</a></code>(5), <code><a href="/docs/linux/man/1-anytopnm/">anytopnm</a></code>(1), <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1), <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1), <code><a href="/docs/linux/man/1-date/">date</a></code>(1), </p>
<p> And documentation within /usr/[local/]share/doc/tuxpaint/. </p>
