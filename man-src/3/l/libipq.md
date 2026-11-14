---
title: "libipq(3)"
name: "libipq"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libipq/"
description: "libipq — iptables userspace packet queuing library."
---

<h2 class="name">NAME</h2>
<p> libipq &#8212; iptables userspace packet queuing library. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/linux/netfilter.h">linux/netfilter.h</a>&gt;</code><br />
 <code>#include &lt;<a href="file:/usr/include/libipq.h">libipq.h</a>&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> libipq is a development library for iptables userspace packet queuing.</p>
<h3>Userspace Packet Queuing</h3>
<p> Netfilter provides a mechanism for passing packets out of the stack for queueing to userspace, then receiving these packets back into the kernel with a verdict specifying what to do with the packets (such as ACCEPT or DROP). These packets may also be modified in userspace prior to reinjection back into the kernel. </p>
<p> For each supported protocol, a kernel module called a <i>queue handler</i> may register with Netfilter to perform the mechanics of passing packets to and from userspace. </p>
<p> The standard queue handler for IPv4 is ip_queue. It is provided as an experimental module with 2.4 kernels, and uses a Netlink socket for kernel/userspace communication. </p>
<p> Once ip_queue is loaded, IP packets may be selected with iptables and queued for userspace processing via the QUEUE target. For example, running the following commands: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># modprobe iptable_filter</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># modprobe ip_queue</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># iptables -A OUTPUT -p icmp -j QUEUE</p>
<p> will cause any locally generated ICMP packets (e.g. ping output) to be sent to the ip_queue module, which will then attempt to deliver the packets to a userspace application. If no userspace application is waiting, the packets will be dropped </p>
<p> An application may receive and process these packets via libipq. </p>
<h3>Libipq Overview</h3>
<p> Libipq provides an API for communicating with ip_queue. The following is an overview of API usage, refer to individual man pages for more details on each function. </p>
<p> <code>Initialisation</code><br />
 To initialise the library, call <code><a href="/docs/linux/man/3-ipq_create_handle/">ipq_create_handle</a></code>(3). This will attempt to bind to the Netlink socket used by ip_queue and return an opaque context handle for subsequent library calls. </p>
<p> <code>Setting the Queue Mode</code><br />
 <code><a href="/docs/linux/man/3-ipq_set_mode/">ipq_set_mode</a></code>(3) allows the application to specify whether packet metadata, or packet payloads as well as metadata are copied to userspace. It is also used to initially notify ip_queue that an application is ready to receive queue messages. </p>
<p> <code>Receiving Packets from the Queue</code><br />
 <code><a href="/docs/linux/man/3-ipq_read/">ipq_read</a></code>(3) waits for queue messages to arrive from ip_queue and copies them into a supplied buffer. Queue messages may be <i>packet messages</i> or <i>error messages.</i> </p>
<p> The type of packet may be determined with <code><a href="/docs/linux/man/3-ipq_message_type/">ipq_message_type</a></code>(3). </p>
<p> If it&#8217;s a packet message, the metadata and optional payload may be retrieved with <code><a href="/docs/linux/man/3-ipq_get_packet/">ipq_get_packet</a></code>(3). </p>
<p> To retrieve the value of an error message, use <code><a href="/docs/linux/man/3-ipq_get_msgerr/">ipq_get_msgerr</a></code>(3). </p>
<p> <code>Issuing Verdicts on Packets</code><br />
 To issue a verdict on a packet, and optionally return a modified version of the packet to the kernel, call <code><a href="/docs/linux/man/3-ipq_set_verdict/">ipq_set_verdict</a></code>(3). </p>
<p> <code>Error Handling</code><br />
 An error string corresponding to the current value of the internal error variable <code>ipq_errno</code> may be obtained with <code><a href="/docs/linux/man/3-ipq_errstr/">ipq_errstr</a></code>(3). </p>
<p> For simple applications, calling <code><a href="/docs/linux/man/3-ipq_perror/">ipq_perror</a></code>(3) will print the same message as <code><a href="/docs/linux/man/3-ipq_errstr/">ipq_errstr</a></code>(3), as well as the string corresponding to the global <code>errno</code> value (if set) to stderr. </p>
<p> <code>Cleaning Up</code><br />
 To free up the Netlink socket and destroy resources associated with the context handle, call <code><a href="/docs/linux/man/3-ipq_destroy_handle/">ipq_destroy_handle</a></code>(3).</p>
