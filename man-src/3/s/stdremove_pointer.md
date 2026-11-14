---
title: "stdremove_pointer(3)"
name: "stdremove_pointer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_pointer/"
---

std::remove_pointer - std::remove_pointer

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct remove_pointer;</code></pre> 
Provides the member typedef type which is the type pointed to by T, or, if T is not a pointer, then type is the same as T. 

<h2>Member types</h2>

Name Definition 
type the type pointed to by T or T if it's not a pointer

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using remove_pointer_t = typename remove_pointer&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_pointer {typedef T type;}; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_pointer&lt;T*&gt; {typedef T type;}; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_pointer&lt;T* const&gt; {typedef T type;}; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_pointer&lt;T* volatile&gt; {typedef T type;}; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_pointer&lt;T* const volatile&gt; {typedef T type;};

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
template &lt;class T1, class T2&gt;

void print_is_same()

{
    std::cout &lt;&lt; std::is_same&lt;T1, T2&gt;() &lt;&lt; '\n';
}
void print_separator()

{
    std::cout &lt;&lt; &quot;-----\n&quot;;
}
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    print_is_same&lt;int, int&gt;();    // true
    print_is_same&lt;int, int *&gt;();  // false
    print_is_same&lt;int, int **&gt;(); // false
    print_separator();
    print_is_same&lt;int, std::remove_pointer&lt;int&gt;::type&gt;();    // true
    print_is_same&lt;int, std::remove_pointer&lt;int *&gt;::type&gt;();  // true
    print_is_same&lt;int, std::remove_pointer&lt;int **&gt;::type&gt;(); // false
    print_separator();
    print_is_same&lt;int, std::remove_pointer&lt;int *const&gt;::type&gt;();          // true
    print_is_same&lt;int, std::remove_pointer&lt;int *volatile&gt;::type&gt;();       // true
    print_is_same&lt;int, std::remove_pointer&lt;int *const volatile&gt;::type&gt;(); // true
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;----- 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;----- 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true

<h2>See also</h2>

is_pointer checks if a type is a pointer type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
add_pointer adds a pointer to the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
