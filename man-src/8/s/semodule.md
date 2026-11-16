---
title: "semodule(8)"
name: "semodule"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semodule/"
description: "semodule – Manage SELinux policy modules."
---

<p>semodule &#8211; Manage SELinux policy modules. </p>
<h2>Synopsis</h2>
<p><code>semodule [options]&#8230; MODE [MODES]&#8230;</code></p>
<h2>Description</h2>
<p>semodule is the tool used to manage SELinux policy modules, including installing, upgrading, listing and removing modules. semodule may also be used to force a rebuild of policy from the module store and/or to force a reload of policy without performing any other transaction. semodule acts on module packages created by semodule_package. Conventionally, these files have a .pp suffix (policy package), although this is not mandated in any way. </p>
<h2>Options</h2>
<dl>
<dt><code>-R, &#8211;reload</code></dt>
<dd>force a reload of policy</dd>
<dt><code>-B, &#8211;build</code></dt>
<dd>force a rebuild of policy (also reloads unless -n is used)</dd>
<dt><code>-D, &#8211;disable_dontaudit</code></dt>
<dd>Temporarily remove dontaudits from policy. Reverts whenever policy is rebuilt</dd>
<dt><code>-i,&#8211;install=MODULE_PKG</code></dt>
<dd>install/replace a module package</dd>
<dt><code>-u,&#8211;upgrade=MODULE_PKG</code></dt>
<dd>deprecated, alias for &#8211;install</dd>
<dt><code>-b,&#8211;base=MODULE_PKG </code></dt>
<dd>deprecated, alias for &#8211;install</dd>
<dt><code>-r,&#8211;remove=MODULE_NAME</code></dt>
<dd>remove existing module</dd>
<dt><code>-l[KIND],&#8211;list-modules[=KIND]</code></dt>
<dd>display list of installed modules (other than base)</dd>
<dt><code>-E,&#8211;extract=MODULE_PKG</code></dt>
<dd>Extract a module from the store as an HLL or CIL file to the current directory. A module is extracted as HLL by default. The name of the module written is &lt;module-name&gt;.&lt;lang_ext&gt;</dd>
<dt><code>KIND:</code></dt>
<dd>
</dd><dt>standard</dt>
<dd>list highest priority, enabled, non-base modules</dd>
<dt>full</dt>
<dd>list all modules</dd>
<dt><code>-X,&#8211;priority=PRIORITY</code></dt>
<dd>set priority for following operations (1-999)</dd>
<dt><code>-e,&#8211;enabled=MODULE_NAME</code></dt>
<dd>enable module</dd>
<dt><code>-d,&#8211;disable=MODULE_NAME</code></dt>
<dd>disable module</dd>
<dt><code>-s,&#8211;store</code></dt>
<dd>name of the store to operate on</dd>
<dt><code>-n,&#8211;noreload,-N</code></dt>
<dd>do not reload policy after commit</dd>
<dt><code>-h,&#8211;help </code></dt>
<dd>prints help message and quit</dd>
<dt><code>-P,&#8211;preserve_tunables</code></dt>
<dd>Preserve tunables in policy</dd>
<dt><code>-C,&#8211;ignore-module-cache</code></dt>
<dd>Recompile CIL modules built from HLL files</dd>
<dt><code>-p,&#8211;path</code></dt>
<dd>Use an alternate path for the policy root</dd>
<dt><code>-S,&#8211;store-path</code></dt>
<dd>Use an alternate path for the policy store root</dd>
<dt><code>-v,&#8211;verbose </code></dt>
<dd>be verbose</dd>
<dt><code>-c,&#8211;cil</code></dt>
<dd>Extract module as a CIL file. This only affects the &#8211;extract option and only modules listed in &#8211;extract after this option.</dd>
<dt><code>-H,&#8211;hll</code></dt>
<dd>Extract module as an HLL file. This only affects the &#8211;extract option and only modules listed in &#8211;extract after this option. </dd>
</dl>
<h2>Example</h2>
<pre># Install or replace a base policy package.
$ semodule -b base.pp
# Install or replace a non-base policy package.
$ semodule -i httpd.pp
# List non-base modules.
$ semodule -l
# Turn on all AVC Messages for which SELinux currently is &quot;dontaudit&quot;ing.
$ semodule -DB
# Turn &quot;dontaudit&quot; rules back on.
$ semodule -B
# Install or replace all non-base modules in the current directory.
$ semodule -i *.pp
# Install or replace all modules in the current directory.
$ ls *.pp | grep -Ev &quot;base.pp|enableaudit.pp&quot; | xargs /usr/sbin/semodule -b base.pp -i
# Disable a module.
$ semodule -d alsa
# Install a module at a specific priority.
$ semodule -X 100 -i alsa.pp
# List all modules.
$ semodule --list=full
# Set an alternate path for the policy root
$ semodule -B -p &quot;/tmp&quot;
# Set an alternate path for the policy store root
$ semodule -B -S &quot;/tmp/var/lib/selinux&quot;
# Write the HLL version of puppet and the CIL version of wireshark
# modules at priority 400 to the current working directory
$ semodule -X 400 --hll -E puppet --cil -E wireshark</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-checkmodule/">checkmodule</a>(8), <a href="/docs/linux/man/8-semodule_package/">semodule_package</a>(8)</code></p>
<h2>Authors</h2>
<pre>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.
The program was written by Karl MacMillan &lt;kmacmillan [at] tresys.com&gt;, Joshua Brindle &lt;jbrindle [at] tresys.com&gt;, Jason Tang &lt;jtang [at] tresys.com&gt;</pre>
