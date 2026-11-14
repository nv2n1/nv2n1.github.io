---
title: "killpgrp(8)"
name: "killpgrp"
section: "8"
letter: "k"
url: "/docs/linux/man/8-killpgrp/"
description: "killpgrp – kill all processes in the same process group"
---

<p>killpgrp &#8211; kill all processes in the same process group</p>
<h2>Synopsis</h2>
<pre><code>killpgrp</code></pre>
<h2>Description</h2>
<p>Kills all processes in its process group when a process group leader is killed. </p>
<p> This program needs to be called by the client uid defined in amanda, and is used to kill VDUMP, VXDUMP, and XFSDUMP in a safe manner. It is called by sendsize, the amanda client software. </p>
<p> killpgrp send a SIGTERM to all processes in its process group. If a process in the group does not exit after three seconds and does not answer, killpgp will send a SIGKILL.</p>
<h2>Options</h2>
<p><code>killpgrp</code> takes no arguments.</p>
<h2>Security</h2>
<p><code>killpgrp</code> needs to be setuid root unless amanda is compiled with DONT_SUID_ROOT.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8)</p>
<h2>Author</h2>
<p>Manpage written by Rodrigo Rubira Branco &lt;rrbranco [at] br.ibm.com&gt;</p>
