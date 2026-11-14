---
title: "struct_w1_master(9)"
name: "struct_w1_master"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_master/"
description: "struct_w1_master – one per bus master"
---

<p>struct_w1_master &#8211; one per bus master</p>
<h2>Synopsis</h2>
<pre><code>struct w1_master {
    struct list_head w1_master_entry;
    struct module *owner;
    unsigned char name[W1_MAXNAMELEN];
    struct mutex list_mutex;
    struct list_head slist;
    struct list_head async_list;
    int max_slave_count;
    int slave_count;
    unsigned long attempts;
    int slave_ttl;
    int initialized;
    u32 id;
    int search_count;
    u64 search_id;
    atomic_t refcnt;
    void *priv;
    int enable_pullup;
    int pullup_duration;
    long flags;
    struct task_struct *thread;
    struct mutex mutex;
    struct mutex bus_mutex;
    struct device_driver *driver;
    struct device dev;
    struct w1_bus_master *bus_master;
    u32 seq;
};</code></pre>
<h2>Members</h2>
<p>w1_master_entry</p>
<dl>
<dd>master linked list</dl>
<p> owner</p>
<dl>
<dd>module owner</dl>
<p> name[W1_MAXNAMELEN]</p>
<dl>
<dd>dynamically allocate bus name</dl>
<p> list_mutex</p>
<dl>
<dd>protect slist and async_list</dl>
<p> slist</p>
<dl>
<dd>linked list of slaves</dl>
<p> async_list</p>
<dl>
<dd>linked list of netlink commands to execute</dl>
<p> max_slave_count</p>
<dl>
<dd>maximum number of slaves to search for at a time</dl>
<p> slave_count</p>
<dl>
<dd>current number of slaves known</dl>
<p> attempts</p>
<dl>
<dd>number of searches ran</dl>
<p> slave_ttl</p>
<dl>
<dd>number of searches before a slave is timed out</dl>
<p> initialized</p>
<dl>
<dd>prevent init/removal race conditions</dl>
<p> id</p>
<dl>
<dd>w1 bus number</dl>
<p> search_count</p>
<dl>
<dd>number of automatic searches to run, -1 unlimited</dl>
<p> search_id</p>
<dl>
<dd>allows continuing a search</dl>
<p> refcnt</p>
<dl>
<dd>reference count</dl>
<p> priv</p>
<dl>
<dd>private data storage</dl>
<p> enable_pullup</p>
<dl>
<dd>allows a strong pullup</dl>
<p> pullup_duration</p>
<dl>
<dd>time for the next strong pullup</dl>
<p> flags</p>
<dl>
<dd>one of w1_master_flags</dl>
<p> thread</p>
<dl>
<dd>thread for bus search and netlink commands</dl>
<p> mutex</p>
<dl>
<dd>protect most of w1_master</dl>
<p> bus_mutex</p>
<dl>
<dd>pretect concurrent bus access</dl>
<p> driver</p>
<dl>
<dd>sysfs driver</dl>
<p> dev</p>
<dl>
<dd>sysfs device</dl>
<p> bus_master</p>
<dl>
<dd>io operations available</dl>
<p> seq</p>
<dl>
<dd>sequence number used for netlink broadcasts</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
