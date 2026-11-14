---
title: "sc_translatedatain(3)"
name: "sc_translatedatain"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_translatedatain/"
description: "sc::TranslateDataIn –"
---

<p>sc::TranslateDataIn &#8211; </p>
<p> Convert data from other formats.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;translate.h&gt;

Public Member Functions</code></pre>
<p> <code>TranslateDataIn</code> (<code>StateIn</code> *s, <code>TranslateData</code> *t)<br />
 <i>Input data will come from s. </i><br />
 virtual int <code>get</code> (char *, int)<br />
 <i>Read and translate data. </i><br />
 virtual int <code>get</code> (short *, int) </p>
<p> virtual int <code>get</code> (unsigned int *, int) </p>
<p> virtual int <code>get</code> (int *, int) </p>
<p> virtual int <code>get</code> (long *, int) </p>
<p> virtual int <code>get</code> (float *, int) </p>
<p> virtual int <code>get</code> (double *, int) </p>
<p> <code>TranslateData</code> * <code>translator</code> ()<br />
 <i>Return the translator. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>int getv (void *d, int s)</code></pre>
<h2>Detailed Description</h2>
<p>Convert data from other formats. </p>
<p> The data is taken from a <code>StateIn</code> object.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::TranslateDataIn::TranslateDataIn (<code>StateIn</code> * s, <code>TranslateData</code> * t)</h3>
<p>Input data will come from s. The t argument will be deleted by this.</p>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::TranslateDataIn::get (char *, int) [virtual]</h3>
<p>Read and translate data. A similar member exists for each basic type.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
