---
title: "dirmngr(1)"
name: "dirmngr"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dirmngr/"
description: "dirmngr – CRL and OCSP daemon"
---

<h2>NAME</h2>
<p> <code>dirmngr</code> &#8211; CRL and OCSP daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>dirmngr</code> [<i>options</i>] <i>command</i> [<i>args</i>] </p>
<h2>DESCRIPTION</h2>
<p> Dirmngr is a server for managing and downloading certificate revocation lists (CRLs) for X.509 certificates and for downloading the certificates themselves. Dirmngr also handles OCSP requests as an alternative to CRLs. Dirmngr is either invoked internally by gpgsm (from GnuPG 2) or when running as a system daemon through the <code>dirmngr-client</code> tool. </p>
<h2>COMMANDS</h2>
<p> Commands are not distinguished from options execpt for the fact that only one command is allowed. </p>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the program version and licensing information. Note that you can abbreviate this command. </dd>
<dt><code>&#8211;help, -h</code></dt>
<dd> Print a usage message summarizing the most useful command-line options. Not that you can abbreviate this command. </dd>
<dt><code>&#8211;server</code></dt>
<dd> Run in server mode and wait for commands on the <code>stdin</code>. The default mode is to create a socket and listen for commands there. </dd>
<dt><code>&#8211;daemon</code></dt>
<dd> Run in background daemon mode and listen for commands on a socket. Note that this also changes the default home directory and enables the internal certificate validation code. </dd>
<dt><code>&#8211;list-crls</code></dt>
<dd> List the contents of the CRL cache on <code>stdout</code>. This is probably only useful for debugging purposes. </dd>
<dt><code>&#8211;load-crl </code><i>file</i></dt>
<dd> This command requires a filename as additional argument, and it will make dirmngr try to import the CRL in <i>file</i> into it&#8217;s cache. Note, that this is only possible if Dirmngr is able to retrieve the CA&#8217;s certificate directly by its own means. In general it is better to use <code>gpgsm</code>&#8216;s <code>&#8211;call-dirmngr loadcrl filename</code> command so that <code>gpgsm</code> can help dirmngr. </dd>
<dt><code>&#8211;fetch-crl </code><i>url</i></dt>
<dd> This command requires an URL as additional argument, and it will make dirmngr try to retrieve an import the CRL from that <i>url</i> into it&#8217;s cache. This is mainly useful for debugging purposes. </dd>
<dt><code>&#8211;shutdown</code></dt>
<dd> This commands shuts down an running instance of Dirmngr. This command has corrently no effect. </dd>
<dt><code>&#8211;flush</code></dt>
<dd> This command removes all CRLs from Dirmngr&#8217;s cache. Client requests will thus trigger reading of fresh CRLs. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;options </code><i>file</i></dt>
<dd> Reads configuration from <i>file</i> instead of from the default per-user configuration file. The default configuration file is named `<i>gpgsm.conf</i>&#8216; and expected in the home directory. </dd>
<dt><code>&#8211;homedir </code><i>dir</i></dt>
<dd> Set the name of the home directory to <i>dir</i>. This option is only effective when used on the command line. The default depends on the running mode: </dd>
<dl>
<dl>
<dt><code>With &#8211;daemon</code> given on the commandline</dt>
<dd> the directory named `<i>/etc/dirmngr</i>&#8216; for configuration files, `<i>/var/lib/dirmngr/</i>&#8216; for extra data and `<i>/var/cache/dirmngr</i>&#8216; for cached CRLs. </dd>
<dt><code>Without &#8211;daemon</code> given on the commandline</dt>
<dd> the directory named `<i>.gnupg</i>&#8216; directly below the home directory of the user unless the environment variable <code>GNUPGHOME</code> has been set in which case its value will be used. All kind of data is stored below this directory.</dd></dl>
</dl>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Outputs additional information while running. You can increase the verbosity by giving several verbose commands to <code>dirmngr</code>, such as <code>-vv</code>. </dd>
<dt><code>&#8211;log-file </code><i>file</i></dt>
<dd> Append all logging output to <i>file</i>. This is very helpful in seeing what the agent actually does. </dd>
<dt><code>&#8211;debug-level </code><i>level</i></dt>
<dd> Select the debug level for investigating problems. <i>level</i> may be one of: </dd>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> no debugging at all.</dd>
<dt><code>basic </code></dt>
<dd> some basic debug messages</dd>
<dt><code>advanced</code></dt>
<dd> more verbose debug messages</dd>
<dt><code>expert</code></dt>
<dd> even more detailed messages</dd>
<dt><code>guru</code></dt>
<dd> all of the debug messages you can get</dd></dl>
</dl>
<p> How these messages are mapped to the actual debugging flags is not specified and may change with newer releases of this program. They are however carefully selected to best aid in debugging. </p>
<dt><code>&#8211;debug </code><i>flags</i></dt>
<dd> This option is only useful for debugging and the behaviour may change at any time without notice. FLAGS are bit encoded and may be given in usual C-Syntax. </dd>
<dt><code>&#8211;debug-all</code></dt>
<dd> Same as <code>&#8211;debug=0xffffffff</code> </dd>
<dt><code>&#8211;debug-wait </code><i>n</i></dt>
<dd> When running in server mode, wait <i>n</i> seconds before entering the actual processing loop and print the pid. This gives time to attach a debugger. </dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;sh</code></dt>
<dd>
</dd><dt><code>-c</code></dt>
<dd>
</dd><dt><code>&#8211;csh</code></dt>
<dd> Format the info output in daemon mode for use with the standard Bourne shell respective the C-shell . The default ist to guess it based on the environment variable <code>SHELL</code> which is in almost all cases sufficient. </dd>
<dt><code>&#8211;force</code></dt>
<dd> Enabling this option forces loading of expired CRLs; this is only useful for debugging. </dd>
<dt><code>&#8211;disable-ldap</code></dt>
<dd> Entirely disables the use of LDAP. </dd>
<dt><code>&#8211;disable-http</code></dt>
<dd> Entirely disables the use of HTTP. </dd>
<dt><code>&#8211;ignore-http-dp</code></dt>
<dd> When looking for the location of a CRL, the to be tested certificate usually contains so called CRL Distribution Point (DP) entries which are URLs describing the way to access the CRL. The first found DP entry is used. With this option all entries using the HTTP scheme are ignored when looking for a suitable DP. </dd>
<dt><code>&#8211;ignore-ldap-dp</code></dt>
<dd> This is similar to <code>&#8211;ignore-http-dp</code> but ignores entries using the LDAP scheme. Both options may be combined resulting in ignoring DPs entirely. </dd>
<dt><code>&#8211;ignore-ocsp-service-url</code></dt>
<dd> Ignore all OCSP URLs contained in the certificate. The effect is to force the use of the default responder. </dd>
<dt><code>&#8211;honor-http-proxy</code></dt>
<dd> If the environment variable `<i>http_proxy</i>&#8216; has been set, use its value to access HTTP servers. </dd>
<dt><code>&#8211;http-proxy </code><i>host</i>[:<i>port</i>]</dt>
<dd> Use <i>host</i> and <i>port</i> to access HTTP servers. The use of this options overrides the environment variable `<i>http_proxy</i>&#8216; regardless whether <code>&#8211;honor-http-proxy</code> has been set. </dd>
<dt><code>&#8211;ldap-proxy </code><i>host</i>[:<i>port</i>]</dt>
<dd> Use <i>host</i> and <i>port</i> to connect to LDAP servers. If <i>port</i> is ommitted, port 389 (standard LDAP port) is used. This overrides any specified host and port part in a LDAP URL and will also be used if host and port have been ommitted from the URL. </dd>
<dt><code>&#8211;only-ldap-proxy</code></dt>
<dd> Never use anything else but the LDAP &quot;proxy&quot; as configured with <code>&#8211;ldap-proxy</code>. Usually <code>dirmngr</code> tries to use other configured LDAP server if the connection using the &quot;proxy&quot; failed. </dd>
<dt><code>&#8211;ldapserverlist-file </code><i>file</i></dt>
<dd> Read the list of LDAP servers to consult for CRLs and certificates from file instead of the default per-user ldap server list file. The default value for <i>file</i> is `<i>dirmngr_ldapservers.conf</i>&#8216; or `<i>ldapservers.conf</i>&#8216; when running in <code>&#8211;daemon</code> mode. </dd>
<p> This server list file contains one LDAP server per line in the format </p>
<p> <code>hostname:port:username:password:base_dn</code> </p>
<p> Lines starting with a &#8216;#&#8217; are comments. </p>
<p> Note that as usual all strings entered are expected to be UTF-8 encoded. Obviously this will lead to problems if the password has orginally been encoded as Latin-1. There is no other solution here than to put such a password in the binary encoding into the file (i.e. non-ascii characters won&#8217;t show up readable). ([The <code>gpgconf</code> tool might be helpful for frontends as it allows to edit this configuration file using percent escaped strings.]) </p>
<dt><code>&#8211;ldaptimeout </code><i>secs</i></dt>
<dd> Specify the number of seconds to wait for an LDAP query before timing out. The default is currently 100 seconds. 0 will never timeout. </dd>
<dt><code>&#8211;add-servers</code></dt>
<dd> This options makes dirmngr add any servers it discovers when validating certificates against CRLs to the internal list of servers to consult for certificates and CRLs. </dd>
<p> This options is useful when trying to validate a certificate that has a CRL distribution point that points to a server that is not already listed in the ldapserverlist. Dirmngr will always go to this server and try to download the CRL, but chances are high that the certificate used to sign the CRL is located on the same server. So if dirmngr doesn&#8217;t add that new server to list, it will often not be able to verify the signature of the CRL unless the <code>&#8211;add-servers</code> option is used. </p>
<p> Note: The current version of dirmngr has this option disabled by default. </p>
<dt><code>&#8211;allow-ocsp</code></dt>
<dd> This option enables OCSP support if requested by the client. </dd>
<p> OCSP requests are rejected by default because they may violate the privacy of the user; for example it is possible to track the time when a user is reading a mail. </p>
<dt><code>&#8211;ocsp-responder </code><i>url</i></dt>
<dd> Use <i>url</i> as the default OCSP Responder if the certificate does not contain information about an assigned responder. Note, that <code>&#8211;ocsp-signer</code> must also be set to a valid certificate. </dd>
<dt><code>&#8211;ocsp-signer </code><i>fpr</i>|<i>file</i></dt>
<dd> Use the certificate with the fingerprint <i>fpr</i> to check the responses of the default OCSP Responder. Alternativly a filename can be given in which case the respinse is expected to be signed by one of the certificates described in that file. Any argument which contains a slash, dot or tilde is considered a filename. Usual filename expansion takes place: A tilde at the start followed by a slash is replaced by the content of `<i>HOME</i>&#8216;, no slash at start describes a relative filename which will be searched at the home directory. To make sure that the <i>file</i> is searched in the home directory, either prepend the name with &quot;./&quot; or use a name which contains a dot. </dd>
<p> If a response has been signed by a certificate described by these fingerprints no further check upon the validity of this certificate is done. </p>
<p> The format of the <i>FILE</i> is a list of SHA-1 fingerprint, one per line with optional colons between the bytes. Empty lines and lines prefix with a hash mark are ignored. </p>
<dt><code>&#8211;ocsp-max-clock-skew </code><i>n</i></dt>
<dd> The number of seconds a skew between the OCSP responder and them local clock is accepted. Default is 600 (20 minutes). </dd>
<dt><code>&#8211;ocsp-max-period </code><i>n</i></dt>
<dd> Seconds a response is at maximum considered valid after the time given in the thisUpdate field. Default is 7776000 (90 days). </dd>
<dt><code>&#8211;ocsp-current-period </code><i>n</i></dt>
<dd> The number of seconds an OCSP response is considered valid after the time given in the NEXT_UPDATE datum. Default is 10800 (3 hours). </dd>
<dt><code>&#8211;max-replies </code><i>n</i></dt>
<dd> Do not return more that <i>n</i> items in one query. The default is 10. </dd>
</dl>
<h2>SIGNALS</h2>
<p> A running <code>dirmngr</code> may be controlled by signals, i.e. using the <code>kill</code> command to send a signal to the process. </p>
<p> Here is a list of supported signals: </p>
<dl>
<dt><code>SIGHUP</code></dt>
<dd> This signals flushes all internally cached CRLs as well as any cached certificates. Then the certificate cache is reinitialized as on startup. Options are re-read from the configuration file. </dd>
<dt><code>SIGTERM</code></dt>
<dd> Shuts down the process but waits until all current requests are fulfilled. If the process has received 3 of these signals and requests are still pending, a shutdown is forced. </dd>
<dt><code>SIGINT</code></dt>
<dd> Shuts down the process immediately. </dd>
<dt><code>SIGUSR1</code></dt>
<dd> This prints some caching statistics to the log file. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> The way to start the dirmngr in the foreground (as done by tools if no dirmngr is running in the background) is to use: </p>
<dl>
<dt>
</dt><dd>
<pre>
  dirmngr --server -v
</pre>
</dd></dl>
<p> If a dirmngr is supposed to be used as a system wide daemon, it should be started like: </p>
<dl>
<dt>
</dt><dd>
<pre>
  dirmngr --daemon
</pre>
</dd></dl>
<p> This will force it to go into the backround, read the default certificates (including the trusted root certificates) and listen on a socket for client requests. It does also print information about the socket used but they are only for compatibilty reasons with old GnuPG versions and may be ignored. </p>
<h2>FILES</h2>
<p> Dirmngr makes use of several directories when running in daemon mode: </p>
<dl>
<dt><code>/etc/dirmngr</code></dt>
<dd> This is where all the configuration files are expected by default. </dd>
<dt><code>/etc/dirmngr/trusted-certs</code></dt>
<dd> This directory should be filled with certificates of Root CAs you are trusting in checking the CRLS and signing OCSP Reponses. Usually these are the same certificates you use with the applications making use of dirmngr. It is expected that each of these certificate files contain exactly one DER encoded certificate in a file with the suffix `<i>.crt</i>&#8216; or `<i>.der</i>&#8216;. <code>dirmngr</code> reads those certificates on startup and when given a SIGHUP. Certificates which are not readable or do not make up a proper X.509 certificate are ignored; see the log file for details. </dd>
<p> Note that for OCSP responses the certificate specified using the option <code>&#8211;ocsp-signer</code> is always considered valid to sign OCSP requests. </p>
<dt><code>/var/lib/dirmngr/extra-certs</code></dt>
<dd> This directory may contain extra certificates which are preloaded into the interal cache on startup. This is convenient in cases you have a couple intermediate CA certificates or certificates ususally used to sign OCSP reponses. These certificates are first tried before going out to the net to look for them. These certificates must also be DER encoded and suffixed with `<i>.crt</i>&#8216; or `<i>.der</i>&#8216;. </dd>
<dt><code>/var/run/dirmngr</code></dt>
<dd> This directory keeps the socket file for accsing <code>dirmngr</code> services. The name of the socket file will be `<i>socket</i>&#8216;. Make sure that this directory has the proper permissions to let <code>dirmngr</code> create the socket file and that eligible users may read and write to that socket. </dd>
<dt><code>/var/cache/dirmngr/crls.d</code></dt>
<dd> This directory is used to store cached CRLs. The `<i>crls.d</i>&#8216; part will be created by dirmngr if it does not exists but you need to make sure that the upper directory exists. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-dirmngr-client/">dirmngr-client</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If dirmngr and the info program are properly installed at your site, the command </p>
<dl>
<dt>
</dt><dd>
<pre>
info dirmngr
</pre>
</dd></dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
