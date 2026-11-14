---
title: "slapd-access(5)"
name: "slapd-access"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-access/"
description: "slapd.access – access configuration for slapd, the stand-alone LDAP daemon"
---

<p>slapd.access &#8211; access configuration for slapd, the stand-alone LDAP daemon</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file contains configuration information for the <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) daemon. This configuration file is also used by the SLAPD tools <code><a href="/docs/linux/man/8-slapacl/">slapacl</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapauth/">slapauth</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapdn/">slapdn</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), and <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8). </p>
<p> The <code>slapd.conf</code> file consists of a series of global configuration options that apply to <code>slapd</code> as a whole (including all backends), followed by zero or more database backend definitions that contain information specific to a backend instance. </p>
<p> The general format of <code>slapd.conf</code> is as follows: </p>
<pre> # comment - these options apply to every database
 &lt;global configuration options&gt;
 # first database definition &amp; configuration options
 database &lt;backend 1 type&gt;
 &lt;configuration options specific to backend 1&gt;
 # subsequent database definitions &amp; configuration options
 ...</pre>
<p>Both the global configuration and each backend-specific section can contain access information. Backend-specific access control directives are used for those entries that belong to the backend, according to their naming context. In case no access control directives are defined for a backend or those which are defined are not applicable, the directives from the global configuration section are then used. </p>
<p> If no access controls are present, the default policy allows anyone and everyone to read anything but restricts updates to rootdn. (e.g., &quot;access to * by * read&quot;). </p>
<p> When dealing with an access list, because the global access list is effectively appended to each per-database list, if the resulting list is non-empty then the access list will end with an implicit <code>access to * by * none</code> directive. If there are no access directives applicable to a backend, then a default read is used. </p>
<p> <code>Be warned: the rootdn can always read and write EVERYTHING!</code> </p>
<p> For entries not held in any backend (such as a root DSE), the global directives are used. </p>
<p> Arguments that should be replaced by actual text are shown in brackets &lt;&gt;.</p>
<h2>The Access Directive</h2>
<p>The structure of the access control directives is</p>
<dl>
<dt><code>access to &lt;what&gt; [ by &lt;who&gt; [ &lt;access&gt; ] [ &lt;control&gt; ] ]+</code></p>
<dd>Grant access (specified by <code>&lt;access&gt;</code>) to a set of entries and/or attributes (specified by <code>&lt;what&gt;</code>) by one or more requestors (specified by <code>&lt;who&gt;</code>). </p>
</dl>
<p> Lists of access directives are evaluated in the order they appear in <i>slapd.conf</i>. When a <code>&lt;what&gt;</code> clause matches the datum whose access is being evaluated, its <code>&lt;who&gt;</code> clause list is checked. When a <code>&lt;who&gt;</code> clause matches the accessor&#8217;s properties, its <code>&lt;access&gt;</code> and <code>&lt;control&gt;</code> clauses are evaluated. Access control checking stops at the first match of the <code>&lt;what&gt;</code> and <code>&lt;who&gt;</code> clause, unless otherwise dictated by the <code>&lt;control&gt;</code> clause. Each <code>&lt;who&gt;</code> clause list is implicitly terminated by a </p>
<pre> by * none stop</pre>
<p>clause that results in stopping the access control with no access privileges granted. Each <code>&lt;what&gt;</code> clause list is implicitly terminated by a </p>
<pre> access to *
 by * none</pre>
<p>clause that results in granting no access privileges to an otherwise unspecified datum.</p>
<h2>THE &lt;WHAT&gt; FIELD</h2>
<p>The field <code>&lt;what&gt;</code> specifies the entity the access control directive applies to. It can have the forms </p>
<pre> dn[.&lt;dnstyle&gt;]=&lt;dnpattern&gt;
 filter=&lt;ldapfilter&gt;
 attrs=&lt;attrlist&gt;[ val[/matchingRule][.&lt;attrstyle&gt;]=&lt;attrval&gt;]</pre>
<p>with </p>
<pre> &lt;dnstyle&gt;=&#123;&#123;exact|base(object)}|regex
 |one(level)|sub(tree)|children}
 &lt;attrlist&gt;={&lt;attr&gt;|[{!|@}]&lt;objectClass&gt;}[,&lt;attrlist&gt;]
 &lt;attrstyle&gt;=&#123;&#123;exact|base(object)}|regex
 |one(level)|sub(tree)|children}</pre>
