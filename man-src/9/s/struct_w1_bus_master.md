---
title: "struct_w1_bus_master(9)"
name: "struct_w1_bus_master"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_bus_master/"
description: "struct_w1_bus_master – operations available on a bus master"
---

<p>struct_w1_bus_master &#8211; operations available on a bus master</p>
<h2>Synopsis</h2>
<pre><code>struct w1_bus_master {
    void *data;
    u8 (*read_bit)(void *);
    void (*write_bit)(void *, u8);
    u8 (*touch_bit)(void *, u8);
    u8 (*read_byte)(void *);
    void (*write_byte)(void *, u8);
    u8 (*read_block)(void *, u8 *, int);
    void (*write_block)(void *, const u8 *, int);
    u8 (*triplet)(void *, u8);
    u8 (*reset_bus)(void *);
    u8 (*set_pullup)(void *, int);
    void (*search)(void *, struct w1_master *, u8, w1_slave_found_callback);
};</code></pre>
<h2>Members</h2>
<p>data</p>
<dl>
<dd>the first parameter in all the functions below</dl>
<p> read_bit</p>
<dl>
<dd>Sample the line level <i>return</i> the level read (0 or 1)</dl>
<p> write_bit</p>
<dl>
<dd>Sets the line level</dl>
<p> touch_bit</p>
<dl>
<dd>the lowest-level function for devices that really support the 1-wire protocol. touch_bit(0) = write-0 cycle <a href="/docs/linux/man/1-touch_bit/">touch_bit</a>(1) = write-1 / read cycle <i>return</i> the bit read (0 or 1)</dl>
<p> read_byte</p>
<dl>
<dd>Reads a bytes. Same as 8 <a href="/docs/linux/man/1-touch_bit/">touch_bit</a>(1) calls. <i>return</i> the byte read</dl>
<p> write_byte</p>
<dl>
<dd>Writes a byte. Same as 8 touch_bit(x) calls.</dl>
<p> read_block</p>
<dl>
<dd>Same as a series of <code>read_byte</code> calls <i>return</i> the number of bytes read</dl>
<p> write_block</p>
<dl>
<dd>Same as a series of <code>write_byte</code> calls</dl>
<p> triplet</p>
<dl>
<dd>Combines two reads and a smart write for ROM searches <i>return</i> bit0=Id bit1=comp_id bit2=dir_taken</dl>
<p> reset_bus</p>
<dl>
<dd>long write-0 with a read for the presence pulse detection <i>return</i> -1=Error, 0=Device present, 1=No device present</dl>
<p> set_pullup</p>
<dl>
<dd>Put out a strong pull-up pulse of the specified duration. <i>return</i> -1=Error, 0=completed</dl>
<p> search</p>
<dl>
<dd>Really nice hardware can handles the different types of ROM search w1_master* is passed to the slave found callback. u8 is search_type, W1_SEARCH or W1_ALARM_SEARCH</dl>
<h2>Note</h2>
<p>read_bit and write_bit are very low level functions and should only be used with hardware that doesn&#8217;t really support 1-wire operations, like a parallel/serial port. Either define read_bit and write_bit OR define, at minimum, touch_bit and reset_bus.</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
