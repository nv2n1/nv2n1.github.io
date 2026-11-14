---
title: "yaws-conf(5)"
name: "yaws-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yaws-conf/"
description: "/etc/yaws/yaws.conf – Configuration file for the Yaws web server"
---

<p>/etc/yaws/yaws.conf &#8211; Configuration file for the Yaws web server</p>
<h2>Description</h2>
<p>Yaws is fast lightweight web server. It reads a configuration file called yaws.conf to control its operations. The configuration contains two distinct parts a global part which affects all the virtual hosts and a server part where options for each virtual host is supplied. </p>
<h2>Global Part</h2>
<dl>
<dt><code>logdir = [+]Directory</code></p>
<dd>All Yaws logs will be written to files in this directory. If specified with <code>+</code>, Yaws will attempt to create the directory if it does not exist. There are several different log files written by Yaws: </p>
<p> <code>report.log</code> &#8211; this is a text file that contains all error logger printouts from Yaws. </p>
<p> <code>&lt;Host&gt;.access</code> &#8211; for each virtual host served by Yaws, a file &lt;Host&gt;.access will be written which contains an access log in Common Log Format. (See <a rel="nofollow" href="http://en.wikipedia.org/wiki/Common_Log_Format">http://en.wikipedia.org/wiki/Common_Log_Format</a> for more details on Common Log Format.) </p>
<p> <code>&lt;Host&gt;.auth</code> &#8211; for each virtual host served by Yaws, a file &lt;Host&gt;.auth will be written which contains all http auth related messages. </p>
<p> <code>trace_&lt;YYYYMMDD_hhmmss&gt;</code> &#8211; Trace files are written in this subdirectory, suffixed by the creation date. </p>
<dl>
<dd><code>trace.&lt;Pid&gt;.http</code> &#8211; this file contains the HTTP trace if that is enabled, where &lt;Pid&gt; is the process id handling the TCP connection. </p>
<p> <code>trace.&lt;Pid&gt;.traffic</code> &#8211; this file contains the traffic trace if that is enabled, where &lt;Pid&gt; is the process id handling the TCP connection.</dl>
<dd>Note that &lt;Host&gt;.access and &lt;Host&gt;.auth files will be used only if the directive <code>logger_mod</code> is not set or set to yaws_log. The default value for logdir is <i>&quot;.&quot;</i> </p>
<dt><code>ebin_dir = Directory</code></p>
<dd>This directive adds Directory to the Erlang search path. It is possible to have several of these commands in the configuration file. The default value is <i>&quot;yaws_dir&quot;/examples/ebin</i> </p>
<dt><code>src_dir = Directory</code></p>
<dd>This directive defines a Directory as a <i>source</i> directory. Yaws will compile all erlang modules found in this directory and all its subdirectories. The compilation occurs when the configuration is loaded or reloaded. The <code>include_dir</code> directives are used to search for includes files. Multiple <code>src_dir</code> directives may be used. There is no such directory configured by default. </p>
<dt><code>id = String</code></p>
<dd>It is possible run multiple Yaws servers on the same machine. We use the id of a Yaws server to control it using the different control commands such as: </p>
<pre> # /usr/local/bin/yaws --id foobar --stop</pre>
<p>To stop the Yaws server with id &quot;foobar&quot;. Each Yaws server will write its internals data into a file called $HOME/.yaws/yaws/ID where ID is the identity of the server. Yaws also creates a file called ${VARDIR}/run/yaws/ctl-${ID} which contain the port number where the server is listening for control commands. The default id is <i>&quot;default&quot;</i>. </p>
<dt><code>server_signature = String</code></p>
<dd>This directive sets the &quot;Server: &quot; output header to the custom value. The default value is <i>&quot;yaws/%VSN%, Yet Another Web Server&quot;</i>. </p>
<dt><code>include_dir = Directory</code></p>
<dd>This directive adds Directory to the path of directories where the Erlang compiler searches for include files. We need to use this if we want to include .hrl files in our Yaws Erlang code. It is possible to have several of these commands in the configuration file. The default value is <i>&quot;yaws_dir&quot;/examples/include</i>. </p>
<dt><code>max_num_cached_files = Integer</code></p>
<dd>Yaws will cache small files such as commonly accessed GIF images in RAM. This directive sets a maximum number on the number of cached files. The default value is <i>400</i>. </p>
<dt><code>max_num_cached_bytes = Integer</code></p>
<dd>This directive controls the total amount of RAM which can maximally be used for cached RAM files. The default value is <i>1000000</i>, 1 megabyte. </p>
<dt><code>max_size_cached_file = Integer</code></p>
<dd>This directive sets a maximum size on the files that are RAM cached by Yaws. The default value is <i>8000</i>, 8 kBytes. </p>
<dt><code>cache_refresh_secs = Integer</code></p>
<dd>The RAM cache is used to serve pages that sit in the cache. An entry sits in cache at most cache_refresh_secs number of seconds. The default is <i>30</i>. This means that when the content is updated under the docroot, that change doesn&#8217;t show until 30 seconds have passed. While developing a Yaws site, it may be convenient to set this value to 0. If the debug flag (-d) is passed to the Yaws start script, this value is automatically set to 0. </p>
<dt><code>trace = false | traffic | http</code></p>
<dd>This enables traffic or http tracing. Tracing is also possible to enable with a command line flag to Yaws. Default is <i>false</i>. </p>
<dt><code>use_old_ssl = true | false</code></p>
<dd>This re-enables the old OTP SSL implementation. By default we use the new SSL implementation. </p>
<dt><code>auth_log = true | false</code></p>
<dd><code>Deprecated and ignored. Now, this target must be set in server part.</code> </p>
<dt><code>max_connections = nolimit | Integer</code></p>
<dd>Set this value to control the maximum number of connections from HTTP clients into the server. This is implemented by closing the last socket if the limit threshold is reached. </p>
<dt><code>keepalive_maxuses = nolimit | Integer</code></p>
<dd>Normally, Yaws does not restrict the number of times a connection is kept alive using keepalive. Setting this parameter to an integer X will ensure that connections are closed once they have been used X times. This can be a useful to guard against long running connections collecting too much garbage in the Erlang VM. </p>
<dt><code>process_options = undefined | Proplist</code></p>
<dd>Set process spawn options for client acceptor processes. Options must be specified as a quoted string of either the atom <i>undefined</i> or as a proplist of valid process options. The supported options are <i>fullsweep_after</i>, <i>min_heap_size</i>, and <i>min_bin_vheap_size</i>, each taking an associated integer value. Other process options are ignored. The proplist may also be empty. See <code>erlang:spawn_opt/4</code> for details on these options. </p>
<dt><code>large_file_chunk_size = Integer</code></p>
<dd>Set the chunk size used by Yaws to send large files when sendfile is not supported or disabled. The default value is <i>10240</i>. </p>
<dt><code>large_file_sendfile = erlang | yaws | disable</code></p>
<dd>Set the version of sendfile method to use to send large files (if supported): </p>
<p> <code>erlang</code> &#8211; use <i>file:sendfile/5</i>, if supported. </p>
<p> <code>yaws</code> &#8211; use Yaws sendfile linked-in driver, if supported. </p>
<p> <code>disable</code> &#8211; do not use any sendfile method, but <i>gen_tcp:send/2</i>. </p>
<p> The default value is <i>yaws</i>. </p>
<dt><code>acceptor_pool_size = Integer</code></p>
<dd>Set the size of the pool of cached acceptor processes. The specified value must be greater than or equal to 0. The default value is <i>8</i>. Specifying a value of 0 effectively disables the process pool. </p>
<dt><code>log_wrap_size = Integer</code></p>
<dd>The logs written by Yaws are all wrap logs, the default value at the size where they wrap around and the original gets renamed to File.old is <i>1000000</i>, 1 megabyte. This value can be changed.<br />
 If we set the value to 0 the logs will never wrap. If we want to use Yaws in combination with a more traditional log wrapper such as logrotate, set the size to 0 and Yaws will reopen the logfiles once they have be renamed/removed. </p>
