---

title: "swaks(1)"
name: "swaks"
section: "1"
letter: "s"
url: "/docs/linux/man/1-swaks/"
---

swaks - Swiss Army Knife SMTP, the all-purpose smtp transaction tester 

<h2>DESCRIPTION</h2>

 swaks' primary design goal is to be a flexible, scriptable, transaction-oriented SMTP test tool. It handles SMTP features and extensions such as TLS, authentication, and pipelining; multiple version of the SMTP protocol including SMTP, ESMTP, and LMTP; and multiple transport methods including unix-domain sockets, internet-domain sockets, and pipes to spawned processes. Options can be specified in environment variables, configuration files, and the command line allowing maximum configurability and ease of use for operators and scripters.

<h2>QUICK START</h2>

 Deliver a standard test email to user [at] example.com on port 25 of test-server.example.net: 

 <pre><code>
swaks-- to user[at] example.com-- server test - server.example.net
</code></pre> 

 Deliver a standard test email, requiring CRAM-MD5 authentication as user me [at] example.com. An ``X-Test'' header will be added to the email body. The authentication password will be prompted for. 

 
swaks-- to user[at] example.com-- from me[at] example.com-- auth CRAM - MD5-- auth - user me[at] example.com-- header - X - Test "test email"
 

 Test a virus scanner using EICAR in an attachment. Don't show the message DATA part.: 

 
swaks - t user[at] example.com-- attach - --server test - server.example.com-- suppress - data &lt; / path / to / eicar.txt
 

 Test a spam scanner using GTUBE in the body of an email, routed via the MX records for example.com: 

 
swaks-- to user[at] example.com-- body / path / to / gtube / file
 

 Deliver a standard test email to user [at] example.com using the LMTP protocol via a UNIX domain socket file 

 
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
</dt><dd> A transaction is the opening of a connection over a transport to a target and using a messaging protocol to attempt to deliver a message.
</dd><dt>Target
</dt><dd> The target of a transaction is the thing that swaks connects to. This generic term is used throughout the documentation because most other terms improperly imply something about the transport being used.
</dd><dt>Transport
</dt><dd> The transport is the underlying method used to connect to the target.
</dd><dt>Protocol
</dt><dd> The protocol is the application language used to communicate with the target. This document uses SMTP to speak generically of all three supported protocols unless it states that it is speaking of the specific 'SMTP' protocol and excluding the others.
</dd><dt>Message
</dt><dd> SMTP protocols exist to transfer messages, a set of bytes in an agreed-upon format that has a sender and a recipient.
</dd><dt>Envelope
</dt><dd> A message's envelope contains the ``true'' sender and receiver of a message. It can also be referred to as its components, envelope-sender and envelope-recipients. It is important to note that a messages envelope does not have to match its To: and From: headers.
</dd><dt>DATA
</dt><dd> The DATA portion of an SMTP transaction is the actual message that is being transported. It consists of both the message's headers and its body. DATA and body are sometimes use synonymously, but they are always two distinct things in this document.
</dd><dt>Headers
</dt><dd> A message's headers are defined as all the lines in the message's DATA section before the first blank line. They contain information about the email that will be displayed to the recipient such as To:, From:, Subject:, etc. In this document headers will always be written with a capitalized first letter and a trailing colon.
</dd><dt>Body
</dt><dd> A message's body is the portion of its DATA section following the first blank line.</dd></dl>

<h2>OPTION PROCESSING</h2>

 To prevent potential confusion in this document a flag to swaks is always referred to as an ``option''. If the option takes additional data, that additional data is referred to as an argument to the option. For example, ``--from fred [at] example.com'' might be provided to swaks on the command line, with ``--from'' being the option and ``fred [at] example.com'' being --from's argument. 

 Options can be given to swaks in three ways. They can be specified in a configuration file, in environment variables, and on the command line. Depending on the specific option and whether or not an argument is given to it, swaks may prompt the user for the argument. 

 When swaks evaluates its options, it first looks for a configuration file (either in a default location or specified with --config). Then it evaluates any options in environment variables. Finally, it evaluates command line options. At each round of processing, any options set earlier will be overridden. Additionally, any option can be prefixed with ``no-'' to cause swaks to forget that the variable had previously been set. This capability is necessary because many options treat defined-but-no-argument differently than not-defined. 

 The exact mechanism and format for using each of the types is listed below.
<dl>
<dt>CONFIGURATION FILE
</dt><dd> A configuration file can be used to set commonly-used or abnormally verbose options. By default swaks looks in order for <tt>$SWAKS_HOME</tt>/.swaksrc, <tt>$HOME</tt>/.swaksrc, and <tt>$LOGDIR</tt>/.swaksrc. If one of those is found to exist (and --config has not been used) that file is used as the configuration file. 
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
</dd><dt>ENVIRONMENT VARIABLES
</dt><dd> Options can be supplied via environment variables. The variables are in the form <tt>$SWAKS_OPT_name</tt>, where name is the name of the option that would be specified on the command line. Because dashes aren't allowed in environment variable names in most unix-ish shells, no leading dashes should be used and any dashes inside the option's name should be replaced with underscores. The following would create the same options shown in the configuration file example: 
$ SWAKS_OPT_from = 'fred [at] example.com' $ SWAKS_OPT_h_From = '"Fred Example" &lt;fred [at] example.com&gt;'
 Setting a variable to an empty value is the same as specifying it on the command line with no argument. For instance, setting SWAKS_OPT_server=&quot;&quot; would cause swaks to prompt the use for the server to which to connect at each invocation. 
 In addition to setting the equivalent of command line options, SWAKS_HOME can be set to a directory containing the default .swaksrc to be used.
</dd><dt>COMMAND LINE OPTIONS
</dt><dd> The final method of supplying options to swaks is via the command line. The options behave in a manner consistent with most unix-ish command line programs. Many options have both a short and long form (for instance -s and --server). By convention short options are specified with a single dash and long options are specified with a double-dash. This is only a convention and either prefix will work with either type. 
 The following demonstrates the example shown in the configuration file and environment variable sections: 
 <pre><code>
$ swaks-- from fred[at] example.com-- h - From : '"Fred Example" &lt;fred [at] example.com&gt;'
</code></pre></dd></dl>

<h2>TRANSPORTS</h2>

 swaks can connect to a target via unix pipes (``pipes''), unix domain sockets (``unix sockets''), or internet domain sockets (``network sockets''). Connecting via network sockets is the default behavior. Because of the singular nature of the transport used, each set of options in the following section is mutually exclusive. Specifying more than one of --server, --pipe, or --socket will result in an error. Mixing other options between transport types will only result in the irrelevant options being ignored. Below is a brief description of each type of transport and the options that are specific to that transport type.