<p>The statement <code>dn=&lt;dnpattern&gt;</code> selects the entries based on their naming context. The <code>&lt;dnpattern&gt;</code> is a string representation of the entry&#8217;s DN. The wildcard <code>*</code> stands for all the entries, and it is implied if no <code>dn</code> form is given. </p>
<p> The <code>&lt;dnstyle&gt; </code> is optional; however, it is recommended to specify it to avoid ambiguities. <code>Base </code> (synonym of <code>baseObject</code>), the default, or <code>exact </code> (an alias of <code>base</code>) indicates the entry whose DN is equal to the <code>&lt;dnpattern&gt;</code>; <code>one</code> (synonym of <code>onelevel</code>) indicates all the entries immediately below the <code>&lt;dnpattern&gt;</code>, <code>sub</code> (synonym of <code>subtree</code>) indicates all entries in the subtree at the <code>&lt;dnpattern&gt;</code>, <code>children</code> indicates all the entries below (subordinate to) the <code>&lt;dnpattern&gt;</code>. </p>
<p> If the <code>&lt;dnstyle&gt;</code> qualifier is <code>regex</code>, then <code>&lt;dnpattern&gt;</code> is a POSIX (&#8221;extended&#8221;) regular expression pattern, as detailed in <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7), matching a normalized string representation of the entry&#8217;s DN. The regex form of the pattern does not (yet) support UTF-8. </p>
<p> The statement <code>filter=&lt;ldapfilter&gt;</code> selects the entries based on a valid LDAP filter as described in RFC 4515. A filter of <code>(objectClass=*)</code> is implied if no <code>filter</code> form is given. </p>
<p> The statement <code>attrs=&lt;attrlist&gt;</code> selects the attributes the access control rule applies to. It is a comma-separated list of attribute types, plus the special names <code>entry</code>, indicating access to the entry itself, and <code>children</code>, indicating access to the entry&#8217;s children. ObjectClass names may also be specified in this list, which will affect all the attributes that are required and/or allowed by that objectClass. Actually, names in <code>&lt;attrlist&gt;</code> that are prefixed by <code>@</code> are directly treated as objectClass names. A name prefixed by <code>!</code> is also treated as an objectClass, but in this case the access rule affects the attributes that are not required nor allowed by that objectClass. If no <code>attrs</code> form is given, <code>attrs=@extensibleObject</code> is implied, i.e. all attributes are addressed. </p>
<p> Using the form <code>attrs=&lt;attr&gt; val[/matchingRule][.&lt;attrstyle&gt;]=&lt;attrval&gt;</code> specifies access to a particular value of a single attribute. In this case, only a single attribute type may be given. The <code>&lt;attrstyle&gt;</code> <code>exact</code> (the default) uses the attribute&#8217;s equality matching rule to compare the value, unless a different (and compatible) matching rule is specified. If the <code>&lt;attrstyle&gt;</code> is <code>regex</code>, the provided value is used as a POSIX (&#8221;extended&#8221;) regular expression pattern. If the attribute has DN syntax, the <code>&lt;attrstyle&gt;</code> can be any of <code>base</code>, <code>onelevel</code>, <code>subtree</code> or <code>children</code>, resulting in base, onelevel, subtree or children match, respectively. </p>
<p> The dn, filter, and attrs statements are additive; they can be used in sequence to select entities the access rule applies to based on naming context, value and attribute type simultaneously. Submatches resulting from <code>regex</code> matching can be dereferenced in the <code>&lt;who&gt;</code> field using the syntax <i>${v&lt;n&gt;}</i>, where <i>&lt;n&gt;</i> is the submatch number. The default syntax, <i>$&lt;n&gt;</i>, is actually an alias for <i>${d&lt;n&gt;}</i>, that corresponds to dereferencing submatches from the <code>dnpattern</code> portion of the <code>&lt;what&gt;</code> field.</p>
<h2>THE &lt;WHO&gt; FIELD</h2>
<p>The field <code>&lt;who&gt;</code> indicates whom the access rules apply to. Multiple <code>&lt;who&gt;</code> statements can appear in an access control statement, indicating the different access privileges to the same resource that apply to different accessee. It can have the forms </p>
<pre> *
 anonymous
 users
 self[.&lt;selfstyle&gt;]
 dn[.&lt;dnstyle&gt;[,&lt;modifier&gt;]]=&lt;DN&gt;
 dnattr=&lt;attrname&gt;
 realanonymous
 realusers
 realself[.&lt;selfstyle&gt;]
 realdn[.&lt;dnstyle&gt;[,&lt;modifier&gt;]]=&lt;DN&gt;
 realdnattr=&lt;attrname&gt;
 group[/&lt;objectclass&gt;[/&lt;attrname&gt;]]
 [.&lt;groupstyle&gt;]=&lt;group&gt;
 peername[.&lt;peernamestyle&gt;]=&lt;peername&gt;
 sockname[.&lt;style&gt;]=&lt;sockname&gt;
 domain[.&lt;domainstyle&gt;[,&lt;modifier&gt;]]=&lt;domain&gt;
 sockurl[.&lt;style&gt;]=&lt;sockurl&gt;
 set[.&lt;setstyle&gt;]=&lt;pattern&gt;
 ssf=&lt;n&gt;
 transport_ssf=&lt;n&gt;
 tls_ssf=&lt;n&gt;
 sasl_ssf=&lt;n&gt;
 dynacl/&lt;name&gt;[/&lt;options&gt;][.&lt;dynstyle&gt;][=&lt;pattern&gt;]</pre>
<p>with </p>
<pre> &lt;style&gt;={exact|regex|expand}
 &lt;selfstyle&gt;={level{&lt;n&gt;}}
 &lt;dnstyle&gt;=&#123;&#123;exact|base(object)}|regex
 |one(level)|sub(tree)|children|level{&lt;n&gt;}}
 &lt;groupstyle&gt;={exact|expand}
 &lt;peernamestyle&gt;={&lt;style&gt;|ip|ipv6|path}
 &lt;domainstyle&gt;={exact|regex|sub(tree)}
 &lt;setstyle&gt;={exact|expand}
 &lt;modifier&gt;={expand}
 &lt;name&gt;=aci &lt;pattern&gt;=&lt;attrname&gt;]</pre>
