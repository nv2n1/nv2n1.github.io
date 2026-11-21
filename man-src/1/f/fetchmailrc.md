---

title: "fetchmailrc(1)"
name: "fetchmailrc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fetchmailrc/"
description: "fetchmail – fetch mail from a POP, IMAP, ETRN, or ODMR-capable server"
---

<p> <code>fetchmail</code> [<i>option...</i>] [<i>mailserver...</i>] <br />
 <code>fetchmailconf</code> </p>
<p> <code>fetchmail</code> is a mail-retrieval and forwarding utility; it fetches mail from remote mailservers and forwards it to your local (client) machine&#8217;s delivery system. You can then handle the retrieved mail using normal mail user agents such as <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code>elm</code>(1) or <code><a href="/docs/linux/man/1-Mail/">Mail</a></code>(1). The <code>fetchmail</code> utility can be run in a daemon mode to repeatedly poll one or more systems at a specified interval. </p>
<p> The <code>fetchmail</code> program can gather mail from servers supporting any of the common mail-retrieval protocols: POP2 (legacy, to be removed from future release), POP3, IMAP2bis, IMAP4, and IMAP4rev1. It can also use the ESMTP ETRN extension and ODMR. (The RFCs describing all these protocols are listed at the end of this manual page.) </p>
<p> While <code>fetchmail</code> is primarily intended to be used over on-demand TCP/IP links (such as SLIP or PPP connections), it may also be useful as a message transfer agent for sites which refuse for security reasons to permit (sender-initiated) SMTP transactions with sendmail. </p>
<h3>SUPPORT, TROUBLESHOOTING</h3>
<p> For troubleshooting, tracing and debugging, you need to increase fetchmail&#8217;s verbosity to actually see what happens. To do that, please run <code>both of the two following commands, adding all of the options you&#8217;d normally use.</code> </p>
<dl>
<dd> <pre><code>env LC_ALL=C fetchmail -V -v --nodetach --nosyslog
</code></pre>
 </dd>
<dd> <p> (This command line prints in English how fetchmail understands your configuration.) </p>
 </dd>
<dd> <pre><code>env LC_ALL=C fetchmail -vvv --nodetach --nosyslog
</code></pre>
 </dd>
<dd> <p> (This command line actually runs fetchmail with verbose English output.) </p>
 </dd></dl>
<p> Also see </p>
<p> You can omit the LC_ALL=C part above if you want output in the local language (if supported). However if you are posting to mailing lists, please leave it in. The maintainers do not necessarily understand your language, please use English. </p>
<h3>CONCEPTS</h3>
<p> If <code>fetchmail</code> is used with a POP or an IMAP server (but not with ETRN or ODMR), it has two fundamental modes of operation for each user account from which it retrieves mail: <i>singledrop</i>- and <i>multidrop</i>-mode. </p>
<dl>
<dt>In singledrop-mode,</dt>
<dd> <p> <code>fetchmail</code> assumes that all messages in the user&#8217;s account (mailbox) are intended for a single recipient. The identity of the recipient will either default to the local user currently executing <code>fetchmail</code>, or will need to be explicitly specified in the configuration file. </p>
 </dd>
<dd> <p> <code>fetchmail</code> uses singledrop-mode when the fetchmailrc configuration contains at most a single local user specification for a given server account. </p>
 </dd>
<dt>In multidrop-mode,</dt>
<dd> <p> <code>fetchmail</code> assumes that the mail server account actually contains mail intended for any number of different recipients. Therefore, <code>fetchmail</code> must attempt to deduce the proper &quot;envelope recipient&quot; from the mail headers of each message. In this mode of operation, <code>fetchmail</code> almost resembles a mail transfer agent (MTA). </p>
 </dd>
<dd> <p> Note that neither the POP nor IMAP protocols were intended for use in this fashion, and hence envelope information is often not directly available. The ISP must stores the envelope information in some message header <code>and</code>. The ISP must also store one copy of the message per recipient. If either of the conditions is not fulfilled, this process is unreliable, because <code>fetchmail</code> must then resort to guessing the true envelope recipient(s) of a message. This usually fails for mailing list messages and Bcc:d mail, or mail for multiple recipients in your domain. </p>
 </dd>
<dd> <p> <code>fetchmail</code> uses multidrop-mode when more than one local user and/or a wildcard is specified for a particular server account in the configuration file. </p>
 </dd>
<dt>In ETRN and ODMR modes,</dt>
<dd> <p> these considerations do not apply, as these protocols are based on SMTP, which provides explicit envelope recipient information. These protocols always support multiple recipients. </p>
 </dd></dl>
<p> As each message is retrieved, <code>fetchmail</code> normally delivers it via SMTP to port 25 on the machine it is running on (localhost), just as though it were being passed in over a normal TCP/IP link. <code>fetchmail</code> provides the SMTP server with an envelope recipient derived in the manner described previously. The mail will then be delivered according to your MTA&#8217;s rules (the Mail Transfer Agent is usually <code>sendmail</code>(8), <code><a href="/docs/linux/man/8-exim/">exim</a></code>(8), or <code>postfix</code>(8)). Invoking your system&#8217;s MDA (Mail Delivery Agent) is the duty of your MTA. All the delivery-control mechanisms (such as <i>.forward</i> files) normally available through your system MTA and local delivery agents will therefore be applied as usual. </p>
<p> If your fetchmail configuration sets a local MDA (see the --mda option), it will be used directly instead of talking SMTP to port 25. </p>
<p> If the program <code>fetchmailconf</code> is available, it will assist you in setting up and editing a fetchmailrc configuration. It runs under the X window system and requires that the language Python and the Tk toolkit (with Python bindings) be present on your system. If you are first setting up fetchmail for single-user mode, it is recommended that you use Novice mode. Expert mode provides complete control of fetchmail configuration, including the multidrop features. In either case, the &#8216;Autoprobe&#8217; button will tell you the most capable protocol a given mailserver supports, and warn you of potential problems with that server. </p>
<h2>GENERAL OPERATION</h2>
<p> The behavior of <code>fetchmail</code> is controlled by command-line options and a run control file, <i>~/.fetchmailrc</i>, the syntax of which we describe in a later section (this file is what the <code>fetchmailconf</code> program edits). Command-line options override <i>~/.fetchmailrc</i> declarations. </p>
<p> Each server name that you specify following the options on the command line will be queried. If you do not specify any servers on the command line, each &#8216;poll&#8217; entry in your <i>~/.fetchmailrc</i> file will be queried, unless the idle option is used, which see. </p>
<p> To facilitate the use of <code>fetchmail</code> in scripts and pipelines, it returns an appropriate exit code upon termination -- see EXIT CODES below. </p>
<p> The following options modify the behavior of <code>fetchmail</code>. It is seldom necessary to specify any of these once you have a working <i>.fetchmailrc</i> file set up. </p>
<p> Almost all options have a corresponding keyword which can be used to declare them in a <i>.fetchmailrc</i> file. </p>
<p> Some special options are not covered here, but are documented instead in sections on AUTHENTICATION and DAEMON MODE which follow.  </p>
<h3>General Options</h3>
<dl>
<dt><code>-? | --help</code></dt>
<dd> <p> Displays option help. </p>
 </dd>
<dt><code>-V | --version</code></dt>
<dd> <p> Displays the version information for your copy of <code>fetchmail</code>. No mail fetch is performed. Instead, for each server specified, all the option information that would be computed if <code>fetchmail</code> were connecting to that server is displayed. Any non-printables in passwords or other string names are shown as backslashed C-like escape sequences. This option is useful for verifying that your options are set the way you want them. </p>
 </dd>
<dt><code>-c | --check</code></dt>
<dd> <p> Return a status code to indicate whether there is mail waiting, without actually fetching or deleting mail (see EXIT CODES below). This option turns off daemon mode (in which it would be useless). It doesn&#8217;t play well with queries to multiple sites, and doesn&#8217;t work with ETRN or ODMR. It will return a false positive if you leave read but undeleted mail in your server mailbox and your fetch protocol can&#8217;t tell kept messages from new ones. This means it will work with IMAP, not work with POP2, and may occasionally flake out under POP3. </p>
 </dd>
<dt><code>-s | --silent</code></dt>
<dd> <p> Silent mode. Suppresses all progress/status messages that are normally echoed to standard output during a fetch (but does not suppress actual error messages). The --verbose option overrides this. </p>
 </dd>
<dt><code>-v | --verbose</code></dt>
<dd> <p> Verbose mode. All control messages passed between <code>fetchmail</code> and the mailserver are echoed to stdout. Overrides --silent. Doubling this option (-v -v) causes extra diagnostic information to be printed. </p>
 </dd>
<dt><code>--nosoftbounce</code></dt>
<dd> <p> (since v6.3.10, Keyword: set no softbounce, since v6.3.10) <br />
 Hard bounce mode. All permanent delivery errors cause messages to be deleted from the upstream server, see &quot;no softbounce&quot; below. </p>
 </dd>
<dt><code>--softbounce</code></dt>
<dd> <p> (since v6.3.10, Keyword: set softbounce, since v6.3.10) <br />
 Soft bounce mode. All permanent delivery errors cause messages to be left on the upstream server if the protocol supports that. <code>This option is on by default to match historic fetchmail documentation,</code> and will be changed to hard bounce mode in the next fetchmail release. </p>
 </dd></dl>
<h3>Disposal Options</h3>
<dl>
<dt><code>-a | --all | (since v6.3.3) --fetchall</code></dt>
<dd> <p> (Keyword: fetchall, since v3.0) <br />
 Retrieve both old (seen) and new messages from the mailserver. The default is to fetch only messages the server has not marked seen. Under POP3, this option also forces the use of RETR rather than TOP. Note that POP2 retrieval behaves as though --all is always on (see RETRIEVAL FAILURE MODES below) and this option does not work with ETRN or ODMR. While the -a and --all command-line and fetchall rcfile options have been supported for a long time, the --fetchall command-line option was added in v6.3.3. </p>
 </dd>
<dt><code>-k | --keep</code></dt>
<dd> <p> (Keyword: keep) <br />
 Keep retrieved messages on the remote mailserver. Normally, messages are deleted from the folder on the mailserver after they have been retrieved. Specifying the <code>keep</code> option causes retrieved messages to remain in your folder on the mailserver. This option does not work with ETRN or ODMR. If used with POP3, it is recommended to also specify the --uidl option or uidl keyword. </p>
 </dd>
<dt><code>-K | --nokeep</code></dt>
<dd> <p> (Keyword: nokeep) <br />
 Delete retrieved messages from the remote mailserver. This option forces retrieved mail to be deleted. It may be useful if you have specified a default of <code>keep</code> in your <i>.fetchmailrc</i>. This option is forced on with ETRN and ODMR. </p>
 </dd>
<dt><code>-F | --flush</code></dt>
<dd> <p> (Keyword: flush) <br />
 POP3/IMAP only. This is a dangerous option and can cause mail loss when used improperly. It deletes old (seen) messages from the mailserver before retrieving new messages. <code>Warning:</code> This can cause mail loss if you check your mail with other clients than fetchmail, and cause fetchmail to delete a message it had never fetched before. It can also cause mail loss if the mail server marks the message seen after retrieval (IMAP2 servers). You should probably not use this option in your configuration file. If you use it with POP3, you must use the &#8216;uidl&#8217; option. What you probably want is the default setting: if you don&#8217;t specify &#8216;-k&#8217;, then fetchmail will automatically delete messages after successful delivery. </p>
 </dd>
<dt><code>--limitflush</code></dt>
<dd> <p> POP3/IMAP only, since version 6.3.0. Delete oversized messages from the mailserver before retrieving new messages. The size limit should be separately specified with the --limit option. This option does not work with ETRN or ODMR. </p>
 </dd></dl>
<h3>Protocol and Query Options</h3>
<dl>
<dt><code>-p &lt;proto&gt; | --proto &lt;proto&gt; | --protocol &lt;proto&gt;</code></dt>
<dd> <p> (Keyword: proto[col]) <br />
 Specify the protocol to use when communicating with the remote mailserver. If no protocol is specified, the default is AUTO. <code>proto</code> may be one of the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>AUTO</dt>
<dd> <p> Tries IMAP, POP3, and POP2 (skipping any of these for which support has not been compiled in). </p>
 </dd>
<dt>POP2</dt>
<dd> <p> Post Office Protocol 2 (legacy, to be removed from future release) </p>
 </dd>
<dt>POP3</dt>
<dd> <p> Post Office Protocol 3 </p>
 </dd>
<dt>APOP</dt>
<dd> <p> Use POP3 with old-fashioned MD5-challenge authentication. Considered not resistant to man-in-the-middle attacks. </p>
 </dd>
<dt>RPOP</dt>
<dd> <p> Use POP3 with RPOP authentication. </p>
 </dd>
<dt>KPOP</dt>
<dd> <p> Use POP3 with Kerberos V4 authentication on port 1109. </p>
 </dd>
<dt>SDPS</dt>
<dd> <p> Use POP3 with Demon Internet&#8217;s SDPS extensions. </p>
 </dd>
<dt>IMAP</dt>
<dd> <p> IMAP2bis, IMAP4, or IMAP4rev1 (<code>fetchmail</code> automatically detects their capabilities). </p>
 </dd>
<dt>ETRN</dt>
<dd> <p> Use the ESMTP ETRN option. </p>
 </dd>
<dt>ODMR</dt>
<dd> <p> Use the the On-Demand Mail Relay ESMTP profile. </p>
 </dd></dl>
</dl>
</dl>
<p> All these alternatives work in basically the same way (communicating with standard server daemons to fetch mail already delivered to a mailbox on the server) except ETRN and ODMR. The ETRN mode allows you to ask a compliant ESMTP server (such as BSD sendmail at release 8.8.0 or higher) to immediately open a sender-SMTP connection to your client machine and begin forwarding any items addressed to your client machine in the server&#8217;s queue of undelivered mail. The ODMR mode requires an ODMR-capable server and works similarly to ETRN, except that it does not require the client machine to have a static DNS. </p>
<dl>
<dt><code>-U | --uidl</code></dt>
<dd> <p> (Keyword: uidl) <br />
 Force UIDL use (effective only with POP3). Force client-side tracking of &#8216;newness&#8217; of messages (UIDL stands for &quot;unique ID listing&quot; and is described in RFC1939). Use with &#8216;keep&#8217; to use a mailbox as a baby news drop for a group of users. The fact that seen messages are skipped is logged, unless error logging is done through syslog while running in daemon mode. Note that fetchmail may automatically enable this option depending on upstream server capabilities. Note also that this option may be removed and forced enabled in a future fetchmail version. See also: --idfile. </p>
 </dd>
<dt><code>--idle (since 6.3.3)</code></dt>
<dd> <p> (Keyword: idle, since before 6.0.0) <br />
 Enable IDLE use (effective only with IMAP). Note that this works with only one account and one folder at a given time, other folders or accounts will not be polled when idle is in effect! While the idle rcfile keyword had been supported for a long time, the --idle command-line option was added in version 6.3.3. IDLE use means that fetchmail tells the IMAP server to send notice of new messages, so they can be retrieved sooner than would be possible with regular polls. </p>
 </dd>
<dt><code>-P &lt;portnumber&gt; | --service &lt;servicename&gt;</code></dt>
<dd> <p> (Keyword: service) Since version 6.3.0. <br />
 The service option permits you to specify a service name to connect to. You can specify a decimal port number here, if your services database lacks the required service-port assignments. See the FAQ item R12 and the --ssl documentation for details. This replaces the older --port option. </p>
 </dd>
<dt><code>--port &lt;portnumber&gt;</code></dt>
<dd> <p> (Keyword: port) <br />
 Obsolete version of --service that does not take service names. <code>Note:</code> this option may be removed from a future version. </p>
 </dd>
<dt><code>--principal &lt;principal&gt;</code></dt>
<dd> <p> (Keyword: principal) <br />
 The principal option permits you to specify a service principal for mutual authentication. This is applicable to POP3 or IMAP with Kerberos 4 authentication only. It does not apply to Kerberos 5 or GSSAPI. This option may be removed in a future fetchmail version. </p>
 </dd>
<dt><code>-t &lt;seconds&gt; | --timeout &lt;seconds&gt;</code></dt>
<dd> <p> (Keyword: timeout) <br />
 The timeout option allows you to set a server-nonresponse timeout in seconds. If a mailserver does not send a greeting message or respond to commands for the given number of seconds, <code>fetchmail</code> will drop the connection to it. Without such a timeout <code>fetchmail</code> might hang until the TCP connection times out, trying to fetch mail from a down host, which may be very long. This would be particularly annoying for a <code>fetchmail</code> running in the background. There is a default timeout which fetchmail~-V will report. If a given connection receives too many timeouts in succession, fetchmail will consider it wedged and stop retrying. The calling user will be notified by email if this happens. </p>
 </dd>
<dd> <p> Beginning with fetchmail 6.3.10, the SMTP client uses the recommended minimum timeouts from RFC-5321 while waiting for the SMTP/LMTP server it is talking to. You can raise the timeouts even more, but you cannot shorten them. This is to avoid a painful situation where fetchmail has been configured with a short timeout (a minute or less), ships a long message (many MBytes) to the local MTA, which then takes longer than timeout to respond &quot;OK&quot;, which it eventually will; that would mean the mail gets delivered properly, but fetchmail cannot notice it and will thus refetch this big message over and over again. </p>
 </dd>
<dt><code>--plugin &lt;command&gt;</code></dt>
<dd> <p> (Keyword: plugin) <br />
 The plugin option allows you to use an external program to establish the TCP connection. This is useful if you want to use ssh, or need some special firewalling setup. The program will be looked up in $PATH and can optionally be passed the hostname and port as arguments using &quot;%h&quot; and &quot;%p&quot; respectively (note that the interpolation logic is rather primitive, and these tokens must be bounded by whitespace or beginning of string or end of string). Fetchmail will write to the plugin&#8217;s stdin and read from the plugin&#8217;s stdout. </p>
 </dd>
