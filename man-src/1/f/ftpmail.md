---
title: "ftpmail(1)"
name: "ftpmail"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftpmail/"
description: "ftpmail – FIFO-based Perl script for sending email based on proftpd TransferLog"
---

<h2 class="name">NAME</h2>
<p> ftpmail &#8211; FIFO-based Perl script for sending email based on proftpd TransferLog </p>
<h2>SYNOPSIS</h2>
<p> <code>ftpmail</code> [ <code>&#8211;help</code> ] [ <code>&#8211;fifo</code> <i>fifo-path</i> ] [ <code>&#8211;from</code> <i>email-address</i> ] [ <code>&#8211;log</code> <i>xferlog-file</i> ] [ <code>&#8211;recipient</code> <i>email-address</i> ] [ <code>&#8211;subject</code> <i>email-subject</i> ] [ <code>&#8211;smtp-server</code> <i>server-address</i> ] [ <code>&#8211;attach-file</code> ] [ <code>&#8211;auth</code> <i>smtp-auth-info-file</i> ] [ <code>&#8211;ignore-users</code> <i>regex-pattern</i> ] [ <code>&#8211;watch-users</code> <i>regex-pattern</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ftpmail</code> is a Perl script designed to read ProFTPD&#8217;s <i>TransferLog</i> log entries, watching for uploads, and to send an automatic email notification when uploads occur. To use <code>ftpmail</code> , you configure your <code>proftpd</code> daemon to write its <i>TransferLog</i> to a FIFO; the <code>ftpmail</code> program is a FIFO reading program which then processes those log messages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display a short usage description, including all available options.</p>
<dt><code>&#8211;attach-file</code></p>
<dd> If used, this will cause a copy of the uploaded file to be included, as an attachment, in the generated email.</p>
<dt><code>&#8211;auth</code><i> smtp-auth-info-file</i></p>
<dd> Configures the path to a file containing SMTP authentication information. The configured file should look like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>user</code></p>
<dd> username</p>
<dt><code>password</code></p>
<dd> password</dl>
</dl>
</dl>
<dt><code>&#8211;fifo</code><i> fifo-path</i></p>
<dd> Indicates the path to the FIFO to which <code>proftpd</code> is writing its <code>TransferLog</code>. That is, this is the path that you used for the <code>TransferLog</code> directive in your <i>proftpd.conf</i>. This parameter is <code>REQUIRED.</code></p>
<dt><code>&#8211;from</code><i> email-address</i></p>
<dd> Specifies the email address to use in the <i>From</i> email header. This parameter is <code>REQUIRED.</code></p>
<dt><code>&#8211;ignore-users</code><i> regex-pattern</i></p>
<dd> Specifies a Perl regular expression. If the uploading user name matches this regular expression, then an email notification is <code>NOT</code> sent; otherwise, an email is sent.</p>
<dt><code>&#8211;log</code><i> xferlog-path</i></p>
<dd> Since this script reads the <code>TransferLog</code> using FIFOs, the actual <code>TransferLog</code> file is not written by default. Use this option to write the normal <code>TransferLog</code> file, in addition to watching for uploads.</p>
<dt><code>&#8211;recipient</code><i> email-address</i></p>
<dd> Specifies an email address to which to send an email notification of the upload. This option can be used multiple times to specify multiple recipients. <code>AT LEAST ONE</code> recipient is <code>REQUIRED.</code></p>
<dt><code>&#8211;smtp-server</code><i> server-address</i></p>
<dd> Specifies the SMTP server to which to send the email. This parameter is <code>REQUIRED.</code></p>
<dt><code>&#8211;subject</code><i> subject</i></p>
<dd> Specify a custom <i>Subject</i> email header for the email sent. The default <i>Subject</i> is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>User &#8216;<i>$user</i>&#8216; uploaded file &#8216;<i>$file</i>&#8216; via FTP</p>
<dd></dl>
</dl>
</dl>
<dt><code>&#8211;watch-users</code><i> regex-pattern</i></p>
<dd> Specifies a Perl regular expression. If the uploading user name matches this regular expression, then an email notification is sent; otherwise, no email is sent.</dl>
<h2>FILES</h2>
<p> <code>/var/log/xferlog</code></p>
<h2>AUTHORS</h2>
<p> ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code> <code><a href="/docs/linux/man/5-xferlog/">xferlog</a>(5)</code> </p>
<p> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> </p>
<p> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> </p>
<p> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
<h2>Index</h2>
