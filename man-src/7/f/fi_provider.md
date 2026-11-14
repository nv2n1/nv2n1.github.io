---
title: "fi_provider(7)"
name: "fi_provider"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fi_provider/"
---

fi_provider - Fabric Interface Providers

<h2>Overview</h2>

Conceptually, a fabric provider may be viewed as a local hardware NIC driver, though a provider is not limited by this definition. The first component of libfabric is a general purpose framework that is capable of handling different types of fabric hardware. All fabric hardware devices and their software drivers are required to support this framework. Devices and the drivers that plug into the libfabric framework are referred to as fabric providers, or simply providers. 

 This distribution of libfabric contains the following providers (although more may be available via run-time plug-ins):

<h3>Core providers</h3>

GNI : A provider for the Aries interconnect in Cray XC(TM) systems utilizing the user-space Generic Networking Interface. See <a HREF="/docs/linux/man/7-fi_gni/">fi_gni</a>(7) for more information. 

 PSM : High-speed InfiniBand networking from Intel. See <a HREF="/docs/linux/man/7-fi_psm/">fi_psm</a>(7) for more information. 

 Sockets : A general purpose provider that can be used on any network that supports TCP/UDP sockets. This provider is not intended to provide performance improvements over regular TCP/UDP sockets, but rather to allow developers to write, test, and debug application code even on platforms that do not have high-speed networking. See <a HREF="/docs/linux/man/7-fi_sockets/">fi_sockets</a>(7) for more information. 

 usNIC : Ultra low latency Ethernet networking over Cisco userspace VIC adapters. See <a HREF="/docs/linux/man/7-fi_usnic/">fi_usnic</a>(7) for more information. 

 Verbs : This provider uses the Linux Verbs API for network transport. Application performance is, obviously expected to be similar to that of the native Linux Verbs API. Analogous to the Sockets provider, the Verbs provider is intended to enable developers to write, test, and debug application code on platforms that only have Linux Verbs-based networking. See <a HREF="/docs/linux/man/7-fi_verbs/">fi_verbs</a>(7) for more information. 

 Blue Gene/Q : See <a HREF="/docs/linux/man/7-fi_bgq/">fi_bgq</a>(7) for more information.

<h3>Utility providers</h3>

RxM : The RxM provider (ofi_rxm) is an utility provider that supports RDM endpoints emulated over MSG endpoints of a core provider. See <a HREF="/docs/linux/man/7-fi_rxm/">fi_rxm</a>(7) for more information.

<h2>Core Versus Utility Providers</h2>

Core providers implement the libfabric interfaces directly over low-level hardware and software interfaces. They are designed to support a specific class of hardware, and may be limited to supporting a single NIC. Core providers often only support libfabric features and interfaces that map efficiently to their underlying hardware. 

 Utility providers are distinct from core providers in that they are not associated with specific classes of devices. They instead work with core providers to expand their features, and interact with core providers through libfabric interfaces internally. Utility providers are often used to support a specific endpoint type over a simpler endpoint type. For example, the RXD provider implements reliability over unreliable datagram endpoints. The utility providers will not layer over the sockets provider unless it is explicitly requested. 

 Utility providers show up as a component in the core provider's component list. See <a HREF="/docs/linux/man/3-fi_fabric/">fi_fabric</a>(3). Utility providers are enabled automatically for core providers that do not support the feature set requested by an application.

<h2>Provider Requirements</h2>

Libfabric provides a general framework for supporting multiple types of fabric objects and their related interfaces. Fabric providers have a large amount of flexibility in selecting which components they are able and willing to support, based on specific hardware constraints. Provider developers should refer to docs/provider for information on functionaliy supplied by the framework to assist in provider implementation. To assist in the development of applications, libfabric specifies the following requirements that must be met by any fabric provider, if requested by an application. 

 Note that the instantiation of a specific fabric object is subject to application configuration parameters and need not meet these requirements.
