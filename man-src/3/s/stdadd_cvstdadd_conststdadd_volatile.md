---
title: "stdadd_cvstdadd_conststdadd_volatile(3)"
name: "stdadd_cvstdadd_conststdadd_volatile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdadd_cvstdadd_conststdadd_volatile/"
---

std::add_cv,std::add_const,std::add_volatile - std::add_cv,std::add_const,std::add_volatile

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct add_cv;

template &lt;class T&gt;
(2)(since C++ 11)

    struct add_const;

template &lt;class T&gt;
(3)(since C++ 11)

    struct add_volatile;</code></pre> 
Provides the member typedef type which is the same as T, except it has a cv-qualifier added (unless T is a function, a reference, or already has this cv-qualifier) 
1) adds both const and volatile 
2) adds const 
3) adds volatile 

<h2>Member types</h2>

Name Definition 
type the type T with the cv-qualifier

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using add_cv_t = typename add_cv&lt;T&gt;::type; 
template&lt; class T &gt; <i>(since C++14)</i> 
using add_const_t = typename add_const&lt;T&gt;::type; 
template&lt; class T &gt; <i>(since C++14)</i> 
using add_volatile_t = typename add_volatile&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;struct add_cv { typedef const volatile T type; }; 

 
&nbsp;<wbr>&nbsp;template&lt; class T&gt; struct add_const { typedef const T type; }; 

 
&nbsp;<wbr>&nbsp;template&lt; class T&gt; struct add_volatile { typedef volatile T type; };

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct foo

{
    void m()
    {
        std::cout &lt;&lt; &quot;Non-cv\n&quot;;
    }
    void m() const
    {
        std::cout &lt;&lt; &quot;Const\n&quot;;
    }
    void m() volatile
    {
        std::cout &lt;&lt; &quot;Volatile\n&quot;;
    }
    void m() const volatile
    {
        std::cout &lt;&lt; &quot;Const-volatile\n&quot;;
    }
};
int main()

{
    foo{}.m();
    std::add_const&lt;foo&gt;::type{}.m();
    std::add_volatile&lt;foo&gt;::type{}.m();
    std::add_cv&lt;foo&gt;::type{}.m();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Non-cv 
&nbsp;<wbr>&nbsp;Const 
&nbsp;<wbr>&nbsp;Volatile 
&nbsp;<wbr>&nbsp;Const-volatile

<h2>See also</h2>

is_const checks if a type is const-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_volatile checks if a type is volatile-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
remove_cv 
remove_const 
remove_volatile removes const or/and volatile specifiers from the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
as_const obtains a reference to const to its argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
