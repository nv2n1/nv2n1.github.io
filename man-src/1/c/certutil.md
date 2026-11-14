---
title: "certutil(1)"
name: "certutil"
section: "1"
letter: "c"
url: "/docs/linux/man/1-certutil/"
description: "certutil – Manage keys and certificate in both NSS databases and other NSS tokens"
---

<h2 class="name">NAME</h2>
<p> certutil &#8211; Manage keys and certificate in both NSS databases and other NSS tokens </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>certutil</code> [<i>options</i>] [[<i>arguments</i>]]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The Certificate Database Tool, <code>certutil</code>, is a command-line utility that can create and modify certificate and key databases. It can specifically list, generate, modify, or delete certificates, create or change the password, generate new public and private key pairs, display the contents of the key database, or delete key pairs within the key database. </p>
<p> Certificate issuance, part of the key and certificate management process, requires that keys and certificates be created in the key database. This document discusses certificate and key database management. For information on the security module database management, see the <code>modutil</code> manpage.</p>
<h2>COMMAND OPTIONS AND ARGUMENTS</h2>
<p> Running <code>certutil</code> always requires one and only one command option to specify the type of certificate operation. Each command option may take zero or more arguments. The command option <code>-H</code> will list all the command options and their relevant arguments. </p>
<p> <code>Command Options</code> </p>
<p> -A</p>
<dl>
<dt>
<dd> Add an existing certificate to a certificate database. The certificate database should already exist; if one is not present, this command option will initialize one by default.</dl>
<p> -B</p>
<dl>
<dt>
<dd> Run a series of commands from the specified batch file. This requires the <code>-i</code> argument.</dl>
<p> -C</p>
<dl>
<dt>
<dd> Create a new binary certificate file from a binary certificate request file. Use the <code>-i</code> argument to specify the certificate request file. If this argument is not used, <code>certutil</code> prompts for a filename.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Delete a certificate from the certificate database.</dl>
<p> &#8211;rename</p>
<dl>
<dt>
<dd> Change the database nickname of a certificate.</dl>
<p> -E</p>
<dl>
<dt>
<dd> Add an email certificate to the certificate database.</dl>
<p> -F</p>
<dl>
<dt>
<dd> Delete a private key from a key database. Specify the key to delete with the -n argument. Specify the database from which to delete the key with the <code>-d</code> argument. Use the <code>-k</code> argument to specify explicitly whether to delete a DSA, RSA, or ECC key. If you don&#8217;t use the <code>-k</code> argument, the option looks for an RSA key matching the specified nickname. </p>
<p> When you delete keys, be sure to also remove any certificates associated with those keys from the certificate database, by using -D. Some smart cards do not let you remove a public key you have generated. In such a case, only the private key is deleted from the key pair. You can display the public key with the command certutil -K -h tokenname.</dl>
<p> -G</p>
<dl>
<dt>
<dd> Generate a new public and private key pair within a key database. The key database should already exist; if one is not present, this command option will initialize one by default. Some smart cards can store only one key pair. If you create a new key pair for such a card, the previous pair is overwritten.</dl>
<p> -H</p>
<dl>
<dt>
<dd> Display a list of the command options and arguments.</dl>
<p> -K</p>
<dl>
<dt>
<dd> List the key ID of keys in the key database. A key ID is the modulus of the RSA key or the publicValue of the DSA key. IDs are displayed in hexadecimal (&quot;0x&quot; is not shown).</dl>
<p> -L</p>
<dl>
<dt>
<dd> List all the certificates, or display information about a named certificate, in a certificate database. Use the -h tokenname argument to specify the certificate database on a particular hardware or software token.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Modify a certificate&#8217;s trust attributes using the values of the -t argument.</dl>
<p> -N</p>
<dl>
<dt>
<dd> Create new certificate and key databases.</dl>
<p> -O</p>
<dl>
<dt>
<dd> Print the certificate chain.</dl>
<p> -R</p>
<dl>
<dt>
<dd> Create a certificate request file that can be submitted to a Certificate Authority (CA) for processing into a finished certificate. Output defaults to standard out unless you use -o output-file argument. Use the -a argument to specify ASCII output.</dl>
<p> -S</p>
<dl>
<dt>
<dd> Create an individual certificate and add it to a certificate database.</dl>
<p> -T</p>
<dl>
<dt>
<dd> Reset the key database or token.</dl>
<p> -U</p>
<dl>
<dt>
<dd> List all available modules or print a single named module.</dl>
<p> -V</p>
<dl>
<dt>
<dd> Check the validity of a certificate and its attributes.</dl>
<p> -W</p>
<dl>
<dt>
<dd> Change the password to a key database.</dl>
<p> &#8211;merge</p>
<dl>
<dt>
<dd> Merge two databases into one.</dl>
<p> &#8211;upgrade-merge</p>
<dl>
<dt>
<dd> Upgrade an old database and merge it into a new database. This is used to migrate legacy NSS databases (cert8.db and key3.db) into the newer SQLite databases (cert9.db and key4.db).</dl>
<p> <code>Arguments</code> </p>
<p> Arguments modify a command option and are usually lower case, numbers, or symbols. </p>
<p> -a</p>
<dl>
<dt>
<dd> Use ASCII format or allow the use of ASCII format for input or output. This formatting follows RFC 1113. For certificate requests, ASCII output defaults to standard output unless redirected.</dl>
<p> -b validity-time</p>
<dl>
<dt>
<dd> Specify a time at which a certificate is required to be valid. Use when checking certificate validity with the <code>-V</code> option. The format of the <i>validity-time</i> argument is <i>YYMMDDHHMMSS[+HHMM|-HHMM|Z]</i>, which allows offsets to be set relative to the validity end time. Specifying seconds (<i>SS</i>) is optional. When specifying an explicit time, use a Z at the end of the term, <i>YYMMDDHHMMSSZ</i>, to close it. When specifying an offset time, use <i>YYMMDDHHMMSS+HHMM</i> or <i>YYMMDDHHMMSS-HHMM</i> for adding or subtracting time, respectively. </p>
<p> If this option is not used, the validity check defaults to the current system time.</dl>
<p> -c issuer</p>
<dl>
<dt>
<dd> Identify the certificate of the CA from which a new certificate will derive its authenticity. Use the exact nickname or alias of the CA certificate, or use the CA&#8217;s email address. Bracket the issuer string with quotation marks if it contains spaces.</dl>
<p> -d [prefix]directory</p>
<dl>
<dt>
<dd> Specify the database directory containing the certificate and key database files. </p>
<p> <code>certutil</code> supports two types of databases: the legacy security databases (cert8.db, key3.db, and secmod.db) and new SQLite databases (cert9.db, key4.db, and pkcs11.txt). </p>
<p> NSS recognizes the following prefixes: </p>
<dl>
<dt>
<dd> &bull; <code>sql:</code> requests the newer database</dl>
<dl>
<dt>
<dd> &bull; <code>dbm:</code> requests the legacy database</dl>
<p> If no prefix is specified the default type is retrieved from NSS_DEFAULT_DB_TYPE. If NSS_DEFAULT_DB_TYPE is not set then <code>dbm:</code> is the default.</dl>
<p> &#8211;dump-ext-val OID</p>
<dl>
<dt>
<dd> For single cert, print binary DER encoding of extension OID.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Check a certificate&#8217;s signature during the process of validating a certificate.</dl>
<p> &#8211;email email-address</p>
<dl>
<dt>
<dd> Specify the email address of a certificate to list. Used with the -L command option.</dl>
<p> &#8211;extGeneric OID:critical-flag:filename[,OID:critical-flag:filename]&#8230;</p>
<dl>
<dt>
<dd> Add one or multiple extensions that certutil cannot encode yet, by loading their encodings from external files. </p>
<dl>
<dt>
<dd> &bull; OID (example): 1.2.3.4</dl>
<dl>
<dt>
<dd> &bull; critical-flag: critical or not-critical</dl>
<dl>
<dt>
<dd> &bull; filename: full path to a file containing an encoded extension</dl>
</dl>
<p> -f password-file</p>
<dl>
<dt>
<dd> Specify a file that will automatically supply the password to include in a certificate or to access a certificate database. This is a plain-text file containing one password. Be sure to prevent unauthorized access to this file.</dl>
<p> -g keysize</p>
<dl>
<dt>
<dd> Set a key size to use when generating new public and private key pairs. The minimum is 512 bits and the maximum is 16384 bits. The default is 2048 bits. Any size between the minimum and maximum is allowed.</dl>
<p> -h tokenname</p>
<dl>
<dt>
<dd> Specify the name of a token to use or act on. If not specified the default token is the internal database slot.</dl>
<p> -i input_file</p>
<dl>
<dt>
<dd> Pass an input file to the command. Depending on the command option, an input file can be a specific certificate, a certificate request file, or a batch file of commands.</dl>
<p> -k key-type-or-id</p>
<dl>
<dt>
<dd> Specify the type or specific ID of a key. </p>
<p> The valid key type options are rsa, dsa, ec, or all. The default value is rsa. Specifying the type of key can avoid mistakes caused by duplicate nicknames. Giving a key type generates a new key pair; giving the ID of an existing key reuses that key pair (which is required to renew certificates).</dl>
<p> -l</p>
<dl>
<dt>
<dd> Display detailed information when validating a certificate with the -V option.</dl>
<p> -m serial-number</p>
<dl>
<dt>
<dd> Assign a unique serial number to a certificate being created. This operation should be performed by a CA. If no serial number is provided a default serial number is made from the current time. Serial numbers are limited to integers</dl>
<p> -n nickname</p>
<dl>
<dt>
<dd> Specify the nickname of a certificate or key to list, create, add to a database, modify, or validate. Bracket the nickname string with quotation marks if it contains spaces.</dl>
<p> -o output-file</p>
<dl>
<dt>
<dd> Specify the output file name for new certificates or binary certificate requests. Bracket the output-file string with quotation marks if it contains spaces. If this argument is not used the output destination defaults to standard output.</dl>
<p> -P dbPrefix</p>
<dl>
<dt>
<dd> Specify the prefix used on the certificate and key database file. This argument is provided to support legacy servers. Most applications do not use a database prefix.</dl>
<p> -p phone</p>
<dl>
<dt>
<dd> Specify a contact telephone number to include in new certificates or certificate requests. Bracket this string with quotation marks if it contains spaces.</dl>
<p> -q pqgfile or curve-name</p>
<dl>
<dt>
<dd> Read an alternate PQG value from the specified file when generating DSA key pairs. If this argument is not used, <code>certutil</code> generates its own PQG value. PQG files are created with a separate DSA utility. </p>
<p> Elliptic curve name is one of the ones from nistp256, nistp384, nistp521, curve25519. </p>
<p> If a token is available that supports more curves, the foolowing curves are supported as well: sect163k1, nistk163, sect163r1, sect163r2, nistb163, sect193r1, sect193r2, sect233k1, nistk233, sect233r1, nistb233, sect239k1, sect283k1, nistk283, sect283r1, nistb283, sect409k1, nistk409, sect409r1, nistb409, sect571k1, nistk571, sect571r1, nistb571, secp160k1, secp160r1, secp160r2, secp192k1, secp192r1, nistp192, secp224k1, secp224r1, nistp224, secp256k1, secp256r1, secp384r1, secp521r1, prime192v1, prime192v2, prime192v3, prime239v1, prime239v2, prime239v3, c2pnb163v1, c2pnb163v2, c2pnb163v3, c2pnb176v1, c2tnb191v1, c2tnb191v2, c2tnb191v3, c2pnb208w1, c2tnb239v1, c2tnb239v2, c2tnb239v3, c2pnb272w1, c2pnb304w1, c2tnb359w1, c2pnb368w1, c2tnb431r1, secp112r1, secp112r2, secp128r1, secp128r2, sect113r1, sect113r2, sect131r1, sect131r2</dl>
<p> -r</p>
<dl>
<dt>
<dd> Display a certificate&#8217;s binary DER encoding when listing information about that certificate with the -L option.</dl>
<p> -s subject</p>
<dl>
<dt>
<dd> Identify a particular certificate owner for new certificates or certificate requests. Bracket this string with quotation marks if it contains spaces. The subject identification format follows RFC #1485.</dl>
<p> -t trustargs</p>
<dl>
<dt>
<dd> Specify the trust attributes to modify in an existing certificate or to apply to a certificate when creating it or adding it to a database. There are three available trust categories for each certificate, expressed in the order <i>SSL, email, object signing</i> for each trust setting. In each category position, use none, any, or all of the attribute codes: </p>
<dl>
<dt>
<dd> &bull; <code>p</code> &#8211; Valid peer</dl>
<dl>
<dt>
<dd> &bull; <code>P</code> &#8211; Trusted peer (implies p)</dl>
<dl>
<dt>
<dd> &bull; <code>c</code> &#8211; Valid CA</dl>
<dl>
<dt>
<dd> &bull; <code>C</code> &#8211; Trusted CA (implies c)</dl>
<dl>
<dt>
<dd> &bull; <code>T</code> &#8211; trusted CA for client authentication (ssl server only)</dl>
<p> The attribute codes for the categories are separated by commas, and the entire set of attributes enclosed by quotation marks. For example: </p>
<p> <code>-t &quot;TC,C,T&quot;</code> </p>
<p> Use the -L option to see a list of the current certificates and trust attributes in a certificate database. </p>
<p> Note that the output of the -L option may include &quot;u&quot; flag, which means that there is a private key associated with the certificate. It is a dynamic flag and you cannot set it with certutil.</dl>
<p> -u certusage</p>
<dl>
<dt>
<dd> Specify a usage context to apply when validating a certificate with the -V option. </p>
<p> The contexts are the following: </p>
<dl>
<dt>
<dd> &bull; <code>C</code> (as an SSL client)</dl>
<dl>
<dt>
<dd> &bull; <code>V</code> (as an SSL server)</dl>
<dl>
<dt>
<dd> &bull; <code>L</code> (as an SSL CA)</dl>
<dl>
<dt>
<dd> &bull; <code>A</code> (as Any CA)</dl>
<dl>
<dt>
<dd> &bull; <code>Y</code> (Verify CA)</dl>
<dl>
<dt>
<dd> &bull; <code>S</code> (as an email signer)</dl>
<dl>
<dt>
<dd> &bull; <code>R</code> (as an email recipient)</dl>
<dl>
<dt>
<dd> &bull; <code>O</code> (as an OCSP status responder)</dl>
<dl>
<dt>
<dd> &bull; <code>J</code> (as an object signer)</dl>
</dl>
<p> -v valid-months</p>
<dl>
<dt>
<dd> Set the number of months a new certificate will be valid. The validity period begins at the current system time unless an offset is added or subtracted with the <code>-w</code> option. If this argument is not used, the default validity period is three months.</dl>
<p> -w offset-months</p>
<dl>
<dt>
<dd> Set an offset from the current system time, in months, for the beginning of a certificate&#8217;s validity period. Use when creating the certificate or adding it to a database. Express the offset in integers, using a minus sign (-) to indicate a negative offset. If this argument is not used, the validity period begins at the current system time. The length of the validity period is set with the -v argument.</dl>
<p> -X</p>
<dl>
<dt>
<dd> Force the key and certificate database to open in read-write mode. This is used with the <code>-U</code> and <code>-L</code> command options.</dl>
<p> -x</p>
<dl>
<dt>
<dd> Use <code>certutil</code> to generate the signature for a certificate being created or added to a database, rather than obtaining a signature from a separate CA.</dl>
<p> -y exp</p>
<dl>
<dt>
<dd> Set an alternate exponent value to use in generating a new RSA public key for the database, instead of the default value of 65537. The available alternate values are 3 and 17.</dl>
<p> -z noise-file</p>
<dl>
<dt>
<dd> Read a seed value from the specified file to generate a new private and public key pair. This argument makes it possible to use hardware-generated seed values or manually create a value from the keyboard. The minimum file size is 20 bytes.</dl>
<p> -Z hashAlg</p>
<dl>
<dt>
<dd> Specify the hash algorithm to use with the -C, -S or -R command options. Possible keywords: </p>
<dl>
<dt>
<dd> &bull; MD2</dl>
<dl>
<dt>
<dd> &bull; MD4</dl>
<dl>
<dt>
<dd> &bull; MD5</dl>
<dl>
<dt>
<dd> &bull; SHA1</dl>
<dl>
<dt>
<dd> &bull; SHA224</dl>
<dl>
<dt>
<dd> &bull; SHA256</dl>
<dl>
<dt>
<dd> &bull; SHA384</dl>
<dl>
<dt>
<dd> &bull; SHA512</dl>
</dl>
<p> -0 SSO_password</p>
<dl>
<dt>
<dd> Set a site security officer password on a token.</dl>
<p> -1 | &#8211;keyUsage keyword,keyword</p>
<dl>
<dt>
<dd> Set an X.509 V3 Certificate Type Extension in the certificate. There are several available keywords: </p>
<dl>
<dt>
<dd> &bull; digitalSignature</dl>
<dl>
<dt>
<dd> &bull; nonRepudiation</dl>
<dl>
<dt>
<dd> &bull; keyEncipherment</dl>
<dl>
<dt>
<dd> &bull; dataEncipherment</dl>
<dl>
<dt>
<dd> &bull; keyAgreement</dl>
<dl>
<dt>
<dd> &bull; certSigning</dl>
<dl>
<dt>
<dd> &bull; crlSigning</dl>
<dl>
<dt>
<dd> &bull; critical</dl>
</dl>
<p> -2</p>
<dl>
<dt>
<dd> Add a basic constraint extension to a certificate that is being created or added to a database. This extension supports the certificate chain verification process. <code>certutil</code> prompts for the certificate constraint extension to select. </p>
<p> X.509 certificate extensions are described in RFC 5280.</dl>
<p> -3</p>
<dl>
<dt>
<dd> Add an authority key ID extension to a certificate that is being created or added to a database. This extension supports the identification of a particular certificate, from among multiple certificates associated with one subject name, as the correct issuer of a certificate. The Certificate Database Tool will prompt you to select the authority key ID extension. </p>
<p> X.509 certificate extensions are described in RFC 5280.</dl>
<p> -4</p>
<dl>
<dt>
<dd> Add a CRL distribution point extension to a certificate that is being created or added to a database. This extension identifies the URL of a certificate&#8217;s associated certificate revocation list (CRL). <code>certutil</code> prompts for the URL. </p>
<p> X.509 certificate extensions are described in RFC 5280.</dl>
<p> -5 | &#8211;nsCertType keyword,keyword</p>
<dl>
<dt>
<dd> Add an X.509 V3 certificate type extension to a certificate that is being created or added to the database. There are several available keywords: </p>
<dl>
<dt>
<dd> &bull; sslClient</dl>
<dl>
<dt>
<dd> &bull; sslServer</dl>
<dl>
<dt>
<dd> &bull; smime</dl>
<dl>
<dt>
<dd> &bull; objectSigning</dl>
<dl>
<dt>
<dd> &bull; sslCA</dl>
<dl>
<dt>
<dd> &bull; smimeCA</dl>
<dl>
<dt>
<dd> &bull; objectSigningCA</dl>
<dl>
<dt>
<dd> &bull; critical</dl>
<p> X.509 certificate extensions are described in RFC 5280.</dl>
<p> -6 | &#8211;extKeyUsage keyword,keyword</p>
<dl>
<dt>
<dd> Add an extended key usage extension to a certificate that is being created or added to the database. Several keywords are available: </p>
<dl>
<dt>
<dd> &bull; serverAuth</dl>
<dl>
<dt>
<dd> &bull; clientAuth</dl>
<dl>
<dt>
<dd> &bull; codeSigning</dl>
<dl>
<dt>
<dd> &bull; emailProtection</dl>
<dl>
<dt>
<dd> &bull; timeStamp</dl>
<dl>
<dt>
<dd> &bull; ocspResponder</dl>
<dl>
<dt>
<dd> &bull; stepUp</dl>
<dl>
<dt>
<dd> &bull; msTrustListSign</dl>
<dl>
<dt>
<dd> &bull; critical</dl>
<p> X.509 certificate extensions are described in RFC 5280.</dl>
<p> -7 emailAddrs</p>
<dl>
<dt>
<dd> Add a comma-separated list of email addresses to the subject alternative name extension of a certificate or certificate request that is being created or added to the database. Subject alternative name extensions are described in Section 4.2.1.7 of RFC 3280.</dl>
<p> -8 dns-names</p>
<dl>
<dt>
<dd> Add a comma-separated list of DNS names to the subject alternative name extension of a certificate or certificate request that is being created or added to the database. Subject alternative name extensions are described in Section 4.2.1.7 of RFC 3280.</dl>
<p> &#8211;extAIA</p>
<dl>
<dt>
<dd> Add the Authority Information Access extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extSIA</p>
<dl>
<dt>
<dd> Add the Subject Information Access extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extCP</p>
<dl>
<dt>
<dd> Add the Certificate Policies extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extPM</p>
<dl>
<dt>
<dd> Add the Policy Mappings extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extPC</p>
<dl>
<dt>
<dd> Add the Policy Constraints extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extIA</p>
<dl>
<dt>
<dd> Add the Inhibit Any Policy Access extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extSKID</p>
<dl>
<dt>
<dd> Add the Subject Key ID extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extNC</p>
<dl>
<dt>
<dd> Add a Name Constraint extension to the certificate. X.509 certificate extensions are described in RFC 5280.</dl>
<p> &#8211;extSAN type:name[,type:name]&#8230;</p>
<dl>
<dt>
<dd> Create a Subject Alt Name extension with one or multiple names. </p>
<p> -type: directory, dn, dns, edi, ediparty, email, ip, ipaddr, other, registerid, rfc822, uri, x400, x400addr</dl>
<p> &#8211;empty-password</p>
<dl>
<dt>
<dd> Use empty password when creating new certificate database with -N.</dl>
<p> &#8211;keyAttrFlags attrflags</p>
<dl>
<dt>
<dd> PKCS #11 key Attributes. Comma separated list of key attribute flags, selected from the following list of choices: {token | session} {public | private} {sensitive | insensitive} {modifiable | unmodifiable} {extractable | unextractable}</dl>
<p> &#8211;keyOpFlagsOn opflags, &#8211;keyOpFlagsOff opflags</p>
<dl>
<dt>
<dd> PKCS #11 key Operation Flags. Comma separated list of one or more of the following: {token | session} {public | private} {sensitive | insensitive} {modifiable | unmodifiable} {extractable | unextractable}</dl>
<p> &#8211;new-n nickname</p>
<dl>
<dt>
<dd> A new nickname, used when renaming a certificate.</dl>
<p> &#8211;source-dir certdir</p>
<dl>
<dt>
<dd> Identify the certificate database directory to upgrade.</dl>
<p> &#8211;source-prefix certdir</p>
<dl>
<dt>
<dd> Give the prefix of the certificate and key databases to upgrade.</dl>
<p> &#8211;upgrade-id uniqueID</p>
<dl>
<dt>
<dd> Give the unique ID of the database to upgrade.</dl>
<p> &#8211;upgrade-token-name name</p>
<dl>
<dt>
<dd> Set the name of the token to use while it is being upgraded.</dl>
<p> -@ pwfile</p>
<dl>
<dt>
<dd> Give the name of a password file to use for the database being upgraded.</dl>
<h2>USAGE AND EXAMPLES</h2>
<p> Most of the command options in the examples listed here have more arguments available. The arguments included in these examples are the most common ones or are used to illustrate a specific scenario. Use the <code>-H</code> option to show the complete list of arguments for each command option. </p>
<p> <code>Creating New Security Databases</code> </p>
<p> Certificates, keys, and security modules related to managing certificates are stored in three related databases: </p>
<dl>
<dt>
<dd> &bull; cert8.db or cert9.db</dl>
<dl>
<dt>
<dd> &bull; key3.db or key4.db</dl>
<dl>
<dt>
<dd> &bull; secmod.db or pkcs11.txt</dl>
<p> These databases must be created before certificates or keys can be generated. </p>
<dl>
<dt>
<dd>
<pre>
certutil -N -d [sql:]directory
</pre>
</dl>
<p> <code>Creating a Certificate Request</code> </p>
<p> A certificate request contains most or all of the information that is used to generate the final certificate. This request is submitted separately to a certificate authority and is then approved by some mechanism (automatically or by human review). Once the request is approved, then the certificate is generated. </p>
<dl>
<dt>
<dd>
<pre><code>
$ certutil - R - k key - type - or -id[-q pqgfile | curve - name] - g key - size - s subject[-h tokenname] - d [sql:] directory[-p phone][-o output - file][-a]
</code></pre>
</dl>
<p> The <code>-R</code> command options requires four arguments: </p>
<dl>
<dt>
<dd> &bull; <code>-k</code> to specify either the key type to generate or, when renewing a certificate, the existing key pair to use</dl>
<dl>
<dt>
<dd> &bull; <code>-g</code> to set the keysize of the key to generate</dl>
<dl>
<dt>
<dd> &bull; <code>-s</code> to set the subject name of the certificate</dl>
<dl>
<dt>
<dd> &bull; <code>-d</code> to give the security database directory</dl>
<p> The new certificate request can be output in ASCII format (<code>-a</code>) or can be written to a specified file (<code>-o</code>). </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -R -k rsa -g 1024 -s &quot;CN=John Smith,O=Example Corp,L=Mountain View,ST=California,C=US&quot; -d sql:$HOME/nssdb -p 650-555-0123 -a -o cert.cer
Generating key.  This may take a few moments...
</pre>
</dl>
<p> <code>Creating a Certificate</code> </p>
<p> A valid certificate must be issued by a trusted CA. This can be done by specifying a CA certificate (<code>-c</code>) that is stored in the certificate database. If a CA key pair is not available, you can create a self-signed certificate using the <code>-x</code> argument with the <code>-S</code> command option. </p>
<dl>
<dt>
<dd>
$ certutil &#8211; S &#8211; k rsa | dsa | ec &#8211; n certname &#8211; s subject[-c issuer | -x] &#8211; t trustargs &#8211; d [sql:] directory[-m serial &#8211; number][-v valid &#8211; months][-w offset &#8211; months][-p phone][-1][-2][-3][-4][-5 keyword][-6 keyword][-7 emailAddress][-8 dns &#8211; names][&#8211;extAIA][&#8211;extSIA][&#8211;extCP][&#8211;extPM][&#8211;extPC][&#8211;extIA][&#8211;extSKID]
</dl>
<p> The series of numbers and <code>&#8211;ext*</code> options set certificate extensions that can be added to the certificate when it is generated by the CA. Interactive prompts will result. </p>
<p> For example, this creates a self-signed certificate: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -S -s &quot;CN=Example CA&quot; -n my-ca-cert -x -t &quot;C,C,C&quot; -1 -2 -5 -m 3650
</pre>
</dl>
<p> The interative prompts for key usage and whether any extensions are critical and responses have been ommitted for brevity. </p>
<p> From there, new certificates can reference the self-signed certificate: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -S -s &quot;CN=My Server Cert&quot; -n my-server-cert -c &quot;my-ca-cert&quot; -t &quot;,,&quot; -1 -5 -6 -8 -m 730
</pre>
</dl>
<p> <code>Generating a Certificate from a Certificate Request</code> </p>
<p> When a certificate request is created, a certificate can be generated by using the request and then referencing a certificate authority signing certificate (the <i>issuer</i> specified in the <code>-c</code> argument). The issuing certificate must be in the certificate database in the specified directory. </p>
<dl>
<dt>
<dd>
certutil &#8211; C &#8211; c issuer &#8211; i cert &#8211; request &#8211; file &#8211; o output &#8211; file[-m serial &#8211; number][-v valid &#8211; months][-w offset &#8211; months] &#8211; d [sql:] directory[-1][-2][-3][-4][-5 keyword][-6 keyword][-7 emailAddress][-8 dns &#8211; names]
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -C -c &quot;my-ca-cert&quot; -i /home/certs/cert.req -o cert.cer -m 010 -v 12 -w 1 -d sql:$HOME/nssdb -1 nonRepudiation,dataEncipherment -5 sslClient -6 clientAuth -7 jsmith [at] example.com
</pre>
</dl>
<p> <code>Listing Certificates</code> </p>
<p> The <code>-L</code> command option lists all of the certificates listed in the certificate database. The path to the directory (<code>-d</code>) is required. </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -L -d sql:/home/my/sharednssdb
Certificate Nickname                                         Trust Attributes
                                                             SSL,S/MIME,JAR/XPI
