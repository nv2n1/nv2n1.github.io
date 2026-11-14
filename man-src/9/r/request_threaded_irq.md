---
title: "request_threaded_irq(9)"
name: "request_threaded_irq"
section: "9"
letter: "r"
url: "/docs/linux/man/9-request_threaded_irq/"
---

request_threaded_irq - allocate an interrupt line

<h2>Synopsis</h2>

<pre><code>int request_threaded_irq(unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn, unsigned long irqflags, const char *devname, void *dev_id);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line to allocate</dl>
 

 <i>handler</i>
<dl><dd>Function to be called when the IRQ occurs. Primary handler for threaded interrupts If NULL and thread_fn != NULL the default primary handler is installed</dl>
 

 <i>thread_fn</i>
<dl><dd>Function called from the irq handler thread If NULL, no irq thread is created</dl>
 

 <i>irqflags</i>
<dl><dd>Interrupt type flags</dl>
 

 <i>devname</i>
<dl><dd>An ascii name for the claiming device</dl>
 

 <i>dev_id</i>
<dl><dd>A cookie passed back to the handler function</dl>

<h2>Description</h2>

This call allocates interrupt resources and enables the interrupt line and IRQ handling. From the point this call is made your handler function may be invoked. Since your handler function must clear any interrupt the board raises, you must take care both to initialise your hardware and to set up the interrupt handler in the right order. 

 If you want to set up a threaded irq handler for your device then you need to supply <i>handler</i> and <i>thread_fn</i>. <i>handler</i> is still called in hard interrupt context and has to check whether the interrupt originates from the device. If yes it needs to disable the interrupt on the device and return IRQ_WAKE_THREAD which will wake up the handler thread and run <i>thread_fn</i>. This split handler design is necessary to support shared interrupts. 

 Dev_id must be globally unique. Normally the address of the device data structure is used as the cookie. Since the handler receives this value it makes sense to use it. 

 If your interrupt is shared you must pass a non NULL dev_id as this is required when freeing the interrupt. 

 Flags: 

 IRQF_SHARED Interrupt is shared IRQF_TRIGGER_* Specify active edge(s) or level

<h2>Copyright</h2>


