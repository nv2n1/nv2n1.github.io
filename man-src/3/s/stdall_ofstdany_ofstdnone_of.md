---
title: "stdall_ofstdany_ofstdnone_of(3)"
name: "stdall_ofstdany_ofstdnone_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdall_ofstdany_ofstdnone_of/"
---

std::all_of,std::any_of,std::none_of - std::all_of,std::any_of,std::none_of

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class UnaryPredicate &gt;                                                      (since C++11)

bool all_of( InputIt first, InputIt last, UnaryPredicate p );                                        (until C++20)

template&lt; class InputIt, class UnaryPredicate &gt;                                                      (since C++20)

constexpr bool all_of( InputIt first, InputIt last, UnaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt, class UnaryPredicate &gt;                         (2) (since C++17)

bool all_of( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, UnaryPredicate p );

template&lt; class InputIt, class UnaryPredicate &gt;                                                                     (since C++11)

bool any_of( InputIt first, InputIt last, UnaryPredicate p );                                                       (until C++20)

template&lt; class InputIt, class UnaryPredicate &gt;                                              (1)                    (since C++20)

constexpr bool any_of( InputIt first, InputIt last, UnaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt, class UnaryPredicate &gt;                             (4)            (since C++17)

bool any_of( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, UnaryPredicate p );      (3)

template&lt; class InputIt, class UnaryPredicate &gt;                                                                                    (since C++11)

bool none_of( InputIt first, InputIt last, UnaryPredicate p );                                                                     (until C++20)

template&lt; class InputIt, class UnaryPredicate &gt;                                                      (5)                           (since C++20)

constexpr bool none_of( InputIt first, InputIt last, UnaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt, class UnaryPredicate &gt;                                            (6)            (since C++17)

bool none_of( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, UnaryPredicate p );</code></pre> 
1) Checks if unary predicate p returns true for all elements in the range [first, last). 
3) Checks if unary predicate p returns true for at least one element in the range [first, last). 
5) Checks if unary predicate p returns true for no elements in the range [first, last). 
2,4,6) Same as (1,3,5), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate . 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

1-2) true if unary predicate returns true for all elements in the range, false otherwise. Returns true if the range is empty. 
3-4) true if unary predicate returns true for at least one element in the range, false otherwise. Returns false if the range is empty. 
5-6) true if unary predicate returns true for no elements in the range, false otherwise. Returns true if the range is empty. 

<h2>Complexity</h2>

1,3,5) At most last - first applications of the predicate 
2,4,6) O(last-first) applications of the predicate

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; class InputIt, class UnaryPredicate &gt; 
&nbsp;<wbr>&nbsp;constexpr bool all_of(InputIt first, InputIt last, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::find_if_not(first, last, p) == last; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt; class InputIt, class UnaryPredicate &gt; 
&nbsp;<wbr>&nbsp;constexpr bool any_of(InputIt first, InputIt last, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::find_if(first, last, p) != last; 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt; class InputIt, class UnaryPredicate &gt; 
&nbsp;<wbr>&nbsp;constexpr bool none_of(InputIt first, InputIt last, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::find_if(first, last, p) == last; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;numeric&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;

#include &lt;iostream&gt;

#include &lt;functional&gt;
int main()

{
    std::vector&lt;int&gt; v(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout &lt;&lt; &quot;Among the numbers: &quot;;
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
    if (std::all_of(v.cbegin(), v.cend(), [](int i) { return i % 2 == 0; })) {
        std::cout &lt;&lt; &quot;All numbers are even\n&quot;;
    }
    if (std::none_of(v.cbegin(), v.cend(), std::bind(std::modulus&lt;int&gt;(), std::placeholders::_1, 2))) {
        std::cout &lt;&lt; &quot;None of them are odd\n&quot;;
    }
    struct DivisibleBy {
        const int d;
        DivisibleBy(int n)
            : d(n)
        {
        }
        bool operator()(int n) const
        {
            return n % d == 0;
        }
    };
    if (std::any_of(v.cbegin(), v.cend(), DivisibleBy(7))) {
        std::cout &lt;&lt; &quot;At least one number is divisible by 7\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Among the numbers: 2 4 6 8 10 12 14 16 18 20 
&nbsp;<wbr>&nbsp;All numbers are even 
&nbsp;<wbr>&nbsp;None of them are odd 
&nbsp;<wbr>&nbsp;At least one number is divisible by 7

<h2>See also</h2>


