---
title: "stdunderlying_type(3)"
name: "stdunderlying_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunderlying_type/"
---

std::underlying_type - std::underlying_type

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct underlying_type;</code></pre> 
If T is a complete enumeration type, provides a member typedef type that names the underlying type of T. 
Otherwise, the behavior is undefined. <i>(until C++20)</i> 
Otherwise, if T is not an enumeration type, there is no member type. Otherwise (T is an incomplete enumeration type), the program is ill-formed. <i>(since C++20)</i> 

<h2>Member types</h2>

Name Definition 
type the underlying type of T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using underlying_type_t = typename underlying_type&lt;T&gt;::type;

<h2>Notes</h2>

Each enumeration_type has an underlying type, which can be 
1. Specified explicitly (both scoped and unscoped enumerations) 
2. Omitted, in which case it is int for scoped enumerations or an implementation-defined integral type capable of representing all values of the enum (for unscoped enumerations) 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2396 C++11 incomplete enumeration types were allowed complete enumeration type required 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
enum e1 {};

enum class e2 : int {};
int main()
{
    bool e1_type = std::is_same&lt;
        unsigned, typename std::underlying_type&lt;e1&gt;::type&gt;::value;
    bool e2_type = std::is_same&lt;
        int, typename std::underlying_type&lt;e2&gt;::type&gt;::value;
    std::cout
        &lt;&lt; &quot;underlying type for 'e1' is &quot; &lt;&lt; (e1_type ? &quot;unsigned&quot; : &quot;non-unsigned&quot;) &lt;&lt; '\n'
        &lt;&lt; &quot;underlying type for 'e2' is &quot; &lt;&lt; (e2_type ? &quot;int&quot; : &quot;non-int&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;underlying type for 'e1' is unsigned 
&nbsp;<wbr>&nbsp;underlying type for 'e2' is int
