---
title: "xdisableaccesscontrol(3)"
name: "xdisableaccesscontrol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdisableaccesscontrol/"
description: "XAddHost, XAddHosts, XListHosts, XRemoveHost, XRemoveHosts, XSetAccessControl, XEnableAccessControl, XDisableAccessControl, XHostAddress, XServerInterpretedAddress – control host access and host co..."
---

<p>XAddHost, XAddHosts, XListHosts, XRemoveHost, XRemoveHosts, XSetAccessControl, XEnableAccessControl, XDisableAccessControl, XHostAddress, XServerInterpretedAddress &#8211; control host access and host control structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XAddHost(Display *<i>display</i>, XHostAddress *<i>host</i>);</p>
<dd>int XAddHosts(Display *<i>display</i>, XHostAddress *<i>hosts</i>, int <i>num_hosts</i>);</p>
<dd>XHostAddress *XListHosts(Display *<i>display</i>, int *<i>nhosts_return</i>, Bool <i>state_return</i>);</p>
<dd>int XRemoveHost(Display *<i>display</i>, XHostAddress *<i>host</i>);</p>
<dd>int XRemoveHosts(Display *<i>display</i>, XHostAddress *<i>hosts</i>, int <i>num_hosts</i>);</p>
<dd>int XSetAccessControl(Display *<i>display</i>, int <i>mode</i>);</p>
<dd>int XEnableAccessControl(Display *<i>display</i>);</p>
<dd>int XDisableAccessControl(Display *<i>display</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>host</i></p>
<dd>Specifies the host that is to be added or removed.</p>
<dt><i>hosts</i></p>
<dd>Specifies each host that is to be added or removed.</p>
<dt><i>mode</i></p>
<dd>Specifies the mode. You can pass <code>EnableAccess</code> or <code>DisableAccess</code>.</p>
<dt><i>nhosts_return</i></p>
<dd>Returns the number of hosts currently in the access control list.</p>
<dt><i>num_hosts</i></p>
<dd>Specifies the number of hosts.</p>
<dt><i>state_return</i></p>
<dd>Returns the state of the access control.</dl>
<h2>Description</h2>
<p>The <code>XAddHost</code> function adds the specified host to the access control list for that display. The server must be on the same host as the client issuing the command, or a <code>BadAccess</code> error results. </p>
<p> <code>XAddHost</code> can generate <code>BadAccess</code> and <code>BadValue</code> errors. </p>
<p> The <code>XAddHosts</code> function adds each specified host to the access control list for that display. The server must be on the same host as the client issuing the command, or a <code>BadAccess</code> error results. </p>
<p> <code>XAddHosts</code> can generate <code>BadAccess</code> and <code>BadValue</code> errors. </p>
<p> The <code>XListHosts</code> function returns the current access control list as well as whether the use of the list at connection setup was enabled or disabled. <code>XListHosts</code> allows a program to find out what machines can make connections. It also returns a pointer to a list of host structures that were allocated by the function. When no longer needed, this memory should be freed by calling <code>XFree</code>. </p>
<p> The <code>XRemoveHost</code> function removes the specified host from the access control list for that display. The server must be on the same host as the client process, or a <code>BadAccess</code> error results. If you remove your machine from the access list, you can no longer connect to that server, and this operation cannot be reversed unless you reset the server. </p>
<p> <code>XRemoveHost</code> can generate <code>BadAccess</code> and <code>BadValue</code> errors. </p>
<p> The <code>XRemoveHosts</code> function removes each specified host from the access control list for that display. The X server must be on the same host as the client process, or a <code>BadAccess</code> error results. If you remove your machine from the access list, you can no longer connect to that server, and this operation cannot be reversed unless you reset the server. </p>
<p> <code>XRemoveHosts</code> can generate <code>BadAccess</code> and <code>BadValue</code> errors. </p>
<p> The <code>XSetAccessControl</code> function either enables or disables the use of the access control list at each connection setup. </p>
<p> <code>XSetAccessControl</code> can generate <code>BadAccess</code> and <code>BadValue</code> errors. </p>
<p> The <code>XEnableAccessControl</code> function enables the use of the access control list at each connection setup. </p>
<p> <code>XEnableAccessControl</code> can generate a <code>BadAccess</code> error. </p>
<p> The <code>XDisableAccessControl</code> function disables the use of the access control list at each connection setup. </p>
<p> <code>XDisableAccessControl</code> can generate a <code>BadAccess</code> error.</p>
<h2>Structures</h2>
<p>The <code>XHostAddress</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int family;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for example FamilyInternet&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int length;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;length of address, in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*address;&nbsp;<wbr>&nbsp;/*&nbsp;pointer to where to find the address&nbsp;*/ } XHostAddress; </p>
<p> The family member specifies which protocol address family to use (for example, TCP/IP or DECnet) and can be <code>FamilyInternet</code>, <code>FamilyInternet6</code>, <code>FamilyServerInterpreted</code>, <code>FamilyDECnet</code>, or <code>FamilyChaos</code>. The length member specifies the length of the address in bytes. The address member specifies a pointer to the address. </p>
<p> For the ServerInterpreted family, the length is ignored and the address member is a pointer to a <code>XServerInterpretedAddress</code> structure which contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int typelength;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;length of type string, in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int valuelength;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;length of value string, in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pointer to where to find the type string&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pointer to where to find the address&nbsp;*/ } XServerInterpretedAddress; </p>
<p> The type and value members point to strings representing the type and value of the server interpreted entry. These strings may not be NULL-terminated so care should be used when accessing them. The typelength and valuelength members specify the length in byte of the type and value strings.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>A client attempted to modify the access control list from other than the local (or otherwise authorized) host.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
