---
title: "stdendstdcend(3)"
name: "stdendstdcend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdendstdcend/"
---

std::end,std::cend - std::end,std::cend

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (since C++ 11)

        auto end(C &amp;c) -&gt; decltype(c.end());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto end(C &amp;c) -&gt; decltype(c.end());

template &lt;class C&gt;
(since C++ 11)

    auto end(const C &amp;c) -&gt; decltype(c.end());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto end(const C &amp;c) -&gt; decltype(c.end());
(1)

    template &lt;class T, std::size_t N&gt;
    (since C++ 11)

        T *end(T (&amp;array)[N]);
(1)(until C++ 14)

    template &lt;class T, std::size_t N&gt;
    (since C++ 14)

        constexpr T *end(T (&amp;array)[N]) noexcept;
(2)

    template &lt;class C&gt;

    constexpr auto cend(const C &amp;c) noexcept(/* see below */)(3)(since C++ 14)

        -&gt; decltype(std::end(c));</code></pre> 
Returns an iterator to the end (i.e. the element after the last element) of the given container c or array array. These templates rely on C::end() having a reasonable implementation. 
1) Returns exactly c.end(), which is typically an iterator one past the end of the sequence represented by c. If C is a standard Container, this returns a C::iterator when c is not const-qualified, and a C::const_iterator otherwise. 
2) Returns a pointer to the end of the array array. 
3) Returns exactly std::end(c), with c always treated as const-qualified. If C is a standard Container, this always returns a C::const_iterator. 
&nbsp;range-begin-end.svg 

<h2>Parameters</h2>

c - a container with an end method 
array - an array of arbitrary type

<h2>Return value</h2>

An iterator to the end of c or array. Note that the end of a container or array is defined as the element following the last valid element. 

<h2>Exceptions</h2>

3) 
noexcept specification: 
noexcept(noexcept(std::end(c)))

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::end and std::cend are guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt; 
, &lt;string_view&gt; 
<i>(since C++17)</i>, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 
User-defined overloads 
Custom overloads of end may be provided for classes that do not expose a suitable end() member function, yet can be iterated. The following overloads are already provided by the standard library: 
std::end(std::initializer_list) specializes std::end 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
std::end(std::valarray) specializes std::end 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support 
begin(std::filesystem::directory_iterator) <i>(function)</i> 
end(std::filesystem::directory_iterator) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support 
begin(std::filesystem::recursive_directory_iterator) <i>(function)</i> 
end(std::filesystem::recursive_directory_iterator) 
Similar to the use of swap (described in Swappable), typical use of the end function in generic context is an equivalent of using std::end; end(arg);, which lets both the ADL-selected overloads for user-defined types and the standard library function templates to appear in the same overload set. template &lt;typename Container, typename Function&gt;

void for_each(Container &amp;&amp;cont, Function f)
{
    using std::begin;
    auto it = begin(cont);
    using std::end;
    auto end_it = end(cont);
    while (it != end_it) {
        f(*it);
        ++it;
    }
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;
int main()

{
    std::vector&lt;int&gt; v = {3, 1, 4};
    if (std::find(std::begin(v), std::end(v), 5) != std::end(v)) {
        std::cout &lt;&lt; &quot;found a 5 in vector v!\n&quot;;
    }
    int a[] = {5, 10, 15};
    if (std::find(std::begin(a), std::end(a), 5) != std::end(a)) {
        std::cout &lt;&lt; &quot;found a 5 in array a!\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;found a 5 in array a!

<h2>See also</h2>

begin 
cbegin returns an iterator to the beginning of a container or array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++14)</i> 