<p>They may be specified in combination. </p>
<p> The wildcard <code>*</code> refers to everybody. </p>
<p> The keywords prefixed by <code>real</code> act as their counterparts without prefix; the checking respectively occurs with the <i>authentication</i> DN and the <i>authorization</i> DN. </p>
<p> The keyword <code>anonymous</code> means access is granted to unauthenticated clients; it is mostly used to limit access to authentication resources (e.g. the <code>userPassword</code> attribute) to unauthenticated clients for authentication purposes. </p>
<p> The keyword <code>users</code> means access is granted to authenticated clients. </p>
<p> The keyword <code>self</code> means access to an entry is allowed to the entry itself (e.g. the entry being accessed and the requesting entry must be the same). It allows the <code>level{&lt;n&gt;}</code> style, where <i>&lt;n&gt;</i> indicates what ancestor of the DN is to be used in matches. A positive value indicates that the &lt;n&gt;-th ancestor of the user&#8217;s DN is to be considered; a negative value indicates that the &lt;n&gt;-th ancestor of the target is to be considered. For example, a &quot;<i>by self.level{1} &#8230;</i>&quot; clause would match when the object &quot;<i>dc=example,dc=com</i>&quot; is accessed by &quot;<i>cn=User,dc=example,dc=com</i>&quot;. A &quot;<i>by self.level{-1} &#8230;</i>&quot; clause would match when the same user accesses the object &quot;<i>ou=Address Book,cn=User,dc=example,dc=com</i>&quot;. </p>
<p> The statement <code>dn=&lt;DN&gt;</code> means that access is granted to the matching DN. The optional style qualifier <code>dnstyle</code> allows the same choices of the dn form of the <code>&lt;what&gt;</code> field. In addition, the <code>regex</code> style can exploit substring substitution of submatches in the <code>&lt;what&gt;</code> dn.regex clause by using the form <code>$&lt;digit&gt;</code>, with <code>digit</code> ranging from 0 to 9 (where 0 matches the entire string), or the form <code>${&lt;digit&gt;+}</code>, for submatches higher than 9. Substring substitution from attribute value can be done in using the form <code>${v&lt;digit&gt;+}</code>. Since the dollar character is used to indicate a substring replacement, the dollar character that is used to indicate match up to the end of the string must be escaped by a second dollar character, e.g. </p>
<pre> access to dn.regex=&quot;^(.+,)?uid=([^,]+),dc=[^,]+,dc=com$&quot;
 by dn.regex=&quot;^uid=$2,dc=[^,]+,dc=com$$&quot; write</pre>
