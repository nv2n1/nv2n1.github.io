---
title: "stdfilesystemspace(3)"
name: "stdfilesystemspace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemspace/"
---

std::filesystem::space - std::filesystem::space

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    std::filesystem::space_info space(const std::filesystem::path &amp;p);

std::filesystem::space_info space(const std::filesystem::path &amp;p, (since C++ 17)

                                                                      std::error_code &amp;ec) noexcept;</code></pre> 
Determines the information about the filesystem on which the pathname p is located, as if by POSIX statvfs 
Populates and returns an object of type space_info, set from the members of the POSIX struct statvfs as follows 
* space_info.capacity is set as if by f_blocks*f_frsize 
* space_info.free is set to f_bfree*f_frsize 
* space_info.available is set to f_bavail*f_frsize 
* Any member that could not be determined is set to static_cast&lt;uintmax_t&gt;(-1) 
The non-throwing overload sets all members to static_cast&lt;uintmax_t&gt;(-1) on error. 

<h2>Parameters</h2>

p - path to examine 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The filesystem information (a space_info object) 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

space_info.available may be less than space_info.free 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::space_info devi = fs::space(&quot;/dev/null&quot;);
    fs::space_info tmpi = fs::space(&quot;/tmp&quot;);
    std::cout &lt;&lt; &quot;.        Capacity       Free      Available\n&quot;
              &lt;&lt; &quot;/dev:   &quot; &lt;&lt; devi.capacity &lt;&lt; &quot;   &quot;
              &lt;&lt; devi.free &lt;&lt; &quot;   &quot; &lt;&lt; devi.available &lt;&lt; '\n'
              &lt;&lt; &quot;/tmp: &quot; &lt;&lt; tmpi.capacity &lt;&lt; &quot; &quot;
              &lt;&lt; tmpi.free &lt;&lt; &quot; &quot; &lt;&lt; tmpi.available &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;. Capacity Free Available 
&nbsp;<wbr>&nbsp;/dev: 4175114240 4175110144 4175110144 
&nbsp;<wbr>&nbsp;/tmp: 420651237376 411962273792 390570749952

<h2>See also</h2>

space_info information about free and available space on the filesystem 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
