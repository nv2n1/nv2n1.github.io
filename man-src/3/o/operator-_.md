---
title: "operator-_(3)"
name: "operator-_"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operator-_/"
description: "QuantLib::Handle – Shared handle to an observable."
---

<p>QuantLib::Handle &#8211; Shared handle to an observable. </p>
<h2>Synopsis</h2>
<pre><code>Handle (const boost::shared_ptr&lt; T &gt; &amp;h=boost::shared_ptr&lt; T &gt;(), bool registerAsObserver=true)



const boost::shared_ptr&lt; T &gt; &amp; currentLink () const


dereferencing


const boost::shared_ptr&lt; T &gt; &amp; operator-&gt; () const



const boost::shared_ptr&lt; T &gt; &amp; operator* () const



bool empty () const


checks if the contained shared pointer points to anything


operator boost::shared_ptr&lt; Observable &gt; () const


allows registration as observable


template&lt;class U &gt; bool operator== (const Handle&lt; U &gt; &amp;other)


equality test


template&lt;class U &gt; bool operator!= (const Handle&lt; U &gt; &amp;other)


disequality test


template&lt;class U &gt; bool operator&lt; (const Handle&lt; U &gt; &amp;other)


strict weak ordering



Protected Attributes</code></pre>
<h3>Public Member Functions</h3>
<pre><code>Handle (const boost::shared_ptr&lt; T &gt; &amp;h=boost::shared_ptr&lt; T &gt;(), bool registerAsObserver=true)



const boost::shared_ptr&lt; T &gt; &amp; currentLink () const


dereferencing


const boost::shared_ptr&lt; T &gt; &amp; operator-&gt; () const



const boost::shared_ptr&lt; T &gt; &amp; operator* () const



bool empty () const


checks if the contained shared pointer points to anything


operator boost::shared_ptr&lt; Observable &gt; () const


allows registration as observable


template&lt;class U &gt; bool operator== (const Handle&lt; U &gt; &amp;other)


equality test


template&lt;class U &gt; bool operator!= (const Handle&lt; U &gt; &amp;other)


disequality test


template&lt;class U &gt; bool operator&lt; (const Handle&lt; U &gt; &amp;other)


strict weak ordering



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; Link &gt; <code>link_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Handle&lt; T &gt;</h3>
<p>Shared handle to an observable. </p>
<p> All copies of an instance of this class refer to the same observable by means of a relinkable smart pointer. When such pointer is relinked to another observable, the change will be propagated to all the copies. </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>Class T must inherit from <code>Observable</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Handle</code> (const boost::shared_ptr&lt; T &gt; &amp; h = boost::shared_ptr&lt;T&gt;(), bool registerAsObserver = true) [explicit]</h3>
<p><code>Warning</code></p>
<dl>
<dd>registerAsObserver is left as a backdoor in case the programmer cannot guarantee that the object pointed to will remain alive for the whole lifetime of the handle&#8212;namely, it should be set to false when the passed shared pointer does not own the pointee (this should only happen in a controlled environment, so that the programmer is aware of it). Failure to do so can very likely result in a program crash. If the programmer does want the handle to register as observer of such a shared pointer, it is his responsibility to ensure that the handle gets destroyed before the pointed object does.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
