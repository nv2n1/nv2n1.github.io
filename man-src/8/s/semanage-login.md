---
title: "semanage-login(8)"
name: "semanage-login"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-login/"
description: "semanage-login – SELinux Policy Management linux user to SELinux User mapping tool"
---

<p><code>semanage-login &#8211; SELinux Policy Management linux user to SELinux User mapping tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage login [-h] [-n] [-N] [-S STORE] [ &#8211;add -s SEUSER -r RANGE LOGIN | &#8211;delete LOGIN | &#8211;deleteall | &#8211;extract | &#8211;list [-C] | &#8211;modify -s SEUSER -r RANGE LOGIN ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage login controls the mapping between a Linux User and the SELinux User. It can be used to turn on confined users. For example you could define that a particular user or group of users will login to a system as the user_u user. Prefix the group name with a &#8216;%&#8217; sign to indicate a group name. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-n, &#8211;noheading</i></p>
<dd>Do not print heading when listing the specified object type</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload policy after commit</p>
<dt><i>-C, &#8211;locallist</i></p>
<dd>List local customizations</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage</p>
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
<dt><i>-s SEUSER, &#8211;seuser SEUSER</i></p>
<dd>SELinux user name</p>
<dt><i>-r RANGE, &#8211;range RANGE</i></p>
<dd>MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range. SELinux Range for SELinux user defaults to s0. </p>
</dl>
<h2>Example</h2>
<pre>Modify the default user on the system to the guest_u user
# semanage login -m -s guest_u __default__
Assign gijoe user on an MLS machine a range and to the staff_u user
# semanage login -a -s staff_u -rSystemLow-Secret gijoe
Assign all users in the engineering group to the staff_u user
# semanage login -a -s staff_u %engineering</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8),</code> <code>semanage-user (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
