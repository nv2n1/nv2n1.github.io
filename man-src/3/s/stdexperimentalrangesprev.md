---
title: "stdexperimentalrangesprev(3)"
name: "stdexperimentalrangesprev"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesprev/"
---

std::experimental::ranges::prev - std::experimental::ranges::prev

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    namespace
{
    (ranges TS)

        constexpr /* unspecified */ prev = /* unspecified */;
    (customization point object)
}

Call signature

    template &lt;Iterator I&gt;
    (1)

        constexpr I prev(I i);

template &lt;Iterator I&gt;
(2)

    constexpr I prev(I i, ranges::difference_type_t&lt;I&gt; n);

template &lt;Iterator I&gt;
(3)

    constexpr I prev(I i, ranges::difference_type_t&lt;I&gt; n, I bound);
Decrements the iterator i n times, or until bound is reached, whichever comes first, and returns the decremented iterator.

1) Equivalent to --i;
return i;.

2) Equivalent to ranges::advance(i, -n);
return i;.

3) Equivalent to ranges::advance(i, -n, bound);
return i;
.</code></pre> 
Customization point objects 
The name ranges::prev denotes a customization point object, which is a function_object of a literal Semiregular class type (denoted, for exposition purposes, as PrevT). All instances of PrevT are equal. Thus, ranges::prev can be copied freely and its copies can be used interchangeably. 
Given a set of types Args..., if std::declval&lt;Args&gt;()... meet the requirements for arguments to ranges::prev above, PrevT will satisfy ranges::Invocable&lt;const PrevT, Args...&gt;. Otherwise, no function call operator of PrevT participates in overload resolution. 
In every translation unit in which ranges::prev is defined, it refers to the same instance of the customization point object. (This means that it can be used freely in things like inline functions and function templates without violating the one-definition_rule.) 

<h2>Return value</h2>

The decremented iterator. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

prev decrement an iterator 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance 
advance <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;increment an iterator 
next <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between an iterator and a sentinel, or between the beginning and the end of a range 
distance <i>(function template)</i> 
