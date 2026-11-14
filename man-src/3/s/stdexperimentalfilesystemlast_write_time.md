---
title: "stdexperimentalfilesystemlast_write_time(3)"
name: "stdexperimentalfilesystemlast_write_time"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemlast_write_time/"
description: "std::experimental::filesystem::last_write_time – std::experimental::filesystem::last_write_time"
---

<p>std::experimental::filesystem::last_write_time &#8211; std::experimental::filesystem::last_write_time</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    file_time_type last_write_time(const path &amp;p);
(1)(filesystem TS)

    file_time_type last_write_time(const path &amp;p, error_code &amp;ec)

        void last_write_time(const path &amp;p, file_time_type new_time);
(2)(filesystem TS)

    void last_write_time(const path &amp;p, file_time_type new_time, error_code &amp;ec);</code></pre>
<p>1) Returns the time of the last modification of p, determined as if by accessing the member st_mtime of the POSIX stat (symlinks are followed) The non-throwing overload returns file_time_type::min() on errors.<br />
2) Changes the time of the last modification of p, as if by POSIX futimens (symlinks are followed) </p>
<h2>Parameters</h2>
<p>p &#8211; path to examine or modify<br />
new_time &#8211; new modification time<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>1) The time of the last modification of p<br />
2) <i>(none)</i> </p>
<h2>Exceptions</h2>
<p>The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>It is not guaranteed that immediately after setting the write time, the value returned by <code>(1)</code> is the same as what was passed as the argument to <code>(2)</code> because the file system&#8217;s time may be more granular than file_time_type. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;iomanip&gt;

#include &lt;fstream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

using namespace std::chrono_literals;

int main()

{
    fs::path p = fs::current_path() / &quot;example.bin&quot;;
    std::ofstream(p.c_str()).put('a'); // create file
    auto ftime = fs::last_write_time(p);
    std::time_t cftime = decltype(ftime)::clock::to_time_t(ftime); // assuming system_clock
    std::cout &lt;&lt; &quot;File write time is &quot; &lt;&lt; std::asctime(std::localtime(&amp;cftime)) &lt;&lt; '
';
    fs::last_write_time(p, ftime + 1h); // move file write time 1 hour to the future
    ftime = fs::last_write_time(p);     // read back from the filesystem
    cftime = decltype(ftime)::clock::to_time_t(ftime);
    std::cout &lt;&lt; &quot;File write time is &quot; &lt;&lt; std::asctime(std::localtime(&amp;cftime)) &lt;&lt; '
';
    fs::remove(p);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;File write time is Tue Mar 31 19:47:04 2015 </p>
<p>&nbsp;<wbr>&nbsp;File write time is Tue Mar 31 20:47:04 2015</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents file time values<br />
file_time_type <i>(typedef)</i> </p>
