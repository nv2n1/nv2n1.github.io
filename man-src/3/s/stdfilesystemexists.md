---
title: "stdfilesystemexists(3)"
name: "stdfilesystemexists"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemexists/"
---

std::filesystem::exists - std::filesystem::exists

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    bool exists(std::filesystem::file_status s) noexcept;
(1)(since C++ 17)

    bool exists(const std::filesystem::path &amp;p);
(2)(since C++ 17)

    bool exists(const std::filesystem::path &amp;p, std::error_code &amp;ec) noexcept;</code></pre> 
Checks if the given file status or path corresponds to an existing file or directory. 
1) Equivalent to status_known(s) &amp;&amp; s.type() != file_type::not_found. 
2) Let s be a std::filesystem::file_status determined as if by status(p) or status(p, ec) (symlinks are followed), respectively. Returns exists(s). The non-throwing overload calls ec.clear() if status_known(s). 

<h2>Parameters</h2>

s - file status to check 
p - path to examine 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

true if the given path or file status corresponds to an existing file or directory, false otherwise. 

<h2>Exceptions</h2>

2) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

The information provided by this function is usually also provided as a byproduct of directory iteration. During directory iteration, calling exists(*iterator) is less efficient than exists(iterator-&gt;status()) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: switch to directory_entry::exists 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdint&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
void demo_exists(const fs::path &amp;p, fs::file_status s = fs::file_status{})

{
    std::cout &lt;&lt; p;
    if (fs::status_known(s) ? fs::exists(s) : fs::exists(p))
        std::cout &lt;&lt; &quot; exists\n&quot;;
    else
        std::cout &lt;&lt; &quot; does not exist\n&quot;;
}

int main()

{
    fs::create_directory(&quot;sandbox&quot;);
    std::ofstream(&quot;sandbox/file&quot;); // create regular file
    fs::create_symlink(&quot;non-existing&quot;, &quot;sandbox/symlink&quot;);
    demo_exists(&quot;sandbox&quot;);
    for (auto it = fs::directory_iterator(&quot;sandbox&quot;); it != fs::directory_iterator(); ++it)
        demo_exists(*it, it-&gt;status()); // use cached status from directory entry
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;sandbox&quot; exists 
&nbsp;<wbr>&nbsp;&quot;sandbox/file&quot; exists 
&nbsp;<wbr>&nbsp;&quot;sandbox/symlink&quot; does not exist

<h2>See also</h2>

status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
file_status represents file type and permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether directory entry refers to existing file system object 
exists <i>(public member function of std::filesystem::directory_entry)</i> 
