---
title: "xinetd-conf(5)"
name: "xinetd-conf"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xinetd-conf/"
description: "xinetd.conf – Extended Internet Services Daemon configuration file"
---

<p>xinetd.conf &#8211; Extended Internet Services Daemon configuration file</p>
<h2>Description</h2>
<p><code>xinetd.conf</code> is the configuration file that determines the services provided by <code>xinetd</code>. Any line whose first non-white-space character is a &#8216;#&#8217; is considered a comment line. Empty lines are ignored. The file contains entries of the form:</p>
<dl>
<dd>
<pre><code>service &lt;service_name&gt;
{
</dd><dl><dt></dt><dd>&lt;attribute&gt; &lt;assign_op&gt; &lt;value&gt; &lt;value&gt; ...
</code><i>...</i>
</dd></dl>
}</pre>
</dl>
<p> The assignment operator, <i>assign_op,</i> can be one of <code>&#8216;=&#8217;, </code> <code>&#8216;+=&#8217;,</code> <code>&#8216;-=&#8217;.</code> The majority of attributes support only the simple assignment operator, <code>&#8216;=&#8217;.</code> Attributes whose value is a set of values support all assignment operators. For such attributes, <code>&#8216;+=&#8217; </code> means adding a value to the set and <code>&#8216;-=&#8217;</code> means removing a value from the set. A list of these attributes will be given after all the attributes are described. Each entry defines a service identified by the <i>service_name</i>. The following is a list of available attributes:</p>
<dl>
<dt><code>id</code></dt>
<dd>This attribute is used to uniquely identify a service. This is useful because there exist services that can use different protocols and need to be described with different entries in the configuration file. By default, the service id is the same as the service name.</dd>
<dt><code>type</code></dt>
<dd>Any combination of the following values may be used:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>RPC</code></dt>
<dd>if this is an RPC service</dd>
<dt><code>INTERNAL</code></dt>
<dd>if this is a service provided by <code>xinetd</code>.</dd>
<dt><code>TCPMUX/TCPMUXPLUS</code></dt>
<dd>if this is a service that will be started according to the RFC 1078 protocol on the TCPMUX well-known port. See the section describing TCPMUX services below.</dd>
<dt><code>UNLISTED</code></dt>
<dd>if this is a service not listed in a standard system file (like <i>/etc/rpc </i> for RPC services, or <i>/etc/services</i> for non-RPC services).</dd></dl>
</dl>
<dt><code>flags</code></dt>
<dd>Any combination of the following flags may be used:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>INTERCEPT</code></dt>
<dd>Intercept packets or accepted connections in order to verify that they are coming from acceptable locations (internal or multi-threaded services cannot be intercepted).</dd>
<dt><code>NORETRY</code></dt>
<dd>Avoid retry attempts in case of fork failure.</dd>
<dt><code>IDONLY</code></dt>
<dd>Accept connections only when the remote end identifies the remote user (i.e. the remote host must run an identification server). This flag applies only to connection-based services. This flag is ineffective if the <code>USERID</code> log option is not used.</dd>
<dt><code>NAMEINARGS</code></dt>
<dd>This will cause the first argument in &quot;server_args&quot; to be argv[0] when executing the server, as specified in &quot;server&quot;. This allows you to use tcpd by putting tcpd in &quot;server&quot; and the name of the server in &quot;server_args&quot; like in normal inetd. This flag has to be specified before &quot;server_args&quot;, otherwise is not taken into account.</dd>
<dt><code>NODELAY</code></dt>
<dd>If the service is a tcp service and the NODELAY flag is set, then the TCP_NODELAY flag will be set on the socket. If the service is not a tcp service, this option has no effect.</dd>
<dt><code>KEEPALIVE</code></dt>
<dd>If the service is a tcp service and the KEEPALIVE flag is set, then the SO_KEEPALIVE socket flag will be set on the socket. If the service is not a tcp service, this option has no effect.</dd>
<dt><code>NOLIBWRAP</code></dt>
<dd>This disables internal calling of the tcpwrap library to determine access to the service. This may be needed in order to use libwrap functionality not available to long-running processes such as xinetd; in this case, the tcpd program can be called explicitly (see also the NAMEINARGS flag). For RPC services using TCP transport, this flag is automatically turned on, because xinetd cannot get remote host address information for the rpc port.</dd>
<dt><code>SENSOR</code></dt>
<dd>This replaces the service with a sensor that detects accesses to the specified port. NOTE: It will NOT detect stealth scans. This flag should be used only on services that you know you don&#8217;t need. When an access is made to this service&#8217;s port, the IP Address is added to a global no_access list. This causes all subsequent accesses from the originating IP address to be denied access until the deny_time setting expires. The amount of time spent on this list is configurable as the deny_time attribute. The SENSOR flag will also cause xinetd to consider the server attribute to be INTERNAL no matter what is typed on the same line. Another important thing to remember is that if the socket_type is set to stream, then the wait attribute should be set to no.</dd>
<dt><code>IPv4</code></dt>
<dd>Sets the service to be an IPv4 service (AF_INET).</dd>
<dt><code>IPv6</code></dt>
<dd>Sets the service to be an IPv6 service (AF_INET6), if IPv6 is available on the system.</dd>
<dt><code>LABELED</code></dt>
<dd>The LABELED flag will tell xinetd to change the child processes SE Linux context to match that of the incoming connection as it starts the service. This only works for external tcp non-waiting servers and is an error if applied to an internal, udp, or tcp-wait server.</dd>
<dt><code>REUSE</code></dt>
<dd>The REUSE flag is deprecated. All services now implicitly use the REUSE flag.</dd></dl>
</dl>
<dt><code>disable</code></dt>
<dd>This is boolean &quot;yes&quot; or &quot;no&quot;. This will result in the service being disabled and not starting. See the DISABLE flag description.</dd>
<dt><code>socket_type</code></dt>
<dd>Possible values for this attribute include:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>stream</i></dt>
<dd>stream-based service</dd>
<dt><i>dgram</i></dt>
<dd>datagram-based service</dd>
<dt><i>raw</i></dt>
<dd>service that requires direct access to IP</dd>
<dt><i>seqpacket</i></dt>
<dd>service that requires reliable sequential datagram transmission</dd></dl>
</dl>
<dt><code>protocol</code></dt>
<dd>determines the protocol that is employed by the service. The protocol must exist in <i>/etc/protocols.</i> If this attribute is not defined, the default protocol employed by the service will be used.</dd>
<dt><code>wait</code></dt>
<dd>This attribute determines if the service is single-threaded or multi-threaded and whether or not xinetd accepts the connection or the server program accepts the connection. If its value is <i>yes</i>, the service is single-threaded; this means that <code>xinetd</code> will start the server and then it will stop handling requests for the service until the server dies and that the server software will accept the connection. If the attribute value is <i>no</i>, the service is multi-threaded and <code>xinetd</code> will keep handling new service requests and xinetd will accept the connection. It should be noted that udp/dgram services normally expect the value to be yes since udp is not connection oriented, while tcp/stream servers normally expect the value to be no.</dd>
<dt><code>user</code></dt>
<dd>determines the uid for the server process. The user attribute can either be numeric or a name. If a name is given (recommended), the user name must exist in <i>/etc/passwd.</i> This attribute is ineffective if the effective user ID of <code>xinetd</code> is not super-user.</dd>
<dt><code>group</code></dt>
<dd>determines the gid for the server process. The group attribute can either be numeric or a name. If a name is given (recommended), the group name must exist in <i>/etc/group.</i> If a group is not specified, the group of <i>user</i> will be used (from <i>/etc/passwd).</i> This attribute is ineffective if the effective user ID of <code>xinetd</code> is not super-user and if the <code>groups</code> attribute is not set to &#8216;yes&#8217;.</dd>
<dt><code>instances</code></dt>
<dd>determines the number of servers that can be simultaneously active for a service (the default is no limit). The value of this attribute can be either a number or <code>UNLIMITED</code> which means that there is no limit.</dd>
<dt><code>nice</code></dt>
<dd>determines the server priority. Its value is a (possibly negative) number; check nice(3) for more information.</dd>
<dt><code>server</code></dt>
<dd>determines the program to execute for this service.</dd>
<dt><code>server_args</code></dt>
<dd>determines the arguments passed to the server. In contrast to <code>inetd</code>, the server name should <i>not</i> be included in <i>server_args</i>.</dd>
<dt>+.B libwrap</dt>
<dd>overrides the service name passed to libwrap (which defaults to the server name, the first server_args component with NAMEINARGS, the id for internal services and the service name for redirected services). This attribute is only valid if xinetd has been configured with the libwrap option.</dd>
<dt><code>only_from</code></dt>
<dd>determines the remote hosts to which the particular service is available. Its value is a list of IP addresses which can be specified in any combination of the following ways:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>a)</code></dt>
<dd>a numeric address in the form of %d.%d.%d.%d. If the rightmost components are 0, they are treated as wildcards (for example, 128.138.12.0 matches all hosts on the 128.138.12 subnet). 0.0.0.0 matches all Internet addresses. IPv6 hosts may be specified in the form of abcd:ef01::2345:6789. The rightmost rule for IPv4 addresses does not apply to IPv6 addresses.</dd>
<dt><code>b)</code></dt>
<dd>a factorized address in the form of %d.%d.%d.{%d,%d,&#8230;}. There is no need for all 4 components (i.e. %d.%d.{%d,%d,&#8230;%d} is also ok). However, the factorized part must be at the end of the address. This form does not work for IPv6 hosts.</dd>
<dt><code>c)</code></dt>
<dd>a network name (from <i>/etc/networks). This form does not work for IPv6 hosts.</i></dd>
<dt><code>d)</code></dt>
<dd>a host name. When a connection is made to xinetd, a reverse lookup is performed, and the canonical name returned is compared to the specified host name. You may also use domain names in the form of .domain.com. If the reverse lookup of the client&#8217;s IP is within .domain.com, a match occurs.</dd>
<dt><code>e)</code></dt>
<dd>an ip address/netmask range in the form of 1.2.3.4/32. IPv6 address/netmask ranges in the form of 1234::/46 are also valid.</dd></dl>
</dl>
<dd>Specifying this attribute without a value makes the service available to nobody.</dd>
<dt><code>no_access</code></dt>
<dd>determines the remote hosts to which the particular service is unavailable. Its value can be specified in the same way as the value of the <code>only_from</code> attribute. These two attributes determine the location access control enforced by <code>xinetd</code>. If none of the two is specified for a service, the service is available to anyone. If both are specified for a service, the one that is the better match for the address of the remote host determines if the service is available to that host (for example, if the <code>only_from</code> list contains 128.138.209.0 and the <code>no_access</code> list contains 128.138.209.10 then the host with the address 128.138.209.10 can not access the service).</dd>
<dt><code>access_times</code></dt>
<dd>determines the time intervals when the service is available. An interval has the form <i>hour:min-hour:min</i> (connections <i>will </i> be accepted at the bounds of an interval). Hours can range from 0 to 23 and minutes from 0 to 59.</dd>
<dt><code>log_type</code></dt>
<dd>determines where the service log output is sent. There are two formats:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>SYSLOG </code><i>syslog_facility [syslog_level]</i></dt>
<dd>The log output is sent to syslog at the specified facility. Possible facility names include: <i>daemon,</i> <i>auth,</i> <i>authpriv,</i> <i>user,</i> <i>mail,</i> <i>lpr,</i> <i>news,</i> <i>uucp,</i> <i>ftp</i> <i>local0-7.</i> Possible level names include: <i>emerg,</i> <i>alert,</i> <i>crit,</i> <i>err,</i> <i>warning,</i> <i>notice,</i> <i>info,</i> <i>debug.</i> If a level is not present, the messages will be recorded at the <i>info</i> level.</dd>
<dt><code>FILE </code><i>file [soft_limit [hard_limit]]</i></dt>
<dd>The log output is appended to <i>file</i> which will be created if it does not exist. Two limits on the size of the log file can be optionally specified. The first limit is a soft one; <code>xinetd </code> will log a message the first time this limit is exceeded (if <code>xinetd</code> logs to syslog, the message will be sent at the <i>alert</i> priority level). The second limit is a hard limit; <code>xinetd </code> will stop logging for the affected service (if the log file is a common log file, then more than one service may be affected) and will log a message about this (if <code>xinetd</code> logs to syslog, the message will be sent at the <i>alert</i> priority level). If a hard limit is not specified, it defaults to the soft limit increased by 1% but the extra size must be within the parameters LOG_EXTRA_MIN and LOG_EXTRA_MAX which default to 5K and 20K respectively (these constants are defined in <i>xconfig.h</i>).</dd></dl>
</dl>
<dt><code>log_on_success</code></dt>
<dd>determines what information is logged when a server is started and when that server exits (the service id is always included in the log entry). Any combination of the following values may be specified:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>PID</code></dt>
<dd>logs the server process id (if the service is implemented by <code>xinetd</code> without forking another process the logged process id will be 0)</dd>
<dt><code>HOST</code></dt>
<dd>logs the remote host address</dd>
<dt><code>USERID</code></dt>
<dd>logs the user id of the remote user using the RFC 1413 identification protocol. This option is available only for multi-threaded stream services.</dd>
<dt><code>EXIT</code></dt>
<dd>logs the fact that a server exited along with the exit status or the termination signal (the process id is also logged if the <code>PID</code> option is used)</dd>
<dt><code>DURATION </code></dt>
<dd>logs the duration of a service session</dd>
<dt><code>TRAFFIC</code></dt>
<dd>logs the total bytes in and out for a redirected service.</dd></dl>
</dl>
<dt><code>log_on_failure</code></dt>
<dd>determines what information is logged when a server cannot be started (either because of a lack of resources or because of access control restrictions). The service id is always included in the log entry along with the reason for failure. Any combination of the following values may be specified:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>HOST</code></dt>
<dd>logs the remote host address.</dd>
<dt><code>USERID</code></dt>
<dd>logs the user id of the remote user using the RFC 1413 identification protocol. This option is available only for multi-threaded stream services.</dd>
<dt><code>ATTEMPT</code></dt>
<dd>logs the fact that a failed attempt was made (this option is implied by all others).</dd></dl>
</dl>
<dt><code>rpc_version</code></dt>
<dd>determines the RPC version for a RPC service. The version can be a single number or a range in the form <i>number</i>&#8211;<i>number</i>.</dd>
<dt><code>rpc_number</code></dt>
<dd>determines the number for an <i>UNLISTED</i> RPC service (this attribute is ignored if the service is not unlisted).</dd>
<dt><code>env</code></dt>
<dd>The value of this attribute is a list of strings of the form &#8216;name=value&#8217;. These strings will be added to the environment before starting a server (therefore the server&#8217;s environment will include <code>xinetd</code>&#8216;s environment plus the specified strings).</dd>
<dt><code>passenv</code></dt>
<dd>The value of this attribute is a list of environment variables from <code>xinetd</code>&#8216;s environment that will be passed to the server. An empty list implies passing no variables to the server except for those explicitly defined using the <i>env</i> attribute. (notice that you can use this attribute in conjunction with the <i>env</i> attribute to specify exactly what environment will be passed to the server).</dd>
<dt><code>port</code></dt>
<dd>determines the service port. If this attribute is specified for a service listed in <i>/etc/services,</i> it must be equal to the port number listed in that file.</dd>
<dt><code>redirect</code></dt>
<dd>Allows a tcp service to be redirected to another host. When xinetd receives a tcp connection on this port it spawns a process that establishes a connection to the host and port number specified, and forwards all data between the two hosts. This option is useful when your internal machines are not visible to the outside world. Syntax is: redirect = (ip address) (port). You can also use a hostname instead of the IP address in this field. The hostname lookup is performed only once, when xinetd is started, and the first IP address returned is the one that is used until xinetd is restarted. The &quot;server&quot; attribute is not required when this option is specified. If the &quot;server&quot; attribute is specified, this attribute takes priority.</dd>
<dt><code>bind</code></dt>
<dd>Allows a service to be bound to a specific interface on the machine. This means you can have a telnet server listening on a local, secured interface, and not on the external interface. Or one port on one interface can do something, while the same port on a different interface can do something completely different. Syntax: bind = (ip address of interface).</dd>
<dt><code>interface</code></dt>
<dd>Synonym for bind.</dd>
<dt><code>banner</code></dt>
<dd>Takes the name of a file to be splatted at the remote host when a connection to that service is established. This banner is printed regardless of access control. It should *always* be printed when a connection has been made. <code>xinetd</code> outputs the file as-is, so you must ensure the file is correctly formatted for the service&#8217;s protocol. In paticular, if the protocol requires CR-LF pairs for line termination, you must supply them.</dd>
<dt><code>banner_success</code></dt>
<dd>Takes the name of a file to be splatted at the remote host when a connection to that service is granted. This banner is printed as soon as access is granted for the service. <code>xinetd</code> outputs the file as-is, so you must ensure the file is correctly formatted for the service&#8217;s protocol. In paticular, if the protocol requires CR-LF pairs for line termination, you must supply them.</dd>
<dt><code>banner_fail</code></dt>
<dd>Takes the name of a file to be splatted at the remote host when a connection to that service is denied. This banner is printed immediately upon denial of access. This is useful for informing your users that they are doing something bad and they shouldn&#8217;t be doing it anymore. <code>xinetd</code> outputs the file as-is, so you must ensure the file is correctly formatted for the service&#8217;s protocol. In paticular, if the protocol requires CR-LF pairs for line termination, you must supply them.</dd>
<dt><code>per_source</code></dt>
<dd>Takes an integer or &quot;UNLIMITED&quot; as an argument. This specifies the maximum instances of this service per source IP address. This can also be specified in the defaults section.</dd>
<dt><code>cps</code></dt>
<dd>Limits the rate of incoming connections. Takes two arguments. The first argument is the number of connections per second to handle. If the rate of incoming connections is higher than this, the service will be temporarily disabled. The second argument is the number of seconds to wait before re-enabling the service after it has been disabled. The default for this setting is 50 incoming connections and the interval is 10 seconds.</dd>
<dt><code>max_load</code></dt>
<dd>Takes a floating point value as the load at which the service will stop accepting connections. For example: 2 or 2.5. The service will stop accepting connections at this load. This is the one minute load average. This is an OS dependent feature, and currently only Linux, Solaris, and FreeBSD are supported for this. This feature is only avaliable if xinetd was configured with the -with-loadavg option.</dd>
<dt><code>groups</code></dt>
<dd>Takes either &quot;yes&quot; or &quot;no&quot;. If the groups attribute is set to &quot;yes&quot;, then the server is executed with access to the groups that the server&#8217;s effective UID has access to. Alternatively, if the <code>group</code> attribute is set, the server is executed with access to the groups specified. If the groups attribute is set to &quot;no&quot;, then the server runs with no supplementary groups. This attribute must be set to &quot;yes&quot; for many BSD systems. This attribute can be set in the defaults section as well.</dd>
<dt><code>mdns</code></dt>
<dd>Takes either &quot;yes&quot; or &quot;no&quot;. On systems that support mdns registration of services (currently only Mac OS X), this will enable or disable registration of the service. This defaults to &quot;yes&quot;.</dd>
<dt><code>umask</code></dt>
<dd>Sets the inherited umask for the service. Expects an octal value. This option may be set in the &quot;defaults&quot; section to set a umask for all services. xinetd sets its own umask to the previous umask OR&#8217;d with 022. This is the umask that will be inherited by all child processes if the umask option is not used.</dd>
<dt><code>enabled</code></dt>
<dd>Takes a list of service ID&#8217;s to enable. This will enable only the services listed as arguments to this attribute; the rest will be disabled. If you have 2 ftp services, you will need to list both of their ID&#8217;s and not just ftp. (ftp is the service name, not the ID. It might accidentally be the ID, but you better check.) Note that the service &quot;disable&quot; attribute and &quot;DISABLE&quot; flag can prevent a service from being enabled despite being listed in this attribute.</dd>
<dt><code>include</code></dt>
<dd>Takes a filename in the form of &quot;include /etc/xinetd/service&quot;. The file is then parsed as a new configuration file. It is not the same thing as pasting the file into xinetd.conf where the include directive is given. The included file must be in the same form as xinetd.conf. This may not be specified from within a service. It must be specified outside a service declaration.</dd>
<dt><code>includedir</code></dt>
<dd>Takes a directory name in the form of &quot;includedir /etc/xinetd.d&quot;. Every file inside that directory, excluding files with names containing a dot (&#8216;.&#8217;) or ending with a tilde (&#8216;~&#8217;), will be parsed as xinetd configuration files. The files will be parsed in alphabetical order according to the C locale. This allows you to specify services one per file within a directory. The <code>includedir</code> directive may not be specified from within a service declaration.</dd>
<dt><code>rlimit_as</code></dt>
<dd>Sets the Address Space resource limit for the service. One parameter is required, which is either a positive integer representing the number of bytes to set the limit to (K or M may be used to specify kilobytes/megabytes) or &quot;UNLIMITED&quot;. Due to the way Linux&#8217;s libc malloc is implemented, it is more useful to set this limit than rlimit_data, rlimit_rss and rlimit_stack. This resource limit is only implemented on Linux systems.</dd>
<dt><code>rlimit_files</code></dt>
<dd>Sets the maximum number of open files that the service may use. One parameter is required, which is a positive integer representing the number of open file descriptors. Practical limit of this number is around 1024000.</dd>
<dt><code>rlimit_cpu</code></dt>
<dd>Sets the maximum number of CPU seconds that the service may use. One parameter is required, which is either a positive integer representing the number of CPU seconds limit to, or &quot;UNLIMITED&quot;.</dd>
<dt><code>rlimit_data</code></dt>
<dd>Sets the maximum data size resource limit for the service. One parameter is required, which is either a positive integer representing the number of bytes or &quot;UNLIMITED&quot;.</dd>
<dt><code>rlimit_rss</code></dt>
<dd>Sets the maximum resident set size limit for the service. Setting this value low will make the process a likely candidate for swapping out to disk when memory is low. One parameter is required, which is either a positive integer representing the number of bytes or &quot;UNLIMITED&quot;.</dd>
<dt><code>rlimit_stack</code></dt>
<dd>Set the maximum stack size limit for the service. One parameter is required, which is either a positive integer representing the number of bytes or &quot;UNLIMITED&quot;.</dd>
<dt><code>deny_time</code></dt>
<dd>Sets the time span that access to all services on all IP addresses are denied to someone that sets off the SENSOR. The unit of time is in minutes. Valid options are: FOREVER, NEVER, and a numeric value. FOREVER causes the IP address not to be purged until xinetd is restarted. NEVER has the effect of just logging the offending IP address. A typical time value would be 60 minutes. This should stop most DOS attacks while allowing IP addresses that come from a pool to be recycled for legitimate purposes. This option must be used in conjunction with the SENSOR flag.</dd></dl>
<p> You don&#8217;t need to specify all of the above attributes for each service. The necessary attributes for a service are:</p>
<dl>
<dd>
</dd><dl>
<dt><code>socket_type</code></dt>
<dd>
</dd><dt><code>user</code></dt>
<dd>(non-<i>internal</i> services only)</dd>
<dt><code>server</code></dt>
<dd>(non-<i>internal</i> services only)</dd>
<dt><code>wait</code></dt>
<dd>
</dd><dt><code>protocol</code></dt>
<dd>(<i>RPC</i> and <i>unlisted</i> services only)</dd>
<dt><code>rpc_version</code></dt>
<dd>(<i>RPC</i> services only)</dd>
<dt><code>rpc_number</code></dt>
<dd>(<i>unlisted</i> RPC services only)</dd>
<dt><code>port</code></dt>
<dd>(<i>unlisted</i> non-RPC services only)</dd></dl>
</dl>
<p> The following attributes support all assignment operators:</p>
<dl>
<dd>
</dd><dl>
<dt><code>only_from</code></dt>
<dd>
</dd><dt><code>no_access</code></dt>
<dd>
</dd><dt><code>log_on_success</code></dt>
<dd>
</dd><dt><code>log_on_failure</code></dt>
<dd>
</dd><dt><code>passenv</code></dt>
<dd>
</dd><dt><code>env</code></dt>
<dd>(does not support the <code>&#8216;-=&#8217;</code> operator)</dd></dl>
</dl>
<p> These attributes can also appear more than once in a service entry. The remaining attributes support only the <code>&#8216;=&#8217;</code> operator and can appear at most once in a service entry. The configuration file may also contain a single defaults entry that has the form </p>
<pre><code>defaults
{
    &lt;attribute&gt; = &lt;value&gt; &lt;value&gt; ...
    ...
}</code></pre>
<p> This entry provides default attribute values for service entries that don&#8217;t specify those attributes. Possible default attributes:</p>
<dl>
<dd>
</dd><dl>
<dt><code>log_type</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>bind </code></dt>
<dd>
</dd><dt><code>per_source </code></dt>
<dd>
</dd><dt><code>umask </code></dt>
<dd>
</dd><dt><code>log_on_success</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>log_on_failure</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>only_from</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>no_access</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>passenv</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>instances</code></dt>
<dd>
</dd><dt><code>disabled</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>enabled</code></dt>
<dd>(cumulative effect)</dd>
<dt><code>banner </code></dt>
<dd>
</dd><dt><code>banner_success </code></dt>
<dd>
</dd><dt><code>banner_fail</code></dt>
<dd>
</dd><dt><code>per_source </code></dt>
<dd>
</dd><dt><code>groups </code></dt>
<dd>
</dd><dt><code>cps </code></dt>
<dd>
</dd><dt><code>max_load </code></dt>
<dd>
</dd><dt></dt></dl>
</dl>
<dd>Attributes with a cumulative effect can be specified multiple times with the values specified each time accumulating (i.e. &#8216;=&#8217; does the same thing as &#8216;+=&#8217;). With the exception of <i>disabled</i> they all have the same meaning as if they were specified in a service entry. <i>disabled</i> determines services that are disabled even if they have entries in the configuration file. This allows for quick reconfiguration by specifying disabled services with the <i>disabled</i> attribute instead of commenting them out. The value of this attribute is a list of space separated service ids. <i>enabled </i> has the same properties as disabled. The difference being that <i>enabled </i> is a list of which services are to be enabled. If <i>enabled </i> is specified, only the services specified are available. If <i>enabled </i> is not specified, all services are assumed to be enabled, except those listed in <i>disabled.</i> </dd>
<h2>Internal Services</h2>
<p><code>xinetd</code> provides the following services internally (both stream and datagram based): <i>echo,</i> <i>time,</i> <i>daytime,</i> <i>chargen,</i> and <i>discard.</i> These services are under the same access restrictions as all other services except for the ones that don&#8217;t require <code>xinetd</code> to fork another process for them. Those ones (<i>time</i>, <i>daytime</i>, and the datagram-based <i>echo</i>, <i>chargen</i>, and <i>discard</i>) have no limitation in the number of <code>instances.</code></p>
<h2>TCPMUX Services</h2>
<p><code>xinetd</code> supports TCPMUX services that conform to RFC 1078. These services may not have a well-known port associated with them, and can be accessed via the TCPMUX well-known port. </p>
<p> For each service that is to be accessed via TCPMUX, a service entry in <code>/etc/xinetd.conf</code> or in a configuration file in an <code>includedir</code> directory must exist. </p>
<p> The <i>service_name</i> field (as defined above for each service in any <code>xinetd</code> configuration file) must be identical to the string that is passed (according to RFC 1078 protocol) to <code>xinetd</code> when the remote service requestor first makes the connection on the TCPMUX well-known port. Private protocols should use a service name that has a high probability of being unique. One way is to prepend the service name with some form of organization ID. </p>
<p> The <i>type</i> field can be either <code>TCPMUX</code> or <code>TCPMUXPLUS</code>. If the type is <code>TCPMUXPLUS</code>, <code>xinetd</code> will handle the initial protocol handshake (as defined in RFC 1078) with the calling process before initiating the service. If the type is <code>TCPMUX</code>, the server that is started is responsible for performing the handshake. </p>
<p> The <i>type</i> field should also include <code>UNLISTED</code> if the service is not listed in a standard system file (like <i>/etc/rpc</i> for RPC services, or <i>/etc/services</i> for non-RPC services). </p>
<p> The <i>socket_type</i> for these services must be <code>stream</code>, and the <i>protocol</i> must be <code>tcp</code>. </p>
<p> Following is a sample TCPMUX service configuration:</p>
<dl>
<dd>
<pre>service myorg_server
{
</dd><dl><dl><dt>disable</dt><dd>= no
</dd><dt>type</dt><dd>= TCPMUX
</dd><dt>socket_type</dt><dd>= stream
</dd><dt>protocol</dt><dd>= tcp
</dd><dt>wait</dt><dd>= no
</dd><dt>user</dt><dd>= root
</dd><dt>server</dt><dd>= /usr/etc/my_server_exec
</dd></dl></dl>
}</pre>
</dl>
<p> Besides a service entry for each service that can be accessed via the TCPMUX well-known port, a service entry for TCPMUX itself must also be included in the <code>xinetd</code> configuration. Consider the following sample:</p>
<dl>
<dd>
<pre>service tcpmux
{
</dd><dl><dl><dt>type</dt><dd>= INTERNAL
</dd><dt>id</dt><dd>= tcpmux
</dd><dt>socket_type</dt><dd>= stream
</dd><dt>protocol</dt><dd>= tcp
</dd><dt>user</dt><dd>= root
</dd><dt>wait</dt><dd>= no
</dd></dl></dl>
}</pre>
</dl>
<h2>Notes</h2>
<dl>
<dt>1.</dt>
<dd>The following service attributes <i>cannot</i> be changed on reconfiguration: <code>socket_type,</code> <code>wait,</code> <code>protocol,</code> <code>type.</code></dd>
<dt>2.</dt>
<dd>When the attributes <i>only_from</i> and <i>no_access</i> are not specified for a service (either directly or via <i>defaults</i>) the address check is considered successful (i.e. access will not be denied).</dd>
<dt>3.</dt>
<dd>The address check is based on the IP address of the remote host and not on its domain address. We do this so that we can avoid remote name lookups which may take a long time (since <code>xinetd</code> is single-threaded, a name lookup will prevent the daemon from accepting any other requests until the lookup is resolved). The down side of this scheme is that if the IP address of a remote host changes, then access to that host may be denied until <code>xinetd</code> is reconfigured. Whether access is actually denied or not will depend on whether the new host IP address is among those allowed access. For example, if the IP address of a host changes from 1.2.3.4 to 1.2.3.5 and only_from is specified as 1.2.3.0 then access will not be denied.</dd>
<dt>4.</dt>
<dd>If the <code>USERID</code> log option is specified and the remote host either does not run an identification server or the server sends back a bad reply, access will not be denied unless the <i>IDONLY</i> service flag is used.</dd>
<dt>5.</dt>
<dd>Interception works by forking a process which acts as a filter between the remote host(s) and the local server. This obviously has a performance impact so it is up to you to make the compromise between security and performance for each service. The following tables show the overhead of interception. The first table shows the time overhead-per-datagram for a UDP-based service using various datagram sizes. For TCP-based services we measured the bandwidth reduction because of interception while sending a certain amount of data from client to server (the time overhead should the same as for UDP-based services but it is &quot;paid&quot; only by the first packet of a continuous data transmission). The amount of data is given in the table as <i>system_calls</i>x<i>data_sent_per_call</i>, i.e. each <i><a href="/docs/linux/man/2-send/">send</a>(2)</i> system call transferred so many bytes of data. The bandwidth reduction is given in terms of bytes per second and as a percentage of the bandwidth when interception is not performed. All measurements were done on a SparcStation IPC running SunOS 4.1.</dd>
<dl>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt>Datagram size (bytes)</dt>
<dd>Latency (msec)</dd>
<dt>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</dt>
<dd>&#8212;&#8212;&#8212;&#8212;&#8211;</dd>
<dt>64</dt>
<dd>1.19</dd>
<dt>256</dt>
<dd>1.51</dd>
<dt>1024</dt>
<dd>1.51</dd>
<dt>4096</dt>
<dd>3.58</dd>
<dt>Bytes sent</dt>
<dd>Bandwidth reduction</dd>
<dt>&#8212;&#8212;&#8212;-</dt>
<dd>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</dd>
<dt>10000&#215;64</dt>
<dd>941 (1.2%)</dd>
<dt>10000&#215;256</dt>
<dd>4,231 (1.8%)</dd>
<dt>10000&#215;1024</dt>
<dd>319,300 (39.5%)</dd>
<dt>10000&#215;4096</dt>
<dd>824,461 (62.1%)</dd></dl>
</dl>
</dl>
<h2>Example</h2>
<pre><code>#
#Sample configuration file for xinetd
#
defaults{
    log_type = FILE / var / log / servicelog log_on_success = PID
                   log_on_failure = HOST
                       only_from = 128.138.193.0 128.138.204.0 only_from = 128.138.252.1 instances = 10 disabled = rstatd
}
#
#Note 1 : the protocol attribute is not required
#Note 2 : the instances attribute overrides the default
#
service login{
    socket_type = stream
        protocol = tcp
            wait = no
                user = root
                    server = / usr / etc / in.rlogind instances = UNLIMITED
}
#
#Note 1 : the instances attribute overrides the default
#Note 2 : the log_on_success flags are augmented
#
service shell{
    socket_type = stream
        wait = no
            user = root
                instances = UNLIMITED
                    server = / usr / etc / in.rshd log_on_success += HOST
}
service ftp{
    socket_type = stream
        wait = no
            nice = 10 user = root
                server = / usr / etc / in.ftpd server_args = -l
                                                                 instances = 4 log_on_success += DURATION HOST USERID
                             access_times = 2 : 00 - 9 : 00 12 : 00 - 24 : 00
}
#Limit telnet sessions to 8 Mbytes of memory and a total
# 20 CPU seconds for child processes.
service telnet{
    socket_type = stream
        wait = no
            nice = 10 user = root
                server = / usr / etc / in.telnetd rlimit_as = 8M rlimit_cpu = 20
}
#
#This entry and the next one specify internal services.Since
#this is the same service using a different socket type, the
#id attribute is used to uniquely identify each entry
#
service echo{
    id = echo - stream
                    type = INTERNAL
             socket_type = stream
                 user = root
                     wait = no
}
service echo{
    id = echo - dgram
                    type = INTERNAL
             socket_type = dgram
                 user = root
                     wait = no
}
#
#Sample RPC service
#
service rstatd{
    type = RPC
        socket_type = dgram
            protocol = udp
                server = / usr / etc / rpc.rstatd wait = yes
                             user = root
                                 rpc_version = 2 - 4 env = LD_LIBRARY_PATH = / etc / securelib
}
#
#Sample unlisted service
#
service unlisted
{
    type = UNLISTED
        socket_type = stream
            protocol = tcp
                wait = no
                    server = / home / user / some_server port = 20020
}</code></pre>
<h2>See Also</h2>
<p><i>xinetd(1L),</i> </p>
<p> <i><a href="/docs/linux/man/5-xinetd-log/">xinetd.log</a>(5)</i> </p>
<p> Postel J., <i>Echo Protocol</i>, RFC 862, May 1983 </p>
<p> Postel J., <i>Discard Protocol</i>, RFC 863, May 1983 </p>
<p> Postel J., <i>Character Generator Protocol</i>, RFC 864, May 1983 </p>
<p> Postel J., <i>Daytime Protocol</i>, RFC 867, May 1983 </p>
<p> Postel J., Harrenstien K., <i>Time Protocol</i>, RFC 868, May 1983 </p>
<p> M. Lottor, <i>TCP Port Service Multiplexer (TCPMUX)</i>, RFC 1078 Nov 1988 </p>
<p> StJohns M., <i> Identification Protocol</i>, RFC 1413, February 1993</p>
<h2>Bugs</h2>
<p>If the <code>INTERCEPT</code> flag is not used, access control on the address of the remote host is not performed when <i>wait</i> is <i>yes</i> and <i>socket_type</i> is <i>stream</i>. The NOLIBWRAP flag is automatically turned on for RPC services whose <i>socket_type</i> is <i>stream</i> because xinetd cannot determine the address of the remote host. If the <code>INTERCEPT</code> flag is not used, access control on the address of the remote host for services where <i>wait</i> is <i>yes</i> and <i>socket_type</i> is <i>dgram</i> is performed only on the first packet. The server may then accept packets from hosts not in the access control list. This can happen with <code>RPC</code> services. There is no way to put a SPACE in an environment variable. When <i>wait</i> is <i>yes</i> and <i>socket_type</i> is <i>stream</i>, the socket passed to the server can only accept connections. The <code>INTERCEPT</code> flag is not supported for internal services or multi-threaded services. </p>
</dl>