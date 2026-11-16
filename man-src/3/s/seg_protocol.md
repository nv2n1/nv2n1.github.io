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
<dt>*</dt>
<dd><i>MESSAGE-TYPE</i> is a three-digit integer. The JSM will parse the message contents based on the message type.</dd></dl>
<dl>
<dt>*</dt>
<dd><i>TIMESTAMP</i> is an unsigned value indicating seconds since the UNIX epoch.</dd></dl>
<h2>Message Types</h2>
<h3>001 &#8211; Job State Change</h3>
<pre> Message Format: 001;TIMESTAMP;JOBID;STATE;EXIT_CODE</pre>
<p>Message Type Specific Content: </p>
<dl>
<dt><code>JOBID </code></dt>
<dd>local scheduler-specific job id</dd>
<dt><code>STATE </code></dt>
<dd>new job state (integer as per the GRAM protocol constants)</dd>
<dt><code>EXIT_CODE </code></dt>
<dd>job exit code if STATE is done or failed.</dd></dl>
