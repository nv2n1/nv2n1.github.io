---
title: "stdaligned_storage(3)"
name: "stdaligned_storage"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdaligned_storage/"
---

std::aligned_storage - std::aligned_storage

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;std::size_t Len, std::size_t Align = /*default-alignment*/&gt;
    (since C++ 11)

        struct aligned_storage;</code></pre> 
Provides the nested type type, which is a trivial standard-layout type suitable for use as uninitialized storage for any object whose size is at most Len and whose alignment_requirement is a divisor of Align. 
The default value of Align is the most stringent (the largest) alignment requirement for any object whose size is at most Len. If the default value is not used, Align must be the value of alignof(T) for some type T, or the behavior is undefined. 
The behavior is undefined if Len == 0. 
It is implementation-defined whether any extended_alignment is supported. 

<h2>Member types</h2>

Name Definition 
type the POD type of at least size Len with alignment requirement Align

<h2>Helper types</h2>

template&lt; std::size_t Len, std::size_t Align = /*default-alignment*/ &gt; <i>(since C++14)</i> 
using aligned_storage_t = typename aligned_storage&lt;Len, Align&gt;::type;

<h2>Notes</h2>

The type defined by std::aligned_storage&lt;&gt;::type can be used to create uninitialized memory blocks suitable to hold the objects of given type, optionally aligned stricter than their natural alignment requirement, for example on a cache or page boundary. 
As with any other uninitialized storage, the objects are created using placement_new and destroyed with explicit destructor calls. 

<h2>Possible implementation</h2>

Except for default argument, aligned_storage is expressible in terms of alignas: 

 

 
&nbsp;<wbr>&nbsp;template&lt;std::size_t Len, std::size_t Align /* default alignment not implemented */&gt; 
&nbsp;<wbr>&nbsp;struct aligned_storage { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct type { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alignas(Align) unsigned char data[Len]; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; 
&nbsp;<wbr>&nbsp;};

<h2>Example</h2>

A primitive static vector class, demonstrating creation, access, and destruction of objects in aligned storage 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;string&gt;
template &lt;class T, std::size_t N&gt;

class static_vector

{
    // properly aligned uninitialized storage for N T's
    typename std::aligned_storage&lt;sizeof(T), alignof(T)&gt;::type data[N];
    std::size_t m_size = 0;

  public:
    // Create an object in aligned storage
    template &lt;typename... Args&gt;
    void emplace_back(Args &amp;&amp;...args)
    {
        if (m_size &gt;= N) // possible error handling
            throw std::bad_alloc{};
        // construct value in memory of aligned storage
        // using inplace operator new
        new (&amp;data[m_size]) T(std::forward&lt;Args&gt;(args)...);
        ++m_size;
    }
    // Access an object in aligned storage
    const T &amp;operator[](std::size_t pos) const
    {
        // note: needs std::launder as of C++17
        return *reinterpret_cast&lt;const T *&gt;(&amp;data[pos]);
    }
    // Delete objects from aligned storage
    ~static_vector()
    {
        for (std::size_t pos = 0; pos &lt; m_size; ++pos) {
            // note: needs std::launder as of C++17
            reinterpret_cast&lt;T *&gt;(&amp;data[pos])-&gt;~T();
        }
    }
};
int main()

{
    static_vector&lt;std::string, 10&gt; v1;
    v1.emplace_back(5, '*');
    v1.emplace_back(10, '*');
    std::cout &lt;&lt; v1[0] &lt;&lt; '\n'
              &lt;&lt; v1[1] &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;***** 
&nbsp;<wbr>&nbsp;**********

<h2>See also</h2>

alignas_specifier specifies that the storage for the variable should be aligned by specific amount <i>(C++11)</i> 
alignment_of obtains the type's alignment requirements 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
aligned_union defines the type suitable for use as uninitialized storage for all given types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
max_align_t trivial type with alignment requirement as great as any other scalar type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
