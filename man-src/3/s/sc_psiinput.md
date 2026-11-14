---
title: "sc_psiinput(3)"
name: "sc_psiinput"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psiinput/"
description: "sc::PsiInput –"
---

<p>sc::PsiInput &#8211; </p>
<p> <code>PsiInput</code> is a Psi input file.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psiinput.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PsiInput</code> (const string &amp;name) </p>
<p> void <code>open</code> () </p>
<p> void <code>close</code> () </p>
<p> void <code>print</code> (std::ostream &amp;) </p>
<p> void <code>begin_section</code> (const char *s) </p>
<p> void <code>end_section</code> () </p>
<p> void <code>write_indent</code> () </p>
<p> void <code>incindent</code> (int) </p>
<p> void <code>decindent</code> (int) </p>
<p> void <code>write_comment</code> (const char *) </p>
<p> void <code>write_keyword</code> (const char *, const char *) </p>
<p> void <code>write_keyword</code> (const char *, int) </p>
<p> void <code>write_keyword</code> (const char *, double) </p>
<p> void <code>write_keyword_array</code> (const char *, int, int *) </p>
<p> void <code>write_keyword_array</code> (const char *, int, double *) </p>
<p> void <code>write_string</code> (const char *) </p>
<p> void <code>write_key_wq</code> (const char *, const char *) </p>
<p> void <code>write_basis</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;)<br />
 <i>Construct the &#8216;basis&#8217; keyword for input. </i><br />
 void <code>write_basis_sets</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;)<br />
 <i>Write basis sets explicitly. </i><br />
 void <code>write_geom</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;) </p>
<p> void <code>write_defaults</code> (const <code>Ref</code>&lt; <code>PsiExEnv</code> &gt; &amp;, const char *dertype)</p>
<h2>Detailed Description</h2>
<p><code>PsiInput</code> is a Psi input file.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
