---
title: "url_handler-sh(1)"
name: "url_handler-sh"
section: "1"
letter: "u"
url: "/docs/linux/man/1-url_handler-sh/"
description: "urlview – URL extractor/launcher"
---

<p>urlview &#8211; URL extractor/launcher</p>
<h2>Synopsis</h2>
<p><code>urlview </code> <i>filename</i> [ <i>filename</i> &#8230; ]</p>
<h2>Description</h2>
<p><code>urlview</code> is a screen oriented program for extracting URLs from text files and displaying a menu from which you may launch a command to view a specific item.</p>
<h2>Configuration</h2>
<p><code>urlview</code> attempts to read <i>~/.urlview</i> upon startup. If this file doesn&#8217;t exist, it will try to read a system wide file in <i>/etc/urlview.conf</i>. There are two configuration commands (order does not matter):</p>
<dl COMPACT>
<dt>REGEXP <i>regexp</i></p>
<dd><code>urlview</code> uses a regular expression to extract URLs from the specified text files. , 	, 
 and  are all converted to their normal <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) meanings. The default REGEXP is:</dl>
<pre>(((http|https|ftp|gopher)|mailto):(//)?[^ &lt;&gt;&quot;	]*|(www|ftp)[0-9]?\.[-a-z0-9.]+)[^ .,;	
&lt;&quot;&gt;\):]?[^, &lt;&gt;&quot;	]*[^ .,;	
&lt;&quot;&gt;\):]</pre>
<dl COMPACT>
<dt>COMMAND <i>command</i></p>
<dd>If the specified command contains a <code>%s</code>, it will be subsituted with the URL that was requested, otherwise the URL is appended to the COMMAND string. The default COMMAND is: </p>
<p> /usr/bin/url_handler.sh</dl>
<p> <code>Note:</code> You should <i>never</i> put single quotes around the <code>%s</code>. <code>urlview</code> does this for you, and also makes sure that single quotes eventually showing up inside the URL are handled properly. (Note that this shouldn&#8217;t happen with the default regular expression, which explicitly excludes single quotes.)</p>
<dl COMPACT>
<dt>WRAP <i>choice</i></p>
<dd>Enable or disable URL wrapping. Valid values for <i>choice</i> are: yes, no (case insensitive). If this option is not supplied, the default behaviour is to disable wrapping.</dl>
<h2>Files</h2>
<dl COMPACT>
<dt>/etc/urlview.conf</p>
<dd>system-wide urlview configuration file</p>
<dt>~/.urlview</p>
<dd>urlview configuration file</dl>
<h2>Environment</h2>
<p>If the environment variable BROWSER is set to a browser command, or a colon-delimited list of commands to try, then the specified browser is used. %s is replaced with the quoted url to view. If %s is not part of a command, the url is appended to the command. </p>
<p> The BROWSER environment variable is honored only if the rc-file doesn&#8217;t contain the COMMAND option. The rc-file provided by the Debian package contains a COMMAND option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>Author</h2>
<p>Michael Elkins &lt;me [at] sigpipe.org&gt; </p>
<p> Modified for Debian by Luis Francisco Gonzalez &lt;luisgh [at] debian.org&gt; and Emanuele Rocca &lt;ema [at] debian.org&gt;. </p>
<p> Modified for SuSE by Dr. Werner Fink &lt;werner [at] suse.de&gt; and Stepan Kasal &lt;kasal [at] suse.cz&gt;. </p>
<p> Changes put together by Thomas Roessler &lt;roessler [at] does-not-exist.org&gt;.</p>
