---
title: "snmp_sess_open(3)"
name: "snmp_sess_open"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snmp_sess_open/"
description: "snmp_sess_init, snmp_sess_open, snmp_sess_session, snmp_sess_send, snmp_sess_async_send, snmp_sess_select_info, snmp_sess_read, snmp_sess_timeout, snmp_sess_synch_response, snmp_sess_close, snmp_se..."
---

<p>snmp_sess_init, snmp_sess_open, snmp_sess_session, snmp_sess_send, snmp_sess_async_send, snmp_sess_select_info, snmp_sess_read, snmp_sess_timeout, snmp_sess_synch_response, snmp_sess_close, snmp_sess_error &#8211; session functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/session_api.h&gt;
void snmp_sess_init(struct snmp_session *session);
void *snmp_sess_open(struct snmp_session *session);
struct snmp_session *snmp_sess_session(void *handle);
int snmp_sess_send(void *handle, struct snmp_pdu *pdu);
int snmp_sess_async_send(void *handle,

                         struct snmp_pdu *pdu,

                         snmp_callback callback,

                         void *callbackData);
int snmp_sess_select_info(void *handle,

                          int *numfds, fd_set *fdset,

                          struct timeval *timeout,

                          int *block);
int snmp_sess_read(void *handle, fd_set *fdset);
void snmp_sess_timeout(void *handle);
int snmp_sess_synch_response(void *handle,

                             netsnmp_pdu *pdu,

                             netsnmp_pdu **response);
int snmp_sess_close(void *handle);
void snmp_sess_error(void *handle, int *pcliberr,

                     int *psnmperr, char **pperrstring);</code></pre>
<h2>Description</h2>
<p>These functions define a subset of the API that can be used to manage single SNMP sessions in a multi-threaded application. Except for <code>snmp_sess_session()</code>, these functions are single session versions of the traditional SNMP library API. </p>
<p> Note that these functions use an opaque pointer (<i>handle</i> in the above prototypes) to identify a single session in lieu of a <i>session</i> pointer (as in the traditional API). </p>
<p> <code>snmp_sess_init()</code> prepares a struct snmp_session that sources transport characteristics and common information that will be used for a set of SNMP transactions. After this structure is passed to <code>snmp_sess_open()</code> to create an SNMP session, the structure is no longer used. Instead the opaque pointer returned by <code>snmp_sess_open()</code> is used to refer to that session henceforth. </p>
<p> SNMP sessions that are created with <code>snmp_sess_open()</code> are not affected by, and SHOULD NOT BE USED WITH, <code>snmp_select_info()</code>, <code>snmp_read()</code>, <code>snmp_timeout()</code> nor <code>snmp_close()</code>. Rather the equivalent single session functions described here should be used. </p>
<p> <code>snmp_sess_init()</code> and <code>snmp_sess_open()</code> each take as input a pointer to a struct snmp_session object. This structure contains information for a set of transactions that will share similar transport characteristics. <code>snmp_sess_session()</code> takes the opaque session handle and returns a pointer to its associated struct snmp_session. </p>
<p> <code>snmp_sess_send()</code> and <code>snmp_sess_async_send()</code> each take a <i>pdu</i> parameter, which points to a struct snmp_pdu object containing information that describes a transaction that will be performed over an open session. </p>
<p> Consult snmp_api.h for the definitions of these structures. </p>
<p> With the <i>snmp_sess_async_send()</i> call, <i>snmp_sess_read</i> will invoke the specified callback when the response is received. </p>
<p> <code>snmp_sess_select_info()</code>, <code>snmp_sess_read()</code> and <code>snmp_sess_timeout()</code> provide an interface for the use of the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) system call so that SNMP transactions for a single session can occur asynchronously. </p>
<p> <code>snmp_sess_select_info()</code> is passed the information that would have been passed to <code><a href="/docs/linux/man/2-select/">select</a></code>(2) in the absence of SNMP. For example, this might include file descriptors associated with the main loop of a graphical application. This information is modified so that SNMP will get the service it requires from the call to <code><a href="/docs/linux/man/2-select/">select</a></code>(2). In this case, <i>numfds</i>, <i>fdset</i> and <i>timeout</i> correspond to the <i>nfds</i>, <i>readfds</i> and <i>timeout</i> arguments to <code><a href="/docs/linux/man/2-select/">select</a></code>(2) respectively. The only exception is that timeout must ALWAYS point to an allocated (but perhaps uninitialized) <i>struct timeval</i> (it cannot be NULL as for <code><a href="/docs/linux/man/2-select/">select</a></code>(2)). If <i>timeout</i> would have been passed as NULL, <i>block</i> is instead set to true, and <i>timeout</i> is treated as undefined. This same rule applies upon return from <code>snmp_select_info()</code>. </p>
<p> After calling <code>snmp_sess_select_info() ,</code> <code><a href="/docs/linux/man/2-select/">select</a></code>(2) should be called with the returned data. When it returns, <code>snmp_sess_read()</code> should then be called with the <i>fd_set</i> returned from <code><a href="/docs/linux/man/2-select/">select</a></code>(2). This will read any input from this session&#8217;s SNMP socket. If <code><a href="/docs/linux/man/2-select/">select</a></code>(2) times out (that is, it returns zero), <code>snmp_sess_timeout()</code> should be called to see if a timeout has occurred on the SNMP session. </p>
<p> <i>snmp_sess_synch_response</i> is a convenience routine that will send the request, wait for the response and process it before returning. See the descriptions of <i>snmp_sess_send , snmp_sess_read</i> etc for details.</p>
<h2>Diagnostics</h2>
<p>Error return status from <code>snmp_sess_open()</code> is indicated by return of a NULL pointer. Error return status from <code>snmp_sess_close()</code> and <code>snmp_sess_send()</code> is indicated by a return value of 0. A successful status will return 1. </p>
<p> Further information can be obtained by using <code>snmp_sess_error()</code> to see what type of error has occurred. This function returns the SNMP <i>snmp_errno</i> variable, the value of the system <i>errno</i> variable, and a string interpretation of both variables. The string must be freed after use by the caller. </p>
<p> For errors returned by <code>snmp_sess_open()</code>, use the corresponding function <code>snmp_error()</code> instead of <code>snmp_sess_error()</code>. </p>
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
<dt>SNMPERR_BAD_RCVFROM</p>
<dd>
<dt>SNMPERR_BAD_PARSE</p>
<dd>
<dt>SNMPERR_BAD_VERSION</p>
<dd>
<dt>SNMPERR_BAD_COMMUNITY</p>
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
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/3-snmp_api/">snmp_api</a></code>(3), <code>snmp_api.h</code> </p>
