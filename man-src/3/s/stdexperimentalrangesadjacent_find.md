---
title: "stdexperimentalrangesadjacent_find(3)"
name: "stdexperimentalrangesadjacent_find"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesadjacent_find/"
description: "std::experimental::ranges::adjacent_find – std::experimental::ranges::adjacent_find"
---

<p>std::experimental::ranges::adjacent_find &#8211; std::experimental::ranges::adjacent_find</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; ForwardIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

IndirectRelation&lt;projected&lt;I, Proj&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;                         (1) (ranges TS)

I adjacent_find(I first, S last, Pred pred = Pred{}, Proj proj = Proj{});

template&lt; ForwardRange R, class Proj = ranges::identity,

IndirectRelation&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;     (2) (ranges TS)

ranges::safe_iterator_t&lt;R&gt; adjacent_find(R&amp;&amp; r, Pred pred = Pred{}, Proj proj = Proj{});</code></pre>
<p>1) Searches the range [first, last) for two consecutive identical elements. Elements are compared using pred after being projected with proj.<br />
2) Same as <code>(1)</code>, but uses r as the source range, as if using ranges::begin(r) as first and ranges::end(r) as last.<br />
Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to examine<br />
r &#8211; the range of elements to examine<br />
pred &#8211; predicate to use to compare the projected elements<br />
proj &#8211; projection to apply to the elements</p>
<h2>Return value</h2>
<p>An iterator to the first of the first pair of identical elements, that is, the first iterator i such that both i and i + 1 are in the range [first, last) and ranges::invoke(pred, ranges::invoke(proj, *i), ranges::invoke(proj, *(i + 1))) != false.<br />
If no such elements are found, an iterator that compares equal to last is returned. </p>
<h2>Complexity</h2>
<p>If the range is nonempty, exactly min((result-first)+1, (last-first)-1) applications of the predicate where result is the return value, and at most twice as many applications of the projection.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; ForwardIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectRelation&lt;projected&lt;I, Proj&gt;&gt; Pred = ranges::equal_to&lt;&gt; &gt;<br />
&nbsp;<wbr>&nbsp;I adjacent_find(I first, S last, Pred pred = Pred{}, Proj proj = Proj{})<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;I next = first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++next;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while(next != last) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(pred, ranges::invoke(proj, *first),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(proj, *next))) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++next;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return next;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first two adjacent items that are equal (or satisfy a given predicate)<br />
adjacent_find <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes consecutive duplicate elements in a range<br />
unique <i>(function template)</i> </p>
