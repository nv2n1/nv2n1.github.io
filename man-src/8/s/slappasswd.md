---
title: "slappasswd(8)"
name: "slappasswd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slappasswd/"
description: "slappasswd – OpenLDAP password utility"
---

<p>slappasswd &#8211; OpenLDAP password utility</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slappasswd</code> [<code>-v</code>] [<code>-u</code>] [<code>-g</code>|<code>-s</code>&nbsp;<wbr><i>secret</i><code>|</code><code>-T&nbsp;<wbr></code><i>file</i>] [<code>-h</code><i>&nbsp;<wbr>hash</i>] [<code>-c</code><i>&nbsp;<wbr>salt-format</i>] [<code>-n</code>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] </p>
<h2>Description</h2>
<p><code>Slappasswd</code> is used to generate an userPassword value suitable for use with <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) <i>rootpw</i> configuration directive or the <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5) <i>olcRootPW</i> configuration directive.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>enable verbose mode.</p>
<dt><code>-u</code></p>
<dd>Generate RFC 2307 userPassword values (the default). Future versions of this program may generate alternative syntaxes by default. This option is provided for forward compatibility.</p>
<dt><code>-s</code><i>&nbsp;<wbr>secret</i></p>
<dd>The secret to hash. If this, <code>-g</code> and <code>-T</code> are absent, the user will be prompted for the secret to hash. <code>-s</code>, <code>-g</code> and <code>-T</code> are mutually exclusive flags.</p>
<dt><code>-g</code></p>
<dd>Generate the secret. If this, <code>-s</code> and <code>-T</code> are absent, the user will be prompted for the secret to hash. <code>-s</code>, <code>-g</code> and <code>-T</code> are mutually exclusive flags. If this is present, <i>{CLEARTEXT}</i> is used as scheme. <code>-g</code> and <code>-h</code> are mutually exclusive flags.</p>
<dt><code>-T</code><i>&nbsp;<wbr>file</i></p>
<dd>Hash the contents of the file. If this, <code>-g</code> and <code>-s</code> are absent, the user will be prompted for the secret to hash. <code>-s</code>, <code>-g</code> and <code>-T</code> and mutually exclusive flags.</p>
<dt><code>-h</code><i>&nbsp;<wbr>scheme</i></p>
<dd>If <code>-h</code> is specified, one of the following RFC 2307 schemes may be specified: <code>{CRYPT}</code>, <code>{MD5}</code>, <code>{SMD5}</code>, <code>{SSHA}</code>, and <code>{SHA}</code>. The default is <code>{SSHA}</code>. </p>
<p> Note that scheme names may need to be protected, due to <code>{</code> and <code>}</code>, from expansion by the user&#8217;s command interpreter. </p>
<p> <code>{SHA}</code> and <code>{SSHA}</code> use the SHA-1 algorithm (FIPS 160-1), the latter with a seed. </p>
<p> <code>{MD5}</code> and <code>{SMD5}</code> use the MD5 algorithm (RFC 1321), the latter with a seed. </p>
<p> <code>{CRYPT}</code> uses the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). </p>
<p> <code>{CLEARTEXT}</code> indicates that the new password should be added to userPassword as clear text. Unless <i>{CLEARTEXT}</i> is used, this flag is incompatible with option <code>-g</code>.</p>
<dt><code>-c</code><i>&nbsp;<wbr>crypt-salt-format</i></p>
<dd>Specify the format of the salt passed to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) when generating {CRYPT} passwords. This string needs to be in <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) format and may include one (and only one) <code>%s</code> conversion. This conversion will be substituted with a string of random characters from [A-Za-z0-9./]. For example, &#8216;<code>%.2s</code>&#8216; provides a two character salt and &#8216;<code>$1$%.8s</code>&#8216; tells some versions of <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) to use an MD5 algorithm and provides 8 random characters of salt. The default is &#8216;<code>%s</code>&#8216;<code>,</code> which provides 31 characters of salt.</p>
<dt><code>-n</code></p>
<dd>Omit the trailing newline; useful to pipe the credentials into a command.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> module-path=&lt;pathspec&gt; (see `<code>modulepath</code>' in <a href="//www.systutorials.com/docs/linux/man/5-slapd.conf/">slapd.conf</a>(5))
 module-load=&lt;filename&gt; (see `<code>moduleload</code>' in <a href="//www.systutorials.com/docs/linux/man/5-slapd.conf/">slapd.conf</a>(5))
You can load a dynamically loadable password hash module by
using this option.</pre>
<h2>Limitations</h2>
<p>The practice of storing hashed passwords in userPassword violates Standard Track (RFC 4519) schema specifications and may hinder interoperability. A new attribute type, authPassword, to hold hashed passwords has been defined (RFC 3112), but is not yet implemented in <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). </p>
<p> It should also be noted that the behavior of <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) is platform specific.</p>
<h2>Security Considerations</h2>
<p>Use of hashed passwords does not protect passwords during protocol transfer. TLS or other eavesdropping protections should be in-place before using LDAP simple bind. </p>
<p> The hashed password values should be protected as if they were clear text passwords.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ldappasswd/">ldappasswd</a></code>(1), <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code>RFC 2307</code>, <code>RFC 4519</code>, <code>RFC 3112</code> </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
