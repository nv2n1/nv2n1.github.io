---
title: "stdreference_wrapper(3)"
name: "stdreference_wrapper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreference_wrapper/"
---

std::reference_wrapper - std::reference_wrapper

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class T &gt;             (since C++11)

class reference_wrapper;</code></pre> 
std::reference_wrapper is a class template that wraps a reference in a copyable, assignable object. It is frequently used as a mechanism to store references inside standard containers (like std::vector) which cannot normally hold references. 
Specifically, std::reference_wrapper is a CopyConstructible and CopyAssignable wrapper around a reference to object or reference to function of type T. Instances of std::reference_wrapper are objects (they can be copied or stored in containers) but they are implicitly convertible to T&amp;, so that they can be used as arguments with the functions that take the underlying type by reference. 
If the stored reference is Callable, std::reference_wrapper is callable with the same arguments. 
Helper functions std::ref and std::cref are often used to generate std::reference_wrapper objects. 
std::reference_wrapper is also used to pass objects by reference to std::bind, the constructor of std::thread, or the helper functions std::make_pair and std::make_tuple. 
std::reference_wrapper is guaranteed to be TriviallyCopyable. <i>(since C++17)</i> 
T may be an incomplete type. <i>(since C++20)</i> 

<h2>Member types</h2>

type definition 
type T 
result_type(deprecated in C++17)(removed in C++20) The return type of T if T is a function. Otherwise, not defined 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1) if T is a function or pointer to function that takes one argument of type A1, then argument_type is A1. 
argument_type(deprecated in C++17)(removed in C++20) 2) if T is a pointer to member function of class T0 that takes no arguments, then argument_type is T0*, possibly cv-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3) if T is a class type with a member type T::argument_type, then argument_type is an alias of that 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1) if T is a function or pointer to function that takes two arguments of types A1 and A2, then first_argument_type is A1. 
first_argument_type(deprecated in C++17)(removed in C++20) 2) if T is a pointer to member function of class T0 that takes one argument, then first_argument_type is T0*, possibly cv-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3) if T is a class type with a member type T::first_argument_type, then first_argument_type is an alias of that 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1) if T is a function or pointer to function that takes two arguments of type s A1 and A2, then second_argument_type is A2. 
second_argument_type(deprecated in C++17)(removed in C++20) 2) if T is a pointer to member function of class T0 that takes one argument A1, then second_argument_type is A1, possibly cv-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3) if T is a class type with a member type T::second_argument_type, then second_argument_type is an alias of that

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores a reference in a new std::reference_wrapper object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rebinds a std::reference_wrapper 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the stored reference 
get <i>(public member function)</i> 
operator_T&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calls the stored function 
operator() <i>(public member function)</i> 

 

 
Deduction_guides<i>(since C++17)</i>

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; T&amp; FUN(T&amp; t) noexcept { return t; } 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; void FUN(T&amp;&amp;) = delete; 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;class reference_wrapper { 
&nbsp;<wbr>&nbsp;public: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef T type; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// construct/copy/destroy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class U, class = decltype( 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;detail::FUN&lt;T&gt;(std::declval&lt;U&gt;()), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::enable_if_t&lt;!std::is_same_v&lt;reference_wrapper, remove_cvref_t&lt;U&gt;&gt;&gt;() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference_wrapper(U&amp;&amp; u) noexcept(noexcept(detail::FUN&lt;T&gt;(std::forward&lt;U&gt;(u)))) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: _ptr(std::addressof(detail::FUN&lt;T&gt;(std::forward&lt;U&gt;(u)))) {} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference_wrapper(const reference_wrapper&amp;) noexcept = default; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// assignment 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference_wrapper&amp; operator=(const reference_wrapper&amp; x) noexcept = default; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// access 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;operator T&amp; () const noexcept { return *_ptr; } 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;T&amp; get() const noexcept { return *_ptr; } 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; class... ArgTypes &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::invoke_result_t&lt;T&amp;, ArgTypes...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;operator() ( ArgTypes&amp;&amp;... args ) const { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::invoke(get(), std::forward&lt;ArgTypes&gt;(args)...); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;private: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;T* _ptr; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;// deduction guides 
&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;reference_wrapper(T&amp;) -&gt; reference_wrapper&lt;T&gt;;

<h2>Example</h2>

Demonstrates the use of reference_wrapper as a container of references, which makes it possible to access the same container using multiple indexes 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;list&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;numeric&gt;

#include &lt;random&gt;

#include &lt;functional&gt;
int main()

{
    std::list&lt;int&gt; l(10);
    std::iota(l.begin(), l.end(), -4);
    std::vector&lt;std::reference_wrapper&lt;int&gt;&gt; v(l.begin(), l.end());
    // can't use shuffle on a list (requires random access), but can use it on a vector
    std::shuffle(v.begin(), v.end(), std::mt19937{std::random_device{}()});
    std::cout &lt;&lt; &quot;Contents of the list: &quot;;
    for (int n : l) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; &quot;\nContents of the list, as seen through a shuffled vector: &quot;;
    for (int i : v) {
        std::cout &lt;&lt; i &lt;&lt; ' ';
    }
    std::cout &lt;&lt; &quot;\n\nDoubling the values in the initial list...\n\n&quot;;
    for (int &amp;i : l) {
        i *= 2;
    }
    std::cout &lt;&lt; &quot;Contents of the list, as seen through a shuffled vector: &quot;;
    for (int i : v) {
        std::cout &lt;&lt; i &lt;&lt; ' ';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Contents of the list: -4 -3 -2 -1 0 1 2 3 4 5 
&nbsp;<wbr>&nbsp;Contents of the list, as seen through a shuffled vector: -1 2 -2 1 5 0 3 -3 -4 4 
&nbsp;<wbr>&nbsp;Doubling the values in the initial list... 
&nbsp;<wbr>&nbsp;Contents of the list, as seen through a shuffled vector: -2 4 -4 2 10 0 6 -6 -8 8

<h2>See also</h2>

ref 
cref creates a std::reference_wrapper with a type deduced from its argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
bind binds one or more arguments to a function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
