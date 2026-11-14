---
title: "xattr(7)"
name: "xattr"
section: "7"
letter: "x"
url: "/docs/linux/man/7-xattr/"
description: "xattr – Extended attributes"
---

<p>xattr &#8211; Extended attributes</p>
<h2>Description</h2>
<p>Extended attributes are name:value pairs associated permanently with files and directories, similar to the environment strings associated with a process. An attribute may be defined or undefined. If it is defined, its value may be empty or non-empty. </p>
<p> Extended attributes are extensions to the normal attributes which are associated with all inodes in the system (i.e., the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) data). They are often used to provide additional functionality to a filesystem&#8212;for example, additional security features such as Access Control Lists (ACLs) may be implemented using extended attributes. </p>
<p> Users with search access to a file or directory may use <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2) to retrieve a list of attribute names defined for that file or directory. </p>
<p> Extended attributes are accessed as atomic objects. Reading (<code><a href="/docs/linux/man/2-getxattr/">getxattr</a></code>(2)) retrieves the whole value of an attribute and stores it in a buffer. Writing (<code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2)) replaces any previous value with the new value. </p>
<p> Space consumed for extended attributes may be counted towards the disk quotas of the file owner and file group.</p>
<h3>Extended attribute namespaces</h3>
<p>Attribute names are null-terminated strings. The attribute name is always specified in the fully qualified <i>namespace.attribute</i> form, for example, <i>user.mime_type</i>, <i>trusted.md5sum</i>, <i>system.posix_acl_access</i>, or <i>security.selinux</i>. </p>
<p> The namespace mechanism is used to define different classes of extended attributes. These different classes exist for several reasons; for example, the permissions and capabilities required for manipulating extended attributes of one namespace may differ to another. </p>
<p> Currently, the <i>security</i>, <i>system</i>, <i>trusted</i>, and <i>user</i> extended attribute classes are defined as described below. Additional classes may be added in the future.</p>
<h3>Extended security attributes</h3>
<p>The security attribute namespace is used by kernel security modules, such as Security Enhanced Linux, and also to implement file capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). Read and write access permissions to security attributes depend on the policy implemented for each security attribute by the security module. When no security module is loaded, all processes have read access to extended security attributes, and write access is limited to processes that have the <code>CAP_SYS_ADMIN</code> capability.</p>
<h3>System extended attributes</h3>
<p>System extended attributes are used by the kernel to store system objects such as Access Control Lists. Read and write access permissions to system attributes depend on the policy implemented for each system attribute implemented by filesystems in the kernel.</p>
<h3>Trusted extended attributes</h3>
<p>Trusted extended attributes are visible and accessible only to processes that have the <code>CAP_SYS_ADMIN</code> capability. Attributes in this class are used to implement mechanisms in user space (i.e., outside the kernel) which keep information in extended attributes to which ordinary processes should not have access.</p>
<h3>User extended attributes</h3>
<p>User extended attributes may be assigned to files and directories for storing arbitrary additional information such as the mime type, character set or encoding of a file. The access permissions for user attributes are defined by the file permission bits: read permission is required to retrieve the attribute value, and writer permission is required to change it. </p>
<p> The file permission bits of regular files and directories are interpreted differently from the file permission bits of special files and symbolic links. For regular files and directories the file permission bits define access to the file&#8217;s contents, while for device special files they define access to the device described by the special file. The file permissions of symbolic links are not used in access checks. These differences would allow users to consume filesystem resources in a way not controllable by disk quotas for group or world writable special files and directories. </p>
<p> For this reason, user extended attributes are allowed only for regular files and directories, and access to user extended attributes is restricted to the owner and to users with appropriate capabilities for directories with the sticky bit set (see the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) manual page for an explanation of the sticky bit).</p>
<h3>Filesystem differences</h3>
<p>The kernel and the filesystem may place limits on the maximum number and size of extended attributes that can be associated with a file. The VFS imposes limitations that an attribute names is limited to 255 bytes and an attribute value is limited to 64 kB. The list of attribute names that can be returned is also limited to 64 kB (see BUGS in <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2)). </p>
<p> Some filesystems, such as Reiserfs (and, historically, ext2 and ext3), require the filesystem to be mounted with the <code>user_xattr</code> mount option in order for user extended attributes to be used. </p>
<p> In the current ext2, ext3, and ext4 filesystem implementations, the total bytes used by the names and values of all of a file&#8217;s extended attributes must fit in a single filesystem block (1024, 2048 or 4096 bytes, depending on the block size specified when the filesystem was created). </p>
<p> In the Btrfs, XFS, and Reiserfs filesystem implementations, there is no practical limit on the number of extended attributes associated with a file, and the algorithms used to store extended attribute information on disk are scalable. </p>
<p> In the JFS, XFS, and Reiserfs filesystem implementations, the limit on bytes used in an EA value is the ceiling imposed by the VFS. </p>
<p> In the Btrfs filesystem implementation, the total bytes used for the name, value, and implementation overhead bytes is limited to the filesystem <i>nodesize</i> value (16 kB by default).</p>
<h2>Conforming To</h2>
<p>Extended attributes are not specified in POSIX.1, but some other systems (e.g., the BSDs and Solaris) provide a similar feature.</p>
<h2>Notes</h2>
<p>Since the filesystems on which extended attributes are stored might also be used on architectures with a different byte order and machine word size, care should be taken to store attribute values in an architecture-independent format. </p>
<p> This page was formerly named <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-attr/">attr</a></code>(1), <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1), <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), <code><a href="/docs/linux/man/2-getxattr/">getxattr</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2), <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2), <code><a href="/docs/linux/man/2-removexattr/">removexattr</a></code>(2), <code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
