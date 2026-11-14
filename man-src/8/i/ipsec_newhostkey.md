---
title: "ipsec_newhostkey(8)"
name: "ipsec_newhostkey"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_newhostkey/"
description: "ipsec_newhostkey – generate a new raw RSA authentication key for a host"
---

<p>ipsec_newhostkey &#8211; generate a new raw RSA authentication key for a host</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>newhostkey</i> [[&#8211;quiet] | [&#8211;verbose]] [&#8211;nssdir<i>nssdir</i>] [&#8211;password&nbsp;<wbr><i>password</i>] [&#8211;bits&nbsp;<wbr><i>bits</i>] [&#8211;seeddev&nbsp;<wbr><i>device</i>] [&#8211;hostname&nbsp;<wbr><i>hostname</i>] [&#8211;output&nbsp;<wbr><i>filename</i>]</dl>
<h2>Description</h2>
<p><i>newhostkey</i></p>
<dd>generates an RSA public/private key pair suitable for authenticating this host is generated and stored in the NSS database. </p>
<p> See <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8) for how to extract the public key from the NSS database.</p>
<h3>Output Options</h3>
<p><code>&#8211;output</code>&nbsp;<wbr><i>filename</i></p>
<dl>
<dd>The <code>&#8211;output</code> option specifies an <i>ipsec.secrets</i> formatted file (see <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5)). to store the public key information. If the file does not exist, it is created under umask <code>077</code>. If the file already exists and is non-empty, a warning message about that is written to standard error, and the output is appended to the file.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dd>The <code>&#8211;quiet</code> option suppresses both the <i>rsasigkey</i> narrative and the existing-file warning message.</dl>
<p> <code>&#8211;nssdir</code>&nbsp;<wbr><i>nssdir</i></p>
<dl>
<dd>The <code>&#8211;nssdir</code> option specifies the NSS DB directory where the certificate key, and modsec databases reside (default /etc/ipsec.d.</dl>
<p> <code>&#8211;password</code>&nbsp;<wbr><i>password</i></p>
<dl>
<dd>The <code>&#8211;password</code> option specifies a module authentication <i>password</i> that may be required if FIPS mode is enabled.</dl>
<p> <code>&#8211;bits</code>&nbsp;<wbr><i>bits</i></p>
<dl>
<dd>The <code>&#8211;bits</code> option specifies the number of bits in the RSA key; the current default is a random (multiple of 16) value between 3072 and 4096. The minimum allowed is 2192.</dl>
<p> <code>&#8211;seeddev</code>&nbsp;<wbr><i>device</i></p>
<dl>
<dd>The <code>&#8211;seeddev</code> is used to specify the random device (default /dev/random used to seed the crypto library RNG.</dl>
<p> <code>&#8211;hostname</code>&nbsp;<wbr><i>hostname</i></p>
<dl>
<dd>The <code>&#8211;hostname</code> option is passed through to <i>rsasigkey</i> to tell it what host name to label the output with (via its <code>&#8211;hostname</code> option).</dl>
<h2>Files</h2>
<p>/dev/random, /dev/urandom</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec_rsasigkey/">ipsec_rsasigkey</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8), <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5)</p>
<h2>History</h2>
<p>Originally written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Henry Spencer. Updated by Paul Wouters</p>
<h2>Bugs</h2>
<p>As with <i>rsasigkey</i>, the run time is difficult to predict, since depletion of the system&#8217;s randomness pool can cause arbitrarily long waits for random bits for seeding the NSS library, and the prime-number searches can also take unpredictable (and potentially large) amounts of CPU time. See <code><a href="/docs/linux/man/8-ipsec_rsasigkey/">ipsec_rsasigkey</a></code>(8) . </p>
<p> A higher-level tool which could handle the clerical details of changing to a new key would be helpful.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
