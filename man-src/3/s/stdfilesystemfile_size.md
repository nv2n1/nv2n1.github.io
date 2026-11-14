---
title: "stdfilesystemfile_size(3)"
name: "stdfilesystemfile_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemfile_size/"
---

std::filesystem::file_size - std::filesystem::file_size

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    std::uintmax_t file_size(const std::filesystem::path &amp;p);

std::uintmax_t file_size(const std::filesystem::path &amp;p, (1)(since C++ 17)

                                                             std::error_code &amp;ec) noexcept;</code></pre> 
If p does not exist, reports an error. 
For a regular file p, returns the size determined as if by reading the st_size member of the structure obtained by POSIX stat (symlinks are followed) 
The result of attempting to determine the size of a directory (as well as any other file that is not a regular file or a symlink) is implementation-defined. 
The non-throwing overload returns -1 on errors. 

<h2>Parameters</h2>

p - path to examine 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The size of the file, in bytes. 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::path p = fs::current_path() / &quot;example.bin&quot;;
    std::ofstream(p).put('a'); // create file of size 1
    std::cout &lt;&lt; &quot;File size = &quot; &lt;&lt; fs::file_size(p) &lt;&lt; '\n';
    fs::remove(p);
    try {
        fs::file_size(&quot;/dev&quot;); // attempt to get size of a directory
    } catch (fs::filesystem_error &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;File size = 1 
&nbsp;<wbr>&nbsp;filesystem error: cannot get file size: Is a directory [/dev]

<h2>See also</h2>

resize_file changes the size of a regular file by truncation or zero-fill 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
space determines available free space on the file system 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the size of the file to which the directory entry refers 
file_size <i>(public member function of std::filesystem::directory_entry)</i> 
