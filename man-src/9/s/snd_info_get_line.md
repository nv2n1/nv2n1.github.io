---
title: "snd_info_get_line(9)"
name: "snd_info_get_line"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_info_get_line/"
---

snd_info_get_line - read one line from the procfs buffer

<h2>Synopsis</h2>

<pre><code>int snd_info_get_line(struct snd_info_buffer *buffer, char *line, int len);</code></pre>

<h2>Arguments</h2>

<i>buffer</i>
<dl><dd><dd>the procfs buffer</dl>
 

 <i>line</i>
<dl><dd>the buffer to store</dl>
 

 <i>len</i>
<dl><dd>the max. buffer size</dl>

<h2>Description</h2>

Reads one line from the buffer and stores the string.

<h2>Return</h2>

Zero if successful, or 1 if error or EOF.

<h2>Copyright</h2>


