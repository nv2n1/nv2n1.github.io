---
title: "ctrlaltdel(8)"
name: "ctrlaltdel"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ctrlaltdel/"
description: "ctrlaltdel – set the function of the Ctrl-Alt-Del combination"
---

<p>ctrlaltdel &#8211; set the function of the Ctrl-Alt-Del combination</p>
<h2>Synopsis</h2>
<p><code>ctrlaltdel</code> <code>hard</code>|<code>soft</code></p>
<h2>Description</h2>
<p>Based on examination of the <i>linux/kernel/reboot.c</i> code, it is clear that there are two supported functions that the &lt;Ctrl-Alt-Del&gt; sequence can perform. </p>
<p> <code>hard</code></p>
<dl>
<dd>Immediately reboot the computer without calling <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) and without any other preparation. This is the default.</dl>
<p> <code>soft</code></p>
<dl>
<dd>Make the kernel send the <code>SIGINT</code> (interrupt) signal to the <code>init</code> process (this is always the process with PID 1). If this option is used, the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) program must support this feature. Since there are now several <code><a href="/docs/linux/man/8-init/">init</a></code>(8) programs in the Linux community, please consult the documentation for the version that you are currently using.</dl>
<p> When the command is run without any argument, it will display the current setting. </p>
<p> The function of <code>ctrlaltdel</code> is usually set in the <i>/etc/rc.local</i> file.</p>
<h2>Options</h2>
<p><code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Files</h2>
<p><i>/etc/rc.local</i></p>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>ctrlaltdel</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
