---
title: "xdr_pmap(3)"
name: "xdr_pmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdr_pmap/"
description: "rpc – library routines for remote procedure calls"
---

<p>rpc &#8211; library routines for remote procedure calls</p>
<h2>Synopsis And Description</h2>
<p>These routines allow C programs to make procedure calls on other machines across the network. First, the client calls a procedure to send a data packet to the server. Upon receipt of the packet, the server calls a dispatch routine to perform the requested service, and then sends back a reply. Finally, the procedure call returns to the client. </p>
<p> To take use of these routines, include the header file <i>&lt;rpc/rpc.h&gt;</i>. </p>
<p> The prototypes below make use of the following types: </p>
<dl>
<dd><code>typedef int </code><i>bool_t</i><code>;</code> </p>
<p> <code>typedef bool_t (*</code><i>xdrproc_t</i><code>) (XDR *, void *, &#8230;);</code> </p>
<p> <code>typedef bool_t (*</code><i>resultproc_t</i><code>) (caddr_t </code><i>resp</i><code>,</code> <code> struct sockaddr_in *</code><i>raddr</i><code>);</code></dl>
<p> See the header files for the declarations of the <i>AUTH</i>, <i>CLIENT</i>, <i>SVCXPRT</i>, and <i>XDR</i> types. </p>
<pre><code>void auth_destroy(AUTH *</code><i>auth</i><code>);</code></pre>
<dl>
<dd>A macro that destroys the authentication information associated with <i>auth</i>. Destruction usually involves deallocation of private data structures. The use of <i>auth</i> is undefined after calling <code>auth_destroy</code>().</dl>
<pre><code>AUTH *authnone_create(void);</code></pre>
<dl>
<dd>Create and return an RPC authentication handle that passes nonusable authentication information with each remote procedure call. This is the default authentication used by RPC.</dl>
<pre><code>AUTH *authunix_create(char *</code><i>host</i><code>, int </code><i>uid</i><code>, int </code><i>gid</i><code>,</code>
<code> int </code><i>len</i><code>, int *</code><i>aup_gids</i><code>);</code></pre>
<dl>
<dd>Create and return an RPC authentication handle that contains authentication information. The parameter <i>host</i> is the name of the machine on which the information was created; <i>uid</i> is the user&#8217;s user ID; <i>gid</i> is the user&#8217;s current group ID; <i>len</i> and <i>aup_gids</i> refer to a counted array of groups to which the user belongs. It is easy to impersonate a user.</dl>
<pre><code>AUTH *authunix_create_default(void);</code></pre>
<dl>
<dd>Calls <code>authunix_create</code>() with the appropriate parameters.</dl>
<pre><code>int callrpc(char *</code><i>host</i><code>, unsigned long </code><i>prognum</i><code>,</code>
<code> unsigned long </code><i>versnum</i><code>, unsigned long </code><i>procnum</i><code>,</code>
<code> xdrproc_t </code><i>inproc</i><code>, char *</code><i>in</i><code>,</code>
<code> xdrproc_t </code><i>outproc</i><code>, char *</code><i>out</i><code>);</code></pre>
<dl>
<dd>Call the remote procedure associated with <i>prognum</i>, <i>versnum</i>, and <i>procnum</i> on the machine, <i>host</i>. The parameter <i>in</i> is the address of the procedure&#8217;s argument(s), and <i>out</i> is the address of where to place the result(s); <i>inproc</i> is used to encode the procedure&#8217;s parameters, and <i>outproc</i> is used to decode the procedure&#8217;s results. This routine returns zero if it succeeds, or the value of <code>enum clnt_stat</code> cast to an integer if it fails. The routine <code>clnt_perrno</code>() is handy for translating failure statuses into messages.</p>
<dd>Warning: calling remote procedures with this routine uses UDP/IP as a transport; see <code>clntudp_create</code>() for restrictions. You do not have control of timeouts or authentication using this routine.</dl>
<pre><code>enum clnt_stat clnt_broadcast(unsigned long </code><i>prognum</i><code>,</code>
<code> unsigned long </code><i>versnum</i><code>, unsigned long </code><i>procnum</i><code>,</code>
<code> xdrproc_t </code><i>inproc</i><code>, char *</code><i>in</i><code>,</code>
<code> xdrproc_t </code><i>outproc</i><code>, char *</code><i>out</i><code>,</code>
<code> resultproc_t </code><i>eachresult</i><code>);</code></pre>
<dl>
<dd>Like <code>callrpc</code>(), except the call message is broadcast to all locally connected broadcast nets. Each time it receives a response, this routine calls <code>eachresult</code>(), whose form is:</p>
<dd><code>eachresult(char *</code><i>out</i><code>, struct sockaddr_in *</code><i>addr</i><code>);</code></p>
<dd>where <i>out</i> is the same as <i>out</i> passed to <code>clnt_broadcast</code>(), except that the remote procedure&#8217;s output is decoded there; <i>addr</i> points to the address of the machine that sent the results. If <code>eachresult</code>() returns zero, <code>clnt_broadcast</code>() waits for more replies; otherwise it returns with appropriate status.</p>
<dd>Warning: broadcast sockets are limited in size to the maximum transfer unit of the data link. For ethernet, this value is 1500 bytes.</dl>
<pre><code>enum clnt_stat clnt_call(CLIENT *</code><i>clnt</i><code>, unsigned long </code><i>procnum</i><code>,</code>
<code> xdrproc_t </code><i>inproc</i><code>, char *</code><i>in</i><code>,</code>
<code> xdrproc_t </code><i>outproc</i><code>, char *</code><i>out</i><code>,</code>
<code> struct timeval </code><i>tout</i><code>);</code></pre>
<dl>
<dd>A macro that calls the remote procedure <i>procnum</i> associated with the client handle, <i>clnt</i>, which is obtained with an RPC client creation routine such as <code>clnt_create</code>(). The parameter <i>in</i> is the address of the procedure&#8217;s argument(s), and <i>out</i> is the address of where to place the result(s); <i>inproc</i> is used to encode the procedure&#8217;s parameters, and <i>outproc</i> is used to decode the procedure&#8217;s results; <i>tout</i> is the time allowed for results to come back.</dl>
<pre><code>clnt_destroy(CLIENT *</code><i>clnt</i><code>);</code></pre>
<dl>
<dd>A macro that destroys the client&#8217;s RPC handle. Destruction usually involves deallocation of private data structures, including <i>clnt</i> itself. Use of <i>clnt</i> is undefined after calling <code>clnt_destroy</code>(). If the RPC library opened the associated socket, it will close it also. Otherwise, the socket remains open.</dl>
<pre><code>CLIENT *clnt_create(char *</code><i>host</i><code>, unsigned long </code><i>prog</i><code>,</code>
<code> unsigned long </code><i>vers</i><code>, char *</code><i>proto</i><code>);</code></pre>
<dl>
<dd>Generic client creation routine. <i>host</i> identifies the name of the remote host where the server is located. <i>proto</i> indicates which kind of transport protocol to use. The currently supported values for this field are &#8220;udp&#8221; and &#8220;tcp&#8221;. Default timeouts are set, but can be modified using <code>clnt_control</code>().</p>
<dd>Warning: using UDP has its shortcomings. Since UDP-based RPC messages can hold only up to 8 Kbytes of encoded data, this transport cannot be used for procedures that take large arguments or return huge results.</dl>
<pre><code>bool_t clnt_control(CLIENT *</code><i>cl</i><code>, int </code><i>req</i><code>, char *</code><i>info</i><code>);</code></pre>
<dl>
<dd>A macro used to change or retrieve various information about a client object. <i>req</i> indicates the type of operation, and <i>info</i> is a pointer to the information. For both UDP and TCP, the supported values of <i>req</i> and their argument types and what they do are:</p>
<dd><code>CLSET_TIMEOUT</code> <i>struct timeval</i> // set total timeout <code>CLGET_TIMEOUT</code> <i>struct timeval</i> // get total timeout</p>
<dd>Note: if you set the timeout using <code>clnt_control</code>(), the timeout parameter passed to <code>clnt_call</code>() will be ignored in all future calls.</p>
<dd><code>CLGET_SERVER_ADDR</code> <i>struct sockaddr_in </i> // get server&#8217;s address</p>
<dd>The following operations are valid for UDP only:</p>
<dd><code>CLSET_RETRY_TIMEOUT</code> <i>struct timeval</i> // set the retry timeout <code>CLGET_RETRY_TIMEOUT</code> <i>struct timeval</i> // get the retry timeout</p>
<dd>The retry timeout is the time that &quot;UDP RPC&quot; waits for the server to reply before retransmitting the request.</dl>
<pre><code>clnt_freeres(CLIENT * </code><i>clnt</i><code>, xdrproc_t </code><i>outproc</i><code>, char *</code><i>out</i><code>);</code></pre>
<dl>
<dd>A macro that frees any data allocated by the RPC/XDR system when it decoded the results of an RPC call. The parameter <i>out</i> is the address of the results, and <i>outproc</i> is the XDR routine describing the results. This routine returns one if the results were successfully freed, and zero otherwise.</dl>
<pre><code>void clnt_geterr(CLIENT *</code><i>clnt</i><code>, struct rpc_err *</code><i>errp</i><code>);</code></pre>
<dl>
<dd>A macro that copies the error structure out of the client handle to the structure at address <i>errp</i>.</dl>
<pre><code>void clnt_pcreateerror(char *</code><i>s</i><code>);</code></pre>
<dl>
<dd>Print a message to standard error indicating why a client RPC handle could not be created. The message is prepended with string <i>s</i> and a colon. Used when a <code>clnt_create</code>(), <code>clntraw_create</code>(), <code>clnttcp_create</code>(), or <code>clntudp_create</code>() call fails.</dl>
<pre><code>void clnt_perrno(enum clnt_stat </code><i>stat</i><code>);</code></pre>
<dl>
<dd>Print a message to standard error corresponding to the condition indicated by <i>stat</i>. Used after <code>callrpc</code>().</dl>
<pre><code>clnt_perror(CLIENT *</code><i>clnt</i><code>, char *</code><i>s</i><code>);</code></pre>
<dl>
<dd>Print a message to standard error indicating why an RPC call failed; <i>clnt</i> is the handle used to do the call. The message is prepended with string <i>s</i> and a colon. Used after <code>clnt_call</code>().</dl>
<pre><code>char *clnt_spcreateerror(char *</code><i>s</i><code>);</code></pre>
<dl>
<dd>Like <code>clnt_pcreateerror</code>(), except that it returns a string instead of printing to the standard error.</p>
<dd>Bugs: returns pointer to static data that is overwritten on each call.</dl>
<pre><code>char *clnt_sperrno(enum clnt_stat </code><i>stat</i><code>);</code></pre>
<dl>
<dd>Take the same arguments as <code>clnt_perrno</code>(), but instead of sending a message to the standard error indicating why an RPC call failed, return a pointer to a string which contains the message. The string ends with a NEWLINE.</p>
<dd><code>clnt_sperrno</code>() is used instead of <code>clnt_perrno</code>() if the program does not have a standard error (as a program running as a server quite likely does not), or if the programmer does not want the message to be output with <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), or if a message format different than that supported by <code>clnt_perrno</code>() is to be used. Note: unlike <code>clnt_sperror</code>() and <code>clnt_spcreateerror</code>(), <code>clnt_sperrno</code>() returns pointer to static data, but the result will not get overwritten on each call.</dl>
<pre><code>char *clnt_sperror(CLIENT *</code><i>rpch</i><code>, char *</code><i>s</i><code>);</code></pre>
<dl>
<dd>Like <code>clnt_perror</code>(), except that (like <code>clnt_sperrno</code>()) it returns a string instead of printing to standard error.</p>
<dd>Bugs: returns pointer to static data that is overwritten on each call.</dl>
<pre><code>CLIENT *clntraw_create(unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>);</code></pre>
<dl>
<dd>This routine creates a toy RPC client for the remote program <i>prognum</i>, version <i>versnum</i>. The transport used to pass messages to the service is actually a buffer within the process&#8217;s address space, so the corresponding RPC server should live in the same address space; see <code>svcraw_create</code>(). This allows simulation of RPC and acquisition of RPC overheads, such as round trip times, without any kernel interference. This routine returns NULL if it fails.</dl>
<pre><code>CLIENT *clnttcp_create(struct sockaddr_in *</code><i>addr</i><code>,</code>
<code> unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> int *</code><i>sockp</i><code>, unsigned int </code><i>sendsz</i><code>, unsigned int </code><i>recvsz</i><code>);</code></pre>
<dl>
<dd>This routine creates an RPC client for the remote program <i>prognum</i>, version <i>versnum</i>; the client uses TCP/IP as a transport. The remote program is located at Internet address <i>*addr</i>. If <i>addr-&gt;sin_port</i> is zero, then it is set to the actual port that the remote program is listening on (the remote <code>portmap</code> service is consulted for this information). The parameter <i>sockp</i> is a socket; if it is <code>RPC_ANYSOCK</code>, then this routine opens a new one and sets <i>sockp</i>. Since TCP-based RPC uses buffered I/O, the user may specify the size of the send and receive buffers with the parameters <i>sendsz</i> and <i>recvsz</i>; values of zero choose suitable defaults. This routine returns NULL if it fails.</dl>
<pre><code>CLIENT *clntudp_create(struct sockaddr_in *</code><i>addr</i><code>,</code>
<code> unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> struct timeval </code><i>wait</i><code>, int *</code><i>sockp</i><code>);</code></pre>
<dl>
<dd>This routine creates an RPC client for the remote program <i>prognum</i>, version <i>versnum</i>; the client uses use UDP/IP as a transport. The remote program is located at Internet address <i>addr</i>. If <i>addr-&gt;sin_port</i> is zero, then it is set to actual port that the remote program is listening on (the remote <code>portmap</code> service is consulted for this information). The parameter <i>sockp</i> is a socket; if it is <code>RPC_ANYSOCK</code>, then this routine opens a new one and sets <i>sockp</i>. The UDP transport resends the call message in intervals of <i>wait</i> time until a response is received or until the call times out. The total time for the call to time out is specified by <code>clnt_call</code>().</p>
<dd>Warning: since UDP-based RPC messages can hold only up to 8 Kbytes of encoded data, this transport cannot be used for procedures that take large arguments or return huge results.</dl>
<pre><code>CLIENT *clntudp_bufcreate(struct sockaddr_in *</code><i>addr</i><code>,</code>
<code> unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> struct timeval </code><i>wait</i><code>, int *</code><i>sockp</i><code>,</code>
<code> unsigned int </code><i>sendsize</i><code>, unsigned int recosize</code><i>);</i></pre>
<dl>
<dd>This routine creates an RPC client for the remote program <i>prognum</i>, on <i>versnum</i>; the client uses use UDP/IP as a transport. The remote program is located at Internet address <i>addr</i>. If <i>addr-&gt;sin_port</i> is zero, then it is set to actual port that the remote program is listening on (the remote <code>portmap</code> service is consulted for this information). The parameter <i>sockp</i> is a socket; if it is <code>RPC_ANYSOCK</code>, then this routine opens a new one and sets <i>sockp</i>. The UDP transport resends the call message in intervals of <i>wait</i> time until a response is received or until the call times out. The total time for the call to time out is specified by <code>clnt_call</code>().</p>
<dd>This allows the user to specify the maximum packet size for sending and receiving UDP-based RPC messages.</dl>
<pre><code>void get_myaddress(struct sockaddr_in *</code><i>addr</i><code>);</code></pre>
<dl>
<dd>Stuff the machine&#8217;s IP address into <i>*addr</i>, without consulting the library routines that deal with <i>/etc/hosts</i>. The port number is always set to <code>htons(PMAPPORT)</code>.</dl>
<pre><code>struct pmaplist *pmap_getmaps(struct sockaddr_in *</code><i>addr</i><code>);</code></pre>
<dl>
<dd>A user interface to the <code>portmap</code> service, which returns a list of the current RPC program-to-port mappings on the host located at IP address <i>*addr</i>. This routine can return NULL. The command <i>rpcinfo -p</i> uses this routine.</dl>
<pre><code>unsigned short pmap_getport(struct sockaddr_in *</code><i>addr</i><code>,</code>
<code> unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> unsigned int </code><i>protocol</i><code>);</code></pre>
<dl>
<dd>A user interface to the <code>portmap</code> service, which returns the port number on which waits a service that supports program number <i>prognum</i>, version <i>versnum</i>, and speaks the transport protocol associated with <i>protocol</i>. The value of <i>protocol</i> is most likely <code>IPPROTO_UDP</code> or <code>IPPROTO_TCP</code>. A return value of zero means that the mapping does not exist or that the RPC system failed to contact the remote <code>portmap</code> service. In the latter case, the global variable <i>rpc_createerr</i> contains the RPC status.</dl>
<pre><code>enum clnt_stat pmap_rmtcall(struct sockaddr_in *</code><i>addr</i><code>,</code>
<code> unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> unsigned long </code><i>procnum</i><code>,</code>
<code> xdrproc_t </code><i>inproc</i><code>, char *</code><i>in</i><code>,</code>
<code> xdrproc_t </code><i>outproc</i><code>, char *</code><i>out</i><code>,</code>
<code> struct timeval </code><i>tout</i><code>, unsigned long *</code><i>portp</i><code>);</code></pre>
<dl>
<dd>A user interface to the <code>portmap</code> service, which instructs <code>portmap</code> on the host at IP address <i>*addr</i> to make an RPC call on your behalf to a procedure on that host. The parameter <i>*portp</i> will be modified to the program&#8217;s port number if the procedure succeeds. The definitions of other parameters are discussed in <code>callrpc</code>() and <code>clnt_call</code>(). This procedure should be used for a &#8220;ping&#8221; and nothing else. See also <code>clnt_broadcast</code>().</dl>
<pre><code>bool_t pmap_set(unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> unsigned int </code><i>protocol</i><code>, unsigned short </code><i>port</i><code>);</code></pre>
<dl>
<dd>A user interface to the <code>portmap</code> service, which establishes a mapping between the triple [<i>prognum</i>,<i>versnum</i>,<i>protocol</i>] and <i>port</i> on the machine&#8217;s <code>portmap</code> service. The value of <i>protocol</i> is most likely <code>IPPROTO_UDP</code> or <code>IPPROTO_TCP</code>. This routine returns one if it succeeds, zero otherwise. Automatically done by <code>svc_register</code>().</dl>
<pre><code>bool_t pmap_unset(unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>);</code></pre>
<dl>
<dd>A user interface to the <code>portmap</code> service, which destroys all mapping between the triple [<i>prognum</i>,<i>versnum</i>,<i>*</i>] and <code>ports</code> on the machine&#8217;s <code>portmap</code> service. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>int registerrpc(unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>,</code>
<code> unsigned long </code><i>procnum</i><code>, char *(*</code><i>procname</i><code>)(char *),</code>
<code> xdrproc_t </code><i>inproc</i><code>, xdrproc_t </code><i>outproc</i><code>);</code></pre>
<dl>
<dd>Register procedure <i>procname</i> with the RPC service package. If a request arrives for program <i>prognum</i>, version <i>versnum</i>, and procedure <i>procnum</i>, <i>procname</i> is called with a pointer to its parameter(s); <i>procname</i> should return a pointer to its static result(s); <i>inproc</i> is used to decode the parameters while <i>outproc</i> is used to encode the results. This routine returns zero if the registration succeeded, -1 otherwise.</p>
<dd>Warning: remote procedures registered in this form are accessed using the UDP/IP transport; see <code>svcudp_create</code>() for restrictions.</dl>
<pre><code>struct rpc_createerr </code><i>rpc_createerr</i><code>;</code></pre>
<dl>
<dd>A global variable whose value is set by any RPC client creation routine that does not succeed. Use the routine <code>clnt_pcreateerror</code>() to print the reason why.</dl>
<pre><code>void svc_destroy(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>A macro that destroys the RPC service transport handle, <i>xprt</i>. Destruction usually involves deallocation of private data structures, including <i>xprt</i> itself. Use of <i>xprt</i> is undefined after calling this routine.</dl>
<pre><code>fd_set </code><i>svc_fdset</i><code>;</code></pre>
<dl>
<dd>A global variable reflecting the RPC service side&#8217;s read file descriptor bit mask; it is suitable as a parameter to the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) system call. This is of interest only if a service implementor does their own asynchronous event processing, instead of calling <code>svc_run</code>(). This variable is read-only (do not pass its address to <code><a href="/docs/linux/man/2-select/">select</a></code>(2)!), yet it may change after calls to <code>svc_getreqset</code>() or any creation routines.</dl>
<pre><code>int </code><i>svc_fds</i><code>;</code></pre>
<dl>
<dd>Similar to <code>svc_fdset</code>, but limited to 32 file descriptors. This interface is obsoleted by <code>svc_fdset</code>.</dl>
<pre><code>svc_freeargs(SVCXPRT *</code><i>xprt</i><code>, xdrproc_t </code><i>inproc</i><code>, char *</code><i>in</i><code>);</code></pre>
<dl>
<dd>A macro that frees any data allocated by the RPC/XDR system when it decoded the arguments to a service procedure using <code>svc_getargs</code>(). This routine returns 1 if the results were successfully freed, and zero otherwise.</dl>
<pre><code>svc_getargs(SVCXPRT *</code><i>xprt</i><code>, xdrproc_t </code><i>inproc</i><code>, char *</code><i>in</i><code>);</code></pre>
<dl>
<dd>A macro that decodes the arguments of an RPC request associated with the RPC service transport handle, <i>xprt</i>. The parameter <i>in</i> is the address where the arguments will be placed; <i>inproc</i> is the XDR routine used to decode the arguments. This routine returns one if decoding succeeds, and zero otherwise.</dl>
<pre><code>struct sockaddr_in *svc_getcaller(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>The approved way of getting the network address of the caller of a procedure associated with the RPC service transport handle, <i>xprt</i>.</dl>
<pre><code>void svc_getreqset(fd_set *</code><i>rdfds</i><code>);</code></pre>
<dl>
<dd>This routine is of interest only if a service implementor does not call <code>svc_run</code>(), but instead implements custom asynchronous event processing. It is called when the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) system call has determined that an RPC request has arrived on some RPC socket(s); <i>rdfds</i> is the resultant read file descriptor bit mask. The routine returns when all sockets associated with the value of <i>rdfds</i> have been serviced.</dl>
<pre><code>void svc_getreq(int </code><i>rdfds</i><code>);</code></pre>
<dl>
<dd>Similar to <code>svc_getreqset</code>(), but limited to 32 file descriptors. This interface is obsoleted by <code>svc_getreqset</code>().</dl>
<pre><code>bool_t svc_register(SVCXPRT *</code><i>xprt</i><code>, unsigned long </code><i>prognum</i><code>,</code>
<code> unsigned long </code><i>versnum</i><code>,</code>
<code> void (*</code><i>dispatch</i><code>)(svc_req *, SVCXPRT *),</code>
<code> unsigned long </code><i>protocol</i><code>);</code></pre>
<dl>
<dd>Associates <i>prognum</i> and <i>versnum</i> with the service dispatch procedure, <i>dispatch</i>. If <i>protocol</i> is zero, the service is not registered with the <code>portmap</code> service. If <i>protocol</i> is nonzero, then a mapping of the triple [<i>prognum</i>,<i>versnum</i>,<i>protocol</i>] to <i>xprt-&gt;xp_port</i> is established with the local <code>portmap</code> service (generally <i>protocol</i> is zero, <code>IPPROTO_UDP</code> or <code>IPPROTO_TCP</code>). The procedure <i>dispatch</i> has the following form:</p>
<dd>dispatch(struct svc_req *request, SVCXPRT *xprt);</p>
<dd>The <code>svc_register</code>() routine returns one if it succeeds, and zero otherwise.</dl>
<pre><code>void svc_run(void);</code></pre>
<dl>
<dd>This routine never returns. It waits for RPC requests to arrive, and calls the appropriate service procedure using <code>svc_getreq</code>() when one arrives. This procedure is usually waiting for a <code><a href="/docs/linux/man/2-select/">select</a></code>(2) system call to return.</dl>
<pre><code>bool_t svc_sendreply(SVCXPRT *</code><i>xprt</i><code>, xdrproc_t </code><i>outproc</i><code>, char *</code><i>out</i><code>);</code></pre>
<dl>
<dd>Called by an RPC service&#8217;s dispatch routine to send the results of a remote procedure call. The parameter <i>xprt</i> is the request&#8217;s associated transport handle; <i>outproc</i> is the XDR routine which is used to encode the results; and <i>out</i> is the address of the results. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>void svc_unregister(unsigned long </code><i>prognum</i><code>, unsigned long </code><i>versnum</i><code>);</code></pre>
<dl>
<dd>Remove all mapping of the double [<i>prognum</i>,<i>versnum</i>] to dispatch routines, and of the triple [<i>prognum</i>,<i>versnum</i>,<i>*</i>] to port number.</dl>
<pre><code>void svcerr_auth(SVCXPRT *</code><i>xprt</i><code>, enum auth_stat </code><i>why</i><code>);</code></pre>
<dl>
<dd>Called by a service dispatch routine that refuses to perform a remote procedure call due to an authentication error.</dl>
<pre><code>void svcerr_decode(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Called by a service dispatch routine that cannot successfully decode its parameters. See also <code>svc_getargs</code>().</dl>
<pre><code>void svcerr_noproc(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Called by a service dispatch routine that does not implement the procedure number that the caller requests.</dl>
<pre><code>void svcerr_noprog(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Called when the desired program is not registered with the RPC package. Service implementors usually do not need this routine.</dl>
<pre><code>void svcerr_progvers(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Called when the desired version of a program is not registered with the RPC package. Service implementors usually do not need this routine.</dl>
<pre><code>void svcerr_systemerr(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Called by a service dispatch routine when it detects a system error not covered by any particular protocol. For example, if a service can no longer allocate storage, it may call this routine.</dl>
<pre><code>void svcerr_weakauth(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Called by a service dispatch routine that refuses to perform a remote procedure call due to insufficient authentication parameters. The routine calls <code>svcerr_auth(xprt, AUTH_TOOWEAK)</code>.</dl>
<pre><code>SVCXPRT *svcfd_create(int </code><i>fd</i><code>, unsigned int </code><i>sendsize</i><code>,</code>
<code> unsigned int </code><i>recvsize</i><code>);</code></pre>
<dl>
<dd>Create a service on top of any open file descriptor. Typically, this file descriptor is a connected socket for a stream protocol such as TCP. <i>sendsize</i> and <i>recvsize</i> indicate sizes for the send and receive buffers. If they are zero, a reasonable default is chosen.</dl>
<pre><code>SVCXPRT *svcraw_create(void);</code></pre>
<dl>
<dd>This routine creates a toy RPC service transport, to which it returns a pointer. The transport is really a buffer within the process&#8217;s address space, so the corresponding RPC client should live in the same address space; see <code>clntraw_create</code>(). This routine allows simulation of RPC and acquisition of RPC overheads (such as round trip times), without any kernel interference. This routine returns NULL if it fails.</dl>
<pre><code>SVCXPRT *svctcp_create(int </code><i>sock</i><code>, unsigned int </code><i>send_buf_size</i><code>,</code>
<code> unsigned int </code><i>recv_buf_size</i><code>);</code></pre>
<dl>
<dd>This routine creates a TCP/IP-based RPC service transport, to which it returns a pointer. The transport is associated with the socket <i>sock</i>, which may be <code>RPC_ANYSOCK</code>, in which case a new socket is created. If the socket is not bound to a local TCP port, then this routine binds it to an arbitrary port. Upon completion, <i>xprt-&gt;xp_sock</i> is the transport&#8217;s socket descriptor, and <i>xprt-&gt;xp_port</i> is the transport&#8217;s port number. This routine returns NULL if it fails. Since TCP-based RPC uses buffered I/O, users may specify the size of buffers; values of zero choose suitable defaults.</dl>
<pre><code>SVCXPRT *svcudp_bufcreate(int </code><i>sock</i><code>, unsigned int </code><i>sendsize</i><code>,</code>
<code> unsigned int </code><i>recosize</i><code>);</code></pre>
<dl>
<dd>This routine creates a UDP/IP-based RPC service transport, to which it returns a pointer. The transport is associated with the socket <i>sock</i>, which may be <code>RPC_ANYSOCK</code>, in which case a new socket is created. If the socket is not bound to a local UDP port, then this routine binds it to an arbitrary port. Upon completion, <i>xprt-&gt;xp_sock</i> is the transport&#8217;s socket descriptor, and <i>xprt-&gt;xp_port</i> is the transport&#8217;s port number. This routine returns NULL if it fails.</p>
<dd>This allows the user to specify the maximum packet size for sending and receiving UDP-based RPC messages.</dl>
<pre><code>SVCXPRT *svcudp_create(int </code><i>sock</i><code>);</code></pre>
<dl>
<dd>This call is equivalent to <i>svcudp_bufcreate(sock,SZ,SZ)</i> for some default size <i>SZ</i>.</dl>
<pre><code>bool_t xdr_accepted_reply(XDR *</code><i>xdrs</i><code>, struct accepted_reply *</code><i>ar</i><code>);</code></pre>
<dl>
<dd>Used for encoding RPC reply messages. This routine is useful for users who wish to generate RPC-style messages without using the RPC package.</dl>
<pre><code>bool_t xdr_authunix_parms(XDR *</code><i>xdrs</i><code>, struct authunix_parms *</code><i>aupp</i><code>);</code></pre>
<dl>
<dd>Used for describing UNIX credentials. This routine is useful for users who wish to generate these credentials without using the RPC authentication package.</dl>
<pre><code>void xdr_callhdr(XDR *</code><i>xdrs</i><code>, struct rpc_msg *</code><i>chdr</i><code>);</code></pre>
<dl>
<dd>Used for describing RPC call header messages. This routine is useful for users who wish to generate RPC-style messages without using the RPC package.</dl>
<pre><code>bool_t xdr_callmsg(XDR *</code><i>xdrs</i><code>, struct rpc_msg *</code><i>cmsg</i><code>);</code></pre>
<dl>
<dd>Used for describing RPC call messages. This routine is useful for users who wish to generate RPC-style messages without using the RPC package.</dl>
<pre><code>bool_t xdr_opaque_auth(XDR *</code><i>xdrs</i><code>, struct opaque_auth *</code><i>ap</i><code>);</code></pre>
<dl>
<dd>Used for describing RPC authentication information messages. This routine is useful for users who wish to generate RPC-style messages without using the RPC package.</dl>
<pre><code>bool_t xdr_pmap(XDR *</code><i>xdrs</i><code>, struct pmap *</code><i>regs</i><code>);</code></pre>
<dl>
<dd>Used for describing parameters to various <code>portmap</code> procedures, externally. This routine is useful for users who wish to generate these parameters without using the <code>pmap</code> interface.</dl>
<pre><code>bool_t xdr_pmaplist(XDR *</code><i>xdrs</i><code>, struct pmaplist **</code><i>rp</i><code>);</code></pre>
<dl>
<dd>Used for describing a list of port mappings, externally. This routine is useful for users who wish to generate these parameters without using the <code>pmap</code> interface.</dl>
<pre><code>bool_t xdr_rejected_reply(XDR *</code><i>xdrs</i><code>, struct rejected_reply *</code><i>rr</i><code>);</code></pre>
<dl>
<dd>Used for describing RPC reply messages. This routine is useful for users who wish to generate RPC-style messages without using the RPC package.</dl>
<pre><code>bool_t xdr_replymsg(XDR *</code><i>xdrs</i><code>, struct rpc_msg *</code><i>rmsg</i><code>);</code></pre>
<dl>
<dd>Used for describing RPC reply messages. This routine is useful for users who wish to generate RPC style messages without using the RPC package.</dl>
<pre><code>void xprt_register(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>After RPC service transport handles are created, they should register themselves with the RPC service package. This routine modifies the global variable <i>svc_fds</i>. Service implementors usually do not need this routine.</dl>
<pre><code>void xprt_unregister(SVCXPRT *</code><i>xprt</i><code>);</code></pre>
<dl>
<dd>Before an RPC service transport handle is destroyed, it should unregister itself with the RPC service package. This routine modifies the global variable <i>svc_fds</i>. Service implementors usually do not need this routine.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>auth_destroy</code>(), <code>authnone_create</code>(),<br />
 <code>authunix_create</code>(),<br />
 <code>authunix_create_default</code>(),<br />
 <code>callrpc</code>(), <code>clnt_broadcast</code>(),<br />
 <code>clnt_call</code>(), <code>clnt_destroy</code>(),<br />
 <code>clnt_create</code>(), <code>clnt_control</code>(),<br />
 <code>clnt_freeres</code>(), <code>clnt_geterr</code>(),<br />
 <code>clnt_pcreateerror</code>(), <code>clnt_perrno</code>(),<br />
 <code>clnt_perror</code>(),<br />
 <code>clnt_spcreateerror</code>(),<br />
 <code>clnt_sperrno</code>(), <code>clnt_sperror</code>(),<br />
 <code>clntraw_create</code>(), <code>clnttcp_create</code>(),<br />
 <code>clntudp_create</code>(),<br />
 <code>clntudp_bufcreate</code>(),<br />
 <code>get_myaddress</code>(), <code>pmap_getmaps</code>(),<br />
 <code>pmap_getport</code>(), <code>pmap_rmtcall</code>(),<br />
 <code>pmap_set</code>(), <code>pmap_unset</code>(),<br />
 <code>registerrpc</code>(), <code>svc_destroy</code>(),<br />
 <code>svc_freeargs</code>(), <code>svc_getargs</code>(),<br />
 <code>svc_getcaller</code>(), <code>svc_getreqset</code>(),<br />
 <code>svc_getreq</code>(), <code>svc_register</code>(),<br />
 <code>svc_run</code>(), <code>svc_sendreply</code>(),<br />
 <code>svc_unregister</code>(), <code>svcerr_auth</code>(),<br />
 <code>svcerr_decode</code>(), <code>svcerr_noproc</code>(),<br />
 <code>svcerr_noprog</code>(), <code>svcerr_progvers</code>(),<br />
 <code>svcerr_systemerr</code>(), <code>svcerr_weakauth</code>(),<br />
 <code>svcfd_create</code>(), <code>svcraw_create</code>(),<br />
 <code>svctcp_create</code>(),<br />
 <code>svcudp_bufcreate</code>(),<br />
 <code>svcudp_create</code>(), <code>xdr_accepted_reply</code>(),<br />
 <code>xdr_authunix_parms</code>(),<br />
 <code>xdr_callhdr</code>(),<br />
 <code>xdr_callmsg</code>(), <code>xdr_opaque_auth</code>(),<br />
 <code>xdr_pmap</code>(), <code>xdr_pmaplist</code>(),<br />
 <code>xdr_rejected_reply</code>(),<br />
 <code>xdr_replymsg</code>(),<br />
 <code>xprt_register</code>(), <code>xprt_unregister</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xdr/">xdr</a></code>(3) </p>
<p> The following manuals:</p>
<dl>
<dd>Remote Procedure Calls: Protocol Specification<br />
 Remote Procedure Call Programming Guide<br />
 rpcgen Programming Guide
</dl>
<p> <i>RPC: Remote Procedure Call Protocol Specification</i>, RFC 1050, Sun Microsystems, Inc., USC-ISI.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
