---
title: "polkit(8)"
name: "polkit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-polkit/"
description: "polkit – Authorization Framework"
---

<p>polkit &#8211; Authorization Framework</p>
<h2>Overview</h2>
<p>PolicyKit provides an authorization API intended to be used by privileged programs (&#8220;MECHANISMS&#8221;) offering service to unprivileged programs (&#8220;CLIENTS&#8221;) through some form of IPC mechanism such as D-Bus or Unix pipes. In this scenario, the mechanism typically treats the client as untrusted. For every request from a client, the mechanism needs to determine if the request is authorized or if it should refuse to service the client. Using the PolicyKit API, a mechanism can offload this decision to a trusted party: The PolicyKit Authority. </p>
<p> In addition to acting as an authority, PolicyKit allows users to obtain temporary authorization through authenticating either an administrative user or the owner of the session the client belongs to. This is useful for scenarios where a mechanism needs to verify that the operator of the system really is the user or really is an administrative user.</p>
<h2>System Architecture</h2>
<p>The system architecture of PolicyKit is comprised of the <i>Authority</i> (implemented as a service on the system message bus) and a <i>Authentication Agent</i> per user session (provided and started by the user session e.g. GNOME or KDE). Additionally, PolicyKit supports a number of extension points &#8211; specifically, vendors and/or sites can write extensions to completely control authorization policy. In a block diagram, the architecture looks like this: </p>
<dl>
<dd>[IMAGE]<font SIZE="-2">[1]</font> </p>
<dl>
<dd>
<pre> +-------------------+
 | Authentication |
 | Agent |
 +-------------------+
 | libpolkit-agent-1 |
 +-------------------+
 ^ +--------+
 | | Client |
 +--------------+ +--------+
 | ^
 | |
User Session | |
=======================|========================|=============
System Context | |
 | |
 | +---+
 V |
 /------------\ |
 | System Bus | |
 \------------/ |
 ^ ^ V
 | | +---------------------+
 +--------------+ | | Mechanism |
 | | +---------------------+
 V +----&gt; | libpolkit-gobject-1 |
+------------------+ +---------------------+
| org.freedesktop. |
| PolicyKit1 |
+------------------+
| Backends and |
| Extensions |
+------------------+</pre>
</dl>
</dl>
<p> For convenience, the libpolkit-gobject-1 library wraps the PolicyKit D-Bus API using GObject. However, a mechanism can also use the D-Bus API or the <code><a href="/docs/linux/man/1-pkcheck/">pkcheck</a></code>(1) command to check authorizations. </p>
<p> The libpolkit-agent-1 library provides an abstraction of the native authentication system, e.g. <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) and also facilities registration and communication with the PolicyKit D-Bus service. </p>
<p> See the m[blue]<code>developer documentation</code>m[]<font SIZE="-2">[2]</font> for more information about using and extending PolicyKit. </p>
<p> See <code><a href="/docs/linux/man/8-pklocalauthority/">pklocalauthority</a></code>(8) for information about the Local Authority &#8211; the default authority implementation shipped with PolicyKit.</p>
<h2>Authentication Agents</h2>
<p>An authentication agent is used to make the user of a session prove that the user of the session really is the user (by authenticating as the user) or an administrative user (by authenticating as a administrator). In order to integrate well with the rest of the user session (e.g. match the look and feel), authentication agents are meant to be provided by the user session that the user uses. For example, an authentication agent may look like this: </p>
<dl>
<dd>[IMAGE]<font SIZE="-2">[3]</font> </p>
<dl>
<dd>
<pre>+----------------------------------------------------------+
| Authenticate [X] |
+----------------------------------------------------------+
| |
| [Icon] Authentication is required to run ATA SMART |
| self tests |
| |
| An application is attempting to perform an |
| action that requires privileges. Authentication |
| as the super user is required to perform this |
| action. |
| |
| Password for root: [_________________________] |
| |
| [V] Details: |
| Drive: ATA INTEL SSDSA2MH08 (045C) |
| Device: /dev/sda |
| Action: org.fd.devicekit.disks.drive-ata-smart-selftest |
| Vendor: The DeviceKit Project |
| |
| [Cancel] [Authenticate] |
+----------------------------------------------------------+</pre>
</dl>
</dl>
<p> If the system is configured without a <i>root</i> account it may allow you to select the administrative user who is authenticating: </p>
<dl>
<dd>[IMAGE]<font SIZE="-2">[4]</font> </p>
<dl>
<dd>
<pre>+----------------------------------------------------------+
| Authenticate [X] |
+----------------------------------------------------------+
| |
| [Icon] Authentication is required to run ATA SMART |
| self tests |
| |
| An application is attempting to perform an |
| action that requires privileges. Authentication |
| as one of the users below is required to |
| perform this action. |
| |
| [[Face] Patrick Bateman (bateman) [V]] |
| |
| Password for bateman: [______________________] |
| |
| [V] Details: |
| Drive: ATA INTEL SSDSA2MH08 (045C) |
| Device: /dev/sda |
| Action: org.fd.devicekit.disks.drive-ata-smart-selftest |
| Vendor: The DeviceKit Project |
| |
| [Cancel] [Authenticate] |
+----------------------------------------------------------+</pre>
</dl>
</dl>
<p> See <code><a href="/docs/linux/man/8-pklocalauthority/">pklocalauthority</a></code>(8) on how to set up the local authority implemention for systems without a root account. </p>
<p> Applications that do not run under a desktop environment (for example, if launched from a <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) login) may not have have an authentication agent associated with them. Such applications may use the PolkitAgentTextListener type or the <code><a href="/docs/linux/man/1-pkttyagent/">pkttyagent</a></code>(1) helper so the user can authenticate using a textual interface.</p>
<h2>Declaring Actions</h2>
<p>A mechanism need to declare a set of &#8220;ACTIONS&#8221; in order to use PolicyKit. Actions correspond to operations that clients can request the mechanism to carry out and are defined in XML files that the mechanism installs into the /usr/share/polkit-1/actions directory. </p>
<p> PolicyKit actions are namespaced and can only contain the characters [a-z][0-9].- e.g. lower-case ASCII, digits, period and hyphen. Each XML file can contain more than one action but all actions need to be in the same namespace and the file needs to be named after the namespace and have the extension .policy. </p>
<p> The XML file must have the following doctype declaration </p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;!DOCTYPE policyconfig PUBLIC &quot;-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN&quot;
&quot;<a rel="nofollow" href="http://www.freedesktop.org/standards/PolicyKit/1.0/policyconfig.dtd">http://www.freedesktop.org/standards/PolicyKit/1.0/policyconfig.dtd</a>&quot;&gt;</pre>
</dl>
<p> The <i>policyconfig</i> element must be present exactly once. Elements that can be used inside <i>policyconfig</i> includes: </p>
<p> <i>vendor</i></p>
<dl>
<dd>The name of the project or vendor that is supplying the actions in the XML document. Optional.</dl>
<p> <i>vendor_url</i></p>
<dl>
<dd>A URL to the project or vendor that is supplying the actions in the XML document. Optional.</dl>
<p> <i>icon_name</i></p>
<dl>
<dd>An icon representing the project or vendor that is supplying the actions in the XML document. The icon name must adhere to the m[blue]<code>Freedesktop.org Icon Naming Specification</code>m[]<font SIZE="-2">[5]</font>. Optional.</dl>
<p> <i>action</i></p>
<dl>
<dd>Declares an action. The action name is specified using the id attribute and can only contain the characters [a-z][0-9].- e.g. lower-case ASCII, digits, period and hyphen.</dl>
<p> Elements that can be used inside <i>action</i> includes: </p>
<p> <i>description</i></p>
<dl>
<dd>A human readable description of the action, e.g. &#8220;Install unsigned software&#8221;.</dl>
<p> <i>message</i></p>
<dl>
<dd>A human readable message displayed to the user when asking for credentials when authentication is needed, e.g. &#8220;Installing unsigned software requires authentication&#8221;.</dl>
<p> <i>defaults</i></p>
<dl>
<dd>This element is used to specify implicit authorizations for clients. </p>
<p> Elements that can be used inside <i>defaults</i> includes: </p>
<p> <i>allow_any</i></p>
<dl>
<dd>Implicit authorizations that apply to any client. Optional.</dl>
<p> <i>allow_inactive</i></p>
<dl>
<dd>Implicit authorizations that apply to clients in inactive sessions on local consoles. Optional.</dl>
<p> <i>allow_active</i></p>
<dl>
<dd>Implicit authorizations that apply to clients in active sessions on local consoles. Optional.</dl>
<p> Each of the <i>allow_any</i>, <i>allow_inactive</i> and <i>allow_active</i> elements can contain the following values: </p>
<p> no</p>
<dl>
<dd>Not authorized.</dl>
<p> yes</p>
<dl>
<dd>Authorized.</dl>
<p> auth_self</p>
<dl>
<dd>Authentication by the owner of the session that the client originates from is required.</dl>
<p> auth_admin</p>
<dl>
<dd>Authentication by an administrative user is required.</dl>
<p> auth_self_keep</p>
<dl>
<dd>Like auth_self but the authorization is kept for a brief period.</dl>
<p> auth_admin_keep</p>
<dl>
<dd>Like auth_admin but the authorization is kept for a brief period.</dl>
</dl>
<p> <i>annotate</i></p>
<dl>
<dd>Used for annotating an action with a key/value pair. The key is specified using the the key attribute and the value is specified using the value attribute. This element may appear zero or more times. See below for known annotations.</dl>
<p> <i>vendor</i></p>
<dl>
<dd>Used for overriding the vendor on a per-action basis. Optional.</dl>
<p> <i>vendor_url</i></p>
<dl>
<dd>Used for overriding the vendor URL on a per-action basis. Optional.</dl>
<p> <i>icon_name</i></p>
<dl>
<dd>Used for overriding the icon name on a per-action basis. Optional.</dl>
<p> For localization, <i>description</i> and <i>message</i> elements may occur multiple times with different xml:lang attributes. </p>
<p> To list installed PolicyKit actions, use the <code><a href="/docs/linux/man/1-pkaction/">pkaction</a></code>(1) command.</p>
<h3>Known annotations</h3>
<p>The org.freedesktop.policykit.exec.path annotation is used by the <code>pkexec</code> program shipped with PolicyKit &#8211; see the <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1) man page for details. </p>
<p> The org.freedesktop.policykit.imply annotation (its value is a string containing a space separated list of action identifiers) can be used to define <i>meta actions</i>. The way it works is that if a subject is authorized for an action with this annotation, then it is also authorized for any action specified by the annotation. A typical use of this annotation is when defining an UI shell with a single lock button that should unlock multiple actions from distinct mechanisms. </p>
<p> The org.freedesktop.policykit.owner annotation can be used to define a set of users who can query whether a client is authorized to perform this action. If this annotation is not specified then only root can query whether a client running as a different user is authorized for an action. The value of this annotation is a string containing a space separated list of PolkitIdentity entries, for example &quot;unix-user:42 unix-user:colord&quot;. A typical use of this annotation is for a daemon process that runs as a system user rather than root.</p>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the polkit-devel mailing list, see the link m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/polkit-devel">http://lists.freedesktop.org/mailman/listinfo/polkit-devel</a></code>m[] on how to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pklocalauthority/">pklocalauthority</a></code>(8) <code><a href="/docs/linux/man/8-polkitd/">polkitd</a></code>(8) <code><a href="/docs/linux/man/1-pkaction/">pkaction</a></code>(1), <code><a href="/docs/linux/man/1-pkcheck/">pkcheck</a></code>(1), <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), <code><a href="/docs/linux/man/1-pkttyagent/">pkttyagent</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>/usr/share/gtk-doc/html/polkit-1/polkit-architecture.png</p>
<dt> 2.</p>
<dd>developer documentation</p>
<dl>
<dd>file:///usr/share/gtk-doc/html/polkit-1/index.html</dl>
<dt> 3.</p>
<dd>/usr/share/gtk-doc/html/polkit-1/polkit-authentication-agent-example.png</p>
<dt> 4.</p>
<dd>/usr/share/gtk-doc/html/polkit-1/polkit-authentication-agent-example-wheel.png</p>
<dt> 5.</p>
<dd>Freedesktop.org Icon Naming Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html">http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html</a></dl>
