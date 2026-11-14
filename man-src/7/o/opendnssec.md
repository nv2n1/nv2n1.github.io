---
title: "opendnssec(7)"
name: "opendnssec"
section: "7"
letter: "o"
url: "/docs/linux/man/7-opendnssec/"
description: "OpenDNSSEC – making DNSSEC easy for DNS administrators"
---

<p><code>OpenDNSSEC</code> &#8211; making DNSSEC easy for DNS administrators</p>
<h2>Synopsis</h2>
<p><code>ods-control start</code> </p>
<p> <code>ods-control stop</code> </p>
<p> <code>ods-ksmutil</code> <i>subcommand&#8230;</i> </p>
<p> <code>ods-signer</code> [<i>subcommand&#8230;</i><code>]</code></p>
<h2>Description</h2>
<p>OpenDNSSEC is a complete DNSSEC zone signing system which maintains stability and security of signed domains. DNSSEC adds many cryptographic concerns to DNS; OpenDNSSEC automates those to allow current DNS administrators to adopt DNSSEC. </p>
<p> Domain signing is done by placing OpenDNSSEC between the place where the zone files are edited and where they are published. The current version of OpenDNSSEC supports files and AXFR to communicate the zone data; effectively, OpenDNSSEC acts as a &quot;bump in the wire&quot; between editing and publishing a zone. </p>
<p> OpenDNSSEC has two daemons, which are unitedly started and stopped through the <i><a href="/docs/linux/man/8-ods-control/">ods-control</a>(8)</i> command. The two daemons in turn invoke other programs to get their work done. </p>
<p> One of the daemons is the KASP Enforcer, which enforces policies that define security and timing requirements for each individual zone. Operators tend to interact with the KASP Enforcer a lot, through the <i><a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1)</i> command. </p>
<p> The other daemon is the Signer Engine, which in turn signs the zone content. It retrieves that content from a file or through AXFR, and publishes a signed version of the zone into a file or through AXFR. Direct interaction with the Signer Engine, although not normally necessary, is possible through the <i><a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8)</i> command. </p>
<p> The keys that sign the zones are managed by an independent repository, which is accessed over a PKCS #11 interface. The principle idea of this interface being to unleash access to cryptographic hardware, there are implementations in software. Also, implementations range from open to commercial, and from very simple to highly secure. By default, OpenDNSSEC is configured to run on top of a SoftHSM, but a few other commands exist to test any Hardware Security Module that may sit under the PKCS #11 API.</p>
<h2>Operational Practices</h2>
<p>The approach used by OpenDNSSEC follows the best current practice of two kinds of key per zone:</p>
<dl>
<dt><code>KSK</code> or <code>Key Signing Key</code></p>
<dd>This key belongs in the apex of a zone, and is referenced in the parent zone (quite possibly a registry) in the form of DS records alongside NS records. These parent references function as trust delegations. </p>
<p> The KSK is usually a longer key, and it could harm the efficiency of secure resolvers if all individual resource records were signed with it. This is why it is advisable to use the KSK only to sign the ZSK. </p>
<p> In DNS records, the KSK can usually be recognised by having its SEP (Secure Entry Point) flag set.</p>
<dt><code>ZSK</code> or <code>Zone Signing Key</code></p>
<dd>This key also belongs in the apex of a zone, and is actually used to sign the resource records in a zone. It is a shorter key for reasons of efficiency, that is rolled over on a fairly regular basis. To detach these rollovers from the parent, the ZSK is not directly trusted by the parent zone, but instead its trust is established by way of a signature by the KSK on the ZSK.</dl>
<p> OpenDNSSEC is mindful about the period of validity of each key, and will rollover in time to keep the domain signed, with new keys, without any downtime for the secure domain. The only thing that is not standardised, and thus cannot be automated at the moment is the interface between a zone and its parent, so this has to be done manually, or scripted around OpenDNSSEC.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>Authors</h2>
<p><code>OpenDNSSEC</code> was made by the OpenDNSSEC project, to be found on <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
