---
title: "strongswan_charon-cmd(8)"
name: "strongswan_charon-cmd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-strongswan_charon-cmd/"
description: "charon-cmd – Simple IKE client (IPsec VPN client)"
---

<p>charon-cmd &#8211; Simple IKE client (IPsec VPN client)</p>
<h2>Synopsis</h2>
<p><code>charon-cmd</code> <code>&#8211;host</code> <i>hostname</i> <code>&#8211;identity</code> <i>identity</i> <code>[ options ]</code> </p>
<h2>Description</h2>
<p><code>charon-cmd</code> is a program for setting up IPsec VPN connections using the Internet Key Exchange protocol (IKE) in version 1 and 2. It supports a number of different road-warrior scenarios. Like the IKE daemon <code>charon</code>, <code>charon-cmd</code> has to be run as <code>root</code> (or more specifically as a user with <code>CAP_NET_ADMIN</code> capability). Of the following options at least <i>&#8211;host</i> and <i>&#8211;identity</i> are required. Depending on the selected authentication <i>profile</i> credentials also have to be provided with their respective options. Many of the <code>charon</code>-specific configuration options in <i>strongswan.conf</i> also apply to <code>charon-cmd</code>. For instance, to configure customized logging to <code>stdout</code> the following snippet can be used: </p>
<pre><code>charon-cmd {
    filelog {
        stdout {
            default = 1
            ike = 2
            cfg = 2
        }
    }
}
</code></pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Prints usage information and a short summary of the available options.</p>
<dt><code>&#8211;version</code></p>
<dd>Prints the strongSwan version.</p>
<dt><code>&#8211;debug </code><i>level</i></p>
<dd>Sets the default log level (defaults to 1). <i>level</i> is a number between -1 and 4. Refer to <i>strongswan.conf</i> for options that allow a more fine-grained configuration of the logging output.</p>
<dt><code>&#8211;host </code><i>hostname</i></p>
<dd>DNS name or IP address to connect to.</p>
<dt><code>&#8211;identity </code><i>identity</i></p>
<dd>Identity the client uses for the IKE exchange.</p>
<dt><code>&#8211;eap-identity </code><i>identity</i></p>
<dd>Identity the client uses for EAP authentication.</p>
<dt><code>&#8211;xauth-username </code><i>username</i></p>
<dd>Username the client uses for XAuth authentication.</p>
<dt><code>&#8211;remote-identity </code><i>identity</i></p>
<dd>Server identity to expect, defaults to <i>hostname</i>.</p>
<dt><code>&#8211;cert </code><i>path</i></p>
<dd>Trusted certificate, either for authentication or trust chain validation. To provide more than one certificate multiple <code>&#8211;cert</code> options can be used.</p>
<dt><code>&#8211;rsa </code><i>path</i></p>
<dd>RSA private key to use for authentication (if a password is required, it will be requested on demand).</p>
<dt><code>&#8211;p12 </code><i>path</i></p>
<dd>PKCS#12 file with private key and certificates to use for authentication and trust chain validation (if a password is required it will be requested on demand).</p>
<dt><code>&#8211;agent</code>[=<i>socket</i>]</p>
<dd>Use SSH agent for authentication. If <i>socket</i> is not specified it is read from the <code>SSH_AUTH_SOCK</code> environment variable.</p>
<dt><code>&#8211;local-ts </code><i>subnet</i></p>
<dd>Additional traffic selector to propose for our side, the requested virtual IP address will always be proposed.</p>
<dt><code>&#8211;remote-ts </code><i>subnet</i></p>
<dd>Traffic selector to propose for remote side, defaults to 0.0.0.0/0.</p>
<dt><code>&#8211;ike-proposal </code><i>proposal</i></p>
<dd>IKE proposal to offer instead of default. For IKEv1, a single proposal consists of one encryption algorithm, an integrity/PRF algorithm and a DH group. IKEv2 can propose multiple algorithms of the same kind. To specify multiple proposals, repeat the option.</p>
<dt><code>&#8211;esp-proposal </code><i>proposal</i></p>
<dd>ESP proposal to offer instead of default. For IKEv1, a single proposal consists of one encryption algorithm, an integrity algorithm and an optional DH group for Perfect Forward Secrecy rekeying. IKEv2 can propose multiple algorithms of the same kind. To specify multiple proposals, repeat the option.</p>
<dt><code>&#8211;ah-proposal </code><i>proposal</i></p>
<dd>AH proposal to offer instead of ESP. For IKEv1, a single proposal consists of an integrity algorithm and an optional DH group for Perfect Forward Secrecy rekeying. IKEv2 can propose multiple algorithms of the same kind. To specify multiple proposals, repeat the option.</p>
<dt><code>&#8211;profile </code><i>name</i></p>
<dd>Authentication profile to use, the list of supported profiles can be found in the <code>Authentication Profiles</code> sections below. Defaults to <code>ikev2-pub</code> if a private key was supplied, and to <code>ikev2-eap</code> otherwise.</dl>
<h3>IKEv2 Authentication Profiles</h3>
<dl>
<dt><code>ikev2-pub</code></p>
<dd>IKEv2 with public key client and server authentication</p>
<dt><code>ikev2-eap</code></p>
<dd>IKEv2 with EAP client authentication and public key server authentication</p>
<dt><code>ikev2-pub-eap</code></p>
<dd>IKEv2 with public key and EAP client authentication (RFC 4739) and public key server authentication</dl>
<h3>IKEv1 Authentication Profiles</h3>
<p>The following authentication profiles use either Main Mode or Aggressive Mode, the latter is denoted with a <code>-am</code> suffix.</p>
<dl>
<dt><code>ikev1-pub</code>, <code>ikev1-pub-am</code></p>
<dd>IKEv1 with public key client and server authentication</p>
<dt><code>ikev1-xauth</code>, <code>ikev1-xauth-am</code></p>
<dd>IKEv1 with public key client and server authentication, followed by client XAuth authentication</p>
<dt><code>ikev1-xauth-psk</code>, <code>ikev1-xauth-psk-am</code></p>
<dd>IKEv1 with pre-shared key (PSK) client and server authentication, followed by client XAuth authentication (INSECURE!)</p>
<dt><code>ikev1-hybrid</code>, <code>ikev1-hybrid-am</code></p>
<dd>IKEv1 with public key server authentication only, followed by client XAuth authentication</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8) </p>
