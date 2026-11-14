---
title: "snd_soc_jack_report(9)"
name: "snd_soc_jack_report"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_report/"
description: "snd_soc_jack_report – Report the current status for a jack"
---

<p>snd_soc_jack_report &#8211; Report the current status for a jack</p>
<h2>Synopsis</h2>
<pre><code>void snd_soc_jack_report(struct snd_soc_jack *jack, int status, int mask);</code></pre>
<h2>Arguments</h2>
<p><i>jack</i></p>
<dl>
<dd>
<dd>the jack</dl>
<p> <i>status</i></p>
<dl>
<dd>a bitmask of enum snd_jack_type values that are currently detected.</dl>
<p> <i>mask</i></p>
<dl>
<dd>a bitmask of enum snd_jack_type values that being reported.</dl>
<h2>Description</h2>
<p>If configured using <code>snd_soc_jack_add_pins</code> then the associated DAPM pins will be enabled or disabled as appropriate and DAPM synchronised.</p>
<h2>Note</h2>
<p>This function uses mutexes and should be called from a context which can sleep (such as a workqueue).</p>
<h2>Copyright</h2>
