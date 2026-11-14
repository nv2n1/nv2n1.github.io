---
title: "unbound-anchor(8)"
name: "unbound-anchor"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unbound-anchor/"
description: "unbound-anchor – Unbound anchor utility."
---

<p><code>unbound-anchor</code> &#8211; Unbound anchor utility.</p>
<h2>Synopsis</h2>
<p><code>unbound-anchor</code> [<code>opts</code>]</p>
<h2>Description</h2>
<p><code>Unbound-anchor</code> performs setup or update of the root trust anchor for DNSSEC validation. It can be run (as root) from the commandline, or run as part of startup scripts. Before you start the <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8) DNS server. </p>
<p> Suggested usage: </p>
<pre> # in the init scripts.
 # provide or update the root anchor (if necessary)
 unbound-anchor -a &quot;/var/lib/unbound/root.key&quot;
 # Please note usage of this root anchor is at your own risk
 # and under the terms of our LICENSE (see source).
 #
 # start validating resolver
 # the unbound.conf contains:
 # auto-trust-anchor-file: &quot;/var/lib/unbound/root.key&quot;
 unbound -c unbound.conf</pre>
<p>This tool provides builtin default contents for the root anchor and root update certificate files. </p>
<p> It tests if the root anchor file works, and if not, and an update is possible, attempts to update the root anchor using the root update certificate. It performs a https fetch of root-anchors.xml and checks the results, if all checks are successful, it updates the root anchor file. Otherwise the root anchor file is unchanged. It performs RFC5011 tracking if the DNSSEC information available via the DNS makes that possible. </p>
<p> It does not perform an update if the certificate is expired, if the network is down or other errors occur. </p>
<p> The available options are:</p>
<dl>
<dt><code>-a </code><i>file</i></p>
<dd>The root anchor key file, that is read in and written out. Default is /var/lib/unbound/root.key. If the file does not exist, or is empty, a builtin root key is written to it.</p>
<dt><code>-c </code><i>file</i></p>
<dd>The root update certificate file, that is read in. Default is /etc/unbound/icannbundle.pem. If the file does not exist, or is empty, a builtin certificate is used.</p>
<dt><code>-l</code></p>
<dd>List the builtin root key and builtin root update certificate on stdout.</p>
<dt><code>-u </code><i>name</i></p>
<dd>The server name, it connects to <a rel="nofollow" href="https://name.">https://name.</a> Specify without https:// prefix. The default is &quot;data.iana.org&quot;. It connects to the port specified with -P. You can pass an IPv4 addres or IPv6 address (no brackets) if you want.</p>
<dt><code>-x </code><i>path</i></p>
<dd>The pathname to the root-anchors.xml file on the server. (forms URL with -u). The default is /root-anchors/root-anchors.xml.</p>
<dt><code>-s </code><i>path</i></p>
<dd>The pathname to the root-anchors.p7s file on the server. (forms URL with -u). The default is /root-anchors/root-anchors.p7s. This file has to be a PKCS7 signature over the xml file, using the pem file (-c) as trust anchor.</p>
<dt><code>-n </code><i>name</i></p>
<dd>The emailAddress for the Subject of the signer&#8217;s certificate from the p7s signature file. Only signatures from this name are allowed. default is dnssec [at] iana.org. If you pass &quot;&quot; then the emailAddress is not checked.</p>
<dt><code>-4</code></p>
<dd>Use IPv4 for domain resolution and contacting the server on https. Default is to use IPv4 and IPv6 where appropriate.</p>
<dt><code>-6</code></p>
<dd>Use IPv6 for domain resolution and contacting the server on https. Default is to use IPv4 and IPv6 where appropriate.</p>
<dt><code>-f </code><i>resolv.conf</i></p>
<dd>Use the given resolv.conf file. Not enabled by default, but you could try to pass /etc/resolv.conf on some systems. It contains the IP addresses of the recursive nameservers to use. However, since this tool could be used to bootstrap that very recursive nameserver, it would not be useful (since that server is not up yet, since we are bootstrapping it). It could be useful in a situation where you know an upstream cache is deployed (and running) and in captive portal situations.</p>
<dt><code>-r </code><i>root.hints</i></p>
<dd>Use the given root.hints file (same syntax as the BIND and Unbound root hints file) to bootstrap domain resolution. By default a list of builtin root hints is used. Unbound-anchor goes to the network itself for these roots, to resolve the server (-u option) and to check the root DNSKEY records. It does so, because the tool when used for bootstrapping the recursive resolver, cannot use that recursive resolver itself because it is bootstrapping that server.</p>
<dt><code>-v</code></p>
<dd>More verbose. Once prints informational messages, multiple times may enable large debug amounts (such as full certificates or byte-dumps of downloaded files). By default it prints almost nothing. It also prints nothing on errors by default; in that case the original root anchor file is simply left undisturbed, so that a recursive server can start right after it.</p>
<dt><code>-C </code><i>unbound.conf</i></p>
<dd>Debug option to read unbound.conf into the resolver process used.</p>
<dt><code>-P </code><i>port</i></p>
<dd>Set the port number to use for the https connection. The default is 443.</p>
<dt><code>-F</code></p>
<dd>Debug option to force update of the root anchor through downloading the xml file and verifying it with the certificate. By default it first tries to update by contacting the DNS, which uses much less bandwidth, is much faster (200 msec not 2 sec), and is nicer to the deployed infrastructure. With this option, it still attempts to do so (and may verbosely tell you), but then ignores the result and goes on to use the xml fallback method.</p>
<dt><code>-h</code></p>
<dd>Show the version and commandline option help.</dl>
<h2>Exit Code</h2>
<p>This tool exits with value 1 if the root anchor was updated using the certificate or if the builtin root-anchor was used. It exits with code 0 if no update was necessary, if the update was possible with RFC5011 tracking, or if an error occurred. </p>
<p> You can check the exit value in this manner: </p>
<pre> unbound-anchor -a &quot;root.key&quot; || logger &quot;Please check root.key&quot;</pre>
<p>Or something more suitable for your operational environment.</p>
<h2>Trust</h2>
<p>The root keys and update certificate included in this tool are provided for convenience and under the terms of our license (see the LICENSE file in the source distribution or <a rel="nofollow" href="http://unbound.nlnetlabs.nl/svn/trunk/LICENSE)">http://unbound.nlnetlabs.nl/svn/trunk/LICENSE)</a> and might be stale or not suitable to your purpose. </p>
<p> By running &quot;unbound-anchor -l&quot; the keys and certificate that are configured in the code are printed for your convenience. </p>
<p> The build-in configuration can be overridden by providing a root-cert file and a rootkey file.</p>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/unbound/root.key</i></p>
<dd>The root anchor file, updated with 5011 tracking, and read and written to. The file is created if it does not exist.</p>
<dt><i>/etc/unbound/icannbundle.pem</i></p>
<dd>The trusted self-signed certificate that is used to verify the downloaded DNSSEC root trust anchor. You can update it by fetching it from <a rel="nofollow" href="https://data.iana.org/root-anchors/icannbundle.pem">https://data.iana.org/root-anchors/icannbundle.pem</a> (and validate it). If the file does not exist or is empty, a builtin version is used.</p>
<dt><i><a rel="nofollow" href="https://data.iana.org/root-anchors/root-anchors.xml">https://data.iana.org/root-anchors/root-anchors.xml</a></i></p>
<dd>Source for the root key information.</p>
<dt><i><a rel="nofollow" href="https://data.iana.org/root-anchors/root-anchors.p7s">https://data.iana.org/root-anchors/root-anchors.p7s</a></i></p>
<dd>Signature on the root key information.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). </p>
