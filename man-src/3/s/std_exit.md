---
title: "std_exit(3)"
name: "std_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_exit/"
---

std::_Exit - std::_Exit

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
[[noreturn]] void _Exit( int exit_code ) noexcept; <i>(since C++11)</i> 
Causes normal program termination to occur without completely cleaning the resources. 
Destructors of variables with automatic, thread local and static storage durations are not called. Functions passed to std::at_quick_exit() or std::atexit() are not called. Whether open resources such as files are closed is implementation defined. 
If exit_code is 0 or EXIT_SUCCESS, an implementation-defined status indicating successful termination is returned to the host environment. If exit_code is EXIT_FAILURE, an implementation-defined status, indicating unsuccessful termination, is returned. In other cases implementation-defined status value is returned. 

<h2>Parameters</h2>

exit_code - exit status of the program

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;
class Static {

    public:
    ~Static()
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

};</code></pre> 
&nbsp;<wbr>&nbsp;Static static_variable; // dtor of this object will *not* be called <pre><code>void atexit_handler()

{
    std::cout &lt;&lt; &quot;atexit handler\n&quot;;
}
int main()

{
    Local local_variable; // dtor of this object will *not* be called
                          // handler will *not* be called
    const int result = std::atexit(atexit_handler);
    if (result != 0) {
        std::cerr &lt;&lt; &quot;atexit registration failed\n&quot;;
        return EXIT_FAILURE;
    }
    std::cout &lt;&lt; &quot;test&quot; &lt;&lt; std::endl; // flush from std::endl
                                      // needs to be here, otherwise nothing will be printed
    std::_Exit(EXIT_FAILURE);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;test

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes abnormal program termination (without cleaning up) 
abort <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes normal program termination with cleaning up 
exit <i>(function)</i> 
