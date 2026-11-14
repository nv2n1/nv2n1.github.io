---
title: "struct_w1_slave(9)"
name: "struct_w1_slave"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_slave/"
description: "struct_w1_slave – holds a single slave device on the bus"
---

<p>struct_w1_slave &#8211; holds a single slave device on the bus</p>
<h2>Synopsis</h2>
<pre><code>struct w1_slave {
    struct module *owner;
    unsigned char name[W1_MAXNAMELEN];
    struct list_head w1_slave_entry;
    struct w1_reg_num reg_num;
    atomic_t refcnt;
    int ttl;
    unsigned long flags;
    struct w1_master *master;
    struct w1_family *family;
    void *family_data;
    struct device dev;
};</code></pre>
<h2>Members</h2>
<p>owner</p>
<dl>
<dd>Points to the one wire &#8220;wire&#8221; kernel module.</dl>
<p> name[W1_MAXNAMELEN]</p>
<dl>
<dd>Device id is ascii.</dl>
<p> w1_slave_entry</p>
<dl>
<dd>data for the linked list</dl>
<p> reg_num</p>
<dl>
<dd>the slave id in binary</dl>
<p> refcnt</p>
<dl>
<dd>reference count, delete when 0</dl>
<p> ttl</p>
<dl>
<dd>decrement per search this slave isn&#8217;t found, deatch at 0</dl>
<p> flags</p>
<dl>
<dd>bit flags for W1_SLAVE_ACTIVE W1_SLAVE_DETACH</dl>
<p> master</p>
<dl>
<dd>bus which this slave is on</dl>
<p> family</p>
<dl>
<dd>module for device family type</dl>
<p> family_data</p>
<dl>
<dd>pointer for use by the family module</dl>
<p> dev</p>
<dl>
<dd>kernel device identifier</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
