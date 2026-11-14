---
title: "ipsec_showhostkey(8)"
name: "ipsec_showhostkey"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_showhostkey/"
description: "ipsec_showhostkey – show host’s authentication key"
---

<p>ipsec_showhostkey &#8211; show host&#8217;s authentication key</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>showhostkey</i> [&#8211;verbose] {&#8211;version | &#8211;list | &#8211;dump | &#8211;left | &#8211;right | &#8211;ipseckey}</p>
<dd>[&#8211;ckaid&nbsp;<wbr><i>ckaid</i>&nbsp;<wbr>| &#8211;rsaid&nbsp;<wbr><i>rsaid</i>]</p>
<dd>[&#8211;gateway&nbsp;<wbr><i>gateway</i>] [&#8211;precedence&nbsp;<wbr><i>precedence</i>]</p>
<dd>[&#8211;nssdir&nbsp;<wbr><i>nssdir</i>] [&#8211;password&nbsp;<wbr><i>password</i>]</dl>
<h2>Description</h2>
<p><i>Showhostkey</i></p>
<dd>outputs (on standard output) a public key suitable for this host, in the format specified, using the host key information stored in the NSS database. </p>
<p> In general, since only the super-user can access the NSS database, only the super-user can display the public key information.</p>
<h3>Common Options</h3>
<p><code>&#8211;version</code></p>
<dl>
<dd>Print the libreswan version, then exit.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dd>Increase the verbosity.</dl>
<p> <code>&#8211;nssdir </code><i>nssdir</i></p>
<dl>
<dd>Specify the libreswan directory that contains the NSS database (default /etc/ipsec.d).</dl>
<p> <code>&#8211;password </code><i>password</i></p>
<dl>
<dd>Specify the password to use when accessing the NSS database (default contained in /etc/ipsec.d/nsspassword).</dl>
<h3>List Options</h3>
<p><code>&#8211;list</code></p>
<dl>
<dd>List the private keys.</dl>
<p> <code>&#8211;dump</code></p>
<dl>
<dd>List, with more details, the private keys.</dl>
<h3>Public Key Options</h3>
<p><code>&#8211;ckaid</code> <i>ckaid</i></p>
<dl>
<dd>Select the public key to display using the NSS ckaid.</dl>
<p> <code>&#8211;rsaid</code> <i>rsaid</i></p>
<dl>
<dd>Select the public key to display using the RSA key ID.</dl>
<p> <code>&#8211;left</code>, <code>&#8211;right</code></p>
<dl>
<dd>Print the selected public key in <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5) format, as a <code>leftrsasigkey</code> or <code>rightrsasigkey</code> parameter respectively. For example, <code>&#8211;left</code> might give (with the key data trimmed down for clarity): </p>
<dl>
<dd>
<pre>leftrsasigkey=0sAQOF8tZ2...+buFuFn/</pre>
</dl>
</dl>
<p> <code>&#8211;ipseckey</code></p>
<dl>
<dd>Print the selected public key in a format suitable for use as opportunistic-encryption DNS IPSECKEY record format (RFC 4025). A gateway can be specified with the <code>&#8211;gateway</code>, which currently supports IPv4 and IPv6 addresses. For the host name, the value returned by <i>gethostname</i> is used, with a <code>.</code> appended. </p>
<p> For example, <code>&#8211;ipseckey &#8211;gateway 10.11.12.13</code> might give (with the key data trimmed for clarity): </p>
<dl>
<dd>
<pre>IN IPSECKEY 10 1 2 10.11.12.13 AQOF8tZ2...+buFuFn/&quot;</pre>
</dl>
</dl>
<p> <code>&#8211;gateway </code><i>gateway</i></p>
<dl>
<dd>For <code>&#8211;ipseckey</code>, specify the <i>gateway</i> to display with the DNS IPSECKEY record.</dl>
<p> <code>&#8211;precedence </code><i>precedence</i></p>
<dl>
<dd>For <code>&#8211;ipseckey</code>, specify the <i>precedence</i> to display with the DNS IPSECKEY record.</dl>
<h2>Diagnostics</h2>
<p>A complaint about &#8220;no pubkey line found&#8221; indicates that the host has a key but it was generated with an old version of FreeS/WAN and does not contain the information that <i>showhostkey</i> needs.</p>
<h2>Files</h2>
<p>/etc/ipsec.d, /etc/ipsec.d/nsspassword</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5), <code>ipsec <a href="/docs/linux/man/8-rsasigkey/">rsasigkey</a></code>(8)<code>ipsec <a href="/docs/linux/man/8-newhostkey/">newhostkey</a></code>(8)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Henry Spencer. Updated by Paul Wouters for the IPSECKEY format.</p>
<h2>Bugs</h2>
<p>Arguably, rather than just reporting the no-IN-KEY-line-found problem, <i>showhostkey</i> should be smart enough to run the existing key through <i>rsasigkey</i> with the <code>&#8211;oldkey</code> option, to generate a suitable output line.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
