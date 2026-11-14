---
title: "stdtype_infohash_code(3)"
name: "stdtype_infohash_code"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_infohash_code/"
---

std::type_info::hash_code - std::type_info::hash_code

<h2>Synopsis</h2>

<pre><code>size_t hash_code() const;
(since C++ 11)</code></pre> 
Returns an unspecified value such that for all type_info objects referring to the same type, their hash_code() is the same. 
No other guarantees are given: type_info objects referring to different types may have the same hash_code (although the standard recommends that implementations avoid this as much as possible), and hash_code for the same type can change between invocations of the same program. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A value that is identical for all type_info objects referring to the same type. 

<h2>Example</h2>

The following program is an example of an efficient type-value mapping without using std::type_index. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;typeinfo&gt;

#include &lt;unordered_map&gt;

#include &lt;string&gt;

#include &lt;functional&gt;

#include &lt;memory&gt;
struct A {
    virtual ~A()
    {
    }
};
struct B : A {
};

struct C : A {
};
using TypeInfoRef = std::reference_wrapper&lt;const std::type_info&gt;;
struct Hasher {
    std::size_t operator()(TypeInfoRef code) const
    {
        return code.get().hash_code();
    }
};
struct EqualTo {
    bool operator()(TypeInfoRef lhs, TypeInfoRef rhs) const
    {
        return lhs.get() == rhs.get();
    }
};
int main()

{
    std::unordered_map&lt;TypeInfoRef, std::string, Hasher, EqualTo&gt; type_names;
    type_names[typeid(int)] = &quot;int&quot;;
    type_names[typeid(double)] = &quot;double&quot;;
    type_names[typeid(A)] = &quot;A&quot;;
    type_names[typeid(B)] = &quot;B&quot;;
    type_names[typeid(C)] = &quot;C&quot;;
    int i;
    double d;
    A a;
    // note that we're storing pointer to type A
    std::unique_ptr&lt;A&gt; b(new B);
    std::unique_ptr&lt;A&gt; c(new C);
    std::cout &lt;&lt; &quot;i is &quot; &lt;&lt; type_names[typeid(i)] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;d is &quot; &lt;&lt; type_names[typeid(d)] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;a is &quot; &lt;&lt; type_names[typeid(a)] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;b is &quot; &lt;&lt; type_names[typeid(*b)] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;c is &quot; &lt;&lt; type_names[typeid(*c)] &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;i is int 
&nbsp;<wbr>&nbsp;d is double 
&nbsp;<wbr>&nbsp;a is A 
&nbsp;<wbr>&nbsp;b is B 
&nbsp;<wbr>&nbsp;c is C

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the objects refer to the same type 
operator== <i>(public member function)</i> 
operator!= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implementation defined name of the type 
name <i>(public member function)</i> 
