---
title: "remctl(3)"
name: "remctl"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl/"
---

remctl, remctl_result_free - Simple remctl call to a remote server

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
struct remctl_result *

remctl(const char *host, unsigned short port,
       const char *principal, const char **command);
void remctl_result_free(struct remctl_result *result);</code></pre>

<h2>Description</h2>

<i>remctl()</i> provides a simplified client <font SIZE="-1">API</font> for the remctl protocol. Given the host, port, service principal for authentication, and command to run, it opens a connection to the remote system, sends the command via the remctl protocol, reads the results, closes the connection, and returns the result as a remctl_result struct. <i>host</i> is a hostname or <font SIZE="-1">IP</font> address and must be non-NULL. <i>port</i> is the port to connect to; if 0, the library first attempts to connect to the registered port of 4373 and then tries the legacy port of 4444 if that fails. Future versions of the library will drop this fallback to 4444. <i>principal</i> is the service principal to use for authentication; if <font SIZE="-1">NULL, </font><tt>&quot;host/</tt>host<tt>&quot;</tt> is used, with the realm determined by domain-realm mapping. <i>command</i> is the command to run as a NULL-terminated array of NUL-terminated strings. If no principal is specified and the default is used, the underlying GSS-API library may canonicalize <i>host</i> via <font SIZE="-1">DNS</font> before determining the service principal, depending on your library configuration. Specifying a principal disables this behavior. The remctl protocol uses Kerberos via GSS-API for authentication. The underlying GSS-API library will use the default ticket cache for authentication, so to successfully use <i>remctl()</i>, the caller should already have Kerberos tickets for an appropriate realm stored in its default ticket cache. The environment variable <font SIZE="-1">KRB5CCNAME</font> can be used to control which ticket cache is used. If the client needs to control which ticket cache is used without changing the environment, use the full client <font SIZE="-1">API</font> along with <i><a HREF="/docs/linux/man/3-remctl_set_ccache/">remctl_set_ccache</a></i>(3). <i>remctl()</i> returns a newly allocated remctl_result struct, which has the following members: <pre><code>struct remctl_result {
    char *error;       /* remctl error if non-NULL. */
    char *stdout_buf;  /* Standard output. */
    size_t stdout_len; /* Length of standard output. */
    char *stderr_buf;  /* Standard error. */
    size_t stderr_len; /* Length of standard error. */
    int status;        /* Exit status of remote command. */
};</code></pre> If error is non-NULL, a protocol error occurred and the command was not successfully completed. Otherwise, standard output from the command will be stored in stdout_buf with the length in stdout_len, standard error from the command will be stored in stderr_buf with the length in stderr_len, and status will hold the exit status of the command. Following the standard Unix convention, a 0 status should normally be considered success and any non-zero status should normally be considered failure, although a given command may have its own exit status conventions. <i>remctl_result_free()</i> frees the remctl_result struct when the calling program is through with it. If you want more control over the steps of the protocol, issue multiple commands on the same connection, control the ticket cache or source <font SIZE="-1">IP,</font> set a timeout on replies, or send data as part of the command that contains NULs, use the full <font SIZE="-1">API</font> described in <i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_commandv/">remctl_commandv</a></i>(3), and <i><a HREF="/docs/linux/man/3-remctl_output/">remctl_output</a></i>(3).

<h2>Return Value</h2>

<i>remctl()</i> returns <font SIZE="-1">NULL</font> on failure to allocate a new remctl_result struct or on failure to allocate space to store an error message. Otherwise, it returns a newly allocated remctl_result struct with either an error message in the error field or the results of the command filled out as described above. If <i>remctl()</i> returns <font SIZE="-1">NULL,</font> errno will be set to an appropriate error code (generally <font SIZE="-1">ENOMEM</font>).

<h2>Compatibility</h2>

This interface has been provided by the remctl client library since its initial release in version 2.0. 

 The default port was changed to the IANA-registered port of 4373 in version 2.11. 

 Support for IPv6 was added in version 2.4.

<h2>Caveats</h2>

If the <i>principal</i> argument to <i>remctl()</i> is <font SIZE="-1">NULL,</font> most GSS-API libraries will canonicalize the <i>host</i> using <font SIZE="-1">DNS</font> before deriving the principal name from it. This means that when connecting to a remctl server via a <font SIZE="-1">CNAME,</font> <i>remctl()</i> will normally authenticate using a principal based on the canonical name of the host instead of the specified <i>host</i> parameter. This behavior may cause problems if two consecutive <font SIZE="-1">DNS</font> lookups of <i>host</i> may return two different results, such as with some DNS-based load-balancing systems. 

 The canonicalization behavior is controlled by the GSS-API library; with the <font SIZE="-1">MIT</font> Kerberos GSS-API library, canonicalization can be disabled by setting <tt>&quot;rdns&quot;</tt> to false in the [libdefaults] section of <i>krb5.conf</i>. It can also be disabled by passing an explicit Kerberos principal name via the <i>principal</i> argument, which will then be used without changes. If canonicalization is desired, the caller may wish to canonicalize <i>host</i> before calling <i>remctl()</i> to avoid problems with multiple <font SIZE="-1">DNS</font> calls returning different results. 

 The default behavior, when a port of 0 is given, of trying 4373 and falling back to 4444 will be removed in a future version of this library in favor of using the <tt>&quot;remctl&quot;</tt> service in <i>/etc/services</i> if set and then falling back on only 4373. 4444 was the poorly-chosen original remctl port and should be phased out.

<h2>Notes</h2>

The remctl port number, 4373, was derived by tracing the diagonals of a <font SIZE="-1">QWERTY</font> keyboard up from the letters <tt>&quot;remc&quot;</tt> to the number row.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2008, 2009, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_command/">remctl_command</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_commandv/">remctl_commandv</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_output/">remctl_output</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_close/">remctl_close</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
