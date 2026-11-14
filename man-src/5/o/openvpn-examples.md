---
title: "openvpn-examples(5)"
name: "openvpn-examples"
section: "5"
letter: "o"
url: "/docs/linux/man/5-openvpn-examples/"
description: "openvpn examples – Secure IP tunnel daemon"
---

<p>openvpn examples &#8211; Secure IP tunnel daemon</p>
<h2>Introduction</h2>
<p>This man page gives a few simple examples to create OpenVPN setups and configuration files.</p>
<h2>Examples</h2>
<p>Prior to running these examples, you should have OpenVPN installed on two machines with network connectivity between them. If you have not yet installed OpenVPN, consult the INSTALL file included in the OpenVPN distribution.</p>
<h3>Firewall Setup:</h3>
<p>If firewalls exist between the two machines, they should be set to forward the port OpenVPN is configured to use, in both directions. The default for OpenVPN is 1194/udp. If you do not have control over the firewalls between the two machines, you may still be able to use OpenVPN by adding <code>&#8211;ping 15</code> to each of the <code>openvpn</code> commands used below in the examples (this will cause each peer to send out a UDP ping to its remote peer once every 15 seconds which will cause many stateful firewalls to forward packets in both directions without an explicit firewall rule). Please see your operating system guides for how to configure the firewall on your systems.</p>
<h3>VPN Address Setup:</h3>
<p>For purposes of our example, our two machines will be called <code>bob.example.com</code> and <code>alice.example.com</code>. If you are constructing a VPN over the internet, then replace <code>bob.example.com</code> and <code>alice.example.com</code> with the internet hostname or IP address that each machine will use to contact the other over the internet. Now we will choose the tunnel endpoints. Tunnel endpoints are private IP addresses that only have meaning in the context of the VPN. Each machine will use the tunnel endpoint of the other machine to access it over the VPN. In our example, the tunnel endpoint for bob.example.com will be 10.4.0.1 and for alice.example.com, 10.4.0.2. Once the VPN is established, you have essentially created a secure alternate path between the two hosts which is addressed by using the tunnel endpoints. You can control which network traffic passes between the hosts (a) over the VPN or (b) independently of the VPN, by choosing whether to use (a) the VPN endpoint address or (b) the public internet address, to access the remote host. For example if you are on bob.example.com and you wish to connect to <code>alice.example.com</code> via <code>ssh</code> without using the VPN (since <code>ssh</code> has its own built-in security) you would use the command <code>ssh alice.example.com</code>. However in the same scenario, you could also use the command <code>telnet 10.4.0.2</code> to create a telnet session with alice.example.com over the VPN, that would use the VPN to secure the session rather than <code>ssh</code>. You can use any address you wish for the tunnel endpoints but make sure that they are private addresses (such as those that begin with 10 or 192.168) and that they are not part of any existing subnet on the networks of either peer, unless you are bridging. If you use an address that is part of your local subnet for either of the tunnel endpoints, you will get a weird feedback loop.</p>
<h3>Example 1: A simple tunnel without security</h3>
<p>On bob: </p>
<pre>openvpn --remote alice.example.com --dev tun1 \
 --ifconfig 10.4.0.1 10.4.0.2 --verb 9</pre>
<p>On alice: </p>
<pre>openvpn --remote bob.example.com --dev tun1 \
 --ifconfig 10.4.0.2 10.4.0.1 --verb 9</pre>
<p>Now verify the tunnel is working by pinging across the tunnel. On bob: </p>
<pre>ping 10.4.0.2</pre>
<p>On alice: </p>
<pre>ping 10.4.0.1</pre>
<p>The <code>&#8211;verb 9</code> option will produce verbose output, similar to the <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8) program. Omit the <code>&#8211;verb 9</code> option to have OpenVPN run quietly.</p>
<h3>Example 2: A tunnel with static-key security (i.e. using a pre-shared secret)</h3>
<p>First build a static key on bob. </p>
<pre>openvpn --genkey --secret key</pre>
<p>This command will build a key file called <code>key</code> (in ascii format). Now copy <code>key</code> to <code>alice.example.com</code> over a secure medium such as by using the <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1) program. On bob: </p>
<pre>openvpn --remote alice.example.com --dev tun1 \
 --ifconfig 10.4.0.1 10.4.0.2 --verb 5 \
 --secret key</pre>
