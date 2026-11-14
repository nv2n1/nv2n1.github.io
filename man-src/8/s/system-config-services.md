---
title: "system-config-services(8)"
name: "system-config-services"
section: "8"
letter: "s"
url: "/docs/linux/man/8-system-config-services/"
---

system-config-services - Service Configuration Utility

<h2>Synopsis</h2>

system-config-services

<h2>Description</h2>

This is a graphical tool for enabling and disabling services (including xinetd services). Functionality to start, stop, and restart services is also included.

<h2>Options</h2>

None

<h2>Files</h2>

<pre><i>/usr/bin/system-config-services</i>
<i>/usr/share/system-config-services/*</i></pre>

<h2>Examples</h2>

To run this program simply type: system-config-services 

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-chkconfig/">chkconfig</a>(8)</i> <i><a HREF="/docs/linux/man/8-ntsysv/">ntsysv</a>(8)</i> 

<h2>Bugs</h2>

- Some services will not start or stop properly if started anywhere but the console (system-config-services will appear to hang in these instances). This is not a bug in system-config-services, but in the individual services. - Some services are incredibly hard to detect if they are running or not. While there are workarounds present to deal with these, it can't be guaranteed that they're detected properly. Please file bugs against the system-config-services component at <a rel="nofollow" HREF="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> if you encounter such services. 

<h2>Authors</h2>

<pre>Tim Powers &lt;timp [at] redhat.com&gt;
Bill Nottingham &lt;notting [at] redhat.com&gt;
Dan Walsh &lt;dwalsh [at] redhat.com&gt;
Nils Philippsen &lt;nils [at] redhat.com&gt;</pre>
