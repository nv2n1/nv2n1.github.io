---
title: "stdtime(3)"
name: "stdtime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime/"
---

std::time - std::time

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ctime&gt;

std::time_t time( std::time_t* arg );</code></pre> 
Returns the current calendar time encoded as a std::time_t object, and also stores it in the object pointed to by arg, unless arg is a null pointer. 

<h2>Parameters</h2>

arg - pointer to a std::time_t object to store the time, or a null pointer

<h2>Return value</h2>

Current calendar time encoded as std::time_t object on success, (std::time_t)(-1) on error. If arg is not null, the return value is also stored in the object pointed to by arg. 

<h2>Notes</h2>

The encoding of calendar time in std::time_t is unspecified, but most systems conform to POSIX_specification and return a value of integral type holding the number of seconds since the_Epoch. Implementations in which std::time_t is a 32-bit signed integer (many historical implementations) fail in the year 2038. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;ctime&gt;

#include &lt;iostream&gt;
int main()

{
    std::time_t result = std::time(nullptr);
    std::cout &lt;&lt; std::asctime(std::localtime(&amp;result))
              &lt;&lt; result &lt;&lt; &quot; seconds since the Epoch\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Wed Sep 21 10:27:52 2011 
&nbsp;<wbr>&nbsp;1316615272 seconds since the Epoch

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as local time 
localtime <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as Universal Coordinated Time 
gmtime <i>(function)</i> 
system_clock wall clock time from the system-wide realtime clock 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
