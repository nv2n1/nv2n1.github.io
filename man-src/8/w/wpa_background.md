---
title: "wpa_background(8)"
name: "wpa_background"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_background/"
description: "wpa_background – Background information on Wi-Fi Protected Access and IEEE 802.11i"
---

<p>wpa_background &#8211; Background information on Wi-Fi Protected Access and IEEE 802.11i</p>
<h2>Wpa</h2>
<p>The original security mechanism of IEEE 802.11 standard was not designed to be strong and has proven to be insufficient for most networks that require some kind of security. Task group I (Security) of IEEE 802.11 working group (<a rel="nofollow" href="http://www.ieee802.org/11/)">http://www.ieee802.org/11/)</a> has worked to address the flaws of the base standard and has in practice completed its work in May 2004. The IEEE 802.11i amendment to the IEEE 802.11 standard was approved in June 2004 and published in July 2004. </p>
<p> Wi-Fi Alliance (<a rel="nofollow" href="http://www.wi-fi.org/)">http://www.wi-fi.org/)</a> used a draft version of the IEEE 802.11i work (draft 3.0) to define a subset of the security enhancements that can be implemented with existing wlan hardware. This is called Wi-Fi Protected Access&lt;TM&gt; (WPA). This has now become a mandatory component of interoperability testing and certification done by Wi-Fi Alliance. Wi-Fi provides information about WPA at its web site (<a rel="nofollow" href="http://www.wi-fi.org/OpenSection/protected_access.asp">http://www.wi-fi.org/OpenSection/protected_access.asp</a>). </p>
<p> IEEE 802.11 standard defined wired equivalent privacy (WEP) algorithm for protecting wireless networks. WEP uses RC4 with 40-bit keys, 24-bit initialization vector (IV), and CRC32 to protect against packet forgery. All these choices have proven to be insufficient: key space is too small against current attacks, RC4 key scheduling is insufficient (beginning of the pseudorandom stream should be skipped), IV space is too small and IV reuse makes attacks easier, there is no replay protection, and non-keyed authentication does not protect against bit flipping packet data. </p>
<p> WPA is an intermediate solution for the security issues. It uses Temporal Key Integrity Protocol (TKIP) to replace WEP. TKIP is a compromise on strong security and possibility to use existing hardware. It still uses RC4 for the encryption like WEP, but with per-packet RC4 keys. In addition, it implements replay protection, keyed packet authentication mechanism (Michael MIC). </p>
<p> Keys can be managed using two different mechanisms. WPA can either use an external authentication server (e.g., RADIUS) and EAP just like IEEE 802.1X is using or pre-shared keys without need for additional servers. Wi-Fi calls these &quot;WPA-Enterprise&quot; and &quot;WPA-Personal&quot;, respectively. Both mechanisms will generate a master session key for the Authenticator (AP) and Supplicant (client station). </p>
<p> WPA implements a new key handshake (4-Way Handshake and Group Key Handshake) for generating and exchanging data encryption keys between the Authenticator and Supplicant. This handshake is also used to verify that both Authenticator and Supplicant know the master session key. These handshakes are identical regardless of the selected key management mechanism (only the method for generating master session key changes).</p>
<h2>Ieee 802.11I / Wpa2</h2>
<p>The design for parts of IEEE 802.11i that were not included in WPA has finished (May 2004) and this amendment to IEEE 802.11 was approved in June 2004. Wi-Fi Alliance is using the final IEEE 802.11i as a new version of WPA called WPA2. This includes, e.g., support for more robust encryption algorithm (CCMP: AES in Counter mode with CBC-MAC) to replace TKIP and optimizations for handoff (reduced number of messages in initial key handshake, pre-authentication, and PMKSA caching).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2022, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
