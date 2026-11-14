---
title: "stduninitialized_copy(3)"
name: "stduninitialized_copy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduninitialized_copy/"
description: "std::uninitialized_copy – std::uninitialized_copy"
---

<p>std::uninitialized_copy &#8211; std::uninitialized_copy</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;memory&gt;

template&lt; class InputIt, class ForwardIt &gt;                                                                (1)

ForwardIt uninitialized_copy( InputIt first, InputIt last, ForwardIt d_first );

template&lt; class ExecutionPolicy, class InputIt, class ForwardIt &gt;                                         (2) (since C++17)

ForwardIt uninitialized_copy( ExecutionPolicy&amp;&amp; policy, InputIt first, InputIt last, ForwardIt d_first );</code></pre>
<p>1) Copies elements from the range [first, last) to an uninitialized memory area beginning at d_first as if by for (; first != last; ++d_first, (void)++first)<br />
    ::new (static_cast&lt;void *&gt;(std::addressof(*d_first)))<br />
        typename std::iterator_traits&lt;ForwardIt&gt;::value_type(*first);<br />
If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of the elements to copy<br />
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
<p>Linear in the distance between first and last</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class InputIt, class ForwardIt&gt;<br />
&nbsp;<wbr>&nbsp;ForwardIt uninitialized_copy(InputIt first, InputIt last, ForwardIt d_first)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::iterator_traits&lt;ForwardIt&gt;::value_type Value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt current = d_first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;try {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first, (void) ++current) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;::new (static_cast&lt;void*&gt;(std::addressof(*current))) Value(*first);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return current;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} catch (&#8230;) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; d_first != current; ++d_first) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_first-&gt;~Value();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;throw;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;cstdlib&gt;

#include &lt;string&gt;
int main()

{
    const char *v[] = {&quot;This&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;};
    auto sz = std::size(v);
    if (void *pbuf = std::aligned_alloc(alignof(std::string), sizeof(std::string) * sz)) {
        try {
            auto first = static_cast&lt;std::string *&gt;(pbuf);
            auto last = std::uninitialized_copy(std::begin(v), std::end(v), first);
            for (auto it = first; it != last; ++it)
                std::cout &lt;&lt; *it &lt;&lt; '_';
            std::destroy(first, last);
        } catch (...) {
        }
        std::free(pbuf);
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;This_is_an_example_</p>
<h2>See also</h2>
<p>uninitialized_copy_n copies a number of objects to an uninitialized area of memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
