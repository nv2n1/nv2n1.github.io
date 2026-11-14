---
title: "stdtype_infoname(3)"
name: "stdtype_infoname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_infoname/"
---

std::type_info::name - std::type_info::name

<h2>Synopsis</h2>

<pre><code>const char *name() const;</code></pre> 
Returns an implementation defined null-terminated character string containing the name of the type. No guarantees are given; in particular, the returned string can be identical for several types and change between invocations of the same program. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

null-terminated character string containing the name of the type. 

<h2>Notes</h2>

The lifetime of the array pointed to by the returned pointer is not specified, but in practice it persist as long as the RTTI data structure for the given type exists, which has application lifetime unless loaded from a dynamic library (that can be unloaded). 
Some implementations (such as MSVC, IBM, Oracle) produce a human-readable type name. Others, most notably gcc and clang, return the mangled name. The mangled name can be converted to human-readable form using implementation-specific API such as abi::__cxa_demangle directly or through boost::core::demangle. It can also be piped through the commandline utility c++filt -t. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;typeinfo&gt;
struct Base {
    virtual ~Base() = default;
};

struct Derived : Base {
};
int main()
{

    Base b1;

    Derived d1;
    const Base *pb = &amp;b1;

    std::cout &lt;&lt; typeid(*pb).name() &lt;&lt; '\n';

    pb = &amp;d1;

    std::cout &lt;&lt; typeid(*pb).name() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;4Base 
&nbsp;<wbr>&nbsp;7Derived

<h2>See also</h2>

hash_code returns a value which is identical for the same types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
