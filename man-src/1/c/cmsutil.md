---

title: "cmsutil(1)"
name: "cmsutil"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmsutil/"
description: "cmsutil – Performs basic cryptograpic operations, such as encryption and decryption, on Cryptographic Message Syntax (CMS) messages."
---

<dl>
<dt> <code>cmsutil</code> [<i>options</i>] [[<i>arguments</i>]]</dt></dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></dd>
<p> The <code>cmsutil</code> command-line uses the S/MIME Toolkit to perform basic operations, such as encryption and decryption, on Cryptographic Message Syntax (CMS) messages. </p>
<p> To run cmsutil, type the command cmsutil option [arguments] where option and arguments are combinations of the options and arguments listed in the following section. Each command takes one option. Each option may take zero or more arguments. To see a usage string, issue the command without options.</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<p> <code>Options</code> </p>
<p> Options specify an action. Option arguments modify an action. The options and arguments for the cmsutil command are defined as follows: </p>
<p> -C</p>
<dl>
<dt>
</dt><dd> Encrypt a message.</dd></dl>
<p> -D</p>
<dl>
<dt>
</dt><dd> Decode a message.</dd></dl>
<p> -E</p>
<dl>
<dt>
</dt><dd> Envelope a message.</dd></dl>
<p> -O</p>
<dl>
<dt>
</dt><dd> Create a certificates-only message.</dd></dl>
<p> -S</p>
<dl>
<dt>
</dt><dd> Sign a message.</dd></dl>
<p> <code>Arguments</code> </p>
<p> Option arguments modify an action. </p>
<p> -b</p>
<dl>
<dt>
</dt><dd> Decode a batch of files named in infile.</dd></dl>
<p> -c content</p>
<dl>
<dt>
</dt><dd> Use this detached content (decode only).</dd></dl>
<p> -d dbdir</p>
<dl>
<dt>
</dt><dd> Specify the key/certificate database directory (default is &quot;.&quot;)</dd></dl>
<p> -e envfile</p>
<dl>
<dt>
</dt><dd> Specify a file containing an enveloped message for a set of recipients to which you would like to send an encrypted message. If this is the first encrypted message for that set of recipients, a new enveloped message will be created that you can then use for future messages (encrypt only).</dd></dl>
<p> -f pwfile</p>
<dl>
<dt>
</dt><dd> Use password file to set password on all PKCS#11 tokens.</dd></dl>
<p> -G</p>
<dl>
<dt>
</dt><dd> Include a signing time attribute (sign only).</dd></dl>
<p> -H hash</p>
<dl>
<dt>
</dt><dd> Use specified hash algorithm (default:SHA1).</dd></dl>
<p> -h num</p>
<dl>
<dt>
</dt><dd> Generate email headers with info about CMS message (decode only).</dd></dl>
<p> -i infile</p>
<dl>
<dt>
</dt><dd> Use infile as a source of data (default is stdin).</dd></dl>
<p> -k</p>
<dl>
<dt>
</dt><dd> Keep decoded encryption certs in permanent cert db.</dd></dl>
<p> -N nickname</p>
<dl>
<dt>
</dt><dd> Specify nickname of certificate to sign with (sign only).</dd></dl>
<p> -n</p>
<dl>
<dt>
</dt><dd> Suppress output of contents (decode only).</dd></dl>
<p> -o outfile</p>
<dl>
<dt>
</dt><dd> Use outfile as a destination of data (default is stdout).</dd></dl>
<p> -P</p>
<dl>
<dt>
</dt><dd> Include an S/MIME capabilities attribute.</dd></dl>
<p> -p password</p>
<dl>
<dt>
</dt><dd> Use password as key database password.</dd></dl>
<p> -r recipient1,recipient2, &#8230;</p>
<dl>
<dt>
</dt><dd> Specify list of recipients (email addresses) for an encrypted or enveloped message. For certificates-only message, list of certificates to send.</dd></dl>
<p> -T</p>
<dl>
<dt>
</dt><dd> Suppress content in CMS message (sign only).</dd></dl>
<p> -u certusage</p>
<dl>
<dt>
</dt><dd> Set type of cert usage (default is certUsageEmailSigner).</dd></dl>
<p> -v</p>
<dl>
<dt>
</dt><dd> Print debugging information.</dd></dl>
<p> -Y ekprefnick</p>
<dl>
<dt>
</dt><dd> Specify an encryption key preference by nickname.</dd></dl>
<h2>USAGE</h2>
<p> Encrypt Example </p>
<dl>
<dt>
</dt><dd>
<pre><code>
cmsutil - C[-i infile][-o outfile][-d dbdir][-p password] - r "recipient1,recipient2, . . ." - e envfile
</code></pre>
</dd></dl>
<p> Decode Example </p>
<dl>
<dt>
</dt><dd>
cmsutil &#8211; D[-i infile][-o outfile][-d dbdir][-p password][-c content][-n][-h num]
</dd></dl>
<p> Envelope Example </p>
<dl>
<dt>
</dt><dd>
cmsutil &#8211; E[-i infile][-o outfile][-d dbdir][-p password] &#8211; r &#8220;recipient1,recipient2, &#8230;&#8221;
</dd></dl>
<p> Certificate-only Example </p>
<dl>
<dt>
</dt><dd>
cmsutil &#8211; O[-i infile][-o outfile][-d dbdir][-p password] &#8211; r &#8220;cert1,cert2, . . .&#8221;
</dd></dl>
<p> Sign Message Example </p>
<dl>
<dt>
</dt><dd>
<pre><code>
cmsutil - S[-i infile][-o outfile][-d dbdir][-p password] - N nickname[-TGP][-Y ekprefnick]
</code></pre>
</dd></dl>
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
<dt> 1.</dt>
<dd> Mozilla NSS bug 836477</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dd></dl>
</dl>
