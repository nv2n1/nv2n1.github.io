---
title: "stdexperimentalfilesystemcopy_options(3)"
name: "stdexperimentalfilesystemcopy_options"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcopy_options/"
---

std::experimental::filesystem::copy_options - std::experimental::filesystem::copy_options

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/filesystem&gt;

enum class copy_options {

    none = 0,

    skip_existing = 1,

    overwrite_existing = 2,

    update_existing = 4,

    recursive = 8,                               (filesystem TS)

    copy_symlinks = 16,

    skip_symlinks = 32,

    directories_only = 64,

    create_symlinks = 128,

    create_hard_links = 256

};</code></pre> 
This type represents available options that control the behavior of the copy() and copy_file() function. 
copy_options satisfies the requirements of BitmaskType (which means the bitwise operators operator&amp;, operator|, operator^, operator~, operator&amp;=, operator|=, and operator^= are defined for this type) 

<h2>Member constants</h2>

At most one copy option in each of the following options groups may be present, otherwise the behavior of the copy functions is undefined. 

 
Member constant Value Meaning 
options controlling copy_file() when the file already exists 
skip_existing 1 Keep the existing file, without reporting an error. 
overwrite_existing 2 Replace the existing file 
update_existing 4 Replace the existing file only if it is older than the file being copied 
options controlling the effects of copy() on subdirectories 
recursive 8 Recursively copy subdirectories and their content 
options controlling the effects of copy() on symbolic links 
copy_symlinks 16 Copy symlinks as symlinks, not as the files they point to 
skip_symlinks 32 Ignore symlinks 
options controlling the kind of copying copy() does 
directories_only 64 Copy the directory structure, but do not copy any non-directory files 
create_symlinks 128 Instead of creating copies of files, create symlinks pointing to the originals. Note: the source path must be an absolute path unless the destination path is in the current directory. 
create_hard_links 256 Instead of creating copies of files, create hardlinks that resolve to the same files as the originals

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies files or directories 
copy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies file contents 
copy_file <i>(function)</i> 
