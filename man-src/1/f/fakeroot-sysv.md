---
title: "fakeroot-sysv(1)"
name: "fakeroot-sysv"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fakeroot-sysv/"
description: "fakeroot – run a command in an environment faking root privileges for file manipulation"
---

<h2 class="name">NAME</h2>
<p> fakeroot &#8211; run a command in an environment faking root privileges for file manipulation </p>
<h2>SYNOPSIS</h2>
<p> <code>fakeroot </code> <code>[-l|&#8211;lib</code> <i>library]</i> <code>[&#8211;faked</code> <i>faked-binary</i><code>]</code> <code>[-i</code> <i>load-file</i><code>]</code> <code>[-s</code> <i>save-file</i><code>]</code> <code>[-u|&#8211;unknown-is-real ]</code> <code>[-b|&#8211;fd-base ]</code> <code>[-h|&#8211;help ]</code> <code>[-v|&#8211;version ]</code> <code>[&#8211;]</code> <code>[command]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>fakeroot</code> runs a command in an environment wherein it appears to have root privileges for file manipulation. This is useful for allowing users to create archives (tar, ar, .deb etc.) with files in them with root permissions/ownership. Without <code>fakeroot</code> one would need to have root privileges to create the constituent files of the archives with the correct permissions and ownership, and then pack them up, or one would have to construct the archives directly, without using the archiver. </p>
<p> <code>fakeroot</code> works by replacing the file manipulation library functions (<a href="/docs/linux/man/2-chmod/">chmod</a>(2), <a href="/docs/linux/man/2-stat/">stat</a>(2) etc.) by ones that simulate the effect the real library functions would have had, had the user really been root. These wrapper functions are in a shared library <code>/usr/lib/*/libfakeroot-*.so</code> or similar location on your platform. The shared object is loaded through the <code>LD_PRELOAD</code> mechanism of the dynamic loader. (See <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)) </p>
<p> If you intend to build packages with <code>fakeroot</code>, please try building the fakeroot package first: the &quot;debian/rules build&quot; stage has a few tests (testing mostly for bugs in old fakeroot versions). If those tests fail (for example because you have certain libc5 programs on your system), other packages you build with fakeroot will quite likely fail too, but possibly in much more subtle ways. </p>
<p> Also, note that it&#8217;s best not to do the building of the binaries themselves under fakeroot. Especially configure and friends don&#8217;t like it when the system suddenly behaves differently from what they expect. (or, they randomly unset some environment variables, some of which fakeroot needs). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code> <i>library</i>, <code>&#8211;lib</code> <i>library</i></p>
<dd> Specify an alternative wrapper library.</p>
<dt><code>&#8211;faked</code><i>&nbsp;binary</i></p>
<dd> Specify an alternative binary to use as faked.</p>
<dt><code>[&#8211;]</code><i>&nbsp;command</i></p>
<dd> Any command you want to be ran as fakeroot. Use &#8216;&#8211;&#8216; if in the command you have other options that may confuse fakeroot&#8217;s option parsing.</p>
<dt><code>-s</code><i>&nbsp;save-file</i></p>
<dd> Save the fakeroot environment to save-file on exit. This file can be used to restore the environment later using -i. However, this file will leak and fakeroot will behave in odd ways unless you leave the files touched inside the fakeroot alone when outside the environment. Still, this can be useful. For example, it can be used with <a href="/docs/linux/man/1-rsync/">rsync</a>(1) to back up and restore whole directory trees complete with user, group and device information without needing to be root. See <i>/usr/share/doc/fakeroot/README.saving</i> for more details.</p>
<dt><code>-i</code><i>&nbsp;load-file</i></p>
<dd> Load a fakeroot environment previously saved using -s from load-file. Note that this does not implicitly save the file, use -s as well for that behaviour. Using the same file for both -i and -s in a single <code>fakeroot</code> invocation is safe.</p>
<dt><code>-u</code>, <code>&#8211;unknown-is-real</code></p>
<dd> Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.</p>
<dt><code>-b</code><i>&nbsp;fd</i></p>
<dd> Specify fd base (TCP mode only). fd is the minimum file descriptor number to use for TCP connections; this may be important to avoid conflicts with the file descriptors used by the programs being run under fakeroot.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-v</code></p>
<dd> Display version. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Here is an example session with <code>fakeroot</code>. Notice that inside the fake root environment file manipulation that requires root privileges succeeds, but is not really happening. </p>
<pre><code>
$ whoami
            joost
                $ fakeroot /
        bin / bash
#whoami
                  root
#mknod hda3 b 3 1
#ls - ld hda3
                      brw -
    r-- r-- 1 root root 3,
    1 Jul 2 22 : 58 hda3
#chown joost : root hda3
#ls - ld hda3
            brw -
        r-- r-- 1 joost root 3,
    1 Jul 2 22 : 58 hda3
#ls - ld /
            drwxr -
        xr - x 20 root root 1024 Jun 17 21 : 50 /
#chown joost : users /
#chmod a + w /
#ls - ld /
                 drwxrwxrwx 20 joost users 1024 Jun 17 21 : 50 /
#exit
                 $ ls -
        ld /
            drwxr -
        xr - x 20 root root 1024 Jun 17 21 : 50 //
        $ ls -
        ld hda3 - rw - r-- r-- 1 joost users 0 Jul 2 22 : 58 hda3
</code></pre>
<p> Only the effects that user <code>joost</code> could do anyway happen for real. </p>
<p> <code>fakeroot</code> was specifically written to enable users to create Debian GNU/Linux packages (in the <code><a href="/docs/linux/man/5-deb/">deb</a>(5)</code> format) without giving them root privileges. This can be done by commands like <code>dpkg-buildpackage -rfakeroot</code> or <code>debuild -rfakeroot</code> (actually, -rfakeroot is default in debuild nowadays, so you don&#8217;t need that argument).</p>
<h2>SECURITY ASPECTS</h2>
<p> <code>fakeroot</code> is a regular, non-setuid program. It does not enhance a user&#8217;s privileges, or decrease the system&#8217;s security.</p>
<h2>FILES</h2>
<p> <i>/usr/lib/*/libfakeroot-*.so</i> The shared library containing the wrapper functions.</p>
<h2>ENVIRONMENT</h2>
<p> <code></p>
<dl>
<dt>FAKEROOTKEY</p>
<dd> </code> The key used to communicate with the fakeroot daemon. Any program started with the right <code>LD_PRELOAD</code> and a <code>FAKEROOTKEY</code> of a running daemon will automatically connect to that daemon, and have the same &quot;fake&quot; view of the file system&#8217;s permissions/ownerships. (assuming the daemon and connecting program were started by the same user). <code></p>
<dt>LD_LIBRARY_PATH</p>
<dd> </code> <code></p>
<dt>LD_PRELOAD</p>
<dd> </code> Fakeroot is implemented by wrapping system calls. This is accomplished by setting LD_LIBRARY_PATH=/usr/lib/fakeroot and LD_PRELOAD=libfakeroot.so.0. That library is loaded before the system&#8217;s C library, and so most of the library functions are intercepted by it. If you need to set either <code>LD_LIBRARY_PATH</code> or <code>LD_PRELOAD</code> from within a fakeroot environment, it should be set relative to the given paths, as in <code>LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/foo/bar/</code> </p>
</dl>
<h2>LIMITATIONS</h2>
<p> <code></p>
<dl>
<dt>Library versions</p>
<dd> </code> Every command executed within <code>fakeroot </code> needs to be linked to the same version of the C library as <code>fakeroot</code> itself. <code></p>
<dt>open()/create()</p>
<dd> </code> fakeroot doesn&#8217;t wrap open(), create(), etc. So, if user <code>joost</code> does either </p>
<pre>
touch foo
fakeroot 
ls -al foo
</pre>
<p> or the other way around, </p>
<pre>
fakeroot
touch foo
ls -al foo
</pre>
<p> fakeroot has no way of knowing that in the first case, the owner of foo really should be <code>joost</code> while the second case it should have been <code>root</code>. For the Debian packaging, defaulting to giving all &quot;unknown&quot; files uid=gid=0, is always OK. The real way around this is to wrap <code>open() </code> and <code>create()</code>, but that creates other problems, as demonstrated by the libtricks package. This package wrapped many more functions, and tried to do a lot more than <code>fakeroot .</code> It turned out that a minor upgrade of libc (from one where the <code>stat()</code> function didn&#8217;t use <code>open()</code> to one with a <code>stat()</code> function that did (in some cases) use <code>open()</code>), would cause unexplainable segfaults (that is, the libc6 <code>stat()</code> called the wrapped <code>open()</code>, which would then call the libc6 <code>stat()</code>, etc). Fixing them wasn&#8217;t all that easy, but once fixed, it was just a matter of time before another function started to use open(), never mind trying to port it to a different operating system. Thus I decided to keep the number of functions wrapped by fakeroot as small as possible, to limit the likelihood of &#8216;collisions&#8217;. <code></p>
<dt>GNU configure (and other such programs)</p>
<dd> </code> fakeroot, in effect, is changing the way the system behaves. Programs that probe the system like GNU configure may get confused by this (or if they don&#8217;t, they may stress fakeroot so much that fakeroot itself becomes confused). So, it&#8217;s advisable not to run &quot;configure&quot; from within fakeroot. As configure should be called in the &quot;debian/rules build&quot; target, running &quot;dpkg-buildpackage -rfakeroot&quot; correctly takes care of this.</dl>
<h2>BUGS</h2>
<p> It doesn&#8217;t wrap open(). This isn&#8217;t bad by itself, but if a program does open(&quot;file&quot;, O_WRONLY, 000), writes to file &quot;file&quot;, closes it, and then again tries to open to read the file, then that open fails, as the mode of the file will be 000. The bug is that if root does the same, open() will succeed, as the file permissions aren&#8217;t checked at all for root. I choose not to wrap open(), as open() is used by many other functions in libc (also those that are already wrapped), thus creating loops (or possible future loops, when the implementation of various libc functions slightly change).</p>
<h2>COPYING</h2>
<p> <code>fakeroot</code> is distributed under the GNU General Public License. (GPL 2.0 or greater).</p>
<h2>AUTHORS</h2>
<dl>
<dt>joost witteveen</p>
<dd> &lt;<i>joostje [at] debian.org</i>&gt;</p>
<dt>Clint Adams</p>
<dd> &lt;<i>clint [at] debian.org</i>&gt;</p>
<dt>Timo Savola</p>
<dd></dl>
<h2>MANUAL PAGE</h2>
<p> mostly by J.H.M. Dassen &lt;jdassen [at] debian.org&gt; Rather a lot mods/additions by joost and Clint.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-faked/">faked</a></code>(1) <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1), <code><a href="/docs/linux/man/1-debuild/">debuild</a></code>(1) <code>/usr/share/doc/fakeroot/DEBUG</code> </p>
<h2>Index</h2>
