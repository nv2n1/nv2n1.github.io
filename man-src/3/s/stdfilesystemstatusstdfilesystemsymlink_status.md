---
title: "stdfilesystemstatusstdfilesystemsymlink_status(3)"
name: "stdfilesystemstatusstdfilesystemsymlink_status"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemstatusstdfilesystemsymlink_status/"
description: "std::filesystem::status,std::filesystem::symlink_status – std::filesystem::status,std::filesystem::symlink_status"
---

<p>std::filesystem::status,std::filesystem::symlink_status &#8211; std::filesystem::status,std::filesystem::symlink_status</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;filesystem&gt;

    std::filesystem::file_status status(const std::filesystem::path &amp;p);

std::filesystem::file_status status(const std::filesystem::path &amp;p, (1)(since C++ 17)

                                                                        std::error_code &amp;ec) noexcept;

std::filesystem::file_status symlink_status(const std::filesystem::path &amp;p);

std::filesystem::file_status symlink_status(const std::filesystem::path &amp;p, (2)(since C++ 17)

                                                                                std::error_code &amp;ec) noexcept;</code></pre>
<p>1) Determines the type and attributes of the filesystem object identified by p as if by POSIX stat (symlinks are followed to their targets). In the following description, prms is the result of (m &amp; perms::mask), where m is obtained as if by taking st_mode from the POSIX struct stat and converting it to the type std::filesystem::perms.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a regular file (as if by POSIX S_ISREG), returns file_status(file_type::regular, prms).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a directory (as if by POSIX S_ISDIR), returns file_status(file_type::directory, prms)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a block special file (as if by POSIX S_ISBLK), returns file_status(file_type::block, prms)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a character special file (as if by POSIX S_ISCHR), returns file_status(file_type::character, prms)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a fifo or pipe file (as if by POSIX S_ISFIFO), returns file_status(file_type::fifo, prms)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a socket (as if by POSIX S_ISSOCK), returns file_status(file_type::socket, prms)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p has an implementation-defined file type, returns file_status(file_type::A, prms) where A is the implementation-defined file_type constant for that type.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p does not exist, returns file_status(file_type::not_found)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p exists but file attributes cannot be determined, e.g. due to lack of permissions, returns file_status(file_type::unknown)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If errors prevent even knowing whether p exists, the non-throwing overload sets ec and returns file_status(file_type::none), and the throwing overload throws filesystem_error<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, returns file_status(file_type::unknown, prms)<br />
2) Same as <code>(1)</code> except that the behavior is as if the POSIX lstat is used (symlinks are not followed):<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a symlink, returns file_status(file_type::symlink) </p>
<h2>Parameters</h2>
<p>p &#8211; path to examine<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>The file status (a file_status object) </p>
<h2>Exceptions</h2>
<p>The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>The information provided by this function is usually also provided as a byproduct of directory iteration, and may be obtained by the member functions of directory_entry. During directory iteration, calling status again is unnecessary. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

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
        std::cout &lt;&lt; &quot; is a regular file
&quot;;
    if (fs::is_directory(s))
        std::cout &lt;&lt; &quot; is a directory
&quot;;
    if (fs::is_block_file(s))
        std::cout &lt;&lt; &quot; is a block device
&quot;;
    if (fs::is_character_file(s))
        std::cout &lt;&lt; &quot; is a character device
&quot;;
    if (fs::is_fifo(s))
        std::cout &lt;&lt; &quot; is a named IPC pipe
&quot;;
    if (fs::is_socket(s))
        std::cout &lt;&lt; &quot; is a named IPC socket
&quot;;
    if (fs::is_symlink(s))
        std::cout &lt;&lt; &quot; is a symlink
&quot;;
    if (!fs::exists(s))
        std::cout &lt;&lt; &quot; does not exist
&quot;;
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
<p>&nbsp;<wbr>&nbsp;&quot;sandbox/file&quot; is a regular file<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/dir&quot; is a directory<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/pipe&quot; is a named IPC pipe<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/sock&quot; is a named IPC socket<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/symlink&quot; is a symlink<br />
&nbsp;<wbr>&nbsp;&quot;dev/null&quot; is a character device<br />
&nbsp;<wbr>&nbsp;&quot;dev/sda&quot; is a block device<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/no&quot; does not exist</p>
<h2>See also</h2>
<p>file_status represents file type and permissions<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++17)</i><br />
status_known checks whether file status is known<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_block_file checks whether the given path refers to block device<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_character_file checks whether the given path refers to a character device<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_directory checks whether the given path refers to a directory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_fifo checks whether the given path refers to a named pipe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_other checks whether the argument refers to an other file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_regular_file checks whether the argument refers to a regular file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_socket checks whether the argument refers to a named IPC socket<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
is_symlink checks whether the argument refers to a symbolic link<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
exists checks whether path refers to existing file system object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;status of the file designated by this directory entry<br />
status symlink_status of the file designated by this directory entry<br />
symlink_status <i>(public member function of std::filesystem::directory_entry)</i> </p>
