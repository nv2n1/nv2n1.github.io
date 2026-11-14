---
title: "sudoers-ldap(5)"
name: "sudoers-ldap"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudoers-ldap/"
description: "sudoers.ldap – sudo LDAP configuration"
---

<p><code>sudoers.ldap</code> &#8211; sudo LDAP configuration</p>
<h2>Description</h2>
<p>In addition to the standard <i>sudoers</i> file, <code>sudo</code> may be configured via LDAP. This can be especially useful for synchronizing <i>sudoers</i> in a large, distributed environment. Using LDAP for <i>sudoers</i> has several benefits: </p>
<ul>
<li> <code>sudo</code> no longer needs to read <i>sudoers</i> in its entirety. When LDAP is used, there are only two or three LDAP queries per invocation. This makes it especially fast and particularly usable in LDAP environments.
<li> <code>sudo</code> no longer exits if there is a typo in <i>sudoers</i> It is not possible to load LDAP data into the server that does not conform to the sudoers schema, so proper syntax is guaranteed. It is still possible to have typos in a user or host name, but this will not prevent <code>sudo</code> from running.
<li> It is possible to specify per-entry options that override the global default options. /etc/sudoers only supports default options and limited options associated with user/host/commands/aliases. The syntax is complicated and can be difficult for users to understand. Placing the options directly in the entry is more natural.
<li> The <code>visudo</code> program is no longer needed. <code>visudo</code> provides locking and syntax checking of the /etc/sudoers file. Since LDAP updates are atomic, locking is no longer necessary. Because syntax is checked when the data is inserted into LDAP, there is no need for a specialized tool to check syntax. </ul>
<p> Another major difference between LDAP and file-based <i>sudoers</i> is that in LDAP, <code>sudo -specific</code> Aliases are not supported. For the most part, there is really no need for <code>sudo -specific</code> Aliases. Unix groups, non-Unix groups (via the <i>group_plugin</i> or user netgroups can be used in place of User_Aliases and Runas_Aliases. Host netgroups can be used in place of Host_Aliases. Since groups and netgroups can also be stored in LDAP there is no real need for <code>sudo -specific</code> aliases. Cmnd_Aliases are not really required either since it is possible to have multiple users listed in a <code>sudoRole</code> Instead of defining a Cmnd_Alias that is referenced by multiple users, one can create a <code>sudoRole</code> that contains the commands and assign multiple users to it.</p>
<h3>SUDOers LDAP container</h3>
<p>The <i>sudoers</i> configuration is contained in the <code>ou=SUDOers</code> LDAP container. Sudo first looks for the <code>cn=defaults</code> entry in the SUDOers container. If found, the multi-valued <code>sudoOption</code> attribute is parsed in the same manner as a global <code>Defaults</code> line in /etc/sudoers In the following example, the <code>SSH_AUTH_SOCK</code> variable will be preserved in the environment for all users. </p>
<pre>dn: cn=defaults,ou=SUDOers,dc=example,dc=com
objectClass: top
objectClass: sudoRole
cn: defaults
description: Default sudoOption's go here
sudoOption: env_keep+=SSH_AUTH_SOCK</pre>
<p>The equivalent of a sudoer in LDAP is a <code>sudoRole</code> It consists of the following attributes:</p>
<dl>
<dt><code>sudoUser</code></p>
<dd>A user name, user ID (prefixed with `#&#8217; ) , Unix group name or ID (prefixed with `%&#8217; or `%#&#8217; respectively), user netgroup (prefixed with `+&#8217; ) , or non-Unix group name or ID (prefixed with `%:&#8217; or `%:#&#8217; respectively). User netgroups are matched using the user and domain members only; the host member is not used when matching. Non-Unix group support is only available when an appropriate <i>group_plugin</i> is defined in the global <i>defaults</i> <code>sudoRole</code> object.</p>
<dt><code>sudoHost</code></p>
<dd>A host name, IP address, IP network, or host netgroup (prefixed with a `+&#8217; ) . The special value <code>ALL</code> will match any host. Host netgroups are matched using the host (both qualified and unqualified) and domain members only; the user member is not used when matching. If a <code>sudoHost</code> entry is preceded by an exclamation point, `!&#8217; , and the entry matches, the <code>sudoRole</code> in which it resides will be ignored. Negated <code>sudoHost</code> entries are only supported by version 1.8.18 or higher.</p>
<dt><code>sudoCommand</code></p>
<dd>A fully-qualified Unix command name with optional command line arguments, potentially including globbing characters (aka wild cards). If a command name is preceded by an exclamation point, `!&#8217; , the user will be prohibited from running that command. The built-in command &#8220;<code>sudoedit</code> &#8221; is used to permit a user to run <code>sudo</code> with the &#8211;<code>e</code> option (or as <code>sudoedit )</code> It may take command line arguments just as a normal command does. Note that &#8220;<code>sudoedit</code> &#8221; is a command built into <code>sudo</code> itself and must be specified in without a leading path. The special value <code>ALL</code> will match any command. If a command name is prefixed with a SHA-2 digest, it will only be allowed if the digest matches. This may be useful in situations where the user invoking <code>sudo</code> has write access to the command or its parent directory. The following digest formats are supported: sha224, sha256, sha384 and sha512. The digest name must be followed by a colon (`:&#8217; ) and then the actual digest, in either hex or base64 format. For example, given the following value for sudoCommand: </p>
<pre>sha224:0GomF8mNN3wlDt1HD9XldjJ3SNgpFdbjO1+NsQ /bin/ls</pre>
<p>The user may only run /bin/ls if its sha224 digest matches the specified value. Command digests are only supported by version 1.8.7 or higher.</p>
<dt><code>sudoOption</code></p>
<dd>Identical in function to the global options described above, but specific to the <code>sudoRole</code> in which it resides.</p>
<dt><code>sudoRunAsUser</code></p>
<dd>A user name or uid (prefixed with `#&#8217; ) that commands may be run as or a Unix group (prefixed with a `%&#8217; ) or user netgroup (prefixed with a `+&#8217; ) that contains a list of users that commands may be run as. The special value <code>ALL</code> will match any user. The <code>sudoRunAsUser</code> attribute is only available in <code>sudo</code> versions 1.7.0 and higher. Older versions of <code>sudo</code> use the <code>sudoRunAs </code>attribute instead.</p>
<dt><code>sudoRunAsGroup</code></p>
<dd>A Unix group or gid (prefixed with `#&#8217; ) that commands may be run as. The special value <code>ALL</code> will match any group. The <code>sudoRunAsGroup</code> attribute is only available in <code>sudo</code> versions 1.7.0 and higher.</p>
<dt><code>sudoNotBefore</code></p>
<dd>A timestamp in the form <code>yyyymmddHHMMSSZ</code> that can be used to provide a start date/time for when the <code>sudoRole</code> will be valid. If multiple <code>sudoNotBefore</code> entries are present, the earliest is used. Note that timestamps must be in Coordinated Universal Time (UTC), not the local timezone. The minute and seconds portions are optional, but some LDAP servers require that they be present (contrary to the RFC). The <code>sudoNotBefore</code> attribute is only available in <code>sudo</code> versions 1.7.5 and higher and must be explicitly enabled via the <code>SUDOERS_TIMED</code> option in /etc/sudo-ldap.conf</p>
<dt><code>sudoNotAfter</code></p>
<dd>A timestamp in the form <code>yyyymmddHHMMSSZ</code> that indicates an expiration date/time, after which the <code>sudoRole</code> will no longer be valid. If multiple <code>sudoNotAfter</code> entries are present, the last one is used. Note that timestamps must be in Coordinated Universal Time (UTC), not the local timezone. The minute and seconds portions are optional, but some LDAP servers require that they be present (contrary to the RFC). The <code>sudoNotAfter</code> attribute is only available in <code>sudo</code> versions 1.7.5 and higher and must be explicitly enabled via the <code>SUDOERS_TIMED</code> option in /etc/sudo-ldap.conf</p>
<dt><code>sudoOrder</code></p>
<dd>The <code>sudoRole</code> entries retrieved from the LDAP directory have no inherent order. The <code>sudoOrder</code> attribute is an integer (or floating point value for LDAP servers that support it) that is used to sort the matching entries. This allows LDAP-based sudoers entries to more closely mimic the behavior of the sudoers file, where the order of the entries influences the result. If multiple entries match, the entry with the highest <code>sudoOrder</code> attribute is chosen. This corresponds to the &#8220;last match&#8221; behavior of the sudoers file. If the <code>sudoOrder</code> attribute is not present, a value of 0 is assumed. The <code>sudoOrder</code> attribute is only available in <code>sudo</code> versions 1.7.5 and higher.</dl>
<p> Each attribute listed above should contain a single value, but there may be multiple instances of each attribute type. A <code>sudoRole</code> must contain at least one <code>sudoUser</code> <code>sudoHost</code> and <code>sudoCommand</code> The following example allows users in group wheel to run any command on any host via <code>sudo</code> </p>
<pre>dn: cn=%wheel,ou=SUDOers,dc=example,dc=com
objectClass: top
objectClass: sudoRole
cn: %wheel
sudoUser: %wheel
sudoHost: ALL
sudoCommand: ALL</pre>
<h3>Anatomy of LDAP sudoers lookup</h3>
<p>When looking up a sudoer using LDAP there are only two or three LDAP queries per invocation. The first query is to parse the global options. The second is to match against the user&#8217;s name and the groups that the user belongs to. (The special <code>ALL</code> tag is matched in this query too.) If no match is returned for the user&#8217;s name and groups, a third query returns all entries containing user netgroups and other non-Unix groups and checks to see if the user belongs to any of them. If timed entries are enabled with the <code>SUDOERS_TIMED</code> configuration directive, the LDAP queries include a sub-filter that limits retrieval to entries that satisfy the time constraints, if any. If the <code>NETGROUP_BASE</code> configuration directive is present (see Sx Configuring ldap.conf below), queries are performed to determine the list of netgroups the user belongs to before the sudoers query. This makes it possible to include netgroups in the sudoers query string in the same manner as Unix groups. The third query mentioned above is not performed unless a group provider plugin is also configured. The actual LDAP queries performed by <code>sudo</code> are as follows: </p>
<ol>
<li> Match all <code>nisNetgroup</code> records with a <code>nisNetgroupTriple</code> containing the user, host and NIS domain. The query will match <code>nisNetgroupTriple</code> entries with either the short or long form of the host name or no host name specified in the tuple. If the NIS domain is set, the query will match only match entries that include the domain or for which there is no domain present. If the NIS domain is <i>not</i> set, a wildcard is used to match any domain name but be aware that the NIS schema used by some LDAP servers may not support wild cards for <code>nisNetgroupTriple</code>
<li> Repeated queries are performed to find any nested <code>nisNetgroup</code> records with a <code>memberNisNetgroup</code> entry that refers to an already-matched record. </ol>
<p> For sites with a large number of netgroups, using <code>NETGROUP_BASE</code> can significantly speed up <code>sudo &#8216;s</code> execution time.</p>
<h3>Differences between LDAP and non-LDAP sudoers</h3>
<p>There are some subtle differences in the way sudoers is handled once in LDAP. Probably the biggest is that according to the RFC, LDAP ordering is arbitrary and you cannot expect that Attributes and Entries are returned in any specific order. The order in which different entries are applied can be controlled using the <code>sudoOrder</code> attribute, but there is no way to guarantee the order of attributes within a specific entry. If there are conflicting command rules in an entry, the negative takes precedence. This is called paranoid behavior (not necessarily the most specific match). Here is an example: </p>
<pre># /etc/sudoers:
# Allow all commands except shell
johnny ALL=(root) ALL,!/bin/sh
# Always allows all commands because ALL is matched last
puddles ALL=(root) !/bin/sh,ALL
# LDAP equivalent of johnny
# Allows all commands except shell
dn: cn=role1,ou=Sudoers,dc=my-domain,dc=com
objectClass: sudoRole
objectClass: top
cn: role1
sudoUser: johnny
sudoHost: ALL
sudoCommand: ALL
sudoCommand: !/bin/sh
# LDAP equivalent of puddles
# Notice that even though ALL comes last, it still behaves like
# role1 since the LDAP code assumes the more paranoid configuration
dn: cn=role2,ou=Sudoers,dc=my-domain,dc=com
objectClass: sudoRole
objectClass: top
cn: role2
sudoUser: puddles
sudoHost: ALL
sudoCommand: !/bin/sh
sudoCommand: ALL</pre>
<p>Another difference is that negations on the Host, User or Runas are currently ignored. For example, the following attributes do not behave the way one might expect. </p>
<pre># does not match all but joe
# rather, does not match anyone
sudoUser: !joe
# does not match all but joe
# rather, matches everyone including Joe
sudoUser: ALL
sudoUser: !joe
# does not match all but web01
# rather, matches all hosts including web01
sudoHost: ALL
sudoHost: !web01</pre>
<h3>Sudoers schema</h3>
<p>In order to use <code>sudo &#8216;s</code> LDAP support, the <code>sudo</code> schema must be installed on your LDAP server. In addition, be sure to index the <code>sudoUser</code> attribute. Three versions of the schema: one for OpenLDAP servers (schema.OpenLDAP ) one for Netscape-derived servers (schema.iPlanet ) and one for Microsoft Active Directory (schema.ActiveDirectory ) may be found in the <code>sudo</code> distribution. The schema for <code>sudo</code> in OpenLDAP form is also included in the Sx EXAMPLES section.</p>
<h3>Configuring ldap.conf</h3>
<p>Sudo reads the /etc/sudo-ldap.conf file for LDAP-specific configuration. Typically, this file is shared between different LDAP-aware clients. As such, most of the settings are not <code>sudo -specific.</code> Note that <code>sudo</code> parses /etc/sudo-ldap.conf itself and may support options that differ from those described in the system&#8217;s ldap.conf5 manual. The path to ldap.conf may be overridden via the <i>ldap_conf</i> plugin argument in sudo.conf5. Also note that on systems using the OpenLDAP libraries, default values specified in /etc/openldap/ldap.conf or the user&#8217;s .ldaprc files are not used. Only those options explicitly listed in /etc/sudo-ldap.conf as being supported by <code>sudo</code> are honored. Configuration options are listed below in upper case but are parsed in a case-independent manner. Lines beginning with a pound sign (`#&#8217; ) are ignored. Leading white space is removed from the beginning of lines.</p>
<dl>
<dt><code>BIND_TIMELIMIT </code><i>seconds</i></p>
<dd>The <code>BIND_TIMELIMIT</code> parameter specifies the amount of time, in seconds, to wait while trying to connect to an LDAP server. If multiple <code>URI s</code> or <code>HOST s</code> are specified, this is the amount of time to wait before trying the next one in the list.</p>
<dt><code>BINDDN </code><i>DN</i></p>
<dd>The <code>BINDDN</code> parameter specifies the identity, in the form of a Distinguished Name (DN), to use when performing LDAP operations. If not specified, LDAP operations are performed with an anonymous identity. By default, most LDAP servers will allow anonymous access.</p>
<dt><code>BINDPW </code><i>secret</i></p>
<dd>The <code>BINDPW</code> parameter specifies the password to use when performing LDAP operations. This is typically used in conjunction with the <code>BINDDN</code> parameter. The <i>secret</i> may be a plain text password or a base64-encoded string with a &#8220;base64:&#8221; prefix. For example: </p>
<pre>BINDPW base64:dGVzdA==</pre>
<p>If a plain text password is used, it should be a simple string without quotes. Plain text passwords may not include the comment character (`#&#8217; ) and the escaping of special characters with a backslash (`\&#8217; ) is not supported.</p>
<dt><code>DEREF </code><i>never/searching/finding/always</i></p>
<dd>How alias dereferencing is to be performed when searching. See the ldap.conf5 manual for a full description of this option.</p>
<dt><code>HOST </code><i>name[:port] &#8230;</i></p>
<dd>If no <code>URI</code> is specified (see below), the <code>HOST</code> parameter specifies a white space-delimited list of LDAP servers to connect to. Each host may include an optional <i>port</i> separated by a colon (`:&#8217; ) The <code>HOST</code> parameter is deprecated in favor of the <code>URI</code> specification and is included for backwards compatibility only.</p>
<dt><code>KRB5_CCNAME </code><i>file name</i></p>
<dd>The path to the Kerberos 5 credential cache to use when authenticating with the remote server. This option is only relevant when using SASL authentication (see below).</p>
<dt><code>LDAP_VERSION </code><i>number</i></p>
<dd>The version of the LDAP protocol to use when connecting to the server. The default value is protocol version 3.</p>
<dt><code>NETGROUP_BASE </code><i>base</i></p>
<dd>The base DN to use when performing LDAP netgroup queries. Typically this is of the form <code>ou=netgroup,dc=example,dc=com</code> for the domain <code>example.com</code> Multiple <code>NETGROUP_BASE</code> lines may be specified, in which case they are queried in the order specified. This option can be used to query a user&#8217;s netgroups directly via LDAP which is usually faster than fetching every <code>sudoRole</code> object containing a <code>sudoUser</code> that begins with a `+&#8217; prefix. The NIS schema used by some LDAP servers need a modificaton to support querying the <code>nisNetgroup</code> object by its <code>nisNetgroupTriple</code> member. OpenLDAP&#8217;s <code>slapd</code> requires the following change to the <code>nisNetgroupTriple</code> attribute: </p>
<pre>attributetype ( 1.3.6.1.1.1.1.14 NAME 'nisNetgroupTriple'
 DESC 'Netgroup triple'
 EQUALITY caseIgnoreIA5Match
 SUBSTR caseIgnoreIA5SubstringsMatch
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )</pre>
<dt><code>NETGROUP_SEARCH_FILTER </code><i>ldap_filter</i></p>
<dd>An LDAP filter which is used to restrict the set of records returned when performing an LDAP netgroup query. Typically, this is of the form <code>attribute=value</code> or <code>(&amp;(attribute=value)(attribute2=value2))</code> The default search filter is: <code>objectClass=nisNetgroup</code> If <i>ldap_filter</i> is omitted, no search filter will be used. This option is only when querying netgroups directly via LDAP.</p>
<dt><code>NETWORK_TIMEOUT </code><i>seconds</i></p>
<dd>An alias for <code>BIND_TIMELIMIT</code> provided for OpenLDAP compatibility.</p>
<dt><code>PORT </code><i>port_number</i></p>
<dd>If no <code>URI</code> is specified, the <code>PORT</code> parameter specifies the default port to connect to on the LDAP server if a <code>HOST</code> parameter does not specify the port itself. If no <code>PORT</code> parameter is used, the default is port 389 for LDAP and port 636 for LDAP over TLS (SSL). The <code>PORT</code> parameter is deprecated in favor of the <code>URI</code> specification and is included for backwards compatibility only.</p>
<dt><code>ROOTBINDDN </code><i>DN</i></p>
<dd>The <code>ROOTBINDDN</code> parameter specifies the identity, in the form of a Distinguished Name (DN), to use when performing privileged LDAP operations, such as <i>sudoers</i> queries. The password corresponding to the identity should be stored in the or the path specified by the <i>ldap_secret</i> plugin argument in sudo.conf5, which defaults to /etc/ldap.secret If no <code>ROOTBINDDN</code> is specified, the <code>BINDDN</code> identity is used (if any).</p>
<dt><code>ROOTUSE_SASL </code><i>on/true/yes/off/false/no</i></p>
<dd>Enable <code>ROOTUSE_SASL</code> to enable SASL authentication when connecting to an LDAP server from a privileged process, such as <code>sudo</code></p>
<dt><code>SASL_AUTH_ID </code><i>identity</i></p>
<dd>The SASL user name to use when connecting to the LDAP server. By default, <code>sudo</code> will use an anonymous connection. This option is only relevant when using SASL authentication.</p>
<dt><code>SASL_SECPROPS </code><i>none/properties</i></p>
<dd>SASL security properties or <i>none</i> for no properties. See the SASL programmer&#8217;s manual for details. This option is only relevant when using SASL authentication.</p>
<dt><code>SSL </code><i>on/true/yes/off/false/no</i></p>
<dd>If the <code>SSL</code> parameter is set to <code>on</code> <code>true</code> <code>or</code> <code>yes</code> TLS (SSL) encryption is always used when communicating with the LDAP server. Typically, this involves connecting to the server on port 636 (ldaps).</p>
<dt><code>SSL </code><i>start_tls</i></p>
<dd>If the <code>SSL</code> parameter is set to <code>start_tls</code> the LDAP server connection is initiated normally and TLS encryption is begun before the bind credentials are sent. This has the advantage of not requiring a dedicated port for encrypted communications. This parameter is only supported by LDAP servers that honor the <i>start_tls</i> extension, such as the OpenLDAP and Tivoli Directory servers.</p>
<dt><code>SUDOERS_BASE </code><i>base</i></p>
<dd>The base DN to use when performing <code>sudo</code> LDAP queries. Typically this is of the form <code>ou=SUDOers,dc=example,dc=com</code> for the domain <code>example.com</code> Multiple <code>SUDOERS_BASE</code> lines may be specified, in which case they are queried in the order specified.</p>
<dt><code>SUDOERS_DEBUG </code><i>debug_level</i></p>
<dd>This sets the debug level for <code>sudo</code> LDAP queries. Debugging information is printed to the standard error. A value of 1 results in a moderate amount of debugging information. A value of 2 shows the results of the matches themselves. This parameter should not be set in a production environment as the extra information is likely to confuse users. The <code>SUDOERS_DEBUG</code> parameter is deprecated and will be removed in a future release. The same information is now logged via the <code>sudo</code> debugging framework using the &#8220;ldap&#8221; subsystem at priorities <i>diag</i> and <i>info</i> for <i>debug_level</i> values 1 and 2 respectively. See the sudo.conf5 manual for details on how to configure <code>sudo</code> debugging.</p>
<dt><code>SUDOERS_SEARCH_FILTER </code><i>ldap_filter</i></p>
<dd>An LDAP filter which is used to restrict the set of records returned when performing a <code>sudo</code> LDAP query. Typically, this is of the form <code>attribute=value</code> or <code>(&amp;(attribute=value)(attribute2=value2))</code> The default search filter is: <code>objectClass=sudoRole</code> If <i>ldap_filter</i> is omitted, no search filter will be used.</p>
<dt><code>SUDOERS_TIMED </code><i>on/true/yes/off/false/no</i></p>
<dd>Whether or not to evaluate the <code>sudoNotBefore</code> and <code>sudoNotAfter</code> attributes that implement time-dependent sudoers entries.</p>
<dt><code>TIMELIMIT </code><i>seconds</i></p>
<dd>The <code>TIMELIMIT</code> parameter specifies the amount of time, in seconds, to wait for a response to an LDAP query.</p>
<dt><code>TIMEOUT </code><i>seconds</i></p>
<dd>The <code>TIMEOUT</code> parameter specifies the amount of time, in seconds, to wait for a response from the various LDAP APIs.</p>
<dt><code>TLS_CACERT </code><i>file name</i></p>
<dd>An alias for <code>TLS_CACERTFILE</code> for OpenLDAP compatibility.</p>
<dt><code>TLS_CACERTFILE </code><i>file name</i></p>
<dd>The path to a certificate authority bundle which contains the certificates for all the Certificate Authorities the client knows to be valid, e.g. /etc/ssl/ca-bundle.pem This option is only supported by the OpenLDAP libraries. Netscape-derived LDAP libraries use the same certificate database for CA and client certificates (see <code>TLS_CERT )</code></p>
<dt><code>TLS_CACERTDIR </code><i>directory</i></p>
<dd>Similar to <code>TLS_CACERTFILE</code> but instead of a file, it is a directory containing individual Certificate Authority certificates, e.g. /etc/ssl/certs The directory specified by <code>TLS_CACERTDIR</code> is checked after <code>TLS_CACERTFILE</code> This option is only supported by the OpenLDAP libraries.</p>
<dt><code>TLS_CERT </code><i>file name</i></p>
<dd>The path to a file containing the client certificate which can be used to authenticate the client to the LDAP server. The certificate type depends on the LDAP libraries used.</p>
<dl>
<dt><code>OpenLDAP:</code></p>
<dd><code>tls_cert /etc/ssl/client_cert.pem</code></p>
<dt><code>Netscape-derived:</code></p>
<dd><code>tls_cert /var/ldap/cert7.db</code></p>
<dt><code>Tivoli Directory Server:</code></p>
<dd>Unused, the key database specified by <code>TLS_KEY</code> contains both keys and certificates. When using Netscape-derived libraries, this file may also contain Certificate Authority certificates.</dl>
<dt><code>TLS_CHECKPEER </code><i>on/true/yes/off/false/no</i></p>
<dd>If enabled, <code>TLS_CHECKPEER</code> will cause the LDAP server&#8217;s TLS certificated to be verified. If the server&#8217;s TLS certificate cannot be verified (usually because it is signed by an unknown certificate authority), <code>sudo</code> will be unable to connect to it. If <code>TLS_CHECKPEER</code> is disabled, no check is made. Note that disabling the check creates an opportunity for man-in-the-middle attacks since the server&#8217;s identity will not be authenticated. If possible, the CA&#8217;s certificate should be installed locally so it can be verified. This option is not supported by the Tivoli Directory Server LDAP libraries.</p>
<dt><code>TLS_KEY </code><i>file name</i></p>
<dd>The path to a file containing the private key which matches the certificate specified by <code>TLS_CERT</code> The private key must not be password-protected. The key type depends on the LDAP libraries used.</p>
<dl>
<dt><code>OpenLDAP:</code></p>
<dd><code>tls_key /etc/ssl/client_key.pem</code></p>
<dt><code>Netscape-derived:</code></p>
<dd><code>tls_key /var/ldap/key3.db</code></p>
<dt><code>Tivoli Directory Server:</code></p>
<dd><code>tls_key /usr/ldap/ldapkey.kdb</code></dl>
<p> When using Tivoli LDAP libraries, this file may also contain Certificate Authority and client certificates and may be encrypted.</p>
<dt><code>TLS_CIPHERS </code><i>cipher list</i></p>
<dd>The <code>TLS_CIPHERS</code> parameter allows the administer to restrict which encryption algorithms may be used for TLS (SSL) connections. See the OpenLDAP or Tivoli Directory Server manual for a list of valid ciphers. This option is not supported by Netscape-derived libraries.</p>
<dt><code>TLS_KEYPW </code><i>secret</i></p>
<dd>The <code>TLS_KEYPW</code> contains the password used to decrypt the key database on clients using the Tivoli Directory Server LDAP library. The <i>secret</i> may be a plain text password or a base64-encoded string with a &#8220;base64:&#8221; prefix. For example: </p>
<pre>TLS_KEYPW base64:dGVzdA==</pre>
<p>If a plain text password is used, it should be a simple string without quotes. Plain text passwords may not include the comment character (`#&#8217; ) and the escaping of special characters with a backslash (`\&#8217; ) is not supported. If this option is used, /etc/sudo-ldap.conf must not be world-readable to avoid exposing the password. Alternately, a <i>stash file</i> can be used to store the password in encrypted form (see below). If no <code>TLS_KEYPW</code> is specified, a <i>stash file</i> will be used if it exists. The <i>stash file</i> must have the same path as the file specified by <code>TLS_KEY</code> but use a <code>.sth</code> file extension instead of <code>.kdb</code> e.g. <code>ldapkey.sth</code> The default <code>ldapkey.kdb</code> that ships with Tivoli Directory Server is encrypted with the password <code>ssl_password</code> The <i>gsk8capicmd</i> utility can be used to manage the key database and create a <i>stash file</i> This option is only supported by the Tivoli LDAP libraries.</p>
<dt><code>TLS_RANDFILE </code><i>file name</i></p>
<dd>The <code>TLS_RANDFILE</code> parameter specifies the path to an entropy source for systems that lack a random device. It is generally used in conjunction with <i>prngd</i> or <i>egd</i> This option is only supported by the OpenLDAP libraries.</p>
<dt><code>URI </code><i>ldap[s]://[hostname[:port]] &#8230;</i></p>
<dd>Specifies a white space-delimited list of one or more URIs describing the LDAP server(s) to connect to. The <i>protocol</i> may be either <i>ldap</i> <i>ldaps</i> the latter being for servers that support TLS (SSL) encryption. If no <i>port</i> is specified, the default is port 389 for <code>ldap://</code> or port 636 for <code>ldaps://</code> If no <i>hostname</i> is specified, <code>sudo</code> will connect to <i>localhost</i> Multiple <code>URI</code> lines are treated identically to a <code>URI</code> line containing multiple entries. Only systems using the OpenSSL libraries support the mixing of <code>ldap://</code> and <code>ldaps://</code> URIs. Both the Netscape-derived and Tivoli LDAP libraries used on most commercial versions of Unix are only capable of supporting one or the other.</p>
<dt><code>USE_SASL </code><i>on/true/yes/off/false/no</i></p>
<dd>Enable <code>USE_SASL</code> for LDAP servers that support SASL authentication.</p>
<dt><code>ROOTSASL_AUTH_ID </code><i>identity</i></p>
<dd>The SASL user name to use when <code>ROOTUSE_SASL</code> is enabled.</dl>
<p> See the ldap.conf entry in the Sx EXAMPLES section.</p>
<h3>Configuring nsswitch.conf</h3>
<p>Unless it is disabled at build time, <code>sudo</code> consults the Name Service Switch file, /etc/nsswitch.conf to specify the <i>sudoers</i> search order. Sudo looks for a line beginning with <code>sudoers</code> and uses this to determine the search order. Note that <code>sudo</code> does not stop searching after the first match and later matches take precedence over earlier ones. The following sources are recognized: </p>
<dt><code>files</code></p>
<dd>read sudoers from /etc/sudoers</p>
<dt><code>ldap</code></p>
<dd>read sudoers from LDAP</dl>
<p> In addition, the entry <code>[NOTFOUND=return]</code> will short-circuit the search if the user was not found in the preceding source. To consult LDAP first followed by the local sudoers file (if it exists), use: </p>
<pre>sudoers: ldap files</pre>
<p>The local <i>sudoers</i> file can be ignored completely by using: </p>
<pre>sudoers: ldap</pre>
<p>If the /etc/nsswitch.conf file is not present or there is no sudoers line, the following default is assumed: </p>
<pre>sudoers: files</pre>
<p>Note that /etc/nsswitch.conf is supported even when the underlying operating system does not use an nsswitch.conf file, except on AIX (see below).</p>
<h3>Configuring netsvc.conf</h3>
<p>On AIX systems, the /etc/netsvc.conf file is consulted instead of /etc/nsswitch.conf <code>sudo</code> simply treats netsvc.conf as a variant of nsswitch.conf information in the previous section unrelated to the file format itself still applies. To consult LDAP first followed by the local sudoers file (if it exists), use: </p>
<pre>sudoers = ldap, files</pre>
<p>The local <i>sudoers</i> file can be ignored completely by using: </p>
<pre>sudoers = ldap</pre>
<p>To treat LDAP as authoritative and only use the local sudoers file if the user is not present in LDAP, use: </p>
<pre>sudoers = ldap = auth, files</pre>
<p>Note that in the above example, the <code>auth</code> qualifier only affects user lookups; both LDAP and <i>sudoers</i> will be queried for <code>Defaults</code> entries. If the /etc/netsvc.conf file is not present or there is no sudoers line, the following default is assumed: </p>
<pre>sudoers = files</pre>
<h3>Integration with sssd</h3>
<p>On systems with the <i>System Security Services Daemon</i> (SSSD) and where <code>sudo</code> has been built with SSSD support, it is possible to use SSSD to cache LDAP <i>sudoers</i> rules. To use SSSD as the <i>sudoers</i> source, you should use <code>sssd</code> instead of <code>ldap</code> for the sudoers entry in /etc/nsswitch.conf Note that the /etc/sudo-ldap.conf file is not used by the SSSD <code>sudo</code> back end. Please see sssd-sudo5 for more information on configuring <code>sudo</code> to work with SSSD.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo-ldap.conf </code></p>
<dd>LDAP configuration file</p>
<dt><code>/etc/nsswitch.conf </code></p>
<dd>determines sudoers source order</p>
<dt><code>/etc/netsvc.conf </code></p>
<dd>determines sudoers source order on AIX</dl>
<h2>Examples</h2>
<h3>Example ldap.conf</h3>
<pre># Either specify one or more URIs or one or more host:port pairs.
# If neither is specified sudo will default to localhost, port 389.
#
#host ldapserver
#host ldapserver1 ldapserver2:390
#
# Default port if host is specified without one, defaults to 389.
#port 389
#
# URI will override the host and port settings.
uri <a href="ldap://ldapserver">ldap://ldapserver</a>
#uri <a href="ldaps://secureldapserver">ldaps://secureldapserver</a>
#uri <a href="ldaps://secureldapserver">ldaps://secureldapserver</a> <a href="ldap://ldapserver">ldap://ldapserver</a>
#
# The amount of time, in seconds, to wait while trying to connect to
# an LDAP server.
bind_timelimit 30
#
# The amount of time, in seconds, to wait while performing an LDAP query.
timelimit 30
#
# Must be set or sudo will ignore LDAP; may be specified multiple times.
sudoers_base ou=SUDOers,dc=example,dc=com
#
# verbose sudoers matching from ldap
#sudoers_debug 2
#
# Enable support for time-based entries in sudoers.
#sudoers_timed yes
#
# optional proxy credentials
#binddn &lt;who to search as&gt;
#bindpw &lt;password&gt;
#rootbinddn &lt;who to search as, uses /etc/ldap.secret for bindpw&gt;
#
# LDAP protocol version, defaults to 3
#ldap_version 3
#
# Define if you want to use an encrypted LDAP connection.
# Typically, you must also set the port to 636 (ldaps).
#ssl on
#
# Define if you want to use port 389 and switch to
# encryption before the bind credentials are sent.
# Only supported by LDAP servers that support the start_tls
# extension such as OpenLDAP.
#ssl start_tls
#
# Additional TLS options follow that allow tweaking of the
# SSL/TLS connection.
#
#tls_checkpeer yes # verify server SSL certificate
#tls_checkpeer no # ignore server SSL certificate
#
# If you enable tls_checkpeer, specify either tls_cacertfile
# or tls_cacertdir. Only supported when using OpenLDAP.
#
#tls_cacertfile /etc/certs/trusted_signers.pem
#tls_cacertdir /etc/certs
#
# For systems that don't have /dev/random
# use this along with PRNGD or EGD.pl to seed the
# random number pool to generate cryptographic session keys.
# Only supported when using OpenLDAP.
#
#tls_randfile /etc/egd-pool
#
# You may restrict which ciphers are used. Consult your SSL
# documentation for which options go here.
# Only supported when using OpenLDAP.
#
#tls_ciphers &lt;cipher-list&gt;
#
# Sudo can provide a client certificate when communicating to
# the LDAP server.
# Tips:
# * Enable both lines at the same time.
# * Do not password protect the key file.
# * Ensure the keyfile is only readable by root.
#
# For OpenLDAP:
#tls_cert /etc/certs/client_cert.pem
#tls_key /etc/certs/client_key.pem
#
# For SunONE or iPlanet LDAP, tls_cert and tls_key may specify either
# a directory, in which case the files in the directory must have the
# default names (e.g. cert8.db and key4.db), or the path to the cert
# and key files themselves. However, a bug in version 5.0 of the LDAP
# SDK will prevent specific file names from working. For this reason
# it is suggested that tls_cert and tls_key be set to a directory,
# not a file name.
#
# The certificate database specified by tls_cert may contain CA certs
# and/or the client's cert. If the client's cert is included, tls_key
# should be specified as well.
# For backward compatibility, &quot;sslpath&quot; may be used in place of tls_cert.
#tls_cert /var/ldap
#tls_key /var/ldap
#
# If using SASL authentication for LDAP (OpenSSL)
# use_sasl yes
# sasl_auth_id &lt;SASL user name&gt;
# rootuse_sasl yes
# rootsasl_auth_id &lt;SASL user name for root access&gt;
# sasl_secprops none
# krb5_ccname /etc/.ldapcache</pre>
<h3>Sudo schema for OpenLDAP</h3>
<p>The following schema, in OpenLDAP format, is included with <code>sudo</code> source and binary distributions as schema.OpenLDAP Simply copy it to the schema directory (e.g. /etc/openldap/schema ) add the proper <code>include</code> line in slapd.conf and restart <code>slapd</code> </p>
<pre>attributetype ( 1.3.6.1.4.1.15953.9.1.1
 NAME 'sudoUser'
 DESC 'User(s) who may run sudo'
 EQUALITY caseExactIA5Match
 SUBSTR caseExactIA5SubstringsMatch
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.2
 NAME 'sudoHost'
 DESC 'Host(s) who may run sudo'
 EQUALITY caseExactIA5Match
 SUBSTR caseExactIA5SubstringsMatch
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.3
 NAME 'sudoCommand'
 DESC 'Command(s) to be executed by sudo'
 EQUALITY caseExactIA5Match
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.4
 NAME 'sudoRunAs'
 DESC 'User(s) impersonated by sudo'
 EQUALITY caseExactIA5Match
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.5
 NAME 'sudoOption'
 DESC 'Options(s) followed by sudo'
 EQUALITY caseExactIA5Match
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.6
 NAME 'sudoRunAsUser'
 DESC 'User(s) impersonated by sudo'
 EQUALITY caseExactIA5Match
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.7
 NAME 'sudoRunAsGroup'
 DESC 'Group(s) impersonated by sudo'
 EQUALITY caseExactIA5Match
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
attributetype ( 1.3.6.1.4.1.15953.9.1.8
 NAME 'sudoNotBefore'
 DESC 'Start of time interval for which the entry is valid'
 EQUALITY generalizedTimeMatch
 ORDERING generalizedTimeOrderingMatch
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.24 )
attributetype ( 1.3.6.1.4.1.15953.9.1.9
 NAME 'sudoNotAfter'
 DESC 'End of time interval for which the entry is valid'
 EQUALITY generalizedTimeMatch
 ORDERING generalizedTimeOrderingMatch
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.24 )
attributeTypes ( 1.3.6.1.4.1.15953.9.1.10
 NAME 'sudoOrder'
 DESC 'an integer to order the sudoRole entries'
 EQUALITY integerMatch
 ORDERING integerOrderingMatch
 SYNTAX 1.3.6.1.4.1.1466.115.121.1.27 )
objectclass ( 1.3.6.1.4.1.15953.9.2.1 NAME 'sudoRole' SUP top STRUCTURAL
 DESC 'Sudoer Entries'
 MUST ( cn )
 MAY ( sudoUser $ sudoHost $ sudoCommand $ sudoRunAs $ sudoRunAsUser $
 sudoRunAsGroup $ sudoOption $ sudoNotBefore $ sudoNotAfter $
 sudoOrder $ description )
 )</pre>
<h2>See Also</h2>
<p>ldap.conf5, sssd-sudo5, sudo.conf5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5)</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Caveats</h2>
<p>Note that there are differences in the way that LDAP-based <i>sudoers</i> is parsed compared to file-based <i>sudoers</i> See the Sx Differences between LDAP and non-LDAP sudoers section for more information.</p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
