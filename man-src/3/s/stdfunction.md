---
title: "stdfunction(3)"
name: "stdfunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfunction/"
---

std::function - std::function

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class &gt;                   (since C++11)

class function; /* undefined */

template&lt; class R, class... Args &gt;  (since C++11)

class function&lt;R(Args...)&gt;;</code></pre> 
Class template std::function is a general-purpose polymorphic function wrapper. Instances of std::function can store, copy, and invoke any Callable target -- functions, lambda_expressions, bind_expressions, or other function objects, as well as pointers to member functions and pointers to data members. 
The stored callable object is called the target of std::function. If a std::function contains no target, it is called empty. Invoking the target of an empty std::function results in std::bad_function_call exception being thrown. 
std::function satisfies the requirements of CopyConstructible and CopyAssignable. 

<h2>Member types</h2>

Type Definition 
result_type R 
argument_type(deprecated in C++17)(removed in C++20) T if sizeof...(Args)==1 and T is the first and only type in Args... 
first_argument_type(deprecated in C++17)(removed in C++20) T1 if sizeof...(Args)==2 and T1 is the first of the two types in Args... 
second_argument_type(deprecated in C++17)(removed in C++20) T2 if sizeof...(Args)==2 and T2 is the second of the two types in Args...

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new std::function instance 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a std::function instance 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns a new target 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 

 
assign assigns a new target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(until C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a valid target is contained 
operator_bool <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes the target 
operator() <i>(public member function)</i>

<h2>Target access</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the typeid of the stored target 
target_type <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a pointer to the stored target 
target <i>(public member function)</i>

<h2>Non-member functions</h2>

std::swap(std::function) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a std::function with nullptr 
operator== <i>(function template)</i> 
operator!=

<h2>Helper classes</h2>

std::uses_allocator&lt;std::function&gt; specializes the std::uses_allocator type trait 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
<i>(C++11)</i> <i>(until C++17)</i> 

 

 
Deduction_guides<i>(since C++17)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
struct Foo {
    Foo(int num)
        : num_(num)
    {
    }
    void print_add(int i) const
    {
        std::cout &lt;&lt; num_ + i &lt;&lt; '\n';
    }
    int num_;
};
void print_num(int i)

{
    std::cout &lt;&lt; i &lt;&lt; '\n';
}
struct PrintNum {
    void operator()(int i) const
    {
        std::cout &lt;&lt; i &lt;&lt; '\n';
    }
};
int main()

{
    // store a free function
    std::function&lt;void(int)&gt; f_display = print_num;
    f_display(-9);
    // store a lambda
    std::function&lt;void()&gt; f_display_42 = []() { print_num(42); };
    f_display_42();
    // store the result of a call to std::bind
    std::function&lt;void()&gt; f_display_31337 = std::bind(print_num, 31337);
    f_display_31337();
    // store a call to a member function
    std::function&lt;void(const Foo &amp;, int)&gt; f_add_display = &amp;Foo::print_add;
    const Foo foo(314159);
    f_add_display(foo, 1);
    f_add_display(314159, 1);
    // store a call to a data member accessor
    std::function&lt;int(Foo const &amp;)&gt; f_num = &amp;Foo::num_;
    std::cout &lt;&lt; &quot;num_: &quot; &lt;&lt; f_num(foo) &lt;&lt; '\n';
    // store a call to a member function and object
    using std::placeholders::_1;
    std::function&lt;void(int)&gt; f_add_display2 = std::bind(&amp;Foo::print_add, foo, _1);
    f_add_display2(2);
    // store a call to a member function and object ptr
    std::function&lt;void(int)&gt; f_add_display3 = std::bind(&amp;Foo::print_add, &amp;foo, _1);
    f_add_display3(3);
    // store a call to a function object
    std::function&lt;void(int)&gt; f_display_obj = PrintNum();
    f_display_obj(18);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;-9 
&nbsp;<wbr>&nbsp;42 
&nbsp;<wbr>&nbsp;31337 
&nbsp;<wbr>&nbsp;314160 
&nbsp;<wbr>&nbsp;314160 
&nbsp;<wbr>&nbsp;num_: 314159 
&nbsp;<wbr>&nbsp;314161 
&nbsp;<wbr>&nbsp;314162 
&nbsp;<wbr>&nbsp;18

<h2>See also</h2>

bad_function_call the exception thrown when invoking an empty std::function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
mem_fn creates a function object out of a pointer to a member 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
