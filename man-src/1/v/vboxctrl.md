---

title: "vboxctrl(1)"
name: "vboxctrl"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxctrl/"
description: "vboxctrl – control vbox functions"
---

<p> <code>vboxctrl</code> [{-c | -r}] {-a | -n | -p | -j} [-s spool]<br />
 <code>vboxctrl</code> -v </p>
<p> <code>vboxctrl</code> controls a number of vbox functions. The user&#8217;s password is asked before performing the requested action.</p>
<h3>OPTIONS</h3>
<dl>
<dt><i>-c, &#8211;create</i></dt>
<dd> Creates a control file.</dd>
<dt><i>-r, &#8211;remove</i></dt>
<dd> Removes a control file (default).</dd>
<dt><i>-n, &#8211;answernow</i></dt>
<dd> Control file &quot;vboxctrl-answernow&quot;.</dd>
<dt><i>-a, &#8211;answerall</i></dt>
<dd> Control file &quot;vboxctrl-answerall&quot;.</dd>
<dt><i>-p, &#8211;stop</i></dt>
<dd> Control file &quot;vboxctrl-stop&quot;.</dd>
<dt><i>-j, &#8211;reject</i></dt>
<dd> Control file &quot;vboxctrl-reject&quot;.</dd>
<dt><i>-s, &#8211;spooldir</i></dt>
<dd> Spooldirectory in which to create/remove control files.</dd>
<dt><i>-v, &#8211;version</i></dt>
<dd> Displays package version.</dd>
<dt><i>-h, &#8211;help</i></dt>
<dd> Displays a usage message.</dd></dl>
<p> The spool directory is taken from one of the following:</p>
<dl>
<dt><i>1</i></dt>
<dd> the default builtin value</dd>
<dt><i>2</i></dt>
<dd> The value of the environment variable VBOXSPOOL, if set.</dd>
<dt><i>3</i></dt>
<dd> The directory of the command line option &quot;&#8211;spooldir&quot;. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vbox/">vbox</a>(1), <a href="/docs/linux/man/8-vboxd/">vboxd</a>(8)</code> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Paul Slootman &lt;paul [at] debian.org&gt;, for Debian GNU/Linux and isdn4linux. </p>
