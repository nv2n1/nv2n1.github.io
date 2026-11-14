---
title: "snd_info_get_str(9)"
name: "snd_info_get_str"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_info_get_str/"
---

snd_info_get_str - parse a string token

<h2>Synopsis</h2>

<pre><code>const char *snd_info_get_str(char *dest, const char *src, int len);</code></pre>

<h2>Arguments</h2>

<i>dest</i>
<dl><dd><dd>the buffer to store the string token</dl>
 

 <i>src</i>
<dl><dd>the original string</dl>
 

 <i>len</i>
<dl><dd>the max. length of token - 1</dl>

<h2>Description</h2>

Parses the original string and copy a token to the given string buffer.

<h2>Return</h2>

The updated pointer of the original string so that it can be used for the next call.

<h2>Copyright</h2>


