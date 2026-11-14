---
title: "nfs4_acl(5)"
name: "nfs4_acl"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nfs4_acl/"
description: "nfs4_acl – NFSv4 Access Control Lists"
---

<p>nfs4_acl &#8211; NFSv4 Access Control Lists</p>
<h2>Description</h2>
<p>An ACL is a list of permissions associated with a file or directory and consists of one or more Access Control Entries (ACEs). NFSv4 ACLs provide finer granularity than typical POSIX read/write/execute permissions and are similar to CIFS ACLs. </p>
<p> A sample NFSv4 file ACL might look like the following (see the <code>ACL FORMAT</code> section for detailed information):</p>
<dl>
<dd>
<pre>A::OWNER@:rwatTnNcCy
A::alice [at] nfsdomain.org:rxtncy
A::bob [at] nfsdomain.org:rwadtTnNcCy
A:g:GROUP@:rtncy
D:g:GROUP@:waxTC
A::EVERYONE@:rtncy
D::EVERYONE@:waxTC</pre>
</dl>
<p> Some observations:</p>
<dl>
<dt>&#8211;</p>
<dd>In the example output above, the user `alice [at] nfsdomain.org&#8217; has the equivalent of &quot;read&quot; and &quot;execute&quot; permissions, `bob [at] nfsdomain.org&#8217; has &quot;read&quot; and &quot;write&quot;, and both `GROUP@&#8217; and `EVERYONE@&#8217; have &quot;read&quot;.</p>
<dt>&#8211;</p>
<dd>NFSv4 ACLs are &quot;default-deny&quot;; that is, if a permission is not explicitly granted by an Allow ACE, it is denied. Because of this, the two Deny ACEs above are superfluous and could be excluded by the server. See the <code>A WARNING ABOUT DENY ACES</code> section for more information.</p>
<dt>&#8211;</p>
<dd>NFSv4 servers may return an ACL slightly different than one you set. For example, a server that always allows reading the attributes of a file may silently turn on the read-attributes <i>permission</i>, and a server that does not support separate write-data and append-data <i>permissions</i>, e.g., may choose to turn off both if you set only one. In extreme cases the server may also reorder or combine ACEs. As a general rule, however, servers will attempt to ensure that the ACLs they return are no more permissive than the ones you set.</dl>
<h2>Acl Format</h2>
<p>An NFSv4 ACL is written as an <i>acl_spec</i>, which is a comma- or tab-delimited string consisting of one or more <i>ace_specs</i>. A single NFSv4 ACE is written as an <i>ace_spec</i>, which is a colon-delimited, 4-field string in the following format: </p>
<dl>
<dd><i>type</i>:<i>flags</i>:<i>principal</i>:<i>permissions</i></dl>
<h3>Ace Types:</h3>
<p>There are four <i>types</i> of ACEs, each represented by a single character. An ACE must have exactly one <i>type</i>.</p>
<dl>
<dd><code>A</code> Allow &#8211; allow <i>principal</i> to perform actions requiring <i>permissions</i>.</p>
<dd><code>D</code> Deny &#8211; prevent <i>principal</i> from performing actions requiring <i>permissions</i>.</p>
<dd><code>U</code> Audit &#8211; log any attempted access by <i>principal</i> which requires <i>permissions</i>. Requires one or both of the successful-access and failed-access <i>flags</i>. System-dependent; not supported by all servers.</p>
<dd><code>L</code> Alarm &#8211; generate a system alarm at any attempted access by <i>principal</i> which requires <i>permissions</i>. Requires one or both of the successful-access and failed-access <i>flags</i>. System-dependent; not supported by all servers.</dl>
<h3>Ace Flags:</h3>
<p>There are three kinds of ACE <i>flags</i>: group, inheritance, and administrative. An Allow or Deny ACE may contain zero or more <i>flags</i>, while an Audit or Alarm ACE must contain at least one of the successful-access and failed-access <i>flags</i>. </p>
<p> Note that ACEs are inherited from the parent directory&#8217;s ACL at the time a file or subdirectory is created. Accordingly, inheritance flags can be used only in ACEs in a directory&#8217;s ACL (and are therefore stripped from inherited ACEs in a new file&#8217;s ACL). Please see the <code>INHERITANCE FLAGS COMMENTARY</code> section for more information.</p>
<dl>
<dd><code>GROUP FLAG</code> &#8211; can be used in any ACE</p>
<dt><code>g</code></p>
<dd>group &#8211; indicates that <i>principal</i> represents a group instead of a user.</p>
<dt><code>INHERITANCE FLAGS</code> &#8211; can be used in any directory ACE</p>
<dd>
<dt><code>d</code></p>
<dd>directory-inherit &#8211; newly-created subdirectories will inherit the ACE.</p>
<dt><code>f</code></p>
<dd>file-inherit &#8211; newly-created files will inherit the ACE, minus its inheritance <i>flags</i>. Newly-created subdirectories will inherit the ACE; if directory-inherit is not also specified in the parent ACE, inherit-only will be added to the inherited ACE.</p>
<dt><code>n</code></p>
<dd>no-propagate-inherit &#8211; newly-created subdirectories will inherit the ACE, minus its inheritance <i>flags</i>.</p>
<dt><code>i</code></p>
<dd>inherit-only &#8211; the ACE is not considered in permissions checks, but it is heritable; however, the inherit-only <i>flag </i> is stripped from inherited ACEs.</p>
<dd><code>ADMINISTRATIVE FLAGS</code> &#8211; can be used in <code>Audit</code> and <code>Alarm</code> ACEs</p>
<dt><code>S</code></p>
<dd>successful-access &#8211; trigger an alarm/audit when <i>principal</i> is allowed to perform an action covered by <i>permissions</i>.</p>
<dt><code>F</code></p>
<dd>failed-access &#8211; trigger an alarm/audit when <i>principal</i> is prevented from performing an action covered by <i>permissions</i>.</dl>
<h3>Ace Principals:</h3>
<p>A <i>principal</i> is either a named user (e.g., `myuser [at] nfsdomain.org&#8217;) or group (provided the group <i>flag </i> is also set), or one of three special <i>principals</i>: `OWNER@&#8217;, `GROUP@&#8217;, and `EVERYONE@&#8217;, which are, respectively, analogous to the POSIX user/group/other distinctions used in, e.g., <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1).</p>
<h3>Ace Permissions:</h3>
<p>There are a variety of different ACE <i>permissions </i> (13 for files, 14 for directories), each represented by a single character. An ACE should have one or more of the following <i>permissions</i> specified:</p>
<dl>
<dt><code>r</code></p>
<dd>read-data (files) / list-directory (directories)</p>
<dt><code>w</code></p>
<dd>write-data (files) / create-file (directories)</p>
<dt><code>a</code></p>
<dd>append-data (files) / create-subdirectory (directories)</p>
<dt><code>x</code></p>
<dd>execute (files) / change-directory (directories)</p>
<dt><code>d</code></p>
<dd>delete &#8211; delete the file/directory. Some servers will allow a delete to occur if either this <i>permission </i> is set in the file/directory or if the delete-child <i>permission</i> is set in its parent direcory.</p>
<dt><code>D</code></p>
<dd>delete-child &#8211; remove a file or subdirectory from within the given directory (directories only)</p>
<dt><code>t</code></p>
<dd>read-attributes &#8211; read the attributes of the file/directory.</p>
<dt><code>T</code></p>
<dd>write-attributes &#8211; write the attributes of the file/directory.</p>
<dt><code>n</code></p>
<dd>read-named-attributes &#8211; read the named attributes of the file/directory.</p>
<dt><code>N</code></p>
<dd>write-named-attributes &#8211; write the named attributes of the file/directory.</p>
<dt><code>c</code></p>
<dd>read-ACL &#8211; read the file/directory NFSv4 ACL.</p>
<dt><code>C</code></p>
<dd>write-ACL &#8211; write the file/directory NFSv4 ACL.</p>
<dt><code>o</code></p>
<dd>write-owner &#8211; change ownership of the file/directory.</p>
<dt><code>y</code></p>
<dd>synchronize &#8211; allow clients to use synchronous I/O with the server. </p>
</dl>
<h2>Inheritance Flags Commentary</h2>
<p>Inheritance <i>flags </i> can be divided into two categories: &quot;primary&quot; (file-inherit and directory-inherit); and &quot;secondary&quot; (no-propagate-inherit and inherit-only), which are significant only insofar as they affect the two &quot;primary&quot; <i>flags</i>. </p>
<p> The no-propagate-inherit and inherit-only <i>flags </i> can be tricky to remember: the former determines whether or not a new child directory&#8217;s inherited ACE is itself heritable by a grandchild subdirectory; the latter determines whether or not a heritable ACE affects the parent directory itself (in addition to being heritable). They can be used in-tandem. </p>
<p> When a subdirectory inherits an ACE from its parent directory&#8217;s ACL, this can happen in one of two different ways, depending on the server implementation:</p>
<dl>
<dt>&#8211;</p>
<dd>In the simple case, that exact same ACE is set in the subdirectory&#8217;s ACL.</p>
<dt>&#8211;</p>
<dd>In the other case, two different ACEs will instead be set in the subdirectory&#8217;s ACL: one with all inheritance <i>flags </i> removed, and one with the inherit-only <i>flag</i> added. The former is the &quot;effective&quot; inherited ACE (used in the subdirectory&#8217;s own permissions checks); the latter is the &quot;heritable&quot; inherited ACE (when the subdirectory has directories created within it, they inherit it). This approach makes it easier to modify access rights to the subdirectory itself without modifying its heritable ACEs.</dl>
<h2>A Warning About Deny Aces</h2>
<p>Deny ACEs should be avoided whenever possible. Although they are a valid part of NFSv4 ACLs, Deny ACEs can be confusing and complicated. This stems primarily from the fact that, unlike POSIX ACLs and CIFS ACLs, the ordering of ACEs within NFSv4 ACLs affects how they are evaluated. </p>
<p> First, it is important to note that (despite some unfortunate ambiguity in <i>RFC3530</i>) NFSv4 ACLs are &quot;default-deny&quot; in practice. That is, if a <i>permission</i> is not explicitly granted, it is denied. </p>
<p> In general, when a <i>principal </i> is attempting to perform an action over NFSv4 which requires one or more <i>permissions</i>, an access check is performed. The NFSv4 ACL (assuming one is present) is evaluated ACE-by-ACE until every one of those <i>permissions </i> has been addressed, or until the end of the ACL is reached. If every requisite <i>permission</i> was granted by Allow ACEs and was not forbidden by Deny ACEs (see next paragraph), the action is allowed to proceed. Otherwise, the action is forbidden. </p>
<p> Note that each requisite <i>permission</i> is only addressed once &#8212; that is, after a <i>permission</i> has been explicitly Allowed or Denied once during an access check, any subsequent ACEs in the ACL which affect that <i>permission</i> are no longer considered. This often introduces problematic ordering issues when Deny ACEs are present. </p>
<p> Additionally, in some cases Group-Deny ACEs can be difficult (if not impossible) to enforce, since a server might not know about all of a given <i>principal</i>&#8216;s memberships in remote groups, e.g. </p>
<p> Because NFSv4 ACLs are &quot;default-deny&quot;, the use of Deny ACEs can (and should) be avoided entirely in most cases.</p>
<h2>Authors</h2>
<p>Tools for viewing and manipulating NFSv4 ACLs, <code>nfs4_getfacl</code> and <code>nfs4_setfacl</code>, were written by people at CITI, the Center for Information Technology Integration (<i><a rel="nofollow" href="http://www.citi.umich.edu">http://www.citi.umich.edu</a></i>). This manpage was written by David Richter and J. Bruce Fields.</p>
<h2>Contact</h2>
<p>Please send bug reports, feature requests, and comments to &lt;<i>nfsv4 [at] linux-nfs.org</i>&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nfs4_getfacl/">nfs4_getfacl</a></code>(1), <code><a href="/docs/linux/man/1-nfs4_setacl/">nfs4_setacl</a></code>(1), <i>RFC3530</i> (NFSv4.0), NFSv4.1 Minor Version Draft. </p>
