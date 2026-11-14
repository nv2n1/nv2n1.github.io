---
title: "stdexperimentalrangesreference_tstdexperimentalrangesrvalue_reference_t(3)"
name: "stdexperimentalrangesreference_tstdexperimentalrangesrvalue_reference_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesreference_tstdexperimentalrangesrvalue_reference_t/"
description: "std::experimental::ranges::reference_t,std::experimental::ranges::rvalue_reference_t, – std::experimental::ranges::reference_t,std::experimental::ranges::rvalue_reference_t,"
---

<p>std::experimental::ranges::reference_t,std::experimental::ranges::rvalue_reference_t, &#8211; std::experimental::ranges::reference_t,std::experimental::ranges::rvalue_reference_t,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class T&gt;

concept bool /*dereferenceable*/ = requires(T&amp; t) { {*t} -&gt; auto&amp;&amp;;

}; // exposition only

template&lt; /*dereferenceable*/ T &gt;                                    (1) (ranges TS)

using reference_t = decltype(*declval&lt;T&amp;&gt;());

template&lt; /*dereferenceable*/ T &gt;</code></pre>
<p>requires requires(T&amp;&nbsp;<wbr>t)&nbsp;<wbr>{&nbsp;<wbr>{&nbsp;<wbr>ranges::iter_move(t)&nbsp;<wbr>}&nbsp;<wbr>-&gt;&nbsp;<wbr>auto&amp;&amp;;&nbsp;<wbr>}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr>(ranges TS) </p>
<pre><code>using rvalue_reference_t =

decltype(ranges::iter_move(declval&lt;T&amp;&gt;()));

template&lt; Readable T &gt;
using iter_common_reference_t =                                      (3) (ranges TS)

ranges::common_reference_t&lt;ranges::reference_t&lt;T&gt;,
ranges::value_type_t&lt;T&gt;&amp;&gt;;</code></pre>
<p>1)&nbsp;<wbr>Obtain the reference type of a dereferenceable type T.<br />
2)&nbsp;<wbr>Obtain the rvalue reference type of a dereferenceable type T, that is, the return<br />
type of ranges::iter_move.<br />
3)&nbsp;<wbr>Compute a Readable type&#8217;s common reference type. This is the common reference<br />
type of its reference type and an lvalue reference to its value type. </p>
<h2>Notes</h2>
<p>The -&gt;&nbsp;<wbr>auto&amp;&amp;&nbsp;<wbr>constraint checks that the type of the expression is not void. </p>
