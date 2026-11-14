---
title: "stdexperimentalrangesmismatch(3)"
name: "stdexperimentalrangesmismatch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesmismatch/"
---

std::experimental::ranges::mismatch - std::experimental::ranges::mismatch

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I2&gt; S2,

              class Proj1 = ranges::identity, class Proj2 = ranges::identity,

              class Pred = ranges::equal_to&lt;&gt;&gt;

requires IndirectRelation&lt;Pred, projected&lt;I1, Proj1&gt;, projected&lt;I2, Proj2&gt;&gt;(1)
(ranges TS)

    auto mismatch(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{},

                  Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{})

        -&gt; ranges::tagged_pair&lt;tag::in1(I1), tag::in2(I2)&gt;;

template &lt;InputRange R1, InputRange R2,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity,

          class Pred = ranges::equal_to&lt;&gt;&gt;

requires IndirectRelation&lt;Pred, projected&lt;ranges::iterator_t&lt;R1&gt;, Proj1&gt;,

                          projected&lt;ranges::iterator_t&lt;R2&gt;, Proj2&gt;&gt;(2)
(ranges TS)

    auto mismatch(R1 &amp;&amp;r1, R2 &amp;&amp;r2, Pred pred = Pred{},

                  Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{})

        -&gt; ranges::tagged_pair&lt;tag::in1(ranges::safe_iterator_t&lt;R1&gt;),

                               tag::in2(ranges::safe_iterator_t&lt;R2&gt;)&gt;;

template &lt;InputIterator I1, Sentinel&lt;I1&gt; S1, class I2,

          class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;

requires InputIterator&lt;std::decay_t&lt;I2&gt;&gt; &amp;&amp; !Range&lt;I2&gt; &amp;&amp; (ranges TS)

                                                              IndirectRelation&lt;Pred, projected&lt;I1, Proj1&gt;, (3)(deprecated)

                                                                                                               projected&lt;std::decay_t&lt;I2&gt;, Proj2&gt;&gt;

                                                          auto mismatch(I1 first1, S1 last1, I2 &amp;&amp;first2_, Pred pred = Pred{},

                                                                        Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{})

                                                              -&gt; ranges::tagged_pair&lt;tag::in1(I1), tag::in2(std::decay_t&lt;I2&gt;)&gt;;

template &lt;InputRange R1, class I2, class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;

requires InputIterator&lt;std::decay_t&lt;I2&gt;&gt; &amp;&amp; !Range&lt;I2&gt; &amp;&amp;

    IndirectRelation&lt;Pred, projected&lt;ranges::iterator_t&lt;R1&gt;, Proj1&gt;, (ranges TS)

                                                                         projected&lt;std::decay_t&lt;I2&gt;, Proj2&gt;&gt;(4)(deprecated)

        auto
        mismatch(R1 &amp;&amp; r1, I2 &amp;&amp;first2_, Pred pred = Pred{},

                 Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{})

            -&gt; ranges::tagged_pair&lt;tag::in1(ranges::safe_iterator_t&lt;Rng1&gt;),

                                   tag::in2(std::decay_t&lt;I2&gt;)&gt;;
1) Returns the first mismatching pair of elements from two ranges: one defined by [first1, last1) and another defined by [first2, last2).

2) Same as (1), but uses r1 as the first source range and r2 as the second source range, as if using ranges::begin(r1) as first1, ranges::end(r1) as last1, ranges::begin(r2) as first2, and ranges::end(r2) as last2.

3) Same as (1), but behaves as if first2 is std::decay_t&lt;I2&gt; first2 = std::forward&lt;I2&gt;(first2_); and last2 is ranges::unreachable{}. The underlying algorithm never increments first2 more than last1 - first1 times.

4) Same as (3), but uses r1 as the first source range, as if using ranges::begin(r1) as first1 and ranges::end(r1) as last1.

Elements are compared using pred to the projected elements of the two ranges, as if by ranges::invoke(pred, ranges::invoke(proj1, *i), ranges::invoke(proj2, *j)).

Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable.
</code></pre>

<h2>Parameters</h2>

first1, last1 - the first range of the elements 
r1 - the first range of the elements 
first2, last2 - the second range of the elements 
r2 - the second range of the elements 
first2_ - the beginning of the second range of the elements 
pred - predicate to apply to the projected elements 
proj1 - projection to apply to the elements in the first range 
proj2 - projection to apply to the elements in the second range

<h2>Return value</h2>

A tagged_pair object with iterators to the first two non-equal elements (the iterator from the first range has the tag in1 and the iterator from the second range has the tag in2). 
If no mismatches are found when the comparison reaches last1 or last2, whichever happens first, the pair holds the end iterator and the corresponding iterator from the other range. 

<h2>Complexity</h2>

At most last1 - first1 applications of the predicate and each projection.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I2&gt; S2, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj1 = ranges::identity, class Proj2 = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Pred = ranges::equal_to&lt;&gt; &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectRelation&lt;Pred, projected&lt;I1, Proj1&gt;, projected&lt;I2, Proj2&gt;&gt; 
&nbsp;<wbr>&nbsp;auto mismatch(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{}, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{}) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; ranges::tagged_pair&lt;tag::in1(I1), tag::in2(I2)&gt; 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1 &amp;&amp; first2 != last2 &amp;&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(pred, ranges::invoke(proj1, *first1), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(proj2, *first2))) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return {first1, first2}; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first position where two ranges differ 
mismatch <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines if two sets of elements are the same 
equal <i>(function template)</i> 
find finds the first element satisfying specific criteria 
find_if <i>(function template)</i> 
find_if_not 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns true if one range is lexicographically less than another 
lexicographical_compare <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
