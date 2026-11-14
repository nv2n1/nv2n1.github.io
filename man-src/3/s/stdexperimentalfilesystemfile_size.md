---
title: "stdexperimentalfilesystemfile_size(3)"
name: "stdexperimentalfilesystemfile_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemfile_size/"
---

std::experimental::filesystem::file_size - std::experimental::filesystem::file_size

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    std::uintmax_t file_size(const path &amp;p);
(1)(filesystem TS)

    std::uintmax_t file_size(const path &amp;p, error_code &amp;ec);</code></pre> 
Returns the size of the regular file p, determined as if by reading the st_size member of the structure obtained by POSIX stat (symlinks are followed) 
Attempting to determine the size of a directory (as well as any other file that is not a regular file or a symlink) is treated as an error. 
The non-throwing overload returns returns -1 on errors. 

<h2>Parameters</h2>

p - path to examine 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The size of the file, in bytes. 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the size of a regular file by truncation or zero-fill 
resize_file <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines available free space on the file system 
space <i>(function)</i> 
