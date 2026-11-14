---
title: "handle(3)"
name: "handle"
section: "3"
letter: "h"
url: "/docs/linux/man/3-handle/"
description: "QuantLib::Handle – Shared handle to an observable."
---

<p>QuantLib::Handle &#8211; Shared handle to an observable. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/handle.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Handle</code> (const boost::shared_ptr&lt; T &gt; &amp;h=boost::shared_ptr&lt; T &gt;(), bool registerAsObserver=true) </p>
<p> const boost::shared_ptr&lt; T &gt; &amp; <code>currentLink</code> () const<br />
 <i>dereferencing </i><br />
 const boost::shared_ptr&lt; T &gt; &amp; <code>operator-&gt;</code> () const </p>
<p> const boost::shared_ptr&lt; T &gt; &amp; <code>operator*</code> () const </p>
<p> bool <code>empty</code> () const<br />
 <i>checks if the contained shared pointer points to anything </i><br />
 <code>operator boost::shared_ptr&lt; Observable &gt;</code> () const<br />
 <i>allows registration as observable </i><br />
 template&lt;class U &gt; bool <code>operator==</code> (const <code>Handle</code>&lt; U &gt; &amp;other)<br />
 <i>equality test </i><br />
 template&lt;class U &gt; bool <code>operator!=</code> (const <code>Handle</code>&lt; U &gt; &amp;other)<br />
 <i>disequality test </i><br />
 template&lt;class U &gt; bool <code>operator&lt;</code> (const <code>Handle</code>&lt; U &gt; &amp;other)<br />
 <i>strict weak ordering </i></p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; Link &gt; <code>link_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Handle&lt; T &gt;</h3>
<p>Shared handle to an observable. </p>
<p> All copies of an instance of this class refer to the same observable by means of a relinkable smart pointer. When such pointer is relinked to another observable, the change will be propagated to all the copies. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>Class T must inherit from <code>Observable</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Handle</code> (const boost::shared_ptr&lt; T &gt; &amp; h = boost::shared_ptr&lt;T&gt;(), bool registerAsObserver = true) [explicit]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>registerAsObserver is left as a backdoor in case the programmer cannot guarantee that the object pointed to will remain alive for the whole lifetime of the handle&#8212;namely, it should be set to false when the passed shared pointer does not own the pointee (this should only happen in a controlled environment, so that the programmer is aware of it). Failure to do so can very likely result in a program crash. If the programmer does want the handle to register as observer of such a shared pointer, it is his responsibility to ensure that the handle gets destroyed before the pointed object does.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
