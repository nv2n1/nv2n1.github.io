---
title: "ods-control(8)"
name: "ods-control"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ods-control/"
description: "ods-control – OpenDNSSEC control utility"
---

<p><code>ods-control</code> &#8211; OpenDNSSEC control utility</p>
<h2>Synopsis</h2>
<p><code>ods-control ksm &#8230;</code><br />
 <code>ods-control hsm &#8230;</code><br />
 <code>ods-control signer &#8230;</code><br />
 <code>ods-control start</code><br />
 <code>ods-control stop</code><br />
 <code>ods-control enforcer start</code><br />
 <code>ods-control enforcer stop</code><br />
 <code>ods-control enforcer notify</code></p>
<h2>Description</h2>
<p>ods-control is a helper utility which gives a combined interface for different command utilities within OpenDNSSEC. It can also start and stop OpenDNSSEC by controlling the two daemons.</p>
<h2>Options</h2>
<dl>
<dt><code>ksm</code></p>
<dd>The remainder of the command line will be sent to the ods-ksmutil utility</p>
<dt><code>hsm</code></p>
<dd>The remainder of the command line will be sent to the ods-hsmutil utility</p>
<dt><code>signer</code></p>
<dd>The remainder of the command line will be sent to the ods-signer utility</p>
<dt><code>start</code></p>
<dd>Will start the two daemons of OpenDNSSEC, ods-enforcerd and ods-signerd</p>
<dt><code>stop</code></p>
<dd>Will stop the two daemons of OpenDNSSEC, ods-enforcerd and ods-signerd</p>
<dt><code>enforcer start</code></p>
<dd>Start the ods-enforcerd daemon without touching the ods-signerd and return non-zero on problems</p>
<dt><code>enforcer stop</code></p>
<dd>Stop the ods-enforcerd daemon without touching the ods-signerd and return non-zero on problems</p>
<dt><code>enforcer notify</code></p>
<dd>Notify the enforcer that its database has been updated and may need further processing by the KASP Enforcer.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>Authors</h2>
<p><code>ods-control</code> was written by Jakob Schlyter as part of the OpenDNSSEC project.</p>
