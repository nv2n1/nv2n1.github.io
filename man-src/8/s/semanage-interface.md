---
title: "semanage-interface(8)"
name: "semanage-interface"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-interface/"
description: "semanage-interface – SELinux Policy Management network interface tool"
---

<p><code>semanage-interface &#8211; SELinux Policy Management network interface tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage interface [-h] [-n] [-N] [-S STORE] [ &#8211;add -t TYPE -r RANGE interface | &#8211;delete interface | &#8211;deleteall | &#8211;extract | &#8211;list [-C] | &#8211;modify -t TYPE -r RANGE interface ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage interface controls the labels assigned to network interfaces. </p>
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
<dd>MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range. SELinux Range for SELinux user defaults to s0. </p>
</dl>
<h2>Example</h2>
<pre>list all interface definitions
# semanage interface -l</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
