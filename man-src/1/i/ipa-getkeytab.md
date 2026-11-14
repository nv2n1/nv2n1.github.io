---
title: "ipa-getkeytab(1)"
name: "ipa-getkeytab"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-getkeytab/"
description: "ipa-getkeytab – Get a keytab for a Kerberos principal"
---

<h2>NAME</h2>
<p> ipa-getkeytab &#8211; Get a keytab for a Kerberos principal</p>
<h2>SYNOPSIS</h2>
<p> ipa-getkeytab <code>-p</code> <i>principal-name</i> <code>-k</code> <i>keytab-file</i> [ <code>-e</code> <i>encryption-types</i> ] [ <code>-s</code> <i>ipaserver</i> ] [ <code>-q</code> ] [ <code>-D</code>|<code>&#8211;binddn</code> <i>BINDDN</i> ] [ <code>-w|&#8211;bindpw</code> ] [ <code>-P</code>|<code>&#8211;password</code> <i>PASSWORD</i> ] [ <code>&#8211;cacert </code><i>CACERT</i> ] [ <code>-H|&#8211;ldapuri </code><i>URI</i> ] [ <code>-Y|&#8211;mech </code><i>GSSAPI|EXTERNAL</i> ] [ <code>-r</code> ] </p>
<h2>DESCRIPTION</h2>
<p> Retrieves a Kerberos <i>keytab</i>. </p>
<p> Kerberos keytabs are used for services (like sshd) to perform Kerberos authentication. A keytab is a file with one or more secrets (or keys) for a Kerberos principal. </p>
<p> A Kerberos service principal is a Kerberos identity that can be used for authentication. Service principals contain the name of the service, the hostname of the server, and the realm name. For example, the following is an example principal for an ldap server: </p>
<p>ldap/foo.example.com [at] EXAMPLE.COM </p>
<p> When using ipa-getkeytab the realm name is already provided, so the principal name is just the service name and hostname (ldap/foo.example.com from the example above). </p>
<p> <code>WARNING:</code> retrieving the keytab resets the secret for the Kerberos principal. This renders all other keytabs for that principal invalid. </p>
<p> This is used during IPA client enrollment to retrieve a host service principal and store it in /etc/krb5.keytab. It is possible to retrieve the keytab without Kerberos credentials if the host was pre-created with a one-time password. The keytab can be retrieved by binding as the host and authenticating with this one-time password. The <code>-D|&#8211;binddn</code> and <code>-w|&#8211;bindpw</code> options are used for this authentication.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p principal-name</code></p>
<dd> The non-realm part of the full principal name.</p>
<dt><code>-k keytab-file</code></p>
<dd> The keytab file where to append the new key (will be created if it does not exist).</p>
<dt><code>-e encryption-types</code></p>
<dd> The list of encryption types to use to generate keys. ipa-getkeytab will use local client defaults if not provided. Valid values depend on the Kerberos library version and configuration. Common values are: aes256-cts aes128-cts des3-hmac-sha1 arcfour-hmac des-hmac-sha1 des-cbc-md5 des-cbc-crc</p>
<dt><code>-s ipaserver</code></p>
<dd> The IPA server to retrieve the keytab from (FQDN). If this option is not provided the server name is read from the IPA configuration file (/etc/ipa/default.conf). Cannot be used together with <code>-H</code>.</p>
<dt><code>-q</code></p>
<dd> Quiet mode. Only errors are displayed.</p>
<dt><code>&#8211;permitted-enctypes</code></p>
<dd> This options returns a description of the permitted encryption types, like this: Supported encryption types: AES-256 CTS mode with 96-bit SHA-1 HMAC AES-128 CTS mode with 96-bit SHA-1 HMAC Triple DES cbc mode with HMAC/sha1 ArcFour with HMAC/md5 DES cbc mode with CRC-32 DES cbc mode with RSA-MD5 DES cbc mode with RSA-MD4</p>
<dt><code>-P, &#8211;password</code></p>
<dd> Use this password for the key instead of one randomly generated.</p>
<dt><code>-D, &#8211;binddn</code></p>
<dd> The LDAP DN to bind as when retrieving a keytab without Kerberos credentials. Generally used with the <code>-w</code> option.</p>
<dt><code>-w, &#8211;bindpw</code></p>
<dd> The LDAP password to use when not binding with Kerberos. <code>-D</code> and <code>-w</code> can not be used together with <code>-Y</code>.</p>
<dt><code>&#8211;cacert</code></p>
<dd> The path to the IPA CA certificate used to validate LDAPS/STARTTLS connections. Defaults to /etc/ipa/ca.crt</p>
<dt><code>-H, &#8211;ldapuri</code></p>
<dd> LDAP URI. If ldap:// is specified, STARTTLS is initiated by default. Can not be used with <code>-s</code>.</p>
<dt><code>-Y, &#8211;mech</code></p>
<dd> SASL mechanism to use if <code>-D</code> and <code>-w</code> are not specified. Use either GSSAPI or EXTERNAL.</p>
<dt><code>-r</code></p>
<dd> Retrieve mode. Retrieve an existing key from the server instead of generating a new one. This is incompatibile with the &#8211;password option, and will work only against a IPA server more recent than version 3.3. The user requesting the keytab must have access to the keys for this operation to succeed.</dl>
<h2>EXAMPLES</h2>
<p> Add and retrieve a keytab for the NFS service principal on the host foo.example.com and save it in the file /tmp/nfs.keytab and retrieve just the des-cbc-crc key. </p>
<p>#&nbsp;<wbr>ipa-getkeytab -p nfs/foo.example.com -k&nbsp;<wbr>/tmp/nfs.keytab -e des-cbc-crc </p>
<p> Add and retrieve a keytab for the ldap service principal on the host foo.example.com and save it in the file /tmp/ldap.keytab. </p>
<p>#&nbsp;<wbr>ipa-getkeytab -s ipaserver.example.com -p ldap/foo.example.com -k&nbsp;<wbr>/tmp/ldap.keytab </p>
<p> Retrieve a keytab using LDAP credentials (this will typically be done by <code><a href="/docs/linux/man/1-ipa-join/">ipa-join</a>(1)</code> when enrolling a client using the <code><a href="/docs/linux/man/1-ipa-client-install/">ipa-client-install</a>(1)</code> command: </p>
<p>#&nbsp;<wbr>ipa-getkeytab -s ipaserver.example.com -p host/foo.example.com -k&nbsp;<wbr>/etc/krb5.keytab -D fqdn=foo.example.com,cn=computers,cn=accounts,dc=example,dc=com -w password</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<p> 0 Success </p>
<p> 1 Kerberos context initialization failed </p>
<p> 2 Incorrect usage </p>
<p> 3 Out of memory </p>
<p> 4 Invalid service principal name </p>
<p> 5 No Kerberos credentials cache </p>
<p> 6 No Kerberos principal and no bind DN and password </p>
<p> 7 Failed to open keytab </p>
<p> 8 Failed to create key material </p>
<p> 9 Setting keytab failed </p>
<p> 10 Bind password required when using a bind DN </p>
<p> 11 Failed to add key to keytab </p>
<p> 12 Failed to close keytab </p>
<h2>Index</h2>
