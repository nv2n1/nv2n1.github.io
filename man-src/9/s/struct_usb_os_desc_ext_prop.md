---
title: "struct_usb_os_desc_ext_prop(9)"
name: "struct_usb_os_desc_ext_prop"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_os_desc_ext_prop/"
description: "struct_usb_os_desc_ext_prop – describes one “Extended Property”"
---

<p>struct_usb_os_desc_ext_prop &#8211; describes one &#8220;Extended Property&#8221;</p>
<h2>Synopsis</h2>
<pre><code>struct usb_os_desc_ext_prop {
    struct list_head entry;
    u8 type;
    int name_len;
    char *name;
    int data_len;
    char *data;
    struct config_item item;
};</code></pre>
<h2>Members</h2>
<p>entry</p>
<dl>
<dd>used to keep a list of extended properties</dl>
<p> type</p>
<dl>
<dd>Extended Property type</dl>
<p> name_len</p>
<dl>
<dd>Extended Property unicode name length, including terminating &#8216;
