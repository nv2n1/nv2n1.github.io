---
title: "stdfilesystempermissions(3)"
name: "stdfilesystempermissions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempermissions/"
---

std::filesystem::permissions - std::filesystem::permissions

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    void permissions(const std::filesystem::path &amp;p,

                     std::filesystem::perms prms,

                     std::filesystem::perm_options opts = perm_options::replace);

void permissions(const std::filesystem::path &amp;p,

                 std::filesystem::perms prms, (since C++ 17)

                                                  std::error_code &amp;ec) noexcept;

void permissions(const std::filesystem::path &amp;p,

                 std::filesystem::perms prms,

                 std::filesystem::perm_options opts,

                 std::error_code &amp;ec);</code></pre> 
Changes access permissions of the file to which p resolves, as if by POSIX fchmodat. Symlinks are followed unless perm_options::nofollow is set in opts 
The second signature behaves as if called with opts set to perm_options::replace 
The effects depend on prms and opts as follows: 
* If opts is perm_options::replace, file permissions are set to exactly prms &amp; std::filesystem::perms::mask (meaning, every valid bit of prms is applied) 
* If opts is perm_options::add, the file permissions are set to exactly status(p).permissions() | (prms &amp; perms::mask) (meaning, any valid bit that is set in prms, but not in the file's current permissions is added to the file's permissions) 
* If opts is perm_options::remove, the file permissions are set to exactly status(p).permissions() &amp; ~(prms &amp; perms::mask) (meaning, any valid bit that is clear in prms, but set in the file's current permissions is cleared in the file's permissions) 
opts is required to have only one of replace, add, or remove to be set. 
The non-throwing overload has no special action on error. 

<h2>Parameters</h2>

p - path to examine 
prms - permissions to set, add, or remove 
opts - options controlling the action taken by this function 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

Permissions may not necessarily be implemented as bits, but they are treated that way conceptually. 
Some permission bits may be ignored on some systems, and changing some bits may automatically change others (e.g. on platforms without owner/group/all distinction, setting any of the three write bits set all three) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;fstream&gt;

#include &lt;bitset&gt;

#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
void demo_perms(fs::perms p)

{
    std::cout &lt;&lt; ((p &amp; fs::perms::owner_read) != fs::perms::none ? &quot;r&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::owner_write) != fs::perms::none ? &quot;w&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::owner_exec) != fs::perms::none ? &quot;x&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::group_read) != fs::perms::none ? &quot;r&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::group_write) != fs::perms::none ? &quot;w&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::group_exec) != fs::perms::none ? &quot;x&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::others_read) != fs::perms::none ? &quot;r&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::others_write) != fs::perms::none ? &quot;w&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::others_exec) != fs::perms::none ? &quot;x&quot; : &quot;-&quot;)
              &lt;&lt; '\n';
}

int main()

{
    std::ofstream(&quot;test.txt&quot;); // create file
    std::cout &lt;&lt; &quot;Created file with permissions: &quot;;
    demo_perms(fs::status(&quot;test.txt&quot;).permissions());
    fs::permissions(&quot;test.txt&quot;,
                    fs::perms::owner_all | fs::perms::group_all,
                    fs::perm_options::add);
    std::cout &lt;&lt; &quot;After adding o+rwx and g+rwx:  &quot;;
    demo_perms(fs::status(&quot;test.txt&quot;).permissions());
    fs::remove(&quot;test.txt&quot;);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Created file with permissions: rw-r--r-- 
&nbsp;<wbr>&nbsp;After adding o+rwx and g+wrx: rwxrwxr--

<h2>See also</h2>

perms identifies file system permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++17)</i> 
status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
