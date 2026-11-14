---
title: "pound(8)"
name: "pound"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pound/"
description: "pound – HTTP/HTTPS reverse-proxy and load-balancer"
---

<p>pound &#8211; HTTP/HTTPS reverse-proxy and load-balancer</p>
<h2>Synopsis</h2>
<dl>
<dt><code>pound</code></p>
<dd>[<i>-v</i>] [<i>-c</i>] [<i>-V</i>] [<i>-f config_file</i>] [<i>-p pid_file</i>]</dl>
<h2>Description</h2>
<p><code>Pound</code> is a reverse-proxy load balancing server. It accepts requests from HTTP/HTTPS clients and distributes them to one or more Web servers. The HTTPS requests are decrypted and passed to the back-ends as plain HTTP. </p>
<p> If more than one back-end server is defined, <code>Pound</code> chooses one of them randomly, based on defined priorities. By default, <code>Pound</code> keeps track of associations between clients and back-end servers (sessions).</p>
<h2>General Principles</h2>
<p>In general <code>Pound</code> needs three types of objects defined in order to function: <i>listeners</i>, <i>services</i> and <i>back-ends</i>.</p>
<dl>
<dt><code>Listeners</code></p>
<dd>A <i>listener</i> is a definition of how <code>Pound</code> receives requests from the clients (browsers). Two types of <i>listeners</i> may be defined: regular HTTP <i>listeners</i> and HTTPS (HTTP over SSL/TLS) <i>listeners</i>. At the very least a <i>listener</i> must define the address and port to listen on, with additional requirements for HTTPS <i>listeners</i>.</p>
<dt><code>Services</code></p>
<dd>A <i>service</i> is the definition of how the requests are answered. The <i>services</i> may be defined within a <i>listener</i> or at the top level (global). When a request is received <code>Pound</code> attempts to match them to each <i>service</i> in turn, starting with the <i>services</i> defined in the <i>listener</i> itself and, if needed, continuing with the <i>services</i> defined at the global level. The <i>services</i> may define their own conditions as to which requests they can answer: typically this involves certain URLs (images only, or a certain path) or specific headers (such as the Host header). A <i>service</i> may also define a <i>session</i> mechanism: if defined future requests from a given client will always be answered by the same <i>back-end</i>.</p>
<dt><code>Back-ends</code></p>
<dd>The <i>back-ends</i> are the actual servers for the content requested. By itself, <code>Pound</code> supplies no responses &#8211; all contents must be received from a &quot;real&quot; web server. The <i>back-end</i> defines how the server should be contacted.</p>
<dd>Three types of <i>back-ends</i> may be defined: a &quot;regular&quot; <i>back-end</i> which receives requests and returns responses, a &quot;redirect&quot; <i>back-end</i> in which case <code>Pound</code> will respond with a redirect response, without accessing any <i>back-end</i> at all, or an &quot;emergency&quot; <i>back-end</i> which will be used only if all other backends are &quot;dead&quot;.</p>
<dd>Multiple <i>back-ends</i> may be defined within a <i>service</i>, in which case <code>Pound</code> will load-balance between the available <i>back-ends</i>.</p>
<dd>If a <i>back-end</i> fails to respond it will be considered &quot;dead&quot;, in which case <code>Pound</code> will stop sending requests to it. Dead <i>back-ends</i> are periodically checked for availability, and once they respond again they are &quot;resurected&quot; and requests are sent again their way. If no <i>back-ends</i> are available (none were defined, or all are &quot;dead&quot;) then <code>Pound</code> will reply with &quot;503 Service Unavailable&quot;, without checking additional <i>services</i>.</p>
<dd>The connection between <code>Pound</code> and the <i>back-ends</i> is always via HTTP, regardless of the actual protocol used between <code>Pound</code> and the client.</dl>
<h2>Options</h2>
<p>Options available (see also below for configuration file options):</p>
<dl>
<dt><code>-v</code></p>
<dd>Verbose mode: error messages will be sent to stdout even if <code>Pound</code> was configured to log to syslog. This applies only to startup messages, before <code>Pound</code> puts itself in the background. Normal operational messages will still go to syslog.</p>
<dt><code>-V</code></p>
<dd>Print version: <code>Pound</code> will exit immediately after printing the current version and configuration flags.</p>
<dt><code>-c</code></p>
<dd>Check only: <code>Pound</code> will exit immediately after parsing the configuration file. This may be used for running a quick syntax check before actually activating a server.</p>
<dt><code>-f</code> config_file</p>
<dd>Location of the configuration file (see below for a full description of the format). Default: <i>/usr/local/etc/pound.cfg</i></p>
<dt><code>-p</code> pid_file</p>
<dd>Location of the pid file. <code>Pound</code> will write its own pid into this file. Normally this is used for shell scripts that control starting and stopping of the daemon. Default: <i>/var/run/pound.pid</i></dl>
<p> In general, any number of back-end servers may be specified. Use the priority to affect the load distribution among unequal-performance servers. </p>
<p> One (or more) copies of <code>Pound</code> should be started at boot time. Use &quot;big iron&quot; if you expect heavy loads: while <code>Pound</code> is as light-weight as I know how to make it, with a lot of simultaneous requests it will use quite a bit of CPU and memory. Multiple CPUs are your friend.</p>
<h2>Configuration File</h2>
<p>Each line in the file is considered a complete configuration directive. The directives are case-insensitive. Empty lines or lines starting in &#8216;#&#8217; are ignored. There are three types of directives: <code>global</code> directives (they affect the settings for the entire program instance), <code>listener</code> directives (they define which requests <code>Pound</code> will listen for), and <code>service</code> directives (they affect only a specific group of requests).</p>
<h2>Global Directives</h2>
<p>Global directives may appear anywhere within the configuration file, though it is customary for them to be at the start. They may appear in any order.</p>
<dl>
<dt><code>User</code> &quot;user_name&quot;</p>
<dd>Specify the user <code>Pound</code> will run as (must be defined in <i>/etc/passwd</i>).</p>
<dt><code>Group</code> &quot;group_name&quot;</p>
<dd>Specify the group <code>Pound</code> will run as (must be defined in <i>/etc/group</i>).</p>
<dt><code>RootJail</code> &quot;directory_path_and_name&quot;</p>
<dd>Specify the directory that <code>Pound</code> will chroot to at runtime. Please note that OpenSSL requires access to /dev/urandom, so make sure you create a device by that name, accessible from the root jail directory. <code>Pound</code> may also require access to <i>/dev/syslog</i> or similar.</p>
<dt><code>Daemon</code> 0|1</p>
<dd>Have <code>Pound</code> run in the foreground (if 0) or as a daemon (if 1). By default <code>Pound</code> runs as a daemon (detaches itself from the controlling terminal and puts itself in the background). By specifying this option you can force <code>Pound</code> to work like a regular process. Useful for debugging or if you want to use something like <i>daemontools</i>.</p>
<dt><code>Threads</code> nnn</p>
<dd>How many worker threads <code>Pound</code> should use. Default: 128. Tune this parameter to improve performance. If you set it too high, <code>Pound</code> will use a lot memory, and some CPU will be wasted on context switches. If you set it too low requests may be served with some delay. Experiment to find the optimal value for your installation.</p>
<dt><code>LogFacility</code> value</p>
<dd>Specify the log facility to use. <i>value</i> (default: daemon) must be one of the symbolic facility names defined in <i>syslog.h</i>. This facility shall be used for logging. Using a &#8211; for the facility name causes <code>Pound</code> to log to stdout/stderr.</p>
<dt><code>LogLevel</code> value</p>
<dd>Specify the logging level: 0 for no logging, 1 (default) for regular logging, 2 for extended logging (show chosen backend server as well), 3 for Apache-like format (Combined Log Format with Virtual Host), 4 (same as 3 but without the virtual host information) and 5 (same as 4 but with information about the <i>Service</i> and <i>BackEnd</i> used). This value can be overridden for specific listeners.</p>
<dt><code>IgnoreCase</code> 0|1</p>
<dd>Ignore case when matching URLs (default: 0). This value can be overridden for specific services.</p>
<dt><code>DynScale</code> 0|1</p>
<dd>Enable or disable the dynamic rescaling code (default: 0). If enabled <code>Pound</code> will periodically try to modify the back-end priorities in order to equalise the response times from the various back-ends. This value can be overridden for specific services.</p>
<dt><code>Alive</code> value</p>
<dd>Specify how often <code>Pound</code> will check for resurected back-end hosts (default: 30 seconds). In general, it is a good idea to set this as low as possible &#8211; it will find resurected hosts faster. However, if you set it too low it will consume resources &#8211; so beware.</p>
<dt><code>Client</code> value</p>
<dd>Specify for how long <code>Pound</code> will wait for a client request (default: 10 seconds). After this long has passed without the client sending any data <code>Pound</code> will close the connection. Set it higher if your clients time-out on a slow network or over-loaded server, lower if you start getting DOS attacks or run into problems with IE clients. This value can be overridden for specific listeners.</p>
<dt><code>TimeOut</code> value</p>
<dd>How long should <code>Pound</code> wait for a response from the back-end (in seconds). Default: 15 seconds. This value can be overridden for specific back-ends.</p>
<dt><code>ConnTO</code> value</p>
<dd>How long should <code>Pound</code> wait for a connection to the back-end (in seconds). Default: the <code>TimeOut</code> value. This value can be overridden for specific back-ends.</p>
<dt><code>Grace</code> value</p>
<dd>How long should <code>Pound</code> continue to answer existing connections after a receiving and INT or HUP signal (default: 30 seconds). The configured listeners are closed immediately. You can bypass this behaviour by stopping <code>Pound</code> with a TERM or QUIT signal, in which case the program exits without any delay.</p>
<dt><code>SSLEngine</code> &quot;name&quot;</p>
<dd>Use an OpenSSL hardware acceleration card called <i>name</i>. Available only if OpenSSL-engine is installed on your system.</p>
<dt><code>ECDHcurve</code> &quot;name&quot;</p>
<dd>Use the named curve for elliptical curve encryption (default: prime256v1).</p>
<dt><code>Control</code> &quot;/path/to/socket&quot;</p>
<dd>Set the control socket path. If not defined <code>Pound</code> does not listen for any commands. The commands may be issued by using the <i><a href="/docs/linux/man/8-poundctl/">poundctl</a>(8)</i> program.</p>
<dt><code>Include</code> &quot;/path/to/file&quot;</p>
<dd>Include the file as though it were part of the configuration file.</p>
<dt><code>Anonymise</code></p>
<dd>Replace the last byte of the client address with 0 for logging purposes. Default: log the client address in full.</dl>
<h2>HTTP Listener</h2>
<p>An HTTP listener defines an address and port that <code>Pound</code> will listen on for HTTP requests. All configuration directives enclosed between <i>ListenHTTP</i> and <i>End</i> are specific to a single HTTP listener. At the very least you must specify and address and a port for each listener. The following directives are available:</p>
<dl>
<dt><code>Address</code> address</p>
<dd>The address that <code>Pound</code> will listen on. This can be a numeric IP address, or a symbolic host name that must be resolvable at run-time. This is a <code>mandatory</code> parameter. The address 0.0.0.0 may be used as an alias for &#8216;all available addresses on this machine&#8217;, but this practice is strongly discouraged, as it will interfere with the rewriting mechanisms (see below).</p>
<dt><code>Port</code> port</p>
<dd>The port number that <code>Pound</code> will listen on. This is a <code>mandatory</code> parameter.</p>
<dt><code>xHTTP</code> value</p>
<dd>Defines which HTTP verbs are accepted. The possible values are:</p>
<dd><i>0</i> (default) accept only standard HTTP requests (GET, POST, HEAD).</p>
<dd><i>1</i> additionally allow extended HTTP requests (PUT, PATCH, DELETE).</p>
<dd><i>2</i> additionally allow standard WebDAV verbs (LOCK, UNLOCK, PROPFIND, PROPPATCH, SEARCH, MKCOL, MOVE, COPY, OPTIONS, TRACE, MKACTIVITY, CHECKOUT, MERGE, REPORT).</p>
<dd><i>3</i> additionally allow MS extensions WebDAV verbs (SUBSCRIBE, UNSUBSCRIBE, NOTIFY, BPROPFIND, BPROPPATCH, POLL, BMOVE, BCOPY, BDELETE, CONNECT).</p>
<dd><i>4</i> additionally allow MS RPC extensions verbs (RPC_IN_DATA, RPC_OUT_DATA).</p>
<dt><code>Client</code> value</p>
<dd>Override the global <i>Client</i> time-out value.</p>
<dt><code>CheckURL</code> &quot;pattern to match&quot;</p>
<dd>Define a pattern that must be matched by each request sent to this listener. A request that does not match is considered to be illegal. By default <code>Pound</code> accepts all requests (i.e. the pattern is &quot;.*&quot;), but you are free to limit it to something more reasonable. Please note that this applies only to the request path &#8211; <code>Pound</code> will still check that the request is syntactically correct.</p>
<dt><code>Err414</code> &quot;filename&quot;</p>
<dd>A file with the text to be displayed if an Error 414 occurs. Default: &quot;Request URI is too long.&quot;.</p>
<dt><code>Err500</code> &quot;filename&quot;</p>
<dd>A file with the text to be displayed if an Error 500 occurs. Default: &quot;An internal server error occurred. Please try again later.&quot;.</p>
<dt><code>Err501</code> &quot;filename&quot;</p>
<dd>A file with the text to be displayed if an Error 501 occurs. Default: &quot;This method may not be used.&quot;.</p>
<dt><code>Err503</code> &quot;filename&quot;</p>
<dd>A file with the text to be displayed if an Error 503 occurs. Default: &quot;The service is not available. Please try again later.&quot;.</p>
<dt><code>MaxRequest</code> nnn</p>
<dd>Request maximal size. All requests will be limited to these many bytes. If a request contains more data than allowed an error 414 is returned. Default: unlimited.</p>
<dt><code>HeadRemove</code> &quot;header pattern&quot;</p>
<dd>Remove certain headers from the incoming requests. All occurences of the matching specified header will be removed. Please note that this filtering is done prior to other checks (such as <i>HeadRequire</i> or <i>HeadDeny</i>), so you should not try to check for these headers in later matches. Multiple directives may be specified in order to remove more than one header, and the header itself may be a regular pattern (though this should be used with caution).</p>
<dt><code>AddHeader</code> &quot;header: to add&quot;</p>
<dd>Add the defined header to the request passed to the back-end server. The header is added verbatim. Use multiple <i>AddHeader</i> directives if you need to add more than one header.</p>
<dt><code>RewriteLocation</code> 0|1|2</p>
<dd>If 1 force <code>Pound</code> to change the Location: and Content-location: headers in responses. If they point to the back-end itself or to the listener (but with the wrong protocol) the response will be changed to show the virtual host in the request. Default: 1 (active). If the value is set to 2 only the back-end address is compared; this is useful for redirecting a request to an HTTPS listener on the same server as the HTTP listener.</p>
<dt><code>RewriteDestination</code> 0|1</p>
<dd>If 1 force <code>Pound</code> to change the Destination: header in requests. The header is changed to point to the back-end itself with the correct protocol. Default: 0.</p>
<dt><code>LogLevel</code> value</p>
<dd>Override the global <i>LogLevel</i> value.</p>
<dt><code>Service</code> [ &quot;name&quot; ]</p>
<dd>This defines a private service (see below for service definition syntax). This service will be used only by this listener. The service may be optionally named, with the name showing in the <i>poundctl</i> listings.</dl>
<h2>HTTPS Listener</h2>
<p>An HTTPS listener defines an address and port that <code>Pound</code> will listen on for HTTPS requests. All configuration directives enclosed between <i>ListenHTTPS</i> and <i>End</i> are specific to a single HTTPS listener. At the very least you must specify and address, a port and a server certificate for each listener. All directives defined for HTTP listeners are applicable to HTTPS listeners as well. The following additional directives are also available:</p>
<dl>
<dt><code>Cert</code> &quot;certificate file&quot;</p>
<dd>Specify the server certificate. The <i>certificate file</i> is the file containing the certificate, possibly a certificate chain and the signature for this server. This directive is <code>mandatory</code> for HTTPS listeners.</p>
<dd>Please note that multiple <i>Cert</i> directives are allowed if your OpenSSL version supports SNI. In such cases, the first directive is the default certificate, with additional certificates used if the client requests them.</p>
<dd>The ordering of the directives is important: the first certificate where the CN matches the client request will be used, so put your directives in the most-specific-to-least specific order (i.e. wildcard certificates <code>after</code> host-specific certificates).</p>
<dd><i>Cert</i> directives <code>must</code> precede all other SSL-specific directives.</p>
<dt><code>ClientCert</code> 0|1|2|3 depth</p>
<dd>Ask for the client&#8217;s HTTPS certificate: 0 &#8211; don&#8217;t ask (default), 1 &#8211; ask, 2 &#8211; ask and fail if no certificate was presented, 3 &#8211; ask but do not verify. <i>Depth</i> is the depth of verification for a client certificate (up to 9). The default depth limit is 9, allowing for the peer certificate and additional 9 CA certificates that must be verified.</p>
<dt><code>Disable</code> SSLv2|SSLv3|TLSv1|TLSv1_1|TLSv1_2</p>
<dd>Disable the protocol <code>and all lower protocols as well</code>. This is due to a limitation in OpenSSL, which does not support disabling a single protocol. For example, <i>Disable TLSv1</i> would disable SSLv2, SSLv3 and TLSv1, thus allowing only TLSv1_1 and TLSv1_2.</p>
<dt><code>Ciphers</code> &quot;acceptable:cipher:list&quot;</p>
<dd>This is the list of ciphers that will be accepted by the SSL connection; it is a string in the same format as in OpenSSL <i><a href="/docs/linux/man/1-ciphers/">ciphers</a>(1)</i> and <i><a href="/docs/linux/man/3-ssl_ctx_set_cipher_list/">SSL_CTX_set_cipher_list</a>(3).</i></p>
<dt><code>SSLHonorCipherOrder</code> 0|1</p>
<dd>If this value is 1, the server will broadcast a preference to use <code>Ciphers</code> in the order supplied in the <code>Ciphers</code> directive. If the value is 0, the server will treat the Ciphers list as the list of Ciphers it will accept, but no preference will be indicated. Default value is 0.</p>
<dt><code>SSLAllowClientRenegotiation</code> 0|1|2</p>
<dd>If this value is 0, client initiated renegotiation will be disabled. This will mitigate DoS exploits based on client renegotiation, regardless of the patch status of clients and servers related to &quot;Secure renegotiation&quot;. If the value is 1, secure renegotiation is supported. If the value is 2, insecure renegotiation is supported, with unpatched clients. <code>This can lead to a DoS and a Man in the Middle attack!</code> The default value is 0.</p>
<dt><code>CAlist</code> &quot;CAcert_file&quot;</p>
<dd>Set the list of &quot;trusted&quot; CA&#8217;s for this server. The CAcert_file is a file containing a sequence of CA certificates (PEM format). The names of the defined CA certificates will be sent to the client on connection.</p>
<dt><code>VerifyList</code> &quot;Verify_file&quot;</p>
<dd>Set the CA (Certificate Authority). The Verify_file is a file that contains the CA root certificates (in PEM format).</p>
<dd><i>Please note:</i> there is an important difference between the CAlist and the VerifyList. The CAlist tells the client (browser) which client certificates it should send. The VerifyList defines which CAs are actually used for the verification of the returned certificate.</p>
<dt><code>CRLlist</code> &quot;CRL_file&quot;</p>
<dd>Set the CRL (Certificate Revocation List) file. The CRL_file is a file that contains the CRLs (in PEM format).</p>
<dt><code>NoHTTPS11</code> 0|1|2</p>
<dd>Behave like an HTTP/1.0 server for HTTPS clients. If this value is 0 disable the check. If the value is 1 do not allow multiple requests on SSL connections. If the value is 2 (default) disable multiple requests on SSL connections only for MSIE clients. Required work-around for a bug in certain versions of IE.</dl>
<h2>Service</h2>
<p>A service is a definition of which back-end servers <code>Pound</code> will use to reply to incoming requests. A service may be defined as part of a listener (in which case it will be used only by that listener), or globally (which makes it available to all listeners). <code>Pound</code> will always try the private services in the order defined, followed by the global ones. </p>
<p> All configuration directives enclosed between <i>Service</i> and <i>End</i> are specific to a single service. The following directives are available:</p>
<dl>
<dt><code>URL</code> &quot;pattern&quot;</p>
<dd>Match the incoming request. If a request fails to match than this service will be skipped and next one tried. If all services fail to match <code>Pound</code> returns an error. You may define multiple <i>URL</i> conditions per service, in which case <code>all</code> patterns must match. If no <i>URL</i> was defined then all requests match. The matching is by default case-sensitive, but this can be overridden by specifying <code>IgnoreCase 1</code></p>
<dt><code>IgnoreCase</code> 0|1</p>
<dd>Override the global <code>IgnoreCase</code> setting.</p>
<dt><code>HeadRequire</code> &quot;pattern&quot;</p>
<dd>The request must contain at least on header matching the given pattern. Multiple <i>HeadRequire</i> directives may be defined per service, in which case all of them must be satisfied.</p>
<dt><code>HeadDeny</code> &quot;pattern&quot;</p>
<dd>The request may <code>not</code> contain any header matching the given pattern. Multiple <i>HeadDeny</i> directives may be defined per service, in which case all of them must be satisfied.</p>
<dd><i>Please note:</i> if the listener defined a <i>HeadRemove</i> directive, the matching headers are removed <code>before</code> the service matching is attempted.</p>
<dt><code>DynScale</code> 0|1</p>
<dd>Enable or disable dynamic rescaling for the current service. This value will override the value globally defined.</p>
<dt><code>Disabled</code> 0|1</p>
<dd>Start <code>Pound</code> with this service disabled (1) or enabled (0). If started as disabled, the service can be later enabled with <i>poundctl</i> (8).</p>
<dt><code>BackEnd</code></p>
<dd>Directives enclosed between a <i>BackEnd</i> and the following <i>End</i> directives define a single back-end server (see below for details). You may define multiple back-ends per service, in which case <code>Pound</code> will attempt to load-balance between them.</p>
<dt><code>Redirect</code> [code] &quot;url&quot;</p>
<dd>This is a special type of back-end. Instead of sending the request to a back-end <code>Pound</code> replies immediately with a redirection to the given URL. You may define multiple redirectors in a service, as well as mixing them with regular back-ends.</p>
<dd>The address the client is redirected to is determined by the actual <i>url</i> you specify: if it is a &quot;pure&quot; host (i.e. with no path) then the client will be redirected to the host you specified, with the original request path appended. If your <i>url</i> does contain a path then the request path is ignored.</p>
<dd>Examples: if you specified </p>
<p>&nbsp;<wbr>Redirect&nbsp;<wbr>&quot;<a rel="nofollow" href="http://abc.example">http://abc.example</a>&quot; </p>
<p> and the client requested <i><a rel="nofollow" href="http://xyz/a/b/c">http://xyz/a/b/c</a></i> then it will be redirected to <i><a rel="nofollow" href="http://abc.example/a/b/c,">http://abc.example/a/b/c,</a></i> but if you specified </p>
<p>&nbsp;<wbr>Redirect&nbsp;<wbr>&quot;<a rel="nofollow" href="http://abc.example/index.html">http://abc.example/index.html</a>&quot; </p>
<p> it will be sent to <i><a rel="nofollow" href="http://abc.example/index.html.">http://abc.example/index.html.</a></i></p>
<dd><i>Technical note:</i> in an ideal world <code>Pound</code> should reply with a &quot;307 Temporary Redirect&quot; status. Unfortunately, that is not yet supported by all clients (in particular HTTP 1.0 ones), so <code>Pound</code> currently replies by default with a &quot;302 Found&quot; instead. You may override this behaviour by specifying the code to be used (301, 302 or 307).</p>
<dt><code>Emergency</code></p>
<dd>Directives enclosed between an <i>Emergency</i> and the following <i>End</i> directives define an emergency back-end server (see below for details). You may define only one emergency server per service, which <code>Pound</code> will attempt to use if all backends are down.</p>
<dt><code>Session</code></p>
<dd>Directives enclosed between a <i>Session</i> and the following <i>End</i> directives define a session-tracking mechanism for the current service. See below for details.</dl>
<h2>BackEnd</h2>
<p>A back-end is a definition of a single back-end server <code>Pound</code> will use to reply to incoming requests. All configuration directives enclosed between <i>BackEnd</i> and <i>End</i> are specific to a single service. The following directives are available:</p>
<dl>
<dt><code>Address</code> address</p>
<dd>The address that <code>Pound</code> will connect to. This can be a numeric IP address, or a symbolic host name that must be resolvable at run-time. If the name cannot be resolved to a valid address, <code>Pound</code> will assume that it represents the path for a Unix-domain socket. This is a <code>mandatory</code> parameter.</p>
<dt><code>Port</code> port</p>
<dd>The port number that <code>Pound</code> will connect to. This is a <code>mandatory</code> parameter for non Unix-domain back-ends.</p>
<dt><code>HTTPS</code></p>
<dd>The back-end is using HTTPS.</p>
<dt><code>Cert</code> &quot;certificate file&quot;</p>
<dd>Specify the certificate that <code>Pound</code> will use as a client. The <i>certificate file</i> is the file containing the certificate, possibly a certificate chain and the signature. This directive may appear only after the <i>HTTPS</i> directive.</p>
<dt><code>Disable</code> SSLv2|SSLv3|TLSv1|TLSv1_1|TLSv1_2</p>
<dd>Disable the protocol <code>and all lower protocols as well</code>. This is due to a limitation in OpenSSL, which does not support disabling a single protocol. For example, <i>Disable TLSv1</i> would disable SSLv2, SSLv3 and TLSv1, thus allowing only TLSv1_1 and TLSv1_2. This directive may appear only after the <i>HTTPS</i> directive.</p>
<dt><code>Ciphers</code> &quot;acceptable:cipher:list&quot;</p>
<dd>This is the list of ciphers that will be accepted by the SSL connection; it is a string in the same format as in OpenSSL <i><a href="/docs/linux/man/1-ciphers/">ciphers</a>(1)</i> and <i><a href="/docs/linux/man/3-ssl_ctx_set_cipher_list/">SSL_CTX_set_cipher_list</a>(3).</i> This directive may appear only after the <i>HTTPS</i> directive.</p>
<dt><code>Priority</code> val</p>
<dd>The priority of this back-end (between 1 and 9, 5 is default). Higher priority back-ends will be used more often than lower priority ones, so you should define higher priorities for more capable servers.</p>
<dt><code>TimeOut</code> val</p>
<dd>Override the global <i>TimeOut</i> value.</p>
<dt><code>ConnTO</code> val</p>
<dd>Override the global <i>ConnTO</i> value.</p>
<dt><code>HAport</code> [ address ] port</p>
<dd>A port (and optional address) to be used for server function checks. See below the &quot;High Availability&quot; section for a more detailed discussion. By default <code>Pound</code> uses the same address as the back-end server, but you may use a separate address if you wish. This directive applies only to non Unix-domain servers.</p>
<dt><code>Disabled</code> 0|1</p>
<dd>Start <code>Pound</code> with this back-end disabled (1) or enabled (0). If started as disabled, the back-end can be later enabled with <i>poundctl</i> (8).</dl>
<h2>Emergency</h2>
<p>The emergency server will be used once all existing back-ends are &quot;dead&quot;. All configuration directives enclosed between <i>Emergency</i> and <i>End</i> are specific to a single service. The following directives are available:</p>
<dl>
<dt><code>Address</code> address</p>
<dd>The address that <code>Pound</code> will connect to. This can be a numeric IP address, or a symbolic host name that must be resolvable at run-time. If the name cannot be resolved to a valid address, <code>Pound</code> will assume that it represents the path for a Unix-domain socket. This is a <code>mandatory</code> parameter.</p>
<dt><code>Port</code> port</p>
<dd>The port number that <code>Pound</code> will connect to. This is a <code>mandatory</code> parameter for non Unix-domain back-ends.</dl>
<h2>Session</h2>
<p>Defines how a service deals with possible HTTP sessions. All configuration directives enclosed between <i>Session</i> and <i>End</i> are specific to a single service. Once a sessions is identified, <code>Pound</code> will attempt to send all requests within that session to the same back-end server. </p>
<p> The following directives are available:</p>
<dl>
<dt><code>Type</code> IP|BASIC|URL|PARM|COOKIE|HEADER</p>
<dd>What kind of sessions are we looking for: IP (the client address), BASIC (basic authentication), URL (a request parameter), PARM (a URI parameter), COOKIE (a certain cookie), or HEADER (a certain request header). This is a <code>mandatory</code> parameter.</p>
<dt><code>TTL</code> seconds</p>
<dd>How long can a session be idle (in seconds). A session that has been idle for longer than the specified number of seconds will be discarded. This is a <code>mandatory</code> parameter.</p>
<dt><code>ID</code> &quot;name&quot;</p>
<dd>The session identifier. This directive is permitted only for sessions of type URL (the name of the request parameter we need to track), COOKIE (the name of the cookie) and HEADER (the header name).</dl>
<p> See below for some examples.</p>
<h2>High-Availability</h2>
<p><code>Pound</code> attempts to keep track of active back-end servers, and will temporarily disable servers that do not respond (though not necessarily dead: an overloaded server that <code>Pound</code> cannot establish a connection to will be considered dead). However, every <i>Alive</i> seconds, an attempt is made to connect to the dead servers in case they have become active again. If this attempt succeeds, connections will be initiated to them again. </p>
<p> In general it is a good idea to set this time interval as low as is consistent with your resources in order to benefit from resurected servers at the earliest possible time. The default value of 30 seconds is probably a good choice. </p>
<p> The clients that happen upon a dead backend server will just receive a <i>503 Service Unavailable</i> message. </p>
<p> The <i>HAport</i> parameter specifies an additional port (and optionally an address) that is used only for viability checks: if this port is specified in a <i>BackEnd</i> directive, <code>Pound</code> will attempt periodically (every <i>Alive</i> seconds) to connect to this port. If the port does not respond the server is considered dead. <code>It never makes sense to have the</code> <i>HAport</i> <code>identical to the main back-end port:</code> this would only generate extra, unncecessary activity (CPU, network traffic) for no good reason whatsoever. The <i>HAport</i> is meant for applications that offer an additional health monitoring port or for installations that wish to take servers off-line in a controlled manner. </p>
<p> By default the address of the <i>HAport</i> health monitor is the same as that of the back-end server. You may specify a different address though, for example if you have a monitoring program running on another host.</p>
<h2>Https Headers</h2>
<p>If a client browser connects to <code>Pound</code> via HTTPS and if it presents a client certificate <code>Pound</code> adds the following headers to the request it issues to the server:</p>
<dl>
<dt><code>X-SSL-Subject</code></p>
<dd>Details about the certificate owner.</p>
<dt><code>X-SSL-Issuer</code></p>
<dd>Details about the certificate issuer (Certificate Authority).</p>
<dt><code>X-SSL-notBefore</code></p>
<dd>Starting date of certificate validity.</p>
<dt><code>X-SSL-notAfter</code></p>
<dd>Ending date of certificate validity.</p>
<dt><code>X-SSL-serial</code></p>
<dd>Certificate serial number (decimal).</p>
<dt><code>X-SSL-cipher</code></p>
<dd>The cipher currently in use.</p>
<dt><code>X-SSL-certificate</code></p>
<dd>The full client certificate (PEM-format multi-line)</dl>
<p> It is the application&#8217;s responsibility to actually use these headers &#8211; Pound just passes this information without checking it in any way (except for signature and encryption correctness).</p>
<h2>Security</h2>
<p>In general, <code>Pound</code> does not read or write to the hard-disk. The exceptions are reading the configuration file and (possibly) the server certificate file(s) and error message(s), which are opened read-only on startup, read, and closed, and the pid file which is opened on start-up, written to and immediately closed. Following this there is no disk access whatsoever, so using a RootJail directive is only for extra security bonus points. </p>
<p> <code>Pound</code> tries to sanitise all HTTP/HTTPS requests: the request itself, the headers and the contents are checked for conformance to the RFC&#8217;s and only valid requests are passed to the back-end servers. This is not absolutely fool-proof &#8211; as the recent Apache problem with chunked transfers demonstrated. However, given the current standards, this is the best that can be done &#8211; HTTP is an inherently weak protocol.</p>
<h2>Additional Notes</h2>
<p><code>Pound</code> uses the system log for messages (default facility LOG_DAEMON). The format is very similar to other web servers, so that if you want to use a log tool:</p>
<dl>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fgrep pound&nbsp;<wbr>/var/log/messages | your_log_tool</p>
<dd></dl>
<p> Translating HTTPS to HTTP is an iffy proposition: no client information is passed to the server itself (certificates, etc) and the backend server may be misled if it uses absolute URLs. A patch for <i>Zope</i> is included in the distribution to address this issue &#8211; for other Web servers you are on your own. May the source be with you. </p>
<p> <code>Pound</code> deals with (and sanitizes) HTTP/1.1 requests. Thus even if you have an HTTP/1.0 server, a single connection to an HTTP/1.1 client is kept, while the connection to the back-end server is re-opened as necessary. </p>
<p> <code>Pound</code> attempts to resolve the names of the hosts that appear in various requests and/or responses. That means it need a functioning resolver of some kind (be it /etc/hosts, DNS or something else).</p>
<h2>Examples</h2>
<p>To translate HTTPS requests to a local HTTP server (assuming your network address is 123.123.123.123):</p>
<dl>
<dd>ListenHTTPS </p>
<p>&nbsp;<wbr>Address 1.2.3.4 </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>443 </p>
<p>&nbsp;<wbr>Cert&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;/etc/pound/server.pem&quot; </p>
<p>&nbsp;<wbr>Service </p>
<p>&nbsp;<wbr>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Address 127.0.0.1 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>End<br />
 End</dl>
