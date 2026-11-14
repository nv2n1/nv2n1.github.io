---
title: "libnet10(3)"
name: "libnet10"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnet10/"
description: "libnet – \"libpwrite\" Network Routine Library"
---

<h2>NAME</h2>
<p> libnet &#8211; &quot;libpwrite&quot; Network Routine Library </p>
<h2>DESCRIPTION</h2>
<p> The Network Library provides a simple API for commonly used low-level network functions (mainly packet injection). Using libnet, it is easy to build and write arbitrary network packets. It provides a portable framework for low-level network packet writing and handling (use libnet in conjunction with libpcap and you can write some really cool stuff). Libnet includes packet creation at the IP layer and at the link layer as well as a host of supplementary and complementary functionality. </p>
<p> For a much more verbose treatment of libnet, including verbosely commented examples, please see the online web-based documentation at <a rel="nofollow" href="http://www.packetfactory.net/libnet/manual/.">http://www.packetfactory.net/libnet/manual/.</a> </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libnet.h&gt;

PACKET MEMORY MANAGEMENT ROUTINES int libnet_init_packet(size_t p_size, u_char **buf);
int libnet_destroy_packet(u_char **buf);
int libnet_init_packet_arena(struct libnet_arena **arena, int p_size,

                             &amp;nbsp;
                             &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short p_num);

u_char *libnet_next_packet_from_arena(struct libnet_arena **arena,

                                      &amp;nbsp;
                                      &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int p_size);
int libnet_destroy_packet_arena(struct libnet_arena **arena);

ADDRESS RESOLUTION ROUTINES
    u_char *
    libnet_host_lookup(u_long in, u_short use_name);
void libnet_host_lookup_r(u_long in, u_short use_name, u_char *buf);
u_long libnet_name_resolve(u_char *hostname, u_short use_name);
u_long libnet_get_ipaddr(struct libnet_link_int *l, const u_char *device,

                         &amp;nbsp;
                         &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *buf);
struct ether_addr *libnet_get_hwaddr(struct libnet_link_int *l,

                                     &amp;nbsp;
                                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *device, const u_char *buf);
PACKET INJECTION FRAMEWORK ROUTINES int libnet_open_raw_sock(int protocol);
int libnet_close_raw_sock(int fd);
int libnet_select_device(struct sockaddr_in *sin, u_char **device,

                         &amp;nbsp;
                         &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * ebuf);
struct libnet_link_int *libnet_open_link_interface(char *device, char *ebuf);
int libnet_close_link_interface(struct libnet_link_int *l);
int libnet_write_ip(int sock, u_char *packet, int len);
int libnet_write_link_layer(struct libnet_link_int *l, const u_char *device,

                            &amp;nbsp;
                            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf, int len);
