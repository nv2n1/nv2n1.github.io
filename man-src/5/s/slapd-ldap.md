---
title: "slapd-ldap(5)"
name: "slapd-ldap"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-ldap/"
description: "slapd-ldap – LDAP backend to slapd"
---

<p>slapd-ldap &#8211; LDAP backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The LDAP backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) is not an actual database; instead it acts as a proxy to forward incoming requests to another LDAP server. While processing requests it will also chase referrals, so that referrals are fully processed instead of being returned to the slapd client. Sessions that explicitly Bind to the back-ldap database always create their own private connection to the remote LDAP server. Anonymous sessions will share a single anonymous connection to the remote server. For sessions bound through other mechanisms, all sessions with the same DN will share the same connection. This connection pooling strategy can enhance the proxy&#8217;s efficiency by reducing the overhead of repeatedly making/breaking multiple connections. The ldap database can also act as an information service, i.e. the identity of locally authenticated clients is asserted to the remote server, possibly in some modified form. For this purpose, the proxy binds to the remote server with some administrative identity, and, if required, authorizes the asserted identity. See the <i>idassert-</i>* rules below. The administrative identity of the proxy, on the remote server, must be allowed to authorize by means of appropriate <code>authzTo</code> rules; see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details. The proxy instance of <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) must contain schema information for the attributes and objectClasses used in filters, request DNs and request-related data in general. It should also contain schema information for the data returned by the proxied server. It is the responsibility of the proxy administrator to keep the schema of the proxy lined up with that of the proxied server. Note: When looping back to the same instance of <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), each connection requires a new thread; as a consequence, <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) must be compiled with thread support, and the <code>threads</code> parameter may need some tuning; in those cases, one may consider using <code><a href="/docs/linux/man/5-slapd-relay/">slapd-relay</a></code>(5) instead, which performs the relayed operation internally and thus reuses the same connection. </p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the LDAP backend database. That is, they must follow a &quot;database ldap&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page. </p>
<p> Note: In early versions of back-ldap it was recommended to always set </p>
<dl>
<dd>
<pre>lastmod off</pre>
</dl>
<p> for <code>ldap</code> and <code>meta</code> databases. This was required because operational attributes related to entry creation and modification should not be proxied, as they could be mistakenly written to the target server(s), generating an error. The current implementation automatically sets lastmod to <code>off</code>, so its use is redundant and should be omitted. </p>
<dl>
<dt><code>uri &lt;ldapurl&gt;</code></p>
<dd>LDAP server to use. Multiple URIs can be set in a single <code>ldapurl</code> argument, resulting in the underlying library automatically calling the first server of the list that responds, e.g. </p>
<p> <code>uri &quot;<a href="ldap://host/">ldap://host/</a> <a href="ldap://backup-host/">ldap://backup-host/</a>&quot;</code> </p>
<p> The URI list is space- or comma-separated. Whenever the server that responds is not the first one in the list, the list is rearranged and the responsive server is moved to the head, so that it will be first contacted the next time a connection needs to be created.</p>
<dt> <code>acl-bind</code> <code>bindmethod=simple|sasl [binddn=&lt;simple DN&gt;] [credentials=&lt;simple password&gt;]</code> <code>[saslmech=&lt;SASL mech&gt;] [secprops=&lt;properties&gt;] [realm=&lt;realm&gt;]</code> <code>[authcId=&lt;authentication ID&gt;] [authzId=&lt;authorization ID&gt;]</code> <code>[starttls=no|yes|critical]</code> <code>[tls_cert=&lt;file&gt;]</code> <code>[tls_key=&lt;file&gt;]</code> <code>[tls_cacert=&lt;file&gt;]</code> <code>[tls_cacertdir=&lt;path&gt;]</code> <code>[tls_reqcert=never|allow|try|demand]</code> <code>[tls_ciphersuite=&lt;ciphers&gt;]</code> <code>[tls_protocol_min=&lt;major&gt;[.&lt;minor&gt;]]</code> <code>[tls_crlcheck=none|peer|all]</code></p>
<dl>
<dd>
<dd>Allows to define the parameters of the authentication method that is internally used by the proxy to collect info related to access control, and whenever an operation occurs with the identity of the rootdn of the LDAP proxy database. The identity defined by this directive, according to the properties associated to the authentication method, is supposed to have read access on the target server to attributes used on the proxy for ACL checking. </p>
<p> There is no risk of giving away such values; they are only used to check permissions. The default is to use <code>simple</code> bind, with empty <i>binddn</i> and <i>credentials</i>, which means that the related operations will be performed anonymously. If not set, and if <code>idassert-bind</code> is defined, this latter identity is used instead. See <code>idassert-bind</code> for details. </p>
<p> The connection between the proxy database and the remote server associated to this identity is cached regardless of the lifespan of the client-proxy connection that first established it. </p>
<p> <code>This identity is not implicitly used by the proxy</code> <code>when the client connects anonymously.</code> The <code>idassert-bind</code> feature, instead, in some cases can be crafted to implement that behavior, which is <i>intrinsically unsafe and should be used with extreme care</i>. This directive obsoletes <code>acl-authcDN</code>, and <code>acl-passwd</code>. </p>
<p> The TLS settings default to the same as the main slapd TLS settings, except for <code>tls_reqcert</code> which defaults to &quot;demand&quot;.</dl>
<dt><code>cancel {ABANDON|ignore|exop[-discover]}</code></p>
<dd>Defines how to handle operation cancellation. By default, <code>abandon</code> is invoked, so the operation is abandoned immediately. If set to <code>ignore</code>, no action is taken and any further response is ignored; this may result in further response messages to be queued for that connection, so it is recommended that long lasting connections are timed out either by <i>idle-timeout</i> or <i>conn-ttl</i>, so that resources eventually get released. If set to <code>exop</code>, a <i>cancel</i> operation (RFC 3909) is issued, resulting in the cancellation of the current operation; the <i>cancel</i> operation waits for remote server response, so its use may not be recommended. If set to <code>exop-discover</code>, support of the <i>cancel </i> extended operation is detected by reading the remote server&#8217;s root DSE. </p>
<dt><code>chase-referrals {YES|no}</code></p>
<dd>enable/disable automatic referral chasing, which is delegated to the underlying libldap, with rebinding eventually performed if the <code>rebind-as-user</code> directive is used. The default is to chase referrals. </p>
<dt><code>conn-ttl &lt;time&gt;</code></p>
<dd>This directive causes a cached connection to be dropped and recreated after a given ttl, regardless of being idle or not. </p>
<dt><code>idassert-authzFrom &lt;authz-regexp&gt;</code></p>
<dd>if defined, selects what <i>local</i> identities are authorized to exploit the identity assertion feature. The string <code>&lt;authz-regexp&gt;</code> follows the rules defined for the <i>authzFrom</i> attribute. See <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), section related to <code>authz-policy</code>, for details on the syntax of this field. </p>
<dt> <code>idassert-bind</code> <code>bindmethod=none|simple|sasl [binddn=&lt;simple DN&gt;] [credentials=&lt;simple password&gt;]</code> <code>[saslmech=&lt;SASL mech&gt;] [secprops=&lt;properties&gt;] [realm=&lt;realm&gt;]</code> <code>[authcId=&lt;authentication ID&gt;] [authzId=&lt;authorization ID&gt;]</code> <code>[authz={native|proxyauthz}] [mode=&lt;mode&gt;] [flags=&lt;flags&gt;]</code> <code>[starttls=no|yes|critical]</code> <code>[tls_cert=&lt;file&gt;]</code> <code>[tls_key=&lt;file&gt;]</code> <code>[tls_cacert=&lt;file&gt;]</code> <code>[tls_cacertdir=&lt;path&gt;]</code> <code>[tls_reqcert=never|allow|try|demand]</code> <code>[tls_ciphersuite=&lt;ciphers&gt;]</code> <code>[tls_protocol_min=&lt;version&gt;]</code> <code>[tls_crlcheck=none|peer|all]</code></p>
<dl>
<dd>
<dd>Allows to define the parameters of the authentication method that is internally used by the proxy to authorize connections that are authenticated by other databases. Direct binds are always proxied without any idassert handling. </p>
<p> The identity defined by this directive, according to the properties associated to the authentication method, is supposed to have auth access on the target server to attributes used on the proxy for authentication and authorization, and to be allowed to authorize the users. This requires to have <code>proxyAuthz</code> privileges on a wide set of DNs, e.g. <code>authzTo=dn.subtree:</code>, and the remote server to have <code>authz-policy</code> set to <code>to</code> or <code>both</code>. See <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details on these statements and for remarks and drawbacks about their usage. The supported bindmethods are </p>
<p> <code>none|simple|sasl</code> </p>
<p> where <code>none</code> is the default, i.e. no <i>identity assertion</i> is performed. </p>
<p> The authz parameter is used to instruct the SASL bind to exploit <code>native </code> SASL authorization, if available; since connections are cached, this should only be used when authorizing with a fixed identity (e.g. by means of the <code>authzDN</code> or <code>authzID</code> parameters). Otherwise, the default <code>proxyauthz</code> is used, i.e. the proxyAuthz control (Proxied Authorization, RFC 4370) is added to all operations. </p>
<p> The supported modes are: </p>
<p> <code>&lt;mode&gt; := {legacy|anonymous|none|self}</code> </p>
<p> If <code>&lt;mode&gt;</code> is not present, and <code>authzId</code> is given, the proxy always authorizes that identity. <code>&lt;authorization ID&gt;</code> can be </p>
<p> <code>u:&lt;user&gt;</code> </p>
<p> <code>[dn:]&lt;DN&gt;</code> </p>
<p> The former is supposed to be expanded by the remote server according to the authz rules; see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details. In the latter case, whether or not the <code>dn:</code> prefix is present, the string must pass DN validation and normalization. </p>
<p> The default mode is <code>legacy</code>, which implies that the proxy will either perform a simple bind as the <i>authcDN</i> or a SASL bind as the <i>authcID</i> and assert the client&#8217;s identity when it is not anonymous. The other modes imply that the proxy will always either perform a simple bind as the <i>authcDN</i> or a SASL bind as the <i>authcID</i>, unless restricted by <code>idassert-authzFrom</code> rules (see below), in which case the operation will fail; eventually, it will assert some other identity according to <code>&lt;mode&gt;</code>. Other identity assertion modes are <code>anonymous</code> and <code>self</code>, which respectively mean that the <i>empty </i> or the <i>client</i>&#8216;s identity will be asserted; <code>none</code>, which means that no proxyAuthz control will be used, so the <i>authcDN</i> or the <i>authcID</i> identity will be asserted. For all modes that require the use of the <i>proxyAuthz </i> control, on the remote server the proxy identity must have appropriate <i>authzTo</i> permissions, or the asserted identities must have appropriate <i>authzFrom </i> permissions. Note, however, that the ID assertion feature is mostly useful when the asserted identities do not exist on the remote server. </p>
<p> Flags can be </p>
<p> <code>override,[non-]prescriptive,proxy-authz-[non-]critical</code> </p>
<p> When the <code>override</code> flag is used, identity assertion takes place even when the database is authorizing for the identity of the client, i.e. after binding with the provided identity, and thus authenticating it, the proxy performs the identity assertion using the configured identity and authentication method. </p>
<p> When the <code>prescriptive</code> flag is used (the default), operations fail with <i>inappropriateAuthentication</i> for those identities whose assertion is not allowed by the <code>idassert-authzFrom</code> patterns. If the <code>non-prescriptive</code> flag is used, operations are performed anonymously for those identities whose assertion is not allowed by the <code>idassert-authzFrom</code> patterns. </p>
<p> When the <code>proxy-authz-non-critical</code> flag is used (the default), the proxyAuthz control is not marked as critical, in violation of RFC 4370. Use of <code>proxy-authz-critical</code> is recommended. </p>
<p> The TLS settings default to the same as the main slapd TLS settings, except for <code>tls_reqcert</code> which defaults to &quot;demand&quot;. </p>
<p> The identity associated to this directive is also used for privileged operations whenever <code>idassert-bind</code> is defined and <code>acl-bind</code> is not. See <code>acl-bind</code> for details. </p>
<p> This directive obsoletes <code>idassert-authcDN</code>, <code>idassert-passwd</code>, <code>idassert-mode</code>, and <code>idassert-method</code>.</dl>
<dt><code>idassert-passthru &lt;authz-regexp&gt;</code></p>
<dd>if defined, selects what <i>local</i> identities bypass the identity assertion feature. Those identities need to be known by the remote host. The string <code>&lt;authz-regexp&gt;</code> follows the rules defined for the <i>authzFrom</i> attribute. See <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), section related to <code>authz-policy</code>, for details on the syntax of this field. </p>
<dt><code>idle-timeout &lt;time&gt;</code></p>
<dd>This directive causes a cached connection to be dropped an recreated after it has been idle for the specified time. </p>
<dt><code>keepalive &lt;idle&gt;:&lt;probes&gt;:&lt;interval&gt;</code></p>
<dd>The <code>keepalive</code> parameter sets the values of <i>idle</i>, <i>probes</i>, and <i>interval</i> used to check whether a socket is alive; <i>idle</i> is the number of seconds a connection needs to remain idle before TCP starts sending keepalive probes; <i>probes</i> is the maximum number of keepalive probes TCP should send before dropping the connection; <i>interval</i> is interval in seconds between individual keepalive probes. Only some systems support the customization of these values; the <code>keepalive</code> parameter is ignored otherwise, and system-wide settings are used. </p>
<dt><code>network-timeout &lt;time&gt;</code></p>
<dd>Sets the network timeout value after which <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)/<code><a href="/docs/linux/man/2-select/">select</a></code>(2) following a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) returns in case of no activity. The value is in seconds, and it can be specified as for <code>idle-timeout</code>. </p>
<dt><code>norefs &lt;NO|yes&gt;</code></p>
<dd>If <code>yes</code>, do not return search reference responses. By default, they are returned unless request is LDAPv2. </p>
<dt><code>noundeffilter &lt;NO|yes&gt;</code></p>
<dd>If <code>yes</code>, return success instead of searching if a filter is undefined or contains undefined portions. By default, the search is propagated after replacing undefined portions with <code>(!(objectClass=*))</code>, which corresponds to the empty result set. </p>
<dt><code>onerr {CONTINUE|stop}</code></p>
<dd>This directive allows to select the behavior in case an error is returned by the remote server during a search. The default, <code>continue</code>, consists in returning success. If the value is set to <code>stop</code>, the error is returned to the client. </p>
<dt><code>protocol-version {0,2,3}</code></p>
<dd>This directive indicates what protocol version must be used to contact the remote server. If set to 0 (the default), the proxy uses the same protocol version used by the client, otherwise the requested protocol is used. The proxy returns <i>unwillingToPerform</i> if an operation that is incompatible with the requested protocol is attempted. </p>
<dt><code>proxy-whoami {NO|yes}</code></p>
<dd>Turns on proxying of the WhoAmI extended operation. If this option is given, back-ldap will replace slapd&#8217;s original WhoAmI routine with its own. On slapd sessions that were authenticated by back-ldap, the WhoAmI request will be forwarded to the remote LDAP server. Other sessions will be handled by the local slapd, as before. This option is mainly useful in conjunction with Proxy Authorization. </p>
<dt><code>quarantine &lt;interval&gt;,&lt;num&gt;[;&lt;interval&gt;,&lt;num&gt;[&#8230;]]</code></p>
<dd>Turns on quarantine of URIs that returned <i>LDAP_UNAVAILABLE</i>, so that an attempt to reconnect only occurs at given intervals instead of any time a client requests an operation. The pattern is: retry only after at least <i>interval</i> seconds elapsed since last attempt, for exactly <i>num</i> times; then use the next pattern. If <i>num</i> for the last pattern is &quot;<code>+</code>&quot;, it retries forever; otherwise, no more retries occur. The process can be restarted by resetting the <i>olcDbQuarantine</i> attribute of the database entry in the configuration backend. </p>
<dt><code>rebind-as-user {NO|yes}</code></p>
<dd>If this option is given, the client&#8217;s bind credentials are remembered for rebinds, when trying to re-establish a broken connection, or when chasing a referral, if <code>chase-referrals</code> is set to <i>yes</i>. </p>
<dt><code>session-tracking-request {NO|yes}</code></p>
<dd>Adds session tracking control for all requests. The client&#8217;s IP and hostname, and the identity associated to each request, if known, are sent to the remote server for informational purposes. This directive is incompatible with setting <i>protocol-version</i> to 2. </p>
<dt><code>single-conn {NO|yes}</code></p>
<dd>Discards current cached connection when the client rebinds. </p>
<dt><code>t-f-support {NO|yes|discover}</code></p>
<dd>enable if the remote server supports absolute filters (see <i>RFC 4526</i> for details). If set to <code>discover</code>, support is detected by reading the remote server&#8217;s root DSE. </p>
<dt><code>timeout [&lt;op&gt;=]&lt;val&gt; [&#8230;]</code></p>
<dd>This directive allows to set per-operation timeouts. Operations can be </p>
<p> <code>&lt;op&gt; ::= bind, add, delete, modrdn, modify, compare, search</code> </p>
<p> The overall duration of the <code>search</code> operation is controlled either by the <code>timelimit</code> parameter or by server-side enforced time limits (see <code>timelimit</code> and <code>limits</code> in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details). This <code>timeout</code> parameter controls how long the target can be irresponsive before the operation is aborted. Timeout is meaningless for the remaining operations, <code>unbind</code> and <code>abandon</code>, which do not imply any response, while it is not yet implemented in currently supported <code>extended</code> operations. If no operation is specified, the timeout <code>val</code> affects all supported operations. </p>
<p> Note: if the timelimit is exceeded, the operation is cancelled (according to the <code>cancel</code> directive); the protocol does not provide any means to rollback operations, so the client will not be notified about the result of the operation, which may eventually succeeded or not. In case the timeout is exceeded during a bind operation, the connection is destroyed, according to RFC4511. </p>
<p> Note: in some cases, this backend may issue binds prior to other operations (e.g. to bind anonymously or with some prescribed identity according to the <code>idassert-bind</code> directive). In this case, the timeout of the operation that resulted in the bind is used. </p>
<dt> <code>tls {[try-]start|[try-]propagate|ldaps}</code> <code>[tls_cert=&lt;file&gt;]</code> <code>[tls_key=&lt;file&gt;]</code> <code>[tls_cacert=&lt;file&gt;]</code> <code>[tls_cacertdir=&lt;path&gt;]</code> <code>[tls_reqcert=never|allow|try|demand]</code> <code>[tls_ciphersuite=&lt;ciphers&gt;]</code> <code>[tls_crlcheck=none|peer|all]</code></p>
<dl>
<dd>
<dd>Specify the use of TLS when a regular connection is initialized. The StartTLS extended operation will be used unless the URI directive protocol scheme is <code>ldaps://</code>. In that case this keyword may only be set to &quot;ldaps&quot; and the StartTLS operation will not be used. <code>propagate</code> issues the StartTLS operation only if the original connection did. The <code>try-</code> prefix instructs the proxy to continue operations if the StartTLS operation failed; its use is <code>not</code> recommended. </p>
<p> The TLS settings default to the same as the main slapd TLS settings, except for <code>tls_reqcert</code> which defaults to &quot;demand&quot;.</dl>
<dt><code>use-temporary-conn {NO|yes}</code></p>
<dd>when set to <code>yes</code>, create a temporary connection whenever competing with other threads for a shared one; otherwise, wait until the shared connection is available. </p>
</dl>
<h2>Backward Compatibility</h2>
<p>The LDAP backend has been heavily reworked between releases 2.2 and 2.3, and subsequently between 2.3 and 2.4. As a side-effect, some of the traditional directives have been deprecated and should be no longer used, as they might disappear in future releases. </p>
<dl>
<dt><code>acl-authcDN &lt;administrative DN for access control purposes&gt;</code></p>
<dd>Formerly known as the <code>binddn</code>, it is the DN that is used to query the target server for acl checking; it is supposed to have read access on the target server to attributes used on the proxy for acl checking. There is no risk of giving away such values; they are only used to check permissions. </p>
<p> <code>The acl-authcDN identity is by no means implicitly used by the proxy </code> <code>when the client connects anonymously.</code> The <code>idassert-*</code> feature can be used (at own risk) for that purpose instead. </p>
<p> This directive is obsoleted by the <code>binddn</code> arg of <code>acl-bind</code> when <i>bindmethod</i>=<code>simple</code>, and will be dismissed in the future. </p>
<dt><code>acl-passwd &lt;password&gt;</code></p>
<dd>Formerly known as the <code>bindpw</code>, it is the password used with the above <code>acl-authcDN</code> directive. This directive is obsoleted by the <code>credentials</code> arg of <code>acl-bind</code> when <i>bindmethod</i>=<code>simple</code>, and will be dismissed in the future. </p>
<dt><code>idassert-authcDN &lt;administrative DN for proxyAuthz purposes&gt;</code></p>
<dd>DN which is used to propagate the client&#8217;s identity to the target by means of the proxyAuthz control when the client does not belong to the DIT fragment that is being proxied by back-ldap. This directive is obsoleted by the <code>binddn</code> arg of <code>idassert-bind</code> when <i>bindmethod</i>=<code>simple</code>, and will be dismissed in the future. </p>
<dt><code>idassert-passwd &lt;password&gt;</code></p>
<dd>Password used with the <code>idassert-authcDN</code> above. This directive is obsoleted by the <code>crendentials</code> arg of <code>idassert-bind</code> when <i>bindmethod</i>=<code>simple</code>, and will be dismissed in the future. </p>
<dt><code>idassert-mode &lt;mode&gt; [&lt;flags&gt;]</code></p>
<dd>defines what type of <i>identity assertion</i> is used. This directive is obsoleted by the <code>mode</code> arg of <code>idassert-bind</code>, and will be dismissed in the future. </p>
<dt><code>idassert-method &lt;method&gt; [&lt;saslargs&gt;]</code></p>
<dd>This directive is obsoleted by the <code>bindmethod</code> arg of <code>idassert-bind</code>, and will be dismissed in the future. </p>
<dt><code>port &lt;port&gt;</code></p>
<dd>this directive is no longer supported. Use the <code>uri</code> directive as described above. </p>
<dt><code>server &lt;hostname[:port]&gt;</code></p>
<dd>this directive is no longer supported. Use the <code>uri</code> directive as described above. </p>
<dt><code>suffixmassage, map, rewrite*</code></p>
<dd>These directives are no longer supported by back-ldap; their functionality is now delegated to the <code>rwm</code> overlay. Essentially, add a statement </p>
<p> <code>overlay rwm</code> </p>
<p> first, and prefix all rewrite/map statements with <code>rwm-</code> to obtain the original behavior. See <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) for details. </p>
</dl>
<h2>Access Control</h2>
<p>The <code>ldap</code> backend does not honor all ACL semantics as described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). In general, access checking is delegated to the remote server(s). Only <code>read (=r)</code> access to the <code>entry</code> pseudo-attribute and to the other attribute values of the entries returned by the <code>search</code> operation is honored, which is performed by the frontend.</p>
<h2>Overlays</h2>
<p>The LDAP backend provides basic proxying functionalities to many overlays. The <code>chain</code> overlay, described in <code><a href="/docs/linux/man/5-slapo-chain/">slapo-chain</a></code>(5), and the <code>translucent</code> overlay, described in <code><a href="/docs/linux/man/5-slapo-translucent/">slapo-translucent</a></code>(5), deserve a special mention. </p>
<p> Conversely, there are many overlays that are best used in conjunction with the LDAP backend. The <code>proxycache </code> overlay allows caching of LDAP search requests (queries) in a local database. See <code><a href="/docs/linux/man/5-slapo-pcache/">slapo-pcache</a></code>(5) for details. The <code>rwm</code> overlay provides DN rewrite and attribute/objectClass mapping capabilities to the underlying database. See <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) for details.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5), <code><a href="/docs/linux/man/5-slapo-chain/">slapo-chain</a></code>(5), <code><a href="/docs/linux/man/5-slapo-pcache/">slapo-pcache</a></code>(5), <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5), <code><a href="/docs/linux/man/5-slapo-translucent/">slapo-translucent</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3).</p>
<h2>Author</h2>
<p>Howard Chu, with enhancements by Pierangelo Masarati</p>
