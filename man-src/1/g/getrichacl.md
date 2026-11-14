---
title: "getrichacl(1)"
name: "getrichacl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getrichacl/"
description: "getrichacl – Get Rich Access Control Lists"
---

<h2>NAME</h2>
<p> getrichacl &#8211; Get Rich Access Control Lists</p>
<h2>SYNOPSIS</h2>
<p> <code>getrichacl</code> [<i>option</i>]&#8230; [<i>file</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each file, <code>getrichacl</code> displays the file name and the file&#8217;s Rich Access Control List (RichACL). </p>
<p> The output format of <code>getrichacl</code> is as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
1 : file : 2 : flags : a 3 : owner : rwp-- -- -- -- -- -- -::mask 4 : group : r - p-- -- -- -- -- -- -::mask 5 : other : r-- -- -- -- -- -- -- -::mask 6 : owner @ : rwp-- -- -- -- -- -- -::allow 7 : user : foo : r - p-- -- -- -- -- -- -::allow 8 : group @ : r - p-- -- -- -- -- -- -::allow 9 : group : bar : r - p-- -- -- -- -- -- -::allow 10 : everyone @ : r-- -- -- -- -- -- -- -::allow 11:
</code></pre>
</dl>
<p> Line 1 contains the file name, followed by a colon. </p>
<p> Line 2 contains the ACL flags. This line is omitted if no flags are set. </p>
<p> Lines 3&#8211;5 indicate the owner, group, and other file masks, which are only shown if the <code>&#8211;raw</code> option is specified. </p>
<p> Lines 6&#8211;10 indicate different ACL entries for the file owner (<code>owner@</code>), user <i>foo</i>, the owning group (<code>group@</code>), group <i>bar</i>, and for everyone (<code>everyone@</code>). </p>
<p> A blank line follows at the end. </p>
<p> The default output format uses the single-letter forms of flags and permissions, identifiers of ACL entries are right justified, permissions are vertically aligned, and permissions which are always granted (<code>read_attributes</code>, <code>read_acl</code>, <code>synchronize</code>) are omitted. See the <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7) manual page for the defined flags and permissions. </p>
<p> By default, <code>getrichacl</code> displays the effective permissions remaining after applying the file masks to the ACL. The file masks and underlying NFSv4 ACL can be displayed with the <code>&#8211;raw</code> option. </p>
<p> When <code>getrichacl</code> is used on a file that does not have a RichACL or on a filesystem that does not support RichACLs, it displays the access permissions defined by the traditional file permission bits as a RichACL. When <code>getrichacl</code> is used on a file that has a POSIX ACL (see <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5)), it prints an error message.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;long</code>, <code>-l</code></p>
<dd> Display access masks and flags in their long form.</p>
<dt><code>&#8211;full</code></p>
<dd> Also show permissions which are always implicitly allowed.</p>
<dt><code>&#8211;raw</code></p>
<dd> Show ACLs as stored on the file system, including the file masks. Implies <code>&#8211;full</code>.</p>
<dt><code>&#8211;unaligned</code></p>
<dd> Do not align ACL entries or pad missing permissions with &#8220;-&#8220;.</p>
<dt><code>&#8211;numeric-ids</code></p>
<dd> Display numeric user and group IDs instead of names.</p>
<dt><code>&#8211;access</code> [=<i>user</i>[:<i>group</i>:&#8230;]}, <code>-a</code>[<i>user</i>[:<i>group</i>:&#8230;]}</p>
<dd> Instead of showing the ACL, show which permissions the user running the command has for the specified file(s). When <i>user</i> is specified, show which permissions the specified user has instead. If <i>user</i> is followed by a colon and a (possibly empty) list of groups, assume that <i>user</i> is a member in the specified groups; otherwise, <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3) is used to determine the groups <i>user</i> is a member of.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Display the version of <code>getrichacl</code> and exit.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Display command-line usage help text.</dl>
<h2>AUTHOR</h2>
<p> Written by Andreas Grünbacher &lt;agruenba [at] redhat.com&gt;. </p>
<p> Please send your bug reports, suggested features and comments to the above address.</p>
<h2>CONFORMING TO</h2>
<p> Rich Access Control Lists are Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setrichacl/">setrichacl</a></code>(1), <code><a href="/docs/linux/man/7-richacl/">richacl</a></code>(7), <code><a href="/docs/linux/man/7-richaclex/">richaclex</a></code>(7) </p>
<h2>Index</h2>
