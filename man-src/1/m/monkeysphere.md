---
title: "monkeysphere(1)"
name: "monkeysphere"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monkeysphere/"
description: "monkeysphere – Monkeysphere client user interface"
---

<h2 class="name">NAME</h2>
<p> monkeysphere &#8211; Monkeysphere client user interface</p>
<h2>SYNOPSIS</h2>
<p> <code>monkeysphere </code><i>subcommand</i> [<i>args</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Monkeysphere</code> is a framework to leverage the OpenPGP web of trust for OpenSSH and TLS key-based authentication. OpenPGP keys are tracked via GnuPG, and added to the authorized_keys and known_hosts files used by OpenSSH for connection authentication. Monkeysphere can also be used by a validation agent to validate TLS connections (e.g. https). </p>
<p> <code>monkeysphere</code> is the Monkeysphere client utility. </p>
<h2>SUBCOMMANDS</h2>
<p> <code>monkeysphere</code> takes various subcommands:</p>
<dl>
<dt><code>update-known_hosts [HOST]&#8230;</code></p>
<dd> Update the known_hosts file. For each specified host, gpg will be queried for a key associated with the host URI (see HOST IDENTIFICATION in <code><a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a>(7)),</code> optionally querying a keyserver. If an acceptable key is found for the host (see KEY ACCEPTABILITY in <code><a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a>(7)),</code> the key is added to the user&#8217;s known_hosts file. If a key is found but is unacceptable for the host, any matching keys are removed from the user&#8217;s known_hosts file. If no gpg key is found for the host, nothing is done. If no hosts are specified, all hosts listed in the known_hosts file will be processed. This subcommand will exit with a status of 0 if at least one acceptable key was found for a specified host, 1 if no matching keys were found at all, and 2 if matching keys were found but none were acceptable. `k&#8217; may be used in place of `update-known_hosts&#8217;.</p>
<dt><code>update-authorized_keys</code></p>
<dd> Update the authorized_keys file for the user executing the command (see MONKEYSPHERE_AUTHORIZED_KEYS in ENVIRONMENT, below). First all monkeysphere keys are cleared from the authorized_keys file. Then, for each user ID in the user&#8217;s authorized_user_ids file, gpg will be queried for keys associated with that user ID, optionally querying a keyserver. If an acceptable key is found (see KEY ACCEPTABILITY in <code><a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a></code>(7)), the key is added to the user&#8217;s authorized_keys file. If a key is found but is unacceptable for the user ID, any matching keys are removed from the user&#8217;s authorized_keys file. If no gpg key is found for the user ID, nothing is done. This subcommand will exit with a status of 0 if at least one acceptable key was found for a user ID, 1 if no matching keys were found at all, and 2 if matching keys were found but none were acceptable. `a&#8217; may be used in place of `update-authorized_keys&#8217;.</p>
<dt><code>gen-subkey [KEYID]</code></p>
<dd> Generate an authentication subkey for a private key in your GnuPG keyring. KEYID is the key ID for the primary key for which the subkey with &quot;authentication&quot; capability will be generated. If no key ID is specified, but only one key exists in the secret keyring, that key will be used. The length of the generated key can be specified with the `&#8211;length&#8217; or `-l&#8217; option. `g&#8217; may be used in place of `gen-subkey&#8217;.</p>
<dt><code>ssh-proxycommand [&#8211;no-connect] HOST [PORT]</code></p>
<dd> An ssh ProxyCommand that can be used to trigger a monkeysphere update of the ssh known_hosts file for a host that is being connected to with ssh. This works by updating the known_hosts file for the host first, before an attempted connection to the host is made. Once the known_hosts file has been updated, a TCP connection to the host is made by exec&#8217;ing <a href="/docs/linux/man/1-netcat/">netcat</a>(1). Regular ssh communication is then done over this netcat TCP connection (see ProxyCommand in <a href="/docs/linux/man/5-ssh_config/">ssh_config</a>(5) for more info). </p>
<p> This command is meant to be run as the ssh &quot;ProxyCommand&quot;. This can either be done by specifying the proxy command on the command line: </p>
<p> <code>ssh -o ProxyCommand=monkeysphere ssh-proxycommand %h %p &#8230;</code> </p>
<p> or by adding the following line to your ~/.ssh/config script: </p>
<p> <code>ProxyCommand monkeysphere ssh-proxycommand %h %p</code> </p>
<p> The script can easily be incorporated into other ProxyCommand scripts by calling it with the &quot;&#8211;no-connect&quot; option, i.e.: </p>
<p> <code>monkeysphere ssh-proxycommand &#8211;no-connect $HOST $PORT</code> </p>
<p> This will run everything except the final exec of netcat to make the TCP connection to the host. In this way this command can be added to another proxy command that does other stuff, and then makes the connection to the host itself. For example, in ~/.ssh/config: </p>
<p> <code>ProxyCommand sh -c &#8216;monkeysphere ssh-proxycommand &#8211;no-connect %h %p; ssh -W %h:%p jumphost.example.net&#8217;</code> </p>
<p> KEYSERVER CHECKING: The proxy command has a fairly nuanced policy for when keyservers are queried when processing a host. If the host userID is not found in either the user&#8217;s keyring or in the known_hosts file, then the keyserver is queried for the host userID. If the host userID is found in the user&#8217;s keyring, then the keyserver is not checked. This assumes that the keyring is kept up-to-date, in a cronjob or the like, so that revocations are properly handled. If the host userID is not found in the user&#8217;s keyring, but the host is listed in the known_hosts file, then the keyserver is not checked. This last policy might change in the future, possibly by adding a deferred check, so that hosts that go from non-monkeysphere-enabled to monkeysphere-enabled will be properly checked. </p>
<p> Setting the CHECK_KEYSERVER variable in the config file or the MONKEYSPHERE_CHECK_KEYSERVER environment variable to either `true&#8217; or `false&#8217; will override the keyserver-checking policy defined above and either always or never check the keyserver for host key updates. </p>
<dt><code>subkey-to-ssh-agent [ssh-add arguments]</code></p>
<dd> Push all authentication-capable subkeys in your GnuPG secret keyring into your running ssh-agent. Additional arguments are passed through to <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1). For example, to remove the authentication subkeys, pass an additional `-d&#8217; argument. To require confirmation on each use of the key, pass `-c&#8217;. The MONKEYSPHERE_SUBKEYS_FOR_AGENT environment can be used to specify the full fingerprints of specific keys to add to the agent (space separated), instead of adding them all. `s&#8217; may be used in place of `subkey-to-ssh-agent&#8217;.</p>
<dt><code>keys-for-userid USERID</code></p>
<dd> Output to stdout all acceptable keys for a given user ID. `u&#8217; may be used in place of `keys-for-userid&#8217;.</p>
<dt><code>sshfprs-for-userid USERID</code></p>
<dd> Output the ssh fingerprints of acceptable keys for a given user ID.</p>
<dt><code>version</code></p>
<dd> Show the monkeysphere version number. `v&#8217; may be used in place of `version&#8217;.</p>
<dt><code>help</code></p>
<dd> Output a brief usage summary. `h&#8217; or `?&#8217; may be used in place of `help&#8217;. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables will override those specified in the monkeysphere.conf configuration file (defaults in parentheses):</p>
<dl>
<dt>MONKEYSPHERE_LOG_LEVEL</p>
<dd> Set the log level. Can be SILENT, ERROR, INFO, VERBOSE, DEBUG, in increasing order of verbosity. (INFO)</p>
<dt>MONKEYSPHERE_GNUPGHOME, GNUPGHOME</p>
<dd> GnuPG home directory. (~/.gnupg)</p>
<dt>MONKEYSPHERE_KEYSERVER</p>
<dd> OpenPGP keyserver to use. (pool.sks-keyservers.net)</p>
<dt>MONKEYSPHERE_CHECK_KEYSERVER</p>
<dd> Whether or not to check keyserver when making gpg queries. (true)</p>
<dt>MONKEYSPHERE_KNOWN_HOSTS</p>
<dd> Path to ssh known_hosts file. (~/.ssh/known_hosts)</p>
<dt>MONKEYSPHERE_HASH_KNOWN_HOSTS</p>
<dd> Whether or not to hash to the known_hosts file entries. (false)</p>
<dt>MONKEYSPHERE_AUTHORIZED_KEYS</p>
<dd> Path to ssh authorized_keys file. (~/.ssh/authorized_keys)</p>
<dt>MONKEYSPHERE_PROMPT</p>
<dd> If set to `false&#8217;, never prompt the user for confirmation. (true)</p>
<dt>MONKEYSPHERE_STRICT_MODES</p>
<dd> If set to `false&#8217;, ignore too-loose permissions on known_hosts, authorized_keys, and authorized_user_ids files. NOTE: setting this to false may expose you to abuse by other users on the system. (true)</p>
<dt>MONKEYSPHERE_SUBKEYS_FOR_AGENT</p>
<dd> A space-separated list of authentication-capable subkeys to add to the ssh agent with subkey-to-ssh-agent. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>~/.monkeysphere/monkeysphere.conf</p>
<dd> User monkeysphere config file.</p>
<dt>/etc/monkeysphere/monkeysphere.conf</p>
<dd> System-wide monkeysphere config file.</p>
<dt>~/.monkeysphere/authorized_user_ids</p>
<dd> A list of OpenPGP user IDs, one per line. OpenPGP keys with an exactly-matching User ID (calculated valid by the designated identity certifiers), will have any valid authorization-capable keys or subkeys added to the given user&#8217;s authorized_keys file. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by: Jameson Rollins &lt;jrollins [at] finestructure.net&gt;, Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-monkeysphere-host/">monkeysphere-host</a></code>(8), <code><a href="/docs/linux/man/8-monkeysphere-authentication/">monkeysphere-authentication</a></code>(8), <code><a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a></code>(7), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<h2>Index</h2>
