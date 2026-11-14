---
title: "mailq-ssmtp(8)"
name: "mailq-ssmtp"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mailq-ssmtp/"
description: "mailq – show contents of the mail queue"
---

<p>mailq &#8211; show contents of the mail queue</p>
<h2>Synopsis</h2>
<p><code>mailq</code></p>
<h2>Description</h2>
<p>This is a link to the ssmtp binary. It invokes <code>/usr/sbin/sendmail</code> with the <code>-q</code> option. It is provided for compatibility with the sendmail program. </p>
<p> In this case it does absolutely nothing since sSMTP does not support mail queues and is just there to avoid programs returning error messages.</p>
<h2>Author</h2>
<p>This manual page was written by Matt Ryan &lt;mryan [at] debian.org&gt; for the Debian GNU/Linux system.</p>
