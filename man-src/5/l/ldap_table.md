---
title: "ldap_table(5)"
name: "ldap_table"
section: "5"
letter: "l"
url: "/docs/linux/man/5-ldap_table/"
description: "ldap_table – Postfix LDAP client configuration"
---

<p>ldap_table &#8211; Postfix LDAP client configuration</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; ldap:/etc/postfix/filename</code>
<code>postmap -q - ldap:/etc/postfix/</code><i>filename</i> &lt;<i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting or mail routing. These tables are usually in <code>dbm</code> or <code>db</code> format. </p>
<p> Alternatively, lookup tables can be specified as LDAP databases. </p>
<p> In order to use LDAP lookups, define an LDAP source as a lookup table in main.cf, for example: </p>
<pre> alias_maps = ldap:/etc/postfix/ldap-aliases.cf</pre>
<p>The file /etc/postfix/ldap-aliases.cf has the same format as the Postfix main.cf file, and can specify the parameters described below. An example is given at the end of this manual. </p>
<p> This configuration method is available with Postfix version 2.1 and later. See the section &quot;BACKWARDS COMPATIBILITY&quot; below for older Postfix versions. </p>
<p> For details about LDAP SSL and STARTTLS, see the section on SSL and STARTTLS below.</p>
<h2>Backwards Compatibility</h2>
<p>For backwards compatibility with Postfix version 2.0 and earlier, LDAP parameters can also be defined in main.cf. Specify as LDAP source a name that doesn&#8217;t begin with a slash or a dot. The LDAP parameters will then be accessible as the name you&#8217;ve given the source in its definition, an underscore, and the name of the parameter. For example, if the map is specified as &quot;ldap:<i>ldapsource</i>&quot;, the &quot;server_host&quot; parameter below would be defined in main.cf as &quot;<i>ldapsource</i>_server_host&quot;. </p>
<p> Note: with this form, the passwords for the LDAP sources are written in main.cf, which is normally world-readable. Support for this form will be removed in a future Postfix version. </p>
<p> For backwards compatibility with the pre 2.2 LDAP clients, <code>result_filter</code> can for now be used instead of <code>result_format</code>, when the latter parameter is not also set. The new name better reflects the function of the parameter. This compatibility interface may be removed in a future release.</p>
<h2>List Membership</h2>
<p>When using LDAP to store lists such as $mynetworks, $mydestination, $relay_domains, $local_recipient_maps, etc., it is important to understand that the table must store each list member as a separate key. The table lookup verifies the *existence* of the key. See &quot;Postfix lists versus tables&quot; in the DATABASE_README document for a discussion. </p>
<p> Do NOT create tables that return the full list of domains in $mydestination or $relay_domains etc., or IP addresses in $mynetworks. </p>
<p> DO create tables with each matching item as a key and with an arbitrary value. With LDAP databases it is not uncommon to return the key itself. </p>
<p> For example, NEVER do this in a map defining $mydestination: </p>
<pre> query_filter = domain=*
 result_attribute = domain</pre>
<p>Do this instead: </p>
<pre> query_filter = domain=%s
 result_attribute = domain</pre>
<h2>General Ldap Parameters</h2>
<p>In the text below, default values are given in parentheses. Note: don&#8217;t use quotes in these variables; at least, not until the Postfix configuration routines understand how to deal with quoted strings.</p>
<dl>
<dt><code>server_host (default: localhost)</code></p>
<dd>The name of the host running the LDAP server, e.g. </p>
<pre> server_host = ldap.example.com</pre>
<p>Depending on the LDAP client library you&#8217;re using, it should be possible to specify multiple servers here, with the library trying them in order should the first one fail. It should also be possible to give each server in the list a different port (overriding <code>server_port</code> below), by naming them like </p>
<pre> server_host = ldap.example.com:1444</pre>
<p>With OpenLDAP, a (list of) LDAP URLs can be used to specify both the hostname(s) and the port(s): </p>
<pre> server_host = <a href="ldap://ldap.example.com:1444">ldap://ldap.example.com:1444</a>
 <a href="ldap://ldap2.example.com:1444">ldap://ldap2.example.com:1444</a></pre>
