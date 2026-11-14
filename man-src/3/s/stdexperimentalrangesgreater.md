---
title: "stdexperimentalrangesgreater(3)"
name: "stdexperimentalrangesgreater"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesgreater/"
description: "std::experimental::ranges::greater – std::experimental::ranges::greater"
---

<p>std::experimental::ranges::greater &#8211; std::experimental::ranges::greater</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / functional&gt;

    template &lt;class T = void&gt;

requires StrictTotallyOrdered&lt;T&gt; ||

    Same&lt;T, void&gt; ||(ranges TS)

    /* &lt; on two const T lvalues invokes a built-in operator comparing pointers */

    struct greater;

template &lt;&gt;
(ranges TS)

    struct greater&lt;void&gt;;
Function object for performing comparisons. The primary template invokes operator&lt; on const lvalues of type T with the argument order inverted. The specialization greater&lt;void&gt; deduces the parameter types of the function call operator from the arguments (but not the return type).

All specializations of greater are Semiregular.
</code></pre>
<h2>Member types</h2>
<p>Member type Definition<br />
is_transparent (member only of greater&lt;void&gt; specialization) /* unspecified */</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the first argument is greater than the second<br />
operator() <i>(public member function)</i> </p>
<p>std::experimental::ranges::greater::operator() </p>
<p>constexpr bool operator()(const T&amp; x, const T&amp; y) const; <code>(1)</code> (member only of primary greater&lt;T&gt; template)<br />
template&lt; class T, class U &gt;<br />
requires StrictTotallyOrderedWith&lt;T, U&gt; ||<br />
/* std::declval&lt;T&gt;() &lt; std::declval&lt;U&gt;() resolves to <code>(2)</code> (member only of greater&lt;void&gt; specialization)<br />
a built-in operator comparing pointers */<br />
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; </p>
<p>1) Compares x and y. Equivalent to return ranges::less&lt;&gt;{}(y, x);<br />
2) Compares t and u. Equivalent to return ranges::less&lt;&gt;{}(std::forward&lt;U&gt;(u), std::forward&lt;T&gt;(t));.</p>
<h2>Notes</h2>
<p>Unlike std::greater, ranges::greater requires all six comparison operators &lt;, &lt;=, &gt;, &gt;=, == and != to be valid (via the StrictTotallyOrdered and StrictTotallyOrderedWith constraints) and is entirely defined in terms of ranges::less. However, the implementation is free to use operator&gt; directly, because those concepts require the results of the comparison operators to be consistent. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &gt; y<br />
greater <i>(class template)</i> </p>
