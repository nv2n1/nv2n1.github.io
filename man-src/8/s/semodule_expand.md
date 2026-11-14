---
title: "semodule_expand(8)"
name: "semodule_expand"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semodule_expand/"
description: "semodule_expand – Expand a SELinux policy module package."
---

<p>semodule_expand &#8211; Expand a SELinux policy module package. </p>
<h2>Synopsis</h2>
<p><code>semodule_expand [-V ] [ -a ] [ -c [version]] basemodpkg outputfile</code></p>
<h2>Description</h2>
<p>semodule_expand is a developer tool for manually expanding a base policy module package into a kernel binary policy file. This tool is not necessary for normal operation of SELinux. In normal operation, such expanding is performed internally by libsemanage in response to semodule commands. Base policy module packages can be created directly by semodule_package or by semodule_link (when linking together a set of packages into a single package). </p>
<h2>Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>show version</p>
<dt><code>-c [version]</code></p>
<dd>policy version to create</p>
<dt><code>-a</code></p>
<dd>Do not check assertions. This will cause the policy to not check any neverallow rules. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-checkmodule/">checkmodule</a>(8), <a href="/docs/linux/man/8-semodule_package/">semodule_package</a>(8), <a href="/docs/linux/man/8-semodule/">semodule</a>(8), <a href="/docs/linux/man/8-semodule_link/">semodule_link</a>(8)</code> (8),</p>
<h2>Authors</h2>
<pre>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.
The program was written by Karl MacMillan &lt;kmacmillan [at] tresys.com&gt;, Joshua Brindle &lt;jbrindle [at] tresys.com&gt;</pre>
