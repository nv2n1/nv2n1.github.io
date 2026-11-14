---
title: "usb_hcd_resume_root_hub(9)"
name: "usb_hcd_resume_root_hub"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_resume_root_hub/"
---

usb_hcd_resume_root_hub - called by HCD to resume its root hub

<h2>Synopsis</h2>

<pre><code>void usb_hcd_resume_root_hub(struct usb_hcd *hcd);</code></pre>

<h2>Arguments</h2>

<i>hcd</i>
<dl><dd><dd>host controller for this root hub</dl>

<h2>Description</h2>

The USB host controller calls this function when its root hub is suspended (with the remote wakeup feature enabled) and a remote wakeup request is received. The routine submits a workqueue request to resume the root hub (that is, manage its downstream ports again).

<h2>Copyright</h2>


