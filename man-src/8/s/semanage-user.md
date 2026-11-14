---
title: "semanage-user(8)"
name: "semanage-user"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-user/"
description: "semanage-user – SELinux Policy Management SELinux User mapping tool"
---

<p><code>semanage-user &#8211; SELinux Policy Management SELinux User mapping tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage user [-h] [-n] [-N] [-S STORE] [ &#8211;add ( -L LEVEL -R ROLES -r RANGE -s SEUSER selinux_name) | &#8211;delete selinux_name | &#8211;deleteall | &#8211;extract | &#8211;list [-C] | &#8211;modify ( -L LEVEL -R ROLES -r RANGE -s SEUSER selinux_name ) ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage user controls the mapping between an SELinux User and the roles and MLS/MCS levels. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-n, &#8211;noheading</i></p>
<dd>Do not print heading when listing the specified object type</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload policy after commit</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage</p>
<dt><i>-C, &#8211;locallist</i></p>
<dd>List local customizations</p>
<dt><i>-a, &#8211;add</i></p>
<dd>Add a record of the specified object type</p>
<dt><i>-d, &#8211;delete</i></p>
<dd>Delete a record of the specified object type</p>
<dt><i>-m, &#8211;modify</i></p>
<dd>Modify a record of the specified object type</p>
<dt><i>-l, &#8211;list</i></p>
<dd>List records of the specified object type</p>
<dt><i>-E, &#8211;extract</i></p>
<dd>Extract customizable commands, for use within a transaction</p>
<dt><i>-D, &#8211;deleteall</i></p>
<dd>Remove all local customizations</p>
<dt><i>-L LEVEL, &#8211;level LEVEL</i></p>
<dd>Default SELinux Level for SELinux user, s0 Default. (MLS/MCS Systems only)</p>
<dt><i>-r RANGE, &#8211;range RANGE</i></p>
<dd>MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range. SELinux Range for SELinux user defaults to s0.</p>
<dt><i>-R [ROLES], &#8211;roles [ROLES]</i></p>
<dd>SELinux Roles. You must enclose multiple roles within quotes, separate by spaces. Or specify -R multiple times. </p>
</dl>
<h2>Example</h2>
<pre>List SELinux users
# semanage user -l
Modify groups for staff_u user
# semanage user -m -R &quot;system_r unconfined_r staff_r&quot; staff_u
Add level for TopSecret Users
# semanage user -a -R &quot;staff_r&quot; -rs0-TopSecret topsecret_u</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> <code>semanage-login (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