<p> To distribute the HTTP/HTTPS requests to three Web servers, where the third one is a newer and faster machine:</p>
<dl>
<dd>ListenHTTP </p>
<p>&nbsp;<wbr>Address 123.123.123.123 </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80<br />
 End<br />
 ListenHTTPS </p>
<p>&nbsp;<wbr>Address 1.2.3.4 </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>443 </p>
<p>&nbsp;<wbr>Cert&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;/etc/pound/server.pem&quot;<br />
 End </p>
<p> Service </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.10 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.11 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.12 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Priority 3 </p>
<p>&nbsp;<wbr>End<br />
 End</dl>
<p> To separate between image requests and other Web content and send all requests for a specific URL to a secure server:</p>
<dl>
<dd>ListenHTTP </p>
<p>&nbsp;<wbr>Address 123.123.123.123 </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80<br />
 End </p>
<p> # Images server(s)<br />
 Service </p>
<p>&nbsp;<wbr>URL&nbsp;<wbr>&quot;.*.(jpg|gif)&quot; </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.12 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>End<br />
 End </p>
<p> # redirect all requests for /forbidden<br />
 Service </p>
<p>&nbsp;<wbr>Url&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;/forbidden.*&quot; </p>
<p>&nbsp;<wbr>Redirect&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;<a rel="nofollow" href="https://xyzzy.com">https://xyzzy.com</a>&quot;<br />
 End </p>