CA Administrator of Instance pki-ca1's Example Domain ID     u,u,u
TPS Administrator's Example Domain ID                        u,u,u
Google Internet Authority                                    ,,   
Certificate Authority - Example Domain                       CT,C,C
</pre>
</dl>
<p> Using additional arguments with <code>-L</code> can return and print the information for a single, specific certificate. For example, the <code>-n</code> argument passes the certificate name, while the <code>-a</code> argument prints the certificate in ASCII format: </p>
<dl>
<dt>
<dd>
$ certutil &#8211; L &#8211; d sql : $HOME / nssdb &#8211; a &#8211; n my &#8211; ca &#8211; cert&#8211; &#8212; -BEGIN CERTIFICATE&#8211; &#8212; -MIIB1DCCAT2gAwIBAgICDkIwDQYJKoZIhvcNAQEFBQAwFTETMBEGA1UEAxMKRXhh bXBsZSBDQTAeFw0xMzAzMTMxOTEwMjlaFw0xMzA2MTMxOTEwMjlaMBUxEzARBgNV BAMTCkV4YW1wbGUgQ0EwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAJ4Kzqvz JyBVgFqDXRYSyTBNw1DrxUU / 3GvWA / ngjAwHEv0Cul / 6sO / gsCvnABHiH6unns6x XRzPORlC2WY3gkk7vmlsLvYpyecNazAi / NAwVnU / 66HOsaoVFWE+gBQo99UrN2yk 0BiK / GMFlLm5dXQROgA9ZKKyFdI0LIXtf6SbAgMBAAGjMzAxMBEGCWCGSAGG + EIB AQQEAwIHADAMBgNVHRMEBTADAQH / MA4GA1UdDwEB / wQEAwICBDANBgkqhkiG9w0B AQUFAAOBgQA6chkzkACN281d1jKMrc + RHG2UMaQyxiteaLVZO + Ro1nnRUvseDf09 XKYFwPMJjWCihVku6bw / ihZfuMHhxK22Nue6inNQ6eDu7WmrqL8z3iUrQwxs + WiF ob2rb8XRVVJkzXdXxlk4uo3UtNvw8sAz7sWD71qxKaIHU5q49zijfg ==<br />
    &#8212; &#8212; -END CERTIFICATE&#8211; &#8212; &#8211;
