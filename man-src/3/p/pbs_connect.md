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
<p> If the parameter, </code><i> is either the null string or a null pointer, a connection will be opened to the default server. The default server is defined by (a) the setting of the environment variable </i><code>PBS_DEFAULT</code> which contains a destination, or (b) the destination in the batch administrator established file <font SIZE="-1"><code> </p>
<p> The variable </code><i> declared in pbs_ifl.h, is set on return to point to the server name to which pbs_connect() connected or attempted to connect. </i></font></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_deljob/">pbs_deljob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_disconnect/">pbs_disconnect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_geterrmsg/">pbs_geterrmsg</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_holdjob/">pbs_holdjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_locate/">pbs_locate</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_manager/">pbs_manager</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_movejob/">pbs_movejob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_msgjob/">pbs_msgjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rerunjob/">pbs_rerunjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rlsjob/">pbs_rlsjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_runjob/">pbs_runjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_selectjob/">pbs_selectjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_selstat/">pbs_selstat</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_sigjob/">pbs_sigjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statjob/">pbs_statjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statque/">pbs_statque</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statserver/">pbs_statserver</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_submit/">pbs_submit</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_terminate/">pbs_terminate</a>(3B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), and the PBS External Reference Specification</p>
<h2>Diagnostics</h2>
<p>When the connection to batch server has been successfully created, the routine will return a connection identifier which is positive. Otherwise, a negative value is returned. The error number is set in pbs_errno.</p>
