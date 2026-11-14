---
title: "stdbeginstdcbegin(3)"
name: "stdbeginstdcbegin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbeginstdcbegin/"
---

std::begin,std::cbegin - std::begin,std::cbegin

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (since C++ 11)

        auto begin(C &amp;c) -&gt; decltype(c.begin());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto begin(C &amp;c) -&gt; decltype(c.begin());

template &lt;class C&gt;
(since C++ 11)

    auto begin(const C &amp;c) -&gt; decltype(c.begin());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto begin(const C &amp;c) -&gt; decltype(c.begin());
(1)

    template &lt;class T, std::size_t N&gt;
    (since C++ 11)

        T *begin(T (&amp;array)[N]);
(1)(until C++ 14)

    template &lt;class T, std::size_t N&gt;
    (since C++ 14)

        constexpr T *begin(T (&amp;array)[N]) noexcept;
(2)

    template &lt;class C&gt;

    constexpr auto cbegin(const C &amp;c) noexcept(/* see below */)(3)(since C++ 14)

        -&gt; decltype(std::begin(c));</code></pre> 
Returns an iterator to the beginning of the given container c or array array. These templates rely on C::begin() having a reasonable implementation. 
1) Returns exactly c.begin(), which is typically an iterator to the beginning of the sequence represented by c. If C is a standard Container, this returns C::iterator when c is not const-qualified, and C::const_iterator otherwise. 
2) Returns a pointer to the beginning of the array. 
3) Returns exactly std::begin(c), with c always treated as const-qualified. If C is a standard Container, this always returns C::const_iterator. 
&nbsp;range-begin-end.svg 
&nbsp;This section is incomplete 
&nbsp;Reason: an explanation why cbegin was introduced 

<h2>Parameters</h2>

c - a container with a begin method 
array - an array of arbitrary type

<h2>Return value</h2>

An iterator to the beginning of c or array 

<h2>Exceptions</h2>

3) 
noexcept specification: 
noexcept(noexcept(std::begin(c)))

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::begin and std::cbegin are guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt; 
, &lt;string_view&gt; 
<i>(since C++17)</i>, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 
User-defined overloads 
Custom overloads of begin may be provided for classes that do not expose a suitable begin() member function, yet can be iterated. The following overloads are already provided by the standard library: 
std::begin(std::initializer_list) specializes std::begin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
std::begin(std::valarray) specializes std::begin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support 
begin(std::filesystem::directory_iterator) <i>(function)</i> 
end(std::filesystem::directory_iterator) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support 
begin(std::filesystem::recursive_directory_iterator) <i>(function)</i> 
end(std::filesystem::recursive_directory_iterator) 
Similar to the use of swap (described in Swappable), typical use of the begin function in generic context is an equivalent of using std::begin; begin(arg);, which allows both the ADL-selected overloads for user-defined types and the standard library function templates to appear in the same overload set. template &lt;typename Container, typename Function&gt;

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
int main()

{
    std::vector&lt;int&gt; v = {3, 1, 4};
    auto vi = std::begin(v);
    std::cout &lt;&lt; *vi &lt;&lt; '\n';
    int a[] = {-5, 10, 15};
    auto ai = std::begin(a);
    std::cout &lt;&lt; *ai &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;-5

<h2>See also</h2>

end 
cend returns an iterator to the end of a container or array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++14)</i> 
