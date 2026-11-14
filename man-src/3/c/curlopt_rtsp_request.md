---
title: "curlopt_rtsp_request(3)"
name: "curlopt_rtsp_request"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_rtsp_request/"
description: "CURLOPT_RTSP_REQUEST – specify RTSP request"
---

<p>CURLOPT_RTSP_REQUEST &#8211; specify RTSP request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RTSP_REQUEST, long request);</p>
<h2>Description</h2>
<p>Tell libcurl what kind of RTSP request to make. Pass one of the following RTSP enum values as a long in the <i>request</i> argument. Unless noted otherwise, commands require the Session ID to be initialized.</p>
<dl COMPACT>
<dt>CURL_RTSPREQ_OPTIONS</p>
<dd>Used to retrieve the available methods of the server. The application is responsible for parsing and obeying the response. <code>(The session ID is not needed for this method.)</code></p>
<dt>CURL_RTSPREQ_DESCRIBE</p>
<dd>Used to get the low level description of a stream. The application should note what formats it understands in the <i>&#8216;Accept:&#8217;</i> header. Unless set manually, libcurl will automatically fill in <i>&#8216;Accept: application/sdp&#8217;</i>. Time-condition headers will be added to Describe requests if the <i><a href="/docs/linux/man/3-curlopt_timecondition/">CURLOPT_TIMECONDITION</a>(3)</i> option is active. <code>(The session ID is not needed for this method)</code></p>
<dt>CURL_RTSPREQ_ANNOUNCE</p>
<dd>When sent by a client, this method changes the description of the session. For example, if a client is using the server to record a meeting, the client can use Announce to inform the server of all the meta-information about the session. ANNOUNCE acts like a HTTP PUT or POST just like <i>CURL_RTSPREQ_SET_PARAMETER</i></p>
<dt>CURL_RTSPREQ_SETUP</p>
<dd>Setup is used to initialize the transport layer for the session. The application must set the desired Transport options for a session by using the <i><a href="/docs/linux/man/3-curlopt_rtsp_transport/">CURLOPT_RTSP_TRANSPORT</a>(3)</i> option prior to calling setup. If no session ID is currently set with <i><a href="/docs/linux/man/3-curlopt_rtsp_session_id/">CURLOPT_RTSP_SESSION_ID</a>(3)</i>, libcurl will extract and use the session ID in the response to this request. <code>(The session ID is not needed for this method).</code></p>
<dt>CURL_RTSPREQ_PLAY</p>
<dd>Send a Play command to the server. Use the <i><a href="/docs/linux/man/3-curlopt_range/">CURLOPT_RANGE</a>(3)</i> option to modify the playback time (e.g. &#8216;npt=10-15&#8217;).</p>
<dt>CURL_RTSPREQ_PAUSE</p>
<dd>Send a Pause command to the server. Use the <i><a href="/docs/linux/man/3-curlopt_range/">CURLOPT_RANGE</a>(3)</i> option with a single value to indicate when the stream should be halted. (e.g. npt=&#8217;25&#8217;)</p>
<dt>CURL_RTSPREQ_TEARDOWN</p>
<dd>This command terminates an RTSP session. Simply closing a connection does not terminate the RTSP session since it is valid to control an RTSP session over different connections.</p>
<dt>CURL_RTSPREQ_GET_PARAMETER</p>
<dd>Retrieve a parameter from the server. By default, libcurl will automatically include a <i>Content-Type: text/parameters</i> header on all non-empty requests unless a custom one is set. GET_PARAMETER acts just like a HTTP PUT or POST (see <i>CURL_RTSPREQ_SET_PARAMETER</i>). Applications wishing to send a heartbeat message (e.g. in the presence of a server-specified timeout) should send use an empty GET_PARAMETER request.</p>
<dt>CURL_RTSPREQ_SET_PARAMETER</p>
<dd>Set a parameter on the server. By default, libcurl will automatically include a <i>Content-Type: text/parameters</i> header unless a custom one is set. The interaction with SET_PARAMETER is much like a HTTP PUT or POST. An application may either use <i><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a>(3)</i> with <i><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a>(3)</i> like a HTTP PUT, or it may use <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> like a HTTP POST. No chunked transfers are allowed, so the application must set the <i><a href="/docs/linux/man/3-curlopt_infilesize/">CURLOPT_INFILESIZE</a>(3)</i> in the former and <i><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a>(3)</i> in the latter. Also, there is no use of multi-part POSTs within RTSP.</p>
<dt>CURL_RTSPREQ_RECORD</p>
<dd>Used to tell the server to record a session. Use the <i><a href="/docs/linux/man/3-curlopt_range/">CURLOPT_RANGE</a>(3)</i> option to modify the record time.</p>
<dt>CURL_RTSPREQ_RECEIVE</p>
<dd>This is a special request because it does not send any data to the server. The application may call this function in order to receive interleaved RTP data. It will return after processing one read buffer of data in order to give the application a chance to run.</dl>
<h2>Default</h2>
<h2>Protocols</h2>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_rtsp_session_id/">CURLOPT_RTSP_SESSION_ID</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_rtsp_stream_uri/">CURLOPT_RTSP_STREAM_URI</a></code>(3),</p>
