---
title: "stdinitializer_list(3)"
name: "stdinitializer_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinitializer_list/"
---

std::initializer_list - std::initializer_list

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;initializer_list&gt;

template&lt; class T &gt;                   (since C++11)

class initializer_list;</code></pre> 
An object of type std::initializer_list&lt;T&gt; is a lightweight proxy object that provides access to an array of objects of type const T. 
A std::initializer_list object is automatically constructed when: 
* a braced-init-list is used to list-initialize an object, where the corresponding constructor accepts an std::initializer_list parameter 
* a braced-init-list is used as the right operand of assignment or as a function_call_argument, and the corresponding assignment operator/function accepts an std::initializer_list parameter 
* a braced-init-list is bound to auto, including in a ranged_for_loop 
Initializer lists may be implemented as a pair of pointers or pointer and length. Copying a std::initializer_list does not copy the underlying objects. 
The underlying array is not guaranteed to exist after the lifetime of the original initializer list object has ended. The storage for std::initializer_list is unspecified (i.e. it could be automatic, temporary, or static read-only memory, depending on the situation). <i>(until C++14)</i> 
The underlying array is a temporary array of type const T[N], in which each element is copy-initialized (except that narrowing conversions are invalid) from the corresponding element of the original initializer list. The lifetime of the underlying array is the same as any other temporary_object, except that initializing an initializer_list object from the array extends the lifetime of the array exactly like binding_a_reference_to_a_temporary (with the same exceptions, such as for initializing a non-static class member). The underlying array may be allocated in read-only memory. <i>(since C++14)</i> 
The program is ill-formed if an explicit or partial specialization of std::initializer_list is declared. <i>(since C++17)</i> 

<h2>Member types</h2>

Member type Definition 
value_type T 
reference const T&amp; 
const_reference const T&amp; 
size_type std::size_t 
iterator const T* 
const_iterator const T*

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates an empty initializer list 
constructor <i>(public member function)</i>

<h2>Capacity</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of elements in the initializer list 
size <i>(public member function)</i>

<h2>Iterators</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the first element 
begin <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to one past the last element 
end <i>(public member function)</i>

<h2>Non-member functions</h2>

std::begin(std::initializer_list) specializes std::begin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 

 
std::end(std::initializer_list) specializes std::end 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
Defined in header &lt;iterator&gt; 

 
rbegin(std::initializer_list) specializes std::rbegin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++14)</i> 

 
rend(std::initializer_list) specializes std::rend 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++14)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;initializer_list&gt;
template &lt;class T&gt;

struct S {
    std::vector&lt;T&gt; v;
    S(std::initializer_list&lt;T&gt; l)
        : v(l)
    {
        std::cout &lt;&lt; &quot;constructed with a &quot; &lt;&lt; l.size() &lt;&lt; &quot;-element list\n&quot;;
    }
    void append(std::initializer_list&lt;T&gt; l)
    {
        v.insert(v.end(), l.begin(), l.end());
    }
    std::pair&lt;const T *, std::size_t&gt; c_arr() const
    {
        return {&amp;v[0], v.size()}; // copy list-initialization in return statement
                                  // this is NOT a use of std::initializer_list
    }
};
template &lt;typename T&gt;

void templated_fn(T)
{
}
int main()

{
    S&lt;int&gt; s = {1, 2, 3, 4, 5}; // copy list-initialization
    s.append({6, 7, 8});        // list-initialization in function call
    std::cout &lt;&lt; &quot;The vector size is now &quot; &lt;&lt; s.c_arr().second &lt;&lt; &quot; ints:\n&quot;;
    for (auto n : s.v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;Range-for over brace-init-list: \n&quot;;
    for (int x : {-1, -2, -3}) // the rule for auto makes this ranged-for work
        std::cout &lt;&lt; x &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    auto al = {10, 11, 12}; // special rule for auto
    std::cout &lt;&lt; &quot;The list bound to auto has size() = &quot; &lt;&lt; al.size() &lt;&lt; '\n';
    //    templated_fn({1, 2, 3}); // compiler error! &quot;{1, 2, 3}&quot; is not an expression,
    // it has no type, and so T cannot be deduced
    templated_fn&lt;std::initializer_list&lt;int&gt;&gt;({1, 2, 3}); // OK
    templated_fn&lt;std::vector&lt;int&gt;&gt;({1, 2, 3});           // also OK
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;constructed with a 5-element list 
&nbsp;<wbr>&nbsp;The vector size is now 8 ints: 
&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8 
&nbsp;<wbr>&nbsp;Range-for over brace-init-list: 
&nbsp;<wbr>&nbsp;-1 -2 -3 
&nbsp;<wbr>&nbsp;The list bound to auto has size() = 3
