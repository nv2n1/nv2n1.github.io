---
title: "rarc(5)"
name: "rarc"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rarc/"
description: "rarc – ra client resource file."
---

<p><code>rarc</code> &#8211; <code>ra</code> client resource file.</p>
<h2>Synopsis</h2>
<p><code>rarc</code></p>
<h2>Description</h2>
<p>Ra* clients will open this file if its in the users $HOME directory, or in the $ARGUSHOME directory, and parse it to set common configuration options. All of these values will be overriden by options set on the command line, or in the file specified using the &#8216;-F conffile&#8217; option. Values can be quoted to make string denotation easier, however, the parser does not require that string values be quoted. To support this, the parse will remove &quot; (double quote) characters from input strings, so do not use this character in strings themselves. Values specified as &quot;&quot; will be treated as a NULL string, and the parser will ignore the variable setting. </p>
<h2>Ra_Argus_Server</h2>
<p>All ra* clients can attach to a remote server, and collect argus data in real time. This variable can be a name or a dot notation IP address. Optionally you can specify a port number using a &#8216;:&#8217; and then providing the port number desired. </p>
<p> <code>RA_ARGUS_SERVER=</code>localhost:561</p>
<h2>Ra_Source_Port</h2>
<p>You can change the default source port value that will be used on remote TCP and UDP connections, using this variable. When you specify the remote server using the -S option, when you don&#8217;t specify a port number, this is the port number it will use. </p>
<p> The default port number is 561. </p>
<p> <code>RA_SOURCE_PORT=</code>561</p>
<h2>Pid File Support</h2>
<p>Any ra* program can generate a pid file, which can be used to control the number of instances that the system can support. </p>
<p> Creating a system pid file may require priviledges that may not be inappropriate for all cases. By specifying <code>RA_PID_PATH</code>, you can create personal pid files that will enforce your own policy for your own use of the ra* programs. </p>
<p> When configured to generate a pid file for a ra* program, if a file called ra*.pid (where ra* is the name of the program in question) exists in the RA_PID_PATH directory, and a program exists with a pid that matches the one contained in the file, then the program will not start. If the pid does not exist, then the ra* program replaces the value in the file, with its own pid. If a pid file does not exist, then the ra* program will create it in the RA_PID_PATH directory, if it can. The end result is that the system will support only one instanace of the program, based on name, running at a time. </p>
<p> The default value is to not generate a pid. The default path for the pid file, is /var/run. </p>
<p> No Commandline equivalent </p>
<pre><code>RA_SET_PID=</code>&quot;no&quot;
<code>RA_PID_PATH=</code>&quot;/var/run&quot;</pre>
<h2>Ra_Output_File</h2>
<p>All ra* clients can support writing output as Argus Records into a file or stdout. Stdout is specified as &#8216;-&#8216;. </p>
<p> <code>RA_OUTPUT_FILE=</code>&quot;filename&quot;</p>
<h2>Ra_Timerange</h2>
<p>All ra* clients can support input filtering on a time range. The format is: </p>
<pre> <code>timeSpecification[-timeSpecification]</code>
where the format of a timeSpecification can be:
 [[[yy/]mm/]dd.]hh[:mm[:ss]]
 [yy/]mm/dd
