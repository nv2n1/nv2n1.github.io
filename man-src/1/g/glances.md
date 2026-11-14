---
title: "glances(1)"
name: "glances"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glances/"
description: "glances – A cross-platform curses-based monitoring tool"
---

<h2>NAME</h2>
<p> glances &#8211; A cross-platform curses-based monitoring tool</p>
<h2>SYNOPSIS</h2>
<p> <code>glances</code> [-bdehmnrsvyz1] [-B bind] [-c server] [-C conffile] [-p port] [-P password] [&#8211;password] [-t refresh] [-f file] [-o output]</p>
<h2>DESCRIPTION</h2>
<p> Glances is a free (LGPL) cross-platform curses-based monitoring tool which aims to present a maximum of information in a minimum of space, ideally to fit in a classical 80&#215;24 terminal or higher to have additionnal information. </p>
<p> Glances can adapt dynamically the displayed information depending on the terminal size. It can also work in a client/server mode for remote monitoring. </p>
<p> This tool is written in Python and uses the psutil library to fetch the statistical values from key elements, like CPU, load average, memory, network, disks, file systems, processes, etc.</p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> The command-line options are the following:</p>
<dl>
<dt><code>-b</code></p>
<dd> Display network rate in Byte per second (default: bit per second)</p>
<dt><code>-B @IP|HOST</code></p>
<dd> Bind server to the given IPv4/IPv6 address or hostname</p>
<dt><code>-c @IP|HOST</code></p>
<dd> Connect to a Glances server by IPv4/IPv6 address or hostname</p>
<dt><code>-C FILE</code></p>
<dd> Path to the configuration file</p>
<dt><code>-d</code></p>
<dd> Disable disk I/O module</p>
<dt><code>-e</code></p>
<dd> Enable sensors module (requires pysensors, Linux-only)</p>
<dt><code>-f FOLDER</code></p>
<dd> Set the HTML or CSV output folder</p>
<dt><code>-h</code></p>
<dd> Display the help and exit</p>
<dt><code>-m</code></p>
<dd> Disable mount module</p>
<dt><code>-n</code></p>
<dd> Disable network module</p>
<dt><code>-o OUTPUT</code></p>
<dd> Define additional output (available: HTML or CSV)</p>
<dt><code>-p PORT</code></p>
<dd> Define the client/server TCP port (default: 61209)</p>
<dt><code>-P PASSWORD</code></p>
<dd> Define a client/server password</p>
<dt><code>&#8211;password</code></p>
<dd> Define a client/server password from the prompt</p>
<dt><code>-r</code></p>
<dd> Disable process list (for low CPU consumption)</p>
<dt><code>-s</code></p>
<dd> Run Glances in server mode</p>
<dt><code>-t SECONDS</code></p>
<dd> Set refresh time in seconds (default: 3 sec)</p>
<dt><code>-v</code></p>
<dd> Display the version and exit</p>
<dt><code>-y</code></p>
<dd> Enable hddtemp module (requires hddtemp)</p>
<dt><code>-z</code></p>
<dd> Do not use the bold color attribute</p>
<dt><code>-1</code></p>
<dd> Start Glances in per-CPU mode</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> You can use the following keys while in Glances:</p>
<dl>
<dt><code>a</code></p>
<dd> Sort process list automatically</p>
<dt><code>b</code></p>
<dd> Switch between bit/s or Byte/s for network I/O</p>
<dt><code>c</code></p>
<dd> Sort processes by CPU usage</p>
<dt><code>d</code></p>
<dd> Show/hide disk I/O stats</p>
<dt><code>f</code></p>
<dd> Show/hide file system stats</p>
<dt><code>h</code></p>
<dd> Show/hide the help screen</p>
<dt><code>i</code></p>
<dd> Sort processes by I/O rate</p>
<dt><code>l</code></p>
<dd> Show/hide log messages</p>
<dt><code>m</code></p>
<dd> Sort processes by MEM usage</p>
<dt><code>n</code></p>
<dd> Show/hide network stats</p>
<dt><code>p</code></p>
<dd> Sort processes by name</p>
<dt><code>q</code></p>
<dd> Quit</p>
<dt><code>s</code></p>
<dd> Show/hide sensors stats (only available with -e flag)</p>
<dt><code>t</code></p>
<dd> View network I/O as combination</p>
<dt><code>u</code></p>
<dd> View cumulative network I/O</p>
<dt><code>w</code></p>
<dd> Delete finished warning log messages</p>
<dt><code>x</code></p>
<dd> Delete finished warning and critical log messages</p>
<dt><code>y</code></p>
<dd> Show/hide hddtemp stats (only available with -y flag)</p>
<dt><code>z</code></p>
<dd> Show/hide processes list (for low CPU consumption)</p>
<dt><code>1</code></p>
<dd> Switch between global CPU and per-CPU stats</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Refresh information every 5 seconds:</p>
<dd> <code>glances</code> -t 5</dl>
<h2>EXIT STATUS</h2>
<p> Glances returns a zero exit status if it succeeds to print/grab information. </p>
<p> It returns 2 if it fails to parse its options (missing arguments, invalid value, etc).</p>
<h2>AUTHOR</h2>
<p> Glances is written by Nicolas Hennion aka Nicolargo (contact [at] nicolargo.com) </p>
<h2>Index</h2>
