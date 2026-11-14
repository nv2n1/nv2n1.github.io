---
title: "stdexperimentalfilesystemrename(3)"
name: "stdexperimentalfilesystemrename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemrename/"
---

std::experimental::filesystem::rename - std::experimental::filesystem::rename

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    void rename(const path &amp;old_p, const path &amp;new_p);
(filesystem TS)

    void rename(const path &amp;old_p, const path &amp;new_p, std::error_code &amp;ec);</code></pre> 
Moves or renames the filesystem object identified by old_p to new_p as if by the POSIX rename: 
* If old_p is a non-directory file, then new_p must be one of: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* the same file as old_p or a hardlink to it: nothing is done in this case 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* existing non-directory file: new_p is first deleted, then, without allowing other processes to observe new_p as deleted, the pathname new_p is linked to the file and old_p is unlinked from the file. Write permissions are required to both the directory that contains old_p and the directory that contains new_p. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* non-existing file in an existing directory: The pathname new_p is linked to the file and old_p is unlinked from the file. Write permissions are required to both the directory that contains old_p and the directory that contains new_p. 
* If old_p is a directory, then new_p must be one of: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* the same directory as old_p or a hardlink to it: nothing is done in this case 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* existing directory: new_p is deleted if empty on POSIX systems, but this may be an error on other systems. If not an error, then new_p is first deleted, then, without allowing other processes to observe new_p as deleted, the pathname new_p is linked to the directory and old_p is unlinked from the directory. Write permissions are required to both the directory that contains old_p and the directory that contains new_p. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* non-existing directory, not ending with a directory separator, and whose parent directory exists: The pathname new_p is linked to the directory and old_p is unlinked from the directory. Write permissions are required to both the directory that contains old_p and the directory that contains new_p. 
* Symlinks are not followed: if old_p is a symlink, it is itself renamed, not its target. If new_p is an existing symlink, it is itself erased, not its target. 
Rename fails if 
* new_p ends with dot or with dot-dot 
* new_p names a non-existing directory ending with a directory separator 
* old_p is a directory which is an ancestor of new_p 

<h2>Parameters</h2>

old_p - path to move or rename 
new_p - target path for the move/rename operation 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with old_p as the first argument, new_p as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    fs::path p = fs::current_path() / &quot;sandbox&quot;;
    fs::create_directories(p / &quot;from&quot;);
    std::ofstream(p / &quot;from/file1.txt&quot;).put('a');
    fs::create_directory(p / &quot;to&quot;);
    //    fs::rename(p/&quot;from/file1.txt&quot;, p/&quot;to/&quot;); // error: to is a directory
    fs::rename(p / &quot;from/file1.txt&quot;, p / &quot;to/file2.txt&quot;); // OK

    //    fs::rename(p/&quot;from&quot;, p/&quot;to&quot;); // error: to is not empty
    fs::rename(p / &quot;from&quot;, p / &quot;to/subdir&quot;); // OK
    fs::remove_all(p);
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;renames a file 
rename <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes a file or empty directory 
remove removes a file or directory and all its contents, recursively 
remove_all <i>(function)</i> 
