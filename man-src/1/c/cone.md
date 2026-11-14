---
title: "cone(1)"
name: "cone"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cone/"
description: "cone – Read and send E-mail messages"
---

<h2 class="name">NAME</h2>
<p> cone &#8211; Read and send E-mail messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cone</code> [-r] [-c&nbsp;<wbr><i>directory</i>]</dl>
<h2>USAGE</h2>
<dd>Cone is a console newsreader and E-mail. It is an interactive program for reading and sending E-mail messages. Cone is designed to be intuitive and easy to learn. Starting Cone for the first time displays two links: one for the default system mailbox, and a second link to a quick online tutorial. The online tutorial provides a brief overview of using Cone for reading and sending E-mail. </p>
<p> Pressing Q on most screens exits Cone. Cone tries to gracefully log out and shut down all server connections. If Cone cannot log out of a remote server because the remote server is down, press CTRL-C (after Q to terminate Cone). </p>
<p> Use CTRL-Z to temporarily suspend Cone and drop back to the shell prompt. Cone remains suspended in the background, and may be restarted by using the shell&#8217;s <code>fg</code> command. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Connections to remote mail servers may be disconnected for inactivity if Cone remains suspended for a prolonged period of time. When suspended, Cone cannot maintain any active connections to remote mail servers. </p>
</dl>
<p> The <code>-c</code> option names a directory where Cone saves its configuration files, and defaults to $HOME/.cone. The configuration directory will be created, if necessary. </p>
<p> The <code>-r</code> option recovers a backup copy of Cone&#8217;s configuration file. This option is primarily used when remote configuration is enabled, but the folder that contains Cone&#8217;s configuration on a remote server was deleted, or is not available. In all cases, Cone makes a daily local configuration file backup. The <code>-r</code> option searches for local configuration file backups, and offers an option to restore the backup copy.</p>
<h3>Reading local mail with Cone</h3>
<p> Cone reads local mail from either maildirs (the preferred format) or mailbox files (or &quot;mboxes&quot;). When mboxes are used, Cone does not read the system mailbox file directly (usually /var/spool/<i>something</i>). All messages in the system mailbox are automatically moved to $HOME/Inbox, which is then accessed as if it was the system mailbox. Starting Cone for the first time on an mbox-based system automatically copies all existing mail from the system mailbox file to $HOME/Inbox. </p>
<p> This is an intentional design choice. Normal user application cannot create new files in /var/spool; all they can do is read the mailbox file from /var/spool. Therefore, the only way to update the mailbox file is by rewriting it from scratch (more or less). While the mailbox file is in the process of being rewritten, if the Cone process is interrupted, or killed, the resulted in a corrupted system mailbox. There are way to minimize this vulnerability, but it cannot be eliminated completely. Some Linux kernels use an &#8220;OOM killer&#8221; that may terminate any process when the system memory is low. There is no way to completely prevent corrupted system mailbox files on those kernels. </p>
<p> Cone uses an alternative way of updating mboxes. Cone updates mboxes by creating a new mbox file separately, then replacing the original mbox file with the new version. Unfortunately this cannot be done with the system mailbox file, because of the restricted access rights on the system spool directory. To solve this problem Cone automatically copies the system mailbox file to $HOME/Inbox, each time the system mailbox file is opened and whenever new mail is available.</p>
<h3>Viewing MIME attachments</h3>
<p> Cone displays text and simple HTML content by itself. Other kinds of attachments may be viewed by using a helper script. Cone invokes a helper script to open a MIME attachment. The helper script&#8217;s name is &#8220;<i>TYPE</i>.<i>SUBTYPE</i>.filter&#8221;, where &#8220;TYPE&#8221; and &#8220;SUBTYPE&#8221; corresponds to the MIME type and subtype, accordingly. Cone looks for helper scripts in $HOME/.cone (or the directory specified by <code>-c</code>) and in /usr/share/cone. </p>
<p> For example, a helper script named &#8220;IMAGE.GIF.filter&#8221;, if installed, is invoked to process image/gif MIME attachments. </p>
<p> <font SIZE="+1"> <code>Helper scripts</code></p>
<dl>
<dt>
<dd>
<p> Cone runs each helper script twice: </p>
<dl>
<dt>
<dd> </font></p>
<pre>
TYPE.SUBTYPE.filter check <i>type/subtype</i>
</pre>
</dl>
<p> When the first argument is &#8220;check&#8221;, the helper script should terminate with a zero exit code if it is willing to process an attachment whose MIME type is specified by the second argument. A script or a program that&#8217;s has multiple &#8220;TYPE.SUBTYPE.filter&#8221; links may use the second argument to identify the attachment&#8217;s mime type. If the helper script is unable to process the attachment, at this time, it should terminate with a non-zero exit code. </p>
<p> The default helper script for image attachments terminates with a non-zero exit code if the <code>DISPLAY</code> environment variable is not initialized. When invoked from an X-Windows terminal, image attachments will be automatically displayed; and image attachments are ignored otherwise on non-graphical consoles. </p>
<dl>
<dt>
<dd>
<pre>
TYPE.SUBTYPE.filter filter <i>type/subtype</i> <i>filename</i>
</pre>
</dl>
<p> If the helper script initially terminates with a zero exit code, it will be invoked again after the MIME attachment is downloaded and decoded. The first argument will be &#8220;filter&#8221;, and the attachment&#8217;s filename is specified by the third argument. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> This is a temporary file, whose extension will not necessary be the file extension associated with this MIME type. </p>
</dl>
<p> The helper script should read and process the file specified by the third argument. Cone interprets anything the helper script writes to standard output as HTML. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Cone waits until the helper script terminates before displaying the rest of the message. Most helper scripts should run in the background. However, note that Cone removes the temporary file when the original message is closed; the temporary file may be removed any time after the helper script terminates. The helper script should make its own private copy of the file, if necessary. </p>
</dl>
</dl>
<h3>Activating URLs</h3>
<p> Cone has limited ability to activate URLs in HTML messages. Cone handles &#8220;mailto:&#8221;URLs by itself. For other URLs Cone runs /usr/share/cone/<i>method</i>.handler with the URL passed as an argument. </p>
<p> Cone installs http.handler (hard linked to https.handler). This script checks if firefox or mozilla binaries are found in the current <code>PATH</code>, and runs them. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Cone also looks <i>method</i>.handler in $HOME/.cone (or the directory specified by <code>-c</code>) in addition to /usr/share/cone. </p>
</dl>
<h2>FILES</h2>
<p> $HOME/.cone</p>
<dl>
<dt>
<dd> Configuration files, and other application data. May be modified by the <code>-c</code> option.</dl>
<p> /usr/share/cone/IMAGE.GIF.filter, /usr/share/cone/IMAGE.JPEG.filter, /usr/share/cone/IMAGE.PNG.filter, /usr/share/cone/APPLICATION.PDF.filter</p>
<dl>
<dt>
<dd> Default helper scripts distributed with Cone.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mailtool/">mailtool</a></code>(1), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd></dl>
<h2>Index</h2>
