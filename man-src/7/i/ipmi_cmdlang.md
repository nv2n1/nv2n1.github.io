---
title: "ipmi_cmdlang(7)"
name: "ipmi_cmdlang"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ipmi_cmdlang/"
description: "ipmi_cmdlang – A command language interface to the IPMI library"
---

<p>ipmi_cmdlang &#8211; A command language interface to the IPMI library</p>
<h2>Description</h2>
<p><code>ipmi_cmdlang</code> is a command language designed to supply the full power of OpenIPMI on a command line. It has a large number of commands and well-formed responses to each command. Note that this assumes some knowledge of OpenIPMI and how it works; you can get that from the IPMI document that comes with OpenIPMI. <code>ipmish</code> starts up with no connections or anything of that nature. You must enter commands to make connections to domains. Then you can enter commands to manipulate those domains or objects inside those domains. Note that you may use quotes, either <code>&#8221;</code> or to contain parameters with spaces. </p>
<h2>Comments</h2>
<p>Lines with a <code>#</code> character in the first column are ignored.</p>
<h2>Objects</h2>
<p>In the command language, you will deal with various objects like sensors, controls, domains, and entities. Each of these has a name. The name of the domain is assigned by the user in the <code>domain new</code> command, all the other names are based on the domain name of the domain they belong to and various attributes about the object. These names are all well-formed. They are </p>
<p> <i>&lt;domain&gt;</i> &#8211; A name of a domain. Each registered domain in a system has a name assigned by the user. </p>
<p> <i>&lt;entity&gt;</i> &#8211; Entity names are in the form:</p>
<dl>
<dd>[<i>&lt;domain&gt;</i>[(<i>&lt;entity spec&gt;</i>)]]</dl>
<p> Notice that the <i>&lt;entity spec&gt;</i> is optional. If it is not listed, then the operation is done on all entities in the domain. The whole thing is optional, too, if nothing is given then the operation is done on every entity in every domain. </p>
<p> The <i>&lt;entity spec&gt;</i> is either</p>
<dl>
<dd><i>&lt;entity id&gt;</i>.<i>&lt;entity instance&gt;</i></dl>
<p> for system-relative entities, or:</p>
<dl>
<dd>r<i>&lt;channel&gt;</i>.<i>&lt;IPMB&gt;</i>.<i>&lt;entity id&gt;</i>.<i>&lt;entity instance-0x60&gt;</i></dl>
<p> for device-relative entities. In IPMI, device-relative entity instances always start at 0x60; the specification suggests that you subtract off the 0x60 from the entity instance when displaying these; the command language follows this suggestion. </p>
<p> <i>&lt;sensor&gt;</i> &#8211; These come in the form</p>
<dl>
<dd>[<i>&lt;entity&gt;</i>[.<i>name</i>]]</dl>
<p> As with entities, only listing a domain will cause the operation to be done on every sensor in the domain, just listing an entity will cause it to be done to every sensor in that entity. An empty sensor entry will cause an operation to be done on every sensor in every domain. </p>
<p> <i>&lt;control&gt;</i> &#8211; These come in the form</p>
<dl>
<dd>[&lt;entity&gt;[.name]]</dl>
<p> These work exactly like sensors. </p>
<p> <i>&lt;mc&gt;</i> &#8211; A management controller. These come in the form</p>
<dl>
<dd>[&lt;domain&gt;[(&lt;channel&gt;.&lt;IPMB&gt;)]]</dl>
<p> As usual, the parts left empty will cause defaulting to all things in the previously specified parts. </p>
<p> <i>&lt;connection&gt;</i> &#8211; A connection number, in the form</p>
<dl>
<dd>[&lt;domain&gt;[.&lt;integer&gt;]]</dl>
<p> The number is the connection number of the domain. </p>
<p> <i>&lt;pet&gt;</i> &#8211; A platform event trap id, in the form</p>
<dl>
<dd>[&lt;domain&gt;[.&lt;integer&gt;]]</dl>
<p> The number is arbitrarily assigned by the system. </p>
<p> <i>&lt;lanparm&gt;</i> &#8211; A LAN parameter id, in the form</p>
<dl>
<dd>[&lt;domain&gt;[.&lt;integer&gt;]]</dl>
<p> The number is arbitrarily assigned by the system. </p>
<p> <i>&lt;pef&gt;</i> &#8211; A PEF id, in the form</p>
<dl>
<dd>[&lt;domain&gt;[.&lt;integer&gt;]]</dl>
<p> The number is arbitrarily assigned by the system. </p>
<p> <i>&lt;fru&gt;</i> &#8211; A FRU id, in the form</p>
<dl>
<dd>[&lt;domain&gt;[.&lt;integer&gt;]]</dl>
<p> The number is arbitrarily assigned by the system. </p>
<p> In all cases, the object names have parts that are optional, and the entire object name is optional. If a part is left empty, then all objects that are part of the specified parts are operated on. For instance, if the system has a sensor named <code>d1(7.1).temp</code> then specifying <code>d1</code> would operation on all sensors in the domain named <code>d1.</code> Specifying <code>d1(7.1)</code> Would operation on all sensors in that entity. Specifying an empty name, either with or by just entering nothing if the object is the last thing in the command&#8217;s parameters. </p>
<p> Note this optionality gives a lot of power, but can be very dangerous. Entering <code>domain close</code> will close every domain, for instance. </p>
<p> In commands, every object operated on will generate a response for that object. If no object is operated on, the command will produce an error.</p>
<h2>Other Parameters</h2>
<p>The commands and displays use a variety of other parameters for specifying various IPMI things. </p>
<p> <i>&lt;guid&gt;</i> &#8211; a 16-byte globally unique ID, all globbed together in one big hexadecimal thing. </p>
<p> <i>&lt;threshold&gt;</i> is a threshold for a sensor; the value it must go over/under to generate an event. It is always displayed as one of <code>lower non-critical</code> <code>lower critical</code> <code>lower non-recoverable</code> <code>upper non-critical</code> <code>upper critical</code> <code>upper non-recoverable.</code> It may be entered as one of the above, or as <code>ln,</code> <code>lc,</code> <code>lr,</code> <code>un,</code> <code>uc,</code> <code>ur</code> as a short form. </p>
<p> <i>&lt;threshold enable&gt;</i> is the enable for a threshold. It is like <i>&lt;threshold&gt;</i> above, but also has a <code>going-high</code> or <code>going-low</code> and an <code>assertion</code> or <code>deassertion</code> appended to the end of the name. The short form will have a <code>l</code> or <code>h</code> for going-low and going high and then a <code>a</code> or <code>d</code> appended for assertion and deassertion So for instance, <code>urld</code> is upper non-recoverable going-low deassertion. </p>
<p> <i>&lt;discrete enable&gt;</i> is the enable or disable for a discrete sensor and is specified with the sensor offset. The long form is <code>&lt;integer&gt; assertion</code> or <code>&lt;integer&gt; deassertion</code> and the short form is <code>&lt;integer&gt;[ad]</code> where the number is the offset and <code>[ad]</code> means assertion or deassertion. </p>
<p> <i>&lt;hot-swap state&gt;</i> is one of <code>not_present,</code> <code>inactive</code> <code>activation_requested</code> <code>activation_in_progress</code> <code>active</code> <code>deactivation_requested</code> <code>deactivation_in_progress</code> or <code>out_of_con.</code> </p>
<p> <i>&lt;color&gt;</i> is one of <code>black,</code> <code>white,</code> <code>red,</code> <code>green</code> <code>blue</code> <code>yellow</code> or <code>orange.</code> </p>
<p> <i>&lt;bool&gt;</i> is one of <code>true,</code> <code>on,</code> <code>t,</code> or <code>1</code> for true and one of <code>false,</code> <code>off,</code> <code>f,</code> or <code>0</code> for false. Output is always <code>true</code> or <code>false.</code></p>
<h2>Commands</h2>
<p>The command language is hierarchical, meaning that commands may have subcommands, and subcommands may have subsubcommands, etc. So, for instance, the command to create a domain is <code>domain new.</code> The command to list all sensors in a domain named domain1 is <code>sensor list domain1.</code> </p>
<p> Each command has a response for each object operated on, which is listed after the command description. In those responses, anything that begins with a <code>%</code> is optional. Entries of the form <code>**name**</code> refer to object info descriptions that are listed in the object info section. If an entry has two &#8216;.&#8217; indented one space below it, then that entry may occur zero or more times. </p>
<p> Each section below defines the unique subcommands of a main command. </p>
<p> Help for any command is available with: </p>
<p> <code>help command [subcommand [&#8230;]]</code> &#8211; Help for any command. </p>
<p> Some commands are common to almost all subcommands. These are: </p>
<p> <code>list &lt;containing object&gt;</code> &#8211; List all objects of the specified type that are contained in the specified object. For instance, <code>control list </code><i>&lt;entity&gt;</i> will list all controls in the given entity.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>&lt;containing object type&gt;
 Name: &lt;name&gt;
 .
 .</pre>
</dl>
<p> <code>info &lt;object&gt;</code> &#8211; List static information about the given object.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>&lt;object type&gt;
 Name: &lt;name&gt;
 **object info**</pre>
</dl>
</dl>
<h3>domain</h3>
<p>These commands deal with domain objects. </p>
<p> <code>new </code><i>&lt;domain&gt;</i> <i>&lt;options&gt;</i> <i>&lt;parms&gt;</i> [<i>&lt;parms&gt;</i>] &#8211; Open a connection to a new domain. <i>&lt;parms&gt;</i> are either:</p>
<dl>
<dd>lan <i>&lt;IP&gt;</i> <i>&lt;port&gt;</i> [<i>&lt;IP&gt;</i> <i>&lt;port&gt;</i>] <i>&lt;enc&gt;</i> <i>&lt;auth&gt;</i> <i>&lt;name&gt;</i> <i>&lt;password&gt;</i></dl>
<p> for a RMCP LAN connection or</p>
<dl>
<dd>smi <i>&lt;smi num&gt;</i></dl>
<p> for a system interface connection. Note that <i>&lt;parms&gt;</i> is listed twice (second one is optional); if the system support it you can make two connections to two independent management controllers in the system. Note that this is not for multiple IP addresses to the same BMC. For that, notice that the LAN connection has an options extra IP and port for the second IP address. OpenIPMI supports these IP addresses and connection, detecting failures, switching between addresses, and other fault-tolerant things. It does this transparently to the user. Multiple connections may require special OEM support, read the documentation about your specific system if you need this. </p>
<p> The <i>&lt;IP&gt;</i> is the IP address or host name of the LAN-capable BMC to connect with. The <i>&lt;port&gt;</i> is generally 623. <i>&lt;enc&gt;</i> is the authentication type, either <code>md5,</code> <code>md2,</code> <code>straight,</code> or <code>none.</code> <i>&lt;auth&gt;</i> is the authentication level, either <code>admin,</code> <code>operator</code> or <code>user.</code> <i>&lt;name&gt;</i> and <i>&lt;password&gt;</i> are the user name and password of the IPMI user to use for the connection. The &lt;smi num&gt; is the driver number, generally 0. Options enable and disable various automatic processing and are:</p>
<dl>
<dt> <code>-[no]all</code> &#8211; all automatic handling. This will override the other</p>
<dd>processing options and turn them all on. This is true by default.</p>
<dt> <code>-[no]sdrs</code> &#8211; sdr fetching. This turns on fetching SDRs when they are found. This</p>
<dd>is false by default.</p>
<dt> <code>-[no]frus</code> &#8211; FRU fetching This turns on fetching FRU information when it is found. This</p>
<dd>is false by default.</p>
<dt> <code>-[no]sel</code> &#8211; SEL fetching. This turns on fetching SELs when they are found. This</p>
<dd>is false by default.</p>
<dt> <code>-[no]ipmbscan</code> &#8211; IPMB bus scanning. This turns on scanning IPMB buses when they are found.</p>
<dd>This is false by default.</p>
<dt> <code>-[no]oeminit</code> &#8211; enable or disable special OEM processing (like ATCA).</p>
<dt> <code>-[no]seteventrcvr</code> &#8211; setting event receivers. Note that setting event</p>
<dd>receivers and waiting til up is not affected by the <code>-all</code> option. If this is true (the default) then OpenIPMI will attempt to set the event receiver for an MC it finds that does not have it set to a valid destination.</p>
<dt> <code>-wait_til_up</code> &#8211; wait until the domain is up before returning</p>
<dd>Note that if you specify this and the domain never comes up, you will never get a prompt. This is not affected by the <code>-all</code> option. By default -all and -seteventrcvr are true, which turns everything on.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain Created: &lt;domain&gt;</pre>
</dl>
<p> <code>open </code><i>&lt;domain&gt;</i> <i>&lt;options&gt;</i> <i>&lt;parms&gt;</i> [<i>&lt;parms&gt;</i>] &#8211; Open a connection to a new domain. <i>&lt;parms&gt;</i> are either:</p>
<dl>
<dd>lan [-U <i>&lt;username&gt;</i>] [-P <i>&lt;password&gt;</i>] [-A <i>&lt;authtype&gt;</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[-L&nbsp;<wbr><i>&lt;privilege&gt;</i>]&nbsp;<wbr>[-s]&nbsp;<wbr>[-p[2]&nbsp;<wbr><i>&lt;port number&gt;</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[-Ra&nbsp;<wbr><i>&lt;auth alg&gt;</i>]&nbsp;<wbr>[-Ri&nbsp;<wbr><i>&lt;integ alg&gt;</i>]&nbsp;<wbr>[-Rc&nbsp;<wbr><i>&lt;conf algo&gt;</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[-Rl]&nbsp;<wbr>[-Rk&nbsp;<wbr><i>&lt;bmc key&gt;</i>]&nbsp;<wbr>[-H&nbsp;<wbr><i>&lt;hackname&gt;</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[-M&nbsp;<wbr><i>&lt;max oustanding msgs</i>&gt;]&nbsp;<wbr><i>&lt;IP&gt;</i>&nbsp;<wbr>[<i>&lt;IP&gt;</i>]</dl>
<p> for a RMCP/RMCP+ LAN connection or</p>
<dl>
<dd>smi <i>&lt;smi num&gt;</i></dl>
<p> for a system interface connection. Note that <i>&lt;parms&gt;</i> is listed twice (second one is optional); if the system support it you can make two connections to two independent management controllers in the system. Note that this is not for multiple IP addresses to the same BMC. For that, use the -s option and the second IP (and -p2) for the second IP address. OpenIPMI supports these IP addresses and connections, detecting failures, switching between addresses, and other fault-tolerant things. It does this transparently to the user. Multiple connections may require special OEM support, read the documentation about your specific system if you need this. </p>
<p> The <i>&lt;IP&gt;</i> is the IP address or host name of the LAN-capable BMC to connect with. The <i>&lt;port&gt;</i> defaults 623. <i>&lt;authtype&gt;</i> is the authentication type, either <code>rmcp+,</code> <code>md5,</code> <code>md2,</code> <code>straight,</code> or <code>none.</code> It defaults to the best authentication supported by the server. <i>&lt;auth&gt;</i> is the authentication level, either <code>admin,</code> <code>operator</code> or <code>user.</code> It defaults to admin. <i>&lt;username&gt;</i> and <i>&lt;password&gt;</i> are the user name and password of the IPMI user to use for the connection. For RMCP+ connections, the authentication algorithms supported (-Ra) are: bmcpick, rakp_none, rakp_hmac_sha1, and rakp_hmac_md5. The integrity algorithms (-Ri) supported are: bmcpick, none, hmac_sha1, hmac_md5, and md5. The confidentiality algorithms (-Rc) are: bmcpick, aes_cbc_128, xrc4_128, and xrc_40. The defaults are rackp_hmac_sha1, hmac_sha1, and aes_cb_128. -Rl turns on lookup up names by the name and the privilege level (allowing the same name with different privileges and different passwords), the default is straight name lookup. -Rk sets the BMC key, needed if the system does two-key lookups. </p>
<p> For SMI types, the &lt;smi num&gt; is the driver number, generally 0. </p>
<p> The <i>&lt;hackname&gt;</i> enables certain hacks for broken platforms. This may be listed multiple times to enable multiple hacks. The currently available hacks are:</p>
<dt> <code>intelplus</code> &#8211; For Intel platforms that have broken RMCP+.</p>
<dt> <code>rakp3_wrong_rolem</code> &#8211; For systems that truncate role(m) in the RAKP3 msg.</p>
<dt> <code>rmcpp_integ_sik</code> &#8211; For systems that use SIK instead of <a href="/docs/linux/man/1-k/">K</a>(1) for integrity. </p>
<dd>The -M option sets the maximum outstanding messages. The default is 2, ranges 1-63. </p>
<p> Options enable and disable various automatic processing and are:</p>
<dt> <code>-[no]all</code> &#8211; all automatic handling. This will override the other</p>
<dd>processing options and turn them all on. This is true by default.</p>
<dt> <code>-[no]sdrs</code> &#8211; sdr fetching. This turns on fetching SDRs when they are found. This</p>
<dd>is false by default.</p>
<dt> <code>-[no]frus</code> &#8211; FRU fetching This turns on fetching FRU information when it is found. This</p>
<dd>is false by default.</p>
<dt> <code>-[no]sel</code> &#8211; SEL fetching. This turns on fetching SELs when they are found. This</p>
<dd>is false by default.</p>
<dt> <code>-[no]ipmbscan</code> &#8211; IPMB bus scanning. This turns on scanning IPMB busses when they are found.</p>
<dd>This is false by default.</p>
<dt> <code>-[no]oeminit</code> &#8211; enable or disable special OEM processing (like ATCA).</p>
<dt> <code>-[no]seteventrcvr</code> &#8211; setting event receivers. Note that setting event</p>
<dd>receivers is not affected by the <code>-all</code> option. If this is true (the default) then OpenIPMI will attempt to set the event receiver for an MC it finds that does not have it set to a valid destination. <code>-[no]setseltime</code> &#8211; set SEL time. Note that setting the SEL time is not affected by the <code>-all</code> option. If this is true (the default) then OpenIPMI will attempt to set the time in the SELs it finds. It will set it to the current system time.</p>
<dt> <code>-wait_til_up</code> &#8211; wait until the domain is up before returning</p>
<dd>Note that if you specify this and the domain never comes up, you will never get a prompt. This is not affected by the <code>-all</code> option. By default -all and -seteventrcvr are true, which turns everything on.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain Created: &lt;domain&gt;</pre>
</dl>
<p> <code>fru &lt;domain&gt; &lt;is_logical&gt; &lt;device_address&gt; &lt;device_id&gt; &lt;lun&gt; &lt;private_bus&gt; &lt;channel&gt;</code> &#8211; dump a fru given all it&#8217;s sundry information.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain
 Name: &lt;domain&gt;
 FRU
 **FRU INFO**</pre>
</dl>
<p> <code>msg &lt;domain&gt; &lt;channel&gt; &lt;ipmb&gt; &lt;LUN&gt; &lt;NetFN&gt; &lt;Cmd&gt; [data&#8230;]</code> &#8211; Send a command to the given IPMB address on the given channel and display the response. Note that this does not require the existence of an MC in OpenIPMI.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre> Domain: &lt;domain&gt;
 channel: &lt;chan&gt;
 ipmb: &lt;ipmb&gt;
 LUN: &lt;lun&gt;
 NetFN: &lt;netfn&gt;
 command: &lt;cmd&gt;
 Data: &lt;data bytes&gt;</pre>
</dl>
<p> <code>scan &lt;domain&gt; &lt;ipmb addr&gt; [ipmb addr]</code> &#8211; scan an IPMB to add or remove it. If a range is given, then scan all IPMBs in the range.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Scan done: &lt;domain&gt;</pre>
</dl>
<p> <code>rescan_sels &lt;domain&gt; </code> &#8211; Rescan all the SELs in the domain.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>SEL Rescan done: &lt;domain&gt;</pre>
</dl>
<p> <code>presence &lt;domain&gt;</code> &#8211; Audit the presence of all entities in the domain. Note that this just starts the process; it will run in the background.</p>
<dt>Response is:</p>
<dd>
<dl>
<dd>
<pre>Presence check started: &lt;domain&gt;</pre>
</dl>
<p> <code>close &lt;domain&gt;</code> &#8211; close the given domain.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain closed: &lt;domain&gt;</pre>
</dl>
<p> <code>sel_rescan_time &lt;domain&gt; &lt;time in seconds&gt;</code> &#8211; Set the time between SEL rescans for all. It affects all current SELs and SELs that are discovered in the future. Zero disables scans.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain SEL rescan time set: &lt;domain&gt;</pre>
</dl>
<p> <code>ipmb_rescan_time &lt;domain&gt; &lt;time in seconds&gt;</code> &#8211; Set the time between IPMB rescans for this domain. zero disables scans.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain IPMB rescan time set: &lt;domain&gt;</pre>
</dl>
</dl>
<h3>fru</h3>
<p>These commands deal with FRU objects. Note that FRU objects are allocated by the domain fru command, and are not allocated here. </p>
<p> <code>list</code> &#8211; List all the frus in the system</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain
 Name: &lt;domain&gt;
 FRUs
 Name: &lt;fru&gt;
 .
 .
 .
 .</pre>
</dl>
<p> <code>info &lt;fru&gt;</code> &#8211; Dump information about a FRU</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>**FRU INFO**</pre>
</dl>
<p> <code>areainfo &lt;fru&gt;</code> &#8211; Dump the info about the FRU&#8217;s areas</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU
 Name: &lt;fru&gt;
 FRU Length: &lt;integer&gt;
 Area
 Name: &lt;area name&gt;
 Number: &lt;integer&gt;
 Offset: &lt;integer&gt;
 Length: &lt;integer&gt;
 Used Length: &lt;Integer&gt;
 .
 .</pre>
</dl>
<p> <code>write &lt;fru&gt;</code> &#8211; Write the local FRU data out into the FRU</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU written: &lt;fru&gt;</pre>
</dl>
<p> <code>close &lt;fru&gt;</code> &#8211; Delete the FRU</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU deleted: &lt;fru&gt;</pre>
</dl>
<p> <code>setval &lt;fru&gt; &lt;name&gt; [num] value</code> &#8211; Set the value of a FRU element. The name is the record name, or multi-record. The number is required for fields that need it (custom and multi-record). The value is a single value for integers. For strings it is a string type (either binary, ascii, or unicode) and the info. Binary and unicode data is specified as numbers. ascii data is specified in a string. Note that setting a ascii value with no string will clear the value. Zero length strings and data is valid.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU value set: &lt;fru&gt;</pre>
</dl>
<p> <code>area_offset &lt;fru&gt; &lt;area name&gt; &lt;offset&gt;</code> &#8211; Set the offset of the given area to the given value. Area names are internal_data, chassis_info, board_info, product_info, and multi_record.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU area offset set: &lt;fru&gt;</pre>
</dl>
<p> area_length &lt;fru&gt; &lt;area name&gt; &lt;length&gt; &#8211; Set the length of the given area to the given value. Area names are internal_data, chassis_info board_info, product_info, and multi_record</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU area length set: &lt;fru&gt;</pre>
</dl>
<p> area_add &lt;fru&gt; &lt;area name&gt; &lt;offset&gt; &lt;length&gt; &#8211; Add the given area to the FRU.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU area added: &lt;fru&gt;</pre>
</dl>
<p> area_delete &lt;fru&gt; &lt;area name&gt; &#8211; Delete the given area from the FRU</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>FRU area deleted: &lt;fru&gt;</pre>
</dl>
</dl>
<h3>entity</h3>
<p>These commands deal with entity objects. </p>
<p> <code>list &lt;entity&gt;</code> &#8211; List all the entities that meed the criteria</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain
 Name: &lt;domain&gt;
 Entities
 Name: &lt;entity&gt;
 .
 .
 .
 .</pre>
</dl>
<p> <code>info &lt;entity&gt;</code> &#8211; Dump information about an entity.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Entity
 Name: &lt;entity&gt;
 **ENTITY INFO**
 .
 .</pre>
</dl>
<p> <code>fru &lt;entity&gt;</code> &#8211; Dump the FRU information about the given entity.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Entity
 Name: &lt;entity&gt;
 FRU
 **FRU INFO**</pre>
</dl>
</dl>
<h3>entity hs</h3>
<p>These commands deal with hot-swap of entities. Note that there is no info or list command for this subcommand. </p>
<p> <code>get_act_time &lt;entity&gt;</code> &#8211; Get the hot-swap auto-activate time.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Entity
 Name: &lt;entity&gt;
 Auto-Activation Time: &lt;integer&gt;</pre>
</dl>
<p> <code>set_act_time &lt;entity&gt;</code> &#8211; Set the hot-swap auto-activate time.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Set act time: &lt;entity&gt;</pre>
</dl>
<p> <code>get_deact_time &lt;entity&gt;</code> &#8211; Get the hot-swap auto-deactivate time Response:</p>
<dl>
<dd>
<pre>Entity
 Name: &lt;entity&gt;
 Auto-Deactivation Time: &lt;integer&gt;</pre>
</dl>
<p> <code>set_deact_time &lt;entity&gt;</code> &#8211; Set the hot-swap auto-deactivate time</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Set deact time: &lt;entity&gt;</pre>
</dl>
<p> <code>activation_request &lt;entity&gt;</code> &#8211; Act like a user requested an activation of the entity. This is generally equivalent to closing the handle latch or something like that.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Activation requested: &lt;entity&gt;</pre>
</dl>
<p> <code>activate &lt;entity&gt;</code> &#8211; activate the given entity</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Activated: &lt;entity&gt;</pre>
</dl>
<p> <code>deactivate &lt;entity&gt;</code> &#8211; deactivate the given entity</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Deactivated: &lt;entity&gt;</pre>
</dl>
<p> <code>state &lt;entity&gt;</code> &#8211; Return the current hot-swap state of the given entity.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Entity
 Name: &lt;entity&gt;
 State: &lt;hot-swap state&gt;</pre>
</dl>
<p> <code>check &lt;entity&gt;</code> &#8211; Audit the entity&#8217;s hot-swap state</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Check started: &lt;entity&gt;</pre>
</dl>
</dl>
<h3>sensor</h3>
<p><code>get &lt;sensor&gt;</code> &#8211; Get the sensor&#8217;s current reading.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Sensor
 Name: &lt;sensor&gt;
 Event Messages Enabled: &lt;bool&gt;
 Sensor Scanning Enabled: &lt;bool&gt;
 Initial Update In Progress: &lt;bool&gt;</pre>
</dl>
<p> For threshold sensors, the following will be output:</p>
<dl>
<dd>
<pre>%Value: &lt;double&gt;
%Raw Value: &lt;integer&gt;
Threshold
 Name: &lt;threshold&gt;
 Out Of Range: &lt;bool&gt;</pre>
</dl>
<p> For discrete sensors, the following will be output:</p>
<dl>
<dd>
<pre>Event
 Offset: &lt;integer&gt;
 %Name: &lt;string name of event offset&gt;
 Set: &lt;bool&gt;</pre>
</dl>
<p> The name field may be custom and is not explicitly specified. </p>
<p> <code>rearm &lt;sensor&gt; global | &lt;threshold enable&gt; [&lt;threshold enable&gt; ..] | &lt;discrete enable&gt; [&lt;discrete enable&gt; ..]</code> &#8211; Rearm the sensor. If global is specified, then rearm all events in the sensor. Otherwise, if it is a threshold sensor, then put in a list of threshold enables. If it is a discrete sensor, then put in a list of discrete enables.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Rearm done: &lt;sensor&gt;</pre>
</dl>
<p> <code>get_thresholds &lt;sensor&gt;</code> &#8211; Get the sensor&#8217;s thresholds</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Sensor
 Name: &lt;sensor&gt;
 Threshold 
 Name: &lt;threshold&gt;
 Value: &lt;double&gt;</pre>
</dl>
<p> <code>set_thresholds &lt;sensor&gt; &lt;threshold&gt; &lt;value&gt; &#8230;</code> &#8211; Set the sensor&#8217;s thresholds to the given values. If a threshold is not specified, it will not be modified. Thresholds are un, uc, ur, lr, lc, ln. The u stands for upper, l for lower, n for non-critical, c for critical, and r for non-recoverable. The value is floating point.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Thresholds set: &lt;sensor&gt;</pre>
</dl>
<p> <code>get_hysteresis &lt;sensor&gt;</code> &#8211; Get the sensor&#8217;s hysteresis values</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Sensor
 Name: &lt;sensor&gt;
 Positive Hysteresis: &lt;integer&gt;
 Negative Hysteresis: &lt;integer&gt;</pre>
</dl>
<p> <code>set_hysteresis &lt;sensor&gt; &lt;pos hyst&gt; &lt;neg hyst&gt;</code> &#8211; Set the sensor&#8217;s hysteresis to the given values. These are raw integer value; hystersis is specified as a raw value and it cannot be converted to floating point because the function may be non-linear.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Hysteresis set: &lt;sensor&gt;</pre>
</dl>
<p> <code>get_event_enables &lt;sensor&gt;</code> &#8211; Get the sensor&#8217;s event enable values</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Sensor
 Name: &lt;sensor&gt;
 Event Messages Enabled: &lt;bool&gt;
 Sensor Scanning Enabled: &lt;bool&gt;
 Busy: &lt;bool&gt;</pre>
</dl>
<p> Threshold sensors report:</p>
<dl>
<dd>
<pre>Threshold
 Name: &lt;threshold&gt;
 Enabled: &lt;bool&gt;
 .
 .</pre>
</dl>
<p> only supported thresholds are listed. Discrete sensors report:</p>
<dl>
<dd>
<pre>Event
 Offset: &lt;integer&gt;
 Name: &lt;event offset name for sensor&gt;
 %Assertion Enabled: &lt;bool&gt;
 %Deassertion Enabled: &lt;bool&gt;</pre>
</dl>
<p> only supported offsets are listed. The assertion and deassertion enables are listed only if the offset support them. </p>
<p> <code>set_event_enables &lt;sensor&gt; msg|nomsg scan|noscan [&lt;enable&gt; [&lt;enable&gt; &#8230;]]</code> &#8211; Set the sensor&#8217;s event enable values. This turns sensor messages and scanning on and off and will enable all the listed enables and disable all over ones. The enables are either a <i>&lt;threshold enable&gt;</i> or a <i>&lt;discrete enable&gt;</i>.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Event enables set: &lt;sensor&gt;</pre>
</dl>
<p> <code>enable_events &lt;sensor&gt; msg|nomsg scan|noscan [&lt;enable&gt; [&lt;enable&gt; &#8230;]]</code> &#8211; Enable event enable values. This turns sensor messages and scanning on and off and will enable all the listed enables. All other enables will be left alone. The enables are either a <i>&lt;threshold enable&gt;</i> or a <i>&lt;discrete enable&gt;</i>.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Event enables set: &lt;sensor&gt;</pre>
</dl>
<p> <code>disable_events &lt;sensor&gt; msg|nomsg scan|noscan [&lt;enable&gt; [&lt;enable&gt; &#8230;]]</code> &#8211; Disable event enable values. This turns sensor messages and scanning on and off and will disable all the listed enable. All other enables will be left alone. The enables are either a <i>&lt;threshold enable&gt;</i> or a <i>&lt;discrete enable&gt;</i>.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Event enables set: &lt;sensor&gt;</pre>
</dl>
</dl>
<h3>control</h3>
<p>Commands dealing with controls. </p>
<p> <code>set &lt;control&gt; &lt;value&gt; [&lt;value&gt; ..]</code> &#8211; Set the value of a control. The settings depend on control type, most take one or more integer values depending on the number of physical things the control contains. An identifier type takes one or more unsigned characters. A light set with settings take the form</p>
<dl>
<dd><code>lc|nolc &lt;color&gt; &lt;on time&gt; &lt;off time&gt;</code></dl>
<p> <code>lc</code> and <code>nolc</code> turn on or of local control, the over values should be obvious. Note all lights support local control, you need to see if it supports the value.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Set done: &lt;control&gt;</pre>
</dl>
<p> <code>get &lt;control&gt;</code> &#8211; Get the value of a control. The response depends on the control type.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Control
 Name: &lt;control&gt;</pre>
</dl>
<p> Response for setting lights is:</p>
<dl>
<dd>
<pre>Light
 Num: 0
 Local Control: &lt;bool&gt;
 %Color: &lt;color&gt;
 %On Time: &lt;integer&gt;
 %Off Time: &lt;integer&gt;</pre>
</dl>
<p> Note that multiple lights may be present if the control supports multiple lights. The options values (marked with <code>%</code> ) will not be present if local control is set to true. Local control means that the LED takes whatever default function it does on the device (like disk activity, Ethernet activity, hot-swap LED, etc.). Response for id control:</p>
<dl>
<dd>
<pre>Data: &lt;byte1&gt; &lt;byte2&gt; ...</pre>
</dl>
<p> Response for other controls:</p>
<dl>
<dd>
<pre>Value
 Num: &lt;integer&gt;
 Value: &lt;integer&gt;</pre>
</dl>
<p> There will be one <code>Value</code> for each value the control supports. </p>
</dl>
<h3>mc</h3>
<p>Commands dealing with MC objects. </p>
<p> <code>reset &lt;warm | cold&gt; &lt;mc&gt;</code> &#8211; Do a warm or cold reset on the given MC</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Reset done: &lt;mc&gt;</pre>
</dl>
<p> <code>msg &lt;mc&gt; &lt;LUN&gt; &lt;NetFN&gt; &lt;Cmd&gt; [data&#8230;]</code> &#8211; Send the given command to the management controller and display the response.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre> MC: &lt;mc&gt;
 LUN: &lt;lun&gt;
 NetFN: &lt;netfn&gt;
 command: &lt;cmd&gt;
 Data: &lt;data bytes&gt;</pre>
</dl>
<p> <code>set_events_enable &lt;mc&gt; &lt;enable | disable&gt;</code> &#8211; enables or disables events on the MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Events enable done: &lt;mc&gt;</pre>
</dl>
<p> <code>get_events_enable &lt;mc&gt;</code> &#8211; Prints out if the events are enabled for the given MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Events Enable: &lt;bool&gt;</pre>
</dl>
<p> <code>sdrs &lt;mc&gt; &lt;main | sensor&gt;</code> &#8211; list the SDRs for the mc. Either gets the main SDR repository or the sensor SDR repository.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC
 Name: &lt;mc&gt;
 SDR
 Record ID: &lt;integer&gt;
 Type: &lt;integer&gt;
 Version: &lt;integer&gt;.&lt;integer&gt;
 Data: &lt;data bytes&gt;</pre>
</dl>
<p> One <code>SDR</code> will be present for each SDR in the repository. </p>
<p> <code>get_sel_time &lt;mc&gt;</code> &#8211; Get the time in the SEL for the given MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC
 Name: &lt;mc&gt;
 SEL Time: &lt;integer&gt;</pre>
</dl>
<p> <code>set_sel_time &lt;mc&gt; &lt;time&gt;</code> &#8211; Set the time in the SEL for the given MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC SEL time set
 Name: &lt;mc&gt;</pre>
</dl>
<p> <code>rescan_sel &lt;mc&gt; </code> &#8211; Rescan the SEL in the MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>SEL Rescan done: &lt;mc&gt;</pre>
</dl>
<p> <code>sel_rescan_time &lt;mc&gt; &lt;time in seconds&gt;</code> &#8211; Set the time between SEL rescans for the SEL on this MC. Zero disables scans.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC SEL rescan time set: &lt;domain&gt;</pre>
</dl>
<p> <code>sel_info &lt;mc&gt;</code> &#8211; Dump information about the MC&#8217;s SEL.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC
 Name: &lt;mc&gt;
 SEL Version: &lt;integer&gt;.&lt;integer&gt;
 SEL Count: &lt;integer&gt;
 SEL Slots Used: &lt;integer&gt;
 SEL Free Bytes: &lt;integer&gt;
 SEL Last Addition Timestamp: &lt;integer&gt;
 SEL overflow: &lt;bool&gt;
 SEL Supports Delete: &lt;bool&gt;
 SEL Supports Partial Add: &lt;bool&gt;
 SEL Supports Reserve: &lt;bool&gt;
 SEL Supports Get SEL Allocation: &lt;bool&gt;</pre>
</dl>
<p> <code>chan info &lt;mc&gt; &lt;channel&gt;</code> &#8211; Dump information about the MC&#8217;s channel.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Channel Info
 MC: &lt;mc&gt;
 Number: &lt;integer&gt;
 Medium: &lt;integer&gt;
 Protocol Type: &lt;integer&gt;
 Session Support: session-less|single-session|multi-session|session-based
 Vendor ID: &lt;data bytes&gt;
 Aux Info: &lt;data bytes&gt;</pre>
</dl>
<p> <code>chan get_access &lt;mc&gt; &lt;channel&gt; non-volatile|present|both</code> &#8211; Dump information about the MC&#8217;s channel access. There are two different places where this is stored, the present in-use values (volatile) and the non-volatile storage that is loaded at startup. Note if you specify channel 0xe, the response channel will be different; it will be the current channel.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Channel Access
 MC: &lt;mc&gt;
 Channel: &lt;integer&gt;
 Type: non-volatile|present
 Alerting Enabled: &lt;bool&gt;
 Per-Message Auth: &lt;bool&gt;
 User Auth: &lt;bool&gt;
 Access Mode: disable|pre-boot|always|shared
 Privilege Limit: callback|user|operator|admin|oem</pre>
</dl>
<p> <code>chan set_access &lt;mc&gt; &lt;channel&gt; non-volatile|present|both &lt;parm&gt; &lt;value&gt; &#8230;</code> &#8211; Set information about the MC&#8217;s channel access. There are two different places where this is stored, the present in-use values (volatile) and the non-volatile storage that is loaded at startup. Note if you specify channel 0xe, the modified channel will be the current channel. Parameters are:</p>
<dl>
<dd>
<pre>alert true|false
msg_auth true|false
user_auth true|false
access_mode disabled|pre-boot|always|shared
privilege_limit callback|user|operator|admin|oem</pre>
</dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Channel Access Set
 MC: &lt;mc&gt;
 Channel: &lt;integer&gt;</pre>
</dl>
<p> <code>chan user list &lt;mc&gt; &lt;channel&gt; [&lt;user num&gt;]</code> &#8211; List users associated with the channel. Each user number has an associated name and password that is global in the MC (not associated with a channel). There is also channel-specific information for each user. This command lists the global user information and the channel-specific information for the channel specified. If no user number is listed, then all users for the channel are listed. Otherwise only the given user is listed.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Channel Access Set
 MC: &lt;mc&gt;
 Channel: &lt;integer&gt;
 Max User: &lt;integer&gt;
 Enabled Users: &lt;integer&gt;
 Fixed Users: &lt;integer&gt;
 User
 Number: &lt;integer&gt;
 *String Name: &lt;string&gt;
 *Binary Name: &lt;data bytes&gt;
 Link Auth Enabled: &lt;bool&gt;
 Msg Auth Enabled: &lt;bool&gt;
 Access CB Only: &lt;bool&gt;
 Privilege Limit: &lt;integer&gt;
 Session Limit: &lt;integer&gt;
 .
 .</pre>
</dl>
<p> All the users are listed. One of string name or binary name is present, if the name is not a printable string, then the binary data is dumped. </p>
<p> <code>chan user set &lt;mc&gt; &lt;channel&gt; &lt;user num&gt; &lt;parm&gt; &lt;value&gt; &#8230;</code> &#8211; Set information about the user number. Only the specified values are modified. The name and password are global values, all other are channel-specific. The parms are: are:</p>
<dl>
<dd>
<pre>link_enabled true|false
msg_enabled true|false
cb_only true|false
privilege_limit callback|user|operator|admin|oem|no_access
session_limit &lt;integer&gt;
name &lt;user name string&gt;
password &lt;password string, &lt;= 16 characters&gt;
password2 &lt;password string, &lt;= 20 characters&gt;
enable
disable</pre>
</dl>
<p> The password is the 16-byte IPMI 1.5 passwords., the password2 is for 20-byte IPMI 2.0 passwords. Note that setting the session limit to zero means there is no session limit. Also note that some systems have a bug where the session limit is not optional (as the spec says it is). If you get C7 errors back from this command, you will have to always specify the session limit. Note that you must enable the user for it to work, but there seems to be no way to get if the user is enabled or not.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>User Info Set: &lt;mc&gt;</pre>
</dl>
</dl>
<h3>sel</h3>
<p>Commands dealing with the system event log. Note that there is no info command. </p>
<p> <code>list &lt;domain&gt;</code> &#8211; The list command is unique in this object, so it is specified explicitly here. List the local copy of the system event log for the entire domain.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Domain
 Name: &lt;domain&gt;
 Entries: &lt;integer&gt;
 Slots in use: &lt;integer&gt;
 Event
 **EVENT INFO**
 .
 .</pre>
</dl>
<p> <code>mc_list &lt;domain&gt;</code> &#8211; List the local copy of the system event log on the given MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC
 Name: &lt;mc&gt;
 Entries: &lt;integer&gt;
 Slots in use: &lt;integer&gt;
 Event
 **EVENT INFO**
 .
 .</pre>
</dl>
<p> <code>delete &lt;mc&gt; &lt;record #&gt;</code> &#8211; Delete the given event number from the SEL</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Event deleted
 MC: &lt;mc&gt;
 Record: &lt;integer&gt;</pre>
</dl>
<p> <code>add &lt;mc&gt; &lt;type&gt; &lt;13 bytes of data&gt;</code> &#8211; Add the event data to the SEL.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>MC
 Name: &lt;mc&gt;
 Record ID: &lt;integer&gt;</pre>
</dl>
<p> <code>clear &lt;domain&gt;</code> &#8211; clear the system event log</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>SEL Clear done: &lt;domain&gt;</pre>
</dl>
</dl>
<h3>con</h3>
<p>Commands dealing with connections. </p>
<p> <code>activate &lt;connection&gt;</code> &#8211; Activate the given connection</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>Connection activated: &lt;connection&gt;</pre>
</dl>
</dl>
<h3>pet</h3>
<p>Commands dealing with platform event traps. </p>
<p> <code>new &lt;domain&gt; &lt;connection&gt; &lt;channel&gt; &lt;ip addr&gt; &lt;mac_addr&gt; &lt;eft selector&gt;</code> &lt;policy num&gt; &lt;apt selector&gt; &lt;lan dest selector&gt; &#8211; Set up the domain to send PET traps from the given connection to the given IP/MAC address over the given channel.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PET Created: &lt;pet&gt;</pre>
</dl>
<p> <code>mcnew &lt;mc&gt; &lt;channel&gt; &lt;ip addr&gt; &lt;mac_addr&gt; &lt;eft selector&gt;</code> &lt;policy num&gt; &lt;apt selector&gt; &lt;lan dest selector&gt; &#8211; Set up the domain to send PET traps from the given connection to the given IP/MAC address over the given channel. This takes an MC instead of a connection.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PET Created: &lt;pet&gt;</pre>
</dl>
<p> <code>close &lt;pet&gt;</code> &#8211; Close the pet.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PET destroyed: &lt;pet&gt;</pre>
</dl>
</dl>
<h3>pef</h3>
<p>commands dealing with platform even filters. These are basically connections to the PEF configuration parameters in an MC. You use a pef to fetch a pef configuration, which you can then modify and write back to the MC. Note that when you get a pef config, you claim a lock on the MC that must be unlocked. </p>
<p> <code>new &lt;mc&gt;</code> &#8211; Create a pef for the given MC.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF: &lt;pef&gt;</pre>
</dl>
<p> <code>unlock_mc &lt;mc&gt;</code> &#8211; Unlock the PEF lock on the given MC.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF unlocked: &lt;mc&gt;</pre>
</dl>
<p> <code>close &lt;pef&gt;</code> &#8211; Free the given pef</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF destroyed: &lt;pef&gt;</pre>
</dl>
</dl>
<h3>pef config</h3>
<p>Commands dealing with PEF configurations. These are the actual PEF data items. </p>
<p> <code>get &lt;pef&gt;</code> &#8211; Fetch the pef data items from the pef and create a pef config.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF Config
 Name: &lt;pef config&gt;
 **PEF CONFIG**</pre>
</dl>
<p> <code>update &lt;pef config&gt; &lt;parm&gt; [selector] &lt;value&gt;</code> &#8211; Set the given parameter in the pef config to the given value. If the parameter has a selector of some type, the selector must be given, otherwise no selector should be given.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF config updated: &lt;pef config&gt;</pre>
</dl>
<p> <code>set &lt;pef&gt; &lt;pef config&gt;</code> &#8211; Write the pef data back to the pef. Note that this must be the same pef used to create the config.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF config set: &lt;pef config&gt;</pre>
</dl>
<p> <code>unlock &lt;pef&gt; &lt;pef config&gt;</code> &#8211; Unlock the lock in the MC and mark the pef config as unlocked.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF config unlocked: &lt;pef config&gt;</pre>
</dl>
<p> <code>close &lt;pef config&gt;</code> &#8211; Free the pef config.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>PEF config destroyed: &lt;pef config&gt;</pre>
</dl>
</dl>
<h3>lanparm</h3>
<p>Commands dealing with lanparms. These are basically connections to the LAN configuration parameters in an MC. You use a lanparm to fetch a lanparm config, which you can then modify and write back to the MC. Note that when you get a lanparm config, you claim a lock on the MC that must be unlocked. </p>
<p> <code>new &lt;mc&gt; &lt;channel&gt;</code> &#8211; Create a lanparm for the given MC and channel.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM: &lt;lanparm&gt;</pre>
</dl>
<p> <code>unlock_mc &lt;mc&gt; &lt;channel&gt;</code> &#8211; Unlock the lanparm lock on the given MC and channel.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM unlocked: &lt;mc&gt;</pre>
</dl>
<p> <code>close &lt;lanparm&gt;</code> &#8211; Free the given lanparm</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM destroyed: &lt;lanparm&gt;</pre>
</dl>
</dl>
<h3>lanparm config</h3>
<p>Commands dealing with lanparm configurations. These are the actual lanparm data items. </p>
<p> <code>get &lt;lanparm&gt;</code> &#8211; Fetch the lanparm data items from the lanparm and create a lanparm config.</p>
<dl>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM Config
 Name: &lt;lanparm config&gt;
 **LANPARM CONFIG**</pre>
</dl>
<p> <code>set &lt;lanparm&gt; &lt;lanparm config&gt;</code> &#8211; Write the lanparm data back to the lanparm. Note that this must be the same lanparm used to create the config.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM config set: &lt;lanparm config&gt;</pre>
</dl>
<p> <code>unlock &lt;lanparm&gt; &lt;lanparm config&gt;</code> &#8211; Unlock the lock in the MC and mark the lanparm config as unlocked.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM config unlocked: &lt;lanparm config&gt;</pre>
</dl>
<p> <code>close &lt;lanparm config&gt;</code> &#8211; Free the lanparm config.</p>
<dt>Response:</p>
<dd>
<dl>
<dd>
<pre>LANPARM config destroyed: &lt;lanparm config&gt;</pre>
</dl>
</dl>
<h2>Other Commands</h2>
<p>A few general commands exist. </p>
<p> <code>evinfo &lt;bool&gt;</code> &#8211; Turn on or off dumping object information when an event comes in. This is false by default. </p>
<p> <code>debug &lt;type&gt; &lt;bool&gt;</code> &#8211; Turn the given debugging type on or off</p>
<h2>Events</h2>
<p>The command language will output events to the console when they happen. Events all occur in the format:</p>
<dl>
<dd>
<pre> Event
 **EVENT INFO**</pre>
</dl>
<p> The event info varies on the type of events. The defined events are listed below. Note that the output of some events depends on the setting of the <code>evinfo</code> command; the information about the object itself may or may not be output. </p>
<p> Some events have another event container; this is the IPMI event that caused the event to be output. </p>
<p> The following event is output when the domain is completely up and operational and finished all it SDR, FRU, and bus scans:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Domain
 Name: &lt;domain&gt;
 Operation: Domain fully up
 Connection Number: &lt;integer&gt;
 Port Number: &lt;integer&gt;
 Any Connection Up: &lt;bool&gt;
 Error: &lt;integer&gt;</pre>
</dl>
<p> The following comes out when domain connection information changes:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Domain
 Name: &lt;domain&gt;
 Operation: Connection Change</pre>
</dl>
<p> The following comes out when domains are added:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Domain
 Name: &lt;domain&gt;
 Operation: Add
 %**DOMAIN INFO**</pre>
</dl>
<p> The following comes out when domains are destroyed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Domain
 Name: &lt;domain&gt;
 Operation: Delete</pre>
</dl>
<p> The following comes out when the domain gets an event that does not have a handler:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Event
 **EVENT INFO**</pre>
</dl>
<p> The following comes out when an entity is added:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity
 Name: &lt;entity&gt;
 Operation: Add
 %**ENTITY INFO**</pre>
</dl>
<p> The following comes out when an entity is deleted:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity
 Name: &lt;entity&gt;
 Operation: Delete</pre>
</dl>
<p> The following comes out when an entity is changed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity
 Name: &lt;entity&gt;
 Operation: Change
 %**ENTITY INFO**</pre>
</dl>
<p> The following comes out when an entity&#8217;s FRU is added:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity FRU
 Name: &lt;entity&gt;
 Operation: Add
 %**FRU INFO**</pre>
</dl>
<p> The following comes out when an entity&#8217;s FRU is deleted:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity FRU
 Name: &lt;entity&gt;
 Operation: Delete</pre>
</dl>
<p> The following comes out when an entity&#8217;s FRU is changed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity FRU
 Name: &lt;entity&gt;
 Operation: Change
 %**FRU INFO**</pre>
</dl>
<p> The following comes out when an entity&#8217;s presence changes:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity
 Name: &lt;entity&gt;
 Operation: Presence Change
 Present: &lt;bool&gt;
 %Event
 **EVENT INFO**</pre>
</dl>
<p> The following comes out when an entity&#8217;s hot-swap state changes:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Entity
 Name: &lt;entity&gt;
 Operation: Hot-Swap Change
 Last State: &lt;hot-swap state&gt;
 State: &lt;hot-swap state&gt;
 %Event
 **EVENT INFO**</pre>
</dl>
<p> The following comes out when an MC is added:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: MC
 Name: &lt;mc&gt;
 Operation: Add
 %**MC INFO**</pre>
</dl>
<p> The following comes out when an MC is removed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: MC
 Name: &lt;mc&gt;
 Operation: Delete</pre>
</dl>
<p> The following comes out when an MC is changed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: MC
 Name: &lt;mc&gt;
 Operation: Change
 %**MC INFO**</pre>
</dl>
<p> The following comes out when an MC changes active state:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: MC
 Name: &lt;mc&gt;
 Operation: Active Changed
 Active: &lt;bool&gt;</pre>
</dl>
<p> The following comes out when a discrete sensor gets an event:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Sensor
 Name: &lt;sensor&gt;
 Operation: Event
 Offset: &lt;integer&gt;
 Direction: assertion | deassertion
 Severity: &lt;integer&gt;
 Previous Severity: &lt;integer&gt;
 %Event
 **EVENT INFO**</pre>
</dl>
<p> The following comes out when a threshold sensor gets an event:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Sensor
 Name: &lt;sensor&gt;
 Operation: Event
 Threshold: &lt;threshold&gt;
 High/Low: going-high | going-low
 Direction: assertion | deassertion
 %Value: &lt;double&gt;
 %Raw Value: &lt;integer&gt;
 %Event
 **EVENT INFO**</pre>
</dl>
<p> The following comes out when a sensor is added:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Sensor
 Name: &lt;sensor&gt;
 Operation: Add
 %**SENSOR INFO**</pre>
</dl>
<p> The following comes out when a sensor is deleted:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Sensor
 Name: &lt;sensor&gt;
 Operation: Delete</pre>
</dl>
<p> The following comes out when a sensor is changed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Sensor
 Name: &lt;sensor&gt;
 Operation: Change
 %**SENSOR INFO**</pre>
</dl>
<p> The following comes out when a control gets an event:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Control
 Name: &lt;control&gt;
 Operation: Event
 Value
 Number: &lt;integer&gt;
 Value: &lt;integer&gt;
 %Event
 **EVENT INFO**</pre>
</dl>
<p> The following comes out when a control is added:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Control
 Name: &lt;control&gt;
 Operation: Add
 %**CONTROL INFO**</pre>
</dl>
<p> The following comes out when a control is deleted:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Control
 Name: &lt;control&gt;
 Operation: Delete</pre>
</dl>
<p> The following comes out when a control is changed:</p>
<dl>
<dd>
<pre> EVENT
 Object Type: Control
 Name: &lt;control&gt;
 Operation: Change
 %**CONTROL INFO**</pre>
</dl>
<h2>Object Info</h2>
<p>Many of the command responses and events contain information about an objects. The definitions of this information output is done here.</p>
<h3>**Event Info**</h3>
<dl>
<dd>
<pre> MC: &lt;mc&gt;
 Record ID: &lt;integer&gt;
 Event type: &lt;integer&gt;
 Timestamp: &lt;integer&gt;
 Data: &lt;data bytes&gt;</pre>
</dl>
<h3>**Domain Info**</h3>
<dl>
<dd>
<pre> Type: &lt;domain type&gt;
 GUID: &lt;hex string&gt;
 SEL Rescan Time: &lt;time&gt;
 IPMB Rescan Time: &lt;time&gt;</pre>
</dl>
<h3>**Entity Info**</h3>
<dl>
<dd>
<pre> Type: unknown | mc | fru | generic
 Present: &lt;bool&gt;
 Presence sensor always there: &lt;bool&gt;
 Hot swappable: &lt;bool&gt;
 %Supports managed hot swap: &lt;bool&gt;
 %Parents
 Name: &lt;entity&gt;
 Name: &lt;entity&gt;
 .
 .
 %Children
 Name: &lt;entity&gt;
 Name: &lt;entity&gt;
 .
 .
 %Physical Slot: &lt;integer&gt;
 %Id: &lt;string&gt;
 Entity ID String: &lt;string&gt;</pre>
</dl>
<p> Note that Parents and Children fields will not be present if the entity has no parents or children. Each entity type except <code>unknown</code> will have its own output info. These are: </p>
<p> <code>mc</code></p>
<dl>
<dd>
<pre> Channel: &lt;channel&gt;
 LUN: &lt;lun&gt;
 OEM: &lt;oem field from SDR&gt;
 Slave Address: &lt;ipmb&gt;
 ACPI_system_power_notify_required: &lt;bool&gt;
 ACPI_device_power_notify_required: &lt;bool&gt;
 controller_logs_init_agent_errors: &lt;bool&gt;
 log_init_agent_errors_accessing: &lt;bool&gt;
 global_init: &lt;bool&gt;
 chassis_device: &lt;bool&gt;
 bridge: &lt;bool&gt;
 IPMB_event_generator: &lt;bool&gt;
 IPMB_event_receiver: &lt;bool&gt;
 FRU_inventory_device: &lt;bool&gt;
 SEL_device: &lt;bool&gt;
 SDR_repository_device: &lt;bool&gt;
 sensor_device: &lt;bool&gt;</pre>
</dl>
<p> <code>fru</code></p>
<dl>
<dd>
<pre> Channel: &lt;channel&gt;
 LUN: &lt;lun&gt;
 OEM: &lt;oem field from SDR&gt;
 Slave Address: &lt;ipmb&gt;
 access_address: &lt;ipmb&gt;
 private_bus_id: &lt;integer&gt;
 device_type: &lt;integer&gt;
 device_modifier: &lt;integer&gt;
 is_logical_fru: &lt;bool&gt;
 fru_device_id: &lt;integer&gt;</pre>
</dl>
<p> <code>generic</code></p>
<dl>
<dd>
<pre> Channel: &lt;channel&gt;
 LUN: &lt;lun&gt;
 OEM: &lt;oem field from SDR&gt;
 access_address: &lt;ipmb&gt;
 private_bus_id: &lt;integer&gt;
 device_type: &lt;integer&gt;
 device_modifier: &lt;integer&gt;
 slave_address: &lt;ipmb&gt;
 address_span: &lt;integer&gt;</pre>
</dl>
<h3>**Mc Info**</h3>
<dl>
<dd>
<pre> Active: &lt;bool&gt;
 GUID: &lt;hex string&gt;
 SEL Rescan Time: &lt;integer&gt;
 provides_device_sdrs: &lt;bool&gt;
 device_available: &lt;bool&gt;
 chassis_support: &lt;bool&gt;
 bridge_support: &lt;bool&gt;
 ipmb_event_generator: &lt;bool&gt;
 ipmb_event_receiver: &lt;bool&gt;
 fru_inventory_support: &lt;bool&gt;
 sel_device_support: &lt;bool&gt;
 sdr_repository_support: &lt;bool&gt;
 sensor_device_support: &lt;bool&gt;
 device_id: &lt;ipmb&gt;
 device_revision: &lt;integer&gt;
 fw_revision: &lt;integer&gt;.&lt;integer&gt;
 version: &lt;integer&gt;.&lt;integer&gt;
 manufacturer_id: &lt;integer&gt;
 product_id: &lt;integer&gt;
 aux_fw_revision: &lt;integer&gt; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;</pre>
</dl>
<h3>*Sensor Info**</h3>
<dl>
<dd>
<pre> LUN: &lt;integer&gt;
 Number: &lt;integer&gt;
 Event Reading Type: &lt;integer&gt;
 Event Reading Type Name: one of:
 unspecified threshold discrete_usage discrete_state
 discrete_predictive_failure discrete_limit_exceeded
 discrete_performance_met discrete_severity discrete_device_presense
 discrete_device_enable discrete_availability discrete_redundancy
 discrete_acpi_power
 Type: &lt;integer&gt;
 Type Name: &lt;sensor type (a generic string)&gt;
 %Direction: input | output
 %Event Support: per state | entire sensor | global
 Init Scanning: &lt;bool&gt;
 Init Events: &lt;bool&gt;
 Init Thresholds: &lt;bool&gt;
 Init Hysteresis: &lt;bool&gt;
 Init Type: &lt;bool&gt;
 Init Power Up Events: &lt;bool&gt;
 Init Power Up Scanning: &lt;bool&gt;
 Ignore If No Entity: &lt;bool&gt;
 Auto Rearm: &lt;bool&gt;
 OEM1: &lt;integer&gt;
 Id: &lt;string&gt;</pre>
</dl>
<p> For threshold sensors, the following exist:</p>
<dl>
<dd>
<pre> Threshold Access: none | readable | settable | fixed
 Threshold
 Name: &lt;threshold&gt;
 Readable: &lt;bool&gt;
 Settable: &lt;bool&gt;
 Supports: going high assertion | going low assertion
 | going high deassertion | going low deassertion
 .
 .
 Hysteresis Support: none | readable | settable | fixed
 %Nominal Reading: &lt;float&gt;
 %Normal Max: &lt;float&gt;
 %Normal Min: &lt;float&gt;
 %Sensor Max: &lt;float&gt;
 %Sensor Min: &lt;float&gt;
 Base Unit: &lt;integer&gt;
 Base Unit Name: &lt;string&gt;
 %Rate Unit: &lt;integer&gt;
 %Rate Unit Name: &lt;string&gt;
 %Modifier Use: / | *
 %Modifier Unit: &lt;integer&gt;
 %Modifier Unit Name: &lt;string&gt;</pre>
</dl>
<p> For discrete sensors, the following exist:</p>
<dl>
<dd>
<pre> Event
 Offset: &lt;integer&gt;
 Supports: assertion | deassertion
 .
 .</pre>
</dl>
<h3>**Control Info**</h3>
<dl>
<dd>
<pre> Type: &lt;control type&gt;
 Generates Events: &lt;bool&gt;
 Settable: &lt;bool&gt;
 Readable: &lt;bool&gt;
 Num Values: &lt;integer&gt;
 Id: &lt;string&gt;</pre>
</dl>
<p> Controls of type light that are set with settings have the following:</p>
<dl>
<dd>
<pre> Set with: settings
 Local Control: &lt;bool&gt;
 Color: &lt;color&gt;
 .
 .</pre>
</dl>
<p> One color is listed for each supported color </p>
<p> Controls of type light that are set with transitions have the following:</p>
<dl>
<dd>
<pre> Light
 Number: &lt;integer&gt;
 Num Values: &lt;integer&gt;
 Value
 Number: &lt;integer&gt;
 Num Transitions: &lt;integer&gt;
 Transition
 Number: &lt;integer&gt;
 Color: &lt;color&gt;
 Time: &lt;integer&gt;
 .
 .
 .
 .</pre>
</dl>
<p> Controls of type identifier have the following:</p>
<dl>
<dd>
<pre> Max Length: &lt;integer&gt;</pre>
</dl>
<h3>**Fru Info**</h3>
<dl>
<dd>
<pre> Name: &lt;fru&gt;
 record
 Name: &lt;name&gt;
 Type: binary | ascii | unicode | integer
 %Number: &lt;integer&gt;
 Data: data depending on type
 .
 .
 Multi-record
 Number: &lt;integer&gt;
 Type: binary | ascii | unicode
 Data: &lt;data in the above format&gt;
 .
 .</pre>
</dl>
<h3>**Lanparm Config**</h3>
<dl>
<dd>
<pre> support_auth_oem: &lt;bool&gt;
 support_auth_straight: &lt;bool&gt;
 support_auth_md5: &lt;bool&gt;
 support_auth_md2: &lt;bool&gt;
 support_auth_none: &lt;bool&gt;
 ip_addr_source: &lt;integer&gt;
 num_alert_destinations: &lt;integer&gt;
 %ipv4_ttl: &lt;integer&gt;
 %ipv4_flags: &lt;integer&gt;
 %ipv4_precedence: &lt;integer&gt;
 %ipv4_tos: &lt;integer&gt;
 %ip_addr: &lt;ip addr&gt;
 %mac_addr: &lt;mac addr&gt;
 %subnet_mask: &lt;ip addr&gt;
 %primary_rmcp_port &lt;integer&gt;
 %secondary_rmcp_port &lt;integer&gt;
 %bmc_generated_arps: &lt;bool&gt;
 %bmc_generated_garps: &lt;bool&gt;
 %garp_interval: &lt;integer&gt;
 %default_gateway_ip_addr: &lt;ip addr&gt;
 %default_gateway_mac_addr: &lt;mac addr&gt;
 %backup_gateway_ip_addr: &lt;ip addr&gt;
 %backup_gateway_mac_addr: &lt;mac addr&gt;
 community_string: &lt;string&gt;
 User
 Name: callback
 enable_auth_oem: &lt;bool&gt;
 enable_auth_straight: &lt;bool&gt;
 enable_auth_md5: &lt;bool&gt;
 enable_auth_md2: &lt;bool&gt;
 enable_auth_none: &lt;bool&gt;
 User
 Name: user
 enable_auth_oem: &lt;bool&gt;
 enable_auth_straight: &lt;bool&gt;
 enable_auth_md5: &lt;bool&gt;
 enable_auth_md2: &lt;bool&gt;
 enable_auth_none: &lt;bool&gt;
 User
 Name: operator
 enable_auth_oem: &lt;bool&gt;
 enable_auth_straight: &lt;bool&gt;
 enable_auth_md5: &lt;bool&gt;
 enable_auth_md2: &lt;bool&gt;
 enable_auth_none: &lt;bool&gt;
 User
 Name: admin
 enable_auth_oem: &lt;bool&gt;
 enable_auth_straight: &lt;bool&gt;
 enable_auth_md5: &lt;bool&gt;
 enable_auth_md2: &lt;bool&gt;
 enable_auth_none: &lt;bool&gt;
 User
 Name: oem
 enable_auth_oem: &lt;bool&gt;
 enable_auth_straight: &lt;bool&gt;
 enable_auth_md5: &lt;bool&gt;
 enable_auth_md2: &lt;bool&gt;
 enable_auth_none: &lt;bool&gt;
 Alert Destination
 Number: &lt;integer&gt;
 alert_ack: &lt;bool&gt;
 dest_type: &lt;integer&gt;
 alert_retry_interval: &lt;integer&gt;
 max_alert_retries: &lt;integer&gt;
 dest_format: &lt;integer&gt;
 gw_to_use: &lt;integer&gt;
 dest_ip_addr: &lt;ip addr&gt;
 dest_mac_addr: &lt;mac addr&gt;
 .
 .</pre>
</dl>
<h3>**Pef Config**</h3>
<dl>
<dd>
<pre> alert_startup_delay_enabled: &lt;bool&gt;
 startup_delay_enabled: &lt;bool&gt;
 event_messages_enabled: &lt;bool&gt;
 pef_enabled: &lt;bool&gt;
 diagnostic_interrupt_enabled: &lt;bool&gt;
 oem_action_enabled: &lt;bool&gt;
 power_cycle_enabled: &lt;bool&gt;
 reset_enabled: &lt;bool&gt;
 power_down_enabled: &lt;bool&gt;
 alert_enabled: &lt;bool&gt;
 %startup_delay: &lt;integer&gt;
 %alert_startup_delay: &lt;integer&gt;
 guid_enabled: &lt;bool&gt;
 guid_val: &lt;guid&gt;
 num_event_filters: &lt;integer&gt;
 num_alert_policies: &lt;integer&gt;
 num_alert_strings: &lt;integer&gt;
 Event Filter
 Number: &lt;integer&gt;
 enable_filter: &lt;bool&gt;
 filter_type: &lt;integer&gt;
 diagnostic_interrupt: &lt;bool&gt;
 oem_action: &lt;bool&gt;
 power_cycle: &lt;bool&gt;
 reset: &lt;bool&gt;
 power_down: &lt;bool&gt;
 alert: &lt;bool&gt;
 alert_policy_number: &lt;integer&gt;
 event_severity: &lt;integer&gt;
 generator_id_addr: &lt;integer&gt;
 generator_id_channel_lun: &lt;integer&gt;
 sensor_type: &lt;integer&gt;
 sensor_number: &lt;integer&gt;
 event_trigger: &lt;integer&gt;
 data1_offset_mask: &lt;integer&gt;
 data1_mask: &lt;integer&gt;
 data1_compare1: &lt;integer&gt;
 data1_compare2: &lt;integer&gt;
 data2_mask: &lt;integer&gt;
 data2_compare1: &lt;integer&gt;
 data2_compare2: &lt;integer&gt;
 data3_mask: &lt;integer&gt;
 data3_compare1: &lt;integer&gt;
 data3_compare2: &lt;integer&gt;
 .
 .
 Alert Policy
 Number: &lt;integer&gt;
 policy_num: &lt;integer&gt;
 enabled: &lt;bool&gt;
 policy: &lt;integer&gt;
 channel: &lt;integer&gt;
 destination_selector: &lt;integer&gt;
 alert_string_event_specific: &lt;bool&gt;
 alert_string_selector: &lt;integer&gt;
 .
 .
 Alert String
 event_filter: &lt;integer&gt;
 alert_string_set: &lt;integer&gt;
 alert_string: &lt;string&gt;
 .
 .</pre>
</dl>
<h3>**Connection Info**</h3>
<dl>
<dd>
<pre> Active: &lt;bool&gt;
 Up: &lt;bool&gt;
 Port
 Number: &lt;integer&gt;
 Info: &lt;info string&gt;
 Up: &lt;bool&gt;
 .
 .</pre>
</dl>
<h3>**Pef Info**</h3>
<dl>
<dd>
<pre> MC: &lt;mc&gt;</pre>
</dl>
<h3>**Pet Info**</h3>
<dl>
<dd>
<pre> MC: &lt;mc&gt;
 Channel: &lt;channel&gt;
 IP Address: &lt;ip address&gt;
 MAC Address: &lt;mac address&gt;
 EFT Selector: &lt;eft selector&gt;
 Policy Number: &lt;policy number&gt;
 APT Selector: &lt;apt selector&gt;
 LAN Dest Selector: &lt;lan dest selector&gt;</pre>
</dl>
<h3>**Lanparm Info**</h3>
<dl>
<dd>
<pre> MC: &lt;mc&gt;
 Channel: &lt;integer&gt;</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipmish/">ipmish</a></code>(1) </p>
<h2>Known Problems</h2>
<p>None</p>
<h2>Author</h2>
<p>Corey Minyard &lt;cminyard [at] mvista.org&gt;</p>