<dt><code>log_resolve_hostname = true | false</code></p>
<dd>By default the client host IP is not resolved in the access logs. </p>
<dt><code>fail_on_bind_err = true | false</code></p>
<dd>Fail completely or not if Yaws fails to bind a listen socket Default is <i>true</i>. </p>
<dt><code>enable_soap = true | false</code></p>
<dd>If true, a soap server will be started at startup of Yaws. Default is <i>false</i>. </p>
<dt><code>soap_srv_mods = ListOfModuleSetting</code></p>
<dd>If enable_soap is true, a startup Yaws will invoke <i>yaws_soap_srv:setup()</i> to setup modules set here. ModuleSetting is either a triad like <i>&lt;Mod, HandlerFunc, WsdlFile&gt;</i> or a quadruple form like <i>&lt;Mod, HandlerFunc, WsdlFile, Prefix&gt;</i> which specifies the <i>prefix</i>. A <i>prefix</i> will be used as argument of <i>yaws_soap_lib:initModel()</i> and then be used as a XML namespace prefix. Note, the <i>WsdlFile</i> here should be an absolute-path file in local file systems. </p>
<p> For example, we can specify </p>
<pre> soap_srv_mods=&lt;Mod1, Handler, Wsdl1&gt; &lt;Mod2, Handler, Wsdl2, Prefix&gt; ...</pre>
<dt><code>php_exe_path = Path</code></p>
<dd><code>this target is deprecated and useless. use &#8216;php_handler&#8217; target in server part instead.</code><br />
 The name of (and possibly path to) the php executable used to interpret php scripts (if allowed). Default is <i>php_exe_path = php-cgi</i>. </p>
