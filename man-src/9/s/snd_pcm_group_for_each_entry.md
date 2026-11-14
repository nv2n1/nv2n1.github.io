---
title: "snd_pcm_group_for_each_entry(9)"
name: "snd_pcm_group_for_each_entry"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_group_for_each_entry/"
description: "snd_pcm_group_for_each_entry – iterate over the linked substreams"
---

<p>snd_pcm_group_for_each_entry &#8211; iterate over the linked substreams</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_pcm_group_for_each_entry(</code><i>s</i><code>, </code><i>substream</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>the iterator</dl>
<p> <i>substream</i></p>
<dl>
<dd>the substream</dl>
<h2>Description</h2>
<p>Iterate over the all linked substreams to the given <i>substream</i>. When <i>substream</i> isn&#8217;t linked with any others, this gives returns <i>substream</i> itself once.</p>
<h2>Copyright</h2>
