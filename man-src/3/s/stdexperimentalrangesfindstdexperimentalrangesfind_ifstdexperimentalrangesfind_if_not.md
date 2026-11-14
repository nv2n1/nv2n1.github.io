---
title: "stdexperimentalrangesfindstdexperimentalrangesfind_ifstdexperimentalrangesfind_if_not(3)"
name: "stdexperimentalrangesfindstdexperimentalrangesfind_ifstdexperimentalrangesfind_if_not"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesfindstdexperimentalrangesfind_ifstdexperimentalrangesfind_if_not/"
---

std::experimental::ranges::find,std::experimental::ranges::find_if,std::experimental::ranges::find_if_not - std::experimental::ranges::find,std::experimental::ranges::find_if,std::experimental::ranges::find_if_not

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;InputIterator I, Sentinel&lt;I&gt; S, class T, class Proj = ranges::identity&gt;

requires IndirectRelation &lt; ranges::equal_to&lt;&gt;, projected&lt;I, Proj&gt;,
const T * &gt; (1)(ranges TS)

                I find(I first, S last, const T &amp;value, Proj proj = Proj{});

template &lt;InputRange R, class T, class Proj = ranges::identity&gt;

requires IndirectRelation &lt; ranges::equal_to&lt;&gt;, (2)
(ranges TS)

    projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;,
    const T * &gt;

        ranges::safe_iterator_t&lt;R&gt; find(R &amp;&amp;r, const T &amp;value, Proj proj = Proj{});

template &lt;InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred&gt;
(3)(ranges TS)

    I find_if(I first, S last, Pred pred, Proj proj = Proj{});

template &lt;InputRange R, class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred&gt;
(4)(ranges TS)

    ranges::safe_iterator_t&lt;R&gt; find_if(R &amp;&amp;r, Pred pred, Proj proj = Proj{});

template &lt;InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred&gt;
(5)(ranges TS)

    I find_if_not(I first, S last, Pred pred, Proj proj = Proj{});

template &lt;InputRange R, class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred&gt;
(6)(ranges TS)

    ranges::safe_iterator_t&lt;R&gt; find_if_not(R &amp;&amp;r, Pred pred, Proj proj = Proj{});</code></pre> 
Returns the first element in the range [first, last) that satisfies specific criteria: 
1) find searches for an element whose projected value is equal to value (i.e., value == ranges::invoke(proj, *i)). 
3) find_if searches for an element for whose projected value predicate p returns true (i.e., ranges::invoke(pred, ranges::invoke(proj, *i))) is true). 
5) find_if_not searches for an element for whose projected value predicate q returns false (i.e., ranges::invoke(pred, ranges::invoke(proj, *i))) is false). 
2,4,6) Same as (1,3,5), but uses r as the source range, as if using ranges::begin(r) as first and ranges::end(r) as last. 
Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable. 

<h2>Parameters</h2>

first, last - the range of elements to examine 
r - the range of elements to examine 
value - value to compare the projected elements to 
pred - predicate to apply to the projected elements 
proj - projection to apply to the elements

<h2>Return value</h2>

Iterator to the first element satisfying the condition. If no such element is found, returns an iterator that compares equal to last. 

<h2>Complexity</h2>

At most last - first applications of the predicate and projection.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class T, class Proj = ranges::identity &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectRelation&lt;ranges::equal_to&lt;&gt;, projected&lt;I, Proj&gt;, const T*&gt; 
&nbsp;<wbr>&nbsp;I find(I first, S last, const T&amp; value, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(proj, *first) == value) break; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;I find_if(I first, S last, Pred pred, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(pred, ranges::invoke(proj, *first))) break; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;I find_if_not(I first, S last, Pred pred, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!ranges::invoke(pred, ranges::invoke(proj, *first))) break; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

find 
find_if 
find_if_not finds the first element satisfying specific criteria 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first two adjacent items that are equal (or satisfy a given predicate) 
adjacent_find <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last sequence of elements in a certain range 
find_end <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for any one of a set of elements 
find_first_of <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first position where two ranges differ 
mismatch <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
