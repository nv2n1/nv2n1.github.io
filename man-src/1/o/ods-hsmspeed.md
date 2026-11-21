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
<p> <code>ods-hsmspeed</code> [<code>-c</code> <i>config</i>] <code>-r</code> <i>repository</i> [<code>-i</code> <i>iterations</i>] [<code>-s</code> <i>keysize</i>] [<code>-t</code> <i>threads</i>]</p>
<p> The ods-hsmspeed utility is part of OpenDNSSEC and can be used to test the performance of the configured HSMs. </p>
<p> The components of OpenDNSSEC do not talk directly to the HSMs, but uses an internal library called libhsm. It then talks to the HSMs using PKCS#11. The libhsm simplifies the process of creating keys and signatures for the other components of OpenDNSSEC. </p>
<p> ods-hsmspeed will measure the speed by using the libhsm. The result that you get is somewhat lower than what the manufactures promises, because the libhsm creates some overhead to the pure PKCS#11 environment.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>config</i></dt>
<dd> Path to an OpenDNSSEC configuration file. </dd>
<p> (defaults to /etc/opendnssec/conf.xml)</p>
<dt><code>-i</code> <i>iterations</i></dt>
<dd> Specify the number of <i>iterations</i> for signing an RRset. A higher number of iterations will increase the performance. </dd>
<p> (defaults to 1 iteration)</p>
<dt><code>-r</code> <i>repository</i></dt>
<dd> The speed test will be performed on this <i>repository</i>.</dd>
<dt><code>-s</code> <i>keysize</i></dt>
<dd> A temporary RSA key with the given <i>keysize</i> will be used for signing. </dd>
<p> (defaults to 1024 bit)</p>
<dt><code>-t</code> <i>threads</i></dt>
<dd> The number of <i>threads</i> to use. Most HSMs will be utilized better with multiple threads. </dd>
<p> (defaults to 1 thread)</dl>
<h2>SEE ALSO</h2>
<p> ods-auditor(1), <a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>ods-hsmspeed</code> was written by Jakob Schlyter and Nominet as part of the OpenDNSSEC project. </p>
