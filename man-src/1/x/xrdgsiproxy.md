---
title: "xrdgsiproxy(1)"
name: "xrdgsiproxy"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrdgsiproxy/"
description: "xrdgsiproxy – generate a proxy X.509 certificate"
---

<h2>NAME</h2>
<p> xrdgsiproxy &#8211; generate a proxy X.509 certificate</p>
<h2>SYNOPSIS</h2>
<pre><code>
xrdgsiproxy[-h][mode][-debug][-f[-out] file]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>xrdgsiproxy</code> utility displays, creates, and destroys X.509 user proxy certificates used by the grid security infrastructure (<code>gsi</code>) security protocol.</p>
<h2>OPERANDS</h2>
<p> <i>mode</i></p>
<dl>
<dt>
<dd> <code>init</code> create proxy certificate and related proxy file<br />
 <code>info</code> display content of existing proxy file<br />
 <code>destroy</code> delete existing proxy file</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code> display help</p>
<dl>
<dt><code>-f</code> [<code>-out</code>] <i>file</i></p>
<dd> Non-standard location of proxy file</p>
<dt><code>init</code><i>&nbsp;<wbr></i><code>mode</code><i>&nbsp;<wbr></i><code>only:</code></p>
<dd>
<dt><code>-certdir</code> <i>dir</i></p>
<dd> Non-standard location of directory with information about known CAs</p>
<dt><code>-cert</code> <i>file</i></p>
<dd> Non-standard location of certificate for which proxies are wanted</p>
<dt><code>-key</code> <i>file</i></p>
<dd> Non-standard location of private key to be used to sign the proxy</p>
<dt><code>-bits</code> <i>n</i></p>
<dd> Strength in bits of the key [default 512]</p>
<dt><code>-valid</code> <i>hh:mm</i></p>
<dd> Time validity of the proxy certificate [default 12:00]</p>
<dt><code>-path-length</code> <i>len</i></p>
<dd> Max number of descendent levels below this proxy [default 0]</dl>
<h2>NOTES</h2>
<p> Complete HTML documentation can be found at <center> <a rel="nofollow" href="http://xrootd.org/doc/prod/sec_config.htm">http://xrootd.org/doc/prod/sec_config.htm</a><br />
 </center><br />
 Documentation for all components associated with <code>xrdgsiproxy</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>DIAGNOSTICS</h2>
<p> Errors yield an error message and a non-zero exit status.</p>
<h2>LICENSE</h2>
<p> License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>SUPPORT LEVEL</h2>
<p> The <code>xrdgsiproxy</code> command is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center> </p>
<h2>Index</h2>
