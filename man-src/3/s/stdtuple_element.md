---
title: "stdtuple_element(3)"
name: "stdtuple_element"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtuple_element/"
---

std::tuple_element&lt;std::tuple&gt; - std::tuple_element&lt;std::tuple&gt;

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;tuple&gt;

    template &lt;std::size_t I, class T&gt;
    (1)(since C++ 11)

        class tuple_element; /* undefined */

template &lt;std::size_t I, class... Types&gt;
(2)(since C++ 11)

    class tuple_element&lt;I, tuple&lt;Types...&gt;&gt;;

Defined in header&lt;tuple&gt;

    Defined in header&lt;array&gt;(since C++ 17)

        Defined in header&lt;utility&gt;(since C++ 17)

            Defined in header&lt;ranges&gt;(since C++ 20)

                Defined in header&lt;span&gt;(since C++ 20)

                    template &lt;std::size_t I, class T&gt;

                    class tuple_element&lt;I, const T&gt;
{

    typedef typename(3)(since C++ 11)

        std::add_const&lt;typename std::tuple_element&lt;I, T&gt;::type&gt;::type type;
};

template &lt;std::size_t I, class T&gt;

class tuple_element&lt;I, volatile T&gt;
{

    typedef typename(4)(since C++ 11)

        std::add_volatile&lt;typename std::tuple_element&lt;I, T&gt;::type&gt;::type type;
};

template &lt;std::size_t I, class T&gt;

class tuple_element&lt;I, const volatile T&gt;
{

    typedef typename(5)(since C++ 11)

        std::add_cv&lt;typename std::tuple_element&lt;I, T&gt;::type&gt;::type type;
};</code></pre> 
Provides compile-time indexed access to the types of the elements of the tuple. 

<h2>Member types</h2>

Member type Definition 
type the type of Ith element of the tuple, where I is in [0, sizeof...(Types))

<h2>Helper types</h2>

template &lt;std::size_t I, class T&gt; <i>(since C++14)</i> 
using tuple_element_t = typename tuple_element&lt;I, T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; std::size_t I, class T &gt; 
&nbsp;<wbr>&nbsp;struct tuple_element; 

 
&nbsp;<wbr>&nbsp;// recursive case 
&nbsp;<wbr>&nbsp;template&lt; std::size_t I, class Head, class... Tail &gt; 
&nbsp;<wbr>&nbsp;struct tuple_element&lt;I, std::tuple&lt;Head, Tail...&gt;&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::tuple_element&lt;I-1, std::tuple&lt;Tail...&gt;&gt; { }; 

 
&nbsp;<wbr>&nbsp;// base case 
&nbsp;<wbr>&nbsp;template&lt; class Head, class... Tail &gt; 
&nbsp;<wbr>&nbsp;struct tuple_element&lt;0, std::tuple&lt;Head, Tail...&gt;&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef Head type; 
&nbsp;<wbr>&nbsp;};

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;
template &lt;class... Args&gt;

struct type_list

{
    template &lt;std::size_t N&gt;
    using type = typename std::tuple_element&lt;N, std::tuple&lt;Args...&gt;&gt;::type;
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    type_list&lt;int, char, bool&gt;::type&lt;2&gt; x = true;
    std::cout &lt;&lt; x &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the type of the elements of array 
std::tuple_element&lt;std::array&gt; <i>(class template specialization)</i> 
std::tuple_element&lt;std::pair&gt; obtains the type of the elements of pair 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
<i>(C++11)</i> 
