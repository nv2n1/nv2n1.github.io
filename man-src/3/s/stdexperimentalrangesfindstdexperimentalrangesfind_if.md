---
title: "stdexperimentalrangesfindstdexperimentalrangesfind_if(3)"
name: "stdexperimentalrangesfindstdexperimentalrangesfind_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesfindstdexperimentalrangesfind_if/"
description: "std::experimental::ranges::find,std::experimental::ranges::find_if, – std::experimental::ranges::find,std::experimental::ranges::find_if,"
---

<p>std::experimental::ranges::find,std::experimental::ranges::find_if, &#8211; std::experimental::ranges::find,std::experimental::ranges::find_if,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class T, class Proj =

ranges::identity &gt;</code></pre>
<p>requires IndirectRelation&lt;ranges::equal_to&lt;&gt;, projected&lt;I, Proj&gt;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr>(ranges TS)<br />
const T*&gt; I find(I first, S last, const T &amp;value, Proj proj = Proj{});</p>
<p>template &lt;InputRange R, class T, class Proj = ranges::identity&gt;<br />
requires IndirectRelation&lt;ranges::equal_to&lt;&gt;,<br />
projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;, const T*&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr>(ranges TS) ranges::safe_iterator_t&lt;R&gt; find(R &amp;&amp;r, const T &amp;value, Proj proj =</p>
<p>                                                           Proj{});</p>
<p>template &lt;InputIterator I, Sentinel&lt;I&gt; S, class Proj =</p>
<p>                                              ranges::identity,<br />
          (3)(ranges TS)</p>
<p>              IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;<br />
                  Pred&gt;<br />