<dt><code>copy_error_log = true | false</code></p>
<dd>Enable or disable copying of the error log. When we run in embedded mode, there may very well be some other systems process that is responsible for writing the errorlog to a file whereas when we run in normal standalone mode, we typically want the Erlang errorlog written to a report.log file. Default value is <i>true</i>. </p>
<dt><code>ysession_mod = Module</code></p>
<dd>Allows to specify a different Yaws session storage mechanism instead of an ETS table. One of the drawbacks of the default yaws_session_server implementation is that server side cookies are lost when the server restarts. Specifying a different module here will pass all writes/read operations to this module (it must implements appropriate callbacks). </p>
<dt><code>runmod = ModuleName</code></p>
<dd>At startup Yaws will invoke <i>ModuleName:start()</i> in a separate process. It is possible to have several runmods. This is useful if we want to reuse the Yaws startup shell script for our own application. </p>
<dt><code>pick_first_virthost_on_nomatch = true | false</code></p>
<dd>When Yaws gets a request, it extracts the Host: header from the client request to choose a virtual server amongst all servers with the same IP/Port pair. This configuration parameter decides whether Yaws should pick the first (as defined in the yaws.conf file) if no name match or not. In real live hosting scenarios we typically want this to be false whereas in testing/development scenarios it may be convenient to set it to true. Default is <i>true</i>. </p>
<dt><code>keepalive_timeout = TimeInMilliseconds | infinity</code></p>
<dd>If the HTTP session will be kept alive (i.e., not immediately closed) it will close after keepalive_timeout milliseconds unless a new request is received in that time. The default value is <i>30000</i>. The value <i>infinity</i> is legal but not recommended. </p>
<dt><code>subconfig = File</code></p>
<dd>Load specified config file. </p>
<dt><code>subconfigdir = Directory</code></p>
<dd>Load all config file in specified directory. </p>
<dt><code>x_forwarded_for_log_proxy_whitelist = ListOfUpstreamProxyServerIps</code></p>
<dd><code>this target is deprecated and will be ignored.</code> </p>
<dt><code>default_type = MimeType</code></p>
<dd>Defines the default MIME type to be used where Yaws cannot determine it by its MIME types mappings. Default is <i>text/plain</i>. </p>
<dt><code>default_charset = Charset</code></p>
<dd>Defines the default charset to be added when a response content-type is <i>text/*</i>. By default, no charset is added. </p>
<dt><code>mime_types_file = File</code></p>
<dd>Overrides the default <i>mime.types</i> file included with Yaws. This file must use the following format: </p>
<pre> # Lines beginning with a '#' or a whitespace are ignored
 # blank lines are also ignored
 &lt;MIME type&gt; &lt;space separated file extensions&gt;</pre>
<p>The default file is located at <i>${PREFIX}/lib/yaws/priv/mime.types</i>. You should not edit this file because it may be replaced when you upgrade your server. </p>
<dt><code>add_types = ListOfTypes</code></p>
<dd>Specifies one or more mappings between MIME types and file extensions. More than one extension can be assigned to a MIME type. <i>ListOfTypes</i> is defined as follows: </p>
<pre> add_types = &lt;MimeType1, Ext&gt; &lt;MimeType2, Ext1 Ext2 ...&gt; ...</pre>
<p>The mappings defined using this directive will overload all other definitions. If a file extension is defined several times, only the last one is kept. Multiple <code>add_types</code> directives may be used. </p>
<dt><code>add_charsets = ListOfCharsets</code></p>
<dd>Specifies one or more mappings between charsets and file extensions. More than one extension can be assigned to a charset. <i>ListOfCharsets</i> is defined as follows: </p>
<pre> add_charsets = &lt;Charset1, Ext&gt; &lt;Charset2, Ext1 Ext2 ...&gt; ...</pre>
<p>The mappings defined using this directive will overload all other definitions. If a file extension is defined several times, only the last one is kept. Multiple <code>add_charsets</code> directives may be used. </p>
</dl>
<h2>Server Part</h2>
<p>Yaws can virthost several web servers on the same IP address as well as several web servers on different IP addresses. This includes SSL servers. </p>
<p> Each virtual host is defined within a matching pair of <code>&lt;server ServerName&gt;</code> and <code>&lt;/server&gt;</code>. The ServerName will be the name of the webserver. </p>
<p> The following directives are allowed inside a server definition.</p>
<dl>
<dt><code>port = Port</code></p>
<dd>This makes the server listen on Port. Default is <i>8000</i>.</p>
<dt><code>listen = IpAddress</code></p>
<dd>This makes the server listen on IpAddress. When virthosting several servers on the same ip/port address, if the browser doesn&#8217;t send a Host: field, Yaws will pick the <i>first</i> server specified in the config file. If the specified IP address is 0.0.0.0 Yaws will listen on all local IP addresses on the specified port. Default is <i>127.0.0.1</i>. Multiple <code>listen</code> directives may be used to specify several addresses to listen on. </p>
<dt><code>listen_backlog = Integer</code></p>
<dd>This sets the TCP listen backlog for the server to define the maximum length the queue of pending connections may grow to. The default is 1024. </p>
<dt><code>&lt;listen_opts&gt; &#8230; &lt;/listen_opts&gt;</code></p>
<dd>Defines extra options to be set on the listen socket and, by inheritance, on accepted sockets. See <i>inet:setopts/2</i> for details. Supported options are: </p>
<p> <code>buffer = Integer</code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>delay_send = true | false </code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>linger = Integer | false </code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>nodelay = true | false </code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>priority = Integer</code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>sndbuf = Integer</code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>recbuf = Integer</code> (default: 8196) </p>
<p> <code>send_timeout = Integer | infinity</code> (default: same as <i>inet:setopts/2</i>) </p>
<p> <code>send_timeout_close = true | false </code> (default: same as <i>inet:setopts/2</i>) </p>
<dt><code>server_signature = String</code></p>
<dd>This directive sets the &quot;Server: &quot; output header to the custom value and overloads the global one for this virtual server. </p>
<dt><code>rhost = Host[:Port]</code></p>
<dd>This forces all local redirects issued by the server to go to Host. This is useful when Yaws listens to a port which is different from the port that the user connects to. For example, running Yaws as a non-privileged user makes it impossible to listen to port 80, since that port can only be opened by a privileged user. Instead Yaws listens to a high port number port, 8000, and iptables are used to redirect traffic to port 80 to port 8000 (most NAT:ing firewalls will also do this for you). </p>
<dt><code>rscheme = http | https</code></p>
<dd>This forces all local redirects issued by the server to use this method. This is useful when an SSL off-loader, or stunnel, is used in front of Yaws. </p>
<dt><code>auth_log = true | false</code></p>
<dd>Enable or disable the auth log for this virtual server. Default is <i>true</i>. </p>
<dt><code>access_log = true | false</code></p>
<dd>Setting this directive to false turns of traffic logging for this virtual server. The default value is <i>true</i>. </p>
<dt><code>logger_mod = Module</code></p>
<dd>It is possible to set a special module that handles access and auth logging. The default is to log all web server traffic to &lt;Host&gt;.access and &lt;Host&gt;.auth files in the configured or default logdir.<br />
 This module must implement the behaviour <i>yaws_logger</i>. Default value is <i>yaws_log</i>. </p>
<p> The following functions should be exported: </p>
<p> <code>Module:open_log(ServerName, Type, LogDir)</code></p>
<dl>
<dd>When Yaws is started, this function is called for this virtual server. If the initialization is successful, the function must return <i>{true,State}</i> and if an error occurred, it must return <i>false</i>.</dl>
<dd><code>Module:close_log(ServerName, Type, State)</code></p>
<dl>
<dd>This function is called for this virtual server when Yaws is stopped.</dl>
<dd><code>Module:wrap_log(ServerName, Type, State, LogWrapSize)</code></p>
<dl>
<dd>This function is used to rotate log files. It is regularly called by Yaws and must return the possibly updated internal NewState.</dl>
<dd><code>Module:write_log(ServerName, Type, State, Infos)</code></p>
<dl>
<dd>When it needs to log a message, Yaws will call this function. The parameter Infos is <i>{Ip,Req,InHdrs,OutHdrs,Time}</i> for an access log and <i>{Ip,Path,Item}</i> for an auth log, where: </p>
<p> <code>Ip</code> &#8211; IP address of the accessing client (as a tuple). </p>
<p> <code>Req</code> &#8211; the HTTP method, URI path, and HTTP version of the request (as a #http_request{} record). </p>
<p> <code>InHdrs</code> &#8211; the HTTP headers which were received from the WWW client (as a #headers{} record). </p>
<p> <code>OutHdrs</code> &#8211; the HTTP headers sent to the WWW client (as a #outh{} record) </p>
<p> <code>Path</code> &#8211; the URI path of the request (as a string). </p>
<p> <code>Item</code> &#8211; the result of an authentication request. May be <i>{ok,User}</i>, <i>403</i> or <i>{401,Realm}</i>. </p>
<p> <code>Time</code> &#8211; The time taken to serve the request, in microseconds.</dl>
<dd>For all of these callbacks, <code>ServerName</code> is the virtual server&#8217;s name, <i>Type</i> is the atom access or auth and <i>State</i> is the internal state of the logger. </p>
<dt><code>shaper = Module</code></p>
<dd>Defines a module to control access to this virtual server. Access can be controlled based on the IP address of the client. It is also possible to throttles HTTP requests based on the client&#8217;s download rate. This module must implement the behaviour <i>yaws_shaper</i>. </p>
<p> There is no such module configured by default. </p>
<dt><code>dir_listings = true | true_nozip | false</code></p>
<dd>Setting this directive to false disallows the automatic dir listing feature of Yaws. A status code 403 Forbidden will be sent. Set to true_nozip to avoid the auto-generated all.zip entries. Default is <i>false</i>. </p>
<dt><code>extra_cgi_vars = &#8230;..</code></p>
<dd>Add additional CGI or FastCGI variables. For example: </p>
<pre> &lt;extra_cgi_vars dir='/path/to/some/scripts'&gt;
 var = val
 ...
 &lt;/extra_cgi_vars&gt;</pre>
<dt><code>statistics = true | false</code></p>
<dd>Turns on/off statistics gathering for a virtual server. Default is <i>false</i>. </p>
<dt><code>fcgi_app_server = Host:Port</code></p>
<dd>The hostname and TCP port number of a FastCGI application server. The TCP port number is not optional. There is no default value. </p>
<dt><code>fcgi_trace_protocol = true | false</code></p>
<dd>Enable or disable tracing of FastCGI protocol messages as info log messages. Disabled by default. </p>
<dt><code>fcgi_log_app_error = true | false</code></p>
<dd>Enable or disable logging of application error messages (output to stderr and non-zero exit value). Disabled by default. </p>
<dt><code>deflate = true | false</code></p>
<dd>Turns on or off deflate compression for a server. Default is <i>false</i>. </p>
<dt><code>&lt;deflate&gt; &#8230; &lt;/deflate&gt;</code></p>
<dd>This begins and ends the deflate compression configuration for this server. The following items are allowed within a matching pair of &lt;deflate&gt; and &lt;/deflate&gt; delimiters. </p>
<p> <code>min_compress_size = nolimit | Integer</code></p>
<dl>
<dd>Defines the smallest response size that will be compressed. If nolimit is not used, the specified value must be strictly positive. The default value is <i>nolimit</i>.</dl>
<dd><code>compress_level = none | default | best_compression | best_speed | 0..9</code></p>
<dl>
<dd>Defines the compression level to be used. 0 (none), gives no compression at all, 1 (best_speed) gives best speed and 9 (best_compression) gives best compression. The default value is <i>default</i>.</dl>
<dd><code>window_size = 9..15</code></p>
<dl>
<dd>Specifies the zlib compression window size. It should be in the range 9 through 15. Larger values of this parameter result in better compression at the expense of memory usage. The default value is <i>15</i>.</dl>
<dd><code>mem_level = 1..9</code></p>
<dl>
<dd>Specifies how much memory should be allocated for the internal compression state. <i>mem_level=1</i> uses minimum memory but is slow and reduces compression ratio; <i>mem_level=9</i> uses maximum memory for optimal speed. The default value is <i>8</i>.</dl>
<dd><code>strategy = default | filtered | huffman_only</code></p>
<dl>
<dd>This parameter is used to tune the compression algorithm. See <code><a href="//www.systutorials.com/docs/linux/man/3erl-zlib/">zlib</a>(3erl)</code> for more details on the <i>strategy</i> parameter. The default value is <i>default</i>.</dl>
<dd><code>use_gzip_static = true | false</code></p>
<dl>
<dd>If true, Yaws will try to serve precompressed versions of static files. It will look for precompressed files in the same location as original files that end in &quot;.gz&quot;. Only files that do not fit in the cache are concerned. The default value is <i>false</i>.</dl>
<dd><code>mime_types = ListOfTypes | defaults | all</code></p>
<dl>
<dd>Restricts the deflate compression to particular MIME types. The special value <i>all</i> enable it for all types (It is a synonym of `*/*&#8217;). MIME types into <i>ListOfTypes</i> must have the form `type/subtype&#8217; or `type/*&#8217; (indicating all subtypes of that type). Here is an example: </p>
<pre> mime_types = default image/*
 mime_types = application/xml application/xhtml+xml application/rss+xml</pre>
<p>By default, following MIME types are compressed (if <code>deflate</code> is set to true): <i>text/*, application/rtf, application/msword, application/pdf, application/x-dvi, application/javascript, application/x-javascript</i>. Multiple <code>mime_types</code> directive can be used.</dl>
<dt><code>docroot = Directory &#8230;</code></p>
<dd>This makes the server serve all its content from Directory.<br />
 It is possible to pass a space-separated list of directories as docroot. If this is the case, the various directories will be searched in order for the requested file. This also works with the ssi and yssi constructs where the full list of directories will be searched for files to ssi/yssi include. Multiple docroot directives can be used. You need at least one valid docroot, invalid docroots are skipped with their associated auth structures. </p>
<dt><code>auth_skip_docroot = true | false</code></p>
<dd>If true, the docroot will not be searched for <i>.yaws_auth</i> files. This is useful when the docroot is quite large and the time to search it is prohibitive when Yaws starts up. Defaults to <i>false</i>. </p>
<dt><code>partial_post_size = Integer | nolimit</code></p>
<dd>When a Yaws file receives large POSTs, the amount of data received in each chunk is determined by the this parameter. The default value is <i>10240</i>. Setting it to nolimit is potentially dangerous. </p>
<dt><code>dav = true | false</code></p>
<dd>Turns on the DAV protocol for this server. The dav support in Yaws is highly limited. If dav is turned on, .yaws processing of .yaws pages is turned off. Default is <i>false</i>. The socket read timeout is supplied by the keepalive_timeout setting. If the read is not done within the timeout, the POST will fail. </p>
<dt><code>tilde_expand = true|false</code></p>
<dd>If this value is set to false Yaws will never do tilde expansion. The default is <i>false</i>. tilde_expansion is the mechanism whereby a URL on the form <a rel="nofollow" href="http://www.foo.com/~username">http://www.foo.com/~username</a> is changed into a request where the docroot for that particular request is set to the directory ~username/public_html/. </p>
<dt><code>allowed_scripts = ListOfSuffixes</code></p>
<dd>The allowed script types for this server. Recognized are `yaws&#8217;, `cgi&#8217;, `fcgi&#8217;, `php&#8217;. Default is <i>allowed_scripts = yaws php cgi fcgi</i>. </p>
<p> Note: for fcgi scripts, the FastCGI application server is only called if a local file with the .fcgi extension exists. However, the contents of the local .fcgi file are ignored. </p>
<dt><code>tilde_allowed_scripts = ListOfSuffixes</code></p>
<dd>The allowed script types for this server when executing files in a users public_html folder Recognized are `yaws&#8217;, `cgi&#8217;, `fcgi&#8217;, `php&#8217;. Default is <i>tilde_allowed_scripts =</i> i.e. empty </p>
<dt><code>index_files = ListOfResources</code></p>
<dd>This directive sets the list of resources to look for, when a directory is requested by the client. If the last entry begins with a `/&#8217;, and none of the earlier resources are found, Yaws will perform a redirect to this uri. Default is <i>index_files = index.yaws index.html index.php</i>. </p>
<dt><code>appmods = ListOfModuleNames</code></p>
<dd>If any the names in ListOfModuleNames appear as components in the path for a request, the path request parsing will terminate and that module will be called. There is also an alternate syntax for specifying the appmods if we don&#8217;t want our internal erlang module names to be exposed in the URL paths. We can specify </p>
<pre> appmods = &lt;Path1, Module1&gt; &lt;Path2, Modules2&gt; ...</pre>
<p>Assume for example that we have the URL <a rel="nofollow" href="http://www.hyber.org/myapp/foo/bar/baz?user=joe">http://www.hyber.org/myapp/foo/bar/baz?user=joe</a> while we have the module foo defined as an appmod, the function foo:out(Arg) will be invoked instead of searching the filesystems below the point foo.<br />
 The Arg argument will have the missing path part supplied in its appmoddata field. </p>
<p> It is also possible to exclude certain directories from appmod processing. This is particulaly interesting for &#8216;/&#8217; appmods. Here is an example: </p>
<pre> appmods = &lt;/, myapp exclude_paths icons js top/static&gt;</pre>
<p>The above configuration will invoke the &#8216;myapp&#8217; erlang module on everything except any file found in directories, &#8216;icons&#8217;, &#8216;js&#8217; and &#8216;top/static&#8217; relative to the docroot. </p>
<dt><code>dispatchmod = DispatchModule</code></p>
<dd>Set <i>DispatchModule</i> as a server-specific request dispatching module. Yaws expects <i>DispatchModule</i> to export a <i>dispatch/1</i> function. When it receives a request, Yaws passes an <i>#arg{}</i> record to the dispatch module&#8217;s <i>dispatch/1</i> function, which returns one of the following atom results: </p>
<dl>
<dd><code>done</code> &#8211; this indicates the dispatch module handled the request itself and already sent the response, and Yaws should resume watching for new requests on the connection </p>
<p> <code>closed</code> &#8211; same as <i>done</i> but the <i>DispatchModule</i> also closed the connection </p>
<p> <code>continue</code> &#8211; the dispatch module has decided not to handle the request, and instead wants Yaws to perform its regular request dispatching</dl>
<dd>Note that when <i>DispatchModule</i> handles a request itself, Yaws does not support tracing, increment statistics counters or allow traffic shaping for that request. It does however still keep track of maximum keepalive uses on the connection. </p>
<dt><code>errormod_404 = Module</code></p>
<dd>It is possible to set a special module that handles 404 Not Found messages. The function <i>Module:out404(Arg, GC, SC)</i> will be invoked. The arguments are </p>
<dl>
<dd><code>Arg</code> &#8211; a #arg{} record </p>
<p> <code>GC</code> &#8211; a #gconf{} record (defined in yaws.hrl) </p>
<p> <code>SC</code> &#8211; a #sconf{} record (defined in yaws.hrl)</dl>
<dd>The function can and must do the same things that a normal <i>out/1</i> does. </p>
<dt><code>errormod_401 = Module</code></p>
<dd>It is possible to set a special module that handles 401 Unauthorized messages. This can for example be used to display a login page instead. The function <i>Module:out401(Arg, Auth, Realm)</i> will be invoked. The arguments are </p>
<dl>
<dd><code>Arg</code> &#8211; a #arg{} record </p>
<p> <code>Auth</code> &#8211; a #auth{} record </p>
<p> <code>Realm</code> &#8211; a string</dl>
<dd>The function can and must do the same things that a normal <i>out/1</i> does. </p>
<dt><code>errormod_crash = Module</code></p>
<dd>It is possible to set a special module that handles the HTML generation of server crash messages. The default is to display the entire formated crash message in the browser. This is good for debugging but not in production.<br />
 The function <i>Module:crashmsg(Arg, SC, Str)</i> will be called. The <i>Str</i> is the real crash message formated as a string.<br />
 The function must return, <i>{content,MimeType,Cont}</i> or <i>{html, Str}</i> or <i>{ehtml, Term}</i>. That data will be shipped to the client. </p>
<dt><code>expires = ListOfExpires</code></p>
<dd>Controls the setting of the <i>Expires</i> HTTP header and the <i>max-age</i> directive of the <i>Cache-Control</i> HTTP header in server responses for specific MIME types. The expiration date can set to be relative to either the time the source file was last modified, or to the time of the client access. ListOfExpires is defined as follows: </p>
<pre> expires = &lt;MimeType1, access+Seconds&gt; &lt;MimeType2, modify+Seconds&gt; ...</pre>
<p>These HTTP headers are an instruction to the client about the document&#8217;s validity and persistence. If cached, the document may be fetched from the cache rather than from the source until this time has passed. After that, the cache copy is considered &quot;expired&quot; and invalid, and a new copy must be obtained from the source. Here is an example: </p>
<pre> expires = &lt;image/gif, access+2592000&gt; &lt;image/png, access+2592000&gt;
 expires = &lt;image/jpeg, access+2592000&gt; &lt;text/css, access+2592000&gt;</pre>
<dt><code>arg_rewrite_mod = Module</code></p>
<dd>It is possible to install a module that rewrites all the Arg #arg{} records at an early stage in the Yaws server. This can be used to do various things such as checking a cookie, rewriting paths etc.<br />
 The module <i>yaws_vdir</i> can be used in case you want to serve static content that is not located in your docroot. See the example at the bottom of this man page for how to use the <i>opaque</i> + <i>vdir</i> elements to instruct the <i>yaws_vdir</i> module what paths to rewrite. </p>
<dt><code>start_mod = Module</code></p>
<dd>Defines a user provided callback module. At startup of the server, Module:start/1 will be called. The #sconf{} record (defined in yaws.hrl) will be used as the input argument. This makes it possible for a user application to synchronize the startup with the Yaws server as well as getting hold of user specific configuration data, see the explanation for the &lt;opaque&gt; context. </p>
<dt><code>revproxy = Prefix Url [intercept_mod Module]</code></p>
<dd>Make Yaws a reverse proxy. <i>Prefix</i> is a path inside our own docroot and <i>Url</i><code> argument is a URL pointing to a website we want to &quot;mount&quot; under the </code><i>Prefix</i> path. This example: </p>
<pre> revproxy = /tmp/foo <a rel="nofollow" href="http://yaws.hyber.org">http://yaws.hyber.org</a></pre>
<p>makes the hyber website appear under <i>/tmp/foo</i>. </p>
<p> It is possible to have multiple reverse proxies inside the same server. </p>
<p> You can optionally configure an interception module for each reverse proxy, allowing your application to examine and modify requests and HTTP headers as they pass through the proxy from client to backend server and also examine and modify responses and HTTP headers as they return from the backend server through the proxy to the client. </p>
<p> You specify an interception module by including the optional <i>intercept_mod</i> keyword followed by <i>Module</i>, which should be the name of your interception module. </p>
<p> An interception module is expected to export two functions: <i>rewrite_request/2</i> and <i>rewrite_response/2</i>. The two arguments passed to <i>rewrite_request/2</i> function are a <i>#http_request{}</i> record and a <i>#headers{}</i> record, whereas <i>rewrite_response/2</i> function takes a <i>#http_response{}</i> record and also a <i>#headers{}</i> record. You can find definitions for these record types in the <i>yaws_api.hrl</i> header file. Each function can examine each record instance and can either return each original instance or can return a modified copy of each instance in its response. The <i>rewrite_request/2</i> function should return a tuple of the following form: </p>
<pre> <i>{ok, #http_request{}, #headers{}}</i></pre>
<p>and the <i>rewrite_response/2</i> function should similarly return a tuple of the following form: </p>
<pre> <i>{ok, #http_response{}, #headers{}}</i></pre>
<p>A <i>#headers{}</i> record can easily be manipulated in an interceptor using the functions listed below: </p>
<pre> <i>yaws_api:set_header/2</i>, <i>yaws_api:set_header/3</i>
 <i>yaws_api:get_header/2</i>, <i>yaws_api:get_header/3</i>
 <i>yaws_api:delete_header/2</i></pre>
<p>Any failures in your interception module&#8217;s functions will result in HTTP status code 500, indicating an internal server error. </p>
<dt><code>fwdproxy = true|false</code></p>
<dd>Make Yaws a forward proxy. By enabling this option you can use Yaws as a proxy for outgoing web traffic, typically by configuring the proxy settings in a web-browser to explicitly target Yaws as its proxy server. </p>
<dt><code>servername = Name</code></p>
<dd>If we&#8217;re virthosting several servers and want to force a server to match specific Host: headers we can do this with the &quot;servername&quot; directive. This name doesn&#8217;t necessarily have to be the same as the the name inside &lt;server Name&gt; in certain NAT scenarios. Rarely used feature. </p>
<dt><code>serveralias = ListOfNames</code></p>
<dd>This directive sets the alternate names for a virtual host. A server alias may contain wildcards:</p>
<dl>
<dd>&nbsp;<wbr>&#8216;*&#8217;&nbsp;<wbr>matches any sequence of zero or more characters<br />
&nbsp;<wbr>&#8216;?&#8217;&nbsp;<wbr>matches one character unless that character is a period&nbsp;<wbr>(&#8216;.&#8217;)</dl>
<dd>Multiple <code>serveralias</code> directives may be used. Here is an example: </p>
<pre> &lt;server server.domain.com&gt;
 serveralias = server server2.domain.com server2
 serveralias = *.server.domain.com *.server?.domain.com
 ...
 &lt;/server&gt;</pre>
<dt><code>php_handler = &lt;Type, Spec&gt;</code></p>
<dd>Set handler to interpret .php files. It can be one of the following definitions: </p>
<p> <code>php_handler = &lt;cgi, Filename&gt;</code> &#8211; The name of (and possibly path to) the php executable used to interpret php scripts (if allowed). </p>
<p> <code>php_handler = &lt;fcgi, Host:Port&gt;</code> &#8211; Use the specified fastcgi server to interpret .php files (if allowed). </p>
<dl>
<dd>Yaws does not start the PHP interpreter in fastcgi mode for you. To run PHP in fastcgi mode, call it with the -b option. For example: </p>
<pre> php5-cgi -b '127.0.0.1:54321'</pre>
<p>This starts a php5 in fastcgi mode listening on the local network interface. To make use of this PHP server from Yaws, specify: </p>
<pre> php_handler = &lt;fcgi, 127.0.0.1:54321&gt;</pre>
<p>The PHP interpreter needs read access to the files it is to serve. Thus, if you run it in a different security context than Yaws itself, make sure it has access to the .php files.<br />
 Please note that anyone who is able to connect to the php fastcgi server directly can use it to read any file to which it has read access. You should consider this when setting up a system with several mutually untrusted instances of php.</dl>
<dd><code>php_handler = &lt;extern, Module:Function | Node:Module:Function&gt;</code> &#8211; Use an external handler, possibly on another node, to interpret .php files (if allowed). </p>
<dl>
<dd>To interpret a .php file, the function <i>Module:Function(Arg)</i> will be invoked (Evaluated inside a rpc call if a <i>Node</i> is specified), where Arg is a #arg{} record.<br />
 The function must do the same things that a normal out/1 does.</dl>
<dd>Default value is <i>&lt;cgi, &quot;/usr/bin/php-cgi&quot;&gt;</i>. </p>
<dt><code>phpfcgi = Host:Port</code></p>
<dd><code>this target is deprecated. use &#8216;php_handler&#8217; target in server part instead.</code><br />
 Use this directive is same as: php_handler = &lt;fcgi, Host:Port&gt;. </p>
<dt><code>default_type = MimeType</code></p>
<dd>Overloads the global <code>default_type</code> value for this virtual server.</p>
<dt><code>default_charset = Charset</code></p>
<dd>Overloads the global <code>default_charset</code> value for this virtual server. </p>
<dt><code>mime_types_file = File</code></p>
<dd>Overloads the global <code>mime_type_file</code> value for this virtual server. Mappings defined in <i>File</i> will not overload those defined by <code>add_types</code> directives in the global part. </p>
<dt><code>add_types = ListOfTypes</code></p>
<dd>Overloads the global <code>add_types</code> values for this virtual server. If a mapping is defined in the global part and redefined in a server part using this directive, then it is replaced. Else it is kept. </p>
<dt><code>add_charsets = ListOfCharsets</code></p>
<dd>Overloads the global <code>add_charsets</code> values for this virtual server. If a mapping is defined in the global part and redefined in a server part using this directive, then it is replaced. Else it is kept. </p>
<dt><code>&lt;ssl&gt; &#8230; &lt;/ssl&gt;</code></p>
<dd>This begins and ends an SSL configuration for this server. It&#8217;s possible to virthost several SSL servers on the same IP given that they all share the same certificate configuration. In general it is complicated to virthost several SSL servers on the same IP address since the certificate is typically bound to a domainname in the common name part of the certificate. One solution (the only?) to this problem is to have a certificate with multiple subjectAltNames. See <a rel="nofollow" href="http://wiki.cacert.org/VhostTaskForce#Interoperability_Test">http://wiki.cacert.org/VhostTaskForce#Interoperability_Test</a> </p>
<p> <code>keyfile = File</code></p>
<dl>
<dd>Specifies which file contains the private key for the certificate. If not specified then the certificate file will be used.</dl>
<dd><code>certfile = File</code></p>
<dl>
<dd>Specifies which file contains the certificate for the server.</dl>
<dd><code>cacertfile = File</code></p>
<dl>
<dd>A file containing trusted certificates to use during client authentication and to use when attempting to build the server certificate chain. The list is also used in the list of acceptable client CAs passed to the client when a certificate is requested.</dl>
<dd><code>verify = 0 | 1 | 2 | verify_none | verify_peer</code></p>
<dl>
<dd>Specifies the level of verification the server does on client certs. 0 means that the server will not ask for a cert (verify_none), 1 means that the server will ask the client for a cert but not fail if the client does not supply a client cert (verify_peer, fail_if_no_peer_cert = false), 2 means that the server requires the client to supply a client cert (verify_peer, fail_if_no_peer_cert = true). </p>
<p> Setting verify_none means that the x509 validation will be skipped (no certificate request is sent to the client), verify_peer means that a certificate request is sent to the client (x509 validation is performed. </p>
<p> You might want to use fail_if_no_peer_cert in combination with verify_peer.</dl>
<dd><code>fail_if_no_peer_cert = true | false</code></p>
<dl>
<dd>If verify is set to verify_peer and set to true the connection will fail if the client does not send a certificate (i.e. an empty certificate). If set to false the server will fail only if an invalid certificate is supplied (an empty certificate is considered valid).</dl>
<dd><code>depth = Int</code></p>
<dl>
<dd>Specifies the depth of certificate chains the server is prepared to follow when verifying client certs. For the OTP new SSL implementation it is also used to specify how far the server, i.e. we, shall follow the SSL certificates we present to the clients. Hence, using self-signed certs, we typically need to set this to 0.</dl>
<dd><code>password = String</code></p>
<dl>
<dd>String If the private key is encrypted on disc, this password is the 3Dee key to decrypt it.</dl>
<dd><code>ciphers = String</code></p>
<dl>
<dd>This string specifies the SSL cipher string. The syntax of the SSL cipher string is an erlang term compliant with the output of ssl:cipher_suites(). </p>
<pre>ciphers = &quot;[{dhe_rsa,aes_256_cbc,sha}, \
 {dhe_dss,aes_256_cbc,sha}]&quot;</pre>
</dl>
<dt><code>&lt;redirect&gt; &#8230; &lt;/redirect&gt;</code></p>
<dd>Defines a redirect mapping. The following items are allowed within a matching pair of &lt;redirect&gt; and &lt;/redirect&gt; delimiters. </p>
<p> We can have a series of redirect rules in one of formats below: </p>
<pre> Path = URL
 Path = code
 Path = code URL</pre>
<p><code>Path</code> must be an url-decoded path beginning with a slash. <code>URL</code> may be either a relative URL (a path beginning with a slash), or an absolute URL. In the first case, the <i>scheme:hostname:port</i> of the current server will be added. All accesses to <code>Path</code> will be redirected to <code>URL/Path</code> (or <code>scheme:hostname:port/URL/Path</code> if <code>URL</code> is relative). <code>URL</code> must be url-encoded. Note that the original path is appended to the redirected URL. </p>
<p> For example, assume we have the following redirect configuration: </p>
<pre> &lt;redirect&gt;
 /foo = <a rel="nofollow" href="http://www.mysite.org/zapp">http://www.mysite.org/zapp</a>
 /bar = /tomato.html
 &lt;/redirect&gt;</pre>
<p>Assuming this config resides on a site called <a rel="nofollow" href="http://abc.com,">http://abc.com,</a> we have the following redirects: </p>
<pre> <a rel="nofollow" href="http://abc.com/foo">http://abc.com/foo</a> -&gt; <a href="http://www.mysite.org/zapp/foo">http://www.mysite.org/zapp/foo</a>
 <a rel="nofollow" href="http://abc.com/foo/test">http://abc.com/foo/test</a> -&gt; <a href="http://www.mysite.org/zapp/foo/test">http://www.mysite.org/zapp/foo/test</a>
 <a rel="nofollow" href="http://abc.com/bar">http://abc.com/bar</a> -&gt; <a href="http://abc.com/tomato.html/bar">http://abc.com/tomato.html/bar</a>
 <a rel="nofollow" href="http://abc.com/bar/x/y/z">http://abc.com/bar/x/y/z</a> -&gt; <a href="http://abc.com/tomato.html/bar/x/y/z">http://abc.com/tomato.html/bar/x/y/z</a></pre>
<p>By default, Yaws will perform a 302 redirect. The HTTP status code can be changed using the <code>code</code> parameter. Note that the status code must be known by Yaws.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>For 3xx status codes, the <code>URL</code> parameter must be present and will be used to build the new location.</p>
<dt>&bull;</p>
<dd>For other status codes (1xx, 2xx, 4xx and 5xx), it can be omitted. In the absence of <code>URL</code>, Yaws will return a generic response with the specified status code.</p>
<dt>&bull;</p>
<dd>Otherwise, the <code>URL</code> parameter must be a relative URL and will be used to customize the response.</dl>
</dl>
<dl>
<dd>Sometimes we do not want to have the original path appended to the redirected path. To get that behaviour we specify the config with &#8216;==&#8217; instead of &#8216;=&#8217;. </p>
<pre> &lt;redirect&gt;
 /foo == <a rel="nofollow" href="http://www.mysite.org/zapp">http://www.mysite.org/zapp</a>
 /bar = /tomato.html
 &lt;/redirect&gt;</pre>
<p>Now a request for <a rel="nofollow" href="http://abc.com/foo/x/y/z">http://abc.com/foo/x/y/z</a> simply gets redirected to <a rel="nofollow" href="http://www.mysite.org/zapp.">http://www.mysite.org/zapp.</a> This is typically used when we simply want a static redirect at some place in the docroot. </p>
<p> When we specify a relative URL as the target for the redirect, the redirect will be to the current http(s) server.</dl>
<dt><code>&lt;auth&gt; &#8230; &lt;/auth&gt;</code></p>
<dd>Defines an auth structure. The following items are allowed within a matching pair of &lt;auth&gt; and &lt;/auth&gt; delimiters. </p>
<p> <code>docroot = Docroot </code></p>
<dl>
<dd>If a docroot is defined, this auth structure will be tested only for requests in the specified docroot. No docroot configured means all docroots. If two auth structures are defined, one with a docroot and one with no docroot, the first of both overrides the second one for requests in the configured docroot.</dl>
<dd><code>dir = Dir</code></p>
<dl>
<dd>Makes Dir to be controlled by WWW-authenticate headers. In order for a user to have access to WWW-Authenticate controlled directory, the user must supply a password. The Dir must be specified relative to the docroot. Multiple dir can be used. If no dir is set, the default value, <i>&quot;/&quot;</i>, will be used.</dl>
<dd><code>realm = Realm</code></p>
<dl>
<dd>In the directory defined here, the WWW-Authenticate Realm is set to this value.</dl>
<dd><code>authmod = AuthMod</code></p>
<dl>
<dd>If an auth module is defined then AuthMod:auth(Arg, Auth) will be called for all access to the directory. The auth/2 function should return one of: true, false, {false, Realm}, {appmod, Mod}. If {appmod, Mod} is returned then a call to Mod:out401(Arg, Auth, Realm) will be used to deliver the content. If errormod_401 is defined, the call to Mod will be ignored. (Mod:out(Arg) is deprecated). </p>
<p> This can, for example, be used to implement cookie authentication. The auth() callback would check if a valid cookie header is present, if not it would return {appmod, ?MODULE} and the out401/1 function in the same module would return {redirect_local, &quot;/login.html&quot;}.</dl>
<dd><code>user = User:Password</code></p>
<dl>
<dd>Inside this directory, the user User has access if the user supplies the password Password in the popup dialogue presented by the browser. We can obviously have several of these value inside a single &lt;auth&gt; &lt;/auth&gt; pair. </p>
<p> The usage of User:Password in the actual config file is deprecated as of release 1.51. It is preferred to have the users in a file called <i>.yaws_auth</i> in the actual directory. The .yaws_auth file has to be file parseable by <i>file:consult/1</i> </p>
<p> Each row of the file must contain terms on the form </p>
<pre> {User, Password}.</pre>
<p>Where both User and Password should be strings. The .yaws_auth file mechanism is recursive. Thus any subdirectories to Dir are automatically also protected. </p>
<p> The .yaws_auth file is never visible in a dir listing</dl>
<dd><code>pam service = </code><i>pam-service</i></p>
<dl>
<dd>If the item <code>pam</code> is part of the auth structure, Yaws will also try to authenticate the user using &quot;pam&quot; using the pam <i>service</i> indicated. Usual services are typically found under /etc/pam.d. Usual values are &quot;system-auth&quot; etc. </p>
<p> pam authentication is performed by an Erlang port program which is typically installed as suid root by the Yaws install script.</dl>
<dd><code>allow = all | ListOfHost</code></p>
<dl>
<dd>The <i>allow</i> directive affects which hosts can access an area of the server. Access can be controlled by IP address or IP address range. If all is specified, then all hosts are allowed access, subject to the configuration of the <i>deny</i> and <i>order</i> directives. To allow only particular hosts or groups of hosts to access the server, the host can be specified in any of the following formats: </p>
<p> <code>A full IP address</code> </p>
<pre> allow = 10.1.2.3
 allow = 192.168.1.104, 192.168.1.205</pre>
<p><code>A network/netmask pair</code> </p>
<pre> allow = 10.1.0.0/255.255.0.0</pre>
<p><code>A network/nnn CIDR specification</code> </p>
<pre> allow = 10.1.0.0/16</pre>
</dl>
<dd><code>deny = all | ListOfHost</code></p>
<dl>
<dd>This directive allows access to the server to be restricted based on IP address. The arguments for the <i>deny</i> directive are identical to the arguments for the <i>allow</i> directive.</dl>
<dd><code>order = Ordering</code></p>
<dl>
<dd>The <i>order</i> directive, along with <i>allow</i> and <i>deny</i> directives, controls a three-pass access control system. The first pass processes either all <i>allow</i> or all <i>deny</i> directives, as specified by the <i>order</i> directive. The second pass parses the rest of the directives (<i>deny</i> or <i>allow</i>). The third pass applies to all requests which do not match either of the first two. </p>
<p> Ordering is one of (Default value is <i>deny,allow</i>): </p>
<dl>
<dt><code>allow,deny</code></p>
<dd>First, all <i>allow</i> directives are evaluated; at least one must match, or the request is rejected. Next, <i>deny</i> directives are evaluated. If any matches, the request is rejected. Last, any requests which do not match an <i>allow</i> or a <i>deny</i> directive are denied by default. </p>
<dt><code>deny,allow</code></p>
<dd>First, all <i>deny</i> directives are evaluated; if any matched, the request is denied unless it also matches an <i>allow</i> directive. Any requests which do not match any <i>allow</i> or <i>deny</i> directives are permitted.</dl>
</dl>
<dt><code>&lt;opaque&gt; &#8230; &lt;/opaque&gt;</code></p>
<dd>This begins and ends an opaque configuration context for this server, where &#8216;Key = Value&#8217; directives can be specified. These directives are ignored by Yaws (hence the name opaque), but can be accessed as a list of tuples <i>{Key,Value}</i> stored in the #sconf.opaque record entry. See also the description of the <i>start_mod</i> directive. </p>
<p> This mechanism can be used to pass data from a surrounding application into the individual .yaws pages. </p>
</dl>
<h2>Examples</h2>
<p>The following example defines a single server on port 80. </p>
<pre> logdir = /var/log/yaws
 &lt;server <a rel="nofollow" href="http://www.mydomain.org">www.mydomain.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www
 &lt;/server&gt;</pre>
<p>And this example shows a similar setup but two web servers on the same IP address. </p>
<pre> logdir = /var/log/yaws
 &lt;server <a rel="nofollow" href="http://www.mydomain.org">www.mydomain.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www
 &lt;/server&gt;
 &lt;server <a rel="nofollow" href="http://www.funky.org">www.funky.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www_funky_org
 &lt;/server&gt;</pre>
<p>An example with www-authenticate and no access logging at all. </p>
<pre> logdir = /var/log/yaws
 &lt;server <a rel="nofollow" href="http://www.mydomain.org">www.mydomain.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www
 access_log = false
 &lt;auth&gt;
 dir = secret/dir1
 realm = foobar
 user = jonny:verysecretpwd
 user = benny:thequestion
 user = ronny:havinganamethatendswithy
 &lt;/auth&gt;
 &lt;/server&gt;</pre>
<p>An example specifying a user defined module to be called at startup, as well as some user specific configuration. </p>
<pre> &lt;server <a rel="nofollow" href="http://www.funky.org">www.funky.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www_funky_org
 start_mod = btt
 &lt;opaque&gt;
 mydbdir = /tmp
 mylogdir = /tmp/log
 &lt;/opaque&gt;
 &lt;/server&gt;</pre>
<p>An example specifying the GSSAPI/SPNEGO module (authmod_gssapi) to be used for authentication. This module requires egssapi version 0.1~pre2 or later available at <a rel="nofollow" href="http://www.hem.za.org/egssapi/.">http://www.hem.za.org/egssapi/.</a> The Kerberos5 keytab is specified as &#8216;keytab = File&#8217; directive in opaque. This keytab should contain the keys of the HTTP service principal, &#8216;HTTP/<a rel="nofollow" href="http://www.funky.org">www.funky.org</a>&#8216; in this example. </p>
<pre> &lt;server <a rel="nofollow" href="http://www.funky.org">www.funky.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www_funky_org
 start_mod = authmod_gssapi
 &lt;auth&gt;
 authmod = authmod_gssapi
 dir = secret/dir1
 &lt;/auth&gt;
 &lt;opaque&gt;
 keytab = /etc/yaws/http.keytab
 &lt;/opaque&gt;
 &lt;/server&gt;</pre>
<p>And finally a slightly more complex example with two servers on the same IP, and one SSL server on a different IP. When there are more than one server on the same IP, and they have different names the server must be able to choose one of them if the client doesn&#8217;t send a Host: header. Yaws will choose the first one defined in the conf file. </p>
<pre> logdir = /var/log/yaws
 max_num_cached_files = 8000
 max_num_cached_bytes = 6000000
 &lt;server <a rel="nofollow" href="http://www.mydomain.org">www.mydomain.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www
 &lt;/server&gt;
 &lt;server <a rel="nofollow" href="http://www.funky.org">www.funky.org</a>&gt;
 port = 80
 listen = 192.168.128.31
 docroot = /var/yaws/www_funky_org
 &lt;/server&gt;
 &lt;server <a rel="nofollow" href="http://www.funky.org">www.funky.org</a>&gt;
 port = 443
 listen = 192.168.128.32
 docroot = /var/yaws/www_funky_org
 &lt;ssl&gt;
 keyfile = /etc/funky.key
 certfile = /etc/funky.cert
 password = gazonk
 &lt;/ssl&gt;
 &lt;/server&gt;</pre>
<p>Finally an example with virtual directories, vdirs.  The first defined vdir can then be accessed at or under <a rel="nofollow" href="http://server.domain/virtual1/">http://server.domain/virtual1/</a> or <a href="http://server.domain/virtual1">http://server.domain/virtual1</a> </p>
<h2>Author</h2>
<p>Written by Claes Wikstrom</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yaws/">yaws</a></code>(1) <code><a href="/docs/linux/man/1-erl/">erl</a></code>(1) </p>