<dl>
<dt>NETWORK SOCKETS
</dt><dd> This transport attempts to deliver a message via TCP/IP, the standard method for delivering SMTP.  This is the default transport for swaks. If none of --server, --pipe, or --socket are given then this transport is used and the target server is determined from the recipient's domain (see --server below for more details). 
 This transport requires the IO::Socket module which is part of the standard perl distribution. If this module is not loadable, attempting to use a this transport will result in an error and program termination. 
 IPv6 is supported when the IO::Socket::INET6 module is present.
</dd><dl>
<dl>
<dt>-s, --server [target mail server[:port]]
</dt><dd> Explicitly tell swaks to use network sockets and specify the hostname or IP address to which to connect, or prompt if no argument is given. If this option is not given and no other transport option is given, the target mail server is determined from the appropriate DNS records for the domain of the recipient email address using the Net::DNS module. If Net::DNS is not available swaks will attempt to connect to localhost to deliver. The target port can optionally be set here. Supported formats for this include SERVER:PORT (supporting names and IPv4 addresses); [SERVER]:PORT and SERVER/PORT (supporting names, IPv4 and IPv6 addresses). See also --copy-routing.
</dd><dt>-p, --port [port]
</dt><dd> Specify which TCP port on the target is to be used, or prompt if no argument is listed. The argument can be a service name (as retrieved by <i><a HREF="/docs/linux/man/3-getservbyname/">getservbyname</a></i>(3)) or a port number. The default port is determined by the --protocol option. See --protocol for more details.
</dd><dt>-li, --local-interface [IP or hostname[:port]]
</dt><dd> Use argument as the local interface for the outgoing SMTP connection, or prompt user if no argument given. Argument can be an IP address or a hostname. Default action is to let the operating system choose local interface. See --server for additional comments on :port format.
</dd><dt>-lp, --local-port [port]
</dt><dd> Specify the outgoing port to originate the transaction from. If this option is not specified the system will pick an ephemeral port. Note that regular users cannot specify some ports.
</dd><dt>--copy-routing [domain]
</dt><dd> The argument is interpreted as the domain part of an email address and it is used to find the target server using the same logic that would be used to look up the target server for a recipient email address. See --to option for more details on how the target is determined from the email domain.
</dd><dt>-4, -6
</dt><dd> Force IPv4 or IPv6.</dd></dl>
</dl>

<dl>
</dl>

<dt>UNIX SOCKETS
</dt><dd> This transport method attempts to deliver messages via a unix-domain socket file. This is useful for testing MTA/MDAs that listen on socket files (for instance, testing LMTP delivery to Cyrus). This transport requires the IO::Socket module which is part of the standard perl distribution. If this module is not loadable, attempting to use this transport will result in an error and program termination.
</dd><dl>
<dl>
<dt>--socket [/path/to/socket/file]
</dt><dd> This option takes as its argument a unix-domain socket file. If swaks is unable to open this socket it will display an error and exit.</dd></dl>
</dl>

<dl>
</dl>

<dt>PIPES
</dt><dd> This transport attempts to spawn a process and communicate with it via pipes. The spawned program must be prepared to behave as a mail server over STDIN/STDOUT.  Any MTA designed to operate from inet/xinet should support this. In addition some MTAs provide testing modes that can be communicated with via STDIN/STDOUT.  This transport can be used to automate that testing. For example, if you implemented DNSBL checking with Exim and you wanted to make sure it was working, you could run 'swaks --pipe ``exim -bh 127.0.0.2'''. In an ideal world the process you are talking to should behave exactly like an SMTP server on stdin and stdout. Any debugging should be sent to stderr, which will be directed to your terminal. In the real world swaks can generally handle some debug on the child's stdout, but there are no guarantees on how much it can handle. 

 This transport requires the IPC::Open2 module which is part of the standard perl distribution. If this module is not loadable, attempting to use this transport will result in an error and program termination.
</dd><dl>
<dl>
<dt>--pipe [/path/to/command and arguments]
</dt><dd> Provide a process name and arguments to the process. swaks will attempt to spawn the process and communicate with it via pipes. If the argument is not an executable swaks will display an error and exit.</dd></dl>
</dl>

<dl>
</dl>
</dl>

<h2>PROTOCOL OPTIONS</h2>

 These options are related to the protocol layer.
<dl>
<dt>-t, --to [email-address[,email-address,...]]
</dt><dd> Tells swaks to use argument(s) as the envelope-recipient for the email, or prompt for recipient if no argument provided. If multiple recipients are provided and the recipient domain is needed to determine routing the domain of the last recipient provided is used. 
 There is no default value for this option. If no recipients are provided via any means, user will be prompted to provide one interactively. The only exception to this is if a --quit-after value is provided which will cause the smtp transaction to be terminated before the recipient is needed.
</dd><dt>-f, --from [email-address]
</dt><dd> Use argument as envelope-sender for email, or prompt user if no argument specified. The string &lt;&gt; can be supplied to mean the null sender. If user does not specify a sender address a default value is used. The domain-part of the default sender is a best guess at the fully-qualified domain name of the local host. The method of determining the local-part varies. On Windows, <i>Win32::LoginName()</i> is used. On unix-ish platforms, the <tt>$LOGNAME</tt> environment variable is used if it is set. Otherwise <i><a HREF="/docs/linux/man/3-getpwuid/">getpwuid</a></i>(3) is used. See also --force-getpwuid.
</dd><dt>--ehlo, --lhlo, -h, --helo [helo-string]
</dt><dd> String to use as argument to HELO/EHLO/LHLO command, or prompt use if no argument is specified. If this option is not used a best guess at the fully-qualified domain name of the local host is used. If the Sys::Hostname module, which is part of the base distribution, is not available the user will be prompted for a HELO value. Note that Sys::Hostname has been observed to not be able to find the local hostname in certain circumstances. This has the same effect as if Sys::Hostname were unavailable.
</dd><dt>-q, --quit, --quit-after [stop-point]
</dt><dd> Point at which the transaction should be stopped. When the requested stopping point is reached in the transaction, and provided that swaks has not errored out prior to reaching it, swaks will send ``QUIT'' and attempt to close the connection cleanly. These are the valid arguments and notes about their meaning.
</dd><dl>
<dl>
<dt>CONNECT, BANNER
</dt><dd> Terminate the session after receiving the greeting banner from the target.
</dd><dt>FIRST-HELO, FIRST-EHLO, FIRST-LHLO
</dt><dd> In a STARTTLS (but not tls-on-connect) session, terminate the transaction after the first of two HELOs. In a non-STARTTLS transaction, behaves the same as HELO (see below).
</dd><dt>XCLIENT
</dt><dd> Quit after XCLIENT is sent
</dd><dt>TLS
</dt><dd> Quit the transaction immediately following TLS negotiation. Note that this happens in different places depending on whether STARTTLS or tls-on-connect are used. This always quits after the point where TLS would have been negotiated, regardless of whether it was attempted.
</dd><dt>HELO, EHLO, LHLO
</dt><dd> In a STARTTLS or XCLIENT session, quit after the second HELO.  Otherwise quit after the first and only HELO.
</dd><dt>AUTH
</dt><dd> Quit after authentication. This always quits after the point where authentication would have been negotiated, regardless of whether it was attempted.
</dd><dt>MAIL, FROM
</dt><dd> Quit after MAIL FROM: is sent.
</dd><dt>RCPT, TO
</dt><dd> Quit after RCPT TO: is sent.</dd></dl>
</dl>

