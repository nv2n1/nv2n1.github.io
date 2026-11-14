---
title: "sepolicy-transition(8)"
name: "sepolicy-transition"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy-transition/"
description: "sepolicy-transition – Examine the SELinux Policy and generate a process transition report"
---

<p>sepolicy-transition &#8211; Examine the SELinux Policy and generate a process transition report </p>
<h2>Synopsis</h2>
<p><code>sepolicy transition [-h] -s SOURCE</code><br />
 <code>sepolicy transition [-h] -s SOURCE -t TARGET</code> </p>
<h2>Description</h2>
<p>sepolicy transition will show all domains that a give SELinux source domain can transition to, including the entrypoint. If a target domain is given, sepolicy transition will examine policy for all transition paths from the source domain to the target domain, and will list the paths. If a transition is possible, this tool will print out all transition paths from the source domain to the target domain </p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message</p>
<dt><i>-s, &#8211;source</i></p>
<dd>Specify the source SELinux domain type.</p>
<dt><i>-t, &#8211;target</i></p>
<dd>Specify the target SELinux domain type. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8) </p>
