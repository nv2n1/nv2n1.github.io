---
title: "gmond(5)"
name: "gmond"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gmond/"
description: "gmond.conf – configuration file for ganglia monitoring daemon (gmond)"
---

<p><code>gmond.conf</code> &#8211; configuration file for ganglia monitoring daemon (gmond)</p>
<h2>Description</h2>
<p>The gmond.conf file is used to configure the ganglia monitoring daemon (gmond) which is part of the <code>Ganglia Distributed Monitoring System</code>.</p>
<h2>Sections And Attributes</h2>
<p>All sections and attributes are case-insensitive. For example, <code>name</code> or <font SIZE="-1"><code>NAME</code></font> or <code>Name</code> or <code>NaMe</code> are all equivalent. </p>
<p> Some sections can be included in the configuration file multiple times and some sections are singular. For example, you can have only one <code>cluster</code> section to define the attributes of the cluster being monitored; however, you can have multiple <code>udp_recv_channel</code> sections to allow gmond to receive message on multiple <font SIZE="-1">UDP</font> channels.</p>
<h2>cluster</h2>
<p>There should only be one <code>cluster</code> section defined. This section controls how gmond reports the attributes of the cluster that it is part of. </p>
<p> The <code>cluster</code> section has four attributes: <code>name</code>, <code>owner</code>, <code>latlong</code> and <code>url</code>. </p>
<p> For example, </p>
<pre> cluster {
 name = &quot;Millennium Cluster&quot;
 owner = &quot;UC Berkeley CS Dept.&quot;
 latlong = &quot;N37.37 W122.23&quot;
 url = &quot;<a rel="nofollow" href="http://www.millennium.berkeley.edu/">http://www.millennium.berkeley.edu/</a>&quot;
 }</pre>
<p>The <code>name</code> attributes specifies the name of the cluster of machines. The <code>owner</code> tag specifies the administrators of the cluster. The pair <code>name</code>/<code>owner</code> should be unique to all clusters in the world. </p>
<p> The <code>latlong</code> attribute is the latitude and longitude <font SIZE="-1">GPS</font> coordinates of this cluster on earth. Specified to 1 mile accuracy with two decimal places per axis in decimal. </p>
<p> The <code>url</code> for more information on the <code>cluster</code>. Intended to give purpose, owner, administration, and account details for this cluster. </p>
<p> There directives directly control the <font SIZE="-1">XML</font> output of gmond. For example, the cluster configuration example above would translate into the following <font SIZE="-1">XML</font>. </p>
<pre> &lt;CLUSTER NAME=&quot;Millennium Cluster&quot; OWNER=&quot;UC Berkeley CS Dept.&quot;
 LATLONG=&quot;N37.37 W122.23&quot; URL=&quot;<a rel="nofollow" href="http://www.millennium.berkeley.edu/">http://www.millennium.berkeley.edu/</a>&quot;&gt;
 ...
 &lt;/CLUSTER&gt;</pre>
<h2>host</h2>
<p>The <code>host</code> section provides information about the host running this instance of <code>gmond</code>. Currently only the <code>location</code> string attribute is supported. Example: </p>
<pre> host {
 location = &quot;1,2,3&quot;
 }</pre>
<p>The numbers represent Rack, Rank and Plane respectively.</p>
<h2>globals</h2>
<p>The <code>globals</code> section controls general characteristics of gmond such as whether is should daemonize, what user it should run as, whether is should send/receive date and such. The <code>globals</code> section has the following attributes: <code>daemonize</code>, <code>setuid</code>, <code>user</code>, <code>debug_level</code>, <code>mute</code>, <code>deaf</code>, <code>allow_extra_data</code>, <code>host_dmax</code>, <code>cleanup_threshold</code>, <code>gexec</code>, <code>send_metadata_interval</code> and <code>module_dir</code>. </p>
<p> For example, </p>
<pre> globals {
 daemonize = true
 setuid = true
 user = nobody
 host_dmax = 3600
 }</pre>
