---
title: "ibv_destroy_flow(3)"
name: "ibv_destroy_flow"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_flow/"
description: "ibv_create_flow, ibv_destroy_flow – create or destroy flow steering rules"
---

<h2 class="name">NAME</h2>
<p> ibv_create_flow, ibv_destroy_flow &#8211; create or destroy flow steering rules </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_flow *ibv_create_flow(struct ibv_qp *qp,
                                 struct ibv_flow_attr *flow_attr);
int ibv_destroy_flow(struct ibv_flow *flow_id);
</code></pre>
<h2>DESCRIPTION</h2>
<h3>ibv_create_flow()</h3>
<p> allows a user application QP <i>qp</i> to be attached into a specified flow <i>flow</i> which is defined in <i>&lt;infiniband/verbs.h&gt;</i> </p>
<p>struct ibv_flow_attr {<br />
    uint32_t comp_mask;           /* Future extendibility */<br />
    enum ibv_flow_attr_type type; /* Rule type &#8211; see below */<br />
    uint16_t size;                /* Size of command */<br />
    uint16_t priority;            /* Rule priority &#8211; see below */<br />
    uint8_t num_of_specs;         /* Number of ibv_flow_spec_xxx */<br />
    uint8_t port;                 /* The uplink port number */<br />
    uint32_t flags;               /* Extra flags for rule &#8211; see below */<br />
    /* Following are the optional layers according to user request<br />
     * struct ibv_flow_spec_xxx<br />
     * struct ibv_flow_spec_yyy<br />
     */<br />
};<br />
enum ibv_flow_attr_type {<br />
    IBV_FLOW_ATTR_NORMAL = 0x0,      /* Steering according to rule specifications */<br />
    IBV_FLOW_ATTR_ALL_DEFAULT = 0x1, /* Default unicast and multicast rule &#8211; receive all Eth traffic which isn&#8217;t steered to any QP */<br />
    IBV_FLOW_ATTR_MC_DEFAULT = 0x2,  /* Default multicast rule &#8211; receive all Eth multicast traffic which isn&#8217;t steered to any QP */<br />
    IBV_FLOW_ATTR_SNIFFER = 0x3,     /* Sniffer rule &#8211; receive all port traffic */<br />
};<br />
enum ibv_flow_flags {<br />
    IBV_FLOW_ATTR_FLAGS_ALLOW_LOOP_BACK = 1 &lt;&lt; 0, /* Apply the rules on packets that were sent from the attached QP through loopback */<br />
    IBV_FLOW_ATTR_FLAGS_DONT_TRAP = 1 &lt;&lt; 1,       /* Rule doesn&#8217;t trap received packets, allowing them to match lower prioritized rules */<br />
    IBV_FLOW_ATTR_FLAGS_EGRESS = 1 &lt;&lt; 2,          /* Match sent packets against EGRESS rules and carry associated actions if required */<br />
};</p>
<p>enum ibv_flow_spec_type {<br />
    IBV_FLOW_SPEC_ETH = 0x20,             /* Flow specification of L2 header */<br />
    IBV_FLOW_SPEC_IPV4 = 0x30,            /* Flow specification of IPv4 header */<br />
    IBV_FLOW_SPEC_IPV6 = 0x31,            /* Flow specification of IPv6 header */<br />
    IBV_FLOW_SPEC_IPV4_EXT = 0x32,        /* Extended flow specification of IPv4 */<br />
    IBV_FLOW_SPEC_ESP = 0x34,             /* Flow specification of ESP (IPSec) header */<br />
    IBV_FLOW_SPEC_TCP = 0x40,             /* Flow specification of TCP header */<br />
    IBV_FLOW_SPEC_UDP = 0x41,             /* Flow specification of UDP header */<br />
    IBV_FLOW_SPEC_VXLAN_TUNNEL = 0x50,    /* Flow specification of VXLAN header */<br />
    IBV_FLOW_SPEC_GRE = 0x51,             /* Flow specification of GRE header */<br />
    IBV_FLOW_SPEC_MPLS = 0x60,            /* Flow specification of MPLS header */<br />
    IBV_FLOW_SPEC_INNER = 0x100,          /* Flag making L2/L3/L4 specifications to be applied on the inner header */<br />
    IBV_FLOW_SPEC_ACTION_TAG = 0x1000,    /* Action tagging matched packet */<br />
    IBV_FLOW_SPEC_ACTION_DROP = 0x1001,   /* Action dropping matched packet */<br />
    IBV_FLOW_SPEC_ACTION_HANDLE = 0x1002, /* Carry out an action created by ibv_create_flow_action_xxxx verb */<br />
    IBV_FLOW_SPEC_ACTION_COUNT = 0x1003,  /* Action count matched packet with a ibv_counters handle */<br />
};</p>
<p>Flow specification general structure : struct ibv_flow_spec_xxx {<br />
    enum ibv_flow_spec_type type;<br />
    uint16_t size; /* Flow specification size = sizeof(struct ibv_flow_spec_xxx) */<br />
    struct ibv_flow_xxx_filter val;<br />
    struct ibv_flow_xxx_filter mask; /* Defines which bits from the filter value are applicable when looking for a match in the incoming packet */<br />
};<br />
Each spec struct holds the relevant network layer parameters for matching. To enforce the match, the user sets a mask for each parameter.</p>
<p>Packets coming from the wire are matched against the flow specification. If a match is found, the associated flow actions are executed on the packet.</p>
<p>In ingress flows, the QP parameter is treated as another action of scattering the packet to the respected QP.</p>
<p>If the bit is set in the mask, the corresponding bit in the value should be matched.</p>
<p>Note that most vendors support either full mask (all &#8220;1&#8221;s) or zero mask (all &#8220;0&#8221;s).</p>
<p>Network parameters in the relevant network structs should be given in network order (big endian).</p>
<h3>Flow domains and priority</h3>
<p> Flow steering defines the concept of domain and priority. Each domain represents an application that can attach a flow. Domains are prioritized. A higher priority domain will always supersede a lower priority domain when their flow specifications overlap.<br />
 <code>IB verbs have the higher priority domain.</code><br />
 In addition to the domain, there is priority within each of the domains. A lower priority numeric value (higher priority) takes precedence over matching rules with higher numeric priority value (lower priority). It is important to note that the priority value of a flow spec is used not only to establish the precedence of conflicting flow matches but also as a way to abstract the order on which flow specs are tested for matches. Flows with higher priorities will be tested before flows with lower priorities. </p>
<h3>Rules definition ordering</h3>
<p> An application can provide the ibv_flow_spec_xxx rules in an un-ordered scheme. In this case, each spec should be well defined and match a specific network header layer. In some cases, when certain flow spec types are present in the spec list, it is required to provide the list in an ordered manner so that the position of that flow spec type in the protocol stack is strictly defined. When the certain spec type, which requires the ordering, resides in the inner network protocol stack (in tunnel protocols) the ordering should be applied to the inner network specs and should be combined with the inner spec indication using the IBV_FLOW_SPEC_INNER flag. For example: An MPLS spec which attempts to match an MPLS tag in the inner network should have the IBV_FLOW_SPEC_INNER flag set and so do the rest of the inner network specs. On top of that, all the inner network specs should be provided in an ordered manner. This is essential to represent many of the encapsulation tunnel protocols. </p>
<p> The flow spec types which require this sort of ordering are:<br />
 <code>1. IBV_FLOW_SPEC_MPLS &#8211;</code><br />
 Since MPLS header can appear at several locations in the protocol stack and can also be encapsulated on top of different layers, it is required to place this spec according to its exact location in the protocol stack. </p>
<h3>ibv_destroy_flow()</h3>
<p> destroys the flow <i>flow_id</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_flow()</code> returns a pointer to the flow, or NULL if the request fails. In case of an error, errno is updated. </p>
<p> <code>ibv_destroy_flow()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>ERRORS</h2>
<h3>EINVAL</h3>
<p> <code>ibv_create_flow()</code> flow specification, QP or priority are invalid </p>
<p> <code>ibv_destroy_flow()</code> flow_id is invalid</p>
<h3>ENOMEM</h3>
<p> Couldn&#8217;t create/destroy flow, not enough memory</p>
<h3>ENXIO</h3>
<p> Device managed flow steering isn&#8217;t currently supported</p>
<h3>EPERM</h3>
<p> No permissions to add the flow steering rule</p>
<h2>NOTES</h2>
<p> 1. These verbs are available only for devices supporting </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IBV_DEVICE_MANAGED_FLOW_STEERING and only for QPs of Transport Service Type <code>IBV_QPT_UD</code> or <code>IBV_QPT_RAW_PACKET</code><br />
 2. User must memset the spec struct with zeros before using it.<br />
 3. ether_type field in ibv_flow_eth_filter is the ethertype following the last VLAN tag of the packet.<br />
 4. Only rule type IBV_FLOW_ATTR_NORMAL supports IBV_FLOW_ATTR_FLAGS_DONT_TRAP flag.<br />
 5. No specifications are needed for IBV_FLOW_ATTR_SNIFFER rule type.<br />
 6. When IBV_FLOW_ATTR_FLAGS_EGRESS flag is set, the qp parameter is used only as a mean to get the device. </p>
<h2>EXAMPLE</h2>
<p> Below flow_attr defines a rule in priority 0 to match a destination mac address and a source ipv4 address. For that, L2 and L3 specs are used.<br />
 If there is a hit on this rule, means the received packet has destination mac: 66:11:22:33:44:55 and source ip: 0x0B86C806, the packet is steered to its attached qp. </p>
<pre><code>
struct raw_eth_flow_attr {
    struct ibv_flow_attr attr;
    struct ibv_flow_spec_eth spec_eth;
    struct ibv_flow_spec_ipv4 spec_ipv4;
} __attribute__((packed));
struct raw_eth_flow_attr flow_attr = {
    .attr = {
        .comp_mask = 0,
        .type = IBV_FLOW_ATTR_NORMAL,
        .size = sizeof(flow_attr),
        .priority = 0,
        .num_of_specs = 2,
        .port = 1,
        .flags = 0,
    },
    .spec_eth = {.type = IBV_FLOW_SPEC_ETH, .size = sizeof(struct ibv_flow_spec_eth), .val = {
                                                                                          .dst_mac = {0x66, 0x11, 0x22, 0x33, 0x44, 0x55},
                                                                                          .src_mac = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00},
                                                                                          .ether_type = 0,
                                                                                          .vlan_tag = 0,
                                                                                      },
                 .mask = {
                     .dst_mac = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
                     .src_mac = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
                     .ether_type = 0,
                     .vlan_tag = 0,
                 }},
    .spec_ipv4 = {.type = IBV_FLOW_SPEC_IPV4, .size = sizeof(struct ibv_flow_spec_ipv4), .val = {
                                                                                             .src_ip = 0x0B86C806,
                                                                                             .dst_ip = 0,
                                                                                         },
                  .mask = {
                      .src_ip = 0xFFFFFFFF,
                      .dst_ip = 0,
                  }}};
</code></pre>
<h2>AUTHORS</h2>
<dl>
<dt>Hadar Hen Zion &lt;hadarh [at] mellanox.com&gt;</p>
<dd>
<dt>Matan Barak &lt;matanb [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
<dt>Maor Gottlieb &lt;maorg [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
