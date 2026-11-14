---
title: "monkeysphere-authentication(8)"
name: "monkeysphere-authentication"
section: "8"
letter: "m"
url: "/docs/linux/man/8-monkeysphere-authentication/"
description: "monkeysphere-authentication – Monkeysphere authentication admin tool."
---

<p>monkeysphere-authentication &#8211; Monkeysphere authentication admin tool.</p>
<h2>Synopsis</h2>
<p><code>monkeysphere-authentication </code><i>subcommand</i> [<i>args</i>] </p>
<h2>Description</h2>
<p><code>Monkeysphere</code> is a framework to leverage the OpenPGP Web of Trust (WoT) for key-based authentication. OpenPGP keys are tracked via GnuPG, and added to the authorized_keys files used by OpenSSH for connection authentication. <code>monkeysphere-authentication</code> is a Monkeysphere server admin utility for configuring and managing SSH user authentication through the WoT. </p>
<h2>Subcommands</h2>
<p><code>monkeysphere-authentication</code> takes various subcommands:</p>
<dl>
<dt><code>update-users [USER]&#8230;</code></p>
<dd>Rebuild the monkeysphere-controlled authorized_keys files. For each specified account, the user ID&#8217;s listed in the account&#8217;s authorized_user_ids file are processed. For each user ID, gpg will be queried for keys associated with that user ID, optionally querying a keyserver. If an acceptable key is found (see KEY ACCEPTABILITY in <a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a>(7)), the key is added to the account&#8217;s monkeysphere-controlled authorized_keys file. If the RAW_AUTHORIZED_KEYS variable is set, then a separate authorized_keys file (usually ~USER/.ssh/authorized_keys) is appended to the monkeysphere-controlled authorized_keys file. If no accounts are specified, then all accounts on the system are processed. `u&#8217; may be used in place of `update-users&#8217;.</p>
<dt><code>keys-for-user USER</code></p>
<dd>Output to stdout authorized_keys lines for USER. This command behaves exactly like update-users (above), except that the resulting authorized_keys lines are output to stdout, instead of being written to the monkeysphere-controlled authorized_keys file.</p>
<dt><code>refresh-keys</code></p>
<dd>Refresh all keys in the monkeysphere-authentication keyring. If no accounts are specified, then all accounts on the system are processed. `r&#8217; may be used in place of `refresh-keys&#8217;.</p>
<dt><code>add-id-certifier KEYID|FILE</code></p>
<dd>Instruct system to trust user identity certifications made by KEYID. The key ID will be loaded from the keyserver. A file may be loaded instead of pulling the key from the keyserver by specifying the path to the file as the argument, or by specifying `-&#8216; to load from stdin. Using the `-n&#8217; or `&#8211;domain&#8217; option allows you to indicate that you only trust the given KEYID to make identifications within a specific domain (e.g. &quot;trust KEYID to certify user identities within the @example.org domain&quot;). A certifier trust level can be specified with the `-t&#8217; or `&#8211;trust&#8217; option (possible values are `marginal&#8217; and `full&#8217; (default is `full&#8217;)). A certifier trust depth can be specified with the `-d&#8217; or `&#8211;depth&#8217; option (default is 1). `c+&#8217; may be used in place of `add-id-certifier&#8217;.</p>
<dt><code>remove-id-certifier KEYID</code></p>
<dd>Instruct system to ignore user identity certifications made by KEYID. `c-&#8216; may be used in place of `remove-id-certifier&#8217;.</p>
<dt><code>list-id-certifiers</code></p>
<dd>List key IDs trusted by the system to certify user identities. `c&#8217; may be used in place of `list-id-certifiers&#8217;.</p>
<dt><code>version</code></p>
<dd>Show the monkeysphere version number. `v&#8217; may be used in place of `version&#8217;.</p>
<dt><code>help</code></p>
<dd>Output a brief usage summary. `h&#8217; or `?&#8217; may be used in place of `help&#8217;. </p>
<p> Other commands:</p>
<dt><code>setup</code></p>
<dd>Setup the server in preparation for Monkeysphere user authentication. This command is idempotent and run automatically by the other commands, and should therefore not usually need to be run manually. `s&#8217; may be used in place of `setup&#8217;.</p>
<dt><code>diagnostics</code></p>
<dd>Review the state of the server with respect to authentication. `d&#8217; may be used in place of `diagnostics&#8217;.</p>
<dt><code>gpg-cmd</code></p>
<dd>Execute a gpg command, as the monkeysphere user, on the monkeysphere authentication `sphere&#8217; keyring. As of monkeysphere 0.36, this takes its arguments separately, not as a single string. Use this command with caution, as modifying the authentication sphere keyring can affect ssh user authentication. </p>
</dl>
<h2>Setup User Authentication</h2>
<p>If the server will handle user authentication through monkeysphere-generated authorized_keys files, the server must be told which keys will act as identity certifiers. This is done with the <code>add-id-certifier</code> command: </p>
<p> # monkeysphere-authentication add-id-certifier KEYID </p>
<p> where KEYID is the key ID of the server admin, or whoever&#8217;s certifications should be acceptable to the system for the purposes of authenticating remote users. You can run this command multiple times to indicate that multiple certifiers are trusted. You may also specify a filename instead of a key ID, as long as the file contains a single OpenPGP public key. Certifiers can be removed with the <code>remove-id-certifier</code> command, and listed with the <code>list-id-certifiers</code> command. </p>
<p> A remote user will be granted access to a local account based on the appropriately-signed and valid keys associated with user IDs listed in that account&#8217;s authorized_user_ids file. By default, the authorized_user_ids file for an account is ~/.monkeysphere/authorized_user_ids. This can be changed in the monkeysphere-authentication.conf file. </p>
<p> The <code>update-users</code> command is used to generate authorized_keys files for a local account based on the user IDs listed in the account&#8217;s authorized_user_ids file: </p>
<p> # monkeysphere-authentication update-users USER </p>
<p> Not specifying USER will cause all accounts on the system to updated. The ssh server can use these monkeysphere-generated authorized_keys files to grant access to user accounts for remote users. In order for sshd to look at the monkeysphere-generated authorized_keys file for user authentication, the AuthorizedKeysFile parameter must be set in the sshd_config to point to the monkeysphere-generated authorized_keys files: </p>
<p> AuthorizedKeysFile /var/lib/monkeysphere/authorized_keys/%u </p>
<p> It is recommended to add &quot;monkeysphere-authentication update-users&quot; to a system crontab, so that user keys are kept up-to-date, and key revocations and expirations can be processed in a timely manner.</p>
<h2>Environment</h2>
<p>The following environment variables will override those specified in the config file (defaults in parentheses):</p>
<dl>
<dt>MONKEYSPHERE_MONKEYSPHERE_USER</p>
<dd>User to control authentication keychain. (monkeysphere)</p>
<dt>MONKEYSPHERE_LOG_LEVEL</p>
<dd>Set the log level. Can be SILENT, ERROR, INFO, VERBOSE, DEBUG, in increasing order of verbosity. (INFO)</p>
<dt>MONKEYSPHERE_KEYSERVER</p>
<dd>OpenPGP keyserver to use. (pool.sks-keyservers.net)</p>
<dt>MONKEYSPHERE_CHECK_KEYSERVER</p>
<dd>Whether or not to check the keyserver when making gpg queries. (true)</p>
<dt>MONKEYSPHERE_AUTHORIZED_USER_IDS</p>
<dd>Path to user&#8217;s authorized_user_ids file. %h gets replaced with the user&#8217;s homedir, %u with the username. (%h/.monkeysphere/authorized_user_ids)</p>
<dt>MONKEYSPHERE_RAW_AUTHORIZED_KEYS</p>
<dd>Path to regular ssh-style authorized_keys file to append to monkeysphere-generated authorized_keys. `none&#8217; means not to add any raw authorized_keys file. %h gets replaced with the user&#8217;s homedir, %u with the username. (%h/.ssh/authorized_keys)</p>
<dt>MONKEYSPHERE_PROMPT</p>
<dd>If set to `false&#8217;, never prompt the user for confirmation. (true)</p>
<dt>MONKEYSPHERE_STRICT_MODES</p>
<dd>If set to `false&#8217;, ignore too-loose permissions on known_hosts, authorized_keys, and authorized_user_ids files. NOTE: setting this to false may expose users to abuse by other users on the system. (true) </p>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/monkeysphere/monkeysphere-authentication.conf</p>
<dd>System monkeysphere-authentication config file.</p>
<dt>/etc/monkeysphere/monkeysphere-authentication-x509-anchors.crt or<br />
 /etc/monkeysphere/monkeysphere-x509-anchors.crt</p>
