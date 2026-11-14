---
title: "dhclient-conf(5)"
name: "dhclient-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhclient-conf/"
description: "dhclient.conf – DHCP client configuration file"
---

<p>dhclient.conf &#8211; DHCP client configuration file</p>
<h2>Description</h2>
<p>The dhclient.conf file contains configuration information for <i>dhclient,</i> the Internet Systems Consortium DHCP Client. </p>
<p> The dhclient.conf file is a free-form ASCII text file. It is parsed by the recursive-descent parser built into dhclient. The file may contain extra tabs and newlines for formatting purposes. Keywords in the file are case-insensitive. Comments may be placed anywhere within the file (except within quotes). Comments begin with the # character and end at the end of the line. </p>
<p> The dhclient.conf file can be used to configure the behaviour of the client in a wide variety of ways: protocol timing, information requested from the server, information required of the server, defaults to use if the server does not provide certain information, values with which to override information provided by the server, or values to prepend or append to information provided by the server. The configuration file can also be preinitialized with addresses to use on networks that don&#8217;t have DHCP servers.</p>
<h2>Protocol Timing</h2>
<p>The timing behaviour of the client need not be configured by the user. If no timing configuration is provided by the user, a fairly reasonable timing behaviour will be used by default &#8211; one which results in fairly timely updates without placing an inordinate load on the server. </p>
<p> If required the following statements can be used to adjust the timing behaviour of the DHCPv4 client. The DHCPv6 protocol provides values to use and they are not currently configurable. </p>
<p> <i>The</i> <code>timeout</code> <i>statement</i> </p>
<p>&nbsp;<code>timeout&nbsp;</code><i>time</i><code>;</code> </p>
<p> The <i>timeout</i> statement determines the amount of time that must pass between the time that the client begins to try to determine its address and the time that it decides that it&#8217;s not going to be able to contact a server. By default, this timeout is 300 seconds. After the timeout has passed, if there are any static leases defined in the configuration file, or any leases remaining in the lease database that have not yet expired, the client will loop through these leases attempting to validate them, and if it finds one that appears to be valid, it will use that lease&#8217;s address. If there are no valid static leases or unexpired leases in the lease database, the client will restart the protocol after the defined retry interval. </p>
<p> <i>The</i> <code>retry</code> <i>statement</i> </p>
<p>&nbsp;<code>retry&nbsp;</code><i>time</i><code>;</code> </p>
<p> The <i>retry</i> statement determines the time that must pass after the client has determined that there is no DHCP server present before it tries again to contact a DHCP server. By default, this is five minutes. </p>
<p> <i>The</i> <code>select-timeout</code> <i>statement</i> </p>
<p>&nbsp;<code>select-timeout&nbsp;</code><i>time</i><code>;</code> </p>
<p> It is possible (some might say desirable) for there to be more than one DHCP server serving any given network. In this case, it is possible that a client may be sent more than one offer in response to its initial lease discovery message. It may be that one of these offers is preferable to the other (e.g., one offer may have the address the client previously used, and the other may not). </p>
<p> The <i>select-timeout</i> is the time after the client sends its first lease discovery request at which it stops waiting for offers from servers, assuming that it has received at least one such offer. If no offers have been received by the time the <i>select-timeout</i> has expired, the client will accept the first offer that arrives. </p>
<p> By default, the select-timeout is zero seconds &#8211; that is, the client will take the first offer it sees. </p>
<p> <i>The</i> <code>reboot</code> <i>statement</i> </p>
<p>&nbsp;<code>reboot&nbsp;</code><i>time</i><code>;</code> </p>
<p> When the client is restarted, it first tries to reacquire the last address it had. This is called the INIT-REBOOT state. If it is still attached to the same network it was attached to when it last ran, this is the quickest way to get started. The <i>reboot</i> statement sets the time that must elapse after the client first tries to reacquire its old address before it gives up and tries to discover a new address. By default, the reboot timeout is ten seconds. </p>
<p> <i>The</i> <code>backoff-cutoff</code> <i>statement</i> </p>
<p>&nbsp;<code>backoff-cutoff&nbsp;</code><i>time</i><code>;</code> </p>
<p> The client uses an exponential backoff algorithm with some randomness, so that if many clients try to configure themselves at the same time, they will not make their requests in lockstep. The <i>backoff-cutoff</i> statement determines the maximum amount of time that the client is allowed to back off, the actual value will be evaluated randomly between 1/2 to 1 1/2 times the <i>time</i> specified. It defaults to fifteen seconds. </p>
<p> <i>The</i> <code>initial-interval</code> <i>statement</i> </p>
<p>&nbsp;<code>initial-interval&nbsp;</code><i>time</i><code>;</code> </p>
<p> The <i>initial-interval</i> statement sets the amount of time between the first attempt to reach a server and the second attempt to reach a server. Each time a message is sent, the interval between messages is incremented by twice the current interval multiplied by a random number between zero and one. If it is greater than the backoff-cutoff amount, it is set to that amount. It defaults to ten seconds. </p>
<p> <i>The initial-delay</i> <i>statement</i> </p>
<p>&nbsp;<code>initial-delay&nbsp;</code><i>time</i><code>;</code> </p>
<p> <i>initial-delay </i> parameter sets the maximum time client can wait after start before commencing first transmission. According to RFC2131 Section 4.4.1, client should wait a random time between startup and the actual first transmission. Previous versions of ISC DHCP client used to wait random time up to 5 seconds, but that was unwanted due to impact on startup time. As such, new versions have the default initial delay set to 0. To restore old behavior, please set initial-delay to 5.</p>
<h2>DHCPv6 LEASE SELECTION</h2>
<p>In the DHCPv6 protocol the client will wait a small amount of time to allow ADVERTISE messages from multiple servers to arrive. It will then need to choose from all of the messages that may have arrived before proceeding to making a request of the selected server. </p>
<p> The first selection criteria is the set of options and addresses in the message. Messages that don&#8217;t include an option specified as required will be given a score of 0 and not used. If the <i>-R</i> option is given on the command line then messages that don&#8217;t include the correct number of bindings (IA-NA, IA-TA or IA-PD) will be discarded. </p>
<p> The next criteria is the preference value from the message. With the highest preference value being used even if leases with better addresses or options are available. </p>
<p> Finally the lease is scored and the lease with the highest score is selected. A lease&#8217;s score is based on the number of bindings, number of addresses and number of options it contains: </p>
<pre> bindings * X + addresses * Y + options</pre>
<p>By default X = 10000 and Y = 100, this will cause the client to select a lease with more bindings over a lease with less bindings but more addresses. The weightings were changed as part of implementing RFC 7550. Previously they were X = 50 and Y = 100 meaning more addresses were preferred over more bindings. If you wish to continue using the old style you may do so by editing the file includes/site.h and uncommenting the define for USE_ORIGINAL_CLIENT_LEASE_WEIGHTS.</p>
<h2>Lease Requirements And Requests</h2>
<p>The DHCP protocol allows the client to request that the server send it specific information, and not send it other information that it is not prepared to accept. The protocol also allows the client to reject offers from servers if they don&#8217;t contain information the client needs, or if the information provided is not satisfactory. </p>
<p> There is a variety of data contained in offers that DHCP servers send to DHCP clients. The data that can be specifically requested is what are called <i>DHCP Options</i>. DHCP Options are defined in<br />
&nbsp;<code><a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5)</code>. </p>
<p> <i>The</i> <code>request</code> <i>statement</i> </p>
<p>&nbsp;<code>[&nbsp;also&nbsp;]&nbsp;request&nbsp;[&nbsp;[&nbsp;</code><i>option-space</i>&nbsp;.&nbsp;]&nbsp;<i>option</i>&nbsp;]&nbsp;[<code>,</code><i>&nbsp;&#8230;&nbsp;]</i><code>;</code> </p>
<p> The request statement causes the client to request that any server responding to the client send the client its values for the specified options. Only the option names should be specified in the request statement &#8211; not option parameters. By default, the DHCPv4 client requests the subnet-mask, broadcast-address, time-offset, routers, domain-name, domain-name-servers and host-name options while the DHCPv6 client requests the dhcp6 name-servers and domain-search options. Note that if you enter a &#8216;request&#8217; statement, you over-ride these defaults and these options will not be requested. </p>
<p> In some cases, it may be desirable to send no parameter request list at all. To do this, simply write the request statement but specify no parameters: </p>
<pre> request;</pre>
<p>In most cases, it is desirable to simply add one option to the request list which is of interest to the client in question. In this case, it is best to &#8216;also request&#8217; the additional options: </p>
<pre> also request domain-search, dhcp6.sip-servers-addresses;</pre>
<p><i>The</i> <code>require</code> <i>statement</i> </p>
<p>&nbsp;<code>[&nbsp;also&nbsp;]&nbsp;require&nbsp;[&nbsp;[&nbsp;</code><i>option-space</i>&nbsp;.&nbsp;]&nbsp;<i>option</i>&nbsp;]&nbsp;[<code>,</code><i>&nbsp;&#8230;&nbsp;]</i><code>;</code> </p>
<p> The require statement lists options that must be sent in order for an offer to be accepted. Offers that do not contain all the listed options will be ignored. There is no default require list. </p>
<pre> require name-servers;
 interface eth0 {
 also require domain-search;
 }</pre>
<p><i>The</i> <code>send</code> <i>statement</i> </p>
<p>&nbsp;<code>send&nbsp;[&nbsp;</code><i>option declaration</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> The send statement causes the client to send the specified option to the server with the specified value. This is a full option declaration as described in <code><a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5)</code>. Options that are always sent in the DHCP protocol should not be specified here, except that the client can specify a requested <code>dhcp-lease-time</code> option other than the default requested lease time, which is two hours. The other obvious use for this statement is to send information to the server that will allow it to differentiate between this client and other clients or kinds of clients.</p>
<h2>Dynamic Dns</h2>
<p>The client now has some very limited support for doing DNS updates when a lease is acquired. This is prototypical, and probably doesn&#8217;t do what you want. It also only works if you happen to have control over your DNS server, which isn&#8217;t very likely. </p>
<p> Note that everything in this section is true whether you are using DHCPv4 or DHCPv6. The exact same syntax is used for both. </p>
<p> To make it work, you have to declare a key and zone as in the DHCP server (see <code><a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a></code>(5) for details). You also need to configure the <i>fqdn</i> option on the client, as follows: </p>
<pre> send fqdn.fqdn &quot;grosse.example.com.&quot;;
 send fqdn.encoded on;
 send fqdn.server-update off;
 also request fqdn, dhcp6.fqdn;</pre>
<p>The <i>fqdn.fqdn</i> option <code>MUST</code> be a fully-qualified domain name. You <code>MUST</code> define a zone statement for the zone to be updated. The <i>fqdn.encoded</i> option may need to be set to <i>on</i> or <i>off</i>, depending on the DHCP server you are using. </p>
<p> <i>The</i> <code>do-forward-updates</code> <i>statement</i> </p>
<p>&nbsp;<code>do-forward-updates&nbsp;[&nbsp;</code><i>flag</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> If you want to do DNS updates in the DHCP client script (see <code><a href="/docs/linux/man/8-dhclient-script/">dhclient-script</a>(8)</code>) rather than having the DHCP client do the update directly (for example, if you want to use SIG(0) authentication, which is not supported directly by the DHCP client, you can instruct the client not to do the update using the <code>do-forward-updates</code> statement. <i>Flag</i> should be <code>true</code> if you want the DHCP client to do the update, and <code>false</code> if you don&#8217;t want the DHCP client to do the update. By default, the DHCP client will do the DNS update.</p>
<h2>Option Modifiers</h2>
<p>In some cases, a client may receive option data from the server which is not really appropriate for that client, or may not receive information that it needs, and for which a useful default value exists. It may also receive information which is useful, but which needs to be supplemented with local information. To handle these needs, several option modifiers are available. </p>
<p> <i>The</i> <code>default</code> <i>statement</i> </p>
<p>&nbsp;<code>default&nbsp;[&nbsp;</code><i>option declaration</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> If for some option the client should use the value supplied by the server, but needs to use some default value if no value was supplied by the server, these values can be defined in the <code>default</code> statement. </p>
<p> <i>The</i> <code>supersede</code> <i>statement</i> </p>
<p>&nbsp;<code>supersede&nbsp;[&nbsp;</code><i>option declaration</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> If for some option the client should always use a locally-configured value or values rather than whatever is supplied by the server, these values can be defined in the <code>supersede</code> statement. </p>
<p> <i>The</i> <code>prepend</code> <i>statement</i> </p>
<p>&nbsp;<code>prepend&nbsp;[&nbsp;</code><i>option declaration</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> If for some set of options the client should use a value you supply, and then use the values supplied by the server, if any, these values can be defined in the <code>prepend</code> statement. The <code>prepend</code> statement can only be used for options which allow more than one value to be given. This restriction is not enforced &#8211; if you ignore it, the behaviour will be unpredictable. </p>
<p> <i>The</i> <code>append</code> <i>statement</i> </p>
<p>&nbsp;<code>append&nbsp;[&nbsp;</code><i>option declaration</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> If for some set of options the client should first use the values supplied by the server, if any, and then use values you supply, these values can be defined in the <code>append</code> statement. The <code>append</code> statement can only be used for options which allow more than one value to be given. This restriction is not enforced &#8211; if you ignore it, the behaviour will be unpredictable.</p>
<h2>Lease Declarations</h2>
<p><i>The</i> <code>lease</code> <i>declaration</i> </p>
<p>&nbsp;<code>lease&nbsp;{</code>&nbsp;<i>lease-declaration</i>&nbsp;[&nbsp;&#8230;&nbsp;<i>lease-declaration&nbsp;]&nbsp;</i><code>}</code> </p>
<p> The DHCP client may decide after some period of time (see <code>PROTOCOL TIMING</code>) that it is not going to succeed in contacting a server. At that time, it consults its own database of old leases and tests each one that has not yet timed out by pinging the listed router for that lease to see if that lease could work. It is possible to define one or more <i>fixed</i> leases in the client configuration file for networks where there is no DHCP or BOOTP service, so that the client can still automatically configure its address. This is done with the <code>lease</code> statement. </p>
<p> NOTE: the lease statement is also used in the dhclient.leases file in order to record leases that have been received from DHCP servers. Some of the syntax for leases as described below is only needed in the dhclient.leases file. Such syntax is documented here for completeness. </p>
<p> A lease statement consists of the lease keyword, followed by a left curly brace, followed by one or more lease declaration statements, followed by a right curly brace. The following lease declarations are possible: </p>
<p>&nbsp;<code>bootp;</code> </p>
<p> The <code>bootp</code> statement is used to indicate that the lease was acquired using the BOOTP protocol rather than the DHCP protocol. It is never necessary to specify this in the client configuration file. The client uses this syntax in its lease database file. </p>
<p>&nbsp;<code>interface</code>&nbsp;<code>&quot;</code><i>string</i><code>&quot;;</code> </p>
<p> The <code>interface</code> lease statement is used to indicate the interface on which the lease is valid. If set, this lease will only be tried on a particular interface. When the client receives a lease from a server, it always records the interface number on which it received that lease. If predefined leases are specified in the dhclient.conf file, the interface should also be specified, although this is not required. </p>
<p>&nbsp;<code>fixed-address</code>&nbsp;<i>ip-address</i><code>;</code> </p>
<p> The <code>fixed-address</code> statement is used to set the ip address of a particular lease. This is required for all lease statements. The IP address must be specified as a dotted quad (e.g., 12.34.56.78). </p>
<p>&nbsp;<code>filename&nbsp;&quot;</code><i>string</i><code>&quot;;</code> </p>
<p> The <code>filename</code> statement specifies the name of the boot filename to use. This is not used by the standard client configuration script, but is included for completeness. </p>
<p>&nbsp;<code>server-name&nbsp;&quot;</code><i>string</i><code>&quot;;</code> </p>
<p> The <code>server-name</code> statement specifies the name of the boot server name to use. This is also not used by the standard client configuration script. </p>
<p>&nbsp;<code>option</code>&nbsp;<i>option-declaration</i><code>;</code> </p>
<p> The <code>option</code> statement is used to specify the value of an option supplied by the server, or, in the case of predefined leases declared in dhclient.conf, the value that the user wishes the client configuration script to use if the predefined lease is used. </p>
<p>&nbsp;<code>script&nbsp;&quot;</code><i>script-name</i><code>&quot;;</code> </p>
<p> The <code>script</code> statement is used to specify the pathname of the dhcp client configuration script. This script is used by the dhcp client to set each interface&#8217;s initial configuration prior to requesting an address, to test the address once it has been offered, and to set the interface&#8217;s final configuration once a lease has been acquired. If no lease is acquired, the script is used to test predefined leases, if any, and also called once if no valid lease can be identified. For more information, see <code><a href="/docs/linux/man/8-dhclient-script/">dhclient-script</a>(8).</code> </p>
<p>&nbsp;<code>vendor option space&nbsp;&quot;</code><i>name</i><code>&quot;;</code> </p>
<p> The <code>vendor option space</code> statement is used to specify which option space should be used for decoding the vendor-encapsulate-options option if one is received. The <i>dhcp-vendor-identifier</i> can be used to request a specific class of vendor options from the server. See <code><a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5)</code> for details. </p>
<p>&nbsp;<code>medium&nbsp;&quot;</code><i>media setup</i><code>&quot;;</code> </p>
<p> The <code>medium</code> statement can be used on systems where network interfaces cannot automatically determine the type of network to which they are connected. The media setup string is a system-dependent parameter which is passed to the dhcp client configuration script when initializing the interface. On Unix and Unix-like systems, the argument is passed on the ifconfig command line when configuring the interface. </p>
<p> The dhcp client automatically declares this parameter if it uses a media type (see the <code>media</code> statement) when configuring the interface in order to obtain a lease. This statement should be used in predefined leases only if the network interface requires media type configuration. </p>
<p>&nbsp;<code>renew</code>&nbsp;<i>date</i><code>;</code> </p>
<p>&nbsp;<code>rebind</code>&nbsp;<i>date</i><code>;</code> </p>
<p>&nbsp;<code>expire</code>&nbsp;<i>date</i><code>;</code> </p>
<p> The <code>renew</code> statement defines the time at which the dhcp client should begin trying to contact its server to renew a lease that it is using. The <code>rebind</code> statement defines the time at which the dhcp client should begin to try to contact <i>any</i> dhcp server in order to renew its lease. The <code>expire</code> statement defines the time at which the dhcp client must stop using a lease if it has not been able to contact a server in order to renew it. </p>
<p> These declarations are automatically set in leases acquired by the DHCP client, but must also be configured in predefined leases &#8211; a predefined lease whose expiry time has passed will not be used by the DHCP client. </p>
<p> Dates are specified in one of two ways. The software will output times in these two formats depending on if the <code>db-time-format</code> configuration parameter has been set to <i>default</i> or <i>local</i>. </p>
<p> If it is set to <i>default</i>, then <i>date</i> values appear as follows: </p>
<p>&nbsp;<i>&lt;weekday&gt;&nbsp;&lt;year&gt;</i><code>/</code><i>&lt;month&gt;</i><code>/</code><i>&lt;day&gt; &lt;hour&gt;</i><code>:</code><i>&lt;minute&gt;</i><code>:</code><i>&lt;second&gt;</i> </p>
<p> The weekday is present to make it easy for a human to tell when a lease expires &#8211; it&#8217;s specified as a number from zero to six, with zero being Sunday. When declaring a predefined lease, it can always be specified as zero. The year is specified with the century, so it should generally be four digits except for really long leases. The month is specified as a number starting with 1 for January. The day of the month is likewise specified starting with 1. The hour is a number between 0 and 23, the minute a number between 0 and 59, and the second also a number between 0 and 59. </p>
<p> If the <code>db-time-format</code> configuration was set to <i>local</i>, then the <i>date</i> values appear as follows: </p>
<p>&nbsp;<code>epoch</code>&nbsp;<i>&lt;seconds-since-epoch&gt;</i><code>;&nbsp;#</code>&nbsp;<i>&lt;day-name&gt;&nbsp;&lt;month-name&gt; &lt;day-number&gt; &lt;hours&gt;</i><code>:</code><i>&lt;minutes&gt;</i><code>:</code><i>&lt;seconds&gt; &lt;year&gt;</i> </p>
<p> The <i>seconds-since-epoch</i> is as according to the system&#8217;s local clock (often referred to as &quot;unix time&quot;). The <code>#</code> symbol supplies a comment that describes what actual time this is as according to the system&#8217;s configured timezone, at the time the value was written. It is provided only for human inspection, the epoch time is the only recommended value for machine inspection. </p>
<p> Note that when defining a static lease, one may use either time format one wishes, and need not include the comment or values after it. </p>
<p> If the time is infinite in duration, then the <i>date</i> is <code>never</code> instead of an actual date.</p>
<h2>Alias Declarations</h2>
<p>&nbsp;<code>alias&nbsp;{&nbsp;</code><i>&nbsp;declarations &#8230;&nbsp;</i><code>}</code> </p>
<p> Some DHCP clients running TCP/IP roaming protocols may require that in addition to the lease they may acquire via DHCP, their interface also be configured with a predefined IP alias so that they can have a permanent IP address even while roaming. The Internet Systems Consortium DHCP client doesn&#8217;t support roaming with fixed addresses directly, but in order to facilitate such experimentation, the dhcp client can be set up to configure an IP alias using the <code>alias</code> declaration. </p>
<p> The alias declaration resembles a lease declaration, except that options other than the subnet-mask option are ignored by the standard client configuration script, and expiry times are ignored. A typical alias declaration includes an interface declaration, a fixed-address declaration for the IP alias address, and a subnet-mask option declaration. A medium statement should never be included in an alias declaration.</p>
<h2>Other Declarations</h2>
<p>&nbsp;<code>db-time-format</code>&nbsp;[&nbsp;<i>default</i>&nbsp;|&nbsp;<i>local</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> The <code>db-time-format</code> option determines which of two output methods are used for printing times in leases files. The <i>default</i> format provides day-and-time in UTC, whereas <i>local</i> uses a seconds-since-epoch to store the time value, and helpfully places a local timezone time in a comment on the same line. The formats are described in detail in this manpage, within the LEASE DECLARATIONS section. </p>
<p> The <i>lease-id-format</i> parameter</p>
<dl>
<dd><code>lease-id-format </code><i>format</i><code>;</code> </p>
<p> The <i>format</i> parameter must be either <code>octal</code> or <code>hex</code>. This parameter governs the format used to write certain values to lease files. With the default format, octal, values are written as quoted strings in which non-printable characters are represented as octal escapes &#8211; a backslash character followed by three octal digits. When the hex format is specified, values are written as an unquoted series of hexadecimal digit pairs, separated by colons. </p>
<p> Currently, the values written out based on lease-id-format are the default-duid and the IAID value (DHCPv6 only). The client automatically reads the values in either format. Note that when the format is octal, rather than as an octal string, IAID is output as hex if it contains no printable characters or as a string if contains only printable characters. This is done to maintain backward compatibility. </p>
<p>&nbsp;<code>reject&nbsp;</code><i>cidr-ip-address</i>&nbsp;[<code>,</code>&nbsp;<i>&#8230;</i><code>&nbsp;</code><i>cidr-ip-address</i>&nbsp;]&nbsp;<code>;</code> </p>
<p> The <code>reject</code> statement causes the DHCP client to reject offers from servers whose server identifier matches any of the specified hosts or subnets. This can be used to avoid being configured by rogue or misconfigured dhcp servers, although it should be a last resort &#8211; better to track down the bad DHCP server and fix it. </p>
<p> The <i>cidr-ip-address</i> configuration type is of the form <i>ip-address</i>[<code>/</code><i>prefixlen</i>], where <i>ip-address</i> is a dotted quad IP address, and prefixlen is the CIDR prefix length of the subnet, counting the number of significant bits in the netmask starting from the leftmost end. Example configuration syntax: </p>
<p> <i>reject</i> 192.168.0.0<code>/</code>16<code>,</code> 10.0.0.5<code>;</code> </p>
<p> The above example would cause offers from any server identifier in the entire RFC 1918 &quot;Class C&quot; network 192.168.0.0/16, or the specific single address 10.0.0.5, to be rejected. </p>
<p>&nbsp;<code>interface&nbsp;&quot;</code><i>name</i><code>&quot;&nbsp;{&nbsp;</code><i>declarations &#8230;&nbsp;</i><code>&nbsp;} </p>
<p> A client with more than one network interface may require different behaviour depending on which interface is being configured. All timing parameters and declarations other than lease and alias declarations can be enclosed in an interface declaration, and those parameters will then be used only for the interface that matches the specified name. Interfaces for which there is no interface declaration will use the parameters declared outside of any interface declaration, or the default settings. </p>
<p> Note well:</code> ISC dhclient only maintains one list of interfaces, which is either determined at startup from command line arguments, or otherwise is autodetected. If you supplied the list of interfaces on the command line, this configuration clause will add the named interface to the list in such a way that will cause it to be configured by DHCP. Which may not be the result you had intended. This is an undesirable side effect that will be addressed in a future release. </p>
<p>&nbsp;<code>pseudo&nbsp;&quot;</code><i>name</i>&quot;&nbsp;&quot;<i>real-name</i><code>&quot;&nbsp;{&nbsp;</code><i>declarations &#8230;&nbsp;</i><code>&nbsp;} </p>
<p> Under some circumstances it can be useful to declare a pseudo-interface and have the DHCP client acquire a configuration for that interface. Each interface that the DHCP client is supporting normally has a DHCP client state machine running on it to acquire and maintain its lease. A pseudo-interface is just another state machine running on the interface named </code><i>real-name</i>, with its own lease and its own state. If you use this feature, you must provide a client identifier for both the pseudo-interface and the actual interface, and the two identifiers must be different. You must also provide a separate client script for the pseudo-interface to do what you want with the IP address. For example: </p>
<pre> interface &quot;ep0&quot; {
 send dhcp-client-identifier &quot;my-client-ep0&quot;;
 }
 pseudo &quot;secondary&quot; &quot;ep0&quot; {
 send dhcp-client-identifier &quot;my-client-ep0-secondary&quot;;
 script &quot;/etc/dhclient-secondary&quot;;
 }</pre>
<p>The client script for the pseudo-interface should not configure the interface up or down &#8211; essentially, all it needs to handle are the states where a lease has been acquired or renewed, and the states where a lease has expired. See <code><a href="/docs/linux/man/8-dhclient-script/">dhclient-script</a>(8)</code> for more information. </p>
<p>&nbsp;<code>media&nbsp;&quot;</code><i>media setup</i><code>&quot;</code><i>&nbsp;[&nbsp;</i><code>,&nbsp;&quot;</code><i>media setup</i><code>&quot;,&nbsp;</code><i>&#8230;&nbsp;]</i><code>;</code> </p>
<p> The <code>media</code> statement defines one or more media configuration parameters which may be tried while attempting to acquire an IP address. The dhcp client will cycle through each media setup string on the list, configuring the interface using that setup and attempting to boot, and then trying the next one. This can be used for network interfaces which aren&#8217;t capable of sensing the media type unaided &#8211; whichever media type succeeds in getting a request to the server and hearing the reply is probably right (no guarantees). </p>
<p> The media setup is only used for the initial phase of address acquisition (the DHCPDISCOVER and DHCPOFFER packets). Once an address has been acquired, the dhcp client will record it in its lease database and will record the media type used to acquire the address. Whenever the client tries to renew the lease, it will use that same media type. The lease must expire before the client will go back to cycling through media types. </p>
<p>&nbsp;<code>hardware</code>&nbsp;<i>link-type mac-address</i><code>;</code> </p>
<p> The <code>hardware</code> statement defines the hardware MAC address to use for this interface, for DHCP servers or relays to direct their replies. dhclient will determine the interface&#8217;s MAC address automatically, so use of this parameter is not recommended. The <i>link-type</i> corresponds to the interface&#8217;s link layer type (example: &#8216;ethernet&#8217;), while the <i>mac-address</i> is a string of colon-separated hexadecimal values for octets. </p>
<p>&nbsp;<code>anycast-mac</code>&nbsp;<i>link-type mac-address</i><code>;</code> </p>
<p> The <code>anycast-mac</code> statement over-rides the all-ones broadcast MAC address dhclient will use when it is transmitting packets to the all-ones limited broadcast IPv4 address. This configuration parameter is useful to reduce the number of broadcast packets transmitted by DHCP clients, but is only useful if you know the DHCP service(s) anycast MAC address prior to configuring your client. The <i>link-type</i> and <i>mac-address</i> parameters are configured in a similar manner to the <code>hardware</code> statement. </p>
</dl>
<h2>Sample</h2>
<p>The following configuration file was used on a laptop running NetBSD 1.3, though the domains have been modified. The laptop has an IP alias of 192.5.5.213, and has one interface, ep0 (a 3com 3C589C). Booting intervals have been shortened somewhat from the default, because the client is known to spend most of its time on networks with little DHCP activity. The laptop does roam to multiple networks. </p>
<pre>timeout 300;
retry 60;
reboot 10;
select-timeout 5;
initial-interval 2;
reject 192.33.137.209;
interface &quot;ep0&quot; {
 send host-name &quot;andare.example.com&quot;;
 hardware ethernet 00:a0:24:ab:fb:9c;
 send dhcp-client-identifier 1:0:a0:24:ab:fb:9c;
 send dhcp-lease-time 3600;
 supersede domain-search &quot;example.com&quot;, &quot;rc.isc.org&quot;, &quot;home.isc.org&quot;;
 prepend domain-name-servers 127.0.0.1;
 request subnet-mask, broadcast-address, time-offset, routers,
 domain-name, domain-name-servers, host-name;
 require subnet-mask, domain-name-servers;
 script &quot;/sbin/dhclient-script&quot;;
 media &quot;media 10baseT/UTP&quot;, &quot;media 10base2/BNC&quot;;
}
alias {
 interface &quot;ep0&quot;;
 fixed-address 192.5.5.213;
 option subnet-mask 255.255.255.255;
}</pre>
<p>This is a very complicated dhclient.conf file &#8211; in general, yours should be much simpler. In many cases, it&#8217;s sufficient to just create an empty dhclient.conf file &#8211; the defaults are usually fine.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5), <a href="/docs/linux/man/5-dhcp-eval/">dhcp-eval</a>(5), <a href="/docs/linux/man/5-dhclient-leases/">dhclient.leases</a>(5), <a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5), RFC2132, RFC2131.</p>
<h2>Author</h2>
<p><code><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8)</code> Information about Internet Systems Consortium can be found at <code><a rel="nofollow" href="https://www.isc.org.">https://www.isc.org.</a></code></p>
