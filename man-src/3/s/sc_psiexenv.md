---
title: "sc_psiexenv(3)"
name: "sc_psiexenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psiexenv/"
description: "sc::PsiExEnv –"
---

<p>sc::PsiExEnv &#8211; </p>
<p> <code>PsiExEnv</code> specifies a Psi calculation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psiexenv.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PsiExEnv</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PsiExEnv</code> (char *cwd, char *fileprefix, int nscratch, char **scratch) </p>
<p> <code>Ref</code>&lt; <code>PsiInput</code> &gt; <code>get_psi_input</code> () const<br />
 <i>Returns the </i><code>PsiInput</code> object which <code>PsiExEnv</code> uses.<br />
 <code>Ref</code>&lt; <code>PsiFile11</code> &gt; <code>get_psi_file11</code> () const<br />
 <i>Returns the </i><code>PsiFile11</code> object which <code>PsiExEnv</code> uses.<br />
 int <code>run_psi</code> ()<br />
 <i>Executes Psi input+driver. </i><br />
 int <code>run_psi_module</code> (char *)<br />
 <i>Executes a Psi module. </i><br />
 string <code>get_cwd</code> () const<br />
 <i>Returns current working directory. </i><br />
 string <code>get_fileprefix</code> () const<br />
 <i>Returns the Psi file prefix. </i><br />
 int <code>get_nscratch</code> () const<br />
 <i>Returns the number of scratch locations. </i><br />
 string <code>get_scratch</code> (int i) const<br />
 <i>Returns the ith scratch location. </i><br />
 void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Print the object. </i></p>
<h2>Detailed Description</h2>
<p><code>PsiExEnv</code> specifies a Psi calculation.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
