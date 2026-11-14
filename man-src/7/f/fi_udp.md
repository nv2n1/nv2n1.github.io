---
title: "fi_udp(7)"
name: "fi_udp"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fi_udp/"
---

fi_udp - The UDP Fabric Provider

<h2>Overview</h2>

The UDP provider is a basic provider that can be used on any system that supports UDP sockets. The provider is not intended to provide performance improvements over regular TCP sockets, but rather to allow application and provider developers to write, test, and debug their code. The UDP provider forms the foundation of a utility provider that enables the implementation of libfabric features over any hardware.

<h2>Supported Features</h2>

The UDP provider supports a minimal set of features useful for sending and receiving datagram messages over an unreliable endpoint. 

 Endpoint types : The provider supports only endpoint type FI_EP_DGRAM. 

 Endpoint capabilities : The following data transfer interface is supported: fi_msg. The provider supports standard unicast datagram transfers, as well as multicast operations. 

 Modes : The provider does not require the use of any mode bits. 

 Progress : The UDP provider supports both FI_PROGRESS_AUTO and FI_PROGRESS_MANUAL, with a default set to auto. However, receive side data buffers are not modified outside of completion processing routines.

<h2>Limitations</h2>

The UDP provider has hard-coded maximums for supported queue sizes and data transfers. These values are reflected in the related fabric attribute structures 

 EPs must be bound to both RX and TX CQs. 

 No support for selective completions or multi-recv. 

 No support for counters.

<h2>Runtime Parameters</h2>

No runtime parameters are currently defined.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-fabric/">fabric</a>(7), <a HREF="/docs/linux/man/7-fi_provider/">fi_provider</a>(7), <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3)

<h2>Authors</h2>

OpenFabrics.
