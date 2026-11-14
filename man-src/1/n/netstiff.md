---
title: "netstiff(1)"
name: "netstiff"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netstiff/"
description: "netstiff – powerful and easy tool to check for Web and FTP updates"
---

<h2>NAME</h2>
<p> netstiff &#8211; powerful and easy tool to check for Web and FTP updates </p>
<h2>SYNOPSIS</h2>
<p> <code>netstiff</code> [<i>options</i>] [<i>command</i>] </p>
<h2>DESCRIPTION</h2>
<p> Netstiff (formerly known as webdiff) is a powerful and easy-to-use tool which checks for Web page and/or FTP site updates. </p>
<p> For the Web, updates are recognized using several test criteria (diff, html, size, date, md5sum, regexp). The FTP update checker is only able to diff on directory listings and files and to compare size and date of files. </p>
<p> Without a given command, netstiff will check for updates of the specified URIs and then print the changes. If no configuration file exists, the configurator is launched instead. </p>
<p> Netstiff exits after all configured URIs are checked. Occuring warnings and errors leave a message in the log file (~/.netstiff/lastlog) and on stderr. Use it with <i>cron</i> if you want to check for updates regularly. </p>
<h2>COMMANDS</h2>
<p> You can only pass one command to netstiff. It has to be the last argument in the argument list. </p>
<p> Commands may be shortened down to one character (e.g. <code>c</code> instead of <code>configure</code>). Leading dashes are ignored. </p>
<p> If you start netstiff without command, the <code>full</code> command will be used.</p>
<dl>
<dt><code>configure</code></p>
<dd> Use this command if you want to start the configurator, the interactive configuration tool of netstiff. Of course, you may also edit the configuration file in ~/.netstiff/config by hand. Using the configurator is recommended if you are a new netstiff user, because it explains the possible test methods, validates your regexps, etc. Nevertheless, the configuration file format is very easy. See section <code>CONFIGURATION FILE</code>.<br />
 The configurator will not initialize the netstiff cache for added URIs, i.e. it will not download anything. To do so, you have to run netstiff update first. This is a feature.<br />
 If the config file does not exit, the configuration tool is started automatically.</p>
<dt><code>diff</code></p>
<dd> Use this command if you want to see the differences between two versions of saved content (Web pages or meta data). See <i><a href="/docs/linux/man/1-diff/">diff</a></i>(1). </p>
<p> The version after the last <code>reset</code> (or the initial version) and the version of the last <code>update</code> will be compared.</p>
<dt><code>full</code></p>
<dd> Use this command if you simply want netstiff to check for updates and print the diff. </p>
<p> <code>full</code> is a simple replacement for the following sequence:<br />
 netstiff update &gt; /dev/null<br />
 netstiff diff<br />
 netstiff reset</p>
<dt><code>help</code></p>
<dd> Use this command to get usage information about netstiff. To be honest, this manual page in conjunction with the configurator is a better documentation.</p>
<dt><code>reset</code></p>
<dd> Use this command after you noticed all differences with the <code>diff</code> command (see above), so that <code>diff</code> will not show you the same changes again and again.</p>
<dt><code>update</code></p>
<dd> Use this command if you want netstiff to fetch the data from the specified URIs and show you only those &#8211; one per line &#8211; that have changed since your last <code>update</code>.</p>
<dt><code>version</code></p>
<dd> This command will display version number and copyright. </p>
</dl>
<h2>OPTIONS</h2>
<p> You may pass the following options.</p>
<dl>
<dt><code>&#8211;no-stderr, -S</code></p>
<dd> Use this option to suppress warning and error messages on stderr. Thus the messages can only be seen in the log file.</p>
<dt><code>&#8211;workdir DIR, -W DIR</code></p>
<dd> Use this option if you want to specify another working directory. The working directory is the directory where netstiff reads the configuration file, stores the downloaded data and writes it logs. It defaults to ~/.netstiff. See also section <code>BUGS</code>. </p>
</dl>
<h2>RESTRICTIONS</h2>
<p> There is no special case to handle status codes other than 200. In practice, netstiff will neither follow redirections nor will it notice any 4xx or 5xx error code. The resulting error pages are treated as usual Web pages. No logged message. Please check on your own. </p>
<h2>USAGE EXAMPLE</h2>
<p> You want to add a new URI netstiff should check for updates. </p>
<pre>
        netstiff conf
</pre>
<p> The configurator is not described here. I know some weaknesses in usability, but you can get along with it. </p>
<p> When you are seeing your shell prompt again, you know that netstiff should retrieve an initial version of the Web page you specified. </p>
<pre>
        netstiff update
</pre>
<p> After some weeks in the sun you want to see if something has changed. So you let netstiff check for updates. </p>
<pre>
        netstiff
