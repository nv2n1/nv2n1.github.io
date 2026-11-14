---
title: "stdexperimentalpropagate_const(3)"
name: "stdexperimentalpropagate_const"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_const/"
---

std::experimental::propagate_const - std::experimental::propagate_const

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/propagate_const&gt;

template&lt;class T&gt;                                 (library fundamentals TS v2)

class propagate_const;</code></pre> 
std::experimental::propagate_const is a const-propagating wrapper for pointers and pointer-like objects. It treats the wrapped pointer as a pointer to const when accessed through a const access path, hence the name. 
The class satisfies the requirements of MoveConstructible and MoveAssignable if the underlying pointer-like type satisfies the corresponding requirement, but propagate_const is neither CopyConstructible nor CopyAssignable. 

<h2>Type requirements</h2>

- 
T must be an object pointer type or a pointer-like class type, as specified below. The program is ill-formed if T is an array type, reference type, pointer to function type, pointer to (possibly cv-qualified) void, or if decltype(*std::declval&lt;T&amp;&gt;()) is not an lvalue reference type. 

 

 
Requirements on pointer-like class types 

 
If T is a class type, it must satisfy the requirements in this subsection. 
Given 

 
* t, a modifiable lvalue_expression of type T 
* ct, a const T&amp; bound to T 
* element_type, an object type 

 
The following expressions must be valid and have their specified effects: 

 
Expression Return type Pre-conditions Operational semantics 
t.get() element_type* 
ct.get() element_type* or const element_type* t.get() == ct.get() 
*t element_type&amp; t.get() != nullptr *t refers to the same object as *(t.get()) 
*ct element_type&amp; or const element_type&amp; ct.get() != nullptr *ct refers to the same object as *(ct.get()) 
t.operator-&gt;() element_type* t.get() != nullptr t.operator-&gt;() == t.get() 
ct.operator-&gt;() element_type* or const element_type* ct.get() != nullptr ct.operator-&gt;() == ct.get() 
(bool)t bool (bool)t is equivalent to t.get() != nullptr 
(bool)ct bool (bool)ct is equivalent to ct.get() != nullptr 

 
Further, T and const T shall be contextually convertible to bool. 
In addition, if T is implicitly convertible to element_type*, then (element_type*)t shall be equal to t.get(). Similarly, if const T is implicitly convertible to const element_type*, then (const element_type*)ct shall be equal to ct.get().

<h2>Member types</h2>

Member type Definition 
element_type std::remove_reference_t&lt;decltype(*std::declval&lt;T&amp;&gt;())&gt;, the type of the object pointed to by T

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new propagate_const 
constructor <i>(public member function)</i> 

 
destructor destructs an propagate_const, destroying the contained pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(implicitly declared) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the propagate_const object 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the wrapped pointer 
swap <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the object pointed to by the wrapped pointer 
get <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the wrapped pointer is null 
operator_bool <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dereferences the wrapped pointer 
operator* <i>(public member function)</i> 
operator-&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implicit conversion function to pointer 
operator_element_type* <i>(public member function)</i> 
operator_const_element_type*

<h2>Non-member functions</h2>

operator== 
operator!= compares to another propagate_const, another pointer, or with nullptr 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes the swap algorithm 
std::experimental::swap(std::experimental::propagate_const) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Retrieves a reference to the wrapped pointer-like object 
get_underlying <i>(function template)</i>

<h2>Helper classes</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hash support for propagate_const 
std::hash&lt;std::experimental::propagate_const&gt; <i>(class template specialization)</i> 

 
std::equal_to&lt;std::experimental::propagate_const&gt; 
std::not_equal_to&lt;std::experimental::propagate_const&gt; Specializations of the standard comparison function objects for propagate_const 
std::less&lt;std::experimental::propagate_const&gt; <i>(class template specialization)</i> 
std::greater&lt;std::experimental::propagate_const&gt; 
std::less_equal&lt;std::experimental::propagate_const&gt; 
std::greater_equal&lt;std::experimental::propagate_const&gt;

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;experimental/propagate_const&gt;
struct X

{
    void g() const
    {
        std::cout &lt;&lt; &quot;g (const)\n&quot;;
    }
    void g()
    {
        std::cout &lt;&lt; &quot;g (non-const)\n&quot;;
    }
};
struct Y

{
    Y()
        : m_ptrX(std::make_unique&lt;X&gt;())
    {
    }
    void f() const
    {
        std::cout &lt;&lt; &quot;f (const)\n&quot;;
        m_ptrX-&gt;g();
    }
    void f()
    {
        std::cout &lt;&lt; &quot;f (non-const)\n&quot;;
        m_ptrX-&gt;g();
    }
    std::experimental::propagate_const&lt;std::unique_ptr&lt;X&gt;&gt; m_ptrX;
};
int main()

{
    Y y;
    y.f();
    const Y cy;
    cy.f();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;f (non-const) 
&nbsp;<wbr>&nbsp;g (non-const) 
&nbsp;<wbr>&nbsp;f (const) 
&nbsp;<wbr>&nbsp;g (const)
