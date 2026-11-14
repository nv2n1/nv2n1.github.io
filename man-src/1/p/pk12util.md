---
title: "pk12util(1)"
name: "pk12util"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pk12util/"
description: "pk12util – Export and import keys and certificate to or from a PKCS #12 file and the NSS database"
---

<h2 class="name">NAME</h2>
<p> pk12util &#8211; Export and import keys and certificate to or from a PKCS #12 file and the NSS database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pk12util</code> [-i p12File|-l p12File|-o p12File] [-d&nbsp;<wbr>[sql:]directory] [-h tokenname] [-P dbprefix] [-r] [-v] [-k slotPasswordFile|-K slotPassword] [-w p12filePasswordFile|-W p12filePassword]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The PKCS #12 utility, <code>pk12util</code>, enables sharing certificates among any server that supports PKCS#12. The tool can import certificates and keys from PKCS#12 files into security databases, export certificates, and list certificates and keys.</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<p> <code>Options</code> </p>
<p> -i p12file</p>
<dl>
<dt>
<dd> Import keys and certificates from a PKCS#12 file into a security database.</dl>
<p> -l p12file</p>
<dl>
<dt>
<dd> List the keys and certificates in PKCS#12 file.</dl>
<p> -o p12file</p>
<dl>
<dt>
<dd> Export keys and certificates from the security database to a PKCS#12 file.</dl>
<p> <code>Arguments</code> </p>
<p> -c keyCipher</p>
<dl>
<dt>
<dd> Specify the key encryption algorithm.</dl>
<p> -C certCipher</p>
<dl>
<dt>
<dd> Specify the key cert (overall package) encryption algorithm.</dl>
<p> -d [sql:]directory</p>
<dl>
<dt>
<dd> Specify the database directory into which to import to or export from certificates and keys. </p>
<p> <code>pk12util</code> supports two types of databases: the legacy security databases (cert8.db, key3.db, and secmod.db) and new SQLite databases (cert9.db, key4.db, and pkcs11.txt). If the prefix <code>sql:</code> is not used, then the tool assumes that the given databases are in the old format.</dl>
<p> -h tokenname</p>
<dl>
<dt>
<dd> Specify the name of the token to import into or export from.</dl>
<p> -k slotPasswordFile</p>
<dl>
<dt>
<dd> Specify the text file containing the slot&#8217;s password.</dl>
<p> -K slotPassword</p>
<dl>
<dt>
<dd> Specify the slot&#8217;s password.</dl>
<p> -m | &#8211;key-len keyLength</p>
<dl>
<dt>
<dd> Specify the desired length of the symmetric key to be used to encrypt the private key.</dl>
<p> -n | &#8211;cert-key-len certKeyLength</p>
<dl>
<dt>
<dd> Specify the desired length of the symmetric key to be used to encrypt the certificates and other meta-data.</dl>
<p> -n certname</p>
<dl>
<dt>
<dd> Specify the nickname of the cert and private key to export.</dl>
<p> -P prefix</p>
<dl>
<dt>
<dd> Specify the prefix used on the certificate and key databases. This option is provided as a special case. Changing the names of the certificate and key databases is not recommended.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Dumps all of the data in raw (binary) form. This must be saved as a DER file. The default is to return information in a pretty-print ASCII format, which displays the information about the certificates and public keys in the p12 file.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Enable debug logging when importing.</dl>
<p> -w p12filePasswordFile</p>
<dl>
<dt>
<dd> Specify the text file containing the pkcs #12 file password.</dl>
<p> -W p12filePassword</p>
<dl>
<dt>
<dd> Specify the pkcs #12 file password.</dl>
<h2>RETURN CODES</h2>
<dl>
<dt>
<dd> &bull; 0 &#8211; No error</dl>
<dl>
<dt>
<dd> &bull; 1 &#8211; User Cancelled</dl>
<dl>
<dt>
<dd> &bull; 2 &#8211; Usage error</dl>
<dl>
<dt>
<dd> &bull; 6 &#8211; NLS init error</dl>
<dl>
<dt>
<dd> &bull; 8 &#8211; Certificate DB open error</dl>
<dl>
<dt>
<dd> &bull; 9 &#8211; Key DB open error</dl>
<dl>
<dt>
<dd> &bull; 10 &#8211; File initialization error</dl>
<dl>
<dt>
<dd> &bull; 11 &#8211; Unicode conversion error</dl>
<dl>
<dt>
<dd> &bull; 12 &#8211; Temporary file creation error</dl>
<dl>
<dt>
<dd> &bull; 13 &#8211; PKCS11 get slot error</dl>
<dl>
<dt>
<dd> &bull; 14 &#8211; PKCS12 decoder start error</dl>
<dl>
<dt>
<dd> &bull; 15 &#8211; error read from import file</dl>
<dl>
<dt>
<dd> &bull; 16 &#8211; pkcs12 decode error</dl>
<dl>
<dt>
<dd> &bull; 17 &#8211; pkcs12 decoder verify error</dl>
<dl>
<dt>
<dd> &bull; 18 &#8211; pkcs12 decoder validate bags error</dl>
<dl>
<dt>
<dd> &bull; 19 &#8211; pkcs12 decoder import bags error</dl>
<dl>
<dt>
<dd> &bull; 20 &#8211; key db conversion version 3 to version 2 error</dl>
<dl>
<dt>
<dd> &bull; 21 &#8211; cert db conversion version 7 to version 5 error</dl>
<dl>
<dt>
<dd> &bull; 22 &#8211; cert and key dbs patch error</dl>
<dl>
<dt>
<dd> &bull; 23 &#8211; get default cert db error</dl>
<dl>
<dt>
<dd> &bull; 24 &#8211; find cert by nickname error</dl>
<dl>
<dt>
<dd> &bull; 25 &#8211; create export context error</dl>
<dl>
<dt>
<dd> &bull; 26 &#8211; PKCS12 add password itegrity error</dl>
<dl>
<dt>
<dd> &bull; 27 &#8211; cert and key Safes creation error</dl>
<dl>
<dt>
<dd> &bull; 28 &#8211; PKCS12 add cert and key error</dl>
<dl>
<dt>
<dd> &bull; 29 &#8211; PKCS12 encode error</dl>
<h2>EXAMPLES</h2>
<p> <code>Importing Keys and Certificates</code> </p>
<p> The most basic usage of <code>pk12util</code> for importing a certificate or key is the PKCS#12 input file (<code>-i</code>) and some way to specify the security database being accessed (either <code>-d</code> for a directory or <code>-h</code> for a token). </p>
<p> pk12util -i p12File [-h tokenname] [-v] [-d [sql:]directory] [-P dbprefix] [-k slotPasswordFile|-K slotPassword] [-w p12filePasswordFile|-W p12filePassword] </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
# pk12util -i /tmp/cert-files/users.p12 -d sql:/home/my/sharednssdb
Enter a password which will be used to encrypt your keys.
The password should be at least 8 characters long,
and should contain at least one non-alphabetic character.
Enter new password: 
Re-enter password: 
Enter password for PKCS12 file: 
pk12util: PKCS12 IMPORT SUCCESSFUL
</pre>
</dl>
<p> <code>Exporting Keys and Certificates</code> </p>
<p> Using the <code>pk12util</code> command to export certificates and keys requires both the name of the certificate to extract from the database (<code>-n</code>) and the PKCS#12-formatted output file to write to. There are optional parameters that can be used to encrypt the file to protect the certificate material. </p>
<p> pk12util -o p12File -n certname [-c keyCipher] [-C certCipher] [-m|&#8211;key_len keyLen] [-n|&#8211;cert_key_len certKeyLen] [-d [sql:]directory] [-P dbprefix] [-k slotPasswordFile|-K slotPassword] [-w p12filePasswordFile|-W p12filePassword] </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
# pk12util -o certs.p12 -n Server-Cert -d sql:/home/my/sharednssdb
Enter password for PKCS12 file: 
Re-enter password: 
</pre>
</dl>
<p> <code>Listing Keys and Certificates</code> </p>
<p> The information in a .p12 file are not human-readable. The certificates and keys in the file can be printed (listed) in a human-readable pretty-print format that shows information for every certificate and any public keys in the .p12 file. </p>
<p> pk12util -l p12File [-h tokenname] [-r] [-d [sql:]directory] [-P dbprefix] [-k slotPasswordFile|-K slotPassword] [-w p12filePasswordFile|-W p12filePassword] </p>
<p> For example, this prints the default ASCII output: </p>
<dl>
<dt>
<dd>
<pre>
# pk12util -l certs.p12
Enter password for PKCS12 file: 
Key(shrouded):
    Friendly Name: Thawte Freemail Member's Thawte Consulting (Pty) Ltd. ID
    Encryption algorithm: PKCS #12 V2 PBE With SHA-1 And 3KEY Triple DES-CBC
        Parameters:
            Salt:
                45:2e:6a:a0:03:4d:7b:a1:63:3c:15:ea:67:37:62:1f
            Iteration Count: 1 (0x1)
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 13 (0xd)
        Signature Algorithm: PKCS #1 SHA-1 With RSA Encryption
        Issuer: &quot;E=personal-freemail [at] thawte.com,CN=Thawte Personal Freemail C
            A,OU=Certification Services Division,O=Thawte Consulting,L=Cape T
            own,ST=Western Cape,C=ZA&quot;
    
</pre>
</dl>
<p> Alternatively, the <code>-r</code> prints the certificates and then exports them into separate DER binary files. This allows the certificates to be fed to another application that supports .p12 files. Each certificate is written to a sequentially-number file, beginning with file0001.der and continuing through file000N.der, incrementing the number for every certificate: </p>
<dl>
<dt>
<dd>
<pre>
pk12util -l test.p12 -r
Enter password for PKCS12 file: 
Key(shrouded):
    Friendly Name: Thawte Freemail Member's Thawte Consulting (Pty) Ltd. ID
    Encryption algorithm: PKCS #12 V2 PBE With SHA-1 And 3KEY Triple DES-CBC
        Parameters:
            Salt:
                45:2e:6a:a0:03:4d:7b:a1:63:3c:15:ea:67:37:62:1f
            Iteration Count: 1 (0x1)
Certificate    Friendly Name: Thawte Personal Freemail Issuing CA - Thawte Consulting
Certificate    Friendly Name: Thawte Freemail Member's Thawte Consulting (Pty) Ltd. ID
    
</pre>
</dl>
<h2>PASSWORD ENCRYPTION</h2>
<p> PKCS#12 provides for not only the protection of the private keys but also the certificate and meta-data associated with the keys. Password-based encryption is used to protect private keys on export to a PKCS#12 file and, optionally, the entire package. If no algorithm is specified, the tool defaults to using <code>PKCS12 V2 PBE with SHA1 and 3KEY Triple DES-cbc</code> for private key encryption. <code>PKCS12 V2 PBE with SHA1 and 40 Bit RC4</code> is the default for the overall package encryption when not in FIPS mode. When in FIPS mode, there is no package encryption. </p>
<p> The private key is always protected with strong encryption by default. </p>
<p> Several types of ciphers are supported. </p>
<p> Symmetric CBC ciphers for PKCS#5 V2</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; DES-CBC</dl>
<dl>
<dt>
<dd> &bull; RC2-CBC</dl>
<dl>
<dt>
<dd> &bull; RC5-CBCPad</dl>
<dl>
<dt>
<dd> &bull; DES-EDE3-CBC (the default for key encryption)</dl>
<dl>
<dt>
<dd> &bull; AES-128-CBC</dl>
<dl>
<dt>
<dd> &bull; AES-192-CBC</dl>
<dl>
<dt>
<dd> &bull; AES-256-CBC</dl>
<dl>
<dt>
<dd> &bull; CAMELLIA-128-CBC</dl>
<dl>
<dt>
<dd> &bull; CAMELLIA-192-CBC</dl>
<dl>
<dt>
<dd> &bull; CAMELLIA-256-CBC</dl>
</dl>
<p> PKCS#12 PBE ciphers</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; PKCS #12 PBE with Sha1 and 128 Bit RC4</dl>
<dl>
<dt>
<dd> &bull; PKCS #12 PBE with Sha1 and 40 Bit RC4</dl>
<dl>
<dt>
<dd> &bull; PKCS #12 PBE with Sha1 and Triple DES CBC</dl>
<dl>
<dt>
<dd> &bull; PKCS #12 PBE with Sha1 and 128 Bit RC2 CBC</dl>
<dl>
<dt>
<dd> &bull; PKCS #12 PBE with Sha1 and 40 Bit RC2 CBC</dl>
<dl>
<dt>
<dd> &bull; PKCS12 V2 PBE with SHA1 and 128 Bit RC4</dl>
<dl>
<dt>
<dd> &bull; PKCS12 V2 PBE with SHA1 and 40 Bit RC4 (the default for non-FIPS mode)</dl>
<dl>
<dt>
<dd> &bull; PKCS12 V2 PBE with SHA1 and 3KEY Triple DES-cbc</dl>
<dl>
<dt>
<dd> &bull; PKCS12 V2 PBE with SHA1 and 2KEY Triple DES-cbc</dl>
<dl>
<dt>
<dd> &bull; PKCS12 V2 PBE with SHA1 and 128 Bit RC2 CBC</dl>
<dl>
<dt>
<dd> &bull; PKCS12 V2 PBE with SHA1 and 40 Bit RC2 CBC</dl>
</dl>
<p> PKCS#5 PBE ciphers</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; PKCS #5 Password Based Encryption with MD2 and DES CBC</dl>
<dl>
<dt>
<dd> &bull; PKCS #5 Password Based Encryption with MD5 and DES CBC</dl>
<dl>
<dt>
<dd> &bull; PKCS #5 Password Based Encryption with SHA1 and DES CBC</dl>
</dl>
<p> With PKCS#12, the crypto provider may be the soft token module or an external hardware module. If the cryptographic module does not support the requested algorithm, then the next best fit will be selected (usually the default). If no suitable replacement for the desired algorithm can be found, the tool returns the error <i>no security module can perform the requested operation</i>.</p>
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
# pk12util -i /tmp/cert-files/users.p12 -d sql:/home/my/sharednssdb
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
<p> This line can be set added to the ~/.bashrc file to make the change permanent. </p>
<p> Most applications do not use the shared database by default, but they can be configured to use them. For example, this how-to article covers how to configure Firefox and Thunderbird to use the new shared NSS databases: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<p> For an engineering draft on the changes in the shared NSS databases, see the NSS project wiki: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
<h2>SEE ALSO</h2>
<p> certutil (1) </p>
<p> modutil (1) </p>
<p> The NSS wiki has information on the new database design and how to configure applications to use it. </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
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