<p>The style qualifier allows an optional <code>modifier</code>. At present, the only type allowed is <code>expand</code>, which causes substring substitution of submatches to take place even if <code>dnstyle</code> is not <code>regex</code>. Note that the <code>regex </code> dnstyle in the above example may be of use only if the <code>&lt;by&gt;</code> clause needs to be a regex; otherwise, if the value of the second (from the right) <code>dc=</code> portion of the DN in the above example were fixed, the form </p>
<pre> access to dn.regex=&quot;^(.+,)?uid=([^,]+),dc=example,dc=com$&quot;
 by dn.exact,expand=&quot;uid=$2,dc=example,dc=com&quot; write</pre>
<p>could be used; if it had to match the value in the <code>&lt;what&gt;</code> clause, the form </p>
<pre> access to dn.regex=&quot;^(.+,)?uid=([^,]+),dc=([^,]+),dc=com$&quot;
 by dn.exact,expand=&quot;uid=$2,dc=$3,dc=com&quot; write</pre>
<p>could be used. </p>
<p> Forms of the <code>&lt;what&gt;</code> clause other than regex may provide submatches as well. The <code>base(object)</code>, the <code>sub(tree)</code>, the <code>one(level)</code>, and the <code>children</code> forms provide <code>$0</code> as the match of the entire string. The <code>sub(tree)</code>, the <code>one(level)</code>, and the <code>children</code> forms also provide <code>$1</code> as the match of the rightmost part of the DN as defined in the <code>&lt;what&gt;</code> clause. This may be useful, for instance, to provide access to all the ancestors of a user by defining </p>
<pre> access to dn.subtree=&quot;dc=com&quot;
 by dn.subtree,expand=&quot;$1&quot; read</pre>