<p>On alice: </p>
<pre>openvpn --remote bob.example.com --dev tun1 \
 --ifconfig 10.4.0.2 10.4.0.1 --verb 5 \
 --secret key</pre>
<p>Now verify the tunnel is working by pinging across the tunnel. On bob: </p>
<pre>ping 10.4.0.2</pre>
<p>On alice: </p>
<pre>ping 10.4.0.1</pre>
<h3>Example 3: A tunnel with full TLS-based security</h3>
<p>For this test, we will designate <code>bob</code> as the TLS client and <code>alice</code> as the TLS server.</p>
<dl>
<dt><i>Note:</i></p>
<dd>The client or server designation only has meaning for the TLS subsystem. It has no bearing on OpenVPN&#8217;s peer-to-peer, UDP-based communication model.* First, build a separate certificate/key pair for both bob and alice (see above where <code>&#8211;cert</code> is discussed for more info). Then construct Diffie Hellman parameters (see above where <code>&#8211;dh</code> is discussed for more info). You can also use the included test files <code>client.crt</code>, <code>client.key</code>, <code>server.crt</code>, <code>server.key</code> and <code>ca.crt</code>. The <code>.crt</code> files are certificates/public-keys, the <code>.key</code> files are private keys, and <code>ca.crt</code> is a certification authority who has signed both <code>client.crt</code> and <code>server.crt</code>. For Diffie Hellman parameters you can use the included file <code>dh2048.pem</code>.</p>
<dt><i>WARNING:</i></p>
<dd>All client, server, and certificate authority certificates and keys included in the OpenVPN distribution are totally insecure and should be used for testing only. On bob: </p>
<pre>openvpn --remote alice.example.com --dev tun1 \
 --ifconfig 10.4.0.1 10.4.0.2 \
 --tls-client --ca ca.crt \
 --cert client.crt --key client.key \
 --reneg-sec 60 --verb 5</pre>
<p>On alice: </p>
<pre>openvpn --remote bob.example.com --dev tun1 \
 --ifconfig 10.4.0.2 10.4.0.1 \
 --tls-server --dh dh1024.pem --ca ca.crt \
 --cert server.crt --key server.key \
 --reneg-sec 60 --verb 5</pre>
<p>Now verify the tunnel is working by pinging across the tunnel. On bob: </p>
<pre>ping 10.4.0.2</pre>
<p>On alice: </p>
<pre>ping 10.4.0.1</pre>
<p>Notice the <code>&#8211;reneg-sec 60</code> option we used above. That tells OpenVPN to renegotiate the data channel keys every minute. Since we used <code>&#8211;verb 5</code> above, you will see status information on each new key negotiation. For production operations, a key renegotiation interval of 60 seconds is probably too frequent. Omit the <code>&#8211;reneg-sec 60</code> option to use OpenVPN&#8217;s default key renegotiation interval of one hour.</dl>
<h3>Routing:</h3>
<p>Assuming you can ping across the tunnel, the next step is to route a real subnet over the secure tunnel. Suppose that bob and alice have two network interfaces each, one connected to the internet, and the other to a private network. Our goal is to securely connect both private networks. We will assume that bob&#8217;s private subnet is <i>10.0.0.0/24</i> and alice&#8217;s is <i>10.0.1.0/24</i>. First, ensure that IP forwarding is enabled on both peers. On Linux, enable routing: </p>
<pre>echo 1 &gt; /proc/sys/net/ipv4/ip_forward</pre>
<p>This setting is not persistent. Please see your operating systems documentation how to properly configure IP forwarding, which is also persistent through system boots. If your system is configured with a firewall. Please see your operating systems guide on how to configure the firewall. You typically want to allow traffic coming from and going to the tun/tap adapter OpenVPN is configured to use. On bob: </p>
<pre>route add -net 10.0.1.0 netmask 255.255.255.0 gw 10.4.0.2</pre>
<p>On alice: </p>
<pre>route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.4.0.1</pre>
<p>Now any machine on the <i>10.0.0.0/24</i> subnet can access any machine on the <i>10.0.1.0/24</i> subnet over the secure tunnel (or vice versa). In a production environment, you could put the route command(s) in a script and execute with the <code>&#8211;up</code> option. </p>