</dl>
<p> For a human-readable display </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -L -d sql:$HOME/nssdb -n my-ca-cert
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 3650 (0xe42)
        Signature Algorithm: PKCS #1 SHA-1 With RSA Encryption
        Issuer: &quot;CN=Example CA&quot;
        Validity:
            Not Before: Wed Mar 13 19:10:29 2013
            Not After : Thu Jun 13 19:10:29 2013
        Subject: &quot;CN=Example CA&quot;
        Subject Public Key Info:
            Public Key Algorithm: PKCS #1 RSA Encryption
            RSA Public Key:
                Modulus:
                    9e:0a:ce:ab:f3:27:20:55:80:5a:83:5d:16:12:c9:30:
                    4d:c3:50:eb:c5:45:3f:dc:6b:d6:03:f9:e0:8c:0c:07:
                    12:fd:02:ba:5f:fa:b0:ef:e0:b0:2b:e7:00:11:e2:1f:
                    ab:a7:9e:ce:b1:5d:1c:cf:39:19:42:d9:66:37:82:49:
                    3b:be:69:6c:2e:f6:29:c9:e7:0d:6b:30:22:fc:d0:30:
                    56:75:3f:eb:a1:ce:b1:aa:15:15:61:3e:80:14:28:f7:
                    d5:2b:37:6c:a4:d0:18:8a:fc:63:05:94:b9:b9:75:74:
                    11:3a:00:3d:64:a2:b2:15:d2:34:2c:85:ed:7f:a4:9b
                Exponent: 65537 (0x10001)
        Signed Extensions:
            Name: Certificate Type
            Data: none
            Name: Certificate Basic Constraints
            Data: Is a CA with no maximum path length.
            Name: Certificate Key Usage
            Critical: True
            Usages: Certificate Signing
    Signature Algorithm: PKCS #1 SHA-1 With RSA Encryption
    Signature:
        3a:72:19:33:90:00:8d:db:cd:5d:d6:32:8c:ad:cf:91:
        1c:6d:94:31:a4:32:c6:2b:5e:68:b5:59:3b:e4:68:d6:
        79:d1:52:fb:1e:0d:fd:3d:5c:a6:05:c0:f3:09:8d:60:
        a2:85:59:2e:e9:bc:3f:8a:16:5f:b8:c1:e1:c4:ad:b6:
        36:e7:ba:8a:73:50:e9:e0:ee:ed:69:ab:a8:bf:33:de:
        25:2b:43:0c:6c:f9:68:85:a1:bd:ab:6f:c5:d1:55:52:
        64:cd:77:57:c6:59:38:ba:8d:d4:b4:db:f0:f2:c0:33:
        ee:c5:83:ef:5a:b1:29:a2:07:53:9a:b8:f7:38:a3:7e
    Fingerprint (MD5):
        86:D8:A5:8B:8A:26:BE:9E:17:A8:7B:66:10:6B:27:80
    Fingerprint (SHA1):
        48:78:09:EF:C5:D4:0C:BD:D2:64:45:59:EB:03:13:15:F7:A9:D6:F7
    Certificate Trust Flags:
        SSL Flags:
            Valid CA
            Trusted CA
            User
        Email Flags:
            Valid CA
            Trusted CA
            User
        Object Signing Flags:
            Valid CA
            Trusted CA
            User
