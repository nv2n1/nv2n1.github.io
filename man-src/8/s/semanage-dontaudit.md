---
title: "semanage-dontaudit(8)"
name: "semanage-dontaudit"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-dontaudit/"
description: "semanage-dontaudit – SELinux Policy Management dontaudit tool"
---

<p><code>semanage-dontaudit &#8211; SELinux Policy Management dontaudit tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage dontaudit [-h] [-S STORE] [-N] {on,off}</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage dontaudit toggles whether or not dontaudit rules will be in the policy. Policy writers use dontaudit rules to cause confined applications to use alternative paths. Dontaudit rules are denied but not reported in the logs. Some times dontaudit rules can cause bugs in applications but policy writers will not realize it since the AVC is not audited. Turning off dontaudit rules with this command to see if the kernel is blocking an access. </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload the policy after commit </p>
</dl>
<h2>Example</h2>
<pre>Turn off dontaudit rules
# semanage dontaudit off</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
