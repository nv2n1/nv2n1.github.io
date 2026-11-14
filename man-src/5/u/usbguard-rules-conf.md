---
title: "usbguard-rules-conf(5)"
name: "usbguard-rules-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-usbguard-rules-conf/"
---

usbguard-rules.conf -- USBGuard rule set file

<h2>Description</h2>

The usbguard-rules.conf file is loaded by the USBGuard daemon after it parses the main configuration file, <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5). The daemon expects the file to contain rules written in a rule language which is described in the Rule Language section below.

<h2>Rule Language</h2>

The USBGuard daemon decides which USB device to authorize based on a policy defined by a set of rules. When a USB device is inserted into the system, the daemon scans the existing rules sequentially and when a matching rule is found, it either authorizes (allows), deauthorizes (blocks) or removes (rejects) the device, based on the rule target. If no matching rule is found, the decision is based on an implicit default target. This implicit default is to block the device until a decision is made by the user. The rule language grammar, expressed in a BNF-like syntax, is the following:
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rule ::=&nbsp;<wbr>target attributes.
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>target ::=&nbsp;<wbr>&quot;allow&quot;&nbsp;<wbr>|&nbsp;<wbr>&quot;block&quot;&nbsp;<wbr>|&nbsp;<wbr>&quot;reject&quot;.
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>attributes ::=&nbsp;<wbr>attributes | attribute.
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>attributes ::=&nbsp;<wbr>.</pre></dl>
 

 Rule attributes specify which devices to match or what condition have to be met for the rule to be applicable. See the Device Attributes section for the list of available attributes and Conditions for the list of supported rule conditions.

<h3>Targets</h3>

The target of a rule specifies whether the device will be authorized for use or not. Three types of target are recognized:
<dl><dt>&bull;
<dd>allow -- Authorize the device. The device and its interfaces will be allowed to communicate with the system.
<dt>&bull;
<dd>block -- Deauthorize the device, i.e. don't talk to the device for now.
<dt>&bull;
<dd>reject -- Remove the device from the system, i.e. ignore the device as if didn't exist.</dl>

<h3>Device Specification</h3>

Except the target, all the other fields of a rule need not be specified. Such a minimal rule will match any device and allows the policy creator to write an explicit default target. If no rule from the policy is applicable to the device, an implicit target configured in <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5) will be used. However, if one wants to narrow the applicability of a rule to a set of devices or one device only, it's possible to do so with device attributes and rule conditions.

<h3>Device Attributes</h3>

Device attributes are specific values read from the USB device after it's inserted to the system. Which attributes are available is defined below. Some of the attributes are derived and some are based on attributes read directly from the device. All attributes support two forms:
<dl><dt>&bull;
<dd>single-valued with a syntax name value
<dt>&bull;
<dd>multi-valued with a syntax name&nbsp;<wbr>[operator]&nbsp;<wbr>{&nbsp;<wbr>value1 value2 ...&nbsp;<wbr>}</dl>
 

 where the optional operator is one of:
<dl><dt>&bull;
<dd>all-of -- The device attribute set must contain all of the specified values for the rule to match.
<dt>&bull;
<dd>one-of -- The device attribute set must contain at least one of the specified values for the rule to match.
<dt>&bull;
<dd>none-of -- The device attribute set must not contain any of the specified values for the rule to match.
<dt>&bull;
<dd>equals -- The device attribute set must contain exactly the same set of values for the rule to match.
<dt>&bull;
<dd>equals-ordered -- The device attribute set must contain exactly the same set of values in the same order for the rule to match.</dl>
 

 If the operator is not specified it is set to equals. 

 List of attributes:
