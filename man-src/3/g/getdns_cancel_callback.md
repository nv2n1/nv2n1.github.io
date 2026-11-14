---
title: "getdns_cancel_callback(3)"
name: "getdns_cancel_callback"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_cancel_callback/"
description: "getdns_cancel_callback — cancel an outstanding asyn getdns request"
---

<h2>NAME</h2>
<p> <code>getdns_cancel_callback</code> &#8212; cancel an outstanding asyn getdns request </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_cancel_callback</code> (getdns_context_t context,</p>
<dl>
<dt>
<dd>
 getdns_transaction_t *transaction_id)</dl>
<h2>DESCRIPTION</h2>
<p> To cancel an outstanding callback, use getdns_cancel_callback. This causes the API to call the callback with a callback_type of GETDNS_CALLBACK_CANCEL if the callback for this transaction_id has not already been called. The callback code for cancellation should clean up any memory related to the identified call, such as to deallocate the memory for the userarg. getdns_cancel_callback() may return immediately, even before the callback finishes its work and returns. </p>
<dl>
<dt> <i>context</i></p>
<dd>see getdns_context (3) </p>
<dt> <i>transaction_id</i></p>
<dd>populated by the API and used to identify the callback (for example to getdns_cancel_callback), can be NULL, set to 0 if the function fails </p>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Upon successful completion the functions return <code>GETDNS_RETURN_GOOD</code> , otherwise the following error values are returned: </p>
<p> <code>GETDNS_RETURN_INVALID_PARAMETER</code> if context == NULL </p>
<p> <code>GETDNS_RETURN_UNKNOWN_TRANSACTION </code> if the transaction_id that is unknown or belongs to a callback that has already been called </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>FILES</h2>
<p> /etc/hosts<br />
 /etc/resolv.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3), <code><a href="/docs/linux/man/3-getdns_context/">getdns_context</a></code>(3), <code><a href="/docs/linux/man/3-getdns_general/">getdns_general</a></code>(3), <code><a href="/docs/linux/man/3-getdns_hostname/">getdns_hostname</a></code>(3), <code><a href="/docs/linux/man/3-getdns_service/">getdns_service</a></code>(3), </p>
<h2>Index</h2>
