---
title: "semanage-node(8)"
name: "semanage-node"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-node/"
description: "semanage-node – SELinux Policy Management node mapping tool"
---

<p><code>semanage-node &#8211; SELinux Policy Management node mapping tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage node [-h] [-n] [-N] [-S STORE] [ &#8211;add -M NETMASK -p PROTOCOL -t TYPE -r RANGE node | &#8211;delete -M NETMASK -p PROTOCOL node | &#8211;deleteall | &#8211;extract | &#8211;list [-C] | &#8211;modify -M NETMASK -p PROTOCOL -t TYPE -r RANGE node ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage controls the ipaddress to node type definitions. </p>
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
<dt><i>-M NETMASK, &#8211;netmask NETMASK</i></p>
<dd>Network Mask</p>
<dt><i>-t TYPE, &#8211;type TYPE</i></p>
<dd>SELinux type for the object</p>
<dt><i>-r RANGE, &#8211;range RANGE</i></p>
<dd>MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range. SELinux Range for SELinux user defaults to s0.</p>
<dt><i>-p PROTO, &#8211;proto PROTO</i></p>
<dd>Protocol for the specified port (tcp|udp) or internet protocol version for the specified node (ipv4|ipv6). </p>
</dl>
