---
title: "ibacm_prov(7)"
name: "ibacm_prov"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ibacm_prov/"
---

ibacm_prov - InfiniBand communication management assistant provider interface

<h2>Synopsis</h2>

<pre><code>#include &lt;infiniband/acm_prov.h&gt;</code></pre>

<h2>Description</h2>

The ibacm provider interface provides a plugin interface that allows a vendor to implement proprietary solutions to support scalable address and route resolution services over InfiniBand. To add a provider to the ibacm core service, the provider must
<dl><dt>1. be implemented as a shared library;
<dd><dt>2. be installed under a configured directory, eg., /usr/lib64/ibacm/;
<dd><dt>3 export a function provider_query() that returns a pointer to its provider info
<dd>and version info.</dl>
 The prototype of provider_query function is defined below: struct acm_provider {
    size_t size;
    uint32_t version;
    char *name;
    int (*open_device)(const struct acm_device *device,
                       void **dev_context);
    void (*close_device)(void *dev_context);
    int (*open_port)(const struct acm_port *port,
                     void *dev_context, void **port_context);
    void (*close_port)(void *port_context);
    int (*open_endpoint)(const struct acm_endpoint *endpoint,
                         void *port_context, void **ep_context);
    void (*close_endpoint)(void *ep_context);
    int (*add_address)(const struct acm_address *addr, void *ep_context,
                       void **addr_context);
    void (*remove_address)(void *addr_context);
    int (*resolve)(void *addr_context, struct acm_msg *msg, uint64_t id);
    int (*query)(void *addr_context, struct acm_msg *msg, uint64_t id);
    int (*handle_event)(void *port_context, enum ibv_event_type type);
    void (*query_perf)(void *ep_context, uint64_t *values, uint8_t *cnt);
}; This function should return a pointer to its provider structure: <pre><code>struct acm_provider {
    size_t size;
    uint32_t version;
    char *name;
    int (*open_device)(const struct acm_device *device,
                       void **dev_context);
    void (*close_device)(void *dev_context);
    int (*open_port)(const struct acm_port *port,
                     void *dev_context, void **port_context);
    void (*close_port)(void *port_context);
    int (*open_endpoint)(const struct acm_endpoint *endpoint,
                         void *port_context, void **ep_context);
    void (*close_endpoint)(void *ep_context);
    int (*add_address)(const struct acm_address *addr, void *ep_context,
                       void **addr_context);
    void (*remove_address)(void *addr_context);
    int (*resolve)(void *addr_context, struct acm_msg *msg, uint64_t id);
    int (*query)(void *addr_context, struct acm_msg *msg, uint64_t id);
    int (*handle_event)(void *port_context, enum ibv_event_type type);
    void (*query_perf)(void *ep_context, uint64_t *values, uint8_t *cnt);
};</code></pre> The size and version fields provide a way to detect version compatibility. When a port is assigned to the provider, the ibacm core will call the open/add_address functions; Similarly, when a port is down or re-assigned to another provider, the close/remove_address functions will be invoked to release resources. The ibacm core will centralize the management of events for each device and events not handled by the ibacm core will be forwarded to the relevant port through the handle_event() function. The resolve() function will be called to resolve a destination name into a path record. The performance of the provider for each endpoint can be queried by calling perf_query(). To share a configuration file, the path for the ibacm configuration file is exported through the variable opts_file. Each loaded provider can open this configuration file and parse the contents related to its own operation. Non-related sections should be ignored. Some helper functions are also exported by the ibacm core. For example, the acm_log define (or the acm_write() function) can be used to log messages into ibacm's log file (default /var/log/ibacm.log). For details, refer to the acm_prov.h file.

<h2>Notes</h2>

A provider should always set the version in its provider info structure as the value of the define ACM_PROV_VERSION at the time the provider is implemented. Never set the version to ACM_PROV_VERSION itself as the define may be changed over time when the provider interface is changed, unless the provider itself is placed in ibacm source tree. This is to avoid the version problem when the old provider implementation is built against a new acm_prov.h file. The ibacm will always check the version of the provider at loading time.

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-ib_acme/">ib_acme</a>(1), <a HREF="/docs/linux/man/1-ibacm/">ibacm</a>(1), <a HREF="/docs/linux/man/7-ibacm/">ibacm</a>(7) 
