---
title: "stdctime(3)"
name: "stdctime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctime/"
---

std::ctime - std::ctime

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;ctime&gt;

    char *ctime(const std::time_t *time);</code></pre> 
Converts given time since epoch to a calendar local time and then to a textual representation, as if by calling std::asctime(std::localtime(time)). The resulting string has the following format: 
&nbsp;<wbr>&nbsp;Www Mmm dd hh:mm:ss yyyy 
* Www - the day of the week (one of Mon, Tue, Wed, Thu, Fri, Sat, Sun). 
* Mmm - the month (one of Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec). 
* dd - the day of the month 
* hh - hours 
* mm - minutes 
* ss - seconds 
* yyyy - years 
The function does not support localization. 

<h2>Parameters</h2>

time - pointer to a std::time_t object specifying the time to print

<h2>Return value</h2>

Pointer to a static null-terminated character string holding the textual representation of date and time. The string may be shared between std::asctime and std::ctime, and may be overwritten on each invocation of any of those functions. 

<h2>Notes</h2>

This function returns a pointer to static data and is not thread-safe. In addition, it modifies the static std::tm object which may be shared with std::gmtime and std::localtime. POSIX marks this function obsolete and recommends std::strftime instead. 
The behavior may be undefined for the values of time_t that result in the string longer than 25 characters (e.g. year 10000) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;ctime&gt;

#include &lt;iostream&gt;
int main()

{
    std::time_t result = std::time(nullptr);
    std::cout &lt;&lt; std::ctime(&amp;result);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Tue Dec 27 17:21:29 2011

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a tm object to a textual representation 
asctime <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a tm object to custom textual representation 
strftime <i>(function)</i> 
put_time formats and outputs a date/time value according to the specified format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
