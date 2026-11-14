---
title: "snd_ctl_free_one(9)"
name: "snd_ctl_free_one"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_free_one/"
description: "snd_ctl_free_one – release the control instance"
---

<p>snd_ctl_free_one &#8211; release the control instance</p>
<h2>Synopsis</h2>
<pre><code>void snd_ctl_free_one(struct snd_kcontrol *kcontrol);</code></pre>
<h2>Arguments</h2>
<p><i>kcontrol</i></p>
<dl>
<dd>
<dd>the control instance</dl>
<h2>Description</h2>
<p>Releases the control instance created via <code>snd_ctl_new</code> or <code>snd_ctl_new1</code>. Don&#8217;t call this after the control was added to the card.</p>
<h2>Copyright</h2>
