---
title: "snd_ac97_resume(9)"
name: "snd_ac97_resume"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_resume/"
---

snd_ac97_resume - General resume function for AC97 codec

<h2>Synopsis</h2>

<pre><code>void snd_ac97_resume(struct snd_ac97 *ac97);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>

<h2>Description</h2>

Do the standard resume procedure, power up and restoring the old register values.

<h2>Copyright</h2>


