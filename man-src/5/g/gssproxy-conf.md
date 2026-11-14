---
title: "gssproxy-conf(5)"
name: "gssproxy-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gssproxy-conf/"
description: "gssproxy.conf – GssProxy Daemon Configuration file"
---

<p>gssproxy.conf &#8211; GssProxy Daemon Configuration file</p>
<h2>Description</h2>
<p>Optional configuration directives for the gssproxy daemon. </p>
<p> GSS-Proxy conf files are classic ini-style configuration files. Each option consist of a key = value pair. Any characters behind &#8216;#&#8217; will be treated as comments and will be ignored. Boolean parameters accept &quot;1&quot;, &quot;true&quot;, &quot;yes&quot; and &quot;on&quot; as positive values. All other values will be considered as negative values. </p>
<p> GSS-Proxy conf files must either be named &quot;gssproxy.conf&quot;, or be of the form &quot;##-foo.conf&quot; (that is, start with two numbers followed by a dash, and end in &quot;.conf&quot;). Files not conforming to this will be ignored unless specifically requested through command line parameters.</p>
<h2>Sections</h2>
<p>A section in a GSS-Proxy conf file is identified by the sectionname in square brackets ([sectionname]). </p>
<p> There is one special section for global gssproxy settings, called [gssproxy]. </p>
<p> Services such as nfs, apache, ssh, etc. are represented by sections like [service/nfs], [service/apache], etc. and are identified by the &quot;euid&quot; setting (see below).</p>
<h2>Variable Substitutions</h2>
<p>String parameters may contain substitution patterns. This allows gssproxy to deal with patterns for the storage location of keytabs or credential caches easier. </p>
<p> The supported patterns are: </p>
<p> %U</p>
<dl>
<dd>substitutes to the user&#8217;s numeric uid (e.g. 123)</dl>
<p> %u</p>
<dl>
<dd>substitutes to the user&#8217;s username (e.g. john).</dl>
<h2>Options</h2>
<p>gssproxy supports the following options: </p>
<p> allow_any_uid (boolean)</p>
<dl>
<dd>Allow any process of any user to use this service. </p>
<p> Note that absent a custom socket or selinux_context option this option may cause a service definition to mask access to following services. To avoid issues change the order of services in your configuation file so that services with allow_any_uid enabled are listed last, or define a custom socket for other services. </p>
<p> Default: false</dl>
<p> allow_protocol_transition (boolean)</p>
<dl>
<dd>Allow clients to request a ticket to self for an arbitrary user. </p>
<p> This option controls whether s4u2self requests are allowed for the requesting client. The configured keytab is used as the service identity for which a ticket is requested. The KDC still needs to allow the operation for it to succeed. </p>
<p> Default: false</dl>
<p> allow_constrained_delegation (boolean)</p>
<dl>
<dd>Allow clients to request a ticket to another service using an evidence ticket. </p>
<p> This option controls whether s4u2proxy requests are allowed for the requesting client. The KDC still needs to allow the operation for it to succeed. </p>
<p> Default: false</dl>
<p> allow_client_ccache_sync (boolean)</p>
<dl>
<dd>Allow clients to request credentials to be sent back for better caching. </p>
<p> This option allows the proxy, in certain circumstances, to send back an additional option in the response structure of certain calls when it determines that a new ticket may have been added to the internal ccache. Clients can then replace their (encrypted) copy with the updated ccache. </p>
<p> Default: false</dl>
<p> cred_usage (string)</p>
<dl>
<dd>Allow to restrict the kind of operations permitted for this service. </p>
<p> The allowed options are: initiate, accept, both </p>
<p> Default: cred_usage = both</dl>
<p> cred_store (string)</p>
<dl>
<dd>This parameter allows to control in which way gssproxy should use the cred_store interface provided by GSSAPI. The parameter can be defined multiple times per service. </p>
<p> The syntax of the cred_store parameter is as follows: cred_store = &lt;cred_store_option&gt;:&lt;cred_store_value&gt; </p>
<p> Currently this interface supports the following options: </p>
<p> keytab</p>
<dl>
<dd>Defines the keytab the service should use. Example: cred_store = keytab:/path/to/keytab</dl>
<p> client_keytab</p>
<dl>
<dd>Defines a client keytab the service should use. Example: cred_store = client_keytab:/path/to/client_keytab.</dl>
<p> ccache</p>
<dl>
<dd>Defines a credential cache the service should use. Example: cred_store = ccache:/path/to/ccache.</dl>
<p> Notably the client_keytab and the ccache setting typically are used with variable substitution placeholders (see above). For example: </p>
<dl>
<dd>
<pre> <code>cred_store = keytab:/etc/krb5.keytab</code>
 <code>cred_store = ccache:FILE:/var/lib/gssproxy/krb5cc_%U</code>
 <code>cred_store = client_keytab:/var/lib/gssproxy/%U.keytab</code></pre>
