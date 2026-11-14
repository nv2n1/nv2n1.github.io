---
title: "stdexperimentalfilesystempermissions(3)"
name: "stdexperimentalfilesystempermissions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempermissions/"
---

std::experimental::filesystem::permissions - std::experimental::filesystem::permissions

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    void permissions(const path &amp;p, perms prms);
(filesystem TS)

    void permissions(const path &amp;p, perms prms, error_code &amp;ec);</code></pre> 
Changes access permissions of the file to which p resolves, as if by POSIX fchmodat. Symlinks are followed if prms::resolve_symlinks is set. 
The effects depend on prms as follows: 
* If neither perms::add_perms nor perms::remove_perms is set, file permissions are set to exactly prms &amp; fs::perms::mask (meaning, every valid bit of prms is applied) 
* If perms::add_perms, the file permissions are set to exactly status(p).permissions() | (prms &amp; perms::mask) (meaning, any valid bit that is set in prms, but not in the file's current permissions is added to the file's permissions) 
* If perms::remove_perms is set, the file permissions are set to exactly status(p).permissions() &amp; ~(prms &amp; perms::mask) (meaning, any valid bit that is clear in prms, but set in the file's current permissions is cleared in the file's permissions) 
* If both perms::add_perms and perms::remove_perms are set, error occurs 
The non-throwing overload has no special action on error. 

<h2>Parameters</h2>

p - path to examine 
prms - permissions to set, add, or remove 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Notes</h2>

Permissions may not necessarily be implemented as bits, but they are treated that way conceptually. 
Some permission bits may be ignored on some systems, and changing some bits may automatically change others (e.g. on platforms without owner/group/all distinction, setting any of the three write bits set all three) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;fstream&gt;

#include &lt;bitset&gt;

#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
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
    fs::permissions(&quot;test.txt&quot;, fs::perms::add_perms |
                                    fs::perms::owner_all | fs::perms::group_all);
    std::cout &lt;&lt; &quot;After adding o+rwx and g+rwx:  &quot;;
    demo_perms(fs::status(&quot;test.txt&quot;).permissions());
    fs::remove(&quot;test.txt&quot;);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Created file with permissions: rw-r--r-- 
&nbsp;<wbr>&nbsp;After adding o+rwx and g+rwx: rwxrwxr--

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;identifies file system permissions 
perms <i>(enum)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes 
status determines file attributes, checking the symlink target 
symlink_status <i>(function)</i> 
