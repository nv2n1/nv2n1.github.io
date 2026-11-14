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
<dd><code><a href="/docs/linux/man/3-obstack_alloc/">obstack_alloc</a></code>(3) &#8211; allocate memory<br />
 <code><a href="/docs/linux/man/3-obstack_free/">obstack_free</a></code>(3) &#8211; free formerly allocated memory<br />
 <code><a href="/docs/linux/man/3-obstack_copy/">obstack_copy</a></code>(3) &#8211; allocate block with content<br />
 <code><a href="/docs/linux/man/3-obstack_copy0/">obstack_copy0</a></code>(3) &#8211; allocate block with content, zero terminated<br />
 <code><a href="/docs/linux/man/3-obstack_blank/">obstack_blank</a></code>(3) &#8211; increase object size<br />
 <code><a href="/docs/linux/man/3-obstack_grow/">obstack_grow</a></code>(3) &#8211; increase object size with content<br />
 <code><a href="/docs/linux/man/3-obstack_grow0/">obstack_grow0</a></code>(3) &#8211; increase object size with content, zero term.<br />
 <code><a href="/docs/linux/man/3-obstack_1grow/">obstack_1grow</a></code>(3) &#8211; increase object size by 1 character<br />
 <code><a href="/docs/linux/man/3-obstack_ptr_grow/">obstack_ptr_grow</a></code>(3) &#8211; increase object size by value of pointer<br />
 <code><a href="/docs/linux/man/3-obstack_int_grow/">obstack_int_grow</a></code>(3) &#8211; increase object size by sizeof(int)<br />
 <code><a href="/docs/linux/man/3-obstack_finish/">obstack_finish</a></code>(3) &#8211; finish growing of an obstack object<br />
 <code><a href="/docs/linux/man/3-obstack_object_size/">obstack_object_size</a></code>(3) &#8211; return the size of an obstack object<br />
 <code><a href="/docs/linux/man/3-obstack_room/">obstack_room</a></code>(3) &#8211; available room in current chunk<br />
 <code><a href="/docs/linux/man/3-obstack_1grow_fast/">obstack_1grow_fast</a></code>(3) &#8211; fast increase object size by 1 character<br />
 <code><a href="/docs/linux/man/3-obstack_ptr_grow_fast/">obstack_ptr_grow_fast</a></code>(3) &#8211; fast increase object by pointer value<br />
 <code><a href="/docs/linux/man/3-obstack_int_grow_fast/">obstack_int_grow_fast</a></code>(3) &#8211; fast increase object size by sizeof(int)<br />
 <code><a href="/docs/linux/man/3-obstack_blank_fast/">obstack_blank_fast</a></code>(3) &#8211; fast increase object size<br />
 <code><a href="/docs/linux/man/3-obstack_base/">obstack_base</a></code>(3) &#8211; return tentative address of beginning<br />
 <code><a href="/docs/linux/man/3-obstack_next_free/">obstack_next_free</a></code>(3) &#8211; return address of the first free byte<br />
 <code><a href="/docs/linux/man/3-obstack_object_size/">obstack_object_size</a></code>(3) &#8211; return size of currently growing object<br />
 <code><a href="/docs/linux/man/3-obstack_alignment_mask/">obstack_alignment_mask</a></code>(3) &#8211; alter mask assignment<br />
 <code><a href="/docs/linux/man/3-obstack_chunk_size/">obstack_chunk_size</a></code>(3) &#8211; return chunk size of given obstack<br />
 <code><a href="/docs/linux/man/3-obstack_init/">obstack_init</a></code>(3) &#8211; initialize use of an obstack</p>
<dt>Bug#<i>172139</i></p>
<dd><code><a href="/docs/linux/man/3-wcstol/">wcstol</a></code>(3) &#8211; convert a wide-character string to a long integer</p>
<dt>Bug#<i>202022</i></p>
<dd><code><a href="/docs/linux/man/3-iruserok_sa/">iruserok_sa</a></code>(3) &#8211; routines for returning a stream to a remote command (see <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3)).</p>
<dt>Bug#<i>208856</i></p>
<dd><code><a href="/docs/linux/man/3-cap_set_proc/">cap_set_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3) &#8211; POSIX capability manipulation on processes<br />
 <code><a href="/docs/linux/man/3-capsetp/">capsetp</a></code>(3), <code><a href="/docs/linux/man/3-capgetp/">capgetp</a></code>(3) &#8211; Linux specific capability manipulation on arbitrary processes</p>
<dt>Bug#<i>349388</i></p>
<dd><code><a href="/docs/linux/man/3-argp_parse/">argp_parse</a></code>(3) &#8211; main interface to argp.</dl>
<h3>Section 9 &#8211; Kernel routines</h3>
<dl>
<dt>Bug#<i>102724</i></p>
<dd>Mandrake seems to deliver section 9 manual pages, though their source is obscure and they do seem to be out-dated. Nevertheless, some section 9 manpages would be nice, indeed.</p>
<dt>Bug#<i>179475</i></p>
<dd><code><a href="/docs/linux/man/9-kapmd/">kapmd</a></code>(9) &#8211; kernel APM thread<br />
 <code><a href="/docs/linux/man/9-keventd/">keventd</a></code>(9) &#8211; manage hotplug events<br />
 <code><a href="/docs/linux/man/9-khubd/">khubd</a></code>(9) &#8211; kernel USB hub daemon thread<br />
 <code><a href="/docs/linux/man/9-kjournald/">kjournald</a></code>(9) &#8211; maintain the filesystem journal<br />
 <code><a href="/docs/linux/man/9-ksoftirqd/">ksoftirqd</a></code>(9) &#8211; software handling of incoming IRQs<br />
 <code><a href="/docs/linux/man/9-kswapd/">kswapd</a></code>(9) &#8211; kernel swap daemon thread<br />
 <code><a href="/docs/linux/man/9-kupdated/">kupdated</a></code>(9) &#8211; flush the journal<br />
 <code><a href="/docs/linux/man/9-scsi_eh/">scsi_eh</a></code>(9) &#8211; kernel SCSI error handler thread</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-undocumented/">undocumented</a></code>(3), <code><a href="/docs/linux/man/7-undocumented/">undocumented</a></code>(7), <code><a href="/docs/linux/man/7-man/">man</a></code>(7).<br />
 Debian Bug Tracking System at &lt;<code><a rel="nofollow" href="http://bugs.debian.org/manpages-dev">http://bugs.debian.org/manpages-dev</a></code>&gt;, the Single UNIX Specification, Version 2, at &lt;<code><a rel="nofollow" href="http://www.opengroup.org/onlinepubs/007908799/toc.htm">http://www.opengroup.org/onlinepubs/007908799/toc.htm</a></code>&gt;, the Single UNIX Specification, Version 3, at &lt;<code><a rel="nofollow" href="http://www.UNIX-systems.org/version3/">http://www.UNIX-systems.org/version3/</a></code>&gt;. </p>
