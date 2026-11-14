---
title: "slapd-meta(5)"
name: "slapd-meta"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-meta/"
description: "slapd-meta – metadirectory backend to slapd"
---

<p>slapd-meta &#8211; metadirectory backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>meta</code> backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) performs basic LDAP proxying with respect to a set of remote LDAP servers, called &quot;targets&quot;. The information contained in these servers can be presented as belonging to a single Directory Information Tree (DIT). A basic knowledge of the functionality of the <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) backend is recommended. This backend has been designed as an enhancement of the ldap backend. The two backends share many features (actually they also share portions of code). While the <code>ldap</code> backend is intended to proxy operations directed to a single server, the <code>meta</code> backend is mainly intended for proxying of multiple servers and possibly naming context masquerading. These features, although useful in many scenarios, may result in excessive overhead for some applications, so its use should be carefully considered. In the examples section, some typical scenarios will be discussed. The proxy instance of <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) must contain schema information for the attributes and objectClasses used in filters, request DN and request-related data in general. It should also contain schema information for the data returned by the proxied server. It is the responsibility of the proxy administrator to keep the schema of the proxy lined up with that of the proxied server. Note: When looping back to the same instance of <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), each connection requires a new thread; as a consequence, <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) must be compiled with thread support, and the <code>threads</code> parameter may need some tuning; in those cases, unless the multiple target feature is required, one may consider using <code><a href="/docs/linux/man/5-slapd-relay/">slapd-relay</a></code>(5) instead, which performs the relayed operation internally and thus reuses the same connection. </p>
<h2>Examples</h2>
<p>There are examples in various places in this document, as well as in the slapd/back-meta/data/ directory in the OpenLDAP source tree.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the META backend database. That is, they must follow a &quot;database meta&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page. </p>
<p> Note: In early versions of back-ldap and back-meta it was recommended to always set </p>
<dl>
<dd>
<pre>lastmod off</pre>
</dl>
<p> for <code>ldap</code> and <code>meta</code> databases. This was required because operational attributes related to entry creation and modification should not be proxied, as they could be mistakenly written to the target server(s), generating an error. The current implementation automatically sets lastmod to <code>off</code>, so its use is redundant and should be omitted.</p>
<h2>Special Configuration Directives</h2>
<p>Target configuration starts with the &quot;uri&quot; directive. All the configuration directives that are not specific to targets should be defined first for clarity, including those that are common to all backends. They are: </p>
<dl>
<dt><code>conn-ttl &lt;time&gt;</code></p>
<dd>This directive causes a cached connection to be dropped an recreated after a given ttl, regardless of being idle or not. </p>
<dt><code>default-target none</code></p>
<dd>This directive forces the backend to reject all those operations that must resolve to a single target in case none or multiple targets are selected. They include: add, delete, modify, modrdn; compare is not included, as well as bind since, as they don&#8217;t alter entries, in case of multiple matches an attempt is made to perform the operation on any candidate target, with the constraint that at most one must succeed. This directive can also be used when processing targets to mark a specific target as default. </p>
<dt><code>dncache-ttl {DISABLED|forever|&lt;ttl&gt;}</code></p>
<dd>This directive sets the time-to-live of the DN cache. This caches the target that holds a given DN to speed up target selection in case multiple targets would result from an uncached search; forever means cache never expires; disabled means no DN caching; otherwise a valid ( &gt; 0 ) ttl is required, in the format illustrated for the <code>idle-timeout</code> directive. </p>
<dt><code>onerr {CONTINUE|report|stop}</code></p>
<dd>This directive allows to select the behavior in case an error is returned by one target during a search. The default, <code>continue</code>, consists in continuing the operation, trying to return as much data as possible. If the value is set to <code>stop</code>, the search is terminated as soon as an error is returned by one target, and the error is immediately propagated to the client. If the value is set to <code>report</code>, the search is continuated to the end but, in case at least one target returned an error code, the first non-success error code is returned. </p>
<dt><code>norefs &lt;NO|yes&gt;</code></p>
<dd>If <code>yes</code>, do not return search reference responses. By default, they are returned unless request is LDAPv2. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>noundeffilter &lt;NO|yes&gt;</code></p>
<dd>If <code>yes</code>, return success instead of searching if a filter is undefined or contains undefined portions. By default, the search is propagated after replacing undefined portions with <code>(!(objectClass=*))</code>, which corresponds to the empty result set. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>protocol-version {0,2,3}</code></p>
<dd>This directive indicates what protocol version must be used to contact the remote server. If set to 0 (the default), the proxy uses the same protocol version used by the client, otherwise the requested protocol is used. The proxy returns <i>unwillingToPerform</i> if an operation that is incompatible with the requested protocol is attempted. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>pseudoroot-bind-defer {YES|no}</code></p>
<dd>This directive, when set to <code>yes</code>, causes the authentication to the remote servers with the pseudo-root identity (the identity defined in each <code>idassert-bind</code> directive) to be deferred until actually needed by subsequent operations. Otherwise, all binds as the rootdn are propagated to the targets. </p>
<dt><code>quarantine &lt;interval&gt;,&lt;num&gt;[;&lt;interval&gt;,&lt;num&gt;[&#8230;]]</code></p>
<dd>Turns on quarantine of URIs that returned <i>LDAP_UNAVAILABLE</i>, so that an attempt to reconnect only occurs at given intervals instead of any time a client requests an operation. The pattern is: retry only after at least <i>interval</i> seconds elapsed since last attempt, for exactly <i>num</i> times; then use the next pattern. If <i>num</i> for the last pattern is &quot;<code>+</code>&quot;, it retries forever; otherwise, no more retries occur. This directive must appear before any target specification; it affects all targets with the same pattern. </p>
<dt><code>rebind-as-user {NO|yes}</code></p>
<dd>If this option is given, the client&#8217;s bind credentials are remembered for rebinds, when trying to re-establish a broken connection, or when chasing a referral, if <code>chase-referrals</code> is set to <i>yes</i>. </p>
<dt><code>session-tracking-request {NO|yes}</code></p>
<dd>Adds session tracking control for all requests. The client&#8217;s IP and hostname, and the identity associated to each request, if known, are sent to the remote server for informational purposes. This directive is incompatible with setting <i>protocol-version</i> to 2. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>single-conn {NO|yes}</code></p>
<dd>Discards current cached connection when the client rebinds. </p>
<dt><code>use-temporary-conn {NO|yes}</code></p>
<dd>when set to <code>yes</code>, create a temporary connection whenever competing with other threads for a shared one; otherwise, wait until the shared connection is available. </p>
</dl>
<h2>Target Specification</h2>
<p>Target specification starts with a &quot;uri&quot; directive: </p>
<dl>
<dt><code>uri &lt;protocol&gt;://[&lt;host&gt;]/&lt;naming context&gt; [&#8230;]</code></p>
<dd>The &lt;protocol&gt; part can be anything <code><a href="/docs/linux/man/3-ldap_initialize/">ldap_initialize</a></code>(3) accepts ({ldap|ldaps|ldapi} and variants); the &lt;host&gt; may be omitted, defaulting to whatever is set in <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5). The &lt;naming context&gt; part is <i>mandatory</i> for the first URI, but it <i>must be omitted</i> for subsequent ones, if any. The naming context part must be within the naming context defined for the backend, e.g.:</dl>
<dl>
<dd>
<pre>suffix &quot;<code>dc=foo,dc=com</code>&quot;
uri &quot;<a href="ldap://x.foo.com/dc=x,">ldap://x.foo.com/dc=x,</a><code>dc=foo,dc=com</code>&quot;</pre>
</dl>
<dl>
<dd>The &lt;naming context&gt; part doesn&#8217;t need to be unique across the targets; it may also match one of the values of the &quot;suffix&quot; directive. Multiple URIs may be defined in a single URI statement. The additional URIs must be separate arguments and must not have any &lt;naming context&gt; part. This causes the underlying library to contact the first server of the list that responds. For example, if <i>l1.foo.com</i> and <i>l2.foo.com</i> are shadows of the same server, the directive </p>
<pre>suffix &quot;<code>dc=foo,dc=com</code>&quot;
uri &quot;<a href="ldap://l1.foo.com/">ldap://l1.foo.com/</a><code>dc=foo,dc=com</code>&quot; &quot;<a href="ldap://l2.foo.com/">ldap://l2.foo.com/</a>&quot;</pre>
</dl>
<dl>
<dd>causes <i>l2.foo.com</i> to be contacted whenever <i>l1.foo.com</i> does not respond. In that case, the URI list is internally rearranged, by moving unavailable URIs to the end, so that further connection attempts occur with respect to the last URI that succeeded.</dl>
<dl>
<dt><code>acl-authcDN &lt;administrative DN for access control purposes&gt;</code></p>
<dd>DN which is used to query the target server for acl checking, as in the LDAP backend; it is supposed to have read access on the target server to attributes used on the proxy for acl checking. There is no risk of giving away such values; they are only used to check permissions. <code>The acl-authcDN identity is by no means implicitly used by the proxy </code> <code>when the client connects anonymously.</code> </p>
<dt><code>acl-passwd &lt;password&gt;</code></p>
<dd>Password used with the <code>acl-authcDN</code> above. </p>
<dt><code>bind-timeout &lt;microseconds&gt;</code></p>
<dd>This directive defines the timeout, in microseconds, used when polling for response after an asynchronous bind connection. The initial call to <a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3) is performed with a trade-off timeout of 100000 us; if that results in a timeout exceeded, subsequent calls use the value provided with <code>bind-timeout</code>. The default value is used also for subsequent calls if <code>bind-timeout</code> is not specified. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>chase-referrals {YES|no}</code></p>
<dd>enable/disable automatic referral chasing, which is delegated to the underlying libldap, with rebinding eventually performed if the <code>rebind-as-user</code> directive is used. The default is to chase referrals. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>client-pr {accept-unsolicited|DISABLE|&lt;size&gt;}</code></p>
<dd>This feature allows to use RFC 2696 Paged Results control when performing search operations with a specific target, irrespective of the client&#8217;s request. When set to a numeric value, Paged Results control is always used with <i>size</i> as the page size. When set to <i>accept-unsolicited</i>, unsolicited Paged Results control responses are accepted and honored for compatibility with broken remote DSAs. The client is not exposed to paged results handling between <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5) and the remote servers. By default (disabled), Paged Results control is not used and responses are not accepted. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>default-target [&lt;target&gt;]</code></p>
<dd>The &quot;default-target&quot; directive can also be used during target specification. With no arguments it marks the current target as the default. The optional number marks target &lt;target&gt; as the default one, starting from 1. Target &lt;target&gt; must be defined. </p>
<dt><code>filter &lt;pattern&gt;</code></p>
<dd>This directive allows specifying a <code><a href="/docs/linux/man/5-regex/">regex</a></code>(5) pattern to indicate what search filter terms are actually served by a target. </p>
<p> In a search request, if the search filter matches the <i>pattern</i> the target is considered while fulfilling the request; otherwise the target is ignored. There may be multiple occurrences of the <code>filter</code> directive for each target. </p>
<dt><code>idassert-authzFrom &lt;authz-regexp&gt;</code></p>
<dd>if defined, selects what <i>local</i> identities are authorized to exploit the identity assertion feature. The string <code>&lt;authz-regexp&gt;</code> follows the rules defined for the <i>authzFrom</i> attribute. See <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), section related to <code>authz-policy</code>, for details on the syntax of this field. </p>
<dt> <code>idassert-bind</code> <code>bindmethod=none|simple|sasl [binddn=&lt;simple DN&gt;] [credentials=&lt;simple password&gt;]</code> <code>[saslmech=&lt;SASL mech&gt;] [secprops=&lt;properties&gt;] [realm=&lt;realm&gt;]</code> <code>[authcId=&lt;authentication ID&gt;] [authzId=&lt;authorization ID&gt;]</code> <code>[authz={native|proxyauthz}] [mode=&lt;mode&gt;] [flags=&lt;flags&gt;]</code> <code>[starttls=no|yes|critical]</code> <code>[tls_cert=&lt;file&gt;]</code> <code>[tls_key=&lt;file&gt;]</code> <code>[tls_cacert=&lt;file&gt;]</code> <code>[tls_cacertdir=&lt;path&gt;]</code> <code>[tls_reqcert=never|allow|try|demand]</code> <code>[tls_ciphersuite=&lt;ciphers&gt;]</code> <code>[tls_protocol_min=&lt;major&gt;[.&lt;minor&gt;]]</code> <code>[tls_crlcheck=none|peer|all]</code></p>
<dl>
<dd>
<dd>Allows to define the parameters of the authentication method that is internally used by the proxy to authorize connections that are authenticated by other databases. The identity defined by this directive, according to the properties associated to the authentication method, is supposed to have auth access on the target server to attributes used on the proxy for authentication and authorization, and to be allowed to authorize the users. This requires to have <code>proxyAuthz</code> privileges on a wide set of DNs, e.g. <code>authzTo=dn.subtree:</code>, and the remote server to have <code>authz-policy</code> set to <code>to</code> or <code>both</code>. See <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details on these statements and for remarks and drawbacks about their usage. The supported bindmethods are </p>
<p> <code>none|simple|sasl</code> </p>
<p> where <code>none</code> is the default, i.e. no <i>identity assertion</i> is performed. </p>
<p> The authz parameter is used to instruct the SASL bind to exploit <code>native </code> SASL authorization, if available; since connections are cached, this should only be used when authorizing with a fixed identity (e.g. by means of the <code>authzDN</code> or <code>authzID</code> parameters). Otherwise, the default <code>proxyauthz</code> is used, i.e. the proxyAuthz control (Proxied Authorization, RFC 4370) is added to all operations. </p>
<p> The supported modes are: </p>
<p> <code>&lt;mode&gt; := {legacy|anonymous|none|self}</code> </p>
<p> If <code>&lt;mode&gt;</code> is not present, and <code>authzId</code> is given, the proxy always authorizes that identity. <code>&lt;authorization ID&gt;</code> can be </p>
<p> <code>u:&lt;user&gt;</code> </p>
<p> <code>[dn:]&lt;DN&gt;</code> </p>
<p> The former is supposed to be expanded by the remote server according to the authz rules; see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details. In the latter case, whether or not the <code>dn:</code> prefix is present, the string must pass DN validation and normalization. </p>
<p> The default mode is <code>legacy</code>, which implies that the proxy will either perform a simple bind as the <i>authcDN</i> or a SASL bind as the <i>authcID</i> and assert the client&#8217;s identity when it is not anonymous. Direct binds are always proxied. The other modes imply that the proxy will always either perform a simple bind as the <i>authcDN</i> or a SASL bind as the <i>authcID</i>, unless restricted by <code>idassert-authzFrom</code> rules (see below), in which case the operation will fail; eventually, it will assert some other identity according to <code>&lt;mode&gt;</code>. Other identity assertion modes are <code>anonymous</code> and <code>self</code>, which respectively mean that the <i>empty </i> or the <i>client</i>&#8216;s identity will be asserted; <code>none</code>, which means that no proxyAuthz control will be used, so the <i>authcDN</i> or the <i>authcID</i> identity will be asserted. For all modes that require the use of the <i>proxyAuthz </i> control, on the remote server the proxy identity must have appropriate <i>authzTo</i> permissions, or the asserted identities must have appropriate <i>authzFrom </i> permissions. Note, however, that the ID assertion feature is mostly useful when the asserted identities do not exist on the remote server. </p>
<p> Flags can be </p>
<p> <code>override,[non-]prescriptive,proxy-authz-[non-]critical</code> </p>
<p> When the <code>override</code> flag is used, identity assertion takes place even when the database is authorizing for the identity of the client, i.e. after binding with the provided identity, and thus authenticating it, the proxy performs the identity assertion using the configured identity and authentication method. </p>
<p> When the <code>prescriptive</code> flag is used (the default), operations fail with <i>inappropriateAuthentication</i> for those identities whose assertion is not allowed by the <code>idassert-authzFrom</code> patterns. If the <code>non-prescriptive</code> flag is used, operations are performed anonymously for those identities whose assertion is not allowed by the <code>idassert-authzFrom</code> patterns. </p>
<p> When the <code>proxy-authz-non-critical</code> flag is used (the default), the proxyAuthz control is not marked as critical, in violation of RFC 4370. Use of <code>proxy-authz-critical</code> is recommended. </p>
<p> The TLS settings default to the same as the main slapd TLS settings, except for <code>tls_reqcert</code> which defaults to &quot;demand&quot;. </p>
<p> The identity associated to this directive is also used for privileged operations whenever <code>idassert-bind</code> is defined and <code>acl-bind</code> is not. See <code>acl-bind</code> for details.</dl>
<dt><code>idle-timeout &lt;time&gt;</code></p>
<dd>This directive causes a cached connection to be dropped an recreated after it has been idle for the specified time. The value can be specified as </p>
<p> [&lt;d&gt;d][&lt;h&gt;h][&lt;m&gt;m][&lt;s&gt;[s]] </p>
<p> where &lt;d&gt;, &lt;h&gt;, &lt;m&gt; and &lt;s&gt; are respectively treated as days, hours, minutes and seconds. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>keepalive &lt;idle&gt;:&lt;probes&gt;:&lt;interval&gt;</code></p>
<dd>The <code>keepalive</code> parameter sets the values of <i>idle</i>, <i>probes</i>, and <i>interval</i> used to check whether a socket is alive; <i>idle</i> is the number of seconds a connection needs to remain idle before TCP starts sending keepalive probes; <i>probes</i> is the maximum number of keepalive probes TCP should send before dropping the connection; <i>interval</i> is interval in seconds between individual keepalive probes. Only some systems support the customization of these values; the <code>keepalive</code> parameter is ignored otherwise, and system-wide settings are used. </p>
<dt><code>map {attribute|objectclass} [&lt;local name&gt;|*] {&lt;foreign name&gt;|*}</code></p>
<dd>This maps object classes and attributes as in the LDAP backend. See <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5). </p>
<dt><code>network-timeout &lt;time&gt;</code></p>
<dd>Sets the network timeout value after which <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)/<code><a href="/docs/linux/man/2-select/">select</a></code>(2) following a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) returns in case of no activity. The value is in seconds, and it can be specified as for <code>idle-timeout</code>. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>nretries {forever|never|&lt;nretries&gt;}</code></p>
<dd>This directive defines how many times a bind should be retried in case of temporary failure in contacting a target. If defined before any target specification, it applies to all targets (by default, <code>3</code> times); the global value can be overridden by redefinitions inside each target specification. </p>
<dt><code>rewrite* &#8230;</code></p>
<dd>The rewrite options are described in the &quot;REWRITING&quot; section. </p>
<dt><code>subtree-{exclude|include} &lt;rule&gt;</code></p>
<dd>This directive allows to indicate what subtrees are actually served by a target. The syntax of the supported rules is </p>
<p> <code>&lt;rule&gt;: [dn[.&lt;style&gt;]:]&lt;pattern&gt;</code> </p>
<p> <code>&lt;style&gt;: subtree|children|regex</code> </p>
<p> When <code>&lt;style&gt;</code> is either <code>subtree</code> or <code>children</code> the <code>&lt;pattern&gt;</code> is a DN that must be within the naming context served by the target. When <code>&lt;style&gt;</code> is <code>regex</code> the <code>&lt;pattern&gt;</code> is a <code><a href="/docs/linux/man/5-regex/">regex</a></code>(5) pattern. If the <code>dn.&lt;style&gt;:</code> prefix is omitted, <code>dn.subtree:</code> is implicitly assumed for backward compatibility. </p>
<p> In the <code>subtree-exclude</code> form if the <i>request DN</i> matches at least one rule, the target is not considered while fulfilling the request; otherwise, the target is considered based on the value of the <i>request DN</i>. When the request is a search, also the <i>scope</i> is considered. </p>
<p> In the <code>subtree-include</code> form if the <i>request DN</i> matches at least one rule, the target is considered while fulfilling the request; otherwise the target is ignored. </p>
</dl>
<dl>
<dd>
<pre> | match | exclude |
 +---------+---------+-------------------+
 | T | T | not candidate |
 | F | T | continue checking |
 +---------+---------+-------------------+
 | T | F | candidate |
 | F | F | not candidate |
 +---------+---------+-------------------+</pre>