</pre>
<p> It is printing an URI! Let&#8217;s see the changes! </p>
<pre>
        netstiff diff
</pre>
<p> Oh, it is so much, that it does not fit on a screen! </p>
<pre>
        netstiff d | pager
</pre>
<p> Now you are satisfied because you read all the changes. So you finally do </p>
<pre>
        netstiff reset
</pre>
<p> and netstiff forgets about the changes. </p>
<h2>CONFIGURATION FILE</h2>
<p> There is no need to manually edit the configuration file <i>WORKDIR</i>/config (usually ~/.netstiff/config), because netstiff configure should do the job. But sometimes it is easier to edit a simple file than to browse through menus, or you are writing another application that changes netstiff settings. So it is useful to describe the file format here. </p>
<h3>RULES</h3>
<dl>
<dt> *</p>
<dd> Whitespace at the begin and end of each line is ignored.</p>
<dt> *</p>
<dd> Empty lines are ignored.</p>
<dt> *</p>
<dd> A line beginning with # is regarded as comment.</p>
<dt> *</p>
<dd> A line beginning with + is regarded as option. The + is followed by the <i>option name</i>, some whitespace and the <i>option value</i>.</p>
<dt> *</p>
<dd> A line neither beginning with # nor + is regarded as URI. URIs without scheme (<a rel="nofollow" href="https://,">https://,</a> <a href="http://,">http://,</a> <a href="ftp://)">ftp://)</a> are recognized as HTTP URIs.</p>
<dt> *</p>
<dd> The configurator interprets a comment right above an URI as the title of the URI.</p>
<dt> *</p>
<dd> Options always apply to the first URI above. Options without URI line above are <i>global options</i> and affect every URI that does not override these specific options. </p>
</dl>
<h3>CONFIGURATION OPTIONS</h3>
<p> The following options are generally available:</p>
<dl>
<dt><code>test</code></p>
<dd> sets the test method (or test criteria).<br />
 See section <code>TEST METHODS</code> for a description. Defaults to diff.</p>
<dt><code>timeout</code></p>
<dd> sets the timeout (in seconds) for TCP connections.<br />
 Defaults to 20.</dl>
<p> The following options only affect HTTP URIs:</p>
<dl>
<dt><code>client</code></p>
<dd> set the user-agent string.<br />
 Some web sites check the HTTP header field <i>User-Agent</i> and display different content for different agents. By setting this field you can pretend to use Mozilla Firefox, for example. Because many log analyzer tools for webmasters display statistics about that field, you may spread the word about netstiff by setting this variable to the truth: netstiff. ;-)<br />
 <i>Example:</i> + client Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080208 Galeon/2.0.4<br />
 This option is not set by default.</p>
<dt><code>lang</code></p>
<dd> sets the accepted languages.<br />
 Internationalized web sites offer there contents in different languages and may check the HTTP header field <i>Accept-Language</i>. It contains a list of languages (and sometimes extra information like associated countries) sorted by priority. The best way to get a good value is to copy and paste it from the preferences of your web browser.<br />
 <i>Example:</i> de,en;q=0.9<br />
 This option is not set by default.</p>
<dt><code>proxy</code></p>
<dd> sets HTTP proxy host and port. Must be in the form host:port. Will fail if no port is given.</p>
<dt><code>range</code></p>
<dd> sets the range (in bytes) to get from a server.<br />
 Use this option if you are only interested in the changes within a small region of a big file on a HTTP server. Examples are 12000-12500 or 13000- (till the end).<br />
 The Range feature is not supported by all web servers or for every content. That means, that some web servers send the whole content instead of only the given range.<br />
 This option is not set by default.</p>
