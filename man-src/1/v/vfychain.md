---
title: "vfychain(1)"
name: "vfychain"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vfychain/"
description: "vfychain_ – vfychain [options] [revocation options] certfile [[options] certfile] …"
---

<h2 class="name">NAME</h2>
<p> vfychain_ &#8211; vfychain [options] [revocation options] certfile [[options] certfile] &#8230; </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>vfychain</code></dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The verification Tool, <code>vfychain</code>, verifies certificate chains. <code>modutil</code> can add and delete PKCS #11 modules, change passwords on security databases, set defaults, list module contents, enable or disable slots, enable or disable FIPS 140-2 compliance, and assign default providers for cryptographic operations. This tool can also create certificate, key, and module security database files. </p>
<p> The tasks associated with security module database management are part of a process that typically also involves managing key databases and certificate databases.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> the following certfile is base64 encoded</dl>
<p> <code>-b </code> <i>YYMMDDHHMMZ</i></p>
<dl>
<dt>
<dd> Validate date (default: now)</dl>
<p> <code>-d </code> <i>directory</i></p>
<dl>
<dt>
<dd> database directory</dl>
<p> <code>-f </code></p>
<dl>
<dt>
<dd> Enable cert fetching from AIA URL</dl>
<p> <code>-o </code> <i>oid</i></p>
<dl>
<dt>
<dd> Set policy OID for cert validation(Format OID.1.2.3)</dl>
<p> <code>-p </code></p>
<dl>
<dt>
<dd> Use PKIX Library to validate certificate by calling: </p>
<p> * CERT_VerifyCertificate if specified once, </p>
<p> * CERT_PKIXVerifyCert if specified twice and more.</dl>
<p> <code>-r </code></p>
<dl>
<dt>
<dd> Following certfile is raw binary DER (default)</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Following cert is explicitly trusted (overrides db trust)</dl>
<p> <code>-u </code> <i>usage</i></p>
<dl>
<dt>
<dd> 0=SSL client, 1=SSL server, 2=SSL StepUp, 3=SSL CA, 4=Email signer, 5=Email recipient, 6=Object signer, 9=ProtectedObjectSigner, 10=OCSP responder, 11=Any CA</dl>
<p> <code>-T </code></p>
<dl>
<dt>
<dd> Trust both explicit trust anchors (-t) and the database. (Without this option, the default is to only trust certificates marked -t, if there are any, or to trust the database if there are certificates marked -t.)</dl>
<p> <code>-v </code></p>
<dl>
<dt>
<dd> Verbose mode. Prints root cert subject(double the argument for whole root cert info)</dl>
<p> <code>-w </code> <i>password</i></p>
<dl>
<dt>
<dd> Database password</dl>
<p> <code>-W </code> <i>pwfile</i></p>
<dl>
<dt>
<dd> Password file</dl>
<dl>
<dt>
<dd> Revocation options for PKIX API (invoked with -pp options) is a collection of the following flags: [-g type [-h flags] [-m type [-s flags]] &#8230;] &#8230; </p>
<p> Where:</dl>
<p> <code>-g </code> <i>test-type</i></p>
<dl>
<dt>
<dd> Sets status checking test type. Possible values are &quot;leaf&quot; or &quot;chain&quot;</dl>
<p> <code>-g </code> <i>test type</i></p>
<dl>
<dt>
<dd> Sets status checking test type. Possible values are &quot;leaf&quot; or &quot;chain&quot;.</dl>
<p> <code>-h </code> <i>test flags</i></p>
<dl>
<dt>
<dd> Sets revocation flags for the test type it follows. Possible flags: &quot;testLocalInfoFirst&quot; and &quot;requireFreshInfo&quot;.</dl>
<p> <code>-m </code> <i>method type</i></p>
<dl>
<dt>
<dd> Sets method type for the test type it follows. Possible types are &quot;crl&quot; and &quot;ocsp&quot;.</dl>
<p> <code>-s </code> <i>method flags</i></p>
<dl>
<dt>
<dd> Sets revocation flags for the method it follows. Possible types are &quot;doNotUse&quot;, &quot;forbidFetching&quot;, &quot;ignoreDefaultSrc&quot;, &quot;requireInfo&quot; and &quot;failIfNoInfo&quot;.</dl>
<h2>ADDITIONAL RESOURCES</h2>
<p> For information about NSS and other tools related to NSS (like JSS), check out the NSS project wiki at m[blue]<code><a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></code>m[]. The NSS site relates directly to NSS code changes and releases. </p>
<p> Mailing lists: <a rel="nofollow" href="https://lists.mozilla.org/listinfo/dev-tech-crypto">https://lists.mozilla.org/listinfo/dev-tech-crypto</a> </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The NSS tools were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Mozilla NSS bug 836477</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dl>
</dl>
<h2>Index</h2>
