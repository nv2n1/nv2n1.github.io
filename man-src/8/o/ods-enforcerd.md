---
title: "ods-enforcerd(8)"
name: "ods-enforcerd"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ods-enforcerd/"
description: "ods-enforcerd – OpenDNSSEC Policy Enforcer daemon"
---

<p><code>ods-enforcerd</code> &#8211; OpenDNSSEC Policy Enforcer daemon</p>
<h2>Synopsis</h2>
<p><code>ods-enforcerd</code> [<code>-c</code> <i>FILE]</i> [<code>-d</code>] [<code>-1</code>] [<code>-p</code> <i>POLICY]</i> [<code>-P</code> <i>PIDFILE</i>] [<code>-v</code>] [<code>-h</code>]</p>
<h2>Description</h2>
<p>ods-enforcerd is part of the OpenDNSSEC software. It will enforce any policies that you have set up for zones under the control of OpenDNSSEC (including the generation of keys if configured to). For more information, go to <code><a rel="nofollow" href="http://www.opendnssec.org">http://www.opendnssec.org</a></code> and visit the Documentation page. Invoked with no arguments, ods-enforcerd will read the default configuration file /etc/opendnssec/conf.xml and act according to its contents. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> FILE</i></p>
<dd>Use alternate conf.xml.</p>
<dt><code>-d</code></p>
<dd>Run in debug mode.</p>
<dt><code>-1</code></p>
<dd>Run once, then exit.</p>
<dt><code>-p</code><i> POLICY</i></p>
<dd>Run once processing only the specified policy, then exit.</p>
<dt><code>-P</code><i> PIDFILE</i></p>
<dd>Use alternate process-id file.</p>
<dt><code>-v</code></p>
<dd>Print the version, then exit.</p>
<dt><code>-h</code></p>
<dd>Show help, then exit.</dl>
<h2>Signals</h2>
<dl>
<dt>The ods-enforcerd can be controlled using the ods-control utility. Signals may also be used.</p>
<dd>
<dt>SIGHUP</p>
<dd>ods-enforcerd runs on a schedule defined in conf.xml; this signal will interrupt that and force the daemon to wake up.</p>
<dt>SIGINT, SIGTERM</p>
<dd>Force the daemon to stop (if it is running it will finish what it is doing first).</dl>
<h2>Configuration</h2>
<p>The configuration of ods-enforcerd is contained in the conf.xml file; the options available are described in the OpenDNSSEC documentation.</p>
<h2>Diagnostics</h2>
<p>will log all the problems via the standard <a href="/docs/linux/man/8-syslog/">syslog</a>(8) <i>daemon</i> facility.</p>
<h2>Files</h2>
<dl>
<dt>/etc/opendnssec/conf.xml</p>
<dd>default configuration file.</p>
<dt>/var/run/opendnssec/zone_fetcher.pid</p>
<dd>default process-id file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>Authors</h2>
<p><code>ods-enforcerd</code> was written by John Dickinson and Nominet as part of the OpenDNSSEC project.</p>
