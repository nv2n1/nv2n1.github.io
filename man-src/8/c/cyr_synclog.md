---
title: "cyr_synclog(8)"
name: "cyr_synclog"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyr_synclog/"
description: "cyr_synclog – add entries to the replication log"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyr_synclog &#8211; add entries to the replication log</p>
<h2>Synopsis</h2>
<p><code>cyr_synclog</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-type</code> ] &lt;value&gt;</p>
<h2>Description</h2>
<p><i>cyr_synclog</i> is used to append a value to the log file. You can either specify the log type and value, or an entire log line. </p>
<p> -u USER </p>
<p> -v SIEVE </p>
<p> -m MAILBOX </p>
<p> -a APPEND </p>
<p> -c ACL </p>
<p> -q QUOTA </p>
<p> -n ANNOTATION </p>
<p> -s SEEN </p>
<p> -b SUBSCRIPTION </p>
<p> Running without any options will print a short usage document. </p>
<p> <i>cyr_synclog</i> reads any applicable configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Examples</h2>
<p>Here are some example ways to use cyr_synclog: </p>
<p> cyr_synclog -m user.brong </p>
<p> cyr_synclog -u brong </p>
<p> cyr_synclog -C /etc/imapd-special.conf -s user.brong brong </p>
<p> cyr_synclog &quot;SEEN user.brong brong&quot;</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code> </p>
