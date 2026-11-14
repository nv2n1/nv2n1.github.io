---
title: "stdfilesystemhard_link_count(3)"
name: "stdfilesystemhard_link_count"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemhard_link_count/"
---

std::filesystem::hard_link_count - std::filesystem::hard_link_count

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    std::uintmax_t hard_link_count(const std::filesystem::path &amp;p);

std::uintmax_t hard_link_count(const std::filesystem::path &amp;p, (1)(since C++ 17)

                                                                   std::error_code &amp;ec) noexcept;</code></pre> 
Returns the number of hard links for the filesystem object identified by path p. 
The non-throwing overload returns static_cast&lt;uintmax_t&gt;(-1) on errors. 

<h2>Parameters</h2>

p - path to examine 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The number of hard links for p 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    // On a POSIX-style filesystem, each directory has at least 2 hard links:
    // itself and the special member pathname &quot;.&quot;
    fs::path p = fs::current_path();
    std::cout &lt;&lt; &quot;Number of hard links for current path is &quot;
              &lt;&lt; fs::hard_link_count(p) &lt;&lt; '\n';
    // each &quot;..&quot; is a hard link to the parent directory, so the total number
    // of hard links for any directory is 2 plus number of direct subdirectories
    p = fs::current_path() / &quot;..&quot;; // each dot-dot is a hard link to parent
    std::cout &lt;&lt; &quot;Number of hard links for .. is &quot;
              &lt;&lt; fs::hard_link_count(p) &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Number of hard links for current path is 2 
&nbsp;<wbr>&nbsp;Number of hard links for .. is 3

<h2>See also</h2>

create_hard_link creates a hard link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of hard links referring to the file to which the directory entry refers 
hard_link_count <i>(public member function of std::filesystem::directory_entry)</i> 
