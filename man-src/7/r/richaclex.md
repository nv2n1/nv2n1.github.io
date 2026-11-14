---
title: "richaclex(7)"
name: "richaclex"
section: "7"
letter: "r"
url: "/docs/linux/man/7-richaclex/"
description: "richaclex – RichACL Examples"
---

<p>richaclex &#8211; RichACL Examples</p>
<h2>Description</h2>
<p>This man-page demonstrates the various features of Rich Access Control Lists (RichACLs) by example, and shows how they interact with the POSIX file permission bits. </p>
<p> For a complete description of the structure, concepts, and algorithms involved, please refer to <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7).</p>
<h2>Examples</h2>
<h3>Traditional POSIX file permissions as RichACLs</h3>
<p>In the traditional POSIX file permission model, each file and directory has a file mode that specifies the file type and file permission bits. The file permission bits determine the permissions for the owner, group, and other classes of processes. The owner class includes processes which are the file owner. The group class includes processes which are not the file owner and which are either a user mentioned in an ACL, or which are in the owning group or in a group mentioned in an ACL. The other class includes all processes which are not in the owner or group class. </p>
<p> In the absence of inheritable permissions, when a file or directory is created, the effective file permissions of the new file or directory are <i>(mode&nbsp;<wbr>&amp;&nbsp;<wbr>~umask)</i>, where <i>mode</i> is the mode parameter to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), and similar, and <i>umask</i> is the process umask (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)): </p>
<dl>
<dd>
<pre>$ <code>umask</code>
0022
$ <code>touch f</code>
$ <code>ls -l f</code>
-rw-r--r-- 1 agruenba users 0 Feb 24 09:37 f</pre>
</dl>
<p> Here, the <i>umask</i> has a value of 022. The <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command calls <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with a <i>mode</i> parameter of 0666 to create a new file, and the resulting effective file permissions are 0644, displayed as rw-r&#8211;r&#8211; by <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1): the owner has read and write access, and the group and other classes have read access only. </p>
<p> These permissions are displayed as a RichACL as follows: </p>
<dl>
<dd>
<pre>$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow
 everyone@:r------------::allow
$ <code>getrichacl --long f</code>
f:
 owner@:read_data/write_data/append_data::allow
 everyone@:read_data::allow</pre>
</dl>
<p> RichACLs have both a short text form in which each permission is represented by a single letter, and a long text form in which each permission is represented by an equivalent string. The <code>owner@</code> special indentifier refers to the file owner, an the <code>everyone@</code> special identifier refers to everyone including the owner and the owning group. The POSIX read permission maps to the RichACL <code>read_data</code>&nbsp;<wbr>(<code>r</code>) permission; the POSIX write permission maps to the RichACL <code>write_data</code>&nbsp;<wbr>(<code>w</code>) and <code>append_data</code>&nbsp;<wbr>(<code>p</code>) permissions. </p>
<p> Creating directories works similarly: </p>
<dl>
<dd>
<pre>$ <code>mkdir d</code>
$ <code>ls -dl d</code>
drwxr-xr-x 2 agruenba users 4096 Feb 24 09:37 d</pre>
</dl>
<p> Here, the <code><a href="/docs/linux/man/1-mkdir/">mkdir</a></code>(1) command calls <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2) with a <i>mode</i> parameter of 0777 to create a new directory, and the resulting effective file permissions are 0755, displayed as rwxr-xr-x by <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1). The owner has read, write and execute (search) access, and the group and other classes have read and execute (search) access. </p>
<p> These permissions are displayed as a RichACL as follows: </p>
<dl>
<dd>
<pre>$ <code>getrichacl d</code>
d:
 owner@:rwpxd--------::allow
 everyone@:r--x---------::allow
$ <code>getrichacl --long d</code>
d:
 owner@:list_directory/add_file/add_subdirectory/execute/delete_child::allow
 everyone@:list_directory/execute::allow</pre>
