---
title: "strongswan_ipsec-secrets(5)"
name: "strongswan_ipsec-secrets"
section: "5"
letter: "s"
url: "/docs/linux/man/5-strongswan_ipsec-secrets/"
description: "ipsec.secrets – secrets for IKE/IPsec authentication"
---

<p>ipsec.secrets &#8211; secrets for IKE/IPsec authentication</p>
<h2>Description</h2>
<p>The file <i>ipsec.secrets</i> holds a table of secrets. These secrets are used by the strongSwan Internet Key Exchange (IKE) daemons pluto (IKEv1) and charon (IKEv2) to authenticate other hosts. It is vital that these secrets be protected. The file should be owned by the super-user, and its permissions should be set to block all access by others. The file is a sequence of entries and include directives. Here is an example.</p>
<dl>
<dd>
<pre># /etc/ipsec.secrets - strongSwan IPsec secrets file
192.168.0.1 %any : PSK &quot;v+NkxY9LLZvwj4qCC2o/gGrWDF2d21jL&quot;
: RSA moonKey.pem
alice [at] strongswan.org : EAP &quot;x3.dEhgN&quot;
carol : XAUTH &quot;4iChxLT3&quot;
dave : XAUTH &quot;ryftzG4A&quot;
# get secrets from other files
include ipsec.*.secrets</pre>
</dl>
<p> Each entry in the file is a list of optional ID selectors, followed by a secret. The two parts are separated by a colon (<code>:</code>) that is surrounded by whitespace. If no ID selectors are specified the line must start with a colon. A selector is an IP address, a Fully Qualified Domain Name, user [at] FQDN, <code>%any</code> or <code>%any6</code> (other kinds may come). Matching IDs with selectors is fairly straightforward: they have to be equal. In the case of a &#8220;Road Warrior&#8221; connection, if an equal match is not found for the Peer&#8217;s ID, and it is in the form of an IP address, a selector of <code>%any</code> will match the peer&#8217;s IP address if IPV4 and <code>%any6</code> will match a the peer&#8217;s IP address if IPV6. Currently, the obsolete notation <code>0.0.0.0</code> may be used in place of <code>%any</code>. In IKEv1 an additional complexity arises in the case of authentication by preshared secret: the responder will need to look up the secret before the Peer&#8217;s ID payload has been decoded, so the ID used will be the IP address. To authenticate a connection between two hosts, the entry that most specifically matches the host and peer IDs is used. An entry with no selectors will match any host and peer. More specifically, an entry with one selector will match a host and peer if the selector matches the host&#8217;s ID (the peer isn&#8217;t considered). Still more specifically, an entry with multiple selectors will match a host and peer if the host ID and peer ID each match one of the selectors. If the key is for an asymmetric authentication technique (i.e. a public key system such as RSA), an entry with multiple selectors will match a host and peer even if only the host ID matches a selector (it is presumed that the selectors are all identities of the host). It is acceptable for two entries to be the best match as long as they agree about the secret or private key. Authentication by preshared secret requires that both systems find the identical secret (the secret is not actually transmitted by the IKE protocol). If both the host and peer appear in the selector list, the same entry will be suitable for both systems so verbatim copying between systems can be used. This naturally extends to larger groups sharing the same secret. Thus multiple-selector entries are best for PSK authentication. Authentication by public key systems such as RSA requires that each host have its own private key. A host could reasonably use a different private keys for different interfaces and for different peers. But it would not be normal to share entries between systems. Thus thus no-selector and one-selector forms of entry often make sense for public key authentication. The key part of an entry must start with a token indicating the kind of key. The following types of secrets are currently supported:</p>
<dl>
<dt><code>PSK</code></p>
<dd>defines a pre-shared key</p>
<dt><code>RSA</code></p>
<dd>defines an RSA private key</p>
<dt><code>ECDSA</code></p>
<dd>defines an ECDSA private key</p>
<dt><code>P12</code></p>
<dd>defines a PKCS#12 container</p>
<dt><code>EAP</code></p>
<dd>defines EAP credentials</p>
<dt><code>NTLM</code></p>
<dd>defines NTLM credentials</p>
<dt><code>XAUTH</code></p>
<dd>defines XAUTH credentials</p>
<dt><code>PIN</code></p>
<dd>defines a smartcard PIN</dl>
<p> Details on each type of secret are given below. Whitespace at the end of a line is ignored. At the start of a line or after whitespace, <code>#</code> and the following text up to the end of the line is treated as a comment. An include directive causes the contents of the named file to be processed before continuing with the current file. The filename is subject to &#8220;globbing&#8221; as in <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), so every file with a matching name is processed. Includes may be nested to a modest depth (10, currently). If the filename doesn&#8217;t start with a <code>/</code>, the directory containing the current file is prepended to the name. The include directive is a line that starts with the word <code>include</code>, followed by whitespace, followed by the filename (which must not contain whitespace).</p>
<h3>Types Of Secrets</h3>
<dl>
<dt><code>[ &lt;selectors&gt; ] : PSK &lt;secret&gt;</code></p>
<dd>A preshared <i>secret</i> is most conveniently represented as a sequence of characters, which is delimited by double-quote characters (<code>&quot;</code>). The sequence cannot contain newline or double-quote characters.<br />
 Alternatively, preshared secrets can be represented as hexadecimal or Base64 encoded binary values. A character sequence beginning with <code>0x</code> is interpreted as sequence of hexadecimal digits. Similarly, a character sequence beginning with <code>0s</code> is interpreted as Base64 encoded binary data.</p>
