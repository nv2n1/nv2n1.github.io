---

title: "dar_cp(1)"
name: "dar_cp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dar_cp/"
description: "dar_cp – ‘cp’ clone command that is able to copy data located after an I/O error"
---

<p> dar_cp &#8211; &#8216;cp&#8217; clone command that is able to copy data located after an I/O error </p>
<h2>SYNOPSIS</h2>
<p> dar_cp &lt;source file&gt; &lt;destination file&gt; </p>
<p> dar_cp -h </p>
<p> dar_cp -V</p>
<h2>DESCRIPTION</h2>
<p> <code>dar_cp</code> is similar to the standard &#8216;cp&#8217; command, except it does not stop copying when an I/O error is met. Instead, it skips a bit further and continues to copy the rest of the file, as much as possible, filling the gaps by zeroed bytes. </p>
<p> <code>dar_cp</code> only accepts full filename (not directory) as argument. The reason of its existence in dar package is that you need it if you use Parchive with dar and have a corruption on a CD-R or any other read-only medium. You need to copy the corrupted slice on a read-write filesystem, for Parchive be able to repair it using slice associated redundancy files. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</dt>
<dd> Displays help usage.</dd>
<dt>-V</dt>
<dd> Displays version information. </dd>
</dl>
<h2>EXIT CODES</h2>
<p> <code>dar_cp</code> exists with the following codes:</p>
<dl>
<dt>0</dt>
<dd> upon normal execution (be some corrupted parted skipped or not)</dd>
<dt>1</dt>
<dd> syntax error on command-line</dd>
<dt>2</dt>
<dd> could not open source or destination files</dd>
<dt>3</dt>
<dd> any other system error met during the copy</dd>
<dt>5</dt>
<dd> when some data could not be copied due to I/O error </dd>
</dl>
<h2>SIGNALS</h2>
<p> Any signal sent to dar_cp will abort the program immediately, there is no way to have a proper termination before the end of the process </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dar/">dar</a>(1), <a href="/docs/linux/man/1-dar_xform/">dar_xform</a>(1), <a href="/docs/linux/man/1-dar_manager/">dar_manager</a>(1), <a href="/docs/linux/man/1-dar_slave/">dar_slave</a>(1), <a href="/docs/linux/man/1-dar_split/">dar_split</a>(1) </p>
<h2>KNOWN BUGS</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/p/dar/bugs/">http://sourceforge.net/p/dar/bugs/</a> </p>
<h2>AUTHOR</h2>
<pre>
<a rel="nofollow" href="http://dar.linux.free.fr/">http://dar.linux.free.fr/</a>
Denis Corbin
France
Europe
</pre>
