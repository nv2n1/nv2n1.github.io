---
title: "normalize_vector_f(3)"
name: "normalize_vector_f"
section: "3"
letter: "n"
url: "/docs/linux/man/3-normalize_vector_f/"
description: "normalize_vector, normalize_vector_f – Converts the vector to a unit vector. Allegro game programming library."
---

<p>normalize_vector, normalize_vector_f &#8211; Converts the vector to a unit vector. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void normalize_vector(fixed *x, fixed *y, fixed *z);
void normalize_vector_f(float *x, float *y, float *z);</code></pre>
<h2>Description</h2>
<p>Converts the vector (*x, *y, *z) to a unit vector. This points in the same direction as the original vector, but has a length of one. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-vector_length/">vector_length</a></code>(3), <code><a href="/docs/linux/man/3-dot_product/">dot_product</a></code>(3), <code><a href="/docs/linux/man/3-cross_product/">cross_product</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
