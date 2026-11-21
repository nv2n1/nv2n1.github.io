---

title: "varnish-cli(7)"
name: "varnish-cli"
section: "7"
letter: "v"
url: "/docs/linux/man/7-varnish-cli/"
description: "Varnish CLI – Varnish Command Line Interface"
---

<p> Varnish CLI - Varnish Command Line Interface  </p>
<p>Varnish as a command line interface (CLI) which can control and change most of the operational parameters and the configuration of Varnish, without interrupting the running service. </p>
<p>The CLI can be used for the following tasks: </p>
<dl>
<dt><code>configuration</code></dt>
<dd> <p> You can upload, change and delete VCL files from the CLI. </p>
 </dd>
<dt><code>parameters</code></dt>
<dd> <p> You can inspect and change the various parameters Varnish has available through the CLI. The individual parameters are documented in the <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) man page. </p>
 </dd>
<dt><code>bans</code></dt>
<dd> <p> Bans are filters that are applied to keep Varnish from serving stale content. When you issue a ban Varnish will not serve any <i>banned</i> object from cache, but rather re-fetch it from its backend servers. </p>
 </dd>
<dt><code>process management</code></dt>
<dd> <p> You can stop and start the cache (child) process though the CLI. You can also retrieve the lastst stack trace if the child process has crashed. </p>
<p>If you invoke <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) with -T, -M or -d the CLI will be available. In debug mode (-d) the CLI will be in the foreground, with -T you can connect to it with varnishadm or telnet and with -M varnishd will connect back to a listening service <i>pushing</i> the CLI to that service. Please see <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) for details. </p>
 </dd></dl>
<h3>Syntax</h3>
<p>Commands are usually terminated with a newline. Long command can be entered using sh style <i>here documents</i>. The format of here-documents is: </p>
<pre><code>&lt;&lt; word
     here document
word
</code></pre>
<p> <i>word</i> can be any continuous string choosen to make sure it doesn&#8217;t appear naturally in the following <i>here document</i>. </p>
<p>When using the here document style of input there are no restrictions on lenght. When using newline-terminated commands maximum lenght is limited by the varnishd parameter <i>cli_buffer</i>. </p>
<p>When commands are newline terminated they get <i>tokenized</i> before parsing so if you have significant spaces enclose your strings in double quotes. Within the quotes you can escape characters with \. The n, r and t get translated to newlines, carrage returns and tabs. Double quotes themselves can be escaped with a backslash. </p>
<p>To enter characters in octals use the \nnn syntax. Hexadecimals can be entered with the \xnn syntax.  </p>
<h3>Commands</h3>
<dl>
<dt><code>help [command]</code></dt>
<dd> <p> Show command/protocol help </p>
 </dd>
<dt><code>ping [timestamp]</code></dt>
<dd> <p> Keep connection alive </p>
 </dd>
<dt><code>auth response</code></dt>
<dd> <p> Authenticate. </p>
 </dd>
<dt><code>quit</code></dt>
<dd> <p> Close connection </p>
 </dd>
<dt><code>banner</code></dt>
<dd> <p> Print welcome banner. </p>
 </dd>
<dt><code>status</code></dt>
<dd> <p> Check status of Varnish cache process. </p>
 </dd>
<dt><code>start</code></dt>
<dd> <p> Start the Varnish cache process. </p>
 </dd>
<dt><code>stop</code></dt>
<dd> <p> Stop the Varnish cache process </p>
 </dd>
<dt><code>vcl.load &lt;configname&gt; &lt;filename&gt;</code></dt>
<dd> <p> Compile and load the VCL file under the name provided. </p>
 </dd>
<dt><code>vcl.inline &lt;configname&gt; &lt;quoted_VCLstring&gt;</code></dt>
<dd> <p> Compile and load the VCL data under the name provided. </p>
 </dd>
<dt><code>vcl.use &lt;configname&gt;</code></dt>
<dd> <p> Switch to the named configuration immediately. </p>
 </dd>
<dt><code>vcl.discard &lt;configname&gt;</code></dt>
<dd> <p> Unload the named configuration (when possible). </p>
 </dd>
<dt><code>vcl.list</code></dt>
<dd> <p> List all loaded configuration. </p>
 </dd>
<dt><code>vcl.show &lt;configname&gt;</code></dt>
<dd> <p> Display the source code for the specified configuration. </p>
 </dd>
<dt><code>param.show [-l] [&lt;param&gt;]</code></dt>
<dd> <p> Show parameters and their values. </p>
 </dd>
<dt><code>param.set &lt;param&gt; &lt;value&gt;</code></dt>
<dd> <p> Set parameter value. </p>
 </dd>
<dt><code>panic.show</code></dt>
<dd> <p> Return the last panic, if any. </p>
 </dd>
<dt><code>panic.clear</code></dt>
<dd> <p> Clear the last panic, if any. </p>
 </dd>
<dt><code>storage.list</code></dt>
<dd> <p> List storage devices </p>
 </dd>
<dt><code>backend.list [&lt;backend_expression&gt;]</code></dt>
<dd> <p> List backends. </p>
 </dd>
<dt><code>backend.set_health &lt;backend_expression&gt; &lt;state&gt;</code></dt>
<dd> <p> Set health status on the backends. State is any of auto, healthy or sick values. </p>
 </dd>
<dt><code>ban &lt;field&gt; &lt;operator&gt; &lt;arg&gt; [&amp;&amp; &lt;field&gt; &lt;oper&gt; &lt;arg&gt;]...</code></dt>
<dd> <p> All objects where the all the conditions match will be marked obsolete. </p>
 </dd>
