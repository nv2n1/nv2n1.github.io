---
title: "stddeclval(3)"
name: "stddeclval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddeclval/"
---

std::declval - std::declval

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    template &lt;class T&gt;
    (since C++ 11)

        typename std::add_rvalue_reference&lt;T&gt;::type declval() noexcept;
Converts any type T to a reference type, making it possible to use member functions in decltype expressions without the need to go through constructors.

declval is commonly used in templates where acceptable template parameters may have no constructor in common, but have the same member function whose return type is needed.

Note that because no definition exists for declval, it can only be used in unevaluated_contexts;
it is an error to evaluate an expression that contains this function.Formally, the program is ill - formed if this function is odr - used.
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Cannot be called and thus never returns a value. The return type is T&amp;&amp; unless T is (possibly cv-qualified) void, in which case the return type is T.


<h2>Example</h2>

// Run this code <pre><code>#include &lt;utility&gt;

#include &lt;iostream&gt;
struct Default {
    int foo() const
    {
        return 1;
    }
};
struct NonDefault

{
    NonDefault(const NonDefault &amp;)
    {
    }
    int foo() const
    {
        return 1;
    }
};
int main()

{
    decltype(Default().foo()) n1 = 1; // type of n1 is int

    //  decltype(NonDefault().foo()) n2 = n1;               // error: no default constructor
    decltype(std::declval&lt;NonDefault&gt;().foo()) n2 = n1; // type of n2 is int
    std::cout &lt;&lt; &quot;n1 = &quot; &lt;&lt; n1 &lt;&lt; '\n'
              &lt;&lt; &quot;n2 = &quot; &lt;&lt; n2 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;n1 = 1 
&nbsp;<wbr>&nbsp;n2 = 1

<h2>See also</h2>

decltype_specifier defines a type equivalent to the type of an expression <i>(C++11)</i> 
result_of 
invoke_result deduces the result type of invoking a callable object with a set of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i>(removed in C++20) 
<i>(C++17)</i> 
