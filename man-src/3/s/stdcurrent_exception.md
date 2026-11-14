---
title: "stdcurrent_exception(3)"
name: "stdcurrent_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcurrent_exception/"
---

std::current_exception - std::current_exception

<h2>Synopsis</h2>

Defined in header &lt;exception&gt; 
std::exception_ptr current_exception() noexcept; <i>(since C++11)</i> 
If called during exception handling (typically, in a catch clause), captures the current exception object and creates an std::exception_ptr that holds either a copy or a reference to that exception object (depending on the implementation). The referenced object remains valid at least as long as there is an exception_ptr object that refers to it. 
If the implementation of this function requires a call to new and the call fails, the returned pointer will hold a reference to an instance of std::bad_alloc. 
If the implementation of this function requires copying the captured exception object and its copy constructor throws an exception, the returned pointer will hold a reference to the exception thrown. If the copy constructor of the thrown exception object also throws, the returned pointer may hold a reference to an instance of std::bad_exception to break the endless loop. 
If the function is called when no exception is being handled, an empty std::exception_ptr is returned. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

An instance of std::exception_ptr holding a reference to the exception object, or a copy of the exception object, or to an instance of std::bad_alloc or to an instance of std::bad_exception. 

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

exception_ptr shared pointer type for handling exception objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
rethrow_exception throws the exception from an std::exception_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
make_exception_ptr creates an std::exception_ptr from an exception object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