<p> # Catch-all server(s)<br />
 Service </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.10 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.11 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>Session </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>BASIC </p>
<p>&nbsp;<wbr>&nbsp;<wbr>TTL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>300 </p>
<p>&nbsp;<wbr>End<br />
 End</dl>
<p> Here is a more complex example: assume your static images (GIF/JPEG) are to be served from a single back-end 192.168.0.10. In addition, 192.168.0.11 is to do the hosting for <a rel="nofollow" href="http://www.myserver.com">www.myserver.com</a> with URL-based sessions, and 192.168.0.20 (a 1GHz PIII) and 192.168.0.21 (800Mhz Duron) are for all other requests (cookie-based sessions). The logging will be done by the back-end servers. The configuration file may look like this:</p>
<dl>
<dd>User &quot;nobody&quot;<br />
 Group &quot;nogroup&quot;<br />
 RootJail &quot;/var/pound/jail&quot;<br />
 Alive 60<br />
 LogLevel 0 </p>
<p> # Main listening ports<br />
 ListenHTTP </p>
<p>&nbsp;<wbr>Address 1.2.3.4 </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>Client&nbsp;<wbr>&nbsp;<wbr>10<br />
 End<br />
 ListenHTTPS </p>
<p>&nbsp;<wbr>Address 1.2.3.4 </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>443 </p>
<p>&nbsp;<wbr>Cert&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;/etc/pound/pound.pem&quot; </p>
<p>&nbsp;<wbr>Client&nbsp;<wbr>&nbsp;<wbr>20<br />
 End </p>
