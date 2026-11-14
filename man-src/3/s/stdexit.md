---
title: "stdexit(3)"
name: "stdexit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexit/"
---

std::exit - std::exit

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
void exit( int exit_code ); <i>(until C++11)</i> 
[[noreturn]] void exit( int exit_code ); <i>(since C++11)</i> 
Causes normal program termination to occur. 
Several cleanup steps are performed: 
1) destructors of objects with static storage duration are called in reverse order of completion of their constructors or the completion of their dynamic_initialization, and the functions passed to std::atexit are called in reverse order they are registered (last one first). 
a) any static objects whose initialization was completed before the call to std::atexit for some function F will be destroyed after the call to F during program termination. <i>(until C++11)</i> 
b) any static objects whose construction began after the call to std::atexit for some function F will be destroyed before the call to F during program termination (this includes the case where std::atexit was called from the constructor of the static object) 
1) The destructors of objects with thread local storage_duration that are associated with the current thread, the destructors of objects with static storage duration, and the functions registered with std::atexit are executed concurrently, while maintaining the following guarantees: 
a) The last destructor for thread-local objects is sequenced-before the first destructor for a static object 
b) If the completion of the constructor or dynamic_initialization for thread-local or static object A was sequenced-before thread-local or static object B, the completion of the destruction of B is sequenced-before the start of the destruction of A <i>(since C++11)</i> 
c) If the completion of the initialization of a static object A was sequenced-before the call to std::atexit for some function F, the call to F during termination is sequenced-before the start of the destruction of A 
d) If the call to std::atexit for some function F was sequenced-before the completion of initialization of a static object A, the start of the destruction of A is sequenced-before the call to F during termination. 
e) If a call to std::atexit for some function F1 was sequenced-before the call to std::atexit for some function F2, then the call to F2 during termination is sequenced-before the call to F1 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* In the above, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if any function registered with atexit or any destructor of static/thread-local object throws an exception, std::terminate is called 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if the compiler opted to lift dynamic initialization of an object to the static initialization phase of non-local_initialization, the sequencing of destruction honors its would-be dynamic initialization. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If a function-local (block-scope) static object was destroyed and then that function is called from the destructor of another static object and the control flow passes through the definition of that object (or if it is used indirectly, via pointer or reference), the behavior is undefined. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if a function-local (block-scope) static object was initialized during construction of a subobject of a class or array, it is only destroyed after all subobjects of that class or all elements of that array were destroyed. 
2) all C streams are flushed and closed 
3) files created by std::tmpfile are removed 
4) control is returned to the host environment. If exit_code is 0 or EXIT_SUCCESS, an implementation-defined status indicating successful termination is returned. If exit_code is EXIT_FAILURE, an implementation-defined status indicating unsuccessful termination is returned. In other cases implementation-defined status value is returned. 
Stack is not unwound: destructors of variables with automatic storage_duration are not called. 

<h2>Relationship with the main function</h2>

Returning from the main_function, either by a return statement or by reaching the end of the function performs the normal function termination (calls the destructors of the variables with automatic storage_durations) and then executes std::exit, passing the argument of the return statement (or 0 if implicit return was used) as exit_code.

<h2>Parameters</h2>

exit_code - exit status of the program

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>void atexit_handler()

{
    std::cout &lt;&lt; &quot;atexit handler\n&quot;;
}
int main()

{
    Local local_variable;                           // dtor of this object will *not* be called
    const int result = std::atexit(atexit_handler); // handler will be called
    if (result != 0) {
        std::cerr &lt;&lt; &quot;atexit registration failed\n&quot;;
        return EXIT_FAILURE;
    }
    std::cout &lt;&lt; &quot;test\n&quot;;
    std::exit(EXIT_FAILURE);
}
</code></pre> 
&nbsp;<wbr>&nbsp;class Static { 
&nbsp;<wbr>&nbsp;public: ~Static()
{
    std::cout &lt;&lt; &quot;Static dtor\n&quot;;
}

};
class Local {

    public:
    ~Local()
    {
        std::cout &lt;&lt; &quot;Local dtor\n&quot;;
    }

}; 
&nbsp;<wbr>&nbsp;Static static_variable; // dtor of this object *will* be called <pre><code>void atexit_handler()

{
    std::cout &lt;&lt; &quot;atexit handler\n&quot;;
}
int main()

{
    Local local_variable;                           // dtor of this object will *not* be called
    const int result = std::atexit(atexit_handler); // handler will be called
    if (result != 0) {
        std::cerr &lt;&lt; &quot;atexit registration failed\n&quot;;
        return EXIT_FAILURE;
    }
    std::cout &lt;&lt; &quot;test\n&quot;;
    std::exit(EXIT_FAILURE);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;test 
&nbsp;<wbr>&nbsp;atexit handler 
&nbsp;<wbr>&nbsp;Static dtor

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes abnormal program termination (without cleaning up) 
abort <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;registers a function to be called on std::exit() invocation 
atexit <i>(function)</i> 
quick_exit causes quick program termination without completely cleaning up 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
at_quick_exit registers a function to be called on quick_exit invocation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
