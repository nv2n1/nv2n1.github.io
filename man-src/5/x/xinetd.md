---
title: "xinetd(5)"
name: "xinetd"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xinetd/"
description: "xinetd.log – xinetd service log format"
---

<p>xinetd.log &#8211; xinetd service log format</p>
<h2>Description</h2>
<p>A service configuration may specify various degrees of logging when attempts are made to access the service. When logging for a service is enabled, <code>xinetd</code> will generate one-line log entries which have the following format (all entries have a timestamp as a prefix): </p>
<dl>
<dd><i>entry</i>: <i>service-id</i> <i>data</i></dd></dl>
<p> The <i>data</i> depends on the <i>entry</i>. Possible <i>entry</i> types include:</p>
<dl>
<dd>
</dd><dl>
<dt><code>START</code></dt>
<dd>generated when a server is started</dd>
<dt><code>EXIT</code></dt>
<dd>generated when a server exits</dd>
<dt><code>FAIL</code></dt>
<dd>generated when it is not possible to start a server</dd>
<dt><code>USERID</code></dt>
<dd>generated if the <i>USERID</i> log option is used.</dd>
<dt><code>NOID</code></dt>
<dd>generated if the <i>USERID</i> log option is used, and the <i>IDONLY</i> service flag is used, and the remote end does not identify who is trying to access the service.</dd></dl>
</dl>
<p> In the following, the information enclosed in brackets appears if the appropriate log option is used. </p>
<p> A <i>START</i> entry has the format: </p>
<dl>
<dd>START: <i>service-id</i> [pid=%d] [from=%d.%d.%d.%d]</dd></dl>
<p> An <i>EXIT</i> entry has the format: </p>
<dl>
<dd>EXIT: <i>service-id</i> [<i>type</i>=%d] [pid=%d] [duration=%d(sec)]</dd></dl>
<p> <i>type</i> can be either <code>status</code> or <code>signal.</code> The number is either the exit status or the signal that caused process termination. </p>
<p> A <i>FAIL</i> entry has the format: </p>
<dl>
<dd>FAIL: <i>service-id</i> <i>reason</i> [from=%d.%d.%d.%d]</dd></dl>
<p> Possible <i>reasons</i> are:</p>
<dl>
<dd>
</dd><dl>
<dt><code>fork</code></dt>
<dd>a certain number of consecutive fork attempts failed (this number is a configurable parameter)</dd>
<dt><code>time</code></dt>
<dd>the time check failed</dd>
<dt><code>address</code></dt>
<dd>the address check failed</dd>
<dt><code>service_limit</code></dt>
<dd>the allowed number of server instances for this service would be exceeded</dd>
<dt><code>process_limit</code></dt>
<dd>a limit on the number of forked processes was specified and it would be exceeded</dd></dl>
</dl>
<p> A <i>DATA</i> entry has the format: </p>
<dl>
<dd>DATA: <i>service-id</i> <i>data</i></dd></dl>
<p> The <i>data</i> logged depends on the service.</p>
<dl>
<dd>
</dd><dl>
<dt><code>login</code></dt>
<dd>remote_user=%s local_user=%s tty=%s</dd>
<dt><code>exec</code></dt>
<dd>remote_user=%s verify=<i>status</i> command=%s<br/>
 Possible <i>status</i> values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>ok</i></dt>
<dd>the password was correct</dd>
<dt><i>failed</i></dt>
<dd>the password was incorrect</dd>
<dt><i>baduser</i></dt>
<dd>no such user</dd></dl>
</dl>
<dt><code>shell</code></dt>
<dd>remote_user=%s local_user=%s command=%s</dd>
<dt><code>finger</code></dt>
<dd><i>received string</i> or <i>EMPTY-LINE</i></dd></dl>
</dl>
<p> A <i>USERID</i> entry has the format: </p>
<dl>
<dd>USERID: <i>service-id</i> <i>text</i></dd></dl>
<p> The <i>text</i> is the response of the identification daemon at the remote end excluding the port numbers (which are included in the response). </p>
<p> A <i>NOID</i> entry has the format: </p>
<dl>
<dd>NOID: <i>service-id</i> <i>IP-address</i> <i>reason</i></dd></dl>
<h2>See Also</h2>
<p><code>xinetd</code>(1L), <code><a href="/docs/linux/man/5-xinetd-conf/">xinetd.conf</a></code>(5) </p>
