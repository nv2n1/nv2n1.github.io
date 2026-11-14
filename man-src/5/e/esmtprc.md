---
title: "esmtprc(5)"
name: "esmtprc"
section: "5"
letter: "e"
url: "/docs/linux/man/5-esmtprc/"
description: "esmtprc – esmtp configuration file."
---

<p>esmtprc &#8211; <code>esmtp</code> configuration file.</p>
<h2>Description</h2>
<p>A <code>esmtp</code> configuration file consists of several options. The options format is: </p>
<pre> <i>keyword</i>=<i>value</i></pre>
<p>The equal sign is optional and can be replaced by whitespace. The <i>value</i> may be enclosed in simple or double quotes, in which case special characters can be escaped as in normal C strings. Comments are delimited by the &#8216;#&#8217; character up to the newline character. </p>
<h2>Options</h2>
<dl>
<dt><code>hostname</code></p>
<dd>Set SMTP host and service (port). </p>
<p> The format is: </p>
<pre> host.example.org[:<i>service</i>]</pre>
<p>With no whitespace surrounding the colon if service is specified. <i>service</i> may be a name from /etc/services or a decimal port number. If not specified the port defaults to 587. </p>
<p> Note (from <code>libESMTP</code> documentation): the default port number is set to 587 since this is the port that should be used for mail submission, see RFC 2476. By choosing this default now, the API does not change behavior unexpectedly in the future as use of the new standard becomes commonplace. The host-port notation simplifies things for the application, the user can type &quot;localhost:smtp&quot; or &quot;localhost:25&quot; where the application expects a host name. </p>
<dt><code>username</code></p>
<dd>Set the username for authentication with the SMTP server. </p>
<p> Do NOT set the username and password in the system configuration file unless you are the only user of this machine. <code>Esmtp</code> is not run with suid privileges therefore the system configuration file must be readable by everyone. If your SMTP server requires authentication and you are not the only user then specify your personal SMTP account details in the user configuration file. </p>
<dt><code>password</code></p>
<dd>Set the password for authentication with the SMTP server. </p>
<dt><code>starttls</code></p>
<dd>Whether to use the StartTLS extension. </p>
<p> It can be one of <code>enabled</code>, <code>disabled</code> or <code>required</code>. It defaults to <code>disabled</code>. </p>
<dt><code>certificate_passphrase</code></p>
<dd>Set the certificate passphrase for the StartTLS extension. </p>
<dt><code>helo</code></p>
<dd>Set the hostname to identify as when sending HELO or EHLO commands. (This is a per identity option, as it should be the name you are seen as from the connected host, which may very with host to host due to NAT or different naming schemes). </p>
<dt><code>qualifydomain</code></p>
<dd>Make all local addresses to remote ones by adding @ and this name. </p>
<dt><code>force sender</code></p>
<dd>Set a &quot;Sender:&quot; header and ignore those in the message. &quot;%u&quot; will be replaced with the username. &quot;%%&quot; by &quot;%&quot;. </p>
<dt><code>force reverse_path</code></p>
<dd>Set the envelope from address. The address given to -f will only be used as &quot;From:&quot; when the message contains none. &quot;%u&quot; will be replaced with the username. &quot;%%&quot; by &quot;%&quot;. </p>
<dt><code>message_id</code></p>
<dd>Whether to set the Message-ID field of the message before sending. Normally the receiving MTA sets the Message-ID if missing, so you can turn this off if your sending host does not have a fully qualified domain name. </p>
<p> Allowed values are either <code>enabled</code> or <code>disabled</code>. It defaults to <code>enabled</code> </p>
<dt><code>preconnect</code></p>
<dd>Shell command to execute prior to opening an SMTP connection. </p>
<p> This may be useful in conjunction with application-level transports (e.g. <code>ssh</code> with its port-forwarding functionality) to secure the SMTP connection. <code>Esmtp</code> will wait for the command to exit before proceeding. If the command returns a non-zero status, delivery will be aborted. </p>
<dt><code>identity</code></p>
<dd>Define an identity. </p>
<p> An identity is a set of options associated with a given address. For example: </p>
<pre> identity = myself [at] somewhere.com
 hostname = smtp.somewhere.com:25
 username = &quot;myself&quot;
 password = &quot;secret&quot;</pre>
<p>Identities are be selected by the address specified in the <code>-f</code> flag. You can have as many you like. </p>
<p> The options in the global section (up to the first <code>identity</code> option) constitute the default identity. If no options in the global section are given then the first defined identity is taken as the default one. </p>
<p> Note that the default identity settings are not shared by the other identities. Everything (username, password, etc.) must be specified for every identity even if they don&#8217;t differ from the default identity. </p>
<dt><code>mda</code></p>
<dd>Set the Mail Delivery Agent (MDA). </p>
<p> <code>Esmtp</code> relies upon a MDA for local mail delivery, i.e., addresses without a &#8216;@&#8217; character. A non-zero error status tells <code>esmtp</code> that delivery failed. </p>
<p> The local delivery addresses will be inserted into the MDA command wherever you place a %T. The mail message&#8217;s <code>From</code> address will be inserted where you place an %F. </p>
<p> Some common MDAs are &quot;/usr/bin/procmail -d %T&quot;, &quot;/usr/bin/deliver&quot; and &quot;/usr/lib/mail.local %T&quot;. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-esmtp/">esmtp</a>(1) </p>
<h2>Author</h2>
<p>Jos&eacute; Fonseca</p>
