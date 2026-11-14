---
title: "stdtimespec_get(3)"
name: "stdtimespec_get"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtimespec_get/"
---

std::timespec_get - std::timespec_get

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ctime&gt;

int timespec_get( std::timespec* ts, int base)  (since C++17)

#define TIME_UTC /* implementation-defined */   (since C++17)</code></pre> 
1) Modifies the std::timespec object pointed to by ts to hold the current calendar time in the time base base. 
2) Expands to a value suitable for use as the base argument of std::timespec_get 
Other macro constants beginning with TIME_ may be provided by the implementation to indicate additional time bases 
If base is TIME_UTC, then 
* ts-&gt;tv_sec is set to the number of seconds since an implementation defined epoch, truncated to a whole value 
* ts-&gt;tv_nsec member is set to the integral number of nanoseconds, rounded to the resolution of the system clock 

<h2>Parameters</h2>

ts - pointer to an object of type std::timespec 
base - TIME_UTC or another nonzero integer value indicating the time base

<h2>Return value</h2>

The value of base if successful, zero otherwise. 

<h2>Notes</h2>

The POSIX function clock_gettime(CLOCK_REALTIME,_ts) may also be used to populate a std::timespec with the time since the Epoch. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;ctime&gt;
int main()

{
    std::timespec ts;
    std::timespec_get(&amp;ts, TIME_UTC);
    char buf[100];
    std::strftime(buf, sizeof buf, &quot;%D %T&quot;, std::gmtime(&amp;ts.tv_sec));
    std::printf(&quot;Current time: %s.%09ld UTC\n&quot;, buf, ts.tv_nsec);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Current time: 06/24/16 20:07:42.949494132 UTC

<h2>See also</h2>

timespec time in seconds and nanoseconds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(struct) 
<i>(since C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the current time of the system as time since epoch 
time <i>(function)</i> 
