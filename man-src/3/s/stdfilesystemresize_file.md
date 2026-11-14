---
title: "stdfilesystemresize_file(3)"
name: "stdfilesystemresize_file"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemresize_file/"
---

std::filesystem::resize_file - std::filesystem::resize_file

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    void resize_file(const std::filesystem::path &amp;p,

                     std::uintmax_t new_size);

void resize_file(const std::filesystem::path &amp;p, (since C++ 17)

                                                     std::uintmax_t new_size,

                 std::error_code &amp;ec) noexcept;</code></pre> 
Changes the size of the regular file named by p as if by POSIX truncate: if the file size was previously larger than new_size, the remainder of the file is discarded. If the file was previously smaller than new_size, the file size is increased and the new area appears as if zero-filled. 

<h2>Parameters</h2>

p - path to resize 
new_size - size that the file will now have 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

On systems that support sparse files, increasing the file size does not increase the space it occupies on the file system: space allocation takes place only when non-zero bytes are written to the file. 

<h2>Example</h2>

demonstrates the effect of creating a sparse file on the free space 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;fstream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::path p = fs::current_path() / &quot;example.bin&quot;;
    std::ofstream(p).put('a');
    std::cout &lt;&lt; &quot;File size: &quot; &lt;&lt; std::setw(10) &lt;&lt; fs::file_size(p)
              &lt;&lt; &quot; Free space: &quot; &lt;&lt; fs::space(p).free &lt;&lt; '\n';
    fs::resize_file(p, 1024 * 1024 * 1024); // resize to 1 G
    std::cout &lt;&lt; &quot;File size: &quot; &lt;&lt; fs::file_size(p)
              &lt;&lt; &quot; Free space: &quot; &lt;&lt; fs::space(p).free &lt;&lt; '\n';
    fs::remove(p);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;File size: 1 Free space: 3724541952 
&nbsp;<wbr>&nbsp;File size: 1073741824 Free space: 3724476416

<h2>See also</h2>

file_size returns the size of a file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
space determines available free space on the file system 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