<h2>SUMMARY</h2>
<dl>
<dt><code><a href="/docs/linux/man/3-ipq_create_handle/">ipq_create_handle</a></code>(3)</p>
<dd> Initialise library, return context handle.</p>
<dt><code><a href="/docs/linux/man/3-ipq_set_mode/">ipq_set_mode</a></code>(3)</p>
<dd> Set the queue mode, to copy either packet metadata, or payloads as well as metadata to userspace.</p>
<dt><code><a href="/docs/linux/man/3-ipq_read/">ipq_read</a></code>(3)</p>
<dd> Wait for a queue message to arrive from ip_queue and read it into a buffer.</p>
<dt><code><a href="/docs/linux/man/3-ipq_message_type/">ipq_message_type</a></code>(3)</p>
<dd> Determine message type in the buffer.</p>
<dt><code><a href="/docs/linux/man/3-ipq_get_packet/">ipq_get_packet</a></code>(3)</p>
<dd> Retrieve a packet message from the buffer.</p>
<dt><code><a href="/docs/linux/man/3-ipq_get_msgerr/">ipq_get_msgerr</a></code>(3)</p>
<dd> Retrieve an error message from the buffer.</p>
<dt><code><a href="/docs/linux/man/3-ipq_set_verdict/">ipq_set_verdict</a></code>(3)</p>
<dd> Set a verdict on a packet, optionally replacing its contents.</p>
<dt><code><a href="/docs/linux/man/3-ipq_errstr/">ipq_errstr</a></code>(3)</p>
<dd> Return an error message corresponding to the internal ipq_errno variable.</p>
<dt><code><a href="/docs/linux/man/3-ipq_perror/">ipq_perror</a></code>(3)</p>
<dd> Helper function to print error messages to stderr.</p>
<dt><code><a href="/docs/linux/man/3-ipq_destroy_handle/">ipq_destroy_handle</a></code>(3)</p>
<dd> Destroy context handle and associated resources.</dl>
<h2>EXAMPLE</h2>
<p> The following is an example of a simple application which receives packets and issues NF_ACCEPT verdicts on each packet.</p>
<dl>
<dt>
<dd>
<pre><code>
/*
 * This code is GPL.
 */
#include &lt;libipq.h&gt;
#include &lt;linux/netfilter.h&gt;
#include &lt;stdio.h&gt;
#define BUFSIZE 2048
static void die(struct ipq_handle *h)
{
    ipq_perror("passer");
    ipq_destroy_handle(h);
    exit(1);
}
int main(int argc, char **argv)
{
    int status;
    unsigned char buf[BUFSIZE];
    struct ipq_handle *h;

    h = ipq_create_handle(0, NFPROTO_IPV4);
    if (!h)
        die(h);

    status = ipq_set_mode(h, IPQ_COPY_PACKET, BUFSIZE);
    if (status &lt; 0)
        die(h);

    do {
        status = ipq_read(h, buf, BUFSIZE, 0);
        if (status &lt; 0)
            die(h);

        switch (ipq_message_type(buf)) {
        case NLMSG_ERROR:
            fprintf(stderr, "Received error message %d
",
                    ipq_get_msgerr(buf));
            break;

        case IPQM_PACKET: {
            ipq_packet_msg_t *m = ipq_get_packet(buf);

            status = ipq_set_verdict(h, m-&gt;packet_id,
                                     NF_ACCEPT, 0, NULL);
            if (status &lt; 0)
                die(h);
            break;
        }

        default:
            fprintf(stderr, "Unknown message type!
");
            break;
        }
    } while (1);

    ipq_destroy_handle(h);
    return 0;
}
</code></pre>
<p> Pointers to more libipq application examples may be found in The Netfilter FAQ.</p>
<h2>DIAGNOSTICS</h2>
<p> For information about monitoring and tuning ip_queue, refer to the Linux 2.4 Packet Filtering HOWTO. </p>
<p> If an application modifies a packet, it needs to also update any checksums for the packet. Typically, the kernel will silently discard modified packets with invalid checksums.</p>
<h2>SECURITY</h2>
<p> Processes require CAP_NET_ADMIN capabilty to access the kernel ip_queue module. Such processes can potentially access and modify any IP packets received, generated or forwarded by the kernel.</p>
<h2>TODO</h2>
<p> Per-handle <code>ipq_errno</code> values.</p>
<h2>BUGS</h2>
<p> Probably.</p>
<h2>AUTHOR</h2>
<p> James Morris &lt;jmorris [at] intercode.com.au&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2001 Netfilter Core Team. </p>
<p> Distributed under the GNU General Public License.</p>
<h2>CREDITS</h2>
<p> Joost Remijn implemented the <code>ipq_read</code> timeout feature, which appeared in the 1.2.4 release of iptables. </p>
<p> Fernando Anton added support for IPv6.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/3-ipq_create_handle/">ipq_create_handle</a></code>(3), <code><a href="/docs/linux/man/3-ipq_destroy_handle/">ipq_destroy_handle</a></code>(3), <code><a href="/docs/linux/man/3-ipq_errstr/">ipq_errstr</a></code>(3), <code><a href="/docs/linux/man/3-ipq_get_msgerr/">ipq_get_msgerr</a></code>(3), <code><a href="/docs/linux/man/3-ipq_get_packet/">ipq_get_packet</a></code>(3), <code><a href="/docs/linux/man/3-ipq_message_type/">ipq_message_type</a></code>(3), <code><a href="/docs/linux/man/3-ipq_perror/">ipq_perror</a></code>(3), <code><a href="/docs/linux/man/3-ipq_read/">ipq_read</a></code>(3), <code><a href="/docs/linux/man/3-ipq_set_mode/">ipq_set_mode</a></code>(3), <code><a href="/docs/linux/man/3-ipq_set_verdict/">ipq_set_verdict</a></code>(3). </p>
<p> The Netfilter home page at <a rel="nofollow" href="http://netfilter.samba.org/">http://netfilter.samba.org/</a> which has links to The Networking Concepts HOWTO, The Linux 2.4 Packet Filtering HOWTO, The Linux 2.4 NAT HOWTO, The Netfilter Hacking HOWTO, The Netfilter FAQ and many other useful resources. </p>
<h2>Index</h2>
