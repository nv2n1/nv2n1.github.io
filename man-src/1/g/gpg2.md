---
title: "gpg2(1)"
name: "gpg2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg2/"
description: "gpg2 – OpenPGP encryption and signing tool"
---

<h2>NAME</h2>
<p> <code>gpg2</code> &#8211; OpenPGP encryption and signing tool</p>
<h2>SYNOPSIS</h2>
<p> <code>gpg2</code> [<code>&#8211;homedir</code> <i>dir</i>] [<code>&#8211;options</code> <i>file</i>] [<i>options</i>] <i>command</i> [<i>args</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>gpg2</code> is the OpenPGP part of the GNU Privacy Guard (GnuPG). It is a tool to provide digital encryption and signing services using the OpenPGP standard. <code>gpg2</code> features complete key management and all bells and whistles you can expect from a decent OpenPGP implementation. </p>
<p> In contrast to the standalone version <code>gpg</code>, which is more suited for server and embedded platforms, this version is commonly installed under the name <code>gpg2</code> and more targeted to the desktop as it requires several other modules to be installed. The standalone version will be kept maintained and it is possible to install both versions on the same system. If you need to use different configuration files, you should make use of something like &#8216;<i>gpg.conf-2</i>&#8216; instead of just &#8216;<i>gpg.conf</i>&#8216;. </p>
<h2>RETURN VALUE</h2>
<p> The program returns 0 if everything was fine, 1 if at least a signature was bad, and other error codes for fatal errors. </p>
<h2>WARNINGS</h2>
<p> Use a *good* password for your user account and a *good* passphrase to protect your secret key. This passphrase is the weakest part of the whole system. Programs to do dictionary attacks on your secret keyring are very easy to write and so you should protect your &quot;~/.gnupg/&quot; directory very well. </p>
<p> Keep in mind that, if this program is used over a network (telnet), it is *very* easy to spy out your passphrase! </p>
<p> If you are going to verify detached signatures, make sure that the program knows about it; either give both filenames on the command line or use &#8216;-&#8216; to specify STDIN. </p>
<h2>INTEROPERABILITY</h2>
<p> GnuPG tries to be a very flexible implementation of the OpenPGP standard. In particular, GnuPG implements many of the optional parts of the standard, such as the SHA-512 hash, and the ZLIB and BZIP2 compression algorithms. It is important to be aware that not all OpenPGP programs implement these optional algorithms and that by forcing their use via the <code>&#8211;cipher-algo</code>, <code>&#8211;digest-algo</code>, <code>&#8211;cert-digest-algo</code>, or <code>&#8211;compress-algo</code> options in GnuPG, it is possible to create a perfectly valid OpenPGP message, but one that cannot be read by the intended recipient. </p>
<p> There are dozens of variations of OpenPGP programs available, and each supports a slightly different subset of these optional algorithms. For example, until recently, no (unhacked) version of PGP supported the BLOWFISH cipher algorithm. A message using BLOWFISH simply could not be read by a PGP user. By default, GnuPG uses the standard OpenPGP preferences system that will always do the right thing and create messages that are usable by all recipients, regardless of which OpenPGP program they use. Only override this safe default if you really know what you are doing. </p>
<p> If you absolutely must override the safe default, or if the preferences on a given key are invalid for some reason, you are far better off using the <code>&#8211;pgp6</code>, <code>&#8211;pgp7</code>, or <code>&#8211;pgp8</code> options. These options are safe as they do not force any particular algorithms in violation of OpenPGP, but rather reduce the available algorithms to a &quot;PGP-safe&quot; list. </p>
<h2>COMMANDS</h2>
<p> Commands are not distinguished from options except for the fact that only one command is allowed. </p>
<p> <code>gpg2</code> may be run with no commands, in which case it will perform a reasonable action depending on the type of file it is given as input (an encrypted message is decrypted, a signature is verified, a file containing keys is listed). </p>
<p> Please remember that option as well as command parsing stops as soon as a non-option is encountered, you can explicitly stop parsing by using the special option <code>&#8212;</code>. </p>
<h3>Commands not specific to the function</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the program version and licensing information. Note that you cannot abbreviate this command. </dd>
<dt><code>&#8211;help</code></dt>
<dd>
</dd><dt><code>-h</code></dt>
<dd> Print a usage message summarizing the most useful command line options. Note that you cannot abbreviate this command. </dd>
<dt><code>&#8211;warranty</code></dt>
<dd> Print warranty information. </dd>
<dt><code>&#8211;dump-options</code></dt>
<dd> Print a list of all available options and commands. Note that you cannot abbreviate this command. </dd>
</dl>
<h3>Commands to select the type of operation</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>&#8211;sign</code></dt>
<dd>
</dd><dt><code>-s</code></dt>
<dd> Make a signature. This command may be combined with <code>&#8211;encrypt</code> (for a signed and encrypted message), <code>&#8211;symmetric</code> (for a signed and symmetrically encrypted message), or <code>&#8211;encrypt</code> and <code>&#8211;symmetric</code> together (for a signed message that may be decrypted via a secret key or a passphrase). The key to be used for signing is chosen by default or can be set with the <code>&#8211;local-user</code> and <code>&#8211;default-key</code> options. </dd>
<dt><code>&#8211;clearsign</code></dt>
<dd> Make a clear text signature. The content in a clear text signature is readable without any special software. OpenPGP software is only needed to verify the signature. Clear text signatures may modify end-of-line whitespace for platform independence and are not intended to be reversible. The key to be used for signing is chosen by default or can be set with the <code>&#8211;local-user</code> and <code>&#8211;default-key</code> options. </dd>
<dt><code>&#8211;detach-sign</code></dt>
<dd>
</dd><dt><code>-b</code></dt>
<dd> Make a detached signature. </dd>
<dt><code>&#8211;encrypt</code></dt>
<dd>
</dd><dt><code>-e</code></dt>
<dd> Encrypt data. This option may be combined with <code>&#8211;sign</code> (for a signed and encrypted message), <code>&#8211;symmetric</code> (for a message that may be decrypted via a secret key or a passphrase), or <code>&#8211;sign</code> and <code>&#8211;symmetric</code> together (for a signed message that may be decrypted via a secret key or a passphrase). </dd>
<dt><code>&#8211;symmetric</code></dt>
<dd>
</dd><dt><code>-c</code></dt>
<dd> Encrypt with a symmetric cipher using a passphrase. The default symmetric cipher used is CAST5, but may be chosen with the <code>&#8211;cipher-algo</code> option. This option may be combined with <code>&#8211;sign</code> (for a signed and symmetrically encrypted message), <code>&#8211;encrypt</code> (for a message that may be decrypted via a secret key or a passphrase), or <code>&#8211;sign</code> and <code>&#8211;encrypt</code> together (for a signed message that may be decrypted via a secret key or a passphrase). </dd>
<dt><code>&#8211;store</code></dt>
<dd> Store only (make a simple RFC1991 literal data packet). </dd>
<dt><code>&#8211;decrypt</code></dt>
<dd>
</dd><dt><code>-d</code></dt>
<dd> Decrypt the file given on the command line (or STDIN if no file is specified) and write it to STDOUT (or the file specified with <code>&#8211;output</code>). If the decrypted file is signed, the signature is also verified. This command differs from the default operation, as it never writes to the filename which is included in the file and it rejects files which don&#8217;t begin with an encrypted message. </dd>
<dt><code>&#8211;verify</code></dt>
<dd> Assume that the first argument is a signed file or a detached signature and verify it without generating any output. With no arguments, the signature packet is read from STDIN. If only a sigfile is given, it may be a complete signature or a detached signature, in which case the signed stuff is expected in a file without the &quot;.sig&quot; or &quot;.asc&quot; extension. With more than 1 argument, the first should be a detached signature and the remaining files are the signed stuff. To read the signed stuff from STDIN, use &#8216;-&#8216; as the second filename. For security reasons a detached signature cannot read the signed material from STDIN without denoting it in the above way. </dd>
<p> Note: When verifying a cleartext signature, <code>gpg</code> verifies only what makes up the cleartext signed data and not any extra data outside of the cleartext signature or header lines following directly the dash marker line. The option <code>&#8211;output</code> may be used to write out the actual signed data; but there are other pitfalls with this format as well. It is suggested to avoid cleartext signatures in favor of detached signatures. </p>
<dt><code>&#8211;multifile</code></dt>
<dd> This modifies certain other commands to accept multiple files for processing on the command line or read from STDIN with each filename on a separate line. This allows for many files to be processed at once. <code>&#8211;multifile</code> may currently be used along with <code>&#8211;verify</code>, <code>&#8211;encrypt</code>, and <code>&#8211;decrypt</code>. Note that <code>&#8211;multifile &#8211;verify</code> may not be used with detached signatures. </dd>
<dt><code>&#8211;verify-files</code></dt>
<dd> Identical to <code>&#8211;multifile &#8211;verify</code>. </dd>
<dt><code>&#8211;encrypt-files</code></dt>
<dd> Identical to <code>&#8211;multifile &#8211;encrypt</code>. </dd>
<dt><code>&#8211;decrypt-files</code></dt>
<dd> Identical to <code>&#8211;multifile &#8211;decrypt</code>. </dd>
<dt><code>&#8211;list-keys</code></dt>
<dd>
</dd><dt><code>-k</code></dt>
<dd>
</dd><dt><code>&#8211;list-public-keys</code></dt>
<dd> List all keys from the public keyrings, or just the keys given on the command line. </dd>
<p> Avoid using the output of this command in scripts or other programs as it is likely to change as GnuPG changes. See <code>&#8211;with-colons</code> for a machine-parseable key listing command that is appropriate for use in scripts and other programs. </p>
<dt><code>&#8211;list-secret-keys</code></dt>
<dd>
</dd><dt><code>-K</code></dt>
<dd> List all keys from the secret keyrings, or just the ones given on the command line. A <code>#</code> after the letters <code>sec</code> means that the secret key is not usable (for example, if it was created via <code>&#8211;export-secret-subkeys</code>). </dd>
<dt><code>&#8211;list-sigs</code></dt>
<dd> Same as <code>&#8211;list-keys</code>, but the signatures are listed too. This command has the same effect as using <code>&#8211;list-keys</code> with <code>&#8211;with-sig-list</code>. </dd>
<p> For each signature listed, there are several flags in between the &quot;sig&quot; tag and keyid. These flags give additional information about each signature. From left to right, they are the numbers 1-3 for certificate check level (see <code>&#8211;ask-cert-level</code>), &quot;L&quot; for a local or non-exportable signature (see <code>&#8211;lsign-key</code>), &quot;R&quot; for a nonRevocable signature (see the <code>&#8211;edit-key</code> command &quot;nrsign&quot;), &quot;P&quot; for a signature that contains a policy URL (see <code>&#8211;cert-policy-url</code>), &quot;N&quot; for a signature that contains a notation (see <code>&#8211;cert-notation</code>), &quot;X&quot; for an eXpired signature (see <code>&#8211;ask-cert-expire</code>), and the numbers 1-9 or &quot;T&quot; for 10 and above to indicate trust signature levels (see the <code>&#8211;edit-key</code> command &quot;tsign&quot;). </p>
<dt><code>&#8211;check-sigs</code></dt>
<dd> Same as <code>&#8211;list-sigs</code>, but the signatures are verified. Note that for performance reasons the revocation status of a signing key is not shown. This command has the same effect as using <code>&#8211;list-keys</code> with <code>&#8211;with-sig-check</code>. </dd>
<p> The status of the verification is indicated by a flag directly following the &quot;sig&quot; tag (and thus before the flags described above for <code>&#8211;list-sigs</code>). A &quot;!&quot; indicates that the signature has been successfully verified, a &quot;-&quot; denotes a bad signature and a &quot;%&quot; is used if an error occurred while checking the signature (e.g. a non supported algorithm). </p>
<dt><code>&#8211;locate-keys</code></dt>
<dd> Locate the keys given as arguments. This command basically uses the same algorithm as used when locating keys for encryption or signing and may thus be used to see what keys <code>gpg2</code> might use. In particular external methods as defined by <code>&#8211;auto-key-locate</code> may be used to locate a key. Only public keys are listed. </dd>
<dt><code>&#8211;fingerprint</code></dt>
<dd> List all keys (or the specified ones) along with their fingerprints. This is the same output as <code>&#8211;list-keys</code> but with the additional output of a line with the fingerprint. May also be combined with <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code>. If this command is given twice, the fingerprints of all secondary keys are listed too. </dd>
<dt><code>&#8211;list-packets</code></dt>
<dd> List only the sequence of packets. This is mainly useful for debugging. </dd>
<dt><code>&#8211;card-edit</code></dt>
<dd> Present a menu to work with a smartcard. The subcommand &quot;help&quot; provides an overview on available commands. For a detailed description, please see the Card HOWTO at <a rel="nofollow" href="http://www.gnupg.org/documentation/howtos.html#GnuPG-cardHOWTO">http://www.gnupg.org/documentation/howtos.html#GnuPG-cardHOWTO</a> . </dd>
<dt><code>&#8211;card-status</code></dt>
<dd> Show the content of the smart card. </dd>
<dt><code>&#8211;change-pin</code></dt>
<dd> Present a menu to allow changing the PIN of a smartcard. This functionality is also available as the subcommand &quot;passwd&quot; with the <code>&#8211;card-edit</code> command. </dd>
<dt><code>&#8211;delete-key name</code></dt>
<dd> Remove key from the public keyring. In batch mode either <code>&#8211;yes</code> is required or the key must be specified by fingerprint. This is a safeguard against accidental deletion of multiple keys. </dd>
<dt><code>&#8211;delete-secret-key name</code></dt>
<dd> Remove key from the secret keyring. In batch mode the key must be specified by fingerprint. </dd>
<dt><code>&#8211;delete-secret-and-public-key name</code></dt>
<dd> Same as <code>&#8211;delete-key</code>, but if a secret key exists, it will be removed first. In batch mode the key must be specified by fingerprint. </dd>
<dt><code>&#8211;export</code></dt>
<dd> Either export all keys from all keyrings (default keyrings and those registered via option <code>&#8211;keyring</code>), or if at least one name is given, those of the given name. The new keyring is written to STDOUT or to the file given with option <code>&#8211;output</code>. Use together with <code>&#8211;armor</code> to mail those keys. </dd>
<dt><code>&#8211;send-keys key IDs</code></dt>
<dd> Similar to <code>&#8211;export</code> but sends the keys to a keyserver. Fingerprints may be used instead of key IDs. Option <code>&#8211;keyserver</code> must be used to give the name of this keyserver. Don&#8217;t send your complete keyring to a keyserver &#8212; select only those keys which are new or changed by you. If no key IDs are given, <code>gpg</code> does nothing. </dd>
<dt><code>&#8211;export-secret-keys</code></dt>
<dd>
</dd><dt><code>&#8211;export-secret-subkeys</code></dt>
<dd> Same as <code>&#8211;export</code>, but exports the secret keys instead. This is normally not very useful and a security risk. The second form of the command has the special property to render the secret part of the primary key useless; this is a GNU extension to OpenPGP and other implementations can not be expected to successfully import such a key. See the option <code>&#8211;simple-sk-checksum</code> if you want to import such an exported key with an older OpenPGP implementation. </dd>
<dt><code>&#8211;import</code></dt>
<dd>
</dd><dt><code>&#8211;fast-import</code></dt>
<dd> Import/merge keys. This adds the given keys to the keyring. The fast version is currently just a synonym. </dd>
<p> There are a few other options which control how this command works. Most notable here is the <code>&#8211;import-options merge-only</code> option which does not insert new keys but does only the merging of new signatures, user-IDs and subkeys. </p>
<dt><code>&#8211;recv-keys key IDs</code></dt>
<dd> Import the keys with the given key IDs from a keyserver. Option <code>&#8211;keyserver</code> must be used to give the name of this keyserver. </dd>
<dt><code>&#8211;refresh-keys</code></dt>
<dd> Request updates from a keyserver for keys that already exist on the local keyring. This is useful for updating a key with the latest signatures, user IDs, etc. Calling this with no arguments will refresh the entire keyring. Option <code>&#8211;keyserver</code> must be used to give the name of the keyserver for all keys that do not have preferred keyservers set (see <code>&#8211;keyserver-options honor-keyserver-url</code>). </dd>
<dt><code>&#8211;search-keys names</code></dt>
<dd> Search the keyserver for the given names. Multiple names given here will be joined together to create the search string for the keyserver. Option <code>&#8211;keyserver</code> must be used to give the name of this keyserver. Keyservers that support different search methods allow using the syntax specified in &quot;How to specify a user ID&quot; below. Note that different keyserver types support different search methods. Currently only LDAP supports them all. </dd>
<dt><code>&#8211;fetch-keys URIs</code></dt>
<dd> Retrieve keys located at the specified URIs. Note that different installations of GnuPG may support different protocols (HTTP, FTP, LDAP, etc.) </dd>
<dt><code>&#8211;update-trustdb</code></dt>
<dd> Do trust database maintenance. This command iterates over all keys and builds the Web of Trust. This is an interactive command because it may have to ask for the &quot;ownertrust&quot; values for keys. The user has to give an estimation of how far she trusts the owner of the displayed key to correctly certify (sign) other keys. GnuPG only asks for the ownertrust value if it has not yet been assigned to a key. Using the <code>&#8211;edit-key</code> menu, the assigned value can be changed at any time. </dd>
<dt><code>&#8211;check-trustdb</code></dt>
<dd> Do trust database maintenance without user interaction. From time to time the trust database must be updated so that expired keys or signatures and the resulting changes in the Web of Trust can be tracked. Normally, GnuPG will calculate when this is required and do it automatically unless <code>&#8211;no-auto-check-trustdb</code> is set. This command can be used to force a trust database check at any time. The processing is identical to that of <code>&#8211;update-trustdb</code> but it skips keys with a not yet defined &quot;ownertrust&quot;. </dd>
<p> For use with cron jobs, this command can be used together with <code>&#8211;batch</code> in which case the trust database check is done only if a check is needed. To force a run even in batch mode add the option <code>&#8211;yes</code>. </p>
<dt><code>&#8211;export-ownertrust</code></dt>
<dd> Send the ownertrust values to STDOUT. This is useful for backup purposes as these values are the only ones which can&#8217;t be re-created from a corrupted trustdb. Example:</dd>
<dl>
<dl>
<dt>
</dt><dd>
<pre>
  gpg2 --export-ownertrust &gt; otrust.txt
</pre>
</dd></dl>
</dl>
<dt><code>&#8211;import-ownertrust</code></dt>
<dd> Update the trustdb with the ownertrust values stored in <code>files</code> (or STDIN if not given); existing values will be overwritten. In case of a severely damaged trustdb and if you have a recent backup of the ownertrust values (e.g. in the file &#8216;<i>otrust.txt</i>&#8216;, you may re-create the trustdb using these commands:</dd>
<dl>
<dl>
<dt>
</dt><dd>
<pre>
  cd ~/.gnupg
  rm trustdb.gpg
  gpg2 --import-ownertrust &lt; otrust.txt
</pre>
</dd></dl>
</dl>
<dt><code>&#8211;rebuild-keydb-caches</code></dt>
<dd> When updating from version 1.0.6 to 1.0.7 this command should be used to create signature caches in the keyring. It might be handy in other situations too. </dd>
<dt><code>&#8211;print-md algo</code></dt>
<dd>
</dd><dt><code>&#8211;print-mds</code></dt>
<dd> Print message digest of algorithm ALGO for all given files or STDIN. With the second form (or a deprecated &quot;*&quot; as algo) digests for all available algorithms are printed. </dd>
<dt><code>&#8211;gen-random 0|1|2</code> <code>count</code></dt>
<dd> Emit <i>count</i> random bytes of the given quality level 0, 1 or 2. If <i>count</i> is not given or zero, an endless sequence of random bytes will be emitted. If used with <code>&#8211;armor</code> the output will be base64 encoded. PLEASE, don&#8217;t use this command unless you know what you are doing; it may remove precious entropy from the system! </dd>
<dt><code>&#8211;gen-prime mode</code> <code>bits</code></dt>
<dd> Use the source, Luke :-). The output format is still subject to change. </dd>
<dt><code>&#8211;enarmor</code></dt>
<dd>
</dd><dt><code>&#8211;dearmor</code></dt>
<dd> Pack or unpack an arbitrary input into/from an OpenPGP ASCII armor. This is a GnuPG extension to OpenPGP and in general not very useful. </dd>
</dl>
<h3>How to manage your keys</h3>
<p> &nbsp;<wbr> </p>
<p> This section explains the main commands for key management </p>
<dl>
<dt><code>&#8211;gen-key</code></dt>
<dd> Generate a new key pair. This command is normally only used interactively. </dd>
<p> There is an experimental feature which allows you to create keys in batch mode. See the file &#8216;<i>doc/DETAILS</i>&#8216; in the source distribution on how to use this. </p>
<dt><code>&#8211;gen-revoke name</code></dt>
<dd> Generate a revocation certificate for the complete key. To revoke a subkey or a signature, use the <code>&#8211;edit</code> command. </dd>
<dt><code>&#8211;desig-revoke name</code></dt>
<dd> Generate a designated revocation certificate for a key. This allows a user (with the permission of the keyholder) to revoke someone else&#8217;s key. </dd>
<dt><code>&#8211;edit-key</code></dt>
<dd> Present a menu which enables you to do most of the key management related tasks. It expects the specification of a key on the command line. </dd>
<dl>
<dl>
<dt><code>uid n</code></dt>
<dd> Toggle selection of user ID or photographic user ID with index <code>n</code>. Use <code>*</code> to select all and <code>0</code> to deselect all. </dd>
<dt><code>key n</code></dt>
<dd> Toggle selection of subkey with index <code>n</code>. Use <code>*</code> to select all and <code>0</code> to deselect all. </dd>
<dt><code>sign</code></dt>
<dd> Make a signature on key of user <code>name</code> If the key is not yet signed by the default user (or the users given with -u), the program displays the information of the key again, together with its fingerprint and asks whether it should be signed. This question is repeated for all users specified with -u. </dd>
<dt><code>lsign</code></dt>
<dd> Same as &quot;sign&quot; but the signature is marked as non-exportable and will therefore never be used by others. This may be used to make keys valid only in the local environment. </dd>
<dt><code>nrsign</code></dt>
<dd> Same as &quot;sign&quot; but the signature is marked as non-revocable and can therefore never be revoked. </dd>
<dt><code>tsign</code></dt>
<dd> Make a trust signature. This is a signature that combines the notions of certification (like a regular signature), and trust (like the &quot;trust&quot; command). It is generally only useful in distinct communities or groups.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Note that &quot;l&quot; (for local / non-exportable), &quot;nr&quot; (for non-revocable, and &quot;t&quot; (for trust) may be freely mixed and prefixed to &quot;sign&quot; to create a signature of any type desired.</dd></dl>
<dl>
<dl>
<dt><code>delsig</code></dt>
<dd> Delete a signature. Note that it is not possible to retract a signature, once it has been send to the public (i.e. to a keyserver). In that case you better use <code>revsig</code>. </dd>
<dt><code>revsig</code></dt>
<dd> Revoke a signature. For every signature which has been generated by one of the secret keys, GnuPG asks whether a revocation certificate should be generated. </dd>
<dt><code>check</code></dt>
<dd> Check the signatures on all selected user IDs. </dd>
<dt><code>adduid</code></dt>
<dd> Create an additional user ID. </dd>
<dt><code>addphoto</code></dt>
<dd> Create a photographic user ID. This will prompt for a JPEG file that will be embedded into the user ID. Note that a very large JPEG will make for a very large key. Also note that some programs will display your JPEG unchanged (GnuPG), and some programs will scale it to fit in a dialog box (PGP). </dd>
<dt><code>showphoto</code></dt>
<dd> Display the selected photographic user ID. </dd>
<dt><code>deluid</code></dt>
<dd> Delete a user ID or photographic user ID. Note that it is not possible to retract a user id, once it has been send to the public (i.e. to a keyserver). In that case you better use <code>revuid</code>. </dd>
<dt><code>revuid</code></dt>
<dd> Revoke a user ID or photographic user ID. </dd>
<dt><code>primary</code></dt>
<dd> Flag the current user id as the primary one, removes the primary user id flag from all other user ids and sets the timestamp of all affected self-signatures one second ahead. Note that setting a photo user ID as primary makes it primary over other photo user IDs, and setting a regular user ID as primary makes it primary over other regular user IDs. </dd>
<dt><code>keyserver</code></dt>
<dd> Set a preferred keyserver for the specified user ID(s). This allows other users to know where you prefer they get your key from. See <code>&#8211;keyserver-options honor-keyserver-url</code> for more on how this works. Setting a value of &quot;none&quot; removes an existing preferred keyserver. </dd>
<dt><code>notation</code></dt>
<dd> Set a name=value notation for the specified user ID(s). See <code>&#8211;cert-notation</code> for more on how this works. Setting a value of &quot;none&quot; removes all notations, setting a notation prefixed with a minus sign (-) removes that notation, and setting a notation name (without the =value) prefixed with a minus sign removes all notations with that name. </dd>
<dt><code>pref</code></dt>
<dd> List preferences from the selected user ID. This shows the actual preferences, without including any implied preferences. </dd>
<dt><code>showpref</code></dt>
<dd> More verbose preferences listing for the selected user ID. This shows the preferences in effect by including the implied preferences of 3DES (cipher), SHA-1 (digest), and Uncompressed (compression) if they are not already included in the preference list. In addition, the preferred keyserver and signature notations (if any) are shown. </dd>
<dt><code>setpref string</code></dt>
<dd> Set the list of user ID preferences to <code>string</code> for all (or just the selected) user IDs. Calling setpref with no arguments sets the preference list to the default (either built-in or set via <code>&#8211;default-preference-list</code>), and calling setpref with &quot;none&quot; as the argument sets an empty preference list. Use <code>gpg2 &#8211;version</code> to get a list of available algorithms. Note that while you can change the preferences on an attribute user ID (aka &quot;photo ID&quot;), GnuPG does not select keys via attribute user IDs so these preferences will not be used by GnuPG. </dd>
<p> When setting preferences, you should list the algorithms in the order which you&#8217;d like to see them used by someone else when encrypting a message to your key. If you don&#8217;t include 3DES, it will be automatically added at the end. Note that there are many factors that go into choosing an algorithm (for example, your key may not be the only recipient), and so the remote OpenPGP application being used to send to you may or may not follow your exact chosen order for a given message. It will, however, only choose an algorithm that is present on the preference list of every recipient key. See also the INTEROPERABILITY WITH OTHER OPENPGP PROGRAMS section below. </p>
<dt><code>addkey</code></dt>
<dd> Add a subkey to this key. </dd>
<dt><code>addcardkey</code></dt>
<dd> Generate a subkey on a card and add it to this key. </dd>
<dt><code>keytocard</code></dt>
<dd> Transfer the selected secret subkey (or the primary key if no subkey has been selected) to a smartcard. The secret key in the keyring will be replaced by a stub if the key could be stored successfully on the card and you use the save command later. Only certain key types may be transferred to the card. A sub menu allows you to select on what card to store the key. Note that it is not possible to get that key back from the card &#8211; if the card gets broken your secret key will be lost unless you have a backup somewhere. </dd>
<dt><code>bkuptocard file</code></dt>
<dd> Restore the given file to a card. This command may be used to restore a backup key (as generated during card initialization) to a new card. In almost all cases this will be the encryption key. You should use this command only with the corresponding public key and make sure that the file given as argument is indeed the backup to restore. You should then select 2 to restore as encryption key. You will first be asked to enter the passphrase of the backup key and then for the Admin PIN of the card. </dd>
<dt><code>delkey</code></dt>
<dd> Remove a subkey (secondart key). Note that it is not possible to retract a subkey, once it has been send to the public (i.e. to a keyserver). In that case you better use <code>revkey</code>. </dd>
<dt><code>revkey</code></dt>
<dd> Revoke a subkey. </dd>
<dt><code>expire</code></dt>
<dd> Change the key or subkey expiration time. If a subkey is selected, the expiration time of this subkey will be changed. With no selection, the key expiration of the primary key is changed. </dd>
<dt><code>trust</code></dt>
<dd> Change the owner trust value for the key. This updates the trust-db immediately and no save is required. </dd>
<dt><code>disable</code></dt>
<dd>
</dd><dt><code>enable</code></dt>
<dd> Disable or enable an entire key. A disabled key can not normally be used for encryption. </dd>
<dt><code>addrevoker</code></dt>
<dd> Add a designated revoker to the key. This takes one optional argument: &quot;sensitive&quot;. If a designated revoker is marked as sensitive, it will not be exported by default (see export-options). </dd>
<dt><code>passwd</code></dt>
<dd> Change the passphrase of the secret key. </dd>
<dt><code>toggle</code></dt>
<dd> Toggle between public and secret key listing. </dd>
<dt><code>clean</code></dt>
<dd> Compact (by removing all signatures except the selfsig) any user ID that is no longer usable (e.g. revoked, or expired). Then, remove any signatures that are not usable by the trust calculations. Specifically, this removes any signature that does not validate, any signature that is superseded by a later signature, revoked signatures, and signatures issued by keys that are not present on the keyring. </dd>
<dt><code>minimize</code></dt>
<dd> Make the key as small as possible. This removes all signatures from each user ID except for the most recent self-signature. </dd>
<dt><code>cross-certify</code></dt>
<dd> Add cross-certification signatures to signing subkeys that may not currently have them. Cross-certification signatures protect against a subtle attack against signing subkeys. See <code>&#8211;require-cross-certification</code>. All new keys generated have this signature by default, so this option is only useful to bring older keys up to date. </dd>
<dt><code>save</code></dt>
<dd> Save all changes to the key rings and quit. </dd>
<dt><code>quit</code></dt>
<dd> Quit the program without updating the key rings.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> The listing shows you the key with its secondary keys and all user ids. The primary user id is indicated by a dot, and selected keys or user ids are indicated by an asterisk. The trust value is displayed with the primary key: the first is the assigned owner trust and the second is the calculated trust value. Letters are used for the values:</dd></dl>
<dl>
<dl>
<dt><code>&#8211;</code></dt>
<dd> No ownertrust assigned / not yet calculated. </dd>
<dt><code>e</code></dt>
<dd> Trust calculation has failed; probably due to an expired key. </dd>
<dt><code>q</code></dt>
<dd> Not enough information for calculation. </dd>
<dt><code>n</code></dt>
<dd> Never trust this key. </dd>
<dt><code>m</code></dt>
<dd> Marginally trusted. </dd>
<dt><code>f</code></dt>
<dd> Fully trusted. </dd>
<dt><code>u</code></dt>
<dd> Ultimately trusted. </dd>
</dl>
</dl>
<dt><code>&#8211;sign-key name</code></dt>
<dd> Signs a public key with your secret key. This is a shortcut version of the subcommand &quot;sign&quot; from <code>&#8211;edit</code>. </dd>
<dt><code>&#8211;lsign-key name</code></dt>
<dd> Signs a public key with your secret key but marks it as non-exportable. This is a shortcut version of the subcommand &quot;lsign&quot; from <code>&#8211;edit-key</code>. </dd>
<dt><code>&#8211;passwd </code><i>user_id</i></dt>
<dd> Change the passphrase of the secret key belonging to the certificate specified as <i>user_id</i>. This is a shortcut for the sub-command <code>passwd</code> of the edit key menu. </dd>
</dl>
<h2>OPTIONS</h2>
<p> <code>gpg2</code> features a bunch of options to control the exact behaviour and to change the default configuration. </p>
<p> Long options can be put in an options file (default &quot;~/.gnupg/gpg.conf&quot;). Short option names will not work &#8211; for example, &quot;armor&quot; is a valid option for the options file, while &quot;a&quot; is not. Do not write the 2 dashes, but simply the name of the option and any required arguments. Lines with a hash (&#8216;#&#8217;) as the first non-white-space character are ignored. Commands may be put in this file too, but that is not generally useful as the command will execute automatically with every execution of gpg. </p>
<p> Please remember that option parsing stops as soon as a non-option is encountered, you can explicitly stop parsing by using the special option <code>&#8212;</code>. </p>
<h3>How to change the configuration</h3>
<p> &nbsp;<wbr> </p>
<p> These options are used to change the configuration and are usually found in the option file. </p>
<dl>
<dt><code>&#8211;default-key </code><i>name</i></dt>
<dd> Use <i>name</i> as the default key to sign with. If this option is not used, the default key is the first key found in the secret keyring. Note that <code>-u</code> or <code>&#8211;local-user</code> overrides this option. </dd>
<dt><code>&#8211;default-recipient </code><i>name</i></dt>
<dd> Use <i>name</i> as default recipient if option <code>&#8211;recipient</code> is not used and don&#8217;t ask if this is a valid one. <i>name</i> must be non-empty. </dd>
<dt><code>&#8211;default-recipient-self</code></dt>
<dd> Use the default key as default recipient if option <code>&#8211;recipient</code> is not used and don&#8217;t ask if this is a valid one. The default key is the first one from the secret keyring or the one set with <code>&#8211;default-key</code>. </dd>
<dt><code>&#8211;no-default-recipient</code></dt>
<dd> Reset <code>&#8211;default-recipient</code> and <code>&#8211;default-recipient-self</code>. </dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Give more information during processing. If used twice, the input data is listed in detail. </dd>
<dt><code>&#8211;no-verbose</code></dt>
<dd> Reset verbose level to 0. </dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Try to be as quiet as possible. </dd>
<dt><code>&#8211;batch</code></dt>
<dd>
</dd><dt><code>&#8211;no-batch</code></dt>
<dd> Use batch mode. Never ask, do not allow interactive commands. <code>&#8211;no-batch</code> disables this option. Note that even with a filename given on the command line, gpg might still need to read from STDIN (in particular if gpg figures that the input is a detached signature and no data file has been specified). Thus if you do not want to feed data via STDIN, you should connect STDIN to &#8216;<i>/dev/null</i>&#8216;. </dd>
<dt><code>&#8211;no-tty</code></dt>
<dd> Make sure that the TTY (terminal) is never used for any output. This option is needed in some cases because GnuPG sometimes prints warnings to the TTY even if <code>&#8211;batch</code> is used. </dd>
<dt><code>&#8211;yes</code></dt>
<dd> Assume &quot;yes&quot; on most questions. </dd>
<dt><code>&#8211;no</code></dt>
<dd> Assume &quot;no&quot; on most questions. </dd>
<dt><code>&#8211;list-options parameters</code></dt>
<dd> This is a space or comma delimited string that gives options used when listing keys and signatures (that is, <code>&#8211;list-keys</code>, <code>&#8211;list-sigs</code>, <code>&#8211;list-public-keys</code>, <code>&#8211;list-secret-keys</code>, and the <code>&#8211;edit-key</code> functions). Options can be prepended with a <code>no-</code> (after the two dashes) to give the opposite meaning. The options are: </dd>
<dl>
<dl>
<dt><code>show-photos</code></dt>
<dd> Causes <code>&#8211;list-keys</code>, <code>&#8211;list-sigs</code>, <code>&#8211;list-public-keys</code>, and <code>&#8211;list-secret-keys</code> to display any photo IDs attached to the key. Defaults to no. See also <code>&#8211;photo-viewer</code>. Does not work with <code>&#8211;with-colons</code>: see <code>&#8211;attribute-fd</code> for the appropriate way to get photo data for scripts and other frontends. </dd>
<dt><code>show-policy-urls</code></dt>
<dd> Show policy URLs in the <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code> listings. Defaults to no. </dd>
<dt><code>show-notations</code></dt>
<dd>
</dd><dt><code>show-std-notations</code></dt>
<dd>
</dd><dt><code>show-user-notations</code></dt>
<dd> Show all, IETF standard, or user-defined signature notations in the <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code> listings. Defaults to no. </dd>
<dt><code>show-keyserver-urls</code></dt>
<dd> Show any preferred keyserver URL in the <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code> listings. Defaults to no. </dd>
<dt><code>show-uid-validity</code></dt>
<dd> Display the calculated validity of user IDs during key listings. Defaults to no. </dd>
<dt><code>show-unusable-uids</code></dt>
<dd> Show revoked and expired user IDs in key listings. Defaults to no. </dd>
<dt><code>show-unusable-subkeys</code></dt>
<dd> Show revoked and expired subkeys in key listings. Defaults to no. </dd>
<dt><code>show-keyring</code></dt>
<dd> Display the keyring name at the head of key listings to show which keyring a given key resides on. Defaults to no. </dd>
<dt><code>show-sig-expire</code></dt>
<dd> Show signature expiration dates (if any) during <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code> listings. Defaults to no. </dd>
<dt><code>show-sig-subpackets</code></dt>
<dd> Include signature subpackets in the key listing. This option can take an optional argument list of the subpackets to list. If no argument is passed, list all subpackets. Defaults to no. This option is only meaningful when using <code>&#8211;with-colons</code> along with <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code>. </dd>
</dl>
</dl>
<dt><code>&#8211;verify-options parameters</code></dt>
<dd> This is a space or comma delimited string that gives options used when verifying signatures. Options can be prepended with a `no-&#8216; to give the opposite meaning. The options are: </dd>
<dl>
<dl>
<dt><code>show-photos</code></dt>
<dd> Display any photo IDs present on the key that issued the signature. Defaults to no. See also <code>&#8211;photo-viewer</code>. </dd>
<dt><code>show-policy-urls</code></dt>
<dd> Show policy URLs in the signature being verified. Defaults to no. </dd>
<dt><code>show-notations</code></dt>
<dd>
</dd><dt><code>show-std-notations</code></dt>
<dd>
</dd><dt><code>show-user-notations</code></dt>
<dd> Show all, IETF standard, or user-defined signature notations in the signature being verified. Defaults to IETF standard. </dd>
<dt><code>show-keyserver-urls</code></dt>
<dd> Show any preferred keyserver URL in the signature being verified. Defaults to no. </dd>
<dt><code>show-uid-validity</code></dt>
<dd> Display the calculated validity of the user IDs on the key that issued the signature. Defaults to no. </dd>
<dt><code>show-unusable-uids</code></dt>
<dd> Show revoked and expired user IDs during signature verification. Defaults to no. </dd>
<dt><code>show-primary-uid-only</code></dt>
<dd> Show only the primary user ID during signature verification. That is all the AKA lines as well as photo Ids are not shown with the signature verification status. </dd>
<dt><code>pka-lookups</code></dt>
<dd> Enable PKA lookups to verify sender addresses. Note that PKA is based on DNS, and so enabling this option may disclose information on when and what signatures are verified or to whom data is encrypted. This is similar to the &quot;web bug&quot; described for the auto-key-retrieve feature. </dd>
<dt><code>pka-trust-increase</code></dt>
<dd> Raise the trust in a signature to full if the signature passes PKA validation. This option is only meaningful if pka-lookups is set.</dd></dl>
</dl>
<dt><code>&#8211;enable-dsa2</code></dt>
<dd>
</dd><dt><code>&#8211;disable-dsa2</code></dt>
<dd> Enable hash truncation for all DSA keys even for old DSA Keys up to 1024 bit. This is also the default with <code>&#8211;openpgp</code>. Note that older versions of GnuPG also required this flag to allow the generation of DSA larger than 1024 bit. </dd>
<dt><code>&#8211;photo-viewer string</code></dt>
<dd> This is the command line that should be run to view a photo ID. &quot;%i&quot; will be expanded to a filename containing the photo. &quot;%I&quot; does the same, except the file will not be deleted once the viewer exits. Other flags are &quot;%k&quot; for the key ID, &quot;%K&quot; for the long key ID, &quot;%f&quot; for the key fingerprint, &quot;%t&quot; for the extension of the image type (e.g. &quot;jpg&quot;), &quot;%T&quot; for the MIME type of the image (e.g. &quot;image/jpeg&quot;), &quot;%v&quot; for the single-character calculated validity of the image being viewed (e.g. &quot;f&quot;), &quot;%V&quot; for the calculated validity as a string (e.g. &quot;full&quot;), and &quot;%%&quot; for an actual percent sign. If neither %i or %I are present, then the photo will be supplied to the viewer on standard input. </dd>
<p> The default viewer is &quot;xloadimage -fork -quiet -title &#8216;KeyID 0x%k&#8217; STDIN&quot;. Note that if your image viewer program is not secure, then executing it from GnuPG does not make it secure. </p>
<dt><code>&#8211;exec-path string</code></dt>
<dd> Sets a list of directories to search for photo viewers and keyserver helpers. If not provided, keyserver helpers use the compiled-in default directory, and photo viewers use the $PATH environment variable. Note, that on W32 system this value is ignored when searching for keyserver helpers. </dd>
<dt><code>&#8211;keyring file</code></dt>
<dd> Add <code>file</code> to the current list of keyrings. If <code>file</code> begins with a tilde and a slash, these are replaced by the $HOME directory. If the filename does not contain a slash, it is assumed to be in the GnuPG home directory (&quot;~/.gnupg&quot; if <code>&#8211;homedir</code> or $GNUPGHOME is not used). </dd>
<p> Note that this adds a keyring to the current list. If the intent is to use the specified keyring alone, use <code>&#8211;keyring</code> along with <code>&#8211;no-default-keyring</code>. </p>
<dt><code>&#8211;secret-keyring file</code></dt>
<dd> Same as <code>&#8211;keyring</code> but for the secret keyrings. </dd>
<dt><code>&#8211;primary-keyring file</code></dt>
<dd> Designate <code>file</code> as the primary public keyring. This means that newly imported keys (via <code>&#8211;import</code> or keyserver <code>&#8211;recv-from</code>) will go to this keyring. </dd>
<dt><code>&#8211;trustdb-name file</code></dt>
<dd> Use <code>file</code> instead of the default trustdb. If <code>file</code> begins with a tilde and a slash, these are replaced by the $HOME directory. If the filename does not contain a slash, it is assumed to be in the GnuPG home directory (&#8216;<i>~/.gnupg</i>&#8216; if <code>&#8211;homedir</code> or $GNUPGHOME is not used). </dd>
<dt><code>&#8211;homedir </code><i>dir</i></dt>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on W32 systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </dd>
<dt><code>&#8211;display-charset name</code></dt>
<dd> Set the name of the native character set. This is used to convert some informational strings like user IDs to the proper UTF-8 encoding. Note that this has nothing to do with the character set of data to be encrypted or signed; GnuPG does not recode user-supplied data. If this option is not used, the default character set is determined from the current locale. A verbosity level of 3 shows the chosen set. Valid values for <code>name</code> are: </dd>
<dl>
<dl>
<dt><code>iso-8859-1</code></dt>
<dd> This is the Latin 1 set. </dd>
<dt><code>iso-8859-2</code></dt>
<dd> The Latin 2 set. </dd>
<dt><code>iso-8859-15</code></dt>
<dd> This is currently an alias for the Latin 1 set. </dd>
<dt><code>koi8-r</code></dt>
<dd> The usual Russian set (rfc1489). </dd>
<dt><code>utf-8</code></dt>
<dd> Bypass all translations and assume that the OS uses native UTF-8 encoding.</dd></dl>
</dl>
<dt><code>&#8211;utf8-strings</code></dt>
<dd>
</dd><dt><code>&#8211;no-utf8-strings</code></dt>
<dd> Assume that command line arguments are given as UTF8 strings. The default (<code>&#8211;no-utf8-strings</code>) is to assume that arguments are encoded in the character set as specified by <code>&#8211;display-charset</code>. These options affect all following arguments. Both options may be used multiple times. </dd>
<dt><code>&#8211;options file</code></dt>
<dd> Read options from <code>file</code> and do not try to read them from the default options file in the homedir (see <code>&#8211;homedir</code>). This option is ignored if used in an options file. </dd>
<dt><code>&#8211;no-options</code></dt>
<dd> Shortcut for <code>&#8211;options /dev/null</code>. This option is detected before an attempt to open an option file. Using this option will also prevent the creation of a &#8216;<i>~/.gnupg</i>&#8216; homedir. </dd>
<dt><code>-z n</code></dt>
<dd>
</dd><dt><code>&#8211;compress-level n</code></dt>
<dd>
</dd><dt><code>&#8211;bzip2-compress-level n</code></dt>
<dd> Set compression level to <code>n</code> for the ZIP and ZLIB compression algorithms. The default is to use the default compression level of zlib (normally 6). <code>&#8211;bzip2-compress-level</code> sets the compression level for the BZIP2 compression algorithm (defaulting to 6 as well). This is a different option from <code>&#8211;compress-level</code> since BZIP2 uses a significant amount of memory for each additional compression level. <code>-z</code> sets both. A value of 0 for <code>n</code> disables compression. </dd>
<dt><code>&#8211;bzip2-decompress-lowmem</code></dt>
<dd> Use a different decompression method for BZIP2 compressed files. This alternate method uses a bit more than half the memory, but also runs at half the speed. This is useful under extreme low memory circumstances when the file was originally compressed at a high <code>&#8211;bzip2-compress-level</code>. </dd>
<dt><code>&#8211;mangle-dos-filenames</code></dt>
<dd>
</dd><dt><code>&#8211;no-mangle-dos-filenames</code></dt>
<dd> Older version of Windows cannot handle filenames with more than one dot. <code>&#8211;mangle-dos-filenames</code> causes GnuPG to replace (rather than add to) the extension of an output filename to avoid this problem. This option is off by default and has no effect on non-Windows platforms. </dd>
<dt><code>&#8211;ask-cert-level</code></dt>
<dd>
</dd><dt><code>&#8211;no-ask-cert-level</code></dt>
<dd> When making a key signature, prompt for a certification level. If this option is not specified, the certification level used is set via <code>&#8211;default-cert-level</code>. See <code>&#8211;default-cert-level</code> for information on the specific levels and how they are used. <code>&#8211;no-ask-cert-level</code> disables this option. This option defaults to no. </dd>
<dt><code>&#8211;default-cert-level n</code></dt>
<dd> The default to use for the check level when signing a key. </dd>
<p> 0 means you make no particular claim as to how carefully you verified the key. </p>
<p> 1 means you believe the key is owned by the person who claims to own it but you could not, or did not verify the key at all. This is useful for a &quot;persona&quot; verification, where you sign the key of a pseudonymous user. </p>
<p> 2 means you did casual verification of the key. For example, this could mean that you verified the key fingerprint and checked the user ID on the key against a photo ID. </p>
<p> 3 means you did extensive verification of the key. For example, this could mean that you verified the key fingerprint with the owner of the key in person, and that you checked, by means of a hard to forge document with a photo ID (such as a passport) that the name of the key owner matches the name in the user ID on the key, and finally that you verified (by exchange of email) that the email address on the key belongs to the key owner. </p>
<p> Note that the examples given above for levels 2 and 3 are just that: examples. In the end, it is up to you to decide just what &quot;casual&quot; and &quot;extensive&quot; mean to you. </p>
<p> This option defaults to 0 (no particular claim). </p>
<dt><code>&#8211;min-cert-level</code></dt>
<dd> When building the trust database, treat any signatures with a certification level below this as invalid. Defaults to 2, which disregards level 1 signatures. Note that level 0 &quot;no particular claim&quot; signatures are always accepted. </dd>
<dt><code>&#8211;trusted-key long key ID</code></dt>
<dd> Assume that the specified key (which must be given as a full 8 byte key ID) is as trustworthy as one of your own secret keys. This option is useful if you don&#8217;t want to keep your secret keys (or one of them) online but still want to be able to check the validity of a given recipient&#8217;s or signator&#8217;s key. </dd>
<dt><code>&#8211;trust-model pgp|classic|direct|always|auto</code></dt>
<dd> Set what trust model GnuPG should follow. The models are: </dd>
<dl>
<dl>
<dt><code>pgp</code></dt>
<dd> This is the Web of Trust combined with trust signatures as used in PGP 5.x and later. This is the default trust model when creating a new trust database. </dd>
<dt><code>classic</code></dt>
<dd> This is the standard Web of Trust as used in PGP 2.x and earlier. </dd>
<dt><code>direct</code></dt>
<dd> Key validity is set directly by the user and not calculated via the Web of Trust. </dd>
<dt><code>always</code></dt>
<dd> Skip key validation and assume that used keys are always fully trusted. You generally won&#8217;t use this unless you are using some external validation scheme. This option also suppresses the &quot;[uncertain]&quot; tag printed with signature checks when there is no evidence that the user ID is bound to the key. </dd>
<dt><code>auto</code></dt>
<dd> Select the trust model depending on whatever the internal trust database says. This is the default model if such a database already exists.</dd></dl>
</dl>
<dt><code>&#8211;auto-key-locate parameters</code></dt>
<dd>
</dd><dt><code>&#8211;no-auto-key-locate</code></dt>
<dd> GnuPG can automatically locate and retrieve keys as needed using this option. This happens when encrypting to an email address (in the &quot;user [at] example.com&quot; form), and there are no user [at] example.com keys on the local keyring. This option takes any number of the following mechanisms, in the order they are to be tried: </dd>
<dl>
<dl>
<dt><code>cert</code></dt>
<dd> Locate a key using DNS CERT, as specified in rfc4398. </dd>
<dt><code>pka</code></dt>
<dd> Locate a key using DNS PKA. </dd>
<dt><code>ldap</code></dt>
<dd> Using DNS Service Discovery, check the domain in question for any LDAP keyservers to use. If this fails, attempt to locate the key using the PGP Universal method of checking &#8216;<a href="ldap://keys.(thedomain)'.">ldap://keys.(thedomain)&#8217;.</a> </dd>
<dt><code>keyserver</code></dt>
<dd> Locate a key using whatever keyserver is defined using the <code>&#8211;keyserver</code> option. </dd>
<dt><code>keyserver-URL</code></dt>
<dd> In addition, a keyserver URL as used in the <code>&#8211;keyserver</code> option may be used here to query that particular keyserver. </dd>
<dt><code>local</code></dt>
<dd> Locate the key using the local keyrings. This mechanism allows to select the order a local key lookup is done. Thus using &#8216;&#8211;auto-key-locate local&#8217; is identical to <code>&#8211;no-auto-key-locate</code>. </dd>
<dt><code>nodefault</code></dt>
<dd> This flag disables the standard local key lookup, done before any of the mechanisms defined by the <code>&#8211;auto-key-locate</code> are tried. The position of this mechanism in the list does not matter. It is not required if <code>local</code> is also used. </dd>
</dl>
</dl>
<dt><code>&#8211;keyid-format short|0xshort|long|0xlong</code></dt>
<dd> Select how to display key IDs. &quot;short&quot; is the traditional 8-character key ID. &quot;long&quot; is the more accurate (but less convenient) 16-character key ID. Add an &quot;0x&quot; to either to include an &quot;0x&quot; at the beginning of the key ID, as in 0x99242560. Note that this option is ignored if the option &#8211;with-colons is used. </dd>
<dt><code>&#8211;keyserver name</code></dt>
<dd> Use <code>name</code> as your keyserver. This is the server that <code>&#8211;recv-keys</code>, <code>&#8211;send-keys</code>, and <code>&#8211;search-keys</code> will communicate with to receive keys from, send keys to, and search for keys on. The format of the <code>name</code> is a URI: `scheme:[//]keyservername[:port]&#8217; The scheme is the type of keyserver: &quot;hkp&quot; for the HTTP (or compatible) keyservers, &quot;ldap&quot; for the LDAP keyservers, or &quot;mailto&quot; for the Graff email keyserver. Note that your particular installation of GnuPG may have other keyserver types available as well. Keyserver schemes are case-insensitive. After the keyserver name, optional keyserver configuration options may be provided. These are the same as the global <code>&#8211;keyserver-options</code> from below, but apply only to this particular keyserver. </dd>
<p> Most keyservers synchronize with each other, so there is generally no need to send keys to more than one server. The keyserver <code><a href="hkp://keys.gnupg.net">hkp://keys.gnupg.net</a></code> uses round robin DNS to give a different keyserver each time you use it. </p>
<dt><code>&#8211;keyserver-options name=value1 </code></dt>
<dd> This is a space or comma delimited string that gives options for the keyserver. Options can be prefixed with a `no-&#8216; to give the opposite meaning. Valid import-options or export-options may be used here as well to apply to importing (<code>&#8211;recv-key</code>) or exporting (<code>&#8211;send-key</code>) a key from a keyserver. While not all options are available for all keyserver types, some common options are: </dd>
<dl>
<dl>
<dt><code>include-revoked</code></dt>
<dd> When searching for a key with <code>&#8211;search-keys</code>, include keys that are marked on the keyserver as revoked. Note that not all keyservers differentiate between revoked and unrevoked keys, and for such keyservers this option is meaningless. Note also that most keyservers do not have cryptographic verification of key revocations, and so turning this option off may result in skipping keys that are incorrectly marked as revoked. </dd>
<dt><code>include-disabled</code></dt>
<dd> When searching for a key with <code>&#8211;search-keys</code>, include keys that are marked on the keyserver as disabled. Note that this option is not used with HKP keyservers. </dd>
<dt><code>auto-key-retrieve</code></dt>
<dd> This option enables the automatic retrieving of keys from a keyserver when verifying signatures made by keys that are not on the local keyring. </dd>
<p> Note that this option makes a &quot;web bug&quot; like behavior possible. Keyserver operators can see which keys you request, so by sending you a message signed by a brand new key (which you naturally will not have on your local keyring), the operator can tell both your IP address and the time when you verified the signature. </p>
<dt><code>honor-keyserver-url</code></dt>
<dd> When using <code>&#8211;refresh-keys</code>, if the key in question has a preferred keyserver URL, then use that preferred keyserver to refresh the key from. In addition, if auto-key-retrieve is set, and the signature being verified has a preferred keyserver URL, then use that preferred keyserver to fetch the key from. Defaults to yes. </dd>
<dt><code>honor-pka-record</code></dt>
<dd> If auto-key-retrieve is set, and the signature being verified has a PKA record, then use the PKA information to fetch the key. Defaults to yes. </dd>
<dt><code>include-subkeys</code></dt>
<dd> When receiving a key, include subkeys as potential targets. Note that this option is not used with HKP keyservers, as they do not support retrieving keys by subkey id. </dd>
<dt><code>use-temp-files</code></dt>
<dd> On most Unix-like platforms, GnuPG communicates with the keyserver helper program via pipes, which is the most efficient method. This option forces GnuPG to use temporary files to communicate. On some platforms (such as Win32 and RISC OS), this option is always enabled. </dd>
<dt><code>keep-temp-files</code></dt>
<dd> If using `use-temp-files&#8217;, do not delete the temp files after using them. This option is useful to learn the keyserver communication protocol by reading the temporary files. </dd>
<dt><code>verbose</code></dt>
<dd> Tell the keyserver helper program to be more verbose. This option can be repeated multiple times to increase the verbosity level. </dd>
<dt><code>timeout</code></dt>
<dd> Tell the keyserver helper program how long (in seconds) to try and perform a keyserver action before giving up. Note that performing multiple actions at the same time uses this timeout value per action. For example, when retrieving multiple keys via <code>&#8211;recv-keys</code>, the timeout applies separately to each key retrieval, and not to the <code>&#8211;recv-keys</code> command as a whole. Defaults to 30 seconds. </dd>
<dt><code>http-proxy=value</code></dt>
<dd> Set the proxy to use for HTTP and HKP keyservers. This overrides the &quot;http_proxy&quot; environment variable, if any. </dd>
<dt><code>max-cert-size</code></dt>
<dd> When retrieving a key via DNS CERT, only accept keys up to this size. Defaults to 16384 bytes. </dd>
<dt><code>debug</code></dt>
<dd> Turn on debug output in the keyserver helper program. Note that the details of debug output depends on which keyserver helper program is being used, and in turn, on any libraries that the keyserver helper program uses internally (libcurl, openldap, etc). </dd>
<dt><code>check-cert</code></dt>
<dd> Enable certificate checking if the keyserver presents one (for hkps or ldaps). Defaults to on. </dd>
<dt><code>ca-cert-file</code></dt>
<dd> Provide a certificate store to override the system default. Only necessary if check-cert is enabled, and the keyserver is using a certificate that is not present in a system default certificate list. </dd>
<p> Note that depending on the SSL library that the keyserver helper is built with, this may actually be a directory or a file.</dl>
</dl>
<dt><code>&#8211;completes-needed n</code></dt>
<dd> Number of completely trusted users to introduce a new key signer (defaults to 1). </dd>
<dt><code>&#8211;marginals-needed n</code></dt>
<dd> Number of marginally trusted users to introduce a new key signer (defaults to 3) </dd>
<dt><code>&#8211;max-cert-depth n</code></dt>
<dd> Maximum depth of a certification chain (default is 5). </dd>
<dt><code>&#8211;simple-sk-checksum</code></dt>
<dd> Secret keys are integrity protected by using a SHA-1 checksum. This method is part of the upcoming enhanced OpenPGP specification but GnuPG already uses it as a countermeasure against certain attacks. Old applications don&#8217;t understand this new format, so this option may be used to switch back to the old behaviour. Using this option bears a security risk. Note that using this option only takes effect when the secret key is encrypted &#8211; the simplest way to make this happen is to change the passphrase on the key (even changing it to the same value is acceptable). </dd>
<dt><code>&#8211;no-sig-cache</code></dt>
<dd> Do not cache the verification status of key signatures. Caching gives a much better performance in key listings. However, if you suspect that your public keyring is not save against write modifications, you can use this option to disable the caching. It probably does not make sense to disable it because all kind of damage can be done if someone else has write access to your public keyring. </dd>
<dt><code>&#8211;no-sig-create-check</code></dt>
<dd> GnuPG normally verifies each signature right after creation to protect against bugs and hardware malfunctions which could leak out bits from the secret key. This extra verification needs some time (about 115% for DSA keys), and so this option can be used to disable it. However, due to the fact that the signature creation needs manual interaction, this performance penalty does not matter in most settings. </dd>
<dt><code>&#8211;auto-check-trustdb</code></dt>
<dd>
</dd><dt><code>&#8211;no-auto-check-trustdb</code></dt>
<dd> If GnuPG feels that its information about the Web of Trust has to be updated, it automatically runs the <code>&#8211;check-trustdb</code> command internally. This may be a time consuming process. <code>&#8211;no-auto-check-trustdb</code> disables this option. </dd>
<dt><code>&#8211;use-agent</code></dt>
<dd>
</dd><dt><code>&#8211;no-use-agent</code></dt>
<dd> This is dummy option. <code>gpg2</code> always requires the agent. </dd>
<dt><code>&#8211;gpg-agent-info</code></dt>
<dd> This is dummy option. It has no effect when used with <code>gpg2</code>. </dd>
<dt><code>&#8211;lock-once</code></dt>
<dd> Lock the databases the first time a lock is requested and do not release the lock until the process terminates. </dd>
<dt><code>&#8211;lock-multiple</code></dt>
<dd> Release the locks every time a lock is no longer needed. Use this to override a previous <code>&#8211;lock-once</code> from a config file. </dd>
<dt><code>&#8211;lock-never</code></dt>
<dd> Disable locking entirely. This option should be used only in very special environments, where it can be assured that only one process is accessing those files. A bootable floppy with a stand-alone encryption system will probably use this. Improper usage of this option may lead to data and key corruption. </dd>
<dt><code>&#8211;exit-on-status-write-error</code></dt>
<dd> This option will cause write errors on the status FD to immediately terminate the process. That should in fact be the default but it never worked this way and thus we need an option to enable this, so that the change won&#8217;t break applications which close their end of a status fd connected pipe too early. Using this option along with <code>&#8211;enable-progress-filter</code> may be used to cleanly cancel long running gpg operations. </dd>
<dt><code>&#8211;limit-card-insert-tries n</code></dt>
<dd> With <code>n</code> greater than 0 the number of prompts asking to insert a smartcard gets limited to N-1. Thus with a value of 1 gpg won&#8217;t at all ask to insert a card if none has been inserted at startup. This option is useful in the configuration file in case an application does not know about the smartcard support and waits ad infinitum for an inserted card. </dd>
<dt><code>&#8211;no-random-seed-file</code></dt>
<dd> GnuPG uses a file to store its internal random pool over invocations. This makes random generation faster; however sometimes write operations are not desired. This option can be used to achieve that with the cost of slower random generation. </dd>
<dt><code>&#8211;no-greeting</code></dt>
<dd> Suppress the initial copyright message. </dd>
<dt><code>&#8211;no-secmem-warning</code></dt>
<dd> Suppress the warning about &quot;using insecure memory&quot;. </dd>
<dt><code>&#8211;no-permission-warning</code></dt>
<dd> Suppress the warning about unsafe file and home directory (<code>&#8211;homedir</code>) permissions. Note that the permission checks that GnuPG performs are not intended to be authoritative, but rather they simply warn about certain common permission problems. Do not assume that the lack of a warning means that your system is secure. </dd>
<p> Note that the warning for unsafe <code>&#8211;homedir</code> permissions cannot be suppressed in the gpg.conf file, as this would allow an attacker to place an unsafe gpg.conf file in place, and use this file to suppress warnings about itself. The <code>&#8211;homedir</code> permissions warning may only be suppressed on the command line. </p>
<dt><code>&#8211;no-mdc-warning</code></dt>
<dd> Suppress the warning about missing MDC integrity protection. </dd>
<dt><code>&#8211;require-secmem</code></dt>
<dd>
</dd><dt><code>&#8211;no-require-secmem</code></dt>
<dd> Refuse to run if GnuPG cannot get secure memory. Defaults to no (i.e. run, but give a warning). </dd>
<dt><code>&#8211;require-cross-certification</code></dt>
<dd>
</dd><dt><code>&#8211;no-require-cross-certification</code></dt>
<dd> When verifying a signature made from a subkey, ensure that the cross certification &quot;back signature&quot; on the subkey is present and valid. This protects against a subtle attack against subkeys that can sign. Defaults to <code>&#8211;require-cross-certification</code> for <code>gpg2</code>. </dd>
<dt><code>&#8211;expert</code></dt>
<dd>
</dd><dt><code>&#8211;no-expert</code></dt>
<dd> Allow the user to do certain nonsensical or &quot;silly&quot; things like signing an expired or revoked key, or certain potentially incompatible things like generating unusual key types. This also disables certain warning messages about potentially incompatible actions. As the name implies, this option is for experts only. If you don&#8217;t fully understand the implications of what it allows you to do, leave this off. <code>&#8211;no-expert</code> disables this option. </dd>
</dl>
<h3>Key related options</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>&#8211;recipient </code><i>name</i></dt>
<dd>
</dd><dt><code>-r</code></dt>
<dd> Encrypt for user id <i>name</i>. If this option or <code>&#8211;hidden-recipient</code> is not specified, GnuPG asks for the user-id unless <code>&#8211;default-recipient</code> is given. </dd>
<dt><code>&#8211;hidden-recipient </code><i>name</i></dt>
<dd>
</dd><dt><code>-R</code></dt>
<dd> Encrypt for user ID <i>name</i>, but hide the key ID of this user&#8217;s key. This option helps to hide the receiver of the message and is a limited countermeasure against traffic analysis. If this option or <code>&#8211;recipient</code> is not specified, GnuPG asks for the user ID unless <code>&#8211;default-recipient</code> is given. </dd>
<dt><code>&#8211;encrypt-to name</code></dt>
<dd> Same as <code>&#8211;recipient</code> but this one is intended for use in the options file and may be used with your own user-id as an &quot;encrypt-to-self&quot;. These keys are only used when there are other recipients given either by use of <code>&#8211;recipient</code> or by the asked user id. No trust checking is performed for these user ids and even disabled keys can be used. </dd>
<dt><code>&#8211;hidden-encrypt-to name</code></dt>
<dd> Same as <code>&#8211;hidden-recipient</code> but this one is intended for use in the options file and may be used with your own user-id as a hidden &quot;encrypt-to-self&quot;. These keys are only used when there are other recipients given either by use of <code>&#8211;recipient</code> or by the asked user id. No trust checking is performed for these user ids and even disabled keys can be used. </dd>
<dt><code>&#8211;no-encrypt-to</code></dt>
<dd> Disable the use of all <code>&#8211;encrypt-to</code> and <code>&#8211;hidden-encrypt-to</code> keys. </dd>
<dt><code>&#8211;group name=value1 </code></dt>
<dd> Sets up a named group, which is similar to aliases in email programs. Any time the group name is a recipient (<code>-r</code> or <code>&#8211;recipient</code>), it will be expanded to the values specified. Multiple groups with the same name are automatically merged into a single group. </dd>
<p> The values are <code>key IDs</code> or fingerprints, but any key description is accepted. Note that a value with spaces in it will be treated as two different values. Note also there is only one level of expansion &#8212; you cannot make an group that points to another group. When used from the command line, it may be necessary to quote the argument to this option to prevent the shell from treating it as multiple arguments. </p>
<dt><code>&#8211;ungroup name</code></dt>
<dd> Remove a given entry from the <code>&#8211;group</code> list. </dd>
<dt><code>&#8211;no-groups</code></dt>
<dd> Remove all entries from the <code>&#8211;group</code> list. </dd>
<dt><code>&#8211;local-user </code><i>name</i></dt>
<dd>
</dd><dt><code>-u</code></dt>
<dd> Use <i>name</i> as the key to sign with. Note that this option overrides <code>&#8211;default-key</code>. </dd>
<dt><code>&#8211;try-secret-key </code><i>name</i></dt>
<dd> For hidden recipients GPG needs to know the keys to use for trial decryption. The key set with <code>&#8211;default-key</code> is always tried first, but this is often not sufficient. This option allows to set more keys to be used for trial decryption. Although any valid user-id specification may be used for <i>name</i> it makes sense to use at least the long keyid to avoid ambiguities. Note that gpg-agent might pop up a pinentry for a lot keys to do the trial decryption. If you want to stop all further trial decryption you may use close-window button instead of the cancel button. </dd>
<dt><code>&#8211;try-all-secrets</code></dt>
<dd> Don&#8217;t look at the key ID as stored in the message but try all secret keys in turn to find the right decryption key. This option forces the behaviour as used by anonymous recipients (created by using <code>&#8211;throw-keyids</code> or <code>&#8211;hidden-recipient</code>) and might come handy in case where an encrypted message contains a bogus key ID. </dd>
<dt><code>&#8211;skip-hidden-recipients</code></dt>
<dd>
</dd><dt><code>&#8211;no-skip-hidden-recipients</code></dt>
<dd> During decryption skip all anonymous recipients. This option helps in the case that people use the hidden recipients feature to hide there own encrypt-to key from others. If oneself has many secret keys this may lead to a major annoyance because all keys are tried in turn to decrypt soemthing which was not really intended for it. The drawback of this option is that it is currently not possible to decrypt a message which includes real anonymous recipients. </dd>
</dl>
<h3>Input and Output</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>&#8211;armor</code></dt>
<dd>
</dd><dt><code>-a</code></dt>
<dd> Create ASCII armored output. The default is to create the binary OpenPGP format. </dd>
<dt><code>&#8211;no-armor</code></dt>
<dd> Assume the input data is not in ASCII armored format. </dd>
<dt><code>&#8211;output </code><i>file</i></dt>
<dd>
</dd><dt><code>-o </code><i>file</i></dt>
<dd> Write output to <i>file</i>. </dd>
<dt><code>&#8211;max-output n</code></dt>
<dd> This option sets a limit on the number of bytes that will be generated when processing a file. Since OpenPGP supports various levels of compression, it is possible that the plaintext of a given message may be significantly larger than the original OpenPGP message. While GnuPG works properly with such messages, there is often a desire to set a maximum file size that will be generated before processing is forced to stop by the OS limits. Defaults to 0, which means &quot;no limit&quot;. </dd>
<dt><code>&#8211;import-options parameters</code></dt>
<dd> This is a space or comma delimited string that gives options for importing keys. Options can be prepended with a `no-&#8216; to give the opposite meaning. The options are: </dd>
<dl>
<dl>
<dt><code>import-local-sigs</code></dt>
<dd> Allow importing key signatures marked as &quot;local&quot;. This is not generally useful unless a shared keyring scheme is being used. Defaults to no. </dd>
<dt><code>repair-pks-subkey-bug</code></dt>
<dd> During import, attempt to repair the damage caused by the PKS keyserver bug (pre version 0.9.6) that mangles keys with multiple subkeys. Note that this cannot completely repair the damaged key as some crucial data is removed by the keyserver, but it does at least give you back one subkey. Defaults to no for regular <code>&#8211;import</code> and to yes for keyserver <code>&#8211;recv-keys</code>. </dd>
<dt><code>merge-only</code></dt>
<dd> During import, allow key updates to existing keys, but do not allow any new keys to be imported. Defaults to no. </dd>
<dt><code>import-clean</code></dt>
<dd> After import, compact (remove all signatures except the self-signature) any user IDs from the new key that are not usable. Then, remove any signatures from the new key that are not usable. This includes signatures that were issued by keys that are not present on the keyring. This option is the same as running the <code>&#8211;edit-key</code> command &quot;clean&quot; after import. Defaults to no. </dd>
<dt><code>import-minimal</code></dt>
<dd> Import the smallest key possible. This removes all signatures except the most recent self-signature on each user ID. This option is the same as running the <code>&#8211;edit-key</code> command &quot;minimize&quot; after import. Defaults to no.</dd></dl>
</dl>
<dt><code>&#8211;export-options parameters</code></dt>
<dd> This is a space or comma delimited string that gives options for exporting keys. Options can be prepended with a `no-&#8216; to give the opposite meaning. The options are: </dd>
<dl>
<dl>
<dt><code>export-local-sigs</code></dt>
<dd> Allow exporting key signatures marked as &quot;local&quot;. This is not generally useful unless a shared keyring scheme is being used. Defaults to no. </dd>
<dt><code>export-attributes</code></dt>
<dd> Include attribute user IDs (photo IDs) while exporting. This is useful to export keys if they are going to be used by an OpenPGP program that does not accept attribute user IDs. Defaults to yes. </dd>
<dt><code>export-sensitive-revkeys</code></dt>
<dd> Include designated revoker information that was marked as &quot;sensitive&quot;. Defaults to no. </dd>
<dt><code>export-reset-subkey-passwd</code></dt>
<dd> When using the <code>&#8211;export-secret-subkeys</code> command, this option resets the passphrases for all exported subkeys to empty. This is useful when the exported subkey is to be used on an unattended machine where a passphrase doesn&#8217;t necessarily make sense. Defaults to no. </dd>
<dt><code>export-clean</code></dt>
<dd> Compact (remove all signatures from) user IDs on the key being exported if the user IDs are not usable. Also, do not export any signatures that are not usable. This includes signatures that were issued by keys that are not present on the keyring. This option is the same as running the <code>&#8211;edit-key</code> command &quot;clean&quot; before export except that the local copy of the key is not modified. Defaults to no. </dd>
<dt><code>export-minimal</code></dt>
<dd> Export the smallest key possible. This removes all signatures except the most recent self-signature on each user ID. This option is the same as running the <code>&#8211;edit-key</code> command &quot;minimize&quot; before export except that the local copy of the key is not modified. Defaults to no.</dd></dl>
</dl>
<dt><code>&#8211;with-colons</code></dt>
<dd> Print key listings delimited by colons. Note that the output will be encoded in UTF-8 regardless of any <code>&#8211;display-charset</code> setting. This format is useful when GnuPG is called from scripts and other programs as it is easily machine parsed. The details of this format are documented in the file &#8216;<i>doc/DETAILS</i>&#8216;, which is included in the GnuPG source distribution. </dd>
<dt><code>&#8211;fixed-list-mode</code></dt>
<dd> Do not merge primary user ID and primary key in <code>&#8211;with-colon</code> listing mode and print all timestamps as seconds since 1970-01-01. Since GnuPG 2.0.10, this mode is always used and thus this option is obsolete; it does not harm to use it though. </dd>
<dt><code>&#8211;with-fingerprint</code></dt>
<dd> Same as the command <code>&#8211;fingerprint</code> but changes only the format of the output and may be used together with another command. </dd>
<dt><code>&#8211;with-keygrip</code></dt>
<dd> Include the keygrip in the key listings. </dd>
</dl>
<h3>OpenPGP protocol specific options.</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>-t, &#8211;textmode</code></dt>
<dd>
</dd><dt><code>&#8211;no-textmode</code></dt>
<dd> Treat input files as text and store them in the OpenPGP canonical text form with standard &quot;CRLF&quot; line endings. This also sets the necessary flags to inform the recipient that the encrypted or signed data is text and may need its line endings converted back to whatever the local system uses. This option is useful when communicating between two platforms that have different line ending conventions (UNIX-like to Mac, Mac to Windows, etc). <code>&#8211;no-textmode</code> disables this option, and is the default. </dd>
<dt><code>&#8211;force-v3-sigs</code></dt>
<dd>
</dd><dt><code>&#8211;no-force-v3-sigs</code></dt>
<dd> OpenPGP states that an implementation should generate v4 signatures but PGP versions 5 through 7 only recognize v4 signatures on key material. This option forces v3 signatures for signatures on data. Note that this option implies <code>&#8211;no-ask-sig-expire</code>, and unsets <code>&#8211;sig-policy-url</code>, <code>&#8211;sig-notation</code>, and <code>&#8211;sig-keyserver-url</code>, as these features cannot be used with v3 signatures. <code>&#8211;no-force-v3-sigs</code> disables this option. Defaults to no. </dd>
<dt><code>&#8211;force-v4-certs</code></dt>
<dd>
</dd><dt><code>&#8211;no-force-v4-certs</code></dt>
<dd> Always use v4 key signatures even on v3 keys. This option also changes the default hash algorithm for v3 RSA keys from MD5 to SHA-1. <code>&#8211;no-force-v4-certs</code> disables this option. </dd>
<dt><code>&#8211;force-mdc</code></dt>
<dd> Force the use of encryption with a modification detection code. This is always used with the newer ciphers (those with a blocksize greater than 64 bits), or if all of the recipient keys indicate MDC support in their feature flags. </dd>
<dt><code>&#8211;disable-mdc</code></dt>
<dd> Disable the use of the modification detection code. Note that by using this option, the encrypted message becomes vulnerable to a message modification attack. </dd>
<dt><code>&#8211;personal-cipher-preferences string</code></dt>
<dd> Set the list of personal cipher preferences to <code>string</code>. Use <code>gpg2 &#8211;version</code> to get a list of available algorithms, and use <code>none</code> to set no preference at all. This allows the user to safely override the algorithm chosen by the recipient key preferences, as GPG will only select an algorithm that is usable by all recipients. The most highly ranked cipher in this list is also used for the <code>&#8211;symmetric</code> encryption command. </dd>
<dt><code>&#8211;personal-digest-preferences string</code></dt>
<dd> Set the list of personal digest preferences to <code>string</code>. Use <code>gpg2 &#8211;version</code> to get a list of available algorithms, and use <code>none</code> to set no preference at all. This allows the user to safely override the algorithm chosen by the recipient key preferences, as GPG will only select an algorithm that is usable by all recipients. The most highly ranked digest algorithm in this list is also used when signing without encryption (e.g. <code>&#8211;clearsign</code> or <code>&#8211;sign</code>). </dd>
<dt><code>&#8211;personal-compress-preferences string</code></dt>
<dd> Set the list of personal compression preferences to <code>string</code>. Use <code>gpg2 &#8211;version</code> to get a list of available algorithms, and use <code>none</code> to set no preference at all. This allows the user to safely override the algorithm chosen by the recipient key preferences, as GPG will only select an algorithm that is usable by all recipients. The most highly ranked compression algorithm in this list is also used when there are no recipient keys to consider (e.g. <code>&#8211;symmetric</code>). </dd>
<dt><code>&#8211;s2k-cipher-algo name</code></dt>
<dd> Use <code>name</code> as the cipher algorithm used to protect secret keys. The default cipher is CAST5. This cipher is also used for conventional encryption if <code>&#8211;personal-cipher-preferences</code> and <code>&#8211;cipher-algo</code> is not given. </dd>
<dt><code>&#8211;s2k-digest-algo name</code></dt>
<dd> Use <code>name</code> as the digest algorithm used to mangle the passphrases. The default algorithm is SHA-1. </dd>
<dt><code>&#8211;s2k-mode n</code></dt>
<dd> Selects how passphrases are mangled. If <code>n</code> is 0 a plain passphrase (which is not recommended) will be used, a 1 adds a salt to the passphrase and a 3 (the default) iterates the whole process a number of times (see &#8211;s2k-count). Unless <code>&#8211;rfc1991</code> is used, this mode is also used for conventional encryption. </dd>
<dt><code>&#8211;s2k-count n</code></dt>
<dd> Specify how many times the passphrase mangling is repeated. This value may range between 1024 and 65011712 inclusive. The default is inquired from gpg-agent. Note that not all values in the 1024-65011712 range are legal and if an illegal value is selected, GnuPG will round up to the nearest legal value. This option is only meaningful if <code>&#8211;s2k-mode</code> is 3. </dd>
</dl>
<h3>Compliance options</h3>
<p> &nbsp;<wbr> </p>
<p> These options control what GnuPG is compliant to. Only one of these options may be active at a time. Note that the default setting of this is nearly always the correct one. See the INTEROPERABILITY WITH OTHER OPENPGP PROGRAMS section below before using one of these options. </p>
<dl>
<dt><code>&#8211;gnupg</code></dt>
<dd> Use standard GnuPG behavior. This is essentially OpenPGP behavior (see <code>&#8211;openpgp</code>), but with some additional workarounds for common compatibility problems in different versions of PGP. This is the default option, so it is not generally needed, but it may be useful to override a different compliance option in the gpg.conf file. </dd>
<dt><code>&#8211;openpgp</code></dt>
<dd> Reset all packet, cipher and digest options to strict OpenPGP behavior. Use this option to reset all previous options like <code>&#8211;s2k-*</code>, <code>&#8211;cipher-algo</code>, <code>&#8211;digest-algo</code> and <code>&#8211;compress-algo</code> to OpenPGP compliant values. All PGP workarounds are disabled. </dd>
<dt><code>&#8211;rfc4880</code></dt>
<dd> Reset all packet, cipher and digest options to strict RFC-4880 behavior. Note that this is currently the same thing as <code>&#8211;openpgp</code>. </dd>
<dt><code>&#8211;rfc2440</code></dt>
<dd> Reset all packet, cipher and digest options to strict RFC-2440 behavior. </dd>
<dt><code>&#8211;rfc1991</code></dt>
<dd> Try to be more RFC-1991 (PGP 2.x) compliant. </dd>
<dt><code>&#8211;pgp2</code></dt>
<dd> Set up all options to be as PGP 2.x compliant as possible, and warn if an action is taken (e.g. encrypting to a non-RSA key) that will create a message that PGP 2.x will not be able to handle. Note that `PGP 2.x&#8217; here means `MIT PGP 2.6.2&#8242;. There are other versions of PGP 2.x available, but the MIT release is a good common baseline. </dd>
<p> This option implies <code>&#8211;rfc1991 &#8211;disable-mdc &#8211;no-force-v4-certs &#8211;escape-from-lines &#8211;force-v3-sigs &#8211;cipher-algo IDEA &#8211;digest-algo MD5 &#8211;compress-algo ZIP</code>. It also disables <code>&#8211;textmode</code> when encrypting. </p>
<dt><code>&#8211;pgp6</code></dt>
<dd> Set up all options to be as PGP 6 compliant as possible. This restricts you to the ciphers IDEA (if the IDEA plugin is installed), 3DES, and CAST5, the hashes MD5, SHA1 and RIPEMD160, and the compression algorithms none and ZIP. This also disables &#8211;throw-keyids, and making signatures with signing subkeys as PGP 6 does not understand signatures made by signing subkeys. </dd>
<p> This option implies <code>&#8211;disable-mdc &#8211;escape-from-lines &#8211;force-v3-sigs</code>. </p>
<dt><code>&#8211;pgp7</code></dt>
<dd> Set up all options to be as PGP 7 compliant as possible. This is identical to <code>&#8211;pgp6</code> except that MDCs are not disabled, and the list of allowable ciphers is expanded to add AES128, AES192, AES256, and TWOFISH. </dd>
<dt><code>&#8211;pgp8</code></dt>
<dd> Set up all options to be as PGP 8 compliant as possible. PGP 8 is a lot closer to the OpenPGP standard than previous versions of PGP, so all this does is disable <code>&#8211;throw-keyids</code> and set <code>&#8211;escape-from-lines</code>. All algorithms are allowed except for the SHA224, SHA384, and SHA512 digests. </dd>
</dl>
<h3>Doing things one usually doesn&#8217;t want to do.</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;dry-run</code></dt>
<dd> Don&#8217;t make any changes (this is not completely implemented). </dd>
<dt><code>&#8211;list-only</code></dt>
<dd> Changes the behaviour of some commands. This is like <code>&#8211;dry-run</code> but different in some cases. The semantic of this command may be extended in the future. Currently it only skips the actual decryption pass and therefore enables a fast listing of the encryption keys. </dd>
<dt><code>-i</code></dt>
<dd>
</dd><dt><code>&#8211;interactive</code></dt>
<dd> Prompt before overwriting any files. </dd>
<dt><code>&#8211;debug-level </code><i>level</i></dt>
<dd> Select the debug level for investigating problems. <i>level</i> may be a numeric value or by a keyword: </dd>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> No debugging at all. A value of less than 1 may be used instead of the keyword.</dd>
<dt><code>basic</code></dt>
<dd> Some basic debug messages. A value between 1 and 2 may be used instead of the keyword.</dd>
<dt><code>advanced</code></dt>
<dd> More verbose debug messages. A value between 3 and 5 may be used instead of the keyword.</dd>
<dt><code>expert</code></dt>
<dd> Even more detailed messages. A value between 6 and 8 may be used instead of the keyword.</dd>
<dt><code>guru</code></dt>
<dd> All of the debug messages you can get. A value greater than 8 may be used instead of the keyword. The creation of hash tracing files is only enabled if the keyword is used.</dd></dl>
</dl>
<p> How these messages are mapped to the actual debugging flags is not specified and may change with newer releases of this program. They are however carefully selected to best aid in debugging. </p>
<dt><code>&#8211;debug </code><i>flags</i></dt>
<dd> Set debugging flags. All flags are or-ed and <i>flags</i> may be given in C syntax (e.g. 0x0042). </dd>
<dt><code>&#8211;debug-all</code></dt>
<dd> Set all useful debugging flags. </dd>
<dt><code>&#8211;faked-system-time </code><i>epoch</i></dt>
<dd> This option is only useful for testing; it sets the system time back or forth to <i>epoch</i> which is the number of seconds elapsed since the year 1970. Alternatively <i>epoch</i> may be given as a full ISO time string (e.g. &quot;20070924T154812&quot;). </dd>
<dt><code>&#8211;enable-progress-filter</code></dt>
<dd> Enable certain PROGRESS status outputs. This option allows frontends to display a progress indicator while gpg is processing larger files. There is a slight performance overhead using it. </dd>
<dt><code>&#8211;status-fd n</code></dt>
<dd> Write special status strings to the file descriptor <code>n</code>. See the file DETAILS in the documentation for a listing of them. </dd>
<dt><code>&#8211;status-file file</code></dt>
<dd> Same as <code>&#8211;status-fd</code>, except the status data is written to file <code>file</code>. </dd>
<dt><code>&#8211;logger-fd n</code></dt>
<dd> Write log output to file descriptor <code>n</code> and not to STDERR. </dd>
<dt><code>&#8211;log-file file</code></dt>
<dd>
</dd><dt><code>&#8211;logger-file file</code></dt>
<dd> Same as <code>&#8211;logger-fd</code>, except the logger data is written to file <code>file</code>. Note that <code>&#8211;log-file</code> is only implemented for GnuPG-2. </dd>
<dt><code>&#8211;attribute-fd n</code></dt>
<dd> Write attribute subpackets to the file descriptor <code>n</code>. This is most useful for use with <code>&#8211;status-fd</code>, since the status messages are needed to separate out the various subpackets from the stream delivered to the file descriptor. </dd>
<dt><code>&#8211;attribute-file file</code></dt>
<dd> Same as <code>&#8211;attribute-fd</code>, except the attribute data is written to file <code>file</code>. </dd>
<dt><code>&#8211;comment string</code></dt>
<dd>
</dd><dt><code>&#8211;no-comments</code></dt>
<dd> Use <code>string</code> as a comment string in clear text signatures and ASCII armored messages or keys (see <code>&#8211;armor</code>). The default behavior is not to use a comment string. <code>&#8211;comment</code> may be repeated multiple times to get multiple comment strings. <code>&#8211;no-comments</code> removes all comments. It is a good idea to keep the length of a single comment below 60 characters to avoid problems with mail programs wrapping such lines. Note that comment lines, like all other header lines, are not protected by the signature. </dd>
<dt><code>&#8211;emit-version</code></dt>
<dd>
</dd><dt><code>&#8211;no-emit-version</code></dt>
<dd> Force inclusion of the version string in ASCII armored output. <code>&#8211;no-emit-version</code> disables this option. </dd>
<dt><code>&#8211;sig-notation name=value</code></dt>
<dd>
</dd><dt><code>&#8211;cert-notation name=value</code></dt>
<dd>
</dd><dt><code>-N, &#8211;set-notation name=value</code></dt>
<dd> Put the name value pair into the signature as notation data. <code>name</code> must consist only of printable characters or spaces, and must contain a &#8216;@&#8217; character in the form keyname [at] domain.example.com (substituting the appropriate keyname and domain name, of course). This is to help prevent pollution of the IETF reserved notation namespace. The <code>&#8211;expert</code> flag overrides the &#8216;@&#8217; check. <code>value</code> may be any printable string; it will be encoded in UTF8, so you should check that your <code>&#8211;display-charset</code> is set correctly. If you prefix <code>name</code> with an exclamation mark (!), the notation data will be flagged as critical (rfc4880:5.2.3.16). <code>&#8211;sig-notation</code> sets a notation for data signatures. <code>&#8211;cert-notation</code> sets a notation for key signatures (certifications). <code>&#8211;set-notation</code> sets both. </dd>
<p> There are special codes that may be used in notation names. &quot;%k&quot; will be expanded into the key ID of the key being signed, &quot;%K&quot; into the long key ID of the key being signed, &quot;%f&quot; into the fingerprint of the key being signed, &quot;%s&quot; into the key ID of the key making the signature, &quot;%S&quot; into the long key ID of the key making the signature, &quot;%g&quot; into the fingerprint of the key making the signature (which might be a subkey), &quot;%p&quot; into the fingerprint of the primary key of the key making the signature, &quot;%c&quot; into the signature count from the OpenPGP smartcard, and &quot;%%&quot; results in a single &quot;%&quot;. %k, %K, and %f are only meaningful when making a key signature (certification), and %c is only meaningful when using the OpenPGP smartcard. </p>
<dt><code>&#8211;sig-policy-url string</code></dt>
<dd>
</dd><dt><code>&#8211;cert-policy-url string</code></dt>
<dd>
</dd><dt><code>&#8211;set-policy-url string</code></dt>
<dd> Use <code>string</code> as a Policy URL for signatures (rfc4880:5.2.3.20). If you prefix it with an exclamation mark (!), the policy URL packet will be flagged as critical. <code>&#8211;sig-policy-url</code> sets a policy url for data signatures. <code>&#8211;cert-policy-url</code> sets a policy url for key signatures (certifications). <code>&#8211;set-policy-url</code> sets both. </dd>
<p> The same %-expandos used for notation data are available here as well. </p>
<dt><code>&#8211;sig-keyserver-url string</code></dt>
<dd> Use <code>string</code> as a preferred keyserver URL for data signatures. If you prefix it with an exclamation mark (!), the keyserver URL packet will be flagged as critical. </dd>
<p> The same %-expandos used for notation data are available here as well. </p>
<dt><code>&#8211;set-filename string</code></dt>
<dd> Use <code>string</code> as the filename which is stored inside messages. This overrides the default, which is to use the actual filename of the file being encrypted. </dd>
<dt><code>&#8211;for-your-eyes-only</code></dt>
<dd>
</dd><dt><code>&#8211;no-for-your-eyes-only</code></dt>
<dd> Set the `for your eyes only&#8217; flag in the message. This causes GnuPG to refuse to save the file unless the <code>&#8211;output</code> option is given, and PGP to use a &quot;secure viewer&quot; with a claimed Tempest-resistant font to display the message. This option overrides <code>&#8211;set-filename</code>. <code>&#8211;no-for-your-eyes-only</code> disables this option. </dd>
<dt><code>&#8211;use-embedded-filename</code></dt>
<dd>
</dd><dt><code>&#8211;no-use-embedded-filename</code></dt>
<dd> Try to create a file with a name as embedded in the data. This can be a dangerous option as it allows to overwrite files. Defaults to no. </dd>
<dt><code>&#8211;cipher-algo name</code></dt>
<dd> Use <code>name</code> as cipher algorithm. Running the program with the command <code>&#8211;version</code> yields a list of supported algorithms. If this is not used the cipher algorithm is selected from the preferences stored with the key. In general, you do not want to use this option as it allows you to violate the OpenPGP standard. <code>&#8211;personal-cipher-preferences</code> is the safe way to accomplish the same thing. </dd>
<dt><code>&#8211;digest-algo name</code></dt>
<dd> Use <code>name</code> as the message digest algorithm. Running the program with the command <code>&#8211;version</code> yields a list of supported algorithms. In general, you do not want to use this option as it allows you to violate the OpenPGP standard. <code>&#8211;personal-digest-preferences</code> is the safe way to accomplish the same thing. </dd>
<dt><code>&#8211;compress-algo name</code></dt>
<dd> Use compression algorithm <code>name</code>. &quot;zlib&quot; is RFC-1950 ZLIB compression. &quot;zip&quot; is RFC-1951 ZIP compression which is used by PGP. &quot;bzip2&quot; is a more modern compression scheme that can compress some things better than zip or zlib, but at the cost of more memory used during compression and decompression. &quot;uncompressed&quot; or &quot;none&quot; disables compression. If this option is not used, the default behavior is to examine the recipient key preferences to see which algorithms the recipient supports. If all else fails, ZIP is used for maximum compatibility. </dd>
<p> ZLIB may give better compression results than ZIP, as the compression window size is not limited to 8k. BZIP2 may give even better compression results than that, but will use a significantly larger amount of memory while compressing and decompressing. This may be significant in low memory situations. Note, however, that PGP (all versions) only supports ZIP compression. Using any algorithm other than ZIP or &quot;none&quot; will make the message unreadable with PGP. In general, you do not want to use this option as it allows you to violate the OpenPGP standard. <code>&#8211;personal-compress-preferences</code> is the safe way to accomplish the same thing. </p>
<dt><code>&#8211;cert-digest-algo name</code></dt>
<dd> Use <code>name</code> as the message digest algorithm used when signing a key. Running the program with the command <code>&#8211;version</code> yields a list of supported algorithms. Be aware that if you choose an algorithm that GnuPG supports but other OpenPGP implementations do not, then some users will not be able to use the key signatures you make, or quite possibly your entire key. </dd>
<dt><code>&#8211;disable-cipher-algo name</code></dt>
<dd> Never allow the use of <code>name</code> as cipher algorithm. The given name will not be checked so that a later loaded algorithm will still get disabled. </dd>
<dt><code>&#8211;disable-pubkey-algo name</code></dt>
<dd> Never allow the use of <code>name</code> as public key algorithm. The given name will not be checked so that a later loaded algorithm will still get disabled. </dd>
<dt><code>&#8211;throw-keyids</code></dt>
<dd>
</dd><dt><code>&#8211;no-throw-keyids</code></dt>
<dd> Do not put the recipient key IDs into encrypted messages. This helps to hide the receivers of the message and is a limited countermeasure against traffic analysis. ([Using a little social engineering anyone who is able to decrypt the message can check whether one of the other recipients is the one he suspects.]) On the receiving side, it may slow down the decryption process because all available secret keys must be tried. <code>&#8211;no-throw-keyids</code> disables this option. This option is essentially the same as using <code>&#8211;hidden-recipient</code> for all recipients. </dd>
<dt><code>&#8211;not-dash-escaped</code></dt>
<dd> This option changes the behavior of cleartext signatures so that they can be used for patch files. You should not send such an armored file via email because all spaces and line endings are hashed too. You can not use this option for data which has 5 dashes at the beginning of a line, patch files don&#8217;t have this. A special armor header line tells GnuPG about this cleartext signature option. </dd>
<dt><code>&#8211;escape-from-lines</code></dt>
<dd>
</dd><dt><code>&#8211;no-escape-from-lines</code></dt>
<dd> Because some mailers change lines starting with &quot;From &quot; to &quot;&gt;From &quot; it is good to handle such lines in a special way when creating cleartext signatures to prevent the mail system from breaking the signature. Note that all other PGP versions do it this way too. Enabled by default. <code>&#8211;no-escape-from-lines</code> disables this option. </dd>
<dt><code>&#8211;passphrase-repeat n</code></dt>
<dd> Specify how many times <code>gpg2</code> will request a new passphrase be repeated. This is useful for helping memorize a passphrase. Defaults to 1 repetition. </dd>
<dt><code>&#8211;passphrase-fd n</code></dt>
<dd> Read the passphrase from file descriptor <code>n</code>. Only the first line will be read from file descriptor <code>n</code>. If you use 0 for <code>n</code>, the passphrase will be read from STDIN. This can only be used if only one passphrase is supplied. Note that this passphrase is only used if the option <code>&#8211;batch</code> has also been given. This is different from <code>gpg</code>. </dd>
<dt><code>&#8211;passphrase-file file</code></dt>
<dd> Read the passphrase from file <code>file</code>. Only the first line will be read from file <code>file</code>. This can only be used if only one passphrase is supplied. Obviously, a passphrase stored in a file is of questionable security if other users can read this file. Don&#8217;t use this option if you can avoid it. Note that this passphrase is only used if the option <code>&#8211;batch</code> has also been given. This is different from <code>gpg</code>. </dd>
<dt><code>&#8211;passphrase string</code></dt>
<dd> Use <code>string</code> as the passphrase. This can only be used if only one passphrase is supplied. Obviously, this is of very questionable security on a multi-user system. Don&#8217;t use this option if you can avoid it. Note that this passphrase is only used if the option <code>&#8211;batch</code> has also been given. This is different from <code>gpg</code>. </dd>
<dt><code>&#8211;pinentry-mode mode</code></dt>
<dd> Set the pinentry mode to <code>mode</code>. Allowed values for <code>mode</code> are:</dd>
<dl>
<dl>
<dt><code>default</code></dt>
<dd> Use the default of the agent, which is <code>ask</code>.</dd>
<dt><code>ask</code></dt>
<dd> Force the use of the Pinentry.</dd>
<dt><code>cancel</code></dt>
<dd> Emulate use of Pinentry&#8217;s cancel button.</dd>
<dt><code>error</code></dt>
<dd> Return a Pinentry error (&#8220;No Pinentry&#8221;).</dd>
<dt><code>loopback</code></dt>
<dd> Redirect Pinentry queries to the caller. Note that in contrast to Pinentry the user is not prompted again if he enters a bad password.</dd></dl>
</dl>
<dt><code>&#8211;command-fd n</code></dt>
<dd> This is a replacement for the deprecated shared-memory IPC mode. If this option is enabled, user input on questions is not expected from the TTY but from the given file descriptor. It should be used together with <code>&#8211;status-fd</code>. See the file doc/DETAILS in the source distribution for details on how to use it. </dd>
<dt><code>&#8211;command-file file</code></dt>
<dd> Same as <code>&#8211;command-fd</code>, except the commands are read out of file <code>file</code> </dd>
<dt><code>&#8211;allow-non-selfsigned-uid</code></dt>
<dd>
</dd><dt><code>&#8211;no-allow-non-selfsigned-uid</code></dt>
<dd> Allow the import and use of keys with user IDs which are not self-signed. This is not recommended, as a non self-signed user ID is trivial to forge. <code>&#8211;no-allow-non-selfsigned-uid</code> disables. </dd>
<dt><code>&#8211;allow-freeform-uid</code></dt>
<dd> Disable all checks on the form of the user ID while generating a new one. This option should only be used in very special environments as it does not ensure the de-facto standard format of user IDs. </dd>
<dt><code>&#8211;ignore-time-conflict</code></dt>
<dd> GnuPG normally checks that the timestamps associated with keys and signatures have plausible values. However, sometimes a signature seems to be older than the key due to clock problems. This option makes these checks just a warning. See also <code>&#8211;ignore-valid-from</code> for timestamp issues on subkeys. </dd>
<dt><code>&#8211;ignore-valid-from</code></dt>
<dd> GnuPG normally does not select and use subkeys created in the future. This option allows the use of such keys and thus exhibits the pre-1.0.7 behaviour. You should not use this option unless there is some clock problem. See also <code>&#8211;ignore-time-conflict</code> for timestamp issues with signatures. </dd>
<dt><code>&#8211;ignore-crc-error</code></dt>
<dd> The ASCII armor used by OpenPGP is protected by a CRC checksum against transmission errors. Occasionally the CRC gets mangled somewhere on the transmission channel but the actual content (which is protected by the OpenPGP protocol anyway) is still okay. This option allows GnuPG to ignore CRC errors. </dd>
<dt><code>&#8211;ignore-mdc-error</code></dt>
<dd> This option changes a MDC integrity protection failure into a warning. This can be useful if a message is partially corrupt, but it is necessary to get as much data as possible out of the corrupt message. However, be aware that a MDC protection failure may also mean that the message was tampered with intentionally by an attacker. </dd>
<dt><code>&#8211;no-default-keyring</code></dt>
<dd> Do not add the default keyrings to the list of keyrings. Note that GnuPG will not operate without any keyrings, so if you use this option and do not provide alternate keyrings via <code>&#8211;keyring</code> or <code>&#8211;secret-keyring</code>, then GnuPG will still use the default public or secret keyrings. </dd>
<dt><code>&#8211;skip-verify</code></dt>
<dd> Skip the signature verification step. This may be used to make the decryption faster if the signature verification is not needed. </dd>
<dt><code>&#8211;with-key-data</code></dt>
<dd> Print key listings delimited by colons (like <code>&#8211;with-colons</code>) and print the public key data. </dd>
<dt><code>&#8211;fast-list-mode</code></dt>
<dd> Changes the output of the list commands to work faster; this is achieved by leaving some parts empty. Some applications don&#8217;t need the user ID and the trust information given in the listings. By using this options they can get a faster listing. The exact behaviour of this option may change in future versions. If you are missing some information, don&#8217;t use this option. </dd>
<dt><code>&#8211;no-literal</code></dt>
<dd> This is not for normal use. Use the source to see for what it might be useful. </dd>
<dt><code>&#8211;set-filesize</code></dt>
<dd> This is not for normal use. Use the source to see for what it might be useful. </dd>
<dt><code>&#8211;show-session-key</code></dt>
<dd> Display the session key used for one message. See <code>&#8211;override-session-key</code> for the counterpart of this option. </dd>
<p> We think that Key Escrow is a Bad Thing; however the user should have the freedom to decide whether to go to prison or to reveal the content of one specific message without compromising all messages ever encrypted for one secret key. DON&#8217;T USE IT UNLESS YOU ARE REALLY FORCED TO DO SO. </p>
<dt><code>&#8211;override-session-key string</code></dt>
<dd> Don&#8217;t use the public key but the session key <code>string</code>. The format of this string is the same as the one printed by <code>&#8211;show-session-key</code>. This option is normally not used but comes handy in case someone forces you to reveal the content of an encrypted message; using this option you can do this without handing out the secret key. </dd>
<dt><code>&#8211;ask-sig-expire</code></dt>
<dd>
</dd><dt><code>&#8211;no-ask-sig-expire</code></dt>
<dd> When making a data signature, prompt for an expiration time. If this option is not specified, the expiration time set via <code>&#8211;default-sig-expire</code> is used. <code>&#8211;no-ask-sig-expire</code> disables this option. </dd>
<dt><code>&#8211;default-sig-expire</code></dt>
<dd> The default expiration time to use for signature expiration. Valid values are &quot;0&quot; for no expiration, a number followed by the letter d (for days), w (for weeks), m (for months), or y (for years) (for example &quot;2m&quot; for two months, or &quot;5y&quot; for five years), or an absolute date in the form YYYY-MM-DD. Defaults to &quot;0&quot;. </dd>
<dt><code>&#8211;ask-cert-expire</code></dt>
<dd>
</dd><dt><code>&#8211;no-ask-cert-expire</code></dt>
<dd> When making a key signature, prompt for an expiration time. If this option is not specified, the expiration time set via <code>&#8211;default-cert-expire</code> is used. <code>&#8211;no-ask-cert-expire</code> disables this option. </dd>
<dt><code>&#8211;default-cert-expire</code></dt>
<dd> The default expiration time to use for key signature expiration. Valid values are &quot;0&quot; for no expiration, a number followed by the letter d (for days), w (for weeks), m (for months), or y (for years) (for example &quot;2m&quot; for two months, or &quot;5y&quot; for five years), or an absolute date in the form YYYY-MM-DD. Defaults to &quot;0&quot;. </dd>
<dt><code>&#8211;allow-secret-key-import</code></dt>
<dd> This is an obsolete option and is not used anywhere. </dd>
<dt><code>&#8211;allow-multiple-messages</code></dt>
<dd>
</dd><dt><code>&#8211;no-allow-multiple-messages</code></dt>
<dd> Allow processing of multiple OpenPGP messages contained in a single file or stream. Some programs that call GPG are not prepared to deal with multiple messages being processed together, so this option defaults to no. Note that versions of GPG prior to 1.4.7 always allowed multiple messages. </dd>
<p> Warning: Do not use this option unless you need it as a temporary workaround! </p>
<dt><code>&#8211;enable-special-filenames</code></dt>
<dd> This options enables a mode in which filenames of the form &#8216;<i>-&amp;n</i>&#8216;, where n is a non-negative decimal number, refer to the file descriptor n and not to a file with that name. </dd>
<dt><code>&#8211;no-expensive-trust-checks</code></dt>
<dd> Experimental use only. </dd>
<dt><code>&#8211;preserve-permissions</code></dt>
<dd> Don&#8217;t change the permissions of a secret keyring back to user read/write only. Use this option only if you really know what you are doing. </dd>
<dt><code>&#8211;default-preference-list string</code></dt>
<dd> Set the list of default preferences to <code>string</code>. This preference list is used for new keys and becomes the default for &quot;setpref&quot; in the edit menu. </dd>
<dt><code>&#8211;default-keyserver-url name</code></dt>
<dd> Set the default keyserver URL to <code>name</code>. This keyserver will be used as the keyserver URL when writing a new self-signature on a key, which includes key generation and changing preferences. </dd>
<dt><code>&#8211;list-config</code></dt>
<dd> Display various internal configuration parameters of GnuPG. This option is intended for external programs that call GnuPG to perform tasks, and is thus not generally useful. See the file &#8216;<i>doc/DETAILS</i>&#8216; in the source distribution for the details of which configuration items may be listed. <code>&#8211;list-config</code> is only usable with <code>&#8211;with-colons</code> set. </dd>
<dt><code>&#8211;gpgconf-list</code></dt>
<dd> This command is similar to <code>&#8211;list-config</code> but in general only internally used by the <code>gpgconf</code> tool. </dd>
<dt><code>&#8211;gpgconf-test</code></dt>
<dd> This is more or less dummy action. However it parses the configuration file and returns with failure if the configuration file would prevent <code>gpg</code> from startup. Thus it may be used to run a syntax check on the configuration file. </dd>
</dl>
<h3>Deprecated options</h3>
<p> &nbsp;<wbr> </p>
<dl>
<dt><code>&#8211;show-photos</code></dt>
<dd>
</dd><dt><code>&#8211;no-show-photos</code></dt>
<dd> Causes <code>&#8211;list-keys</code>, <code>&#8211;list-sigs</code>, <code>&#8211;list-public-keys</code>, <code>&#8211;list-secret-keys</code>, and verifying a signature to also display the photo ID attached to the key, if any. See also <code>&#8211;photo-viewer</code>. These options are deprecated. Use <code>&#8211;list-options [no-]show-photos</code> and/or <code>&#8211;verify-options [no-]show-photos</code> instead. </dd>
<dt><code>&#8211;show-keyring</code></dt>
<dd> Display the keyring name at the head of key listings to show which keyring a given key resides on. This option is deprecated: use <code>&#8211;list-options [no-]show-keyring</code> instead. </dd>
<dt><code>&#8211;always-trust</code></dt>
<dd> Identical to <code>&#8211;trust-model always</code>. This option is deprecated. </dd>
<dt><code>&#8211;show-notation</code></dt>
<dd>
</dd><dt><code>&#8211;no-show-notation</code></dt>
<dd> Show signature notations in the <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code> listings as well as when verifying a signature with a notation in it. These options are deprecated. Use <code>&#8211;list-options [no-]show-notation</code> and/or <code>&#8211;verify-options [no-]show-notation</code> instead. </dd>
<dt><code>&#8211;show-policy-url</code></dt>
<dd>
</dd><dt><code>&#8211;no-show-policy-url</code></dt>
<dd> Show policy URLs in the <code>&#8211;list-sigs</code> or <code>&#8211;check-sigs</code> listings as well as when verifying a signature with a policy URL in it. These options are deprecated. Use <code>&#8211;list-options [no-]show-policy-url</code> and/or <code>&#8211;verify-options [no-]show-policy-url</code> instead. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gpg -se -r Bob</code> <code>file</code></dt>
<dd> sign and encrypt for user Bob </dd>
<dt><code>gpg &#8211;clearsign file</code></dt>
<dd> make a clear text signature </dd>
<dt><code>gpg -sb file</code></dt>
<dd> make a detached signature </dd>
<dt><code>gpg -u 0x12345678 -sb file</code></dt>
<dd> make a detached signature with the key 0x12345678 </dd>
<dt><code>gpg &#8211;list-keys user_ID</code></dt>
<dd> show keys </dd>
<dt><code>gpg &#8211;fingerprint user_ID</code></dt>
<dd> show fingerprint </dd>
<dt><code>gpg &#8211;verify pgpfile</code></dt>
<dd>
</dd><dt><code>gpg &#8211;verify sigfile</code></dt>
<dd> Verify the signature of the file but do not output the data. The second form is used for detached signatures, where <code>sigfile</code> is the detached signature (either ASCII armored or binary) and are the signed data; if this is not given, the name of the file holding the signed data is constructed by cutting off the extension (&quot;.asc&quot; or &quot;.sig&quot;) of <code>sigfile</code> or by asking the user for the filename. </dd>
</dl>
<h2>HOW TO SPECIFY A USER ID</h2>
<p> There are different ways to specify a user ID to GnuPG. Some of them are only valid for <code>gpg</code> others are only good for <code>gpgsm</code>. Here is the entire list of ways to specify a key: </p>
<dl>
<dt><code>By key Id. </code></dt>
<dd> This format is deduced from the length of the string and its content or <code>0x</code> prefix. The key Id of an X.509 certificate are the low 64 bits of its SHA-1 fingerprint. The use of key Ids is just a shortcut, for all automated processing the fingerprint should be used. </dd>
<p> When using <code>gpg</code> an exclamation mark (!) may be appended to force using the specified primary or secondary key and not to try and calculate which primary or secondary key to use. </p>
<p> The last four lines of the example give the key ID in their long form as internally used by the OpenPGP protocol. You can see the long key ID using the option <code>&#8211;with-colons</code>. </p>
<dl>
<dt>
</dt><dd>
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
</dd></dl>
<dt><code>By fingerprint.</code></dt>
<dd> This format is deduced from the length of the string and its content or the <code>0x</code> prefix. Note, that only the 20 byte version fingerprint is available with <code>gpgsm</code> (i.e. the SHA-1 hash of the certificate). </dd>
<p> When using <code>gpg</code> an exclamation mark (!) may be appended to force using the specified primary or secondary key and not to try and calculate which primary or secondary key to use. </p>
<p> The best way to specify a key Id is by using the fingerprint. This avoids any ambiguities in case that there are duplicated key IDs. </p>
<dl>
<dt>
</dt><dd>
<pre>
1234343434343434C434343434343434
123434343434343C3434343434343734349A3434
0E12343434343434343434EAB3484343434343434
0xE12343434343434343434EAB3484343434343434
</pre>
</dd></dl>
<p> (<code>gpgsm</code> also accepts colons between each pair of hexadecimal digits because this is the de-facto standard on how to present X.509 fingerprints.) </p>
<dt><code>By exact match on OpenPGP user ID.</code></dt>
<dd> This is denoted by a leading equal sign. It does not make sense for X.509 certificates. </dd>
<dl>
<dt>
</dt><dd>
<pre>
=Heinrich Heine &lt;heinrichh [at] uni-duesseldorf.de&gt;
</pre>
</dd></dl>
<dt><code>By exact match on an email address.</code></dt>
<dd> This is indicated by enclosing the email address in the usual way with left and right angles. </dd>
<dl>
<dt>
</dt><dd>
<pre>
&lt;heinrichh [at] uni-duesseldorf.de&gt;
</pre>
</dd></dl>
<dt><code>By word match.</code></dt>
<dd> All words must match exactly (not case sensitive) but can appear in any order in the user ID or a subjects name. Words are any sequences of letters, digits, the underscore and all characters with bit 7 set. </dd>
<dl>
<dt>
</dt><dd>
<pre>
+Heinrich Heine duesseldorf
</pre>
</dd></dl>
<dt><code>By exact match on the subject&#8217;s DN.</code></dt>
<dd> This is indicated by a leading slash, directly followed by the RFC-2253 encoded DN of the subject. Note that you can&#8217;t use the string printed by &quot;gpgsm &#8211;list-keys&quot; because that one as been reordered and modified for better readability; use &#8211;with-colons to print the raw (but standard escaped) RFC-2253 string </dd>
<dl>
<dt>
</dt><dd>
<pre>
/CN=Heinrich Heine,O=Poets,L=Paris,C=FR
</pre>
</dd></dl>
<dt><code>By exact match on the issuer&#8217;s DN.</code></dt>
<dd> This is indicated by a leading hash mark, directly followed by a slash and then directly followed by the rfc2253 encoded DN of the issuer. This should return the Root cert of the issuer. See note above. </dd>
<dl>
<dt>
</dt><dd>
<pre>
#/CN=Root Cert,O=Poets,L=Paris,C=FR
</pre>
</dd></dl>
<dt><code>By exact match on serial number and issuer&#8217;s DN.</code></dt>
<dd> This is indicated by a hash mark, followed by the hexadecimal representation of the serial number, then followed by a slash and the RFC-2253 encoded DN of the issuer. See note above. </dd>
<dl>
<dt>
</dt><dd>
<pre>
#4F03/CN=Root Cert,O=Poets,L=Paris,C=FR
</pre>
</dd></dl>
<dt><code>By keygrip</code></dt>
<dd> This is indicated by an ampersand followed by the 40 hex digits of a keygrip. <code>gpgsm</code> prints the keygrip when using the command <code>&#8211;dump-cert</code>. It does not yet work for OpenPGP keys. </dd>
<dl>
<dt>
</dt><dd>
<pre>
&amp;D75F22C3F86E355877348498CDC92BD21010A480
</pre>
</dd></dl>
<dt><code>By substring match.</code></dt>
<dd> This is the default mode but applications may want to explicitly indicate this by putting the asterisk in front. Match is not case sensitive. </dd>
<dl>
<dt>
</dt><dd>
<pre>
Heine
*Heine
</pre>
</dd></dl>
<p> Please note that we have reused the hash mark identifier which was used in old GnuPG versions to indicate the so called local-id. It is not anymore used and there should be no conflict when used with X.509 stuff. </p>
<p> Using the RFC-2253 format of DNs has the drawback that it is not possible to map them back to the original encoding, however we don&#8217;t have to do this because our key database stores this encoding as meta data. </p>
</dl>
<h2>FILES</h2>
<p> There are a few configuration files to control certain aspects of <code>gpg2</code>&#8216;s operation. Unless noted, they are expected in the current home directory (see: [option &#8211;homedir]). </p>
<dl>
<dt><code>gpg.conf</code></dt>
<dd> This is the standard configuration file read by <code>gpg2</code> on startup. It may contain any valid long option; the leading two dashes may not be entered and the option may not be abbreviated. This default name may be changed on the command line (see: [gpg-option &#8211;options]). You should backup this file. </dd>
<p> Note that on larger installations, it is useful to put predefined files into the directory &#8216;<i>/etc/skel/.gnupg/</i>&#8216; so that newly created users start up with a working configuration. For existing users the a small helper script is provided to create these files (see: [addgnupghome]). </p>
<p> For internal purposes <code>gpg2</code> creates and maintains a few other files; They all live in in the current home directory (see: [option &#8211;homedir]). Only the <code>gpg2</code> may modify these files. </p>
<dt><code>~/.gnupg/secring.gpg</code></dt>
<dd> The secret keyring. You should backup this file. </dd>
<dt><code>~/.gnupg/secring.gpg.lock</code></dt>
<dd> The lock file for the secret keyring. </dd>
<dt><code>~/.gnupg/pubring.gpg</code></dt>
<dd> The public keyring. You should backup this file. </dd>
<dt><code>~/.gnupg/pubring.gpg.lock</code></dt>
<dd> The lock file for the public keyring. </dd>
<dt><code>~/.gnupg/trustdb.gpg</code></dt>
<dd> The trust database. There is no need to backup this file; it is better to backup the ownertrust values (see: [option &#8211;export-ownertrust]). </dd>
<dt><code>~/.gnupg/trustdb.gpg.lock</code></dt>
<dd> The lock file for the trust database. </dd>
<dt><code>~/.gnupg/random_seed</code></dt>
<dd> A file used to preserve the state of the internal random pool. </dd>
<dt><code>/usr[/local]/share/gnupg/options.skel</code></dt>
<dd> The skeleton options file. </dd>
<dt><code>/usr[/local]/lib/gnupg/</code></dt>
<dd> Default location for extensions. </dd>
<p> Operation is further controlled by a few environment variables: </p>
<dt><code>HOME</code></dt>
<dd> Used to locate the default home directory. </dd>
<dt><code>GNUPGHOME</code></dt>
<dd> If set directory used instead of &quot;~/.gnupg&quot;. </dd>
<dt><code>GPG_AGENT_INFO</code></dt>
<dd> Used to locate the gpg-agent.<br />
&nbsp;<wbr>&nbsp;<wbr>The value consists of 3 colon delimited fields: The first is the path<br />
&nbsp;<wbr>&nbsp;<wbr>to the Unix Domain Socket, the second the PID of the gpg-agent and the<br />
&nbsp;<wbr>&nbsp;<wbr>protocol version which should be set to 1. When starting the gpg-agent<br />
&nbsp;<wbr>&nbsp;<wbr>as described in its documentation, this variable is set to the correct<br />
&nbsp;<wbr>&nbsp;<wbr>value. The option&nbsp;<wbr><code>&#8211;gpg-agent-info</code>&nbsp;<wbr>can be used to override it. </dd>
<dt><code>PINENTRY_USER_DATA</code></dt>
<dd> This value is passed via gpg-agent to pinentry. It is useful to convey extra information to a custom pinentry. </dd>
<dt><code>COLUMNS</code></dt>
<dd>
</dd><dt><code>LINES</code></dt>
<dd> Used to size some displays to the full size of the screen. </dd>
<dt><code>LANGUAGE</code></dt>
<dd> Apart from its use by GNU, it is used in the W32 version to override the language selection done through the Registry. If used and set to a valid and available language name (<i>langid</i>), the file with the translation is loaded from </dd>
<p> <i>gpgdir</i>/gnupg.nls/<i>langid</i>.mo. Here <i>gpgdir</i> is the directory out of which the gpg binary has been loaded. If it can&#8217;t be loaded the Registry is tried and as last resort the native Windows locale system is used. </p>
</dl>
<h2>BUGS</h2>
<p> On older systems this program should be installed as setuid(root). This is necessary to lock memory pages. Locking memory pages prevents the operating system from writing memory pages (which may contain passphrases or other sensitive material) to disk. If you get no warning message about insecure memory your operating system supports locking without being root. The program drops root privileges as soon as locked memory is allocated. </p>
<p> Note also that some systems (especially laptops) have the ability to &#8220;suspend to disk&#8221; (also known as &#8220;safe sleep&#8221; or &#8220;hibernate&#8221;). This writes all memory to disk before going into a low power or even powered off mode. Unless measures are taken in the operating system to protect the saved memory, passphrases or other sensitive material may be recoverable from it later. </p>
<p> Before you report a bug you should first search the mailing list archives for similar problems and second check whether such a bug has already been reported to our bug tracker at <a rel="nofollow" href="http://bugs.gnupg.org">http://bugs.gnupg.org</a> . </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpgv/">gpgv</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
</dt><dd>
<pre>
info gnupg
</pre>
</dd></dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
