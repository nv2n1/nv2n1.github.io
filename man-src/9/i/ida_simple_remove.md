---
title: "ida_simple_remove(9)"
name: "ida_simple_remove"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ida_simple_remove/"
---

ida_simple_remove - remove an allocated id.

<h2>Synopsis</h2>

<pre><code>void ida_simple_remove(struct ida *ida, unsigned int id);</code></pre>

<h2>Arguments</h2>

<i>ida</i>
<dl><dd><dd>the (initialized) ida.</dl>
 

 <i>id</i>
<dl><dd>the id returned by ida_simple_get.</dl>

<h2>Copyright</h2>


