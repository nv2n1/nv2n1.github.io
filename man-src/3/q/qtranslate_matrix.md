---
title: "qtranslate_matrix(3)"
name: "qtranslate_matrix"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qtranslate_matrix/"
description: "qtranslate_matrix, qtranslate_matrix_f – Optimised routine for translating an already generated matrix. Allegro game programming library."
---

<p>qtranslate_matrix, qtranslate_matrix_f &#8211; Optimised routine for translating an already generated matrix. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void qtranslate_matrix(MATRIX *m, fixed x, fixed y, fixed z);
void qtranslate_matrix_f(MATRIX_f *m, float x, float y, float z);</code></pre>
<h2>Description</h2>
<p>Optimised routine for translating an already generated matrix: this simply adds in the translation offset, so there is no need to build two temporary matrices and then multiply them together. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_translation_matrix/">get_translation_matrix</a></code>(3) </p>
