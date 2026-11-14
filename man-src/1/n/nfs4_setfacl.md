---
title: "nfs4_setfacl(1)"
name: "nfs4_setfacl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfs4_setfacl/"
description: "nfs4_setfacl, nfs4_editfacl – manipulate NFSv4 file/directory access control lists"
---

<h2>NAME</h2>
<p> nfs4_setfacl, nfs4_editfacl &#8211; manipulate NFSv4 file/directory access control lists</p>
<h2>SYNOPSIS</h2>
<p> <code>nfs4_setfacl</code> [OPTIONS] COMMAND <i>file</i>&#8230;<br />
 <code>nfs4_editfacl</code> [OPTIONS] <i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>nfs4_setfacl </code> manipulates the NFSv4 Access Control List (ACL) of one or more <i>files </i> (or directories), provided they are on a mounted NFSv4 filesystem which supports ACLs. </p>
<p> <code>nfs4_editfacl </code> is equivalent to <code>nfs4_setfacl -e</code>. </p>
<p> Refer to the <code><a href="/docs/linux/man/5-nfs4_acl/">nfs4_acl</a></code>(5) manpage for information about NFSv4 ACL terminology and syntax.</p>
<h3>COMMANDS</h3>
<dl>
<dt><code>-a </code><i>acl_spec</i> [<i>index</i>]</p>
<dd> add the ACEs from <i>acl_spec</i> to <i>file</i>&#8216;s ACL. ACEs are inserted starting at the <i>index</i>th position (DEFAULT: 1) of <i>file</i>&#8216;s ACL.</p>
<dt><code>-A </code><i>acl_file</i> [<i>index</i>]</p>
<dd> add the ACEs from the acl_spec in <i>acl_file</i> to <i>file</i>&#8216;s ACL. ACEs are inserted starting at the <i>index</i>th position (DEFAULT: 1) of <i>file</i>&#8216;s ACL.</p>
<dt><code>-x </code><i>acl_spec </i>| index</p>
<dd> delete ACEs matched from <i>acl_spec</i> &#8211; or delete the <i>index</i>th ACE &#8211; from <i>file</i>&#8216;s ACL. Note that the ordering of the ACEs in <i>acl_spec</i> does not matter.</p>
<dt><code>-X </code><i>acl_file</i></p>
<dd> delete ACEs matched from the acl_spec in <i>acl_file</i> from <i>file</i>&#8216;s ACL. Note that the ordering of the ACEs in the acl_spec does not matter.</p>
<dt><code>-s </code><i>acl_spec</i></p>
<dd> set <i>file</i>&#8216;s ACL to <i>acl_spec</i>.</p>
<dt><code>-S </code><i>acl_file</i></p>
<dd> set <i>file</i>&#8216;s ACL to the acl_spec in <i>acl_file</i>.</p>
<dt><code>-e</code>,<code> &#8211;edit</code></p>
<dd> edit <i>file</i>&#8216;s ACL in the editor defined in the EDITOR environment variable (DEFAULT: <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1)) and set the resulting ACL upon a clean exit, assuming changes made in the editor were saved. Note that if multiple <i>files</i> are specified, the editor will be serially invoked once per <i>file</i>.</p>
<dt><code>-m </code><i>from_ace to_ace</i></p>
<dd> modify <i>file</i>&#8216;s ACL in-place by replacing <i>from_ace</i> with <i>to_ace</i>.</p>
<dt><code>-?</code>, <code>-h</code>, <code>&#8211;help</code></p>
<dd> display help text and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> display this program&#8217;s version and exit.</dl>
<p> NOTE: if &#8216;-&#8216; is given as the <i>acl_file</i> with the <code>-A</code>/<code>-X</code>/<code>-S</code> flags, the acl_spec will be read from stdin.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-R</code>,<code> &#8211;recursive</code></p>
<dd> recursively apply to a directory&#8217;s files and subdirectories. Similar to <code><a href="/docs/linux/man/1-setfacl/">setfacl</a></code>(1), the default behavior is to follow symlinks given on the command line and to skip symlinks encountered while recursing through directories.</p>
<dt><code>-L</code>,<code> &#8211;logical</code></p>
<dd> in conjunction with <code>-R</code>/<code>&#8211;recursive</code>, a logical walk follows all symbolic links.</p>
<dt><code>-P</code>,<code> &#8211;physical</code></p>
<dd> in conjunction with <code>-R</code>/<code>&#8211;recursive</code>, a physical walk skips all symbolic links.</p>
<dt><code>&#8211;test</code></p>
<dd> display results of <code>COMMAND</code>, but do not save changes. </p>
</dl>
<h2>PERMISSIONS ALIASES</h2>
<p> With <code>nfs4_setfacl</code>, one can use simple abbreviations (&quot;aliases&quot;) to express generic &quot;read&quot; (<code>R</code>), generic &quot;write&quot; (<code>W</code>), and generic &quot;execute&quot; (<code>X</code>) <i>permissions</i>, familiar from the POSIX mode bits used by, e.g., <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1). To use these aliases, one can put them in the <i>permissions</i> field of an NFSv4 ACE and <code>nfs4_setfacl</code> will convert them: an <code>R</code> is expanded to <code>rntcy</code>, a <code>W</code> is expanded to <code>watTNcCy </code> (with <code>D</code> added to directory ACEs), and an <code>X</code> is expanded to <code>xtcy</code>. Please refer to the <code><a href="/docs/linux/man/5-nfs4_acl/">nfs4_acl</a></code>(5) manpage for information on specific NFSv4 ACE <i>permissions</i>. </p>
<p> For example, if one wanted to grant generic &quot;read&quot; and &quot;write&quot; access on a file, the NFSv4 <i>permissions</i> field would normally contain something like <code>rwatTnNcCy</code>. Instead, one might use aliases to accomplish the same goal with <code>RW</code>. </p>
<p> The two <i>permissions</i> not included in any of the aliases are <code>d</code> (delete) and <code>o</code> (write-owner). However, they can still be used: e.g., a <i>permissions</i> field consisting of <code>Wdo</code> expresses generic &quot;write&quot; access as well as the ability to delete and change ownership.</p>
<h2>EXAMPLES</h2>
<p> Assume that the file `foo&#8217; has the following NFSv4 ACL for the following examples:</p>
<dl>
<dt>
<dd>
<pre>
A::OWNER@:rwatTnNcCy
D::OWNER@:x
A:g:GROUP@:rtncy
D:g:GROUP@:waxTC
A::EVERYONE@:rtncy
D::EVERYONE@:waxTC
</pre>
</dl>
<dl>
<dt>&#8211;</p>
<dd> add ACE granting `alice [at] nfsdomain.org&#8217; generic &quot;read&quot; and &quot;execute&quot; access (defaults to prepending ACE to ACL):<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -a A::alice [at] nfsdomain.org:rxtncy foo</p>
<dt>&#8211;</p>
<dd> add the same ACE as above, but using aliases:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -a A::alice [at] nfsdomain.org:RX foo</p>
<dt>&#8211;</p>
<dd> edit existing ACL in a text editor and set modified ACL on clean save/exit:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -e foo</p>
<dt>&#8211;</p>
<dd> set ACL (overwrites original) to contents of a <i>spec_file</i> named `newacl.txt&#8217;:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -S newacl.txt foo</p>
<dt>&#8211;</p>
<dd> recursively set the ACLs of all files and subdirectories in the current directory, skipping all symlinks encountered, to the ACL contained in the <i>spec_file</i> named `newacl.txt&#8217;:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -R -P -S newacl.txt *</p>
<dt>&#8211;</p>
<dd> delete the first ACE, but only print the resulting ACL (does not save changes):<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl &#8211;test -x 1 foo</p>
<dt>&#8211;</p>
<dd> delete the last two ACEs above:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -x A::EVERYONE [at] rtncy,D::EVERYONE@:waxTC foo</p>
<dt>&#8211;</p>
<dd> modify (in-place) the second ACE above:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_setfacl -m D::OWNER@:x D::OWNER@:xo foo</p>
<dt>&#8211;</p>
<dd> set ACLs of `bar&#8217; and `frobaz&#8217; to ACL of `foo&#8217;:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ nfs4_getfacl foo | nfs4_setfacl -S &#8211; bar frobaz
</dl>
<h2>AUTHORS</h2>
<p> <code>nfs4_setfacl </code> was written by people at CITI, the Center for Information Technology Integration (<i><a rel="nofollow" href="http://www.citi.umich.edu">http://www.citi.umich.edu</a></i>). This manpage was written by David Richter.</p>
<h2>CONTACT</h2>
<p> Please send bug reports, feature requests, and comments to &lt;<i>nfsv4 [at] linux-nfs.org</i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nfs4_getfacl/">nfs4_getfacl</a></code>(1), <code><a href="/docs/linux/man/5-nfs4_acl/">nfs4_acl</a></code>(5), <i>RFC3530</i> (NFSv4.0), NFSv4.1 Minor Version Draft. </p>
<h2>Index</h2>
