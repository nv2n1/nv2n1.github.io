---
title: "dmail(1)"
name: "dmail"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmail/"
description: "dmail – procmail Mail Delivery Module"
---

<h2>NAME</h2>
<p> dmail &#8211; procmail Mail Delivery Module</p>
<h2>SYNOPSIS</h2>
<p> <code>dmail</code> <i>[-D] [-f from_name] [-s] [-k keyword_list] [user][+folder]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>dmail</i> delivers mail to a user&#8217;s INBOX or a designated folder. <i>dmail</i> may be configured as a drop-in replacement for <i><a href="/docs/linux/man/1-binmail/">binmail</a></i>(1), <i><a href="/docs/linux/man/1-mail-local/">mail.local</a></i>(1) for use with a mail delivery filter such as <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1)<i>.</i> </p>
<p> Because of security considerations (see below) <i>dmail</i> is not intended to be used for direct delivery by the mailer daemon; <i><a href="/docs/linux/man/1-tmail/">tmail</a></i>(1) is the preferred tool for this purpose. If <i>dmail</i> is used for mailer daemon delivery, the mailer daemon must invoke <i>dmail</i> with the <i>dmail</i> process&#8217; user id set to the recipient&#8217;s user id. </p>
<p> When <i>dmail</i> exits, it returns exit status values to enable <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1) to determine whether a message was delivered successfully or had a temporary (requeue for later delivery) or permanent (return to sender) failure. </p>
<p> If the <i>user</i> name is present, it must be the same as the logged-in user name. </p>
<p> If the <i>+folder</i> extension is included in the user argument (or appears by itself if there is no user argument), <i>dmail</i> will attempt to deliver to the designated folder. If the folder does not exist or the extension is not included, the message is delivered to the user&#8217;s INBOX. If delivery is to INBOX and no INBOX currently exists, <i>dmail</i> will create a new INBOX. <i>dmail</i> recognizes the format of an existing INBOX or folder, and appends the new message in that format. </p>
<p> The <code>-D</code> flag specifies debugging; this enables additional message telemetry. </p>
<p> The <code>-f</code> or <code>-r</code> flag is used to specify a Return-Path. The header </p>
<p>Return-Path:&nbsp;<wbr>&lt;<i>from_name</i>&gt;&nbsp;<wbr><br />
 is prepended to the message before delivery. </p>
<p> The <code>-s</code> flag specifies that the message will be flagged as being &quot;seen&quot;. </p>
<p> The <code>-k</code> flag is used to specify delivery keywords, which are set on the message at delivery time if and <code>only</code> if the keywords are already defined in the mailbox. Multiple keywords can be specified by using a quoted string, e.g., </p>
<p>dmail -k&nbsp;<wbr>&quot;$Junk Discard&quot;&nbsp;<wbr>+junkbox </p>
<h2>RESTRICTIONS</h2>
<p> Absolute pathnames and <i>~user</i> specifications are not permitted in <i>+folder</i> extensions.</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p> Unlike <i>tmail</i> you can use <i>dmail</i> to deliver to IMAP4 namespace names via <i>+folder</i> extensions. This means that it is possible to deliver to <i><a href="/docs/linux/man/1-mh/">mh</a></i>(1) format mailboxes. </p>
<p> However, this can also include such namespaces as #shared, #public, and #ftp. In most cases, it is undesirable to allow anybody sending mail to the user to deliver to these namespaces. Consequently, there needs to be a rule in place in the configuration of either <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8) or <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1) to prevent such abuse.</p>
<h2>AUTHOR</h2>
<p> Mark Crispin, MRC [at] CAC.Washington.EDU</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-binmail/">binmail</a>(1)<br />
 <a href="/docs/linux/man/1-procmail/">procmail</a>(1) </p>
<h2>Index</h2>
