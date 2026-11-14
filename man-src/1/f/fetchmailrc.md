---
title: "fetchmailrc(1)"
name: "fetchmailrc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fetchmailrc/"
description: "fetchmail – fetch mail from a POP, IMAP, ETRN, or ODMR-capable server"
---

<h2 class="name">NAME</h2>
<p> fetchmail &#8211; fetch mail from a POP, IMAP, ETRN, or ODMR-capable server</p>
<h2>SYNOPSIS</h2>
<p> <code>fetchmail</code> [<i>option&#8230;</i>] [<i>mailserver&#8230;</i>]<br />
 <code>fetchmailconf</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>fetchmail</code> is a mail-retrieval and forwarding utility; it fetches mail from remote mailservers and forwards it to your local (client) machine&#8217;s delivery system. You can then handle the retrieved mail using normal mail user agents such as <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code><a href="/docs/linux/man/1-elm/">elm</a></code>(1) or <code><a href="/docs/linux/man/1-mail/">Mail</a></code>(1). The <code>fetchmail</code> utility can be run in a daemon mode to repeatedly poll one or more systems at a specified interval. </p>
<p> The <code>fetchmail</code> program can gather mail from servers supporting any of the common mail-retrieval protocols: POP2 (legacy, to be removed from future release), POP3, IMAP2bis, IMAP4, and IMAP4rev1. It can also use the ESMTP ETRN extension and ODMR. (The RFCs describing all these protocols are listed at the end of this manual page.) </p>
<p> While <code>fetchmail</code> is primarily intended to be used over on-demand TCP/IP links (such as SLIP or PPP connections), it may also be useful as a message transfer agent for sites which refuse for security reasons to permit (sender-initiated) SMTP transactions with sendmail. </p>
<h3>SUPPORT, TROUBLESHOOTING</h3>
<p> For troubleshooting, tracing and debugging, you need to increase fetchmail&#8217;s verbosity to actually see what happens. To do that, please run <code>both of the two following commands, adding all of the options you&#8217;d normally use.</code> </p>
<dl>
<dt>
<dd>
<pre>
env LC_ALL=C fetchmail -V -v --nodetach --nosyslog
</pre>
<dt>
<dd> (This command line prints in English how fetchmail understands your configuration.) </p>
<dt>
<dd>
<pre>
env LC_ALL=C fetchmail -vvv  --nodetach --nosyslog
</pre>
<dt>
<dd> (This command line actually runs fetchmail with verbose English output.)</dl>
<p> Also see </p>
<p> You can omit the LC_ALL=C part above if you want output in the local language (if supported). However if you are posting to mailing lists, please leave it in. The maintainers do not necessarily understand your language, please use English. </p>
<h3>CONCEPTS</h3>
<p> If <code>fetchmail</code> is used with a POP or an IMAP server (but not with ETRN or ODMR), it has two fundamental modes of operation for each user account from which it retrieves mail: <i>singledrop</i>&#8211; and <i>multidrop</i>-mode.</p>
<dl>
<dt>In singledrop-mode,</p>
<dd> <code>fetchmail</code> assumes that all messages in the user&#8217;s account (mailbox) are intended for a single recipient. The identity of the recipient will either default to the local user currently executing <code>fetchmail</code>, or will need to be explicitly specified in the configuration file.</p>
<dt>
<dd> <code>fetchmail</code> uses singledrop-mode when the fetchmailrc configuration contains at most a single local user specification for a given server account.</p>
<dt>In multidrop-mode,</p>
<dd> <code>fetchmail</code> assumes that the mail server account actually contains mail intended for any number of different recipients. Therefore, <code>fetchmail</code> must attempt to deduce the proper &quot;envelope recipient&quot; from the mail headers of each message. In this mode of operation, <code>fetchmail</code> almost resembles a mail transfer agent (MTA).</p>
<dt>
<dd> Note that neither the POP nor IMAP protocols were intended for use in this fashion, and hence envelope information is often not directly available. The ISP must stores the envelope information in some message header <code>and</code>. The ISP must also store one copy of the message per recipient. If either of the conditions is not fulfilled, this process is unreliable, because <code>fetchmail</code> must then resort to guessing the true envelope recipient(s) of a message. This usually fails for mailing list messages and Bcc:d mail, or mail for multiple recipients in your domain.</p>
<dt>
<dd> <code>fetchmail</code> uses multidrop-mode when more than one local user and/or a wildcard is specified for a particular server account in the configuration file.</p>
<dt>In ETRN and ODMR modes,</p>
<dd> these considerations do not apply, as these protocols are based on SMTP, which provides explicit envelope recipient information. These protocols always support multiple recipients.</dl>
<p> As each message is retrieved, <code>fetchmail</code> normally delivers it via SMTP to port 25 on the machine it is running on (localhost), just as though it were being passed in over a normal TCP/IP link. <code>fetchmail</code> provides the SMTP server with an envelope recipient derived in the manner described previously. The mail will then be delivered according to your MTA&#8217;s rules (the Mail Transfer Agent is usually <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/8-exim/">exim</a></code>(8), or <code><a href="/docs/linux/man/8-postfix/">postfix</a></code>(8)). Invoking your system&#8217;s MDA (Mail Delivery Agent) is the duty of your MTA. All the delivery-control mechanisms (such as <i>.forward</i> files) normally available through your system MTA and local delivery agents will therefore be applied as usual. </p>
<p> If your fetchmail configuration sets a local MDA (see the &#8211;mda option), it will be used directly instead of talking SMTP to port 25. </p>
<p> If the program <code>fetchmailconf</code> is available, it will assist you in setting up and editing a fetchmailrc configuration. It runs under the X window system and requires that the language Python and the Tk toolkit (with Python bindings) be present on your system. If you are first setting up fetchmail for single-user mode, it is recommended that you use Novice mode. Expert mode provides complete control of fetchmail configuration, including the multidrop features. In either case, the &#8216;Autoprobe&#8217; button will tell you the most capable protocol a given mailserver supports, and warn you of potential problems with that server. </p>
<h2>GENERAL OPERATION</h2>
<p> The behavior of <code>fetchmail</code> is controlled by command-line options and a run control file, <i>~/.fetchmailrc</i>, the syntax of which we describe in a later section (this file is what the <code>fetchmailconf</code> program edits). Command-line options override <i>~/.fetchmailrc</i> declarations. </p>
<p> Each server name that you specify following the options on the command line will be queried. If you do not specify any servers on the command line, each &#8216;poll&#8217; entry in your <i>~/.fetchmailrc</i> file will be queried, unless the idle option is used, which see. </p>
<p> To facilitate the use of <code>fetchmail</code> in scripts and pipelines, it returns an appropriate exit code upon termination &#8212; see EXIT CODES below. </p>
<p> The following options modify the behavior of <code>fetchmail</code>. It is seldom necessary to specify any of these once you have a working <i>.fetchmailrc</i> file set up. </p>
<p> Almost all options have a corresponding keyword which can be used to declare them in a <i>.fetchmailrc</i> file. </p>
<p> Some special options are not covered here, but are documented instead in sections on AUTHENTICATION and DAEMON MODE which follow.</p>
<h3>General Options</h3>
<dl>
<dt><code>-? | &#8211;help</code></p>
<dd> Displays option help.</p>
<dt><code>-V | &#8211;version</code></p>
<dd> Displays the version information for your copy of <code>fetchmail</code>. No mail fetch is performed. Instead, for each server specified, all the option information that would be computed if <code>fetchmail</code> were connecting to that server is displayed. Any non-printables in passwords or other string names are shown as backslashed C-like escape sequences. This option is useful for verifying that your options are set the way you want them.</p>
<dt><code>-c | &#8211;check</code></p>
<dd> Return a status code to indicate whether there is mail waiting, without actually fetching or deleting mail (see EXIT CODES below). This option turns off daemon mode (in which it would be useless). It doesn&#8217;t play well with queries to multiple sites, and doesn&#8217;t work with ETRN or ODMR. It will return a false positive if you leave read but undeleted mail in your server mailbox and your fetch protocol can&#8217;t tell kept messages from new ones. This means it will work with IMAP, not work with POP2, and may occasionally flake out under POP3.</p>
<dt><code>-s | &#8211;silent</code></p>
<dd> Silent mode. Suppresses all progress/status messages that are normally echoed to standard output during a fetch (but does not suppress actual error messages). The &#8211;verbose option overrides this.</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Verbose mode. All control messages passed between <code>fetchmail</code> and the mailserver are echoed to stdout. Overrides &#8211;silent. Doubling this option (-v -v) causes extra diagnostic information to be printed.</p>
<dt><code>&#8211;nosoftbounce</code></p>
<dd> (since v6.3.10, Keyword: set no softbounce, since v6.3.10)<br />
 Hard bounce mode. All permanent delivery errors cause messages to be deleted from the upstream server, see &quot;no softbounce&quot; below.</p>
<dt><code>&#8211;softbounce</code></p>
<dd> (since v6.3.10, Keyword: set softbounce, since v6.3.10)<br />
 Soft bounce mode. All permanent delivery errors cause messages to be left on the upstream server if the protocol supports that. <code>This option is on by default to match historic fetchmail documentation,</code> and will be changed to hard bounce mode in the next fetchmail release.</dl>
<h3>Disposal Options</h3>
<dl>
<dt><code>-a | &#8211;all | (since v6.3.3) &#8211;fetchall</code></p>
<dd> (Keyword: fetchall, since v3.0)<br />
 Retrieve both old (seen) and new messages from the mailserver. The default is to fetch only messages the server has not marked seen. Under POP3, this option also forces the use of RETR rather than TOP. Note that POP2 retrieval behaves as though &#8211;all is always on (see RETRIEVAL FAILURE MODES below) and this option does not work with ETRN or ODMR. While the -a and &#8211;all command-line and fetchall rcfile options have been supported for a long time, the &#8211;fetchall command-line option was added in v6.3.3.</p>
<dt><code>-k | &#8211;keep</code></p>
<dd> (Keyword: keep)<br />
 Keep retrieved messages on the remote mailserver. Normally, messages are deleted from the folder on the mailserver after they have been retrieved. Specifying the <code>keep</code> option causes retrieved messages to remain in your folder on the mailserver. This option does not work with ETRN or ODMR. If used with POP3, it is recommended to also specify the &#8211;uidl option or uidl keyword.</p>
<dt><code>-K | &#8211;nokeep</code></p>
<dd> (Keyword: nokeep)<br />
 Delete retrieved messages from the remote mailserver. This option forces retrieved mail to be deleted. It may be useful if you have specified a default of <code>keep</code> in your <i>.fetchmailrc</i>. This option is forced on with ETRN and ODMR.</p>
<dt><code>-F | &#8211;flush</code></p>
<dd> (Keyword: flush)<br />
 POP3/IMAP only. This is a dangerous option and can cause mail loss when used improperly. It deletes old (seen) messages from the mailserver before retrieving new messages. <code>Warning:</code> This can cause mail loss if you check your mail with other clients than fetchmail, and cause fetchmail to delete a message it had never fetched before. It can also cause mail loss if the mail server marks the message seen after retrieval (IMAP2 servers). You should probably not use this option in your configuration file. If you use it with POP3, you must use the &#8216;uidl&#8217; option. What you probably want is the default setting: if you don&#8217;t specify &#8216;-k&#8217;, then fetchmail will automatically delete messages after successful delivery.</p>
<dt><code>&#8211;limitflush</code></p>
<dd> POP3/IMAP only, since version 6.3.0. Delete oversized messages from the mailserver before retrieving new messages. The size limit should be separately specified with the &#8211;limit option. This option does not work with ETRN or ODMR.</dl>
<h3>Protocol and Query Options</h3>
<dl>
<dt><code>-p &lt;proto&gt; | &#8211;proto &lt;proto&gt; | &#8211;protocol &lt;proto&gt;</code></p>
<dd> (Keyword: proto[col])<br />
 Specify the protocol to use when communicating with the remote mailserver. If no protocol is specified, the default is AUTO. <code>proto</code> may be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>AUTO</p>
<dd> Tries IMAP, POP3, and POP2 (skipping any of these for which support has not been compiled in).</p>
<dt>POP2</p>
<dd> Post Office Protocol 2 (legacy, to be removed from future release)</p>
<dt>POP3</p>
<dd> Post Office Protocol 3</p>
<dt>APOP</p>
<dd> Use POP3 with old-fashioned MD5-challenge authentication. Considered not resistant to man-in-the-middle attacks.</p>
<dt>RPOP</p>
<dd> Use POP3 with RPOP authentication.</p>
<dt>KPOP</p>
<dd> Use POP3 with Kerberos V4 authentication on port 1109.</p>
<dt>SDPS</p>
<dd> Use POP3 with Demon Internet&#8217;s SDPS extensions.</p>
<dt>IMAP</p>
<dd> IMAP2bis, IMAP4, or IMAP4rev1 (<code>fetchmail</code> automatically detects their capabilities).</p>
<dt>ETRN</p>
<dd> Use the ESMTP ETRN option.</p>
<dt>ODMR</p>
<dd> Use the the On-Demand Mail Relay ESMTP profile.</dl>
</dl>
</dl>
<p> All these alternatives work in basically the same way (communicating with standard server daemons to fetch mail already delivered to a mailbox on the server) except ETRN and ODMR. The ETRN mode allows you to ask a compliant ESMTP server (such as BSD sendmail at release 8.8.0 or higher) to immediately open a sender-SMTP connection to your client machine and begin forwarding any items addressed to your client machine in the server&#8217;s queue of undelivered mail. The ODMR mode requires an ODMR-capable server and works similarly to ETRN, except that it does not require the client machine to have a static DNS.</p>
<dl>
<dt><code>-U | &#8211;uidl</code></p>
<dd> (Keyword: uidl)<br />
 Force UIDL use (effective only with POP3). Force client-side tracking of &#8216;newness&#8217; of messages (UIDL stands for &quot;unique ID listing&quot; and is described in RFC1939). Use with &#8216;keep&#8217; to use a mailbox as a baby news drop for a group of users. The fact that seen messages are skipped is logged, unless error logging is done through syslog while running in daemon mode. Note that fetchmail may automatically enable this option depending on upstream server capabilities. Note also that this option may be removed and forced enabled in a future fetchmail version. See also: &#8211;idfile.</p>
<dt><code>&#8211;idle (since 6.3.3)</code></p>
<dd> (Keyword: idle, since before 6.0.0)<br />
 Enable IDLE use (effective only with IMAP). Note that this works with only one account and one folder at a given time, other folders or accounts will not be polled when idle is in effect! While the idle rcfile keyword had been supported for a long time, the &#8211;idle command-line option was added in version 6.3.3. IDLE use means that fetchmail tells the IMAP server to send notice of new messages, so they can be retrieved sooner than would be possible with regular polls.</p>
<dt><code>-P &lt;portnumber&gt; | &#8211;service &lt;servicename&gt;</code></p>
<dd> (Keyword: service) Since version 6.3.0.<br />
 The service option permits you to specify a service name to connect to. You can specify a decimal port number here, if your services database lacks the required service-port assignments. See the FAQ item R12 and the &#8211;ssl documentation for details. This replaces the older &#8211;port option.</p>
<dt><code>&#8211;port &lt;portnumber&gt;</code></p>
<dd> (Keyword: port)<br />
 Obsolete version of &#8211;service that does not take service names. <code>Note:</code> this option may be removed from a future version.</p>
<dt><code>&#8211;principal &lt;principal&gt;</code></p>
<dd> (Keyword: principal)<br />
 The principal option permits you to specify a service principal for mutual authentication. This is applicable to POP3 or IMAP with Kerberos 4 authentication only. It does not apply to Kerberos 5 or GSSAPI. This option may be removed in a future fetchmail version.</p>
<dt><code>-t &lt;seconds&gt; | &#8211;timeout &lt;seconds&gt;</code></p>
<dd> (Keyword: timeout)<br />
 The timeout option allows you to set a server-nonresponse timeout in seconds. If a mailserver does not send a greeting message or respond to commands for the given number of seconds, <code>fetchmail</code> will drop the connection to it. Without such a timeout <code>fetchmail</code> might hang until the TCP connection times out, trying to fetch mail from a down host, which may be very long. This would be particularly annoying for a <code>fetchmail</code> running in the background. There is a default timeout which fetchmail~-V will report. If a given connection receives too many timeouts in succession, fetchmail will consider it wedged and stop retrying. The calling user will be notified by email if this happens.</p>
<dt>
<dd> Beginning with fetchmail 6.3.10, the SMTP client uses the recommended minimum timeouts from RFC-5321 while waiting for the SMTP/LMTP server it is talking to. You can raise the timeouts even more, but you cannot shorten them. This is to avoid a painful situation where fetchmail has been configured with a short timeout (a minute or less), ships a long message (many MBytes) to the local MTA, which then takes longer than timeout to respond &quot;OK&quot;, which it eventually will; that would mean the mail gets delivered properly, but fetchmail cannot notice it and will thus refetch this big message over and over again.</p>
<dt><code>&#8211;plugin &lt;command&gt;</code></p>
<dd> (Keyword: plugin)<br />
 The plugin option allows you to use an external program to establish the TCP connection. This is useful if you want to use ssh, or need some special firewalling setup. The program will be looked up in $PATH and can optionally be passed the hostname and port as arguments using &quot;%h&quot; and &quot;%p&quot; respectively (note that the interpolation logic is rather primitive, and these tokens must be bounded by whitespace or beginning of string or end of string). Fetchmail will write to the plugin&#8217;s stdin and read from the plugin&#8217;s stdout.</p>
<dt><code>&#8211;plugout &lt;command&gt;</code></p>
<dd> (Keyword: plugout)<br />
 Identical to the plugin option above, but this one is used for the SMTP connections.</p>
<dt><code>-r &lt;name&gt; | &#8211;folder &lt;name&gt;</code></p>
<dd> (Keyword: folder[s])<br />
 Causes a specified non-default mail folder on the mailserver (or comma-separated list of folders) to be retrieved. The syntax of the folder name is server-dependent. This option is not available under POP3, ETRN, or ODMR.</p>
<dt><code>&#8211;tracepolls</code></p>
<dd> (Keyword: tracepolls)<br />
 Tell fetchmail to poll trace information in the form &#8216;polling account %s&#8217; and &#8216;folder %s&#8217; to the Received line it generates, where the %s parts are replaced by the user&#8217;s remote name, the poll label, and the folder (mailbox) where available (the Received header also normally includes the server&#8217;s true name). This can be used to facilitate mail filtering based on the account it is being received from. The folder information is written only since version 6.3.4.</p>
<dt><code>&#8211;ssl</code></p>
<dd> (Keyword: ssl)<br />
 Causes the connection to the mail server to be encrypted via SSL, by negotiating SSL directly after connecting (SSL-wrapped mode). Please see the description of &#8211;sslproto below! More information is available in the <i>README.SSL</i> file that ships with fetchmail.</p>
<dt>
<dd> Note that even if this option is omitted, fetchmail may still negotiate SSL in-band for POP3 or IMAP, through the STLS or STARTTLS feature. You can use the &#8211;sslproto option to modify that behavior.</p>
<dt>
<dd> If no port is specified, the connection is attempted to the well known port of the SSL version of the base protocol. This is generally a different port than the port used by the base protocol. For IMAP, this is port 143 for the clear protocol and port 993 for the SSL secured protocol; for POP3, it is port 110 for the clear text and port 995 for the encrypted variant.</p>
<dt>
<dd> If your system lacks the corresponding entries from /etc/services, see the &#8211;service option and specify the numeric port number as given in the previous paragraph (unless your ISP had directed you to different ports, which is uncommon however).</p>
<dt><code>&#8211;sslcert &lt;name&gt;</code></p>
<dd> (Keyword: sslcert)<br />
 For certificate-based client authentication. Some SSL encrypted servers require client side keys and certificates for authentication. In most cases, this is optional. This specifies the location of the public key certificate to be presented to the server at the time the SSL session is established. It is not required (but may be provided) if the server does not require it. It may be the same file as the private key (combined key and certificate file) but this is not recommended. Also see &#8211;sslkey below. </p>
<p> <code>NOTE:</code> If you use client authentication, the user name is fetched from the certificate&#8217;s CommonName and overrides the name set with &#8211;user.</p>
<dt><code>&#8211;sslkey &lt;name&gt;</code></p>
<dd> (Keyword: sslkey)<br />
 Specifies the file name of the client side private SSL key. Some SSL encrypted servers require client side keys and certificates for authentication. In most cases, this is optional. This specifies the location of the private key used to sign transactions with the server at the time the SSL session is established. It is not required (but may be provided) if the server does not require it. It may be the same file as the public key (combined key and certificate file) but this is not recommended.</p>
<dt>
<dd> If a password is required to unlock the key, it will be prompted for at the time just prior to establishing the session to the server. This can cause some complications in daemon mode.</p>
<dt>
<dd> Also see &#8211;sslcert above.</p>
<dt><code>&#8211;sslproto &lt;value&gt;</code></p>
<dd> (Keyword: sslproto, NOTE: semantic changes since v6.4.0)<br />
 This option has a dual use, out of historic fetchmail behaviour. It controls both the SSL/TLS protocol version and, if &#8211;ssl is not specified, the STARTTLS behaviour (upgrading the protocol to an SSL or TLS connection in-band). Some other options may however make TLS mandatory.</dl>
<p> Only if this option and &#8211;ssl are both missing for a poll, there will be opportunistic TLS for POP3 and IMAP, where fetchmail will attempt to upgrade to TLSv1 or newer. </p>
<p> Recognized values for &#8211;sslproto are given below. You should normally chose one of the auto-negotiating options, i. e. &#8216;<code>auto</code>&#8216; or one of the options ending in a plus (<code>+</code>) character. Note that depending on OpenSSL library version and configuration, some options cause run-time errors because the requested SSL or TLS versions are not supported by the particular installed OpenSSL library.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8221;</code>, the empty string</p>
<dd> Disable STARTTLS. If &#8211;ssl is given for the same server, log an error and pretend that &#8216;<code>auto</code>&#8216; had been used instead.</p>
<dt>&#8216;<code>auto</code>&#8216;</p>
<dd> (default). Since v6.4.0. Require TLS. Auto-negotiate TLSv1 or newer, disable SSLv3 downgrade. (fetchmail 6.3.26 and older have auto-negotiated all protocols that their OpenSSL library supported, including the broken SSLv3).</p>
<dt>&#8216;<code>SSL23</code>&#8216;</p>
<dd> see &#8216;<code>auto</code>&#8216;.</p>
<dt>&#8216;<code>SSL3</code>&#8216;</p>
<dd> Require SSLv3 exactly. SSLv3 is broken, not supported on all systems, avoid it if possible. This will make fetchmail negotiate SSLv3 only, and is the only way besides &#8216;<code>SSL3+</code>&#8216; to have fetchmail 6.4.0 or newer permit SSLv3.</p>
<dt>&#8216;<code>SSL3+</code>&#8216;</p>
<dd> same as &#8216;<code>auto</code>&#8216;, but permit SSLv3 as well. This is the only way besides &#8216;<code>SSL3</code>&#8216; to have fetchmail 6.4.0 or newer permit SSLv3.</p>
<dt>&#8216;<code>TLS1</code>&#8216;</p>
<dd> Require TLSv1. This does not negotiate TLSv1.1 or newer, and is discouraged. Replace by TLS1+ unless the latter chokes your server.</p>
<dt>&#8216;<code>TLS1+</code>&#8216;</p>
<dd> Since v6.4.0. See &#8216;<code>auto</code>&#8216;.</p>
<dt>&#8216;<code>TLS1.1</code>&#8216;</p>
<dd> Since v6.4.0. Require TLS v1.1 exactly.</p>
<dt>&#8216;<code>TLS1.1+</code>&#8216;</p>
<dd> Since v6.4.0. Require TLS. Auto-negotiate TLSv1.1 or newer.</p>
<dt>&#8216;<code>TLS1.2</code>&#8216;</p>
<dd> Since v6.4.0. Require TLS v1.2 exactly.</p>
<dt>&#8216;<code>TLS1.2+</code>&#8216;</p>
<dd> Since v6.4.0. Require TLS. Auto-negotiate TLSv1.2 or newer.</p>
<dt>Unrecognized parameters</p>
<dd> are treated the same as &#8216;<code>auto</code>&#8216;.</dl>
</dl>
<dl>
<dt>
<dd> NOTE: you should hardly ever need to use anything other than &#8221; (to force an unencrypted connection) or &#8216;auto&#8217; (to enforce TLS).</p>
<dt><code>&#8211;sslcertck</code></p>
<dd> (Keyword: sslcertck, default enabled since v6.4.0)<br />
 <code>&#8211;sslcertck causes fetchmail to require that SSL/TLS be used and</code> disconnect if it can not successfully negotiate SSL or TLS, or if it cannot successfully verify and validate the certificate and follow it to a trust anchor (or trusted root certificate). The trust anchors are given as a set of local trusted certificates (see the <code>sslcertfile</code> and <code>sslcertpath</code> options). If the server certificate cannot be obtained or is not signed by one of the trusted ones (directly or indirectly), fetchmail will disconnect, regardless of the <code>sslfingerprint</code> option.</p>
<dt>
<dd> Note that CRL (certificate revocation lists) are only supported in OpenSSL 0.9.7 and newer! Your system clock should also be reasonably accurate when using this option.</p>
<dt><code>&#8211;nosslcertck</code></p>
<dd> (Keyword: no sslcertck, only in v6.4.X)<br />
 The opposite of &#8211;sslcertck, this is a disouraged option. It permits fetchmail to continue connecting even if the server certificate failed the verification checks. Should only be used together with &#8211;sslfingerprint.</p>
<dt><code>&#8211;sslcertfile &lt;file&gt;</code></p>
<dd> (Keyword: sslcertfile, since v6.3.17)<br />
 Sets the file fetchmail uses to look up local certificates. The default is empty. This can be given in addition to <code>&#8211;sslcertpath</code> below, and certificates specified in <code>&#8211;sslcertfile</code> will be processed before those in <code>&#8211;sslcertpath</code>. The option can be used in addition to <code>&#8211;sslcertpath</code>.</p>
<dt>
<dd> The file is a text file. It contains the concatenation of trusted CA certificates in PEM format.</p>
<dt>
<dd> Note that using this option will suppress loading the default SSL trusted CA certificates file unless you set the environment variable <code>FETCHMAIL_INCLUDE_DEFAULT_X509_CA_CERTS</code> to a non-empty value.</p>
<dt><code>&#8211;sslcertpath &lt;directory&gt;</code></p>
<dd> (Keyword: sslcertpath)<br />
 Sets the directory fetchmail uses to look up local certificates. The default is your OpenSSL default directory. The directory must be hashed the way OpenSSL expects it &#8211; every time you add or modify a certificate in the directory, you need to use the <code>c_rehash</code> tool (which comes with OpenSSL in the tools/ subdirectory). Also, after OpenSSL upgrades, you may need to run <code>c_rehash</code>; particularly when upgrading from 0.9.X to 1.0.0.</p>
<dt>
<dd> This can be given in addition to <code>&#8211;sslcertfile</code> above, which see for precedence rules.</p>
<dt>
<dd> Note that using this option will suppress adding the default SSL trusted CA certificates directory unless you set the environment variable <code>FETCHMAIL_INCLUDE_DEFAULT_X509_CA_CERTS</code> to a non-empty value.</p>
<dt><code>&#8211;sslcommonname &lt;common name&gt;</code></p>
<dd> (Keyword: sslcommonname; since v6.3.9)<br />
 Use of this option is discouraged. Before using it, contact the administrator of your upstream server and ask for a proper SSL certificate to be used. If that cannot be attained, this option can be used to specify the name (CommonName) that fetchmail expects on the server certificate. A correctly configured server will have this set to the hostname by which it is reached, and by default fetchmail will expect as much. Use this option when the CommonName is set to some other value, to avoid the &quot;Server CommonName mismatch&quot; warning, and only if the upstream server can&#8217;t be made to use proper certificates.</p>
<dt><code>&#8211;sslfingerprint &lt;fingerprint&gt;</code></p>
<dd> (Keyword: sslfingerprint)<br />
 Specify the fingerprint of the server key (an MD5 hash of the key) in hexadecimal notation with colons separating groups of two digits. The letter hex digits must be in upper case. This is the format that fetchmail uses to report the fingerprint when an SSL connection is established. When this is specified, fetchmail will compare the server key fingerprint with the given one, and the connection will fail if they do not match, regardless of the <code>sslcertck</code> setting. The connection will also fail if fetchmail cannot obtain an SSL certificate from the server. This can be used to prevent man-in-the-middle attacks, but the finger print from the server must be obtained or verified over a secure channel, and certainly not over the same Internet connection that fetchmail would use.</p>
<dt>
<dd> Using this option will prevent printing certificate verification errors as long as &#8211;nosslcertck is in effect.</p>
<dt>
<dd> To obtain the fingerprint of a certificate stored in the file cert.pem, try: </p>
<pre>
        openssl x509 -in cert.pem -noout -md5 -fingerprint
</pre>
<p> For details, see <code>x509</code>(1ssl).</dl>
<h3>Delivery Control Options</h3>
<dl>
<dt><code>-S &lt;hosts&gt; | &#8211;smtphost &lt;hosts&gt;</code></p>
<dd> (Keyword: smtp[host])<br />
 Specify a hunt list of hosts to forward mail to (one or more hostnames, comma-separated). Hosts are tried in list order; the first one that is up becomes the forwarding target for the current run. If this option is not specified, &#8216;localhost&#8217; is used as the default. Each hostname may have a port number following the host name. The port number is separated from the host name by a slash; the default port is &quot;smtp&quot;. If you specify an absolute path name (beginning with a /), it will be interpreted as the name of a UNIX socket accepting LMTP connections (such as is supported by the Cyrus IMAP daemon) Example: </p>
<pre>
        --smtphost server1,server2/2525,server3,/var/imap/socket/lmtp
</pre>
<p> This option can be used with ODMR, and will make fetchmail a relay between the ODMR server and SMTP or LMTP receiver.</p>
<dt>
<dd> WARNING: if you use address numeric IP addresses here, be sure to use &#8211;smtpaddress or &#8211;smtpname (either of which see) with a valid SMTP address literal!</p>
<dt><code>&#8211;fetchdomains &lt;hosts&gt;</code></p>
<dd> (Keyword: fetchdomains)<br />
 In ETRN or ODMR mode, this option specifies the list of domains the server should ship mail for once the connection is turned around. The default is the FQDN of the machine running <code>fetchmail</code>.</p>
<dt><code>-D &lt;domain&gt; | &#8211;smtpaddress &lt;domain&gt;</code></p>
<dd> (Keyword: smtpaddress)<br />
 Specify the domain to be appended to addresses in RCPT TO lines shipped to SMTP. When this is not specified, the name of the SMTP server (as specified by &#8211;smtphost) is used for SMTP/LMTP and &#8216;localhost&#8217; is used for UNIX socket/BSMTP.</p>
<dt>
<dd> NOTE: if you intend to use numeric addresses, or so-called address literals per the SMTP standard, write them in proper SMTP syntax, for instance &#8211;smtpaddress &quot;[192.0.2.6]&quot; or &#8211;smtpaddress &quot;[IPv6:2001:DB8::6]&quot;.</p>
<dt><code>&#8211;smtpname &lt;user [at] domain&gt;</code></p>
<dd> (Keyword: smtpname)<br />
 Specify the domain and user to be put in RCPT TO lines shipped to SMTP. The default user is the current local user. Please also see the NOTE about &#8211;smtpaddress and address literals above.</p>
<dt><code>-Z &lt;nnn&gt; | &#8211;antispam &lt;nnn[, nnn]&#8230;&gt;</code></p>
<dd> (Keyword: antispam)<br />
 Specifies the list of numeric SMTP errors that are to be interpreted as a spam-block response from the listener. A value of -1 disables this option. For the command-line option, the list values should be comma-separated. Note that the antispam values only apply to &quot;MAIL FROM&quot; responses in the SMTP/LMTP dialogue, but several MTAs (Postfix in its default configuration, qmail) defer the anti-spam response code until after the RCPT TO. &#8211;antispam does not work in these circumstances. Also see &#8211;softbounce (default) and its inverse.</p>
<dt><code>-m &lt;command&gt; | &#8211;mda &lt;command&gt;</code></p>
<dd> (Keyword: mda)<br />
 This option lets <code>fetchmail</code> use a Message or Local Delivery Agent (MDA or LDA) directly, rather than forward via SMTP or LMTP. </p>
<p> To avoid losing mail, use this option only with MDAs like maildrop or MTAs like sendmail that exit with a nonzero status on disk-full and other delivery errors; the nonzero status tells fetchmail that delivery failed and prevents the message from being deleted on the server. </p>
<p> If <code>fetchmail</code> is running as root, it sets its user id while delivering mail through an MDA as follows: First, the FETCHMAILUSER, LOGNAME, and USER environment variables are checked in this order. The value of the first variable from his list that is defined (even if it is empty!) is looked up in the system user database. If none of the variables is defined, fetchmail will use the real user id it was started with. If one of the variables was defined, but the user stated there isn&#8217;t found, fetchmail continues running as root, without checking remaining variables on the list. Practically, this means that if you run fetchmail as root (not recommended), it is most useful to define the FETCHMAILUSER environment variable to set the user that the MDA should run as. Some MDAs (such as maildrop) are designed to be setuid root and setuid to the recipient&#8217;s user id, so you don&#8217;t lose functionality this way even when running fetchmail as unprivileged user. Check the MDA&#8217;s manual for details. </p>
<p> Some possible MDAs are &quot;/usr/sbin/sendmail -i -f %F &#8212; %T&quot; (<code>Note:</code> some several older or vendor sendmail versions mistake &#8212; for an address, rather than an indicator to mark the end of the option arguments), &quot;/usr/bin/deliver&quot; and &quot;/usr/bin/maildrop -d %T&quot;. Local delivery addresses will be inserted into the MDA command wherever you place a %T; the mail message&#8217;s From address will be inserted where you place an %F. </p>
<p> <code>Do NOT enclose the %F or %T string in single quotes!</code> For both %T and %F, fetchmail encloses the addresses in single quotes (&#8216;), after removing any single quotes they may contain, before the MDA command is passed to the shell. </p>
<p> <code>Do NOT use an MDA invocation that dispatches on the contents of To/Cc/Bcc,</code> like &quot;sendmail -i -t&quot; or &quot;qmail-inject&quot;, it will create mail loops and bring the just wrath of many postmasters down upon your head. This is one of the most frequent configuration errors! </p>
<p> Also, do <i>not</i> try to combine multidrop mode with an MDA such as maildrop that can only accept one address, unless your upstream stores one copy of the message per recipient and transports the envelope recipient in a header; you will lose mail. </p>
<p> The well-known <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1) package is very hard to configure properly, it has a very nasty &quot;fall through to the next rule&quot; behavior on delivery errors (even temporary ones, such as out of disk space if another user&#8217;s mail daemon copies the mailbox around to purge old messages), so your mail will end up in the wrong mailbox sooner or later. The proper procmail configuration is outside the scope of this document. Using <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1) is usually much easier, and many users find the filter syntax used by maildrop easier to understand. </p>
<p> Finally, we strongly advise that you do <code>not</code> use qmail-inject. The command line interface is non-standard without providing benefits for typical use, and fetchmail makes no attempts to accommodate qmail-inject&#8217;s deviations from the standard. Some of qmail-inject&#8217;s command-line and environment options are actually dangerous and can cause broken threads, non-detected duplicate messages and forwarding loops. </p>
<dt><code>&#8211;lmtp</code></p>
<dd> (Keyword: lmtp)<br />
 Cause delivery via LMTP (Local Mail Transfer Protocol). A service host and port <code>must</code> be explicitly specified on each host in the smtphost hunt list (see above) if this option is selected; the default port 25 will (in accordance with RFC 2033) not be accepted.</p>
<dt><code>&#8211;bsmtp &lt;filename&gt;</code></p>
<dd> (Keyword: bsmtp)<br />
 Append fetched mail to a BSMTP file. This simply contains the SMTP commands that would normally be generated by fetchmail when passing mail to an SMTP listener daemon. </p>
<p> An argument of &#8216;-&#8216; causes the SMTP batch to be written to standard output, which is of limited use: this only makes sense for debugging, because fetchmail&#8217;s regular output is interspersed on the same channel, so this isn&#8217;t suitable for mail delivery. This special mode may be removed in a later release. </p>
<p> Note that fetchmail&#8217;s reconstruction of MAIL FROM and RCPT TO lines is not guaranteed correct; the caveats discussed under THE USE AND ABUSE OF MULTIDROP MAILBOXES below apply. This mode has precedence before &#8211;mda and SMTP/LMTP.</p>
<dt><code>&#8211;bad-header {reject|accept}</code></p>
<dd> (Keyword: bad-header; since v6.3.15)<br />
 Specify how fetchmail is supposed to treat messages with bad headers, i. e. headers with bad syntax. Traditionally, fetchmail has rejected such messages, but some distributors modified fetchmail to accept them. You can now configure fetchmail&#8217;s behaviour per server. </p>
</dl>
<h3>Resource Limit Control Options</h3>
<dl>
<dt><code>-l &lt;maxbytes&gt; | &#8211;limit &lt;maxbytes&gt;</code></p>
<dd> (Keyword: limit)<br />
 Takes a maximum octet size argument, where 0 is the default and also the special value designating &quot;no limit&quot;. If nonzero, messages larger than this size will not be fetched and will be left on the server (in foreground sessions, the progress messages will note that they are &quot;oversized&quot;). If the fetch protocol permits (in particular, under IMAP or POP3 without the fetchall option) the message will not be marked seen. </p>
<p> An explicit &#8211;limit of 0 overrides any limits set in your run control file. This option is intended for those needing to strictly control fetch time due to expensive and variable phone rates. </p>
<p> Combined with &#8211;limitflush, it can be used to delete oversized messages waiting on a server. In daemon mode, oversize notifications are mailed to the calling user (see the &#8211;warnings option). This option does not work with ETRN or ODMR.</p>
<dt><code>-w &lt;interval&gt; | &#8211;warnings &lt;interval&gt;</code></p>
<dd> (Keyword: warnings)<br />
 Takes an interval in seconds. When you call <code>fetchmail</code> with a &#8216;limit&#8217; option in daemon mode, this controls the interval at which warnings about oversized messages are mailed to the calling user (or the user specified by the &#8216;postmaster&#8217; option). One such notification is always mailed at the end of the the first poll that the oversized message is detected. Thereafter, re-notification is suppressed until after the warning interval elapses (it will take place at the end of the first following poll).</p>
<dt><code>-b &lt;count&gt; | &#8211;batchlimit &lt;count&gt;</code></p>
<dd> (Keyword: batchlimit)<br />
 Specify the maximum number of messages that will be shipped to an SMTP listener before the connection is deliberately torn down and rebuilt (defaults to 0, meaning no limit). An explicit &#8211;batchlimit of 0 overrides any limits set in your run control file. While <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8) normally initiates delivery of a message immediately after receiving the message terminator, some SMTP listeners are not so prompt. MTAs like <code><a href="/docs/linux/man/8-smail/">smail</a></code>(8) may wait till the delivery socket is shut down to deliver. This may produce annoying delays when <code>fetchmail</code> is processing very large batches. Setting the batch limit to some nonzero size will prevent these delays. This option does not work with ETRN or ODMR.</p>
<dt><code>-B &lt;number&gt; | &#8211;fetchlimit &lt;number&gt;</code></p>
<dd> (Keyword: fetchlimit)<br />
 Limit the number of messages accepted from a given server in a single poll. By default there is no limit. An explicit &#8211;fetchlimit of 0 overrides any limits set in your run control file. This option does not work with ETRN or ODMR.</p>
<dt><code>&#8211;fetchsizelimit &lt;number&gt;</code></p>
<dd> (Keyword: fetchsizelimit)<br />
 Limit the number of sizes of messages accepted from a given server in a single transaction. This option is useful in reducing the delay in downloading the first mail when there are too many mails in the mailbox. By default, the limit is 100. If set to 0, sizes of all messages are downloaded at the start. This option does not work with ETRN or ODMR. For POP3, the only valid non-zero value is 1.</p>
<dt><code>&#8211;fastuidl &lt;number&gt;</code></p>
<dd> (Keyword: fastuidl)<br />
 Do a binary instead of linear search for the first unseen UID. Binary search avoids downloading the UIDs of all mails. This saves time (especially in daemon mode) where downloading the same set of UIDs in each poll is a waste of bandwidth. The number &#8216;n&#8217; indicates how rarely a linear search should be done. In daemon mode, linear search is used once followed by binary searches in &#8216;n-1&#8217; polls if &#8216;n&#8217; is greater than 1; binary search is always used if &#8216;n&#8217; is 1; linear search is always used if &#8216;n&#8217; is 0. In non-daemon mode, binary search is used if &#8216;n&#8217; is 1; otherwise linear search is used. The default value of &#8216;n&#8217; is 4. This option works with POP3 only.</p>
<dt><code>-e &lt;count&gt; | &#8211;expunge &lt;count&gt;</code></p>
<dd> (Keyword: expunge)<br />
 Arrange for deletions to be made final after a given number of messages. Under POP2 or POP3, fetchmail cannot make deletions final without sending QUIT and ending the session &#8212; with this option on, fetchmail will break a long mail retrieval session into multiple sub-sessions, sending QUIT after each sub-session. This is a good defense against line drops on POP3 servers. Under IMAP, <code>fetchmail</code> normally issues an EXPUNGE command after each deletion in order to force the deletion to be done immediately. This is safest when your connection to the server is flaky and expensive, as it avoids resending duplicate mail after a line hit. However, on large mailboxes the overhead of re-indexing after every message can slam the server pretty hard, so if your connection is reliable it is good to do expunges less frequently. Also note that some servers enforce a delay of a few seconds after each quit, so fetchmail may not be able to get back in immediately after an expunge &#8212; you may see &quot;lock busy&quot; errors if this happens. If you specify this option to an integer N, it tells <code>fetchmail</code> to only issue expunges on every Nth delete. An argument of zero suppresses expunges entirely (so no expunges at all will be done until the end of run). This option does not work with ETRN or ODMR. </p>
</dl>
<h3>Authentication Options</h3>
<dl>
<dt><code>-u &lt;name&gt; | &#8211;user &lt;name&gt; | &#8211;username &lt;name&gt;</code></p>
<dd> (Keyword: user[name])<br />
 Specifies the user identification to be used when logging in to the mailserver. The appropriate user identification is both server and user-dependent. The default is your login name on the client machine that is running <code>fetchmail</code>. See USER AUTHENTICATION below for a complete description.</p>
<dt><code>-I &lt;specification&gt; | &#8211;interface &lt;specification&gt;</code></p>
<dd> (Keyword: interface)<br />
 Require that a specific interface device be up and have a specific local or remote IPv4 (IPv6 is not supported by this option yet) address (or range) before polling. Frequently <code>fetchmail</code> is used over a transient point-to-point TCP/IP link established directly to a mailserver via SLIP or PPP. That is a relatively secure channel. But when other TCP/IP routes to the mailserver exist (e.g. when the link is connected to an alternate ISP), your username and password may be vulnerable to snooping (especially when daemon mode automatically polls for mail, shipping a clear password over the net at predictable intervals). The &#8211;interface option may be used to prevent this. When the specified link is not up or is not connected to a matching IP address, polling will be skipped. The format is: </p>
<pre>
        interface/iii.iii.iii.iii[/mmm.mmm.mmm.mmm]
</pre>
<p> The field before the first slash is the interface name (i.e. sl0, ppp0 etc.). The field before the second slash is the acceptable IP address. The field after the second slash is a mask which specifies a range of IP addresses to accept. If no mask is present 255.255.255.255 is assumed (i.e. an exact match). This option is currently only supported under Linux and FreeBSD. Please see the <code>monitor</code> section for below for FreeBSD specific information. </p>
<p> Note that this option may be removed from a future fetchmail version.</p>
<dt><code>-M &lt;interface&gt; | &#8211;monitor &lt;interface&gt;</code></p>
<dd> (Keyword: monitor)<br />
 Daemon mode can cause transient links which are automatically taken down after a period of inactivity (e.g. PPP links) to remain up indefinitely. This option identifies a system TCP/IP interface to be monitored for activity. After each poll interval, if the link is up but no other activity has occurred on the link, then the poll will be skipped. However, when fetchmail is woken up by a signal, the monitor check is skipped and the poll goes through unconditionally. This option is currently only supported under Linux and FreeBSD. For the <code>monitor</code> and <code>interface</code> options to work for non root users under FreeBSD, the fetchmail binary must be installed SGID kmem. This would be a security hole, but fetchmail runs with the effective GID set to that of the kmem group <i>only</i> when interface data is being collected. </p>
<p> Note that this option may be removed from a future fetchmail version.</p>
<dt><code>&#8211;auth &lt;type&gt;</code></p>
<dd> (Keyword: auth[enticate])<br />
 This option permits you to specify an authentication type (see USER AUTHENTICATION below for details). The possible values are <code>any</code>, <code>password</code>, <code>kerberos_v5</code>, <code>kerberos</code> (or, for excruciating exactness, <code>kerberos_v4</code>), <code>gssapi</code>, <code>cram-md5</code>, <code>otp</code>, <code>ntlm</code>, <code>msn</code> (only for POP3), <code>external</code> (only IMAP) and <code>ssh</code>. When <code>any</code> (the default) is specified, fetchmail tries first methods that don&#8217;t require a password (EXTERNAL, GSSAPI, KERBEROS IV, KERBEROS 5); then it looks for methods that mask your password (CRAM-MD5, NTLM, X-OTP &#8211; note that MSN is only supported for POP3, but not autoprobed); and only if the server doesn&#8217;t support any of those will it ship your password en clair. Other values may be used to force various authentication methods (<code>ssh</code> suppresses authentication and is thus useful for IMAP PREAUTH). (<code>external</code> suppresses authentication and is thus useful for IMAP EXTERNAL). Any value other than <code>password</code>, <code>cram-md5</code>, <code>ntlm</code>, <code>msn</code> or <code>otp</code> suppresses fetchmail&#8217;s normal inquiry for a password. Specify <code>ssh</code> when you are using an end-to-end secure connection such as an ssh tunnel; specify <code>external</code> when you use TLS with client authentication and specify <code>gssapi</code> or <code>kerberos_v4</code> if you are using a protocol variant that employs GSSAPI or K4. Choosing KPOP protocol automatically selects Kerberos authentication. This option does not work with ETRN. GSSAPI service names are in line with RFC-2743 and IANA registrations, see</dl>
<h3>Miscellaneous Options</h3>
<dl>
<dt><code>-f &lt;pathname&gt; | &#8211;fetchmailrc &lt;pathname&gt;</code></p>
<dd> Specify a non-default name for the <i>~/.fetchmailrc</i> run control file. The pathname argument must be either &quot;-&quot; (a single dash, meaning to read the configuration from standard input) or a filename. Unless the &#8211;version option is also on, a named file argument must have permissions no more open than 0700 (u=rwx,g=,o=) or else be /dev/null.</p>
<dt><code>-i &lt;pathname&gt; | &#8211;idfile &lt;pathname&gt;</code></p>
<dd> (Keyword: idfile)<br />
 Specify an alternate name for the .fetchids file used to save message UIDs. NOTE: since fetchmail 6.3.0, write access to the directory containing the idfile is required, as fetchmail writes a temporary file and renames it into the place of the real idfile only if the temporary file has been written successfully. This avoids the truncation of idfiles when running out of disk space.</p>
<dt><code>&#8211;pidfile &lt;pathname&gt;</code></p>
<dd> (Keyword: pidfile; since fetchmail v6.3.4)<br />
 Override the default location of the PID file. Default: see &quot;ENVIRONMENT&quot; below.</p>
<dt><code>-n | &#8211;norewrite</code></p>
<dd> (Keyword: no rewrite)<br />
 Normally, <code>fetchmail</code> edits RFC-822 address headers (To, From, Cc, Bcc, and Reply-To) in fetched mail so that any mail IDs local to the server are expanded to full addresses (@ and the mailserver hostname are appended). This enables replies on the client to get addressed correctly (otherwise your mailer might think they should be addressed to local users on the client machine!). This option disables the rewrite. (This option is provided to pacify people who are paranoid about having an MTA edit mail headers and want to know they can prevent it, but it is generally not a good idea to actually turn off rewrite.) When using ETRN or ODMR, the rewrite option is ineffective.</p>
<dt><code>-E &lt;line&gt; | &#8211;envelope &lt;line&gt;</code></p>
<dd> (Keyword: envelope; Multidrop only)<br />
 In the configuration file, an enhanced syntax is used:<br />
 <code>envelope [&lt;count&gt;] &lt;line&gt;</code> </p>
<p> This option changes the header <code>fetchmail</code> assumes will carry a copy of the mail&#8217;s envelope address. Normally this is &#8216;X-Envelope-To&#8217;. Other typically found headers to carry envelope information are &#8216;X-Original-To&#8217; and &#8216;Delivered-To&#8217;. Now, since these headers are not standardized, practice varies. See the discussion of multidrop address handling below. As a special case, &#8216;envelope &quot;Received&quot;&#8217; enables parsing of sendmail-style Received lines. This is the default, but discouraged because it is not fully reliable. </p>
<p> Note that fetchmail expects the Received-line to be in a specific format: It must contain &quot;by <i>host</i> for <i>address</i>&quot;, where <i>host</i> must match one of the mailserver names that fetchmail recognizes for the account in question. </p>
<p> The optional count argument (only available in the configuration file) determines how many header lines of this kind are skipped. A count of 1 means: skip the first, take the second. A count of 2 means: skip the first and second, take the third, and so on.</p>
<dt><code>-Q &lt;prefix&gt; | &#8211;qvirtual &lt;prefix&gt;</code></p>
<dd> (Keyword: qvirtual; Multidrop only)<br />
 The string prefix assigned to this option will be removed from the user name found in the header specified with the <i>envelope</i> option (<i>before</i> doing multidrop name mapping or localdomain checking, if either is applicable). This option is useful if you are using <code>fetchmail</code> to collect the mail for an entire domain and your ISP (or your mail redirection provider) is using qmail. One of the basic features of qmail is the <i>Delivered-To:</i> message header. Whenever qmail delivers a message to a local mailbox it puts the username and hostname of the envelope recipient on this line. The major reason for this is to prevent mail loops. To set up qmail to batch mail for a disconnected site the ISP-mailhost will have normally put that site in its &#8216;Virtualhosts&#8217; control file so it will add a prefix to all mail addresses for this site. This results in mail sent to &#8216;username [at] userhost.userdom.dom.com&#8217; having a <i>Delivered-To:</i> line of the form:</p>
<dt>
<dd> Delivered-To: mbox-userstr-username [at] userhost.example.com</p>
<dt>
<dd> The ISP can make the &#8216;mbox-userstr-&#8216; prefix anything they choose but a string matching the user host name is likely. By using the option &#8216;envelope Delivered-To:&#8217; you can make fetchmail reliably identify the original envelope recipient, but you have to strip the &#8216;mbox-userstr-&#8216; prefix to deliver to the correct user. This is what this option is for.</p>
<dt><code>&#8211;configdump</code></p>
<dd> Parse the <i>~/.fetchmailrc</i> file, interpret any command-line options specified, and dump a configuration report to standard output. The configuration report is a data structure assignment in the language Python. This option is meant to be used with an interactive <i>~/.fetchmailrc</i> editor like <code>fetchmailconf</code>, written in Python.</p>
<dt><code>-y | &#8211;yydebug</code></p>
<dd> Enables parser debugging, this option is meant to be used by developers only. </p>
</dl>
<h3>Removed Options</h3>
<dl>
<dt><code>-T | &#8211;netsec</code></p>
<dd> Removed before version 6.3.0, the required underlying inet6_apps library had been discontinued and is no longer available. </p>
</dl>
<h2>USER AUTHENTICATION AND ENCRYPTION</h2>
<p> All modes except ETRN require authentication of the client to the server. Normal user authentication in <code>fetchmail</code> is very much like the authentication mechanism of <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1). The correct user-id and password depend upon the underlying security system at the mailserver. </p>
<p> If the mailserver is a Unix machine on which you have an ordinary user account, your regular login name and password are used with <code>fetchmail</code>. If you use the same login name on both the server and the client machines, you needn&#8217;t worry about specifying a user-id with the <code>-u</code> option &#8212; the default behavior is to use your login name on the client machine as the user-id on the server machine. If you use a different login name on the server machine, specify that login name with the <code>-u</code> option. e.g. if your login name is &#8216;jsmith&#8217; on a machine named &#8216;mailgrunt&#8217;, you would start <code>fetchmail</code> as follows:</p>
<dl>
<dt>
<dd> fetchmail -u jsmith mailgrunt</dl>
<p> The default behavior of <code>fetchmail</code> is to prompt you for your mailserver password before the connection is established. This is the safest way to use <code>fetchmail</code> and ensures that your password will not be compromised. You may also specify your password in your <i>~/.fetchmailrc</i> file. This is convenient when using <code>fetchmail</code> in daemon mode or with scripts. </p>
<h3>Using netrc files</h3>
<p> If you do not specify a password, and <code>fetchmail</code> cannot extract one from your <i>~/.fetchmailrc</i> file, it will look for a <i>~/.netrc</i> file in your home directory before requesting one interactively; if an entry matching the mailserver is found in that file, the password will be used. Fetchmail first looks for a match on poll name; if it finds none, it checks for a match on via name. See the <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) man page for details of the syntax of the <i>~/.netrc</i> file. To show a practical example, a .netrc might look like this:</p>
<dl>
<dt>
<dd>
<pre>
machine hermes.example.org
login joe
password topsecret
</pre>
</dl>
<p> You can repeat this block with different user information if you need to provide more than one password. </p>
<p> This feature may allow you to avoid duplicating password information in more than one file. </p>
<p> On mailservers that do not provide ordinary user accounts, your user-id and password are usually assigned by the server administrator when you apply for a mailbox on the server. Contact your server administrator if you don&#8217;t know the correct user-id and password for your mailbox account.</p>
<h2>POP3 VARIANTS</h2>
<p> Early versions of POP3 (RFC1081, RFC1225) supported a crude form of independent authentication using the <i>.rhosts</i> file on the mailserver side. Under this RPOP variant, a fixed per-user ID equivalent to a password was sent in clear over a link to a reserved port, with the command RPOP rather than PASS to alert the server that it should do special checking. RPOP is supported by <code>fetchmail</code> (you can specify &#8216;protocol RPOP&#8217; to have the program send &#8216;RPOP&#8217; rather than &#8216;PASS&#8217;) but its use is strongly discouraged, and support will be removed from a future fetchmail version. This facility was vulnerable to spoofing and was withdrawn in RFC1460. </p>
<p> RFC1460 introduced APOP authentication. In this variant of POP3, you register an APOP password on your server host (on some servers, the program to do this is called <code><a href="/docs/linux/man/8-popauth/">popauth</a></code>(8)). You put the same password in your <i>~/.fetchmailrc</i> file. Each time <code>fetchmail</code> logs in, it sends an MD5 hash of your password and the server greeting time to the server, which can verify it by checking its authorization database. </p>
<p> <code>Note that APOP is no longer considered resistant against man-in-the-middle attacks.</code></p>
<h3>RETR or TOP</h3>
<p> <code>fetchmail</code> makes some efforts to make the server believe messages had not been retrieved, by using the TOP command with a large number of lines when possible. TOP is a command that retrieves the full header and a <code>fetchmail</code>-specified amount of body lines. It is optional and therefore not implemented by all servers, and some are known to implement it improperly. On many servers however, the RETR command which retrieves the full message with header and body, sets the &quot;seen&quot; flag (for instance, in a web interface), whereas the TOP command does not do that. </p>
<p> <code>fetchmail</code> will always use the RETR command if &quot;fetchall&quot; is set. <code>fetchmail</code> will also use the RETR command if &quot;keep&quot; is set and &quot;uidl&quot; is unset. Finally, <code>fetchmail</code> will use the RETR command on Maillennium POP3/PROXY servers (used by Comcast) to avoid a deliberate TOP misinterpretation in this server that causes message corruption. </p>
<p> In all other cases, <code>fetchmail</code> will use the TOP command. This implies that in &quot;keep&quot; setups, &quot;uidl&quot; must be set if &quot;TOP&quot; is desired. </p>
<p> <code>Note</code> that this description is true for the current version of fetchmail, but the behavior may change in future versions. In particular, fetchmail may prefer the RETR command because the TOP command causes much grief on some servers and is only optional.</p>
<h2>ALTERNATE AUTHENTICATION FORMS</h2>
<p> If your <code>fetchmail</code> was built with Kerberos support and you specify Kerberos authentication (either with &#8211;auth or the <i>.fetchmailrc</i> option <code>authenticate kerberos_v4</code>) it will try to get a Kerberos ticket from the mailserver at the start of each query. Note: if either the pollname or via name is &#8216;hesiod&#8217;, fetchmail will try to use Hesiod to look up the mailserver. </p>
<p> If you use POP3 or IMAP with GSSAPI authentication, <code>fetchmail</code> will expect the server to have RFC1731- or RFC1734-conforming GSSAPI capability, and will use it. Currently this has only been tested over Kerberos V, so you&#8217;re expected to already have a ticket-granting ticket. You may pass a username different from your principal name using the standard <code>&#8211;user</code> command or by the <i>.fetchmailrc</i> option <code>user</code>. </p>
<p> If your IMAP daemon returns the PREAUTH response in its greeting line, fetchmail will notice this and skip the normal authentication step. This can be useful, e.g. if you start imapd explicitly using ssh. In this case you can declare the authentication value &#8216;ssh&#8217; on that site entry to stop <i>.fetchmail</i> from asking you for a password when it starts up. </p>
<p> If you use client authentication with <i>TLS1</i> and your IMAP daemon returns the <i>AUTH=EXTERNAL</i> response, fetchmail will notice this and will use the authentication shortcut and will not send the passphrase. In this case you can declare the authentication value &#8216;external&#8217;<br />
&nbsp;on that site to stop&nbsp;<code>fetchmail</code>&nbsp;from asking you for a password when it starts up. </p>
<p> If you are using POP3, and the server issues a one-time-password challenge conforming to RFC1938, <code>fetchmail</code> will use your password as a pass phrase to generate the required response. This avoids sending secrets over the net unencrypted. </p>
<p> Compuserve&#8217;s RPA authentication is supported. If you compile in the support, <code>fetchmail</code> will try to perform an RPA pass-phrase authentication instead of sending over the password en clair if it detects &quot;@compuserve.com&quot; in the hostname. </p>
<p> If you are using IMAP, Microsoft&#8217;s NTLM authentication (used by Microsoft Exchange) is supported. If you compile in the support, <code>fetchmail</code> will try to perform an NTLM authentication (instead of sending over the password en clair) whenever the server returns AUTH=NTLM in its capability response. Specify a user option value that looks like &#8216;user [at] domain&#8217;: the part to the left of the @ will be passed as the username and the part to the right as the NTLM domain. </p>
<h3>Secure Socket Layers (SSL) and Transport Layer Security (TLS)</h3>
<p> All retrieval protocols can use SSL or TLS wrapping for the transport. Additionally, POP3 and IMAP retrival can also negotiate SSL/TLS by means of STARTTLS (or STLS). </p>
<p> Note that fetchmail currently uses the OpenSSL library, which is severely underdocumented, so failures may occur just because the programmers are not aware of OpenSSL&#8217;s requirement of the day. For instance, since v6.3.16, fetchmail calls OpenSSL_add_all_algorithms(), which is necessary to support certificates using SHA256 on OpenSSL 0.9.8 &#8212; this information is deeply hidden in the documentation and not at all obvious. Please do not hesitate to report subtle SSL failures. </p>
<p> You can access SSL encrypted services by specifying the options starting with &#8211;ssl, such as &#8211;ssl, &#8211;sslproto, &#8211;sslcertck, and others. You can also do this using the corresponding user options in the .fetchmailrc file. Some services, such as POP3 and IMAP, have different well known ports defined for the SSL encrypted services. The encrypted ports will be selected automatically when SSL is enabled and no explicit port is specified. Also, the &#8211;sslcertck command line or sslcertck run control file option should be used to force strict certificate checking with older fetchmail versions &#8211; see below. </p>
<p> If SSL is not configured, fetchmail will usually opportunistically try to use STARTTLS. STARTTLS can be enforced by using &#8211;sslproto~auto and defeated by using &#8211;sslproto~&#8221;. TLS connections use the same port as the unencrypted version of the protocol and negotiate TLS via special command. The &#8211;sslcertck command line or sslcertck run control file option should be used to force strict certificate checking &#8211; see below. </p>
<p> <code>&#8211;sslcertck is recommended:</code> When connecting to an SSL or TLS encrypted server, the server presents a certificate to the client for validation. The certificate is checked to verify that the common name in the certificate matches the name of the server being contacted and that the effective and expiration dates in the certificate indicate that it is currently valid. If any of these checks fail, a warning message is printed, but the connection continues. The server certificate does not need to be signed by any specific Certifying Authority and may be a &quot;self-signed&quot; certificate. If the &#8211;sslcertck command line option or sslcertck run control file option is used, fetchmail will instead abort if any of these checks fail, because it must assume that there is a man-in-the-middle attack in this scenario, hence fetchmail must not expose cleartext passwords. Use of the sslcertck or &#8211;sslcertck option is therefore advised; it has become the default in fetchmail 6.4.0. </p>
<p> Some SSL encrypted servers may request a client side certificate. A client side public SSL certificate and private SSL key may be specified. If requested by the server, the client certificate is sent to the server for validation. Some servers may require a valid client certificate and may refuse connections if a certificate is not provided or if the certificate is not valid. Some servers may require client side certificates be signed by a recognized Certifying Authority. The format for the key files and the certificate files is that required by the underlying SSL libraries (OpenSSL in the general case). </p>
<p> A word of care about the use of SSL: While above mentioned setup with self-signed server certificates retrieved over the wires can protect you from a passive eavesdropper, it doesn&#8217;t help against an active attacker. It&#8217;s clearly an improvement over sending the passwords in clear, but you should be aware that a man-in-the-middle attack is trivially possible (in particular with tools such as ). Use of strict certificate checking with a certification authority recognized by server and client, or perhaps of an SSH tunnel (see below for some examples) is preferable if you care seriously about the security of your mailbox and passwords. </p>
<h3>ESMTP AUTH</h3>
<p> <code>fetchmail</code> also supports authentication to the ESMTP server on the client side according to RFC 2554. You can specify a name/password pair to be used with the keywords &#8216;esmtpname&#8217; and &#8216;esmtppassword&#8217;; the former defaults to the username of the calling user. </p>
<h2>DAEMON MODE</h2>
<h3>Introducing the daemon mode</h3>
<p> In daemon mode, <code>fetchmail</code> puts itself into the background and runs forever, querying each specified host and then sleeping for a given polling interval.</p>
<h3>Starting the daemon mode</h3>
<p> There are several ways to make fetchmail work in daemon mode. On the command line, <code>&#8211;daemon&nbsp;&lt;interval&gt;</code> or <code>-d&nbsp;&lt;interval&gt;</code> option runs <code>fetchmail</code> in daemon mode. You must specify a numeric argument which is a polling interval (time to wait after completing a whole poll cycle with the last server and before starting the next poll cycle with the first server) in seconds. </p>
<p> Example: simply invoking</p>
<dl>
<dt>
<dd> fetchmail -d 900</dl>
<p> will, therefore, poll all the hosts described in your <i>~/.fetchmailrc</i> file (except those explicitly excluded with the &#8216;skip&#8217; verb) a bit less often than once every 15 minutes (exactly: 15 minutes + time that the poll takes). </p>
<p> It is also possible to set a polling interval in your <i>~/.fetchmailrc</i> file by saying &#8216;set daemon&nbsp;&lt;interval&gt;&#8217;, where &lt;interval&gt; is an integer number of seconds. If you do this, fetchmail will always start in daemon mode unless you override it with the command-line option &#8211;daemon 0 or -d0. </p>
<p> Only one daemon process is permitted per user; in daemon mode, <code>fetchmail</code> sets up a per-user lockfile to guarantee this. (You can however cheat and set the FETCHMAILHOME environment variable to overcome this setting, but in that case, it is your responsibility to make sure you aren&#8217;t polling the same server with two processes at the same time.)</p>
<h3>Awakening the background daemon</h3>
<p> Normally, calling fetchmail with a daemon in the background sends a wake-up signal to the daemon and quits without output. The background daemon then starts its next poll cycle immediately. The wake-up signal, SIGUSR1, can also be sent manually. The wake-up action also clears any &#8216;wedged&#8217; flags indicating that connections have wedged due to failed authentication or multiple timeouts.</p>
<h3>Terminating the background daemon</h3>
<p> The option <code>-q</code> or <code>&#8211;quit</code> will kill a running daemon process instead of waking it up (if there is no such process, <code>fetchmail</code> will notify you). If the &#8211;quit option appears last on the command line, <code>fetchmail</code> will kill the running daemon process and then quit. Otherwise, <code>fetchmail</code> will first kill a running daemon process and then continue running with the other options.</p>
<h3>Useful options for daemon mode</h3>
<p> The <code>-L &lt;filename&gt;</code> or <code>&#8211;logfile &lt;filename&gt;</code> option (keyword: set logfile) is only effective when fetchmail is detached and in daemon mode. Note that <code>the logfile must exist before</code> fetchmail is run, you can use the <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command with the filename as its sole argument to create it.<br />
 This option allows you to redirect status messages into a specified logfile (follow the option with the logfile name). The logfile is opened for append, so previous messages aren&#8217;t deleted. This is primarily useful for debugging configurations. Note that fetchmail does not detect if the logfile is rotated, the logfile is only opened once when fetchmail starts. You need to restart fetchmail after rotating the logfile and before compressing it (if applicable). </p>
<p> The <code>&#8211;syslog</code> option (keyword: set syslog) allows you to redirect status and error messages emitted to the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) system daemon if available. Messages are logged with an id of <code>fetchmail</code>, the facility <code>LOG_MAIL</code>, and priorities <code>LOG_ERR</code>, <code>LOG_ALERT</code> or <code>LOG_INFO</code>. This option is intended for logging status and error messages which indicate the status of the daemon and the results while fetching mail from the server(s). Error messages for command line options and parsing the <i>.fetchmailrc</i> file are still written to stderr, or to the specified log file. The <code>&#8211;nosyslog</code> option turns off use of <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), assuming it&#8217;s turned on in the <i>~/.fetchmailrc</i> file. This option is overridden, in certain situations, by <code>&#8211;logfile</code> (which see). </p>
<p> The <code>-N</code> or <code>&#8211;nodetach</code> option suppresses backgrounding and detachment of the daemon process from its control terminal. This is useful for debugging or when fetchmail runs as the child of a supervisor process such as <code><a href="/docs/linux/man/8-init/">init</a></code>(8) or Gerrit Pape&#8217;s <code><a href="/docs/linux/man/8-runit/">runit</a></code>(8). Note that this also causes the logfile option to be ignored. </p>
<p> Note that while running in daemon mode polling a POP2 or IMAP2bis server, transient errors (such as DNS failures or sendmail delivery refusals) may force the fetchall option on for the duration of the next polling cycle. This is a robustness feature. It means that if a message is fetched (and thus marked seen by the mailserver) but not delivered locally due to some transient error, it will be re-fetched during the next poll cycle. (The IMAP logic doesn&#8217;t delete messages until they&#8217;re delivered, so this problem does not arise.) </p>
<p> If you touch or change the <i>~/.fetchmailrc</i> file while fetchmail is running in daemon mode, this will be detected at the beginning of the next poll cycle. When a changed <i>~/.fetchmailrc</i> is detected, fetchmail rereads it and restarts from scratch (using <a href="/docs/linux/man/2-exec/">exec</a>(2); no state information is retained in the new instance). Note that if fetchmail needs to query for passwords, of that if you break the <i>~/.fetchmailrc</i> file&#8217;s syntax, the new instance will softly and silently vanish away on startup. </p>
<h2>ADMINISTRATIVE OPTIONS</h2>
<p> The <code>&#8211;postmaster &lt;name&gt;</code> option (keyword: set postmaster) specifies the last-resort username to which multidrop mail is to be forwarded if no matching local recipient can be found. It is also used as destination of undeliverable mail if the &#8216;bouncemail&#8217; global option is off and additionally for spam-blocked mail if the &#8216;bouncemail&#8217; global option is off and the &#8216;spambounce&#8217; global option is on. This option defaults to the user who invoked <code>fetchmail</code>. If the invoking user is root, then the default of this option is the user &#8216;postmaster&#8217;. Setting postmaster to the empty string causes such mail as described above to be discarded &#8211; this however is usually a bad idea. See also the description of the &#8216;FETCHMAILUSER&#8217; environment variable in the ENVIRONMENT section below. </p>
<p> The <code>&#8211;nobounce</code> behaves like the &quot;set no bouncemail&quot; global option, which see. </p>
<p> The <code>&#8211;invisible</code> option (keyword: set invisible) tries to make fetchmail invisible. Normally, fetchmail behaves like any other MTA would &#8212; it generates a Received header into each message describing its place in the chain of transmission, and tells the MTA it forwards to that the mail came from the machine fetchmail itself is running on. If the invisible option is on, the Received header is suppressed and fetchmail tries to spoof the MTA it forwards to into thinking it came directly from the mailserver host. </p>
<p> The <code>&#8211;showdots</code> option (keyword: set showdots) forces fetchmail to show progress dots even if the output goes to a file or fetchmail is not in verbose mode. Fetchmail shows the dots by default when run in &#8211;verbose mode <i>and</i> output goes to console. This option is ignored in &#8211;silent mode. </p>
<p> By specifying the <code>&#8211;tracepolls</code> option, you can ask fetchmail to add information to the Received header on the form &quot;polling {label} account {user}&quot;, where {label} is the account label (from the specified rcfile, normally ~/.fetchmailrc) and {user} is the username which is used to log on to the mail server. This header can be used to make filtering email where no useful header information is available and you want mail from different accounts sorted into different mailboxes (this could, for example, occur if you have an account on the same server running a mailing list, and are subscribed to the list using that account). The default is not adding any such header. In <i>.fetchmailrc</i>, this is called &#8216;tracepolls&#8217;. </p>
<h2>RETRIEVAL FAILURE MODES</h2>
<p> The protocols <code>fetchmail</code> uses to talk to mailservers are next to bulletproof. In normal operation forwarding to port 25, no message is ever deleted (or even marked for deletion) on the host until the SMTP listener on the client side has acknowledged to <code>fetchmail</code> that the message has been either accepted for delivery or rejected due to a spam block. </p>
<p> When forwarding to an MDA, however, there is more possibility of error. Some MDAs are &#8216;safe&#8217; and reliably return a nonzero status on any delivery error, even one due to temporary resource limits. The <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1) program is like this; so are most programs designed as mail transport agents, such as <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), including the sendmail wrapper of Postfix and <code><a href="/docs/linux/man/1-exim/">exim</a></code>(1). These programs give back a reliable positive acknowledgement and can be used with the mda option with no risk of mail loss. Unsafe MDAs, though, may return 0 even on delivery failure. If this happens, you will lose mail. </p>
<p> The normal mode of <code>fetchmail</code> is to try to download only &#8216;new&#8217; messages, leaving untouched (and undeleted) messages you have already read directly on the server (or fetched with a previous <i>fetchmail &#8211;keep</i>). But you may find that messages you&#8217;ve already read on the server are being fetched (and deleted) even when you don&#8217;t specify &#8211;all. There are several reasons this can happen. </p>
<p> One could be that you&#8217;re using POP2. The POP2 protocol includes no representation of &#8216;new&#8217; or &#8216;old&#8217; state in messages, so <code>fetchmail</code> must treat all messages as new all the time. But POP2 is obsolete, so this is unlikely. </p>
<p> A potential POP3 problem might be servers that insert messages in the middle of mailboxes (some VMS implementations of mail are rumored to do this). The <code>fetchmail</code> code assumes that new messages are appended to the end of the mailbox; when this is not true it may treat some old messages as new and vice versa. Using UIDL whilst setting fastuidl 0 might fix this, otherwise, consider switching to IMAP. </p>
<p> Yet another POP3 problem is that if they can&#8217;t make tempfiles in the user&#8217;s home directory, some POP3 servers will hand back an undocumented response that causes fetchmail to spuriously report &quot;No mail&quot;. </p>
<p> The IMAP code uses the presence or absence of the server flag \Seen to decide whether or not a message is new. This isn&#8217;t the right thing to do, fetchmail should check the UIDVALIDITY and use UID, but it doesn&#8217;t do that yet. Under Unix, it counts on your IMAP server to notice the BSD-style Status flags set by mail user agents and set the \Seen flag from them when appropriate. All Unix IMAP servers we know of do this, though it&#8217;s not specified by the IMAP RFCs. If you ever trip over a server that doesn&#8217;t, the symptom will be that messages you have already read on your host will look new to the server. In this (unlikely) case, only messages you fetched with <i>fetchmail &#8211;keep</i> will be both undeleted and marked old. </p>
<p> In ETRN and ODMR modes, <code>fetchmail</code> does not actually retrieve messages; instead, it asks the server&#8217;s SMTP listener to start a queue flush to the client via SMTP. Therefore it sends only undelivered messages. </p>
<h2>SPAM FILTERING</h2>
<p> Many SMTP listeners allow administrators to set up &#8216;spam filters&#8217; that block unsolicited email from specified domains. A MAIL FROM or DATA line that triggers this feature will elicit an SMTP response which (unfortunately) varies according to the listener. </p>
<p> Newer versions of <code>sendmail</code> return an error code of 571. </p>
<p> According to RFC2821, the correct thing to return in this situation is 550 &quot;Requested action not taken: mailbox unavailable&quot; (the draft adds &quot;[E.g., mailbox not found, no access, or command rejected for policy reasons].&quot;). </p>
<p> Older versions of the <code>exim</code> MTA return 501 &quot;Syntax error in parameters or arguments&quot;. </p>
<p> The <code>postfix</code> MTA runs 554 as an antispam response. </p>
<p> <code>Zmailer</code> may reject code with a 500 response (followed by an enhanced status code that contains more information). </p>
<p> Return codes which <code>fetchmail</code> treats as antispam responses and discards the message can be set with the &#8216;antispam&#8217; option. This is one of the <i>only</i> three circumstance under which fetchmail ever discards mail (the others are the 552 and 553 errors described below, and the suppression of multidropped messages with a message-ID already seen). </p>
<p> If <code>fetchmail</code> is fetching from an IMAP server, the antispam response will be detected and the message rejected immediately after the headers have been fetched, without reading the message body. Thus, you won&#8217;t pay for downloading spam message bodies. </p>
<p> By default, the list of antispam responses is empty. </p>
<p> If the <i>spambounce</i> global option is on, mail that is spam-blocked triggers an RFC1892/RFC1894 bounce message informing the originator that we do not accept mail from it. See also BUGS. </p>
<h2>SMTP/ESMTP ERROR HANDLING</h2>
<p> Besides the spam-blocking described above, fetchmail takes special actions &#8212; that may be modified by the &#8211;softbounce option &#8212; on the following SMTP/ESMTP error response codes</p>
<dl>
<dt>452 (insufficient system storage)</p>
<dd> Leave the message in the server mailbox for later retrieval.</p>
<dt>552 (message exceeds fixed maximum message size)</p>
<dd> Delete the message from the server. Send bounce-mail to the originator.</p>
<dt>553 (invalid sending domain)</p>
<dd> Delete the message from the server. Don&#8217;t even try to send bounce-mail to the originator.</dl>
<p> Other errors greater or equal to 500 trigger bounce mail back to the originator, unless suppressed by &#8211;softbounce. See also BUGS. </p>
<h2>THE RUN CONTROL FILE</h2>
<p> The preferred way to set up fetchmail is to write a <i>.fetchmailrc</i> file in your home directory (you may do this directly, with a text editor, or indirectly via <code>fetchmailconf</code>). When there is a conflict between the command-line arguments and the arguments in this file, the command-line arguments take precedence. </p>
<p> To protect the security of your passwords, your <i>~/.fetchmailrc</i> may not normally have more than 0700 (u=rwx,g=,o=) permissions; <code>fetchmail</code> will complain and exit otherwise (this check is suppressed when &#8211;version is on). </p>
<p> You may read the <i>.fetchmailrc</i> file as a list of commands to be executed when <code>fetchmail</code> is called with no arguments.</p>
<h3>Run Control Syntax</h3>
<p> Comments begin with a &#8216;#&#8217; and extend through the end of the line. Otherwise the file consists of a series of server entries or global option statements in a free-format, token-oriented syntax. </p>
<p> There are four kinds of tokens: grammar keywords, numbers (i.e. decimal digit sequences), unquoted strings, and quoted strings. A quoted string is bounded by double quotes and may contain whitespace (and quoted digits are treated as a string). Note that quoted strings will also contain line feed characters if they run across two or more lines, unless you use a backslash to join lines (see below). An unquoted string is any whitespace-delimited token that is neither numeric, string quoted nor contains the special characters &#8216;,&#8217;, &#8216;;&#8217;, &#8216;:&#8217;, or &#8216;=&#8217;. </p>
<p> Any amount of whitespace separates tokens in server entries, but is otherwise ignored. You may use backslash escape sequences (
 for LF, 	 for HT,  for BS,  for CR, \<i>nnn</i> for decimal (where nnn cannot start with a 0), 
