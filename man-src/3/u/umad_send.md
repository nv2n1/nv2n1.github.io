---
title: "umad_send(3)"
name: "umad_send"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_send/"
description: "umad_send – send umad"
---

<p>umad_send &#8211; send umad</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_send(int portid, int agentid, void *umad, int length, int timeout_ms, int retries);</code></pre>
<h2>Description</h2>
<p><code>umad_send()</code> sends <i>length</i> bytes from the specified <i>umad</i> buffer from the port specified by <i>portid</i>, and using the agent specified by <i>agentid</i>. </p>
<p> The buffer can contain a RMPP transmission which is larger than a single MAD packet when the agentid specifies a class which utilizes RMPP and the header flags indicate RMPP is active. NOTE currently only RMPPFlags.Active is meaningful in the header in user space. All other RMPP fields are ignored. The data section of the buffer will be sent in multiple RMPP MAD packets with headers built for the user. </p>
<p> <i>timeout_ms</i> controls the solicited MADs behavior as follows: zero value means not solicited. Positive value makes kernel indicate timeout in milliseconds. If reply is not received within the specified value, the original buffer is returned in the read channel with the status field set (to non zero). Negative <i>timeout_ms</i> makes kernel wait forever for the reply. <i>retries</i> indicates the number of times the MAD will be retried before giving up.</p>
<h2>Return Value</h2>
<p><code>umad_send()</code> returns 0 on success; on error, errno is set and a negative value is returned as follows:<br />
&nbsp;<wbr>-EINVAL invalid port handle or agentid<br />
&nbsp;<wbr>-EIO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>send operation failed</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
