---
title: "chacl(1)"
name: "chacl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chacl/"
description: "chacl – change the access control list of a file or directory"
---

<h2 class="name">NAME</h2>
<p> chacl &#8211; change the access control list of a file or directory </p>
<h2>SYNOPSIS</h2>
<p> <code>chacl acl pathname&#8230;</code><br />
 <code>chacl -b acl dacl pathname&#8230;</code><br />
 <code>chacl -d dacl pathname&#8230;</code><br />
 <code>chacl -R pathname&#8230;</code><br />
 <code>chacl -D pathname&#8230;</code><br />
 <code>chacl -B pathname&#8230;</code><br />
 <code>chacl -l pathname&#8230;</code><br />
 <code>chacl -r pathname&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>chacl</i> is an IRIX-compatibility command, and is maintained for those users who are familiar with its use from either XFS or IRIX. Refer to the <code>SEE ALSO</code> section below for a description of tools which conform more closely to the (withdrawn draft) POSIX 1003.1e standard which describes Access Control Lists (ACLs). </p>
<p> <i>chacl</i> changes the ACL(s) for a file or directory. The ACL(s) specified are applied to each file in the <tt>pathname</tt> arguments. </p>
<p> Each ACL is a string which is interpreted using the <i><a href="/docs/linux/man/3-acl_from_text/">acl_from_text</a></i>(3) routine. These strings are made up of comma separated clauses each of which is of the form, tag:name:perm. Where <tt>tag</tt> can be:</p>
<dl>
<dt>&quot;user&quot; (or &quot;u&quot;)</p>
<dd> indicating that the entry is a &quot;user&quot; ACL entry.</p>
<dt>&quot;group&quot; (or &quot;g&quot;)</p>
<dd> indicating that the entry is a &quot;group&quot; ACL entry.</p>
<dt>&quot;other&quot; (or &quot;o&quot;)</p>
<dd> indicating that the entry is an &quot;other&quot; ACL entry.</p>
<dt>&quot;mask&quot; (or &quot;m&quot;)</p>
<dd> indicating that the entry is a &quot;mask&quot; ACL entry.</dl>
<p> <tt>name</tt> is a string which is the user or group name for the ACL entry. A null <tt>name</tt> in a user or group ACL entry indicates the file&#8217;s owner or file&#8217;s group. <tt>perm</tt> is the string &quot;rwx&quot; where each of the entries may be replaced by a &quot;-&quot; indicating no access of that type, e.g. &quot;r-x&quot;, &quot;&#8211;x&quot;, &quot;&#8212;&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Indicates that there are two ACLs to change, the first is the file access ACL and the second the directory default ACL.</p>
<dt><code>-d</code></p>
<dd> Used to set only the default ACL of a directory.</p>
<dt><code>-R</code></p>
<dd> Removes the file access ACL only.</p>
<dt><code>-D</code></p>
<dd> Removes directory default ACL only.</p>
<dt><code>-B</code></p>
<dd> Remove all ACLs.</p>
<dt><code>-l</code></p>
<dd> Lists the access ACL and possibly the default ACL associated with the specified files or directories. This option was added during the Linux port of XFS, and is not IRIX compatible.</p>
<dt><code>-r</code></p>
<dd> Set the access ACL recursively for each subtree rooted at <tt>pathname</tt>(s). This option was also added during the Linux port of XFS, and is not compatible with IRIX.</dl>
<h2>EXAMPLES</h2>
<p> A minimum ACL: </p>
<pre>
  <code>chacl u::rwx,g::r-x,o::r-- file</code>
</pre>
<p> The file ACL is set so that the file&#8217;s owner has &quot;rwx&quot;, the file&#8217;s group has read and execute, and others have read only access to the file. </p>
<p> An ACL that is not a minimum ACL, that is, one that specifies a user or group other than the file&#8217;s owner or owner&#8217;s group, must contain a mask entry: </p>
<pre>
  <tt>chacl u::rwx,g::r-x,o::r--,u:bob:r--,m::r-x file1 file2</tt>
</pre>
<p> To set the default and access ACLs on <tt>newdir</tt> to be the same as on <tt>olddir</tt>, you could type: </p>
<pre>
  <tt>chacl -b `chacl -l olddir | \
      sed -e 's/.*\[//' -e 's#/# #' -e 's/]$//'` newdir
</tt>
</pre>
<h2>CAUTIONS</h2>
<p> <i>chacl</i> can replace the existing ACL. To add or delete entries, you must first do <tt>chacl -l</tt> to get the existing ACL, and use the output to form the arguments to <i>chacl</i>. </p>
<p> Changing the permission bits of a file will change the file access ACL settings (see <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1)). However, file creation mode masks (see <i><a href="/docs/linux/man/1-umask/">umask</a></i>(1)) will not affect the access ACL settings of files created using directory default ACLs. </p>
<p> ACLs are filesystem extended attributes and hence are not typically archived or restored using the conventional archiving utilities. See <i><a href="/docs/linux/man/5-attr/">attr</a></i>(5) for more information about extended attributes and see <i><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></i>(8) for a method of backing them up under XFS.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getfacl/">getfacl</a></code>(1), <code><a href="/docs/linux/man/1-setfacl/">setfacl</a></code>(1), <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/1-umask/">umask</a></code>(1), <code><a href="/docs/linux/man/3-acl_from_text/">acl_from_text</a></code>(3), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5), <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8) </p>
<h2>Index</h2>