int libnet_do_checksum(u_char *buf, int protocol, int len);
u_short libnet_ip_check(u_short *buf, int len);
PACKET BUILDER ROUTINES int libnet_build_arp(u_short hrd, u_short pro, u_short hln, u_short pln,

                                             &amp;nbsp;
                                             &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short op, u_char *sha, u_char *spa, u_char *tha,

                                                                                              &amp;nbsp;
                                             &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * tpa, const u_char *payload, int payload_s,

                                                                                              &amp;nbsp;
                                             &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_dns(u_short id, u_short flags, u_short num_q,

                     &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short num_anws_rr, u_short num_auth_rr,

                                                                      &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short num_addi_rr, const u_char *payload, int payload_s,

                                                                      &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_ethernet(u_char *daddr, u_char *saddr, u_short id,

                          &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_build_icmp_echo(u_char type, u_char code, u_short id,

                           &amp;nbsp;
                           &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short seq, const u_char *payload, int payload_s,

                                                                            &amp;nbsp;
                           &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_icmp_mask(u_char type, u_char code, u_short id,

                           &amp;nbsp;
                           &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short seq, u_long mask, const u_char *payload,

                                                                            &amp;nbsp;
                           &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int payload_s, u_char *buf);
int libnet_build_icmp_unreach(u_char type, u_char code,

                              &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short orig_len, u_char orig_tos, u_short orig_id,

                                                                               &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short orig_frag, u_char orig_ttl, u_char orig_prot,

                                                                               &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long orig_src, u_long orig_dst, const u_char *orig_payload,

                                                                               &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int payload_s, u_char *buf);
int libnet_build_icmp_timeexceed(u_char type, u_char code,

                                 &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short orig_len, u_char orig_tos, u_short orig_id,

                                                                                  &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short orig_frag, u_char orig_ttl, u_char orig_prot,

                                                                                  &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long orig_src, u_long orig_dst, const u_char *orig_payload,

                                                                                  &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int payload_s, u_char *buf);
int libnet_build_icmp_redirect(u_char type, u_char code, u_long gateway

                                                             &amp;nbsp;
                               &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short orig_len, u_char orig_tos, u_short orig_id,

                                                                                &amp;nbsp;
                               &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short orig_frag, u_char orig_ttl, u_char orig_prot,

                                                                                &amp;nbsp;
                               &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long orig_src, u_long orig_dst, const u_char *orig_payload,

                                                                                &amp;nbsp;
                               &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int payload_s, u_char *buf);
int libnet_build_icmp_timestamp(u_char type, u_char code, u_short id,

                                &amp;nbsp;
                                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short seq, n_time otime, n_time rtime, n_time ttime,

                                                                                 &amp;nbsp;
                                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_build_igmp(u_char type, u_char code, u_long ip,

                      &amp;nbsp;
                      &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_build_ip(u_short len, u_char tos, u_short id, u_short frag,

                    &amp;nbsp;
                    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char ttl, u_char prot, u_long saddr, u_long daddr,

                                                                     &amp;nbsp;
                    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_build_ospf(u_short len, u_char type, u_long router_id,

                      &amp;nbsp;
                      &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long area_id, u_short auth_type, const char *payload,

                                                                       &amp;nbsp;
                      &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int payload_s, u_char *buf);
int libnet_build_ospf_hello(u_long netmask, u_short interval,

                            &amp;nbsp;
                            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char options, u_char priority, u_int dead_interval,

                                                                             &amp;nbsp;
                            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long des_router, u_long backup, u_long neighbor,

                                                                             &amp;nbsp;
                            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char *payload, int payload_s, u_char *buf);
int libnet_build_ospf_dbd(u_short len, u_char options, u_char type,

                          &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_int sequence_num, const char *payload, int payload_s,

                                                                           &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_ospf_lsr(u_int type, u_int ls_id, u_long adv_router,

                          &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char *payload, int payload_s, u_char *buf);
int libnet_build_ospf_lsu(u_int num, const char *payload, int payload_s,

                          &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_ospf_lsa(u_short age, u_char options, u_char type,

                          &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_int ls_id, u_long adv_router, u_int sequence_num,

                                                                           &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short len, const char *payload, int payload_s,

                                                                           &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_ospf_lsa_rtr(u_short flags, u_short num, u_int id,

                              &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_int data, u_char type, u_char tos, u_short metric,

                                                                               &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char *payload, int payload_s, u_char *buf);
int libnet_build_ospf_lsa_net(u_long netmask, u_int router_id,

                              &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char *payload, int payload_s, u_char *buf);
int libnet_build_ospf_lsa_sum(u_long netmask, u_int metric, u_int tos,

                              &amp;nbsp;
                              &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char *payload, int payload_s, u_char *buf);
int libnet_build_ospf_lsa_as(u_long netmask, u_int metric,

                             &amp;nbsp;
                             &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long fwd_addr, u_int tag, const char *payload,

                                                                              &amp;nbsp;
                             &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int payload_s, u_char *buf);
int libnet_build_rip(u_char command, u_char ver, u_short rd, u_short af,

                     &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short rt, u_long addr, u_long mask, u_long next_hop,

                                                                      &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long metric, const u_char *payload, int payload_s,

                                                                      &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
int libnet_build_tcp(u_short sport, u_short dport, u_long seq,

                     &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long ack, u_char control, u_short win, u_short urg,

                                                                      &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_build_udp(u_short sport, u_short dport,

                     &amp;nbsp;
                     &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_build_vrrp(u_char vrouter_id, u_char priority,

                      &amp;nbsp;
                      &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char ip_count, u_char auth_type, u_char advert_int,

                                                                       &amp;nbsp;
                      &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const u_char *payload, int payload_s, u_char *buf);
int libnet_insert_ipo(struct ipoption *opt, u_char opt_len, u_char *buf);
int libnet_insert_tcpo(struct tcpoption *opt, u_char opt_len,

                       &amp;nbsp;
                       &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * buf);
MISCELLANEOUS SUPPORT ROUTINES int libnet_seed_prand();
u_long libnet_get_prand(int type);
void libnet_hex_dump(u_char *buf, int len, int swap, FILE *stream);
int libnet_plist_chain_new(struct libnet_plist_chain **head,

                           &amp;nbsp;
                           &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; char *tok_list);
int libnet_plist_chain_next_pair(struct libnet_plist_chain *p,

                                 &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_short * bport, u_short *eport);
int libnet_plist_chain_dump(struct libnet_plist_chain *p);
u_char *libnet_plist_chain_dump_string(struct libnet_plist_chain *p);
int libnet_plist_chain_free(struct libnet_plist_chain *p);
void libnet_error(int severity, char *msg, ...);
ASN .1 BER ROUTINES
    u_char *
    libnet_build_asn1_int(u_char *data, int *datalen, u_char type,

                          &amp;nbsp;
                          &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; long *int_p, int int_s);
u_char *libnet_build_asn1_uint(u_char *data, int *datalen, u_char type,

                               &amp;nbsp;
                               &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char * int_p, int int_s);
u_char *libnet_build_asn1_string(u_char *data, int *datalen, u_char type,

                                 &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_long * string, int str_s);
u_char *libnet_build_asn1_header(u_char *data, int *datalen, u_char type,

                                 &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int len);
u_char *libnet_build_asn1_length(u_char *data, int *datalen, int len);
u_char *libnet_build_asn1_sequence(u_char *data, int *datalen,

                                   &amp;nbsp;
                                   &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char type, int len);
u_char *libnet_build_asn1_objid(u_char *data, int *datalen, u_char type,

                                &amp;nbsp;
                                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; oid * objid, int oid_s);
u_char *libnet_build_asn1_null(u_char *data, int *datalen, u_char type);
u_char *libnet_build_asn1_bitstring(u_char *data, int *datalen,

                                    &amp;nbsp;
                                    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; u_char type, u_long *string, int str_s);
</code></pre>
<h2>ADDRESS RESOLUTION ROUTINES</h2>
<p> <code>libnet_host_lookup()</code> converts the supplied network-ordered (big-endian) IPv4 address into its human-readable coutnerpart. If use_name is 1, <code>libnet_host_lookup()</code> will attempt to resolve this IP address and return a hostname, otherwise (or if the lookup fails), the function returns a dotted-decimal ASCII string. This function is hopelessly non re-entrant as it uses static data. Users concerned with re-entrancy should use <code>libnet_host_lookup_r()</code>. </p>
<p> <code>libnet_host_lookup_r()</code> is the (planned) reentrant version of the above function. As soon as reentrant network resolver libraries become available this function will likewise be reentrant. An additional argument of a buffer to store the converted (or resolved) IPv4 address is supplied by the user. </p>
<p> <code>libnet_name_resolve()</code> takes a NULL terminated ASCII string representation of an IPv4 address (dots and decimals or canonical hostname if use_name is 1) and converts it into a network-ordered (big-endian) 4-byte value. </p>
<p> <code>libnet_get_ipaddr()</code> takes a pointer to a link layer interface struct, a pointer to the network device name, and an empty buffer to be used in case of error. Upon success the function returns the IP address of the specified interface in host-byte order or 0 upon error (and errbuf will contain a reason). </p>
<p> <code>libnet_get_hwaddr()</code> takes a pointer to a link layer interface struct, a pointer to the network device name, and an empty buffer to be used in case of error. The function returns the MAC address of the specified interface upon success or 0 upon error (and errbuf will contain a reason). </p>
<h2>PACKET MEMORY MANAGEMENT ROUTINES</h2>
<p> <code>libnet_init_packet()</code> initializes a packet for use. If the size parameter is omitted (or negative) the library will pick a reasonable value for the user (currently LIBNET_MAX_PACKET). If the memory allocation is successful, the memory is zeroed and the function returns 1. If there is an error, the function returns -1. Since this function calls malloc, you certainly should, at some point, make a corresponding call to destroy_packet(). </p>
<p> <code>libnet_destroy_packet()</code> frees the memory associated with the packet. </p>
<p> <code>libnet_init_packet_arena()</code> allocates and initializes a memory pool. If you plan on building and sending several different packets, this is a good choice. It allocates a pool of memory from which you can grab chunks to build packets (see next_packet_from_arena() below). It takes the address to an arena structure pointer (so it can modify the structure elements), and hints on the possible packet size and number of packets. The last two arguments are used to compute the size of the memory pool. The function returns -1 if the malloc fails or 1 if everything goes ok. </p>
<p> <code>libnet_next_packet_from_arena()</code> returns a chunk of memory from the arena of the requested size pool and decrements the available byte counter. If the requested memory is not available from the arena, it returns NULL. Note that there is nothing preventing a poorly coded application from using more memory than requested and causing all kinds of problems. Take heed. </p>
<p> <code>libnet_destroy_packet_arena()</code> frees the memory associated with the arena. </p>
<p> During packet or arena initilization and utilization, if 0 is passed for either of size values, the functions make a best guest. If 0 is passed for the packet size, it adjusts it to be LIBNET_MAX_PACKET, and if 0 is passed for the packet number (in the case of libnet_init_packet_arena) it adjusts it to be 3. Be aware that this is 196605 bytes of memory. </p>
<p> The number of bytes allocated may actually be slightly more than requested due to alignment constraints (values are aligned on a 4-byte boundry). </p>
<p> For the above three functions, it is a checked runtime error for arena to be a NULL pointer. </p>
<p> The arena interface also includes LIBNET_GET_ARENA_SIZE which returns the total size of an arena and LIBNET_GET_ARENA_REMAINING_BYTES which returns the remaining bytes of usable memory from an arena. </p>
<h2>PACKET INJECTION FRAMEWORK ROUTINES</h2>
<p> <code>libnet_open_raw_sock()</code> opens a raw IPv4 socket of the supplied protocol type and sets the IP_HDRINCL socket option. Returned is the socket file descriptor or -1 on error. </p>
<p> <code>libnet_close_raw_sock()</code> closes an opened raw socket. Returned is 1 upon success or -1 on error. </p>
<p> <code>libnet_select_device()</code> will run through the list of interfaces and select one for use (ignoring the loopback device). If device points to NULL, (don&#8217;t pass in a NULL pointer, the function expects a pointer to a pointer, and C can&#8217;t derefence a NULL pointer) it will try to fill it in with the first non-loopback device it finds, otherwise, it will try to open the specified device. If successful, 1 is returned (and if device was NULL, it will now contain the device name which can be used in libnet_*link*() type calls). If an error occurs, -1 is returned and errbuf will contain a reason. The errbuf should contain a pointer to a buffer at least as large as LIBNET_ERR_BUF. </p>
<p> <code>libnet_open_link_interface()</code> opens a low-level packet interface. This is required to write link layer frames. Supplied is a u_char pointer to the interface device name and a u_char pointer to an error buffer. Returned is a filled in libnet_link_int struct or NULL on error. </p>
<p> <code>libnet_close_link_interface()</code> closes an opened low-level packet interface. Returned is 1 upon success or -1 on error. </p>
<p> <code>libnet_write_ip()</code> writes an IP packet to the network. The first argument is the socket created with <code>libnet_open_raw_sock()</code>, the second is a pointer to a buffer containing a complete IP datagram, and the third argument is the total packet size. It returns the number of bytes written. </p>
<p> <code>libnet_write_link_layer()</code> writes an link-layer frame to the network. The first argument is a pointer to a filled in libnet_link_int structure, the next is a pointer to the network device, the next is the raw packet and the last is the packet size. Returned is the number of bytes written or -1 on error. </p>
<p> <code>libnet_do_checksum()</code> calculates the checksum for the packet header. The first argument is a pointer to the constructed IPv4 packet buffer. The second is the transport protocol used and the third is the packet length (not including the IP header). The function calculates the checksum for the transport protocol and fills it in at the appropriate header location. This function should be called only after a complete packet has been built. Note that when using raw sockets the IP checksum is always computed by the kernel, but when using link layer interfaces, the IP checksum must be explicitly computed. The function returns 1 upon success or -1 if an error occurs. </p>
<h2>PACKET BUILDER ROUTINES</h2>
<p> For all of the build_* functions, it is a checked runtime error for buf to be a NULL pointer (the function will return -1), but an unchecked error for the optional payload or the packet header itself to exceed the allocated memory. Take heed. </p>
<p> <code>libnet_build_arp()</code> constructs an ARP (Address Resolution Protocol) packet. Supplied are the following: hardware addresss type, protocol address type, the hardware addess length, the protocol address length, the ARP packet type, the sender hardware address, the sender protocol address, the target hardware address, the target protocol address, the packet payload, the payload size, and finally, a pointer to the packet header memory. Note that this function only builds ethernet/IP ARP packets, and consequently the first value should be ARPHRD_ETHER. The ARP packet type should be one of the following: ARPOP_REQUEST, ARPOP_REPLY, ARPOP_REVREQUEST, ARPOP_REVREPLY, ARPOP_INVREQUEST, or ARPOP_INVREPLY. </p>
<p> <code>libnet_build_dns()</code> constructs a DNS (Domain Name Service) packet. Supplied are the following: DNS packet ID, flags, number of questions, number of answer resource records, number of authority resource records, number of additional resource records. All of the above are unsigned shorts. All of the `interesting` fields of the header are variable in content and length, and therefore have to be included at the programmer&#8217;s discretion. We use the standard libnet payload and payload size interface for this. Finally, please be sure to include a pointer to some preallocated memory. </p>
<p> <code>libnet_build_ethernet()</code> constructs an ethernet packet. Supplied is the destination address, source address (as arrays of unsigned character bytes) and the ethernet frame type, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The ethernet packet type should be one of the following: </p>
<p> Value Type </p>
<p> Please note that some low-level interfaces (bpf in particular) do not allow for the spoofing of ethernet addresses without kernel modification. </p>
<p> The following functions construct ICMP (Internet Control Message Protocol) packets. </p>
<p> <code>libnet_build_icmp_echo()</code> builds an ICMP_ECHO / ICMP_ECHOREPLY packet. Supplied is a byte for the packet type, a byte for the code, an unsigned short for the packet id, an unsigned short for the packet sequence number, and a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The type should be ICMP_ECHOREPLY or ICMP_ECHO and the code should be 0. </p>
<p> <code>libnet_build_icmp_mask()</code> builds an ICMP_MASKREQ / ICMP_MASKREPLY packet. Supplied is a byte for the packet type, a byte for the code, an unsigned short for the packet id, an unsigned short for the packet sequence number, a 32-bit subnet mask, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The type should be ICMP_MASKREQ or ICMP_MASKREPLY and the code should be 0. </p>
<p> <code>libnet_build_icmp_unreach()</code> builds an ICMP_UNREACH packet. Supplied is the normal ICMP stuff, a byte for the packet type and a byte for the code. Next come the values for the IP header that caused the error that necessitated the unreachable. The standard payload arguments to this function actually apply to the original IP packet and will be tacked on there. The type should be ICMP_UNREACH and the code should be one of the following 16 different unreachable codes: </p>
<p> Code Symbolic Name </p>
<p> <code>libnet_build_icmp_timeexceed()</code> builds an ICMP_TIMEXCEED packet. Supplied is the normal ICMP stuff, a byte for the packet type and a byte for the code. Next come the values for the IP header that caused the error that necessitated the unreachable. The standard payload arguments to this function actually apply to the original IP packet and will be tacked on there. The type should be ICMP_REDIRECT and the code should be ICMP_TIMXCEED_INTRANS or ICMP_TIMXCEED_REASS. </p>
<p> <code>libnet_build_icmp_redirect()</code> builds an ICMP_REDIRECT packet. Supplied is a byte for the packet type, a byte for the code, and the unsigned long IP address of the gateway that should be used. Next come the values for the IP header that caused the error that necessitated the redirect. The standard payload arguments to this function actually apply to the original IP packet and will be tacked on there. The type should be ICMP_REDIRECT and the code should be one of the following: </p>
<p> Code Symbolic Name </p>
<p> <code>libnet_build_icmp_timestamp()</code> builds an ICMP_TSTAMP / ICMP_TSTAMPREPLY packet. Supplied is a byte for the packet type, a byte for the code, an unsigned short for the packet id, an unsigned short for the packet sequence number, the three timestamp values, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The type should be ICMP_TSTAMP or ICMP_TSTAMPREPLY and the code should be 0. </p>
<p> <code>libnet_build_igmp()</code> builds an IGMP (Internet Group Membership Protocol) packet. Supplied is a byte for the packet type, a byte for the code, an unsigned long for the Class D address, and the other usual things. </p>
<p> <code>libnet_build_ip()</code> builds an IP (Internet Protocol) packet. Supplied is the packet length (not including the IP header), the IP tos bits, the IP ID, the fragmentation flags and offset, the packet TTL, the transport protocol, the source and destination IP addresses (in network-byte order), a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. To just build an IP header with no data payload, only IP_H bytes need to be allocated. The payload and payload size arguments should not be used to build any of the supported transport protocol-type packets; for these transports, the relevant functions should be used. The payload arguments should only be used to build an arbitrary IP packet with a payload. </p>
<h2>OSPF PACKET CREATION ROUTINES</h2>
<p> <code>libnet_build_ospf()</code> builds a OSPF (Open Shortest Path First) packet. You pass the packet length (not including the OSPF header), the packet type, 32-bit router ID, 32-bit area ID, the authentication type, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The payload should not be used to build the Hello, LSA, LSU, LSR, or DBD packets. The following variables are to be used for the OSPF packet type: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>OSPF_UMD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>UMd monitoring packet </p>
<p>&nbsp;<wbr>&nbsp;<wbr>OSPF_AUTH_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NULL password </p>
<p> The following is the structure used for the 64 bit field when using MD5: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>struct auth&nbsp;<wbr>{ </p>
<p> netmask for the interface, the number of seconds since the last packet was sent, possible options, the router&#8217;s priority (if 0, it can&#8217;t be a backup router), the time (in seconds) until a router is deemed down, the networks designated router, the networks backup router, a neighbor, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory used for the packet. If there are more than one neighbors that are to be included in the packet, just allocate enough space for the packet buf, and pass the neighbors as the &quot;optional data payload.&quot; </p>
<p> <code>libnet_build_ospf_dbd()</code> builds an OSPF DataBase Description (DBD) packet. You pass the maximum length of an IP packet the interface can use, packet options, the type of exchange occuring, a sequence number, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The following can be used for the type variable: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>DBD_IBIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Init bit </p>
<p> <code>libnet_build_ospf_lsr()</code> builds an OSPF Link State Request (LSR) packet. You pass the type of link state packet being requested, the link state ID, the advertising router, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. See the <code>libnet_build_ospf_lsa()</code> section for more information regarding variables. </p>
<p> <code>libnet_build_ospf_lsu()</code> builds an OSPF Link State Update (LSU) packet. You pass the number of Link State Acknowledgment (LSA) packets that will be in the packet, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. </p>
<p> <code>libnet_build_ospf_lsa()</code> builds an OSPF Link State Acknowledgement (LSA) packet. You pass the link state age, packet options, type of LSA, the link state ID, the advertising router, the packet&#8217;s sequence number, the length of the packet (_not_ including the LSA header length), a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The following variables can be used for the type of LSA: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>LS_TYPE_RTR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Router LSA </p>
<p> <code>libnet_build_ospf_lsa_rtr()</code> builds an OSPF Link State Router packet. You pass the optional packet flags, the number of links within that packet, the link ID (helps describe the next variable), the info for the specified link ID, the type of router link, the number of TOS metrics for this link, the metric (the cost of using the link), a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. The possible flags (not including 0x00) are as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>RTR_FLAGS_W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>W bit </p>
<p> The possible values for the router type are as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>RTR_TYPE_PTP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Point-to-point </p>
<p> You pass the interface&#8217;s netmask, the router ID, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. </p>
<p> <code>libnet_build_ospf_lsa_sum()</code> builds an OSPF Link State Summary packet. You pass the interface&#8217;s netmask, the cost of using the link (metric), the TOS and metric, which is passed as a unsigned integer but the first 8 bits are the TOS and the last 24 bits are the TOS metric, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. </p>
<p> <code>libnet_buils_ospf_lsa_as()</code> builds an OSPF Link State AS External packet. You pass the interface&#8217;s netmask, the cost of using the link (metric), the forwarding address, the external route tag, a pointer to an optional data payload, the payload length, and a pointer to a pre-allocated block of memory for the packet. In reality, the metric only uses the last 24 bits of the unsigned int. The first 8bits are reserved for a possible bit to be set (the E bit, see above for more info). The variable AS_E_BIT_ON can be used logically to set the E bit on. </p>
<h2>OSPF MACROS</h2>
<p> <code>LIBNET_OSPF_AUTHCPY()</code> simply copies, byte for byte, your authentication buf to the pre-allocated block of memory for your packet. </p>
<h2>OSPF FUNCTION VARIABLES</h2>
<p> Random variables: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>IPPROTO_OSPF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>89 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>OSPF_H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OSPF header </p>
<p>&nbsp;<wbr>&nbsp;<wbr>OPT_EBIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>AS-external-LSAs are flooded </p>
<p> <code>libnet_build_rip()</code> constructs a RIP (Routing Information Protocol) packet. The values supplied depend on the version of the RIP packet you desire to build. The following table applies: </p>
<p> Passing Order Datatype RIP v1 RIPv2 </p>
<p> The command should be one of the following: RIPCMD_REQUEST, RIPCMD_RESPONSE, RIPCMD_TRACEON, RIPCMD_TRACEOFF, RIPCMD_POLL, RIPCMD_POLLENTRY, or RIPCMD_MAX. The version should be RIPVER_1 or RIPVER_2. </p>
<p> <code>libnet_build_tcp()</code> builds a TCP (Transmission Control Protocol) packet. Supplied is the source port, destination port, the sequence and acknowledgement numbers, the control bits (which can be logically OR&#8217;d together to set multiple flags &#8212; see the example below), the advertised window size, the urgent pointer, a pointer to an optional data payload, the payload size, and lastly, the pointer to a pre-allocated block of memory for the packet. To just build a TCP header with no data payload, only TCP_H bytes need be allocated. </p>
<p> <code>libnet_build_udp()</code> builds a UDP (User Datagram Protocol) packet. Supplied is the source port, the destination port, a pointer to an optional data payload, the payload size, and lastly, a pointer to a pre-allocated block of memory for the packet. To just build a UDP header with no data payload, only UDP_H bytes need to be allocated. </p>
<p> <code>libnet_vuild_vrrp()</code> builds a VRRP (Virtual Router Redundancy Protocol) packet. Supplied is the virtual router ID, the priority, the number of IP addresses in the packet, the authorization type (LIBNET_VRRP_AUTH_NONE, LIBNET_VRRP_AUTH_PASSWD, or LIBNET_VRRP_AUTH_IPAH), the adverstisment interval, a pointer to an optional data payload, the payload size, and lastly, a pointer to a pre-allocated block of memory for the packet. </p>
<p> <code>libnet_insert_ipo()</code> inserts IP options into an already created IP packet. Supplied is a pointer to an ip option struct (which must be filled in by the user), the size of the options list, and a pointer the completed packet. The function returns -1 if the options would make the packet too large (greater then 65535 bytes) or 1 otherwise. It is an unchecked runtime error for the user to have not allocated enough heap memory for the packet + options. </p>
<p> <code>libnet_insert_tcpo()</code> inserts TCP options into an already created IP packet. Replace the pointer to an IP option struct with one to a TCP option struct and this function is exactly the same as above. </p>
<h2>MISCELLANEOUS SUPPORT ROUTINES</h2>
<p> <code>libnet_seed_prand()</code> seeds the psuedorandom number generator. Returns 1 on success, -1 on failure. </p>
<p> <code>libnet_get_prand()</code> returns a positive psuedorandom integer of the specified type. Expects type to be one of five symbolics PR2, PR8, PR16, PRu16, PR32 or PRu32. PR2 returns a one or a zero, PR8 returns a byte, PR16 returns up to a signed short (from 0 to 32767), PRu16 returns an unsigned short (from 0 to 65535), PR32 returns a signed long (from 0 to 2147483647) and PRu32 returns an unsigned long number (from 0 to 4294967295). </p>
<p> <code>libnet_hex_dump()</code> prints a packet out in hex. Supplied is the packet and its length, a swap flag, and a pointer to a previously opened stream. The swap flag (1 or 0) specifies whether or not to print the packet as it appears in memory (0) or to swap the bytes into host order (1). </p>
<p> <code>libnet_plist_chain_new()</code> builds a new libnet port list chain. A libnet port list chain is a fast and simple way of implementing port list ranges (useful for applications that employ a list of ports like a port scanner). You&#8217;ll see naive implementations that allocate an entire array of 65535 bytes and fill in the desired ports one by one. However, we only really need to store the beginning port and the ending port, and we can efficiently store multiple port ranges (delimated by commas) by using a linked list chain with each node holding the beginning and ending port for a particular range. For example, The port range `1-1024` would occupy one node with the bport being 1 and the eport being 1024. The port range `25,110-161,6000` would result in 3 nodes being allocated. Single ports are taken as single ranges (port 25 ends up being 25-25). A port list range without a terminating port (port_num &#8211; ) is considered shorthand for (port_num &#8211; 65535). The arguments are a pointer to libnet_plist_chain pointer (which will end up being the head of the linked list) and pointer to the port list itself. The function checks this character port list for valid tokens (1234567890,- ) and returns an error if an unrecognized token is found. Upon success the function returns 1, and head points to the newly formed port list (and also contains the number of nodes in the list. If an error occurs (an unrecognized token is found or malloc fails) -1 is returned and head is set to NULL. libnet_plist_chain_next_pair() should be used to extract port list pairs. </p>
<p> <code>libnet_plist_chain_next_pair()</code> fetchs the next pair of ports from the list. The function takes a pointer to the head of the prebuilt list and a pointer to a u_short that will contain the beginning port and a pointer to a u_short that will contain the ending port. The function returns 1 and fills in these values if there are nodes remaining, or if the port list chain is exhausted, it returns 0. </p>
<p> <code>libnet_plist_chain_dump()</code> prints the list (as lists of integers). </p>
<p> <code>libnet_plist_chain_dump_string()</code> returns a string containing the port list chain. </p>
<p> <code>libnet_plist_chain_free()</code> frees the entire list. </p>
<p> <code>libnet_error()</code> dumps an error message to stderr. Included is the severity of the message (LIBNET_ERR_WARNING, LIBNET_ERR_CRITICAL, or LIBNET_ERR_FATAL) and the message string itself. If the severity is LIBNET_ERR_FATAL, the function will exit the program. This is the only defined exit point in the whole library. </p>
<h2>ASN.1 BER ROUTINES</h2>
<p> <code>libnet_build_asn1_int()</code> </p>
<p> <code>libnet_build_asn1_uint()</code> </p>
<p> <code>libnet_build_asn1_string()</code> </p>
<p> <code>libnet_build_asn1_header()</code> </p>
<p> <code>libnet_build_asn1_length()</code> </p>
<p> <code>libnet_build_asn1_sequence()</code> </p>
<p> <code>libnet_build_asn1_objid()</code> </p>
<p> <code>libnet_build_asn1_null()</code> </p>
<p> <code>libnet_build_asn1_bitstring()</code> </p>
<h2>SYMBOLIC CONSTANTS</h2>
<p> To make your life and code cleaner, libnet defines symbolic constants to make your life easier. </p>
<p> Default packet header sizes: </p>
<p> Standard memory sizes for packets: </p>
<p> Other constants you should know about: </p>
<p> IP Type Of Service constants: </p>
<p> IP Fragmentation flags: </p>
<p> TCP control bits: </p>
<h2>COMPLIATION USING THE CONFIGURE SCRIPT</h2>
<p> To properly compile your applications under libnet, you should use the `libnet-config` script. This script is created during the GNU configure process will ensure that future compilations linked against libnet contain the correct CPP and CFLAG options as well as additional libraries for the targeted architecture. To invoke it simply: </p>
<p>&nbsp;<wbr>gcc&nbsp;<wbr>`libnet-config &#8211;defines &#8211;cflags`&nbsp;<wbr>foo.c -o foo&nbsp;<wbr>`libnet-config &#8211;libs` </p>
<p> The script handles all libnet dependencies and concessions for the architecture it was compiled on. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-pcap/">pcap</a>(3), <a href="/docs/linux/man/4-bpf/">bpf</a>(4), <a href="//www.systutorials.com/docs/linux/man/7P-dlpi/">dlpi</a>(7P)</p>
<h2>AUTHOR</h2>
<p> Mike D. Schiffman &lt;mike [at] infonexus.com&gt; See the online web reference manual for additional contributers. </p>
<p> The current version is always available: </p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://www.packetfactory.net/libnet">http://www.packetfactory.net/libnet</a></i></dl>
<h2>BUGS</h2>
<p> Solaris raw sockets are cooked. They do not allow one to set the ip_len, ip_frag or the ip_id (including IP options at the raw socket layer doesn&#8217;t work either). To work around this, use the link-layer API instead of raw socket functions. </p>
<p> The Berkeley Packet Filter alone does not allow for the arbitrary specification of source ethernet addresses. This is not so much a bug as an oversight in the protocol. Included with the distribution is lkm code to work around this (FreeBSD has support for an ioctl that works around this). </p>
<p> The OSPF functionality has not been extensively tested as yet and is considered to be in beta release. </p>
<p> Please send bug reports to mike [at] infonexus.com. </p>
<h2>Index</h2>
