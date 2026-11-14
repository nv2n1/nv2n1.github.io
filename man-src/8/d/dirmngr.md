---
title: "dirmngr(8)"
name: "dirmngr"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dirmngr/"
description: "dirmngr – CRL and OCSP daemon"
---

<p><code>dirmngr</code> &#8211; CRL and OCSP daemon</p>
<h2>Synopsis</h2>
<p><code>dirmngr</code> [<i>options</i>] <i>command</i> [<i>args</i>] </p>
<h2>Description</h2>
<p>Since version 2.1 of GnuPG, <code>dirmngr</code> takes care of accessing the OpenPGP keyservers. As with previous versions it is also used as a server for managing and downloading certificate revocation lists (CRLs) for X.509 certificates, downloading X.509 certificates, and providing access to OCSP providers. Dirmngr is invoked internally by <code>gpg</code>, <code>gpgsm</code>, or via the <code>gpg-connect-agent</code> tool. </p>
<h2>Commands</h2>
<p>Commands are not distinguished from options except for the fact that only one command is allowed. </p>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Print the program version and licensing information. Note that you cannot abbreviate this command. </p>
<dt><code>&#8211;help, -h</code></p>
<dd>Print a usage message summarizing the most useful command-line options. Note that you cannot abbreviate this command. </p>
<dt><code>&#8211;dump-options</code></p>
<dd>Print a list of all available options and commands. Note that you cannot abbreviate this command. </p>
<dt><code>&#8211;server</code></p>
<dd>Run in server mode and wait for commands on the <code>stdin</code>. The default mode is to create a socket and listen for commands there. This is only used for testing. </p>
<dt><code>&#8211;daemon</code></p>
<dd>Run in background daemon mode and listen for commands on a socket. This is the way <code>dirmngr</code> is started on demand by the other GnuPG components. To force starting <code>dirmngr</code> it is in general best to use <code>gpgconf &#8211;launch dirmngr</code>. </p>
<dt><code>&#8211;supervised</code></p>
<dd>Run in the foreground, sending logs to stderr, and listening on file descriptor 3, which must already be bound to a listening socket. This is useful when running under systemd or other similar process supervision schemes. This option is not supported on Windows. </p>
<dt><code>&#8211;list-crls</code></p>
<dd>List the contents of the CRL cache on <code>stdout</code>. This is probably only useful for debugging purposes. </p>
<dt><code>&#8211;load-crl </code><i>file</i></p>
<dd>This command requires a filename as additional argument, and it will make Dirmngr try to import the CRL in <i>file</i> into it&#8217;s cache. Note, that this is only possible if Dirmngr is able to retrieve the CA&#8217;s certificate directly by its own means. In general it is better to use <code>gpgsm</code>&#8216;s <code>&#8211;call-dirmngr loadcrl filename</code> command so that <code>gpgsm</code> can help dirmngr. </p>
<dt><code>&#8211;fetch-crl </code><i>url</i></p>
<dd>This command requires an URL as additional argument, and it will make dirmngr try to retrieve and import the CRL from that <i>url</i> into it&#8217;s cache. This is mainly useful for debugging purposes. The <code>dirmngr-client</code> provides the same feature for a running dirmngr. </p>
<dt><code>&#8211;shutdown</code></p>
<dd>This commands shuts down an running instance of Dirmngr. This command has currently no effect. </p>
<dt><code>&#8211;flush</code></p>
<dd>This command removes all CRLs from Dirmngr&#8217;s cache. Client requests will thus trigger reading of fresh CRLs. </p>
</dl>
<h2>Options</h2>
<p>Note that all long options with the exception of <code>&#8211;options</code> and <code>&#8211;homedir</code> may also be given in the configuration file after stripping off the two leading dashes. </p>
<dl>
<dt><code>&#8211;options </code><i>file</i></p>
<dd>Reads configuration from <i>file</i> instead of from the default per-user configuration file. The default configuration file is named &#8216;<i>dirmngr.conf</i>&#8216; and expected in the home directory. </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd>Set the name of the home directory to <i>dir</i>. This option is only effective when used on the command line. The default is the directory named &#8216;<i>.gnupg</i>&#8216; directly below the home directory of the user unless the environment variable <code>GNUPGHOME</code> has been set in which case its value will be used. Many kinds of data are stored within this directory. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Outputs additional information while running. You can increase the verbosity by giving several verbose commands to <code>dirmngr</code>, such as <code>-vv</code>. </p>
<dt><code>&#8211;log-file </code><i>file</i></p>
<dd>Append all logging output to <i>file</i>. This is very helpful in seeing what the agent actually does. Use &#8216;<i>socket://</i>&#8216; to log to socket. </p>
<dt><code>&#8211;debug-level </code><i>level</i></p>
<dd>Select the debug level for investigating problems. <i>level</i> may be a numeric value or by a keyword: </p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>No debugging at all. A value of less than 1 may be used instead of the keyword.</p>
<dt><code>basic</code></p>
<dd>Some basic debug messages. A value between 1 and 2 may be used instead of the keyword.</p>
<dt><code>advanced</code></p>
<dd>More verbose debug messages. A value between 3 and 5 may be used instead of the keyword.</p>
<dt><code>expert</code></p>
<dd>Even more detailed messages. A value between 6 and 8 may be used instead of the keyword.</p>
<dt><code>guru</code></p>
<dd>All of the debug messages you can get. A value greater than 8 may be used instead of the keyword. The creation of hash tracing files is only enabled if the keyword is used.</dl>
</dl>
<p> How these messages are mapped to the actual debugging flags is not specified and may change with newer releases of this program. They are however carefully selected to best aid in debugging. </p>
<dt><code>&#8211;debug </code><i>flags</i></p>
<dd>Set debugging flags. This option is only useful for debugging and its behavior may change with a new release. All flags are or-ed and may be given in C syntax (e.g. 0x0042) or as a comma separated list of flag names. To get a list of all supported flags the single word &quot;help&quot; can be used. </p>
<dt><code>&#8211;debug-all</code></p>
<dd>Same as <code>&#8211;debug=0xffffffff</code> </p>
<dt><code>&#8211;tls-debug </code><i>level</i></p>
<dd>Enable debugging of the TLS layer at <i>level</i>. The details of the debug level depend on the used TLS library and are not set in stone. </p>
<dt><code>&#8211;debug-wait </code><i>n</i></p>
<dd>When running in server mode, wait <i>n</i> seconds before entering the actual processing loop and print the pid. This gives time to attach a debugger. </p>
<dt><code>&#8211;disable-check-own-socket</code></p>
<dd>On some platforms <code>dirmngr</code> is able to detect the removal of its socket file and shutdown itself. This option disable this self-test for debugging purposes. </p>
<dt><code>-s</code></p>
<dd><code>&#8211;sh</code> <code>-c</code> <code>&#8211;csh</code> Format the info output in daemon mode for use with the standard Bourne shell respective the C-shell. The default is to guess it based on the environment variable <code>SHELL</code> which is in almost all cases sufficient. </p>
<dt><code>&#8211;force</code></p>
<dd>Enabling this option forces loading of expired CRLs; this is only useful for debugging. </p>
<dt><code>&#8211;use-tor</code></p>
<dd><code>&#8211;no-use-tor</code> The option <code>&#8211;use-tor</code> switches Dirmngr and thus GnuPG into &#8220;Tor mode&#8221; to route all network access via Tor (an anonymity network). Certain other features are disabled in this mode. The effect of <code>&#8211;use-tor</code> cannot be overridden by any other command or even by reloading dirmngr. The use of <code>&#8211;no-use-tor</code> disables the use of Tor. The default is to use Tor if it is available on startup or after reloading dirmngr. </p>
<dt><code>&#8211;standard-resolver</code></p>
<dd>This option forces the use of the system&#8217;s standard DNS resolver code. This is mainly used for debugging. Note that on Windows a standard resolver is not used and all DNS access will return the error &#8220;Not Implemented&#8221; if this option is used. Using this together with enabled Tor mode returns the error &#8220;Not Enabled&#8221;. </p>
<dt><code>&#8211;recursive-resolver</code></p>
<dd>When possible use a recursive resolver instead of a stub resolver. </p>
<dt><code>&#8211;resolver-timeout </code><i>n</i></p>
<dd>Set the timeout for the DNS resolver to N seconds. The default are 30 seconds. </p>
<dt><code>&#8211;connect-timeout </code><i>n</i></p>
<dd>
<dt><code>&#8211;connect-quick-timeout </code><i>n</i></p>
<dd>Set the timeout for HTTP and generic TCP connection attempts to N seconds. The value set with the quick variant is used when the &#8211;quick option has been given to certain Assuan commands. The quick value is capped at the value of the regular connect timeout. The default values are 15 and 2 seconds. Note that the timeout values are for each connection attempt; the connection code will attempt to connect all addresses listed for a server. </p>
<dt><code>&#8211;listen-backlog </code><i>n</i></p>
<dd>Set the size of the queue for pending connections. The default is 64. </p>
<dt><code>&#8211;allow-version-check</code></p>
<dd>Allow Dirmngr to connect to <code><a rel="nofollow" href="https://versions.gnupg.org">https://versions.gnupg.org</a></code> to get the list of current software versions. On debian-packaged versions, this option does nothing since software updates should be handled by the distribution. See the option <code>&#8211;query-swdb</code> of the command <code>gpgconf</code> for more details. Note, that regardless of this option a version check can always be triggered using this command: </p>
<dl>
<dd>
<pre> gpg-connect-agent --dirmngr 'loadswdb --force' /bye</pre>
</dl>
<dt><code>&#8211;keyserver </code><i>name</i></p>
<dd>Use <i>name</i> as your keyserver. This is the server that <code>gpg</code> communicates with to receive keys, send keys, and search for keys. The format of the <i>name</i> is a URI: `scheme:[//]keyservername[:port]&#8217; The scheme is the type of keyserver: &quot;hkp&quot; for the HTTP (or compatible) keyservers, &quot;ldap&quot; for the LDAP keyservers, or &quot;mailto&quot; for the Graff email keyserver. Note that your particular installation of GnuPG may have other keyserver types available as well. Keyserver schemes are case-insensitive. After the keyserver name, optional keyserver configuration options may be provided. These are the same as the <code>&#8211;keyserver-options</code> of <code>gpg</code>, but apply only to this particular keyserver. </p>
<p> Most keyservers synchronize with each other, so there is generally no need to send keys to more than one server. The keyserver <code><a href="hkp://keys.gnupg.net">hkp://keys.gnupg.net</a></code> uses round robin DNS to give a different keyserver each time you use it. </p>
<p> If exactly two keyservers are configured and only one is a Tor hidden service (.onion), Dirmngr selects the keyserver to use depending on whether Tor is locally running or not. The check for a running Tor is done for each new connection. </p>
<p> If no keyserver is explicitly configured, dirmngr will use the built-in default of <code><a href="hkps://keys.openpgp.org">hkps://keys.openpgp.org</a></code>. </p>
<p> Note that the above default is a Debian-specific choice. Upstream GnuPG prefers <code><a href="hkps://hkps.pool.sks-keyservers.net">hkps://hkps.pool.sks-keyservers.net</a></code>. See /usr/share/doc/gpgconf/NEWS.Debian.gz for more details. </p>
<p> Windows users with a keyserver running on their Active Directory should use <code><a href="ldap:///">ldap:///</a></code> for <i>name</i> to access this directory. </p>
<p> For accessing anonymous LDAP keyservers <i>name</i> is in general just a <code><a href="ldaps://ldap.example.com">ldaps://ldap.example.com</a></code>. A BaseDN parameter should never be specified. If authentication is required the value of <i>name</i> is for example: </p>
<dl>
<dd>
<pre> keyserver <a href="ldaps://ldap.example.com/????bindname=uid=USERNAME">ldaps://ldap.example.com/????bindname=uid=USERNAME</a>
 %2Cou=GnuPG%20Users%2Cdc=example%2Cdc=com,password=PASSWORD</pre>
</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Put this all on one line without any spaces and keep the&nbsp;&#8216;%2C&#8217;&nbsp;as given.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Replace USERNAME, PASSWORD, and the&nbsp;&#8216;dc&#8217;&nbsp;parts according to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;instructions received from the LDAP administrator.&nbsp;<wbr>&nbsp;Note that only<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;simple authentication&nbsp;(i.e. cleartext passwords)&nbsp;is supported and thus<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using ldaps is strongly suggested. </p>
<dt><code>&#8211;nameserver </code><i>ipaddr</i></p>
<dd>In &#8220;Tor mode&#8221; Dirmngr uses a public resolver via Tor to resolve DNS names. If the default public resolver, which is <code>8.8.8.8</code>, shall not be used a different one can be given using this option. Note that a numerical IP address must be given (IPv6 or IPv4) and that no error checking is done for <i>ipaddr</i>. </p>
<dt><code>&#8211;disable-ipv4</code></p>
<dd>
<dt><code>&#8211;disable-ipv6</code></p>
<dd>Disable the use of all IPv4 or IPv6 addresses. </p>
<dt><code>&#8211;disable-ldap</code></p>
<dd>Entirely disables the use of LDAP. </p>
<dt><code>&#8211;disable-http</code></p>
<dd>Entirely disables the use of HTTP. </p>
<dt><code>&#8211;ignore-http-dp</code></p>
<dd>When looking for the location of a CRL, the to be tested certificate usually contains so called CRL Distribution Point (DP) entries which are URLs describing the way to access the CRL. The first found DP entry is used. With this option all entries using the HTTP scheme are ignored when looking for a suitable DP. </p>
<dt><code>&#8211;ignore-ldap-dp</code></p>
<dd>This is similar to <code>&#8211;ignore-http-dp</code> but ignores entries using the LDAP scheme. Both options may be combined resulting in ignoring DPs entirely. </p>
<dt><code>&#8211;ignore-ocsp-service-url</code></p>
<dd>Ignore all OCSP URLs contained in the certificate. The effect is to force the use of the default responder. </p>
<dt><code>&#8211;honor-http-proxy</code></p>
<dd>If the environment variable &#8216;<i>http_proxy</i>&#8216; has been set, use its value to access HTTP servers. </p>
<dt><code>&#8211;http-proxy </code><i>host</i>[:<i>port</i>]</p>
<dd>Use <i>host</i> and <i>port</i> to access HTTP servers. The use of this option overrides the environment variable &#8216;<i>http_proxy</i>&#8216; regardless whether <code>&#8211;honor-http-proxy</code> has been set. </p>
<dt><code>&#8211;ldap-proxy </code><i>host</i>[:<i>port</i>]</p>
<dd>Use <i>host</i> and <i>port</i> to connect to LDAP servers. If <i>port</i> is omitted, port 389 (standard LDAP port) is used. This overrides any specified host and port part in a LDAP URL and will also be used if host and port have been omitted from the URL. </p>
<dt><code>&#8211;only-ldap-proxy</code></p>
<dd>Never use anything else but the LDAP &quot;proxy&quot; as configured with <code>&#8211;ldap-proxy</code>. Usually <code>dirmngr</code> tries to use other configured LDAP server if the connection using the &quot;proxy&quot; failed. </p>
<dt><code>&#8211;ldapserverlist-file </code><i>file</i></p>
<dd>Read the list of LDAP servers to consult for CRLs and certificates from file instead of the default per-user ldap server list file. The default value for <i>file</i> is &#8216;<i>dirmngr_ldapservers.conf</i>&#8216;. </p>
<p> This server list file contains one LDAP server per line in the format </p>
<p> <code>hostname:port:username:password:base_dn</code> </p>
<p> Lines starting with a &#8216;#&#8217; are comments. </p>
<p> Note that as usual all strings entered are expected to be UTF-8 encoded. Obviously this will lead to problems if the password has originally been encoded as Latin-1. There is no other solution here than to put such a password in the binary encoding into the file (i.e. non-ascii characters won&#8217;t show up readable). ([The <code>gpgconf</code> tool might be helpful for frontends as it enables editing this configuration file using percent-escaped strings.]) </p>
<dt><code>&#8211;ldaptimeout </code><i>secs</i></p>
<dd>Specify the number of seconds to wait for an LDAP query before timing out. The default are 15 seconds. 0 will never timeout. </p>
<dt><code>&#8211;add-servers</code></p>
<dd>This option makes dirmngr add any servers it discovers when validating certificates against CRLs to the internal list of servers to consult for certificates and CRLs. </p>
<p> This option is useful when trying to validate a certificate that has a CRL distribution point that points to a server that is not already listed in the ldapserverlist. Dirmngr will always go to this server and try to download the CRL, but chances are high that the certificate used to sign the CRL is located on the same server. So if dirmngr doesn&#8217;t add that new server to list, it will often not be able to verify the signature of the CRL unless the <code>&#8211;add-servers</code> option is used. </p>
<p> Note: The current version of dirmngr has this option disabled by default. </p>
<dt><code>&#8211;allow-ocsp</code></p>
<dd>This option enables OCSP support if requested by the client. </p>
<p> OCSP requests are rejected by default because they may violate the privacy of the user; for example it is possible to track the time when a user is reading a mail. </p>
<dt><code>&#8211;ocsp-responder </code><i>url</i></p>
<dd>Use <i>url</i> as the default OCSP Responder if the certificate does not contain information about an assigned responder. Note, that <code>&#8211;ocsp-signer</code> must also be set to a valid certificate. </p>
<dt><code>&#8211;ocsp-signer </code><i>fpr</i>|<i>file</i></p>
<dd>Use the certificate with the fingerprint <i>fpr</i> to check the responses of the default OCSP Responder. Alternatively a filename can be given in which case the response is expected to be signed by one of the certificates described in that file. Any argument which contains a slash, dot or tilde is considered a filename. Usual filename expansion takes place: A tilde at the start followed by a slash is replaced by the content of &#8216;<i>HOME</i>&#8216;, no slash at start describes a relative filename which will be searched at the home directory. To make sure that the <i>file</i> is searched in the home directory, either prepend the name with &quot;./&quot; or use a name which contains a dot. </p>
<p> If a response has been signed by a certificate described by these fingerprints no further check upon the validity of this certificate is done. </p>
<p> The format of the <i>FILE</i> is a list of SHA-1 fingerprint, one per line with optional colons between the bytes. Empty lines and lines prefix with a hash mark are ignored. </p>
<dt><code>&#8211;ocsp-max-clock-skew </code><i>n</i></p>
<dd>The number of seconds a skew between the OCSP responder and them local clock is accepted. Default is 600 (10 minutes). </p>
<dt><code>&#8211;ocsp-max-period </code><i>n</i></p>
<dd>Seconds a response is at maximum considered valid after the time given in the thisUpdate field. Default is 7776000 (90 days). </p>
<dt><code>&#8211;ocsp-current-period </code><i>n</i></p>
<dd>The number of seconds an OCSP response is considered valid after the time given in the NEXT_UPDATE datum. Default is 10800 (3 hours). </p>
<dt><code>&#8211;max-replies </code><i>n</i></p>
<dd>Do not return more that <i>n</i> items in one query. The default is 10. </p>
<dt><code>&#8211;ignore-cert-extension </code><i>oid</i></p>
<dd>Add <i>oid</i> to the list of ignored certificate extensions. The <i>oid</i> is expected to be in dotted decimal form, like <code>2.5.29.3</code>. This option may be used more than once. Critical flagged certificate extensions matching one of the OIDs in the list are treated as if they are actually handled and thus the certificate won&#8217;t be rejected due to an unknown critical extension. Use this option with care because extensions are usually flagged as critical for a reason. </p>
<dt><code>&#8211;hkp-cacert </code><i>file</i></p>
<dd>Use the root certificates in <i>file</i> for verification of the TLS certificates used with <code>hkps</code> (keyserver access over TLS). If the file is in PEM format a suffix of <code>.pem</code> is expected for <i>file</i>. This option may be given multiple times to add more root certificates. Tilde expansion is supported. </p>
<p> If no <code>hkp-cacert</code> directive is present, dirmngr will make a reasonable choice: if the keyserver in question is the special pool <code>hkps.pool.sks-keyservers.net</code>, it will use the bundled root certificate for that pool. Otherwise, it will use the system CAs. </p>
</dl>
<h2>Examples</h2>
<p>Here is an example on how to show dirmngr&#8217;s internal table of OpenPGP keyserver addresses. The output is intended for debugging purposes and not part of a defined API.</p>
<dl>
<dd>
<pre> gpg-connect-agent --dirmngr 'keyserver --hosttable' /bye</pre>
</dl>
<p> To inhibit the use of a particular host you have noticed in one of the keyserver pools, you may use</p>
<dl>
<dd>
<pre> gpg-connect-agent --dirmngr 'keyserver --dead pgpkeys.bnd.de' /bye</pre>
</dl>
<p> The description of the <code>keyserver</code> command can be printed using</p>
<dl>
<dd>
<pre> gpg-connect-agent --dirmngr 'help keyserver' /bye</pre>
</dl>
<h2>Files</h2>
<p>Dirmngr makes use of several directories when running in daemon mode: There are a few configuration files whih control the operation of dirmngr. By default they may all be found in the current home directory (see: [option &#8211;homedir]). </p>
<dl>
<dt><code>dirmngr.conf</code></p>
<dd>This is the standard configuration file read by <code>dirmngr</code> on startup. It may contain any valid long option; the leading two dashes may not be entered and the option may not be abbreviated. This file is also read after a <code>SIGHUP</code> however not all options will actually have an effect. This default name may be changed on the command line (see: [option &#8211;options]). You should backup this file. </p>
<dt><code>/etc/gnupg/trusted-certs</code></p>
<dd>This directory should be filled with certificates of Root CAs you are trusting in checking the CRLs and signing OCSP Responses. </p>
<p> Usually these are the same certificates you use with the applications making use of dirmngr. It is expected that each of these certificate files contain exactly one DER encoded certificate in a file with the suffix &#8216;<i>.crt</i>&#8216; or &#8216;<i>.der</i>&#8216;. <code>dirmngr</code> reads those certificates on startup and when given a SIGHUP. Certificates which are not readable or do not make up a proper X.509 certificate are ignored; see the log file for details. </p>
<p> Applications using dirmngr (e.g. gpgsm) can request these certificates to complete a trust chain in the same way as with the extra-certs directory (see below). </p>
<p> Note that for OCSP responses the certificate specified using the option <code>&#8211;ocsp-signer</code> is always considered valid to sign OCSP requests. </p>
<dt><code>/etc/gnupg/extra-certs</code></p>
<dd>This directory may contain extra certificates which are preloaded into the internal cache on startup. Applications using dirmngr (e.g. gpgsm) can request cached certificates to complete a trust chain. This is convenient in cases you have a couple intermediate CA certificates or certificates usually used to sign OCSP responses. These certificates are first tried before going out to the net to look for them. These certificates must also be DER encoded and suffixed with &#8216;<i>.crt</i>&#8216; or &#8216;<i>.der</i>&#8216;. </p>
<dt><code>~/.gnupg/crls.d</code></p>
<dd>This directory is used to store cached CRLs. The &#8216;<i>crls.d</i>&#8216; part will be created by dirmngr if it does not exists but you need to make sure that the upper directory exists. </p>
</dl>
<h2>Signals</h2>
<p>A running <code>dirmngr</code> may be controlled by signals, i.e. using the <code>kill</code> command to send a signal to the process. </p>
<p> Here is a list of supported signals: </p>
<dl>
<dt><code>SIGHUP</code></p>
<dd>This signal flushes all internally cached CRLs as well as any cached certificates. Then the certificate cache is reinitialized as on startup. Options are re-read from the configuration file. Instead of sending this signal it is better to use</p>
<dl>
<dd>
<pre>gpgconf --reload dirmngr</pre>
</dl>
<dt><code>SIGTERM</code></p>
<dd>Shuts down the process but waits until all current requests are fulfilled. If the process has received 3 of these signals and requests are still pending, a shutdown is forced. You may also use</p>
<dl>
<dd>
<pre>gpgconf --kill dirmngr</pre>
</dl>
<p> instead of this signal </p>
<dt><code>SIGINT</code></p>
<dd>Shuts down the process immediately. </p>
<dt><code>SIGUSR1</code></p>
<dd>This prints some caching statistics to the log file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-dirmngr-client/">dirmngr-client</a></code>(1) The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command</p>
<dl>
<dd>
<pre>info gnupg</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
