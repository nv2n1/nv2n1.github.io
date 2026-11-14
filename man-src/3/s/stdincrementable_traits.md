---
title: "stdincrementable_traits(3)"
name: "stdincrementable_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdincrementable_traits/"
---

std::incrementable_traits - std::incrementable_traits

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class I&gt;
    (1)(since C++ 20)

        struct incrementable_traits {
};

template &lt;class T&gt;

requires std::is_object_v&lt;T&gt;(2)
(since C++ 20)

    struct incrementable_traits&lt;T *&gt;;

template &lt;class T&gt;
(3)(since C++ 20)

    struct incrementable_traits&lt;const T&gt; : incrementable_traits&lt;T&gt; {
};

template &lt;class T&gt;

requires requires
{
    typename T::difference_type;
}
(4)(since C++ 20)

    struct incrementable_traits&lt;T&gt;;

template &lt;class T&gt;

requires(!requires { typename T::difference_type; }) &amp;&amp; (5)(since C++ 20)

                                                            requires(const T &amp;a, const T &amp;b)
{
    {
        a - b
        } -&gt; Integral;
}

struct incrementable_traits&lt;T&gt;;</code></pre> 
Computes the associated difference type of the type I, if any. Users may specialize incrementable_traits for a program-defined type. 
1) Primary template is an empty struct. 
2) Specialization for pointers. Provides a member type difference_type equal to std::ptrdiff_t. 
3) Specialization for const-qualified types. 
4) Specialization for types that define a public and accessible member type difference_type. Provides a member type difference_type equal to T::difference_type. 
5) Specialization for types that do not define a public and accessible member type difference_type but do support subtraction. Provides a member type difference_type equal to std::make_signed_t&lt;decltype(std::declval&lt;T&gt;() - std::declval&lt;T&gt;())&gt;. The implicit expression variations rule (see below) applies to the expression a - b. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a Semiregular type can be incremented with pre- and post-increment operators 
WeaklyIncrementable (concept) 
iter_value_t 
iter_reference_t computes the associate types of an iterator 
iter_difference_t (alias template) 
iter_rvalue_reference_t 
iter_common_reference_t 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides uniform interface to the properties of an iterator 
iterator_traits <i>(class template)</i> 
