---
title: "ldapexop(1)"
name: "ldapexop"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapexop/"
description: "ldapexop – issue LDAP extended operations"
---

<h2 class="name">NAME</h2>
<p> ldapexop &#8211; issue LDAP extended operations</p>
<h2>SYNOPSIS</h2>
<p> ldapexop [<code>-V</code>[<code>V</code>]] [<code>-d</code><i>&nbsp;<wbr>debuglevel</i>] [<code>-n</code>] [<code>-v</code>] [<code>-f</code><i>&nbsp;<wbr>file</i>] [<code>-x</code>] [<code>-D</code><i>&nbsp;<wbr>binddn</i>] [<code>-W</code>] [<code>-w</code><i>&nbsp;<wbr>passwd</i>] [<code>-y</code><i>&nbsp;<wbr>passwdfile</i>] [<code>-H</code><i>&nbsp;<wbr>URI</i>] [<code>-h</code><i>&nbsp;<wbr>ldaphost</i>] [<code>-p</code><i>&nbsp;<wbr>ldapport</i>] [<code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]] [<code>-O</code><i>&nbsp;<wbr>security-properties</i>] [<code>-I</code>] [<code>-Q</code>] [<code>-N</code>] [<code>-U</code><i>&nbsp;<wbr>authcid</i>] [<code>-R</code><i>&nbsp;<wbr>realm</i>] [<code>-X</code><i>&nbsp;<wbr>authzid</i>] [<code>-Y</code><i>&nbsp;<wbr>mech</i>] [<code>-Z</code>[<code>Z</code>]] {<i>oid</i> | <code>oid:</code><i>data</i> | <code>oid::</code><i>b64data</i> | <code>whoami</code> | <code>cancel</code><i>&nbsp;<wbr>cancel-id</i> | <code>refresh</code><i>&nbsp;<wbr>DN</i><code>&nbsp;<wbr></code>[<i>ttl</i>]} </p>
<h2>DESCRIPTION</h2>
<p> ldapexop issues the LDAP extended operation specified by <code>oid</code> or one of the special keywords <code>whoami</code>, <code>cancel</code>, or <code>refresh</code>. </p>
<p> Additional data for the extended operation can be passed to the server using <i>data</i> or base-64 encoded as <i>b64data</i> in the case of <code>oid</code>, or using the additional parameters in the case of the specially named extended operations above. </p>
<p> Please note that ldapexop behaves differently for the same extended operation when it was given as an OID or as a specialliy named operation: </p>
<p> Calling ldapexop with the OID of the <code>whoami</code> (RFC 4532) extended operation </p>
<pre>
  ldapexop [&lt;options&gt;] 1.3.6.1.4.1.4203.1.11.3
</pre>
<p> yields </p>
<pre>
  # extended operation response
  data:: &lt;base64 encoded response data&gt;
</pre>
<p> while calling it with the keyword <code>whoami</code> </p>
<pre>
  ldapexop [&lt;options&gt;] whoami
