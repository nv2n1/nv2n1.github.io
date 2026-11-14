---
title: "stdterminate_handler(3)"
name: "stdterminate_handler"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdterminate_handler/"
---

std::terminate_handler - std::terminate_handler

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;exception&gt;

    typedef void (*terminate_handler)();</code></pre> 
std::terminate_handler is the function pointer type (pointer to function that takes no arguments and returns void), which is installed and queried by the functions std::set_terminate and std::get_terminate and called by std::terminate. 
The C++ implementation provides a default std::terminate_handler function, which calls std::abort(). If the null pointer value is installed (by means of std::set_terminate), the implementation may restore the default handler instead. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function called when exception handling fails 
terminate <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the function to be called by std::terminate 
set_terminate <i>(function)</i> 
get_terminate obtains the current terminate_handler 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
