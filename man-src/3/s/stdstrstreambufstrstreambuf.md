---
title: "stdstrstreambufstrstreambuf(3)"
name: "stdstrstreambufstrstreambuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufstrstreambuf/"
---

std::strstreambuf::~strstreambuf - std::strstreambuf::~strstreambuf

<h2>Synopsis</h2>

<pre><code>virtual ~strstreambuf();</code></pre> 
Destroys a std::strstreambuf object. if the object is managing a dynamically-allocated buffer (the buffer state is &quot;allocated&quot;) and if the object is not frozen, then deallocates the buffer using the deallocation function provided at construction or delete[] if none was provided. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Notes</h2>

This destructor is typically called by the destructor of std::strstream 
If str() was called on a dynamic strstream and freeze(false) was not called after that, this destructor leaks memory. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
void *my_alloc(size_t n)

{
    std::cout &lt;&lt; &quot;my_alloc(&quot; &lt;&lt; n &lt;&lt; &quot;) called\n&quot;;
    return new char[n];
}
void my_free(void *p)

{
    std::cout &lt;&lt; &quot;my_free() called\n&quot;;
    delete[](char *) p;
}
int main()

{
    {
        std::strstreambuf buf(my_alloc, my_free);
        std::ostream s(&amp;buf);
        s &lt;&lt; 1.23 &lt;&lt; std::ends;
        std::cout &lt;&lt; buf.str() &lt;&lt; '\n';
        buf.freeze(false);
    } // destructor called here, buffer deallocated
    {
        std::strstreambuf buf(my_alloc, my_free);
        std::ostream s(&amp;buf);
        s &lt;&lt; 1.23 &lt;&lt; std::ends;
        std::cout &lt;&lt; buf.str() &lt;&lt; '\n';

        //        buf.freeze(false);
    } // destructor called here, memory leak!
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;my_alloc(4096) called 
&nbsp;<wbr>&nbsp;1.23 
&nbsp;<wbr>&nbsp;my_free() called 
&nbsp;<wbr>&nbsp;my_alloc(4096) called 
&nbsp;<wbr>&nbsp;1.23
