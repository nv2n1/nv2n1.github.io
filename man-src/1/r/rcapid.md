---
title: "rcapid(1)"
name: "rcapid"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcapid/"
---

<h2>NAME</h2>

 rcapid - remote CAPI server

<h2>SYNOPSIS</h2>

 rcapid [-l loglevel]

<h2>DESCRIPTION</h2>

 

 rcapid is a server to communicate with CAPI clients. It is designed to run from inetd. add the following line to /etc/services: 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>capi 6000/tcp
 

 Add the following line to /etc/inetd.conf: 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>capi stream tcp nowait.9999 /usr/sbin/rcapid rcapid

<h2>OPTIONS</h2>

<dl>
<dt>-l loglevel
<dd> the level of verbosity in the logging. This is logged in /tmp/rcapid.log</dl>

<h2>AUTHOR</h2>

 This manual page was written by Paul Slootman &lt;paul [at] tdebian.org&gt;, Than Ngo &lt;than [at] redhat.com&gt; 

<h2>Index</h2>


