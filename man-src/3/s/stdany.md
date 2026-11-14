---
title: "stdany(3)"
name: "stdany"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdany/"
---

std::any - std::any

<h2>Synopsis</h2>

Defined in header &lt;any&gt; 
class any; <i>(since C++17)</i> 
The class any describes a type-safe container for single values of any type. 
1) An object of class any stores an instance of any type that satisfies the constructor requirements or is empty, and this is referred to as the state of the class any object. The stored instance is called the contained object. Two states are equivalent if they are either both empty or if both are not empty and if the contained objects are equivalent. 
2) The non-member any_cast functions provide type-safe access to the contained object. 
Implementations are encouraged to avoid dynamic allocations for small objects, but such an optimization may only be applied to types for which std::is_nothrow_move_constructible returns true. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an any object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns an any object 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys an any object 
destructor <i>(public member function)</i>

<h2>Modifiers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;change the contained object, constructing the new object directly 
emplace <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys contained object 
reset <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two any objects 
swap <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if object holds a value 
has_value <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the typeid of the contained value 
type <i>(public member function)</i>

<h2>Non-member functions</h2>

std::swap(std::any) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 

 
any_cast type-safe access to the contained object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 

 
make_any creates an any object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i>

<h2>Helper classes</h2>

bad_any_cast exception thrown by the value-returning forms of any_cast on a type mismatch 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;any&gt;

#include &lt;iostream&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    // any type
    std::any a = 1;
    std::cout &lt;&lt; a.type().name() &lt;&lt; &quot;: &quot; &lt;&lt; std::any_cast&lt;int&gt;(a) &lt;&lt; '\n';
    a = 3.14;
    std::cout &lt;&lt; a.type().name() &lt;&lt; &quot;: &quot; &lt;&lt; std::any_cast&lt;double&gt;(a) &lt;&lt; '\n';
    a = true;
    std::cout &lt;&lt; a.type().name() &lt;&lt; &quot;: &quot; &lt;&lt; std::any_cast&lt;bool&gt;(a) &lt;&lt; '\n';
    // bad cast
    try {
        a = 1;
        std::cout &lt;&lt; std::any_cast&lt;float&gt;(a) &lt;&lt; '\n';
    } catch (const std::bad_any_cast &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
    // has value
    a = 1;
    if (a.has_value()) {
        std::cout &lt;&lt; a.type().name() &lt;&lt; '\n';
    }
    // reset
    a.reset();
    if (!a.has_value()) {
        std::cout &lt;&lt; &quot;no value\n&quot;;
    }
    // pointer to contained data
    a = 1;
    int *i = std::any_cast&lt;int&gt;(&amp;a);
    std::cout &lt;&lt; *i &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;i: 1 
&nbsp;<wbr>&nbsp;d: 3.14 
&nbsp;<wbr>&nbsp;b: true 
&nbsp;<wbr>&nbsp;bad any_cast 
&nbsp;<wbr>&nbsp;i 
&nbsp;<wbr>&nbsp;no value 
&nbsp;<wbr>&nbsp;1
