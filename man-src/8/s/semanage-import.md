---
title: "semanage-import(8)"
name: "semanage-import"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-import/"
description: "semanage-import – SELinux Policy Management import tool"
---

<p><code>semanage-import &#8211; SELinux Policy Management import tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage import [-h] [-N] [-S STORE] [-f INPUT_FILE]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage import and export can be used to extract the SELinux modifications from one machine and apply them to another. You can put a whole group of semanage commands within a file and apply them to a machine in a single transaction. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload policy after commit</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage</p>
<dt><i>-f INPUT_FILE, &#8211;input_file INPUT_FILE</i></p>
<dd>Input file</dl>
<h2>Example</h2>
<pre>Import semanage modifications from another machine
# semanage import -f semanage.mods</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8),</code> <code>semanage-export (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
