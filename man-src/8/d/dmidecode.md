---
title: "dmidecode(8)"
name: "dmidecode"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmidecode/"
description: "dmidecode – DMI table decoder"
---

<p>dmidecode &#8211; <font SIZE="-1">DMI</font> table decoder</p>
<h2>Synopsis</h2>
<p><code>dmidecode</code> [<code>OPTIONS</code>]</p>
<h2>Description</h2>
<p><code>dmidecode</code> is a tool for dumping a computer&#8217;s <font SIZE="-1">DMI</font> (some say <font SIZE="-1">SMBIOS</font>) table contents in a human-readable format. This table contains a description of the system&#8217;s hardware components, as well as other useful pieces of information such as serial numbers and <font SIZE="-1">BIOS</font> revision. Thanks to this table, you can retrieve this information without having to probe for the actual hardware. While this is a good point in terms of report speed and safeness, this also makes the presented information possibly unreliable. </p>
<p> The <font SIZE="-1">DMI</font> table doesn&#8217;t only describe what the system is currently made of, it also can report the possible evolutions (such as the fastest supported <font SIZE="-1">CPU</font> or the maximal amount of memory supported). </p>
<p> <font SIZE="-1">SMBIOS</font> stands for System Management <font SIZE="-1">BIOS</font>, while <font SIZE="-1">DMI</font> stands for Desktop Management Interface. Both standards are tightly related and developed by the <font SIZE="-1">DMTF</font> (Desktop Management Task Force). </p>
<p> As you run it, <code>dmidecode</code> will try to locate the <font SIZE="-1">DMI</font> table. It will first try to read the DMI table from sysfs, and next try reading directly from memory if sysfs access failed. If <code>dmidecode</code> succeeds in locating a valid DMI table, it will then parse this table and display a list of records like this one: </p>
<p> Handle 0x0002, DMI type 2, 8 bytes. Base Board Information<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Manufacturer: Intel<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Product Name: C440GX+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Version: 727281-001<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Serial Number: INCY92700942 </p>
<p> Each record has:</p>
<dl>
<dt>&bull;</p>
<dd>A handle. This is a unique identifier, which allows records to reference each other. For example, processor records usually reference cache memory records using their handles.</p>
<dt>&bull;</p>
<dd>A type. The <font SIZE="-1">SMBIOS</font> specification defines different types of elements a computer can be made of. In this example, the type is 2, which means that the record contains &quot;Base Board Information&quot;.</p>
<dt>&bull;</p>
<dd>A size. Each record has a 4-byte header (2 for the handle, 1 for the type, 1 for the size), the rest is used by the record data. This value doesn&#8217;t take text strings into account (these are placed at the end of the record), so the actual length of the record may be (and is often) greater than the displayed value.</p>
<dt>&bull;</p>
<dd>Decoded values. The information presented of course depends on the type of record. Here, we learn about the board&#8217;s manufacturer, model, version and serial number.</dl>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;dev-mem FILE</code></p>
<dd>Read memory from device <code>FILE</code> (default: <code>/dev/mem</code>)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Be less verbose. Unknown, inactive and <font SIZE="-1">OEM</font>-specific entries are not displayed. Meta-data and handle references are hidden.</p>
<dt><code>-s</code>, <code>&#8211;string KEYWORD</code></p>
<dd>Only display the value of the <font SIZE="-1">DMI</font> string identified by <code>KEYWORD</code>. <code>KEYWORD</code> must be a keyword from the following list: <code>bios-vendor</code>, <code>bios-version</code>, <code>bios-release-date</code>, <code>bios-revision</code>, <code>firmware-revision</code>, <code>system-manufacturer</code>, <code>system-product-name</code>, <code>system-version</code>, <code>system-serial-number</code>, <code>system-uuid</code>, <code>system-sku-number</code>, <code>system-family</code>, <code>baseboard-manufacturer</code>, <code>baseboard-product-name</code>, <code>baseboard-version</code>, <code>baseboard-serial-number</code>, <code>baseboard-asset-tag</code>, <code>chassis-manufacturer</code>, <code>chassis-type</code>, <code>chassis-version</code>, <code>chassis-serial-number</code>, <code>chassis-asset-tag</code>, <code>processor-family</code>, <code>processor-manufacturer</code>, <code>processor-version</code>, <code>processor-frequency</code>. Each keyword corresponds to a given <font SIZE="-1">DMI</font> type and a given offset within this entry type. Not all strings may be meaningful or even defined on all systems. Some keywords may return more than one result on some systems (e.g. <code>processor-version</code> on a multi-processor system). If <code>KEYWORD</code> is not provided or not valid, a list of all valid keywords is printed and <code>dmidecode</code> exits with an error. This option cannot be used more than once. </p>
<p> Note: on Linux, most of these strings can alternatively be read directly from <code>sysfs</code>, typically from files under <i>/sys/devices/virtual/dmi/id</i>. Most of these files are even readable by regular users.</p>
<dt><code>-t</code>, <code>&#8211;type TYPE</code></p>
<dd>Only display the entries of type <code>TYPE</code>. <code>TYPE</code> can be either a <font SIZE="-1">DMI</font> type number, or a comma-separated list of type numbers, or a keyword from the following list: <code>bios</code>, <code>system</code>, <code>baseboard</code>, <code>chassis</code>, <code>processor</code>, <code>memory</code>, <code>cache</code>, <code>connector</code>, <code>slot</code>. Refer to the DMI TYPES section below for details. If this option is used more than once, the set of displayed entries will be the union of all the given types. If <code>TYPE</code> is not provided or not valid, a list of all valid keywords is printed and <code>dmidecode</code> exits with an error.</p>
<dt><code>-H</code>, <code>&#8211;handle HANDLE</code></p>
<dd>Only display the entry whose handle matches <code>HANDLE</code>. <code>HANDLE</code> is a 16-bit integer.</p>
<dt><code>-u</code>, <code>&#8211;dump</code></p>
<dd>Do not decode the entries, dump their contents as hexadecimal instead. Note that this is still a text output, no binary data will be thrown upon you. The strings attached to each entry are displayed as both hexadecimal and <font SIZE="-1">ASCII</font>. This option is mainly useful for debugging.</p>
<dt> <code>&#8211;dump-bin FILE</code></p>
<dd>Do not decode the entries, instead dump the DMI data to a file in binary form. The generated file is suitable to pass to <code>&#8211;from-dump</code> later.</p>
<dt> <code>&#8211;from-dump FILE</code></p>
<dd>Read the DMI data from a binary file previously generated using <code>&#8211;dump-bin</code>.</p>
<dt> <code>&#8211;no-sysfs</code></p>
<dd>Do not attempt to read DMI data from sysfs files. This is mainly useful for debugging.</p>
<dt> <code>&#8211;oem-string N</code></p>
<dd>Only display the value of the <font SIZE="-1">OEM</font> string number <code>N</code>. The first <font SIZE="-1">OEM</font> string has number 1. With special value &quot;count&quot;, return the number of OEM strings instead.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage information and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display the version and exit</dl>
<p> Options &#8211;string, &#8211;type, &#8211;dump-bin and &#8211;oem-string determine the output format and are mutually exclusive. </p>
<p> Please note in case of <code>dmidecode</code> is run on a system with BIOS that boasts new SMBIOS specification, which is not supported by the tool yet, it will print out relevant message in addition to requested data on the very top of the output. Thus informs the output data is not reliable.</p>
<h2>Dmi Types</h2>
<p>The <font SIZE="-1">SMBIOS</font> specification defines the following <font SIZE="-1">DMI</font> types: </p>
<table>
<tr VALIGN=top>
<td ALIGN=right>Type</td>
<td>Information
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td>System
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td>Baseboard
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td>Chassis
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td>Processor
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5</td>
<td>Memory Controller
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6</td>
<td>Memory Module
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7</td>
<td>Cache
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8</td>
<td>Port Connector
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9</td>
<td>System Slots
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>10</td>
<td>On Board Devices
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>11</td>
<td>OEM Strings
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>12</td>
<td>System Configuration Options
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>13</td>
<td>BIOS Language
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>14</td>
<td>Group Associations
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>15</td>
<td>System Event Log
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>16</td>
<td>Physical Memory Array
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>17</td>
<td>Memory Device
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>18</td>
<td>32-bit Memory Error
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>19</td>
<td>Memory Array Mapped Address
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>20</td>
<td>Memory Device Mapped Address
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>21</td>
<td>Built-in Pointing Device
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>22</td>
<td>Portable Battery
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>23</td>
<td>System Reset
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>24</td>
<td>Hardware Security
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>25</td>
<td>System Power Controls
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>26</td>
<td>Voltage Probe
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>27</td>
<td>Cooling Device
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>28</td>
<td>Temperature Probe
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>29</td>
<td>Electrical Current Probe
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>30</td>
<td>Out-of-band Remote Access
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>31</td>
<td>Boot Integrity Services
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>32</td>
<td>System Boot
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>33</td>
<td>64-bit Memory Error
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>34</td>
<td>Management Device
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>35</td>
<td>Management Device Component
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>36</td>
<td>Management Device Threshold Data
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>37</td>
<td>Memory Channel
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>38</td>
<td>IPMI Device
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>39</td>
<td>Power Supply
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>40</td>
<td>Additional Information
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>41</td>
<td>Onboard Devices Extended Information
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>42</td>
<td>Management Controller Host Interface
</td>
</tr>
</table>
<p> Additionally, type 126 is used for disabled entries and type 127 is an end-of-table marker. Types 128 to 255 are for <font SIZE="-1">OEM</font>-specific data. <code>dmidecode</code> will display these entries by default, but it can only decode them when the vendors have contributed documentation or code for them. </p>
<p> Keywords can be used instead of type numbers with <code>&#8211;type</code>. Each keyword is equivalent to a list of type numbers: </p>
<table>
<tr VALIGN=top>
<td>Keyword</td>
<td>Types
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>system</td>
<td>1, 12, 15, 23, 32
</td>
</tr>
<tr VALIGN=top>
<td>baseboard</td>
<td>2, 10, 41
</td>
</tr>
<tr VALIGN=top>
<td>chassis</td>
<td>3
</td>
</tr>
<tr VALIGN=top>
<td>processor</td>
<td>4
</td>
</tr>
<tr VALIGN=top>
<td>memory</td>
<td>5, 6, 16, 17
</td>
</tr>
<tr VALIGN=top>
<td>cache</td>
<td>7
</td>
</tr>
<tr VALIGN=top>
<td>connector</td>
<td>8
</td>
</tr>
<tr VALIGN=top>
<td>slot</td>
<td>9
</td>
</tr>
</table>
<p> Keywords are matched case-insensitively. The following command lines are equivalent:</p>
<dl>
<dt>&bull;</p>
<dd>dmidecode &#8211;type 0 &#8211;type 13</p>
<dt>&bull;</p>
<dd>dmidecode &#8211;type 0,13</p>
<dt>&bull;</p>
<dd>dmidecode &#8211;type bios</p>
<dt>&bull;</p>
<dd>dmidecode &#8211;type BIOS</dl>
<h2>Binary Dump File Format</h2>
<p>The binary dump files generated by &#8211;dump-bin and read using &#8211;from-dump are formatted as follows:</p>
<dl>
<dt>&bull;</p>
<dd>The SMBIOS or DMI entry point is located at offset 0x00. It is crafted to hard-code the table address at offset 0x20.</p>
<dt>&bull;</p>
<dd>The DMI table is located at offset 0x20.</dl>
<h2>Uuid Format</h2>
<p>There is some ambiguity about how to interpret the UUID fields prior to SMBIOS specification version 2.6. There was no mention of byte swapping, and RFC 4122 says that no byte swapping should be applied by default. However, SMBIOS specification version 2.6 (and later) explicitly states that the first 3 fields of the UUID should be read as little-endian numbers (byte-swapped). Furthermore, it implies that the same was already true for older versions of the specification, even though it was not mentioned. In practice, many hardware vendors were not byte-swapping the UUID. So, in order to preserve compatibility, it was decided to interpret the UUID fields according to RFC 4122 (no byte swapping) when the SMBIOS version is older than 2.6, and to interpret the first 3 fields as little-endian (byte-swapped) when the SMBIOS version is 2.6 or later. The Linux kernel follows the same logic.</p>
<h2>Files</h2>
<p><i>/dev/mem</i><br />
 <i>/sys/firmware/dmi/tables/smbios_entry_point</i> (Linux only)<br />
 <i>/sys/firmware/dmi/tables/DMI</i> (Linux only)</p>
<h2>Bugs</h2>
<p>More often than not, information contained in the <font SIZE="-1">DMI</font> tables is inaccurate, incomplete or simply wrong.</p>
<h2>Authors</h2>
<p>Alan Cox, Jean Delvare</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-biosdecode/">biosdecode</a></code>(8), <code><a href="/docs/linux/man/4-mem/">mem</a></code>(4), <code><a href="/docs/linux/man/8-ownership/">ownership</a></code>(8), <code><a href="/docs/linux/man/8-vpddecode/">vpddecode</a></code>(8) </p>
