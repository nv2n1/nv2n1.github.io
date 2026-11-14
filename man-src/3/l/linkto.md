---
title: "linkto(3)"
name: "linkto"
section: "3"
letter: "l"
url: "/docs/linux/man/3-linkto/"
description: "QuantLib::RelinkableHandle – Relinkable handle to an observable."
---

<p>QuantLib::RelinkableHandle &#8211; Relinkable handle to an observable. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/handle.hpp&gt; </p>
<p> Inherits <code>Handle&lt; T &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>RelinkableHandle</code> (const boost::shared_ptr&lt; T &gt; &amp;h=boost::shared_ptr&lt; T &gt;(), bool registerAsObserver=true) </p>
<p> void <code>linkTo</code> (const boost::shared_ptr&lt; T &gt; &amp;, bool registerAsObserver=true) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::RelinkableHandle&lt; T &gt;</h3>
<p>Relinkable handle to an observable. </p>
<p> An instance of this class can be relinked so that it points to another observable. The change will be propagated to all handles that were created as copies of such instance. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>Class T must inherit from <code>Observable</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>RelinkableHandle</code> (const boost::shared_ptr&lt; T &gt; &amp; h = boost::shared_ptr&lt;T&gt;(), bool registerAsObserver = true) [explicit]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>see the <code>Handle</code> documentation for issues relatives to registerAsObserver.</dl>
<h2>Member Function Documentation</h2>
<h3>void linkTo (const boost::shared_ptr&lt; T &gt; &amp; h, bool registerAsObserver = true)</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>see the <code>Handle</code> documentation for issues relatives to registerAsObserver.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
