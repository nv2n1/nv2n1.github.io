---
title: "snd_ctl_sync_vmaster(9)"
name: "snd_ctl_sync_vmaster"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_sync_vmaster/"
---

snd_ctl_sync_vmaster - Sync the vmaster slaves and hook

<h2>Synopsis</h2>

<pre><code>void snd_ctl_sync_vmaster(struct snd_kcontrol *kcontrol, bool hook_only);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>vmaster kctl element</dl>
 

 <i>hook_only</i>
<dl><dd>sync only the hook</dl>

<h2>Description</h2>

Forcibly call the put callback of each slave and call the hook function to synchronize with the current value of the given vmaster element. NOP when NULL is passed to <i>kcontrol</i>.

<h2>Copyright</h2>


