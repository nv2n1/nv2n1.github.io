---

title: "kdenlive_render(1)"
name: "kdenlive_render"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdenlive_render/"
description: "kdenlive_render – Render program for Kdenlive."
---

<h2>NAME</h2>
<p> kdenlive_render &#8211; Render program for Kdenlive.</p>
<p> kdenlive_render [-erase] [in=pos] [out=pos] [render] [profile] [rendermodule] [player] [src] [dest] [[arg1] [arg2] &#8230;]</p>
<p> Render program for Kdenlive. Renders kdenlive project detached from Kdenlive, while providing feedback through kuiserver. This program is not meant to be called directly by users, but is called from Kdenlive, when a rendering process is started.</p>
<h2>OPTIONS</h2>
<h3>
<h3>Options:</h3>
</h3>
<dl>
<dt><code>-erase</code></dt>
<dd> If present, src file will be erased after rendering</dd>
<dt><code>in=pos</code></dt>
<dd> Start rendering at frame pos</dd>
<dt><code>out=pos</code></dt>
<dd> End rendering at frame pos</dd>
<dt><code>render</code></dt>
<dd> Path to MLT melt render program</dd>
<dt><code>profile</code></dt>
<dd> The MLT video profile</dd>
<dt><code>rendermodule</code></dt>
<dd> The MLT consumer used for rendering, usually it is avformat</dd>
<dt><code>player</code></dt>
<dd> Path to video player to play when rendering is over, use &#8216;-&#8216; to disable playing</dd>
<dt><code>src</code></dt>
<dd> Source file &#8211; usually MLT playlist</dd>
<dt><code>dest</code></dt>
<dd> Destination file</dd>
<dt><code>args</code></dt>
<dd> Space separated libavformat arguments</dd></dl>
<h3></h3>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>KDENLIVE_RENDER_LOG</code></dt>
<dd> If $<code>KDENLIVE_RENDER_LOG</code> is set, a log will be written to /tmp/kdenlive_render.log.XXXXXXXX, that contains information about the result of calling melt, ffmpeg, etc. This can be used for debugging. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> Please see the homepage at <code><a rel="nofollow" href="http://www.kdenlive.org/">http://www.kdenlive.org/</a></code> </p>
<h2>AUTHORS</h2>
<pre><code>
Jean - Baptiste Mardelle&lt;jb[at] kdenlive.org&gt;
           Marco Gittler&lt;g.marco[at] freenet.de&gt;
</code></pre>
