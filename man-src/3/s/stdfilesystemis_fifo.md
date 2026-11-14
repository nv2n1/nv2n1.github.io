---
title: "stdfilesystemis_fifo(3)"
name: "stdfilesystemis_fifo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemis_fifo/"
---

std::filesystem::is_fifo - std::filesystem::is_fifo

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    bool is_fifo(std::filesystem::file_status s) noexcept;
(1)(since C++ 17)

    bool is_fifo(const std::filesystem::path &amp;p);
(2)(since C++ 17)

    bool is_fifo(const std::filesystem::path &amp;p, std::error_code &amp;ec) noexcept;</code></pre> 
Checks if the given file status or path corresponds to a FIFO or pipe file as if determined by POSIX S_ISFIFO. 
1) Equivalent to s.type() == file_type::fifo. 
2) Equivalent to is_fifo(status(p)) or is_fifo(status(p, ec)) respectively 

<h2>Parameters</h2>

s - file status to check 
p - path to query 
ec - error code to modify in case of errors

<h2>Return value</h2>

true if the file indicated by p or if the type indicated s refers to a FIFO pipe, false otherwise. The non-throwing overload returns false if an error occurs. 

<h2>Exceptions</h2>

2) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdio&gt;

#include &lt;cstring&gt;

#include &lt;filesystem&gt;

#include &lt;unistd.h&gt;

#include &lt;sys/socket.h&gt;

#include &lt;sys/un.h&gt;

#include &lt;sys/stat.h&gt;
namespace fs = std::filesystem;
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

status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
file_status represents file type and permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
status_known checks whether file status is known 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_block_file checks whether the given path refers to block device 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_character_file checks whether the given path refers to a character device 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_directory checks whether the given path refers to a directory 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_other checks whether the argument refers to an other file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_regular_file checks whether the argument refers to a regular file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_socket checks whether the argument refers to a named IPC socket 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
is_symlink checks whether the argument refers to a symbolic link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
exists checks whether path refers to existing file system object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the directory entry refers to a named pipe 
is_fifo <i>(public member function of std::filesystem::directory_entry)</i> 
