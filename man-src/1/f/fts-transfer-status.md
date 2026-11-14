---
title: "fts-transfer-status(1)"
name: "fts-transfer-status"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-transfer-status/"
---

<h2>NAME</h2>

 fts-transfer-status

<h2>SYNOPSIS</h2>

 fts-transfer-status [options] JOBID [JOBID...]

<h2>DESCRIPTION</h2>

 fts-transfer-status is a tool for checking transfer-job status. The has to provide the transfer-job ID.

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
&nbsp;<wbr>&nbsp;<wbr>-l&nbsp;<wbr>[&nbsp;<wbr>--list&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>List status for all files. 
&nbsp;<wbr>&nbsp;<wbr>-a&nbsp;<wbr>[&nbsp;<wbr>--archive&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Query the archive. 
&nbsp;<wbr>&nbsp;<wbr>-d&nbsp;<wbr>[&nbsp;<wbr>--detailed&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Retrieve details&nbsp;<wbr>(i.e. transfer retries) 
&nbsp;<wbr>&nbsp;<wbr>-F&nbsp;<wbr>[&nbsp;<wbr>--dump-failed&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>Dump failed transfers into a file that can be used as&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>input for submission

<h2>SEE ALSO</h2>

 <a rel="nofollow" HREF="http://fts3-service.web.cern.ch/">http://fts3-service.web.cern.ch/</a> 

<h2>Index</h2>


