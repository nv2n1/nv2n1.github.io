---
title: "wget(1)"
name: "wget"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wget/"
description: "Wget – The non-interactive network downloader."
---

<h2 class="name">NAME</h2>
<p> Wget &#8211; The non-interactive network downloader. </p>
<h2>SYNOPSIS</h2>
<p> wget [<i>option</i>]&#8230; [<i></i><font SIZE="-1"><i>URL</i></font><i></i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU</font> Wget is a free utility for non-interactive download of files from the Web. It supports <font SIZE="-1">HTTP, HTTPS,</font> and <font SIZE="-1">FTP</font> protocols, as well as retrieval through <font SIZE="-1">HTTP</font> proxies. </p>
<p> Wget is non-interactive, meaning that it can work in the background, while the user is not logged on. This allows you to start a retrieval and disconnect from the system, letting Wget finish the work. By contrast, most of the Web browsers require constant user&#8217;s presence, which can be a great hindrance when transferring a lot of data. </p>
<p> Wget can follow links in <font SIZE="-1">HTML, XHTML,</font> and <font SIZE="-1">CSS</font> pages, to create local versions of remote web sites, fully recreating the directory structure of the original site. This is sometimes referred to as &#8220;recursive downloading.&#8221; While doing that, Wget respects the Robot Exclusion Standard (<i>/robots.txt</i>). Wget can be instructed to convert the links in downloaded files to point at the local files, for offline viewing. </p>
<p> Wget has been designed for robustness over slow or unstable network connections; if a download fails due to a network problem, it will keep retrying until the whole file has been retrieved. If the server supports regetting, it will instruct the server to continue the download from where it left off.</p>
<h2>OPTIONS</h2>
<h3>Option Syntax</h3>
<p> Since Wget uses <font SIZE="-1">GNU</font> getopt to process command-line arguments, every option has a long form along with the short one. Long options are more convenient to remember, but take time to type. You may freely mix different option styles, or specify options after the command-line arguments. Thus you may write: </p>
<pre>
        wget -r --tries=10 <a rel="nofollow" href="http://fly.srk.fer.hr/">http://fly.srk.fer.hr/</a> -o log
</pre>
<p> The space between the option accepting an argument and the argument may be omitted. Instead of <code>-o log</code> you can write <code>-olog</code>. </p>
<p> You may put several options that do not require arguments together, like: </p>
<pre>
        wget -drc &lt;URL&gt;
</pre>
<p> This is completely equivalent to: </p>
<pre>
        wget -d -r -c &lt;URL&gt;
</pre>
<p> Since the options can be specified after the arguments, you may terminate them with <code>&#8212;</code>. So the following will try to download <font SIZE="-1">URL</font> <code>-x</code>, reporting failure to <i>log</i>: </p>
<pre>
        wget -o log -- -x
</pre>
<p> The options that accept comma-separated lists all respect the convention that specifying an empty list clears its value. This can be useful to clear the <i>.wgetrc</i> settings. For instance, if your <i>.wgetrc</i> sets <tt>&quot;exclude_directories&quot;</tt> to <i>/cgi-bin</i>, the following example will first reset it, and then set it to exclude <i>/~nobody</i> and <i>/~somebody</i>. You can also clear the lists in <i>.wgetrc</i>. </p>
<pre>
        wget -X &quot;&quot; -X /~nobody,/~somebody
