---
title: "setproctitle(3)"
name: "setproctitle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setproctitle/"
description: "setproctitle – set process title"
---

<p><code>setproctitle</code> &#8211; set process title</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In sys/types.h In bsd/unistd.h Ft void Fn setproctitle_init int argc char *argv[] char *envp[] Ft void Fn setproctitle const char *fmt &#8230;</p>
<h2>Description</h2>
<p>The Fn setproctitle library routine sets the process title that appears on the <a href="/docs/linux/man/1-ps/">ps</a>(1) command. </p>
<p> The Fn setproctitle_init library routine only needs to be called (before any call to Fn setproctitle and with Fn main arguments), if the automatic constructor support has not been linked in through the libbsd-ctor pkg-config file. </p>
<p> The title is set from the executable&#8217;s name, followed by the result of a <a href="/docs/linux/man/3-printf/">printf</a>(3) style expansion of the arguments as specified by the <i>fmt</i> argument. If the <i>fmt</i> argument begins with a &#8220;-&#8221; character, the executable&#8217;s name is skipped. </p>
<p> If <i>fmt</i> is NULL, the process title is restored.</p>
<h2>Examples</h2>
<p>To set the title on a daemon to indicate its activity: </p>
<blockquote>
<pre>setproctitle(&quot;talking to %s&quot;, inet_ntoa(addr));</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/1-w/">w</a>(1), <a href="/docs/linux/man/3-kvm/">kvm</a>(3), kvm_getargv3, <a href="/docs/linux/man/3-printf/">printf</a>(3)</p>
<h2>Standards</h2>
<p>The Fn setproctitle function is implicitly non-standard. Other methods of causing the <a href="/docs/linux/man/1-ps/">ps</a>(1) command line to change, including copying over the argv[0] string are also implicitly non-portable. It is preferable to use an operating system supplied Fn setproctitle if present. </p>
<p> Unfortunately, it is possible that there are other calling conventions to other versions of Fn setproctitle , although none have been found by the author as yet. This is believed to be the predominant convention. </p>
<p> It is thought that the implementation is compatible with other systems, including Nx and Bs x .</p>
<h2>History</h2>
<p>The Fn setproctitle function first appeared in Fx 2.2 . Other operating systems have similar functions. </p>
<p> The Fn setproctitle_init function is a libbsd extension not present on the BSDs, avoid using it in portable code.</p>
<h2>Authors</h2>
<p>An -nosplit An Peter Wemm Aq peter [at] FreeBSD.org stole the idea from the <code>Sendmail 8.7.3</code> source code by An Eric Allman Aq eric [at] sendmail.org .</p>
<h2>Bugs</h2>
<p>Never pass a string with user-supplied data as a format without using `%s&#8217; An attacker can put format specifiers in the string to mangle your stack, leading to a possible security hole. This holds true even if the string was built using a function like Fn snprintf , as the resulting string may still contain user-supplied conversion specifiers for later interpolation by Fn setproctitle . Always use the proper secure idiom: </p>
<blockquote><p><tt>setproctitle(&quot;%s&quot;, string);</tt></p></blockquote>
