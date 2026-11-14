---
title: "ipa-replica-install(1)"
name: "ipa-replica-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-replica-install/"
description: "ipa-replica-install – Create an IPA replica"
---

<h2>NAME</h2>
<p> ipa-replica-install &#8211; Create an IPA replica</p>
<h2>SYNOPSIS</h2>
<h3>DOMAIN LEVEL 0</h3>
<dl>
<dt>ipa-replica-install [<i>OPTION</i>]&#8230; [replica_file]</p>
<dd></dl>
<h3>DOMAIN LEVEL 1</h3>
<dl>
<dt>ipa-replica-install [<i>OPTION</i>]&#8230;</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> Configures a new IPA server that is a replica of the server. Once it has been created it is an exact copy of the original IPA server and is an equal master. Changes made to any master are automatically replicated to other masters. </p>
<p> To create a replica in a domain at domain level 0, you need to provide an replica file. The replica_file is created using the ipa-replica-prepare utility. </p>
<p> To create a replica in a domain at domain level 1, you don&#8217;t have to provide a replica file, the machine only needs to be enrolled in the FreeIPA domain first. This process of turning the IPA client into a replica is also referred to as replica promotion. </p>
<p> If you&#8217;re starting with an existing IPA client, simply run ipa-replica-install to have it promoted into a replica. </p>
<p> To promote a blank machine into a replica, you have two options, you can either run ipa-client-install in a separate step, or pass the enrollment related options to the ipa-replica-install (see DOMAIN LEVEL 1 CLIENT ENROLLMENT OPTIONS). In the latter case, ipa-replica-install will join the machine to the IPA realm automatically and will proceed with the promotion step. </p>
<p> If the installation fails you may need to run ipa-server-install &#8211;uninstall and ipa-client-install before running ipa-replica-install again. </p>
<p> The installation will fail if the host you are installing the replica on exists as a host in IPA or an existing replication agreement exists (for example, from a previously failed installation). </p>
<p> A replica should only be installed on the same or higher version of IPA on the remote system.</p>
<h2>OPTIONS</h2>
<h3>DOMAIN LEVEL 1 OPTIONS</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;principal</code></p>
<dd> The user principal which will be used to promote the client to the replica and enroll the client itself, if necessary.</p>
<dt><code>-w</code>, <code>&#8211;admin-password</code></p>
<dd> The Kerberos password for the given principal. </p>
</dl>
<h3>DOMAIN LEVEL 1 CLIENT ENROLLMENT OPTIONS</h3>
<p> To install client and promote it to replica using a host keytab or One Time Password, the host needs to be a member of ipaservers group. This requires to create a host entry and add it to the host group prior replica installation. </p>
<p> &#8211;server, &#8211;domain, &#8211;realm options are autodiscovered via DNS records by default. </p>
<dl>
<dt><code>-p</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd> One Time Password for joining a machine to the IPA realm.</p>
<dt><code>-k</code>, <code>&#8211;keytab</code></p>
<dd> Path to host keytab.</p>
<dt><code>&#8211;server</code></p>
<dd> The fully qualified domain name of the IPA server to enroll to.</p>
<dt><code>-n</code>, <code>&#8211;domain</code>=<i>DOMAIN</i></p>
<dd> Set the domain name to DOMAIN.</p>
<dt><code>-r</code>, <code>&#8211;realm</code>=<i>REALM_NAME</i></p>
<dd> Set the IPA realm name to REALM_NAME.</p>
<dt><code>&#8211;hostname</code></p>
<dd> The hostname of this machine (FQDN). If specified, the hostname will be set and the system configuration will be updated to persist over reboot. </p>
</dl>
<h3>DOMAIN LEVEL 0 OPTIONS</h3>
<dl>
<dt><code>-p</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd> Directory Manager (existing master) password</p>
<dt><code>-w</code>, <code>&#8211;admin-password</code></p>
<dd> Admin user Kerberos password used for connection check </p>
</dl>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>&#8211;ip-address</code>=<i>IP_ADDRESS</i></p>
<dd> The IP address of this server. If this address does not match the address the host resolves to and &#8211;setup-dns is not selected the installation will fail. If the server hostname is not resolvable, a record for the hostname and IP_ADDRESS is added to /etc/hosts. This this option can be used multiple times to specify more IP addresses of the server (e.g. multihomed and/or dualstacked server).</p>
<dt><code>&#8211;mkhomedir</code></p>
<dd> Create home directories for users on their first login</p>
<dt><code>-N</code>, <code>&#8211;no-ntp</code></p>
<dd> Do not configure NTP</p>
<dt><code>&#8211;no-ui-redirect</code></p>
<dd> Do not automatically redirect to the Web UI.</p>
<dt><code>&#8211;ssh-trust-dns</code></p>
<dd> Configure OpenSSH client to trust DNS SSHFP records.</p>
<dt><code>&#8211;no-ssh</code></p>
<dd> Do not configure OpenSSH client.</p>
<dt><code>&#8211;no-sshd</code></p>
<dd> Do not configure OpenSSH server.</p>
<dt><code>&#8211;skip-conncheck</code></p>
<dd> Skip connection check to remote master</p>
<dt><code>-d</code>, <code>&#8211;debug</p>
<dd> Enable debug logging when more verbose output is needed</p>
<dt>-U</code>, <code>&#8211;unattended</code></p>
<dd> An unattended installation that will never prompt for user input</p>
<dt><code>&#8211;dirsrv-config-file</code></p>
<dd> The path to LDIF file that will be used to modify configuration of dse.ldif during installation of the directory server instance </p>
</dl>
<h3>CERTIFICATE SYSTEM OPTIONS</h3>
<dl>
<dt><code>&#8211;setup-ca</code></p>
<dd> Install and configure a CA on this replica. If a CA is not configured then certificate operations will be forwarded to a master with a CA installed.</p>
<dt><code>&#8211;dirsrv-cert-file</code>=FILE</p>
<dd> File containing the Directory Server SSL certificate and private key</p>
<dt><code>&#8211;http-cert-file</code>=FILE</p>
<dd> File containing the Apache Server SSL certificate and private key</p>
<dt><code>&#8211;dirsrv-pin</code>=PIN</p>
<dd> The password to unlock the Directory Server private key</p>
<dt><code>&#8211;http-pin</code>=PIN</p>
<dd> The password to unlock the Apache Server private key</p>
<dt><code>&#8211;dirsrv-cert-name</code>=NAME</p>
<dd> Name of the Directory Server SSL certificate to install</p>
<dt><code>&#8211;http-cert-name</code>=NAME</p>
<dd> Name of the Apache Server SSL certificate to install</p>
<dt><code>&#8211;skip-schema-check</code></p>
<dd> Skip check for updated CA DS schema on the remote master </p>
</dl>
<h3>DNS OPTIONS</h3>
<dl>
<dt><code>&#8211;setup-dns</code></p>
<dd> Generate a DNS zone if it does not exist already and configure the DNS server. This option requires that you either specify at least one DNS forwarder through the <code>&#8211;forwarder</code> option or use the <code>&#8211;no-forwarders</code> option.</p>
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
<dd> Do not create new reverse DNS zone. If a reverse DNS zone already exists for the subnet, it will be used.</p>
<dt><code>&#8211;auto-reverse</code></p>
<dd> Create necessary reverse zones</p>
<dt><code>&#8211;allow-zone-overlap</code></p>
<dd> Create DNS zone even if it already exists</p>
<dt><code>&#8211;no-host-dns</code></p>
<dd> Do not use DNS for hostname lookup during installation</p>
<dt><code>&#8211;no-dns-sshfp</code></p>
<dd> Do not automatically create DNS SSHFP records.</p>
<dt><code>&#8211;no-dnssec-validation</code></p>
<dd> Disable DNSSEC validation on this server. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<p> 3 if the host exists in the IPA server or a replication agreement to the remote master already exists </p>
<h2>Index</h2>
