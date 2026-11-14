---
title: "stdgmtime(3)"
name: "stdgmtime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgmtime/"
---

std::gmtime - std::gmtime

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;ctime&gt;

    std::tm *gmtime(const std::time_t *time);</code></pre> 
Converts given time since epoch as std::time_t value into calendar time, expressed in Coordinated Universal Time (UTC). 

<h2>Parameters</h2>

time - pointer to a time_t object to convert

<h2>Return value</h2>

Pointer to a static internal std::tm object on success, or null pointer otherwise. The structure may be shared between std::gmtime, std::localtime, and std::ctime and may be overwritten on each invocation. 

<h2>Notes</h2>

This function may not be thread-safe. 
POSIX requires that this function sets errno to EOVERFLOW if it fails because the argument is too large. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;ctime&gt;
int main()

{
    std::time_t t = std::time(nullptr);
    std::cout &lt;&lt; &quot;UTC:   &quot; &lt;&lt; std::put_time(std::gmtime(&amp;t), &quot;%c %Z&quot;) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;local: &quot; &lt;&lt; std::put_time(std::localtime(&amp;t), &quot;%c %Z&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;UTC: Wed Dec 28 11:44:28 2011 GMT 
&nbsp;<wbr>&nbsp;local: Wed Dec 28 06:44:28 2011 EST

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as local time 
localtime <i>(function)</i> 
