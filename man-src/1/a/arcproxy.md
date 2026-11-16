---
title: "arcproxy(1)"
name: "arcproxy"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcproxy/"
description: "arcproxy – ARC Credentials Proxy generation utility"
---

<h2>NAME</h2>
<p> arcproxy &#8211; ARC Credentials Proxy generation utility</p>
<h2>SYNOPSIS</h2>
<p> <code>arcproxy</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> arcproxy generates proxy credentials (general proxy certificate, or proxy certificate with VOMS AC extenstion) from private key and certificate of user.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> prints short usage description </dd>
<dt><code>-P</code> <i>filename</i></dt>
<dd> location of the generated proxy file </dd>
<dt><code>-C</code></dt>
<dd> location of X509 certificate file, the file can be either pem, der, or pkcs12 formated; if this option is not set, then env X509_USER_CERT will be searched; if X509_USER_CERT env is not set, then certificatepath item in client.conf will be searched; if the location still is not found, then ~/.arc/, ~/.globus/, ./etc/arc, and ./ will be searched. </dd>
<dt><code>-K</code></dt>
<dd> location of private key file, if the certificate is in pkcs12 format, then no need to give private key; if this option is not set, then env X509_USER_KEY will be searched; if X509_USER_KEY env is not set, then keypath item in client.conf will be searched; if the location still is not found, then ~/.arc/, ~/.globus/, ./etc/arc, and ./ will be searched. </dd>
<dt><code>-T</code></dt>
<dd> path to trusted certificate directory, only needed for VOMS client functionality; if this option is not set, then env X509_CERT_DIR will be searched; if X509_CERT_DIR env is not set, then cacertificatesdirectory item in client.conf will be searched. </dd>
<dt><code>-s</code></dt>
<dd> path to top directory of VOMS *.lsc files, only needed for VOMS client functionality </dd>
<dt><code>-V</code></dt>
<dd> path to VOMS server configuration file, only needed for VOMS client functionality if the path is a directory rather than a file, all of the files under this directory will be searched </dd>
<dt><code>-S</code></dt>
<dd> voms&lt;:command&gt;. Specify VOMS server.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:command is optional, and is used to ask for specific attributes(e.g: roles)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>command option is:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>all &#8212; put all of this DN&#8217;s attributes into AC;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list &#8212;list all of the DN&#8217;s attribute,will not create AC extension;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/Role=yourRole &#8212; specify the role, if this DN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>has such a role, the role will be put into AC<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/voname/groupname/Role=yourRole &#8212; specify the vo,group and role if this DN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>has such a role, the role will be put into AC </dd>
<dt><code>-o</code></dt>
<dd> group&lt;:role&gt;. Specify ordering of attributes.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example: &#8211;order&nbsp;<wbr>/knowarc.eu/coredev:Developer,/knowarc.eu/testers:Tester<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or: &#8211;order&nbsp;<wbr>/knowarc.eu/coredev:Developer &#8211;order&nbsp;<wbr>/knowarc.eu/testers:Tester<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Note that it does not make sense to specify the order if you have two or more different VOMS server specified </dd>
<dt><code>-G</code></dt>
<dd> use GSI communication protocol for contacting VOMS services </dd>
<dt><code>-H</code></dt>
<dd> use HTTP communication protocol for contacting VOMS services that provide RESTful access<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Note for RESTful access,&nbsp;<wbr>&#8216;list&#8217;&nbsp;<wbr>command and multiple VOMS server are not supported </dd>
<dt><code>-O</code></dt>
<dd> use GSI proxy (RFC 3820 compliant proxy is default) </dd>
<dt><code>-I</code></dt>
<dd> print all information about this proxy.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>In order to show the Identity&nbsp;<wbr>(DN without CN as subfix for proxy)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the certificate, the&nbsp;<wbr>&#8216;trusted certdir&#8217;&nbsp;<wbr>is needed. </dd>
<dt><code>-i</code></dt>
<dd> print selected information about this proxy. Currently following information items are supported: </dd>
<p> <code>subject</code> &#8211; subject name of proxy certificate. </p>
<p> <code>identity</code> &#8211; identity subject name of proxy certificate. </p>
<p> <code>issuer</code> &#8211; issuer subject name of proxy certificate. </p>
<p> <code>ca</code> &#8211; subject name of CA which issued initial certificate. </p>
<p> <code>path</code> &#8211; file system path to file containing proxy. </p>
<p> <code>type</code> &#8211; type of proxy certificate. </p>
<p> <code>validityStart</code> &#8211; timestamp when proxy validity starts. </p>
<p> <code>validityEnd</code> &#8211; timestamp when proxy validity ends. </p>
<p> <code>validityPeriod</code> &#8211; duration of proxy validity in seconds. </p>
<p> <code>validityLeft</code> &#8211; duration of proxy validity left in seconds. </p>
<p> <code>vomsVO</code> &#8211; VO name represented by VOMS attribute. </p>
<p> <code>vomsSubject</code> &#8211; subject of certificate for which VOMS attribute is issued. </p>
<p> <code>vomsIssuer</code> &#8211; subject of service which issued VOMS certificate. </p>
<p> <code>vomsACvalidityStart</code> &#8211; timestamp when VOMS attribute validity starts. </p>
<p> <code>vomsACvalidityEnd</code> &#8211; timestamp when VOMS attribute validity ends. </p>
<p> <code>vomsACvalidityPeriod</code> &#8211; duration of VOMS attribute validity in seconds. </p>
<p> <code>vomsACvalidityLeft</code> &#8211; duration of VOMS attribute validity left in seconds. </p>
<p> <code>proxyPolicy</code> </p>
<p> <code>keybits</code> &#8211; size of proxy certificate key in bits. </p>
<p> <code>signingAlgorithm</code> &#8211; algorithm used to sign proxy certificate. </p>
<p> Items are printed in requested order and are separated by newline. If item has multiple values they are printed in same line separated by |. </p>
<dt><code>-r</code></dt>
<dd> Remove the proxy file. </dd>
<dt><code>-U</code></dt>
<dd> Username to myproxy server. </dd>
<dt><code>-N</code></dt>
<dd> don&#8217;t prompt for a credential passphrase, when retrieve a credential from on MyProxy server.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The precondition of this choice is the credential is PUT onto&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the MyProxy server without a passphrase by using -R&nbsp;<wbr>(&#8211;retrievable_by_cert)&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>option when being PUTing onto Myproxy server.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>This option is specific for the GET command when contacting Myproxy server. </dd>
<dt><code>-R</code></dt>
<dd> Allow specified entity to retrieve credential without passphrase.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>This option is specific for the PUT command when contacting Myproxy server. </dd>
<dt><code>-L</code></dt>
<dd> hostname of myproxy server optionally followed by colon and port number, e.g.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>example.org:7512. If the port number has not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>been specified, 7512 is used by default. </dd>
<dt><code>-M</code></dt>
<dd> command to myproxy server. The command can be PUT and GET.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PUT/put &#8212; put a delegated credential to myproxy server;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GET/get &#8212; get a delegated credential from myproxy server,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>credential&nbsp;<wbr>(certificate and key)&nbsp;<wbr>is not needed in this case;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>myproxy functionality can be used together with VOMS functionality.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>voms and vomses can be used for Get command if VOMS attributes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is required to be included in the proxy. </dd>
<dt><code>-F</code></dt>
<dd> use NSS credential DB in default Mozilla profiles, including Firefox, Seamonkey and Thunderbird. </dd>
<dt><code>-c</code></dt>
<dd> constraints of proxy certificate. Currently following constraints are supported: </dd>
<p> <code>validityStart=time</code> &#8211; time when certificate becomes valid. Default is now. </p>
<p> <code>validityEnd=time</code> &#8211; time when certificate becomes invalid. Default is 43200 (12 hours) from start for local proxy and 7 days for delegated to MyProxy. </p>
<p> <code>validityPeriod=time</code> &#8211; for how long certificate is valid. Default is 43200 (12 hours)for local proxy and 7 days for delegated to MyProxy. </p>
<p> <code>vomsACvalidityPeriod=time</code> &#8211; for how long the AC is valid. Default is shorter of validityPeriod and 12 hours. </p>
<p> <code>myproxyvalidityPeriod=time</code> &#8211; lifetime of proxies delegated by myproxy server. Default is shorter of validityPeriod and 12 hours. </p>
<p> <code>proxyPolicy=policy content</code> &#8211; assigns specified string to proxy policy to limit it&#8217;s functionality. </p>
<p> <code>keybits=number</code> &#8211; length of the key to generate. Default is 1024 bits. Special value &#8216;inherit&#8217; is to use key length of signing certificate. </p>
<p> <code>signingAlgorithm=name</code> &#8211; signing algorithm to use for signing public key of proxy. Default is sha1. Possible values are sha1, sha2 (alias for sha256), sha224, sha256, sha384, sha512 and inherit (use algorithm of signing certificate). </p>
<dt><code>-p</code></dt>
<dd> password destination=password source. Supported password destinations are: </dd>
<p> <code>key</code> &#8211; for reading private key </p>
<p> <code>myproxy</code> &#8211; for accessing credentials at MyProxy service </p>
<p> <code>myproxynew</code> &#8211; for creating credentials at MyProxy service </p>
<p> <code>all</code> &#8211; for any purspose. </p>
<p> Supported password sources are: </p>
<p> <code>quoted string (&quot;password&quot;)</code> &#8211; explicitly specified password </p>
<p> <code>int</code> &#8211; interactively request password from console </p>
<p> <code>stdin</code> &#8211; read password from standard input delimited by newline </p>
<p> <code>file:filename</code> &#8211; read password from file named filename </p>
<p> <code>stream:#</code> &#8211; read password from input stream number #. Currently only 0 (standard input) is supported. </p>
<dt><code>-t</code></dt>
<dd> timeout in seconds (default 20) </dd>
<dt><code>-z</code></dt>
<dd> configuration file (default ~/.arc/client.conf) </dd>
<dt><code>-d</code></dt>
<dd> level of information printed. Possible values are DEBUG, VERBOSE, INFO, WARNING, ERROR and FATAL. </dd>
<dt><code>-v</code></dt>
<dd> print version information </dd>
</dl>
<p> If location of certificate and key are not exlicitly specified they are looked for in following location and order: </p>
<p> Key/certificate paths specified by the environment variables X509_USER_KEY and X509_USER_CERT respectively. </p>
<p> Paths specified in configuration file. </p>
<p> ~/.arc/usercert.pem and ~/.arc/userkey.pem for certificate and key respectively. </p>
<p> ~/.globus/usercert.pem and ~/.globus/userkey.pem for certificate and key respectively. </p>
<p> If destination location of proxy file is not specified, the value of X509_USER_PROXY environment variable is used explicitly. If no value is provided, the default location is used &#8211; &lt;TEMPORARY DIRECTORY&gt;/x509up_u&lt;USER ID&gt;. Here TEMPORARY DIRECTORY is derived from environment variables TMPDIR, TMP, TEMP or default location /tmp is used. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.nordugrid.org/">http://bugzilla.nordugrid.org/</a> </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>ARC_LOCATION</code></dt>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </dd>
<dt><code>ARC_PLUGIN_PATH</code></dt>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/vomses</code></dt>
<dd> Common file containing a list of selected VO contact point, one VO per line, for example:</dd>
<dl>
<dl>
<dt>&quot;gin&quot; &quot;kuiken.nikhef.nl&quot; &quot;15050&quot; &quot;/O=dutchgrid/O=hosts/OU=nikhef.nl/CN=kuiken.nikhef.nl&quot; &quot;gin.ggf.org&quot;</dt>
<dd>
</dd><dt>&quot;nordugrid.org&quot; &quot;voms.uninett.no&quot; &quot;15015&quot; &quot;/O=Grid/O=NorduGrid/CN=host/voms.ndgf.org&quot; &quot;nordugrid.org&quot;</dt>
<dd></dd></dl>
</dl>
<dt><code>~/.voms/vomses</code></dt>
<dd> Same as <code>/etc/vomses</code> but located in user&#8217;s home area. If exists, has precedence over <code>/etc/vomses</code> </dd>
<dl>
<dt>
</dt><dd> The order of the parsing of vomses location is: </dd>
<dl>
<dt>
</dt><dd> 1. command line options</dd></dl>
<dl>
<dt>
</dt><dd> 2. client configuration file ~/.arc/client.conf</dd></dl>
<dl>
<dt>
</dt><dd> 3. $X509_VOMSES or $X509_VOMS_FILE</dd></dl>
<dl>
<dt>
</dt><dd> 4. ~/.arc/vomses</dd></dl>
<dl>
<dt>
</dt><dd> 5. ~/.voms/vomses</dd></dl>
<dl>
<dt>
</dt><dd> 6. $ARC_LOCATION/etc/vomses (this is for Windows environment)</dd></dl>
<dl>
<dt>
</dt><dd> 7. $ARC_LOCATION/etc/grid-security/vomses (this is for Windows environment)</dd></dl>
<dl>
<dt>
</dt><dd> 8. $PWD/vomses</dd></dl>
<dl>
<dt>
</dt><dd> 9. /etc/vomses</dd></dl>
<dl>
<dt>
</dt><dd> 10. /etc/grid-security/vomses</dd></dl>
</dl>
<dt><code>~/.arc/client.conf</code></dt>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </dd>
</dl>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
<h2>Index</h2>