</dl>
<dl>
<dd>There may be multiple occurrences of the <code>subtree-exclude</code> or <code>subtree-include</code> directive for each of the targets, but they are mutually exclusive.</dl>
<dl>
<dt><code>suffixmassage &lt;virtual naming context&gt; &lt;real naming context&gt;</code></p>
<dd>All the directives starting with &quot;rewrite&quot; refer to the rewrite engine that has been added to slapd. The &quot;suffixmassage&quot; directive was introduced in the LDAP backend to allow suffix massaging while proxying. It has been obsoleted by the rewriting tools. However, both for backward compatibility and for ease of configuration when simple suffix massage is required, it has been preserved. It wraps the basic rewriting instructions that perform suffix massaging. See the &quot;REWRITING&quot; section for a detailed list of the rewrite rules it implies. </p>
<dt><code>t-f-support {NO|yes|discover}</code></p>
<dd>enable if the remote server supports absolute filters (see <i>RFC 4526</i> for details). If set to <code>discover</code>, support is detected by reading the remote server&#8217;s root DSE. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
<dt><code>timeout [&lt;op&gt;=]&lt;val&gt; [&#8230;]</code></p>
<dd>This directive allows to set per-operation timeouts. Operations can be </p>
<p> <code>&lt;op&gt; ::= bind, add, delete, modrdn, modify, compare, search</code> </p>
<p> The overall duration of the <code>search</code> operation is controlled either by the <code>timelimit</code> parameter or by server-side enforced time limits (see <code>timelimit</code> and <code>limits</code> in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details). This <code>timeout</code> parameter controls how long the target can be irresponsive before the operation is aborted. Timeout is meaningless for the remaining operations, <code>unbind</code> and <code>abandon</code>, which do not imply any response, while it is not yet implemented in currently supported <code>extended</code> operations. If no operation is specified, the timeout <code>val</code> affects all supported operations. If specified before any target definition, it affects all targets unless overridden by per-target directives. </p>
<p> Note: if the timeout is exceeded, the operation is cancelled (according to the <code>cancel</code> directive); the protocol does not provide any means to rollback operations, so the client will not be notified about the result of the operation, which may eventually succeeded or not. In case the timeout is exceeded during a bind operation, the connection is destroyed, according to RFC4511. </p>
<dt><code>tls {[try-]start|[try-]propagate}</code></p>
<dd>execute the StartTLS extended operation when the connection is initialized; only works if the URI directive protocol scheme is not <code>ldaps://</code>. <code>propagate</code> issues the StartTLS operation only if the original connection did. The <code>try-</code> prefix instructs the proxy to continue operations if the StartTLS operation failed; its use is highly deprecated. If set before any target specification, it affects all targets, unless overridden by any per-target directive. </p>
</dl>
<h2>Scenarios</h2>
<p>A powerful (and in some sense dangerous) rewrite engine has been added to both the LDAP and Meta backends. While the former can gain limited beneficial effects from rewriting stuff, the latter can become an amazingly powerful tool. </p>
<p> Consider a couple of scenarios first. </p>
<p> 1) Two directory servers share two levels of naming context; say &quot;dc=a,dc=foo,dc=com&quot; and &quot;dc=b,dc=foo,dc=com&quot;. Then, an unambiguous Meta database can be configured as: </p>
<dl>
<dd>
<pre>database meta
suffix &quot;<code>dc=foo,dc=com</code>&quot;
uri &quot;<a href="ldap://a.foo.com/dc=a,">ldap://a.foo.com/dc=a,</a><code>dc=foo,dc=com</code>&quot;
uri &quot;<a href="ldap://b.foo.com/dc=b,">ldap://b.foo.com/dc=b,</a><code>dc=foo,dc=com</code>&quot;</pre>
</dl>
<p> Operations directed to a specific target can be easily resolved because there are no ambiguities. The only operation that may resolve to multiple targets is a search with base &quot;dc=foo,dc=com&quot; and scope at least &quot;one&quot;, which results in spawning two searches to the targets. </p>
<p> 2a) Two directory servers don&#8217;t share any portion of naming context, but they&#8217;d present as a single DIT [Caveat: uniqueness of (massaged) entries among the two servers is assumed; integrity checks risk to incur in excessive overhead and have not been implemented]. Say we have &quot;dc=bar,dc=org&quot; and &quot;o=Foo,c=US&quot;, and we&#8217;d like them to appear as branches of &quot;dc=foo,dc=com&quot;, say &quot;dc=a,dc=foo,dc=com&quot; and &quot;dc=b,dc=foo,dc=com&quot;. Then we need to configure our Meta backend as: </p>
<dl>
<dd>
<pre>database meta
suffix &quot;dc=foo,dc=com&quot;
uri &quot;<a href="ldap://a.bar.com/">ldap://a.bar.com/</a><code>dc=a,dc=foo,dc=com</code>&quot;
suffixmassage &quot;<code>dc=a,dc=foo,dc=com</code>&quot; &quot;dc=bar,dc=org&quot;
uri &quot;<a href="ldap://b.foo.com/">ldap://b.foo.com/</a><code>dc=b,dc=foo,dc=com</code>&quot;
suffixmassage &quot;<code>dc=b,dc=foo,dc=com</code>&quot; &quot;o=Foo,c=US&quot;</pre>
</dl>
<p> Again, operations can be resolved without ambiguity, although some rewriting is required. Notice that the virtual naming context of each target is a branch of the database&#8217;s naming context; it is rewritten back and forth when operations are performed towards the target servers. What &quot;back and forth&quot; means will be clarified later. </p>
<p> When a search with base &quot;dc=foo,dc=com&quot; is attempted, if the scope is &quot;base&quot; it fails with &quot;no such object&quot;; in fact, the common root of the two targets (prior to massaging) does not exist. If the scope is &quot;one&quot;, both targets are contacted with the base replaced by each target&#8217;s base; the scope is derated to &quot;base&quot;. In general, a scope &quot;one&quot; search is honored, and the scope is derated, only when the incoming base is at most one level lower of a target&#8217;s naming context (prior to massaging). </p>
<p> Finally, if the scope is &quot;sub&quot; the incoming base is replaced by each target&#8217;s unmassaged naming context, and the scope is not altered. </p>
<p> 2b) Consider the above reported scenario with the two servers sharing the same naming context: </p>
<dl>
<dd>
<pre>database meta
suffix &quot;<code>dc=foo,dc=com</code>&quot;
uri &quot;<a href="ldap://a.bar.com/">ldap://a.bar.com/</a><code>dc=foo,dc=com</code>&quot;
suffixmassage &quot;<code>dc=foo,dc=com</code>&quot; &quot;dc=bar,dc=org&quot;
uri &quot;<a href="ldap://b.foo.com/">ldap://b.foo.com/</a><code>dc=foo,dc=com</code>&quot;
suffixmassage &quot;<code>dc=foo,dc=com</code>&quot; &quot;o=Foo,c=US&quot;</pre>
</dl>
<p> All the previous considerations hold, except that now there is no way to unambiguously resolve a DN. In this case, all the operations that require an unambiguous target selection will fail unless the DN is already cached or a default target has been set. Practical configurations may result as a combination of all the above scenarios.</p>
<h2>ACLs</h2>
<p>Note on ACLs: at present you may add whatever ACL rule you desire to to the Meta (and LDAP) backends. However, the meaning of an ACL on a proxy may require some considerations. Two philosophies may be considered: </p>
<p> a) the remote server dictates the permissions; the proxy simply passes back what it gets from the remote server. </p>
<p> b) the remote server unveils &quot;everything&quot;; the proxy is responsible for protecting data from unauthorized access. </p>
<p> Of course the latter sounds unreasonable, but it is not. It is possible to imagine scenarios in which a remote host discloses data that can be considered &quot;public&quot; inside an intranet, and a proxy that connects it to the internet may impose additional constraints. To this purpose, the proxy should be able to comply with all the ACL matching criteria that the server supports. This has been achieved with regard to all the criteria supported by slapd except a special subtle case (please file an ITS if you can find other exceptions: &lt;<a rel="nofollow" href="http://www.openldap.org/its/">http://www.openldap.org/its/</a>&gt;). The rule </p>
<dl>
<dd>
<pre>access to dn=&quot;&lt;dn&gt;&quot; attrs=&lt;attr&gt;
 by dnattr=&lt;dnattr&gt; read
 by * none</pre>
</dl>
<p> cannot be matched iff the attribute that is being requested, &lt;attr&gt;, is NOT &lt;dnattr&gt;, and the attribute that determines membership, &lt;dnattr&gt;, has not been requested (e.g. in a search) </p>
<p> In fact this ACL is resolved by slapd using the portion of entry it retrieved from the remote server without requiring any further intervention of the backend, so, if the &lt;dnattr&gt; attribute has not been fetched, the match cannot be assessed because the attribute is not present, not because no value matches the requirement! </p>
<p> Note on ACLs and attribute mapping: ACLs are applied to the mapped attributes; for instance, if the attribute locally known as &quot;foo&quot; is mapped to &quot;bar&quot; on a remote server, then local ACLs apply to attribute &quot;foo&quot; and are totally unaware of its remote name. The remote server will check permissions for &quot;bar&quot;, and the local server will possibly enforce additional restrictions to &quot;foo&quot;.</p>
<h2>Rewriting</h2>
<p>A string is rewritten according to a set of rules, called a `rewrite context&#8217;. The rules are based on POSIX (&#8221;extended&#8221;) regular expressions (regex) with substring matching; basic variable substitution and map resolution of substrings is allowed by specific mechanisms detailed in the following. The behavior of pattern matching/substitution can be altered by a set of flags. </p>
<p> The underlying concept is to build a lightweight rewrite module for the slapd server (initially dedicated to the LDAP backend).</p>
<h2>Passes</h2>
<p>An incoming string is matched against a set of rules. Rules are made of a regex match pattern, a substitution pattern and a set of actions, described by a set of flags. In case of match a string rewriting is performed according to the substitution pattern that allows to refer to substrings matched in the incoming string. The actions, if any, are finally performed. The substitution pattern allows map resolution of substrings. A map is a generic object that maps a substitution pattern to a value. The flags are divided in &quot;Pattern matching Flags&quot; and &quot;Action Flags&quot;; the former alter the regex match pattern behavior while the latter alter the action that is taken after substitution.</p>
<h2>Pattern Matching Flags</h2>
<dl>
<dt><code>`C&#8217;</code></p>
<dd>honors case in matching (default is case insensitive)</p>
<dt><code>`R&#8217;</code></p>
<dd>use POSIX &#8221;basic&#8221; regular expressions (default is &#8221;extended&#8221;)</p>
<dt><code>`M{n}&#8217;</code></p>
<dd>allow no more than <code>n</code> recursive passes for a specific rule; does not alter the max total count of passes, so it can only enforce a stricter limit for a specific rule.</dl>
<h2>Action Flags</h2>
<dl>
<dt><code>`:&#8217;</code></p>
<dd>apply the rule once only (default is recursive)</p>
<dt><code>`@&#8217;</code></p>
<dd>stop applying rules in case of match; the current rule is still applied recursively; combine with `:&#8217; to apply the current rule only once and then stop.</p>
<dt><code>`#&#8217;</code></p>
<dd>stop current operation if the rule matches, and issue an `unwilling to perform&#8217; error.</p>
<dt><code>`G{n}&#8217;</code></p>
<dd>jump <code>n</code> rules back and forth (watch for loops!). Note that `G{1}&#8217; is implicit in every rule.</p>
<dt><code>`I&#8217;</code></p>
<dd>ignores errors in rule; this means, in case of error, e.g. issued by a map, the error is treated as a missed match. The `unwilling to perform&#8217; is not overridden.</p>
<dt><code>`U{n}&#8217;</code></p>
<dd>uses <code>n</code> as return code if the rule matches; the flag does not alter the recursive behavior of the rule, so, to have it performed only once, it must be used in combination with `:&#8217;, e.g. <code>`:U{16}&#8217;</code> returns the value `16&#8242; after exactly one execution of the rule, if the pattern matches. As a consequence, its behavior is equivalent to `@&#8217;, with the return code set to <code>n</code>; or, in other words, `@&#8217; is equivalent to `U{0}&#8217;. By convention, the freely available codes are above 16 included; the others are reserved.</dl>
<p> The ordering of the flags can be significant. For instance: `IG{2}&#8217; means ignore errors and jump two lines ahead both in case of match and in case of error, while `G{2}I&#8217; means ignore errors, but jump two lines ahead only in case of match. </p>
<p> More flags (mainly Action Flags) will be added as needed.</p>
<h2>Pattern matching:</h2>
<p>See <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7).</p>
<h2>Substitution Pattern Syntax:</h2>
<p>Everything starting with `%&#8217; requires substitution; </p>
<p> the only obvious exception is `%%&#8217;, which is left as is; </p>
<p> the basic substitution is `%d&#8217;, where `d&#8217; is a digit; 0 means the whole string, while 1-9 is a submatch; </p>
<p> a `%&#8217; followed by a `{&#8216; invokes an advanced substitution. The pattern is: </p>
<dl>
<dd>`%&#8217; `{&#8216; [ &lt;op&gt; ] &lt;name&gt; `(&#8216; &lt;substitution&gt; `)&#8217; `}&#8217;</dl>
<p> where &lt;name&gt; must be a legal name for the map, i.e. </p>
<dl>
<dd>
<pre>&lt;name&gt; ::= [a-z][a-z0-9]* (case insensitive)
&lt;op&gt; ::= `&gt;' `|' `&amp;' `&amp;&amp;' `*' `**' `$'</pre>
</dl>
<p> and &lt;substitution&gt; must be a legal substitution pattern, with no limits on the nesting level. </p>
<p> The operators are:</p>
<dl>
<dt><code>&gt;</code></p>
<dd>sub context invocation; &lt;name&gt; must be a legal, already defined rewrite context name</p>
<dt><code>|</code></p>
<dd>external command invocation; &lt;name&gt; must refer to a legal, already defined command name (NOT IMPL.)</p>
<dt><code>&amp;</code></p>
<dd>variable assignment; &lt;name&gt; defines a variable in the running operation structure which can be dereferenced later; operator <code>&amp;</code> assigns a variable in the rewrite context scope; operator <code>&amp;&amp;</code> assigns a variable that scopes the entire session, e.g. its value can be dereferenced later by other rewrite contexts</p>
<dt><code>*</code></p>
<dd>variable dereferencing; &lt;name&gt; must refer to a variable that is defined and assigned for the running operation; operator <code>*</code> dereferences a variable scoping the rewrite context; operator <code>**</code> dereferences a variable scoping the whole session, e.g. the value is passed across rewrite contexts</p>
<dt><code>$</code></p>
<dd>parameter dereferencing; &lt;name&gt; must refer to an existing parameter; the idea is to make some run-time parameters set by the system available to the rewrite engine, as the client host name, the bind DN if any, constant parameters initialized at config time, and so on; no parameter is currently set by either <code>back-ldap</code> or <code>back-meta</code>, but constant parameters can be defined in the configuration file by using the <code>rewriteParam</code> directive.</dl>
<p> Substitution escaping has been delegated to the `%&#8217; symbol, which is used instead of `\&#8217; in string substitution patterns because `\&#8217; is already escaped by slapd&#8217;s low level parsing routines; as a consequence, regex escaping requires two `\&#8217; symbols, e.g. `<code>.*\.foo\.bar</code>&#8216; must be written as `<code>.*\.foo\.bar</code>&#8216;.</p>
<h2>Rewrite context:</h2>
<p>A rewrite context is a set of rules which are applied in sequence. The basic idea is to have an application initialize a rewrite engine (think of Apache&#8217;s mod_rewrite &#8230;) with a set of rewrite contexts; when string rewriting is required, one invokes the appropriate rewrite context with the input string and obtains the newly rewritten one if no errors occur. </p>
<p> Each basic server operation is associated to a rewrite context; they are divided in two main groups: client -&gt; server and server -&gt; client rewriting. </p>
<p> client -&gt; server: </p>
<dl>
<dd>
<pre>(default) if defined and no specific context 
 is available
bindDN bind
searchBase search
searchFilter search
searchFilterAttrDN search
compareDN compare
compareAttrDN compare AVA
addDN add
addAttrDN add AVA
modifyDN modify
modifyAttrDN modify AVA
modrDN modrdn
newSuperiorDN modrdn
deleteDN delete
exopPasswdDN password modify extended operation DN if proxy</pre>
</dl>
<p> server -&gt; client: </p>
<dl>
<dd>
<pre>searchResult search (only if defined; no default;
 acts on DN and DN-syntax attributes 
 of search results)
searchAttrDN search AVA
matchedDN all ops (only if applicable)</pre>
</dl>
<h2>Basic configuration syntax</h2>
<dl>
<dt><code>rewriteEngine { on | off }</code></p>
<dd>If `on&#8217;, the requested rewriting is performed; if `off&#8217;, no rewriting takes place (an easy way to stop rewriting without altering too much the configuration file).</p>
<dt><code>rewriteContext &lt;context name&gt; [ alias &lt;aliased context name&gt; ]</code></p>
<dd>&lt;Context name&gt; is the name that identifies the context, i.e. the name used by the application to refer to the set of rules it contains. It is used also to reference sub contexts in string rewriting. A context may alias another one. In this case the alias context contains no rule, and any reference to it will result in accessing the aliased one.</p>
<dt><code>rewriteRule &lt;regex match pattern&gt; &lt;substitution pattern&gt; [ &lt;flags&gt; ]</code></p>
<dd>Determines how a string can be rewritten if a pattern is matched. Examples are reported below.</dl>
<h2>Additional configuration syntax:</h2>
<dl>
<dt><code>rewriteMap &lt;map type&gt; &lt;map name&gt; [ &lt;map attrs&gt; ]</code></p>
<dd>Allows to define a map that transforms substring rewriting into something else. The map is referenced inside the substitution pattern of a rule.</p>
<dt><code>rewriteParam &lt;param name&gt; &lt;param value&gt;</code></p>
<dd>Sets a value with global scope, that can be dereferenced by the command `%{$paramName}&#8217;.</p>
<dt><code>rewriteMaxPasses &lt;number of passes&gt; [&lt;number of passes per rule&gt;]</code></p>
<dd>Sets the maximum number of total rewriting passes that can be performed in a single rewrite operation (to avoid loops). A safe default is set to 100; note that reaching this limit is still treated as a success; recursive invocation of rules is simply interrupted. The count applies to the rewriting operation as a whole, not to any single rule; an optional per-rule limit can be set. This limit is overridden by setting specific per-rule limits with the `M{n}&#8217; flag.</dl>
<h2>Configuration examples:</h2>
<pre># set to `off' to disable rewriting
rewriteEngine on
# the rules the &quot;suffixmassage&quot; directive implies
rewriteEngine on
# all dataflow from client to server referring to DNs
rewriteContext default
rewriteRule &quot;(.*)&lt;virtualnamingcontext&gt;$&quot; &quot;%1&lt;realnamingcontext&gt;&quot; &quot;:&quot;
# empty filter rule
rewriteContext searchFilter
# all dataflow from server to client
rewriteContext searchResult
rewriteRule &quot;(.*)&lt;realnamingcontext&gt;$&quot; &quot;%1&lt;virtualnamingcontext&gt;&quot; &quot;:&quot;
rewriteContext searchAttrDN alias searchResult
rewriteContext matchedDN alias searchResult
# Everything defined here goes into the `default' context.
# This rule changes the naming context of anything sent
# to `dc=home,dc=net' to `dc=OpenLDAP, dc=org'
rewriteRule &quot;(.*)dc=home,[ ]?dc=net&quot;
 &quot;%1dc=OpenLDAP, dc=org&quot; &quot;:&quot;
# since a pretty/normalized DN does not include spaces
# after rdn separators, e.g. `,', this rule suffices:
rewriteRule &quot;(.*)dc=home,dc=net&quot;
 &quot;%1dc=OpenLDAP,dc=org&quot; &quot;:&quot;
# Start a new context (ends input of the previous one).
# This rule adds blanks between DN parts if not present.
rewriteContext addBlanks
rewriteRule &quot;(.*),([^ ].*)&quot; &quot;%1, %2&quot;
# This one eats blanks
rewriteContext eatBlanks
rewriteRule &quot;(.*),[ ](.*)&quot; &quot;%1,%2&quot;
# Here control goes back to the default rewrite
# context; rules are appended to the existing ones.
# anything that gets here is piped into rule `addBlanks'
rewriteContext default
rewriteRule &quot;.*&quot; &quot;%{&gt;addBlanks(%0)}&quot; &quot;:&quot;
# Rewrite the search base according to `default' rules.
rewriteContext searchBase alias default
# Search results with OpenLDAP DN are rewritten back with
# `dc=home,dc=net' naming context, with spaces eaten.
rewriteContext searchResult
rewriteRule &quot;(.*[^ ]?)[ ]?dc=OpenLDAP,[ ]?dc=org&quot;
 &quot;%{&gt;eatBlanks(%1)}dc=home,dc=net&quot; &quot;:&quot;
# Bind with email instead of full DN: we first need
# an ldap map that turns attributes into a DN (the
# argument used when invoking the map is appended to 
# the URI and acts as the filter portion)
rewriteMap ldap attr2dn &quot;<a href="ldap://host/dc=my,dc=org?dn?sub">ldap://host/dc=my,dc=org?dn?sub</a>&quot;
# Then we need to detect DN made up of a single email,
# e.g. `mail=someone [at] example.com'; note that the rule
# in case of match stops rewriting; in case of error,
# it is ignored. In case we are mapping virtual
# to real naming contexts, we also need to rewrite
# regular DNs, because the definition of a bindDn
# rewrite context overrides the default definition.
rewriteContext bindDN
rewriteRule &quot;^mail=[^,]+@[^,]+$&quot; &quot;%{attr2dn(%0)}&quot; &quot;:@I&quot;
# This is a rather sophisticated example. It massages a
# search filter in case who performs the search has
# administrative privileges. First we need to keep
# track of the bind DN of the incoming request, which is
# stored in a variable called `binddn' with session scope,
# and left in place to allow regular binding:
rewriteContext bindDN
rewriteRule &quot;.+&quot; &quot;%{&amp;&amp;binddn(%0)}%0&quot; &quot;:&quot;
# A search filter containing `uid=' is rewritten only
# if an appropriate DN is bound.
# To do this, in the first rule the bound DN is
# dereferenced, while the filter is decomposed in a
# prefix, in the value of the `uid=&lt;arg&gt;' AVA, and 
# in a suffix. A tag `&lt;&gt;' is appended to the DN. 
# If the DN refers to an entry in the `ou=admin' subtree, 
# the filter is rewritten OR-ing the `uid=&lt;arg&gt;' with
# `cn=&lt;arg&gt;'; otherwise it is left as is. This could be
# useful, for instance, to allow apache's auth_ldap-1.4
# module to authenticate users with both `uid' and
# `cn', but only if the request comes from a possible
# `cn=Web auth,ou=admin,dc=home,dc=net' user.
rewriteContext searchFilter
rewriteRule &quot;(.*\()uid=([a-z0-9_]+)(\).*)&quot;
 &quot;%{**binddn}&lt;&gt;%{&amp;prefix(%1)}%{&amp;arg(%2)}%{&amp;suffix(%3)}&quot;
 &quot;:I&quot;
rewriteRule &quot;[^,]+,ou=admin,dc=home,dc=net&quot;
 &quot;%{*prefix}|(uid=%{*arg})(cn=%{*arg})%{*suffix}&quot; &quot;:@I&quot;
rewriteRule &quot;.*&lt;&gt;&quot; &quot;%{*prefix}uid=%{*arg}%{*suffix}&quot; &quot;:&quot;
# This example shows how to strip unwanted DN-valued
# attribute values from a search result; the first rule
# matches DN values below &quot;ou=People,dc=example,dc=com&quot;;
# in case of match the rewriting exits successfully.
# The second rule matches everything else and causes
# the value to be rejected.
rewriteContext searchResult
rewriteRule &quot;.*,ou=People,dc=example,dc=com&quot; &quot;%0&quot; &quot;:@&quot;
rewriteRule &quot;.*&quot; &quot;&quot; &quot;#&quot;</pre>
<h2>LDAP Proxy resolution (a possible evolution of <a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a>(5)):</h2>
<p>In case the rewritten DN is an LDAP URI, the operation is initiated towards the host[:port] indicated in the uri, if it does not refer to the local server. E.g.: </p>
<pre> rewriteRule '^cn=root,.*' '%0' 'G{3}'
 rewriteRule '^cn=[a-l].*' '<a href="ldap://ldap1.my.org/%0'">ldap://ldap1.my.org/%0'</a> ':@'
 rewriteRule '^cn=[m-z].*' '<a href="ldap://ldap2.my.org/%0'">ldap://ldap2.my.org/%0'</a> ':@'
 rewriteRule '.*' '<a href="ldap://ldap3.my.org/%0'">ldap://ldap3.my.org/%0'</a> ':@'</pre>
<p>(Rule 1 is simply there to illustrate the `G{n}&#8217; action; it could have been written: </p>
<pre> rewriteRule '^cn=root,.*' '<a href="ldap://ldap3.my.org/%0'">ldap://ldap3.my.org/%0'</a> ':@'</pre>
<p>with the advantage of saving one rewrite pass &#8230;)</p>
<h2>Access Control</h2>
<p>The <code>meta</code> backend does not honor all ACL semantics as described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). In general, access checking is delegated to the remote server(s). Only <code>read (=r)</code> access to the <code>entry</code> pseudo-attribute and to the other attribute values of the entries returned by the <code>search</code> operation is honored, which is performed by the frontend.</p>
<h2>Proxy Cache Overlay</h2>
<p>The proxy cache overlay allows caching of LDAP search requests (queries) in a local database. See <code><a href="/docs/linux/man/5-slapo-pcache/">slapo-pcache</a></code>(5) for details.</p>
<h2>Deprecated Statements</h2>
<p>The following statements have been deprecated and should no longer be used. </p>
<dl>
<dt><code>pseudorootdn &lt;substitute DN in case of rootdn bind&gt;</code></p>
<dd>Use <code>idassert-bind</code> instead. </p>
<dt><code>pseudorootpw &lt;substitute password in case of rootdn bind&gt;</code></p>
<dd>Use <code>idassert-bind</code> instead. </p>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-slapo-pcache/">slapo-pcache</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7).</p>
<h2>Author</h2>
<p>Pierangelo Masarati, based on back-ldap by Howard Chu</p>
