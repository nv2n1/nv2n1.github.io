---
title: "stdexperimentaloptionaloperator-stdexperimentaloptionaloperator(3)"
name: "stdexperimentaloptionaloperator-stdexperimentaloptionaloperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloptionaloperator-stdexperimentaloptionaloperator/"
description: "std::experimental::optional<T>::operator->,std::experimental::optional<T>::operator* – std::experimental::optional<T>::operator->,std::experimental::optional<T>::operator*"
---

<p>std::experimental::optional&lt;T&gt;::operator-&gt;,std::experimental::optional&lt;T&gt;::operator* &#8211; std::experimental::optional&lt;T&gt;::operator-&gt;,std::experimental::optional&lt;T&gt;::operator*</p>
<h2>Synopsis</h2>
<p>constexpr const T* operator-&gt;() const; <code>(1)</code> (library fundamentals TS)<br />
constexpr T* operator-&gt;(); <code>(1)</code> (library fundamentals TS)<br />
constexpr const T&amp; operator*() const&amp;; <code>(2)</code> (library fundamentals TS)<br />
constexpr T&amp; operator*() &amp;; <code>(2)</code> (library fundamentals TS)<br />
constexpr const T&amp;&amp; operator*() const&amp;&amp;; <code>(2)</code> (library fundamentals TS)<br />
constexpr T&amp;&amp; operator*() &amp;&amp;; <code>(2)</code> (library fundamentals TS)<br />
Accesses the contained value.<br />
1) Returns a pointer to the contained value.<br />
2) Returns a reference to the contained value.<br />
The behavior is undefined if *this does not contain a value </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>Pointer or reference to the contained value. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Notes</h2>
<p>This operator does not check whether the optional contains a value. If checked access is needed, value() or value_or() may be used. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;experimental/optional&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

using namespace std::literals;

int main()

{
    std::experimental::optional&lt;int&gt; opt1 = 1;
    std::cout &lt;&lt; *opt1 &lt;&lt; '
';
    std::experimental::optional&lt;std::string&gt; opt2 = &quot;abc&quot;s;
    std::cout &lt;&lt; opt2-&gt;size() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;3</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value<br />
value <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value if available, another value otherwise<br />
value_or <i>(public member function)</i> </p>
