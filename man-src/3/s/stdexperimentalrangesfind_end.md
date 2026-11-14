---
title: "stdexperimentalrangesfind_end(3)"
name: "stdexperimentalrangesfind_end"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesfind_end/"
description: "std::experimental::ranges::find_end – std::experimental::ranges::find_end"
---

<p>std::experimental::ranges::find_end &#8211; std::experimental::ranges::find_end</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; ForwardIterator I1, Sentinel&lt;I1&gt; S1, ForwardIterator I2, Sentinel&lt;I2&gt; S2,

class Proj = ranges::identity,

IndirectRelation&lt;I2, projected&lt;I1, Proj&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;               (1) (ranges TS)

I1 find_end(I1 first1, S1 last1, I2 first2, S2 last2,

Pred pred = Pred{}, Proj proj = Proj{});

template&lt; ForwardRange R1, ForwardRange R2, class Proj = ranges::identity,

IndirectRelation&lt;ranges::iterator_t&lt;R2&gt;,

projected&lt;ranges::iterator_t&lt;R1&gt;, Proj&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;                (2) (ranges TS)

ranges::safe_iterator_t&lt;R1&gt; find_end(Rng1&amp;&amp; rng1, Rng2&amp;&amp; rng2,

Pred pred = Pred{}, Proj proj = Proj{});</code></pre>
<p>1) Searches for the last occurrence of the sequence [first2, last2) in the range [first1, last1) (after projection with proj).<br />
2) Same as <code>(1)</code>, but uses r1 as the first source range and r2 as the second source range, as if using ranges::begin(r1) as first1, ranges::end(r1) as last1, ranges::begin(r2) as first2, and ranges::end(r2) as last2.<br />
Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable. </p>
<h2>Parameters</h2>
<p>first1, last1 &#8211; the range of elements to examine<br />
r1 &#8211; the range of elements to examine<br />
first2, last2 &#8211; the range of elements to search for<br />
r2 &#8211; the range of elements to search for<br />
pred &#8211; predicate to compare the elements<br />
proj &#8211; projection to apply to the elements in the first range</p>
<h2>Return value</h2>
<p>Iterator to the beginning of last occurrence of the sequence [first2, last2) in range [first1, last1) (after projection with proj).<br />
If [first2, last2) is empty or if no such sequence is found, an iterator that compares equal to last1 is returned. </p>
<h2>Complexity</h2>
<p>At most S*(N-S+1) applications of the predicate and projection, where S = last2 &#8211; first2 and N = last1 &#8211; first1.</p>
<h2>Notes</h2>
<p>The projection is only applied to the range [first1, last1). </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; ForwardIterator I1, Sentinel&lt;I1&gt; S1, ForwardIterator I2, Sentinel&lt;I2&gt; S2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj = ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectRelation&lt;I2, projected&lt;I1, Proj&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;<br />
&nbsp;<wbr>&nbsp;I1 find_end(I1 first1, S1 last1, I2 first2, S2 last2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pred pred = Pred{}, Proj proj = Proj{})<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;I1 result = ranges::next(first1, last1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first2 == last2)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return result;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (true) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;I1 new_result = ranges::search(first1, last1, first2, last2, pred, proj);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (new_result == last1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} else {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;result = new_result;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first1 = result;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return result;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last sequence of elements in a certain range<br />
find_end <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements<br />
search <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns true if one set is a subset of another<br />
includes <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first two adjacent items that are equal (or satisfy a given predicate)<br />
adjacent_find <i>(function template)</i><br />
find finds the first element satisfying specific criteria<br />
find_if <i>(function template)</i><br />
find_if_not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for any one of a set of elements<br />
find_first_of <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a number consecutive copies of an element in a range<br />
search_n <i>(function template)</i> </p>
