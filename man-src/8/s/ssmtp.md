---
title: "ssmtp(8)"
name: "ssmtp"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ssmtp/"
description: "ssmtp, sendmail – send a message using smtp"
---

<p>ssmtp, sendmail &#8211; send a message using smtp</p>
<h2>Synopsis</h2>
<p><code>ssmtp</code> [ <i>flags</i> ] [ <i>address</i> <i>&#8230;</i> ]<br />
 <code>/usr/lib/sendmail</code> [ <i>flags</i> ] [ <i>address</i> <i>&#8230;</i> ]</p>
<h2>Description</h2>
<p><i>ssmtp</i> is a send-only sendmail emulator for machines which normally pick their mail up from a centralized mailhub (via pop, imap, nfs mounts or other means). It provides the functionality required for humans and programs to send mail via the standard or /usr/bin/mail user agents. It accepts a mail stream on standard input with recipients specified on the command line and synchronously forwards the message to the mail transfer agent of a mailhub for the mailhub MTA to process. Failed messages are placed in dead.letter in the sender&#8217;s home directory. Config files allow one to specify the address to receive mail from root, daemon, etc.; a default mailhub; a default domain to be used in From: lines; per-user From: addresses and mailhub names; and aliases in the traditional format used by sendmail for the /etc/aliases file. It does not attempt to provide all the functionality of sendmail: it is intended for use where other programs are the primary means of at last mail delivery. It is usefull with pop/imap, or to simulate the Sun shared mail spool option for non-Sun machines, for machines whose sendmails are too difficult (or various) to configure, for machines with known disfeatures in their sendmails or for ones where there are &#8220;mysterious problems&#8221;. It does not honor .forwards, which have to be done on the recieving host. It especially does not deliver to pipelines. </p>
<h2>Options</h2>
<p>Most sendmail options are irrelevent to sSMTP. Those marked &#8220;ignored&#8221; or &#8220;default&#8221; have no effect on mail transfer. Those marked &#8220;unsupported&#8221; are fatal errors. Those marked &#8220;simulated&#8221; are not errors, but the result is for the program to exit with an informative message. A sort of fatal non-error. </p>
<dl>
<dt><code>-4</code></dt>
<dd>Forces ssmtp to use IPv4 addresses only. </dd>
<dt><code>-6</code></dt>
<dd>Forces ssmtp to use IPv6 addresses only. </dd>
<dt><code>-au</code><i>username</i></dt>
<dd>Specifies username for SMTP authentication. </dd>
<dt><code>-ap</code><i>password</i></dt>
<dd>Specifies password for SMTP authentication. </dd>
<dt><code>-am</code><i>mechanism</i></dt>
<dd>Specifies mechanism for SMTP authentication. (Only LOGIN and CRAM-MD5) </dd>
<dt><code>-ba</code></dt>
<dd>(unsupported) ARPANET mode. All input lines must end with a LINEFEED, and all messages will be generated with a CR-LF at the end. Also, the &#8220;From:&#8221; and &#8220;Sender:&#8221; fields are examined for the name of the sender. </dd>
<dt><code>-bd </code></dt>
<dd>(unsupported) Run as a daemon. </dd>
<dt><code>-bi</code></dt>
<dd>(ignored) Initialise the alias database. </dd>
<dt><code>-bm</code></dt>
<dd>(default) Deliver mail in the usual way. </dd>
<dt><code>-bp</code></dt>
<dd>(simulated) Print a summary of the mail queue. </dd>
<dt><code>-bs</code></dt>
<dd>(unsupported) Read SMTP commands from stdin. </dd>
<dt><code>-bt</code></dt>
<dd>(unsupported) Run in address test mode. </dd>
<dt><code>-bv</code></dt>
<dd>(unsupported) Verify names only. </dd>
<dt><code>-bz</code></dt>
<dd>(unsupported) Create the configuration freeze file. </dd>
<dt><code>-C</code><i>file</i></dt>
<dd>Use alternate configuration file. </dd>
<dt><code>-d</code><i>X</i></dt>
<dd>Set debugging value to X. </dd>
<dt><code>-E </code></dt>
<dd>(ignored) Don&#8217;t trust userid of sender. </dd>
<dt><code>-F</code><i>fullname</i></dt>
<dd>Set the full name of the sender. </dd>
<dt><code>-f</code><i>name</i></dt>
<dd>Sets the name of the &#8220;from&#8221; person. This option is valid only if no From: line is specified within the header of the email. </dd>
<dt><code>-h</code><i></i></dt>
<dd>(ignored) Set the hop count to N. </dd>
<dt><code>-m </code></dt>
<dd>(ignored) Ignore originator in alias. </dd>
<dt><code>-M</code><i>id</i></dt>
<dd>(ignored) Attempt to deliver the queued message with message-id id. </dd>
<dt><code>-N</code> <i>dsn</i></dt>
<dd>(ignored) Set delivery status notification conditions to dsn. </dd>
<dt><code>-n </code></dt>
<dd>(default) Do not do aliasing. </dd>
<dt><code>-oA</code><i>file</i></dt>
<dd>(ignored) Use alternate alias file. </dd>
<dt><code>-oc</code></dt>
<dd>(ignored) Delay &#8220;expensive&#8221; connections. </dd>
<dt><code>-od</code></dt>
<dd>(ignored) Set the delivery mode to interactive/synchronous, background or queue (Always interactive). </dd>
<dt><code>-oD</code></dt>
<dd>(ignored) Run newaliases if required. </dd>
<dt><code>-oe</code></dt>
<dd>(ignored) Set error processing to mail, write, print or quit. (Always print). </dd>
<dt><code>-oF</code><i>mode</i></dt>
<dd>(ignored) The mode to use when creating temporary files. </dd>
<dt><code>-of</code></dt>
<dd>(ignored) Save UNIX-system-style &#8220;From&#8221; lines at the front of messages. </dd>
<dt><code>-og</code><i>N</i></dt>
<dd>(ignored) Set group ID to use when calling mailers. </dd>
<dt><code>-oH</code><i>file</i></dt>
<dd>(ignored) Set SMTP help file. </dd>
<dt><code>-oi</code></dt>
<dd>(default) Do not take dots on a line by themselves as a message terminator. </dd>
<dt><code>-oL</code><i>n</i></dt>
<dd>(ignored) The log level. </dd>
<dt><code>-om</code></dt>
<dd>(default) Send to &#8220;me&#8221; (the sender) also if in an alias. </dd>
<dt><code>-oo</code></dt>
<dd>(unsupported) If set, this message may have old style headers. </dd>
<dt><code>-oQ</code><i>queuedir</i></dt>
<dd>(ignored) Select the directory in which to queue messages. </dd>
<dt><code>-or</code><i>timeout</i></dt>
<dd>(ignored) The timeout on reads. </dd>
<dt><code>-oS</code><i>file</i></dt>
<dd>(ignored) Save statistics in the named file. </dd>
<dt><code>-os</code></dt>
<dd>(ignored) Always instantiate the queue. </dd>
<dt><code>-oT</code><i>time</i></dt>
<dd>(ignored) Set timeout on messages. </dd>
<dt><code>-ot</code><i>stz,dtz</i></dt>
<dd>(ignored) Set the name of the time zone. </dd>
<dt><code>-ou</code><i>N</i></dt>
<dd>(ignored) Set the default user id for mailers. </dd>
<dt><code>-q</code><i>[time]</i></dt>
<dd>(simulated) Process the queue. </dd>
<dt><code>-r</code><i>name</i></dt>
<dd>Same as -f. </dd>
<dt><code>-R</code><i>string</i></dt>
<dd>(ignored) Process queue for recipient. </dd>
<dt><code>-R</code> <i>return</i></dt>
<dd>(ignored) Set the amount of the message to be returned if the message bounces. </dd>
<dt><code>-t</code></dt>
<dd>Read message, searching for recipients. &#8220;To:&#8221;, `Cc:&#8221;, and &#8220;Bcc:&#8221; lines will be scanned for people to send to. Any addresses in the argument list will be suppressed (not supported). </dd>
<dt><code>-v</code></dt>
<dd>Go into verbose mode. </dd>
<dt><code>-V</code></dt>
<dd>Say version and quit. </dd>
</dl>
<h2>Reverse Aliases</h2>
<p>A reverse alias gives the From: address placed on a user&#8217;s outgoing messages and (optionally) the mailhub these messages will be sent through. Example: </p>
<dl>
<dd>
<pre>root:jdoe [at] isp.com:mail.isp.com</pre>
</dd></dl>
<p> Messages root sends will be identified as from jdoe [at] isp.com and sent through mail.isp.com.</p>
<h2>Files</h2>
<p>&nbsp;<wbr>/etc/ssmtp/ssmtp.conf &#8211; configuration file </p>
<p>&nbsp;<wbr>/etc/ssmtp/revaliases &#8211; reverse aliases file </p>
<p>&nbsp;<wbr>/etc/aliases &#8211; aliases file</p>
<h2>See Also</h2>
<p>RFC821, RFC822, <a href="/docs/linux/man/5-ssmtp-conf/">ssmtp.conf</a>(5). </p>
<h2>Authors</h2>
<p>Matt Ryan (mryan [at] debian.org) Hugo Haas (hugo [at] debian.org) Christoph Lameter (clameter [at] debian.org) Dave Collier-Brown (davecb [at] hobbes.ss.org)</p>
<h2>Bugs</h2>
<p>sSMTP does not support exception lists to the -t option (never seen it used). sSMTP will fail if the mailhub is unreachable. </p>
