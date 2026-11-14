---
title: "stdexperimentalrangesdistance(3)"
name: "stdexperimentalrangesdistance"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesdistance/"
---

std::experimental::ranges::distance - std::experimental::ranges::distance

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    namespace
{
    (ranges TS)

        constexpr /* unspecified */ distance = /* unspecified */;
    (customization point object)
}

Call signature

    template &lt;Iterator I, Sentinel&lt;I&gt; S&gt;
    (1)

        constexpr ranges::difference_type_t&lt;I&gt; distance(I first, S last);

template &lt;Range R&gt;
(2)

    constexpr ranges::difference_type_t&lt;ranges::iterator_t&lt;R&gt;&gt; distance(R &amp;&amp;r);

template &lt;SizedRange R&gt;
(3)

    constexpr ranges::difference_type_t&lt;ranges::iterator_t&lt;R&gt;&gt; distance(R &amp;&amp;r);
Returns the distance between first and last, or between the beginning and the end of the range r.

1) If SizedSentinel&lt;S, I&gt; is satisfied, equivalent to return last - first;. Otherwise, returns the number of increments needed to get from first to last. If [first, last) does not denote a range, then I and S must be the same type and must model SizedSentinel, and [last, first) must denote a range. Otherwise, the behavior is undefined.

2) Equivalent to return ranges::distance(ranges::begin(r), ranges::end(r));

3) Equivalent to return ranges::size(r);

Instantiating overloads (2-3) may be ill-formed if the header &lt;experimental/ranges/range&gt; is not included before the point of instantiation.</code></pre> 
Customization point objects 
The name ranges::distance denotes a customization point object, which is a function_object of a literal Semiregular class type (denoted, for exposition purposes, as DistanceT). All instances of DistanceT are equal. Thus, ranges::distance can be copied freely and its copies can be used interchangeably. 
Given a set of types Args..., if std::declval&lt;Args&gt;()... meet the requirements for arguments to ranges::distance above, DistanceT will satisfy ranges::Invocable&lt;const DistanceT, Args...&gt;. Otherwise, no function call operator of DistanceT participates in overload resolution. 
In every translation unit in which ranges::distance is defined, it refers to the same instance of the customization point object. (This means that it can be used freely in things like inline functions and function templates without violating the one-definition_rule.) 

<h2>Return value</h2>

The distance between first and last, or between the beginning and the end of the range r. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between two iterators 
distance <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance 
advance <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;increment an iterator 
next <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;decrement an iterator 
prev <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the size of a range whose size can be calculated in constant time 
size (customization point object) 
