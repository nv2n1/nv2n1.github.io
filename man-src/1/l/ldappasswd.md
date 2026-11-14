---
title: "ldappasswd(1)"
name: "ldappasswd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldappasswd/"
description: "ldappasswd – change the password of an LDAP entry"
---

<h2 class="name">NAME</h2>
<p> ldappasswd &#8211; change the password of an LDAP entry </p>
<h2>SYNOPSIS</h2>
<p> <code>ldappasswd</code> [<code>-V</code>[<code>V</code>]] [<code>-d</code><i>&nbsp;<wbr>debuglevel</i>] [<code>-n</code>] [<code>-v</code>] [<code>-A</code>] [<code>-a</code><i>&nbsp;<wbr>oldPasswd</i>] [<code>-t</code><i>&nbsp;<wbr>oldpasswdfile</i>] [<code>-S</code>] [<code>-s</code><i>&nbsp;<wbr>newPasswd</i>] [<code>-T</code><i>&nbsp;<wbr>newpasswdfile</i>] [<code>-x</code>] [<code>-D</code><i>&nbsp;<wbr>binddn</i>] [<code>-W</code>] [<code>-w</code><i>&nbsp;<wbr>passwd</i>] [<code>-y</code><i>&nbsp;<wbr>passwdfile</i>] [<code>-H</code><i>&nbsp;<wbr>ldapuri</i>] [<code>-h</code><i>&nbsp;<wbr>ldaphost</i>] [<code>-p</code><i>&nbsp;<wbr>ldapport</i>] [<code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]] [<code>-O</code><i>&nbsp;<wbr>security-properties</i>] [<code>-I</code>] [<code>-Q</code>] [<code>-N</code>] [<code>-U</code><i>&nbsp;<wbr>authcid</i>] [<code>-R</code><i>&nbsp;<wbr>realm</i>] [<code>-X</code><i>&nbsp;<wbr>authzid</i>] [<code>-Y</code><i>&nbsp;<wbr>mech</i>] [<code>-Z</code>[<code>Z</code>]] [<i>user</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ldappasswd</code> is a tool to set the password of an LDAP user. <code>ldappasswd</code> uses the LDAPv3 Password Modify (RFC 3062) extended operation. </p>
<p> <code>ldappasswd</code> sets the password of associated with the user [or an optionally specified <i>user</i>]. If the new password is not specified on the command line and the user doesn&#8217;t enable prompting, the server will be asked to generate a password for the user. </p>
<p> <code>ldappasswd</code> is neither designed nor intended to be a replacement for <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1) and should not be installed as such.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>[<code>V</code>]</p>
<dd> Print version info. If <code>-VV</code> is given, only the version information is printed.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debuglevel</i></p>
<dd> Set the LDAP debugging level to <i>debuglevel</i>. <code>ldappasswd</code> must be compiled with LDAP_DEBUG defined for this option to have any effect.</p>
<dt><code>-n</code></p>
<dd> Do not set password. (Can be useful when used in conjunction with <code>-v</code> or <code>-d</code>)</p>
<dt><code>-v</code></p>
<dd> Increase the verbosity of output. Can be specified multiple times.</p>
<dt><code>-A</code></p>
<dd> Prompt for old password. This is used instead of specifying the password on the command line.</p>
<dt><code>-a</code><i>&nbsp;<wbr>oldPasswd</i></p>
<dd> Set the old password to <i>oldPasswd</i>.</p>
<dt><code>-t</code><i>&nbsp;<wbr>oldPasswdFile</i></p>
<dd> Set the old password to the contents of <i>oldPasswdFile</i>.</p>
<dt><code>-S</code></p>
<dd> Prompt for new password. This is used instead of specifying the password on the command line.</p>
<dt><code>-s</code><i>&nbsp;<wbr>newPasswd</i></p>
<dd> Set the new password to <i>newPasswd</i>.</p>
<dt><code>-T</code><i>&nbsp;<wbr>newPasswdFile</i></p>
<dd> Set the new password to the contents of <i>newPasswdFile</i>.</p>
<dt><code>-x </code></p>
<dd> Use simple authentication instead of SASL.</p>
<dt><code>-D</code><i>&nbsp;<wbr>binddn</i></p>
<dd> Use the Distinguished Name <i>binddn</i> to bind to the LDAP directory. For SASL binds, the server is expected to ignore this value.</p>
<dt><code>-W</code></p>
<dd> Prompt for bind password. This is used instead of specifying the password on the command line.</p>
<dt><code>-w</code><i>&nbsp;<wbr>passwd</i></p>
<dd> Use <i>passwd</i> as the password to bind with.</p>
<dt><code>-y</code><i>&nbsp;<wbr>passwdfile</i></p>
<dd> Use complete contents of <i>passwdfile</i> as the password for simple authentication.</p>
<dt><code>-H</code><i>&nbsp;<wbr>ldapuri</i></p>
<dd> Specify URI(s) referring to the ldap server(s); only the protocol/host/port fields are allowed; a list of URI, separated by whitespace or commas is expected.</p>
<dt><code>-h</code><i>&nbsp;<wbr>ldaphost</i></p>
<dd> Specify an alternate host on which the ldap server is running. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-p</code><i>&nbsp;<wbr>ldapport</i></p>
<dd> Specify an alternate TCP port where the ldap server is listening. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<dt><code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<p> Specify general extensions with <code>-e</code> and passwd modify extensions with <code>-E</code>. &#8216;<code>!</code>&#8216; indicates criticality. </p>
<p> General extensions: </p>
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
<p> Passwd Modify extensions: </p>
<pre>
  (none)
</pre>
<dt><code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]]</p>
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
<dd> Specify the requested authorization ID for SASL bind. <i>authzid</i> must be one of the following formats: <code>dn:</code><i>&lt;distinguished name&gt;</i> or <code>u:</code><i>&lt;username&gt;</i>.</p>
<dt><code>-Y</code><i>&nbsp;<wbr>mech</i></p>
<dd> Specify the SASL mechanism to be used for authentication. If it&#8217;s not specified, the program will choose the best mechanism the server knows.</p>
<dt><code>-Z</code>[<code>Z</code>]</p>
<dd> Issue StartTLS (Transport Layer Security) extended operation. If you use <code>-ZZ</code>, the command will require the operation to be successful</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap_sasl_bind/">ldap_sasl_bind</a></code>(3), <code><a href="/docs/linux/man/3-ldap_extended_operation/">ldap_extended_operation</a></code>(3), <code><a href="/docs/linux/man/3-ldap_start_tls_s/">ldap_start_tls_s</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
