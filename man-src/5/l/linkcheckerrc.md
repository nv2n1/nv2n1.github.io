---
title: "linkcheckerrc(5)"
name: "linkcheckerrc"
section: "5"
letter: "l"
url: "/docs/linux/man/5-linkcheckerrc/"
description: "linkcheckerrc – configuration file for LinkChecker"
---

<p>linkcheckerrc &#8211; configuration file for LinkChecker</p>
<h2>Description</h2>
<p><code>linkcheckerrc</code> is the configuration file for LinkChecker. The file is written in an INI-style format.<br/>
 The default file location is <code>~/.linkchecker/linkcheckerrc</code> on Unix, <code>%HOMEPATH%\.linkchecker\linkcheckerrc</code> on Windows systems.</p>
<h2>Settings</h2>
<h3><code>[checking]</code></h3>
<dl>
<dt><code>cookiefile=</code><i>filename</i></dt>
<dd>Read a file with initial cookie data. The cookie data format is explained in <a href="/docs/linux/man/1-linkchecker/">linkchecker</a>(1).<br/>
 Command line option: <code>&#8211;cookiefile</code></dd>
<dt><code>localwebroot=</code><i>STRING</i></dt>
<dd>When checking absolute URLs inside local files, the given root directory is used as base URL.<br/>
 Note that the given directory must have URL syntax, so it must use a slash to join directories instead of a backslash. And the given directory must end with a slash.<br/>
 Command line option: none</dd>
<dt><code>nntpserver=</code><i>STRING</i></dt>
<dd>Specify an NNTP server for <code>news:</code> links. Default is the environment variable <code>NNTP_SERVER</code>. If no host is given, only the syntax of the link is checked.<br/>
 Command line option: <code>&#8211;nntp-server</code></dd>
<dt><code>recursionlevel=</code><i>NUMBER</i></dt>
<dd>Check recursively all links up to given depth. A negative depth will enable infinite recursion. Default depth is infinite.<br/>
 Command line option: <code>&#8211;recursion-level</code></dd>
<dt><code>threads=</code><i>NUMBER</i></dt>
<dd>Generate no more than the given number of threads. Default number of threads is 100. To disable threading specify a non-positive number.<br/>
 Command line option: <code>&#8211;threads</code></dd>
<dt><code>timeout=</code><i>NUMBER</i></dt>
<dd>Set the timeout for connection attempts in seconds. The default timeout is 60 seconds.<br/>
 Command line option: <code>&#8211;timeout</code></dd>
<dt><code>aborttimeout=</code><i>NUMBER</i></dt>
<dd>Time to wait for checks to finish after the user aborts the first time (with Ctrl-C or the abort button). The default abort timeout is 300 seconds.<br/>
 Command line option: <code>&#8211;timeout</code></dd>
<dt><code>useragent=</code><i>STRING</i></dt>
<dd>Specify the User-Agent string to send to the HTTP server, for example &quot;Mozilla/4.0&quot;. The default is &quot;LinkChecker/X.Y&quot; where X.Y is the current version of LinkChecker.<br/>
 Command line option: <code>&#8211;user-agent</code></dd>
<dt><code>sslverify=</code>[<code>0</code>|<code>1</code>|<i>filename</i>]</dt>
<dd>If set to zero disables SSL certificate checking. If set to one (the default) enables SSL certificate checking with the provided CA certificate file. If a filename is specified, it will be used as the certificate file.<br/>
 Command line option: none</dd>
<dt><code>maxrunseconds=</code><i>NUMBER</i></dt>
<dd>Stop checking new URLs after the given number of seconds. Same as if the user stops (by hitting Ctrl-C or clicking the abort buttin in the GUI) after the given number of seconds.<br/>
 The default is not to stop until all URLs are checked.<br/>
 Command line option: none</dd>
<dt><code>maxnumurls=</code><i>NUMBER</i></dt>
<dd>Maximum number of URLs to check. New URLs will not be queued after the given number of URLs is checked.<br/>
 The default is to queue and check all URLs.<br/>
 Command line option: none</dd>
