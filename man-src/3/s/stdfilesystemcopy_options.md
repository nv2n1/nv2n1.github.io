---
title: "stdfilesystemcopy_options(3)"
name: "stdfilesystemcopy_options"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcopy_options/"
---

std::filesystem::copy_options - std::filesystem::copy_options

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;filesystem&gt;

enum class copy_options {

    none = /* unspecified */,

    skip_existing = /* unspecified */,

    overwrite_existing = /* unspecified */,

    update_existing = /* unspecified */,

    recursive = /* unspecified */,           (since C++17)

    copy_symlinks = /* unspecified */,

    skip_symlinks = /* unspecified */,

    directories_only = /* unspecified */,

    create_symlinks = /* unspecified */,

    create_hard_links = /* unspecified */

};</code></pre> 
This type represents available options that control the behavior of the copy() and copy_file() function. 
copy_options satisfies the requirements of BitmaskType (which means the bitwise operators operator&amp;, operator|, operator^, operator~, operator&amp;=, operator|=, and operator^= are defined for this type). none represents the empty bitmask; every other enumerator represents a distinct bitmask element. 

<h2>Member constants</h2>

At most one copy option in each of the following options groups may be present, otherwise the behavior of the copy functions is undefined. 

 
Member constant Meaning 
options controlling copy_file() when the file already exists 
none Report an error (default behavior) 
skip_existing Keep the existing file, without reporting an error. 
overwrite_existing Replace the existing file 
update_existing Replace the existing file only if it is older than the file being copied 
options controlling the effects of copy() on subdirectories 
none Skip subdirectories (default behavior) 
recursive Recursively copy subdirectories and their content 
options controlling the effects of copy() on symbolic links 
none Follow symlinks (default behavior) 
copy_symlinks Copy symlinks as symlinks, not as the files they point to 
skip_symlinks Ignore symlinks 
options controlling the kind of copying copy() does 
none Copy file content (default behavior) 
directories_only Copy the directory structure, but do not copy any non-directory files 
create_symlinks Instead of creating copies of files, create symlinks pointing to the originals. Note: the source path must be an absolute path unless the destination path is in the current directory. 
create_hard_links Instead of creating copies of files, create hardlinks that resolve to the same files as the originals

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/dir/subdir&quot;);
    std::ofstream(&quot;sandbox/file1.txt&quot;).put('a');
    fs::copy(&quot;sandbox/file1.txt&quot;, &quot;sandbox/file2.txt&quot;); // copy file
    fs::copy(&quot;sandbox/dir&quot;, &quot;sandbox/dir2&quot;);            // copy directory (non-recursive)
    // sandbox holds 2 files and 2 directories, one of which has a subdirectory
    // sandbox/file1.txt
    // sandbox/file2.txt
    // sandbox/dir2
    // sandbox/dir
    //    sandbox/dir/subdir
    fs::copy(&quot;sandbox&quot;, &quot;sandbox/copy&quot;, fs::copy_options::recursive);
    // sandbox/copy holds copies of the above files and subdirectories
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>

<h2>See also</h2>

copy copies files or directories 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
copy_file copies file contents 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