</dl>
<p> For directories, the POSIX read permission maps to the RichACL <code>list_directory</code>&nbsp;<wbr>(<code>r</code>) permission; the POSIX write permission maps to the RichACL <code>add_file</code>&nbsp;<wbr>(<code>w</code>), <code>add_subdirectory</code>&nbsp;<wbr>(<code>p</code>), and <code>delete_child</code>&nbsp;<wbr>(<code>d</code>) permissions; the POSIX execute (search) permission maps to the RichACL <code>execute</code>&nbsp;<wbr>(<code>x</code>) permission. The long text forms for some of the permissions differ between files and directories. When setting ACLs, either form can be used interchangeably. </p>
<p> When the file permission bits of a file are set to the unusual value of 0604, the owning group will not have read access, but everyone else will. This maps to the following RichACL: </p>
<dl>
<dd>
<pre>$ <code>chmod 604 f</code>
$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow
 group@:r------------::deny
 everyone@:r------------::allow</pre>
</dl>
<p> A <code>deny</code> entry for the owning group (<code>group@</code>) before the final <code>allow</code> entry for everyone else indicates that the owning group is denied <code>read_data</code>&nbsp;<wbr>(<code>r</code>) access.</p>
<h3>RichACLs</h3>
<p>RichACLs can be used for granting users and groups additional permissions, or for denying them some permissions. This includes permissions that go beyond what can be granted by the traditional POSIX read, write, and execute permissions. The following example grants user Tim the right to read, write, and append to a file, to change the file&#8217;s permissions (<code>write_acl</code>&nbsp;<wbr>(<code>C</code>)), and to take ownership of the file (<code>write_owner</code>&nbsp;<wbr>(<code>o</code>)): </p>
<dl>
<dd>
<pre>$ <code>touch f</code>
$ <code>ls -l f</code>
-rw-r--r-- 1 agruenba users 0 Feb 24 09:37 f
$ <code>setrichacl --modify user:tim:rwpCo::allow f</code>
$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow
 everyone@:r------------::allow
 user:tim:rwp------Co--::allow
$ <code>ls -l f</code>
-rw-rw-r--+ 1 agruenba users 0 Feb 24 09:37 f</pre>
</dl>
<p> Setting the ACL has updated the file permission bits, and <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) shows a <code>+</code> sign after the file permissions to indicate that the file now has an ACL. The change in file permission bits indicates that one or more members of the group class now have POSIX write access, or a subset of POSIX write access (in this case, the RichACL <code>write_data</code>&nbsp;<wbr>(<code>w</code>) and <code>append_data</code>&nbsp;<wbr>(<code>p</code>) permissions). </p>
<p> The group class permissions <i>are not</i> the same as the permissions of the owning group; the owning group still only has <code>read_data</code>&nbsp;<wbr>(<code>r</code>) access. </p>
<p> In general, when the ACL of a file or directory is changed, the file permission bits are updated to reflect the maximum permissions of each of the file classes as closely as possible. Permissions that go beyond the POSIX read, write, and execute permissions are not reflected in the file permission bits.</p>
<h3>Changing the file permission bits</h3>
<p>When the file permission bits of a file or directory are changed with <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), POSIX requires that the new file permission bits define the maximum permissions that any process is granted. Therefore, when the file permission bits of file f from the previous example are changed to 0664 (their current value), the following happens: </p>
<dl>
<dd>
<pre>$ <code>chmod 664 f</code>
$ <code>ls -l f</code>
-rw-rw-r--+ 1 agruenba users 0 Feb 24 09:37 f
$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow
 user:tim:rwp----------::allow
 everyone@:r------------::allow</pre>
