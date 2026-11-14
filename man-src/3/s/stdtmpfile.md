---
title: "stdtmpfile(3)"
name: "stdtmpfile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtmpfile/"
---

std::tmpfile - std::tmpfile

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cstdio&gt;

std::FILE* tmpfile();</code></pre> 
Creates and opens a temporary file with a unique auto-generated filename. 
The file is opened as a binary file for update (as by std::fopen with access mode &quot;wb+&quot;). At least TMP_MAX files may be opened during the lifetime of a program (this limit may be shared with std::tmpnam and may be further limited by FOPEN_MAX). 
If the program closes the file, e.g. by executing std::fclose, the file is automatically deleted. 
If the program terminates normally (by calling std::exit, returning from main, etc), all files that were opened by calling std::tmpfile are also automatically deleted. 
If the program terminates abnormally, it is implementation-defined if these temporary files are deleted. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The associated file stream or NULL if an error has occurred 

<h2>Notes</h2>

On some implementations (e.g. Linux), this function actually creates, opens, and immediately deletes the file from the file system: as long as an open file descriptor to a deleted file is held by a program, the file exists, but since it was deleted, its name does not appear in any directory, so that no other process can open it. Once the file descriptor is closed, the space occupied by the file is reclaimed by the filesystem. 
On some implementations (e.g. Windows), elevated privileges are required as the function may create the temporary file in a system directory. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdio&gt;

#include &lt;cstdlib&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    std::FILE *tmpf = std::tmpfile();
    std::fputs(&quot;Hello, world&quot;, tmpf);
    std::rewind(tmpf);
    char buf[6];
    std::fgets(buf, sizeof buf, tmpf);
    std::cout &lt;&lt; buf &lt;&lt; '\n';
    // Linux-specific method to display the tmpfile name
    std::cout &lt;&lt; fs::read_symlink(
                     fs::path(&quot;/proc/self/fd&quot;) / std::to_string(fileno(tmpf)))
              &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Hello 
&nbsp;<wbr>&nbsp;&quot;/tmp/tmpfBlY1lI (deleted)&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a unique filename 
tmpnam <i>(function)</i> 
temp_directory_path returns a directory suitable for temporary files 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
