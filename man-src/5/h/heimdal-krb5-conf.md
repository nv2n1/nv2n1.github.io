---
title: "heimdal-krb5-conf(5)"
name: "heimdal-krb5-conf"
section: "5"
letter: "h"
url: "/docs/linux/man/5-heimdal-krb5-conf/"
description: "krb5.conf – configuration file for Kerberos 5"
---

<p><code>krb5.conf</code> &#8211; configuration file for Kerberos 5</p>
<h2>Synopsis</h2>
<p>In krb5.h</p>
<h2>Description</h2>
<p>The file specifies several configuration parameters for the Kerberos 5 library, as well as for some programs. The file consists of one or more sections, containing a number of bindings. The value of each binding can be either a string or a list of other bindings. The grammar looks like: </p>
<blockquote>
<pre>file:
 /* empty */
 sections
sections:
 section sections
 section
section:
 '[' section_name ']' bindings
section_name:
 STRING
bindings:
 binding bindings
 binding
binding:
 name '=' STRING
 name '=' '{' bindings '}'
name:
 STRING</pre>
</blockquote>
<p> <code>STRINGs </code>consists of one or more non-whitespace characters. STRINGs that are specified later in this man-page uses the following notation.</p>
<dl>
<dt><code>boolean</code></dt>
<dd>values can be either yes/true or no/false.</dd>
<dt><code>time</code></dt>
<dd>values can be a list of year, month, day, hour, min, second. Example: 1 month 2 days 30 min. If no unit is given, seconds is assumed.</dd>
<dt><code>etypes</code></dt>
<dd>valid encryption types are: des-cbc-crc, des-cbc-md4, des-cbc-md5, des3-cbc-sha1, arcfour-hmac-md5, aes128-cts-hmac-sha1-96, and aes256-cts-hmac-sha1-96 .</dd>
<dt><code>address</code></dt>
<dd>an address can be either a IPv4 or a IPv6 address.</dd></dl>
<p> Currently recognised sections and bindings are:</p>
<dl>
<dt><code>[appdefaults]</code></dt>
<dd>Specifies the default values to be used for Kerberos applications. You can specify defaults per application, realm, or a combination of these. The preference order is: </dd>
<ol>
<li> <i>application realm option</i>
<li> <i>application option</i>
<li> <i>realm option</i>
<li> <i>option</i> </ol>
<p> The supported options are:</p>
<dl>
<dt><code>forwardable = </code><i>boolean</i></dt>
<dd>When obtaining initial credentials, make the credentials forwardable.</dd>
<dt><code>proxiable = </code><i>boolean</i></dt>
<dd>When obtaining initial credentials, make the credentials proxiable.</dd>
<dt><code>no-addresses = </code><i>boolean</i></dt>
<dd>When obtaining initial credentials, request them for an empty set of addresses, making the tickets valid from any address.</dd>
<dt><code>ticket_lifetime = </code><i>time</i></dt>
<dd>Default ticket lifetime.</dd>
<dt><code>renew_lifetime = </code><i>time</i></dt>
<dd>Default renewable ticket lifetime.</dd>
<dt><code>encrypt = </code><i>boolean</i></dt>
<dd>Use encryption, when available.</dd>
<dt><code>forward = </code><i>boolean</i></dt>
<dd>Forward credentials to remote host (for <a href="/docs/linux/man/1-rsh/">rsh</a>(1), <a href="/docs/linux/man/1-telnet/">telnet</a>(1), etc).</dd></dl>
<dt><code>[libdefaults]</code></dt>
<dd>
</dd><dl>
<dt><code>default_realm = </code><i>REALM</i></dt>
<dd>Default realm to use, this is also known as your &#8220;local realm&#8221; The default is the result of Fn krb5_get_host_realm local hostname .</dd>
<dt><code>allow_weak_crypto = </code><i>boolean</i></dt>
<dd>is weaks crypto algorithms allowed to be used, among others, DES is considered weak.</dd>
<dt><code>clockskew = </code><i>time</i></dt>
<dd>Maximum time differential (in seconds) allowed when comparing times. Default is 300 seconds (five minutes).</dd>
<dt><code>kdc_timeout = </code><i>time</i></dt>
<dd>Maximum time to wait for a reply from the kdc, default is 3 seconds.</dd>
<dt><code>v4_name_convert</code></dt>
<dd>
</dd><dt><code>v4_instance_resolve</code></dt>
<dd>These are described in the krb5_425_conv_principal3 manual page.</dd>
<dt><code>capath</code></dt>
<dd>
</dd><dl>
<pre><code>destination-realm = next-hop-realm
...
}</code></pre>
<p> This is deprecated, see the <code>capaths</code> section below.</p>
<dt><code>default_cc_type = </code><i>cctype</i></dt>
<dd>sets the default credentials type.</dd>
<dt><code>default_cc_name = </code><i>ccname</i></dt>
<dd>the default credentials cache name. If you want to change the type only use <code>default_cc_type</code> The string can contain variables that are expanded on runtime. Only support variable now is <code>%{uid}</code> that expands to the current user id.</dd>
<dt><code>default_etypes = </code><i>etypes &#8230;</i></dt>
<dd>A list of default encryption types to use. (Default: all enctypes if allow_weak_crypto = TRUE, else all enctypes except single DES enctypes.)</dd>
<dt><code>default_as_etypes = </code><i>etypes &#8230;</i></dt>
<dd>A list of default encryption types to use in AS requests. (Default: the value of default_etypes.)</dd>
<dt><code>default_tgs_etypes = </code><i>etypes &#8230;</i></dt>
<dd>A list of default encryption types to use in TGS requests. (Default: the value of default_etypes.)</dd>
<dt><code>default_etypes_des = </code><i>etypes &#8230;</i></dt>
<dd>A list of default encryption types to use when requesting a DES credential.</dd>
<dt><code>default_keytab_name = </code><i>keytab</i></dt>
<dd>The keytab to use if no other is specified, default is &#8220;FILE:/etc/krb5.keytab&#8221;</dd>
<dt><code>dns_lookup_kdc = </code><i>boolean</i></dt>
<dd>Use DNS SRV records to lookup KDC services location.</dd>
<dt><code>dns_lookup_realm = </code><i>boolean</i></dt>
<dd>Use DNS TXT records to lookup domain to realm mappings.</dd>
<dt><code>kdc_timesync = </code><i>boolean</i></dt>
<dd>Try to keep track of the time differential between the local machine and the KDC, and then compensate for that when issuing requests.</dd>
<dt><code>max_retries = </code><i>number</i></dt>
<dd>The max number of times to try to contact each KDC.</dd>
<dt><code>large_msg_size = </code><i>number</i></dt>
<dd>The threshold where protocols with tiny maximum message sizes are not considered usable to send messages to the KDC.</dd>
<dt><code>ticket_lifetime = </code><i>time</i></dt>
<dd>Default ticket lifetime.</dd>
<dt><code>renew_lifetime = </code><i>time</i></dt>
<dd>Default renewable ticket lifetime.</dd>
<dt><code>forwardable = </code><i>boolean</i></dt>
<dd>When obtaining initial credentials, make the credentials forwardable. This option is also valid in the [realms] section.</dd>
<dt><code>proxiable = </code><i>boolean</i></dt>
<dd>When obtaining initial credentials, make the credentials proxiable. This option is also valid in the [realms] section.</dd>
<dt><code>verify_ap_req_nofail = </code><i>boolean</i></dt>
<dd>If enabled, failure to verify credentials against a local key is a fatal error. The application has to be able to read the corresponding service key for this to work. Some applications, like <a href="/docs/linux/man/1-su/">su</a>(1), enable this option unconditionally.</dd>
<dt><code>warn_pwexpire = </code><i>time</i></dt>
<dd>How soon to warn for expiring password. Default is seven days.</dd>
<dt><code>http_proxy = </code><i>proxy-spec</i></dt>
<dd>A HTTP-proxy to use when talking to the KDC via HTTP.</dd>
<dt><code>dns_proxy = </code><i>proxy-spec</i></dt>
<dd>Enable using DNS via HTTP.</dd>
<dt><code>extra_addresses = </code><i>address &#8230;</i></dt>
<dd>A list of addresses to get tickets for along with all local addresses.</dd>
<dt><code>time_format = </code><i>string</i></dt>
<dd>How to print time strings in logs, this string is passed to <a href="/docs/linux/man/3-strftime/">strftime</a>(3).</dd>
<dt><code>date_format = </code><i>string</i></dt>
<dd>How to print date strings in logs, this string is passed to <a href="/docs/linux/man/3-strftime/">strftime</a>(3).</dd>
<dt><code>log_utc = </code><i>boolean</i></dt>
<dd>Write log-entries using UTC instead of your local time zone.</dd>
<dt><code>scan_interfaces = </code><i>boolean</i></dt>
<dd>Scan all network interfaces for addresses, as opposed to simply using the address associated with the system&#8217;s host name.</dd>
<dt><code>fcache_version = </code><i>int</i></dt>
<dd>Use file credential cache format version specified.</dd>
<dt><code>krb4_get_tickets = </code><i>boolean</i></dt>
<dd>Also get Kerberos 4 tickets in <code>kinit</code> <code>login</code> and other programs. This option is also valid in the [realms] section.</dd>
<dt><code>fcc-mit-ticketflags = </code><i>boolean</i></dt>
<dd>Use MIT compatible format for file credential cache. It&#8217;s the field ticketflags that is stored in reverse bit order for older than Heimdal 0.7. Setting this flag to <code>TRUE</code> make it store the MIT way, this is default for Heimdal 0.7.</dd>
<dt><code>check-rd-req-server</code></dt>
<dd>If set to &quot;ignore&quot;, the framework will ignore any the server input to krb5_rd_req3, this is very useful when the GSS-API server input the wrong server name into the gss_accept_sec_context call.</dd>
<dt><code>k5login_directory = </code><i>directory</i></dt>
<dd>Alternative location for user .k5login files. This option is provided for compatibility with MIT krb5 configuration files.</dd>
<dt><code>k5login_authoritative = </code><i>boolean</i></dt>
<dd>If true then if a principal is not found in k5login files then krb5_userok3 will not fallback on principal to username mapping. This option is provided for compatibility with MIT krb5 configuration files.</dd>
<dt><code>kuserok = </code><i>rule &#8230;</i></dt>
<dd>Specifies krb5_userok3 behavior. If multiple values are given, then krb5_userok3 will evaluate them in order until one succeeds or all fail. Rules are implemented by plugins, with three built-in plugins described below. Default: USER-K5LOGIN SIMPLE DENY.</dd>
<dt><code>kuserok = </code><i>DENY</i></dt>
<dd>If set and evaluated then krb5_userok3 will deny access to the given username no matter what the principal name might be.</dd>
<dt><code>kuserok = </code><i>SIMPLE</i></dt>
<dd>If set and evaluated then krb5_userok3 will use principal to username mapping (see auth_to_local below). If the principal maps to the requested username then access is allowed.</dd>
<dt><code>kuserok = </code><i>SYSTEM-K5LOGIN[:directory]</i></dt>
<dd>If set and evaluated then krb5_userok3 will use k5login files named after the <i>luser</i> argument to krb5_userok3 in the given directory or in /etc/k5login.d/ K5login files are text files, with each line containing just a principal name; principals apearing in a user&#8217;s k5login file are permitted access to the user&#8217;s account. Note: this rule performs no ownership nor permissions checks on k5login files; proper ownership and permissions/ACLs are expected due to the system k5login location being a system location.</dd>
<dt><code>kuserok = </code><i>USER-K5LOGIN</i></dt>
<dd>If set and evaluated then krb5_userok3 will use ~luser/.k5login and ~luser/.k5login.d/* User k5login files and directories must be owned by the user and must not have world nor group write permissions.</dd>
<dt><code>aname2lname-text-db = </code><i>filename</i></dt>
<dd>The named file must be a sorted (in increasing order) text file where every line consists of an unparsed principal name optionally followed by whitespace and a username. The aname2lname function will do a binary search on this file, if configured, looking for lines that match the given principal name, and if found the given username will be used, or, if the username is missing, an error will be returned. If the file doesn&#8217;t exist, or if no matching line is found then other plugins will be allowed to run.</dd>
<dt><code>fcache_strict_checking</code></dt>
<dd>strict checking in FILE credential caches that owner, no symlink and permissions is correct.</dd></dl>
<dt><code>[domain_realm]</code></dt>
<dd>This is a list of mappings from DNS domain to Kerberos realm. Each binding in this section looks like: </dd>
<blockquote><p><tt>domain = realm</tt></p></blockquote>
<p> The domain can be either a full name of a host or a trailing component, in the latter case the domain-string should start with a period. The trailing component only matches hosts that are in the same domain, ie &#8220;.example.com&#8221; matches &#8220;foo.example.com&#8221; but not &#8220;foo.test.example.com&#8221; The realm may be the token `dns_locate&#8217;, in which case the actual realm will be determined using DNS (independently of the setting of the `dns_lookup_realm&#8217; option).</p>
<dt><code>[realms]</code></dt>
<dd>
</dd><dl>
<dt><i>REALM </i><code>=</code></dt>
<dd>
</dd><dl>
<dt><code>kdc = </code><i>[service/]host[:port]</i></dt>
<dd>Specifies a list of kdcs for this realm. If the optional <i>port</i> is absent, the default value for the &#8220;kerberos/udp&#8221; &#8220;kerberos/tcp&#8221; and &#8220;http/tcp&#8221; port (depending on service) will be used. The kdcs will be used in the order that they are specified. The optional <i>service</i> specifies over what medium the kdc should be contacted. Possible services are &#8220;udp&#8221; &#8220;tcp&#8221; and &#8220;http&#8221; Http can also be written as &#8220;<a rel="nofollow" href="http://''">http://&#8221;</a> Default service is &#8220;udp&#8221; and &#8220;tcp&#8221;</dd>
<dt><code>admin_server = </code><i>host[:port]</i></dt>
<dd>Specifies the admin server for this realm, where all the modifications to the database are performed.</dd>
<dt><code>kpasswd_server = </code><i>host[:port]</i></dt>
<dd>Points to the server where all the password changes are performed. If there is no such entry, the kpasswd port on the admin_server host will be tried.</dd>
<dt><code>krb524_server = </code><i>host[:port]</i></dt>
<dd>Points to the server that does 524 conversions. If it is not mentioned, the krb524 port on the kdcs will be tried.</dd>
<dt><code>v4_instance_convert</code></dt>
<dd>
</dd><dt><code>v4_name_convert</code></dt>
<dd>
</dd><dt><code>default_domain</code></dt>
<dd>See krb5_425_conv_principal3.</dd>
<dt><code>tgs_require_subkey</code></dt>
<dd>a boolan variable that defaults to false. Old DCE secd (pre 1.1) might need this to be true.</dd>
<dt><code>auth_to_local_names</code></dt>
<dd>
</dd><dl>
<dt><i>principal_name = username</i></dt>
<dd>The given <i>principal_name</i> will be mapped to the given <i>username</i> if the <i>REALM</i> is a default realm.</dd></dl>
<p> }</p>
<p>auth_to_local = HEIMDAL_DEFAULT</p>
<p>Use the Heimdal default principal to username mapping.<br />
Applies to principals from the<br />
REALM</p>
<p>if and only if<br />
REALM</p>
<p>is a default realm.<br />
auth_to_local = DEFAULT</p>
<p>Use the MIT default principal to username mapping.<br />
Applies to principals from the<br />
REALM</p>
<p>if and only if<br />
REALM</p>
<p>is a default realm.<br />
auth_to_local = DB:/path/to/db.txt</p>
<p>Use a binary search of the given DB.  The DB must be a flat-text<br />
file sortedf in the &quot;C&quot; locale, with each record being a line<br />
(separated by either LF or CRLF) consisting of a principal name<br />
followed by whitespace followed by a username.<br />
Applies to principals from the<br />
REALM</p>
<p>if and only if<br />
REALM</p>
<p>is a default realm.<br />
auth_to_local = DB:/path/to/db</p>
<p>Use the given DB, if there&#8217;s a plugin for it.<br />
Applies to principals from the<br />
REALM</p>
<p>if and only if<br />
REALM</p>
<p>is a default realm.<br />
auth_to_local = RULE:&#8230;</p>
<p>Use the given rule, if there&#8217;s a plugin for it.<br />
Applies to principals from the<br />
REALM</p>
<p>if and only if<br />
REALM</p>
<p>is a default realm.<br />
auth_to_local = NONE</p>
<p>No additional principal to username mapping is done. Note that<br />
auth_to_local_names</p>
<p>and any preceding<br />
auth_to_local</p>
<p>rules have precedence.<br />
}</p>
<dt><code>[capaths]</code></dt>
<dd>
</dd><dl>
<dt><i>client-realm </i><code>=</code></dt>
<dd>
</dd><dl>
<dt><i>server-realm </i><code>= </code><i>hop-realm &#8230;</i></dt>
<dd>This serves two purposes. First the first listed <i>hop-realm</i> tells a client which realm it should contact in order to ultimately obtain credentials for a service in the <i>server-realm</i> Secondly, it tells the KDC (and other servers) which realms are allowed in a multi-hop traversal from <i>client-realm</i> to <i>server-realm</i> Except for the client case, the order of the realms are not important.</dd></dl>
<p> }</p>
<dt><code>[logging]</code></dt>
<dd>
</dd><dl>
<dt><i>entity </i><code>= </code><i>destination</i></dt>
<dd>Specifies that <i>entity</i> should use the specified <code>destination</code> for logging. See the krb5_openlog3 manual page for a list of defined destinations.</dd></dl>
<dt><code>[kdc]</code></dt>
<dd>
</dd><dl>
<dt><code>database =</code></dt>
<dd>
</dd><dl>
<dt><code>dbname = </code><i>DATABASENAME</i></dt>
<dd>Use this database for this realm. See the info documetation how to configure different database backends.</dd>
<dt><code>realm = </code><i>REALM</i></dt>
<dd>Specifies the realm that will be stored in this database. It realm isn&#8217;t set, it will used as the default database, there can only be one entry that doesn&#8217;t have a <code>realm</code> stanza.</dd>
<dt><code>mkey_file = FILENAME </code></dt>
<dd>Use this keytab file for the master key of this database. If not specified <i>DATABASENAME </i><code>.mkey</code> will be used.</dd>
<dt><code>acl_file = PA FILENAME</code></dt>
<dd>Use this file for the ACL list of this database.</dd>
<dt><code>log_file = FILENAME </code></dt>
<dd>Use this file as the log of changes performed to the database. This file is used by <code>ipropd-master</code> for propagating changes to slaves.</dd></dl>
<p> }</p>
<p>max-request = SIZE</p>
<p>Maximum size of a kdc request.<br />
require-preauth = BOOL</p>
<p>If set pre-authentication is required.<br />
Since krb4 requests are not pre-authenticated they will be rejected.<br />
ports = list of ports</p>
<p>List of ports the kdc should listen to.<br />
addresses = list of interfaces</p>
<p>List of addresses the kdc should bind to.<br />
enable-kerberos4 = BOOL</p>
<p>Turn on Kerberos 4 support.<br />
v4-realm = REALM</p>
<p>To what realm v4 requests should be mapped.<br />
enable-524 = BOOL</p>
<p>Should the Kerberos 524 converting facility be turned on.<br />
Default is the same as<br />
enable-kerberos4</p>
<p>enable-http = BOOL</p>
<p>Should the kdc answer kdc-requests over http.<br />
tgt-use-strongest-session-key = BOOL</p>
<p>If this is TRUE then the KDC will prefer the strongest key from the<br />
client&#8217;s AS-REQ or TGS-REQ enctype list for the ticket session key that<br />
is supported by the KDC and the target principal when the target<br />
principal is a krbtgt principal.  Else it will prefer the first key from<br />
the client&#8217;s AS-REQ enctype list that is also supported by the KDC and<br />
the target principal.  Defaults to FALSE.<br />
svc-use-strongest-session-key = BOOL</p>
<p>Like tgt-use-strongest-session-key, but applies to the session key<br />
enctype of tickets for services other than krbtgt principals. Defaults<br />
to FALSE.<br />
preauth-use-strongest-session-key = BOOL</p>
<p>If TRUE then select the strongest possible enctype from the client&#8217;s<br />
AS-REQ for PA-ETYPE-INFO2 (i.e., for password-based pre-authentication).<br />
Else pick the first supported enctype from the client&#8217;s AS-REQ.  Defaults<br />
to FALSE.<br />
use-strongest-server-key = BOOL</p>
<p>If TRUE then the KDC picks, for the ticket encrypted part&#8217;s key, the<br />
first supported enctype from the target service principal&#8217;s hdb entry&#8217;s<br />
current keyset. Else the KDC picks the first supported enctype from the<br />
target service principal&#8217;s hdb entry&#8217;s current keyset.  Defaults to TRUE.<br />
check-ticket-addresses = BOOL</p>
<p>Verify the addresses in the tickets used in tgs requests.</p>
<p>allow-null-ticket-addresses = BOOL</p>
<p>Allow address-less tickets.</p>
<p>allow-anonymous = BOOL</p>
<p>If the kdc is allowed to hand out anonymous tickets.<br />
encode_as_rep_as_tgs_rep = BOOL</p>
<p>Encode as-rep as tgs-rep tobe compatible with mistakes older DCE secd did.</p>
<p>kdc_warn_pwexpire = TIME</p>
<p>The time before expiration that the user should be warned that her<br />
password is about to expire.<br />
logging = Logging</p>
<p>What type of logging the kdc should use, see also [logging]/kdc.<br />
use_2b<br />
principal = BOOL</p>
<p>boolean value if the 524 daemon should return AFS 2b tokens for<br />
Fa principal .</p>
<p>&#8230;<br />
}</p>
<p>hdb-ldap-structural-object structural object</p>
<p>If the LDAP backend is used for storing principals, this is the<br />
structural object that will be used when creating and when reading<br />
objects.<br />
The default value is account .<br />
hdb-ldap-create-base creation dn</p>
<p>is the dn that will be appended to the principal when creating entries.<br />
Default value is the search dn.<br />
enable-digest = BOOL</p>
<p>Should the kdc answer digest requests. The default is FALSE.<br />
digests_allowed = list of digests</p>
<p>Specifies the digests the kdc will reply to. The default is<br />
ntlm-v2</p>
<p>kx509_ca = file</p>
<p>Specifies the PEM credentials for the kx509 certification authority.<br />
require_initial_kca_tickets = boolean</p>
<p>Specified whether to require that tickets for the<br />
kca_service</p>
<p>service principal be INITIAL.<br />
This may be set on a per-realm basis as well as globally.<br />
Defaults to true for the global setting.<br />
kx509_include_pkinit_san = boolean</p>
<p>If true then the kx509 client principal&#8217;s name and realm will be<br />
included in an<br />
id-pkinit-san</p>
<p>certificate extension.<br />
This can be set on a per-realm basis as well as globally.<br />
Defaults to true for the global setting.<br />
kx509_template = file</p>
<p>Specifies the PEM file with a template for the certificates to be<br />
issued.<br />
The following variables can be interpolated in the subject name using<br />
${variable} syntax:</p>
<dt><code>principal-name</code></dt>
<dd>The full name of the kx509 client principal.</dd>
<dt><code>principal-name-without-realm</code></dt>
<dd>The full name of the kx509 client principal, excluding the realm name.</dd>
<dt><code>principal-name-realm</code></dt>
<dd>The name of the client principal&#8217;s realm.</dd></dl>
<p>  The <code>kx509</code> <code>kx509_template</code> <code>kx509_include_pkinit_san</code> and <code>require_initial_kca_tickets</code> parameters may be set on a per-realm basis as well.</p>
<dt><code>[kadmin]</code></dt>
<dd>
</dd><dl>
<dt><code>password_lifetime = </code><i>time</i></dt>
<dd>If a principal already have its password set for expiration, this is the time it will be valid for after a change.</dd>
<dt><code>default_keys = </code><i>keytypes&#8230;</i></dt>
<dd>For each entry in <i>default_keys</i> try to parse it as a sequence of <i>etype:salttype:salt</i> syntax of this if something like: [(des|des3|etype):](pw-salt|afs3-salt)[:string] If <i>etype</i> is omitted it means everything, and if string is omitted it means the default salt string (for that principal and encryption type). Additional special values of keytypes are:</dd>
<dl>
<dt><code>v5</code></dt>
<dd>The Kerberos 5 salt <i>pw-salt</i></dd>
<dt><code>v4</code></dt>
<dd>The Kerberos 4 salt <i>des:pw-salt:</i></dd></dl>
<p> default_key_rules = {<br />
    globing-rule = keytypes&#8230;</p>
<p>    a globbing rule to matching a principal, and when true, use the<br />
    keytypes as specified the same format as [kadmin]default_keys .<br />
}</p>
<dt><code>use_v4_salt = </code><i>BOOL</i></dt>
<dd>When true, this is the same as <i>default_keys = des3:pw-salt v4</i> and is only left for backwards compatibility.</dd>
<dt><code>[password_quality]</code></dt>
<dd>Check the Password quality assurance in the info documentation for more information.</dd>
<dl>
<dt><code>check_library = </code><i>library-name</i></dt>
<dd>Library name that contains the password check_function</dd>
<dt><code>check_function = </code><i>function-name</i></dt>
<dd>Function name for checking passwords in check_library</dd>
<dt><code>policy_libraries = </code><i>library1 &#8230; libraryN</i></dt>
<dd>List of libraries that can do password policy checks</dd>
<dt><code>policies = </code><i>policy1 &#8230; policyN</i></dt>
<dd>List of policy names to apply to the password. Builtin policies are among other minimum-length, character-class, external-check.</dd></dl>
<h2>Environment</h2>
<p><code>KRB5_CONFIG</code> points to the configuration file to read.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/krb5.conf </code></dt>
<dd>configuration file for Kerberos 5.</dd></dl>
<h2>Examples</h2>
<pre><code>[libdefaults]
default_realm = FOO.SE
[domain_realm]
.foo.se = FOO.SE
.bar.se = FOO.SE
[realms]
FOO.SE = {
    kdc = kerberos.foo.se
    v4_name_convert = {
        rcmd = host
    }
    v4_instance_convert = {
        xyz = xyz.bar.se
    }
    default_domain = foo.se
}
[logging]
kdc = FILE:/var/heimdal/kdc.log
kdc = SYSLOG:INFO
default = SYSLOG:INFO:USER
[kadmin]
default_key_rules = {
    */ppp@* = arcfour-hmac-md5:pw-salt
}</code></pre>
<h2>Diagnostics</h2>
<p>Since is read and parsed by the krb5 library, there is not a lot of opportunities for programs to report parsing errors in any useful format. To help overcome this problem, there is a program <code>verify_krb5_conf</code> that reads and tries to emit useful diagnostics from parsing errors. Note that this program does not have any way of knowing what options are actually used and thus cannot warn about unknown or misspelled ones.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kinit/">kinit</a>(1), krb5_425_conv_principal3, krb5_openlog3, <a href="/docs/linux/man/3-strftime/">strftime</a>(3), verify_krb5_conf8 </p>
</dl></dl></dl></dl></dl></dl>