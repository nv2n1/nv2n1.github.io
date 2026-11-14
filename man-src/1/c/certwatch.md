---
title: "certwatch(1)"
name: "certwatch"
section: "1"
letter: "c"
url: "/docs/linux/man/1-certwatch/"
description: "certwatch – generate SSL certificate expiry warnings"
---

<h2 class="name">NAME</h2>
<p> certwatch &#8211; generate SSL certificate expiry warnings </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>certwatch</code> [OPTION&#8230;] <i>filename</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>certwatch</code> program is used to issue warning mail when an SSL certificate is about to expire. </p>
<p> The program has two modes of operation: normal mode and quiet mode. In normal mode, the certificate given by the <i>filename</i> argument is examined, and a warning email is issued to standard output if the certificate is outside its validity period, or approaching expiry. If the certificate cannot be found, or any errors occur whilst parsing the certificate, the certificate is ignored and no output is produced. In quiet mode, no output is given, but the exit status can still be used. </p>
<p> The certificate can be specified by its nickname or by a path to the containing file.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dt>
<dd> Enable quiet mode; no output is produced whether the certificate is expired or not</dl>
<p> <code>&#8211;period </code><i>days</i>, <code>-p </code><i>days</i></p>
<dl>
<dt>
<dd> Specify the number of days within which an expiry warning will be produced; default is 30. Expiry warnings are always produced if, on the day of invocation, the certificate is not yet valid, has already expired, or is due to expire either that day or the following day.</dl>
<p> <code>&#8211;address </code><i>address</i>, <code>-a </code><i>address</i></p>
<dl>
<dt>
<dd> Specify the address used in the To field of the warning e-mail issued if quiet mode is not enabled. The default is root.</dl>
<p> <code>&#8211;directory </code><i>cert-directory</i>, <code>-d </code><i>cert-directory</i></p>
<dl>
<dt>
<dd> Specify the database directory containing the certificate and key database files. The default is yet to be determined.</dl>
<h2>DIAGNOSTICS</h2>
<p> The exit code indicates the state of the certificate: </p>
<p> <i>0</i></p>
<dl>
<dt>
<dd> The certificate is outside its validity period, or approaching expiry</dl>
<p> <i>1</i></p>
<dl>
<dt>
<dd> The certificate is inside its validity period, or could not be parsed</dl>
<h2>NOTES</h2>
<p> The <code>certwatch</code> program is run daily by <code>crond</code> from the file /etc/cron.daily/certwatch to generate warning mail concerning the imminent expiry of SSL certificates configured for use in the Apache HTTP server. These warnings can be disabled by adding the line: NOCERTWATCH=yes to the file /etc/sysconfig/httpd. Additional options to pass to <code>certwatch</code> can be specified in that file in the CERTWATCH_OPTS environment variable.</p>
<h2>FILES</h2>
<p> /etc/cron.daily/certwatch, /etc/sysconfig/httpd</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-genkey/">genkey</a>(1) </p>
<h2>Index</h2>
