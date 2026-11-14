---
title: "stdexception_ptr(3)"
name: "stdexception_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexception_ptr/"
---

std::exception_ptr - std::exception_ptr

<h2>Synopsis</h2>

Defined in header &lt;exception&gt; 
typedef /*unspecified*/ exception_ptr; <i>(since C++11)</i> 
std::exception_ptr is a nullable pointer-like type that manages an exception object which has been thrown and captured with std::current_exception. An instance of std::exception_ptr may be passed to another function, possibly on another thread, where the exception may be rethrown and handled with a catch clause. 
A default-constructed std::exception_ptr is a null pointer; it does not point to an exception object. 
Two instances of std::exception_ptr compare equal only if they are both null or both point at the same exception object. 
std::exception_ptr is not implicitly convertible to any arithmetic, enumeration, or pointer type. It is contextually convertible to bool, and will evaluate to false if it is null, true otherwise. 
The exception object referenced by an std::exception_ptr remains valid as long as there remains at least one std::exception_ptr that is referencing it: std::exception_ptr is a shared-ownership smart pointer (note; this is in addition to the usual exception_object_lifetime_rules) 
std::exception_ptr meets the requirements of NullablePointer. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;exception&gt;

#include &lt;stdexcept&gt;
void handle_eptr(std::exception_ptr eptr) // passing by value is ok

{
    try {
        if (eptr) {
            std::rethrow_exception(eptr);
        }
    } catch (const std::exception &amp;e) {
        std::cout &lt;&lt; &quot;Caught exception \&quot;&quot; &lt;&lt; e.what() &lt;&lt; &quot;\&quot;\n&quot;;
    }
}
int main()

{
    std::exception_ptr eptr;
    try {
        std::string().at(1); // this generates an std::out_of_range
    } catch (...) {
        eptr = std::current_exception(); // capture
    }
    handle_eptr(eptr);

} // destructor for std::out_of_range called here, when the eptr is destructed
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Caught exception &quot;basic_string::at&quot;

<h2>See also</h2>

make_exception_ptr creates an std::exception_ptr from an exception object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
current_exception captures the current exception in a std::exception_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
rethrow_exception throws the exception from an std::exception_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