</dl>
<p> User Tim loses the <code>write_acl</code>&nbsp;<wbr>(<code>C</code>) and <code>write_owner</code>&nbsp;<wbr>(<code>o</code>) permissions. In addition, the entry for the special identifier <code>everyone@</code> moves to the end of the ACL; this does not change the permissions that the ACL grants. </p>
<p> When the file permission bits are changed so that only the file owner has access to the file, the ACL changes in the following way: </p>
<dl>
<dd>
<pre>$ <code>chmod 600 f</code>
$ <code>ls -l f</code>
-rw-------+ 1 agruenba users 0 Feb 24 09:37 f
$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow</pre>
</dl>
<p> The ACL reflects that user Tim and the special identfier <code>everyone@</code> no longer have access to the file. The permissions prevously granted by the ACL have not entirely disappeared, they are merely masked by the new file permission bits, though (by way of the file masks; see <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7)). When the file permission bits are changed back to their previous value, those permissions become effective again: </p>
<dl>
<dd>
<pre>$ <code>chmod 664 f</code>
$ <code>ls -l f</code>
-rw-rw-r--+ 1 agruenba users 0 Feb 24 09:37 f
$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow
 user:tim:rwp----------::allow
 everyone@:r------------::allow</pre>
</dl>
<p> When the file permission bits are changed to the value 0666, we end up with the following result: </p>
<dl>
<dd>
<pre>$ <code>chmod 666 f</code>
$ <code>ls -l f</code>
-rw-rw-rw-+ 1 agruenba users 0 Feb 24 09:37 f
$ <code>getrichacl f</code>
f:
 owner@:rwp----------::allow
 user:tim:rwp----------::allow
 group@:-wp----------::deny
 everyone@:rwp----------::allow</pre>
</dl>
<p> By giving POSIX write access to the other class, the <code>everyone@</code> special identifier has gained <code>write_data</code>&nbsp;<wbr>(<code>w</code>) and <code>append_data</code>&nbsp;<wbr>(<code>p</code>) access to the file. The owning group still only has <code>read_data</code>&nbsp;<wbr>(<code>r</code>) access, though.</p>
<h3>Inheritance of permissions at file-creation time</h3>
<p>When a file or directory is created, the ACL of the parent directory defines which of the parent&#8217;s ACL entries the new file or directory will inherit: files will inherit entries with the <code>file_inherit</code>&nbsp;<wbr>(<code>f</code>) flag set. Directories will inherit entries with the <code>dir_inherit</code>&nbsp;<wbr>(<code>d</code>) flag set. In addition, directories will inherit entries with the <code>file_inherit</code>&nbsp;<wbr>(<code>f</code>) flag set as inheritable-only permissions for their children; the <code>inherit_only</code>&nbsp;<wbr>(<code>i</code>) flag is set. The <code>no_propagate</code>&nbsp;<wbr>(<code>n</code>) flag can be used to inherit permissions one level deep only. </p>
<p> When a file or directory inherits permissions, the file permissions are determined by the <i>mode</i> parameter as given to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), and similar, and by the inherited permissions; the process umask (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)) is ignored. </p>
<p> The following example creates a directory and sets up inheritable permissions for files and subdirectories (the example is indented and padded with dashes for improved readability): </p>
<dl>
<dd>
<pre>$ <code>mkdir d</code>
$ <code>setrichacl --set '</code>
&gt; <code> owner@:rwpxd:fd:allow</code>
&gt; <code> user:tim:rwpxd:fd:allow</code>
&gt; <code>group:staff:r--x-:f-:allow</code>
&gt; <code> everyone@:r--x-:fd:allow' d</code></pre>
</dl>
<p> Of the four ACL entries, three are inheritable for files and directories (the <code>file_inherit</code>&nbsp;<wbr>(<code>f</code>) and <code>dir_inherit</code>&nbsp;<wbr>(<code>d</code>) flags are set), and the entry for group Staff is inheritable for files only (the <code>dir_inherit</code>&nbsp;<wbr>(<code>d</code>) flag is not set). </p>
<p> Files created inside <code>d</code> inherit the following permissions: </p>
<dl>
<dd>
<pre>$ <code>touch d/f</code>
$ <code>ls -l d/f</code>
-rw-rw-r--+ 1 agruenba users 0 Feb 24 09:37 d/f
$ <code>getrichacl d/f</code>
d/f:
 owner@:rwp----------::allow
 user:tim:rwp----------::allow
 group:staff:r------------::allow
 everyone@:r------------::allow</pre>
