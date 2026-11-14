---
title: "stdmove_if_noexcept(3)"
name: "stdmove_if_noexcept"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmove_if_noexcept/"
---

std::move_if_noexcept - std::move_if_noexcept

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    template &lt;class T&gt;

    typename std::conditional&lt;

        !std::is_nothrow_move_constructible&lt;T&gt;::value &amp;&amp; std::is_copy_constructible&lt;T&gt;::value, (since C++ 11)

                                                                                                   const T &amp;,
        (until C++ 14)

            T &amp;&amp;

        &gt;::type
    move_if_noexcept(T &amp;x) noexcept;

template &lt;class T&gt;

constexpr typename std::conditional&lt;

    !std::is_nothrow_move_constructible&lt;T&gt;::value &amp;&amp; std::is_copy_constructible&lt;T&gt;::value, (since C++ 14)

                                                                                               const T &amp;,

    T &amp;&amp;

    &gt;::type
move_if_noexcept(T &amp;x) noexcept;</code></pre> 
move_if_noexcept obtains an rvalue reference to its argument if its move constructor does not throw exceptions or if there is no copy constructor (move-only type), otherwise obtains an lvalue reference to its argument. It is typically used to combine move semantics with strong exception guarantee. 

<h2>Parameters</h2>

x - the object to be moved or copied

<h2>Return value</h2>

std::move(x) or x, depending on exception guarantees. 

<h2>Notes</h2>

This is used, for example, by std::vector::resize, which may have to allocate new storage and then move or copy elements from old storage to new storage. If an exception occurs during this operation, std::vector::resize undoes everything it did to this point, which is only possible if std::move_if_noexcept was used to decide whether to use move construction or copy construction. (unless copy constructor is not available, in which case move constructor is used either way and the strong exception guarantee may be waived) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;
struct Bad

{
    Bad()
    {
    }
    Bad(Bad &amp;&amp;) // may throw
    {
        std::cout &lt;&lt; &quot;Throwing move constructor called\n&quot;;
    }
    Bad(const Bad &amp;) // may throw as well
    {
        std::cout &lt;&lt; &quot;Throwing copy constructor called\n&quot;;
    }
};
struct Good

{
    Good()
    {
    }
    Good(Good &amp;&amp;) noexcept // will NOT throw
    {
        std::cout &lt;&lt; &quot;Non-throwing move constructor called\n&quot;;
    }
    Good(const Good &amp;) noexcept // will NOT throw
    {
        std::cout &lt;&lt; &quot;Non-throwing copy constructor called\n&quot;;
    }
};
int main()

{
    Good g;
    Bad b;
    Good g2 = std::move_if_noexcept(g);
    Bad b2 = std::move_if_noexcept(b);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Non-throwing move constructor called 
&nbsp;<wbr>&nbsp;Throwing copy constructor called

<h2>Complexity</h2>

Constant

<h2>See also</h2>

forward forwards a function argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
move obtains an rvalue reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
