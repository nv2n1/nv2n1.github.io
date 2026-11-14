---
title: "quodlibet(1)"
name: "quodlibet"
section: "1"
letter: "q"
url: "/docs/linux/man/1-quodlibet/"
description: "quodlibet – audio library manager and player"
---

<h2>NAME</h2>
<p> quodlibet &#8211; audio library manager and player</p>
<h2>SYNOPSIS</h2>
<pre><code>
quodlibet[--print - playing | control] exfalso[directory]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Quod Libet is a music management program. It provides several different ways to view your audio library, as well as support for Internet radio and audio feeds. It has extremely flexible metadata tag editing and searching capabilities. </p>
<p> This manual page is only a short reference for Quod Libet. Complete documentation is available at <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide">http://code.google.com/p/quodlibet/wiki/Guide</a></i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;enqueue filename|query</code></p>
<dd> Enqueue a filename or query results</p>
<dt><code>&#8211;filter tag=value</code></p>
<dd> Filter on a tag value</p>
<dt><code>&#8211;focus</code></p>
<dd> Focus the running player</p>
<dt><code>&#8211;hide-window</code></p>
<dd> Hide main window</p>
<dt><code>&#8211;next</code></p>
<dd> Jump to next song</p>
<dt><code>&#8211;list-browsers</code></p>
<dd> List available browsers</p>
<dt><code>&#8211;open-browser=</code><i>BrowserName</i></p>
<dd> Open a new browser</p>
<dt><code>&#8211;order=inorder|shuffle|weighted|onesong|toggle</code></p>
<dd> Set or toggle the playback order</p>
<dt><code>&#8211;pause</code></p>
<dd> Pause playback</p>
<dt><code>&#8211;play</code></p>
<dd> Start playback</p>
<dt><code>&#8211;play-file=</code><i>filename</i></p>
<dd> Play a file</p>
<dt><code>&#8211;play-pause</code></p>
<dd> Toggle play/pause mode</p>
<dt><code>&#8211;previous</code></p>
<dd> Jump to previous song or restart if near the beginning</p>
<dt><code>&#8211;force-previous</code></p>
<dd> Jump to previous song</p>
<dt><code>&#8211;print-playlist</code></p>
<dd> Print the current playlist</p>
<dt><code>&#8211;print-queue</code></p>
<dd> Print the contents of the queue</p>
<dt><code>&#8211;print-playing</code></p>
<dd> Print out information about the currently playing song. You may provide in a string like the kind described in the RENAMING FILES section below.</p>
<dt><code>&#8211;query=</code><i>search-string</i></p>
<dd> Search your audio library</p>
<dt><code>&#8211;quit</code></p>
<dd> Exit Quod Libet</p>
<dt><code>&#8211;random=</code><i>tag</i></p>
<dd> Filter on a random value</p>
<dt><code>&#8211;repeat=off|on|t</code></p>
<dd> Turn repeat off, on, or toggle</p>
<dt><code>&#8211;seek=[+|-][HH:]MM:SS</code></p>
<dd> Seek within the playing song</p>
<dt><code>&#8211;set-browser=</code><i>BrowserName</i></p>
<dd> Set the current browser</p>
<dt><code>&#8211;set-rating=0.0..1.0</code></p>
<dd> Rate the playing song</p>
<dt><code>&#8211;show-window</code></p>
<dd> Hide main window</p>
<dt><code>&#8211;start-playing</code></p>
<dd> Begin playing immediately</p>
<dt><code>&#8211;status</code></p>
<dd> Print playing status</p>
<dt><code>&#8211;toggle-window</code></p>
<dd> Toggle main window visibility</p>
<dt><code>&#8211;unfilter</code></p>
<dd> Remove active browser filters</p>
<dt><code>&#8211;unqueue=filename|query</code></p>
<dd> Unqueue a file or query</p>
<dt><code>&#8211;volume=(+|-|)0..100</code></p>
<dd> Set the volume</dl>
<h2>ALBUM COVERS</h2>
<p> Album covers should be put in the same directory as the songs they apply to, and have &quot;folder&quot;, &quot;front&quot;, or &quot;cover&quot; in their filenames. If you want to store multiple albums in the same directory but keep distinct cover images, the name of the appropriate image file must contain the labelid tag value, e.g. COCX-32760 cover.jpg.</p>
<h2>TIED TAGS</h2>
<p> Many places in Quod Libet allow you to use &quot;tied tags&quot;. Tied tags are two tag names joined together with a &quot;~&quot; like &quot;title~version&quot; or &quot;album~part&quot;. Tied tags result in &quot;nice&quot; displays even when one of the tags is missing; for example, &quot;title~version&quot; will result in Title &#8211; Version when a version tag is present, but only Title when one isn&#8217;t. You can tie any number of tags together.</p>
<h2>SEARCH SYNTAX</h2>
<p> All of Quod Libet&#8217;s search boxes support advanced searches of the following forms: </p>
<pre>
tag = value
tag = !value
tag = &quot;value&quot;
tag = /value/
tag = &amp;(value1, value2)
tag = |(value1, value2)
!tag = value
|(tag1 = value1, tag2 = value2)
&amp;(tag1 = value1, tag2 = value2)
#(numerictag &lt; value)
#(numerictag = value)
#(numerictag &gt; value)
</pre>
<p> The &#8216;c&#8217; postfix on strings or regular expressions makes the search case-sensitive. Numeric values may be given as integers, floating-point numbers, MM:SS format, or simple English, e.g. &quot;3 days&quot;, &quot;2 hours&quot;. </p>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_Searching">http://code.google.com/p/quodlibet/wiki/Guide_Searching</a></i>. </p>
<p> All internal tags begin with a ~ character. Non-numeric internal tags are ~base‐ name, ~dirname, ~filename, ~format, ~length, ~people, and ~rating. Numeric internal tags are ~#added, ~#bitrate, ~#disc, ~#lastplayed, ~#laststarted, ~#length, ~#mtime, ~#playcount, ~#skipcount, and ~#track. </p>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_InternalTags">http://code.google.com/p/quodlibet/wiki/Guide_InternalTags</a></i>.</p>
<h2>RENAMING FILES</h2>
<p> Quod Libet allows you to rename files based on their tags. In some cases you may wish to alter the filename depending on whether some tags are present or missing, in addition to their values. A common pattern might be </p>
<p> <code>&lt;tracknumber&gt;. &lt;title~version&gt;</code> </p>
<p> You can use a &#8216;|&#8217; to only text when a tag is present: </p>
<p> <code>&lt;tracknumber|&lt;tracknumber&gt;. &gt;&lt;title~version&gt;</code> </p>
<p> You can also specify literal text to use if the tag is missing by adding another &#8216;|&#8217;: </p>
<p> <code>&lt;album|&lt;album&gt;|No Album&gt; &#8211; &lt;title&gt;</code> </p>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_Renaming">http://code.google.com/p/quodlibet/wiki/Guide_Renaming</a></i>.</p>
<h2>AUDIO BACKENDS</h2>
<p> Quod Libet uses GStreamer for audio playback. It tries to read your GConf GStreamer configuration, but if that fails it falls back to osssink. You can change the pipeline option in ~/.quodlibet/config to use a different sink, or pass options to the sink. For example, you might use esdsink or alsasink device=hw:1. </p>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_AudioBackends">http://code.google.com/p/quodlibet/wiki/Guide_AudioBackends</a></i>.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.quodlibet/songs</code></p>
<dd> A pickled Python dict of cached metadata. Deleting this file will remove all songs from your library.</p>
<dt><code>~/.quodlibet/config</code></p>
<dd> Quod Libet&#8217;s configuration file. This file is overwritten when Quod Libet exits.</p>
<dt><code>~/.quodlibet/current</code></p>
<dd> A &quot;key=value&quot; file containing information about the currently playing song.</p>
<dt><code>~/.quodlibet/control</code></p>
<dd> A FIFO connected to the most-recently-started instance of the program. &#8211;next, &#8211;previous, etc., use this to control the player.</p>
<dt><code>~/.quodlibet/plugins/</code></p>
<dd> Put plugins (from <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_Plugins">http://code.google.com/p/quodlibet/wiki/Guide_Plugins</a></i>) here.</p>
<dt><code>~/.quodlibet/browsers/</code></p>
<dd> Put custom library browsers here. </p>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_Extending">http://code.google.com/p/quodlibet/wiki/Guide_Extending</a></i>.</dl>
<h2>BUGS</h2>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/issues/list">http://code.google.com/p/quodlibet/issues/list</a></i> for a list of all currently open bugs and feature requests.</p>
<h2>AUTHORS</h2>
<p> Joe Wreschnig and Michael Urman are the primary authors of Quod Libet.</p>
<h2>SEE ALSO</h2>
<pre>
<i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide">http://code.google.com/p/quodlibet/wiki/Guide</a></i>,
<i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/FAQ">http://code.google.com/p/quodlibet/wiki/FAQ</a></i>,
<code><a href="//www.systutorials.com/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="//www.systutorials.com/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1)
</pre>
<h2>Index</h2>
