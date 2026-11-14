---
title: "stdexperimentalfilesystemdirectory_entrystatus(3)"
name: "stdexperimentalfilesystemdirectory_entrystatus"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_entrystatus/"
---

std::experimental::filesystem::directory_entry::status,std::experimental::filesystem::directory_entry::symlink_status - std::experimental::filesystem::directory_entry::status,std::experimental::filesystem::directory_entry::symlink_status

<h2>Synopsis</h2>

<pre><code>file_status status() const;
(1)(filesystem TS)

    file_status status(error_code &amp;ec) const;

file_status symlink_status() const;
(2)(filesystem TS)

    file_status symlink_status(error_code &amp;ec) const;</code></pre> 
1) Returns the potentially cached status of the entry, as if determined by a status call (symlinks are followed to their targets) 
2) Returns the potentially cached status of the entry, as if determined by a symlink_status call (symlinks are not followed) 

<h2>Parameters</h2>

ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The status of the file referred to by the entry. 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Notes</h2>

The file status information is usually provided as a byproduct of directory iteration, in which case it is cached and may be obtained by these member functions without the cost of an additional system call. During directory iteration, calling status is unnecessary and accessors such as is_directory should be called with the cached status value, not with a path. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdio&gt;

#include &lt;cstring&gt;

#include &lt;experimental/filesystem&gt;

#include &lt;unistd.h&gt;

#include &lt;sys/socket.h&gt;

#include &lt;sys/un.h&gt;

#include &lt;sys/stat.h&gt;
namespace fs = std::experimental::filesystem;
void demo_status(const fs::path &amp;p, fs::file_status s)

{
    std::cout &lt;&lt; p;
    // alternative: switch(s.type()) { case fs::file_type::regular: ...}
    if (fs::is_regular_file(s))
        std::cout &lt;&lt; &quot; is a regular file\n&quot;;
    if (fs::is_directory(s))
        std::cout &lt;&lt; &quot; is a directory\n&quot;;
    if (fs::is_block_file(s))
        std::cout &lt;&lt; &quot; is a block device\n&quot;;
    if (fs::is_character_file(s))
        std::cout &lt;&lt; &quot; is a character device\n&quot;;
    if (fs::is_fifo(s))
        std::cout &lt;&lt; &quot; is a named IPC pipe\n&quot;;
    if (fs::is_socket(s))
        std::cout &lt;&lt; &quot; is a named IPC socket\n&quot;;
    if (fs::is_symlink(s))
        std::cout &lt;&lt; &quot; is a symlink\n&quot;;
    if (!fs::exists(s))
        std::cout &lt;&lt; &quot; does not exist\n&quot;;
}

int main()

{
    // create files of different kinds
    fs::create_directory(&quot;sandbox&quot;);
    std::ofstream(&quot;sandbox/file&quot;); // create regular file
    fs::create_directory(&quot;sandbox/dir&quot;);
    mkfifo(&quot;sandbox/pipe&quot;, 0644);
    struct sockaddr_un addr;
    addr.sun_family = AF_UNIX;
    std::strcpy(addr.sun_path, &quot;sandbox/sock&quot;);
    int fd = socket(PF_UNIX, SOCK_STREAM, 0);
    bind(fd, (struct sockaddr *)&amp;addr, sizeof addr);
    fs::create_symlink(&quot;file&quot;, &quot;sandbox/symlink&quot;);
    // demo different status accessors
    for (auto it = fs::directory_iterator(&quot;sandbox&quot;); it != fs::directory_iterator(); ++it)
        demo_status(*it, it-&gt;symlink_status());       // use cached status from directory entry
    demo_status(&quot;dev/null&quot;, fs::status(&quot;/dev/null&quot;)); // direct calls to status
    demo_status(&quot;dev/sda&quot;, fs::status(&quot;/dev/sda&quot;));
    demo_status(&quot;sandbox/no&quot;, fs::status(&quot;/sandbox/no&quot;));
    // cleanup
    close(fd);
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;sandbox/file&quot; is a regular file 
&nbsp;<wbr>&nbsp;&quot;sandbox/dir&quot; is a directory 
&nbsp;<wbr>&nbsp;&quot;sandbox/pipe&quot; is a named IPC pipe 
&nbsp;<wbr>&nbsp;&quot;sandbox/sock&quot; is a named IPC socket 
&nbsp;<wbr>&nbsp;&quot;sandbox/symlink&quot; is a symlink 
&nbsp;<wbr>&nbsp;&quot;dev/null&quot; is a character device 
&nbsp;<wbr>&nbsp;&quot;dev/sda&quot; is a block device 
&nbsp;<wbr>&nbsp;&quot;sandbox/no&quot; does not exist

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents file type and permissions 
file_status <i>(class)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes 
status determines file attributes, checking the symlink target 
symlink_status <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether file status is known 
status_known <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to block device 
is_block_file <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to a character device 
is_character_file <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to a directory 
is_directory <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to a named pipe 
is_fifo <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to an other file 
is_other <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a regular file 
is_regular_file <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a named IPC socket 
is_socket <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a symbolic link 
is_symlink <i>(function)</i> 
