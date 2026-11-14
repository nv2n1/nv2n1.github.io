---
title: "snmp_api_errstring(3)"
name: "snmp_api_errstring"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snmp_api_errstring/"
description: "snmp_sess_init, snmp_open, snmp_send, snmp_async_send, snmp_select_info, snmp_read, snmp_timeout, snmp_synch_response, snmp_close, snmp_perror, snmp_sess_perror, snmp_error, snmp_api_errstring – ne..."
---

<p>snmp_sess_init, snmp_open, snmp_send, snmp_async_send, snmp_select_info, snmp_read, snmp_timeout, snmp_synch_response, snmp_close, snmp_perror, snmp_sess_perror, snmp_error, snmp_api_errstring &#8211; netsnmp_session_api functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/session_api.h&gt;
void snmp_sess_init(netsnmp_session *sess);</code></pre>
<p> <code>netsnmp_session* snmp_open ( netsnmp_session *</code><i>sess);</i></p>
<dl>
<dd><i>/* Input parameter not used in active sessions */</i></dl>
<p> int snmp_send(netsnmp_session *session,</p>
<p>              netsnmp_pdu *pdu);<br />
int snmp_async_send(netsnmp_session *session,</p>
<p>                    netsnmp_pdu *pdu,</p>
<p>                    snmp_callback callback,</p>
<p>                    void *callbackData);<br />
int snmp_select_info(int *numfds, fd_set *fdset,</p>
<p>                     struct timeval *timeout, int *block);<br />
void snmp_read(fd_set *fdset);<br />
void snmp_timeout(void);<br />
int snmp_synch_response(netsnmp_session *session,</p>
<p>                        netsnmp_pdu *pdu,</p>
<p>                        netsnmp_pdu **response);<br />
int snmp_close(netsnmp_session *session);</p>
<p>int snmp_close_sessions(void);</p>
<h3>Error Reporting</h3>
<p><i>(Move to <a href="/docs/linux/man/3-output_api/">output_api</a>(3))</i><br />
 <code>void snmp_error ( netsnmp_session *session,</code></p>
<dl>
<dd><code>int *</code><i>pcliberr,</i><code>int *</code><i>psnmperr,</i><code>char **</code><i>pperrstring</i><code>);</code></dl>
<pre><code>char *snmp_api_errstring(intsnmperr);</code></pre>
<p> <code>void snmp_perror ( char *</code><i>msg</i><code>);</code></p>
<dl>
<dd><i>/* for parsing errors only */</i></dl>
<p> <code>void snmp_sess_perror (char *</code><i>msg,</i><code>netsnmp_session *</code><i>sess</i><code>);</code></p>
<dl>
<dd><i>/* all other SNMP library errors */</i></dl>
<h2>Description</h2>
<p><i>Snmp_sess_init</i> prepares a netsnmp_session that sources transport characteristics and common information that will be used for a set of SNMP transactions. After this structure is passed to <i>snmp_open</i> to create an SNMP session, the structure is not used. </p>
<p> <i>Snmp_open</i> returns a pointer to a newly-formed <i>netsnmp_session</i> object, which the application must use to reference the active SNMP session. </p>
<p> <i>snmp_send</i> and <i>snmp_async_send()</i> each take as input a pointer to a <i>netsnmp_pdu</i> object. This structure contains information that describes a transaction that will be performed over an open session. </p>
<p> Consult snmp_api.h for the definitions of these structures. </p>
<p> With the <i>snmp_async_send()</i> call, <i>snmp_read</i> will invoke the specified callback when the response is received. </p>
<p> <i>Snmp_read, snmp_select_info,</i> and <i>snmp_timeout</i> provide an interface for the use of the <i><a href="/docs/linux/man/2-select/">select</a>(2)</i> system call so that SNMP transactions can occur asynchronously. </p>
<p> <i>Snmp_select_info</i> is given the information that would have been passed to <i>select</i> in the absence of SNMP. For example, this might include window update information. This information is modified so that SNMP will get the service it requires from the call to <i>select.</i> In this case, <i>numfds, fdset,</i> and <i>timeout</i> correspond to the <i>nfds, readfds,</i> and <i>timeout</i> arguments to <i>select,</i> respectively. The only exception is that timeout must always point to an allocated (but perhaps uninitialized) <i>struct timeval.</i> If <i>timeout</i> would have been passed as NULL, <i>block</i> is set to true, and <i>timeout</i> is treated as undefined. This same rule applies upon return from <i>snmp_select_info.</i> </p>
<p> After calling <i>snmp_select_info, select</i> is called with the returned data. When select returns, <i>snmp_read</i> should be called with the <i>fd_set</i> returned from <i>select</i> to read each SNMP socket that has input. If <i>select</i> times out, <i>snmp_timeout</i> should be called to see if the timeout was intended for SNMP. </p>
<p> <i>snmp_synch_response</i> is a convenience routine that will send the request, wait for the response and process it before returning. See the descriptions of <i>snmp_send , snmp_read</i> etc for details.</p>
<h2>Diagnostics</h2>
<p>Previous versions of the library used <i>snmp_get_errno</i> to read the global variable <i>snmp_errno</i> which may have held the error status within the SNMP library. The existing method <i>snmp_perror</i> should be used to log ASN.1 coding errors only. </p>
<p> The new method <i>snmp_sess_perror</i> is provided to capture errors that occur during the processing of a particular SNMP session. <i>Snmp_sess_perror</i> calls <i>snmp_error</i> function to obtain the &quot;C&quot; library error <i>errno</i> , the SNMP library error <i>snmperr</i> , and the SNMP library detailed error message that is associated with an error that occurred during a given session. </p>
<p> Note that in all cases except one, <i>snmp_sess_perror</i> should be handed the <i>netsnmp_session *</i> pointer returned from <i>snmp_open.</i> If <i>snmp_open</i> returns a null pointer, pass the INPUT <i>netsnmp_session *</i> pointer used to call <i>snmp_open.</i> </p>
<p> Error return status from <i>snmp_close</i> and <i>snmp_send</i> is indicated by return of 0. A successful status will return a 1 for <i>snmp_close</i> and the request id of the packet for <i>snmp_send.</i> Upon successful return from <i>snmp_send</i> the pdu will be freed by the library. </p>
<p> Consult snmp_api.h for the complete set of SNMP library error values. The SNMP library error value <i>snmperr</i> can be one of the following values:</p>
<dl>
<dd>
<dl>
<dt>SNMPERR_GENERR</p>
<dd>A generic error occurred.</p>
<dt>SNMPERR_BAD_LOCPORT</p>
<dd>The local port was bad because it had already been allocated or permission was denied.</p>
<dt>SNMPERR_BAD_ADDRESS</p>
<dd>The host name or address given was not useable.</p>
<dt>SNMPERR_BAD_SESSION</p>
<dd>The specified session was not open.</p>
<dt>SNMPERR_TOO_LONG</p>
<dd>
<dt>SNMPERR_NO_SOCKET</p>
<dd>
<dt>SNMPERR_V2_IN_V1</p>
<dd>
<dt>SNMPERR_V1_IN_V2</p>
<dd>
<dt>SNMPERR_BAD_REPEATERS</p>
<dd>
<dt>SNMPERR_BAD_REPETITIONS</p>
<dd>
<dt>SNMPERR_BAD_ASN1_BUILD</p>
<dd>
<dt>SNMPERR_BAD_SENDTO</p>
<dd>
<dt>SNMPERR_BAD_PARSE</p>
<dd>
<dt>SNMPERR_BAD_VERSION</p>
<dd>
<dt>SNMPERR_NOAUTH_DESPRIV</p>
<dd>
<dt>SNMPERR_ABORT</p>
<dd>
<dt>SNMPERR_UNKNOWN_PDU</p>
<dd>
<dt>SNMPERR_TIMEOUT</p>
<dd></dl>
</dl>
<p> A string representation of the error code can be obtained with <i>snmp_api_errstring</i>, and a standard error message may be printed using <i>snmp_perror</i> that functions like the <i>perror</i> standard routine.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/2-select/">select</a>(2), snmp_api.h </p>
