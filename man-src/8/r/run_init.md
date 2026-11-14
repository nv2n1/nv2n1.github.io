---
title: "run_init(8)"
name: "run_init"
section: "8"
letter: "r"
url: "/docs/linux/man/8-run_init/"
description: "run_init – run an init script in the proper SELinux context"
---

<p>run_init &#8211; run an init script in the proper SELinux context</p>
<h2>Synopsis</h2>
<p><code>run_init </code> <i>SCRIPT</i> [[<i>ARGS</i>]&#8230;]</p>
<h2>Description</h2>
<p>Run a init script under the proper context, which is specified in /etc/selinux/POLICYTYPE/contexts/initrc_context.</p>
<h2>Files</h2>
<p>/etc/passwd &#8211; user account information<br />
 /etc/shadow &#8211; encrypted passwords and age information<br />
 /etc/selinux/POLICYTYPE/contexts/initrc_context &#8211; contains the context to run init scripts under</p>
<h2>See Also</h2>
<p><code>newrole</code> (1), <code>runcon</code> (1)</p>
<h2>Authors</h2>
<pre>Wayne Salamon (wsalamon [at] tislabs.com) 
Dan Walsh (dwalsh [at] redhat.com) </pre>
