---
title: "xiqueryversion(3)"
name: "xiqueryversion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xiqueryversion/"
---

XIQueryVersion - announce and query the support XI2 version. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Status XIQueryVersion( Display *display,
 int *major_version_inout,
 int *minor_version_inout);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>major_version_inout
 Specifies the client's supported XI2 version, and
 returns the server's supported version.</pre><pre>minor_version_inout
 Specifies the client's supported XI2 version, and
 returns the server's supported version.</pre><h2>Description</h2><dl COMPACT><dd><pre>XIQueryVersion announces the client's supported XI2 version to
the server and returns server's supported X Input version. Clients
are required to use XIQueryVersion instead of XGetExtensionVersion
if they use XI2 calls. The server may treat a client differently
depending on the supported version announced by the client.
The major_version_inout must be 2 or greater, otherwise a BadValue
error occurs.</pre></dl><dl COMPACT><dd><pre>If the server does not support XI2, XIQueryVersion returns BadRequest
to the client. Otherwise, XIQueryVersion returns Success. In both
cases major_version_inout and minor_version_inout are set to the
server's supported version.</pre></dl><dl COMPACT><dd><pre>If the client has previously called XIQueryVersion, then the result
depends on the previously requested version and the currently
requested version.</pre></dl><dl COMPACT><dd><pre>If either the previous or current requested versions is less than
2.2, or if the requested major version numbers do not match, then
consecutive calls to XIQueryVersion by the same client always
return the first returned major.minor version. If the client
requests a version lower than the first returned major.minor
version in a subsequent call, a BadValue error occurs.</pre></dl><dl COMPACT><dd><pre>If all of the requested versions are 2.2 or greater, then
consecutive calls to XIQueryVersion by the same client with the
same major version will return the requested version, but the server
will operate according to the highest requested version number or
the highest supported version, whichever is lower.</pre></dl><dl COMPACT><dd><pre>XIQueryVersion can generate a BadValue error.</pre></dl><h2>Examples</h2><dl COMPACT><dd><pre>int rc;
int major = 2;
int minor = 0;</pre></dl><dl COMPACT><dd><pre>rc = XIQueryVersion(dpy, &amp;major, &amp;minor);
if (rc == Success)
 printf(&quot;XI2 supported. (%d.%d)\n&quot;, major, minor);
else if (rc == BadRequest)
 printf(&quot;No XI2 support. (%d.%d only)\n&quot;, major, minor);
else
 printf(&quot;Internal error\n&quot;);</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadValue
 A value is outside of the permitted range.</pre></dl>
