---
title: "hosts_options(5)"
name: "hosts_options"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hosts_options/"
---

hosts_options - host access control language extensions

<h2>Description</h2>

This document describes extensions to the language described in the <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) document. 

 The extensible language uses the following format: 

 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp; daemon_list : client_list : option : option ... 

 The first two fields are described in the <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) manual page. The remainder of the rules is a list of zero or more options. Any &quot;:&quot; characters within options should be protected with a backslash. 

 An option is of the form &quot;keyword&quot; or &quot;keyword value&quot;. Options are processed in the specified order. Some options are subjected to %&lt;letter&gt; substitutions. For the sake of backwards compatibility with earlier versions, an &quot;=&quot; is permitted between keyword and value.

<h2>Logging</h2>

<dl><dt>severity mail.info
<dd><dt>severity notice
<dd>Change the severity level at which the event will be logged. Facility names (such as mail) are optional, and are not supported on systems with older syslog implementations. The severity option can be used to emphasize or to ignore specific events.</dl>

<h2>Access Control</h2>

<dl><dt>allow
<dd><dt>deny
<dd>Grant (deny) service. These options must appear at the end of a rule.</dl>
 

 The <i>allow</i> and <i>deny</i> keywords make it possible to keep all access control rules within a single file, for example in the <i>hosts.allow</i> file. 

 To permit access from specific hosts only: 

 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp; ALL: .friendly.domain: ALLOW 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp; ALL: ALL: DENY 

 To permit access from all hosts except a few trouble makers: 

 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp; ALL: .bad.domain: DENY 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp; ALL: ALL: ALLOW 

 Notice the leading dot on the domain name patterns.

<h2>Running Other Commands</h2>

<dl><dt>aclexec shell_command
<dd>Execute, in a child process, the specified shell command, after performing the %&lt;letter&gt; expansions described in the <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) manual page. The command is executed with stdin, stdout and stderr connected to the null device, so that it won't mess up the conversation with the client host. Example: 

 <pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;smtp : ALL : aclexec checkdnsbl %a</pre>executes, in a background child process, the shell command &quot;checkdnsbl %a&quot; after replacing %a by the address of the remote host. 

 The connection will be allowed or refused depending on whether the command returns a true or false exit status.
<dt>spawn shell_command
<dd>Execute, in a child process, the specified shell command, after performing the %&lt;letter&gt; expansions described in the <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) manual page. The command is executed with stdin, stdout and stderr connected to the null device, so that it won't mess up the conversation with the client host. Example: 

 <pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;spawn (/usr/sbin/safe_finger -l @%h | /usr/bin/mail root) &amp;</pre>executes, in a background child process, the shell command &quot;safe_finger -l @%h | mail root&quot; after replacing %h by the name or address of the remote host. 

 The example uses the &quot;safe_finger&quot; command instead of the regular &quot;finger&quot; command, to limit possible damage from data sent by the finger server. The &quot;safe_finger&quot; command is part of the daemon wrapper package; it is a wrapper around the regular finger command that filters the data sent by the remote host.
<dt>twist shell_command
<dd>Replace the current process by an instance of the specified shell command, after performing the %&lt;letter&gt; expansions described in the <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) manual page. Stdin, stdout and stderr are connected to the client process. This option must appear at the end of a rule. 

 To send a customized bounce message to the client instead of running the real ftp daemon: 

 <pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;in.ftpd : ... : twist /bin/echo 421 Some bounce message</pre>For an alternative way to talk to client processes, see the <i>banners</i> option below. 

 To run /some/other/in.telnetd without polluting its command-line array or its process environment: 

 <pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;in.telnetd : ... : twist PATH=/some/other; exec in.telnetd</pre>Warning: in case of UDP services, do not twist to commands that use the standard I/O or the <a HREF="/docs/linux/man/2-read/">read</a>(2)/<a HREF="/docs/linux/man/2-write/">write</a>(2) routines to communicate with the client process; UDP requires other I/O primitives.</dl>

<h2>Network Options</h2>

<dl><dt>keepalive
<dd>Causes the server to periodically send a message to the client. The connection is considered broken when the client does not respond. The keepalive option can be useful when users turn off their machine while it is still connected to a server. The keepalive option is not useful for datagram (UDP) services.
<dt>linger number_of_seconds
<dd>Specifies how long the kernel will try to deliver not-yet delivered data after the server process closes a connection.</dl>

<h2>Username Lookup</h2>

<dl><dt>rfc931 [ timeout_in_seconds ]
<dd>Look up the client user name with the RFC 931 (TAP, IDENT, RFC 1413) protocol. This option is silently ignored in case of services based on transports other than TCP. It requires that the client system runs an RFC 931 (IDENT, etc.) -compliant daemon, and may cause noticeable delays with connections from non-UNIX clients. The timeout period is optional. If no timeout is specified a compile-time defined default value is taken.</dl>

<h2>Miscellaneous</h2>

<dl><dt>banners /some/directory
<dd>Look for a file in `/some/directory' with the same name as the daemon process (for example in.telnetd for the telnet service), and copy its contents to the client. Newline characters are replaced by carriage-return newline, and %&lt;letter&gt; sequences are expanded (see the <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) manual page). 

 The tcp wrappers source code distribution provides a sample makefile (Banners.Makefile) for convenient banner maintenance. 

 Warning: banners are supported for connection-oriented (TCP) network services only.
<dt>nice [ number ]
<dd>Change the nice value of the process (default 10). Specify a positive value to spend more CPU resources on other processes.
<dt>setenv name value
<dd>Place a (name, value) pair into the process environment. The value is subjected to %&lt;letter&gt; expansions and may contain whitespace (but leading and trailing blanks are stripped off). 

 Warning: many network daemons reset their environment before spawning a login or shell process.
<dt>umask 022
<dd>Like the umask command that is built into the shell. An umask of 022 prevents the creation of files with group and world write permission. The umask argument should be an octal number.
<dt>user nobody
<dd><dt>user nobody.kmem
<dd>Assume the privileges of the &quot;nobody&quot; userid (or user &quot;nobody&quot;, group &quot;kmem&quot;). The first form is useful with inetd implementations that run all services with root privilege. The second form is useful for services that need special group privileges only.</dl>

<h2>Diagnostics</h2>

When a syntax error is found in an access control rule, the error is reported to the syslog daemon; further options will be ignored, and service is denied.

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5), the default access control language

<h2>Author</h2>

<pre>Wietse Venema (wietse [at] wzv.win.tue.nl)
Department of Mathematics and Computing Science
Eindhoven University of Technology
Den Dolech 2, P.O. Box 513, 
5600 MB Eindhoven, The Netherlands</pre>
