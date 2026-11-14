---
title: "xrdcp(1)"
name: "xrdcp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrdcp/"
description: "xrdcp – copy files"
---

<h2>NAME</h2>
<p> xrdcp &#8211; copy files</p>
<h2>SYNOPSIS</h2>
<pre><code>
xrdcp[options] source destination
    options : [--cksum args][--debug lvl]
                            [--coerce][--force][--help][--license]
                            [--nopbar][--posc] [--proxy ipaddr:port]
                            [--recursive][--retry time][--server]
                            [--silent][--sources num][--streams num]
                            [--tpc first | only][--verbose][--version]
                            [--xrate rate][--zip file] legacy options : [-adler][-DSparm string][-DIparm number]
                                                                                [-md5][-np][-ODcgi][-OScgi][-x]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>xrdcp</code> utility copies one or more files from one location to another. The data source and destination may be a local or remote file or directory. Additionally, the data source may also reside on multiple servers.</p>
<h2>OPTIONS</h2>
<p> <code>-C</code> | <code>&#8211;cksum</code> <i>type</i>[<code>:</code><i>value</i>|<i>print</i>|<i>source</i>]</p>
<dl>
<dt>
<dd> obtains the checksum of <i>type</i> (i.e. adler32, crc32, or md5) from the source, computes the checksum at the destination, and verifies that they are the same. If a <i>value</i> is specified, it is used as the source checksum. When <i>print</i> is specified, the checksum at the destination is printed but is <i>not</i> verified. </p>
</dl>
<p> <code>-d</code> | <code>&#8211;debug</code> <i>lvl</i></p>
<dl>
<dt>
<dd> debug level: 1 (low), 2 (medium), 3 (high) </p>
</dl>
<p> <code>-F</code> | <code>&#8211;coerce</code></p>
<dl>
<dt>
<dd> ignores locking semantics on the destination file. This option may lead to file corruption if not properly used. </p>
</dl>
<p> <code>-f</code> | <code>&#8211;force</code></p>
<dl>
<dt>
<dd> re-creates a file if it is already present. </p>
</dl>
<p> <code>-h</code> | <code>&#8211;help</code></p>
<dl>
<dt>
<dd> displays usage information. </p>
</dl>
<p> <code>-H</code> | <code>&#8211;license</code></p>
<dl>
<dt>
<dd> displays license terms and conditions. </p>
</dl>
<p> <code>-N</code> | <code>&#8211;nopbar</code></p>
<dl>
<dt>
<dd> does not display the progress bar. </p>
</dl>
<p> <code>-P</code> | <code>&#8211;posc</code></p>
<dl>
<dt>
<dd> requests POSC (persist-on-successful-close) processing to create a new file. Files are automatically deleted should they not be successfully closed. </p>
</dl>
<p> <code>-D</code> | <code>&#8211;proxy</code> <i>proxyaddr</i><code>:</code><i>proxyport</i></p>
<dl>
<dt>
<dd> [NOT YET IMPLEMENTED] </p>
<p> use <i>proxyaddr</i><code>:</code><i>proxyport</i> as a SOCKS4 proxy. Only numerical addresses are supported. </p>
</dl>
<p> <code>-r</code> | <code>&#8211;recursive</code></p>
<dl>
<dt>
<dd> recursively copy all files starting at the given source directory. This option is <i>only</i> supported for local files. </p>
</dl>
<p> <code>&#8211;server</code></p>
<dl>
<dt>
<dd> runs as if in a server environment. Used only for server-side third party copy support. </p>
</dl>
<p> <code>-s</code> | <code>&#8211;silent</code></p>
<dl>
<dt>
<dd> neither produces summary information nor displays the progress bar. </p>
</dl>
<p> <code>-y</code> | <code>&#8211;sources</code> <i>num</i></p>
<dl>
<dt>
<dd> [NOT YET IMPLEMENTED] </p>
<p> uses up to <i>num</i> sources to copy the file. </p>
</dl>
<p> <code>-S</code> | <code>&#8211;streams</code> <i>num</i></p>
<dl>
<dt>
<dd> uses <i>num</i> additional parallel streams to do the transfer. The maximum value is 15. The default is 0 (i.e., use only the main stream). </p>
</dl>
<p> <code>&#8211;tpc</code> <i>first|only</i></p>
<dl>
<dt>
<dd> copies the file from remote server to remote server using third-party-copy protocol (i.e., data flows from server to server). The source and destination servers must support third party copies. Additional security restrictions may apply and may cause the copy to fail if they cannot be satisfied. Argument <i>&#8216;first&#8217;</i> tries tpc and if it fails, does a normal copy; while <i>&#8216;only&#8217;</i> fails the copy unless tpc succeeds. </p>
</dl>
<p> <code>-v</code> | <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> displays summary output. </p>
</dl>
<p> <code>-V</code> | <code>-version</code></p>
<dl>
<dt>
<dd> displays version information and immediately exits. </p>
</dl>
<p> <code>-z</code> | <code>&#8211;zip</code></p>
<dl>
<dt>
<dd> copy given file from a ZIP archive. </p>
</dl>
<p> <code>-X</code> | <code>&#8211;xrate</code> <i>rate</i></p>
<dl>
<dt>
<dd> [NOT YET IMPLEMENTED] </p>
<p> limits the copy speed to the specified <i>rate</i><code>. The rate may be qualified with the letter k</code>, <code>m</code>, or <code>g</code> to indicate kilo, mega, or giga bytes, respectively. The option only applies when the source or destination is local. </p>
</dl>
<h2>LEGACY OPTIONS</h2>
<p> Legacy options are provided for backward compatability. These are now deprecated and should be avoided. <code>-adler</code></p>
<dl>
<dt>
<dd> equivalent to &quot;<code>&#8211;cksum adler32:source</code>&quot;. </p>
</dl>
<p> <code>-DI</code><i>pname numberval</i></p>
<dl>
<dt>
<dd> set the internal parameter <i>pname</i> with the numeric value <i>numberval</i>. </p>
</dl>
<p> <code>-DS</code><i>pname stringval</i></p>
<dl>
<dt>
<dd> set the internal parameter <i>pname</i> with the string value <i>stringval</i>. </p>
</dl>
<p> <code>-md5</code></p>
<dl>
<dt>
<dd> equivalent to &quot;<code>&#8211;cksum md5:source</code>&quot;. </p>
</dl>
<p> <code>-np</code></p>
<dl>
<dt>
<dd> equivalent to &quot;<code>&#8211;nopbar</code>&quot;. </p>
</dl>
<p> <code>-OD</code><i>cgi</i></p>
<dl>
<dt>
<dd> add cgi information <i>cgi</i> to any destination xrootd URL. You should specify the opaque information directly on the destination URL. </p>
</dl>
<p> <code>-OS</code><i>cgi</i></p>
<dl>
<dt>
<dd> add cgi information <i>cgi</i> to any source xrootd URL. </p>
</dl>
<p> <code>-x</code></p>
<dl>
<dt>
<dd> equivalent to &quot;<code>&#8211;sources 12</code>&quot;. </p>
</dl>
<h2>OPERANDS</h2>
<p> <i>source</i></p>
<dl>
<dt>
<dd> a dash (i.e. <code>&#8211;</code>) indicating stanard in, a local file, a local directory name suffixed by /, or an xrootd URL in the form of <center> <code><a href="xroot://[">xroot://[</a></code><i>user</i><code>@</code>]<i>host[</i><code>:</code><i>port</i>]<code>/</code><i>absolutepath</i><br />
 </center> The <i>absolutepath</i> can be a directory. </p>
</dl>
<p> <i>destination</i></p>
<dl>
<dt>
<dd> a dash (i.e. <code>&#8211;</code>) indicating stanard out, a local file, a local directory name suffixed by /, or an xrootd URL in the form <center> <code><a href="xroot://[">xroot://[</a></code><i>user</i><code>@</code>]<i>host[</i><code>:</code><i>port</i>]<code>/</code><i>absolutepath</i><br />
 </center> The <i>absolutepath</i> can be a directory. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables are supported. They apply to xrdfs and any other application using the libXrdCl library, unless specified otherwise. The text in the brackets is a name of the corresponding xrdcp commandline parameter. </p>
<p> XRD_LOGLEVEL</p>
<dl>
<dt>
<dd> Detemines the amout of diagnostics that should be printed. Valid values are: <i>Dump</i>, <i>Debug</i>, <i>Info</i>, <i>Warning</i>, and <i>Error</i>.</dl>
<p> XRD_LOGFILE</p>
<dl>
<dt>
<dd> If set, the diagnostics will be printed to the specified file instead of stderr.</dl>
<p> XRD_LOGMASK</p>
<dl>
<dt>
<dd> Determines which diagnostics topics should be printed at all levels. It&#8217;s a &quot;|&quot; separated list of topics. The first element may be &quot;All&quot; in which case all the topics are enabled and the subsequent elements may turn them off, or &quot;None&quot; in which case all the topics are disabled and the subsequent flags may turn them on. If the topic name is prefixed with &quot;^&quot;, then it means that the topic should be disabled. If the topic name is not prefixed, then it means that the topic should be enabled. </p>
<p> The log mask may as well be handled for each diagnostic level separately by setting one or more of the following variables: <i>XRD_LOGMASK_ERROR</i>, <i>XRD_LOGMASK_WARNING</i>, <i>XRD_LOGMASK_INFO</i>, <i>XRD_LOGMASK_DEBUG</i>, and <i>XRD_LOGMASK_DUMP</i>. The default for each level is &quot;All&quot;, except for the <i>Dump</i> level, where the default is &quot;All|^PollerMsg&quot;. This means that, at the <i>Dump</i> level, all the topics but &quot;PollerMsg&quot; are enabled. </p>
<p> Available topics: AppMsg, UtilityMsg, FileMsg, PollerMsg, PostMasterMsg, XRootDTransportMsg, TaskMgrMsg, XRootDMsg, FileSystemMsg, AsyncSockMsg</dl>
<p> XRD_PARALLELEVTLOOP</p>
<dl>
<dt>
<dd> The number of event loops.</dl>
<p> XRD_READRECOVERY</p>
<dl>
<dt>
<dd> Determines if read recovery should be enabled or disabled (enabled by default).</dl>
<p> XRD_WRITERECOVERY</p>
<dl>
<dt>
<dd> Determines if write recovery should be enabled or disabled (enabled by default).</dl>
<p> XRD_CONNECTIONWINDOW (-DIConnectionWindow)</p>
<dl>
<dt>
<dd> A time window for the connection establishment. A connection failure is declared if the connection is not established within the time window. If a connection failure happens earlier then another connection attempt will only be made at the beginning of the next window.</dl>
<p> XRD_CONNECTIONRETRY (-DIConnectionRetry)</p>
<dl>
<dt>
<dd> Number of connection attempts that should be made (number of available connection windows) before declaring a permanent failure.</dl>
<p> XRD_REQUESTTIMEOUT (-DIRequestTimeout)</p>
<dl>
<dt>
<dd> Default value for the time after which an error is declared if it was impossible to get a response to a request.</dl>
<p> XRD_STREAMTIMEOUT (-DIStreamTimeout)</p>
<dl>
<dt>
<dd> Default value for the time after which a connection error is declared (and a recovery attempted) if there are unfulfilled requests and there is no socket activity or a registered wait timeout.</dl>
<p> XRD_SUBSTREAMSPERCHANNEL (-DISubStreamsPerChannel)</p>
<dl>
<dt>
<dd> Number of streams per session.</dl>
<p> XRD_TIMEOUTRESOLUTION (-DITimeoutResolution)</p>
<dl>
<dt>
<dd> Resolution for the timeout events. Ie. timeout events will be processed only every XRD_TIMEOUTRESOLUTION seconds.</dl>
<p> XRD_STREAMERRORWINDOW (-DIStreamErrorWindow)</p>
<dl>
<dt>
<dd> Time after which the permanent failure flags are cleared out and a new connection may be attempted if needed.</dl>
<p> XRD_RUNFORKHANDLER (-DIRunForkHandler)</p>
<dl>
<dt>
<dd> Determines whether the fork handlers should be enabled, making the API fork safe.</dl>
<p> XRD_REDIRECTLIMIT (-DIRedirectLimit)</p>
<dl>
<dt>
<dd> Maximum number of allowed redirections.</dl>
<p> XRD_POLLERPREFERENCE (-DSPollerPreference)</p>
<dl>
<dt>
<dd> A comma separated list of poller implementations in order of preference. The default is: built-in.</dl>
<p> XRD_CLIENTMONITOR (-DSClientMonitor)</p>
<dl>
<dt>
<dd> Path to the client monitor library.</dl>
<p> XRD_CLIENTMONITORPARAM (-DSClientMonitorParam)</p>
<dl>
<dt>
<dd> Additional optional parameters that will be passed to the monitoring object on initialization.</dl>
<p> XRD_WORKERTHREADS (-DIWorkerThreads)</p>
<dl>
<dt>
<dd> Number of threads processing user callbacks.</dl>
<p> XRD_CPPARALLELCHUNKS (-DICPParallelChunks)</p>
<dl>
<dt>
<dd> Maximum number of asynchronous requests being processed by the xrdcp command at any given time.</dl>
<p> XRD_CPCHUNKSIZE (-DICPChunkSize)</p>
<dl>
<dt>
<dd> Size of a single data chunk handled by xrdcp.</dl>
<p> XRD_NETWORKSTACK (-DSNetworkStack)</p>
<dl>
<dt>
<dd> The network stack that the client should use to connect to the server. Possible values are: </p>
<p> <code>IPAuto</code> &#8211; automatically detect which IP stack to use </p>
<p> <code>IPAll</code> &#8211; use IPv6 stack (AF_INET6 sockets) and both IPv6 and IPv4 (mapped to IPv6) addresses </p>
<p> <code>IPv6</code> &#8211; use only IPv6 stack and addresses </p>
<p> <code>IPv4</code> &#8211; use only IPv4 stack (AF_INET sockets) and addresses </p>
<p> <code>IPv4Mapped6</code> &#8211; use IPv6 stack and mapped IPv4 addresses</dl>
<p> XRD_DATASERVERTTL (-DIDataServerTTL)</p>
<dl>
<dt>
<dd> Time period after which an idle connection to a data server should be closed.</dl>
<p> XRD_LOADBALANCERTTL (-DILoadBalancerTTL)</p>
<dl>
<dt>
<dd> Time period after which an idle connection to a manager or a load balancer should be closed.</dl>
<p> XRD_APPNAME (-DSAppName)</p>
<dl>
<dt>
<dd> Override the application name reported to the server.</dl>
<p> XRD_PLUGINCONFDIR</p>
<dl>
<dt>
<dd> A custom location containing client plug-in config files.</dl>
<p> XRD_PLUGIN</p>
<dl>
<dt>
<dd> A default client plug-in to be used.</dl>
<p> XRD_CPINITTIMEOUT (-DICPInitTimeout)</p>
<dl>
<dt>
<dd> Maximum time allowed for the copy process to initialize, ie. open the source and destination files.</dl>
<p> XRD_CPTPCTIMEOUT (-DICPTPCTimeout)</p>
<dl>
<dt>
<dd> Maximum time allowed for a third-party copy operation to finish.</dl>
<p> XRD_TCPKEEPALIVE (-DITCPKeepAlive)</p>
<dl>
<dt>
<dd> Enable/Disable the TCP keep alive functionality</dl>
<p> XRD_TCPKEEPALIVETIME (-DITCPKeepAliveTime)</p>
<dl>
<dt>
<dd> Time between last data packet sent and the first keepalive probe (Linux only)</dl>
<p> XRD_TCPKEEPALIVEINTERVAL (-DITCPKeepAliveInterval)</p>
<dl>
<dt>
<dd> Interval between subsequent keepalive probes (Linux only)</dl>
<p> XRD_TCPKEEPALIVEPROBES (-DITCPKeepProbes)</p>
<dl>
<dt>
<dd> Number of unacknowledged probes before considering the connection dead (Linux only)</dl>
<p> XRD_METALINKPROCESSING</p>
<dl>
<dt>
<dd> Enable/Disable Metalink processing (enabled by default)</dl>
<p> XRD_LOCALMETALINKFILE</p>
<dl>
<dt>
<dd> Enable/Disable local Metalink file processing (by convention the following URL schema has to be used: <a href="root://localfile//path/filename.meta4)">root://localfile//path/filename.meta4)</a></dl>
<p> XRD_GLFNREDIRECTOR</p>
<dl>
<dt>
<dd> The redirector will be used as a last resort if the GLFN tag is specified in a Metalink file.</dl>
<h2>NOTES</h2>
<p> Documentation for all components associated with <code>xrdcp</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a> </p>
<h2>DIAGNOSTICS</h2>
<p> Errors yield an error message and a non-zero exit status. </p>
<h2>LICENSE</h2>
<p> LGPL </p>
<h2>SUPPORT LEVEL</h2>
<p> The <code>xrdcp</code> command is supported by the xrootd collaboration. Contact information can be found at: </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center> </p>
<h2>Index</h2>
