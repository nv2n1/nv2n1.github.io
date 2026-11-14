---
title: "stdexperimentalrangescountstdexperimentalrangescount_if(3)"
name: "stdexperimentalrangescountstdexperimentalrangescount_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescountstdexperimentalrangescount_if/"
---

std::experimental::ranges::count,std::experimental::ranges::count_if - std::experimental::ranges::count,std::experimental::ranges::count_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;InputIterator I, Sentinel&lt;I&gt; S, class T, class Proj = ranges::identity&gt;

requires IndirectRelation &lt; ranges::equal_to&lt;&gt;, projected&lt;I, Proj&gt;,
const T * &gt; (1)(ranges TS)

                ranges::difference_type_t&lt;I&gt; count(I first, S last, const T &amp;value, Proj proj = Proj{});

template &lt;InputRange R, class T, class Proj = ranges::identity&gt;

requires IndirectRelation &lt; ranges::equal_to&lt;&gt;,

    projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;,
const T * &gt; (2)(ranges TS)

                ranges::difference_type_t&lt;ranges::iterator_t&lt;R&gt;&gt;

    count(R &amp;&amp;r, const T &amp;value, Proj proj = Proj{});

template &lt;InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred&gt;
(3)(ranges TS)

    ranges::difference_type_t&lt;I&gt; count_if(I first, S last, Pred pred, Proj proj = Proj{});

template &lt;InputRange R, class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred&gt;
(4)(ranges TS)

    ranges::difference_type_t&lt;ranges::iterator_t&lt;R&gt;&gt;

    count_if(R &amp;&amp;r, Pred pred, Proj proj = Proj{});</code></pre> 
Returns the number of elements in the range [first, last) satisfying specific criteria. 
1) counts the elements whose projected values are equal to value (i.e., ranges::invoke(proj, *i) == value). 
3) counts the elements whose projected values satisfy the predicate pred (i.e., ranges::invoke(pred, ranges::invoke(proj, *i)) != false). 
2,4) Same as (1,3), but uses r as the source range, as if using ranges::begin(r) as first and ranges::end(r) as last. 
Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable. 

<h2>Parameters</h2>

first, last - the range of elements to examine 
r - the range of elements to examine 
value - the value to search for 
pred - predicate to apply to the projected elements 
proj - projection to apply to the elements

<h2>Return value</h2>

number of elements satisfying the condition. 

<h2>Complexity</h2>

exactly last - first comparisons / applications of the predicate, and the same number of applications of the projection.

<h2>Notes</h2>

For the number of elements in the range [first, last) without any additional criteria, see ranges::distance. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class T, class Proj = ranges::identity &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectRelation&lt;ranges::equal_to&lt;&gt;, projected&lt;I, Proj&gt;, const T*&gt; 
&nbsp;<wbr>&nbsp;ranges::difference_type_t&lt;I&gt; count(I first, S last, const T&amp; value, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::difference_type_t&lt;I&gt; ret = 0; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(proj, *first) == value) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++ret; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ret; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt; 
&nbsp;<wbr>&nbsp;ranges::difference_type_t&lt;I&gt; count_if(I first, S last, Pred pred, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::difference_type_t&lt;I&gt; ret = 0; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(pred, ranges::invoke(proj, *i))) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++ret; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ret; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of elements satisfying specific criteria 
count <i>(function template)</i> 
count_if 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between an iterator and a sentinel, or between the beginning and the end of a range 
distance <i>(function template)</i> 
