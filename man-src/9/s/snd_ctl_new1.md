---
title: "snd_ctl_new1(9)"
name: "snd_ctl_new1"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_new1/"
description: "snd_ctl_new1 – create a control instance from the template"
---

<p>snd_ctl_new1 &#8211; create a control instance from the template</p>
<h2>Synopsis</h2>
<pre><code>struct snd_kcontrol *snd_ctl_new1(const struct snd_kcontrol_new *ncontrol, void *private_data);</code></pre>
<h2>Arguments</h2>
<p><i>ncontrol</i></p>
<dl>
<dd>
<dd>the initialization record</dl>
<p> <i>private_data</i></p>
<dl>
<dd>the private data to set</dl>
<h2>Description</h2>
<p>Allocates a new struct snd_kcontrol instance and initialize from the given template. When the access field of ncontrol is 0, it&#8217;s assumed as READWRITE access. When the count field is 0, it&#8217;s assumes as one.</p>
<h2>Return</h2>
<p>The pointer of the newly generated instance, or <code>NULL</code> on failure.</p>
<h2>Copyright</h2>
