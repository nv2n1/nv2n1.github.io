---
title: "stdoperatorstdbasic_string(3)"
name: "stdoperatorstdbasic_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoperatorstdbasic_string/"
---

std::operator+(std::basic_string) - std::operator+(std::basic_string)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(1)

operator+(const basic_string&lt;CharT, Traits, Alloc&gt; &amp;lhs,

          const basic_string&lt;CharT, Traits, Alloc&gt; &amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(2)

operator+(const basic_string&lt;CharT, Traits, Alloc&gt; &amp;lhs,

          const CharT *rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(3)

operator+(const basic_string&lt;CharT, Traits, Alloc&gt; &amp;lhs,

          CharT rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(4)

operator+(const CharT *lhs,

          const basic_string&lt;CharT, Traits, Alloc&gt; &amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(5)

operator+(CharT lhs,

          const basic_string&lt;CharT, Traits, Alloc&gt; &amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(6)(since C++ 11)

operator+(basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;lhs,

          basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(7)(since C++ 11)

operator+(basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;lhs,

          const basic_string&lt;CharT, Traits, Alloc&gt; &amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(8)(since C++ 11)

operator+(basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;lhs,

          const CharT *rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(9)(since C++ 11)

operator+(basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;lhs,

          CharT rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(10)(since C++ 11)

operator+(const basic_string&lt;CharT, Traits, Alloc&gt; &amp;lhs,

          basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(11)(since C++ 11)

operator+(const CharT *lhs,

          basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

basic_string&lt;CharT, Traits, Alloc&gt;(12)(since C++ 11)

operator+(CharT lhs,

          basic_string&lt;CharT, Traits, Alloc&gt; &amp;&amp;rhs);</code></pre> 
Returns a string containing characters from lhs followed by the characters from rhs. 
The allocator used for the result is: 
1-3) std::allocator_traits&lt;Alloc&gt;::select_on_container_copy_construction(lhs.get_allocator()) 
4-5) std::allocator_traits&lt;Alloc&gt;::select_on_container_copy_construction(rhs.get_allocator()) 
6-9) lhs.get_allocator() <i>(since C++11)</i> 
10-12) rhs.get_allocator() 
In other words, if one operand is a basic_string rvalue, its allocator is used; otherwise, select_on_container_copy_construction is used on the allocator of the lvalue basic_string operand. In each case, the left operand is preferred when both are basic_strings of the same value category. 
For (6-12), all rvalue basic_string operands are left in valid but unspecified states. 

<h2>Parameters</h2>

lhs - string, character, or pointer to the first character in a null-terminated array 
rhs - string, character, or pointer to the first character in a null-terminated array

<h2>Return value</h2>

A string containing characters from lhs followed by the characters from rhs 
, using the allocator determined as above 
<i>(since C++11)</i>. 

<h2>Notes</h2>

operator+ should be used with great caution when stateful allocators are involved

(such as when std::pmr::string is used)

(since C++17). Prior to P1165R1, the allocator used for the result was determined by historical accident and can vary from overload to overload for no apparent reason. Moreover, for (1-5), the allocator propagation behavior varies across major standard library implementations and differs from the behavior depicted in the standard.

Because the allocator used by the result of operator+ is sensitive to value category, operator+ is not associative with respect to allocator propagation:
using my_string = std::basic_string&lt;char, std::char_traits&lt;char&gt;, my_allocator&lt;char&gt;&gt;;

my_string cat();

const my_string &amp;dog();
my_string meow = /* ... */, woof = /* ... */;
(since C++ 11)

        meow
    + cat() +
    /*...*/; // uses SOCCC on meow's allocator

woof + dog() + /*...*/; // uses allocator of dog()'s return value instead 
&nbsp;<wbr>&nbsp;meow + woof + meow; // uses SOCCC on meow's allocator 
&nbsp;<wbr>&nbsp;meow + (woof + meow); // uses SOCCC on woof's allocator instead 
For a chain of operator+ invocations, the allocator used for the ultimate result may be controlled by prepending an rvalue basic_string with the desired allocator: // use my_favorite_allocator for the final result

my_string(my_favorite_allocator) + meow + woof + cat() + dog(); 
For better and portable control over allocators, member functions like append(), insert(), and operator+=() should be used on a result string constructed with the desired allocator. 

<h2>Example</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    std::string s1 = &quot;Hello&quot;;
    std::string s2 = &quot;world&quot;;
    std::cout &lt;&lt; s1 + ' ' + s2 + &quot;!\n&quot;;
}


<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello world! 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
P1165R1 C++11 allocator propagation is haphazard and inconsistent made more consistent

<h2>See also</h2>

<pre><code>appends characters to the end

operator+= (public member function)
appends characters to the end

append     (public member function)
inserts characters

insert     (public member function)




</code></pre>
