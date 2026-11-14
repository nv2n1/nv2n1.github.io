---
title: "snd_pcm_trigger_done(9)"
name: "snd_pcm_trigger_done"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_trigger_done/"
description: "snd_pcm_trigger_done – Mark the master substream"
---

<p>snd_pcm_trigger_done &#8211; Mark the master substream</p>
<h2>Synopsis</h2>
<pre><code>void snd_pcm_trigger_done(struct snd_pcm_substream *substream, struct snd_pcm_substream *master);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the pcm substream instance</dl>
<p> <i>master</i></p>
<dl>
<dd>the linked master substream</dl>
<h2>Description</h2>
<p>When multiple substreams of the same card are linked and the hardware supports the single-shot operation, the driver calls this in the loop in <code>snd_pcm_group_for_each_entry</code> for marking the substream as &#8220;done&#8221;. Then most of trigger operations are performed only to the given master substream. </p>
<p> The trigger_master mark is cleared at timestamp updates at the end of trigger operations.</p>
<h2>Copyright</h2>