<dl><dt>id usb-device-id
<dd>Match a USB device ID.
<dl><dd></dl><dt>id [operator]&nbsp;<wbr>{&nbsp;<wbr>usb-device-id ...&nbsp;<wbr>}
<dd>Match a set of USB device IDs.
<dl><dd></dl><dt>hash value
<dd>Match a hash computed from the device attribute values and the USB descriptor data. The hash is computed for every device by USBGuard.
<dl><dd></dl><dt>hash [operator]&nbsp;<wbr>{&nbsp;<wbr>value ...&nbsp;<wbr>}
<dd>Match a set of device hashes.
<dl><dd></dl><dt>parent-hash value
<dd>Match a hash of the parent device.
<dl><dd></dl><dt>parent-hash [operator]&nbsp;<wbr>{&nbsp;<wbr>value ...&nbsp;<wbr>}
<dd>Match a set of parent device hashes.
<dl><dd></dl><dt>name device-name
<dd>Match the USB device name attribute.
<dl><dd></dl><dt>name [operator]&nbsp;<wbr>{&nbsp;<wbr>device-name ...&nbsp;<wbr>}
<dd>Match a set of USB device names.
<dl><dd></dl><dt>serial serial-number
<dd>Match the USB iSerial device attribute.
<dl><dd></dl><dt>serial [operator]&nbsp;<wbr>{&nbsp;<wbr>serial-number ...&nbsp;<wbr>}
<dd>Match a set of USB iSerial device attributes.
<dl><dd></dl><dt>via-port port-id
<dd>Match the USB port through which the device is connected. Note that some systems have unstable port numbering which change after the system reboots or certain kernel modules are reloaded (and maybe in other cases). Use the parent-hash attribute if you want to ensure that a device is connected via a specific parent device.
<dl><dd></dl><dt>via-port [operator]&nbsp;<wbr>{&nbsp;<wbr>port-id ...&nbsp;<wbr>}
<dd>Match a set of USB ports.
<dl><dd></dl><dt>with-interface interface-type
<dd>Match an interface type that the USB device provides.
<dl><dd></dl><dt>with-interface
<dd>[operator]&nbsp;<wbr>{&nbsp;<wbr>interface-type interface-type ...&nbsp;<wbr>} Match a set of interface types against the set of interfaces that the USB device provides.
<dl><dd></dl></dl>
 

 The usb-device-id is a colon delimited pair in the form vendor_id:product_id. All USB devices have this ID assigned by the manufacturer and it should uniquely identify a USB product. Both vendor_id and product_id are 16-bit numbers represented in hexadecimal base. It's possible to use an asterisk character to match either any device ID *:* or any product ID from a specific vendor, e.g. 1234:*. 

 The port-id value is a platform specific USB port identification. On Linux it's in the form of &quot;usbN&quot; in case of a USB controller (more accurately a &quot;root hub&quot;) or &quot;bus-port[.port[.port ...]]&quot; (e.g. &quot;1-2&quot;, &quot;1-2.1&quot;, ...). 

 The interface-type represents a USB interface and should be formatted as three 8-bit numbers in hexadecimal base delimited by a colon character, i.e. cc:ss:pp. The numbers represent the interface class (cc), subclass (ss) and protocol (pp) as assigned by the USB-IF (<a rel="nofollow" HREF="http://www.usb.org/about">http://www.usb.org/about</a>). See the list of assigned classes, subclasses and protocols (<a rel="nofollow" HREF="http://www.usb.org/developers/defined_class">http://www.usb.org/developers/defined_class</a>). Instead of the subclass and protocol number, you may write an asterisk character (*) to match all subclasses or protocols. Matching a specific class and a specific protocol is not allowed, i.e. if you use an asterisk as the subclass number, you have to use an asterisk for the protocol too.

<h3>Conditions</h3>

Whether a rule that matches a device will be applied or not can be further restricted using rule conditions. If the condition expression is met at the rule evaluation time, then the rule target is applied for the device. A condition expression is met if it evaluates to true. Otherwise, the rule evaluation continues with the next rule. A rule conditions has the following syntax:
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>[!]condition
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>[operator]&nbsp;<wbr>{&nbsp;<wbr>[!]conditionA&nbsp;<wbr>[!]conditionB ...&nbsp;<wbr>}</pre></dl>
 

 Optionally, an exclamation mark (!) can be used to negate the result of a condition. 

 Interpretation of the set operator:
<dl><dt>&bull;
<dd>all-of -- Evaluate to true if all of the specified conditions evaluated to true.
<dt>&bull;
<dd>one-of -- Evaluate to true if one of the specified conditions evaluated to true.
<dt>&bull;
<dd>none-of -- Evaluate to true if none of the specified conditions evaluated to true.
<dt>&bull;
<dd>equals -- Same as all-of.
<dt>&bull;
<dd>equals-ordered -- Same as all-of.</dl>
 

 List of conditions:
<dl><dt>localtime(time_range)
<dd>Evaluates to true if the local time is in the specified time range. time_range can be written either as HH:MM[:SS] or HH:MM[:SS]-HH:MM[:SS].
<dl><dd></dl><dt>allowed-matches(query)
<dd>Evaluates to true if an allowed device matches the specified query. The query uses the rule syntax. Conditions in the query are not evaluated.
<dl><dd></dl><dt>rule-applied
<dd>Evaluates to true if the rule currently being evaluated ever matched a device.
<dl><dd></dl><dt>rule-applied(past_duration)
<dd>Evaluates to true if the rule currently being evaluated matched a device in the past duration of time specified by the parameter. past_duration can be written as HH:MM:SS, HH:MM, or SS.
<dl><dd></dl><dt>rule-evaluated
<dd>Evaluates to true if the rule currently being evaluated was ever evaluated before.
<dl><dd></dl><dt>rule-evaluated(past_duration)
<dd>Evaluates to true if the rule currently being evaluated was evaluated in the pas duration of time specified by the parameter. past_duration can be written as HH:MM:SS, HH:MM, or SS.
<dl><dd></dl><dt>random
<dd>Evaluates to true/false with a probability of p=0.5.
<dl><dd></dl><dt>random(p_true)
<dd>Evaluates to true with the specified probability p_true.
<dl><dd></dl><dt>true
<dd>Evaluates always to true.
<dl><dd></dl><dt>false
<dd>Evaluates always to false.
<dl><dd></dl></dl>

<h3>Initial policy</h3>

Using the usbguard CLI tool and its generate-policy subcommand, you can generate an initial policy for your system instead of writing one from scratch. The tool generates an allow policy for all devices connected to the system at the moment of execution. It has several options to tweak the resulting policy, see <a HREF="/docs/linux/man/1-usbguard/">usbguard</a>(1) for further details. 

 The policy will be printed out on the standard output. It's a good idea to review the generated rules before using them on a system. The typical workflow for generating an initial policy could look like this:
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>usbguard generate-policy&nbsp;<wbr>&gt;&nbsp;<wbr>rules.conf
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>vi rules.conf
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(review/modify the rule set)
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sudo install -m 0600 -o root -g root rules.conf&nbsp;<wbr>/etc/usbguard/rules.conf
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sudo systemctl restart usbguard</pre></dl>

<h3>Example Policies</h3>

The following examples show what to put into the rules.conf file in order to implement the given policy. 

 1) Allow USB mass storage devices (USB flash disks) and block everything else 

 This policy will block any device that isn't just a mass storage device. Devices with a hidden keyboard interface in a USB flash disk will be blocked. Only devices with a single mass storage interface will be allowed to interact with the operating system. The policy consists of a single rule:
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow with-interface equals&nbsp;<wbr>{&nbsp;<wbr>08:*:*&nbsp;<wbr>}</pre></dl>
 

 The blocking is implicit in this case because we didn't write a block rule. Implicit blocking is useful to desktop users because a desktop applet listening to USBGuard events can ask the user for a decision if an implicit target was selected for a device. 

 2) Allow a specific Yubikey device to be connected via a specific port. Reject everything else on that port
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow 1050:0011 name&nbsp;<wbr>&quot;Yubico Yubikey II&quot;&nbsp;<wbr>serial&nbsp;<wbr>&quot;0001234567&quot;&nbsp;<wbr>via-port&nbsp;<wbr>&quot;1-2&quot;&nbsp;<wbr>hash&nbsp;<wbr>&quot;044b5e168d40ee0245478416caf3d998&quot;
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reject via-port&nbsp;<wbr>&quot;1-2&quot;</pre></dl>
 

 We could use just the hash to match the device. However, using the name and serial attributes allows the policy creator to quickly assign rules to specific devices without computing the hash. On the other hand, the hash is the most specific value we can use to identify a device in USBGuard so it's the best attribute to use if you want a rule to match just one device. 

 3) Reject devices with suspicious combination of interfaces 

 A USB flash disk which implements a keyboard or a network interface is very suspicious. The following set of rules forms a policy which allows USB flash disks and explicitly rejects devices with an additional and suspicious (as defined before) interface.
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow with-interface equals&nbsp;<wbr>{&nbsp;<wbr>08:*:*&nbsp;<wbr>}
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reject with-interface all-of&nbsp;<wbr>{&nbsp;<wbr>08:*:*&nbsp;<wbr>03:00:*&nbsp;<wbr>}
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reject with-interface all-of&nbsp;<wbr>{&nbsp;<wbr>08:*:*&nbsp;<wbr>03:01:*&nbsp;<wbr>}
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reject with-interface all-of&nbsp;<wbr>{&nbsp;<wbr>08:*:*&nbsp;<wbr>e0:*:*&nbsp;<wbr>}
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reject with-interface all-of&nbsp;<wbr>{&nbsp;<wbr>08:*:*&nbsp;<wbr>02:*:*&nbsp;<wbr>}</pre></dl>
 

 The policy rejects all USB flash disk devices with an interface from the HID/Keyboard, Communications and Wireless classes. Please note that blacklisting is the wrong approach and you shouldn't just blacklist a set of devices and allow the rest. The policy above assumes that blocking is the implicit default. Rejecting a set of devices considered as &quot;bad&quot; is a good approach how to limit the exposure of the OS to such devices as much as possible. 

 4) Allow a keyboard-only USB device only if there isn't already a USB device with a keyboard interface allowed
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow with-interface one-of&nbsp;<wbr>{&nbsp;<wbr>03:00:01 03:01:01&nbsp;<wbr>}&nbsp;<wbr>if&nbsp;<wbr>!allowed-matches(with-interface one-of&nbsp;<wbr>{&nbsp;<wbr>03:00:01 03:01:01&nbsp;<wbr>})</pre></dl>
 

 5) Play &quot;Russian roulette&quot; with USB devices
<dl><dd><pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow if random(0.1666)
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reject</pre></dl>

<h2>Bugs</h2>

If you find a bug in this software or if you'd like to request a feature to be implemented, please file a ticket at &lt;<a rel="nofollow" HREF="https://github.com/dkopecek/usbguard/issues/new">https://github.com/dkopecek/usbguard/issues/new</a>&gt;.

<h2>Copyright</h2>

Copyright © 2016 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8), <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5)

<h2>Authors</h2>

Daniel Kopeček &lt;dkopecek [at] redhat.com&gt;.
