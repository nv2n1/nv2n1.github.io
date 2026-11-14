---
title: "ntlm_auth(1)"
name: "ntlm_auth"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ntlm_auth/"
description: "ntlm_auth – tool to allow external access to Winbind’s NTLM authentication function"
---

<h2 class="name">NAME</h2>
<p> ntlm_auth &#8211; tool to allow external access to Winbind&#8217;s NTLM authentication function </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>ntlm_auth</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> ntlm_auth is a helper utility that authenticates users using NT/LM authentication. It returns 0 if the users is authenticated successfully and 1 if access was denied. ntlm_auth uses winbind to access the user and authentication data for a domain. This utility is only intended to be used by other programs (currently Squid and mod_ntlm_winbind)</p>
<h2>OPERATIONAL REQUIREMENTS</h2>
<p> The <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) daemon must be operational for many of these commands to function. </p>
<p> Some of these commands also require access to the directory winbindd_privileged in $LOCKDIR. This should be done either by running this command as root or providing group access to the winbindd_privileged directory. For security reasons, this directory should not be world-accessable.</p>
<h2>OPTIONS</h2>
<p> &#8211;helper-protocol=PROTO</p>
<dl>
<dt>
<dd> Operate as a stdio-based helper. Valid helper protocols are: </p>
<p> squid-2.4-basic</p>
<dl>
<dt>
<dd> Server-side helper for use with Squid 2.4&#8217;s basic (plaintext) authentication.</dl>
<p> squid-2.5-basic</p>
<dl>
<dt>
<dd> Server-side helper for use with Squid 2.5&#8217;s basic (plaintext) authentication.</dl>
<p> squid-2.5-ntlmssp</p>
<dl>
<dt>
<dd> Server-side helper for use with Squid 2.5&#8217;s NTLMSSP authentication. </p>
<p> Requires access to the directory winbindd_privileged in $LOCKDIR. The protocol used is described here: <a rel="nofollow" href="http://devel.squid-cache.org/ntlm/squid_helper_protocol.html.">http://devel.squid-cache.org/ntlm/squid_helper_protocol.html.</a> This protocol has been extended to allow the NTLMSSP Negotiate packet to be included as an argument to the YR command. (Thus avoiding loss of information in the protocol exchange).</dl>
<p> ntlmssp-client-1</p>
<dl>
<dt>
<dd> Client-side helper for use with arbitrary external programs that may wish to use Samba&#8217;s NTLMSSP authentication knowledge. </p>
<p> This helper is a client, and as such may be run by any user. The protocol used is effectively the reverse of the previous protocol. A YR command (without any arguments) starts the authentication exchange.</dl>
<p> gss-spnego</p>
<dl>
<dt>
<dd> Server-side helper that implements GSS-SPNEGO. This uses a protocol that is almost the same as squid-2.5-ntlmssp, but has some subtle differences that are undocumented outside the source at this stage. </p>
<p> Requires access to the directory winbindd_privileged in $LOCKDIR.</dl>
<p> gss-spnego-client</p>
<dl>
<dt>
<dd> Client-side helper that implements GSS-SPNEGO. This also uses a protocol similar to the above helpers, but is currently undocumented.</dl>
<p> ntlm-server-1</p>
<dl>
<dt>
<dd> Server-side helper protocol, intended for use by a RADIUS server or the &#8216;winbind&#8217; plugin for pppd, for the provision of MSCHAP and MSCHAPv2 authentication. </p>
<p> This protocol consists of lines in the form: Parameter: value and Parameter:: Base64-encode value. The presence of a single period . indicates that one side has finished supplying data to the other. (Which in turn could cause the helper to authenticate the user). </p>
<p> Currently implemented parameters from the external program to the helper are: </p>
<p> Username</p>
<dl>
<dt>
<dd> The username, expected to be in Samba&#8217;s m[blue]<code>unix charset</code>m[]. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> Username: bob </p>
<p> Username:: Ym9i</dl>
</dl>
<p> NT-Domain</p>
<dl>
<dt>
<dd> The user&#8217;s domain, expected to be in Samba&#8217;s m[blue]<code>unix charset</code>m[]. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> NT-Domain: WORKGROUP </p>
<p> NT-Domain:: V09SS0dST1VQ</dl>
</dl>
<p> Full-Username</p>
<dl>
<dt>
<dd> The fully qualified username, expected to be in Samba&#8217;s m[blue]<code>unix charset</code>m[] and qualified with the m[blue]<code>winbind separator</code>m[]. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> Full-Username: WORKGROUPob </p>
<p> Full-Username:: V09SS0dST1VQYm9i</dl>
</dl>
<p> LANMAN-Challenge</p>
<dl>
<dt>
<dd> The 8 byte LANMAN Challenge value, generated randomly by the server, or (in cases such as MSCHAPv2) generated in some way by both the server and the client. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> LANMAN-Challenge: 0102030405060708</dl>
</dl>
<p> LANMAN-Response</p>
<dl>
<dt>
<dd> The 24 byte LANMAN Response value, calculated from the user&#8217;s password and the supplied LANMAN Challenge. Typically, this is provided over the network by a client wishing to authenticate. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> LANMAN-Response: 0102030405060708090A0B0C0D0E0F101112131415161718</dl>
</dl>
<p> NT-Response</p>
<dl>
<dt>
<dd> The &gt;= 24 byte NT Response calculated from the user&#8217;s password and the supplied LANMAN Challenge. Typically, this is provided over the network by a client wishing to authenticate. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> NT-Response: 0102030405060708090A0B0C0D0E0F10111213141516171</dl>
</dl>
<p> Password</p>
<dl>
<dt>
<dd> The user&#8217;s password. This would be provided by a network client, if the helper is being used in a legacy situation that exposes plaintext passwords in this way. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> Password: samba2 </p>
<p> Password:: c2FtYmEy</dl>
</dl>
<p> Request-User-Session-Key</p>
<dl>
<dt>
<dd> Upon successful authenticaiton, return the user session key associated with the login. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> Request-User-Session-Key: Yes</dl>
</dl>
<p> Request-LanMan-Session-Key</p>
<dl>
<dt>
<dd> Upon successful authenticaiton, return the LANMAN session key associated with the login. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> Request-LanMan-Session-Key: Yes</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 Implementers should take care to base64 encode any data (such as usernames/passwords) that may contain malicous user data, such as a newline. They may also need to decode strings from the helper, which likewise may have been base64 encoded. </p>
</dl>
</dl>
<p> &#8211;username=USERNAME</p>
<dl>
<dt>
<dd> Specify username of user to authenticate</dl>
<p> &#8211;domain=DOMAIN</p>
<dl>
<dt>
<dd> Specify domain of user to authenticate</dl>
<p> &#8211;workstation=WORKSTATION</p>
<dl>
<dt>
<dd> Specify the workstation the user authenticated from</dl>
<p> &#8211;challenge=STRING</p>
<dl>
<dt>
<dd> NTLM challenge (in HEXADECIMAL)</dl>
<p> &#8211;lm-response=RESPONSE</p>
<dl>
<dt>
<dd> LM Response to the challenge (in HEXADECIMAL)</dl>
<p> &#8211;nt-response=RESPONSE</p>
<dl>
<dt>
<dd> NT or NTLMv2 Response to the challenge (in HEXADECIMAL)</dl>
<p> &#8211;password=PASSWORD</p>
<dl>
<dt>
<dd> User&#8217;s plaintext password </p>
<p> If not specified on the command line, this is prompted for when required. </p>
<p> For the NTLMSSP based server roles, this parameter specifies the expected password, allowing testing without winbindd operational.</dl>
<p> &#8211;request-lm-key</p>
<dl>
<dt>
<dd> Retrieve LM session key</dl>
<p> &#8211;request-nt-key</p>
<dl>
<dt>
<dd> Request NT key</dl>
<p> &#8211;diagnostics</p>
<dl>
<dt>
<dd> Perform Diagnostics on the authentication chain. Uses the password from &#8211;password or prompts for one.</dl>
<p> &#8211;require-membership-of={SID|Name}</p>
<dl>
<dt>
<dd> Require that a user be a member of specified group (either name or SID) for authentication to succeed.</dl>
<p> &#8211;pam-winbind-conf=FILENAME</p>
<dl>
<dt>
<dd> Define the path to the pam_winbind.conf file.</dl>
<p> &#8211;target-hostname=HOSTNAME</p>
<dl>
<dt>
<dd> Define the target hostname.</dl>
<p> &#8211;target-service=SERVICE</p>
<dl>
<dt>
<dd> Define the target service.</dl>
<p> &#8211;use-cached-creds</p>
<dl>
<dt>
<dd> Whether to use credentials cached by winbindd.</dl>
<p> &#8211;allow-mschapv2</p>
<dl>
<dt>
<dd> Explicitly allow MSCHAPv2.</dl>
<p> &#8211;offline-logon</p>
<dl>
<dt>
<dd> Allow offline logons for plain text auth.</dl>
<p> &#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dt>
<dd> The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -V|&#8211;version</p>
<dl>
<dt>
<dd> Prints the program version number.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
<h2>EXAMPLE SETUP</h2>
<p> To setup ntlm_auth for use by squid 2.5, with both basic and NTLMSSP authentication, the following should be placed in the squid.conf file. </p>
<dl>
<dt>
<dd>
<pre>
auth_param ntlm program ntlm_auth --helper-protocol=squid-2.5-ntlmssp
auth_param basic program ntlm_auth --helper-protocol=squid-2.5-basic
auth_param basic children 5
auth_param basic realm Squid proxy-caching web server
auth_param basic credentialsttl 2 hours
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> This example assumes that ntlm_auth has been installed into your path, and that the group permissions on winbindd_privileged are as described above. </p>
</dl>
<p> To setup ntlm_auth for use by squid 2.5 with group limitation in addition to the above example, the following should be added to the squid.conf file. </p>
<dl>
<dt>
<dd>
<pre><code>
auth_param ntlm program ntlm_auth-- helper - protocol = squid - 2.5 - ntlmssp-- require - membership - of = 'WORKGROUP\Domain Users' auth_param basic program ntlm_auth-- helper - protocol = squid - 2.5 - basic-- require - membership - of = 'WORKGROUP\Domain Users'
</code></pre>
</dl>
<h2>TROUBLESHOOTING</h2>
<p> If you&#8217;re experiencing problems with authenticating Internet Explorer running under MS Windows 9X or Millennium Edition against ntlm_auth&#8217;s NTLMSSP authentication helper (&#8211;helper-protocol=squid-2.5-ntlmssp), then please read the Microsoft Knowledge Base article #239869 and follow instructions described there.</p>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The ntlm_auth manpage was written by Jelmer Vernooij and Andrew Bartlett. </p>
<h2>Index</h2>
