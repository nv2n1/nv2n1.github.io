---
title: "stdfilesystemfile_time_type(3)"
name: "stdfilesystemfile_time_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemfile_time_type/"
---

std::filesystem::file_time_type - std::filesystem::file_time_type

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;filesystem&gt;

using file_time_type = std::chrono::time_point&lt;/*trivial-clock*/&gt;;        (since C++17)
(until C++20)

using file_time_type = std::chrono::time_point&lt;std::chrono::file_clock&gt;;  (since C++20)</code></pre> 
Represents file time. 
trivial-clock is an implementation-defined type that satisfies TrivialClock and is sufficient to represent the resolution and range of the file time values offered by the filesystem. <i>(until C++20)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;iomanip&gt;

#include &lt;fstream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

using namespace std::chrono_literals;

int main()

{
    fs::path p = fs::current_path() / &quot;example.bin&quot;;
    std::ofstream(p.c_str()).put('a'); // create file
    auto ftime = fs::last_write_time(p);
    // assuming system_clock for this demo
    // note: not true on MSVC or GCC 9; C++20 will allow portable output
    std::time_t cftime = decltype(ftime)::clock::to_time_t(ftime);
    std::cout &lt;&lt; &quot;File write time is &quot; &lt;&lt; std::asctime(std::localtime(&amp;cftime)) &lt;&lt; '\n';
    fs::last_write_time(p, ftime + 1h); // move file write time 1 hour to the future
    ftime = fs::last_write_time(p);     // read back from the filesystem
    cftime = decltype(ftime)::clock::to_time_t(ftime);
    std::cout &lt;&lt; &quot;File write time is &quot; &lt;&lt; std::asctime(std::localtime(&amp;cftime)) &lt;&lt; '\n';
    fs::remove(p);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;File write time is Tue Mar 31 19:47:04 2015 

 
&nbsp;<wbr>&nbsp;File write time is Tue Mar 31 20:47:04 2015

<h2>See also</h2>

last_write_time gets or sets the time of the last data modification 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
