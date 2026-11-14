---
title: "quantlib_disposable(3)"
name: "quantlib_disposable"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_disposable/"
description: "QuantLib::Disposable – generic disposable object with move semantics"
---

<p>QuantLib::Disposable &#8211; generic disposable object with move semantics </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/utilities/disposable.hpp&gt; </p>
<p> Inherits T. </p>
<h3>Public Member Functions</h3>
<p><code>Disposable</code> (T &amp;t) </p>
<p> <code>Disposable</code> (const <code>Disposable</code>&lt; T &gt; &amp;t) </p>
<p> <code>Disposable</code>&lt; T &gt; &amp; <code>operator=</code> (const <code>Disposable</code>&lt; T &gt; &amp;t) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Disposable&lt; T &gt;</h3>
<p>generic disposable object with move semantics </p>
<p> This class can be used for returning a value by copy. It relies on the returned object exposing a swap(T&amp;) method through which the copy constructor and assignment operator are implemented, thus resulting in actual move semantics. Typical use of this class is along the following lines: </p>
<pre> Disposable&lt;Foo&gt; bar(Integer i) {
 Foo f(i*2);
 return f;
 }</pre>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>In order to avoid copies in code such as shown above, the conversion from T to <code>Disposable</code>&lt;T&gt; is destructive, i.e., it does <code>not</code> preserve the state of the original object. Therefore, it is necessary for the developer to avoid code such as</dl>
<pre> Disposable&lt;Foo&gt; bar(Foo&amp; f) {
 return f;
 }</pre>
<p>&nbsp;<wbr>which would likely render the passed object unusable. The correct way to obtain the desired behavior would be:&nbsp;<wbr> </p>
<pre> Disposable&lt;Foo&gt; bar(Foo&amp; f) {
 Foo temp = f;
 return temp;
 }</pre>
<p>&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
