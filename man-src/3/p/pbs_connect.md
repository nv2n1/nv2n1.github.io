---
title: "pbs_connect(3)"
name: "pbs_connect"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_connect/"
description: "pbs_connect – connect to a pbs batch server"
---

<p>pbs_connect &#8211; connect to a pbs batch server</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;
#include &lt;pbs_ifl.h&gt;
int pbs_connect(char *server)
    extern char *pbs_server;</code></pre>
<h2>Description</h2>
<p>A virtual stream (TCP/IP) connection is established with the server specified by <i> </p>
<p> This function must be called before any of the other </i><code>pbs_</code> functions. They will transmit their batch requests over the connection established by this function. Multiple requests may be issued over the connection before it is closed. </p>
<p> The connection should be closed by a call to <code>pbs_disconnect</code>() when all requests have been sent to the server. </p>
<p> The parameter, <i> is of the form </i><code> see section 2.7.9. If is not specified, the standard PBS port number will be used. </p>
<p> If the parameter, </code><i> is either the null string or a null pointer, a connection will be opened to the default server. The default server is defined by (a) the setting of the environment variable </i><code>PBS_DEFAULT</code> which contains a destination, or (b) the destination in the batch administrator established file <code> </p>
<p> The variable </code><i> declared in pbs_ifl.h, is set on return to point to the server name to which pbs_connect() connected or attempted to connect. </i></p>
<h2>See Also</h2>
<p>qsub(1B), pbs_alterjob(3B), pbs_deljob(3B), pbs_disconnect(3B), pbs_geterrmsg(3B), pbs_holdjob(3B), pbs_locate(3B), pbs_manager(3B), pbs_movejob(3B), pbs_msgjob(3B), pbs_rerunjob(3B), pbs_rlsjob(3B), pbs_runjob(3B), pbs_selectjob(3B), pbs_selstat(3B), pbs_sigjob(3B), pbs_statjob(3B), pbs_statque(3B), pbs_statserver(3B), pbs_submit(3B), pbs_terminate(3B), pbs_server(8B), and the PBS External Reference Specification</p>
<h2>Diagnostics</h2>
<p>When the connection to batch server has been successfully created, the routine will return a connection identifier which is positive. Otherwise, a negative value is returned. The error number is set in pbs_errno.</p>
