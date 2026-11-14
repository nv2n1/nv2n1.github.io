---
title: "network_namespaces(7)"
name: "network_namespaces"
section: "7"
letter: "n"
url: "/docs/linux/man/7-network_namespaces/"
---

network_namespaces - overview of Linux network namespaces

<h2>Description</h2>

Network namespaces provide isolation of the system resources associated with networking: network devices, IPv4 and IPv6 protocol stacks, IP routing tables, firewall rules, the <i>/proc/net</i> directory (which is a symbolic link to <i>/proc/PID/net</i>), the <i>/sys/class/net</i> directory, various files under <i>/proc/sys/net</i>, port numbers (sockets), and so on. In addition, network namespaces isolate the UNIX domain abstract socket namespace (see <b><a HREF="/docs/linux/man/7-unix/">unix</a></b>(7)). 

 A physical network device can live in exactly one network namespace. When a network namespace is freed (i.e., when the last process in the namespace terminates), its physical network devices are moved back to the initial network namespace (not to the parent of the process). 

 A virtual network (<b><a HREF="/docs/linux/man/4-veth/">veth</a></b>(4)) device pair provides a pipe-like abstraction that can be used to create tunnels between network namespaces, and can be used to create a bridge to a physical network device in another namespace. When a namespace is freed, the <b><a HREF="/docs/linux/man/4-veth/">veth</a></b>(4) devices that it contains are destroyed. 

 Use of network namespaces requires a kernel that is configured with the <b>CONFIG_NET_NS</b> option.

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/1-nsenter/">nsenter</a></b>(1), <b><a HREF="/docs/linux/man/1-unshare/">unshare</a></b>(1), <b><a HREF="/docs/linux/man/2-clone/">clone</a></b>(2), <b><a HREF="/docs/linux/man/4-veth/">veth</a></b>(4), <b><a HREF="/docs/linux/man/5-proc/">proc</a></b>(5), <b><a HREF="/docs/linux/man/5-sysfs/">sysfs</a></b>(5), <b><a HREF="/docs/linux/man/7-namespaces/">namespaces</a></b>(7), <b><a HREF="/docs/linux/man/7-user_namespaces/">user_namespaces</a></b>(7), <b><a HREF="/docs/linux/man/8-brctl/">brctl</a></b>(8), <b><a HREF="/docs/linux/man/8-ip/">ip</a></b>(8), <b><a HREF="/docs/linux/man/8-ip-address/">ip-address</a></b>(8), <b><a HREF="/docs/linux/man/8-ip-link/">ip-link</a></b>(8), <b><a HREF="/docs/linux/man/8-ip-netns/">ip-netns</a></b>(8), <b><a HREF="/docs/linux/man/8-iptables/">iptables</a></b>(8), <b><a HREF="/docs/linux/man/8-ovs-vsctl/">ovs-vsctl</a></b>(8)

<h2>Colophon</h2>

This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 
