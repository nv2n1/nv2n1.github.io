---
title: "ipc_parse_version(9)"
name: "ipc_parse_version"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_parse_version/"
---

ipc_parse_version - ipc call version

<h2>Synopsis</h2>

<pre><code>int ipc_parse_version(int *cmd);</code></pre>

<h2>Arguments</h2>

<i>cmd</i>
<dl><dd><dd>pointer to command</dl>

<h2>Description</h2>

Return IPC_64 for new style IPC and IPC_OLD for old style IPC. The <i>cmd</i> value is turned from an encoding command and version into just the command code.

<h2>Copyright</h2>


