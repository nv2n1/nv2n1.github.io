---
title: "fi_verbs(7)"
name: "fi_verbs"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fi_verbs/"
---

fi_verbs - The Verbs Fabric Provider

<h2>Overview</h2>

The verbs provider enables applications using OFI to be run over any verbs hardware (Infiniband, iWarp, etc). It uses the Linux Verbs API for network transport and provides a translation of OFI calls to appropriate verbs API calls. It uses librdmacm for communication management and libibverbs for other control and data transfer operations.

<h2>Supported Features</h2>

The verbs provider supports a subset of OFI features.

<h3>Endpoint types</h3>

FI_EP_MSG, FI_EP_RDM (Experimental support FI_MSG, FI_TAGGED, FI_RMA interfaces).

<h3>Endpoint capabilities and features</h3>

<h3>MSG endpoints</h3>

FI_MSG, FI_RMA, FI_ATOMIC and shared receive contexts.

<h3>RDM endpoints</h3>

FI_MSG, FI_TAGGED, FI_RMA

<h3>Modes</h3>

Verbs provider requires applications to support the following modes:
<dl><dt>&bull;
<dd>FI_LOCAL_MR for all applications.
<dt>&bull;
<dd>FI_RX_CQ_DATA for applications that want to use RMA. Applications must take responsibility of posting receives for any incoming CQ data.
<dt>&bull;
<dd>FI_CONTEXT for applications making uses of the experimental FI_EP_RDM capability.</dl>

<h3>Addressing Formats</h3>

Supported addressing formats include FI_SOCKADDR, FI_SOCKADDR_IN, FI_SOCKADDR_IN6, FI_SOCKADDR_IB

<h3>Progress</h3>

Verbs provider supports FI_PROGRESS_AUTO: Asynchronous operations make forward progress automatically.

<h3>Operation flags</h3>

Verbs provider supports FI_INJECT, FI_COMPLETION, FI_REMOTE_CQ_DATA, FI_TRANSMIT_COMPLETE.

<h3>Msg Ordering</h3>

Verbs provider support the following message ordering:
<dl><dt>&bull;
<dd>Read after Read
<dt>&bull;
<dd>Read after Write
<dt>&bull;
<dd>Read after Send
<dt>&bull;
<dd>Write after Write
<dt>&bull;
<dd>Write after Send
<dt>&bull;
<dd>Send after Write
<dt>&bull;
<dd>Send after Send</dl>
 

 and the following completion ordering:
<dl><dt>&bull;
<dd>TX contexts: FI_ORDER_STRICT
<dt>&bull;
<dd>RX contexts: FI_ORDER_DATA</dl>

<h3>Fork</h3>

Verbs provider supports the fork system call by default. See the limitations section for restrictions. It can be turned off by setting the FI_FORK_UNSAFE environment variable to &quot;yes&quot;. This can improve the performance of memory registrations but it also makes the use of fork unsafe.

<h2>Limitations</h2>

<h3>Memory Regions</h3>

Only FI_MR_BASIC mode is supported. Adding regions via s/g list is supported only up to s/g list size of 1. No support for binding memory regions to a counter.

<h3>Wait objects</h3>

Only FI_WAIT_FD wait object is supported only for FI_EP_MSG endpoint type. Wait sets are not supported.

<h3>Resource Management</h3>

Application has to make sure CQs are not overrun as this cannot be detected by the provider.

<h3>Unsupported Features</h3>

The following features are not supported in verbs provider:

<h3>Unsupported Endpoint types</h3>

FI_EP_DGRAM

<h3>Unsupported Capabilities</h3>

FI_NAMED_RX_CTX, FI_DIRECTED_RECV, FI_TRIGGER, FI_MULTI_RECV, FI_RMA_EVENT

<h3>Other unsupported features</h3>

Scalable endpoints, FABRIC_DIRECT

<h3>Unsupported features specific to MSG endpoints</h3>

<dl><dt>&bull;
<dd>Counters, FI_SOURCE, FI_TAGGED, FI_PEEK, FI_CLAIM, fi_cancel, fi_ep_alias, shared TX context, cq_readfrom operations.
<dt>&bull;
<dd>Completion flags are not reported if a request posted to an endpoint completes in error.</dl>

<h3>Unsupported features specific to RDM endpoints</h3>

The RDM support for verbs have the following limitations:
<dl><dt>&bull;
<dd>Supports iovs of only size 1.
<dt>&bull;
<dd>Wait objects are not supported.
<dt>&bull;
<dd>Not thread safe.</dl>

<h3>Fork</h3>

The support for fork in the provider has the following limitations:
<dl><dt>&bull;
<dd>Fabric resources like endpoint, CQ, EQ, etc. should not be used in the forked process.
<dt>&bull;
<dd>The memory registered using fi_mr_reg has to be page aligned since ibv_reg_mr marks the entire page that a memory region belongs to as not to be re-mapped when the process is forked (MADV_DONTFORK).</dl>

<h2>Runtime Parameters</h2>

The verbs provider checks for the following environment variables.

<h3>Variables specific to MSG endpoints</h3>

FI_VERBS_TX_SIZE : Default maximum tx context size (default: 384) 

 FI_VERBS_RX_SIZE : Default maximum rx context size (default: 384) 

 FI_VERBS_TX_IOV_LIMIT : Default maximum tx iov_limit (default: 4) 

 FI_VERBS_RX_IOV_LIMIT : Default maximum rx iov_limit (default: 4)

<h3>Variables specific to RDM endpoints</h3>

FI_VERBS_IFACE : The prefix or the full name of the network interface associated with the IB device (default: ib) 

 FI_VERBS_RDM_BUFFER_NUM : The number of pre-registered buffers for buffered operations between the endpoints, must be a power of 2 (default: 8). 

 FI_VERBS_RDM_BUFFER_SIZE : The maximum size of a buffered operation (bytes) (default: platform specific). 

 FI_VERBS_RDM_RNDV_SEG_SIZE : The segment size for zero copy protocols (bytes)(default: 1073741824). 

 FI_VERBS_RDM_CQREAD_BUNCH_SIZE : The number of entries to be read from the verbs completion queue at a time (default: 8). 

 FI_VERBS_RDM_THREAD_TIMEOUT : The wake up timeout of the helper thread (usec) (default: 100). 

 FI_VERBS_RDM_EAGER_SEND_OPCODE : The operation code that will be used for eager messaging. Only IBV_WR_SEND and IBV_WR_RDMA_WRITE_WITH_IMM are supported. The last one is not applicable for iWarp. (default: IBV_WR_SEND)

<h3>Environment variables notes</h3>

The fi_info utility would give the up-to-date information on environment variables: fi_info -p verbs -e

<h2>Troubleshooting / Known issues</h2>

When running an app over verbs provider with valgrind, there may be reports of memory leak in functions from dependent libraries (e.g. libibverbs, librdmacm). These leaks are safe to ignore.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-fabric/">fabric</a>(7), <a HREF="/docs/linux/man/7-fi_provider/">fi_provider</a>(7),

<h2>Authors</h2>

OpenFabrics.
