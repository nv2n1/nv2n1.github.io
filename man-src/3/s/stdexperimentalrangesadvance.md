---
title: "stdexperimentalrangesadvance(3)"
name: "stdexperimentalrangesadvance"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesadvance/"
---

std::experimental::ranges::advance - std::experimental::ranges::advance

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    namespace
{
    (ranges TS)

        constexpr /* unspecified */ advance = /* unspecified */;
    (customization point object)
}

Call signature

    template &lt;Iterator I&gt;
    (1)

        constexpr void advance(I &amp;i, ranges::difference_type_t&lt;I&gt; n);

template &lt;Iterator I, Sentinel&lt;I&gt; S&gt;
(2)

    constexpr void advance(I &amp;i, S bound);

template &lt;Iterator I, Sentinel&lt;I&gt; S&gt;
(3)

    constexpr ranges::difference_type_t&lt;I&gt; advance(I &amp;i, ranges::difference_type_t&lt;I&gt; n, S bound);
Advances the iterator i n times, or until bound is reached, whichever comes first.

1) If I models RandomAccessIterator, equivalent to i += n. Otherwise, increments (or decrements if n is negative) i n times. The behavior is undefined if n is negative and I does not model BidirectionalIterator.

2) If Assignable&lt;I&amp;, S&gt; is satisfied, equivalent to &#123;&#123;{1}}}.

Otherwise, if [i, bound) does not denote a range, the behavior is undefined.

Otherwise, if SizedSentinel&lt;S, I&gt; is satisfied, equivalent to ranges::advance(i, bound - i).

Otherwise, increments i until i == bound.

3) If SizedSentinel&lt;S, I&gt; is satisfied, equivalent to ranges::advance(i, bound) if |n| &gt;= |bound - i|, and ranges::advance(i, n) otherwise.

Otherwise, increments (or decrements if n is negative) i either n times or until i == bound, whichever comes first.

If n &gt; 0, [i, bound) shall denote a range; if n == 0, either [i, bound) or [bound, i) shall denote a range; if n &lt; 0, [bound, i) shall denote a range, I and S shall be the same type, and I must model BidirectionalIterator. Otherwise, the behavior is undefined.</code></pre> 
Customization point objects 
The name ranges::advance denotes a customization point object, which is a function_object of a literal Semiregular class type (denoted, for exposition purposes, as AdvanceT). All instances of AdvanceT are equal. Thus, ranges::advance can be copied freely and its copies can be used interchangeably. 
Given a set of types Args..., if std::declval&lt;Args&gt;()... meet the requirements for arguments to ranges::advance above, AdvanceT will satisfy ranges::Invocable&lt;const AdvanceT, Args...&gt;. Otherwise, no function call operator of AdvanceT participates in overload resolution. 
In every translation unit in which ranges::advance is defined, it refers to the same instance of the customization point object. (This means that it can be used freely in things like inline functions and function templates without violating the one-definition_rule.) 

<h2>Return value</h2>

1-2) <i>(none)</i> 
3) The number of increment/decrements not performed due to reaching bound. In other words, n - M, where M is the distance from the starting position of i to the ending position and is negative if the ending position is before the starting position. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance 
advance <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between an iterator and a sentinel, or between the beginning and the end of a range 
distance <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;increment an iterator 
next <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;decrement an iterator 
prev <i>(function template)</i> 
