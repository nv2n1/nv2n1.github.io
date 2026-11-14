---
title: "strongimcv(8)"
name: "strongimcv"
section: "8"
letter: "s"
url: "/docs/linux/man/8-strongimcv/"
description: "ipsec – invoke IPsec utilities"
---

<p>ipsec &#8211; invoke IPsec utilities</p>
<h2>Synopsis</h2>
<p><i>command</i> [<i>arguments</i>] [<i>options</i>]</p>
<h2>Description</h2>
<p>The <code>ipsec</code> utility invokes any of several utilities involved in controlling and monitoring the IPsec encryption/authentication system, running the specified <i>command</i> with the specified <i>arguments</i> and <i>options</i> as if it had been invoked directly. This largely eliminates possible name collisions with other software, and also permits some centralized services. </p>
<p> All the commands described in this manual page are built-in and are used to control and monitor IPsec connections as well as the IKE daemon. </p>
<p> For other commands <i>ipsec</i> supplies the invoked <i>command</i> with a suitable PATH environment variable, and also provides the environment variables listed under <i>ENVIRONMENT</i>.</p>
<h3>Control Commands</h3>
<dl>
<dt><code>start [</code><i>starter options</i><code>]</code></p>
<dd>calls <code>starter</code> which in turn parses <i>ipsec.conf</i> and starts the IKE daemon <i>charon</i>.</p>
<dt><code>update</code></p>
<dd>sends a <i>HUP</i> signal to <code>starter</code> which in turn determines any changes in <i>ipsec.conf</i> and updates the configuration on the running IKE daemon <i>charon</i>.</p>
<dt><code>reload</code></p>
<dd>sends a <i>USR1</i> signal to <code>starter</code> which in turn reloads the whole configuration of the running IKE daemon <i>charon</i> based on the actual <i>ipsec.conf</i>.</p>
<dt><code>restart</code></p>
<dd>is equivalent to <code>stop</code> followed by <code>start</code> after a guard of 2 seconds.</p>
<dt><code>stop</code></p>
<dd>terminates all IPsec connections and stops the IKE daemon <i>charon</i> by sending a <i>TERM</i> signal to <code>starter.</code></p>
<dt><code>up </code><i>name</i></p>
<dd>tells the IKE daemon to start up connection <i>name</i>.</p>
<dt><code>down </code><i>name</i></p>
<dd>tells the IKE daemon to terminate connection <i>name</i>.</p>
<dt><code>down </code><i>name{n}</i></p>
<dd>terminates IKEv1 Quick Mode and IKEv2 CHILD SA instance <i>n</i> of connection <i>name</i>.</p>
<dt><code>down </code><i>name{*}</i></p>
<dd>terminates all IKEv1 Quick Mode and IKEv2 CHILD SA instances of connection <i>name</i>.</p>
<dt><code>down </code><i>name[n]</i></p>
<dd>terminates IKE SA instance <i>n</i> of connection <i>name</i>.</p>
<dt><code>down </code><i>name[*]</i></p>
<dd>terminates all IKE SA instances of connection <i>name</i>.</p>
<dt><code>route </code><i>name</i></p>
<dd>tells the IKE daemon to insert an IPsec policy in the kernel for connection <i>name</i>. The first payload packet matching the IPsec policy will automatically trigger an IKE connection setup.</p>
<dt><code>unroute </code><i>name</i></p>
<dd>remove the IPsec policy in the kernel for connection <i>name</i>.</p>
<dt><code>status [</code><i>name</i><code>]</code></p>
<dd>returns concise status information either on connection <i>name</i> or if the argument is lacking, on all connections.</p>
<dt><code>statusall [</code><i>name</i><code>]</code></p>
<dd>returns detailed status information either on connection <i>name</i> or if the argument is lacking, on all connections.</dl>
<h3>List Commands</h3>
<dl>
<dt><code>listalgs</code></p>
<dd>returns a list supported cryptographic algorithms usable for IKE, and their corresponding plugin.</p>
<dt><code>listpubkeys [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of RSA public keys that were either loaded in raw key format or extracted from X.509 and|or OpenPGP certificates.</p>
<dt><code>listcerts [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of X.509 and|or OpenPGP certificates that were either loaded locally by the IKE daemon or received via the IKE protocol.</p>
<dt><code>listcacerts [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of X.509 Certification Authority (CA) certificates that were loaded locally by the IKE daemon from the <i>/etc/ipsec.d/cacerts/</i> directory or received via the IKE protocol.</p>
<dt><code>listaacerts [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of X.509 Authorization Authority (AA) certificates that were loaded locally by the IKE daemon from the <i>/etc/ipsec.d/aacerts/</i> directory.</p>
<dt><code>listocspcerts [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of X.509 OCSP Signer certificates that were either loaded locally by the IKE daemon from the <i>/etc/ipsec.d/ocspcerts/</i> directory or were sent by an OCSP server.</p>
<dt><code>listacerts [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of X.509 Attribute certificates that were loaded locally by the IKE daemon from the <i>/etc/ipsec.d/acerts/</i> directory.</p>
<dt><code>listgroups [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of groups that are used to define user authorization profiles.</p>
<dt><code>listcainfos [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns certification authority information (CRL distribution points, OCSP URIs, LDAP servers) that were defined by <code>ca</code> sections in <i>ipsec.conf</i>.</p>
<dt><code>listcrls [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns a list of Certificate Revocation Lists (CRLs) that were either loaded by the IKE daemon from the <i>/etc/ipsec.d/crls</i> directory or fetched from an HTTP- or LDAP-based CRL distribution point.</p>
<dt><code>listocsp [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns revocation information fetched from OCSP servers.</p>
<dt><code>listplugins</code></p>
<dd>returns a list of all loaded plugin features.</p>
<dt><code>listcounters [</code><i>name</i><code>]</code></p>
<dd>returns a list of global or connection specific IKE counter values collected since daemon startup.</p>
<dt><code>listall [</code><i>&#8211;utc</i><code>]</code></p>
<dd>returns all information generated by the list commands above. Each list command can be called with the <code>&#8211;utc</code> option which displays all dates in UTC instead of local time.</dl>
<h3>Reread Commands</h3>
<dl>
<dt><code>rereadsecrets</code></p>
<dd>flushes and rereads all secrets defined in <i>ipsec.secrets</i>.</p>
<dt><code>rereadcacerts</code></p>
<dd>reads all certificate files contained in the <i>/etc/ipsec.d/cacerts</i> directory and adds them to the list of Certification Authority (CA) certificates.</p>
<dt><code>rereadaacerts</code></p>
<dd>reads all certificate files contained in the <i>/etc/ipsec.d/aacerts</i> directory and adds them to the list of Authorization Authority (AA) certificates.</p>
<dt><code>rereadocspcerts</code></p>
<dd>reads all certificate files contained in the <i>/etc/ipsec.d/ocspcerts/</i> directory and adds them to the list of OCSP signer certificates.</p>
<dt><code>rereadacerts</code></p>
<dd>reads all certificate files contained in the <i>/etc/ipsec.d/acerts/</i> directory and adds them to the list of attribute certificates.</p>
<dt><code>rereadcrls</code></p>
<dd>reads all Certificate Revocation Lists (CRLs) contained in the <i>/etc/ipsec.d/crls/</i> directory and adds them to the list of CRLs.</p>
<dt><code>rereadall</code></p>
<dd>executes all reread commands listed above.</dl>
<h3>Reset Commands</h3>
<dl>
<dt><code>resetcounters [</code><i>name</i><code>]</code></p>
<dd>resets global or connection specific counters.</dl>
<h3>Purge Commands</h3>
<dl>
<dt><code>purgecerts</code></p>
<dd>purges all cached certificates.</p>
<dt><code>purgecrl</code></p>
<dd>purges all cached CRLs.</p>
<dt><code>purgeike</code></p>
<dd>purges IKE SAs that don&#8217;t have a Quick Mode or CHILD SA.</p>
<dt><code>purgeocsp</code></p>
<dd>purges all cached OCSP information records.</dl>
<h3>Info Commands</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd>returns the usage information for the <code>ipsec</code> command.</p>
<dt><code>&#8211;version</code></p>
<dd>returns the version in the form of <code>Linux strongSwan U&lt;strongSwan userland version&gt;/K&lt;Linux kernel version&gt;</code> if strongSwan uses the native NETKEY IPsec stack of the Linux kernel it is running on.</p>
<dt><code>&#8211;versioncode</code></p>
<dd>returns the version number in the form of <code>U&lt;strongSwan userland version&gt;/K&lt;Linux kernel version&gt;</code> if strongSwan uses the native NETKEY IPsec stack of the Linux kernel it is running on.</p>
<dt><code>&#8211;copyright</code></p>
<dd>returns the copyright information.</p>
<dt><code>&#8211;directory</code></p>
<dd>returns the <i>LIBEXECDIR</i> directory as defined by the configure options.</p>
<dt><code>&#8211;confdir</code></p>
<dd>returns the <i>SYSCONFDIR</i> directory as defined by the configure options.</p>
<dt><code>&#8211;piddir</code></p>
<dd>returns the <i>PIDDIR</i> directory as defined by the configure options.</dl>
<h2>Files</h2>
<p>/usr/libexec/ipsec<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>utilities directory</p>
<h2>Environment</h2>
<p>When calling other commands the <code>ipsec</code> command supplies the following environment variables. </p>
<pre>IPSEC_DIR directory containing ipsec programs and utilities
IPSEC_BINDIR directory containing <code>pki</code> command
IPSEC_SBINDIR directory containing <code>ipsec</code> command
IPSEC_CONFDIR directory containing configuration files
IPSEC_PIDDIR directory containing PID/socket files
IPSEC_SCRIPT name of the ipsec script
IPSEC_NAME name of ipsec distribution
IPSEC_VERSION version numer of ipsec userland and kernel
IPSEC_STARTER_PID PID file for ipsec starter
IPSEC_CHARON_PID PID file for IKE keying daemon</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5), <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5)</p>
<h2>History</h2>
<p>Originally written for the FreeS/WAN project by Henry Spencer. Updated and extended for the strongSwan project &lt;<a rel="nofollow" href="http://www.strongswan.org">http://www.strongswan.org</a>&gt; by Tobias Brunner and Andreas Steffen.</p>
