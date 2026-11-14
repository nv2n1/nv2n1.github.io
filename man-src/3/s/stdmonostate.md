---
title: "stdmonostate(3)"
name: "stdmonostate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmonostate/"
---

std::monostate - std::monostate

<h2>Synopsis</h2>

Defined in header &lt;variant&gt; 
struct monostate { }; <i>(since C++17)</i> 
Unit type intended for use as a well-behaved empty alternative in std::variant. In particular, a variant of non-default-constructible types may list std::monostate as its first alternative: this makes the variant itself default-constructible. 

<h2>Member functions</h2>

constructor trivial implicit default/copy/move constructor 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(implicitly declared) 

 
destructor trivial implicit destructor 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(implicitly declared) 

 
operator= trivial implicit copy/move assignment 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(implicitly declared)

<h2>Non-member functions</h2>

constexpr bool operator&lt;(monostate, monostate) noexcept { return false; } 
constexpr bool operator&gt;(monostate, monostate) noexcept { return false; } 
constexpr bool operator&lt;=(monostate, monostate) noexcept { return true; } 
constexpr bool operator&gt;=(monostate, monostate) noexcept { return true; } 
constexpr bool operator==(monostate, monostate) noexcept { return true; } 
constexpr bool operator!=(monostate, monostate) noexcept { return false; } 

 
All instances of std::monostate compare equal.

<h2>Helper classes</h2>

&nbsp;std::hash&lt;std::monostate&gt; 

 

 
template &lt;&gt; struct std::hash&lt;monostate&gt;; 

 
Specializes the std::hash algorithm for std::monostate.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;variant&gt;

#include &lt;iostream&gt;
struct S

{
    S(int i)
        : i(i)
    {
    }
    int i;
};
int main()
{
    // Without the monostate type this declaration will fail.
    // This is because S is not default-constructible.
    std::variant&lt;std::monostate, S&gt; var;
    // var.index() is now 0 - the first element
    // std::get&lt;S&gt; will throw! We need to assign a value
    var = 12;
    std::cout &lt;&lt; std::get&lt;S&gt;(var).i &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;12

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the variant object 
constructor <i>(public member function)</i> 
