---
title: "semanage-permissive(8)"
name: "semanage-permissive"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-permissive/"
description: "semanage-permissive – SELinux Policy Management permissive mapping tool"
---

<p><code>semanage-permissive &#8211; SELinux Policy Management permissive mapping tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage permissive [-h] (-a | -d | -l) [-n] [-N] [-S STORE] [type]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage permissive adds or removes a SELinux Policy permissive module. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-a, &#8211;add</i></p>
<dd>Add a record of the specified object type</p>
<dt><i>-d, &#8211;delete</i></p>
<dd>Delete a record of the specified object type</p>
<dt><i>-l, &#8211;list</i></p>
<dd>List records of the specified object type</p>
<dt><i>-n, &#8211;noheading</i></p>
<dd>Do not print heading when listing the specified object type</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload the policy after commit</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage </p>
</dl>
<h2>Example</h2>
<pre>List all permissive modules
# semanage permissive -l
Make httpd_t (Web Server) a permissive domain
# semanage permissive -a httpd_t</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
