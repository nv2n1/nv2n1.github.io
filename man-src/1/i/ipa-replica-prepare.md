---
title: "ipa-replica-prepare(1)"
name: "ipa-replica-prepare"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-replica-prepare/"
description: "ipa-replica-prepare – Create an IPA replica file"
---

<h2>NAME</h2>
<p> ipa-replica-prepare &#8211; Create an IPA replica file</p>
<h2>SYNOPSIS</h2>
<p> ipa-replica-prepare [<i>OPTION</i>]&#8230; hostname</p>
<h2>DESCRIPTION</h2>
<p> Generates a replica file that may be used with ipa-replica-install to create a replica of an IPA server. </p>
<p> A replica can be created on any IPA master or replica server. </p>
<p> You must provide the fully-qualified hostname of the machine you want to install the replica on and a host-specific replica_file will be created. It is host-specific because SSL server certificates are generated as part of the process and they are specific to a particular hostname. </p>
<p> If IPA manages the DNS for your domain, you should either use the <code>&#8211;ip-address</code> option or add the forward and reverse records manually using IPA plugins. </p>
<p> Once the file has been created it will be named replica-hostname. This file can then be moved across the network to the target machine and a new IPA replica setup by running ipa-replica-install replica-hostname.</p>
<h3>Limitations</h3>
<p> A replica should only be installed on the same or higher version of IPA on the remote system. </p>
<p> A replica with PKI can only be installed from a replica file prepared on a master with PKI.</p>
<h2>OPTIONS</h2>
<dl>
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
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;password</code>=<i>DM_PASSWORD</i></p>
<dd> Directory Manager (existing master) password</p>
<dt><code>&#8211;ip-address</code>=<i>IP_ADDRESS</i></p>
<dd> IPv4 or IPv6 address of the replica server. This option can be specified multiple times for each interface of the server (e.g. multihomed and/or dualstacked server), or for each IPv4 and IPv6 address of the server. The corresponding A or AAAA and PTR records will be added to the DNS if they do not exist already.</p>
<dt><code>&#8211;reverse-zone</code>=<i>REVERSE_ZONE</i></p>
<dd> The reverse DNS zone to use. This option can be used multiple times to specify multiple reverse zones.</p>
<dt><code>&#8211;no-reverse</code></p>
<dd> Do not create reverse DNS zone</p>
<dt><code>&#8211;ca</code>=<i>CA_FILE</i></p>
<dd> Location of CA PKCS#12 file, default /root/cacert.p12</p>
<dt><code>&#8211;debug</code></p>
<dd> Prints info log messages to the output</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
