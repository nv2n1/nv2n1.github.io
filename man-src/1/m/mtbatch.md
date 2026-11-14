---
title: "mtbatch(1)"
name: "mtbatch"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtbatch/"
description: "mtbatch – Sends SMS in batch mode"
---

<h2>NAME</h2>
<p> mtbatch &#8211; Sends SMS in batch mode</p>
<h2>SYNOPSIS</h2>
<p> <code>mtbatch</code> <i></i>[options]<i>content-file</i>receivers-file<i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mtbatch</code> -v number<br />
&nbsp;<wbr>set log level for stderr logging -b host<br />
&nbsp;<wbr>defines the host of bearerbox&nbsp;<wbr>(default: localhost) -p port<br />
&nbsp;<wbr>the smsbox port to connect to&nbsp;<wbr>(default: 13002) -s<br />
&nbsp;<wbr>inidicatr to use SSL for bearerbox connection&nbsp;<wbr>(default: no) -i smsbox-id<br />
&nbsp;<wbr>defines the smsbox-id to be used for bearerbox connection&nbsp;<wbr>(default: none) -f sender<br />
&nbsp;<wbr>which sender address should be used -n service<br />
&nbsp;<wbr>defines which service name should be logged&nbsp;<wbr>(default: none) -a account<br />
&nbsp;<wbr>defines which account name should be logged&nbsp;<wbr>(default: none) -d seconds<br />
&nbsp;<wbr>delay between message sending to bearerbox&nbsp;<wbr>(default: 0) -r smsc-id<br />
&nbsp;<wbr>use a specific route for the MT traffic</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-kannel/">kannel</a></code>(8) </p>
<h2>Index</h2>
