---
title: "kinit(1)"
name: "kinit"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kinit/"
description: "kinit – obtain and cache Kerberos ticket-granting ticket"
---

<h2>NAME</h2>
<p> kinit &#8211; obtain and cache Kerberos ticket-granting ticket</p>
<h2>SYNOPSIS</h2>
<p> <code>kinit</code> [<code>-V</code>] [<code>-l</code> <i>lifetime</i>] [<code>-s</code> <i>start_time</i>] [<code>-r</code> <i>renewable_life</i>] [<code>-p</code> | &#8211;<code>P</code>] [<code>-f</code> | &#8211;<code>F</code>] [<code>-a</code>] [<code>-A</code>] [<code>-C</code>] [<code>-E</code>] [<code>-v</code>] [<code>-R</code>] [<code>-k</code> [-<code>t</code> <i>keytab_file</i>]] [<code>-c</code> <i>cache_name</i>] [<code>-n</code>] [<code>-S</code> <i>service_name</i>] [<code>-I</code> <i>input_ccache</i>] [<code>-T</code> <i>armor_ccache</i>] [<code>-X</code> <i>attribute</i>[=<i>value</i>]] [<i>principal</i>]</p>
<h2>DESCRIPTION</h2>
<p> kinit obtains and caches an initial ticket-granting ticket for <i>principal</i>. If <i>principal</i> is absent, kinit chooses an appropriate principal name based on existing credential cache contents or the local username of the user invoking kinit. Some options modify the choice of principal name.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> display verbose output.</p>
<dt><code>-l</code> <i>lifetime</i></p>
<dd> (<i>duration</i> string.) Requests a ticket with the lifetime <i>lifetime</i>. </p>
<p> For example, <code>kinit -l 5:30</code> or <code>kinit -l 5h30m</code>. </p>
<p> If the <code>-l</code> option is not specified, the default ticket lifetime (configured by each site) is used. Specifying a ticket lifetime longer than the maximum ticket lifetime (configured by each site) will not override the configured maximum ticket lifetime.</p>
<dt><code>-s</code> <i>start_time</i></p>
<dd> (<i>duration</i> string.) Requests a postdated ticket. Postdated tickets are issued with the <code>invalid</code> flag set, and need to be resubmitted to the KDC for validation before use. </p>
<p> <i>start_time</i> specifies the duration of the delay before the ticket can become valid.</p>
<dt><code>-r</code> <i>renewable_life</i></p>
<dd> (<i>duration</i> string.) Requests renewable tickets, with a total lifetime of <i>renewable_life</i>.</p>
<dt><code>-f</code></p>
<dd> requests forwardable tickets.</p>
<dt><code>-F</code></p>
<dd> requests non-forwardable tickets.</p>
<dt><code>-p</code></p>
<dd> requests proxiable tickets.</p>
<dt><code>-P</code></p>
<dd> requests non-proxiable tickets.</p>
<dt><code>-a</code></p>
<dd> requests tickets restricted to the host&#8217;s local address[es].</p>
<dt><code>-A</code></p>
<dd> requests tickets not restricted by address.</p>
<dt><code>-C</code></p>
<dd> requests canonicalization of the principal name, and allows the KDC to reply with a different client principal from the one requested.</p>
<dt><code>-E</code></p>
<dd> treats the principal name as an enterprise name (implies the <code>-C</code> option).</p>
<dt><code>-v</code></p>
<dd> requests that the ticket-granting ticket in the cache (with the <code>invalid</code> flag set) be passed to the KDC for validation. If the ticket is within its requested time range, the cache is replaced with the validated ticket.</p>
<dt><code>-R</code></p>
<dd> requests renewal of the ticket-granting ticket. Note that an expired ticket cannot be renewed, even if the ticket is still within its renewable life. </p>
<p> Note that renewable tickets that have expired as reported by <i><a href="/docs/linux/man/1-klist/">klist</a>(1)</i> may sometimes be renewed using this option, because the KDC applies a grace period to account for client-KDC clock skew. See <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i> <code>clockskew</code> setting.</p>
<dt><code>-k</code> [<code>-i</code> | <code>-t</code> <i>keytab_file</i>]</p>
<dd> requests a ticket, obtained from a key in the local host&#8217;s keytab. The location of the keytab may be specified with the <code>-t</code> <i>keytab_file</i> option, or with the <code>-i</code> option to specify the use of the default client keytab; otherwise the default keytab will be used. By default, a host ticket for the local host is requested, but any principal may be specified. On a KDC, the special keytab location <code>KDB:</code> can be used to indicate that kinit should open the KDC database and look up the key directly. This permits an administrator to obtain tickets as any principal that supports authentication based on the key.</p>
<dt><code>-n</code></p>
<dd> Requests anonymous processing. Two types of anonymous principals are supported. </p>
<p> For fully anonymous Kerberos, configure pkinit on the KDC and configure <code>pkinit_anchors</code> in the client&#8217;s <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i>. Then use the <code>-n</code> option with a principal of the form <code>@REALM</code> (an empty principal name followed by the at-sign and a realm name). If permitted by the KDC, an anonymous ticket will be returned. </p>
<p> A second form of anonymous tickets is supported; these realm-exposed tickets hide the identity of the client but not the client&#8217;s realm. For this mode, use <code>kinit -n</code> with a normal principal name. If supported by the KDC, the principal (but not realm) will be replaced by the anonymous principal. </p>
<p> As of release 1.8, the MIT Kerberos KDC only supports fully anonymous operation. </p>
<p> <code>-I</code> <i>input_ccache</i> Specifies the name of a credentials cache that already contains a ticket. When obtaining that ticket, if information about how that ticket was obtained was also stored to the cache, that information will be used to affect how new credentials are obtained, including preselecting the same methods of authenticating to the KDC.</p>
<dt><code>-T</code> <i>armor_ccache</i></p>
<dd> Specifies the name of a credentials cache that already contains a ticket. If supported by the KDC, this cache will be used to armor the request, preventing offline dictionary attacks and allowing the use of additional preauthentication mechanisms. Armoring also makes sure that the response from the KDC is not modified in transit.</p>
<dt><code>-c</code> <i>cache_name</i></p>
<dd> use <i>cache_name</i> as the Kerberos 5 credentials (ticket) cache location. If this option is not used, the default cache location is used. </p>
<p> The default cache location may vary between systems. If the <code>KRB5CCNAME</code> environment variable is set, its value is used to locate the default cache. If a principal name is specified and the type of the default cache supports a collection (such as the DIR type), an existing cache containing credentials for the principal is selected or a new one is created and becomes the new primary cache. Otherwise, any existing contents of the default cache are destroyed by kinit.</p>
<dt><code>-S</code> <i>service_name</i></p>
<dd> specify an alternate service name to use when getting initial tickets.</p>
<dt><code>-X</code> <i>attribute</i>[=<i>value</i>]</p>
<dd> specify a pre-authentication <i>attribute</i> and <i>value</i> to be interpreted by pre-authentication modules. The acceptable attribute and value values vary from module to module. This option may be specified multiple times to specify multiple attributes. If no value is specified, it is assumed to be &quot;yes&quot;. </p>
<p> The following attributes are recognized by the PKINIT pre-authentication mechanism:</p>
<dt><code>X509_user_identity</code>=<i>value</i></p>
<dd> specify where to find user&#8217;s X509 identity information</p>
<dt><code>X509_anchors</code>=<i>value</i></p>
<dd> specify where to find trusted X509 anchor information</p>
<dt><code>flag_RSA_PROTOCOL</code>[<code>=yes</code>]</p>
<dd> specify use of RSA, rather than the default Diffie-Hellman protocol</dl>
<h2>ENVIRONMENT</h2>
<p> kinit uses the following environment variables:</p>
<dl>
<dt><code>KRB5CCNAME</code></p>
<dd> Location of the default Kerberos 5 credentials cache, in the form <i>type</i>:<i>residual</i>. If no <i>type</i> prefix is present, the <code>FILE</code> type is assumed. The type of the default cache may determine the availability of a cache collection; for instance, a default cache of type <code>DIR</code> causes caches within the directory to be present in the collection.</dl>
<h2>FILES</h2>
<dl>
<dt><code>FILE:/tmp/krb5cc_%{uid}</code></p>
<dd> default location of Kerberos 5 credentials cache</p>
<dt><code>FILE:/etc/krb5.keytab</code></p>
<dd> default location for the local host&#8217;s keytab.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-klist/">klist</a>(1)</i>, <i><a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1)</i>, <a href="/docs/linux/man/1-kerberos/">kerberos</a>(1)</p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