<dt><code>--plugout &lt;command&gt;</code></dt>
<dd> <p> (Keyword: plugout) <br />
 Identical to the plugin option above, but this one is used for the SMTP connections. </p>
 </dd>
<dt><code>-r &lt;name&gt; | --folder &lt;name&gt;</code></dt>
<dd> <p> (Keyword: folder[s]) <br />
 Causes a specified non-default mail folder on the mailserver (or comma-separated list of folders) to be retrieved. The syntax of the folder name is server-dependent. This option is not available under POP3, ETRN, or ODMR. </p>
 </dd>
<dt><code>--tracepolls</code></dt>
<dd> <p> (Keyword: tracepolls) <br />
 Tell fetchmail to poll trace information in the form &#8216;polling account %s&#8217; and &#8216;folder %s&#8217; to the Received line it generates, where the %s parts are replaced by the user&#8217;s remote name, the poll label, and the folder (mailbox) where available (the Received header also normally includes the server&#8217;s true name). This can be used to facilitate mail filtering based on the account it is being received from. The folder information is written only since version 6.3.4. </p>
 </dd>
<dt><code>--ssl</code></dt>
<dd> <p> (Keyword: ssl) <br />
 Causes the connection to the mail server to be encrypted via SSL, by negotiating SSL directly after connecting (SSL-wrapped mode). Please see the description of --sslproto below! More information is available in the <i>README.SSL</i> file that ships with fetchmail. </p>
 </dd>
<dd> <p> Note that even if this option is omitted, fetchmail may still negotiate SSL in-band for POP3 or IMAP, through the STLS or STARTTLS feature. You can use the --sslproto option to modify that behavior. </p>
 </dd>
<dd> <p> If no port is specified, the connection is attempted to the well known port of the SSL version of the base protocol. This is generally a different port than the port used by the base protocol. For IMAP, this is port 143 for the clear protocol and port 993 for the SSL secured protocol; for POP3, it is port 110 for the clear text and port 995 for the encrypted variant. </p>
 </dd>
<dd> <p> If your system lacks the corresponding entries from /etc/services, see the --service option and specify the numeric port number as given in the previous paragraph (unless your ISP had directed you to different ports, which is uncommon however). </p>
 </dd>
<dt><code>--sslcert &lt;name&gt;</code></dt>
<dd> <p> (Keyword: sslcert) <br />
 For certificate-based client authentication. Some SSL encrypted servers require client side keys and certificates for authentication. In most cases, this is optional. This specifies the location of the public key certificate to be presented to the server at the time the SSL session is established. It is not required (but may be provided) if the server does not require it. It may be the same file as the private key (combined key and certificate file) but this is not recommended. Also see --sslkey below. </p>
<p> <code>NOTE:</code> If you use client authentication, the user name is fetched from the certificate&#8217;s CommonName and overrides the name set with --user. </p>
 </dd>
<dt><code>--sslkey &lt;name&gt;</code></dt>
<dd> <p> (Keyword: sslkey) <br />
 Specifies the file name of the client side private SSL key. Some SSL encrypted servers require client side keys and certificates for authentication. In most cases, this is optional. This specifies the location of the private key used to sign transactions with the server at the time the SSL session is established. It is not required (but may be provided) if the server does not require it. It may be the same file as the public key (combined key and certificate file) but this is not recommended. </p>
 </dd>
<dd> <p> If a password is required to unlock the key, it will be prompted for at the time just prior to establishing the session to the server. This can cause some complications in daemon mode. </p>
 </dd>
<dd> <p> Also see --sslcert above. </p>
 </dd>
<dt><code>--sslproto &lt;value&gt;</code></dt>
<dd> <p> (Keyword: sslproto, NOTE: semantic changes since v6.4.0) <br />
 This option has a dual use, out of historic fetchmail behaviour. It controls both the SSL/TLS protocol version and, if --ssl is not specified, the STARTTLS behaviour (upgrading the protocol to an SSL or TLS connection in-band). Some other options may however make TLS mandatory. </p>
 </dd></dl>
<p> Only if this option and --ssl are both missing for a poll, there will be opportunistic TLS for POP3 and IMAP, where fetchmail will attempt to upgrade to TLSv1 or newer. </p>
<p> Recognized values for --sslproto are given below. You should normally chose one of the auto-negotiating options, i. e. &#8216;<code>auto</code>&#8216; or one of the options ending in a plus (<code>+</code>) character. Note that depending on OpenSSL library version and configuration, some options cause run-time errors because the requested SSL or TLS versions are not supported by the particular installed OpenSSL library. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>&#8216;&#8216;</code>, the empty string</dt>
<dd> <p> Disable STARTTLS. If --ssl is given for the same server, log an error and pretend that &#8216;<code>auto</code>&#8216; had been used instead. </p>
 </dd>
<dt>&#8216;<code>auto</code>&#8216;</dt>
<dd> <p> (default). Since v6.4.0. Require TLS. Auto-negotiate TLSv1 or newer, disable SSLv3 downgrade. (fetchmail 6.3.26 and older have auto-negotiated all protocols that their OpenSSL library supported, including the broken SSLv3). </p>
 </dd>
<dt>&#8216;<code>SSL23</code>&#8216;</dt>
<dd> <p> see &#8216;<code>auto</code>&#8216;. </p>
 </dd>
<dt>&#8216;<code>SSL3</code>&#8216;</dt>
<dd> <p> Require SSLv3 exactly. SSLv3 is broken, not supported on all systems, avoid it if possible. This will make fetchmail negotiate SSLv3 only, and is the only way besides &#8216;<code>SSL3+</code>&#8216; to have fetchmail 6.4.0 or newer permit SSLv3. </p>
 </dd>
<dt>&#8216;<code>SSL3+</code>&#8216;</dt>
<dd> <p> same as &#8216;<code>auto</code>&#8216;, but permit SSLv3 as well. This is the only way besides &#8216;<code>SSL3</code>&#8216; to have fetchmail 6.4.0 or newer permit SSLv3. </p>
 </dd>
<dt>&#8216;<code>TLS1</code>&#8216;</dt>
<dd> <p> Require TLSv1. This does not negotiate TLSv1.1 or newer, and is discouraged. Replace by TLS1+ unless the latter chokes your server. </p>
 </dd>
<dt>&#8216;<code>TLS1+</code>&#8216;</dt>
<dd> <p> Since v6.4.0. See &#8216;<code>auto</code>&#8216;. </p>
 </dd>
<dt>&#8216;<code>TLS1.1</code>&#8216;</dt>
<dd> <p> Since v6.4.0. Require TLS v1.1 exactly. </p>
 </dd>
<dt>&#8216;<code>TLS1.1+</code>&#8216;</dt>
<dd> <p> Since v6.4.0. Require TLS. Auto-negotiate TLSv1.1 or newer. </p>
 </dd>
<dt>&#8216;<code>TLS1.2</code>&#8216;</dt>
<dd> <p> Since v6.4.0. Require TLS v1.2 exactly. </p>
 </dd>
<dt>&#8216;<code>TLS1.2+</code>&#8216;</dt>
<dd> <p> Since v6.4.0. Require TLS. Auto-negotiate TLSv1.2 or newer. </p>
 </dd>
<dt>Unrecognized parameters</dt>
<dd> <p> are treated the same as &#8216;<code>auto</code>&#8216;. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> NOTE: you should hardly ever need to use anything other than &#8216;&#8216; (to force an unencrypted connection) or &#8216;auto&#8217; (to enforce TLS). </p>
 </dd>
<dt><code>--sslcertck</code></dt>
<dd> <p> (Keyword: sslcertck, default enabled since v6.4.0) <br />
 <code>--sslcertck causes fetchmail to require that SSL/TLS be used and</code> disconnect if it can not successfully negotiate SSL or TLS, or if it cannot successfully verify and validate the certificate and follow it to a trust anchor (or trusted root certificate). The trust anchors are given as a set of local trusted certificates (see the <code>sslcertfile</code> and <code>sslcertpath</code> options). If the server certificate cannot be obtained or is not signed by one of the trusted ones (directly or indirectly), fetchmail will disconnect, regardless of the <code>sslfingerprint</code> option. </p>
 </dd>
<dd> <p> Note that CRL (certificate revocation lists) are only supported in OpenSSL 0.9.7 and newer! Your system clock should also be reasonably accurate when using this option. </p>
 </dd>
<dt><code>--nosslcertck</code></dt>
<dd> <p> (Keyword: no sslcertck, only in v6.4.X) <br />
 The opposite of --sslcertck, this is a disouraged option. It permits fetchmail to continue connecting even if the server certificate failed the verification checks. Should only be used together with --sslfingerprint. </p>
 </dd>
<dt><code>--sslcertfile &lt;file&gt;</code></dt>
<dd> <p> (Keyword: sslcertfile, since v6.3.17) <br />
 Sets the file fetchmail uses to look up local certificates. The default is empty. This can be given in addition to <code>--sslcertpath</code> below, and certificates specified in <code>--sslcertfile</code> will be processed before those in <code>--sslcertpath</code>. The option can be used in addition to <code>--sslcertpath</code>. </p>
 </dd>
<dd> <p> The file is a text file. It contains the concatenation of trusted CA certificates in PEM format. </p>
 </dd>
<dd> <p> Note that using this option will suppress loading the default SSL trusted CA certificates file unless you set the environment variable <code>FETCHMAIL_INCLUDE_DEFAULT_X509_CA_CERTS</code> to a non-empty value. </p>
 </dd>
<dt><code>--sslcertpath &lt;directory&gt;</code></dt>
<dd> <p> (Keyword: sslcertpath) <br />
 Sets the directory fetchmail uses to look up local certificates. The default is your OpenSSL default directory. The directory must be hashed the way OpenSSL expects it - every time you add or modify a certificate in the directory, you need to use the <code>c_rehash</code> tool (which comes with OpenSSL in the tools/ subdirectory). Also, after OpenSSL upgrades, you may need to run <code>c_rehash</code>; particularly when upgrading from 0.9.X to 1.0.0. </p>
 </dd>
<dd> <p> This can be given in addition to <code>--sslcertfile</code> above, which see for precedence rules. </p>
 </dd>
<dd> <p> Note that using this option will suppress adding the default SSL trusted CA certificates directory unless you set the environment variable <code>FETCHMAIL_INCLUDE_DEFAULT_X509_CA_CERTS</code> to a non-empty value. </p>
 </dd>
<dt><code>--sslcommonname &lt;common name&gt;</code></dt>
<dd> <p> (Keyword: sslcommonname; since v6.3.9) <br />
 Use of this option is discouraged. Before using it, contact the administrator of your upstream server and ask for a proper SSL certificate to be used. If that cannot be attained, this option can be used to specify the name (CommonName) that fetchmail expects on the server certificate. A correctly configured server will have this set to the hostname by which it is reached, and by default fetchmail will expect as much. Use this option when the CommonName is set to some other value, to avoid the &quot;Server CommonName mismatch&quot; warning, and only if the upstream server can&#8217;t be made to use proper certificates. </p>
 </dd>
<dt><code>--sslfingerprint &lt;fingerprint&gt;</code></dt>
<dd> <p> (Keyword: sslfingerprint) <br />
 Specify the fingerprint of the server key (an MD5 hash of the key) in hexadecimal notation with colons separating groups of two digits. The letter hex digits must be in upper case. This is the format that fetchmail uses to report the fingerprint when an SSL connection is established. When this is specified, fetchmail will compare the server key fingerprint with the given one, and the connection will fail if they do not match, regardless of the <code>sslcertck</code> setting. The connection will also fail if fetchmail cannot obtain an SSL certificate from the server. This can be used to prevent man-in-the-middle attacks, but the finger print from the server must be obtained or verified over a secure channel, and certainly not over the same Internet connection that fetchmail would use. </p>
 </dd>
<dd> <p> Using this option will prevent printing certificate verification errors as long as --nosslcertck is in effect. </p>
 </dd>
<dd> <p> To obtain the fingerprint of a certificate stored in the file cert.pem, try: </p>
<pre><code>        openssl x509 -in cert.pem -noout -md5 -fingerprint
</code></pre>
<p> For details, see <code>x509</code>(1ssl). </p>
 </dd></dl>
<h3>Delivery Control Options</h3>
<dl>
<dt><code>-S &lt;hosts&gt; | --smtphost &lt;hosts&gt;</code></dt>
<dd> <p> (Keyword: smtp[host]) <br />
 Specify a hunt list of hosts to forward mail to (one or more hostnames, comma-separated). Hosts are tried in list order; the first one that is up becomes the forwarding target for the current run. If this option is not specified, &#8216;localhost&#8217; is used as the default. Each hostname may have a port number following the host name. The port number is separated from the host name by a slash; the default port is &quot;smtp&quot;. If you specify an absolute path name (beginning with a /), it will be interpreted as the name of a UNIX socket accepting LMTP connections (such as is supported by the Cyrus IMAP daemon) Example: </p>
<pre><code>        --smtphost server1,server2/2525,server3,/var/imap/socket/lmtp
</code></pre>
<p> This option can be used with ODMR, and will make fetchmail a relay between the ODMR server and SMTP or LMTP receiver. </p>
 </dd>
<dd> <p> WARNING: if you use address numeric IP addresses here, be sure to use --smtpaddress or --smtpname (either of which see) with a valid SMTP address literal! </p>
 </dd>
<dt><code>--fetchdomains &lt;hosts&gt;</code></dt>
<dd> <p> (Keyword: fetchdomains) <br />
 In ETRN or ODMR mode, this option specifies the list of domains the server should ship mail for once the connection is turned around. The default is the FQDN of the machine running <code>fetchmail</code>. </p>
 </dd>
<dt><code>-D &lt;domain&gt; | --smtpaddress &lt;domain&gt;</code></dt>
<dd> <p> (Keyword: smtpaddress) <br />
 Specify the domain to be appended to addresses in RCPT TO lines shipped to SMTP. When this is not specified, the name of the SMTP server (as specified by --smtphost) is used for SMTP/LMTP and &#8216;localhost&#8217; is used for UNIX socket/BSMTP. </p>
 </dd>
<dd> <p> NOTE: if you intend to use numeric addresses, or so-called address literals per the SMTP standard, write them in proper SMTP syntax, for instance --smtpaddress &quot;[192.0.2.6]&quot; or --smtpaddress &quot;[IPv6:2001:DB8::6]&quot;. </p>
 </dd>
<dt><code>--smtpname &lt;user [at] domain&gt;</code></dt>
<dd> <p> (Keyword: smtpname) <br />
 Specify the domain and user to be put in RCPT TO lines shipped to SMTP. The default user is the current local user. Please also see the NOTE about --smtpaddress and address literals above. </p>
 </dd>
<dt><code>-Z &lt;nnn&gt; | --antispam &lt;nnn[, nnn]...&gt;</code></dt>
<dd> <p> (Keyword: antispam) <br />
 Specifies the list of numeric SMTP errors that are to be interpreted as a spam-block response from the listener. A value of -1 disables this option. For the command-line option, the list values should be comma-separated. Note that the antispam values only apply to &quot;MAIL FROM&quot; responses in the SMTP/LMTP dialogue, but several MTAs (Postfix in its default configuration, qmail) defer the anti-spam response code until after the RCPT TO. --antispam does not work in these circumstances. Also see --softbounce (default) and its inverse. </p>
 </dd>
<dt><code>-m &lt;command&gt; | --mda &lt;command&gt;</code></dt>
<dd> <p> (Keyword: mda) <br />
 This option lets <code>fetchmail</code> use a Message or Local Delivery Agent (MDA or LDA) directly, rather than forward via SMTP or LMTP. </p>
