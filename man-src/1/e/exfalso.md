---
title: "exfalso(1)"
name: "exfalso"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exfalso/"
description: "exfalso – audio tag editor"
---

<h2>NAME</h2>
<p> exfalso &#8211; audio tag editor</p>
<h2>SYNOPSIS</h2>
<p> <code>exfalso</code> [ <i>directory</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Ex Falso displays and edits audio metadata tags. Supported formats include MP3, Ogg Vorbis, FLAC, Musepack (MPC), WavPack, and MOD/XM/IT. </p>
<p> This manual page is only a short reference for Ex Falso. Complete documentation is available at <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide">http://code.google.com/p/quodlibet/wiki/Guide</a></i>.</p>
<h2>OPTIONS</h2>
<p> Ex Falso may be given a directory to open on the command line.</p>
<h2>TIED TAGS</h2>
<p> Many places in Ex Falso allow you to use &quot;tied tags&quot;. Tied tags are two tag names joined together with a &quot;~&quot; like &quot;title~version&quot; or &quot;album~part&quot;. Tied tags result in &quot;nice&quot; displays even when one of the tags is missing; for example, &quot;title~version&quot; will result in Title &#8211; Version when a version tag is present, but only Title when one isn&#8217;t. You can tie any number of tags together.</p>
<h2>RENAMING FILES</h2>
<p> Ex Falso allows you to rename files based on their tags. In some cases you may wish to alter the filename depending on whether some tags are present or missing, in addition to their values. A common pattern might be </p>
<p> <code>&lt;tracknumber&gt;. &lt;title~version&gt;</code> </p>
<p> You can use a &#8216;|&#8217; to only text when a tag is present: </p>
<p> <code>&lt;tracknumber|&lt;tracknumber&gt;. &gt;&lt;title~version&gt;</code> </p>
<p> You can also specify literal text to use if the tag is missing by adding another &#8216;|&#8217;: </p>
<p> <code>&lt;album|&lt;album&gt;|No Album&gt; &#8211; &lt;title&gt;</code> </p>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide_Renaming">http://code.google.com/p/quodlibet/wiki/Guide_Renaming</a></i>.</p>
<h2>BUGS</h2>
<p> See <i><a rel="nofollow" href="http://code.google.com/p/quodlibet/issues/list">http://code.google.com/p/quodlibet/issues/list</a></i> for a list of all currently open bugs and feature requests.</p>
<h2>AUTHORS</h2>
<p> Joe Wreschnig and Michael Urman are the primary authors of Ex Falso.</p>
<h2>SEE ALSO</h2>
<pre>
<i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/Guide">http://code.google.com/p/quodlibet/wiki/Guide</a></i>,
<i><a rel="nofollow" href="http://code.google.com/p/quodlibet/wiki/FAQ">http://code.google.com/p/quodlibet/wiki/FAQ</a></i>
</pre>
<h2>Index</h2>
