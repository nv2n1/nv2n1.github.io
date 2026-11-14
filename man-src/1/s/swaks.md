---
title: "swaks(1)"
name: "swaks"
section: "1"
letter: "s"
url: "/docs/linux/man/1-swaks/"
---

<h2 class="name">NAME</h2>
 

 swaks - Swiss Army Knife SMTP, the all-purpose smtp transaction tester 

<h2>DESCRIPTION</h2>

 swaks' primary design goal is to be a flexible, scriptable, transaction-oriented <font SIZE="-1">SMTP</font> test tool. It handles <font SIZE="-1">SMTP</font> features and extensions such as <font SIZE="-1">TLS,</font> authentication, and pipelining; multiple version of the <font SIZE="-1">SMTP</font> protocol including <font SIZE="-1">SMTP, ESMTP,</font> and <font SIZE="-1">LMTP</font>; and multiple transport methods including unix-domain sockets, internet-domain sockets, and pipes to spawned processes. Options can be specified in environment variables, configuration files, and the command line allowing maximum configurability and ease of use for operators and scripters.

<h2>QUICK START</h2>

 Deliver a standard test email to user [at] example.com on port 25 of test-server.example.net: 

 <pre><code>
swaks-- to user[at] example.com-- server test - server.example.net
</code></pre> 

 Deliver a standard test email, requiring <font SIZE="-1">CRAM-MD5</font> authentication as user me [at] example.com. An ``X-Test'' header will be added to the email body. The authentication password will be prompted for. 

 
swaks-- to user[at] example.com-- from me[at] example.com-- auth CRAM - MD5-- auth - user me[at] example.com-- header - X - Test "test email"
 

 Test a virus scanner using <font SIZE="-1">EICAR</font> in an attachment. Don't show the message <font SIZE="-1">DATA</font> part.: 

 
swaks - t user[at] example.com-- attach - --server test - server.example.com-- suppress - data &lt; / path / to / eicar.txt
 

 Test a spam scanner using <font SIZE="-1">GTUBE</font> in the body of an email, routed via the <font SIZE="-1">MX</font> records for example.com: 

 
swaks-- to user[at] example.com-- body / path / to / gtube / file
 

 Deliver a standard test email to user [at] example.com using the <font SIZE="-1">LMTP</font> protocol via a <font SIZE="-1">UNIX</font> domain socket file 

 
swaks-- to user[at] example.com-- socket / var / lda.sock-- protocol LMTP
 

 Report all the recipients in a text file that are non-verifyiable on a test server: 

 
 for E in `cat /path/to/email/file`
 do
     swaks --to $E --server test-server.example.com --quit-after RCPT --hide-all
     [ $? -ne 0 ] &amp;&amp; echo $E
 done


<h2>TERMS AND CONVENTIONS</h2>

 This document tries to be consistent and specific in its use of the following terms to reduce confusion.
<dl>
<dt>Transaction
<dd> A transaction is the opening of a connection over a transport to a target and using a messaging protocol to attempt to deliver a message.
<dt>Target
<dd> The target of a transaction is the thing that swaks connects to. This generic term is used throughout the documentation because most other terms improperly imply something about the transport being used.
<dt>Transport
<dd> The transport is the underlying method used to connect to the target.
<dt>Protocol
<dd> The protocol is the application language used to communicate with the target. This document uses <font SIZE="-1">SMTP</font> to speak generically of all three supported protocols unless it states that it is speaking of the specific '<font SIZE="-1">SMTP</font>' protocol and excluding the others.
<dt>Message
<dd> <font SIZE="-1">SMTP</font> protocols exist to transfer messages, a set of bytes in an agreed-upon format that has a sender and a recipient.
<dt>Envelope
<dd> A message's envelope contains the ``true'' sender and receiver of a message. It can also be referred to as its components, envelope-sender and envelope-recipients. It is important to note that a messages envelope does not have to match its To: and From: headers.
<dt><font SIZE="-1">DATA</font>
<dd> The <font SIZE="-1">DATA</font> portion of an <font SIZE="-1">SMTP</font> transaction is the actual message that is being transported. It consists of both the message's headers and its body. <font SIZE="-1">DATA</font> and body are sometimes use synonymously, but they are always two distinct things in this document.
<dt>Headers
<dd> A message's headers are defined as all the lines in the message's <font SIZE="-1">DATA</font> section before the first blank line. They contain information about the email that will be displayed to the recipient such as To:, From:, Subject:, etc. In this document headers will always be written with a capitalized first letter and a trailing colon.
<dt>Body
<dd> A message's body is the portion of its <font SIZE="-1">DATA</font> section following the first blank line.</dl>

<h2>OPTION PROCESSING</h2>

 To prevent potential confusion in this document a flag to swaks is always referred to as an ``option''. If the option takes additional data, that additional data is referred to as an argument to the option. For example, ``--from fred [at] example.com'' might be provided to swaks on the command line, with ``--from'' being the option and ``fred [at] example.com'' being --from's argument. 

 Options can be given to swaks in three ways. They can be specified in a configuration file, in environment variables, and on the command line. Depending on the specific option and whether or not an argument is given to it, swaks may prompt the user for the argument. 

 When swaks evaluates its options, it first looks for a configuration file (either in a default location or specified with --config). Then it evaluates any options in environment variables. Finally, it evaluates command line options. At each round of processing, any options set earlier will be overridden. Additionally, any option can be prefixed with ``no-'' to cause swaks to forget that the variable had previously been set. This capability is necessary because many options treat defined-but-no-argument differently than not-defined. 

 The exact mechanism and format for using each of the types is listed below.
