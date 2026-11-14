---
title: "stdreadable_traits(3)"
name: "stdreadable_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreadable_traits/"
description: "std::readable_traits – std::readable_traits"
---

<p>std::readable_traits &#8211; std::readable_traits</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class I&gt;
    (1)(since C++ 20)

        struct readable_traits {
};

template &lt;class T&gt;
(2)(since C++ 20)

    struct readable_traits&lt;T *&gt;;

template &lt;class I&gt;

requires std::is_array_v&lt;I&gt;(3)
(since C++ 20)

    struct readable_traits&lt;I&gt;;

template &lt;class T&gt;
(4)(since C++ 20)

    struct readable_traits&lt;const T&gt; : value_type&lt;T&gt; {
};

template &lt;class T&gt;

requires requires
{
    typename T::value_type;
}
(5)(since C++ 20)

    struct readable_traits&lt;T&gt;;

template &lt;class T&gt;

requires requires
{
    typename T::element_type;
}
(6)(since C++ 20)

    struct readable_traits&lt;T&gt;;</code></pre>
<p>Computes the associated value type of the type I, if any. Users may specialize readable_traits for a program-defined type.<br />
1) Primary template is an empty struct.<br />
2) Specialization for pointers. If T is an object type, provides a member type value_type equal to std::remove_cv_t&lt;T&gt;. Otherwise, there is no member value_type.<br />
3) Specialization for array types. Provides a member type value_type equal to std::remove_cv_t&lt;std::remove_extent_t&lt;I&gt;&gt;.<br />
4) Specialization for const-qualified types.<br />
5) Specialization for types that define a public and accessible member type value_type. If T::value_type is an object type, provides a member type value_type equal to std::remove_cv_t&lt;typename T::value_type&gt;. Otherwise, there is no member value_type.<br />
6) Specialization for types that define a public and accessible member type element_type (e.g., std::shared_ptr). If T::element_type is an object type, provides a member type value_type equal to std::remove_cv_t&lt;typename T::element_type&gt;. Otherwise, there is no member value_type. </p>
<h2>Notes</h2>
<p>If a type contains both a value_type member and a element_type member, then the specializations <code>(5)</code> and <code>(6)</code> are ambiguous.<br />
value_type is intended for use with Readable types such as iterators. It is not intended for use with ranges. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a type is readable by applying operator *<br />
Readable (concept)<br />
iter_value_t<br />
iter_reference_t computes the associate types of an iterator<br />
iter_difference_t (alias template)<br />
iter_rvalue_reference_t<br />
iter_common_reference_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides uniform interface to the properties of an iterator<br />
iterator_traits <i>(class template)</i> </p>
