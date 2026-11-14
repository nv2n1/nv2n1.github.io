---
title: "monkeysphere-host(8)"
name: "monkeysphere-host"
section: "8"
letter: "m"
url: "/docs/linux/man/8-monkeysphere-host/"
description: "monkeysphere-host – Monkeysphere host key administration tool."
---

<p>monkeysphere-host &#8211; Monkeysphere host key administration tool.</p>
<h2>Synopsis</h2>
<p><code>monkeysphere-host </code><i>subcommand</i> [<i>args</i>] </p>
<h2>Description</h2>
<p><code>Monkeysphere</code> is a framework to leverage the OpenPGP web of trust for SSH and TLS key-based authentication. <code>monkeysphere-host</code> stores and manages OpenPGP certificates for various services offered by the host. Most subcommands take a KEYID argument, which identifies (by OpenPGP key ID (e.g. 0xDEADBEEF) or full OpenPGP fingerprint) which certificate is to be operated upon. If only one certificate is currently managed by <code>monkeysphere-host</code>, the KEYID argument may be omitted, and <code>monkeysphere-host</code> will operate on it. </p>
<h2>Subcommands</h2>
<p><code>monkeysphere-host</code> takes various subcommands:</p>
<dl>
<dt><code>import-key FILE SCHEME://HOSTNAME[:PORT]</code></p>
<dd>Import a PEM-encoded host secret key from file FILE. If FILE is `-&#8216;, then the key will be imported from stdin. Only RSA keys are supported at the moment. SCHEME://HOSTNAME[:PORT] is used to specify the scheme (e.g. ssh or https), fully-qualified hostname (and port) used in the user ID of the new OpenPGP key (e.g. <a href="ssh://example.net">ssh://example.net</a> or <a rel="nofollow" href="https://www.example.net">https://www.example.net</a>). If PORT is not specified, then no port is added to the user ID, which means the default port for that service (e.g. 22 for ssh) is assumed. `i&#8217; may be used in place of `import-key&#8217;.</p>
<dt><code>show-keys [KEYID &#8230;]</code></p>
<dd>Output information about the OpenPGP certificate(s) for services offered by the host, including their KEYIDs. If no KEYID is specified (or if the special string `&#8211;all&#8217; is used), output information about all certificates managed by <code>monkeysphere-host</code>. `s&#8217; may be used in place of `show-keys&#8217;.</p>
<dt><code>set-expire EXPIRE [KEYID]</code></p>
<dd>Extend the validity of the OpenPGP certificate specified until EXPIRE from the present. Expiration is specified as with GnuPG (measured from today&#8217;s date): </p>
<pre> 0 = key does not expire
 &lt;n&gt; = key expires in n days
 &lt;n&gt;w = key expires in n weeks
 &lt;n&gt;m = key expires in n months
 &lt;n&gt;y = key expires in n years</pre>
<p>`e&#8217; may be used in place of `set-expire&#8217;.</p>
<dt><code>add-servicename SCHEME://HOSTNAME[:PORT] [KEYID]</code></p>
<dd>Add a service-specific user ID to the specified certificate. For example, the operator of `<a rel="nofollow" href="https://example.net'">https://example.net&#8217;</a> may wish to add an additional servicename of `<a rel="nofollow" href="https://www.example.net'">https://www.example.net&#8217;</a> to the certificate corresponding to the secret key used by the TLS-enabled web server. `add-name&#8217; or `n+&#8217; may be used in place of `add-servicename&#8217;.</p>
<dt><code>revoke-servicename SCHEME://HOSTNAME[:PORT] [KEYID]</code></p>
<dd>Revoke a service-specific user ID from the specified certificate. `revoke-name&#8217; or `n-&#8216; may be used in place of `revoke-servicename&#8217;.</p>
<dt><code>add-revoker REVOKER_KEYID|FILE [KEYID]</code></p>
<dd>Add a revoker to the specified OpenPGP certificate. The revoker can be specified by their own REVOKER_KEYID (in which case it will be loaded from an OpenPGP keyserver), or by specifying a path to a file containing the revoker&#8217;s OpenPGP certificate, or by specifying `-&#8216; to load from stdin. `r+&#8217; may be be used in place of `add-revoker&#8217;.</p>
<dt><code>revoke-key [KEYID]</code></p>
<dd>Generate (with the option to publish) a revocation certificate for given OpenPGP certificate. If such a certificate is published, the given key will be permanently revoked, and will no longer be accepted by monkeysphere-enabled clients. This subcommand will ask you a series of questions, and then generate a key revocation certificate, sending it to stdout. You might want to store these certificates safely offline, to publish in case of compromise). If you explicitly tell it to publish the revocation certificate immediately, it will send it to the public keyservers. PUBLISH THESE CERTIFICATES ONLY IF YOU ARE SURE THE CORRESPONDING KEY WILL NEVER BE RE-USED!</p>
<dt><code>publish-keys [KEYID &#8230;]</code></p>
<dd>Publish the specified OpenPGP certificates to the public keyservers. If the special string `&#8211;all&#8217; is specified, all of the host&#8217;s OpenPGP certificates will be published. `p&#8217; may be used in place of `publish-keys&#8217;. NOTE: that there is no way to remove a key from the public keyservers once it is published!</p>
<dt><code>version</code></p>
<dd>Show the monkeysphere version number. `v&#8217; may be used in place of `version&#8217;.</p>
<dt><code>help</code></p>
<dd>Output a brief usage summary. `h&#8217; or `?&#8217; may be used in place of `help&#8217;.</p>
<dt><code>diagnostics</code></p>
<dd>Review the state of the monkeysphere server host key and report on suggested changes. Among other checks, this includes making sure there is a valid host key, that the key is not expired, that the sshd configuration points to the right place, etc. `d&#8217; may be used in place of `diagnostics&#8217;. </p>
</dl>
<h2>Setup Ssh Server Certificates</h2>
<p>To enable users to verify your SSH host&#8217;s key via the monkeysphere, an OpenPGP certificate must be made out of the host&#8217;s RSA ssh key, and the certificate must be published to the Web of Trust. Certificate publication is not done by default. The first step is to import the host&#8217;s ssh key into a monkeysphere-style OpenPGP certificate. This is done with the import-key command. For example: </p>
<p> # monkeysphere-host import-key /etc/ssh/ssh_host_rsa_key <a href="ssh://host.example.org">ssh://host.example.org</a> </p>
<p> On most systems, sshd&#8217;s RSA secret key is stored at /etc/ssh/ssh_host_rsa_key. </p>
<p> See PUBLISHING AND CERTIFYING MONKEYSPHERE SERVICE CERTIFICATES for how to make sure your users can verify the ssh service offered by your host once the key is imported into <code>monkeysphere-host</code>.</p>
<h2>Setup Web Server Certificates</h2>
<p>You can set up your HTTPS-capable web server so that your users can verify it via the monkeysphere, without changing your server&#8217;s software at all. You just need access to a (PEM-encoded) version of the server&#8217;s RSA secret key (most secret keys are already stored PEM-encoded). The first step is to import the web server&#8217;s key into a monkeysphere-style OpenPGP certificate. This is done with the import-key command. For example: </p>
<p> # monkeysphere-host import-key /etc/ssl/private/host.example.net-key.pem <a rel="nofollow" href="https://host.example.net">https://host.example.net</a> </p>
<p> If you don&#8217;t know where the web server&#8217;s key is stored on your machine, consult the configuration files for your web server. Debian-based systems using the `ssl-cert&#8217; packages often have a default self-signed certificate stored in `/etc/ssl/private/ssl-cert-snakeoil.key&#8217; ; if you&#8217;re using that key, your users are getting browser warnings about it. You can keep using the same key, but help them use the OpenPGP WoT to verify that it does belong to your web server by using something like: </p>
<p> # monkeysphere-host import-key /etc/ssl/private/ssl-cert-snakeoil.key <a rel="nofollow" href="https://$(hostname">https://$(hostname</a> &#8211;fqdn) </p>
<p> If you offer multiple HTTPS websites using the same secret key, you should add the additional website names with the `add-servicename&#8217; subcommand. </p>
<p> See PUBLISHING AND CERTIFYING MONKEYSPHERE SERVICE CERTIFICATES (the next section) for how to make sure your users can verify the https service offered by your host once the key is imported and any extra site names have been added. Note that you can add or remove additional servicenames at any time, but you&#8217;ll need to certify any new ones separately.</p>
<h2>Publishing And Certifying Monkeysphere Service Certificates</h2>
<p>Once the host key has been imported, the corresponding certificate must be published to the Web of Trust so that users can retrieve the cert when connecting to the host. The host certificates are published to the keyserver with the publish-key command: </p>
<p> $ monkeysphere-host publish-key &#8211;all </p>
<p> In order for users accessing the system to be able to identify the host&#8217;s service via the monkeysphere, at least one person (e.g. a server admin) will need to sign the host&#8217;s certificate. This is done using standard OpenPGP keysigning techniques. Usually: pull the host&#8217;s OpenPGP certificate from the keyserver, verify and sign it, and then re-publish your signature. More than one person can certify any certificate. Please see <a rel="nofollow" href="http://web.monkeysphere.info/doc/host-keys/">http://web.monkeysphere.info/doc/host-keys/</a> for more information and details. Once an admin&#8217;s signature is published, users accessing the host can use the certificate to validate the host&#8217;s key without having to manually check the host key&#8217;s fingerprint (in the case of ssh) or without seeing a nasty &quot;security warning&quot; in their browsers (in the case of https).</p>
<h2>Security Considerations</h2>
<p>Note that <code>monkeysphere-host</code> currently caches a copy of all imported secret keys (stored in OpenPGP form for future manipulation) in /var/lib/monkeysphere/host/secring.gpg. Cleartext backups of this file could expose secret key material if not handled sensitively.</p>
<h2>Environment</h2>
<p>The following environment variables will override those specified in the config file (defaults in parentheses):</p>
<dl>
<dt>MONKEYSPHERE_LOG_LEVEL</p>
<dd>Set the log level. Can be SILENT, ERROR, INFO, VERBOSE, DEBUG, in increasing order of verbosity. (INFO)</p>
<dt>MONKEYSPHERE_KEYSERVER</p>
<dd>OpenPGP keyserver to use. (pool.sks-keyservers.net)</p>
<dt>MONKEYSPHERE_PROMPT</p>
<dd>If set to `false&#8217;, never prompt the user for confirmation. (true) </p>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/monkeysphere/monkeysphere-host.conf</p>
<dd>System monkeysphere-host config file.</p>
<dt>/var/lib/monkeysphere/host_keys.pub.pgp</p>
<dd>A world-readable copy of the host&#8217;s OpenPGP certificates in ASCII armored format. This includes the certificates (including the public keys, servicename-based User IDs, and most recent relevant self-signatures) corresponding to every key used by Monkeysphere-enabled services on the host.</p>
<dt>/var/lib/monkeysphere/host/</p>
<dd>A locked directory (readable only by the superuser) containing copies of all imported secret keys (this is the host&#8217;s GNUPGHOME directory).</p>
<dt>/etc/monkeysphere/monkeysphere-host-x509-anchors.crt or<br />
 /etc/monkeysphere/monkeysphere-x509-anchors.crt</p>
<dd>If monkeysphere-host is configured to query an hkps keyserver for publish-keys, it will use the PEM-encoded X.509 Certificate Authority certificates in this file to validate any X.509 certificates used by the keyserver. If the monkeysphere-host-x509 file is present, the monkeysphere-x509 file will be ignored. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by: Jameson Rollins &lt;jrollins [at] finestructure.net&gt;, Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt;, Matthew Goins &lt;mjgoins [at] openflows.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-monkeysphere/">monkeysphere</a></code>(1), <code><a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a></code>(7), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/8-monkeysphere-authentication/">monkeysphere-authentication</a></code>(8), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8) </p>
