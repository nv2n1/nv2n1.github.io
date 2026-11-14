---
title: "esmtp(1)"
name: "esmtp"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esmtp/"
description: "esmtp – libESMTP to Sendmail compatibility interface"
---

<h2 class="name">NAME</h2>
<p> esmtp &#8211; libESMTP to Sendmail compatibility interface</p>
<h2>SYNOPSIS</h2>
<p> <code>esmtp</code> [<i>flags</i>] [<i>address &#8230;</i>]<br />
 <code>sendmail</code> [<i>flags</i>] [<i>address &#8230;</i>] </p>
<p> <code>mailq</code><br />
 <code>sendmail -bp</code> </p>
<p> <code>newaliases</code><br />
 <code>sendmail -bi</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Esmtp</code> is a send-only <code>sendmail</code> emulator for machines which normally retrieve their mail from a centralized mailhub using programs such as <code>fetchmail</code>. </p>
<p> <code>Esmtp</code> does not attempt to provide all the functionality of <code>sendmail</code>: it is intended to be used by mail user agents as <code>mutt</code>. </p>
<h2>OPTIONS</h2>
<p> Most <code>sendmail</code> options are irrelevant to <code>esmtp</code> . Those marked &#8220;ignored&#8221; or &#8220;default&#8221; have no effect on mail transfer. Those marked &#8220;unsupported&#8221; are fatal errors. </p>
<dl>
<dt><code>-Ac</code> (ignored)</p>
<dd> Use submit.cf even if the operation mode does not indicate an initial mail submission. </p>
<dt><code>-Am</code> (ignored)</p>
<dd> Use sendmail.cf even if the operation mode indicates an initial mail submission. </p>
<dt><code>-B</code> <i>type</i></p>
<dd> Set the body type to <i>type</i>. Current legal values are 7BIT or 8BITMIME. </p>
<dt><code>-ba</code> (unsupported)</p>
<dd> Go into ARPANET mode. </p>
<dt><code>-bd</code> (unsupported)</p>
<dd> Run as a daemon. </p>
<dt><code>-bD</code> (unsupported)</p>
<dd> Same as <code>-bd</code> except runs in foreground. </p>
<dt><code>-bh</code> (unsupported)</p>
<dd> Print the persistent host status database. </p>
<dt><code>-bH</code> (unsupported)</p>
<dd> Purge expired entries from the persistent host status database. </p>
<dt><code>-bi</code> (ignored)</p>
<dd> Initialize the alias database. </p>
<dt><code>-bm</code> (default)</p>
<dd> Deliver mail in the usual way. </p>
<dt><code>-bp</code></p>
<dd> Print a listing of the queue(s). </p>
<dt><code>-bP</code> (unsupported)</p>
<dd> Print number of entries in the queue(s); only available with shared memory support. </p>
<dt><code>-bs</code> (unsupported)</p>
<dd> Use the SMTP protocol as described in RFC821 on standard input and output. </p>
<dt><code>-bt</code> (unsupported)</p>
<dd> Run in address test mode. </p>
<dt><code>-bv</code> (unsupported)</p>
<dd> Verify names only &#8211; do not try to collect or deliver a message. </p>
<dt><code>-C</code> <i>file</i></p>
<dd> Use alternate configuration file. </p>
<dt><code>-d</code> <i>X</i> (ignored)</p>
<dd> Set debugging value to <i>X</i>. </p>
<dt><code>-F</code> <i>fullname</i></p>
<dd> Set the full name of the sender. </p>
<dt><code>-f</code> <i>name</i></p>
<dd> Sets the name of the &#8220;from&#8221; person (i.e., the envelope sender of the mail). This address may also be used in the From: header if that header is missing during initial submission. The envelope sender address is used as the recipient for delivery status notifications and may also appear in a Return-Path: header. </p>
<p> This address is also used to select from different identities in the configuration file. </p>
<p> If no envelope sender is specified in the command line then the default identity&#8217;s address is used. </p>
<dt><code>-G</code> (ignored)</p>
<dd> Relay (gateway) submission of a message. </p>
<dt><code>-h</code> <i>N</i> (ignored)</p>
<dd> Set the hop count to <i>N</i>. </p>
<dt><code>-I</code> (ignored)</p>
<dd> Same as <code>-bi</code>. </p>
<dt><code>-i</code> (ignored)</p>
<dd> Ignore dots alone on lines by themselves in incoming messages. This should be set if you are reading data from a file. </p>
<dt><code>-L</code> <i>tag</i> (ignored)</p>
<dd> Set the identifier used in syslog messages to the supplied <i>tag</i>. </p>
<dt><code>-N</code> <i>dsn</i></p>
<dd> Set delivery status notification conditions to <i>dsn</i>, which can be `never&#8217; for no notifications or a comma separated list of the values `failure&#8217; to be notified if delivery failed, `delay&#8217; to be notified if delivery is delayed, and `success&#8217; to be notified when the message is successfully delivered. </p>
<dt><code>-n</code> (default)</p>
<dd> Don&#8217;t do aliasing. </p>
<dt><code>-O</code> <i>option</i>=<i>value</i> (ignored)</p>
<dd> Set option <i>option</i> to the specified <i>value</i>. This form uses long names. </p>
<dt><code>-o</code> <i>x value</i> (ignored)</p>
<dd> Set option <i>x</i> to the specified <i>value</i>. This form uses single character names only. </p>
<dt><code>-p</code> <i>protocol</i> (ignored)</p>
<dd> Set the name of the protocol used to receive the message. </p>
<dt><code>-q</code>[<i>time</i>] (ignored)</p>
<dd> Process saved messages in the queue at given intervals. </p>
<dt><code>-qp</code>[<i>time</i>] (ignored)</p>
<dd> Similar to <code>-q</code><i>time</i>, except that instead of periodically forking a child to process the queue, forks a single persistent child for each queue that alternates between processing the queue and sleeping. </p>
<dt><code>-qf</code> (ignored)</p>
<dd> Process saved messages in the queue once and do not fork(), but run in the foreground. </p>
<dt><code>-qG</code> <i>name</i> (ignored)</p>
<dd> Process jobs in queue group called <i>name</i> only. </p>
<dt><code>-q</code>[<i>!</i>]<code>I</code> <i>substr</i> (ignored)</p>
<dd> Limit processed jobs to those containing <i>substr</i> as a substring of the queue id or not when <i>!</i> is specified. </p>
<dt><code>-q</code>[<i>!</i>]<code>R</code> <i>substr</i> (ignored)</p>
<dd> Limit processed jobs to those containing <i>substr</i> as a substring of one of the recipients or not when <i>!</i> is specified. </p>
<dt><code>-q</code>[<i>!</i>]<code>S</code> <i>substr</i> (ignored)</p>
<dd> Limit processed jobs to those containing <i>substr</i> as a substring of the sender or not when <i>!</i> is specified. </p>
<dt><code>-R</code> <i>return</i></p>
<dd> Set the amount of the message to be returned if the message bounces. The <i>return</i> parameter can be `full&#8217; to return the entire message or `hdrs&#8217; to return only the headers. In the latter case also local bounces return only the headers. </p>
<dt><code>-r</code> <i>name</i></p>
<dd> An alternate and obsolete form of the <code>-f</code> flag. </p>
<dt><code>-t</code></p>
<dd> Read message for recipients. To:, Cc:, and Bcc: lines will be scanned for recipient addresses. The Bcc: line will be deleted before transmission. </p>
<dt><code>-V</code> <i>envid</i></p>
<dd> Set the original envelope id. </p>
<dt><code>-v</code></p>
<dd> Go into verbose mode. </p>
<dt><code>-X</code> <i>logfile</i></p>
<dd> Log all traffic in and out of mailers in the indicated log file. </p>
<dt><code>&#8212;</code></p>
<dd> Stop processing command flags and use the rest of the arguments as addresses. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr>~/.esmtprc</p>
<dd> User configuration file. Only read if no configuration file is specified on the command line. </p>
<dt>/etc/esmtprc</p>
<dd> System configuration file. Only read if no configuration file is specified on the command line and there is no user configuration file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-esmtprc/">esmtprc</a>(5), <a href="/docs/linux/man/1-fetchmail/">fetchmail</a>(1) </p>
<h2>AUTHOR</h2>
<p> Jos&eacute; Fonseca </p>
<h2>Index</h2>