<dl>
<dt><font SIZE="-1">CONFIGURATION FILE</font>
<dd> A configuration file can be used to set commonly-used or abnormally verbose options. By default swaks looks in order for <tt>$SWAKS_HOME</tt>/.swaksrc, <tt>$HOME</tt>/.swaksrc, and <tt>$LOGDIR</tt>/.swaksrc. If one of those is found to exist (and --config has not been used) that file is used as the configuration file. 

 Additionally a configuration file in a non-default location can be specified using --config. If this is set and not given an argument swaks will not use any configuration file, including any default file. If --config points to a readable file, it is used as the configuration file, overriding any default that may exist. If it points to a non-readable file and error will be shown and swaks will exit. 

 A set of ``portable'' defaults can also be created by adding options to the end of the swaks program file. As distributed, the last line of swaks should be ``__END__''. Any lines added after __END__ will be treated as the contents of a configuration file. This allows a set of user preferences to be automatically copied from server to server in a single file. 

 If present and configuration files have not been explicitly turned off, the __END__ config is always read. Only one other configuration file will ever be used per single invocation of swaks, even if multiple configuration files are specified. Specifying the --config option with no argument turns off the processing of both the __END__ config and any actual config files. 

 In a configuration file lines beginning with a hash (#) are ignored. All other lines are assumed to be an option to swaks, with the leading dash or dashes optional. Everything after a option line's first space is assumed to be the option's argument and is not shell processed. Therefore quoting is usually unneeded and will be included literally in the argument. Here is an example of the contents of a configuration file: 

 
#always use this sender, no matter server or logged in user
--from fred[at] example.com
#I prefer my test emails have a pretty from header.Note
#the lack of dashes on option and lack of quotes around
#entire argument.
            h -
        From : "Fred Example" &lt;
    fred[at] example.com &gt;

<dt><font SIZE="-1">ENVIRONMENT VARIABLES</font>
<dd> Options can be supplied via environment variables. The variables are in the form <tt>$SWAKS_OPT_name</tt>, where name is the name of the option that would be specified on the command line. Because dashes aren't allowed in environment variable names in most unix-ish shells, no leading dashes should be used and any dashes inside the option's name should be replaced with underscores. The following would create the same options shown in the configuration file example: 

 
$ SWAKS_OPT_from = 'fred [at] example.com' $ SWAKS_OPT_h_From = '"Fred Example" &lt;fred [at] example.com&gt;'
 

 Setting a variable to an empty value is the same as specifying it on the command line with no argument. For instance, setting SWAKS_OPT_server=&quot;&quot; would cause swaks to prompt the use for the server to which to connect at each invocation. 

 In addition to setting the equivalent of command line options, <font SIZE="-1">SWAKS_HOME</font> can be set to a directory containing the default .swaksrc to be used.
<dt><font SIZE="-1">COMMAND LINE OPTIONS</font>
<dd> The final method of supplying options to swaks is via the command line. The options behave in a manner consistent with most unix-ish command line programs. Many options have both a short and long form (for instance -s and --server). By convention short options are specified with a single dash and long options are specified with a double-dash. This is only a convention and either prefix will work with either type. 

 The following demonstrates the example shown in the configuration file and environment variable sections: 

 <pre><code>
$ swaks-- from fred[at] example.com-- h - From : '"Fred Example" &lt;fred [at] example.com&gt;'
</code></pre></dl>

<h2>TRANSPORTS</h2>

 swaks can connect to a target via unix pipes (``pipes''), unix domain sockets (``unix sockets''), or internet domain sockets (``network sockets''). Connecting via network sockets is the default behavior. Because of the singular nature of the transport used, each set of options in the following section is mutually exclusive. Specifying more than one of --server, --pipe, or --socket will result in an error. Mixing other options between transport types will only result in the irrelevant options being ignored. Below is a brief description of each type of transport and the options that are specific to that transport type.
<dl>
<dt><font SIZE="-1">NETWORK SOCKETS</font>
<dd> This transport attempts to deliver a message via <font SIZE="-1">TCP/IP,</font> the standard method for delivering <font SIZE="-1">SMTP. </font> This is the default transport for swaks. If none of --server, --pipe, or --socket are given then this transport is used and the target server is determined from the recipient's domain (see --server below for more details). 

 This transport requires the IO::Socket module which is part of the standard perl distribution. If this module is not loadable, attempting to use a this transport will result in an error and program termination. 

 IPv6 is supported when the IO::Socket::INET6 module is present.
<dl>
<dt>
<dd>
<dl>
<dt>-s, --server [target mail server[:port]]
<dd> Explicitly tell swaks to use network sockets and specify the hostname or <font SIZE="-1">IP</font> address to which to connect, or prompt if no argument is given. If this option is not given and no other transport option is given, the target mail server is determined from the appropriate <font SIZE="-1">DNS</font> records for the domain of the recipient email address using the Net::DNS module. If Net::DNS is not available swaks will attempt to connect to localhost to deliver. The target port can optionally be set here. Supported formats for this include <font SIZE="-1">SERVER:PORT </font>(supporting names and IPv4 addresses); [<font SIZE="-1">SERVER</font>]:PORT and <font SIZE="-1">SERVER/PORT </font>(supporting names, IPv4 and IPv6 addresses). See also --copy-routing.
<dt>-p, --port [port]
<dd> Specify which <font SIZE="-1">TCP</font> port on the target is to be used, or prompt if no argument is listed. The argument can be a service name (as retrieved by <i><a HREF="/docs/linux/man/3-getservbyname/">getservbyname</a></i>(3)) or a port number. The default port is determined by the --protocol option. See --protocol for more details.
<dt>-li, --local-interface [<font SIZE="-1">IP</font> or hostname[:port]]
<dd> Use argument as the local interface for the outgoing <font SIZE="-1">SMTP</font> connection, or prompt user if no argument given. Argument can be an <font SIZE="-1">IP</font> address or a hostname. Default action is to let the operating system choose local interface. See --server for additional comments on :port format.
<dt>-lp, --local-port [port]
<dd> Specify the outgoing port to originate the transaction from. If this option is not specified the system will pick an ephemeral port. Note that regular users cannot specify some ports.
<dt>--copy-routing [domain]
<dd> The argument is interpreted as the domain part of an email address and it is used to find the target server using the same logic that would be used to look up the target server for a recipient email address. See --to option for more details on how the target is determined from the email domain.
<dt>-4, -6
<dd> Force IPv4 or IPv6.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt><font SIZE="-1">UNIX SOCKETS</font>
<dd> This transport method attempts to deliver messages via a unix-domain socket file. This is useful for testing MTA/MDAs that listen on socket files (for instance, testing <font SIZE="-1">LMTP</font> delivery to Cyrus). This transport requires the IO::Socket module which is part of the standard perl distribution. If this module is not loadable, attempting to use this transport will result in an error and program termination.
<dl>
<dt>
<dd>
<dl>
<dt>--socket [/path/to/socket/file]
<dd> This option takes as its argument a unix-domain socket file. If swaks is unable to open this socket it will display an error and exit.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt><font SIZE="-1">PIPES</font>
<dd> This transport attempts to spawn a process and communicate with it via pipes. The spawned program must be prepared to behave as a mail server over <font SIZE="-1">STDIN/STDOUT. </font> Any <font SIZE="-1">MTA</font> designed to operate from inet/xinet should support this. In addition some MTAs provide testing modes that can be communicated with via <font SIZE="-1">STDIN/STDOUT. </font> This transport can be used to automate that testing. For example, if you implemented <font SIZE="-1">DNSBL</font> checking with Exim and you wanted to make sure it was working, you could run 'swaks --pipe ``exim -bh 127.0.0.2'''. In an ideal world the process you are talking to should behave exactly like an <font SIZE="-1">SMTP</font> server on stdin and stdout. Any debugging should be sent to stderr, which will be directed to your terminal. In the real world swaks can generally handle some debug on the child's stdout, but there are no guarantees on how much it can handle. 

 This transport requires the IPC::Open2 module which is part of the standard perl distribution. If this module is not loadable, attempting to use this transport will result in an error and program termination.
<dl>
<dt>
<dd>
<dl>
<dt>--pipe [/path/to/command and arguments]
<dd> Provide a process name and arguments to the process. swaks will attempt to spawn the process and communicate with it via pipes. If the argument is not an executable swaks will display an error and exit.</dl>
</dl>

<dl>
<dt>
<dd></dl>
</dl>

<h2>PROTOCOL OPTIONS</h2>

 These options are related to the protocol layer.
<dl>
<dt>-t, --to [email-address[,email-address,...]]
<dd> Tells swaks to use argument(s) as the envelope-recipient for the email, or prompt for recipient if no argument provided. If multiple recipients are provided and the recipient domain is needed to determine routing the domain of the last recipient provided is used. 

 There is no default value for this option. If no recipients are provided via any means, user will be prompted to provide one interactively. The only exception to this is if a --quit-after value is provided which will cause the smtp transaction to be terminated before the recipient is needed.
<dt>-f, --from [email-address]
<dd> Use argument as envelope-sender for email, or prompt user if no argument specified. The string &lt;&gt; can be supplied to mean the null sender. If user does not specify a sender address a default value is used. The domain-part of the default sender is a best guess at the fully-qualified domain name of the local host. The method of determining the local-part varies. On Windows, <i>Win32::LoginName()</i> is used. On unix-ish platforms, the <tt>$LOGNAME</tt> environment variable is used if it is set. Otherwise <i><a HREF="/docs/linux/man/3-getpwuid/">getpwuid</a></i>(3) is used. See also --force-getpwuid.
<dt>--ehlo, --lhlo, -h, --helo [helo-string]
<dd> String to use as argument to <font SIZE="-1">HELO/EHLO/LHLO</font> command, or prompt use if no argument is specified. If this option is not used a best guess at the fully-qualified domain name of the local host is used. If the Sys::Hostname module, which is part of the base distribution, is not available the user will be prompted for a <font SIZE="-1">HELO</font> value. Note that Sys::Hostname has been observed to not be able to find the local hostname in certain circumstances. This has the same effect as if Sys::Hostname were unavailable.
<dt>-q, --quit, --quit-after [stop-point]
<dd> Point at which the transaction should be stopped. When the requested stopping point is reached in the transaction, and provided that swaks has not errored out prior to reaching it, swaks will send ``<font SIZE="-1">QUIT''</font> and attempt to close the connection cleanly. These are the valid arguments and notes about their meaning.
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">CONNECT, BANNER</font>
<dd> Terminate the session after receiving the greeting banner from the target.
<dt>FIRST-HELO, FIRST-EHLO, FIRST-LHLO
<dd> In a <font SIZE="-1">STARTTLS </font>(but not tls-on-connect) session, terminate the transaction after the first of two HELOs. In a non-STARTTLS transaction, behaves the same as <font SIZE="-1">HELO </font>(see below).
<dt><font SIZE="-1">XCLIENT</font>
<dd> Quit after <font SIZE="-1">XCLIENT</font> is sent
<dt><font SIZE="-1">TLS</font>
<dd> Quit the transaction immediately following <font SIZE="-1">TLS</font> negotiation. Note that this happens in different places depending on whether <font SIZE="-1">STARTTLS</font> or tls-on-connect are used. This always quits after the point where <font SIZE="-1">TLS</font> would have been negotiated, regardless of whether it was attempted.
<dt><font SIZE="-1">HELO, EHLO, LHLO</font>
<dd> In a <font SIZE="-1">STARTTLS</font> or <font SIZE="-1">XCLIENT</font> session, quit after the second <font SIZE="-1">HELO. </font> Otherwise quit after the first and only <font SIZE="-1">HELO.</font>
<dt><font SIZE="-1">AUTH</font>
<dd> Quit after authentication. This always quits after the point where authentication would have been negotiated, regardless of whether it was attempted.
<dt><font SIZE="-1">MAIL, FROM</font>
<dd> Quit after <font SIZE="-1">MAIL FROM:</font> is sent.
<dt><font SIZE="-1">RCPT, TO</font>
<dd> Quit after <font SIZE="-1">RCPT TO:</font> is sent.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>--da, --drop-after [stop-point]
<dd> The option is similar to --quit-after, but instead of trying to cleanly shut down the session it simply terminates the session. This option accepts the same stop-points as --quit-after.
<dt>--das, --drop-after-send
<dd> This option is similar to --drop-after, but instead of dropping the connection after reading a response to the stop-point, it drops the connection immediately after sending stop-point.
<dt>--timeout [time]
<dd> Use argument as the <font SIZE="-1">SMTP</font> transaction timeout, or prompt user if no argument given. Argument can either be a pure digit, which will be interpretted as seconds, or can have a specifier s or m (5s = 5 seconds, 3m = 180 seconds). As a special case, 0 means don't timeout the transactions. Default value is 30s.
<dt>--protocol [protocol]
<dd> Specify which protocol to use in the transaction. Valid options are shown in the table below. Currently the 'core' protocols are <font SIZE="-1">SMTP, ESMTP,</font> and <font SIZE="-1">LMTP. </font> By using variations of these protocol types one can tersely specify default ports, whether authentication should be attempted, and the type of <font SIZE="-1">TLS</font> connection that should be attempted. The default protocol is <font SIZE="-1">ESMTP. </font> This table demonstrates the available arguments to --protocol and the options each sets as a side effect:
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">SMTP</font>
<dd> <font SIZE="-1">HELO, </font>``-p 25''
<dt><font SIZE="-1">SSMTP</font>
<dd> <font SIZE="-1">EHLO-</font>&gt;<font SIZE="-1">HELO, </font>``-tlsc -p 465''
<dt><font SIZE="-1">SSMTPA</font>
<dd> <font SIZE="-1">EHLO-</font>&gt;<font SIZE="-1">HELO, </font>``-a -tlsc -p 465''
<dt><font SIZE="-1">SMTPS</font>
<dd> <font SIZE="-1">HELO, </font>``-tlsc -p 465''
<dt><font SIZE="-1">ESMTP</font>
<dd> <font SIZE="-1">EHLO-</font>&gt;<font SIZE="-1">HELO, </font>``-p 25''
<dt><font SIZE="-1">ESMTPA</font>
<dd> <font SIZE="-1">EHLO-</font>&gt;<font SIZE="-1">HELO, </font>``-a -p 25''
<dt><font SIZE="-1">ESMTPS</font>
<dd> <font SIZE="-1">EHLO-</font>&gt;<font SIZE="-1">HELO, </font>``-tls -p 25''
<dt><font SIZE="-1">ESMTPSA</font>
<dd> <font SIZE="-1">EHLO-</font>&gt;<font SIZE="-1">HELO, </font>``-a -tls -p 25''
<dt><font SIZE="-1">LMTP</font>
<dd> <font SIZE="-1">LHLO, </font>``-p 24''
<dt><font SIZE="-1">LMTPA</font>
<dd> <font SIZE="-1">LHLO, </font>``-a -p 24''
<dt><font SIZE="-1">LMTPS</font>
<dd> <font SIZE="-1">LHLO, </font>``-tls -p 24''
<dt><font SIZE="-1">LMTPSA</font>
<dd> <font SIZE="-1">LHLO, </font>``-a -tls -p 24''</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>--pipeline
<dd> If the remote server supports it, attempt <font SIZE="-1">SMTP PIPELINING </font>(<font SIZE="-1">RFC 2920</font>).
<dt>--prdr
<dd> If the server supports it, attempt Per-Recipient Data Response (<font SIZE="-1">PRDR</font>) (<a rel="nofollow" HREF="https://tools.ietf.org/html/draft-hall-prdr-00.txt">https://tools.ietf.org/html/draft-hall-prdr-00.txt</a>). <font SIZE="-1">PRDR</font> is not yet standardized, but MTAs have begun implementing the proposal.
<dt>--force-getpwuid
<dd> Tell swaks to use the getpwuid method of finding the default sender local-part instead of trying <tt>$LOGNAME</tt> first.</dl>

<h2>TLS / ENCRYPTION</h2>

 These are options related to encrypting the transaction. These have been tested and confirmed to work with all three transport methods. The Net::SSLeay module is used to perform encryption when it is requested. If this module is not loadable swaks will either ignore the <font SIZE="-1">TLS</font> request or error out, depending on whether the request was optional. <font SIZE="-1">STARTTLS</font> is defined as an extension in the <font SIZE="-1">ESMTP</font> protocol and will be unavailable if --protocol is set to a variation of smtp. Because it is not defined in the protocol itself, --tls-on-connect is available for any protocol type if the target supports it. 

 A local certificate is not required for a <font SIZE="-1">TLS</font> connection to be negotiated. However, some servers use client certificate checking to verify that the client is allowed to connect. swaks can be told to use a specific local certificate through the use of the --tls-cert and --tls-key options.
<dl>
<dt>-tls
<dd> Require connection to use <font SIZE="-1">STARTTLS. </font> Exit if <font SIZE="-1">TLS</font> not available for any reason (not advertised, negotiations failed, etc).
<dt>-tlso, --tls-optional
<dd> Attempt to use <font SIZE="-1">STARTTLS</font> if available, continue with normal transaction if <font SIZE="-1">TLS</font> was unable to be negotiated for any reason. Note that this is a semi-useless option as currently implemented because after a negotiation failure the state of the connection is unknown. In some cases, like a version mismatch, the connection should be left as plaintext. In others, like a verification failure, the server-side may think that it should continue speaking <font SIZE="-1">TLS</font> while the client thinks it is plaintext. There may be an attempt to add more granular state detection in the future, but for now just be aware that odd things may happen with this option if the <font SIZE="-1">TLS</font> negotiation is attempted and fails.
<dt>-tlsos, --tls-optional-strict
<dd> Attempt to use <font SIZE="-1">STARTTLS</font> if available. Proceed with transaction if <font SIZE="-1">TLS</font> is negotiated successfully or <font SIZE="-1">STARTTLS</font> not advertised. If <font SIZE="-1">STARTTLS</font> is advertised but <font SIZE="-1">TLS</font> negotiations fail, treat as an error and abort transaction. Due to the caveat noted above, this is a much more sane option than --tls-optional.
<dt>--tlsc, --tls-on-connect
<dd> Initiate a <font SIZE="-1">TLS</font> connection immediately on connection. Following common convention, if this option is specified the default port changes from 25 to 465, though this can still be overridden with the --port option.
<dt>-tlsp, --tls-protocol <font SIZE="-1">SPECIFICATION</font>
<dd> Specify which protocols to use (or not use) when negotiating <font SIZE="-1">TLS. </font> At the time of this writing, the available protocols are sslv2, sslv3, tlsv1, tlsv1_1, and tlsv1_2. The availability of these protocols is dependent on your underlying OpenSSL library, so not all of these may be available. The list of available protocols is shown in the output of --dump (assuming <font SIZE="-1">TLS</font> is available at all). 

 The specification string is a comma-delimited list of protocols that can be used or not used. For instance 'tlsv1,tlsv1_1' will only succeed if one of those two protocols is available on both the client and the server. Conversely, 'no_sslv2,no_sslv3' will attempt to negotiate any protocol except sslv2 and sslv3. The two forms of specification cannot be mixed.
<dt>-tls-cipher <font SIZE="-1">CIPHER_STRING</font>
<dd> Th argument to this option is passed to the underlying OpenSSL library to set the list of acceptable ciphers to the be used for the connection. The format of this string is opaque to swaks and is defined in <a rel="nofollow" HREF="http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT.">http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT.</a> A brief example would be --tls-cipher '3DES:+RSA'.
<dt>--tls-verify
<dd> By default swaks does not do any certificate verification. Setting --tls-verify will cause swaks to attempt to verify the server's certificate. If this option is set and the server's certificate is not verifiable (either using the system-default <font SIZE="-1">CA</font> information, or custom <font SIZE="-1">CA</font> information (see --tls-ca-path)) <font SIZE="-1">TLS</font> negotiation will not succeed.
<dt>--tls-ca-path [ /path/to/CAfile | /path/to/CAdir/ ]
<dd> By default swaks will use the underlying OpenSSL library's default <font SIZE="-1">CA</font> information for verifying server certificates. --tls-ca-path allows you to specify an alternate location. See <a rel="nofollow" HREF="http://www.openssl.org/docs/ssl/SSL_CTX_load_verify_locations.html">http://www.openssl.org/docs/ssl/SSL_CTX_load_verify_locations.html</a> for details of the file/directory contents.
<dt>--tls-cert /path/to/file
<dd> Provide a path to a file containing the local certificate swaks should use if <font SIZE="-1">TLS</font> is negotiated. The file path argument is required. As currently implemented the certificate in the file must be in <font SIZE="-1">PEM</font> format. Contact the author if there's a compelling need for <font SIZE="-1">ASN1. </font> If this option is set, --tls-key is also required.
<dt>--tls-key /path/to/file
<dd> Provide a path to a file containing the local private key swaks should use if <font SIZE="-1">TLS</font> is negotiated. The file path argument is required. As currently implemented the certificate in the file must be in <font SIZE="-1">PEM</font> format. Contact the author if there's a compelling need for <font SIZE="-1">ASN1. </font> If this option is set, --tls-cert is also required.
<dt>--tls-get-peer-cert [/path/to/file]
<dd> Get a copy of the <font SIZE="-1">TLS</font> peer's certificate. If no argument is given, it will be displayed to <font SIZE="-1">STDOUT. </font> If an argument is given it is assumed to be a filesystem path specifying where the certificate should be written. The saved certificate can then be examined using standard tools such as the openssl command. If a file is specified its contents will be overwritten.</dl>

<h2>AUTHENTICATION</h2>

 swaks will attempt to authenticate to the target mail server if instructed to do so. This section details available authentication types, requirements, options and their interactions, and other fine points in authentication usage. Because authentication is defined as an extension in the <font SIZE="-1">ESMTP</font> protocol it will be unavailable if --protocol is set to a variation of smtp. 

 All authentication methods require base64 encoding. If the MIME::Base64 perl module is loadable swaks attempts to use it to perform these encodings. If MIME::Base64 is not available swaks will use its own onboard base64 routines. These are slower than the MIME::Base64 routines and less reviewed, though they have been tested thoroughly. Using the MIME::Base64 module is encouraged. 

 If authentication is required (see options below for when it is and isn't required) and the requirements aren't met for the authentication type available, swaks displays an error and exits. Two ways this can happen include forcing swaks to use a specific authentication type that swaks can't use due to missing requirements, or allowing swaks to use any authentication type, but the server only advertises types swaks can't support. In the former case swaks errors out at option processing time since it knows up front it won't be able to authenticate. In the latter case swaks will error out at the authentication stage of the smtp transaction since swaks will not be aware that it will not be able to authenticate until that point. 

 Following are the supported authentication types including any individual notes and requirements. 

 The following options affect swaks' use of authentication. These options are all inter-related. For instance, specifying --auth-user implies --auth and --auth-password. Specifying --auth-optional implies --auth-user and --auth-password, etc.
<dl>
<dt>-a, --auth [auth-type[,auth-type,...]]
<dd> Require swaks to authenticate. If no argument is given, any supported auth-types advertised by the server are tried until one succeeds or all fail. If one or more auth-types are specified as an argument, each that the server also supports is tried in order until one succeeds or all fail. This option requires swaks to authenticate, so if no common auth-types are found or no credentials succeed, swaks displays an error and exits. 

 The following tables lists the valid auth-types
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">LOGIN, PLAIN</font>
<dd> These basic authentication types are fully supported and tested and have no additional requirements
<dt><font SIZE="-1">CRAM-MD5</font>
<dd> The <font SIZE="-1">CRAM-MD5</font> authenticator requires the Digest::MD5 module. It is fully tested and believed to work against any server that implements it.
<dt><font SIZE="-1">DIGEST-MD5</font>
<dd> The <font SIZE="-1">DIGEST-MD5</font> authenticator (<font SIZE="-1">RFC2831</font>) requires the Authen::SASL module. Version 20100211.0 and earlier used Authen::DigestMD5 which had some protocol level errors which prevented it from working with some servers. Authen::SASL's <font SIZE="-1">DIGEST-MD5</font> handling is much more robust. 

 The <font SIZE="-1">DIGEST-MD5</font> implementation in swaks is fairly immature. It currently supports only the ``auth'' qop type, for instance. If you have <font SIZE="-1">DIGEST-MD5</font> experience and would like to help swaks support <font SIZE="-1">DIGEST-MD5</font> better, please get in touch with me. 

 The <font SIZE="-1">DIGEST-MD5</font> protocol's ``realm'' value can be set using the --auth-extra ``realm'' keyword. If no realm is given, a reasonable default will be used. 

 The <font SIZE="-1">DIGEST-MD5</font> protocol's ``digest-uri'' values can be set using the --auth-extra option. For instance, you could create the digest-uri-value of ``lmtp/mail.example.com/example.com'' with the option ``--auth-extra dmd5-serv-type=lmtp,dmd5-host=mail.example.com,dmd5-serv-name=example.com''. The ``digest-uri-value'' string and its components is defined in <font SIZE="-1">RFC2831. </font> If none of these values are given, reasonable defaults will be used.
<dt><font SIZE="-1">CRAM-SHA1</font>
<dd> The <font SIZE="-1">CRAM-SHA1</font> authenticator requires the Digest::SHA module. This type has only been tested against a non-standard implementation on an Exim server and may therefore have some implementation deficiencies.
<dt><font SIZE="-1">NTLM/SPA/MSN</font>
<dd> These authenticators require the Authen::NTLM module. Note that there are two modules using the Authen::NTLM namespace on <font SIZE="-1">CPAN. </font> The Mark Bush implementation (Authen/NTLM-1.03.tar.gz) is the version required by swaks. This type has been tested against Exim, Communigate, and Exchange 2007. 

 In addition to the standard username and password, this authentication type can also recognize a ``domain''. The domain can be set using the --auth-extra ``domain'' keyword. Note that this has never been tested with a mail server that doesn't ignore <font SIZE="-1">DOMAIN</font> so this may be implemented incorrectly.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>-ao, --auth-optional [auth-type[,auth-type,...]]
<dd> This option behaves identically to --auth except that it requests authentication rather than requiring it. If no common auth-types are found or no credentials succeed, swaks proceeds as if authentication had not been requested.
<dt>-aos, --auth-optional-strict [auth-type[,auth-type,...]]
<dd> This option is a compromise between --auth and --auth-optional. If no common auth-types are found, swaks behaves as if --auth-optional were specified and proceeds with the transaction. If swaks can't support requested auth-type, the server doesn't advertise any common auth-types, or if no credentials succeed, swaks behaves as if --auth were used and exits with an error.
<dt>-au, --auth-user [username]
<dd> Provide the username to be used for authentication, or prompt the user for it if no argument is provided. The string &lt;&gt; can be supplied to mean an empty username.
<dt>-ap, --auth-password [password]
<dd> Provide the password to be used for authentication, or prompt the user for it if no argument is provided. The string &lt;&gt; can be supplied to mean an empty password.
<dt>-ae, --auth-extra [KEYWORD=value[,...]]
<dd> Some of the authentication types allow extra information to be included in the authentication process. Rather than add a new option for every nook and cranny of each authenticator, the --auth-extra option allows this information to be supplied. 

 The following table lists the currently recognized keywords and the authenticators that use them
<dl>
<dt>
<dd>
<dl>
<dt>realm, domain
<dd> The realm and domain keywords are synonymous. Using either will set the ``domain'' option in <font SIZE="-1">NTLM/MSN/SPA</font> and the ``realm'' option in <font SIZE="-1">DIGEST-MD5</font>
<dt>dmd5-serv-type
<dd> The dmd5-serv-type keyword is used by the <font SIZE="-1">DIGEST-MD5</font> authenticator and is used, in part, to build the digest-uri-value string (see <font SIZE="-1">RFC2831</font>)
<dt>dmd5-host
<dd> The dmd5-host keyword is used by the <font SIZE="-1">DIGEST-MD5</font> authenticator and is used, in part, to build the digest-uri-value string (see <font SIZE="-1">RFC2831</font>)
<dt>dmd5-serv-name
<dd> The dmd5-serv-name keyword is used by the <font SIZE="-1">DIGEST-MD5</font> authenticator and is used, in part, to build the digest-uri-value string (see <font SIZE="-1">RFC2831</font>)</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>-am, --auth-map [auth-alias=auth-type[,...]]
<dd> Provides a way to map alternate names onto base authentication types. Useful for any sites that use alternate names for common types. This functionality is actually used internally to map types <font SIZE="-1">SPA</font> and <font SIZE="-1">MSN</font> onto the base type <font SIZE="-1">NTLM. </font> The command line argument to simulate this would be ``--auth-map SPA=NTLM,MSN=NTLM''. All of the auth-types listed above are valid targets for mapping except <font SIZE="-1">SPA</font> and <font SIZE="-1">MSN.</font>
<dt>-apt, --auth-plaintext
<dd> Instead of showing <font SIZE="-1">AUTH</font> strings base64 encoded as they are transmitted, translate them to plaintext before printing on screen.
<dt>-ahp, --auth-hide-password [replacement string]
<dd> If this option is specified, any time a readable password would be printed to the terminal (specifically <font SIZE="-1">AUTH PLAIN</font> and <font SIZE="-1">AUTH LOGIN</font>) the password is replaced with a dummy string (or the contents of ``replacement string'' if provided). The dummy string will be base64 encoded or not contingent on the --auth-plaintext option. 

 Note that --auth-hide-password is similar, but not identical, to the --protect-prompt option. The former protects passwords from being displayed in the <font SIZE="-1">SMTP</font> transaction regardless of how they are entered. The latter protects sensitive strings when the user types them at the terminal, regardless of how the string would be used.</dl>

<h2>XCLIENT OPTIONS</h2>

 <font SIZE="-1">XCLIENT</font> is an <font SIZE="-1">SMTP</font> extension introduced by the Postfix project. <font SIZE="-1">XCLIENT</font> allows a (properly-authorized) client to tell a server to use alternate information, such as <font SIZE="-1">IP</font> address or hostname, for the client. This allows much easier paths for testing mail server configurations. Full details on the protocol are available at <a rel="nofollow" HREF="http://www.postfix.org/XCLIENT_README.html.">http://www.postfix.org/XCLIENT_README.html.</a>
<dl>
<dt>--xclient-addr [<font SIZE="-1">VALUE</font>]
<dd>
<dt>--xclient-name [<font SIZE="-1">VALUE</font>]
<dd>
<dt>--xclient-port [<font SIZE="-1">VALUE</font>]
<dd>
<dt>--xclient-proto [<font SIZE="-1">VALUE</font>]
<dd>
<dt>--xclient-helo [<font SIZE="-1">VALUE</font>]
<dd>
<dt>--xclient-login [<font SIZE="-1">VALUE</font>]
<dd>
<dt>--xclient-reverse-name [<font SIZE="-1">VALUE</font>]
<dd> These options specify <font SIZE="-1">XCLIENT</font> attrubutes that should be sent to the target server. If [<font SIZE="-1">VALUE</font>] is not provided, swaks will prompt and read the value on <font SIZE="-1">STDIN. </font> See <a rel="nofollow" HREF="http://www.postfix.org/XCLIENT_README.html">http://www.postfix.org/XCLIENT_README.html</a> for official documentation for what the attributes mean and their possible values, including the special ``[<font SIZE="-1">UNAVAILABLE</font>]'' and ``[<font SIZE="-1">TEMPUNAVAIL</font>]'' values. 

 By way of simple example, setting ``--xclient-name foo.example.com --xclient-addr 192.168.1.1'' will cause swaks to send the <font SIZE="-1">SMTP</font> command ``<font SIZE="-1">XCLIENT</font> NAME=foo.example.com ADDR=192.168.1.1''. 

 Note that the ``<font SIZE="-1">REVERSE_NAME''</font> attribute doesn't seem to appear in the official documentation. There is a mailing list thread that documents it, viewable at <a rel="nofollow" HREF="http://comments.gmane.org/gmane.mail.postfix.user/192623.">http://comments.gmane.org/gmane.mail.postfix.user/192623.</a> 

 These options can all be mixed with each other, and can be mixed with the --xclient option (see below).
<dt>--xclient [<font SIZE="-1">XCLIENT_STRING</font>]
<dd> This is the ``free form'' <font SIZE="-1">XCLIENT</font> option. Whatever value is provided for <font SIZE="-1">XCLIENT_STRING</font> will be sent verbatim as the argument to the <font SIZE="-1">XCLIENT</font> smtp command. For example, if ``--xclient 'NAME= ADDR=192.168.1.1 FOO=bar''' is used, swaks will send the <font SIZE="-1">SMTP</font> command ``<font SIZE="-1">XCLIENT</font> NAME= ADDR=192.168.1.1 FOO=bar''. If no <font SIZE="-1">XCLIENT_STRING</font> is passed on command line, swaks will prompt and read the value on <font SIZE="-1">STDIN.</font> 

 The primary advantage to this over the more specific options above is that there is no <font SIZE="-1">XCLIENT</font> syntax validation here. This allows you to send invalid <font SIZE="-1">XCLIENT</font> to the target server for testing. Additionally, at least one <font SIZE="-1">MTA </font>(Message Systems' Momentum, formerly ecelerity) implements <font SIZE="-1">XCLIENT</font> without advertising supported attributes. The --xclient option allows you to skip the ``supported attributes'' check when communicating with this type of <font SIZE="-1">MTA.</font> 

 The --xclient option can be mixed freely with the --xclient-* options above. If ``--xclient-addr 192.168.0.1 --xclient 'FOO=bar NAME=wind''' is given to swaks, ``<font SIZE="-1">XCLIENT</font> ADDR=192.168.0.1 FOO=bar NAME=wind'' will be sent to the target server.
<dt>--xclient-optional
<dd>
<dt>--xclient-optional-strict
<dd> In normal operation, setting one of the --xclient* options will cause a successful <font SIZE="-1">XCLIENT</font> transaction to take place in order to proceed (that is, <font SIZE="-1">XCLIENT</font> needs to be advertised, all the user-requested attributes need to have been advertised, and the server needs to have accepted swaks' <font SIZE="-1">XCLIENT</font> request). These options change that behavior. --xclient-optional tells swaks to proceed unconditionally past the <font SIZE="-1">XCLIENT</font> stage of the <font SIZE="-1">SMTP</font> transaction, regardless of whether it was successful. --xclient-optional-strict is similar but more granular. The strict version will continue to <font SIZE="-1">XCLIENT</font> was not advertised, but will fail if <font SIZE="-1">XCLIENT</font> was attempted but did not succeed.</dl>

<h2>PROXY OPTIONS</h2>

 Swaks implements the Proxy protocol as defined in <a rel="nofollow" HREF="http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt.">http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt.</a> Proxy allows an application load balancer, such as HAProxy, to be used in front of an <font SIZE="-1">MTA</font> while still allowing the <font SIZE="-1">MTA</font> access to the originating host information. Proxy support in swaks allows direct testing of an <font SIZE="-1">MTA</font> configured to expect requests from a proxy, bypassing the proxy itself during testing. 

 Swaks makes no effort to ensure that the Proxy options used are internally consistant. For instance, --proxy-family (in version 1) is expected to be one of ``<font SIZE="-1">TCP4''</font> or ``<font SIZE="-1">TCP6''. </font> While it will likely not make sense to the target server, swaks makes no attempt to ensure that --proxy-source and --proxy-dest are in the same protocol family as --proxy-family or each other. 

 The --proxy option is mutually exclusive with all other --proxy-* options except --proxy-version. 

 When --proxy is not used, all of --proxy-family, --proxy-source, --proxy-source-port, --proxy-dest, and --proxy-dest-port are required. Additionally, when --proxy-version is 2, --proxy-protocol and --proxy-command are optional.
<dl>
<dt>--proxy-version [ 1 | 2 ]
<dd> Whether to use version 1 (human readable) or version 2 (binary) of the Proxy protocol. Version 1 is the default. Version 2 is only implemented through the ``address block'', and is roughly on par with the information provided in version 1. 

 Note that at the time of release, version 2 has been implemented but not fully tested. Postfix does not implement version 2 and Exim appears to have a bug in version 2 at the time of writing. It does mirror HAProxy's output though.
<dt>--proxy [<font SIZE="-1">VALUE</font>]
<dd> If this option is used, its argument is passed unchanged after the ``<font SIZE="-1">PROXY ''</font> portion (or the 12 byte protocol header for version 2) of the Proxy exchange. This option allows sending incomplete or malformed Proxy strings to a target server for testing. No attempt to translate or modify this string is made, so if used with ``--proxy-version 2'' the argument should be in the appropriate binary format. This option is mutually exclusive with all other --proxy-* options which provide granular proxy information.
<dt>--proxy-family [<font SIZE="-1">VALUE</font>]
<dd> For version 1, specifies both the address family and transport protocol. The protocol defines <font SIZE="-1">TCP4</font> and <font SIZE="-1">TCP6.</font> 

 For version 2, specifies only the address family. The protocol defines <font SIZE="-1">AF_UNSPEC, AF_INET, AF_INET6,</font> and <font SIZE="-1">AF_UNIX.</font>
<dt>--proxy-protocol [<font SIZE="-1">VALUE</font>]
<dd> For version 2, specifies the transport protocol. The protocol defines <font SIZE="-1">UNSPEC, STREAM,</font> and <font SIZE="-1">DGRAM. </font> The default is <font SIZE="-1">STREAM. </font> This option is unused in version 1
<dt>--proxy-command [<font SIZE="-1">VALUE</font>]
<dd> For version 2, specifies the transport protocol. The protocol defines <font SIZE="-1">LOCAL</font> and <font SIZE="-1">PROXY. </font> The default is <font SIZE="-1">PROXY. </font> This option is unused in version 1
<dt>--proxy-source [<font SIZE="-1">VALUE</font>]
<dd> Specify the source address of the proxied connection.
<dt>--proxy-source-port [<font SIZE="-1">VALUE</font>]
<dd> Specify the source port of the proxied connection.
<dt>--proxy-dest [<font SIZE="-1">VALUE</font>]
<dd> Specify the destination address of the proxied connection.
<dt>--proxy-dest-port [<font SIZE="-1">VALUE</font>]
<dd> Specify the destination port of the proxied connection.</dl>

<h2>DATA OPTIONS</h2>

 These options pertain to the contents for the <font SIZE="-1">DATA</font> portion of the <font SIZE="-1">SMTP</font> transaction.
<dl>
<dt>-d, --data [data-portion]
<dd> Use argument as the entire contents of <font SIZE="-1">DATA,</font> or prompt user if no argument specified. If the argument '-' is provided the data will be read from <font SIZE="-1">STDIN. </font> If any other argument is provided and it represents the name of an open-able file, the contents of the file will be used. Any other argument will be itself for the <font SIZE="-1">DATA</font> contents. 

 The value can be on one single line, with \n (ascii 0x5c, 0x6e) representing where line breaks should be placed. Leading dots will be quoted. Closing dot is not required but is allowed. The default value for this option is ``Date: <tt>%DATE</tt>%\nTo: <tt>%TO_ADDRESS</tt>%\nFrom: <tt>%FROM_ADDRESS</tt>%\nSubject: test <tt>%DATE</tt>%\nMessage-Id: &lt;%MESSAGEID%&gt;\nX-Mailer: swaks v%SWAKS_VERSION jetmore.org/john/code/swaks/\n%NEW_HEADERS%\n%BODY%\n''. 

 Very basic token parsing is performed on the <font SIZE="-1">DATA</font> portion. See --use-old-data-tokens for details about the single-character tokens marked as deprecated. The following table shows the recognized tokens and their replacement values:
<dl>
<dt>
<dd>
<dl>
<dt>%FROM_ADDRESS%
<dd> Replaced with the envelope-sender. Replaces the deprecated <tt>%F</tt> token.
<dt>%TO_ADDRESS%
<dd> Replaced with the envelope-recipient(s). Replaces the deprecated <tt>%T</tt> token.
<dt>%DATE%
<dd> Replaced with the current time in a format suitable for inclusion in the Date: header. Note this attempts to use the standard module Time::Local for timezone calculations. If this module is unavailable the date string will be in <font SIZE="-1">GMT. </font> Replaces the deprecated <tt>%D</tt> token.
<dt>%MESSAGEID%
<dd> Replaced with the a message <font SIZE="-1">ID</font> string suitable for use in a Message-Id header. The value for this token will remain consistent for the life of the process.
<dt>%SWAKS_VERSION%
<dd> Replaced with the version of the currently-running Swaks process.
<dt>%NEW_HEADERS%
<dd> Replaced with the contents of the --add-header option. If --add-header is not specified this token is simply removed. Replaces the deprecated <tt>%H</tt> token.
<dt>%BODY%
<dd> Replaced with the value specified by the --body option. See --body for default. Replaces the deprecated <tt>%H</tt> token.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>--use-old-data-tokens
<dd> In previous versions of swaks the <font SIZE="-1">DATA</font> tokens as described in the --data option above used single-character tokens (e.g., <tt>%F</tt>). These were not a great choice for default tokens, and proved especially troublesome with encoded, non-english languages where these character combinations might be common. The single-character tokens were replaced with the slightly-less-error-prone versions listed above. The retention of the old tokens and the inclusion of this option to activate them are intended as a temporary aid to users who have an existing message corpus using the old tokens. The single-character tokens and the --use-old-data-tokens option should be considered deprecated and likely to be removed in the next release.
<dt>-dab, --dump-as-body
<dd> If --dump-as-body is used and no other option is used to changed the default body of the message, the body is replaced with output similar to the output of what is provided by --dump. --dump's initial program capability stanza is not displayed, and the ``data'' section is not included. Additionally, --dump always includes passwords. By default --dump-as-body does not include passwords, though this can be changed with --dump-as-body-shows-password.
<dt>-dabsp, --dump-as-body-shows-password
<dd> Cause --dump-as-body to include plaintext passwords. This option is not recommended. This option implies --dump-as-body.
<dt>--body [body-specification]
<dd> Specify the body of the email. The default is ``This is a test mailing''. If no argument to --body is given, prompt to supply one interactively. If '-' is supplied, the body will be read from standard input. If any other text is provided and the text represents an open-able file, the content of that file is used as the body. If it does not represent an open-able file, the text itself is used as the body. 

 If the message is forced to <font SIZE="-1">MIME</font> format (see --attach) the argument to this option will be included unencoded as the first <font SIZE="-1">MIME</font> part. Its content-type will always be text/plain.
<dt>--attach [attachment-specification]
<dd> When one or more --attach option is supplied, the message is changed into a multipart/mixed <font SIZE="-1">MIME</font> message. The arguments to --attach are processed the same as --body with regard to stdin, file contents, etc. --attach can be supplied multiple times to create multiple attachments. By default each attachment is attached as a application/octet-stream file. See --attach-type for changing this behavior. 

 If a filename is specified, the <font SIZE="-1">MIME</font> encoding will include that file name. See --attach-name for more detail on file naming. 

 It is legal for '-' (<font SIZE="-1">STDIN</font>) to be specified as an argument multiple times (once for --body and multiple times for --attach). In this case, the same content will be attached each time it is specified. This is useful for attaching the same content with multiple <font SIZE="-1">MIME</font> types.
<dt>--attach-type [mime-type]
<dd> By default, content that gets <font SIZE="-1">MIME</font> attached to a message with the --attach option is encoded as application/octet-stream. --attach-type changes the mime type for every --attach option which follows it. It can be specified multiple times.
<dt>--attach-name [name]
<dd> This option sets the filename that will be included in the <font SIZE="-1">MIME</font> part created for the next --attach option. If no argument is set for this option, it causes no filename information to be included for the next <font SIZE="-1">MIME</font> part, even if swaks could generate it from the local file name.
<dt>-ah, --add-header [header]
<dd> This option allows headers to be added to the <font SIZE="-1">DATA. </font> If <tt>%H</tt> is present in the <font SIZE="-1">DATA</font> it is replaced with the argument to this option. If <tt>%H</tt> is not present, the argument is inserted between the first two consecutive newlines in the <font SIZE="-1">DATA </font>(that is, it is inserted at the end of the existing headers). 

 The option can either be specified multiple times or a single time with multiple headers separated by a literal '\n' string. So, ``--add-header 'Foo: bar' --add-header 'Baz: foo''' and ``--add-header 'Foo: bar\nBaz: foo''' end up adding the same two headers.
<dt>--header [header-and-data], --h-Header [data]
<dd> These options allow a way to change headers that already exist in the <font SIZE="-1">DATA. </font>'--header ``Subject: foo''' and '--h-Subject foo' are equivalent. If the header does not already exist in the data then this argument behaves identically to --add-header. However, if the header already exists it is replaced with the one specified.
<dt>-g
<dd> If specified, swaks will read the <font SIZE="-1">DATA</font> value for the mail from <font SIZE="-1">STDIN. </font> This is equivalent to ``--data -''. If there is a From_ line in the email, it will be removed (but see -nsf option). Useful for delivering real message (stored in files) instead of using example messages.
<dt>--no-data-fixup, -ndf
<dd> This option forces swaks to do no massaging of the <font SIZE="-1">DATA</font> portion of the email. This includes token replacement, From_ stripping, trailing-dot addition, --body/attachment inclusion, and any header additions. This option is really only useful when used with --data, since the internal default <font SIZE="-1">DATA</font> portion uses tokens.
<dt>--no-strip-from, -nsf
<dd> Don't strip the From_ line from the <font SIZE="-1">DATA</font> portion, if present.</dl>

<h2>OUTPUT OPTIONS</h2>

 By default swaks provides a transcript of its transactions to its caller (<font SIZE="-1">STDOUT/STDERR</font>). This transcript aims to be as faithful a representation as possible of the transaction though it does modify this output by adding informational prefixes to lines and by providing plaintext versions of <font SIZE="-1">TLS</font> transactions 

 The ``informational prefixes'' are referred to as transaction hints. These hints are initially composed of those marking lines that are output of swaks itself, either informational or error messages, and those that indicate a line of data actually sent or received in a transaction. This table indicates the hints and their meanings:
<dl>
<dt>&quot;===&quot;
<dd> Indicates an informational line generated by swaks
<dt>&quot;***&quot;
<dd> Indicates an error generated within swaks
<dt>&quot;&nbsp;<wbr>-&gt;&quot;
<dd> Indicates an expected line sent by swaks to target server
<dt>&quot;&nbsp;<wbr>~&gt;&quot;
<dd> Indicates a TLS-encrypted, expected line sent by swaks to target server
<dt>&quot;**&gt;&quot;
<dd> Indicates an unexpected line sent by swaks to the target server
<dt>&quot;*~&gt;&quot;
<dd> Indicates a TLS-encrypted, unexpected line sent by swaks to target server
<dt>&quot;&nbsp;<wbr>&nbsp;<wbr>&gt;&quot;
<dd> Indicates a raw chunk of text sent by swaks to a target server (see --show-raw-text). There is no concept of ``expected'' or ``unexpected'' at this level.
<dt>&quot;&lt;-&nbsp;<wbr>&quot;
<dd> Indicates an expected line sent by target server to swaks
<dt>&quot;&lt;~&nbsp;<wbr>&quot;
<dd> Indicates a TLS-encrypted, expected line sent by target server to swaks
<dt>&quot;&lt;**&quot;
<dd> Indicates an unexpected line sent by target server to swaks
<dt>&quot;&lt;~*&quot;
<dd> Indicates a TLS-encrypted, unexpected line sent by target server to swaks
<dt>&quot;&lt;&nbsp;<wbr>&nbsp;<wbr>&quot;
<dd> Indicates a raw chunk of text received by swaks from a target server (see --show-raw-text). There is no concept of ``expected'' or ``unexpected'' at this level.</dl>
 

 The following options control what and how output is displayed to the caller.
<dl>
<dt>-n, --suppress-data
<dd> Summarizes the <font SIZE="-1">DATA</font> portion of the <font SIZE="-1">SMTP</font> transaction instead of printing every line. This option is very helpful, bordering on required, when using swaks to send certain test emails. Emails with attachments, for instance, will quickly overwhelm a terminal if the <font SIZE="-1">DATA</font> is not supressed.
<dt>-stl, --show-time-lapse [i]
<dd> Display time lapse between send/receive pairs. This option is most useful when Time::HiRes is available, in which case the time lapse will be displayed in thousandths of a second. If Time::HiRes is unavailable or ``i'' is given as an argument the lapse will be displayed in integer seconds only.
<dt>-nih, --no-info-hints
<dd> Don't display the transaction hint for informational transactions. This is most useful when needing to copy some portiong of the informational lines, for instance the certificate output from --tls-get-peer-cert.
<dt>-nsh, --no-send-hints
<dd>
<dt>-nrh, --no-receive-hints
<dd>
<dt>-nth, --no-hints
<dd> --no-send-hints and --no-receive-hints supress the transaction prefix from send and receive lines, respectively. This is often useful when copying some portion of the transaction for use elsewhere (for instance, ``--no-send-hints --hide-receive --hide-informational'' is a useful way to get only the client-side commands for a given transaction). --no-hints is identical to specifying both --no-send-hints and --no-receive-hints. 

 Don't show transaction hints (useful in conjunction with -hr to create copy/paste-able transactions).
<dt>-raw, --show-raw-text
<dd> This option will print a hex dump of raw data sent and received by swaks. Each hex dump is the contents of a single read or write on the network. This should be identical to what is already being displayed (with the exception of the \r characters being removed). This option is useful in seeing details when servers are sending lots of data in single packets, or breaking up individual lines into multiple packets. If you really need to go in depth in that area you're probably better with a packet sniffer, but this option is a good first step to seeing odd connection issues.
<dt>--output-file &lt;/path/to/file&gt;
<dd>
<dt>--output-file-stdout &lt;/path/to/file&gt;
<dd>
<dt>--output-file-stderr &lt;/path/to/file&gt;
<dd> These options allow the user to send output to files instead of stdout/stderr. The first option sends both to the same file. The arguments of &amp;STDOUT and &amp;STDERR are treated specially, refering to the ``normal'' file handles, so ``--output-file-stderr '&amp;STDOUT''' would redirect <font SIZE="-1">STDERR</font> to <font SIZE="-1">STDOUT.</font>
<dt>-pp, --protect-prompt
<dd> Don't echo user input on prompts that are potentially sensitive (right now only authentication password). See also --auth-hide-password
<dt>-hr, --hide-receive
<dd> Don't display lines sent from the remote server being received by swaks
<dt>-hs, --hide-send
<dd> Don't display lines being sent by swaks to the remote server
<dt>-hi, --hide-informational
<dd> Don't display non-error informational lines from swaks itself.
<dt>-ha, --hide-all
<dd> Do not display any content to the terminal.
<dt>-S, --silent [level]
<dd> Cause swaks to be silent. If no argument is given or if an argument of ``1'' is given, print no output unless/until an error occurs, after which all output is shown. If an argument of ``2'' is given, only print errors. If ``3'' is given, show no output ever.
<dt>--support
<dd> Print capabilities and exit. Certain features require non-standard perl modules. This options evaluates whether these modules are present and displays which functionality is available and which isn't, and which modules would need to be added to gain the missing functionality.
<dt>--dump
<dd> This option causes swaks to print the results of option processing, immediately before mail would have been sent. No mail will be sent when --dump is used. Note that --dump is considered to be a pure self-diagnosis tool and no effort is made or will ever be made to mask passwords in the --dump output.
<dt>--help
<dd> Display this help information.
<dt>--version
<dd> Display version information.</dl>

<h2>PORTABILITY</h2>

<dl>
<dt><font SIZE="-1">OPERATING SYSTEMS</font>
<dd> This program was primarily intended for use on unix-like operating systems, and it should work on any reasonable version thereof. It has been developed and tested on Solaris, Linux, and Mac <font SIZE="-1">OS X</font> and is feature complete on all of these. 

 This program is known to demonstrate basic functionality on Windows using ActiveState's Perl. It has not been fully tested. Known to work are basic <font SIZE="-1">SMTP</font> functionality and the <font SIZE="-1">LOGIN, PLAIN,</font> and <font SIZE="-1">CRAM-MD5</font> auth types. Unknown is any <font SIZE="-1">TLS</font> functionality and the <font SIZE="-1">NTLM/SPA</font> and <font SIZE="-1">DIGEST-MD5</font> auth types. 

 Because this program should work anywhere Perl works, I would appreciate knowing about any new operating systems you've thoroughly used swaks on as well as any problems encountered on a new <font SIZE="-1">OS.</font>
<dt><font SIZE="-1">MAIL SERVERS</font>
<dd> This program was almost exclusively developed against Exim mail servers. It was been used casually by the author, though not thoroughly tested, with Sendmail, Smail, Exchange, Oracle Collaboration Suite, qpsmtpd, and Communigate. Because all functionality in swaks is based off of known standards it should work with any fairly modern mail server. If a problem is found, please alert the author at the address below.</dl>

<h2>EXIT CODES</h2>

<dl>
<dt>0
<dd> no errors occurred
<dt>1
<dd> error parsing command line options
<dt>2
<dd> error connecting to remote server
<dt>3
<dd> unknown connection type
<dt>4
<dd> while running with connection type of ``pipe'', fatal problem writing to or reading from the child process
<dt>5
<dd> while running with connection type of ``pipe'', child process died unexpectedly. This can mean that the program specified with --pipe doesn't exist.
<dt>6
<dd> Connection closed unexpectedly. If the close is detected in response to the '<font SIZE="-1">QUIT</font>' swaks sends following an unexpected response, the error code for that unexpected response is used instead. For instance, if a mail server returns a 550 response to a <font SIZE="-1">MAIL FROM:</font> and then immediately closes the connection, swaks detects that the connection is closed, but uses the more specific exit code 23 to detail the nature of the failure. If instead the server return a 250 code and then immediately closes the connection, swaks will use the exit code 6 because there is not a more specific exit code.
<dt>10
<dd> error in prerequisites (needed module not available)
<dt>21
<dd> error reading initial banner from server
<dt>22
<dd> error in <font SIZE="-1">HELO</font> transaction
<dt>23
<dd> error in <font SIZE="-1">MAIL</font> transaction
<dt>24
<dd> no RCPTs accepted
<dt>25
<dd> server returned error to <font SIZE="-1">DATA</font> request
<dt>26
<dd> server did not accept mail following data
<dt>27
<dd> server returned error after normal-session quit request
<dt>28
<dd> error in <font SIZE="-1">AUTH</font> transaction
<dt>29
<dd> error in <font SIZE="-1">TLS</font> transaction
<dt>30
<dd> <font SIZE="-1">PRDR</font> requested/required but not advertised
<dt>32
<dd> error in <font SIZE="-1">EHLO</font> following <font SIZE="-1">TLS</font> negotiation
<dt>33
<dd> error in <font SIZE="-1">XCLIENT</font> transaction
<dt>34
<dd> error in <font SIZE="-1">EHLO</font> following <font SIZE="-1">XCLIENT</font>
<dt>35
<dd> error in <font SIZE="-1">PROXY</font> option processing
<dt>36
<dd> error sending <font SIZE="-1">PROXY</font> banner</dl>

<h2>ABOUT THE NAME</h2>

 The name ``swaks'' is a (sort-of) acronym for ``SWiss Army Knife Smtp''. It was chosen to be fairly distinct and pronounceable. While ``swaks'' is unique as the name of a software package, it has some other, non-software meanings. Please send in other uses of ``swak'' or ``swaks'' for inclusion.
<dl>
<dt>&quot;Sealed With A Kiss&quot;
<dd> SWAK/SWAKs turns up occasionally on the internet with the meaning ``with love''.
<dt>bad / poor / ill (Afrikaans)
<dd> Seen in the headline ``<font SIZE="-1">SA</font> se bes en swaks gekledes in 2011'', which was translated as ``best and worst dressed'' by native speakers. Google Translate doesn't like ``swaks gekledes'', but it will translate ``swak'' as ``poor'' and ``swak geklede'' as ``ill-dressed''.</dl>

<h2>CONTACT</h2>

<dl>
<dt>proj-swaks [at] jetmore.net
<dd> Please use this address for general contact, questions, patches, requests, etc.
<dt>updates-swaks [at] jetmore.net
<dd> If you would like to be put on a list to receive notifications when a new version of swaks is released, please send an email to this address.
<dt><a rel="nofollow" HREF="http://www.jetmore.org/john/code/swaks/">http://www.jetmore.org/john/code/swaks/</a>
<dd> Change logs, this help, and the latest version is found at this link. 

</dl>

<h2>Index</h2>


