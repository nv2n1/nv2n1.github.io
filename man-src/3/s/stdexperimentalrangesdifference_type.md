---
title: "stdexperimentalrangesdifference_type(3)"
name: "stdexperimentalrangesdifference_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesdifference_type/"
---

std::experimental::ranges::difference_type - std::experimental::ranges::difference_type

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class I&gt;
    (1)

        struct difference_type {
};

template &lt;class T&gt;
(2)

    struct difference_type&lt;T *&gt;;

template &lt;class T&gt;
(3)

    struct difference_type&lt;const T&gt; : difference_type&lt;std::decay_t&lt;T&gt;&gt; {
};

template &lt;class T&gt;

requires requires
{
    typename T::difference_type;
}
(4)

    struct difference_type&lt;T&gt;;

template &lt;class T&gt;

requires !requires
{
    typename T::difference_type;
}
&amp;&amp;(5)

    requires(const T &amp;a, const T &amp;b)
{
    {
        a - b
        } -&gt; Integral;
}

struct difference_type&lt;T&gt;;</code></pre> 
Computes the associated difference type of the type I, if any. Users may specialize difference_type for a program-defined type. 
1) Primary template is an empty struct. 
2) Specialization for pointers. If T is an object type, provides a member type type equal to std::ptrdiff_t. Otherwise, there is no member type. 
3) Specialization for const-qualified types. 
4) Specialization for types that define a public and accessible member type difference_type. Provides a member type type equal to T::difference_type. 
5) Specialization for types that do not define a public and accessible member type difference_type but do support subtraction. Provides a member type type equal to std::make_signed_t&lt;decltype(std::declval&lt;T&gt;() - std::declval&lt;T&gt;())&gt;. 
Helper alias template <pre><code>template&lt; class T &gt;                                                   (ranges TS)

using difference_type_t = typename ranges::difference_type&lt;T&gt;::type;

</code></pre>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a Semiregular type can be incremented with pre- and post-increment operators 
WeaklyIncrementable (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compatibility traits class that collects an iterator’s associated types 
iterator_traits (alias template) 
