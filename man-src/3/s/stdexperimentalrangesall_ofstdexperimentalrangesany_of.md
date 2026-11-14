---
title: "stdexperimentalrangesall_ofstdexperimentalrangesany_of(3)"
name: "stdexperimentalrangesall_ofstdexperimentalrangesany_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesall_ofstdexperimentalrangesany_of/"
description: "std::experimental::ranges::all_of,std::experimental::ranges::any_of, – std::experimental::ranges::all_of,std::experimental::ranges::any_of,"
---

<p>std::experimental::ranges::all_of,std::experimental::ranges::any_of, &#8211; std::experimental::ranges::all_of,std::experimental::ranges::any_of,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj =

ranges::identity,
(1) (ranges TS)

IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;
bool all_of( I first, S last, Pred pred, Proj proj = Proj{} );

template&lt; InputRange R, class Proj = ranges::identity,</code></pre>
<p>IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr>(ranges TS)<br />
&gt; bool all_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} );</p>
<p>template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj =</p>
<p>ranges::identity,<br />
(3) (ranges TS)</p>
<p>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;<br />
bool any_of( I first, S last, Pred pred, Proj proj = Proj{} );</p>
<p>template&lt; InputRange R, class Proj = ranges::identity,<br />
IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr>(ranges TS)<br />
&gt; bool any_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} );</p>
<p>template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = identity,<br />
IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(5)</code>&nbsp;<wbr>(ranges TS) bool none_of( I first, S last, Pred pred, Proj proj = Proj{} );</p>
<p>template&lt; InputRange R, class Proj = ranges::identity,<br />
IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&nbsp;<wbr><code>(6)</code>&nbsp;<wbr>(ranges TS)<br />
&gt; bool none_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} );<br />
1)&nbsp;<wbr>Checks if unary predicate pred returns true for all elements in the range&nbsp;<wbr>[first,<br />
last).<br />
3)&nbsp;<wbr>Checks if unary predicate pred returns true for at least one element in the range<br />
[first, last).<br />
5)&nbsp;<wbr>Checks if unary predicate pred returns true for no elements in the range&nbsp;<wbr>[first,<br />
last).<br />
2,4,6)&nbsp;<wbr>Same as&nbsp;<wbr>(1,3,5), but uses r as the source range, as if using ranges::begin(r)<br />
as first and ranges::end(r)&nbsp;<wbr>as last.<br />
Notwithstanding the declarations depicted above, the actual number and order of<br />
template parameters for algorithm declarations is unspecified. Thus, if explicit<br />
template arguments are used when calling an algorithm, the program is probably<br />
non-portable. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of the elements to examine<br />
r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the range of the elements to examine<br />
pred&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; predicate to apply to the projected elements<br />
proj&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; projection to apply to the elements</p>
<h2>Return value</h2>
<p>1-2)&nbsp;<wbr>true if pred returns true for all elements in the range, false otherwise.<br />
Returns true if the range is empty.<br />
3-4)&nbsp;<wbr>true if pred returns true for at least one element in the range, false<br />
otherwise. Returns false if the range is empty.<br />
5-6)&nbsp;<wbr>true if pred returns true for no elements in the range, false otherwise.<br />
Returns true if the range is empty. </p>
<h2>Complexity</h2>
<p>1-6)&nbsp;<wbr>At most last &#8211; first applications of the predicate and last &#8211; first<br />
applications of the projection.</p>
<h2>Possible implementation</h2>
<h2>First version</h2>
<p>template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,<br />
&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt; bool all_of( I first, S last, Pred pred, Proj proj = Proj{} ) {<br />
return ranges::find_if_not(first, last, std::ref(pred), std::ref(proj))&nbsp;<wbr>==&nbsp;<wbr>last; } </p>
<p> template&lt; InputRange R, class Proj = ranges::identity,<br />
&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt; bool all_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} ) {<br />
return ranges::all_of(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); }</p>
<h2>Second version</h2>
<p>template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,<br />
&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt; bool any_of( I first, S last, Pred pred, Proj proj = Proj{} ) {<br />
return ranges::find_if(first, last, std::ref(pred), std::ref(proj))&nbsp;<wbr>!=&nbsp;<wbr>last; } </p>
<p> template&lt; InputRange R, class Proj = ranges::identity,<br />
IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt; bool any_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} ) {<br />
return ranges::any_of(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); }<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Third version template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = identity,<br />
&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt; bool none_of( I first, S last, Pred pred, Proj proj = Proj{} ) {<br />
return ranges::find_if(first, last, std::ref(pred), std::ref(proj))&nbsp;<wbr>==&nbsp;<wbr>last; } </p>
<p> template&lt; InputRange R, class Proj = ranges::identity,<br />
&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt; bool none_of( R&amp;&amp; r, Pred pred, Proj proj = Proj{} ) {<br />
return ranges::none_of(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj)); }</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;vector&gt;

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
    std::cout &lt;&lt; '
';
    if (ranges::all_of(v.cbegin(), v.cend(), [](int i) { return i % 2 == 0; })) {

        std::cout &lt;&lt; &quot;All numbers are even
&quot;;
    }
    if (ranges::none_of(v, std::bind(std::modulus&lt;int&gt;(), std::placeholders::_1, 2))) {

        std::cout &lt;&lt; &quot;None of them are odd
&quot;;
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

        std::cout &lt;&lt; &quot;At least one number is divisible by 7
&quot;;
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>Among the numbers: 2 4 6 8 10 12 14 16 18 20<br />
&nbsp;<wbr>All numbers are even<br />
&nbsp;<wbr>None of them are odd<br />
&nbsp;<wbr>At least one number is divisible by 7</p>
<h2>See also</h2>
<p>all_of<br />
any_of&nbsp;<wbr>&nbsp;<wbr>checks if a predicate is true for all, any or none of the elements in a<br />
none_of range<br />
<i>(C++11)</i>&nbsp;<wbr><i>(function template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