<dd>If monkeysphere-authentication is configured to query an hkps keyserver, it will use the PEM-encoded X.509 Certificate Authority certificates in this file to validate any X.509 certificates used by the keyserver. If the monkeysphere-authentication-x509 file is present, the monkeysphere-x509 file will be ignored.</p>
<dt>/var/lib/monkeysphere/authorized_keys/USER</p>
<dd>Monkeysphere-controlled user authorized_keys files.</p>
<dt>~/.monkeysphere/authorized_user_ids</p>
<dd>A list of OpenPGP user IDs, one per line. OpenPGP keys with an exactly-matching User ID (calculated valid by the designated identity certifiers), will have any valid authorization-capable keys or subkeys added to the given user&#8217;s authorized_keys file. Any line with initial whitespace will be interpreted as ssh authorized_keys options applicable to the preceding User ID. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by: Jameson Rollins &lt;jrollins [at] finestructure.net&gt;, Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt;, Matthew Goins &lt;mjgoins [at] openflows.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-monkeysphere/">monkeysphere</a></code>(1), <code><a href="/docs/linux/man/8-monkeysphere-host/">monkeysphere-host</a></code>(8), <code><a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a></code>(7), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8), <code><a href="/docs/linux/man/5-sshd_config/">sshd_config</a></code>(5) </p>
