---
title: "hydra(1)"
name: "hydra"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hydra/"
description: "hydra – a very fast network logon cracker which support many different services"
---

<h2>NAME</h2>
<p> hydra &#8211; a very fast network logon cracker which support many different services</p>
<h2>SYNOPSIS</h2>
<p> <code>hydra</code><br />
&nbsp;<wbr>[[[-l LOGIN|-L FILE]&nbsp;<wbr>[-p PASS|-P FILE|-x OPT]]&nbsp;<wbr>|&nbsp;<wbr>[-C FILE]]&nbsp;<wbr>[-e nsr]<br />
&nbsp;<wbr>[-u]&nbsp;<wbr>[-f]&nbsp;<wbr>[-F]&nbsp;<wbr>[-M FILE]&nbsp;<wbr>[-o FILE]&nbsp;<wbr>[-t TASKS]&nbsp;<wbr>[-w TIME]&nbsp;<wbr>[-W TIME]<br />
&nbsp;<wbr>[-s PORT]&nbsp;<wbr>[-S]&nbsp;<wbr>[-4/6]&nbsp;<wbr>[-vV]&nbsp;<wbr>[-d]<br />
&nbsp;<wbr>server service&nbsp;<wbr>[OPTIONAL_SERVICE_PARAMETER] </p>
<h2>DESCRIPTION</h2>
<p> Hydra is a parallized login cracker which supports numerous protocols to attack. New modules are easy to add, beside that, it is flexible and very fast. </p>
<p> This tool gives researchers and security consultants the possiblity to show how easy it would be to gain unauthorized access from remote to a system. </p>
<p> Currently this tool supports:<br />
&nbsp;<wbr>AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP, FTPS,&nbsp;<wbr><br />
&nbsp;<wbr>HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-PROXY,<br />
&nbsp;<wbr>HTTP-PROXY-URLENUM, ICQ, IMAP, IRC, LDAP2, LDAP3, MS-SQL, MYSQL, NCP, NNTP,<br />
&nbsp;<wbr>Oracle, Oracle-Listener, Oracle-SID, PC-Anywhere, PCNFS, POP3, POSTGRES,<br />
&nbsp;<wbr>RDP, REXEC, RLOGIN, RSH, SAP/R3, SIP, SMB, SMTP, SMTP-Enum, SNMP,<br />
&nbsp;<wbr>SOCKS5, SSH(v1 and v2), SSHKEY, Subversion, Teamspeak&nbsp;<wbr>(TS2), Telnet,<br />
&nbsp;<wbr>VMware-Auth, VNC and XMPP.<br />
&nbsp;<wbr>For most protocols, SSL mode is available&nbsp;<wbr>(e.g. https-get, ftp-ssl, etc.)<br />
&nbsp;<wbr>If not all necessary libraries are found during compile time, your<br />
&nbsp;<wbr>available services will be less. Type&nbsp;<wbr>&quot;hydra&quot;&nbsp;<wbr>to see what is available.</p>
<h2>Options</h2>
<dl>
<dt><code>target</code></p>
<dd> a target to attack, can be an IPv4 address, IPv6 address or DNS name.</p>
<dt><code>service</code></p>
<dd> a service to attack, see the list of protocols available</p>
<dt><code>OPTIONAL SERVICE PARAMETER</code></p>
<dd> Some modules have optional or mandatory options. type &quot;hydra -U &lt;servicename&gt;&quot;<br />
&nbsp;<wbr>to get help on on the options of a service.</p>
<dt><code>-R </code></p>
<dd> restore a previously aborted session. Requires a hydra.restore file was written. No other options are allowed when using -R</p>
<dt><code>-S</code></p>
<dd> connect via SSL</p>
<dt><code>-s PORT</code></p>
<dd> if the service is on a different default port, define it here</p>
<dt><code>-l LOGIN</code></p>
<dd> or -L FILE login with LOGIN name, or load several logins from FILE</p>
<dt><code>-p PASS</code></p>
<dd> or -P FILE try password PASS, or load several passwords from FILE</p>
<dt><code>-x min:max:charset</code></p>
<dd> generate passwords from min to max length. charset can contain 1<br />
&nbsp;<wbr>for numbers, a for lowcase and A for upcase characters.<br />
&nbsp;<wbr>Any other character is added is put to the list.&nbsp;<wbr><br />
Example: 1:2:a1%.<br />
The generated passwords will be of length 1 to 2 and contain<br />
lowcase letters, numbers and/or percent signs and dots.</p>
<dt><code>-e nsr</code></p>
<dd> additional checks, &quot;n&quot; for null password, &quot;s&quot; try login as pass, &quot;r&quot; try the reverse login as pass</p>
<dt><code>-C FILE</code></p>
<dd> colon separated &quot;login:pass&quot; format, instead of -L/-P options</p>
<dt><code>-u</code></p>
<dd> by default Hydra checks all passwords for one login and then tries the next login. This option loops around the passwords, so the first password is tried on all logins, then the next password.</p>
<dt><code>-f</code></p>
<dd> exit after the first found login/password pair (per host if -M)</p>
<dt><code>-F</code></p>
<dd> exit after the first found login/password pair for any host (for usage with -M)</p>
<dt><code>-M FILE</code></p>
<dd> server list for parallel attacks, one entry per line</p>
<dt><code>-o FILE</code></p>
<dd> write found login/password pairs to FILE instead of stdout</p>
<dt><code>-t TASKS</code></p>
<dd> run TASKS number of connects in parallel (default: 16)</p>
<dt><code>-w TIME</code></p>
<dd> defines the max wait time in seconds for responses (default: 32)</p>
<dt><code>-W TIME</code></p>
<dd> defines a wait time between each connection a task performs. This usually only makes sense if a low task number is used, .e.g -t 1</p>
<dt><code>-4 / -6 </code></p>
<dd> prefer IPv4 (default) or IPv6 addresses</p>
<dt><code>-v / -V </code></p>
<dd> verbose mode / show login+pass combination for each attempt <code>-d</code> debug mode</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xhydra/">xhydra</a></code>(1), <code><a href="/docs/linux/man/1-pw-inspector/">pw-inspector</a></code>(1).<br />
 The programs are documented fully by van Hauser &lt;vh [at] thc.org&gt;</p>
<h2>AUTHOR</h2>
<p> hydra was written by van Hauser / THC &lt;vh [at] thc.org&gt; </p>
<p> This manual page was written by Daniel Echeverry &lt;epsilon77 [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>