<p>The <code>daemonize</code> attribute is a boolean. When true, <code>gmond</code> will daemonize. When false, <code>gmond</code> will run in the foreground. </p>
<p> The <code>setuid</code> attribute is a boolean. When true, <code>gmond</code> will set its effective <font SIZE="-1">UID</font> to the uid of the user specified by the <code>user</code> attribute. When false, <code>gmond</code> will not change its effective user. </p>
<p> The <code>debug_level</code> is an integer value. When set to zero (0), <code>gmond</code> will run normally. A <code>debug_level</code> greater than zero will result in <code>gmond</code> running in the foreground and outputting debugging information. The higher the <code>debug_level</code> the more verbose the output. </p>
<p> The <code>mute</code> attribute is a boolean. When true, <code>gmond</code> will not send data regardless of any other configuration directives. </p>
<p> The <code>deaf</code> attribute is a boolean. When true, <code>gmond</code> will not receive data regardless of any other configuration directives. </p>
<p> The <code>allow_extra_data</code> attribute is a boolean. When false, <code>gmond</code> will not send out the <font SIZE="-1">EXTRA_ELEMENT</font> and <font SIZE="-1">EXTRA_DATA</font> parts of the <font SIZE="-1">XML</font>. This might be useful if you are using your own frontend to the metric data and will like to save some bandwith. </p>
<p> The <code>host_dmax</code> value is an integer with units in seconds. When set to zero (0), <code>gmond</code> will never delete a host from its list even when a remote host has stopped reporting. If <code>host_dmax</code> is set to a positive number then <code>gmond</code> will flush a host after it has not heard from it for <code>host_dmax</code> seconds. By the way, dmax means &#8220;delete max&#8221;. </p>
<p> The <code>cleanup_threshold</code> is the minimum amount of time before gmond will cleanup any hosts or metrics where <code>tn</code> &gt; <code>dmax</code> a.k.a. expired data. </p>
<p> The <code>gexec</code> boolean allows you to specify whether gmond will announce the hosts availability to run gexec jobs. <code>Note</code>: this requires that <code>gexecd</code> is running on the host and the proper keys have been installed. </p>
<p> The <code>send_metadata_interval</code> establishes an interval in which gmond will send or resend the metadata packets that describe each enabled metric. This directive by default is set to 0 which means that gmond will only send the metadata packets at startup and upon request from other gmond nodes running remotely. If a new machine running gmond is added to a cluster, it needs to announce itself and inform all other nodes of the metrics that it currently supports. In multicast mode, this isn&#8217;t a problem because any node can request the metadata of all other nodes in the cluster. However in unicast mode, a resend interval must be established. The interval value is the minimum number of seconds between resends. </p>
<p> The <code>module_dir</code> is an optional parameter indicating the directory where the <font SIZE="-1">DSO</font> modules are to be located. If absent, the value to use is set at configure time with the &#8211;with-moduledir option which will default if omitted to the a subdirectory named &#8220;ganglia&#8221; in the directory where libganglia will be installed. </p>
<p> For example, in a 32-bit Intel compatible Linux host that is usually: </p>
<pre> /usr/lib/ganglia</pre>
<h2>udp_send_channel</h2>
<p>You can define as many <code>udp_send_channel</code> sections as you like within the limitations of memory and file descriptors. If <code>gmond</code> is configured as <code>mute</code> this section will be ignored. </p>
<p> The <code>udp_send_channel</code> has a total of five attributes: <code>mcast_join</code>, <code>mcast_if</code>, <code>host</code>, <code>port</code> and <code>ttl</code>. </p>
<p> For example, the 2.5.x version gmond would send on the following single channel by default&#8230; </p>
<pre> udp_send_channel {
 mcast_join = 239.2.11.71
 port = 8649
 }</pre>
<p>The <code>mcast_join</code> and <code>mcast_if</code> attributes are optional. When specified <code>gmond</code> will create the <font SIZE="-1">UDP</font> socket and join the <code>mcast_join</code> multicast group and send data out the interface specified by <code>mcast_if</code>. </p>
<p> If only a <code>host</code> and <code>port</code> are specified then <code>gmond</code> will send unicast <font SIZE="-1">UDP</font> messages to the hosts specified. You could specify multiple unicast hosts for redundancy as <code>gmond</code> will send <font SIZE="-1">UDP</font> messages to all <font SIZE="-1">UDP</font> channels. </p>
<p> For example&#8230; </p>
<pre> udp_send_channel {
 host = host.foo.com
 port = 2389
 }
 udp_send_channel {
 host = 192.168.3.4
 port = 2344
 }</pre>
