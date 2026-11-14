---
title: "kstrtobool(9)"
name: "kstrtobool"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kstrtobool/"
---

kstrtobool - convert common user inputs into boolean values

<h2>Synopsis</h2>

<pre><code>int kstrtobool(const char *s, bool *res);</code></pre>

<h2>Arguments</h2>

<i>s</i>
<dl><dd><dd>input string</dl>
 

 <i>res</i>
<dl><dd>result</dl>

<h2>Description</h2>

This routine returns 0 iff the first character is one of 'Yy1Nn0', or [oO][NnFf] for "on" and "off". Otherwise it will return -EINVAL. Value pointed to by res is updated upon finding a match.

<h2>Copyright</h2>


