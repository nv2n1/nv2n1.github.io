---
title: "globus-gatekeeper(8)"
name: "globus-gatekeeper"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-gatekeeper/"
description: "globus-gatekeeper – Authorize and execute a grid service on behalf of a user"
---

<p>globus-gatekeeper &#8211; Authorize and execute a grid service on behalf of a user</p>
<h2>Synopsis</h2>
<p><code>globus-gatekeeper</code> [-help] </p>
<p> <code>globus-gatekeeper</code> -conf <i>PARAMETER_FILE</i> [-test] [-d | -debug] [-inetd | -f] [-p <i>PORT</i> | -port <i>PORT</i>] [-l <i>LOGFILE</i> | -logfile <i>LOGFILE</i>] [-lf <i>LOG_FACILITY</i>] [-acctfile <i>ACCTFILE</i>] [-e <i>LIBEXECDIR</i>] [-launch_method { <i>fork_and_exit</i> | <i>fork_and_wait</i> | <i>dont_fork</i> }] [-grid_services <i>SERVICEDIR</i>] [-globusid <i>GLOBUSID</i>] [-gridmap <i>GRIDMAP</i>] [-x509_cert_dir <i>TRUSTED_CERT_DIR</i>] [-x509_cert_file <i>TRUSTED_CERT_FILE</i>] [-x509_user_cert <i>CERT_PATH</i>] [-x509_user_key <i>KEY_PATH</i>] [-x509_user_proxy <i>PROXY_PATH</i>] [-k] [-globuskmap <i>KMAP</i>] [-pidfile <i>PIDFILE</i>]</p>
<h2>Description</h2>
<p>The <code>globus-gatekeeper</code> program is a meta-server similar to <code>inetd</code> or*xinetd* that starts other services after authenticating a TCP connection using GSSAPI and mapping the client&#8217;s credential to a local account. </p>
<p> The most common use for the <code>globus-gatekeeper</code> program is to start instances of the <code><a href="/docs/linux/man/8-globus-job-manager/">globus-job-manager</a></code>(8) service. A single <code>globus-gatekeeper</code> deployment can handle multiple different service configurations by having entries in the /etc/grid-services/ directory. </p>
<p> Typically, users interact with the <code>globus-gatekeeper</code> program via client applications such as <code><a href="/docs/linux/man/1-globusrun/">globusrun</a></code>(1), <code><a href="/docs/linux/man/1-globus-job-submit/">globus-job-submit</a></code>(1), or tools such as CoG jglobus or Condor-G. </p>
<p> The full set of command-line options to <code>globus-gatekeeper</code> consists of: </p>
<p> <code>-help</code></p>
<dl>
<dd>Display a help message to standard error and exit</dl>
<p> <code>-conf </code><i>PARAMETER_FILE</i></p>
<dl>
<dd>Load configuration parameters from <i>PARAMETER_FILE</i>. The parameters in that file are treated as additional command-line options.</dl>
<p> <code>-test</code></p>
<dl>
<dd>Parse the configuration file and print out the POSIX user id of the <code>globus-gatekeeper</code> process, service home directory, service execution directory, and X.509 subject name and then exits.</dl>
<p> <code>-d, -debug</code></p>
<dl>
<dd>Run the <code>globus-gatekeeper</code> process in the foreground.</dl>
<p> <code>-inetd</code></p>
<dl>
<dd>Flag to indicate that the <code>globus-gatekeeper</code> process was started via <code>inetd</code> or a similar super-server. If this flag is set and the <code>globus-gatekeeper</code> was not started via inetd, a warning will be printed in the gatekeeper log.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Flag to indicate that the <code>globus-gatekeeper</code> process should run in the foreground. This flag has no effect when the <code>globus-gatekeeper</code> is started via inetd.</dl>
<p> <code>-p </code><i>PORT</i><code>, -port </code><i>PORT</i></p>
<dl>
<dd>Listen for connections on the TCP/IP port <i>PORT</i>. This option has no effect if the <code>globus-gatekeeper</code> is started via inetd or a similar service. If not specified and the gatekeeper is running as root, the default of 2119 is used. Otherwise, the gatekeeper defaults to an ephemeral port.</dl>
<p> <code>-home </code><i>PATH</i></p>
<dl>
<dd>Sets the gatekeeper deployment directory to <i>PATH</i>. This is used to interpret relative paths for accounting files, libexecdir, certificate paths, and also to set the GLOBUS_LOCATION environment variable in the service environment. If not specified, the gatekeeper looks for service executables in /usr/sbin, configuration in /etc, and writes logs and accounting files to /var/log.</dl>
<p> <code>-l </code><i>LOGFILE</i><code>, -logfile </code><i>LOGFILE</i></p>
<dl>
<dd>Write log entries to <i>LOGFILE</i>. If <i>LOGFILE</i> is equal to logoff or LOGOFF, then logging will be disabled, both to file and to syslog.</dl>
<p> <code>-lf </code><i>LOG_FACILITY</i></p>
<dl>
<dd>Open syslog using the <i>LOG_FACILITY</i>. If not specified, LOG_DAEMON will be used as the default when using syslog.</dl>
<p> <code>&lt;option&gt;-acctfile </code><i>ACCTFILE</i><code>&lt;/option&gt;</code></p>
<dl>
<dd>Set the path to write accounting records to <i>ACCTFILE</i>. If not set, records will be written to the log file.</dl>
<p> <code>-e </code><i>LIBEXECDIR</i></p>
<dl>
<dd>Look for service executables in <i>LIBEXECDIR</i>. If not specified, the sbin subdirectory of the parameter to <i>-home</i> is used, or /usr/sbin if that is not set.</dl>
<p> <code>-launch_method </code><code>fork_and_exit</code><code> | </code><code>fork_and_wait</code><code> | </code><code>dont_fork</code></p>
<dl>
<dd>Determine how to launch services. The method may be either fork_and_exit (the service runs completely independently of the gatekeeper, which exits after creating the new service process), fork_and_wait (the service is run in a separate process from the gatekeeper but the gatekeeper does not exit until the service terminates), or dont_fork, where the gatekeeper process becomes the service process via the <code>exec</code>() system call.</dl>
<p> <code>-grid_services </code><i>SERVICEDIR</i></p>
<dl>
<dd>Look for service descriptions in <i>SERVICEDIR</i>.</dl>
<p> <code>-globusid </code><i>GLOBUSID</i></p>
<dl>
<dd>Sets the GLOBUSID environment variable to <i>GLOBUSID</i>. This variable is used to construct the gatekeeper contact string if it can not be parsed from the service credential.</dl>
<p> <code>-gridmap </code><i>GRIDMAP</i></p>
<dl>
<dd>Use the file at <i>GRIDMAP</i> to map GSSAPI names to POSIX user names.</dl>
<p> <code>-x509_cert_dir </code><i>TRUSTED_CERT_DIR</i></p>
<dl>
<dd>Use the directory <i>TRUSTED_CERT_DIR</i> to locate trusted CA X.509 certificates. The gatekeeper sets the environment variable X509_CERT_DIR to this value.</dl>
<p> <code>-x509_user_cert </code><i>CERT_PATH</i></p>
<dl>
<dd>Read the service X.509 certificate from <i>CERT_PATH</i>. The gatekeeper sets the X509_USER_CERT environment variable to this value.</dl>
<p> <code>-x509_user_key </code><i>KEY_PATH</i></p>
<dl>
<dd>Read the private key for the service from <i>KEY_PATH</i>. The gatekeeper sets the X509_USER_KEY environment variable to this value.</dl>
<p> <code>-x509_user_proxy </code><i>PROXY_PATH</i></p>
<dl>
<dd>Read the X.509 proxy certificate from <i>PROXY_PATH</i>. The gatekeeper sets the X509_USER_PROXY environment variable to this value.</dl>
<p> <code>-k</code></p>
<dl>
<dd>Use the &lt;command&gt;globus-k5&lt;/command&gt; command to acquire Kerberos 5 credentials before starting the service.</dl>
<p> <code>-globuskmap </code><i>KMAP</i></p>
<dl>
<dd>Use <i>KMAP</i> as the path to the Grid credential to kerberos initialization mapping file.</dl>
<p> <code>-pidfile </code><i>PIDFILE</i></p>
<dl>
<dd>Write the process id of the <code>globus-gatekeeper</code> to the file named by <i>PIDFILE</i>.</dl>
<h2>Environment</h2>
<p>The following environment variables affect the execution of <code>globus-gatekeeper</code>: </p>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dd>Directory containing X.509 trust anchors and signing policy files.</dl>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dd>Path to file containing an X.509 proxy.</dl>
<p> <code>X509_USER_CERT</code></p>
<dl>
<dd>Path to file containing an X.509 user certificate.</dl>
<p> <code>X509_USER_KEY</code></p>
<dl>
<dd>Path to file containing an X.509 user key.</dl>
<p> <code>GLOBUS_LOCATION</code></p>
<dl>
<dd>Default path to gatekeeper service files.</dl>
<h2>Files</h2>
<p>The following files affect the execution of <code>globus-gatekeeper</code>: </p>
<p> <code>/etc/grid-services/</code><i>SERVICENAME</i></p>
<dl>
<dd>Service configuration for <i>SERVICENAME</i>.</dl>
<p> <code>/etc/grid-security/grid-mapfile</code></p>
<dl>
<dd>Default file mapping Grid identities to POSIX identities.</dl>
<p> <code>/etc/globuskmap</code></p>
<dl>
<dd>Default file mapping Grid identities to Kerberos 5 principals.</dl>
<p> <code>/etc/globus-nologin</code></p>
<dl>
<dd>File to disable the <code>globus-gatekeeper</code> program.</dl>
<p> <code>/var/log/globus-gatekeeper.log</code></p>
<dl>
<dd>Default gatekeeper log.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-globus-k5/">globus-k5</a></code>(8), <code><a href="/docs/linux/man/1-globusrun/">globusrun</a></code>(1), <code><a href="/docs/linux/man/8-globus-job-manager/">globus-job-manager</a></code>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
