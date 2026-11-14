---
title: "https(1)"
name: "https"
section: "1"
letter: "h"
url: "/docs/linux/man/1-https/"
description: "httpie – CLI, cURL-like tool for humans"
---

<h2 class="name">NAME</h2>
<p> httpie &#8211; CLI, cURL-like tool for humans </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>http</code></p>
<dd> [&#8211;json] [&#8211;form] [&#8211;pretty {all,colors,format,none}] [&#8211;style STYLE] [&#8211;print WHAT] [&#8211;verbose] [&#8211;headers] [&#8211;body] [&#8211;stream] [&#8211;output FILE] [&#8211;download] [&#8211;continue] [&#8211;session SESSION_NAME_OR_PATH | &#8211;session-read-only SESSION_NAME_OR_PATH] [&#8211;auth USER[:PASS]] [&#8211;auth-type {basic,digest}] [&#8211;proxy PROTOCOL:PROXY_URL] [&#8211;follow] [&#8211;verify VERIFY] [&#8211;cert CERT] [&#8211;cert-key CERT_KEY] [&#8211;timeout SECONDS] [&#8211;check-status] [&#8211;ignore-stdin] [&#8211;help] [&#8211;version] [&#8211;traceback] [&#8211;debug]<br />
 [METHOD] <i>URL</i> [REQUEST_ITEM [REQUEST_ITEM &#8230;]] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>HTTPie</code> is a CLI HTTP utility built out of frustration with existing tools. The goal is to make CLI interaction with HTTP-based services as human-friendly as possible. </p>
<p> HTTPie does so by providing an http command that allows for issuing arbitrary HTTP requests using a simple and natural syntax and displaying colorized responses. </p>
<h2>OPTIONS</h2>
<h3>Positional Arguments</h3>
<p> These arguments come after any flags and in the order they are listed here. Only URL is required.</p>
<dl>
<dt>METHOD</p>
<dd>
<p> The HTTP method to be used for the request (GET, POST, PUT, DELETE, &#8230;).<br />
 This argument can be omitted in which case HTTPie will use POST if there is some data to be sent, otherwise GET: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<tt>$&nbsp;http example.org&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;=&gt;&nbsp;GET</tt> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<tt>$&nbsp;http example.org hello=world&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;=&gt;&nbsp;POST</tt> </p>
<dt>URL</p>
<dd>
<p> The scheme defaults to &#8216;<a rel="nofollow" href="http://'">http://&#8217;</a> if the URL does not include one. </p>
<p> You can also use a shorthand for localhost </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<tt>$&nbsp;http :3000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;=&gt;&nbsp;<a rel="nofollow" href="http://localhost:3000">http://localhost:3000</a></tt> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<tt>$&nbsp;http :/foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;=&gt;&nbsp;<a rel="nofollow" href="http://localhost/foo">http://localhost/foo</a></tt> </p>
<dt>REQUEST_ITEM</p>
<dd>
<p> Optional key-value pairs to be included in the request. The separator used determines the type: </p>
<p> <code>&#8216;:&#8217;</code> HTTP headers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Referer:<a rel="nofollow" href="http://httpie.org">http://httpie.org</a><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Cookie:foo=bar<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;User-Agent:bacon/1.0 </p>
<p> <code>&#8216;==&#8217;</code> URL parameters to be appended to the request URI<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;search==httpie<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>&#8216;=&#8217;</code> Data fields to be serialized into a JSON object (with <code>&#8211;json</code>, <code>-j</code>) or form data (with <code>&#8211;form</code>, <code>-f</code>)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name=HTTPie<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;language=Python<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;description=&#8217;CLI HTTP client&#8217; </p>
<p> <code>&#8216;:=&#8217;</code> Non-string JSON data fields (only with <code>&#8211;json</code>, <code>-j</code>)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;awesome:=true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;amount:=42<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;colors:='[&quot;red&quot;,&nbsp;&quot;green&quot;,&nbsp;&quot;blue&quot;]&#8217; </p>
<p> <code>&#8216;@&#8217;</code> Form file fields (only with <code>&#8211;form</code>, <code>-f</code>)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cs@~/Documents/CV.pdf </p>
<p> <code>&#8216;=@&#8217;</code> A data field like &#8216;=&#8217;, but takes a file path and embeds its content:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;essay=@Documents/essay.txt </p>
<p> <code>&#8216;:=@&#8217;</code> A raw JSON field like &#8216;:=&#8217;, but takes a file path and embeds its content:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;package:=@./package.json </p>
<p> You can use a backslash to escape a colliding separator in the field name: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;field-name-with\:colon=value </p>
</dl>
<h3>Predefined Content Types:</h3>
<dl>
<dt> <code>&#8211;json</code>, <code>-j</code></p>
<dt>
<dd> (default) Data items from the command line are serialized as a JSON object.</p>
<dd>The Content-Type and Accept headers are set to application/json (if not specified).</p>
<dt> <code>&#8211;form</code>, <code>-f</code></p>
<dt>
<dd>
<dd>Data items from the command line are serialized as form fields.</p>
<dt>
<dd> The Content-Type is set to application/x-www-form-urlencoded (if not specified). The presence of any file fields results in a multipart/form-data request.</dl>
<h3>Output Processing:</h3>
<dl>
<dt> <code>&#8211;pretty</code> {all,colors,format,none}</p>
<dt>
<dd>
<dd>Controls output processing. The value can be &quot;none&quot; to not prettify the output (default for redirected output), &quot;all&quot; to apply both colors and formatting (default for terminal output), &quot;colors&quot;, or &quot;format&quot;.</p>
<dt> <code>&#8211;style</code> STYLE, <code>-s</code> STYLE</p>
<dt>
<dd>
<dd>Output coloring style (default is &quot;solarized&quot;). One of:</p>
<dt>
<dd> algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly, fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark, paraiso-light, pastie, perldoc, rrt, solarized, tango, trac, vim, vs, xcode</p>
<dt>
<dd> For this option to work properly, please make sure that the $TERM environment variable is set to &quot;xterm-256color&quot; or similar (e.g., via `export TERM=xterm-256color&#8217; in your ~/.bashrc).</dl>
<h3>Output Options:</h3>
<dl>
<dt> <code>&#8211;print</code> WHAT, <code>-p</code> WHAT</p>
<dt>
<dd>
<dd>String specifying what the output should contain:</p>
<dt>
<dd> &#8216;H&#8217; request headers &#8216;B&#8217; request body &#8216;h&#8217; response headers &#8216;b&#8217; response body</p>
<dt>
<dd> The default behaviour is &#8216;hb&#8217; (i.e., the response headers and body is printed), if standard output is not redirected. If the output is piped to another program or to a file, then only the response body is printed by default.</p>
<dt> <code>&#8211;verbose</code>, <code>-v</code></p>
<dt>
<dd>
<dd>Print the whole request as well as the response. Shortcut for <code>&#8211;print</code>=<i>,HBbh/</i>.</p>
<dt> <code>&#8211;headers</code>, <code>-h</code></p>
<dt>
<dd>
<dd>Print only the response headers. Shortcut for <code>&#8211;print</code>=<i>,h/</i>.</p>
<dt> <code>&#8211;body</code>, <code>-b</code></p>
<dt>
<dd>
<dd>Print only the response body. Shortcut for <code>&#8211;print</code>=<i>,b/</i>.</p>
<dt> <code>&#8211;stream</code>, <code>-S</code></p>
<dt>
<dd>
<dd>Always stream the output by line, i.e., behave like `tail <code>-f</code>&#8216;.</p>
<dt>
<dd> Without <code>&#8211;stream</code> and with <code>&#8211;pretty</code> (either set or implied), HTTPie fetches the whole response before it outputs the processed data.</p>
<dt>
<dd> Set this option when you want to continuously display a prettified long-lived response, such as one from the Twitter streaming API.</p>
<dt>
<dd> It is useful also without <code>&#8211;pretty</code>: It ensures that the output is flushed more often and in smaller chunks.</p>
<dt> <code>&#8211;output</code> FILE, <code>-o</code> FILE</p>
<dt>
<dd>
<dd>Save output to FILE. If <code>&#8211;download</code> is set, then only the response body is saved to the file. Other parts of the HTTP exchange are printed to stderr.</p>
<dt> <code>&#8211;download</code>, <code>-d</code></p>
<dt>
<dd>
<dd>Do not print the response body to stdout. Rather, download it and store it in a file. The filename is guessed unless specified with <code>&#8211;output</code> [filename]. This action is similar to the default behaviour of wget.</p>
<dt> <code>&#8211;continue</code>, <code>-c</code></p>
<dt>
<dd>
<dd>Resume an interrupted download. Note that the <code>&#8211;output</code> option needs to be specified as well.</dl>
<h3>Sessions:</h3>
<dl>
<dt> <code>&#8211;session</code> SESSION_NAME_OR_PATH</p>
<dt>
<dd>
<dd>Create, or reuse and update a session. Within a session, custom headers, auth credential, as well as any cookies sent by the server persist between requests.</p>
<dt>
<dd> Session files are stored in:</p>
<dt>
<dd> /home/gaetano/.httpie/sessions/&lt;HOST&gt;/&lt;SESSION_NAME&gt;.json.</p>
<dt> <code>&#8211;session-read-only</code> SESSION_NAME_OR_PATH</p>
<dt>
<dd>
<dd>Create or read a session without updating it form the request/response exchange.</dl>
<h3>Authentication:</h3>
<dl>
<dt> <code>&#8211;auth</code> USER[:PASS], <code>-a</code> USER[:PASS]</p>
<dt>
<dd>
<dd>If only the username is provided (<code>-a</code> username), HTTPie will prompt for the password.</p>
<dt> <code>&#8211;auth-type</code> {basic,digest}</p>
<dt>
<dd>
<dd>The authentication mechanism to be used. Defaults to &quot;basic&quot;.</p>
<dt>
<dd> &quot;basic&quot;: Basic HTTP auth &quot;digest&quot;: Digest HTTP auth</dl>
<h3>Network:</h3>
<dl>
<dt> <code>&#8211;proxy</code> PROTOCOL:PROXY_URL</p>
<dt>
<dd>
<dd>String mapping protocol to the URL of the proxy (e.g. http:<a rel="nofollow" href="http://foo.bar:3128">http://foo.bar:3128</a>). You can specify multiple proxies with different protocols.</p>
<dt> <code>&#8211;follow</code></p>
<dt>
<dd>
<dd>Set this flag if full redirects are allowed (e.g. re-POST-ing of data at new Location).</p>
<dt> <code>&#8211;verify</code> VERIFY</p>
<dt>
<dd>
<dd>Set to &quot;no&quot; to skip checking the host&#8217;s SSL certificate. You can also pass the path to a CA_BUNDLE file for private certs. You can also set the REQUESTS_CA_BUNDLE environment variable. Defaults to &quot;yes&quot;.</p>
<dt> <code>&#8211;cert</code> CERT</p>
<dt>
<dd>
<dd>You can specify a local cert to use as client side SSL certificate. This file may either contain both private key and certificate or you may specify <code>&#8211;cert-key</code> separately.</p>
<dt> <code>&#8211;cert-key</code> CERT_KEY</p>
<dt>
<dd>
<dd>The private key to use with SSL. Only needed if <code>&#8211;cert</code> is given and the certificate file does not contain the private key.</p>
<dt> <code>&#8211;timeout</code> SECONDS</p>
<dt>
<dd>
<dd>The connection timeout of the request in seconds. The default value is 30 seconds.</p>
<dt> <code>&#8211;check-status</code></p>
<dt>
<dd>
<dd>By default, HTTPie exits with 0 when no network or other fatal errors occur. This flag instructs HTTPie to also check the HTTP status code and exit with an error if the status indicates one.</p>
<dt>
<dd> When the server replies with a 4xx (Client Error) or 5xx (Server Error) status code, HTTPie exits with 4 or 5 respectively. If the response is a 3xx (Redirect) and <code>&#8211;follow</code> hasn&#8217;t been set, then the exit status is 3. Also an error message is written to stderr if stdout is redirected.</dl>
<h3>Troubleshooting:</h3>
<dl>
<dt> <code>&#8211;ignore-stdin</code></p>
<dt>
<dd>
<dd>Do not attempt to read stdin.</p>
<dt> <code>&#8211;help</code></p>
<dt>
<dd>
<dd>Show this help message and exit.</p>
<dt> <code>&#8211;version</code></p>
<dt>
<dd>
<dd>Show version and exit.</p>
<dt> <code>&#8211;traceback</code></p>
<dt>
<dd>
<dd>Prints exception traceback should one occur.</p>
<dt> <code>&#8211;debug</code></p>
<dt>
<dd>
<dd>Prints exception traceback should one occur, and also other information that is useful for debugging HTTPie itself and for reporting bugs.</dl>
<p> For every <code>&#8211;OPTION</code> there is also a <code>&#8211;no-OPTION</code> that reverts OPTION to its default value. </p>
<h2>REPORTING BUGS</h2>
<p> Suggestions and bug reports are greatly appreciated: &lt;<a rel="nofollow" href="https://github.com/jakubroztocil/httpie/issues">https://github.com/jakubroztocil/httpie/issues</a>&gt; </p>
<h2>AUTHOR</h2>
<p> httpie was written by Jakub Roztocil &lt;jakub [at] roztocil.name&gt;. </p>
<p> This manual page was written for the Debian project (and may be used by others). </p>
<h2>Index</h2>
