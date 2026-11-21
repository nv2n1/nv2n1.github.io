---

title: "btool(1)"
name: "btool"
section: "1"
letter: "b"
url: "/docs/linux/man/1-btool/"
description: "btool – Barry Project’s program to interface with BlackBerry handheld"
---

<p> <code>btool</code> &#8211; Barry Project&#8217;s program to interface with BlackBerry handheld </p>
<p> <code>btool</code> [-B busname][-N devname][-a db][-c dn][-C dnattr][-d db [-f file][-r#][-R#]-D#]][-h][-l][-L][-m cmd][-M][-p pin][-P password][-s db -f file][-S][-t][-v][-X][-z][-Z]</p>
<p> <code>btool</code> is a program that communicates with a BlackBerry device over USB; there is no intention to support ancient serial-port BlackBerries. Since the protocols used by BlackBerry are not documented by the manufacturer Research In Motion, this program is experimental and you <code>use at own risk</code>. Be sure your device is backed up by another program if it contains important data.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-B busname</code></dt>
<dd> Specify the USB bus to search for Blackberry devices on. This is the first number displayed in the output from the lsusb command, such as 002. If the busname is numeric on your system, 2 and 002 are equal. See also the -N option, which can be used together with this option to precisely select the device to work with.</dd>
<dt><code>-a db</code></dt>
<dd> Delete all records from specified database. This can be used multiple times to clear multiple databases.</dd>
<dt><code>-c dn</code></dt>
<dd> Convert address book database to LDIF format, using the specified dn as the baseDN. Sends LDIF output to stdout.</dd>
<dt><code>-C dnattr</code></dt>
<dd> Spcify LDIF attribute name to use when building the FQDN in the dn attribute. Defaults to &#8216;cn&#8217;. If you modify the mapping with the -m switch, make sure that the new dnattr exists.</dd>
<dt><code>-d db</code></dt>
<dd> Load database &#8216;db&#8217; FROM device and dump to stdout. Can be used multiple times to fetch more than one database. See the -t option for a list of device databases.</dd>
<dt><code>-e epp</code></dt>
<dd> Override endpoint pair detection. &#8216;epp&#8217; is a single string separated by a comma, holding the read,write endpoint pair. </dd>
<p> Example: -e 83,5 </p>
<p> Note: Endpoints are specified in hex. Use the same numbers given by the lsusb -v output. </p>
<p> You should never need to use this option, as endpoints are autodetected.</p>
<dt><code>-f file</code></dt>
<dd> Filename to write or read handheld data to/from. Used in conjunction with the -d and -s options, respectively. Note: the file format of this file is not backward compatible between devel releases.</dd>
<dt><code>-i charset</code></dt>
<dd> Specifies the iconv charset to use for converting international strings. The Blackberry uses the WINDOWS-1252 charset, which is incompatible with the more common code pages used in Linux. The most useful charset to use with this option is UTF-8, and is highly recommended. Any other charset available via &#8216;iconv &#8211;list&#8217; can be used here too, but may not be successful for some character conversions.</dd>
<dt><code>-l</code></dt>
<dd> Lists attached Blackberry devices, and their PIN numbers.</dd>
<dt><code>-L</code></dt>
<dd> List Contact field names. Each name represents a contact field that the Barry library recognizes. Use these names with the -m option to adjust the LDIF name to field mapping.</dd>
<dt><code>-m command</code></dt>
<dd> Map LDIF name to Contact field, or unmap LDIF name. To map a new or existing LDIF attribute name to a Barry contact field, use the format &#8216;ldif,read,write&#8217; where ldif represents the name of the attribute to map, read is the contact field name used to read data from the record, and write is the contact field name used to write data to the record. </dd>
<p> To unmap an LDIF name, specify the LDIF attribute alone. </p>
<p> For example, to map a new LDIF attribute called &quot;strange&quot; to read from FirstName and write to LastName, use: </p>
<p> -m strange,FirstName,LastName </p>
<p> The -m option can be specified multiple times to create the desired mapping.</p>
<dt><code>-M</code></dt>
<dd> List current LDIF mapping to stdout.</dd>
<dt><code>-N devname</code></dt>
<dd> Specify the USB device name. This is the second number displayed in the output from the lsusb command, such as 005. If the device name is numeric on your system, 5 and 005 are equal. See also the -B option.</dd>
<dt><code>-p pin</code></dt>
<dd> PIN of device to talk with. Only needed if you have more than one Blackberry connected at once.</dd>
<dt><code>-P password</code></dt>
<dd> Simplistic method to specify device password. In a real application, this would be done using a more secure prompt.</dd>
<dt><code>-s db</code></dt>
<dd> Save database &#8216;db&#8217; TO device from data loaded from -f file. See the -t option for a list of device databases.</dd>
<dt><code>-S</code></dt>
<dd> Show list of supported database parsers and builders. Parsers are used when reading data out of the device, and builders are used when writing data to the device. If a parser is supported, but its associated builder is not, that means you cannot change the database programmatically, such as with the -s option.</dd>
<dt><code>-t</code></dt>
<dd> Show device&#8217;s database table.</dd>
<dt><code>-T db</code></dt>
<dd> Show record state table for given database.</dd>
<dt><code>-v</code></dt>
<dd> Dump verbose protocol data during operation.</dd>
<dt><code>-X</code></dt>
<dd> Reset device.</dd>
<dt><code>-z</code></dt>
<dd> Use non-threaded sockets when communicating with the device. This is the behaviour seen in versions 0.12 and earlier, since threads were not yet supported. This option, along with -Z, are for debugging and testing.</dd>
<dt><code>-Z</code></dt>
<dd> Use a threaded socket router when communicating with the device. This is the default for btool. This option, along with -Z, are for debugging and testing.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options. </dd>
</dl>
<h2>DATABASE COMMAND MODIFIERS</h2>
<p> The following options modify the -d command option above, and can be used multiple times for more than one record.</p>
<dl>
<dt><code>-r #</code></dt>
<dd> Fetch specific record, given a record index number as seen in the -T state table. Can be used multiple times to fetch specific records from a single database.</dd>
<dt><code>-R #</code></dt>
<dd> Same as -r, but also clears the record&#8217;s dirty flags.</dd>
<dt><code>-D #</code></dt>
<dd> Delete the specified record using the index number as seen in the -T state table. </dd>
</dl>
<h2>AUTHOR</h2>
<p> <code>btool</code> is part of the Barry project. This manual page was written by Ian Darwin and Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a><br />
 Especially the caveats, and the call for developers and others to help with the project. </p>
