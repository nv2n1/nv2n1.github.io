---
title: "hosts_access(5)"
name: "hosts_access"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hosts_access/"
description: "hosts_access – format of host access control files"
---

<p>hosts_access &#8211; format of host access control files</p>
<h2>Description</h2>
<p>This manual page describes a simple access control language that is based on client (host name/address, user name), and server (process name, host name/address) patterns. Examples are given at the end. The impatient reader is encouraged to skip to the EXAMPLES section for a quick introduction. </p>
<p> The extended version of the access control language is described in the <i><a href="/docs/linux/man/5-hosts_options/">hosts_options</a></i>(5) document. <code>Note that this language supersedes the meaning of </code><i>shell_command</i><code> as documented below.</code> </p>
<p> In the following text, <i>daemon</i> is the process name of a network daemon process, and <i>client</i> is the name and/or address of a host requesting service. Network daemon process names are specified in the inetd configuration file.</p>
<h2>Access Control Files</h2>
<p>The access control software consults two files. The search stops at the first match:</p>
<dl>
<dt>&bull;</p>
<dd>Access will be granted when a (daemon,client) pair matches an entry in the <i>/etc/hosts.allow</i> file.</p>
<dt>&bull;</p>
<dd>Otherwise, access will be denied when a (daemon,client) pair matches an entry in the <i>/etc/hosts.deny</i> file.</p>
<dt>&bull;</p>
<dd>Otherwise, access will be granted.</dl>
<p> A non-existing access control file is treated as if it were an empty file. Thus, access control can be turned off by providing no access control files.</p>
<h2>Access Control Rules</h2>
<p>Each access control file consists of zero or more lines of text. These lines are processed in order of appearance. The search terminates when a match is found.</p>
<dl>
<dt>&bull;</p>
<dd>A newline character is ignored when it is preceded by a backslash character. This permits you to break up long lines so that they are easier to edit.</p>
<dt>&bull;</p>
<dd>Blank lines or lines that begin with a `#&#8217; character are ignored. This permits you to insert comments and whitespace so that the tables are easier to read.</p>
<dt>&bull;</p>
<dd>All other lines should satisfy the following format, things between [] being optional: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp; daemon_list : client_list [ : shell_command ]</dl>
<p> <i>daemon_list</i> is a list of one or more daemon process names (argv[0] values) or server port numbers or wildcards (see below). </p>
<p> <i>client_list</i> is a list of one or more host names, host addresses, patterns or wildcards (see below) that will be matched against the client host name or address. </p>
<p> The more complex forms <i>daemon [at] host</i> and <i>user [at] host</i> are explained in the sections on server endpoint patterns and on client username lookups, respectively. </p>
<p> List elements should be separated by blanks and/or commas. </p>
<p> With the exception of NIS (YP) netgroup lookups, all access control checks are case insensitive.</p>
<h2>Patterns</h2>
<p>The access control language implements the following patterns:</p>
<dl>
<dt>&bull;</p>
<dd>A string that begins with a `.&#8217; character. A host name is matched if the last components of its name match the specified pattern. For example, the pattern `.tue.nl&#8217; matches the host name `wzv.win.tue.nl&#8217;.</p>
<dt>&bull;</p>
<dd>A string that ends with a `.&#8217; character. A host address is matched if its first numeric fields match the given string. For example, the pattern `131.155.&#8217; matches the address of (almost) every host on the Eindhoven University network (131.155.x.x).</p>
<dt>&bull;</p>
<dd>A string that begins with an `@&#8217; character is treated as an NIS (formerly YP) netgroup name. A host name is matched if it is a host member of the specified netgroup. Netgroup matches are not supported for daemon process names or for client user names.</p>
<dt>&bull;</p>
<dd>An expression of the form `n.n.n.n/m.m.m.m&#8217; is interpreted as a `net/mask&#8217; pair. An IPv4 host address is matched if `net&#8217; is equal to the bitwise AND of the address and the `mask&#8217;. For example, the net/mask pattern `131.155.72.0/255.255.254.0&#8242; matches every address in the range `131.155.72.0&#8242; through `131.155.73.255&#8242;. `255.255.255.255&#8242; is not a valid mask value, so a single host can be matched just by its IP.</p>
<dt>&bull;</p>
<dd>An expression of the form `n.n.n.n/mm&#8217; is interpreted as a `net/masklength&#8217; pair, where `mm&#8217; is the number of consecutive `1&#8242; bits in the netmask applied to the `n.n.n.n&#8217; address.</p>
<dt>&bull;</p>
<dd>An expression of the form `[n:n:n:n:n:n:n:n]/m&#8217; is interpreted as a `[net]/prefixlen&#8217; pair. An IPv6 host address is matched if `prefixlen&#8217; bits of `net&#8217; is equal to the `prefixlen&#8217; bits of the address. For example, the [net]/prefixlen pattern `[3ffe:505:2:1::]/64&#8242; matches every address in the range `3ffe:505:2:1::&#8217; through `3ffe:505:2:1:ffff:ffff:ffff:ffff&#8217;.</p>
<dt>&bull;</p>
<dd>A string that begins with a `/&#8217; character is treated as a file name. A host name or address is matched if it matches any host name or address pattern listed in the named file. The file format is zero or more lines with zero or more host name or address patterns separated by whitespace. A file name pattern can be used anywhere a host name or address pattern can be used.</p>
<dt>&bull;</p>
<dd>Wildcards `*&#8217; and `?&#8217; can be used to match hostnames or IP addresses. This method of matching cannot be used in conjunction with `net/mask&#8217; matching, hostname matching beginning with `.&#8217; or IP address matching ending with `.&#8217;.</dl>
<h2>Wildcards</h2>
<p>The access control language supports explicit wildcards:</p>
<dl>
<dt>ALL</p>
<dd>The universal wildcard, always matches.</p>
<dt>LOCAL</p>
<dd>Matches any host whose name does not contain a dot character.</p>
<dt>UNKNOWN</p>
<dd>Matches any user whose name is unknown, and matches any host whose name <i>or</i> address are unknown. This pattern should be used with care: host names may be unavailable due to temporary name server problems. A network address will be unavailable when the software cannot figure out what type of network it is talking to.</p>
<dt>KNOWN</p>
<dd>Matches any user whose name is known, and matches any host whose name <i>and</i> address are known. This pattern should be used with care: host names may be unavailable due to temporary name server problems. A network address will be unavailable when the software cannot figure out what type of network it is talking to.</p>
<dt>PARANOID</p>
<dd>Matches any host whose name does not match its address. When tcpd is built with -DPARANOID (default mode), it drops requests from such clients even before looking at the access control tables. Build without -DPARANOID when you want more control over such requests.</dl>
<h2>Operators</h2>
<dl>
<dt>EXCEPT</p>
<dd>Intended use is of the form: `list_1 EXCEPT list_2&#8242;; this construct matches anything that matches <i>list_1</i> unless it matches <i>list_2</i>. The EXCEPT operator can be used in daemon_lists and in client_lists. The EXCEPT operator can be nested: if the control language would permit the use of parentheses, `a EXCEPT b EXCEPT c&#8217; would parse as `(a EXCEPT (b EXCEPT c))&#8217;.
</dl>
<h2>Shell Commands</h2>
<p>If the first-matched access control rule contains a shell command, that command is subjected to %&lt;letter&gt; substitutions (see next section). The result is executed by a <i>/bin/sh</i> child process with standard input, output and error connected to <i>/dev/null</i>. Specify an `&amp;&#8217; at the end of the command if you do not want to wait until it has completed. </p>
<p> Shell commands should not rely on the PATH setting of the inetd. Instead, they should use absolute path names, or they should begin with an explicit PATH=whatever statement. </p>
<p> The <i><a href="/docs/linux/man/5-hosts_options/">hosts_options</a></i>(5) document describes an alternative language that uses the shell command field in a different and incompatible way.</p>
<h2>% Expansions</h2>
<p>The following expansions are available within shell commands:</p>
<dl>
<dt>%a (%A)</p>
<dd>The client (server) host address.</p>
<dt>%c</p>
<dd>Client information: user [at] host, user [at] address, a host name, or just an address, depending on how much information is available.</p>
<dt>%d</p>
<dd>The daemon process name (argv[0] value).</p>
<dt>%h (%H)</p>
<dd>The client (server) host name or address, if the host name is unavailable.</p>
<dt>%n (%N)</p>
<dd>The client (server) host name (or &quot;unknown&quot; or &quot;paranoid&quot;).</p>
<dt>%r (%R)</p>
<dd>The clients (servers) port number (or &quot;0&quot;).</p>
<dt>%p</p>
<dd>The daemon process id.</p>
<dt>%s</p>
<dd>Server information: daemon [at] host, daemon [at] address, or just a daemon name, depending on how much information is available.</p>
<dt>%u</p>
<dd>The client user name (or &quot;unknown&quot;).</p>
<dt>%%</p>
<dd>Expands to a single `%&#8217; character.</dl>
<p> Characters in % expansions that may confuse the shell are replaced by underscores.</p>
<h2>Server Endpoint Patterns</h2>
<p>In order to distinguish clients by the network address that they connect to, use patterns of the form: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp; process_name [at] host_pattern : client_list &#8230; </p>
<p> Patterns like these can be used when the machine has different internet addresses with different internet hostnames. Service providers can use this facility to offer FTP, GOPHER or WWW archives with internet names that may even belong to different organizations. See also the `twist&#8217; option in the <a href="/docs/linux/man/5-hosts_options/">hosts_options</a>(5) document. Some systems (Solaris, FreeBSD) can have more than one internet address on one physical interface; with other systems you may have to resort to SLIP or PPP pseudo interfaces that live in a dedicated network address space. </p>
<p> The host_pattern obeys the same syntax rules as host names and addresses in client_list context. Usually, server endpoint information is available only with connection-oriented services.</p>
<h2>Client Username Lookup</h2>
<p>When the client host supports the RFC 931 protocol or one of its descendants (TAP, IDENT, RFC 1413) the wrapper programs can retrieve additional information about the owner of a connection. Client username information, when available, is logged together with the client host name, and can be used to match patterns like: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp; daemon_list : &#8230; user_pattern [at] host_pattern &#8230; </p>
<p> The daemon wrappers can be configured at compile time to perform rule-driven username lookups (default) or to always interrogate the client host. In the case of rule-driven username lookups, the above rule would cause username lookup only when both the <i>daemon_list</i> and the <i>host_pattern</i> match. </p>
<p> A user pattern has the same syntax as a daemon process pattern, so the same wildcards apply (netgroup membership is not supported). One should not get carried away with username lookups, though.</p>
<dl>
<dt>&bull;</p>
<dd>The client username information cannot be trusted when it is needed most, i.e. when the client system has been compromised. In general, ALL and (UN)KNOWN are the only user name patterns that make sense.</p>
<dt>&bull;</p>
<dd>Username lookups are possible only with TCP-based services, and only when the client host runs a suitable daemon; in all other cases the result is &quot;unknown&quot;.</p>
<dt>&bull;</p>
<dd>A well-known UNIX kernel bug may cause loss of service when username lookups are blocked by a firewall. The wrapper README document describes a procedure to find out if your kernel has this bug.</p>
<dt>&bull;</p>
<dd>Username lookups may cause noticeable delays for non-UNIX users. The default timeout for username lookups is 10 seconds: too short to cope with slow networks, but long enough to irritate PC users.</dl>
<p> Selective username lookups can alleviate the last problem. For example, a rule like: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp; daemon_list : @pcnetgroup ALL@ALL </p>
<p> would match members of the pc netgroup without doing username lookups, but would perform username lookups with all other systems.</p>
<h2>Detecting Address Spoofing Attacks</h2>
<p>A flaw in the sequence number generator of many TCP/IP implementations allows intruders to easily impersonate trusted hosts and to break in via, for example, the remote shell service. The IDENT (RFC931 etc.) service can be used to detect such and other host address spoofing attacks. </p>
<p> Before accepting a client request, the wrappers can use the IDENT service to find out that the client did not send the request at all. When the client host provides IDENT service, a negative IDENT lookup result (the client matches `UNKNOWN [at] host&#8217;) is strong evidence of a host spoofing attack. </p>
<p> A positive IDENT lookup result (the client matches `KNOWN [at] host&#8217;) is less trustworthy. It is possible for an intruder to spoof both the client connection and the IDENT lookup, although doing so is much harder than spoofing just a client connection. It may also be that the client&#8217;s IDENT server is lying. </p>
<p> Note: IDENT lookups don&#8217;t work with UDP services.</p>
<h2>Examples</h2>
<p>The language is flexible enough that different types of access control policy can be expressed with a minimum of fuss. Although the language uses two access control tables, the most common policies can be implemented with one of the tables being trivial or even empty. </p>
<p> When reading the examples below it is important to realize that the allow table is scanned before the deny table, that the search terminates when a match is found, and that access is granted when no match is found at all. </p>
<p> The examples use host and domain names. They can be improved by including address and/or network/netmask information, to reduce the impact of temporary name server lookup failures.</p>
<h2>Mostly Closed</h2>
<p>In this case, access is denied by default. Only explicitly authorized hosts are permitted access. </p>
<p> The default policy (no access) is implemented with a trivial deny file: </p>
<p> /etc/hosts.deny: ALL: ALL </p>
<p> This denies all service to all hosts, unless they are permitted access by entries in the allow file. </p>
<p> The explicitly authorized hosts are listed in the allow file. For example: </p>
<p> /etc/hosts.allow: ALL: LOCAL @some_netgroup<br />
 ALL: .foobar.edu EXCEPT terminalserver.foobar.edu </p>
<p> The first rule permits access from hosts in the local domain (no `.&#8217; in the host name) and from members of the <i>some_netgroup</i> netgroup. The second rule permits access from all hosts in the <i>foobar.edu</i> domain (notice the leading dot), with the exception of <i>terminalserver.foobar.edu</i>.</p>
<h2>Mostly Open</h2>
<p>Here, access is granted by default; only explicitly specified hosts are refused service. </p>
<p> The default policy (access granted) makes the allow file redundant so that it can be omitted. The explicitly non-authorized hosts are listed in the deny file. For example: </p>
<p> /etc/hosts.deny: ALL: some.host.name, .some.domain<br />
 ALL EXCEPT in.fingerd: other.host.name, .other.domain </p>
<p> The first rule denies some hosts and domains all services; the second rule still permits finger requests from other hosts and domains.</p>
<h2>Booby Traps</h2>
<p>The next example permits tftp requests from hosts in the local domain (notice the leading dot). Requests from any other hosts are denied. Instead of the requested file, a finger probe is sent to the offending host. The result is mailed to the superuser. </p>
<p> /etc/hosts.allow: </p>
<pre>in.tftpd: LOCAL, .my.domain
/etc/hosts.deny:
in.tftpd: ALL: (/usr/sbin/safe_finger -l @%h | \
 /usr/bin/mail -s %d-%h root) &amp;</pre>
<p>The safe_finger command comes with the tcpd wrapper and should be installed in a suitable place. It limits possible damage from data sent by the remote finger server. It gives better protection than the standard finger command. </p>
<p> The expansion of the %h (client host) and %d (service name) sequences is described in the section on shell commands. </p>
<p> Warning: do not booby-trap your finger daemon, unless you are prepared for infinite finger loops. </p>
<p> On network firewall systems this trick can be carried even further. The typical network firewall only provides a limited set of services to the outer world. All other services can be &quot;bugged&quot; just like the above tftp example. The result is an excellent early-warning system.</p>
<h2>Diagnostics</h2>
<p>An error is reported when a syntax error is found in a host access control rule; when the length of an access control rule exceeds the capacity of an internal buffer; when an access control rule is not terminated by a newline character; when the result of %&lt;letter&gt; expansion would overflow an internal buffer; when a system call fails that shouldn&#8217;t. All problems are reported via the syslog daemon.</p>
<h2>Files</h2>
<pre>/etc/hosts.allow, (daemon,client) pairs that are granted access.
/etc/hosts.deny, (daemon,client) pairs that are denied access.</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-hosts_options/">hosts_options</a>(5) extended syntax.
<a href="//www.systutorials.com/docs/linux/man/8-tcpd/">tcpd</a>(8) tcp/ip daemon wrapper program.
<a href="//www.systutorials.com/docs/linux/man/8-tcpdchk/">tcpdchk</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-tcpdmatch/">tcpdmatch</a>(8), test programs.</pre>
<h2>Bugs</h2>
<p>If a name server lookup times out, the host name will not be available to the access control software, even though the host is registered. </p>
<p> Domain name server lookups are case insensitive; NIS (formerly YP) netgroup lookups are case sensitive.</p>
<h2>Author</h2>
<pre>Wietse Venema (wietse [at] wzv.win.tue.nl)
Department of Mathematics and Computing Science
Eindhoven University of Technology
Den Dolech 2, P.O. Box 513, 
5600 MB Eindhoven, The Netherlands</pre>
