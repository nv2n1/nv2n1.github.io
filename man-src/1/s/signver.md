---
title: "signver(1)"
name: "signver"
section: "1"
letter: "s"
url: "/docs/linux/man/1-signver/"
description: "signver – Verify a detached PKCS#7 signature for a file."
---

<h2 class="name">NAME</h2>
<p> signver &#8211; Verify a detached PKCS#7 signature for a file. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>signtool</code> -A | -V -d&nbsp;<wbr><i>directory</i> [-a] [-i&nbsp;<wbr><i>input_file</i>] [-o&nbsp;<wbr><i>output_file</i>] [-s&nbsp;<wbr><i>signature_file</i>] [-v]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The Signature Verification Tool, <code>signver</code>, is a simple command-line utility that unpacks a base-64-encoded PKCS#7 signed object and verifies the digital signature using standard cryptographic techniques. The Signature Verification Tool can also display the contents of the signed object.</p>
<h2>OPTIONS</h2>
<p> -A</p>
<dl>
<dt>
<dd> Displays all of the information in the PKCS#7 signature.</dl>
<p> -V</p>
<dl>
<dt>
<dd> Verifies the digital signature.</dl>
<p> -d [sql:]<i>directory</i></p>
<dl>
<dt>
<dd> Specify the database directory which contains the certificates and keys. </p>
<p> <code>signver</code> supports two types of databases: the legacy security databases (cert8.db, key3.db, and secmod.db) and new SQLite databases (cert9.db, key4.db, and pkcs11.txt). If the prefix <code>sql:</code> is not used, then the tool assumes that the given databases are in the old format.</dl>
<p> -a</p>
<dl>
<dt>
<dd> Sets that the given signature file is in ASCII format.</dl>
<p> -i <i>input_file</i></p>
<dl>
<dt>
<dd> Gives the input file for the object with signed data.</dl>
<p> -o <i>output_file</i></p>
<dl>
<dt>
<dd> Gives the output file to which to write the results.</dl>
<p> -s <i>signature_file</i></p>
<dl>
<dt>
<dd> Gives the input file for the digital signature.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Enables verbose output.</dl>
<h2>EXTENDED EXAMPLES</h2>
<h3>Verifying a Signature</h3>
<p> The <code>-V</code> option verifies that the signature in a given signature file is valid when used to sign the given object (from the input file). </p>
<dl>
<dt>
<dd>
<pre>
signver -V -s <i>signature_file</i> -i <i>signed_file</i> -d sql:/home/my/sharednssdb
signatureValid=yes
</pre>
</dl>
<h3>Printing Signature Data</h3>
<p> The <code>-A</code> option prints all of the information contained in a signature file. Using the <code>-o</code> option prints the signature file information to the given output file rather than stdout. </p>
<dl>
<dt>
<dd>
<pre>
signver -A -s <i>signature_file</i> -o <i>output_file</i>
</pre>
</dl>
<h2>NSS DATABASE TYPES</h2>
<p> NSS originally used BerkeleyDB databases to store security information. The last versions of these <i>legacy</i> databases are: </p>
<dl>
<dt>
<dd> &bull; cert8.db for certificates</dl>
<dl>
<dt>
<dd> &bull; key3.db for keys</dl>
<dl>
<dt>
<dd> &bull; secmod.db for PKCS #11 module information</dl>
<p> BerkeleyDB has performance limitations, though, which prevent it from being easily used by multiple applications simultaneously. NSS has some flexibility that allows applications to use their own, independent database engine while keeping a shared database and working around the access issues. Still, NSS requires more flexibility to provide a truly shared security database. </p>
<p> In 2009, NSS introduced a new set of databases that are SQLite databases rather than BerkleyDB. These new databases provide more accessibility and performance: </p>
<dl>
<dt>
<dd> &bull; cert9.db for certificates</dl>
<dl>
<dt>
<dd> &bull; key4.db for keys</dl>
<dl>
<dt>
<dd> &bull; pkcs11.txt, which is listing of all of the PKCS #11 modules contained in a new subdirectory in the security databases directory</dl>
<p> Because the SQLite databases are designed to be shared, these are the <i>shared</i> database type. The shared database type is preferred; the legacy format is included for backward compatibility. </p>
<p> By default, the tools (<code>certutil</code>, <code>pk12util</code>, <code>modutil</code>) assume that the given security databases follow the more common legacy type. Using the SQLite databases must be manually specified by using the <code>sql:</code> prefix with the given security directory. For example: </p>
<dl>
<dt>
<dd>
<pre>
# signver -A -s <i>signature</i> -d sql:/home/my/sharednssdb
</pre>
</dl>
<p> To set the shared database type as the default type for the tools, set the <code>NSS_DEFAULT_DB_TYPE</code> environment variable to <code>sql</code>: </p>
<dl>
<dt>
<dd>
<pre>
export NSS_DEFAULT_DB_TYPE=&quot;sql&quot;
</pre>
</dl>
<p> This line can be added to the ~/.bashrc file to make the change permanent for the user. </p>
<p> Most applications do not use the shared database by default, but they can be configured to use them. For example, this how-to article covers how to configure Firefox and Thunderbird to use the new shared NSS databases: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<p> For an engineering draft on the changes in the shared NSS databases, see the NSS project wiki: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
<h2>SEE ALSO</h2>
<p> signtool (1) </p>
<p> The NSS wiki has information on the new database design and how to configure applications to use it. </p>
<dl>
<dt>
<dd> &bull; Setting up the shared NSS database </p>
<p> <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<dl>
<dt>
<dd> &bull; Engineering and technical information about the shared NSS database </p>
<p> <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
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
