---
title: "lvmlockctl(8)"
name: "lvmlockctl"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvmlockctl/"
description: "lvmlockctl — Control for lvmlockd"
---

<p>lvmlockctl &#8212; Control for lvmlockd</p>
<h2>Description</h2>
<p>This command interacts with <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8). </p>
<h2>Options</h2>
<p>lvmlockctl [options] </p>
<p> <code>&#8211;help | -h</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show this help information. </p>
<p> <code>&#8211;quit | -q</code><br />
&nbsp;<wbr>&nbsp;<wbr>Tell lvmlockd to quit. </p>
<p> <code>&#8211;info | -i</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print lock state information from lvmlockd. </p>
<p> <code>&#8211;dump | -d</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print log buffer from lvmlockd. </p>
<p> <code>&#8211;wait | -w 0|1</code><br />
&nbsp;<wbr>&nbsp;<wbr>Wait option for other commands. </p>
<p> <code>&#8211;force | -f 0|1</code><br />
&nbsp;<wbr>&nbsp;<wbr>Force option for other commands. </p>
<p> <code>&#8211;kill | -k</code> <i>vgname</i><br />
&nbsp;<wbr>&nbsp;<wbr>Kill access to the VG when sanlock cannot renew lease. </p>
<p> <code>&#8211;drop | -r</code> <i>vgname</i><br />
&nbsp;<wbr>&nbsp;<wbr>Clear locks for the VG when it is unused after kill&nbsp;<wbr>(-k). </p>
<p> <code>&#8211;gl-enable | -E</code> <i>vgname</i><br />
&nbsp;<wbr>&nbsp;<wbr>Tell lvmlockd to enable the global lock in a sanlock VG. </p>
<p> <code>&#8211;gl-disable | -D</code> <i>vgname</i><br />
&nbsp;<wbr>&nbsp;<wbr>Tell lvmlockd to disable the global lock in a sanlock VG. </p>
<p> <code>&#8211;stop-lockspaces | -S</code><br />
&nbsp;<wbr>&nbsp;<wbr>Stop all lockspaces.</p>
<h2>Usage</h2>
<h3>info</h3>
<p>This collects and displays lock state from lvmlockd. The display is primitive, incomplete and will change in future version. To print the raw lock state from lvmlockd, combine this option with &#8211;dump|-d.</p>
<h3>dump</h3>
<p>This collects the circular log buffer of debug statements from lvmlockd and prints it.</p>
<h3>kill</h3>
<p>This is run by sanlock when it loses access to the storage holding leases for a VG. It currently emits a syslog message stating that the VG must be immediately deactivated. In the future it may automatically attempt to forcibly deactivate the VG. For more, see <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8).</p>
<h3>drop</h3>
<p>This should only be run after a VG has been successfully deactivated following an lvmlockctl &#8211;kill command. It clears the stale lockspace from lvmlockd. In the future, this may become automatic along with an automatic handling of &#8211;kill. For more, see <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8).</p>
<h3>gl-enable</h3>
<p>This enables the global lock in a sanlock VG. This is necessary if the VG that previously held the global lock is removed. For more, see <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8).</p>
<h3>gl-disable</h3>
<p>This disables the global lock in a sanlock VG. This is necessary if the global lock has mistakenly been enabled in more than one VG. The global lock should be disabled in all but one sanlock VG. For more, see <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8).</p>
<h3>stop-lockspaces</h3>
<p>This tells lvmlockd to stop all lockspaces. It can be useful to stop lockspaces for VGs that the vgchange &#8211;lock-stop comand can no longer see, or to stop the dlm global lockspace which is not directly stopped by the vgchange command. The wait and force options can be used with this command.</p>
