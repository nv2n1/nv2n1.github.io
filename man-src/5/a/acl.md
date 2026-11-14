---
title: "acl(5)"
name: "acl"
section: "5"
letter: "a"
url: "/docs/linux/man/5-acl/"
description: "acl – Access Control Lists"
---

<p>Linux ACL</p>
<h2>Name</h2>
<p><code>acl</code> &#8211; Access Control Lists</p>
<h2>Description</h2>
<p>This manual page describes POSIX Access Control Lists, which are used to define more fine-grained discretionary access rights for files and directories.</p>
<h2>Acl Types</h2>
<p>Every object can be thought of as having associated with it an ACL that governs the discretionary access to that object; this ACL is referred to as an access ACL. In addition, a directory may have an associated ACL that governs the initial access ACL for objects created within that directory; this ACL is referred to as a default ACL.</p>
<h2>Acl Entries</h2>
<p>An ACL consists of a set of ACL entries. An ACL entry specifies the access permissions on the associated object for an individual user or a group of users as a combination of read, write and search/execute permissions. </p>
<p> An ACL entry contains an entry tag type, an optional entry tag qualifier, and a set of permissions. We use the term qualifier to denote the entry tag qualifier of an ACL entry. </p>
<p> The qualifier denotes the identifier of a user or a group, for entries with tag types of ACL_USER or ACL_GROUP, respectively. Entries with tag types other than ACL_USER or ACL_GROUP have no defined qualifiers. </p>
<p> The following entry tag types are defined:</p>
<dl>
<dt><code>ACL_USER_OBJ</code></p>
<dd>The ACL_USER_OBJ entry denotes access rights for the file owner.</p>
<dt><code>ACL_USER</code></p>
<dd>ACL_USER entries denote access rights for users identified by the entry&#8217;s qualifier.</p>
<dt><code>ACL_GROUP_OBJ</code></p>
<dd>The ACL_GROUP_OBJ entry denotes access rights for the file group.</p>
<dt><code>ACL_GROUP</code></p>
<dd>ACL_GROUP entries denote access rights for groups identified by the entry&#8217;s qualifier.</p>
<dt><code>ACL_MASK</code></p>
<dd>The ACL_MASK entry denotes the maximum access rights that can be granted by entries of type ACL_USER, ACL_GROUP_OBJ, or ACL_GROUP.</p>
<dt><code>ACL_OTHER</code></p>
<dd>The ACL_OTHER entry denotes access rights for processes that do not match any other entry in the ACL.</dl>
<p> When an access check is performed, the ACL_USER_OBJ and ACL_USER entries are tested against the effective user ID. The effective group ID, as well as all supplementary group IDs are tested against the ACL_GROUP_OBJ and ACL_GROUP entries.</p>
<h2>VALID ACLs A valid ACL contains exactly one entry with each of the ACL_USER_OBJ,</h2>
<p>ACL_GROUP_OBJ, and ACL_OTHER tag types. Entries with ACL_USER and ACL_GROUP tag types may appear zero or more times in an ACL. An ACL that contains entries of ACL_USER or ACL_GROUP tag types must contain exactly one entry of the ACL_MASK tag type. If an ACL contains no entries of ACL_USER or ACL_GROUP tag types, the ACL_MASK entry is optional. </p>
<p> All user ID qualifiers must be unique among all entries of ACL_USER tag type, and all group IDs must be unique among all entries of ACL_GROUP tag type. </p>
<p>&nbsp;<wbr>&nbsp;The Fn acl_get_file function returns an ACL with zero ACL entries as the default ACL of a directory, if the directory is not associated with a default ACL. The Fn acl_set_file function also accepts an ACL with zero ACL entries as a valid default ACL for directories, denoting that the directory shall not be associated with a default ACL. This is equivalent to using the Fn acl_delete_def_file function.</p>
<h2>Correspondence Between Acl Entries And File Permission Bits</h2>
<p>The permissions defined by ACLs are a superset of the permissions specified by the file permission bits. </p>
<p> There is a correspondence between the file owner, group, and other permissions and specific ACL entries: the owner permissions correspond to the permissions of the ACL_USER_OBJ entry. If the ACL has an ACL_MASK entry, the group permissions correspond to the permissions of the ACL_MASK entry. Otherwise, if the ACL has no ACL_MASK entry, the group permissions correspond to the permissions of the ACL_GROUP_OBJ entry. The other permissions correspond to the permissions of the ACL_OTHER entry. </p>
<p> The file owner, group, and other permissions always match the permissions of the corresponding ACL entry. Modification of the file permission bits results in the modification of the associated ACL entries, and modification of these ACL entries results in the modification of the file permission bits.</p>
<h2>OBJECT CREATION AND DEFAULT ACLs The access ACL of a file object is initialized when the object is</h2>
<p>created with any of the Fn creat , Fn mkdir , Fn mknod , Fn mkfifo , or Fn open functions. If a default ACL is associated with a directory, the <i>mode</i> parameter to the functions creating file objects and the default ACL of the directory are used to determine the ACL of the new object: </p>
<ol>
<li> The new object inherits the default ACL of the containing directory as its access ACL.
<li> The access ACL entries corresponding to the file permission bits are modified so that they contain no permissions that are not contained in the permissions specified by the <i>mode</i> parameter. </ol>
<p> If no default ACL is associated with a directory, the <i>mode</i> parameter to the functions creating file objects and the file creation mask (see <a href="/docs/linux/man/2-umask/">umask</a>(2)) are used to determine the ACL of the new object: </p>
<ol>
<li> The new object is assigned an access ACL containing entries of tag types ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER. The permissions of these entries are set to the permissions specified by the file creation mask.
<li> The access ACL entries corresponding to the file permission bits are modified so that they contain no permissions that are not contained in the permissions specified by the <i>mode</i> parameter. </ol>
<h2>Access Check Algorithm</h2>
<p>A process may request read, write, or execute/search access to a file object protected by an ACL. The access check algorithm determines whether access to the object will be granted. </p>
<ol>
<li> <code>If </code>the effective user ID of the process matches the user ID of the file object owner, <code>then</code><br />
<blockquote><p> <code>if</code> the ACL_USER_OBJ entry contains the requested permissions, access is granted, </p>
<p> <code>else</code> access is denied. </p></blockquote>
<li> <code>else if</code> the effective user ID of the process matches the qualifier of any entry of type ACL_USER, <code>then</code><br />
<blockquote><p> <code>if</code> the matching ACL_USER entry and the ACL_MASK entry contain the requested permissions, access is granted, </p>
<p> <code>else</code> access is denied. </p></blockquote>
<li> <code>else if</code> the effective group ID or any of the supplementary group IDs of the process match the file group or the qualifier of any entry of type ACL_GROUP, <code>then</code><br />
<blockquote><p> <code>if</code> the ACL contains an ACL_MASK entry, <code>then</code> </p>
<blockquote><p> <code>if</code> the ACL_MASK entry and any of the matching ACL_GROUP_OBJ or ACL_GROUP entries contain the requested permissions, access is granted, </p>
<p> <code>else</code> access is denied. </p>
</blockquote>
<p> <code>else</code> (note that there can be no ACL_GROUP entries without an ACL_MASK entry) </p>
<blockquote><p> <code>if</code> the ACL_GROUP_OBJ entry contains the requested permissions, access is granted, </p>
<p> <code>else</code> access is denied. </p></blockquote>
</blockquote>
<li> <code>else if</code> the ACL_OTHER entry contains the requested permissions, access is granted.
<li> <code>else</code> access is denied. </ol>
<h2>Acl Text Forms</h2>
<p>A long and a short text form for representing ACLs is defined. In both forms, ACL entries are represented as three colon separated fields: an ACL entry tag type, an ACL entry qualifier, and the discretionary access permissions. The first field contains one of the following entry tag type keywords:</p>
<dl>
<dt><code>user</code></p>
<dd>A <code>user</code> ACL entry specifies the access granted to either the file owner (entry tag type ACL_USER_OBJ) or a specified user (entry tag type ACL_USER).</p>
<dt><code>group</code></p>
<dd>A <code>group</code> ACL entry specifies the access granted to either the file group (entry tag type ACL_GROUP_OBJ) or a specified group (entry tag type ACL_GROUP).</p>
<dt><code>mask</code></p>
<dd>A <code>mask</code> ACL entry specifies the maximum access which can be granted by any ACL entry except the <code>user</code> entry for the file owner and the <code>other</code> entry (entry tag type ACL_MASK).</p>
<dt><code>other</code></p>
<dd>An <code>other</code> ACL entry specifies the access granted to any process that does not match any <code>user</code> or <code>group</code> ACL entries (entry tag type ACL_OTHER).</dl>
<p> The second field contains the user or group identifier of the user or group associated with the ACL entry for entries of entry tag type ACL_USER or ACL_GROUP, and is empty for all other entries. A user identifier can be a user name or a user ID number in decimal form. A group identifier can be a group name or a group ID number in decimal form. </p>
<p> The third field contains the discretionary access permissions. The read, write and search/execute permissions are represented by the <code>r</code> <code>w</code> and <code>x</code> characters, in this order. Each of these characters is replaced by the <code>&#8211;</code> character to denote that a permission is absent in the ACL entry. When converting from the text form to the internal representation, permissions that are absent need not be specified. </p>
<p> White space is permitted at the beginning and end of each ACL entry, and immediately before and after a field separator (the colon character).</p>
<h3>Long Text Form</h3>
<p>The long text form contains one ACL entry per line. In addition, a number sign <code>( #</code> may start a comment that extends until the end of the line. If an ACL_USER, ACL_GROUP_OBJ or ACL_GROUP ACL entry contains permissions that are not also contained in the ACL_MASK entry, the entry is followed by a number sign, the string &#8220;effective:&#8221;, and the effective access permissions defined by that entry. This is an example of the long text form: </p>
<blockquote>
<pre>user::rw-
user:lisa:rw- #effective:r--
group::r--
group:toolies:rw- #effective:r--
mask::r--
other::r--</pre>
</blockquote>
<h3>Short Text Form</h3>
<p>The short text form is a sequence of ACL entries separated by commas, and is used for input. Comments are not supported. Entry tag type keywords may either appear in their full unabbreviated form, or in their single letter abbreviated form. The abbreviation for <code>user</code> is <code>u</code> the abbreviation for <code>group</code> is <code>g</code> the abbreviation for <code>mask</code> is <code>m</code> and the abbreviation for <code>other</code> is <code>o</code> The permissions may contain at most one each of the following characters in any order: <code>r</code> <code>w</code> <code>x</code> These are examples of the short text form: </p>
<blockquote>
<pre>u::rw-,u:lisa:rw-,g::r--,g:toolies:rw-,m::r--,o::r--
g:toolies:rw,u:lisa:rw,u::wr,g::r,o::r,m::r</pre>
</blockquote>
<h2>Rationale</h2>
<p>IEEE 1003.1e draft 17 defines Access Control Lists that include entries of tag type ACL_MASK, and defines a mapping between file permission bits that is not constant. The standard working group defined this relatively complex interface in order to ensure that applications that are compliant with IEEE 1003.1 (&#8220;POSIX.1&#8221;) will still function as expected on systems with ACLs. The IEEE 1003.1e draft 17 contains the rationale for choosing this interface in section B.23.</p>
<h2>Changes To The File Utilities</h2>
<p>On a system that supports ACLs, the file utilities <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-cp/">cp</a>(1), and <a href="/docs/linux/man/1-mv/">mv</a>(1) change their behavior in the following way: </p>
<ul>
<li> For files that have a default ACL or an access ACL that contains more than the three required ACL entries, the <a href="/docs/linux/man/1-ls/">ls</a>(1) utility in the long form produced by <code>ls -l</code> displays a plus sign <code>( +</code> after the permission string.
<li> If the &#8211;<code>p</code> flag is specified, the <a href="/docs/linux/man/1-cp/">cp</a>(1) utility also preserves ACLs. If this is not possible, a warning is produced.
<li>
&nbsp;<wbr>&nbsp;The <a href="/docs/linux/man/1-mv/">mv</a>(1) utility always preserves ACLs. If this is not possible, a warning is produced. </ul>
<p> The effect of the <a href="/docs/linux/man/1-chmod/">chmod</a>(1) utility, and of the <a href="/docs/linux/man/2-chmod/">chmod</a>(2) system call, on the access ACL is described in Sx CORRESPONDENCE BETWEEN ACL ENTRIES AND FILE PERMISSION BITS .</p>
<h2>Standards</h2>
<p>The IEEE 1003.1e draft 17 (&#8220;POSIX.1e&#8221;) document describes several security extensions to the IEEE 1003.1 standard. While the work on 1003.1e has been abandoned, many UNIX style systems implement parts of POSIX.1e draft 17, or of earlier drafts. </p>
<p> Linux Access Control Lists implement the full set of functions and utilities defined for Access Control Lists in POSIX.1e, and several extensions. The implementation is fully compliant with POSIX.1e draft 17; extensions are marked as such. The Access Control List manipulation functions are defined in the ACL library (libacl, -lacl). The POSIX compliant interfaces are declared in the <code>&lt;sys/acl.h&gt;</code> header. Linux-specific extensions to these functions are declared in the <code>&lt;acl/libacl.h&gt;</code> header.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-chmod/">chmod</a>(1), <a href="/docs/linux/man/2-creat/">creat</a>(2), <a href="/docs/linux/man/1-getfacl/">getfacl</a>(1), <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/2-mkdir/">mkdir</a>(2), <a href="/docs/linux/man/2-mkfifo/">mkfifo</a>(2), <a href="/docs/linux/man/2-mknod/">mknod</a>(2), <a href="/docs/linux/man/8-mount/">mount</a>(8), <a href="/docs/linux/man/2-open/">open</a>(2), <a href="/docs/linux/man/1-setfacl/">setfacl</a>(1), <a href="/docs/linux/man/2-stat/">stat</a>(2), <a href="/docs/linux/man/1-umask/">umask</a>(1)</p>
<h3>POSIX 1003.1e DRAFT 17</h3>
<p><a rel="nofollow" href="http://wt.tuxomania.net/publications/posix.1e/download.html">http://wt.tuxomania.net/publications/posix.1e/download.html</a></p>
<h3>POSIX 1003.1e FUNCTIONS BY CATEGORY</h3>
<dl>
<dt><code>ACL storage management</code></p>
<dd>acl_dup3, acl_free3, acl_init3</p>
<dt><code>ACL entry manipulation</code></p>
<dd>acl_copy_entry3, acl_create_entry3, acl_delete_entry3, acl_get_entry3, acl_valid3 </p>
<p> acl_add_perm3, acl_calc_mask3, acl_clear_perms3, acl_delete_perm3, acl_get_permset3, acl_set_permset3 </p>
<p> acl_get_qualifier3, acl_get_tag_type3, acl_set_qualifier3, acl_set_tag_type3</p>
<dt><code>ACL manipulation on an object</code></p>
<dd>acl_delete_def_file3, acl_get_fd3, acl_get_file3, acl_set_fd3, acl_set_file3</p>
<dt><code>ACL format translation</code></p>
<dd>acl_copy_entry3, acl_copy_ext3, acl_from_text3, acl_to_text3, acl_size3</dl>
<h3>POSIX 1003.1e FUNCTIONS BY AVAILABILITY</h3>
<p>The first group of functions is supported on most systems with POSIX-like access control lists, while the second group is supported on fewer systems. For applications that will be ported the second group is best avoided. </p>
<p> acl_delete_def_file3, acl_dup3, acl_free3, acl_from_text3, acl_get_fd3, acl_get_file3, acl_init3, acl_set_fd3, acl_set_file3, acl_to_text3, acl_valid3 </p>
<p> acl_add_perm3, acl_calc_mask3, acl_clear_perms3, acl_copy_entry3, acl_copy_ext3, acl_copy_int3, acl_create_entry3, acl_delete_entry3, acl_delete_perm3, acl_get_entry3, acl_get_permset3, acl_get_qualifier3, acl_get_tag_type3, acl_set_permset3, acl_set_qualifier3, acl_set_tag_type3, acl_size3</p>
<h3>Linux Extensions</h3>
<p>These non-portable extensions are available on Linux systems. </p>
<p> acl_check3, acl_cmp3, acl_entries3, acl_equiv_mode3, acl_error3, acl_extended_fd3, acl_extended_file3, acl_extended_file_nofollow3, acl_from_mode3, acl_get_perm3, acl_to_any_text3</p>
<h2>Author</h2>
<p>Andreas Gruenbacher, &lt;andreas.gruenbacher [at] gmail.com&gt;</p>
