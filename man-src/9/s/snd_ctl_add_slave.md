---
title: "snd_ctl_add_slave(9)"
name: "snd_ctl_add_slave"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_add_slave/"
description: "snd_ctl_add_slave – Add a virtual slave control"
---

<p>snd_ctl_add_slave &#8211; Add a virtual slave control</p>
<h2>Synopsis</h2>
<pre><code>int snd_ctl_add_slave(struct snd_kcontrol *master, struct snd_kcontrol *slave);</code></pre>
<h2>Arguments</h2>
<p><i>master</i></p>
<dl>
<dd>
<dd>vmaster element</dl>
<p> <i>slave</i></p>
<dl>
<dd>slave element to add</dl>
<h2>Description</h2>
<p>Add a virtual slave control to the given master element created via <code>snd_ctl_create_virtual_master</code> beforehand. </p>
<p> All slaves must be the same type (returning the same information via info callback). The function doesn&#8217;t check it, so it&#8217;s your responsibility. </p>
<p> Also, some additional limitations: at most two channels, logarithmic volume control (dB level) thus no linear volume, master can only attenuate the volume without gain</p>
<h2>Return</h2>
<p>Zero if successful or a negative error code.</p>
<h2>Copyright</h2>
