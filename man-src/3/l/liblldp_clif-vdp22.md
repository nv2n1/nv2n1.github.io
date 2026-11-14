---
title: "liblldp_clif-vdp22(3)"
name: "liblldp_clif-vdp22"
section: "3"
letter: "l"
url: "/docs/linux/man/3-liblldp_clif-vdp22/"
description: "clif_vsi,clif_vsievt,clif_vsiwait – Manipulate VDP IEEE 802.1 Ratified Standard Assocications"
---

<h2>NAME</h2>
<p> clif_vsi,clif_vsievt,clif_vsiwait &#8211; Manipulate VDP IEEE 802.1 Ratified Standard Assocications</p>
<h2>SYNOPSIS</h2>
<p> #include &quot;include/clif.h&quot; </p>
<p> <code>int clif_vsi(struct clif *connp, char *ifname, unsigned int tlvid, char *cmd, char *reply, size_t *reply_len);</code> </p>
<p> <code>int clif_vsievt(struct clif *connp, char *reply, size_t *reply_len, int wait);</code> </p>
<p> <code>int clif_vsiwait(struct clif *connp, char *ifname, unsigned int tlvid, char *cmd, char *reply, size_t *reply_len, int wait);</code> </p>
<h2>DESCRIPTION</h2>
<p> The Virtual station interface Discovery Protocol is a protocol to manage the association and deassociation of virtual machine network interfaces (VSIs) between the station and an adjacent switch. VDP is typically used with the local switch in VEPA mode and the adjacent switch port in reflective relay (also called haripin) mode. This allows all traffic to be sent to the switch for processing. Reflective relay mode is negotiated via EVB TLVs (see lldptool-evb). </p>
<p> This man pages describes the IEEE 802.1 Qbg ratified standard dated from July 5th, 2012. This differs from the draft 0.2 which is implemented as well, see <code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8). For clarification in this man page the version complying to the ratified standard is called VDP22 and the version complying to the draft 0.2 is called VDP.</p>
<h3>VSI Parameter</h3>
<p> Each VDP22 TLVs contains a command mode, manager identifier, type identifier, type identifier version, VSI instance identifier, migiration hints and filter information. The fields are explained next:</p>
<dl>
<dt><code>Command Mode:</code></p>
<dd> The command mode determines the type of the VSI association to be established. It is an ascii string can be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>assoc:</p>
<dd> Create an VSI association.</p>
<dt>preassoc:</p>
<dd> Create an VSI preassociation. The association is only announced to the switch.</p>
<dt>preassoc-rr:</p>
<dd> Create an VSI preassociation. The association is only announced to the switch and the switch should reserve the resources.</p>
<dt>deassoc:</p>
<dd> Delete an VSI association.</dl>
</dl>
<p> Other strings are not recognized and return an error.</p>
<dt><code>Manager identifier:</code></p>
<dd> The manager identifier is a string of up to 16 alphanumeric characters. It can also be an UUID according to RFC 4122 with optional dashes in between.</p>
<dt><code>Type Identifier:</code></p>
<dd> The type identifier is a number in the range of 0 to 2^24 &#8211; 1.</p>
<dt><code>Type Identifier Version:</code></p>
<dd> The type identifer version is a number in the range of 0 to 255.</p>
<dt><code>VSI Instance Identifier:</code></p>
<dd> The VSI instance identifier is an UUID according to RFC 4122 with optional dashes in between.</p>
<dt><code>Migration Hints:</code></p>
<dd> The migiration hints is a string aiding in migration of virtual machines:</p>
<dl>
<dt>
<dd>
<dl>
<dt>none:</p>
<dd> No hints available.</p>
<dt>from:</p>
<dd> The virtual machine is migriting away.</p>
<dt>to:</p>
<dd> The virtual machine is migriting to.</dl>
</dl>
<dt><code>Filter Information Data:</code></p>
<dd> The filter information data can be supplied in four different formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt>vlan (1)</p>
<dd> A vlan number only, also known as filter information format 1. The vlan identifier is a number in the range of 1 to 2^16 &#8211; 1. The high order 4 bits are used as quality of service bits. The vlan identifier can be zero, a vlan identifier is then selected by the switch. Refer to IEEE 802.1 Qbg ratified standard for details.</p>
<dt>vlan-mac (2)</p>
<dd> A vlan number and MAC address delimited by a slash (&#8216;-&#8216;), also known as filter information format 2. The MAC address is specified in the format xx:xx:xx:xx:xx:xx. The colons are mandatory. For vlan details see (1).</p>
<dt>vlan-mac-group (4)</p>
<dd> A vlan number, MAC address and group identifier, each delimited by a slash (&#8216;-&#8216;), also known as filter information format 4. The group identifier is a 32 bit number. For vlan and MAC address details see (1) and (2).</p>
<dt>vlan&#8211;group (3)</p>
<dd> A vlan number and group identifier, delimited by two slashes (&#8216;&#8211;&#8216;), also known as filter information format 3. For vlan and group details see (1) and (4).</dl>
</dl>
<p> Several filter information fields can be supplied. The have to be separated by comma (&#8216;,&#8217;) and must be of the same format.</dl>
<h3>clif_vsi</h3>
<p> This function sends a VSI command to <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8). Parameter <i>connp</i> is a pointer to the connection information. This information is obtained by calling <i>clif_open</i> and <i>clif_attach</i>. Parameter <i>ifname</i> is the interface name <code>lldpad </code> (8) uses to send the VSI data. Paramenter <i>tlvid</i> is the number of the VSI request. Valid numbers are 1 (for Preassociation), 2 (for Preassociation with resource reservation) and 3 (for association), 4 (for Deassociation). Parameter <i>cmd</i> points to a character string containing the VSI command. The layout of the VSI command has been explained above. All VSI fields are concatenated together and separated to by commas (&#8216;,&#8217;) to form one large string. Parameter <i>reply</i> is a pointer to a character array to receive the reply from <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8). Parameter <i>reply_len</i> holds the maximum number of characters available in the array pointed to by <i>reply</i>. On successful return of the call, <i>reply_len</i> contains the number of characters stored by <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) as the response of the command. </p>
<p> The functions returns zero on success and the <i>reply</i> and <i>reply_len</i> parameters are set. <i>Reply_len</i> contains the number of bytes in the memory area pointed to by <i>reply</i>. <i>Reply</i> contains the same information and format as the <i>cmd</i> parameter with several exceptions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Command Mode:</p>
<dd> This field should be the same as in <i>cmd</i> parameter. If it contains <i>deassoc</i> then the command failed and the field <i>,igration hints</i> contains an error numner.</p>
<dt>Migration Hints:</p>
<dd> This field contains the error number on why the command was not accepted by <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8). This command failed to pass the <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) sanity checks. Note that the command was not even sent to the switch for processing. If no error occured, this field contains a dash (&#8216;-&#8216;).</p>
<dt>Filter Information Data:</p>
<dd> If parameter <i>cmd</i> contained the a <i>vlan identifier</i> of value zero or a <i>group identifier</i> the switch is allowed to assign a different <i>vlan identifier</i>, which is saved and returned in the reply buffer.</dl>
</dl>
<p> All the other fields should be returned unchanged. </p>
<p> The function returns zero when the command was accepted by <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8). Otherwise it returns a positive number on why the command was not accepted.</p>
<h3>clif_vsievt</h3>
<p> After a successful return of <i>clif_vsi</i>, <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) has sent the command to the switch and waits for a response from the switch. The switch can still deny the request. Function <i>clif_vsievt</i> waits for parameter <i>wait</i> seconds for a reply from <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8). Parameter <i>reply_len</i> specifies the maximum buffer size pointed to by parameter <i>reply.</i> If a response was received in <i>wait </i> seconds, the function returns zero and sets <i>reply_len</i> to the number of bytes received and <i>reply</i> contains the response. The format is the same as in <i>clif_vsi</i>. </p>
<p> Since the switch can disassociate an established VSI association any time, it is recommended to call <i>clif_vsievt</i> periodically to check for disassociate event messages from <i><a href="/docs/linux/man/8-lldpad/">lldpad</a></i>(8). </p>
<p> If the functions fails it returns</p>
<dl>
<dt>-EINVAL</p>
<dd> No attachment to <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) or <i>wait</i> is negative.</p>
<dt>-EAGAIN</p>
<dd> No message was received during the wait.</p>
<dt>-EIO</p>
<dd> Message was received but could not be read.</p>
<dt>-EBADF</p>
<dd> Message was received but was not an event message.</dl>
<h3>clif_vsiwait</h3>
<p> This function combines <i>clif_vsi </i> and <i>clif_vsievt</i> into one function call.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<p> Code sample to create an VSI association on <i>eth0</i>: </p>
<pre><code>
char ok[MAX_CLIF_MSGBUF];
int rc;
size_t ok_len = sizeof(ok);
char *cmd = "assoc,blabla,12345,1,00000000-1111-2222-3333-aabbccddeeff"
            ",none,10-aa:bb:00:00:00:10,11-aa:bb:00:00:00:11";
struct clif *tool_conn = clif_open();
if (!tool_conn) {
    fprintf(stderr, "%s can not open connection to LLDPAD,
            progname);
    exit(5);
}
/* Attach to the vdp22 module */
if (clif_attach(tool_conn, "80c4")) {
        fprintf(stderr, "%s can not attach to LLDPAD, progname);
        clif_close(tool_conn);
        tool_conn = NULL;
        exit(5);
}
rc = clif_vsiwait(tool_conn, "eth0", 1, cmd, ok, &amp;ok_len, 5);
if (!rc) {
    /* Parse the response in ok */
    ....
}
clif_detach(tool_conn));
clif_close(tool_conn);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb/">lldptool-evb</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb22/">lldptool-evb22</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8)<br />
 IEEE 802.1Qbg (<a rel="nofollow" href="http://www.ieee802.org/1/pages/802.1bg.html)">http://www.ieee802.org/1/pages/802.1bg.html)</a></p>
<h2>AUTHOR</h2>
<p> Thomas Richter </p>
<h2>Index</h2>