<p>which means that only access to entries that appear in the DN of the <code>&lt;by&gt;</code> clause is allowed. </p>
<p> The <code>level{&lt;n&gt;}</code> form is an extension and a generalization of the <code>onelevel</code> form, which matches all DNs whose &lt;n&gt;-th ancestor is the pattern. So, <i>level{1}</i> is equivalent to <i>onelevel</i>, and <i>level{0}</i> is equivalent to <i>base</i>. </p>
<p> It is perfectly useless to give any access privileges to a DN that exactly matches the <code>rootdn</code> of the database the ACLs apply to, because it implicitly possesses write privileges for the entire tree of that database. Actually, access control is bypassed for the <code>rootdn</code>, to solve the intrinsic chicken-and-egg problem. </p>
<p> The statement <code>dnattr=&lt;attrname&gt;</code> means that access is granted to requests whose DN is listed in the entry being accessed under the <code>&lt;attrname&gt;</code> attribute. </p>
<p> The statement <code>group=&lt;group&gt;</code> means that access is granted to requests whose DN is listed in the group entry whose DN is given by <code>&lt;group&gt;</code>. The optional parameters <code>&lt;objectclass&gt;</code> and <code>&lt;attrname&gt;</code> define the objectClass and the member attributeType of the group entry. The defaults are <code>groupOfNames</code> and <code>member</code>, respectively. The optional style qualifier <code>&lt;style&gt;</code> can be <code>expand</code>, which means that <code>&lt;group&gt;</code> will be expanded as a replacement string (but not as a regular expression) according to <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7), and <code>exact</code>, which means that exact match will be used. If the style of the DN portion of the <code>&lt;what&gt;</code> clause is regex, the submatches are made available according to <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) and/or <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7); other styles provide limited submatches as discussed above about the DN form of the <code>&lt;by&gt;</code> clause. </p>
<p> For static groups, the specified attributeType must have <code>DistinguishedName</code> or <code>NameAndOptionalUID</code> syntax. For dynamic groups the attributeType must be a subtype of the <code>labeledURI</code> attributeType. Only LDAP URIs of the form <code><a href="ldap:///">ldap:///</a>&lt;base&gt;??&lt;scope&gt;?&lt;filter&gt;</code> will be evaluated in a dynamic group, by searching the local server only. </p>
<p> The statements <code>peername=&lt;peername&gt;</code>, <code>sockname=&lt;sockname&gt;</code>, <code>domain=&lt;domain&gt;</code>, and <code>sockurl=&lt;sockurl&gt;</code> mean that the contacting host IP (in the form <code>IP=&lt;ip&gt;:&lt;port&gt;</code> for IPv4, or <code>IP=[&lt;ipv6&gt;]:&lt;port&gt;</code> for IPv6) or the contacting host named pipe file name (in the form <code>PATH=&lt;path&gt;</code> if connecting through a named pipe) for <code>peername</code>, the named pipe file name for <code>sockname</code>, the contacting host name for <code>domain</code>, and the contacting URL for <code>sockurl</code> are compared against <code>pattern</code> to determine access. The same <code>style</code> rules for pattern match described for the <code>group</code> case apply, plus the <code>regex</code> style, which implies submatch <code>expand</code> and regex match of the corresponding connection parameters. The <code>exact</code> style of the <code>&lt;peername&gt;</code> clause (the default) implies a case-exact match on the client&#8217;s <code>IP</code>, including the <code>IP=</code> prefix and the trailing <code>:&lt;port&gt;</code>, or the client&#8217;s <code>path</code>, including the <code>PATH=</code> prefix if connecting through a named pipe. The special <code>ip</code> style interprets the pattern as <code>&lt;peername&gt;=&lt;ip&gt;[%&lt;mask&gt;][{&lt;n&gt;}]</code>, where <code>&lt;ip&gt;</code> and <code>&lt;mask&gt;</code> are dotted digit representations of the IP and the mask, while <code>&lt;n&gt;</code>, delimited by curly brackets, is an optional port. The same applies to IPv6 addresses when the special <code>ipv6</code> style is used. When checking access privileges, the IP portion of the <code>peername</code> is extracted, eliminating the <code>IP=</code> prefix and the <code>:&lt;port&gt;</code> part, and it is compared against the <code>&lt;ip&gt;</code> portion of the pattern after masking with <code>&lt;mask&gt;</code>: <i>((peername &amp; &lt;mask&gt;) == &lt;ip&gt;)</i>. As an example, <code>peername.ip=127.0.0.1</code> and <code>peername.ipv6=::1</code> allow connections only from localhost, <code>peername.ip=192.168.1.0%255.255.255.0 </code> allows connections from any IP in the 192.168.1 class C domain, and <code>peername.ip=192.168.1.16%255.255.255.240{9009}</code> allows connections from any IP in the 192.168.1.[16-31] range of the same domain, only if port 9009 is used. The special <code>path</code> style eliminates the <code>PATH=</code> prefix from the <code>peername</code> when connecting through a named pipe, and performs an exact match on the given pattern. The <code>&lt;domain&gt;</code> clause also allows the <code>subtree</code> style, which succeeds when a fully qualified name exactly matches the <code>domain</code> pattern, or its trailing part, after a <code>dot</code>, exactly matches the <code>domain</code> pattern. The <code>expand</code> style is allowed, implying an <code>exact </code> match with submatch expansion; the use of <code>expand </code> as a style modifier is considered more appropriate. As an example, <code>domain.subtree=example.com</code> will match <a rel="nofollow" href="http://www.example.com">www.example.com</a>, but will not match <a href="http://www.anotherexample.com">www.anotherexample.com</a>. The <code>domain</code> of the contacting host is determined by performing a DNS reverse lookup. As this lookup can easily be spoofed, use of the <code>domain</code> statement is strongly discouraged. By default, reverse lookups are disabled. The optional <code>domainstyle</code> qualifier of the <code>&lt;domain&gt;</code> clause allows a <code>modifier</code> option; the only value currently supported is <code>expand</code>, which causes substring substitution of submatches to take place even if the <code>domainstyle</code> is not <code>regex</code>, much like the analogous usage in <code>&lt;dn&gt;</code> clause. </p>
<p> The statement <code>set=&lt;pattern&gt;</code> is undocumented yet. </p>
<p> The statement <code>dynacl/&lt;name&gt;[/&lt;options&gt;][.&lt;dynstyle&gt;][=&lt;pattern&gt;]</code> means that access checking is delegated to the admin-defined method indicated by <code>&lt;name&gt;</code>, which can be registered at run-time by means of the <code>moduleload</code> statement. The fields <code>&lt;options&gt;</code>, <code>&lt;dynstyle&gt;</code> and <code>&lt;pattern&gt;</code> are optional, and are directly passed to the registered parsing routine. Dynacl is experimental; it must be enabled at compile time. </p>
<p> The statement <code>dynacl/aci[=&lt;attrname&gt;]</code> means that the access control is determined by the values in the <code>attrname</code> of the entry itself. The optional <code>&lt;attrname&gt;</code> indicates what attributeType holds the ACI information in the entry. By default, the <code>OpenLDAPaci</code> operational attribute is used. ACIs are experimental; they must be enabled at compile time. </p>
<p> The statements <code>ssf=&lt;n&gt;</code>, <code>transport_ssf=&lt;n&gt;</code>, <code>tls_ssf=&lt;n&gt;</code>, and <code>sasl_ssf=&lt;n&gt;</code> set the minimum required Security Strength Factor (ssf) needed to grant access. The value should be positive integer.</p>
<h2>THE &lt;ACCESS&gt; FIELD</h2>
<p>The optional field <code>&lt;access&gt; ::= [[real]self]{&lt;level&gt;|&lt;priv&gt;}</code> determines the access level or the specific access privileges the <code>who </code> field will have. Its component are defined as </p>
<pre> &lt;level&gt; ::= none|disclose|auth|compare|search|read|{write|add|delete}|manage
 &lt;priv&gt; ::= {=|+|-}{0|d|x|c|s|r|{w|a|z}|m}+</pre>
