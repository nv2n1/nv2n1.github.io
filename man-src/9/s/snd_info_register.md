---
title: "snd_info_register(9)"
name: "snd_info_register"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_info_register/"
---

snd_info_register - register the info entry

<h2>Synopsis</h2>

<pre><code>int snd_info_register(struct snd_info_entry *entry);</code></pre>

<h2>Arguments</h2>

<i>entry</i>
<dl><dd><dd>the info entry</dl>

<h2>Description</h2>

Registers the proc info entry.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