<p> # Image server<br />
 Service </p>
<p>&nbsp;<wbr>URL&nbsp;<wbr>&quot;.*.(jpg|gif)&quot; </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.10 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>End<br />
 End </p>
<pre><code># Virtual host www.myserver.com

Service


URL         &quot;.*sessid=.*&quot;


HeadRequire &quot;Host:.*www.myserver.com.*&quot;


BackEnd

Address 192.168.0.11

Port    80


End


Session

Type    URL

ID      &quot;sessid&quot;

TTL     120


End

End</code></pre>
<p> # Everybody else<br />
 Service </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.20 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Priority 5 </p>
<p>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>BackEnd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Address 192.168.0.21 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Priority 4 </p>
<p>&nbsp;<wbr>End </p>
<p>&nbsp;<wbr>Session </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>COOKIE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;userid&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>TTL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>180 </p>
<p>&nbsp;<wbr>End<br />
 End
</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/run/pound.nnn</i></p>
<dd>this is where <code>Pound</code> will attempt to record its process id.</p>
<dt><i>/usr/local/etc/pound.cfg</i></p>
<dd>the default configuration file (the location may be changed when compiling &#8211; see the F_CONF flag in the Makefile).</p>
<dt><i>/usr/local/etc/pound/cert.pem</i></p>
<dd>the certificate file(s) for HTTPS. The location must be defined in the configuration file &#8211; this is only a suggestion. The file must contain a PEM-encoded certificate, optionally a certificate chain from a known Certificate Authority to your server certificate and a PEM-encoded private key (not password protected). See <i><a href="/docs/linux/man/1-openssl/">OpenSSL</a>(1)</i> for details. This file should be well protected, lest someone gets your server private key.</dl>
<h2>Author</h2>
<p>Written by Robert Segall, Apsis GmbH.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;roseg [at] apsis.ch&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2010 Apsis GmbH.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