</pre>
<p> results in </p>
<pre>
  dn:&lt;client's identity&gt;
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code><i>[</i><code>V</code><i>]</i></p>
<dd> Print version info. If<code>-VV</code> is given, only the version information is printed.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debuglevel</i></p>
<dd> Set the LDAP debugging level to <i>debuglevel</i>.</p>
<dt><code>-n</code></p>
<dd> Show what would be done but don&#8217;t actually do it. Useful for debugging in conjunction with <code>-v</code>.</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode, with many diagnostics written to standard output.</p>
<dt><code>-f</code><i>&nbsp;<wbr>file</i></p>
<dd> Read operations from <i>file</i>.</p>
<dt><code>-x</code></p>
<dd> Use simple authentication instead of SASL.</p>
<dt><code>-D</code><i>&nbsp;<wbr>binddn</i></p>
<dd> Use the Distinguished Name <i>binddn</i> to bind to the LDAP directory.</p>
<dt><code>-W</code></p>
<dd> Prompt for simple authentication. This is used instead of specifying the password on the command line.</p>
<dt><code>-w</code><i>&nbsp;<wbr>passwd</i></p>
<dd> Use <i>passwd</i> as the password for simple authentication.</p>
<dt><code>-y</code><i>&nbsp;<wbr>passwdfile</i></p>
<dd> Use complete contents of <i>passwdfile</i> as the password for simple authentication.</p>
<dt><code>-H</code><i>&nbsp;<wbr>URI</i></p>
<dd> Specify URI(s) referring to the ldap server(s); only the protocol/host/port fields are allowed; a list of URI, separated by whitespace or commas is expected.</p>
<dt><code>-h</code><i>&nbsp;<wbr>ldaphost</i></p>
<dd> Specify the host on which the ldap server is running. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-p</code><i>&nbsp;<wbr>ldapport</i></p>
<dd> Specify the TCP port where the ldap server is listening. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd> Specify general extensions. &#8216;!&#8217; indicates criticality. </p>
<pre><code>
[!] assert = &lt;filter&gt;(an RFC 4515 Filter) !authzid = &lt;authzid&gt;("dn:&lt;dn&gt;" or "u:&lt;user&gt;")
    [!] bauthzid(RFC 3829 authzid control)
        [!] chaining[=&lt;resolve&gt;[/&lt;cont&gt;]]
                    [!] manageDSAit
                        [!] noop
                            ppolicy
                                [!] postread[=&lt;attrs&gt;](a comma - separated attribute list)
                                    [!] preread[=&lt;attrs&gt;](a comma - separated attribute list)
                                        [!] relax
                                            sessiontracking
                                                abandon,
    cancel, ignore(SIGINT sends abandon / cancel, or ignores response; if critical, doesn't wait for SIGINT. not really controls)
</code></pre>
<dt><code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]</p>
<dd>
<p> Specify general options. </p>
<p> General options: </p>
<pre>
  nettimeout=&lt;timeout&gt;  (in seconds, or &quot;none&quot; or &quot;max&quot;)
  ldif-wrap=&lt;width&gt;     (in columns, or &quot;no&quot; for no wrapping)
</pre>
<dt><code>-O</code><i>&nbsp;<wbr>security-properties</i></p>
<dd> Specify SASL security properties.</p>
<dt><code>-I</code></p>
<dd> Enable SASL Interactive mode. Always prompt. Default is to prompt only as needed.</p>
<dt><code>-Q</code></p>
<dd> Enable SASL Quiet mode. Never prompt.</p>
<dt><code>-N</code></p>
<dd> Do not use reverse DNS to canonicalize SASL host name.</p>
<dt><code>-U</code><i>&nbsp;<wbr>authcid</i></p>
<dd> Specify the authentication ID for SASL bind. The form of the ID depends on the actual SASL mechanism used.</p>
<dt><code>-R</code><i>&nbsp;<wbr>realm</i></p>
<dd> Specify the realm of authentication ID for SASL bind. The form of the realm depends on the actual SASL mechanism used.</p>
<dt><code>-X</code><i>&nbsp;<wbr>authzid</i></p>
<dd> Specify the requested authorization ID for SASL bind. <i>authzid</i> must be one of the following formats: <code>dn:</code><i>&lt;distinguished name&gt;</i> or <code>u:</code><i>&lt;username&gt;</i></p>
<dt><code>-Y</code><i>&nbsp;<wbr>mech</i></p>
<dd> Specify the SASL mechanism to be used for authentication. Without this option, the program will choose the best mechanism the server knows.</p>
<dt><code>-Z</code>[<code>Z</code>]</p>
<dd> Issue StartTLS (Transport Layer Security) extended operation. Giving it twice (<code>-ZZ</code>) will require the operation to be successful. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap_extended_operation_s/">ldap_extended_operation_s</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Peter Marschall based on <code>ldapexop</code>&#8216;s usage message and a few tests with <code>ldapexop</code>. Do not expect it to be complete or absolutely correct. </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
