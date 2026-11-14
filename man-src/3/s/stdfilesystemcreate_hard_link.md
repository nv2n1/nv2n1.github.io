---
title: "stdfilesystemcreate_hard_link(3)"
name: "stdfilesystemcreate_hard_link"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcreate_hard_link/"
---

std::filesystem::create_hard_link - std::filesystem::create_hard_link

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    void create_hard_link(const std::filesystem::path &amp;target,

                          const std::filesystem::path &amp;link);

void create_hard_link(const std::filesystem::path &amp;target, (since C++ 17)

                                                               const std::filesystem::path &amp;link,

                      std::error_code &amp;ec) noexcept;</code></pre> 
Creates a hard link link with its target set to target as if by POSIX link(): the pathname target must exist. 
Once created, link and target are two logical names that refer to the same file (they are equivalent). Even if the original name target is deleted, the file continues to exist and is accessible as link. 

<h2>Parameters</h2>

target - path of the file or directory to link to 
link - path of the new hard link 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with target as the first path argument, link as the second path argument, and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

Some operating systems do not support hard links at all or support them only for regular files. 
Some file systems do not support hard links regardless of the operating system: the FAT file system used on memory cards and flash drives, for example. 
Some file systems limit the number of links per file. 
Hardlinking to directories is typically restricted to the superuser. 
Hard links typically cannot cross filesystem boundaries. 
The special pathname dot (&quot;.&quot;) is a hard link to its parent directory. The special pathname dot-dot &quot;..&quot; is a hard link to the directory that is the parent of its parent. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/subdir&quot;);
    std::ofstream(&quot;sandbox/a&quot;).put('a'); // create regular file
    fs::create_hard_link(&quot;sandbox/a&quot;, &quot;sandbox/b&quot;);
    fs::remove(&quot;sandbox/a&quot;);
    // read from the original file via surviving hard link
    char c = std::ifstream(&quot;sandbox/b&quot;).get();
    std::cout &lt;&lt; c &lt;&lt; '\n';
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;a

<h2>See also</h2>

create_symlink 
create_directory_symlink creates a symbolic link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
hard_link_count returns the number of hard links referring to the specific file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
