---
title: "stduninitialized_copy_n(3)"
name: "stduninitialized_copy_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduninitialized_copy_n/"
description: "std::uninitialized_copy_n – std::uninitialized_copy_n"
---

<p>std::uninitialized_copy_n &#8211; std::uninitialized_copy_n</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;memory&gt;

template&lt; class InputIt, class Size, class ForwardIt &gt;                                                   (1) (since C++11)

ForwardIt uninitialized_copy_n( InputIt first, Size count, ForwardIt d_first);

template&lt; class ExecutionPolicy, class InputIt, class Size, class ForwardIt &gt;                            (2) (since C++17)

ForwardIt uninitialized_copy_n( ExecutionPolicy&amp;&amp; policy, InputIt first, Size count, ForwardIt d_first);</code></pre>
<p>1) Copies count elements from a range beginning at first to an uninitialized memory area beginning at d_first as if by for (; n &gt; 0; ++d_first, (void)++first, &#8211;n)<br />
    ::new (static_cast&lt;void *&gt;(std::addressof(*d_first)))<br />
        typename std::iterator_traits&lt;ForwardIt&gt;::value_type(*first);<br />
If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first &#8211; the beginning of the range of the elements to copy<br />
d_first &#8211; the beginning of the destination range<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
No increment, assignment, comparison, or indirection through valid instances of ForwardIt may throw exceptions.</p>
<h2>Return value</h2>
<p>Iterator to the element past the last element copied. </p>
<h2>Complexity</h2>
<p>Linear in count.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class InputIt, class Size, class ForwardIt&gt;<br />
&nbsp;<wbr>&nbsp;ForwardIt uninitialized_copy_n(InputIt first, Size count, ForwardIt d_first)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::iterator_traits&lt;ForwardIt&gt;::value_type Value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt current = d_first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;try {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; count &gt; 0; ++first, (void) ++current, &#8211;count) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;::new (static_cast&lt;void*&gt;(std::addressof(*current))) Value(*first);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} catch (&#8230;) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; d_first != current; ++d_first) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_first-&gt;~Value();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;throw;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return current;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;string&gt;

#include &lt;tuple&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;std::string&gt; v = {&quot;This&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;};
    std::string *p;
    std::size_t sz;
    std::tie(p, sz) = std::get_temporary_buffer&lt;std::string&gt;(v.size());
    sz = std::min(sz, v.size());
    std::uninitialized_copy_n(v.begin(), sz, p);
    for (std::string *i = p; i != p + sz; ++i) {
        std::cout &lt;&lt; *i &lt;&lt; ' ';
        i-&gt;~basic_string&lt;char&gt;();
    }
    std::return_temporary_buffer(p);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;This is an example</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of objects to an uninitialized area of memory<br />
uninitialized_copy <i>(function template)</i> </p>
