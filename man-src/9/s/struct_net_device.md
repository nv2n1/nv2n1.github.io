---
title: "struct_net_device(9)"
name: "struct_net_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_net_device/"
---

struct_net_device - The DEVICE structure. Actually, this whole structure is a big mistake. It mixes I/O data with strictly "high-level" data, and it has to know about almost every data structure used in the INET module.

<h2>Synopsis</h2>

<pre><code>struct net_device {
    char name[IFNAMSIZ];
    struct hlist_node name_hlist;
    char *ifalias;
    unsigned long mem_end;
    unsigned long mem_start;
    unsigned long base_addr;
    int irq;
    atomic_t carrier_changes;
    unsigned long state;
    struct list_head dev_list;
    struct list_head napi_list;
    struct list_head unreg_list;
    struct list_head close_list;
    struct list_head ptype_all;
    struct list_head ptype_specific;
    struct {
        unnamed_struct
    };
    struct garp_port __rcu *garp_port;
    struct mrp_port __rcu *mrp_port;
    struct device dev;
    const struct attribute_group *sysfs_groups[4];
    const struct attribute_group *sysfs_rx_queue_group;
    const struct rtnl_link_ops *rtnl_link_ops;
#define GSO_MAX_SIZE 65536
    unsigned int gso_max_size;
#define GSO_MAX_SEGS 65535
    u16 gso_max_segs;
#ifdef CONFIG_DCB
    const struct dcbnl_rtnl_ops *dcbnl_ops;
#endif
    u8 num_tc;
    struct netdev_tc_txq tc_to_txq[TC_MAX_QUEUE];
    u8 prio_tc_map[TC_BITMASK + 1];
#if IS_ENABLED(CONFIG_FCOE)
    unsigned int fcoe_ddp_xid;
#endif
#if IS_ENABLED(CONFIG_CGROUP_NET_PRIO)
    struct netprio_map __rcu *priomap;
#endif
    struct phy_device *phydev;
    struct lock_class_key *qdisc_tx_busylock;
    struct lock_class_key *qdisc_running_key;
    bool proto_down;
};</code></pre>

<h2>Members</h2>

name[IFNAMSIZ]
<dl><dd>This is the first field of the "visible" part of this structure (i.e. as seen by users in the "Space.c" file). It is the name of the interface.</dl>
 

 name_hlist
<dl><dd>Device name hash chain, please keep it close to name[]</dl>
 

 ifalias
<dl><dd>SNMP alias</dl>
 

 mem_end
<dl><dd>Shared memory end</dl>
 

 mem_start
<dl><dd>Shared memory start</dl>
 

 base_addr
<dl><dd>Device I/O address</dl>
 

 irq
<dl><dd>Device IRQ number</dl>
 

 carrier_changes
<dl><dd>Stats to monitor carrier on&lt;-&gt;off transitions</dl>
 

 state
<dl><dd>Generic network queuing layer state, see netdev_state_t</dl>
 

 dev_list
<dl><dd>The global list of network devices</dl>
 

 napi_list
<dl><dd>List entry used for polling NAPI devices</dl>
 

 unreg_list
<dl><dd>List entry when we are unregistering the device; see the function unregister_netdev</dl>
 

 close_list
<dl><dd>List entry used when we are closing the device</dl>
 

 ptype_all
<dl><dd>Device-specific packet handlers for all protocols</dl>
 

 ptype_specific
<dl><dd>Device-specific, protocol-specific packet handlers</dl>
 

 {unnamed_struct}
<dl><dd>anonymous</dl>
 

 garp_port
<dl><dd>GARP</dl>
 

 mrp_port
<dl><dd>MRP</dl>
 

 dev
<dl><dd>Class/net/name entry</dl>
 

 sysfs_groups[4]
<dl><dd>Space for optional device, statistics and wireless sysfs groups</dl>
 

 sysfs_rx_queue_group
<dl><dd>Space for optional per-rx queue attributes</dl>
 

 rtnl_link_ops
<dl><dd>Rtnl_link_ops</dl>
 

 gso_max_size
<dl><dd>Maximum size of generic segmentation offload</dl>
 

 gso_max_segs
<dl><dd>Maximum number of segments that can be passed to the NIC for GSO</dl>
 

 dcbnl_ops
<dl><dd>Data Center Bridging netlink ops</dl>
 

 num_tc
<dl><dd>Number of traffic classes in the net device</dl>
 

 tc_to_txq[TC_MAX_QUEUE]
<dl><dd>XXX: need comments on this one</dl>
 

 prio_tc_map[TC_BITMASK + 1]
<dl><dd>XXX: need comments on this one</dl>
 

 fcoe_ddp_xid
<dl><dd>Max exchange id for FCoE LRO by ddp</dl>
 

 priomap
<dl><dd>XXX: need comments on this one</dl>
 

 phydev
<dl><dd>Physical device may attach itself for hardware timestamping</dl>
 

 qdisc_tx_busylock
<dl><dd>lockdep class annotating Qdisc-&gt;busylock spinlock</dl>
 

 qdisc_running_key
<dl><dd>lockdep class annotating Qdisc-&gt;running seqcount</dl>
 

 proto_down
<dl><dd>protocol port state information can be sent to the switch driver and used to set the phys state of the switch port.</dl>

<h2>Description</h2>

interface address info: 

 FIXME: cleanup struct net_device such that network protocol info moves out.

<h2>Copyright</h2>