<p>would configure gmond to send messages to two hosts. The <code>host</code> specification can be an IPv4/IPv6 address or a resolvable hostname.</p>
<h2>udp_recv_channel</h2>
<p>You can specify as many <code>udp_recv_channel</code> sections as you like within the limits of memory and file descriptors. If <code>gmond</code> is configured <code>deaf</code> this attribute will be ignored. </p>
<p> The <code>udp_recv_channel</code> section has following attributes: <code>mcast_join</code>, <code>bind</code>, <code>port</code>, <code>mcast_if</code>, <code>family</code>. The <code>udp_recv_channel</code> can also have an <code>acl</code> definition (see <font SIZE="-1">ACCESS</font> <font SIZE="-1">CONTROL</font> <font SIZE="-1">LISTS</font> below). </p>
<p> For example, the 2.5.x gmond ran with a single udp receive channel&#8230; </p>
<pre> udp_recv_channel {
 mcast_join = 239.2.11.71
 bind = 239.2.11.71
 port = 8649
 }</pre>
<p>The <code>mcast_join</code> and <code>mcast_if</code> should only be used if you want to have this <font SIZE="-1">UDP</font> channel receive multicast packets the multicast group <code>mcast_join</code> on interface <code>mcast_if</code>. If you do not specify multicast attributes then <code>gmond</code> will simply create a <font SIZE="-1">UDP</font> server on the specified <code>port</code>. </p>
<p> You can use the <code>bind</code> attribute to bind to a particular local address. </p>
<p> The family address is set to <code>inet4</code> by default. If you want to bind the port to an <code>inet6</code> port, you need to specify that in the family attribute. Ganglia will not allow IPV6=&gt;<font SIZE="-1">IPV4</font> mapping (for portability and security reasons). If you want to listen on both <code>inet4</code> and <code>inet6</code> for a particular port, explicitly state it with the following: </p>
<pre> udp_recv_channel {
 port = 8666
 family = inet4
 }
 udp_recv_channel {
 port = 8666
 family = inet6
 }</pre>
<p>If you specify a bind address, the family of that address takes precedence. f your IPv6 stack doesn&#8217;t support <font SIZE="-1">IPV6_V6ONLY</font>, a warning will be issued but gmond will continue working (this should rarely happen). </p>
<p> Multicast Note: for multicast, specifying a <code>bind</code> address with the same value used for <code>mcast_join</code> will prevent unicast <font SIZE="-1">UDP</font> messages to the same <code>port</code> from being processed.</p>
<h2>tcp_accept_channel</h2>
<p>You can specify as many <code>tcp_accept_channel</code> sections as you like within the limitations of memory and file descriptors. If <code>gmond</code> is configured to be <code>mute</code>, then these sections are ignored. </p>
<p> The <code>tcp_accept_channel</code> has the following attributes: <code>bind</code>, <code>port</code>, <code>interface</code>, <code>family</code> and <code>timeout</code>. A <code>tcp_accept_channel</code> may also have an <code>acl</code> section specified (see <font SIZE="-1">ACCESS</font> <font SIZE="-1">CONTROL</font> <font SIZE="-1">LISTS</font> below). </p>
<p> For example, 2.5.x gmond would accept connections on a single <font SIZE="-1">TCP</font> channel. </p>
<pre> tcp_accept_channel {
 port = 8649
 }</pre>
<p>The <code>bind</code> address is optional and allows you to specify which local address <code>gmond</code> will bind to for this channel. </p>
<p> The <code>port</code> is an integer than specifies which port to answer requests for data. </p>
<p> The <code>family</code> address is set to <code>inet4</code> by default. If you want to bind the port to an <code>inet6</code> port, you need to specify that in the family attribute. Ganglia will not allow IPV6=&gt;<font SIZE="-1">IPV4</font> mapping (for portability and security reasons). If you want to listen on both <code>inet4</code> and <code>inet6</code> for a particular port, explicitly state it with the following: </p>
<pre> tcp_accept_channel {
 port = 8666
 family = inet4
 }
 tcp_accept_channel {
 port = 8666
 family = inet6
 }</pre>
