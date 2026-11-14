---
title: "gsissh-keygen(1)"
name: "gsissh-keygen"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsissh-keygen/"
description: "ssh-keygen – authentication key generation, management and conversion"
---

<h2>NAME</h2>
<p> <code>ssh-keygen</code> &#8211; authentication key generation, management and conversion</p>
<h2>SYNOPSIS</h2>
<p> -words <code>ssh-keygen</code> [-<code>q</code> ] [-<code>b </code><i>bits</i> ] [-<code>t </code><i>type</i> ] [-<code>N </code><i>new_passphrase</i> ] [-<code>C </code><i>comment</i> ] [-<code>f </code><i>output_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>p</code> [-<code>P </code><i>old_passphrase</i> ] [-<code>N </code><i>new_passphrase</i> ] [-<code>f </code><i>keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>i</code> [-<code>m </code><i>key_format</i> ] [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>e</code> [-<code>m </code><i>key_format</i> ] [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>y</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>c</code> [-<code>P </code><i>passphrase</i> ] [-<code>C </code><i>comment</i> ] [-<code>f </code><i>keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>l</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>B</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>D </code><i>pkcs11</i><br />
<code>ssh-keygen</code> &#8211;<code>F </code><i>hostname</i> [-<code>f </code><i>known_hosts_file</i> ] [-<code>l</code> ]<br />
<code>ssh-keygen</code> &#8211;<code>H</code> [-<code>f </code><i>known_hosts_file</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>R </code><i>hostname</i> [-<code>f </code><i>known_hosts_file</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>r </code><i>hostname</i> [-<code>f </code><i>input_keyfile</i> ] [-<code>g</code> ]<br />
<code>ssh-keygen</code> &#8211;<code>G </code><i>output_file</i> [-<code>v</code> ] [-<code>b </code><i>bits</i> ] [-<code>M </code><i>memory</i> ] [-<code>S </code><i>start_point</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>T </code><i>output_file</i> &#8211;<code>f </code><i>input_file</i> [-<code>v</code> ] [-<code>a </code><i>rounds</i> ] [-<code>J </code><i>num_lines</i> ] [-<code>j </code><i>start_line</i> ] [-<code>K </code><i>checkpt</i> ] [-<code>W </code><i>generator</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>s </code><i>ca_key</i> &#8211;<code>I </code><i>certificate_identity</i> [-<code>h</code> ] [-<code>n </code><i>principals</i> ] [-<code>O </code><i>option</i> ] [-<code>V </code><i>validity_interval</i> ] [-<code>z </code><i>serial_number</i> ] <i>file &#8230;</i><br />
<code>ssh-keygen</code> &#8211;<code>L</code> [-<code>f </code><i>input_keyfile</i> ]<br />
<code>ssh-keygen</code> &#8211;<code>A</code><br />
<code>ssh-keygen</code> &#8211;<code>k</code> &#8211;<code>f </code><i>krl_file</i> [-<code>u</code> ] [-<code>s </code><i>ca_public</i> ] [-<code>z </code><i>version_number</i> ] <i>file &#8230;</i><br />
<code>ssh-keygen</code> &#8211;<code>Q</code> &#8211;<code>f </code><i>krl_file</i> <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-keygen</code> generates, manages and converts authentication keys for <a href="/docs/linux/man/1-ssh/">ssh</a>(1). <code>ssh-keygen</code> can create RSA keys for use by SSH protocol version 1 and DSA, ECDSA, ED25519 or RSA keys for use by SSH protocol version 2. The type of key to be generated is specified with the &#8211;<code>t</code> option. If invoked without any arguments, <code>ssh-keygen</code> will generate an RSA key for use in SSH protocol 2 connections. </p>
<p> <code>ssh-keygen</code> is also used to generate groups for use in Diffie-Hellman group exchange (DH-GEX). See the Sx MODULI GENERATION section for details. </p>
<p> Finally, <code>ssh-keygen</code> can be used to generate and update Key Revocation Lists, and to test whether given keys have been revoked by one. See the Sx KEY REVOCATION LISTS section for details. </p>
<p> Normally each user wishing to use SSH with public key authentication runs this once to create the authentication key in ~/.ssh/identity ~/.ssh/id_dsa ~/.ssh/id_ecdsa ~/.ssh/id_ed25519 or ~/.ssh/id_rsa Additionally, the system administrator may use this to generate host keys, as seen in /etc/rc </p>
<p> Normally this program generates the key and asks for a file in which to store the private key. The public key is stored in a file with the same name but &#8220;.pub&#8221; appended. The program also asks for a passphrase. The passphrase may be empty to indicate no passphrase (host keys must have an empty passphrase), or it may be a string of arbitrary length. A passphrase is similar to a password, except it can be a phrase with a series of words, punctuation, numbers, whitespace, or any string of characters you want. Good passphrases are 10-30 characters long, are not simple sentences or otherwise easily guessable (English prose has only 1-2 bits of entropy per character, and provides very bad passphrases), and contain a mix of upper and lowercase letters, numbers, and non-alphanumeric characters. The passphrase can be changed later by using the &#8211;<code>p</code> option. </p>
<p> There is no way to recover a lost passphrase. If the passphrase is lost or forgotten, a new key must be generated and the corresponding public key copied to other machines. </p>
<p> For RSA1 keys, there is also a comment field in the key file that is only for convenience to the user to help identify the key. The comment can tell what the key is for, or whatever is useful. The comment is initialized to &#8220;user [at] host&#8221; when the key is created, but can be changed using the &#8211;<code>c</code> option. </p>
<p> After a key is generated, instructions below detail where the keys should be placed to be activated. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-A</code></p>
<dd> For each of the key types (rsa1, rsa, dsa, ecdsa and ed25519) for which host keys do not exist, generate the host keys with the default key file path, an empty passphrase, default bits for the key type, and default comment. This is used by /etc/rc to generate new host keys.</p>
<dt><code>-a </code><i>rounds</i></p>
<dd> When saving a new-format private key (i.e. an ed25519 key or any SSH protocol 2 key when the &#8211;<code>o</code> flag is set), this option specifies the number of KDF (key derivation function) rounds used. Higher numbers result in slower passphrase verification and increased resistance to brute-force password cracking (should the keys be stolen). </p>
<p> When screening DH-GEX candidates ( using the &#8211;<code>T</code> command). This option specifies the number of primality tests to perform.</p>
<dt><code>-B</code></p>
<dd> Show the bubblebabble digest of specified private or public key file.</p>
<dt><code>-b </code><i>bits</i></p>
<dd> Specifies the number of bits in the key to create. For RSA keys, the minimum size is 768 bits and the default is 2048 bits. Generally, 2048 bits is considered sufficient. DSA keys must be exactly 1024 bits as specified by FIPS 186-2. For ECDSA keys, the &#8211;<code>b</code> flag determines the key length by selecting from one of three elliptic curve sizes: 256, 384 or 521 bits. Attempting to use bit lengths other than these three values for ECDSA keys will fail. ED25519 keys have a fixed length and the &#8211;<code>b</code> flag will be ignored.</p>
<dt><code>-C </code><i>comment</i></p>
<dd> Provides a new comment.</p>
<dt><code>-c</code></p>
<dd> Requests changing the comment in the private and public key files. This operation is only supported for RSA1 keys. The program will prompt for the file containing the private keys, for the passphrase if the key has one, and for the new comment.</p>
<dt><code>-D </code><i>pkcs11</i></p>
<dd> Download the RSA public keys provided by the PKCS#11 shared library <i>pkcs11</i> When used in combination with &#8211;<code>s</code> this option indicates that a CA key resides in a PKCS#11 token (see the Sx CERTIFICATES section for details).</p>
<dt><code>-e</code></p>
<dd> This option will read a private or public OpenSSH key file and print to stdout the key in one of the formats specified by the &#8211;<code>m</code> option. The default export format is &#8220;RFC4716&#8221; This option allows exporting OpenSSH keys for use by other programs, including several commercial SSH implementations.</p>
<dt><code>-F </code><i>hostname</i></p>
<dd> Search for the specified <i>hostname</i> in a known_hosts file, listing any occurrences found. This option is useful to find hashed host names or addresses and may also be used in conjunction with the &#8211;<code>H</code> option to print found keys in a hashed format.</p>
<dt><code>-f </code><i>filename</i></p>
<dd> Specifies the filename of the key file.</p>
<dt><code>-G </code><i>output_file</i></p>
<dd> Generate candidate primes for DH-GEX. These primes must be screened for safety (using the &#8211;<code>T</code> option) before use.</p>
<dt><code>-g</code></p>
<dd> Use generic DNS format when printing fingerprint resource records using the &#8211;<code>r</code> command.</p>
<dt><code>-H</code></p>
<dd> Hash a known_hosts file. This replaces all hostnames and addresses with hashed representations within the specified file; the original content is moved to a file with a .old suffix. These hashes may be used normally by <code>ssh</code> and <code>sshd</code> but they do not reveal identifying information should the file&#8217;s contents be disclosed. This option will not modify existing hashed hostnames and is therefore safe to use on files that mix hashed and non-hashed names.</p>
<dt><code>-h</code></p>
<dd> When signing a key, create a host certificate instead of a user certificate. Please see the Sx CERTIFICATES section for details.</p>
<dt><code>-I </code><i>certificate_identity</i></p>
<dd> Specify the key identity when signing a public key. Please see the Sx CERTIFICATES section for details.</p>
<dt><code>-i</code></p>
<dd> This option will read an unencrypted private (or public) key file in the format specified by the &#8211;<code>m</code> option and print an OpenSSH compatible private (or public) key to stdout.</p>
<dt><code>-J </code><i>num_lines</i></p>
<dd> Exit after screening the specified number of lines while performing DH candidate screening using the &#8211;<code>T</code> option.</p>
<dt><code>-j </code><i>start_line</i></p>
<dd> Start screening at the specified line number while performing DH candidate screening using the &#8211;<code>T</code> option.</p>
<dt><code>-K </code><i>checkpt</i></p>
<dd> Write the last line processed to the file <i>checkpt</i> while performing DH candidate screening using the &#8211;<code>T</code> option. This will be used to skip lines in the input file that have already been processed if the job is restarted. This option allows importing keys from other software, including several commercial SSH implementations. The default import format is &#8220;RFC4716&#8221;</p>
<dt><code>-k</code></p>
<dd> Generate a KRL file. In this mode, <code>ssh-keygen</code> will generate a KRL file at the location specified via the &#8211;<code>f</code> flag that revokes every key or certificate presented on the command line. Keys/certificates to be revoked may be specified by public key file or using the format described in the Sx KEY REVOCATION LISTS section.</p>
<dt><code>-L</code></p>
<dd> Prints the contents of a certificate.</p>
<dt><code>-l</code></p>
<dd> Show fingerprint of specified public key file. Private RSA1 keys are also supported. For RSA and DSA keys <code>ssh-keygen</code> tries to find the matching public key file and prints its fingerprint. If combined with &#8211;<code>v</code> an ASCII art representation of the key is supplied with the fingerprint.</p>
<dt><code>-M </code><i>memory</i></p>
<dd> Specify the amount of memory to use (in megabytes) when generating candidate moduli for DH-GEX.</p>
<dt><code>-m </code><i>key_format</i></p>
<dd> Specify a key format for the &#8211;<code>i</code> (import) or &#8211;<code>e</code> (export) conversion options. The supported key formats are: &#8220;RFC4716&#8221; (RFC 4716/SSH2 public or private key), &#8220;PKCS8&#8221; (PEM PKCS8 public key) or &#8220;PEM&#8221; (PEM public key). The default conversion format is &#8220;RFC4716&#8221;</p>
<dt><code>-N </code><i>new_passphrase</i></p>
<dd> Provides the new passphrase.</p>
<dt><code>-n </code><i>principals</i></p>
<dd> Specify one or more principals (user or host names) to be included in a certificate when signing a key. Multiple principals may be specified, separated by commas. Please see the Sx CERTIFICATES section for details.</p>
<dt><code>-O </code><i>option</i></p>
<dd> Specify a certificate option when signing a key. This option may be specified multiple times. Please see the Sx CERTIFICATES section for details. The options that are valid for user certificates are:</p>
<dl>
<dt><code>clear</code></p>
<dd> Clear all enabled permissions. This is useful for clearing the default set of permissions so permissions may be added individually.</p>
<dt><code>force-command = </code><i>command</i></p>
<dd> Forces the execution of <i>command</i> instead of any shell or command specified by the user when the certificate is used for authentication.</p>
<dt><code>no-agent-forwarding</code></p>
<dd> Disable ssh-agent1 forwarding (permitted by default).</p>
<dt><code>no-port-forwarding</code></p>
<dd> Disable port forwarding (permitted by default).</p>
<dt><code>no-pty</code></p>
<dd> Disable PTY allocation (permitted by default).</p>
<dt><code>no-user-rc</code></p>
<dd> Disable execution of ~/.ssh/rc by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) (permitted by default).</p>
<dt><code>no-x11-forwarding</code></p>
<dd> Disable X11 forwarding (permitted by default).</p>
<dt><code>permit-agent-forwarding</code></p>
<dd> Allows ssh-agent1 forwarding.</p>
<dt><code>permit-port-forwarding</code></p>
<dd> Allows port forwarding.</p>
<dt><code>permit-pty</code></p>
<dd> Allows PTY allocation.</p>
<dt><code>permit-user-rc</code></p>
<dd> Allows execution of ~/.ssh/rc by <a href="/docs/linux/man/8-sshd/">sshd</a>(8).</p>
<dt><code>permit-x11-forwarding</code></p>
<dd> Allows X11 forwarding.</p>
<dt><code>source-address = </code><i>address_list</i></p>
<dd> Restrict the source addresses from which the certificate is considered valid. The <i>address_list</i> is a comma-separated list of one or more address/netmask pairs in CIDR format.</dl>
<p> At present, no options are valid for host keys.</p>
<dt><code>-o</code></p>
<dd> Causes <code>ssh-keygen</code> to save SSH protocol 2 private keys using the new OpenSSH format rather than the more compatible PEM format. The new format has increased resistance to brute-force password cracking but is not supported by versions of OpenSSH prior to 6.5. Ed25519 keys always use the new private key format.</p>
<dt><code>-P </code><i>passphrase</i></p>
<dd> Provides the (old) passphrase.</p>
<dt><code>-p</code></p>
<dd> Requests changing the passphrase of a private key file instead of creating a new private key. The program will prompt for the file containing the private key, for the old passphrase, and twice for the new passphrase.</p>
<dt><code>-Q</code></p>
<dd> Test whether keys have been revoked in a KRL.</p>
<dt><code>-q</code></p>
<dd> Silence <code>ssh-keygen</code></p>
<dt><code>-R </code><i>hostname</i></p>
<dd> Removes all keys belonging to <i>hostname</i> from a known_hosts file. This option is useful to delete hashed hosts (see the &#8211;<code>H</code> option above).</p>
<dt><code>-r </code><i>hostname</i></p>
<dd> Print the SSHFP fingerprint resource record named <i>hostname</i> for the specified public key file.</p>
<dt><code>-S </code><i>start</i></p>
<dd> Specify start point (in hex) when generating candidate moduli for DH-GEX.</p>
<dt><code>-s </code><i>ca_key</i></p>
<dd> Certify (sign) a public key using the specified CA key. Please see the Sx CERTIFICATES section for details. </p>
<p> When generating a KRL, &#8211;<code>s</code> specifies a path to a CA public key file used to revoke certificates directly by key ID or serial number. See the Sx KEY REVOCATION LISTS section for details.</p>
<dt><code>-T </code><i>output_file</i></p>
<dd> Test DH group exchange candidate primes (generated using the &#8211;<code>G</code> option) for safety.</p>
<dt><code>-t </code><i>type</i></p>
<dd> Specifies the type of key to create. The possible values are &#8220;rsa1&#8221; for protocol version 1 and &#8220;dsa&#8221; &#8220;ecdsa&#8221; &#8220;ed25519&#8221; or &#8220;rsa&#8221; for protocol version 2.</p>
<dt><code>-u</code></p>
<dd> Update a KRL. When specified with &#8211;<code>k</code> keys listed via the command line are added to the existing KRL rather than a new KRL being created.</p>
<dt><code>-V </code><i>validity_interval</i></p>
<dd> Specify a validity interval when signing a certificate. A validity interval may consist of a single time, indicating that the certificate is valid beginning now and expiring at that time, or may consist of two times separated by a colon to indicate an explicit time interval. The start time may be specified as a date in YYYYMMDD format, a time in YYYYMMDDHHMMSS format or a relative time (to the current time) consisting of a minus sign followed by a relative time in the format described in the TIME FORMATS section of sshd_config5. The end time may be specified as a YYYYMMDD date, a YYYYMMDDHHMMSS time or a relative time starting with a plus character. </p>
<p> For example: &#8220;+52w1d&#8221; (valid from now to 52 weeks and one day from now), &#8220;-4w:+4w&#8221; (valid from four weeks ago to four weeks from now), &#8220;20100101123000:20110101123000&#8221; (valid from 12:30 PM, January 1st, 2010 to 12:30 PM, January 1st, 2011), &#8220;-1d:20110101&#8221; (valid from yesterday to midnight, January 1st, 2011).</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Causes <code>ssh-keygen</code> to print debugging messages about its progress. This is helpful for debugging moduli generation. Multiple &#8211;<code>v</code> options increase the verbosity. The maximum is 3.</p>
<dt><code>-W </code><i>generator</i></p>
<dd> Specify desired generator when testing candidate moduli for DH-GEX.</p>
<dt><code>-y</code></p>
<dd> This option will read a private OpenSSH format file and print an OpenSSH public key to stdout.</p>
<dt><code>-z </code><i>serial_number</i></p>
<dd> Specifies a serial number to be embedded in the certificate to distinguish this certificate from others from the same CA. The default serial number is zero. </p>
<p> When generating a KRL, the &#8211;<code>z</code> flag is used to specify a KRL version number.</dl>
<h2>MODULI GENERATION</h2>
<p> <code>ssh-keygen</code> may be used to generate groups for the Diffie-Hellman Group Exchange (DH-GEX) protocol. Generating these groups is a two-step process: first, candidate primes are generated using a fast, but memory intensive process. These candidate primes are then tested for suitability (a CPU-intensive process). </p>
<p> Generation of primes is performed using the &#8211;<code>G</code> option. The desired length of the primes may be specified by the &#8211;<code>b</code> option. For example: </p>
<blockquote><p><tt># ssh-keygen -G moduli-2048.candidates -b 2048</tt></p></blockquote>
<p> By default, the search for primes begins at a random point in the desired length range. This may be overridden using the &#8211;<code>S</code> option, which specifies a different start point (in hex). </p>
<p> Once a set of candidates have been generated, they must be screened for suitability. This may be performed using the &#8211;<code>T</code> option. In this mode <code>ssh-keygen</code> will read candidates from standard input (or a file specified using the &#8211;<code>f</code> option). For example: </p>
<blockquote><p><tt># ssh-keygen -T moduli-2048 -f moduli-2048.candidates</tt></p></blockquote>
<p> By default, each candidate will be subjected to 100 primality tests. This may be overridden using the &#8211;<code>a</code> option. The DH generator value will be chosen automatically for the prime under consideration. If a specific generator is desired, it may be requested using the &#8211;<code>W</code> option. Valid generator values are 2, 3, and 5. </p>
<p> Screened DH groups may be installed in /etc/gsissh/moduli It is important that this file contains moduli of a range of bit lengths and that both ends of a connection share common moduli.</p>
<h2>CERTIFICATES</h2>
<p> <code>ssh-keygen</code> supports signing of keys to produce certificates that may be used for user or host authentication. Certificates consist of a public key, some identity information, zero or more principal (user or host) names and a set of options that are signed by a Certification Authority (CA) key. Clients or servers may then trust only the CA key and verify its signature on a certificate rather than trusting many user/host keys. Note that OpenSSH certificates are a different, and much simpler, format to the X.509 certificates used in <a href="/docs/linux/man/8-ssl/">ssl</a>(8). </p>
<p> <code>ssh-keygen</code> supports two types of certificates: user and host. User certificates authenticate users to servers, whereas host certificates authenticate server hosts to users. To generate a user certificate: </p>
<blockquote><p><tt>$ ssh-keygen -s /path/to/ca_key -I key_id /path/to/user_key.pub</tt></p></blockquote>
<p> The resultant certificate will be placed in /path/to/user_key-cert.pub A host certificate requires the &#8211;<code>h</code> option: </p>
<blockquote><p><tt>$ ssh-keygen -s /path/to/ca_key -I key_id -h /path/to/host_key.pub</tt></p></blockquote>
<p> The host certificate will be output to /path/to/host_key-cert.pub </p>
<p> It is possible to sign using a CA key stored in a PKCS#11 token by providing the token library using &#8211;<code>D</code> and identifying the CA key by providing its public half as an argument to &#8211;<code>s</code> </p>
<blockquote><p><tt>$ ssh-keygen -s ca_key.pub -D libpkcs11.so -I key_id host_key.pub</tt></p></blockquote>
<p> In all cases, <i>key_id</i> is a &quot;key identifier&quot; that is logged by the server when the certificate is used for authentication. </p>
<p> Certificates may be limited to be valid for a set of principal (user/host) names. By default, generated certificates are valid for all users or hosts. To generate a certificate for a specified set of principals: </p>
<blockquote><p><tt>$ ssh-keygen -s ca_key -I key_id -n user1,user2 user_key.pub</tt></p></blockquote>
<blockquote><p><tt>&quot;$ ssh-keygen -s ca_key -I key_id -h -n host.domain user_key.pub&quot;</tt></p></blockquote>
<p> Additional limitations on the validity and use of user certificates may be specified through certificate options. A certificate option may disable features of the SSH session, may be valid only when presented from particular source addresses or may force the use of a specific command. For a list of valid certificate options, see the documentation for the &#8211;<code>O</code> option above. </p>
<p> Finally, certificates may be defined with a validity lifetime. The &#8211;<code>V</code> option allows specification of certificate start and end times. A certificate that is presented at a time outside this range will not be considered valid. By default, certificates are valid from UNIX Epoch to the distant future. </p>
<p> For certificates to be used for user or host authentication, the CA public key must be trusted by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) or <a href="/docs/linux/man/1-ssh/">ssh</a>(1). Please refer to those manual pages for details.</p>
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
<dd> Revokes the specified key by its SHA1 hash.</dl>
<p> KRLs may be updated using the &#8211;<code>u</code> flag in addition to &#8211;<code>k</code> When this option is specified, keys listed via the command line are merged into the KRL, adding to those already there. </p>
<p> It is also possible, given a KRL, to test whether it revokes a particular key (or keys). The &#8211;<code>Q</code> flag will query an existing KRL, testing each key specified on the commandline. If any key listed on the command line has been revoked (or an error encountered) then <code>ssh-keygen</code> will exit with a non-zero exit status. A zero exit status will only be returned if no key was revoked.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.ssh/identity </code></p>
<dd> Contains the protocol version 1 RSA authentication identity of the user. This file should not be readable by anyone but the user. It is possible to specify a passphrase when generating the key; that passphrase will be used to encrypt the private part of this file using 3DES. This file is not automatically accessed by <code>ssh-keygen</code> but it is offered as the default file for the private key. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will read this file when a login attempt is made. </p>
<dt><code>~/.ssh/identity.pub </code></p>
<dd> Contains the protocol version 1 RSA public key for authentication. The contents of this file should be added to ~/.ssh/authorized_keys on all machines where the user wishes to log in using RSA authentication. There is no need to keep the contents of this file secret. </p>
<dt><code>~/.ssh/id_dsa </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519 </code></p>
<dd>
<dt><code>~/.ssh/id_rsa </code></p>
<dd> Contains the protocol version 2 DSA, ECDSA, ED25519 or RSA authentication identity of the user. This file should not be readable by anyone but the user. It is possible to specify a passphrase when generating the key; that passphrase will be used to encrypt the private part of this file using 128-bit AES. This file is not automatically accessed by <code>ssh-keygen</code> but it is offered as the default file for the private key. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will read this file when a login attempt is made. </p>
<dt><code>~/.ssh/id_dsa.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519.pub </code></p>
<dd>
<dt><code>~/.ssh/id_rsa.pub </code></p>
<dd> Contains the protocol version 2 DSA, ECDSA, ED25519 or RSA public key for authentication. The contents of this file should be added to ~/.ssh/authorized_keys on all machines where the user wishes to log in using public key authentication. There is no need to keep the contents of this file secret. </p>
<dt><code>/etc/gsissh/moduli </code></p>
<dd> Contains Diffie-Hellman groups used for DH-GEX. The file format is described in <a href="/docs/linux/man/5-moduli/">moduli</a>(5).</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SSH_USE_STRONG_RNG </code></p>
<dd> The reseeding of the OpenSSL random generator is usually done from <code>/dev/urandom</code> If the <code>SSH_USE_STRONG_RNG</code> environment variable is set to value other than <code>0</code> the OpenSSL random generator is reseeded from <code>/dev/random</code> The number of bytes read is defined by the SSH_USE_STRONG_RNG value. Minimum is 14 bytes. This setting is not recommended on the computers without the hardware random generator because insufficient entropy causes the connection to be blocked until enough entropy is available.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, <a href="/docs/linux/man/5-moduli/">moduli</a>(5), <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<dl>
<dt>
<dd> <i>RFC 4716</i> <i>&quot;The Secure Shell (SSH) Public Key File Format&quot;</i> 2006</dl>
<h2>AUTHORS</h2>
<p> OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. </p>
<h2>Index</h2>