<p>All LDAP URLs accepted by the OpenLDAP library are supported, including connections over UNIX domain sockets, and LDAP SSL (the last one provided that OpenLDAP was compiled with support for SSL): </p>
<pre> server_host = <a href="ldapi://%2Fsome%2Fpath">ldapi://%2Fsome%2Fpath</a>
 <a href="ldaps://ldap.example.com:636">ldaps://ldap.example.com:636</a></pre>
<dt><code>server_port (default: 389)</code></p>
<dd>The port the LDAP server listens on, e.g. </p>
<pre> server_port = 778</pre>
<dt><code>timeout (default: 10 seconds)</code></p>
<dd>The number of seconds a search can take before timing out, e.g. </p>
<p>&nbsp;<wbr>timeout&nbsp;<wbr>=&nbsp;<wbr>5</p>
<dt><code>search_base (No default; you must configure this)</code></p>
<dd>The RFC2253 base DN at which to conduct the search, e.g. </p>
<pre> search_base = dc=your, dc=com</pre>
<dd>With Postfix 2.2 and later this parameter supports the following &#8216;%&#8217; expansions:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>This is replaced by a literal &#8216;%&#8217; character.</p>
<dt><code>%s</code></p>
<dd>This is replaced by the input key. RFC 2253 quoting is used to make sure that the input key does not add unexpected metacharacters.</p>
<dt><code>%u</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%u</code> is replaced by the (RFC 2253) quoted local part of the address. Otherwise, <code>%u</code> is replaced by the entire search string. If the localpart is empty, the search is suppressed and returns no results.</p>
<dt><code>%d</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%d</code> is replaced by the (RFC 2253) quoted domain part of the address. Otherwise, the search is suppressed and returns no results.</p>
<dt><code>%[SUD]</code></p>
<dd>For the <code>search_base</code> parameter, the upper-case equivalents of the above expansions behave identically to their lower-case counter-parts. With the <code>result_format</code> parameter (previously called <code>result_filter</code> see the COMPATIBILITY section and below), they expand to the corresponding components of input key rather than the result value.</p>
<dt><code>%[1-9]</code></p>
<dd>The patterns %1, %2, &#8230; %9 are replaced by the corresponding most significant component of the input key&#8217;s domain. If the input key is <i>user [at] mail.example.com</i>, then %1 is <code>com</code>, %2 is <code>example</code> and %3 is <code>mail</code>. If the input key is unqualified or does not have enough domain components to satisfy all the specified patterns, the search is suppressed and returns no results.</dl>
</dl>
<dt><code>query_filter (default: mailacceptinggeneralid=%s)</code></p>
<dd>The RFC2254 filter used to search the directory, where <code>%s</code> is a substitute for the address Postfix is trying to resolve, e.g. </p>
<pre> query_filter = (&amp;(mail=%s)(paid_up=true))</pre>
<p>This parameter supports the following &#8216;%&#8217; expansions:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>This is replaced by a literal &#8216;%&#8217; character. (Postfix 2.2 and later).</p>
<dt><code>%s</code></p>
<dd>This is replaced by the input key. RFC 2254 quoting is used to make sure that the input key does not add unexpected metacharacters.</p>
<dt><code>%u</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%u</code> is replaced by the (RFC 2254) quoted local part of the address. Otherwise, <code>%u</code> is replaced by the entire search string. If the localpart is empty, the search is suppressed and returns no results.</p>
<dt><code>%d</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%d</code> is replaced by the (RFC 2254) quoted domain part of the address. Otherwise, the search is suppressed and returns no results.</p>
<dt><code>%[SUD]</code></p>
<dd>The upper-case equivalents of the above expansions behave in the <code>query_filter</code> parameter identically to their lower-case counter-parts. With the <code>result_format</code> parameter (previously called <code>result_filter</code> see the COMPATIBILITY section and below), they expand to the corresponding components of input key rather than the result value.</p>
<dd>The above %S, %U and %D expansions are available with Postfix 2.2 and later.</p>
<dt><code>%[1-9]</code></p>
<dd>The patterns %1, %2, &#8230; %9 are replaced by the corresponding most significant component of the input key&#8217;s domain. If the input key is <i>user [at] mail.example.com</i>, then %1 is <code>com</code>, %2 is <code>example</code> and %3 is <code>mail</code>. If the input key is unqualified or does not have enough domain components to satisfy all the specified patterns, the search is suppressed and returns no results.</p>
<dd>The above %1, &#8230;, %9 expansions are available with Postfix 2.2 and later.</dl>
</dl>
<dd>The &quot;domain&quot; parameter described below limits the input keys to addresses in matching domains. When the &quot;domain&quot; parameter is non-empty, LDAP queries for unqualified addresses or addresses in non-matching domains are suppressed and return no results. </p>
<p> NOTE: DO NOT put quotes around the <code>query_filter</code> parameter.</p>
<dt><code>result_format (default: %s</code>)</p>
<dd>Called <code>result_filter</code> in Postfix releases prior to 2.2. Format template applied to result attributes. Most commonly used to append (or prepend) text to the result. This parameter supports the following &#8216;%&#8217; expansions:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>This is replaced by a literal &#8216;%&#8217; character. (Postfix 2.2 and later).</p>
<dt><code>%s</code></p>
<dd>This is replaced by the value of the result attribute. When result is empty it is skipped.</p>
<dt><code>%u</code></p>
<dd>When the result attribute value is an address of the form user [at] domain, <code>%u</code> is replaced by the local part of the address. When the result has an empty localpart it is skipped.</p>
<dt><code>%d</code></p>
<dd>When a result attribute value is an address of the form user [at] domain, <code>%d</code> is replaced by the domain part of the attribute value. When the result is unqualified it is skipped.</p>
<dt><code>%[SUD1-9]</code><code></p>
<dd>The upper-case and decimal digit expansions interpolate the parts of the input key rather than the result. Their behavior is identical to that described with query_filter</code>, and in fact because the input key is known in advance, lookups whose key does not contain all the information specified in the result template are suppressed and return no results.</p>
<dd>The above %S, %U, %D and %1, &#8230;, %9 expansions are available with Postfix 2.2 and later.</dl>
</dl>
<dd>For example, using &quot;result_format = smtp:[%s]&quot; allows one to use a mailHost attribute as the basis of a <a href="/docs/linux/man/5-transport/">transport</a>(5) table. After applying the result format, multiple values are concatenated as comma separated strings. The expansion_limit and size_limit parameters explained below allow one to restrict the number of values in the result, which is especially useful for maps that should return a single value. </p>
<p> The default value <code>%s</code> specifies that each attribute value should be used as is. </p>
<p> This parameter was called <code>result_filter</code> in Postfix releases prior to 2.2. If no &quot;result_format&quot; is specified, the value of &quot;result_filter&quot; will be used instead before resorting to the default value. This provides compatibility with old configuration files. </p>
<p> NOTE: DO NOT put quotes around the result format!</p>
<dt><code>domain (default: no domain list)</code></p>
<dd>This is a list of domain names, paths to files, or dictionaries. When specified, only fully qualified search keys with a *non-empty* localpart and a matching domain are eligible for lookup: &#8216;user&#8217; lookups, bare domain lookups and &quot;@domain&quot; lookups are not performed. This can significantly reduce the query load on the LDAP server. </p>
<pre> domain = postfix.org, hash:/etc/postfix/searchdomains</pre>
<p>It is best not to use LDAP to store the domains eligible for LDAP lookups. </p>
<p> NOTE: DO NOT define this parameter for <a href="/docs/linux/man/8-local/">local</a>(8) aliases. </p>
<p> This feature is available in Postfix 1.0 and later.</p>
<dt><code>result_attribute (default: maildrop)</code></p>
<dd>The attribute(s) Postfix will read from any directory entries returned by the lookup, to be resolved to an email address. </p>
<pre> result_attribute = mailbox, maildrop</pre>
<p>Don&#8217;t rely on the default value (&quot;maildrop&quot;). Set the result_attribute explicitly in all ldap table configuration files. This is particularly relevant when no result_attribute is applicable, e.g. cases in which leaf_result_attribute and/or terminal_result_attribute are used instead. The default value is harmless if &quot;maildrop&quot; is also listed as a leaf or terminal result attribute, but it is best to not leave this to chance.</p>
<dt><code>special_result_attribute (default: empty)</code></p>
<dd>The attribute(s) of directory entries that can contain DNs or RFC 2255 LDAP URLs. If found, a recursive search is performed to retrieve the entry referenced by the DN, or the entries matched by the URL query. </p>
<pre> special_result_attribute = memberdn</pre>
<p>DN recursion retrieves the same result_attributes as the main query, including the special attributes for further recursion. </p>
<p> URL processing retrieves only those attributes that are included in both the URL definition and as result attributes (ordinary, special, leaf or terminal) in the Postfix table definition. If the URL lists any of the table&#8217;s special result attributes, these are retrieved and used recursively. A URL that does not specify any attribute selection, is equivalent (RFC 2255) to a URL that selects all attributes, in which case the selected attributes will be the full set of result attributes in the Postfix table. </p>
<p> If an LDAP URL attribute-descriptor or the corresponding Postfix LDAP table result attribute (but not both) uses RFC 2255 sub-type options (&quot;attr;option&quot;), the attribute requested from the LDAP server will include the sub-type option. In all other cases, the URL attribute and the table attribute must match exactly. Attributes with options in both the URL and the Postfix table are requested only when the options are identical. LDAP attribute-descriptor options are very rarely used, most LDAP users will not need to concern themselves with this level of nuanced detail.</p>
<dt><code>terminal_result_attribute (default: empty)</code></p>
<dd>When one or more terminal result attributes are found in an LDAP entry, all other result attributes are ignored and only the terminal result attributes are returned. This is useful for delegating expansion of group members to a particular host, by using an optional &quot;maildrop&quot; attribute on selected groups to route the group to a specific host, where the group is expanded, possibly via mailing-list manager or other special processing. </p>
<pre> result_attribute =
 terminal_result_attribute = maildrop</pre>