<dl><dt>&bull;
<dd>A fabric provider must support at least one endpoint type.
<dt>&bull;
<dd>All endpoints must support the message queue data transfer interface (fi_ops_msg).
<dt>&bull;
<dd>An endpoint that advertises support for a specific endpoint capability must support the corresponding data transfer interface.
<dt>&bull;
<dd>FI_ATOMIC - fi_ops_atomic
<dt>&bull;
<dd>FI_RMA - fi_ops_rma
<dt>&bull;
<dd>FI_TAGGED - fi_ops_tagged
<dt>&bull;
<dd>Endpoints must support all transmit and receive operations for any data transfer interface that they support.
<dt>&bull;
<dd>Exception: If an operation is only usable for an operation that the provider does not support, and support for that operation is conveyed using some other mechanism, the operation may return
<dl><dd><dl><dt>&bull;
<dd>FI_ENOSYS. For example, if the provider does not support injected data, it can set the attribute inject_size = 0, and fail all fi_inject operations.</dl></dl><dt>&bull;
<dd>The framework supplies wrappers around the 'msg' operations that can be used. For example, the framework implements the sendv() msg operation by calling sendmsg(). Providers may reference the general operation, and supply on the sendmsg() implementation.
<dt>&bull;
<dd>Providers must set all operations to an implementation. Function pointers may not be left NULL or uninitialized. The framework supplies empty functions that return -FI_ENOSYS which can be used for this purpose.
<dt>&bull;
<dd>Endpoints must support the CM interface as follows:
<dt>&bull;
<dd>FI_EP_MSG endpoints must support all CM operations.
<dt>&bull;
<dd>FI_EP_DGRAM endpoints must support CM getname and setname.
<dt>&bull;
<dd>FI_EP_RDM endpoints must support CM getname and setname.
<dt>&bull;
<dd>Providers that support connectionless endpoints must support all AV operations (fi_ops_av).
<dt>&bull;
<dd>Providers that support memory registration, must support all MR operations (fi_ops_mr).
<dt>&bull;
<dd>Providers should support both completion queues and counters.
<dt>&bull;
<dd>If FI_RMA_EVENT is not supported, counter support is limited to local events only.
<dt>&bull;
<dd>Completion queues must support the FI_CQ_FORMAT_CONTEXT and FI_CQ_FORMAT_MSG.
<dt>&bull;
<dd>Providers that support FI_REMOTE_CQ_DATA shall support FI_CQ_FORMAT_DATA.
<dt>&bull;
<dd>Providers that support FI_TAGGED shall support FI_CQ_FORMAT_TAGGED.
<dt>&bull;
<dd>A provider is expected to be forward compatible, and must be able to be compiled against expanded fi_xxx_ops structures that define new functions added after the provider was written. Any unknown functions must be set to NULL.
<dt>&bull;
<dd>Providers shall document in their man page which features they support, and any missing requirements.</dl>
 

 Future versions of libfabric will automatically enable a more complete set of features for providers that focus their implementation on a narrow subset of libfabric capabilities.

<h2>Logging Interface</h2>

Logging is performed using the FI_ERR, FI_LOG, and FI_DEBUG macros.

<h3>Definitions</h3>

<dl><dd><pre>#define FI_ERR(prov_name, subsystem, ...)
#define FI_LOG(prov_name, prov, level, subsystem, ...)
#define FI_DEBUG(prov_name, subsystem, ...)</pre></dl>

<h3>Arguments</h3>

prov_name : String representing the provider name. 

 prov : Provider context structure. 

 level : Log level associated with log statement. 

 subsystem : Subsystem being logged from.

<h3>Description</h3>

FI_ERR : Always logged. 

 FI_LOG : Logged if the intended provider, log level, and subsystem parameters match the user supplied values. 

 FI_DEBUG : Logged if configured with the --enable-debug flag.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-fi_gni/">fi_gni</a>(7), <a HREF="/docs/linux/man/7-fi_psm/">fi_psm</a>(7), <a HREF="/docs/linux/man/7-fi_sockets/">fi_sockets</a>(7), <a HREF="/docs/linux/man/7-fi_usnic/">fi_usnic</a>(7), <a HREF="/docs/linux/man/7-fi_verbs/">fi_verbs</a>(7), <a HREF="/docs/linux/man/7-fi_bgq/">fi_bgq</a>(7),

<h2>Authors</h2>

OpenFabrics.