<p>The modifier <code>self</code> allows special operations like having a certain access level or privilege only in case the operation involves the name of the user that&#8217;s requesting the access. It implies the user that requests access is authorized. The modifier <code>realself</code> refers to the authenticated DN as opposed to the authorized DN of the <code>self</code> modifier. An example is the <code>selfwrite</code> access to the member attribute of a group, which allows one to add/delete its own DN from the member list of a group, while being not allowed to affect other members. </p>
<p> The <code>level </code> access model relies on an incremental interpretation of the access privileges. The possible levels are <code>none</code>, <code>disclose</code>, <code>auth</code>, <code>compare</code>, <code>search</code>, <code>read</code>, <code>write</code>, and <code>manage</code>. Each access level implies all the preceding ones, thus <code>manage</code> grants all access including administrative access. The <code>write</code> access is actually the combination of <code>add</code> and <code>delete</code>, which respectively restrict the write privilege to add or delete the specified <code>&lt;what&gt;</code>. </p>
<p> The <code>none </code> access level disallows all access including disclosure on error. </p>
<p> The <code>disclose</code> access level allows disclosure of information on error. </p>
<p> The <code>auth</code> access level means that one is allowed access to an attribute to perform authentication/authorization operations (e.g. <code>bind</code>) with no other access. This is useful to grant unauthenticated clients the least possible access level to critical resources, like passwords. </p>
<p> The <code>priv</code> access model relies on the explicit setting of access privileges for each clause. The <code>=</code> sign resets previously defined accesses; as a consequence, the final access privileges will be only those defined by the clause. The <code>+</code> and <code>&#8211;</code> signs add/remove access privileges to the existing ones. The privileges are <code>m</code> for manage, <code>w</code> for write, <code>a</code> for add, <code>z</code> for delete, <code>r</code> for read, <code>s </code> for search, <code>c </code> for compare, <code>x</code> for authentication, and <code>d</code> for disclose. More than one of the above privileges can be added in one statement. <code>0</code> indicates no privileges and is used only by itself (e.g., +0). Note that <code>+az</code> is equivalent to <code>+w</code>. </p>
<p> If no access is given, it defaults to <code>+0</code>.</p>
<h2>THE &lt;CONTROL&gt; FIELD</h2>
<p>The optional field <code>&lt;control&gt;</code> controls the flow of access rule application. It can have the forms </p>
<pre> stop
 continue
 break</pre>
