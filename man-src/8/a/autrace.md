---
title: "autrace(8)"
name: "autrace"
section: "8"
letter: "a"
url: "/docs/linux/man/8-autrace/"
description: "autrace – a program similar to strace"
---

<p>autrace &#8211; a program similar to strace</p>
<h2>Synopsis</h2>
<p><code>autrace</code> <i>program</i> [<code>-r</code>] [<i>program-args</i>]&#8230;</p>
<h2>Description</h2>
<p><code>autrace</code> is a program that will add the audit rules to trace a process similar to strace. It will then execute the <i>program</i> passing <i>arguments</i> to it. The resulting audit information will be in the audit logs if the audit daemon is running or syslog. This command deletes all audit rules prior to executing the target program and after executing it. As a safety precaution, it will not run unless all rules are deleted with <code>auditctl</code> prior to use.</p>
<h2>Options</h2>
<dl>
<dt><code>-r</code></p>
<dd>Limit syscalls collected to ones needed for analyzing resource usage. This could help people doing threat modeling. This saves space in logs.</dl>
<h2>Examples</h2>
<p>The following illustrates a typical session: </p>
<pre><code>autrace /bin/ls /tmp</code>
<code>ausearch --start recent -p 2442 -i </code></pre>
<p>and for resource usage mode: </p>
<pre><code>autrace -r /bin/ls</code>
<code>ausearch --start recent -p 2450 --raw | aureport --file --summary</code>
<code>ausearch --start recent -p 2450 --raw | aureport --host --summary</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
