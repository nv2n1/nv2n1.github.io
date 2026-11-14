---
title: "stdexperimentalrangesiterator_category(3)"
name: "stdexperimentalrangesiterator_category"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesiterator_category/"
---

std::experimental::ranges::iterator_category - std::experimental::ranges::iterator_category

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class I&gt;
    (1)

        struct iterator_category {
};

template &lt;class T&gt;
(2)

    struct iterator_category&lt;T *&gt;;

template &lt;class T&gt;
(3)

    struct iterator_category&lt;const T&gt; : iterator_category&lt;T&gt; {
};

template &lt;class T&gt;

requires requires
{
    typename T::iterator_category;
}
(4)

    struct iterator_category&lt;T&gt;;</code></pre> 
Computes the iterator category of the class I, if any. Users may specialize iterator_category for a program-defined type. 
1) Primary template is an empty struct. 
2) Specialization for pointers. If T is an object type, provides a member type type equal to ranges::random_access_iterator_tag. Otherwise, there is no member type. 
3) Specialization for const-qualified types. 
4) Specialization for types that define a public and accessible member type iterator_category. If T::iterator_category is the same as or derived from one of iterator category tags in namespace std, it is mapped to the corresponding tag in the namespace ranges as described below. Otherwise, provides a member type type equal to T::iterator_category. 
* If T::iterator_category is the same as or derives from std::random_access_iterator_tag, provides a member type type equal to ranges::random_access_iterator_tag. 
* Otherwise, if T::iterator_category is the same as or derives from std::bidirectional_iterator_tag, provides a member type type equal to ranges::bidirectional_iterator_tag. 
* Otherwise, if T::iterator_category is the same as or derives from std::forward_iterator_tag, provides a member type type equal to ranges::forward_iterator_tag. 
* Otherwise, if T::iterator_category is the same as or derives from std::input_iterator_tag, provides a member type type equal to ranges::input_iterator_tag. 
* Otherwise, if T::iterator_category is the same as or derives from std::output_iterator_tag, there is no member type. 
Helper alias template <pre><code>template&lt; class T &gt;                                                       (ranges TS)

using iterator_category_t = typename ranges::iterator_category&lt;T&gt;::type;

</code></pre>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

input_iterator_tag 
output_iterator_tag 
forward_iterator_tag 
bidirectional_iterator_tag 
random_access_iterator_tag 
contiguous_iterator_tag empty class types used to indicate iterator categories 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
input_iterator_tag 
output_iterator_tag empty class types used to indicate iterator categories 
forward_iterator_tag <i>(class)</i> 
bidirectional_iterator_tag 
random_access_iterator_tag 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compatibility traits class that collects an iterator’s associated types 
iterator_traits (alias template) 
