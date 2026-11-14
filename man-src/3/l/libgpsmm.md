---
title: "libgpsmm(3)"
name: "libgpsmm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libgpsmm/"
description: "libgpsmm, libQgpsmm – C++ and QT class wrapper for the GPS daemon"
---

<h2 class="name">NAME</h2>
<p> libgpsmm, libQgpsmm &#8211; C++ and QT class wrapper for the GPS daemon </p>
<h2>SYNOPSIS</h2>
<pre><code>
C++:
#include &lt;libgpsmm&gt;
</code></pre>
<dl>
<dt> <code>struct gps_data_t *open(char&nbsp;<wbr>*</code><i>host</i><code>, char&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>struct gps_data_t *open(void);</code></p>
<dt> <code>struct gps_data_t *send(char&nbsp;<wbr>*</code><i>request</i><code>);</code></p>
<dt> <code>struct gps_data_t *read(void);</code></p>
<dt> <code>struct gps_data_t *waiting(int);</code></p>
<dt> <code>struct gps_data_t *stream(unsigned int</code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>libgpsmm and libQgpsmm</code></p>
<dd>are mere wrappers over <code>libgps</code>. The important difference between the libraries is that libgpsmm is targeted at C++ applications and contained in <code>libgps</code>, while libQgpsmm is platform independent by using QTcpSocket to connect to <code>gpsd</code> and shipped as an additional library due to the necessary linking to QT. Method names are the same as the analogue C functions. For a detailed description of the functions please read <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3). <code>open()</code> must be called after class constructor and before any other method (<code>open()</code> is not inside the constructor since it may fail, however constructors have no return value). The analogue of the C function <code>gps_close()</code> is in the destructor.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> Alfredo Pironti &lt;alfredio [at] users.sourceforge.net&gt;. </p>
<h2>Index</h2>
