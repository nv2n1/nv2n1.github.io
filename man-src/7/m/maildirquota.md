---
title: "maildirquota(7)"
name: "maildirquota"
section: "7"
letter: "m"
url: "/docs/linux/man/7-maildirquota/"
description: "maildirquota – voluntary Maildir quotas"
---

<p>maildirquota &#8211; voluntary Maildir quotas</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>maildirmake</code> {-q} {10000000S} {./Maildir}</dl>
<h2>Description</h2>
<p><code>maildrop</code></p>
<dd>has a manual quota enforcement implementation that does use the quota facilities of the host operating system (filesystem-based quotas). This is an option that is set at configuration time, and may be disabled. </p>
<p> Using filesystem quotas sometimes leads to problems. After a hard quota is hit, most commands issued by mail clients fail, including some commands that poorly-written mail software may not expect to fail, and therefore be unable to gracefully handle the unexpected failure. </p>
<p> With manual quotas, the only operations that fail are the ones that most mail clients expect to fail, when the mailbox is full. However, filesystem-based quotas cannot be used in some situations, such as virtual mailboxes. If this experimental feature is enabled, approximate quota enforcement can be implemented by <code>maildrop</code> or <code>deliverquota</code> to whatever extent it&#8217;s possible to do so. Quotas are enabled by the <code>-q</code> option to <code>maildirmake</code>. Both <code>maildrop</code> and <code>deliverquota</code> will observe any <code>maildirmake</code>-requested quota.</p>
<h3>Limitations</h3>
<p>This quota mechanism will only work as long as <code>maildrop</code> (or <code>deliverquota</code>) are the only applications that deliver messages to the maildir, or as long as other applications implement the same quota enforcement mechanism. The quota enforcement mechanism is described separately in the README.maildirquota.html file in the source code distribution. </p>
<p> Quota enforcement will still work, to some extent, if there are other applications that deliver or modify messages in the maildir. However, quota enforcement may not kick in immediately when the maildir goes over quota, in fact the maildir can go over quota by a noticeable amount. But eventually, as long as <code>maildrop</code> or <code>deliverquota</code> are responsible for delivering the majority of messages, quota enforcement will kick in. Also, other sources of messages may also result in noticeable performance degradation, because quote recalculation will become noticeably more expensive. </p>
<p> Also keep in mind that this quota mechanism is generally useless if mail recipients have direct access to their maildirs. </p>
<p> Finally even under the best conditions this quota enforcement does have a small chance of a race condition where a maildir will go over quota by some amount. maildirs are designed for speed, and this quota implementation was designed to have as little additional overhead as possible, compared to regular maildirs. To enforce an exact quota you would have to use some kind of a locking facility, which will impose a drastic performance degradation on the overall maildir performance. A decision has been made to avoid locking, with the only negative side effect being a possibility of going over quota in very low probability situations. </p>
<p> A way to minimize the risk of going over quota is to set reasonable quotas, in relation to maximum message sizes supported by your mail server. If you set your maildir quota to five gigabytes, for example, it makes very little sense to configure your mail server to accept messages up to three gigabytes in size. Your maildir quota should be chosen so that it makes sense when compared to the maximum message size allowed by your mail server.</p>
<h3>Folders</h3>
<p>This quota implementation is compatible with a popular extension to maildir which defines individual mail folders within a single maildir. However, in order to create a compatible folder, you MUST use the <code>maildirmake</code> command that comes with <code>maildrop</code>, and you MUST use the <code>-f</code> option to <code>maildirmake</code>, giving the name of the folder. Do not use <code>maildirmake</code> and specify the directory name of the maildir folder. Quota enforcement will not work if you do that.</p>
<h2>See Also</h2>
<p>m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[1]</font>, m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[2]</font>, m[blue]<code><a href="/docs/linux/man/5-maildropfilter/">maildropfilter</a></code>(5)m[]<font SIZE="-2">[3]</font>, m[blue]<code><a href="/docs/linux/man/8-deliverquota/">deliverquota</a></code>(8)m[]<font SIZE="-2">[4]</font>.</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildrop.html</dl>
<dt> 2.</p>
<dd><code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildirmake.html</dl>
<dt> 3.</p>
<dd><code><a href="/docs/linux/man/5-maildropfilter/">maildropfilter</a></code>(5)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildropfilter.html</dl>
<dt> 4.</p>
<dd><code><a href="/docs/linux/man/8-deliverquota/">deliverquota</a></code>(8)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/deliverquota.html</dl>
