---
title: "stddestroy_at(3)"
name: "stddestroy_at"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddestroy_at/"
---

std::destroy_at - std::destroy_at

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T&gt;
    (since C++ 17)

        void destroy_at(T *p);</code></pre> 
Calls the destructor of the object pointed to by p, as if by p-&gt;~T(). 

<h2>Parameters</h2>

p - a pointer to the object to be destroyed

<h2>Return value</h2>

<i>(none)</i> 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;void destroy_at(T* p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p-&gt;~T(); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following example demonstrates how to use destroy_at to destroy a contiguous sequence of elements. 
 // Run this code <pre><code>#include &lt;memory&gt;

#include &lt;new&gt;

#include &lt;iostream&gt;
struct Tracer {
    int value;
    ~Tracer()
    {
        std::cout &lt;&lt; value &lt;&lt; &quot; destructed\n&quot;;
    }
};
int main()

{
    alignas(Tracer) unsigned char buffer[sizeof(Tracer) * 8];
    for (int i = 0; i &lt; 8; ++i)
        new (buffer + sizeof(Tracer) * i) Tracer{i}; // manually construct objects
    auto ptr = std::launder(reinterpret_cast&lt;Tracer *&gt;(buffer));
    for (int i = 0; i &lt; 8; ++i)
        std::destroy_at(ptr + i);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 destructed 
&nbsp;<wbr>&nbsp;1 destructed 
&nbsp;<wbr>&nbsp;2 destructed 
&nbsp;<wbr>&nbsp;3 destructed 
&nbsp;<wbr>&nbsp;4 destructed 
&nbsp;<wbr>&nbsp;5 destructed 
&nbsp;<wbr>&nbsp;6 destructed 
&nbsp;<wbr>&nbsp;7 destructed

<h2>See also</h2>

destroy destroys a range of objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
destroy_n destroys a number of objects in a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