<dt><code>ban.list</code></dt>
<dd> <p> List the active bans. </p>
 </dd></dl>
<h3>Backend Expression</h3>
<p>A backend expression can be a backend name or a combination of backend name, IP address and port in &quot;name(IP address:port)&quot; format. All fields are optional. If no exact matching backend is found, partial matching will be attempted based on the provided name, IP address and port fields.  </p>
<h3>Ban Expressions</h3>
<p>A ban expression consists of one or more conditions. A condition consists of a field, an operator, and an argument. Conditions can be ANDed together with &quot;&amp;&amp;&quot;. </p>
<p>A field can be any of the variables from VCL, for instance req.url, req.http.host or obj.http.set-cookie. </p>
<p>Operators are &quot;==&quot; for direct comparision, &quot;~&quot; for a regular expression match, and &quot;&gt;&quot; or &quot;&lt;&quot; for size comparisons. Prepending an operator with &quot;!&quot; negates the expression. </p>
<p>The argument could be a quoted string, a regexp, or an integer. Integers can have &quot;KB&quot;, &quot;MB&quot;, &quot;GB&quot; or &quot;TB&quot; appended for size related fields.  </p>
<h3>Scripting</h3>
<p>If you are going to write a script that talks CLI to varnishd, the include/cli.h contains the relevant magic numbers. </p>
<p>One particular magic number to know, is that the line with the status code and length field always is exactly 13 characters long, including the NL character. </p>
<p>For your reference the sourcefile lib/libvarnish/cli_common.h contains the functions Varnish code uses to read and write CLI response.  </p>
<h3>How -S/PSK Authentication Works</h3>
<p>If the -S secret-file is given as argument to varnishd, all network CLI connections must authenticate, by proving they know the contents of that file. </p>
<p>The file is read at the time the auth command is issued and the contents is not cached in varnishd, so it is possible to update the file on the fly. </p>
<p>Use the unix file permissions to control access to the file. </p>
<p>An authenticated session looks like this: </p>
<pre><code>critter phk&gt; telnet localhost 1234
Trying ::1...
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
107 59
ixslvvxrgkjptxmcgnnsdxsvdmvfympg
Authentication required.
auth 455ce847f0073c7ab3b1465f74507b75d3dc064c1e7de3b71e00de9092fdc89a
200 193
-----------------------------
Varnish HTTP accelerator CLI.
-----------------------------
Type 'help' for command list.
Type 'quit' to close CLI session.
Type 'start' to launch worker process.
</code></pre>
<p>The CLI status of 107 indicates that authentication is necessary. The first 32 characters of the reponse text is the challenge &quot;ixsl...mpg&quot;. The challenge is randomly generated for each CLI connection, and changes each time a 107 is emitted. </p>
<p>The most recently emitted challenge must be used for calculating the authenticator &quot;455c...c89a&quot;. </p>
<p>The authenticator is calculated by applying the SHA256 function to the following byte sequence: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Challenge string </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Newline (0x0a) character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Contents of the secret file </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Challenge string </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Newline (0x0a) character. </p>
<p>and dumping the resulting digest in lower-case hex. </p>
<p>In the above example, the secret file contained foon and thus: </p>
<pre><code>critter phk&gt; cat &gt; _
ixslvvxrgkjptxmcgnnsdxsvdmvfympg
foo
ixslvvxrgkjptxmcgnnsdxsvdmvfympg
^D
critter phk&gt; hexdump -C _
00000000 69 78 73 6c 76 76 78 72 67 6b 6a 70 74 78 6d 63 |ixslvvxrgkjptxmc|
00000010 67 6e 6e 73 64 78 73 76 64 6d 76 66 79 6d 70 67 |gnnsdxsvdmvfympg|
00000020 0a 66 6f 6f 0a 69 78 73 6c 76 76 78 72 67 6b 6a |.foo.ixslvvxrgkj|
00000030 70 74 78 6d 63 67 6e 6e 73 64 78 73 76 64 6d 76 |ptxmcgnnsdxsvdmv|
00000040 66 79 6d 70 67 0a |fympg.|
00000046
critter phk&gt; sha256 _
SHA256 (_) = 455ce847f0073c7ab3b1465f74507b75d3dc064c1e7de3b71e00de9092fdc89a
critter phk&gt; openssl dgst -sha256 &lt; _
455ce847f0073c7ab3b1465f74507b75d3dc064c1e7de3b71e00de9092fdc89a
</code></pre>
<p>The sourcefile lib/libvarnish/cli_auth.c contains a useful function which calculates the response, given an open filedescriptor to the secret file, and the challenge string. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p>Simple example: All requests where req.url exactly matches the string /news are banned from the cache: </p>
<pre><code>req.url == &quot;/news&quot;
</code></pre>
<p>Example: Ban all documents where the serving host is &quot;example.com&quot; or &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;, and where the Set-Cookie header received from the backend contains &quot;USERID=1663&quot;: </p>
<pre><code>req.http.host ~ &quot;^(?i)(www\.)example.com$&quot; &amp;&amp; obj.http.set-cookie ~ &quot;USERID=1663&quot;
</code></pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> vanrishadm(1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <a href="/docs/linux/man/7-vcl/">vcl</a>(7) </p>
 </dd></dl>
<h2>HISTORY</h2>
<p>The Varnish manual page was written by Per Buer in 2011. Some of the text was taken from the Varnish Cache wiki, the varnishd(7) man page or the Varnish source code.  </p>
<h2>COPYRIGHT</h2>
<p>This document is licensed under the same licence as Varnish itself. See LICENCE for details. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Copyright (c) 2011-2014 Varnish Software AS </p>
 </dd></dl>
