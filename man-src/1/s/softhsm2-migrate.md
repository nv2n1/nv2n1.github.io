---
title: "softhsm2-migrate(1)"
name: "softhsm2-migrate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-softhsm2-migrate/"
description: "softhsm2-migrate – SoftHSM v1 migration tool"
---

<h2>NAME</h2>
<p> softhsm2-migrate &#8211; SoftHSM v1 migration tool</p>
<h2>SYNOPSIS</h2>
<p> <code>softhsm2-migrate &#8211;db</code> <i>path</i> <code>&#8211;slot</code> <i>number</i> [<code>&#8211;pin</code> <i>PIN</i> <code>&#8211;no-public-key]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>softhsm2-migrate</code> is a tool that can migrate SoftHSM v1 databases to PKCS#11. The default HSM is SoftHSM v2, but can be used with other PKCS#11 libraries by using the option <code>&#8211;module</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;db </code><i>path</i></p>
<dd> The SoftHSM v1 database that is going to be migrated. The location of the token database can be found in the configuration file for SoftHSM v1.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Show the help information.</p>
<dt><code>&#8211;module </code><i>path</i></p>
<dd> Use another PKCS#11 library than SoftHSM.</p>
<dt><code>&#8211;no-public-key</code></p>
<dd> Do not migrate the public key.</p>
<dt><code>&#8211;pin </code><i>PIN</i></p>
<dd> The <i>PIN</i> for the normal user.</p>
<dt><code>&#8211;slot </code><i>number</i></p>
<dd> The database will be migrated to this slot.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Show the version info.</dl>
<h2>EXAMPLE</h2>
<p> A token database can be migrated with the following command: </p>
<dl>
<dt>
<dd>
<pre>
softhsm2-migrate --db /home/user/token.db --slot 1
</pre>
</dl>
<h2>AUTHORS</h2>
<p> Written by Rickard Bellgrim, Francis Dupont, René Post, and Roland van Rijswijk. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-softhsm2-keyconv/">softhsm2-keyconv</a></i>(1), <i><a href="/docs/linux/man/1-softhsm2-util/">softhsm2-util</a></i>(1), <i><a href="/docs/linux/man/5-softhsm2-conf/">softhsm2.conf</a></i>(5) </p>
<h2>Index</h2>
