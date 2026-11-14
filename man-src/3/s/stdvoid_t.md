---
title: "stdvoid_t(3)"
name: "stdvoid_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvoid_t/"
---

std::void_t - std::void_t

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class...&gt;
    (since C++ 17)

        using void_t = void;</code></pre> 
Utility metafunction that maps a sequence of any types to the type void 

<h2>Notes</h2>

This metafunction is used in template metaprogramming to detect ill-formed types in SFINAE context: template &lt;typename... Ts&gt;
struct make_void {
    typedef void type;
};

template &lt;typename... Ts&gt;
using void_t = typename make_void&lt;Ts...&gt;::type;
 
It can also be used to detect validity of an expression: // primary template handles types that do not support pre-increment:

template &lt;class, class = std::void_t&lt;&gt;&gt;

struct has_pre_increment_member : std::false_type {
};

// specialization recognizes types that do support pre-increment:

template &lt;class T&gt;

struct has_pre_increment_member&lt;T,
                                std::void_t&lt;decltype(++std::declval&lt;T &amp;&gt;())&gt;&gt; : std::true_type {
}; 
Until CWG_1558 (a C++14 defect), unused parameters in alias_templates were not guaranteed to ensure SFINAE and could be ignored, so earlier compilers require a more complex definition of void_t, such as template &lt;typename... Ts&gt;
struct make_void {
    typedef void type;
};

template &lt;typename... Ts&gt;
using void_t = typename make_void&lt;Ts...&gt;::type;


<h2>Examples</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;vector&gt;

#include &lt;map&gt;
class A
{
};
template &lt;typename T, typename = void&gt;

struct is_iterable : std::false_type {
};

template &lt;typename T&gt;

struct is_iterable&lt;T, std::void_t&lt;decltype(std::declval&lt;T&gt;().begin()),
                                  decltype(std::declval&lt;T&gt;().end())&gt;&gt;
    : std::true_type {
}; 
&nbsp;<wbr>&nbsp;// An iterator trait which value_type is always the value_type of the 
&nbsp;<wbr>&nbsp;// iterated container, even with back_insert_iterator which value_type is void <pre><code>template &lt;typename T, typename = void&gt;

struct iterator_trait

    : std::iterator_traits&lt;T&gt; {
};

template &lt;typename T&gt;

struct iterator_trait&lt;T, std::void_t&lt;typename T::container_type&gt;&gt;

    : std::iterator_traits&lt;typename T::container_type::iterator&gt; {
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; is_iterable&lt;std::vector&lt;double&gt;&gt;::value &lt;&lt; '\n';
    std::cout &lt;&lt; is_iterable&lt;std::map&lt;int, double&gt;&gt;::value &lt;&lt; '\n';
    std::cout &lt;&lt; is_iterable&lt;double&gt;::value &lt;&lt; '\n';
    std::cout &lt;&lt; is_iterable&lt;A&gt;::value &lt;&lt; '\n';

    std::vector&lt;int&gt; v;
    std::cout &lt;&lt; std::is_same&lt;iterator_trait&lt;decltype(std::back_inserter(v))&gt;::value_type, iterator_trait&lt;decltype(v.cbegin())&gt;::value_type&gt;::value &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;true

<h2>See also</h2>

enable_if hides a function overload or template specialization based on compile-time boolean 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
