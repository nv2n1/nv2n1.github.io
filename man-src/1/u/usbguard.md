---
title: "usbguard(1)"
name: "usbguard"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usbguard/"
---

<h2>NAME</h2>

 

 usbguard -- USBGuard command-line interface

<h2>SYNOPSIS</h2>

 

 usbguard&nbsp;<wbr>[OPTIONS]&nbsp;<wbr>command&nbsp;<wbr>[COMMAND-OPTIONS]&nbsp;<wbr>... 

 usbguard list-devices 

 usbguard allow-device&nbsp;<wbr>&lt;id&gt; 

 usbguard block-device&nbsp;<wbr>&lt;id&gt; 

 usbguard reject-device&nbsp;<wbr>&lt;id&gt; 

 usbguard list-rules 

 usbguard append-rule&nbsp;<wbr>&lt;rule&gt; 

 usbguard remove-rule&nbsp;<wbr>&lt;id&gt; 

 usbguard generate-policy 

 usbguard watch 

 usbguard read-descriptor &lt;file&gt;

<h2>DESCRIPTION</h2>

 

 The usbguard command provides a command-line interface (CLI) to the <a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8) instance and provides a tool for generating initial USBGuard policies.

<h2>SUBCOMMANDS</h2>

 

 list-devices 

 List all USB devices recognized by the USBGuard daemon. 

 Available options:
<dl>
<dt>-a, --allowed
<dd> List allowed devices.
<dl>
<dt>
<dd></dl>

<dt>-b, --blocked
<dd> List blocked devices.
<dl>
<dt>
<dd></dl>

<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 allow-device [OPTIONS] &lt;id&gt; 

 Authorize a device identified by the device id to interact with the system. 

 Available options:
<dl>
<dt>-p, --permanent
<dd> Make the decision permanent. A device specific allow rule will be appended to the current policy.
<dl>
<dt>
<dd></dl>

<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 block-device [OPTIONS] &lt;id&gt; 

 Deauthorize a device identified by the device id. 

 Available options:
<dl>
<dt>-p, --permanent
<dd> Make the decision permanent. A device specific block rule will be appended to the current policy.
<dl>
<dt>
<dd></dl>

<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 reject-device [OPTIONS] &lt;id&gt; 

 Deauthorize and remove a device identified by the device id. 

 Available options:
<dl>
<dt>-p, --permanent
<dd> Make the decision permanent. A device specific reject rule will be appended to the current policy.
<dl>
<dt>
<dd></dl>

<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 list-rules [OPTIONS] 

 List the rule set (policy) used by the USBGuard daemon. 

 Available options:
<dl>
<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 append-rule [OPTIONS] &lt;rule&gt; 

 Append the rule to the current rule set. 

 Available options:
<dl>
<dt>-a, --after &lt;id&gt;
<dd> Append the new rule after a rule with the specified rule id.
<dl>
<dt>
<dd></dl>

<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 remove-rule [OPTIONS] &lt;id&gt; 

 Remove a rule identified by the rule id from the rule set. 

 Available options:
<dl>
<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 generate-policy [OPTIONS] 

 Generate a rule set (policy) which authorizes the currently connected USB devices. 

 Available options:
<dl>
<dt>-p, --with-ports
<dd> Generate port specific rules for all devices. By default, port specific rules are generated only for devices which do not export an iSerial value.
<dl>
<dt>
<dd></dl>

<dt>-P, --no-ports-sn
<dd> Don't generate port specific rules for devices without an iSerial value. Without this option, the tool will add a via-port attribute to any device that doesn't provide a serial number. This is a security measure to limit devices that cannot be uniquely identified to connect only via a specific port. This makes it harder to bypass the policy since the real device will occupy the allowed USB port most of the time.
<dl>
<dt>
<dd></dl>

<dt>-t, --target &lt;target&gt;
<dd> Generate an explicit &quot;catch all&quot; rule with the specified target. The target can be one of the following values: allow, block, reject
<dl>
<dt>
<dd></dl>

<dt>-X, --no-hashes
<dd> Don't generate a hash attribute for each device.
<dl>
<dt>
<dd></dl>

<dt>-H, --hash-only
<dd> Generate a hash-only policy.
<dl>
<dt>
<dd></dl>

<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 watch [OPTIONS] 

 Watch the IPC interface events and print them to stdout. 

 Available options:
<dl>
<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>
 

 ~ ~ ~ ~ 

 read-descriptor [OPTIONS] &lt;file&gt; 

 Read a USB descriptor from a file and print it in human-readable form. 

 Available options:
<dl>
<dt>-h, --help
<dd> Show help.
<dl>
<dt>
<dd></dl>
</dl>

<h2>EXAMPLES</h2>

 

 Creating an initial policy
<dl>
<dt>
<dd> <pre><code>
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
$ &amp;nbsp;
sudo usbguard generate - policy &amp;nbsp;
&gt; &amp;nbsp;
rules.conf
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
$ &amp;nbsp;
vi rules.conf
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
(review / modify the rule set) &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
$ &amp;nbsp;
sudo install - m 0600 - o root - g root &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
rules.conf &amp;nbsp;
/ etc / usbguard / rules.conf
</code></pre></dl>

<h2>BUGS</h2>

 

 If you find a bug in this software or if you'd like to request a feature to be implemented, please file a ticket at &lt;<a rel="nofollow" HREF="https://github.com/dkopecek/usbguard/issues/new">https://github.com/dkopecek/usbguard/issues/new</a>&gt;.

<h2>COPYRIGHT</h2>

 

 Copyright © 2015 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-usbguard-rules-conf/">usbguard-rules.conf</a>(5), <a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8), <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5)

<h2>AUTHORS</h2>

 Daniel Kopeček &lt;dkopecek [at] redhat.com&gt;. 

<h2>Index</h2>


