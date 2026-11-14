---
title: "stdremovestdremove_if(3)"
name: "stdremovestdremove_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremovestdremove_if/"
---

std::remove,std::remove_if - std::remove,std::remove_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt, class T&gt;
    (until C++ 20)

        ForwardIt remove(ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class ForwardIt, class T&gt;
(since C++ 20)

    constexpr ForwardIt remove(ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt, class T&gt;
(2)(since C++ 17)

    ForwardIt remove(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, const T &amp;value);
(1)

    template &lt;class ForwardIt, class UnaryPredicate&gt;
    (until C++ 20)

        ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPredicate p);

template &lt;class ForwardIt, class UnaryPredicate&gt;
(3)(since C++ 20)

    constexpr ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPredicate p);

template &lt;class ExecutionPolicy, class ForwardIt, class UnaryPredicate&gt;
(4)(since C++ 17)

    ForwardIt remove_if(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, UnaryPredicate p);</code></pre> 
Removes all elements satisfying specific criteria from the range [first, last) and returns a past-the-end iterator for the new end of the range. 
1) Removes all elements that are equal to value. 
3) Removes all elements for which predicate p returns true. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 
Removing is done by shifting (by means of move assignment) the elements in the range in such a way that the elements that are not to be removed appear in the beginning of the range. Relative order of the elements that remain is preserved and the physical size of the container is unchanged. Iterators pointing to an element between the new logical end and the physical end of the range are still dereferenceable, but the elements themselves have unspecified values (as per MoveAssignable post-condition). A call to remove is typically followed by a call to a container's erase method, which erases the unspecified values and reduces the physical size of the container to match its new logical size. 

<h2>Parameters</h2>

first, last - the range of elements to process 
value - the value of elements to remove 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element should be removed. 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of ForwardIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
The type of dereferenced ForwardIt must meet the requirements of MoveAssignable. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

Past-the-end iterator for the new range of values (if this is not end, then it points to an unspecified value, and so do iterators to any values between this iterator and end) 

<h2>Complexity</h2>

Exactly std::distance(first, last) applications of the predicate.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

The similarly-named container member functions list::remove, list::remove_if, forward_list::remove, and forward_list::remove_if erase the removed elements. 
These algorithms cannot be used with associative containers such as std::set and std::map because ForwardIt does not dereference to a MoveAssignable type (the keys in these containers are not modifiable) 
The standard library also defines an overload of std::remove taking const char*, used to delete files: std::remove. 
Because std::remove takes value by reference, it can have unexpected behavior if it is a reference to an element of the range [first, last). 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; class ForwardIt, class T &gt; 
&nbsp;<wbr>&nbsp;ForwardIt remove(ForwardIt first, ForwardIt last, const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = std::find(first, last, value); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first != last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for(ForwardIt i = first; ++i != last; ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!(*i == value)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first++ = std::move(*i); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class UnaryPredicate&gt; 
&nbsp;<wbr>&nbsp;ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = std::find_if(first, last, p); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first != last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for(ForwardIt i = first; ++i != last; ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!p(*i)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first++ = std::move(*i); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Examples</h2>

The following code removes all spaces from a string by shifting all non-space characters to the left and then erasing the extra. This is an example of erase-remove_idiom. 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;cctype&gt;
int main()

{
    std::string str1 = &quot;Text with some   spaces&quot;;
    str1.erase(std::remove(str1.begin(), str1.end(), ' '),
               str1.end());
    std::cout &lt;&lt; str1 &lt;&lt; '\n';
    std::string str2 = &quot;Text\n with\tsome \t  whitespaces\n\n&quot;;
    str2.erase(std::remove_if(str2.begin(),
                              str2.end(),
                              [](unsigned char x) { return std::isspace(x); }),
               str2.end());
    std::cout &lt;&lt; str2 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Textwithsomespaces 
&nbsp;<wbr>&nbsp;Textwithsomewhitespaces

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements omitting those that satisfy specific criteria 
remove_copy <i>(function template)</i> 
remove_copy_if 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes consecutive duplicate elements in a range 
unique <i>(function template)</i> 
