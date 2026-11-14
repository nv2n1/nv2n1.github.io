---
title: "stdmake_move_iterator(3)"
name: "stdmake_move_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_move_iterator/"
---

std::make_move_iterator - std::make_move_iterator

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class Iter&gt;
    (since C++ 11)

        std::move_iterator&lt;Iter&gt; make_move_iterator(const Iter &amp;i);
(until C++ 14)

    template &lt;class Iter&gt;
    (since C++ 14)

        std::move_iterator&lt;Iter&gt; make_move_iterator(Iter i);
(until C++ 17)

    template &lt;class Iter&gt;
    (since C++ 17)

        constexpr std::move_iterator&lt;Iter&gt; make_move_iterator(Iter i);</code></pre> 
make_move_iterator is a convenience function template that constructs a std::move_iterator for the given iterator i with the type deduced from the type of the argument. 

<h2>Parameters</h2>

i - input iterator to be converted to move iterator

<h2>Return value</h2>

A std::move_iterator which can be used to move from the elements accessed through i 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class Iter &gt; 
&nbsp;<wbr>&nbsp;constexpr std::move_iterator&lt;Iter&gt; make_move_iterator( Iter i ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::move_iterator&lt;Iter&gt;(i); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;list&gt;

#include &lt;vector&gt;

#include &lt;string&gt;

#include &lt;iterator&gt;
int main()

{
    std::list&lt;std::string&gt; s{&quot;one&quot;, &quot;two&quot;, &quot;three&quot;};
    std::vector&lt;std::string&gt; v1(s.begin(), s.end()); // copy
    std::vector&lt;std::string&gt; v2(std::make_move_iterator(s.begin()),
                                std::make_move_iterator(s.end())); // move
    std::cout &lt;&lt; &quot;v1 now holds: &quot;;
    for (auto str : v1)
        std::cout &lt;&lt; &quot;\&quot;&quot; &lt;&lt; str &lt;&lt; &quot;\&quot; &quot;;
    std::cout &lt;&lt; &quot;\nv2 now holds: &quot;;
    for (auto str : v2)
        std::cout &lt;&lt; &quot;\&quot;&quot; &lt;&lt; str &lt;&lt; &quot;\&quot; &quot;;
    std::cout &lt;&lt; &quot;\noriginal list now holds: &quot;;
    for (auto str : s)
        std::cout &lt;&lt; &quot;\&quot;&quot; &lt;&lt; str &lt;&lt; &quot;\&quot; &quot;;
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;v1 now holds: &quot;one&quot; &quot;two&quot; &quot;three&quot; 
&nbsp;<wbr>&nbsp;v2 now holds: &quot;one&quot; &quot;two&quot; &quot;three&quot; 
&nbsp;<wbr>&nbsp;original list now holds: &quot;&quot; &quot;&quot; &quot;&quot;

<h2>See also</h2>

move_iterator iterator adaptor which dereferences to an rvalue reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
move obtains an rvalue reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
