---
title: "man2html(1)"
name: "man2html"
section: "1"
letter: "m"
url: "/docs/linux/man/1-man2html/"
description: "man2html – format a manual page in html"
---

<h2 class="name">NAME</h2>
<p> man2html &#8211; format a manual page in html </p>
<h2>SYNOPSIS</h2>
<p> man2html [options] [file]</p>
<h2>DESCRIPTION</h2>
<p> <code>man2html</code> converts a manual page as found in <i>file</i> (or stdin, in case no file argument, or the argument &quot;-&quot;, is given) from man-style nroff into html, and prints the result on stdout. It does support tbl but does not know about eqn. The exit status is 0. If something goes wrong, an error page is printed on stdout. </p>
<p> This can be used as a stand-alone utility, but is mainly intended as an auxiliary, to enable users to browse their man pages using a html browser like <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-xmosaic/">xmosaic</a></code>(1) or <code><a href="/docs/linux/man/1-netscape/">netscape</a></code>(1). </p>
<p> The main part of <code>man2html</code> is the troff-to-html engine written by Richard Verhoeven (rcb5 [at] win.tue.nl). It adds hyperlinks for the following constructs: </p>
<table>
<tr VALIGN=top>
<td><a href="//www.systutorials.com/docs/linux/man/3x-foo/">foo</a>(3x)</td>
<td>&quot;<a rel="nofollow" href="http://localhost/cgi-bin/man/man2html?3x+foo">http://localhost/cgi-bin/man/man2html?3x+foo</a>&quot;
</td>
</tr>
<tr VALIGN=top>
<td><a href="method://string">method://string</a></td>
<td>&quot;<a href="method://string">method://string</a>&quot;
</td>
</tr>
<tr VALIGN=top>
<td><a rel="nofollow" href="http://www.host.name">www.host.name</a></td>
<td>&quot;<a rel="nofollow" href="http://www.host.name">http://www.host.name</a>&quot;
</td>
</tr>
<tr VALIGN=top>
<td><a href="ftp://ftp.host.name">ftp.host.name</a></td>
<td>&quot;<a href="ftp://ftp.host.name">ftp://ftp.host.name</a>&quot;
</td>
</tr>
<tr VALIGN=top>
<td>name [at] host</td>
<td>&quot;mailto:name [at] host&quot;
</td>
</tr>
<tr VALIGN=top>
<td>&lt;string.h&gt;</td>
<td>&quot;file:/usr/include/string.h&quot;
</td>
</tr>
</table>
<p> (The first of these can be tuned by options &#8211; see below.) No lookup is done &#8211; the links generated need not exist. Also an index with internal hyperlinks to the various sections is generated, so that it is easier to find one&#8217;s way in large man pages like <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1). </p>
<h2>OPTIONS</h2>
<p> When reading from stdin, it is not always clear how to do .so expansion. The -D option allows a script to define the working directory. </p>
<dl>
<dt><code>-D pathname</code></p>
<dd> Strip the last two parts from the pathname, and do a <i>chdir</i>(<i>dir</i>) before starting the conversion.</dl>
<p> The -E option allows the easy generation of error messages from a cgi script. </p>
<dl>
<dt><code>-E string</code></p>
<dd> Output an error page containing the given error message.</dl>
<p> The general form of a hyperlink generated for a man page reference is</p>
<dl>
<dt>
<dd> &lt;method:cgipath&gt;&lt;man2htmlpath&gt;&lt;separator&gt;&lt;manpage&gt;</dl>
<p> with a default as shown above. The parts of this hyperlink are set using the various options.</p>
<dl>
<dt><code>-h</code></p>
<dd> Set method:cgipath to <a rel="nofollow" href="http://localhost.">http://localhost.</a></p>
<dt><code>-H</code><i> host[.domain][:port]</i></p>
<dd> Set method:cgipath to http://<i>host.domain:port</i>.</p>
<dt><code>-l</code></p>
<dd> Set method:cgipath to lynxcgi:<i>/usr/lib</i>.</p>
<dt><code>-L</code><i> dir</i></p>
<dd> Set method:cgipath to lynxcgi:<i>dir</i>.</p>
<dt><code>-M</code><i> man2htmlpath</i></p>
<dd> Set the man2htmlpath to use. The default is <i>/cgi-bin/man/man2html</i>.</p>
<dt><code>-p</code></p>
<dd> Set separator to &#8216;/&#8217;.</p>
<dt><code>-q</code></p>
<dd> Set separator to &#8216;?&#8217;. This is the default.</p>
<dt><code>-r</code></p>
<dd> Use relative html paths, instead of cgi-bin paths.</dl>
<p> On a machine without running <code>httpd</code>, one can use <code>lynx</code> to browse the man pages, using the lynxcgi method. When some http daemon is running, lynx, or any other browser, can be used to browse the man pages, using the http method. The option -l (for `lynxcgi&#8217;) selects the former behaviour. With it, the default cgipath is <i>/usr/lib</i>. </p>
<p> In general, a cgi script can be called by</p>
<dl>
<dt>
<dd> &lt;path_to_script&gt;/&lt;more_path&gt;?&lt;query&gt;</dl>
<p> and the environment variables PATH_INFO and QUERY_STRING will be set to &lt;more_path&gt; and &lt;query&gt;, respectively. Since lynxcgi does not handle the PATH_INFO part, we generate hyperlinks with `?&#8217; as a separator by default. The option -p (for `path&#8217;) selects &#8216;/&#8217; as a separator, while the option -q (for `query&#8217;) selects &#8216;?&#8217; as a separator. </p>
<p> The option -H <i>host</i> will specify the host to use (instead of <i>localhost</i>). A cgi script could use</p>
<dl>
<dt>
<dd> man2html -H $SERVER_NAME</dl>
<p> if the variable SERVER_NAME is set. This would allow your machine to act as a server and export man pages. </p>
<h2>BUGS</h2>
<p> There are many heuristics. The output will not always be perfect. The lynxcgi method will not work if lynx was compiled without selecting support for it. There may be problems with security. </p>
<h2>AUTHOR</h2>
<p> Richard Verhoeven was the original author of <code>man2html</code>. Michael Hamilton and Andries Brouwer subsequently improved on it. Federico Lucifredi &lt;flucifredi [at] acm.org&gt; is the current maintainer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-hman/">hman</a></code>(1) </p>
<h2>Index</h2>
