---
title: "semanage-port(8)"
name: "semanage-port"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-port/"
description: "semanage-port – SELinux Policy Management port mapping tool"
---

<p><code>semanage-port &#8211; SELinux Policy Management port mapping tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage port [-h] [-n] [-N] [-S STORE] [ &#8211;add -t TYPE -p PROTOCOL -r RANGE port_name | port_range | &#8211;delete -p PROTOCOL port_name | port_range | &#8211;deleteall | &#8211;extract | &#8211;list [-C] | &#8211;modify -t TYPE -p PROTOCOL -r RANGE port_name | port_range ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage port controls the port number to port type definitions. </p>
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
<dt><i>-t TYPE, &#8211;type TYPE</i></p>
<dd>SELinux type for the object</p>
<dt><i>-r RANGE, &#8211;range RANGE</i></p>
<dd>MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range. SELinux Range for SELinux user defaults to s0.</p>
<dt><i>-p PROTO, &#8211;proto PROTO</i></p>
<dd>Protocol for the specified port (tcp|udp) or internet protocol version for the specified node (ipv4|ipv6). </p>
</dl>
<h2>Example</h2>
<pre>List all port definitions
# semanage port -l
Allow Apache to listen on tcp port 81
# semanage port -a -t http_port_t -p tcp 81
Allow sshd to listen on tcp port 8991
# semanage port -a -t ssh_port_t -p tcp 8991</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
