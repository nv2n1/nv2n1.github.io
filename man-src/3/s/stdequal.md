---
title: "stdequal(3)"
name: "stdequal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdequal/"
---

std::equal - std::equal

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt1, class InputIt2 &gt;

bool equal( InputIt1 first1, InputIt1 last1,                                                         (until C++20)

InputIt2 first2 );

template&lt; class InputIt1, class InputIt2 &gt;

constexpr bool equal( InputIt1 first1, InputIt1 last1,                                               (since C++20)

InputIt2 first2 );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

bool equal( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                       (2) (since C++17)

ForwardIt2 first2 );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

bool equal( InputIt1 first1, InputIt1 last1,                                                                       (until C++20)

InputIt2 first2, BinaryPredicate p );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

constexpr bool equal( InputIt1 first1, InputIt1 last1,                                                             (since C++20)

InputIt2 first2, BinaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

bool equal( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                           (4)           (since C++17)

ForwardIt2 first2, BinaryPredicate p );

template&lt; class InputIt1, class InputIt2 &gt;                                                                                       (since C++14)

bool equal( InputIt1 first1, InputIt1 last1,                                                 (1)                                 (until C++20)

InputIt2 first2, InputIt2 last2 );

template&lt; class InputIt1, class InputIt2 &gt;

constexpr bool equal( InputIt1 first1, InputIt1 last1,                                                                           (since C++20)

InputIt2 first2, InputIt2 last2 );                                                               (3)

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

bool equal( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                                         (6)           (since C++17)

ForwardIt2 first2, ForwardIt2 last2 );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

bool equal( InputIt1 first1, InputIt1 last1,                                                         (5)                                        (since C++14)

InputIt2 first2, InputIt2 last2,                                                                                                                (until C++20)

BinaryPredicate p );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

constexpr bool equal( InputIt1 first1, InputIt1 last1,                                                             (7)                          (since C++20)

InputIt2 first2, InputIt2 last2,

BinaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

bool equal( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                                                       (8)            (since C++17)

ForwardIt2 first2, ForwardIt2 last2,

BinaryPredicate p );</code></pre> 
1,3) Returns true if the range [first1, last1) is equal to the range [first2, first2 + (last1 - first1)), and false otherwise 
5,7) Returns true if the range [first1, last1) is equal to the range [first2, last2), and false otherwise. 
2,4,6,8) Same as (1,3,5,7), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 
Two ranges are considered equal if they have the same number of elements and, for every iterator i in the range [first1,last1), *i equals *(first2 + (i - first1)). The overloads (1,2,5,6) use operator== to determine if two elements are equal, whereas overloads (3,4,7,8) use the given binary predicate p. 

<h2>Parameters</h2>

first1, last1 - the first range of the elements to compare 
first2, last2 - the second range of the elements to compare 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the elements should be treated as equal. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
p - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that objects of types InputIt1 and InputIt2 can be dereferenced and then implicitly converted to Type1 and Type2 respectively.

<h2>Type requirements</h2>

- 
InputIt1, InputIt2 must meet the requirements of LegacyInputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

5-8) If the length of the range [first1, last1) does not equal the length of the range [first2, last2), returns false 
If the elements in the two ranges are equal, returns true. 
Otherwise returns false. 

<h2>Notes</h2>

std::equal should not be used to compare the ranges formed by the iterators from std::unordered_set, std::unordered_multiset, std::unordered_map, or std::unordered_multimap because the order in which the elements are stored in those containers may be different even if the two containers store the same elements. 
When comparing entire containers for equality, operator== for the corresponding container are usually preferred. 

<h2>Complexity</h2>

1,3) At most last1 - first1 applications of the predicate 
5,7) At most min(last1 - first1, last2 - first2) applications of the predicate. 
However, if InputIt1 and InputIt2 meet the requirements of LegacyRandomAccessIterator and last1 - first1 != last2 - first2 then no applications of the predicate are made (size mismatch is detected without looking at any elements). 
2,4,6,8) same, but the complexity is specified as O(x), rather than &quot;at most x&quot;

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2&gt; 
&nbsp;<wbr>&nbsp;bool equal(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first1 != last1; ++first1, ++first2) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!(*first1 == *first2)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return true; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, class BinaryPredicate&gt; 
&nbsp;<wbr>&nbsp;bool equal(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, BinaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first1 != last1; ++first1, ++first2) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!p(*first1, *first2)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return true; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following code uses equal() to test if a string is a palindrome 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;
bool is_palindrome(const std::string &amp;s)

{
    return std::equal(s.begin(), s.begin() + s.size() / 2, s.rbegin());
}
void test(const std::string &amp;s)

{
    std::cout &lt;&lt; &quot;\&quot;&quot; &lt;&lt; s &lt;&lt; &quot;\&quot; &quot;
              &lt;&lt; (is_palindrome(s) ? &quot;is&quot; : &quot;is not&quot;)
              &lt;&lt; &quot; a palindrome\n&quot;;
}
int main()

{
    test(&quot;radar&quot;);
    test(&quot;hello&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;radar&quot; is a palindrome 
&nbsp;<wbr>&nbsp;&quot;hello&quot; is not a palindrome

<h2>See Also</h2>

find 
find_if 
find_if_not finds the first element satisfying specific criteria 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns true if one range is lexicographically less than another 
lexicographical_compare <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first position where two ranges differ 
mismatch <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
