---
title: "stdexchange(3)"
name: "stdexchange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexchange/"
---

std::exchange - std::exchange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;utility&gt;

template&lt; class T, class U = T &gt;                (since C++14)

T exchange( T&amp; obj, U&amp;&amp; new_value );            (until C++20)

template&lt; class T, class U = T &gt;                (since C++20)

constexpr T exchange( T&amp; obj, U&amp;&amp; new_value );</code></pre> 
Replaces the value of obj with new_value and returns the old value of obj. 

<h2>Parameters</h2>

obj - object whose value to replace 
new_value - the value to assign to obj

<h2>Type requirements</h2>

- 
T must meet the requirements of MoveConstructible. Also, it must be possible to move-assign objects of type U to objects of type T

<h2>Return value</h2>

The old value of obj 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class T, class U = T&gt; 
&nbsp;<wbr>&nbsp;T exchange(T&amp; obj, U&amp;&amp; new_value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;T old_value = std::move(obj); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obj = std::forward&lt;U&gt;(new_value); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return old_value; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

This function can be used when implementing move_assignment_operators and move_constructors: struct S

{
    int *p;
    int n;
    S(S &amp;&amp;other)
        : p{std::exchange(other.p, nullptr)}, n{std::exchange(other.n, 0)}
    {
    }
    S &amp;operator=(S &amp;&amp;other)
    {
        p = std::exchange(other.p, nullptr); // move p, while leaving nullptr in other.p
        n = std::exchange(other.n, 0);       // move n, while leaving zero in other.n
        return *this;
    }
};


<h2>Example</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt; 
&nbsp;<wbr>&nbsp;class stream 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;public: using flags_type = int; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;public: flags_type flags() const
{
    return flags_;
}
/// Replaces flags_ by newf, and returns the old value.
flags_type flags(flags_type newf)
{
    return std::exchange(flags_, newf);
} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;private: <pre><code>flags_type flags_ = 0;
}
;
void f()
{
    std::cout &lt;&lt; &quot;f()&quot;;
}
int main()

{
    stream s;
    std::cout &lt;&lt; s.flags() &lt;&lt; '\n';
    std::cout &lt;&lt; s.flags(12) &lt;&lt; '\n';
    std::cout &lt;&lt; s.flags() &lt;&lt; &quot;\n\n&quot;;
    std::vector&lt;int&gt; v;
    // Since the second template parameter has a default value, it is possible
    // to use a braced-init-list as second argument. The expression below
    // is equivalent to std::exchange(v, std::vector&lt;int&gt;{1,2,3,4});
    std::exchange(v, {1, 2, 3, 4});
    std::copy(begin(v), end(v), std::ostream_iterator&lt;int&gt;(std::cout, &quot;, &quot;));
    std::cout &lt;&lt; &quot;\n\n&quot;;
    void (*fun)();
    // the default value of template parameter also makes possible to use a
    // normal function as second argument. The expression below is equivalent to
    // std::exchange(fun, static_cast&lt;void(*)()&gt;(f))
    std::exchange(fun, f);
    fun();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 
&nbsp;<wbr>&nbsp;0 
&nbsp;<wbr>&nbsp;12 

 
&nbsp;<wbr>&nbsp;1, 2, 3, 4, 

 
&nbsp;<wbr>&nbsp;f()

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
atomic_exchange 
atomic_exchange_explicit atomically replaces the value of the atomic object with non-atomic argument and returns the old value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