<dl>
</dl>

<dt>--da, --drop-after [stop-point]
</dt><dd> The option is similar to --quit-after, but instead of trying to cleanly shut down the session it simply terminates the session. This option accepts the same stop-points as --quit-after.
</dd><dt>--das, --drop-after-send
</dt><dd> This option is similar to --drop-after, but instead of dropping the connection after reading a response to the stop-point, it drops the connection immediately after sending stop-point.
</dd><dt>--timeout [time]
</dt><dd> Use argument as the SMTP transaction timeout, or prompt user if no argument given. Argument can either be a pure digit, which will be interpretted as seconds, or can have a specifier s or m (5s = 5 seconds, 3m = 180 seconds). As a special case, 0 means don't timeout the transactions. Default value is 30s.
</dd><dt>--protocol [protocol]
</dt><dd> Specify which protocol to use in the transaction. Valid options are shown in the table below. Currently the 'core' protocols are SMTP, ESMTP, and LMTP.  By using variations of these protocol types one can tersely specify default ports, whether authentication should be attempted, and the type of TLS connection that should be attempted. The default protocol is ESMTP.  This table demonstrates the available arguments to --protocol and the options each sets as a side effect:
</dd><dl>
<dl>
<dt>SMTP
</dt><dd> HELO, ``-p 25''
</dd><dt>SSMTP
</dt><dd> EHLO-&gt;HELO, ``-tlsc -p 465''
</dd><dt>SSMTPA
</dt><dd> EHLO-&gt;HELO, ``-a -tlsc -p 465''
</dd><dt>SMTPS
</dt><dd> HELO, ``-tlsc -p 465''
</dd><dt>ESMTP
</dt><dd> EHLO-&gt;HELO, ``-p 25''
</dd><dt>ESMTPA
</dt><dd> EHLO-&gt;HELO, ``-a -p 25''
</dd><dt>ESMTPS
</dt><dd> EHLO-&gt;HELO, ``-tls -p 25''
</dd><dt>ESMTPSA
</dt><dd> EHLO-&gt;HELO, ``-a -tls -p 25''
</dd><dt>LMTP
</dt><dd> LHLO, ``-p 24''
</dd><dt>LMTPA
</dt><dd> LHLO, ``-a -p 24''
</dd><dt>LMTPS
</dt><dd> LHLO, ``-tls -p 24''
</dd><dt>LMTPSA
</dt><dd> LHLO, ``-a -tls -p 24''</dd></dl>
</dl>

<dl>
</dl>

