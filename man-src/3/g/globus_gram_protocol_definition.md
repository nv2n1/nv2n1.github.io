---
title: "globus_gram_protocol_definition(3)"
name: "globus_gram_protocol_definition"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_definition/"
description: "globus_gram_protocol_definition – GRAM Protocol Definition The GRAM Protocol is used to handle communication between the Gatekeeper, Job Manager, and GRAM Clients. The protocol is based on a subset..."
---

<h2 class="name">NAME</h2>
<p> globus_gram_protocol_definition &#8211; GRAM Protocol Definition The GRAM Protocol is used to handle communication between the Gatekeeper, Job Manager, and GRAM Clients. The protocol is based on a subset of the HTTP/1.1 protocol, with a small set of message types and responses sent as the body of the HTTP requests and responses. This document describes GRAM Protocol version 2.</p>
<h3>Framing</h3>
<p> GRAM messages are framed in HTTP/1.1 messages. However, only a small subset of the HTTP specification is used or understood by the GRAM system. All GRAM requests are HTTP POST messages. Only the following HTTP headers are understood:</p>
<dl>
<dt>&bull;</p>
<dd> Host</p>
<dt>&bull;</p>
<dd> Content-Type (set to &#8216;application/x-globus-gram&#8217; in all cases)</p>
<dt>&bull;</p>
<dd> Content-Length</p>
<dt>&bull;</p>
<dd> Connection (set to &#8216;close&#8217; in all HTTP responses)</dl>
<p> Only the following status codes are supported in response&#8217;s HTTP Status-Lines:</p>
<dl>
<dt>&bull;</p>
<dd> 200 OK</p>
<dt>&bull;</p>
<dd> 403 Forbidden</p>
<dt>&bull;</p>
<dd> 404 Not Found</p>
<dt>&bull;</p>
<dd> 500 Internal Server Error</p>
<dt>&bull;</p>
<dd> 400 Bad Request</dl>
<h3>Message Format</h3>
<p> All messages use the carriage return (ASCII value 13) followed by line feed (ASCII value 10) sequence to delimit lines. In all cases, a blank line separates the HTTP header from the message body. All <code>application/x-globus-gram</code> message bodies consist of attribute names followed by a colon, a space, and then the value of the attribute. When the value may contain a newline or double-quote character, a special escaping rule is used to encapsulate the complete string. This encapsulation consists of surrounding the string with double-quotes, and escaping all double-quote and backslash characters within the string with a backslash. All other characters are sent without modification. For example, the string </p>
<pre>
rsl: &amp;( executable = &quot;/bin/echo&quot; )
 ( arguments = &quot;hello&quot; )
</pre>
<p>&nbsp;<wbr>becomes&nbsp;<wbr> </p>
<pre>
rsl: &quot;&amp;( executable =   (arguments = 
</pre>
<p> This is the only form of quoting which <code>application/x-globus-gram</code> messages support. Use of % HEX HEX escapes (such as seen in URL encodings) is not meaningful for this protocol. </p>
<h3>Message Types</h3>
<h3>Ping Request</h3>
<p> A ping request is used to verify that the gatekeeper is configured properly to handle a named service. The ping request consists of the following: </p>
<pre>
    POST ping/<i>job-manager-name</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
</pre>
<p> The values of the message-specific strings are</p>
<dl>
<dt><i>job-manager-name</i></p>
<dd> The name of the service to have the gatekeeper check. The service name corresponds to one of the gatekeeper&#8217;s configured grid-services, and is usually of the form &#8216;jobmanager-&lt;em&gt;scheduler-type&lt;/em&gt;&#8217;.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the gatekeeper is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</dl>
<h3>Job Request</h3>
<p> A job request is used to scheduler a job remotely using GRAM. The ping request consists of the HTTP framing described above with the request-URI consisting of <i>job-manager-name</i>, where <i>job-manager name</i> is the name of the service to use to schedule the job. The format of a job request message consists of the following: </p>
<pre>
    POST <i>job-manager-name</i>[@<i>user-name</i>] HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    job-state-mask: <i>mask</i>
    callback-url: <i>callback-contact</i>
    rsl: <i>rsl-description</i>
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>job-manager-name</i></p>
<dd> The name of the service to submit the job request to. The service name corresponds to one of the gatekeeper&#8217;s configured grid-services, and is usually of the form &#8216;jobmanager-&lt;em&gt;scheduler-type&lt;/em&gt;&#8217;.</p>
<dt><i>user-name</i></p>
<dd> Starting with GT4.0, a client may request that a certain account by used by the gatekeeper to start the job manager. This is done optionally by appending the @ symbol and the local user name that the job should be run as to the <i>job-manager-name</i>. If the @ and username are not present, then the first grid map entry will be used. If the client credential is not authorized in the grid map to use the specified account, an authorization error will occur in the gatekeeper.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the gatekeeper is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</p>
<dt><i>mask</i></p>
<dd> An integer representation of the job state mask. This value is obtained from a bitwise-OR of the job state values which the client wishes to receive job status callbacks about. These meanings of the various job state values are defined in the <code>GRAM Protocol API documentation</code>.</p>
<dt><i>callback-contact</i></p>
<dd> A https URL which defines a GRAM protocol listener which will receive job state updates. The from a bitwise-OR of the job state values which the client wishes to receive job status callbacks about. The job status update messages are defined <code>below</code>.</p>
<dt><i>rsl-description</i></p>
<dd> A quoted string containing the RSL description of the job request.</dl>
<h3>Status Request</h3>
<p> A status request is used by a GRAM client to get the current job state of a running job. This type of message can only be sent to a job manager&#8217;s job-contact (as returned in the reply to a job request message). The format of a job request message consists of the following: </p>
<pre>
    POST <i>job-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    'status'
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>job-contact</i></p>
<dd> The job contact string returned in a response to a job request message, or determined by querying the MDS system.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the job manager is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</dl>
<h3>Callback Register Request</h3>
<p> A callback register request is used by a GRAM client to register a new callback contact to receive GRAM job state updates. This type of message can only be sent to a job manager&#8217;s job-contact (as returned in the reply to a job request message). The format of a job request message consists of the following: </p>
<pre>
    POST <i>job-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    'register &lt;em&gt;mask&lt;/em&gt; &lt;em&gt;callback-contact&lt;/em&gt;'
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>job-contact</i></p>
<dd> The job contact string returned in a response to a job request message, or determined by querying the MDS system.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the job manager is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</p>
<dt><i>mask</i></p>
<dd> An integer representation of the job state mask. This value is obtained from a bitwise-OR of the job state values which the client wishes to receive job status callbacks about. These meanings of the various job state values are defined in the <code>GRAM Protocol API documentation</code>.</p>
<dt><i>callback-contact</i></p>
<dd> A https URL which defines a GRAM protocol listener which will receive job state updates. The from a bitwise-OR of the job state values which the client wishes to receive job status callbacks about. The job status update messages are defined <code>below</code>.</dl>
<h3>Callback Unregister Request</h3>
<p> A callback unregister request is used by a GRAM client to request that the job manager no longer send job state updates to the specified callback contact. This type of message can only be sent to a job manager&#8217;s job-contact (as returned in the reply to a job request message). The format of a job request message consists of the following: </p>
<pre>
    POST <i>job-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    'unregister &lt;em&gt;callback-contact&lt;/em&gt;'
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>job-contact</i></p>
<dd> The job contact string returned in a response to a job request message, or determined by querying the MDS system.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the job manager is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</p>
<dt><i>callback-contact</i></p>
<dd> A https URL which defines a GRAM protocol listener which should no longer receive job state updates. The from a bitwise-OR of the job state values which the client wishes to receive job status callbacks about. The job status update messages are defined <code>below</code>.</dl>
<h3>Job Cancel Request</h3>
<p> A job cancel request is used by a GRAM client to request that the job manager terminate a job. This type of message can only be sent to a job manager&#8217;s job-contact (as returned in the reply to a job request message). The format of a job request message consists of the following: </p>
<pre>
    POST <i>job-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    'cancel'
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>job-contact</i></p>
<dd> The job contact string returned in a response to a job request message, or determined by querying the MDS system.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the job manager is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</dl>
<h3>Job Signal Request</h3>
<p> A job signal request is used by a GRAM client to request that the job manager process a signal for a job. The arguments to the various signals are discussed in the <code>globus_gram_protocol_job_signal_t</code> documentation. </p>
<pre>
    POST <i>job-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    '&lt;em&gt;signal&lt;/em&gt;'
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>job-contact</i></p>
<dd> The job contact string returned in a response to a job request message, or determined by querying the MDS system.</p>
<dt><i>host-name</i></p>
<dd> The name of the host on which the job manager is running. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</p>
<dt><i>signal</i></p>
<dd> A quoted string containing the signal number and it&#8217;s parameters.</dl>
<h3>Job State Updates</h3>
<p> A job status update message is sent by the job manager to all registered callback contacts when the job&#8217;s status changes. The format of the job status update messages is as follows: </p>
<pre>
    POST <i>callback-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    job-manager-url: <i>job-contact</i>
    status: <i>status-code</i>
    failure-code: <i>failure-code</i>
</pre>
<p> The values of the emphasized text items are as below:</p>
<dl>
<dt><i>callback-contact</i></p>
<dd> The callback contact string registered with the job manager either by being passed as the <i>callback-contact</i> in a job request message or in a callback register message.</p>
<dt><i>host-name</i></p>
<dd> The host part of the callback-contact URL. This exists only for compatibility with the HTTP/1.1 protocol.</p>
<dt><i>message-size</i></p>
<dd> The length of the content of the message, not including the HTTP/1.1 header.</p>
<dt><i>version</i></p>
<dd> The version of the GRAM protocol which is being used. For the protocol defined in this document, the value must be the string &#8216;2&#8217;.</p>
<dt><i>job-contact</i></p>
<dd> The job contact of the job which has changed states.</dl>
<h3>Proxy Delegation</h3>
<p> A proxy delegation message is sent by the client to the job manager to initiate a delegation handshake to generate a new proxy credential for the job manager. This credential is used by the job manager or the job when making further secured connections. The format of the delegation message is as follows: </p>
<pre>
    POST <i>callback-contact</i> HTTP/1.1
    Host: <i>host-name</i>
    Content-Type: application/x-globus-gram
    Content-Length: <i>message-size</i>
</pre>
<pre>
    protocol-version: <i>version</i>
    'renew'
</pre>
<p> If a successful (200) reply is sent in response to this message, then the client will procede with a GSI delegation handshake. The tokens in this handshake will be framed with a 4 byte big-endian token length header. The framed tokens will then be wrapped using the GLOBUS_IO_SECURE_CHANNEL_MODE_SSL_WRAP wrapping mode. The job manager will frame response tokens in the same manner. After the job manager receives its final delegation token, it will respond with another response message that indicates whether the delegation was processed or not. This response message is a standard GRAM response message. </p>
<h3>Note on Security Attributes</h3>
<p> The following security attributes are needed to communicate with the Gatekeeper:</p>
<dl>
<dt>&bull;</p>
<dd> Authentication must be done using GSSAPI mutual authentication</p>
<dt>&bull;</p>
<dd> Messages must be wrapped with support for the delegation message. When using Globus I/O, this is accomplished by using the the GLOBUS_IO_SECURE_CHANNEL_MODE_GSI_WRAP wrapping mode.</dl>
<h3>Changes</h3>
<p> 2004-08-11 Added information about gridmap choosing </p>
<h2>Index</h2>
