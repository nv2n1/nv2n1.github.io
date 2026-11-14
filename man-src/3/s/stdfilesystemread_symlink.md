---
title: "stdfilesystemread_symlink(3)"
name: "stdfilesystemread_symlink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemread_symlink/"
---

std::filesystem::read_symlink - std::filesystem::read_symlink

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    std::filesystem::path read_symlink(const std::filesystem::path &amp;p);

std::filesystem::path read_symlink(const std::filesystem::path &amp;p, (since C++ 17)

                                                                       std::error_code &amp;ec);</code></pre> 
If the path p refers to a symbolic link, returns a new path object which refers to the target of that symbolic link. 
It is an error if p does not refer to a symbolic link. 
The non-throwing overload returns an empty path on errors. 

<h2>Parameters</h2>

p - path to a symlink 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The target of the symlink (which may not necessarily exist) 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;
namespace fs = std::filesystem;
int main()

{
    // on a typical Linux system, /lib/libc.so.6 is a symlink
    fs::path p = &quot;/lib/libc.so.6&quot;;
    if (fs::exists(p) &amp;&amp; fs::is_symlink(p))
        std::cout &lt;&lt; p &lt;&lt; &quot; -&gt; &quot; &lt;&lt; fs::read_symlink(p) &lt;&lt; '\n';
    else
        std::cout &lt;&lt; p &lt;&lt; &quot; does not exist or is not a symlink\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;/lib/libc.so.6&quot; -&gt; &quot;libc-2.12.so&quot;

<h2>See also</h2>

is_symlink checks whether the argument refers to a symbolic link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
create_symlink 
create_directory_symlink creates a symbolic link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
copy_symlink copies a symbolic link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
