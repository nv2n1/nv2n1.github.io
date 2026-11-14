---
title: "pki(1)"
name: "pki"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki/"
description: "pki – Command-Line Interface for accessing Certificate System services."
---

<h2 class="name">NAME</h2>
<p> pki &#8211; Command-Line Interface for accessing Certificate System services.</p>
<h2>SYNOPSIS</h2>
<p> <code>pki</code> [CLI options] &lt;command&gt; [command arguments] </p>
<h2>DESCRIPTION</h2>
<p> The <code>pki</code> command provides a command-line interface allowing clients to access various services on the Certificate System server. These services include certificates, groups, keys, security domains, and users.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h2>CLI OPTIONS</h2>
<dl>
<dt><code>-c &lt;client security database password&gt;</code></p>
<dd> Specifies the client security database password (mutually exclusive to the &#8216;-C&#8217; option).</p>
<dt><code>-C &lt;client-side password file&gt;</code></p>
<dd> Specifies the file which contains the client security database password (mutually exclusive to the &#8216;-c&#8217; option).</p>
<dt><code>-d &lt;client security database location&gt;</code></p>
<dd> Specifies the client security database location (default: <i>~/.dogtag/nssdb</i>).</p>
<dt><code>-h &lt;hostname&gt;</code></p>
<dd> Specifies the hostname (default: hostname of the local machine).</p>
<dt><code>&#8211;help</code></p>
<dd> Prints additional help information.</p>
<dt><code>&#8211;ignore-cert-status &lt;list&gt;</code></p>
<dd> Comma-separated list of ignored certificate validity statuses.</p>
<dt><code>&#8211;message-format &lt;format&gt;</code></p>
<dd> Message format: xml (default), json.</p>
<dt><code>-n &lt;client certificate nickname&gt;</code></p>
<dd> Specifies the nickname for client certificate authentication (mutually exclusive to the &#8216;-u&#8217; option). This authentication requires a security database password.</p>
<dt><code>&#8211;output &lt;folder&gt;</code></p>
<dd> Folder to store HTTP messages.</p>
<dt><code>-P &lt;protocol&gt;</code></p>
<dd> Specifies the protocol (default: http).</p>
<dt><code>-p &lt;port&gt;</code></p>
<dd> Specifies the port (default: 8080).</p>
<dt><code>&#8211;reject-cert-status &lt;list&gt;</code></p>
<dd> Comma-separated list of rejected certificate validity statuses. PKI subsystem type &#8211; [CA, KRA, OCSP, TKS, or TPS] (non-case-sensitive).</p>
<dt><code>-U &lt;URI&gt;</code></p>
<dd> Specifies the server URI.</p>
<dt><code>-u &lt;username&gt;</code></p>
<dd> Specifies the username for basic authentication (mutually exclusive to the &#8216;-n&#8217; option). This authentication requires a user password.</p>
<dt><code>-v</code></p>
<dd> Displays verbose information.</p>
<dt><code>&#8211;version</code></p>
<dd> Displays CLI version information.</p>
<dt><code>-w &lt;password&gt;</code></p>
<dd> Specifies the user password (mutually exclusive to the &#8216;-W&#8217; option).</p>
<dt><code>-W &lt;client-side password file&gt;</code></p>
<dd> Specifies the file which contains the user password (mutually exclusive to the &#8216;-w&#8217; option). </p>
</dl>
<h2>OPERATIONS</h2>
<p> To view available commands and options, simply type <code>pki</code>. Some commands have sub-commands. To view the sub-commands, type <code>pki &lt;command&gt;</code>. To view each command&#8217;s usage, type <code> pki &lt;command&gt; &#8211;help</code>. </p>
<p> A client security database is needed to execute commands that require SSL connection or client certificate for authentication. See <code><a href="/docs/linux/man/1-pki-client/">pki-client</a></code>(1) for more information. </p>
<h3>Connection</h3>
<p> By default, the CLI connects to a server running on the local machine via the non-secure HTTP port 8080. To specify a different server location, use the appropriate arguments to give a different host (<code>-h</code>), port (<code>-p</code>), or connection protocol (<code>-P</code>). </p>
<p> <code>pki -P &lt;protocol&gt; -h &lt;hostname&gt; -p &lt;port&gt; &lt;command&gt;</code> </p>
<p> Alternatively, the connection parameters can be specified as a URI: </p>
<p> <code>pki -U &lt;URI&gt; &lt;command&gt;</code> </p>
<p> where the URI is of the format <i>&lt;protocol&gt;://&lt;hostname&gt;:&lt;port&gt;</i>. </p>
<h3>Authentication</h3>
<p> Some commands require authentication. These are commands that are restricted to particular sets of users (such as agents or admins) or those operations involving certificate profiles that require authentication. </p>
<p> To execute a command without authentication: </p>
<p> <code>pki &lt;command&gt;</code> </p>
<p> To execute a command using basic authentication (i. e. &#8211; username/password), see the <code>Basic Authentication</code> section of this man page. </p>
<p> To execute a command using client authentication (i. e. &#8211; client certificate), see the <code>Client Authentication</code> section of this man page. </p>
<h3>Basic Authentication</h3>
<p> To authenticate with a username and password: </p>
<p> <code>pki -u &lt;username&gt; -w &lt;password&gt; &lt;command&gt;</code> </p>
<p> Rather than being exposed in plaintext on the command-line, user passwords may be stored in a file instead. See <code>Client-side Password Files</code> for detailed information. </p>
<p> To authenticate with a username by obtaining the user password from a client-side password file: </p>
<p> <code>pki -u &lt;username&gt; -W &lt;client-side password file&gt; &lt;command&gt;</code> </p>
<p> Finally, if a username has been specified on the command-line, and neither the &#8216;-W &lt;client-side password file&gt;&#8217; nor the &#8216;-w &lt;password&gt;&#8217; options have been utilized, the password will be prompted for. </p>
<p> To authenticate with a username by interactively prompting for a password: </p>
<p> <code>pki -u &lt;username&gt; &lt;command&gt;</code> </p>
<p> <code>Note:</code> Prompting for a user password is not suitable for automated batch processing. </p>
<h3>Client Authentication Setup</h3>
<p> A client certificate associated with the desired PKI server must be used for client authentication. This can be done by importing the client certificate into an NSS security database and passing the values to the relevant options provided by the <code>pki</code> CLI framework. </p>
<p> To achieve this, execute the following commands to set up an NSS security database for use by the <code>pki</code> client, import the client certificate into the NSS database, and list information (including the nickname of the client certificate) stored in the NSS database: </p>
<p> <code>&#8211; certutil -N -d &lt;CERT_DB_DIR_PATH&gt;</code> </p>
<p> <code>&#8211; pk12util -i &lt;Agent_Cert_P12_FILE_PATH&gt; -d &lt;CERT_DB_DIR_PATH&gt;</code> </p>
<p> <code>&#8211; certutil -L -d &lt;CERT_DB_DIR_PATH&gt;</code> </p>
<p> The first command creates a client security database, and asks the client user to enter a password for this NSS database. </p>
<p> The second command imports a client certificate stored in a PKCS12 format into this NSS database; it prompts for the passwords of the PKCS12 file and the client security database. The simplist example of such a client certificate is to obtain the administrator certificate created during the configuration portion of the basic PKI installation of the associated PKI server (e. g. &#8211; located at <i>/root/.dogtag/pki-tomcat/ca_admin_cert.p12</i> on the PKI server machine). </p>
<p> The third command shows the information about the imported client certificate (including its nickname). </p>
<p> <code>Note:</code> When issuing the first <code>pki</code> command using the authentication parameters (after completion of the setup of the client security database), a user may be greeted with a warning message which indicates that an untrusted issuer was encountered. Simply reply &#8216;Y&#8217; to import the CA certificate, and, presuming that the displayed CA server URL is valid, press the carriage return. </p>
<h3>Client Authentication</h3>
<p> To authenticate with a client certificate: </p>
<p> <code>pki -d &lt;client security database location&gt; -c &lt;client security database password&gt; -n &lt;client certificate nickname&gt; &lt;command&gt;</code><br />
&nbsp;<wbr> Alternatively, to prevent exposure via the command-line, a client security database may store their password in a file instead. See <code>Client-side Password Files</code> for detailed information. </p>
<p> To authenticate with a client certificate by obtaining the client security database password from a client-side password file: </p>
<p> <code>pki -d &lt;client security database location&gt; -C &lt;client-side password file&gt; -n &lt;client certificate nickname&gt; &lt;command&gt;</code> </p>
<p> Finally, if a client certificate has been specified on the command-line, and neither the &#8216;-C &lt;client-side password file&gt;&#8217; nor the &#8216;-c &lt;client security database password&gt;&#8217; options have been utilized, the client security database password will be prompted for. </p>
<p> To authenticate with a client certificate by interactively prompting for a client security database password: </p>
<p> <code>pki -d &lt;client security database location&gt; -n &lt;client certificate nickname&gt; &lt;command&gt;</code> </p>
<p> <code>Note:</code> Prompting for a client security database password is not suitable for automated batch processing. </p>
<h3>Client-side Password Files</h3>
<p> Both the &#8216;-C&#8217; (client authentication) and the &#8216;-W&#8217; (basic authentication) options require the use of a client-side password file. </p>
<p> For security purposes, client-side password files should be, at a minimum, operating system protected non-world readable files. </p>
<p> Client-side password files generally store a password in an equals-sign-delimited plaintext format &#8216;token=password&#8217; (e. g. &#8211; &#8216;internal=foobar&#8217; where &#8216;internal&#8217; is the token, &#8216;=&#8217; is the delimiter, and &#8216;foobar&#8217; is the actual password). The token keyword &#8216;internal&#8217; is the default specification for a token, and refers to the &quot;Internal Key Storage Token&quot;. If a client-side password file is being used for the sole purposes of the <code>pki</code> command-line tool, a client-side password file also supports the format that merely consists of the plaintext password on a single line (read the <code>Caveats</code> which follow). </p>
<p> <code>Caveats:</code></p>
<dl>
<dt>
<dd> &bull; Since client-side password files are allowed to use the &#8216;token=password&#8217; format, the first &#8216;=&#8217; character can only be used as a delimiter (i. e. &#8211; it cannot be used as a valid character within the &#8216;token&#8217; name) as escaping the &#8216;=&#8217; character within a token is not supported. </p>
<p> &bull; When specifying a password which contains an &#8216;=&#8217; character, always specify an initial &#8216;=&#8217; prior to specifying the actual password (mandatory when no token has been specified) as escaping the &#8216;=&#8217; character within a password is not supported. </p>
<p> &bull; Tokens do not support leading or trailing whitespace since these characters are stripped prior to their use; however, all whitespace inside tokens will be preserved. </p>
<p> &bull; Passwords preserve all leading, trailing, and internal whitespace since passwords are not trimmed prior to their use. </p>
<p> &bull; TBD: Supply code to handle the case of a non-internal token (e. g. &#8211; &#8216;hardware-nethsm&#8217; utilized in the following examples) since the current code ignores the specified token (i. e. &#8211; it always utilizes the default &#8216;internal&#8217; token no matter what is currently specified). </p>
<p> &bull; TBD: Allow numerous &#8216;token=password&#8217; lines in a single client-side password file to support the ability to authenticate against specified tokens as well as multiple tokens. </p>
</dl>
<p> <code>Valid examples include:</code> </p>
<p> <code>internal=foobar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;internal&quot;, password=&quot;foobar&quot; </p>
<p> <code>hardware-nethsm=foobar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;hardware-nethsm&quot;&nbsp;<wbr>(ignored &#8211; TBD), password=&quot;foobar&quot; </p>
<p> <code>internal=ack=bar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;internal&quot;, password=&quot;ack=bar&quot; </p>
<p> <code>hardware-nethsm=ack=bar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;hardware-nethsm&quot;&nbsp;<wbr>(ignored &#8211; TBD), password=&quot;ack=bar&quot; </p>
<p> <code>=foobar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;internal&quot;&nbsp;<wbr>(default), password=&quot;foobar&quot; </p>
<p> <code>=foo=bar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;internal&quot;&nbsp;<wbr>(default), password=&quot;foo=bar&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Since the password contains an&nbsp;<wbr>&#8216;=&#8217;&nbsp;<wbr>character,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>an initial&nbsp;<wbr>&#8216;=&#8217;&nbsp;<wbr>character must be specified!) </p>
<p> <code>foobar</code><br />
where:&nbsp;<wbr>&nbsp;<wbr>token=&quot;internal&quot;&nbsp;<wbr>(default), password=&quot;foobar&quot; </p>
<h3>Results Paging</h3>
<p> Some commands (e.g. cert-find) may return multiple results. Since the number of results may be large, the results are split into multiple pages. By default the command will return only the first page (e.g. the first 20 results). To retrieve results from another page, additional paging parameters can be specified: </p>
<pre>
* start: index of the first result to return (default: 0)
* size: number of results to return (default: 20)
</pre>
<p> For example, to retrieve the first page (index #0-#19): </p>
<p> <code>pki cert-find &#8211;start 0 &#8211;size 20</code> </p>
<p> To retrieve the second page (index #20-#39): </p>
<p> <code>pki cert-find &#8211;start 20 &#8211;size 20</code> </p>
<p> To retrieve the third page (index #40-#59): </p>
<p> <code>pki cert-find &#8211;start 40 &#8211;size 20</code> </p>
<h2>FILES</h2>
<p> <i>/usr/bin/pki</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki-cert/">pki-cert</a></code>(1)</p>
<dl>
<dt>
<dd> Certificate management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-client/">pki-client</a></code>(1)</p>
<dl>
<dt>
<dd> Client security database management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-group/">pki-group</a></code>(1)</p>
<dl>
<dt>
<dd> Group management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-group-member/">pki-group-member</a></code>(1)</p>
<dl>
<dt>
<dd> Group member management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-key/">pki-key</a></code>(1)</p>
<dl>
<dt>
<dd> Key management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-securitydomain/">pki-securitydomain</a></code>(1)</p>
<dl>
<dt>
<dd> Security domain management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-user/">pki-user</a></code>(1)</p>
<dl>
<dt>
<dd> User management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-user-cert/">pki-user-cert</a></code>(1)</p>
<dl>
<dt>
<dd> User certificate management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-user-membership/">pki-user-membership</a></code>(1)</p>
<dl>
<dt>
<dd> User membership management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-ca-profile/">pki-ca-profile</a></code>(1)</p>
<dl>
<dt>
<dd> Profile management commands</dl>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, and Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
