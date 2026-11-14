---
title: "mosquitto_sub(1)"
name: "mosquitto_sub"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mosquitto_sub/"
description: "mosquitto_sub – an MQTT version 3.1 client for subscribing to topics"
---

<h2 class="name">NAME</h2>
<p> mosquitto_sub &#8211; an MQTT version 3.1 client for subscribing to topics </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mosquitto_sub</code> [<code>-A</code>&nbsp;<wbr><i>bind_address</i>] [<code>-c</code>] [<code>-C</code>&nbsp;<wbr><i>msg count</i>] [<code>-d</code>] [<code>-h</code>&nbsp;<wbr><i>hostname</i>] [<code>-i</code>&nbsp;<wbr><i>client_id</i>] [<code>-I</code>&nbsp;<wbr><i>client id prefix</i>] [<code>-k</code>&nbsp;<wbr><i>keepalive time</i>] [<code>-p</code>&nbsp;<wbr><i>port number</i>] [<code>-q</code>&nbsp;<wbr><i>message QoS</i>] [<code>-R</code>] [<code>-S</code>] [<code>-N</code>] [<code>&#8211;quiet</code>] [<code>-v</code>] [[<code>-u</code>&nbsp;<wbr><i>username</i>]&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr><i>password</i>]] [<code>&#8211;will-topic</code>&nbsp;<wbr><i>topic</i>&nbsp;<wbr>[<code>&#8211;will-payload</code>&nbsp;<wbr><i>payload</i>]&nbsp;<wbr>[<code>&#8211;will-qos</code>&nbsp;<wbr><i>qos</i>]&nbsp;<wbr>[<code>&#8211;will-retain</code>]] [[{<code>&#8211;cafile</code>&nbsp;<wbr><i>file</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;capath</code>&nbsp;<wbr><i>dir</i>}&nbsp;<wbr>[<code>&#8211;cert</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>&#8211;key</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>&#8211;tls-version</code>&nbsp;<wbr><i>version</i>]&nbsp;<wbr>[<code>&#8211;insecure</code>]] | [<code>&#8211;psk</code>&nbsp;<wbr><i>hex-key</i>&nbsp;<wbr><code>&#8211;psk-identity</code>&nbsp;<wbr><i>identity</i>&nbsp;<wbr>[<code>&#8211;tls-version</code>&nbsp;<wbr><i>version</i>]]] [<code>&#8211;proxy</code>&nbsp;<wbr><i>socks-url</i>] [<code>-V</code>&nbsp;<wbr><i>protocol-version</i>] [<code>-T</code>&nbsp;<wbr><i>filter-out</i>&#8230;] <code>-t</code>&nbsp;<wbr><i>message-topic</i>&#8230;</p>
<dt> <code>mosquitto_sub</code> [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mosquitto_sub</code></p>
<dd>is a simple MQTT version 3.1 client that will subscribe to a topic and print the messages that it receives.</p>
<h2>OPTIONS</h2>
<p> The options below may be given on the command line, but may also be placed in a config file located at <code>$XDG_CONFIG_HOME/mosquitto_sub</code> or <code>$HOME/.config/mosquitto_sub</code> with one pair of <code>-option </code><i>value</i> per line. The values in the config file will be used as defaults and can be overridden by using the command line. The exceptions to this are <code>-t</code> and <code>-T</code>, which if given in the config file will not be overridden. Note also that currently some options cannot be negated, e.g. <code>-S</code>. Config file lines that have a <code>#</code> as the first character are treated as comments and not processed any further. </p>
<p> <code>-A</code></p>
<dl>
<dt>
<dd> Bind the outgoing connection to a local ip address/hostname. Use this argument if you need to restrict network communication to a particular interface.</dl>
<p> <code>-c</code>, <code>&#8211;disable-clean-session</code></p>
<dl>
<dt>
<dd> Disable the &#8216;clean session&#8217; flag. This means that all of the subscriptions for the client will be maintained after it disconnects, along with subsequent QoS 1 and QoS 2 messages that arrive. When the client reconnects, it will receive all of the queued messages. </p>
<p> If using this option, it is recommended that the client id is set manually with <code>&#8211;id</code></dl>
<p> <code>&#8211;cafile</code></p>
<dl>
<dt>
<dd> Define the path to a file containing PEM encoded CA certificates that are trusted. Used to enable SSL communication. </p>
<p> See also <code>&#8211;capath</code></dl>
<p> <code>&#8211;capath</code></p>
<dl>
<dt>
<dd> Define the path to a directory containing PEM encoded CA certificates that are trusted. Used to enable SSL communication. </p>
<p> For <code>&#8211;capath</code> to work correctly, the certificate files must have &quot;.crt&quot; as the file ending and you must run &quot;c_rehash &lt;path to capath&gt;&quot; each time you add/remove a certificate. </p>
<p> See also <code>&#8211;cafile</code></dl>
<p> <code>&#8211;cert</code></p>
<dl>
<dt>
<dd> Define the path to a file containing a PEM encoded certificate for this client, if required by the server. </p>
<p> See also <code>&#8211;key</code>.</dl>
<p> <code>&#8211;ciphers</code></p>
<dl>
<dt>
<dd> An openssl compatible list of TLS ciphers to support in the client. See <code><a href="/docs/linux/man/1-ciphers/">ciphers</a></code>(1) for more information.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> Disconnect and exit the program immediately after the given count of messages have been received. This may be useful in shell scripts where on a single status value is required, for example. </p>
<p> Combine with <code>-R</code> to print only the first set of fresh messages (i.e. that does not have the retained flag set), or with <code>-T</code> to filter which topics are processed.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Enable debug messages.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display usage information.</dl>
<p> <code>-h</code>, <code>&#8211;host</code></p>
<dl>
<dt>
<dd> Specify the host to connect to. Defaults to localhost.</dl>
<p> <code>-i</code>, <code>&#8211;id</code></p>
<dl>
<dt>
<dd> The id to use for this client. If not given, defaults to mosquitto_sub_ appended with the process id of the client. Cannot be used at the same time as the <code>&#8211;id-prefix</code> argument.</dl>
<p> <code>-I</code>, <code>&#8211;id-prefix</code></p>
<dl>
<dt>
<dd> Provide a prefix that the client id will be built from by appending the process id of the client. This is useful where the broker is using the clientid_prefixes option. Cannot be used at the same time as the <code>&#8211;id</code> argument.</dl>
<p> <code>&#8211;insecure</code></p>
<dl>
<dt>
<dd> When using certificate based encryption, this option disables verification of the server hostname in the server certificate. This can be useful when testing initial server configurations but makes it possible for a malicious third party to impersonate your server through DNS spoofing, for example. Use this option in testing <i>only</i>. If you need to resort to using this option in a production environment, your setup is at fault and there is no point using encryption.</dl>
<p> <code>-k</code>, <code>&#8211;keepalive</code></p>
<dl>
<dt>
<dd> The number of seconds between sending PING commands to the broker for the purposes of informing it we are still connected and functioning. Defaults to 60 seconds.</dl>
<p> <code>&#8211;key</code></p>
<dl>
<dt>
<dd> Define the path to a file containing a PEM encoded private key for this client, if required by the server. </p>
<p> See also <code>&#8211;cert</code>.</dl>
<p> <code>-N</code></p>
<dl>
<dt>
<dd> Do not append an end of line character to the payload when printing. This allows streaming of payload data from multiple messages directly to another application unmodified. Only really makes sense when not using <code>-v</code>.</dl>
<p> <code>-p</code>, <code>&#8211;port</code></p>
<dl>
<dt>
<dd> Connect to the port specified instead of the default 1883.</dl>
<p> <code>-P</code>, <code>&#8211;pw</code></p>
<dl>
<dt>
<dd> Provide a password to be used for authenticating with the broker. Using this argument without also specifying a username is invalid. This requires a broker that supports MQTT v3.1. See also the <code>&#8211;username</code> option.</dl>
<p> <code>&#8211;proxy</code></p>
<dl>
<dt>
<dd> Specify a SOCKS5 proxy to connect through. &quot;None&quot; and &quot;username&quot; authentication types are supported. The <code>socks-url</code> must be of the form <code>socks5h://[username[:password]@]host[:port]</code>. The protocol prefix <code>socks5h</code> means that hostnames are resolved by the proxy. The symbols %25, %3A and %40 are URL decoded into %, : and @ respectively, if present in the username or password. </p>
<p> If username is not given, then no authentication is attempted. If the port is not given, then the default of 1080 is used. </p>
<p> More SOCKS versions may be available in the future, depending on demand, and will use different protocol prefixes as described in <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1).</dl>
<p> <code>&#8211;psk</code></p>
<dl>
<dt>
<dd> Provide the hexadecimal (no leading 0x) pre-shared-key matching the one used on the broker to use TLS-PSK encryption support. <code>&#8211;psk-identity</code> must also be provided to enable TLS-PSK.</dl>
<p> <code>&#8211;psk-identity</code></p>
<dl>
<dt>
<dd> The client identity to use with TLS-PSK support. This may be used instead of a username if the broker is configured to do so.</dl>
<p> <code>-q</code>, <code>&#8211;qos</code></p>
<dl>
<dt>
<dd> Specify the quality of service desired for the incoming messages, from 0, 1 and 2. Defaults to 0. See <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7) for more information on QoS. </p>
<p> The QoS is identical for all topics subscribed to in a single instance of mosquitto_sub.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> If this argument is given, no runtime errors will be printed. This excludes any error messages given in case of invalid user input (e.g. using <code>&#8211;port</code> without a port).</dl>
<p> <code>-R</code></p>
<dl>
<dt>
<dd> If this argument is given, messages that are received that have the retain bit set will not be printed. Messages with retain set are &quot;stale&quot;, in that it is not known when they were originally published. When subscribing to a wildcard topic there may be a large number of retained messages. This argument suppresses their display.</dl>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> Use SRV lookups to determine which host to connect to. Performs lookups to <code>_mqtt._tcp.&lt;host&gt;</code> when used in conjunction with <code>-h</code>, otherwise uses <code>_mqtt._tcp.&lt;local dns domain&gt;</code>.</dl>
<p> <code>-t</code>, <code>&#8211;topic</code></p>
<dl>
<dt>
<dd> The MQTT topic to subscribe to. See <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7) for more information on MQTT topics. </p>
<p> This option may be repeated to subscribe to multiple topics.</dl>
<p> <code>-T</code>, <code>&#8211;filter-out</code></p>
<dl>
<dt>
<dd> Suppress printing of topics that match the filter. This allows subscribing to a wildcard topic and only printing a partial set of the wildcard hierarchy. </p>
<p> For example, subscribe to the BBC tree, but suppress output from Radio 3: </p>
<dl>
<dt>
<dd> &bull; mosquitto_sub -t bbc/# -T bbc/radio3</dl>
<p> This option may be repeated to filter out multiple topics or topic trees.</dl>
<p> <code>&#8211;tls-version</code></p>
<dl>
<dt>
<dd> Choose which TLS protocol version to use when communicating with the broker. Valid options are <code>tlsv1.2</code>, <code>tlsv1.1</code> and <code>tlsv1</code>. The default value is <code>tlsv1.2</code>. If the installed version of openssl is too old, only <code>tlsv1</code> will be available. Must match the protocol version used by the broker.</dl>
<p> <code>-u</code>, <code>&#8211;username</code></p>
<dl>
<dt>
<dd> Provide a username to be used for authenticating with the broker. This requires a broker that supports MQTT v3.1. See also the <code>&#8211;pw</code> argument.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print received messages verbosely. With this argument, messages will be printed as &quot;topic payload&quot;. When this argument is not given, the messages are printed as &quot;payload&quot;.</dl>
<p> <code>-V</code>, <code>&#8211;protocol-version</code></p>
<dl>
<dt>
<dd> Specify which version of the MQTT protocol should be used when connecting to the rmeote broker. Can be <code>mqttv31</code> or <code>mqttv311</code>. Defaults to <code>mqttv31</code>.</dl>
<p> <code>&#8211;will-payload</code></p>
<dl>
<dt>
<dd> Specify a message that will be stored by the broker and sent out if this client disconnects unexpectedly. This must be used in conjunction with <code>&#8211;will-topic</code>.</dl>
<p> <code>&#8211;will-qos</code></p>
<dl>
<dt>
<dd> The QoS to use for the Will. Defaults to 0. This must be used in conjunction with <code>&#8211;will-topic</code>.</dl>
<p> <code>&#8211;will-retain</code></p>
<dl>
<dt>
<dd> If given, if the client disconnects unexpectedly the message sent out will be treated as a retained message. This must be used in conjunction with <code>&#8211;will-topic</code>.</dl>
<p> <code>&#8211;will-topic</code></p>
<dl>
<dt>
<dd> The topic on which to send a Will, in the event that the client disconnects unexpectedly.</dl>
<h2>WILLS</h2>
<p> mosquitto_sub can register a message with the broker that will be sent out if it disconnects unexpectedly. See <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7) for more information. </p>
<p> The minimum requirement for this is to use <code>&#8211;will-topic</code> to specify which topic the will should be sent out on. This will result in a non-retained, zero length message with QoS 0. </p>
<p> Use the <code>&#8211;will-retain</code>, <code>&#8211;will-payload</code> and <code>&#8211;will-qos</code> arguments to modify the other will parameters.</p>
<h2>EXAMPLES</h2>
<p> Note that these really are examples &#8211; the subscriptions will work if you run them as shown, but there must be something publishing messages on those topics for you to receive anything. </p>
<p> Subscribe to temperature information on localhost with QoS 1: </p>
<dl>
<dt>
<dd> &bull; mosquitto_sub -t sensors/temperature -q 1</dl>
<p> Subscribe to hard drive temperature updates on multiple machines/hard drives. This expects each machine to be publishing its hard drive temperature to sensors/machines/HOSTNAME/temperature/HD_NAME. </p>
<dl>
<dt>
<dd> &bull; mosquitto_sub -t sensors/machines/+/temperature/+</dl>
<p> Subscribe to all broker status messages: </p>
<dl>
<dt>
<dd> &bull; mosquitto_sub -v -t \$SYS/#</dl>
<h2>FILES</h2>
<p> $XDG_CONFIG_HOME/mosquitto_sub, $HOME/.config/mosquitto_sub</p>
<dl>
<dt>
<dd> Configuration file for default options.</dl>
<h2>BUGS</h2>
<p> <code>mosquitto_sub</code> bug information can be found at <a rel="nofollow" href="https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto">https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7), <code><a href="/docs/linux/man/1-mosquitto_pub/">mosquitto_pub</a></code>(1), <code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8), <code><a href="/docs/linux/man/3-libmosquitto/">libmosquitto</a></code>(3), <code><a href="/docs/linux/man/7-mosquitto-tls/">mosquitto-tls</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> Roger Light &lt;roger [at] atchoo.org&gt; </p>
<h2>Index</h2>
