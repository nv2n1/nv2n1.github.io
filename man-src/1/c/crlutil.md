---
title: "crlutil(1)"
name: "crlutil"
section: "1"
letter: "c"
url: "/docs/linux/man/1-crlutil/"
description: "crlutil – List, generate, modify, or delete CRLs within the NSS security database file(s) and list, create, modify or delete certificates entries in a particular CRL."
---

<h2 class="name">NAME</h2>
<p> crlutil &#8211; List, generate, modify, or delete CRLs within the NSS security database file(s) and list, create, modify or delete certificates entries in a particular CRL. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>crlutil</code> [<i>options</i>] [[<i>arguments</i>]]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The Certificate Revocation List (CRL) Management Tool, <code>crlutil</code>, is a command-line utility that can list, generate, modify, or delete CRLs within the NSS security database file(s) and list, create, modify or delete certificates entries in a particular CRL. </p>
<p> The key and certificate management process generally begins with creating keys in the key database, then generating and managing certificates in the certificate database(see certutil tool) and continues with certificates expiration or revocation. </p>
<p> This document discusses certificate revocation list management. For information on security module database management, see Using the Security Module Database Tool. For information on certificate and key database management, see Using the Certificate Database Tool. </p>
<p> To run the Certificate Revocation List Management Tool, type the command </p>
<p> crlutil option [arguments] </p>
<p> where options and arguments are combinations of the options and arguments listed in the following section. Each command takes one option. Each option may take zero or more arguments. To see a usage string, issue the command without options, or with the -H option.</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<p> <code>Options</code> </p>
<p> Options specify an action. Option arguments modify an action. The options and arguments for the crlutil command are defined as follows: </p>
<p> -D</p>
<dl>
<dt>
<dd> Delete Certificate Revocation List from cert database.</dl>
<p> -E</p>
<dl>
<dt>
<dd> Erase all CRLs of specified type from the cert database</dl>
<p> -G</p>
<dl>
<dt>
<dd> Create new Certificate Revocation List (CRL).</dl>
<p> -I</p>
<dl>
<dt>
<dd> Import a CRL to the cert database</dl>
<p> -L</p>
<dl>
<dt>
<dd> List existing CRL located in cert database file.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Modify existing CRL which can be located in cert db or in arbitrary file. If located in file it should be encoded in ASN.1 encode format.</dl>
<p> -S</p>
<dl>
<dt>
<dd> Show contents of a CRL file which isn&#8217;t stored in the database.</dl>
<p> <code>Arguments</code> </p>
<p> Option arguments modify an action. </p>
<p> -a</p>
<dl>
<dt>
<dd> Use ASCII format or allow the use of ASCII format for input and output. This formatting follows RFC #1113.</dl>
<p> -B</p>
<dl>
<dt>
<dd> Bypass CA signature checks.</dl>
<p> -c crl-gen-file</p>
<dl>
<dt>
<dd> Specify script file that will be used to control crl generation/modification. See crl-cript-file format below. If options -M|-G is used and -c crl-script-file is not specified, crlutil will read script data from standard input.</dl>
<p> -d directory</p>
<dl>
<dt>
<dd> Specify the database directory containing the certificate and key database files. On Unix the Certificate Database Tool defaults to $HOME/.netscape (that is, ~/.netscape). On Windows NT the default is the current directory. </p>
<p> The NSS database files must reside in the same directory.</dl>
<p> -f password-file</p>
<dl>
<dt>
<dd> Specify a file that will automatically supply the password to include in a certificate or to access a certificate database. This is a plain-text file containing one password. Be sure to prevent unauthorized access to this file.</dl>
<p> -i crl-file</p>
<dl>
<dt>
<dd> Specify the file which contains the CRL to import or show.</dl>
<p> -l algorithm-name</p>
<dl>
<dt>
<dd> Specify a specific signature algorithm. List of possible algorithms: MD2 | MD4 | MD5 | SHA1 | SHA256 | SHA384 | SHA512</dl>
<p> -n nickname</p>
<dl>
<dt>
<dd> Specify the nickname of a certificate or key to list, create, add to a database, modify, or validate. Bracket the nickname string with quotation marks if it contains spaces.</dl>
<p> -o output-file</p>
<dl>
<dt>
<dd> Specify the output file name for new CRL. Bracket the output-file string with quotation marks if it contains spaces. If this argument is not used the output destination defaults to standard output.</dl>
<p> -P dbprefix</p>
<dl>
<dt>
<dd> Specify the prefix used on the NSS security database files (for example, my_cert8.db and my_key3.db). This option is provided as a special case. Changing the names of the certificate and key databases is not recommended.</dl>
<p> -t crl-type</p>
<dl>
<dt>
<dd> Specify type of CRL. possible types are: 0 &#8211; SEC_KRL_TYPE, 1 &#8211; SEC_CRL_TYPE. This option is obsolete</dl>
<p> -u url</p>
<dl>
<dt>
<dd> Specify the url.</dl>
<p> -w pwd-string</p>
<dl>
<dt>
<dd> Provide db password in command line.</dl>
<p> -Z algorithm</p>
<dl>
<dt>
<dd> Specify the hash algorithm to use for signing the CRL.</dl>
<h2>CRL GENERATION SCRIPT SYNTAX</h2>
<p> CRL generation script file has the following syntax: </p>
<p> * Line with comments should have # as a first symbol of a line </p>
<p> * Set &quot;this update&quot; or &quot;next update&quot; CRL fields: </p>
<p> update=YYYYMMDDhhmmssZ nextupdate=YYYYMMDDhhmmssZ </p>
<p> Field &quot;next update&quot; is optional. Time should be in GeneralizedTime format (YYYYMMDDhhmmssZ). For example: 20050204153000Z </p>
<p> * Add an extension to a CRL or a crl certificate entry: </p>
<p> addext extension-name critical/non-critical [arg1[arg2 &#8230;]] </p>
<p> Where: </p>
<p> extension-name: string value of a name of known extensions. critical/non-critical: is 1 when extension is critical and 0 otherwise. arg1, arg2: specific to extension type extension parameters </p>
<p> addext uses the range that was set earlier by addcert and will install an extension to every cert entries within the range. </p>
<p> * Add certificate entries(s) to CRL: </p>
<p> addcert range date </p>
<p> range: two integer values separated by dash: range of certificates that will be added by this command. dash is used as a delimiter. Only one cert will be added if there is no delimiter. date: revocation date of a cert. Date should be represented in GeneralizedTime format (YYYYMMDDhhmmssZ). </p>
<p> * Remove certificate entry(s) from CRL </p>
<p> rmcert range </p>
<p> Where: </p>
<p> range: two integer values separated by dash: range of certificates that will be added by this command. dash is used as a delimiter. Only one cert will be added if there is no delimiter. </p>
<p> * Change range of certificate entry(s) in CRL </p>
<p> range new-range </p>
<p> Where: </p>
<p> new-range: two integer values separated by dash: range of certificates that will be added by this command. dash is used as a delimiter. Only one cert will be added if there is no delimiter. </p>
<p> Implemented Extensions </p>
<p> The extensions defined for CRL provide methods for associating additional attributes with CRLs of theirs entries. For more information see RFC #3280 </p>
<p> * Add The Authority Key Identifier extension: </p>
<p> The authority key identifier extension provides a means of identifying the public key corresponding to the private key used to sign a CRL. </p>
<p> authKeyId critical [key-id | dn cert-serial] </p>
<p> Where: </p>
<p> authKeyIdent: identifies the name of an extension critical: value of 1 of 0. Should be set to 1 if this extension is critical or 0 otherwise. key-id: key identifier represented in octet string. dn:: is a CA distinguished name cert-serial: authority certificate serial number. </p>
<p> * Add Issuer Alternative Name extension: </p>
<p> The issuer alternative names extension allows additional identities to be associated with the issuer of the CRL. Defined options include an rfc822 name (electronic mail address), a DNS name, an IP address, and a URI. </p>
<p> issuerAltNames non-critical name-list </p>
<p> Where: </p>
<p> subjAltNames: identifies the name of an extension should be set to 0 since this is non-critical extension name-list: comma separated list of names </p>
<p> * Add CRL Number extension: </p>
<p> The CRL number is a non-critical CRL extension which conveys a monotonically increasing sequence number for a given CRL scope and CRL issuer. This extension allows users to easily determine when a particular CRL supersedes another CRL </p>
<p> crlNumber non-critical number </p>
<p> Where: </p>
<p> crlNumber: identifies the name of an extension critical: should be set to 0 since this is non-critical extension number: value of long which identifies the sequential number of a CRL. </p>
<p> * Add Revocation Reason Code extension: </p>
<p> The reasonCode is a non-critical CRL entry extension that identifies the reason for the certificate revocation. </p>
<p> reasonCode non-critical code </p>
<p> Where: </p>
<p> reasonCode: identifies the name of an extension non-critical: should be set to 0 since this is non-critical extension code: the following codes are available: </p>
<p> unspecified (0), keyCompromise (1), cACompromise (2), affiliationChanged (3), superseded (4), cessationOfOperation (5), certificateHold (6), removeFromCRL (8), privilegeWithdrawn (9), aACompromise (10) </p>
<p> * Add Invalidity Date extension: </p>
<p> The invalidity date is a non-critical CRL entry extension that provides the date on which it is known or suspected that the private key was compromised or that the certificate otherwise became invalid. </p>
<p> invalidityDate non-critical date </p>
<p> Where: </p>
<p> crlNumber: identifies the name of an extension non-critical: should be set to 0 since this is non-critical extension date: invalidity date of a cert. Date should be represented in GeneralizedTime format (YYYYMMDDhhmmssZ).</p>
<h2>USAGE</h2>
<p> The Certificate Revocation List Management Tool&#8217;s capabilities are grouped as follows, using these combinations of options and arguments. Options and arguments in square brackets are optional, those without square brackets are required. </p>
<p> See &quot;Implemented extensions&quot; for more information regarding extensions and their parameters. </p>
<p> * Creating or modifying a CRL: </p>
<dl>
<dt>
<dd>
<pre><code>
crlutil - G | -M - c crl - gen - file - n nickname[-i crl][-u url][-d keydir][-P dbprefix][-l alg][-a][-B]
</code></pre>
</dl>
<p> * Listing all CRls or a named CRL: </p>
<dl>
<dt>
<dd>
crlutil &#8211; L[-n crl &#8211; name][-d krydir]
</dl>
<p> * Deleting CRL from db: </p>
<dl>
<dt>
<dd>
crlutil &#8211; D &#8211; n nickname[-d keydir][-P dbprefix]
</dl>
<p> * Erasing CRLs from db: </p>
<dl>
<dt>
<dd>
crlutil &#8211; E[-d keydir][-P dbprefix]
</dl>
<p> * Deleting CRL from db: </p>
<dl>
<dt>
<dd>
crlutil &#8211; D &#8211; n nickname[-d keydir][-P dbprefix]
</dl>
<p> * Erasing CRLs from db: </p>
<dl>
<dt>
<dd>
crlutil &#8211; E[-d keydir][-P dbprefix]
</dl>
<p> * Import CRL from file: </p>
<dl>
<dt>
<dd>
<pre><code>
crlutil - I - i crl[-t crlType][-u url][-d keydir][-P dbprefix][-B]
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-certutil/">certutil</a>(1)</p>
<h2>ADDITIONAL RESOURCES</h2>
<p> For information about NSS and other tools related to NSS (like JSS), check out the NSS project wiki at m[blue]<code><a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></code>m[]. The NSS site relates directly to NSS code changes and releases. </p>
<p> Mailing lists: <a rel="nofollow" href="https://lists.mozilla.org/listinfo/dev-tech-crypto">https://lists.mozilla.org/listinfo/dev-tech-crypto</a> </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The NSS tools were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Mozilla NSS bug 836477</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dl>
</dl>
<h2>Index</h2>
