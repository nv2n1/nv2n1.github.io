---
title: "stdexperimentalrangesfor_each(3)"
name: "stdexperimentalrangesfor_each"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesfor_each/"
description: "std::experimental::ranges::for_each – std::experimental::ranges::for_each"
---

<p>std::experimental::ranges::for_each &#8211; std::experimental::ranges::for_each</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/ranges/algorithm&gt;

template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,

IndirectUnaryInvocable&lt;projected&lt;I, Proj&gt;&gt; Fun &gt;                         (1) (ranges TS)

ranges::tagged_pair&lt;tag::in(I), tag::fun(Fun)&gt;

for_each(I first, S last, Fun f, Proj proj = Proj{});

template&lt; InputRange R, class Proj = ranges::identity,

IndirectUnaryInvocable&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Fun &gt;     (2) (ranges TS)

ranges::tagged_pair&lt;tag::in(ranges::safe_iterator_t&lt;R&gt;), tag::fun(Fun)&gt;

for_each(R&amp;&amp; r, Fun f, Proj proj = Proj{});</code></pre>
<p>1) Invokes the given function object f to the result of invoking the projection proj on dereferencing every iterator in the range [first, last) (i.e.,ranges::invoke(f, ranges::invoke(proj, *i))), in order.<br />
2) Same as <code>(1)</code>, but uses r as the source range, as if using ranges::begin(r) as first and ranges::end(r) as last.<br />
For both overloads, if the iterator type is mutable, f may modify the elements of the range through the dereferenced iterator. If f returns a result, the result is ignored.<br />
Unlike the rest of the algorithms, for_each is not allowed to make copies of the elements in the sequence even if they are trivially copyable.<br />
Unlike std::for_each (which requires only MoveConstructible), these functions require Fun to model CopyConstructible.<br />
Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range to apply the function to<br />
r &#8211; the range to apply the function to<br />
f &#8211; callable object to be applied to each projected element in the range<br />
proj &#8211; projection to apply to the elements</p>
<h2>Return value</h2>
<p>A tagged_pair object containing the following two members:<br />
* The first member, with the tag tag::in, is the past-the-end iterator of the source range (that is, an iterator of type I that compares equal to the sentinel last).<br />
* The second member, with the tag tag::fun, is initialized from std::move(f) (after all applications of the function object). </p>
<h2>Complexity</h2>
<p>Exactly last &#8211; first applications of f and proj</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; InputIterator I, Sentinel&lt;I&gt; S, class Proj = ranges::identity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryInvocable&lt;ranges::projected&lt;I, Proj&gt;&gt; Fun &gt;<br />
&nbsp;<wbr>&nbsp;auto for_each(I first, S last, Fun f, Proj proj = Proj{})<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; ranges::tagged_pair&lt;tag::in(I), tag::fun(Fun)&gt;<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for(; first != last; ++first) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(f, ranges::invoke(proj, *first));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return {std::move(first), std::move(f)};<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements<br />
transform <i>(function template)</i><br />
range-for_loop executes loop over range <i>(since C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements<br />
for_each <i>(function template)</i><br />
for_each_n applies a function object to the first n elements of a sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
