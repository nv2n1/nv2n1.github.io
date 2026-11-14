---
title: "gpg(1)"
name: "gpg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg/"
description: "gpg – OpenPGP encryption and signing tool"
---

<h2 class="name">NAME</h2>
<p> <code>gpg</code> &#8211; OpenPGP encryption and signing tool </p>
<h2>SYNOPSIS</h2>
<p> <code>gpg</code> [<code>&#8211;homedir</code> <i>dir</i>] [<code>&#8211;options</code> <i>file</i>] [<i>options</i>] <i>command</i> [<i>args</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>gpg</code> is the OpenPGP part of the GNU Privacy Guard (GnuPG). It is a tool to provide digital encryption and signing services using the OpenPGP standard. <code>gpg</code> features complete key management and all the bells and whistles you would expect from a full OpenPGP implementation. </p>
<p> There are two main versions of GnuPG: GnuPG 1.x and GnuPG 2.x. GnuPG 2.x supports modern encryption algorithms and thus should be preferred over GnuPG 1.x. You only need to use GnuPG 1.x if your platform doesn&#8217;t support GnuPG 2.x, or you need support for some features that GnuPG 2.x has deprecated, e.g., decrypting data created with PGP-2 keys. </p>
<p> If you are looking for version 1 of GnuPG, you may find that version installed under the name <code>gpg1</code>. </p>
<h2>RETURN VALUE</h2>
<p> The program returns 0 if there are no severe errors, 1 if at least a signature was bad, and other error codes for fatal errors. </p>
<p> Note that signature verification requires exact knowledge of what has been signed and by whom it has beensigned. Using only the return code is thus not an appropriate way to verify a signature by a script. Either make proper use or the status codes or use the <code>gpgv</code> tool which has been designed to make signature verification easy for scripts. </p>
<h2>WARNINGS</h2>
<p> Use a good password for your user account and make sure that all security issues are always fixed on your machine. Also employ diligent physical protection to your machine. Consider to use a good passphrase as a last resort protection to your secret key in the case your machine gets stolen. It is important that your secret key is never leaked. Using an easy to carry around token or smartcard with the secret key is often a advisable. </p>
<p> If you are going to verify detached signatures, make sure that the program knows about it; either give both filenames on the command line or use &#8216;-&#8216; to specify STDIN. </p>
<p> For scripted or other unattended use of <code>gpg</code> make sure to use the machine-parseable interface and not the default interface which is intended for direct use by humans. The machine-parseable interface provides a stable and well documented API independent of the locale or future changes of <code>gpg</code>. To enable this interface use the options <code>&#8211;with-colons</code> and <code>&#8211;status-fd</code>. For certain operations the option <code>&#8211;command-fd</code> may come handy too. See this man page and the file &#8216;<i>DETAILS</i>&#8216; for the specification of the interface. Note that the GnuPG &#8220;info&#8221; pages as well as the PDF version of the GnuPG manual features a chapter on unattended use of GnuPG. As an alternative the library <code>GPGME</code> can be used as a high-level abstraction on top of that interface. </p>
<h2>INTEROPERABILITY</h2>
<p> GnuPG tries to be a very flexible implementation of the OpenPGP standard. In particular, GnuPG implements many of the optional parts of the standard, such as the SHA-512 hash, and the ZLIB and BZIP2 compression algorithms. It is important to be aware that not all OpenPGP programs implement these optional algorithms and that by forcing their use via the <code>&#8211;cipher-algo</code>, <code>&#8211;digest-algo</code>, <code>&#8211;cert-digest-algo</code>, or <code>&#8211;compress-algo</code> options in GnuPG, it is possible to create a perfectly valid OpenPGP message, but one that cannot be read by the intended recipient. </p>
<p> There are dozens of variations of OpenPGP programs available, and each supports a slightly different subset of these optional algorithms. For example, until recently, no (unhacked) version of PGP supported the BLOWFISH cipher algorithm. A message using BLOWFISH simply could not be read by a PGP user. By default, GnuPG uses the standard OpenPGP preferences system that will always do the right thing and create messages that are usable by all recipients, regardless of which OpenPGP program they use. Only override this safe default if you really know what you are doing. </p>
<p> If you absolutely must override the safe default, or if the preferences on a given key are invalid for some reason, you are far better off using the <code>&#8211;pgp6</code>, <code>&#8211;pgp7</code>, or <code>&#8211;pgp8</code> options. These options are safe as they do not force any particular algorithms in violation of OpenPGP, but rather reduce the available algorithms to a &quot;PGP-safe&quot; list. </p>
<h2>COMMANDS</h2>
<p> Commands are not distinguished from options except for the fact that only one command is allowed. Generally speaking, irrelevant options are silently ignored, and may not be checked for correctness. </p>
<p> <code>gpg</code> may be run with no commands. In this case it will print a warning perform a reasonable action depending on the type of file it is given as input (an encrypted message is decrypted, a signature is verified, a file containing keys is listed, etc.). </p>
<p> If you run into any problems, please add the option <code>&#8211;verbose</code> to the invocation to see more diagnostics. </p>
<h3>Commands not specific to the function</h3>
<p> &nbsp; </p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the program version and licensing information. Note that you cannot abbreviate this command. </p>
<dt><code>&#8211;help</code></p>
<dd> <code>-h</code> Print a usage message summarizing the most useful command-line options. Note that you cannot arbitrarily abbreviate this command (though you can use its short form <code>-h</code>). </p>
<dt><code>&#8211;warranty</code></p>
<dd> Print warranty information. </p>
<dt><code>&#8211;dump-options</code></p>
<dd> Print a list of all available options and commands. Note that you cannot abbreviate this command.</dl>
<h3>Commands to select the type of operation</h3>
<p> &nbsp; </p>
<dl>
<dt><code>&#8211;sign</code></p>
<dd> <code>-s</code> Sign a message. This command may be combined with <code>&#8211;encrypt</code> (to sign and encrypt a message), <code>&#8211;symmetric</code> (to sign and symmetrically encrypt a message), or both <code>&#8211;encrypt</code> and <code>&#8211;symmetric</code> (to sign and encrypt a message that can be decrypted using a secret key or a passphrase). The signing key is chosen by default or can be set explicitly using the <code>&#8211;local-user</code> and <code>&#8211;default-key</code> options. </p>
<dt><code>&#8211;clear-sign</code></p>
<dd> <code>&#8211;clearsign</code> Make a cleartext signature. The content in a cleartext signature is readable without any special software. OpenPGP software is only needed to verify the signature. cleartext signatures may modify end-of-line whitespace for platform independence and are not intended to be reversible. The signing key is chosen by default or can be set explicitly using the <code>&#8211;local-user</code> and <code>&#8211;default-key</code> options. </p>
<dt><code>&#8211;detach-sign</code></p>
<dd> <code>-b</code> Make a detached signature. </p>
<dt><code>&#8211;encrypt</code></p>
<dd> <code>-e</code> Encrypt data to one or more public keys. This command may be combined with <code>&#8211;sign</code> (to sign and encrypt a message), <code>&#8211;symmetric</code> (to encrypt a message that can be decrypted using a secret key or a passphrase), or <code>&#8211;sign</code> and <code>&#8211;symmetric</code> together (for a signed message that can be decrypted using a secret key or a passphrase). <code>&#8211;recipient</code> and related options specify which public keys to use for encryption. </p>
<dt><code>&#8211;symmetric</code></p>
<dd> <code>-c</code> Encrypt with a symmetric cipher using a passphrase. The default symmetric cipher used is AES-128, but may be chosen with the <code>&#8211;cipher-algo</code> option. This command may be combined with <code>&#8211;sign</code> (for a signed and symmetrically encrypted message), <code>&#8211;encrypt</code> (for a message that may be decrypted via a secret key or a passphrase), or <code>&#8211;sign</code> and <code>&#8211;encrypt</code> together (for a signed message that may be decrypted via a secret key or a passphrase). <code>gpg</code> caches the passphrase used for symmetric encryption so that a decrypt operation may not require that the user needs to enter the passphrase. The option <code>&#8211;no-symkey-cache</code> can be used to disable this feature. </p>
<dt><code>&#8211;store</code></p>
<dd> Store only (make a simple literal data packet). </p>
<dt><code>&#8211;decrypt</code></p>
<dd> <code>-d</code> Decrypt the file given on the command line (or STDIN if no file is specified) and write it to STDOUT (or the file specified with <code>&#8211;output</code>). If the decrypted file is signed, the signature is also verified. This command differs from the default operation, as it never writes to the filename which is included in the file and it rejects files that don&#8217;t begin with an encrypted message. </p>
<dt><code>&#8211;verify</code></p>
<dd> Assume that the first argument is a signed file and verify it without generating any output. With no arguments, the signature packet is read from STDIN. If only one argument is given, the specified file is expected to include a complete signature. </p>
<p> With more than one argument, the first argument should specify a file with a detached signature and the remaining files should contain the signed data. To read the signed data from STDIN, use &#8216;-&#8216; as the second filename. For security reasons, a detached signature will not read the signed material from STDIN if not explicitly specified. </p>
<p> Note: If the option <code>&#8211;batch</code> is not used, <code>gpg</code> may assume that a single argument is a file with a detached signature, and it will try to find a matching data file by stripping certain suffixes. Using this historical feature to verify a detached signature is strongly discouraged; you should always specify the data file explicitly. </p>
<p> Note: When verifying a cleartext signature, <code>gpg</code> verifies only what makes up the cleartext signed data and not any extra data outside of the cleartext signature or the header lines directly following the dash marker line. The option <code>&#8211;output</code> may be used to write out the actual signed data, but there are other pitfalls with this format as well. It is suggested to avoid cleartext signatures in favor of detached signatures. </p>
<p> Note: Sometimes the use of the <code>gpgv</code> tool is easier than using the full-fledged <code>gpg</code> with this option. <code>gpgv</code> is designed to compare signed data against a list of trusted keys and returns with success only for a good signature. It has its own manual page. </p>
<dt><code>&#8211;multifile</code></p>
<dd> This modifies certain other commands to accept multiple files for processing on the command line or read from STDIN with each filename on a separate line. This allows for many files to be processed at once. <code>&#8211;multifile</code> may currently be used along with <code>&#8211;verify</code>, <code>&#8211;encrypt</code>, and <code>&#8211;decrypt</code>. Note that <code>&#8211;multifile &#8211;verify</code> may not be used with detached signatures. </p>
<dt><code>&#8211;verify-files</code></p>
<dd> Identical to <code>&#8211;multifile &#8211;verify</code>. </p>
<dt><code>&#8211;encrypt-files</code></p>
<dd> Identical to <code>&#8211;multifile &#8211;encrypt</code>. </p>
<dt><code>&#8211;decrypt-files</code></p>
<dd> Identical to <code>&#8211;multifile &#8211;decrypt</code>. </p>
<dt><code>&#8211;list-keys</code></p>
<dd> <code>-k</code> <code>&#8211;list-public-keys</code> List the specified keys. If no keys are specified, then all keys from the configured public keyrings are listed. </p>
<p> Never use the output of this command in scripts or other programs. The output is intended only for humans and its format is likely to change. The <code>&#8211;with-colons</code> option emits the output in a stable, machine-parseable format, which is intended for use by scripts and other programs. </p>
<dt><code>&#8211;list-secret-keys</code></p>
<dd> <code>-K</code> List the specified secret keys. If no keys are specified, then all known secret keys are listed. A <code>#</code> after the initial tags <code>sec</code> or <code>ssb</code> means that the secret key or subkey is currently not usable. We also say that this key has been taken offline (for example, a primary key can be taken offline by exporting the key using the command <code>&#8211;export-secret-subkeys</code>). A <code>&gt;</code> after these tags indicate that the key is stored on a smartcard. See also <code>&#8211;list-keys</code>. </p>
<dt><code>&#8211;check-signatures</code></p>
<dd> <code>&#8211;check-sigs</code> Same as <code>&#8211;list-keys</code>, but the key signatures are verified and listed too. Note that for performance reasons the revocation status of a signing key is not shown. This command has the same effect as using <code>&#8211;list-keys</code> with <code>&#8211;with-sig-check</code>. </p>
<p> The status of the verification is indicated by a flag directly following the &quot;sig&quot; tag (and thus before the flags described below. A &quot;!&quot; indicates that the signature has been successfully verified, a &quot;-&quot; denotes a bad signature and a &quot;%&quot; is used if an error occurred while checking the signature (e.g. a non supported algorithm). Signatures where the public key is not available are not listed; to see their keyids the command <code>&#8211;list-sigs</code> can be used. </p>
<p> For each signature listed, there are several flags in between the signature status flag and keyid. These flags give additional information about each key signature. From left to right, they are the numbers 1-3 for certificate check level (see <code>&#8211;ask-cert-level</code>), &quot;L&quot; for a local or non-exportable signature (see <code>&#8211;lsign-key</code>), &quot;R&quot; for a nonRevocable signature (see the <code>&#8211;edit-key</code> command &quot;nrsign&quot;), &quot;P&quot; for a signature that contains a policy URL (see <code>&#8211;cert-policy-url</code>), &quot;N&quot; for a signature that contains a notation (see <code>&#8211;cert-notation</code>), &quot;X&quot; for an eXpired signature (see <code>&#8211;ask-cert-expire</code>), and the numbers 1-9 or &quot;T&quot; for 10 and above to indicate trust signature levels (see the <code>&#8211;edit-key</code> command &quot;tsign&quot;). </p>
<dt><code>&#8211;locate-keys</code></p>
<dd> <code>&#8211;locate-external-keys</code> Locate the keys given as arguments. This command basically uses the same algorithm as used when locating keys for encryption or signing and may thus be used to see what keys <code>gpg</code> might use. In particular external methods as defined by <code>&#8211;auto-key-locate</code> may be used to locate a key. Only public keys are listed. The variant <code>&#8211;locate-external-keys</code> does not consider a locally existing key and can thus be used to force the refresh of a key via the defined external methods. </p>
<dt><code>&#8211;show-keys</code></p>
<dd> This commands takes OpenPGP keys as input and prints information about them in the same way the command <code>&#8211;list-keys</code> does for locally stored key. In addition the list options <code>show-unusable-uids</code>, <code>show-unusable-subkeys</code>, <code>show-notations</code> and <code>show-policy-urls</code> are also enabled. As usual for automated processing, this command should be combined with the option <code>&#8211;with-colons</code>. </p>
<dt><code>&#8211;fingerprint</code></p>
<dd> List all keys (or the specified ones) along with their fingerprints. This is the same output as <code>&#8211;list-keys</code> but with the additional output of a line with the fingerprint. May also be combined with <code>&#8211;check-signatures</code>. If this command is given twice, the fingerprints of all secondary keys are listed too. This command also forces pretty printing of fingerprints if the keyid format has been set to &quot;none&quot;. </p>
<dt><code>&#8211;list-packets</code></p>
<dd> List only the sequence of packets. This command is only useful for debugging. When used with option <code>&#8211;verbose</code> the actual MPI values are dumped and not only their lengths. Note that the output of this command may change with new releases. </p>
<dt><code>&#8211;edit-card</code></p>
<dd> <code>&#8211;card-edit</code> Present a menu to work with a smartcard. The subcommand &quot;help&quot; provides an overview on available commands. For a detailed description, please see the Card HOWTO at <a rel="nofollow" href="https://gnupg.org/documentation/howtos.html#GnuPG-cardHOWTO">https://gnupg.org/documentation/howtos.html#GnuPG-cardHOWTO</a> . </p>
<dt><code>&#8211;card-status</code></p>
<dd> Show the content of the smart card. </p>
<dt><code>&#8211;change-pin</code></p>
<dd> Present a menu to allow changing the PIN of a smartcard. This functionality is also available as the subcommand &quot;passwd&quot; with the <code>&#8211;edit-card</code> command. </p>
<dt><code>&#8211;delete-keys </code><i>name</i></p>
<dd> Remove key from the public keyring. In batch mode either <code>&#8211;yes</code> is required or the key must be specified by fingerprint. This is a safeguard against accidental deletion of multiple keys. If the exclamation mark syntax is used with the fingerprint of a subkey only that subkey is deleted; if the exclamation mark is used with the fingerprint of the primary key the entire public key is deleted. </p>
<dt><code>&#8211;delete-secret-keys </code><i>name</i></p>
<dd> Remove key from the secret keyring. In batch mode the key must be specified by fingerprint. The option <code>&#8211;yes</code> can be used to advise gpg-agent not to request a confirmation. This extra pre-caution is done because <code>gpg</code> can&#8217;t be sure that the secret key (as controlled by gpg-agent) is only used for the given OpenPGP public key. If the exclamation mark syntax is used with the fingerprint of a subkey only the secret part of that subkey is deleted; if the exclamation mark is used with the fingerprint of the primary key only the secret part of the primary key is deleted. </p>
<dt><code>&#8211;delete-secret-and-public-key </code><i>name</i></p>
<dd> Same as <code>&#8211;delete-key</code>, but if a secret key exists, it will be removed first. In batch mode the key must be specified by fingerprint. The option <code>&#8211;yes</code> can be used to advise gpg-agent not to request a confirmation. </p>
<dt><code>&#8211;export</code></p>
<dd> Either export all keys from all keyrings (default keyrings and those registered via option <code>&#8211;keyring</code>), or if at least one name is given, those of the given name. The exported keys are written to STDOUT or to the file given with option <code>&#8211;output</code>. Use together with <code>&#8211;armor</code> to mail those keys. </p>
<dt><code>&#8211;send-keys </code><i>keyIDs</i></p>
<dd> Similar to <code>&#8211;export</code> but sends the keys to a keyserver. Fingerprints may be used instead of key IDs. Don&#8217;t send your complete keyring to a keyserver &#8212; select only those keys which are new or changed by you. If no <i>keyIDs</i> are given, <code>gpg</code> does nothing. </p>
<p> Take care: Keyservers are by design write only systems and thus it is not possible to ever delete keys once they have been send to a keyserver. </p>
<dt><code>&#8211;export-secret-keys</code></p>
<dd> <code>&#8211;export-secret-subkeys</code> Same as <code>&#8211;export</code>, but exports the secret keys instead. The exported keys are written to STDOUT or to the file given with option <code>&#8211;output</code>. This command is often used along with the option <code>&#8211;armor</code> to allow for easy printing of the key for paper backup; however the external tool <code>paperkey</code> does a better job of creating backups on paper. Note that exporting a secret key can be a security risk if the exported keys are sent over an insecure channel. </p>
<p> The second form of the command has the special property to render the secret part of the primary key useless; this is a GNU extension to OpenPGP and other implementations can not be expected to successfully import such a key. Its intended use is in generating a full key with an additional signing subkey on a dedicated machine. This command then exports the key without the primary key to the main machine. </p>
<p> GnuPG may ask you to enter the passphrase for the key. This is required, because the internal protection method of the secret key is different from the one specified by the OpenPGP protocol. </p>
<dt><code>&#8211;export-ssh-key</code></p>
<dd> This command is used to export a key in the OpenSSH public key format. It requires the specification of one key by the usual means and exports the latest valid subkey which has an authentication capability to STDOUT or to the file given with option <code>&#8211;output</code>. That output can directly be added to ssh&#8217;s &#8216;<i>authorized_key</i>&#8216; file. </p>
<p> By specifying the key to export using a key ID or a fingerprint suffixed with an exclamation mark (!), a specific subkey or the primary key can be exported. This does not even require that the key has the authentication capability flag set. </p>
<dt><code>&#8211;import</code></p>
<dd> <code>&#8211;fast-import</code> Import/merge keys. This adds the given keys to the keyring. The fast version is currently just a synonym. </p>
<p> There are a few other options which control how this command works. Most notable here is the <code>&#8211;import-options merge-only</code> option which does not insert new keys but does only the merging of new signatures, user-IDs and subkeys. </p>
<dt><code>&#8211;receive-keys </code><i>keyIDs</i></p>
<dd> <code>&#8211;recv-keys </code><i>keyIDs</i> Import the keys with the given <i>keyIDs</i> from a keyserver. </p>
<dt><code>&#8211;refresh-keys</code></p>
<dd> Request updates from a keyserver for keys that already exist on the local keyring. This is useful for updating a key with the latest signatures, user IDs, etc. Calling this with no arguments will refresh the entire keyring. </p>
<dt><code>&#8211;search-keys </code><i>names</i></p>
<dd> Search the keyserver for the given <i>names</i>. Multiple names given here will be joined together to create the search string for the keyserver. Note that keyservers search for <i>names</i> in a different and simpler way than gpg does. The best choice is to use a mail address. Due to data privacy reasons keyservers may even not even allow searching by user id or mail address and thus may only return results when being used with the <code>&#8211;recv-key</code> command to search by key fingerprint or keyid. </p>
<dt><code>&#8211;fetch-keys </code><i>URIs</i></p>
<dd> Retrieve keys located at the specified <i>URIs</i>. Note that different installations of GnuPG may support different protocols (HTTP, FTP, LDAP, etc.). When using HTTPS the system provided root certificates are used by this command. </p>
<dt><code>&#8211;update-trustdb</code></p>
<dd> Do trust database maintenance. This command iterates over all keys and builds the Web of Trust. This is an interactive command because it may have to ask for the &quot;ownertrust&quot; values for keys. The user has to give an estimation of how far she trusts the owner of the displayed key to correctly certify (sign) other keys. GnuPG only asks for the ownertrust value if it has not yet been assigned to a key. Using the <code>&#8211;edit-key</code> menu, the assigned value can be changed at any time. </p>
<dt><code>&#8211;check-trustdb</code></p>
<dd> Do trust database maintenance without user interaction. From time to time the trust database must be updated so that expired keys or signatures and the resulting changes in the Web of Trust can be tracked. Normally, GnuPG will calculate when this is required and do it automatically unless <code>&#8211;no-auto-check-trustdb</code> is set. This command can be used to force a trust database check at any time. The processing is identical to that of <code>&#8211;update-trustdb</code> but it skips keys with a not yet defined &quot;ownertrust&quot;. </p>
<p> For use with cron jobs, this command can be used together with <code>&#8211;batch</code> in which case the trust database check is done only if a check is needed. To force a run even in batch mode add the option <code>&#8211;yes</code>. </p>
<dt><code>&#8211;export-ownertrust</code></p>
<dd> Send the ownertrust values to STDOUT. This is useful for backup purposes as these values are the only ones which can&#8217;t be re-created from a corrupted trustdb. Example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
  gpg --export-ownertrust &gt; otrust.txt
</pre>
</dl>
</dl>
<dt><code>&#8211;import-ownertrust</code></p>
<dd> Update the trustdb with the ownertrust values stored in <code>files</code> (or STDIN if not given); existing values will be overwritten. In case of a severely damaged trustdb and if you have a recent backup of the ownertrust values (e.g. in the file &#8216;<i>otrust.txt</i>&#8216;), you may re-create the trustdb using these commands:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
  cd ~/.gnupg
  rm trustdb.gpg
  gpg --import-ownertrust &lt; otrust.txt
</pre>
</dl>
</dl>
<dt><code>&#8211;rebuild-keydb-caches</code></p>
<dd> When updating from version 1.0.6 to 1.0.7 this command should be used to create signature caches in the keyring. It might be handy in other situations too. </p>
<dt><code>&#8211;print-md </code><i>algo</i></p>
<dd> <code>&#8211;print-mds</code> Print message digest of algorithm <i>algo</i> for all given files or STDIN. With the second form (or a deprecated &quot;*&quot; for <i>algo</i>) digests for all available algorithms are printed. </p>
<dt><code>&#8211;gen-random </code><i>0|1|2</i> <i>count</i></p>
<dd> Emit <i>count</i> random bytes of the given quality level 0, 1 or 2. If <i>count</i> is not given or zero, an endless sequence of random bytes will be emitted. If used with <code>&#8211;armor</code> the output will be base64 encoded. PLEASE, don&#8217;t use this command unless you know what you are doing; it may remove precious entropy from the system! </p>
<dt><code>&#8211;gen-prime </code><i>mode</i> <i>bits</i></p>
<dd> Use the source, Luke :-). The output format is subject to change with ant release. </p>
<dt><code>&#8211;enarmor</code></p>
<dd> <code>&#8211;dearmor</code> Pack or unpack an arbitrary input into/from an OpenPGP ASCII armor. This is a GnuPG extension to OpenPGP and in general not very useful. </p>
<dt><code>&#8211;tofu-policy {auto|good|unknown|bad|ask} </code><i>keys</i></p>
<dd> Set the TOFU policy for all the bindings associated with the specified <i>keys</i>. For more information about the meaning of the policies, see: [trust-model-tofu]. The <i>keys</i> may be specified either by their fingerprint (preferred) or their keyid. </p>
</dl>
<h3>How to manage your keys</h3>
<p> &nbsp; </p>
<p> This section explains the main commands for key management. </p>
<dl>
<dt><code>&#8211;quick-generate-key </code><i>user-id</i> [<i>algo</i> [<i>usage</i> [<i>expire</i>]]]</p>
<dd> <code>&#8211;quick-gen-key</code> This is a simple command to generate a standard key with one user id. In contrast to <code>&#8211;generate-key</code> the key is generated directly without the need to answer a bunch of prompts. Unless the option <code>&#8211;yes</code> is given, the key creation will be canceled if the given user id already exists in the keyring. </p>
<p> If invoked directly on the console without any special options an answer to a &#8220;Continue?&#8221; style confirmation prompt is required. In case the user id already exists in the keyring a second prompt to force the creation of the key will show up. </p>
<p> If <i>algo</i> or <i>usage</i> are given, only the primary key is created and no prompts are shown. To specify an expiration date but still create a primary and subkey use &#8220;default&#8221; or &#8220;future-default&#8221; for <i>algo</i> and &#8220;default&#8221; for <i>usage</i>. For a description of these optional arguments see the command <code>&#8211;quick-add-key</code>. The <i>usage</i> accepts also the value &#8220;cert&#8221; which can be used to create a certification only primary key; the default is to a create certification and signing key. </p>
<p> The <i>expire</i> argument can be used to specify an expiration date for the key. Several formats are supported; commonly the ISO formats &#8220;YYYY-MM-DD&#8221; or &#8220;YYYYMMDDThhmmss&#8221; are used. To make the key expire in N seconds, N days, N weeks, N months, or N years use &#8220;seconds=N&#8221;, &#8220;Nd&#8221;, &#8220;Nw&#8221;, &#8220;Nm&#8221;, or &#8220;Ny&#8221; respectively. Not specifying a value, or using &#8220;-&#8221; results in a key expiring in a reasonable default interval. The values &#8220;never&#8221;, &#8220;none&#8221; can be used for no expiration date. </p>
<p> If this command is used with <code>&#8211;batch</code>, <code>&#8211;pinentry-mode</code> has been set to <code>loopback</code>, and one of the passphrase options (<code>&#8211;passphrase</code>, <code>&#8211;passphrase-fd</code>, or <code>passphrase-file</code>) is used, the supplied passphrase is used for the new key and the agent does not ask for it. To create a key without any protection <code>&#8211;passphrase &#8221;</code> may be used. </p>
<p> To create an OpenPGP key from the keys available on the currently inserted smartcard, the special string &#8220;card&#8221; can be used for <i>algo</i>. If the card features an encryption and a signing key, gpg will figure them out and creates an OpenPGP key consisting of the usual primary key and one subkey. This works only with certain smartcards. Note that the interactive <code>&#8211;full-gen-key</code> command allows to do the same but with greater flexibility in the selection of the smartcard keys. </p>
<p> Note that it is possible to create a primary key and a subkey using non-default algorithms by using &#8220;default&#8221; and changing the default parameters using the option <code>&#8211;default-new-key-algo</code>. </p>
<dt><code>&#8211;quick-set-expire </code><i>fpr</i> <i>expire</i> [*|<i>subfprs</i>]</p>
<dd> With two arguments given, directly set the expiration time of the primary key identified by <i>fpr</i> to <i>expire</i>. To remove the expiration time <code>0</code> can be used. With three arguments and the third given as an asterisk, the expiration time of all non-revoked and not yet expired subkeys are set to <i>expire</i>. With more than two arguments and a list of fingerprints given for <i>subfprs</i>, all non-revoked subkeys matching these fingerprints are set to <i>expire</i>. </p>
<dt><code>&#8211;quick-add-key </code><i>fpr</i> [<i>algo</i> [<i>usage</i> [<i>expire</i>]]]</p>
<dd> Directly add a subkey to the key identified by the fingerprint <i>fpr</i>. Without the optional arguments an encryption subkey is added. If any of the arguments are given a more specific subkey is added. </p>
<p> <i>algo</i> may be any of the supported algorithms or curve names given in the format as used by key listings. To use the default algorithm the string &#8220;default&#8221; or &#8220;-&#8221; can be used. Supported algorithms are &#8220;rsa&#8221;, &#8220;dsa&#8221;, &#8220;elg&#8221;, &#8220;ed25519&#8221;, &#8220;cv25519&#8221;, and other ECC curves. For example the string &#8220;rsa&#8221; adds an RSA key with the default key length; a string &#8220;rsa4096&#8221; requests that the key length is 4096 bits. The string &#8220;future-default&#8221; is an alias for the algorithm which will likely be used as default algorithm in future versions of gpg. To list the supported ECC curves the command <code>gpg &#8211;with-colons &#8211;list-config curve</code> can be used. </p>
<p> Depending on the given <i>algo</i> the subkey may either be an encryption subkey or a signing subkey. If an algorithm is capable of signing and encryption and such a subkey is desired, a <i>usage</i> string must be given. This string is either &#8220;default&#8221; or &#8220;-&#8221; to keep the default or a comma delimited list (or space delimited list) of keywords: &#8220;sign&#8221; for a signing subkey, &#8220;auth&#8221; for an authentication subkey, and &#8220;encr&#8221; for an encryption subkey (&#8220;encrypt&#8221; can be used as alias for &#8220;encr&#8221;). The valid combinations depend on the algorithm. </p>
<p> The <i>expire</i> argument can be used to specify an expiration date for the key. Several formats are supported; commonly the ISO formats &#8220;YYYY-MM-DD&#8221; or &#8220;YYYYMMDDThhmmss&#8221; are used. To make the key expire in N seconds, N days, N weeks, N months, or N years use &#8220;seconds=N&#8221;, &#8220;Nd&#8221;, &#8220;Nw&#8221;, &#8220;Nm&#8221;, or &#8220;Ny&#8221; respectively. Not specifying a value, or using &#8220;-&#8221; results in a key expiring in a reasonable default interval. The values &#8220;never&#8221;, &#8220;none&#8221; can be used for no expiration date. </p>
<dt><code>&#8211;generate-key</code></p>
<dd> <code>&#8211;gen-key</code> Generate a new key pair using the current default parameters. This is the standard command to create a new key. In addition to the key a revocation certificate is created and stored in the &#8216;<i>openpgp-revocs.d</i>&#8216; directory below the GnuPG home directory. </p>
<dt><code>&#8211;full-generate-key</code></p>
<dd> <code>&#8211;full-gen-key</code> Generate a new key pair with dialogs for all options. This is an extended version of <code>&#8211;generate-key</code>. </p>
<p> There is also a feature which allows you to create keys in batch mode. See the manual section &#8220;Unattended key generation&#8221; on how to use this. </p>
<dt><code>&#8211;generate-revocation </code><i>name</i></p>
<dd> <code>&#8211;gen-revoke </code><i>name</i> Generate a revocation certificate for the complete key. To only revoke a subkey or a key signature, use the <code>&#8211;edit</code> command. </p>
<p> This command merely creates the revocation certificate so that it can be used to revoke the key if that is ever needed. To actually revoke a key the created revocation certificate needs to be merged with the key to revoke. This is done by importing the revocation certificate using the <code>&#8211;import</code> command. Then the revoked key needs to be published, which is best done by sending the key to a keyserver (command <code>&#8211;send-key</code>) and by exporting (<code>&#8211;export</code>) it to a file which is then send to frequent communication partners. </p>
<dt><code>&#8211;generate-designated-revocation </code><i>name</i></p>
<dd> <code>&#8211;desig-revoke </code><i>name</i> Generate a designated revocation certificate for a key. This allows a user (with the permission of the keyholder) to revoke someone else&#8217;s key. </p>
<dt><code>&#8211;edit-key</code></p>
<dd> Present a menu which enables you to do most of the key management related tasks. It expects the specification of a key on the command line. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>uid </code><i>n</i></p>
<dd> Toggle selection of user ID or photographic user ID with index <i>n</i>. Use <code>*</code> to select all and <code>0</code> to deselect all. </p>
<dt><code>key </code><i>n</i></p>
<dd> Toggle selection of subkey with index <i>n</i> or key ID <i>n</i>. Use <code>*</code> to select all and <code>0</code> to deselect all. </p>
<dt><code>sign</code></p>
<dd> Make a signature on key of user <code>name</code>. If the key is not yet signed by the default user (or the users given with <code>-u</code>), the program displays the information of the key again, together with its fingerprint and asks whether it should be signed. This question is repeated for all users specified with <code>-u</code>. </p>
<dt><code>lsign</code></p>
<dd> Same as &quot;sign&quot; but the signature is marked as non-exportable and will therefore never be used by others. This may be used to make keys valid only in the local environment. </p>
<dt><code>nrsign</code></p>
<dd> Same as &quot;sign&quot; but the signature is marked as non-revocable and can therefore never be revoked. </p>
<dt><code>tsign</code></p>
<dd> Make a trust signature. This is a signature that combines the notions of certification (like a regular signature), and trust (like the &quot;trust&quot; command). It is generally only useful in distinct communities or groups. For more information please read the sections &#8220;Trust Signature&#8221; and &#8220;Regular Expression&#8221; in RFC-4880.</dl>
</dl>
<dl>
<dt>
<dd> Note that &quot;l&quot; (for local / non-exportable), &quot;nr&quot; (for non-revocable, and &quot;t&quot; (for trust) may be freely mixed and prefixed to &quot;sign&quot; to create a signature of any type desired.</dl>
<p> If the option <code>&#8211;only-sign-text-ids</code> is specified, then any non-text based user ids (e.g., photo IDs) will not be selected for signing. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>delsig</code></p>
<dd> Delete a signature. Note that it is not possible to retract a signature, once it has been send to the public (i.e. to a keyserver). In that case you better use <code>revsig</code>. </p>
<dt><code>revsig</code></p>
<dd> Revoke a signature. For every signature which has been generated by one of the secret keys, GnuPG asks whether a revocation certificate should be generated. </p>
<dt><code>check</code></p>
<dd> Check the signatures on all selected user IDs. With the extra option <code>selfsig</code> only self-signatures are shown. </p>
<dt><code>adduid</code></p>
<dd> Create an additional user ID. </p>
<dt><code>addphoto</code></p>
<dd> Create a photographic user ID. This will prompt for a JPEG file that will be embedded into the user ID. Note that a very large JPEG will make for a very large key. Also note that some programs will display your JPEG unchanged (GnuPG), and some programs will scale it to fit in a dialog box (PGP). </p>
<dt><code>showphoto</code></p>
<dd> Display the selected photographic user ID. </p>
<dt><code>deluid</code></p>
<dd> Delete a user ID or photographic user ID. Note that it is not possible to retract a user id, once it has been send to the public (i.e. to a keyserver). In that case you better use <code>revuid</code>. </p>
<dt><code>revuid</code></p>
<dd> Revoke a user ID or photographic user ID. </p>
<dt><code>primary</code></p>
<dd> Flag the current user id as the primary one, removes the primary user id flag from all other user ids and sets the timestamp of all affected self-signatures one second ahead. Note that setting a photo user ID as primary makes it primary over other photo user IDs, and setting a regular user ID as primary makes it primary over other regular user IDs. </p>
<dt><code>keyserver</code></p>
<dd> Set a preferred keyserver for the specified user ID(s). This allows other users to know where you prefer they get your key from. See <code>&#8211;keyserver-options honor-keyserver-url</code> for more on how this works. Setting a value of &quot;none&quot; removes an existing preferred keyserver. </p>
<dt><code>notation</code></p>
<dd> Set a name=value notation for the specified user ID(s). See <code>&#8211;cert-notation</code> for more on how this works. Setting a value of &quot;none&quot; removes all notations, setting a notation prefixed with a minus sign (-) removes that notation, and setting a notation name (without the =value) prefixed with a minus sign removes all notations with that name. </p>
<dt><code>pref</code></p>
<dd> List preferences from the selected user ID. This shows the actual preferences, without including any implied preferences. </p>
<dt><code>showpref</code></p>
<dd> More verbose preferences listing for the selected user ID. This shows the preferences in effect by including the implied preferences of 3DES (cipher), SHA-1 (digest), and Uncompressed (compression) if they are not already included in the preference list. In addition, the preferred keyserver and signature notations (if any) are shown. </p>
<dt><code>setpref </code><i>string</i></p>
<dd> Set the list of user ID preferences to <i>string</i> for all (or just the selected) user IDs. Calling setpref with no arguments sets the preference list to the default (either built-in or set via <code>&#8211;default-preference-list</code>), and calling setpref with &quot;none&quot; as the argument sets an empty preference list. Use <code>gpg &#8211;version</code> to get a list of available algorithms. Note that while you can change the preferences on an attribute user ID (aka &quot;photo ID&quot;), GnuPG does not select keys via attribute user IDs so these preferences will not be used by GnuPG. </p>
<p> When setting preferences, you should list the algorithms in the order which you&#8217;d like to see them used by someone else when encrypting a message to your key. If you don&#8217;t include 3DES, it will be automatically added at the end. Note that there are many factors that go into choosing an algorithm (for example, your key may not be the only recipient), and so the remote OpenPGP application being used to send to you may or may not follow your exact chosen order for a given message. It will, however, only choose an algorithm that is present on the preference list of every recipient key. See also the INTEROPERABILITY WITH OTHER OPENPGP PROGRAMS section below. </p>
<dt><code>addkey</code></p>
<dd> Add a subkey to this key. </p>
<dt><code>addcardkey</code></p>
<dd> Generate a subkey on a card and add it to this key. </p>
<dt><code>keytocard</code></p>
<dd> Transfer the selected secret subkey (or the primary key if no subkey has been selected) to a smartcard. The secret key in the keyring will be replaced by a stub if the key could be stored successfully on the card and you use the save command later. Only certain key types may be transferred to the card. A sub menu allows you to select on what card to store the key. Note that it is not possible to get that key back from the card &#8211; if the card gets broken your secret key will be lost unless you have a backup somewhere. </p>
<dt><code>bkuptocard </code><i>file</i></p>
<dd> Restore the given <i>file</i> to a card. This command may be used to restore a backup key (as generated during card initialization) to a new card. In almost all cases this will be the encryption key. You should use this command only with the corresponding public key and make sure that the file given as argument is indeed the backup to restore. You should then select 2 to restore as encryption key. You will first be asked to enter the passphrase of the backup key and then for the Admin PIN of the card. </p>
<dt><code>delkey</code></p>
<dd> Remove a subkey (secondary key). Note that it is not possible to retract a subkey, once it has been send to the public (i.e. to a keyserver). In that case you better use <code>revkey</code>. Also note that this only deletes the public part of a key. </p>
<dt><code>revkey</code></p>
<dd> Revoke a subkey. </p>
<dt><code>expire</code></p>
<dd> Change the key or subkey expiration time. If a subkey is selected, the expiration time of this subkey will be changed. With no selection, the key expiration of the primary key is changed. </p>
<dt><code>trust</code></p>
<dd> Change the owner trust value for the key. This updates the trust-db immediately and no save is required. </p>
<dt><code>disable</code></p>
<dd> <code>enable</code> Disable or enable an entire key. A disabled key can not normally be used for encryption. </p>
<dt><code>addrevoker</code></p>
<dd> Add a designated revoker to the key. This takes one optional argument: &quot;sensitive&quot;. If a designated revoker is marked as sensitive, it will not be exported by default (see export-options). </p>
<dt><code>passwd</code></p>
<dd> Change the passphrase of the secret key. </p>
<dt><code>toggle</code></p>
<dd> This is dummy command which exists only for backward compatibility. </p>
<dt><code>clean</code></p>
<dd> Compact (by removing all signatures except the selfsig) any user ID that is no longer usable (e.g. revoked, or expired). Then, remove any signatures that are not usable by the trust calculations. Specifically, this removes any signature that does not validate, any signature that is superseded by a later signature, revoked signatures, and signatures issued by keys that are not present on the keyring. </p>
<dt><code>minimize</code></p>
<dd> Make the key as small as possible. This removes all signatures from each user ID except for the most recent self-signature. </p>
<dt><code>change-usage</code></p>
<dd> Change the usage flags (capabilities) of the primary key or of subkeys. These usage flags (e.g. Certify, Sign, Authenticate, Encrypt) are set during key creation. Sometimes it is useful to have the opportunity to change them (for example to add Authenticate) after they have been created. Please take care when doing this; the allowed usage flags depend on the key algorithm. </p>
<dt><code>cross-certify</code></p>
<dd> Add cross-certification signatures to signing subkeys that may not currently have them. Cross-certification signatures protect against a subtle attack against signing subkeys. See <code>&#8211;require-cross-certification</code>. All new keys generated have this signature by default, so this command is only useful to bring older keys up to date. </p>
<dt><code>save</code></p>
<dd> Save all changes to the keyrings and quit. </p>
<dt><code>quit</code></p>
<dd> Quit the program without updating the keyrings.</dl>
</dl>
<dl>
<dt>
<dd> The listing shows you the key with its secondary keys and all user IDs. The primary user ID is indicated by a dot, and selected keys or user IDs are indicated by an asterisk. The trust value is displayed with the primary key: &quot;trust&quot; is the assigned owner trust and &quot;validity&quot; is the calculated validity of the key. Validity values are also displayed for all user IDs. For possible values of trust, see: [trust-values].</dl>
<dt><code>&#8211;sign-key </code><i>name</i></p>
<dd> Signs a public key with your secret key. This is a shortcut version of the subcommand &quot;sign&quot; from <code>&#8211;edit</code>. </p>
<dt><code>&#8211;lsign-key </code><i>name</i></p>
<dd> Signs a public key with your secret key but marks it as non-exportable. This is a shortcut version of the subcommand &quot;lsign&quot; from <code>&#8211;edit-key</code>. </p>
<dt><code>&#8211;quick-sign-key </code><i>fpr</i> [<i>names</i>]</p>
<dd> <code>&#8211;quick-lsign-key </code><i>fpr</i> [<i>names</i>] Directly sign a key from the passphrase without any further user interaction. The <i>fpr</i> must be the verified primary fingerprint of a key in the local keyring. If no <i>names</i> are given, all useful user ids are signed; with given [<i>names</i>] only useful user ids matching one of theses names are signed. By default, or if a name is prefixed with a &#8216;*&#8217;, a case insensitive substring match is used. If a name is prefixed with a &#8216;=&#8217; a case sensitive exact match is done. </p>
<p> The command <code>&#8211;quick-lsign-key</code> marks the signatures as non-exportable. If such a non-exportable signature already exists the <code>&#8211;quick-sign-key</code> turns it into a exportable signature. </p>
<p> This command uses reasonable defaults and thus does not provide the full flexibility of the &quot;sign&quot; subcommand from <code>&#8211;edit-key</code>. Its intended use is to help unattended key signing by utilizing a list of verified fingerprints. </p>
<dt><code>&#8211;quick-add-uid </code><i>user-id</i> <i>new-user-id</i></p>
<dd> This command adds a new user id to an existing key. In contrast to the interactive sub-command <code>adduid</code> of <code>&#8211;edit-key</code> the <i>new-user-id</i> is added verbatim with only leading and trailing white space removed, it is expected to be UTF-8 encoded, and no checks on its form are applied. </p>
<dt><code>&#8211;quick-revoke-uid </code><i>user-id</i> <i>user-id-to-revoke</i></p>
<dd> This command revokes a user ID on an existing key. It cannot be used to revoke the last user ID on key (some non-revoked user ID must remain), with revocation reason &#8220;User ID is no longer valid&#8221;. If you want to specify a different revocation reason, or to supply supplementary revocation text, you should use the interactive sub-command <code>revuid</code> of <code>&#8211;edit-key</code>. </p>
<dt><code>&#8211;quick-revoke-sig </code><i>fpr</i> <i>signing-fpr</i> [<i>names</i>]</p>
<dd> This command revokes the key signatures made by <i>signing-fpr</i> from the key specified by the fingerprint <i>fpr</i>. With <i>names</i> given only the signatures on user ids of the key matching any of the given names are affected (see <code>&#8211;quick-sign-key</code>). If a revocation already exists a notice is printed instead of creating a new revocation; no error is returned in this case. Note that key signature revocations may be superseded by a newer key signature and in turn again revoked. </p>
<dt><code>&#8211;quick-set-primary-uid </code><i>user-id</i> <i>primary-user-id</i></p>
<dd> This command sets or updates the primary user ID flag on an existing key. <i>user-id</i> specifies the key and <i>primary-user-id</i> the user ID which shall be flagged as the primary user ID. The primary user ID flag is removed from all other user ids and the timestamp of all affected self-signatures is set one second ahead. </p>
<dt><code>&#8211;change-passphrase </code><i>user-id</i></p>
<dd> <code>&#8211;passwd </code><i>user-id</i> Change the passphrase of the secret key belonging to the certificate specified as <i>user-id</i>. This is a shortcut for the sub-command <code>passwd</code> of the edit key menu. When using together with the option <code>&#8211;dry-run</code> this will not actually change the passphrase but check that the current passphrase is correct. </p>
</dl>
<h2>OPTIONS</h2>
<p> <code>gpg</code> features a bunch of options to control the exact behaviour and to change the default configuration. </p>
<p> Long options can be put in an options file (default &quot;~/.gnupg/gpg.conf&quot;). Short option names will not work &#8211; for example, &quot;armor&quot; is a valid option for the options file, while &quot;a&quot; is not. Do not write the 2 dashes, but simply the name of the option and any required arguments. Lines with a hash (&#8216;#&#8217;) as the first non-white-space character are ignored. Commands may be put in this file too, but that is not generally useful as the command will execute automatically with every execution of gpg. </p>
<p> Please remember that option parsing stops as soon as a non-option is encountered, you can explicitly stop parsing by using the special option <code>&#8212;</code>. </p>
<h3>How to change the configuration</h3>
<p> &nbsp; </p>
<p> These options are used to change the configuration and are usually found in the option file. </p>
<dl>
<dt><code>&#8211;default-key </code><i>name</i></p>
<dd> Use <i>name</i> as the default key to sign with. If this option is not used, the default key is the first key found in the secret keyring. Note that <code>-u</code> or <code>&#8211;local-user</code> overrides this option. This option may be given multiple times. In this case, the last key for which a secret key is available is used. If there is no secret key available for any of the specified values, GnuPG will not emit an error message but continue as if this option wasn&#8217;t given. </p>
<dt><code>&#8211;default-recipient </code><i>name</i></p>
<dd> Use <i>name</i> as default recipient if option <code>&#8211;recipient</code> is not used and don&#8217;t ask if this is a valid one. <i>name</i> must be non-empty. </p>
<dt><code>&#8211;default-recipient-self</code></p>
<dd> Use the default key as default recipient if option <code>&#8211;recipient</code> is not used and don&#8217;t ask if this is a valid one. The default key is the first one from the secret keyring or the one set with <code>&#8211;default-key</code>. </p>
<dt><code>&#8211;no-default-recipient</code></p>
<dd> Reset <code>&#8211;default-recipient</code> and <code>&#8211;default-recipient-self</code>. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Give more information during processing. If used twice, the input data is listed in detail. </p>
<dt><code>&#8211;no-verbose</code></p>
<dd> Reset verbose level to 0. </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Try to be as quiet as possible. </p>
<dt><code>&#8211;batch</code></p>
<dd> <code>&#8211;no-batch</code> Use batch mode. Never ask, do not allow interactive commands. <code>&#8211;no-batch</code> disables this option. Note that even with a filename given on the command line, gpg might still need to read from STDIN (in particular if gpg figures that the input is a detached signature and no data file has been specified). Thus if you do not want to feed data via STDIN, you should connect STDIN to g&#8217;<i>/dev/null</i>&#8216;. </p>
<p> It is highly recommended to use this option along with the options <code>&#8211;status-fd</code> and <code>&#8211;with-colons</code> for any unattended use of <code>gpg</code>. </p>
<dt><code>&#8211;no-tty</code></p>
<dd> Make sure that the TTY (terminal) is never used for any output. This option is needed in some cases because GnuPG sometimes prints warnings to the TTY even if <code>&#8211;batch</code> is used. </p>
<dt><code>&#8211;yes</code></p>
<dd> Assume &quot;yes&quot; on most questions. </p>
<dt><code>&#8211;no</code></p>
<dd> Assume &quot;no&quot; on most questions. </p>
<dt><code>&#8211;list-options </code><i>parameters</i></p>
<dd> This is a space or comma delimited string that gives options used when listing keys and signatures (that is, <code>&#8211;list-keys</code>, <code>&#8211;check-signatures</code>, <code>&#8211;list-public-keys</code>, <code>&#8211;list-secret-keys</code>, and the <code>&#8211;edit-key</code> functions). Options can be prepended with a <code>no-</code> (after the two dashes) to give the opposite meaning. The options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>show-photos</code></p>
<dd> Causes <code>&#8211;list-keys</code>, <code>&#8211;check-signatures</code>, <code>&#8211;list-public-keys</code>, and <code>&#8211;list-secret-keys</code> to display any photo IDs attached to the key. Defaults to no. See also <code>&#8211;photo-viewer</code>. Does not work with <code>&#8211;with-colons</code>: see <code>&#8211;attribute-fd</code> for the appropriate way to get photo data for scripts and other frontends. </p>
<dt><code>show-usage</code></p>
<dd> Show usage information for keys and subkeys in the standard key listing. This is a list of letters indicating the allowed usage for a key (<code>E</code>=encryption, <code>S</code>=signing, <code>C</code>=certification, <code>A</code>=authentication). Defaults to yes. </p>
<dt><code>show-policy-urls</code></p>
<dd> Show policy URLs in the <code>&#8211;check-signatures</code> listings. Defaults to no. </p>
<dt><code>show-notations</code></p>
<dd> <code>show-std-notations</code> <code>show-user-notations</code> Show all, IETF standard, or user-defined signature notations in the <code>&#8211;check-signatures</code> listings. Defaults to no. </p>
<dt><code>show-keyserver-urls</code></p>
<dd> Show any preferred keyserver URL in the <code>&#8211;check-signatures</code> listings. Defaults to no. </p>
<dt><code>show-uid-validity</code></p>
<dd> Display the calculated validity of user IDs during key listings. Defaults to yes. </p>
<dt><code>show-unusable-uids</code></p>
<dd> Show revoked and expired user IDs in key listings. Defaults to no. </p>
<dt><code>show-unusable-subkeys</code></p>
<dd> Show revoked and expired subkeys in key listings. Defaults to no. </p>
<dt><code>show-keyring</code></p>
<dd> Display the keyring name at the head of key listings to show which keyring a given key resides on. Defaults to no. </p>
<dt><code>show-sig-expire</code></p>
<dd> Show signature expiration dates (if any) during <code>&#8211;check-signatures</code> listings. Defaults to no. </p>
<dt><code>show-sig-subpackets</code></p>
<dd> Include signature subpackets in the key listing. This option can take an optional argument list of the subpackets to list. If no argument is passed, list all subpackets. Defaults to no. This option is only meaningful when using <code>&#8211;with-colons</code> along with <code>&#8211;check-signatures</code>. </p>
<dt><code>show-only-fpr-mbox</code></p>
<dd> For each user-id which has a valid mail address print only the fingerprint followed by the mail address.</dl>
</dl>
<dt><code>&#8211;verify-options </code><i>parameters</i></p>
<dd> This is a space or comma delimited string that gives options used when verifying signatures. Options can be prepended with a `no-&#8216; to give the opposite meaning. The options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>show-photos</code></p>
<dd> Display any photo IDs present on the key that issued the signature. Defaults to no. See also <code>&#8211;photo-viewer</code>. </p>
<dt><code>show-policy-urls</code></p>
<dd> Show policy URLs in the signature being verified. Defaults to yes. </p>
<dt><code>show-notations</code></p>
<dd> <code>show-std-notations</code> <code>show-user-notations</code> Show all, IETF standard, or user-defined signature notations in the signature being verified. Defaults to IETF standard. </p>
<dt><code>show-keyserver-urls</code></p>
<dd> Show any preferred keyserver URL in the signature being verified. Defaults to yes. </p>
<dt><code>show-uid-validity</code></p>
<dd> Display the calculated validity of the user IDs on the key that issued the signature. Defaults to yes. </p>
<dt><code>show-unusable-uids</code></p>
<dd> Show revoked and expired user IDs during signature verification. Defaults to no. </p>
<dt><code>show-primary-uid-only</code></p>
<dd> Show only the primary user ID during signature verification. That is all the AKA lines as well as photo Ids are not shown with the signature verification status. </p>
<dt><code>pka-lookups</code></p>
<dd> Enable PKA lookups to verify sender addresses. Note that PKA is based on DNS, and so enabling this option may disclose information on when and what signatures are verified or to whom data is encrypted. This is similar to the &quot;web bug&quot; described for the <code>&#8211;auto-key-retrieve</code> option. </p>
<dt><code>pka-trust-increase</code></p>
<dd> Raise the trust in a signature to full if the signature passes PKA validation. This option is only meaningful if pka-lookups is set.</dl>
</dl>
<dt><code>&#8211;enable-large-rsa</code></p>
<dd> <code>&#8211;disable-large-rsa</code> With &#8211;generate-key and &#8211;batch, enable the creation of RSA secret keys as large as 8192 bit. Note: 8192 bit is more than is generally recommended. These large keys don&#8217;t significantly improve security, but they are more expensive to use, and their signatures and certifications are larger. This option is only available if the binary was build with large-secmem support. </p>
<dt><code>&#8211;enable-dsa2</code></p>
<dd> <code>&#8211;disable-dsa2</code> Enable hash truncation for all DSA keys even for old DSA Keys up to 1024 bit. This is also the default with <code>&#8211;openpgp</code>. Note that older versions of GnuPG also required this flag to allow the generation of DSA larger than 1024 bit. </p>
<dt><code>&#8211;photo-viewer </code><i>string</i></p>
<dd> This is the command line that should be run to view a photo ID. &quot;%i&quot; will be expanded to a filename containing the photo. &quot;%I&quot; does the same, except the file will not be deleted once the viewer exits. Other flags are &quot;%k&quot; for the key ID, &quot;%K&quot; for the long key ID, &quot;%f&quot; for the key fingerprint, &quot;%t&quot; for the extension of the image type (e.g. &quot;jpg&quot;), &quot;%T&quot; for the MIME type of the image (e.g. &quot;image/jpeg&quot;), &quot;%v&quot; for the single-character calculated validity of the image being viewed (e.g. &quot;f&quot;), &quot;%V&quot; for the calculated validity as a string (e.g. &quot;full&quot;), &quot;%U&quot; for a base32 encoded hash of the user ID, and &quot;%%&quot; for an actual percent sign. If neither %i or %I are present, then the photo will be supplied to the viewer on standard input. </p>
<p> On Unix the default viewer is <code>xloadimage -fork -quiet -title &#8216;KeyID 0x%k&#8217; STDIN</code> with a fallback to <code>display -title &#8216;KeyID 0x%k&#8217; %i</code> and finally to <code>xdg-open %i</code>. On Windows <code>!ShellExecute 400 %i</code> is used; here the command is a meta command to use that API call followed by a wait time in milliseconds which is used to give the viewer time to read the temporary image file before gpg deletes it again. Note that if your image viewer program is not secure, then executing it from gpg does not make it secure. </p>
<dt><code>&#8211;exec-path </code><i>string</i></p>
<dd> Sets a list of directories to search for photo viewers If not provided photo viewers use the <code>PATH</code> environment variable. </p>
<dt><code>&#8211;keyring </code><i>file</i></p>
<dd> Add <i>file</i> to the current list of keyrings. If <i>file</i> begins with a tilde and a slash, these are replaced by the $HOME directory. If the filename does not contain a slash, it is assumed to be in the GnuPG home directory (&quot;~/.gnupg&quot; if <code>&#8211;homedir</code> or $GNUPGHOME is not used). </p>
<p> Note that this adds a keyring to the current list. If the intent is to use the specified keyring alone, use <code>&#8211;keyring</code> along with <code>&#8211;no-default-keyring</code>. </p>
<p> If the option <code>&#8211;no-keyring</code> has been used no keyrings will be used at all. </p>
<dt><code>&#8211;secret-keyring </code><i>file</i></p>
<dd> This is an obsolete option and ignored. All secret keys are stored in the &#8216;<i>private-keys-v1.d</i>&#8216; directory below the GnuPG home directory. </p>
<dt><code>&#8211;primary-keyring </code><i>file</i></p>
<dd> Designate <i>file</i> as the primary public keyring. This means that newly imported keys (via <code>&#8211;import</code> or keyserver <code>&#8211;recv-from</code>) will go to this keyring. </p>
<dt><code>&#8211;trustdb-name </code><i>file</i></p>
<dd> Use <i>file</i> instead of the default trustdb. If <i>file</i> begins with a tilde and a slash, these are replaced by the $HOME directory. If the filename does not contain a slash, it is assumed to be in the GnuPG home directory (&#8216;<i>~/.gnupg</i>&#8216; if <code>&#8211;homedir</code> or $GNUPGHOME is not used). </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on Windows systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </p>
<p> On Windows systems it is possible to install GnuPG as a portable application. In this case only this command line option is considered, all other ways to set a home directory are ignored. </p>
<p> To install GnuPG as a portable application under Windows, create an empty file named &#8216;<i>gpgconf.ctl</i>&#8216; in the same directory as the tool &#8216;<i>gpgconf.exe</i>&#8216;. The root of the installation is then that directory; or, if &#8216;<i>gpgconf.exe</i>&#8216; has been installed directly below a directory named &#8216;<i>bin</i>&#8216;, its parent directory. You also need to make sure that the following directories exist and are writable: &#8216;<i>ROOT/home</i>&#8216; for the GnuPG home and &#8216;<i>ROOT/var/cache/gnupg</i>&#8216; for internal cache files. </p>
<dt><code>&#8211;display-charset </code><i>name</i></p>
<dd> Set the name of the native character set. This is used to convert some informational strings like user IDs to the proper UTF-8 encoding. Note that this has nothing to do with the character set of data to be encrypted or signed; GnuPG does not recode user-supplied data. If this option is not used, the default character set is determined from the current locale. A verbosity level of 3 shows the chosen set. Valid values for <i>name</i> are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>iso-8859-1</code></p>
<dd> This is the Latin 1 set. </p>
<dt><code>iso-8859-2</code></p>
<dd> The Latin 2 set. </p>
<dt><code>iso-8859-15</code></p>
<dd> This is currently an alias for the Latin 1 set. </p>
<dt><code>koi8-r</code></p>
<dd> The usual Russian set (RFC-1489). </p>
<dt><code>utf-8</code></p>
<dd> Bypass all translations and assume that the OS uses native UTF-8 encoding.</dl>
</dl>
<dt><code>&#8211;utf8-strings</code></p>
<dd> <code>&#8211;no-utf8-strings</code> Assume that command line arguments are given as UTF-8 strings. The default (<code>&#8211;no-utf8-strings</code>) is to assume that arguments are encoded in the character set as specified by <code>&#8211;display-charset</code>. These options affect all following arguments. Both options may be used multiple times. </p>
<dt><code>&#8211;options </code><i>file</i></p>
<dd> Read options from <i>file</i> and do not try to read them from the default options file in the homedir (see <code>&#8211;homedir</code>). This option is ignored if used in an options file. </p>
<dt><code>&#8211;no-options</code></p>
<dd> Shortcut for <code>&#8211;options /dev/null</code>. This option is detected before an attempt to open an option file. Using this option will also prevent the creation of a &#8216;<i>~/.gnupg</i>&#8216; homedir. </p>
<dt><code>-z </code><i>n</i></p>
<dd> <code>&#8211;compress-level </code><i>n</i> <code>&#8211;bzip2-compress-level </code><i>n</i> Set compression level to <i>n</i> for the ZIP and ZLIB compression algorithms. The default is to use the default compression level of zlib (normally 6). <code>&#8211;bzip2-compress-level</code> sets the compression level for the BZIP2 compression algorithm (defaulting to 6 as well). This is a different option from <code>&#8211;compress-level</code> since BZIP2 uses a significant amount of memory for each additional compression level. <code>-z</code> sets both. A value of 0 for <i>n</i> disables compression. </p>
<dt><code>&#8211;bzip2-decompress-lowmem</code></p>
<dd> Use a different decompression method for BZIP2 compressed files. This alternate method uses a bit more than half the memory, but also runs at half the speed. This is useful under extreme low memory circumstances when the file was originally compressed at a high <code>&#8211;bzip2-compress-level</code>. </p>
<dt><code>&#8211;mangle-dos-filenames</code></p>
<dd> <code>&#8211;no-mangle-dos-filenames</code> Older version of Windows cannot handle filenames with more than one dot. <code>&#8211;mangle-dos-filenames</code> causes GnuPG to replace (rather than add to) the extension of an output filename to avoid this problem. This option is off by default and has no effect on non-Windows platforms. </p>
<dt><code>&#8211;ask-cert-level</code></p>
<dd> <code>&#8211;no-ask-cert-level</code> When making a key signature, prompt for a certification level. If this option is not specified, the certification level used is set via <code>&#8211;default-cert-level</code>. See <code>&#8211;default-cert-level</code> for information on the specific levels and how they are used. <code>&#8211;no-ask-cert-level</code> disables this option. This option defaults to no. </p>
<dt><code>&#8211;default-cert-level </code><i>n</i></p>
<dd> The default to use for the check level when signing a key. </p>
<p> 0 means you make no particular claim as to how carefully you verified the key. </p>
<p> 1 means you believe the key is owned by the person who claims to own it but you could not, or did not verify the key at all. This is useful for a &quot;persona&quot; verification, where you sign the key of a pseudonymous user. </p>
<p> 2 means you did casual verification of the key. For example, this could mean that you verified the key fingerprint and checked the user ID on the key against a photo ID. </p>
<p> 3 means you did extensive verification of the key. For example, this could mean that you verified the key fingerprint with the owner of the key in person, and that you checked, by means of a hard to forge document with a photo ID (such as a passport) that the name of the key owner matches the name in the user ID on the key, and finally that you verified (by exchange of email) that the email address on the key belongs to the key owner. </p>
<p> Note that the examples given above for levels 2 and 3 are just that: examples. In the end, it is up to you to decide just what &quot;casual&quot; and &quot;extensive&quot; mean to you. </p>
<p> This option defaults to 0 (no particular claim). </p>
<dt><code>&#8211;min-cert-level</code></p>
<dd> When building the trust database, treat any signatures with a certification level below this as invalid. Defaults to 2, which disregards level 1 signatures. Note that level 0 &quot;no particular claim&quot; signatures are always accepted. </p>
<dt><code>&#8211;trusted-key </code><i>long key ID or fingerprint</i></p>
<dd> Assume that the specified key (which must be given as a full 8 byte key ID or 20 byte fingerprint) is as trustworthy as one of your own secret keys. This option is useful if you don&#8217;t want to keep your secret keys (or one of them) online but still want to be able to check the validity of a given recipient&#8217;s or signator&#8217;s key. </p>
<dt><code>&#8211;trust-model {pgp|classic|tofu|tofu+pgp|direct|always|auto}</code></p>
<dd> Set what trust model GnuPG should follow. The models are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>pgp</code></p>
<dd> This is the Web of Trust combined with trust signatures as used in PGP 5.x and later. This is the default trust model when creating a new trust database. </p>
<dt><code>classic</code></p>
<dd> This is the standard Web of Trust as introduced by PGP 2. </p>
<dt><code>tofu</code></p>
<dd>
<p> TOFU stands for Trust On First Use. In this trust model, the first time a key is seen, it is memorized. If later another key with a user id with the same email address is seen, both keys are marked as suspect. In that case, the next time either is used, a warning is displayed describing the conflict, why it might have occurred (either the user generated a new key and failed to cross sign the old and new keys, the key is forgery, or a man-in-the-middle attack is being attempted), and the user is prompted to manually confirm the validity of the key in question. </p>
<p> Because a potential attacker is able to control the email address and thereby circumvent the conflict detection algorithm by using an email address that is similar in appearance to a trusted email address, whenever a message is verified, statistics about the number of messages signed with the key are shown. In this way, a user can easily identify attacks using fake keys for regular correspondents. </p>
<p> When compared with the Web of Trust, TOFU offers significantly weaker security guarantees. In particular, TOFU only helps ensure consistency (that is, that the binding between a key and email address doesn&#8217;t change). A major advantage of TOFU is that it requires little maintenance to use correctly. To use the web of trust properly, you need to actively sign keys and mark users as trusted introducers. This is a time-consuming process and anecdotal evidence suggests that even security-conscious users rarely take the time to do this thoroughly and instead rely on an ad-hoc TOFU process. </p>
<p> In the TOFU model, policies are associated with bindings between keys and email addresses (which are extracted from user ids and normalized). There are five policies, which can be set manually using the <code>&#8211;tofu-policy</code> option. The default policy can be set using the <code>&#8211;tofu-default-policy</code> option. </p>
<p> The TOFU policies are: <code>auto</code>, <code>good</code>, <code>unknown</code>, <code>bad</code> and <code>ask</code>. The <code>auto</code> policy is used by default (unless overridden by <code>&#8211;tofu-default-policy</code>) and marks a binding as marginally trusted. The <code>good</code>, <code>unknown</code> and <code>bad</code> policies mark a binding as fully trusted, as having unknown trust or as having trust never, respectively. The <code>unknown</code> policy is useful for just using TOFU to detect conflicts, but to never assign positive trust to a binding. The final policy, <code>ask</code> prompts the user to indicate the binding&#8217;s trust. If batch mode is enabled (or input is inappropriate in the context), then the user is not prompted and the <code>undefined</code> trust level is returned. </p>
<dt><code>tofu+pgp</code></p>
<dd> This trust model combines TOFU with the Web of Trust. This is done by computing the trust level for each model and then taking the maximum trust level where the trust levels are ordered as follows: <code>unknown &lt; undefined &lt; marginal &lt; fully &lt; ultimate &lt; expired &lt; never</code>. </p>
<p> By setting <code>&#8211;tofu-default-policy=unknown</code>, this model can be used to implement the web of trust with TOFU&#8217;s conflict detection algorithm, but without its assignment of positive trust values, which some security-conscious users don&#8217;t like. </p>
<dt><code>direct</code></p>
<dd> Key validity is set directly by the user and not calculated via the Web of Trust. This model is solely based on the key and does not distinguish user IDs. Note that when changing to another trust model the trust values assigned to a key are transformed into ownertrust values, which also indicate how you trust the owner of the key to sign other keys. </p>
<dt><code>always</code></p>
<dd> Skip key validation and assume that used keys are always fully valid. You generally won&#8217;t use this unless you are using some external validation scheme. This option also suppresses the &quot;[uncertain]&quot; tag printed with signature checks when there is no evidence that the user ID is bound to the key. Note that this trust model still does not allow the use of expired, revoked, or disabled keys. </p>
<dt><code>auto</code></p>
<dd> Select the trust model depending on whatever the internal trust database says. This is the default model if such a database already exists. Note that a tofu trust model is not considered here and must be enabled explicitly.</dl>
</dl>
<dt><code>&#8211;auto-key-locate </code><i>mechanisms</i></p>
<dd> <code>&#8211;no-auto-key-locate</code> GnuPG can automatically locate and retrieve keys as needed using this option. This happens when encrypting to an email address (in the &quot;user [at] example.com&quot; form), and there are no &quot;user [at] example.com&quot; keys on the local keyring. This option takes any number of the mechanisms listed below, in the order they are to be tried. Instead of listing the mechanisms as comma delimited arguments, the option may also be given several times to add more mechanism. The option <code>&#8211;no-auto-key-locate</code> or the mechanism &quot;clear&quot; resets the list. The default is &quot;local,wkd&quot;. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cert</code></p>
<dd> Locate a key using DNS CERT, as specified in RFC-4398. </p>
<dt><code>pka</code></p>
<dd> Locate a key using DNS PKA. </p>
<dt><code>dane</code></p>
<dd> Locate a key using DANE, as specified in draft-ietf-dane-openpgpkey-05.txt. </p>
<dt><code>wkd</code></p>
<dd> Locate a key using the Web Key Directory protocol. </p>
<dt><code>ldap</code></p>
<dd> Using DNS Service Discovery, check the domain in question for any LDAP keyservers to use. If this fails, attempt to locate the key using the PGP Universal method of checking &#8216;<a href="ldap://keys.(thedomain)'.">ldap://keys.(thedomain)&#8217;.</a> </p>
<dt><code>ntds</code></p>
<dd> Locate the key using the Active Directory (Windows only). </p>
<dt><code>keyserver</code></p>
<dd> Locate a key using a keyserver. </p>
<dt><code>keyserver-URL</code></p>
<dd> In addition, a keyserver URL as used in the <code>dirmngr</code> configuration may be used here to query that particular keyserver. </p>
<dt><code>local</code></p>
<dd> Locate the key using the local keyrings. This mechanism allows the user to select the order a local key lookup is done. Thus using &#8216;&#8211;auto-key-locate local&#8217; is identical to <code>&#8211;no-auto-key-locate</code>. </p>
<dt><code>nodefault</code></p>
<dd> This flag disables the standard local key lookup, done before any of the mechanisms defined by the <code>&#8211;auto-key-locate</code> are tried. The position of this mechanism in the list does not matter. It is not required if <code>local</code> is also used. </p>
<dt><code>clear</code></p>
<dd> Clear all defined mechanisms. This is useful to override mechanisms given in a config file. Note that a <code>nodefault</code> in <i>mechanisms</i> will also be cleared unless it is given after the <code>clear</code>. </p>
</dl>
</dl>
<dt><code>&#8211;auto-key-import</code></p>
<dd> <code>&#8211;no-auto-key-import</code> This is an offline mechanism to get a missing key for signature verification and for later encryption to this key. If this option is enabled and a signature includes an embedded key, that key is used to verify the signature and on verification success that key is imported. The default is <code>&#8211;no-auto-key-import</code>. </p>
<p> On the sender (signing) site the option <code>&#8211;include-key-block</code> needs to be used to put the public part of the signing key as “Key Block subpacket” into the signature. </p>
<dt><code>&#8211;auto-key-retrieve</code></p>
<dd> <code>&#8211;no-auto-key-retrieve</code> These options enable or disable the automatic retrieving of keys from a keyserver when verifying signatures made by keys that are not on the local keyring. The default is <code>&#8211;no-auto-key-retrieve</code>. </p>
<p> The order of methods tried to lookup the key is: </p>
<p> 1. If the option <code>&#8211;auto-key-import</code> is set and the signatures includes an embedded key, that key is used to verify the signature and on verification success that key is imported. </p>
<p> 2. If a preferred keyserver is specified in the signature and the option <code>honor-keyserver-url</code> is active (which is not the default), that keyserver is tried. Note that the creator of the signature uses the option <code>&#8211;sig-keyserver-url</code> to specify the preferred keyserver for data signatures. </p>
<p> 3. If the signature has the Signer&#8217;s UID set (e.g. using <code>&#8211;sender</code> while creating the signature) a Web Key Directory (WKD) lookup is done. This is the default configuration but can be disabled by removing WKD from the auto-key-locate list or by using the option <code>&#8211;disable-signer-uid</code>. </p>
<p> 4. If the option <code>honor-pka-record</code> is active, the legacy PKA method is used. </p>
<p> 5. If any keyserver is configured and the Issuer Fingerprint is part of the signature (since GnuPG 2.1.16), the configured keyservers are tried. </p>
<p> Note that this option makes a &quot;web bug&quot; like behavior possible. Keyserver or Web Key Directory operators can see which keys you request, so by sending you a message signed by a brand new key (which you naturally will not have on your local keyring), the operator can tell both your IP address and the time when you verified the signature. </p>
<dt><code>&#8211;keyid-format {none|short|0xshort|long|0xlong}</code></p>
<dd> Select how to display key IDs. &quot;none&quot; does not show the key ID at all but shows the fingerprint in a separate line. &quot;short&quot; is the traditional 8-character key ID. &quot;long&quot; is the more accurate (but less convenient) 16-character key ID. Add an &quot;0x&quot; to either to include an &quot;0x&quot; at the beginning of the key ID, as in 0x99242560. Note that this option is ignored if the option <code>&#8211;with-colons</code> is used. </p>
<dt><code>&#8211;keyserver </code><i>name</i></p>
<dd> This option is deprecated &#8211; please use the <code>&#8211;keyserver</code> in &#8216;<i>dirmngr.conf</i>&#8216; instead. </p>
<p> Use <i>name</i> as your keyserver. This is the server that <code>&#8211;receive-keys</code>, <code>&#8211;send-keys</code>, and <code>&#8211;search-keys</code> will communicate with to receive keys from, send keys to, and search for keys on. The format of the <i>name</i> is a URI: `scheme:[//]keyservername[:port]&#8217; The scheme is the type of keyserver: &quot;hkp&quot; for the HTTP (or compatible) keyservers, &quot;ldap&quot; for the LDAP keyservers, or &quot;mailto&quot; for the Graff email keyserver. Note that your particular installation of GnuPG may have other keyserver types available as well. Keyserver schemes are case-insensitive. After the keyserver name, optional keyserver configuration options may be provided. These are the same as the global <code>&#8211;keyserver-options</code> from below, but apply only to this particular keyserver. </p>
<p> Most keyservers synchronize with each other, so there is generally no need to send keys to more than one server. The keyserver <code><a href="hkp://keys.gnupg.net">hkp://keys.gnupg.net</a></code> uses round robin DNS to give a different keyserver each time you use it. </p>
<dt><code>&#8211;keyserver-options {</code><i>name</i>=<i>value</i>}</p>
<dd> This is a space or comma delimited string that gives options for the keyserver. Options can be prefixed with a `no-&#8216; to give the opposite meaning. Valid import-options or export-options may be used here as well to apply to importing (<code>&#8211;recv-key</code>) or exporting (<code>&#8211;send-key</code>) a key from a keyserver. While not all options are available for all keyserver types, some common options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>include-revoked</code></p>
<dd> When searching for a key with <code>&#8211;search-keys</code>, include keys that are marked on the keyserver as revoked. Note that not all keyservers differentiate between revoked and unrevoked keys, and for such keyservers this option is meaningless. Note also that most keyservers do not have cryptographic verification of key revocations, and so turning this option off may result in skipping keys that are incorrectly marked as revoked. </p>
<dt><code>include-disabled</code></p>
<dd> When searching for a key with <code>&#8211;search-keys</code>, include keys that are marked on the keyserver as disabled. Note that this option is not used with HKP keyservers. </p>
<dt><code>auto-key-retrieve</code></p>
<dd> This is an obsolete alias for the option <code>auto-key-retrieve</code>. Please do not use it; it will be removed in future versions.. </p>
<dt><code>honor-keyserver-url</code></p>
<dd> When using <code>&#8211;refresh-keys</code>, if the key in question has a preferred keyserver URL, then use that preferred keyserver to refresh the key from. In addition, if auto-key-retrieve is set, and the signature being verified has a preferred keyserver URL, then use that preferred keyserver to fetch the key from. Note that this option introduces a &quot;web bug&quot;: The creator of the key can see when the keys is refreshed. Thus this option is not enabled by default. </p>
<dt><code>honor-pka-record</code></p>
<dd> If <code>&#8211;auto-key-retrieve</code> is used, and the signature being verified has a PKA record, then use the PKA information to fetch the key. Defaults to &quot;yes&quot;. </p>
<dt><code>include-subkeys</code></p>
<dd> When receiving a key, include subkeys as potential targets. Note that this option is not used with HKP keyservers, as they do not support retrieving keys by subkey id. </p>
<dt><code>timeout</code></p>
<dd> <code>http-proxy=</code><i>value</i> <code>verbose</code> <code>debug</code> <code>check-cert</code></p>
<dt><code>ca-cert-file</code></p>
<dd> These options have no more function since GnuPG 2.1. Use the <code>dirmngr</code> configuration options instead. </p>
</dl>
</dl>
<p> The default list of options is: &quot;self-sigs-only, repair-keys, repair-pks-subkey-bug, export-attributes, honor-pka-record&quot;. </p>
<dt><code>&#8211;completes-needed </code><i>n</i></p>
<dd> Number of completely trusted users to introduce a new key signer (defaults to 1). </p>
<dt><code>&#8211;marginals-needed </code><i>n</i></p>
<dd> Number of marginally trusted users to introduce a new key signer (defaults to 3) </p>
<dt><code>&#8211;tofu-default-policy {auto|good|unknown|bad|ask}</code></p>
<dd> The default TOFU policy (defaults to <code>auto</code>). For more information about the meaning of this option, see: [trust-model-tofu]. </p>
<dt><code>&#8211;max-cert-depth </code><i>n</i></p>
<dd> Maximum depth of a certification chain (default is 5). </p>
<dt><code>&#8211;no-sig-cache</code></p>
<dd> Do not cache the verification status of key signatures. Caching gives a much better performance in key listings. However, if you suspect that your public keyring is not safe against write modifications, you can use this option to disable the caching. It probably does not make sense to disable it because all kind of damage can be done if someone else has write access to your public keyring. </p>
<dt><code>&#8211;auto-check-trustdb</code></p>
<dd> <code>&#8211;no-auto-check-trustdb</code> If GnuPG feels that its information about the Web of Trust has to be updated, it automatically runs the <code>&#8211;check-trustdb</code> command internally. This may be a time consuming process. <code>&#8211;no-auto-check-trustdb</code> disables this option. </p>
<dt><code>&#8211;use-agent</code></p>
<dd> <code>&#8211;no-use-agent</code> This is dummy option. <code>gpg</code> always requires the agent. </p>
<dt><code>&#8211;gpg-agent-info</code></p>
<dd> This is dummy option. It has no effect when used with <code>gpg</code>. </p>
<dt><code>&#8211;agent-program </code><i>file</i></p>
<dd> Specify an agent program to be used for secret key operations. The default value is determined by running <code>gpgconf</code> with the option <code>&#8211;list-dirs</code>. Note that the pipe symbol (<code>|</code>) is used for a regression test suite hack and may thus not be used in the file name. </p>
<dt><code>&#8211;dirmngr-program </code><i>file</i></p>
<dd> Specify a dirmngr program to be used for keyserver access. The default value is &#8216;<i>/usr/bin/dirmngr</i>&#8216;. </p>
<dt><code>&#8211;disable-dirmngr</code></p>
<dd> Entirely disable the use of the Dirmngr. </p>
<dt><code>&#8211;no-autostart</code></p>
<dd> Do not start the gpg-agent or the dirmngr if it has not yet been started and its service is required. This option is mostly useful on machines where the connection to gpg-agent has been redirected to another machines. If dirmngr is required on the remote machine, it may be started manually using <code>gpgconf &#8211;launch dirmngr</code>. </p>
<dt><code>&#8211;lock-once</code></p>
<dd> Lock the databases the first time a lock is requested and do not release the lock until the process terminates. </p>
<dt><code>&#8211;lock-multiple</code></p>
<dd> Release the locks every time a lock is no longer needed. Use this to override a previous <code>&#8211;lock-once</code> from a config file. </p>
<dt><code>&#8211;lock-never</code></p>
<dd> Disable locking entirely. This option should be used only in very special environments, where it can be assured that only one process is accessing those files. A bootable floppy with a stand-alone encryption system will probably use this. Improper usage of this option may lead to data and key corruption. </p>
<dt><code>&#8211;exit-on-status-write-error</code></p>
<dd> This option will cause write errors on the status FD to immediately terminate the process. That should in fact be the default but it never worked this way and thus we need an option to enable this, so that the change won&#8217;t break applications which close their end of a status fd connected pipe too early. Using this option along with <code>&#8211;enable-progress-filter</code> may be used to cleanly cancel long running gpg operations. </p>
<dt><code>&#8211;limit-card-insert-tries </code><i>n</i></p>
<dd> With <i>n</i> greater than 0 the number of prompts asking to insert a smartcard gets limited to N-1. Thus with a value of 1 gpg won&#8217;t at all ask to insert a card if none has been inserted at startup. This option is useful in the configuration file in case an application does not know about the smartcard support and waits ad infinitum for an inserted card. </p>
<dt><code>&#8211;no-random-seed-file</code></p>
<dd> GnuPG uses a file to store its internal random pool over invocations. This makes random generation faster; however sometimes write operations are not desired. This option can be used to achieve that with the cost of slower random generation. </p>
<dt><code>&#8211;no-greeting</code></p>
<dd> Suppress the initial copyright message. </p>
<dt><code>&#8211;no-secmem-warning</code></p>
<dd> Suppress the warning about &quot;using insecure memory&quot;. </p>
<dt><code>&#8211;no-permission-warning</code></p>
<dd> Suppress the warning about unsafe file and home directory (<code>&#8211;homedir</code>) permissions. Note that the permission checks that GnuPG performs are not intended to be authoritative, but rather they simply warn about certain common permission problems. Do not assume that the lack of a warning means that your system is secure. </p>
<p> Note that the warning for unsafe <code>&#8211;homedir</code> permissions cannot be suppressed in the gpg.conf file, as this would allow an attacker to place an unsafe gpg.conf file in place, and use this file to suppress warnings about itself. The <code>&#8211;homedir</code> permissions warning may only be suppressed on the command line. </p>
<dt><code>&#8211;require-secmem</code></p>
<dd> <code>&#8211;no-require-secmem</code> Refuse to run if GnuPG cannot get secure memory. Defaults to no (i.e. run, but give a warning). </p>
<dt><code>&#8211;require-cross-certification</code></p>
<dd> <code>&#8211;no-require-cross-certification</code> When verifying a signature made from a subkey, ensure that the cross certification &quot;back signature&quot; on the subkey is present and valid. This protects against a subtle attack against subkeys that can sign. Defaults to <code>&#8211;require-cross-certification</code> for <code>gpg</code>. </p>
<dt><code>&#8211;expert</code></p>
<dd> <code>&#8211;no-expert</code> Allow the user to do certain nonsensical or &quot;silly&quot; things like signing an expired or revoked key, or certain potentially incompatible things like generating unusual key types. This also disables certain warning messages about potentially incompatible actions. As the name implies, this option is for experts only. If you don&#8217;t fully understand the implications of what it allows you to do, leave this off. <code>&#8211;no-expert</code> disables this option. </p>
</dl>
<h3>Key related options</h3>
<p> &nbsp; </p>
<dl>
<dt><code>&#8211;recipient </code><i>name</i></p>
<dd> <code>-r</code> Encrypt for user id <i>name</i>. If this option or <code>&#8211;hidden-recipient</code> is not specified, GnuPG asks for the user-id unless <code>&#8211;default-recipient</code> is given. </p>
<dt><code>&#8211;hidden-recipient </code><i>name</i></p>
<dd> <code>-R</code> Encrypt for user ID <i>name</i>, but hide the key ID of this user&#8217;s key. This option helps to hide the receiver of the message and is a limited countermeasure against traffic analysis. If this option or <code>&#8211;recipient</code> is not specified, GnuPG asks for the user ID unless <code>&#8211;default-recipient</code> is given. </p>
<dt><code>&#8211;recipient-file </code><i>file</i></p>
<dd> <code>-f</code> This option is similar to <code>&#8211;recipient</code> except that it encrypts to a key stored in the given file. <i>file</i> must be the name of a file containing exactly one key. <code>gpg</code> assumes that the key in this file is fully valid. </p>
<dt><code>&#8211;hidden-recipient-file </code><i>file</i></p>
<dd> <code>-F</code> This option is similar to <code>&#8211;hidden-recipient</code> except that it encrypts to a key stored in the given file. <i>file</i> must be the name of a file containing exactly one key. <code>gpg</code> assumes that the key in this file is fully valid. </p>
<dt><code>&#8211;encrypt-to </code><i>name</i></p>
<dd> Same as <code>&#8211;recipient</code> but this one is intended for use in the options file and may be used with your own user-id as an &quot;encrypt-to-self&quot;. These keys are only used when there are other recipients given either by use of <code>&#8211;recipient</code> or by the asked user id. No trust checking is performed for these user ids and even disabled keys can be used. </p>
<dt><code>&#8211;hidden-encrypt-to </code><i>name</i></p>
<dd> Same as <code>&#8211;hidden-recipient</code> but this one is intended for use in the options file and may be used with your own user-id as a hidden &quot;encrypt-to-self&quot;. These keys are only used when there are other recipients given either by use of <code>&#8211;recipient</code> or by the asked user id. No trust checking is performed for these user ids and even disabled keys can be used. </p>
<dt><code>&#8211;no-encrypt-to</code></p>
<dd> Disable the use of all <code>&#8211;encrypt-to</code> and <code>&#8211;hidden-encrypt-to</code> keys. </p>
<dt><code>&#8211;group {</code><i>name</i>=<i>value</i>}</p>
<dd> Sets up a named group, which is similar to aliases in email programs. Any time the group name is a recipient (<code>-r</code> or <code>&#8211;recipient</code>), it will be expanded to the values specified. Multiple groups with the same name are automatically merged into a single group. </p>
<p> The values are <code>key IDs</code> or fingerprints, but any key description is accepted. Note that a value with spaces in it will be treated as two different values. Note also there is only one level of expansion &#8212; you cannot make an group that points to another group. When used from the command line, it may be necessary to quote the argument to this option to prevent the shell from treating it as multiple arguments. </p>
<dt><code>&#8211;ungroup </code><i>name</i></p>
<dd> Remove a given entry from the <code>&#8211;group</code> list. </p>
<dt><code>&#8211;no-groups</code></p>
<dd> Remove all entries from the <code>&#8211;group</code> list. </p>
<dt><code>&#8211;local-user </code><i>name</i></p>
<dd> <code>-u</code> Use <i>name</i> as the key to sign with. Note that this option overrides <code>&#8211;default-key</code>. </p>
<dt><code>&#8211;sender </code><i>mbox</i></p>
<dd> This option has two purposes. <i>mbox</i> must either be a complete user id with a proper mail address or just a mail address. When creating a signature this option tells gpg the user id of a key used to make a signature if the key was not directly specified by a user id. When verifying a signature the <i>mbox</i> is used to restrict the information printed by the TOFU code to matching user ids. </p>
<dt><code>&#8211;try-secret-key </code><i>name</i></p>
<dd> For hidden recipients GPG needs to know the keys to use for trial decryption. The key set with <code>&#8211;default-key</code> is always tried first, but this is often not sufficient. This option allows setting more keys to be used for trial decryption. Although any valid user-id specification may be used for <i>name</i> it makes sense to use at least the long keyid to avoid ambiguities. Note that gpg-agent might pop up a pinentry for a lot keys to do the trial decryption. If you want to stop all further trial decryption you may use close-window button instead of the cancel button. </p>
<dt><code>&#8211;try-all-secrets</code></p>
<dd> Don&#8217;t look at the key ID as stored in the message but try all secret keys in turn to find the right decryption key. This option forces the behaviour as used by anonymous recipients (created by using <code>&#8211;throw-keyids</code> or <code>&#8211;hidden-recipient</code>) and might come handy in case where an encrypted message contains a bogus key ID. </p>
<dt><code>&#8211;skip-hidden-recipients</code></p>
<dd> <code>&#8211;no-skip-hidden-recipients</code> During decryption skip all anonymous recipients. This option helps in the case that people use the hidden recipients feature to hide their own encrypt-to key from others. If one has many secret keys this may lead to a major annoyance because all keys are tried in turn to decrypt something which was not really intended for it. The drawback of this option is that it is currently not possible to decrypt a message which includes real anonymous recipients. </p>
</dl>
<h3>Input and Output</h3>
<p> &nbsp; </p>
<dl>
<dt><code>&#8211;armor</code></p>
<dd> <code>-a</code> Create ASCII armored output. The default is to create the binary OpenPGP format. </p>
<dt><code>&#8211;no-armor</code></p>
<dd> Assume the input data is not in ASCII armored format. </p>
<dt><code>&#8211;output </code><i>file</i></p>
<dd> <code>-o </code><i>file</i> Write output to <i>file</i>. To write to stdout use <code>&#8211;</code> as the filename. </p>
<dt><code>&#8211;max-output </code><i>n</i></p>
<dd> This option sets a limit on the number of bytes that will be generated when processing a file. Since OpenPGP supports various levels of compression, it is possible that the plaintext of a given message may be significantly larger than the original OpenPGP message. While GnuPG works properly with such messages, there is often a desire to set a maximum file size that will be generated before processing is forced to stop by the OS limits. Defaults to 0, which means &quot;no limit&quot;. </p>
<dt><code>&#8211;input-size-hint </code><i>n</i></p>
<dd> This option can be used to tell GPG the size of the input data in bytes. <i>n</i> must be a positive base-10 number. This option is only useful if the input is not taken from a file. GPG may use this hint to optimize its buffer allocation strategy. It is also used by the <code>&#8211;status-fd</code> line &#8220;PROGRESS&#8221; to provide a value for &#8220;total&#8221; if that is not available by other means. </p>
<dt><code>&#8211;key-origin </code><i>string</i>[,<i>url</i>]</p>
<dd> gpg can track the origin of a key. Certain origins are implicitly known (e.g. keyserver, web key directory) and set. For a standard import the origin of the keys imported can be set with this option. To list the possible values use &quot;help&quot; for <i>string</i>. Some origins can store an optional <i>url</i> argument. That URL can appended to <i>string</i> after a comma. </p>
<dt><code>&#8211;import-options </code><i>parameters</i></p>
<dd> This is a space or comma delimited string that gives options for importing keys. Options can be prepended with a `no-&#8216; to give the opposite meaning. The options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>import-local-sigs</code></p>
<dd> Allow importing key signatures marked as &quot;local&quot;. This is not generally useful unless a shared keyring scheme is being used. Defaults to no. </p>
<dt><code>keep-ownertrust</code></p>
<dd> Normally possible still existing ownertrust values of a key are cleared if a key is imported. This is in general desirable so that a formerly deleted key does not automatically gain an ownertrust values merely due to import. On the other hand it is sometimes necessary to re-import a trusted set of keys again but keeping already assigned ownertrust values. This can be achieved by using this option. </p>
<dt><code>repair-pks-subkey-bug</code></p>
<dd> During import, attempt to repair the damage caused by the PKS keyserver bug (pre version 0.9.6) that mangles keys with multiple subkeys. Note that this cannot completely repair the damaged key as some crucial data is removed by the keyserver, but it does at least give you back one subkey. Defaults to no for regular <code>&#8211;import</code> and to yes for keyserver <code>&#8211;receive-keys</code>. </p>
<dt><code>import-show</code></p>
<dd> <code>show-only</code> Show a listing of the key as imported right before it is stored. This can be combined with the option <code>&#8211;dry-run</code> to only look at keys; the option <code>show-only</code> is a shortcut for this combination. The command <code>&#8211;show-keys</code> is another shortcut for this. Note that suffixes like &#8216;#&#8217; for &quot;sec&quot; and &quot;sbb&quot; lines may or may not be printed. </p>
<dt><code>import-export</code></p>
<dd> Run the entire import code but instead of storing the key to the local keyring write it to the output. The export options <code>export-pka</code> and <code>export-dane</code> affect the output. This option can be used to remove all invalid parts from a key without the need to store it. </p>
<dt><code>merge-only</code></p>
<dd> During import, allow key updates to existing keys, but do not allow any new keys to be imported. Defaults to no. </p>
<dt><code>import-clean</code></p>
<dd> After import, compact (remove all signatures except the self-signature) any user IDs from the new key that are not usable. Then, remove any signatures from the new key that are not usable. This includes signatures that were issued by keys that are not present on the keyring. This option is the same as running the <code>&#8211;edit-key</code> command &quot;clean&quot; after import. Defaults to no. </p>
<dt><code>self-sigs-only</code></p>
<dd> Accept only self-signatures while importing a key. All other key signatures are skipped at an early import stage. This option can be used with <code>keyserver-options</code> to mitigate attempts to flood a key with bogus signatures from a keyserver. The drawback is that all other valid key signatures, as required by the Web of Trust are also not imported. Note that when using this option along with import-clean it suppresses the final clean step after merging the imported key into the existing key. </p>
<dt><code>repair-keys</code></p>
<dd> After import, fix various problems with the keys. For example, this reorders signatures, and strips duplicate signatures. Defaults to yes. </p>
<dt><code>import-minimal</code></p>
<dd> Import the smallest key possible. This removes all signatures except the most recent self-signature on each user ID. This option is the same as running the <code>&#8211;edit-key</code> command &quot;minimize&quot; after import. Defaults to no. </p>
<dt><code>restore</code></p>
<dd> <code>import-restore</code> Import in key restore mode. This imports all data which is usually skipped during import; including all GnuPG specific data. All other contradicting options are overridden.</dl>
</dl>
<dt><code>&#8211;import-filter {</code><i>name</i>=<i>expr</i>}</p>
<dd> <code>&#8211;export-filter {</code><i>name</i>=<i>expr</i>} These options define an import/export filter which are applied to the imported/exported keyblock right before it will be stored/written. <i>name</i> defines the type of filter to use, <i>expr</i> the expression to evaluate. The option can be used several times which then appends more expression to the same <i>name</i>. </p>
<p> The available filter types are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>keep-uid</code></p>
<dd> This filter will keep a user id packet and its dependent packets in the keyblock if the expression evaluates to true. </p>
<dt><code>drop-subkey</code></p>
<dd> This filter drops the selected subkeys. Currently only implemented for &#8211;export-filter. </p>
<dt><code>drop-sig</code></p>
<dd> This filter drops the selected key signatures on user ids. Self-signatures are not considered. Currently only implemented for &#8211;import-filter. </p>
</dl>
</dl>
<p> For the syntax of the expression see the chapter &quot;FILTER EXPRESSIONS&quot;. The property names for the expressions depend on the actual filter type and are indicated in the following table. </p>
<p> The available properties are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>uid</code></p>
<dd> A string with the user id. (keep-uid) </p>
<dt><code>mbox</code></p>
<dd> The addr-spec part of a user id with mailbox or the empty string. (keep-uid) </p>
<dt><code>key_algo</code></p>
<dd> A number with the public key algorithm of a key or subkey packet. (drop-subkey) </p>
<dt><code>key_created</code></p>
<dd> <code>key_created_d</code> The first is the timestamp a public key or subkey packet was created. The second is the same but given as an ISO string, e.g. &quot;2016-08-17&quot;. (drop-subkey) </p>
<dt><code>fpr</code></p>
<dd> The hexified fingerprint of the current subkey or primary key. (drop-subkey) </p>
<dt><code>primary</code></p>
<dd> Boolean indicating whether the user id is the primary one. (keep-uid) </p>
<dt><code>expired</code></p>
<dd> Boolean indicating whether a user id (keep-uid), a key (drop-subkey), or a signature (drop-sig) expired. </p>
<dt><code>revoked</code></p>
<dd> Boolean indicating whether a user id (keep-uid) or a key (drop-subkey) has been revoked. </p>
<dt><code>disabled</code></p>
<dd> Boolean indicating whether a primary key is disabled. (not used) </p>
<dt><code>secret</code></p>
<dd> Boolean indicating whether a key or subkey is a secret one. (drop-subkey) </p>
<dt><code>usage</code></p>
<dd> A string indicating the usage flags for the subkey, from the sequence &#8220;ecsa?&#8221;. For example, a subkey capable of just signing and authentication would be an exact match for &#8220;sa&#8221;. (drop-subkey) </p>
<dt><code>sig_created</code></p>
<dd> <code>sig_created_d</code> The first is the timestamp a signature packet was created. The second is the same but given as an ISO date string, e.g. &quot;2016-08-17&quot;. (drop-sig) </p>
<dt><code>sig_algo</code></p>
<dd> A number with the public key algorithm of a signature packet. (drop-sig) </p>
<dt><code>sig_digest_algo</code></p>
<dd> A number with the digest algorithm of a signature packet. (drop-sig) </p>
</dl>
</dl>
<dt><code>&#8211;export-options </code><i>parameters</i></p>
<dd> This is a space or comma delimited string that gives options for exporting keys. Options can be prepended with a `no-&#8216; to give the opposite meaning. The options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>export-local-sigs</code></p>
<dd> Allow exporting key signatures marked as &quot;local&quot;. This is not generally useful unless a shared keyring scheme is being used. Defaults to no. </p>
<dt><code>export-attributes</code></p>
<dd> Include attribute user IDs (photo IDs) while exporting. Not including attribute user IDs is useful to export keys that are going to be used by an OpenPGP program that does not accept attribute user IDs. Defaults to yes. </p>
<dt><code>export-sensitive-revkeys</code></p>
<dd> Include designated revoker information that was marked as &quot;sensitive&quot;. Defaults to no. </p>
<dt><code>backup</code></p>
<dd> <code>export-backup</code> Export for use as a backup. The exported data includes all data which is needed to restore the key or keys later with GnuPG. The format is basically the OpenPGP format but enhanced with GnuPG specific data. All other contradicting options are overridden. </p>
<dt><code>export-clean</code></p>
<dd> Compact (remove all signatures from) user IDs on the key being exported if the user IDs are not usable. Also, do not export any signatures that are not usable. This includes signatures that were issued by keys that are not present on the keyring. This option is the same as running the <code>&#8211;edit-key</code> command &quot;clean&quot; before export except that the local copy of the key is not modified. Defaults to no. </p>
<dt><code>export-minimal</code></p>
<dd> Export the smallest key possible. This removes all signatures except the most recent self-signature on each user ID. This option is the same as running the <code>&#8211;edit-key</code> command &quot;minimize&quot; before export except that the local copy of the key is not modified. Defaults to no. </p>
<dt><code>export-pka</code></p>
<dd> Instead of outputting the key material output PKA records suitable to put into DNS zone files. An ORIGIN line is printed before each record to allow diverting the records to the corresponding zone file. </p>
<dt><code>export-dane</code></p>
<dd> Instead of outputting the key material output OpenPGP DANE records suitable to put into DNS zone files. An ORIGIN line is printed before each record to allow diverting the records to the corresponding zone file. </p>
</dl>
</dl>
<dt><code>&#8211;with-colons</code></p>
<dd> Print key listings delimited by colons. Note that the output will be encoded in UTF-8 regardless of any <code>&#8211;display-charset</code> setting. This format is useful when GnuPG is called from scripts and other programs as it is easily machine parsed. The details of this format are documented in the file &#8216;<i>doc/DETAILS</i>&#8216;, which is included in the GnuPG source distribution. </p>
<dt><code>&#8211;fixed-list-mode</code></p>
<dd> Do not merge primary user ID and primary key in <code>&#8211;with-colon</code> listing mode and print all timestamps as seconds since 1970-01-01. Since GnuPG 2.0.10, this mode is always used and thus this option is obsolete; it does not harm to use it though. </p>
<dt><code>&#8211;legacy-list-mode</code></p>
<dd> Revert to the pre-2.1 public key list mode. This only affects the human readable output and not the machine interface (i.e. <code>&#8211;with-colons</code>). Note that the legacy format does not convey suitable information for elliptic curves. </p>
<dt><code>&#8211;with-fingerprint</code></p>
<dd> Same as the command <code>&#8211;fingerprint</code> but changes only the format of the output and may be used together with another command. </p>
<dt><code>&#8211;with-subkey-fingerprint</code></p>
<dd> If a fingerprint is printed for the primary key, this option forces printing of the fingerprint for all subkeys. This could also be achieved by using the <code>&#8211;with-fingerprint</code> twice but by using this option along with keyid-format &quot;none&quot; a compact fingerprint is printed. </p>
<dt><code>&#8211;with-icao-spelling</code></p>
<dd> Print the ICAO spelling of the fingerprint in addition to the hex digits. </p>
<dt><code>&#8211;with-keygrip</code></p>
<dd> Include the keygrip in the key listings. In <code>&#8211;with-colons</code> mode this is implicitly enable for secret keys. </p>
<dt><code>&#8211;with-key-origin</code></p>
<dd> Include the locally held information on the origin and last update of a key in a key listing. In <code>&#8211;with-colons</code> mode this is always printed. This data is currently experimental and shall not be considered part of the stable API. </p>
<dt><code>&#8211;with-wkd-hash</code></p>
<dd> Print a Web Key Directory identifier along with each user ID in key listings. This is an experimental feature and semantics may change. </p>
<dt><code>&#8211;with-secret</code></p>
<dd> Include info about the presence of a secret key in public key listings done with <code>&#8211;with-colons</code>. </p>
</dl>
<h3>OpenPGP protocol specific options</h3>
<p> &nbsp; </p>
<dl>
<dt><code>-t, &#8211;textmode</code></p>
<dd> <code>&#8211;no-textmode</code> Treat input files as text and store them in the OpenPGP canonical text form with standard &quot;CRLF&quot; line endings. This also sets the necessary flags to inform the recipient that the encrypted or signed data is text and may need its line endings converted back to whatever the local system uses. This option is useful when communicating between two platforms that have different line ending conventions (UNIX-like to Mac, Mac to Windows, etc). <code>&#8211;no-textmode</code> disables this option, and is the default. </p>
<dt><code>&#8211;force-v3-sigs</code></p>
<dd> <code>&#8211;no-force-v3-sigs</code></p>
<dt><code>&#8211;force-v4-certs</code></p>
<dd> <code>&#8211;no-force-v4-certs</code> These options are obsolete and have no effect since GnuPG 2.1. </p>
<dt><code>&#8211;force-mdc</code></p>
<dd> <code>&#8211;disable-mdc</code> These options are obsolete and have no effect since GnuPG 2.2.8. The MDC is always used. But note: If the creation of a legacy non-MDC message is exceptionally required, the option <code>&#8211;rfc2440</code> allows for this. </p>
<dt><code>&#8211;disable-signer-uid</code></p>
<dd> By default the user ID of the signing key is embedded in the data signature. As of now this is only done if the signing key has been specified with <code>local-user</code> using a mail address, or with <code>sender</code>. This information can be helpful for verifier to locate the key; see option <code>&#8211;auto-key-retrieve</code>. </p>
<dt><code>&#8211;include-key-block</code></p>
<dd> This option is used to embed the actual signing key into a data signature. The embedded key is stripped down to a single user id and includes only the signing subkey used to create the signature as well as as valid encryption subkeys. All other info is removed from the key to keep it and thus the signature small. This option is the OpenPGP counterpart to the <code>gpgsm</code> option <code>&#8211;include-certs</code>. </p>
<dt><code>&#8211;personal-cipher-preferences </code><i>string</i></p>
<dd> Set the list of personal cipher preferences to <i>string</i>. Use <code>gpg &#8211;version</code> to get a list of available algorithms, and use <code>none</code> to set no preference at all. This allows the user to safely override the algorithm chosen by the recipient key preferences, as GPG will only select an algorithm that is usable by all recipients. The most highly ranked cipher in this list is also used for the <code>&#8211;symmetric</code> encryption command. </p>
<dt><code>&#8211;personal-digest-preferences </code><i>string</i></p>
<dd> Set the list of personal digest preferences to <i>string</i>. Use <code>gpg &#8211;version</code> to get a list of available algorithms, and use <code>none</code> to set no preference at all. This allows the user to safely override the algorithm chosen by the recipient key preferences, as GPG will only select an algorithm that is usable by all recipients. The most highly ranked digest algorithm in this list is also used when signing without encryption (e.g. <code>&#8211;clear-sign</code> or <code>&#8211;sign</code>). </p>
<dt><code>&#8211;personal-compress-preferences </code><i>string</i></p>
<dd> Set the list of personal compression preferences to <i>string</i>. Use <code>gpg &#8211;version</code> to get a list of available algorithms, and use <code>none</code> to set no preference at all. This allows the user to safely override the algorithm chosen by the recipient key preferences, as GPG will only select an algorithm that is usable by all recipients. The most highly ranked compression algorithm in this list is also used when there are no recipient keys to consider (e.g. <code>&#8211;symmetric</code>). </p>
<dt><code>&#8211;s2k-cipher-algo </code><i>name</i></p>
<dd> Use <i>name</i> as the cipher algorithm for symmetric encryption with a passphrase if <code>&#8211;personal-cipher-preferences</code> and <code>&#8211;cipher-algo</code> are not given. The default is AES-128. </p>
<dt><code>&#8211;s2k-digest-algo </code><i>name</i></p>
<dd> Use <i>name</i> as the digest algorithm used to mangle the passphrases for symmetric encryption. The default is SHA-1. </p>
<dt><code>&#8211;s2k-mode </code><i>n</i></p>
<dd> Selects how passphrases for symmetric encryption are mangled. If <i>n</i> is 0 a plain passphrase (which is in general not recommended) will be used, a 1 adds a salt (which should not be used) to the passphrase and a 3 (the default) iterates the whole process a number of times (see <code>&#8211;s2k-count</code>). </p>
<dt><code>&#8211;s2k-count </code><i>n</i></p>
<dd> Specify how many times the passphrases mangling for symmetric encryption is repeated. This value may range between 1024 and 65011712 inclusive. The default is inquired from gpg-agent. Note that not all values in the 1024-65011712 range are legal and if an illegal value is selected, GnuPG will round up to the nearest legal value. This option is only meaningful if <code>&#8211;s2k-mode</code> is set to the default of 3. </p>
</dl>
<h3>Compliance options</h3>
<p> &nbsp; </p>
<p> These options control what GnuPG is compliant to. Only one of these options may be active at a time. Note that the default setting of this is nearly always the correct one. See the INTEROPERABILITY WITH OTHER OPENPGP PROGRAMS section below before using one of these options. </p>
<dl>
<dt><code>&#8211;gnupg</code></p>
<dd> Use standard GnuPG behavior. This is essentially OpenPGP behavior (see <code>&#8211;openpgp</code>), but with some additional workarounds for common compatibility problems in different versions of PGP. This is the default option, so it is not generally needed, but it may be useful to override a different compliance option in the gpg.conf file. </p>
<dt><code>&#8211;openpgp</code></p>
<dd> Reset all packet, cipher and digest options to strict OpenPGP behavior. Use this option to reset all previous options like <code>&#8211;s2k-*</code>, <code>&#8211;cipher-algo</code>, <code>&#8211;digest-algo</code> and <code>&#8211;compress-algo</code> to OpenPGP compliant values. All PGP workarounds are disabled. </p>
<dt><code>&#8211;rfc4880</code></p>
<dd> Reset all packet, cipher and digest options to strict RFC-4880 behavior. Note that this is currently the same thing as <code>&#8211;openpgp</code>. </p>
<dt><code>&#8211;rfc4880bis</code></p>
<dd> Enable experimental features from proposed updates to RFC-4880. This option can be used in addition to the other compliance options. Warning: The behavior may change with any GnuPG release and created keys or data may not be usable with future GnuPG versions. </p>
<dt><code>&#8211;rfc2440</code></p>
<dd> Reset all packet, cipher and digest options to strict RFC-2440 behavior. Note that by using this option encryption packets are created in a legacy mode without MDC protection. This is dangerous and should thus only be used for experiments. See also option <code>&#8211;ignore-mdc-error</code>. </p>
<dt><code>&#8211;pgp6</code></p>
<dd> Set up all options to be as PGP 6 compliant as possible. This restricts you to the ciphers IDEA (if the IDEA plugin is installed), 3DES, and CAST5, the hashes MD5, SHA1 and RIPEMD160, and the compression algorithms none and ZIP. This also disables <code>&#8211;throw-keyids</code>, and making signatures with signing subkeys as PGP 6 does not understand signatures made by signing subkeys. </p>
<p> This option implies <code>&#8211;escape-from-lines</code>. </p>
<dt><code>&#8211;pgp7</code></p>
<dd> Set up all options to be as PGP 7 compliant as possible. This is identical to <code>&#8211;pgp6</code> except that MDCs are not disabled, and the list of allowable ciphers is expanded to add AES128, AES192, AES256, and TWOFISH. </p>
<dt><code>&#8211;pgp8</code></p>
<dd> Set up all options to be as PGP 8 compliant as possible. PGP 8 is a lot closer to the OpenPGP standard than previous versions of PGP, so all this does is disable <code>&#8211;throw-keyids</code> and set <code>&#8211;escape-from-lines</code>. All algorithms are allowed except for the SHA224, SHA384, and SHA512 digests. </p>
<dt><code>&#8211;compliance </code><i>string</i></p>
<dd> This option can be used instead of one of the options above. Valid values for <i>string</i> are the above option names (without the double dash) and possibly others as shown when using &quot;help&quot; for <i>value</i>. </p>
</dl>
<h3>Doing things one usually doesn&#8217;t want to do</h3>
<p> &nbsp; </p>
<dl>
<dt><code>-n</code></p>
<dd> <code>&#8211;dry-run</code> Don&#8217;t make any changes (this is not completely implemented). </p>
<dt><code>&#8211;list-only</code></p>
<dd> Changes the behaviour of some commands. This is like <code>&#8211;dry-run</code> but different in some cases. The semantic of this option may be extended in the future. Currently it only skips the actual decryption pass and therefore enables a fast listing of the encryption keys. </p>
<dt><code>-i</code></p>
<dd> <code>&#8211;interactive</code> Prompt before overwriting any files. </p>
<dt><code>&#8211;debug-level </code><i>level</i></p>
<dd> Select the debug level for investigating problems. <i>level</i> may be a numeric value or by a keyword: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> No debugging at all. A value of less than 1 may be used instead of the keyword.</p>
<dt><code>basic</code></p>
<dd> Some basic debug messages. A value between 1 and 2 may be used instead of the keyword.</p>
<dt><code>advanced</code></p>
<dd> More verbose debug messages. A value between 3 and 5 may be used instead of the keyword.</p>
<dt><code>expert</code></p>
<dd> Even more detailed messages. A value between 6 and 8 may be used instead of the keyword.</p>
<dt><code>guru</code></p>
<dd> All of the debug messages you can get. A value greater than 8 may be used instead of the keyword. The creation of hash tracing files is only enabled if the keyword is used.</dl>
</dl>
<p> How these messages are mapped to the actual debugging flags is not specified and may change with newer releases of this program. They are however carefully selected to best aid in debugging. </p>
<dt><code>&#8211;debug </code><i>flags</i></p>
<dd> Set debugging flags. All flags are or-ed and <i>flags</i> may be given in C syntax (e.g. 0x0042) or as a comma separated list of flag names. To get a list of all supported flags the single word &quot;help&quot; can be used. </p>
<dt><code>&#8211;debug-all</code></p>
<dd> Set all useful debugging flags. </p>
<dt><code>&#8211;debug-iolbf</code></p>
<dd> Set stdout into line buffered mode. This option is only honored when given on the command line. </p>
<dt><code>&#8211;faked-system-time </code><i>epoch</i></p>
<dd> This option is only useful for testing; it sets the system time back or forth to <i>epoch</i> which is the number of seconds elapsed since the year 1970. Alternatively <i>epoch</i> may be given as a full ISO time string (e.g. &quot;20070924T154812&quot;). </p>
<p> If you suffix <i>epoch</i> with an exclamation mark (!), the system time will appear to be frozen at the specified time. </p>
<dt><code>&#8211;enable-progress-filter</code></p>
<dd> Enable certain PROGRESS status outputs. This option allows frontends to display a progress indicator while gpg is processing larger files. There is a slight performance overhead using it. </p>
<dt><code>&#8211;status-fd </code><i>n</i></p>
<dd> Write special status strings to the file descriptor <i>n</i>. See the file DETAILS in the documentation for a listing of them. </p>
<dt><code>&#8211;status-file </code><i>file</i></p>
<dd> Same as <code>&#8211;status-fd</code>, except the status data is written to file <i>file</i>. </p>
<dt><code>&#8211;logger-fd </code><i>n</i></p>
<dd> Write log output to file descriptor <i>n</i> and not to STDERR. </p>
<dt><code>&#8211;log-file </code><i>file</i></p>
<dd> <code>&#8211;logger-file </code><i>file</i> Same as <code>&#8211;logger-fd</code>, except the logger data is written to file <i>file</i>. Use &#8216;<i>socket://</i>&#8216; to log to a socket. Note that in this version of gpg the option has only an effect if <code>&#8211;batch</code> is also used. </p>
<dt><code>&#8211;attribute-fd </code><i>n</i></p>
<dd> Write attribute subpackets to the file descriptor <i>n</i>. This is most useful for use with <code>&#8211;status-fd</code>, since the status messages are needed to separate out the various subpackets from the stream delivered to the file descriptor. </p>
<dt><code>&#8211;attribute-file </code><i>file</i></p>
<dd> Same as <code>&#8211;attribute-fd</code>, except the attribute data is written to file <i>file</i>. </p>
<dt><code>&#8211;comment </code><i>string</i></p>
<dd> <code>&#8211;no-comments</code> Use <i>string</i> as a comment string in cleartext signatures and ASCII armored messages or keys (see <code>&#8211;armor</code>). The default behavior is not to use a comment string. <code>&#8211;comment</code> may be repeated multiple times to get multiple comment strings. <code>&#8211;no-comments</code> removes all comments. It is a good idea to keep the length of a single comment below 60 characters to avoid problems with mail programs wrapping such lines. Note that comment lines, like all other header lines, are not protected by the signature. </p>
<dt><code>&#8211;emit-version</code></p>
<dd> <code>&#8211;no-emit-version</code> Force inclusion of the version string in ASCII armored output. If given once only the name of the program and the major number is emitted, given twice the minor is also emitted, given thrice the micro is added, and given four times an operating system identification is also emitted. <code>&#8211;no-emit-version</code> (default) disables the version line. </p>
<dt><code>&#8211;sig-notation {</code><i>name</i>=<i>value</i>}</p>
<dd> <code>&#8211;cert-notation {</code><i>name</i>=<i>value</i>} <code>-N, &#8211;set-notation {</code><i>name</i>=<i>value</i>} Put the name value pair into the signature as notation data. <i>name</i> must consist only of printable characters or spaces, and must contain a &#8216;@&#8217; character in the form keyname [at] domain.example.com (substituting the appropriate keyname and domain name, of course). This is to help prevent pollution of the IETF reserved notation namespace. The <code>&#8211;expert</code> flag overrides the &#8216;@&#8217; check. <i>value</i> may be any printable string; it will be encoded in UTF-8, so you should check that your <code>&#8211;display-charset</code> is set correctly. If you prefix <i>name</i> with an exclamation mark (!), the notation data will be flagged as critical (rfc4880:5.2.3.16). <code>&#8211;sig-notation</code> sets a notation for data signatures. <code>&#8211;cert-notation</code> sets a notation for key signatures (certifications). <code>&#8211;set-notation</code> sets both. </p>
<p> There are special codes that may be used in notation names. &quot;%k&quot; will be expanded into the key ID of the key being signed, &quot;%K&quot; into the long key ID of the key being signed, &quot;%f&quot; into the fingerprint of the key being signed, &quot;%s&quot; into the key ID of the key making the signature, &quot;%S&quot; into the long key ID of the key making the signature, &quot;%g&quot; into the fingerprint of the key making the signature (which might be a subkey), &quot;%p&quot; into the fingerprint of the primary key of the key making the signature, &quot;%c&quot; into the signature count from the OpenPGP smartcard, and &quot;%%&quot; results in a single &quot;%&quot;. %k, %K, and %f are only meaningful when making a key signature (certification), and %c is only meaningful when using the OpenPGP smartcard. </p>
<dt><code>&#8211;known-notation </code><i>name</i></p>
<dd> Adds <i>name</i> to a list of known critical signature notations. The effect of this is that gpg will not mark a signature with a critical signature notation of that name as bad. Note that gpg already knows by default about a few critical signatures notation names. </p>
<dt><code>&#8211;sig-policy-url </code><i>string</i></p>
<dd> <code>&#8211;cert-policy-url </code><i>string</i> <code>&#8211;set-policy-url </code><i>string</i> Use <i>string</i> as a Policy URL for signatures (rfc4880:5.2.3.20). If you prefix it with an exclamation mark (!), the policy URL packet will be flagged as critical. <code>&#8211;sig-policy-url</code> sets a policy url for data signatures. <code>&#8211;cert-policy-url</code> sets a policy url for key signatures (certifications). <code>&#8211;set-policy-url</code> sets both. </p>
<p> The same %-expandos used for notation data are available here as well. </p>
<dt><code>&#8211;sig-keyserver-url </code><i>string</i></p>
<dd> Use <i>string</i> as a preferred keyserver URL for data signatures. If you prefix it with an exclamation mark (!), the keyserver URL packet will be flagged as critical. </p>
<p> The same %-expandos used for notation data are available here as well. </p>
<dt><code>&#8211;set-filename </code><i>string</i></p>
<dd> Use <i>string</i> as the filename which is stored inside messages. This overrides the default, which is to use the actual filename of the file being encrypted. Using the empty string for <i>string</i> effectively removes the filename from the output. </p>
<dt><code>&#8211;for-your-eyes-only</code></p>
<dd> <code>&#8211;no-for-your-eyes-only</code> Set the `for your eyes only&#8217; flag in the message. This causes GnuPG to refuse to save the file unless the <code>&#8211;output</code> option is given, and PGP to use a &quot;secure viewer&quot; with a claimed Tempest-resistant font to display the message. This option overrides <code>&#8211;set-filename</code>. <code>&#8211;no-for-your-eyes-only</code> disables this option. </p>
<dt><code>&#8211;use-embedded-filename</code></p>
<dd> <code>&#8211;no-use-embedded-filename</code> Try to create a file with a name as embedded in the data. This can be a dangerous option as it enables overwriting files. Defaults to no. Note that the option <code>&#8211;output</code> overrides this option. </p>
<dt><code>&#8211;cipher-algo </code><i>name</i></p>
<dd> Use <i>name</i> as cipher algorithm. Running the program with the command <code>&#8211;version</code> yields a list of supported algorithms. If this is not used the cipher algorithm is selected from the preferences stored with the key. In general, you do not want to use this option as it allows you to violate the OpenPGP standard. <code>&#8211;personal-cipher-preferences</code> is the safe way to accomplish the same thing. </p>
<dt><code>&#8211;digest-algo </code><i>name</i></p>
<dd> Use <i>name</i> as the message digest algorithm. Running the program with the command <code>&#8211;version</code> yields a list of supported algorithms. In general, you do not want to use this option as it allows you to violate the OpenPGP standard. <code>&#8211;personal-digest-preferences</code> is the safe way to accomplish the same thing. </p>
<dt><code>&#8211;compress-algo </code><i>name</i></p>
<dd> Use compression algorithm <i>name</i>. &quot;zlib&quot; is RFC-1950 ZLIB compression. &quot;zip&quot; is RFC-1951 ZIP compression which is used by PGP. &quot;bzip2&quot; is a more modern compression scheme that can compress some things better than zip or zlib, but at the cost of more memory used during compression and decompression. &quot;uncompressed&quot; or &quot;none&quot; disables compression. If this option is not used, the default behavior is to examine the recipient key preferences to see which algorithms the recipient supports. If all else fails, ZIP is used for maximum compatibility. </p>
<p> ZLIB may give better compression results than ZIP, as the compression window size is not limited to 8k. BZIP2 may give even better compression results than that, but will use a significantly larger amount of memory while compressing and decompressing. This may be significant in low memory situations. Note, however, that PGP (all versions) only supports ZIP compression. Using any algorithm other than ZIP or &quot;none&quot; will make the message unreadable with PGP. In general, you do not want to use this option as it allows you to violate the OpenPGP standard. <code>&#8211;personal-compress-preferences</code> is the safe way to accomplish the same thing. </p>
<dt><code>&#8211;cert-digest-algo </code><i>name</i></p>
<dd> Use <i>name</i> as the message digest algorithm used when signing a key. Running the program with the command <code>&#8211;version</code> yields a list of supported algorithms. Be aware that if you choose an algorithm that GnuPG supports but other OpenPGP implementations do not, then some users will not be able to use the key signatures you make, or quite possibly your entire key. </p>
<dt><code>&#8211;disable-cipher-algo </code><i>name</i></p>
<dd> Never allow the use of <i>name</i> as cipher algorithm. The given name will not be checked so that a later loaded algorithm will still get disabled. </p>
<dt><code>&#8211;disable-pubkey-algo </code><i>name</i></p>
<dd> Never allow the use of <i>name</i> as public key algorithm. The given name will not be checked so that a later loaded algorithm will still get disabled. </p>
<dt><code>&#8211;throw-keyids</code></p>
<dd> <code>&#8211;no-throw-keyids</code> Do not put the recipient key IDs into encrypted messages. This helps to hide the receivers of the message and is a limited countermeasure against traffic analysis. ([Using a little social engineering anyone who is able to decrypt the message can check whether one of the other recipients is the one he suspects.]) On the receiving side, it may slow down the decryption process because all available secret keys must be tried. <code>&#8211;no-throw-keyids</code> disables this option. This option is essentially the same as using <code>&#8211;hidden-recipient</code> for all recipients. </p>
<dt><code>&#8211;not-dash-escaped</code></p>
<dd> This option changes the behavior of cleartext signatures so that they can be used for patch files. You should not send such an armored file via email because all spaces and line endings are hashed too. You can not use this option for data which has 5 dashes at the beginning of a line, patch files don&#8217;t have this. A special armor header line tells GnuPG about this cleartext signature option. </p>
<dt><code>&#8211;escape-from-lines</code></p>
<dd> <code>&#8211;no-escape-from-lines</code> Because some mailers change lines starting with &quot;From &quot; to &quot;&gt;From &quot; it is good to handle such lines in a special way when creating cleartext signatures to prevent the mail system from breaking the signature. Note that all other PGP versions do it this way too. Enabled by default. <code>&#8211;no-escape-from-lines</code> disables this option. </p>
<dt><code>&#8211;passphrase-repeat </code><i>n</i></p>
<dd> Specify how many times <code>gpg</code> will request a new passphrase be repeated. This is useful for helping memorize a passphrase. Defaults to 1 repetition; can be set to 0 to disable any passphrase repetition. Note that a <i>n</i> greater than 1 will pop up the pinentry window <i>n</i>+1 times even if a modern pinentry with two entry fields is used. </p>
<dt><code>&#8211;passphrase-fd </code><i>n</i></p>
<dd> Read the passphrase from file descriptor <i>n</i>. Only the first line will be read from file descriptor <i>n</i>. If you use 0 for <i>n</i>, the passphrase will be read from STDIN. This can only be used if only one passphrase is supplied. </p>
<p> Note that since Version 2.0 this passphrase is only used if the option <code>&#8211;batch</code> has also been given. Since Version 2.1 the <code>&#8211;pinentry-mode</code> also needs to be set to <code>loopback</code>. </p>
<dt><code>&#8211;passphrase-file </code><i>file</i></p>
<dd> Read the passphrase from file <i>file</i>. Only the first line will be read from file <i>file</i>. This can only be used if only one passphrase is supplied. Obviously, a passphrase stored in a file is of questionable security if other users can read this file. Don&#8217;t use this option if you can avoid it. </p>
<p> Note that since Version 2.0 this passphrase is only used if the option <code>&#8211;batch</code> has also been given. Since Version 2.1 the <code>&#8211;pinentry-mode</code> also needs to be set to <code>loopback</code>. </p>
<dt><code>&#8211;passphrase </code><i>string</i></p>
<dd> Use <i>string</i> as the passphrase. This can only be used if only one passphrase is supplied. Obviously, this is of very questionable security on a multi-user system. Don&#8217;t use this option if you can avoid it. </p>
<p> Note that since Version 2.0 this passphrase is only used if the option <code>&#8211;batch</code> has also been given. Since Version 2.1 the <code>&#8211;pinentry-mode</code> also needs to be set to <code>loopback</code>. </p>
<dt><code>&#8211;pinentry-mode </code><i>mode</i></p>
<dd> Set the pinentry mode to <i>mode</i>. Allowed values for <i>mode</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd> Use the default of the agent, which is <code>ask</code>.</p>
<dt><code>ask</code></p>
<dd> Force the use of the Pinentry.</p>
<dt><code>cancel</code></p>
<dd> Emulate use of Pinentry&#8217;s cancel button.</p>
<dt><code>error</code></p>
<dd> Return a Pinentry error (&#8220;No Pinentry&#8221;).</p>
<dt><code>loopback</code></p>
<dd> Redirect Pinentry queries to the caller. Note that in contrast to Pinentry the user is not prompted again if he enters a bad password.</dl>
</dl>
<dt><code>&#8211;no-symkey-cache</code></p>
<dd> Disable the passphrase cache used for symmetrical en- and decryption. This cache is based on the message specific salt value (cf. <code>&#8211;s2k-mode</code>). </p>
<dt><code>&#8211;request-origin </code><i>origin</i></p>
<dd> Tell gpg to assume that the operation ultimately originated at <i>origin</i>. Depending on the origin certain restrictions are applied and the Pinentry may include an extra note on the origin. Supported values for <i>origin</i> are: <code>local</code> which is the default, <code>remote</code> to indicate a remote origin or <code>browser</code> for an operation requested by a web browser. </p>
<dt><code>&#8211;command-fd </code><i>n</i></p>
<dd> This is a replacement for the deprecated shared-memory IPC mode. If this option is enabled, user input on questions is not expected from the TTY but from the given file descriptor. It should be used together with <code>&#8211;status-fd</code>. See the file doc/DETAILS in the source distribution for details on how to use it. </p>
<dt><code>&#8211;command-file </code><i>file</i></p>
<dd> Same as <code>&#8211;command-fd</code>, except the commands are read out of file <i>file</i> </p>
<dt><code>&#8211;allow-non-selfsigned-uid</code></p>
<dd> <code>&#8211;no-allow-non-selfsigned-uid</code> Allow the import and use of keys with user IDs which are not self-signed. This is not recommended, as a non self-signed user ID is trivial to forge. <code>&#8211;no-allow-non-selfsigned-uid</code> disables. </p>
<dt><code>&#8211;allow-freeform-uid</code></p>
<dd> Disable all checks on the form of the user ID while generating a new one. This option should only be used in very special environments as it does not ensure the de-facto standard format of user IDs. </p>
<dt><code>&#8211;ignore-time-conflict</code></p>
<dd> GnuPG normally checks that the timestamps associated with keys and signatures have plausible values. However, sometimes a signature seems to be older than the key due to clock problems. This option makes these checks just a warning. See also <code>&#8211;ignore-valid-from</code> for timestamp issues on subkeys. </p>
<dt><code>&#8211;ignore-valid-from</code></p>
<dd> GnuPG normally does not select and use subkeys created in the future. This option allows the use of such keys and thus exhibits the pre-1.0.7 behaviour. You should not use this option unless there is some clock problem. See also <code>&#8211;ignore-time-conflict</code> for timestamp issues with signatures. </p>
<dt><code>&#8211;ignore-crc-error</code></p>
<dd> The ASCII armor used by OpenPGP is protected by a CRC checksum against transmission errors. Occasionally the CRC gets mangled somewhere on the transmission channel but the actual content (which is protected by the OpenPGP protocol anyway) is still okay. This option allows GnuPG to ignore CRC errors. </p>
<dt><code>&#8211;ignore-mdc-error</code></p>
<dd> This option changes a MDC integrity protection failure into a warning. It is required to decrypt old messages which did not use an MDC. It may also be useful if a message is partially garbled, but it is necessary to get as much data as possible out of that garbled message. Be aware that a missing or failed MDC can be an indication of an attack. Use with great caution; see also option <code>&#8211;rfc2440</code>. </p>
<dt><code>&#8211;allow-weak-digest-algos</code></p>
<dd> Signatures made with known-weak digest algorithms are normally rejected with an &#8220;invalid digest algorithm&#8221; message. This option allows the verification of signatures made with such weak algorithms. MD5 is the only digest algorithm considered weak by default. See also <code>&#8211;weak-digest</code> to reject other digest algorithms. </p>
<dt><code>&#8211;weak-digest </code><i>name</i></p>
<dd> Treat the specified digest algorithm as weak. Signatures made over weak digests algorithms are normally rejected. This option can be supplied multiple times if multiple algorithms should be considered weak. See also <code>&#8211;allow-weak-digest-algos</code> to disable rejection of weak digests. MD5 is always considered weak, and does not need to be listed explicitly. </p>
<dt><code>&#8211;allow-weak-key-signatures</code></p>
<dd> To avoid a minor risk of collision attacks on third-party key signatures made using SHA-1, those key signatures are considered invalid. This options allows to override this restriction. </p>
<dt><code>&#8211;no-default-keyring</code></p>
<dd> Do not add the default keyrings to the list of keyrings. Note that GnuPG will not operate without any keyrings, so if you use this option and do not provide alternate keyrings via <code>&#8211;keyring</code> or <code>&#8211;secret-keyring</code>, then GnuPG will still use the default public or secret keyrings. </p>
<dt><code>&#8211;no-keyring</code></p>
<dd> Do not use any keyring at all. This overrides the default and all options which specify keyrings. </p>
<dt><code>&#8211;skip-verify</code></p>
<dd> Skip the signature verification step. This may be used to make the decryption faster if the signature verification is not needed. </p>
<dt><code>&#8211;with-key-data</code></p>
<dd> Print key listings delimited by colons (like <code>&#8211;with-colons</code>) and print the public key data. </p>
<dt><code>&#8211;list-signatures</code></p>
<dd> <code>&#8211;list-sigs</code> Same as <code>&#8211;list-keys</code>, but the signatures are listed too. This command has the same effect as using <code>&#8211;list-keys</code> with <code>&#8211;with-sig-list</code>. Note that in contrast to <code>&#8211;check-signatures</code> the key signatures are not verified. This command can be used to create a list of signing keys missing in the local keyring; for example: </p>
<dl>
<dt>
<dd>
<pre><code>
gpg-- list - sigs-- with - colons USERID |
    awk - F : '$1=="sig" &amp;&amp; $2=="?" {if($13){print $13}else{print $5}}'
</code></pre>
</dl>
<dt><code>&#8211;fast-list-mode</code></p>
<dd> Changes the output of the list commands to work faster; this is achieved by leaving some parts empty. Some applications don&#8217;t need the user ID and the trust information given in the listings. By using this options they can get a faster listing. The exact behaviour of this option may change in future versions. If you are missing some information, don&#8217;t use this option. </p>
<dt><code>&#8211;no-literal</code></p>
<dd> This is not for normal use. Use the source to see for what it might be useful. </p>
<dt><code>&#8211;set-filesize</code></p>
<dd> This is not for normal use. Use the source to see for what it might be useful. </p>
<dt><code>&#8211;show-session-key</code></p>
<dd> Display the session key used for one message. See <code>&#8211;override-session-key</code> for the counterpart of this option. </p>
<p> We think that Key Escrow is a Bad Thing; however the user should have the freedom to decide whether to go to prison or to reveal the content of one specific message without compromising all messages ever encrypted for one secret key. </p>
<p> You can also use this option if you receive an encrypted message which is abusive or offensive, to prove to the administrators of the messaging system that the ciphertext transmitted corresponds to an inappropriate plaintext so they can take action against the offending user. </p>
<dt><code>&#8211;override-session-key </code><i>string</i></p>
<dd> <code>&#8211;override-session-key-fd </code><i>fd</i> Don&#8217;t use the public key but the session key <i>string</i> respective the session key taken from the first line read from file descriptor <i>fd</i>. The format of this string is the same as the one printed by <code>&#8211;show-session-key</code>. This option is normally not used but comes handy in case someone forces you to reveal the content of an encrypted message; using this option you can do this without handing out the secret key. Note that using <code>&#8211;override-session-key</code> may reveal the session key to all local users via the global process table. Often it is useful to combine this option with <code>&#8211;no-keyring</code>. </p>
<dt><code>&#8211;ask-sig-expire</code></p>
<dd> <code>&#8211;no-ask-sig-expire</code> When making a data signature, prompt for an expiration time. If this option is not specified, the expiration time set via <code>&#8211;default-sig-expire</code> is used. <code>&#8211;no-ask-sig-expire</code> disables this option. </p>
<dt><code>&#8211;default-sig-expire</code></p>
<dd> The default expiration time to use for signature expiration. Valid values are &quot;0&quot; for no expiration, a number followed by the letter d (for days), w (for weeks), m (for months), or y (for years) (for example &quot;2m&quot; for two months, or &quot;5y&quot; for five years), or an absolute date in the form YYYY-MM-DD. Defaults to &quot;0&quot;. </p>
<dt><code>&#8211;ask-cert-expire</code></p>
<dd> <code>&#8211;no-ask-cert-expire</code> When making a key signature, prompt for an expiration time. If this option is not specified, the expiration time set via <code>&#8211;default-cert-expire</code> is used. <code>&#8211;no-ask-cert-expire</code> disables this option. </p>
<dt><code>&#8211;default-cert-expire</code></p>
<dd> The default expiration time to use for key signature expiration. Valid values are &quot;0&quot; for no expiration, a number followed by the letter d (for days), w (for weeks), m (for months), or y (for years) (for example &quot;2m&quot; for two months, or &quot;5y&quot; for five years), or an absolute date in the form YYYY-MM-DD. Defaults to &quot;0&quot;. </p>
<dt><code>&#8211;default-new-key-algo </code><i>string</i></p>
<dd> This option can be used to change the default algorithms for key generation. The <i>string</i> is similar to the arguments required for the command <code>&#8211;quick-add-key</code> but slightly different. For example the current default of <code>&quot;rsa2048/cert,sign+rsa2048/encr&quot;</code> (or <code>&quot;rsa3072&quot;</code>) can be changed to the value of what we currently call future default, which is <code>&quot;ed25519/cert,sign+cv25519/encr&quot;</code>. You need to consult the source code to learn the details. Note that the advanced key generation commands can always be used to specify a key algorithm directly. </p>
<dt><code>&#8211;allow-secret-key-import</code></p>
<dd> This is an obsolete option and is not used anywhere. </p>
<dt><code>&#8211;allow-multiple-messages</code></p>
<dd>
<dt><code>&#8211;no-allow-multiple-messages</code></p>
<dd> Allow processing of multiple OpenPGP messages contained in a single file or stream. Some programs that call GPG are not prepared to deal with multiple messages being processed together, so this option defaults to no. Note that versions of GPG prior to 1.4.7 always allowed multiple messages. Future versions of GnUPG will remove this option. </p>
<p> Warning: Do not use this option unless you need it as a temporary workaround! </p>
<dt><code>&#8211;enable-special-filenames</code></p>
<dd> This option enables a mode in which filenames of the form &#8216;<i>-&amp;n</i>&#8216;, where n is a non-negative decimal number, refer to the file descriptor n and not to a file with that name. </p>
<dt><code>&#8211;no-expensive-trust-checks</code></p>
<dd> Experimental use only. </p>
<dt><code>&#8211;preserve-permissions</code></p>
<dd> Don&#8217;t change the permissions of a secret keyring back to user read/write only. Use this option only if you really know what you are doing. </p>
<dt><code>&#8211;default-preference-list </code><i>string</i></p>
<dd> Set the list of default preferences to <i>string</i>. This preference list is used for new keys and becomes the default for &quot;setpref&quot; in the edit menu. </p>
<dt><code>&#8211;default-keyserver-url </code><i>name</i></p>
<dd> Set the default keyserver URL to <i>name</i>. This keyserver will be used as the keyserver URL when writing a new self-signature on a key, which includes key generation and changing preferences. </p>
<dt><code>&#8211;list-config</code></p>
<dd> Display various internal configuration parameters of GnuPG. This option is intended for external programs that call GnuPG to perform tasks, and is thus not generally useful. See the file &#8216;<i>doc/DETAILS</i>&#8216; in the source distribution for the details of which configuration items may be listed. <code>&#8211;list-config</code> is only usable with <code>&#8211;with-colons</code> set. </p>
<dt><code>&#8211;list-gcrypt-config</code></p>
<dd> Display various internal configuration parameters of Libgcrypt. </p>
<dt><code>&#8211;gpgconf-list</code></p>
<dd> This command is similar to <code>&#8211;list-config</code> but in general only internally used by the <code>gpgconf</code> tool. </p>
<dt><code>&#8211;gpgconf-test</code></p>
<dd> This is more or less dummy action. However it parses the configuration file and returns with failure if the configuration file would prevent <code>gpg</code> from startup. Thus it may be used to run a syntax check on the configuration file. </p>
</dl>
<h3>Deprecated options</h3>
<p> &nbsp; </p>
<dl>
<dt><code>&#8211;show-photos</code></p>
<dd> <code>&#8211;no-show-photos</code> Causes <code>&#8211;list-keys</code>, <code>&#8211;list-signatures</code>, <code>&#8211;list-public-keys</code>, <code>&#8211;list-secret-keys</code>, and verifying a signature to also display the photo ID attached to the key, if any. See also <code>&#8211;photo-viewer</code>. These options are deprecated. Use <code>&#8211;list-options [no-]show-photos</code> and/or <code>&#8211;verify-options [no-]show-photos</code> instead. </p>
<dt><code>&#8211;show-keyring</code></p>
<dd> Display the keyring name at the head of key listings to show which keyring a given key resides on. This option is deprecated: use <code>&#8211;list-options [no-]show-keyring</code> instead. </p>
<dt><code>&#8211;always-trust</code></p>
<dd> Identical to <code>&#8211;trust-model always</code>. This option is deprecated. </p>
<dt><code>&#8211;show-notation</code></p>
<dd> <code>&#8211;no-show-notation</code> Show signature notations in the <code>&#8211;list-signatures</code> or <code>&#8211;check-signatures</code> listings as well as when verifying a signature with a notation in it. These options are deprecated. Use <code>&#8211;list-options [no-]show-notation</code> and/or <code>&#8211;verify-options [no-]show-notation</code> instead. </p>
<dt><code>&#8211;show-policy-url</code></p>
<dd> <code>&#8211;no-show-policy-url</code> Show policy URLs in the <code>&#8211;list-signatures</code> or <code>&#8211;check-signatures</code> listings as well as when verifying a signature with a policy URL in it. These options are deprecated. Use <code>&#8211;list-options [no-]show-policy-url</code> and/or <code>&#8211;verify-options [no-]show-policy-url</code> instead. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gpg -se -r Bob</code> <code>file</code></p>
<dd> sign and encrypt for user Bob </p>
<dt><code>gpg &#8211;clear-sign file</code></p>
<dd> make a cleartext signature </p>
<dt><code>gpg -sb file</code></p>
<dd> make a detached signature </p>
<dt><code>gpg -u 0x12345678 -sb file</code></p>
<dd> make a detached signature with the key 0x12345678 </p>
<dt><code>gpg &#8211;list-keys user_ID</code></p>
<dd> show keys </p>
<dt><code>gpg &#8211;fingerprint user_ID</code></p>
<dd> show fingerprint </p>
<dt><code>gpg &#8211;verify pgpfile</code></p>
<dd> <code>gpg &#8211;verify sigfile</code> [<code>datafile</code>] Verify the signature of the file but do not output the data unless requested. The second form is used for detached signatures, where <code>sigfile</code> is the detached signature (either ASCII armored or binary) and <code>datafile</code> are the signed data; if this is not given, the name of the file holding the signed data is constructed by cutting off the extension (&quot;.asc&quot; or &quot;.sig&quot;) of <code>sigfile</code> or by asking the user for the filename. If the option <code>&#8211;output</code> is also used the signed data is written to the file specified by that option; use <code>&#8211;</code> to write the signed data to stdout.</dl>
<h2>HOW TO SPECIFY A USER ID</h2>
<p> There are different ways to specify a user ID to GnuPG. Some of them are only valid for <code>gpg</code> others are only good for <code>gpgsm</code>. Here is the entire list of ways to specify a key: </p>
<dl>
<dt><code>By key Id.</code></p>
<dd> This format is deduced from the length of the string and its content or <code>0x</code> prefix. The key Id of an X.509 certificate are the low 64 bits of its SHA-1 fingerprint. The use of key Ids is just a shortcut, for all automated processing the fingerprint should be used. </p>
<p> When using <code>gpg</code> an exclamation mark (!) may be appended to force using the specified primary or secondary key and not to try and calculate which primary or secondary key to use. </p>
<p> The last four lines of the example give the key ID in their long form as internally used by the OpenPGP protocol. You can see the long key ID using the option <code>&#8211;with-colons</code>. </p>
<dl>
<dt>
<dd>
<pre>
234567C4
0F34E556E
01347A56A
0xAB123456
234AABBCC34567C4
0F323456784E56EAB
01AB3FED1347A5612
0x234AABBCC34567C4
</pre>
</dl>
<dt><code>By fingerprint.</code></p>
<dd> This format is deduced from the length of the string and its content or the <code>0x</code> prefix. Note, that only the 20 byte version fingerprint is available with <code>gpgsm</code> (i.e. the SHA-1 hash of the certificate). </p>
<p> When using <code>gpg</code> an exclamation mark (!) may be appended to force using the specified primary or secondary key and not to try and calculate which primary or secondary key to use. </p>
<p> The best way to specify a key Id is by using the fingerprint. This avoids any ambiguities in case that there are duplicated key IDs. </p>
<dl>
<dt>
<dd>
<pre>
1234343434343434C434343434343434
123434343434343C3434343434343734349A3434
0E12343434343434343434EAB3484343434343434
0xE12343434343434343434EAB3484343434343434
</pre>
</dl>
<p> <code>gpgsm</code> also accepts colons between each pair of hexadecimal digits because this is the de-facto standard on how to present X.509 fingerprints. <code>gpg</code> also allows the use of the space separated SHA-1 fingerprint as printed by the key listing commands. </p>
<dt><code>By exact match on OpenPGP user ID.</code></p>
<dd> This is denoted by a leading equal sign. It does not make sense for X.509 certificates. </p>
<dl>
<dt>
<dd>
<pre>
=Heinrich Heine &lt;heinrichh [at] uni-duesseldorf.de&gt;
</pre>
</dl>
<dt><code>By exact match on an email address.</code></p>
<dd> This is indicated by enclosing the email address in the usual way with left and right angles. </p>
<dl>
<dt>
<dd>
<pre>
&lt;heinrichh [at] uni-duesseldorf.de&gt;
</pre>
</dl>
<dt><code>By partial match on an email address.</code></p>
<dd> This is indicated by prefixing the search string with an <code>@</code>. This uses a substring search but considers only the mail address (i.e. inside the angle brackets). </p>
<dl>
<dt>
<dd>
<pre>
@heinrichh
</pre>
</dl>
<dt><code>By exact match on the subject&#8217;s DN.</code></p>
<dd> This is indicated by a leading slash, directly followed by the RFC-2253 encoded DN of the subject. Note that you can&#8217;t use the string printed by <code>gpgsm &#8211;list-keys</code> because that one has been reordered and modified for better readability; use <code>&#8211;with-colons</code> to print the raw (but standard escaped) RFC-2253 string. </p>
<dl>
<dt>
<dd>
<pre>
/CN=Heinrich Heine,O=Poets,L=Paris,C=FR
</pre>
</dl>
<dt><code>By exact match on the issuer&#8217;s DN.</code></p>
<dd> This is indicated by a leading hash mark, directly followed by a slash and then directly followed by the RFC-2253 encoded DN of the issuer. This should return the Root cert of the issuer. See note above. </p>
<dl>
<dt>
<dd>
<pre>
#/CN=Root Cert,O=Poets,L=Paris,C=FR
</pre>
</dl>
<dt><code>By exact match on serial number and issuer&#8217;s DN.</code></p>
<dd> This is indicated by a hash mark, followed by the hexadecimal representation of the serial number, then followed by a slash and the RFC-2253 encoded DN of the issuer. See note above. </p>
<dl>
<dt>
<dd>
<pre>
#4F03/CN=Root Cert,O=Poets,L=Paris,C=FR
</pre>
</dl>
<dt><code>By keygrip.</code></p>
<dd> This is indicated by an ampersand followed by the 40 hex digits of a keygrip. <code>gpgsm</code> prints the keygrip when using the command <code>&#8211;dump-cert</code>. </p>
<dl>
<dt>
<dd>
<pre>
&amp;D75F22C3F86E355877348498CDC92BD21010A480
</pre>
</dl>
<dt><code>By substring match.</code></p>
<dd> This is the default mode but applications may want to explicitly indicate this by putting the asterisk in front. Match is not case sensitive. </p>
<dl>
<dt>
<dd>
<pre>
Heine
*Heine
</pre>
</dl>
<dt><code>. and + prefixes</code></p>
<dd> These prefixes are reserved for looking up mails anchored at the end and for a word search mode. They are not yet implemented and using them is undefined. </p>
<p> Please note that we have reused the hash mark identifier which was used in old GnuPG versions to indicate the so called local-id. It is not anymore used and there should be no conflict when used with X.509 stuff. </p>
<p> Using the RFC-2253 format of DNs has the drawback that it is not possible to map them back to the original encoding, however we don&#8217;t have to do this because our key database stores this encoding as meta data. </p>
</dl>
<h2>FILTER EXPRESSIONS</h2>
<p> The options <code>&#8211;import-filter</code> and <code>&#8211;export-filter</code> use expressions with this syntax (square brackets indicate an optional part and curly braces a repetition, white space between the elements are allowed): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
[lc] { [{flag}] PROPNAME op VALUE[lc] }
</dl>
</dl>
<p> The name of a property (<i>PROPNAME</i>) may only consist of letters, digits and underscores. The description for the filter type describes which properties are defined. If an undefined property is used it evaluates to the empty string. Unless otherwise noted, the <i>VALUE</i> must always be given and may not be the empty string. No quoting is defined for the value, thus the value may not contain the strings <code>&amp;&amp;</code> or <code>||</code>, which are used as logical connection operators. The flag <code>&#8212;</code> can be used to remove this restriction. </p>
<p> Numerical values are computed as long int; standard C notation applies. <i>lc</i> is the logical connection operator; either <code>&amp;&amp;</code> for a conjunction or <code>||</code> for a disjunction. A conjunction is assumed at the begin of an expression. Conjunctions have higher precedence than disjunctions. If <i>VALUE</i> starts with one of the characters used in any <i>op</i> a space after the <i>op</i> is required. </p>
<p> The supported operators (<i>op</i>) are: </p>
<dl>
<dt><code>=~</code></p>
<dd> Substring must match. </p>
<dt><code>!~</code></p>
<dd> Substring must not match. </p>
<dt><code>=</code></p>
<dd> The full string must match. </p>
<dt><code>&lt;&gt;</code></p>
<dd> The full string must not match. </p>
<dt><code>==</code></p>
<dd> The numerical value must match. </p>
<dt><code>!=</code></p>
<dd> The numerical value must not match. </p>
<dt><code>&lt;=</code></p>
<dd> The numerical value of the field must be LE than the value. </p>
<dt><code>&lt;</code></p>
<dd> The numerical value of the field must be LT than the value. </p>
<dt><code>&gt;</code></p>
<dd> The numerical value of the field must be GT than the value. </p>
<dt><code>&gt;=</code></p>
<dd> The numerical value of the field must be GE than the value. </p>
<dt><code>-le</code></p>
<dd> The string value of the field must be less or equal than the value. </p>
<dt><code>-lt</code></p>
<dd> The string value of the field must be less than the value. </p>
<dt><code>-gt</code></p>
<dd> The string value of the field must be greater than the value. </p>
<dt><code>-ge</code></p>
<dd> The string value of the field must be greater or equal than the value. </p>
<dt><code>-n</code></p>
<dd> True if value is not empty (no value allowed). </p>
<dt><code>-z</code></p>
<dd> True if value is empty (no value allowed). </p>
<dt><code>-t</code></p>
<dd> Alias for &quot;PROPNAME != 0&quot; (no value allowed). </p>
<dt><code>-f</code></p>
<dd> Alias for &quot;PROPNAME == 0&quot; (no value allowed). </p>
</dl>
<p> Values for <i>flag</i> must be space separated. The supported flags are: </p>
<dl>
<dt><code>&#8212;</code></p>
<dd> <i>VALUE</i> spans to the end of the expression.</p>
<dt><code>-c</code></p>
<dd> The string match in this part is done case-sensitive.</dl>
<p> The filter options concatenate several specifications for a filter of the same type. For example the four options in this example: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&#8211;import &#8211; filter keep &#8211; uid = &#8220;uid =~ Alfa&#8221; &#8211;import &#8211; filter keep &#8211; uid = &#8220;&amp;&amp; uid !~ Test&#8221; &#8211;import &#8211; filter keep &#8211; uid = &#8220;|| uid =~ Alpha&#8221; &#8211;import &#8211; filter keep &#8211; uid = &#8220;uid !~ Test&#8221;
</dl>
</dl>
<p> which is equivalent to </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&#8211;import &#8211; filter keep &#8211; uid = &#8220;uid =~ Alfa&#8221; &amp;&amp; uid !~Test &#8221; || uid =~ Alpha&#8221; &amp;&amp; &#8220;uid !~ Test&#8221;
</dl>
</dl>
<p> imports only the user ids of a key containing the strings &quot;Alfa&quot; or &quot;Alpha&quot; but not the string &quot;test&quot;. </p>
<h2>TRUST VALUES</h2>
<p> Trust values are used to indicate ownertrust and validity of keys and user IDs. They are displayed with letters or strings: </p>
<dl>
<dt><code>&#8211;</code></p>
<dd> <code>unknown</code> No ownertrust assigned / not yet calculated. </p>
<dt><code>e</code></p>
<dd> <code>expired</code> </p>
<p> Trust calculation has failed; probably due to an expired key. </p>
<dt><code>q</code></p>
<dd> <code>undefined, undef</code> Not enough information for calculation. </p>
<dt><code>n</code></p>
<dd> <code>never</code> Never trust this key. </p>
<dt><code>m</code></p>
<dd> <code>marginal</code> Marginally trusted. </p>
<dt><code>f</code></p>
<dd> <code>full</code> Fully trusted. </p>
<dt><code>u</code></p>
<dd> <code>ultimate</code> Ultimately trusted. </p>
<dt><code>r</code></p>
<dd> <code>revoked</code> For validity only: the key or the user ID has been revoked. </p>
<dt><code>?</code></p>
<dd> <code>err</code> The program encountered an unknown trust value. </p>
</dl>
<h2>FILES</h2>
<p> There are a few configuration files to control certain aspects of <code>gpg</code>&#8216;s operation. Unless noted, they are expected in the current home directory (see: [option &#8211;homedir]). </p>
<dl>
<dt><code>gpg.conf</code></p>
<dd> This is the standard configuration file read by <code>gpg</code> on startup. It may contain any valid long option; the leading two dashes may not be entered and the option may not be abbreviated. This default name may be changed on the command line (see: [gpg-option &#8211;options]). You should backup this file. </p>
</dl>
<p> Note that on larger installations, it is useful to put predefined files into the directory &#8216;<i>/etc/skel/.gnupg</i>&#8216; so that newly created users start up with a working configuration. For existing users a small helper script is provided to create these files (see: [addgnupghome]). </p>
<p> For internal purposes <code>gpg</code> creates and maintains a few other files; They all live in the current home directory (see: [option &#8211;homedir]). Only the <code>gpg</code> program may modify these files. </p>
<dl>
<dt><code>~/.gnupg</code></p>
<dd> This is the default home directory which is used if neither the environment variable <code>GNUPGHOME</code> nor the option <code>&#8211;homedir</code> is given. </p>
<dt><code>~/.gnupg/pubring.gpg</code></p>
<dd> The public keyring using a legacy format. You should backup this file. </p>
<p> If this file is not available, <code>gpg</code> defaults to the new keybox format and creates a file &#8216;<i>pubring.kbx</i>&#8216; unless that file already exists in which case that file will also be used for OpenPGP keys. </p>
<p> Note that in the case that both files, &#8216;<i>pubring.gpg</i>&#8216; and &#8216;<i>pubring.kbx</i>&#8216; exists but the latter has no OpenPGP keys, the legacy file &#8216;<i>pubring.gpg</i>&#8216; will be used. Take care: GnuPG versions before 2.1 will always use the file &#8216;<i>pubring.gpg</i>&#8216; because they do not know about the new keybox format. In the case that you have to use GnuPG 1.4 to decrypt archived data you should keep this file. </p>
<dt><code>~/.gnupg/pubring.gpg.lock</code></p>
<dd> The lock file for the public keyring. </p>
<dt><code>~/.gnupg/pubring.kbx</code></p>
<dd> The public keyring using the new keybox format. This file is shared with <code>gpgsm</code>. You should backup this file. See above for the relation between this file and it predecessor. </p>
<p> To convert an existing &#8216;<i>pubring.gpg</i>&#8216; file to the keybox format, you first backup the ownertrust values, then rename &#8216;<i>pubring.gpg</i>&#8216; to &#8216;<i>publickeys.backup</i>&#8216;, so it won’t be recognized by any GnuPG version, run import, and finally restore the ownertrust values: </p>
<dl>
<dt>
<dd>
<pre><code>
$ cd ~ /.gnupg
                $ gpg-- export -
        ownertrust &gt;
    otrust.lst
            $ mv pubring.gpg publickeys.backup
                $ gpg-- import -
        options restore-- import publickeys.backups
            $ gpg-- import -
        ownertrust otrust.lst
</code></pre>
</dl>
<dt><code>~/.gnupg/pubring.kbx.lock</code></p>
<dd> The lock file for &#8216;<i>pubring.kbx</i>&#8216;. </p>
<dt><code>~/.gnupg/secring.gpg</code></p>
<dd> The legacy secret keyring as used by GnuPG versions before 2.1. It is not used by GnuPG 2.1 and later. You may want to keep it in case you have to use GnuPG 1.4 to decrypt archived data. </p>
<dt><code>~/.gnupg/secring.gpg.lock</code></p>
<dd> The lock file for the legacy secret keyring. </p>
<dt><code>~/.gnupg/.gpg-v21-migrated</code></p>
<dd> File indicating that a migration to GnuPG 2.1 has been done. </p>
<dt><code>~/.gnupg/trustdb.gpg</code></p>
<dd> The trust database. There is no need to backup this file; it is better to backup the ownertrust values (see: [option &#8211;export-ownertrust]). </p>
<dt><code>~/.gnupg/trustdb.gpg.lock</code></p>
<dd> The lock file for the trust database. </p>
<dt><code>~/.gnupg/random_seed</code></p>
<dd> A file used to preserve the state of the internal random pool. </p>
<dt><code>~/.gnupg/openpgp-revocs.d/</code></p>
<dd> This is the directory where gpg stores pre-generated revocation certificates. The file name corresponds to the OpenPGP fingerprint of the respective key. It is suggested to backup those certificates and if the primary private key is not stored on the disk to move them to an external storage device. Anyone who can access theses files is able to revoke the corresponding key. You may want to print them out. You should backup all files in this directory and take care to keep this backup closed away. </p>
</dl>
<p> Operation is further controlled by a few environment variables: </p>
<dl>
<dt><code>HOME</code></p>
<dd> Used to locate the default home directory. </p>
<dt><code>GNUPGHOME</code></p>
<dd> If set directory used instead of &quot;~/.gnupg&quot;. </p>
<dt><code>GPG_AGENT_INFO</code></p>
<dd> This variable is obsolete; it was used by GnuPG versions before 2.1. </p>
<dt><code>PINENTRY_USER_DATA</code></p>
<dd> This value is passed via gpg-agent to pinentry. It is useful to convey extra information to a custom pinentry. </p>
<dt><code>COLUMNS</code></p>
<dd> <code>LINES</code> Used to size some displays to the full size of the screen. </p>
<dt><code>LANGUAGE</code></p>
<dd> Apart from its use by GNU, it is used in the W32 version to override the language selection done through the Registry. If used and set to a valid and available language name (<i>langid</i>), the file with the translation is loaded from <i>gpgdir</i>/gnupg.nls/<i>langid</i>.mo. Here <i>gpgdir</i> is the directory out of which the gpg binary has been loaded. If it can&#8217;t be loaded the Registry is tried and as last resort the native Windows locale system is used. </p>
</dl>
<p> When calling the gpg-agent component <code>gpg</code> sends a set of environment variables to gpg-agent. The names of these variables can be listed using the command: </p>
<dl>
<dt>
<dd>
<pre>
  gpg-connect-agent 'getinfo std_env_names' /bye | awk '$1==&quot;D&quot; {print $2}'
</pre>
</dl>
<h2>BUGS</h2>
<p> On older systems this program should be installed as setuid(root). This is necessary to lock memory pages. Locking memory pages prevents the operating system from writing memory pages (which may contain passphrases or other sensitive material) to disk. If you get no warning message about insecure memory your operating system supports locking without being root. The program drops root privileges as soon as locked memory is allocated. </p>
<p> Note also that some systems (especially laptops) have the ability to &#8220;suspend to disk&#8221; (also known as &#8220;safe sleep&#8221; or &#8220;hibernate&#8221;). This writes all memory to disk before going into a low power or even powered off mode. Unless measures are taken in the operating system to protect the saved memory, passphrases or other sensitive material may be recoverable from it later. </p>
<p> Before you report a bug you should first search the mailing list archives for similar problems and second check whether such a bug has already been reported to our bug tracker at <code><a rel="nofollow" href="https://bugs.gnupg.org">https://bugs.gnupg.org</a></code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpgv/">gpgv</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
