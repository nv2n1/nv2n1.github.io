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
<dt><code>-4</code></p>
<dd>Forces ssmtp to use IPv4 addresses only. </p>
<dt><code>-6</code></p>
<dd>Forces ssmtp to use IPv6 addresses only. </p>
<dt><code>-au</code><i>username</i></p>
<dd>Specifies username for SMTP authentication. </p>
<dt><code>-ap</code><i>password</i></p>
<dd>Specifies password for SMTP authentication. </p>
<dt><code>-am</code><i>mechanism</i></p>
<dd>Specifies mechanism for SMTP authentication. (Only LOGIN and CRAM-MD5) </p>
<dt><code>-ba</code></p>
<dd>(unsupported) ARPANET mode. All input lines must end with a LINEFEED, and all messages will be generated with a CR-LF at the end. Also, the &#8220;From:&#8221; and &#8220;Sender:&#8221; fields are examined for the name of the sender. </p>
<dt><code>-bd </code></p>
<dd>(unsupported) Run as a daemon. </p>
<dt><code>-bi</code></p>
<dd>(ignored) Initialise the alias database. </p>
<dt><code>-bm</code></p>
<dd>(default) Deliver mail in the usual way. </p>
<dt><code>-bp</code></p>
<dd>(simulated) Print a summary of the mail queue. </p>
<dt><code>-bs</code></p>
<dd>(unsupported) Read SMTP commands from stdin. </p>
<dt><code>-bt</code></p>
<dd>(unsupported) Run in address test mode. </p>
<dt><code>-bv</code></p>
<dd>(unsupported) Verify names only. </p>
<dt><code>-bz</code></p>
<dd>(unsupported) Create the configuration freeze file. </p>
<dt><code>-C</code><i>file</i></p>
<dd>Use alternate configuration file. </p>
<dt><code>-d</code><i>X</i></p>
<dd>Set debugging value to X. </p>
<dt><code>-E </code></p>
<dd>(ignored) Don&#8217;t trust userid of sender. </p>
<dt><code>-F</code><i>fullname</i></p>
<dd>Set the full name of the sender. </p>
<dt><code>-f</code><i>name</i></p>
<dd>Sets the name of the &#8220;from&#8221; person. This option is valid only if no From: line is specified within the header of the email. </p>
<dt><code>-h</code><i></i></p>
<dd>(ignored) Set the hop count to N. </p>
<dt><code>-m </code></p>
<dd>(ignored) Ignore originator in alias. </p>
<dt><code>-M</code><i>id</i></p>
<dd>(ignored) Attempt to deliver the queued message with message-id id. </p>
<dt><code>-N</code> <i>dsn</i></p>
<dd>(ignored) Set delivery status notification conditions to dsn. </p>
<dt><code>-n </code></p>
<dd>(default) Do not do aliasing. </p>
<dt><code>-oA</code><i>file</i></p>
<dd>(ignored) Use alternate alias file. </p>
<dt><code>-oc</code></p>
<dd>(ignored) Delay &#8220;expensive&#8221; connections. </p>
<dt><code>-od</code></p>
<dd>(ignored) Set the delivery mode to interactive/synchronous, background or queue (Always interactive). </p>
<dt><code>-oD</code></p>
<dd>(ignored) Run newaliases if required. </p>
<dt><code>-oe</code></p>
<dd>(ignored) Set error processing to mail, write, print or quit. (Always print). </p>
<dt><code>-oF</code><i>mode</i></p>
<dd>(ignored) The mode to use when creating temporary files. </p>
<dt><code>-of</code></p>
<dd>(ignored) Save UNIX-system-style &#8220;From&#8221; lines at the front of messages. </p>
<dt><code>-og</code><i>N</i></p>
<dd>(ignored) Set group ID to use when calling mailers. </p>
<dt><code>-oH</code><i>file</i></p>
<dd>(ignored) Set SMTP help file. </p>
<dt><code>-oi</code></p>
<dd>(default) Do not take dots on a line by themselves as a message terminator. </p>
<dt><code>-oL</code><i>n</i></p>
<dd>(ignored) The log level. </p>
<dt><code>-om</code></p>
<dd>(default) Send to &#8220;me&#8221; (the sender) also if in an alias. </p>
<dt><code>-oo</code></p>
<dd>(unsupported) If set, this message may have old style headers. </p>
<dt><code>-oQ</code><i>queuedir</i></p>
<dd>(ignored) Select the directory in which to queue messages. </p>
<dt><code>-or</code><i>timeout</i></p>
<dd>(ignored) The timeout on reads. </p>
<dt><code>-oS</code><i>file</i></p>
<dd>(ignored) Save statistics in the named file. </p>
<dt><code>-os</code></p>
<dd>(ignored) Always instantiate the queue. </p>
<dt><code>-oT</code><i>time</i></p>
<dd>(ignored) Set timeout on messages. </p>
<dt><code>-ot</code><i>stz,dtz</i></p>
<dd>(ignored) Set the name of the time zone. </p>
<dt><code>-ou</code><i>N</i></p>
<dd>(ignored) Set the default user id for mailers. </p>
<dt><code>-q</code><i>[time]</i></p>
<dd>(simulated) Process the queue. </p>
<dt><code>-r</code><i>name</i></p>
<dd>Same as -f. </p>
<dt><code>-R</code><i>string</i></p>
<dd>(ignored) Process queue for recipient. </p>
<dt><code>-R</code> <i>return</i></p>
<dd>(ignored) Set the amount of the message to be returned if the message bounces. </p>
<dt><code>-t</code></p>
<dd>Read message, searching for recipients. &#8220;To:&#8221;, `Cc:&#8221;, and &#8220;Bcc:&#8221; lines will be scanned for people to send to. Any addresses in the argument list will be suppressed (not supported). </p>
<dt><code>-v</code></p>
<dd>Go into verbose mode. </p>
<dt><code>-V</code></p>
<dd>Say version and quit. </p>
</dl>
<h2>Reverse Aliases</h2>
<p>A reverse alias gives the From: address placed on a user&#8217;s outgoing messages and (optionally) the mailhub these messages will be sent through. Example: </p>
<dl>
<dd>
<pre>root:jdoe [at] isp.com:mail.isp.com</pre>
</dl>
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
