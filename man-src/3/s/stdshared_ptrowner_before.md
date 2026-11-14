---
title: "stdshared_ptrowner_before(3)"
name: "stdshared_ptrowner_before"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptrowner_before/"
---

std::shared_ptr&lt;T&gt;::owner_before - std::shared_ptr&lt;T&gt;::owner_before

<h2>Synopsis</h2>

<pre><code>template &lt;class Y&gt;
(until C++ 17)

    bool owner_before(const shared_ptr&lt;Y&gt; &amp;other) const;

template &lt;class Y&gt;
(since C++ 17)

    bool owner_before(const shared_ptr&lt;Y&gt; &amp;other) const noexcept;

template &lt;class Y&gt;
(until C++ 17)

    bool owner_before(const std::weak_ptr&lt;Y&gt; &amp;other) const;

template &lt;class Y&gt;
(since C++ 17)

    bool owner_before(const std::weak_ptr&lt;Y&gt; &amp;other) const noexcept;</code></pre> 
Checks whether this shared_ptr precedes other in implementation defined owner-based (as opposed to value-based) order. The order is such that two smart pointers compare equivalent only if they are both empty or if they both own the same object, even if the values of the pointers obtained by get() are different (e.g. because they point at different subobjects within the same object) 
This ordering is used to make shared and weak pointers usable as keys in associative containers, typically through std::owner_less. 

<h2>Parameters</h2>

other - the std::shared_ptr or std::weak_ptr to be compared

<h2>Return value</h2>

true if *this precedes other, false otherwise. Common implementations compare the addresses of the control blocks. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
struct Foo {
    int n1;
    int n2;
    Foo(int a, int b)
        : n1(a), n2(b)
    {
    }
};

int main()

{
    auto p1 = std::make_shared&lt;Foo&gt;(1, 2);
    std::shared_ptr&lt;int&gt; p2(p1, &amp;p1-&gt;n1);
    std::shared_ptr&lt;int&gt; p3(p1, &amp;p1-&gt;n2);
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;p2 &lt; p3 &quot; &lt;&lt; (p2 &lt; p3) &lt;&lt; '\n'
              &lt;&lt; &quot;p3 &lt; p2 &quot; &lt;&lt; (p3 &lt; p2) &lt;&lt; '\n'
              &lt;&lt; &quot;p2.owner_before(p3) &quot; &lt;&lt; p2.owner_before(p3) &lt;&lt; '\n'
              &lt;&lt; &quot;p3.owner_before(p2) &quot; &lt;&lt; p3.owner_before(p2) &lt;&lt; '\n';
    std::weak_ptr&lt;int&gt; w2(p2);
    std::weak_ptr&lt;int&gt; w3(p3);
    std::cout

        //              &lt;&lt; &quot;w2 &lt; w3 &quot; &lt;&lt; (w2 &lt; w3) &lt;&lt; '\n'  // won't compile

        //              &lt;&lt; &quot;w3 &lt; w2 &quot; &lt;&lt; (w3 &lt; w2) &lt;&lt; '\n'  // won't compile
        &lt;&lt; &quot;w2.owner_before(w3) &quot; &lt;&lt; w2.owner_before(w3) &lt;&lt; '\n'
        &lt;&lt; &quot;w3.owner_before(w2) &quot; &lt;&lt; w3.owner_before(w2) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;p2 &lt; p3 true 
&nbsp;<wbr>&nbsp;p3 &lt; p2 false 
&nbsp;<wbr>&nbsp;p2.owner_before(p3) false 
&nbsp;<wbr>&nbsp;p3.owner_before(p2) false 
&nbsp;<wbr>&nbsp;w2.owner_before(w3) false 
&nbsp;<wbr>&nbsp;w3.owner_before(w2) false

<h2>See also</h2>

owner_less provides mixed-type owner-based ordering of shared and weak pointers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
