---
title: "stditerator_traits(3)"
name: "stditerator_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stditerator_traits/"
---

std::iterator_traits - std::iterator_traits

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class Iter&gt;

    struct iterator_traits;

template &lt;class T&gt;

struct iterator_traits&lt;T *&gt;;

template &lt;class T&gt;
(until C++ 20)

    struct iterator_traits&lt;const T *&gt;;</code></pre> 
std::iterator_traits is the type trait class that provides uniform interface to the properties of LegacyIterator types. This makes it possible to implement algorithms only in terms of iterators. 
The class defines the following types: 
* difference_type - a signed integer type that can be used to identify distance between iterators 
* value_type - the type of the values that can be obtained by dereferencing the iterator. This type is void for output iterators. 
* pointer - defines a pointer to the type iterated over (value_type) 
* reference - defines a reference to the type iterated over (value_type) 
* iterator_category - the category of the iterator. Must be one of iterator_category_tags. 
The template can be specialized for user-defined iterators so that the information about the iterator can be retrieved even if the type does not provide the usual typedefs. 
User specializations may define the member type iterator_concept to one of iterator_category_tags, to indicate conformance to the iterator concepts. <i>(since C++20)</i> 

<h2>Template parameters</h2>

Iter - the iterator type to retrieve properties for

<h2>Member types</h2>

Member type Definition 
difference_type Iter::difference_type 
value_type Iter::value_type 
pointer Iter::pointer 
reference Iter::reference 
iterator_category Iter::iterator_category 

 

 
If Iter does not have all five member types difference_type, value_type, pointer, reference, and iterator_category, then this template has no members by any of those names (std::iterator_traits is SFINAE-friendly) <i>(since C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i> 
If Iter does not have pointer, but has all other four member types, then the member types are declared as follows: 

 
Member type Definition 
difference_type Iter::difference_type 
value_type Iter::value_type 
pointer void 
reference Iter::reference 
iterator_category Iter::iterator_category 

 
Otherwise, if Iter satisfies the exposition-only concept __LegacyInputIterator, the member types are declared as follows: 

 
Member type Definition 
difference_type std::incrementable_traits&lt;Iter&gt;::difference_type 
value_type std::readable_traits&lt;Iter&gt;::value_type 
pointer Iter::pointer if valid, otherwise decltype(std::declval&lt;Iter&amp;&gt;().operator-&gt;()) if valid, otherwise void 
reference Iter::reference if valid, otherwise std::iter_reference_t&lt;Iter&gt; <i>(since C++20)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Iter::iterator_category if valid, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;otherwise, std::random_access_iterator_tag if Iter satisfies __LegacyRandomAccessIterator, 
iterator_category otherwise, std::bidirectional_iterator_tag if Iter satisfies __LegacyBidirectionalIterator, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;otherwise, std::forward_iterator_tag if Iter satisfies __LegacyForwardIterator, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;otherwise, std::input_iterator_tag 

 
Otherwise, if Iter satisfies the exposition-only concept __LegacyIterator, the member types are declared as follows: 

 
Member type Definition 
difference_type std::incrementable_traits&lt;Iter&gt;::difference_type if valid, otherwise void 
value_type void 
pointer void 
reference void 
iterator_category std::output_iterator_tag 

 
Otherwise, this template has no members by any of those names (std::iterator_traits is SFINAE-friendly).

<h2>Specializations</h2>

This type trait may be specialized for user-provided types that may be used as iterators. The standard library provides two partial specializations for pointer types T*, which makes it possible to use all iterator-based algorithms with raw pointers.

<h2>T* specialization member types</h2>

Only specialized if std::is_object_v&lt;T&gt; is true. <i>(since C++20)</i> 

 

 
Member type Definition 
difference_type std::ptrdiff_t 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;T 
value_type <i>(until C++20)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::remove_cv_t&lt;T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i> 
pointer T* 
reference T&amp; 
iterator_category std::random_access_iterator_tag 
iterator_concept<i>(since C++20)</i> std::contiguous_iterator_tag

<h2>const T* specialization member types</h2>

Member type Definition 
difference_type std::ptrdiff_t <i>(until C++20)</i> 
value_type T 
pointer const T* 
reference const T&amp; 
iterator_category std::random_access_iterator_tag

<h2>Example</h2>

The following example shows a general-purpose reverse() implementation for bidirectional iterators 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;

#include &lt;list&gt;
template &lt;class BidirIt&gt;

void my_reverse(BidirIt first, BidirIt last)

{
    typename std::iterator_traits&lt;BidirIt&gt;::difference_type n = std::distance(first, last);
    --n;
    while (n &gt; 0) {
        typename std::iterator_traits&lt;BidirIt&gt;::value_type tmp = *first;
        *first++ = *--last;
        *last = tmp;
        n -= 2;
    }
}
int main()

{
    std::vector&lt;int&gt; v{1, 2, 3, 4, 5};
    my_reverse(v.begin(), v.end());
    for (int n : v) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
    std::list&lt;int&gt; l{1, 2, 3, 4, 5};
    my_reverse(l.begin(), l.end());
    for (auto n : l) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
    int a[] = {1, 2, 3, 4, 5};
    my_reverse(a, a + 5);
    for (int i = 0; i &lt; 5; ++i) {
        std::cout &lt;&lt; a[i] &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
    //    std::istreambuf_iterator&lt;char&gt; i1(std::cin), i2;

    //    my_reverse(i1, i2); // compilation error
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;5 4 3 2 1 
&nbsp;<wbr>&nbsp;5 4 3 2 1 
&nbsp;<wbr>&nbsp;5 4 3 2 1

<h2>See also</h2>

iterator base class to ease the definition of required types for simple iterators 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++17) 
input_iterator_tag 
output_iterator_tag 
forward_iterator_tag 
bidirectional_iterator_tag 
random_access_iterator_tag 
contiguous_iterator_tag empty class types used to indicate iterator categories 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
