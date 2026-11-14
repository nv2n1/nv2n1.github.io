---
title: "mosquitto_pub(1)"
name: "mosquitto_pub"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mosquitto_pub/"
description: "mosquitto_pub – an MQTT version 3.1/3.1.1 client for publishing simple messages"
---

<h2 class="name">NAME</h2>
<p> mosquitto_pub &#8211; an MQTT version 3.1/3.1.1 client for publishing simple messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mosquitto_pub</code> [<code>-A</code>&nbsp;<wbr><i>bind_address</i>] [<code>-d</code>] [<code>-h</code>&nbsp;<wbr><i>hostname</i>] [<code>-i</code>&nbsp;<wbr><i>client_id</i>] [<code>-I</code>&nbsp;<wbr><i>client id prefix</i>] [<code>-k</code>&nbsp;<wbr><i>keepalive time</i>] [<code>-p</code>&nbsp;<wbr><i>port number</i>] [<code>-q</code>&nbsp;<wbr><i>message QoS</i>] [<code>&#8211;quiet</code>] [<code>-r</code>] [<code>-S</code>] {<code>-f</code>&nbsp;<wbr><i>file</i> | <code>-l</code> | <code>-m</code>&nbsp;<wbr><i>message</i> | <code>-n</code> | <code>-s</code>} [[<code>-u</code>&nbsp;<wbr><i>username</i>]&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr><i>password</i>]] [<code>&#8211;will-topic</code>&nbsp;<wbr><i>topic</i>&nbsp;<wbr>[<code>&#8211;will-payload</code>&nbsp;<wbr><i>payload</i>]&nbsp;<wbr>[<code>&#8211;will-qos</code>&nbsp;<wbr><i>qos</i>]&nbsp;<wbr>[<code>&#8211;will-retain</code>]] [[{<code>&#8211;cafile</code>&nbsp;<wbr><i>file</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;capath</code>&nbsp;<wbr><i>dir</i>}&nbsp;<wbr>[<code>&#8211;cert</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>&#8211;key</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>&#8211;ciphers</code>&nbsp;<wbr><i>ciphers</i>]&nbsp;<wbr>[<code>&#8211;tls-version</code>&nbsp;<wbr><i>version</i>]&nbsp;<wbr>[<code>&#8211;insecure</code>]] | [<code>&#8211;psk</code>&nbsp;<wbr><i>hex-key</i>&nbsp;<wbr><code>&#8211;psk-identity</code>&nbsp;<wbr><i>identity</i>&nbsp;<wbr>[<code>&#8211;ciphers</code>&nbsp;<wbr><i>ciphers</i>]&nbsp;<wbr>[<code>&#8211;tls-version</code>&nbsp;<wbr><i>version</i>]]] [<code>&#8211;proxy</code>&nbsp;<wbr><i>socks-url</i>] [<code>-V</code>&nbsp;<wbr><i>protocol-version</i>] <code>-t</code>&nbsp;<wbr><i>message-topic</i></p>
<dt> <code>mosquitto_pub</code> [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mosquitto_pub</code></p>
<dd>is a simple MQTT version 3.1 client that will publish a single message on a topic and exit.</p>
<h2>OPTIONS</h2>
<p> The options below may be given on the command line, but may also be placed in a config file located at <code>$XDG_CONFIG_HOME/mosquitto_pub</code> or <code>$HOME/.config/mosquitto_sub</code> with one pair of <code>-option </code><i>value</i> per line. The values in the config file will be used as defaults and can be overridden by using the command line. The exceptions to this are the message type options, of which only one can be specified. Note also that currently some options cannot be negated, e.g. <code>-S</code>. Config file lines that have a <code>#</code> as the first character are treated as comments and not processed any further. </p>
<p> <code>-A</code></p>
<dl>
<dt>
<dd> Bind the outgoing connection to a local ip address/hostname. Use this argument if you need to restrict network communication to a particular interface.</dl>
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
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Enable debug messages.</dl>
<p> <code>-f</code>, <code>&#8211;file</code></p>
<dl>
<dt>
<dd> Send the contents of a file as the message.</dl>
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
<dd> The id to use for this client. If not given, defaults to mosquitto_pub_ appended with the process id of the client. Cannot be used at the same time as the <code>&#8211;id-prefix</code> argument.</dl>
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
<p> <code>-l</code>, <code>&#8211;stdin-line</code></p>
<dl>
<dt>
<dd> Send messages read from stdin, splitting separate lines into separate messages. Note that blank lines won&#8217;t be sent.</dl>
<p> <code>-m</code>, <code>&#8211;message</code></p>
<dl>
<dt>
<dd> Send a single message from the command line.</dl>
<p> <code>-n</code>, <code>&#8211;null-message</code></p>
<dl>
<dt>
<dd> Send a null (zero length) message.</dl>
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
<dd> Specify the quality of service to use for the message, from 0, 1 and 2. Defaults to 0.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> If this argument is given, no runtime errors will be printed. This excludes any error messages given in case of invalid user input (e.g. using <code>&#8211;port</code> without a port).</dl>
<p> <code>-r</code>, <code>&#8211;retain</code></p>
<dl>
<dt>
<dd> If retain is given, the message will be retained as a &quot;last known good&quot; value on the broker. See <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7) for more information.</dl>
<p> <code>-s</code>, <code>&#8211;stdin-file</code></p>
<dl>
<dt>
<dd> Send a message read from stdin, sending the entire content as a single message.</dl>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> Use SRV lookups to determine which host to connect to. Performs lookups to <code>_mqtt._tcp.&lt;host&gt;</code> when used in conjunction with <code>-h</code>, otherwise uses <code>_mqtt._tcp.&lt;local dns domain&gt;</code>.</dl>
<p> <code>-t</code>, <code>&#8211;topic</code></p>
<dl>
<dt>
<dd> The MQTT topic on which to publish the message. See <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7) for more information on MQTT topics.</dl>
<p> <code>&#8211;tls-version</code></p>
<dl>
<dt>
<dd> Choose which TLS protocol version to use when communicating with the broker. Valid options are <code>tlsv1.2</code>, <code>tlsv1.1</code> and <code>tlsv1</code>. The default value is <code>tlsv1.2</code>. If the installed version of openssl is too old, only <code>tlsv1</code> will be available. Must match the protocol version used by the broker.</dl>
<p> <code>-u</code>, <code>&#8211;username</code></p>
<dl>
<dt>
<dd> Provide a username to be used for authenticating with the broker. This requires a broker that supports MQTT v3.1. See also the <code>&#8211;pw</code> argument.</dl>
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
<p> Publish temperature information to localhost with QoS 1: </p>
<dl>
<dt>
<dd> &bull; mosquitto_pub -t sensors/temperature -m 32 -q 1</dl>
<p> Publish timestamp and temperature information to a remote host on a non-standard port and QoS 0: </p>
<dl>
<dt>
<dd> &bull; mosquitto_pub -h 192.168.1.1 -p 1885 -t sensors/temperature -m &quot;1266193804 32&quot;</dl>
<p> Publish light switch status. Message is set to retained because there may be a long period of time between light switch events: </p>
<dl>
<dt>
<dd> &bull; mosquitto_pub -r -t switches/kitchen_lights/status -m &quot;on&quot;</dl>
<p> Send the contents of a file in two ways: </p>
<dl>
<dt>
<dd> &bull; mosquitto_pub -t my/topic -f ./data</dl>
<dl>
<dt>
<dd> &bull; mosquitto_pub -t my/topic -s &lt; ./data</dl>
<p> Send parsed electricity usage data from a Current Cost meter, reading from stdin with one line/reading as one message: </p>
<dl>
<dt>
<dd> &bull; read_cc128.pl | mosquitto_pub -t sensors/cc128 -l</dl>
<h2>FILES</h2>
<p> $XDG_CONFIG_HOME/mosquitto_pub, $HOME/.config/mosquitto_pub</p>
<dl>
<dt>
<dd> Configuration file for default options.</dl>
<h2>BUGS</h2>
<p> <code>mosquitto_pub</code> bug information can be found at <a rel="nofollow" href="https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto">https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7), <code><a href="/docs/linux/man/1-mosquitto_sub/">mosquitto_sub</a></code>(1), <code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8), <code><a href="/docs/linux/man/3-libmosquitto/">libmosquitto</a></code>(3), <code><a href="/docs/linux/man/7-mosquitto-tls/">mosquitto-tls</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> Roger Light &lt;roger [at] atchoo.org&gt; </p>
<h2>Index</h2>
