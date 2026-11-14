---
title: "stddestroy_n(3)"
name: "stddestroy_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddestroy_n/"
description: "std::destroy_n – std::destroy_n"
---

<p>std::destroy_n &#8211; std::destroy_n</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;memory&gt;

template&lt; class ForwardIt, class Size &gt;                                   (1) (since C++17)

ForwardIt destroy_n( ForwardIt first, Size n );

template&lt; class ExecutionPolicy, class ForwardIt, class Size &gt;            (2) (since C++17)

ForwardIt destroy_n( ExecutionPolicy&amp;&amp; policy, ForwardIt first, Size n );</code></pre>
<p>1) Destroys the n objects in the range starting at first, as if by for (; n &gt; 0; (void)++first, &#8211;n)<br />
    std::destroy_at(std::addressof(*first));<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first &#8211; the beginning of the range of elements to destroy<br />
n &#8211; the number of elements to destroy<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
No increment, assignment, comparison, or indirection through valid instances of ForwardIt may throw exceptions.</p>
<h2>Return value</h2>
<p>The end of the range of objects that has been destroyed (i.e., std::next(first, n)). </p>
<h2>Complexity</h2>
<p>Linear in n.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class Size&gt;<br />
&nbsp;<wbr>&nbsp;ForwardIt destroy_n( ForwardIt first, Size n )<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; n &gt; 0; (void) ++first, &#8211;n)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::destroy_at(std::addressof(*first));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>The following example demonstrates how to use destroy_n to destroy a contiguous sequence of elements.<br />
 // Run this code </p>
<pre><code>#include &lt;memory&gt;

#include &lt;new&gt;

#include &lt;iostream&gt;
struct Tracer {
    int value;
    ~Tracer()
    {
        std::cout &lt;&lt; value &lt;&lt; &quot; destructed
&quot;;
    }
};
int main()

{
    alignas(Tracer) unsigned char buffer[sizeof(Tracer) * 8];
    for (int i = 0; i &lt; 8; ++i)
        new (buffer + sizeof(Tracer) * i) Tracer{i}; // manually construct objects
    auto ptr = std::launder(reinterpret_cast&lt;Tracer *&gt;(buffer));
    std::destroy_n(ptr, 8);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0 destructed<br />
&nbsp;<wbr>&nbsp;1 destructed<br />
&nbsp;<wbr>&nbsp;2 destructed<br />
&nbsp;<wbr>&nbsp;3 destructed<br />
&nbsp;<wbr>&nbsp;4 destructed<br />
&nbsp;<wbr>&nbsp;5 destructed<br />
&nbsp;<wbr>&nbsp;6 destructed<br />
&nbsp;<wbr>&nbsp;7 destructed</p>
<h2>See also</h2>
<p>destroy destroys a range of objects<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
destroy_at destroys an object at a given address<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
