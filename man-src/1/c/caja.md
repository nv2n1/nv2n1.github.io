---

title: "caja(1)"
name: "caja"
section: "1"
letter: "c"
url: "/docs/linux/man/1-caja/"
description: "Caja – The MATE File Manager"
---

<p> Caja &#8211; The MATE File Manager </p>
<h2>SYNOPSIS</h2>
<p> <code>caja [OPTIONS&#8230;] [URI&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> Caja is the default file manager for the MATE Desktop Environment. It makes it easy to manage, manipulate, and customize files and directories. Caja can access local and remote filesystems such as SSH, FTP, and WebDav (HTTP/HTTPS). </p>
<p> Caja also provides the desktop background and the icons it uses for launching links and applications, as well as accessing files, directories, the trash, and removable media like CD/DVD/BD and USB drives. </p>
<p> This manual page briefly documents the <code>caja</code> command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;browser</code></dt>
<dd> Open a browser window.</dd>
<dt><code>-c, &#8211;check</code></dt>
<dd> Perform a quick set of self-check tests.</dd>
<dt><code>&#8211;display=DISPLAY</code></dt>
<dd> X display to use.</dd>
<dt><code>-g, &#8211;geometry=</code><i>GEOMETRY</i></dt>
<dd> Create the initial window with the given geometry.</dd>
<dt><code>-n, &#8211;no-default-window</code></dt>
<dd> Only create windows for explicitly specified URIs.</dd>
<dt><code>&#8211;no-desktop</code></dt>
<dd> Do not manage the desktop (ignore the preference set in the preferences dialog).</dd>
<dt><code>-q, &#8211;quit</code></dt>
<dd> Quit Caja.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print current version information and exit.</dd>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print standard command line options.</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Print all command line options.</dd></dl>
<p> This program also accepts the standard GTK options. </p>
<h2>EXAMPLES</h2>
<p> <code>caja <a href="ftp://ftp.kernel.org/">ftp://ftp.kernel.org/</a></code></p>
<dl>
<dt>
</dt><dd> Open a new Caja window on the Linux Kernel ftp server.</dd></dl>
<p> <code>caja &#8211;no-desktop /home/user/</code></p>
<dl>
<dt>
</dt><dd> Open a Caja window in &quot;user&#8217;s&quot; home directory without managing the desktop.</dd></dl>
<p> <code>caja -g 600&#215;400</code></p>
<dl>
<dt>
</dt><dd> Open a Caja window that is 600 pixels wide by 400 pixels high.</dd></dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/caja/issues">http://github.com/mate-desktop/caja/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Man Page has been updated/re-written for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>HISTORY</h2>
<p> This manual page was originally written by Takuo KITAME &lt;kitame [at] debian.org&gt; and Dafydd Harries &lt;daf [at] muse.19inch.net&gt; to accompany the Nautilus file manager for the GNOME Desktop Environment on Debian GNU/Linux. (2004)</p>
<h2>SEE ALSO</h2>
<h3>Caja documentation can be found from the Help menu, or by pressing the F1 key.</h3>
<p> Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a> </p>
<p> <code><a href="/docs/linux/man/1-caja-file-management-properties/">caja-file-management-properties</a></code>(1), <code><a href="/docs/linux/man/1-caja-autorun-software/">caja-autorun-software</a></code>(1), <code><a href="/docs/linux/man/1-caja-connect-server/">caja-connect-server</a></code>(1) </p>
