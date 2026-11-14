---
title: "snd_soc_cnew(9)"
name: "snd_soc_cnew"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_cnew/"
---

snd_soc_cnew - create new control

<h2>Synopsis</h2>

<pre><code>struct snd_kcontrol *snd_soc_cnew(const struct snd_kcontrol_new *_template, void *data, const char *long_name, const char *prefix);</code></pre>

<h2>Arguments</h2>

<i>_template</i>
<dl><dd><dd>control template</dl>
 

 <i>data</i>
<dl><dd>control private data</dl>
 

 <i>long_name</i>
<dl><dd>control long name</dl>
 

 <i>prefix</i>
<dl><dd>control name prefix</dl>

<h2>Description</h2>

Create a new mixer control from a template control. 

 Returns 0 for success, else error.

<h2>Copyright</h2>


