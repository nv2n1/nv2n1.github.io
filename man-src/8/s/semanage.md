---
title: "semanage(8)"
name: "semanage"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage/"
description: "semanage – SELinux Policy Management tool"
---

<p>semanage &#8211; SELinux Policy Management tool </p>
<h2>Synopsis</h2>
<p><code>semanage {import,export,login,user,port,interface,module,node,fcontext,boolean,permissive,dontaudit}</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230; <code>positional arguments:</code> <code>import</code> Import local customizations <code>export</code> Output local customizations <code>login</code> Manage login mappings between linux users and SELinux confined users <code>user</code> Manage SELinux confined users (Roles and levels for an SELinux user) <code>port</code> Manage network port type definitions <code>interface</code> Manage network interface type definitions <code>module</code> Manage SELinux policy modules <code>node</code> Manage network node type definitions <code>fcontext</code> Manage file context mapping definitions <code>boolean</code> Manage booleans to selectively enable functionality <code>permissive</code> Manage process type enforcement mode <code>dontaudit</code> Disable/Enable dontaudit rules in policy </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. This includes the mapping from Linux usernames to SELinux user identities (which controls the initial security context assigned to Linux users when they login and bounds their authorized role set) as well as security context mappings for various kinds of objects, such as network ports, interfaces, and nodes (hosts) as well as the file context mapping. Note that the semanage login command deals with the mapping from Linux usernames (logins) to SELinux user identities, while the semanage user command deals with the mapping from SELinux user identities to authorized role sets. In most cases, only the former mapping needs to be adjusted by the administrator; the latter is principally defined by the base policy and usually does not require modification. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>List help information </p>
</dl>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage-boolean (8),</code> <code>semanage-dontaudit (8),</code> <code>semanage-export (8),</code> <code>semanage-fcontext (8),</code> <code>semanage-import (8),</code> <code>semanage-interface (8),</code> <code>semanage-login (8),</code> <code>semanage-module (8),</code> <code>semanage-node (8),</code> <code>semanage-permissive (8),</code> <code>semanage-port (8),</code> <code>semanage-user (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;<br />
 and Russell Coker &lt;rcoker [at] redhat.com&gt;.<br />
 Examples by Thomas Bleher &lt;ThomasBleher [at] gmx.de&gt;. usage: semanage [-h]</p>
