---
title: "stdremove_cvstdremove_conststdremove_volatile(3)"
name: "stdremove_cvstdremove_conststdremove_volatile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_cvstdremove_conststdremove_volatile/"
---

std::remove_cv,std::remove_const,std::remove_volatile - std::remove_cv,std::remove_const,std::remove_volatile

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct remove_cv;

template &lt;class T&gt;
(2)(since C++ 11)

    struct remove_const;

template &lt;class T&gt;
(3)(since C++ 11)

    struct remove_volatile;</code></pre> 
Provides the member typedef type which is the same as T, except that its topmost cv-qualifiers are removed. 
1) removes the topmost const, the topmost volatile, or both, if present. 
2) removes the topmost const 
3) removes the topmost volatile 

<h2>Member types</h2>

Name Definition 
type the type T without cv-qualifier

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using remove_cv_t = typename remove_cv&lt;T&gt;::type; 
template&lt; class T &gt; <i>(since C++14)</i> 
using remove_const_t = typename remove_const&lt;T&gt;::type; 
template&lt; class T &gt; <i>(since C++14)</i> 
using remove_volatile_t = typename remove_volatile&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;struct remove_cv { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::remove_volatile&lt;typename std::remove_const&lt;T&gt;::type&gt;::type type; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_const { typedef T type; }; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_const&lt;const T&gt; { typedef T type; }; 

 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_volatile { typedef T type; }; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_volatile&lt;volatile T&gt; { typedef T type; };

<h2>Example</h2>

Removing const/volatile from const volatile int * does not modify the type, because the pointer itself is neither const nor volatile. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()
{
    typedef std::remove_cv&lt;const int&gt;::type type1;
    typedef std::remove_cv&lt;volatile int&gt;::type type2;
    typedef std::remove_cv&lt;const volatile int&gt;::type type3;
    typedef std::remove_cv&lt;const volatile int *&gt;::type type4;
    typedef std::remove_cv&lt;int *const volatile&gt;::type type5;
    std::cout &lt;&lt; &quot;test1 &quot; &lt;&lt; (std::is_same&lt;int, type1&gt;::value ? &quot;passed&quot; : &quot;failed&quot;) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;test2 &quot; &lt;&lt; (std::is_same&lt;int, type2&gt;::value ? &quot;passed&quot; : &quot;failed&quot;) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;test3 &quot; &lt;&lt; (std::is_same&lt;int, type3&gt;::value ? &quot;passed&quot; : &quot;failed&quot;) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;test4 &quot; &lt;&lt; (std::is_same&lt;const volatile int *, type4&gt;::value ? &quot;passed&quot; : &quot;failed&quot;) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;test5 &quot; &lt;&lt; (std::is_same&lt;int *, type5&gt;::value ? &quot;passed&quot; : &quot;failed&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;test1 passed 
&nbsp;<wbr>&nbsp;test2 passed 
&nbsp;<wbr>&nbsp;test3 passed 
&nbsp;<wbr>&nbsp;test4 passed 
&nbsp;<wbr>&nbsp;test5 passed

<h2>See also</h2>

is_const checks if a type is const-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_volatile checks if a type is volatile-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
add_cv 
add_const 
add_volatile adds const or/and volatile specifiers to the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
remove_cvref combines std::remove_cv and std::remove_reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(C++20) 
