---
title: "stdexperimentalrangesnext(3)"
name: "stdexperimentalrangesnext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesnext/"
description: "std::experimental::ranges::next – std::experimental::ranges::next"
---

<p>std::experimental::ranges::next &#8211; std::experimental::ranges::next</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    namespace
{
    (ranges TS)

        constexpr /* unspecified */ next = /* unspecified */;
    (customization point object)
}

Call signature

    template &lt;Iterator I&gt;
    (1)

        constexpr I next(I i);

template &lt;Iterator I&gt;
(2)

    constexpr I next(I i, ranges::difference_type_t&lt;I&gt; n);

template &lt;Iterator I, Sentinel&lt;I&gt; S&gt;
(3)

    constexpr I next(I i, S bound);

template &lt;Iterator I, Sentinel&lt;I&gt; S&gt;
(4)

    constexpr I next(I i, ranges::difference_type_t&lt;I&gt; n, S bound);
Advances the iterator i n times, or until bound is reached, whichever comes first, and returns the advanced iterator.

1) Equivalent to ++i;
return i;.

2) Equivalent to ranges::advance(i, n);
return i;.

3) Equivalent to ranges::advance(i, bound);
return i;.

4) Equivalent to ranges::advance(i, n, bound);
return i;
.</code></pre>
<p>Customization point objects<br />
The name ranges::next denotes a customization point object, which is a function_object of a literal Semiregular class type (denoted, for exposition purposes, as NextT). All instances of NextT are equal. Thus, ranges::next can be copied freely and its copies can be used interchangeably.<br />
Given a set of types Args&#8230;, if std::declval&lt;Args&gt;()&#8230; meet the requirements for arguments to ranges::next above, NextT will satisfy ranges::Invocable&lt;const NextT, Args&#8230;&gt;. Otherwise, no function call operator of NextT participates in overload resolution.<br />
In every translation unit in which ranges::next is defined, it refers to the same instance of the customization point object. (This means that it can be used freely in things like inline functions and function templates without violating the one-definition_rule.) </p>
<h2>Return value</h2>
<p>The advanced iterator. </p>
<h2>Notes</h2>
<p>Even though omitting n for overload <code>(2)</code> behaves as if n is 1, omitting n for overload <code>(4)</code> effectively behaves as if n is infinity (always advance to bound). </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>next increment an iterator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance<br />
advance <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;decrement an iterator<br />
prev <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between an iterator and a sentinel, or between the beginning and the end of a range<br />
distance <i>(function template)</i> </p>