<dt><code>maxrequestspersecond=</code><i>NUMBER</i></dt>
<dd>Limit the maximum number of requests per second to one host.</dd>
<dt><code>allowedschemes=</code><i>NAME</i>[<code>,</code><i>NAME</i>&#8230;]</dt>
<dd>Allowed URL schemes as comma-separated list.</dd></dl>
<h3><code>[filtering]</code></h3>
<dl>
<dt><code>ignore=</code><i>REGEX</i> (MULTILINE)</dt>
<dd>Only check syntax of URLs matching the given regular expressions.<br/>
 Command line option: <code>&#8211;ignore-url</code></dd>
<dt><code>ignorewarnings=</code><i>NAME</i>[<code>,</code><i>NAME</i>&#8230;]</dt>
<dd>Ignore the comma-separated list of warnings. See <code>WARNIGS</code> for the list of supported warnings.<br/>
 Command line option: none</dd>
<dt><code>internlinks=</code><i>REGEX</i></dt>
<dd>Regular expression to add more URLs recognized as internal links. Default is that URLs given on the command line are internal.<br/>
 Command line option: none</dd>
<dt><code>nofollow=</code><i>REGEX</i> (MULTILINE)</dt>
<dd>Check but do not recurse into URLs matching the given regular expressions.<br/>
 Command line option: <code>&#8211;no-follow-url</code></dd>
<dt><code>checkextern=</code>[<code>0</code>|<code>1</code>]</dt>
<dd>Check external links. Default is to check internal links only.<br/>
 Command line option: <code>&#8211;checkextern</code></dd></dl>
<h3><code>[authentication]</code></h3>
<dl>
<dt><code>entry=</code><i>REGEX</i> <i>USER</i> [<i>PASS</i>] (MULTILINE)</dt>
<dd>Provide different user/password pairs for different link types. Entries are a triple (URL regex, username, password) or a tuple (URL regex, username), where the entries are separated by whitespace.<br/>
 The password is optional and if missing it has to be entered at the commandline.<br/>
 If the regular expression matches the checked URL, the given user/password pair is used for authentication. The commandline options <code>-u</code> and <code>-p</code> match every link and therefore override the entries given here. The first match wins. At the moment, authentication is used/needed for http[s] and ftp links.<br/>
 Command line option: <code>-u</code>, <code>-p</code></dd>
<dt><code>loginurl=</code><i>URL</i></dt>
<dd>A login URL to be visited before checking. Also needs authentication data set for it.</dd>
<dt><code>loginuserfield=</code><i>STRING</i></dt>
<dd>The name of the user CGI field. Default name is <code>login</code>.</dd>
<dt><code>loginpasswordfield=</code><i>STRING</i></dt>
<dd>The name of the password CGI field. Default name is <code>password</code>.</dd>
<dt><code>loginextrafields=</code><i>NAME</i><code>:</code><i>VALUE</i> (MULTILINE)</dt>
<dd>Optionally any additional CGI name/value pairs. Note that the default values are submitted automatically.</dd></dl>
<h3><code>[output]</code></h3>
<dl>
<dt><code>debug=</code><i>STRING</i>[<code>,</code><i>STRING</i>&#8230;]</dt>
<dd>Print debugging output for the given loggers. Available loggers are <code>cmdline</code>, <code>checking</code>, <code>cache</code>, <code>gui</code>, <code>dns</code>, <code>thread</code> and <code>all</code>. Specifying <code>all</code> is an alias for specifying all available loggers.<br/>
 Command line option: <code>&#8211;debug</code></dd>
<dt><code>fileoutput=</code><i>TYPE</i>[<code>,</code><i>TYPE</i>&#8230;]</dt>
<dd>Output to a files <code>linkchecker-out.</code><i>TYPE</i>, <code>$HOME/.linkchecker/blacklist</code> for <code>blacklist</code> output.<br/>
 Valid file output types are <code>text</code>, <code>html</code>, <code>sql</code>, <code>csv</code>, <code>gml</code>, <code>dot</code>, <code>xml</code>, <code>none</code> or <code>blacklist</code> Default is no file output. The various output types are documented below. Note that you can suppress all console output with <code>output=none</code>.<br/>
 Command line option: <code>&#8211;file-output</code></dd>
<dt><code>log=</code><i>TYPE</i>[<code>/</code><i>ENCODING</i>]</dt>
<dd>Specify output type as <code>text</code>, <code>html</code>, <code>sql</code>, <code>csv</code>, <code>gml</code>, <code>dot</code>, <code>xml</code>, <code>none</code> or <code>blacklist</code>. Default type is <code>text</code>. The various output types are documented below.<br/>
 The <i>ENCODING</i> specifies the output encoding, the default is that of your locale. Valid encodings are listed at <code><a rel="nofollow" href="http://docs.python.org/library/codecs.html#standard-encodings">http://docs.python.org/library/codecs.html#standard-encodings</a></code>.<br/>
 Command line option: <code>&#8211;output</code></dd>
<dt><code>quiet=</code>[<code>0</code>|<code>1</code>]</dt>
<dd>If set, operate quiet. An alias for <code>log=none</code>. This is only useful with <code>fileoutput</code>.<br/>
 Command line option: <code>&#8211;verbose</code></dd>
<dt><code>status=</code>[<code>0</code>|<code>1</code>]</dt>
<dd>Control printing check status messages. Default is 1.<br/>
 Command line option: <code>&#8211;no-status</code></dd>
<dt><code>verbose=</code>[<code>0</code>|<code>1</code>]</dt>
<dd>If set log all checked URLs once. Default is to log only errors and warnings.<br/>
 Command line option: <code>&#8211;verbose</code></dd>
<dt><code>warnings=</code>[<code>0</code>|<code>1</code>]</dt>
<dd>If set log warnings. Default is to log warnings.<br/>
 Command line option: <code>&#8211;no-warnings</code></dd></dl>
<h3><code>[text]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>Specify output filename for text logging. Default filename is <code>linkchecker-out.txt</code>.<br/>
 Command line option: <code>&#8211;file-output=</code></dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>Comma-separated list of parts that have to be logged. See <code>LOGGER PARTS</code> below.<br/>
 Command line option: none</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>Valid encodings are listed in <code><a rel="nofollow" href="http://docs.python.org/library/codecs.html#standard-encodings">http://docs.python.org/library/codecs.html#standard-encodings</a></code>.<br/>
 Default encoding is <code>iso-8859-15</code>.</dd>
<dt><i>color*</i></dt>
<dd>Color settings for the various log parts, syntax is <i>color</i> or <i>type</i><code>;</code><i>color</i>. The <i>type</i> can be <code>bold</code>, <code>light</code>, <code>blink</code>, <code>invert</code>. The <i>color</i> can be <code>default</code>, <code>black</code>, <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>purple</code>, <code>cyan</code>, <code>white</code>, <code>Black</code>, <code>Red</code>, <code>Green</code>, <code>Yellow</code>, <code>Blue</code>, <code>Purple</code>, <code>Cyan</code> or <code>White</code>.<br/>
 Command line option: none</dd>
<dt><code>colorparent=</code><i>STRING</i></dt>
<dd>Set parent color. Default is <code>white</code>.</dd>
<dt><code>colorurl=</code><i>STRING</i></dt>
<dd>Set URL color. Default is <code>default</code>.</dd>
<dt><code>colorname=</code><i>STRING</i></dt>
<dd>Set name color. Default is <code>default</code>.</dd>
<dt><code>colorreal=</code><i>STRING</i></dt>
<dd>Set real URL color. Default is <code>cyan</code>.</dd>
<dt><code>colorbase=</code><i>STRING</i></dt>
<dd>Set base URL color. Default is <code>purple</code>.</dd>
<dt><code>colorvalid=</code><i>STRING</i></dt>
<dd>Set valid color. Default is <code>bold;green</code>.</dd>
<dt><code>colorinvalid=</code><i>STRING</i></dt>
<dd>Set invalid color. Default is <code>bold;red</code>.</dd>
<dt><code>colorinfo=</code><i>STRING</i></dt>
<dd>Set info color. Default is <code>default</code>.</dd>
<dt><code>colorwarning=</code><i>STRING</i></dt>
<dd>Set warning color. Default is <code>bold;yellow</code>.</dd>
<dt><code>colordltime=</code><i>STRING</i></dt>
<dd>Set download time color. Default is <code>default</code>.</dd>
<dt><code>colorreset=</code><i>STRING</i></dt>
<dd>Set reset color. Default is <code>deault</code>.</dd></dl>
<h3><code>[gml]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd></dl>
<h3><code>[dot]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd></dl>
<h3><code>[csv]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>separator=</code><i>CHAR</i></dt>
<dd>Set CSV separator. Default is a comma (<code>,</code>).</dd>
<dt><code>quotechar=</code><i>CHAR</i></dt>
<dd>Set CSV quote character. Default is a double quote (<code>&quot;</code>).</dd></dl>
<h3><code>[sql]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>dbname=</code><i>STRING</i></dt>
<dd>Set database name to store into. Default is <code>linksdb</code>.</dd>
<dt><code>separator=</code><i>CHAR</i></dt>
<dd>Set SQL command separator character. Default is a semicolor (<code>;</code>).</dd></dl>
<h3><code>[html]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>colorbackground=</code><i>COLOR</i></dt>
<dd>Set HTML background color. Default is <code>#fff7e5</code>.</dd>
<dt><code>colorurl=</code></dt>
<dd>Set HTML URL color. Default is <code>#dcd5cf</code>.</dd>
<dt><code>colorborder=</code></dt>
<dd>Set HTML border color. Default is <code>#000000</code>.</dd>
<dt><code>colorlink=</code></dt>
<dd>Set HTML link color. Default is <code>#191c83</code>.</dd>
<dt><code>colorwarning=</code></dt>
<dd>Set HTML warning color. Default is <code>#e0954e</code>.</dd>
<dt><code>colorerror=</code></dt>
<dd>Set HTML error color. Default is <code>#db4930</code>.</dd>
<dt><code>colorok=</code></dt>
<dd>Set HTML valid color. Default is <code>#3ba557</code>.</dd></dl>
<h3><code>[blacklist]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd></dl>
<h3><code>[xml]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd></dl>
<h3><code>[gxml]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd></dl>
<h3><code>[sitemap]</code></h3>
<dl>
<dt><code>filename=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>parts=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>encoding=</code><i>STRING</i></dt>
<dd>See [text] section above.</dd>
<dt><code>priority=</code><i>FLOAT</i></dt>
<dd>A number between 0.0 and 1.0 determining the priority. The default priority for the first URL is 1.0, for all child URLs 0.5.</dd>
<dt><code>frequency=</code>[<code>always</code>|<code>hourly</code>|<code>daily</code>|<code>weekly</code>|<code>monthly</code>|<code>yearly</code>|<code>never</code>]</dt>
<dd>The frequence pages are changing with.</dd></dl>
<h2>Logger Parts</h2>
<p>&nbsp;<code>all</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(for all parts)<br/>
&nbsp;<code>id</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(a unique ID for each logentry)<br/>
&nbsp;<code>realurl</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(the full url link)<br/>
&nbsp;<code>result</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(valid or invalid, with messages)<br/>
&nbsp;<code>extern</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(1 or 0, only in some logger types reported)<br/>
&nbsp;<code>base</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(base href=&#8230;)<br/>
&nbsp;<code>name</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(&lt;a href=&#8230;&gt;name&lt;/a&gt;&nbsp;and&nbsp;&lt;img alt=&quot;name&quot;&gt;)<br/>
&nbsp;<code>parenturl</code>&nbsp;(if any)<br/>
&nbsp;<code>info</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(some additional info, e.g. FTP welcome messages)<br/>
&nbsp;<code>warning</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(warnings)<br/>
&nbsp;<code>dltime</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(download time)<br/>
&nbsp;<code>checktime</code>&nbsp;(check time)<br/>
&nbsp;<code>url</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(the original url name, can be relative)<br/>
&nbsp;<code>intro</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(the blurb at the beginning,&nbsp;&quot;starting at &#8230;&quot;)<br/>
&nbsp;<code>outro</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(the blurb at the end,&nbsp;&quot;found x errors &#8230;&quot;)</p>
<h2>Multiline</h2>
<p>Some option values can span multiple lines. Each line has to be indented for that to work. Lines starting with a hash (<code>#</code>) will be ignored, though they must still be indented. </p>
<p>&nbsp;ignore=<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;lconline<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;bookmark<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;a comment<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;^mailto:</p>
<h2>Example</h2>
<pre><code>[output]
log=html
[checking]
threads=5
[filtering]
ignorewarnings=http-moved-permanent
</code></pre>
<h2>Plugins</h2>
<p>All plugins have a separate section. If the section appears in the configuration file the plugin is enabled. Some plugins read extra options in their section.</p>
<h3><code>[AnchorCheck]</code></h3>
<p>Checks validity of HTML anchors.</p>
<h3><code>[LocationInfo]</code></h3>
<p>Adds the country and if possible city name of the URL host as info. Needs GeoIP or pygeoip and a local country or city lookup DB installed.</p>
<h3><code>[RegexCheck]</code></h3>
<p>Define a regular expression which prints a warning if it matches any content of the checked link. This applies only to valid pages, so we can get their content. </p>
<p> Use this to check for pages that contain some form of error message, for example &#8216;This page has moved&#8217; or &#8216;Oracle Application error&#8217;. </p>
<p> Note that multiple values can be combined in the regular expression, for example &quot;(This page has moved|Oracle Application error)&quot;.</p>
<h3><code>[SslCertificateCheck]</code></h3>
<p>Check SSL certificate expiration date. Only internal https: links will be checked. A domain will only be checked once to avoid duplicate warnings.</p>
<dl>
<dt><code>sslcertwarndays=</code><i>NUMBER</i></dt>
<dd>Configures the expiration warning time in days. </dd>
</dl>
<h3><code>[HtmlSyntaxCheck]</code></h3>
<p>Check the syntax of HTML pages with the online W3C HTML validator. See <a rel="nofollow" href="http://validator.w3.org/docs/api.html.">http://validator.w3.org/docs/api.html.</a></p>
<h3><code>[HttpHeaderInfo]</code></h3>
<p>Print HTTP headers in URL info.</p>
<dl>
<dt><code>prefixes=</code><i>prefix1</i>[,<i>prefix2</i>]&#8230;</dt>
<dd>List of comma separated header prefixes. For example to display all HTTP headers that start with &quot;X-&quot;. </dd>
</dl>
<h3><code>[CssSyntaxCheck]</code></h3>
<p>Check the syntax of HTML pages with the online W3C CSS validator. See <a rel="nofollow" href="http://jigsaw.w3.org/css-validator/manual.html#expert.">http://jigsaw.w3.org/css-validator/manual.html#expert.</a></p>
<h3><code>[VirusCheck]</code></h3>
<p>Checks the page content for virus infections with clamav. A local clamav daemon must be installed.</p>
<dl>
<dt><code>clamavconf=</code><i>filename</i></dt>
<dd>Filename of <code>clamd.conf</code> config file.</dd></dl>
<h3><code>[PdfParser]</code></h3>
<p>Parse PDF files for URLs to check. Needs the <code>pdfminer</code> Python package installed.</p>
<h3><code>[WordParser]</code></h3>
<p>Parse Word files for URLs to check. Needs the pywin32 Python extension installed.</p>
<h2>Warnings</h2>
<p>The following warnings are recognized in the &#8216;ignorewarnings&#8217; config file entry: </p>
<dl>
<dt><code>file-missing-slash</code></dt>
<dd>The file: URL is missing a trailing slash.</dd>
<dt><code>file-system-path</code></dt>
<dd>The file: path is not the same as the system specific path.</dd>
<dt><code>ftp-missing-slash</code></dt>
<dd>The ftp: URL is missing a trailing slash.</dd>
<dt><code>http-cookie-store-error</code></dt>
<dd>An error occurred while storing a cookie.</dd>
<dt><code>http-empty-content</code></dt>
<dd>The URL had no content.</dd>
<dt><code>mail-no-mx-host</code></dt>
<dd>The mail MX host could not be found.</dd>
<dt><code>nntp-no-newsgroup</code></dt>
<dd>The NNTP newsgroup could not be found.</dd>
<dt><code>nntp-no-server</code></dt>
<dd>No NNTP server was found.</dd>
<dt><code>url-content-size-zero</code></dt>
<dd>The URL content size is zero.</dd>
<dt><code>url-content-too-large</code></dt>
<dd>The URL content size is too large.</dd>
<dt><code>url-effective-url</code></dt>
<dd>The effective URL is different from the original.</dd>
<dt><code>url-error-getting-content</code></dt>
<dd>Could not get the content of the URL.</dd>
<dt><code>url-obfuscated-ip</code></dt>
<dd>The IP is obfuscated.</dd>
<dt><code>url-whitespace</code></dt>
<dd>The URL contains leading or trailing whitespace. </dd>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-linkchecker/">linkchecker</a>(1)</p>
<h2>Author</h2>
<p>Bastian Kleineidam &lt;bastian.kleineidam [at] web.de&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2014 Bastian Kleineidam</p>
