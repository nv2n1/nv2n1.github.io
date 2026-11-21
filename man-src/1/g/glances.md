---

title: "glances(1)"
name: "glances"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glances/"
description: "glances – A cross-platform curses-based monitoring tool"
---

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
<dt><code>-b</code></dt>
<dd> Display network rate in Byte per second (default: bit per second)</dd>
<dt><code>-B @IP|HOST</code></dt>
<dd> Bind server to the given IPv4/IPv6 address or hostname</dd>
<dt><code>-c @IP|HOST</code></dt>
<dd> Connect to a Glances server by IPv4/IPv6 address or hostname</dd>
<dt><code>-C FILE</code></dt>
<dd> Path to the configuration file</dd>
<dt><code>-d</code></dt>
<dd> Disable disk I/O module</dd>
<dt><code>-e</code></dt>
<dd> Enable sensors module (requires pysensors, Linux-only)</dd>
<dt><code>-f FOLDER</code></dt>
<dd> Set the HTML or CSV output folder</dd>
<dt><code>-h</code></dt>
<dd> Display the help and exit</dd>
<dt><code>-m</code></dt>
<dd> Disable mount module</dd>
<dt><code>-n</code></dt>
<dd> Disable network module</dd>
<dt><code>-o OUTPUT</code></dt>
<dd> Define additional output (available: HTML or CSV)</dd>
<dt><code>-p PORT</code></dt>
<dd> Define the client/server TCP port (default: 61209)</dd>
<dt><code>-P PASSWORD</code></dt>
<dd> Define a client/server password</dd>
<dt><code>&#8211;password</code></dt>
<dd> Define a client/server password from the prompt</dd>
<dt><code>-r</code></dt>
<dd> Disable process list (for low CPU consumption)</dd>
<dt><code>-s</code></dt>
<dd> Run Glances in server mode</dd>
<dt><code>-t SECONDS</code></dt>
<dd> Set refresh time in seconds (default: 3 sec)</dd>
<dt><code>-v</code></dt>
<dd> Display the version and exit</dd>
<dt><code>-y</code></dt>
<dd> Enable hddtemp module (requires hddtemp)</dd>
<dt><code>-z</code></dt>
<dd> Do not use the bold color attribute</dd>
<dt><code>-1</code></dt>
<dd> Start Glances in per-CPU mode</dd></dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> You can use the following keys while in Glances:</p>
<dl>
<dt><code>a</code></dt>
<dd> Sort process list automatically</dd>
<dt><code>b</code></dt>
<dd> Switch between bit/s or Byte/s for network I/O</dd>
<dt><code>c</code></dt>
<dd> Sort processes by CPU usage</dd>
<dt><code>d</code></dt>
<dd> Show/hide disk I/O stats</dd>
<dt><code>f</code></dt>
<dd> Show/hide file system stats</dd>
<dt><code>h</code></dt>
<dd> Show/hide the help screen</dd>
<dt><code>i</code></dt>
<dd> Sort processes by I/O rate</dd>
<dt><code>l</code></dt>
<dd> Show/hide log messages</dd>
<dt><code>m</code></dt>
<dd> Sort processes by MEM usage</dd>
<dt><code>n</code></dt>
<dd> Show/hide network stats</dd>
<dt><code>p</code></dt>
<dd> Sort processes by name</dd>
<dt><code>q</code></dt>
<dd> Quit</dd>
<dt><code>s</code></dt>
<dd> Show/hide sensors stats (only available with -e flag)</dd>
<dt><code>t</code></dt>
<dd> View network I/O as combination</dd>
<dt><code>u</code></dt>
<dd> View cumulative network I/O</dd>
<dt><code>w</code></dt>
<dd> Delete finished warning log messages</dd>
<dt><code>x</code></dt>
<dd> Delete finished warning and critical log messages</dd>
<dt><code>y</code></dt>
<dd> Show/hide hddtemp stats (only available with -y flag)</dd>
<dt><code>z</code></dt>
<dd> Show/hide processes list (for low CPU consumption)</dd>
<dt><code>1</code></dt>
<dd> Switch between global CPU and per-CPU stats</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Refresh information every 5 seconds:</dt>
<dd> <code>glances</code> -t 5</dd></dl>
<h2>EXIT STATUS</h2>
<p> Glances returns a zero exit status if it succeeds to print/grab information. </p>
<p> It returns 2 if it fails to parse its options (missing arguments, invalid value, etc).</p>
<h2>AUTHOR</h2>
<p> Glances is written by Nicolas Hennion aka Nicolargo (contact [at] nicolargo.com) </p>
