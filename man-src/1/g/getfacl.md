---
title: "getfacl(1)"
name: "getfacl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getfacl/"
description: "getfacl – get file access control lists"
---

<h2 class="name">NAME</h2>
<p> getfacl &#8211; get file access control lists </p>
<h2>SYNOPSIS</h2>
<p> <code>getfacl</code> [-aceEsRLPtpndvh] file &#8230; </p>
<p> <code>getfacl</code> [-aceEsRLPtpndvh] &#8211; </p>
<h2>DESCRIPTION</h2>
<p> For each file, getfacl displays the file name, owner, the group, and the Access Control List (ACL). If a directory has a default ACL, getfacl also displays the default ACL. Non-directories cannot have default ACLs. </p>
<p> If getfacl is used on a file system that does not support ACLs, getfacl displays the access permissions defined by the traditional file mode permission bits. </p>
<p> The output format of getfacl is as follows:</p>
<dl>
<dt>
<dd>
<pre>
 1:  # file: somedir/
 2:  # owner: lisa
 3:  # group: staff
 4:  # flags: -s-
 5:  user::rwx
 6:  user:joe:rwx               #effective:r-x
 7:  group::rwx                 #effective:r-x
 8:  group:cool:r-x
 9:  mask::r-x
10:  other::r-x
11:  default:user::rwx
12:  default:user:joe:rwx       #effective:r-x
13:  default:group::r-x
14:  default:mask::r-x
15:  default:other::---
</pre>
</dl>
<p> Lines 1&#8211;3 indicate the file name, owner, and owning group. </p>
<p> Line 4 indicates the setuid (s), setgid (s), and sticky (t) bits: either the letter representing the bit, or else a dash (-). This line is included if any of those bits is set and left out otherwise, so it will not be shown for most files. (See CONFORMANCE TO POSIX 1003.1e DRAFT STANDARD~17 below.) </p>
<p> Lines 5, 7 and 10 correspond to the user, group and other fields of the file mode permission bits. These three are called the base ACL entries. Lines 6 and 8 are named user and named group entries. Line 9 is the effective rights mask. This entry limits the effective rights granted to all groups and to named users. (The file owner and others permissions are not affected by the effective rights mask; all other entries are.) Lines 11&#8211;15 display the default ACL associated with this directory. Directories may have a default ACL. Regular files never have a default ACL. </p>
<p> The default behavior for getfacl is to display both the ACL and the default ACL, and to include an effective rights comment for lines where the rights of the entry differ from the effective rights. </p>
<p> If output is to a terminal, the effective rights comment is aligned to column 40. Otherwise, a single tab character separates the ACL entry and the effective rights comment. </p>
<p> The ACL listings of multiple files are separated by blank lines. The output of getfacl can also be used as input to setfacl. </p>
<h3>PERMISSIONS</h3>
<p> Process with search access to a file (i.e., processes with read access to the containing directory of a file) are also granted read access to the file&#8217;s ACLs. This is analogous to the permissions required for accessing the file mode. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-a, &#8211;access</i></p>
<dd> Display the file access control list.</p>
<dt><i>-d, &#8211;default</i></p>
<dd> Display the default access control list.</p>
<dt><i>-c, &#8211;omit-header</i></p>
<dd> Do not display the comment header (the first three lines of each file&#8217;s output).</p>
<dt><i>-e, &#8211;all-effective</i></p>
<dd> Print all effective rights comments, even if identical to the rights defined by the ACL entry.</p>
<dt><i>-E, &#8211;no-effective</i></p>
<dd> Do not print effective rights comments.</p>
<dt><i>-s, &#8211;skip-base</i></p>
<dd> Skip files that only have the base ACL entries (owner, group, others).</p>
<dt><i>-R, &#8211;recursive</i></p>
<dd> List the ACLs of all files and directories recursively.</p>
<dt><i>-L, &#8211;logical</i></p>
<dd> Logical walk, follow symbolic links to directories. The default behavior is to follow symbolic link arguments, and skip symbolic links encountered in subdirectories. Only effective in combination with -R.</p>
<dt><i>-P, &#8211;physical</i></p>
<dd> Physical walk, do not follow symbolic links to directories. This also skips symbolic link arguments. Only effective in combination with -R.</p>
<dt><i>-t, &#8211;tabular</i></p>
<dd> Use an alternative tabular output format. The ACL and the default ACL are displayed side by side. Permissions that are ineffective due to the ACL mask entry are displayed capitalized. The entry tag names for the ACL_USER_OBJ and ACL_GROUP_OBJ entries are also displayed in capital letters, which helps in spotting those entries.</p>
<dt><i>-p, &#8211;absolute-names</i></p>
<dd> Do not strip leading slash characters (`/&#8217;). The default behavior is to strip leading slash characters.</p>
<dt><i>-n, &#8211;numeric</i></p>
<dd> List numeric user and group IDs</p>
<dt><i>-v, &#8211;version</i></p>
<dd> Print the version of getfacl and exit.</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Print help explaining the command line options.</p>
<dt><i>&#8212;</i></p>
<dd> End of command line options. All remaining parameters are interpreted as file names, even if they start with a dash character.</p>
<dt><i>&#8211;</i></p>
<dd> If the file name parameter is a single dash character, getfacl reads a list of files from standard input. </p>
</dl>
<h2>CONFORMANCE TO POSIX 1003.1e DRAFT STANDARD 17</h2>
<p> If the environment variable POSIXLY_CORRECT is defined, the default behavior of getfacl changes in the following ways: Unless otherwise specified, only the ACL is printed. The default ACL is only printed if the <i>-d</i> option is given. If no command line parameter is given, <i>getfacl</i> behaves as if it was invoked as &#8220;getfacl -&#8221;. No flags comments indicating the setuid, setgid, and sticky bits are generated.</p>
<h2>AUTHOR</h2>
<p> Andreas Gruenbacher, &lt;<i>andreas.gruenbacher [at] gmail.com</i>&gt;. </p>
<p> Please send your bug reports and comments to the above address.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setfacl/">setfacl</a></code>(1), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) </p>
<h2>Index</h2>
