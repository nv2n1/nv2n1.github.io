---
title: "stdhashstdstringstdwstringstdu16stringstdu32stringstdpmrstringstdpmrwstringstdpmru16stringstdpmru32string(3)"
name: "stdhashstdstringstdwstringstdu16stringstdu32stringstdpmrstringstdpmrwstringstdpmru16stringstdpmru32string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdstringstdwstringstdu16stringstdu32stringstdpmrstringstdpmrwstringstdpmru16stringstdpmru32string/"
---

std::hash(std::string,std::wstring,std::u16string,std::u32string,std::pmr::string,std::pmr::wstring,std::pmr::u16string,std::pmr::u32string) - std::hash(std::string,std::wstring,std::u16string,std::u32string,std::pmr::string,std::pmr::wstring,std::pmr::u16string,std::pmr::u32string)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;string&gt;

    template &lt;&gt;
    struct hash&lt;std::string&gt;;

template &lt;&gt;
struct hash&lt;std::wstring&gt;;

template &lt;&gt;
struct hash&lt;std::u8string&gt;; // c++20  (since C++11)

template &lt;&gt;
struct hash&lt;std::u16string&gt;;

template &lt;&gt;
struct hash&lt;std::u32string&gt;;

template &lt;&gt;
struct hash&lt;std::pmr::string&gt;;

template &lt;&gt;
struct hash&lt;std::pmr::wstring&gt;;

template &lt;&gt;
struct hash&lt;std::pmr::u8string&gt;;
(since C++ 20)

    template &lt;&gt;
    struct hash&lt;std::pmr::u16string&gt;;

template &lt;&gt;
struct hash&lt;std::pmr::u32string&gt;;</code></pre> 
The template specializations of std::hash for the various string classes allow users to obtain hashes of strings. 
These hashes equal the hashes of corresponding std::basic_string_view classes: If S is one of these string types, SV is the corresponding string view type, and s is an object of type S, then std::hash&lt;S&gt;()(s) == std::hash&lt;SV&gt;()(SV(s)). <i>(since C++17)</i> 

<h2>Example</h2>

The following code shows one possible output of a hash function used on a string: 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;functional&gt;
int main()

{
    std::string s = &quot;Stand back! I've got jimmies!&quot;;
    std::hash&lt;std::string&gt; hash_fn;
    size_t hash = hash_fn(s);
    std::cout &lt;&lt; hash &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;325378910

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
