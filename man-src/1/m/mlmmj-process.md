---
title: "mlmmj-process(1)"
name: "mlmmj-process"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-process/"
description: "mlmmj-process – process mail for an mlmmj managed mailinglist"
---

<h2>NAME</h2>
<p> mlmmj-process &#8211; process mail for an mlmmj managed mailinglist</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-process</code> <i>-L /path/to/list -m /path/to/mail </i>[<i>-h</i>] [<i>-P</i>] [<i>-V</i>]</p>
<dl>
<dt> <code>-h</code>: This help</dt>
<dt> <code>-L</code>: Full path to list directory</dt>
<dt> <code>-m</code>: Full path to mail file</dt>
<dt> <code>-P</code>: Don&#8217;t execute mlmmj-send (debugging only)</dt>
<dt> <code>-V</code>: Print version</dt></dl>
<h2>DESCRIPTION</h2>
<dd>This is the binary which processes a mail. Examples of what such processing is:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <code>Access control</code> </dd>
<p> Using the access rules specified in &lt;listdir&gt;/control/access to perform access control to the list. This is done before headers are stripped, so one can create allow rules based on headers that are later stripped.</p>
<dt>&bull;</dt>
<dd> <code>Header stripping</code> </dd>
<p> Headers specified in &lt;listdir&gt;/control/delheaders are deleted from the mail.</p>
<dt>&bull;</dt>
<dd> <code>Header addition</code> </dd>
<p> Headers specified in &lt;listdir&gt;/control/customheaders are added to the mail. This could be headers like List-ID: or Reply-To:</p>
<dt>&bull;</dt>
<dd> <code>List control</code> </dd>
<p> In case there&#8217;s a mail with a recipient delimiter it&#8217;s not a regular list mail. Processing of these happens in mlmmj-receive as well. Examples of such are subscription requests, mails to owner etc. It will base it&#8217;s recipient delimiter detection on the Delivered-To: header if present. If not, the To: header is used.</p>
<dt>&bull;</dt>
<dd> <code>Moderation</code> </dd>
<p> If the list is moderated, it will happen in mlmmj-process.</dl>
</dl>
<p> When processing is done, it will invoke the needed binary according to whatever mail it is. If it&#8217;s a subscription request it will invoke mlmmj-sub, if it&#8217;s a regular list mail it will invoke mlmmj-send.</p>
<h2>SEE ALSO</h2>
<p> The file TUNABLES from the mlmmj source distribution or in the documentation directory of the operating system distribution.</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
</dt><dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</dd>
<dt>
</dt><dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </dd>
</dl>
