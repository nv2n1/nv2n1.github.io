---
title: "stdexperimentalrangesis_permutation(3)"
name: "stdexperimentalrangesis_permutation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesis_permutation/"
---

std::experimental::ranges::is_permutation - std::experimental::ranges::is_permutation

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;ForwardIterator I1, Sentinel&lt;I1&gt; S1, ForwardIterator I2, Sentinel&lt;I2&gt; S2,

              class Pred = ranges::equal_to&lt;&gt;,

              class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;
    (1)(ranges TS)

        requires IndirectlyComparable&lt;I1, I2, Pred, Proj1, Proj2&gt;

bool is_permutation(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = Pred{},

                    Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template &lt;ForwardRange R1, ForwardRange R2, class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;

requires IndirectlyComparable &lt; ranges::iterator_t&lt;R1&gt;, ranges::iterator_t&lt;R2&gt;, (2)
(ranges TS)

    Pred,
    Proj1, Proj2 &gt;

               bool is_permutation(R1 &amp;&amp;r1, R2 &amp;&amp;r2, Pred pred = Pred{},

                                   Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template &lt;ForwardIterator I1, Sentinel&lt;I1&gt; S1, class I2,

          class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;
    (ranges TS)

        requires ForwardIterator&lt;std::decay_t&lt;I2&gt;&gt; &amp;&amp; !Range&lt;I2&gt; &amp;&amp;
    (3)(deprecated)

        IndirectlyComparable&lt;I1, std::decay_t&lt;I2&gt;, Pred, Proj1, Proj2&gt;

    bool is_permutation(I1 first1, S1 last1, I2 &amp;&amp;first2_, Pred pred = Pred{},

                        Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});

template &lt;ForwardRange R1, class I2, class Pred = ranges::equal_to&lt;&gt;,

          class Proj1 = ranges::identity, class Proj2 = ranges::identity&gt;

requires ForwardIterator&lt;std::decay_t&lt;I2&gt;&gt; &amp;&amp; !Range&lt;I2&gt; &amp;&amp; (4)(ranges TS)

                                                                IndirectlyComparable&lt;ranges::iterator_t&lt;R1&gt;, std::decay_t&lt;I2&gt;, Pred, Proj1, Proj2&gt;(deprecated)

                                                                    bool
                                                                    is_permutation(R1 &amp;&amp; r1, I2 &amp;&amp;first2_, Pred pred = Pred{},

                                                                                   Proj1 proj1 = Proj1{}, Proj2 proj2 = Proj2{});
1) Returns true if the exists a permutation of the elements in range [first1, last1) that makes the range equal to [first2, last2), and false otherwise.

2) Same as (1), but uses r1 as the first source range and r2 as the second source range, as if using ranges::begin(r1) as first1, ranges::end(r1) as last1, ranges::begin(r2) as first2, and ranges::end(r2) as last2.

3) Same as (1), except that first2 is defined as if by std::decay_t&lt;I2&gt; first2 = std::forward&lt;I2&gt;(first2_); and last2 is first2 + (last1 - first1).

4) Same as (3), but uses r1 as the first source range, as if using ranges::begin(r1) as first1 and ranges::end(r1) as last1.

Two ranges are considered equal if they have the same number of elements and, for every iterator i in the range [first1, last1), ranges::invoke(pred, ranges::invoke(proj1, *i), ranges::invoke(proj2, *(first2 + (i - first1)))) is true.

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

true if the range [first1, last1) is a permutation of the range [first2, last2). 

<h2>Complexity</h2>

At most O(N2) applications of the predicate and each projection, or exactly N if the sequences are already equal, where N=last1 - first1). 
However if SizedSentinel&lt;S1, I1&gt; &amp;&amp; SizedSentinel&lt;S2, I2&gt; is satisfied and last1 - first1 != last2 - first2, no applications of the predicate and projections are made.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See Also</h2>

is_permutation determines if a sequence is a permutation of another sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next greater lexicographic permutation of a range of elements 
next_permutation <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next smaller lexicographic permutation of a range of elements 
prev_permutation <i>(function template)</i> 
