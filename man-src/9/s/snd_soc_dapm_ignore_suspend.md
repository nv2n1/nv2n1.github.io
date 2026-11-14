---
title: "snd_soc_dapm_ignore_suspend(9)"
name: "snd_soc_dapm_ignore_suspend"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_ignore_suspend/"
---

snd_soc_dapm_ignore_suspend - ignore suspend status for DAPM endpoint

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_ignore_suspend(struct snd_soc_dapm_context *dapm, const char *pin);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>DAPM context</dl>
 

 <i>pin</i>
<dl><dd>audio signal pin endpoint (or start point)</dl>

<h2>Description</h2>

Mark the given endpoint or pin as ignoring suspend. When the system is disabled a path between two endpoints flagged as ignoring suspend will not be disabled. The path must already be enabled via normal means at suspend time, it will not be turned on if it was not already enabled.

<h2>Copyright</h2>


