---
title: "busctl(1)"
name: "busctl"
section: "1"
letter: "b"
url: "/docs/linux/man/1-busctl/"
description: "busctl – Introspect the bus"
---

<h2 class="name">NAME</h2>
<p> busctl &#8211; Introspect the bus </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>busctl</code> [OPTIONS&#8230;] [COMMAND] [<i>NAME</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>busctl</code></p>
<dd>may be used to introspect and monitor the D-Bus bus.</p>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>list</code></p>
<dl>
<dt>
<dd> Show all peers on the bus, by their service names. By default, shows both unique and well-known names, but this may be changed with the <code>&#8211;unique</code> and <code>&#8211;acquired</code> switches. This is the default operation if no command is specified.</dl>
<p> <code>status</code> [<i>SERVICE</i>]</p>
<dl>
<dt>
<dd> Show process information and credentials of a bus service (if one is specified by its unique or well-known name), a process (if one is specified by its numeric PID), or the owner of the bus (if no parameter is specified).</dl>
<p> <code>monitor</code> [<i>SERVICE</i>&#8230;]</p>
<dl>
<dt>
<dd> Dump messages being exchanged. If <i>SERVICE</i> is specified, show messages to or from this peer, identified by its well-known or unique name. Otherwise, show all messages on the bus. Use Ctrl+C to terminate the dump.</dl>
<p> <code>capture</code> [<i>SERVICE</i>&#8230;]</p>
<dl>
<dt>
<dd> Similar to <code>monitor</code> but writes the output in pcap format (for details, see the m[blue]<code>Libpcap File Format</code>m[]<font SIZE="-2">[1]</font> description). Make sure to redirect standard output to a file. Tools like <code><a href="/docs/linux/man/1-wireshark/">wireshark</a></code>(1) may be used to dissect and view the resulting files.</dl>
<p> <code>tree</code> [<i>SERVICE</i>&#8230;]</p>
<dl>
<dt>
<dd> Shows an object tree of one or more services. If <i>SERVICE</i> is specified, show object tree of the specified services only. Otherwise, show all object trees of all services on the bus that acquired at least one well-known name.</dl>
<p> <code>introspect</code> <i>SERVICE</i> <i>OBJECT</i> [<i>INTERFACE</i>]</p>
<dl>
<dt>
<dd> Show interfaces, methods, properties and signals of the specified object (identified by its path) on the specified service. If the interface argument is passed, the output is limited to members of the specified interface.</dl>
<p> <code>call</code> <i>SERVICE</i> <i>OBJECT</i> <i>INTERFACE</i> <i>METHOD</i> [<i>SIGNATURE</i>&nbsp;[<i>ARGUMENT</i>&#8230;]]</p>
<dl>
<dt>
<dd> Invoke a method and show the response. Takes a service name, object path, interface name and method name. If parameters shall be passed to the method call, a signature string is required, followed by the arguments, individually formatted as strings. For details on the formatting used, see below. To suppress output of the returned data, use the <code>&#8211;quiet</code> option.</dl>
<p> <code>emit</code> <i>OBJECT</i> <i>INTERFACE</i> <i>SIGNAL</i> [<i>SIGNATURE</i>&nbsp;[<i>ARGUMENT</i>&#8230;]]</p>
<dl>
<dt>
<dd> Emit a signal. Takes an object path, interface name and method name. If parameters shall be passed, a signature string is required, followed by the arguments, individually formatted as strings. For details on the formatting used, see below. To specify the destination of the signal, use the <code>&#8211;destination=</code> option.</dl>
<p> <code>get-property</code> <i>SERVICE</i> <i>OBJECT</i> <i>INTERFACE</i> <i>PROPERTY</i>&#8230;</p>
<dl>
<dt>
<dd> Retrieve the current value of one or more object properties. Takes a service name, object path, interface name and property name. Multiple properties may be specified at once, in which case their values will be shown one after the other, separated by newlines. The output is, by default, in terse format. Use <code>&#8211;verbose</code> for a more elaborate output format.</dl>
<p> <code>set-property</code> <i>SERVICE</i> <i>OBJECT</i> <i>INTERFACE</i> <i>PROPERTY</i> <i>SIGNATURE</i> <i>ARGUMENT</i>&#8230;</p>
<dl>
<dt>
<dd> Set the current value of an object property. Takes a service name, object path, interface name, property name, property signature, followed by a list of parameters formatted as strings.</dl>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Show command syntax help.</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;address=</code><i>ADDRESS</i></p>
<dl>
<dt>
<dd> Connect to the bus specified by <i>ADDRESS</i> instead of using suitable defaults for either the system or user bus (see <code>&#8211;system</code> and <code>&#8211;user</code> options).</dl>
<p> <code>&#8211;show-machine</code></p>
<dl>
<dt>
<dd> When showing the list of peers, show a column containing the names of containers they belong to. See <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8).</dl>
<p> <code>&#8211;unique</code></p>
<dl>
<dt>
<dd> When showing the list of peers, show only &quot;unique&quot; names (of the form &quot;:<i>number</i>.<i>number</i>&quot;).</dl>
<p> <code>&#8211;acquired</code></p>
<dl>
<dt>
<dd> The opposite of <code>&#8211;unique</code> &#8212; only &quot;well-known&quot; names will be shown.</dl>
<p> <code>&#8211;activatable</code></p>
<dl>
<dt>
<dd> When showing the list of peers, show only peers which have actually not been activated yet, but may be started automatically if accessed.</dl>
<p> <code>&#8211;match=</code><i>MATCH</i></p>
<dl>
<dt>
<dd> When showing messages being exchanged, show only the subset matching <i>MATCH</i>. See <code><a href="/docs/linux/man/3-sd_bus_add_match/">sd_bus_add_match</a></code>(3).</dl>
<p> <code>&#8211;size=</code></p>
<dl>
<dt>
<dd> When used with the <code>capture</code> command, specifies the maximum bus message size to capture (&quot;snaplen&quot;). Defaults to 4096 bytes.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> When used with the <code>tree</code> command, shows a flat list of object paths instead of a tree.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> When used with the <code>call</code> command, suppresses display of the response message payload. Note that even if this option is specified, errors returned will still be printed and the tool will indicate success or failure with the process exit code.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> When used with the <code>call</code> or <code>get-property</code> command, shows output in a more verbose format.</dl>
<p> <code>&#8211;xml-interface</code></p>
<dl>
<dt>
<dd> When used with the <code>introspect</code> call, dump the XML description received from the D-Bus <code>org.freedesktop.DBus.Introspectable.Introspect</code> call instead of the normal output.</dl>
<p> <code>&#8211;json=</code><i>MODE</i></p>
<dl>
<dt>
<dd> When used with the <code>call</code> or <code>get-property</code> command, shows output formatted as JSON. Expects one of &quot;short&quot; (for the shortest possible output without any redundant whitespace or line breaks) or &quot;pretty&quot; (for a pretty version of the same, with indentation and line breaks). Note that transformation from D-Bus marshalling to JSON is done in a loss-less way, which means type information is embedded into the JSON object tree.</dl>
<p> <code>-j</code></p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;json=pretty</code> when invoked interactively from a terminal. Otherwise equivalent to <code>&#8211;json=short</code>, in particular when the output is piped to some other program.</dl>
<p> <code>&#8211;expect-reply=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> When used with the <code>call</code> command, specifies whether <code>busctl</code> shall wait for completion of the method call, output the returned method response data, and return success or failure via the process exit code. If this is set to &quot;no&quot;, the method call will be issued but no response is expected, the tool terminates immediately, and thus no response can be shown, and no success or failure is returned via the exit code. To only suppress output of the reply message payload, use <code>&#8211;quiet</code> above. Defaults to &quot;yes&quot;.</dl>
<p> <code>&#8211;auto-start=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> When used with the <code>call</code> or <code>emit</code> command, specifies whether the method call should implicitly activate the called service, should it not be running yet but is configured to be auto-started. Defaults to &quot;yes&quot;.</dl>
<p> <code>&#8211;allow-interactive-authorization=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> When used with the <code>call</code> command, specifies whether the services may enforce interactive authorization while executing the operation, if the security policy is configured for this. Defaults to &quot;yes&quot;.</dl>
<p> <code>&#8211;timeout=</code><i>SECS</i></p>
<dl>
<dt>
<dd> When used with the <code>call</code> command, specifies the maximum time to wait for method call completion. If no time unit is specified, assumes seconds. The usual other units are understood, too (ms, us, s, min, h, d, w, month, y). Note that this timeout does not apply if <code>&#8211;expect-reply=no</code> is used, as the tool does not wait for any reply message then. When not specified or when set to 0, the default of &quot;25s&quot; is assumed.</dl>
<p> <code>&#8211;augment-creds=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Controls whether credential data reported by <code>list</code> or <code>status</code> shall be augmented with data from /proc/. When this is turned on, the data shown is possibly inconsistent, as the data read from /proc/ might be more recent than the rest of the credential information. Defaults to &quot;yes&quot;.</dl>
<p> <code>&#8211;watch-bind=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Controls whether to wait for the specified <code>AF_UNIX</code> bus socket to appear in the file system before connecting to it. Defaults to off. When enabled, the tool will watch the file system until the socket is created and then connect to it.</dl>
<p> <code>&#8211;destination=</code><i>SERVICE</i></p>
<dl>
<dt>
<dd> Takes a service name. When used with the <code>emit</code> command, a signal is emitted to the specified service.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the calling user, rather than the service manager of the system.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the system. This is the implied default.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize the output in <code>list</code> command.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
<dd> Do not print the legend, i.e. column headers and the footer with hints.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>PARAMETER FORMATTING</h2>
<p> The <code>call</code> and <code>set-property</code> commands take a signature string followed by a list of parameters formatted as string (for details on D-Bus signature strings, see the m[blue]<code>Type system chapter of the D-Bus specification</code>m[]<font SIZE="-2">[2]</font>). For simple types, each parameter following the signature should simply be the parameter&#8217;s value formatted as string. Positive boolean values may be formatted as &quot;true&quot;, &quot;yes&quot;, &quot;on&quot;, or &quot;1&quot;; negative boolean values may be specified as &quot;false&quot;, &quot;no&quot;, &quot;off&quot;, or &quot;0&quot;. For arrays, a numeric argument for the number of entries followed by the entries shall be specified. For variants, the signature of the contents shall be specified, followed by the contents. For dictionaries and structs, the contents of them shall be directly specified. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
s jawoll
</pre>
</dl>
<p> is the formatting of a single string &quot;jawoll&quot;. </p>
<dl>
<dt>
<dd>
<pre>
as 3 hello world foobar
</pre>
</dl>
<p> is the formatting of a string array with three entries, &quot;hello&quot;, &quot;world&quot; and &quot;foobar&quot;. </p>
<dl>
<dt>
<dd>
<pre>
a{sv} 3 One s Eins Two u 2 Yes b true
</pre>
</dl>
<p> is the formatting of a dictionary array that maps strings to variants, consisting of three entries. The string &quot;One&quot; is assigned the string &quot;Eins&quot;. The string &quot;Two&quot; is assigned the 32-bit unsigned integer 2. The string &quot;Yes&quot; is assigned a positive boolean. </p>
<p> Note that the <code>call</code>, <code>get-property</code>, <code>introspect</code> commands will also generate output in this format for the returned data. Since this format is sometimes too terse to be easily understood, the <code>call</code> and <code>get-property</code> commands may generate a more verbose, multi-line output when passed the <code>&#8211;verbose</code> option.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Write and Read a Property</code> </p>
<p> The following two commands first write a property and then read it back. The property is found on the &quot;/org/freedesktop/systemd1&quot; object of the &quot;org.freedesktop.systemd1&quot; service. The name of the property is &quot;LogLevel&quot; on the &quot;org.freedesktop.systemd1.Manager&quot; interface. The property contains a single string: </p>
<dl>
<dt>
<dd>
<pre>
# busctl set-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel s debug
# busctl get-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel
s &quot;debug&quot;
</pre>
</dl>
<p> <code>Example 2. Terse and Verbose Output</code> </p>
<p> The following two commands read a property that contains an array of strings, and first show it in terse format, followed by verbose format: </p>
<dl>
<dt>
<dd>
<pre><code>
$ busctl get - property org.freedesktop.systemd1 / org / freedesktop / systemd1 org.freedesktop.systemd1.Manager Environment as 2 "LANG=en_US.UTF-8"
                                                                                                                                  "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin" $ busctl get -
    property-- verbose org.freedesktop.systemd1 / org / freedesktop / systemd1 org.freedesktop.systemd1.Manager Environment ARRAY "s"
{
    STRING "LANG=en_US.UTF-8";
    STRING "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin";
};
</code></pre>
</dl>
<p> <code>Example 3. Invoking a Method</code> </p>
<p> The following command invokes the &quot;StartUnit&quot; method on the &quot;org.freedesktop.systemd1.Manager&quot; interface of the &quot;/org/freedesktop/systemd1&quot; object of the &quot;org.freedesktop.systemd1&quot; service, and passes it two strings &quot;cups.service&quot; and &quot;replace&quot;. As a result of the method call, a single object path parameter is received and shown: </p>
<dl>
<dt>
<dd>
<pre>
# busctl call org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager StartUnit ss &quot;cups.service&quot; &quot;replace&quot;
o &quot;/org/freedesktop/systemd1/job/42684&quot;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), m[blue]<code>D-Bus</code>m[]<font SIZE="-2">[3]</font>, <code><a href="/docs/linux/man/3-sd-bus/">sd-bus</a></code>(3), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1), <code><a href="/docs/linux/man/1-wireshark/">wireshark</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Libpcap File Format</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://wiki.wireshark.org/Development/LibpcapFileFormat">https://wiki.wireshark.org/Development/LibpcapFileFormat</a></dl>
<dt> 2.</p>
<dd> Type system chapter of the D-Bus specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://dbus.freedesktop.org/doc/dbus-specification.html#type-system">http://dbus.freedesktop.org/doc/dbus-specification.html#type-system</a></dl>
<dt> 3.</p>
<dd> D-Bus</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/dbus">https://www.freedesktop.org/wiki/Software/dbus</a></dl>
</dl>
<h2>Index</h2>
