---
title: "linkchecker(1)"
name: "linkchecker"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linkchecker/"
description: "linkchecker – command line client to check HTML documents and websites for broken links"
---

<h2 class="name">NAME</h2>
<p> linkchecker &#8211; command line client to check HTML documents and websites for broken links </p>
<h2>SYNOPSIS</h2>
<p> <code>linkchecker</code> [<i>options</i>] [<i>file-or-url</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> LinkChecker features</p>
<dl>
<dt>&bull;</p>
<dd> recursive and multithreaded checking,</p>
<dt>&bull;</p>
<dd> output in colored or normal text, HTML, SQL, CSV, XML or a sitemap graph in different formats,</p>
<dt>&bull;</p>
<dd> support for HTTP/1.1, HTTPS, FTP, mailto:, news:, nntp:, Telnet and local file links,</p>
<dt>&bull;</p>
<dd> restriction of link checking with URL filters,</p>
<dt>&bull;</p>
<dd> proxy support,</p>
<dt>&bull;</p>
<dd> username/password authorization for HTTP, FTP and Telnet,</p>
<dt>&bull;</p>
<dd> support for robots.txt exclusion protocol,</p>
<dt>&bull;</p>
<dd> support for Cookies</p>
<dt>&bull;</p>
<dd> support for HTML5</p>
<dt>&bull;</p>
<dd> HTML and CSS syntax check</p>
<dt>&bull;</p>
<dd> Antivirus check</p>
<dt>&bull;</p>
<dd> a command line, GUI and web interface</dl>
<h2>EXAMPLES</h2>
<p> The most common use checks the given domain recursively:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker&nbsp;<a rel="nofollow" href="http://www.example.com/">http://www.example.com/</a></code><br />
 Beware that this checks the whole site which can have thousands of URLs. Use the <code>-r</code> option to restrict the recursion depth.<br />
 Don&#8217;t check URLs with <code>/secret</code> in its name. All other links are checked as usual:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker &#8211;ignore-url=/secret mysite.example.com</code><br />
 Checking a local HTML file on Unix:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker ../bla.html</code><br />
 Checking a local HTML file on Windows:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker c:	emp	est.html</code><br />
 You can skip the <code>http://</code> url part if the domain starts with <code>www.</code>:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker&nbsp;<a rel="nofollow" href="http://www.example.com">www.example.com</a></code><br />
 You can skip the <code>ftp://</code> url part if the domain starts with <code>ftp.</code>:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker -r0&nbsp;<a href="ftp://ftp.example.com">ftp.example.com</a></code><br />
 Generate a sitemap graph and convert it with the graphviz dot utility:<br />
&nbsp;<wbr>&nbsp;<code>linkchecker -odot -v&nbsp;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&nbsp;| dot -Tps&nbsp;&gt;&nbsp;sitemap.ps</code></p>
<h2>OPTIONS</h2>
<h3>General options</h3>
<dl>
<dt><code>-f</code><i>FILENAME</i>, <code>&#8211;config=</code><i>FILENAME</i></p>
<dd> Use <i>FILENAME</i> as configuration file. As default LinkChecker uses <code>~/.linkchecker/linkcheckerrc</code>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Help me! Print usage information for this program.</p>
<dt><code>&#8211;stdin</code></p>
<dd> Read list of white-space separated URLs to check from stdin.</p>
<dt><code>-t</code><i>NUMBER</i>, <code>&#8211;threads=</code><i>NUMBER</i></p>
<dd> Generate no more than the given number of threads. Default number of threads is 100. To disable threading specify a non-positive number.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit.</p>
<dt><code>&#8211;list-plugins</code></p>
<dd> Print available check plugins and exit.</dl>
<h3>Output options</h3>
<dl>
<dt><code>-D</code><i>STRING</i>, <code>&#8211;debug=</code><i>STRING</i></p>
<dd> Print debugging output for the given logger. Available loggers are <code>cmdline</code>, <code>checking</code>, <code>cache</code>, <code>gui</code>, <code>dns</code> and <code>all</code>. Specifying <code>all</code> is an alias for specifying all available loggers. The option can be given multiple times to debug with more than one logger. For accurate results, threading will be disabled during debug runs.</p>
<dt><code>-F</code><i>TYPE</i>[<code>/</code><i>ENCODING</i>][<code>/</code><i>FILENAME</i>], <code>&#8211;file-output=</code><i>TYPE</i>[<code>/</code><i>ENCODING</i>][<code>/</code><i>FILENAME</i>]</p>
<dd> Output to a file <code>linkchecker-out.</code><i>TYPE</i>, <code>$HOME/.linkchecker/blacklist</code> for <code>blacklist</code> output, or <i>FILENAME</i> if specified. The <i>ENCODING</i> specifies the output encoding, the default is that of your locale. Valid encodings are listed at <code><a rel="nofollow" href="http://docs.python.org/library/:codecs.html#standard-encodings">http://docs.python.org/library/:codecs.html#standard-encodings</a></code>.<br />
 The <i>FILENAME</i> and <i>ENCODING</i> parts of the <code>none</code> output type will be ignored, else if the file already exists, it will be overwritten. You can specify this option more than once. Valid file output types are <code>text</code>, <code>html</code>, <code>sql</code>, <code>csv</code>, <code>gml</code>, <code>dot</code>, <code>xml</code>, <code>sitemap</code>, <code>none</code> or <code>blacklist</code>. Default is no file output. The various output types are documented below. Note that you can suppress all console output with the option <code>-o none</code>.</p>
<dt><code>&#8211;no-status</code></p>
<dd> Do not print check status messages.</p>
<dt><code>&#8211;no-warnings</code></p>
<dd> Don&#8217;t log warnings. Default is to log warnings.</p>
<dt><code>-o</code><i>TYPE</i>[<code>/</code><i>ENCODING</i>], <code>&#8211;output=</code><i>TYPE</i>[<code>/</code><i>ENCODING</i>]</p>
<dd> Specify output type as <code>text</code>, <code>html</code>, <code>sql</code>, <code>csv</code>, <code>gml</code>, <code>dot</code>, <code>xml</code>, <code>sitemap</code>, <code>none</code> or <code>blacklist</code>. Default type is <code>text</code>. The various output types are documented below.<br />
 The <i>ENCODING</i> specifies the output encoding, the default is that of your locale. Valid encodings are listed at <code><a rel="nofollow" href="http://docs.python.org/library/:codecs.html#standard-encodings">http://docs.python.org/library/:codecs.html#standard-encodings</a></code>.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Quiet operation, an alias for <code>-o none</code>. This is only useful with <code>-F</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Log all checked URLs. Default is to log only errors and warnings.</p>
<dt><code>-W</code><i>REGEX</i>, <code>&#8211;warning-regex=</code><i>REGEX</i></p>
<dd> Define a regular expression which prints a warning if it matches any content of the checked link. This applies only to valid pages, so we can get their content.<br />
 Use this to check for pages that contain some form of error, for example &quot;This page has moved&quot; or &quot;Oracle Application error&quot;.<br />
 Note that multiple values can be combined in the regular expression, for example &quot;(This page has moved|Oracle Application error)&quot;.<br />
 See section <code>REGULAR EXPRESSIONS</code> for more info.</dl>
<h3>Checking options</h3>
<dl>
<dt><code>&#8211;cookiefile=</code><i>FILENAME</i></p>
<dd> Read a file with initial cookie data. The cookie data format is explained below.</p>
<dt><code>&#8211;check-extern</p>
<dd> Check external URLs.</p>
<dt>&#8211;ignore-url=</code><i>REGEX</i></p>
<dd> URLs matching the given regular expression will be ignored and not checked.<br />
 This option can be given multiple times.<br />
 See section <code>REGULAR EXPRESSIONS</code> for more info.</p>
<dt><code>-N</code><i>STRING</i>, <code>&#8211;nntp-server=</code><i>STRING</i></p>
<dd> Specify an NNTP server for <code>news:</code> links. Default is the environment variable <code>NNTP_SERVER</code>. If no host is given, only the syntax of the link is checked.</p>
<dt><code>&#8211;no-follow-url=</code><i>REGEX</i></p>
<dd> Check but do not recurse into URLs matching the given regular expression.<br />
 This option can be given multiple times.<br />
 See section <code>REGULAR EXPRESSIONS</code> for more info.</p>
<dt><code>-p</code>, <code>&#8211;password</code></p>
<dd> Read a password from console and use it for HTTP and FTP authorization. For FTP the default password is <code>anonymous@</code>. For HTTP there is no default password. See also <code>-u</code>.</p>
<dt><code>-r</code><i>NUMBER</i>, <code>&#8211;recursion-level=</code><i>NUMBER</i></p>
<dd> Check recursively all links up to given depth. A negative depth will enable infinite recursion. Default depth is infinite.</p>
<dt><code>&#8211;timeout=</code><i>NUMBER</i></p>
<dd> Set the timeout for connection attempts in seconds. The default timeout is 60 seconds.</p>
<dt><code>-u</code><i>STRING</i>, <code>&#8211;user=</code><i>STRING</i></p>
<dd> Try the given username for HTTP and FTP authorization. For FTP the default username is <code>anonymous</code>. For HTTP there is no default username. See also <code>-p</code>.</p>
<dt><code>&#8211;user-agent=</code><i>STRING</i></p>
<dd> Specify the User-Agent string to send to the HTTP server, for example &quot;Mozilla/4.0&quot;. The default is &quot;LinkChecker/X.Y&quot; where X.Y is the current version of LinkChecker. </p>
</dl>
<h2>CONFIGURATION FILES</h2>
<p> Configuration files can specify all options above. They can also specify some options that cannot be set on the command line. See <code><a href="/docs/linux/man/5-linkcheckerrc/">linkcheckerrc</a></code>(5) for more info. </p>
<h2>OUTPUT TYPES</h2>
<p> Note that by default only errors and warnings are logged. You should use the <code>&#8211;verbose</code> option to get the complete URL list, especially when outputting a sitemap graph format. </p>
<dl>
<dt><code>text</code></p>
<dd> Standard text logger, logging URLs in keyword: argument fashion.</p>
<dt><code>html</code></p>
<dd> Log URLs in keyword: argument fashion, formatted as HTML. Additionally has links to the referenced pages. Invalid URLs have HTML and CSS syntax check links appended.</p>
<dt><code>csv</code></p>
<dd> Log check result in CSV format with one URL per line.</p>
<dt><code>gml</code></p>
<dd> Log parent-child relations between linked URLs as a GML sitemap graph.</p>
<dt><code>dot</code></p>
<dd> Log parent-child relations between linked URLs as a DOT sitemap graph.</p>
<dt><code>gxml</code></p>
<dd> Log check result as a GraphXML sitemap graph.</p>
<dt><code>xml</code></p>
<dd> Log check result as machine-readable XML.</p>
<dt><code>sitemap</code></p>
<dd> Log check result as an XML sitemap whose protocol is documented at <code><a rel="nofollow" href="http://www.sitemaps.org/protocol.html">http://www.sitemaps.org/protocol.html</a></code>.</p>
<dt><code>sql</code></p>
<dd> Log check result as SQL script with INSERT commands. An example script to create the initial SQL table is included as create.sql.</p>
<dt><code>blacklist</code></p>
<dd> Suitable for cron jobs. Logs the check result into a file <code>~/.linkchecker/blacklist</code> which only contains entries with invalid URLs and the number of times they have failed.</p>
<dt><code>none</code></p>
<dd> Logs nothing. Suitable for debugging or checking the exit code.</dl>
<h2>REGULAR EXPRESSIONS</h2>
<p> LinkChecker accepts Python regular expressions. See <code><a rel="nofollow" href="http://docs.python.org/:howto/regex.html">http://docs.python.org/:howto/regex.html</a></code> for an introduction. </p>
<p> An addition is that a leading exclamation mark negates the regular expression.</p>
<h2>COOKIE FILES</h2>
<p> A cookie file contains standard HTTP header (RFC 2616) data with the following possible names:</p>
<dl>
<dt><code>Host</code> (required)</p>
<dd> Sets the domain the cookies are valid for.</p>
<dt><code>Path</code> (optional)</p>
<dd> Gives the path the cookies are value for; default path is <code>/</code>.</p>
<dt><code>Set-cookie</code> (required)</p>
<dd> Set cookie name/value. Can be given more than once.</dl>
<p> Multiple entries are separated by a blank line. The example below will send two cookies to all URLs starting with <code><a rel="nofollow" href="http://example.com/hello/">http://example.com/hello/</a></code> and one to all URLs starting with <code><a rel="nofollow" href="https://example.org/">https://example.org/</a></code>: </p>
<p>&nbsp;Host: example.com<br />
&nbsp;Path:&nbsp;/hello<br />
&nbsp;Set-cookie: ID=&quot;smee&quot;<br />
&nbsp;Set-cookie: spam=&quot;egg&quot; </p>
<p>&nbsp;Host: example.org<br />
&nbsp;Set-cookie: baggage=&quot;elitist&quot;;&nbsp;comment=&quot;hologram&quot; </p>
<h2>PROXY SUPPORT</h2>
<p> To use a proxy on Unix or Windows set the $http_proxy, $https_proxy or $ftp_proxy environment variables to the proxy URL. The URL should be of the form <code>http://</code>[<i>user</i><code>:</code><i>pass</i><code>@</code>]<i>host</i>[<code>:</code><i>port</i>]. LinkChecker also detects manual proxy settings of Internet Explorer under Windows systems, and gconf or KDE on Linux systems. On a Mac use the Internet Config to select a proxy. You can also set a comma-separated domain list in the $no_proxy environment variables to ignore any proxy settings for these domains. Setting a HTTP proxy on Unix for example looks like this: </p>
<p>&nbsp;<wbr>&nbsp;export http_proxy=&quot;<a rel="nofollow" href="http://proxy.example.com:8080">http://proxy.example.com:8080</a>&quot; </p>
<p> Proxy authentication is also supported: </p>
<p>&nbsp;<wbr>&nbsp;export http_proxy=&quot;<a rel="nofollow" href="http://user1:mypass@proxy.example.org:8081">http://user1:mypass@proxy.example.org:8081</a>&quot; </p>
<p> Setting a proxy on the Windows command prompt: </p>
<p>&nbsp;<wbr>&nbsp;set http_proxy=<a rel="nofollow" href="http://proxy.example.com:8080">http://proxy.example.com:8080</a> </p>
<h2>PERFORMED CHECKS</h2>
<p> All URLs have to pass a preliminary syntax test. Minor quoting mistakes will issue a warning, all other invalid syntax issues are errors. After the syntax check passes, the URL is queued for connection checking. All connection check types are described below.</p>
<dl>
<dt>HTTP links (<code>http:</code>, <code>https:</code>)</p>
<dd> After connecting to the given HTTP server the given path or query is requested. All redirections are followed, and if user/password is given it will be used as authorization when necessary. All final HTTP status codes other than 2xx are errors. HTML page contents are checked for recursion.</p>
<dt>Local files (<code>file:</code>)</p>
<dd> A regular, readable file that can be opened is valid. A readable directory is also valid. All other files, for example device files, unreadable or non-existing files are errors. HTML or other parseable file contents are checked for recursion.</p>
<dt>Mail links (<code>mailto:</code>)</p>
<dd> A mailto: link eventually resolves to a list of email addresses. If one address fails, the whole list will fail. For each mail address we check the following things:<br />
&nbsp;<wbr>&nbsp;1)&nbsp;Check the adress syntax, both of the part before and after<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;@&nbsp;sign.<br />
&nbsp;<wbr>&nbsp;2)&nbsp;Look up the MX DNS records. If we found no MX record,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print an error.<br />
&nbsp;<wbr>&nbsp;3)&nbsp;Check if one of the mail hosts accept an SMTP connection.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Check hosts with higher priority first.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;If no host accepts SMTP, we print a warning.<br />
&nbsp;<wbr>&nbsp;4)&nbsp;Try to verify the address with the VRFY command. If we got<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;an answer, print the verified address as an info.</p>
<dt>FTP links (<code>ftp:</code>)</p>
<dd>
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;For FTP links we do:<br />
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;1)&nbsp;connect to the specified host<br />
&nbsp;<wbr>&nbsp;2)&nbsp;try to login with the given user and password. The default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;user is&nbsp;&#8220;anonymous&#8220;, the default password is&nbsp;&#8220;anonymous@&#8220;.<br />
&nbsp;<wbr>&nbsp;3)&nbsp;try to change to the given directory<br />
&nbsp;<wbr>&nbsp;4)&nbsp;list the file with the NLST command </p>
<dt>Telnet links (&#8220;telnet:&#8220;)</p>
<dd>
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;We try to connect and if user/password are given, login to the<br />
&nbsp;<wbr>&nbsp;given telnet server. </p>
<dt>NNTP links (&#8220;news:&#8220;, &#8220;snews:&#8220;, &#8220;nntp&#8220;)</p>
<dd>
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;We try to connect to the given NNTP server. If a news group or<br />
&nbsp;<wbr>&nbsp;article is specified, try to request it from the server. </p>
<dt>Unsupported links (&#8220;javascript:&#8220;, etc.)</p>
<dd>
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;An unsupported link will only print a warning. No further checking<br />
&nbsp;<wbr>&nbsp;will be made.<br />
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;The complete list of recognized, but unsupported links can be found<br />
&nbsp;<wbr>&nbsp;in the&nbsp;<code>linkcheck/checker/unknownurl.py</code>&nbsp;source file.<br />
&nbsp;<wbr>&nbsp;The most prominent of them should be JavaScript links. </p>
</dl>
<h2>PLUGINS</h2>
<p> There are two plugin types: connection and content plugins. Connection plugins are run after a successful connection to the URL host. Content plugins are run if the URL type has content (mailto: URLs have no content for example) and if the check is not forbidden (ie. by HTTP robots.txt). See <code>linkchecker &#8211;list-plugins</code> for a list of plugins and their documentation. All plugins are enabled via the <code><a href="/docs/linux/man/5-linkcheckerrc/">linkcheckerrc</a></code>(5) configuration file. </p>
<h2>RECURSION</h2>
<p> Before descending recursively into a URL, it has to fulfill several conditions. They are checked in this order: </p>
<p> 1. A URL must be valid. </p>
<p> 2. A URL must be parseable. This currently includes HTML files,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Opera bookmarks files, and directories. If a file type cannot<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;be determined&nbsp;(for example it does not have a common HTML file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;extension, and the content does not look like HTML), it is assumed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;to be non-parseable. </p>
<p> 3. The URL content must be retrievable. This is usually the case<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;except for example mailto: or unknown URL types. </p>
<p> 4. The maximum recursion level must not be exceeded. It is configured<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;with the&nbsp;<code>&#8211;recursion-level</code>&nbsp;option and is unlimited per default. </p>
<p> 5. It must not match the ignored URL list. This is controlled with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;<code>&#8211;ignore-url</code>&nbsp;option. </p>
<p> 6. The Robots Exclusion Protocol must allow links in the URL to be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;followed recursively. This is checked by searching for a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;nofollow&quot;&nbsp;directive in the HTML header data. </p>
<p> Note that the directory recursion reads all files in that directory, not just a subset like <code>index.htm*</code>. </p>
<h2>NOTES</h2>
<p> URLs on the commandline starting with <code>ftp.</code> are treated like <code><a href="ftp://ftp.">ftp://ftp.</a></code>, URLs starting with <code>www.</code> are treated like <code><a rel="nofollow" href="http://www.">http://www.</a></code>. You can also give local files as arguments. </p>
<p> If you have your system configured to automatically establish a connection to the internet (e.g. with diald), it will connect when checking links not pointing to your local host. Use the <code>&#8211;ignore-url</code> option to prevent this. </p>
<p> Javascript links are not supported. </p>
<p> If your platform does not support threading, LinkChecker disables it automatically. </p>
<p> You can supply multiple user/password pairs in a configuration file. </p>
<p> When checking <code>news:</code> links the given NNTP host doesn&#8217;t need to be the same as the host of the user browsing your pages.</p>
<h2>ENVIRONMENT</h2>
<p> <code>NNTP_SERVER</code> &#8211; specifies default NNTP server<br />
 <code>http_proxy</code> &#8211; specifies default HTTP proxy server<br />
 <code>ftp_proxy</code> &#8211; specifies default FTP proxy server<br />
 <code>no_proxy</code> &#8211; comma-separated list of domains to not contact over a proxy server<br />
 <code>LC_MESSAGES</code>, <code>LANG</code>, <code>LANGUAGE</code> &#8211; specify output language</p>
<h2>RETURN VALUE</h2>
<p> The return value is 2 when</p>
<dl>
<dt>&bull;</p>
<dd> a program error occurred.</dl>
<p> The return value is 1 when</p>
<dl>
<dt>&bull;</p>
<dd> invalid links were found or</p>
<dt>&bull;</p>
<dd> link warnings were found and warnings are enabled</dl>
<p> Else the return value is zero.</p>
<h2>LIMITATIONS</h2>
<p> LinkChecker consumes memory for each queued URL to check. With thousands of queued URLs the amount of consumed memory can become quite large. This might slow down the program or even the whole system.</p>
<h2>FILES</h2>
<p> <code>~/.linkchecker/linkcheckerrc</code> &#8211; default configuration file<br />
 <code>~/.linkchecker/blacklist</code> &#8211; default blacklist logger output filename<br />
 <code>linkchecker-out.</code><i>TYPE</i> &#8211; default logger file output name<br />
 <code><a rel="nofollow" href="http://docs.python.org/library/codecs.html#standard-encodings">http://docs.python.org/library/codecs.html#standard-encodings</a></code> &#8211; valid output encodings<br />
 <code><a rel="nofollow" href="http://docs.python.org/howto/regex.html">http://docs.python.org/howto/regex.html</a></code> &#8211; regular expression documentation </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-linkcheckerrc/">linkcheckerrc</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Bastian Kleineidam &lt;bastian.kleineidam [at] web.de&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2014 Bastian Kleineidam </p>
<h2>Index</h2>
