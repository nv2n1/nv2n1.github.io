---
title: "snd_jack_add_new_kctl(9)"
name: "snd_jack_add_new_kctl"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_jack_add_new_kctl/"
---

snd_jack_add_new_kctl - Create a new snd_jack_kctl and add it to jack

<h2>Synopsis</h2>

<pre><code>int snd_jack_add_new_kctl(struct snd_jack *jack, const char *name, int mask);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>the jack instance which the kctl will attaching to</dl>
 

 <i>name</i>
<dl><dd>the name for the snd_kcontrol object</dl>
 

 <i>mask</i>
<dl><dd>a bitmask of enum snd_jack_type values that can be detected by this snd_jack_kctl object.</dl>

<h2>Description</h2>

Creates a new snd_kcontrol object and adds it to the jack kctl_list.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


