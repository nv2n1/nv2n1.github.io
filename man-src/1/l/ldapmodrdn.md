---
title: "ldapmodrdn(1)"
name: "ldapmodrdn"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapmodrdn/"
description: "ldapmodrdn – LDAP rename entry tool"
---

<h2 class="name">NAME</h2>
<p> ldapmodrdn &#8211; LDAP rename entry tool </p>
<h2>SYNOPSIS</h2>
<p> <code>ldapmodrdn</code> [<code>-V</code>[<code>V</code>]] [<code>-d</code><i>&nbsp;<wbr>debuglevel</i>] [<code>-n</code>] [<code>-v</code>] [<code>-r</code>] [<code>-s</code><i>&nbsp;<wbr>newsup</i>] [<code>-c</code>] [<code>-f</code><i>&nbsp;<wbr>file</i>] [<code>-M</code>[<code>M</code>]] [<code>-x</code>] [<code>-D</code><i>&nbsp;<wbr>binddn</i>] [<code>-W</code>] [<code>-w</code><i>&nbsp;<wbr>passwd</i>] [<code>-y</code><i>&nbsp;<wbr>passwdfile</i>] [<code>-H</code><i>&nbsp;<wbr>ldapuri</i>] [<code>-h</code><i>&nbsp;<wbr>ldaphost</i>] [<code>-p</code><i>&nbsp;<wbr>ldapport</i>] [<code>-P</code>&nbsp;<wbr>{<code>2</code>|<code>3</code>}] [<code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]] [<code>-O</code><i>&nbsp;<wbr>security-properties</i>] [<code>-I</code>] [<code>-Q</code>] [<code>-N</code>] [<code>-U</code><i>&nbsp;<wbr>authcid</i>] [<code>-R</code><i>&nbsp;<wbr>realm</i>] [<code>-X</code><i>&nbsp;<wbr>authzid</i>] [<code>-Y</code><i>&nbsp;<wbr>mech</i>] [<code>-Z</code>[<code>Z</code>]] [<i>dn rdn</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ldapmodrdn</code> is a shell-accessible interface to the <code><a href="/docs/linux/man/3-ldap_rename/">ldap_rename</a></code>(3) library call. </p>
<p> <code>ldapmodrdn</code> opens a connection to an LDAP server, binds, and modifies the RDN of entries. The entry information is read from standard input, from <i>file</i> through the use of the &#8211;<i>f</i> option, or from the command-line pair <i>dn</i> and <i>rdn</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>[<code>V</code>]</dt>
<dd> Print version info. If <code>-VV</code> is given, only the version information is printed.</dd>
<dt><code>-d</code><i>&nbsp;<wbr>debuglevel</i></dt>
<dd> Set the LDAP debugging level to <i>debuglevel</i>. <code>ldapmodrdn</code> must be compiled with LDAP_DEBUG defined for this option to have any effect.</dd>
<dt><code>-n</code></dt>
<dd> Show what would be done, but don&#8217;t actually change entries. Useful for debugging in conjunction with <code>-v</code>.</dd>
<dt><code>-v</code></dt>
<dd> Use verbose mode, with many diagnostics written to standard output.</dd>
<dt><code>-r</code></dt>
<dd> Remove old RDN values from the entry. Default is to keep old values.</dd>
<dt><code>-s</code><i>&nbsp;<wbr>newsup</i></dt>
<dd> Specify a new superior entry. (I.e., move the target entry and make it a child of the new superior.) This option is not supported in LDAPv2.</dd>
<dt><code>-c</code></dt>
<dd> Continuous operation mode. Errors are reported, but ldapmodrdn will continue with modifications. The default is to exit after reporting an error.</dd>
<dt><code>-f</code><i>&nbsp;<wbr>file</i></dt>
<dd> Read the entry modification information from <i>file</i> instead of from standard input or the command-line.</dd>
<dt><code>-M</code>[<code>M</code>]</dt>
<dd> Enable manage DSA IT control. <code>-MM</code> makes control critical.</dd>
<dt><code>-x </code></dt>
<dd> Use simple authentication instead of SASL.</dd>
<dt><code>-D</code><i>&nbsp;<wbr>binddn</i></dt>
<dd> Use the Distinguished Name <i>binddn</i> to bind to the LDAP directory. For SASL binds, the server is expected to ignore this value.</dd>
<dt><code>-W</code></dt>
<dd> Prompt for simple authentication. This is used instead of specifying the password on the command line.</dd>
<dt><code>-w</code><i>&nbsp;<wbr>passwd</i></dt>
<dd> Use <i>passwd</i> as the password for simple authentication.</dd>
<dt><code>-y</code><i>&nbsp;<wbr>passwdfile</i></dt>
<dd> Use complete contents of <i>passwdfile</i> as the password for simple authentication.</dd>
<dt><code>-H</code><i>&nbsp;<wbr>ldapuri</i></dt>
<dd> Specify URI(s) referring to the ldap server(s); only the protocol/host/port fields are allowed; a list of URI, separated by whitespace or commas is expected.</dd>
<dt><code>-h</code><i>&nbsp;<wbr>ldaphost</i></dt>
<dd> Specify an alternate host on which the ldap server is running. Deprecated in favor of <code>-H</code>.</dd>
<dt><code>-p</code><i>&nbsp;<wbr>ldapport</i></dt>
<dd> Specify an alternate TCP port where the ldap server is listening. Deprecated in favor of <code>-H</code>.</dd>
<dt><code>-P</code>&nbsp;<wbr>{<code>2</code>|<code>3</code>}</dt>
<dd> Specify the LDAP protocol version to use.</dd>
<dt><code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</dt>
<dd>
</dd><dt><code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</dt>
<dd>
<p> Specify general extensions with <code>-e</code> and modrdn extensions with <code>-E</code>. &#8216;<code>!</code>&#8216; indicates criticality. </p>
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
<p> Modrdn extensions: </p>
<pre>
  (none)
</pre>
</dd><dt><code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]</dt>
<dd>
<p> Specify general options. </p>
<p> General options: </p>
<pre>
  nettimeout=&lt;timeout&gt;  (in seconds, or &quot;none&quot; or &quot;max&quot;)
  ldif-wrap=&lt;width&gt;     (in columns, or &quot;no&quot; for no wrapping)
