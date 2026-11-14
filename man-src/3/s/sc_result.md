---
title: "sc_result(3)"
name: "sc_result"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_result/"
description: "sc::Result –"
---

<p>sc::Result &#8211; </p>
<p> <code>Result</code> are members of <code>Compute</code> specializations that keep track of whether or not a particular result should be computed or if it has already been computed.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;comptmpl.h&gt;</code></pre>
<p> Inherits <code>sc::ResultInfo</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Result (Compute *c)



Result (const Result&lt; T &gt; &amp;r, Compute *c)



operator T &amp; ()



T * operator-&gt; ()



T &amp; result ()



T &amp; result_noupdate ()



const T &amp; result_noupdate () const



void operator= (const T &amp;a)



void operator= (const Result&lt; T &gt; &amp;r)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::Result&lt; T &gt;</h3>
<p><code>Result</code> are members of <code>Compute</code> specializations that keep track of whether or not a particular result should be computed or if it has already been computed. </p>
<p> For non-class template parameters, use <code>NCResult</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
