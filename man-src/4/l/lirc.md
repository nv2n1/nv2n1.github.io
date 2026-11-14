---
title: "lirc(4)"
name: "lirc"
section: "4"
letter: "l"
url: "/docs/linux/man/4-lirc/"
description: "lirc – lirc devices"
---

<p>lirc &#8211; lirc devices</p>
<h2>Description</h2>
<p>The <i>/dev/lirc*</i> character devices provide a low-level bidirectional interface to infra-red (IR) remotes. Most of these devices can receive, and some can send. When receiving or sending data, the driver works in two different modes depending on the underlying hardware. </p>
<p> Some hardware (typically TV-cards) decodes the IR signal internally and provides decoded button presses as scancode values. Drivers for this kind of hardware work in <code>LIRC_MODE_SCANCODE</code> mode. Such hardware usually does not support sending IR signals. Furthermore, such hardware can only decode a limited set of IR protocols, usually only the protocol of the specific remote which is bundled with, for example, a TV-card. </p>
<p> Other hardware provides a stream of pulse/space durations. Such drivers work in <code>LIRC_MODE_MODE2</code> mode. Sometimes, this kind of hardware also supports sending IR data. Such hardware can be used with (almost) any kind of remote. This type of hardware can also be used in <code>LIRC_MODE_SCANCODE</code> mode, in which case the kernel IR decoders will decode the IR. These decoders can be written in extended BPF (see <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2)) and attached to the <code>lirc</code> device. </p>
<p> The <code>LIRC_GET_FEATURES</code> ioctl (see below) allows probing for whether receiving and sending is supported, and in which modes, amongst other features.</p>
<h3>Reading input with the LIRC_MODE_MODE2 mode</h3>
<p>In the <code>LIRC_MODE_MODE2 mode</code>, the data returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) provides 32-bit values representing a space or a pulse duration. The time of the duration (microseconds) is encoded in the lower 24 bits. The upper 8 bits indicate the type of package:</p>
<dl>
<dt><code>LIRC_MODE2_SPACE</code></p>
<dd>Value reflects a space duration (microseconds).</p>
<dt><code>LIRC_MODE2_PULSE</code></p>
<dd>Value reflects a pulse duration (microseconds).</p>
<dt><code>LIRC_MODE2_FREQUENCY</code></p>
<dd>Value reflects a frequency (Hz); see the <code>LIRC_SET_MEASURE_CARRIER_MODE</code> ioctl.</p>
<dt><code>LIRC_MODE2_TIMEOUT</code></p>
<dd>Value reflects a space duration (microseconds). The package reflects a timeout; see the <code>LIRC_SET_REC_TIMEOUT_REPORTS</code> ioctl.</dl>
<h3>Reading input with the LIRC_MODE_SCANCODE mode</h3>
<p>In the <code>LIRC_MODE_SCANCODE</code> mode, the data returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) reflects decoded button presses, in the struct <i>lirc_scancode</i>. The scancode is stored in the <i>scancode</i> field, and the IR protocol is stored in <i>rc_proto</i>. This field has one the values of the <i>enum rc_proto</i>.</p>
<h3>Writing output with the LIRC_MODE_PULSE mode</h3>
<p>The data written to the character device using <code><a href="/docs/linux/man/2-write/">write</a></code>(2) is a pulse/space sequence of integer values. Pulses and spaces are only marked implicitly by their position. The data must start and end with a pulse, thus it must always include an odd number of samples. The <code><a href="/docs/linux/man/2-write/">write</a></code>(2) function blocks until the data has been transmitted by the hardware. If more data is provided than the hardware can send, the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) call fails with the error <code>EINVAL</code>.</p>
<h3>Writing output with the LIRC_MODE_SCANCODE mode</h3>
<p>The data written to the character devices must be a single struct <i>lirc_scancode</i>. The <i>scancode</i> and <i>rc_proto</i> fields must filled in, all other fields must be 0. The kernel IR encoders will convert the scancode to pulses and spaces. The protocol or scancode is invalid, or the <code>lirc</code> device cannot transmit.</p>
<h2>Ioctl Commands</h2>
<p>The LIRC device&#8217;s ioctl definition is bound by the ioctl function definition of <i>struct file_operations</i>, leaving us with an <i>unsigned int</i> for the ioctl command and an <i>unsigned long</i> for the argument. For the purposes of ioctl portability across 32-bit and 64-bit architectures, these values are capped to their 32-bit sizes. </p>
<pre>#include &lt;linux/lirc.h&gt; /* But see BUGS */
int ioctl(int fd, int cmd, ...);</pre>
<p>The following ioctls can be used to probe or change specific <code>lirc</code> hardware settings. Many require a third argument, usually an <i>int</i>. referred to below as <i>val</i>.</p>
<h3>Always Supported Commands</h3>
<p><i>/dev/lirc*</i> devices always support the following commands:</p>
<dl>
<dt><code>LIRC_GET_FEATURES</code> (<i>void</i>)</p>
<dd>Returns a bit mask of combined features bits; see FEATURES.</dl>
<p> If a device returns an error code for <code>LIRC_GET_FEATURES</code>, it is safe to assume it is not a <code>lirc</code> device.</p>
<h3>Optional Commands</h3>
<p>Some <code>lirc</code> devices support the commands listed below. Unless otherwise stated, these fail with the error <code>ENOTTY</code> if the operation isn&#8217;t supported, or with the error <code>EINVAL</code> if the operation failed, or invalid arguments were provided. If a driver does not announce support of certain features, invoking the corresponding ioctls will fail with the error <code>ENOTTY</code>.</p>
<dl>
<dt><code>LIRC_GET_REC_MODE</code> (<i>void</i>)</p>
<dd>If the <code>lirc</code> device has no receiver, this operation fails with the error <code>ENOTTY</code>. Otherwise, it returns the receive mode, which will be one of:</p>
<dl>
<dd>
<dl>
<dt><code>LIRC_MODE_MODE2</code></p>
<dd>The driver returns a sequence of pulse/space durations.</p>
<dt><code>LIRC_MODE_SCANCODE</code></p>
<dd>The driver returns struct <i>lirc_scancode</i> values, each of which represents a decoded button press.</dl>
</dl>
<dt><code>LIRC_SET_REC_MODE</code> (<i>int</i>)</p>
<dd>Set the receive mode. <i>val</i> is either <code>LIRC_MODE_SCANCODE</code> or <code>LIRC_MODE_MODE2</code>. If the <code>lirc</code> device has no receiver, this operation fails with the error <code>ENOTTY.</code></p>
<dt><code>LIRC_GET_SEND_MODE</code> (<i>void</i>)</p>
<dd>Return the send mode. <code>LIRC_MODE_PULSE</code> or <code>LIRC_MODE_SCANCODE</code> is supported. If the <code>lirc</code> device cannot send, this operation fails with the error <code>ENOTTY.</code></p>
<dt><code>LIRC_SET_SEND_MODE</code> (<i>int</i>)</p>
<dd>Set the send mode. <i>val</i> is either <code>LIRC_MODE_SCANCODE</code> or <code>LIRC_MODE_PULSE</code>. If the <code>lirc</code> device cannot send, this operation fails with the error <code>ENOTTY</code>.</p>
<dt><code>LIRC_SET_SEND_CARRIER</code> (<i>int</i>)</p>
<dd>Set the modulation frequency. The argument is the frequency (Hz).</p>
<dt><code>LIRC_SET_SEND_DUTY_CYCLE</code> (<i>int</i>)</p>
<dd>Set the carrier duty cycle. <i>val</i> is a number in the range [0,100] which describes the pulse width as a percentage of the total cycle. Currently, no special meaning is defined for 0 or 100, but the values are reserved for future use.</p>
<dd>
<dt><code>LIRC_GET_MIN_TIMEOUT</code> (<i>void</i>),<code> LIRC_GET_MAX_TIMEOUT</code> (<i>void</i>)</p>
<dd>Some devices have internal timers that can be used to detect when there has been no IR activity for a long time. This can help <code><a href="/docs/linux/man/8-lircd/">lircd</a></code>(8) in detecting that an IR signal is finished and can speed up the decoding process. These operations return integer values with the minimum/maximum timeout that can be set (microseconds). Some devices have a fixed timeout. For such drivers, <code>LIRC_GET_MIN_TIMEOUT</code> and <code>LIRC_GET_MAX_TIMEOUT</code> will fail with the error <code>ENOTTY</code>.</p>
<dt><code>LIRC_SET_REC_TIMEOUT</code> (<i>int</i>)</p>
<dd>Set the integer value for IR inactivity timeout (microseconds). To be accepted, the value must be within the limits defined by <code>LIRC_GET_MIN_TIMEOUT</code> and <code>LIRC_GET_MAX_TIMEOUT</code>. A value of 0 (if supported by the hardware) disables all hardware timeouts and data should be reported as soon as possible. If the exact value cannot be set, then the next possible value <i>greater</i> than the given value should be set.</p>
<dt><code>LIRC_GET_REC_TIMEOUT</code> (<i>void</i>)</p>
<dd>Return the current inactivity timeout (microseconds). Available since Linux 4.18.</p>
<dt><code>LIRC_SET_REC_TIMEOUT_REPORTS</code> (<i>int</i>)</p>
<dd>Enable (<i>val</i> is 1) or disable (<i>val</i> is 0) timeout packages in <code>LIRC_MODE_MODE2</code>. The behavior of this operation has varied across kernel versions:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Since Linux 4.16: each time the <code>lirc device is opened,</code> timeout reports are by default enabled for the resulting file descriptor. The <code>LIRC_SET_REC_TIMEOUT</code> operation can be used to disable (and, if desired, to later re-enable) the timeout on the file descriptor.</p>
<dt>*</p>
<dd>In Linux 4.15 and earlier: timeout reports are disabled by default, and enabling them (via <code>LIRC_SET_REC_TIMEOUT</code>) on any file descriptor associated with the <code>lirc</code> device has the effect of enabling timeouts for all file descriptors referring to that device (until timeouts are disabled again).</dl>
</dl>
<dt><code>LIRC_SET_REC_CARRIER</code> (<i>int</i>)</p>
<dd>Set the upper bound of the receive carrier frequency (Hz). See <code>LIRC_SET_REC_CARRIER_RANGE</code>.</p>
<dt><code>LIRC_SET_REC_CARRIER_RANGE</code> (<i>int</i>)</p>
<dd>Sets the lower bound of the receive carrier frequency (Hz). For this to take affect, first set the lower bound using the <code>LIRC_SET_REC_CARRIER_RANGE</code> ioctl, and then the upper bound using the <code>LIRC_SET_REC_CARRIER</code> ioctl.</p>
<dt><code>LIRC_SET_MEASURE_CARRIER_MODE</code> (<i>int</i>)</p>
<dd>Enable (<i>val</i> is 1) or disable (<i>val</i> is 0) the measure mode. If enabled, from the next key press on, the driver will send <code>LIRC_MODE2_FREQUENCY</code> packets. By default, this should be turned off.</p>
<dt><code>LIRC_GET_REC_RESOLUTION</code> (<i>void</i>)</p>
<dd>Return the driver resolution (microseconds).</p>
<dt><code>LIRC_SET_TRANSMITTER_MASK</code> (<i>int</i>)</p>
<dd>Enable the set of transmitters specified in <i>val</i>, which contains a bit mask where each enabled transmitter is a 1. The first transmitter is encoded by the least significant bit, and so on. When an invalid bit mask is given, for example a bit is set even though the device does not have so many transmitters, this operation returns the number of available transmitters and does nothing otherwise.</p>
<dt><code>LIRC_SET_WIDEBAND_RECEIVER</code> (<i>int</i>)</p>
<dd>Some devices are equipped with a special wide band receiver which is intended to be used to learn the output of an existing remote. This ioctl can be used to enable (<i>val</i> equals 1) or disable (<i>val</i> equals 0) this functionality. This might be useful for devices that otherwise have narrow band receivers that prevent them to be used with certain remotes. Wide band receivers may also be more precise. On the other hand, their disadvantage usually is reduced range of reception.</p>
<dd>Note: wide band receiver may be implicitly enabled if you enable carrier reports. In that case, it will be disabled as soon as you disable carrier reports. Trying to disable a wide band receiver while carrier reports are active will do nothing.</dl>
<h2>Features</h2>
<p>the <code>LIRC_GET_FEATURES</code> ioctl returns a bit mask describing features of the driver. The following bits may be returned in the mask:</p>
<dl>
<dt><code>LIRC_CAN_REC_MODE2</code></p>
<dd>The driver is capable of receiving using <code>LIRC_MODE_MODE2</code>.</p>
<dt><code>LIRC_CAN_REC_SCANCODE</code></p>
<dd>The driver is capable of receiving using <code>LIRC_MODE_SCANCODE</code>.</p>
<dt><code>LIRC_CAN_SET_SEND_CARRIER</code></p>
<dd>The driver supports changing the modulation frequency using <code>LIRC_SET_SEND_CARRIER</code>.</p>
<dt><code>LIRC_CAN_SET_SEND_DUTY_CYCLE</code></p>
<dd>The driver supports changing the duty cycle using <code>LIRC_SET_SEND_DUTY_CYCLE</code>.</p>
<dt><code>LIRC_CAN_SET_TRANSMITTER_MASK</code></p>
<dd>The driver supports changing the active transmitter(s) using <code>LIRC_SET_TRANSMITTER_MASK</code>.</p>
<dt><code>LIRC_CAN_SET_REC_CARRIER</code></p>
<dd>The driver supports setting the receive carrier frequency using <code>LIRC_SET_REC_CARRIER</code>. Any <code>lirc</code> device since the drivers were merged in kernel release 2.6.36 must have <code>LIRC_CAN_SET_REC_CARRIER_RANGE</code> set if <code>LIRC_CAN_SET_REC_CARRIER</code> feature is set.</p>
<dt><code>LIRC_CAN_SET_REC_CARRIER_RANGE</code></p>
<dd>The driver supports <code>LIRC_SET_REC_CARRIER_RANGE</code>. The lower bound of the carrier must first be set using the <code>LIRC_SET_REC_CARRIER_RANGE</code> ioctl, before using the <code>LIRC_SET_REC_CARRIER</code> ioctl to set the upper bound.</p>
<dt><code>LIRC_CAN_GET_REC_RESOLUTION</code></p>
<dd>The driver supports <code>LIRC_GET_REC_RESOLUTION</code>.</p>
<dt><code>LIRC_CAN_SET_REC_TIMEOUT</code></p>
<dd>The driver supports <code>LIRC_SET_REC_TIMEOUT</code>.</p>
<dt><code>LIRC_CAN_MEASURE_CARRIER</code></p>
<dd>The driver supports measuring of the modulation frequency using <code>LIRC_SET_MEASURE_CARRIER_MODE</code>.</p>
<dt><code>LIRC_CAN_USE_WIDEBAND_RECEIVER</code></p>
<dd>The driver supports learning mode using <code>LIRC_SET_WIDEBAND_RECEIVER</code>.</p>
<dt><code>LIRC_CAN_SEND_PULSE</code></p>
<dd>The driver supports sending using <code>LIRC_MODE_PULSE</code> or <code>LIRC_MODE_SCANCODE</code></dl>
<h2>Bugs</h2>
<p>Using these devices requires the kernel source header file <i>lirc.h</i>. This file is not available before kernel release 4.6. Users of older kernels could use the file bundled in</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ir-ctl/">ir-ctl</a></code>(1), <code><a href="/docs/linux/man/8-lircd/">lircd</a></code>(8),&nbsp;<code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2) </p>
<p> <a rel="nofollow" href="https://www.kernel.org/doc/html/latest/media/uapi/rc/lirc-dev.html">https://www.kernel.org/doc/html/latest/media/uapi/rc/lirc-dev.html</a></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
