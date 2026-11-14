---
title: "quantlib_observablevalue(3)"
name: "quantlib_observablevalue"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_observablevalue/"
description: "QuantLib::ObservableValue – observable and assignable proxy to concrete value"
---

<p>QuantLib::ObservableValue &#8211; observable and assignable proxy to concrete value </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/utilities/observablevalue.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>ObservableValue</code> (const T &amp;) </p>
<p> <code>ObservableValue</code> (const <code>ObservableValue</code>&lt; T &gt; &amp;) </p>
<p> <code>operator T</code> () const<br />
 <i>implicit conversion </i><br />
 <code>operator boost::shared_ptr&lt; Observable &gt;</code> () const </p>
<p> const T &amp; <code>value</code> () const<br />
 <i>explicit inspector </i> </p>
<p> <code>controlled assignment</code> </p>
<p> <code>ObservableValue</code>&lt; T &gt; &amp; <code>operator=</code> (const T &amp;) </p>
<p> <code>ObservableValue</code>&lt; T &gt; &amp; <code>operator=</code> (const <code>ObservableValue</code>&lt; T &gt; &amp;) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::ObservableValue&lt; T &gt;</h3>
<p>observable and assignable proxy to concrete value </p>
<p> Observers can be registered with instances of this class so that they are notified when a different value is assigned to such instances. Client code can copy the contained value or pass it to functions via implicit conversion. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>it is not possible to call non-const method on the returned value. This is by design, as this possibility would necessarily bypass the notification code; client code should modify the value via re-assignment instead.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
