---
title: "yaws_api(5)"
name: "yaws_api"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yaws_api/"
description: "yaws_api – api available to yaws web server programmers"
---

<p>yaws_api &#8211; api available to yaws web server programmers</p>
<h2>Synopsis</h2>
<p><code>yaws_api:Function(&#8230;)</code> </p>
<h2>Description</h2>
<p>This is the api available to yaws web server programmers. The Erlang module yaws_api contains a wide variety of functions that can be used inside yaws pages. Each chunk of yaws code is executed while the yaws page is being delivered from the server. We give a very simple example here to show the basic idea. Imagine the following HTML code: <i> </i></p>
<pre>&lt;html&gt;
&lt;body&gt;
&lt;h1&gt; Header 1&lt;/h1&gt;
&lt;erl&gt;
out(Arg) -&gt;
 {html, &quot;&lt;p&gt; Insert this text into the document&quot;}.
&lt;/erl&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>
<p>The <code>out(Arg)</code> function is supplied one argument, an #arg{} structure. We have the following relevant record definitions: <i> </i></p>
<pre>-record(arg, {
 clisock, % the socket leading to the peer client
 client_ip_port, % {ClientIp, ClientPort} tuple
 headers, % headers
 req, % request
 orig_req, % original request
 clidata, % The client data (as a binary in POST requests)
 server_path, % The normalized server path
 % (pre-querystring part of URI)
 querydata, % For URIs of the form ...?querydata
 % equiv of cgi QUERY_STRING
 appmoddata, % (deprecated - use pathinfo instead) the remainder
 % of the path leading up to the query
 docroot, % Physical base location of data for this request
 docroot_mount, % virtual directory e.g /myapp/ that the docroot
 % refers to.
 fullpath, % full deep path to yaws file
 cont, % Continuation for chunked multipart uploads
 state, % State for use by users of the out/1 callback
 pid, % pid of the yaws worker process
 opaque, % useful to pass static data
 appmod_prepath, % (deprecated - use prepath instead) path in front
 % of: &lt;appmod&gt;&lt;appmoddata&gt;
 prepath, % Path prior to 'dynamic' segment of URI.
 % ie <a rel="nofollow" href="http://some.host/">http://some.host/</a>&lt;prepath&gt;/&lt;script-point&gt;/d/e
 % where &lt;script-point&gt; is an appmod mount point,
 % or .yaws,.php,.cgi,.fcgi etc script file.
 pathinfo % Set to '/d/e' when calling c.yaws for the request
 % <a rel="nofollow" href="http://some.host/a/b/c.yaws/d/e">http://some.host/a/b/c.yaws/d/e</a>
 % equiv of cgi PATH_INFO
 }).</pre>
<p>The headers argument is also a record: <i> </i></p>
<pre>-record(headers, {
 connection,
 accept,
 host,
 if_modified_since,
 if_match,
 if_none_match,
 if_range,
 if_unmodified_since,
 range,
 referer,
 user_agent,
 accept_ranges,
 cookie = [],
 keep_alive,
 location,
 content_length,
 content_type,
 content_encoding,
 authorization,
 transfer_encoding,
 x_forwarded_for,
 other = [] % misc other headers
 }).</pre>
<p>The <code>out/1</code> function can use the Arg to generate any content it likes. We have the following functions to aid that generation. </p>
<h2>Api</h2>
<dl>
<dt><code>ssi(DocRoot, ListOfFiles)</code></p>
<dd>Server side include. Just include the files as is in the document. The files will <code>not</code> be parsed and searched for &lt;erl&gt; tags. </p>
<dt><code>pre_ssi_files(DocRoot, ListOfFiles) -&gt;</p>
<dd>Server side include of pre-indented code. The data in Files will be included but contained in a &lt;pre&gt; tag. The data will be htmlized. </p>
<dt>pre_ssi_string(String)</code></p>
<dd>Include htmlized content from String. </p>
<dt><code>f(Fmt, Args)</code></p>
<dd>The equivalent of io_lib:format/2. This function is automatically -included in all erlang code which is a part of a yaws page. </p>
<dt><code>htmlize(Binary | List | Char)</code></p>
<dd>Htmlize an IO list object. </p>
<dt><code>set_cookie(Name, Value, Options])</code></p>
<dd>Sets a cookie to the browser. Options are: <i> </i></p>
<pre>{expires, UtcTime} - Cookie expiration time, where UtcTime is
 a tuple returned by calendar:universal_time/0.
{max_age, Age} - Defines the lifetime of the cookie, in seconds,
 where age is an integer &gt;= 0.
{path, Path} - Path is a string that specifies the subset of URLs to
 which this cookie applies.
{domain, Domain} - Domain is a string that specifies the domain for which
 the cookie is valid.
{comment, Comment} - Comment is a string that doccuments the server's
 intended use of the cookie.