</pre>
</dd><dt><code>-O</code><i>&nbsp;<wbr>security-properties</i></dt>
<dd> Specify SASL security properties.</dd>
<dt><code>-I</code></dt>
<dd> Enable SASL Interactive mode. Always prompt. Default is to prompt only as needed.</dd>
<dt><code>-Q</code></dt>
<dd> Enable SASL Quiet mode. Never prompt.</dd>
<dt><code>-N</code></dt>
<dd> Do not use reverse DNS to canonicalize SASL host name.</dd>
<dt><code>-U</code><i>&nbsp;<wbr>authcid</i></dt>
<dd> Specify the authentication ID for SASL bind. The form of the ID depends on the actual SASL mechanism used.</dd>
<dt><code>-R</code><i>&nbsp;<wbr>realm</i></dt>
<dd> Specify the realm of authentication ID for SASL bind. The form of the realm depends on the actual SASL mechanism used.</dd>
<dt><code>-X</code><i>&nbsp;<wbr>authzid</i></dt>
<dd> Specify the requested authorization ID for SASL bind. <i>authzid</i> must be one of the following formats: <code>dn:</code><i>&lt;distinguished name&gt;</i> or <code>u:</code><i>&lt;username&gt;</i></dd>
<dt><code>-Y</code><i>&nbsp;<wbr>mech</i></dt>
<dd> Specify the SASL mechanism to be used for authentication. If it&#8217;s not specified, the program will choose the best mechanism the server knows.</dd>
<dt><code>-Z</code>[<code>Z</code>]</dt>
<dd> Issue StartTLS (Transport Layer Security) extended operation. If you use <code>-ZZ</code>, the command will require the operation to be successful.</dd></dl>
<h2>INPUT FORMAT</h2>
<p> If the command-line arguments <i>dn</i> and <i>rdn</i> are given, <i>rdn</i> will replace the RDN of the entry specified by the DN, <i>dn</i>. </p>
<p> Otherwise, the contents of <i>file</i> (or standard input if no <code>-f</code> flag is given) should consist of one or more entries. </p>
<pre>
    Distinguished Name (DN)
    Relative Distinguished Name (RDN)
</pre>
<p> One or more blank lines may be used to separate each DN/RDN pair.</p>
<h2>EXAMPLE</h2>
<p> Assuming that the file <code>/tmp/entrymods</code> exists and has the contents: </p>
<pre>
    cn=Modify Me,dc=example,dc=com
    cn=The New Me
</pre>
<p> the command: </p>
<pre>
    ldapmodrdn -r -f /tmp/entrymods
</pre>
<p> will change the RDN of the &quot;Modify Me&quot; entry from &quot;Modify Me&quot; to &quot;The New Me&quot; and the old cn, &quot;Modify Me&quot; will be removed. </p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1), <code><a href="/docs/linux/man/1-ldapdelete/">ldapdelete</a></code>(1), <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1), <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5), <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_rename/">ldap_rename</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
