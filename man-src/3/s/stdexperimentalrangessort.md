---
title: "stdexperimentalrangessort(3)"
name: "stdexperimentalrangessort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessort/"
description: "std::experimental::ranges::sort – std::experimental::ranges::sort"
---

<p>std::experimental::ranges::sort &#8211; std::experimental::ranges::sort</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;RandomAccessIterator I, Sentinel&lt;I&gt; S,

              class Comp = ranges::less&lt;&gt;, class Proj = ranges::identity&gt;
    (1)(ranges TS)

        requires Sortable&lt;I, Comp, Proj&gt;

    I sort(I first, S last, Comp comp = Comp{}, Proj proj = Proj{});

template &lt;RandomAccessRange R,

          class Comp = ranges::less&lt;&gt;, class Proj = ranges::identity&gt;
(2)(ranges TS)

    requires Sortable&lt;ranges::iterator_t&lt;R&gt;, Comp, Proj&gt;

    ranges::safe_iterator_t&lt;R&gt; sort(R &amp;&amp;r, Comp comp = Comp{}, Proj proj = Proj{});
1) Sorts the elements in the range [first, last) in ascending order. The order of equal elements is not guaranteed to be preserved. Elements are compared using comp after applying the projection proj.

2) Sorts the elements in the range r, as if by return ranges::sort(ranges::begin(r), ranges::end(r), comp, proj);

Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable.
</code></pre>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to sort<br />
r &#8211; the range of elements to sort<br />
comp &#8211; the comparator to use<br />
proj &#8211; the projection to apply to elements in the range</p>
<h2>Return value</h2>
<p>An iterator pointing past the end of the range (i.e., it compares equal to last for overload <code>(1)</code>, and ranges::end(r) for overload <code>(2)</code>). </p>
<h2>Complexity</h2>
<p>O(N·log(N)) comparisons, where N is equal to the number of elements in the range.</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order<br />
sort <i>(function template)</i> </p>
