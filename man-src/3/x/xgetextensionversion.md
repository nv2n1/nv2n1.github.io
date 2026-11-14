---
title: "xgetextensionversion(3)"
name: "xgetextensionversion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetextensionversion/"
---

XGetExtensionVersion - query the version of the input extension. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>XExtensionVersion *XGetExtensionVersion( Display *display,
 char *name);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>name
 Specifies the extension to be queried. The input
 extension name is definedin the header file XI.h.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XGetExtensionVersion request is deprecated and should not
be used in XI2 applications. Clients issuing a XGetExtensionVersion
request will not be able to use XI2 features.</pre></dl><dl COMPACT><dd><pre>The XGetExtensionVersion request queries the version of the input
extension, and returns an XExtensionVersion structure. This structure
contains a major_version and minor_version number which can be compared
with constants defined in XI.h. Support for additional protocol
requests added to the input extension after its initial release
is indicated by a version number corresponding to the added
requests. Each version contains all the protocol requests
contained by previous versions.</pre></dl><dl COMPACT><dd><pre>You should use XFree to free the XExtensionVersion structure.</pre></dl><h2>Structures</h2><dl COMPACT><dd><pre>This request returns an XExtensionVersion structure.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 int present;
 short major_version;
 short minor_version;
} XExtensionVersion;</pre></dl>
