---
title: "saslauthd(8)"
name: "saslauthd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-saslauthd/"
description: "saslauthd – sasl authentication server"
---

<p><code>saslauthd</code> &#8211; sasl authentication server</p>
<h2>Synopsis</h2>
<p>&#8211;<code>a</code> <i>authmech</i> [-<code>Tvdchlr</code> ] [-<code>O </code><i>option</i> ] [-<code>m </code><i>mux_path</i> ] [-<code>n </code><i>threads</i> ] [-<code>s </code><i>size</i> ] [-<code>t </code><i>timeout</i> ]</p>
<h2>Description</h2>
<p>is a daemon process that handles plaintext authentication requests on behalf of the SASL library. </p>
<p> The server fulfills two roles: it isolates all code requiring superuser privileges into a single process, and it can be used to provide <i>proxy</i> authentication services to clients that do not understand SASL based authentication. </p>
<p> should be started from the system boot scripts when going to multi-user mode. When running against a protected authentication database (e.g. the <code>shadow</code> mechanism), it must be run as the superuser. Otherwise it is recommended to run daemon unprivileged as saslauth:saslauth. You can do so by following these steps: </p>
<ol>
<li> create directory /etc/systemd/system/saslauthd.service.d/
<li> create file /etc/systemd/system/saslauthd.service.d/user.conf with content
<pre>[Service]
User=saslauth
Group=saslauth</pre>
<li> Reload systemd service file: run &#8220;systemctl daemon-reload&#8221; </ol>
<h3>Options</h3>
<p>Options named by lower-case letters configure the server itself. Upper-case options control the behavior of specific authentication mechanisms; their applicability to a particular authentication mechanism is described in the Sx AUTHENTICATION MECHANISMS section.</p>
<dl>
<dt><code>-a </code><i>authmech</i></p>
<dd>Use <i>authmech</i> as the authentication mechanism. (See the Sx AUTHENTICATION MECHANISMS section below.) This parameter is mandatory.</p>
<dt><code>-O </code><i>option</i></p>
<dd>A mechanism specific option (e.g. rimap hostname or config file path)</p>
<dt><code>-H </code><i>hostname</i></p>
<dd>The remote host to be contacted by the <code>rimap</code> authentication mechanism. (Deprecated, use -O instead)</p>
<dt><code>-m </code><i>path</i></p>
<dd>Use <i>path</i> as the pathname to the named socket to listen on for connection requests. This must be an absolute pathname, and MUST NOT include the trailing &quot;/mux&quot;. Note that the default for this value is &quot;/var/state/saslauthd&quot; (or what was specified at compile time) and that this directory must exist for saslauthd to function.</p>
<dt><code>-n </code><i>threads</i></p>
<dd>Use <i>threads</i> processes for responding to authentication queries. (default: 5) A value of zero will indicate that saslauthd should fork an individual process for each connection. This can solve leaks that occur in some deployments.</p>
<dt><code>-s </code><i>size</i></p>
<dd>Use <i>size</i> as the table size of the hash table (in kilobytes)</p>
<dt><code>-t </code><i>timeout</i></p>
<dd>Use <i>timeout</i> as the expiration time of the authentication cache (in seconds)</p>
<dt><code>-T</code></p>
<dd>Honour time-of-day login restrictions.</p>
<dt><code>-h</code></p>
<dd>Show usage information</p>
<dt><code>-c</code></p>
<dd>Enable caching of authentication credentials</p>
<dt><code>-l</code></p>
<dd>Disable the use of a lock file for controlling access to accept().</p>
<dt><code>-r</code></p>
<dd>Combine the realm with the login (with an &#8216;@&#8217; sign in between). e.g. login: &quot;foo&quot; realm: &quot;bar&quot; will get passed as login: &quot;foo@bar&quot;. Note that the realm will still be passed, which may lead to unexpected behavior for authentication mechanisms that make use of the realm, however for mechanisms which don&#8217;t, such as <i>getpwent</i> this is the only way to authenticate domain-specific users sharing the same userid.</p>
<dt><code>-v</code></p>
<dd>Print the version number and available authentication mechanisms on standard error, then exit.</p>
<dt><code>-d</code></p>
<dd>Debugging mode.</dl>
<h3>Logging</h3>
<p>logs its activities via <code>syslogd</code> using the <code>LOG_AUTH</code> facility.</p>
<h2>Authentication Mechanisms</h2>
<p>supports one or more Qq authentication mechanisms , dependent upon the facilities provided by the underlying operating system. The mechanism is selected by the &#8211;<code>a</code> flag from the following list of choices:</p>
<dl>
<dt><code>dce</code></p>
<dd><i>(AIX)</i> </p>
<p> Authenticate using the DCE authentication environment.</p>
<dt><code>getpwent</code></p>
<dd><i>(All platforms)</i> </p>
<p> Authenticate using the Fn getpwent library function. Typically this authenticates against the local password file. See your system&#8217;s <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3) man page for details.</p>
<dt><code>kerberos4</code></p>
<dd><i>(All platforms)</i> </p>
<p> Authenticate against the local Kerberos 4 realm. (See the Sx NOTES section for caveats about this driver.)</p>
<dt><code>kerberos5</code></p>
<dd><i>(All platforms)</i> </p>
<p> Authenticate against the local Kerberos 5 realm.</p>
<dt><code>pam</code></p>
<dd><i>(Linux, Solaris)</i> </p>
<p> Authenticate using Pluggable Authentication Modules (PAM).</p>
<dt><code>rimap</code></p>
<dd><i>(All platforms)</i> </p>
<p> Forward authentication requests to a remote IMAP server. This driver connects to a remote IMAP server, specified using the -O flag, and attempts to login (via an IMAP `LOGIN&#8217; command) using the credentials supplied to the local server. If the remote authentication succeeds the local connection is also considered to be authenticated. The remote connection is closed as soon as the tagged response from the `LOGIN&#8217; command is received from the remote server. </p>
<p> The <i>option</i> parameter to the &#8211;<code>O</code> flag describes the remote server to forward authentication requests to. <i>hostname</i> can be a hostname (imap.example.com) or a dotted-quad IP address (192.168.0.1). The latter is useful if the remote server is multi-homed and has network interfaces that are unreachable from the local IMAP server. The remote host is contacted on the `imap&#8217; service port. A non-default port can be specified by appending a slash and the port name or number to the <i>hostname</i> argument. </p>
<p> The &#8211;<code>O</code> flag and argument are mandatory when using the <code>rimap</code> mechanism.</p>
<dt><code>shadow</code></p>
<dd><i>(AIX, Irix, Linux, Solaris)</i> </p>
<p> Authenticate against the local Qq shadow password file . The exact mechanism is system dependent. currently understands the Fn getspnam and Fn getuserpw library routines. Some systems honour the &#8211;<code>T</code> flag.</p>
<dt><code>sasldb</code></p>
<dd><i>(All platforms)</i> </p>
<p> Authenticate against the SASL authentication database. Note that this is probably not what you want to use, and is even disabled at compile-time by default. If you want to use sasldb with the SASL library, you probably want to use the pwcheck_method of &quot;auxprop&quot; along with the sasldb auxprop plugin instead.</p>
<dt><code>ldap</code></p>
<dd><i>(All platforms that support OpenLDAP 2.0 or higher)</i> </p>
<p> Authenticate against an ldap server. The ldap configuration parameters are read from /etc/saslauthd.conf. The location of this file can be changed with the -O parameter. See the LDAP_SASLAUTHD file included with the distribution for the list of available parameters.</p>
<dt><code>sia</code></p>
<dd><i>(Digital UNIX)</i> </p>
<p> Authenticate using the Digital UNIX Security Integration Architecture (a.k.a. Qq enhanced security ) .</dl>
<h2>Notes</h2>
<p>The <code>kerberos4</code> authentication driver consumes considerable resources. To perform an authentication it must obtain a ticket granting ticket from the TGT server <code>on every authentication request.</code> The Kerberos library routines that obtain the TGT also create a local ticket file, on the reasonable assumption that you will want to save the TGT for use by other Kerberos applications. These ticket files are unusable by <code>,</code> however there is no way not to create them. The overhead of creating and removing these ticket files can cause serious performance degradation on busy servers. (Kerberos was never intended to be used in this manner, anyway.)</p>
<h2>Files</h2>
<dl>
<dt><code>/run/saslauthd/mux </code></p>
<dd>The default communications socket.</p>
<dt><code>/etc/saslauthd.conf </code></p>
<dd>The default configuration file for ldap support.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-passwd/">passwd</a>(1), <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3), <a href="/docs/linux/man/3-getspnam/">getspnam</a>(3), <a href="/docs/linux/man/3-getuserpw/">getuserpw</a>(3), sasl_checkpass3 sia_authenticate_user3, </p>
