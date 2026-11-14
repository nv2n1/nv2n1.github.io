---
title: "findproxyfile(1)"
name: "findproxyfile"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findproxyfile/"
description: "findproxyfile – returns full path to GSI Proxy file"
---

<h2>NAME</h2>
<p> <code>findproxyfile</code> &#8211; returns full path to GSI Proxy file</p>
<h2>SYNOPSIS</h2>
<p> <code>findproxyfile </code> [&#8211;proxycache=PATH] [&#8211;delegation-id=ID] [&#8211;user-dn=DN] [&#8211;outsidecache]</p>
<h2>DESCRIPTION</h2>
<p> <code>findproxyfile</code> returns full path to a GSI Proxy file, either in the proxy cache maintained by the GridSite G-HTTPS and delegation portType functions, or in other standard places. </p>
<p> If a User DN is given <code>findproxyfile </code> uses the value of the <code>&#8211;proxycache</code> argument, the GRST_PROXY_PATH or the compile time default to determine the location of the proxy cache directory. The directory is searched for a proxy having the given User DN and Delegation ID. (If no Delegation ID is specificed, then the default value is used.) </p>
<p> If <code>findproxyfile</code> does not find a proxy or if a User DN is not given, but <code>&#8211;outsidecache</code> was given, then the environment variable X509_USER_PROXY and the standard location /tmp/x509up_uUID are searched as well. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;proxycache=PATH</p>
<dd> Give the path of the proxy cache directory explicitly, overriding the default and the GRST_PROXY_PATH environment variable if present. </p>
<dt>&#8211;delegation-id=ID</p>
<dd> The optional delegation ID is search for in the proxy cache in addition to the User DN. If absent, the default Delegation ID value is searched for. </p>
<dt>&#8211;user-dn=DN</p>
<dd> The DN of the full user certificate associated with the proxy to be searched for in the proxy cache. (This is not the DN of any proxy earlier in the chain: it is a the DN of a certificate issued by a recognised CA.) </p>
<dt>&#8211;outsidecache</p>
<dd> If a User DN is not given, or a proxy not found in the cache, then search for a proxy using X509_USER_PROXY environment variable and file name of form /tmp/x509up_uUID as well. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> If a proxy is found, its full path is output on standard out. </p>
<h2>EXIT CODES</h2>
<p> 0 is returned on succcess. Non-zero otherwise. </p>
<h2>BUGS</h2>
<p> In this version, no attempt is made to verify or validate the proxies. </p>
<h2>AUTHOR</h2>
<p> Andrew McNab &lt;Andrew.McNab [at] man.ac.uk&gt; </p>
<p> findproxyfile is part of GridSite: <a rel="nofollow" href="http://www.gridsite.org/">http://www.gridsite.org/</a> </p>
<h2>Index</h2>
