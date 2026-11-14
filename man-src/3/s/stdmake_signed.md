---
title: "stdmake_signed(3)"
name: "stdmake_signed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_signed/"
---

std::make_signed - std::make_signed

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct make_signed;</code></pre> 
If T is an integral (except bool) or enumeration type, provides the member typedef type which is the signed integer type corresponding to T, with the same cv-qualifiers. 
Otherwise, the behavior is undefined. 

<h2>Member types</h2>

Name Definition 
type the signed integer type corresponding to T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using make_signed_t = typename make_signed&lt;T&gt;::type;

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()
{
    typedef std::make_signed&lt;unsigned char&gt;::type char_type;
    typedef std::make_signed&lt;unsigned int&gt;::type int_type;
    typedef std::make_signed&lt;volatile unsigned long&gt;::type long_type;
    bool ok1 = std::is_same&lt;char_type, signed char&gt;::value;
    bool ok2 = std::is_same&lt;int_type, signed int&gt;::value;
    bool ok3 = std::is_same&lt;long_type, volatile signed long&gt;::value;
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;char_type is 'signed char'?          : &quot; &lt;&lt; ok1 &lt;&lt; '\n'
              &lt;&lt; &quot;int_type  is 'signed int'?           : &quot; &lt;&lt; ok2 &lt;&lt; '\n'
              &lt;&lt; &quot;long_type is 'volatile signed long'? : &quot; &lt;&lt; ok3 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;char_type is 'signed char'? : true 
&nbsp;<wbr>&nbsp;int_type is 'signed int'? : true 
&nbsp;<wbr>&nbsp;long_type is 'volatile signed long'? : true

<h2>See also</h2>

is_signed checks if a type is a signed arithmetic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_unsigned checks if a type is an unsigned arithmetic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
make_unsigned makes the given integral type unsigned 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
