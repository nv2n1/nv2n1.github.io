---
title: "fwbedit(1)"
name: "fwbedit"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fwbedit/"
description: "fwbedit – General purpose object tree editing tool"
---

<h2>NAME</h2>
<p> fwbedit &#8211; General purpose object tree editing tool</p>
<h2>SYNOPSIS</h2>
<p> <code>fwbedit</code> command [options] </p>
<h2>DESCRIPTION</h2>
<p> <code>fwbedit</code> is a general purpose object tree editing tool for Firewall Builder (see <a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1)). This tool can be used in the shell scripts written for batch-processing of the Firewall Builder data files. Fwbedit can perform the following operations on the objects and the tree: create new object, delete existing object, modify attributes of an object, add a reference to the given object to a group, remove reference to an object from a group, upgrade data file and check object tree in the file and repair it if necessary. Both object and a group can be defined by their ID or by their name and a full path in the tree (see section <code>EXAMPLES</code> below). </p>
<h2>COMMANDS AND OPTIONS:</h2>
<p> <code>new -f file.fwb -t objtype -n name -p parent [-c comment] [-a attrs]</code> </p>
<p> Creates new object. </p>
<p>&nbsp;<wbr>-f file.fwb: data file </p>
<p>&nbsp;<wbr>-t objtype: create new object of this type </p>
<p> -p parent: create new object as a child of this object. This parameter is mandatory. If you are adding an address to an interface, corresponding interface onkect must be specified as the parent. Similarly if you need to add an interface to a host or a firewall, corresponding host or firewall object is the parent. If you are adding an object to one of the standard folders, the parent is the library you want to add the object to or correct full path to the folder in the tree. </p>
<p>&nbsp;<wbr>-n name: the name of the new object </p>
<p>&nbsp;<wbr>-c txt:&nbsp;<wbr>&nbsp;<wbr>specify comment for the new object </p>
<p>&nbsp;<wbr>-a attribute1[,attribute2&#8230;]&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>&nbsp;<wbr>specify attributes that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>define parameters of the new object&nbsp;<wbr>(see below) </p>
<p> <code>delete -f file.fwb -o object</code> </p>
<p> Deletes object specified by its full path in the tree or object ID. </p>
<p>&nbsp;<wbr>-f file.fwb: data file </p>
<p>&nbsp;<wbr>-o object: object to be deleted, full path or ID </p>
<p> <code>modify -f file.fwb -o object -c comment [-a attrs]</code> </p>
<p> Modifies object specified by its full path in the tree or object ID. Object can not be renamed using this operation. </p>
<p>&nbsp;<wbr>-f file.fwb: data file </p>
<p>&nbsp;<wbr>-o object: object to be deleted, full path or ID </p>
<p>&nbsp;<wbr>-c txt:&nbsp;<wbr>&nbsp;<wbr>specify comment for the new object </p>
<p>&nbsp;<wbr>-a attribute1[,attribute2&#8230;]&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>&nbsp;<wbr>specify attributes that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>define parameters of the new object&nbsp;<wbr>(see below) </p>
<p> <code>list -f file.fwb -o object [-r|-c] [-d|-Fformat]</code> </p>
<p> Prints name and ID of an object. </p>
<p>&nbsp;<wbr>-f file.fwb: data file </p>
<p>&nbsp;<wbr>-o object: object to print, full path or ID </p>
<p> -r print specified object and all objects under it in the tree </p>
<p> -c print only children objects of the given object but do not<br />
&nbsp;<wbr>print the object itself. </p>
<p> -d print full dump of all object&#8217;s attributes including internal debugging information if available, this can be very verbose. </p>
<p> -Fformat_string Program recognizes macros in the format string and replaces them with values of corresponding object&#8217;s attributes. Macro is the name of the attribute surrounded with &#8216;%&#8217;, such as &#8216;%name%&#8217; or &#8216;%address%&#8217;. Here is the list of some attribute names: &quot;id&quot;, &quot;name&quot;, &quot;path&quot;, &quot;comment&quot;, &quot;type&quot;, &quot;address&quot;, &quot;netmask&quot;, &quot;dnsname&quot;. TCP and UDP service objects provide attributes &quot;src_range_start&quot;, &quot;src_range_end&quot;, &quot;dst_range_start&quot;, &quot;dst_range_end&quot; for the source and destination port ranges. ICMP and ICMP6 service objects have attributes &quot;icmp_type&quot; and &quot;icmp_code&quot;. </p>
<p> <code>add -f file.fwb -g group -o object</code> </p>
<p> Adds object specified by path or ID to a group, also specified by its path or ID. </p>
<p>&nbsp;<wbr>-f file.fwb: data file </p>
<p>&nbsp;<wbr>-g group: group the object should be added to,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>full path or ID </p>
<p>&nbsp;<wbr>-o object: object to be deleted, full path or ID </p>
<p> <code>remove -f file.fwb -g group -o object</code> </p>
<p> Removes object from a group. </p>
<p>&nbsp;<wbr>-f file.fwb: data file </p>
<p>&nbsp;<wbr>-g group: group the object should be removed from,<br />
&nbsp;<wbr>full path or ID </p>
<p>&nbsp;<wbr>-o object: object to be deleted, full path or ID </p>
<p> <code>upgrade -f file.fwb</code> </p>
<p> Upgrades data file to the latest data format version. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-f file.fwb: data file </p>
<p> <code>checktree -f file.fwb</code> </p>
<p> Checks consistency and correctness of the object tree in the given data file and repairs it if necessary.<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-f file.fwb: data file </p>
<h2>ATTRIBUTES FOR THE NEW OBJECTS, BY TYPE</h2>
<p> -t Firewall -a platform, host OS </p>
<p> -t IPv4 -a IP address [,netmask] </p>
<p> -t IPv6 -a IPv6 address [,masklen] </p>
<p> -t DNSName -a DNS record,run time </p>
<p> -t AddressRange -a start address, end address </p>
<p> -t ObjectGroup </p>
<p> -t Network -a address,netmask </p>
<p> -t NetworkIPv6 -a ipv6_address,netmask_length </p>
<p> -t Interval -a start time,start date,start day,end time, end date, end day </p>
<p> -t Interface -a security level,address type (dynamic or unnumbered),management </p>
<p> -t Host </p>
<p> -t TCPService -a source port range start,end,destination port range start,end,UAPRSF,UAPRSF </p>
<p> -t UDPService -a source port range start,end,Destination port range start,end </p>
<p> -t ICMPService -a ICMP type,ICMP code </p>
<p> -t IPService -a protocol number,lsrr/ssrr/rr/ts/fragm/short_fragm </p>
<h2>EXAMPLES</h2>
<p> Print contents of the object /User/Firewalls/firewall/eth0 according to the provided format. Note that object of the type &quot;Interface&quot; does not have attribute that would define its address, IP address is defined by its child object of the type IPv4 or IPv6. </p>
<p> fwbedit list -f x.fwb -o /User/Firewalls/firewall/eth0 -F &quot;type=%type% name=%name% id=%id% %comment%&quot; </p>
<p> Print contents of the object /User/Firewalls/firewall/eth0 and all its child objects. This is the way to see addresses and netmasks. Interface object does not have attribiute &quot;address&quot; so the program ignores macro &quot;%address%&quot; when it prints interface. </p>
<p> fwbedit list -f x.fwb -o /User/Firewalls/firewall/eth0 -F &quot;type=%type% name=%name% id=%id% %comment% %address%&quot; -r </p>
<p> Print group object /User/Objects/Addresses </p>
<p> fwbedit list -f x.fwb -o /User/Objects/Addresses -F &quot;type=%type% name=%name% id=%id% %comment%&quot; </p>
<p> Print group object /User/Objects/Addresses and all address objects inside of it: </p>
<p> fwbedit list -f x.fwb -o /User/Objects/Addresses -F &quot;type=%type% name=%name% id=%id% %comment%&quot; -r </p>
<p> Print address objects inside group /User/Objects/Addresses but do not print the group object itself: </p>
<p> fwbedit list -f x.fwb -o /User/Objects/Addresses -F &quot;type=%type% name=%name% id=%id% %comment%&quot; -c </p>
<p> Print addresses and netmasks of all interfaces of all firewalls in the form of their full object tree path, followed by the type, id, address and netmask: </p>
<p> fwbedit list -f x.fwb -o /User/Firewalls -F &quot;%path% %type% %id% %address% %netmask%&quot; -r | grep IP </p>
<p> Print names, platform and version information for all firewall objects defined in the data file: </p>
<p> fwbedit list -f x.fwb -o /User/Firewalls -F &quot;%name% platform: %platform% version: %version%&quot; -c </p>
<p> Print name, source and destination port ranges for all TCP services in the folder TCP of the user-defined group User: </p>
<p> fwbedit list -f x.fwb -o /User/Services/TCP -c -F &quot;name=&#8217;%name%&#8217; est=%established% %src_range_start%-%src_range_end% : %dst_range_start%-%dst_range_end%&quot; </p>
<p> Print icmp type and code for all ICMP services in the folder ICMP of the user-defined group User: </p>
<p> fwbedit list -f x.fwb -o /User/Services/ICMP -c -F &quot;name=&#8217;%name%&#8217; icmp_type=%icmp_type% icmp_code=%icmp_code%&quot; </p>
<p> Add IPv6 address to one of the interfaces of firewall object &quot;firewall&quot;: </p>
<p> fwbedit new -f x.fwb -p /User/Firewalls/firewall/eth3 -t IPv6 -n eth3-v6-addr -a 2001:470:1f05:590::2,64 </p>
<p> Add reference to the Host object &#8216;A&#8217; to the group &#8216;B&#8217;: </p>
<p> fwbedit add -f x.fwb -g /User/Objects/Groups/B -o /User/Objects/Hosts/A </p>
<p> Add reference to the object with ID id3D71A1BA to the group with ID id3D151943. If objects with given IDs do not exist, fwbedit prints an error message and does not make any changes in the data file. </p>
<p> fwbedit add -f x.fwb -o id3D71A1BA -g id3D151943 </p>
<p> Add reference to the object with ID id3D71A1BA to the group &#8216;testgroup&#8217;: </p>
<p> fwbedit add -f x.fwb -o id3D71A1BA -g /User/Objects/Groups/testgroup </p>
<p> The following script uses fwbedit &quot;list&quot; command to print IDs of all Address objects in the folder /User/Objects/Addresses , then cycles through the obtained list and uses fwbedit to add them to the group &quot;group1&quot;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>fwbedit list -f x.fwb -o&nbsp;<wbr>/User/Objects/Addresses -F&nbsp;<wbr>&quot;%id%&quot;&nbsp;<wbr>-c&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>\<br />
&nbsp;<wbr>while read id;&nbsp;<wbr>do&nbsp;<wbr>\<br />
fwbedit add -f x.fwb -g&nbsp;<wbr>/User/Objects/Groups/group1 -o&nbsp;<wbr>$id;&nbsp;<wbr>\<br />
&nbsp;<wbr>done </p>
<p> Here is slightly more complex example. The following script uses fwbedit &quot;list&quot; command to print types and IDs of all Address objects in the folder /User/Objects/Addresses , then filters them using grep to get only IPv6 objects and finally cycles through the obtained list and uses fwbedit to add them to the group &quot;group1&quot;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>fwbedit list -f x.fwb&nbsp;<wbr>&nbsp;<wbr>-o&nbsp;<wbr>/User/Objects/Addresses -F&nbsp;<wbr>&quot;%type%&nbsp;<wbr>%id%&quot;&nbsp;<wbr>-c |&nbsp;<wbr>\<br />
&nbsp;<wbr>grep IPv6 |&nbsp;<wbr>\<br />
&nbsp;<wbr>while read type id;&nbsp;<wbr>do&nbsp;<wbr>\<br />
fwbedit add -f x.fwb&nbsp;<wbr>&nbsp;<wbr>-g&nbsp;<wbr>/User/Objects/Groups/group1 -o&nbsp;<wbr>$id;&nbsp;<wbr>\<br />
&nbsp;<wbr>done </p>
<h2>URL</h2>
<p> Firewall Builder home page is located at the following URL: <code><a rel="nofollow" href="http://www.fwbuilder.org/">http://www.fwbuilder.org/</a></code> </p>
<h2>BUGS</h2>
<p> Please report bugs using bug tracking system on SourceForge: </p>
<p> <code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=5314">http://sourceforge.net/tracker/?group_id=5314</a>&amp;atid=105314</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1),</code> </p>
<h2>Index</h2>
