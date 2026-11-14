---
title: "stdexperimentalfilesystemstatusstdexperimentalfilesystemsymlink_status(3)"
name: "stdexperimentalfilesystemstatusstdexperimentalfilesystemsymlink_status"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemstatusstdexperimentalfilesystemsymlink_status/"
description: "std::experimental::filesystem::status,std::experimental::filesystem::symlink_status – std::experimental::filesystem::status,std::experimental::filesystem::symlink_status"
---

<p>std::experimental::filesystem::status,std::experimental::filesystem::symlink_status &#8211; std::experimental::filesystem::status,std::experimental::filesystem::symlink_status</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    file_status status(const path &amp;p);
(1)(filesystem TS)

    file_status status(const path &amp;p, error_code &amp;ec) noexcept;

file_status symlink_status(const path &amp;p);
(2)(filesystem TS)

    file_status symlink_status(const path &amp;p, error_code &amp;ec) noexcept;</code></pre>
<p>1) Determines the type and attributes of the filesystem object identified by p as if by POSIX stat (symlinks are followed to their targets).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a regular file, returns file_status(file_type::regular).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a directory, returns file_status(file_type::directory)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a block special file, returns file_status(file_type::block)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a character special file, returns file_status(file_type::character)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a fifo or pipe file, returns file_status(file_type::fifo)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a socket, returns file_status(file_type::socket)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p does not exist, returns file_status(file_type::not_found)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p exists but file attributes cannot be determined, e.g. due to lack of permissions, returns file_status(file_type::unknown)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If errors prevent even knowing whether p exists, the non-throwing overload sets ec and returns file_status(file_type::none), and the throwing overload throws filesystem_error<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, returns file_status(file_type::unknown)<br />
2) Same as <code>(1)</code> except that the behavior is as if the POSIX lstat is used (symlinks are not followed):<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p is a symlink, returns file_status(file_type::symlink) </p>
<h2>Parameters</h2>
<p>p &#8211; path to examine<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>The file status (a file_status object) </p>
<h2>Exceptions</h2>
<p>The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>The information provided by this function is usually also provided as a byproduct of directory iteration, and may be obtained by the member functions of directory_entry. During directory iteration, calling status again is unnecessary. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

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
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents file type and permissions<br />
file_status <i>(class)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether file status is known<br />
status_known <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to block device<br />
is_block_file <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to a character device<br />
is_character_file <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to a directory<br />
is_directory <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the given path refers to a named pipe<br />
is_fifo <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to an other file<br />
is_other <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a regular file<br />
is_regular_file <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a named IPC socket<br />
is_socket <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a symbolic link<br />
is_symlink <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether path refers to existing file system object<br />
exists <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cached status of the file designated by this directory entry<br />
status cached symlink_status of the file designated by this directory entry<br />
symlink_status <i>(public member function of std::experimental::filesystem::directory_entry)</i> </p>
