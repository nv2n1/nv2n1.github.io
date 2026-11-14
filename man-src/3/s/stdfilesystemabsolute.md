---
title: "stdfilesystemabsolute(3)"
name: "stdfilesystemabsolute"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemabsolute/"
---

std::filesystem::absolute - std::filesystem::absolute

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    path absolute(const std::filesystem::path &amp;p);
(since C++ 17)

    path absolute(const std::filesystem::path &amp;p, std::error_code &amp;ec);</code></pre> 
Returns a path referencing the same file system location as p, for which is_absolute() is true. The non-throwing overload returns default-constructed path if an error occurs. 

<h2>Parameters</h2>

p - path to convert to absolute form 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

Returns an absolute (although not necessarily canonical) pathname referencing the same file as p 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

Implementations are encouraged to not consider p not existing to be an error. 
For POSIX-based operating systems, std::filesystem::absolute(p) is equivalent to std::filesystem::current_path() / p 
For Windows, absolute may be implemented as a call to GetFullPathNameW. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::path p = &quot;C:cl.exe&quot;;
    std::cout &lt;&lt; &quot;Current path is &quot; &lt;&lt; fs::current_path() &lt;&lt; '\n'
              &lt;&lt; &quot;Absolute path for &quot; &lt;&lt; p &lt;&lt; &quot; is &quot; &lt;&lt; fs::absolute(p) &lt;&lt; '\n';

    // actual location: &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\cl.exe&quot;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Current path is &quot;D:/local/ConsoleApplication1&quot; 
&nbsp;<wbr>&nbsp;Absolute path for &quot;C:cl.exe&quot; is &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\cl.exe&quot;

<h2>See also</h2>

canonical composes a canonical path 
weakly_canonical <i>(function)</i> 
<i>(C++17)</i> 
relative composes a relative path 
proximate <i>(function)</i> 
<i>(C++17)</i> 
