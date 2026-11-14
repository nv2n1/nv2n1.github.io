---
title: "monkeysphere(7)"
name: "monkeysphere"
section: "7"
letter: "m"
url: "/docs/linux/man/7-monkeysphere/"
description: "monkeysphere – ssh and TLS authentication framework using OpenPGP Web of Trust"
---

<p>monkeysphere &#8211; ssh and TLS authentication framework using OpenPGP Web of Trust</p>
<h2>Description</h2>
<p><code>Monkeysphere</code> is a framework to leverage the OpenPGP web of trust for OpenSSH and TLS key-based authentication. OpenPGP keys are tracked via GnuPG, and added to the authorized_keys and known_hosts files used by OpenSSH for connection authentication. Monkeysphere can also be used by a validation agent to validate TLS connections (e.g. https). </p>
<h2>Identity Certifiers</h2>
<p>Each host that uses the <code>Monkeysphere</code> to authenticate its remote users needs some way to determine that those users are who they claim to be. SSH permits key-based authentication, but we want instead to bind authenticators to human-comprehensible user identities. This switch from raw keys to User IDs makes it possible for administrators to see intuitively who has access to an account, and it also enables end users to transition keys (and revoke compromised ones) automatically across all <code>Monkeysphere</code>-enabled hosts. The User IDs and certifications that the <code>Monkeysphere</code> relies on are found in the OpenPGP Web of Trust. </p>
<p> However, in order to establish this binding, each host must know whose cerifications to trust. Someone who a host trusts to certify User Identities is called an Identity Certifier. A host must have at least one Identity Certifier in order to bind User IDs to keys. Commonly, every ID Certifier would be trusted by the host to fully identify any User ID, but more nuanced approaches are possible as well. For example, a given host could specify a dozen ID certifiers, but assign them all &quot;marginal&quot; trust. Then any given User ID would need to be certified in the OpenPGP Web of Trust by at least three of those certifiers. </p>
<p> It is also possible to limit the scope of trust for a given ID Certifier to a particular domain. That is, a host can be configured to fully (or marginally) trust a particular ID Certifier only when they certify identities within, say, example.org (based on the e-mail address in the User ID).</p>
<h2>Key Acceptability</h2>
<p>The monkeysphere commands work from a set of user IDs to determine acceptable keys for ssh and TLS authentication. OpenPGP keys are considered acceptable if the following criteria are met:</p>
<dl>
<dt><code>capability</code></p>
<dd>The key must have the `authentication&#8217; (`a&#8217;) usage flag set.</p>
<dt><code>validity</code></p>
<dd>The key itself must be valid, i.e. it must be well-formed, not expired, and not revoked.</p>
<dt><code>certification</code></p>
<dd>The relevant user ID must be signed by a trusted identity certifier. </p>
</dl>
<h2>Host Identification</h2>
<p>The OpenPGP keys for hosts have associated `service names` (OpenPGP user IDs) that are based on URI specifications for the service. Some examples:</p>
<dl>
<dt><code>ssh:</code></p>
<dd><a href="ssh://host.example.com[:port]">ssh://host.example.com[:port]</a></p>
<dt><code>https:</code></p>
<dd><a rel="nofollow" href="https://host.example.com[:port]">https://host.example.com[:port]</a> </p>
</dl>
<h2>Author</h2>
<p>Written by: Jameson Rollins &lt;jrollins [at] finestructure.net&gt;, Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-monkeysphere/">monkeysphere</a></code>(1), <code><a href="/docs/linux/man/8-monkeysphere-host/">monkeysphere-host</a></code>(8), <code><a href="/docs/linux/man/8-monkeysphere-authentication/">monkeysphere-authentication</a></code>(8), <code><a href="/docs/linux/man/1-openpgp2ssh/">openpgp2ssh</a></code>(1), <code><a href="/docs/linux/man/1-pem2openpgp/">pem2openpgp</a></code>(1), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a rel="nofollow" href="http://tools.ietf.org/html/rfc4880,">http://tools.ietf.org/html/rfc4880,</a></code> <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a rel="nofollow" href="http://tools.ietf.org/wg/secsh/draft-ietf-secsh-scp-sftp-ssh-uri/">http://tools.ietf.org/wg/secsh/draft-ietf-secsh-scp-sftp-ssh-uri/</a></code> </p>