</dl>
<p> Default: cred_store =</dl>
<p> debug (boolean)</p>
<dl>
<dd>Enable debugging to syslog. </p>
<p> Default: debug = false</dl>
<p> debug_level (integer)</p>
<dl>
<dd>Detail level at which to log debugging messages. 0 corresponds to no logging, while 1 turns on basic debug logging. Level 2 increases verbosity, including more detailed credential verification. </p>
<p> At level 3 and above, KRB5_TRACE output is logged. If KRB5_TRACE was already set in the execution environment, trace output is sent to its value instead. </p>
<p> Default: 1 if debug is true, otherwise 0</dl>
<p> euid (integer or string)</p>
<dl>
<dd>Either the numeric (e.g., 48) or symbolic (e.g., apache) effective uid of a running process, required to identify a service. </p>
<p> The &quot;euid&quot; parameter is imperative, any section without it will be discarded. </p>
<p> Default: euid =</dl>
<p> enforce_flags (string)</p>
<dl>
<dd>A list of GSS Request Flags that are added unconditionally to every context initialization call. Flags can only be added to the list or removed from the list by prepending a +/- sign to the flag name or value. </p>
<p> Recognized flag names: DELEGATE, MUTUAL_AUTH, REPLAY_DETECT, SEQUENCE, CONFIDENTIALITY, INTEGRITY, ANONYMOUS </p>
<p> Examples: </p>
<dl>
<dd>
<pre> <code>enforce_flags = +REPLAY_DETECT</code>
 <code>enforce_flags = -0x0001</code></pre>
</dl>
<p> Default: enforce_flags =</dl>
<p> filter_flags (string)</p>
<dl>
<dd>A list of GSS Request Flags that are filtered unconditionally from every context initialization call. Flags can only be added to the list or removed from the list by prepending a +/- sign to the flag name or value. </p>
<p> NOTE: Because often gssproxy is used to withold access to credentials the Delegate Flag is filtered by default. To allow a service to delegate credentials use the first example below. </p>
<p> Recognized flag names: DELEGATE, MUTUAL_AUTH, REPLAY_DETECT, SEQUENCE, CONFIDENTIALITY, INTEGRITY, ANONYMOUS </p>
<p> Examples: </p>
<dl>
<dd>
<pre> <code>filter_flags = -DELEGATE</code>
 <code>filter_flags = -0x0001 +ANONYMOUS</code></pre>
</dl>
<p> Default: filter_flags = +DELEGATE</dl>
<p> impersonate (boolean)</p>
<dl>
<dd>Use impersonation (s4u2self + s4u2proxy) to obtain credentials </p>
<p> Default: impersonate = false</dl>
<p> kernel_nfsd (boolean)</p>
<dl>
<dd>Boolean flag that allows the Linux kernel to check if gssproxy is running (via /proc/net/rpc/use-gss-proxy). </p>
<p> Default: kernel_nfsd = false</dl>
<p> krb5_principal (string)</p>
<dl>
<dd>The krb5 principal to be used by this service. </p>
<p> Default: krb5_principal =</dl>
<p> mechs (string)</p>
<dl>
<dd>Currently only <i>krb5</i> is supported. </p>
<p> The &quot;mechs&quot; parameter is imperative, any section without it will be discarded. </p>
<p> Default: mechs =</dl>
<p> run_as_user (string)</p>
<dl>
<dd>The name of the user gssproxy will drop privileges to. </p>
<p> This option is only available in the global section. </p>
<p> Default: run_as_user =</dl>
<p> selinux_context (string)</p>
<dl>
<dd>This parameter instructs the proxy to allow map a request to the service only if the context of the connecting client matches the one defined here. </p>
<p> When this parameter is not set any client will be allowed regardless of their selinux context. </p>
<p> Example: selinux_context = system_u:system_r:gssd_t</dl>
<p> socket (string)</p>
<dl>
<dd>This parameter allows to create a per-service socket file over which gssproxy client and server components communicate. </p>
<p> When this parameter is not set, gssproxy will use a compiled-in default.</dl>
<p> trusted (boolean)</p>
<dl>
<dd>Defines whether this service is considered trusted. Use with caution, this enables impersonation. </p>
<p> Default: trusted = false</dl>
<p> worker threads (integer)</p>
<dl>
<dd>Defines the amount of worker threads gssproxy will create at startup. </p>
<p> Default: worker threads =</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gssproxy/">gssproxy</a></code>(8) and <code><a href="/docs/linux/man/8-gssproxy-mech/">gssproxy-mech</a></code>(8).</p>
<h2>Authors</h2>
<p><code>GSS-Proxy &#8211; <a rel="nofollow" href="http://fedorahosted.org/gss-proxy">http://fedorahosted.org/gss-proxy</a></code></p>
