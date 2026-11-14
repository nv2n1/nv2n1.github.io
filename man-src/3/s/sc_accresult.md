---
title: "sc_accresult(3)"
name: "sc_accresult"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_accresult/"
description: "sc::AccResult –"
---

<p>sc::AccResult &#8211; </p>
<p> This associates a result datum with an accuracy.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;comptmpl.h&gt;</code></pre>
<p> Inherits <code>sc::AccResultInfo</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>AccResult (Compute *c)



AccResult (const AccResult&lt; T &gt; &amp;r, Compute *c)



operator T &amp; ()



T * operator-&gt; ()



T &amp; result ()



T &amp; result_noupdate ()



const T &amp; result_noupdate () const



void operator= (const T &amp;a)



void operator= (const AccResult&lt; T &gt; &amp;r)



void restore_state (StateIn &amp;s)



void save_data_state (StateOut &amp;s)



AccResult (StateIn &amp;s, Compute *c)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::AccResult&lt; T &gt;</h3>
<p>This associates a result datum with an accuracy. </p>
<p> If the result datum is to be saved or restored use <code>SSAccResult</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