<dt><code>referer</code></p>
<dd> sets the referrer.<br />
 Some web sites check the HTTP header field <i>Referer</i> and refuse to display the wished contents if it is not appropriately set. When clicking on a link in an ordinary web browser, the referrer is set to the URI, where you clicked on the link. By setting this option to an URI, you can pretend clicking on a link on the web page of this URI. Please do not use this option to `advertise&#8217; your own homepage (so-called <i>referer spamming</i>).<br />
 This option is not set by default.</dl>
<p> The following options only affect the test method html:</p>
<dl>
<dt><code>htmlcmd</code></p>
<dd> sets the command that is used to produce non-HTML human-readable output. The command will be run on a temporary file.<br />
 Doing many experiments I got my best results using + htmlcmd lynx -nolist -dump. Other dumpers had features, like justified text or well-formatted tables, that turned out to be disadvantages when looking at the diffs.<br />
 This option is not set by default. If you use the html test method then, a very simple mechanism will hide HTML tags. It is possible to get good results doing that, but it is not likely and thus not recommended to leave this option unset.</dl>
<p> The following options only affect the test methods diff and html:</p>
<dl>
<dt><code>start</code>, <code>end</code></p>
<dd> <i>Motivation:</i> Many modern or CMS-generated web pages have a dynamic and a static part. For example, at the beginning of a web page there is always a randomly chosen citation the author liked. At the end there is a calendar showing the current date, a weather analysis for the next days, and some other useless stuff. The information you want to monitor for changes (the <i>static part</i>) is situated between those dynamic parts. It is very often possible to figure out <i>textual anchors</i>, that indicate the start or the end of the static part.<br />
 Using this options you can set regular expressions to that anchors. For example, if the last entry of the navigation bar is <i>Imprint</i> and thereafter comes the static part, set + start /Imprint/. I hope, you can imagine analogous examples for the end option.<br />
 Note, that the regular expressions act on the unprocessed input (e.g. HTML source code), also when using the html test method.<br />
 These options are not set by default.</dl>
<p> The following options only affect FTP URIs:</p>
<dl>
<dt><code>passive</code></p>
<dd> is a boolean option (value true or false, case-insensitive). Passive mode (PASV) will not be used on FTP connections iff set to false.<br />
 Defaults to true. </p>
</dl>
<h3>EXAMPLE</h3>
<pre>
# this is my netstiff config file
+ test      html
+ htmlcmd   lynx -nolist -dump
+ client    netstiff
+ lang      de_DE
+ timeout   6
# local usage statistics
<a rel="nofollow" href="http://localhost/stats.php">http://localhost/stats.php</a>
  + start   /Statistics/
  + end     /Generating page took/
# sbeyer's homepage
<a rel="nofollow" href="http://pkqs.net/~sbeyer/">http://pkqs.net/~sbeyer/</a>
# buggy scripts test
<a rel="nofollow" href="http://localhost/buggyscripts/test.cgi">http://localhost/buggyscripts/test.cgi</a>
  + test /Internal Server Error/
# muetze's funny videos
<a href="ftp://foo:duff23@muetze.localnet/funnyvideos/">ftp://foo:duff23@muetze.localnet/funnyvideos/</a>
  + passive false
</pre>
<h2>TEST METHODS</h2>
<p> The following test methods can be used:</p>
<dl>
<dt><code>date</code></p>
<dd> On HTTP URIs, this method downloads the HTTP header to check when the file has last been modified. To make this feature work, the server should response the <i>Last-Modified</i> header entity. This behaviour can become useless when fetching some dynamic web sites.<br />
 On FTP URIs, this method requests the last modification date of the file on the FTP site to check when the file has last been modified.</p>
<dt><code>diff</code></p>
<dd> This method downloads the HTTP content, FTP file or FTP directory listing and saves the two last versions. Later you can use netstiff diff to take a look at a diff of these versions.</p>
<dt><code>html</code></p>
<dd> This method acts like diff, but assumes to get HTML input and preprocesses it to it more human-readable.<br />
 See also the description of the htmlcmd option in section <code>CONFIGURATION FILE / CONFIGURATION OPTIONS</code>.<br />
 This method is not available on FTP URIs.</p>
<dt><code>md5sum</code></p>
<dd> This method downloads the HTTP header to check if the MD5 sum has changed. The server should response the <i>Content-MD5</i> header entity to make this method work.<br />
 Use this method on big binary files on HTTP sites and only if the server supports it. (netstiff will tell you.)<br />
 This method is not available on FTP URIs.</p>
<dt><code>size</code></p>
<dd> On HTTP URIs, this method downloads the HTTP header to check if the file size has changed. This feature needs the server to response the <i>Content-Length</i> header entity.<br />
 On FTP URIs, this method requests the size of the file on the FTP site to check if it has changed.</p>
<dt><code>/regexp/</code></p>
<dd> This method downloads the HTTP content and checks if the given regular expression matches or not. The URI is prompted (when using <code>update</code>) iff this match status has changed.<br />
 This method is not available on FTP URIs. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> The number of errors are returned. So exit code 0 is success. </p>
<h2>BUGS</h2>
<p> The regular expression stuff is using the <i>eval</i> function of Ruby. This means that you are able to do non-regex-related stuff using special strings as `regular expressions&#8217;. This is a big security issue when using netstiff as a backend for e.g. Web applications. So do NOT do it and NEVER start netstiff on foreign, unchecked configurations (<code>-W</code> can be dangerous). </p>
<p> Feel free to send feedback, bug reports, etc. </p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> &#169; 2004, 2007-2008 Stephan Beyer &lt;s-beyer [at] gmx.net&gt;, GNU GPL </p>
<h2>Index</h2>