<p>If you specify a bind address, the family of that address takes precedence. If your IPv6 stack doesn&#8217;t support <font SIZE="-1">IPV6_V6ONLY</font>, a warning will be issued but gmond will continue working (this should rarely happen). </p>
<p> The <code>timeout</code> attribute allows you to specify how many microseconds to block before closing a connection to a client. The default is set to 1 second (1000000 usecs). If you have a very slow connection you may need to increase this value. </p>
<p> The <code>interface</code> is not implemented at this time (use <code>bind</code>).</p>
<h2>collection_group</h2>
<p>You can specify as many <code>collection_group</code> section as you like within the limitations of memory. A <code>collection_group</code> has the following attributes: <code>collect_once</code>, <code>collect_every</code> and <code>time_threshold</code>. A <code>collection_group</code> must also contain one or more <code>metric</code> sections. </p>
<p> The <code>metric</code> section has the following attributes: <code>name</code>, <code>value_threshold</code> and <code>title</code>. For a list of available metric names, run the following command: </p>
<pre> % gmond -m</pre>
<p>Here is an example of a collection group for a static metric&#8230; </p>
<pre> collection_group {
 collect_once = yes
 time_threshold = 1800
 metric {
 name = &quot;cpu_num&quot;
 title = &quot;Number of CPUs&quot;
 }
 }</pre>
<p>This <code>collection_group</code> entry would cause gmond to collect the <code>cpu_num</code> metric once at startup (since the number of CPUs will not change between reboots). The metric <code>cpu_num</code> would be send every 1/2 hour (1800 seconds). The default value for the <code>time_threshold</code> is 3600 seconds if no <code>time_threshold</code> is specified. </p>
<p> The <code>time_threshold</code> is the maximum amount of time that can pass before gmond sends all <code>metric</code>s specified in the <code>collection_group</code> to all configured <code>udp_send_channel</code>s. A <code>metric</code> may be sent before this <code>time_threshold</code> is met if during collection the value surpasses the <code>value_threshold</code> (explained below). </p>
<p> Here is an example of a collection group for a volatile metric&#8230; </p>
<pre> collection_group {
 collect_every = 60
 time_threshold = 300
 metric {
 name = &quot;cpu_user&quot;
 value_threshold = 5.0
 title = &quot;CPU User&quot;
 }
 metric {
 name = &quot;cpu_idle&quot;
 value_threshold = 10.0
 title = &quot;CPU Idle&quot;
 }
 }</pre>
