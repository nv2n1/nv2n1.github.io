---
title: "stdexperimentalrangeslexicographical_compare(3)"
name: "stdexperimentalrangeslexicographical_compare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangeslexicographical_compare/"
description: "std::experimental::ranges::lexicographical_compare – std::experimental::ranges::lexicographical_compare"
---

<p>std::experimental::ranges::lexicographical_compare &#8211; std::experimental::ranges::lexicographical_compare</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I2&gt; S2,

class Proj1 = ranges::identity, class Proj2 = ranges::identity,

class Comp = ranges::less&lt;&gt; &gt;

requires IndirectStrictWeakOrder&lt;Comp, projected&lt;I1, Proj1&gt;, projected&lt;I2, Proj2&gt;&gt; (1) (ranges TS)

bool lexicographical_compare(I1 first1, S1 last1, I2 first2, S2 last2,

Comp comp = Comp{},

Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template&lt; InputRange R1, InputRange R2,

class Proj1 = ranges::identity, class Proj2 = ranges::identity,

class Comp = ranges::less&lt;&gt; &gt;

requires IndirectStrictWeakOrder&lt;Comp, projected&lt;ranges::iterator_t&lt;R1&gt;, Proj1&gt;,   (2) (ranges TS)

projected&lt;ranges::iterator_t&lt;R2&gt;, Proj2&gt;&gt;

bool lexicographical_compare(R1&amp;&amp; r1, R2&amp;&amp; r2, Comp comp = Comp{},

Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});</code></pre>
<p>1) Checks if the first range [first1, last1) is lexicographically less than the second range [first2, last2). Elements are compared using the given binary comparison function comp, after being projected with proj1 and proj2 respectively.<br />
2) Same as <code>(1)</code>, but uses r1 as the first source range and r2 as the second source range, as if using ranges::begin(r1) as first1, ranges::end(r1) as last1, ranges::begin(r2) as first2, and ranges::end(r2) as last2.<br />
Lexicographical comparison is a operation with the following properties:<br />
* Two ranges are compared element by element.<br />
* The first mismatching element defines which range is lexicographically less or greater than the other.<br />
* If one range is a prefix of another, the shorter range is lexicographically less than the other.<br />
* If two ranges have equivalent elements and are of the same length, then the ranges are lexicographically equal.<br />
* An empty range is lexicographically less than any non-empty range.<br />
* Two empty ranges are lexicographically equal. </p>
<h2>Parameters</h2>
<p>first1, last1 &#8211; the first range of elements to examine<br />
r1 &#8211; the first range of elements to examine<br />
first2, last2 &#8211; the second range of elements to examine<br />
r2 &#8211; the second range of elements to examine<br />
comp &#8211; comparison function to apply to the projected elements<br />
proj1 &#8211; projection to apply to the elements in the first range<br />
proj2 &#8211; projection to apply to the elements in the second range</p>
<h2>Return value</h2>
<p>true if the first range is lexicographically less than the second. </p>
<h2>Complexity</h2>
<p>At most 2·min(N1, N2) applications of the comparison operation, where N1 = last1 &#8211; first1 and N2 = last2 &#8211; first2.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I2&gt; S2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj1 = ranges::identity, class Proj2 = ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Comp = ranges::less&lt;&gt; &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectStrictWeakOrder&lt;Comp, projected&lt;I1, Proj1&gt;, projected&lt;I2, Proj2&gt;&gt;<br />
&nbsp;<wbr>&nbsp;bool lexicographical_compare(I1 first1, S1 last1, I2 first2, S2 last2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Comp comp = Comp{},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{})<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for ( ; (first1 != last1) &amp;&amp; (first2 != last2); (void) ++first1, (void) ++first2 ) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(comp, ranges::invoke(proj1, *first1),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(proj2, *first2))) return true;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(comp, ranges::invoke(proj2, *first2),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(proj1, *first1))) return false;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (first1 == last1) &amp;&amp; (first2 != last2);<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns true if one range is lexicographically less than another<br />
lexicographical_compare <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines if two sets of elements are the same<br />
equal <i>(function template)</i> </p>
