---
title: "asr_run(3)"
name: "asr_run"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asr_run/"
description: "asr_run, asr_run_sync, asr_abort, res_send_async, res_query_async, res_search_async, getrrsetbyname_async, gethostbyname_async, gethostbyname2_async, gethostbyaddr_async, getnetbyname_async, getnet..."
---

<h2>NAME</h2>
<p> <code>asr_run</code>, <code>asr_run_sync</code>, <code>asr_abort</code>, <code>res_send_async</code>, <code>res_query_async</code>, <code>res_search_async</code>, <code>getrrsetbyname_async</code>, <code>gethostbyname_async</code>, <code>gethostbyname2_async</code>, <code>gethostbyaddr_async</code>, <code>getnetbyname_async</code>, <code>getnetbyaddr_async</code>, <code>getaddrinfo_async</code>, <code>getnameinfo_async</code> &#8211; asynchronous resolver functions</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code> <code>#include &lt;sys/socket.h&gt;</code> <code>#include &lt;netdb.h&gt;</code> <code>#include &lt;asr.h&gt;</code><br />
 <i>int</i><br />
 <code>asr_run</code>(<i>struct asr_query&nbsp;<wbr>*aq</i>, <i>struct asr_result&nbsp;<wbr>*ar</i>);<br />
 <i>int</i><br />
 <code>asr_run_sync</code>(<i>struct asr_query&nbsp;<wbr>*aq</i>, <i>struct asr_result&nbsp;<wbr>*ar</i>);<br />
 <i>void</i><br />
 <code>asr_abort</code>(<i>struct asr_query&nbsp;<wbr>*aq</i>);<br />
 <i>struct asr_query *</i><br />
 <code>res_send_async</code>(<i>const unsigned char&nbsp;<wbr>*pkt</i>, <i>int pktlen</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>res_query_async</code>(<i>const char&nbsp;<wbr>*name</i>, <i>int class</i>, <i>int type</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>res_search_async</code>(<i>const char&nbsp;<wbr>*name</i>, <i>int class</i>, <i>int type</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>getrrsetbyname_async</code>(<i>const char&nbsp;<wbr>*hostname</i>, <i>unsigned int rdclass</i>, <i>unsigned int rdtype</i>, <i>unsigned int flags</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>gethostbyname_async</code>(<i>const char&nbsp;<wbr>*name</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>gethostbyname2_async</code>(<i>const char&nbsp;<wbr>*name</i>, <i>int af</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>gethostbyaddr_async</code>(<i>const void&nbsp;<wbr>*addr</i>, <i>socklen_t len</i>, <i>int af</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>getnetbyname_async</code>(<i>const char&nbsp;<wbr>*name</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>getnetbyaddr_async</code>(<i>in_addr_t net</i>, <i>int type</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>getaddrinfo_async</code>(<i>const char&nbsp;<wbr>*hostname</i>, <i>const char&nbsp;<wbr>*servname</i>, <i>const struct addrinfo&nbsp;<wbr>*hints</i>, <i>void&nbsp;<wbr>*asr</i>);<br />
 <i>struct asr_query *</i><br />
 <code>getnameinfo_async</code>(<i>const struct sockaddr&nbsp;<wbr>*sa</i>, <i>socklen_t salen</i>, <i>char&nbsp;<wbr>*host</i>, <i>size_t hostlen</i>, <i>char&nbsp;<wbr>*serv</i>, <i>size_t servlen</i>, <i>int flags</i>, <i>void&nbsp;<wbr>*asr</i>);</p>
<h2>DESCRIPTION</h2>
<p> The <code>asr</code> functions provide a simple interface for asynchronous address resolution and nameserver querying. They should be used in place of the classical resolver functions of libc when blocking is not desirable. </p>
<p> The principle of operation is as follows: All async requests are made against an <code>asr</code> context which basically defines a list of sources to query and a strategy to do so. The user creates a query through one of the dedicated functions, and gets a handle representing the internal query. A query is a state-machine that can be run to try to fulfill a particular request. This is done by calling in a generic API that performs the state transitions until it needs to give the control back to the user, either because a result is available, or because the next transition implies a blocking call (a file descriptor needs to be read from or written to). The user is responsible for dealing with the situation: either get the result, or wait until the fd conditions are met, and then call back into the resolving machinery when it is ready to proceed. </p>
<p> The <code>asr_run</code>() function drives the resolving process. It runs the asynchronous query represented by the handle until a result is available, or until it cannot continue without blocking. The results are returned to the user through the parameter, which must be a valid pointer to user allocated memory. is defined as:</p>
<dl>
<dt>
<dd>
<pre><code>
struct asr_result {
    /* Fields set if the query is not done yet (asr_run returns 0) */
    int ar_cond;    /* ASR_WANT_READ or ASR_WANT_WRITE */
    int ar_fd;      /* the fd waiting for io condition */
    int ar_timeout; /* time to wait for in milliseconds */
    /* Error fields.  Depends on the query type. */
    int ar_errno;
    int ar_h_errno;
    int ar_gai_errno;
    int ar_rrset_errno;
    /* Result for res_*_async() calls */
    int ar_count;                  /* number of answers in the dns reply */
    int ar_rcode;                  /* response code in the dns reply */
    void *ar_data;                 /* raw reply packet (must be freed) */
    int ar_datalen;                /* reply packet length */
    struct sockaddr_storage ar_ns; /* nameserver that responded */
    /* Result for other calls. Must be freed properly. */
    struct addrinfo *ar_addrinfo;
    struct rrsetinfo *ar_rrsetinfo;
    struct hostent *ar_hostent;
    struct netent *ar_netent;
};

The function returns one of the following values:

0The query cannot be processed further until a specific condition on a
file descriptor becomes true.
The following members of the
structure are filled:


one of ASR_WANT_READ or ASR_WANT_WRITE,the file descriptor waiting for an IO operation,the amount of time to wait for in milliseconds.

The caller is expected to call
asr_run()
again once the condition holds or the timeout expires.

1The query is completed.
The members relevant to the actual async query type are set accordingly,
including error conditions.
In any case, the query is cleared and its handle is invalidated.


Note that although the query itself may fail (the error being properly reported
in the
structure), the
asr_run()
function itself cannot fail and it always preserves errno.
The
asr_run_sync()
function is a wrapper around
asr_run()
that handles the read/write conditions, thus falling back to a blocking
interface.
It only returns 1.
It also preserves errno.
The
asr_abort()
function clears a running query.
It can be called when the query is waiting on a file descriptor.
Note that a completed query is already cleared when
asr_run()
returns, so
asr_abort()
must not be called in this case.
The remaining functions are used to initiate different kinds of query
on the
resolver context.
The specific operational details for each of them are described below.
All functions return a handle to an internal query, or NULL if they could
not allocate the necessary resources to initiate the query.
All other errors (especially invalid parameters) are reported when calling
asr_run().
They usually have the same interface as an existing resolver function, with
an additional
asr
argument, which specifies the context to use for this request.
For now, the argument must always be NULL, which will use the default
context for the current thread.
The
res_send_async(),
res_query_async()
and
res_search_async()
functions are asynchronous versions of the standard libc resolver routines.
Their interface is very similar, except that the response buffer is always
allocated internally.
The return value is found upon completion in the
member of the response structure.
In addition, the
structure contains the address of the DNS server that sent the response,
contains the code returned by the server in the DNS response packet, and
contains the number of answers in the packet.
If a response is received it is placed in a newly allocated buffer
and returned as
member.
This buffer must be freed by the caller.
On error, the
and
members are set accordingly.
The
getrrsetbyname_async()
function is an asynchronous version of
getrrsetbyname(3).
Upon completion, the return code is found in
and the address to the newly allocated result set is set in
As for the blocking function, it must be freed by calling
freerrset(3).
The
gethostbyname_async(),
gethostbyname2_async()
and
gethostbyaddr_async()
functions provide an asynchronous version of the network host entry functions.
Upon completion,
ar_h_errno
is set and the resulting hostent address, if found, is set
in the
ar_hostent
field.
Note that unlike their blocking counterparts, these functions always return a
pointer to newly allocated memory, which must be released by the caller using
free(3).
Similarly, the
getnetbyname_async()
and
getnetbyaddr_async()
functions provide an asynchronous version of the network entry functions.
Upon completion,
ar_h_errno
is set and the resulting netent address, if found, is set
in the
ar_netent
field.
The memory there is also allocated for the request, and it must be freed by
free(3).
The
getaddrinfo_async()
function is an asynchronous version of the
getaddrinfo(3)
call.
It provides a chain of addrinfo structures with all valid combinations of
socket address for the given
,
and
Those three parameters have the same meaning as for the blocking counterpart.
Upon completion the return code is set in
The
member may also be set.
On success, the
member points to a newly allocated list of addrinfo.
This list must be freed with
freeaddrinfo(3).
</code></pre>
<h2>WORKING WITH THREADS</h2>
<p> This implementation of the asynchronous resolver interface is thread-safe and lock-free internally, but the following restriction applies: Two different threads must not create queries on the same context or run queries originating from the same context at the same time. If they want to do that, all calls must be protected by a mutex around that context. </p>
<p> It is generally not a problem since the main point of the asynchronous resolver is to multiplex queries within a single thread of control, so sharing a resolver among threads is not useful.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-getnetbyname/">getnetbyname</a></code>(3), <code><a href="/docs/linux/man/3-getrrsetbyname/">getrrsetbyname</a></code>(3), <code><a href="/docs/linux/man/3-res_send/">res_send</a></code>(3), <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5)</p>
<h2>CAVEATS</h2>
<p> This DNS resolver implementation doesn&#8217;t support the EDNS0 protocol extension yet. </p>
<h2>Index</h2>
