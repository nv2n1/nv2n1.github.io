---
title: "stdexperimentalrangesvalue_type(3)"
name: "stdexperimentalrangesvalue_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesvalue_type/"
description: "std::experimental::ranges::value_type – std::experimental::ranges::value_type"
---

<p>std::experimental::ranges::value_type &#8211; std::experimental::ranges::value_type</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class I&gt;
    (1)

        struct value_type {
};

template &lt;class T&gt;
(2)

    struct value_type&lt;T *&gt;;

template &lt;class I&gt;

requires std::is_array&lt;I&gt;::value(3)

struct value_type&lt;I&gt; : value_type&lt;std::decay_t&lt;I&gt;&gt; {
};

template &lt;class T&gt;
(4)

    struct value_type&lt;const T&gt; : value_type&lt;std::decay_t&lt;T&gt;&gt; {
};

template &lt;class T&gt;

requires requires
{
    typename T::value_type;
}
(5)

    struct value_type&lt;T&gt;;

template &lt;class T&gt;

requires requires
{
    typename T::element_type;
}
(6)

    struct value_type&lt;T&gt;;</code></pre>
<p>Computes the associated value type of the type I, if any. Users may specialize value_type for a program-defined type.<br />
1) Primary template is an empty struct.<br />
2) Specialization for pointers. If T is an object type, provides a member type type equal to std::remove_cv_t&lt;T&gt;. Otherwise, there is no member type.<br />
3) Specialization for array types.<br />
4) Specialization for const-qualified types.<br />
5) Specialization for types that define a public and accessible member type value_type. If T::value_type is an object type, provides a member type type equal to T::value_type. Otherwise, there is no member type.<br />
6) Specialization for types that define a public and accessible member type element_type (e.g., std::shared_ptr). If T::element_type is an object type, provides a member type type equal to std::remove_cv_t&lt;typename T::element_type&gt;. Otherwise, there is no member type.<br />
Helper alias template </p>
<pre><code>template&lt; class T &gt;                                         (ranges TS)

using value_type_t = typename ranges::value_type&lt;T&gt;::type;

</code></pre>
<h2>Notes</h2>
<p>If a type contains both a value_type member and a element_type member, then the specializations <code>(5)</code> and <code>(6)</code> are ambiguous.<br />
value_type is intended for use with Readable types such as iterators. It is not intended for use with ranges. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a type is readable by applying operator *<br />
Readable (concept)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compatibility traits class that collects an iterator’s associated types<br />
iterator_traits (alias template) </p>
