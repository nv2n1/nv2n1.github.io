---
title: "iscsiadm(8)"
name: "iscsiadm"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iscsiadm/"
description: "iscsiadm – open-iscsi administration utility"
---

<p>iscsiadm &#8211; open-iscsi administration utility</p>
<h2>Synopsis</h2>
<p><code>iscsiadm</code> <code>-m discoverydb</code> [<code>-hV</code>] [<code>-d</code> <i>debug_level</i>] [<code>-P</code> <i>printlevel</i>] [<code>-I&nbsp;<wbr></code><i>iface&nbsp;<wbr></i><code>-t&nbsp;<wbr></code><i>type&nbsp;<wbr></i><code>-p&nbsp;<wbr></code><i>ip:port</i> [<code>-lD</code>] ] | [ [<code>-p</code> <i>ip:port</i> <code>-t</code> <i>type</i>] [<code>-o</code> <i>operation</i>] [<code>-n</code> <i>name</i>] [<code>-v</code> <i>value</i>] [<code>-lD</code>] ] <code>iscsiadm</code> <code>-m discovery</code> [<code>-hV</code>] [<code>-d</code> <i>debug_level</i>] [<code>-P</code> <i>printlevel</i>] [<code>-I&nbsp;<wbr></code><i>iface&nbsp;<wbr></i><code>-t&nbsp;<wbr></code><i>type&nbsp;<wbr></i><code>-p&nbsp;<wbr></code><i>ip:port</i> [<code>-l</code>] ] | [ [<code>-p</code> <i>ip:port</i>] [<code>-l</code>|<code>-D</code>] ] <code>iscsiadm</code> <code>-m node</code> [<code>-hV</code>] [<code>-d</code> <i>debug_level</i>] [<code>-P</code> <i>printlevel</i>] [<code>-L</code> <i>all,manual,automatic</i>] [<code>-U</code> <i>all,manual,automatic</i>] [<code>-S</code>] [ [<code>-T</code> <i>targetname&nbsp;<wbr></i><code>-p&nbsp;<wbr></code><i>ip:port&nbsp;<wbr></i><code>-I&nbsp;<wbr></code><i>iface</i> ] [<code>-l</code>|<code>-u</code>|<code>-R</code>|<code>-s</code>] ] [ [<code>-o</code> <i>operation</i>] [<code>-n</code> <i>name</i>] [<code>-v</code> <i>value</i>] [<code>-p</code> <i>ip:port</i>] ] <code>iscsiadm</code> <code>-m session</code> [<code>-hV</code>] [<code>-d</code> <i>debug_level</i>] [<code>-P</code> <i>printlevel</i>] [ <code>-r</code> <i>sessionid</i>|<i>sysfsdir</i> [<code>-R</code>] [<code>-u</code>|<code>-s</code>|<code>-o</code> <i>new</i>] ] <code>iscsiadm</code> <code>-m iface</code> [<code>-hV</code>] [<code>-d</code> <i>debug_level</i>] [<code>-P</code> <i>printlevel</i>] [ <code>-I&nbsp;<wbr></code><i>ifacename</i> | <code>-H&nbsp;<wbr></code><i>hostno|MAC</i> ] [ [<code>-o</code> <i>operation</i>] [<code>-n</code> <i>name</i>] [<code>-v</code> <i>value</i>] ] [ <code>-C&nbsp;<wbr></code><i>ping</i> [<code>-a</code> <i>ip</i>] [<code>-b</code> <i>packetsize</i>] [<code>-c</code> <i>count</i>] [<code>-i</code> <i>interval</i>] ] <code>iscsiadm</code> <code>-m fw</code> [<code>-d</code> <i>debug_level</i>] [<code>-l</code>] <code>iscsiadm</code> <code>-m host</code> [<code>-P</code> <i>printlevel</i>] [<code>-H</code> <i>hostno|MAC</i>] [ [&nbsp;<wbr><code>-C</code> <i>chap</i> [<code>-x</code> <i>chap_tbl_idx</i>] ] | [&nbsp;<wbr><code>-C</code> <i>flashnode</i> [<code>-A</code> <i>portal_type</i>] [<code>-x</code> <i>flashnode_idx</i>] ] | [&nbsp;<wbr><code>-C</code> <i>stats</i>&nbsp;<wbr>] ] [ [<code>-o</code> <i>operation</i>] [<code>-n</code> <i>name</i>] [<code>-v</code> <i>value</i>] ] <code>iscsiadm</code> <code>-k priority</code> </p>
<h2>Description</h2>
<p>The iscsiadm utility is a command-line tool allowing discovery and login to iSCSI targets, as well as access and management of the open-iscsi database. Open-iscsi does not use the term node as defined by the iSCSI RFC, where a node is a single iSCSI initiator or target. Open-iscsi uses the term node to refer to a portal on a target. For session mode, a session id (sid) is used. The sid of a session can be found by running iscsiadm -m session -P 1. The session id and sysfs path are not currently persistent and is partially determined by when the session is setup. Note that many of the node and discovery operations require that the iSCSI daemon (iscsid) be running. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;ip=</code><i>ipaddr</i></p>
<dd><i>ipaddr</i> can be IPv4 or IPv6. </p>
<p> This option is only valid for ping submode. </p>
<dt><code>-A</code>, <code>&#8211;portal_type=</code><i>[ipv4|ipv6]</i></p>
<dd>Specify the portal type for the new flash node entry to be created.</p>
<dd>This option is only valid for flashnode submode of host mode and only with <i>new</i> operation. </p>
<dt><code>-b</code>, <code>&#8211;packetsize=</code><i>packetsize</i></p>
<dd>Specify the ping <i>packetsize</i>. </p>
<p> This option is only valid for ping submode. </p>
<dt><code>-c</code>, <code>&#8211;count=</code><i>count</i></p>
<dd><i>count</i> specify number of ping iterations. </p>
<p> This option is only valid for ping submode. </p>
<dt><code>-C</code>, <code>&#8211;submode=</code><i>op</i></p>
<dd>Specify the submode for mode. op must be name of submode. </p>
<p> Currently iscsiadm support ping as submode for iface. For example, </p>
<p> iscsiadm -m iface -I ifacename -C ping -a ipaddr -b packetsize -c count -i interval </p>
<p> For host, it supports chap , flashnode and stats as submodes. For example, </p>
<p> iscsiadm -m host -H hostno -C chap -x chap_tbl_idx -o operation </p>
<p> iscsiadm -m host -H hostno -C flashnode -x flashnode_idx -o operation </p>
<p> iscsiadm -m host -H hostno -C stats </p>
<dt><code>-d</code>, <code>&#8211;debug=</code><i>debug_level</i></p>
<dd>print debugging information. Valid values for debug_level are 0 to 8. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>display help text and exit </p>
<dt><code>-H</code>, <code>&#8211;host=</code><i>[hostno|MAC]</i></p>
<dd>The host argument specifies the SCSI host to use for the operation. It can be the scsi host number assigned to the host by the kernel&#8217;s scsi layer, or the MAC address of a scsi host. </p>
<dt><code>-i</code>, <code>&#8211;interval=</code><i>interval</i></p>
<dd><i>interval</i> specify delay between two ping iterations. </p>
<p> This option is only valid for ping submode. </p>
<dt><code>-I</code>, <code>&#8211;interface=</code><i>[iface]</i></p>
<dd>The interface argument specifies the iSCSI interface to use for the operation. iSCSI interfaces (iface) are defined in /var/lib/iscsi/ifaces. For hardware iSCSI (qla4xxx) the iface config must have the hardware address (iface.hwaddress = port&#8217;s MAC address) and the driver/transport_name (iface.transport_name). The iface&#8217;s name is then the filename of the iface config. For software iSCSI, the iface config must have either the hardware address (iface.hwaddress), or the network layer&#8217;s interface name (iface.net_ifacename), and it must have the driver/transport_name </p>
<p> The available drivers/iscsi_transports are tcp (software iSCSI over TCP/IP), iser (software iSCSI over InfiniBand), or qla4xxx (Qlogic 4XXXX HBAs). The hwaddress is the MAC address or for software iSCSI it may be the special value &quot;default&quot; which directs the initiator to not bind the session to a specific hardware resource and instead allow the network or InfiniBand layer to decide what to do. There is no need to create an iface config with the default behavior. If you do not specify an iface, then the default behavior is used. </p>
<p> As mentioned above there is a special iface name default. There are three others &#8212; cxgb3i, bnx2i and iser, which does not bind the session to a specific card, but will bind the session to the cxgb3i, bnx2i or iser transport. These are experimental and the use is not supported as a stable interface yet. </p>
<p> In discovery mode multiple interfaces can be specified by passing in multiple -I/&#8211;interface instances. For example, </p>
<p> &quot;iscsiadm -m discoverydb -t st -p ip:port -I iface0 -I iface2 &#8211;discover&quot; </p>
<p> Will direct iscsiadm to setup the node db to create records which will create sessions through the two intefaces passed in. </p>
<p> In node mode, only a single interface is supported in each call to iscsiadm.</p>
<dd>This option is valid for discovery, node and iface mode. </p>
<dt><code>-k</code>, <code>&#8211;killiscsid=</code><i>[priority]</i></p>
<dd>Currently priority must be zero. This will immediately stop all iscsid operations and shutdown iscsid. It does not logout any sessions. Running this command is the same as doing &quot;killall iscsid&quot;. Neither should normally be used, because if iscsid is doing error recovery or if there is an error while iscsid is not running, the system may not be able to recover. This command and iscsid&#8217;s SIGTERM handling are experimental. </p>
<dt><code>-D</code>, <code>&#8211;discover</code></p>
<dd>Discover targets using the discovery record with the <i>recid</i> matching the the discovery type and portal passed in. If there is no matching record, it will be created using the iscsid.conf discovery settings. This must be passed in <i>discoverydb</i> mode to instruct iscsiadm to perform discovery.</p>
<dd>This option is only valid for SendTargets discovery mode. </p>
<dt><code>-l</code>, <code>&#8211;login</code></p>
<dd>For node and fw mode, login to a specified record. For discovery mode, login to all discovered targets.</p>
<dd>This option is only valid for discovery and node modes. </p>
<dt><code>-L</code>, <code>&#8211;loginall=</code><i>[all|manual|automatic]</i></p>
<dd>For node mode, login all sessions with the node or conn startup values passed in or all running session, except ones marked onboot, if all is passed in.</p>
<dd>This option is only valid for node mode (it is valid but not functional for session mode). </p>
<dt><code>-m, &#8211;mode </code><i>op</i></p>
<dd>specify the mode. <i>op</i> must be one of <i>discovery</i>, <i>discoverydb</i>, <i>node</i>, <i>fw</i>, <i>host</i> <i>iface</i> or <i>session</i>.</p>
<dd>If no other options are specified: for <i>discovery</i>, <i>discoverydb</i> and <i>node</i>, all of their respective records are displayed; for <i>session</i>, all active sessions and connections are displayed; for <i>fw</i>, all boot firmware values are displayed; for <i>host</i>, all iSCSI hosts are displayed; and for <i>iface</i>, all ifaces setup in /var/lib/iscsi/ifaces are displayed. </p>
<dt><code>-n</code>, <code>&#8211;name=</code><i>name</i></p>
<dd>In node mode, specify a field <i>name</i> in a record. In flashnode submode of host mode, specify name of the flash node parameter. </p>
<p> For use with the <i>update</i> operator.</p>
<dd>
<dt><code>-o</code>, <code>&#8211;op=</code><i>op</i></p>
<dd>Specifies a database operator <i>op</i>. <i>op</i> must be one of <i>new</i>, <i>delete</i>, <i>update</i>, <i>show</i> or <i>nonpersistent</i>.</p>
<dd>For iface mode, <i>apply</i> and <i>applyall</i> are also applicable.</p>
<dd>For flashnode submode of host mode, <i>login</i> and <i>logout</i> are also applicable.</p>
<dd>This option is valid for all modes except fw. Delete should not be used on a running session. If it is iscsiadm will stop the session and then delete the record.</p>
<dd><i>new</i> creates a new database record for a given object. In node mode, the <i>recid</i> is the target name and portal (IP:port). In iface mode, the <i>recid</i> is the iface name. In discovery mode, the <i>recid</i> is the portal and discovery type.</p>
<dd>In session mode, the <i>new</i> operation logs in a new session using the same node database and iface information as the specified session.</p>
<dd>In discovery mode, if the <i>recid</i> and new operation is passed in, but the <i>&#8211;discover</i> argument is not, then iscsiadm will only create a discovery record (it will not perform discovery). If the <i>&#8211;discover</i> argument is passed in with the portal and discovery type, then iscsiadm will create the discovery record if needed, and it will create records for portals returned by the target that do not yet have a node DB record.</p>
<dd><i>delete</i> deletes a specified <i>recid</i>. In discovery mode, if iscsiadm is performing discovery it will delete records for portals that are no longer returned.</p>
<dd><i>update</i> will update the <i>recid</i> with <i>name</i> to the specified <i>value</i>. In discovery mode, if iscsiadm is performing discovery the <i>recid</i>, <i>name</i> and <i>value</i> arguments are not needed. The update operation will operate on the portals returned by the target, and will update the node records with info from the config file and command line.</p>
<dd><i>show</i> is the default behaviour for node, discovery and iface mode. It is also used when there are no commands passed into session mode and a running sid is passed in. <i>name</i> and <i>value</i> are currently ignored when used with <i>show</i>.</p>
<dd><i>nonpersistent</i> instructs iscsiadm to not manipulate the node DB. </p>
<dd><i>apply</i> will cause the network settings to take effect on the specified iface. </p>
<dd><i>applyall</i> will cause the network settings to take effect on all the ifaces whose MAC address or host number matches that of the specific host. </p>
<dd><i>login</i> will log into the specified flash node entry. </p>
<dd><i>logout</i> does the logout from the given flash node entry. </p>
<dt><code>-p</code>, <code>&#8211;portal=</code><i>ip[:port]</i></p>
<dd>Use target portal with ip-address <i>ip</i> and <i>port</i>. If port is not passed in the default <i>port</i> value is 3260.</p>
<dd>IPv6 addresses can be specified as [ddd.ddd.ddd.ddd]:port or ddd.ddd.ddd.ddd.</p>
<dd>Hostnames can also be used for the ip argument. </p>
<dd>This option is only valid for discovery, or for node operations with the <i>new</i> operator.</p>
<dd>This should be used along with &#8211;target in node mode, to specify what the open-iscsi docs refer to as a node or node record. Note: open-iscsi&#8217;s use of the word node, does not match the iSCSI RFC&#8217;s iSCSI Node term. </p>
<dt><code>-P</code>, <code>&#8211;print=</code><i>printlevel</i></p>
<dd>If in node mode print nodes in tree format. If in session mode print sessions in tree format. If in discovery mode print the nodes in tree format. </p>
<dt><code>-T</code>, <code>&#8211;targetname=</code><i>targetname</i></p>
<dd>Use target <i>targetname</i>.</p>
<dd>This should be used along with &#8211;portal in node mode, to specify what the open-iscsi docs refer to as a node or node record. Note: open-iscsi&#8217;s use of the word node, does not match the iSCSI RFC&#8217;s iSCSI Node term. </p>
<dt><code>-r</code>, <code>&#8211;sid=</code><i>sid | sysfsdir</i></p>
<dd>Use session ID <i>sid</i>. The sid of a session can be found from running iscsiadm in session mode with the &#8211;info argument. </p>
<p> Instead of sid, a sysfs path containing the session can be used. For example using one of the following: /sys/devices/platform/hostH/sessionS/targetH:B:I/H:B:I:L, /sys/devices/platform/hostH/sessionS/targetH:B:I, or /sys/devices/platform/hostH/sessionS, for the sysfsdir argument would result in the session with sid S to be used.</p>
<dd><i>sid | sysfsdir</i> is only required for session mode. </p>
<dt><code>-R</code>, <code>&#8211;rescan</code></p>
<dd>In session mode, if sid is also passed in rescan the session. If no sid has been passed in rescan all running sessions. </p>
<p> In node mode, rescan a session running through the target, portal, iface tuple passed in. </p>
<dt><code>-s</code>, <code>&#8211;stats</code></p>
<dd>Display session statistics. This option when used with host mode, displays host statistics. </p>
<dt><code>-S</code>, <code>&#8211;show</code></p>
<dd>When displaying records, do not hide masked values, such as the CHAP secret (password).</p>
<dd>This option is only valid for node and session mode. </p>
<dt><code>-t</code>, <code>&#8211;type=</code><i>type</i></p>
<dd><i>type</i> must be <i>sendtargets</i> (or abbreviated as <i>st</i>), <i>slp</i>, <i>isns</i> or <i>fw</i>. Currently only sendtargets, fw, and iSNS is supported, see the DISCOVERY TYPES section.</p>
<dd>This option is only valid for discovery mode. </p>
<dt><code>-u</code>, <code>&#8211;logout</code></p>
<dd>logout for a specified record.</p>
<dd>This option is only valid for node and session mode. </p>
<dt><code>-U</code>, <code>&#8211;logoutall=</code><i>[all,manual,automatic]</i></p>
<dd>logout all sessions with the node or conn startup values passed in or all running session, except ones marked onboot, if all is passed in.</p>
<dd>This option is only valid for node mode (it is valid but not functional for session mode). </p>
<dt><code>-v</code>, <code>&#8211;value=</code><i>value</i></p>
<dd>Specify a <i>value</i> for use with the <i>update</i> operator.</p>
<dd>This option is only valid for node mode and flashnode submode of host mode. </p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>display version and exit </p>
<dt><code>-x</code>, <code>&#8211;index=</code><i>index</i></p>
<dd>Specify the <i>index</i> of the entity to operate on.</p>
<dd>This option is only valid for chap and flashnode submodes of host mode. </p>
</dl>
<h2>Discovery Types</h2>
<p>iSCSI defines 3 discovery types: SendTargets, SLP, and iSNS. </p>
<dl>
<dt><code>SendTargets</code></p>
<dd>A native iSCSI protocol which allows each iSCSI target to send a list of available targets to the initiator. </p>
<dt><code>SLP</code></p>
<dd>Optionally an iSCSI target can use the Service Location Protocol (SLP) to announce the available targets. The initiator can either implement SLP queries directly or can use a separate tool to acquire the information about available targets. </p>
<dt><code>iSNS</code></p>
<dd>iSNS (Internet Storage Name Service) records information about storage volumes within a larger network. To utilize iSNS, pass the address and optionally the port of the iSNS server to do discovery to. </p>
<dt><code>fw</code></p>
<dd>Several NICs and systems contain a mini iSCSI initiator which can be used for boot. To get the values used for boot the fw option can be used. Doing fw discovery, does not store persistent records in the node or discovery DB, because the values are stored in the system&#8217;s or NIC&#8217;s resource. </p>
<p> Performing fw discovery will print the portals, like with other discovery methods. To see other settings like CHAP values and initiator settings, like you would in node mode, run &quot;iscsiadm -m fw&quot;. </p>
<p> fw support in open-iscsi is experimental. The settings and iscsiadm syntax and output format may change. </p>
</dl>
<p> iscsiadm supports the <code>iSNS (isns)</code> or <code>SendTargets (st)</code> discovery type. An SLP implementation is under development.</p>
<h2>Exit Status</h2>
<p>On success 0 is returned. On error one of the return codes below will be returned. </p>
<p> Commands that operate on multiple objects (sessions, records, etc), iscsiadm/iscsistart will return the first error that is encountered. iscsiadm/iscsistart will attempt to execute the operation on the objects it can. If no objects are found ISCSI_ERR_NO_OBJS_FOUND is returned. </p>
<dl>
<dt><code>0</code></p>
<dd>ISCSI_SUCCESS &#8211; command executed successfully. </p>
<dt><code>1</code></p>
<dd>ISCSI_ERR &#8211; generic error code. </p>
<dt><code>2</code></p>
<dd>ISCSI_ERR_SESS_NOT_FOUND &#8211; session could not be found. </p>
<dt><code>3</code></p>
<dd>ISCSI_ERR_NOMEM &#8211; could not allocate resource for operation.</p>
<dt><code>4</code></p>
<dd>ISCSI_ERR_TRANS &#8211; connect problem caused operation to fail. </p>
<dt><code>5</code></p>
<dd>ISCSI_ERR_LOGIN &#8211; generic iSCSI login failure. </p>
<dt><code>6</code></p>
<dd>ISCSI_ERR_IDBM &#8211; error accessing/managing iSCSI DB. </p>
<dt><code>7</code></p>
<dd>ISCSI_ERR_INVAL &#8211; invalid argument. </p>
<dt><code>8</code></p>
<dd>ISCSI_ERR_TRANS_TIMEOUT &#8211; connection timer exired while trying to connect. </p>
<dt><code>9</code></p>
<dd>ISCSI_ERR_INTERNAL &#8211; generic internal iscsid/kernel failure. </p>
<dt><code>10</code></p>
<dd>ISCSI_ERR_LOGOUT &#8211; iSCSI logout failed. </p>
<dt><code>11</code></p>
<dd>ISCSI_ERR_PDU_TIMEOUT &#8211; iSCSI PDU timedout. </p>
<dt><code>12</code></p>
<dd>ISCSI_ERR_TRANS_NOT_FOUND &#8211; iSCSI transport module not loaded in kernel or iscsid. </p>
<dt><code>13</code></p>
<dd>ISCSI_ERR_ACCESS &#8211; did not have proper OS permissions to access iscsid or execute iscsiadm command. </p>
<dt><code>14</code></p>
<dd>ISCSI_ERR_TRANS_CAPS &#8211; transport module did not support operation. </p>
<dt><code>15</code></p>
<dd>ISCSI_ERR_SESS_EXISTS &#8211; session is logged in. </p>
<dt><code>16</code></p>
<dd>ISCSI_ERR_INVALID_MGMT_REQ &#8211; invalid IPC MGMT request. </p>
<dt><code>17</code></p>
<dd>ISCSI_ERR_ISNS_UNAVAILABLE &#8211; iSNS service is not supported. </p>
<dt><code>18</code></p>
<dd>ISCSI_ERR_ISCSID_COMM_ERR &#8211; a read/write to iscsid failed. </p>
<dt><code>19</code></p>
<dd>ISCSI_ERR_FATAL_LOGIN &#8211; fatal iSCSI login error. </p>
<dt><code>20</code></p>
<dd>ISCSI_ERR_ISCSID_NOTCONN &#8211; could not connect to iscsid. </p>
<dt><code>21</code></p>
<dd>ISCSI_ERR_NO_OBJS_FOUND &#8211; no records/targets/sessions/portals found to execute operation on. </p>
<dt><code>22</code></p>
<dd>ISCSI_ERR_SYSFS_LOOKUP &#8211; could not lookup object in sysfs. </p>
<dt><code>23</code></p>
<dd>ISCSI_ERR_HOST_NOT_FOUND &#8211; could not lookup host. </p>
<dt><code>24</code></p>
<dd>ISCSI_ERR_LOGIN_AUTH_FAILED &#8211; login failed due to authorization failure. </p>
<dt><code>25</code></p>
<dd>ISCSI_ERR_ISNS_QUERY &#8211; iSNS query failure. </p>
<dt><code>26</code></p>
<dd>ISCSI_ERR_ISNS_REG_FAILED &#8211; iSNS registration/deregistration failed. </p>
</dl>
<h2>Examples</h2>
<pre>Discover targets at a given IP address:
 iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.10 --discover
Login, must use a node record id found by the discovery:
 iscsiadm --mode node --targetname iqn.2001-05.com.doe:test --portal 192.168.1.1:3260 --login
Logout:
 iscsiadm --mode node --targetname iqn.2001-05.com.doe:test --portal 192.168.1.1:3260 --logout
List node records:
 iscsiadm --mode node
Display all data for a given node record:
 iscsiadm --mode node --targetname iqn.2001-05.com.doe:test --portal 192.168.1.1:3260</pre>
<h2>Files</h2>
<dl>
<dt>/etc/iscsi/iscsid.conf</p>
<dd>The configuration file read by <code>iscsid</code> and <code>iscsiadm</code> on startup.</p>
<dt>/etc/iscsi/initiatorname.iscsi</p>
<dd>The file containing the iSCSI InitiatorName and InitiatorAlias read by <code>iscsid</code> and <code>iscsiadm</code> on startup.</p>
<dt>/var/lib/iscsi/nodes/</p>
<dd>This directory contains the nodes with their targets.</p>
<dt>/var/lib/iscsi/send_targets</p>
<dd>This directory contains the portals. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iscsid/">iscsid</a></code>(8) </p>
<h2>Authors</h2>
<p>Open-iSCSI project &lt;<a rel="nofollow" href="http://www.open-iscsi.com/">http://www.open-iscsi.com/</a>&gt;<br />
 Alex Aizman &lt;itn780 [at] yahoo.com&gt;<br />
 Dmitry Yusupov &lt;dmitry_yus [at] yahoo.com&gt;</p>