</pre>
</dl>
<p> <code>Listing Keys</code> </p>
<p> Keys are the original material used to encrypt certificate data. The keys generated for certificates are stored separately, in the key database. </p>
<p> To list all keys in the database, use the <code>-K</code> command option and the (required) <code>-d</code> argument to give the path to the directory. </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -K -d sql:$HOME/nssdb
certutil: Checking token &quot;NSS Certificate DB&quot; in slot &quot;NSS User Private Key and Certificate Services                  &quot;
&lt; 0&gt; rsa      455a6673bde9375c2887ec8bf8016b3f9f35861d   Thawte Freemail Member's Thawte Consulting (Pty) Ltd. ID
&lt; 1&gt; rsa      40defeeb522ade11090eacebaaf1196a172127df   Example Domain Administrator Cert
&lt; 2&gt; rsa      1d0b06f44f6c03842f7d4f4a1dc78b3bcd1b85a5   John Smith user cert
</pre>
</dl>
<p> There are ways to narrow the keys listed in the search results: </p>
<dl>
<dt>
<dd> &bull; To return a specific key, use the <code>-n</code><i>name</i> argument with the name of the key.</dl>
<dl>
<dt>
<dd> &bull; If there are multiple security devices loaded, then the <code>-h</code><i>tokenname</i> argument can search a specific token or all tokens.</dl>
<dl>
<dt>
<dd> &bull; If there are multiple key types available, then the <code>-k</code><i>key-type</i> argument can search a specific type of key, like RSA, DSA, or ECC.</dl>
<p> <code>Listing Security Modules</code> </p>
<p> The devices that can be used to store certificates &#8212; both internal databases and external devices like smart cards &#8212; are recognized and used by loading security modules. The <code>-U</code> command option lists all of the security modules listed in the secmod.db database. The path to the directory (<code>-d</code>) is required. </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -U -d sql:/home/my/sharednssdb
    slot: NSS User Private Key and Certificate Services                  
   token: NSS Certificate DB
    slot: NSS Internal Cryptographic Services                            
   token: NSS Generic Crypto Services
