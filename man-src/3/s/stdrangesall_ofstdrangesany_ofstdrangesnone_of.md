---
title: "stdrangesall_ofstdrangesany_ofstdrangesnone_of(3)"
name: "stdrangesall_ofstdrangesany_ofstdrangesnone_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesall_ofstdrangesany_ofstdrangesnone_of/"
---

std::ranges::all_of,std::ranges::any_of,std::ranges::none_of - std::ranges::all_of,std::ranges::any_of,std::ranges::none_of

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

Call signature

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = std::identity,

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;                     (1) (since C++20)

bool all_of( I first, S last, Pred pred, Proj proj = {} );

template&lt; InputRange R, class Proj = std::identity,

IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; (2) (since C++20)

bool all_of( R&amp;&amp; r, Pred pred, Proj proj = {} );

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = std::identity,

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;                     (3) (since C++20)

bool any_of( I first, S last, Pred pred, Proj proj = {} );

template&lt; InputRange R, class Proj = std::identity,

IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; (4) (since C++20)

bool any_of( R&amp;&amp; r, Pred pred, Proj proj = {} );

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = std::identity,

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;                     (5) (since C++20)

bool none_of( I first, S last, Pred pred, Proj proj = {} );

template&lt; InputRange R, class Proj = std::identity,

IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; (6) (since C++20)

bool none_of( R&amp;&amp; r, Pred pred, Proj proj = {} );</code></pre> 
1) Checks if unary predicate pred returns true for all elements in the range [first, last) (after projecting with the projection proj). 
3) Checks if unary predicate pred returns true for at least one element in the range [first, last) (after projecting with the projection proj). 
5) Checks if unary predicate pred returns true for no elements in the range [first, last) (after projecting with the projection proj). 
2,4,6) Same as (1,3,5), but uses r as the source range, as if using ranges::begin(r) as first and ranges::end(r) as last. 
The function-like entities described on this page are niebloids, that is: 
* Explicit template argument lists may not be specified when calling any of them. 
* None of them is visible to argument-dependent_lookup. 
* When one of them is found by normal_unqualified_lookup for the name to the left of the function-call operator, it inhibits argument-dependent_lookup. 
In practice, they may be implemented as function objects, or with special compiler extensions. 

<h2>Parameters</h2>

first, last - the range of the elements to examine 
r - the range of the elements to examine 
pred - predicate to apply to the projected elements 
proj - projection to apply to the elements

<h2>Return value</h2>

1-2) true if std::invoke(pred, std::invoke(proj, *i)) != false for every iterator i in the range, false otherwise. Returns true if the range is empty. 
3-4) true if std::invoke(pred, std::invoke(proj, *i)) != false for at least one iterator i in the range, false otherwise. Returns false if the range is empty. 
5-6) true if std::invoke(pred, std::invoke(proj, *i)) == false for every iterator i in the range, false otherwise. Returns true if the range is empty. 

<h2>Complexity</h2>

At most last - first applications of the predicate and the projection.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;struct all_of_fn { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = std::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator()( I first, S last, Pred pred, Proj proj = {} ) const 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::find_if_not(first, last, std::ref(pred), std::ref(proj)) == last; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputRange R, class Proj = std::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator()( R&amp;&amp; r, Pred pred, Proj proj = {} ) const 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return operator()(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;inline constexpr all_of_fn all_of;

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;struct any_of_fn { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = std::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator()( I first, S last, Pred pred, Proj proj = {} ) const 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::find_if(first, last, std::ref(pred), std::ref(proj)) != last; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputRange R, class Proj = std::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator()( R&amp;&amp; r, Pred pred, Proj proj = {} ) const 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return operator()(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;inline constexpr any_of_fn any_of; 

 
Third version 

 
&nbsp;<wbr>&nbsp;struct none_of_fn { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = std::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator()( I first, S last, Pred pred, Proj proj = {} ) const 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::find_if(first, last, std::ref(pred), std::ref(proj)) == last; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputRange R, class Proj = std::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator()( R&amp;&amp; r, Pred pred, Proj proj = {} ) const 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return operator()(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;inline constexpr none_of_fn none_of;

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;numeric&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;

#include &lt;iterator&gt;

#include &lt;iostream&gt;

#include &lt;functional&gt;
namespace ranges = std::ranges;
int main()

{
    std::vector&lt;int&gt; v(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout &lt;&lt; &quot;Among the numbers: &quot;;
    ranges::copy(v, std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
    if (ranges::all_of(v.cbegin(), v.cend(), [](int i) { return i % 2 == 0; })) {
        std::cout &lt;&lt; &quot;All numbers are even\n&quot;;
    }
    if (ranges::none_of(v, std::bind(std::modulus&lt;int&gt;(), std::placeholders::_1, 2))) {
        std::cout &lt;&lt; &quot;None of them are odd\n&quot;;
    }
    struct DivisibleBy {
        const int d;
        DivisibleBy(int n)
            : d(n)
        {
        }
        bool operator()(int n) const
        {
            return n % d == 0;
        }
    };
    if (ranges::any_of(v, DivisibleBy(7))) {
        std::cout &lt;&lt; &quot;At least one number is divisible by 7\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Among the numbers: 2 4 6 8 10 12 14 16 18 20 
&nbsp;<wbr>&nbsp;All numbers are even 
&nbsp;<wbr>&nbsp;None of them are odd 
&nbsp;<wbr>&nbsp;At least one number is divisible by 7

<h2>See also</h2>

all_of 
any_of 
none_of checks if a predicate is true for all, any or none of the elements in a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
