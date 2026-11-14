---
title: "faxq-helper(8)"
name: "faxq-helper"
section: "8"
letter: "f"
url: "/docs/linux/man/8-faxq-helper/"
description: "faxq-helper – privileged helper process to access the fax queue"
---

<p>faxq-helper &#8211; privileged helper process to access the fax queue</p>
<h2>Synopsis</h2>
<p><code>faxq-helper &lt;command&gt; [&lt;options&gt;]</code></p>
<h2>Description</h2>
<p><i>faxq-helper</i> is part of the internal workings of <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1). Formerly, the /var/spool/fax/outgoing directory was world-writeable, leading to all sort of funny symlink attacks against <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) and <a href="/docs/linux/man/8-faxrunq/">faxrunq</a>(8). These days, it&#8217;s owned by the user &#8220;fax&#8221;, and only this user can write to it. To be able to put jobs there, <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) calls <i>faxq-helper</i> for very clearly defined purposes:<br />
&nbsp;<wbr>&#8211; make a new queue directory<br />
&nbsp;<wbr>&#8211; put a new fax G3 file into this queue directory<br />
&nbsp;<wbr>&#8211; put a JOB file into this queue directory, and activate the fax job and possibly:<br />
&nbsp;<wbr>&#8211; remove a fax job from the queue&nbsp;<wbr>(to be used by faxrm and in case of errors)<br />
&nbsp;<wbr>&#8211; re-queue a job that has been suspended due to repeated failures&nbsp;<wbr>(faxq -r) To achieve this, <i>faxq-helper</i> is installed set-user-id fax. If you remove the suid bit, or chown the fax queue directory to a different user, it will stop working. </p>
<h2>Return Values</h2>
<p><i>faxq-helper</i> has the following exit() values: </p>
<dl>
<dt><code>0</code></p>
<dd>everything went fine </p>
<dt><code>1</code></p>
<dd>invalid JOB ID specified on the command line </p>
<dt><code>2</code></p>
<dd>some problem with the directory setup of the outgoing queue dir, /var/spool/fax/outgoing (it will print a detailed error message) </p>
<dt><code>3</code></p>
<dd>some problems with the user ID setup of the &#8220;fax&#8221; user (it will print a detailed error message) </p>
<dt><code>10</code></p>
<dd>failure to process the specified command (it will print a detailed error message) </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/1-faxrm/">faxrm</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5)</p>
<h2>Author</h2>
<p><i>faxq-helper</i> is Copyright (C) 2004-2006 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;.</p>
