---
title: "slapd-config(5)"
name: "slapd-config"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-config/"
description: "slapd-config – configuration backend to slapd"
---

<p>slapd-config &#8211; configuration backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.d</p>
<h2>Description</h2>
<p>The <code>config</code> backend manages all of the configuration information for the <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) daemon. This configuration information is also used by the SLAPD tools <code><a href="/docs/linux/man/8-slapacl/">slapacl</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapauth/">slapauth</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapdn/">slapdn</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), and <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8). </p>
<p> The <code>config</code> backend is backward compatible with the older <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file but provides the ability to change the configuration dynamically at runtime. If slapd is run with only a <code>slapd.conf</code> file dynamic changes will be allowed but they will not persist across a server restart. Dynamic changes are only saved when slapd is running from a <code>slapd.d</code> configuration directory. </p>
<p> Unlike other backends, there can only be one instance of the <code>config</code> backend, and most of its structure is predefined. The root of the database is hardcoded to <code>cn=config</code> and this root entry contains global settings for slapd. Multiple child entries underneath the root entry are used to carry various other settings:</p>
<dl>
<dd>
<dl>
<dt><code>cn=Module</code></p>
<dd>dynamically loaded modules</p>
<dt><code>cn=Schema</code></p>
<dd>schema definitions</p>
<dt><code>olcBackend=xxx</code></p>
<dd>backend-specific settings</p>
<dt><code>olcDatabase=xxx</code></p>
<dd>database-specific settings</dl>
</dl>
<p> The <code>cn=Module</code> entries will only appear in configurations where slapd was built with support for dynamically loaded modules. There can be multiple entries, one for each configured module path. Within each entry there will be values recorded for each module loaded on a given path. These entries have no children. </p>
<p> The <code>cn=Schema</code> entry contains all of the hardcoded schema elements. The children of this entry contain all user-defined schema elements. In schema that were loaded from include files, the child entry will be named after the include file from which the schema was loaded. Typically the first child in this subtree will be <code>cn=core,cn=schema,cn=config</code>. </p>
<p> <code>olcBackend</code> entries are for storing settings specific to a single backend type (and thus global to all database instances of that type). At present there are no backends that implement settings of this nature, so usually there will not be any olcBackend entries. </p>
<p> <code>olcDatabase</code> entries store settings specific to a single database instance. These entries may have <code>olcOverlay</code> child entries corresponding to any overlays configured on the database. The olcDatabase and olcOverlay entries may also have miscellaneous child entries for other settings as needed. There are two special database entries that are predefined &#8211; one is an entry for the config database itself, and the other is for the &quot;frontend&quot; database. Settings in the frontend database are inherited by the other databases, unless they are explicitly overridden in a specific database. </p>
<p> The specific configuration options available are discussed below in the Global Configuration Options, General Backend Options, and General Database Options. Options are set by defining LDAP attributes with specific values. In general the names of the LDAP attributes are the same as the corresponding <code>slapd.conf</code> keyword, with an &quot;olc&quot; prefix added on. </p>
<p> The parser for many of these attributes is the same as used for parsing the slapd.conf keywords. As such, slapd.conf keywords that allow multiple items to be specified on one line, separated by whitespace, will allow multiple items to be specified in one attribute value. However, when reading the attribute via LDAP, the items will be returned as individual attribute values. </p>
<p> Backend-specific options are discussed in the <code>slapd-&lt;backend&gt;(5)</code> manual pages. Refer to the &quot;OpenLDAP Administrator&#8217;s Guide&quot; for more details on configuring slapd.</p>
<h2>Global Configuration Options</h2>
<p>Options described in this section apply to the server as a whole. Arguments that should be replaced by actual text are shown in brackets &lt;&gt;. </p>
<p> These options may only be specified in the <code>cn=config</code> entry. This entry must have an objectClass of <code>olcGlobal</code>. </p>
<dl>
<dt><code>olcAllows: &lt;features&gt;</code></p>
<dd>Specify a set of features to allow (default none). <code>bind_v2</code> allows acceptance of LDAPv2 bind requests. Note that <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) does not truly implement LDAPv2 (RFC 1777), now Historic (RFC 3494). <code>bind_anon_cred</code> allows anonymous bind when credentials are not empty (e.g. when DN is empty). <code>bind_anon_dn</code> allows unauthenticated (anonymous) bind when DN is not empty. <code>update_anon</code> allows unauthenticated (anonymous) update operations to be processed (subject to access controls and other administrative limits). <code>proxy_authz_anon</code> allows unauthenticated (anonymous) proxy authorization control to be processed (subject to access controls, authorization and other administrative limits).</p>
<dt><code>olcArgsFile: &lt;filename&gt;</code></p>
<dd>The (absolute) name of a file that will hold the <code>slapd</code> server&#8217;s command line (program name and options).</p>
<dt><code>olcAttributeOptions: &lt;option-name&gt;&#8230;</code></p>
<dd>Define tagging attribute options or option tag/range prefixes. Options must not end with `-&#8216;, prefixes must end with `-&#8216;. The `lang-&#8216; prefix is predefined. If you use the <code>olcAttributeOptions</code> directive, `lang-&#8216; will no longer be defined and you must specify it explicitly if you want it defined. </p>
<p> An attribute description with a tagging option is a subtype of that attribute description without the option. Except for that, options defined this way have no special semantics. Prefixes defined this way work like the `lang-&#8216; options: They define a prefix for tagging options starting with the prefix. That is, if you define the prefix `x-foo-&#8216;, you can use the option `x-foo-bar&#8217;. Furthermore, in a search or compare, a prefix or range name (with a trailing `-&#8216;) matches all options starting with that name, as well as the option with the range name sans the trailing `-&#8216;. That is, `x-foo-bar-&#8216; matches `x-foo-bar&#8217; and `x-foo-bar-baz&#8217;. </p>
<p> RFC 4520 reserves options beginning with `x-&#8216; for private experiments. Other options should be registered with IANA, see RFC 4520 section 3.5. OpenLDAP also has the `binary&#8217; option built in, but this is a transfer option, not a tagging option.</p>
<dt><code>olcAuthIDRewrite: &lt;rewrite-rule&gt;</code></p>
<dd>Used by the authentication framework to convert simple user names to an LDAP DN used for authorization purposes. Its purpose is analogous to that of <code>olcAuthzRegexp</code> (see below). The <code>rewrite-rule</code> is a set of rules analogous to those described in <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) for data rewriting (after stripping the <i>rwm-</i> prefix). <code>olcAuthIDRewrite</code> and <code>olcAuthzRegexp</code> should not be intermixed.</p>
<dt><code>olcAuthzPolicy: &lt;policy&gt;</code></p>
<dd>Used to specify which rules to use for Proxy Authorization. Proxy authorization allows a client to authenticate to the server using one user&#8217;s credentials, but specify a different identity to use for authorization and access control purposes. It essentially allows user A to login as user B, using user A&#8217;s password. The <code>none</code> flag disables proxy authorization. This is the default setting. The <code>from</code> flag will use rules in the <i>authzFrom</i> attribute of the authorization DN. The <code>to</code> flag will use rules in the <i>authzTo</i> attribute of the authentication DN. The <code>any</code> flag, an alias for the deprecated value of <code>both</code>, will allow any of the above, whatever succeeds first (checked in <code>to</code>, <code>from</code> sequence. The <code>all</code> flag requires both authorizations to succeed.</dl>
<dl>
<dd>The rules are mechanisms to specify which identities are allowed to perform proxy authorization. The <i>authzFrom</i> attribute in an entry specifies which other users are allowed to proxy login to this entry. The <i>authzTo</i> attribute in an entry specifies which other users this user can authorize as. Use of <i>authzTo</i> rules can be easily abused if users are allowed to write arbitrary values to this attribute. In general the <i>authzTo</i> attribute must be protected with ACLs such that only privileged users can modify it. The value of <i>authzFrom</i> and <i>authzTo</i> describes an <code>identity </code> or a set of identities; it can take five forms:</p>
<dl>
<dd>
<dl>
<dt><code><a href="ldap:///">ldap:///</a>&lt;base&gt;??[&lt;scope&gt;]?&lt;filter&gt;</code></p>
<dd></dl>
</dl>
<dl>
<dd><code>dn[.&lt;dnstyle&gt;]:&lt;pattern&gt;</code></dl>
<dl>
<dd><code>u[&lt;mech&gt;[&lt;realm&gt;]]:&lt;pattern&gt;</code></dl>
<dl>
<dd><code>group[/objectClass[/attributeType]]:&lt;pattern&gt;</code></dl>
<dl>
<dd><code>&lt;pattern&gt;</code></dl>
<dl>
<dd><code>&lt;dnstyle&gt;:={exact|onelevel|children|subtree|regex}</code> </p>
</dl>
<p> The first form is a valid LDAP <code>URI</code> where the <i>&lt;host&gt;:&lt;port&gt;</i>, the <i>&lt;attrs&gt;</i> and the <i>&lt;extensions&gt;</i> portions must be absent, so that the search occurs locally on either <i>authzFrom</i> or <i>authzTo</i>. The second form is a <code>DN</code>, with the optional style modifiers <i>exact</i>, <i>onelevel</i>, <i>children</i>, and <i>subtree</i> for exact, onelevel, children and subtree matches, which cause <i>&lt;pattern&gt;</i> to be normalized according to the DN normalization rules, or the special <i>regex</i> style, which causes the <i>&lt;pattern&gt;</i> to be treated as a POSIX (&#8221;extended&#8221;) regular expression, as discussed in <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7). A pattern of <i>*</i> means any non-anonymous DN. The third form is a SASL <code>id</code>, with the optional fields <i>&lt;mech&gt;</i> and <i>&lt;realm&gt;</i> that allow to specify a SASL <code>mechanism</code>, and eventually a SASL <code>realm</code>, for those mechanisms that support one. The need to allow the specification of a mechanism is still debated, and users are strongly discouraged to rely on this possibility. The fourth form is a group specification, consisting of the keyword <code>group</code>, optionally followed by the specification of the group <code>objectClass</code> and member <code>attributeType</code>. The group with DN <code>&lt;pattern&gt;</code> is searched with base scope, and in case of match, the values of the member <code>attributeType</code> are searched for the asserted DN. For backwards compatibility, if no identity type is provided, i.e. only <code>&lt;pattern&gt;</code> is present, an <i>exact DN</i> is assumed; as a consequence, <code>&lt;pattern&gt;</code> is subjected to DN normalization. Since the interpretation of <i>authzFrom</i> and <i>authzTo</i> can impact security, users are strongly encouraged to explicitly set the type of identity specification that is being used. A subset of these rules can be used as third arg in the <code>olcAuthzRegexp</code> statement (see below); significantly, the <i>URI</i> and the <i>dn.exact:&lt;dn&gt; </i> forms.</dl>
<dl>
<dt><code>olcAuthzRegexp: &lt;match&gt; &lt;replace&gt;</code></p>
<dd>Used by the authentication framework to convert simple user names, such as provided by SASL subsystem, to an LDAP DN used for authorization purposes. Note that the resultant DN need not refer to an existing entry to be considered valid. When an authorization request is received from the SASL subsystem, the SASL <code>USERNAME</code>, <code>REALM</code>, and <code>MECHANISM</code> are taken, when available, and combined into a name of the form</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>UID=&lt;username&gt;[[,CN=&lt;realm&gt;],CN=&lt;mechanism&gt;],CN=auth</code></p>
<dd></dl>
</dl>
<p> This name is then compared against the <code>match</code> POSIX (&#8221;extended&#8221;) regular expression, and if the match is successful, the name is replaced with the <code>replace</code> string. If there are wildcard strings in the <code>match</code> regular expression that are enclosed in parenthesis, e.g.</p>
<dl>
<dd>
<dl>
<dt><code>UID=([^,]*),CN=.*</code></p>
<dd></dl>
</dl>
<p> then the portion of the name that matched the wildcard will be stored in the numbered placeholder variable $1. If there are other wildcard strings in parenthesis, the matching strings will be in $2, $3, etc. up to $9. The placeholders can then be used in the <code>replace</code> string, e.g.</p>
<dl>
<dd>
<dl>
<dt><code>UID=$1,OU=Accounts,DC=example,DC=com </code></p>
<dd></dl>
</dl>
<p> The replaced name can be either a DN, i.e. a string prefixed by &quot;dn:&quot;, or an LDAP URI. If the latter, the server will use the URI to search its own database(s) and, if the search returns exactly one entry, the name is replaced by the DN of that entry. The LDAP URI must have no hostport, attrs, or extensions components, but the filter is mandatory, e.g.</p>
<dl>
<dd>
<dl>
<dt><code><a href="ldap:///OU=Accounts,DC=example,DC=com??one?(UID=$1)">ldap:///OU=Accounts,DC=example,DC=com??one?(UID=$1)</a></code></p>
<dd></dl>
</dl>
<p> The protocol portion of the URI must be strictly <code>ldap</code>. Note that this search is subject to access controls. Specifically, the authentication identity must have &quot;auth&quot; access in the subject. </p>
<p> Multiple <code>olcAuthzRegexp </code> values can be specified to allow for multiple matching and replacement patterns. The matching patterns are checked in the order they appear in the attribute, stopping at the first successful match. </p>
</dl>
<dt><code>olcConcurrency: &lt;integer&gt;</code></p>
<dd>Specify a desired level of concurrency. Provided to the underlying thread system as a hint. The default is not to provide any hint. This setting is only meaningful on some platforms where there is not a one to one correspondence between user threads and kernel threads.</p>
<dt><code>olcConnMaxPending: &lt;integer&gt;</code></p>
<dd>Specify the maximum number of pending requests for an anonymous session. If requests are submitted faster than the server can process them, they will be queued up to this limit. If the limit is exceeded, the session is closed. The default is 100.</p>
<dt><code>olcConnMaxPendingAuth: &lt;integer&gt;</code></p>
<dd>Specify the maximum number of pending requests for an authenticated session. The default is 1000.</p>
<dt><code>olcDisallows: &lt;features&gt;</code></p>
<dd>Specify a set of features to disallow (default none). <code>bind_anon</code> disables acceptance of anonymous bind requests. Note that this setting does not prohibit anonymous directory access (See &quot;require authc&quot;). <code>bind_simple</code> disables simple (bind) authentication. <code>tls_2_anon</code> disables forcing session to anonymous status (see also <code>tls_authc</code>) upon StartTLS operation receipt. <code>tls_authc</code> disallows the StartTLS operation if authenticated (see also <code>tls_2_anon</code>).</p>
<dt><code>olcGentleHUP: { TRUE | FALSE }</code></p>
<dd>A SIGHUP signal will only cause a &#8216;gentle&#8217; shutdown-attempt: <code>Slapd</code> will stop listening for new connections, but will not close the connections to the current clients. Future write operations return unwilling-to-perform, though. Slapd terminates when all clients have closed their connections (if they ever do), or &#8211; as before &#8211; if it receives a SIGTERM signal. This can be useful if you wish to terminate the server and start a new <code>slapd</code> server <code>with another database,</code> without disrupting the currently active clients. The default is FALSE. You may wish to use <code>olcIdleTimeout</code> along with this option.</p>
<dt><code>olcIdleTimeout: &lt;integer&gt;</code></p>
<dd>Specify the number of seconds to wait before forcibly closing an idle client connection. A setting of 0 disables this feature. The default is 0. You may also want to set the <code>olcWriteTimeout</code> option.</p>
<dt><code>olcIndexIntLen: &lt;integer&gt;</code></p>
<dd>Specify the key length for ordered integer indices. The most significant bytes of the binary integer will be used for index keys. The default value is 4, which provides exact indexing for 31 bit values. A floating point representation is used to index too large values.</p>
<dt><code>olcIndexSubstrIfMaxlen: &lt;integer&gt;</code></p>
<dd>Specify the maximum length for subinitial and subfinal indices. Only this many characters of an attribute value will be processed by the indexing functions; any excess characters are ignored. The default is 4.</p>
<dt><code>olcIndexSubstrIfMinlen: &lt;integer&gt;</code></p>
<dd>Specify the minimum length for subinitial and subfinal indices. An attribute value must have at least this many characters in order to be processed by the indexing functions. The default is 2.</p>
<dt><code>olcIndexSubstrAnyLen: &lt;integer&gt;</code></p>
<dd>Specify the length used for subany indices. An attribute value must have at least this many characters in order to be processed. Attribute values longer than this length will be processed in segments of this length. The default is 4. The subany index will also be used in subinitial and subfinal index lookups when the filter string is longer than the <i>olcIndexSubstrIfMaxlen</i> value.</p>
<dt><code>olcIndexSubstrAnyStep: &lt;integer&gt;</code></p>
<dd>Specify the steps used in subany index lookups. This value sets the offset for the segments of a filter string that are processed for a subany index lookup. The default is 2. For example, with the default values, a search using this filter &quot;cn=*abcdefgh*&quot; would generate index lookups for &quot;abcd&quot;, &quot;cdef&quot;, and &quot;efgh&quot;. </p>
</dl>
<p> Note: Indexing support depends on the particular backend in use. Also, changing these settings will generally require deleting any indices that depend on these parameters and recreating them with <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8). </p>
<dl>
<dt><code>olcListenerThreads: &lt;integer&gt;</code></p>
<dd>Specify the number of threads to use for the connection manager. The default is 1 and this is typically adequate for up to 16 CPU cores. The value should be set to a power of 2.</p>
<dt><code>olcLocalSSF: &lt;SSF&gt;</code></p>
<dd>Specifies the Security Strength Factor (SSF) to be given local LDAP sessions, such as those to the ldapi:// listener. For a description of SSF values, see <code>olcSaslSecProps</code>&#8216;s <code>minssf</code> option description. The default is 71.</p>
<dt><code>olcLogFile: &lt;filename&gt;</code></p>
<dd>Specify a file for recording debug log messages. By default these messages only go to stderr and are not recorded anywhere else. Specifying a logfile copies messages to both stderr and the logfile.</p>
<dt><code>olcLogLevel: &lt;integer&gt; [&#8230;]</code></p>
<dd>Specify the level at which debugging statements and operation statistics should be syslogged (currently logged to the <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) LOG_LOCAL4 facility). They must be considered subsystems rather than increasingly verbose log levels. Some messages with higher priority are logged regardless of the configured loglevel as soon as any logging is configured. Log levels are additive, and available levels are:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>1</code></p>
<dd><code>(0x1 trace)</code> trace function calls</p>
<dt><code>2</code></p>
<dd><code>(0x2 packets)</code> debug packet handling</p>
<dt><code>4</code></p>
<dd><code>(0x4 args)</code> heavy trace debugging (function args)</p>
<dt><code>8</code></p>
<dd><code>(0x8 conns)</code> connection management</p>
<dt><code>16</code></p>
<dd><code>(0x10 BER)</code> print out packets sent and received</p>
<dt><code>32</code></p>
<dd><code>(0x20 filter)</code> search filter processing</p>
<dt><code>64</code></p>
<dd><code>(0x40 config)</code> configuration file processing</p>
<dt><code>128</code></p>
<dd><code>(0x80 ACL)</code> access control list processing</p>
<dt><code>256</code></p>
<dd><code>(0x100 stats)</code> stats log connections/operations/results</p>
<dt><code>512</code></p>
<dd><code>(0x200 stats2)</code> stats log entries sent</p>
<dt><code>1024</code></p>
<dd><code>(0x400 shell)</code> print communication with shell backends</p>
<dt><code>2048</code></p>
<dd><code>(0x800 parse)</code> entry parsing</p>
<dt><code>16384</code></p>
<dd><code>(0x4000 sync)</code> LDAPSync replication</p>
<dt><code>32768</code></p>
<dd><code>(0x8000 none)</code> only messages that get logged whatever log level is set</dl>
</dl>
<p> The desired log level can be input as a single integer that combines the (ORed) desired levels, both in decimal or in hexadecimal notation, as a list of integers (that are ORed internally), or as a list of the names that are shown between brackets, such that </p>
<pre> olcLogLevel: 129
 olcLogLevel: 0x81
 olcLogLevel: 128 1
 olcLogLevel: 0x80 0x1
 olcLogLevel: acl trace</pre>
<p>are equivalent. The keyword <code>any</code> can be used as a shortcut to enable logging at all levels (equivalent to -1). The keyword <code>none</code>, or the equivalent integer representation, causes those messages that are logged regardless of the configured olcLogLevel to be logged. In fact, if no olcLogLevel (or a 0 level) is defined, no logging occurs, so at least the <code>none</code> level is required to have high priority messages logged.</dl>
<dt><code>olcPasswordCryptSaltFormat: &lt;format&gt;</code></p>
<dd>Specify the format of the salt passed to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) when generating {CRYPT} passwords (see <code>olcPasswordHash</code>) during processing of LDAP Password Modify Extended Operations (RFC 3062). </p>
<p> This string needs to be in <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) format and may include one (and only one) %s conversion. This conversion will be substituted with a string of random characters from [A-Za-z0-9./]. For example, &quot;%.2s&quot; provides a two character salt and &quot;$1$%.8s&quot; tells some versions of <a href="/docs/linux/man/3-crypt/">crypt</a>(3) to use an MD5 algorithm and provides 8 random characters of salt. The default is &quot;%s&quot;, which provides 31 characters of salt.</p>
<dt><code>olcPidFile: &lt;filename&gt;</code></p>
<dd>The (absolute) name of a file that will hold the <code>slapd</code> server&#8217;s process ID (see <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)).</p>
<dt><code>olcPluginLogFile: &lt;filename&gt;</code></p>
<dd>The ( absolute ) name of a file that will contain log messages from <code>SLAPI</code> plugins. See <code><a href="/docs/linux/man/5-slapd-plugin/">slapd.plugin</a></code>(5) for details.</p>
<dt><code>olcReferral: &lt;url&gt;</code></p>
<dd>Specify the referral to pass back when <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) cannot find a local database to handle a request. If multiple values are specified, each url is provided.</p>
<dt><code>olcReverseLookup: TRUE | FALSE</code></p>
<dd>Enable/disable client name unverified reverse lookup (default is <code>FALSE</code> if compiled with &#8211;enable-rlookups).</p>
<dt><code>olcRootDSE: &lt;file&gt;</code></p>
<dd>Specify the name of an <a href="/docs/linux/man/5-ldif/">LDIF</a>(5) file containing user defined attributes for the root DSE. These attributes are returned in addition to the attributes normally produced by slapd. </p>
<p> The root DSE is an entry with information about the server and its capabilities, in operational attributes. It has the empty DN, and can be read with e.g.:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> ldapsearch -x -b &quot;&quot; -s base &quot;+&quot;<br />
 See RFC 4512 section 5.1 for details.</p>
<dt><code>olcSaslAuxprops: &lt;plugin&gt; [&#8230;]</code></p>
<dd>Specify which auxprop plugins to use for authentication lookups. The default is empty, which just uses slapd&#8217;s internal support. Usually no other auxprop plugins are needed.</p>
<dt><code>olcSaslHost: &lt;fqdn&gt;</code></p>
<dd>Used to specify the fully qualified domain name used for SASL processing.</p>
<dt><code>olcSaslRealm: &lt;realm&gt;</code></p>
<dd>Specify SASL realm. Default is empty.</p>
<dt><code>olcSaslSecProps: &lt;properties&gt;</code></p>
<dd>Used to specify Cyrus SASL security properties. The <code>none</code> flag (without any other properties) causes the flag properties default, &quot;noanonymous,noplain&quot;, to be cleared. The <code>noplain</code> flag disables mechanisms susceptible to simple passive attacks. The <code>noactive</code> flag disables mechanisms susceptible to active attacks. The <code>nodict</code> flag disables mechanisms susceptible to passive dictionary attacks. The <code>noanonymous</code> flag disables mechanisms which support anonymous login. The <code>forwardsec</code> flag require forward secrecy between sessions. The <code>passcred</code> require mechanisms which pass client credentials (and allow mechanisms which can pass credentials to do so). The <code>minssf=&lt;factor&gt; </code> property specifies the minimum acceptable <i>security strength factor</i> as an integer approximate to effective key length used for encryption. 0 (zero) implies no protection, 1 implies integrity protection only, 56 allows DES or other weak ciphers, 112 allows triple DES and other strong ciphers, 128 allows RC4, Blowfish and other modern strong ciphers. The default is 0. The <code>maxssf=&lt;factor&gt; </code> property specifies the maximum acceptable <i>security strength factor</i> as an integer (see minssf description). The default is INT_MAX. The <code>maxbufsize=&lt;size&gt; </code> property specifies the maximum security layer receive buffer size allowed. 0 disables security layers. The default is 65536.</p>
<dt><code>olcServerID: &lt;integer&gt; [&lt;URL&gt;]</code></p>
<dd>Specify an integer ID from 0 to 4095 for this server (limited to 3 hexadecimal digits). The ID may also be specified as a hexadecimal ID by prefixing the value with &quot;0x&quot;. These IDs are required when using multimaster replication and each master must have a unique ID. Note that this requirement also applies to separate masters contributing to a glued set of databases. If the URL is provided, this directive may be specified multiple times, providing a complete list of participating servers and their IDs. The fully qualified hostname of each server should be used in the supplied URLs. The IDs are used in the &quot;replica id&quot; field of all CSNs generated by the specified server. The default value is zero. Example:</dl>
<pre> olcServerID: 1 <a href="ldap://ldap1.example.com">ldap://ldap1.example.com</a>
 olcServerID: 2 <a href="ldap://ldap2.example.com">ldap://ldap2.example.com</a></pre>
<dl>
<dt><code>olcSockbufMaxIncoming: &lt;integer&gt;</code></p>
<dd>Specify the maximum incoming LDAP PDU size for anonymous sessions. The default is 262143.</p>
<dt><code>olcSockbufMaxIncomingAuth: &lt;integer&gt;</code></p>
<dd>Specify the maximum incoming LDAP PDU size for authenticated sessions. The default is 4194303.</p>
<dt><code>olcTCPBuffer [listener=&lt;URL&gt;] [{read|write}=]&lt;size&gt;</code></p>
<dd>Specify the size of the TCP buffer. A global value for both read and write TCP buffers related to any listener is defined, unless the listener is explicitly specified, or either the read or write qualifiers are used. See <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7) for details. Note that some OS-es implement automatic TCP buffer tuning.</p>
<dt><code>olcThreads: &lt;integer&gt;</code></p>
<dd>Specify the maximum size of the primary thread pool. The default is 16; the minimum value is 2.</p>
<dt><code>olcToolThreads: &lt;integer&gt;</code></p>
<dd>Specify the maximum number of threads to use in tool mode. This should not be greater than the number of CPUs in the system. The default is 1.</p>
<dt><code>olcWriteTimeout: &lt;integer&gt;</code></p>
<dd>Specify the number of seconds to wait before forcibly closing a connection with an outstanding write. This allows recovery from various network hang conditions. A setting of 0 disables this feature. The default is 0.</dl>
<h2>Tls Options</h2>
<p>If <code>slapd</code> is built with support for Transport Layer Security, there are more options you can specify.</p>
<dl>
<dt><code>olcTLSCipherSuite: &lt;cipher-suite-spec&gt;</code></p>
<dd>Permits configuring what ciphers will be accepted and the preference order. &lt;cipher-suite-spec&gt; should be a cipher specification for the TLS library in use (OpenSSL, GnuTLS, or Mozilla NSS). Example:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><i>OpenSSL:</i></p>
<dd>olcTLSCipherSuite: HIGH:MEDIUM:+SSLv2</p>
<dt><i>GnuTLS:</i></p>
<dd>TLSCiphersuite SECURE256:!AES-128-CBC</dl>
</dl>
<p> To check what ciphers a given spec selects in OpenSSL, use: </p>
<pre> openssl ciphers -v &lt;cipher-suite-spec&gt;</pre>
<p>With GnuTLS the available specs can be found in the manual page of <code><a href="/docs/linux/man/1-gnutls-cli/">gnutls-cli</a></code>(1) (see the description of the option <code>&#8211;priority</code>). </p>
<p> In older versions of GnuTLS, where gnutls-cli does not support the option &#8211;priority, you can obtain the &#8212; more limited &#8212; list of ciphers by calling: </p>
<pre> gnutls-cli -l</pre>
<p>When using Mozilla NSS, the OpenSSL cipher suite specifications are used and translated into the format used internally by Mozilla NSS. There isn&#8217;t an easy way to list the cipher suites from the command line. The authoritative list is in the source code for Mozilla NSS in the file sslinfo.c in the structure </p>
<pre> static const SSLCipherSuiteInfo suiteInfo[]</pre>
</dl>
<dt><code>olcTLSCACertificateFile: &lt;filename&gt;</code></p>
<dd>Specifies the file that contains certificates for all of the Certificate Authorities that <code>slapd</code> will recognize.</p>
<dt><code>olcTLSCACertificatePath: &lt;path&gt;</code></p>
<dd>Specifies the path of a directory that contains Certificate Authority certificates in separate individual files. Usually only one of this or the olcTLSCACertificateFile is defined. If both are specified, both locations will be used. This directive is not supported when using GnuTLS. </p>
<p> When using Mozilla NSS, &lt;path&gt; may contain a Mozilla NSS cert/key database. If &lt;path&gt; contains a Mozilla NSS cert/key database and CA cert files, OpenLDAP will use the cert/key database and will ignore the CA cert files.</p>
<dt><code>olcTLSCertificateFile: &lt;filename&gt;</code></p>
<dd>Specifies the file that contains the <code>slapd</code> server certificate. </p>
<p> When using Mozilla NSS, if using a cert/key database (specified with olcTLSCACertificatePath), olcTLSCertificateFile specifies the name of the certificate to use: </p>
<pre> olcTLSCertificateFile: Server-Cert</pre>
<p>If using a token other than the internal built in token, specify the token name first, followed by a colon: </p>
<pre> olcTLSCertificateFile: my hardware device:Server-Cert</pre>
<p>Use certutil -L to list the certificates by name: </p>
<pre> certutil -d /path/to/certdbdir -L</pre>
<dt><code>olcTLSCertificateKeyFile: &lt;filename&gt;</code></p>
<dd>Specifies the file that contains the <code>slapd</code> server private key that matches the certificate stored in the <code>olcTLSCertificateFile</code> file. If the private key is protected with a password, the password must be manually typed in when slapd starts. Usually the private key is not protected with a password, to allow slapd to start without manual intervention, so it is of critical importance that the file is protected carefully. </p>
<p> When using Mozilla NSS, olcTLSCertificateKeyFile specifies the name of a file that contains the password for the key for the certificate specified with olcTLSCertificateFile. The modutil command can be used to turn off password protection for the cert/key database. For example, if olcTLSCACertificatePath specifes /etc/openldap/certdb as the location of the cert/key database, use modutil to change the password to the empty string: </p>
<pre> modutil -dbdir /etc/openldap/certdb -changepw 'NSS Certificate DB'</pre>
<p>You must have the old password, if any. Ignore the WARNING about the running browser. Press &#8216;Enter&#8217; for the new password. </p>
<dt><code>olcTLSDHParamFile: &lt;filename&gt;</code></p>
<dd>This directive specifies the file that contains parameters for Diffie-Hellman ephemeral key exchange. This is required in order to use a DSA certificate on the server. If multiple sets of parameters are present in the file, all of them will be processed. Note that setting this option may also enable Anonymous Diffie-Hellman key exchanges in certain non-default cipher suites. You should append &quot;!ADH&quot; to your cipher suites if you have changed them from the default, otherwise no certificate exchanges or verification will be done. When using GnuTLS or Mozilla NSS these parameters are always generated randomly so this directive is ignored.</p>
<dt><code>olcTLSProtocolMin: &lt;major&gt;[.&lt;minor&gt;]</code></p>
<dd>Specifies minimum SSL/TLS protocol version that will be negotiated. If the server doesn&#8217;t support at least that version, the SSL handshake will fail. To require TLS 1.x or higher, set this option to 3.(x+1), e.g., </p>
<pre> olcTLSProtocolMin: 3.2</pre>
<p>would require TLS 1.1. Specifying a minimum that is higher than that supported by the OpenLDAP implementation will result in it requiring the highest level that it does support. This directive is ignored with GnuTLS.</p>
<dt><code>olcTLSRandFile: &lt;filename&gt;</code></p>
<dd>Specifies the file to obtain random bits from when /dev/[u]random is not available. Generally set to the name of the EGD/PRNGD socket. The environment variable RANDFILE can also be used to specify the filename. This directive is ignored with GnuTLS and Mozilla NSS.</p>
<dt><code>olcTLSVerifyClient: &lt;level&gt;</code></p>
<dd>Specifies what checks to perform on client certificates in an incoming TLS session, if any. The <code>&lt;level&gt;</code> can be specified as one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>never</code></p>
<dd>This is the default. <code>slapd</code> will not ask the client for a certificate.</p>
<dt><code>allow</code></p>
<dd>The client certificate is requested. If no certificate is provided, the session proceeds normally. If a bad certificate is provided, it will be ignored and the session proceeds normally.</p>
<dt><code>try</code></p>
<dd>The client certificate is requested. If no certificate is provided, the session proceeds normally. If a bad certificate is provided, the session is immediately terminated.</p>
<dt><code>demand | hard | true</code></p>
<dd>These keywords are all equivalent, for compatibility reasons. The client certificate is requested. If no certificate is provided, or a bad certificate is provided, the session is immediately terminated. </p>
<p> Note that a valid client certificate is required in order to use the SASL EXTERNAL authentication mechanism with a TLS session. As such, a non-default <code>olcTLSVerifyClient</code> setting must be chosen to enable SASL EXTERNAL authentication.</dl>
</dl>
<dt><code>olcTLSCRLCheck: &lt;level&gt;</code></p>
<dd>Specifies if the Certificate Revocation List (CRL) of the CA should be used to verify if the client certificates have not been revoked. This requires <code>olcTLSCACertificatePath</code> parameter to be set. This parameter is ignored with GnuTLS and Mozilla NSS. <code>&lt;level&gt;</code> can be specified as one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>No CRL checks are performed</p>
<dt><code>peer</code></p>
<dd>Check the CRL of the peer certificate</p>
<dt><code>all</code></p>
<dd>Check the CRL for a whole certificate chain</dl>
</dl>
<dt><code>olcTLSCRLFile: &lt;filename&gt;</code></p>
<dd>Specifies a file containing a Certificate Revocation List to be used for verifying that certificates have not been revoked. This parameter is only valid when using GnuTLS or Mozilla NSS.</dl>
<h2>Dynamic Module Options</h2>
<p>If <code>slapd</code> is compiled with &#8211;enable-modules then the module-related entries will be available. These entries are named <code>cn=module{x},cn=config</code> and must have the olcModuleList objectClass. One entry should be created per <code>olcModulePath.</code> Normally the config engine generates the &quot;{x}&quot; index in the RDN automatically, so it can be omitted when initially loading these entries.</p>
<dl>
<dt><code>olcModuleLoad: &lt;filename&gt;</code></p>
<dd>Specify the name of a dynamically loadable module to load. The filename may be an absolute path name or a simple filename. Non-absolute names are searched for in the directories specified by the <code>olcModulePath</code> option.</p>
<dt><code>olcModulePath: &lt;pathspec&gt;</code></p>
<dd>Specify a list of directories to search for loadable modules. Typically the path is colon-separated but this depends on the operating system. The default is /usr/lib64/openldap, which is where the standard OpenLDAP install will place its modules.</dl>
<h2>Schema Options</h2>
<p>Schema definitions are created as entries in the <code>cn=schema,cn=config</code> subtree. These entries must have the olcSchemaConfig objectClass. As noted above, the actual <code>cn=schema,cn=config</code> entry is predefined and any values specified for it are ignored. </p>
<dl>
<dt> <code>olcAttributetypes: (&nbsp;<wbr>&lt;oid&gt;<br />
&nbsp;<wbr>[NAME&nbsp;<wbr>&lt;name&gt;]&nbsp;<wbr>[DESC&nbsp;<wbr>&lt;description&gt;]&nbsp;<wbr>[OBSOLETE]&nbsp;<wbr>[SUP&nbsp;<wbr>&lt;oid&gt;]&nbsp;<wbr>[EQUALITY&nbsp;<wbr>&lt;oid&gt;]&nbsp;<wbr>[ORDERING&nbsp;<wbr>&lt;oid&gt;]&nbsp;<wbr>[SUBSTR&nbsp;<wbr>&lt;oid&gt;]&nbsp;<wbr>[SYNTAX&nbsp;<wbr>&lt;oidlen&gt;]&nbsp;<wbr>[SINGLE-VALUE]&nbsp;<wbr>[COLLECTIVE]&nbsp;<wbr>[NO-USER-MODIFICATION]&nbsp;<wbr>[USAGE&nbsp;<wbr>&lt;attributeUsage&gt;]&nbsp;<wbr>)</code></p>
<dl>
<dd>
<dd>Specify an attribute type using the LDAPv3 syntax defined in RFC 4512. The slapd parser extends the RFC 4512 definition by allowing string forms as well as numeric OIDs to be used for the attribute OID and attribute syntax OID. (See the <code>olcObjectIdentifier</code> description.)</dl>
<dt> <code>olcDitContentRules: (&nbsp;<wbr>&lt;oid&gt;<br />
&nbsp;<wbr>[NAME&nbsp;<wbr>&lt;name&gt;]&nbsp;<wbr>[DESC&nbsp;<wbr>&lt;description&gt;]&nbsp;<wbr>[OBSOLETE]&nbsp;<wbr>[AUX&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>[MUST&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>[MAY&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>[NOT&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>)</code></p>
<dl>
<dd>
<dd>Specify an DIT Content Rule using the LDAPv3 syntax defined in RFC 4512. The slapd parser extends the RFC 4512 definition by allowing string forms as well as numeric OIDs to be used for the attribute OID and attribute syntax OID. (See the <code>olcObjectIdentifier</code> description.)</dl>
<dt> <code>olcObjectClasses: (&nbsp;<wbr>&lt;oid&gt;<br />
&nbsp;<wbr>[NAME&nbsp;<wbr>&lt;name&gt;]&nbsp;<wbr>[DESC&nbsp;<wbr>&lt;description&gt;]&nbsp;<wbr>[OBSOLETE]&nbsp;<wbr>[SUP&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>[{&nbsp;<wbr>ABSTRACT | STRUCTURAL | AUXILIARY&nbsp;<wbr>}]&nbsp;<wbr>[MUST&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>[MAY&nbsp;<wbr>&lt;oids&gt;]&nbsp;<wbr>)</code></p>
<dl>
<dd>
<dd>Specify an objectclass using the LDAPv3 syntax defined in RFC 4512. The slapd parser extends the RFC 4512 definition by allowing string forms as well as numeric OIDs to be used for the object class OID. (See the <code>olcObjectIdentifier</code> description.) Object classes are &quot;STRUCTURAL&quot; by default.</dl>
<dt><code>olcObjectIdentifier: &lt;name&gt; { &lt;oid&gt; | &lt;name&gt;[:&lt;suffix&gt;] }</code></p>
<dd>Define a string name that equates to the given OID. The string can be used in place of the numeric OID in objectclass and attribute definitions. The name can also be used with a suffix of the form &quot;:xx&quot; in which case the value &quot;oid.xx&quot; will be used. </p>
</dl>
<h2>General Backend Options</h2>
<p>Options in these entries only apply to the configuration of a single type of backend. All backends may support this class of options, but currently none do. The entry must be named <code>olcBackend=&lt;databasetype&gt;,cn=config</code> and must have the olcBackendConfig objectClass. &lt;databasetype&gt; should be one of <code>bdb</code>, <code>config</code>, <code>dnssrv</code>, <code>hdb</code>, <code>ldap</code>, <code>ldif</code>, <code>mdb</code>, <code>meta</code>, <code>monitor</code>, <code>ndb</code>, <code>null</code>, <code>passwd</code>, <code>perl</code>, <code>relay</code>, <code>shell</code>, or <code>sql</code>. At present, no backend implements any options of this type, so this entry should not be used.</p>
<h2>Database Options</h2>
<p>Database options are set in entries named <code>olcDatabase={x}&lt;databasetype&gt;,cn=config</code> and must have the olcDatabaseConfig objectClass. Normally the config engine generates the &quot;{x}&quot; index in the RDN automatically, so it can be omitted when initially loading these entries. </p>
<p> The special frontend database is always numbered &quot;{-1}&quot; and the config database is always numbered &quot;{0}&quot;.</p>
<h2>Global Database Options</h2>
<p>Options in this section may be set in the special &quot;frontend&quot; database and inherited in all the other databases. These options may be altered by further settings in each specific database. The frontend entry must be named <code>olcDatabase=frontend,cn=config</code> and must have the olcFrontendConfig objectClass.</p>
<dl>
<dt><code>olcAccess: to &lt;what&gt; [ by &lt;who&gt; &lt;access&gt; &lt;control&gt; ]+</code></p>
<dd>Grant access (specified by &lt;access&gt;) to a set of entries and/or attributes (specified by &lt;what&gt;) by one or more requestors (specified by &lt;who&gt;). If no access controls are present, the default policy allows anyone and everyone to read anything but restricts updates to rootdn. (e.g., &quot;olcAccess: to * by * read&quot;). See <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5) and the &quot;OpenLDAP Administrator&#8217;s Guide&quot; for details. </p>
<p> Access controls set in the frontend are appended to any access controls set on the specific databases. The rootdn of a database can always read and write EVERYTHING in that database. </p>
<p> Extra special care must be taken with the access controls on the config database. Unlike other databases, the default policy for the config database is to only allow access to the rootdn. Regular users should not have read access, and write access should be granted very carefully to privileged administrators. </p>
<dt><code>olcDefaultSearchBase: &lt;dn&gt;</code></p>
<dd>Specify a default search base to use when client submits a non-base search request with an empty base DN. Base scoped search requests with an empty base DN are not affected. This setting is only allowed in the frontend entry.</p>
<dt><code>olcExtraAttrs: &lt;attr&gt;</code></p>
<dd>Lists what attributes need to be added to search requests. Local storage backends return the entire entry to the frontend. The frontend takes care of only returning the requested attributes that are allowed by ACLs. However, features like access checking and so may need specific attributes that are not automatically returned by remote storage backends, like proxy backends and so on. <code>&lt;attr&gt;</code> is an attribute that is needed for internal purposes and thus always needs to be collected, even when not explicitly requested by clients. This attribute is multi-valued.</p>
<dt><code>olcPasswordHash: &lt;hash&gt; [&lt;hash&gt;&#8230;]</code></p>
<dd>This option configures one or more hashes to be used in generation of user passwords stored in the userPassword attribute during processing of LDAP Password Modify Extended Operations (RFC 3062). The &lt;hash&gt; must be one of <code>{SSHA}</code>, <code>{SHA}</code>, <code>{SMD5}</code>, <code>{MD5}</code>, <code>{CRYPT}</code>, and <code>{CLEARTEXT}</code>. The default is <code>{SSHA}</code>. </p>
<p> <code>{SHA}</code> and <code>{SSHA}</code> use the SHA-1 algorithm (FIPS 160-1), the latter with a seed. </p>
<p> <code>{MD5}</code> and <code>{SMD5}</code> use the MD5 algorithm (RFC 1321), the latter with a seed. </p>
<p> <code>{CRYPT}</code> uses the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). </p>
<p> <code>{CLEARTEXT}</code> indicates that the new password should be added to userPassword as clear text. </p>
<p> Note that this option does not alter the normal user applications handling of userPassword during LDAP Add, Modify, or other LDAP operations. This setting is only allowed in the frontend entry.</p>
<dt><code>olcReadOnly: TRUE | FALSE</code></p>
<dd>This option puts the database into &quot;read-only&quot; mode. Any attempts to modify the database will return an &quot;unwilling to perform&quot; error. By default, olcReadOnly is FALSE. Note that when this option is set TRUE on the frontend, it cannot be reset without restarting the server, since further writes to the config database will be rejected.</p>
<dt><code>olcRequires: &lt;conditions&gt;</code></p>
<dd>Specify a set of conditions to require (default none). The directive may be specified globally and/or per-database; databases inherit global conditions, so per-database specifications are additive. <code>bind</code> requires bind operation prior to directory operations. <code>LDAPv3</code> requires session to be using LDAP version 3. <code>authc</code> requires authentication prior to directory operations. <code>SASL</code> requires SASL authentication prior to directory operations. <code>strong</code> requires strong authentication prior to directory operations. The strong keyword allows protected &quot;simple&quot; authentication as well as SASL authentication. <code>none</code> may be used to require no conditions (useful to clear out globally set conditions within a particular database); it must occur first in the list of conditions.</p>
<dt><code>olcRestrict: &lt;oplist&gt;</code></p>
<dd>Specify a list of operations that are restricted. Restrictions on a specific database override any frontend setting. Operations can be any of <code>add</code>, <code>bind</code>, <code>compare</code>, <code>delete</code>, <code>extended[=&lt;OID&gt;]</code>, <code>modify</code>, <code>rename</code>, <code>search</code>, or the special pseudo-operations <code>read</code> and <code>write</code>, which respectively summarize read and write operations. The use of <i>restrict write</i> is equivalent to <i>olcReadOnly: TRUE</i> (see above). The <code>extended</code> keyword allows to indicate the OID of the specific operation to be restricted.</p>
<dt><code>olcSchemaDN: &lt;dn&gt;</code></p>
<dd>Specify the distinguished name for the subschema subentry that controls the entries on this server. The default is &quot;cn=Subschema&quot;.</p>
<dt><code>olcSecurity: &lt;factors&gt;</code></p>
<dd>Specify a set of security strength factors (separated by white space) to require (see <code>olcSaslSecprops</code>&#8216;s <code>minssf</code> option for a description of security strength factors). The directive may be specified globally and/or per-database. <code>ssf=&lt;n&gt;</code> specifies the overall security strength factor. <code>transport=&lt;n&gt;</code> specifies the transport security strength factor. <code>tls=&lt;n&gt;</code> specifies the TLS security strength factor. <code>sasl=&lt;n&gt;</code> specifies the SASL security strength factor. <code>update_ssf=&lt;n&gt;</code> specifies the overall security strength factor to require for directory updates. <code>update_transport=&lt;n&gt;</code> specifies the transport security strength factor to require for directory updates. <code>update_tls=&lt;n&gt;</code> specifies the TLS security strength factor to require for directory updates. <code>update_sasl=&lt;n&gt;</code> specifies the SASL security strength factor to require for directory updates. <code>simple_bind=&lt;n&gt;</code> specifies the security strength factor required for <i>simple</i> username/password authentication. Note that the <code>transport</code> factor is measure of security provided by the underlying transport, e.g. ldapi:// (and eventually IPSEC). It is not normally used.</p>
<dt><code>olcSizeLimit: {&lt;integer&gt;|unlimited}</code></p>
<dd>
<dt><code>olcSizeLimit: size[.{soft|hard|unchecked}]=&lt;integer&gt; [&#8230;]</code></p>
<dd>Specify the maximum number of entries to return from a search operation. The default size limit is 500. Use <code>unlimited</code> to specify no limits. The second format allows a fine grain setting of the size limits. Extra args can be added in the same value or as additional values. See <code>olcLimits</code> for an explanation of the different flags.</p>
<dt><code>olcSortVals: &lt;attr&gt; [&#8230;]</code></p>
<dd>Specify a list of multi-valued attributes whose values will always be maintained in sorted order. Using this option will allow Modify, Compare, and filter evaluations on these attributes to be performed more efficiently. The resulting sort order depends on the attributes&#8217; syntax and matching rules and may not correspond to lexical order or any other recognizable order. This setting is only allowed in the frontend entry.</p>
<dt><code>olcTimeLimit: {&lt;integer&gt;|unlimited}</code></p>
<dd>
<dt><code>olcTimeLimit: time[.{soft|hard}]=&lt;integer&gt; [&#8230;]</code></p>
<dd>Specify the maximum number of seconds (in real time) <code>slapd</code> will spend answering a search request. The default time limit is 3600. Use <code>unlimited</code> to specify no limits. The second format allows a fine grain setting of the time limits. Extra args can be added in the same value or as additional values. See <code>olcLimits</code> for an explanation of the different flags. </p>
</dl>
<h2>General Database Options</h2>
<p>Options in this section only apply to the specific database for which they are defined. They are supported by every type of backend. All of the Global Database Options may also be used here.</p>
<dl>
<dt><code>olcAddContentAcl: TRUE | FALSE</code></p>
<dd>Controls whether Add operations will perform ACL checks on the content of the entry being added. This check is off by default. See the <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5) manual page for more details on ACL requirements for Add operations.</p>
<dt><code>olcHidden: TRUE | FALSE</code></p>
<dd>Controls whether the database will be used to answer queries. A database that is hidden will never be selected to answer any queries, and any suffix configured on the database will be ignored in checks for conflicts with other databases. By default, olcHidden is FALSE.</p>
<dt><code>olcLastMod: TRUE | FALSE</code></p>
<dd>Controls whether <code>slapd</code> will automatically maintain the modifiersName, modifyTimestamp, creatorsName, and createTimestamp attributes for entries. It also controls the entryCSN and entryUUID attributes, which are needed by the syncrepl provider. By default, olcLastMod is TRUE.</p>
<dt><code>olcLimits: &lt;selector&gt; &lt;limit&gt; [&lt;limit&gt; [&#8230;]]</code></p>
<dd>Specify time and size limits based on the operation&#8217;s initiator or base DN. The argument <code>&lt;selector&gt;</code> can be any of</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>anonymous | users | [&lt;dnspec&gt;=]&lt;pattern&gt; | group[/oc[/at]]=&lt;pattern&gt;</p>
<dd></dl>
</dl>
<p> with</p>
<dl>
<dd>
<dl>
<dt>&lt;dnspec&gt; ::= dn[.&lt;type&gt;][.&lt;style&gt;]</p>
<dd>
<dt>&lt;type&gt; ::= self | this</p>
<dd>
<dt>&lt;style&gt; ::= exact | base | onelevel | subtree | children | regex | anonymous</p>
<dd></dl>
</dl>
<p> DN type <code>self</code> is the default and means the bound user, while <code>this</code> means the base DN of the operation. The term <code>anonymous</code> matches all unauthenticated clients. The term <code>users</code> matches all authenticated clients; otherwise an <code>exact</code> dn pattern is assumed unless otherwise specified by qualifying the (optional) key string <code>dn</code> with <code>exact</code> or <code>base</code> (which are synonyms), to require an exact match; with <code>onelevel</code>, to require exactly one level of depth match; with <code>subtree</code>, to allow any level of depth match, including the exact match; with <code>children</code>, to allow any level of depth match, not including the exact match; <code>regex</code> explicitly requires the (default) match based on POSIX (&#8221;extended&#8221;) regular expression pattern. Finally, <code>anonymous</code> matches unbound operations; the <code>pattern</code> field is ignored. The same behavior is obtained by using the <code>anonymous</code> form of the <code>&lt;selector&gt;</code> clause. The term <code>group</code>, with the optional objectClass <code>oc</code> and attributeType <code>at</code> fields, followed by <code>pattern</code>, sets the limits for any DN listed in the values of the <code>at</code> attribute (default <code>member</code>) of the <code>oc</code> group objectClass (default <code>groupOfNames</code>) whose DN exactly matches <code>pattern</code>. </p>
<p> The currently supported limits are <code>size</code> and <code>time</code>. </p>
<p> The syntax for time limits is <code>time[.{soft|hard}]=&lt;integer&gt;</code>, where <i>integer</i> is the number of seconds slapd will spend answering a search request. If no time limit is explicitly requested by the client, the <code>soft</code> limit is used; if the requested time limit exceeds the <code>hard</code> limit, the value of the limit is used instead. If the <code>hard</code> limit is set to the keyword <i>soft</i>, the soft limit is used in either case; if it is set to the keyword <i>unlimited</i>, no hard limit is enforced. Explicit requests for time limits smaller or equal to the <code>hard</code> limit are honored. If no limit specifier is set, the value is assigned to the <code>soft</code> limit, and the <code>hard</code> limit is set to <i>soft</i>, to preserve the original behavior. </p>
<p> The syntax for size limits is <code>size[.{soft|hard|unchecked}]=&lt;integer&gt;</code>, where <i>integer</i> is the maximum number of entries slapd will return answering a search request. If no size limit is explicitly requested by the client, the <code>soft</code> limit is used; if the requested size limit exceeds the <code>hard</code> limit, the value of the limit is used instead. If the <code>hard</code> limit is set to the keyword <i>soft</i>, the soft limit is used in either case; if it is set to the keyword <i>unlimited</i>, no hard limit is enforced. Explicit requests for size limits smaller or equal to the <code>hard</code> limit are honored. The <code>unchecked</code> specifier sets a limit on the number of candidates a search request is allowed to examine. The rationale behind it is that searches for non-properly indexed attributes may result in large sets of candidates, which must be examined by <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) to determine whether they match the search filter or not. The <code>unchecked</code> limit provides a means to drop such operations before they are even started. If the selected candidates exceed the <code>unchecked</code> limit, the search will abort with <i>Unwilling to perform</i>. If it is set to the keyword <i>unlimited</i>, no limit is applied (the default). If it is set to <i>disable</i>, the search is not even performed; this can be used to disallow searches for a specific set of users. If no limit specifier is set, the value is assigned to the <code>soft</code> limit, and the <code>hard</code> limit is set to <i>soft</i>, to preserve the original behavior. </p>
<p> In case of no match, the global limits are used. The default values are the same as for <code>olcSizeLimit</code> and <code>olcTimeLimit</code>; no limit is set on <code>unchecked</code>. </p>
<p> If <code>pagedResults</code> control is requested, the <code>hard</code> size limit is used by default, because the request of a specific page size is considered an explicit request for a limitation on the number of entries to be returned. However, the size limit applies to the total count of entries returned within the search, and not to a single page. Additional size limits may be enforced; the syntax is <code>size.pr={&lt;integer&gt;|noEstimate|unlimited}</code>, where <i>integer</i> is the max page size if no explicit limit is set; the keyword <i>noEstimate</i> inhibits the server from returning an estimate of the total number of entries that might be returned (note: the current implementation does not return any estimate). The keyword <i>unlimited</i> indicates that no limit is applied to the pagedResults control page size. The syntax <code>size.prtotal={&lt;integer&gt;|unlimited|disabled}</code> allows to set a limit on the total number of entries that a pagedResults control allows to return. By default it is set to the <code>hard</code> limit. When set, <i>integer</i> is the max number of entries that the whole search with pagedResults control can return. Use <i>unlimited</i> to allow unlimited number of entries to be returned, e.g. to allow the use of the pagedResults control as a means to circumvent size limitations on regular searches; the keyword <i>disabled</i> disables the control, i.e. no paged results can be returned. Note that the total number of entries returned when the pagedResults control is requested cannot exceed the <code>hard </code> size limit of regular searches unless extended by the <code>prtotal</code> switch.</dl>
<dt><code>olcMaxDerefDepth: &lt;depth&gt;</code></p>
<dd>Specifies the maximum number of aliases to dereference when trying to resolve an entry, used to avoid infinite alias loops. The default is 15.</p>
<dt><code>olcMirrorMode: TRUE | FALSE</code></p>
<dd>This option puts a replica database into &quot;mirror&quot; mode. Update operations will be accepted from any user, not just the updatedn. The database must already be configured as syncrepl consumer before this keyword may be set. This mode also requires a <code>olcServerID</code> (see above) to be configured. By default, this setting is FALSE.</p>
<dt><code>olcPlugin: &lt;plugin_type&gt; &lt;lib_path&gt; &lt;init_function&gt; [&lt;arguments&gt;]</code></p>
<dd>Configure a SLAPI plugin. See the <code><a href="/docs/linux/man/5-slapd-plugin/">slapd.plugin</a></code>(5) manpage for more details.</p>
<dt><code>olcRootDN: &lt;dn&gt;</code></p>
<dd>Specify the distinguished name that is not subject to access control or administrative limit restrictions for operations on this database. This DN may or may not be associated with an entry. An empty root DN (the default) specifies no root access is to be granted. It is recommended that the rootdn only be specified when needed (such as when initially populating a database). If the rootdn is within a namingContext (suffix) of the database, a simple bind password may also be provided using the <code>olcRootPW</code> directive. Note that the rootdn is always needed when using syncrepl. The <code>olcRootDN</code> of the <code>cn=config</code> database defaults to <code>cn=config</code> itself.</p>
<dt><code>olcRootPW: &lt;password&gt;</code></p>
<dd>Specify a password (or hash of the password) for the rootdn. The password can only be set if the rootdn is within the namingContext (suffix) of the database. This option accepts all RFC 2307 userPassword formats known to the server (see <code>olcPasswordHash</code> description) as well as cleartext. <code><a href="/docs/linux/man/8-slappasswd/">slappasswd</a></code>(8) may be used to generate a hash of a password. Cleartext and <code>{CRYPT}</code> passwords are not recommended. If empty (the default), authentication of the root DN is by other means (e.g. SASL). Use of SASL is encouraged.</p>
<dt><code>olcSubordinate: [TRUE | FALSE | advertise]</code></p>
<dd>Specify that the current backend database is a subordinate of another backend database. A subordinate database may have only one suffix. This option may be used to glue multiple databases into a single namingContext. If the suffix of the current database is within the namingContext of a superior database, searches against the superior database will be propagated to the subordinate as well. All of the databases associated with a single namingContext should have identical rootdns. Behavior of other LDAP operations is unaffected by this setting. In particular, it is not possible to use moddn to move an entry from one subordinate to another subordinate within the namingContext. </p>
<p> If the optional <code>advertise</code> flag is supplied, the naming context of this database is advertised in the root DSE. The default is to hide this database context, so that only the superior context is visible. </p>
<p> If the slap tools <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), or <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8) are used on the superior database, any glued subordinates that support these tools are opened as well. </p>
<p> Databases that are glued together should usually be configured with the same indices (assuming they support indexing), even for attributes that only exist in some of these databases. In general, all of the glued databases should be configured as similarly as possible, since the intent is to provide the appearance of a single directory. </p>
<p> Note that the subordinate functionality is implemented internally by the <i>glue</i> overlay and as such its behavior will interact with other overlays in use. By default, the glue overlay is automatically configured as the last overlay on the superior database. Its position on the database can be explicitly configured by setting an <code>overlay glue</code> directive at the desired position. This explicit configuration is necessary e.g. when using the <i>syncprov</i> overlay, which needs to follow <i>glue</i> in order to work over all of the glued databases. E.g.</p>
<dl>
<dd>
<pre> dn: olcDatabase={1}bdb,cn=config
 olcSuffix: dc=example,dc=com
 ...
 dn: olcOverlay={0}glue,olcDatabase={1}bdb,cn=config
 ...
 dn: olcOverlay={1}syncprov,olcDatabase={1}bdb,cn=config
 ...</pre>
</dl>
<p> See the Overlays section below for more details.</p>
<dt><code>olcSuffix: &lt;dn suffix&gt;</code></p>
<dd>Specify the DN suffix of queries that will be passed to this backend database. Multiple suffix lines can be given and at least one is required for each database definition. </p>
<p> If the suffix of one database is &quot;inside&quot; that of another, the database with the inner suffix must come first in the configuration file. You may also want to glue such databases together with the <code>olcSubordinate</code> attribute.</p>
<dt><code>olcSyncUseSubentry: TRUE | FALSE</code></p>
<dd>Store the syncrepl contextCSN in a subentry instead of the context entry of the database. The subentry&#8217;s RDN will be &quot;cn=ldapsync&quot;. The default is FALSE, meaning the contextCSN is stored in the context entry.</p>
<dt> <code>olcSyncrepl: rid=&lt;replica ID&gt;</code> <code>provider=ldap[s]://&lt;hostname&gt;[:port]</code> <code>searchbase=&lt;base DN&gt;</code> <code>[type=refreshOnly|refreshAndPersist]</code> <code>[interval=dd:hh:mm:ss]</code> <code>[retry=[&lt;retry interval&gt; &lt;# of retries&gt;]+]</code> <code>[filter=&lt;filter str&gt;]</code> <code>[scope=sub|one|base|subord]</code> <code>[attrs=&lt;attr list&gt;]</code> <code>[exattrs=&lt;attr list&gt;]</code> <code>[attrsonly]</code> <code>[sizelimit=&lt;limit&gt;]</code> <code>[timelimit=&lt;limit&gt;]</code> <code>[schemachecking=on|off]</code> <code>[network-timeout=&lt;seconds&gt;]</code> <code>[timeout=&lt;seconds&gt;]</code> <code>[bindmethod=simple|sasl]</code> <code>[binddn=&lt;dn&gt;]</code> <code>[saslmech=&lt;mech&gt;]</code> <code>[authcid=&lt;identity&gt;]</code> <code>[authzid=&lt;identity&gt;]</code> <code>[credentials=&lt;passwd&gt;]</code> <code>[realm=&lt;realm&gt;]</code> <code>[secprops=&lt;properties&gt;]</code> <code>[keepalive=&lt;idle&gt;:&lt;probes&gt;:&lt;interval&gt;]</code> <code>[starttls=yes|critical]</code> <code>[tls_cert=&lt;file&gt;]</code> <code>[tls_key=&lt;file&gt;]</code> <code>[tls_cacert=&lt;file&gt;]</code> <code>[tls_cacertdir=&lt;path&gt;]</code> <code>[tls_reqcert=never|allow|try|demand]</code> <code>[tls_ciphersuite=&lt;ciphers&gt;]</code> <code>[tls_crlcheck=none|peer|all]</code> <code>[tls_protocol_min=&lt;major&gt;[.&lt;minor&gt;]]</code> <code>[suffixmassage=&lt;real DN&gt;]</code> <code>[logbase=&lt;base DN&gt;]</code> <code>[logfilter=&lt;filter str&gt;]</code> <code>[syncdata=default|accesslog|changelog]</code></p>
<dl>
<dd>
<dd>Specify the current database as a replica which is kept up-to-date with the master content by establishing the current <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) as a replication consumer site running a <code>syncrepl</code> replication engine. The replica content is kept synchronized to the master content using the LDAP Content Synchronization protocol. Refer to the &quot;OpenLDAP Administrator&#8217;s Guide&quot; for detailed information on setting up a replicated <code>slapd</code> directory service using the <code>syncrepl</code> replication engine. </p>
<p> <code>rid</code> identifies the current <code>syncrepl</code> directive within the replication consumer site. It is a non-negative integer having no more than three decimal digits. </p>
<p> <code>provider</code> specifies the replication provider site containing the master content as an LDAP URI. If &lt;port&gt; is not given, the standard LDAP port number (389 or 636) is used. </p>
<p> The content of the <code>syncrepl</code> replica is defined using a search specification as its result set. The consumer <code>slapd</code> will send search requests to the provider <code>slapd</code> according to the search specification. The search specification includes <code>searchbase, scope, filter, attrs, attrsonly, sizelimit,</code> and <code>timelimit</code> parameters as in the normal search specification. The <code>exattrs</code> option may also be used to specify attributes that should be omitted from incoming entries. The <code>scope</code> defaults to <code>sub</code>, the <code>filter</code> defaults to <code>(objectclass=*)</code>, and there is no default <code>searchbase</code>. The <code>attrs</code> list defaults to <code>&quot;*,+&quot;</code> to return all user and operational attributes, and <code>attrsonly</code> and <code>exattrs</code> are unset by default. The <code>sizelimit</code> and <code>timelimit</code> only accept &quot;unlimited&quot; and positive integers, and both default to &quot;unlimited&quot;. Note, however, that any provider-side limits for the replication identity will be enforced by the provider regardless of the limits requested by the LDAP Content Synchronization operation, much like for any other search operation. </p>
<p> The LDAP Content Synchronization protocol has two operation types. In the <code>refreshOnly</code> operation, the next synchronization search operation is periodically rescheduled at an interval time (specified by <code>interval</code> parameter; 1 day by default) after each synchronization operation finishes. In the <code>refreshAndPersist</code> operation, a synchronization search remains persistent in the provider slapd. Further updates to the master replica will generate <code>searchResultEntry</code> to the consumer slapd as the search responses to the persistent synchronization search. </p>
<p> If an error occurs during replication, the consumer will attempt to reconnect according to the <code>retry</code> parameter which is a list of the &lt;retry interval&gt; and &lt;# of retries&gt; pairs. For example, retry=&quot;60 10 300 3&quot; lets the consumer retry every 60 seconds for the first 10 times and then retry every 300 seconds for the next 3 times before stop retrying. The `+&#8217; in &lt;# of retries&gt; means indefinite number of retries until success. </p>
<p> The schema checking can be enforced at the LDAP Sync consumer site by turning on the <code>schemachecking</code> parameter. The default is off. </p>
<p> The <code>network-timeout</code> parameter sets how long the consumer will wait to establish a network connection to the provider. Once a connection is established, the <code>timeout</code> parameter determines how long the consumer will wait for the initial Bind request to complete. The defaults for these parameters come from <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5). </p>
<p> A <code>bindmethod</code> of <code>simple</code> requires the options <code>binddn</code> and <code>credentials</code> and should only be used when adequate security services (e.g. TLS or IPSEC) are in place. A <code>bindmethod</code> of <code>sasl</code> requires the option <code>saslmech.</code> Depending on the mechanism, an authentication identity and/or credentials can be specified using <code>authcid</code> and <code>credentials.</code> The <code>authzid</code> parameter may be used to specify an authorization identity. Specific security properties (as with the <code>sasl-secprops</code> keyword above) for a SASL bind can be set with the <code>secprops</code> option. A non default SASL realm can be set with the <code>realm </code> option. The provider, other than allow authentication of the syncrepl identity, should grant that identity appropriate access privileges to the data that is being replicated (<code>access</code> directive), and appropriate time and size limits (<code>limits</code> directive). </p>
<p> The <code>keepalive</code> parameter sets the values of <i>idle</i>, <i>probes</i>, and <i>interval</i> used to check whether a socket is alive; <i>idle</i> is the number of seconds a connection needs to remain idle before TCP starts sending keepalive probes; <i>probes</i> is the maximum number of keepalive probes TCP should send before dropping the connection; <i>interval</i> is interval in seconds between individual keepalive probes. Only some systems support the customization of these values; the <code>keepalive</code> parameter is ignored otherwise, and system-wide settings are used. </p>
<p> The <code>starttls</code> parameter specifies use of the StartTLS extended operation to establish a TLS session before Binding to the provider. If the <code>critical</code> argument is supplied, the session will be aborted if the StartTLS request fails. Otherwise the syncrepl session continues without TLS. The tls_reqcert setting defaults to &quot;demand&quot; and the other TLS settings default to the same as the main slapd TLS settings. </p>
<p> The <code>suffixmassage</code> parameter allows the consumer to pull entries from a remote directory whose DN suffix differs from the local directory. The portion of the remote entries&#8217; DNs that matches the <i>searchbase</i> will be replaced with the suffixmassage DN. </p>
<p> Rather than replicating whole entries, the consumer can query logs of data modifications. This mode of operation is referred to as <i>delta syncrepl</i>. In addition to the above parameters, the <code>logbase</code> and <code>logfilter</code> parameters must be set appropriately for the log that will be used. The <code>syncdata</code> parameter must be set to either &quot;accesslog&quot; if the log conforms to the <code><a href="/docs/linux/man/5-slapo-accesslog/">slapo-accesslog</a></code>(5) log format, or &quot;changelog&quot; if the log conforms to the obsolete <i>changelog</i> format. If the <code>syncdata</code> parameter is omitted or set to &quot;default&quot; then the log parameters are ignored.</dl>
<dt><code>olcUpdateDN: &lt;dn&gt;</code></p>
<dd>This option is only applicable in a slave database. It specifies the DN permitted to update (subject to access controls) the replica. It is only needed in certain push-mode replication scenarios. Generally, this DN <i>should not</i> be the same as the <code>rootdn </code> used at the master.</p>
<dt><code>olcUpdateRef: &lt;url&gt;</code></p>
<dd>Specify the referral to pass back when <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) is asked to modify a replicated local database. If multiple values are specified, each url is provided. </p>
</dl>
<h2>Database-Specific Options</h2>
<p>Each database may allow specific configuration options; they are documented separately in the backends&#8217; manual pages. See the <code><a href="/docs/linux/man/5-slapd-backends/">slapd.backends</a></code>(5) manual page for an overview of available backends.</p>
<h2>Overlays</h2>
<p>An overlay is a piece of code that intercepts database operations in order to extend or change them. Overlays are pushed onto a stack over the database, and so they will execute in the reverse of the order in which they were configured and the database itself will receive control last of all. </p>
<p> Overlays must be configured as child entries of a specific database. The entry&#8217;s RDN must be of the form <code>olcOverlay={x}&lt;overlaytype&gt;</code> and the entry must have the olcOverlayConfig objectClass. Normally the config engine generates the &quot;{x}&quot; index in the RDN automatically, so it can be omitted when initially loading these entries. </p>
<p> See the <code><a href="/docs/linux/man/5-slapd-overlays/">slapd.overlays</a></code>(5) manual page for an overview of available overlays.</p>
<h2>Examples</h2>
<p>Here is a short example of a configuration in LDIF suitable for use with <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8) :</p>
<dl>
<dd>
<pre>dn: cn=config
objectClass: olcGlobal
cn: config
olcPidFile: /var/run/slapd.pid
olcAttributeOptions: x-hidden lang-
dn: cn=schema,cn=config
objectClass: olcSchemaConfig
cn: schema
include: file:///etc/openldap/schema/core.ldif
dn: olcDatabase=frontend,cn=config
objectClass: olcDatabaseConfig
objectClass: olcFrontendConfig
olcDatabase: frontend
# Subtypes of &quot;name&quot; (e.g. &quot;cn&quot; and &quot;ou&quot;) with the
# option &quot;;x-hidden&quot; can be searched for/compared,
# but are not shown. See <code><a href="//www.systutorials.com/docs/linux/man/5-slapd.access/">slapd.access</a></code>(5).
olcAccess: to attrs=name;x-hidden by * =cs
# Protect passwords. See <code><a href="//www.systutorials.com/docs/linux/man/5-slapd.access/">slapd.access</a></code>(5).
olcAccess: to attrs=userPassword by * auth
# Read access to other attributes and entries.
olcAccess: to * by * read
# set a rootpw for the config database so we can bind.
# deny access to everyone else.
dn: olcDatabase=config,cn=config
objectClass: olcDatabaseConfig
olcDatabase: config
olcRootPW: {SSHA}XKYnrjvGT3wZFQrDD5040US592LxsdLy
olcAccess: to * by * none
dn: olcDatabase=bdb,cn=config
objectClass: olcDatabaseConfig
objectClass: olcBdbConfig
olcDatabase: bdb
olcSuffix: &quot;dc=our-domain,dc=com&quot;
# The database directory MUST exist prior to
# running slapd AND should only be accessible
# by the slapd/tools. Mode 0700 recommended.
olcDbDirectory: /var/openldap-data
# Indices to maintain
olcDbIndex: objectClass eq
olcDbIndex: cn,sn,mail pres,eq,approx,sub
# We serve small clients that do not handle referrals,
# so handle remote lookups on their behalf.
dn: olcDatabase=ldap,cn=config
objectClass: olcDatabaseConfig
objectClass: olcLdapConfig
olcDatabase: ldap
olcSuffix: &quot;&quot;
olcDbUri: <a href="ldap://ldap.some-server.com/">ldap://ldap.some-server.com/</a></pre>
</dl>
<p> Assuming the above data was saved in a file named &quot;config.ldif&quot; and the /etc/openldap/slapd.d directory has been created, this command will initialize the configuration:</p>
<dl>
<dd>
<pre>slapadd -F /etc/openldap/slapd.d -n 0 -l config.ldif</pre>
</dl>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; contains a longer annotated example of a slapd configuration. Alternatively, an existing slapd.conf file can be converted to the new format using slapd or any of the slap tools:</p>
<dl>
<dd>
<pre>slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d</pre>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/etc/openldap/slapd.d</p>
<dd>default slapd configuration directory</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5), <code><a href="/docs/linux/man/1-gnutls-cli/">gnutls-cli</a></code>(1), <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5), <code><a href="/docs/linux/man/5-slapd-backends/">slapd.backends</a></code>(5), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-overlays/">slapd.overlays</a></code>(5), <code><a href="/docs/linux/man/5-slapd-plugin/">slapd.plugin</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slapacl/">slapacl</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapauth/">slapauth</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapdn/">slapdn</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), <code><a href="/docs/linux/man/8-slappasswd/">slappasswd</a></code>(8), <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8). </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
