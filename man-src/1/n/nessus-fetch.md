---
title: "nessus-fetch(1)"
name: "nessus-fetch"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nessus-fetch/"
description: "nessus-fetch – A simple utility to retrieve plugins from www.nessus.org"
---

<h2>NAME</h2>
<p> nessus-fetch &#8211; A simple utility to retrieve plugins from <a rel="nofollow" href="http://www.nessus.org">www.nessus.org</a></p>
<h2>SYNOPSIS</h2>
<p> <code>nessus-fetch &#8211;plugins </code> <code>nessus-fetch &#8211;plugins-md5</code> <code>nessus-fetch &#8211;register &lt;code&gt; </code> <code>nessus-fetch &#8211;check</code> <code>nessus-fetch &#8211;url &lt;url&gt; &lt;localfile&gt; [&lt;http_login&gt; &lt;http_password&gt;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>nessus-fetch</code> is a simple utility is used by <code>nessus-update-plugins</code> to fetch the newest Nessus plugins from <a rel="nofollow" href="http://www.nessus.org">www.nessus.org</a> and to register a Nessus installation with plugins.nessus.org. It can also be used to retrieve arbitrary files from third party servers. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;register &lt;code&gt; </code></p>
<dd> Register the current Nessus installation to <a rel="nofollow" href="http://plugins.nessus.org.">http://plugins.nessus.org.</a> Registering entitles you to receive a complete feed of the newest Nessus plugins. To register, an <code>activation code</code> is required. Please see <a rel="nofollow" href="http://plugins.nessus.org">http://plugins.nessus.org</a> for more details on how to get such a code. </p>
<dt><code>&#8211;check </code></p>
<dd> Makes sure that nessus-fetch is properly configured to receive a direct plugin feed from plugins.nessus.org by attempting to login into the remote server with the username and password obtained with nessus-fetch &#8211;register. Please see <a rel="nofollow" href="http://plugins.nessus.org">http://plugins.nessus.org</a> for more details on how to get a direct plugin feed. </p>
<dt><code>&#8211;plugins-md5</code></p>
<dd> Obtains the MD5 of the remote plugin archive. Depending if the user registered or not, the file will be fetched from <a rel="nofollow" href="http://www.nessus.org">www.nessus.org</a> or plugins.nessus.org. A file named &#8216;all-2.0.tar.gz.md5&#8217; will be created in the current working directory. </p>
<dt><code>&#8211;plugins</code></p>
<dd> Obtains the newest Nessus plugins from <a rel="nofollow" href="http://www.nessus.org">www.nessus.org</a> or plugins.nessus.org, as well as their signature file. The files &#8216;all-2.0.tar.gz&#8217; and &#8216;all-2.0.tar.gz.sig&#8217; will be created in the current working directory. </p>
<dt><code>&#8211;url &lt;url&gt; &lt;localfile&gt; [&lt;http_login&gt; &lt;http_password&gt;]</code></p>
<dd> Retrieves the file located at &lt;url&gt; (ie: <a rel="nofollow" href="http://www.nessus.org/index.html)">http://www.nessus.org/index.html)</a> and stores in in &lt;localfile&gt;. An optional http login and passwords can be provided if the remote server requires Basic authentication. </p>
</dl>
<h2>PROXY SUPPORT</h2>
<p> If you need to connect to the internet through a proxy, nessus-fetch can be configured to use one. Simply edit the file <code>nessus-fetch.rc</code> and add the following lines, changing the appropriate values where necessary : proxy=192.168.0.1 proxy_port=3128 proxy_username=renaud proxy_password=s3cr3t </p>
<h2>BUGS</h2>
<p> nessus-fetch will not retrieve files bigger than 40MB. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nessus-update-plugins/">nessus-update-plugins</a></code>(1) </p>
<h2>MORE INFORMATION ABOUT THE NESSUS PROJECT</h2>
<p> The canonical place where you will find more information about the Nessus project is : </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.nessus.org/">http://www.nessus.org/</a> </p>
</dl>
<h2>AUTHORS</h2>
<p> nessus-fetch is (C) 2004 Tenable Network Security </p>
<h2>Index</h2>
