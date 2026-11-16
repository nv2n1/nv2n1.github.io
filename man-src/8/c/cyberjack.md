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
<dt>cyberjack-report.log</dt>
<dd>with the test results</dd>
<dt>cyberjack-hints.log</dt>
<dd>with possible hints for you to solve the issue you may have</dd>
<dt>cyberjack.xml</dt>
<dd>with detailed results for the support team </dd>
<h2>Options</h2>
<dl>
<dt><code>check</code></dt>
<dd>perform system checks </dd>
<dt><code>addflags &lt;flag&gt;</code></dt>
<dd>adds flags in the CTAPI configuration file. This command needs an argument (the flags to add) </dd>
<dt><code>delflags &lt;flag&gt;</code></dt>
<dd>clears flags in the CTAPI configuration file. This command needs an argument (the flags to add) </dd>
<dt><code>beep1</code></dt>
<dd>Beeps using /dev/console </dd>
<dt><code>beep2</code></dt>
<dd>Beeps by outputting sending a control character to stdout </dd>
<dt><code>beep3</code></dt>
<dd>Beeps using a running X11 server </dd>
</dl>
<h2>Examples</h2>
<p>cyberjack check cyberjack addflags 0xffff cyberjack delflags 0xff00 cyberjack &#8211;help </p>
</dl>