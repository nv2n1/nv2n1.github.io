---
title: "ods-hsmutil(1)"
name: "ods-hsmutil"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ods-hsmutil/"
description: "ods-hsmutil – OpenDNSSEC HSM utility"
---

<h2>NAME</h2>
<p> <code>ods-hsmutil</code> &#8211; OpenDNSSEC HSM utility</p>
<h2>SYNOPSIS</h2>
<p> <code>ods-hsmutil</code> [<code>-c</code> <i>config</i>] [<code>-v</code>] <code>command </code> [<code>options</code>]</p>
<h2>DESCRIPTION</h2>
<p> The ods-hsmutil utility is mainly used for debugging or testing. It is designed to interact directly with your HSM and can be used to manually list, create or delete keys. It can also be used to perform a set of basics HSM tests. Be careful before creating or deleting keys using ods-hsmutil, as the changes are not synchronized with the KASP Enforcer. </p>
<p> The repositories are configured by the user in the OpenDNSSEC configuration file. The configuration contains the name of the repository, the token label, the user PIN, and the path to its shared library.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>login</code></p>
<dd> If there is no PIN in conf.xml, then this command will ask for it and login. The PINs are stored in a shared memory and are accessible to the other daemons.</p>
<dt><code>logout</code></p>
<dd> Will erase the semaphore and the shared memory containing any credentials. Authenticated processes will still be able to interact with the HSM.</p>
<dt><code>list</code> [<i>repository</i>]</p>
<dd> List the keys that are available in all or one <i>repository</i></p>
<dt><code>generate</code> <i>repository</i> <code>rsa</code> <i>keysize</i></p>
<dd> Generate a new RSA key with the given <i>keysize</i> in the <i>repository</i></p>
<dt><code>remove</code> <i>id</i></p>
<dd> Delete the key with the given <i>id</i></p>
<dt><code>purge</code> <i>repository</i></p>
<dd> Delete all keys in one <i>repository</i></p>
<dt><code>dnskey</code> <i>id</i> <i>name</i></p>
<dd> Create a DNSKEY RR for the given owner <i>name</i> based on the key with this <i>id</i></p>
<dt><code>test</code> <i>repository</i></p>
<dd> Perform a number of tests on a <i>repository</i></p>
<dt><code>info</code></p>
<dd> Show detailed information about all repositories</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>config</i></p>
<dd> Path to an OpenDNSSEC configuration file </p>
<p> (defaults to /etc/opendnssec/conf.xml)</p>
<dt><code>-h</code></p>
<dd> Show the help screen</p>
<dt><code>-v</code></p>
<dd> Output more information by increasing the verbosity level</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ods-auditor/">ods-auditor</a>(1), <a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>ods-hsmutil</code> was written by Jakob Schlyter as part of the OpenDNSSEC project. </p>
<h2>Index</h2>
