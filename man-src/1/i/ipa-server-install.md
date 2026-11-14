---
title: "ipa-server-install(1)"
name: "ipa-server-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-server-install/"
description: "ipa-server-install – Configure an IPA server"
---

<h2>NAME</h2>
<p> ipa-server-install &#8211; Configure an IPA server</p>
<h2>SYNOPSIS</h2>
<p> ipa-server-install [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Configures the services needed by an IPA server. This includes setting up a Kerberos Key Distribution Center (KDC) and a Kadmin daemon with an LDAP back-end, configuring Apache, configuring NTP and optionally configuring and starting an LDAP-backed DNS server. By default a dogtag-based CA will be configured to issue server certificates. </p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>-r</code> <i>REALM_NAME</i>, <code>&#8211;realm</code>=<i>REALM_NAME</i></p>
<dd> The Kerberos realm name for the IPA server. You will not be able to estabilish trust with Active Directory unless the realm name is uppercased domain name.</p>
<dt><code>-n</code> <i>DOMAIN_NAME</i>, <code>&#8211;domain</code>=<i>DOMAIN_NAME</i></p>
<dd> Your DNS domain name</p>
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;ds-password</code>=<i>DM_PASSWORD</i></p>
<dd> The password to be used by the Directory Server for the Directory Manager user</p>
<dt><code>-a</code> <i>ADMIN_PASSWORD</i>, <code>&#8211;admin-password</code>=<i>ADMIN_PASSWORD</i></p>
<dd> The password for the IPA admin user</p>
<dt><code>&#8211;mkhomedir</code></p>
<dd> Create home directories for users on their first login</p>
<dt><code>&#8211;hostname</code>=<i>HOST_NAME</i></p>
<dd> The fully-qualified DNS name of this server. If the hostname does not match system hostname, the system hostname will be updated accordingly to prevent service failures.</p>
<dt><code>&#8211;ip-address</code>=<i>IP_ADDRESS</i></p>
<dd> The IP address of this server. If this address does not match the address the host resolves to and &#8211;setup-dns is not selected the installation will fail. If the server hostname is not resolvable, a record for the hostname and IP_ADDRESS is added to /etc/hosts. This this option can be used multiple times to specify more IP addresses of the server (e.g. multihomed and/or dualstacked server).</p>
<dt><code>-N</code>, <code>&#8211;no-ntp</code></p>
<dd> Do not configure NTP</p>
<dt><code>&#8211;idstart</code>=<i>IDSTART</i></p>
<dd> The starting user and group id number (default random)</p>
<dt><code>&#8211;idmax</code>=<i>IDMAX</i></p>
<dd> The maximum user and group id number (default: idstart+199999). If set to zero, the default value will be used.</p>
<dt><code>&#8211;no_hbac_allow</code></p>
<dd> Don&#8217;t install allow_all HBAC rule. This rule lets any user from any host access any service on any other host. It is expected that users will remove this rule before moving to production.</p>
<dt><code>&#8211;ignore-topology-disconnect</code></p>
<dd> Ignore errors reported when IPA server uninstall would lead to disconnected topology. This option can be used only when domain level is 1 or more.</p>
<dt><code>&#8211;no-ui-redirect</code></p>
<dd> Do not automatically redirect to the Web UI.</p>
<dt><code>&#8211;ssh-trust-dns</code></p>
<dd> Configure OpenSSH client to trust DNS SSHFP records.</p>
<dt><code>&#8211;no-ssh</code></p>
<dd> Do not configure OpenSSH client.</p>
<dt><code>&#8211;no-sshd</code></p>
<dd> Do not configure OpenSSH server.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable debug logging when more verbose output is needed</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> An unattended installation that will never prompt for user input</p>
<dt><code>&#8211;dirsrv-config-file</code></p>
<dd> The path to LDIF file that will be used to modify configuration of dse.ldif during installation of the directory server instance </p>
</dl>
<h3>CERTIFICATE SYSTEM OPTIONS</h3>
<dl>
<dt><code>&#8211;external-ca</code></p>
<dd> Generate a CSR for the IPA CA certificate to be signed by an external CA.</p>
<dt><code>&#8211;external-ca-type</code>=<i>TYPE</i></p>
<dd> Type of the external CA. Possible values are &quot;generic&quot;, &quot;ms-cs&quot;. Default value is &quot;generic&quot;. Use &quot;ms-cs&quot; to include template name required by Microsoft Certificate Services (MS CS) in the generated CSR.</p>
<dt><code>&#8211;external-cert-file</code>=<i>FILE</i></p>
<dd> File containing the IPA CA certificate and the external CA certificate chain. The file is accepted in PEM and DER certificate and PKCS#7 certificate chain formats. This option may be used multiple times.</p>
<dt><code>&#8211;dirsrv-cert-file</code>=<i>FILE</i></p>
<dd> File containing the Directory Server SSL certificate and private key. The files are accepted in PEM and DER certificate, PKCS#7 certificate chain, PKCS#8 and raw private key and PKCS#12 formats. This option may be used multiple times.</p>
<dt><code>&#8211;http-cert-file</code>=<i>FILE</i></p>
<dd> File containing the Apache Server SSL certificate and private key. The files are accepted in PEM and DER certificate, PKCS#7 certificate chain, PKCS#8 and raw private key and PKCS#12 formats. This option may be used multiple times.</p>
<dt><code>&#8211;dirsrv-pin</code>=<i>PIN</i></p>
<dd> The password to unlock the Directory Server private key</p>
<dt><code>&#8211;http-pin</code>=<i>PIN</i></p>
<dd> The password to unlock the Apache Server private key</p>
<dt><code>&#8211;dirsrv-cert-name</code>=<i>NAME</i></p>
<dd> Name of the Directory Server SSL certificate to install</p>
<dt><code>&#8211;http-cert-name</code>=<i>NAME</i></p>
<dd> Name of the Apache Server SSL certificate to install</p>
<dt><code>&#8211;ca-cert-file</code>=<i>FILE</i></p>
<dd> File containing the CA certificate of the CA which issued the Directory Server, Apache Server and Kerberos KDC certificates. The file is accepted in PEM and DER certificate and PKCS#7 certificate chain formats. This option may be used multiple times. Use this option if the CA certificate is not present in the certificate files.</p>
<dt><code>&#8211;subject</code>=<i>SUBJECT</i></p>
<dd> The certificate subject base (default O=REALM.NAME)</p>
<dt><code>&#8211;ca-signing-algorithm</code>=<i>ALGORITHM</i></p>
<dd> Signing algorithm of the IPA CA certificate. Possible values are SHA1withRSA, SHA256withRSA, SHA512withRSA. Default value is SHA256withRSA. Use this option with &#8211;external-ca if the external CA does not support the default signing algorithm. </p>
</dl>
<h3>DNS OPTIONS</h3>
<dl>
<dt><code>&#8211;setup-dns</code></p>
<dd> Generate a DNS zone if it does not exist already and configure the DNS server. This option requires that you either specify at least one DNS forwarder through the <code>&#8211;forwarder</code> option or use the <code>&#8211;no-forwarders</code> option. </p>
<p> Note that you can set up a DNS at any time after the initial IPA server install by running <code>ipa-dns-install</code> (see <code><a href="/docs/linux/man/1-ipa-dns-install/">ipa-dns-install</a></code>(1)).</p>
<dt><code>&#8211;forwarder</code>=<i>IP_ADDRESS</i></p>
<dd> Add a DNS forwarder to the DNS configuration. You can use this option multiple times to specify more forwarders, but at least one must be provided, unless the <code>&#8211;no-forwarders</code> option is specified.</p>
<dt><code>&#8211;no-forwarders</code></p>
<dd> Do not add any DNS forwarders. Root DNS servers will be used instead.</p>
<dt><code>&#8211;auto-forwarders</code></p>
<dd> Add DNS forwarders configured in /etc/resolv.conf to the list of forwarders used by IPA DNS.</p>
<dt><code>&#8211;forward-policy</code>=<i>first|only</i></p>
<dd> DNS forwarding policy for global forwarders specified using other options. Defaults to first if no IP address belonging to a private or reserved ranges is detected on local interfaces (RFC 6303). Defaults to only if a private IP address is detected.</p>
<dt><code>&#8211;reverse-zone</code>=<i>REVERSE_ZONE</i></p>
<dd> The reverse DNS zone to use. This option can be used multiple times to specify multiple reverse zones.</p>
<dt><code>&#8211;no-reverse</code></p>
<dd> Do not create reverse DNS zone</p>
<dt><code>&#8211;auto-reverse</code></p>
<dd> Try to resolve reverse records and reverse zones for server IP addresses and if neither is resolvable creates these reverse zones.</p>
<dt><code>&#8211;zonemgr</code></p>
<dd> The e-mail address of the DNS zone manager. Defaults to hostmaster [at] DOMAIN</p>
<dt><code>&#8211;no-host-dns</code></p>
<dd> Do not use DNS for hostname lookup during installation</p>
<dt><code>&#8211;no-dns-sshfp</code></p>
<dd> Do not automatically create DNS SSHFP records.</p>
<dt><code>&#8211;no-dnssec-validation</code></p>
<dd> Disable DNSSEC validation on this server.</p>
<dt><code>&#8211;allow-zone-overlap</code></p>
<dd> Allow creatin of (reverse) zone even if the zone is already resolvable. Using this option is discouraged as it result in later problems with domain name resolution. </p>
</dl>
<h3>UNINSTALL OPTIONS</h3>
<dl>
<dt><code>&#8211;uninstall</code></p>
<dd> Uninstall an existing IPA installation</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> An unattended uninstallation that will never prompt for user input </p>
</dl>
<h2>DEPRECATED OPTIONS</h2>
<dl>
<dt><code>-P</code> <i>MASTER_PASSWORD</i>, <code>&#8211;master-password</code>=<i>MASTER_PASSWORD</i></p>
<dd> The kerberos master password (normally autogenerated). </p>
</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the (un)installation was successful </p>
<p> 1 if an error occurred </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipa-dns-install/">ipa-dns-install</a></code>(1) </p>
<h2>Index</h2>
