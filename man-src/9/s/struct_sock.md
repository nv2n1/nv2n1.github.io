---
title: "struct_sock(9)"
name: "struct_sock"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_sock/"
description: "struct_sock – network layer representation of sockets"
---

<p>struct_sock &#8211; network layer representation of sockets</p>
<h2>Synopsis</h2>
<pre><code>struct sock {
    struct sock_common __sk_common;
#define sk_node __sk_common.skc_node
#define sk_nulls_node __sk_common.skc_nulls_node
#define sk_refcnt __sk_common.skc_refcnt
#define sk_tx_queue_mapping __sk_common.skc_tx_queue_mapping
#define sk_dontcopy_begin __sk_common.skc_dontcopy_begin
#define sk_dontcopy_end __sk_common.skc_dontcopy_end
#define sk_hash __sk_common.skc_hash
#define sk_portpair __sk_common.skc_portpair
#define sk_num __sk_common.skc_num
#define sk_dport __sk_common.skc_dport
#define sk_addrpair __sk_common.skc_addrpair
#define sk_daddr __sk_common.skc_daddr
#define sk_rcv_saddr __sk_common.skc_rcv_saddr
#define sk_family __sk_common.skc_family
#define sk_state __sk_common.skc_state
#define sk_reuse __sk_common.skc_reuse
#define sk_reuseport __sk_common.skc_reuseport
#define sk_ipv6only __sk_common.skc_ipv6only
#define sk_net_refcnt __sk_common.skc_net_refcnt
#define sk_bound_dev_if __sk_common.skc_bound_dev_if
#define sk_bind_node __sk_common.skc_bind_node
#define sk_prot __sk_common.skc_prot
#define sk_net __sk_common.skc_net
#define sk_v6_daddr __sk_common.skc_v6_daddr
#define sk_v6_rcv_saddr __sk_common.skc_v6_rcv_saddr
#define sk_cookie __sk_common.skc_cookie
#define sk_incoming_cpu __sk_common.skc_incoming_cpu
#define sk_flags __sk_common.skc_flags
#define sk_rxhash __sk_common.skc_rxhash
    socket_lock_t sk_lock;
    struct sk_buff_head sk_receive_queue;
    struct {
        unnamed_struct
    };
#ifdef CONFIG_XFRM
    struct xfrm_policy __rcu *sk_policy[2];
#endif
    struct dst_entry *sk_rx_dst;
    struct dst_entry __rcu *sk_dst_cache;
    atomic_t sk_wmem_alloc;
    atomic_t sk_omem_alloc;
    int sk_sndbuf;
    struct sk_buff_head sk_write_queue;
    unsigned int sk_padding : 2;
    unsigned int sk_no_check_tx : 1;
    unsigned int sk_no_check_rx : 1;
    unsigned int sk_userlocks : 4;
    unsigned int sk_protocol : 8;
    unsigned int sk_type : 16;
#define SK_PROTOCOL_MAX U8_MAX
    int sk_wmem_queued;
    gfp_t sk_allocation;
    u32 sk_pacing_rate;
    u32 sk_max_pacing_rate;
    netdev_features_t sk_route_caps;
    netdev_features_t sk_route_nocaps;
    int sk_gso_type;
    unsigned int sk_gso_max_size;
    u16 sk_gso_max_segs;
    int sk_rcvlowat;
    unsigned long sk_lingertime;
    struct sk_buff_head sk_error_queue;
    struct proto *sk_prot_creator;
    rwlock_t sk_callback_lock;
    int sk_err;
    int sk_err_soft;
    u32 sk_ack_backlog;
    u32 sk_max_ack_backlog;
    __u32 sk_priority;
    __u32 sk_mark;
    struct pid *sk_peer_pid;
    const struct cred *sk_peer_cred;
    long sk_rcvtimeo;
    long sk_sndtimeo;
    struct timer_list sk_timer;
    ktime_t sk_stamp;
    u16 sk_tsflags;
    u8 sk_shutdown;
    u32 sk_tskey;
    struct socket *sk_socket;
    void *sk_user_data;
    struct page_frag sk_frag;
    struct sk_buff *sk_send_head;
    __s32 sk_peek_off;
    int sk_write_pending;
#ifdef CONFIG_SECURITY
    void *sk_security;
#endif
    struct sock_cgroup_data sk_cgrp_data;
    struct mem_cgroup *sk_memcg;
    void (*sk_state_change)(struct sock *sk);
    void (*sk_data_ready)(struct sock *sk);
    void (*sk_write_space)(struct sock *sk);
    void (*sk_error_report)(struct sock *sk);
    int (*sk_backlog_rcv)(struct sock *sk, struct sk_buff *skb);
    void (*sk_destruct)(struct sock *sk);
    struct sock_reuseport __rcu *sk_reuseport_cb;
    struct rcu_head sk_rcu;
};</code></pre>
<h2>Members</h2>
<p>__sk_common</p>
<dl>
<dd>shared layout with inet_timewait_sock</dl>
<p> sk_lock</p>
<dl>
<dd>synchronizer</dl>
<p> sk_receive_queue</p>
<dl>
<dd>incoming packets</dl>
<p> {unnamed_struct}</p>
<dl>
<dd>anonymous</dl>
<p> sk_policy[2]</p>
<dl>
<dd>flow policy</dl>
<p> sk_rx_dst</p>
<dl>
<dd>receive input route used by early demux</dl>
<p> sk_dst_cache</p>
<dl>
<dd>destination cache</dl>
<p> sk_wmem_alloc</p>
<dl>
<dd>transmit queue bytes committed</dl>
<p> sk_omem_alloc</p>
<dl>
<dd>&quot;o&#8221; is &#8220;option&#8221; or &#8220;other&quot;</dl>
<p> sk_sndbuf</p>
<dl>
<dd>size of send buffer in bytes</dl>
<p> sk_write_queue</p>
<dl>
<dd>Packet sending queue</dl>
<p> sk_padding</p>
<dl>
<dd>unused element for alignment</dl>
<p> sk_no_check_tx</p>
<dl>
<dd><code>SO_NO_CHECK</code> setting, set checksum in TX packets</dl>
<p> sk_no_check_rx</p>
<dl>
<dd>allow zero checksum in RX packets</dl>
<p> sk_userlocks</p>
<dl>
<dd><code>SO_SNDBUF</code> and <code>SO_RCVBUF</code> settings</dl>
<p> sk_protocol</p>
<dl>
<dd>which protocol this socket belongs in this network family</dl>
<p> sk_type</p>
<dl>
<dd>socket type (<code>SOCK_STREAM</code>, etc)</dl>
<p> sk_wmem_queued</p>
<dl>
<dd>persistent queue size</dl>
<p> sk_allocation</p>
<dl>
<dd>allocation mode</dl>
<p> sk_pacing_rate</p>
<dl>
<dd>Pacing rate (if supported by transport/packet scheduler)</dl>
<p> sk_max_pacing_rate</p>
<dl>
<dd>Maximum pacing rate (<code>SO_MAX_PACING_RATE</code>)</dl>
<p> sk_route_caps</p>
<dl>
<dd>route capabilities (e.g. <code>NETIF_F_TSO</code>)</dl>
<p> sk_route_nocaps</p>
<dl>
<dd>forbidden route capabilities (e.g NETIF_F_GSO_MASK)</dl>
<p> sk_gso_type</p>
<dl>
<dd>GSO type (e.g. <code>SKB_GSO_TCPV4</code>)</dl>
<p> sk_gso_max_size</p>
<dl>
<dd>Maximum GSO segment size to build</dl>
<p> sk_gso_max_segs</p>
<dl>
<dd>Maximum number of GSO segments</dl>
<p> sk_rcvlowat</p>
<dl>
<dd><code>SO_RCVLOWAT</code> setting</dl>
<p> sk_lingertime</p>
<dl>
<dd><code>SO_LINGER</code> l_linger setting</dl>
<p> sk_error_queue</p>
<dl>
<dd>rarely used</dl>
<p> sk_prot_creator</p>
<dl>
<dd>sk_prot of original sock creator (see ipv6_setsockopt, IPV6_ADDRFORM for instance)</dl>
<p> sk_callback_lock</p>
<dl>
<dd>used with the callbacks in the end of this struct</dl>
<p> sk_err</p>
<dl>
<dd>last error</dl>
<p> sk_err_soft</p>
<dl>
<dd>errors that don&#8217;t cause failure but are the cause of a persistent failure not just &#8216;timed out&#8217;</dl>
<p> sk_ack_backlog</p>
<dl>
<dd>current listen backlog</dl>
<p> sk_max_ack_backlog</p>
<dl>
<dd>listen backlog set in <code>listen</code></dl>
<p> sk_priority</p>
<dl>
<dd><code>SO_PRIORITY</code> setting</dl>
<p> sk_mark</p>
<dl>
<dd>generic packet mark</dl>
<p> sk_peer_pid</p>
<dl>
<dd>struct pid for this socket&#8217;s peer</dl>
<p> sk_peer_cred</p>
<dl>
<dd><code>SO_PEERCRED</code> setting</dl>
<p> sk_rcvtimeo</p>
<dl>
<dd><code>SO_RCVTIMEO</code> setting</dl>
<p> sk_sndtimeo</p>
<dl>
<dd><code>SO_SNDTIMEO</code> setting</dl>
<p> sk_timer</p>
<dl>
<dd>sock cleanup timer</dl>
<p> sk_stamp</p>
<dl>
<dd>time stamp of last packet received</dl>
<p> sk_tsflags</p>
<dl>
<dd>SO_TIMESTAMPING socket options</dl>
<p> sk_shutdown</p>
<dl>
<dd>mask of <code>SEND_SHUTDOWN</code> and/or <code>RCV_SHUTDOWN</code></dl>
<p> sk_tskey</p>
<dl>
<dd>counter to disambiguate concurrent tstamp requests</dl>
<p> sk_socket</p>
<dl>
<dd>Identd and reporting IO signals</dl>
<p> sk_user_data</p>
<dl>
<dd>RPC layer private data</dl>
<p> sk_frag</p>
<dl>
<dd>cached page frag</dl>
<p> sk_send_head</p>
<dl>
<dd>front of stuff to transmit</dl>
<p> sk_peek_off</p>
<dl>
<dd>current peek_offset value</dl>
<p> sk_write_pending</p>
<dl>
<dd>a write to stream socket waits to start</dl>
<p> sk_security</p>
<dl>
<dd>used by security modules</dl>
<p> sk_cgrp_data</p>
<dl>
<dd>cgroup data for this cgroup</dl>
<p> sk_memcg</p>
<dl>
<dd>this socket&#8217;s memory cgroup association</dl>
<p> sk_state_change</p>
<dl>
<dd>callback to indicate change in the state of the sock</dl>
<p> sk_data_ready</p>
<dl>
<dd>callback to indicate there is data to be processed</dl>
<p> sk_write_space</p>
<dl>
<dd>callback to indicate there is bf sending space available</dl>
<p> sk_error_report</p>
<dl>
<dd>callback to indicate errors (e.g. <code>MSG_ERRQUEUE</code>)</dl>
<p> sk_backlog_rcv</p>
<dl>
<dd>callback to process the backlog</dl>
<p> sk_destruct</p>
<dl>
<dd>called at sock freeing time, i.e. when all refcnt == 0</dl>
<p> sk_reuseport_cb</p>
<dl>
<dd>reuseport group container</dl>
<p> sk_rcu</p>
<dl>
<dd>used during RCU grace period</dl>
<h2>Copyright</h2>
