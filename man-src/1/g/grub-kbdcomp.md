---

title: "grub-kbdcomp(1)"
name: "grub-kbdcomp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-kbdcomp/"
description: "grub-kbdcomp – generate a GRUB keyboard layout file"
---

<p> <code>grub-kbdcomp</code> <i>,-o OUTPUT CKBMAP_ARGUMENTS/</i>&#8230;</p>
<p> grub-kbdcomp processes a X keyboard layout description in <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) format into a format that can be used by GRUB&#8217;s <code>keymap</code> command. </p>
<p> Make GRUB keyboard layout file.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> print this message and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print the version information and exit</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> save output in FILE [required]</dd></dl>
<p> grub-kbdcomp generates a keyboard layout for GRUB using ckbcomp</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code>grub-mklayout</code>(8) </p>
<p> The full documentation for <code>grub-kbdcomp</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-kbdcomp</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-kbdcomp</code></dd></dl>
<p> should give you access to the complete manual. </p>