<p> To avoid losing mail, use this option only with MDAs like maildrop or MTAs like sendmail that exit with a nonzero status on disk-full and other delivery errors; the nonzero status tells fetchmail that delivery failed and prevents the message from being deleted on the server. </p>
<p> If <code>fetchmail</code> is running as root, it sets its user id while delivering mail through an MDA as follows: First, the FETCHMAILUSER, LOGNAME, and USER environment variables are checked in this order. The value of the first variable from his list that is defined (even if it is empty!) is looked up in the system user database. If none of the variables is defined, fetchmail will use the real user id it was started with. If one of the variables was defined, but the user stated there isn&#8217;t found, fetchmail continues running as root, without checking remaining variables on the list. Practically, this means that if you run fetchmail as root (not recommended), it is most useful to define the FETCHMAILUSER environment variable to set the user that the MDA should run as. Some MDAs (such as maildrop) are designed to be setuid root and setuid to the recipient&#8217;s user id, so you don&#8217;t lose functionality this way even when running fetchmail as unprivileged user. Check the MDA&#8217;s manual for details. </p>
<p> Some possible MDAs are &quot;/usr/sbin/sendmail -i -f %F -- %T&quot; (<code>Note:</code> some several older or vendor sendmail versions mistake -- for an address, rather than an indicator to mark the end of the option arguments), &quot;/usr/bin/deliver&quot; and &quot;/usr/bin/maildrop -d %T&quot;. Local delivery addresses will be inserted into the MDA command wherever you place a %T; the mail message&#8217;s From address will be inserted where you place an %F. </p>
<p> <code>Do NOT enclose the %F or %T string in single quotes!</code> For both %T and %F, fetchmail encloses the addresses in single quotes (&#8216;), after removing any single quotes they may contain, before the MDA command is passed to the shell. </p>
<p> <code>Do NOT use an MDA invocation that dispatches on the contents of To/Cc/Bcc,</code> like &quot;sendmail -i -t&quot; or &quot;qmail-inject&quot;, it will create mail loops and bring the just wrath of many postmasters down upon your head. This is one of the most frequent configuration errors! </p>
<p> Also, do <i>not</i> try to combine multidrop mode with an MDA such as maildrop that can only accept one address, unless your upstream stores one copy of the message per recipient and transports the envelope recipient in a header; you will lose mail. </p>
<p> The well-known <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1) package is very hard to configure properly, it has a very nasty &quot;fall through to the next rule&quot; behavior on delivery errors (even temporary ones, such as out of disk space if another user&#8217;s mail daemon copies the mailbox around to purge old messages), so your mail will end up in the wrong mailbox sooner or later. The proper procmail configuration is outside the scope of this document. Using <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1) is usually much easier, and many users find the filter syntax used by maildrop easier to understand. </p>
<p> Finally, we strongly advise that you do <code>not</code> use qmail-inject. The command line interface is non-standard without providing benefits for typical use, and fetchmail makes no attempts to accommodate qmail-inject&#8217;s deviations from the standard. Some of qmail-inject&#8217;s command-line and environment options are actually dangerous and can cause broken threads, non-detected duplicate messages and forwarding loops. </p>
 </dd>
<dt><code>--lmtp</code></dt>
<dd> <p> (Keyword: lmtp) <br />
 Cause delivery via LMTP (Local Mail Transfer Protocol). A service host and port <code>must</code> be explicitly specified on each host in the smtphost hunt list (see above) if this option is selected; the default port 25 will (in accordance with RFC 2033) not be accepted. </p>
 </dd>
<dt><code>--bsmtp &lt;filename&gt;</code></dt>
<dd> <p> (Keyword: bsmtp) <br />
 Append fetched mail to a BSMTP file. This simply contains the SMTP commands that would normally be generated by fetchmail when passing mail to an SMTP listener daemon. </p>
<p> An argument of &#8216;-&#8216; causes the SMTP batch to be written to standard output, which is of limited use: this only makes sense for debugging, because fetchmail&#8217;s regular output is interspersed on the same channel, so this isn&#8217;t suitable for mail delivery. This special mode may be removed in a later release. </p>
<p> Note that fetchmail&#8217;s reconstruction of MAIL FROM and RCPT TO lines is not guaranteed correct; the caveats discussed under THE USE AND ABUSE OF MULTIDROP MAILBOXES below apply. This mode has precedence before --mda and SMTP/LMTP. </p>
 </dd>
<dt><code>--bad-header {reject|accept}</code></dt>
<dd> <p> (Keyword: bad-header; since v6.3.15) <br />
 Specify how fetchmail is supposed to treat messages with bad headers, i. e. headers with bad syntax. Traditionally, fetchmail has rejected such messages, but some distributors modified fetchmail to accept them. You can now configure fetchmail&#8217;s behaviour per server. </p>
 </dd></dl>
<h3>Resource Limit Control Options</h3>
<dl>
<dt><code>-l &lt;maxbytes&gt; | --limit &lt;maxbytes&gt;</code></dt>
<dd> <p> (Keyword: limit) <br />
 Takes a maximum octet size argument, where 0 is the default and also the special value designating &quot;no limit&quot;. If nonzero, messages larger than this size will not be fetched and will be left on the server (in foreground sessions, the progress messages will note that they are &quot;oversized&quot;). If the fetch protocol permits (in particular, under IMAP or POP3 without the fetchall option) the message will not be marked seen. </p>
<p> An explicit --limit of 0 overrides any limits set in your run control file. This option is intended for those needing to strictly control fetch time due to expensive and variable phone rates. </p>
<p> Combined with --limitflush, it can be used to delete oversized messages waiting on a server. In daemon mode, oversize notifications are mailed to the calling user (see the --warnings option). This option does not work with ETRN or ODMR. </p>
 </dd>
<dt><code>-w &lt;interval&gt; | --warnings &lt;interval&gt;</code></dt>
<dd> <p> (Keyword: warnings) <br />
 Takes an interval in seconds. When you call <code>fetchmail</code> with a &#8216;limit&#8217; option in daemon mode, this controls the interval at which warnings about oversized messages are mailed to the calling user (or the user specified by the &#8216;postmaster&#8217; option). One such notification is always mailed at the end of the the first poll that the oversized message is detected. Thereafter, re-notification is suppressed until after the warning interval elapses (it will take place at the end of the first following poll). </p>
 </dd>
<dt><code>-b &lt;count&gt; | --batchlimit &lt;count&gt;</code></dt>
<dd> <p> (Keyword: batchlimit) <br />
 Specify the maximum number of messages that will be shipped to an SMTP listener before the connection is deliberately torn down and rebuilt (defaults to 0, meaning no limit). An explicit --batchlimit of 0 overrides any limits set in your run control file. While <code>sendmail</code>(8) normally initiates delivery of a message immediately after receiving the message terminator, some SMTP listeners are not so prompt. MTAs like <code>smail</code>(8) may wait till the delivery socket is shut down to deliver. This may produce annoying delays when <code>fetchmail</code> is processing very large batches. Setting the batch limit to some nonzero size will prevent these delays. This option does not work with ETRN or ODMR. </p>
 </dd>
<dt><code>-B &lt;number&gt; | --fetchlimit &lt;number&gt;</code></dt>
<dd> <p> (Keyword: fetchlimit) <br />
 Limit the number of messages accepted from a given server in a single poll. By default there is no limit. An explicit --fetchlimit of 0 overrides any limits set in your run control file. This option does not work with ETRN or ODMR. </p>
 </dd>
<dt><code>--fetchsizelimit &lt;number&gt;</code></dt>
<dd> <p> (Keyword: fetchsizelimit) <br />
 Limit the number of sizes of messages accepted from a given server in a single transaction. This option is useful in reducing the delay in downloading the first mail when there are too many mails in the mailbox. By default, the limit is 100. If set to 0, sizes of all messages are downloaded at the start. This option does not work with ETRN or ODMR. For POP3, the only valid non-zero value is 1. </p>
 </dd>
<dt><code>--fastuidl &lt;number&gt;</code></dt>
<dd> <p> (Keyword: fastuidl) <br />
 Do a binary instead of linear search for the first unseen UID. Binary search avoids downloading the UIDs of all mails. This saves time (especially in daemon mode) where downloading the same set of UIDs in each poll is a waste of bandwidth. The number &#8216;n&#8217; indicates how rarely a linear search should be done. In daemon mode, linear search is used once followed by binary searches in &#8216;n-1&#8217; polls if &#8216;n&#8217; is greater than 1; binary search is always used if &#8216;n&#8217; is 1; linear search is always used if &#8216;n&#8217; is 0. In non-daemon mode, binary search is used if &#8216;n&#8217; is 1; otherwise linear search is used. The default value of &#8216;n&#8217; is 4. This option works with POP3 only. </p>
 </dd>
<dt><code>-e &lt;count&gt; | --expunge &lt;count&gt;</code></dt>
<dd> <p> (Keyword: expunge) <br />
 Arrange for deletions to be made final after a given number of messages. Under POP2 or POP3, fetchmail cannot make deletions final without sending QUIT and ending the session -- with this option on, fetchmail will break a long mail retrieval session into multiple sub-sessions, sending QUIT after each sub-session. This is a good defense against line drops on POP3 servers. Under IMAP, <code>fetchmail</code> normally issues an EXPUNGE command after each deletion in order to force the deletion to be done immediately. This is safest when your connection to the server is flaky and expensive, as it avoids resending duplicate mail after a line hit. However, on large mailboxes the overhead of re-indexing after every message can slam the server pretty hard, so if your connection is reliable it is good to do expunges less frequently. Also note that some servers enforce a delay of a few seconds after each quit, so fetchmail may not be able to get back in immediately after an expunge -- you may see &quot;lock busy&quot; errors if this happens. If you specify this option to an integer N, it tells <code>fetchmail</code> to only issue expunges on every Nth delete. An argument of zero suppresses expunges entirely (so no expunges at all will be done until the end of run). This option does not work with ETRN or ODMR. </p>
 </dd></dl>
<h3>Authentication Options</h3>
<dl>
<dt><code>-u &lt;name&gt; | --user &lt;name&gt; | --username &lt;name&gt;</code></dt>
<dd> <p> (Keyword: user[name]) <br />
 Specifies the user identification to be used when logging in to the mailserver. The appropriate user identification is both server and user-dependent. The default is your login name on the client machine that is running <code>fetchmail</code>. See USER AUTHENTICATION below for a complete description. </p>
 </dd>
<dt><code>-I &lt;specification&gt; | --interface &lt;specification&gt;</code></dt>
<dd> <p> (Keyword: interface) <br />
 Require that a specific interface device be up and have a specific local or remote IPv4 (IPv6 is not supported by this option yet) address (or range) before polling. Frequently <code>fetchmail</code> is used over a transient point-to-point TCP/IP link established directly to a mailserver via SLIP or PPP. That is a relatively secure channel. But when other TCP/IP routes to the mailserver exist (e.g. when the link is connected to an alternate ISP), your username and password may be vulnerable to snooping (especially when daemon mode automatically polls for mail, shipping a clear password over the net at predictable intervals). The --interface option may be used to prevent this. When the specified link is not up or is not connected to a matching IP address, polling will be skipped. The format is: </p>
<pre><code>        interface/iii.iii.iii.iii[/mmm.mmm.mmm.mmm]
</code></pre>
<p> The field before the first slash is the interface name (i.e. sl0, ppp0 etc.). The field before the second slash is the acceptable IP address. The field after the second slash is a mask which specifies a range of IP addresses to accept. If no mask is present 255.255.255.255 is assumed (i.e. an exact match). This option is currently only supported under Linux and FreeBSD. Please see the <code>monitor</code> section for below for FreeBSD specific information. </p>
<p> Note that this option may be removed from a future fetchmail version. </p>
 </dd>
<dt><code>-M &lt;interface&gt; | --monitor &lt;interface&gt;</code></dt>
<dd> <p> (Keyword: monitor) <br />
 Daemon mode can cause transient links which are automatically taken down after a period of inactivity (e.g. PPP links) to remain up indefinitely. This option identifies a system TCP/IP interface to be monitored for activity. After each poll interval, if the link is up but no other activity has occurred on the link, then the poll will be skipped. However, when fetchmail is woken up by a signal, the monitor check is skipped and the poll goes through unconditionally. This option is currently only supported under Linux and FreeBSD. For the <code>monitor</code> and <code>interface</code> options to work for non root users under FreeBSD, the fetchmail binary must be installed SGID kmem. This would be a security hole, but fetchmail runs with the effective GID set to that of the kmem group <i>only</i> when interface data is being collected. </p>
<p> Note that this option may be removed from a future fetchmail version. </p>
 </dd>
<dt><code>--auth &lt;type&gt;</code></dt>
<dd> <p> (Keyword: auth[enticate]) <br />
 This option permits you to specify an authentication type (see USER AUTHENTICATION below for details). The possible values are <code>any</code>, <code>password</code>, <code>kerberos_v5</code>, <code>kerberos</code> (or, for excruciating exactness, <code>kerberos_v4</code>), <code>gssapi</code>, <code>cram-md5</code>, <code>otp</code>, <code>ntlm</code>, <code>msn</code> (only for POP3), <code>external</code> (only IMAP) and <code>ssh</code>. When <code>any</code> (the default) is specified, fetchmail tries first methods that don&#8217;t require a password (EXTERNAL, GSSAPI, KERBEROS IV, KERBEROS 5); then it looks for methods that mask your password (CRAM-MD5, NTLM, X-OTP - note that MSN is only supported for POP3, but not autoprobed); and only if the server doesn&#8217;t support any of those will it ship your password en clair. Other values may be used to force various authentication methods (<code>ssh</code> suppresses authentication and is thus useful for IMAP PREAUTH). (<code>external</code> suppresses authentication and is thus useful for IMAP EXTERNAL). Any value other than <code>password</code>, <code>cram-md5</code>, <code>ntlm</code>, <code>msn</code> or <code>otp</code> suppresses fetchmail&#8217;s normal inquiry for a password. Specify <code>ssh</code> when you are using an end-to-end secure connection such as an ssh tunnel; specify <code>external</code> when you use TLS with client authentication and specify <code>gssapi</code> or <code>kerberos_v4</code> if you are using a protocol variant that employs GSSAPI or K4. Choosing KPOP protocol automatically selects Kerberos authentication. This option does not work with ETRN. GSSAPI service names are in line with RFC-2743 and IANA registrations, see </p>
 </dd></dl>
<h3>Miscellaneous Options</h3>
<dl>
<dt><code>-f &lt;pathname&gt; | --fetchmailrc &lt;pathname&gt;</code></dt>
<dd> <p> Specify a non-default name for the <i>~/.fetchmailrc</i> run control file. The pathname argument must be either &quot;-&quot; (a single dash, meaning to read the configuration from standard input) or a filename. Unless the --version option is also on, a named file argument must have permissions no more open than 0700 (u=rwx,g=,o=) or else be /dev/null. </p>
 </dd>
<dt><code>-i &lt;pathname&gt; | --idfile &lt;pathname&gt;</code></dt>
<dd> <p> (Keyword: idfile) <br />
 Specify an alternate name for the .fetchids file used to save message UIDs. NOTE: since fetchmail 6.3.0, write access to the directory containing the idfile is required, as fetchmail writes a temporary file and renames it into the place of the real idfile only if the temporary file has been written successfully. This avoids the truncation of idfiles when running out of disk space. </p>
 </dd>
<dt><code>--pidfile &lt;pathname&gt;</code></dt>
<dd> <p> (Keyword: pidfile; since fetchmail v6.3.4) <br />
 Override the default location of the PID file. Default: see &quot;ENVIRONMENT&quot; below. </p>
 </dd>
<dt><code>-n | --norewrite</code></dt>
<dd> <p> (Keyword: no rewrite) <br />
 Normally, <code>fetchmail</code> edits RFC-822 address headers (To, From, Cc, Bcc, and Reply-To) in fetched mail so that any mail IDs local to the server are expanded to full addresses (@ and the mailserver hostname are appended). This enables replies on the client to get addressed correctly (otherwise your mailer might think they should be addressed to local users on the client machine!). This option disables the rewrite. (This option is provided to pacify people who are paranoid about having an MTA edit mail headers and want to know they can prevent it, but it is generally not a good idea to actually turn off rewrite.) When using ETRN or ODMR, the rewrite option is ineffective. </p>
 </dd>
<dt><code>-E &lt;line&gt; | --envelope &lt;line&gt;</code></dt>
<dd> <p> (Keyword: envelope; Multidrop only) <br />
 In the configuration file, an enhanced syntax is used: <br />
 <code>envelope [&lt;count&gt;] &lt;line&gt;</code> </p>
<p> This option changes the header <code>fetchmail</code> assumes will carry a copy of the mail&#8217;s envelope address. Normally this is &#8216;X-Envelope-To&#8217;. Other typically found headers to carry envelope information are &#8216;X-Original-To&#8217; and &#8216;Delivered-To&#8217;. Now, since these headers are not standardized, practice varies. See the discussion of multidrop address handling below. As a special case, &#8216;envelope &quot;Received&quot;&#8216; enables parsing of sendmail-style Received lines. This is the default, but discouraged because it is not fully reliable. </p>
<p> Note that fetchmail expects the Received-line to be in a specific format: It must contain &quot;by <i>host</i> for <i>address</i>&quot;, where <i>host</i> must match one of the mailserver names that fetchmail recognizes for the account in question. </p>
<p> The optional count argument (only available in the configuration file) determines how many header lines of this kind are skipped. A count of 1 means: skip the first, take the second. A count of 2 means: skip the first and second, take the third, and so on. </p>
 </dd>
<dt><code>-Q &lt;prefix&gt; | --qvirtual &lt;prefix&gt;</code></dt>
<dd> <p> (Keyword: qvirtual; Multidrop only) <br />
 The string prefix assigned to this option will be removed from the user name found in the header specified with the <i>envelope</i> option (<i>before</i> doing multidrop name mapping or localdomain checking, if either is applicable). This option is useful if you are using <code>fetchmail</code> to collect the mail for an entire domain and your ISP (or your mail redirection provider) is using qmail. One of the basic features of qmail is the <i>Delivered-To:</i> message header. Whenever qmail delivers a message to a local mailbox it puts the username and hostname of the envelope recipient on this line. The major reason for this is to prevent mail loops. To set up qmail to batch mail for a disconnected site the ISP-mailhost will have normally put that site in its &#8216;Virtualhosts&#8217; control file so it will add a prefix to all mail addresses for this site. This results in mail sent to &#8216;username [at] userhost.userdom.dom.com&#8217; having a <i>Delivered-To:</i> line of the form: </p>
 </dd>
<dd> <p> Delivered-To: mbox-userstr-username [at] userhost.example.com </p>
 </dd>
<dd> <p> The ISP can make the &#8216;mbox-userstr-&#8216; prefix anything they choose but a string matching the user host name is likely. By using the option &#8216;envelope Delivered-To:&#8216; you can make fetchmail reliably identify the original envelope recipient, but you have to strip the &#8216;mbox-userstr-&#8216; prefix to deliver to the correct user. This is what this option is for. </p>
 </dd>
<dt><code>--configdump</code></dt>
<dd> <p> Parse the <i>~/.fetchmailrc</i> file, interpret any command-line options specified, and dump a configuration report to standard output. The configuration report is a data structure assignment in the language Python. This option is meant to be used with an interactive <i>~/.fetchmailrc</i> editor like <code>fetchmailconf</code>, written in Python. </p>
 </dd>
<dt><code>-y | --yydebug</code></dt>
<dd> <p> Enables parser debugging, this option is meant to be used by developers only. </p>
 </dd></dl>
<h3>Removed Options</h3>
<dl>
<dt><code>-T | --netsec</code></dt>
<dd> <p> Removed before version 6.3.0, the required underlying inet6_apps library had been discontinued and is no longer available. </p>
 </dd></dl>
<h2>USER AUTHENTICATION AND ENCRYPTION</h2>
<p> All modes except ETRN require authentication of the client to the server. Normal user authentication in <code>fetchmail</code> is very much like the authentication mechanism of <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1). The correct user-id and password depend upon the underlying security system at the mailserver. </p>
<p> If the mailserver is a Unix machine on which you have an ordinary user account, your regular login name and password are used with <code>fetchmail</code>. If you use the same login name on both the server and the client machines, you needn&#8217;t worry about specifying a user-id with the <code>-u</code> option -- the default behavior is to use your login name on the client machine as the user-id on the server machine. If you use a different login name on the server machine, specify that login name with the <code>-u</code> option. e.g. if your login name is &#8216;jsmith&#8217; on a machine named &#8216;mailgrunt&#8217;, you would start <code>fetchmail</code> as follows: </p>
<dl>
<dd> <p> fetchmail -u jsmith mailgrunt </p>
 </dd></dl>
