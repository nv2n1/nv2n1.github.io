---
title: "mailq-sendmail(1)"
name: "mailq-sendmail"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailq-sendmail/"
description: "mailq – print the mail queue"
---

<p>mailq &#8211; print the mail queue</p>
<h2>Synopsis</h2>
<p><code>mailq</code> [<code>-Ac</code>] [<code>-q&#8230;</code>] [<code>-v</code>]</p>
<h2>Description</h2>
<p><code>Mailq</code> prints a summary of the mail messages queued for future delivery. </p>
<p> The first line printed for each message shows the internal identifier used on this host for the message with a possible status character, the size of the message in bytes, the date and time the message was accepted into the queue, and the envelope sender of the message. The second line shows the error message that caused this message to be retained in the queue; it will not be present if the message is being processed for the first time. The status characters are either <code>*</code> to indicate the job is being processed; <code>X</code> to indicate that the load is too high to process the job; and <code>&#8211;</code> to indicate that the job is too young to process. The following lines show message recipients, one per line. </p>
<p> <code>Mailq</code> is identical to &#8220;sendmail -bp&#8221;. </p>
<p> The relevant options are as follows:</p>
<dl COMPACT>
<dt><code>-Ac</code></p>
<dd>Show the mail submission queue specified in <i>/etc/mail/submit.cf</i> instead of the MTA queue specified in <i>/etc/mail/sendmail.cf</i>.</p>
<dt><code>-qL</code></p>
<dd>Show the &quot;lost&quot; items in the mail queue instead of the normal queue items.</p>
<dt><code>-qQ</code></p>
<dd>Show the quarantined items in the mail queue instead of the normal queue items.</p>
<dt><code>-q</code>[<i>!</i>]I substr</p>
<dd>Limit processed jobs to those containing <i>substr</i> as a substring of the queue id or not when <i>!</i> is specified.</p>
<dt><code>-q</code>[<i>!</i>]Q substr</p>
<dd>Limit processed jobs to quarantined jobs containing <i>substr</i> as a substring of the quarantine reason or not when <i>!</i> is specified.</p>
<dt><code>-q</code>[<i>!</i>]R substr</p>
<dd>Limit processed jobs to those containing <i>substr</i> as a substring of one of the recipients or not when <i>!</i> is specified.</p>
<dt><code>-q</code>[<i>!</i>]S substr</p>
<dd>Limit processed jobs to those containing <i>substr</i> as a substring of the sender or not when <i>!</i> is specified.</p>
<dt><code>-v</code></p>
<dd>Print verbose information. This adds the priority of the message and a single character indicator (&#8220;+&#8221; or blank) indicating whether a warning message has been sent on the first line of the message. Additionally, extra lines may be intermixed with the recipients indicating the &#8220;controlling user&#8221; information; this shows who will own any programs that are executed on behalf of this message and the name of the alias this command expanded from, if any. Moreover, status messages for each recipient are printed if available.</dl>
<p> Several sendmail.cf options influence the behavior of the <code>mailq</code> utility: The number of items printed per queue group is restricted by <code>MaxQueueRunSize</code> if that value is set. The status character <code>*</code> is not printed for some values of <code>QueueSortOrder,</code> e.g., filename, random, modification, and none, unless a <code>-q</code> option is used to limit the processed jobs. </p>
<p> The <code>mailq</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</p>
<h2>History</h2>
<p>The <code>mailq</code> command appeared in 4.0BSD.</p>
