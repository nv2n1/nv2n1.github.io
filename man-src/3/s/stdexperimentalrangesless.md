---
title: "stdexperimentalrangesless(3)"
name: "stdexperimentalrangesless"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesless/"
description: "std::experimental::ranges::less – std::experimental::ranges::less"
---

<p>std::experimental::ranges::less &#8211; std::experimental::ranges::less</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / functional&gt;

    template &lt;class T = void&gt;

requires StrictTotallyOrdered&lt;T&gt; ||

    Same&lt;T, void&gt; ||(ranges TS)

    /* &lt; on two const T lvalues invokes a built-in operator comparing pointers */

    struct less;

template &lt;&gt;
(ranges TS)

    struct less&lt;void&gt;;
Function object for performing comparisons. The primary template invokes operator&lt; on const lvalues of type T. The specialization less&lt;void&gt; deduces the parameter types of the function call operator from the arguments (but not the return type).

All specializations of less are Semiregular.
</code></pre>
<h2>Member types</h2>
<p>Member type Definition<br />
is_transparent (member only of less&lt;void&gt; specialization) /* unspecified */</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the first argument is less than the second<br />
operator() <i>(public member function)</i> </p>
<p>std::experimental::ranges::less::operator() </p>
<p>constexpr bool operator()(const T&amp; x, const T&amp; y) const; <code>(1)</code> (member only of primary less&lt;T&gt; template)<br />
template&lt; class T, class U &gt;<br />
requires StrictTotallyOrderedWith&lt;T, U&gt; ||<br />
/* std::declval&lt;T&gt;() &lt; std::declval&lt;U&gt;() resolves to <code>(2)</code> (member only of less&lt;void&gt; specialization)<br />
a built-in operator comparing pointers */<br />
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; </p>
<p>1) Compares x and y. Equivalent to return ranges::less&lt;&gt;{}(x, y);<br />
2) Compares t and u, equivalent to return std::forward&lt;T&gt;(t) &lt; std::forward&lt;U&gt;(u);, except when that expression resolves to a call to a builtin operator&lt; comparing pointers.<br />
When a call to <code>(1)</code> or <code>(2)</code> would invoke a built-in operator comparing pointers of type P, the result is instead determined as follows: </p>
<p>* Returns true if the (possibly converted) value of the first argument precedes the (possibly converted) value of the second argument in the implementation-defined strict total ordering over all pointer values of type P. This strict total ordering is consistent with the partial order imposed by the builtin operators &lt;, &gt;, &lt;=, and &gt;=.<br />
* Otherwise, returns false. </p>
<p>The behavior is undefined unless the the conversion sequences from both T and U to P are equality-preserving (see below). </p>
<p>Equality preservation </p>
<p>An expression is equality preserving if it results in equal outputs given equal inputs. </p>
<p>* The inputs to an expression consist of its operands.<br />
* The outputs of an expression consist of its result and all operands modified by the expression (if any). </p>
<p>Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects.</p>
<h2>Notes</h2>
<p>Unlike std::less, ranges::less requires all six comparison operators &lt;, &lt;=, &gt;, &gt;=, == and != to be valid (via the StrictTotallyOrdered and StrictTotallyOrderedWith constraints). </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &lt; y<br />
less <i>(class template)</i> </p>