</pre>
</dl>
<p> <code>Adding Certificates to the Database</code> </p>
<p> Existing certificates or certificate requests can be added manually to the certificate database, even if they were generated elsewhere. This uses the <code>-A</code> command option. </p>
<dl>
<dt>
<dd>
certutil &#8211; A &#8211; n certname &#8211; t trustargs &#8211; d [sql:] directory[-a][-i input &#8211; file]
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -A -n &quot;CN=My SSL Certificate&quot; -t &quot;,,&quot; -d sql:/home/my/sharednssdb -i /home/example-certs/cert.cer
</pre>
</dl>
<p> A related command option, <code>-E</code>, is used specifically to add email certificates to the certificate database. The <code>-E</code> command has the same arguments as the <code>-A</code> command. The trust arguments for certificates have the format <i>SSL,S/MIME,Code-signing</i>, so the middle trust settings relate most to email certificates (though the others can be set). For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -E -n &quot;CN=John Smith Email Cert&quot; -t &quot;,P,&quot; -d sql:/home/my/sharednssdb -i /home/example-certs/email.cer
</pre>
</dl>
<p> <code>Deleting Certificates to the Database</code> </p>
<p> Certificates can be deleted from a database using the <code>-D</code> option. The only required options are to give the security database directory and to identify the certificate nickname. </p>
<dl>
<dt>
<dd>
<pre>
certutil -D -d [sql:]directory -n &quot;nickname&quot;
</pre>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -D -d sql:/home/my/sharednssdb -n &quot;my-ssl-cert&quot;
</pre>
</dl>
<p> <code>Validating Certificates</code> </p>
<p> A certificate contains an expiration date in itself, and expired certificates are easily rejected. However, certificates can also be revoked before they hit their expiration date. Checking whether a certificate has been revoked requires validating the certificate. Validation can also be used to ensure that the certificate is only used for the purposes it was initially issued for. Validation is carried out by the <code>-V</code> command option. </p>
<dl>
<dt>
<dd>
certutil &#8211; V &#8211; n certificate &#8211; name[-b time][-e][-u cert &#8211; usage] &#8211; d [sql:] directory
</dl>
<p> For example, to validate an email certificate: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -V -n &quot;John Smith's Email Cert&quot; -e -u S,R -d sql:/home/my/sharednssdb
</pre>
</dl>
<p> <code>Modifying Certificate Trust Settings</code> </p>
<p> The trust settings (which relate to the operations that a certificate is allowed to be used for) can be changed after a certificate is created or added to the database. This is especially useful for CA certificates, but it can be performed for any type of certificate. </p>
<dl>
<dt>
<dd>
<pre>
certutil -M -n certificate-name -t trust-args -d [sql:]directory
</pre>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -M -n &quot;My CA Certificate&quot; -d sql:/home/my/sharednssdb -t &quot;CT,CT,CT&quot;
</pre>
</dl>
<p> <code>Printing the Certificate Chain</code> </p>
<p> Certificates can be issued in <i>chains</i> because every certificate authority itself has a certificate; when a CA issues a certificate, it essentially stamps that certificate with its own fingerprint. The <code>-O</code> prints the full chain of a certificate, going from the initial CA (the root CA) through ever intermediary CA to the actual certificate. For example, for an email certificate with two CAs in the chain: </p>
<dl>
<dt>
<dd>
$ certutil &#8211; d sql : / home / my / sharednssdb &#8211; O &#8211; n &#8220;jsmith [at] example.com&#8221;<br />
                                                       &#8220;Builtin Object Token:Thawte Personal Freemail CA&#8221;[E = personal &#8211; freemail[at] thawte.com, CN = Thawte Personal Freemail CA, OU = Certification Services Division, O = Thawte Consulting, L = Cape Town, ST = Western Cape, C = ZA] &#8220;Thawte Personal Freemail Issuing CA &#8211; Thawte Consulting&#8221;[CN = Thawte Personal Freemail Issuing CA, O = Thawte Consulting(Pty) Ltd., C = ZA] &#8220;(null)&#8221;[E = jsmith[at] example.com, CN = Thawte Freemail Member]
