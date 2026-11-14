---
title: "stddestroy(3)"
name: "stddestroy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddestroy/"
description: "std::destroy – std::destroy"
---

<p>std::destroy &#8211; std::destroy</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class ForwardIt&gt;
    (1)(since C++ 17)

        void destroy(ForwardIt first, ForwardIt last);

template &lt;class ExecutionPolicy, class ForwardIt&gt;
(2)(since C++ 17)

    void destroy(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last);</code></pre>
<p>1) Destroys the objects in the range [first, last), as if by for (; first != last; ++first)<br />
    std::destroy_at(std::addressof(*first));<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to destroy<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
No increment, assignment, comparison, or indirection through valid instances of ForwardIt may throw exceptions.</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Complexity</h2>
<p>Linear in the distance between first and last.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class ForwardIt &gt;<br />
&nbsp;<wbr>&nbsp;void destroy( ForwardIt first, ForwardIt last )<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::destroy_at(std::addressof(*first));<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>The following example demonstrates how to use destroy to destroy a contiguous sequence of elements.<br />
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
    std::destroy(ptr, ptr + 8);
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
<p>destroy_n destroys a number of objects in a range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
destroy_at destroys an object at a given address<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
