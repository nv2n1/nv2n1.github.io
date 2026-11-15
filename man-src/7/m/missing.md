---
title: "missing(7)"
name: "missing"
section: "7"
letter: "m"
url: "/docs/linux/man/7-missing/"
description: "missing – missing manual pages"
---

<p>missing &#8211; missing manual pages</p>
<h2>Description</h2>
<p>This manual page intends to document which manual pages are missing in various sections. Bug reports against the package <code>manpages-dev</code> or <code>manpages</code> were opened for all of them through the Debian Bug Tracking System (BTS). Some of these bug reports were reported upstream while some weren&#8217;t. Upstream, however, is not able to create arbitrary manpages without additional information and additional spare time. Hence, it&#8217;s completely useless to simply report them upstream. </p>
<p> Manpages represent an important means of documentation which can easily be read and converted into various formats. They are very helpful for checking how things work, rather than for a tutorial. If you notice that more pages are missing, please try to find additional information and report it as wishlist bug against this package. </p>
<p> If you are confident with the issue, please write up a preliminary manpage and attach it to the bug report. It doesn&#8217;t matter if your English is bad or if you mixed up markup, as long as the content can be used as source for a new manpage. A detailed documentation on how to write manpages is available in <code><a href="/docs/linux/man/7-man/">man</a></code>(7). </p>
<p> When writing manual pages please ensure that they are conforming with The Single UNIX Specification (see below). Linux ought to be conforming to this specification. Differences need to be documented, in additional sections, though.</p>
<h2>Missing Pages</h2>
<p>The following is a list of missing pages sorted by section and bug number. If you can contribute content or even a manual page, please send a mail to <i>nnnnn</i><code>@bugs.debian.org</code> where <i>nnnnn</i> refers to the bug number from below.</p>
<h3>Section 3 &#8211; Library calls</h3>
<dl>
<dt>Bug#<i>123999</i></p>
<dd><code>obstack_alloc</code>(3) &#8211; allocate memory<br />
 <code>obstack_free</code>(3) &#8211; free formerly allocated memory<br />
 <code>obstack_copy</code>(3) &#8211; allocate block with content<br />
 <code>obstack_copy0</code>(3) &#8211; allocate block with content, zero terminated<br />
 <code>obstack_blank</code>(3) &#8211; increase object size<br />
 <code>obstack_grow</code>(3) &#8211; increase object size with content<br />
 <code>obstack_grow0</code>(3) &#8211; increase object size with content, zero term.<br />
 <code>obstack_1grow</code>(3) &#8211; increase object size by 1 character<br />
 <code>obstack_ptr_grow</code>(3) &#8211; increase object size by value of pointer<br />
 <code>obstack_int_grow</code>(3) &#8211; increase object size by sizeof(int)<br />
 <code>obstack_finish</code>(3) &#8211; finish growing of an obstack object<br />
 <code>obstack_object_size</code>(3) &#8211; return the size of an obstack object<br />
 <code>obstack_room</code>(3) &#8211; available room in current chunk<br />
 <code>obstack_1grow_fast</code>(3) &#8211; fast increase object size by 1 character<br />
 <code>obstack_ptr_grow_fast</code>(3) &#8211; fast increase object by pointer value<br />
 <code>obstack_int_grow_fast</code>(3) &#8211; fast increase object size by sizeof(int)<br />
 <code>obstack_blank_fast</code>(3) &#8211; fast increase object size<br />
 <code>obstack_base</code>(3) &#8211; return tentative address of beginning<br />
 <code>obstack_next_free</code>(3) &#8211; return address of the first free byte<br />
 <code>obstack_object_size</code>(3) &#8211; return size of currently growing object<br />
 <code>obstack_alignment_mask</code>(3) &#8211; alter mask assignment<br />
 <code>obstack_chunk_size</code>(3) &#8211; return chunk size of given obstack<br />
 <code>obstack_init</code>(3) &#8211; initialize use of an obstack</p>
<dt>Bug#<i>172139</i></p>
<dd><code>wcstol</code>(3) &#8211; convert a wide-character string to a long integer</p>
<dt>Bug#<i>202022</i></p>
<dd><code>iruserok_sa</code>(3) &#8211; routines for returning a stream to a remote command (see <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3)).</p>
<dt>Bug#<i>208856</i></p>
<dd><code><a href="/docs/linux/man/3-cap_set_proc/">cap_set_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3) &#8211; POSIX capability manipulation on processes<br />
 <code><a href="/docs/linux/man/3-capsetp/">capsetp</a></code>(3), <code><a href="/docs/linux/man/3-capgetp/">capgetp</a></code>(3) &#8211; Linux specific capability manipulation on arbitrary processes</p>
<dt>Bug#<i>349388</i></p>
<dd><code>argp_parse</code>(3) &#8211; main interface to argp.</dl>
<h3>Section 9 &#8211; Kernel routines</h3>
<dl>
<dt>Bug#<i>102724</i></p>
<dd>Mandrake seems to deliver section 9 manual pages, though their source is obscure and they do seem to be out-dated. Nevertheless, some section 9 manpages would be nice, indeed.</p>
<dt>Bug#<i>179475</i></p>
<dd><code>kapmd</code>(9) &#8211; kernel APM thread<br />
 <code>keventd</code>(9) &#8211; manage hotplug events<br />
 <code>khubd</code>(9) &#8211; kernel USB hub daemon thread<br />
 <code>kjournald</code>(9) &#8211; maintain the filesystem journal<br />
 <code>ksoftirqd</code>(9) &#8211; software handling of incoming IRQs<br />
 <code>kswapd</code>(9) &#8211; kernel swap daemon thread<br />
 <code>kupdated</code>(9) &#8211; flush the journal<br />
 <code>scsi_eh</code>(9) &#8211; kernel SCSI error handler thread</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-undocumented/">undocumented</a></code>(3), <code><a href="/docs/linux/man/7-undocumented/">undocumented</a></code>(7), <code><a href="/docs/linux/man/7-man/">man</a></code>(7).<br />
 Debian Bug Tracking System at &lt;<code><a rel="nofollow" href="http://bugs.debian.org/manpages-dev">http://bugs.debian.org/manpages-dev</a></code>&gt;, the Single UNIX Specification, Version 2, at &lt;<code><a rel="nofollow" href="http://www.opengroup.org/onlinepubs/007908799/toc.htm">http://www.opengroup.org/onlinepubs/007908799/toc.htm</a></code>&gt;, the Single UNIX Specification, Version 3, at &lt;<code><a rel="nofollow" href="http://www.UNIX-systems.org/version3/">http://www.UNIX-systems.org/version3/</a></code>&gt;. </p>
