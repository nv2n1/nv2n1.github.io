---
title: "stdoptionaloperator-stdoptionaloperator(3)"
name: "stdoptionaloperator-stdoptionaloperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionaloperator-stdoptionaloperator/"
description: "std::optional<T>::operator->,std::optional<T>::operator* – std::optional<T>::operator->,std::optional<T>::operator*"
---

<p>std::optional&lt;T&gt;::operator-&gt;,std::optional&lt;T&gt;::operator* &#8211; std::optional&lt;T&gt;::operator-&gt;,std::optional&lt;T&gt;::operator*</p>
<h2>Synopsis</h2>
<p>constexpr const T* operator-&gt;() const; <code>(1)</code> <i>(since C++17)</i><br />
constexpr T* operator-&gt;(); <code>(1)</code> <i>(since C++17)</i><br />
constexpr const T&amp; operator*() const&amp;; <code>(2)</code> <i>(since C++17)</i><br />
constexpr T&amp; operator*() &amp;; <code>(2)</code> <i>(since C++17)</i><br />
constexpr const T&amp;&amp; operator*() const&amp;&amp;; <code>(2)</code> <i>(since C++17)</i><br />
constexpr T&amp;&amp; operator*() &amp;&amp;; <code>(2)</code> <i>(since C++17)</i><br />
Accesses the contained value.<br />
1) Returns a pointer to the contained value.<br />
2) Returns a reference to the contained value.<br />
The behavior is undefined if *this does not contain a value. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>Pointer or reference to the contained value. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Notes</h2>
<p>This operator does not check whether the optional contains a value! You can do so manually by using has_value() or simply operator_bool(). Alternatively, if checked access is needed, value() or value_or() may be used. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;optional&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    using namespace std::string_literals;
    std::optional&lt;int&gt; opt1 = 1;
    std::cout &lt;&lt; &quot;opt1: &quot; &lt;&lt; *opt1 &lt;&lt; '
';
    *opt1 = 2;
    std::cout &lt;&lt; &quot;opt1: &quot; &lt;&lt; *opt1 &lt;&lt; '
';
    std::optional&lt;std::string&gt; opt2 = &quot;abc&quot;s;
    std::cout &lt;&lt; &quot;opt2: &quot; &lt;&lt; *opt2 &lt;&lt; &quot; size: &quot; &lt;&lt; opt2-&gt;size() &lt;&lt; '
';
    // You can &quot;take&quot; the contained value by calling operator* on a rvalue to optional
    auto taken = *std::move(opt2);
    std::cout &lt;&lt; &quot;taken: &quot; &lt;&lt; taken &lt;&lt; &quot; opt2: &quot; &lt;&lt; *opt2 &lt;&lt; &quot;size: &quot; &lt;&lt; opt2-&gt;size() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;opt1: 1<br />
&nbsp;<wbr>&nbsp;opt1: 2<br />
&nbsp;<wbr>&nbsp;opt2: abc size: 3<br />
&nbsp;<wbr>&nbsp;taken: abc opt2: size: 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value<br />
value <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value if available, another value otherwise<br />
value_or <i>(public member function)</i> </p>