I find_if(I first, S last, Pred pred, Proj proj = Proj{});</p>
<p>template &lt;InputRange R, class Proj = ranges::identity,<br />
IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred<br />
&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr>(ranges TS) ranges::safe_iterator_t&lt;R&gt; find_if(R&amp;&amp; r, Pred pred, Proj proj =</p>
<p>Proj{});</p>
<p>template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj =</p>
<p>ranges::identity,<br />
(5) (ranges TS)</p>
<p>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred &gt;<br />
I find_if_not(I first, S last, Pred pred, Proj proj = Proj{});</p>
<p>template&lt; InputRange R, class Proj = ranges::identity,<br />
IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt;&nbsp;<wbr>Pred<br />
&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(6)</code>&nbsp;<wbr>(ranges TS) </p>
<pre><code>ranges::safe_iterator_t&lt;R&gt; find_if_not(R&amp;&amp; r, Pred pred, Proj proj =

Proj{});</code></pre>
<p>Returns the first element in the range&nbsp;<wbr>[first, last)&nbsp;<wbr>that satisfies specific<br />
criteria:<br />
1)&nbsp;<wbr>find searches for an element whose projected value is equal to value&nbsp;<wbr>(i.e., value<br />
==&nbsp;<wbr>ranges::invoke(proj,&nbsp;<wbr>*i)).<br />
3)&nbsp;<wbr>find_if searches for an element for whose projected value predicate p returns<br />
true&nbsp;<wbr>(i.e., ranges::invoke(pred, ranges::invoke(proj,&nbsp;<wbr>*i)))&nbsp;<wbr>is true).<br />
5)&nbsp;<wbr>find_if_not searches for an element for whose projected value predicate q returns<br />
false&nbsp;<wbr>(i.e., ranges::invoke(pred, ranges::invoke(proj,&nbsp;<wbr>*i)))&nbsp;<wbr>is false).<br />
2,4,6)&nbsp;<wbr>Same as&nbsp;<wbr>(1,3,5), but uses r as the source range, as if using ranges::begin(r)<br />
as first and ranges::end(r)&nbsp;<wbr>as last.<br />
Notwithstanding the declarations depicted above, the actual number and order of<br />
template parameters for algorithm declarations is unspecified. Thus, if explicit<br />
template arguments are used when calling an algorithm, the program is probably<br />
non-portable. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to examine<br />
r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the range of elements to examine<br />
value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; value to compare the projected elements to<br />
pred&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; predicate to apply to the projected elements<br />
proj&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; projection to apply to the elements</p>
<h2>Return value</h2>
<p>Iterator to the first element satisfying the condition. If no such element is found,<br />
returns an iterator that compares equal to last. </p>
<h2>Complexity</h2>
<p>At most last &#8211; first applications of the predicate and projection.</p>
<h2>Possible implementation</h2>
<h2>First version</h2>
<p>template&lt;&nbsp;<wbr>InputIterator I, Sentinel&lt;I&gt;&nbsp;<wbr>S, class T, class Proj&nbsp;<wbr>=&nbsp;<wbr>ranges::identity&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>requires IndirectRelation&lt;ranges::equal_to&lt;&gt;, projected&lt;I, Proj&gt;, const T*&gt;<br />
I find(I first, S last, const T&amp;&nbsp;<wbr>value, Proj proj&nbsp;<wbr>=&nbsp;<wbr>Proj{})<br />
{<br />
&nbsp;<wbr>for&nbsp;<wbr>(;&nbsp;<wbr>first&nbsp;<wbr>!=&nbsp;<wbr>last;&nbsp;<wbr>++first)&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>(ranges::invoke(proj,&nbsp;<wbr>*first)&nbsp;<wbr>==&nbsp;<wbr>value)&nbsp;<wbr>break;<br />
&nbsp;<wbr>}<br />
&nbsp;<wbr>return first;<br />
}</p>
<h2>Second version</h2>
<p>template&lt;&nbsp;<wbr>InputIterator I, Sentinel&lt;I&gt;&nbsp;<wbr>S, class Proj&nbsp;<wbr>=&nbsp;<wbr>ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt;<br />
I find_if(I first, S last, Pred pred, Proj proj&nbsp;<wbr>=&nbsp;<wbr>Proj{})<br />
{<br />
&nbsp;<wbr>for&nbsp;<wbr>(;&nbsp;<wbr>first&nbsp;<wbr>!=&nbsp;<wbr>last;&nbsp;<wbr>++first)&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>(ranges::invoke(pred, ranges::invoke(proj,&nbsp;<wbr>*first)))&nbsp;<wbr>break;<br />
&nbsp;<wbr>}<br />
&nbsp;<wbr>return first;<br />
}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Third version<br />
template&lt;&nbsp;<wbr>InputIterator I, Sentinel&lt;I&gt;&nbsp;<wbr>S, class Proj&nbsp;<wbr>=&nbsp;<wbr>ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt;&nbsp;<wbr>Pred&nbsp;<wbr>&gt;<br />
I find_if_not(I first, S last, Pred pred, Proj proj&nbsp;<wbr>=&nbsp;<wbr>Proj{})<br />
{<br />
&nbsp;<wbr>for&nbsp;<wbr>(;&nbsp;<wbr>first&nbsp;<wbr>!=&nbsp;<wbr>last;&nbsp;<wbr>++first)&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>(!ranges::invoke(pred, ranges::invoke(proj,&nbsp;<wbr>*first)))&nbsp;<wbr>break;<br />
&nbsp;<wbr>}<br />
&nbsp;<wbr>return first;<br />
}</p>
<h2>Example</h2>
<p>&nbsp;<wbr>This section is incomplete<br />
&nbsp;<wbr>Reason: no example </p>
<h2>See also</h2>
<p>find<br />
find_if&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>finds the first element satisfying specific criteria<br />
find_if_not&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>finds the first two adjacent items that are equal&nbsp;<wbr>(or satisfy a given<br />
adjacent_find predicate)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
find_end&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>finds the last sequence of elements in a certain range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
find_first_of searches for any one of a set of elements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
mismatch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>finds the first position where two ranges differ<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
search&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>searches for a range of elements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i> </p>
