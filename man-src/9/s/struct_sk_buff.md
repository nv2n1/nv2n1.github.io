---
title: "struct_sk_buff(9)"
name: "struct_sk_buff"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_sk_buff/"
---

struct_sk_buff - socket buffer

<h2>Synopsis</h2>

<pre><code>struct sk_buff {
    union {
        unnamed_union
    };
    __u16 inner_transport_header;
    __u16 inner_network_header;
    __u16 inner_mac_header;
    __be16 protocol;
    __u16 transport_header;
    __u16 network_header;
    __u16 mac_header;
    sk_buff_data_t tail;
    sk_buff_data_t end;
    unsigned char *head;
    unsigned char *data;
    unsigned int truesize;
    atomic_t users;
};</code></pre>

<h2>Members</h2>

{unnamed_union}
<dl><dd>anonymous</dl>
 

 inner_transport_header
<dl><dd>Inner transport layer header (encapsulation)</dl>
 

 inner_network_header
<dl><dd>Network layer header (encapsulation)</dl>
 

 inner_mac_header
<dl><dd>Link layer header (encapsulation)</dl>
 

 protocol
<dl><dd>Packet protocol from driver</dl>
 

 transport_header
<dl><dd>Transport layer header</dl>
 

 network_header
<dl><dd>Network layer header</dl>
 

 mac_header
<dl><dd>Link layer header</dl>
 

 tail
<dl><dd>Tail pointer</dl>
 

 end
<dl><dd>End pointer</dl>
 

 head
<dl><dd>Head of buffer</dl>
 

 data
<dl><dd>Data head pointer</dl>
 

 truesize
<dl><dd>Buffer size</dl>
 

 users
<dl><dd>User count - see {datagram,tcp}.c</dl>

<h2>Copyright</h2>