<code>RA_TIMERANGE=</code>&quot;55/12/04.00:00:01-55/12/04.23:59:59&quot;
<code>RA_TIMERANGE=</code>&quot;12/04-12/05&quot;</pre>
<h2>Ra_Run_Time</h2>
<p>All ra* clients can support running for a number of seconds, while attached to a remote source of argus data. This is a type of polling. The default is zero (0), which means run indefinately. </p>
<p> <code>RA_RUN_TIME</code>=0</p>
<h2>Ra_Print_Man_Records</h2>
<p>Specify if ra* clients should print management records by default. This does not affect management record processing, nor down stream management record propagation. </p>
<p> Commandline equivalents: -M [no]man </p>
<p> <code>RA_PRINT_MAN_RECORDS</code>=no <code>RA_PRINT_EVENT_RECORDS</code>=no</p>
<h2>Ra_Print_Labels</h2>
<p>Most ra* clients are designed to print argus records out in ASCII, with each client supporting its own output formats. For ra() like clients, this variable will generate column headers as labels. The number is the number of lines between repeated header labeling. Setting this value to zero (0) will cause the labels to be printed once. If you don&#8217;t want labels, comment this line out, delete it or set the value to -1. </p>
<p> <code>RA_PRINT_LABELS</code>=0</p>
<h2>Ra_Field_Delimiter</h2>
<p>Most ra* clients are designed to print argus records out in ASCII, with each client supporting its own output formats. For ra() like clients, this variable can overide the default field delimiter, which are variable spans of space (&#8216; &#8216;), to be any character. The most common are expected to be &#8216; &#8216; for tabs, and &#8216;,&#8217; for comma separated fields. </p>
<p> <code>RA_FIELD_DELIMITER=</code>&#8216;,&#8217;</p>
<h2>Ra_Print_Names</h2>
<p>For <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> like clients, this variable will control the translation of various numbers to names, such as address hostnames, port service names and/or protocol names. There can be a huge performance impact with name lookup, so the default is to not resolve hostnames. </p>
<p> <code>RA_PRINT_NAMES=</code>port </p>
<p> Other valid options are none to print no names, proto to translate the protocol names, port to translate port names, and all to translate all the fields. An invalid option will default to port, silently.</p>
<h2>Ra_Cidr_Address_Format</h2>
<p>Use this variable to specify whether <code>ra()</code> clients, when printing numeric IP addresses, will print them as CIDR addresses, or not. CIDR notation is constructed from the IP address and the prefix size, the latter being the number of leading 1 bits of the routing prefix. The IP address is expressed according to the standards of IPv4 or IPv6. It is followed by a separator character, the forward slash (/) character, and the prefix size expressed as a decimal number.<br />
&nbsp;<wbr> Argus IPv4 data contains the CIDR mask length, when its less than 32, and ra* programs will by default provides the &quot;/masklen&quot; suffix when the mask is less than 32.<br />
&nbsp;<wbr> This maybe confusing for some data processors, which would rather not see the &quot;/masklen&quot; never, or all the time. Use this option to specify changes in the default printing stratgy.<br />
&nbsp;<wbr> Accepatable values for this variable are:<br />
&nbsp;<wbr>&quot;no&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>do not provide the CIDR mask length&nbsp;<wbr>(legacy mode)&nbsp;<wbr>[default]<br />
&nbsp;<wbr>&quot;yes&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>print CIDR mask length when less than 32<br />
&nbsp;<wbr>&quot;strict&quot;&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>always print CIDR mask length </p>
<p> <code>RA_CIDR_ADDRESS_FORMAT=</code>&quot;no&quot;</p>
<h2>Ra_Asn_Print_Format</h2>
<p>All ra() clients can print and process AS Numbers that have been added to the records through metadata labeling, or were a part of the original Netflow to argus conversion process.. </p>
<p> RFC 5396 specifies 3 formats for representing AS Numbers, and all 3 are acceptable formats. These format are:<br />
&nbsp;<wbr>&quot;asplain&quot;&nbsp;<wbr>&#8211; 2 and 4-byte ASNs are printed as decimal integers.<br />
&nbsp;<wbr>&quot;asdot+&quot;&nbsp;<wbr>&nbsp;<wbr>&#8211; 2 and 4-byte ASNs are printed using a dot notation.<br />
&nbsp;<wbr>&quot;asdot&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 2 byte ASNs are printed as decimal, and 4-byte ASNs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>are printed using a dotted notation.. </p>
<p> The default is &#8216;asplain&#8217;. </p>
<p> No Commandline equivalent </p>
<p> <code>RA_ASN_PRINT_FORMAT=</code>&quot;asplain&quot;</p>
<h2>Ra_Print_Response_Data</h2>
<p>For ra() like clients, this variable will include the response data that is provided by Argus. This is protocol and state specific. </p>
<p> <code>RA_PRINT_RESPONSE_DATA=</code>no</p>
<h2>Ra_Print_Unix_Time</h2>
<p>For ra() like clients, this variable will force the timestamp to be in Unix time format, which is an integer representing the number of elapsed seconds since the epoch. </p>
<p> <code>RA_PRINT_UNIX_TIME</code>=no</p>
<h2>Ra_Time_Format</h2>
<p>For ra() like clients, the format that is used to print timestamps, is based on the strftime() library call, with an extension to print fractions of a sec using &quot;%f&quot;. The default is &quot;%T.%f&quot;. You can overide this default time format by setting this variable. This string must conform to the format specified in strftime(). Malformed strings can generate interesting output, so be aware with this one, and don&#8217;t forget the &#8216;.&#8217; when doing fractions of a second. </p>
<p> <code>RA_TIME_FORMAT=</code>&quot;%T.%f&quot;</p>
<h2>Ra_Tz</h2>
<p>The timezone used for timestamps is specified by the tzset() library routines, and is normally specified by factors such as the TZ environment variable found on most machines. You can override the TZ environment variable by specifying a time zone using this variable. The format of this string must conform to the format specified by <a href="/docs/linux/man/3-tzset/">tzset</a>(3). </p>
<pre><code>RA_TZ=</code>&quot;EST5EDT4,M3.2.0/02,M11.1.0/02&quot;
<code>RA_TZ=</code>&quot;PST8PDT&quot;</pre>
<h2>Ra_Usec_Precision</h2>
<p>For ra() like clients, this variable is used to override the time format of the timestamp. This variable specifies the number of decimal places that will be printed as the fractional part of the time. Argus collects usec precision, and so a maximum value of 6 is supported. To not print the fractional part, specify the value zero (0). </p>
<p> <code>RA_USEC_PRECISION=</code>6</p>
<h2>Ra_Userdata_Encode</h2>
<p>Argus can capture user data, and the argus clients can print, merge, filter, and strip user data from argus records. When printing out the user data contents, using tools such as ra.1, the type of encoding used to print the buffers can be specified here. This is available because many user data buffers are not printable text, and other representations may be more appropriate. </p>
<p> Supported values are &quot;Ascii&quot;, &quot;Obfuscate&quot;, &quot;Hex&quot;, &quot;Encode32&quot; or &quot;Encode64&quot;. The default is &quot;Ascii&quot;. </p>
<p> Obfuscate is an extension to the Ascii print, that attempts to over-write plain text passwords, encountered in the user data, with &#8216;x&#8217;s. </p>
<p> Commandline equivalent: -M printer=&lt;printer&gt; </p>
<p> <code>RA_USERDATA_ENCODE=</code>Ascii</p>
<h2>Ra_Filter</h2>
<p>You can provide a filter expression here, if you like. It should be limited to 2K in length. The default is to not filter. See <a href="/docs/linux/man/1-ra/">ra</a>(1) for the format of the filter expression. </p>
<p> <code>RA_FILTER=</code>&quot;&quot;</p>
<h2>Ra_Filter_Timeout</h2>
<p>The filter is compiled in a separate process, and all ra* programs need to wait a reasonable time for the filter compiler to finish, or time out and return an error, in the case of a fatal error in compiling. Many systems are very busy, and could benefit from a prolonged wait period, however, this timeout value could generate a significant startup wait state for programs that have poor filter specifications, if the timer is too long. </p>
<p> The current default is 1.5 seconds, but you can set this to any amount of time. </p>
<p> No Commandline equivalent </p>
<p> <code>RA_FILTER_TIMEOUT=</code>1.5</p>
<h2>Sasl Suppport</h2>
<p>When argus is compiled with SASL support, ra* clients may be required to authenticate to the argus server before the argus will accept the connection. This variable will allow one to set the user and authorization id&#8217;s, if needed. Although not the best practice, you can provide a password through the RA_AUTH_PASS variable. If you do this, you should protect the contents of this file. The format for this variable is:<br />
&nbsp;<wbr> </p>
<pre><code>RA_USER_AUTH=</code>&quot;user_id/authorization_id&quot;
<code>RA_AUTH_PASS=</code>&quot;password&quot;</pre>
<p>The clients can specify a part of the negotiation of the security policy that argus uses. This is controlled through the use of a minimum and maximum allowable protection strength values. Set these variable to control this policy. </p>
<pre><code>RA_MIN_SSF=</code>0
<code>RA_MAX_SSF=</code>128</pre>
<h2>Ra_Debug_Level</h2>
<p>If compiled to support this option, ra* clients are capable of generating a lot of use [full | less | whatever] debug information. The default value is zero (0). </p>
<pre><code>RA_DEBUG_LEVEL=</code>0</pre>
<h2>Ra_Connect_Time</h2>
<p>Some ra style clients use a non-blocking method to connect to remote data sources, so the user many need to control how long to wait if a remote source doesn&#8217;t respond. This variable sets the number of seconds to wait. This number should be set to a reasonable value (5 &lt; value &lt; 60). The default value is 10 seconds. </p>
<pre><code>RA_CONNECT_TIME=</code>10</pre>
<h2>Ra_Sort_Algorithms</h2>
<p>Many ra* programs sort records as a part of their function. Programs like rasort.1, providing explicit command-line options to specify the sort algorithms and their order, using the </p>
<p> Use this configuration directive to specify the default sorting algorithm table for your ra* programs. The default sort algorithm is record start time &quot;stime&quot;. </p>
<pre><code>RA_SORT_ALGORITHMS=</code>&quot;stime &quot;</pre>
<h2>Ra_Timeout_Interval</h2>
<p>Some ra* clients have a timeout based function. Ratop, as an example, times out flows and removes them from screen at a fixed interval. This variable can be set using the RA_TIMEOUT_INTERVAL variable, which is a float in seconds. 60.0 seconds is the default. </p>
<pre><code>RA_TIMEOUT_INTERVAL=</code>60.0</pre>
<h2>Ra_Update_Interval</h2>
<p>Some ra* clients have an interval based function. Ratop, as an example, can refresh the screen at a fixed interval. This variable can be set using the RA_UPDATE_INTERVAL variable, which is a float in seconds. 0.5 seconds is the default. </p>
<pre><code>RA_UPDATE_INTERVAL=</code>0.5</pre>
<h2>Ra_Print_Ethernet_Vendors</h2>
<p>All ra* clients have the ability to print vendor names for the vendor part of ethernet addresses that are in flow records. ra* programs get its strings for the ethernet vendors using Wireshark &#8216;manuf&#8217; files. One is provided with the distribution, and installed into /usr/local/argus. </p>
<p> No Commandline equivalent </p>
<pre><code>RA_PRINT_ETHERNET_VENDORS=</code>&quot;no&quot;
<code>RA_ETHERNET_VENDORS=</code>&quot;/usr/local/argus/wireshark.manuf.txt&quot;</pre>
<h2>Ra_Delegated_Ip</h2>
<p>All ra* clients have the ability to print country codes for the IP addresses that are in a flow record. Country codes are generated from the ARIN delegated address space files. Specify the location of your DELEGATED_IP file here. </p>
<p> No Commandline equivalent </p>
<pre><code>RA_DELEGATED_IP=</code>&quot;/usr/local/argus/delegated-ipv4-latest&quot;</pre>
<h2>Ra_Reliable_Connect</h2>
<p>All ra* clients can reliably connect to remote data sources. This causes the ra* program to try to reconnect to lost remote sources every 5 seconds, indefinately. This causes ra* program to not terminate but retry connection attempts when they fail. </p>
<p> This feature is implemented using threads, and so threads support must be compiled in. </p>
<p> No Commandline equivalent </p>
<pre><code>RA_RELIABLE_CONNECT=</code>no</pre>
<h2>Mysql Support</h2>
<p>Many ra* clients can connect and use a MySQL database, either reading for writing. This may require references to remotes database hosts, databases, tables, and mysql account names and passwords. </p>
<p> Default values for these variables can be set here. support must be compiled in. </p>
<p> Commandline equivalents:<br />
&nbsp;<wbr>&nbsp;<wbr>-r&nbsp;<wbr><a href="mysql://[username[:password]@]hostname[:port]/database/tablename">mysql://[username[:password]@]hostname[:port]/database/tablename</a><br />
&nbsp;<wbr>&nbsp;<wbr>-w&nbsp;<wbr><a href="mysql://[username[:password]@]hostname[:port]/database/tablename">mysql://[username[:password]@]hostname[:port]/database/tablename</a><br />
&nbsp;<wbr>&nbsp;<wbr>-u username:password </p>
<pre><code>RA_DATABASE=</code>&quot;argus&quot;
<code>RA_DB_TABLE=</code>&quot;table&quot;
<code>RA_DB_USER=</code>&quot;carter&quot;
<code>RA_DB_PASS=</code>&quot;whatever&quot;</pre>
<p>Those ra* clients that can create database tables may need to specify a table type or rather, a database engine other than the defaul, MyISAM. </p>
<p> Commandline equivalents:<br />
&nbsp;<wbr>&nbsp;<wbr>-M mysql_engine=tableType<br />
&nbsp;<wbr>&nbsp;<wbr>Current tableTypes are<br />
&nbsp;<wbr>&nbsp;<wbr>MyISAM<br />
&nbsp;<wbr>&nbsp;<wbr>InnoDB<br />
&nbsp;<wbr>&nbsp;<wbr>Merge<br />
&nbsp;<wbr>&nbsp;<wbr>Memory<br />
&nbsp;<wbr>&nbsp;<wbr>Archive<br />
&nbsp;<wbr>&nbsp;<wbr>NDB<br />
&nbsp;<wbr>&nbsp;<wbr>Federated<br />
&nbsp;<wbr>&nbsp;<wbr>CSV </p>
<pre><code>MYSQL_DB_ENGINE=</code>&quot;MyISAM&quot;</pre>
<h2>Color Support</h2>
<p>For ra* programs that use curses, these variables defined color schemes and color assignments.<br />
&nbsp;<wbr> Argus uses a sixteen color palette, with 8 monotone and 8 accent colors, plus 16 colors of gray. Currently these color values are hard coded. New versions should allow you to provide color definitions for all internal values using a 256 Xterm color wheel, to assign foreground and background colors. But we&#8217;re not there yet </p>
<pre><code>RA_COLOR_SUPPORT=</code>&quot;yes&quot;
<code>RA_COLOR_CONFIG=</code>&quot;/usr/carter/.racolor.conf&quot;</pre>
<h2>Direction Support</h2>
<p>Many ra* clients process flow records based on source and destination properties. TCP and UDP ports values can be used to assign direction, and are best used for well-known ports (&lt; 1024), values that are in the /etc/services defintions, and the reserved ports (&gt; 1023, &lt; 49151). </p>
<p> The syntax is:<br />
&nbsp;<wbr>RA_PORT_DIRECTION=&quot;services&quot;<br />
&nbsp;<wbr>RA_PORT_DIRECTION=&quot;services,wellknown&quot;<br />
&nbsp;<wbr>RA_PORT_DIRECTION=&quot;services,wellknown,registered&quot; </p>
<p> We recommend the wellknown and services options, as they are a bit more discriminating. If there are ports that you know are services that are in the registered port range, we suggest that you add them to your /etc/services file rather than include the registered port range; only because the registered range is so large. However, this option is applied only to flow in which the direction is ambiguous, and as such, corrections based on the logic should have minimum effect on analytics. </p>
<pre><code>RA_PORT_DIRECTION=</code>&quot;services,wellknown&quot;</pre>
<p>Sites use locality for a number of features, such as access control, and this support is intended to support visualization, and analytics. </p>
<p> Currently, you can identify a collection of IP addresses that represent RA_LOCAL, and are specified using an iana-address-file formatted file. (See ralabel.conf) </p>
<pre><code>RA_LOCAL=</code>&quot;/usr/local/argus/local.addrs&quot;</pre>
<p>When locality information is available, programs like ra(), and as the assignement of source when there is ambiguity in the flow record as to who is the actual initiator or receiver of the flow. </p>
<p> When locality information is available, programs like ra(), and ratop() can use that information to make display decisions, such </p>
<p> RA_LOCAL_DIRECTION provides the logic for using the locality information to assign flow direction. You can force the local address to be either the source (src) or the destination (dst). </p>
<p> The syntax is:<br />
&nbsp;<wbr>RA_LOCAL_DIRECTION=&quot;local:src&quot;<br />
&nbsp;<wbr>RA_LOCAL_DIRECTION=&quot;local:dst&quot; </p>
<pre><code>RA_LOCAL_DIRECTION=&quot;suggest:src&quot;
RA_LOCAL_DIRECTION=&quot;force:src
</code></pre>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ra/">ra</a></code>(1) </p>
