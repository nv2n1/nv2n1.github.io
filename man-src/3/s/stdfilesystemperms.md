---
title: "stdfilesystemperms(3)"
name: "stdfilesystemperms"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemperms/"
---

std::filesystem::perms - std::filesystem::perms

<h2>Synopsis</h2>

Defined in header &lt;filesystem&gt; 
enum class perms; <i>(since C++17)</i> 
This type represents file access permissions. perms satisfies the requirements of BitmaskType (which means the bitwise operators operator&amp;, operator|, operator^, operator~, operator&amp;=, operator|=, and operator^= are defined for this type) 
Access permissions model POSIX_permission_bits, and any individual file permissions (as reported by status) are a combination of some of the following bits: 

<h2>Member constants</h2>

Member constant Value (octal) POSIX equivalent Meaning 
none 0 no permission bits are set 
owner_read 0400 S_IRUSR File owner has read permission 
owner_write 0200 S_IWUSR File owner has write permission 
owner_exec 0100 S_IXUSR File owner has execute/search permission 
owner_all 0700 S_IRWXU File owner has read, write, and execute/search permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Equivalent to owner_read | owner_write | owner_exec 
group_read 040 S_IRGRP The file's user group has read permission 
group_write 020 S_IWGRP The file's user group has write permission 
group_exec 010 S_IXGRP The file's user group has execute/search permission 
group_all 070 S_IRWXG The file's user group has read, write, and execute/search permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Equivalent to group_read | group_write | group_exec 
others_read 04 S_IROTH Other users have read permission 
others_write 02 S_IWOTH Other users have write permission 
others_exec 01 S_IXOTH Other users have execute/search permission 
others_all 07 S_IRWXO Other users have read, write, and execute/search permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Equivalent to others_read | others_write | others_exec 
all 0777 All users have read, write, and execute/search permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Equivalent to owner_all | group_all | others_all 
set_uid 04000 S_ISUID Set user ID to file owner user ID on execution 
set_gid 02000 S_ISGID Set group ID to file's user group ID on execution 
sticky_bit 01000 S_ISVTX Implementation-defined meaning, but POSIX XSI specifies that when set on a directory, only file owners may delete files even if the directory is writeable to others (used with /tmp) 
mask 07777 All valid permission bits. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Equivalent to all | set_uid | set_gid | sticky_bit 

 
Additionally, the following constants of this type are defined, which do not represent permissions: 

 
Member constant Value (hex) Meaning 
unknown 0xFFFF Unknown permissions (e.g. when file_status is created without permissions)

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

status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
permissions modifies file access permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
