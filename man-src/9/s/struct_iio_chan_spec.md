---
title: "struct_iio_chan_spec(9)"
name: "struct_iio_chan_spec"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_iio_chan_spec/"
description: "struct_iio_chan_spec – specification of a single channel"
---

<p>struct_iio_chan_spec &#8211; specification of a single channel</p>
<h2>Synopsis</h2>
<pre><code>struct iio_chan_spec {
    enum iio_chan_type type;
    int channel;
    int channel2;
    unsigned long address;
    int scan_index;
    struct scan_type;
    long info_mask_separate;
    long info_mask_shared_by_type;
    long info_mask_shared_by_dir;
    long info_mask_shared_by_all;
    const struct iio_event_spec *event_spec;
    unsigned int num_event_specs;
    const struct iio_chan_spec_ext_info *ext_info;
    const char *extend_name;
    const char *datasheet_name;
    unsigned modified : 1;
    unsigned indexed : 1;
    unsigned output : 1;
    unsigned differential : 1;
};</code></pre>
<h2>Members</h2>
<p>type</p>
<dl>
<dd>What type of measurement is the channel making.</dl>
<p> channel</p>
<dl>
<dd>What number do we wish to assign the channel.</dl>
<p> channel2</p>
<dl>
<dd>If there is a second number for a differential channel then this is it. If modified is set then the value here specifies the modifier.</dl>
<p> address</p>
<dl>
<dd>Driver specific identifier.</dl>
<p> scan_index</p>
<dl>
<dd>Monotonic index to give ordering in scans when read from a buffer.</dl>
<p> scan_type</p>
<dl>
<dd>sign: &#8216;s&#8217; or &#8216;u&#8217; to specify signed or unsigned realbits: Number of valid bits of data storagebits: Realbits + padding shift: Shift right by this before masking out realbits. repeat: Number of times real/storage bits repeats. When the repeat element is more than 1, then the type element in sysfs will show a repeat value. Otherwise, the number of repetitions is omitted. endianness: little or big endian</dl>
<p> info_mask_separate</p>
<dl>
<dd>What information is to be exported that is specific to this channel.</dl>
<p> info_mask_shared_by_type</p>
<dl>
<dd>What information is to be exported that is shared by all channels of the same type.</dl>
<p> info_mask_shared_by_dir</p>
<dl>
<dd>What information is to be exported that is shared by all channels of the same direction.</dl>
<p> info_mask_shared_by_all</p>
<dl>
<dd>What information is to be exported that is shared by all channels.</dl>
<p> event_spec</p>
<dl>
<dd>Array of events which should be registered for this channel.</dl>
<p> num_event_specs</p>
<dl>
<dd>Size of the event_spec array.</dl>
<p> ext_info</p>
<dl>
<dd>Array of extended info attributes for this channel. The array is NULL terminated, the last element should have its name field set to NULL.</dl>
<p> extend_name</p>
<dl>
<dd>Allows labeling of channel attributes with an informative name. Note this has no effect codes etc, unlike modifiers.</dl>
<p> datasheet_name</p>
<dl>
<dd>A name used in in-kernel mapping of channels. It should correspond to the first name that the channel is referred to by in the datasheet (e.g. IND), or the nearest possible compound name (e.g. IND-INC).</dl>
<p> modified</p>
<dl>
<dd>Does a modifier apply to this channel. What these are depends on the channel type. Modifier is set in channel2. Examples are IIO_MOD_X for axial sensors about the &#8216;x&#8217; axis.</dl>
<p> indexed</p>
<dl>
<dd>Specify the channel has a numerical index. If not, the channel index number will be suppressed for sysfs attributes but not for event codes.</dl>
<p> output</p>
<dl>
<dd>Channel is output.</dl>
<p> differential</p>
<dl>
<dd>Channel is differential.</dl>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
