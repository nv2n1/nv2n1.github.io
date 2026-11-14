---
title: "ldapcompare(1)"
name: "ldapcompare"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapcompare/"
description: "ldapcompare – LDAP compare tool"
---

<h2 class="name">NAME</h2>
<p> ldapcompare &#8211; LDAP compare tool </p>
<h2>SYNOPSIS</h2>
<p> <code>ldapcompare</code> [<code>-V</code>[<code>V</code>]] [<code>-d</code><i>&nbsp;<wbr>debuglevel</i>] [<code>-n</code>] [<code>-v</code>] [<code>-z</code>] [<code>-M</code>[<code>M</code>]] [<code>-x</code>] [<code>-D</code><i>&nbsp;<wbr>binddn</i>] [<code>-W</code>] [<code>-w</code><i>&nbsp;<wbr>passwd</i>] [<code>-y</code><i>&nbsp;<wbr>passwdfile</i>] [<code>-H</code><i>&nbsp;<wbr>ldapuri</i>] [<code>-h</code><i>&nbsp;<wbr>ldaphost</i>] [<code>-p</code><i>&nbsp;<wbr>ldapport</i>] [<code>-P</code>&nbsp;<wbr>{<code>2</code>|<code>3</code>}] [<code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]] [<code>-O</code><i>&nbsp;<wbr>security-properties</i>] [<code>-I</code>] [<code>-Q</code>] [<code>-N</code>] [<code>-U</code><i>&nbsp;<wbr>authcid</i>] [<code>-R</code><i>&nbsp;<wbr>realm</i>] [<code>-X</code><i>&nbsp;<wbr>authzid</i>] [<code>-Y</code><i>&nbsp;<wbr>mech</i>] [<code>-Z</code>[<code>Z</code>]] <i>DN</i> {<code>attr:</code><i>value</i> | <code>attr::</code><i>b64value</i>}</p>
<h2>DESCRIPTION</h2>
<p> <i>ldapcompare</i> is a shell-accessible interface to the <code><a href="/docs/linux/man/3-ldap_compare_ext/">ldap_compare_ext</a></code>(3) library call. </p>
<p> <code>ldapcompare</code> opens a connection to an LDAP server, binds, and performs a compare using specified parameters. The <i>DN</i> should be a distinguished name in the directory. <i>Attr</i> should be a known attribute. If followed by one colon, the assertion <i>value</i> should be provided as a string. If followed by two colons, the base64 encoding of the value is provided. The result code of the compare is provided as the exit code and, unless ran with <code>-z</code>, the program prints TRUE, FALSE, or UNDEFINED on standard output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>[<code>V</code>]</p>
<dd> Print version info. If <code>-VV</code> is given, only the version information is printed.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debuglevel</i></p>
<dd> Set the LDAP debugging level to <i>debuglevel</i>. <code>ldapcompare</code> must be compiled with LDAP_DEBUG defined for this option to have any effect.</p>
<dt><code>-n</code></p>
<dd> Show what would be done, but don&#8217;t actually perform the compare. Useful for debugging in conjunction with <code>-v</code>.</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode, with many diagnostics written to standard output.</p>
<dt><code>-z</code></p>
<dd> Run in quiet mode, no output is written. You must check the return status. Useful in shell scripts.</p>
<dt><code>-M</code>[<code>M</code>]</p>
<dd> Enable manage DSA IT control. <code>-MM</code> makes control critical.</p>
<dt><code>-x </code></p>
<dd> Use simple authentication instead of SASL.</p>
<dt><code>-D</code><i>&nbsp;<wbr>binddn</i></p>
<dd> Use the Distinguished Name <i>binddn</i> to bind to the LDAP directory. For SASL binds, the server is expected to ignore this value.</p>
<dt><code>-W</code></p>
<dd> Prompt for simple authentication. This is used instead of specifying the password on the command line.</p>
<dt><code>-w</code><i>&nbsp;<wbr>passwd</i></p>
<dd> Use <i>passwd</i> as the password for simple authentication.</p>
<dt><code>-y</code><i>&nbsp;<wbr>passwdfile</i></p>
<dd> Use complete contents of <i>passwdfile</i> as the password for simple authentication. Note that <i>complete</i> means that any leading or trailing whitespaces, including newlines, will be considered part of the password and, unlike other software, they will not be stripped. As a consequence, passwords stored in files by commands like <code><a href="/docs/linux/man/1-echo/">echo</a></code>(1) will not behave as expected, since <code><a href="/docs/linux/man/1-echo/">echo</a></code>(1) by default appends a trailing newline to the echoed string. The recommended portable way to store a cleartext password in a file for use with this option is to use <code><a href="/docs/linux/man/8-slappasswd/">slappasswd</a></code>(8) with <i>{CLEARTEXT}</i> as hash and the option <code>-n</code>.</p>
<dt><code>-H</code><i>&nbsp;<wbr>ldapuri</i></p>
<dd> Specify URI(s) referring to the ldap server(s); only the protocol/host/port fields are allowed; a list of URI, separated by whitespace or commas is expected.</p>
<dt><code>-h</code><i>&nbsp;<wbr>ldaphost</i></p>
<dd> Specify an alternate host on which the ldap server is running. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-p</code><i>&nbsp;<wbr>ldapport</i></p>
<dd> Specify an alternate TCP port where the ldap server is listening. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-P</code>&nbsp;<wbr>{<code>2</code>|<code>3</code>}</p>
<dd> Specify the LDAP protocol version to use.</p>
<dt><code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<dt><code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<p> Specify general extensions with <code>-e</code> and compare extensions with <code>-E</code>. &#8216;<code>!</code>&#8216; indicates criticality. </p>
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
<p> Compare extensions: </p>
<pre>
  !dontUseCopy
</pre>
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
<dd> Specify the SASL mechanism to be used for authentication. If it&#8217;s not specified, the program will choose the best mechanism the server knows.</p>
<dt><code>-Z</code>[<code>Z</code>]</p>
<dd> Issue StartTLS (Transport Layer Security) extended operation. If you use <code>-ZZ</code>, the command will require the operation to be successful.</dl>
<h2>EXAMPLES</h2>
<pre>
    ldapcompare &quot;uid=babs,dc=example,dc=com&quot;  sn:Jensen
    ldapcompare &quot;uid=babs,dc=example,dc=com&quot;  sn::SmVuc2Vu
</pre>
<p> are all equivalent.</p>
<h2>LIMITATIONS</h2>
<p> Requiring the value be passed on the command line is limiting and introduces some security concerns. The command should support a mechanism to specify the location (file name or URL) to read the value from.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5), <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_compare_ext/">ldap_compare_ext</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
