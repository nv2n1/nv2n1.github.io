---
title: "struct_iio_dev(9)"
name: "struct_iio_dev"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_iio_dev/"
description: "struct_iio_dev – industrial I/O device"
---

<p>struct_iio_dev &#8211; industrial I/O device</p>
<h2>Synopsis</h2>
<pre><code>struct iio_dev {
    int id;
    int modes;
    int currentmode;
    struct device dev;
    struct iio_event_interface *event_interface;
    struct iio_buffer *buffer;
    struct list_head buffer_list;
    int scan_bytes;
    struct mutex mlock;
    const unsigned long *available_scan_masks;
    unsigned masklength;
    const unsigned long *active_scan_mask;
    bool scan_timestamp;
    unsigned scan_index_timestamp;
    struct iio_trigger *trig;
    struct iio_poll_func *pollfunc;
    struct iio_poll_func *pollfunc_event;
    struct iio_chan_spec const *channels;
    int num_channels;
    struct list_head channel_attr_list;
    struct attribute_group chan_attr_group;
    const char *name;
    const struct iio_info *info;
    clockid_t clock_id;
    struct mutex info_exist_lock;
    const struct iio_buffer_setup_ops *setup_ops;
    struct cdev chrdev;
#define IIO_MAX_GROUPS 6
    const struct attribute_group *groups[IIO_MAX_GROUPS + 1];
    int groupcounter;
    unsigned long flags;
#if defined(CONFIG_DEBUG_FS)
    struct dentry *debugfs_dentry;
    unsigned cached_reg_addr;
#endif
};</code></pre>
<h2>Members</h2>
<p>id</p>
<dl>
<dd>[INTERN] used to identify device internally</dl>
<p> modes</p>
<dl>
<dd>[DRIVER] operating modes supported by device</dl>
<p> currentmode</p>
<dl>
<dd>[DRIVER] current operating mode</dl>
<p> dev</p>
<dl>
<dd>[DRIVER] device structure, should be assigned a parent and owner</dl>
<p> event_interface</p>
<dl>
<dd>[INTERN] event chrdevs associated with interrupt lines</dl>
<p> buffer</p>
<dl>
<dd>[DRIVER] any buffer present</dl>
<p> buffer_list</p>
<dl>
<dd>[INTERN] list of all buffers currently attached</dl>
<p> scan_bytes</p>
<dl>
<dd>[INTERN] num bytes captured to be fed to buffer demux</dl>
<p> mlock</p>
<dl>
<dd>[DRIVER] lock used to prevent simultaneous device state changes</dl>
<p> available_scan_masks</p>
<dl>
<dd>[DRIVER] optional array of allowed bitmasks</dl>
<p> masklength</p>
<dl>
<dd>[INTERN] the length of the mask established from channels</dl>
<p> active_scan_mask</p>
<dl>
<dd>[INTERN] union of all scan masks requested by buffers</dl>
<p> scan_timestamp</p>
<dl>
<dd>[INTERN] set if any buffers have requested timestamp</dl>
<p> scan_index_timestamp</p>
<dl>
<dd>[INTERN] cache of the index to the timestamp</dl>
<p> trig</p>
<dl>
<dd>[INTERN] current device trigger (buffer modes) <i>trig_readonly</i> [INTERN] mark the current trigger immutable</dl>
<p> pollfunc</p>
<dl>
<dd>[DRIVER] function run on trigger being received</dl>
<p> pollfunc_event</p>
<dl>
<dd>[DRIVER] function run on events trigger being received</dl>
<p> channels</p>
<dl>
<dd>[DRIVER] channel specification structure table</dl>
<p> num_channels</p>
<dl>
<dd>[DRIVER] number of channels specified in <i>channels</i>.</dl>
<p> channel_attr_list</p>
<dl>
<dd>[INTERN] keep track of automatically created channel attributes</dl>
<p> chan_attr_group</p>
<dl>
<dd>[INTERN] group for all attrs in base directory</dl>
<p> name</p>
<dl>
<dd>[DRIVER] name of the device.</dl>
<p> info</p>
<dl>
<dd>[DRIVER] callbacks and constant info from driver</dl>
<p> clock_id</p>
<dl>
<dd>[INTERN] timestamping clock posix identifier</dl>
<p> info_exist_lock</p>
<dl>
<dd>[INTERN] lock to prevent use during removal</dl>
<p> setup_ops</p>
<dl>
<dd>[DRIVER] callbacks to call before and after buffer enable/disable</dl>
<p> chrdev</p>
<dl>
<dd>[INTERN] associated character device</dl>
<p> groups[IIO_MAX_GROUPS + 1]</p>
<dl>
<dd>[INTERN] attribute groups</dl>
<p> groupcounter</p>
<dl>
<dd>[INTERN] index of next attribute group</dl>
<p> flags</p>
<dl>
<dd>[INTERN] file ops related flags including busy flag.</dl>
<p> debugfs_dentry</p>
<dl>
<dd>[INTERN] device specific debugfs dentry.</dl>
<p> cached_reg_addr</p>
<dl>
<dd>[INTERN] cached register address for debugfs reads.</dl>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
