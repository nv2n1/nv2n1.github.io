---
title: "nameif(8)"
name: "nameif"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nameif/"
description: "nameif – name network interfaces based on MAC addresses"
---

<p>nameif &#8211; name network interfaces based on MAC addresses</p>
<h2>Synopsis</h2>
<p><code>nameif [-c configfile] [-s]</code><br />
 <code>nameif [-c configfile] [-s] {interface macaddress}</code></p>
<h2>Description</h2>
<p><code>nameif </code> renames network interfaces based on mac addresses. When no arguments are given <i>/etc/mactab</i> is read. Each line of it contains an interface name and a Ethernet MAC address. Comments are allowed starting with #. Otherwise the interfaces specified on the command line are processed. <i>nameif</i> looks for the interface with the given MAC address and renames it to the name given. When the <i>-s</i> argument is given all error messages go to the syslog. When the <i>-c </i> argument is given with a file name that file is read instead of /etc/mactab. </p>
<h2>Notes</h2>
<p><i>nameif</i> should be run before the interface is up, otherwise it&#8217;ll fail. </p>
<h2>Files</h2>
<p>/etc/mactab</p>
<h2>Bugs</h2>
<p>Only works for Ethernet currently. </p>
