---
title: "cyberjack(8)"
name: "cyberjack"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyberjack/"
description: "cyberjack — configuration and testing utility"
---

<p>cyberjack &#8212; configuration and testing utility</p>
<h2>Synopsis</h2>
<p>cyberjack [COMMAND] [ARGUMENTS] </p>
<h2>Description</h2>
<p>cyberjack helps you in case of troubleshooting as well as for configuration of your CyberJack card reader. Using the &quot;check&quot; command, it will create 3 files:</p>
<dl>
<dt>cyberjack-report.log</p>
<dd>with the test results</p>
<dt>cyberjack-hints.log</p>
<dd>with possible hints for you to solve the issue you may have</p>
<dt>cyberjack.xml</p>
<dd>with detailed results for the support team </p>
<h2>Options</h2>
<dl>
<dt><code>check</code></p>
<dd>perform system checks </p>
<dt><code>addflags &lt;flag&gt;</code></p>
<dd>adds flags in the CTAPI configuration file. This command needs an argument (the flags to add) </p>
<dt><code>delflags &lt;flag&gt;</code></p>
<dd>clears flags in the CTAPI configuration file. This command needs an argument (the flags to add) </p>
<dt><code>beep1</code></p>
<dd>Beeps using /dev/console </p>
<dt><code>beep2</code></p>
<dd>Beeps by outputting sending a control character to stdout </p>
<dt><code>beep3</code></p>
<dd>Beeps using a running X11 server </p>
</dl>
<h2>Examples</h2>
<p>cyberjack check cyberjack addflags 0xffff cyberjack delflags 0xff00 cyberjack &#8211;help </p>
