---
title: "aaxine(1)"
name: "aaxine"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aaxine/"
description: "aaxine – an ASCII art video player"
---

<h2 class="name">NAME</h2>
<p> aaxine &#8211; an ASCII art video player</p>
<h2>SYNOPSIS</h2>
<p> <code>aaxine </code> [<i>aalib-options</i>] [<i>-A</i>&lt;audio-driver&gt;] [<i>-a</i>&lt;audio-channel&gt;] [<i>-R</i>&lt;rec-by&gt;] [<i>MRL</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> This manual page explains the <code>aaxine</code> program. Aaxine, is an aalib based frontend for libxine, a versatile video/multimedia player. </p>
<p> <code>aaxine</code> is for those who don&#8217;t have a high end video card, but just want to watch DVDs on their good old vt100 ;-) </p>
<p> Like xine, <code>aaxine</code> plays MPEG system (audio and video) streams, mpeg elementary streams (e.g. .mp3 or .mpv files), avi files (using win32 codecs or ffmpeg), (S)VCDs, DVDs and many more. In short, anything that&#8217;s supported by xine-lib. </p>
<h2>OPTIONS</h2>
<p> The program follows usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options are included below. For a complete description, see <i>README</i> and <i>FAQ</i> in <i>/usr/share/doc/xine-ui-0.99.9</i> or on the xine home page.</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options and available output drivers (plugins).</dd></dl>
<p> A big bunch of these options is provided by aalib. Please refer to your aalib documentation for those! </p>
<p> The remaining options, labelled <code>AAXINE options:</code> when listed with &quot;<i>aaxine &#8211;help</i>&quot;, are explained here.</p>
<dl>
<dt><code>-A, &#8211;audio-driver&nbsp;<wbr></code><i>&lt;drv&gt;</i></dt>
<dd> Use given audio driver. Available drivers can be listed with &quot;aaxine &#8211;help&quot;</dd>
<dt><code>-a, &#8211;audio-channel&nbsp;<wbr></code><i>&lt;num&gt;</i></dt>
<dd> Use given audio channel. Channels are sequentially numbered from 0 for first audio track.</dd>
<dt><code>-R, &#8211;recognize-by&nbsp;<wbr></code><i>[option]</i></dt>
<dd> Determine the method used to recognize stream type. Possible options are:<br />
 `<code>default</code>&#8216;: by content, then by extension,<br />
 `<code>revert</code>&#8216;: by extension, then by content,<br />
 `<code>content</code>&#8216;: only by content,<br />
 `<code>extension</code>&#8216;: only by extension.<br />
 If <code>-R</code> is given without an additional option, `<code>revert</code>&#8216; is selected. </dd>
</dl>
<h2>MRLs</h2>
<p> MRLs are similar to URLs in your web browser. They describe the media to read from. valid MRLs may be plain file names or one of the following:<br />
 <code>file:</code><i>&lt;path&gt;</i><br />
 <code>fifo:</code><i>&lt;path&gt;</i><br />
 <code>stdin:/</code><br />
 <code>dvd:/</code><i>&lt;title&gt;</i><code>.</code><i>&lt;part&gt;</i><br />
 <code>vcd:/</code><i>&lt;tracknumber&gt;</i><br />
 <code>tcp://</code><i>&lt;host&gt;</i><code>:</code><i>&lt;port&gt;</i><br />
 <code>rtp://</code><i>&lt;host&gt;</i><code>:</code><i>&lt;port&gt;</i><br />
 <code>udp://</code><i>&lt;host&gt;</i><code>:</code><i>&lt;port&gt;</i><br />
 <code>mms://</code><i>&lt;host&gt;&#8230;</i><br />
 <code>http://</code><i>&lt;host&gt;&#8230;</i><br />
 <code>cdda://</code><i>&lt;tracknumber&gt;</i> </p>
<p> Several MRLs may be specified in order to play a number of consecutive streams. Additional input plugins will provide additional MRL types. The ones listed above are available with stock libxine&#8230;<br />
 After a delimiting <code>#</code> you can add several stream parameters:</p>
<dl>
<dt><code>novideo</code></dt>
<dd> video will be ignored</dd>
<dt><code>noaudio</code></dt>
<dd> audio will be ignored</dd>
<dt><code>nospu</code></dt>
<dd> subpictures will be ignored</dd>
<dt><code>demux:</code><i>&lt;demux name&gt;</i></dt>
<dd> specify the demux plugin to use</dd>
<dt><code>volume:</code><i>&lt;level&gt;</i></dt>
<dd> set audio volume</dd>
<dt><code>compression:</code><i>&lt;level&gt;</i></dt>
<dd> set audio dynamic range compression</dd>
<dt><i>&lt;config entry&gt;</i><code>:</code><i>&lt;config value&gt;</i></dt>
<dd> assign a new value to any config entry </dd>
</dl>
<h2>CONTROL KEYS</h2>
<p> Many features can be controlled by pressing control keys. The Key bindings are:</p>
<dl>
<dt><code>&lt;RETURN&gt;</code> / <code>R</code></dt>
<dd> Play</dd>
<dt><code>&lt;SPACE&gt;</code> / <code>P</code></dt>
<dd> Pause</dd>
<dt><code>0</code></dt>
<dd> Jump to start of current stream</dd>
<dt><code>1</code> .. <code>9</code></dt>
<dd> Jump to 10%..90% of current stream</dd>
<dt><code>&lt;PgUp&gt;</code></dt>
<dd> Jump to previous stream in playlist</dd>
<dt><code>&lt;PgDown&gt;</code></dt>
<dd> Jump to next stream in playlist</dd>
<dt><code>+</code></dt>
<dd> Select next audio channel (may take up to a few seconds to take effect)</dd>
<dt><code>&#8211;</code></dt>
<dd> Select prev audio channel</dd>
<dt><code>Q</code></dt>
<dd> Exit. </dd>
</dl>
<h2>BUGS</h2>
<p> none, of course ;-) Well, there are surely a few of those. You can probably best ask for support (and report bugs) on our mailing list at &lt;xine-user [at] lists.sf.net&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xine/">xine</a></code>(1), <code><a rel="nofollow" href="http://www.xine-project.org/,">http://www.xine-project.org/,</a></code> <code><a rel="nofollow" href="http://aa-project.sf.net/aalib,">http://aa-project.sf.net/aalib,</a></code> <code>xine-lib</code>(3) </p>
<h2>AUTHOR</h2>
<p> Siggi Langauf for the xine project. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 The xine project </p>
<h2>Index</h2>