<p>where <code>stop</code>, the default, means access checking stops in case of match. The other two forms are used to keep on processing access clauses. In detail, the <code>continue</code> form allows for other <code>&lt;who&gt;</code> clauses in the same <code>&lt;access&gt;</code> clause to be considered, so that they may result in incrementally altering the privileges, while the <code>break</code> form allows for other <code>&lt;access&gt;</code> clauses that match the same target to be processed. Consider the (silly) example </p>
<pre> access to dn.subtree=&quot;dc=example,dc=com&quot; attrs=cn
 by * =cs break
 access to dn.subtree=&quot;ou=People,dc=example,dc=com&quot;
 by * +r</pre>
<p>which allows search and compare privileges to everybody under the &quot;dc=example,dc=com&quot; tree, with the second rule allowing also read in the &quot;ou=People&quot; subtree, or the (even more silly) example </p>
<pre> access to dn.subtree=&quot;dc=example,dc=com&quot; attrs=cn
 by * =cs continue
 by users +r</pre>
<p>which grants everybody search and compare privileges, and adds read privileges to authenticated clients. </p>
<p> One useful application is to easily grant write privileges to an <code>updatedn</code> that is different from the <code>rootdn</code>. In this case, since the <code>updatedn</code> needs write access to (almost) all data, one can use </p>
<pre> access to *
 by dn.exact=&quot;cn=The Update DN,dc=example,dc=com&quot; write
 by * break</pre>
<p>as the first access rule. As a consequence, unless the operation is performed with the <code>updatedn</code> identity, control is passed straight to the subsequent rules.</p>
<h2>Operation Requirements</h2>
<p>Operations require different privileges on different portions of entries. The following summary applies to primary database backends such as the BDB and HDB backends. Requirements for other backends may (and often do) differ. </p>
<p> The <code>add</code> operation requires <code>add (=a)</code> privileges on the pseudo-attribute <code>entry</code> of the entry being added, and <code>add (=a)</code> privileges on the pseudo-attribute <code>children</code> of the entry&#8217;s parent. When adding the suffix entry of a database, <code>add</code> access to <code>children</code> of the empty DN (&quot;&quot;) is required. Also if Add content ACL checking has been configured on the database (see the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) or <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5) manual page), <code>add (=a)</code> will be required on all of the attributes being added. </p>
<p> The <code>bind</code> operation, when credentials are stored in the directory, requires <code>auth (=x)</code> privileges on the attribute the credentials are stored in (usually <code>userPassword</code>). </p>
<p> The <code>compare</code> operation requires <code>compare (=c)</code> privileges on the attribute that is being compared. </p>
<p> The <code>delete</code> operation requires <code>delete (=z)</code> privileges on the pseudo-attribute <code>entry </code> of the entry being deleted, and <code>delete (=d)</code> privileges on the <code>children</code> pseudo-attribute of the entry&#8217;s parent. </p>
<p> The <code>modify</code> operation requires <code>write (=w)</code> privileges on the attributes being modified. In detail, <code>add (=a)</code> is required to add new values, <code>delete (=z)</code> is required to delete existing values, and both <code>delete</code> and <code>add (=az)</code>, or <code>write (=w)</code>, are required to replace existing values. </p>
<p> The <code>modrdn</code> operation requires <code>write (=w)</code> privileges on the pseudo-attribute <code>entry</code> of the entry whose relative DN is being modified, <code>delete (=z)</code> privileges on the pseudo-attribute <code>children</code> of the old entry&#8217;s parents, <code>add (=a)</code> privileges on the pseudo-attribute <code>children</code> of the new entry&#8217;s parents, and <code>add (=a)</code> privileges on the attributes that are present in the new relative DN. <code>Delete (=z)</code> privileges are also required on the attributes that are present in the old relative DN if <code>deleteoldrdn</code> is set to 1. </p>
<p> The <code>search</code> operation, requires <code>search (=s)</code> privileges on the <code>entry</code> pseudo-attribute of the searchBase (NOTE: this was introduced with OpenLDAP 2.4). Then, for each entry, it requires <code>search (=s)</code> privileges on the attributes that are defined in the filter. The resulting entries are finally tested for <code>read (=r)</code> privileges on the pseudo-attribute <code>entry</code> (for read access to the entry itself) and for <code>read (=r)</code> access on each value of each attribute that is requested. Also, for each <code>referral</code> object used in generating continuation references, the operation requires <code>read (=r)</code> access on the pseudo-attribute <code>entry</code> (for read access to the referral object itself), as well as <code>read (=r)</code> access to the attribute holding the referral information (generally the <code>ref</code> attribute). </p>
<p> Some internal operations and some <code>controls</code> require specific access privileges. The <code>authzID</code> mapping and the <code>proxyAuthz</code> control require <code>auth (=x)</code> privileges on all the attributes that are present in the search filter of the URI regexp maps (the right-hand side of the <code>authz-regexp</code> directives). <code>Auth (=x)</code> privileges are also required on the <code>authzTo</code> attribute of the authorizing identity and/or on the <code>authzFrom</code> attribute of the authorized identity. In general, when an internal lookup is performed for authentication or authorization purposes, search-specific privileges (see the access requirements for the search operation illustrated above) are relaxed to <code>auth</code>. </p>
<p> Access control to search entries is checked by the frontend, so it is fully honored by all backends; for all other operations and for the discovery phase of the search operation, full ACL semantics is only supported by the primary backends, i.e. <code><a href="/docs/linux/man/5-back-bdb/">back-bdb</a></code>(5), and <code><a href="/docs/linux/man/5-back-hdb/">back-hdb</a></code>(5). </p>
<p> Some other backend, like <code><a href="/docs/linux/man/5-back-sql/">back-sql</a></code>(5), may fully support them; others may only support a portion of the described semantics, or even differ in some aspects. The relevant details are described in the backend-specific man pages.</p>
<h2>Caveats</h2>
<p>It is strongly recommended to explicitly use the most appropriate <code>&lt;dnstyle&gt;</code> in <code>&lt;what&gt;</code> and <code>&lt;who&gt;</code> clauses, to avoid possible incorrect specifications of the access rules as well as for performance (avoid unnecessary regex matching when an exact match suffices) reasons. </p>
<p> An administrator might create a rule of the form: </p>
<pre> access to dn.regex=&quot;dc=example,dc=com&quot;
 by ...</pre>
