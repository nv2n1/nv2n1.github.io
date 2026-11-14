---
title: "cmsutil(1)"
name: "cmsutil"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmsutil/"
description: "cmsutil – Performs basic cryptograpic operations, such as encryption and decryption, on Cryptographic Message Syntax (CMS) messages."
---

<h2 class="name">NAME</h2>
<p> cmsutil &#8211; Performs basic cryptograpic operations, such as encryption and decryption, on Cryptographic Message Syntax (CMS) messages. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cmsutil</code> [<i>options</i>] [[<i>arguments</i>]]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The <code>cmsutil</code> command-line uses the S/MIME Toolkit to perform basic operations, such as encryption and decryption, on Cryptographic Message Syntax (CMS) messages. </p>
<p> To run cmsutil, type the command cmsutil option [arguments] where option and arguments are combinations of the options and arguments listed in the following section. Each command takes one option. Each option may take zero or more arguments. To see a usage string, issue the command without options.</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<p> <code>Options</code> </p>
<p> Options specify an action. Option arguments modify an action. The options and arguments for the cmsutil command are defined as follows: </p>
<p> -C</p>
<dl>
<dt>
<dd> Encrypt a message.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Decode a message.</dl>
<p> -E</p>
<dl>
<dt>
<dd> Envelope a message.</dl>
<p> -O</p>
<dl>
<dt>
<dd> Create a certificates-only message.</dl>
<p> -S</p>
<dl>
<dt>
<dd> Sign a message.</dl>
<p> <code>Arguments</code> </p>
<p> Option arguments modify an action. </p>
<p> -b</p>
<dl>
<dt>
<dd> Decode a batch of files named in infile.</dl>
<p> -c content</p>
<dl>
<dt>
<dd> Use this detached content (decode only).</dl>
<p> -d dbdir</p>
<dl>
<dt>
<dd> Specify the key/certificate database directory (default is &quot;.&quot;)</dl>
<p> -e envfile</p>
<dl>
<dt>
<dd> Specify a file containing an enveloped message for a set of recipients to which you would like to send an encrypted message. If this is the first encrypted message for that set of recipients, a new enveloped message will be created that you can then use for future messages (encrypt only).</dl>
<p> -f pwfile</p>
<dl>
<dt>
<dd> Use password file to set password on all PKCS#11 tokens.</dl>
<p> -G</p>
<dl>
<dt>
<dd> Include a signing time attribute (sign only).</dl>
<p> -H hash</p>
<dl>
<dt>
<dd> Use specified hash algorithm (default:SHA1).</dl>
<p> -h num</p>
<dl>
<dt>
<dd> Generate email headers with info about CMS message (decode only).</dl>
<p> -i infile</p>
<dl>
<dt>
<dd> Use infile as a source of data (default is stdin).</dl>
<p> -k</p>
<dl>
<dt>
<dd> Keep decoded encryption certs in permanent cert db.</dl>
<p> -N nickname</p>
<dl>
<dt>
<dd> Specify nickname of certificate to sign with (sign only).</dl>
<p> -n</p>
<dl>
<dt>
<dd> Suppress output of contents (decode only).</dl>
<p> -o outfile</p>
<dl>
<dt>
<dd> Use outfile as a destination of data (default is stdout).</dl>
<p> -P</p>
<dl>
<dt>
<dd> Include an S/MIME capabilities attribute.</dl>
<p> -p password</p>
<dl>
<dt>
<dd> Use password as key database password.</dl>
<p> -r recipient1,recipient2, &#8230;</p>
<dl>
<dt>
<dd> Specify list of recipients (email addresses) for an encrypted or enveloped message. For certificates-only message, list of certificates to send.</dl>
<p> -T</p>
<dl>
<dt>
<dd> Suppress content in CMS message (sign only).</dl>
<p> -u certusage</p>
<dl>
<dt>
<dd> Set type of cert usage (default is certUsageEmailSigner).</dl>
<p> -v</p>
<dl>
<dt>
<dd> Print debugging information.</dl>
<p> -Y ekprefnick</p>
<dl>
<dt>
<dd> Specify an encryption key preference by nickname.</dl>
<h2>USAGE</h2>
<p> Encrypt Example </p>
<dl>
<dt>
<dd>
<pre><code>
cmsutil - C[-i infile][-o outfile][-d dbdir][-p password] - r "recipient1,recipient2, . . ." - e envfile
</code></pre>
</dl>
<p> Decode Example </p>
<dl>
<dt>
<dd>
cmsutil &#8211; D[-i infile][-o outfile][-d dbdir][-p password][-c content][-n][-h num]
</dl>
<p> Envelope Example </p>
<dl>
<dt>
<dd>
cmsutil &#8211; E[-i infile][-o outfile][-d dbdir][-p password] &#8211; r &#8220;recipient1,recipient2, &#8230;&#8221;
</dl>
<p> Certificate-only Example </p>
<dl>
<dt>
<dd>
cmsutil &#8211; O[-i infile][-o outfile][-d dbdir][-p password] &#8211; r &#8220;cert1,cert2, . . .&#8221;
</dl>
<p> Sign Message Example </p>
<dl>
<dt>
<dd>
<pre><code>
cmsutil - S[-i infile][-o outfile][-d dbdir][-p password] - N nickname[-TGP][-Y ekprefnick]
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-certutil/">certutil</a>(1)</p>
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
