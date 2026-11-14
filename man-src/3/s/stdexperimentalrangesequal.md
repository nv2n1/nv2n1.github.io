---
title: "stdexperimentalrangesequal(3)"
name: "stdexperimentalrangesequal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesequal/"
---

std::experimental::ranges::equal - std::experimental::ranges::equal

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I2&gt; S2,

              class Pred = ranges::equal_to&lt;&gt;,

              class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;
    (1)(ranges TS)

        requires IndirectlyComparable&lt;I1, I2, Pred, Proj1, Proj2&gt;

bool equal(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{},

           Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template &lt;InputRange R1, InputRange R2, class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;

requires IndirectlyComparable &lt; ranges::iterator_t&lt;R1&gt;, ranges::iterator_t&lt;R2&gt;, (2)
(ranges TS)

    Pred,
    Proj1, Proj2 &gt;

               bool equal(R1 &amp;&amp;r1, R2 &amp;&amp;r2, Pred pred = Pred{},

                          Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template &lt;InputIterator I1, Sentinel&lt;I1&gt; S1, class I2,

          class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;
    (ranges TS)

        requires InputIterator&lt;std::decay_t&lt;I2&gt;&gt; &amp;&amp; !Range&lt;I2&gt; &amp;&amp;
    (3)(deprecated)

        IndirectlyComparable&lt;I1, std::decay_t&lt;I2&gt;, Pred, Proj1, Proj2&gt;

    bool equal(I1 first1, S1 last1, I2 &amp;&amp;first2_, Pred pred = Pred{},

               Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template &lt;InputRange R1, class I2, class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;

requires InputIterator&lt;std::decay_t&lt;I2&gt;&gt; &amp;&amp; !Range&lt;I2&gt; &amp;&amp; (4)(ranges TS)

                                                              IndirectlyComparable&lt;ranges::iterator_t&lt;R1&gt;, std::decay_t&lt;I2&gt;, Pred, Proj1, Proj2&gt;(deprecated)

                                                                  bool
                                                                  equal(R1 &amp;&amp; r1, I2 &amp;&amp;first2_, Pred pred = Pred{},

                                                                        Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});
1) Returns true if the range [first1, last1) is equal to the range [first2, last2), and false otherwise.

2) Same as (1), but uses r1 as the first source range and r2 as the second source range, as if using ranges::begin(r1) as first1, ranges::end(r1) as last1, ranges::begin(r2) as first2, and ranges::end(r2) as last2.

3) Same as (1), except that the second range is considered to end when either the first range is exhausted or the first mismatch is detected. Equivalent to return last1 == ranges::mismatch(first1, last1, std::forward&lt;I2&gt;(first2_), comp, proj1, proj2).in1();

4) Same as (3), but uses r1 as the first source range, as if using ranges::begin(r1) as first1 and ranges::end(r1) as last1.

Two ranges are considered equal if they have the same number of elements and, for every iterator i in the range [first1,last1), ranges::invoke(pred, ranges::invoke(proj1, *i), ranges::invoke(proj2, *(first2 + (i - first1)))) is true.

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

true if the two ranges are equal, otherwise returns false. 

<h2>Notes</h2>

ranges::equal should not be used to compare the ranges formed by the iterators from std::unordered_set, std::unordered_multiset, std::unordered_map, or std::unordered_multimap because the order in which the elements are stored in those containers may be different even if the two containers store the same elements. 
When comparing entire containers for equality, operator== for the corresponding container are usually preferred. 

<h2>Complexity</h2>

1-2) If SizedSentinel&lt;S1, I1&gt; &amp;&amp; SizedSentinel&lt;S2, I2&gt; is satisfied and last1 - first1 != last2 - first2, no applications of the predicate and projections. Otherwise, at most min(last1 - first1, last2 - first2) applications of the predicate and each projection. 
3-4) At most last1 - first1 applications of the predicate and each projection.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputIterator I1, SizedSentinel&lt;I1&gt; S1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIterator I2, SizedSentinel&lt;I1&gt; S2 &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool check_size(I1&amp; first1, S1&amp; last1, I2&amp; first2, S2&amp; last2) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last1 - first1 != last2 - first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I1&gt; S2 &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool check_size(I1&amp; first1, S1&amp; last1, I2&amp; first2, S2&amp; last2) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template&lt; InputIterator I1, Sentinel&lt;I1&gt; S1, InputIterator I2, Sentinel&lt;I2&gt; S2, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Pred = ranges::equal_to&lt;&gt;, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj1 = ranges::identity, class Proj2 = ranges::identity &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectlyComparable&lt;I1, I2, Pred, Proj1, Proj2&gt; 
&nbsp;<wbr>&nbsp;bool equal(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{}, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(detail::check_size(first1, last1, first2, last2)) return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for(; first1 != last1 &amp;&amp; first2 != last2; (void) ++first1, (void)++first2) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(!ranges::invoke(pred, ranges::invoke(proj1, *first1), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ranges::invoke(proj2, *first2))) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first1 == last1 &amp;&amp; first2 == last2; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See Also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines if two sets of elements are the same 
equal <i>(function template)</i> 
find finds the first element satisfying specific criteria 
find_if <i>(function template)</i> 
find_if_not 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns true if one range is lexicographically less than another 
lexicographical_compare <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first position where two ranges differ 
mismatch <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
