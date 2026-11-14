---
title: "stdlocaltime(3)"
name: "stdlocaltime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaltime/"
---

std::localtime - std::localtime

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;ctime&gt;

    std::tm *localtime(const std::time_t *time);</code></pre> 
Converts given time since epoch as std::time_t value into calendar time, expressed in local time. 

<h2>Parameters</h2>

time - pointer to a time_t object to convert

<h2>Return value</h2>

pointer to a static internal std::tm object on success, or null pointer otherwise. The structure may be shared between std::gmtime, std::localtime, and std::ctime, and may be overwritten on each invocation. 

<h2>Notes</h2>

This function may not be thread-safe. 
POSIX requires that this function sets errno to EOVERFLOW if it fails because the argument is too large. 
POSIX_specifies that the timezone information is determined by this function as if by calling tzset, which reads the environment variable TZ. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;ctime&gt;

#include &lt;stdlib.h&gt; // defines putenv in POSIX
int main()

{
    std::time_t t = std::time(nullptr);
    std::cout &lt;&lt; &quot;UTC:       &quot; &lt;&lt; std::put_time(std::gmtime(&amp;t), &quot;%c %Z&quot;) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;local:     &quot; &lt;&lt; std::put_time(std::localtime(&amp;t), &quot;%c %Z&quot;) &lt;&lt; '\n';
    // POSIX-specific:
    std::string tz = &quot;TZ=Asia/Singapore&quot;;
    putenv(tz.data());
    std::cout &lt;&lt; &quot;Singapore: &quot; &lt;&lt; std::put_time(std::localtime(&amp;t), &quot;%c %Z&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;UTC: Fri Sep 15 14:16:29 2017 GMT 
&nbsp;<wbr>&nbsp;local: Fri Sep 15 14:16:29 2017 UTC 
&nbsp;<wbr>&nbsp;Singapore: Fri Sep 15 22:16:29 2017 SGT

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as Universal Coordinated Time 
gmtime <i>(function)</i> 
