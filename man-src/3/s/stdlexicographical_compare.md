---
title: "stdlexicographical_compare(3)"
name: "stdlexicographical_compare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlexicographical_compare/"
---

std::lexicographical_compare - std::lexicographical_compare

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt1, class InputIt2 &gt;

bool lexicographical_compare( InputIt1 first1, InputIt1 last1,                                       (until C++20)

InputIt2 first2, InputIt2 last2 );

template&lt; class InputIt1, class InputIt2 &gt;

constexpr bool lexicographical_compare( InputIt1 first1, InputIt1 last1,                             (since C++20)

InputIt2 first2, InputIt2 last2 );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

bool lexicographical_compare( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,     (2) (since C++17)

ForwardIt2 first2, ForwardIt2 last2 );

template&lt; class InputIt1, class InputIt2, class Compare &gt;

bool lexicographical_compare( InputIt1 first1, InputIt1 last1,                               (1)                   (until C++20)

InputIt2 first2, InputIt2 last2,

Compare comp );

template&lt; class InputIt1, class InputIt2, class Compare &gt;

constexpr bool lexicographical_compare( InputIt1 first1, InputIt1 last1,                         (3)               (since C++20)

InputIt2 first2, InputIt2 last2,

Compare comp );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class Compare &gt;

bool lexicographical_compare( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,         (4)           (since C++17)

ForwardIt2 first2, ForwardIt2 last2,

Compare comp );</code></pre> 
Checks if the first range [first1, last1) is lexicographically less than the second range [first2, last2). 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given binary comparison function comp. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 
Lexicographical comparison is a operation with the following properties: 
* Two ranges are compared element by element. 
* The first mismatching element defines which range is lexicographically less or greater than the other. 
* If one range is a prefix of another, the shorter range is lexicographically less than the other. 
* If two ranges have equivalent elements and are of the same length, then the ranges are lexicographically equal. 
* An empty range is lexicographically less than any non-empty range. 
* Two empty ranges are lexicographically equal. 

<h2>Parameters</h2>

first1, last1 - the first range of elements to examine 
first2, last2 - the second range of elements to examine 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that objects of types InputIt1 and InputIt2 can be dereferenced and then implicitly converted to both Type1 and Type2.

<h2>Type requirements</h2>

- 
InputIt1, InputIt2 must meet the requirements of LegacyInputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

true if the first range is lexicographically less than the second. 

<h2>Complexity</h2>

At most 2·min(N1, N2) applications of the comparison operation, where N1 = std::distance(first1, last1) and N2 = std::distance(first2, last2).

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2&gt; 
&nbsp;<wbr>&nbsp;bool lexicographical_compare(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, InputIt2 last2) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for ( ; (first1 != last1) &amp;&amp; (first2 != last2); ++first1, (void) ++first2 ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*first1 &lt; *first2) return true; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*first2 &lt; *first1) return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (first1 == last1) &amp;&amp; (first2 != last2); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, class Compare&gt; 
&nbsp;<wbr>&nbsp;bool lexicographical_compare(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, InputIt2 last2, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for ( ; (first1 != last1) &amp;&amp; (first2 != last2); ++first1, (void) ++first2 ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (comp(*first1, *first2)) return true; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (comp(*first2, *first1)) return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (first1 == last1) &amp;&amp; (first2 != last2); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;random&gt;
int main()

{
    std::vector&lt;char&gt; v1{'a', 'b', 'c', 'd'};
    std::vector&lt;char&gt; v2{'a', 'b', 'c', 'd'};
    std::mt19937 g{std::random_device{}()};
    while (!std::lexicographical_compare(v1.begin(), v1.end(),
                                         v2.begin(), v2.end())) {
        for (auto c : v1)
            std::cout &lt;&lt; c &lt;&lt; ' ';
        std::cout &lt;&lt; &quot;&gt;= &quot;;
        for (auto c : v2)
            std::cout &lt;&lt; c &lt;&lt; ' ';
        std::cout &lt;&lt; '\n';
        std::shuffle(v1.begin(), v1.end(), g);
        std::shuffle(v2.begin(), v2.end(), g);
    }
    for (auto c : v1)
        std::cout &lt;&lt; c &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;&lt; &quot;;
    for (auto c : v2)
        std::cout &lt;&lt; c &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;a b c d &gt;= a b c d 
&nbsp;<wbr>&nbsp;d a b c &gt;= c b d a 
&nbsp;<wbr>&nbsp;b d a c &gt;= a d c b 
&nbsp;<wbr>&nbsp;a c d b &lt; c d a b

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines if two sets of elements are the same 
equal <i>(function template)</i> 
