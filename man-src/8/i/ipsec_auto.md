---
title: "ipsec_auto(8)"
name: "ipsec_auto"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_auto/"
description: "ipsec_auto – control automatically-keyed IPsec connections"
---

<p>ipsec_auto &#8211; control automatically-keyed IPsec connections</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>auto</i> [&#8211;showonly] [&#8211;asynchronous]</p>
<dd>[&#8211;config&nbsp;<wbr><i>configfile</i>] [&#8211;verbose] <i>operation connection</i></p>
<dd>
<dt> <code>ipsec</code> <i>auto</i> [&#8211;showonly] [&#8211;asynchronous]</p>
<dd>[&#8211;config&nbsp;<wbr><i>configfile</i>] [&#8211;verbose] <i>operation connection</i></p>
<dd>
<h2>Examples</h2>
<dl>
<dt> <code>ipsec</code> <i>auto</i> {&nbsp;<wbr>&#8211;add | &#8211;delete | &#8211;replace | &#8211;start&nbsp;<wbr>} <i>connection</i></p>
<dt> <code>ipsec</code> <i>auto</i> {&nbsp;<wbr>&#8211;up | &#8211;down&nbsp;<wbr>} <i>connection</i></p>
<dt> <code>ipsec</code> <i>auto</i> {&nbsp;<wbr>&#8211;route | &#8211;unroute&nbsp;<wbr>} <i>connection</i></p>
<dt> <code>ipsec</code> <i>auto</i> {&nbsp;<wbr>&#8211;status | &#8211;ready&nbsp;<wbr>}</p>
<dt> <code>ipsec</code> <i>auto</i> [&#8211;utc] [&#8211;listall | &#8211;rereadall] [&#8211;rereadsecrets] [&#8211;listcerts] [&#8211;listpubkeys] [&#8211;checkpubkeys] [&#8211;listcacerts] [&#8211;listcrls | &#8211;rereadcrls] [&#8211;listgroups | &#8211;rereadgroups] [&#8211;purgeocsp]</dl>
<h2>Description</h2>
<p><i>Auto</i></p>
<dd>manipulates automatically-keyed Libreswan IPsec connections, setting them up and shutting them down based on the information in the IPsec configuration file. In the normal usage, <i>connection</i> is the name of a connection specification in the configuration file; <i>operation</i> is <code>&#8211;add</code>, <code>&#8211;delete</code>, <code>&#8211;replace</code>, <code>&#8211;start</code>, <code>&#8211;up</code>, <code>&#8211;down</code>, <code>&#8211;route</code>, or <code>&#8211;unroute</code>. The <code>&#8211;ready</code>, <code>&#8211;rereadsecrets</code>, <code>&#8211;rereadgroups</code>, and <code>&#8211;status</code><i>operations</i> do not take a connection name. <i>Auto</i> generates suitable commands and feeds them to a shell for execution. </p>
<p> The <code>&#8211;add</code> operation adds a connection specification to the internal database within <i>pluto</i>; it will fail if <i>pluto</i> already has a specification by that name. The <code>&#8211;delete</code> operation deletes a connection specification from <i>pluto</i>&#8216;s internal database (also tearing down any connections based on it); The <code>&#8211;replace</code> operation is equivalent to <code>&#8211;delete</code> (if there is already a loaded connection by the given name) followed by <code>&#8211;add</code>, and is a convenience for updating <i>pluto</i>&#8216;s internal specification to match an external one. (Note that a <code>&#8211;rereadsecrets</code> may also be needed.) The <code>&#8211;start</code> operation is equivalent to running first with <code>&#8211;add</code> and then with <code>&#8211;up</code>, causing same effect as connection configuration option <code>auto=start</code>. The <code>&#8211;rereadgroups</code> operation causes any changes to the policy group files to take effect (this is currently a synonym for <code>&#8211;ready</code>, but that may change). None of the other operations alters the internal database. </p>
<p> The <code>&#8211;up</code> operation asks <i>pluto</i> to establish a connection based on an entry in its internal database. The <code>&#8211;down</code> operation tells <i>pluto</i> to tear down such a connection. </p>
<p> Normally, <i>pluto</i> establishes a route to the destination specified for a connection as part of the <code>&#8211;up</code> operation. However, the route (for KLIPS) and packet capture (KLIPS and NETKEY) can be established with the <code>&#8211;route</code> operation. Until and unless an actual connection is established, this discards any packets sent there, which may be preferable to having them sent elsewhere based on a more general route (e.g., a default route). </p>
<p> Normally, <i>pluto</i>&#8216;s route (KLIPS) or packet capture (NETKEY) to a destination remains in place when a <code>&#8211;down</code> operation is used to take the connection down (or if connection setup, or later automatic rekeying, fails). This permits establishing a new connection (perhaps using a different specification; the route is altered as necessary) without having a &#8220;window&#8221; in which packets might go elsewhere based on a more general route. Such a route can be removed using the <code>&#8211;unroute</code> operation (and is implicitly removed by <code>&#8211;delete</code>). </p>
<p> The <code>&#8211;ready</code> operation tells <i>pluto</i> to listen for connection-setup requests from other hosts. Doing an <code>&#8211;up</code> operation before doing <code>&#8211;ready</code> on both ends is futile and will not work, although this is now automated as part of IPsec startup and should not normally be an issue. </p>
<p> The <code>&#8211;status</code> operation asks <i>pluto</i> for current connection status. The output format is ad-hoc and likely to change. </p>
<p> The <code>&#8211;rereadsecrets</code> operation tells <i>pluto</i> to re-read the /etc/ipsec.secrets secret-keys file, which it normally reads only at startup time. (This is currently a synonym for <code>&#8211;ready</code>, but that may change.) </p>
<p> The <code>&#8211;rereadsecrets</code> operation tells pluto to re-read the /etc/ipsec.secrets secret-keys file, which it normally reads only at startup time. (This is currently a synonym for <code>&#8211;ready,</code> but that may change.) </p>
<p> The <code>&#8211;rereadcrls</code> operation reads all certificate revocation list (CRL) files contained in the /etc/ipsec.d/crls directory and adds them to pluto&#8217;s list of CRLs. Note CRLs can and should be stored inside NSS instead of in the /etc/ipsec.d/crls directory which will result in automatic updates. This option will be obsoleted in the near future. </p>
<p> The <code>&#8211;rereadall</code> operation is equivalent to the execution of &#8211;rereadsecrets and &#8211;rereadcrls. </p>
<p> The <code>&#8211;listpubkeys</code> operation lists all RSA public keys either received from peers via the IKE protocol embedded in authenticated certificate payloads or loaded locally using the rightcert / leftcert or rightr- sasigkey / leftrsasigkey parameters in <a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a>(5). </p>
<p> The <code>&#8211;listcerts</code> operation lists all X.509 certificates loaded locally using the rightcert and leftcert parameters in <a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a>(5). To see all certificates in the NSS database, use <code>certutil -d /etc/ipsec.d -L</code>. </p>
<p> The <code>&#8211;checkpubkeys</code> operation lists all loaded X.509 certificates which are about to expire or have been expired. </p>
<p> The <code>&#8211;listcacerts</code> operation lists all X.509 CA certificates contained in the NSS database. </p>
<p> The <code>&#8211;listgroups</code> operation lists all groups that are either used in connection definitions in <a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a>(5) or are embedded in loaded X.509 attributes certificates. </p>
<p> The <code>&#8211;listcrls</code> operation lists all Certificate Revocation Lists (CRLs) either loaded locally from the /etc/ipsec.d/crls directory or fetched dynamically from an HTTP or LDAP server. </p>
<p> The <code>&#8211;listall</code> operation is equivalent to the execution of &#8211;listpubkeys, &#8211;listcerts, &#8211;listcacerts, &#8211;listgroups, &#8211;listcrls. </p>
<p> The <code>&#8211;purgeocsp</code> operation displays &#8211;listall and purges the NSS OCSP cache. </p>
<p> The <code>&#8211;showonly</code> option causes <i>auto</i> to show the commands it would run, on standard output, and not run them. </p>
<p> The <code>&#8211;asynchronous</code> option, applicable only to the <code>up</code> operation, tells <i>pluto</i> to attempt to establish the connection, but does not delay to report results. This is especially useful to start multiple connections in parallel when network links are slow. </p>
<p> The <code>&#8211;verbose</code> option instructs <i>auto</i> to pass through all output from <code><a href="/docs/linux/man/8-ipsec_whack/">ipsec_whack</a></code>(8), including log output that is normally filtered out as uninteresting. </p>
<p> The <code>&#8211;config</code> option specifies a non-standard location for the IPsec configuration file (default /etc/ipsec.conf). </p>
<p> See <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5) for details of the configuration file.</p>
<h2>Files</h2>
<dl>
<dd>
<pre>/etc/ipsec.conf default IPSEC configuration file
/etc/ipsec.d X.509 and Opportunistic Encryption files
/var/run/pluto/pluto.ctl Pluto command socket</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_whack/">ipsec_whack</a></code>(8)</p>
<h2>History</h2>
<p>Originally written for the FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Henry Spencer.</p>
<h2>Bugs</h2>
<p>Although an <code>&#8211;up</code> operation does connection setup on both ends, <code>&#8211;down</code> tears only one end of the connection down (although the orphaned end will eventually time out). </p>
<p> There is no support for <code>passthrough</code> connections. </p>
<p> A connection description which uses <code>%defaultroute</code> for one of its <code>nexthop</code> parameters but not the other may be falsely rejected as erroneous in some circumstances. </p>
<p> The exit status of <code>&#8211;showonly</code> does not always reflect errors discovered during processing of the request. (This is fine for human inspection, but not so good for use in scripts.)</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