<p> The default behavior of <code>fetchmail</code> is to prompt you for your mailserver password before the connection is established. This is the safest way to use <code>fetchmail</code> and ensures that your password will not be compromised. You may also specify your password in your <i>~/.fetchmailrc</i> file. This is convenient when using <code>fetchmail</code> in daemon mode or with scripts. </p>
<h3>Using netrc files</h3>
<p> If you do not specify a password, and <code>fetchmail</code> cannot extract one from your <i>~/.fetchmailrc</i> file, it will look for a <i>~/.netrc</i> file in your home directory before requesting one interactively; if an entry matching the mailserver is found in that file, the password will be used. Fetchmail first looks for a match on poll name; if it finds none, it checks for a match on via name. See the <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) man page for details of the syntax of the <i>~/.netrc</i> file. To show a practical example, a .netrc might look like this: </p>
<dl>
<dd> <pre><code>machine hermes.example.org
login joe
password topsecret
</code></pre>
 </dd></dl>
<p> You can repeat this block with different user information if you need to provide more than one password. </p>
<p> This feature may allow you to avoid duplicating password information in more than one file. </p>
<p> On mailservers that do not provide ordinary user accounts, your user-id and password are usually assigned by the server administrator when you apply for a mailbox on the server. Contact your server administrator if you don&#8217;t know the correct user-id and password for your mailbox account.  </p>
<h2>POP3 VARIANTS</h2>
<p> Early versions of POP3 (RFC1081, RFC1225) supported a crude form of independent authentication using the <i>.rhosts</i> file on the mailserver side. Under this RPOP variant, a fixed per-user ID equivalent to a password was sent in clear over a link to a reserved port, with the command RPOP rather than PASS to alert the server that it should do special checking. RPOP is supported by <code>fetchmail</code> (you can specify &#8216;protocol RPOP&#8217; to have the program send &#8216;RPOP&#8217; rather than &#8216;PASS&#8217;) but its use is strongly discouraged, and support will be removed from a future fetchmail version. This facility was vulnerable to spoofing and was withdrawn in RFC1460. </p>
<p> RFC1460 introduced APOP authentication. In this variant of POP3, you register an APOP password on your server host (on some servers, the program to do this is called <code>popauth</code>(8)). You put the same password in your <i>~/.fetchmailrc</i> file. Each time <code>fetchmail</code> logs in, it sends an MD5 hash of your password and the server greeting time to the server, which can verify it by checking its authorization database. </p>
<p> <code>Note that APOP is no longer considered resistant against man-in-the-middle attacks.</code>  </p>
<h3>RETR or TOP</h3>
<p> <code>fetchmail</code> makes some efforts to make the server believe messages had not been retrieved, by using the TOP command with a large number of lines when possible. TOP is a command that retrieves the full header and a <code>fetchmail</code>-specified amount of body lines. It is optional and therefore not implemented by all servers, and some are known to implement it improperly. On many servers however, the RETR command which retrieves the full message with header and body, sets the &quot;seen&quot; flag (for instance, in a web interface), whereas the TOP command does not do that. </p>
<p> <code>fetchmail</code> will always use the RETR command if &quot;fetchall&quot; is set. <code>fetchmail</code> will also use the RETR command if &quot;keep&quot; is set and &quot;uidl&quot; is unset. Finally, <code>fetchmail</code> will use the RETR command on Maillennium POP3/PROXY servers (used by Comcast) to avoid a deliberate TOP misinterpretation in this server that causes message corruption. </p>
<p> In all other cases, <code>fetchmail</code> will use the TOP command. This implies that in &quot;keep&quot; setups, &quot;uidl&quot; must be set if &quot;TOP&quot; is desired. </p>
<p> <code>Note</code> that this description is true for the current version of fetchmail, but the behavior may change in future versions. In particular, fetchmail may prefer the RETR command because the TOP command causes much grief on some servers and is only optional.  </p>
<h2>ALTERNATE AUTHENTICATION FORMS</h2>
<p> If your <code>fetchmail</code> was built with Kerberos support and you specify Kerberos authentication (either with --auth or the <i>.fetchmailrc</i> option <code>authenticate kerberos_v4</code>) it will try to get a Kerberos ticket from the mailserver at the start of each query. Note: if either the pollname or via name is &#8216;hesiod&#8217;, fetchmail will try to use Hesiod to look up the mailserver. </p>
<p> If you use POP3 or IMAP with GSSAPI authentication, <code>fetchmail</code> will expect the server to have RFC1731- or RFC1734-conforming GSSAPI capability, and will use it. Currently this has only been tested over Kerberos V, so you&#8217;re expected to already have a ticket-granting ticket. You may pass a username different from your principal name using the standard <code>--user</code> command or by the <i>.fetchmailrc</i> option <code>user</code>. </p>
<p> If your IMAP daemon returns the PREAUTH response in its greeting line, fetchmail will notice this and skip the normal authentication step. This can be useful, e.g. if you start imapd explicitly using ssh. In this case you can declare the authentication value &#8216;ssh&#8217; on that site entry to stop <i>.fetchmail</i> from asking you for a password when it starts up. </p>
<p> If you use client authentication with <i>TLS1</i> and your IMAP daemon returns the <i>AUTH=EXTERNAL</i> response, fetchmail will notice this and will use the authentication shortcut and will not send the passphrase. In this case you can declare the authentication value &#8216;external&#8217; <br />
&nbsp;on that site to stop&nbsp;<code>fetchmail</code>&nbsp;from asking you for a password when it starts up. </p>
<p> If you are using POP3, and the server issues a one-time-password challenge conforming to RFC1938, <code>fetchmail</code> will use your password as a pass phrase to generate the required response. This avoids sending secrets over the net unencrypted. </p>
<p> Compuserve&#8217;s RPA authentication is supported. If you compile in the support, <code>fetchmail</code> will try to perform an RPA pass-phrase authentication instead of sending over the password en clair if it detects &quot;@compuserve.com&quot; in the hostname. </p>
<p> If you are using IMAP, Microsoft&#8217;s NTLM authentication (used by Microsoft Exchange) is supported. If you compile in the support, <code>fetchmail</code> will try to perform an NTLM authentication (instead of sending over the password en clair) whenever the server returns AUTH=NTLM in its capability response. Specify a user option value that looks like &#8216;user [at] domain&#8217;: the part to the left of the @ will be passed as the username and the part to the right as the NTLM domain. </p>
<h3>Secure Socket Layers (SSL) and Transport Layer Security (TLS)</h3>
<p> All retrieval protocols can use SSL or TLS wrapping for the transport. Additionally, POP3 and IMAP retrival can also negotiate SSL/TLS by means of STARTTLS (or STLS). </p>
<p> Note that fetchmail currently uses the OpenSSL library, which is severely underdocumented, so failures may occur just because the programmers are not aware of OpenSSL&#8217;s requirement of the day. For instance, since v6.3.16, fetchmail calls OpenSSL_add_all_algorithms(), which is necessary to support certificates using SHA256 on OpenSSL 0.9.8 -- this information is deeply hidden in the documentation and not at all obvious. Please do not hesitate to report subtle SSL failures. </p>
<p> You can access SSL encrypted services by specifying the options starting with --ssl, such as --ssl, --sslproto, --sslcertck, and others. You can also do this using the corresponding user options in the .fetchmailrc file. Some services, such as POP3 and IMAP, have different well known ports defined for the SSL encrypted services. The encrypted ports will be selected automatically when SSL is enabled and no explicit port is specified. Also, the --sslcertck command line or sslcertck run control file option should be used to force strict certificate checking with older fetchmail versions - see below. </p>
<p> If SSL is not configured, fetchmail will usually opportunistically try to use STARTTLS. STARTTLS can be enforced by using --sslproto~auto and defeated by using --sslproto~&#8216;&#8216;. TLS connections use the same port as the unencrypted version of the protocol and negotiate TLS via special command. The --sslcertck command line or sslcertck run control file option should be used to force strict certificate checking - see below. </p>
<p> <code>--sslcertck is recommended:</code> When connecting to an SSL or TLS encrypted server, the server presents a certificate to the client for validation. The certificate is checked to verify that the common name in the certificate matches the name of the server being contacted and that the effective and expiration dates in the certificate indicate that it is currently valid. If any of these checks fail, a warning message is printed, but the connection continues. The server certificate does not need to be signed by any specific Certifying Authority and may be a &quot;self-signed&quot; certificate. If the --sslcertck command line option or sslcertck run control file option is used, fetchmail will instead abort if any of these checks fail, because it must assume that there is a man-in-the-middle attack in this scenario, hence fetchmail must not expose cleartext passwords. Use of the sslcertck or --sslcertck option is therefore advised; it has become the default in fetchmail 6.4.0. </p>
<p> Some SSL encrypted servers may request a client side certificate. A client side public SSL certificate and private SSL key may be specified. If requested by the server, the client certificate is sent to the server for validation. Some servers may require a valid client certificate and may refuse connections if a certificate is not provided or if the certificate is not valid. Some servers may require client side certificates be signed by a recognized Certifying Authority. The format for the key files and the certificate files is that required by the underlying SSL libraries (OpenSSL in the general case). </p>
<p> A word of care about the use of SSL: While above mentioned setup with self-signed server certificates retrieved over the wires can protect you from a passive eavesdropper, it doesn&#8217;t help against an active attacker. It&#8217;s clearly an improvement over sending the passwords in clear, but you should be aware that a man-in-the-middle attack is trivially possible (in particular with tools such as ). Use of strict certificate checking with a certification authority recognized by server and client, or perhaps of an SSH tunnel (see below for some examples) is preferable if you care seriously about the security of your mailbox and passwords. </p>
<h3>ESMTP AUTH</h3>
<p> <code>fetchmail</code> also supports authentication to the ESMTP server on the client side according to RFC 2554. You can specify a name/password pair to be used with the keywords &#8216;esmtpname&#8217; and &#8216;esmtppassword&#8217;; the former defaults to the username of the calling user. </p>
<h2>DAEMON MODE</h2>
<h3>Introducing the daemon mode</h3>
<p> In daemon mode, <code>fetchmail</code> puts itself into the background and runs forever, querying each specified host and then sleeping for a given polling interval.  </p>
<h3>Starting the daemon mode</h3>
<p> There are several ways to make fetchmail work in daemon mode. On the command line, <code>--daemon&nbsp;&lt;interval&gt;</code> or <code>-d&nbsp;&lt;interval&gt;</code> option runs <code>fetchmail</code> in daemon mode. You must specify a numeric argument which is a polling interval (time to wait after completing a whole poll cycle with the last server and before starting the next poll cycle with the first server) in seconds. </p>
<p> Example: simply invoking </p>
<dl>
<dd> <p> fetchmail -d 900 </p>
 </dd></dl>
<p> will, therefore, poll all the hosts described in your <i>~/.fetchmailrc</i> file (except those explicitly excluded with the &#8216;skip&#8217; verb) a bit less often than once every 15 minutes (exactly: 15 minutes + time that the poll takes). </p>
<p> It is also possible to set a polling interval in your <i>~/.fetchmailrc</i> file by saying &#8216;set daemon&nbsp;&lt;interval&gt;&#8216;, where &lt;interval&gt; is an integer number of seconds. If you do this, fetchmail will always start in daemon mode unless you override it with the command-line option --daemon 0 or -d0. </p>
<p> Only one daemon process is permitted per user; in daemon mode, <code>fetchmail</code> sets up a per-user lockfile to guarantee this. (You can however cheat and set the FETCHMAILHOME environment variable to overcome this setting, but in that case, it is your responsibility to make sure you aren&#8217;t polling the same server with two processes at the same time.)  </p>
<h3>Awakening the background daemon</h3>
<p> Normally, calling fetchmail with a daemon in the background sends a wake-up signal to the daemon and quits without output. The background daemon then starts its next poll cycle immediately. The wake-up signal, SIGUSR1, can also be sent manually. The wake-up action also clears any &#8216;wedged&#8217; flags indicating that connections have wedged due to failed authentication or multiple timeouts.  </p>
<h3>Terminating the background daemon</h3>
<p> The option <code>-q</code> or <code>--quit</code> will kill a running daemon process instead of waking it up (if there is no such process, <code>fetchmail</code> will notify you). If the --quit option appears last on the command line, <code>fetchmail</code> will kill the running daemon process and then quit. Otherwise, <code>fetchmail</code> will first kill a running daemon process and then continue running with the other options.  </p>
<h3>Useful options for daemon mode</h3>
<p> The <code>-L &lt;filename&gt;</code> or <code>--logfile &lt;filename&gt;</code> option (keyword: set logfile) is only effective when fetchmail is detached and in daemon mode. Note that <code>the logfile must exist before</code> fetchmail is run, you can use the <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command with the filename as its sole argument to create it. <br />
 This option allows you to redirect status messages into a specified logfile (follow the option with the logfile name). The logfile is opened for append, so previous messages aren&#8217;t deleted. This is primarily useful for debugging configurations. Note that fetchmail does not detect if the logfile is rotated, the logfile is only opened once when fetchmail starts. You need to restart fetchmail after rotating the logfile and before compressing it (if applicable). </p>
<p> The <code>--syslog</code> option (keyword: set syslog) allows you to redirect status and error messages emitted to the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) system daemon if available. Messages are logged with an id of <code>fetchmail</code>, the facility <code>LOG_MAIL</code>, and priorities <code>LOG_ERR</code>, <code>LOG_ALERT</code> or <code>LOG_INFO</code>. This option is intended for logging status and error messages which indicate the status of the daemon and the results while fetching mail from the server(s). Error messages for command line options and parsing the <i>.fetchmailrc</i> file are still written to stderr, or to the specified log file. The <code>--nosyslog</code> option turns off use of <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), assuming it&#8217;s turned on in the <i>~/.fetchmailrc</i> file. This option is overridden, in certain situations, by <code>--logfile</code> (which see). </p>
<p> The <code>-N</code> or <code>--nodetach</code> option suppresses backgrounding and detachment of the daemon process from its control terminal. This is useful for debugging or when fetchmail runs as the child of a supervisor process such as <code><a href="/docs/linux/man/8-init/">init</a></code>(8) or Gerrit Pape&#8217;s <code>runit</code>(8). Note that this also causes the logfile option to be ignored. </p>
<p> Note that while running in daemon mode polling a POP2 or IMAP2bis server, transient errors (such as DNS failures or sendmail delivery refusals) may force the fetchall option on for the duration of the next polling cycle. This is a robustness feature. It means that if a message is fetched (and thus marked seen by the mailserver) but not delivered locally due to some transient error, it will be re-fetched during the next poll cycle. (The IMAP logic doesn&#8217;t delete messages until they&#8217;re delivered, so this problem does not arise.) </p>
<p> If you touch or change the <i>~/.fetchmailrc</i> file while fetchmail is running in daemon mode, this will be detected at the beginning of the next poll cycle. When a changed <i>~/.fetchmailrc</i> is detected, fetchmail rereads it and restarts from scratch (using exec(2); no state information is retained in the new instance). Note that if fetchmail needs to query for passwords, of that if you break the <i>~/.fetchmailrc</i> file&#8217;s syntax, the new instance will softly and silently vanish away on startup. </p>
<h2>ADMINISTRATIVE OPTIONS</h2>
<p> The <code>--postmaster &lt;name&gt;</code> option (keyword: set postmaster) specifies the last-resort username to which multidrop mail is to be forwarded if no matching local recipient can be found. It is also used as destination of undeliverable mail if the &#8216;bouncemail&#8217; global option is off and additionally for spam-blocked mail if the &#8216;bouncemail&#8217; global option is off and the &#8216;spambounce&#8217; global option is on. This option defaults to the user who invoked <code>fetchmail</code>. If the invoking user is root, then the default of this option is the user &#8216;postmaster&#8217;. Setting postmaster to the empty string causes such mail as described above to be discarded - this however is usually a bad idea. See also the description of the &#8216;FETCHMAILUSER&#8217; environment variable in the ENVIRONMENT section below. </p>
<p> The <code>--nobounce</code> behaves like the &quot;set no bouncemail&quot; global option, which see. </p>
<p> The <code>--invisible</code> option (keyword: set invisible) tries to make fetchmail invisible. Normally, fetchmail behaves like any other MTA would -- it generates a Received header into each message describing its place in the chain of transmission, and tells the MTA it forwards to that the mail came from the machine fetchmail itself is running on. If the invisible option is on, the Received header is suppressed and fetchmail tries to spoof the MTA it forwards to into thinking it came directly from the mailserver host. </p>
<p> The <code>--showdots</code> option (keyword: set showdots) forces fetchmail to show progress dots even if the output goes to a file or fetchmail is not in verbose mode. Fetchmail shows the dots by default when run in --verbose mode <i>and</i> output goes to console. This option is ignored in --silent mode. </p>
<p> By specifying the <code>--tracepolls</code> option, you can ask fetchmail to add information to the Received header on the form &quot;polling {label} account {user}&quot;, where {label} is the account label (from the specified rcfile, normally ~/.fetchmailrc) and {user} is the username which is used to log on to the mail server. This header can be used to make filtering email where no useful header information is available and you want mail from different accounts sorted into different mailboxes (this could, for example, occur if you have an account on the same server running a mailing list, and are subscribed to the list using that account). The default is not adding any such header. In <i>.fetchmailrc</i>, this is called &#8216;tracepolls&#8217;. </p>
<h2>RETRIEVAL FAILURE MODES</h2>
<p> The protocols <code>fetchmail</code> uses to talk to mailservers are next to bulletproof. In normal operation forwarding to port 25, no message is ever deleted (or even marked for deletion) on the host until the SMTP listener on the client side has acknowledged to <code>fetchmail</code> that the message has been either accepted for delivery or rejected due to a spam block. </p>
<p> When forwarding to an MDA, however, there is more possibility of error. Some MDAs are &#8216;safe&#8217; and reliably return a nonzero status on any delivery error, even one due to temporary resource limits. The <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1) program is like this; so are most programs designed as mail transport agents, such as <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), including the sendmail wrapper of Postfix and <code>exim</code>(1). These programs give back a reliable positive acknowledgement and can be used with the mda option with no risk of mail loss. Unsafe MDAs, though, may return 0 even on delivery failure. If this happens, you will lose mail. </p>
<p> The normal mode of <code>fetchmail</code> is to try to download only &#8216;new&#8217; messages, leaving untouched (and undeleted) messages you have already read directly on the server (or fetched with a previous <i>fetchmail --keep</i>). But you may find that messages you&#8217;ve already read on the server are being fetched (and deleted) even when you don&#8217;t specify --all. There are several reasons this can happen. </p>
<p> One could be that you&#8217;re using POP2. The POP2 protocol includes no representation of &#8216;new&#8217; or &#8216;old&#8217; state in messages, so <code>fetchmail</code> must treat all messages as new all the time. But POP2 is obsolete, so this is unlikely. </p>
<p> A potential POP3 problem might be servers that insert messages in the middle of mailboxes (some VMS implementations of mail are rumored to do this). The <code>fetchmail</code> code assumes that new messages are appended to the end of the mailbox; when this is not true it may treat some old messages as new and vice versa. Using UIDL whilst setting fastuidl 0 might fix this, otherwise, consider switching to IMAP. </p>
<p> Yet another POP3 problem is that if they can&#8217;t make tempfiles in the user&#8217;s home directory, some POP3 servers will hand back an undocumented response that causes fetchmail to spuriously report &quot;No mail&quot;. </p>
<p> The IMAP code uses the presence or absence of the server flag \Seen to decide whether or not a message is new. This isn&#8217;t the right thing to do, fetchmail should check the UIDVALIDITY and use UID, but it doesn&#8217;t do that yet. Under Unix, it counts on your IMAP server to notice the BSD-style Status flags set by mail user agents and set the \Seen flag from them when appropriate. All Unix IMAP servers we know of do this, though it&#8217;s not specified by the IMAP RFCs. If you ever trip over a server that doesn&#8217;t, the symptom will be that messages you have already read on your host will look new to the server. In this (unlikely) case, only messages you fetched with <i>fetchmail --keep</i> will be both undeleted and marked old. </p>
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
<p> Besides the spam-blocking described above, fetchmail takes special actions --- that may be modified by the --softbounce option --- on the following SMTP/ESMTP error response codes </p>
<dl>
<dt>452 (insufficient system storage)</dt>
<dd> <p> Leave the message in the server mailbox for later retrieval. </p>
 </dd>
<dt>552 (message exceeds fixed maximum message size)</dt>
<dd> <p> Delete the message from the server. Send bounce-mail to the originator. </p>
 </dd>
<dt>553 (invalid sending domain)</dt>
<dd> <p> Delete the message from the server. Don&#8217;t even try to send bounce-mail to the originator. </p>
 </dd></dl>
<p> Other errors greater or equal to 500 trigger bounce mail back to the originator, unless suppressed by --softbounce. See also BUGS. </p>
<h2>THE RUN CONTROL FILE</h2>
<p> The preferred way to set up fetchmail is to write a <i>.fetchmailrc</i> file in your home directory (you may do this directly, with a text editor, or indirectly via <code>fetchmailconf</code>). When there is a conflict between the command-line arguments and the arguments in this file, the command-line arguments take precedence. </p>
<p> To protect the security of your passwords, your <i>~/.fetchmailrc</i> may not normally have more than 0700 (u=rwx,g=,o=) permissions; <code>fetchmail</code> will complain and exit otherwise (this check is suppressed when --version is on). </p>
<p> You may read the <i>.fetchmailrc</i> file as a list of commands to be executed when <code>fetchmail</code> is called with no arguments.  </p>
<h3>Run Control Syntax</h3>
<p> Comments begin with a &#8216;#&#8216; and extend through the end of the line. Otherwise the file consists of a series of server entries or global option statements in a free-format, token-oriented syntax. </p>
<p> There are four kinds of tokens: grammar keywords, numbers (i.e. decimal digit sequences), unquoted strings, and quoted strings. A quoted string is bounded by double quotes and may contain whitespace (and quoted digits are treated as a string). Note that quoted strings will also contain line feed characters if they run across two or more lines, unless you use a backslash to join lines (see below). An unquoted string is any whitespace-delimited token that is neither numeric, string quoted nor contains the special characters &#8216;,&#8216;, &#8216;;&#8216;, &#8216;:&#8216;, or &#8216;=&#8216;. </p>
<p> Any amount of whitespace separates tokens in server entries, but is otherwise ignored. You may use backslash escape sequences (\n for LF, \t for HT, \b for BS, \r for CR, \<i>nnn</i> for decimal (where nnn cannot start with a 0), \0 <i>ooo</i> for octal, and \x <i>hh</i> for hex) to embed non-printable characters or string delimiters in strings. In quoted strings, a backslash at the very end of a line will cause the backslash itself and the line feed (LF or NL, new line) character to be ignored, so that you can wrap long strings. Without the backslash at the line end, the line feed character would become part of the string. </p>
<p> <code>Warning:</code> while these resemble C-style escape sequences, they are not the same. fetchmail only supports these eight styles. C supports more escape sequences that consist of backslash (\) and a single character, but does not support decimal codes and does not require the leading 0 in octal notation. Example: fetchmail interprets \233 the same as \xE9 (Latin small letter e with acute), where C would interpret \233 as octal 0233 = \x9B (CSI, control sequence introducer). </p>
<p> Each server entry consists of one of the keywords &#8216;poll&#8217; or &#8216;skip&#8217;, followed by a server name, followed by server options, followed by any number of user (or username) descriptions, followed by user options. Note: the most common cause of syntax errors is mixing up user and server options or putting user options before the user descriptions. </p>
<p> For backward compatibility, the word &#8216;server&#8217; is a synonym for &#8216;poll&#8217;. </p>
<p> You can use the noise keywords &#8216;and&#8217;, &#8216;with&#8217;, &#8216;has&#8217;, &#8216;wants&#8217;, and &#8216;options&#8217; anywhere in an entry to make it resemble English. They&#8217;re ignored, but but can make entries much easier to read at a glance. The punctuation characters &#8216;:&#8216;, &#8216;;&#8216; and &#8216;,&#8216; are also ignored.  </p>
<h3>Poll vs. Skip</h3>
<p> The &#8216;poll&#8217; verb tells fetchmail to query this host when it is run with no arguments. The &#8216;skip&#8217; verb tells <code>fetchmail</code> not to poll this host unless it is explicitly named on the command line. (The &#8216;skip&#8217; verb allows you to experiment with test entries safely, or easily disable entries for hosts that are temporarily down.)  </p>
<h3>Keyword/Option Summary</h3>
<p> Here are the legal options. Keyword suffixes enclosed in square brackets are optional. Those corresponding to short command-line options are followed by &#8216;-&#8216; and the appropriate option letter. If option is only relevant to a single mode of operation, it is noted as &#8216;s&#8217; or &#8216;m&#8217; for singledrop- or multidrop-mode, respectively. </p>
<p> Here are the legal global options: </p>
<table>
<tr VALIGN=top>
<td>Keyword </td>
<td>Opt</td>
<td>Mode</td>
<td>Function
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>set daemon </td>
<td>-d</td>
<td></td>
<td> Set a background poll interval in seconds. 
</td>
</tr>
<tr VALIGN=top>
<td>set postmaster </td>
<td></td>
<td></td>
<td> Give the name of the last-resort mail recipient (default: user running fetchmail, &quot;postmaster&quot; if run by the root user) 
</td>
</tr>
<tr VALIGN=top>
<td>set bouncemail</td>
<td></td>
<td></td>
<td> Direct error mail to the sender (default) 
</td>
</tr>
<tr VALIGN=top>
<td>set no bouncemail</td>
<td></td>
<td></td>
<td> Direct error mail to the local postmaster (as per the &#8216;postmaster&#8217; global option above). 
</td>
</tr>
<tr VALIGN=top>
<td>set no spambounce</td>
<td></td>
<td></td>
<td> Do not bounce spam-blocked mail (default). 
</td>
</tr>
<tr VALIGN=top>
<td>set spambounce</td>
<td></td>
<td></td>
<td> Bounce blocked spam-blocked mail (as per the &#8216;antispam&#8217; user option) back to the destination as indicated by the &#8216;bouncemail&#8217; global option. Warning: Do not use this to bounce spam back to the sender - most spam is sent with false sender address and thus this option hurts innocent bystanders. 
</td>
</tr>
<tr VALIGN=top>
<td>set no softbounce</td>
<td></td>
<td></td>
<td> Delete permanently undeliverable mail. It is recommended to use this option if the configuration has been thoroughly tested. 
</td>
</tr>
<tr VALIGN=top>
<td>set softbounce</td>
<td></td>
<td></td>
<td> Keep permanently undeliverable mail as though a temporary error had occurred (default). 
</td>
</tr>
<tr VALIGN=top>
<td>set logfile </td>
<td>-L</td>
<td></td>
<td> Name of a file to append error and status messages to. Only effective in daemon mode and if fetchmail detaches. If effective, overrides <code>set syslog</code>. 
</td>
</tr>
<tr VALIGN=top>
<td>set pidfile </td>
<td>-p</td>
<td></td>
<td> Name of the PID file. 
</td>
</tr>
<tr VALIGN=top>
<td>set idfile </td>
<td>-i</td>
<td></td>
<td> Name of the file to store UID lists in. 
</td>
</tr>
<tr VALIGN=top>
<td>set syslog</td>
<td></td>
<td></td>
<td> Do error logging through <a href="/docs/linux/man/3-syslog/">syslog</a>(3). May be overridden by <code>set logfile</code>. 
</td>
</tr>
<tr VALIGN=top>
<td>set no syslog </td>
<td></td>
<td></td>
<td> Turn off error logging through <a href="/docs/linux/man/3-syslog/">syslog</a>(3). (default) 
</td>
</tr>
<tr VALIGN=top>
<td>set properties </td>
<td></td>
<td></td>
<td> String value that is ignored by fetchmail (may be used by extension scripts). 
</td>
</tr>
</table>
<p> Here are the legal server options: </p>
<table>
<tr VALIGN=top>
<td>Keyword </td>
<td>Opt</td>
<td>Mode</td>
<td>Function
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>via </td>
<td></td>
<td></td>
<td> Specify DNS name of mailserver, overriding poll name 
</td>
</tr>
<tr VALIGN=top>
<td>proto[col]</td>
<td>-p</td>
<td></td>
<td> Specify protocol (case insensitive): POP2, POP3, IMAP, APOP, KPOP 
</td>
</tr>
<tr VALIGN=top>
<td>local[domains]</td>
<td></td>
<td>m</td>
<td> Specify domain(s) to be regarded as local 
</td>
</tr>
<tr VALIGN=top>
<td>port </td>
<td></td>
<td></td>
<td> Specify TCP/IP service port (obsolete, use &#8216;service&#8217; instead). 
</td>
</tr>
<tr VALIGN=top>
<td>service </td>
<td>-P</td>
<td></td>
<td> Specify service name (a numeric value is also allowed and considered a TCP/IP port number). 
</td>
</tr>
<tr VALIGN=top>
<td>auth[enticate]</td>
<td></td>
<td></td>
<td> Set authentication type (default &#8216;any&#8217;) 
</td>
</tr>
<tr VALIGN=top>
<td>timeout </td>
<td>-t</td>
<td></td>
<td> Server inactivity timeout in seconds (default 300) 
</td>
</tr>
<tr VALIGN=top>
<td>envelope</td>
<td>-E</td>
<td>m</td>
<td> Specify envelope-address header name 
</td>
</tr>
<tr VALIGN=top>
<td>no envelope</td>
<td></td>
<td>m</td>
<td> Disable looking for envelope address 
</td>
</tr>
<tr VALIGN=top>
<td>qvirtual</td>
<td>-Q</td>
<td>m</td>
<td> Qmail virtual domain prefix to remove from user name 
</td>
</tr>
<tr VALIGN=top>
<td>aka </td>
<td></td>
<td>m</td>
<td> Specify alternate DNS names of mailserver 
</td>
</tr>
<tr VALIGN=top>
<td>interface</td>
<td>-I</td>
<td></td>
<td> specify IP interface(s) that must be up for server poll to take place 
</td>
</tr>
<tr VALIGN=top>
<td>monitor </td>
<td>-M</td>
<td></td>
<td> Specify IP address to monitor for activity 
</td>
</tr>
<tr VALIGN=top>
<td>plugin </td>
<td></td>
<td></td>
<td> Specify command through which to make server connections. 
</td>
</tr>
<tr VALIGN=top>
<td>plugout </td>
<td></td>
<td></td>
<td> Specify command through which to make listener connections. 
</td>
</tr>
<tr VALIGN=top>
<td>dns </td>
<td></td>
<td>m</td>
<td> Enable DNS lookup for multidrop (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no dns </td>
<td></td>
<td>m</td>
<td> Disable DNS lookup for multidrop 
</td>
</tr>
<tr VALIGN=top>
<td>checkalias</td>
<td></td>
<td>m</td>
<td> Do comparison by IP address for multidrop 
</td>
</tr>
<tr VALIGN=top>
<td>no checkalias</td>
<td></td>
<td>m</td>
<td> Do comparison by name for multidrop (default) 
</td>
</tr>
<tr VALIGN=top>
<td>uidl </td>
<td>-U</td>
<td></td>
<td> Force POP3 to use client-side UIDLs (recommended) 
</td>
</tr>
<tr VALIGN=top>
<td>no uidl </td>
<td></td>
<td></td>
<td> Turn off POP3 use of client-side UIDLs (default) 
</td>
</tr>
<tr VALIGN=top>
<td>interval </td>
<td></td>
<td></td>
<td> Only check this site every N poll cycles; N is a numeric argument. 
</td>
</tr>
<tr VALIGN=top>
<td>tracepolls</td>
<td></td>
<td></td>
<td> Add poll tracing information to the Received header 
</td>
</tr>
<tr VALIGN=top>
<td>principal </td>
<td></td>
<td></td>
<td> Set Kerberos principal (only useful with IMAP and kerberos) 
</td>
</tr>
<tr VALIGN=top>
<td>esmtpname </td>
<td></td>
<td></td>
<td> Set name for RFC2554 authentication to the ESMTP server. 
</td>
</tr>
<tr VALIGN=top>
<td>esmtppassword</td>
<td></td>
<td></td>
<td> Set password for RFC2554 authentication to the ESMTP server. 
</td>
</tr>
<tr VALIGN=top>
<td>bad-header</td>
<td></td>
<td></td>
<td> How to treat messages with a bad header. Can be reject (default) or accept. 
</td>
</tr>
</table>
<p> Here are the legal user descriptions and options: </p>
<table>
<tr VALIGN=top>
<td>Keyword </td>
<td>Opt</td>
<td>Mode</td>
<td>Function
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>user[name]</td>
<td>-u</td>
<td></td>
<td> This is the user description and must come first after server description and after possible server options, and before user options.  It sets the remote user name if by itself or followed by &#8216;there&#8217;, or the local user name if followed by &#8216;here&#8217;. 
</td>
</tr>
<tr VALIGN=top>
<td>is </td>
<td></td>
<td></td>
<td> Connect local and remote user names 
</td>
</tr>
<tr VALIGN=top>
<td>to </td>
<td></td>
<td></td>
<td> Connect local and remote user names 
</td>
</tr>
<tr VALIGN=top>
<td>pass[word]</td>
<td></td>
<td></td>
<td> Specify remote account password 
</td>
</tr>
<tr VALIGN=top>
<td>ssl </td>
<td></td>
<td></td>
<td> Connect to server over the specified base protocol using SSL encryption 
</td>
</tr>
<tr VALIGN=top>
<td>sslcert </td>
<td></td>
<td></td>
<td> Specify file for <code>client side</code> public SSL certificate 
</td>
</tr>
<tr VALIGN=top>
<td>sslcertck</td>
<td></td>
<td></td>
<td> Enable strict certificate checking and abort connection on failure. Default only since fetchmail v6.4.0. 
</td>
</tr>
<tr VALIGN=top>
<td>no sslcertck</td>
<td></td>
<td></td>
<td> Disable strict certificate checking and permit connections to continue on failed verification. Discouraged. Should only be used together with sslfingerprint. 
</td>
</tr>
<tr VALIGN=top>
<td>sslcertfile</td>
<td></td>
<td></td>
<td> Specify file with trusted CA certificates 
</td>
</tr>
<tr VALIGN=top>
<td>sslcertpath</td>
<td></td>
<td></td>
<td> Specify c_rehash-ed directory with trusted CA certificates. 
</td>
</tr>
<tr VALIGN=top>
<td>sslfingerprint</td>
<td>&lt;HASH&gt; </td>
<td></td>
<td> Specify the expected server certificat finger print. Fetchmail will disconnect and log an error if it does not match. 
</td>
</tr>
<tr VALIGN=top>
<td>sslkey </td>
<td></td>
<td></td>
<td> Specify file for <code>client side</code> private SSL key 
</td>
</tr>
<tr VALIGN=top>
<td>sslproto</td>
<td></td>
<td></td>
<td> Force ssl protocol for connection 
</td>
</tr>
<tr VALIGN=top>
<td>folder </td>
<td>-r</td>
<td></td>
<td> Specify remote folder to query 
</td>
</tr>
<tr VALIGN=top>
<td>smtphost</td>
<td>-S</td>
<td></td>
<td> Specify smtp host(s) to forward to 
</td>
</tr>
<tr VALIGN=top>
<td>fetchdomains</td>
<td></td>
<td>m</td>
<td> Specify domains for which mail should be fetched 
</td>
</tr>
<tr VALIGN=top>
<td>smtpaddress</td>
<td>-D</td>
<td></td>
<td> Specify the domain to be put in RCPT TO lines 
</td>
</tr>
<tr VALIGN=top>
<td>smtpname</td>
<td></td>
<td></td>
<td> Specify the user and domain to be put in RCPT TO lines 
</td>
</tr>
<tr VALIGN=top>
<td>antispam</td>
<td>-Z</td>
<td></td>
<td> Specify what SMTP returns are interpreted as spam-policy blocks 
</td>
</tr>
<tr VALIGN=top>
<td>mda </td>
<td>-m</td>
<td></td>
<td> Specify MDA for local delivery 
</td>
</tr>
<tr VALIGN=top>
<td>bsmtp </td>
<td></td>
<td></td>
<td> Specify BSMTP batch file to append to 
</td>
</tr>
<tr VALIGN=top>
<td>preconnect</td>
<td></td>
<td></td>
<td> Command to be executed before each connection 
</td>
</tr>
<tr VALIGN=top>
<td>postconnect</td>
<td></td>
<td></td>
<td> Command to be executed after each connection 
</td>
</tr>
<tr VALIGN=top>
<td>keep </td>
<td>-k</td>
<td></td>
<td> Don&#8217;t delete seen messages from server (for POP3, uidl is recommended) 
</td>
</tr>
<tr VALIGN=top>
<td>flush </td>
<td>-F</td>
<td></td>
<td> Flush all seen messages before querying (DANGEROUS) 
</td>
</tr>
<tr VALIGN=top>
<td>limitflush </td>
<td></td>
<td></td>
<td> Flush all oversized messages before querying 
</td>
</tr>
<tr VALIGN=top>
<td>fetchall</td>
<td>-a</td>
<td></td>
<td> Fetch all messages whether seen or not 
</td>
</tr>
<tr VALIGN=top>
<td>rewrite </td>
<td></td>
<td></td>
<td> Rewrite destination addresses for reply (default) 
</td>
</tr>
<tr VALIGN=top>
<td>stripcr </td>
<td></td>
<td></td>
<td> Strip carriage returns from ends of lines 
</td>
</tr>
<tr VALIGN=top>
<td>forcecr </td>
<td></td>
<td></td>
<td> Force carriage returns at ends of lines 
</td>
</tr>
<tr VALIGN=top>
<td>pass8bits</td>
<td></td>
<td></td>
<td> Force BODY=8BITMIME to ESMTP listener 
</td>
</tr>
<tr VALIGN=top>
<td>dropstatus</td>
<td></td>
<td></td>
<td> Strip Status and X-Mozilla-Status lines out of incoming mail 
</td>
</tr>
<tr VALIGN=top>
<td>dropdelivered</td>
<td></td>
<td></td>
<td> Strip Delivered-To lines out of incoming mail 
</td>
</tr>
<tr VALIGN=top>
<td>mimedecode</td>
<td></td>
<td></td>
<td> Convert quoted-printable to 8-bit in MIME messages 
</td>
</tr>
<tr VALIGN=top>
<td>idle </td>
<td></td>
<td></td>
<td> Idle waiting for new messages after each poll (IMAP only) 
</td>
</tr>
<tr VALIGN=top>
<td>no keep </td>
<td>-K</td>
<td></td>
<td> Delete seen messages from server (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no flush</td>
<td></td>
<td></td>
<td> Don&#8217;t flush all seen messages before querying (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no fetchall</td>
<td></td>
<td></td>
<td> Retrieve only new messages (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no rewrite</td>
<td></td>
<td></td>
<td> Don&#8217;t rewrite headers 
</td>
</tr>
<tr VALIGN=top>
<td>no stripcr</td>
<td></td>
<td></td>
<td> Don&#8217;t strip carriage returns (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no forcecr</td>
<td></td>
<td></td>
<td> Don&#8217;t force carriage returns at EOL (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no pass8bits</td>
<td></td>
<td></td>
<td> Don&#8217;t force BODY=8BITMIME to ESMTP listener (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no dropstatus</td>
<td></td>
<td></td>
<td> Don&#8217;t drop Status headers (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no dropdelivered</td>
<td></td>
<td></td>
<td> Don&#8217;t drop Delivered-To headers (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no mimedecode</td>
<td></td>
<td></td>
<td> Don&#8217;t convert quoted-printable to 8-bit in MIME messages (default) 
</td>
</tr>
<tr VALIGN=top>
<td>no idle </td>
<td></td>
<td></td>
<td> Don&#8217;t idle waiting for new messages after each poll (IMAP only) 
</td>
</tr>
<tr VALIGN=top>
<td>limit </td>
<td>-l</td>
<td></td>
<td> Set message size limit 
</td>
</tr>
<tr VALIGN=top>
<td>warnings </td>
<td>-w</td>
<td></td>
<td> Set message size warning interval 
</td>
</tr>
<tr VALIGN=top>
<td>batchlimit</td>
<td>-b</td>
<td></td>
<td> Max # messages to forward in single connect 
</td>
</tr>
<tr VALIGN=top>
<td>fetchlimit</td>
<td>-B</td>
<td></td>
<td> Max # messages to fetch in single connect 
</td>
</tr>
<tr VALIGN=top>
<td>fetchsizelimit</td>
<td></td>
<td></td>
<td> Max # message sizes to fetch in single transaction 
</td>
</tr>
<tr VALIGN=top>
<td>fastuidl</td>
<td></td>
<td></td>
<td> Use binary search for first unseen message (POP3 only) 
</td>
</tr>
<tr VALIGN=top>
<td>expunge </td>
<td>-e</td>
<td></td>
<td> Perform an expunge on every #th message (IMAP and POP3 only) 
</td>
</tr>
<tr VALIGN=top>
<td>properties </td>
<td></td>
<td></td>
<td> String value is ignored by fetchmail (may be used by extension scripts) 
</td>
</tr>
</table>
<p> All user options must begin with a user description (user or username option) and <i>follow</i> all server descriptions and options. </p>
<p> In the .fetchmailrc file, the &#8216;envelope&#8217; string argument may be preceded by a whitespace-separated number. This number, if specified, is the number of such headers to skip over (that is, an argument of 1 selects the second header of the given type). This is sometime useful for ignoring bogus envelope headers created by an ISP&#8217;s local delivery agent or internal forwards (through mail inspection systems, for instance).  </p>
<h3>Keywords Not Corresponding To Option Switches</h3>
<p> The &#8216;folder&#8217; and &#8216;smtphost&#8217; options (unlike their command-line equivalents) can take a space- or comma-separated list of names following them. </p>
<p> All options correspond to the obvious command-line arguments, except the following: &#8216;via&#8217;, &#8216;interval&#8217;, &#8216;aka&#8217;, &#8216;is&#8217;, &#8216;to&#8217;, &#8216;dns&#8217;/&#8216;no dns&#8217;, &#8216;checkalias&#8217;/&#8216;no checkalias&#8217;, &#8216;password&#8217;, &#8216;preconnect&#8217;, &#8216;postconnect&#8217;, &#8216;localdomains&#8217;, &#8216;stripcr&#8217;/&#8216;no stripcr&#8217;, &#8216;forcecr&#8217;/&#8216;no forcecr&#8217;, &#8216;pass8bits&#8217;/&#8216;no pass8bits&#8217; &#8216;dropstatus/no dropstatus&#8217;, &#8216;dropdelivered/no dropdelivered&#8217;, &#8216;mimedecode/no mimedecode&#8217;, &#8216;no idle&#8217;, and &#8216;no envelope&#8217;. </p>
<p> The &#8216;via&#8217; option is for if you want to have more than one configuration pointing at the same site. If it is present, the string argument will be taken as the actual DNS name of the mailserver host to query. This will override the argument of poll, which can then simply be a distinct label for the configuration (e.g. what you would give on the command line to explicitly query this host). </p>
<p> The &#8216;interval&#8217; option (which takes a numeric argument) allows you to poll a server less frequently than the basic poll interval. If you say &#8216;interval N&#8217; the server this option is attached to will only be queried every N poll intervals.  </p>
<h3>Singledrop vs. Multidrop options</h3>
<p> Please ensure you read the section titled <code>THE USE AND ABUSE OF MULTIDROP MAILBOXES </code> if you intend to use multidrop mode. </p>
<p> The &#8216;is&#8217; or &#8216;to&#8217; keywords associate the following local (client) name(s) (or server-name to client-name mappings separated by =) with the mailserver user name in the entry. If an is/to list has &#8216;*&#8216; as its last name, unrecognized names are simply passed through. Note that until <code>fetchmail</code> version 6.3.4 inclusively, these lists could only contain local parts of user names (fetchmail would only look at the part before the @ sign). <code>fetchmail</code> versions 6.3.5 and newer support full addresses on the left hand side of these mappings, and they take precedence over any &#8216;localdomains&#8217;, &#8216;aka&#8217;, &#8216;via&#8217; or similar mappings. </p>
<p> A single local name can be used to support redirecting your mail when your username on the client machine is different from your name on the mailserver. When there is only a single local name, mail is forwarded to that local username regardless of the message&#8217;s Received, To, Cc, and Bcc headers. In this case, <code>fetchmail</code> never does DNS lookups. </p>
<p> When there is more than one local name (or name mapping), <code>fetchmail</code> looks at the envelope header, if configured, and otherwise at the Received, To, Cc, and Bcc headers of retrieved mail (this is &#8216;multidrop mode&#8217;). It looks for addresses with hostname parts that match your poll name or your &#8216;via&#8217;, &#8216;aka&#8217; or &#8216;localdomains&#8217; options, and usually also for hostname parts which DNS tells it are aliases of the mailserver. See the discussion of &#8216;dns&#8217;, &#8216;checkalias&#8217;, &#8216;localdomains&#8217;, and &#8216;aka&#8217; for details on how matching addresses are handled. </p>
<p> If <code>fetchmail</code> cannot match any mailserver usernames or localdomain addresses, the mail will be bounced. Normally it will be bounced to the sender, but if the &#8216;bouncemail&#8217; global option is off, the mail will go to the local postmaster instead. (see the &#8216;postmaster&#8217; global option). See also BUGS. </p>
<p> The &#8216;dns&#8217; option (normally on) controls the way addresses from multidrop mailboxes are checked. On, it enables logic to check each host address that does not match an &#8216;aka&#8217; or &#8216;localdomains&#8217; declaration by looking it up with DNS. When a mailserver username is recognized attached to a matching hostname part, its local mapping is added to the list of local recipients. </p>
<p> The &#8216;checkalias&#8217; option (normally off) extends the lookups performed by the &#8216;dns&#8217; keyword in multidrop mode, providing a way to cope with remote MTAs that identify themselves using their canonical name, while they&#8217;re polled using an alias. When such a server is polled, checks to extract the envelope address fail, and <code>fetchmail</code> reverts to delivery using the To/Cc/Bcc headers (See below &#8216;Header vs. Envelope addresses&#8217;). Specifying this option instructs <code>fetchmail</code> to retrieve all the IP addresses associated with both the poll name and the name used by the remote MTA and to do a comparison of the IP addresses. This comes in handy in situations where the remote server undergoes frequent canonical name changes, that would otherwise require modifications to the rcfile. &#8216;checkalias&#8217; has no effect if &#8216;no dns&#8217; is specified in the rcfile. </p>
<p> The &#8216;aka&#8217; option is for use with multidrop mailboxes. It allows you to pre-declare a list of DNS aliases for a server. This is an optimization hack that allows you to trade space for speed. When <code>fetchmail</code>, while processing a multidrop mailbox, grovels through message headers looking for names of the mailserver, pre-declaring common ones can save it from having to do DNS lookups. Note: the names you give as arguments to &#8216;aka&#8217; are matched as suffixes -- if you specify (say) &#8216;aka netaxs.com&#8217;, this will match not just a hostname netaxs.com, but any hostname that ends with &#8216;.netaxs.com&#8217;; such as (say) pop3.netaxs.com and mail.netaxs.com. </p>
<p> The &#8216;localdomains&#8217; option allows you to declare a list of domains which fetchmail should consider local. When fetchmail is parsing address lines in multidrop modes, and a trailing segment of a host name matches a declared local domain, that address is passed through to the listener or MDA unaltered (local-name mappings are <i>not</i> applied). </p>
<p> If you are using &#8216;localdomains&#8217;, you may also need to specify &#8216;no envelope&#8217;, which disables <code>fetchmail</code>&#8216;s normal attempt to deduce an envelope address from the Received line or X-Envelope-To header or whatever header has been previously set by &#8216;envelope&#8217;. If you set &#8216;no envelope&#8217; in the defaults entry it is possible to undo that in individual entries by using &#8216;envelope &lt;string&gt;&#8216;. As a special case, &#8216;envelope &quot;Received&quot;&#8216; restores the default parsing of Received lines. </p>
<p> The <code>password</code> option requires a string argument, which is the password to be used with the entry&#8217;s server. </p>
<p> The &#8216;preconnect&#8217; keyword allows you to specify a shell command to be executed just before each time <code>fetchmail</code> establishes a mailserver connection. This may be useful if you are attempting to set up secure POP connections with the aid of <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). If the command returns a nonzero status, the poll of that mailserver will be aborted. </p>
<p> Similarly, the &#8216;postconnect&#8217; keyword similarly allows you to specify a shell command to be executed just after each time a mailserver connection is taken down. </p>
<p> The &#8216;forcecr&#8217; option controls whether lines terminated by LF only are given CRLF termination before forwarding. Strictly speaking RFC821 requires this, but few MTAs enforce the requirement so this option is normally off (only one such MTA, qmail, is in significant use at time of writing). </p>
<p> The &#8216;stripcr&#8217; option controls whether carriage returns are stripped out of retrieved mail before it is forwarded. It is normally not necessary to set this, because it defaults to &#8216;on&#8217; (CR stripping enabled) when there is an MDA declared but &#8216;off&#8217; (CR stripping disabled) when forwarding is via SMTP. If &#8216;stripcr&#8217; and &#8216;forcecr&#8217; are both on, &#8216;stripcr&#8217; will override. </p>
<p> The &#8216;pass8bits&#8217; option exists to cope with Microsoft mail programs that stupidly slap a &quot;Content-Transfer-Encoding: 7bit&quot; on everything. With this option off (the default) and such a header present, <code>fetchmail</code> declares BODY=7BIT to an ESMTP-capable listener; this causes problems for messages actually using 8-bit ISO or KOI-8 character sets, which will be garbled by having the high bits of all characters stripped. If &#8216;pass8bits&#8217; is on, <code>fetchmail</code> is forced to declare BODY=8BITMIME to any ESMTP-capable listener. If the listener is 8-bit-clean (as all the major ones now are) the right thing will probably result. </p>
<p> The &#8216;dropstatus&#8217; option controls whether nonempty Status and X-Mozilla-Status lines are retained in fetched mail (the default) or discarded. Retaining them allows your MUA to see what messages (if any) were marked seen on the server. On the other hand, it can confuse some new-mail notifiers, which assume that anything with a Status line in it has been seen. (Note: the empty Status lines inserted by some buggy POP servers are unconditionally discarded.) </p>
<p> The &#8216;dropdelivered&#8217; option controls whether Delivered-To headers will be kept in fetched mail (the default) or discarded. These headers are added by Qmail and Postfix mailservers in order to avoid mail loops but may get in your way if you try to &quot;mirror&quot; a mailserver within the same domain. Use with caution. </p>
<p> The &#8216;mimedecode&#8217; option controls whether MIME messages using the quoted-printable encoding are automatically converted into pure 8-bit data. If you are delivering mail to an ESMTP-capable, 8-bit-clean listener (that includes all of the major MTAs like sendmail), then this will automatically convert quoted-printable message headers and data into 8-bit data, making it easier to understand when reading mail. If your e-mail programs know how to deal with MIME messages, then this option is not needed. The mimedecode option is off by default, because doing RFC2047 conversion on headers throws away character-set information and can lead to bad results if the encoding of the headers differs from the body encoding. </p>
<p> The &#8216;idle&#8217; option is intended to be used with IMAP servers supporting the RFC2177 IDLE command extension, but does not strictly require it. If it is enabled, and fetchmail detects that IDLE is supported, an IDLE will be issued at the end of each poll. This will tell the IMAP server to hold the connection open and notify the client when new mail is available. If IDLE is not supported, fetchmail will simulate it by periodically issuing NOOP. If you need to poll a link frequently, IDLE can save bandwidth by eliminating TCP/IP connects and LOGIN/LOGOUT sequences. On the other hand, an IDLE connection will eat almost all of your fetchmail&#8217;s time, because it will never drop the connection and allow other polls to occur unless the server times out the IDLE. It also doesn&#8217;t work with multiple folders; only the first folder will ever be polled. </p>
<p> The &#8216;properties&#8217; option is an extension mechanism. It takes a string argument, which is ignored by fetchmail itself. The string argument may be used to store configuration information for scripts which require it. In particular, the output of &#8216;--configdump&#8217; option will make properties associated with a user entry readily available to a Python script.  </p>
<h3>Miscellaneous Run Control Options</h3>
<p> The words &#8216;here&#8217; and &#8216;there&#8217; have useful English-like significance. Normally &#8216;user eric is esr&#8217; would mean that mail for the remote user &#8216;eric&#8217; is to be delivered to &#8216;esr&#8217;, but you can make this clearer by saying &#8216;user eric there is esr here&#8217;, or reverse it by saying &#8216;user esr here is eric there&#8217; </p>
<p> Legal protocol identifiers for use with the &#8216;protocol&#8217; keyword are: </p>
<pre><code>    auto (or AUTO) (legacy, to be removed from future release)
    pop2 (or POP2) (legacy, to be removed from future release)
    pop3 (or POP3)
    sdps (or SDPS)
    imap (or IMAP)
    apop (or APOP)
    kpop (or KPOP)
</code></pre>
<p> Legal authentication types are &#8216;any&#8217;, &#8216;password&#8217;, &#8216;kerberos&#8217;, &#8216;kerberos_v4&#8217;, &#8216;kerberos_v5&#8217; and &#8216;gssapi&#8217;, &#8216;cram-md5&#8217;, &#8216;otp&#8217;, &#8216;msn&#8217; (only for POP3), &#8216;ntlm&#8217;, &#8216;ssh&#8217;, &#8216;external&#8217; (only IMAP). The &#8216;password&#8217; type specifies authentication by normal transmission of a password (the password may be plain text or subject to protocol-specific encryption as in CRAM-MD5); &#8216;kerberos&#8217; tells <code>fetchmail</code> to try to get a Kerberos ticket at the start of each query instead, and send an arbitrary string as the password; and &#8216;gssapi&#8217; tells fetchmail to use GSSAPI authentication. See the description of the &#8216;auth&#8217; keyword for more. </p>
<p> Specifying &#8216;kpop&#8217; sets POP3 protocol over port 1109 with Kerberos V4 authentication. These defaults may be overridden by later options. </p>
<p> There are some global option statements: &#8216;set logfile&#8217; followed by a string sets the same global specified by --logfile. A command-line --logfile option will override this. Note that --logfile is only effective if fetchmail detaches itself from the terminal and the logfile already exists before fetchmail is run, and it overrides --syslog in this case. Also, &#8216;set daemon&#8217; sets the poll interval as --daemon does. This can be overridden by a command-line --daemon option; in particular --daemon~0 can be used to force foreground operation. The &#8216;set postmaster&#8217; statement sets the address to which multidrop mail defaults if there are no local matches. Finally, &#8216;set syslog&#8217; sends log messages to syslogd(8). </p>
<h2>DEBUGGING FETCHMAIL</h2>
<h3>Fetchmail crashing</h3>
<p> There are various ways in that fetchmail may &quot;crash&quot;, i. e. stop operation suddenly and unexpectedly. A &quot;crash&quot; usually refers to an error condition that the software did not handle by itself. A well-known failure mode is the &quot;segmentation fault&quot; or &quot;signal 11&quot; or &quot;SIGSEGV&quot; or just &quot;segfault&quot; for short. These can be caused by hardware or by software problems. Software-induced segfaults can usually be reproduced easily and in the same place, whereas hardware-induced segfaults can go away if the computer is rebooted, or powered off for a few hours, and can happen in random locations even if you use the software the same way. </p>
<p> For solving hardware-induced segfaults, find the faulty component and repair or replace it. may help you with details. </p>
<p> For solving software-induced segfaults, the developers may need a &quot;stack backtrace&quot;. </p>
<h3>Enabling fetchmail core dumps</h3>
<p> By default, fetchmail suppresses core dumps as these might contain passwords and other sensitive information. For debugging fetchmail crashes, obtaining a &quot;stack backtrace&quot; from a core dump is often the quickest way to solve the problem, and when posting your problem on a mailing list, the developers may ask you for a &quot;backtrace&quot;. </p>
<p> 1. To get useful backtraces, fetchmail needs to be installed without getting stripped of its compilation symbols. Unfortunately, most binary packages that are installed are stripped, and core files from symbol-stripped programs are worthless. So you may need to recompile fetchmail. On many systems, you can type </p>
<pre><code>        file `which fetchmail`
</code></pre>
<p> to find out if fetchmail was symbol-stripped or not. If yours was unstripped, fine, proceed, if it was stripped, you need to recompile the source code first. You do not usually need to install fetchmail in order to debug it. </p>
<p> 2. The shell environment that starts fetchmail needs to enable core dumps. The key is the &quot;maximum core (file) size&quot; that can usually be configured with a tool named &quot;limit&quot; or &quot;ulimit&quot;. See the documentation for your shell for details. In the popular bash shell, &quot;ulimit -Sc unlimited&quot; will allow the core dump. </p>
<p> 3. You need to tell fetchmail, too, to allow core dumps. To do this, run fetchmail with the <code>-d0 -v</code> options. It is often easier to also add <code>--nosyslog -N</code> as well. </p>
<p> Finally, you need to reproduce the crash. You can just start fetchmail from the directory where you compiled it by typing <code>./fetchmail</code>, so the complete command line will start with <code>./fetchmail -Nvd0 --nosyslog</code> and perhaps list your other options. </p>
<p> After the crash, run your debugger to obtain the core dump. The debugger will often be GNU GDB, you can then type (adjust paths as necessary) <code>gdb ./fetchmail fetchmail.core</code> and then, after GDB has started up and read all its files, type <code>backtrace full</code>, save the output (copy &amp; paste will do, the backtrace will be read by a human) and then type <code>quit</code> to leave gdb. <code>Note:</code> on some systems, the core files have different names, they might contain a number instead of the program name, or number and name, but it will usually have &quot;core&quot; as part of their name. </p>
<h2>INTERACTION WITH RFC 822</h2>
<p> When trying to determine the originating address of a message, fetchmail looks through headers in the following order: </p>
<pre><code>        Return-Path:
        Resent-Sender: (ignored if it doesn't contain an @ or !)
        Sender: (ignored if it doesn't contain an @ or !)
        Resent-From:
        From:
        Reply-To:
        Apparently-From:
</code></pre>
<p> The originating address is used for logging, and to set the MAIL FROM address when forwarding to SMTP. This order is intended to cope gracefully with receiving mailing list messages in multidrop mode. The intent is that if a local address doesn&#8217;t exist, the bounce message won&#8217;t be returned blindly to the author or to the list itself, but rather to the list manager (which is less annoying). </p>
<p> In multidrop mode, destination headers are processed as follows: First, fetchmail looks for the header specified by the &#8216;envelope&#8217; option in order to determine the local recipient address. If the mail is addressed to more than one recipient, the Received line won&#8217;t contain any information regarding recipient addresses. </p>
<p> Then fetchmail looks for the Resent-To:, Resent-Cc:, and Resent-Bcc: lines. If they exist, they should contain the final recipients and have precedence over their To:/Cc:/Bcc: counterparts. If the Resent-* lines don&#8217;t exist, the To:, Cc:, Bcc: and Apparently-To: lines are looked for. (The presence of a Resent-To: is taken to imply that the person referred by the To: address has already received the original copy of the mail.) </p>
<h2>CONFIGURATION EXAMPLES</h2>
<p> Note that although there are password declarations in a good many of the examples below, this is mainly for illustrative purposes. We recommend stashing account/password pairs in your $HOME/.netrc file, where they can be used not just by fetchmail but by <a href="/docs/linux/man/1-ftp/">ftp</a>(1) and other programs. </p>
<p> The basic format is: </p>
<dl>
<dd> <p> poll <i>SERVERNAME</i> protocol <i>PROTOCOL</i> username <i>NAME</i> password <i>PASSWORD</i> </p>
 </dd></dl>
<p> Example: </p>
<dl>
<dd> <pre><code>poll pop.provider.net protocol pop3 username &quot;jsmith&quot; password &quot;secret1&quot;
</code></pre>
 </dd></dl>
<p> Or, using some abbreviations: </p>
<dl>
<dd> <pre><code>poll pop.provider.net proto pop3 user &quot;jsmith&quot; password &quot;secret1&quot;
</code></pre>
 </dd></dl>
<p> Multiple servers may be listed: </p>
<dl>
<dd> <pre><code>poll pop.provider.net proto pop3 user &quot;jsmith&quot; pass &quot;secret1&quot;
poll other.provider.net proto pop2 user &quot;John.Smith&quot; pass &quot;My^Hat&quot;
</code></pre>
 </dd></dl>
<p> Here&#8217;s the same version with more whitespace and some noise words: </p>
<dl>
<dd> <pre><code>poll pop.provider.net proto pop3
     user &quot;jsmith&quot;, with password secret1, is &quot;jsmith&quot; here;
poll other.provider.net proto pop2:
     user &quot;John.Smith&quot;, with password &quot;My^Hat&quot;, is &quot;John.Smith&quot; here;
</code></pre>
 </dd></dl>
<p> If you need to include whitespace in a parameter string or start the latter with a number, enclose the string in double quotes. Thus: </p>
<dl>
<dd> <pre><code>poll mail.provider.net with proto pop3:
     user &quot;jsmith&quot; there has password &quot;4u but u can't krak this&quot;
     is jws here and wants mda &quot;/bin/mail&quot;
</code></pre>
 </dd></dl>
<p> You may have an initial server description headed by the keyword &#8216;defaults&#8217; instead of &#8216;poll&#8217; followed by a name. Such a record is interpreted as defaults for all queries to use. It may be overwritten by individual server descriptions. So, you could write: </p>
<dl>
<dd> <pre><code>defaults proto pop3
     user &quot;jsmith&quot;
poll pop.provider.net
     pass &quot;secret1&quot;
poll mail.provider.net
     user &quot;jjsmith&quot; there has password &quot;secret2&quot;
</code></pre>
 </dd></dl>
<p> It&#8217;s possible to specify more than one user per server. The &#8216;user&#8217; keyword leads off a user description, and every user specification in a multi-user entry must include it. Here&#8217;s an example: </p>
<dl>
<dd> <pre><code>poll pop.provider.net proto pop3 port 3111
     user &quot;jsmith&quot; with pass &quot;secret1&quot; is &quot;smith&quot; here
     user jones with pass &quot;secret2&quot; is &quot;jjones&quot; here keep
</code></pre>
 </dd></dl>
<p> This associates the local username &#8216;smith&#8217; with the pop.provider.net username &#8216;jsmith&#8217; and the local username &#8216;jjones&#8217; with the pop.provider.net username &#8216;jones&#8217;. Mail for &#8216;jones&#8217; is kept on the server after download. </p>
<p> Here&#8217;s what a simple retrieval configuration for a multidrop mailbox looks like: </p>
<dl>
<dd> <pre><code>poll pop.provider.net:
     user maildrop with pass secret1 to golux 'hurkle'='happy' snark here
</code></pre>
 </dd></dl>
<p> This says that the mailbox of account &#8216;maildrop&#8217; on the server is a multidrop box, and that messages in it should be parsed for the server user names &#8216;golux&#8217;, &#8216;hurkle&#8217;, and &#8216;snark&#8217;. It further specifies that &#8216;golux&#8217; and &#8216;snark&#8217; have the same name on the client as on the server, but mail for server user &#8216;hurkle&#8217; should be delivered to client user &#8216;happy&#8217;. </p>
<p> <code>Note</code> that <code>fetchmail,</code> until version 6.3.4, did NOT allow full user [at] domain specifications here, these would never match. <i>Fetchmail</i> 6.3.5 and newer support user [at] domain specifications on the left-hand side of a user mapping. </p>
<p> Here&#8217;s an example of another kind of multidrop connection: </p>
<dl>
<dd> <pre><code>poll pop.provider.net localdomains loonytoons.org toons.org
     envelope X-Envelope-To
     user maildrop with pass secret1 to * here
</code></pre>
 </dd></dl>
<p> This also says that the mailbox of account &#8216;maildrop&#8217; on the server is a multidrop box. It tells fetchmail that any address in the loonytoons.org or toons.org domains (including sub-domain addresses like &#8216;joe [at] daffy.loonytoons.org&#8217;) should be passed through to the local SMTP listener without modification. Be careful of mail loops if you do this! </p>
<p> Here&#8217;s an example configuration using ssh and the plugin option. The queries are made directly on the stdin and stdout of imapd via ssh. Note that in this setup, IMAP authentication can be skipped. </p>
<dl>
<dd> <pre><code>poll mailhost.net with proto imap:
     plugin &quot;ssh %h /usr/sbin/imapd&quot; auth ssh;
     user esr is esr here
</code></pre>
 </dd></dl>
<h2>THE USE AND ABUSE OF MULTIDROP MAILBOXES</h2>
<p> Use the multiple-local-recipients feature with caution -- it can bite. All multidrop features are ineffective in ETRN and ODMR modes. </p>
<p> Also, note that in multidrop mode duplicate mails are suppressed. A piece of mail is considered duplicate if it has the same message-ID as the message immediately preceding and more than one addressee. Such runs of messages may be generated when copies of a message addressed to multiple users are delivered to a multidrop box. </p>
<h3>Header vs. Envelope addresses</h3>
<p> The fundamental problem is that by having your mailserver toss several peoples&#8217; mail in a single maildrop box, you may have thrown away potentially vital information about who each piece of mail was actually addressed to (the &#8216;envelope address&#8217;, as opposed to the header addresses in the RFC822 To/Cc headers - the Bcc is not available at the receiving end). This &#8216;envelope address&#8217; is the address you need in order to reroute mail properly. </p>
<p> Sometimes <code>fetchmail</code> can deduce the envelope address. If the mailserver MTA is <code>sendmail</code> and the item of mail had just one recipient, the MTA will have written a &#8216;by/for&#8217; clause that gives the envelope addressee into its Received header. But this doesn&#8217;t work reliably for other MTAs, nor if there is more than one recipient. By default, <code>fetchmail</code> looks for envelope addresses in these lines; you can restore this default with -E &quot;Received&quot; or &#8216;envelope Received&#8217;. </p>
<p> <code>As a better alternative,</code> some SMTP listeners and/or mail servers insert a header in each message containing a copy of the envelope addresses. This header (when it exists) is often &#8216;X-Original-To&#8217;, &#8216;Delivered-To&#8217; or &#8216;X-Envelope-To&#8217;. Fetchmail&#8217;s assumption about this can be changed with the -E or &#8216;envelope&#8217; option. Note that writing an envelope header of this kind exposes the names of recipients (including blind-copy recipients) to all receivers of the messages, so the upstream must store one copy of the message per recipient to avoid becoming a privacy problem. </p>
<p> Postfix, since version 2.0, writes an X-Original-To: header which contains a copy of the envelope as it was received. </p>
<p> Qmail and Postfix generally write a &#8216;Delivered-To&#8217; header upon delivering the message to the mail spool and use it to avoid mail loops. Qmail virtual domains however will prefix the user name with a string that normally matches the user&#8217;s domain. To remove this prefix you can use the -Q or &#8216;qvirtual&#8217; option. </p>
<p> Sometimes, unfortunately, neither of these methods works. That is the point when you should contact your ISP and ask them to provide such an envelope header, and you should not use multidrop in this situation. When they all fail, fetchmail must fall back on the contents of To/Cc headers (Bcc headers are not available - see below) to try to determine recipient addressees -- and these are unreliable. In particular, mailing-list software often ships mail with only the list broadcast address in the To header. </p>
<p> <code>Note that a future version of fetchmail</code> may remove To/Cc parsing! </p>
<p> When <code>fetchmail</code> cannot deduce a recipient address that is local, and the intended recipient address was anyone other than fetchmail&#8217;s invoking user, <code>mail will get lost.</code> This is what makes the multidrop feature risky without proper envelope information. </p>
<p> A related problem is that when you blind-copy a mail message, the Bcc information is carried <i>only</i> as envelope address (it&#8217;s removed from the headers by the sending mail server, so fetchmail can see it only if there is an X-Envelope-To header). Thus, blind-copying to someone who gets mail over a fetchmail multidrop link will fail unless the the mailserver host routinely writes X-Envelope-To or an equivalent header into messages in your maildrop. </p>
<p> <code>In conclusion, mailing lists and Bcc&#8217;d mail can only work if the server you&#8217;re fetching from</code> </p>
<dl>
<dt>(1)</dt>
<dd> <p> <code>stores one copy of the message per recipient in your domain and</code> </p>
 </dd>
<dt>(2)</dt>
<dd> <p> <code>records the envelope information in a special header (X-Original-To, Delivered-To, X-Envelope-To).</code> </p>
 </dd></dl>
<h3>Good Ways To Use Multidrop Mailboxes</h3>
<p> Multiple local names can be used to administer a mailing list from the client side of a <code>fetchmail</code> collection. Suppose your name is &#8216;esr&#8217;, and you want to both pick up your own mail and maintain a mailing list called (say) &quot;fetchmail-friends&quot;, and you want to keep the alias list on your client machine. </p>
<p> On your server, you can alias &#8216;fetchmail-friends&#8217; to &#8216;esr&#8217;; then, in your <i>.fetchmailrc</i>, declare &#8216;to esr fetchmail-friends here&#8217;. Then, when mail including &#8216;fetchmail-friends&#8217; as a local address gets fetched, the list name will be appended to the list of recipients your SMTP listener sees. Therefore it will undergo alias expansion locally. Be sure to include &#8216;esr&#8217; in the local alias expansion of fetchmail-friends, or you&#8217;ll never see mail sent only to the list. Also be sure that your listener has the &quot;me-too&quot; option set (sendmail&#8217;s -oXm command-line option or OXm declaration) so your name isn&#8217;t removed from alias expansions in messages you send. </p>
<p> This trick is not without its problems, however. You&#8217;ll begin to see this when a message comes in that is addressed only to a mailing list you do <i>not</i> have declared as a local name. Each such message will feature an &#8216;X-Fetchmail-Warning&#8217; header which is generated because fetchmail cannot find a valid local name in the recipient addresses. Such messages default (as was described above) to being sent to the local user running <code>fetchmail</code>, but the program has no way to know that that&#8217;s actually the right thing. </p>
<h3>Bad Ways To Abuse Multidrop Mailboxes</h3>
<p> Multidrop mailboxes and <code>fetchmail</code> serving multiple users in daemon mode do not mix. The problem, again, is mail from mailing lists, which typically does not have an individual recipient address on it. Unless <code>fetchmail</code> can deduce an envelope address, such mail will only go to the account running fetchmail (probably root). Also, blind-copied users are very likely never to see their mail at all. </p>
<p> If you&#8217;re tempted to use <code>fetchmail</code> to retrieve mail for multiple users from a single mail drop via POP or IMAP, think again (and reread the section on header and envelope addresses above). It would be smarter to just let the mail sit in the mailserver&#8217;s queue and use fetchmail&#8217;s ETRN or ODMR modes to trigger SMTP sends periodically (of course, this means you have to poll more frequently than the mailserver&#8217;s expiry period). If you can&#8217;t arrange this, try setting up a UUCP feed. </p>
<p> If you absolutely <i>must</i> use multidrop for this purpose, make sure your mailserver writes an envelope-address header that fetchmail can see. Otherwise you <i>will</i> lose mail and it <i>will</i> come back to haunt you. </p>
<h3>Speeding Up Multidrop Checking</h3>
<p> Normally, when multiple users are declared <code>fetchmail</code> extracts recipient addresses as described above and checks each host part with DNS to see if it&#8217;s an alias of the mailserver. If so, the name mappings described in the &quot;to ... here&quot; declaration are done and the mail locally delivered. </p>
<p> This is a convenient but also slow method. To speed it up, pre-declare mailserver aliases with &#8216;aka&#8217;; these are checked before DNS lookups are done. If you&#8217;re certain your aka list contains <code>all</code> DNS aliases of the mailserver (and all MX names pointing at it - note this may change in a future version) you can declare &#8216;no dns&#8217; to suppress DNS lookups entirely and <i>only</i> match against the aka list. </p>
<h2>SOCKS</h2>
<p> Support for socks4/5 is a <code>compile time</code> configuration option. Once compiled in, fetchmail will always use the socks libraries and configuration on your system, there are no run-time switches in fetchmail - but you can still configure SOCKS: you can specify which SOCKS configuration file is used in the <code>SOCKS_CONF</code> environment variable. </p>
<p> For instance, if you wanted to bypass the SOCKS proxy altogether and have fetchmail connect directly, you could just pass SOCKS_CONF=/dev/null in the environment, for example (add your usual command line options - if any - to the end of this line): </p>
<pre><code>env SOCKS_CONF=/dev/null fetchmail
</code></pre>
<h2>EXIT CODES</h2>
<p> To facilitate the use of <code>fetchmail</code> in shell scripts, an exit status code is returned to give an indication of what occurred during a given connection. </p>
<p> The exit codes returned by <code>fetchmail</code> are as follows: </p>
<dl>
<dt>0</dt>
<dd> <p> One or more messages were successfully retrieved (or, if the -c option was selected, were found waiting but not retrieved). </p>
 </dd>
<dt>1</dt>
<dd> <p> There was no mail awaiting retrieval. (There may have been old mail still on the server but not selected for retrieval.) If you do not want &quot;no mail&quot; to be an error condition (for instance, for cron jobs), use a POSIX-compliant shell and add </p>
<pre><code>|| [ $? -eq 1 ]
</code></pre>
<p> to the end of the fetchmail command line, note that this leaves 0 untouched, maps 1 to 0, and maps all other codes to 1. See also item #C8 in the FAQ. </p>
 </dd>
<dt>2</dt>
<dd> <p> An error was encountered when attempting to open a socket to retrieve mail. If you don&#8217;t know what a socket is, don&#8217;t worry about it -- just treat this as an &#8216;unrecoverable error&#8217;. This error can also be because a protocol fetchmail wants to use is not listed in /etc/services. </p>
 </dd>
<dt>3</dt>
<dd> <p> The user authentication step failed. This usually means that a bad user-id, password, or APOP id was specified. Or it may mean that you tried to run fetchmail under circumstances where it did not have standard input attached to a terminal and could not prompt for a missing password. </p>
 </dd>
<dt>4</dt>
<dd> <p> Some sort of fatal protocol error was detected. </p>
 </dd>
<dt>5</dt>
<dd> <p> There was a syntax error in the arguments to <code>fetchmail</code>, or a pre- or post-connect command failed. </p>
 </dd>
<dt>6</dt>
<dd> <p> The run control file had bad permissions. </p>
 </dd>
<dt>7</dt>
<dd> <p> There was an error condition reported by the server. Can also fire if <code>fetchmail</code> timed out while waiting for the server. </p>
 </dd>
<dt>8</dt>
<dd> <p> Client-side exclusion error. This means <code>fetchmail</code> either found another copy of itself already running, or failed in such a way that it isn&#8217;t sure whether another copy is running. </p>
 </dd>
<dt>9</dt>
<dd> <p> The user authentication step failed because the server responded &quot;lock busy&quot;. Try again after a brief pause! This error is not implemented for all protocols, nor for all servers. If not implemented for your server, &quot;3&quot; will be returned instead, see above. May be returned when talking to qpopper or other servers that can respond with &quot;lock busy&quot; or some similar text containing the word &quot;lock&quot;. </p>
 </dd>
<dt>10</dt>
<dd> <p> The <code>fetchmail</code> run failed while trying to do an SMTP port open or transaction. </p>
 </dd>
<dt>11</dt>
<dd> <p> Fatal DNS error. Fetchmail encountered an error while performing a DNS lookup at startup and could not proceed. </p>
 </dd>
<dt>12</dt>
<dd> <p> BSMTP batch file could not be opened. </p>
 </dd>
<dt>13</dt>
<dd> <p> Poll terminated by a fetch limit (see the --fetchlimit option). </p>
 </dd>
<dt>14</dt>
<dd> <p> Server busy indication. </p>
 </dd>
<dt>23</dt>
<dd> <p> Internal error. You should see a message on standard error with details. </p>
 </dd>
<dt>24 - 26, 28, 29</dt>
<dd> <p> These are internal codes and should not appear externally. </p>
 </dd></dl>
<p> When <code>fetchmail</code> queries more than one host, return status is 0 if <i>any</i> query successfully retrieved mail. Otherwise the returned error status is that of the last host queried. </p>
<h2>FILES</h2>
<dl>
<dt>~/.fetchmailrc, $HOME/.fetchmailrc, $HOME_ETC/.fetchmailrc, $FETCHMAILHOME/fetchmailrc</dt>
<dd> <p> default run control file (location can be overridden with environment variables) </p>
 </dd>
<dt>~/.fetchids, $HOME/.fetchids, $HOME_ETC/.fetchids, $FETCHMAILHOME/.fetchids</dt>
<dd> <p> default location of file recording last message UIDs seen per host. (location can be overridden with environment variables) </p>
 </dd>
<dt>~/.fetchmail.pid, $HOME/.fetchmail.pid, $HOME_ETC/.fetchmail.pid, $FETCHMAILHOME/fetchmail.pid</dt>
<dd> <p> default location of lock file to help prevent concurrent runs (non-root mode). (location can be overridden with environment variables) </p>
 </dd>
<dt>~/.netrc, $HOME/.netrc, $HOME_ETC/.netrc</dt>
<dd> <p> your FTP run control file, which (if present) will be searched for passwords as a last resort before prompting for one interactively. (location can be overridden with environment variables) </p>
 </dd>
<dt>/var/run/fetchmail.pid</dt>
<dd> <p> lock file to help prevent concurrent runs (root mode, Linux systems). </p>
 </dd>
<dt>/etc/fetchmail.pid</dt>
<dd> <p> lock file to help prevent concurrent runs (root mode, systems without /var/run). </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FETCHMAILHOME</code></dt>
<dd> <p> If this environment variable is set to a valid and existing directory name, fetchmail will read $FETCHMAILHOME/fetchmailrc (the dot is missing in this case), $FETCHMAILHOME/.fetchids (keeping its dot) and $FETCHMAILHOME/fetchmail.pid (without dot) rather than from the user&#8217;s home directory. The .netrc file is always looked for in the the invoking user&#8217;s home directory (or $HOME_ETC) regardless of FETCHMAILHOME&#8217;s setting. </p>
 </dd>
<dt><code>FETCHMAILUSER</code></dt>
<dd> <p> If this environment variable is set, it is used as the name of the calling user (default local name) for purposes such as mailing error notifications. Otherwise, if either the LOGNAME or USER variable is correctly set (e.g. the corresponding UID matches the session user ID) then that name is used as the default local name. Otherwise <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3) must be able to retrieve a password entry for the session ID (this elaborate logic is designed to handle the case of multiple names per userid gracefully). </p>
 </dd>
<dt><code>FETCHMAIL_DISABLE_CBC_IV_COUNTERMEASURE</code></dt>
<dd> <p> (since v6.3.22): If this environment variable is set and not empty, fetchmail will disable a countermeasure against an SSL CBC IV attack (by setting SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS). This is a security risk, but may be necessary for connecting to certain non-standards-conforming servers. See fetchmail&#8217;s NEWS file and fetchmail-SA-2012-01.txt for details. Earlier fetchmail versions (v6.3.21 and older) used to disable this countermeasure, but v6.3.22 no longer does that as a safety precaution. </p>
 </dd>
<dt><code>FETCHMAIL_POP3_FORCE_RETR</code></dt>
<dd> <p> (since v6.3.9): If this environment variable is defined at all (even if empty), fetchmail will forgo the POP3 TOP command and always use RETR. This can be used as a workaround when TOP does not work properly. </p>
 </dd>
<dt><code>FETCHMAIL_INCLUDE_DEFAULT_X509_CA_CERTS</code></dt>
<dd> <p> (since v6.3.17): If this environment variable is set and not empty, fetchmail will always load the default X.509 trusted certificate locations for SSL/TLS CA certificates, even if <code>--sslcertfile</code> and <code>--sslcertpath</code> are given. The latter locations take precedence over the system default locations. This is useful in case there are broken certificates in the system directories and the user has no administrator privileges to remedy the problem. </p>
 </dd>
<dt><code>HOME</code></dt>
<dd> <p> (documented since 6.4.1): This variable is nomally set to the user&#8217;s home directory. If it is set to a different directory than what is the password database, HOME takes precedence. </p>
 </dd>
<dt><code>HOME_ETC</code></dt>
<dd> <p> (documentation corrected to match behaviour code since 6.4.1): If the HOME_ETC variable is set, it will override fetchmail&#8217;s idea of $HOME, i. e. fetchmail will read .fetchmailrc, .fetchids, .fetchmail.pid and .netrc from $HOME_ETC instead of $HOME (or if HOME is also unset, from the passwd file&#8217;s home directory location). </p>
<p> If HOME_ETC and FETCHMAILHOME are both set, FETCHMAILHOME takes prececence and HOME_ETC will be ignored. </p>
 </dd>
<dt><code>SOCKS_CONF</code></dt>
<dd> <p> (only if SOCKS support is compiled in) this variable is used by the socks library to find out which configuration file it should read. Set this to /dev/null to bypass the SOCKS proxy. </p>
 </dd></dl>
<h2>SIGNALS</h2>
<p> If a <code>fetchmail</code> daemon is running as root, SIGUSR1 wakes it up from its sleep phase and forces a poll of all non-skipped servers. For compatibility reasons, SIGHUP can also be used in 6.3.X but may not be available in future fetchmail versions. </p>
<p> If <code>fetchmail</code> is running in daemon mode as non-root, use SIGUSR1 to wake it (this is so SIGHUP due to logout can retain the default action of killing it). </p>
<p> Running <code>fetchmail</code> in foreground while a background fetchmail is running will do whichever of these is appropriate to wake it up. </p>
<h2>BUGS, LIMITATIONS, AND KNOWN PROBLEMS</h2>
<p> Please check the <code>NEWS</code> file that shipped with fetchmail for more known bugs than those listed here. </p>
<p> Fetchmail cannot handle user names that contain blanks after a &quot;@&quot; character, for instance &quot;demonstr@ti on&quot;. These are rather uncommon and only hurt when using UID-based --keep setups, so the 6.3.X versions of fetchmail won&#8217;t be fixed. </p>
<p> Fetchmail cannot handle configurations where you have multiple accounts that use the same server name and the same login. Any user [at] server combination must be unique. </p>
<p> The assumptions that the DNS and in particular the checkalias options make are not often sustainable. For instance, it has become uncommon for an MX server to be a POP3 or IMAP server at the same time. Therefore the MX lookups may go away in a future release. </p>
<p> The mda and plugin options interact badly. In order to collect error status from the MDA, fetchmail has to change its normal signal handling so that dead plugin processes don&#8217;t get reaped until the end of the poll cycle. This can cause resource starvation if too many zombies accumulate. So either don&#8217;t deliver to a MDA using plugins or risk being overrun by an army of undead. </p>
<p> The --interface option does not support IPv6 and it is doubtful if it ever will, since there is no portable way to query interface IPv6 addresses. </p>
<p> The RFC822 address parser used in multidrop mode chokes on some @-addresses that are technically legal but bizarre. Strange uses of quoting and embedded comments are likely to confuse it. </p>
<p> In a message with multiple envelope headers, only the last one processed will be visible to fetchmail. </p>
<p> Use of some of these protocols requires that the program send unencrypted passwords over the TCP/IP connection to the mailserver. This creates a risk that name/password pairs might be snaffled with a packet sniffer or more sophisticated monitoring software. Under Linux and FreeBSD, the --interface option can be used to restrict polling to availability of a specific interface device with a specific local or remote IP address, but snooping is still possible if (a) either host has a network device that can be opened in promiscuous mode, or (b) the intervening network link can be tapped. We recommend the use of <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) tunnelling to not only shroud your passwords but encrypt the entire conversation. </p>
<p> Use of the %F or %T escapes in an mda option could open a security hole, because they pass text manipulable by an attacker to a shell command. Potential shell characters are replaced by &#8216;_&#8216; before execution. The hole is further reduced by the fact that fetchmail temporarily discards any suid privileges it may have while running the MDA. For maximum safety, however, don&#8217;t use an mda command containing %F or %T when fetchmail is run from the root account itself. </p>
<p> Fetchmail&#8217;s method of sending bounces due to errors or spam-blocking and spam bounces requires that port 25 of localhost be available for sending mail via SMTP. </p>
<p> If you modify <i>~/.fetchmailrc</i> while a background instance is running and break the syntax, the background instance will die silently. Unfortunately, it can&#8217;t die noisily because we don&#8217;t yet know whether syslog should be enabled. On some systems, fetchmail dies quietly even if there is no syntax error; this seems to have something to do with buggy terminal ioctl code in the kernel. </p>
<p> The -f~- option (reading a configuration from stdin) is incompatible with the plugin option. </p>
<p> The &#8216;principal&#8217; option only handles Kerberos IV, not V. </p>
<p> Interactively entered passwords are truncated after 63 characters. If you really need to use a longer password, you will have to use a configuration file. </p>
<p> A backslash as the last character of a configuration file will be flagged as a syntax error rather than ignored. </p>
<p> The BSMTP error handling is virtually nonexistent and may leave broken messages behind. </p>
<p> Send comments, bug reports, gripes, and the like to the </p>
<p> An is available at the fetchmail home page, it should also accompany your installation. </p>
<h2>AUTHOR</h2>
<p> Fetchmail is currently maintained by Matthias Andree and Rob Funk with major assistance from Sunil Shetye (for code) and Rob MacGregor (for the mailing lists). </p>
<p> Most of the code is from . Too many other people to name here have contributed code and patches. </p>
<p> This program is descended from and replaces <code>popclient</code>, by ; the internals have become quite different, but some of its interface design is directly traceable to that ancestral program. </p>
<p> This manual page has been improved by Matthias Andree, R. Hannes Beinert, and H&eacute;ctor Garc&iacute;a. </p>
<h2>SEE ALSO</h2>
<p> <code>README</code>, <code>README.SSL</code>, <code>README.SSL-SERVER</code>, <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code>elm</code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code>sendmail</code>(8), <code>popd</code>(8), <code>imapd</code>(8), <code><a href="/docs/linux/man/5-netrc/">netrc</a></code>(5). </p>
<h2>APPLICABLE STANDARDS</h2>
<p> Note that this list is just a collection of references and not a statement as to the actual protocol conformance or requirements in fetchmail. </p>
<dl>
<dt>SMTP/ESMTP:</dt>
<dd> <p> RFC 821, RFC 2821, RFC 1869, RFC 1652, RFC 1870, RFC 1983, RFC 1985, RFC 2554. </p>
 </dd>
<dt>mail:</dt>
<dd> <p> RFC 822, RFC 2822, RFC 1123, RFC 1892, RFC 1894. </p>
 </dd>
<dt>POP2:</dt>
<dd> <p> RFC 937 </p>
 </dd>
<dt>POP3:</dt>
<dd> <p> RFC 1081, RFC 1225, RFC 1460, RFC 1725, RFC 1734, RFC 1939, RFC 1957, RFC 2195, RFC 2449. </p>
 </dd>
<dt>APOP:</dt>
<dd> <p> RFC 1939. </p>
 </dd>
<dt>RPOP:</dt>
<dd> <p> RFC 1081, RFC 1225. </p>
 </dd>
<dt>IMAP2/IMAP2BIS:</dt>
<dd> <p> RFC 1176, RFC 1732. </p>
 </dd>
<dt>IMAP4/IMAP4rev1:</dt>
<dd> <p> RFC 1730, RFC 1731, RFC 1732, RFC 2060, RFC 2061, RFC 2195, RFC 2177, RFC 2683. </p>
 </dd>
<dt>ETRN:</dt>
<dd> <p> RFC 1985. </p>
 </dd>
<dt>ODMR/ATRN:</dt>
<dd> <p> RFC 2645. </p>
 </dd>
<dt>OTP:</dt>
<dd> <p> RFC 1938. </p>
 </dd>
<dt>LMTP:</dt>
<dd> <p> RFC 2033. </p>
 </dd>
<dt>GSSAPI:</dt>
<dd> <p> RFC 1508, RFC 1734, </p>
 </dd>
<dt>TLS:</dt>
<dd> <p> RFC 2595. </p>
 </dd></dl>
