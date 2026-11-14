---
title: "stdexperimentalrangesnot_equal_to(3)"
name: "stdexperimentalrangesnot_equal_to"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesnot_equal_to/"
description: "std::experimental::ranges::not_equal_to – std::experimental::ranges::not_equal_to"
---

<p>std::experimental::ranges::not_equal_to &#8211; std::experimental::ranges::not_equal_to</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / functional&gt;

    template &lt;class T = void&gt;

requires EqualityComparable&lt;T&gt; ||

    Same&lt;T, void&gt; ||(ranges TS)

    /* == on two const T lvalues invokes a built-in operator comparing pointers */

    struct not_equal_to;

template &lt;&gt;
(ranges TS)

    struct not_equal_to&lt;void&gt;;
Function object for performing comparisons. The primary template invokes operator == on const lvalues of type T and negates the result. The specialization not_equal_to&lt;void&gt; deduces the parameter types of the function call operator from the arguments (but not the return type).

All specializations of not_equal_to are Semiregular.
</code></pre>
<h2>Member types</h2>
<p>Member type Definition<br />
is_transparent (member only of not_equal_to&lt;void&gt; specialization) /* unspecified */</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the arguments are not equal<br />
operator() <i>(public member function)</i> </p>
<p>std::experimental::ranges::not_equal_to::operator() </p>
<p>constexpr bool operator()(const T&amp; x, const T&amp; y) const; <code>(1)</code> (member only of primary not_equal_to&lt;T&gt; template)<br />
template&lt; class T, class U &gt;<br />
requires EqualityComparableWith&lt;T, U&gt; ||<br />
/* std::declval&lt;T&gt;() == std::declval&lt;U&gt;() resolves to <code>(2)</code> (member only of not_equal_to&lt;void&gt; specialization)<br />
a built-in operator comparing pointers */<br />
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; </p>
<p>1) Compares x and y. Equivalent to return !ranges::equal_to&lt;&gt;{}(x, y);<br />
2) Compares t and u. Equivalent to return !ranges::equal_to&lt;&gt;{}(std::forward&lt;T&gt;(t), std::forward&lt;U&gt;(u));.</p>
<h2>Notes</h2>
<p>Unlike std::not_equal_to, ranges::not_equal_to requires both == and != to be valid (via the EqualityComparable and EqualityComparableWith constraints), and is entirely defined in terms of ranges::equal_to. However, the implementation is free to use operator!= directly, because those concepts require the results of == and != to be consistent. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x != y<br />
not_equal_to <i>(class template)</i> </p>
