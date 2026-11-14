---
title: "stdremove_cvref(3)"
name: "stdremove_cvref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_cvref/"
---

std::remove_cvref - std::remove_cvref

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 20)

        struct remove_cvref;</code></pre> 
If the type T is a reference type, provides the member typedef type which is the type referred to by T with its topmost cv-qualifiers removed. Otherwise type is T with its topmost cv-qualifiers removed. 

<h2>Member types</h2>

Name Definition 
type the type referred by T or T itself if it is not a reference, with top-level cv-qualifiers removed

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++20)</i> 
using remove_cvref_t = typename remove_cvref&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;struct remove_cvref { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef std::remove_cv_t&lt;std::remove_reference_t&lt;T&gt;&gt; type; 
&nbsp;<wbr>&nbsp;};

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;int&gt;, int&gt; &lt;&lt; '\n'
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;int &amp;&gt;, int&gt; &lt;&lt; '\n'
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;int &amp;&amp;&gt;, int&gt; &lt;&lt; '\n'
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;const int &amp;&gt;, int&gt; &lt;&lt; '\n'
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;const int[2]&gt;, int[2]&gt; &lt;&lt; '\n'
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;const int(&amp;)[2]&gt;, int[2]&gt; &lt;&lt; '\n'
              &lt;&lt; std::is_same_v&lt;std::remove_cvref_t&lt;int(int)&gt;, int(int)&gt; &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true

<h2>See also</h2>

remove_cv 
remove_const 
remove_volatile removes const or/and volatile specifiers from the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
remove_reference removes a reference from the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
decay applies type transformations as when passing a function argument by value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
