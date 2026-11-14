---
title: "eapol_test(8)"
name: "eapol_test"
section: "8"
letter: "e"
url: "/docs/linux/man/8-eapol_test/"
description: "eapol_test – EAP peer and RADIUS client testing"
---

<p>eapol_test &#8211; EAP peer and RADIUS client testing</p>
<h2>Synopsis</h2>
<p><code>eapol_test</code> [ <code>-nWS</code> ] [ <code>-c</code><i>config file</i> ] [ <code>-a</code><i>server IP address</i> ] [ <code>-A</code><i>client IP address</i> ] [ <code>-p</code><i>UDP port</i> ] [ <code>-s</code><i>shared secret</i> ] [ <code>-r</code><i>re-authentications</i> ] [ <code>-t</code><i>timeout</i> ] [ <code>-C</code><i>Connect-Info</i> ] [ <code>-M</code><i>MAC address</i> ] [ <code>-o</code><i>file</i> ] [ <code>-N</code><i>attr spec</i> ] </p>
<p> <code>eapol_test scard</code> </p>
<p> <code>eapol_test sim</code> [ <code>PIN</code> ] [ <code>num triplets</code> ]</p>
<h2>Overview</h2>
<p>eapol_test is a program that links together the same EAP peer implementation that wpa_supplicant is using and the RADIUS authentication client code from hostapd. In addition, it has minimal glue code to combine these two components in similar ways to IEEE 802.1X/EAPOL Authenticator state machines. In other words, it integrates IEEE 802.1X Authenticator (normally, an access point) and IEEE 802.1X Supplicant (normally, a wireless client) together to generate a single program that can be used to test EAP methods without having to setup an access point and a wireless client. </p>
<p> The main uses for eapol_test are in interoperability testing of EAP methods against RADIUS servers and in development testing for new EAP methods. It can be easily used to automate EAP testing for interoperability and regression since the program can be run from shell scripts without require additional test components apart from a RADIUS server. For example, the automated EAP tests described in eap_testing.txt are implemented with eapol_test. Similarly, eapol_test could be used to implement an automated regression test suite for a RADIUS authentication server. </p>
<p> As an example: </p>
<dl>
<dd>
<pre>eapol_test -ctest.conf -a127.0.0.1 -p1812 -ssecret -r1</pre>
</dl>
<p> tries to complete EAP authentication based on the network configuration from test.conf against the RADIUS server running on the local host. A re-authentication is triggered to test fast re-authentication. The configuration file uses the same format for network blocks as wpa_supplicant.</p>
<h2>Command Arguments</h2>
<dl>
<dt><code>-c configuration file path</code></p>
<dd>A configuration to use. The configuration should use the same format for network blocks as wpa_supplicant.</p>
<dt><code>-a AS address</code></p>
<dd>IP address of the authentication server. The default is &#8216;127.0.0.1&#8217;.</p>
<dt><code>-A client address</code></p>
<dd>IP address of the client. The default is to select an address automatically.</p>
<dt><code>-p AS port</code></p>
<dd>UDP port of the authentication server. The default is &#8216;1812&#8217;.</p>
<dt><code>-s AS secret</code></p>
<dd>Shared secret with the authentication server. The default is &#8216;radius&#8217;.</p>
<dt><code>-r count</code></p>
<dd>Number of reauthentications.</p>
<dt><code>-t timeout</code></p>
<dd>Timeout in seconds. The default is 30.</p>
<dt><code>-C info</code></p>
<dd>RADIUS Connect-Info. The default is &#8216;CONNECT 11Mbps 802.11b&#8217;.</p>
<dt><code>-M mac address</code></p>
<dd>Client MAC address (Calling-Station-Id). The default is &#8217;02:00:00:00:00:01&#8242;.</p>
<dt><code>-o file</code></p>
<dd>Location to write out server certificate.</p>
<dt><code>-N attr spec</code></p>
<dd>Send arbitrary attribute specific by attr_id:syntax:value, or attr_id alone. attr_id should be the numeric ID of the attribute, and syntax should be one of &#8216;s&#8217; (string), &#8216;d&#8217; (integer), or &#8216;x&#8217; (octet string). The value is the attribute value to send. When attr_id is given alone, NULL is used as the attribute value. Multiple attributes can be specified by using the option several times.</p>
<dt><code>-n</code></p>
<dd>Indicates that no MPPE keys are expected.</p>
<dt><code>-W</code></p>
<dd>Wait for a control interface monitor before starting.</p>
<dt><code>-S</code></p>
<dd>Save configuration after authentication.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2016, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
