---
title: "stdexperimentalrangesfind_first_of(3)"
name: "stdexperimentalrangesfind_first_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesfind_first_of/"
description: "std::experimental::ranges::find_first_of – std::experimental::ranges::find_first_of"
---

<p>std::experimental::ranges::find_first_of &#8211; std::experimental::ranges::find_first_of</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, ForwardIterator I2, Sentinel&lt;I2&gt; S2,

class Proj1 = ranges::identity, class Proj2 = ranges::identity,

IndirectRelation&lt;projected&lt;I1, Proj1&gt;,                                            (1) (ranges TS)

projected&lt;I2, Proj2&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;

I1 find_first_of(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{},

Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template&lt; InputRange R1, ForwardRange R2,

class Proj1 = ranges::identity, class Proj2 = ranges::identity,

IndirectRelation&lt;projected&lt;ranges::iterator_t&lt;R1&gt;, Proj1&gt;,                        (2) (ranges TS)

projected&lt;ranges::iterator_t&lt;R2&gt;, Proj2&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;

ranges::safe_iterator_t&lt;R1&gt; find_first_of(R1&amp;&amp; r1, R2&amp;&amp; r2, Pred pred = Pred{},

Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});</code></pre>
<p>1) Searches the range [first1, last1) for any of the elements in the range [first2, last2), after projecting the ranges with proj1 and proj2 respectively. The projected elements are compared using pred.<br />
2) Same as <code>(1)</code>, but uses r1 as the first source range and r2 as the second source range, as if using ranges::begin(r1) as first1, ranges::end(r1) as last1, ranges::begin(r2) as first2, and ranges::end(r2) as last2. </p>
<h2>Parameters</h2>
<p>first1, last1 &#8211; the range of elements to examine<br />
r1 &#8211; the range of elements to examine<br />
first2, last2 &#8211; the range of elements to search for<br />
r2 &#8211; the range of elements to search for<br />
pred &#8211; predicate to use to compare the projected elements with<br />
proj1 &#8211; projection to apply to the elements in the first range<br />
proj2 &#8211; projection to apply to the elements in the second range</p>
<h2>Return value</h2>
<p>Iterator to the first element in the range [first1, last1) that is equal to an element from the range [first2, last2) after projection. If no such element is found, an iterator comparing equal to last1 is returned. </p>
<h2>Complexity</h2>
<p>At most (S*N) applications of the predicate and each projection, where S = distance(last2 &#8211; first2) and N = last1 &#8211; first1.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, ForwardIterator I2, Sentinel&lt;I2&gt; S2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj1 = ranges::identity, class Proj2 = ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectRelation&lt;projected&lt;I1, Proj1&gt;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;projected&lt;I2, Proj2&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;<br />
&nbsp;<wbr>&nbsp;I1 find_first_of(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{})<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first1 != last1; ++first1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (ForwardIt it = first2; it != last2; ++it) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(pred, ranges::invoke(proj1, *first1),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(proj2, *it))) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first1;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for any one of a set of elements<br />
find_first_of <i>(function template)</i><br />
find finds the first element satisfying specific criteria<br />
find_if <i>(function template)</i><br />
find_if_not </p>
