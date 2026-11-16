---
title: "struct_usb_os_desc(9)"
name: "struct_usb_os_desc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_os_desc/"
description: "struct_usb_os_desc – describes OS descriptors associated with one interface"
---

<p>struct_usb_os_desc &#8211; describes OS descriptors associated with one interface</p>
<h2>Synopsis</h2>
<pre><code>struct usb_os_desc {
    char *ext_compat_id;
    struct list_head ext_prop;
    int ext_prop_len;
    int ext_prop_count;
    struct mutex *opts_mutex;
    struct config_group group;
    struct module *owner;
};</code></pre>
<h2>Members</h2>
<p>ext_compat_id</p>
<dl>
<dd>16 bytes of &#8220;Compatible ID&#8221; and &#8220;Subcompatible ID&#8221;</dd></dl>
<p> ext_prop</p>
<dl>
<dd>Extended Properties list</dd></dl>
<p> ext_prop_len</p>
<dl>
<dd>Total length of Extended Properties blobs</dd></dl>
<p> ext_prop_count</p>
<dl>
<dd>Number of Extended Properties</dd></dl>
<p> opts_mutex</p>
<dl>
<dd>Optional mutex protecting config data of a usb_function_instance</dd></dl>
<p> group</p>
<dl>
<dd>Represents OS descriptors associated with an interface in configfs</dd></dl>
<p> owner</p>
<dl>
<dd>Module associated with this OS descriptor</dd></dl>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
