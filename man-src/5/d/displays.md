---
title: "displays(5)"
name: "displays"
section: "5"
letter: "d"
url: "/docs/linux/man/5-displays/"
description: "displays – Display Configuration File"
---

<p>displays &#8211; Display Configuration File</p>
<h2>Description</h2>
<p>The interactive graphics programs Caesar, Magic, and Gremlin use two separate terminals: a text terminal from which commands are issued, and a color graphics terminal on which graphical output is displayed. These programs use a <code>displays</code> file to associate their text terminal with its corresponding display device. The <code>displays</code> file is an ASCII text file with one line for each text terminal/graphics terminal pair. Each line contains 4 items separated by spaces: the name of the port attached to a text terminal, the name of the port attached to the associated graphics terminal, the phosphor type of the graphics terminal&#8217;s monitor, and the type of graphics terminal. An applications program may use the phosphor type to select a color map tuned to the monitor&#8217;s characteristics. Only the <code>std</code> phosphor type is supported at UC Berkeley. The graphics terminal type specifies the device driver a program should use when communicating with its graphics terminal. Magic supports types <code>UCB512</code>, <code>AED1024</code>, and <code>SUN120</code>. Other programs may recognize different display types. See the manual entry for your specific application for more information. A sample displays file is: <code><br />
 </code> /dev/ttyi1 /dev/ttyi0 std UCB512<br />
 /dev/ttyj0 /dev/ttyj1 std UCB512<br />
 /dev/ttyjf /dev/ttyhf std UCB512<br />
 /dev/ttyhb /dev/ttyhc std UCB512<br />
 /dev/ttyhc /dev/ttyhb std UCB512<br />
 In this example, <code>/dev/ttyi1</code> connects to a text terminal. An associated <code>UCB512</code> graphics terminal with standard phosphor is connected to <code>/dev/ttyi0</code>. </p>
<h2>Files</h2>
<p>Magic uses the displays file ~cad/lib/displays. Gremlin looks in /usr/local/displays.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-magic/">magic</a>(1) </p>
