---
title: "bzero(3)"
name: "bzero"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bzero/"
description: "bzero, explicit_bzero – zero a byte string"
---

<h2 class="name">NAME</h2>
<p> bzero, explicit_bzero &#8211; zero a byte string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;strings.h&gt;
void bzero(void *s, size_t n);
#include &lt;string.h&gt;
void explicit_bzero(void *s, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bzero</code>() function erases the data in the <i>n</i> bytes of the memory starting at the location pointed to by <i>s</i>, by writing zeros (bytes containing &#8216;\0&#8217;) to that area. </p>
<p> The <code>explicit_bzero</code>() function performs the same task as <code>bzero</code>(). It differs from <code>bzero</code>() in that it guarantees that compiler optimizations will not remove the erase operation if the compiler deduces that the operation is &quot;unnecessary&quot;.  </p>
<h2>RETURN VALUE</h2>
<p> None.  </p>
<h2>VERSIONS</h2>
<p> <code>explicit_bzero</code>() first appeared in glibc 2.25.  </p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bzero</code>(),  <code>explicit_bzero</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The <code>bzero</code>() function is deprecated (marked as LEGACY in POSIX.1-2001); use <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3) in new programs. POSIX.1-2008 removes the specification of <code>bzero</code>(). The <code>bzero</code>() function first appeared in 4.3BSD. </p>
<p> The <code>explicit_bzero</code>() function is a nonstandard extension that is also present on some of the BSDs. Some other implementations have a similar function, such as <code>memset_explicit</code>() or <code>memset_s</code>().  </p>
<h2>NOTES</h2>
<p> The <code>explicit_bzero</code>() function addresses a problem that security-conscious applications may run into when using <code>bzero</code>(): if the compiler can deduce that the location to zeroed will never again be touched by a <i>correct</i> program, then it may remove the <code>bzero</code>() call altogether. This is a problem if the intent of the <code>bzero</code>() call was to erase sensitive data (e.g., passwords) to prevent the possibility that the data was leaked by an incorrect or compromised program. Calls to <code>explicit_bzero</code>() are never optimized away by the compiler. </p>
<p> The <code>explicit_bzero</code>() function does not solve all problems associated with erasing sensitive data: </p>
<dl>
<dt>1.</dt>
<dd> <p> The <code>explicit_bzero</code>() function does <i>not</i> guarantee that sensitive data is completely erased from memory. (The same is true of <code>bzero</code>().) For example, there may be copies of the sensitive data in a register and in &quot;scratch&quot; stack areas. The <code>explicit_bzero</code>() function is not aware of these copies, and can&#8217;t erase them. </p>
 </dd>
<dt>2.</dt>
<dd> <p> In some circumstances, <code>explicit_bzero</code>() can <i>decrease</i> security. If the compiler determined that the variable containing the sensitive data could be optimized to be stored in a register (because it is small enough to fit in a register, and no operation other than the <code>explicit_bzero</code>() call would need to take the address of the variable), then the <code>explicit_bzero</code>() call will force the data to be copied from the register to a location in RAM that is then immediately erased (while the copy in the register remains unaffected). The problem here is that data in RAM is more likely to be exposed by a bug than data in a register, and thus the <code>explicit_bzero</code>() call creates a brief time window where the sensitive data is more vulnerable than it would otherwise have been if no attempt had been made to erase the data. </p>
 </dd></dl>
<p> Note that declaring the sensitive variable with the <code>volatile</code> qualifier does <i>not</i> eliminate the above problems. Indeed, it will make them worse, since, for example, it may force a variable that would otherwise have been optimized into a register to instead be maintained in (more vulnerable) RAM for its entire lifetime. </p>
<p> Notwithstanding the above details, for security-conscious applications, using <code>explicit_bzero</code>() is generally preferable to not using it. The developers of <code>explicit_bzero</code>() anticipate that future compilers will recognize calls to <code>explicit_bzero</code>() and take steps to ensure that all copies of the sensitive data are erased, including copies in registers or in &quot;scratch&quot; stack areas.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3), <code><a href="/docs/linux/man/3-swab/">swab</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
