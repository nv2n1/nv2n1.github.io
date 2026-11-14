---
title: "semodule_unpackage(8)"
name: "semodule_unpackage"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semodule_unpackage/"
description: "semodule_unpackage – Extract policy module and file context file from an SELinux policy module unpackage."
---

<p>semodule_unpackage &#8211; Extract policy module and file context file from an SELinux policy module unpackage. </p>
<h2>Synopsis</h2>
<p><code>semodule_unpackage &lt;module&gt; [&lt;file contexts&gt;]</code></p>
<h2>Description</h2>
<p>semodule_unpackage is the tool used to extract the SELinux policy module<br />
&nbsp;<wbr>and file context file from an SELinux Policy Package. </p>
<h2>Example</h2>
<pre># Extract the httpd module file from httpd policy package.
$ semodule_unpackage httpd.pp httpd.mod httpd.fc</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-semodule_package/">semodule_package</a>(8)</code></p>
<h2>Authors</h2>
<pre>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.
The program was written by Stephen Smalley &lt;sds [at] tycho.nsa.gov&gt;</pre>
