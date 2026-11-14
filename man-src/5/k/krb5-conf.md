---
title: "krb5-conf(5)"
name: "krb5-conf"
section: "5"
letter: "k"
url: "/docs/linux/man/5-krb5-conf/"
description: "krb5.conf – Kerberos configuration file"
---

<p>krb5.conf &#8211; Kerberos configuration file </p>
<p> The krb5.conf file contains Kerberos configuration information, including the locations of KDCs and admin servers for the Kerberos realms of interest, defaults for the current realm and for Kerberos applications, and mappings of hostnames onto Kerberos realms. Normally, you should install your krb5.conf file in the directory <code>/etc</code>. You can override the default location by setting the environment variable <code>KRB5_CONFIG</code>. Multiple colon-separated filenames may be specified in <code>KRB5_CONFIG</code>; all files which are present will be read. Starting in release 1.14, directory names can also be specified in <code>KRB5_CONFIG</code>; all files within the directory whose names consist solely of alphanumeric characters, dashes, or underscores will be read.</p>
<h2>Structure</h2>
<p>The krb5.conf file is set up in the style of a Windows INI file. Sections are headed by the section name, in square brackets. Each section may contain zero or more relations, of the form: </p>
<pre>foo = bar</pre>
<p>or: </p>
<pre>fubar = {
 foo = bar
 baz = quux
}</pre>
<p>Placing a &#8216;*&#8217; at the end of a line indicates that this is the <i>final</i> value for the tag. This means that neither the remainder of this configuration file nor any other configuration file will be checked for any other values for this tag. </p>
<p> For example, if you have the following lines: </p>
<pre>foo = bar*
foo = baz</pre>
<p>then the second value of <code>foo</code> (<code>baz</code>) would never be read. </p>
<p> The krb5.conf file can include other files using either of the following directives at the beginning of a line: </p>
<pre>include FILENAME
includedir DIRNAME</pre>
<p><i>FILENAME</i> or <i>DIRNAME</i> should be an absolute path. The named file or directory must exist and be readable. Including a directory includes all files within the directory whose names consist solely of alphanumeric characters, dashes, or underscores. Starting in release 1.15, files with names ending in &quot;.conf&quot; are also included. Included profile files are syntactically independent of their parents, so each included file must begin with a section header. </p>
<p> The krb5.conf file can specify that configuration should be obtained from a loadable module, rather than the file itself, using the following directive at the beginning of a line before any section headers: </p>
<pre>module MODULEPATH:RESIDUAL</pre>
<p><i>MODULEPATH</i> may be relative to the library path of the krb5 installation, or it may be an absolute path. <i>RESIDUAL</i> is provided to the module at initialization time. If krb5.conf uses a module directive, <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> should also use one if it exists.</p>
<h2>Sections</h2>
<p>The krb5.conf file may contain the following sections: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[libdefaults]</i> </td>
<td> Settings used by the Kerberos V5 library
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[realms]</i> </td>
<td> Realm-specific contact information and settings
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[domain_realm]</i> </td>
<td> Maps server hostnames to Kerberos realms
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[capaths]</i> </td>
<td> Authentication paths for non-hierarchical cross-realm
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[appdefaults]</i> </td>
<td> Settings used by some Kerberos V5 applications
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[plugins]</i> </td>
<td> Controls plugin module registration
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Additionally, krb5.conf may include any of the relations described in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>, but it is not a recommended practice.</p>
<h3>[libdefaults]</h3>
<p>The libdefaults section may contain any of the following relations:</p>
<dl>
<dt><code>allow_weak_crypto</code></p>
<dd>If this flag is set to false, then weak encryption types (as noted in <i>Encryption_types</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>) will be filtered out of the lists <code>default_tgs_enctypes</code>, <code>default_tkt_enctypes</code>, and <code>permitted_enctypes</code>. The default value for this tag is false, which may cause authentication failures in existing Kerberos infrastructures that do not support strong crypto. Users in affected environments should set this tag to true until their infrastructure adopts stronger ciphers.</p>
<dt><code>ap_req_checksum_type</code></p>
<dd>An integer which specifies the type of AP-REQ checksum to use in authenticators. This variable should be unset so the appropriate checksum for the encryption key in use will be used. This can be set if backward compatibility requires a specific checksum type. See the <code>kdc_req_checksum_type</code> configuration option for the possible values and their meanings.</p>
<dt><code>canonicalize</code></p>
<dd>If this flag is set to true, initial ticket requests to the KDC will request canonicalization of the client principal name, and answers with different client principals than the requested principal will be accepted. The default value is false.</p>
<dt><code>ccache_type</code></p>
<dd>This parameter determines the format of credential cache types created by <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i> or other programs. The default value is 4, which represents the most current format. Smaller values can be used for compatibility with very old implementations of Kerberos which interact with credential caches on the same host.</p>
<dt><code>clockskew</code></p>
<dd>Sets the maximum allowable amount of clockskew in seconds that the library will tolerate before assuming that a Kerberos message is invalid. The default value is 300 seconds, or five minutes. </p>
<p> The clockskew setting is also used when evaluating ticket start and expiration times. For example, tickets that have reached their expiration time can still be used (and renewed if they are renewable tickets) if they have been expired for a shorter duration than the <code>clockskew</code> setting.</p>
<dt><code>default_ccache_name</code></p>
<dd>This relation specifies the name of the default credential cache. The default is <code>FILE:/tmp/krb5cc_%{uid}</code>. This relation is subject to parameter expansion (see below). New in release 1.11.</p>
<dt><code>default_client_keytab_name</code></p>
<dd>This relation specifies the name of the default keytab for obtaining client credentials. The default is <code>FILE:/var/kerberos/krb5/user/%{euid}/client.keytab</code>. This relation is subject to parameter expansion (see below). New in release 1.11.</p>
<dt><code>default_keytab_name</code></p>
<dd>This relation specifies the default keytab name to be used by application servers such as sshd. The default is <code>FILE:/etc/krb5.keytab</code>. This relation is subject to parameter expansion (see below).</p>
<dt><code>default_realm</code></p>
<dd>Identifies the default Kerberos realm for the client. Set its value to your Kerberos realm. If this value is not set, then a realm must be specified with every Kerberos principal when invoking programs such as <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i>.</p>
<dt><code>default_tgs_enctypes</code></p>
<dd>Identifies the supported list of session key encryption types that the client should request when making a TGS-REQ, in order of preference from highest to lowest. The list may be delimited with commas or whitespace. See <i>Encryption_types</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of the accepted values for this tag. The default value is <code>aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1 arcfour-hmac-md5 camellia256-cts-cmac camellia128-cts-cmac des-cbc-crc des-cbc-md5 des-cbc-md4</code>, but single-DES encryption types will be implicitly removed from this list if the value of <code>allow_weak_crypto</code> is false. </p>
<p> Do not set this unless required for specific backward compatibility purposes; stale values of this setting can prevent clients from taking advantage of new stronger enctypes when the libraries are upgraded.</p>
<dt><code>default_tkt_enctypes</code></p>
<dd>Identifies the supported list of session key encryption types that the client should request when making an AS-REQ, in order of preference from highest to lowest. The format is the same as for default_tgs_enctypes. The default value for this tag is <code>aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1 arcfour-hmac-md5 camellia256-cts-cmac camellia128-cts-cmac des-cbc-crc des-cbc-md5 des-cbc-md4</code>, but single-DES encryption types will be implicitly removed from this list if the value of <code>allow_weak_crypto</code> is false. </p>
<p> Do not set this unless required for specific backward compatibility purposes; stale values of this setting can prevent clients from taking advantage of new stronger enctypes when the libraries are upgraded.</p>
<dt><code>dns_canonicalize_hostname</code></p>
<dd>Indicate whether name lookups will be used to canonicalize hostnames for use in service principal names. Setting this flag to false can improve security by reducing reliance on DNS, but means that short hostnames will not be canonicalized to fully-qualified hostnames. The default value is true.</p>
<dt><code>dns_lookup_kdc</code></p>
<dd>Indicate whether DNS SRV records should be used to locate the KDCs and other servers for a realm, if they are not listed in the krb5.conf information for the realm. (Note that the admin_server entry must be in the krb5.conf realm information in order to contact kadmind, because the DNS implementation for kadmin is incomplete.) </p>
<p> Enabling this option does open up a type of denial-of-service attack, if someone spoofs the DNS records and redirects you to another server. However, it&#8217;s no worse than a denial of service, because that fake KDC will be unable to decode anything you send it (besides the initial ticket request, which has no encrypted data), and anything the fake KDC sends will not be trusted without verification using some secret that it won&#8217;t know.</p>
<dt><code>dns_uri_lookup</code></p>
<dd>Indicate whether DNS URI records should be used to locate the KDCs and other servers for a realm, if they are not listed in the krb5.conf information for the realm. SRV records are used as a fallback if no URI records were found. The default value is true. New in release 1.15.</p>
<dt><code>err_fmt</code></p>
<dd>This relation allows for custom error message formatting. If a value is set, error messages will be formatted by substituting a normal error message for %M and an error code for %C in the value.</p>
<dt><code>extra_addresses</code></p>
<dd>This allows a computer to use multiple local addresses, in order to allow Kerberos to work in a network that uses NATs while still using address-restricted tickets. The addresses should be in a comma-separated list. This option has no effect if <code>noaddresses</code> is true.</p>
<dt><code>forwardable</code></p>
<dd>If this flag is true, initial tickets will be forwardable by default, if allowed by the KDC. The default value is false.</p>
<dt><code>ignore_acceptor_hostname</code></p>
<dd>When accepting GSSAPI or krb5 security contexts for host-based service principals, ignore any hostname passed by the calling application, and allow clients to authenticate to any service principal in the keytab matching the service name and realm name (if given). This option can improve the administrative flexibility of server applications on multihomed hosts, but could compromise the security of virtual hosting environments. The default value is false. New in release 1.10.</p>
<dt><code>k5login_authoritative</code></p>
<dd>If this flag is true, principals must be listed in a local user&#8217;s k5login file to be granted login access, if a <i><a href="/docs/linux/man/5--k5login/">.k5login</a>(5)</i> file exists. If this flag is false, a principal may still be granted login access through other mechanisms even if a k5login file exists but does not list the principal. The default value is true.</p>
<dt><code>k5login_directory</code></p>
<dd>If set, the library will look for a local user&#8217;s k5login file within the named directory, with a filename corresponding to the local username. If not set, the library will look for k5login files in the user&#8217;s home directory, with the filename .k5login. For security reasons, .k5login files must be owned by the local user or by root.</p>
<dt><code>kcm_mach_service</code></p>
<dd>On OS X only, determines the name of the bootstrap service used to contact the KCM daemon for the KCM credential cache type. If the value is <code>&#8211;</code>, Mach RPC will not be used to contact the KCM daemon. The default value is <code>org.h5l.kcm</code>.</p>
<dt><code>kcm_socket</code></p>
<dd>Determines the path to the Unix domain socket used to access the KCM daemon for the KCM credential cache type. If the value is <code>&#8211;</code>, Unix domain sockets will not be used to contact the KCM daemon. The default value is <code>/var/run/.heim_org.h5l.kcm-socket</code>.</p>
<dt><code>kdc_default_options</code></p>
<dd>Default KDC options (Xored for multiple values) when requesting initial tickets. By default it is set to 0x00000010 (KDC_OPT_RENEWABLE_OK).</p>
<dt><code>kdc_timesync</code></p>
<dd>Accepted values for this relation are 1 or 0. If it is nonzero, client machines will compute the difference between their time and the time returned by the KDC in the timestamps in the tickets and use this value to correct for an inaccurate system clock when requesting service tickets or authenticating to services. This corrective factor is only used by the Kerberos library; it is not used to change the system clock. The default value is 1.</p>
<dt><code>kdc_req_checksum_type</code></p>
<dd>An integer which specifies the type of checksum to use for the KDC requests, for compatibility with very old KDC implementations. This value is only used for DES keys; other keys use the preferred checksum type for those keys. </p>
<p> The possible values and their meanings are as follows. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> CRC32
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> RSA MD4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> RSA MD4 DES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 4 </td>
<td> DES CBC
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 7 </td>
<td> RSA MD5
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 8 </td>
<td> RSA MD5 DES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 9 </td>
<td> NIST SHA
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 12 </td>
<td> HMAC SHA1 DES3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -138 </td>
<td> Microsoft MD5 HMAC checksum type
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>noaddresses</code></p>
<dd>If this flag is true, requests for initial tickets will not be made with address restrictions set, allowing the tickets to be used across NATs. The default value is true.</p>
<dt><code>permitted_enctypes</code></p>
<dd>Identifies all encryption types that are permitted for use in session key encryption. The default value for this tag is <code>aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1 arcfour-hmac-md5 camellia256-cts-cmac camellia128-cts-cmac des-cbc-crc des-cbc-md5 des-cbc-md4</code>, but single-DES encryption types will be implicitly removed from this list if the value of <code>allow_weak_crypto</code> is false.</p>
<dt><code>plugin_base_dir</code></p>
<dd>If set, determines the base directory where krb5 plugins are located. The default value is the <code>krb5/plugins</code> subdirectory of the krb5 library directory.</p>
<dt><code>preferred_preauth_types</code></p>
<dd>This allows you to set the preferred preauthentication types which the client will attempt before others which may be advertised by a KDC. The default value for this setting is &quot;17, 16, 15, 14&quot;, which forces libkrb5 to attempt to use PKINIT if it is supported.</p>
<dt><code>proxiable</code></p>
<dd>If this flag is true, initial tickets will be proxiable by default, if allowed by the KDC. The default value is false.</p>
<dt><code>rdns</code></p>
<dd>If this flag is true, reverse name lookup will be used in addition to forward name lookup to canonicalizing hostnames for use in service principal names. If <code>dns_canonicalize_hostname</code> is set to false, this flag has no effect. The default value is true.</p>
<dt><code>realm_try_domains</code></p>
<dd>Indicate whether a host&#8217;s domain components should be used to determine the Kerberos realm of the host. The value of this variable is an integer: -1 means not to search, 0 means to try the host&#8217;s domain itself, 1 means to also try the domain&#8217;s immediate parent, and so forth. The library&#8217;s usual mechanism for locating Kerberos realms is used to determine whether a domain is a valid realm, which may involve consulting DNS if <code>dns_lookup_kdc</code> is set. The default is not to search domain components.</p>
<dt><code>renew_lifetime</code></p>
<dd>(<i>duration</i> string.) Sets the default renewable lifetime for initial ticket requests. The default value is 0.</p>
<dt><code>safe_checksum_type</code></p>
<dd>An integer which specifies the type of checksum to use for the KRB-SAFE requests. By default it is set to 8 (RSA MD5 DES). For compatibility with applications linked against DCE version 1.1 or earlier Kerberos libraries, use a value of 3 to use the RSA MD4 DES instead. This field is ignored when its value is incompatible with the session key type. See the <code>kdc_req_checksum_type</code> configuration option for the possible values and their meanings.</p>
<dt><code>ticket_lifetime</code></p>
<dd>(<i>duration</i> string.) Sets the default lifetime for initial ticket requests. The default value is 1 day.</p>
<dt><code>udp_preference_limit</code></p>
<dd>When sending a message to the KDC, the library will try using TCP before UDP if the size of the message is above <code>udp_preference_limit</code>. If the message is smaller than <code>udp_preference_limit</code>, then UDP will be tried before TCP. Regardless of the size, both protocols will be tried if the first attempt fails.</p>
<dt><code>verify_ap_req_nofail</code></p>
<dd>If this flag is true, then an attempt to verify initial credentials will fail if the client machine does not have a keytab. The default value is false.</dl>
<h3>[realms]</h3>
<p>Each tag in the [realms] section of the file is the name of a Kerberos realm. The value of the tag is a subsection with relations that define the properties of that particular realm. For each realm, the following tags may be specified in the realm&#8217;s subsection:</p>
<dl>
<dt><code>admin_server</code></p>
<dd>Identifies the host where the administration server is running. Typically, this is the master Kerberos server. This tag must be given a value in order to communicate with the <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> server for the realm.</p>
<dt><code>auth_to_local</code></p>
<dd>This tag allows you to set a general rule for mapping principal names to local user names. It will be used if there is not an explicit mapping for the principal name that is being translated. The possible values are:</p>
<dt><code>RULE:</code><i>exp</i></p>
<dd>The local name will be formulated from <i>exp</i>. </p>
<p> The format for <i>exp</i> is <code>[</code><i>n</i><code>:</code><i>string</i><code>](</code><i>regexp</i><code>)s/</code><i>pattern</i><code>/</code><i>replacement</i><code>/g</code>. The integer <i>n</i> indicates how many components the target principal should have. If this matches, then a string will be formed from <i>string</i>, substituting the realm of the principal for <code>$0</code> and the <i>n</i>&#8216;th component of the principal for <code>$n</code> (e.g., if the principal was <code>johndoe/admin</code> then <code>[2:$2$1foo]</code> would result in the string <code>adminjohndoefoo</code>). If this string matches <i>regexp</i>, then the <code>s//[g]</code> substitution command will be run over the string. The optional <code>g</code> will cause the substitution to be global over the <i>string</i>, instead of replacing only the first match in the <i>string</i>.</p>
<dt><code>DEFAULT</code></p>
<dd>The principal name will be used as the local user name. If the principal has more than one component or is not in the default realm, this rule is not applicable and the conversion will fail. </p>
<p> For example: </p>
<pre>[realms]
 ATHENA.MIT.EDU = {
 auth_to_local = RULE:[2:$1](johndoe)s/^.*$/guest/
 auth_to_local = RULE:[2:$1;$2](^.*;admin$)s/;admin$//
 auth_to_local = RULE:[2:$2](^.*;root)s/^.*$/root/
 auto_to_local = DEFAULT
 }</pre>