secure - Directs the user agent to use only secure means to
 contact the origin server whenever it sends back this
 cookie.
http_only - Restricts cookie access from other non-HTTP APIs.</pre>
<dt><code>setcookie(Name, Value, [Path, [ Expire, [Domain , [Secure]]]])</code></p>
<dd>Sets a cookie to the browser. This function is deprecated by set_cookie/3. </p>
<dt><code>find_cookie_val(Cookie, Header)</code></p>
<dd>This function can be used to search for a cookie that was previously set by <code>setcookie/2-6</code>. For example if we set a cookie as <code>yaws_api:setcookie(&quot;sid&quot;,SomeRandomSid)</code>, then on subsequent requests from the browser we can call: <code>find_cookie(&quot;sid&quot;,(Arg#arg.headers)#headers.cookie)</code> </p>
<p> The function returns [] if no cookie was found, otherwise the actual cookie is returned as a string. </p>
<dt><code>parse_set_cookie(Str)</code></p>
<dd>This function parses the value of a <code>Set-Cookie</code> header, following the RFC6265. Because old RFCs (2109 and 2965) are still used, it is backward compatible. So this function returns a <i>#setcookie{}</i> record when only one cookie is found. If multiple cookies are set in a single <code>Set-Cookie</code> header, it returns a list of <i>#setcookie{}</i> records. If no cookie was found or if an error occurred, it returns []. </p>
<p> <i>#setcookie{}</i> record is defined in <i>yaws_api.hrl</i>: <i> </i></p>
<pre>-record(setcookie, {key,
 value,
 quoted = false,
 domain,
 max_age,
 expires,
 path,
 secure = false,
 http_only = false,
 extensions = []}).</pre>
<dt><code>parse_cookie(Str)</code></p>
<dd>This function parses the value of <code>Cookie</code> header, following the RFC6265. It returns a list of <i>#cookie{}</i> records. If no cookie was found or if an error occurred, it returns []. </p>
<p> <i>#cookie{}</i> record is defined in <i>yaws_api.hrl</i>: <i> </i></p>
<pre>-record(cookie, {key,
 value,
 quoted = false}).</pre>
<dt><code>format_set_cookie(SetCookie)</code></p>
<dd>Build a cookie string from a <i>#setcookie{}</i> record like returned by <code>parse_set_cookie/1</code>. </p>
<dt><code>format_cookie(Cookie | [Cookie])</code></p>
<dd>Build a cookie string from a <i>#cookie{}</i> record (or a list or records) like returned by <code>parse_cookie/1</code>. </p>
<dt><code>redirect(Url)</code></p>
<dd>This function generates a redirect to the browser. It will clear any previously set headers. So to generate a redirect <code>and</code> set a cookie, we need to set the cookie after the redirect as in: <i> </i></p>
<pre>out(Arg) -&gt;
 ... do some stuff
 Ret = [{redirect, &quot;<a rel="nofollow" href="http://www.somewhere.com">http://www.somewhere.com</a>&quot;},
 setcookie(&quot;sid&quot;, Random)
 ].</pre>
<dt><code>redirect_self(Arg)</code></p>
<dd>If we want to issue a redirect to ourselves, this function is useful. It returns a record <i>#redir_self{}</i> defined in <i>yaws_api.hrl</i>. The record contains fields to construct a URL to ourselves. <i> </i></p>
<pre>-record(redir_self, {
 host, % string() - our own host
 scheme, % http | https
 scheme_str, % &quot;https://&quot; | &quot;http://&quot;
 port, % integer() - our own port
 port_str % &quot;&quot; | &quot;:&lt;int&gt;&quot; - the optional port part
 % to append to the url
 }).</pre>
<dt><code>get_line(String)</code></p>
<dd>This function is convenient when getting 
 terminated lines from a stream of data. It returns: </p>
<p> <code>{line, Line, Tail}</code> or <code>{lastline, Line, Tail}</code> </p>
<p> The function handles multilines as defined in e.g. SMTP or HTTP </p>
<dt><code>mime_type(Scope, FileName)</code></p>
<dd>Returns the MIME type as defined by the extension of <i>FileName</i>. <i>Scope</i> can have following values: </p>
<dl>
<dd><code>global</code> &#8211; returns the result obtained from the global context.<br />
 <code>#sconf{} | {ServerName, Port}</code> &#8211; returns the result obtained from the virtual server&#8217;s context. If no MIME type is found in this scope, it falls back on the global one.</dl>
<dt><code>mime_type(FileName)</code></p>
<dd>Tries to determine the right <i>Scope</i> before calling mime_type/2. </p>
<dt><code>stream_chunk_deliver(YawsPid, Data)</code></p>
<dd>When a yaws function needs to deliver chunks of data which it gets from a process. The other process can call this function to deliver these chunks. It requires the <code>out/1</code> function to return the value <code>{streamcontent, MimeType, FirstChunk}</code> to work. YawsPid is the process identifier of the yaws process delivering the original .yaws file. That is self() in the yaws code. The Pid must typically be passed (somehow) to the producer of the stream. </p>
<dt><code>stream_chunk_deliver_blocking(YawsPid, Data)</code></p>
<dd>A synchronous version of the above function. This synchronous version must always be used when the producer of the stream is faster than the consumer. This is usually the case since the client is the WWW browser. </p>
<dt><code>stream_chunk_end(YawsPid)</code></p>
<dd>When the process discussed above is done delivering data, it must call this function to let the yaws content delivering process finish up the HTTP transaction. </p>
<dt><code>stream_process_deliver(Socket, IoList)</code></p>
<dd>Yaws allows application processes to deliver data directly to the client. The application tells yaws about such a process by returning <code>{streamcontent_from_pid, MimeType, Pid}</code> from its <code>out/1</code> function. In this case, <i>Pid</i> uses the <code>stream_process_deliver/2</code> function to deliver data to the client. The application gets <i>Socket</i> from <i>Arg#arg.clisock</i>, and <i>IoList</i> is the data to be sent to the client. </p>
<dt><code>stream_process_deliver_chunk(Socket, IoList)</code></p>
<dd>Same as above but delivers <i>IoList</i> using HTTP chunked transfer format. <i>IoList</i> must have a size greater than zero. The application process delivering the data will have had to have make sure that the HTTP headers of the response indicate chunked transfer mode, either by ensuring no Content-Length header is set or by specifically setting the Transfer-Encoding header to chunked. </p>
<dt><code>stream_process_deliver_final_chunk(Socket, IoList)</code></p>
<dd>If the application process delivering data to the client uses chunked transfer mode, it must call this to deliver the final chunk of the transfer. This tells yaws to create a special final chunk in the format required by the HTTP specification (RFC 2616). <i>IoList</i> may be empty, but if its size is greater than zero, that data will be sent as a separate chunk before the final chunk. </p>
<dt><code>stream_process_end(Socket, YawsPid)</code></p>
<dd>Application processes delivering data directly to clients must call this function to inform yaws that they&#8217;ve finished using <i>Socket</i>. The <i>YawsPid</i> argument will have been passed to the process earlier when yaws sent it a message telling it to proceed with data delivery. Yaws expects <i>Socket</i> to be open. </p>
<dt><code>stream_process_end(closed, YawsPid)</code></p>
<dd>Same as the previous function but the application calls this if it closes the client socket as part of its data delivery process. This allows yaws to continue without assuming the socket is still open and encountering errors due to that assumption. The <i>YawsPid</i> argument will have been passed to the application process earlier when yaws sent it a message telling it to proceed with data delivery. </p>
<dt><code>parse_query(Arg)</code></p>
<dd>This function will parse the query part of the URL. It will return a {Key, Value} list of the items supplied in the query part of the URL. </p>
<dt><code>queryvar(Arg, VarName)</code></p>
<dd>This function is automatically included from yaws_api in all<br />
&nbsp;<wbr>.yaws pages. It is used to search for a variable in the querypart of the url. Returns {ok, Val} or undefined. If a variable is defined multiple times, the function may also return <i>{Val1, &#8230;.}</i>. </p>
<dt><code>parse_post(Arg)</code></p>
<dd>This function will parse the POST data as supplied from the browser. It will return a {Key, Value} list of the items set by the browser. </p>
<dt><code>postvar(Arg, VarName)</code></p>
<dd>This function is automatically included from yaws_api in all<br />
&nbsp;<wbr>.yaws pages. It is used to search for a variable in the POSTed data from the client. Returns {ok, Val} or undefined. If a variable is defined multiple times, the function may also return <i>{Val1, &#8230;.}</i>. </p>
<dt><code>getvar(Arg, VarName)</code></p>
<dd>This function looks at the HTTP request method from the client and invokes postvar/2 if it is a POST from the client and queryvar/2 if it is a GET request from the client. </p>
<dt><code>parse_multipart_post(Arg)</code></p>
<dd>If the browser has set the Content-Type header to the value &quot;multipart/form-data&quot;, which is the case when the browser wants to upload a file to the server the following happens: </p>
<p> If the function returns <code>{result, Res}</code> no more data will come from the browser. </p>
<p> If the function returns <code>{cont, Cont, Res}</code> the browser will supply more data. (The file was to big to come in one read) </p>
<p> This indicates that there is more data to come and the out/1 function should return {get_more, Cont, User_state} where User_state might usefully be a File Descriptor. The Res value is a list of either: <code>{head, {Name, Headers}}</code> | <code>{part_body, Binary}</code> | <code>{body, Binary}</code> </p>
<p> The function returns <code>{error, Reason}</code> when an error occurred during the parsing. </p>
<p> Example usage could be: <i> </i></p>
<pre> &lt;erl&gt;
 out(A) -&gt;
 case yaws_api:parse_multipart_post(A) of
 {cont, Cont, Res} -&gt;
 St = handle_res(A, Res),
 {get_more, Cont, St};
 {result, Res} -&gt;
 handle_res(A, Res),
 {html, f(&quot;&lt;pre&gt;Done &lt;/pre&gt;&quot;,[])};
 {error, Reason} -&gt;
 {html, f(&quot;An error occured: ~p&quot;, [Reason])}
 end.
 handle_res(A, [{head, {Name, _Hdrs}}|T]) -&gt;
 io:format(&quot;head:~p~n&quot;,[Name]),
 handle_res(A, T);
 handle_res(A, [{part_body, Data}|T]) -&gt;
 io:format(&quot;part_body:~p~n&quot;,[Data]),
 handle_res(A, T);
 handle_res(A, [{body, Data}|T]) -&gt;
 io:format(&quot;body:~p~n&quot;,[Data]),
 handle_res(A, T);
 handle_res(A, []) -&gt;
 io:format(&quot;End_res~n&quot;).
 &lt;/erl&gt;</pre>
<dt><code>new_cookie_session(Opaque)</code></p>
<dd>Create a new cookie based session, the yaws system will set the cookie. The new random generated cookie is returned from this function. The Opaque argument will typically contain user data such as user name and password </p>
<dt><code>new_cookie_session(Opaque, TTL)</code></p>
<dd>As above, but allows to set a session specific time-out value, overriding the system specified time-out value. </p>
<dt><code>new_cookie_session(Opaque, TTL, CleanupPid)</code></p>
<dd>As above, but also sends a message <i>{yaws_session_end, Reason, Cookie, Opaque}</i> to the provided CleanuPid where Reason can be either of <i>timeout</i> or <i>normal</i>. The <i>Cookie</i> is the HTTP cookie as returned by <i>new_session()</i> and the Opaque is the user provided Opaque parameter to <i>new_session()</i>. The purpose of the feature is to cleanup resources assigned to the session. </p>
<dt><code>cookieval_to_opaque(CookieVal)</code></p>
<dd>
<dt><code>print_cookie_sessions() </code></p>
<dd>
<dt><code>replace_cookie_session(Cookie, NewOpaque)</code></p>
<dd>
<dt><code>delete_cookie_session(Cookie)</code></p>
<dd>
<dt><code>setconf(Gconf, Groups)</code></p>
<dd>This function is intended for embedded mode in yaws. It makes it possible to load a yaws configuration from another data source than /etc/yaws.conf, such as a database. If yaws is started with the environment <i>{embedded, true}</i>, yaws will start with an empty default configuration, and wait for some other program to execute a <i>setconf/2</i> The Gconf is a <i>#gconf{}</i> record and the Group variable is a list of lists of <i>#sconf{}</i> records. Each sublist must contain <i>#sconf{}</i> records with the same IP/Port listen address. To create a suitable initial #gconf{} record see the code in yaws_config:make_default_gconf/2. Especially the <i>yaws_dir</i> parameter is important to get right. </p>
<dt><code>url_decode(Str)</code></p>
<dd>Decode url-encoded string. A URL encoded string is a string where all alfa numeric characters and the the character _ are preserved and all other characters are encode as &quot;%XY&quot; where X and Y are the hex values of the least respective most significant 4 bits in the 8 bit character. </p>
<dt><code>url_encode(Str)</code></p>
<dd>Url-encodes a string. All URLs in HTML documents must be URL encoded. </p>
<dt><code>get_sslsocket(Socket)</code></p>
<dd>Returns a socket for SSL sockets or the atom <i>undefined</i> for non-SSL sockets. Useful for applications that have to deal with both SSL and non-SSL sockets. </p>
<dt><code>get_listen_port(Sconf)</code></p>
<dd>Return the actual port number used by the listen socket of the virtual server indicated by the function argument, an <i>#sconf{}</i> record instance. If successful, returns the requested port number, or returns <i>{error, not_found}</i> if the function argument does not match any known virtual server. This function is useful for retrieving the actual port number when, e.g. for testing purposes, a virtual server is configured to use port 0, which will cause it to have an ephemeral port assigned by the operating system. </p>
<dt><code>reformat_header(H)</code></p>
<dd>Returns a list of reformatted header values from a #headers{} record. The return list is suitable for retransmit. </p>
<dt><code>reformat_header(H, FormatFun)</code></p>
<dd>Returns a list of reformatted header values from a #headers{} record, with each element of the list formatted via a call to <i>FormatFun</i>. This enables converting #headers{} records into various lists of headers and their values. Note that sometimes the <i>Set-Cookie</i> header will contain a tuple value of the form <i>{multi, ValueList}</i> &#8212; see <i>merge_header/2</i> below for details &#8212; so formatting functions should be prepared to handle such a tuple. They should handle it by formatting each member of <i>ValueList</i> as a separate <i>Set-Cookie</i> header, then returning all such header-value pairs in a list. Note that this implies that sometimes the return values of <i>reformat_header/1</i> and <i>reformat_header/2</i> can be a multi-level list. The <i>{multi, ValueList}</i> construct results only from calls to <i>merge_header/2</i> or <i>merge_header/3</i>, where multiple values are set in separate calls for the same header. </p>
<dt><code>set_header(Headers, {Header, Value})</code></p>
<dd>Sets header <i>Header</i> with value <i>Value</i> in the #headers{} record <i>Headers</i>, and returns a new #headers{} record. Using the atom <i>undefined</i> for <i>Value</i> effectively deletes the header, same as <i>delete_header/2</i>. </p>
<dt><code>set_header(Headers, Header, Value)</code></p>
<dd>Same as <i>set_header/2</i> above, except <i>Header</i> and <i>Value</i> are not passed in a tuple. </p>
<dt><code>merge_header(Headers, {Header, Value})</code></p>
<dd>Merges value <i>Value</i> for header <i>Header</i> with any existing value for that header in the #headers{} record <i>Headers</i>, and returns a new #headers{} record. Using the atom <i>undefined</i> for <i>Value</i> simply returns <i>Headers</i>. Otherwise, <i>Value</i> is merged with any existing value already present in the <i>Headers</i> record for header <i>Header</i>, comma-separated from that existing value. If no such value exists in the <i>Headers</i> record, the effect is the same as <i>set_header/2</i>. Note that for the <i>Set-Cookie</i> header, values are not comma-separated but are instead collected into a tuple <i>{multi, ValueList}</i> where <i>ValueList</i> is the collection of <i>Set-Cookie</i> values. This implies that any formatting fun passed to <i>reformat_header/2</i> must be prepared to handle such tuples. </p>
<dt><code>merge_header(Headers, Header, Value)</code></p>
<dd>Same as <i>merge_header/2</i> above, except <i>Header</i> and <i>Value</i> are not passed in a tuple. </p>
<dt><code>get_header(Headers, Header)</code></p>
<dd>Gets the value of header <i>Header</i> from the #headers{} record <i>Headers</i> and returns it. If the header isn&#8217;t set, the atom <i>undefined</i> is returned. </p>
<dt><code>delete_header(Headers, Header)</code></p>
<dd>Deletes any value set for header <i>Header</i> in the #headers{} record <i>Headers</i>, and returns a new #headers{} record. </p>
<dt><code>request_url(ARG)</code></p>
<dd>Return the url as requested by the client. Return value is a #url{} record as defined in yaws_api.hrl </p>
<dt><code>parse_url(Str)</code></p>
<dd>Parse URL in a string, returns a #url record </p>
<dt><code>format_url(UrlRecord)</code></p>
<dd>Takes a #url record a formats the Url as a string </p>
<dt><code>call_cgi(Arg, Scriptfilename)</code></p>
<dd>Calls an executable CGI script, given by its full path. Used to make `.yaws&#8217; wrappers for CGI programs. This function usually returns <i>streamcontent</i>. </p>
<dt><code>call_cgi(Arg, Exefilename, Scriptfilename)</code></p>
<dd>Like before, but calls <i>Exefilename</i> to handle the script. The file name of the script is handed to the executable via a CGI meta variable. </p>
<dt><code>call_fcgi_responder(Arg)</code></p>
<dd>Calls a FastCGI responder. The address and port of the FastCGI application server are taken from the server configuration (see yaws.conf). Used to make `.yaws&#8217; wrappers for FastCGI responders. Returns the same return values as out/1 (see below). </p>
<dt><code>call_fcgi_responder(Arg, Options)</code></p>
<dd>Same as above, but Options overrides the defaults from the server configuration: </p>
<p> <i> </i></p>
<pre>Options = [Option]
Option -- one of the following:</pre>
<p><code>{app_server_host, string() | ip_address()}</code> The hostname or the IP address of the FastCGI application server. </p>
<p> <code>{app_server_port, 0..65535}</code> The TCP port number of the FastCGI application server. </p>
<p> <code>{path_info, string()}</code> Override default pathinfo in Arg#arg.pathinfo. </p>
<p> <code>{extra_env, ExtraEnv}</code> Override default pathinfo in Arg#arg.pathinfo. </p>
<p> <i> </i></p>
<pre>ExtraEnv = [Var]
Var = {Name, Value}
Name = string()
Value = string()</pre>
<p><code>{trace_protocol, boolean()}</code> Enable or disable tracing of FastCGI protocol messages as info log messages. </p>
<p> <code>{log_app_error, boolean()}</code> Enable or disable logging of application error messages: output to stderr and non-zero exit value. </p>
<dt><code>call_fcgi_authorizer(Arg) -&gt; {allowed, Out} | {denied, Out}</code></p>
<dd>Calls a FastCGI authorizer. The address and port of the FastCGI application server are taken from the server configuration (see yaws.conf). Used to make `.yaws&#8217; wrappers for FastCGI authorizers. Variables contains the values of the variables returned by the FastCGI application server in the &quot;Variable-XXX: YYY&quot; headers. </p>
<p> If access is denied, Out contains the complete response returned by the FastCGI application server. This response is typically returned as-is to the HTTP client. </p>
<p> If access is allowed, Out contains the response returned by the FastCGI application server minus the body (i.e. minus the content) which should be ignored per the FastCGI specification. This response is typically not returned to the HTTP client. The calling application module may wish to inspect the response, for example by extracting variables (see fcgi_extract_variables below) or by inspecting the headers returned by the FastCGI application server. </p>
<p> <i> </i></p>
<pre>Out -- See return values for out/1 below</pre>
<dt><code>call_fcgi_authorizer(Arg, Options) -&gt; {allowed, Out} | {denied, Out}</code></p>
<dd>Same as above, but Options overrides the defaults from the server configuration. See call_fcgi_responder/2 above for a description of Options. </p>
<dt><code>fcgi_extract_variables(Out) -&gt; [{Name, Value}]</code></p>
<dd>Extracts the environment variables from a FastCGI authorizer response by looking for headers of the form &quot;Variable-Name: Value&quot;. </p>
<p> <i> </i></p>
<pre>Name = string() -- The name of the variable (the &quot;Variable-&quot; prefix
has already been removed).
Value = string() -- The value of the variable.</pre>
<dt><code>dir_listing(Arg)</code></p>
<dd>Perform a directory listing. Can be used in special directories when we don&#8217;t want to turn on dir listings for the entire server. Always returns ok. </p>
</dl>
<h2>RETURN VALUES from out/1</h2>
<p>The out/1 function can return different values to control the behavior of the server. </p>
<dl>
<dt><code>{html, DeepList}</p>
<dd>This assumes that DeepList is formatted HTML code. The code will be inserted in the page. </p>
<dt>{ehtml|exhtml, Term}</code></p>
<dd>This will transform the erlang term Term into a stream of HTML content. The exhtml variant transforms into strict XHTML code. The basic syntax of Term is </p>
<p> <i> </i></p>
<pre>EHTML = [EHTML] | {Tag, Attrs, Body} | {Tag, Attrs} | {Tag} |
 binary() | character()
Tag = atom()
Attrs = [{Key, Value}] or {EventTag, {jscall, FunName, [Args]}}
Key = atom()
Value = string()
Body = EHTML</pre>
<p>For example, <i>{p, [], &quot;Howdy&quot;}</i> expands into &quot;&lt;p&gt;Howdy&lt;/p&gt;&quot; and </p>
<p> <i> </i></p>
<pre>{form, [{action, &quot;a.yaws&quot;}],
 {input, [{type,text}]}}</pre>
<p>expands into </p>
<p> <i> </i></p>
<pre>&lt;form action=&quot;a.yaws&quot;
 &lt;input type=&quot;text&quot;&gt;
&lt;/form&gt;</pre>
<p>It may be more convenient to generate erlang tuples than plain html code. </p>
<dt><code>{content, MimeType, Content}</code></p>
<dd>This function will make the web server generate different content than HTML. This return value is only allowed in a yaws file which has only one &lt;erl&gt; &lt;/erl&gt; part and no html parts at all. </p>
<dt><code>{streamcontent, MimeType, FirstChunk}</code></p>
<dd>This return value plays the same role as the <i>content</i> return value above. </p>
<p> However it makes it possible to stream data to the client if the yaws code doesn&#8217;t have access to all the data in one go. (Typically if a file is very large or if data arrives from back end servers on the network. </p>
<dt><code>{streamcontent_with_timeout, MimeType, FirstChunk, Timeout}</code></p>
<dd>Similar to above, but with an explicit timeout. The default timeout is 30 secs. I.e if the application fails to deliver data to the Yaws process, the streaming will stop. This is often not the desired behaviour in Comet/Ajax applications. It&#8217;s possible to provide &#8216;infinity&#8217; as timeout. </p>
<dt><code>{streamcontent_from_pid, MimeType, Pid}</code></p>
<dd>This return value is similar to the <i>streamcontent</i> return value above. </p>
<p> However it makes it possible to stream data to the client directly from an application process to the socket. This approach can be useful for applications that employ long-polling (Comet) techniques, for example, and for applications wanting to avoid buffering data or avoid HTTP chunked mode transfer for streamed data. </p>
<dt><code>{streamcontent_with_size, Sz, MimeType, FirstChunk}</code></p>
<dd>This return value is similar to the <i>streamcontent</i> return value above. </p>
<p> However it makes it possible to stream data to the client by setting the content length of the response. As the opposite of other ways to stream data, in this case, the response is not chunked encoded. </p>
<dt><code>{header, H}</code></p>
<dd>Accumulates a HTTP header. The trailing CRNL which is supposed to end all HTTP headers must NOT be added. It is added by the server. The following list of headers are given special treatment. </p>
<p> <i>{connection, What}</i> </p>
<p> This sets the Connection: header. If <i>What</i> is the special value <i>&quot;close&quot;</i>, the connection will be closed once the yaws page is delivered to the client. </p>
<p> <i>{server, What}</i> </p>
<p> Sets the Server: header. By setting this header, the server&#8217;s signature will be dynamically overloaded. </p>
<p> <i>{location, Url}</i> </p>
<p> Sets the Location: header. This header is typically combined with the <i>{status, 302}</i> return value. </p>
<p> <i>{cache_control, What}</i> </p>
<p> Sets the Cache-Control: header. </p>
<p> <i>{expires, What}</i> </p>
<p> Sets the Expires: header. </p>
<p> <i>{date, What}</i> </p>
<p> Sets the Date: header. </p>
<p> <i>{allow, What}</i> </p>
<p> Sets the Allow: header. </p>
<p> <i>{last_modified, What}</i> </p>
<p> Sets the Last-Modified: header. </p>
<p> <i>{etag, What}</i> </p>
<p> Sets the Etag: header. </p>
<p> <i>{set_cookie, Cookie}</i> </p>
<p> Prepends a Set-Cookie: header to the list of previously set Set-Cookie: headers. </p>
<p> <i>{content_range, What}</i> </p>
<p> Sets the Content-Range: header. </p>
<p> <i>{content_type, MimeType}</i> </p>
<p> Sets the Content-Type: header. </p>
<p> <i>{content_encoding, What}</i> </p>
<p> Sets the Content-Encoding: header. If this header is defined, no deflate is performed by Yaws. So you can compress data by yourself. </p>
<p> <i>{content_length, Len}</i> </p>
<p> Normally yaws will ship Yaws pages using Transfer-Encoding: chunked. This is because we generally can&#8217;t know how long a yaws page will be. If we for some reason want to force a Content-Length: header (and we actually do know the length of the content, we can force yaws to not ship the page chunked. </p>
<p> <i>{transfer_encoding, What}</i> </p>
<p> Sets the Transfer-Encoding: header. </p>
<p> <i>{www_authenticate, What}</i> </p>
<p> Sets the WWW-Authenticate: header. </p>
<p> <i>{vary, What}</i> </p>
<p> Sets the Vary: header. </p>
<p> All other headers must be added using the normal HTTP syntax. Example: </p>
<p> <i>{header, {&quot;My-X-Header&quot;, &quot;gadong&quot;}}</i> or <i>{header, &quot;My-X-Header: gadong&quot;}</i> </p>
<dt><code>{header, {HeaderName, erase}}</code></p>
<dd>Clears the header named <i>HeaderName</i> from the accumulated headers. </p>
<dt><code>{allheaders, HeaderList}</code></p>
<dd>Will clear all previously accumulated headers and replace them. </p>
<dt><code>{status, Code}</code></p>
<dd>Will set another HTTP status code than 200. </p>
<dt><code>break</code></p>
<dd>Will stop processing of any consecutive chunks of erl or html code in the yaws file. </p>
<dt><code>ok</code></p>
<dd>Do nothing. </p>
<dt><code>flush</code></p>
<dd>Flush remaining data sent by the client. </p>
<dt><code>{redirect, Url}</code></p>
<dd>Erase all previous headers and accumulate a single Location header. Set the status code. </p>
<dt><code>{redirect_local, Path}</code></p>
<dd>Does a redirect to the same S<a href="cheme://Host:Port/Path">cheme://Host:Port/Path</a> as we currently are executing in. </p>
<dt><code>{get_more, Cont, State}</code></p>
<dd>When we are receiving large POSTs we can return this value and be invoked again when more Data arrives. </p>
<dt><code>{page, Page}</code></p>
<dd>Make Yaws returns a different page than the one being requested. <i>Page</i> is a Request-URI, so it must be url-encoded and can contain a query-string. </p>
<dt><code>{page, {Options, Page}}</code></p>
<dd>Like the above, but supplying an additional deep list of options. Supported option types are: </p>
<p> <i>{status, C}</i> &#8211; Set the HTTP response status code <i>C</i> for page <i>Page</i>. </p>
<p> <i>{header, H}</i> &#8211; Accumulate the HTTP header <i>H</i> for page <i>Page</i>. </p>
<p> <i>{disable_cache, Bool}</i> &#8211; if set to <i>true</i>, disable the cache of <i>Page</i> for this call. </p>
<dt><code>{ssi, File, Delimiter, Bindings}</code></p>
<dd>Server side include File and macro expansion in File. Each occurrence of a string, say &quot;xyz&quot;, inside File which is inside Delimiters is replaced with the corresponding value in Bindings. </p>
<p> Example: Delimiter = %% </p>
<p> File contains the string &#8230;. %%xyz%% &#8230;.. </p>
<p> Bindings contain the tuple {&quot;xyz&quot;, &quot;Dingbat&quot;} </p>
<p> The occurrence of %%xyz%% in File will be replaced with &quot;Dingbat&quot; in the Server side included output. </p>
<p> The {ssi, File, Delimiter, Bindings} statement can also occur inside a deep ehtml structure. </p>
<dt><code>{bindings, [{Key1, Value2}, {Key2, Value2} &#8230;..]}</code></p>
<dd>Establish variable bindings that can be used in the page. </p>
<p> All bindings can then be used in the rest of yaws code (in HTML source and within erl tags). In HTML source %%Key%% is expanded to Value and within erl tags <i>yaws_api:binding(Key)</i> can be used to extract Value and <i>yaws_api:binding_exists(Key)</i> can be used to check for the existence of a binding. </p>
<dt><code>{yssi, YawsFile}</code></p>
<dd>Include a yaws file. Compile it and expand as if it had occured inline. </p>
<dt><code>[ListOfValues]</code></p>
<dd>It is possible to return a deep list of the above defined return values. Any occurrence of <i>streamcontent</i>, <i>streamcontent_with_timeout</i>, <i>streamcontent_with_size</i>, <i>streamcontent_from_pid</i>, <i>get_more</i>, <i>page</i> or <i>break</i> in this list is legal only if it is the last position of the list. If not, remaining values in the list are ignored. </p>
</dl>
<h2>Author</h2>
<p>Written by Claes Wikstrom</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-yaws-conf/">yaws.conf</a></code>(5) <code><a href="/docs/linux/man/1-erl/">erl</a></code>(1) </p>
