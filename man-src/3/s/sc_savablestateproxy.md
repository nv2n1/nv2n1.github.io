---
title: "sc_savablestateproxy(3)"
name: "sc_savablestateproxy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_savablestateproxy/"
description: "sc::SavableStateProxy –"
---

<p>sc::SavableStateProxy &#8211; </p>
<p> Create a proxy for a <code>SavableState</code> object.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;proxy.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClassProxy</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Ref</code>&lt; <code>DescribedClass</code> &gt; <code>object</code> ()<br />
 <i>Return the object referred to by this proxy. </i><br />
 <code>SavableStateProxy</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Create the proxy with a </i><code>Ref</code> to a <code>KeyVal</code> object.</p>
<h2>Detailed Description</h2>
<p>Create a proxy for a <code>SavableState</code> object. </p>
<p> This can be used to include an object that has been saved with <code>SavableState</code> in an input file for <code>ParsedKeyVal</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
