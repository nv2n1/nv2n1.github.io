---
title: "ods-hsmspeed(1)"
name: "ods-hsmspeed"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ods-hsmspeed/"
description: "ods-hsmspeed – OpenDNSSEC HSM speed tester"
---

<h2>NAME</h2>
<p> <code>ods-hsmspeed</code> &#8211; OpenDNSSEC HSM speed tester</p>
<h2>SYNOPSIS</h2>
<p> <code>ods-hsmspeed</code> [<code>-c</code> <i>config</i>] <code>-r</code> <i>repository</i> [<code>-i</code> <i>iterations</i>] [<code>-s</code> <i>keysize</i>] [<code>-t</code> <i>threads</i>]</p>
<h2>DESCRIPTION</h2>
<p> The ods-hsmspeed utility is part of OpenDNSSEC and can be used to test the performance of the configured HSMs. </p>
<p> The components of OpenDNSSEC do not talk directly to the HSMs, but uses an internal library called libhsm. It then talks to the HSMs using PKCS#11. The libhsm simplifies the process of creating keys and signatures for the other components of OpenDNSSEC. </p>
<p> ods-hsmspeed will measure the speed by using the libhsm. The result that you get is somewhat lower than what the manufactures promises, because the libhsm creates some overhead to the pure PKCS#11 environment.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>config</i></p>
<dd> Path to an OpenDNSSEC configuration file. </p>
<p> (defaults to /etc/opendnssec/conf.xml)</p>
<dt><code>-i</code> <i>iterations</i></p>
<dd> Specify the number of <i>iterations</i> for signing an RRset. A higher number of iterations will increase the performance. </p>
<p> (defaults to 1 iteration)</p>
<dt><code>-r</code> <i>repository</i></p>
<dd> The speed test will be performed on this <i>repository</i>.</p>
<dt><code>-s</code> <i>keysize</i></p>
<dd> A temporary RSA key with the given <i>keysize</i> will be used for signing. </p>
<p> (defaults to 1024 bit)</p>
<dt><code>-t</code> <i>threads</i></p>
<dd> The number of <i>threads</i> to use. Most HSMs will be utilized better with multiple threads. </p>
<p> (defaults to 1 thread)</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ods-auditor/">ods-auditor</a>(1), <a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>ods-hsmspeed</code> was written by Jakob Schlyter and Nominet as part of the OpenDNSSEC project. </p>
<h2>Index</h2>
