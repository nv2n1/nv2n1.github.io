---
title: "snd_ac97_write(9)"
name: "snd_ac97_write"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_write/"
description: "snd_ac97_write – write a value on the given register"
---

<p>snd_ac97_write &#8211; write a value on the given register</p>
<h2>Synopsis</h2>
<pre><code>void snd_ac97_write(struct snd_ac97 *ac97, unsigned short reg, unsigned short value);</code></pre>
<h2>Arguments</h2>
<p><i>ac97</i></p>
<dl>
<dd>
<dd>the ac97 instance</dl>
<p> <i>reg</i></p>
<dl>
<dd>the register to change</dl>
<p> <i>value</i></p>
<dl>
<dd>the value to set</dl>
<h2>Description</h2>
<p>Writes a value on the given register. This will invoke the write callback directly after the register check. This function doesn&#8217;t change the register cache unlike #<code>snd_ca97_write_cache</code>, so use this only when you don&#8217;t want to reflect the change to the suspend/resume state.</p>
<h2>Copyright</h2>