<p>expecting it to match all entries in the subtree &quot;dc=example,dc=com&quot;. However, this rule actually matches any DN which contains anywhere the substring &quot;dc=example,dc=com&quot;. That is, the rule matches both &quot;uid=joe,dc=example,dc=com&quot; and &quot;dc=example,dc=com,uid=joe&quot;. </p>
<p> To match the desired subtree, the rule would be more precisely written: </p>
<pre> access to dn.regex=&quot;^(.+,)?dc=example,dc=com$&quot;
 by ...</pre>
<p>For performance reasons, it would be better to use the subtree style. </p>
<pre> access to dn.subtree=&quot;dc=example,dc=com&quot;
 by ...</pre>
<p>When writing submatch rules, it may be convenient to avoid unnecessary <code>regex</code> <code>&lt;dnstyle&gt;</code> use; for instance, to allow access to the subtree of the user that matches the <code>&lt;what&gt;</code> clause, one could use </p>
<pre> access to dn.regex=&quot;^(.+,)?uid=([^,]+),dc=example,dc=com$&quot;
 by dn.regex=&quot;^uid=$2,dc=example,dc=com$$&quot; write
 by ...</pre>
<p>However, since all that is required in the <code>&lt;by&gt;</code> clause is substring expansion, a more efficient solution is </p>
<pre> access to dn.regex=&quot;^(.+,)?uid=([^,]+),dc=example,dc=com$&quot;
 by dn.exact,expand=&quot;uid=$2,dc=example,dc=com&quot; write
 by ...</pre>
<p>In fact, while a <code>&lt;dnstyle&gt;</code> of <code>regex</code> implies substring expansion, <code>exact</code>, as well as all the other DN specific <code>&lt;dnstyle&gt;</code> values, does not, so it must be explicitly requested.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code>slapd-*</code>(5), <code><a href="/docs/linux/man/8-slapacl/">slapacl</a></code>(8), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
