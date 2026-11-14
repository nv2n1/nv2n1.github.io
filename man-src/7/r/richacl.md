---
title: "richacl(7)"
name: "richacl"
section: "7"
letter: "r"
url: "/docs/linux/man/7-richacl/"
description: "richacl – Rich Access Control Lists"
---

<p>richacl &#8211; Rich Access Control Lists</p>
<h2>Description</h2>
<p>Rich Access Control Lists (RichACLs) are an extension of the traditional POSIX file permission model to support NFSv4 Access Control Lists &lt;URL: <a rel="nofollow" href="https://tools.ietf.org/rfc/rfc5661.txt">https://tools.ietf.org/rfc/rfc5661.txt</a> &gt; on local and remote-mounted filesystems. </p>
<p> A RichACL can always be translated into an equivalent NFSv4 ACL which grants the same permissions. </p>
<p> RichACLs can be enabled on supported local filesystems (currently, ext4 and XFS). The in-kernel NFSv4 server and client also include RichACL support. </p>
<p> Enabling RichACLs disables POSIX Access Control Lists; the two ACL models cannot coexist on the same filesystem. </p>
<p> When used on a filesystem that does not support RichACLs, the <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1) and <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1) utilities will operate on the file permission bits instead: <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1) will display the file permission bits as a RichACL; when a RichACL is set with <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1) which can be represented exactly by the file permission bits, <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1) will set the file permission bits instead. An attempt to set a RichACL that cannot be represented exactly by the file permission bits results in an error. </p>
<p> This man-page describes the structure, concepts and algorithms involved in RichACLs. For examples, please refer to <code><a href="/docs/linux/man/7-richaclex/">richaclex</a></code>(7).</p>
<h3>Structure of RichACLs</h3>
<p>RichACLs consist of a number of ACL entries, three file masks, and a set of flags specifying attributes of the ACL as a whole (by contrast with the per-ACL-entry flags described below). </p>
<p> Each of the ACL entries allows or denies some permissions to a particular user, group, or special identifier. An ACL entry consists of four fields:</p>
<dl>
<dt>&bull;</p>
<dd>A tag which specifies the user, group, or special identifier the entry applies to. Special identifiers can be the file owner (<code>owner@</code>), the owning group (<code>group@</code>), or everyone (<code>everyone@</code>).</p>
<dt>&bull;</p>
<dd>A set of permissions the entry allows or denies.</p>
<dt>&bull;</p>
<dd>A set of flags that indicate whether the user or group identifier is mapped or unmapped, and whether the entry has been and can be inherited.</p>
<dt>&bull;</p>
<dd>A type field indicating whether the entry allows or denies the permissions specified in the second field.</dl>
<p> The owner, group, and other file masks further control which permissions the ACL grants, subject to the <code>masked</code>&nbsp;<wbr>(<code>m</code>) and <code>write_through</code>&nbsp;<wbr>(<code>w</code>) ACL flags: when the permissions of a file or directory are changed with <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), the file masks are set based on the new file mode, and the <code>masked</code> and <code>write_through</code> ACL flags are set. Likewise, when a new file or directory inherits an ACL from its parent directory, the file masks are set to the intersection between the permissions granted by the inherited ACL and the <i>mode</i> parameter as given to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), and similar, and the <code>masked</code> ACL flag is set. In both cases, the file masks limit the permissions that the ACL will grant. </p>
<p> The purpose of the file masks is to allow traditional POSIX applications which are unaware of RichACLs to place limits on the permissions granted by the RichACL without causing the ACL entries to be modified. Without the file mask, the only alternative would be for the kernel to directly modify the ACL entries. However, this latter approach could have a &#8220;hysteresis effect&#8221;, whereby a RichACL-unaware application that performs a transition from one file mode to another file mode and then back to the original file mode could cause destruction of the permission information in ACL entries. When creating files or directories, the <i>mode</i> parameter to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), and similar would have the same effect. </p>
<p> Note that entries with the identifier <code>everyone@</code> apply to all processes, whereas the &#8220;other&#8221; file permissions and &#8220;other&#8221; (<code>ACL_OTHER</code>) entries in POSIX ACLs apply to all processes which are not the owner, are not in the owning group, and do not match a user or group mentioned in the ACL. </p>
<p> Unlike POSIX ACLs, RichACLs do not have separate &#8220;access&#8221; ACLs that define the access permissions and &#8220;default&#8221; ACLs that define the inheritable permissions. Instead, flags on each ACL entry determine whether the entry is effective during access checks and/or inheritable.</p>
<h3>ACL flags</h3>
<p>The following ACL flags are defined:</p>
<dl>
<dt><code>masked</code>&nbsp;<wbr>(<code>m</code>)</p>
<dd>When set, the file masks define upper limits on the permissions the ACL may grant. When not set, the file masks are ignored.</p>
<dt><code>write_through</code>&nbsp;<wbr>(<code>w</code>)</p>
<dd>When this flag and the <code>masked</code> flag are both set, the owner and other file masks define the actual permissions granted to the file owner and to others instead of defining an upper limit. When the <code>masked</code> flag is not set, the <code>write_through</code> flag has no effect.</p>
<dt><code>auto_inherit</code>&nbsp;<wbr>(<code>a</code>)</p>
<dd>Automatic Inheritance is enabled. See <i>Automatic Inheritance</i>.</p>
<dt><code>protected</code>&nbsp;<wbr>(<code>p</code>)</p>
<dd>The ACL is protected from modification by Automatic Inheritance.</p>
<dt><code>defaulted</code>&nbsp;<wbr>(<code>d</code>)</p>
<dd>Indicates that the ACL has been assigned in an application-dependent way when the file or directory was created; it has neither been inherited nor set explicitly. ACLs of files created on Linux will never have the <code>defaulted</code> flag set, but the flag may be set on files created on or copied over from other operating systems. When this flag is set for an ACL, Automatic Inheritance will completely replace the ACL.</dl>
<h3>ACL entry flags</h3>
<p>The following flags on ACL entries are defined:</p>
<dl>
<dt><code>file_inherit</code>&nbsp;<wbr>(<code>f</code>)</p>
<dd>When this flag appears in the ACL entry of a directory, then:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>That entry is inherited by new files created in the directory such that the permissions of the entry apply to the file (the inheritance flags of the inherited entry are cleared).</p>
<dt>&bull;</p>
<dd>The entry is is inherited by new subdirectories created in the directory such that the permissions of the entry will apply to new files created in the subdirectory.</dl>
</dl>
<dt><code>dir_inherit</code>&nbsp;<wbr>(<code>d</code>)</p>
<dd>When this flag appears in the ACL entry of a directory, then that entry is inherited by new subdirectories created in the directory such that the permissions of the entry apply to the subdirectory (the <code>inherit_only</code> flag is cleared).</p>
<dt><code>no_propagate</code>&nbsp;<wbr>(<code>n</code>)</p>
<dd>Inheritance stops at the next subdirectory level. When a file or directory inherits an entry that has this flag set, the <code>file_inherit</code>, <code>dir_inherit</code>, <code>no_propagate</code>, and <code>inherit_only</code> flags are cleared.</p>
<dt><code>inherit_only</code>&nbsp;<wbr>(<code>i</code>)</p>
<dd>The entry defines inheritable permissions only and is ignored for access checking. When a file or directory inherits an entry that has this flag set, the flag is cleared.</p>
<dt><code>inherited</code>&nbsp;<wbr>(<code>a</code>)</p>
<dd>The entry has been automatically inherited from the parent directory.</p>
<dt><code>unmapped</code>&nbsp;<wbr>(<code>u</code>)</p>
<dd>The user or group identifier is a textual string and is not mapped to a numeric user or group identifier. ACLs with unmapped identifiers can occur on NFSv4 mounted filesystems when the client cannot determine numeric user or group identifiers for some of the NFSv4 user [at] domain or group [at] domain who values. They cannot be assigned to local files or directories.</dl>
<h3>Permissions</h3>
<p>The following permissions are defined for RichACL entries and for the three file masks:</p>
<dl>
<dt><code>read_data</code> / <code>list_directory</code>&nbsp;<wbr>(<code>r</code>)</p>
<dd>For a file: read the data of the file. For a directory: list the contents of the directory.</p>
<dt><code>write_data</code> / <code>add_file</code>&nbsp;<wbr>(<code>w</code>)</p>
<dd>For a file: modify the data of the file; does not include opening the file in append mode. For a directory: add a new file in the directory.</p>
<dt><code>append_data</code> / <code>add_subdirectory</code>&nbsp;<wbr>(<code>p</code>)</p>
<dd>For a file: open the file in append mode. For a directory: create a subdirectory in the directory.</p>
<dt><code>execute</code>&nbsp;<wbr>(<code>x</code>)</p>
<dd>For a file: execute the file. For a directory: traverse (search) the directory.</p>
<dt><code>delete_child</code>&nbsp;<wbr>(<code>d</code>)</p>
<dd>Delete a file or directory within a directory. This permission is meaningful only for directories.</p>
<dt><code>delete</code>&nbsp;<wbr>(<code>D</code>)</p>
<dd>Delete the file or directory.</p>
<dt><code>read_attributes</code>&nbsp;<wbr>(<code>a</code>)</p>
<dd>Read basic attributes of a file or directory (see <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)). This permission is defined by NFSv4. It is stored, but ignored. Reading basic attributes of files and directories is always allowed on Linux.</p>
<dt><code>write_attributes</code>&nbsp;<wbr>(<code>A</code>)</p>
<dd>Change the times associated with a file or directory to an arbitrary value. This permission is always implicitly granted to the file owner.</p>
<dt><code>read_acl</code>&nbsp;<wbr>(<code>c</code>)</p>
<dd>Read the ACL of a file or directory. Like reading the basic file attributes (the <code>read_attributes</code> permission), reading ACLs is always allowed on Linux.</p>
<dt><code>write_acl</code>&nbsp;<wbr>(<code>C</code>)</p>
<dd>Change the ACL or file mode of a file or directory.</p>
<dt><code>write_owner</code>&nbsp;<wbr>(<code>o</code>)</p>
<dd>Take ownership of a file or directory. Change the owning group of a file or directory to a group of which the calling process is a member.</p>
<dd><code>read_named_attrs</code>&nbsp;<wbr>(<code>R</code>), <code>write_named_attrs</code>&nbsp;<wbr>(<code>W</code>), <code>synchronize</code>&nbsp;<wbr>(<code>S</code>), <code>write_retention</code>&nbsp;<wbr>(<code>e</code>), <code>write_retention_hold</code>&nbsp;<wbr>(<code>E</code>) These permissions are defined by NFSv4 and NFSv4.1. They are stored, but ignored.</dl>
<p> For the <code>r</code>, <code>w</code>, and <code>p</code> permissions, which have different long forms for files and directories, the <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1) utility will output the appropriate form(s) depending on the context. The <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1) utility will accept either form for any file type.</p>
<h3>Text form</h3>
<p>The common textual representation of a RichACL consists of the colon-separated fields of the ACL flags, file masks, and ACL entries in the following format:</p>
<dl>
<dt><code>flags:</code><i>acl_flags</i></p>
<dd>The ACL flags.</p>
<dt><code>owner:</code><i>perm</i><code>::mask</code>, <code>group:</code><i>perm</i><code>::mask</code>, <code>other:</code><i>perm</i><code>::mask</code></p>
<dd>The file masks and their permissions.</p>
<dt><i>who</i><code>:</code><i>perm</i><code>:</code><i>flags</i><code>:allow</code>, <i>who</i><code>:</code><i>perm</i><code>:</code><i>flags</i><code>:deny</code></p>
<dd>For each ACL entry, who the entry applies to, the permissions of the entry, the entry flags, and the entry type. The <i>who</i> field is one of the following:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>One of the special identifiers: <code>owner@</code>, <code>group@</code>, or <code>everyone@</code>,</p>
<dt>&bull;</p>
<dd>A <code>user:</code> or <code>u:</code> prefix followed by a user name or user ID that designates a specific user,</p>
<dt>&bull;</p>
<dd>A <code>group:</code> or <code>g:</code> prefix followed by a group name or group ID that designates a specific group.</dl>
</dl>
</dl>
<p> The ACL flags, file masks, and ACL entries are comma, whitespace, or newline separated. </p>
<p> Flags and permissions have single-letter as well as long forms, as listed under <i>ACL flags</i>, <i>ACL entry flags</i>, and <i>Permissions</i>. When the single-letter forms are used, the flags or permissions are concatenated. When the long forms are used, the flags or permissions are separated by slashes. To align permissions or flags vertically, dashes can be used for padding.</p>
<h3>Setting and modifying file permissions</h3>
<p>The access permissions for a file can either be set by assigning an Access Control List (<code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1)) or by changing the file mode permission bits (<code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1)). In addition, a file can inherit an ACL from its parent directory at creation time as described under <i>Permissions at file-creation time</i>.</p>
<h3>Assigning an Access Control List</h3>
<p>When assigning an ACL to a file, unless explicitly specified, the owner, group, and other file masks will be computed from the ACL entries as described in the section <i>Computing the maximum file masks</i>. The owner, group, and other file mode permission bits are then each set from the owner, group, and other file mask as follows:</p>
<dl>
<dt>&bull;</p>
<dd>If the file mask includes the <code>r</code> permission, the read file mode permission bit will be set.</p>
<dt>&bull;</p>
<dd>If the file mask includes the <code>w</code> or <code>p</code> permission, the write file mode permission bit will be set.</p>
<dt>&bull;</p>
<dd>If the file mask includes the <code>x</code> permission, the execute file mode permission bit will be set.</dl>
<p> If the ACL can be represented exactly by the file mode permission bits, the file permission bits are set to match the ACL and no ACL is stored. (When the ACL of a file is requested which doesn&#8217;t have an ACL, the file mode permission bits are converted into an equivalent ACL.)</p>
<h3>Changing the file mode permission bits</h3>
<p>When changing the file mode permission bits with <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), the owner, group, and other file permission bits are set to the permission bits in the new mode, and the owner, group, and other file masks are set based on the new mode bits as follows:</p>
<dl>
<dt>&bull;</p>
<dd>If the read bit in a set of permissions is set, the <code>r</code> permission in the corresponding file mask will be set.</p>
<dt>&bull;</p>
<dd>If the write bit in a set of permissions is set, the <code>w</code> and <code>p</code> permissions in the corresponding file mask will be set.</p>
<dt>&bull;</p>
<dd>If the execute bit in a set of permissions is set, the <code>x</code> permission in the corresponding file mask will be set.</dl>
<p> In addition, the <code>masked</code> and <code>write_through</code> ACL flags are set. This has the effect of limiting the permissions granted by the ACL to the file mode permission bits; in addition, the owner is granted the owner mode bits and others are granted the other mode bits. If the <code>auto_inherit</code> flag is set, the <code>protected</code> flag is also set to prevent the Automatic Inheritance algorithm from modifying the ACL.</p>
<h3>Permissions at file-creation time</h3>
<p>When a directory has any inheritable ACL entries, the following happens when a file or directory is created inside that directory:</p>
<dl>
<dt>1.</p>
<dd>A file created inside that directory will inherit all of the ACL entries that have the <code>file_inherit</code> flag set, and all inheritance-related flags in the inherited entries flag will be cleared.</p>
<dl>
<dd>A subdirectory created inside that directory will inherit all of the ACL entries that either have the <code>dir_inherit</code> flag set, or the <code>file_inherit</code> flag set and the <code>no_propagate</code> flag not set. Entries whose <code>dir_inherit</code> flag is set will have their <code>inherit_only</code> flag cleared, and entries whose <code>dir_inherit</code> flag is not set will have their <code>inherit_only</code> flag set. Finally, entries whose <code>no_propagate</code> flag is set will have all inheritance-related flags cleared.</dl>
<dt>2.</p>
<dd>If the parent directory&#8217;s ACL has the <code>auto_inherit</code> flag set, then the inherited ACL will have its <code>auto_inherit</code> flag set, and all entries will have their <code>inherited</code> flag set. Otherwise, the <code>auto_inherit</code> and <code>inherited</code> flags are cleared.</p>
<dt>3.</p>
<dd>The three file masks are computed from the inherited ACL as described in the section <i>Computing the maximum file masks</i>.</p>
<dt>4.</p>
<dd>The three sets of permissions for the owner, the group, and for others in the <i>mode</i> parameter as given to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), and similar are converted into sets of RichACL permissions. The correspondence between mask flags and RichACL permission bits is described in the section <i>Changing the file mode permission bits</i>. Any RichACL permissions not included in those sets are removed from the owner, group, and other file masks. The file mode permission bits are then computed from the file masks as described in the section <i>Assigning an Access Control List</i>. The process umask (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)) is ignored.</p>
<dt>5.</p>
<dd>The <code>masked</code> ACL flag is set. The <code>write_through</code> ACL flag remains cleared. In addition, if the <code>auto_inherit</code> flag of the inherited ACL is set, the <code>protected</code> flag is also set to prevent the Automatic Inheritance algorithm from modifying the ACL.</dl>
<p> When a directory does not have inheritable ACL entries, files and directories created inside that directory will not be assigned Access Control Lists and the file mode permission bits will be set to (<i>mode</i>&nbsp;<wbr>&amp;&nbsp;<wbr>~<i>umask</i>) where <i>mode</i> is the mode argument of the relevant system call and <i>umask</i> is the process umask (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)).</p>
<h3>Automatic Inheritance</h3>
<p>Automatic Inheritance is a mechanism that allows permission changes to propagate from a directory to files and subdirectories inside that directory, recursively. Propagation is carried out by the process changing the directory permissions (usually, <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1)); it happens without user intervention albeit not entirely automatically. </p>
<p> A significant limitation of the Automatic Inheritance feature is that this mechanism works only as long as files are created without explicitly specifying the file permissions to use. The standard system calls for creating files and directories (<code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), and so on) all have mandatory mode parameters which define the maximum allowed permissions of the new files. To take account of this restriction, the <code>protected</code> ACL flag must be set if the <code>inherited</code> flag is set. This effectively disables Automatic Inheritance for that particular file. </p>
<p> Notwithstanding the aforementioned limitation, Automatic Inheritance still remains useful for network protocols like NFSv4 and SMB, which both support creating files and directories without defining their permissions. These protocols can implement those operations by using the standard system calls and by then undoing the effect of applying the mode parameters. </p>
<p> When the ACL of a directory is changed, the following happens for each entry (&#8220;child&#8221;) inside that directory:</p>
<dl>
<dt>1.</p>
<dd>If the entry is a symbolic link, skip the child.</p>
<dt>2.</p>
<dd>If the <code>auto_inherit</code> flag of the entry&#8217;s ACL is not set or the <code>protected</code> flag is set, skip the child.</p>
<dt>3.</p>
<dd>With the child&#8217;s ACL:</p>
<dl>
<dd>
<dl>
<dt>a)</p>
<dd>If the <code>defaulted</code> flag is set, replace the ACL with an empty ACL with the <code>auto_inherit</code> flag set.</p>
<dt>b)</p>
<dd>Delete all entries which have the <code>inherited</code> flag set.</p>
<dt>c)</p>
<dd>Append all entries inherited from the parent directory according to step 1 of the algorithm described under <i>Permissions at file-creation time.</i> Set the <code>inherited</code> flag of each of these entries.</p>
<dt>d)</p>
<dd>Recompute the file masks as decribed in the section <i>Computing the maximum file masks</i>.</dl>
</dl>
<dt>4.</p>
<dd>If the child is a directory, recursively apply this algorithm.</dl>
<h3>Access check algorithm</h3>
<p>When a process requests a particular kind of access (expressed as a set of RichACL permissions) to a file, the following algorithm determines whether the access is granted or denied:</p>
<dl>
<dt>1.</p>
<dd>If the <code>masked</code> ACL flag is set, then:</p>
<dl>
<dd>
<dl>
<dt>a)</p>
<dd>If the <code>write_through</code> ACL flag is set, then:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the requesting process is the file owner, then access is granted if the owner mask includes the requested permissions, and is otherwise denied.</p>
<dt>&bull;</p>
<dd>If the requesting process is not the file owner and it is in the owning group or matches any ACL entries other than <code>everyone@</code>, proceed to step b).</p>
<dt>&bull;</p>
<dd>If the requesting process is not the file owner, is not in the owning group, and no ACL entries other than <code>everyone@</code> match the process, then access is granted if the other mask includes the requested permissions, and is otherwise denied.</dl>
</dl>
<dt>b)</p>
<dd>If any of the following is true:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>the requesting process is the file owner and the owner mask does not include all requested permissions,</p>
<dt>&bull;</p>
<dd>the requesting process is not the file owner and it is in the owning group or matches any ACL entries other than <code>everyone@</code>, and the group mask does not include all requested permissions,</p>
<dt>&bull;</p>
<dd>the requesting process is not the file owner, not in the owning group, it matches no ACL entries other than <code>everyone@</code>, and the other mask does not include all requested permissions,</dl>
<p> then access is denied.</dl>
</dl>
</dl>
<dt>2.</p>
<dd>Upon reaching this point, the determination of whether or not access is granted is made by scanning all ACL entries to see if one or more applicable entries together grant a cumulative set of permissions that matches the requested permissions or there is an applicable entry that explicitly denies one or more of the requested permissions. The scan of all ACL entries begins by first initializing the set of remaining permissions (i.e., those that have not yet been satisfied during the scan) to be the set of requested permissions. Then the ACL entries are scanned <i>in order</i>, and for each entry:</p>
<dl>
<dd>
<dl>
<dt>a)</p>
<dd>If the <code>inherit_only</code> or <code>unmapped</code> flags are set, continue with the next ACL entry.</p>
<dt>b)</p>
<dd>If any of the following is true:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>the entry&#8217;s identifier is <code>owner@</code> and the requesting process is the file owner,</p>
<dt>&bull;</p>
<dd>the entry&#8217;s identifier is <code>group@</code> and the requesting process is in the owning group,</p>
<dt>&bull;</p>
<dd>the entry&#8217;s identifier is a user and the requesting process is owned by that user,</p>
<dt>&bull;</p>
<dd>the entry&#8217;s identifier is a group and the requesting process is a member in that group,</p>
<dt>&bull;</p>
<dd>the entry&#8217;s identifier is <code>everyone@</code>,</dl>
<p> then the entry matches the process; proceed to the next step. Otherwise, continue with the next ACL entry.</dl>
<dt>c)</p>
<dd>If the entry denies any of the remaining permissions, access is denied.</p>
<dt>d)</p>
<dd>If the entry allows any of the remaining permissions, then:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the <code>masked</code> ACL flag is set and the entry&#8217;s identifier is not <code>owner@</code> or <code>everyone@</code> or is a user entry matching the file owner, remove all permissions from the remaining permissions which are both allowed by the entry and included in the group mask,</p>
<dt>&bull;</p>
<dd>Otherwise, remove all permissions from the remaining permissions which are allowed by the entry.</dl>
</dl>
</dl>
</dl>
<dt>3.</p>
<dd>If there are no more remaining permissions, access is allowed. Otherwise, access is denied.</dl>
<p> In this algorithm, a process can gain the permissions it requires by accumulating them from multiple RichACL entries. This is in contrast with POSIX ACLs, where access is only granted if an ACL entry exists that matches the requesting process and includes all the requested permissions.</p>
<h3>Computing the maximum file masks</h3>
<p>When setting an ACL and no file masks have been explicitly specified and when inheriting an ACL from the parent directory (as described in the section <i>Permissions at file-creation time</i>), the following algorithm is used for computing the file masks:</p>
<dl>
<dt>1.</p>
<dd>Clear the owner, group, and other file masks. Remember which permissions have already been processed (initially, the empty set).</p>
<dt>2.</p>
<dd>For each ACL entry:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the <code>inherit_only</code> flag is set, skip the entry.</p>
<dt>&bull;</p>
<dd>Otherwise, compute which permissions the entry allows or denies that have not been processed yet (the remaining permissions).</p>
<dt>&bull;</p>
<dd>If the entry is an <code>owner@</code> entry, add the remaining permissions to the owner mask for <code>allow</code> entries, and remove the remaining permissions from the owner mask for <code>deny</code> entries.</p>
<dt>&bull;</p>
<dd>Otherwise, if the entry is an <code>everyone@</code> entry, proceed as with <code>owner@</code> entries but add or remove the remaining permissions from the owner, group, and other file masks.</p>
<dt>&bull;</p>
<dd>Otherwise, proceed as with <code>owner@</code> entries but add or remove the remaining permissions from the owner and group file masks.</p>
<dt>&bull;</p>
<dd>Add the entry&#8217;s permissions to the processed permissions.</dl>
</dl>
</dl>
<p> The resulting file masks represent the ACL as closely as possible. With these file masks, the effective permissions that the ACL grants will be the same when the <code>masked</code> flag is set as when it is not set.</p>
<h2>Author</h2>
<p>Written by Andreas Grünbacher &lt;agruenba [at] redhat.com&gt;. </p>
<p> Please send your bug reports, suggested features and comments to the above address.</p>
<h2>Conforming To</h2>
<p>Rich Access Control Lists are Linux-specific.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-richaclex/">richaclex</a></code>(7), <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1) <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) </p>