<dt><code>: RSA &lt;private key file&gt; [ &lt;passphrase&gt; | %prompt ]</code></p>
<dd><code>: ECDSA &lt;private key file&gt; [ &lt;passphrase&gt; | %prompt ]</code> For the private key file both absolute paths or paths relative to <i>/etc/ipsec.d/private</i> are accepted. If the private key file is encrypted, the <i>passphrase</i> must be defined. Instead of a passphrase <code>%prompt</code> can be used which then causes the daemon to ask the user for the password whenever it is required to decrypt the key.</p>
<dt><code>: P12 &lt;PKCS#12 file&gt; [ &lt;passphrase&gt; | %prompt ]</code></p>
<dd>For the PKCS#12 file both absolute paths or paths relative to <i>/etc/ipsec.d/private</i> are accepted. If the container is encrypted, the <i>passphrase</i> must be defined. Instead of a passphrase <code>%prompt</code> can be used which then causes the daemon to ask the user for the password whenever it is required to decrypt the container. Private keys, client and CA certificates are extracted from the container. To use such a client certificate in a connection set leftid to one of the subjects of the certificate.</p>
<dt><code>&lt;user id&gt; : EAP &lt;secret&gt;</code></p>
<dd>The format of <i>secret</i> is the same as that of <code>PSK</code> secrets.<br />
 <code>EAP</code> secrets are IKEv2 only.</p>
<dt><code>&lt;user id&gt; : NTLM &lt;secret&gt;</code></p>
<dd>The format of <i>secret</i> is the same as that of <code>PSK</code> secrets, but the secret is stored as NTLM hash, which is MD4(UTF-16LE(secret)), instead of as cleartext.<br />
 <code>NTLM</code> secrets can only be used with the <code>eap-mschapv2</code> plugin.</p>
<dt><code>[ &lt;servername&gt; ] &lt;username&gt; : XAUTH &lt;password&gt;</code></p>
<dd>The format of <i>password</i> is the same as that of <code>PSK</code> secrets. <code>XAUTH</code> secrets are IKEv1 only.</p>
<dt><code>: PIN %smartcard[&lt;slot nr&gt;[@&lt;module&gt;]]:&lt;keyid&gt; &lt;pin code&gt; | %prompt</code></p>
<dd>The smartcard selector always requires a keyid to uniquely select the correct key. The slot number defines the slot on the token, the module name refers to the module name defined in <a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a>(5). Instead of specifying the pin code statically, <code>%prompt</code> can be specified, which causes the daemon to ask the user for the pin code.</dl>
<h2>Files</h2>
<p>/etc/ipsec.secrets</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a>(5), <a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a>(5), <a href="/docs/linux/man/8-ipsec/">ipsec</a>(8)</p>
<h2>History</h2>
<p>Originally written for the FreeS/WAN project by D. Hugh Redelmeier. Updated and extended for the strongSwan project &lt;<a rel="nofollow" href="http://www.strongswan.org">http://www.strongswan.org</a>&gt; by Tobias Brunner and Andreas Steffen.</p>
<h2>Bugs</h2>
<p>If an ID is <code>0.0.0.0</code>, it will match <code>%any</code>; if it is <code>0::0</code>, it will match <code>%any6</code>. </p>
