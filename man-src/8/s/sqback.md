---
title: "sqback(8)"
name: "sqback"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sqback/"
description: "sqback – send sagator’s quarantined files back to mail queue"
---

<p>sqback &#8211; send sagator&#8217;s quarantined files back to mail queue</p>
<h2>Synopsis</h2>
<p><code>sqback</code> [&#8211;help] [&#8211;to RCPT] quarantined_file1 [quarantined_files&#8230;]</p>
<h2>Description</h2>
<p>This command can be used to deliver emails, quarantined by sagator. Sometimes sagator quarantines an email as virus or spam, which need to be delivered to it&#8217;s recipient (or admin).</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Display a short help text.</p>
<dt>&#8211;to RCPT</p>
<dd>Define one new recipient for this email. All other recipients from quarantined file will be replaced by this new recipient.</p>
<dt>quarantined_files</p>
<dd>You can define one or more files to return back to mail queue.</dl>
<h2>Examples</h2>
<dl>
<dt>Deliver an file quarantined as /tmp/quarantine/200412/qm-20041220-102448-0 in chroot set to /var/spool/vscan:</p>
<dd><code>sqback</code> /var/spool/vscan/tmp/quarantine/200412/qm-20041220-102448-0</p>
<dt>Deliver same file to admin for analyze:</p>
<dd><code>sqback</code> &#8211;to admin [at] localhost /var/spool/vscan/tmp/quarantine/200412/qm-20041220-102448-0</dl>
<h2>Author</h2>
<p>Jan ONDREJ (SAL) &lt;ondrejj (at) salstar.sk&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sagator/">sagator</a>(8), <a href="/docs/linux/man/1-sgscan/">sgscan</a>(1), <a href="/docs/linux/man/1-sgfilter/">sgfilter</a>(1) </p>
