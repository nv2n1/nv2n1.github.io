---
title: "systemd-run-generator(8)"
name: "systemd-run-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-run-generator/"
description: "systemd-run-generator – Generator for invoking commands specified on the kernel command line as system service"
---

<p>systemd-run-generator &#8211; Generator for invoking commands specified on the kernel command line as system service</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-run-generator</p>
<h2>Description</h2>
<p>systemd-run-generator is a generator that reads the kernel command line and understands three options: </p>
<p> If the <code>systemd.run=</code> option is specified and followed by a command line, a unit named kernel-command-line.service is generated for it and booted into. The service has <i>Type=oneshot</i> set, and has <i>SuccessAction=exit</i> and <i>FailureAction=exit</i> configured by default, thus ensuring that the system is shut down as soon as the command completes. The exit status of the command line is propagated to the invoking container manager, if this applies (which might propagate this further, to the calling shell &#8212; e.g. <code><a href="/docs/linux/man/7-systemd-nspawn/">systemd-nspawn</a></code>(7) does this). If this option is used multiple times the unit file will contain multiple <i>ExecStart=</i> lines, to execute all commands in order. The command is started as regular service, i.e. with <i>DefaultDependencies=</i> on. </p>
<p> Use <code>systemd.run_success_action=</code> and <code>systemd.run_failure_action=</code> to tweak how to react to the process completing. In particular assigning &quot;none&quot; will leave the system running after the command completes. For further details on supported arguments, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). </p>
<p> systemd-run-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>Example</h2>
<p>Use a command like the following to add a user to the user database inside a container run with <code><a href="/docs/linux/man/7-systemd-nspawn/">systemd-nspawn</a></code>(7): </p>
<dl>
<dd>
<pre># systemd-nspawn -D mycontainer -b systemd.run='&quot;adduser test&quot;'</pre>
</dl>
<p> (Note the requirement for double quoting in the command line above. The first level of quoting (&#8221;) is processed and removed by the command shell used to invoke <code>systemd-nspawn</code>. The second level of quoting (&quot;&quot;) is propagated to the kernel command line of the container and processed and removed by <code>systemd-run-generator</code>. Both together make sure both words of the specified command line <code>adduser test</code> end up in the generated unit file together and are neither split apart by the command shell nor by the generator.)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7), <code><a href="/docs/linux/man/7-systemd-nspawn/">systemd-nspawn</a></code>(7), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) </p>
