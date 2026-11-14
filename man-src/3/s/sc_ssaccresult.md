---
title: "sc_ssaccresult(3)"
name: "sc_ssaccresult"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ssaccresult/"
description: "sc::SSAccResult –"
---

<p>sc::SSAccResult &#8211; </p>
<p> This associates a result datum with an accuracy.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;comptmpl.h&gt;</code></pre>
<p> Inherits <code>sc::AccResultInfo</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SSAccResult (Compute *c)



SSAccResult (const SSAccResult&lt; T &gt; &amp;r, Compute *c)



operator T &amp; ()



T * operator-&gt; ()



T &amp; result ()



T &amp; result_noupdate ()



const T &amp; result_noupdate () const



void operator= (const T &amp;a)



void operator= (const SSAccResult&lt; T &gt; &amp;r)



void restore_state (StateIn &amp;s)



void save_data_state (StateOut &amp;s)



SSAccResult (StateIn &amp;s, Compute *c)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::SSAccResult&lt; T &gt;</h3>
<p>This associates a result datum with an accuracy. </p>
<p> The datum must be a <code>SavableState</code> and will be saved and restored.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
