---
title: "stdmake_unsigned(3)"
name: "stdmake_unsigned"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_unsigned/"
---

std::make_unsigned - std::make_unsigned

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct make_unsigned;</code></pre> 
If T is an integral (except bool) or enumeration type, provides the member typedef type which is the unsigned integer type corresponding to T, with the same cv-qualifiers. The unsigned integer type corresponding to an enumeration type is the unsigned integer type with the smallest rank having the same sizeof as the enumeration. 
Otherwise, the behavior is undefined. 

<h2>Member types</h2>

Name Definition 
type the unsigned integer type corresponding to T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using make_unsigned_t = typename make_unsigned&lt;T&gt;::type;

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()
{
    typedef std::make_unsigned&lt;char&gt;::type char_type;
    typedef std::make_unsigned&lt;int&gt;::type int_type;
    typedef std::make_unsigned&lt;volatile long&gt;::type long_type;
    bool ok1 = std::is_same&lt;char_type, unsigned char&gt;::value;
    bool ok2 = std::is_same&lt;int_type, unsigned int&gt;::value;
    bool ok3 = std::is_same&lt;long_type, volatile unsigned long&gt;::value;
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;char_type is 'unsigned char'?          : &quot; &lt;&lt; ok1 &lt;&lt; '\n'
              &lt;&lt; &quot;int_type  is 'unsigned int'?           : &quot; &lt;&lt; ok2 &lt;&lt; '\n'
              &lt;&lt; &quot;long_type is 'volatile unsigned long'? : &quot; &lt;&lt; ok3 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;char_type is 'unsigned char'? : true 
&nbsp;<wbr>&nbsp;int_type is 'unsigned int'? : true 
&nbsp;<wbr>&nbsp;long_type is 'volatile unsigned long'? : true

<h2>See also</h2>

is_signed checks if a type is a signed arithmetic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_unsigned checks if a type is an unsigned arithmetic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
make_signed makes the given integral type signed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