<dt>--pipeline
</dt><dd> If the remote server supports it, attempt SMTP PIPELINING (RFC 2920).
</dd><dt>--prdr
</dt><dd> If the server supports it, attempt Per-Recipient Data Response (PRDR) (<a rel="nofollow" HREF="https://tools.ietf.org/html/draft-hall-prdr-00.txt">https://tools.ietf.org/html/draft-hall-prdr-00.txt</a>). PRDR is not yet standardized, but MTAs have begun implementing the proposal.
</dd><dt>--force-getpwuid
</dt><dd> Tell swaks to use the getpwuid method of finding the default sender local-part instead of trying <tt>$LOGNAME</tt> first.</dd></dl>

<h2>TLS / ENCRYPTION</h2>

 These are options related to encrypting the transaction. These have been tested and confirmed to work with all three transport methods. The Net::SSLeay module is used to perform encryption when it is requested. If this module is not loadable swaks will either ignore the TLS request or error out, depending on whether the request was optional. STARTTLS is defined as an extension in the ESMTP protocol and will be unavailable if --protocol is set to a variation of smtp. Because it is not defined in the protocol itself, --tls-on-connect is available for any protocol type if the target supports it. 

 A local certificate is not required for a TLS connection to be negotiated. However, some servers use client certificate checking to verify that the client is allowed to connect. swaks can be told to use a specific local certificate through the use of the --tls-cert and --tls-key options.
<dl>
<dt>-tls
</dt><dd> Require connection to use STARTTLS.  Exit if TLS not available for any reason (not advertised, negotiations failed, etc).
</dd><dt>-tlso, --tls-optional
</dt><dd> Attempt to use STARTTLS if available, continue with normal transaction if TLS was unable to be negotiated for any reason. Note that this is a semi-useless option as currently implemented because after a negotiation failure the state of the connection is unknown. In some cases, like a version mismatch, the connection should be left as plaintext. In others, like a verification failure, the server-side may think that it should continue speaking TLS while the client thinks it is plaintext. There may be an attempt to add more granular state detection in the future, but for now just be aware that odd things may happen with this option if the TLS negotiation is attempted and fails.
</dd><dt>-tlsos, --tls-optional-strict
</dt><dd> Attempt to use STARTTLS if available. Proceed with transaction if TLS is negotiated successfully or STARTTLS not advertised. If STARTTLS is advertised but TLS negotiations fail, treat as an error and abort transaction. Due to the caveat noted above, this is a much more sane option than --tls-optional.
</dd><dt>--tlsc, --tls-on-connect
</dt><dd> Initiate a TLS connection immediately on connection. Following common convention, if this option is specified the default port changes from 25 to 465, though this can still be overridden with the --port option.
</dd><dt>-tlsp, --tls-protocol SPECIFICATION
</dt><dd> Specify which protocols to use (or not use) when negotiating TLS.  At the time of this writing, the available protocols are sslv2, sslv3, tlsv1, tlsv1_1, and tlsv1_2. The availability of these protocols is dependent on your underlying OpenSSL library, so not all of these may be available. The list of available protocols is shown in the output of --dump (assuming TLS is available at all). 
 The specification string is a comma-delimited list of protocols that can be used or not used. For instance 'tlsv1,tlsv1_1' will only succeed if one of those two protocols is available on both the client and the server. Conversely, 'no_sslv2,no_sslv3' will attempt to negotiate any protocol except sslv2 and sslv3. The two forms of specification cannot be mixed.
</dd><dt>-tls-cipher CIPHER_STRING
</dt><dd> Th argument to this option is passed to the underlying OpenSSL library to set the list of acceptable ciphers to the be used for the connection. The format of this string is opaque to swaks and is defined in <a rel="nofollow" HREF="http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT.">http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT.</a> A brief example would be --tls-cipher '3DES:+RSA'.
</dd><dt>--tls-verify
</dt><dd> By default swaks does not do any certificate verification. Setting --tls-verify will cause swaks to attempt to verify the server's certificate. If this option is set and the server's certificate is not verifiable (either using the system-default CA information, or custom CA information (see --tls-ca-path)) TLS negotiation will not succeed.
</dd><dt>--tls-ca-path [ /path/to/CAfile | /path/to/CAdir/ ]
</dt><dd> By default swaks will use the underlying OpenSSL library's default CA information for verifying server certificates. --tls-ca-path allows you to specify an alternate location. See <a rel="nofollow" HREF="http://www.openssl.org/docs/ssl/SSL_CTX_load_verify_locations.html">http://www.openssl.org/docs/ssl/SSL_CTX_load_verify_locations.html</a> for details of the file/directory contents.
</dd><dt>--tls-cert /path/to/file
</dt><dd> Provide a path to a file containing the local certificate swaks should use if TLS is negotiated. The file path argument is required. As currently implemented the certificate in the file must be in PEM format. Contact the author if there's a compelling need for ASN1.  If this option is set, --tls-key is also required.
</dd><dt>--tls-key /path/to/file
</dt><dd> Provide a path to a file containing the local private key swaks should use if TLS is negotiated. The file path argument is required. As currently implemented the certificate in the file must be in PEM format. Contact the author if there's a compelling need for ASN1.  If this option is set, --tls-cert is also required.
</dd><dt>--tls-get-peer-cert [/path/to/file]
</dt><dd> Get a copy of the TLS peer's certificate. If no argument is given, it will be displayed to STDOUT.  If an argument is given it is assumed to be a filesystem path specifying where the certificate should be written. The saved certificate can then be examined using standard tools such as the openssl command. If a file is specified its contents will be overwritten.</dd></dl>

<h2>AUTHENTICATION</h2>

 swaks will attempt to authenticate to the target mail server if instructed to do so. This section details available authentication types, requirements, options and their interactions, and other fine points in authentication usage. Because authentication is defined as an extension in the ESMTP protocol it will be unavailable if --protocol is set to a variation of smtp. 

 All authentication methods require base64 encoding. If the MIME::Base64 perl module is loadable swaks attempts to use it to perform these encodings. If MIME::Base64 is not available swaks will use its own onboard base64 routines. These are slower than the MIME::Base64 routines and less reviewed, though they have been tested thoroughly. Using the MIME::Base64 module is encouraged. 

 If authentication is required (see options below for when it is and isn't required) and the requirements aren't met for the authentication type available, swaks displays an error and exits. Two ways this can happen include forcing swaks to use a specific authentication type that swaks can't use due to missing requirements, or allowing swaks to use any authentication type, but the server only advertises types swaks can't support. In the former case swaks errors out at option processing time since it knows up front it won't be able to authenticate. In the latter case swaks will error out at the authentication stage of the smtp transaction since swaks will not be aware that it will not be able to authenticate until that point. 

 Following are the supported authentication types including any individual notes and requirements. 

 The following options affect swaks' use of authentication. These options are all inter-related. For instance, specifying --auth-user implies --auth and --auth-password. Specifying --auth-optional implies --auth-user and --auth-password, etc.
<dl>
<dt>-a, --auth [auth-type[,auth-type,...]]
</dt><dd> Require swaks to authenticate. If no argument is given, any supported auth-types advertised by the server are tried until one succeeds or all fail. If one or more auth-types are specified as an argument, each that the server also supports is tried in order until one succeeds or all fail. This option requires swaks to authenticate, so if no common auth-types are found or no credentials succeed, swaks displays an error and exits. 
 The following tables lists the valid auth-types
</dd><dl>
<dl>
<dt>LOGIN, PLAIN
</dt><dd> These basic authentication types are fully supported and tested and have no additional requirements
</dd><dt>CRAM-MD5
</dt><dd> The CRAM-MD5 authenticator requires the Digest::MD5 module. It is fully tested and believed to work against any server that implements it.
</dd><dt>DIGEST-MD5
</dt><dd> The DIGEST-MD5 authenticator (RFC2831) requires the Authen::SASL module. Version 20100211.0 and earlier used Authen::DigestMD5 which had some protocol level errors which prevented it from working with some servers. Authen::SASL's DIGEST-MD5 handling is much more robust. 
 The DIGEST-MD5 implementation in swaks is fairly immature. It currently supports only the ``auth'' qop type, for instance. If you have DIGEST-MD5 experience and would like to help swaks support DIGEST-MD5 better, please get in touch with me. 
 The DIGEST-MD5 protocol's ``realm'' value can be set using the --auth-extra ``realm'' keyword. If no realm is given, a reasonable default will be used. 
 The DIGEST-MD5 protocol's ``digest-uri'' values can be set using the --auth-extra option. For instance, you could create the digest-uri-value of ``lmtp/mail.example.com/example.com'' with the option ``--auth-extra dmd5-serv-type=lmtp,dmd5-host=mail.example.com,dmd5-serv-name=example.com''. The ``digest-uri-value'' string and its components is defined in RFC2831.  If none of these values are given, reasonable defaults will be used.
</dd><dt>CRAM-SHA1
</dt><dd> The CRAM-SHA1 authenticator requires the Digest::SHA module. This type has only been tested against a non-standard implementation on an Exim server and may therefore have some implementation deficiencies.
</dd><dt>NTLM/SPA/MSN
</dt><dd> These authenticators require the Authen::NTLM module. Note that there are two modules using the Authen::NTLM namespace on CPAN.  The Mark Bush implementation (Authen/NTLM-1.03.tar.gz) is the version required by swaks. This type has been tested against Exim, Communigate, and Exchange 2007. 
 In addition to the standard username and password, this authentication type can also recognize a ``domain''. The domain can be set using the --auth-extra ``domain'' keyword. Note that this has never been tested with a mail server that doesn't ignore DOMAIN so this may be implemented incorrectly.</dd></dl>
</dl>

<dl>
</dl>

<dt>-ao, --auth-optional [auth-type[,auth-type,...]]
</dt><dd> This option behaves identically to --auth except that it requests authentication rather than requiring it. If no common auth-types are found or no credentials succeed, swaks proceeds as if authentication had not been requested.
</dd><dt>-aos, --auth-optional-strict [auth-type[,auth-type,...]]
</dt><dd> This option is a compromise between --auth and --auth-optional. If no common auth-types are found, swaks behaves as if --auth-optional were specified and proceeds with the transaction. If swaks can't support requested auth-type, the server doesn't advertise any common auth-types, or if no credentials succeed, swaks behaves as if --auth were used and exits with an error.
</dd><dt>-au, --auth-user [username]
</dt><dd> Provide the username to be used for authentication, or prompt the user for it if no argument is provided. The string &lt;&gt; can be supplied to mean an empty username.
</dd><dt>-ap, --auth-password [password]
</dt><dd> Provide the password to be used for authentication, or prompt the user for it if no argument is provided. The string &lt;&gt; can be supplied to mean an empty password.
</dd><dt>-ae, --auth-extra [KEYWORD=value[,...]]
</dt><dd> Some of the authentication types allow extra information to be included in the authentication process. Rather than add a new option for every nook and cranny of each authenticator, the --auth-extra option allows this information to be supplied. 

 The following table lists the currently recognized keywords and the authenticators that use them
</dd><dl>
<dl>
<dt>realm, domain
</dt><dd> The realm and domain keywords are synonymous. Using either will set the ``domain'' option in NTLM/MSN/SPA and the ``realm'' option in DIGEST-MD5
</dd><dt>dmd5-serv-type
</dt><dd> The dmd5-serv-type keyword is used by the DIGEST-MD5 authenticator and is used, in part, to build the digest-uri-value string (see RFC2831)
</dd><dt>dmd5-host
</dt><dd> The dmd5-host keyword is used by the DIGEST-MD5 authenticator and is used, in part, to build the digest-uri-value string (see RFC2831)
</dd><dt>dmd5-serv-name
</dt><dd> The dmd5-serv-name keyword is used by the DIGEST-MD5 authenticator and is used, in part, to build the digest-uri-value string (see RFC2831)</dd></dl>
</dl>

<dl>
</dl>

<dt>-am, --auth-map [auth-alias=auth-type[,...]]
</dt><dd> Provides a way to map alternate names onto base authentication types. Useful for any sites that use alternate names for common types. This functionality is actually used internally to map types SPA and MSN onto the base type NTLM.  The command line argument to simulate this would be ``--auth-map SPA=NTLM,MSN=NTLM''. All of the auth-types listed above are valid targets for mapping except SPA and MSN.
</dd><dt>-apt, --auth-plaintext
</dt><dd> Instead of showing AUTH strings base64 encoded as they are transmitted, translate them to plaintext before printing on screen.
</dd><dt>-ahp, --auth-hide-password [replacement string]
</dt><dd> If this option is specified, any time a readable password would be printed to the terminal (specifically AUTH PLAIN and AUTH LOGIN) the password is replaced with a dummy string (or the contents of ``replacement string'' if provided). The dummy string will be base64 encoded or not contingent on the --auth-plaintext option. 

 Note that --auth-hide-password is similar, but not identical, to the --protect-prompt option. The former protects passwords from being displayed in the SMTP transaction regardless of how they are entered. The latter protects sensitive strings when the user types them at the terminal, regardless of how the string would be used.</dd></dl>

<h2>XCLIENT OPTIONS</h2>

 XCLIENT is an SMTP extension introduced by the Postfix project. XCLIENT allows a (properly-authorized) client to tell a server to use alternate information, such as IP address or hostname, for the client. This allows much easier paths for testing mail server configurations. Full details on the protocol are available at <a rel="nofollow" HREF="http://www.postfix.org/XCLIENT_README.html.">http://www.postfix.org/XCLIENT_README.html.</a>
<dl>
<dt>--xclient-addr [VALUE]
</dt><dd>
</dd><dt>--xclient-name [VALUE]
</dt><dd>
</dd><dt>--xclient-port [VALUE]
</dt><dd>
</dd><dt>--xclient-proto [VALUE]
</dt><dd>
</dd><dt>--xclient-helo [VALUE]
</dt><dd>
</dd><dt>--xclient-login [VALUE]
</dt><dd>
</dd><dt>--xclient-reverse-name [VALUE]
</dt><dd> These options specify XCLIENT attrubutes that should be sent to the target server. If [VALUE] is not provided, swaks will prompt and read the value on STDIN.  See <a rel="nofollow" HREF="http://www.postfix.org/XCLIENT_README.html">http://www.postfix.org/XCLIENT_README.html</a> for official documentation for what the attributes mean and their possible values, including the special ``[UNAVAILABLE]'' and ``[TEMPUNAVAIL]'' values. 
 By way of simple example, setting ``--xclient-name foo.example.com --xclient-addr 192.168.1.1'' will cause swaks to send the SMTP command ``XCLIENT NAME=foo.example.com ADDR=192.168.1.1''. 
 Note that the ``REVERSE_NAME'' attribute doesn't seem to appear in the official documentation. There is a mailing list thread that documents it, viewable at <a rel="nofollow" HREF="http://comments.gmane.org/gmane.mail.postfix.user/192623.">http://comments.gmane.org/gmane.mail.postfix.user/192623.</a> 
 These options can all be mixed with each other, and can be mixed with the --xclient option (see below).
</dd><dt>--xclient [XCLIENT_STRING]
</dt><dd> This is the ``free form'' XCLIENT option. Whatever value is provided for XCLIENT_STRING will be sent verbatim as the argument to the XCLIENT smtp command. For example, if ``--xclient 'NAME= ADDR=192.168.1.1 FOO=bar''' is used, swaks will send the SMTP command ``XCLIENT NAME= ADDR=192.168.1.1 FOO=bar''. If no XCLIENT_STRING is passed on command line, swaks will prompt and read the value on STDIN. 
 The primary advantage to this over the more specific options above is that there is no XCLIENT syntax validation here. This allows you to send invalid XCLIENT to the target server for testing. Additionally, at least one MTA (Message Systems' Momentum, formerly ecelerity) implements XCLIENT without advertising supported attributes. The --xclient option allows you to skip the ``supported attributes'' check when communicating with this type of MTA. 
 The --xclient option can be mixed freely with the --xclient-* options above. If ``--xclient-addr 192.168.0.1 --xclient 'FOO=bar NAME=wind''' is given to swaks, ``XCLIENT ADDR=192.168.0.1 FOO=bar NAME=wind'' will be sent to the target server.
</dd><dt>--xclient-optional
</dt><dd>
</dd><dt>--xclient-optional-strict
</dt><dd> In normal operation, setting one of the --xclient* options will cause a successful XCLIENT transaction to take place in order to proceed (that is, XCLIENT needs to be advertised, all the user-requested attributes need to have been advertised, and the server needs to have accepted swaks' XCLIENT request). These options change that behavior. --xclient-optional tells swaks to proceed unconditionally past the XCLIENT stage of the SMTP transaction, regardless of whether it was successful. --xclient-optional-strict is similar but more granular. The strict version will continue to XCLIENT was not advertised, but will fail if XCLIENT was attempted but did not succeed.</dd></dl>

<h2>PROXY OPTIONS</h2>

 Swaks implements the Proxy protocol as defined in <a rel="nofollow" HREF="http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt.">http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt.</a> Proxy allows an application load balancer, such as HAProxy, to be used in front of an MTA while still allowing the MTA access to the originating host information. Proxy support in swaks allows direct testing of an MTA configured to expect requests from a proxy, bypassing the proxy itself during testing. 

 Swaks makes no effort to ensure that the Proxy options used are internally consistant. For instance, --proxy-family (in version 1) is expected to be one of ``TCP4'' or ``TCP6''.  While it will likely not make sense to the target server, swaks makes no attempt to ensure that --proxy-source and --proxy-dest are in the same protocol family as --proxy-family or each other. 

 The --proxy option is mutually exclusive with all other --proxy-* options except --proxy-version. 

 When --proxy is not used, all of --proxy-family, --proxy-source, --proxy-source-port, --proxy-dest, and --proxy-dest-port are required. Additionally, when --proxy-version is 2, --proxy-protocol and --proxy-command are optional.
<dl>
<dt>--proxy-version [ 1 | 2 ]
</dt><dd> Whether to use version 1 (human readable) or version 2 (binary) of the Proxy protocol. Version 1 is the default. Version 2 is only implemented through the ``address block'', and is roughly on par with the information provided in version 1. 
 Note that at the time of release, version 2 has been implemented but not fully tested. Postfix does not implement version 2 and Exim appears to have a bug in version 2 at the time of writing. It does mirror HAProxy's output though.
</dd><dt>--proxy [VALUE]
</dt><dd> If this option is used, its argument is passed unchanged after the ``PROXY '' portion (or the 12 byte protocol header for version 2) of the Proxy exchange. This option allows sending incomplete or malformed Proxy strings to a target server for testing. No attempt to translate or modify this string is made, so if used with ``--proxy-version 2'' the argument should be in the appropriate binary format. This option is mutually exclusive with all other --proxy-* options which provide granular proxy information.
</dd><dt>--proxy-family [VALUE]
</dt><dd> For version 1, specifies both the address family and transport protocol. The protocol defines TCP4 and TCP6. 
 For version 2, specifies only the address family. The protocol defines AF_UNSPEC, AF_INET, AF_INET6, and AF_UNIX.
</dd><dt>--proxy-protocol [VALUE]
</dt><dd> For version 2, specifies the transport protocol. The protocol defines UNSPEC, STREAM, and DGRAM.  The default is STREAM.  This option is unused in version 1
</dd><dt>--proxy-command [VALUE]
</dt><dd> For version 2, specifies the transport protocol. The protocol defines LOCAL and PROXY.  The default is PROXY.  This option is unused in version 1
</dd><dt>--proxy-source [VALUE]
</dt><dd> Specify the source address of the proxied connection.
</dd><dt>--proxy-source-port [VALUE]
</dt><dd> Specify the source port of the proxied connection.
</dd><dt>--proxy-dest [VALUE]
</dt><dd> Specify the destination address of the proxied connection.
</dd><dt>--proxy-dest-port [VALUE]
</dt><dd> Specify the destination port of the proxied connection.</dd></dl>

<h2>DATA OPTIONS</h2>

 These options pertain to the contents for the DATA portion of the SMTP transaction.
<dl>
<dt>-d, --data [data-portion]
</dt><dd> Use argument as the entire contents of DATA, or prompt user if no argument specified. If the argument '-' is provided the data will be read from STDIN.  If any other argument is provided and it represents the name of an open-able file, the contents of the file will be used. Any other argument will be itself for the DATA contents. 
 The value can be on one single line, with \n (ascii 0x5c, 0x6e) representing where line breaks should be placed. Leading dots will be quoted. Closing dot is not required but is allowed. The default value for this option is ``Date: <tt>%DATE</tt>%\nTo: <tt>%TO_ADDRESS</tt>%\nFrom: <tt>%FROM_ADDRESS</tt>%\nSubject: test <tt>%DATE</tt>%\nMessage-Id: &lt;%MESSAGEID%&gt;\nX-Mailer: swaks v%SWAKS_VERSION jetmore.org/john/code/swaks/\n%NEW_HEADERS%\n%BODY%\n''. 
 Very basic token parsing is performed on the DATA portion. See --use-old-data-tokens for details about the single-character tokens marked as deprecated. The following table shows the recognized tokens and their replacement values:
</dd><dl>
<dl>
<dt>%FROM_ADDRESS%
</dt><dd> Replaced with the envelope-sender. Replaces the deprecated <tt>%F</tt> token.
</dd><dt>%TO_ADDRESS%
</dt><dd> Replaced with the envelope-recipient(s). Replaces the deprecated <tt>%T</tt> token.
</dd><dt>%DATE%
</dt><dd> Replaced with the current time in a format suitable for inclusion in the Date: header. Note this attempts to use the standard module Time::Local for timezone calculations. If this module is unavailable the date string will be in GMT.  Replaces the deprecated <tt>%D</tt> token.
</dd><dt>%MESSAGEID%
</dt><dd> Replaced with the a message ID string suitable for use in a Message-Id header. The value for this token will remain consistent for the life of the process.
</dd><dt>%SWAKS_VERSION%
</dt><dd> Replaced with the version of the currently-running Swaks process.
</dd><dt>%NEW_HEADERS%
</dt><dd> Replaced with the contents of the --add-header option. If --add-header is not specified this token is simply removed. Replaces the deprecated <tt>%H</tt> token.
</dd><dt>%BODY%
</dt><dd> Replaced with the value specified by the --body option. See --body for default. Replaces the deprecated <tt>%H</tt> token.</dd></dl>
</dl>

<dl>
</dl>

<dt>--use-old-data-tokens
</dt><dd> In previous versions of swaks the DATA tokens as described in the --data option above used single-character tokens (e.g., <tt>%F</tt>). These were not a great choice for default tokens, and proved especially troublesome with encoded, non-english languages where these character combinations might be common. The single-character tokens were replaced with the slightly-less-error-prone versions listed above. The retention of the old tokens and the inclusion of this option to activate them are intended as a temporary aid to users who have an existing message corpus using the old tokens. The single-character tokens and the --use-old-data-tokens option should be considered deprecated and likely to be removed in the next release.
</dd><dt>-dab, --dump-as-body
</dt><dd> If --dump-as-body is used and no other option is used to changed the default body of the message, the body is replaced with output similar to the output of what is provided by --dump. --dump's initial program capability stanza is not displayed, and the ``data'' section is not included. Additionally, --dump always includes passwords. By default --dump-as-body does not include passwords, though this can be changed with --dump-as-body-shows-password.
</dd><dt>-dabsp, --dump-as-body-shows-password
</dt><dd> Cause --dump-as-body to include plaintext passwords. This option is not recommended. This option implies --dump-as-body.
</dd><dt>--body [body-specification]
</dt><dd> Specify the body of the email. The default is ``This is a test mailing''. If no argument to --body is given, prompt to supply one interactively. If '-' is supplied, the body will be read from standard input. If any other text is provided and the text represents an open-able file, the content of that file is used as the body. If it does not represent an open-able file, the text itself is used as the body. 

 If the message is forced to MIME format (see --attach) the argument to this option will be included unencoded as the first MIME part. Its content-type will always be text/plain.
</dd><dt>--attach [attachment-specification]
</dt><dd> When one or more --attach option is supplied, the message is changed into a multipart/mixed MIME message. The arguments to --attach are processed the same as --body with regard to stdin, file contents, etc. --attach can be supplied multiple times to create multiple attachments. By default each attachment is attached as a application/octet-stream file. See --attach-type for changing this behavior. 

 If a filename is specified, the MIME encoding will include that file name. See --attach-name for more detail on file naming. 

 It is legal for '-' (STDIN) to be specified as an argument multiple times (once for --body and multiple times for --attach). In this case, the same content will be attached each time it is specified. This is useful for attaching the same content with multiple MIME types.
</dd><dt>--attach-type [mime-type]
</dt><dd> By default, content that gets MIME attached to a message with the --attach option is encoded as application/octet-stream. --attach-type changes the mime type for every --attach option which follows it. It can be specified multiple times.
</dd><dt>--attach-name [name]
</dt><dd> This option sets the filename that will be included in the MIME part created for the next --attach option. If no argument is set for this option, it causes no filename information to be included for the next MIME part, even if swaks could generate it from the local file name.
</dd><dt>-ah, --add-header [header]
</dt><dd> This option allows headers to be added to the DATA.  If <tt>%H</tt> is present in the DATA it is replaced with the argument to this option. If <tt>%H</tt> is not present, the argument is inserted between the first two consecutive newlines in the DATA (that is, it is inserted at the end of the existing headers). 

 The option can either be specified multiple times or a single time with multiple headers separated by a literal '\n' string. So, ``--add-header 'Foo: bar' --add-header 'Baz: foo''' and ``--add-header 'Foo: bar\nBaz: foo''' end up adding the same two headers.
</dd><dt>--header [header-and-data], --h-Header [data]
</dt><dd> These options allow a way to change headers that already exist in the DATA. '--header ``Subject: foo''' and '--h-Subject foo' are equivalent. If the header does not already exist in the data then this argument behaves identically to --add-header. However, if the header already exists it is replaced with the one specified.
</dd><dt>-g
</dt><dd> If specified, swaks will read the DATA value for the mail from STDIN.  This is equivalent to ``--data -''. If there is a From_ line in the email, it will be removed (but see -nsf option). Useful for delivering real message (stored in files) instead of using example messages.
</dd><dt>--no-data-fixup, -ndf
</dt><dd> This option forces swaks to do no massaging of the DATA portion of the email. This includes token replacement, From_ stripping, trailing-dot addition, --body/attachment inclusion, and any header additions. This option is really only useful when used with --data, since the internal default DATA portion uses tokens.
</dd><dt>--no-strip-from, -nsf
</dt><dd> Don't strip the From_ line from the DATA portion, if present.</dd></dl>

<h2>OUTPUT OPTIONS</h2>

 By default swaks provides a transcript of its transactions to its caller (STDOUT/STDERR). This transcript aims to be as faithful a representation as possible of the transaction though it does modify this output by adding informational prefixes to lines and by providing plaintext versions of TLS transactions 

 The ``informational prefixes'' are referred to as transaction hints. These hints are initially composed of those marking lines that are output of swaks itself, either informational or error messages, and those that indicate a line of data actually sent or received in a transaction. This table indicates the hints and their meanings:
<dl>
<dt>&quot;===&quot;
</dt><dd> Indicates an informational line generated by swaks
</dd><dt>&quot;***&quot;
</dt><dd> Indicates an error generated within swaks
</dd><dt>&quot;&nbsp;<wbr>-&gt;&quot;
</dt><dd> Indicates an expected line sent by swaks to target server
</dd><dt>&quot;&nbsp;<wbr>~&gt;&quot;
</dt><dd> Indicates a TLS-encrypted, expected line sent by swaks to target server
</dd><dt>&quot;**&gt;&quot;
</dt><dd> Indicates an unexpected line sent by swaks to the target server
</dd><dt>&quot;*~&gt;&quot;
</dt><dd> Indicates a TLS-encrypted, unexpected line sent by swaks to target server
</dd><dt>&quot;&nbsp;<wbr>&nbsp;<wbr>&gt;&quot;
</dt><dd> Indicates a raw chunk of text sent by swaks to a target server (see --show-raw-text). There is no concept of ``expected'' or ``unexpected'' at this level.
</dd><dt>&quot;&lt;-&nbsp;<wbr>&quot;
</dt><dd> Indicates an expected line sent by target server to swaks
</dd><dt>&quot;&lt;~&nbsp;<wbr>&quot;
</dt><dd> Indicates a TLS-encrypted, expected line sent by target server to swaks
</dd><dt>&quot;&lt;**&quot;
</dt><dd> Indicates an unexpected line sent by target server to swaks
</dd><dt>&quot;&lt;~*&quot;
</dt><dd> Indicates a TLS-encrypted, unexpected line sent by target server to swaks
</dd><dt>&quot;&lt;&nbsp;<wbr>&nbsp;<wbr>&quot;
</dt><dd> Indicates a raw chunk of text received by swaks from a target server (see --show-raw-text). There is no concept of ``expected'' or ``unexpected'' at this level.</dd></dl>
 

 The following options control what and how output is displayed to the caller.
<dl>
<dt>-n, --suppress-data
</dt><dd> Summarizes the DATA portion of the SMTP transaction instead of printing every line. This option is very helpful, bordering on required, when using swaks to send certain test emails. Emails with attachments, for instance, will quickly overwhelm a terminal if the DATA is not supressed.
</dd><dt>-stl, --show-time-lapse [i]
</dt><dd> Display time lapse between send/receive pairs. This option is most useful when Time::HiRes is available, in which case the time lapse will be displayed in thousandths of a second. If Time::HiRes is unavailable or ``i'' is given as an argument the lapse will be displayed in integer seconds only.
</dd><dt>-nih, --no-info-hints
</dt><dd> Don't display the transaction hint for informational transactions. This is most useful when needing to copy some portiong of the informational lines, for instance the certificate output from --tls-get-peer-cert.
</dd><dt>-nsh, --no-send-hints
</dt><dd>
</dd><dt>-nrh, --no-receive-hints
</dt><dd>
</dd><dt>-nth, --no-hints
</dt><dd> --no-send-hints and --no-receive-hints supress the transaction prefix from send and receive lines, respectively. This is often useful when copying some portion of the transaction for use elsewhere (for instance, ``--no-send-hints --hide-receive --hide-informational'' is a useful way to get only the client-side commands for a given transaction). --no-hints is identical to specifying both --no-send-hints and --no-receive-hints. 
 Don't show transaction hints (useful in conjunction with -hr to create copy/paste-able transactions).
</dd><dt>-raw, --show-raw-text
</dt><dd> This option will print a hex dump of raw data sent and received by swaks. Each hex dump is the contents of a single read or write on the network. This should be identical to what is already being displayed (with the exception of the \r characters being removed). This option is useful in seeing details when servers are sending lots of data in single packets, or breaking up individual lines into multiple packets. If you really need to go in depth in that area you're probably better with a packet sniffer, but this option is a good first step to seeing odd connection issues.
</dd><dt>--output-file &lt;/path/to/file&gt;
</dt><dd>
</dd><dt>--output-file-stdout &lt;/path/to/file&gt;
</dt><dd>
</dd><dt>--output-file-stderr &lt;/path/to/file&gt;
</dt><dd> These options allow the user to send output to files instead of stdout/stderr. The first option sends both to the same file. The arguments of &amp;STDOUT and &amp;STDERR are treated specially, refering to the ``normal'' file handles, so ``--output-file-stderr '&amp;STDOUT''' would redirect STDERR to STDOUT.
</dd><dt>-pp, --protect-prompt
</dt><dd> Don't echo user input on prompts that are potentially sensitive (right now only authentication password). See also --auth-hide-password
</dd><dt>-hr, --hide-receive
</dt><dd> Don't display lines sent from the remote server being received by swaks
</dd><dt>-hs, --hide-send
</dt><dd> Don't display lines being sent by swaks to the remote server
</dd><dt>-hi, --hide-informational
</dt><dd> Don't display non-error informational lines from swaks itself.
</dd><dt>-ha, --hide-all
</dt><dd> Do not display any content to the terminal.
</dd><dt>-S, --silent [level]
</dt><dd> Cause swaks to be silent. If no argument is given or if an argument of ``1'' is given, print no output unless/until an error occurs, after which all output is shown. If an argument of ``2'' is given, only print errors. If ``3'' is given, show no output ever.
</dd><dt>--support
</dt><dd> Print capabilities and exit. Certain features require non-standard perl modules. This options evaluates whether these modules are present and displays which functionality is available and which isn't, and which modules would need to be added to gain the missing functionality.
</dd><dt>--dump
</dt><dd> This option causes swaks to print the results of option processing, immediately before mail would have been sent. No mail will be sent when --dump is used. Note that --dump is considered to be a pure self-diagnosis tool and no effort is made or will ever be made to mask passwords in the --dump output.
</dd><dt>--help
</dt><dd> Display this help information.
</dd><dt>--version
</dt><dd> Display version information.</dd></dl>

<h2>PORTABILITY</h2>

<dl>
<dt>OPERATING SYSTEMS
</dt><dd> This program was primarily intended for use on unix-like operating systems, and it should work on any reasonable version thereof. It has been developed and tested on Solaris, Linux, and Mac OS X and is feature complete on all of these. 
 This program is known to demonstrate basic functionality on Windows using ActiveState's Perl. It has not been fully tested. Known to work are basic SMTP functionality and the LOGIN, PLAIN, and CRAM-MD5 auth types. Unknown is any TLS functionality and the NTLM/SPA and DIGEST-MD5 auth types. 
 Because this program should work anywhere Perl works, I would appreciate knowing about any new operating systems you've thoroughly used swaks on as well as any problems encountered on a new OS.
</dd><dt>MAIL SERVERS
</dt><dd> This program was almost exclusively developed against Exim mail servers. It was been used casually by the author, though not thoroughly tested, with Sendmail, Smail, Exchange, Oracle Collaboration Suite, qpsmtpd, and Communigate. Because all functionality in swaks is based off of known standards it should work with any fairly modern mail server. If a problem is found, please alert the author at the address below.</dd></dl>

<h2>EXIT CODES</h2>

<dl>
<dt>0
</dt><dd> no errors occurred
</dd><dt>1
</dt><dd> error parsing command line options
</dd><dt>2
</dt><dd> error connecting to remote server
</dd><dt>3
</dt><dd> unknown connection type
</dd><dt>4
</dt><dd> while running with connection type of ``pipe'', fatal problem writing to or reading from the child process
</dd><dt>5
</dt><dd> while running with connection type of ``pipe'', child process died unexpectedly. This can mean that the program specified with --pipe doesn't exist.
</dd><dt>6
</dt><dd> Connection closed unexpectedly. If the close is detected in response to the 'QUIT' swaks sends following an unexpected response, the error code for that unexpected response is used instead. For instance, if a mail server returns a 550 response to a MAIL FROM: and then immediately closes the connection, swaks detects that the connection is closed, but uses the more specific exit code 23 to detail the nature of the failure. If instead the server return a 250 code and then immediately closes the connection, swaks will use the exit code 6 because there is not a more specific exit code.
</dd><dt>10
</dt><dd> error in prerequisites (needed module not available)
</dd><dt>21
</dt><dd> error reading initial banner from server
</dd><dt>22
</dt><dd> error in HELO transaction
</dd><dt>23
</dt><dd> error in MAIL transaction
</dd><dt>24
</dt><dd> no RCPTs accepted
</dd><dt>25
</dt><dd> server returned error to DATA request
</dd><dt>26
</dt><dd> server did not accept mail following data
</dd><dt>27
</dt><dd> server returned error after normal-session quit request
</dd><dt>28
</dt><dd> error in AUTH transaction
</dd><dt>29
</dt><dd> error in TLS transaction
</dd><dt>30
</dt><dd> PRDR requested/required but not advertised
</dd><dt>32
</dt><dd> error in EHLO following TLS negotiation
</dd><dt>33
</dt><dd> error in XCLIENT transaction
</dd><dt>34
</dt><dd> error in EHLO following XCLIENT
</dd><dt>35
</dt><dd> error in PROXY option processing
</dd><dt>36
</dt><dd> error sending PROXY banner</dd></dl>

<h2>ABOUT THE NAME</h2>

 The name ``swaks'' is a (sort-of) acronym for ``SWiss Army Knife Smtp''. It was chosen to be fairly distinct and pronounceable. While ``swaks'' is unique as the name of a software package, it has some other, non-software meanings. Please send in other uses of ``swak'' or ``swaks'' for inclusion.
<dl>
<dt>&quot;Sealed With A Kiss&quot;
</dt><dd> SWAK/SWAKs turns up occasionally on the internet with the meaning ``with love''.
</dd><dt>bad / poor / ill (Afrikaans)
</dt><dd> Seen in the headline ``SA se bes en swaks gekledes in 2011'', which was translated as ``best and worst dressed'' by native speakers. Google Translate doesn't like ``swaks gekledes'', but it will translate ``swak'' as ``poor'' and ``swak geklede'' as ``ill-dressed''.</dd></dl>

<h2>CONTACT</h2>

<dl>
<dt>proj-swaks [at] jetmore.net
</dt><dd> Please use this address for general contact, questions, patches, requests, etc.
</dd><dt>updates-swaks [at] jetmore.net
</dt><dd> If you would like to be put on a list to receive notifications when a new version of swaks is released, please send an email to this address.
</dd><dt><a rel="nofollow" HREF="http://www.jetmore.org/john/code/swaks/">http://www.jetmore.org/john/code/swaks/</a>
</dt><dd> Change logs, this help, and the latest version is found at this link. 
</dd></dl>
