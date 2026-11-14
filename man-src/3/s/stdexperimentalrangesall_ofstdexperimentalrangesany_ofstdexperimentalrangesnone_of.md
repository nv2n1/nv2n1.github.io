---
title: "stdexperimentalrangesall_ofstdexperimentalrangesany_ofstdexperimentalrangesnone_of(3)"
name: "stdexperimentalrangesall_ofstdexperimentalrangesany_ofstdexperimentalrangesnone_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesall_ofstdexperimentalrangesany_ofstdexperimentalrangesnone_of/"
---

std::experimental::ranges::all_of,std::experimental::ranges::any_of,std::experimental::ranges::none_of - std::experimental::ranges::all_of,std::experimental::ranges::any_of,std::experimental::ranges::none_of

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;                        (1) (ranges TS)

bool all_of( I first, S last, Pred pred, Proj proj = Proj{} );

template&lt; InputRange R, class Proj = ranges::identity,

IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt;    (2) (ranges TS)

bool all_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} );

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;                        (3) (ranges TS)

bool any_of( I first, S last, Pred pred, Proj proj = Proj{} );

template&lt; InputRange R, class Proj = ranges::identity,

IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt;    (4) (ranges TS)

bool any_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} );

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = identity,

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;                        (5) (ranges TS)

bool none_of( I first, S last, Pred pred, Proj proj = Proj{} );

template&lt; InputRange R, class Proj = ranges::identity,

IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt;    (6) (ranges TS)

bool none_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} );</code></pre> 
1) Checks if unary predicate pred returns true for all elements in the range [first, last). 
3) Checks if unary predicate pred returns true for at least one element in the range [first, last). 
5) Checks if unary predicate pred returns true for no elements in the range [first, last). 
2,4,6) Same as (1,3,5), but uses r as the source range, as if using ranges::begin(r) as first and ranges::end(r) as last. 
Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable. 

<h2>Parameters</h2>

first, last - the range of the elements to examine 
r - the range of the elements to examine 
pred - predicate to apply to the projected elements 
proj - projection to apply to the elements

<h2>Return value</h2>

1-2) true if pred returns true for all elements in the range, false otherwise. Returns true if the range is empty. 
3-4) true if pred returns true for at least one element in the range, false otherwise. Returns false if the range is empty. 
5-6) true if pred returns true for no elements in the range, false otherwise. Returns true if the range is empty. 

<h2>Complexity</h2>

1-6) At most last - first applications of the predicate and last - first applications of the projection.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;bool all_of( I first, S last, Pred pred, Proj proj = Proj{} ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::find_if_not(first, last, std::ref(pred), std::ref(proj)) == last; 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template&lt; InputRange R, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;bool all_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::all_of(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;bool any_of( I first, S last, Pred pred, Proj proj = Proj{} ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::find_if(first, last, std::ref(pred), std::ref(proj)) != last; 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template&lt; InputRange R, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;bool any_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::any_of(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;bool none_of( I first, S last, Pred pred, Proj proj = Proj{} ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::find_if(first, last, std::ref(pred), std::ref(proj)) == last; 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template&lt; InputRange R, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;bool none_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::none_of(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;numeric&gt;

#include &lt;experimental/ranges/algorithm&gt;

#include &lt;experimental/ranges/iterator&gt;

#include &lt;iterator&gt;

#include &lt;iostream&gt;

#include &lt;functional&gt;
namespace ranges = std::experimental::ranges;
int main()

{
    std::vector&lt;int&gt; v(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout &lt;&lt; &quot;Among the numbers: &quot;;
    ranges::copy(v, ranges::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
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
