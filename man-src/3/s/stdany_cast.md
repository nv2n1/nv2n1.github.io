---
title: "stdany_cast(3)"
name: "stdany_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdany_cast/"
---

std::any_cast - std::any_cast

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(1)(since C++ 17)

    T any_cast(const any &amp;operand);

template &lt;class T&gt;
(2)(since C++ 17)

    T any_cast(any &amp;operand);

template &lt;class T&gt;
(3)(since C++ 17)

    T any_cast(any &amp;&amp;operand);

template &lt;class T&gt;
(4)(since C++ 17)

    const T *any_cast(const any *operand) noexcept;

template &lt;class T&gt;
(5)(since C++ 17)

    T *any_cast(any *operand) noexcept;</code></pre> 
Performs type-safe access to the contained object. 
Let U be std::remove_cv_t&lt;std::remove_reference_t&lt;T&gt;&gt;. 
1) The program is ill-formed if std::is_constructible_v&lt;T, const U&amp;&gt; is false. 
2) The program is ill-formed if std::is_constructible_v&lt;T, U&amp;&gt; is false. 
3) The program is ill-formed if std::is_constructible_v&lt;T, U&gt; is false. 

<h2>Parameters</h2>

operand - target any object

<h2>Return value</h2>

1-2) Returns static_cast&lt;T&gt;(*std::any_cast&lt;U&gt;(&amp;operand)) 
3) Returns static_cast&lt;T&gt;(std::move(*std::any_cast&lt;U&gt;(&amp;operand))). 
4-5) If operand is not a null pointer, and the typeid of the requested T matches that of the contents of operand, a pointer to the value contained by operand, otherwise a null pointer. 

<h2>Exceptions</h2>

1-3) Throws std::bad_any_cast if the typeid of the requested T does not match that of the contents of operand.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;any&gt;

#include &lt;utility&gt;
int main()

{
    // simple example
    auto a = std::any(12);
    std::cout &lt;&lt; std::any_cast&lt;int&gt;(a) &lt;&lt; '\n';
    try {
        std::cout &lt;&lt; std::any_cast&lt;std::string&gt;(a) &lt;&lt; '\n';
    } catch (const std::bad_any_cast &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
    // pointer example
    if (int *i = std::any_cast&lt;int&gt;(&amp;a)) {
        std::cout &lt;&lt; &quot;a is int: &quot; &lt;&lt; *i &lt;&lt; '\n';
    } else if (std::string *s = std::any_cast&lt;std::string&gt;(&amp;a)) {
        std::cout &lt;&lt; &quot;a is std::string: &quot; &lt;&lt; *s &lt;&lt; '\n';
    } else {
        std::cout &lt;&lt; &quot;a is another type or unset\n&quot;;
    }
    // advanced example
    a = std::string(&quot;hello&quot;);
    auto &amp;ra = std::any_cast&lt;std::string &amp;&gt;(a); //&lt; reference
    ra[1] = 'o';
    std::cout &lt;&lt; &quot;a: &quot;
              &lt;&lt; std::any_cast&lt;const std::string &amp;&gt;(a) &lt;&lt; '\n'; //&lt; const reference
    auto b = std::any_cast&lt;std::string &amp;&amp;&gt;(std::move(a));       //&lt; rvalue reference
    // Note: 'b' is a move-constructed std::string,
    // 'a' is left in valid but unspecified state
    std::cout &lt;&lt; &quot;a: &quot; &lt;&lt; *std::any_cast&lt;std::string&gt;(&amp;a) //&lt; pointer
              &lt;&lt; &quot;b: &quot; &lt;&lt; b &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;12 
&nbsp;<wbr>&nbsp;bad any_cast 
&nbsp;<wbr>&nbsp;a is int: 12 
&nbsp;<wbr>&nbsp;a: hollo 
&nbsp;<wbr>&nbsp;a: b: hollo
