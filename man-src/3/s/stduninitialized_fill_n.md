---
title: "stduninitialized_fill_n(3)"
name: "stduninitialized_fill_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduninitialized_fill_n/"
description: "std::uninitialized_fill_n – std::uninitialized_fill_n"
---

<p>std::uninitialized_fill_n &#8211; std::uninitialized_fill_n</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class ForwardIt, class Size, class T&gt;
    (until C++ 11)

        void uninitialized_fill_n(ForwardIt first, Size count, const T &amp;value);

template &lt;class ForwardIt, class Size, class T&gt;
(1)(since C++ 11)

    ForwardIt uninitialized_fill_n(ForwardIt first, Size count, const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt, class Size, class T&gt;
(2)(since C++ 17)

    ForwardIt uninitialized_fill_n(ExecutionPolicy &amp;&amp;policy, ForwardIt first, Size count, const T &amp;value);</code></pre>
<p>1) Copies the given value value to the first count elements in an uninitialized memory area beginning at first as if by for (; n&#8211;; ++first)<br />
    ::new (static_cast&lt;void *&gt;(std::addressof(*first)))<br />
        typename std::iterator_traits&lt;ForwardIt&gt;::value_type(x);<br />
If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first &#8211; the beginning of the range of the elements to initialize<br />
count &#8211; number of elements to construct<br />
value &#8211; the value to construct the elements with</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
No increment, assignment, comparison, or indirection through valid instances of ForwardIt may throw exceptions.</p>
<h2>Return value</h2>
<p><i>(none)</i> <i>(until C++11)</i><br />
Iterator to the element past the last element copied. <i>(since C++11)</i> </p>
<h2>Complexity</h2>
<p>Linear in count.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class ForwardIt, class Size, class T &gt;<br />
&nbsp;<wbr>&nbsp;ForwardIt uninitialized_fill_n(ForwardIt first, Size count, const T&amp; value)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::iterator_traits&lt;ForwardIt&gt;::value_type Value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt current = first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;try {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; count &gt; 0; ++current, (void) &#8211;count) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;::new (static_cast&lt;void*&gt;(std::addressof(*current))) Value(value);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return current;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} catch (&#8230;) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != current; ++first) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first-&gt;~Value();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;throw;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;string&gt;

#include &lt;tuple&gt;
int main()

{
    std::string *p;
    std::size_t sz;
    std::tie(p, sz) = std::get_temporary_buffer&lt;std::string&gt;(4);
    std::uninitialized_fill_n(p, sz, &quot;Example&quot;);
    for (std::string *i = p; i != p + sz; ++i) {
        std::cout &lt;&lt; *i &lt;&lt; '
';
        i-&gt;~basic_string&lt;char&gt;();
    }
    std::return_temporary_buffer(p);
}
</code></pre>
<h2>Output:</h2>
<h2>Example</h2>
<h2>Example</h2>
<h2>Example</h2>
<h2>Example</h2>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies an object to an uninitialized area of memory, defined by a range<br />
uninitialized_fill <i>(function template)</i> </p>
