---
title: "bsmtp(1)"
name: "bsmtp"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsmtp/"
description: "bsmtp – Bacula’s SMTP client (mail submission program)"
---

<h2 class="name">NAME</h2>
<p>&nbsp;<wbr>bsmtp &#8211; Bacula&#8217;s SMTP client&nbsp;<wbr>(mail submission program)</p>
<h2>SYNOPSIS</h2>
<p> <code>bsmtp</code> [<i>options</i>] <i>&lt;recipient&gt; &lt;&#8230;&gt;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>bsmtp</code> is a simple mail user agent designed to permit more flexibility than the standard mail programs typically found on Unix systems, and to ease portability. It can even run on Windows machines. It is used by the Director daemon to send notifications and requests to the operator. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> Forces bsmtp to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd> Forces bsmtp to use IPv6 addresses only.</p>
<dt><code>-8</code></p>
<dd> Encode the mail in UTF-8.</p>
<dt><code>-a</code></p>
<dd> Use any ip protocol for address resolution.</p>
<dt><code>-c</code></p>
<dd> Set the <code>Cc:</code> header.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd> Set debug level to <i>nn</i>.</p>
<dt><code>-dt</code></p>
<dd> Print timestamp in debug output.</p>
<dt><code>-f</code></p>
<dd> Set the <code>From:</code> header. If not specified, <code>bsmtp</code> will try to use your username.</p>
<dt><code>-h&nbsp;<wbr></code><i>mailhost:port</i></p>
<dd> Use mailhost:port as the SMTP server. (default port: 25)</p>
<dt><code>-s</code></p>
<dd> Set the <code>Subject:</code> header.</p>
<dt><code>-r</code></p>
<dd> Set the <code>Reply-To:</code>: header.</p>
<dt><code>-l</code></p>
<dd> Set the maximum number of lines to be sent. (default: unlimited)</p>
<dt><code>-?</code></p>
<dd> Show version and usage of program. </p>
</dl>
<h2>USAGE</h2>
<p> <i>recipients</i> is a space separated list of email addresses. </p>
<p> The body of the email message is read from standard input. Message is ended by sending the EOF character (Ctrl-D on many systems) on the start of a new line, much like many &#8216;mail&#8217; commands. </p>
<p> The actual, automated behavior of <code>bsmtp</code> will depend on the mail-related configuration of the Director in the <i>Messages</i> resource of <i>bacula-dir.conf</i>. </p>
<p> Interactive use of <code>bsmtp</code> is pertinent to manually test and ensure these configuration bits are valid. This is highly recommended. </p>
<h2>CONFIGURATION</h2>
<p> These commands should each appear on a single line in the configuration file. </p>
<p> Messages {<br />
&nbsp;<wbr>&nbsp;<wbr>Name&nbsp;<wbr>=&nbsp;<wbr>Standard<br />
&nbsp;<wbr>&nbsp;<wbr>mailcommand&nbsp;<wbr>=&nbsp;<wbr>&quot;/home/bacula/bin/bsmtp -h mail.domain.com -f&nbsp;<wbr>\&quot;\(Bacula\)&nbsp;<wbr>\&lt;%r\&gt;\&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-s&nbsp;<wbr>\&quot;Bacula:&nbsp;<wbr>%t&nbsp;<wbr>%e of&nbsp;<wbr>%c&nbsp;<wbr>%l\&quot;&nbsp;<wbr>%r&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>operatorcommand&nbsp;<wbr>=&nbsp;<wbr>&quot;/home/bacula/bin/bsmtp -h mail.domain.com -f&nbsp;<wbr>\&quot;\(Bacula\)&nbsp;<wbr>\&lt;%r\&gt;\&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-s&nbsp;<wbr>\&quot;Bacula: Intervention needed for&nbsp;<wbr>%j\&quot;&nbsp;<wbr>%r&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>mail&nbsp;<wbr>=&nbsp;<wbr>sysadmin [at] site.domain.com&nbsp;<wbr>=&nbsp;<wbr>all,&nbsp;<wbr>!skipped<br />
&nbsp;<wbr>&nbsp;<wbr>operator&nbsp;<wbr>=&nbsp;<wbr>sysop [at] site.domain.com&nbsp;<wbr>=&nbsp;<wbr>mount<br />
&nbsp;<wbr>&nbsp;<wbr>console&nbsp;<wbr>=&nbsp;<wbr>all,&nbsp;<wbr>!skipped,&nbsp;<wbr>!saved<br />
&nbsp;<wbr>} </p>
<p> <i>home/bacula/bin</i> is replaced with the path to the Bacula binary directory, and mail.domain.com is replaced with the fully qualified name of an SMTP server, which usually listen on port 25. </p>
<h2>ENVIRONMENT</h2>
<p> If the <code>-h</code> option is not specified, <code>bsmtp</code> will use environment variable <code>SMTPSERVER</code>, or &#8216;localhost&#8217; if not set. </p>
<h2>NOTES</h2>
<p> Since <code>bsmtp</code> always uses a TCP connection rather than writing to a spool file, you may find that your <code>From:</code> address is being rejected because it does not contain a valid domain, or because your message has gotten caught in spam filtering rules. Generally, you should specify a fully qualified domain name in the from field, and depending on whether your SMTP gateway is Exim or Sendmail, you may need to modify the syntax of the from part of the message. </p>
<p> If <code>bsmtp</code> cannot connect to the specified mail host, it will retry to connect to <code>localhost</code>. </p>
<h2>BUGS</h2>
<p> If you are getting incorrect dates (e.g. 1970) and you are running with a non-English locale, you might try setting the <code>LANG=&quot;en_US&quot;</code> environment variable. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;, revised and edited by Lucas B. Cohen &lt;lbc [at] members.fsf.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-bacula-dir/">bacula-dir</a></code>(8) </p>
<h2>Index</h2>