</dl>
<p> The <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command calls <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with a <i>mode</i> parameter of 0666 to create a new file, so the <code>execute</code>&nbsp;<wbr>(<code>x</code>) permission is masked by the file permission bits. When the file permission bits are changed to the value 0775 with <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), the ACL changes as follows: </p>
<dl>
<dd>
<pre>$ <code>chmod 775 d/f</code>
$ <code>getrichacl d/f</code>
d/f:
 owner@:rwpx---------::allow
 user:tim:rwpx---------::allow
 group:staff:r--x---------::allow
 everyone@:r--x---------::allow</pre>
</dl>
<p> Directories created inside <code>d</code> inherit the following permissions: </p>
<dl>
<dd>
<pre>$ <code>mkdir d/d</code>
$ <code>ls -dl d/d</code>
drwxrwxr-x+ 2 agruenba users 4096 Feb 24 09:37 d/d
$ <code>getrichacl d/d</code>
d/d:
 owner@:rwpxd--------:fd:allow
 user:tim:rwpxd--------:fd:allow
 group:staff:r--x---------:fi:allow
 everyone@:r--x---------:fd:allow</pre>
</dl>
<p> The <code>inherit_only</code>&nbsp;<wbr>(<code>i</code>) flag of the entry for group Staff is set to indicate that the entry has no effect on the effective permissions of <code>d/d</code>. When a file is created inside <code>d/d</code>, the <code>inherit_only</code>&nbsp;<wbr>(<code>i</code>) flag in the entry inherited by the file is cleared again, and the resulting ACL is somilar to that of <code>d/f</code>.</p>
<h3>Inheritance of file permission bits only</h3>
<p>When the permissions inherited by a new file or directory can be exactly represented by the file permission bits, only the file permission bits of the new file or directory will be set, and no ACL will be stored (no <code>+</code> sign is shown after the file permission bits): </p>
<dl>
<dd>
<pre>$ <code>ls -dl d</code>
drw-------+ 3 agruenba users 4096 Feb 24 09:37 d
$ <code>getrichacl d</code>
d:
 owner@:rwp----------:f:allow
$ <code>touch d/f</code>
$ <code>ls -l d/f</code>
-rw------- 1 agruenba users 0 Feb 24 09:37 d/f
$ <code>getrichacl d/f</code>
d/f:
 owner@:rwp----------::allow</pre>
</dl>
<h3>Automatic Inheritance</h3>
<p>The NFSv4 and SMB network protocols support creating files and directories without specifying any permissions for the new file or directory. When the directory in which such a file is created has the <code>auto_inherit</code>&nbsp;<wbr>(<code>a</code>) ACL flag set, then the new files and directories created in the directory will have the <code>auto_inherit</code>&nbsp;<wbr>(<code>a</code>) ACL flag set, and each ACL entry inherited from the parent directory will have the <code>inherited</code>&nbsp;<wbr>(<code>a</code>) flag set. For example, consider the following directory: </p>
<dl>
<dd>
<pre>$ <code>ls -dl d</code>
drw-rw----+ 2 agruenba users 4096 Feb 24 09:37 d
$ <code>getrichacl d</code>
d:
 flags:a
 owner@:rwp----------:f:allow
 user:tim:rwp----------:f:allow</pre>
</dl>
<p> When a file is created inside that directory without specifying any file permissions, the file inherits the following ACL: </p>
<dl>
<dd>
<pre>$ <code>getrichacl d/f</code>
d/f:
 flags:a
 owner@:rwp----------:a:allow
 user:tim:rwp----------:a:allow</pre>