<p>would result in any principal without <code>root</code> or <code>admin</code> as the second component to be translated with the default rule. A principal with a second component of <code>admin</code> will become its first component. <code>root</code> will be used as the local name for any principal with a second component of <code>root</code>. The exception to these two rules are any principals <code>johndoe/*</code>, which will always get the local name <code>guest</code>.</p>
<dt><code>auth_to_local_names</code></p>
<dd>This subsection allows you to set explicit mappings from principal names to local user names. The tag is the mapping name, and the value is the corresponding local user name.</p>
<dt><code>default_domain</code></p>
<dd>This tag specifies the domain used to expand hostnames when translating Kerberos 4 service principals to Kerberos 5 principals (for example, when converting <code>rcmd.hostname</code> to <code>host/hostname.domain</code>).</p>
<dt><code>http_anchors</code></p>
<dd>When KDCs and kpasswd servers are accessed through HTTPS proxies, this tag can be used to specify the location of the CA certificate which should be trusted to issue the certificate for a proxy server. If left unspecified, the system-wide default set of CA certificates is used. </p>
<p> The syntax for values is similar to that of values for the <code>pkinit_anchors</code> tag: </p>
<p> <code>FILE:</code> <i>filename</i> </p>
<p> <i>filename</i> is assumed to be the name of an OpenSSL-style ca-bundle file. </p>
<p> <code>DIR:</code> <i>dirname</i> </p>
<p> <i>dirname</i> is assumed to be an directory which contains CA certificates. All files in the directory will be examined; if they contain certificates (in PEM format), they will be used. </p>
<p> <code>ENV:</code> <i>envvar</i> </p>
<p> <i>envvar</i> specifies the name of an environment variable which has been set to a value conforming to one of the previous values. For example, <code>ENV:X509_PROXY_CA</code>, where environment variable <code>X509_PROXY_CA</code> has been set to <code>FILE:/tmp/my_proxy.pem</code>.</p>
<dt><code>kdc</code></p>
<dd>The name or address of a host running a KDC for that realm. An optional port number, separated from the hostname by a colon, may be included. If the name or address contains colons (for example, if it is an IPv6 address), enclose it in square brackets to distinguish the colon from a port separator. For your computer to be able to communicate with the KDC for each realm, this tag must be given a value in each realm subsection in the configuration file, or there must be DNS SRV records specifying the KDCs.</p>
<dt><code>kpasswd_server</code></p>
<dd>Points to the server where all the password changes are performed. If there is no such entry, the port 464 on the <code>admin_server</code> host will be tried.</p>
<dt><code>master_kdc</code></p>
<dd>Identifies the master KDC(s). Currently, this tag is used in only one case: If an attempt to get credentials fails because of an invalid password, the client software will attempt to contact the master KDC, in case the user&#8217;s password has just been changed, and the updated database has not been propagated to the slave servers yet.</p>
<dt><code>v4_instance_convert</code></p>
<dd>This subsection allows the administrator to configure exceptions to the <code>default_domain</code> mapping rule. It contains V4 instances (the tag name) which should be translated to some specific hostname (the tag value) as the second component in a Kerberos V5 principal name.</p>
<dt><code>v4_realm</code></p>
<dd>This relation is used by the krb524 library routines when converting a V5 principal name to a V4 principal name. It is used when the V4 realm name and the V5 realm name are not the same, but still share the same principal names and passwords. The tag value is the Kerberos V4 realm name.</dl>
<h3>[domain_realm]</h3>
<p>The [domain_realm] section provides a translation from a domain name or hostname to a Kerberos realm name. The tag name can be a host name or domain name, where domain names are indicated by a prefix of a period (<code>.</code>). The value of the relation is the Kerberos realm name for that particular host or domain. A host name relation implicitly provides the corresponding domain name relation, unless an explicit domain name relation is provided. The Kerberos realm may be identified either in the <i>realms</i> section or using DNS SRV records. Host names and domain names should be in lower case. For example: </p>
<pre>[domain_realm]
 crash.mit.edu = TEST.ATHENA.MIT.EDU
 .dev.mit.edu = TEST.ATHENA.MIT.EDU
 mit.edu = ATHENA.MIT.EDU</pre>
<p>maps the host with the name <code>crash.mit.edu</code> into the <code>TEST.ATHENA.MIT.EDU</code> realm. The second entry maps all hosts under the domain <code>dev.mit.edu</code> into the <code>TEST.ATHENA.MIT.EDU</code> realm, but not the host with the name <code>dev.mit.edu</code>. That host is matched by the third entry, which maps the host <code>mit.edu</code> and all hosts under the domain <code>mit.edu</code> that do not match a preceding rule into the realm <code>ATHENA.MIT.EDU</code>. </p>
<p> If no translation entry applies to a hostname used for a service principal for a service ticket request, the library will try to get a referral to the appropriate realm from the client realm&#8217;s KDC. If that does not succeed, the host&#8217;s realm is considered to be the hostname&#8217;s domain portion converted to uppercase, unless the <code>realm_try_domains</code> setting in [libdefaults] causes a different parent domain to be used.</p>
<h3>[capaths]</h3>
<p>In order to perform direct (non-hierarchical) cross-realm authentication, configuration is needed to determine the authentication paths between realms. </p>
<p> A client will use this section to find the authentication path between its realm and the realm of the server. The server will use this section to verify the authentication path used by the client, by checking the transited field of the received ticket. </p>
<p> There is a tag for each participating client realm, and each tag has subtags for each of the server realms. The value of the subtags is an intermediate realm which may participate in the cross-realm authentication. The subtags may be repeated if there is more then one intermediate realm. A value of &quot;.&quot; means that the two realms share keys directly, and no intermediate realms should be allowed to participate. </p>
<p> Only those entries which will be needed on the client or the server need to be present. A client needs a tag for its local realm with subtags for all the realms of servers it will need to authenticate to. A server needs a tag for each realm of the clients it will serve, with a subtag of the server realm. </p>
<p> For example, <code>ANL.GOV</code>, <code>PNL.GOV</code>, and <code>NERSC.GOV</code> all wish to use the <code>ES.NET</code> realm as an intermediate realm. ANL has a sub realm of <code>TEST.ANL.GOV</code> which will authenticate with <code>NERSC.GOV</code> but not <code>PNL.GOV</code>. The [capaths] section for <code>ANL.GOV</code> systems would look like this: </p>
<pre>[capaths]
 ANL.GOV = {
 TEST.ANL.GOV = .
 PNL.GOV = ES.NET
 NERSC.GOV = ES.NET
 ES.NET = .
 }
 TEST.ANL.GOV = {
 ANL.GOV = .
 }
 PNL.GOV = {
 ANL.GOV = ES.NET
 }
 NERSC.GOV = {
 ANL.GOV = ES.NET
 }
 ES.NET = {
 ANL.GOV = .
 }</pre>
<p>The [capaths] section of the configuration file used on <code>NERSC.GOV</code> systems would look like this: </p>
<pre>[capaths]
 NERSC.GOV = {
 ANL.GOV = ES.NET
 TEST.ANL.GOV = ES.NET
 TEST.ANL.GOV = ANL.GOV
 PNL.GOV = ES.NET
 ES.NET = .
 }
 ANL.GOV = {
 NERSC.GOV = ES.NET
 }
 PNL.GOV = {
 NERSC.GOV = ES.NET
 }
 ES.NET = {
 NERSC.GOV = .
 }
 TEST.ANL.GOV = {
 NERSC.GOV = ANL.GOV
 NERSC.GOV = ES.NET
 }</pre>
<p>When a subtag is used more than once within a tag, clients will use the order of values to determine the path. The order of values is not important to servers.</p>
<h3>[appdefaults]</h3>
<p>Each tag in the [appdefaults] section names a Kerberos V5 application or an option that is used by some Kerberos V5 application[s]. The value of the tag defines the default behaviors for that application. </p>
<p> For example: </p>
<pre>[appdefaults]
 telnet = {
 ATHENA.MIT.EDU = {
 option1 = false
 }
 }
 telnet = {
 option1 = true
 option2 = true
 }
 ATHENA.MIT.EDU = {
 option2 = false
 }
 option2 = true</pre>
<p>The above four ways of specifying the value of an option are shown in order of decreasing precedence. In this example, if telnet is running in the realm EXAMPLE.COM, it should, by default, have option1 and option2 set to true. However, a telnet program in the realm <code>ATHENA.MIT.EDU</code> should have <code>option1</code> set to false and <code>option2</code> set to true. Any other programs in ATHENA.MIT.EDU should have <code>option2</code> set to false by default. Any programs running in other realms should have <code>option2</code> set to true. </p>
<p> The list of specifiable options for each application may be found in that application&#8217;s man pages. The application defaults specified here are overridden by those specified in the <i>realms</i> section.</p>
<h3>[plugins]</h3>
<dl>
<dt>&bull;</p>
<dd><i>pwqual</i> interface</p>
<dt>&bull;</p>
<dd><i>kadm5_hook</i> interface</p>
<dt>&bull;</p>
<dd><i>clpreauth</i> and <i>kdcpreauth</i> interfaces </p>
<p> Tags in the [plugins] section can be used to register dynamic plugin modules and to turn modules on and off. Not every krb5 pluggable interface uses the [plugins] section; the ones that do are documented here. </p>
<p> New in release 1.9. </p>
<p> Each pluggable interface corresponds to a subsection of [plugins]. All subsections support the same tags:</p>
<dt><code>disable</code></p>
<dd>This tag may have multiple values. If there are values for this tag, then the named modules will be disabled for the pluggable interface.</p>
<dt><code>enable_only</code></p>
<dd>This tag may have multiple values. If there are values for this tag, then only the named modules will be enabled for the pluggable interface.</p>
<dt><code>module</code></p>
<dd>This tag may have multiple values. Each value is a string of the form <code>modulename:pathname</code>, which causes the shared object located at <i>pathname</i> to be registered as a dynamic module named <i>modulename</i> for the pluggable interface. If <i>pathname</i> is not an absolute path, it will be treated as relative to the <code>plugin_base_dir</code> value from <i>[libdefaults]</i>. </p>
<p> For pluggable interfaces where module order matters, modules registered with a <code>module</code> tag normally come first, in the order they are registered, followed by built-in modules in the order they are documented below. If <code>enable_only</code> tags are used, then the order of those tags overrides the normal module order. </p>
<p> The following subsections are currently supported within the [plugins] section:</dl>
<h3>ccselect interface</h3>
<p>The ccselect subsection controls modules for credential cache selection within a cache collection. In addition to any registered dynamic modules, the following built-in modules exist (and may be disabled with the disable tag):</p>
<dl>
<dt><code>k5identity</code></p>
<dd>Uses a .k5identity file in the user&#8217;s home directory to select a client principal</p>
<dt><code>realm</code></p>
<dd>Uses the service realm to guess an appropriate cache from the collection</dl>
<h3>pwqual interface</h3>
<p>The pwqual subsection controls modules for the password quality interface, which is used to reject weak passwords when passwords are changed. The following built-in modules exist for this interface:</p>
<dl>
<dt><code>dict</code></p>
<dd>Checks against the realm dictionary file</p>
<dt><code>empty</code></p>
<dd>Rejects empty passwords</p>
<dt><code>hesiod</code></p>
<dd>Checks against user information stored in Hesiod (only if Kerberos was built with Hesiod support)</p>
<dt><code>princ</code></p>
<dd>Checks against components of the principal name</dl>
<h3>kadm5_hook interface</h3>
<p>The kadm5_hook interface provides plugins with information on principal creation, modification, password changes and deletion. This interface can be used to write a plugin to synchronize MIT Kerberos with another database such as Active Directory. No plugins are built in for this interface.</p>
<h3>clpreauth and kdcpreauth interfaces</h3>
<p>The clpreauth and kdcpreauth interfaces allow plugin modules to provide client and KDC preauthentication mechanisms. The following built-in modules exist for these interfaces:</p>
<dl>
<dt><code>pkinit</code></p>
<dd>This module implements the PKINIT preauthentication mechanism.</p>
<dt><code>encrypted_challenge</code></p>
<dd>This module implements the encrypted challenge FAST factor.</p>
<dt><code>encrypted_timestamp</code></p>
<dd>This module implements the encrypted timestamp mechanism.</dl>
<h3>hostrealm interface</h3>
<p>The hostrealm section (introduced in release 1.12) controls modules for the host-to-realm interface, which affects the local mapping of hostnames to realm names and the choice of default realm. The following built-in modules exist for this interface:</p>
<dl>
<dt><code>profile</code></p>
<dd>This module consults the [domain_realm] section of the profile for authoritative host-to-realm mappings, and the <code>default_realm</code> variable for the default realm.</p>
<dt><code>dns</code></p>
<dd>This module looks for DNS records for fallback host-to-realm mappings and the default realm. It only operates if the <code>dns_lookup_realm</code> variable is set to true.</p>
<dt><code>domain</code></p>
<dd>This module applies heuristics for fallback host-to-realm mappings. It implements the <code>realm_try_domains</code> variable, and uses the uppercased parent domain of the hostname if that does not produce a result.</dl>
<h3>localauth interface</h3>
<p>The localauth section (introduced in release 1.12) controls modules for the local authorization interface, which affects the relationship between Kerberos principals and local system accounts. The following built-in modules exist for this interface:</p>
<dl>
<dt><code>default</code></p>
<dd>This module implements the <code>DEFAULT</code> type for <code>auth_to_local</code> values.</p>
<dt><code>rule</code></p>
<dd>This module implements the <code>RULE</code> type for <code>auth_to_local</code> values.</p>
<dt><code>names</code></p>
<dd>This module looks for an <code>auth_to_local_names</code> mapping for the principal name.</p>
<dt><code>auth_to_local</code></p>
<dd>This module processes <code>auth_to_local</code> values in the default realm&#8217;s section, and applies the default method if no <code>auth_to_local</code> values exist.</p>
<dt><code>k5login</code></p>
<dd>This module authorizes a principal to a local account according to the account&#8217;s <i><a href="/docs/linux/man/5--k5login/">.k5login</a>(5)</i> file.</p>
<dt><code>an2ln</code></p>
<dd>This module authorizes a principal to a local account if the principal name maps to the local account name.</dl>
<h3>certauth interface</h3>
<p>The certauth section (introduced in release 1.16) controls modules for the certificate authorization interface, which determines whether a certificate is allowed to preauthenticate a user via PKINIT. The following built-in modules exist for this interface:</p>
<dl>
<dt><code>pkinit_san</code></p>
<dd>This module authorizes the certificate if it contains a PKINIT Subject Alternative Name for the requested client principal, or a Microsoft UPN SAN matching the principal if <code>pkinit_allow_upn</code> is set to true for the realm.</p>
<dt><code>pkinit_eku</code></p>
<dd>This module rejects the certificate if it does not contain an Extended Key Usage attribute consistent with the <code>pkinit_eku_checking</code> value for the realm.</dl>
<h2>Pkinit Options</h2>
<p><code>NOTE:</code> The following are PKINIT-specific options. These values may be specified in [libdefaults] as global defaults, or within a realm-specific subsection of [libdefaults], or may be specified as realm-specific values in the [realms] section. A realm-specific value overrides, not adds to, a generic [libdefaults] specification. The search order is:</p>
<dl>
<dt>1.</p>
<dd>realm-specific subsection of [libdefaults]: </p>
<pre>[libdefaults]
 EXAMPLE.COM = {
 pkinit_anchors = FILE:/usr/local/example.com.crt
 }</pre>
<dt>2.</p>
<dd>realm-specific value in the [realms] section: </p>
<pre>[realms]
 OTHERREALM.ORG = {
 pkinit_anchors = FILE:/usr/local/otherrealm.org.crt
 }</pre>
<dt>3.</p>
<dd>generic value in the [libdefaults] section: </p>
<pre>[libdefaults]
 pkinit_anchors = DIR:/usr/local/generic_trusted_cas/</pre>
</dl>
<h3>Specifying PKINIT identity information</h3>
<p>The syntax for specifying Public Key identity, trust, and revocation information for PKINIT is as follows:</p>
<dl>
<dt><code>FILE:</code><i>filename</i>[<code>,</code><i>keyfilename</i>]</p>
<dd>This option has context-specific behavior. </p>
<p> In <code>pkinit_identity</code> or <code>pkinit_identities</code>, <i>filename</i> specifies the name of a PEM-format file containing the user&#8217;s certificate. If <i>keyfilename</i> is not specified, the user&#8217;s private key is expected to be in <i>filename</i> as well. Otherwise, <i>keyfilename</i> is the name of the file containing the private key. </p>
<p> In <code>pkinit_anchors</code> or <code>pkinit_pool</code>, <i>filename</i> is assumed to be the name of an OpenSSL-style ca-bundle file.</p>
<dt><code>DIR:</code><i>dirname</i></p>
<dd>This option has context-specific behavior. </p>
<p> In <code>pkinit_identity</code> or <code>pkinit_identities</code>, <i>dirname</i> specifies a directory with files named <code>*.crt</code> and <code>*.key</code> where the first part of the file name is the same for matching pairs of certificate and private key files. When a file with a name ending with <code>.crt</code> is found, a matching file ending with <code>.key</code> is assumed to contain the private key. If no such file is found, then the certificate in the <code>.crt</code> is not used. </p>
<p> In <code>pkinit_anchors</code> or <code>pkinit_pool</code>, <i>dirname</i> is assumed to be an OpenSSL-style hashed CA directory where each CA cert is stored in a file named <code>hash-of-ca-cert.#</code>. This infrastructure is encouraged, but all files in the directory will be examined and if they contain certificates (in PEM format), they will be used. </p>
<p> In <code>pkinit_revoke</code>, <i>dirname</i> is assumed to be an OpenSSL-style hashed CA directory where each revocation list is stored in a file named <code>hash-of-ca-cert.r#</code>. This infrastructure is encouraged, but all files in the directory will be examined and if they contain a revocation list (in PEM format), they will be used.</p>
<dt><code>PKCS12:</code><i>filename</i></p>
<dd><i>filename</i> is the name of a PKCS #12 format file, containing the user&#8217;s certificate and private key.</p>
<dt><code>PKCS11:</code>[<code>module_name=</code>]<i>modname</i>[<code>:slotid=</code><i>slot-id</i>][<code>:token=</code><i>token-label</i>][<code>:certid=</code><i>cert-id</i>][<code>:certlabel=</code><i>cert-label</i>]</p>
<dd>All keyword/values are optional. <i>modname</i> specifies the location of a library implementing PKCS #11. If a value is encountered with no keyword, it is assumed to be the <i>modname</i>. If no module-name is specified, the default is <code>opensc-pkcs11.so</code>. <code>slotid=</code> and/or <code>token=</code> may be specified to force the use of a particular smard card reader or token if there is more than one available. <code>certid=</code> and/or <code>certlabel=</code> may be specified to force the selection of a particular certificate on the device. See the <code>pkinit_cert_match</code> configuration option for more ways to select a particular certificate to use for PKINIT.</p>
<dt><code>ENV:</code><i>envvar</i></p>
<dd><i>envvar</i> specifies the name of an environment variable which has been set to a value conforming to one of the previous values. For example, <code>ENV:X509_PROXY</code>, where environment variable <code>X509_PROXY</code> has been set to <code>FILE:/tmp/my_proxy.pem</code>.</dl>
<h3>PKINIT krb5.conf options</h3>
<dl>
<dt><code>pkinit_anchors</code></p>
<dd>Specifies the location of trusted anchor (root) certificates which the client trusts to sign KDC certificates. This option may be specified multiple times. These values from the config file are not used if the user specifies X509_anchors on the command line.</p>
<dt><code>pkinit_cert_match</code></p>
<dd>Specifies matching rules that the client certificate must match before it is used to attempt PKINIT authentication. If a user has multiple certificates available (on a smart card, or via other media), there must be exactly one certificate chosen before attempting PKINIT authentication. This option may be specified multiple times. All the available certificates are checked against each rule in order until there is a match of exactly one certificate. </p>
<p> The Subject and Issuer comparison strings are the <i>RFC 2253</i> string representations from the certificate Subject DN and Issuer DN values. </p>
<p> The syntax of the matching rules is: [<i>relation-operator</i>]<i>component-rule</i> &#8230; </p>
<p> where:</p>
<dt><i>relation-operator</i></p>
<dd>can be either <code>&amp;&amp;</code>, meaning all component rules must match, or <code>||</code>, meaning only one component rule must match. The default is <code>&amp;&amp;</code>.</p>
<dt><i>component-rule</i></p>
<dd>can be one of the following. Note that there is no punctuation or whitespace between component rules. </p>
<pre><code>&lt;SUBJECT&gt;</code><i>regular-expression</i>
<code>&lt;ISSUER&gt;</code><i>regular-expression</i>
<code>&lt;SAN&gt;</code><i>regular-expression</i>
<code>&lt;EKU&gt;</code><i>extended-key-usage-list</i>
<code>&lt;KU&gt;</code><i>key-usage-list</i></pre>
<p><i>extended-key-usage-list</i> is a comma-separated list of required Extended Key Usage values. All values in the list must be present in the certificate. Extended Key Usage values can be:</p>
<dt>&bull;</p>
<dd>pkinit</p>
<dt>&bull;</p>
<dd>msScLogin</p>
<dt>&bull;</p>
<dd>clientAuth</p>
<dt>&bull;</p>
<dd>emailProtection </p>
<p> <i>key-usage-list</i> is a comma-separated list of required Key Usage values. All values in the list must be present in the certificate. Key Usage values can be:</p>
<dt>&bull;</p>
<dd>digitalSignature</p>
<dt>&bull;</p>
<dd>keyEncipherment </p>
<p> Examples: </p>
<pre>pkinit_cert_match = ||&lt;SUBJECT&gt;.*DoE.*&lt;SAN&gt;.*@EXAMPLE.COM
pkinit_cert_match = &amp;&amp;&lt;EKU&gt;msScLogin,clientAuth&lt;ISSUER&gt;.*DoE.*
pkinit_cert_match = &lt;EKU&gt;msScLogin,clientAuth&lt;KU&gt;digitalSignature</pre>
<dt><code>pkinit_eku_checking</code></p>
<dd>This option specifies what Extended Key Usage value the KDC certificate presented to the client must contain. (Note that if the KDC certificate has the pkinit SubjectAlternativeName encoded as the Kerberos TGS name, EKU checking is not necessary since the issuing CA has certified this as a KDC certificate.) The values recognized in the krb5.conf file are:</p>
<dt><code>kpKDC</code></p>
<dd>This is the default value and specifies that the KDC must have the id-pkinit-KPKdc EKU as defined in <i>RFC 4556</i>.</p>
<dt><code>kpServerAuth</code></p>
<dd>If <code>kpServerAuth</code> is specified, a KDC certificate with the id-kp-serverAuth EKU will be accepted. This key usage value is used in most commercially issued server certificates.</p>
<dt><code>none</code></p>
<dd>If <code>none</code> is specified, then the KDC certificate will not be checked to verify it has an acceptable EKU. The use of this option is not recommended.</p>
<dt><code>pkinit_dh_min_bits</code></p>
<dd>Specifies the size of the Diffie-Hellman key the client will attempt to use. The acceptable values are 1024, 2048, and 4096. The default is 2048.</p>
<dt><code>pkinit_identities</code></p>
<dd>Specifies the location(s) to be used to find the user&#8217;s X.509 identity information. This option may be specified multiple times. Each value is attempted in order until identity information is found and authentication is attempted. Note that these values are not used if the user specifies <code>X509_user_identity</code> on the command line.</p>
<dt><code>pkinit_kdc_hostname</code></p>
<dd>The presense of this option indicates that the client is willing to accept a KDC certificate with a dNSName SAN (Subject Alternative Name) rather than requiring the id-pkinit-san as defined in <i>RFC 4556</i>. This option may be specified multiple times. Its value should contain the acceptable hostname for the KDC (as contained in its certificate).</p>
<dt><code>pkinit_pool</code></p>
<dd>Specifies the location of intermediate certificates which may be used by the client to complete the trust chain between a KDC certificate and a trusted anchor. This option may be specified multiple times.</p>
<dt><code>pkinit_require_crl_checking</code></p>
<dd>The default certificate verification process will always check the available revocation information to see if a certificate has been revoked. If a match is found for the certificate in a CRL, verification fails. If the certificate being verified is not listed in a CRL, or there is no CRL present for its issuing CA, and <code>pkinit_require_crl_checking</code> is false, then verification succeeds. </p>
<p> However, if <code>pkinit_require_crl_checking</code> is true and there is no CRL information available for the issuing CA, then verification fails. </p>
<p> <code>pkinit_require_crl_checking</code> should be set to true if the policy is such that up-to-date CRLs must be present for every CA.</p>
<dt><code>pkinit_revoke</code></p>
<dd>Specifies the location of Certificate Revocation List (CRL) information to be used by the client when verifying the validity of the KDC certificate presented. This option may be specified multiple times.</dl>
<h2>Parameter Expansion</h2>
<p>Starting with release 1.11, several variables, such as <code>default_keytab_name</code>, allow parameters to be expanded. Valid parameters are: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{TEMP} </td>
<td> Temporary directory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{uid} </td>
<td> Unix real UID or Windows SID
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{euid} </td>
<td> Unix effective user ID or Windows SID
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{USERID} </td>
<td> Same as %{uid}
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{null} </td>
<td> Empty string
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{LIBDIR} </td>
<td> Installation library directory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{BINDIR} </td>
<td> Installation binary directory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{SBINDIR} </td>
<td> Installation admin binary directory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{username} </td>
<td> (Unix) Username of effective user ID
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{APPDATA} </td>
<td> (Windows) Roaming application data for current user
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{COMMON_APPDATA} </td>
<td> (Windows) Application data for all users
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{LOCAL_APPDATA} </td>
<td> (Windows) Local application data for current user
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{SYSTEM} </td>
<td> (Windows) Windows system folder
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{WINDOWS} </td>
<td> (Windows) Windows folder
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{USERCONFIG} </td>
<td> (Windows) Per-user MIT krb5 config file directory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{COMMONCONFIG} </td>
<td> (Windows) Common MIT krb5 config file directory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>Sample Krb5.Conf File</h2>
<p>Here is an example of a generic krb5.conf file: </p>
<pre>[libdefaults]
 default_realm = ATHENA.MIT.EDU
 dns_lookup_kdc = true
 dns_lookup_realm = false
[realms]
 ATHENA.MIT.EDU = {
 kdc = kerberos.mit.edu
 kdc = kerberos-1.mit.edu
 kdc = kerberos-2.mit.edu
 admin_server = kerberos.mit.edu
 master_kdc = kerberos.mit.edu
 }
 EXAMPLE.COM = {
 kdc = kerberos.example.com
 kdc = kerberos-1.example.com
 admin_server = kerberos.example.com
 }
[domain_realm]
 mit.edu = ATHENA.MIT.EDU
[capaths]
 ATHENA.MIT.EDU = {
 EXAMPLE.COM = .
 }
 EXAMPLE.COM = {
 ATHENA.MIT.EDU = .
 }</pre>
<h2>Files</h2>
<p><code>/etc/krb5.conf</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2017, MIT</p>
