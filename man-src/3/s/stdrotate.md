---
title: "stdrotate(3)"
name: "stdrotate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrotate/"
description: "std::rotate – std::rotate"
---

<p>std::rotate &#8211; std::rotate</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt&gt;
    (until C++ 11)

        void rotate(ForwardIt first, ForwardIt n_first, ForwardIt last);

template &lt;class ForwardIt&gt;
(since C++ 11)

    ForwardIt rotate(ForwardIt first, ForwardIt n_first, ForwardIt last);
(until C++ 20)

    template &lt;class ForwardIt&gt;
    (1)(since C++ 20)

        constexpr ForwardIt rotate(ForwardIt first, ForwardIt n_first, ForwardIt last);

template &lt;class ExecutionPolicy, class ForwardIt&gt;

ForwardIt rotate(ExecutionPolicy &amp;&amp;policy, (2)(since C++ 17)

                                               ForwardIt first,
                 ForwardIt n_first, ForwardIt last);</code></pre>
<p>1) Performs a left rotation on a range of elements.<br />
Specifically, std::rotate swaps the elements in the range [first, last) in such a way that the element n_first becomes the first element of the new range and n_first &#8211; 1 becomes the last element.<br />
A precondition of this function is that [first, n_first) and [n_first, last) are valid ranges.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first &#8211; the beginning of the original range<br />
n_first &#8211; the element that should appear at the beginning of the rotated range<br />
last &#8211; the end of the original range<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of ValueSwappable and LegacyForwardIterator.<br />
&#8211;<br />
The type of dereferenced ForwardIt must meet the requirements of MoveAssignable and MoveConstructible.</p>
<h2>Return value</h2>
<p><i>(none)</i> <i>(until C++11)</i><br />
The iterator equal to first + (last &#8211; n_first) <i>(since C++11)</i> </p>
<h2>Complexity</h2>
<p>Linear in the distance between first and last</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>See also the implementations in libstdc++ and libc++. </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt;<br />
&nbsp;<wbr>&nbsp;ForwardIt rotate(ForwardIt first, ForwardIt n_first, ForwardIt last)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(first == n_first) return last;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(n_first == last) return first; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt read = n_first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt write = first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt next_read = first; // read position for when &quot;read&quot; hits &quot;last&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while(read != last) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(write == next_read) next_read = read; // track where &quot;first&quot; went<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::iter_swap(write++, read++);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// rotate the remaining sequence into place<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(rotate)(write, next_read, last);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return write;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>std::rotate is a common building block in many algorithms. This example demonstrates insertion sort:<br />
 // Run this code </p>
<pre><code>#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;
int main()

{
    std::vector&lt;int&gt; v{2, 4, 2, 0, 5, 10, 7, 3, 7, 1};
    std::cout &lt;&lt; &quot;before sort:      &quot;;
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    // insertion sort
    for (auto i = v.begin(); i != v.end(); ++i) {
        std::rotate(std::upper_bound(v.begin(), i, *i), i, i + 1);
    }
    std::cout &lt;&lt; &quot;after sort:       &quot;;
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    // simple rotation to the left
    std::rotate(v.begin(), v.begin() + 1, v.end());
    std::cout &lt;&lt; &quot;simple rotate left  : &quot;;
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    // simple rotation to the right
    std::rotate(v.rbegin(), v.rbegin() + 1, v.rend());
    std::cout &lt;&lt; &quot;simple rotate right : &quot;;
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;before sort: 2 4 2 0 5 10 7 3 7 1<br />
&nbsp;<wbr>&nbsp;after sort: 0 1 2 2 3 4 5 7 7 10<br />
&nbsp;<wbr>&nbsp;simple rotate left : 1 2 2 3 4 5 7 7 10 0<br />
&nbsp;<wbr>&nbsp;simple rotate right: 0 1 2 2 3 4 5 7 7 10</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies and rotate a range of elements<br />
rotate_copy <i>(function template)</i> </p>
