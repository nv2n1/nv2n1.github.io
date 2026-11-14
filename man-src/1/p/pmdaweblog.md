---
title: "pmdaweblog(1)"
name: "pmdaweblog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaweblog/"
description: "pmdaweblog – performance metrics domain agent (PMDA) for Web server logs"
---

<h2>NAME</h2>
<p> <code>pmdaweblog</code> &#8211; performance metrics domain agent (PMDA) for Web server logs</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/weblog/pmdaweblog</code> [<code>-Cp</code>] [<code>-d</code> <i>domain</i>] [<code>-h</code> <i>helpfile</i>] [<code>-i</code> <i>port</i>] [<code>-l</code> <i>logfile</i>] [<code>-n</code> <i>idlesec</i>] [<code>-S</code> <i>num</i>] [<code>-t</code> <i>delay</i>] [<code>-u</code> <i>socket</i>] [<code>-U</code> <i>username</i>] <i>configfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaweblog</code> is a Performance Metrics Domain Agent (<code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)) that scans Web server logs to extract metrics characterizing Web server activity. These performance metrics are then made available through the infrastructure of the Performance Co-Pilot (PCP). </p>
<p> The <i>configfile</i> specifies which Web servers are to be monitored, their associated access logs and error logs, and a regular-expression based scheme for extracting detailed information about each Web access. This file is maintained as part of the PMDA installation and/or de-installation by the scripts <code>Install</code> and <code>Remove</code> in the directory <code>$PCP_PMDAS_DIR/weblog</code>. For more details, refer to the section below covering installation. </p>
<p> Once started, <code>pmdaweblog</code> monitors a set of log files and in response to a request for information, will process any new information that has been appended to the log files, similar to a <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1). There is also periodic &quot;catch up&quot; to process new information from all log files, and a scheme to detect the rotation of log files. </p>
<p> Like all other PMDAs, <code>pmdaweblog</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) using command line options specified in <i>$PCP_PMCDCONF_PATH</i> &#8211; the <code>Install</code> script will prompt for appropriate values for the command line options, and update <i>$PCP_PMCDCONF_PATH</i>. </p>
<p> A brief description of the <code>pmdaweblog</code> command line options follows:</p>
<dl>
<dt><code>-C</code></p>
<dd> Check the configuration and exit.</p>
<dt><code>-d</code><i> domain</i></p>
<dd> Specify the <i>domain</i> number. It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the <code>pmdaweblog</code> PMDA on all hosts.</p>
<dl>
<dt>
<dd>
<p> For most installations, the default <i>domain</i> as encapsulated in the file <code>$PCP_PMDAS_DIR/weblog/domain.h</code> will suffice. For alternate values, check <i>$PCP_PMCDCONF_PATH</i> for the <i>domain</i> values already in use on this host, and the file <code>$PCP_VAR_DIR/pmns/stdpmid</code> contains a repository of &#8220;well known&#8221; <i>domain</i> assignments that probably should be avoided.</dl>
<dt><code>-h</code><i> helpfile</i></p>
<dd> Get the help text from the supplied <i>helpfile</i> rather than from the default location.</p>
<dt><code>-i</code><i> port</i></p>
<dd> Communicate with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the specified Internet <i>port</i> (which may be a number or a name).</p>
<dt><code>-l</code><i> logfile</i></p>
<dd> Location of the log file. By default, a log file named <i>weblog.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdaweblog</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-n</code><i> idlesec</i></p>
<dd> If a Web server log file has not been modified for <i>idlesec</i> seconds, then the file will be closed and re-opened. This is the only way <code>pmdaweblog</code> can detect any asynchronous rotation of the logs by Web server administrative scripts. The default period is 20 seconds. This value may be changed dynamically using <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) to modify the value of the performance metric <code>web.config.check</code>. <i></p>
<dt></i><code>-p</code></p>
<dd> Communicate with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) via a pipe.</p>
<dt><code>-S</code><i> num</i></p>
<dd> Specify the maximum number of Web servers per <i>sproc</i>. It may be desirable (from a latency and load balancing perspective) or necessary (due to file descriptor limits) to delegate responsibility for scanning the Web server log files to several <i>sprocs</i>. <code>pmdaweblog</code> will ensure that each <i>sproc</i> handles the log files for at most <i>num</i> Web servers. The default value is 80 Web servers per <i>sproc</i>.</p>
<dt><code>-t</code><i> delay</i></p>
<dd> To avoid the need to scan a lot of information from the Web server logs in response to a single request for performance metrics, all log files will be checked at least once every <i>delay</i> seconds. The default is 15 seconds. This value may by changed dynamically using <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) to modify the value of the performance metric <code>web.config.catchup</code>.</p>
<dt><code>-u</code><i> socket</i></p>
<dd> Communicate with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) via the given Unix domain <i>socket</i>.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> The PCP framework allows metrics to be collected on one host and monitored from another. These hosts are referred to as <i>collector </i> and <i>monitor </i> hosts, respectively. A host may be both a collector and a monitor. </p>
<p> Collector hosts require the installation of the agent, while monitoring hosts require no agent installation at all. </p>
<p> For collector hosts do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/weblog
# ./Install
</pre>
<p> The installation procedure prompts for a default or non-default installation. A default installation will search for known server configurations and automatically configure the PMDA for any server log files that are found. A non-default installation will step through each server, prompting the user for other server configurations and arguments to <code>pmdaweblog</code>. The end result of a collector installation is to build a configuration file that is passed to <code>pmdaweblog</code> via the <i>configfile</i> argument. </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/weblog
# ./Remove
</pre>
<p> <code>pmdaweblog</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The <code>Install</code> and <code>Remove </code> scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>CONFIGURATION</h2>
<p> The configuration file for the weblog PMDA is an ASCII file that can be easily modified. Empty lines and lines beginning with &#8216;<code>#</code>&#8216; are ignored. All other lines must be either a regular expression or server specification. </p>
<p> Regular expressions, which are used on both the access and error log files, must be of the form: </p>
<p> <code>regex</code> <i>regexName regexp</i> <i>or</i> </p>
<p> <code>regex_posix</code> <i>regexName ordering regexp_posix</i> </p>
<p> The <i>regexName</i> is a word which uniquely identifies the regular expression. This is the reference used in the server specification. The <i>regexp</i> for access logs is in the format described for <code><a href="/docs/linux/man/3-regcmp/">regcmp</a></code>(3). The <i>regexp_posix</i> for access logs is in the format described for <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3). The argument <i>ordering</i> is explained below. The <code>Posix</code> form should be available on all platforms. </p>
<p> The regular expression requires the specification of up to four arguments to be extracted from each line of a Web server access log, depending on the type of server. In the most common case there are two arguments representing the method and the size. </p>
<p> For the non- <code>Posix</code> version, argument <i>$0</i> should contain the method: <code>GET</code>, <code>HEAD ,</code> <code>POST</code> or <code>PUT</code>. The method <code>PUT</code> is treated as a synonym for <code>POST</code>, and anything else is categorized as <code>OTHER</code>. </p>
<p> The second argument, <i>$1</i>, should contain the size of the request. A size of &#8220;<code>&#8211;</code>&#8221; or &#8220; &#8221; is treated as unknown. </p>
<p> Argument <i>$3</i> should contain the status code returned to the client browser and argument <i>$4</i> should contain the status code returned to the server from a remote host. These latter two arguments are used for caching servers and must be specified as a pair (or <i>$3</i> will be ignored). For further information on status codes, refer to the web site <code><a rel="nofollow" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html">http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html</a></code> </p>
<p> Some legal non- <code>Posix</code> regex expression specifications for monitoring an access log are: </p>
<pre><code>
#pattern for CERN, NCSA, Netscape etc Access Logs
regex CERN ] "([A-Za-z][-A-Za-z]+)$0 .*" [-0-9]+ ([-0-9]+)$1
#pattern for FTP Server access logs(normally in SYSLOG)
regex SYSLOG_FTP ftpd[.*]: ([gp][-A-Za-z]+)$0( )$1
</code></pre>
<p> There is 1 special types of access logs with the <i>RegexName</i> <i>SQUID.</i> This formats extract 4 parameters but since the <code>Squid</code> log file uses text-based status codes, it is handled as a special case. </p>
<p> In the examples below, <i>NS_PROXY</i> parses the Netscape/W3C <i>Common Extended Log Format</i> and <i>SQUID</i> parses the default Squid Object Cache format log file. </p>
<p>#pattern for Netscape Proxy Server Extended Logs<br />
regex NS_PROXY ] &#8220;([A-Za-z][-A-Za-z]+)$0 .*&#8221; ([-0-9]+)$2 \<br />
([-0-9]+)$1 ([-0-9]+)$3<br />
#pattern for Squid Cache logs<br />
regex SQUID [0-9]+.[0-9]+[ ]+[0-9]+ [a-zA-Z0-9.]+ \<br />
([_A-Z]+)$3/([0-9]+)$2 ([0-9]+)$1 ([A-Z]+)$0</p>
<p> The <i>regexp</i> for the error logs does not require any arguments, only a match. Some legal expressions are: </p>
<pre>
# pattern for CERN, NCSA, Netscape etc Error Logs
regex CERN_err .
# pattern for FTP Server error logs (normally in SYSLOG)
regex SYSLOG_FTP_err FTP LOGIN FAILED
</pre>
<p> If <code>POSIX</code> compliant regular expressions are used, additional information is required since the order of parameters cannot be specified in the regular expression. For backwards compatibility, the common case of two parameters the order may be specified as <i>method,size</i> or <i>size,method</i> In the general case, the ordering is specified by one of the following methods:</p>
<dl>
<dt>n1,n2,n3,n4</p>
<dd> where nX is a digit between 1 and 4. Each comma-seperated field represents (in order) the argument number for <i>method,size,client_status,server_status</i></p>
<dt>&#8211;</p>
<dd> Used for cases like the error logs where the content is ignored.</dl>
<p> As for the non- <code>Posix</code> format, the <i>SQUID</i> RegexName is treated as a special case to match the non-numerical status codes. </p>
<p> Some legal <code>Posix</code> regex expression specifications for monitoring an access log are: </p>
<pre><code>
#pattern for CERN, NCSA, Netscape, Apache etc Access Logs
regex_posix CERN method,size ][ \]+"([A-Za-z][-A-Za-z]+) \
[^"]*" [-0-9]+ ([-0-9]+)
#pattern for CERN, NCSA, Netscape, Apache etc Access Logs
regex_posix CERN 1,2 ][ \]+"([A-Za-z][-A-Za-z]+) \
[^"]*" [-0-9]+ ([-0-9]+)
#pattern for FTP Server access logs(normally in SYSLOG)
regex_posix SYSLOG_FTP method,size ftpd[.*]: \
([gp][-A-Za-z]+)( )
#pattern for Netscape Proxy Server Extended Logs
regex_posix NS_PROXY 1,3,2,4 ][ ]+"([A-Za-z][-A-Za-z]+) \
[^"]*" ([-0-9]+) ([-0-9]+) ([-0-9]+)
#pattern for Squid Cache logs
regex_posix SQUID 4,3,2,1 [0-9]+.[0-9]+[ ]+[0-9]+ \
[a-zA-Z0-9.]+ ([_A-Z]+)/([0-9]+) ([0-9]+) ([A-Z]+)
#pattern for CERN, NCSA, Netscape etc Error Logs
regex_posix CERN_err - .
#pattern for FTP Server error logs(normally in SYSLOG)
regex_posix SYSLOG_FTP_err - FTP LOGIN FAILED
</code></pre>
<p> A Web server can be specified using this syntax: </p>
<pre>
<code>server </code><i>serverName </i><code>on</code><i>|</i><code>off </code><i>accessRegex accessFile errorRegex errorFile
</i></pre>
<p> The <i>serverName</i> must be unique for each server, and is the name given to the instance for the associated performance metrics. See <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) for a discussion of PCP instance domains. The <code>on</code> or <code>off</code> flag indicates whether the server is to be monitored when the PMDA is installed. This can altered dynamically using <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) for the metric <code>web.perserver.watched</code>, which has one instance for each Web server named in <i>configfile</i>. </p>
<p> Two files are monitored for each Web server, the access and the error log. Each file requires the name of a previously declared regular expression, and a file name. The log files specified for each server do not have to exist when the weblog PMDA is installed. The PMDA will continue to check for non-existent log files and open them when possible. Some legal server specifications are: </p>
<pre>
# Netscape Server on Port 80 at IP address 127.55.555.555
server 127.55.555.555:80 on CERN /logs/access CERN_err /logs/errors
# FTP Server.
server ftpd on SYSLOG_FTP /var/log/messages SYSLOG_FTP_err /var/log/messages
</pre>
<h2>CAVEATS</h2>
<p> Specifying regular expressions with an incorrect number of arguments, anything other than 2 for access logs, and none for error logs, may cause the PMDA to behave incorrectly and even crash. This is due to limitations in the interface of <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3).</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/weblog</code></p>
<dd> installation directory for the weblog PMDA</p>
<dt><code>$PCP_PMDAS_DIR/weblog/Install</code></p>
<dd> installation script for the weblog PMDA</p>
<dt><code>$PCP_PMDAS_DIR/weblog/Remove</code></p>
<dd> de-installation script for the weblog PMDA</p>
<dt><code>$PCP_LOG_DIR/pmcd/weblog.log</code></p>
<dd> default log file for error reporting</p>
<dt><i>$PCP_PMCDCONF_PATH</i></p>
<dd> <code>pmcd</code> configuration file that specifies the command line options to be used when <code>pmdaweblog</code> is launched</p>
<dt><code>$PCP_LOG_DIR/NOTICES</code></p>
<dd> log of PMDA installations and removals</p>
<dt><code>$PCP_VAR_DIR/config/web/weblog.conf</code></p>
<dd> likely location of the weblog PMDA configuration file</p>
<dt><code>$PCP_DOC_DIR/pcpweb/index.html</code></p>
<dd> the online HTML documentation for PCPWEB</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmdawebping/">pmdawebping</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), <code><a href="/docs/linux/man/1-pmview/">pmview</a></code>(1), <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1), <code><a href="/docs/linux/man/1-weblogvis/">weblogvis</a></code>(1), <code><a href="/docs/linux/man/1-webvis/">webvis</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) and <code><a href="/docs/linux/man/3-regcmp/">regcmp</a></code>(3). </p>
<h2>Index</h2>
