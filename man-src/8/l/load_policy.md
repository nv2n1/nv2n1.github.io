---
title: "load_policy(8)"
name: "load_policy"
section: "8"
letter: "l"
url: "/docs/linux/man/8-load_policy/"
description: "load_policy – load a new SELinux policy into the kernel"
---

<p>load_policy &#8211; load a new SELinux policy into the kernel </p>
<h2>Synopsis</h2>
<p><code>load_policy </code> [-qi]</p>
<h2>Description</h2>
<p>load_policy loads the installed policy file into the kernel. The existing policy boolean values are automatically preserved across policy reloads rather than being reset to the default values in the policy file. </p>
<h2>Options</h2>
<dl>
<dt><code>-q</code></p>
<dd>suppress warning messages.</p>
<dt><code>-i</code></p>
<dd>initial policy load. Only use this if this is the first time policy is being loaded since boot (usually called from initramfs). </p>
</dl>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></p>
<dd>Success</p>
<dt><code>1</code></p>
<dd>Invalid option</p>
<dt><code>2</code></p>
<dd>Policy load failed</p>
<dt><code>3</code></p>
<dd>Initial policy load failed and enforcing mode requested</dl>
<h2>See Also</h2>
<p><code>booleans</code> (8),</p>
<h2>Authors</h2>
<pre>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.
The program was written by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;.</pre>
