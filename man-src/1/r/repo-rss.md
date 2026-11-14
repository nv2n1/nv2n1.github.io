---
title: "repo-rss(1)"
name: "repo-rss"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repo-rss/"
description: "repo-rss – generates an RSS feed from one or more Yum repositories"
---

<h2>NAME</h2>
<p> repo-rss &#8211; generates an RSS feed from one or more Yum repositories</p>
<h2>SYNOPSIS</h2>
<p> <code>repo-rss</code> [options] repoid1 [repoid2&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>repo-rss</code> is a program for generating RSS feeds for one or more Yum repositories. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Help; display a help message and then quit.</p>
<dt><code>-f &lt;file&gt;</code></p>
<dd> Specify the file to which the RSS will be written. Default is repo-rss.xml.</p>
<dt><code>-l &lt;link&gt;</code></p>
<dd> Specify the URL to the RSS feed. Default is <a rel="nofollow" href="http://yum.baseurl.org/.">http://yum.baseurl.org/.</a></p>
<dt><code>-t &lt;title&gt;</code></p>
<dd> Specify the title for the RSS feed. Default is &quot;RSS Repository &#8211; Recent Packages&quot;.</p>
<dt><code>-d &lt;description&gt;</code></p>
<dd> Specify the description of the RSS feed. Default is &quot;Most recent packages in Repositories&quot;.</p>
<dt><code>-r &lt;days&gt;</code></p>
<dd> Specify the number of days to consider most recent. Default is 3.</p>
<dt><code>&#8211;tempcache</code></p>
<dd> Enable the use of a temporary directory for the yum cache. This is enabled by default for non-root users. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Generate an RSS for the updates-released repository and save it as updates-release.xml:</p>
<dd> <code>repo-rss -f updates-released.xml updates-released</code></dl>
<h2>FILES</h2>
<p> As repo-rss uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/
</pre>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>BUGS</h2>
<p> There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>Index</h2>
