---
title: "stdexperimentalrangesequal_to(3)"
name: "stdexperimentalrangesequal_to"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesequal_to/"
description: "std::experimental::ranges::equal_to – std::experimental::ranges::equal_to"
---

<p>std::experimental::ranges::equal_to &#8211; std::experimental::ranges::equal_to</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / functional&gt;

    template &lt;class T = void&gt;

requires EqualityComparable&lt;T&gt; ||

    Same&lt;T, void&gt; ||(ranges TS)

    /* == on two const T lvalues invokes a built-in operator comparing pointers */

    struct equal_to;

template &lt;&gt;
(ranges TS)

    struct equal_to&lt;void&gt;;
Function object for performing comparisons. The primary template invokes operator == on const lvalues of type T. The specialization equal_to&lt;void&gt; deduces the parameter types of the function call operator from the arguments (but not the return type).

All specializations of equal_to are Semiregular.
</code></pre>
<h2>Member types</h2>
<p>Member type Definition<br />
is_transparent (member only of equal_to&lt;void&gt; specialization) /* unspecified */</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the arguments are equal<br />
operator() <i>(public member function)</i> </p>
<p>std::experimental::ranges::equal_to::operator() </p>
<p>constexpr bool operator()(const T&amp; x, const T&amp; y) const; <code>(1)</code> (member only of primary equal_to&lt;T&gt; template)<br />
template&lt; class T, class U &gt;<br />
requires EqualityComparableWith&lt;T, U&gt; ||<br />
/* std::declval&lt;T&gt;() == std::declval&lt;U&gt;() resolves to <code>(2)</code> (member only of equal_to&lt;void&gt; specialization)<br />
a built-in operator comparing pointers */<br />
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; </p>
<p>1) Compares x and y. Equivalent to return ranges::equal_to&lt;&gt;{}(x, y);<br />
2) Compares t and u, equivalent to return std::forward&lt;T&gt;(t) == std::forward&lt;U&gt;(u);, except when that expression resolves to a call to a builtin operator == comparing pointers.<br />
When a call to <code>(1)</code> or <code>(2)</code> would invoke a built-in operator comparing pointers of type P, the result is instead determined as follows: </p>
<p>* Returns false if one of the (possibly converted) value of the first argument and the (possibly converted) value of the second argument precedes the other in the implementation-defined strict total ordering over all pointer values of type P. This strict total ordering is consistent with the partial order imposed by the builtin operators &lt;, &gt;, &lt;=, and &gt;=.<br />
* Otherwise (neither precedes the other), returns true. </p>
<p>The behavior is undefined unless the the conversion sequences from both T and U to P are equality-preserving (see below). </p>
<p>Equality preservation </p>
<p>An expression is equality preserving if it results in equal outputs given equal inputs. </p>
<p>* The inputs to an expression consist of its operands.<br />
* The outputs of an expression consist of its result and all operands modified by the expression (if any). </p>
<p>Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects.</p>
<h2>Notes</h2>
<p>Unlike std::equal_to, ranges::equal_to requires both == and != to be valid (via the EqualityComparable and EqualityComparableWith constraints). </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x == y<br />
equal_to <i>(class template)</i> </p>
