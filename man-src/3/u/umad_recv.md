---
title: "umad_recv(3)"
name: "umad_recv"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_recv/"
description: "umad_recv – receive umad"
---

<p>umad_recv &#8211; receive umad</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_recv(int portid, void *umad, int *length, int timeout_ms);</code></pre>
<h2>Description</h2>
<p><code>umad_recv()</code> waits up to <i>timeout_ms</i> milliseconds for an incoming MAD message to be received from the port specified by <i>portid</i>. A MAD &quot;message&quot; consists of a single MAD packet <i>or</i> a coalesced multipacket RMPP transmission. In the RMPP case the header of the first RMPP packet is returned as the header of the buffer and the buffer data contains the coalesced data section of each subsequent RMPP MAD packet within the transmission. Thus all the RMPP headers except the first are not copied to user space from the kernel. The message is copied to the <i>umad</i> buffer if there is sufficient room and the received <i>length</i> is indicated. If the buffer is not large enough, the size of the umad buffer needed is returned in <i>length</i>. A negative <i>timeout_ms</i> makes the function block until a packet is received. A <i>timeout_ms</i> parameter of zero indicates a non blocking read. <code>Note</code> <i>length</i> is a pointer to the length of the <code>data</code> portion of the umad buffer. This means that <i>umad</i> must point to a buffer at least umad_size() + <i>*length</i> bytes long. <code>Note also</code> that <i>*length</i> must be &gt;= 256 bytes. This length allows for at least a single MAD packet to be returned. </p>
<h2>Return Value</h2>
<p><code>umad_recv()</code> on success return the agentid; on error, errno is set and a negative value is returned as follows:<br />
&nbsp;<wbr>-EINVAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>invalid port handle or agentid or&nbsp;<wbr>*length is less than the minimum supported<br />
&nbsp;<wbr>-EIO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>receive operation failed<br />
&nbsp;<wbr>-EWOULDBLOCK non blocking read can&#8217;t be fulfilled<br />
&nbsp;<wbr>-ENOSPC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The provided buffer is not long enough for the complete message.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_poll/">umad_poll</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
