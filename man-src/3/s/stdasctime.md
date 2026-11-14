---
title: "stdasctime(3)"
name: "stdasctime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdasctime/"
---

std::asctime - std::asctime

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;ctime&gt;

    char *asctime(const std::tm *time_ptr);</code></pre> 
Converts given calendar time std::tm to a textual representation of the following fixed 25-character form: Www Mmm dd hh:mm:ss yyyy\n 
* Www - three-letter English abbreviated day of the week from time_ptr-&gt;tm_wday, one of Mon, Tue, Wed, Thu, Fri, Sat, Sun. 
* Mmm - three-letter English abbreviated month name from time_ptr-&gt;tm_mon, one of Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec. 
* dd - 2-digit day of the month from timeptr-&gt;tm_mday as if printed by sprintf using %2d 
* hh - 2-digit hour from timeptr-&gt;tm_hour as if printed by sprintf using %.2d 
* mm - 2-digit minute from timeptr-&gt;tm_min as if printed by sprintf using %.2d 
* ss - 2-digit second from timeptr-&gt;tm_sec as if printed by sprintf using %.2d 
* yyyy - 4-digit year from timeptr-&gt;tm_year + 1900 as if printed by sprintf using %4d 
The behavior is undefined if any member of *time_ptr is outside its normal range 
The behavior is undefined if the calendar year indicated by time_ptr-&gt;tm_year has more than 4 digits or is less than the year 1000. 
The function does not support localization, and the newline character cannot be removed. 
The function modifies static storage and is not thread-safe. 

<h2>Parameters</h2>

time_ptr - pointer to a std::tm object specifying the time to print

<h2>Return value</h2>

Pointer to a static null-terminated character string holding the textual representation of date and time. The string may be shared between std::asctime and std::ctime, and may be overwritten on each invocation of any of those functions. 

<h2>Notes</h2>

This function returns a pointer to static data and is not thread-safe. POSIX marks this function obsolete and recommends std::strftime instead. 
POSIX limits undefined behaviors only to when the output string would be longer than 25 characters, when timeptr-&gt;tm_wday or timeptr-&gt;tm_mon are not within the expected ranges, or when timeptr-&gt;tm_year exceeds INT_MAX-1990. 
Some implementations handle timeptr-&gt;tm_mday==0 as meaning the last day of the preceding month. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;ctime&gt;

#include &lt;iostream&gt;
int main()

{
    std::time_t result = std::time(nullptr);
    std::cout &lt;&lt; std::asctime(std::localtime(&amp;result));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Mon Apr 3 20:26:26 2017

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a time_t object to a textual representation 
ctime <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a tm object to custom textual representation 
strftime <i>(function)</i> 
put_time formats and outputs a date/time value according to the specified format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