<p>This collection group would collect the <code>cpu_user</code> and <code>cpu_idle</code> metrics every 60 seconds (specified in <code>collect_every</code>). If <code>cpu_user</code> varies by 5.0% or <code>cpu_idle</code> varies by 10.0%, then the entire <code>collection_group</code> is sent. If no <code>value_threshold</code> is triggered within <code>time_threshold</code> seconds (in this case 300), the entire <code>collection_group</code> is sent. </p>
<p> Each time the metric value is collected the new value is compared with the old value collected. If the difference between the last value and the current value is greater than the <code>value_threshold</code>, the entire collection group is send to the <code>udp_send_channel</code>s defined. </p>
<p> It&#8217;s important to note that all metrics in a collection group are sent even when only a single <code>value_threshold</code> is surpassed. </p>
<p> In addition a user friendly title can be substituted for the metric name by including a <code>title</code> within the <code>metric</code> section.</p>
<h2>Modules</h2>
<p>A <code>modules</code> section contains the parameters that are necessary to load a metric module. A metric module is a dynamically loadable module that extends the available metrics that gmond is able to collect. Each <code>modules</code> section contains at least one <code>module</code> section. Within a <code>module</code> section are the directives <code>name</code>, <code>language</code>, <code>enabled</code>, <code>path</code> and <code>params</code>. The module <code>name</code> is the name of the module as determined by the module structure if the module was developed in C/C<font SIZE="-2">++</font>. Alternatively, the <code>name</code> can be the name of the source file if the module has been implemented in a interpreted language such as python. A <code>language</code> designation must be specified as a string value for each module. The <code>language</code> directive must correspond to the source code language in which the module was implemented (ex. language = &#8220;python&#8221;). If a <code>language</code> directive does not exist for the module, the assumed language will be &#8220;C/C<font SIZE="-2">++</font>&#8221;. The <code>enabled</code> directive allows a metric module to be easily enabled or disabled through the configuration file. If the <code>enabled</code> directive is not included in the module configuration, the enabled state will default to &#8220;yes&#8221;. One thing to note is that if a module has been disabled yet the metric which that module implements is still listed as part of a collection group, gmond will produce a warning message. However gmond will continue to function normally by simply ignoring the metric. The <code>path</code> is the path from which gmond is expected to load the module (C/C<font SIZE="-2">++</font> compiled dynamically loadable module only). The <code>params</code> directive can be used to pass a single string parameter directly to the module initialization function (C/C<font SIZE="-2">++</font> module only). Multiple parameters can be passed to the module&#8217;s initialization function by including one or more <code>param</code> sections. Each <code>param</code> section must be named and contain a <code>value</code> directive. Once a module has been loaded, the additional metrics can be discovered by invoking <code>gmond -m</code>. </p>
<pre> modules {
 module {
 name = &quot;example_module&quot;
 enabled = yes
 path = &quot;modexample.so&quot;
 params = &quot;An extra raw parameter&quot;
 param RandomMax {
 value = 75
 }
 param ConstantValue {
 value = 25
 }
 }
 }</pre>
<h2>Include</h2>
<p>This directive allows the user to include additional configuration files rather than having to add all gmond configuration directives to the gmond.conf file. The following example includes any file with the extension of .conf contained in the directory conf.d as if the contents of the included configuration files were part of the original gmond.conf file. This allows the user to modularize their configuration file. One usage example might be to load individual metric modules by including module specific .conf files. </p>
<p> include (&#8216;/etc/ganglia/conf.d/*.conf&#8217;)</p>
<h2>Access Control</h2>
<p>The <code>udp_recv_channel</code> and <code>tcp_accept_channel</code> directives can contain an Access Control List (<font SIZE="-1">ACL</font>). This <font SIZE="-1">ACL</font> allows you to specify exactly which hosts gmond process data from. </p>
<p> An example of an <code>acl</code> entry looks like </p>
<pre> acl {
 default = &quot;deny&quot;
 access {
 ip = 192.168.0.4
 mask = 32
 action = &quot;allow&quot;
 }
 }</pre>
<p>This <font SIZE="-1">ACL</font> will by default reject all traffic that is not specifically from host 192.168.0.4 (the mask size for an IPv4 address is 32, the mask size for an IPv6 address is 128 to represent a single host). </p>
<p> Here is another example </p>
<pre> acl {
 default = &quot;allow&quot;
 access {
 ip = 192.168.0.0
 mask = 24
 action = &quot;deny&quot;
 }
 access {
 ip = ::ff:1.2.3.0
 mask = 120
 action = &quot;deny&quot;
 }
 }</pre>
<p>This <font SIZE="-1">ACL</font> will by default allow all traffic unless it comes from the two subnets specified with action = &#8220;deny&#8221;.</p>
<h2>Example</h2>
<p>The default behavior for a 2.5.x gmond would be specified as&#8230; </p>
<pre><code>udp_recv_channel {
    mcast_join = 239.2.11.71
    bind       = 239.2.11.71
    port       = 8649
}
udp_send_channel {
    mcast_join = 239.2.11.71
    port       = 8649
}
tcp_accept_channel {
    port       = 8649
}</code></pre>
<p> To see the complete default configuration for gmond simply run: </p>
<pre> % gmond -t</pre>
<p>gmond will print out its default behavior in a configuration file and then exit. Capturing this output to a file can serve as a useful starting point for creating your own custom configuration. </p>
<pre> % gmond -t &gt; custom.conf</pre>
<p>edit <code>custom.conf</code> to taste and then </p>
<pre> % gmond -c ./custom.conf</pre>
<h2>Notes</h2>
<p>The ganglia web site is at <a rel="nofollow" href="http://ganglia.info/.">http://ganglia.info/.</a></p>
<h2>Copyright</h2>
<p>Copyright (c) 2005 The University of California, Berkeley</p>
