---
title: "pmdatrace(3)"
name: "pmdatrace"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdatrace/"
description: "pmtracebegin, pmtraceend, pmtraceabort, pmtracepoint, pmtraceobs, pmtracecounter, pmtracestate, pmtraceerrstr – application-level performance instrumentation services"
---

<p><code>pmtracebegin</code>, <code>pmtraceend</code>, <code>pmtraceabort</code>, <code>pmtracepoint</code>, <code>pmtraceobs</code>, <code>pmtracecounter</code>, <code>pmtracestate</code>, <code>pmtraceerrstr</code> &#8211; application-level performance instrumentation services</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/trace.h&gt; </p>
<p> </code></p>
<pre>int pmtracebegin(const char *<i>tag</i>);
int pmtraceend(const char *<i>tag</i>);
int pmtraceabort(const char *<i>tag</i>);
int pmtracepoint(const char *<i>tag</i>);
int pmtraceobs(const char *<i>tag</i>, double <i>value</i>);
int pmtracecounter(const char *<i>tag</i>, double <i>value</i>);
char *pmtraceerrstr(int <i>code</i>);
int pmtracestate(int <i>flags</i>);</pre>
<p>cc &#8230; -lpcp_trace</p>
<h2>Fortran Synopsis</h2>
<pre>character*(*) <i>tag</i>
integer <i>code</i>
integer <i>flags</i>
integer <i>state</i>
character*(*) <i>estr</i>
real*8 <i>value</i></pre>
<pre><i>code</i> = pmtracebegin(<i>tag</i>)
<i>code</i> = pmtraceend(<i>tag</i>)
<i>code</i> = pmtraceabort(<i>tag</i>)
<i>code</i> = pmtracepoint(<i>tag</i>)
<i>code</i> = pmtraceobs(<i>tag</i>, <i>value</i>)
<i>code</i> = pmtracecounter(<i>tag</i>, <i>value</i>)
pmtraceerrstr(<i>code</i>, <i>estr</i>)
<i>state</i> = pmtracestate(<i>flags</i>)</pre>
<pre>f77 ... -lpcp_trace or<code> f90 ... -lpcp_trace
</code></pre>
<h2>Java Synopsis</h2>
<pre>import sgi.pcp.trace;
int trace.pmtracebegin(String <i>tag</i>);
int trace.pmtraceend(String <i>tag</i>);
int trace.pmtraceabort(String <i>tag</i>);
int trace.pmtracepoint(String <i>tag</i>);
int trace.pmtraceobs(String <i>tag</i>, double <i>value</i>);
int trace.pmtracecounter(String <i>tag</i>, double <i>value</i>);
String trace.pmtraceerrstr(int <i>code</i>);
int trace.pmtracestate(int <i>flags</i>);</pre>
<h2>Description</h2>
<p>The <i>pcp_trace</i> library functions provide a mechanism for identifying sections of a program as transactions or events for use by the trace Performance Metrics Domain Agent (refer to <code><a href="/docs/linux/man/1-pmdatrace/">pmdatrace</a></code>(1) and <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)). </p>
<p> The monitoring of transactions using the Performance Co-Pilot (PCP) infrastructure is initiated through a call to <code>pmtracebegin</code>. Time will be recorded from the end of each <code>pmtracebegin</code> call to the start of the following call to <code>pmtraceend</code>, where the same <i>tag</i> identifier is used in both calls. Following from this, no visible recording will occur until at least one call to <code>pmtraceend</code> is made referencing a <i>tag</i> previously used in a call to <code>pmtracebegin</code>. </p>
<p> A transaction which is currently in progress can be cancelled by calling <code>pmtraceabort</code>. No transaction data gathered for that particular transaction will be exported, although data from previous and subsequent successful transactions with that <i>tag</i> name are still exported. This is most useful when an error condition arises during transaction processing and the transaction does not run to completion. </p>
<p> The <i>tag</i> argument to <code>pmtracebegin</code>, <code>pmtraceend</code> and <code>pmtraceabort</code> is used to uniquely identify each transaction within the <i>pcp_trace</i> library and later by the trace PMDA as the instance domain identifiers for the transaction performance metrics which it exports. These routines are most useful when used around blocks of code which are likely to be executed a number of times over some relatively long time period (in a daemon process, for example). </p>
<p> <code>pmtracebegin</code> has two distinct roles &#8211; firstly as the initiator of a new transaction, and secondly as a mechanism for setting a new start time. Similarly, <code>pmtraceend</code> is used to register a new <i>tag</i> and its initial state with the trace PMDA, or alternatively to update the statistics which the PMDA currently associates with the given <i>tag</i>. </p>
<p> A second form of program instrumentation can be obtained from <code>pmtracepoint</code>. This is a simpler form of monitoring as it exports only the number of times that a particular point in a program has been passed. This differs to the transaction monitoring offered by <code>pmtracebegin</code> and <code>pmtraceend</code>, which exports a running count of successful transaction completions as well as statistics on the time interval between the start and end points of each transaction. This function is most useful when start and end points are not well defined. Examples of this would be when the code branches in such a way that a transaction cannot be clearly identified, or when processing does not follow a transactional model, or the desired instrumentation is akin to event rates rather than event service times. </p>
<p> The <code>pmtraceobs</code> and <code>pmtracecounter</code> functions have similar semantics to <code>pmtracepoint</code>, but also allow an arbitrary numeric <i>value</i> to be passed to the trace PMDA. The most recent <i>value</i> for each <i>tag</i> is then immediately available from the PMDA. The only difference between <code>pmtraceobs</code> and <code>pmtracecounter</code> is that the value exported via <code>pmtracecounter</code> is assumed to be a monotonically increasing counter value (e.g. the number of bytes read from a socket), whereas the value exported via <code>pmtraceobs</code> can be any value at all. </p>
<p> <code>pmtracestate</code> allows the application to set state <i>flags</i> which are honoured by subsequent calls to the <i>pcp_trace</i> library routines. There are currently two types of flag &#8211; debugging flags and the asynchronous protocol flag. A single call may specify a number of <i>flags</i> together, combined using a (bitwise) logical OR operation, and overrides the previous state setting. </p>
<p> The debugging flags to <code>pmtracestate</code> cause <i>pcp_trace</i> to print diagnostic messages on the standard output stream at important processing points. The default protocol used between the trace PMDA and individual <i>pcp_trace</i> client applications is a synchronous protocol, which allows for dropped connections to be reestablished at a later stage should this become possible. An asynchronous protocol is also available which does not provide the reconnection capability, but which does away with much of the overhead inherent in synchronous communication. This behaviour can be toggled using the <code>pmtracestate</code> call, but must be called before other calls to the library. This differs to the debugging state behaviour, which can be altered at any time. <code>pmtracestate</code> returns the previous state (setting prior to being called). </p>
<p> The following table describes each of the <code>pmtracestate</code> <i>flags</i> &#8211; examples of the use of these flags in each supported language are given in the demo applications (refer to the &#8220;FILES&#8221; section below). <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>State Flags</td>
<td ALIGN=center>Semantics
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>0 NONE</td>
<td>Synchronous PDUs and no diagnostics (default)
</td>
</tr>
<tr VALIGN=top>
<td>1 API</td>
<td>Shows processing just below the API (debug)
</td>
</tr>
<tr VALIGN=top>
<td>2 COMMS</td>
<td>Shows network-related activity (debug)
</td>
</tr>
<tr VALIGN=top>
<td>4 PDU</td>
<td>Shows app&lt;-&gt;PMDA IPC traffic (debug)
</td>
</tr>
<tr VALIGN=top>
<td>8 PDUBUF</td>
<td>Shows internal IPC buffer management (debug)
</td>
</tr>
<tr VALIGN=top>
<td>16 NOAGENT</td>
<td>No PMDA communications at all (debug)
</td>
</tr>
<tr VALIGN=top>
<td>32 ASYNC</td>
<td>Use the asynchronous PDU protocol (control)
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Should any of the <i>pcp_trace</i> library functions return a negative value, an error has occurred. This can be diagnosed further using the <code>pmtraceerrstr</code> routine, which takes the negative return value as its <i>code</i> argument, and in the C-callable interface returns a pointer to the associated error message. This points into a static error table, and should therefore not be passed to <code><a href="/docs/linux/man/3-free/">free</a></code>(3). The Fortran-callable interface has a slightly different syntax, requiring the destination character array to be passed in as the second argument. The Java-callable interface returns a UTF-8 string, created using the JNI (Java Native Interface) routine <code>NewStringUTF</code>.</p>
<h2>Environment</h2>
<p>The <i>pcp_trace</i> routines communicate with the trace PMDA via a socket connection, which by default uses TCP/IP port number 4323. This can be over-ridden by setting <code>PCP_TRACE_PORT</code> to a different port number when the application is started. The host where the trace PMDA is running is by default the localhost, but this can be changed using <code>PCP_TRACE_HOST</code>. When attempting to connect to a remote trace PMDA, after some specified time interval has elapsed, the connection attempt will be aborted and an error status will be returned. The default timeout interval is 3 seconds, and this can be modified by setting <code>PCP_TRACE_TIMEOUT</code> in the environment to a real number of seconds for the desired timeout. This is most useful in cases where the remote host is at the end of a slow network, requiring longer latencies to establish the connection correctly.</p>
<h2>Notes</h2>
<p>The <i>pcp_trace</i> Java class interface has been developed and verified using version 1.1 of the Java Native Interface (JNI) specification.</p>
<h2>Files</h2>
<dl>
<dt><code>$PCP_DEMOS_DIR/trace/*.c</code></p>
<dd>Sample C programs and source for <code><a href="/docs/linux/man/1-pmtrace/">pmtrace</a></code>(1). Use <code><a href="/docs/linux/man/1-make/">make</a></code>(1) to build these programs.</p>
<dt><code>$PCP_DEMOS_DIR/trace/fapp1.f</code></p>
<dd>Sample Fortran program. Call `make fortran77&#8242; or `make fortran90&#8242; to build this program.</p>
<dt><code>$PCP_DEMOS_DIR/trace/japp1.java</code></p>
<dd>Sample Java program. `make java&#8217; builds the java class file.</p>
<dt><code>/usr/java/classes/sgi/pcp/trace.java</code></p>
<dd>Java trace class definition.</dl>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <i><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></i>(3) function.</p>
<h2>See Also</h2>
<p><code>file:$PCP_DOC_DIR/Tutorial/trace.html,</code> <code>pcp.man.tutorial,</code> Provided the, <code><a href="/docs/linux/man/1-make/">make</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdatrace/">pmdatrace</a></code>(1), <code><a href="/docs/linux/man/1-pmprobe/">pmprobe</a></code>(1), <code><a href="/docs/linux/man/1-pmtrace/">pmtrace</a></code>(1), Relevant information is also available from the on-line PCP Tutorial, subsystem from the PCP images has been installed, access the URL and from your web browser.</p>
<h2>Diagnostics</h2>
<p>A negative return value from a <i>pcp_trace</i> function indicates that an error has occurred &#8211; if this is the case, the return value can be passed to <code>pmtraceerrstr</code> to obtain the associated error message. </p>
<p> Success is indicated by a return value of zero. </p>
<p> <code>pmtracestate</code> also returns an integer representing the state <i>flags</i> which were set prior to the call.</p>
<h2>Caveat</h2>
<p>Applications that use <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) should exercise caution because the static fields in <i>struct hostent</i> may not be preserved across some <i>pcp_trace</i> calls. In particular, <code>pmtracebegin</code>, <code>pmtraceend</code>, <code>pmtracepoint</code>, <code>pmtracecounter</code>, and <code>pmtraceobs</code> may all call <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) internally.</p>
