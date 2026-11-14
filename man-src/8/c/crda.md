---
title: "crda(8)"
name: "crda"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crda/"
description: "crda – send to the kernel a wireless regulatory domain for a given ISO / IEC 3166 alpha2"
---

<p>crda &#8211; send to the kernel a wireless regulatory domain for a given ISO / IEC 3166 alpha2</p>
<h2>Synopsis</h2>
<p><code>crda</code> </p>
<h2>Description</h2>
</h3>
<p><code>crda</code> is the Linux wireless central regulatory domain agent. <code>crda</code> is intended to be used by <code>udev</code> scripts and should not be run manually unless debugging udev scripts. <code>crda</code> is triggered to run by the kernel by sending a <code>udev</code> event upon a new regulatory domain change. Regulatory domain changes are triggered by the wireless kernel subsystem (upon initialization and on reception of country IEs), wireless drivers, or userspace (see <code>iw</code> ). Upon a regulatory domain change the kernel sends a udev change event for the regulatory platform. The kernel ignores regulatory domains sent to it if it does not expect them. The regulatory domain is read by crda from the <code>regulatory.bin</code> file. </p>
<h2>RSA Digital Signature</h2>
</h3>
<p>If built with openssl or gcrypt support <code>crda</code> will have embedded into it an RSA digital signature which will prevent it from reading corrupted or non-authored <code>regulatory.bin</code> files. Authorship is respected by the RSA public key packed into <code>crda.</code> <i>This</i> specific <code>crda</code> package has been built with RSA public keys from <i>John Linville (the Linux wireless kernel maintainer)</i> and <i>Seth Forshee (the wireless regulatory databse maintainer)</i> and as such will only read <code>regulatory.bin</code> files signed by one of them. For further information see the <code>regulatory.bin</code> man page.</p>
<h3>
<h2>Udev Rule</h2>
</h3>
<p>A udev regulatory rule must be put in place in order to receive and parse udev events from the kernel in order to get udev to call crda with the passed ISO / IEC 3166 alpha2 country code. An example udev rule which can be used (usually in <code>/lib/udev/rules.d/85-regulatory.rules</code> ): </p>
<p> <i>KERNEL==regulatory*, ACTION==change, SUBSYSTEM==platform, RUN+=/sbin/crda</i></p>
<h3>
<h2>Environment variable</h2>
</h3>
<p>Set the <code>COUNTRY</code> environment variable with a specific ISO / IEC 3166 alpha2 country code and then run <code>crda</code> without arguments. This will send a regulatory domain for that alpha2 to the kernel.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iw/">iw</a></code>(8) <code><a href="/docs/linux/man/5-regulatory-bin/">regulatory.bin</a></code>(5) <code><a rel="nofollow" href="http://wireless.kernel.org/en/developers/Regulatory/">http://wireless.kernel.org/en/developers/Regulatory/</a></code> </p>
