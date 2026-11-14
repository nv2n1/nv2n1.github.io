---
title: "repro(8)"
name: "repro"
section: "8"
letter: "r"
url: "/docs/linux/man/8-repro/"
description: "repro – repro SIP proxy server"
---

<p>repro &#8211; repro SIP proxy server</p>
<h2>Synopsis</h2>
<p><code>repro [OPTIONS&#8230;]</code> </p>
<h2>Description</h2>
<p><code>repro</code> is an open-source, free SIP server. SIP is changing the way people communicate using the Internet. It is not only about making phone calls over the Net. The SIP protocol and its extensions defines the way of establishing, modifying and ending interactive sessions, no matter if they are voice, video, IM or a combination of them. At the heart of SIP architecture, there are certain services which needs to be provided at some place of the network. <code>repro</code> provides SIP proxy, registrar, redirect, and identity services. These services are the foundation needed to run a SIP service. </p>
<h2>Options</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;log-type</code>=<code>cout</code>|<code>syslog</code>|<code>cerr</code></p>
<dd>Set where to send logging messages. The default <code>cout</code> sends the messages to standard output, <code>cerr</code> uses the standard error pipe. With <code>syslog</code> the messages are send to the system log using the logging facility <code>local6</code>. See <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5) for more information.</p>
<dt><code>-v</code>, <code>&#8211;log-level</code>=<code>STACK</code>|<code>DEBUG</code>|<code>INFO</code>|<code>WARNING</code>|<code>ALERT</code></p>
<dd>Set the minimum level a logging message needs to have in order to by written. The severity rises from left to right in the above order. The default is to log messages with level <code>INFO</code> or above.</p>
<dt><code>-r</code>, <code>&#8211;record-route</code>=<i>sip:example.com</i></p>
<dd>Activate record routing. The argument is the URI used in the Record-Route header field.</p>
<dt><code>&#8211;udp</code>=<i>5060</i></p>
<dd>Specify the port to use for the UDP transport. Set to 0 to turn UDP off. Defaults to port 5060.</p>
<dt><code>&#8211;tcp</code>=<i>5060</i></p>
<dd>Specify the port to use for the TCP transport. Set to 0 to turn TCP off. Defaults to port 5060.</p>
<dt><code>-t</code>, <code>&#8211;tls-domain</code>=<i>example.com</i></p>
<dd>Act as a TLS server for specified domain.</p>
<dt><code>&#8211;tls</code>=<i>5061</i></p>
<dd>Set the port to use for the TLS transport. Set to 0 to turn TLS off. Defaults to port 5061.</p>
<dt><code>&#8211;dtls</code>=<i>0</i></p>
<dd>Set the port to use for the DTLS transport. Set to 0 to turn DTLS off which is the default.</p>
<dt><code>&#8211;enable-cert-server</p>
<dd>Run a cert server.</p>
<dt>-c</code>, <code>&#8211;cert-path</code>=<i>STRING</i></p>
<dd>Set the path for certificates. Defaults to <code>~/.sipCerts</code>.</p>
<dt><code>&#8211;enable-v6</code></p>
<dd>Enable IPv6.</p>
<dt><code>&#8211;disable-v4</code></p>
<dd>Disable IPv4.</p>
<dt><code>&#8211;disable-auth</code></p>
<dd>Disable DIGEST challenges for certain SIP requests.</p>
<dt><code>&#8211;disable-web-auth</code></p>
<dd>Disable authentication for the web administration server.</p>
<dt><code>&#8211;disable-reg</code></p>
<dd>Disable the registrar.</p>
<dt><code>-i</code>, <code>&#8211;interfaces</code>=<i>sip:10.1.1.1:5065;transport=tls</i></p>
<dd>Specify interfaces to add transports to. Each transport is given as a SIP-URI with the IP address and port of the local interface as the hostport part and the transport protocol as a <code>transport</code> parameter. Several transports are separated by a comma. </p>
<p> For example, to set up two transports, one for TLS and one for UDP use <code>sip:192.168.1.200:5060;transport=tls,sip:192.168.1.200:5060;transport=udp</code></p>
<dt><code>-d</code>, <code>&#8211;domains</code>=<i>example.com,foo.com</i></p>
<dd>Specify the list of domains this proxy is authorative for separated by comma.</p>
<dt><code>-R</code>, <code>&#8211;route</code>=<i>sip:p1.example.com,sip:p2.example.com</i></p>
<dd>Specify a route set where all requests this proxy is authorative for are sent to. Using this option overides the routes set through the web interface.</p>
<dt><code>&#8211;reqChainName</code>=<i>STRING</i></p>
<dd>Name of request chain used for processing requests. Currently, the only chain available is <code>default</code>.</p>
<dt><code>&#8211;http</code>=<i>5080</i></p>
<dd>Specify the port used by the HTTP server. Defaults to 5080.</p>
<dt><code>&#8211;recursive-redirect</code></p>
<dd>Enable to handle of 3xx responses in the proxy.</p>
<dt><code>&#8211;q-value</code></p>
<dd>Enable q-value processing. The q-value can be given in registrations and is used by the location server to order forwarding for multiple registrations. Without this option a request is forked to all registrations.</p>
<dt><code>&#8211;q-value-behavior</code>=<code>FULL_SEQUENTIAL</code>|<code>EQUAL_Q_PARALLEL</code>|<code>FULL_PARALLEL</code></p>
<dd>Specify forking behavior if <code>&#8211;q-value</code> is given. With <code>FULL_SEQUENTIAL</code> one target is called after another in the order of their q values. Using <code>EQUAL_Q_PARALLEL</code> (the default), the request is sent in batches of all registrations with the same q value. The batches are again ordered by the q value. <code>FULL_PARALLEL</code> causes the request to be sent in parallel to all registrations.</p>
<dt><code>&#8211;q-value-cancel-btw-fork-groups</code></p>
<dd>If given, groups of parallel forks are canceled after the period specified by the <code>&#8211;q-value-ms-before-cancel</code> option if no response was received.</p>
<dt><code>&#8211;q-value-wait-for-terminate-btw-fork-groups</code></p>
<dd>If given, the proxy waits for groups of parallel forks to terminate before a new group is started. Otherwise, the next group is started once the waiting time has passed.</p>
<dt><code>&#8211;q-value-ms-between-fork-groups</code>=<i>INT</i></p>
<dd>Specify the number of milliseconds to wait for a response from a group of parallel forks before starting another group.</p>
<dt><code>&#8211;q-value-ms-before-cancel</code>=<i>INT</i></p>
<dd>Specify the number of milliseconds to wait before cancelling a group of parallel forks if the <code>&#8211;q-value-cancel-btw-fork-groups</code> option is given.</p>
<dt><code>-e</code>, <code>&#8211;enum-suffix</code>=<i>e164.arpa</i></p>
<dd>Specify enum suffix to search.</p>
<dt><code>-b</code>, <code>&#8211;allow-bad-reg</code></p>
<dd>Allow To tag in registrations.</p>
<dt><code>&#8211;timer-C</code>=<i>180</i></p>
<dd>Specify the length of timer C in sec which specifies the time a proxy waits before generating a timeout response. Set to 0 or a negative value to turn timer C of completely.</p>
<dt><code>&#8211;admin-password</code>=<i>STRING</i></p>
<dd>Set the web administrator password.</dl>
<p> Help options:</p>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Show a help message.</p>
<dt><code>&#8211;usage</p>
<dd>Display brief usage message.</p>
<dt>&#8211;version</code></p>
<dd>Display the version information. </p>
</dl>
<h2>See Also</h2>
<p>Repro web site at <code><a rel="nofollow" href="http://www.resiprocate.org/About_Repro">http://www.resiprocate.org/About_Repro</a></code> </p>
