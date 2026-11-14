---
title: "slapo-rwm(5)"
name: "slapo-rwm"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-rwm/"
description: "slapo-rwm – rewrite/remap overlay to slapd"
---

<p>slapo-rwm &#8211; rewrite/remap overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>rwm</code> overlay to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) performs basic DN/data rewrite and objectClass/attributeType mapping. Its usage is mostly intended to provide virtual views of existing data either remotely, in conjunction with the proxy backend described in <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), or locally, in conjunction with the relay backend described in <code><a href="/docs/linux/man/5-slapd-relay/">slapd-relay</a></code>(5). </p>
<p> This overlay is experimental.</p>
<h2>Mapping</h2>
<p>An important feature of the <code>rwm</code> overlay is the capability to map objectClasses and attributeTypes from the local set (or a subset of it) to a foreign set, and vice versa. This is accomplished by means of the <code>rwm-map</code> directive.</p>
<dl>
<dt><code>rwm-map {attribute | objectclass} [&lt;local name&gt; | *] {&lt;foreign name&gt; | *}</code></p>
<dd>Map attributeTypes and objectClasses from the foreign server to different values on the local slapd. The reason is that some attributes might not be part of the local slapd&#8217;s schema, some attribute names might be different but serve the same purpose, etc. If local or foreign name is `*&#8217;, the name is preserved. If local name is omitted, the foreign name is removed. Unmapped names are preserved if both local and foreign name are `*&#8217;, and removed if local name is omitted and foreign name is `*&#8217;.</dl>
<p> The local <i>objectClasses </i> and <i>attributeTypes </i> must be defined in the local schema; the foreign ones do not have to, but users are encouraged to explicitly define the remote attributeTypes and the objectClasses they intend to map. All in all, when remapping a remote server via back-ldap (<code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5)) or back-meta (<code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5)) their definition can be easily obtained by querying the <i>subschemaSubentry</i> of the remote server; the problem should not exist when remapping a local database. Note, however, that the decision whether to rewrite or not attributeTypes with <i>distinguishedName syntax</i>, requires the knowledge of the attributeType syntax. See the REWRITING section for details. </p>
<p> Note that when mapping DN-valued attributes from local to remote, first the DN is rewritten, and then the attributeType is mapped; while mapping from remote to local, first the attributeType is mapped, and then the DN is rewritten. As such, it is important that the local attributeType is appropriately defined as using the distinguishedName syntax. Also, note that there are DN-related syntaxes (i.e. compound types with a portion that is DN-valued), like nameAndOptionalUID, whose values are currently not rewritten. </p>
<p> If the foreign type of an attribute mapping is not defined on the local server, it might be desirable to have the attribute values normalized after the mapping process. Not normalizing the values can lead to wrong results, when the <code>rwm</code> overlay is used together with e.g. the <code>pcache</code> overlay. This normalization can be enabled by means of the <code>rwm-normalize-mapped-attrs</code> directive.</p>
<dl>
<dt><code>rwm-normalize-mapped-attrs {yes|no}</code></p>
<dd>Set this to &quot;yes&quot;, if the <code>rwm</code> overlay should try to normalize the values of attributes that are mapped from an attribute type that is unknown to the local server. The default value of this setting is &quot;no&quot;.</p>
<dt><code>rwm-drop-unrequested-attrs {yes|no}</code></p>
<dd>Set this to &quot;yes&quot;, if the <code>rwm</code> overlay should drop attributes that are not explicitly requested by a search operation. When this is set to &quot;no&quot;, the <code>rwm</code> overlay will leave all attributes in place, so that subsequent modules can further manipulate them. In any case, unrequested attributes will be omitted from search results by the frontend, when the search entry response package is encoded. The default value of this setting is &quot;yes&quot;.</dl>
<h2>Suffix Massaging</h2>
<p>A basic feature of the <code>rwm</code> overlay is the capability to perform suffix massaging between a virtual and a real naming context by means of the <code>rwm-suffixmassage</code> directive. This, in conjunction with proxy backends, <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) and <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5), or with the relay backend, <code><a href="/docs/linux/man/5-slapd-relay/">slapd-relay</a></code>(5), allows to create virtual views of databases. A distinguishing feature of this overlay is that, when instantiated before any database, it can modify the DN of requests <i>before</i> database selection. For this reason, rules that rewrite the empty DN (&quot;&quot;) or the subschemaSubentry DN (usually &quot;cn=subschema&quot;), would prevent clients from reading the root DSE or the DSA&#8217;s schema.</p>
<dl>
<dt><code>rwm-suffixmassage [&lt;virtual naming context&gt;] &lt;real naming context&gt;</code></p>
<dd>Shortcut to implement naming context rewriting; the trailing part of the DN is rewritten from the virtual to the real naming context in the bindDN, searchDN, searchFilterAttrDN, compareDN, compareAttrDN, addDN, addAttrDN, modifyDN, modifyAttrDN, modrDN, newSuperiorDN, deleteDN, exopPasswdDN, and from the real to the virtual naming context in the searchEntryDN, searchAttrDN and matchedDN rewrite contexts. By default no rewriting occurs for the searchFilter and for the referralAttrDN and referralDN rewrite contexts. If no <i>&lt;virtual naming context&gt;</i> is given, the first suffix of the database is used; this requires the <code>rwm-suffixmassage</code> directive be defined <i>after</i> the database <code>suffix</code> directive. The <code>rwm-suffixmassage</code> directive automatically sets the <code>rwm-rewriteEngine</code> to <code>ON</code>.</dl>
<p> See the REWRITING section for details.</p>
<h2>Rewriting</h2>
<p>A string is rewritten according to a set of rules, called a `rewrite context&#8217;. The rules are based on POSIX (&#8221;extended&#8221;) regular expressions with substring matching; basic variable substitution and map resolution of substrings is allowed by specific mechanisms detailed in the following. The behavior of pattern matching/substitution can be altered by a set of flags. </p>
<dl>
<dd>
<pre>&lt;rewrite context&gt; ::= &lt;rewrite rule&gt; [...]
&lt;rewrite rule&gt; ::= &lt;pattern&gt; &lt;action&gt; [&lt;flags&gt;]</pre>
</dl>
<p> The underlying concept is to build a lightweight rewrite module for the slapd server (initially dedicated to the LDAP backend):</p>
<h2>Passes</h2>
<p>An incoming string is matched against a set of <i>rewriteRules</i>. Rules are made of a <i>regex match pattern</i>, a <i>substitution pattern</i> and a set of actions, described by a set of <i>optional flags</i>. In case of match, string rewriting is performed according to the substitution pattern that allows to refer to substrings matched in the incoming string. The actions, if any, are finally performed. Each rule is executed recursively, unless altered by specific action flags; see &quot;Action Flags&quot; for details. A default limit on the recursion level is set, and can be altered by the <code>rwm-rewriteMaxPasses</code> directive, as detailed in the &quot;Additional Configuration Syntax&quot; section. The substitution pattern allows map resolution of substrings. A map is a generic object that maps a substitution pattern to a value. The flags are divided in &quot;Pattern Matching Flags&quot; and &quot;Action Flags&quot;; the former alter the regex match pattern behavior, while the latter alter the actions that are taken after substitution.</p>
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
<dd>uses <code>n</code> as return code if the rule matches; the flag does not alter the recursive behavior of the rule, so, to have it performed only once, it must be used in combination with `:&#8217;, e.g. <code>`:U{32}&#8217;</code> returns the value `32&#8242; (indicating noSuchObject) after exactly one execution of the rule, if the pattern matches. As a consequence, its behavior is equivalent to `@&#8217;, with the return code set to <code>n</code>; or, in other words, `@&#8217; is equivalent to `U{0}&#8217;. Positive errors are allowed, indicating the related LDAP error codes as specified in <i>draft-ietf-ldapbis-protocol</i>.</dl>
<p> The ordering of the flags can be significant. For instance: `IG{2}&#8217; means ignore errors and jump two lines ahead both in case of match and in case of error, while `G{2}I&#8217; means ignore errors, but jump two lines ahead only in case of match. </p>
<p> More flags (mainly Action Flags) will be added as needed.</p>
<h2>Pattern Matching</h2>
<p>See <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7).</p>
<h2>Substitution Pattern Syntax</h2>
<p>Everything starting with `$&#8217; requires substitution; </p>
<p> the only obvious exception is `$$&#8217;, which is turned into a single `$&#8217;; </p>
<p> the basic substitution is `$&lt;d&gt;&#8217;, where `&lt;d&gt;&#8217; is a digit; 0 means the whole string, while 1-9 is a submatch, as discussed in <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7). </p>
<p> a `$&#8217; followed by a `{&#8216; invokes an advanced substitution. The pattern is: </p>
<dl>
<dd>`$&#8217; `{&#8216; [ &lt;operator&gt; ] &lt;name&gt; `(&#8216; &lt;substitution&gt; `)&#8217; `}&#8217;</dl>
<p> where &lt;name&gt; must be a legal name for the map, i.e. </p>
<dl>
<dd>
<pre>&lt;name&gt; ::= [a-z][a-z0-9]* (case insensitive)
&lt;operator&gt; ::= `&gt;' `|' `&amp;' `&amp;&amp;' `*' `**' `$'</pre>
</dl>
<p> and &lt;substitution&gt; must be a legal substitution pattern, with no limits on the nesting level. </p>
<p> The operators are:</p>
<dl>
<dt><code>&gt;</code></p>
<dd>sub-context invocation; &lt;name&gt; must be a legal, already defined rewrite context name</p>
<dt><code>|</code></p>
<dd>external command invocation; &lt;name&gt; must refer to a legal, already defined command name (NOT IMPLEMENTED YET)</p>
<dt><code>&amp;</code></p>
<dd>variable assignment; &lt;name&gt; defines a variable in the running operation structure which can be dereferenced later; operator <code>&amp;</code> assigns a variable in the rewrite context scope; operator <code>&amp;&amp;</code> assigns a variable that scopes the entire session, e.g. its value can be dereferenced later by other rewrite contexts</p>
<dt><code>*</code></p>
<dd>variable dereferencing; &lt;name&gt; must refer to a variable that is defined and assigned for the running operation; operator <code>*</code> dereferences a variable scoping the rewrite context; operator <code>**</code> dereferences a variable scoping the whole session, e.g. the value is passed across rewrite contexts</p>
<dt><code>$</code></p>
<dd>parameter dereferencing; &lt;name&gt; must refer to an existing parameter; the idea is to make some run-time parameters set by the system available to the rewrite engine, as the client host name, the bind DN if any, constant parameters initialized at config time, and so on; no parameter is currently set by either <code>back-ldap</code> or <code>back-meta</code>, but constant parameters can be defined in the configuration file by using the <code>rewriteParam</code> directive.</dl>
<p> Substitution escaping has been delegated to the `$&#8217; symbol, which is used instead of `\&#8217; in string substitution patterns because `\&#8217; is already escaped by slapd&#8217;s low level parsing routines; as a consequence, regex escaping requires two `\&#8217; symbols, e.g. `<code>.*\.foo\.bar</code>&#8216; must be written as `<code>.*\.foo\.bar</code>&#8216;.</p>
<h2>Rewrite Context</h2>
<p>A rewrite context is a set of rules which are applied in sequence. The basic idea is to have an application initialize a rewrite engine (think of Apache&#8217;s mod_rewrite &#8230;) with a set of rewrite contexts; when string rewriting is required, one invokes the appropriate rewrite context with the input string and obtains the newly rewritten one if no errors occur. </p>
<p> Each basic server operation is associated to a rewrite context; they are divided in two main groups: client -&gt; server and server -&gt; client rewriting. </p>
<p> client -&gt; server: </p>
<dl>
<dd>
<pre>(default) if defined and no specific context 
 is available
bindDN bind
searchDN search
searchFilter search
searchFilterAttrDN search
compareDN compare
compareAttrDN compare AVA
addDN add
addAttrDN add AVA (DN portion of &quot;ref&quot; excluded)
modifyDN modify
modifyAttrDN modify AVA (DN portion of &quot;ref&quot; excluded)
referralAttrDN add/modify DN portion of referrals
 (default to none)
renameDN modrdn (the old DN)
newSuperiorDN modrdn (the new parent DN, if any)
newRDN modrdn (the new relative DN)
deleteDN delete
exopPasswdDN password modify extended operation DN</pre>
</dl>
<p> server -&gt; client: </p>
<dl>
<dd>
<pre>searchEntryDN search (only if defined; no default;
 acts on DN of search entries)
searchAttrDN search AVA (only if defined; defaults
 to searchEntryDN; acts on DN-syntax
 attributes of search results)
matchedDN all ops (only if applicable; defaults
 to searchEntryDN)
referralDN all ops (only if applicable; defaults
 to none)</pre>
</dl>
<h2>Basic Configuration Syntax</h2>
<p>All rewrite/remap directives start with the prefix <code>rwm-</code>; for backwards compatibility with the historical <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) and <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5) builtin rewrite/remap capabilities, the prefix may be omitted, but this practice is strongly discouraged.</p>
<dl>
<dt><code>rwm-rewriteEngine { on | off }</code></p>
<dd>If `on&#8217;, the requested rewriting is performed; if `off&#8217;, no rewriting takes place (an easy way to stop rewriting without altering too much the configuration file).</p>
<dt><code>rwm-rewriteContext &lt;context name&gt; [ alias &lt;aliased context name&gt; ]</code></p>
<dd>&lt;Context name&gt; is the name that identifies the context, i.e. the name used by the application to refer to the set of rules it contains. It is used also to reference sub contexts in string rewriting. A context may alias another one. In this case the alias context contains no rule, and any reference to it will result in accessing the aliased one.</p>
<dt><code>rwm-rewriteRule &lt;regex match pattern&gt; &lt;substitution pattern&gt; [ &lt;flags&gt; ]</code></p>
<dd>Determines how a string can be rewritten if a pattern is matched. Examples are reported below.</dl>
<h2>Additional Configuration Syntax</h2>
<dl>
<dt><code>rwm-rewriteMap &lt;map type&gt; &lt;map name&gt; [ &lt;map attrs&gt; ]</code></p>
<dd>Allows to define a map that transforms substring rewriting into something else. The map is referenced inside the substitution pattern of a rule.</p>
<dt><code>rwm-rewriteParam &lt;param name&gt; &lt;param value&gt;</code></p>
<dd>Sets a value with global scope, that can be dereferenced by the command `${$paramName}&#8217;.</p>
<dt><code>rwm-rewriteMaxPasses &lt;number of passes&gt; [&lt;number of passes per rule&gt;]</code></p>
<dd>Sets the maximum number of total rewriting passes that can be performed in a single rewrite operation (to avoid loops). A safe default is set to 100; note that reaching this limit is still treated as a success; recursive invocation of rules is simply interrupted. The count applies to the rewriting operation as a whole, not to any single rule; an optional per-rule limit can be set. This limit is overridden by setting specific per-rule limits with the `M{n}&#8217; flag. </p>
</dl>
<h2>Maps</h2>
<p>Currently, few maps are builtin but additional map types may be registered at runtime. </p>
<p> Supported maps are:</p>
<dl>
<dt><code>LDAP &lt;URI&gt; [bindwhen=&lt;when&gt;] [version=&lt;version&gt;] [binddn=&lt;DN&gt;] [credentials=&lt;cred&gt;]</code></p>
<dd>The <code>LDAP</code> map expands a value by performing a simple LDAP search. Its configuration is based on a mandatory URI, whose <code>attrs</code> portion must contain exactly one attribute (use <code>entryDN</code> to fetch the DN of an entry). If a multi-valued attribute is used, only the first value is considered. </p>
<p> The parameter <code>bindwhen</code> determines when the connection is established. It can take the values <code>now</code>, <code>later</code>, and <code>everytime</code>, respectively indicating that the connection should be created at startup, when required, or any time it is used. In the former two cases, the connection is cached, while in the latter a fresh new one is used all times. This is the default. </p>
<p> The parameters <code>binddn</code> and <code>credentials</code> represent the DN and the password that is used to perform an authenticated simple bind before performing the search operation; if not given, an anonymous connection is used. </p>
<p> The parameter <code>version</code> can be 2 or 3 to indicate the protocol version that must be used. The default is 3. </p>
<dt><code>slapd &lt;URI&gt;</code></p>
<dd>The <code>slapd</code> map expands a value by performing an internal LDAP search. Its configuration is based on a mandatory URI, which must begin with <code><a href="ldap:///">ldap:///</a></code> (i.e., it must be an LDAP URI and it must not specify a host). As with the LDAP map, the <code>attrs</code> portion must contain exactly one attribute, and if a multi-valued attribute is used, only the first value is considered. </p>
</dl>
<h2>Rewrite Configuration Examples</h2>
<pre># set to `off' to disable rewriting
rwm-rewriteEngine on
# the rules the &quot;suffixmassage&quot; directive implies
rwm-rewriteEngine on
# all dataflow from client to server referring to DNs
rwm-rewriteContext default
rwm-rewriteRule &quot;(.+,)?&lt;virtualnamingcontext&gt;$&quot; &quot;$1&lt;realnamingcontext&gt;&quot; &quot;:&quot;
# empty filter rule
rwm-rewriteContext searchFilter
# all dataflow from server to client
rwm-rewriteContext searchEntryDN
rwm-rewriteRule &quot;(.+,)?&lt;realnamingcontext&gt;$&quot; &quot;$1&lt;virtualnamingcontext&gt;&quot; &quot;:&quot;
rwm-rewriteContext searchAttrDN alias searchEntryDN
rwm-rewriteContext matchedDN alias searchEntryDN
# misc empty rules
rwm-rewriteContext referralAttrDN
rwm-rewriteContext referralDN
# Everything defined here goes into the `default' context.
# This rule changes the naming context of anything sent
# to `dc=home,dc=net' to `dc=OpenLDAP, dc=org'
rwm-rewriteRule &quot;(.+,)?dc=home,[ ]?dc=net$&quot;
 &quot;$1dc=OpenLDAP, dc=org&quot; &quot;:&quot;
# since a pretty/normalized DN does not include spaces
# after rdn separators, e.g. `,', this rule suffices:
rwm-rewriteRule &quot;(.+,)?dc=home,dc=net$&quot;
 &quot;$1dc=OpenLDAP,dc=org&quot; &quot;:&quot;
# Start a new context (ends input of the previous one).
# This rule adds blanks between DN parts if not present.
rwm-rewriteContext addBlanks
rwm-rewriteRule &quot;(.*),([^ ].*)&quot; &quot;$1, $2&quot;
# This one eats blanks
rwm-rewriteContext eatBlanks
rwm-rewriteRule &quot;(.*), (.*)&quot; &quot;$1,$2&quot;
# Here control goes back to the default rewrite
# context; rules are appended to the existing ones.
# anything that gets here is piped into rule `addBlanks'
rwm-rewriteContext default
rwm-rewriteRule &quot;.*&quot; &quot;${&gt;addBlanks($0)}&quot; &quot;:&quot;
# Rewrite the search base according to `default' rules.
rwm-rewriteContext searchDN alias default
# Search results with OpenLDAP DN are rewritten back with
# `dc=home,dc=net' naming context, with spaces eaten.
rwm-rewriteContext searchEntryDN
rwm-rewriteRule &quot;(.*[^ ],)?[ ]?dc=OpenLDAP,[ ]?dc=org$&quot;
 &quot;${&gt;eatBlanks($1)}dc=home,dc=net&quot; &quot;:&quot;
# Bind with email instead of full DN: we first need
# an ldap map that turns attributes into a DN (the
# argument used when invoking the map is appended to 
# the URI and acts as the filter portion)
rwm-rewriteMap ldap attr2dn &quot;<a href="ldap://host/dc=my,dc=org?dn?sub">ldap://host/dc=my,dc=org?dn?sub</a>&quot;
# Then we need to detect DN made up of a single email,
# e.g. `mail=someone [at] example.com'; note that the rule
# in case of match stops rewriting; in case of error,
# it is ignored. In case we are mapping virtual
# to real naming contexts, we also need to rewrite
# regular DNs, because the definition of a bindDN
# rewrite context overrides the default definition.
rwm-rewriteContext bindDN
rwm-rewriteRule &quot;^mail=[^,]+@[^,]+$&quot; &quot;${attr2dn($0)}&quot; &quot;:@I&quot;
# This is a rather sophisticated example. It massages a
# search filter in case who performs the search has
# administrative privileges. First we need to keep
# track of the bind DN of the incoming request, which is
# stored in a variable called `binddn' with session scope,
# and left in place to allow regular binding:
rwm-rewriteContext bindDN
rwm-rewriteRule &quot;.+&quot; &quot;${&amp;&amp;binddn($0)}$0&quot; &quot;:&quot;
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
rwm-rewriteContext searchFilter
rwm-rewriteRule &quot;(.*\()uid=([a-z0-9_]+)(\).*)&quot;
 &quot;${**binddn}&lt;&gt;${&amp;prefix($1)}${&amp;arg($2)}${&amp;suffix($3)}&quot;
 &quot;:I&quot;
rwm-rewriteRule &quot;^[^,]+,ou=admin,dc=home,dc=net$&quot;
 &quot;${*prefix}|(uid=${*arg})(cn=${*arg})${*suffix}&quot; &quot;:@I&quot;
rwm-rewriteRule &quot;.*&lt;&gt;$&quot; &quot;${*prefix}uid=${*arg}${*suffix}&quot; &quot;:&quot;
# This example shows how to strip unwanted DN-valued
# attribute values from a search result; the first rule
# matches DN values below &quot;ou=People,dc=example,dc=com&quot;;
# in case of match the rewriting exits successfully.
# The second rule matches everything else and causes
# the value to be rejected.
rwm-rewriteContext searchEntryDN
rwm-rewriteRule &quot;.+,ou=People,dc=example,dc=com$&quot; &quot;$0&quot; &quot;:@&quot;
rwm-rewriteRule &quot;.*&quot; &quot;&quot; &quot;#&quot;</pre>
<h2>Mapping Examples</h2>
<p>The following directives map the object class `groupOfNames&#8217; to the object class `groupOfUniqueNames&#8217; and the attribute type `member&#8217; to the attribute type `uniqueMember&#8217;: </p>
<dl>
<dd>
<pre>map objectclass groupOfNames groupOfUniqueNames
map attribute uniqueMember member</pre>
</dl>
<p> This presents a limited attribute set from the foreign server: </p>
<dl>
<dd>
<pre>map attribute cn *
map attribute sn *
map attribute manager *
map attribute description *
map attribute *</pre>
</dl>
<p> These lines map cn, sn, manager, and description to themselves, and any other attribute gets &quot;removed&quot; from the object before it is sent to the client (or sent up to the LDAP server). This is obviously a simplistic example, but you get the point.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5), <code><a href="/docs/linux/man/5-slapd-relay/">slapd-relay</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7).</p>
<h2>Author</h2>
<p>Pierangelo Masarati; based on back-ldap rewrite/remap features by Howard Chu, Pierangelo Masarati.</p>
