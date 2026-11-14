---
title: "ldapurl(1)"
name: "ldapurl"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapurl/"
description: "ldapurl – LDAP URL formatting tool"
---

<h2 class="name">NAME</h2>
<p> ldapurl &#8211; LDAP URL formatting tool </p>
<h2>SYNOPSIS</h2>
<p> <code>ldapurl</code> [<code>-a</code>&nbsp;<wbr>attrs] [<code>-b</code><i>&nbsp;<wbr>searchbase</i>] [<code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-f</code><i>&nbsp;<wbr>filter</i>] [<code>-H</code><i>&nbsp;<wbr>ldapuri</i>] [<code>-h</code><i>&nbsp;<wbr>ldaphost</i>] [<code>-p</code><i>&nbsp;<wbr>ldapport</i>] [<code>-s</code>&nbsp;<wbr>{<code>base</code>|<code>one</code>|<code>sub</code>|<code>children</code>}] [<code>-S</code><i>&nbsp;<wbr>scheme</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>ldapurl</i> is a command that allows to either compose or decompose LDAP URIs. </p>
<p> When invoked with the <code>-H</code> option, <code>ldapurl</code> extracts the components of the <i>ldapuri</i> option argument, unescaping hex-escaped chars as required. It basically acts as a frontend to the <code><a href="/docs/linux/man/3-ldap_url_parse/">ldap_url_parse</a></code>(3) call. Otherwise, it builds an LDAP URI based on the components passed with the appropriate options, performing the inverse operation. Option <code>-H</code> is incompatible with options <code>-a</code>, <code>-b</code>, <code>-E</code>, <code>-f</code>, <code>-H</code>, <code>-h</code>, <code>-p</code>, <code>-S</code>, and <code>-s</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-a</code><i>&nbsp;<wbr>attrs</i></p>
<dd>
<dd> Set a comma-separated list of attribute selectors.</p>
<dt><code>-b</code><i>&nbsp;<wbr>searchbase</i></p>
<dd> Set the <i>searchbase</i>.</p>
<dt><code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<p> Specify general extensions with <code>-e</code> &#8216;<code>!</code>&#8216; indicates criticality. </p>
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
<dt><code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd> Set URL extensions; incompatible with <code>-H</code>.</p>
<dt><code>-f</code><i>&nbsp;<wbr>filter</i></p>
<dd> Set the URL filter. No particular check on conformity with RFC 4515 LDAP filters is performed, but the value is hex-escaped as required.</p>
<dt><code>-H</code><i>&nbsp;<wbr>ldapuri</i></p>
<dd> Specify URI to be exploded.</p>
<dt><code>-h</code><i>&nbsp;<wbr>ldaphost</i></p>
<dd> Set the host.</p>
<dt><code>-p</code><i>&nbsp;<wbr>ldapport</i></p>
<dd> Set the TCP port.</p>
<dt><code>-S</code><i>&nbsp;<wbr>scheme</i></p>
<dd> Set the URL scheme. Defaults for other fields, like <i>ldapport</i>, may depend on the value of <i>scheme</i>.</p>
<dt><code>-s</code>&nbsp;<wbr>{<code>base</code>|<code>one</code>|<code>sub</code>|<code>children</code>}</p>
<dd> Specify the scope of the search to be one of <code>base</code>, <code>one</code>, <code>sub</code>, or <code>children</code> to specify a base object, one-level, subtree, or children search. The default is <code>sub</code>. Note: <code>children</code> scope requires LDAPv3 subordinate feature extension. </p>
</dl>
<h2>OUTPUT FORMAT</h2>
<p> If the <code>-H</code> option is used, the <i>ldapuri</i> supplied is exploded in its components, which are printed to standard output in an LDIF-like form. </p>
<p> Otherwise, the URI built using the values passed with the other options is printed to standard output.</p>
<h2>EXAMPLE</h2>
<p> The following command: </p>
<pre>
    ldapurl -h ldap.example.com -b dc=example,dc=com -s sub -f &quot;(cn=Some One)&quot;
</pre>
<p> returns </p>
<pre>
    <a href="ldap://ldap.example.com:389/dc=example,dc=com??sub?(cn=Some%20One)">ldap://ldap.example.com:389/dc=example,dc=com??sub?(cn=Some%20One)</a>
</pre>
<p> The command: </p>
<pre>
    ldapurl -H <a href="ldap://ldap.example.com:389/dc=example,dc=com??sub?(cn=Some%20One)">ldap://ldap.example.com:389/dc=example,dc=com??sub?(cn=Some%20One)</a>
</pre>
<p> returns </p>
<pre>
    scheme: ldap
    host: ldap.example.com
    port: 389
    dn: dc=example,dc=com
    scope: sub
    filter: (cn=Some One)
</pre>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_url_parse/">ldap_url_parse</a></code>(3),</p>
<h2>AUTHOR</h2>
<p> The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
