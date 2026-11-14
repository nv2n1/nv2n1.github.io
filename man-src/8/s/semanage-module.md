---
title: "semanage-module(8)"
name: "semanage-module"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-module/"
description: "semanage-module – SELinux Policy Management module mapping tool"
---

<p><code>semanage-module &#8211; SELinux Policy Management module mapping tool</code></p>
<h2>Synopsis</h2>
<p><code>semanage module [-h] [-n] [-N] [-S STORE] (-a | -r | -e | -d | &#8211;extract | &#8211;list [-C] | &#8211;deleteall) [module_name]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage module installs, removes, disables SELinux Policy modules. </p>
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
<dt><i>-a, &#8211;add</i></p>
<dd>Install specified module</p>
<dt><i>-r, &#8211;remove</i></p>
<dd>Remove specified module</p>
<dt><i>-d &#8211;disable</i></p>
<dd>Disable specified module</p>
<dt><i>-e &#8211;enable</i></p>
<dd>Enable specified module</p>
<dt><i>-E, &#8211;extract</i></p>
<dd>Extract customizable commands, for use within a transaction</p>
<dt><i>-l, &#8211;list</i></p>
<dd>List records of the specified object type</p>
<dt><i>-C, &#8211;locallist</i></p>
<dd>List local customizations </p>
</dl>
<h2>Example</h2>
<pre>List all modules
# semanage module -l
Disable unconfined module
# semanage module --disable unconfined
Install custom apache policy module
# semanage module -a myapache</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> <code>semodule (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
