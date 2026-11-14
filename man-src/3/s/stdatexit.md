---
title: "stdatexit(3)"
name: "stdatexit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatexit/"
---

std::atexit - std::atexit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    int atexit(/*c-atexit-handler*/ *func);
(until C++ 11)

    int atexit(/*atexit-handler*/ *func);

int atexit(/*c-atexit-handler*/ *func) noexcept;
(1)(since C++ 11)

    int atexit(/*atexit-handler*/ *func) noexcept;

extern &quot;C++&quot; using /*atexit-handler*/ = void(); // exposition-only     (2)

extern &quot;C&quot; using /*c-atexit-handler*/ = void(); // exposition-only</code></pre> 
Registers the function pointed to by func to be called on normal program termination (via std::exit() or returning from the main_function) 
The functions will be called during the destruction of the static objects, in reverse order: if A was registered before B, then the call to B is made before the call to A. Same applies to the ordering between static object constructors and the calls to atexit: see std::exit <i>(until C++11)</i> 
The functions may be called concurrently with the destruction of the objects with static storage duration and with each other, maintaining the guarantee that if registration of A was sequenced-before the registration of B, then the call to B is sequenced-before the call to A, same applies to the sequencing between static object constructors and calls to atexit: see std::exit <i>(since C++11)</i> 
The same function may be registered more than once. 
If a function exits via an exception, std::terminate is called. 
atexit is thread-safe: calling the function from several threads does not induce a data race. 
The implementation is guaranteed to support the registration of at least 32 functions. The exact limit is implementation-defined. 

<h2>Parameters</h2>

func - pointer to a function to be called on normal program termination

<h2>Return value</h2>

0 if the registration succeeds, nonzero value otherwise. 

<h2>Notes</h2>

The two overloads are distinct because the types of the parameter func are distinct (language_linkage is part of its type) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
void atexit_handler_1()

{
    std::cout &lt;&lt; &quot;at exit #1\n&quot;;
}
void atexit_handler_2()

{
    std::cout &lt;&lt; &quot;at exit #2\n&quot;;
}
int main()

{
    const int result_1 = std::atexit(atexit_handler_1);
    const int result_2 = std::atexit(atexit_handler_2);
    if ((result_1 != 0) or (result_2 != 0)) {
        std::cerr &lt;&lt; &quot;Registration failed\n&quot;;
        return EXIT_FAILURE;
    }
    std::cout &lt;&lt; &quot;returning from main\n&quot;;
    return EXIT_SUCCESS;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;returning from main 
&nbsp;<wbr>&nbsp;at exit #2 
&nbsp;<wbr>&nbsp;at exit #1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes abnormal program termination (without cleaning up) 
abort <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes normal program termination with cleaning up 
exit <i>(function)</i> 
quick_exit causes quick program termination without completely cleaning up 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
at_quick_exit registers a function to be called on quick_exit invocation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
