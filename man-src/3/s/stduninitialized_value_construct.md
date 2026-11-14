---
title: "stduninitialized_value_construct(3)"
name: "stduninitialized_value_construct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduninitialized_value_construct/"
description: "std::uninitialized_value_construct – std::uninitialized_value_construct"
---

<p>std::uninitialized_value_construct &#8211; std::uninitialized_value_construct</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class ForwardIt&gt;
    (1)(since C++ 17)

        void uninitialized_value_construct(ForwardIt first, ForwardIt last);

template &lt;class ExecutionPolicy, class ForwardIt&gt;
(2)(since C++ 17)

    void uninitialized_value_construct(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last);</code></pre>
<p>1) Constructs objects of type typename iterator_traits&lt;ForwardIt&gt;::value_type in the uninitialized storage designated by the range [first, last) by value-initialization, as if by </p>
<pre><code>for (; first != last; ++first)
    ::new (static_cast&lt;void *&gt;(std::addressof(*first)))
        typename std::iterator_traits&lt;ForwardIt&gt;::value_type();</code></pre>
<p>If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of the elements to initialize<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
No increment, assignment, comparison, or indirection through valid instances of ForwardIt may throw exceptions.</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Complexity</h2>
<p>Linear in the distance between first and last</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt;<br />
&nbsp;<wbr>&nbsp;void uninitialized_value_construct(ForwardIt first, ForwardIt last)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using Value = typename std::iterator_traits&lt;ForwardIt&gt;::value_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt current = first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;try {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; current != last; ++current) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;::new (static_cast&lt;void*&gt;(std::addressof(*current))) Value();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} catch (&#8230;) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::destroy(first, current);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;throw;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>uninitialized_value_construct_n constructs objects by value-initialization in an uninitialized area of memory, defined by a start and a count<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
uninitialized_default_construct constructs objects by default-initialization in an uninitialized area of memory, defined by a range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
