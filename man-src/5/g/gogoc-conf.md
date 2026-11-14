---
title: "gogoc-conf(5)"
name: "gogoc-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gogoc-conf/"
description: "gogoc.conf – gogoCLIENT Configuration File"
---

<p><code>gogoc.conf</code> &#8211; gogoCLIENT Configuration File</p>
<h2>Synopsis</h2>
<p>The gogoCLIENT <a href="/docs/linux/man/8-gogoc/">gogoc</a>(8) is a client program which enables a host to query a tunnel server to establish a tunnel between the host and the server using the TSP protocol. The gogoc configuration file contains information that is read by <a href="/docs/linux/man/8-gogoc/">gogoc</a>(8) for specific details regarding the server and the tunnel to be established. </p>
<h2>File Format</h2>
<p>This file is designed to be human readable and may be edited with any text editor. The file consists of tokens and values, which are separated by the equal sign. Each &quot;Token=Value&quot; pair must be on their own line. </p>
<p> The different configuration directives(or options) are grouped in the following sections:</p>
<h2>Basic Configuration</h2>
<dl>
<dt><code>userid</code></p>
<dd>The userid is used for authentication with the server. The TSP protocol supports both anonymous and authenticated tunnels. Refer to the server policies for supported modes and related Services, as well as for how to register your user name. The syntax to use is given below: </p>
<p> userid=user_name </p>
<p> This variable is MANDATORY if you are using an authenticated tunnel. Leave empty if you are using anonymous access.</p>
<dt><code>passwd</code></p>
<dd>passwd=your_password </p>
<p> Leave empty if you are using anonymous access.</p>
<dt><code>server</code></p>
<dd>Name and port number of the tunnel server. This variable is used to specify the gogoSERVER to be queried. An IPv4 or IPv6 address or FQDN (Fully Qualified Domain Name) can be used. The port number is optional. The default TSP port is 3653. </p>
<p> server=host[:port] </p>
<p> server=broker.freenet6.net </p>
<p> server=192.168.1.1:3653 </p>
<p> This variable is MANDATORY.</p>
<dt><code>auth_method</code></p>
<dd>The tunnel negotiation authentication method. If you are using anonymous access, enter `anonymous&#8217; here. Otherwise, choose one of the following authentication methods: any|digest-md5|passdss-3des-1|plain </p>
<p> anonymous sends no username or password. </p>
<p> any is the preferred one. The most secure mechanism common to the client and the broker will be used. </p>
<p> digest-md5 sends the username in clear text, but not the password. </p>
<p> passdss-3des-1 sends the username in clear text, but not the password. </p>
<p> plain sends both username and password in clear text. </p>
<p> Default: any</dl>
<h2>Router Configuration</h2>
<dl>
<dt><code>host_type</code></p>
<dd>Set the value of this directive to `router&#8217; to configure the machine as a router. By doing so, you will be given a prefix to advertise on a local interface. </p>
<p> host_type=host|router </p>
<p> Default: host </p>
<dt><code>prefixlen</code></p>
<dd>prefixlen specifies the required prefix length for the gogoCLIENT network. Valid values range from 0 to 64; however, values are usually between 48 and 64. </p>
<p> Default: 64 </p>
<dt><code>if_prefix</code></p>
<dd>if_prefix is the name of the OS interface that will be configured with the first /64 of the received prefix from the broker. The router advertisement daemon is started to advertise this prefix on the if_prefix interface. </p>
<dt><code>dns_server</code></p>
<dd>This directive specifies the DNS servers that should be used for reverse DNS delegation of the prefix allocated. </p>
<p> Syntax is: </p>
<p> dns_server=fqdn[:fqdn]&#8230; </p>
<p> For example, to set ns1.example.net and ns2.example.net as authoritative DNS servers for reverse DNS of the prefix, this line would be used in gogoc.conf: </p>
<p> dns_server=ns1.example.net:ns2.example.net </p>
<p> NOTE: Never use an IP address as a DNS server name.</dl>
<h2>Advanced Configuration</h2>
<dl>
<dt><code>tunnel_mode</code></p>
<dd>The tunnel encapsulation mode. It can take the following values: </p>
<p> v6anyv4 This mode lets the broker determine whether or not the gogoCLIENT is behind a NAT. The broker will then inform the gogoCLIENT which tunnel mode to use: v6v4 or v6udpv4. </p>
<p> v6v4 Explicitly requests an IPv6-in-IPv4 tunnel. </p>
<p> v6udpv4 Explicitly requests an IPv6-in-UDP-IPv4 tunnel (for clients behind a NAT). This type of tunnel is supported under Linux, FreeBSD and Windows. </p>
<p> v4v6 Explicitly requests an IPv4-in-IPv6 tunnel (for dual-stack transition mechanism). </p>
<p> Default: v6anyv4</p>
<dt><code>auto_retry_connect</code></p>
<dd>This directive is used when a keepalive timeout or similar error occurred, resulting in a loss of connectivity with the tunnel endpoint. If you wish the gogoCLIENT to re-establish connectivity with tunnel endpoint when such an error occurs, set this variable to `yes&#8217;. </p>
<p> auto_retry_connect=yes|no </p>
<p> Default: yes</p>
<dt><code>retry_delay</code></p>
<dd>The retry_delay directive is used to set the number of seconds to sleep before reattempting to establish a tunnel with the gogoSERVER. It will retry until it succeeds, unless you have set the auto_retry_connect variable to `no&#8217;. </p>
<p> Default: 30 </p>
<dt><code>keepalive </code></p>
<dd>keepalive indicates that this client will send keepalive packets to maintain tunnel activity and detect inactive tunnels (if no response is received from the server). This directive must be set to `yes&#8217; when using v6udpv4 tunnels to keep the NAT entry active. </p>
<p> keepalive=yes|no </p>
<p> Default: yes </p>
<dt><code>keepalive_interval</code></p>
<dd>The keepalive_interval is a suggestion from the gogoCLIENT to the broker for the interval to wait between sending keepalive messages. The broker may impose a different interval value to the client if the suggested value is too low. </p>
<p> keepalive_interval=30 </p>
<p> Default: 30 </p>
<dt><code>if_tunnel_v6v4</code></p>
<dd>The logical interface name that will be used for the configured tunnel (IPv6 over IPv4). The syntax is: </p>
<p> if_tunnel_v6v4=name </p>
<p> Under *BSD: gif0 </p>
<p> Under Linux: sit0 </p>
<p> Under Windows: 2 </p>
<p> This variable is MANDATORY.</p>
<dt><code>if_tunnel_v6udpv4</code></p>
<dd>The logical interface name that will be used for v6udpv4 tunnels (IPv6 over UDPv4). The syntax is: </p>
<p> if_tunnel_v6udpv4=name </p>
<p> Under FreeBSD: tun1 </p>
<p> Under Linux: tun </p>
<p> Under Windows: tunv6 </p>
<dt><code>if_tunnel_v4v6</code></p>
<dd>The logical interface name that will be used for v4v6 tunnels (IPv4 over IPv6). The syntax is: </p>
<p> if_tunnel_v4v6=name</p>
<dt><code>gogoc_dir</code></p>
<dd>The directory where the gogoCLIENT program is installed. Binaries, manual pages, this configuration file and templates are all located in this directory. This variable may resemble the following: </p>
<p> gogoc_dir=/usr/local/gogoc </p>
<p> This variable is MANDATORY.</p>
<dt><code>template</code></p>
<dd>This directive indicates which configuration template must be used when configuring the tunnel. The configuration template is a script file, located in the template directory of the package, that contains the system commands to be executed for tunnel setup. The directives are passed to the script file as environment variables. The template directive is normally set when the package is built for the specific operating system. View the contents of the template directory to learn which ones are available. The template name must be the file name without the .sh or .cmd suffix. </p>
<p> template=linux </p>
<p> This variable is MANDATORY.</p>
<dt><code>proxy_client</code></p>
<dd>The proxy_client directive indicates that this client acts as a TSP proxy for a remote client tunnel endpoint machine. It is set to `yes&#8217; if the machine running the gogoCLIENT requests a tunnel for another machine. (e.g.: cisco template). This directive must be used in conjunction with a static IPv4 address assigned to the client_v4 variable. </p>
<p> NOTE: proxy_client=yes is incompatible with tunnel_mode=v6udpv4 </p>
<p> Default: no</p>
<dt><code>client_v4</code></p>
<dd>The IPv4 address of the client tunnel endpoint. If the host has more than one IPv4 address, it is recommended to manually set this variable with its local IPv4 address as the value. If set to auto, it chooses the source IP address used when communicating with the server. This variable may resemble the following: </p>
<p> client_v4=auto|a.b.c.d </p>
<p> Default: auto</p>
<dt><code>client_v6</code></p>
<dd>This directive is similar te client_v4, except that this one is for users that have enabled IPv4 in IPv6 encapsulation (i.e., DSTM). </p>
<p> client_v6=auto|XX:XX::XX:XX </p>
<p> Default: auto</p>
<dt><code>broker_list</code></p>
<dd>The &#8216;broker_list&#8217; directive specifies the name of the file where the broker list received during broker redirection will be saved. </p>
<p> Default: tsp-broker-list.txt</p>
<dt><code>last_server</code></p>
<dd>The &#8216;last_server&#8217; directive specifies the name of the file where the address of the last broker to which a connection was successfully established will be saved. </p>
<p> Default: tsp-last-server.txt</p>
<dt><code>always_use_same_server</code></p>
<dd>The value of the &#8216;always_use_same_server&#8217; directive determines whether the client should always try to connect to the broker specified by the &#8216;last_server&#8217; directive (if any). </p>
<p> Default: no</dl>
<h2>Logging Configuration</h2>
<dl>
<dt><code>log_file</code></p>
<dd>This directive is used to specify the quantity of information that will be logged to the file. Values range inclusively from 0 (no logging) to 3 (full logging). </p>
<p> Default: 0</p>
<dt><code>log_stderr</code></p>
<dd>This directive is used to specify the quantity of information that will be logged to the standard error device. Values range inclusively from 0 (no logging) to 3 (full logging). </p>
<p> Default: 1</p>
<dt><code>log_console</code></p>
<dd>This directive is used to specify the quantity of information that will be logged to the console. Values range inclusively from 0 (no logging) to 3 (full logging). </p>
<p> Default: 0</p>
<dt><code>log_syslog</code></p>
<dd>This directive is used to specify the quantity of information that will be logged to the syslog. Values range inclusively from 0 (no logging) to 3 (full logging). </p>
<p> Default: 0</p>
<dt><code>log_filename</code></p>
<dd>When logging to file is requested via the &#8216;log_file&#8217; directive, the name and path of the file to use may be specified using the &#8216;log_filename&#8217; directive. </p>
<p> log_filename=[/path/to/the/]file </p>
<p> Default: gogoc.log </p>
<dt><code>log_rotation</code></p>
<dd>When logging to file is requested via the &#8216;log_file&#8217; directive, log file rotation may be enabled using the &#8216;log_rotation&#8217; directive. </p>
<p> When enabled, the contents of the log file will be moved to a backup file just before it reaches the maximum log file size specified via the<br />
&nbsp;<wbr>`log_rotation_size&#8217;&nbsp;<wbr>directive. </p>
<p> The name of the backup file is the name of the original log file with `.&lt;timestamp&gt;&#8217; inserted before the file extension. If the file does not have an extension, `.&lt;timestamp&gt;&#8217; is appended to the name of the original log file. The timestamp specifies when the rotation occurred. </p>
<p> After the contents of the log file have been moved to the backup file, the original file is cleared, and logging resumes at the beginning of the file. </p>
<p> log_rotation=yes|no </p>
<p> Default: yes </p>
<dt><code>log_rotation_size</code></p>
<dd>The `log_rotation_size&#8217; directive specifies the maximum size a log file may reach before rotation occurs (if rotation has been enabled via the `log_rotation&#8217; directive). </p>
<p> The value is expressed in kilobytes. </p>
<p> log_rotation_size=16|32|128|1024 </p>
<p> Default value: 32 </p>
<dt><code>log_rotation_delete</code></p>
<dd>The `log_rotation_delete&#8217; directive specifies that the log file will be recycled on rotation. No backup log files will be kept. (if rotation has been enabled via the &#8216;log_rotation&#8217; directive). </p>
<p> log_rotation_delete=yes|no </p>
<p> Default: no </p>
<dt><code>syslog_facility</code></p>
<dd>When logging to syslog is requested using the `log&#8217; directive, the facility to use may be specified using the `syslog_facility&#8217; directive. </p>
<p> Valid values are USER, and LOCAL[0-7]. </p>
<p> syslog_facility=FACILITY </p>
<p> Default: USER </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>&lt;gogoc_dir&gt;/bin/gogoc.conf </code></p>
<dd>
<dt><code>&lt;gogoc_dir&gt;/bin/gogoc.conf.sample </code></p>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-gogoc/">gogoc</a>(8)</p>
<dl>
<dd>Freenet6 Web site: <a rel="nofollow" href="http://www.go6.net">http://www.go6.net</a> gogo6 Web site: <a rel="nofollow" href="http://www.gogo6.com">http://www.gogo6.com</a></dl>
