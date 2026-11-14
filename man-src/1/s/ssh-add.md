---
title: "ssh-add(1)"
name: "ssh-add"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-add/"
description: "ssh-add – adds private key identities to the OpenSSH authentication agent"
---

<h2 class="name">NAME</h2>
<p> <code>ssh-add</code> &#8211; adds private key identities to the OpenSSH authentication agent </p>
<h2>SYNOPSIS</h2>
<p> <code>ssh-add</code> [-<code>cDdKkLlqvXx </code>[-<code>E </code><i>fingerprint_hash</i> ] ] [-<code>H </code><i>hostkey_file</i> ] [-<code>h </code><i>destination_constraint</i> ] [-<code>S </code><i>provider</i> ] [-<code>t </code><i>life</i> ] [<i>file &#8230;</i> ]<br />
<code>ssh-add</code> &#8211;<code>s </code><i>pkcs11</i><br />
<code>ssh-add</code> &#8211;<code>e </code><i>pkcs11</i><br />
<code>ssh-add</code> &#8211;<code>T</code> <i>pubkey &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-add</code> adds private key identities to the authentication agent, ssh-agent1. When run without arguments, it adds the files ~/.ssh/id_rsa ~/.ssh/id_ecdsa ~/.ssh/id_ecdsa_sk ~/.ssh/id_ed25519 ~/.ssh/id_ed25519_sk and ~/.ssh/id_dsa After loading a private key, <code>ssh-add</code> will try to load corresponding certificate information from the filename obtained by appending -cert.pub to the name of the private key file. Alternative file names can be given on the command line. </p>
<p> If any file requires a passphrase, <code>ssh-add</code> asks for the passphrase from the user. The passphrase is read from the user&#8217;s tty. <code>ssh-add</code> retries the last passphrase if multiple identity files are given. </p>
<p> The authentication agent must be running and the <code>SSH_AUTH_SOCK</code> environment variable must contain the name of its socket for <code>ssh-add</code> to work. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> Indicates that added identities should be subject to confirmation before being used for authentication. Confirmation is performed by ssh-askpass1. Successful confirmation is signaled by a zero exit status from ssh-askpass1, rather than text entered into the requester.</p>
<dt><code>-D</code></p>
<dd> Deletes all identities from the agent.</p>
<dt><code>-d</code></p>
<dd> Instead of adding identities, removes identities from the agent. If <code>ssh-add</code> has been run without arguments, the keys for the default identities and their corresponding certificates will be removed. Otherwise, the argument list will be interpreted as a list of paths to public key files to specify keys and certificates to be removed from the agent. If no public key is found at a given path, <code>ssh-add</code> will append .pub and retry. If the argument list consists of &#8220;-&#8221; then <code>ssh-add</code> will read public keys to be removed from standard input.</p>
<dt><code>-E </code><i>fingerprint_hash</i></p>
<dd> Specifies the hash algorithm used when displaying key fingerprints. Valid options are: &#8220;md5&#8221; and &#8220;sha256&#8221; The default is &#8220;sha256&#8221;</p>
<dt><code>-e </code><i>pkcs11</i></p>
<dd> Remove keys provided by the PKCS#11 shared library <i>pkcs11</i></p>
<dt><code>-H </code><i>hostkey_file</i></p>
<dd> Specifies a known hosts file to look up hostkeys when using destination-constrained keys via the &#8211;<code>h</code> flag. This option may be specified multiple times to allow multiple files to be searched. If no files are specified, <code>ssh-add</code> will use the default ssh_config5 known hosts files: ~/.ssh/known_hosts ~/.ssh/known_hosts2 /etc/ssh/ssh_known_hosts and /etc/ssh/ssh_known_hosts2</p>
<dt><code>-h </code><i>destination_constraint</i></p>
<dd> When adding keys, constrain them to be usable only through specific hosts or to specific destinations. </p>
<p> Destination constraints of the form `[user@]dest-hostname&#8217; permit use of the key only from the origin host (the one running ssh-agent1) to the listed destination host, with optional user name. </p>
<p> Constraints of the form `src-hostname&gt;[user@]dst-hostname&#8217; allow a key available on a forwarded ssh-agent1 to be used through a particular host (as specified by `src-hostname&#8217; to authenticate to a further host, specified by `dst-hostname&#8217; </p>
<p> Multiple destination constraints may be added when loading keys. When attempting authentication with a key that has destination constraints, the whole connection path, including ssh-agent1 forwarding, is tested against those constraints and each hop must be permitted for the attempt to succeed. For example, if key is forwarded to a remote host, `host-b&#8217; and is attempting authentication to another host, `host-c&#8217; then the operation will be successful only if `host-b&#8217; was permitted from the origin host and the subsequent `host-b&gt;host-c&#8217; hop is also permitted by destination constraints. </p>
<p> Hosts are identified by their host keys, and are looked up from known hosts files by <code>ssh-add.</code> Wildcards patterns may be used for hostnames and certificate host keys are supported. By default, keys added by <code>ssh-add</code> are not destination constrained. </p>
<p> Destination constraints were added in OpenSSH release 8.9. Support in both the remote SSH client and server is required when using destination-constrained keys over a forwarded ssh-agent1 channel. </p>
<p> It is also important to note that destination constraints can only be enforced by ssh-agent1 when a key is used, or when it is forwarded by a <code>cooperating</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1). Specifically, it does not prevent an attacker with access to a remote <code>SSH_AUTH_SOCK</code> from forwarding it again and using it on a different host (but only to a permitted destination).</p>
<dt><code>-K</code></p>
<dd> Load resident keys from a FIDO authenticator.</p>
<dt><code>-k</code></p>
<dd> When loading keys into or deleting keys from the agent, process plain private keys only and skip certificates.</p>
<dt><code>-L</code></p>
<dd> Lists public key parameters of all identities currently represented by the agent.</p>
<dt><code>-l</code></p>
<dd> Lists fingerprints of all identities currently represented by the agent.</p>
<dt><code>-q</code></p>
<dd> Be quiet after a successful operation.</p>
<dt><code>-S </code><i>provider</i></p>
<dd> Specifies a path to a library that will be used when adding FIDO authenticator-hosted keys, overriding the default of using the internal USB HID support.</p>
<dt><code>-s </code><i>pkcs11</i></p>
<dd> Add keys provided by the PKCS#11 shared library <i>pkcs11</i></p>
<dt><code>-T </code><i>pubkey &#8230;</i></p>
<dd> Tests whether the private keys that correspond to the specified <i>pubkey</i> files are usable by performing sign and verify operations on each.</p>
<dt><code>-t </code><i>life</i></p>
<dd> Set a maximum lifetime when adding identities to an agent. The lifetime may be specified in seconds or in a time format specified in sshd_config5.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Causes <code>ssh-add</code> to print debugging messages about its progress. This is helpful in debugging problems. Multiple &#8211;<code>v</code> options increase the verbosity. The maximum is 3.</p>
<dt><code>-X</code></p>
<dd> Unlock the agent.</p>
<dt><code>-x</code></p>
<dd> Lock the agent with a password.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY, SSH_ASKPASS and SSH_ASKPASS_REQUIRE</code></p>
<dd> If <code>ssh-add</code> needs a passphrase, it will read the passphrase from the current terminal if it was run from a terminal. If <code>ssh-add</code> does not have a terminal associated with it but <code>DISPLAY</code> and <code>SSH_ASKPASS</code> are set, it will execute the program specified by <code>SSH_ASKPASS</code> (by default &#8220;ssh-askpass&#8221; and open an X11 window to read the passphrase. This is particularly useful when calling <code>ssh-add</code> from a .xsession or related script. </p>
<p> <code>SSH_ASKPASS_REQUIRE</code> allows further control over the use of an askpass program. If this variable is set to &#8220;never&#8221; then <code>ssh-add</code> will never attempt to use one. If it is set to &#8220;prefer&#8221; then <code>ssh-add</code> will prefer to use the askpass program instead of the TTY when requesting passwords. Finally, if the variable is set to &#8220;force&#8221; then the askpass program will be used for all passphrase input regardless of whether <code>DISPLAY</code> is set.</p>
<dt><code>SSH_AUTH_SOCK</code></p>
<dd> Identifies the path of a UNIX socket used to communicate with the agent.</p>
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
<dd> Contains the DSA, ECDSA, authenticator-hosted ECDSA, Ed25519, authenticator-hosted Ed25519 or RSA authentication identity of the user.</dl>
<p> Identity files should not be readable by anyone but the user. Note that <code>ssh-add</code> ignores identity files if they are accessible by others.</p>
<h2>EXIT STATUS</h2>
<p> Exit status is 0 on success, 1 if the specified command fails, and 2 if <code>ssh-add</code> is unable to contact the authentication agent.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-agent1, ssh-askpass1, ssh-keygen1, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>AUTHORS</h2>
<p> OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. </p>
<h2>Index</h2>
