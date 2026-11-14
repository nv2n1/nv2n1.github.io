---
title: "struct_usb_function(9)"
name: "struct_usb_function"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_function/"
description: "struct_usb_function – describes one function of a configuration"
---

<p>struct_usb_function &#8211; describes one function of a configuration</p>
<h2>Synopsis</h2>
<pre><code>struct usb_function {
    const char *name;
    struct usb_gadget_strings **strings;
    struct usb_descriptor_header **fs_descriptors;
    struct usb_descriptor_header **hs_descriptors;
    struct usb_descriptor_header **ss_descriptors;
    struct usb_descriptor_header **ssp_descriptors;
    struct usb_configuration *config;
    struct usb_os_desc_table *os_desc_table;
    unsigned os_desc_n;
    int (*bind)(struct usb_configuration *, struct usb_function *);
    void (*unbind)(struct usb_configuration *, struct usb_function *);
    void (*free_func)(struct usb_function *f);
    struct module *mod;
    int (*set_alt)(struct usb_function *, unsigned interface, unsigned alt);
    int (*get_alt)(struct usb_function *, unsigned interface);
    void (*disable)(struct usb_function *);
    int (*setup)(struct usb_function *, const struct usb_ctrlrequest *);
    bool (*req_match)(struct usb_function *, const struct usb_ctrlrequest *, bool config0);
    void (*suspend)(struct usb_function *);
    void (*resume)(struct usb_function *);
    int (*get_status)(struct usb_function *);
    int (*func_suspend)(struct usb_function *, u8 suspend_opt);
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>For diagnostics, identifies the function.</dl>
<p> strings</p>
<dl>
<dd>tables of strings, keyed by identifiers assigned during <code>bind</code> and by language IDs provided in control requests</dl>
<p> fs_descriptors</p>
<dl>
<dd>Table of full (or low) speed descriptors, using interface and string identifiers assigned during <i>bind</i>(). If this pointer is null, the function will not be available at full speed (or at low speed).</dl>
<p> hs_descriptors</p>
<dl>
<dd>Table of high speed descriptors, using interface and string identifiers assigned during <i>bind</i>(). If this pointer is null, the function will not be available at high speed.</dl>
<p> ss_descriptors</p>
<dl>
<dd>Table of super speed descriptors, using interface and string identifiers assigned during <i>bind</i>(). If this pointer is null after initiation, the function will not be available at super speed.</dl>
<p> ssp_descriptors</p>
<dl>
<dd>Table of super speed plus descriptors, using interface and string identifiers assigned during <i>bind</i>(). If this pointer is null after initiation, the function will not be available at super speed plus.</dl>
<p> config</p>
<dl>
<dd>assigned when <i>usb_add_function</i>() is called; this is the configuration with which this function is associated.</dl>
<p> os_desc_table</p>
<dl>
<dd>Table of (interface id, os descriptors) pairs. The function can expose more than one interface. If an interface is a member of an IAD, only the first interface of IAD has its entry in the table.</dl>
<p> os_desc_n</p>
<dl>
<dd>Number of entries in os_desc_table</dl>
<p> bind</p>
<dl>
<dd>Before the gadget can register, all of its functions <code>bind</code> to the available resources including string and interface identifiers used in interface or class descriptors; endpoints; I/O buffers; and so on.</dl>
<p> unbind</p>
<dl>
<dd>Reverses <i>bind</i>; called as a side effect of unregistering the driver which added this function.</dl>
<p> free_func</p>
<dl>
<dd>free the struct usb_function.</dl>
<p> mod</p>
<dl>
<dd>(internal) points to the module that created this structure.</dl>
<p> set_alt</p>
<dl>
<dd>(REQUIRED) Reconfigures altsettings; function drivers may initialize usb_ep.driver data at this time (when it is used). Note that setting an interface to its current altsetting resets interface state, and that all interfaces have a disabled state.</dl>
<p> get_alt</p>
<dl>
<dd>Returns the active altsetting. If this is not provided, then only altsetting zero is supported.</dl>
<p> disable</p>
<dl>
<dd>(REQUIRED) Indicates the function should be disabled. Reasons include host resetting or reconfiguring the gadget, and disconnection.</dl>
<p> setup</p>
<dl>
<dd>Used for interface-specific control requests.</dl>
<p> req_match</p>
<dl>
<dd>Tests if a given class request can be handled by this function.</dl>
<p> suspend</p>
<dl>
<dd>Notifies functions when the host stops sending USB traffic.</dl>
<p> resume</p>
<dl>
<dd>Notifies functions when the host restarts USB traffic.</dl>
<p> get_status</p>
<dl>
<dd>Returns function status as a reply to <code>GetStatus</code> request when the recipient is Interface.</dl>
<p> func_suspend</p>
<dl>
<dd>callback to be called when SetFeature(FUNCTION_SUSPEND) is reseived</dl>
<h2>Description</h2>
<p>A single USB function uses one or more interfaces, and should in most cases support operation at both full and high speeds. Each function is associated by <i>usb_add_function</i>() with a one configuration; that function causes <i>bind</i>() to be called so resources can be allocated as part of setting up a gadget driver. Those resources include endpoints, which should be allocated using <i>usb_ep_autoconfig</i>(). </p>
<p> To support dual speed operation, a function driver provides descriptors for both high and full speed operation. Except in rare cases that don&#8217;t involve bulk endpoints, each speed needs different endpoint descriptors. </p>
<p> Function drivers choose their own strategies for managing instance data. The simplest strategy just declares it &quot;static&#8217;, which means the function can only be activated once. If the function needs to be exposed in more than one configuration at a given speed, it needs to support multiple usb_function structures (one for each configuration). </p>
<p> A more complex strategy might encapsulate a <i>usb_function</i> structure inside a driver-specific instance structure to allows multiple activations. An example of multiple activations might be a CDC ACM function that supports two or more distinct instances within the same configuration, providing several independent logical data links to a USB host.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