</dl>
<p> <code>Resetting a Token</code> </p>
<p> The device which stores certificates &#8212; both external hardware devices and internal software databases &#8212; can be blanked and reused. This operation is performed on the device which stores the data, not directly on the security databases, so the location must be referenced through the token name (<code>-h</code>) as well as any directory path. If there is no external token used, the default value is internal. </p>
<dl>
<dt>
<dd>
<pre>
certutil -T -d [sql:]directory -h token-name -0 security-officer-password
</pre>
</dl>
<p> Many networks have dedicated personnel who handle changes to security tokens (the security officer). This person must supply the password to access the specified token. For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -T -d sql:/home/my/sharednssdb -h nethsm -0 secret
</pre>
</dl>
<p> <code>Upgrading or Merging the Security Databases</code> </p>
<p> Many networks or applications may be using older BerkeleyDB versions of the certificate database (cert8.db). Databases can be upgraded to the new SQLite version of the database (cert9.db) using the <code>&#8211;upgrade-merge</code> command option or existing databases can be merged with the new cert9.db databases using the <code>&#8212;merge</code> command. </p>
<p> The <code>&#8211;upgrade-merge</code> command must give information about the original database and then use the standard arguments (like <code>-d</code>) to give the information about the new databases. The command also requires information that the tool uses for the process to upgrade and write over the original database. </p>
<dl>
<dt>
<dd>
certutil&#8211; upgrade &#8211; merge &#8211; d [sql:] directory[-P dbprefix]&#8211; source &#8211; dir directory&#8211; source &#8211; prefix dbprefix&#8211; upgrade &#8211; id id&#8211; upgrade &#8211; token &#8211; name name[-@password &#8211; file]
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
$ certutil&#8211; upgrade &#8211; merge &#8211; d sql : / home / my / sharednssdb&#8211; source &#8211; dir / opt / my &#8211; app / alias / &#8211;source &#8211; prefix serverapp &#8211; &#8211;upgrade &#8211; id 1 &#8211;upgrade &#8211; token &#8211; name internal
</dl>
<p> The <code>&#8211;merge</code> command only requires information about the location of the original database; since it doesn&#8217;t change the format of the database, it can write over information without performing interim step. </p>
<dl>
<dt>
<dd>
<pre><code>
certutil-- merge - d [sql:] directory[-P dbprefix]-- source - dir directory-- source - prefix dbprefix[-@password - file]
</code></pre>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil --merge -d sql:/home/my/sharednssdb --source-dir /opt/my-app/alias/ --source-prefix serverapp-
</pre>
</dl>
<p> <code>Running certutil Commands from a Batch File</code> </p>
<p> A series of commands can be run sequentially from a text file with the <code>-B</code> command option. The only argument for this specifies the input file. </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -B -i /path/to/batch-file
</pre>
</dl>
<h2>NSS DATABASE TYPES</h2>
<p> NSS originally used BerkeleyDB databases to store security information. The last versions of these <i>legacy</i> databases are: </p>
<dl>
<dt>
<dd> &bull; cert8.db for certificates</dl>
<dl>
<dt>
<dd> &bull; key3.db for keys</dl>
<dl>
<dt>
<dd> &bull; secmod.db for PKCS #11 module information</dl>
<p> BerkeleyDB has performance limitations, though, which prevent it from being easily used by multiple applications simultaneously. NSS has some flexibility that allows applications to use their own, independent database engine while keeping a shared database and working around the access issues. Still, NSS requires more flexibility to provide a truly shared security database. </p>
<p> In 2009, NSS introduced a new set of databases that are SQLite databases rather than BerkeleyDB. These new databases provide more accessibility and performance: </p>
<dl>
<dt>
<dd> &bull; cert9.db for certificates</dl>
<dl>
<dt>
<dd> &bull; key4.db for keys</dl>
<dl>
<dt>
<dd> &bull; pkcs11.txt, a listing of all of the PKCS #11 modules, contained in a new subdirectory in the security databases directory</dl>
<p> Because the SQLite databases are designed to be shared, these are the <i>shared</i> database type. The shared database type is preferred; the legacy format is included for backward compatibility. </p>
<p> By default, the tools (<code>certutil</code>, <code>pk12util</code>, <code>modutil</code>) assume that the given security databases follow the more common legacy type. Using the SQLite databases must be manually specified by using the <code>sql:</code> prefix with the given security directory. For example: </p>
<dl>
<dt>
<dd>
<pre>
$ certutil -L -d sql:/home/my/sharednssdb
</pre>
</dl>
<p> To set the shared database type as the default type for the tools, set the <code>NSS_DEFAULT_DB_TYPE</code> environment variable to <code>sql</code>: </p>
<dl>
<dt>
<dd>
<pre>
export NSS_DEFAULT_DB_TYPE=&quot;sql&quot;
</pre>
</dl>
<p> This line can be set added to the ~/.bashrc file to make the change permanent. </p>
<p> Most applications do not use the shared database by default, but they can be configured to use them. For example, this how-to article covers how to configure Firefox and Thunderbird to use the new shared NSS databases: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<p> For an engineering draft on the changes in the shared NSS databases, see the NSS project wiki: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
<h2>SEE ALSO</h2>
<p> pk12util (1) </p>
<p> modutil (1) </p>
<p> <code>certutil</code> has arguments or operations that use features defined in several IETF RFCs. </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="http://tools.ietf.org/html/rfc5280">http://tools.ietf.org/html/rfc5280</a></dl>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="http://tools.ietf.org/html/rfc1113">http://tools.ietf.org/html/rfc1113</a></dl>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="http://tools.ietf.org/html/rfc1485">http://tools.ietf.org/html/rfc1485</a></dl>
<p> The NSS wiki has information on the new database design and how to configure applications to use it. </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
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
