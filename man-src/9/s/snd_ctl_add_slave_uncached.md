---
title: "snd_ctl_add_slave_uncached(9)"
name: "snd_ctl_add_slave_uncached"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_add_slave_uncached/"
description: "snd_ctl_add_slave_uncached – Add a virtual slave control"
---

<p>snd_ctl_add_slave_uncached &#8211; Add a virtual slave control</p>
<h2>Synopsis</h2>
<pre><code>int snd_ctl_add_slave_uncached(struct snd_kcontrol *master, struct snd_kcontrol *slave);</code></pre>
<h2>Arguments</h2>
<p><i>master</i></p>
<dl>
<dd>
<dd>vmaster element</dl>
<p> <i>slave</i></p>
<dl>
<dd>slave element to add</dl>
<h2>Description</h2>
<p>Add a virtual slave control to the given master. Unlike <code>snd_ctl_add_slave</code>, the element added via this function is supposed to have volatile values, and get callback is called at each time queried from the master. </p>
<p> When the control peeks the hardware values directly and the value can be changed by other means than the put callback of the element, this function should be used to keep the value always up-to-date.</p>
<h2>Return</h2>
<p>Zero if successful or a negative error code.</p>
<h2>Copyright</h2>