<p>When using terminal and/or leaf result attributes, the result_attribute is best set to an empty value when it is not used, or else explicitly set to the desired value, even if it is the default value &quot;maildrop&quot;. </p>
<p> This feature is available with Postfix 2.4 or later.</p>
<dt><code>leaf_result_attribute (default: empty)</code></p>
<dd>When one or more special result attributes are found in a non-terminal (see above) LDAP entry, leaf result attributes are excluded from the expansion of that entry. This is useful when expanding groups and the desired mail address attribute(s) of the member objects obtained via DN or URI recursion are also present in the group object. To only return the attribute values from the leaf objects and not the containing group, add the attribute to the leaf_result_attribute list, and not the result_attribute list, which is always expanded. Note, the default value of &quot;result_attribute&quot; is not empty, you may want to set it explicitly empty when using &quot;leaf_result_attribute&quot; to expand the group to a list of member DN addresses. If groups have both member DN references AND attributes that hold multiple string valued rfc822 addresses, then the string attributes go in &quot;result_attribute&quot;. The attributes that represent the email addresses of objects referenced via a DN (or LDAP URI) go in &quot;leaf_result_attribute&quot;. </p>
<pre> result_attribute = memberaddr
 special_result_attribute = memberdn
 terminal_result_attribute = maildrop
 leaf_result_attribute = mail</pre>
