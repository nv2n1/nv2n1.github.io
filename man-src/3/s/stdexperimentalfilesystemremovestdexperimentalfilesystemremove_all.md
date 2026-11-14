---
title: "stdexperimentalfilesystemremovestdexperimentalfilesystemremove_all(3)"
name: "stdexperimentalfilesystemremovestdexperimentalfilesystemremove_all"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemremovestdexperimentalfilesystemremove_all/"
---

std::experimental::filesystem::remove,std::experimental::filesystem::remove_all - std::experimental::filesystem::remove,std::experimental::filesystem::remove_all

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    bool remove(const path &amp;p);
(1)(filesystem TS)

    bool remove(const path &amp;p, error_code &amp;ec);

std::uintmax_t remove_all(const path &amp;p);
(2)(filesystem TS)

    std::uintmax_t remove_all(const path &amp;p, error_code &amp;ec);</code></pre> 
1) The file or empty directory identified by the path p is deleted as if by the POSIX remove. Symlinks are not followed (symlink is removed, not its target) 
2) Deletes the contents of p (if it is a directory) and the contents of all its subdirectories, recursively, then deletes p itself as if by repeatedly applying the POSIX remove. Symlinks are not followed (symlink is removed, not its target) 

<h2>Parameters</h2>

p - path to delete 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

1) true if the file was deleted, false if it did not exist. The overload that takes error_code&amp; argument returns false on errors. 
2) Returns the number of files and directories that were deleted (which may be zero if p did not exist to begin with). The overload that takes error_code&amp; argument returns static_cast&lt;std::uintmax_t&gt;(-1) on error. 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Notes</h2>

On POSIX systems, this function typically calls unlink and rmdir as needed, on Windows RemoveDirectoryW and DeleteFileW. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdint&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    fs::path dir = fs::temp_directory_path();
    fs::create_directories(dir / &quot;abcdef/example&quot;);
    std::uintmax_t n = fs::remove_all(dir / &quot;abcdef&quot;);
    std::cout &lt;&lt; &quot;Deleted &quot; &lt;&lt; n &lt;&lt; &quot; files or directories\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Deleted 2 files or directories

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erases a file 
remove <i>(function)</i> 
