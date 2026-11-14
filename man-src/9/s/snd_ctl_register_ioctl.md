---
title: "snd_ctl_register_ioctl(9)"
name: "snd_ctl_register_ioctl"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_register_ioctl/"
---

snd_ctl_register_ioctl - register the device-specific control-ioctls

<h2>Synopsis</h2>

<pre><code>int snd_ctl_register_ioctl(snd_kctl_ioctl_func_t fcn);</code></pre>

<h2>Arguments</h2>

<i>fcn</i>
<dl><dd><dd>ioctl callback function</dl>

<h2>Description</h2>

called from each device manager like pcm.c, hwdep.c, etc.

<h2>Copyright</h2>


