---
title: "ods-kaspcheck(1)"
name: "ods-kaspcheck"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ods-kaspcheck/"
description: "ods-kaspcheck – Performs a sanity check of the policy for OpenDNSSEC"
---

<h2>NAME</h2>
<p> <code>ods-kaspcheck</code> &#8211; Performs a sanity check of the policy for OpenDNSSEC</p>
<h2>SYNOPSIS</h2>
<p> <code>ods-kaspcheck</code> [<code>-c</code> <i>path</i> <code>-k</code> <i>path</i>]</p>
<h2>DESCRIPTION</h2>
<p> The OpenDNSSEC XML configuration files (conf.xml and kasp.xml) offer the user many options to configure the OpenDNSSEC signing system. Some syntactic constraints are placed on the configuration by the .rng definition (for example, whether an element is required or optional), but some semantic constraints cannot be defined this way (for example, if NSEC3 is used to secure the zone, then a consistent DNSKEY algorithm choice should be made). </p>
<p> ods-kaspcheck is provided to check that the configuration files (conf.xml and kasp.xml) are semantically sane and contain no inconsistencies. It is advisable to use this tool to check your configuration before starting to use OpenDNSSEC.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;conf</code> <i>path</i></p>
<dd> Path to an OpenDNSSEC configuration file </p>
<p> (defaults to /etc/opendnssec/conf.xml)</p>
<dt><code>-k</code>, <code>&#8211;kasp</code> <i>path</i></p>
<dd> Path to KASP policy file </p>
<p> (defaults to the path given in the configuration file)</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the help screen</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>ods-kaspcheck</code> was written by Alex Dalitz and Nominet as part of the OpenDNSSEC project. </p>
<h2>Index</h2>
