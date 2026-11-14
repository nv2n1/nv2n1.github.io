---
title: "ssh-keygen(1)"
name: "ssh-keygen"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-keygen/"
description: "ssh-keygen – OpenSSH authentication key utility"
---

<h2 class="name">NAME</h2>
<p> <code>ssh-keygen</code> &#8211; OpenSSH authentication key utility </p>
<h2>SYNOPSIS</h2>
<p> <code>ssh-keygen</code> [-<code>q</code> ] [-<code>a </code><i>rounds</i> ] [-<code>b </code><i>bits</i> ] [-<code>C </code><i>comment</i> ] [-<code>f </code><i>output_keyfile</i> ] [-<code>m </code><i>format</i> ] [-<code>N </code><i>new_passphrase</i> ] [-<code>O </code><i>option</i> ] [-<code>t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa</code> ] [-<code>w </code><i>provider</i> ] [-<code>Z </code><i>cipher</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>p</code> [-<code>a </code><i>rounds</i> ] [-<code>f </code><i>keyfile</i> ] [-<code>m </code><i>format</i> ] [-<code>N </code><i>new_passphrase</i> ] [-<code>P </code><i>old_passphrase</i> ] [-<code>Z </code><i>cipher</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>i</code> [-<code>f </code><i>input_keyfile</i> ] [-<code>m </code><i>key_format</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>e</code> [-<code>f </code><i>input_keyfile</i> ] [-<code>m </code><i>key_format</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>y</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>c</code> [-<code>a </code><i>rounds</i> ] [-<code>C </code><i>comment</i> ] [-<code>f </code><i>keyfile</i> ] [-<code>P </code><i>passphrase</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>l</code> [-<code>v</code> ] [-<code>E </code><i>fingerprint_hash</i> ] [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>B</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>D </code><i>pkcs11</i><br />
<code>ssh-keygen</code> &#8211;<code>F </code><i>hostname</i> [-<code>lv</code> ] [-<code>f </code><i>known_hosts_file</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>H</code> [-<code>f </code><i>known_hosts_file</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>K</code> [-<code>a </code><i>rounds</i> ] [-<code>w </code><i>provider</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>R </code><i>hostname</i> [-<code>f </code><i>known_hosts_file</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>r </code><i>hostname</i> [-<code>g</code> ] [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>M generate</code> [-<code>O </code><i>option</i> ] <i>output_file</i><br />
<code>ssh-keygen</code> &#8211;<code>M screen</code> [-<code>f </code><i>input_file</i> ] [-<code>O </code><i>option</i> ] <i>output_file</i><br />
<code>ssh-keygen</code> &#8211;<code>I </code><i>certificate_identity</i> &#8211;<code>s </code><i>ca_key</i> [-<code>hU</code> ] [-<code>D </code><i>pkcs11_provider</i> ] [-<code>n </code><i>principals</i> ] [-<code>O </code><i>option</i> ] [-<code>V </code><i>validity_interval</i> ] [-<code>z </code><i>serial_number</i> ] <i>file &#8230;</i><br />
<code>ssh-keygen</code> &#8211;<code>L</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>A</code> [-<code>a </code><i>rounds</i> ] [-<code>f </code><i>prefix_path</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>k</code> &#8211;<code>f </code><i>krl_file</i> [-<code>u</code> ] [-<code>s </code><i>ca_public</i> ] [-<code>z </code><i>version_number</i> ] <i>file &#8230;</i><br />
<code>ssh-keygen</code> &#8211;<code>Q</code> [-<code>l</code> ] &#8211;<code>f </code><i>krl_file</i> <i>file &#8230;</i><br />
<code>ssh-keygen</code> &#8211;<code>Y find-principals</code> [-<code>O </code><i>option</i> ] &#8211;<code>s </code><i>signature_file</i> &#8211;<code>f </code><i>allowed_signers_file</i><br />
<code>ssh-keygen</code> &#8211;<code>Y match-principals</code> &#8211;<code>I </code><i>signer_identity</i> &#8211;<code>f </code><i>allowed_signers_file</i><br />
<code>ssh-keygen</code> &#8211;<code>Y check-novalidate</code> [-<code>O </code><i>option</i> ] &#8211;<code>n </code><i>namespace</i> &#8211;<code>s </code><i>signature_file</i><br />
<code>ssh-keygen</code> &#8211;<code>Y sign</code> [-<code>O </code><i>option</i> ] &#8211;<code>f </code><i>key_file</i> &#8211;<code>n </code><i>namespace</i> <i>file &#8230;</i><br />
<code>ssh-keygen</code> &#8211;<code>Y verify</code> [-<code>O </code><i>option</i> ] &#8211;<code>f </code><i>allowed_signers_file</i> &#8211;<code>I </code><i>signer_identity</i> &#8211;<code>n </code><i>namespace</i> &#8211;<code>s </code><i>signature_file</i> [-<code>r </code><i>revocation_file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-keygen</code> generates, manages and converts authentication keys for <a href="/docs/linux/man/1-ssh/">ssh</a>(1). <code>ssh-keygen</code> can create keys for use by SSH protocol version 2. </p>
<p> The type of key to be generated is specified with the &#8211;<code>t</code> option. If invoked without any arguments, <code>ssh-keygen</code> will generate an RSA key. </p>
<p> <code>ssh-keygen</code> is also used to generate groups for use in Diffie-Hellman group exchange (DH-GEX). See the Sx MODULI GENERATION section for details. </p>
<p> Finally, <code>ssh-keygen</code> can be used to generate and update Key Revocation Lists, and to test whether given keys have been revoked by one. See the Sx KEY REVOCATION LISTS section for details. </p>
<p> Normally each user wishing to use SSH with public key authentication runs this once to create the authentication key in ~/.ssh/id_dsa ~/.ssh/id_ecdsa ~/.ssh/id_ecdsa_sk ~/.ssh/id_ed25519 ~/.ssh/id_ed25519_sk or ~/.ssh/id_rsa Additionally, the system administrator may use this to generate host keys. </p>
<p> Normally this program generates the key and asks for a file in which to store the private key. The public key is stored in a file with the same name but &#8220;.pub&#8221; appended. The program also asks for a passphrase. The passphrase may be empty to indicate no passphrase (host keys must have an empty passphrase), or it may be a string of arbitrary length. A passphrase is similar to a password, except it can be a phrase with a series of words, punctuation, numbers, whitespace, or any string of characters you want. Good passphrases are 10-30 characters long, are not simple sentences or otherwise easily guessable (English prose has only 1-2 bits of entropy per character, and provides very bad passphrases), and contain a mix of upper and lowercase letters, numbers, and non-alphanumeric characters. The passphrase can be changed later by using the &#8211;<code>p</code> option. </p>
<p> There is no way to recover a lost passphrase. If the passphrase is lost or forgotten, a new key must be generated and the corresponding public key copied to other machines. </p>
<p> <code>ssh-keygen</code> will by default write keys in an OpenSSH-specific format. This format is preferred as it offers better protection for keys at rest as well as allowing storage of key comments within the private key file itself. The key comment may be useful to help identify the key. The comment is initialized to &#8220;user [at] host&#8221; when the key is created, but can be changed using the &#8211;<code>c</code> option. </p>
<p> It is still possible for <code>ssh-keygen</code> to write the previously-used PEM format private keys using the &#8211;<code>m</code> flag. This may be used when generating new keys, and existing new-format keys may be converted using this option in conjunction with the &#8211;<code>p</code> (change passphrase) flag. </p>
<p> After a key is generated, <code>ssh-keygen</code> will ask where the keys should be placed to be activated. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-A</code></p>
<dd> For each of the key types (rsa, dsa, ecdsa and ed25519) for which host keys do not exist, generate the host keys with the default key file path, an empty passphrase, default bits for the key type, and default comment. If &#8211;<code>f</code> has also been specified, its argument is used as a prefix to the default path for the resulting host key files. This is used by system administration scripts to generate new host keys.</p>
<dt><code>-a </code><i>rounds</i></p>
<dd> When saving a private key, this option specifies the number of KDF (key derivation function, currently bcrypt_pbkdf3) rounds used. Higher numbers result in slower passphrase verification and increased resistance to brute-force password cracking (should the keys be stolen). The default is 16 rounds.</p>
<dt><code>-B</code></p>
<dd> Show the bubblebabble digest of specified private or public key file.</p>
<dt><code>-b </code><i>bits</i></p>
<dd> Specifies the number of bits in the key to create. For RSA keys, the minimum size is 1024 bits and the default is 3072 bits. Generally, 3072 bits is considered sufficient. DSA keys must be exactly 1024 bits as specified by FIPS 186-2. For ECDSA keys, the &#8211;<code>b</code> flag determines the key length by selecting from one of three elliptic curve sizes: 256, 384 or 521 bits. Attempting to use bit lengths other than these three values for ECDSA keys will fail. ECDSA-SK, Ed25519 and Ed25519-SK keys have a fixed length and the &#8211;<code>b</code> flag will be ignored.</p>
<dt><code>-C </code><i>comment</i></p>
<dd> Provides a new comment.</p>
<dt><code>-c</code></p>
<dd> Requests changing the comment in the private and public key files. The program will prompt for the file containing the private keys, for the passphrase if the key has one, and for the new comment.</p>
<dt><code>-D </code><i>pkcs11</i></p>
<dd> Download the public keys provided by the PKCS#11 shared library <i>pkcs11</i> When used in combination with &#8211;<code>s</code> this option indicates that a CA key resides in a PKCS#11 token (see the Sx CERTIFICATES section for details).</p>
<dt><code>-E </code><i>fingerprint_hash</i></p>
<dd> Specifies the hash algorithm used when displaying key fingerprints. Valid options are: &#8220;md5&#8221; and &#8220;sha256&#8221; The default is &#8220;sha256&#8221;</p>
<dt><code>-e</code></p>
<dd> This option will read a private or public OpenSSH key file and print to stdout a public key in one of the formats specified by the &#8211;<code>m</code> option. The default export format is &#8220;RFC4716&#8221; This option allows exporting OpenSSH keys for use by other programs, including several commercial SSH implementations.</p>
<dt><code>-F </code><i>hostname | [hostname]:port</i></p>
<dd> Search for the specified <i>hostname</i> (with optional port number) in a known_hosts file, listing any occurrences found. This option is useful to find hashed host names or addresses and may also be used in conjunction with the &#8211;<code>H</code> option to print found keys in a hashed format.</p>
<dt><code>-f </code><i>filename</i></p>
<dd> Specifies the filename of the key file.</p>
<dt><code>-g</code></p>
<dd> Use generic DNS format when printing fingerprint resource records using the &#8211;<code>r</code> command.</p>
<dt><code>-H</code></p>
<dd> Hash a known_hosts file. This replaces all hostnames and addresses with hashed representations within the specified file; the original content is moved to a file with a .old suffix. These hashes may be used normally by <code>ssh</code> and <code>sshd</code> but they do not reveal identifying information should the file&#8217;s contents be disclosed. This option will not modify existing hashed hostnames and is therefore safe to use on files that mix hashed and non-hashed names.</p>
<dt><code>-h</code></p>
<dd> When signing a key, create a host certificate instead of a user certificate. See the Sx CERTIFICATES section for details.</p>
<dt><code>-I </code><i>certificate_identity</i></p>
<dd> Specify the key identity when signing a public key. See the Sx CERTIFICATES section for details.</p>
<dt><code>-i</code></p>
<dd> This option will read an unencrypted private (or public) key file in the format specified by the &#8211;<code>m</code> option and print an OpenSSH compatible private (or public) key to stdout. This option allows importing keys from other software, including several commercial SSH implementations. The default import format is &#8220;RFC4716&#8221;</p>
<dt><code>-K</code></p>
<dd> Download resident keys from a FIDO authenticator. Public and private key files will be written to the current directory for each downloaded key. If multiple FIDO authenticators are attached, keys will be downloaded from the first touched authenticator.</p>
<dt><code>-k</code></p>
<dd> Generate a KRL file. In this mode, <code>ssh-keygen</code> will generate a KRL file at the location specified via the &#8211;<code>f</code> flag that revokes every key or certificate presented on the command line. Keys/certificates to be revoked may be specified by public key file or using the format described in the Sx KEY REVOCATION LISTS section.</p>
<dt><code>-L</code></p>
<dd> Prints the contents of one or more certificates.</p>
<dt><code>-l</code></p>
<dd> Show fingerprint of specified public key file. For RSA and DSA keys <code>ssh-keygen</code> tries to find the matching public key file and prints its fingerprint. If combined with &#8211;<code>v</code> a visual ASCII art representation of the key is supplied with the fingerprint.</p>
<dt><code>-M generate</code></p>
<dd> Generate candidate Diffie-Hellman Group Exchange (DH-GEX) parameters for eventual use by the `diffie-hellman-group-exchange-*&#8217; key exchange methods. The numbers generated by this operation must be further screened before use. See the Sx MODULI GENERATION section for more information.</p>
<dt><code>-M screen</code></p>
<dd> Screen candidate parameters for Diffie-Hellman Group Exchange. This will accept a list of candidate numbers and test that they are safe (Sophie Germain) primes with acceptable group generators. The results of this operation may be added to the /etc/ssh/moduli file. See the Sx MODULI GENERATION section for more information.</p>
<dt><code>-m </code><i>key_format</i></p>
<dd> Specify a key format for key generation, the &#8211;<code>i</code> (import), &#8211;<code>e</code> (export) conversion options, and the &#8211;<code>p</code> change passphrase operation. The latter may be used to convert between OpenSSH private key and PEM private key formats. The supported key formats are: &#8220;RFC4716&#8221; (RFC 4716/SSH2 public or private key), &#8220;PKCS8&#8221; (PKCS8 public or private key) or &#8220;PEM&#8221; (PEM public key). By default OpenSSH will write newly-generated private keys in its own format, but when converting public keys for export the default format is &#8220;RFC4716&#8221; Setting a format of &#8220;PEM&#8221; when generating or updating a supported private key type will cause the key to be stored in the legacy PEM private key format.</p>
<dt><code>-N </code><i>new_passphrase</i></p>
<dd> Provides the new passphrase.</p>
<dt><code>-n </code><i>principals</i></p>
<dd> Specify one or more principals (user or host names) to be included in a certificate when signing a key. Multiple principals may be specified, separated by commas. See the Sx CERTIFICATES section for details.</p>
<dt><code>-O </code><i>option</i></p>
<dd> Specify a key/value option. These are specific to the operation that <code>ssh-keygen</code> has been requested to perform. </p>
<p> When signing certificates, one of the options listed in the Sx CERTIFICATES section may be specified here. </p>
<p> When performing moduli generation or screening, one of the options listed in the Sx MODULI GENERATION section may be specified. </p>
<p> When generating a key that will be hosted on a FIDO authenticator, this flag may be used to specify key-specific options. Those supported at present are:</p>
<dl>
<dt><code>application</code></p>
<dd> Override the default FIDO application/origin string of &#8220;ssh:&#8221; This may be useful when generating host or domain-specific resident keys. The specified application string must begin with &#8220;ssh:&#8221;</p>
<dt><code>challenge = </code><i>path</i></p>
<dd> Specifies a path to a challenge string that will be passed to the FIDO token during key generation. The challenge string may be used as part of an out-of-band protocol for key enrollment (a random challenge is used by default).</p>
<dt><code>device</code></p>
<dd> Explicitly specify a <a href="/docs/linux/man/4-fido/">fido</a>(4) device to use, rather than letting the token middleware select one.</p>
<dt><code>no-touch-required</code></p>
<dd> Indicate that the generated private key should not require touch events (user presence) when making signatures. Note that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse such signatures by default, unless overridden via an authorized_keys option.</p>
<dt><code>resident</code></p>
<dd> Indicate that the key should be stored on the FIDO authenticator itself. Resident keys may be supported on FIDO2 tokens and typically require that a PIN be set on the token prior to generation. Resident keys may be loaded off the token using ssh-add1.</p>
<dt><code>user</code></p>
<dd> A username to be associated with a resident key, overriding the empty default username. Specifying a username may be useful when generating multiple resident keys for the same application name.</p>
<dt><code>verify-required</code></p>
<dd> Indicate that this private key should require user verification for each signature. Not all FIDO tokens support this option. Currently PIN authentication is the only supported verification method, but other methods may be supported in the future.</p>
<dt><code>write-attestation = </code><i>path</i></p>
<dd> May be used at key generation time to record the attestation data returned from FIDO tokens during key generation. This information is potentially sensitive. By default, this information is discarded.</dl>
<p> When performing signature-related options using the &#8211;<code>Y</code> flag, the following options are accepted:</p>
<dl>
<dt><code>hashalg = </code><i>algorithm</i></p>
<dd> Selects the hash algorithm to use for hashing the message to be signed. Valid algorithms are &#8220;sha256&#8221; and &#8220;sha512.&#8221; The default is &#8220;sha512.&#8221;</p>
<dt><code>print-pubkey</code></p>
<dd> Print the full public key to standard output after signature verification.</p>
<dt><code>verify-time = </code><i>timestamp</i></p>
<dd> Specifies a time to use when validating signatures instead of the current time. The time may be specified as a date in YYYYMMDD format or a time in YYYYMMDDHHMM[SS] format.</dl>
<p> The &#8211;<code>O</code> option may be specified multiple times.</p>
<dt><code>-P </code><i>passphrase</i></p>
<dd> Provides the (old) passphrase.</p>
<dt><code>-p</code></p>
<dd> Requests changing the passphrase of a private key file instead of creating a new private key. The program will prompt for the file containing the private key, for the old passphrase, and twice for the new passphrase.</p>
<dt><code>-Q</code></p>
<dd> Test whether keys have been revoked in a KRL. If the &#8211;<code>l</code> option is also specified then the contents of the KRL will be printed.</p>
<dt><code>-q</code></p>
<dd> Silence <code>ssh-keygen</code></p>
<dt><code>-R </code><i>hostname | [hostname]:port</i></p>
<dd> Removes all keys belonging to the specified <i>hostname</i> (with optional port number) from a known_hosts file. This option is useful to delete hashed hosts (see the &#8211;<code>H</code> option above).</p>
<dt><code>-r </code><i>hostname</i></p>
<dd> Print the SSHFP fingerprint resource record named <i>hostname</i> for the specified public key file.</p>
<dt><code>-s </code><i>ca_key</i></p>
<dd> Certify (sign) a public key using the specified CA key. See the Sx CERTIFICATES section for details. </p>
<p> When generating a KRL, &#8211;<code>s</code> specifies a path to a CA public key file used to revoke certificates directly by key ID or serial number. See the Sx KEY REVOCATION LISTS section for details.</p>
<dt><code>-t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa</code></p>
<dd> Specifies the type of key to create. The possible values are &#8220;dsa&#8221; &#8220;ecdsa&#8221; &#8220;ecdsa-sk&#8221; &#8220;ed25519&#8221; &#8220;ed25519-sk&#8221; or &#8220;rsa&#8221; </p>
<p> This flag may also be used to specify the desired signature type when signing certificates using an RSA CA key. The available RSA signature variants are &#8220;ssh-rsa&#8221; (SHA1 signatures, not recommended), &#8220;rsa-sha2-256&#8221; and &#8220;rsa-sha2-512&#8221; (the default).</p>
<dt><code>-U</code></p>
<dd> When used in combination with &#8211;<code>s</code> this option indicates that a CA key resides in a ssh-agent1. See the Sx CERTIFICATES section for more information.</p>
<dt><code>-u</code></p>
<dd> Update a KRL. When specified with &#8211;<code>k</code> keys listed via the command line are added to the existing KRL rather than a new KRL being created.</p>
<dt><code>-V </code><i>validity_interval</i></p>
<dd> Specify a validity interval when signing a certificate. A validity interval may consist of a single time, indicating that the certificate is valid beginning now and expiring at that time, or may consist of two times separated by a colon to indicate an explicit time interval. </p>
<p> The start time may be specified as the string &#8220;always&#8221; to indicate the certificate has no specified start time, a date in YYYYMMDD format, a time in YYYYMMDDHHMM[SS] format, a relative time (to the current time) consisting of a minus sign followed by an interval in the format described in the TIME FORMATS section of sshd_config5. </p>
<p> The end time may be specified as a YYYYMMDD date, a YYYYMMDDHHMM[SS] time, a relative time starting with a plus character or the string &#8220;forever&#8221; to indicate that the certificate has no expiry date. </p>
<p> For example: &#8220;+52w1d&#8221; (valid from now to 52 weeks and one day from now), &#8220;-4w:+4w&#8221; (valid from four weeks ago to four weeks from now), &#8220;20100101123000:20110101123000&#8221; (valid from 12:30 PM, January 1st, 2010 to 12:30 PM, January 1st, 2011), &#8220;-1d:20110101&#8221; (valid from yesterday to midnight, January 1st, 2011), &#8220;-1m:forever&#8221; (valid from one minute ago and never expiring).</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Causes <code>ssh-keygen</code> to print debugging messages about its progress. This is helpful for debugging moduli generation. Multiple &#8211;<code>v</code> options increase the verbosity. The maximum is 3.</p>
<dt><code>-w </code><i>provider</i></p>
<dd> Specifies a path to a library that will be used when creating FIDO authenticator-hosted keys, overriding the default of using the internal USB HID support.</p>
<dt><code>-Y find-principals</code></p>
<dd> Find the principal(s) associated with the public key of a signature, provided using the &#8211;<code>s</code> flag in an authorized signers file provided using the &#8211;<code>f</code> flag. The format of the allowed signers file is documented in the Sx ALLOWED SIGNERS section below. If one or more matching principals are found, they are returned on standard output.</p>
<dt><code>-Y match-principals</code></p>
<dd> Find principal matching the principal name provided using the &#8211;<code>I</code> flag in the authorized signers file specified using the &#8211;<code>f</code> flag. If one or more matching principals are found, they are returned on standard output.</p>
<dt><code>-Y check-novalidate</code></p>
<dd> Checks that a signature generated using <code>ssh-keygen</code> &#8211;<code>Y sign</code> has a valid structure. This does not validate if a signature comes from an authorized signer. When testing a signature, <code>ssh-keygen</code> accepts a message on standard input and a signature namespace using &#8211;<code>n</code> A file containing the corresponding signature must also be supplied using the &#8211;<code>s</code> flag. Successful testing of the signature is signalled by <code>ssh-keygen</code> returning a zero exit status.</p>
<dt><code>-Y sign</code></p>
<dd> Cryptographically sign a file or some data using a SSH key. When signing, <code>ssh-keygen</code> accepts zero or more files to sign on the command-line &#8211; if no files are specified then <code>ssh-keygen</code> will sign data presented on standard input. Signatures are written to the path of the input file with &#8220;.sig&#8221; appended, or to standard output if the message to be signed was read from standard input. </p>
<p> The key used for signing is specified using the &#8211;<code>f</code> option and may refer to either a private key, or a public key with the private half available via ssh-agent1. An additional signature namespace, used to prevent signature confusion across different domains of use (e.g. file signing vs email signing) must be provided via the &#8211;<code>n</code> flag. Namespaces are arbitrary strings, and may include: &#8220;file&#8221; for file signing, &#8220;email&#8221; for email signing. For custom uses, it is recommended to use names following a NAMESPACE [at] YOUR.DOMAIN pattern to generate unambiguous namespaces.</p>
<dt><code>-Y verify</code></p>
<dd> Request to verify a signature generated using <code>ssh-keygen</code> &#8211;<code>Y sign</code> as described above. When verifying a signature, <code>ssh-keygen</code> accepts a message on standard input and a signature namespace using &#8211;<code>n</code> A file containing the corresponding signature must also be supplied using the &#8211;<code>s</code> flag, along with the identity of the signer using &#8211;<code>I</code> and a list of allowed signers via the &#8211;<code>f</code> flag. The format of the allowed signers file is documented in the Sx ALLOWED SIGNERS section below. A file containing revoked keys can be passed using the &#8211;<code>r</code> flag. The revocation file may be a KRL or a one-per-line list of public keys. Successful verification by an authorized signer is signalled by <code>ssh-keygen</code> returning a zero exit status.</p>
<dt><code>-y</code></p>
<dd> This option will read a private OpenSSH format file and print an OpenSSH public key to stdout.</p>
<dt><code>-Z </code><i>cipher</i></p>
<dd> Specifies the cipher to use for encryption when writing an OpenSSH-format private key file. The list of available ciphers may be obtained using Qq ssh -Q cipher . The default is &#8220;aes256-ctr&#8221;</p>
<dt><code>-z </code><i>serial_number</i></p>
<dd> Specifies a serial number to be embedded in the certificate to distinguish this certificate from others from the same CA. If the <i>serial_number</i> is prefixed with a `+&#8217; character, then the serial number will be incremented for each certificate signed on a single command-line. The default serial number is zero. </p>
<p> When generating a KRL, the &#8211;<code>z</code> flag is used to specify a KRL version number.</dl>
<h2>MODULI GENERATION</h2>
<p> <code>ssh-keygen</code> may be used to generate groups for the Diffie-Hellman Group Exchange (DH-GEX) protocol. Generating these groups is a two-step process: first, candidate primes are generated using a fast, but memory intensive process. These candidate primes are then tested for suitability (a CPU-intensive process). </p>
<p> Generation of primes is performed using the &#8211;<code>M generate</code> option. The desired length of the primes may be specified by the &#8211;<code>O bits</code> option. For example: </p>
<blockquote><p><tt># ssh-keygen -M generate -O bits=2048 moduli-2048.candidates</tt></p></blockquote>
<p> By default, the search for primes begins at a random point in the desired length range. This may be overridden using the &#8211;<code>O start</code> option, which specifies a different start point (in hex). </p>
<p> Once a set of candidates have been generated, they must be screened for suitability. This may be performed using the &#8211;<code>M screen</code> option. In this mode <code>ssh-keygen</code> will read candidates from standard input (or a file specified using the &#8211;<code>f</code> option). For example: </p>
<blockquote><p><tt># ssh-keygen -M screen -f moduli-2048.candidates moduli-2048</tt></p></blockquote>
<p> By default, each candidate will be subjected to 100 primality tests. This may be overridden using the &#8211;<code>O prime-tests</code> option. The DH generator value will be chosen automatically for the prime under consideration. If a specific generator is desired, it may be requested using the &#8211;<code>O generator</code> option. Valid generator values are 2, 3, and 5. </p>
<p> Screened DH groups may be installed in /etc/ssh/moduli It is important that this file contains moduli of a range of bit lengths. </p>
<p> A number of options are available for moduli generation and screening via the &#8211;<code>O</code> flag:</p>
<dl>
<dt><code>lines = </code><i>number</i></p>
<dd> Exit after screening the specified number of lines while performing DH candidate screening.</p>
<dt><code>start-line = </code><i>line-number</i></p>
<dd> Start screening at the specified line number while performing DH candidate screening.</p>
<dt><code>checkpoint = </code><i>filename</i></p>
<dd> Write the last line processed to the specified file while performing DH candidate screening. This will be used to skip lines in the input file that have already been processed if the job is restarted.</p>
<dt><code>memory = </code><i>mbytes</i></p>
<dd> Specify the amount of memory to use (in megabytes) when generating candidate moduli for DH-GEX.</p>
<dt><code>start = </code><i>hex-value</i></p>
<dd> Specify start point (in hex) when generating candidate moduli for DH-GEX.</p>
<dt><code>generator = </code><i>value</i></p>
<dd> Specify desired generator (in decimal) when testing candidate moduli for DH-GEX.</dl>
<h2>CERTIFICATES</h2>
<p> <code>ssh-keygen</code> supports signing of keys to produce certificates that may be used for user or host authentication. Certificates consist of a public key, some identity information, zero or more principal (user or host) names and a set of options that are signed by a Certification Authority (CA) key. Clients or servers may then trust only the CA key and verify its signature on a certificate rather than trusting many user/host keys. Note that OpenSSH certificates are a different, and much simpler, format to the X.509 certificates used in <a href="/docs/linux/man/8-ssl/">ssl</a>(8). </p>
<p> <code>ssh-keygen</code> supports two types of certificates: user and host. User certificates authenticate users to servers, whereas host certificates authenticate server hosts to users. To generate a user certificate: </p>
<blockquote><p><tt>$ ssh-keygen -s /path/to/ca_key -I key_id /path/to/user_key.pub</tt></p></blockquote>
<p> The resultant certificate will be placed in /path/to/user_key-cert.pub A host certificate requires the &#8211;<code>h</code> option: </p>
<blockquote><p><tt>$ ssh-keygen -s /path/to/ca_key -I key_id -h /path/to/host_key.pub</tt></p></blockquote>
<p> The host certificate will be output to /path/to/host_key-cert.pub </p>
<p> It is possible to sign using a CA key stored in a PKCS#11 token by providing the token library using &#8211;<code>D</code> and identifying the CA key by providing its public half as an argument to &#8211;<code>s</code> </p>
<blockquote><p><tt>$ ssh-keygen -s ca_key.pub -D libpkcs11.so -I key_id user_key.pub</tt></p></blockquote>
<p> Similarly, it is possible for the CA key to be hosted in a ssh-agent1. This is indicated by the &#8211;<code>U</code> flag and, again, the CA key must be identified by its public half. </p>
<blockquote><p><tt>$ ssh-keygen -Us </tt>ca_key.pub -I key_id user_key.pub </p></blockquote>
<p> In all cases, <i>key_id</i> is a &quot;key identifier&quot; that is logged by the server when the certificate is used for authentication. </p>
<p> Certificates may be limited to be valid for a set of principal (user/host) names. By default, generated certificates are valid for all users or hosts. To generate a certificate for a specified set of principals: </p>
<blockquote><p><tt>$ ssh-keygen -s ca_key -I key_id -n user1,user2 user_key.pub</tt></p></blockquote>
<blockquote><p><tt>&quot;$ ssh-keygen -s ca_key -I key_id -h -n host.domain host_key.pub&quot;</tt></p></blockquote>
<p> Additional limitations on the validity and use of user certificates may be specified through certificate options. A certificate option may disable features of the SSH session, may be valid only when presented from particular source addresses or may force the use of a specific command. </p>
<p> The options that are valid for user certificates are: </p>
<dl>
<dt><code>clear</code></p>
<dd> Clear all enabled permissions. This is useful for clearing the default set of permissions so permissions may be added individually. </p>
<dt><code>critical : </code><i>name </i>[<code>= </code><i>contents</i> ]</p>
<dd>
<dt><code>extension : </code><i>name </i>[<code>= </code><i>contents</i> ]</p>
<dd> Includes an arbitrary certificate critical option or extension. The specified <i>name</i> should include a domain suffix, e.g. &#8220;name [at] example.com&#8221; If <i>contents</i> is specified then it is included as the contents of the extension/option encoded as a string, otherwise the extension/option is created with no contents (usually indicating a flag). Extensions may be ignored by a client or server that does not recognise them, whereas unknown critical options will cause the certificate to be refused. </p>
<dt><code>force-command = </code><i>command</i></p>
<dd> Forces the execution of <i>command</i> instead of any shell or command specified by the user when the certificate is used for authentication. </p>
<dt><code>no-agent-forwarding</code></p>
<dd> Disable ssh-agent1 forwarding (permitted by default). </p>
<dt><code>no-port-forwarding</code></p>
<dd> Disable port forwarding (permitted by default). </p>
<dt><code>no-pty</code></p>
<dd> Disable PTY allocation (permitted by default). </p>
<dt><code>no-user-rc</code></p>
<dd> Disable execution of ~/.ssh/rc by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) (permitted by default). </p>
<dt><code>no-x11-forwarding</code></p>
<dd> Disable X11 forwarding (permitted by default). </p>
<dt><code>permit-agent-forwarding</code></p>
<dd> Allows ssh-agent1 forwarding. </p>
<dt><code>permit-port-forwarding</code></p>
<dd> Allows port forwarding. </p>
<dt><code>permit-pty</code></p>
<dd> Allows PTY allocation. </p>
<dt><code>permit-user-rc</code></p>
<dd> Allows execution of ~/.ssh/rc by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). </p>
<dt><code>permit-X11-forwarding</code></p>
<dd> Allows X11 forwarding. </p>
<dt><code>no-touch-required</code></p>
<dd> Do not require signatures made using this key include demonstration of user presence (e.g. by having the user touch the authenticator). This option only makes sense for the FIDO authenticator algorithms <code>ecdsa-sk</code> and <code>ed25519-sk</code> </p>
<dt><code>source-address = </code><i>address_list</i></p>
<dd> Restrict the source addresses from which the certificate is considered valid. The <i>address_list</i> is a comma-separated list of one or more address/netmask pairs in CIDR format. </p>
<dt><code>verify-required</code></p>
<dd> Require signatures made using this key indicate that the user was first verified. This option only makes sense for the FIDO authenticator algorithms <code>ecdsa-sk</code> and <code>ed25519-sk</code> Currently PIN authentication is the only supported verification method, but other methods may be supported in the future.</dl>
<p> At present, no standard options are valid for host keys. </p>
<p> Finally, certificates may be defined with a validity lifetime. The &#8211;<code>V</code> option allows specification of certificate start and end times. A certificate that is presented at a time outside this range will not be considered valid. By default, certificates are valid from the UNIX Epoch to the distant future. </p>
<p> For certificates to be used for user or host authentication, the CA public key must be trusted by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) or <a href="/docs/linux/man/1-ssh/">ssh</a>(1). Refer to those manual pages for details.</p>
<h2>KEY REVOCATION LISTS</h2>
<p> <code>ssh-keygen</code> is able to manage OpenSSH format Key Revocation Lists (KRLs). These binary files specify keys or certificates to be revoked using a compact format, taking as little as one bit per certificate if they are being revoked by serial number. </p>
<p> KRLs may be generated using the &#8211;<code>k</code> flag. This option reads one or more files from the command line and generates a new KRL. The files may either contain a KRL specification (see below) or public keys, listed one per line. Plain public keys are revoked by listing their hash or contents in the KRL and certificates revoked by serial number or key ID (if the serial is zero or not available). </p>
<p> Revoking keys using a KRL specification offers explicit control over the types of record used to revoke keys and may be used to directly revoke certificates by serial number or key ID without having the complete original certificate on hand. A KRL specification consists of lines containing one of the following directives followed by a colon and some directive-specific information.</p>
<dl>
<dt><code>serial : </code><i>serial_number </i>[- <i>serial_number</i> ]</p>
<dd> Revokes a certificate with the specified serial number. Serial numbers are 64-bit values, not including zero and may be expressed in decimal, hex or octal. If two serial numbers are specified separated by a hyphen, then the range of serial numbers including and between each is revoked. The CA key must have been specified on the <code>ssh-keygen</code> command line using the &#8211;<code>s</code> option.</p>
<dt><code>id : </code><i>key_id</i></p>
<dd> Revokes a certificate with the specified key ID string. The CA key must have been specified on the <code>ssh-keygen</code> command line using the &#8211;<code>s</code> option.</p>
<dt><code>key : </code><i>public_key</i></p>
<dd> Revokes the specified key. If a certificate is listed, then it is revoked as a plain public key.</p>
<dt><code>sha1 : </code><i>public_key</i></p>
<dd> Revokes the specified key by including its SHA1 hash in the KRL.</p>
<dt><code>sha256 : </code><i>public_key</i></p>
<dd> Revokes the specified key by including its SHA256 hash in the KRL. KRLs that revoke keys by SHA256 hash are not supported by OpenSSH versions prior to 7.9.</p>
<dt><code>hash : </code><i>fingerprint</i></p>
<dd> Revokes a key using a fingerprint hash, as obtained from a <a href="/docs/linux/man/8-sshd/">sshd</a>(8) authentication log message or the <code>ssh-keygen</code> &#8211;<code>l</code> flag. Only SHA256 fingerprints are supported here and resultant KRLs are not supported by OpenSSH versions prior to 7.9.</dl>
<p> KRLs may be updated using the &#8211;<code>u</code> flag in addition to &#8211;<code>k</code> When this option is specified, keys listed via the command line are merged into the KRL, adding to those already there. </p>
<p> It is also possible, given a KRL, to test whether it revokes a particular key (or keys). The &#8211;<code>Q</code> flag will query an existing KRL, testing each key specified on the command line. If any key listed on the command line has been revoked (or an error encountered) then <code>ssh-keygen</code> will exit with a non-zero exit status. A zero exit status will only be returned if no key was revoked.</p>
<h2>ALLOWED SIGNERS</h2>
<p> When verifying signatures, <code>ssh-keygen</code> uses a simple list of identities and keys to determine whether a signature comes from an authorized source. This &quot;allowed signers&quot; file uses a format patterned after the AUTHORIZED_KEYS FILE FORMAT described in <a href="/docs/linux/man/8-sshd/">sshd</a>(8). Each line of the file contains the following space-separated fields: principals, options, keytype, base64-encoded key. Empty lines and lines starting with a `#&#8217; are ignored as comments. </p>
<p> The principals field is a pattern-list (see PATTERNS in ssh_config5) consisting of one or more comma-separated USER [at] DOMAIN identity patterns that are accepted for signing. When verifying, the identity presented via the &#8211;<code>I</code> option must match a principals pattern in order for the corresponding key to be considered acceptable for verification. </p>
<p> The options (if present) consist of comma-separated option specifications. No spaces are permitted, except within double quotes. The following option specifications are supported (note that option keywords are case-insensitive):</p>
<dl>
<dt><code>cert-authority</code></p>
<dd> Indicates that this key is accepted as a certificate authority (CA) and that certificates signed by this CA may be accepted for verification.</p>
<dt><code>namespaces = namespace-list</code></p>
<dd> Specifies a pattern-list of namespaces that are accepted for this key. If this option is present, the signature namespace embedded in the signature object and presented on the verification command-line must match the specified list before the key will be considered acceptable.</p>
<dt><code>valid-after = timestamp</code></p>
<dd> Indicates that the key is valid for use at or after the specified timestamp, which may be a date in YYYYMMDD format or a time in YYYYMMDDHHMM[SS] format.</p>
<dt><code>valid-before = timestamp</code></p>
<dd> Indicates that the key is valid for use at or before the specified timestamp.</dl>
<p> When verifying signatures made by certificates, the expected principal name must match both the principals pattern in the allowed signers file and the principals embedded in the certificate itself. </p>
<p> An example allowed signers file: </p>
<pre><code>
#Comments allowed at start of line
user1[at] example.com, user2[at] example.com ssh - rsa AAAAX1...
#A certificate authority, trusted for all principals in a domain.
                                                       *@example.com cert -
                           authority ssh - ed25519 AAAB4...
#A key that is accepted only for file signing.
                                           user2[at] example.com namespaces = "file" ssh - ed25519 AAA41...
</code></pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SSH_SK_PROVIDER</code></p>
<dd> Specifies a path to a library that will be used when loading any FIDO authenticator-hosted keys, overriding the default of using the built-in USB HID support.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.ssh/id_dsa </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa_sk </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519 </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519_sk </code></p>
<dd>
<dt><code>~/.ssh/id_rsa </code></p>
<dd> Contains the DSA, ECDSA, authenticator-hosted ECDSA, Ed25519, authenticator-hosted Ed25519 or RSA authentication identity of the user. This file should not be readable by anyone but the user. It is possible to specify a passphrase when generating the key; that passphrase will be used to encrypt the private part of this file using 128-bit AES. This file is not automatically accessed by <code>ssh-keygen</code> but it is offered as the default file for the private key. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will read this file when a login attempt is made. </p>
<dt><code>~/.ssh/id_dsa.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa_sk.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519_sk.pub </code></p>
<dd>
<dt><code>~/.ssh/id_rsa.pub </code></p>
<dd> Contains the DSA, ECDSA, authenticator-hosted ECDSA, Ed25519, authenticator-hosted Ed25519 or RSA public key for authentication. The contents of this file should be added to ~/.ssh/authorized_keys on all machines where the user wishes to log in using public key authentication. There is no need to keep the contents of this file secret. </p>
<dt><code>/etc/ssh/moduli </code></p>
<dd> Contains Diffie-Hellman groups used for DH-GEX. The file format is described in <a href="/docs/linux/man/5-moduli/">moduli</a>(5).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, <a href="/docs/linux/man/5-moduli/">moduli</a>(5), <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<dl>
<dt>
<dd> <i>RFC 4716</i> <i>&quot;The Secure Shell (SSH) Public Key File Format&quot;</i> 2006</dl>
<h2>AUTHORS</h2>
<p> OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. </p>
<h2>Index</h2>