</dl>
<p> When the ACL of the directory is then changed, those changes propagate to the file: </p>
<dl>
<dd>
<pre>$ <code>setrichacl --modify group:staff:r:f:allow d</code>
$ <code>getrichacl d/f</code>
d:
 flags:a
 owner@:rwp----------:a:allow
 user:tim:rwp----------:a:allow
 group:staff:r------------:a:allow</pre>
</dl>
<p> When ACL entries are propagated from a directory to one of its children (the files and directories inside the directory), all entries in the child&#8217;s ACL that have the <code>inherited</code>&nbsp;<wbr>(<code>a</code>) flag set are removed, and the child inherits ACL entries from the parent in the same way as when a new file or directory is created. The <code>inherited</code>&nbsp;<wbr>(<code>a</code>) flag of those inherited entries is set. Existing entries in the child&#8217;s ACL that do not have the <code>inherited</code>&nbsp;<wbr>(<code>a</code>) flag set are left untouched: </p>
<dl>
<dd>
<pre>$ <code>setrichacl --modify user:ada:rwp::allow d/f</code>
$ <code>getrichacl d/f</code>
d:
 flags:a
 user:ada:rwp----------::allow
 owner@:rwp----------:a:allow
 user:tim:rwp----------:a:allow
 group:staff:r------------:a:allow
$ <code>setrichacl --modify group:staff:::allow d</code>
$ <code>getrichacl d</code>
d:
 flags:a
 owner@:rwp----------:f:allow
 user:tim:rwp----------:f:allow
$ <code>getrichacl d/f</code>
d:
 flags:a
 user:ada:rwp----------::allow
 owner@:rwp----------:a:allow
 user:tim:rwp----------:a:allow</pre>
</dl>
<p> We remove the allow entry for group Staff from the ACL by assigning it an empty set of permissions. </p>
<p> When the file permission bits of a file or directory are changed with <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), the Automatic Inheritance algorithm must no longer override those permissions. Likewise, when a file or directory is created with <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), or similar, the <i>mode</i> parameter to those system calls defines an upper limit to the file permission bits of the new file or directory, and the Automatic Inheritance algorithm must no longer override the resulting permissions. To achieve that, when the ACL of the file or directory has the <code>auto_inherit</code>&nbsp;<wbr>(<code>a</code>) flag set, those operations set the <code>protected</code>&nbsp;<wbr>(<code>p</code>) flag, which stops the Automatic Inheritance algorithm from modifying the ACL: </p>
<dl>
<dd>
<pre>$ <code>chmod 660 d/f</code>
$ <code>getrichacl d/f</code>
d/f:
 flags:ap
 user:ada:rwp----------::allow
 owner@:rwp----------:a:allow
 user:tim:rwp----------:a:allow
$ <code>touch d/g</code>
$ <code>getrichacl d/g</code>
d/g:
 flags:ap
 owner@:rwp----------:a:allow
 user:tim:rwp----------:a:allow</pre>
</dl>
<h3>Effective permissions</h3>
<p>With complex ACLs, it can become difficult to determine the permissions of a particular user or group. In this situation, the <code>&#8211;access</code> option of <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1) can be used: </p>
<dl>
<dd>
<pre>$ <code>getrichacl --access d/f</code>
rwpx--------- d/f
$ <code>getrichacl --access=tim d/f</code>
rwpx--------- d/f
$ <code>getrichacl --access=:staff d/f</code>
r--x--------- d/f</pre>
</dl>
<p> When the <code>&#8211;access</code> option is used without arguments, getrichacl displays the permissions the current process has for the specified file or files. With a user name as the argument, getrichacl displays the permissions of that user. With a colon followed by a group name, getrichacl displays the permissions of that group.</p>
<h2>Author</h2>
<p>Written by Andreas Grünbacher &lt;agruenba [at] redhat.com&gt;. </p>
<p> Please send your bug reports, suggested features and comments to the above address.</p>
<h2>Conforming To</h2>
<p>Rich Access Control Lists are Linux-specific.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1), <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1), <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7) </p>
