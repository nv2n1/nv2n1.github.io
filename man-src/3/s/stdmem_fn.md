---
title: "stdmem_fn(3)"
name: "stdmem_fn"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmem_fn/"
---

std::mem_fn - std::mem_fn

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class M, class T &gt;                 (since C++11)

/*unspecified*/ mem_fn(M T::* pm);           (until C++17)

template&lt; class M, class T &gt;                 (since C++17)

/*unspecified*/ mem_fn(M T::* pm) noexcept;</code></pre> 
Function template std::mem_fn generates wrapper objects for pointers to members, which can store, copy, and invoke a pointer to member. Both references and pointers (including smart pointers) to an object can be used when invoking a std::mem_fn. 

<h2>Parameters</h2>

pm - pointer to member that will be wrapped

<h2>Return value</h2>

std::mem_fn returns a call wrapper of unspecified type that has the following members: 
&nbsp;std::mem_fn Return type 

<h2>Member types</h2>

type definition <i>(until C++20)</i> 
result_type(deprecated in C++17) the return type of pm if pm is a pointer to member function, not defined for pointer to member object 
argument_type(deprecated in C++17) T*, possibly cv-qualified, if pm is a pointer to member function taking no arguments 
first_argument_type(deprecated in C++17) T* if pm is a pointer to member function taking one argument 
second_argument_type(deprecated in C++17) T1 if pm is a pointer to member function taking one argument of type T1

<h2>Member function</h2>

template&lt;class... Args&gt; 
/* see below */ operator()(Args&amp;&amp;... args); 

 
Let fn be the call wrapper returned by a call to std::mem_fn with a pointer to member pm. Then the expression fn(t, a2, ..., aN) is equivalent to INVOKE(pm, t, a2, ..., aN), where INVOKE is the operation defined in Callable. (Thus, the return type of operator() is std::result_of&lt;decltype(pm)(Args&amp;&amp;...)&gt;::type.) 
Each argument in args is perfectly forwarded, as if by std::forward&lt;Args&gt;(args)....

<h2>Example</h2>

Use mem_fn to store and execute a member function and a member object: 
 // Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
struct Foo {
    void display_greeting()
    {
        std::cout &lt;&lt; &quot;Hello, world.\n&quot;;
    }
    void display_number(int i)
    {
        std::cout &lt;&lt; &quot;number: &quot; &lt;&lt; i &lt;&lt; '\n';
    }
    int data = 7;
};
int main()
{
    Foo f;
    auto greet = std::mem_fn(&amp;Foo::display_greeting);
    greet(f);
    auto print_num = std::mem_fn(&amp;Foo::display_number);
    print_num(f, 42);
    auto access_data = std::mem_fn(&amp;Foo::data);
    std::cout &lt;&lt; &quot;data: &quot; &lt;&lt; access_data(f) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello, world. 
&nbsp;<wbr>&nbsp;number: 42 
&nbsp;<wbr>&nbsp;data: 7 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2048 C++11 unnecessary overloads provided removed

<h2>See also</h2>

function wraps callable object of any type with specified function call signature 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
bind binds one or more arguments to a function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
