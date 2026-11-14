---
title: "sc_psifile11(3)"
name: "sc_psifile11"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psifile11/"
description: "sc::PsiFile11 –"
---

<p>sc::PsiFile11 &#8211; </p>
<p> <code>PsiFile11</code> is a Psi gradient file.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psifile11.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PsiFile11</code> (const string &amp;name) </p>
<p> void <code>open</code> () </p>
<p> void <code>close</code> () </p>
<p> void <code>remove</code> () </p>
<p> int <code>get_natom</code> (int entry) </p>
<p> double <code>get_energy</code> (int entry) </p>
<p> double <code>get_coord</code> (int entry, int atom, int xyz) </p>
<p> double <code>get_grad</code> (int entry, int atom, int xyz)</p>
<h2>Detailed Description</h2>
<p><code>PsiFile11</code> is a Psi gradient file.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
