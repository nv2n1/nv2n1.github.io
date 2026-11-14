---
title: "mimedefang-filter(5)"
name: "mimedefang-filter"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mimedefang-filter/"
description: "mimedefang-filter – Configuration file for MIMEDefang mail filter."
---

<p>mimedefang-filter &#8211; Configuration file for MIMEDefang mail filter.</p>
<h2>Description</h2>
<p><code>mimedefang-filter</code> is a Perl fragment that controls how <code>mimedefang.pl</code> disposes of various parts of a MIME message. In addition, it contains some global variable settings that affect the operation of <code>mimedefang.pl</code>. </p>
<h2>Calling Sequence</h2>
<p>Incoming messages are scanned as follows: </p>
<p> 1) A temporary working directory is created. It is made the current working directory and the e-mail message is split into parts in this directory. Each part is represented internally as an instance of MIME::Entity. </p>
<p> 2) If the file <code>/etc/mail/mimedefang-filter.pl</code> defines a Perl function called <code>filter_begin</code>, it is called with a single argument consisting of a MIME::Entity representing the parsed e-mail message. Any return value is ignored. </p>
<p> 3) For each <i>leaf</i> part of the mail message, <code>filter</code> is called with four arguments: <code>entity</code>, a MIME::Entity object; <code>fname</code>, the suggested filename taken from the MIME Content-Disposition header; <code>ext</code>, the file extension, and <code>type</code>, the MIME Content-Type value. For each <i>non-leaf</i> part of the mail message, <code>filter_multipart</code> is called with the same four arguments as <code>filter</code>. A non-leaf part of a message is a part that contains nested parts. Such a part has no useful body, but you should <i>still perform filename checks</i> to check for viruses that use malformed MIME to masquerade as non-leaf parts (like message/rfc822). In general, any action you perform in <code>filter_multipart</code> applies to the part itself <i>and</i> any contained parts. </p>
<p> Note that both <code>filter</code> and <code>filter_multipart</code> are optional. If you do not define them, a default function that simply accepts each part is used. </p>
<p> 4) After all parts have been processed, the function <code>filter_end</code> is called if it has been defined. It is passed a single argument consisting of the (possibly modified) MIME::Entity object representing the message about to be delivered. Within <code>filter_end</code>, you can call functions that modify the message headers body. </p>
<p> 5) After <code>filter_end</code> returns, the function <code>filter_wrapup</code> is called if it has been defined. It is passed a single argument consisting of the (possibly modified) MIME::Entity object representing the message about to be delivered, including any modifications made in <code>filter_end</code>. Within <code>filter_wrapup</code>, you can <i>not</i> call functions that modify the message body, but you can still add or modify message headers.</p>
<h2>Disposition</h2>
<p><code>mimedefang.pl</code> examines each part of the MIME message and chooses a <i>disposition</i> for that part. (A disposition is selected by calling one of the following functions from <code>filter</code> and then immediately returning.) Available dispositions are: </p>
<dl>
<dt><code>action_accept</code></p>
<dd>The part is passed through unchanged. If no disposition function is returned, this is the default. </p>
<dt><code>action_accept_with_warning</code></p>
<dd>The part is passed through unchanged, but a warning is added to the mail message. </p>
<dt><code>action_drop</code></p>
<dd>The part is deleted without any notification to the recipients. </p>
<dt><code>action_drop_with_warning</code></p>
<dd>The part is deleted and a warning is added to the mail message. </p>
<dt><code>action_replace_with_warning</code></p>
<dd>The part is deleted and instead replaced with a text message. </p>
<dt><code>action_quarantine</code></p>
<dd>The part is deleted and a warning is added to the mail message. In addition, a copy of the part is saved on the mail server in the directory /var/spool/MD-Quarantine and a notification is sent to the MIMEDefang administrator. </p>
<dt><code>action_bounce</code></p>
<dd>The entire e-mail message is rejected and an error returned to the sender. The intended recipients are not notified. Note that in spite of the name, MIMEDefang does <i>not</i> generate and e-mail a failure notification. Rather, it causes the SMTP server to return a 5<i>XX</i> SMTP failure code. </p>
<dt><code>action_discard</code></p>
<dd>The entire e-mail message is discarded silently. Neither the sender nor the intended recipients are notified. </p>
</dl>
<h2>Controlling Relaying</h2>
<p>You can define a function called <code>filter_relay</code> in your filter. This lets you reject SMTP connection attempts early on in the SMTP dialog, rather than waiting until the whole message has been sent. Note that for this check to take place, you must use the -r flag with <code>mimedefang</code>. </p>
<p> <code>filter_relay</code> is passed five arguments: $hostip is the IP address of the relay host (for example, &quot;127.0.0.1&quot;), $hostname is the host name if known (for example, &quot;localhost.localdomain&quot;). If the host name could not be determined, $hostname is $hostip enclosed in square brackets. (That is, (&quot;$hostname&quot; eq &quot;[$hostip]&quot;) will be true.) </p>
<p> The remaining three arguments to <code>filter_relay</code> are $port, $myip and $myport which contain the client&#8217;s TCP port, the Sendmail daemon&#8217;s listening IP address and the Sendmail daemon&#8217;s listening port. </p>
<p> <code>filter_relay</code> must return a two-element list: ($code, $msg). $msg specifies the text message to use for the SMTP reply, but because of limitations in the Milter API, this message is for documentation purposes only&#8212;you cannot set the text of the SMTP message returned to the SMTP client from <code>filter_relay</code>. </p>
<p> $code is a literal string, and can have one of the following values: </p>
<dl>
<dt><code>&#8216;REJECT&#8217;</code></p>
<dd>if the connection should be rejected. </p>
<dt><code>&#8216;CONTINUE&#8217;</code></p>
<dd>if the connection should be accepted. </p>
<dt><code>&#8216;TEMPFAIL&#8217;</code></p>
<dd>if a temporary failure code should be returned. </p>
<dt><code>&#8216;DISCARD&#8217;</code></p>
<dd>if the message should be accepted and silently discarded. </p>
<dt><code>&#8216;ACCEPT_AND_NO_MORE_FILTERING&#8217;</code></p>
<dd>if the connection should be accepted <i>and no further filtering done</i>. </p>
</dl>
<p> Earlier versions of MIMEDefang used -1 for TEMPFAIL, 0 for REJECT and 1 for CONTINUE. These values still work, but are deprecated. </p>
<p> In the case of REJECT or TEMPFAIL, $msg specifies the text part of the SMTP reply. $msg <i>must not</i> contain newlines. </p>
<p> For example, if you wish to reject connection attempts from any machine in the spammer.com domain, you could use this function: </p>
<pre>sub filter_relay {
 my ($ip, $name) = @_;
 if ($name =~ /spammer\.com$/) {
 return ('REJECT', &quot;Sorry; spammer.com is blacklisted&quot;);
 }
 return ('CONTINUE', &quot;ok&quot;);
}</pre>
<h2>Filtering By Helo</h2>
<p>You can define a function called <code>filter_helo</code> in your filter. This lets you reject connections after the HELO/EHLO SMTP command. Note that for this function to be called, you must use the -H flag with <code>mimedefang</code>. </p>
<p> <code>filter_helo</code> is passed six arguments: $ip and $name are the IP address and name of the sending relay, as in <code>filter_relay</code>. The third argument, $helo, is the argument supplied in the HELO/EHLO command. </p>
<p> The remaining three arguments to <code>filter_relay</code> are $port, $myip and $myport which contain the client&#8217;s TCP port, the Sendmail daemon&#8217;s listening IP address and the Sendmail daemon&#8217;s listening port. </p>
<p> <code>filter_helo</code> must return a two-to-five element list: ($code, $msg, $smtp_code, $smtp_dsn, $delay). $code is a return code, with the same meaning as the $code return from <code>filter_relay</code>. $msg specifies the text message to use for the SMTP reply. If $smtp_code and $smtp_dsn are supplied, they become the SMTP numerical reply code and the enhanced status delivery code (DSN code). If they are not supplied, sensible defaults are used. $delay specifies a delay in seconds; the C milter code will sleep for $delay seconds before returning the reply to Sendmail. $delay defaults to zero. </p>
<p> (Note that the delay is implemented in the Milter C code; if you specify a delay of 30 seconds, that doesn&#8217;t mean a Perl slave is tied up for the duration of the delay. The delay only costs one Milter thread.)</p>
<h2>Filtering By Sender</h2>
<p>You can define a function called <code>filter_sender</code> in your filter. This lets you reject messages from certain senders, rather than waiting until the whole message has been sent. Note that for this check to take place, you must use the -s flag with <code>mimedefang</code>. </p>
<p> <code>filter_sender</code> is passed four arguments: $sender is the envelope e-mail address of the sender (for example, &quot;&lt;dfs [at] roaringpenguin.com&gt;&quot;). The address may or may not be surrounded by angle brackets. $ip and $name are the IP address and host name of the SMTP relay. Finally, $helo is the argument to the SMTP &quot;HELO&quot; command. </p>
<p> Inside <code>filter_sender</code>, you can access any ESMTP arguments (such as &quot;SIZE=12345&quot;) in the array @ESMTPArgs. Each ESMTP argument occupies one array element. </p>
<p> <code>filter_sender</code> must return a two-to-five element list, with the same meaning as the return value from <code>filter_helo</code>. </p>
<p> For example, if you wish to reject messages from spammer [at] badguy.com, you could use this function: </p>
<pre>sub filter_sender {
 my ($sender, $ip, $hostname, $helo) = @_;
 if ($sender =~ /^&lt;?spammer\@badguy\.com&gt;?$/i) {
 return ('REJECT', 'Sorry; spammer [at] badguy.com is blacklisted.');
 }
 return ('CONTINUE', &quot;ok&quot;);
}</pre>
<p>As another example, some spammers identify their own machine as your machine in the SMTP &quot;HELO&quot; command. This function rejects a machine claiming to be in the &quot;roaringpenguin.com&quot; domain unless it really is a Roaring Penguin machine: </p>
<pre>sub filter_sender {
 my($sender, $ip, $hostname, $helo) = @_;
 if ($helo =~ /roaringpenguin.com/i) {
 if ($ip ne &quot;127.0.0.1&quot; and
 $ip ne &quot;216.191.236.23&quot; and
 $ip ne &quot;216.191.236.30&quot;) {
 return('REJECT', &quot;Go away... $ip is not in roaringpenguin.com&quot;);
 }
 }
 return ('CONTINUE', &quot;ok&quot;);
}</pre>
<p>As a third example, you may wish to prevent spoofs by requiring SMTP authentication when email is sent from some email addresses. This function rejects mail from &quot;king [at] example.com&quot;, unless the connecting user properly authenticated as &quot;elvisp&quot;. Note that this needs access to the %SendmailMacros global, that is not available in filter_sender until after a call to <code>read_commands_file</code>. </p>
<pre>sub filter_sender {
 my($sender, $ip, $hostname, $helo) = @_;
 read_commands_file();
 ### notice: This assumes The King uses authentication without realm!
 if ($sender =~ /^&lt;?king\@example\.com&gt;?$/i and
 $SendmailMacros{auth_authen} ne &quot;elvisp&quot;) {
 return('REJECT', &quot;Faking mail from the king is not allowed.&quot;);
 }
 return ('CONTINUE', &quot;ok&quot;);
}</pre>
<h2>Filtering By Recipient</h2>
<p>You can define a function called <code>filter_recipient</code> in your filter. This lets you reject messages to certain recipients, rather than waiting until the whole message has been sent. Note that for this check to take place, you must use the -t flag with <code>mimedefang</code>. </p>
<p> <code>filter_recipient</code> is passed nine arguments: $recipient is the envelope address of the recipient and $sender is the envelope e-mail address of the sender (for example, &quot;&lt;dfs [at] roaringpenguin.com&gt;&quot;). The addresses may or may not be surrounded by angle brackets. $ip and $name are the IP address and host name of the SMTP relay. $first is the envelope address of the <i>first</i> recipient for this message, and $helo is the argument to the SMTP &quot;HELO&quot; command. The last three arguments, $rcpt_mailer, $rcpt_host and $rcpt_addr are the Sendmail mailer, host and address triple for the recipient address. For example, for local recipients, $rcpt_mailer is likely to be &quot;local&quot;, while for remote recipients, it is likely to be &quot;esmtp&quot;. </p>
<p> Inside <code>filter_recipient</code>, you can access any ESMTP arguments (such as &quot;NOTIFY=never&quot;) in the array @ESMTPArgs. Each ESMTP argument occupies one array element. </p>
<p> <code>filter_recipient</code> must return a two-to-five element list whose interpretation is the same as for <code>filter_sender</code>. Note, however, that if <code>filter_recipient</code> returns &#8216;DISCARD&#8217;, then the entire message for <i>all</i> recipients is discarded. (It doesn&#8217;t really make sense, but that&#8217;s how Milter works.) </p>
<p> For example, if you wish to reject messages from spammer [at] badguy.com, unless they are to postmaster [at] mydomain.com, you could use this function: </p>
<pre>sub filter_recipient {
 my ($recipient, $sender, $ip, $hostname, $first, $helo,
 $rcpt_mailer, $rcpt_host, $rcpt_addr) = @_;
 if ($sender =~ /^&lt;?spammer\@badguy\.com&gt;?$/i) {
 if ($recipient =~ /^&lt;?postmaster\@mydomain\.com&gt;?$/i) {
 return ('CONTINUE', &quot;ok&quot;);
 }
 return ('REJECT', 'Sorry; spammer [at] badguy.com is blacklisted.');
 }
 return ('CONTINUE', &quot;ok&quot;);
}</pre>
<h2>Initialization And Cleanup</h2>
<p>Just before a slave begins processing messages, <code>mimedefang.pl</code> calls the functions <code>filter_initialize</code> (if it is defined) with no arguments. By the time <code>filter_initialize</code> is called, all the other initialization (such as setting up syslog facility and priority) has been done. </p>
<p> If you are not using an embedded Perl interpreter, then performing an action inside <code>filter_initialize</code> is practically the same as performing it directly in the filter file, outside any function definition. However, if you are using an embedded Perl interpreter, then anything you call directly from outside a function definition is executed <i>once only</i> in the parent process. Anything in <code>filter_initialize</code> is executed <i>once per slave</i>. If you use any code that opens a descriptor (for example, a connection to a database server), you <i>must</i> run that code inside <code>filter_initialize</code> and not directly from the filter, because the multiplexor closes all open descriptors when it activates a new slave. </p>
<p> When a slave is about to exit, <code>mimedefang.pl</code> calls the function <code>filter_cleanup</code> (if it is defined) with no arguments. This function can do whatever cleanup you like, such as closing file descriptors and cleaning up long-lived slave resources. The return value from <code>filter_cleanup</code> becomes the slave&#8217;s exit status. (You should therefore ensure that <code>filter_cleanup</code> returns an integer suitable for a process exit status.) </p>
<p> If <code>filter_cleanup</code> takes longer than 10 seconds to run, the slave is sent a SIGTERM signal. If that doesn&#8217;t kill it (because you&#8217;re catching signals, perhaps), then a further 10 seconds later, the slave is sent a SIGKILL signal.</p>
<h2>Controlling Parsing</h2>
<p>If you define a function called <code>filter_create_parser</code> taking no arguments, then <code>mimedefang.pl</code> will call it to create a MIME::Parser object for parsing mail messages. </p>
<p> <code>Filter_create_parser</code> is expected to return a MIME::Parser object (or an instance of a class derived from MIME::Parser). </p>
<p> You can use <code>filter_create_parser</code> to change the behavior of the MIME::Parser used by <code>mimedefang.pl</code>. </p>
<p> If you do not define a <code>filter_create_parser</code> function, then a built-in version equivalent to this is used: </p>
<pre> sub filter_create_parser () {
 my $parser = MIME::Parser-&gt;new();
 $parser-&gt;<a href="//www.systutorials.com/docs/linux/man/1-extract_nested_messages/">extract_nested_messages</a>(1);
 $parser-&gt;<a href="//www.systutorials.com/docs/linux/man/1-extract_uuencode/">extract_uuencode</a>(1);
 $parser-&gt;output_to_core(0);
 $parser-&gt;tmp_to_core(0);
 return $parser;
 }</pre>
<h2>Extending Mimedefang</h2>
<p>The man page for <code><a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a></code>(7) lists commands that are passed to slaves in server mode (see &quot;SERVER COMMANDS&quot;.) You can define a function called <code>filter_unknown_cmd</code> to extend the set of commands your filter can handle. </p>
<p> If you define <code>filter_unknown_cmd</code>, it is passed the unknown command as a single argument. It should return a list of values as follows: The first element of the list must be either &quot;ok&quot; or &quot;error:&quot; (with the colon.) The remaining arguments are percent-encoded. All the resulting pieces are joined together with a single space between them, and the resulting string passed back as the reply to the multiplexor. </p>
<p> For example, the following function will make your filter reply to a &quot;PING&quot; command with &quot;PONG&quot;: </p>
<pre>sub filter_unknown_cmd ($) {
 my($cmd) = @_;
 if ($cmd eq &quot;PING&quot;) {
 return(&quot;ok&quot;, &quot;PONG&quot;);
 }
 return(&quot;error:&quot;, &quot;Unknown command&quot;);
}</pre>
<p>You can test this filter by typing the following as root: </p>
<pre>md-mx-ctrl PING</pre>
<p>The response should be: </p>
<pre>ok PONG</pre>
<p>If you extend the set of commands using <code>filter_unknown_cmd</code>, you should make all your commands start with an upper-case letter to avoid clashes with future built-in commands.</p>
<h2>Rejecting Unknown Users Early</h2>
<p>A very common mail setup is to have a MIMEDefang machine act as an SMTP proxy, accepting and scanning mail and then relaying it to the real mail server. Unfortunately, this means that the MIMEDefang machine cannot know if a local address is valid or not, and will forward all mail for the appropriate domains. If a mail comes in for an unknown user, the MIMEDefang machine will be forced to generate a bounce message when it tries to relay the mail. </p>
<p> It&#8217;s often desirable to have the MIMEDefang host reply with a &quot;User unknown&quot; SMTP response directly. While this can be done by copying the list of local users to the MIMEDefang machine, MIMEDefang has a built-in function called <code>md_check_against_smtp_server</code> for querying another relay host: </p>
<dl>
<dt><code>md_check_against_smtp_server($sender, $recip, $helo, $server, $port) This</code></p>
<dd>function connects to the SMTP server $server and pretends to send mail from $sender to $recip. The return value is always a two-element array. If the RCPT TO: command succeeds, the return value is (&quot;CONTINUE&quot;, &quot;OK&quot;). If the RCPT fails with a permanent failure, the return value is (&quot;REJECT&quot;, $msg), where $msg is the message from the SMTP server. Any temporary failures, connection errors, etc. result in a return value of (&quot;TEMPFAIL&quot;, $msg). </p>
<p> The optional argument $port specifies the TCP port to connect to. If it is not supplied, then the default SMTP port of 25 is used. </p>
</dl>
<p> Suppose the machine <code>filter.domain.tld</code> is filtering mail destined for the real mail server <code>mail.domain.tld</code>. You could have a <code>filter_recipient</code> function like this: </p>
<pre>sub filter_recipient
{
 my($recip, $sender, $ip, $host, $first, $helo,
 $rcpt_mailer, $rcpt_host, $rcpt_addr) = @_;
 return md_check_against_smtp_server($sender, $recip,
 &quot;filter.domain.tld&quot;,
 &quot;mail.domain.tld&quot;);
}</pre>
<p>For each RCPT TO: command, MIMEDefang opens an SMTP connection to <code>mail.domain.tld</code> and checks if the command would succeed. </p>
<p> Please note that you should only use <code>md_check_against_smtp_server</code> if your mail server responds with a failure code for nonexistent users at the RCPT TO: level. Also, this function may impose too much overhead if you receive a lot of e-mail, and it will generate lots of useless log entries on the real mail server (because of all the RCPT TO: probes.) It may also significantly increase the load on the real mail server.</p>
<h2>Global Variables You Can Set</h2>
<p>The following Perl global variables should be set in <code>mimedefang-filter</code>: </p>
<dl>
<dt><code>$AdminAddress</code></p>
<dd>The e-mail address of the MIMEDefang administrator. </p>
<dt><code>$DaemonAddress</code></p>
<dd>The e-mail address from which MIMEDefang-originated notifications come. </p>
<dt><code>$AddWarningsInline</code></p>
<dd>If this variable is set to 0, then all MIMEDefang warnings (such as created by action_quarantine or action_drop_with_warning) are collected together and added in a separate MIME part called WARNING.TXT. If the variable is set to 1, then the warnings are added directly in the first text/plain and text/html parts of the message. If the message does not contain any text/plain or text/html parts, then a WARNING.TXT MIME part is added as before. </p>
<dt><code>$MaxMIMEParts</code></p>
<dd>A message containing many MIME parts can cause MIME::Tools to consume large amounts of memory and bring your system to its knees. If you set $MaxMIMEParts to a positive number, then MIME parsing is terminated for messages with more than that many parts, and the message is bounced. In this case, <i>none</i> of your filter functions is called. </p>
<p> By default, $MaxMIMEParts is set to -1, meaning there is no limit on the number of parts in a message. Note that in order to use this variable, you <i>must</i> install the Roaring Penguin patched version of MIME::Tools, version 5.411a-RP-Patched-02 or newer. </p>
<dt><code>$Stupidity{NoMultipleInlines}</code></p>
<dd>Set this to 1 if your e-mail is too stupid to display multiple MIME parts in-line. In this case, a nasty hack causes the first part of the original message to appear as an attachment if warning are issued. Mail clients that are not this stupid are Netscape Communicator and Pine. On the other hand, Microsoft Exchange and Microsoft Outlook are indeed this stupid. Perhaps users of those clients should switch. </p>
<p> The following global variables may optionally be set. If they are not set, sensible defaults are used: </p>
<dt><code>$AddApparentlyToForSpamAssassin</code></p>
<dd>By default, MIMEDefang tries to pass SpamAssassin a message that looks exactly like one it would receive via procmail. This means adding a Received: header, adding a Message-ID header if necessary, and adding a Return-Path: header. If you set $AddApparentlyToForSpamAssassin to 1, then MIMEDefang also adds an Apparently-To: header with all the envelope recipients before passing the message to SpamAssassin. This lets SpamAssassin detect possibly whitelisted recipient addresses. </p>
<p> The default value for $AddApparentlyToForSpamAssassin is 0. </p>
<dt><code>$SyslogFacility</code></p>
<dd>This specifies the logging facility used by mimedefang.pl. By default, it is set to &quot;mail&quot;, but you can set it to other possibilites. See the <a href="/docs/linux/man/3-openlog/">openlog</a>(3) man page for details. You should name facilities as all-lowercase without the leading &quot;LOG_&quot;. That is, use &quot;local3&quot;, not &quot;LOG_LOCAL3&quot;. </p>
<dt><code>$WarningLocation </code>(default 0)</p>
<dd>If set to 0 (the default), non-inline warnings are placed first. If you want the warning at the end of the e-mail, set $WarningLocation to -1. </p>
<dt><code>$DaemonName </code>(default MIMEDefang)</p>
<dd>The full name used when MIMEDefang sends out notifications. </p>
<dt><code>$AdminName </code>(default MIMEDefang Administrator)</p>
<dd>The full name of the MIMEDefang administrator. </p>
<dt><code>$SALocalTestsOnly </code>(default 1)</p>
<dd>If set to 1, SpamAssassin calls will use only local tests. This is the default and recommended setting. This disables Received, RBL and Razor tests in an all or nothing fashion. To use Razor this <code>MUST</code> be set to 0. You can add &#8216;skip_rbl_checks 1&#8217; to your SpamAssassin config file if you need to. </p>
<dt><code>$NotifySenderSubject </code>(default MIMEDefang Notification)</p>
<dd>The subject used when e-mail is sent out by action_notify_sender(). If you set this, you should set it each time you call action_notify_sender() to ensure consistency.</p>
<dt><code>$NotifyAdministratorSubject </code>(default MIMEDefang Notification)</p>
<dd>The subject used when e-mail is sent out by action_notify_administrator(). If you set this, you should set it each time you call action_notify_administrator() to ensure consistency. </p>
<dt><code>$QuarantineSubject </code>(default MIMEDefang Quarantine Report)</p>
<dd>The subject used when a quarantine notice is sent to the administrator. If you set this, you should set it each time you call action_quarantine() or action_quarantine_entire_message(). </p>
<dt><code>$NotifyNoPreamble </code>(default 0)</p>
<dd>Normally, notifications sent by action_notify_sender() have a preamble warning about message modifications. If you do not want this, set $NotifyNoPreamble to 1. </p>
<dt><code>$CSSHost </code>(default 127.0.0.1:7777:local)</p>
<dd>Host and port for the Symantec CarrierScan Server virus scanner. This takes the form <i>ip_addr</i>:<i>port</i>:<i>local_or_nonlocal</i>. The <i>ip_addr</i> and <i>port</i> are the host and port on which CarrierScan Server is listening. If you want to scan local files, append :local to force the use of the AVSCANLOCAL command. If the CarrierScan Server is on another host, append :nonlocal to force the file contents to be sent to the scanner over the socket. </p>
<dt><code>$SophieSock </code>(default /var/spool/MIMEDefang/sophie)</p>
<dd>Socket used for Sophie daemon calls within message_contains_virus_sophie and entity_contains_virus_sophie unless a socket is provided by the calling routine. </p>
<dt><code>$ClamdSock </code>(default /var/spool/MIMEDefang/clamd.sock)</p>
<dd>Socket used for clamd daemon calls within message_contains_virus_clamd and entity_contains_virus_clamd unless a socket is provided by the calling routine. </p>
<dt><code>$TrophieSock </code>(default /var/spool/MIMEDefang/trophie)</p>
<dd>Socket used for Trophie daemon calls within message_contains_virus_trophie and entity_contains_virus_trophie unless a socket is provided by the calling routine. </p>
</dl>
<h2>Filter</h2>
<p>The heart of <code>mimedefang-filter</code> is the <code>filter</code> procedure. See the examples that came with MIMEDefang to learn to write a filter. The filter is called with the following arguments: </p>
<dl>
<dt><code>$entity</code></p>
<dd>The MIME::Entity object. (See the MIME::tools Perl module documentation.) </p>
<dt><code>$fname</code></p>
<dd>The suggested attachment filename, or &quot;&quot; if none was supplied. </p>
<dt><code>$ext</code></p>
<dd>The file extension (all characters from the rightmost period to the end of the filename.) </p>
<dt><code>$type</code></p>
<dd>The MIME type (for example, &quot;text/plain&quot;.) </p>
</dl>
<p> The filename is derived as follows: </p>
<dl>
<dt>o</p>
<dd>First, if the Content-Disposition header has a &quot;filename&quot; field, it is used. </p>
<dt>o</p>
<dd>Otherwise, if the Content-Type header has a &quot;name&quot; field, it is used. </p>
<dt>o</p>
<dd>Otherwise, the Content-Description header value is used. </p>
</dl>
<p> Note that the truly paranoid will check all three fields for matches. The functions <code>re_match</code> and <code>re_match_ext</code> perform regular expression matches on all three of the fields named above, and return 1 if any field matches. See the sample filters for details. The calling sequence is: </p>
<pre> re_match($entity, &quot;regexp&quot;)
 re_match_ext($entity, &quot;regexp&quot;)</pre>
<p><code>re_match</code> returns true if any of the fields matches the regexp without regard to case. <code>re_match_ext</code> returns true if the extension in any field matches. An extension is defined as the last dot in a name and all remaining characters. </p>
<p> A third function called <code>re_match_in_zip_directory</code> will look inside zip files and return true if any of the file names inside the zip archive match the regular expression. Call it like this: </p>
<pre> my $bh = $entity-&gt;bodyhandle();
 my $path = (defined($bh)) ? $bh-&gt;path() : undef;
 if (defined($path) and re_match_in_zip_directory($path, &quot;regexp&quot;)) {
 # Take action...
 }</pre>
<p>You should <i>not</i> call <code>re_match_in_zip_directory</code> unless you know that the entity is a zip file attachment.</p>
<h2>Global Variables Set By Mimedefang.Pl</h2>
<p>The following global variables are set by <code>mimedefang.pl</code> and are available for use in your filter. All of these variables are always available to filter_begin, filter, filter_multipart and filter_end. In addition, some of them are available in <code>filter_relay</code>, <code>filter_sender</code> or <code>filter_recipient</code>. If this is the case, it will be noted below. </p>
<dl>
<dt><code>%Features</code></p>
<dd>This hash lets you determine at run-time whether certain functionality is available. This hash is available at all times assuming the detect_and_load_perl_modules() function has been called. The defined features are: </p>
<p> $Features{&quot;SpamAssassin&quot;} is 1 if SpamAssassin 1.6 or better is installed; 0 otherwise. </p>
<p> $Features{&quot;HTML::Parser&quot;} is 1 if HTML::Parser is installed; 0 otherwise. </p>
<p> $Features{&quot;Virus:FPROTD&quot;} is currently always 0. Set it to 1 in your filter file if you have F-Risk&#8217;s FPROTD scanner earlier than version 6. </p>
<p> $Features{&quot;Virus:FPROTD6&quot;} is currently always 0. Set it to 1 in your filter file if you have version 6 of F-Risk&#8217;s FPROTD scanner. </p>
<p> $Features{&quot;Virus:SymantecCSS&quot;} is currently always 0. Set it to 1 in your filter file if you have the Symantec CarrierScan Server virus scanner. </p>
<p> $Features{&quot;Virus:NAI&quot;} is the full path to NAI uvscan if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:BDC&quot;} is the full path to Bitdefender bdc if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:NVCC&quot;} is the full path to Norman Virus Control nvcc if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:HBEDV&quot;} is the full path to H+BEDV AntiVir if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:VEXIRA&quot;} is the full path to Central Command Vexira if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:SOPHOS&quot;} is the full path to Sophos sweep if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:SAVSCAN&quot;} is the full path to Sophos savscan if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:CLAMAV&quot;} is the full path to Clam AV clamscan if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:AVP&quot;} is the full path to AVP AvpLinux if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:AVP5&quot;} is the full path to Kaspersky &quot;aveclient&quot; if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:CSAV&quot;} is the full path to Command csav if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:FSAV&quot;} is the full path to F-Secure fsav if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:FPROT&quot;} is the full path to F-Risk f-prot if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:FPSCAN&quot;} is the full path to F-Risk fpscan if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:SOPHIE&quot;} is the full path to Sophie if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:CLAMD&quot;} is the full path to clamd if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:TROPHIE&quot;} is the full path to Trophie if it is installed; 0 if it is not. </p>
<p> $Features{&quot;Virus:NOD32&quot;} is the full path to ESET NOD32 nod32cli if it is installed; 0 if it is not. </p>
<p> <code>NOTE:</code> Perl-module based features such as SpamAssassin are determined at runtime and may change as these are added and removed. Most Virus features are predetermined at the time of configuration and do not adapt to runtime availability unless changed by the filter rules. </p>
<dt><code>$CWD</code></p>
<dd>This variable holds the working directory for the current message. During filter processing, <code>mimedefang.pl</code> chdir&#8217;s into this directory before calling any of the filter_ functions. Note that this variable <i>is</i> set correctly in <code>filter_sender</code> and <code>filter_recipient</code>, but <i>not</i> in <code>filter_relay</code>. </p>
<dt><code>$SuspiciousCharsInHeaders</code></p>
<dd>If this variable is true, then <code>mimedefang</code> has discovered suspicious characters in message headers. This might be an exploit for bugs in MIME-parsing routines in some badly-written mail user agents (e.g. Microsoft Outlook.) You should <i>always</i> drop such messages. </p>
<dt><code>$SuspiciousCharsInBody</code></p>
<dd>If this variable is true, then <code>mimedefang</code> has discovered suspicious characters in the message body. This might be an exploit for bugs in MIME-parsing routines in some badly-written mail user agents (e.g. Microsoft Outlook.) You should <i>always</i> drop such messages. </p>
<dt><code>$RelayHostname</code></p>
<dd>The host name of the relay. This is the name of the host that is attempting to send e-mail to your host. May be &quot;undef&quot; if the host name could not be determined. This variable is available in <code>filter_relay</code>, <code>filter_sender</code> and <code>filter_recipient</code> in addition to the body filtering functions. </p>
<dt><code>$RelayAddr</code></p>
<dd>The IP address of the sending relay (as a string consisting of four dot-separated decimal numbers.) One potential use of <code>$RelayAddr</code> is to limit mailing to certain lists to people within your organization. This variable is available in <code>filter_relay</code>, <code>filter_sender</code> and <code>filter_recipient</code> in addition to the body filtering functions. </p>
<p> <code>$Helo</code> The argument given to the SMTP &quot;HELO&quot; command. This variable is available in <code>filter_sender</code> and <code>filter_recipient</code>, but <i>not</i> in <code>filter_relay</code>. </p>
<dt><code>$Subject</code></p>
<dd>The contents of the &quot;Subject:&quot; header. </p>
<dt><code>$Sender</code></p>
<dd>The sender of the e-mail. This variable is set in <code>filter_sender</code> and <code>filter_recipient</code> in addition to the body filtering functions. </p>
<dt><code>@Recipients</code></p>
<dd>A list of the recipients. In <code>filter_recipient</code>, it is set to the single recipient currently under consideration. Or, after calling <code>read_commands_file</code> within <code>filter_recipient</code>, the current recipient under consideration is in the final position of the array, at <code>$Recipients[-1]</code>, while any previous (and accepted) recipients are at the beginning of the array, that is, in <code>@Recipients[0 .. $#Recipients-1]</code>. </p>
<dt><code>$MessageID</code></p>
<dd>The contents of the &quot;Message-ID:&quot; header if one is present. Otherwise, contains the string &quot;NOQUEUE&quot;. </p>
<dt><code>$QueueID</code></p>
<dd>The Sendmail queue identifier if it could be determined. Otherwise, contains the string &quot;NOQUEUE&quot;. This variable <i>is</i> set correctly in <code>filter_sender</code> and <code>filter_recipient</code>, but it is <i>not</i> available in <code>filter_relay</code>. </p>
<dt><code>$MsgID</code></p>
<dd>Set to $QueueID if the queue ID could be determined; otherwise, set to $MessageID. This identifier should be used in logging, because it matches the identifier used by Sendmail to log messages. Note that this variable <i>is</i> set correctly in <code>filter_sender</code> and <code>filter_recipient</code>, but it is <i>not</i> available in <code>filter_relay</code>. </p>
<dt><code>$VirusScannerMessages</code></p>
<dd>Each time a virus-scanning function is called, messages (if any) from the virus scanner are accumulated in this variable. You can use it in filter_end to formulate a notification (if you wish.) </p>
<dt><code>$VirusName</code></p>
<dd>If a virus-scanning function found a virus, this variable will hold the virus name (if it could be determined.) </p>
<dt><code>$SASpamTester</code></p>
<dd>If defined, this is the configured Mail::SpamAssassin object used for mail tests. It may be initialized with a call to <code>spam_assassin_init</code> which also returns it. </p>
<dt><code>%SendmailMacros</code></p>
<dd>This hash contains the values of some Sendmail macros. The hash elements exist only for macros defined by Sendmail. See the Sendmail documentation for the meanings of the macros. </p>
<p> By default, <code>mimedefang</code> passes the values of the following macros: ${daemon_name}, ${daemon_port}, ${if_name}, ${if_addr}, $j, $_, $i, ${tls_version}, ${cipher}, ${cipher_bits}, ${cert_subject}, ${cert_issuer}, ${auth_type}, ${auth_authen}, ${auth_ssf}, ${auth_author}, ${mail_mailer}, ${mail_host} and ${mail_addr}. In addition, ${client_port} is set to the client&#8217;s TCP port. </p>
<p> If any macro is not set or not passed to milter, it will be unavailable. To access the value of a macro, use: </p>
<pre> $SendmailMacros{&quot;macro_name&quot;}</pre>
<p>Do not place curly brackets around the macro name. This variable is available in <code>filter_sender</code> and <code>filter_recipient</code> after a call to <code>read_commands_file</code>. </p>
<dt><code>@SenderESMTPArgs</code></p>
<dd>This array contains all the ESMTP arguments supplied in the MAIL FROM: command. For example: </p>
<pre>sub print_sender_esmtp_args {
 foreach (@SenderESMTPArgs) {
 print STDERR &quot;Sender ESMTP arg: $_;
 }
}</pre>
<dt><code>%RecipientESMTPArgs</code></p>
<dd>This hash contains all the ESMTP arguments supplied in each RCPT TO: command. For example: </p>
<pre>sub print_recip_esmtp_args {
 foreach my $recip (@Recipients) {
 foreach(@{$RecipientESMTPArgs{$recip}}) {
 print STDERR &quot;Recip ESMTP arg for $recip: $_;
 }
 }
}</pre>
<dt><code>%RecipientMailers</code></p>
<dd>This hash contains the Sendmail &quot;mailer-host-address&quot; triple for each recipient. Here&#8217;s an example of how to use it: </p>
<pre>sub print_mailer_info {
 my($recip, $mailer, $host, $addr);
 foreach $recip (@Recipients) {
 $mailer = ${RecipientMailers{$recip}}[0];
 $host = ${RecipientMailers{$recip}}[1];
 $addr = ${RecipientMailers{$recip}}[2];
 print STDERR &quot;$recip: mailer=$mailer, host=$host, addr=$addr
&quot;;
 }
}</pre>
<p>In <code>filter_recipient</code>, this variable by default only contains information on the recipient currently under investigation. Information on all recipients is available after calling <code>read_commands_file</code>. </p>
</dl>
<h2>Actions</h2>
<p>When the filter procedure decides how to dispose of a part, it should call one or more <code>action_</code> subroutines. The action subroutines are: </p>
<dl>
<dt><code>action_accept()</code></p>
<dd>Accept the part. </p>
<dt><code>action_rebuild() </code></p>
<dd>Rebuild the mail body, even if <code>mimedefang</code> thinks no changes were made. Normally, <code>mimedefang</code> does not alter a message if no changes were made. <code>action_rebuild</code> may be used if you make changes to entities directly (by manipulating the MIME::Head, for example.) Unless you call <code>action_rebuild</code>, <code>mimedefang</code> will be unaware of the changes. Note that all the built-in <code>action&#8230;</code> routines that change a message implicitly call <code>action_rebuild</code>. </p>
<dt><code>action_add_header($hdr, $val)</code></p>
<dd>Add a header to the message. This can be used in <code>filter_begin</code> or <code>filter_end</code>. The $hdr component is the header name <i>without the colon</i>, and the $val is the header value. For example, to add the header: </p>
<pre> X-MyHeader: A nice piece of text</pre>
<p>use: </p>
<pre> action_add_header(&quot;X-MyHeader&quot;, &quot;A nice piece of text&quot;);</pre>
<dt><code>action_change_header($hdr, $val, $index)</code></p>
<dd>Changes an existing header in the message. This can be used in <code>filter_begin</code> or <code>filter_end</code>. The $hdr parameter is the header name <i>without the colon</i>, and $val is the header value. If the header does not exist, then a header with the given name and value is added. </p>
<p> The $index parameter is optional; it defaults to 1. If you supply it, then the $index&#8217;th occurrence of the header is changed, if there is more than one header with the same name. (This is common with the Received: header, for example.) </p>
<dt><code>action_insert_header($hdr, $val, $index)</code></p>
<dd>Add a header to the message int the specified position $index. A position of 0 specifies that the header should be prepended before existing headers. This can be used in <code>filter_begin</code> or <code>filter_end</code>. The $hdr component is the header name <i>without the colon</i>, and the $val is the header value. </p>
<dt><code>action_delete_header($hdr, $index)</code></p>
<dd>Deletes an existing header in the message. This can be used in <code>filter_begin</code> or <code>filter_end</code>. The $hdr parameter is the header name <i>without the colon</i>. </p>
<p> The $index parameter is optional; it defaults to 1. If you supply it, then the $index&#8217;th occurrence of the header is deleted, if there is more than one header with the same name. </p>
<dt><code>action_delete_all_headers($hdr)</code></p>
<dd>Deletes all headers with the specified name. This can be used in <code>filter_begin</code> or <code>filter_end</code>. The $hdr parameter is the header name <i>without the colon</i>. </p>
<dt><code>action_drop()</code></p>
<dd>Drop the part. If called from <code>filter_multipart</code>, drops all contained parts also. </p>
<dt><code>action_drop_with_warning($msg)</code></p>
<dd>Drop the part, but add the warning <i>$msg</i> to the e-mail message. If called from <code>filter_multipart</code>, drops all contained parts also. </p>
<dt><code>action_accept_with_warning($msg)</code></p>
<dd>Accept the part, but add the warning <i>$msg</i> to the e-mail message. </p>
<dt><code>action_replace_with_warning($msg)</code></p>
<dd>Drop the part and replace it with a text part <i>$msg</i>. If called from <code>filter_multipart</code>, drops all contained parts also. </p>
<dt><code>action_replace_with_url($entity, $doc_root, $base_url, $msg, [$cd_data, $salt])</code></p>
<dd>Drop the part, but save it in a unique location under $doc_root. The part is replaced with the text message $msg. The string &quot;_URL_&quot; in $msg is replaced with $base_url/something, that can be used to retrieve the message. </p>
<p> You should not use this function in <code>filter_multipart</code>. </p>
<p> This action is intended for stripping large parts out of the message and replacing them to a link on a Web server. Here&#8217;s how you would use it in filter(): </p>
<pre>$size = (stat($entity-&gt;bodyhandle-&gt;path))[7];
if ($size &gt; 1000000) {
 return action_replace_with_url($entity,
 &quot;/home/httpd/html/mail_parts&quot;,
 &quot;<a rel="nofollow" href="http://mailserver.company.com/mail_parts">http://mailserver.company.com/mail_parts</a>&quot;,
 &quot;The attachment was larger than 1,000,000 bytes.
&quot; .
 &quot;It was removed, but may be accessed at this URL:

&quot; .
 &quot;	_URL_
&quot;);
}</pre>
<p>This example moves attachments greater than 1,000,000 bytes into /home/httpd/html/mail_parts and replaces them with a link. The directory should be accessible via a Web server at <a rel="nofollow" href="http://mailserver.company.com/mail_parts.">http://mailserver.company.com/mail_parts.</a> </p>
<p> The generated name is created by performing a SHA1 hash of the part and adding the extension to the ASCII-HEX representation of the hash. If many different e-mails are sent containing an identical large part, only one copy of the part is stored, regardless of the number of senders or recipients. </p>
<p> For privacy reasons, you <code>must</code> turn off Web server indexing in the directory in which you place mail parts, or anyone will be able to read them. If indexing is disabled, an attacker would have to guess the SHA1 hash of a part in order to read it. </p>
<p> Optionally, a fifth argument can supply data to be saved into a hidden dot filename based on the generated name. This data can then be read in on the fly by a CGI script or mod_perl module before serving the file to a web client, and used to add information to the response, such as Content-Disposition data. </p>
<p> A sixth optional argument, $salt, is mixed in to the SHA1 hash. This salt can be any string and should be kept confidential. The salt is designed to prevent people from guessing whether or not a particular attachment has been received on your server by altering the SHA1 hash calculation. </p>
<dt><code>action_defang($entity, $name, $fname, $type)</code></p>
<dd>Accept the part, but change its name to <i>$name</i>, its suggested filename to <i>$fname</i> and its MIME type to <i>$type</i>. If <i>$name</i> or <i>$fname</i> are &quot;&quot;, then <code>mimedefang.pl</code> generates generic names. Do not use this action in <code>filter_multipart</code>. </p>
<p> If you use <code>action_defang</code>, you must define a subroutine called <code>defang_warning</code> in your filter. This routine takes two arguments: $oldfname (the original name of an attachment) and $fname (the defanged version.) It should return a message telling the user what happened. For example: </p>
<pre>sub defang_warning {
 my($oldfname, $fname) = @_;
 return &quot;The attachment '$oldfname' was renamed to '$fname'
&quot;;
}</pre>
<dt><code>action_external_filter($entity, $cmd)</code></p>
<dd>Run an external UNIX command <code>$cmd</code>. This command must read the part from the file <code>./FILTERINPUT</code> and leave the result in <code>./FILTEROUTPUT</code>. If the command executes successfully, returns 1, otherwise 0. You can test the return value and call another <code>action_</code> if the filter failed. Do not use this action in <code>filter_multipart</code>. </p>
<dt><code>action_quarantine($entity, $msg)</code></p>
<dd>Drop and quarantine the part, but add the warning <i>$msg</i> to the e-mail message. </p>
<dt><code>action_quarantine_entire_message($msg)</code></p>
<dd>Quarantines the entire message in a quarantine directory on the mail server, but does not otherwise affect disposition of the message. If &quot;$msg&quot; is non-empty, it is included in any administrator notification. </p>
<dt><code>action_sm_quarantine($reason)</code></p>
<dd>Quarantines a message <i>in the Sendmail mail queue</i> using the new QUARANTINE facility of Sendmail 8.13. Consult the Sendmail documentation for details about this facility. If you use <code>action_sm_quarantine</code> with a version of Sendmail that lacks the QUARANTINE facility, <code>mimedefang</code> will log an error message and not quarantine the message. </p>
<dt><code>action_bounce($reply, $code, $dsn)</code></p>
<dd>Reject the entire e-mail message with an SMTP failure code, and the one-line error message <i>$reply</i>. If the optional $code and $dsn arguments are supplied, they specify the numerical SMTP reply code and the extended status code (DSN code). If the codes you supply do not make sense for a bounce, they are replaced with &quot;554&quot; and &quot;5.7.1&quot; respectively. </p>
<p> <code>action_bounce</code> merely makes a note that the message is to be bounced; remaining parts are still processed. If <code>action_bounce</code> is called for more than one part, the mail is bounced with the message in the final call to <code>action_bounce</code>. You can profitably call <code>action_quarantine</code> followed by <code>action_bounce</code> if you want to keep a copy of the offending part. Note that the message is not bounced immediately; rather, remaining parts are processed and the message is bounced after all parts have been processed. </p>
<p> Note that despite its name, <code>action_bounce</code> does <i>not</i> generate a &quot;bounce message&quot;. It merely rejects the message with an SMTP failure code. </p>
<p> <code>WARNING:</code> <code>action_bounce()</code> may cause the sending relay to generate spurious bounce messages if the sender address is faked. This is a particular problem with viruses. However, we believe that on balance, it&#8217;s better to bounce a virus than to silently discard it. It&#8217;s almost never a good idea to hide a problem. </p>
<dt><code>action_tempfail($msg, $code, $dsn)</code></p>
<dd>Cause an SMTP &quot;temporary failure&quot; code to be returned, so the sending mail relay requeues the message and tries again later. The message $msg is included with the temporary failure code. If the optional $code and $dsn arguments are supplied, they specify the numerical SMTP reply code and the extended status code (DSN code). If the codes you supply do not make sense for a temporary failure, they are replaced with &quot;450&quot; and &quot;4.7.1&quot; respectively. </p>
<dt><code>action_discard()</code></p>
<dd>Silently discard the message, notifying nobody. You can profitably call <code>action_quarantine</code> followed by <code>action_discard</code> if you want to keep a copy of the offending part. Note that the message is not discarded immediately; rather, remaining parts are processed and the message is discarded after all parts have been processed. </p>
<dt><code>action_notify_sender($message)</code></p>
<dd>This action sends an e-mail back to the original sender with the indicated message. You may call another action after this one. If <code>action_notify_sender</code> is called more than once, the messages are accumulated into a single e-mail message &#8212; at most one notification message is sent per incoming message. The message should be terminated with a newline. </p>
<p> The notification is delivered in deferred mode; you should run a client-queue runner if you are using Sendmail 8.12. </p>
<p> <i>NOTE</i>: Viruses often fake the sender address. For that reason, if a virus-scanner has detected a virus, <code>action_notify_sender</code> is <i>disabled</i> and will simply log an error message if you try to use it. </p>
<dt><code>action_notify_administrator($message)</code></p>
<dd>This action e-mails the MIMEDefang administrator the supplied message. You may call another action after this one; <code>action_notify_administrator</code> does not affect mail processing. If <code>action_notify_administrator</code> is called more than once, the messages are accumulated into a single e-mail message &#8212; at most one notification message is sent per incoming message. The message should be terminated with a newline. </p>
<p> The notification is delivered in deferred mode; you should run a client-queue runner if you are using Sendmail 8.12. </p>
<dt><code>append_text_boilerplate($entity, $boilerplate, $all)</code></p>
<dd>This action should <i>only</i> be called from <code>filter_end</code>. It appends the text &quot;
$boilerplate
&quot; to the first text/plain part (if $all is 0) or to <i>all</i> text/plain parts (if $all is 1). </p>
<dt><code>append_html_boilerplate($entity, $boilerplate, $all)</code></p>
<dd>This action should <i>only</i> be called from <code>filter_end</code>. It adds the text &quot;
$boilerplate
&quot; to the first text/html part (if $all is 0) or to <i>all</i> text/html parts (if $all is 1). This function tries to be smart about inserting the boilerplate; it uses HTML::Parser to detect closing tags and inserts the boilerplate before the &lt;/body&gt; tag if there is one, or before the &lt;/html&gt; tag if there is no &lt;/body&gt;. If there is no &lt;/body&gt; or &lt;/html&gt; tag, it appends the boilerplate to the end of the part. </p>
<p> Do not use append_html_boilerplate unless you have installed the HTML::Parser Perl module. </p>
<p> Here is an example illustrating how to use the boilerplate functions: </p>
<pre> sub filter_end {
 my($entity) = @_;
 append_text_boilerplate($entity,
 &quot;Lame text disclaimer&quot;, 0);
 append_html_boilerplate($entity,
 &quot;&lt;em&gt;Lame&lt;/em&gt; HTML disclaimer&quot;, 0);
 }</pre>
<dt><code>action_add_part($entity, $type, $encoding, $data, $fname, $disposition [, $offset])</code></p>
<dd>This action should <i>only</i> be called from the <code>filter_end</code> routine. It adds a new part to the message, converting the original message to mutipart if necessary. The function returns the part so that additional mime attributes may be set on it. Here&#8217;s an example: </p>
<pre> sub filter_end {
 my($entity) = @_;
 action_add_part($entity, &quot;text/plain&quot;, &quot;-suggest&quot;,
 &quot;This e-mail does not represent&quot; .
 &quot;the official policy of FuBar, Inc.
&quot;,
 &quot;disclaimer.txt&quot;, &quot;inline&quot;);
 }</pre>
<p>The $entity parameter <i>must</i> be the argument passed in to <code>filter_end</code>. The $offset parameter is optional; if omitted, it defaults to -1, which adds the new part at the end. See the MIME::Entity man page and the <code>add_part</code> member function for the meaning of $offset. </p>
<p> Note that <code>action_add_part</code> tries to be more intelligent than simply calling $entity-&gt;add_part. The decision process is as follows: </p>
<dt><code>o</code></p>
<dd>If the top-level entity is multipart/mixed, then the part is simply added. </p>
<dt><code>o</code></p>
<dd>Otherwise, a new top-level multipart/mixed container is generated, and the original top-level entity is made the first part of the multipart/mixed container. The new part is then added to the multipart/mixed container. </p>
<dt><code>action_add_entity($entity [, $offset])</code></p>
<dd>This is similar to <code>action_add_part</code> but takes a pre-built MIME::Entity object rather than constructing one based on $type, $encoding, $data, $fname and $disposition arguments. </p>
</dl>
<h2>Useful Routines</h2>
<p><code>mimedefang.pl</code> includes some useful functions you can call from your filter: </p>
<dl>
<dt><code>detect_and_load_perl_modules()</code></p>
<dd>Unless you <i>really</i> know what you&#8217;re doing, this function <code>must</code> be called first thing in your filter file. It causes <code>mimedefang.pl</code> to detect and load Perl modules such as Mail::SpamAssassin, Net::DNS, etc., and to populate the %Features hash. </p>
<dt><code>send_quarantine_notifications()</code></p>
<dd>This function should be called from <code>filter_end</code>. If any parts were quarantined, a quarantine notification is sent to the MIMEDefang administrator. Please note that if you do not call <code>send_quarantine_notifications</code>, then <i>no</i> quarantine notifications are sent. </p>
<dt><code>get_quarantine_dir()</code></p>
<dd>This function returns the full path name of the quarantine directory. If you have not yet quarantined any parts of the message, a quarantine directory is created and its pathname returned. </p>
<dt><code>change_sender($sender)</code></p>
<dd>This function changes the envelope sender to $sender. It can only be called from <code>filter_begin</code> or any later function. Please note that this function is <i>only</i> supported with Sendmail/Milter 8.14.0 or newer. It has <i>no effect</i> if you&#8217;re running older versions. </p>
<dt><code>add_recipient($recip)</code></p>
<dd>This function adds $recip to the list of envelope recipients. A copy of the message (after any modifications by MIMEDefang) will be sent to $recip in addition to the original recipients. Note that <code>add_recipient</code> does <i>not</i> modify the @Recipients array; it just makes a note to Sendmail to add the recipient. </p>
<dt><code>delete_recipient($recip)</code></p>
<dd>This function deletes $recip from the list of recipients. That person will not receive a copy of the mail. $recip should exactly match an entry in the @Recipients array for delete_recipient() to work. Note that <code>delete_recipient</code> does <i>not</i> modify the @Recipients array; it just makes a note to Sendmail to delete the recipient.</p>
<dt><code>resend_message($recip1, $recip2, &#8230;)</code></p>
<dd>or</p>
<dt><code>resend_message(@recips)</code></p>
<dd>This function <i>immediately</i> resends the <i>original, unmodified</i> mail message to each of the named recipients. The sender&#8217;s address is preserved. Be very careful when using this function, because it resends the <i>original</i> message, which may contain undesired attachments. Also, you should <i>not</i> call this function from filter(), because it resends the message <i>each time</i> it is called. This may result in multiple copies being sent if you are not careful. Call from filter_begin() or filter_end() to be safe. </p>
<p> The function returns true on success, or false if it fails. </p>
<p> Note that the resend_message function delivers the mail in deferred mode (using Sendmail&#8217;s &quot;-odd&quot; flag.) You <i>must</i> run a client-submission queue processor if you use Sendmail 8.12. We recommend executing this command as part of the Sendmail startup sequence: </p>
<pre> sendmail -Ac -q5m</pre>
<dt><code>remove_redundant_html_parts($entity)</code></p>
<dd>This function should only be called from <code>filter_end</code>. It removes redundant HTML parts from the message. It works by deleting any part of type text/html from the message if (1) it is a sub-part of a multipart/alternative part, and (2) there is another part of type text/plain under the multipart/alternative part. </p>
<dt><code>replace_entire_message($entity)</code></p>
<dd>This function can only be called from <code>filter_end</code>. It replaces the entire message with $entity, a MIME::Entity object that you have constructed. You can use any of the MIME::Tools functions to construct the entity. </p>
<dt><code>read_commands_file()</code></p>
<dd>This function should only be called from <code>filter_sender</code> and <code>filter_recipient</code>. This will read the <code>COMMANDS</code> file (as described in <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7)), and will fill or update the following global variables: $Sender, @Recipients, %RecipientMailers, $RelayAddr, $RealRelayAddr, $RelayHostname, $RealRelayHostname, $QueueID, $Helo, %SendmailMacros. </p>
<p> If you do not call <code>read_commands_file</code>, then the only information available in <code>filter_sender</code> and <code>filter_recipient</code> is that which is passed as an argument to the function. </p>
<dt><code>stream_by_domain()</code></p>
<dd><i>Do not use this function unless you have Sendmail 8.12 and locally- submitted e-mail is submitted using SMTP.</i> </p>
<p> This function should <i>only</i> be called at the very beginning of filter_begin(), like this: </p>
<pre> sub filter_begin {
 if (stream_by_domain()) {
 return;
 }
 # Rest of filter_begin
 }</pre>
<p>stream_by_domain() looks at all the recipients of the message, and if they belong to the same domain (e.g., joe [at] domain.com, jane [at] domain.com and sue [at] domain.com), it returns 0 and sets the global variable $Domain to the domain (domain.com in this example.) </p>
<p> If users are in different domains, stream_by_domain() <i>resends</i> the message (once to each domain) and returns 1 For example, if the original recipients are joe [at] abc.net, jane [at] xyz.net and sue [at] abc.net, the original message is resent twice: One copy to joe [at] abc.net and sue [at] abc.net, and another copy to jane [at] xyz.net. Also, any subsequent scanning is canceled (filter() and filter_end() will <i>not</i> be called for the original message) and the message is silently discarded. </p>
<p> If you have Sendmail 8.12, then locally-submitted messages are sent via SMTP, and MIMEDefang will be called for each resent message. It is possible to set up Sendmail 8.12 so locally-submitted messages are delivered directly; in this case, stream_by_domain will <i>not</i> work. </p>
<p> Using stream_by_domain allows you to customize your filter rules for each domain. If you use the function as described above, you can do this in your filter routine: </p>
<pre> sub filter {
 my($entity, $fname, $ext, $type) = @_;
 if ($Domain eq &quot;abc.com&quot;) {
 # Filter actions for abc.com
 } elsif ($Domain eq &quot;xyz.com&quot;) {
 # Filter actions for xyz.com
 } else {
 # Default filter actions
 }
 }</pre>
<p>You cannot rely on $Domain being set unless you have called stream_by_domain(). </p>
<dt><code>stream_by_recipient()</code></p>
<dd><i>Do not use this function unless you have Sendmail 8.12 and locally- submitted e-mail is submitted using SMTP.</i> </p>
<p> This function should <i>only</i> be called at the very beginning of filter_begin(), like this: </p>
<pre> sub filter_begin {
 if (stream_by_recipient()) {
 return;
 }
 # Rest of filter_begin
 }</pre>
<p>If there is more than one recipient, stream_by_recipient() resends the message once to each recipient. That way, you can customize your filter rules on a per-recipient basis. This may increase the load on your mail server considerably. </p>
<p> Also, a &quot;recipient&quot; is determined before alias expansion. So &quot;all [at] mydomain.com&quot; is considered a single recipient, even if Sendmail delivers to a list. </p>
<p> If you have Sendmail 8.12, then locally-submitted messages are sent via SMTP, and MIMEDefang will be called for each resent message. It is possible to set up Sendmail 8.12 so locally-submitted messages are delivered directly; in this case, stream_by_recipient() will <i>not</i> work. </p>
<p> stream_by_recipient() allows you to customize your filter rules for each recipient in a manner similar to stream_by_domain(). </p>
</dl>
<h2>Logging</h2>
<dl>
<dt><code>md_graphdefang_log_enable($facility, $enum_recips)</code></p>
<dd>Enables the md_graphdefang_log function (described next). The function logs to syslog using the specified facility. If you omit $facility, it defaults to &#8216;mail&#8217;. If you do not call md_graphdefang_log_enable in your filter, then any calls to md_graphdefang_log simply do nothing. </p>
<p> If you supply $enum_recips as 1, then a line of logging is output for <i>each</i> recipient of a mail message. If it is zero, then only a single line is output for each message. If you omit $enum_recips, it defaults to 1. </p>
<dt><code>md_graphdefang_log($event, $v1, $v2)</code></p>
<dd>Logs an event with up to two optional additional parameters. The log message has a specific format useful for graphing tools; the message looks like this: </p>
<pre> MDLOG,msgid,event,v1,v2,sender,recipient,subj</pre>
<p>&quot;MDLOG&quot; is literal text. &quot;msgid&quot; is the Sendmail queue identifier. &quot;event&quot; is the event name, and &quot;v1&quot; and &quot;v2&quot; are the additional parameters. &quot;sender&quot; is the sender&#8217;s e-mail address. &quot;recipient&quot; is the recipient&#8217;s e-mail address, and &quot;subj&quot; is the message subject. If a message has more than one recipient, md_graphdefang_log may log an event message for <i>each</i> recipient, depending on how you called md_graphdefang_log_enable. </p>
<p> Note that md_graphdefang_log should not be used in filter_relay, filter_sender or filter_recipient. The global variables it relies on are not valid in that context. </p>
<p> If you want to log general text strings, <i>do not</i> use md_graphdefang_log. Instead, use md_syslog (described next). </p>
<dt><code>md_syslog($level, $msg)</code></p>
<dd>Logs the message $msg to syslog, using level $level. The level is a literal string, and should be one of &#8216;err&#8217;, &#8216;debug&#8217;, &#8216;warning&#8217;, &#8217;emerg&#8217;, &#8216;crit&#8217;, &#8216;notice&#8217; or &#8216;info&#8217;. (See <a href="/docs/linux/man/3-syslog/">syslog</a>(3) for details.) </p>
<p> Note that md_syslog does <i>not</i> perform %-subsitutions like <a href="/docs/linux/man/3-syslog/">syslog</a>(3) does. Depending on your Perl installation, md_syslog boils down to a call to Unix::Syslog::syslog or Sys::Syslog::syslog. See the Unix::Syslog or Sys::Syslog man pages for more details. </p>
<dt><code>md_openlog($tag, $facility)</code></p>
<dd>Sets the tag used in syslog messages to $tag, and sends the logs to the $facility facility. If you do not call md_openlog before you call md_syslog, then it is called implicitly with $tag set to <code>mimedefang.pl</code> and $facility set to <code>mail</code>. </p>
</dl>
<h2>Rbl Lookup Functions</h2>
<p><code>mimedefang.pl</code> includes the following functions for looking up IP addresses in DNS-based real-time blacklists. Note that the &quot;relay_is_blacklisted&quot; functions are deprecated and may be removed in a future release. Instead, you should use the module Net::DNSBL::Client from CPAN. </p>
<dl>
<dt><code>relay_is_blacklisted($relay, $domain)</code></p>
<dd>This checks a DNS-based real-time spam blacklist, and returns true if the relay host is blacklisted, or false otherwise. (In fact, the return value is whatever the blacklist returns as a resolved hostname, such as &quot;127.0.0.4&quot;) </p>
<p> Note that <code>relay_is_blacklisted</code> uses the built-in <code>gethostbyname</code> function; this is usually quite inefficient and does not permit you to set a timeout on the lookup. Instead, we recommend using one of the other DNS lookup function described in this section. (Note, though, that the other functions require the Perl Net::DNS module, whereas <code>relay_is_blacklisted</code> does not.) </p>
<p> Here&#8217;s an example of how to use <code>relay_is_blacklisted</code>: </p>
<pre> if (relay_is_blacklisted($RelayAddr, &quot;rbl.spamhaus.org&quot;)) {
 action_add_header(&quot;X-Blacklist-Warning&quot;,
 &quot;Relay $RelayAddr is blacklisted by Spamhaus&quot;);
 }</pre>
<dt><code>relay_is_blacklisted_multi($relay, $timeout, $answers_wanted, [$domain1, $domain2, &#8230;], $res)</code></p>
<dd>This function is similar to <code>relay_is_blacklisted</code>, except that it takes a timeout argument (specified in seconds) and an array of domains to check. The function checks all domains in parallel, and is guaranteed to return in <code>$timeout</code> seconds. (Actually, it may take up to one second longer.) </p>
<p> The parameters are: </p>
<p> $relay &#8212; the IP address you want to look up </p>
<p> $timeout &#8212; a timeout in seconds after which the function should return </p>
<p> $answers_wanted &#8212; the maximum number of positive answers you care about. For example, if you&#8217;re looking up an address in 10 different RBLs, but are going to bounce it if it is on four or more, you can set $answers_wanted to 4, and the function returns as soon as four &quot;hits&quot; are discovered. If you set $answers_wanted to zero, then the function does not return early. </p>
<p> [$domain1, $domain2, &#8230;] &#8212; a reference to an array of strings, where each string is an RBL domain. </p>
<p> $res &#8212; a Net::DNS::Resolver object. This argument is optional; if you do not supply it, then <code>relay_is_blacklisted_multi</code> constructs its own resolver. </p>
<p> The return value is a reference to a hash; the keys of the hash are the original domains, and the corresponding values are either SERVFAIL, NXDOMAIN, or a list of IP addresses in dotted-quad notation. </p>
<p> Here&#8217;s an example: </p>
<pre> $ans = relay_is_blacklisted_multi($RelayAddr, 8, 0,
 [&quot;sbl.spamhaus.org&quot;, &quot;relays.ordb.org&quot;]);
 foreach $domain (keys(%$ans)) {
 $r = $ans-&gt;{$domain};
 if (ref($r) eq &quot;ARRAY&quot;) {
 # It's an array -- it IS listed in RBL
 print STDERR &quot;Lookup in $domain yields [ &quot;;
 foreach $addr (@$r) {
 print STDERR $addr . &quot; &quot;;
 }
 print STDERR &quot;]
&quot;;
 } else {
 # It is NOT listed in RBL
 print STDERR &quot;Lookup in $domain yields &quot;
 . $ans-&gt;{$domain} . &quot;
&quot;;
 }
 }</pre>
<p>You should compare each of $ans-&gt;{$domain} to &quot;SERVFAIL&quot; and &quot;NXDOMAIN&quot; to see if the relay is <i>not</i> listed. Any other return value will be an array of IP addresses indicating that the relay is listed. </p>
<p> Any lookup that does not succeed within $timeout seconds has the corresponding return value set to SERVFAIL. </p>
<dt><code>relay_is_blacklisted_multi_list($relay, $timeout, $answers_wanted, [$domain1, $domain2, &#8230;], $res)</code></p>
<dd>This function is similar to <code>relay_is_blacklisted_multi</code> except that the return value is simply an array of RBL domains in which the relay was listed. </p>
<dt><code>relay_is_blacklisted_multi_count($relay, $timeout, $answers_wanted, [$domain1, $domain2, &#8230;], $res)</code></p>
<dd>This function is similar to <code>relay_is_blacklisted_multi</code> except that the return value is an integer specifying the number of domains on which the relay was blacklisted. </p>
<dt><code>md_get_bogus_mx_hosts($domain)</code></p>
<dd>This function looks up all the MX records for the specified domain (or A records if there are no MX records) and returns a list of &quot;bogus&quot; IP addresses found amongst the records. A &quot;bogus&quot; IP address is an IP address in a private network (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), the loopback network (127.0.0.0/8), local-link for auto-DHCP (169.254.0.0/16), IPv4 multicast (224.0.0.0/4) or reserved (240.0.0.0/4). </p>
</dl>
<p> Here&#8217;s how you might use the function in filter_sender: </p>
<pre>sub filter_sender {
 my ($sender, $ip, $hostname, $helo) = @_;
 if ($sender =~ /@([^&gt;]+)/) {
 my $domain = $1;
 my @bogushosts = md_get_bogus_mx_hosts($domain);
 if (scalar(@bogushosts)) {
 return('REJECT', &quot;Domain $domain contains bogus MX record(s) &quot; .
 join(', ', @bogushosts));
 }
 }
 return ('CONTINUE', 'ok');
}</pre>
<h2>Test Functions</h2>
<p><code>mimedefang.pl</code> includes some &quot;test&quot; functions: </p>
<dl>
<dt><code>md_version()</code></p>
<dd>returns the version of MIMEDefang as a string (for example, &quot;2.79&quot;). </p>
<dt><code>message_rejected()</code></p>
<dd>Returns true if any of <code>action_tempfail</code>, <code>action_bounce</code> or <code>action_discard</code> have been called for this message; returns false otherwise. </p>
</dl>
<p> If you have the Mail::SpamAssassin Perl module installed (see <a rel="nofollow" href="http://www.spamassassin.org)">http://www.spamassassin.org)</a> you may call any of the spam_assassin_* functions. They should only be called from <code>filter_begin</code> or <code>filter_end</code> because they operate on the entire message at once. Most functions use an optionally provided config file. If no config file is provided, mimedefang.pl will look for one of four default SpamAssassin preference files. The first of the following found will be used: </p>
<dl>
<dt><code>o</code></p>
<dd>/etc/mail/sa-mimedefang.cf</p>
<dt><code>o</code></p>
<dd>/etc/mail/spamassassin/sa-mimedefang.cf</p>
<dt><code>o</code></p>
<dd>/etc/mail/spamassassin/local.cf</p>
<dt><code>o</code></p>
<dd>/etc/mail/spamassassin.cf </p>
</dl>
<p> <code>Important Note</code>: MIMEDefang does <i>not</i> permit SpamAssassin to modify messages. If you want to tag spam messages with special headers or alter the subject line, you must use MIMEDefang functions to do it. Setting SpamAssassin configuration options to alter messages will not work. </p>
<dl>
<dt><code>spam_assassin_is_spam([ $config_file ])</code></p>
<dd>Determine if the current message is SPAM/UCE as determined by SpamAssassin. Compares the score of the message against the threshold score (see below) and returns true if it is. Uses <code>spam_assassin_check</code> below. </p>
<dt><code>spam_assassin_check([ $config_file ])</code></p>
<dd>This function returns a four-element list of the form ($hits, $required, $tests, $report). $hits is the &quot;score&quot; given to the message by SpamAssassin (higher score means more likely SPAM). $required is the number of hits required before SpamAssassin concludes that the message is SPAM. $tests is a comma-separated list of SpamAssassin test names, and $report is text detailing which tests triggered and their point score. This gives you insight into why SpamAssassin concluded that the message is SPAM. Uses <code>spam_assassin_status</code> below.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>spam_assassin_status([ $config_file ])</code></p>
<dd>This function returns a Mail::SpamAssasin::PerMsgStatus object. Read the SpamAssassin documentation for details about this object. You are responsible for calling the <code>finish</code> method when you are done with it. Uses <code>spam_assassin_init</code> and <code>spam_assassin_mail</code> below. </p>
<dt><code>spam_assassin_init([ $config_file ])</code></p>
<dd>This function returns the new global Mail::SpamAssassin object with the specified or default config (outlined above). If the global object is already defined, returns it &#8212; does not change config files! The object can be used to perform other SpamAssassin related functions. </p>
<dt><code>spam_assassin_mail()</code></p>
<dd>This function returns a Mail::SpamAssassin::NoMailAudit object with the current email message contained in it. It may be used to perform other SpamAssassin related functions. </p>
<dt><code>md_copy_orig_msg_to_work_dir()</code></p>
<dd>Normally, virus-scanners are passed only the unpacked, decoded parts of a MIME message. If you want to pass the original, undecoded message in as well, call <code>md_copy_orig_msg_to_work_dir</code> <i>prior to</i> calling <code>message_contains_virus</code>. </p>
<dt><code>md_copy_orig_msg_to_work_dir_as_mbox_file()</code></p>
<dd>Normally, virus-scanners are passed only the unpacked, decoded parts of a MIME message. If you want to pass the original, undecoded message in as a UNIX-style &quot;mbox&quot; file, call <code>md_copy_orig_msg_to_work_dir_as_mbox_file</code> <i>prior to</i> calling <code>message_contains_virus</code>. The only difference between this function and <code>md_copy_orig_msg_to_work_dir</code> is that this function prepends a &quot;From_&quot; line to make the message look like a UNIX-style mbox file. This is required for some virus scanners (such as Clam AntiVirus) to recognize the file as an e-mail message. </p>
<dt><code>message_contains_virus()</code></p>
<dd>This function runs <i>every</i> installed virus-scanner and returns the scanner results. The function should be called in list context; the return value is a three-element list ($code, $category, $action). </p>
<p> $code is the actual return code from the virus scanner. </p>
<p> $category is a string categorizing the return code: </p>
<p> &quot;ok&quot; &#8211; no viruses detected. </p>
<p> &quot;not-installed&quot; &#8211; indicated virus scanner is not installed. </p>
<p> &quot;cannot-execute&quot; &#8211; for some reason, the scanner could not be executed. </p>
<p> &quot;virus&quot; &#8211; a virus was found. </p>
<p> &quot;suspicious&quot; &#8211; a &quot;suspicious&quot; file was found. </p>
<p> &quot;interrupted&quot; &#8211; scanning was interrupted. </p>
<p> &quot;swerr&quot; &#8211; an internal scanner software error occurred. </p>
<p> $action is a string containing the recommended action: </p>
<p> &quot;ok&quot; &#8211; allow the message through unmolested. </p>
<p> &quot;quarantine&quot; &#8211; a virus was detected; quarantine it. </p>
<p> &quot;tempfail&quot; &#8211; something went wrong; tempfail the message. </p>
<dt><code>message_contains_virus_trend()</code></p>
<dd>
<dt><code>message_contains_virus_nai()</code></p>
<dd>
<dt><code>message_contains_virus_bdc()</code></p>
<dd>
<dt><code>message_contains_virus_nvcc()</code></p>
<dd>
<dt><code>message_contains_virus_csav()</code></p>
<dd>
<dt><code>message_contains_virus_fsav()</code></p>
<dd>
<dt><code>message_contains_virus_hbedv()</code></p>
<dd>
<dt><code>message_contains_virus_vexira()</code></p>
<dd>
<dt><code>message_contains_virus_sophos()</code></p>
<dd>
<dt><code>message_contains_virus_clamav()</code></p>
<dd>
<dt><code>message_contains_virus_avp()</code></p>
<dd>
<dt><code>message_contains_virus_avp5()</code></p>
<dd>
<dt><code>message_contains_virus_fprot()</code></p>
<dd>
<dt><code>message_contains_virus_fpscan()</code></p>
<dd>
<dt><code>message_contains_virus_fprotd()</code></p>
<dd>
<dt><code>message_contains_virus_fprotd_v6()</code></p>
<dd>
<dt><code>message_contains_virus_nod32()</code></p>
<dd>These functions should be called in <code>list context</code>. They use the indicated anti-virus software to scan the message for viruses. These functions are intended for use in filter_begin() to make an initial scan of the e-mail message. </p>
<p> The supported virus scanners are:</p>
<dt><code>nai</code></p>
<dd>NAI &quot;uvscan&quot; &#8211; <a rel="nofollow" href="http://www.nai.com/">http://www.nai.com/</a></p>
<dd>Bitdefender &quot;bdc&quot; &#8211; <a rel="nofollow" href="http://www.bitdefender.com/">http://www.bitdefender.com/</a></p>
<dt><code>csav</code></p>
<dd>Command Anti-Virus &#8211; <a rel="nofollow" href="http://www.commandsoftware.com/">http://www.commandsoftware.com/</a></p>
<dt><code>fsav</code></p>
<dd>F-Secure Anti-Virus &#8211; <a rel="nofollow" href="http://www.f-secure.com/">http://www.f-secure.com/</a></p>
<dt><code>hbedv</code></p>
<dd>H+BEDV &quot;AntiVir&quot; &#8211; <a rel="nofollow" href="http://www.hbedv.com/">http://www.hbedv.com/</a></p>
<dt><code>vexira</code></p>
<dd>Vexira &quot;Vexira&quot; &#8211; <a rel="nofollow" href="http://www.centralcommand.com/">http://www.centralcommand.com/</a></p>
<dt><code>sophos</code></p>
<dd>Sophos AntiVirus &#8211; <a rel="nofollow" href="http://www.sophos.com/">http://www.sophos.com/</a></p>
<dt><code>avp</code></p>
<dd>Kaspersky AVP and aveclient (AVP5) &#8211; <a rel="nofollow" href="http://www.avp.ru/">http://www.avp.ru/</a></p>
<dt><code>clamav</code></p>
<dd>Clam AntiVirus &#8211; <a rel="nofollow" href="http://www.clamav.net/">http://www.clamav.net/</a></p>
<dt><code>f-prot</code></p>
<dd>F-RISK F-PROT &#8211; <a rel="nofollow" href="http://www.f-prot.com/">http://www.f-prot.com/</a></p>
<dt><code>nod32cli</code></p>
<dd>ESET NOD32 &#8211; <a rel="nofollow" href="http://www.eset.com/">http://www.eset.com/</a> </p>
<dt><code>message_contains_virus_carrier_scan([$host])</code></p>
<dd>Connects to the specified host:port:local_or_nonlocal (default <code>$CSSHost</code>), where the Symantec CarrierScan Server daemon is expected to be listening. Return values are the same as the other message_contains_virus functions. </p>
<dt><code>message_contains_virus_sophie([$sophie_sock])</code></p>
<dd>Connects to the specified socket (default <code>$SophieSock</code>), where the Sophie daemon is expected to be listening. Return values are the same as the other message_contains_virus functions. </p>
<dt><code>message_contains_virus_clamd([$clamd_sock])</code></p>
<dd>Connects to the specified socket (default <code>$ClamdSock</code>), where the clamd daemon is expected to be listening. Return values are the same as the other message_contains_virus functions. </p>
<dt><code>message_contains_virus_trophie([$trophie_sock])</code></p>
<dd>Connects to the specified socket (default <code>$TrophieSock</code>), where the Trophie daemon is expected to be listening. Return values are the same as the other message_contains_virus functions. </p>
<dt><code>entity_contains_virus($entity)</code></p>
<dd>This function runs the specified MIME::Entity through <i>every</i> installed virus-scanner and returns the scanner results. The return values are the same as for <code>message_contains_virus()</code>. </p>
<dt><code>entity_contains_virus_trend($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_nai($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_bdc($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_nvcc($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_csav($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_fsav($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_hbedv($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_sophos($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_clamav($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_avp($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_avp5($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_fprot($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_fpscan($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_fprotd($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_fprotd_v6($entity)</code></p>
<dd>
<dt><code>entity_contains_virus_nod32($entity)</code></p>
<dd>These functions, meant to be called from filter(), are similar to the message_contains_virus functions except they scan only the current part. They should be called from list context, and their return values are as described for the message_contains_virus functions. </p>
<dt><code>entity_contains_virus_carrier_scan($entity[, $host])</code></p>
<dd>Connects to the specified host:port:local_or_nonlocal (default <code>$CSSHost</code>), where the Symantec CarrierScan Server daemon is expected to be listening. Return values are the same as the other entity_contains_virus functions. </p>
<dt><code>entity_contains_virus_sophie($entity[, $sophie_sock])</code></p>
<dd>Connects to the specified socket (default <code>$SophieSock</code>), where the Sophie daemon is expected to be listening. Return values are the same as the other entity_contains_virus functions. </p>
<dt><code>entity_contains_virus_trophie($entity[, $trophie_sock])</code></p>
<dd>Connects to the specified socket (default <code>$TrophieSock</code>), where the Trophie daemon is expected to be listening. Return values are the same as the other entity_contains_virus functions. </p>
<dt><code>entity_contains_virus_clamd($entity[, $clamd_sock])</code></p>
<dd>Connects to the specified socket (default <code>$ClamdSock</code>), where the clamd daemon is expected to be listening. Return values are the same as the other entity_contains_virus functions. </p>
</dl>
<h2>Smtp Flow</h2>
<p>This section illustrates the flow of messages through MIMEDefang. </p>
<dl>
<dt><code>1. INITIAL CONNECTION</code></p>
<dd>If you invoked <code>mimedefang</code> with the <code>-r</code> option and have defined a filter_relay routine, it is called. </p>
<dt><code>2. SMTP HELO COMMAND</code></p>
<dd>The HELO string is stored internally, but no filter functions are called. </p>
<dt><code>3. SMTP MAIL FROM: COMMAND</code></p>
<dd>If you invoked <code>mimedefang</code> with the <code>-s</code> option and have defined a filter_sender routine, it is called. </p>
<dt><code>4. SMTP RCPT TO: COMMAND</code></p>
<dd>If you invoked <code>mimedefang</code> with the <code>-t</code> option and have defined a filter_recipient routine, it is called. </p>
<dt><code>5. END OF SMTP DATA</code></p>
<dd>filter_begin is called. For each MIME part, filter is called. Then filter_end is called. </p>
</dl>
<h2>Preserving Relay Information</h2>
<p>Most organizations have more than one machine handling internet e-mail. If the primary machine is down, mail is routed to a secondary (or tertiary, etc.) MX server, which stores the mail until the primary MX host comes back up. Mail is then relayed to the primary MX host. </p>
<p> Relaying from a secondary to a primary MX host has the unfortunate side effect of losing the original relay&#8217;s IP address information. MIMEDefang allows you to preserve this information. One way around the problem is to run MIMEDefang on all the secondary MX hosts and use the same filter. However, you may not have control over the secondary MX hosts. If you can persuade the owners of the secondary MX hosts to run MIMEDefang with a simple filter that only preserves relay information and does no other scanning, your primary MX host can obtain relay information and make decisions using $RelayAddr and $RelayHostname. </p>
<p> When you configure MIMEDefang, supply the &quot;&#8211;with-ipheader&quot; argument to the ./configure script. When you install MIMEDefang, a file called <code>/etc/mail/mimedefang-ip-key</code> will be created which contains a randomly-generated header name. Copy this file to all of your mail relays. It is important that all of your MX hosts have the <code>same</code> key. The key should be kept confidential, but it&#8217;s not disastrous if it leaks out. </p>
<p> On your secondary MX hosts, add this line to filter_end: </p>
<pre> add_ip_validation_header();</pre>
<p><i>Note</i>: You should <i>only</i> add the validation header to mail destined for one of your other MX hosts! Otherwise, the validation header will leak out. </p>
<p> When the secondary MX hosts relay to the primary MX host, $RelayAddr and $RelayHostname will be set based on the IP validation header. If MIMEDefang notices this header, it sets the global variable $WasResent to 1. Since you don&#8217;t want to trust the header unless it was set by one of your secondary MX hosts, you should put this code in filter_begin: </p>
<pre> if ($WasResent) {
 if ($RealRelayAddr ne &quot;ip.of.secondary.mx&quot; and
 $RealRelayAddr ne &quot;ip.of.tertiary.mx&quot;) {
 $RelayAddr = $RealRelayAddr;
 $RelayHostname = $RealRelayHostname;
 }
 }</pre>
<p>This resets the relay address and hostname to the actual relay address and hostname, unless the message is coming from one of your other MX hosts. </p>
<p> On the primary MX host, you should add this in filter_begin: </p>
<pre> delete_ip_validation_header();</pre>
<p>This prevents the validation header from leaking out to recipients. </p>
<p> <i>Note</i>: The IP validation header works only in message-oriented functions. It (obviously) has no effect on <code>filter_relay</code>, <code>filter_sender</code> and <code>filter_recipient</code>, because no header information is available yet. You must take this into account when writing your filter; you must defer relay-based decisions to the message filter for mail arriving from your other MX hosts.</p>
<h2>Global Variable Lifetime</h2>
<p>The following list describes the lifetime of global variables (thanks to Tony Nugent for providing this documentation.) </p>
<p> If you set a global variable: </p>
<dl>
<dt><code>Outside a subroutine in your filter file</code></p>
<dd>It is available to all functions, all the time. </p>
<dt><code>In filter_relay, filter_sender or filter_recipient</code></p>
<dd>Not guaranteed to be available to any other function, not even from one filter_recipient call to the next, when receiving a multi-recipient email message. </p>
<dt><code>In filter_begin</code></p>
<dd>Available to filter_begin, filter and filter_end </p>
<dt><code>In filter</code></p>
<dd>Available to filter and filter_end </p>
<dt><code>In filter_end</code></p>
<dd>Available within filter_end </p>
</dl>
<p> The &quot;built-in&quot; globals like $Subject, $Sender, etc. are always available to filter_begin, filter and filter_end. Some are available to filter_relay, filter_sender or filter_recipient, but you should check the documentation of the variable above for details.</p>
<h2>Maintaining State</h2>
<p>There are four basic groups of filtering functions: </p>
<dl>
<dt><code>1</code></p>
<dd>filter_relay </p>
<dt><code>2</code></p>
<dd>filter_sender </p>
<dt><code>3</code></p>
<dd>filter_recipient </p>
<dt><code>4</code></p>
<dd>filter_begin, filter, filter_multipart, filter_end </p>
</dl>
<p> In general, for a given mail message, these groups of functions may be called in completely different Perl processes. Thus, there is <i>no way</i> to maintain state inside Perl between groups of functions. That is, you cannot set a variable in <code>filter_relay</code> and expect it to be available in <code>filter_sender</code>, because the <code>filter_sender</code> invocation might take place in a completely different process. </p>
<p> For a given mail message, it <i>is</i> always the case that <code>filter_begin</code>, <code>filter</code>, <code>filter_multipart</code> and <code>filter_end</code> are called in the same Perl process. Therefore, you can use global variables to carry state among those functions. You should be very careful to initialize such variables in <code>filter_begin</code> to ensure no data leaks from one message to another. </p>
<p> Also for a given mail message, the $CWD global variable holds the message spool directory, and the current working directory is set to $CWD. Therefore, you can store state in files inside $CWD. If <code>filter_sender</code> stores data in a file inside $CWD, then <code>filter_recipient</code> can retrieve that data. </p>
<p> Since <code>filter_relay</code> is called directly after a mail connection is established, there is no message context yet, no per-message mimedefang spool directory, and the $CWD global is not set. Therefore, it is not possible to share information from <code>filter_relay</code> to one of the other filter functions. The only thing that <code>filter_relay</code> has in common with the other functions are the values in the globals $RelayAddr, and $RelayHostname. These could be used to access per-remote-host information in some database. </p>
<p> Inside $CWD, we reserve filenames beginning with upper-case letters for internal MIMEDefang use. If you want to create files to store state, name them beginning with a lower-case letter to avoid clashes with future releases of MIMEDefang.</p>
<h2>Socket Maps</h2>
<p>If you have Sendmail 8.13 or later, and have compiled it with the SOCKETMAP option, then you can use a special map type that communicates over a socket with another program (rather than looking up a key in a Berkeley database, for example.) </p>
<p> <code>mimedefang-multiplexor</code> implements the Sendmail SOCKETMAP protocol if you supply the <code>-N</code> option. In that case, you can define a function called <code>filter_map</code> to implement map lookups. <code>filter_map</code> takes two arguments: $mapname is the name of the Sendmail map (as given in the K sendmail configuration directive), and $key is the key to be looked up. </p>
<p> <code>filter_map</code> must return a two-element list: ($code, $val) $code can be one of: </p>
<dl>
<dt><code>OK</code></p>
<dd>The lookup was successful. In this case, $val must be the result of the lookup </p>
<dt><code>NOTFOUND</code></p>
<dd>The lookup was unsuccessful &#8212; the key was not found. In this case, $val should be the empty string. </p>
<dt><code>TEMP</code></p>
<dd>There was a temporary failure of some kind. $val can be an explanatory error message. </p>
<dt><code>TIMEOUT</code></p>
<dd>There was a timeout of some kind. $val can be an explanatory error message. </p>
<dt><code>PERM</code></p>
<dd>There was a permanent failure. This is <i>not</i> the same as an unsuccessful lookup; it should be used only to indicate a serious misconfiguration. As before, $val can be an explanatory error message. </p>
</dl>
<p> Consider this small example. Here is a minimal Sendmail configuration file: </p>
<pre> V10/Berkeley
 Kmysock socket unix:/var/spool/MIMEDefang/map.sock
 kothersock socket unix:/var/spool/MIMEDefang/map.sock</pre>
<p>If <code>mimedefang-multiplexor</code> is invoked with the arguments <code>-N unix:/var/spool/MIMEDefang/map.sock</code>, and the filter defines <code>filter_map</code> as follows: </p>
<pre> sub filter_map ($$) {
 my($mapname, $key) = @_;
 my $ans;
 if($mapname ne &quot;mysock&quot;) {
 return(&quot;PERM&quot;, &quot;Unknown map $mapname&quot;);
 }
 $ans = reverse($key);
 return (&quot;OK&quot;, $ans);
 }</pre>
<p>Then in Sendmail&#8217;s testing mode, we see the following: </p>
<pre> &gt; /map mysock testing123
 map_lookup: mysock (testing123) returns 321gnitset (0)
 &gt; /map othersock foo
 map_lookup: othersock (foo) no match (69)</pre>
<p>(The return code of 69 means EX_UNAVAILABLE or Service Unavailable) </p>
<p> A real-world example could do map lookups in an LDAP directory or SQL database, or perform other kinds of processing. You can even implement standard Sendmail maps like virtusertable, mailertable, access_db, etc. using SOCKETMAP.</p>
<h2>Tick Requests</h2>
<p>If you supply the <code>-X</code> option to <code>mimedefang-multiplexor</code>, then every so often, a &quot;tick&quot; request is sent to a free slave. If your filter defines a function called <code>filter_tick</code>, then this function is called with a single argument: the tick type. If you run multiple parallel ticks, then each tick has a type ranging from 0 to <i>n</i>-1, where <i>n</i> is the number of parallel ticks. If you&#8217;re only running one tick request, then the argument to <code>filter_tick</code> is always 0. </p>
<p> You can use this facility to run periodic tasks from within MIMEDefang. Note, however, that you have no control over which slave is picked to run <code>filter_tick</code>. Also, at most one <code>filter_tick</code> call with a particular &quot;type&quot; argument will be active at any time, and if there are no free slaves when a tick would occur, the tick is skipped.</p>
<h2>Supported Virus Scanners</h2>
<p>The following virus scanners are supported by MIMEDefang: </p>
<dl>
<dt><code>o</code></p>
<dd>Symantec CarrierScan Server (<a rel="nofollow" href="http://www.symantec.com/region/can/eng/product/scs/)">http://www.symantec.com/region/can/eng/product/scs/)</a> </p>
<dt><code>o</code></p>
<dd>Trend Micro vscan (<a rel="nofollow" href="http://www.antivirus.com/)">http://www.antivirus.com/)</a> </p>
<dt><code>o</code></p>
<dd>Sophos Sweep (<a rel="nofollow" href="http://www.sophos.com/products/antivirus/savunix.html)">http://www.sophos.com/products/antivirus/savunix.html)</a> </p>
<dt><code>o</code></p>
<dd>H+BEDV AntiVir (<a rel="nofollow" href="http://www.hbedv.com/)">http://www.hbedv.com/)</a> </p>
<dt><code>o</code></p>
<dd>Central Command Vexira (<a rel="nofollow" href="http://www.centralcommand.com/)">http://www.centralcommand.com/)</a> </p>
<dt><code>o</code></p>
<dd>NAI uvscan (<a rel="nofollow" href="http://www.nai.com)">http://www.nai.com)</a> </p>
<dt><code>o</code></p>
<dd>Bitdefender bdc (<a rel="nofollow" href="http://www.bitdefender.com)">http://www.bitdefender.com)</a> </p>
<dt><code>o</code></p>
<dd>Norman Virus Control (NVCC) (<a rel="nofollow" href="http://www.norman.no/)">http://www.norman.no/)</a> </p>
<dt><code>o</code></p>
<dd>Command csav (<a rel="nofollow" href="http://www.commandsoftware.com)">http://www.commandsoftware.com)</a> </p>
<dt><code>o</code></p>
<dd>F-Secure fsav (<a rel="nofollow" href="http://www.f-secure.com)">http://www.f-secure.com)</a> </p>
<dt><code>o</code></p>
<dd>The clamscan command-line scanner and the clamd daemon from Clam AntiVirus (<a rel="nofollow" href="http://www.clamav.net/)">http://www.clamav.net/)</a> </p>
<dt><code>o</code></p>
<dd>Kaspersky Anti-Virus (AVP) (<a rel="nofollow" href="http://www.kaspersky.com/)">http://www.kaspersky.com/)</a> </p>
<dt><code>o</code></p>
<dd>F-Risk F-Prot (<a rel="nofollow" href="http://www.f-prot.com/)">http://www.f-prot.com/)</a> </p>
<dt><code>o</code></p>
<dd>F-Risk F-Prot v6 (<a rel="nofollow" href="http://www.f-prot.com/)">http://www.f-prot.com/)</a> </p>
<dt><code>o</code></p>
<dd>F-Risk FPROTD (daemonized version of F-Prot) </p>
<dt><code>o</code></p>
<dd>Symantec CarrierScan Server (<a rel="nofollow" href="http://www.symantec.ca/region/can/eng/product/scs/buymenu.html)">http://www.symantec.ca/region/can/eng/product/scs/buymenu.html)</a> </p>
<dt><code>o</code></p>
<dd>Sophie (<a rel="nofollow" href="http://www.vanja.com/tools/sophie/">http://www.vanja.com/tools/sophie/</a>), which uses the libsavi library from Sophos, is supported in daemon-scanning mode. </p>
<dt><code>o</code></p>
<dd>Trophie (<a rel="nofollow" href="http://www.vanja.com/tools/trophie/">http://www.vanja.com/tools/trophie/</a>), which uses the libvsapi library from Trend Micro, is supported in daemon-scanning mode. </p>
<dt><code>o</code></p>
<dd>ESET NOD32 (<a rel="nofollow" href="http://www.eset.com/)">http://www.eset.com/)</a> </p>
</dl>
<h2>Authors</h2>
<p><code>mimedefang</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8) </p>