<p>When using terminal and/or leaf result attributes, the result_attribute is best set to an empty value when it is not used, or else explicitly set to the desired value, even if it is the default value &quot;maildrop&quot;. </p>
<p> This feature is available with Postfix 2.4 or later.</p>
<dt><code>scope (default: sub)</code></p>
<dd>The LDAP search scope: <code>sub</code>, <code>base</code>, or <code>one</code>. These translate into LDAP_SCOPE_SUBTREE, LDAP_SCOPE_BASE, and LDAP_SCOPE_ONELEVEL.</p>
<dt><code>bind (default: yes)</code></p>
<dd>Whether or how to bind to the LDAP server. Newer LDAP implementations don&#8217;t require clients to bind, which saves time. Example: </p>
<pre> # Don't bind
 bind = no
 # Use SIMPLE bind
 bind = yes
 # Use SASL bind
 bind = sasl</pre>
<p>Postfix versions prior to 2.8 only support &quot;bind = no&quot; which means don&#8217;t bind, and &quot;bind = yes&quot; which means do a SIMPLE bind. Postfix 2.8 and later also supports &quot;bind = SASL&quot; when compiled with LDAP SASL support as described in LDAP_README, it also adds the synonyms &quot;bind = none&quot; and &quot;bind = simple&quot; for &quot;bind = no&quot; and &quot;bind = yes&quot; respectively. See the SASL section below for additional parameters available with &quot;bind = sasl&quot;. </p>
<p> If you do need to bind, you might consider configuring Postfix to connect to the local machine on a port that&#8217;s an SSL tunnel to your LDAP server. If your LDAP server doesn&#8217;t natively support SSL, put a tunnel (wrapper, proxy, whatever you want to call it) on that system too. This should prevent the password from traversing the network in the clear.</p>
<dt><code>bind_dn (default: empty)</code></p>
<dd>If you do have to bind, do it with this distinguished name. Example: </p>
<pre> bind_dn = uid=postfix, dc=your, dc=com</pre>
<p>With &quot;bind = sasl&quot; (see above) the DN may be optional for some SASL mechanisms, don&#8217;t specify a DN if not needed.</p>
<dt><code>bind_pw (default: empty)</code></p>
<dd>The password for the distinguished name above. If you have to use this, you probably want to make the map configuration file readable only by the Postfix user. When using the obsolete ldap:ldapsource syntax, with map parameters in main.cf, it is not possible to securely store the bind password. This is because main.cf needs to be world readable to allow local accounts to submit mail via the sendmail command. Example: </p>
<pre> bind_pw = postfixpw</pre>
<p>With &quot;bind = sasl&quot; (see above) the password may be optional for some SASL mechanisms, don&#8217;t specify a password if not needed.</p>
<dt><code>cache (IGNORED with a warning)</code></p>
<dd>
<dt><code>cache_expiry (IGNORED with a warning)</code></p>
<dd>
<dt><code>cache_size (IGNORED with a warning)</code></p>
<dd>The above parameters are NO LONGER SUPPORTED by Postfix. Cache support has been dropped from OpenLDAP as of release 2.1.13.</p>
<dt><code>recursion_limit (default: 1000)</code></p>
<dd>A limit on the nesting depth of DN and URL special result attribute evaluation. The limit must be a non-zero positive number.</p>
<dt><code>expansion_limit (default: 0)</code></p>
<dd>A limit on the total number of result elements returned (as a comma separated list) by a lookup against the map. A setting of zero disables the limit. Lookups fail with a temporary error if the limit is exceeded. Setting the limit to 1 ensures that lookups do not return multiple values.</p>
<dt><code>size_limit (default: $expansion_limit)</code></p>
<dd>A limit on the number of LDAP entries returned by any single LDAP search performed as part of the lookup. A setting of 0 disables the limit. Expansion of DN and URL references involves nested LDAP queries, each of which is separately subjected to this limit. </p>
<p> Note: even a single LDAP entry can generate multiple lookup results, via multiple result attributes and/or multi-valued result attributes. This limit caps the per search resource utilization on the LDAP server, not the final multiplicity of the lookup result. It is analogous to the &quot;-z&quot; option of &quot;ldapsearch&quot;.</p>
<dt><code>dereference (default: 0)</code></p>
<dd>When to dereference LDAP aliases. (Note that this has nothing do with Postfix aliases.) The permitted values are those legal for the OpenLDAP/UM LDAP implementations:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>never</p>
<dt>1</p>
<dd>when searching</p>
<dt>2</p>
<dd>when locating the base object for the search</p>
<dt>3</p>
<dd>always</dl>
</dl>
<dd>See ldap.h or the <a href="/docs/linux/man/3-ldap_open/">ldap_open</a>(3) or <a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a>(1) man pages for more information. And if you&#8217;re using an LDAP package that has other possible values, please bring it to the attention of the postfix-users [at] postfix.org mailing list.</p>
<dt><code>chase_referrals (default: 0)</code></p>
<dd>Sets (or clears) LDAP_OPT_REFERRALS (requires LDAP version 3 support).</p>
<dt><code>version (default: 2)</code></p>
<dd>Specifies the LDAP protocol version to use.</p>
<dt><code>debuglevel (default: 0)</code></p>
<dd>What level to set for debugging in the OpenLDAP libraries.</dl>
<h2>Ldap Sasl Parameters</h2>
<p>If you&#8217;re using the OpenLDAP libraries compiled with SASL support, Postfix 2.8 and later built with LDAP SASL support as described in LDAP_README can authenticate to LDAP servers via SASL. </p>
<p> This enables authentication to the LDAP server via mechanisms other than a simple password. The added flexibility has a cost: it is no longer practical to set an explicit timeout on the duration of an LDAP bind operation. Under adverse conditions, whether a SASL bind times out, or if it does, the duration of the timeout is determined by the LDAP and SASL libraries. </p>
<p> It is best to use tables that use SASL binds via <a href="/docs/linux/man/8-proxymap/">proxymap</a>(8), this way the requesting process can time-out the proxymap request. This also lets you tailer the process environment by overriding the <a href="/docs/linux/man/8-proxymap/">proxymap</a>(8) import_environment setting in <a href="/docs/linux/man/5-master-cf/">master.cf</a>(5). Special environment settings may be needed to configure GSSAPI credential caches or other SASL mechanism specific options. The GSSAPI credentials used for LDAP lookups may need to be different than say those used for the Postfix SMTP client to authenticate to remote servers. </p>
<p> Using SASL mechanisms requires LDAP protocol version 3, the default protocol version is 2 for backwards compatibility. You must set &quot;version = 3&quot; in addition to &quot;bind = sasl&quot;. </p>
<p> The following parameters are relevant to using LDAP with SASL</p>
<dl>
<dt><code>sasl_mechs (default: empty)</code></p>
<dd>Space separated list of SASL mechanism(s) to try.</p>
<dt><code>sasl_realm (default: empty)</code></p>
<dd>SASL Realm to use, if applicable.</p>
<dt><code>sasl_authz_id (default: empty)</code></p>
<dd>The SASL authorization identity to assert, if applicable.</p>
<dt><code>sasl_minssf (default: 0)</code></p>
<dd>The minimum required sasl security factor required to establish a connection.</dl>
<h2>Ldap Ssl And Starttls Parameters</h2>
<p>If you&#8217;re using the OpenLDAP libraries compiled with SSL support, Postfix can connect to LDAP SSL servers and can issue the STARTTLS command. </p>
<p> LDAP SSL service can be requested by using a LDAP SSL URL in the server_host parameter: </p>
<pre> server_host = <a href="ldaps://ldap.example.com:636">ldaps://ldap.example.com:636</a></pre>
<p>STARTTLS can be turned on with the start_tls parameter: </p>
<pre> start_tls = yes</pre>
<p>Both forms require LDAP protocol version 3, which has to be set explicitly with: </p>
<pre> version = 3</pre>
<p>If any of the Postfix programs querying the map is configured in master.cf to run chrooted, all the certificates and keys involved have to be copied to the chroot jail. Of course, the private keys should only be readable by the user &quot;postfix&quot;. </p>
<p> The following parameters are relevant to LDAP SSL and STARTTLS:</p>
<dl>
<dt><code>start_tls (default: no)</code></p>
<dd>Whether or not to issue STARTTLS upon connection to the server. Don&#8217;t set this with LDAP SSL (the SSL session is setup automatically when the TCP connection is opened).</p>
<dt><code>tls_ca_cert_dir (No default; set either this or tls_ca_cert_file)</code></p>
<dd>Directory containing X509 Certificate Authority certificates in PEM format which are to be recognized by the client in SSL/TLS connections. The files each contain one CA certificate. The files are looked up by the CA subject name hash value, which must hence be available. If more than one CA certificate with the same name hash value exist, the extension must be different (e.g. 9d66eef0.0, 9d66eef0.1 etc). The search is performed in the ordering of the extension number, regardless of other properties of the certificates. Use the c_rehash utility (from the OpenSSL distribution) to create the necessary links.</p>
<dt><code>tls_ca_cert_file (No default; set either this or tls_ca_cert_dir)</code></p>
<dd>File containing the X509 Certificate Authority certificates in PEM format which are to be recognized by the client in SSL/TLS connections. This setting takes precedence over tls_ca_cert_dir.</p>
<dt><code>tls_cert (No default; you must set this)</code></p>
<dd>File containing client&#8217;s X509 certificate to be used by the client in SSL/ TLS connections.</p>
<dt><code>tls_key (No default; you must set this)</code></p>
<dd>File containing the private key corresponding to the above tls_cert.</p>
<dt><code>tls_require_cert (default: no)</code></p>
<dd>Whether or not to request server&#8217;s X509 certificate and check its validity when establishing SSL/TLS connections. The supported values are <code>no</code> and <code>yes</code>. </p>
<p> With <code>no</code>, the server certificate trust chain is not checked, but with OpenLDAP prior to 2.1.13, the name in the server certificate must still match the LDAP server name. With OpenLDAP 2.0.0 to 2.0.11 the server name is not necessarily what you specified, rather it is determined (by reverse lookup) from the IP address of the LDAP server connection. With OpenLDAP prior to 2.0.13, subjectAlternativeName extensions in the LDAP server certificate are ignored: the server name must match the subject CommonName. The <code>no</code> setting corresponds to the <code>never</code> value of <code>TLS_REQCERT</code> in LDAP client configuration files. </p>
<p> Don&#8217;t use TLS with OpenLDAP 2.0.x (and especially with x &lt;= 11) if you can avoid it. </p>
<p> With <code>yes</code>, the server certificate must be issued by a trusted CA, and not be expired. The LDAP server name must match one of the name(s) found in the certificate (see above for OpenLDAP library version dependent behavior). The <code>yes</code> setting corresponds to the <code>demand</code> value of <code>TLS_REQCERT</code> in LDAP client configuration files. </p>
<p> The &quot;try&quot; and &quot;never&quot; values of <code>TLS_REQCERT</code> have no equivalents here. They are not available with OpenLDAP 2.0, and in any case have questionable security properties. Either you want TLS verified LDAP connections, or you don&#8217;t. </p>
<p> The <code>yes</code> value only works correctly with Postfix 2.5 and later, or with OpenLDAP 2.0. Earlier Postfix releases or later OpenLDAP releases don&#8217;t work together with this setting. Support for LDAP over TLS was added to Postfix based on the OpenLDAP 2.0 API.</p>
<dt><code>tls_random_file (No default)</code></p>
<dd>Path of a file to obtain random bits from when /dev/[u]random is not available, to be used by the client in SSL/TLS connections.</p>
<dt><code>tls_cipher_suite (No default)</code></p>
<dd>Cipher suite to use in SSL/TLS negotiations.</dl>
<h2>Example</h2>
<p>Here&#8217;s a basic example for using LDAP to look up <a href="/docs/linux/man/8-local/">local</a>(8) aliases. Assume that in main.cf, you have: </p>
<pre> alias_maps = hash:/etc/aliases,
 ldap:/etc/postfix/ldap-aliases.cf</pre>
<p>and in ldap:/etc/postfix/ldap-aliases.cf you have: </p>
<pre> server_host = ldap.example.com
 search_base = dc=example, dc=com</pre>
<p>Upon receiving mail for a local address &quot;ldapuser&quot; that isn&#8217;t found in the /etc/aliases database, Postfix will search the LDAP server listening at port 389 on ldap.example.com. It will bind anonymously, search for any directory entries whose mailacceptinggeneralid attribute is &quot;ldapuser&quot;, read the &quot;maildrop&quot; attributes of those found, and build a list of their maildrops, which will be treated as RFC822 addresses to which the message will be delivered.</p>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-mysql_table/">mysql_table</a>(5), MySQL lookup tables
<a href="//www.systutorials.com/docs/linux/man/5-pgsql_table/">pgsql_table</a>(5), PostgreSQL lookup tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview
LDAP_README, Postfix LDAP client guide</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<p>Carsten Hoeger, Hery Rakotoarisoa, John Hensley, Keith Stevenson, LaMont Jones, Liviu Daia, Manuel Guesdon, Mike Mattice, Prabhat K Singh, Sami Haahtinen, Samuel Tardieu, Victor Duchovni, and many others.</p>
