---
title: "usb_set_device_state(9)"
name: "usb_set_device_state"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_set_device_state/"
---

usb_set_device_state - change a device's current state (usbcore, hcds)

<h2>Synopsis</h2>

<pre><code>void usb_set_device_state(struct usb_device *udev, enum usb_device_state new_state);</code></pre>

<h2>Arguments</h2>

<i>udev</i>
<dl><dd><dd>pointer to device whose state should be changed</dl>
 

 <i>new_state</i>
<dl><dd>new state value to be stored</dl>

<h2>Description</h2>

udev-&gt;state is _not_ fully protected by the device lock. Although most transitions are made only while holding the lock, the state can can change to USB_STATE_NOTATTACHED at almost any time. This is so that devices can be marked as disconnected as soon as possible, without having to wait for any semaphores to be released. As a result, all changes to any device's state must be protected by the device_state_lock spinlock. 

 Once a device has been added to the device tree, all changes to its state should be made using this routine. The state should _not_ be set directly. 

 If udev-&gt;state is already USB_STATE_NOTATTACHED then no change is made. Otherwise udev-&gt;state is set to new_state, and if new_state is USB_STATE_NOTATTACHED then all of udev's descendants' states are also set to USB_STATE_NOTATTACHED.

<h2>Copyright</h2>


