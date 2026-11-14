---
title: "pmdarootconnect(3)"
name: "pmdarootconnect"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdarootconnect/"
description: "pmdaRootConnect, pmdaRootShutdown, pmdaRootContainerHostName, pmdaRootContainerProcessID, pmdaRootContainerCGroupName, pmdaRootProcessStart, pmdaRootProcessWait, pmdaRootProcessTerminate – privileg..."
---

<p><code>pmdaRootConnect</code>, <code>pmdaRootShutdown</code>, <code>pmdaRootContainerHostName</code>, <code>pmdaRootContainerProcessID</code>, <code>pmdaRootContainerCGroupName</code>, <code>pmdaRootProcessStart</code>, <code>pmdaRootProcessWait</code>, <code>pmdaRootProcessTerminate</code> &#8211; privileged PCP collector services</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaRootConnect(void); </p>
<p> void pmdaRootShutdown(int </code><i>fd</i>); </p>
<p> int pmdaRootContainerHostName(int <i>fd</i>, char *<i>name</i>, int <i>namelen</i>, char *<i>buffer</i>, int <i>buflen</i>); </p>
<p> int pmdaRootContainerProcessID(int <i>fd</i>, char *<i>name</i>, int <i>namelen</i>); </p>
<p> int pmdaRootContainerCGroupName(int <i>fd</i>, char *<i>name</i>, int <i>namelen</i>, char *<i>buffer</i>, int <i>buflen</i>); </p>
<p> int pmdaRootProcessStart(int <i>fd</i>, int <i>ipctype</i>, char *<i>label</i>, int <i>labellen</i>, const char *<i>args</i>, int <i>argslen</i>, int *<i>pid</i>, int *<i>infd</i>, int *<i>outfd</i>); </p>
<p> int pmdaRootProcessWait(int <i>fd</i>, int <i>pid</i>, int *<i>status</i>); </p>
<p> int pmdaRootProcessTerminate(int <i>fd</i>, int <i>pid</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaRootConnect</code> initializes an IPC channel between a PCP collector process &#8211; either a <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) or <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) itself &#8211; and the <code><a href="/docs/linux/man/1-pmdaroot/">pmdaroot</a></code>(1) server. </p>
<p> On success, the return value from <code>pmdaRootConnect</code> is a <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) domain socket file descriptor, which can be subsequently passed to each of the other APIs described here. This channel can be used to perform limited privilege escalation for specific scenarios needed by PCP collector services. The channel can be deactivated using the <code>pmdaRootShutdown</code> interface.</p>
<h2>Containers</h2>
<p>Several interfaces are provided for access to the container facilities of modern Linux distributions, as needed by various agents accessing kernel features related to containers. </p>
<p> <code>pmdaRootContainerHostName</code> allows lookup of the current hostname for a named container on behalf of an unprivileged process, via the <code><a href="/docs/linux/man/3-setns/">setns</a></code>(3) system call on Linux. On success, the hostname is returned in the supplied <code>buffer</code>, of size <code>buflen</code> and the return value indicates the length of the hostname. </p>
<p> <code>pmdaRootContainerProcessID</code> performs a <i>name</i> to process identifier translation &#8211; on success, the return value is the identifier of the first process started (process 1) in the named container. </p>
<p> <code>pmdaRootContainerCGroupName</code> fills the supplied <i>buffer</i> with the engine-specific names of kernel control groups that have been used to build the container identified by <i>name</i>. When successful, the return value indicates the length of the cgroup name resolved for the container. </p>
<p> The <i>name</i> of the container is interpreted by <code><a href="/docs/linux/man/1-pmdaroot/">pmdaroot</a></code>(1), which attempts to match up the specified name with one of the implementations of containers that it is aware of. Hence, the <i>name</i> argument is potentially interpreted differently, depending on the installed container engine, as determined internally by <code>pmdaroot</code>). </p>
<p> In the case of the Docker container engine, for example, a valid container name can be the unique hash identifier, the human-readable name, or any unique identifier substring. This is the algorithm used by the Docker client tools themselves.</p>
<h2>Processes</h2>
<p>A second set of interfaces are provided allowing the collector system to start privileged child processes. In particular, these are used by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) so that it can start privileged PMDAs even when it is running under an unprivileged account itself. </p>
<p> These interfaces allow processes to be started (<code>pmdaRootProcessStart</code>), reaped upon completion (<code>pmdaRootProcessWait</code>), and forcibly terminated through use of signals (<code>pmdaRootProcessTerminate</code>). At this stage, they are intended only for use by <code>pmcd</code> itself and as such are described here only for completeness.</p>
<h2>Diagnostics</h2>
<p>All <code>pmdaRoot</code> interfaces will return negative status codes suitable for passing to <code><a href="/docs/linux/man/3-pmerrstr_r/">pmErrStr_r</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdaroot/">pmdaroot</a></code>(1), <code><a href="/docs/linux/man/3-pmerrstr_r/">pmErrStr_r</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-setns/">setns</a></code>(3) and <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7). </p>
