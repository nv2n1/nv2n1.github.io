---
title: "stdmove(3)"
name: "stdmove"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmove/"
---

std::move - std::move

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;utility&gt;

template&lt; class T &gt;                                                          (since C++11)

typename std::remove_reference&lt;T&gt;::type&amp;&amp; move( T&amp;&amp; t ) noexcept;            (until C++14)

template&lt; class T &gt;                                                          (since C++14)

constexpr typename std::remove_reference&lt;T&gt;::type&amp;&amp; move( T&amp;&amp; t ) noexcept;</code></pre> 
std::move is used to indicate that an object t may be &quot;moved from&quot;, i.e. allowing the efficient transfer of resources from t to another object. 
In particular, std::move produces an xvalue_expression that identifies its argument t. It is exactly equivalent to a static_cast to an rvalue reference type. 

<h2>Parameters</h2>

t - the object to be moved

<h2>Return value</h2>

static_cast&lt;typename std::remove_reference&lt;T&gt;::type&amp;&amp;&gt;(t) 

<h2>Notes</h2>

The functions that accept rvalue reference parameters (including move_constructors, move_assignment_operators, and regular member functions such as std::vector::push_back) are selected, by overload_resolution, when called with rvalue arguments (either prvalues such as a temporary objects or xvalues such as the one produced by std::move). If the argument identifies a resource-owning object, these overloads have the option, but aren't required, to move any resources held by the argument. For example, a move constructor of a linked list might copy the pointer to the head of the list and store nullptr in the argument instead of allocating and copying individual nodes. 
Names of rvalue_reference variables are lvalues and have to be converted to xvalues to be bound to the function overloads that accept rvalue reference parameters, which is why move_constructors and move_assignment_operators typically use std::move: // Simple move constructor

A(A &amp;&amp;arg)
    : member(std::move(arg.member)) // the expression &quot;arg.member&quot; is lvalue

{
}

// Simple move assignment operator

A &amp;operator=(A &amp;&amp;other)
{
    member = std::move(other.member);
    return *this;
} 
One exception is when the type of the function parameter is rvalue reference to type template parameter (&quot;forwarding reference&quot; or &quot;universal reference&quot;), in which case std::forward is used instead. 
Unless otherwise specified, all standard library objects that have been moved from are placed in a valid but unspecified state. That is, only the functions without preconditions, such as the assignment operator, can be safely used on the object after it was moved from: std::vector&lt;std::string&gt; v;

std::string str = &quot;example&quot;;

v.push_back(std::move(str)); // str is now valid but unspecified

str.back(); // undefined behavior if size() == 0: back() has a precondition !empty()

str.clear(); // OK, clear() has no preconditions 
Also, the standard library functions called with xvalue arguments may assume the argument is the only reference to the object; if it was constructed from an lvalue with std::move, no aliasing checks are made. In particular, this means that standard library move assignment operators do not have to perform self-assignment checks: std::vector&lt;int&gt; v = {2, 3, 3};

v = std::move(v); // the value of v is unspecified


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;vector&gt;

#include &lt;string&gt;
int main()

{
    std::string str = &quot;Hello&quot;;
    std::vector&lt;std::string&gt; v;
    // uses the push_back(const T&amp;) overload, which means
    // we'll incur the cost of copying str
    v.push_back(str);
    std::cout &lt;&lt; &quot;After copy, str is \&quot;&quot; &lt;&lt; str &lt;&lt; &quot;\&quot;\n&quot;;
    // uses the rvalue reference push_back(T&amp;&amp;) overload,
    // which means no strings will be copied; instead, the contents
    // of str will be moved into the vector.  This is less
    // expensive, but also means str might now be empty.
    v.push_back(std::move(str));
    std::cout &lt;&lt; &quot;After move, str is \&quot;&quot; &lt;&lt; str &lt;&lt; &quot;\&quot;\n&quot;;
    std::cout &lt;&lt; &quot;The contents of the vector are \&quot;&quot; &lt;&lt; v[0]
              &lt;&lt; &quot;\&quot;, \&quot;&quot; &lt;&lt; v[1] &lt;&lt; &quot;\&quot;\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;After copy, str is &quot;Hello&quot; 
&nbsp;<wbr>&nbsp;After move, str is &quot;&quot; 
&nbsp;<wbr>&nbsp;The contents of the vector are &quot;Hello&quot;, &quot;Hello&quot;

<h2>See also</h2>

forward forwards a function argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
move_if_noexcept obtains an rvalue reference if the move constructor does not throw 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
move moves a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