</pre>
<p> Most options that do not accept arguments are <i>boolean</i> options, so named because their state can be captured with a yes-or-no (&#8220;boolean&#8221;) variable. For example, <code>&#8211;follow-ftp</code> tells Wget to follow <font SIZE="-1">FTP</font> links from <font SIZE="-1">HTML</font> files and, on the other hand, <code>&#8211;no-glob</code> tells it not to perform file globbing on <font SIZE="-1">FTP</font> URLs. A boolean option is either <i>affirmative</i> or <i>negative</i> (beginning with <code>&#8211;no</code>). All such options share several properties. </p>
<p> Unless stated otherwise, it is assumed that the default behavior is the opposite of what the option accomplishes. For example, the documented existence of <code>&#8211;follow-ftp</code> assumes that the default is to <i>not</i> follow <font SIZE="-1">FTP</font> links from <font SIZE="-1">HTML</font> pages. </p>
<p> Affirmative options can be negated by prepending the <code>&#8211;no-</code> to the option name; negative options can be negated by omitting the <code>&#8211;no-</code> prefix. This might seem superfluous&#8212;if the default for an affirmative option is to not do something, then why provide a way to explicitly turn it off? But the startup file may in fact change the default. For instance, using <tt>&quot;follow_ftp = on&quot;</tt> in <i>.wgetrc</i> makes Wget <i>follow</i> <font SIZE="-1">FTP</font> links by default, and using <code>&#8211;no-follow-ftp</code> is the only way to restore the factory default from the command line.</p>
<h3>Basic Startup Options</h3>
<dl>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the version of Wget.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Print a help message describing all of Wget&#8217;s command-line options.</p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8211;background</code></p>
<dd> Go to background immediately after startup. If no output file is specified via the <code>-o</code>, output is redirected to <i>wget-log</i>.</p>
<dt><code>-e</code> <i>command</i></p>
<dd>
<dt><code>&#8211;execute</code> <i>command</i></p>
<dd> Execute <i>command</i> as if it were a part of <i>.wgetrc</i>. A command thus invoked will be executed <i>after</i> the commands in <i>.wgetrc</i>, thus taking precedence over them. If you need to specify more than one wgetrc command, use multiple instances of <code>-e</code>.</dl>
<h3>Logging and Input File Options</h3>
<dl>
<dt><code>-o</code> <i>logfile</i></p>
<dd>
<dt><code>&#8211;output-file=</code><i>logfile</i></p>
<dd> Log all messages to <i>logfile</i>. The messages are normally reported to standard error.</p>
<dt><code>-a</code> <i>logfile</i></p>
<dd>
<dt><code>&#8211;append-output=</code><i>logfile</i></p>
<dd> Append to <i>logfile</i>. This is the same as <code>-o</code>, only it appends to <i>logfile</i> instead of overwriting the old log file. If <i>logfile</i> does not exist, a new file is created.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Turn on debug output, meaning various information important to the developers of Wget if it does not work properly. Your system administrator may have chosen to compile Wget without debug support, in which case <code>-d</code> will not work. Please note that compiling with debug support is always safe&#8212;Wget compiled with the debug support will <i>not</i> print any debug info unless requested with <code>-d</code>.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Turn off Wget&#8217;s output.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Turn on verbose output, with all the available data. The default output is verbose.</p>
<dt><code>-nv</code></p>
<dd>
<dt><code>&#8211;no-verbose</code></p>
<dd> Turn off verbose without being completely quiet (use <code>-q</code> for that), which means that error messages and basic information still get printed.</p>
<dt><code>&#8211;report-speed=</code><i>type</i></p>
<dd> Output bandwidth as <i>type</i>. The only accepted value is <code>bits</code>.</p>
<dt><code>-i</code> <i>file</i></p>
<dd>
<dt><code>&#8211;input-file=</code><i>file</i></p>
<dd> Read URLs from a local or external <i>file</i>. If <code>&#8211;</code> is specified as <i>file</i>, URLs are read from the standard input. (Use <code>./-</code> to read from a file literally named <code>&#8211;</code>.) </p>
<p> If this function is used, no URLs need be present on the command line. If there are URLs both on the command line and in an input file, those on the command lines will be the first ones to be retrieved. If <code>&#8211;force-html</code> is not specified, then <i>file</i> should consist of a series of URLs, one per line. </p>
<p> However, if you specify <code>&#8211;force-html</code>, the document will be regarded as <code>html</code>. In that case you may have problems with relative links, which you can solve either by adding <tt>&quot;&lt;base href=&quot;</tt>url<tt>&quot;&gt;&quot;</tt> to the documents or by specifying <code>&#8211;base=</code><i>url</i> on the command line. </p>
<p> If the <i>file</i> is an external one, the document will be automatically treated as <code>html</code> if the Content-Type matches <code>text/html</code>. Furthermore, the <i>file</i>&#8216;s location will be implicitly used as base href if none was specified.</p>
<dt><code>&#8211;input-metalink=</code><i>file</i></p>
<dd> Downloads files covered in local Metalink <i>file</i>. Metalink version 3 and 4 are supported.</p>
<dt><code>&#8211;keep-badhash</code></p>
<dd> Keeps downloaded Metalink&#8217;s files with a bad hash. It appends .badhash to the name of Metalink&#8217;s files which have a checksum mismatch, except without overwriting existing files.</p>
<dt><code>&#8211;metalink-over-http</code></p>
<dd> Issues <font SIZE="-1">HTTP HEAD</font> request instead of <font SIZE="-1">GET</font> and extracts Metalink metadata from response headers. Then it switches to Metalink download. If no valid Metalink metadata is found, it falls back to ordinary <font SIZE="-1">HTTP</font> download. Enables <code>Content-Type: application/metalink4+xml</code> files download/processing.</p>
<dt><code>&#8211;metalink-index=</code><i>number</i></p>
<dd> Set the Metalink <code>application/metalink4+xml</code> metaurl ordinal <font SIZE="-1">NUMBER.</font> From 1 to the total number of &#8220;application/metalink4+xml&#8221; available. Specify 0 or <code>inf</code> to choose the first good one. Metaurls, such as those from a <code>&#8211;metalink-over-http</code>, may have been sorted by priority key&#8217;s value; keep this in mind to choose the right <font SIZE="-1">NUMBER.</font></p>
<dt><code>&#8211;preferred-location</code></p>
<dd> Set preferred location for Metalink resources. This has effect if multiple resources with same priority are available.</p>
<dt><code>&#8211;xattr</code></p>
<dd> Enable use of file system&#8217;s extended attributes to save the original <font SIZE="-1">URL</font> and the Referer <font SIZE="-1">HTTP</font> header value if used. </p>
<p> Be aware that the <font SIZE="-1">URL</font> might contain private information like access tokens or credentials.</p>
<dt><code>-F</code></p>
<dd>
<dt><code>&#8211;force-html</code></p>
<dd> When input is read from a file, force it to be treated as an <font SIZE="-1">HTML</font> file. This enables you to retrieve relative links from existing <font SIZE="-1">HTML</font> files on your local disk, by adding <tt>&quot;&lt;base href=&quot;</tt>url<tt>&quot;&gt;&quot;</tt> to <font SIZE="-1">HTML,</font> or using the <code>&#8211;base</code> command-line option.</p>
<dt><code>-B</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd>
<dt><code>&#8211;base=</code><i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> Resolves relative links using <i></i><font SIZE="-1"><i>URL</i></font><i></i> as the point of reference, when reading links from an <font SIZE="-1">HTML</font> file specified via the <code>-i</code>/<code>&#8211;input-file</code> option (together with <code>&#8211;force-html</code>, or when the input file was fetched remotely from a server describing it as <font SIZE="-1">HTML</font>). This is equivalent to the presence of a <tt>&quot;BASE&quot;</tt> tag in the <font SIZE="-1">HTML</font> input file, with <i></i><font SIZE="-1"><i>URL</i></font><i></i> as the value for the <tt>&quot;href&quot;</tt> attribute. </p>
<p> For instance, if you specify <code><a rel="nofollow" href="http://foo/bar/a.html">http://foo/bar/a.html</a></code> for <i></i><font SIZE="-1"><i>URL</i></font><i></i>, and Wget reads <code>../baz/b.html</code> from the input file, it would be resolved to <code><a rel="nofollow" href="http://foo/baz/b.html">http://foo/baz/b.html</a></code>.</p>
<dt><code>&#8211;config=</code><i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Specify the location of a startup file you wish to use instead of the default one(s). Use &#8211;no-config to disable reading of config files. If both &#8211;config and &#8211;no-config are given, &#8211;no-config is ignored.</p>
<dt><code>&#8211;rejected-log=</code><i>logfile</i></p>
<dd> Logs all <font SIZE="-1">URL</font> rejections to <i>logfile</i> as comma separated values. The values include the reason of rejection, the <font SIZE="-1">URL</font> and the parent <font SIZE="-1">URL</font> it was found in.</dl>
<h3>Download Options</h3>
<dl>
<dt><code>&#8211;bind-address=</code><i></i><font SIZE="-1"><i>ADDRESS</i></font><i></i></p>
<dd> When making client <font SIZE="-1">TCP/IP</font> connections, bind to <i></i><font SIZE="-1"><i>ADDRESS</i></font><i></i> on the local machine. <i></i><font SIZE="-1"><i>ADDRESS</i></font><i></i> may be specified as a hostname or <font SIZE="-1">IP</font> address. This option can be useful if your machine is bound to multiple IPs.</p>
<dt><code>&#8211;bind-dns-address=</code><i></i><font SIZE="-1"><i>ADDRESS</i></font><i></i></p>
<dd> [libcares only] This address overrides the route for <font SIZE="-1">DNS</font> requests. If you ever need to circumvent the standard settings from /etc/resolv.conf, this option together with <code>&#8211;dns-servers</code> is your friend. <i></i><font SIZE="-1"><i>ADDRESS</i></font><i></i> must be specified either as IPv4 or IPv6 address. Wget needs to be built with libcares for this option to be available.</p>
<dt><code>&#8211;dns-servers=</code><i></i><font SIZE="-1"><i>ADDRESSES</i></font><i></i></p>
<dd> [libcares only] The given address(es) override the standard nameserver addresses, e.g. as configured in /etc/resolv.conf. <i></i><font SIZE="-1"><i>ADDRESSES</i></font><i></i> may be specified either as IPv4 or IPv6 addresses, comma-separated. Wget needs to be built with libcares for this option to be available.</p>
<dt><code>-t</code> <i>number</i></p>
<dd>
<dt><code>&#8211;tries=</code><i>number</i></p>
<dd> Set number of tries to <i>number</i>. Specify 0 or <code>inf</code> for infinite retrying. The default is to retry 20 times, with the exception of fatal errors like &#8220;connection refused&#8221; or &#8220;not found&#8221; (404), which are not retried.</p>
<dt><code>-O</code> <i>file</i></p>
<dd>
<dt><code>&#8211;output-document=</code><i>file</i></p>
<dd> The documents will not be written to the appropriate files, but all will be concatenated together and written to <i>file</i>. If <code>&#8211;</code> is used as <i>file</i>, documents will be printed to standard output, disabling link conversion. (Use <code>./-</code> to print to a file literally named <code>&#8211;</code>.) </p>
<p> Use of <code>-O</code> is <i>not</i> intended to mean simply &quot;use the name <i>file</i> instead of the one in the <font SIZE="-1">URL</font>;&quot; rather, it is analogous to shell redirection: <code>wget -O file <a rel="nofollow" href="http://foo">http://foo</a></code> is intended to work like <code>wget -O &#8211; <a rel="nofollow" href="http://foo">http://foo</a> &gt; file</code>; <i>file</i> will be truncated immediately, and <i>all</i> downloaded content will be written there. </p>
<p> For this reason, <code>-N</code> (for timestamp-checking) is not supported in combination with <code>-O</code>: since <i>file</i> is always newly created, it will always have a very new timestamp. A warning will be issued if this combination is used. </p>
<p> Similarly, using <code>-r</code> or <code>-p</code> with <code>-O</code> may not work as you expect: Wget won&#8217;t just download the first file to <i>file</i> and then download the rest to their normal names: <i>all</i> downloaded content will be placed in <i>file</i>. This was disabled in version 1.11, but has been reinstated (with a warning) in 1.11.2, as there are some cases where this behavior can actually have some use. </p>
<p> A combination with <code>-nc</code> is only accepted if the given output file does not exist. </p>
<p> Note that a combination with <code>-k</code> is only permitted when downloading a single document, as in that case it will just convert all relative URIs to external ones; <code>-k</code> makes no sense for multiple URIs when they&#8217;re all being downloaded to a single file; <code>-k</code> can be used only when the output is a regular file.</p>
<dt><code>-nc</code></p>
<dd>
<dt><code>&#8211;no-clobber</code></p>
<dd> If a file is downloaded more than once in the same directory, Wget&#8217;s behavior depends on a few options, including <code>-nc</code>. In certain cases, the local file will be <i>clobbered</i>, or overwritten, upon repeated download. In other cases it will be preserved. </p>
<p> When running Wget without <code>-N</code>, <code>-nc</code>, <code>-r</code>, or <code>-p</code>, downloading the same file in the same directory will result in the original copy of <i>file</i> being preserved and the second copy being named <i>file</i><code>.1</code>. If that file is downloaded yet again, the third copy will be named <i>file</i><code>.2</code>, and so on. (This is also the behavior with <code>-nd</code>, even if <code>-r</code> or <code>-p</code> are in effect.) When <code>-nc</code> is specified, this behavior is suppressed, and Wget will refuse to download newer copies of <i>file</i>. Therefore, &quot;<tt>&quot;no-clobber&quot;</tt>&quot; is actually a misnomer in this mode&#8212;it&#8217;s not clobbering that&#8217;s prevented (as the numeric suffixes were already preventing clobbering), but rather the multiple version saving that&#8217;s prevented. </p>
<p> When running Wget with <code>-r</code> or <code>-p</code>, but without <code>-N</code>, <code>-nd</code>, or <code>-nc</code>, re-downloading a file will result in the new copy simply overwriting the old. Adding <code>-nc</code> will prevent this behavior, instead causing the original version to be preserved and any newer copies on the server to be ignored. </p>
<p> When running Wget with <code>-N</code>, with or without <code>-r</code> or <code>-p</code>, the decision as to whether or not to download a newer copy of a file depends on the local and remote timestamp and size of the file. <code>-nc</code> may not be specified at the same time as <code>-N</code>. </p>
<p> A combination with <code>-O</code>/<code>&#8211;output-document</code> is only accepted if the given output file does not exist. </p>
<p> Note that when <code>-nc</code> is specified, files with the suffixes <code>.html</code> or <code>.htm</code> will be loaded from the local disk and parsed as if they had been retrieved from the Web.</p>
<dt><code>&#8211;backups=</code><i>backups</i></p>
<dd> Before (over)writing a file, back up an existing file by adding a <code>.1</code> suffix (<code>_1</code> on <font SIZE="-1">VMS</font>) to the file name. Such backup files are rotated to <code>.2</code>, <code>.3</code>, and so on, up to <i>backups</i> (and lost beyond that).</p>
<dt><code>&#8211;no-netrc</code></p>
<dd> Do not try to obtain credentials from <i>.netrc</i> file. By default <i>.netrc</i> file is searched for credentials in case none have been passed on command line and authentication is required.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;continue</code></p>
<dd> Continue getting a partially-downloaded file. This is useful when you want to finish up a download started by a previous instance of Wget, or by another program. For instance: </p>
<pre>
        wget -c <a href="ftp://sunsite.doc.ic.ac.uk/ls-lR.Z">ftp://sunsite.doc.ic.ac.uk/ls-lR.Z</a>
</pre>
<p> If there is a file named <i>ls-lR.Z</i> in the current directory, Wget will assume that it is the first portion of the remote file, and will ask the server to continue the retrieval from an offset equal to the length of the local file. </p>
<p> Note that you don&#8217;t need to specify this option if you just want the current invocation of Wget to retry downloading a file should the connection be lost midway through. This is the default behavior. <code>-c</code> only affects resumption of downloads started <i>prior</i> to this invocation of Wget, and whose local files are still sitting around. </p>
<p> Without <code>-c</code>, the previous example would just download the remote file to <i>ls-lR.Z.1</i>, leaving the truncated <i>ls-lR.Z</i> file alone. </p>
<p> If you use <code>-c</code> on a non-empty file, and the server does not support continued downloading, Wget will restart the download from scratch and overwrite the existing file entirely. </p>
<p> Beginning with Wget 1.7, if you use <code>-c</code> on a file which is of equal size as the one on the server, Wget will refuse to download the file and print an explanatory message. The same happens when the file is smaller on the server than locally (presumably because it was changed on the server since your last download attempt)&#8212;because &#8220;continuing&#8221; is not meaningful, no download occurs. </p>
<p> On the other side of the coin, while using <code>-c</code>, any file that&#8217;s bigger on the server than locally will be considered an incomplete download and only <tt>&quot;(length(remote) - length(local))&quot;</tt> bytes will be downloaded and tacked onto the end of the local file. This behavior can be desirable in certain cases&#8212;for instance, you can use <code>wget -c</code> to download just the new portion that&#8217;s been appended to a data collection or log file. </p>
<p> However, if the file is bigger on the server because it&#8217;s been <i>changed</i>, as opposed to just <i>appended</i> to, you&#8217;ll end up with a garbled file. Wget has no way of verifying that the local file is really a valid prefix of the remote file. You need to be especially careful of this when using <code>-c</code> in conjunction with <code>-r</code>, since every file will be considered as an &#8220;incomplete download&#8221; candidate. </p>
<p> Another instance where you&#8217;ll get a garbled file if you try to use <code>-c</code> is if you have a lame <font SIZE="-1">HTTP</font> proxy that inserts a &#8220;transfer interrupted&#8221; string into the local file. In the future a &#8220;rollback&#8221; option may be added to deal with this case. </p>
<p> Note that <code>-c</code> only works with <font SIZE="-1">FTP</font> servers and with <font SIZE="-1">HTTP</font> servers that support the <tt>&quot;Range&quot;</tt> header.</p>
<dt><code>&#8211;start-pos=</code><i></i><font SIZE="-1"><i>OFFSET</i></font><i></i></p>
<dd> Start downloading at zero-based position <i></i><font SIZE="-1"><i>OFFSET</i></font><i></i>. Offset may be expressed in bytes, kilobytes with the `k&#8217; suffix, or megabytes with the `m&#8217; suffix, etc. </p>
<p> <code>&#8211;start-pos</code> has higher precedence over <code>&#8211;continue</code>. When <code>&#8211;start-pos</code> and <code>&#8211;continue</code> are both specified, wget will emit a warning then proceed as if <code>&#8211;continue</code> was absent. </p>
<p> Server support for continued download is required, otherwise <code>&#8211;start-pos</code> cannot help. See <code>-c</code> for details.</p>
<dt><code>&#8211;progress=</code><i>type</i></p>
<dd> Select the type of the progress indicator you wish to use. Legal indicators are &#8220;dot&#8221; and &#8220;bar&#8221;. </p>
<p> The &#8220;bar&#8221; indicator is used by default. It draws an <font SIZE="-1">ASCII</font> progress bar graphics (a.k.a &#8220;thermometer&#8221; display) indicating the status of retrieval. If the output is not a <font SIZE="-1">TTY,</font> the &#8220;dot&#8221; bar will be used by default. </p>
<p> Use <code>&#8211;progress=dot</code> to switch to the &#8220;dot&#8221; display. It traces the retrieval by printing dots on the screen, each dot representing a fixed amount of downloaded data. </p>
<p> The progress <i>type</i> can also take one or more parameters. The parameters vary based on the <i>type</i> selected. Parameters to <i>type</i> are passed by appending them to the type sperated by a colon (:) like this: <code>&#8211;progress=</code><i>type</i><code>:</code><i>parameter1</i><code>:</code><i>parameter2</i>. </p>
<p> When using the dotted retrieval, you may set the <i>style</i> by specifying the type as <code>dot:</code><i>style</i>. Different styles assign different meaning to one dot. With the <tt>&quot;default&quot;</tt> style each dot represents 1K, there are ten dots in a cluster and 50 dots in a line. The <tt>&quot;binary&quot;</tt> style has a more &#8220;computer&#8221;-like orientation&#8212;8K dots, 16-dots clusters and 48 dots per line (which makes for 384K lines). The <tt>&quot;mega&quot;</tt> style is suitable for downloading large files&#8212;each dot represents 64K retrieved, there are eight dots in a cluster, and 48 dots on each line (so each line contains 3M). If <tt>&quot;mega&quot;</tt> is not enough then you can use the <tt>&quot;giga&quot;</tt> style&#8212;each dot represents 1M retrieved, there are eight dots in a cluster, and 32 dots on each line (so each line contains 32M). </p>
<p> With <code>&#8211;progress=bar</code>, there are currently two possible parameters, <i>force</i> and <i>noscroll</i>. </p>
<p> When the output is not a <font SIZE="-1">TTY,</font> the progress bar always falls back to &#8220;dot&#8221;, even if <code>&#8211;progress=bar</code> was passed to Wget during invocation. This behaviour can be overridden and the &#8220;bar&#8221; output forced by using the &#8220;force&#8221; parameter as <code>&#8211;progress=bar:force</code>. </p>
<p> By default, the <code>bar</code> style progress bar scroll the name of the file from left to right for the file being downloaded if the filename exceeds the maximum length allotted for its display. In certain cases, such as with <code>&#8211;progress=bar:force</code>, one may not want the scrolling filename in the progress bar. By passing the &#8220;noscroll&#8221; parameter, Wget can be forced to display as much of the filename as possible without scrolling through it. </p>
<p> Note that you can set the default style using the <tt>&quot;progress&quot;</tt> command in <i>.wgetrc</i>. That setting may be overridden from the command line. For example, to force the bar output without scrolling, use <code>&#8211;progress=bar:force:noscroll</code>.</p>
<dt><code>&#8211;show-progress</code></p>
<dd> Force wget to display the progress bar in any verbosity. </p>
<p> By default, wget only displays the progress bar in verbose mode. One may however, want wget to display the progress bar on screen in conjunction with any other verbosity modes like <code>&#8211;no-verbose</code> or <code>&#8211;quiet</code>. This is often a desired a property when invoking wget to download several small/large files. In such a case, wget could simply be invoked with this parameter to get a much cleaner output on the screen. </p>
<p> This option will also force the progress bar to be printed to <i>stderr</i> when used alongside the <code>&#8211;output-file</code> option.</p>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;timestamping</code></p>
<dd> Turn on time-stamping.</p>
<dt><code>&#8211;no-if-modified-since</code></p>
<dd> Do not send If-Modified-Since header in <code>-N</code> mode. Send preliminary <font SIZE="-1">HEAD</font> request instead. This has only effect in <code>-N</code> mode.</p>
<dt><code>&#8211;no-use-server-timestamps</code></p>
<dd> Don&#8217;t set the local file&#8217;s timestamp by the one on the server. </p>
<p> By default, when a file is downloaded, its timestamps are set to match those from the remote file. This allows the use of <code>&#8211;timestamping</code> on subsequent invocations of wget. However, it is sometimes useful to base the local file&#8217;s timestamp on when it was actually downloaded; for that purpose, the <code>&#8211;no-use-server-timestamps</code> option has been provided.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;server-response</code></p>
<dd> Print the headers sent by <font SIZE="-1">HTTP</font> servers and responses sent by <font SIZE="-1">FTP</font> servers.</p>
<dt><code>&#8211;spider</code></p>
<dd> When invoked with this option, Wget will behave as a Web <i>spider</i>, which means that it will not download the pages, just check that they are there. For example, you can use Wget to check your bookmarks: </p>
<pre>
        wget --spider --force-html -i bookmarks.html
</pre>
<p> This feature needs much more work for Wget to get close to the functionality of real web spiders.</p>
<dt><code>-T seconds</code></p>
<dd>
<dt><code>&#8211;timeout=</code><i>seconds</i></p>
<dd> Set the network timeout to <i>seconds</i> seconds. This is equivalent to specifying <code>&#8211;dns-timeout</code>, <code>&#8211;connect-timeout</code>, and <code>&#8211;read-timeout</code>, all at the same time. </p>
<p> When interacting with the network, Wget can check for timeout and abort the operation if it takes too long. This prevents anomalies like hanging reads and infinite connects. The only timeout enabled by default is a 900-second read timeout. Setting a timeout to 0 disables it altogether. Unless you know what you are doing, it is best not to change the default timeout settings. </p>
<p> All timeout-related options accept decimal values, as well as subsecond values. For example, <code>0.1</code> seconds is a legal (though unwise) choice of timeout. Subsecond timeouts are useful for checking server response times or for testing network latency.</p>
<dt><code>&#8211;dns-timeout=</code><i>seconds</i></p>
<dd> Set the <font SIZE="-1">DNS</font> lookup timeout to <i>seconds</i> seconds. <font SIZE="-1">DNS</font> lookups that don&#8217;t complete within the specified time will fail. By default, there is no timeout on <font SIZE="-1">DNS</font> lookups, other than that implemented by system libraries.</p>
<dt><code>&#8211;connect-timeout=</code><i>seconds</i></p>
<dd> Set the connect timeout to <i>seconds</i> seconds. <font SIZE="-1">TCP</font> connections that take longer to establish will be aborted. By default, there is no connect timeout, other than that implemented by system libraries.</p>
<dt><code>&#8211;read-timeout=</code><i>seconds</i></p>
<dd> Set the read (and write) timeout to <i>seconds</i> seconds. The &#8220;time&#8221; of this timeout refers to <i>idle time</i>: if, at any point in the download, no data is received for more than the specified number of seconds, reading fails and the download is restarted. This option does not directly affect the duration of the entire download. </p>
<p> Of course, the remote server may choose to terminate the connection sooner than this option requires. The default read timeout is 900 seconds.</p>
<dt><code>&#8211;limit-rate=</code><i>amount</i></p>
<dd> Limit the download speed to <i>amount</i> bytes per second. Amount may be expressed in bytes, kilobytes with the <code>k</code> suffix, or megabytes with the <code>m</code> suffix. For example, <code>&#8211;limit-rate=20k</code> will limit the retrieval rate to 20KB/s. This is useful when, for whatever reason, you don&#8217;t want Wget to consume the entire available bandwidth. </p>
<p> This option allows the use of decimal numbers, usually in conjunction with power suffixes; for example, <code>&#8211;limit-rate=2.5k</code> is a legal value. </p>
<p> Note that Wget implements the limiting by sleeping the appropriate amount of time after a network read that took less time than specified by the rate. Eventually this strategy causes the <font SIZE="-1">TCP</font> transfer to slow down to approximately the specified rate. However, it may take some time for this balance to be achieved, so don&#8217;t be surprised if limiting the rate doesn&#8217;t work well with very small files.</p>
<dt><code>-w</code> <i>seconds</i></p>
<dd>
<dt><code>&#8211;wait=</code><i>seconds</i></p>
<dd> Wait the specified number of seconds between the retrievals. Use of this option is recommended, as it lightens the server load by making the requests less frequent. Instead of in seconds, the time can be specified in minutes using the <tt>&quot;m&quot;</tt> suffix, in hours using <tt>&quot;h&quot;</tt> suffix, or in days using <tt>&quot;d&quot;</tt> suffix. </p>
<p> Specifying a large value for this option is useful if the network or the destination host is down, so that Wget can wait long enough to reasonably expect the network error to be fixed before the retry. The waiting interval specified by this function is influenced by <tt>&quot;--random-wait&quot;</tt>, which see.</p>
<dt><code>&#8211;waitretry=</code><i>seconds</i></p>
<dd> If you don&#8217;t want Wget to wait between <i>every</i> retrieval, but only between retries of failed downloads, you can use this option. Wget will use <i>linear backoff</i>, waiting 1 second after the first failure on a given file, then waiting 2 seconds after the second failure on that file, up to the maximum number of <i>seconds</i> you specify. </p>
<p> By default, Wget will assume a value of 10 seconds.</p>
<dt><code>&#8211;random-wait</code></p>
<dd> Some web sites may perform log analysis to identify retrieval programs such as Wget by looking for statistically significant similarities in the time between requests. This option causes the time between requests to vary between 0.5 and 1.5 * <i>wait</i> seconds, where <i>wait</i> was specified using the <code>&#8211;wait</code> option, in order to mask Wget&#8217;s presence from such analysis. </p>
<p> A 2001 article in a publication devoted to development on a popular consumer platform provided code to perform this analysis on the fly. Its author suggested blocking at the class C address level to ensure automated retrieval programs were blocked despite changing DHCP-supplied addresses. </p>
<p> The <code>&#8211;random-wait</code> option was inspired by this ill-advised recommendation to block many unrelated users from a web site due to the actions of one.</p>
<dt><code>&#8211;no-proxy</code></p>
<dd> Don&#8217;t use proxies, even if the appropriate <tt>*_proxy</tt> environment variable is defined.</p>
<dt><code>-Q</code> <i>quota</i></p>
<dd>
<dt><code>&#8211;quota=</code><i>quota</i></p>
<dd> Specify download quota for automatic retrievals. The value can be specified in bytes (default), kilobytes (with <code>k</code> suffix), or megabytes (with <code>m</code> suffix). </p>
<p> Note that quota will never affect downloading a single file. So if you specify <code>wget -Q10k <a rel="nofollow" href="https://example.com/ls-lR.gz">https://example.com/ls-lR.gz</a></code>, all of the <i>ls-lR.gz</i> will be downloaded. The same goes even when several URLs are specified on the command-line. The quota is checked only at the end of each downloaded file, so it will never result in a partially downloaded file. Thus you may safely type <code>wget -Q2m -i sites</code>&#8212;download will be aborted after the file that exhausts the quota is completely downloaded. </p>
<p> Setting quota to 0 or to <code>inf</code> unlimits the download quota.</p>
<dt><code>&#8211;no-dns-cache</code></p>
<dd> Turn off caching of <font SIZE="-1">DNS</font> lookups. Normally, Wget remembers the <font SIZE="-1">IP</font> addresses it looked up from <font SIZE="-1">DNS</font> so it doesn&#8217;t have to repeatedly contact the <font SIZE="-1">DNS</font> server for the same (typically small) set of hosts it retrieves from. This cache exists in memory only; a new Wget run will contact <font SIZE="-1">DNS</font> again. </p>
<p> However, it has been reported that in some situations it is not desirable to cache host names, even for the duration of a short-running application like Wget. With this option Wget issues a new <font SIZE="-1">DNS</font> lookup (more precisely, a new call to <tt>&quot;gethostbyname&quot;</tt> or <tt>&quot;getaddrinfo&quot;</tt>) each time it makes a new connection. Please note that this option will <i>not</i> affect caching that might be performed by the resolving library or by an external caching layer, such as <font SIZE="-1">NSCD.</font> </p>
<p> If you don&#8217;t understand exactly what this option does, you probably won&#8217;t need it.</p>
<dt><code>&#8211;restrict-file-names=</code><i>modes</i></p>
<dd> Change which characters found in remote URLs must be escaped during generation of local filenames. Characters that are <i>restricted</i> by this option are escaped, i.e. replaced with %HH, where <font SIZE="-1"><code>HH</code></font> is the hexadecimal number that corresponds to the restricted character. This option may also be used to force all alphabetical cases to be either lower- or uppercase. </p>
<p> By default, Wget escapes the characters that are not valid or safe as part of file names on your operating system, as well as control characters that are typically unprintable. This option is useful for changing these defaults, perhaps because you are downloading to a non-native partition, or because you want to disable escaping of the control characters, or you want to further restrict characters to only those in the <font SIZE="-1">ASCII</font> range of values. </p>
<p> The <i>modes</i> are a comma-separated set of text values. The acceptable values are <code>unix</code>, <code>windows</code>, <code>nocontrol</code>, <code>ascii</code>, <code>lowercase</code>, and <code>uppercase</code>. The values <code>unix</code> and <code>windows</code> are mutually exclusive (one will override the other), as are <code>lowercase</code> and <code>uppercase</code>. Those last are special cases, as they do not change the set of characters that would be escaped, but rather force local file paths to be converted either to lower- or uppercase. </p>
<p> When &#8220;unix&#8221; is specified, Wget escapes the character <code>/</code> and the control characters in the ranges 0&#8211;31 and 128&#8211;159. This is the default on Unix-like operating systems. </p>
<p> When &#8220;windows&#8221; is given, Wget escapes the characters <code>\</code>, <code>|</code>, <code>/</code>, <code>:</code>, <code>?</code>, <code>&quot;</code>, <code>*</code>, <code>&lt;</code>, <code>&gt;</code>, and the control characters in the ranges 0&#8211;31 and 128&#8211;159. In addition to this, Wget in Windows mode uses <code>+</code> instead of <code>:</code> to separate host and port in local file names, and uses <code>@</code> instead of <code>?</code> to separate the query portion of the file name from the rest. Therefore, a <font SIZE="-1">URL</font> that would be saved as <code><a rel="nofollow" href="http://www.xemacs.org">www.xemacs.org</a>:4300/search.pl?input=blah</code> in Unix mode would be saved as <code><a rel="nofollow" href="http://www.xemacs.org+4300">www.xemacs.org+4300</a>/search.pl [at] input=blah</code> in Windows mode. This mode is the default on Windows. </p>
<p> If you specify <code>nocontrol</code>, then the escaping of the control characters is also switched off. This option may make sense when you are downloading URLs whose names contain <font SIZE="-1">UTF-8</font> characters, on a system which can save and display filenames in <font SIZE="-1">UTF-8</font> (some possible byte values used in <font SIZE="-1">UTF-8</font> byte sequences fall in the range of values designated by Wget as &#8220;controls&#8221;). </p>
<p> The <code>ascii</code> mode is used to specify that any bytes whose values are outside the range of <font SIZE="-1">ASCII</font> characters (that is, greater than 127) shall be escaped. This can be useful when saving filenames whose encoding does not match the one used locally.</p>
<dt><code>-4</code></p>
<dd>
<dt><code>&#8211;inet4-only</code></p>
<dd>
<dt><code>-6</code></p>
<dd>
<dt><code>&#8211;inet6-only</code></p>
<dd> Force connecting to IPv4 or IPv6 addresses. With <code>&#8211;inet4-only</code> or <code>-4</code>, Wget will only connect to IPv4 hosts, ignoring <font SIZE="-1">AAAA</font> records in <font SIZE="-1">DNS,</font> and refusing to connect to IPv6 addresses specified in URLs. Conversely, with <code>&#8211;inet6-only</code> or <code>-6</code>, Wget will only connect to IPv6 hosts and ignore A records and IPv4 addresses. </p>
<p> Neither options should be needed normally. By default, an IPv6-aware Wget will use the address family specified by the host&#8217;s <font SIZE="-1">DNS</font> record. If the <font SIZE="-1">DNS</font> responds with both IPv4 and IPv6 addresses, Wget will try them in sequence until it finds one it can connect to. (Also see <tt>&quot;--prefer-family&quot;</tt> option described below.) </p>
<p> These options can be used to deliberately force the use of IPv4 or IPv6 address families on dual family systems, usually to aid debugging or to deal with broken network configuration. Only one of <code>&#8211;inet6-only</code> and <code>&#8211;inet4-only</code> may be specified at the same time. Neither option is available in Wget compiled without IPv6 support.</p>
<dt><code>&#8211;prefer-family=none/IPv4/IPv6</code></p>
<dd> When given a choice of several addresses, connect to the addresses with specified address family first. The address order returned by <font SIZE="-1">DNS</font> is used without change by default. </p>
<p> This avoids spurious errors and connect attempts when accessing hosts that resolve to both IPv6 and IPv4 addresses from IPv4 networks. For example, <code><a rel="nofollow" href="http://www.kame.net">www.kame.net</a></code> resolves to <code>2001:200:0:8002:203:47ff:fea5:3085</code> and to <code>203.178.141.194</code>. When the preferred family is <tt>&quot;IPv4&quot;</tt>, the IPv4 address is used first; when the preferred family is <tt>&quot;IPv6&quot;</tt>, the IPv6 address is used first; if the specified value is <tt>&quot;none&quot;</tt>, the address order returned by <font SIZE="-1">DNS</font> is used without change. </p>
<p> Unlike <code>-4</code> and <code>-6</code>, this option doesn&#8217;t inhibit access to any address family, it only changes the <i>order</i> in which the addresses are accessed. Also note that the reordering performed by this option is <i>stable</i>&#8212;it doesn&#8217;t affect order of addresses of the same family. That is, the relative order of all IPv4 addresses and of all IPv6 addresses remains intact in all cases.</p>
<dt><code>&#8211;retry-connrefused</code></p>
<dd> Consider &#8220;connection refused&#8221; a transient error and try again. Normally Wget gives up on a <font SIZE="-1">URL</font> when it is unable to connect to the site because failure to connect is taken as a sign that the server is not running at all and that retries would not help. This option is for mirroring unreliable sites whose servers tend to disappear for short periods of time.</p>
<dt><code>&#8211;user=</code><i>user</i></p>
<dd>
<dt><code>&#8211;password=</code><i>password</i></p>
<dd> Specify the username <i>user</i> and password <i>password</i> for both <font SIZE="-1">FTP</font> and <font SIZE="-1">HTTP</font> file retrieval. These parameters can be overridden using the <code>&#8211;ftp-user</code> and <code>&#8211;ftp-password</code> options for <font SIZE="-1">FTP</font> connections and the <code>&#8211;http-user</code> and <code>&#8211;http-password</code> options for <font SIZE="-1">HTTP</font> connections.</p>
<dt><code>&#8211;ask-password</code></p>
<dd> Prompt for a password for each connection established. Cannot be specified when <code>&#8211;password</code> is being used, because they are mutually exclusive.</p>
<dt><code>&#8211;use-askpass=</code><i>command</i></p>
<dd> Prompt for a user and password using the specified command. If no command is specified then the command in the environment variable <font SIZE="-1">WGET_ASKPASS</font> is used. If <font SIZE="-1">WGET_ASKPASS</font> is not set then the command in the environment variable <font SIZE="-1">SSH_ASKPASS</font> is used. </p>
<p> You can set the default command for use-askpass in the <i>.wgetrc</i>. That setting may be overridden from the command line.</p>
<dt><code>&#8211;no-iri</code></p>
<dd> Turn off internationalized <font SIZE="-1">URI</font> (<font SIZE="-1">IRI</font>) support. Use <code>&#8211;iri</code> to turn it on. <font SIZE="-1">IRI</font> support is activated by default. </p>
<p> You can set the default state of <font SIZE="-1">IRI</font> support using the <tt>&quot;iri&quot;</tt> command in <i>.wgetrc</i>. That setting may be overridden from the command line.</p>
<dt><code>&#8211;local-encoding=</code><i>encoding</i></p>
<dd> Force Wget to use <i>encoding</i> as the default system encoding. That affects how Wget converts URLs specified as arguments from locale to <font SIZE="-1">UTF-8</font> for <font SIZE="-1">IRI</font> support. </p>
<p> Wget use the function <tt>&quot;nl_langinfo()&quot;</tt> and then the <tt>&quot;CHARSET&quot;</tt> environment variable to get the locale. If it fails, <font SIZE="-1">ASCII</font> is used. </p>
<p> You can set the default local encoding using the <tt>&quot;local_encoding&quot;</tt> command in <i>.wgetrc</i>. That setting may be overridden from the command line.</p>
<dt><code>&#8211;remote-encoding=</code><i>encoding</i></p>
<dd> Force Wget to use <i>encoding</i> as the default remote server encoding. That affects how Wget converts URIs found in files from remote encoding to <font SIZE="-1">UTF-8</font> during a recursive fetch. This options is only useful for <font SIZE="-1">IRI</font> support, for the interpretation of non-ASCII characters. </p>
<p> For <font SIZE="-1">HTTP,</font> remote encoding can be found in <font SIZE="-1">HTTP</font> <tt>&quot;Content-Type&quot;</tt> header and in <font SIZE="-1">HTML</font> <tt>&quot;Content-Type http-equiv&quot;</tt> meta tag. </p>
<p> You can set the default encoding using the <tt>&quot;remoteencoding&quot;</tt> command in <i>.wgetrc</i>. That setting may be overridden from the command line.</p>
<dt><code>&#8211;unlink</code></p>
<dd> Force Wget to unlink file instead of clobbering existing file. This option is useful for downloading to the directory with hardlinks.</dl>
<h3>Directory Options</h3>
<dl>
<dt><code>-nd</code></p>
<dd>
<dt><code>&#8211;no-directories</code></p>
<dd> Do not create a hierarchy of directories when retrieving recursively. With this option turned on, all files will get saved to the current directory, without clobbering (if a name shows up more than once, the filenames will get extensions <code>.n</code>).</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;force-directories</code></p>
<dd> The opposite of <code>-nd</code>&#8212;create a hierarchy of directories, even if one would not have been created otherwise. E.g. <code>wget -x <a rel="nofollow" href="http://fly.srk.fer.hr/robots.txt">http://fly.srk.fer.hr/robots.txt</a></code> will save the downloaded file to <i>fly.srk.fer.hr/robots.txt</i>.</p>
<dt><code>-nH</code></p>
<dd>
<dt><code>&#8211;no-host-directories</code></p>
<dd> Disable generation of host-prefixed directories. By default, invoking Wget with <code>-r <a rel="nofollow" href="http://fly.srk.fer.hr/">http://fly.srk.fer.hr/</a></code> will create a structure of directories beginning with <i>fly.srk.fer.hr/</i>. This option disables such behavior.</p>
<dt><code>&#8211;protocol-directories</code></p>
<dd> Use the protocol name as a directory component of local file names. For example, with this option, <code>wget -r http://</code><i>host</i> will save to <code>http/</code><i>host</i><code>/&#8230;</code> rather than just to <i>host</i><code>/&#8230;</code>.</p>
<dt><code>&#8211;cut-dirs=</code><i>number</i></p>
<dd> Ignore <i>number</i> directory components. This is useful for getting a fine-grained control over the directory where recursive retrieval will be saved. </p>
<p> Take, for example, the directory at <code><a href="ftp://ftp.xemacs.org/pub/xemacs/">ftp://ftp.xemacs.org/pub/xemacs/</a></code>. If you retrieve it with <code>-r</code>, it will be saved locally under <i><a href="ftp://ftp.xemacs.org">ftp.xemacs.org</a>/pub/xemacs/</i>. While the <code>-nH</code> option can remove the <i><a href="ftp://ftp.xemacs.org">ftp.xemacs.org</a>/</i> part, you are still stuck with <i>pub/xemacs</i>. This is where <code>&#8211;cut-dirs</code> comes in handy; it makes Wget not &#8220;see&#8221; <i>number</i> remote directory components. Here are several examples of how <code>&#8211;cut-dirs</code> option works. </p>
<pre><code>
No options-&gt;ftp.xemacs.org / pub / xemacs /
        -nH-&gt;pub / xemacs /
        -nH-- cut -
    dirs = 1-&gt;xemacs /
               -nH-- cut -
           dirs = 2-&gt;.

                  --cut -
                  dirs = 1-&gt;ftp.xemacs.org / xemacs /
                         ...
</code></pre>
<p> If you just want to get rid of the directory structure, this option is similar to a combination of <code>-nd</code> and <code>-P</code>. However, unlike <code>-nd</code>, <code>&#8211;cut-dirs</code> does not lose with subdirectories&#8212;for instance, with <code>-nH &#8211;cut-dirs=1</code>, a <i>beta/</i> subdirectory will be placed to <i>xemacs/beta</i>, as one would expect.</p>
<dt><code>-P</code> <i>prefix</i></p>
<dd>
<dt><code>&#8211;directory-prefix=</code><i>prefix</i></p>
<dd> Set directory prefix to <i>prefix</i>. The <i>directory prefix</i> is the directory where all other files and subdirectories will be saved to, i.e. the top of the retrieval tree. The default is <code>.</code> (the current directory).</dl>
<h3><font SIZE="-1">HTTP</font> Options</h3>
<dl>
<dt><code>&#8211;default-page=</code><i>name</i></p>
<dd> Use <i>name</i> as the default file name when it isn&#8217;t known (i.e., for URLs that end in a slash), instead of <i>index.html</i>.</p>
<dt><code>-E</code></p>
<dd>
<dt><code>&#8211;adjust-extension</code></p>
<dd> If a file of type <code>application/xhtml+xml</code> or <code>text/html</code> is downloaded and the <font SIZE="-1">URL</font> does not end with the regexp <code>\.[Hh][Tt][Mm][Ll]?</code>, this option will cause the suffix <code>.html</code> to be appended to the local filename. This is useful, for instance, when you&#8217;re mirroring a remote site that uses <code>.asp</code> pages, but you want the mirrored pages to be viewable on your stock Apache server. Another good use for this is when you&#8217;re downloading CGI-generated materials. A <font SIZE="-1">URL</font> like <code><a rel="nofollow" href="http://site.com/article.cgi?25">http://site.com/article.cgi?25</a></code> will be saved as <i>article.cgi?25.html</i>. </p>
<p> Note that filenames changed in this way will be re-downloaded every time you re-mirror a site, because Wget can&#8217;t tell that the local <i>X.html</i> file corresponds to remote <font SIZE="-1">URL</font> <i>X</i> (since it doesn&#8217;t yet know that the <font SIZE="-1">URL</font> produces output of type <code>text/html</code> or <code>application/xhtml+xml</code>. </p>
<p> As of version 1.12, Wget will also ensure that any downloaded files of type <code>text/css</code> end in the suffix <code>.css</code>, and the option was renamed from <code>&#8211;html-extension</code>, to better reflect its new behavior. The old option name is still acceptable, but should now be considered deprecated. </p>
<p> As of version 1.19.2, Wget will also ensure that any downloaded files with a <tt>&quot;Content-Encoding&quot;</tt> of <code>br</code>, <code>compress</code>, <code>deflate</code> or <code>gzip</code> end in the suffix <code>.br</code>, <code>.Z</code>, <code>.zlib</code> and <code>.gz</code> respectively. </p>
<p> At some point in the future, this option may well be expanded to include suffixes for other types of content, including content types that are not parsed by Wget.</p>
<dt><code>&#8211;http-user=</code><i>user</i></p>
<dd>
<dt><code>&#8211;http-password=</code><i>password</i></p>
<dd> Specify the username <i>user</i> and password <i>password</i> on an <font SIZE="-1">HTTP</font> server. According to the type of the challenge, Wget will encode them using either the <tt>&quot;basic&quot;</tt> (insecure), the <tt>&quot;digest&quot;</tt>, or the Windows <tt>&quot;NTLM&quot;</tt> authentication scheme. </p>
<p> Another way to specify username and password is in the <font SIZE="-1">URL</font> itself. Either method reveals your password to anyone who bothers to run <tt>&quot;ps&quot;</tt>. To prevent the passwords from being seen, use the <code>&#8211;use-askpass</code> or store them in <i>.wgetrc</i> or <i>.netrc</i>, and make sure to protect those files from other users with <tt>&quot;chmod&quot;</tt>. If the passwords are really important, do not leave them lying in those files either&#8212;edit the files and delete them after Wget has started the download.</p>
<dt><code>&#8211;no-http-keep-alive</code></p>
<dd> Turn off the &#8220;keep-alive&#8221; feature for <font SIZE="-1">HTTP</font> downloads. Normally, Wget asks the server to keep the connection open so that, when you download more than one document from the same server, they get transferred over the same <font SIZE="-1">TCP</font> connection. This saves time and at the same time reduces the load on the server. </p>
<p> This option is useful when, for some reason, persistent (keep-alive) connections don&#8217;t work for you, for example due to a server bug or due to the inability of server-side scripts to cope with the connections.</p>
<dt><code>&#8211;no-cache</code></p>
<dd> Disable server-side cache. In this case, Wget will send the remote server appropriate directives (<code>Cache-Control: no-cache</code> and <code>Pragma: no-cache</code>) to get the file from the remote service, rather than returning the cached version. This is especially useful for retrieving and flushing out-of-date documents on proxy servers. </p>
<p> Caching is allowed by default.</p>
<dt><code>&#8211;no-cookies</code></p>
<dd> Disable the use of cookies. Cookies are a mechanism for maintaining server-side state. The server sends the client a cookie using the <tt>&quot;Set-Cookie&quot;</tt> header, and the client responds with the same cookie upon further requests. Since cookies allow the server owners to keep track of visitors and for sites to exchange this information, some consider them a breach of privacy. The default is to use cookies; however, <i>storing</i> cookies is not on by default.</p>
<dt><code>&#8211;load-cookies</code> <i>file</i></p>
<dd> Load cookies from <i>file</i> before the first <font SIZE="-1">HTTP</font> retrieval. <i>file</i> is a textual file in the format originally used by Netscape&#8217;s <i>cookies.txt</i> file. </p>
<p> You will typically use this option when mirroring sites that require that you be logged in to access some or all of their content. The login process typically works by the web server issuing an <font SIZE="-1">HTTP</font> cookie upon receiving and verifying your credentials. The cookie is then resent by the browser when accessing that part of the site, and so proves your identity. </p>
<p> Mirroring such a site requires Wget to send the same cookies your browser sends when communicating with the site. This is achieved by <code>&#8211;load-cookies</code>&#8212;simply point Wget to the location of the <i>cookies.txt</i> file, and it will send the same cookies your browser would send in the same situation. Different browsers keep textual cookie files in different locations:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;Netscape 4.x.&quot;</p>
<dd> The cookies are in <i>~/.netscape/cookies.txt</i>.</p>
<dt>&quot;Mozilla and Netscape 6.x.&quot;</p>
<dd> Mozilla&#8217;s cookie file is also named <i>cookies.txt</i>, located somewhere under <i>~/.mozilla</i>, in the directory of your profile. The full path usually ends up looking somewhat like <i>~/.mozilla/default/some-weird-string/cookies.txt</i>.</p>
<dt>&quot;Internet Explorer.&quot;</p>
<dd> You can produce a cookie file Wget can use by using the File menu, Import and Export, Export Cookies. This has been tested with Internet Explorer 5; it is not guaranteed to work with earlier versions.</p>
<dt>&quot;Other browsers.&quot;</p>
<dd> If you are using a different browser to create your cookies, <code>&#8211;load-cookies</code> will only work if you can locate or produce a cookie file in the Netscape format that Wget expects.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If you cannot use <code>&#8211;load-cookies</code>, there might still be an alternative. If your browser supports a &#8220;cookie manager&#8221;, you can use it to view the cookies used when accessing the site you&#8217;re mirroring. Write down the name and value of the cookie, and manually instruct Wget to send those cookies, bypassing the &#8220;official&#8221; cookie support: </p>
<pre>
        wget --no-cookies --header &quot;Cookie: &lt;name&gt;=&lt;value&gt;&quot;
</pre>
</dl>
<dt><code>&#8211;save-cookies</code> <i>file</i></p>
<dd> Save cookies to <i>file</i> before exiting. This will not save cookies that have expired or that have no expiry time (so-called &#8220;session cookies&#8221;), but also see <code>&#8211;keep-session-cookies</code>.</p>
<dt><code>&#8211;keep-session-cookies</code></p>
<dd> When specified, causes <code>&#8211;save-cookies</code> to also save session cookies. Session cookies are normally not saved because they are meant to be kept in memory and forgotten when you exit the browser. Saving them is useful on sites that require you to log in or to visit the home page before you can access some pages. With this option, multiple Wget runs are considered a single browser session as far as the site is concerned. </p>
<p> Since the cookie file format does not normally carry session cookies, Wget marks them with an expiry timestamp of 0. Wget&#8217;s <code>&#8211;load-cookies</code> recognizes those as session cookies, but it might confuse other browsers. Also note that cookies so loaded will be treated as other session cookies, which means that if you want <code>&#8211;save-cookies</code> to preserve them again, you must use <code>&#8211;keep-session-cookies</code> again.</p>
<dt><code>&#8211;ignore-length</code></p>
<dd> Unfortunately, some <font SIZE="-1">HTTP</font> servers (<font SIZE="-1">CGI</font> programs, to be more precise) send out bogus <tt>&quot;Content-Length&quot;</tt> headers, which makes Wget go wild, as it thinks not all the document was retrieved. You can spot this syndrome if Wget retries getting the same document again and again, each time claiming that the (otherwise normal) connection has closed on the very same byte. </p>
<p> With this option, Wget will ignore the <tt>&quot;Content-Length&quot;</tt> header&#8212;as if it never existed.</p>
<dt><code>&#8211;header=</code><i>header-line</i></p>
<dd> Send <i>header-line</i> along with the rest of the headers in each <font SIZE="-1">HTTP</font> request. The supplied header is sent as-is, which means it must contain name and value separated by colon, and must not contain newlines. </p>
<p> You may define more than one additional header by specifying <code>&#8211;header</code> more than once. </p>
<pre>
        wget --header='Accept-Charset: iso-8859-2' \
             --header='Accept-Language: hr'        \
               <a rel="nofollow" href="http://fly.srk.fer.hr/">http://fly.srk.fer.hr/</a>
</pre>
<p> Specification of an empty string as the header value will clear all previous user-defined headers. </p>
<p> As of Wget 1.10, this option can be used to override headers otherwise generated automatically. This example instructs Wget to connect to localhost, but to specify <code>foo.bar</code> in the <tt>&quot;Host&quot;</tt> header: </p>
<pre>
        wget --header=&quot;Host: foo.bar&quot; <a rel="nofollow" href="http://localhost/">http://localhost/</a>
</pre>
<p> In versions of Wget prior to 1.10 such use of <code>&#8211;header</code> caused sending of duplicate headers.</p>
<dt><code>&#8211;compression=</code><i>type</i></p>
<dd> Choose the type of compression to be used. Legal values are <code>auto</code>, <code>gzip</code> and <code>none</code>. </p>
<p> If <code>auto</code> or <code>gzip</code> are specified, Wget asks the server to compress the file using the gzip compression format. If the server compresses the file and responds with the <tt>&quot;Content-Encoding&quot;</tt> header field set appropriately, the file will be decompressed automatically. </p>
<p> If <code>none</code> is specified, wget will not ask the server to compress the file and will not decompress any server responses. This is the default. </p>
<p> Compression support is currently experimental. In case it is turned on, please report any bugs to <tt>&quot;bug-wget [at] gnu.org&quot;</tt>.</p>
<dt><code>&#8211;max-redirect=</code><i>number</i></p>
<dd> Specifies the maximum number of redirections to follow for a resource. The default is 20, which is usually far more than necessary. However, on those occasions where you want to allow more (or fewer), this is the option to use.</p>
<dt><code>&#8211;proxy-user=</code><i>user</i></p>
<dd>
<dt><code>&#8211;proxy-password=</code><i>password</i></p>
<dd> Specify the username <i>user</i> and password <i>password</i> for authentication on a proxy server. Wget will encode them using the <tt>&quot;basic&quot;</tt> authentication scheme. </p>
<p> Security considerations similar to those with <code>&#8211;http-password</code> pertain here as well.</p>
<dt><code>&#8211;referer=</code><i>url</i></p>
<dd> Include `Referer: <i>url</i>&#8216; header in <font SIZE="-1">HTTP</font> request. Useful for retrieving documents with server-side processing that assume they are always being retrieved by interactive web browsers and only come out properly when Referer is set to one of the pages that point to them.</p>
<dt><code>&#8211;save-headers</code></p>
<dd> Save the headers sent by the <font SIZE="-1">HTTP</font> server to the file, preceding the actual contents, with an empty line as the separator.</p>
<dt><code>-U</code> <i>agent-string</i></p>
<dd>
<dt><code>&#8211;user-agent=</code><i>agent-string</i></p>
<dd> Identify as <i>agent-string</i> to the <font SIZE="-1">HTTP</font> server. </p>
<p> The <font SIZE="-1">HTTP</font> protocol allows the clients to identify themselves using a <tt>&quot;User-Agent&quot;</tt> header field. This enables distinguishing the <font SIZE="-1">WWW</font> software, usually for statistical purposes or for tracing of protocol violations. Wget normally identifies as <code>Wget/</code><i>version</i>, <i>version</i> being the current version number of Wget. </p>
<p> However, some sites have been known to impose the policy of tailoring the output according to the <tt>&quot;User-Agent&quot;</tt>-supplied information. While this is not such a bad idea in theory, it has been abused by servers denying information to clients other than (historically) Netscape or, more frequently, Microsoft Internet Explorer. This option allows you to change the <tt>&quot;User-Agent&quot;</tt> line issued by Wget. Use of this option is discouraged, unless you really know what you are doing. </p>
<p> Specifying empty user agent with <code>&#8211;user-agent=&quot;&quot;</code> instructs Wget not to send the <tt>&quot;User-Agent&quot;</tt> header in <font SIZE="-1">HTTP</font> requests.</p>
<dt><code>&#8211;post-data=</code><i>string</i></p>
<dd>
<dt><code>&#8211;post-file=</code><i>file</i></p>
<dd> Use <font SIZE="-1">POST</font> as the method for all <font SIZE="-1">HTTP</font> requests and send the specified data in the request body. <code>&#8211;post-data</code> sends <i>string</i> as data, whereas <code>&#8211;post-file</code> sends the contents of <i>file</i>. Other than that, they work in exactly the same way. In particular, they <i>both</i> expect content of the form <tt>&quot;key1=value1&amp;key2=value2&quot;</tt>, with percent-encoding for special characters; the only difference is that one expects its content as a command-line parameter and the other accepts its content from a file. In particular, <code>&#8211;post-file</code> is <i>not</i> for transmitting files as form attachments: those must appear as <tt>&quot;key=value&quot;</tt> data (with appropriate percent-coding) just like everything else. Wget does not currently support <tt>&quot;multipart/form-data&quot;</tt> for transmitting <font SIZE="-1">POST</font> data; only <tt>&quot;application/x-www-form-urlencoded&quot;</tt>. Only one of <code>&#8211;post-data</code> and <code>&#8211;post-file</code> should be specified. </p>
<p> Please note that wget does not require the content to be of the form <tt>&quot;key1=value1&amp;key2=value2&quot;</tt>, and neither does it test for it. Wget will simply transmit whatever data is provided to it. Most servers however expect the <font SIZE="-1">POST</font> data to be in the above format when processing <font SIZE="-1">HTML</font> Forms. </p>
<p> When sending a <font SIZE="-1">POST</font> request using the <code>&#8211;post-file</code> option, Wget treats the file as a binary file and will send every character in the <font SIZE="-1">POST</font> request without stripping trailing newline or formfeed characters. Any other control characters in the text will also be sent as-is in the <font SIZE="-1">POST</font> request. </p>
<p> Please be aware that Wget needs to know the size of the <font SIZE="-1">POST</font> data in advance. Therefore the argument to <tt>&quot;--post-file&quot;</tt> must be a regular file; specifying a <font SIZE="-1">FIFO</font> or something like <i>/dev/stdin</i> won&#8217;t work. It&#8217;s not quite clear how to work around this limitation inherent in <font SIZE="-1">HTTP/1.0.</font> Although <font SIZE="-1">HTTP/1.1</font> introduces <i>chunked</i> transfer that doesn&#8217;t require knowing the request length in advance, a client can&#8217;t use chunked unless it knows it&#8217;s talking to an <font SIZE="-1">HTTP/1.1</font> server. And it can&#8217;t know that until it receives a response, which in turn requires the request to have been completed &#8212; a chicken-and-egg problem. </p>
<p> Note: As of version 1.15 if Wget is redirected after the <font SIZE="-1">POST</font> request is completed, its behaviour will depend on the response code returned by the server. In case of a 301 Moved Permanently, 302 Moved Temporarily or 307 Temporary Redirect, Wget will, in accordance with <font SIZE="-1">RFC2616,</font> continue to send a <font SIZE="-1">POST</font> request. In case a server wants the client to change the Request method upon redirection, it should send a 303 See Other response code. </p>
<p> This example shows how to log in to a server using <font SIZE="-1">POST</font> and then proceed to download the desired pages, presumably only accessible to authorized users: </p>
<pre>
        # Log in to the server.  This can be done only once.
        wget --save-cookies cookies.txt \
             --post-data 'user=foo&amp;password=bar' \
             <a rel="nofollow" href="http://example.com/auth.php">http://example.com/auth.php</a>
        
        # Now grab the page or pages we care about.
        wget --load-cookies cookies.txt \
             -p <a rel="nofollow" href="http://example.com/interesting/article.php">http://example.com/interesting/article.php</a>
</pre>
<p> If the server is using session cookies to track user authentication, the above will not work because <code>&#8211;save-cookies</code> will not save them (and neither will browsers) and the <i>cookies.txt</i> file will be empty. In that case use <code>&#8211;keep-session-cookies</code> along with <code>&#8211;save-cookies</code> to force saving of session cookies.</p>
<dt><code>&#8211;method=</code><i>HTTP-Method</i></p>
<dd> For the purpose of RESTful scripting, Wget allows sending of other <font SIZE="-1">HTTP</font> Methods without the need to explicitly set them using <code>&#8211;header=Header-Line</code>. Wget will use whatever string is passed to it after <code>&#8211;method</code> as the <font SIZE="-1">HTTP</font> Method to the server.</p>
<dt><code>&#8211;body-data=</code><i>Data-String</i></p>
<dd>
<dt><code>&#8211;body-file=</code><i>Data-File</i></p>
<dd> Must be set when additional data needs to be sent to the server along with the Method specified using <code>&#8211;method</code>. <code>&#8211;body-data</code> sends <i>string</i> as data, whereas <code>&#8211;body-file</code> sends the contents of <i>file</i>. Other than that, they work in exactly the same way. </p>
<p> Currently, <code>&#8211;body-file</code> is <i>not</i> for transmitting files as a whole. Wget does not currently support <tt>&quot;multipart/form-data&quot;</tt> for transmitting data; only <tt>&quot;application/x-www-form-urlencoded&quot;</tt>. In the future, this may be changed so that wget sends the <code>&#8211;body-file</code> as a complete file instead of sending its contents to the server. Please be aware that Wget needs to know the contents of <font SIZE="-1">BODY</font> Data in advance, and hence the argument to <code>&#8211;body-file</code> should be a regular file. See <code>&#8211;post-file</code> for a more detailed explanation. Only one of <code>&#8211;body-data</code> and <code>&#8211;body-file</code> should be specified. </p>
<p> If Wget is redirected after the request is completed, Wget will suspend the current method and send a <font SIZE="-1">GET</font> request till the redirection is completed. This is true for all redirection response codes except 307 Temporary Redirect which is used to explicitly specify that the request method should <i>not</i> change. Another exception is when the method is set to <tt>&quot;POST&quot;</tt>, in which case the redirection rules specified under <code>&#8211;post-data</code> are followed.</p>
<dt><code>&#8211;content-disposition</code></p>
<dd> If this is set to on, experimental (not fully-functional) support for <tt>&quot;Content-Disposition&quot;</tt> headers is enabled. This can currently result in extra round-trips to the server for a <tt>&quot;HEAD&quot;</tt> request, and is known to suffer from a few bugs, which is why it is not currently enabled by default. </p>
<p> This option is useful for some file-downloading <font SIZE="-1">CGI</font> programs that use <tt>&quot;Content-Disposition&quot;</tt> headers to describe what the name of a downloaded file should be. </p>
<p> When combined with <code>&#8211;metalink-over-http</code> and <code>&#8211;trust-server-names</code>, a <code>Content-Type: application/metalink4+xml</code> file is named using the <tt>&quot;Content-Disposition&quot;</tt> filename field, if available.</p>
<dt><code>&#8211;content-on-error</code></p>
<dd> If this is set to on, wget will not skip the content when the server responds with a http status code that indicates error.</p>
<dt><code>&#8211;trust-server-names</code></p>
<dd> If this is set, on a redirect, the local file name will be based on the redirection <font SIZE="-1">URL.</font> By default the local file name is based on the original <font SIZE="-1">URL.</font> When doing recursive retrieving this can be helpful because in many web sites redirected URLs correspond to an underlying file structure, while link URLs do not.</p>
<dt><code>&#8211;auth-no-challenge</code></p>
<dd> If this option is given, Wget will send Basic <font SIZE="-1">HTTP</font> authentication information (plaintext username and password) for all requests, just like Wget 1.10.2 and prior did by default. </p>
<p> Use of this option is not recommended, and is intended only to support some few obscure servers, which never send <font SIZE="-1">HTTP</font> authentication challenges, but accept unsolicited auth info, say, in addition to form-based authentication.</p>
<dt><code>&#8211;retry-on-host-error</code></p>
<dd> Consider host errors, such as &#8220;Temporary failure in name resolution&#8221;, as non-fatal, transient errors.</p>
<dt><code>&#8211;retry-on-http-error=</code><i>code[,code,&#8230;]</i></p>
<dd> Consider given <font SIZE="-1">HTTP</font> response codes as non-fatal, transient errors. Supply a comma-separated list of 3-digit <font SIZE="-1">HTTP</font> response codes as argument. Useful to work around special circumstances where retries are required, but the server responds with an error code normally not retried by Wget. Such errors might be 503 (Service Unavailable) and 429 (Too Many Requests). Retries enabled by this option are performed subject to the normal retry timing and retry count limitations of Wget. </p>
<p> Using this option is intended to support special use cases only and is generally not recommended, as it can force retries even in cases where the server is actually trying to decrease its load. Please use wisely and only if you know what you are doing.</dl>
<h3><font SIZE="-1">HTTPS</font> (<font SIZE="-1">SSL/TLS</font>) Options</h3>
<p> To support encrypted <font SIZE="-1">HTTP</font> (<font SIZE="-1">HTTPS</font>) downloads, Wget must be compiled with an external <font SIZE="-1">SSL</font> library. The current default is GnuTLS. In addition, Wget also supports <font SIZE="-1">HSTS</font> (<font SIZE="-1">HTTP</font> Strict Transport Security). If Wget is compiled without <font SIZE="-1">SSL</font> support, none of these options are available.</p>
<dl>
<dt><code>&#8211;secure-protocol=</code><i>protocol</i></p>
<dd> Choose the secure protocol to be used. Legal values are <code>auto</code>, <code>SSLv2</code>, <code>SSLv3</code>, <code>TLSv1</code>, <code>TLSv1_1</code>, <code>TLSv1_2</code>, <code>TLSv1_3</code> and <font SIZE="-1"><code>PFS</code></font>. If <code>auto</code> is used, the <font SIZE="-1">SSL</font> library is given the liberty of choosing the appropriate protocol automatically, which is achieved by sending a TLSv1 greeting. This is the default. </p>
<p> Specifying <code>SSLv2</code>, <code>SSLv3</code>, <code>TLSv1</code>, <code>TLSv1_1</code>, <code>TLSv1_2</code> or <code>TLSv1_3</code> forces the use of the corresponding protocol. This is useful when talking to old and buggy <font SIZE="-1">SSL</font> server implementations that make it hard for the underlying <font SIZE="-1">SSL</font> library to choose the correct protocol version. Fortunately, such servers are quite rare. </p>
<p> Specifying <font SIZE="-1"><code>PFS</code></font> enforces the use of the so-called Perfect Forward Security cipher suites. In short, <font SIZE="-1">PFS</font> adds security by creating a one-time key for each <font SIZE="-1">SSL</font> connection. It has a bit more <font SIZE="-1">CPU</font> impact on client and server. We use known to be secure ciphers (e.g. no <font SIZE="-1">MD4</font>) and the <font SIZE="-1">TLS</font> protocol. This mode also explicitly excludes non-PFS key exchange methods, such as <font SIZE="-1">RSA.</font></p>
<dt><code>&#8211;https-only</code></p>
<dd> When in recursive mode, only <font SIZE="-1">HTTPS</font> links are followed.</p>
<dt><code>&#8211;ciphers</code></p>
<dd> Set the cipher list string. Typically this string sets the cipher suites and other <font SIZE="-1">SSL/TLS</font> options that the user wish should be used, in a set order of preference (GnuTLS calls it &#8216;priority string&#8217;). This string will be fed verbatim to the <font SIZE="-1">SSL/TLS</font> engine (OpenSSL or GnuTLS) and hence its format and syntax is dependent on that. Wget will not process or manipulate it in any way. Refer to the OpenSSL or GnuTLS documentation for more information.</p>
<dt><code>&#8211;no-check-certificate</code></p>
<dd> Don&#8217;t check the server certificate against the available certificate authorities. Also don&#8217;t require the <font SIZE="-1">URL</font> host name to match the common name presented by the certificate. </p>
<p> As of Wget 1.10, the default is to verify the server&#8217;s certificate against the recognized certificate authorities, breaking the <font SIZE="-1">SSL</font> handshake and aborting the download if the verification fails. Although this provides more secure downloads, it does break interoperability with some sites that worked with previous Wget versions, particularly those using self-signed, expired, or otherwise invalid certificates. This option forces an &#8220;insecure&#8221; mode of operation that turns the certificate verification errors into warnings and allows you to proceed. </p>
<p> If you encounter &#8220;certificate verification&#8221; errors or ones saying that &#8220;common name doesn&#8217;t match requested host name&#8221;, you can use this option to bypass the verification and proceed with the download. <i>Only use this option if you are otherwise convinced of the site&#8217;s authenticity, or if you really don&#8217;t care about the validity of its certificate.</i> It is almost always a bad idea not to check the certificates when transmitting confidential or important data. For self-signed/internal certificates, you should download the certificate and verify against that instead of forcing this insecure mode. If you are really sure of not desiring any certificate verification, you can specify &#8211;check-certificate=quiet to tell wget to not print any warning about invalid certificates, albeit in most cases this is the wrong thing to do.</p>
<dt><code>&#8211;certificate=</code><i>file</i></p>
<dd> Use the client certificate stored in <i>file</i>. This is needed for servers that are configured to require certificates from the clients that connect to them. Normally a certificate is not required and this switch is optional.</p>
<dt><code>&#8211;certificate-type=</code><i>type</i></p>
<dd> Specify the type of the client certificate. Legal values are <font SIZE="-1"><code>PEM</code></font> (assumed by default) and <font SIZE="-1"><code>DER</code></font>, also known as <font SIZE="-1"><code>ASN1</code></font>.</p>
<dt><code>&#8211;private-key=</code><i>file</i></p>
<dd> Read the private key from <i>file</i>. This allows you to provide the private key in a file separate from the certificate.</p>
<dt><code>&#8211;private-key-type=</code><i>type</i></p>
<dd> Specify the type of the private key. Accepted values are <font SIZE="-1"><code>PEM</code></font> (the default) and <font SIZE="-1"><code>DER</code></font>.</p>
<dt><code>&#8211;ca-certificate=</code><i>file</i></p>
<dd> Use <i>file</i> as the file with the bundle of certificate authorities (&#8220;<font SIZE="-1">CA&#8221;</font>) to verify the peers. The certificates must be in <font SIZE="-1">PEM</font> format. </p>
<p> Without this option Wget looks for <font SIZE="-1">CA</font> certificates at the system-specified locations, chosen at OpenSSL installation time.</p>
<dt><code>&#8211;ca-directory=</code><i>directory</i></p>
<dd> Specifies directory containing <font SIZE="-1">CA</font> certificates in <font SIZE="-1">PEM</font> format. Each file contains one <font SIZE="-1">CA</font> certificate, and the file name is based on a hash value derived from the certificate. This is achieved by processing a certificate directory with the <tt>&quot;c_rehash&quot;</tt> utility supplied with OpenSSL. Using <code>&#8211;ca-directory</code> is more efficient than <code>&#8211;ca-certificate</code> when many certificates are installed because it allows Wget to fetch certificates on demand. </p>
<p> Without this option Wget looks for <font SIZE="-1">CA</font> certificates at the system-specified locations, chosen at OpenSSL installation time.</p>
<dt><code>&#8211;crl-file=</code><i>file</i></p>
<dd> Specifies a <font SIZE="-1">CRL</font> file in <i>file</i>. This is needed for certificates that have been revocated by the CAs.</p>
<dt><code>&#8211;pinnedpubkey=file/hashes</code></p>
<dd> Tells wget to use the specified public key file (or hashes) to verify the peer. This can be a path to a file which contains a single public key in <font SIZE="-1">PEM</font> or <font SIZE="-1">DER</font> format, or any number of base64 encoded sha256 hashes preceded by &#8220;sha256//&#8221; and separated by &#8220;;&#8221; </p>
<p> When negotiating a <font SIZE="-1">TLS</font> or <font SIZE="-1">SSL</font> connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key(s) provided to this option, wget will abort the connection before sending or receiving any data.</p>
<dt><code>&#8211;random-file=</code><i>file</i></p>
<dd> [OpenSSL and LibreSSL only] Use <i>file</i> as the source of random data for seeding the pseudo-random number generator on systems without <i>/dev/urandom</i>. </p>
<p> On such systems the <font SIZE="-1">SSL</font> library needs an external source of randomness to initialize. Randomness may be provided by <font SIZE="-1">EGD</font> (see <code>&#8211;egd-file</code> below) or read from an external source specified by the user. If this option is not specified, Wget looks for random data in <tt>$RANDFILE</tt> or, if that is unset, in <i></i>$HOME<i>/.rnd</i>. </p>
<p> If you&#8217;re getting the &#8220;Could not seed OpenSSL <font SIZE="-1">PRNG</font>; disabling <font SIZE="-1">SSL.&#8221;</font> error, you should provide random data using some of the methods described above.</p>
<dt><code>&#8211;egd-file=</code><i>file</i></p>
<dd> [OpenSSL only] Use <i>file</i> as the <font SIZE="-1">EGD</font> socket. <font SIZE="-1">EGD</font> stands for <i>Entropy Gathering Daemon</i>, a user-space program that collects data from various unpredictable system sources and makes it available to other programs that might need it. Encryption software, such as the <font SIZE="-1">SSL</font> library, needs sources of non-repeating randomness to seed the random number generator used to produce cryptographically strong keys. </p>
<p> OpenSSL allows the user to specify his own source of entropy using the <tt>&quot;RAND_FILE&quot;</tt> environment variable. If this variable is unset, or if the specified file does not produce enough randomness, OpenSSL will read random data from <font SIZE="-1">EGD</font> socket specified using this option. </p>
<p> If this option is not specified (and the equivalent startup command is not used), <font SIZE="-1">EGD</font> is never contacted. <font SIZE="-1">EGD</font> is not needed on modern Unix systems that support <i>/dev/urandom</i>.</p>
<dt><code>&#8211;no-hsts</code></p>
<dd> Wget supports <font SIZE="-1">HSTS</font> (<font SIZE="-1">HTTP</font> Strict Transport Security, <font SIZE="-1">RFC 6797</font>) by default. Use <code>&#8211;no-hsts</code> to make Wget act as a non-HSTS-compliant <font SIZE="-1">UA.</font> As a consequence, Wget would ignore all the <tt>&quot;Strict-Transport-Security&quot;</tt> headers, and would not enforce any existing <font SIZE="-1">HSTS</font> policy.</p>
<dt><code>&#8211;hsts-file=</code><i>file</i></p>
<dd> By default, Wget stores its <font SIZE="-1">HSTS</font> database in <i>~/.wget-hsts</i>. You can use <code>&#8211;hsts-file</code> to override this. Wget will use the supplied file as the <font SIZE="-1">HSTS</font> database. Such file must conform to the correct <font SIZE="-1">HSTS</font> database format used by Wget. If Wget cannot parse the provided file, the behaviour is unspecified. </p>
<p> The Wget&#8217;s <font SIZE="-1">HSTS</font> database is a plain text file. Each line contains an <font SIZE="-1">HSTS</font> entry (ie. a site that has issued a <tt>&quot;Strict-Transport-Security&quot;</tt> header and that therefore has specified a concrete <font SIZE="-1">HSTS</font> policy to be applied). Lines starting with a dash (<tt>&quot;#&quot;</tt>) are ignored by Wget. Please note that in spite of this convenient human-readability hand-hacking the <font SIZE="-1">HSTS</font> database is generally not a good idea. </p>
<p> An <font SIZE="-1">HSTS</font> entry line consists of several fields separated by one or more whitespace: </p>
<p> <tt>&quot;&lt;hostname&gt; SP [&lt;port&gt;] SP &lt;include subdomains&gt; SP &lt;created&gt; SP &lt;max-age&gt;&quot;</tt> </p>
<p> The <i>hostname</i> and <i>port</i> fields indicate the hostname and port to which the given <font SIZE="-1">HSTS</font> policy applies. The <i>port</i> field may be zero, and it will, in most of the cases. That means that the port number will not be taken into account when deciding whether such <font SIZE="-1">HSTS</font> policy should be applied on a given request (only the hostname will be evaluated). When <i>port</i> is different to zero, both the target hostname and the port will be evaluated and the <font SIZE="-1">HSTS</font> policy will only be applied if both of them match. This feature has been included for testing/development purposes only. The Wget testsuite (in <i>testenv/</i>) creates <font SIZE="-1">HSTS</font> databases with explicit ports with the purpose of ensuring Wget&#8217;s correct behaviour. Applying <font SIZE="-1">HSTS</font> policies to ports other than the default ones is discouraged by <font SIZE="-1">RFC 6797</font> (see Appendix B &#8220;Differences between <font SIZE="-1">HSTS</font> Policy and Same-Origin Policy&#8221;). Thus, this functionality should not be used in production environments and <i>port</i> will typically be zero. The last three fields do what they are expected to. The field <i>include_subdomains</i> can either be <tt>1</tt> or <tt>0</tt> and it signals whether the subdomains of the target domain should be part of the given <font SIZE="-1">HSTS</font> policy as well. The <i>created</i> and <i>max-age</i> fields hold the timestamp values of when such entry was created (first seen by Wget) and the HSTS-defined value &#8216;max-age&#8217;, which states how long should that <font SIZE="-1">HSTS</font> policy remain active, measured in seconds elapsed since the timestamp stored in <i>created</i>. Once that time has passed, that <font SIZE="-1">HSTS</font> policy will no longer be valid and will eventually be removed from the database. </p>
<p> If you supply your own <font SIZE="-1">HSTS</font> database via <code>&#8211;hsts-file</code>, be aware that Wget may modify the provided file if any change occurs between the <font SIZE="-1">HSTS</font> policies requested by the remote servers and those in the file. When Wget exits, it effectively updates the <font SIZE="-1">HSTS</font> database by rewriting the database file with the new entries. </p>
<p> If the supplied file does not exist, Wget will create one. This file will contain the new <font SIZE="-1">HSTS</font> entries. If no <font SIZE="-1">HSTS</font> entries were generated (no <tt>&quot;Strict-Transport-Security&quot;</tt> headers were sent by any of the servers) then no file will be created, not even an empty one. This behaviour applies to the default database file (<i>~/.wget-hsts</i>) as well: it will not be created until some server enforces an <font SIZE="-1">HSTS</font> policy. </p>
<p> Care is taken not to override possible changes made by other Wget processes at the same time over the <font SIZE="-1">HSTS</font> database. Before dumping the updated <font SIZE="-1">HSTS</font> entries on the file, Wget will re-read it and merge the changes. </p>
<p> Using a custom <font SIZE="-1">HSTS</font> database and/or modifying an existing one is discouraged. For more information about the potential security threats arose from such practice, see section 14 &#8220;Security Considerations&#8221; of <font SIZE="-1">RFC 6797,</font> specially section 14.9 &#8220;Creative Manipulation of <font SIZE="-1">HSTS</font> Policy Store&#8221;.</p>
<dt><code>&#8211;warc-file=</code><i>file</i></p>
<dd> Use <i>file</i> as the destination <font SIZE="-1">WARC</font> file.</p>
<dt><code>&#8211;warc-header=</code><i>string</i></p>
<dd> Use <i>string</i> into as the warcinfo record.</p>
<dt><code>&#8211;warc-max-size=</code><i>size</i></p>
<dd> Set the maximum size of the <font SIZE="-1">WARC</font> files to <i>size</i>.</p>
<dt><code>&#8211;warc-cdx</code></p>
<dd> Write <font SIZE="-1">CDX</font> index files.</p>
<dt><code>&#8211;warc-dedup=</code><i>file</i></p>
<dd> Do not store records listed in this <font SIZE="-1">CDX</font> file.</p>
<dt><code>&#8211;no-warc-compression</code></p>
<dd> Do not compress <font SIZE="-1">WARC</font> files with <font SIZE="-1">GZIP.</font></p>
<dt><code>&#8211;no-warc-digests</code></p>
<dd> Do not calculate <font SIZE="-1">SHA1</font> digests.</p>
<dt><code>&#8211;no-warc-keep-log</code></p>
<dd> Do not store the log file in a <font SIZE="-1">WARC</font> record.</p>
<dt><code>&#8211;warc-tempdir=</code><i>dir</i></p>
<dd> Specify the location for temporary files created by the <font SIZE="-1">WARC</font> writer.</dl>
<h3><font SIZE="-1">FTP</font> Options</h3>
<dl>
<dt><code>&#8211;ftp-user=</code><i>user</i></p>
<dd>
<dt><code>&#8211;ftp-password=</code><i>password</i></p>
<dd> Specify the username <i>user</i> and password <i>password</i> on an <font SIZE="-1">FTP</font> server. Without this, or the corresponding startup option, the password defaults to <code>-wget@</code>, normally used for anonymous <font SIZE="-1">FTP.</font> </p>
<p> Another way to specify username and password is in the <font SIZE="-1">URL</font> itself. Either method reveals your password to anyone who bothers to run <tt>&quot;ps&quot;</tt>. To prevent the passwords from being seen, store them in <i>.wgetrc</i> or <i>.netrc</i>, and make sure to protect those files from other users with <tt>&quot;chmod&quot;</tt>. If the passwords are really important, do not leave them lying in those files either&#8212;edit the files and delete them after Wget has started the download.</p>
<dt><code>&#8211;no-remove-listing</code></p>
<dd> Don&#8217;t remove the temporary <i>.listing</i> files generated by <font SIZE="-1">FTP</font> retrievals. Normally, these files contain the raw directory listings received from <font SIZE="-1">FTP</font> servers. Not removing them can be useful for debugging purposes, or when you want to be able to easily check on the contents of remote server directories (e.g. to verify that a mirror you&#8217;re running is complete). </p>
<p> Note that even though Wget writes to a known filename for this file, this is not a security hole in the scenario of a user making <i>.listing</i> a symbolic link to <i>/etc/passwd</i> or something and asking <tt>&quot;root&quot;</tt> to run Wget in his or her directory. Depending on the options used, either Wget will refuse to write to <i>.listing</i>, making the globbing/recursion/time-stamping operation fail, or the symbolic link will be deleted and replaced with the actual <i>.listing</i> file, or the listing will be written to a <i>.listing.number</i> file. </p>
<p> Even though this situation isn&#8217;t a problem, though, <tt>&quot;root&quot;</tt> should never run Wget in a non-trusted user&#8217;s directory. A user could do something as simple as linking <i>index.html</i> to <i>/etc/passwd</i> and asking <tt>&quot;root&quot;</tt> to run Wget with <code>-N</code> or <code>-r</code> so the file will be overwritten.</p>
<dt><code>&#8211;no-glob</code></p>
<dd> Turn off <font SIZE="-1">FTP</font> globbing. Globbing refers to the use of shell-like special characters (<i>wildcards</i>), like <code>*</code>, <code>?</code>, <code>[</code> and <code>]</code> to retrieve more than one file from the same directory at once, like: </p>
<pre>
        wget <a href="ftp://gnjilux.srk.fer.hr/*.msg">ftp://gnjilux.srk.fer.hr/*.msg</a>
</pre>
<p> By default, globbing will be turned on if the <font SIZE="-1">URL</font> contains a globbing character. This option may be used to turn globbing on or off permanently. </p>
<p> You may have to quote the <font SIZE="-1">URL</font> to protect it from being expanded by your shell. Globbing makes Wget look for a directory listing, which is system-specific. This is why it currently works only with Unix <font SIZE="-1">FTP</font> servers (and the ones emulating Unix <tt>&quot;ls&quot;</tt> output).</p>
<dt><code>&#8211;no-passive-ftp</code></p>
<dd> Disable the use of the <i>passive</i> <font SIZE="-1">FTP</font> transfer mode. Passive <font SIZE="-1">FTP</font> mandates that the client connect to the server to establish the data connection rather than the other way around. </p>
<p> If the machine is connected to the Internet directly, both passive and active <font SIZE="-1">FTP</font> should work equally well. Behind most firewall and <font SIZE="-1">NAT</font> configurations passive <font SIZE="-1">FTP</font> has a better chance of working. However, in some rare firewall configurations, active <font SIZE="-1">FTP</font> actually works when passive <font SIZE="-1">FTP</font> doesn&#8217;t. If you suspect this to be the case, use this option, or set <tt>&quot;passive_ftp=off&quot;</tt> in your init file.</p>
<dt><code>&#8211;preserve-permissions</code></p>
<dd> Preserve remote file permissions instead of permissions set by umask.</p>
<dt><code>&#8211;retr-symlinks</code></p>
<dd> By default, when retrieving <font SIZE="-1">FTP</font> directories recursively and a symbolic link is encountered, the symbolic link is traversed and the pointed-to files are retrieved. Currently, Wget does not traverse symbolic links to directories to download them recursively, though this feature may be added in the future. </p>
<p> When <code>&#8211;retr-symlinks=no</code> is specified, the linked-to file is not downloaded. Instead, a matching symbolic link is created on the local filesystem. The pointed-to file will not be retrieved unless this recursive retrieval would have encountered it separately and downloaded it anyway. This option poses a security risk where a malicious <font SIZE="-1">FTP</font> Server may cause Wget to write to files outside of the intended directories through a specially crafted .LISTING file. </p>
<p> Note that when retrieving a file (not a directory) because it was specified on the command-line, rather than because it was recursed to, this option has no effect. Symbolic links are always traversed in this case.</dl>
<h3><font SIZE="-1">FTPS</font> Options</h3>
<dl>
<dt><code>&#8211;ftps-implicit</code></p>
<dd> This option tells Wget to use <font SIZE="-1">FTPS</font> implicitly. Implicit <font SIZE="-1">FTPS</font> consists of initializing <font SIZE="-1">SSL/TLS</font> from the very beginning of the control connection. This option does not send an <tt>&quot;AUTH TLS&quot;</tt> command: it assumes the server speaks <font SIZE="-1">FTPS</font> and directly starts an <font SIZE="-1">SSL/TLS</font> connection. If the attempt is successful, the session continues just like regular <font SIZE="-1">FTPS</font> (<tt>&quot;PBSZ&quot;</tt> and <tt>&quot;PROT&quot;</tt> are sent, etc.). Implicit <font SIZE="-1">FTPS</font> is no longer a requirement for <font SIZE="-1">FTPS</font> implementations, and thus many servers may not support it. If <code>&#8211;ftps-implicit</code> is passed and no explicit port number specified, the default port for implicit <font SIZE="-1">FTPS, 990,</font> will be used, instead of the default port for the &#8220;normal&#8221; (explicit) <font SIZE="-1">FTPS</font> which is the same as that of <font SIZE="-1">FTP, 21.</font></p>
<dt><code>&#8211;no-ftps-resume-ssl</code></p>
<dd> Do not resume the <font SIZE="-1">SSL/TLS</font> session in the data channel. When starting a data connection, Wget tries to resume the <font SIZE="-1">SSL/TLS</font> session previously started in the control connection. <font SIZE="-1">SSL/TLS</font> session resumption avoids performing an entirely new handshake by reusing the <font SIZE="-1">SSL/TLS</font> parameters of a previous session. Typically, the <font SIZE="-1">FTPS</font> servers want it that way, so Wget does this by default. Under rare circumstances however, one might want to start an entirely new <font SIZE="-1">SSL/TLS</font> session in every data connection. This is what <code>&#8211;no-ftps-resume-ssl</code> is for.</p>
<dt><code>&#8211;ftps-clear-data-connection</code></p>
<dd> All the data connections will be in plain text. Only the control connection will be under <font SIZE="-1">SSL/TLS.</font> Wget will send a <tt>&quot;PROT C&quot;</tt> command to achieve this, which must be approved by the server.</p>
<dt><code>&#8211;ftps-fallback-to-ftp</code></p>
<dd> Fall back to <font SIZE="-1">FTP</font> if <font SIZE="-1">FTPS</font> is not supported by the target server. For security reasons, this option is not asserted by default. The default behaviour is to exit with an error. If a server does not successfully reply to the initial <tt>&quot;AUTH TLS&quot;</tt> command, or in the case of implicit <font SIZE="-1">FTPS,</font> if the initial <font SIZE="-1">SSL/TLS</font> connection attempt is rejected, it is considered that such server does not support <font SIZE="-1">FTPS.</font></dl>
<h3>Recursive Retrieval Options</h3>
<dl>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;recursive</code></p>
<dd> Turn on recursive retrieving. The default maximum depth is 5.</p>
<dt><code>-l</code> <i>depth</i></p>
<dd>
<dt><code>&#8211;level=</code><i>depth</i></p>
<dd> Set the maximum number of subdirectories that Wget will recurse into to <i>depth</i>. In order to prevent one from accidentally downloading very large websites when using recursion this is limited to a depth of 5 by default, i.e., it will traverse at most 5 directories deep starting from the provided <font SIZE="-1">URL.</font> Set <code>-l 0</code> or <code>-l inf</code> for infinite recursion depth. </p>
<pre>
        wget -r -l 0 http://&lt;site&gt;/1.html
</pre>
<p> Ideally, one would expect this to download just <i>1.html</i>. but unfortunately this is not the case, because <code>-l 0</code> is equivalent to <code>-l inf</code>&#8212;that is, infinite recursion. To download a single <font SIZE="-1">HTML</font> page (or a handful of them), specify them all on the command line and leave away <code>-r</code> and <code>-l</code>. To download the essential items to view a single <font SIZE="-1">HTML</font> page, see <code>page requisites</code>.</p>
<dt><code>&#8211;delete-after</code></p>
<dd> This option tells Wget to delete every single file it downloads, <i>after</i> having done so. It is useful for pre-fetching popular pages through a proxy, e.g.: </p>
<pre>
        wget -r -nd --delete-after <a rel="nofollow" href="http://whatever.com/~popular/page/">http://whatever.com/~popular/page/</a>
</pre>
<p> The <code>-r</code> option is to retrieve recursively, and <code>-nd</code> to not create directories. </p>
<p> Note that <code>&#8211;delete-after</code> deletes files on the local machine. It does not issue the <font SIZE="-1"><code>DELE</code></font> command to remote <font SIZE="-1">FTP</font> sites, for instance. Also note that when <code>&#8211;delete-after</code> is specified, <code>&#8211;convert-links</code> is ignored, so <code>.orig</code> files are simply not created in the first place.</p>
<dt><code>-k</code></p>
<dd>
<dt><code>&#8211;convert-links</code></p>
<dd> After the download is complete, convert the links in the document to make them suitable for local viewing. This affects not only the visible hyperlinks, but any part of the document that links to external content, such as embedded images, links to style sheets, hyperlinks to non-HTML content, etc. </p>
<p> Each link will be changed in one of the two ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The links to files that have been downloaded by Wget will be changed to refer to the file they point to as a relative link. </p>
<p> Example: if the downloaded file <i>/foo/doc.html</i> links to <i>/bar/img.gif</i>, also downloaded, then the link in <i>doc.html</i> will be modified to point to <code>../bar/img.gif</code>. This kind of transformation works reliably for arbitrary combinations of directories.</p>
<dt>&bull;</p>
<dd> The links to files that have not been downloaded by Wget will be changed to include host name and absolute path of the location they point to. </p>
<p> Example: if the downloaded file <i>/foo/doc.html</i> links to <i>/bar/img.gif</i> (or to <i>../bar/img.gif</i>), then the link in <i>doc.html</i> will be modified to point to <i><a rel="nofollow" href="http://hostname/bar/img.gif">http://hostname/bar/img.gif</a></i>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Because of this, local browsing works reliably: if a linked file was downloaded, the link will refer to its local name; if it was not downloaded, the link will refer to its full Internet address rather than presenting a broken link. The fact that the former links are converted to relative links ensures that you can move the downloaded hierarchy to another directory. </p>
<p> Note that only at the end of the download can Wget know which links have been downloaded. Because of that, the work done by <code>-k</code> will be performed at the end of all the downloads.</dl>
<dt><code>&#8211;convert-file-only</code></p>
<dd> This option converts only the filename part of the URLs, leaving the rest of the URLs untouched. This filename part is sometimes referred to as the &#8220;basename&#8221;, although we avoid that term here in order not to cause confusion. </p>
<p> It works particularly well in conjunction with <code>&#8211;adjust-extension</code>, although this coupling is not enforced. It proves useful to populate Internet caches with files downloaded from different hosts. </p>
<p> Example: if some link points to <i>//foo.com/bar.cgi?xyz</i> with <code>&#8211;adjust-extension</code> asserted and its local destination is intended to be <i>./foo.com/bar.cgi?xyz.css</i>, then the link would be converted to <i>//foo.com/bar.cgi?xyz.css</i>. Note that only the filename part has been modified. The rest of the <font SIZE="-1">URL</font> has been left untouched, including the net path (<tt>&quot;//&quot;</tt>) which would otherwise be processed by Wget and converted to the effective scheme (ie. <tt>&quot;http://&quot;</tt>).</p>
<dt><code>-K</code></p>
<dd>
<dt><code>&#8211;backup-converted</code></p>
<dd> When converting a file, back up the original version with a <code>.orig</code> suffix. Affects the behavior of <code>-N</code>.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;mirror</code></p>
<dd> Turn on options suitable for mirroring. This option turns on recursion and time-stamping, sets infinite recursion depth and keeps <font SIZE="-1">FTP</font> directory listings. It is currently equivalent to <code>-r -N -l inf &#8211;no-remove-listing</code>.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;page-requisites</code></p>
<dd> This option causes Wget to download all the files that are necessary to properly display a given <font SIZE="-1">HTML</font> page. This includes such things as inlined images, sounds, and referenced stylesheets. </p>
<p> Ordinarily, when downloading a single <font SIZE="-1">HTML</font> page, any requisite documents that may be needed to display it properly are not downloaded. Using <code>-r</code> together with <code>-l</code> can help, but since Wget does not ordinarily distinguish between external and inlined documents, one is generally left with &#8220;leaf documents&#8221; that are missing their requisites. </p>
<p> For instance, say document <i>1.html</i> contains an <tt>&quot;&lt;IMG&gt;&quot;</tt> tag referencing <i>1.gif</i> and an <tt>&quot;&lt;A&gt;&quot;</tt> tag pointing to external document <i>2.html</i>. Say that <i>2.html</i> is similar but that its image is <i>2.gif</i> and it links to <i>3.html</i>. Say this continues up to some arbitrarily high number. </p>
<p> If one executes the command: </p>
<pre>
        wget -r -l 2 http://&lt;site&gt;/1.html
</pre>
<p> then <i>1.html</i>, <i>1.gif</i>, <i>2.html</i>, <i>2.gif</i>, and <i>3.html</i> will be downloaded. As you can see, <i>3.html</i> is without its requisite <i>3.gif</i> because Wget is simply counting the number of hops (up to 2) away from <i>1.html</i> in order to determine where to stop the recursion. However, with this command: </p>
<pre>
        wget -r -l 2 -p http://&lt;site&gt;/1.html
</pre>
<p> all the above files <i>and</i> <i>3.html</i>&#8216;s requisite <i>3.gif</i> will be downloaded. Similarly, </p>
<pre>
        wget -r -l 1 -p http://&lt;site&gt;/1.html
</pre>
<p> will cause <i>1.html</i>, <i>1.gif</i>, <i>2.html</i>, and <i>2.gif</i> to be downloaded. One might think that: </p>
<pre>
        wget -r -l 0 -p http://&lt;site&gt;/1.html
</pre>
<p> would download just <i>1.html</i> and <i>1.gif</i>, but unfortunately this is not the case, because <code>-l 0</code> is equivalent to <code>-l inf</code>&#8212;that is, infinite recursion. To download a single <font SIZE="-1">HTML</font> page (or a handful of them, all specified on the command-line or in a <code>-i</code> <font SIZE="-1">URL</font> input file) and its (or their) requisites, simply leave off <code>-r</code> and <code>-l</code>: </p>
<pre>
        wget -p http://&lt;site&gt;/1.html
</pre>
<p> Note that Wget will behave as if <code>-r</code> had been specified, but only that single page and its requisites will be downloaded. Links from that page to external documents will not be followed. Actually, to download a single page and all its requisites (even if they exist on separate websites), and make sure the lot displays properly locally, this author likes to use a few options in addition to <code>-p</code>: </p>
<pre>
        wget -E -H -k -K -p http://&lt;site&gt;/&lt;document&gt;
</pre>
<p> To finish off this topic, it&#8217;s worth knowing that Wget&#8217;s idea of an external document link is any <font SIZE="-1">URL</font> specified in an <tt>&quot;&lt;A&gt;&quot;</tt> tag, an <tt>&quot;&lt;AREA&gt;&quot;</tt> tag, or a <tt>&quot;&lt;LINK&gt;&quot;</tt> tag other than <tt>&quot;&lt;LINK REL=&quot;stylesheet&quot;&gt;&quot;</tt>.</p>
<dt><code>&#8211;strict-comments</code></p>
<dd> Turn on strict parsing of <font SIZE="-1">HTML</font> comments. The default is to terminate comments at the first occurrence of <code>&#8211;&gt;</code>. </p>
<p> According to specifications, <font SIZE="-1">HTML</font> comments are expressed as <font SIZE="-1">SGML</font> <i>declarations</i>. Declaration is special markup that begins with <code>&lt;!</code> and ends with <code>&gt;</code>, such as <code>&lt;!DOCTYPE &#8230;&gt;</code>, that may contain comments between a pair of <code>&#8212;</code> delimiters. <font SIZE="-1">HTML</font> comments are &#8220;empty declarations&#8221;, <font SIZE="-1">SGML</font> declarations without any non-comment text. Therefore, <code>&lt;!&#8211;foo&#8211;&gt;</code> is a valid comment, and so is <code>&lt;!&#8211;one&#8212; &#8211;two&#8211;&gt;</code>, but <code>&lt;!&#8211;1&#8211;2&#8211;&gt;</code> is not. </p>
<p> On the other hand, most <font SIZE="-1">HTML</font> writers don&#8217;t perceive comments as anything other than text delimited with <code>&lt;!&#8211;</code> and <code>&#8211;&gt;</code>, which is not quite the same. For example, something like <code>&lt;!&#8212;&#8212;&#8212;&#8212;&gt;</code> works as a valid comment as long as the number of dashes is a multiple of four (!). If not, the comment technically lasts until the next <code>&#8212;</code>, which may be at the other end of the document. Because of this, many popular browsers completely ignore the specification and implement what users have come to expect: comments delimited with <code>&lt;!&#8211;</code> and <code>&#8211;&gt;</code>. </p>
<p> Until version 1.9, Wget interpreted comments strictly, which resulted in missing links in many web pages that displayed fine in browsers, but had the misfortune of containing non-compliant comments. Beginning with version 1.9, Wget has joined the ranks of clients that implements &#8220;naive&#8221; comments, terminating each comment at the first occurrence of <code>&#8211;&gt;</code>. </p>
<p> If, for whatever reason, you want strict comment parsing, use this option to turn it on.</dl>
<h3>Recursive Accept/Reject Options</h3>
<dl>
<dt><code>-A</code> <i>acclist</i> <code>&#8211;accept</code> <i>acclist</i></p>
<dd>
<dt><code>-R</code> <i>rejlist</i> <code>&#8211;reject</code> <i>rejlist</i></p>
<dd> Specify comma-separated lists of file name suffixes or patterns to accept or reject. Note that if any of the wildcard characters, <code>*</code>, <code>?</code>, <code>[</code> or <code>]</code>, appear in an element of <i>acclist</i> or <i>rejlist</i>, it will be treated as a pattern, rather than a suffix. In this case, you have to enclose the pattern into quotes to prevent your shell from expanding it, like in <code>-A &#8220;*.mp3&#8221;</code> or <code>-A &#8216;*.mp3&#8217;</code>.</p>
<dt><code>&#8211;accept-regex</code> <i>urlregex</i></p>
<dd>
<dt><code>&#8211;reject-regex</code> <i>urlregex</i></p>
<dd> Specify a regular expression to accept or reject the complete <font SIZE="-1">URL.</font></p>
<dt><code>&#8211;regex-type</code> <i>regextype</i></p>
<dd> Specify the regular expression type. Possible types are <code>posix</code> or <code>pcre</code>. Note that to be able to use <code>pcre</code> type, wget has to be compiled with libpcre support.</p>
<dt><code>-D</code> <i>domain-list</i></p>
<dd>
<dt><code>&#8211;domains=</code><i>domain-list</i></p>
<dd> Set domains to be followed. <i>domain-list</i> is a comma-separated list of domains. Note that it does <i>not</i> turn on <code>-H</code>.</p>
<dt><code>&#8211;exclude-domains</code> <i>domain-list</i></p>
<dd> Specify the domains that are <i>not</i> to be followed.</p>
<dt><code>&#8211;follow-ftp</code></p>
<dd> Follow <font SIZE="-1">FTP</font> links from <font SIZE="-1">HTML</font> documents. Without this option, Wget will ignore all the <font SIZE="-1">FTP</font> links.</p>
<dt><code>&#8211;follow-tags=</code><i>list</i></p>
<dd> Wget has an internal table of <font SIZE="-1">HTML</font> tag / attribute pairs that it considers when looking for linked documents during a recursive retrieval. If a user wants only a subset of those tags to be considered, however, he or she should be specify such tags in a comma-separated <i>list</i> with this option.</p>
<dt><code>&#8211;ignore-tags=</code><i>list</i></p>
<dd> This is the opposite of the <code>&#8211;follow-tags</code> option. To skip certain <font SIZE="-1">HTML</font> tags when recursively looking for documents to download, specify them in a comma-separated <i>list</i>. </p>
<p> In the past, this option was the best bet for downloading a single page and its requisites, using a command-line like: </p>
<pre>
        wget --ignore-tags=a,area -H -k -K -r http://&lt;site&gt;/&lt;document&gt;
</pre>
<p> However, the author of this option came across a page with tags like <tt>&quot;&lt;LINK REL=&quot;home&quot; href=&quot;/&quot;&gt;&quot;</tt> and came to the realization that specifying tags to ignore was not enough. One can&#8217;t just tell Wget to ignore <tt>&quot;&lt;LINK&gt;&quot;</tt>, because then stylesheets will not be downloaded. Now the best bet for downloading a single page and its requisites is the dedicated <code>&#8211;page-requisites</code> option.</p>
<dt><code>&#8211;ignore-case</code></p>
<dd> Ignore case when matching files and directories. This influences the behavior of -R, -A, -I, and -X options, as well as globbing implemented when downloading from <font SIZE="-1">FTP</font> sites. For example, with this option, <code>-A &#8220;*.txt&#8221;</code> will match <code>file1.txt</code>, but also <code>file2.TXT</code>, <code>file3.TxT</code>, and so on. The quotes in the example are to prevent the shell from expanding the pattern.</p>
<dt><code>-H</code></p>
<dd>
<dt><code>&#8211;span-hosts</code></p>
<dd> Enable spanning across hosts when doing recursive retrieving.</p>
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;relative</code></p>
<dd> Follow relative links only. Useful for retrieving a specific home page without any distractions, not even those from the same hosts.</p>
<dt><code>-I</code> <i>list</i></p>
<dd>
<dt><code>&#8211;include-directories=</code><i>list</i></p>
<dd> Specify a comma-separated list of directories you wish to follow when downloading. Elements of <i>list</i> may contain wildcards.</p>
<dt><code>-X</code> <i>list</i></p>
<dd>
<dt><code>&#8211;exclude-directories=</code><i>list</i></p>
<dd> Specify a comma-separated list of directories you wish to exclude from download. Elements of <i>list</i> may contain wildcards.</p>
<dt><code>-np</code></p>
<dd>
<dt><code>&#8211;no-parent</code></p>
<dd> Do not ever ascend to the parent directory when retrieving recursively. This is a useful option, since it guarantees that only the files <i>below</i> a certain hierarchy will be downloaded.</dl>
<h2>ENVIRONMENT</h2>
<p> Wget supports proxies for both <font SIZE="-1">HTTP</font> and <font SIZE="-1">FTP</font> retrievals. The standard way to specify proxy location, which Wget recognizes, is using the following environment variables:</p>
<dl>
<dt><code>http_proxy</code></p>
<dd>
<dt><code>https_proxy</code></p>
<dd> If set, the <code>http_proxy</code> and <code>https_proxy</code> variables should contain the URLs of the proxies for <font SIZE="-1">HTTP</font> and <font SIZE="-1">HTTPS</font> connections respectively.</p>
<dt><code>ftp_proxy</code></p>
<dd> This variable should contain the <font SIZE="-1">URL</font> of the proxy for <font SIZE="-1">FTP</font> connections. It is quite common that <code>http_proxy</code> and <code>ftp_proxy</code> are set to the same <font SIZE="-1">URL.</font></p>
<dt><code>no_proxy</code></p>
<dd> This variable should contain a comma-separated list of domain extensions proxy should <i>not</i> be used for. For instance, if the value of <code>no_proxy</code> is <code>.mit.edu</code>, proxy will not be used to retrieve documents from <font SIZE="-1">MIT.</font></dl>
<h2>EXIT STATUS</h2>
<p> Wget may return one of several error codes if it encounters problems.</p>
<dl>
<dt>0</p>
<dd> No problems occurred.</p>
<dt>1</p>
<dd> Generic error code.</p>
<dt>2</p>
<dd> Parse error&#8212;for instance, when parsing command-line options, the <code>.wgetrc</code> or <code>.netrc</code>&#8230;</p>
<dt>3</p>
<dd> File I/O error.</p>
<dt>4</p>
<dd> Network failure.</p>
<dt>5</p>
<dd> <font SIZE="-1">SSL</font> verification failure.</p>
<dt>6</p>
<dd> Username/password authentication failure.</p>
<dt>7</p>
<dd> Protocol errors.</p>
<dt>8</p>
<dd> Server issued an error response.</dl>
<p> With the exceptions of 0 and 1, the lower-numbered exit codes take precedence over higher-numbered ones, when multiple types of errors are encountered. </p>
<p> In versions of Wget prior to 1.12, Wget&#8217;s exit status tended to be unhelpful and inconsistent. Recursive downloads would virtually always return 0 (success), regardless of any issues encountered, and non-recursive fetches only returned the status corresponding to the most recently-attempted download.</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/wgetrc</code></p>
<dd> Default location of the <i>global</i> startup file.</p>
<dt><code>.wgetrc</code></p>
<dd> User startup file.</dl>
<h2>BUGS</h2>
<p> You are welcome to submit bug reports via the <font SIZE="-1">GNU</font> Wget bug tracker (see &lt;<code><a rel="nofollow" href="https://savannah.gnu.org/bugs/?func=additem">https://savannah.gnu.org/bugs/?func=additem</a>&amp;group=wget</code>&gt;) or to our mailing list &lt;<code>bug-wget [at] gnu.org</code>&gt;. </p>
<p> Visit &lt;<code><a rel="nofollow" href="https://lists.gnu.org/mailman/listinfo/bug-wget">https://lists.gnu.org/mailman/listinfo/bug-wget</a></code>&gt; to get more info (how to subscribe, list archives, &#8230;). </p>
<p> Before actually submitting a bug report, please try to follow a few simple guidelines.</p>
<dl>
<dt>1.</p>
<dd> Please try to ascertain that the behavior you see really is a bug. If Wget crashes, it&#8217;s a bug. If Wget does not behave as documented, it&#8217;s a bug. If things work strange, but you are not sure about the way they are supposed to work, it might well be a bug, but you might want to double-check the documentation and the mailing lists.</p>
<dt>2.</p>
<dd> Try to repeat the bug in as simple circumstances as possible. E.g. if Wget crashes while downloading <code>wget -rl0 -kKE -t5 &#8211;no-proxy <a rel="nofollow" href="http://example.com">http://example.com</a> -o /tmp/log</code>, you should try to see if the crash is repeatable, and if will occur with a simpler set of options. You might even try to start the download at the page where the crash occurred to see if that page somehow triggered the crash. </p>
<p> Also, while I will probably be interested to know the contents of your <i>.wgetrc</i> file, just dumping it into the debug message is probably a bad idea. Instead, you should first try to see if the bug repeats with <i>.wgetrc</i> moved out of the way. Only if it turns out that <i>.wgetrc</i> settings affect the bug, mail me the relevant parts of the file.</p>
<dt>3.</p>
<dd> Please start Wget with <code>-d</code> option and send us the resulting output (or relevant parts thereof). If Wget was compiled without debug support, recompile it&#8212;it is <i>much</i> easier to trace bugs with debug support on. </p>
<p> Note: please make sure to remove any potentially sensitive information from the debug log before sending it to the bug address. The <tt>&quot;-d&quot;</tt> won&#8217;t go out of its way to collect sensitive information, but the log <i>will</i> contain a fairly complete transcript of Wget&#8217;s communication with the server, which may include passwords and pieces of downloaded data. Since the bug address is publicly archived, you may assume that all bug reports are visible to the public.</p>
<dt>4.</p>
<dd> If Wget has crashed, try to run it in a debugger, e.g. <tt>&quot;gdb `which wget` core&quot;</tt> and type <tt>&quot;where&quot;</tt> to get the backtrace. This may not work if the system administrator has disabled core files, but it is safe to try.</dl>
<h2>SEE ALSO</h2>
<p> This is <code>not</code> the complete manual for <font SIZE="-1">GNU</font> Wget. For more complete information, including more detailed explanations of some of the options, and a number of commands available for use with <i>.wgetrc</i> files and the <code>-e</code> option, see the <font SIZE="-1">GNU</font> Info entry for <i>wget</i>. </p>
<p> Also see <code><a href="/docs/linux/man/1-wget2/">wget2</a></code>(1), the updated version of <font SIZE="-1">GNU</font> Wget with even better support for recursive downloading and modern protocols like <font SIZE="-1">HTTP/2.</font></p>
<h2>AUTHOR</h2>
<p> Originally written by Hrvoje Nikšić &lt;hniksic [at] xemacs.org&gt;. Currently maintained by Darshit Shah &lt;darnir [at] gnu.org&gt; and Tim Rühsen &lt;tim.ruehsen [at] gmx.de&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1996&#8211;2011, 2015, 2018&#8211;2021 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAR">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAS">FILES</a></p>
<dd>
<dt><a href="#lbAT">BUGS</a></p>
<dd>
<dt><a href="#lbAU">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAV">AUTHOR</a></p>
<dd>
<dt><a href="#lbAW">COPYRIGHT</a></p>
<dd></dl>
