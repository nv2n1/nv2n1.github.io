---
title: "syntax-validate-pl(8)"
name: "syntax-validate-pl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-syntax-validate-pl/"
description: "syntax-validate.pl – Directory Server perl script for validating attribute syntax."
---

<p>syntax-validate.pl &#8211; Directory Server perl script for validating attribute syntax.</p>
<h2>Synopsis</h2>
<p>syntax-validate.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } -b baseDN [-f filter] [-P protocol] [-v] [-h]</p>
<h2>Description</h2>
<p>Syntax validation checks every modification to attributes to make sure that the new value has the required syntax for that attribute type. All attribute syntaxes are validated against the definitions in RFC 4514.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-D</code> <i>Root DN</i></p>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</p>
<dt><code>-w</code> <i>password</i></p>
<dd>The rootdn password.</p>
<dt><code>-w &#8211;</code></p>
<dd>Prompt for the rootdn password.</p>
<dt><code>-j</code> <i>password filename</i></p>
<dd>The name of the file that contains the root DN password.</p>
<dt><code>-b</code> <i>baseDN</i></p>
<dd>Gives the base DN for the entries to validate.</p>
<dt><code>-f</code> <i>filter</i></p>
<dd>Contains a search filter to use to select a subset of entries to validate. If this is not given, then all entries under the base DN are checked.</p>
<dt><code>-P</code> <i>protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>syntax-validate.pl -Z instance2 -D &#8216;cn=directory manager&#8217; -w password -b &#8216;dc=example,dc=com&#8217; -f &#8216;cn=*&#8217; -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>syntax-validate.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
