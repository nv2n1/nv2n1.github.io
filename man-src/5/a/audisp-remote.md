---
title: "audisp-remote(5)"
name: "audisp-remote"
section: "5"
letter: "a"
url: "/docs/linux/man/5-audisp-remote/"
description: "audisp-remote.conf – the audisp-remote configuration file"
---

<p>audisp-remote.conf &#8211; the audisp-remote configuration file</p>
<h2>Description</h2>
<p><code>audisp-remote.conf</code> is the file that controls the configuration of the audit remote logging subsystem. The options that are available are as follows:</p>
<dl>
<dt><i>remote_server</i></p>
<dd>This is a one word character string that is the remote server hostname or address that this daemon will send log information to. This can be the numeric address or a resolvable hostname.</p>
<dt><i>port</i></p>
<dd>This option is an unsigned integer that indicates what port to connect to on the remote machine.</p>
<dt><i>local_port</i></p>
<dd>This option is an unsigned integer that indicates what local port to connect from on the local machine. If unspecified (the default) or set to the word <i>any</i> then any available unpriviledged port is used. This is a security mechanism to prevent untrusted user space apps from injecting events into the audit daemon. You should set it to an unused port &lt; 1024 to ensure that only privileged users can bind to that port. Then also set the tcp_client_ports in the aggregating auditd.conf file to match the ports that clients are sending from.</p>
<dt><i>transport</i></p>
<dd>This parameter tells the remote logging app how to send events to the remote system. The only valid value right now is <i>tcp</i>. If set to <i>tcp</i>, the remote logging app will just make a normal clear text connection to the remote system. This is not used if kerberos is enabled.</p>
<dt><i>mode</i></p>
<dd>This parameter tells the remote logging app what strategy to use getting records to the remote system. Valid values are <i>immediate</i>, and <i>forward</i> . If set to <i>immediate</i>, the remote logging app will attempt to send events immediately after getting them. <i>forward</i> , which is not implemented yet, means that it will store the events to disk and then attempt to send the records. If the connection cannot be made, it will queue records until it can connection to the remote system. The depth of the queue is controlled by the <i>queue_depth</i> option.</p>
<dt><i>queue_depth</i></p>
<dd>This option is an unsigned integer that determines how many records can be buffered to disk or in memory before considering it to be a failure sending. This parameter affects the <i>forward</i> mode of the <i>mode</i> option and internal queueing for temporary network outtages. The default depth is 200.</p>
<dt><i>format</i></p>
<dd>This parameter tells the remote logging app what data format will be used for the messages sent over the network. The default is <i>managed</i> which adds some overhead to ensure each message is properly handled on the remote end, and to receive status messages from the remote server. If <i>ascii</i> is given instead, each message is a simple ASCII text line with no overhead at all.</p>
<dt><i>network_retry_time</i></p>
<dd>The time, in seconds, between retries when a network error is detected. Note that this pause applies starting after the second attempt, so as to avoid unneeded delays if a reconnect is sufficient to fix the problem. The default is 1 second.</p>
<dt><i>max_tries_per_record</i></p>
<dd>The maximum number of times an attempt is made to deliver each message. The minimum value is one, as even a completely successful delivery requires at least one try. If too many attempts are made, the network_failure_action action is performed. The default is 3.</p>
<dt><i>max_time_per_record</i></p>
<dd>The maximum amount of time, in seconds, spent attempting to deliver each message. Note that both this and <i>max_tries_per_record</i> should be set, as each try may take a long time to time out. The default value is 5 seconds. If too much time is used on a message, the network_failure_action action is performed.</p>
<dt><i>heartbeat_timeout</i></p>
<dd>This parameter determines how often in seconds the client should send a heartbeat event to the remote server. This is used to let both the client and server know that each end is alive and has not terminated in a way that it did not shutdown the connection uncleanly. This value must be coordinated with the server&#8217;s <i>tcp_client_max_idle</i> setting. The default value is 0 which disables sending a heartbeat.</p>
<dt><i>network_failure_action</i></p>
<dd>This parameter tells the system what action to take whenever there is an error detected when sending audit events to the remote system. Valid values are <i>ignore</i>, <i>syslog</i>, <i>exec</i>, <i>suspend</i>, <i>single</i>, <i>halt</i>, and <i>stop</i>. If set to <i>ignore</i>, the audit daemon does nothing. <i>Syslog</i> means that it will issue a warning to syslog. This is the default. <i>exec</i> /path-to-script will execute the script. You cannot pass parameters to the script. <i>Suspend</i> will cause the remote logging app to stop sending records to the remote system. The logging app will still be alive. The <i>single</i> option will cause the remote logging app to put the computer system in single user mode. The <i>stop</i> option will cause the remote logging app to exit, but leave other plugins running. The <i>halt</i> option will cause the remote logging app to shutdown the computer system.</p>
<dt><i>disk_low_action</i></p>
<dd>Likewise, this parameter tells the system what action to take if the remote end signals a disk low error. The default is to ignore it.</p>
<dt><i>disk_full_action</i></p>
<dd>Likewise, this parameter tells the system what action to take if the remote end signals a disk full error. The default is to ignore it.</p>
<dt><i>disk_error_action</i></p>
<dd>Likewise, this parameter tells the system what action to take if the remote end signals a disk error. The default is to log it to syslog.</p>
<dt><i>remote_ending_action</i></p>
<dd>Likewise, this parameter tells the system what action to take if the remote end signals a disk error. This action has one additional option, <i>reconnect</i> which tells the remote plugin to attempt to reconnect to the server upon receipt of the next audit record. If it is unsuccessful, the audit record could be lost. The default is to suspend logging.</p>
<dt><i>generic_error_action</i></p>
<dd>Likewise, this parameter tells the system what action to take if the remote end signals an error we don&#8217;t recognize. The default is to log it to syslog.</p>
<dt><i>generic_warning_action</i></p>
<dd>Likewise, this parameter tells the system what action to take if the remote end signals a warning we don&#8217;t recognize. The default is to log it to syslog.</p>
<dt><i>enable_krb5</i></p>
<dd>If set to &quot;yes&quot;, Kerberos 5 will be used for authentication and encryption. Default is &quot;no&quot;. Note that encryption can only be used with managed connections, not plain ASCII.</p>
<dt><i>krb5_principal</i></p>
<dd>If specified, This is the expected principal for the server. The client and server will use the specified principal to negotiate the encryption. The format for the <i>krb5_principal</i> is like somename/hostname, see the auditd.conf man page for details. If not specified, the krb5_client_name and remote_server values are used.</p>
<dt><i>krb5_client_name</i></p>
<dd>This specifies the name portion of the client&#8217;s own principal. If unspecified, the default is &quot;auditd&quot;. The remainder of the principal will consist of the host&#8217;s fully qualified domain name and the default Kerberos realm, like this: <i>auditd/host14.example.com [at] EXAMPLE.COM</i> (assuming you gave &quot;auditd&quot; as the krb_client_name). Note that the client and server must have the same principal name and realm.</p>
<dt><i>krb5_key_file</i></p>
<dd>Location of the key for this client&#8217;s principal. Note that the key file must be owned by root and mode 0400. The default is <i>/etc/audisp/audisp-remote.key</i> </p>
<h2>Notes</h2>
<p>Specifying a local port may make it difficult to restart the audit subsystem due to the previous connection being in a TIME_WAIT state, if you&#8217;re reconnecting to and from the same hosts and ports as before. The network failure logic works as follows: The first attempt to deliver normally &quot;just works&quot;. If it doesn&#8217;t, a second attempt is immediately made, perhaps after reconnecting to the server. If the second attempt also fails, <i>audispd-remote</i> pauses for the configured time and tries again. It continues to pause and retry until either too many attempts have been made or the allowed time expires. Note that these times govern the maximum amount of time the remote server is allowed in order to reboot, if you want to maintain logging across a reboot. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8), <code><a href="/docs/linux/man/8-audisp-remote/">audisp-remote</a>(8),</code> <code><a href="/docs/linux/man/5-auditd-conf/">auditd.conf</a>(5).</code></p>
<h2>Author</h2>
<p>Steve Grubb</p>
