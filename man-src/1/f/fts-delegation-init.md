---
title: "fts-delegation-init(1)"
name: "fts-delegation-init"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-delegation-init/"
---

<h2>NAME</h2>

 fts-delegation-init

<h2>SYNOPSIS</h2>

 fts-delegation-init [options]

<h2>DESCRIPTION</h2>

 fts-delegation-init is a tool for delegating a proxy certificate to FTS3 endpoint.

<h2>OPTIONS</h2>

 
&nbsp;<wbr>&nbsp;<wbr>-h&nbsp;<wbr>[&nbsp;<wbr>--help&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print this help text and exit. 
&nbsp;<wbr>&nbsp;<wbr>-q&nbsp;<wbr>[&nbsp;<wbr>--quite&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Quiet operation. 
&nbsp;<wbr>&nbsp;<wbr>-v&nbsp;<wbr>[&nbsp;<wbr>--verbose&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Be more verbose. 
&nbsp;<wbr>&nbsp;<wbr>-s&nbsp;<wbr>[&nbsp;<wbr>--service&nbsp;<wbr>]&nbsp;<wbr>arg&nbsp;<wbr>&nbsp;<wbr>Use the transfer service at the specified URL. 
&nbsp;<wbr>&nbsp;<wbr>-V&nbsp;<wbr>[&nbsp;<wbr>--version&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print the version number and exit. 
&nbsp;<wbr>&nbsp;<wbr>-j&nbsp;<wbr>[&nbsp;<wbr>--json&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The output should be printed in JSON format 

 
&nbsp;<wbr>&nbsp;<wbr>--rest&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the RESTful interface. 
&nbsp;<wbr>&nbsp;<wbr>--capath arg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Path to the GRID security certificates&nbsp;<wbr>(e.g.&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/etc/grid-security/certificates). 
&nbsp;<wbr>&nbsp;<wbr>--proxy arg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Path to the proxy certificate&nbsp;<wbr>(e.g.&nbsp;<wbr>/tmp/x509up_u500). 
&nbsp;<wbr>&nbsp;<wbr>-I&nbsp;<wbr>[&nbsp;<wbr>--id&nbsp;<wbr>]&nbsp;<wbr>arg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Delegation with ID as the delegation identifier. 
&nbsp;<wbr>&nbsp;<wbr>-e&nbsp;<wbr>[&nbsp;<wbr>--expire&nbsp;<wbr>]&nbsp;<wbr>arg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Expiration time of the delegation in minutes. 

<h2>SEE ALSO</h2>

 <a rel="nofollow" HREF="http://fts3-service.web.cern.ch/">http://fts3-service.web.cern.ch/</a> 

<h2>Index</h2>


