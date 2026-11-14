---
title: "setrichacl(1)"
name: "setrichacl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setrichacl/"
description: "setrichacl – Set Rich Access Control Lists"
---

<h2>NAME</h2>
<p> setrichacl &#8211; Set Rich Access Control Lists</p>
<h2>SYNOPSIS</h2>
<p> <code>setrichacl</code> [<i>option</i>]&#8230; [<i>file</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>setrichacl</code> utility sets or modifies Rich Access Control Lists (RichACLs) of files and directories. </p>
<p> The <code>-m</code> and <code>-s</code> options expect an ACL or parts of an ACL on the command line. The <code>-M</code> and <code>-S</code> options read an ACL or parts of an ACL from a file. In either case, the entry format is described in section <i>Text form</i> of the <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7) manual page. The single-letter or long forms of flags and permissions can be mixed arbitrarily. Multiple entries are separated by whitespace, newlines, or commas. </p>
<p> Note that the order of entries in a RichACL is significant, and that reordering entries may change the permissions granted. </p>
<p> The use of <code>deny</code> entries is discouraged. If <code>deny</code> entries are used, they should be placed ahead of <code>allow</code> entries for improved interoperability with Windows where possible. </p>
<p> When the file masks are not specified, they are computed automatically. </p>
<p> When the ACL to be set is simple enough that the traditional file permission bits can express the same permissions, <code>setrichacl</code> sets the file permission bits and removes the ACL. When <code>setrichacl</code>&#8216;s counterpart utility, <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1), is used on a file or directory that does not have a RichACL, it displays the access permissions defined by the file permission bits as an ACL. This means that for simple ACLs, <code>getrichacl</code> may display a slightly different ACL which is equivalent to the one that was set with <code>setrichacl</code>.</p>
<h3>Permissions</h3>
<p> Setting ACLs or changing the file permission bits is allowed to the file owner, to processes which have the <code>write_acl</code> permission, and to processes which have the <code>CAP_FOWNER</code> capability.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;modify</code> <i>acl</i>, <code>-m</code> <i>acl</i></p>
<dd> Modify the ACL of <i>file</i> by replacing existing entries with the entries in <i>acl</i>, and adding all new entries. When the permissions of an entry are empty, remove the entry.</p>
<dt><code>&#8211;modify-file</code> <i>acl_file</i>, <code>-M</code> <i>acl_file</i></p>
<dd> Identical to <code>&#8211;modify</code>, but read the ACL from <i>acl_file</i> instead. If the file is &#8220;-&#8220;, read from standard input.</p>
<dt><code>&#8211;set</code> <i>acl</i>, <code>-s</code> <i>acl</i></p>
<dd> Set the ACL of <i>file</i> to <i>acl</i>. Any previous ACL is replaced. ACL entries are separated by whitespace, newlines, or commas.</p>
<dt><code>&#8211;set-file</code> <i>acl_file</i>, <code>-S</code> <i>acl_file</i></p>
<dd> Identical to <code>&#8211;set</code>, but read the ACL from <i>acl_file</i> instead. If the file is &#8220;-&#8220;, read from standard input.</p>
<dt><code>&#8211;remove</code>, <code>-b</code></p>
<dd> Remove all extended permissions and revert to the file permission bits only.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Display the version of <code>setrichacl</code> and exit.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Display command-line usage help text.</dl>
<h2>AUTHOR</h2>
<p> Written by Andreas Grünbacher &lt;agruenba [at] redhat.com&gt;. </p>
<p> Please send your bug reports, suggested features and comments to the above address.</p>
<h2>CONFORMING TO</h2>
<p> Rich Access Control Lists are Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getrichacl/">getrichacl</a></code>(1), <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7), <code><a href="/docs/linux/man/7-richaclex/">richaclex</a></code>(7) </p>
<h2>Index</h2>
