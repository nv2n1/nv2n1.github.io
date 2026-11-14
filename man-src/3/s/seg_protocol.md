---
title: "seg_protocol(3)"
name: "seg_protocol"
section: "3"
letter: "s"
url: "/docs/linux/man/3-seg_protocol/"
description: "seg_protocol – SEG Protocol The general form for the SEG protocol messages is"
---

<p>seg_protocol &#8211; SEG Protocol The general form for the SEG protocol messages is </p>
<pre>MESSAGE-TYPE;TIMESTAMP;message-type-specific content</pre>
<dl>
<dt>*</p>
<dd><i>MESSAGE-TYPE</i> is a three-digit integer. The JSM will parse the message contents based on the message type.</dl>
<dl>
<dt>*</p>
<dd><i>TIMESTAMP</i> is an unsigned value indicating seconds since the UNIX epoch.</dl>
<h2>Message Types</h2>
<h3>001 &#8211; Job State Change</h3>
<pre> Message Format: 001;TIMESTAMP;JOBID;STATE;EXIT_CODE</pre>
<p>Message Type Specific Content: </p>
<dl>
<dt><code>JOBID </code></p>
<dd>local scheduler-specific job id</p>
<dt><code>STATE </code></p>
<dd>new job state (integer as per the GRAM protocol constants)</p>
<dt><code>EXIT_CODE </code></p>
<dd>job exit code if STATE is done or failed.</dl>
