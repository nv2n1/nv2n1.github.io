---
title: "websockify(1)"
name: "websockify"
section: "1"
letter: "w"
url: "/docs/linux/man/1-websockify/"
---

<h2 class="name">NAME</h2>
 

 

 websockify - WebSockets to TCP socket bridge

<h2>SYNOPSIS</h2>

 

 
&nbsp;<wbr>websockify&nbsp;<wbr>[options]&nbsp;<wbr>[source_addr:]source_port target_addr:target_port 
&nbsp;<wbr>websockify&nbsp;<wbr>[options]&nbsp;<wbr>[source_addr:]source_port -- WRAP_COMMAND_LINE 

<h2>OPTIONS</h2>

 

 
&nbsp;<wbr>-h, --help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit 
&nbsp;<wbr>-v, --verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>verbose messages and per frame traffic 
&nbsp;<wbr>--record=FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>record sessions to FILE.[session_number] 
&nbsp;<wbr>-D, --daemon&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>become a daemon&nbsp;<wbr>(background process) 
&nbsp;<wbr>--run-once&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>handle a single WebSocket connection and exit 
&nbsp;<wbr>--timeout=TIMEOUT&nbsp;<wbr>&nbsp;<wbr>after TIMEOUT seconds exit when not connected 
&nbsp;<wbr>--cert=CERT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SSL certificate file 
&nbsp;<wbr>--key=KEY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SSL key file&nbsp;<wbr>(if separate from cert) 
&nbsp;<wbr>--ssl-only&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disallow non-encrypted connections 
&nbsp;<wbr>--web=DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run webserver on same port. Serve files from DIR. 
&nbsp;<wbr>--wrap-mode=MODE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>action to take when the wrapped program exits or 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>daemonizes: exit&nbsp;<wbr>(default), ignore, respawn 

<h2>DESCRIPTION</h2>

 

 At the most basic level, websockify just translates WebSockets traffic to normal TCP socket traffic. Websockify accepts the WebSockets handshake, parses it, and then begins forwarding traffic between the client and the target in both directions. 

 websockify was formerly named wsproxy and was part of the noVNC project. 

<h2>NOTES</h2>

 

<h3>WebSockets binary data</h3>

 

 Websockify supports all versions of the WebSockets protocol (Hixie and HyBI). The older Hixie versions of the protocol only support UTF-8 text payloads. In order to transport binary data over UTF-8 an encoding must used to encapsulate the data within UTF-8. Websockify uses base64 to encode all traffic to and from the client. This does not affect the data between websockify and the server. 

<h3>Encrypted WebSocket connections (<a HREF="wss://)">wss://)</a></h3>

 

 To encrypt the traffic using the WebSocket '<a HREF="wss://'">wss://'</a> URI scheme you need to generate a certificate for websockify to load. By default websockify loads a certificate file name self.pem but the --cert=CERT option can override the file name. You can generate a self-signed certificate using openssl. When asked for the common name, use the hostname of the server where the proxy will be running: 

 openssl req -new -x509 -days 365 -nodes -out self.pem -keyout self.pem 

<h3>Websock Javascript library</h3>

 

 The websock.js (see <a rel="nofollow" HREF="https://github.com/kanaka/websockify)">https://github.com/kanaka/websockify)</a> Javascript library library provides a Websock object that is similar to the standard WebSocket object but Websock enables communication with raw TCP sockets (i.e. the binary stream) via websockify. This is accomplished by base64 encoding the data stream between Websock and websockify. 

 Websock has built-in receive queue buffering; the message event does not contain actual data but is simply a notification that there is new data available. Several rQ* methods are available to read binary data off of the receive queue. 

 The Websock API is documented on the websock.js API wiki page: 

 <a rel="nofollow" HREF="https://github.com/kanaka/websockify/wiki/websock.js">https://github.com/kanaka/websockify/wiki/websock.js</a> 

 See the &quot;Wrap a Program&quot; section below for an example of using Websock and websockify as a browser telnet client (wstelnet.html). 

<h3>Additional websockify features</h3>

 

 These are not necessary for the basic operation. 

<dl>
<dt>*
<dd> Daemonizing: When the -D option is specified, websockify runs in the background as a daemon process. 

<dt>*
<dd> SSL (the wss:// WebSockets URI): This is detected automatically by websockify by sniffing the first byte sent from the client and then wrapping the socket if the data starts with '\x16' or '\x80' (indicating SSL). 

<dt>*
<dd> Flash security policy: websockify detects flash security policy requests (again by sniffing the first packet) and answers with an appropriate flash security policy response (and then closes the port). This means no separate flash security policy server is needed for supporting the flash WebSockets fallback emulator. 

<dt>*
<dd> Session recording: This feature that allows recording of the traffic sent and received from the client to a file using the --record option. 

<dt>*
<dd> Mini-webserver: websockify can detect and respond to normal web requests on the same port as the WebSockets proxy and Flash security policy. This functionality is activate with the --web DIR option where DIR is the root of the web directory to serve. 

<dt>*
<dd> Wrap a program: see the &quot;Wrap a Program&quot; section below. 

</dl>

<h3>Wrap a Program</h3>

 

 In addition to proxying from a source address to a target address (which may be on a different system), websockify has the ability to launch a program on the local system and proxy WebSockets traffic to a normal TCP port owned/bound by the program. 

 The is accomplished with a small LD_PRELOAD library (rebind.so) which intercepts bind() system calls by the program. The specified port is moved to a new localhost/loopback free high port. websockify then proxies WebSockets traffic directed to the original port to the new (moved) port of the program. 

 The program wrap mode is invoked by replacing the target with -- followed by the program command line to wrap. 

 `./websockify 2023 -- PROGRAM ARGS` 

 The --wrap-mode option can be used to indicate what action to take when the wrapped program exits or daemonizes. 

 Here is an example of using websockify to wrap the vncserver command (which backgrounds itself) for use with noVNC: 

 `./websockify 5901 --wrap-mode=ignore -- vncserver -geometry 1024x768 :1` 

 Here is an example of wrapping telnetd (from krb5-telnetd).telnetd exits after the connection closes so the wrap mode is set to respawn the command: 

 `sudo ./websockify 2023 --wrap-mode=respawn -- telnetd -debug 2023` 

 The wstelnet.html page demonstrates a simple WebSockets based telnet client. 

 

<h2>AUTHOR</h2>

 Joel Martin (github [at] martintribe.org) 

<h2>SEE ALSO</h2>

 

 <a rel="nofollow" HREF="https://github.com/kanaka/websockify/">https://github.com/kanaka/websockify/</a> 

 <a rel="nofollow" HREF="https://github.com/kanaka/websockify/wiki/">https://github.com/kanaka/websockify/wiki/</a> 

 

<h2>Index</h2>


