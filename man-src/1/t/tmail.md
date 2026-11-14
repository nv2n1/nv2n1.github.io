---
title: "tmail(1)"
name: "tmail"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tmail/"
description: "tmail – Mail Delivery Module"
---

<h2>NAME</h2>
<p> tmail &#8211; Mail Delivery Module</p>
<h2>SYNOPSIS</h2>
<p> <code>tmail</code> <i>[-b format] [-D] [-f from_name] [-I inbox_specifier] user[+folder] &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>tmail</i> delivers mail to a user&#8217;s INBOX or a designated folder. <i>tmail</i> may be configured as a drop-in replacement for <i><a href="/docs/linux/man/1-binmail/">binmail</a></i>(1), <i><a href="/docs/linux/man/1-mail-local/">mail.local</a></i>(1) or any program intended for use for mail delivery by a mail delivery program such as <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8). </p>
<p> <i>tmail</i> is intended to be used for direct delivery by the mailer daemon; <i><a href="/docs/linux/man/1-dmail/">dmail</a></i>(1) is the preferred tool for user applications, e.g. a mail delivery filter such as <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1)<i>.</i> If <i>tmail</i> is used for a user application, then the calling program must be aware of the restrictions noted below. </p>
<p> When <i>tmail</i> exits, it returns exit status values to enable the mail delivery program to determine whether a message was delivered successfully or had a temporary (requeue for later delivery) or permanent (return to sender) failure. </p>
<p> If the <i>+folder</i> extension is included in the user argument, <i>tmail</i> will attempt to deliver to the designated folder. If the folder does not exist or the extension is not included, the message is delivered to the user&#8217;s INBOX. If delivery is to INBOX and no INBOX currently exists, <i>tmail</i> will create a new INBOX, using the <code>-I</code> or <code>-b</code> flag if specified. <i>tmail</i> recognizes the format of an existing INBOX or folder, and appends the new message in that format. </p>
<p> The <code>-b</code> flag specifies a format to create INBOX if INBOX does not already exist. This flag requires privileges, and can not be used with <code>-I</code>. The argument is a format name such as mix, mbx, etc. </p>
<p> The <code>-D</code> flag specifies debugging; this enables additional message telemetry. </p>
<p> The <code>-f</code> or <code>-r</code> flag is used by the mail delivery program to specify a Return-Path. The header </p>
<p>Return-Path:&nbsp;<wbr>&lt;<i>from_name</i>&gt;&nbsp;<wbr><br />
 is prepended to the message before delivery. </p>
<p> The <code>-I</code> flag is used by the mail delivery program to specify an alternative INBOX name. This flag requires privileges, and can not be used with <code>-b</code>. This affects the location and format of INBOX. If specified, it should be in one of three forms: </p>
<p> The first form of argument to <code>-I</code> is the string &quot;INBOX&quot;, which means to write to the system default inbox using the system default mailbox format. These system defaults are defined when the c-client library is built. </p>
<p> The second form of argument to <code>-I</code> is a delivery specification, consisting of &quot;#driver.&quot;, a c-client mailbox format driver name, &quot;/&quot;, and a file name. This will write to the specified file in the specified format. For example, #driver.mbx/INBOX will write to file &quot;INBOX&quot; in the home directory in mbx format; and #driver.unix/mail/incoming will write to file &quot;incoming&quot; in the user&#8217;s &quot;mail&quot; subdirectory in unix (default UNIX) format. </p>
<p> The third form of argument to <code>-I</code> is any other name. Normally, this will write to the specified file on the user&#8217;s home directory in the specified format. However, certain names are special. These are: </p>
<pre><code>
value equivalant to-- -- - -- -- -- -- -- -- -INBOX.MTX #driver.mtx / INBOX.MTX mbox #driver.unix / mbox mail.txt #driver.tenex / mail.txt
</code></pre>
<p> If <code>-I</code> is not specified, the default action is <code>-I INBOX</code>. </p>
<p> If multiple recipients are specified on the command line, <i>tmail</i> spawns one child process per recipient to perform actual delivery. This way of calling <i>tmail</i> is not recommended; see below under <i>RESTRICTIONS</i>.</p>
<h2>INSTALLATION</h2>
<p> If <i>tmail</i> is to be used for mail delivery from the mail delivery program, it <i>must</i> be installed setuid root. </p>
<p> If sendmail is the mail delivery program, <i>tmail</i> is invoked from sendmail.cf. Look for the &quot;Mlocal&quot; line, and substitute the path name for the <i>tmail</i> binary in place of /bin/mail, /usr/lib/mail.local, etc. You should also add the flag to invoke <i>tmail</i> with CRLF style newlines; this is usually done with E=
 in the Mlocal line. </p>
<p> Here is an example of an Mlocal line in sendmail version 8: </p>
<pre>
Mlocal, P=/usr/local/etc/tmail, F=lsDFMAw5:/|@qPrn+,
  S=10/30, R=20/40, E=
, T=DNS/RFC822/X-Unix,
  A=tmail $u
</pre>
<p> If <i>tmail</i> is to be called with the <code>-I</code> flag, it must be invoked with both real and effective UID root. Many sendmail configurations invoke the local mailer as the sending user when that user is local, which will prevent <code>-b</code> or <code>-I</code> from working.</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p> If <i>tmail</i> is invoked by an ordinary user, the Received: header line will indicate the name or UID of the user that invoked it. </p>
<p> Ordinary users are not permitted to use the <code>-b</code> or <code>-I</code> flag since otherwise a user could create any file on another user&#8217;s directory. </p>
<p> <i>tmail</i> can deliver mail to home directories. In addition, <i>tmail</i> can be used to deliver mail to other mail folders in a home directory or an inferior directory of a home directory.</p>
<h2>RESTRICTIONS</h2>
<p> The calling program should invoke <i>tmail</i> with CRLF newlines, otherwise <i>tmail</i> will complain in syslog. </p>
<p> Absolute pathnames and <i>~user</i> specifications are not permitted in <i>+folder</i> extensions. </p>
<p> Ordinary users are not permitted to use the <code>-I</code> flag. </p>
<p> IMAP4 namespace names are not yet supported in <i>+folder</i> extensions. </p>
<p> It is not possible to use <i>tmail</i> to deliver to <i><a href="/docs/linux/man/1-mh/">mh</a></i>(1) format mailboxes. </p>
<p> If delivery to multiple users is specified and delivery to any single user fails, the entire delivery will be reported as having failed, even though delivery to other users may have succeeded. If <i>tmail</i> is used for mail delivery from <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8), a separate tmail invocation should be done for each user. Otherwise a delivery failure for a single user in a message going to multiple users will cause multiple deliveries to all the other users every time <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8), retries.</p>
<h2>AUTHOR</h2>
<p> Mark Crispin, MRC [at] CAC.Washington.EDU</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-binmail/">binmail</a>(1)<br />
 <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) </p>
<h2>Index</h2>
