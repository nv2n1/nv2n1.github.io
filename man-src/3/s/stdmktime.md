---
title: "stdmktime(3)"
name: "stdmktime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmktime/"
---

std::mktime - std::mktime

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ctime&gt;

std::time_t mktime( std::tm* time );</code></pre> 
Converts local calendar time to a time since epoch as a time_t object. time-&gt;tm_wday and time-&gt;tm_yday are ignored. The values in time are permitted to be outside their normal ranges. 
A negative value of time-&gt;tm_isdst causes mktime to attempt to determine if Daylight Saving Time was in effect. 
If the conversion is successful, the time object is modified. All fields of time are updated to fit their proper ranges. time-&gt;tm_wday and time-&gt;tm_yday are recalculated using information available in other fields. 

<h2>Parameters</h2>

time - pointer to a std::tm object specifying local calendar time to convert

<h2>Return value</h2>

Time since epoch as a std::time_t object on success or -1 if time cannot be represented as a std::time_t object. 

<h2>Notes</h2>

If the std::tm object was obtained from std::get_time or the POSIX strptime, the value of tm_isdst is indeterminate, and needs to be set explicitly before calling mktime. 

<h2>Example</h2>

Display the time 100 months ago. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;ctime&gt;

#include &lt;stdlib.h&gt;
int main()

{
    setenv(&quot;TZ&quot;, &quot;/usr/share/zoneinfo/America/New_York&quot;, 1); // POSIX-specific
    std::time_t t = std::time(nullptr);
    std::tm tm = *std::localtime(&amp;t);
    std::cout &lt;&lt; &quot;Today is           &quot; &lt;&lt; std::put_time(&amp;tm, &quot;%c %Z&quot;)
              &lt;&lt; &quot; and DST is &quot; &lt;&lt; (tm.tm_isdst ? &quot;in effect&quot; : &quot;not in effect&quot;) &lt;&lt; '\n';
    tm.tm_mon -= 100; // tm_mon is now outside its normal range
    std::mktime(&amp;tm); // tm_dst is not set to -1; today's DST status is used
    std::cout &lt;&lt; &quot;100 months ago was &quot; &lt;&lt; std::put_time(&amp;tm, &quot;%c %Z&quot;)
              &lt;&lt; &quot; and DST was &quot; &lt;&lt; (tm.tm_isdst ? &quot;in effect&quot; : &quot;not in effect&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Today is Fri Apr 22 11:40:36 2016 EDT and DST is in effect 
&nbsp;<wbr>&nbsp;100 months ago was Sat Dec 22 10:40:36 2007 EST and DST was not in effect

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as local time 
localtime <i>(function)</i> 
