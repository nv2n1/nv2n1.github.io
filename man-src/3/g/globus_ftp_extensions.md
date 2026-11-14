---
title: "globus_ftp_extensions(3)"
name: "globus_ftp_extensions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_extensions/"
description: "globus_ftp_extensions – GridFTP: Protocol Extensions to FTP for the Grid"
---

<h2 class="name">NAME</h2>
<p> globus_ftp_extensions &#8211; GridFTP: Protocol Extensions to FTP for the Grid</p>
<h2>Introduction</h2>
<p> This section defines extensions to the FTP specification STD 9, RFC 959, <code>FILE TRANSFER PROTOCOL (FTP)</code> (October 1985) These extensions provide striped data transfer, parallel data transfer, extended data transfer, data buffer size configuration, and data channel authentication. </p>
<p> The following new commands are introduced in this specification</p>
<dl>
<dt>&bull;</p>
<dd> <code>Striped Passive (SPAS)</code></p>
<dt>&bull;</p>
<dd> <code>Striped Data Port (SPOR)</code></p>
<dt>&bull;</p>
<dd> <code>Extended Retrieve (ERET)</code></p>
<dt>&bull;</p>
<dd> <code>Extended Store (ESTO)</code></p>
<dt>&bull;</p>
<dd> <code>Set Data Buffer Size (SBUF)</code></p>
<dt>&bull;</p>
<dd> <code>Data Channel Authentication Mode (DCAU)</code></dl>
<p> A new transfer mode (<code>extended-block mode</code>) is introduced for parallel and striped data transfers. Also, a set of extension <code>options to RETR</code> are added to control striped data layout and parallelism. </p>
<p> The following new feature names are to be included in the FTP server&#8217;s response to FEAT if it implements the following sets of functionality </p>
<p> <code>PARALLEL</code></p>
<dl>
<dt>
<dd> The server supports the SPOR, SPAS, the RETR options mentioned above, and extended block mode.</dl>
<p> <code>ESTO</code></p>
<dl>
<dt>
<dd> The server implements the ESTO command as described in this document.</dl>
<p> <code>ERET</code></p>
<dl>
<dt>
<dd> The server implements the ERET command as described in this document.</dl>
<p> <code>SBUF</code></p>
<dl>
<dt>
<dd> The server implements the SBUF command as described in this document.</dl>
<p> <code>DCAU</code></p>
<dl>
<dt>
<dd> The server implements the DCAU command as described in this document, including the requirement that data channels are authenticated by default, if <code>RFC 2228</code> authentication is used to establish the control channel.</dl>
<h2>Terminology</h2>
<p> <code>Parallel transfer</code></p>
<dl>
<dt>
<dd> From a single data server, splitting file data for transfer over multiple data connections.</dl>
<p> <code>Striped transfer</code></p>
<dl>
<dt>
<dd> Distributing a file&#8217;s data over multiple independent data nodes, and transerring over multiple data connections.</dl>
<p> <code>Data Node</code></p>
<dl>
<dt>
<dd> In a striped data transfer, a data node is one of the stripe destinations returned in the SPAS command, or one of the stripe destinations sent in the SPOR command.</dl>
<p> <code>DTP</code></p>
<dl>
<dt>
<dd> The data transfer process establishes and manages the data connection. The DTP can be passive or active.</dl>
<p> <code>PI</code></p>
<dl>
<dt>
<dd> The protocol interpreter. The user and server sides of the protocol have distinct roles implemented in a user-PI and a server-PI.</dl>
<h2>FTP Standards Used</h2>
<dl>
<dt>&bull;</p>
<dd> RFC 959, <code>FILE TRANSFER PROTOCOL (FTP)</code>, J. Postel, R. Reynolds (October 1985)</p>
<dt> &bull;</p>
<dd> Commands used by GridFTP</p>
<dt> &bull;</p>
<dd> USER</p>
<dt> &bull;</p>
<dd> PASS</p>
<dt> &bull;</p>
<dd> ACCT</p>
<dt> &bull;</p>
<dd> CWD</p>
<dt> &bull;</p>
<dd> CDUP</p>
<dt> &bull;</p>
<dd> QUIT</p>
<dt> &bull;</p>
<dd> REIN</p>
<dt> &bull;</p>
<dd> PORT</p>
<dt> &bull;</p>
<dd> PASV</p>
<dt> &bull;</p>
<dd> TYPE</p>
<dt> &bull;</p>
<dd> MODE</p>
<dt> &bull;</p>
<dd> RETR</p>
<dt> &bull;</p>
<dd> STOR</p>
<dt> &bull;</p>
<dd> STOU</p>
<dt> &bull;</p>
<dd> APPE</p>
<dt> &bull;</p>
<dd> ALLO</p>
<dt> &bull;</p>
<dd> REST</p>
<dt> &bull;</p>
<dd> RNFR</p>
<dt> &bull;</p>
<dd> RNTO</p>
<dt> &bull;</p>
<dd> ABOR</p>
<dt> &bull;</p>
<dd> DELE</p>
<dt> &bull;</p>
<dd> RMD</p>
<dt> &bull;</p>
<dd> MKD</p>
<dt> &bull;</p>
<dd> PWD</p>
<dt> &bull;</p>
<dd> LIST</p>
<dt> &bull;</p>
<dd> NLST</p>
<dt> &bull;</p>
<dd> SITE</p>
<dt> &bull;</p>
<dd> SYST</p>
<dt> &bull;</p>
<dd> STAT</p>
<dt> &bull;</p>
<dd> HELP</p>
<dt> &bull;</p>
<dd> NOOP</dl>
<dl>
<dt> &bull;</p>
<dd> Features used by GridFTP</p>
<dt> &bull;</p>
<dd> ASCII and Image types</p>
<dt> &bull;</p>
<dd> Stream mode</p>
<dt> &bull;</p>
<dd> File structure</dl>
<dl>
<dt>&bull;</p>
<dd> RFC 2228, <code>FTP Security Extensions</code>, Horowitz, M. and S. Lunt (October 1997)</p>
<dt> &bull;</p>
<dd> Commands used by GridFTP</p>
<dt> &bull;</p>
<dd> AUTH</p>
<dt> &bull;</p>
<dd> ADAT</p>
<dt> &bull;</p>
<dd> MIC</p>
<dt> &bull;</p>
<dd> CONF</p>
<dt> &bull;</p>
<dd> ENC</dl>
<dl>
<dt> &bull;</p>
<dd> Features used by GridFTP</p>
<dt> &bull;</p>
<dd> GSSAPI authentication</dl>
<dl>
<dt>&bull;</p>
<dd> RFC 2389, <code>Feature negotiation mechanism for the File Transfer Protocol</code>, P. Hethmon , R. Elz (August 1998)</p>
<dt> &bull;</p>
<dd> Commands used by GridFTP</p>
<dt> &bull;</p>
<dd> FEAT</p>
<dt> &bull;</p>
<dd> OPTS</dl>
<dl>
<dt> &bull;</p>
<dd> Features used by GridFTP</dl>
<dl>
<dt>&bull;</p>
<dd> <code>FTP Extensions</code>, R. Elz, P. Hethmon (September 2000)</p>
<dt> &bull;</p>
<dd> Commands used by GridFTP</p>
<dt> &bull;</p>
<dd> SIZE</dl>
<dl>
<dt> &bull;</p>
<dd> Features used by GridFTP</p>
<dt> &bull;</p>
<dd> Restart of a stream mode transfer</dl>
<h2>Striped Passive (SPAS)</h2>
<p> This extension is used to establish a vector of data socket listeners for for a server with one or more stripes. This command MUST be used in conjunction with the extended block mode. The response to this command includes a list of host and port addresses the server is listening on. </p>
<p> Due to the nature of the extended block mode protocol, SPAS must be used in conjunction with data transfer commands which receive data (such as STOR, ESTO, or APPE) and can not be used with commands which send data on the data channels. </p>
<p> <code>Syntax</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The syntax of the SPAS command is: </p>
<pre>
spas = &quot;SPAS&quot; &lt;CRLF&gt;
</pre>
<p> <code>Responses</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The server-PI will respond to the SPAS command with a 229 reply giving the list of host-port strings for the remote server-DTP or user-DTP to connect to. </p>
<pre>
spas-response = &quot;229-Entering Striped Passive Mode&quot; CRLF
                 1*(&lt;SP&gt; host-port CRLF)
                 229 End
</pre>
<p> Where the command is correctly parsed, but the server-DTP cannot process the SPAS request, it must return the same error responses as the PASV command. </p>
<p> <code>OPTS for SPAS</code></p>
<dl>
<dt>
<dd>
</dl>
<p> There are no options in this SPAS specification, and hence there is no OPTS command defined. </p>
<h2>Striped Data Port (SPOR)</h2>
<p> This extension is to be used as a complement to the SPAS command to implement striped third-party transfers. This command MUST always be used in conjunction with the extended block mode. The argument to SPOR is a vector of host/TCP listener port pairs to which the server is to connect. This </p>
<p> Due to the nature of the extended block mode protocol, SPOR must be used in conjunction with data transfer commands which send data (such as RETR, ERET, LIST, or NLST) and can not be used with commands which receive data on the data channels. </p>
<p> <code>Syntax</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The syntax of the SPOR command is: </p>
<pre>
SPOR 1*(&lt;SP&gt; &lt;host-port&gt;) &lt;CRLF&gt;
</pre>
<p> The host-port sequence in the command structure MUST match the host-port replies to a SPAS command. </p>
<p> <code>Responses</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The server-PI will respond to the SPOR command with the same response set as the PORT command described in the <code>ftp specification</code>. </p>
<p> <code>OPTS for SPOR</code></p>
<dl>
<dt>
<dd>
</dl>
<p> There are no options in this SPOR specification, and hence there is no OPTS command defined. </p>
<h2>Extended Retrieve (ERET)</h2>
<p> The extended retrieve extension is used to request that a retrieve be done with some additional processing on the server. This command an extensible way of providing server-side data reduction or other modifications to the RETR command. This command is used in place of OPTS to the RETR command to allow server side processing to be done with a single round trip (one command sent to the server instead of two) for latency-critical applications. </p>
<p> ERET may be used with either the data transports defined in RFC 959, or using extended block mode as defined in this document. Using an ERET creates a new virtual file which will be sent, with it&#8217;s own size and byte range starting at zero. Restart markers generated while processing an ERET are relative to the beginning of this view of the file. </p>
<p> <code>Syntax</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The syntax of the ERET command is </p>
<pre>
ERET &lt;SP&gt; &lt;retrieve-mode&gt; &lt;SP&gt; &lt;filename&gt;
retrieve-mode ::= P &lt;SP&gt; &lt;offset&gt; &lt;SP&gt; &lt;size&gt;
offset ::= 64 bit integer
size ::= 64 bit integer
</pre>
<p> The <code>retrieve-mode</code> defines behavior of the extended-retrieve mode. There is one mode defined by this specification, but other general purpose or application-specific ones may be added later. </p>
<p> <code>modes_ERET Extended Retrieve Modes</code></p>
<dl>
<dt>
<dd>
</dl>
<p> <code>Partial Retrieve Mode (P)</code></p>
<dl>
<dt>
<dd> A section of the file will be retrieved from the data server. The section is defined by the starting <code>offset</code> and extent <code>size</code> parameters. When used with extended block mode, the extended block headers sent along with data will send the data with offset of 0 meaning the beginning of the section of the file which was requested.</dl>
<h2>Extended Store (ESTO)</h2>
<p> The extended store extension is used to request that a store be done with some additional processing on the server. Arbitrary data processing algorithms may be added by defining additional ESTO store-modes. Similar to the ERET, the ESTO command expects data sent to satisfy the request to be sent as if it were a new file with data block offset 0 being beginning the beginning of the new file. </p>
<p> The format of the ESTO command is </p>
<pre>
ESTO &lt;SP&gt; &lt;store-mode&gt; &lt;filename&gt;
store-mode ::= A &lt;SP&gt; &lt;offset&gt;
</pre>
<p> The store-mode defines the behavior of the extended store. There is one mode defined by this specification, but others may be added later. </p>
<p> <code>Extended Store Modes</code></p>
<dl>
<dt>
<dd>
</dl>
<p> <code>Adjusted store (A)</code></p>
<dl>
<dt>
<dd> The data in the file is to stored with <code>offset</code> added to the file pointer before storing the blocks of the file. In extended block mode, this value is added to the offset in the extended block header by the server when writing to disk. Extended block headers should therefore send the beginning of the byte range on the data channel with offset of zero. In stream mode, the offset is added to the implicit offset of 0 for the beginning of the data before writing. If a stream mode restart marker is used in conjunction with this ESTO mode, the restart marker&#8217;s offset is added to the offset passed as the parameter to the adjusted store.</dl>
<h2>Set Buffer Size (SBUF)</h2>
<p> This extension adds the capability of a client to set the TCP buffer size for subsequent data connections to a value. This replaces the server-specific commands SITE RBUFSIZE, SITE RETRBUFSIZE, SITE RBUFSZ, SITE SBUFSIZE, SITE SBUFSZ, and SITE BUFSIZE. Clients may wish to consider supporting these other commands to ensure wider compatibility. </p>
<p> <code>Syntax</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The syntax of the SBUF command is </p>
<pre>
sbuf = SBUF &lt;SP&gt; &lt;buffer-size&gt;
buffer-size ::= &lt;number&gt;
</pre>
<p> The <code>buffer-size</code> value is the TCP buffer size in bytes. The TCP window size should be set accordingly by the server. </p>
<p> <code>Response Codes</code></p>
<dl>
<dt>
<dd>
</dl>
<p> If the server-PI is able to set the buffer size state to the requested <code>buffer-size</code>, then it will return a 200 reply. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Even if the SBUF is accepted by the server, an error may occur later when the data connections are actually created, depending on how the server or client operating systems&#8217; TCP implementations.</dl>
<h2>Data Channel Authentication (DCAU)</h2>
<p> This extension provides a method for specifying the type of authentication to be performed on FTP data channels. This extension may only be used when the control connection was authenticated using RFC 2228 Security extensions. </p>
<p> The format of the DCAU command is </p>
<pre>
DCAU &lt;SP&gt; &lt;authentication-mode&gt; &lt;CRLF&gt;
authentication-mode ::= &lt;no-authentication&gt;
                      | &lt;authenticate-with-self&gt;
                      | &lt;authenticate-with-subject&gt;
no-authentication ::= N
authenticate-with-self ::= A
authenticate-with-subject ::= S &lt;subject-name&gt;
subject-name ::= string
</pre>
<p> <code>Authentication Modes</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> No authentication (<code>N</code>) </p>
<p>&nbsp;<wbr>No authentication handshake will be done upon data connection establishment.</p>
<dt>&bull;</p>
<dd> Self authentication (<code>A</code>) </p>
<p>&nbsp;<wbr>A security-protocol specific authentication will be used on the data channel. The identity of the remote data connection will be the same as the identity of the user which authenticated to the control connection.</p>
<dt>&bull;</p>
<dd> Subject-name authentication (<code>S</code>) </p>
<p>&nbsp;<wbr>A security-protocol specific authentication will be used on the data channel. The identity of the remote data connection MUST match the supplied&nbsp;<wbr><code>subject-name</code>&nbsp;<wbr>string.</dl>
</dl>
<p> The default data channel authentication mode is <code>A</code> for FTP sessions which are RFC 2228 authenticated&#8212;the client must explicitly send a DCAU N message to disable it if it does not implement data channel authentication. </p>
<p> If the security handshake fails, the server should return the error response 432 (Data channel authentication failed).</p>
<h2>Extended Block Mode</h2>
<p> The striped and parallel data transfer methods described above require an extended transfer mode to support out-of-sequence data delivery, and partial data transmission per data connection. The extended block mode described here extends the block mode header to provide support for these as well as large blocks, and end-of-data synchronization. </p>
<p> Clients indicate that they want to use extended block mode by sending the command </p>
<pre>
MODE &lt;SP&gt; E &lt;CRLF&gt;
</pre>
<p> on the control channel before a transfer command is sent. </p>
<p> The structure of the extended block header is </p>
<pre><code>
Extended Block Header + -- -- -- -- -- -- -- --+-- -- -- - / -- -- -- -- -- -+-- -- -- / -- -- -- -- -- --+ | Descriptor | Byte Count | Offset Count |
    | 8 bits | 64 bits | 64 bits |
    +-- -- -- -- -- -- -- --+-- -- -- - / -- -- -- -- -- -+-- -- -- / -- -- -- -- -- --+
</code></pre>
<p> The descriptor codes are indicated by bit flags in the descriptor byte. Six codes have been assigned, where each code number is the decimal value of the corresponding bit in the byte. </p>
<pre>
Code     Meaning
 128     End of data block is EOR (Legacy)
  64     End of data block is EOF
  32     Suspected errors in data block
  16     Data block is a restart marker
   8     End of data block is EOD for a parallel/striped transfer
   4     Sender will close the data connection
</pre>
<p> With this encoding, more than one descriptor coded condition may exist for a particular block. As many bits as necessary may be flagged. </p>
<p> Some additional protocol is added to the extended block mode data channels, to properly handle end-of-file detection in the presence of an unknown number of data streams. </p>
<dl>
<dt>&bull;</p>
<dd> When no more data is to be sent on the data channel, then the sender will mark the last block, or send a zero-length block after the last block with the EOD bit (8) set in the extended block header.</p>
<dt>&bull;</p>
<dd> After receiving an EOD the data connection can be cached for use in a subsequent transfer. To signifiy that the data connection will be closed the sender sets the close bit (4) in the header on the last message sent.</p>
<dt>&bull;</p>
<dd> The sender communicates end of file by sending an EOF message to all servers receiving data. The EOF message format follows.</dl>
<p> Extended Block EOF Header </p>
<p>+ &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211; / &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; / &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | Descriptor | unused | EOD count expected |<br />
    | 8 bits | 64 bits | 64 bits |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211; / &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; / &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+</p>
<p> EOF Descriptor. The EOF header descriptor has the same definition as the regular data message header described above. </p>
<p> EOD Count Expected. This 64 bit field represents the total number of data connections that will be established with the server receiving the file. This number is used by the receiver to determine it has received all of the data. When the number of EOD messages received equals the number represented by the &#8216;EOD Count Expected&#8217; field the receiver has hit end of file. </p>
<p> Simply waiting for EOD on all open data connections is not sufficient. It is possible that the receiver reads an EOD message on all of its open data connects while an additional data connection is in flight. If the receiver were to assume it reached end of file it would fail to receive the data on the in flight connection. </p>
<p> To handle EOF in the multi-striped server case a 126 response has been introduced. When receiving data from a striped server a client makes a control connection to a single host, but several host may create several data connections back to the client. Each host can independently decide how many data connections it will use, but only a single EOF message may be sent to back to the client, therefore it must be possible to aggregate the total number of data connections used in the transfer across the stripes. The 126 response serves this purpose. </p>
<p> The 126 is an intermediate response to RETR command. It has the following format. </p>
<pre>
126 &lt;SP&gt; 1*(count of data connections)
</pre>
<p> Several &#8216;Count of data connections&#8217; can be in a single reply. They correspond to the stripes returned in the response to the SPAS command. </p>
<p> Discussion of protocol change to enable bidirectional data channels brought up the following problem if doing bidirectional data channels </p>
<p> If the client is pasv, and sending to a multi-stripe server, then the server creates data connections connections; since the client didn&#8217;t do SPAS, it cannot associate HOST/PORT pairs on the data connections with stripes on the server (it doesn&#8217;t even know how many there are). it cannot reliably determine which nodes to send data to. (Becomes even more complex in the third-party transfer case, because the sender may have multiple stripes of data.) The basic problem is that we need to know logical stripe numbers to know where to send the data. </p>
<p> <code>EOF Handling in Extended Block Mode</code></p>
<dl>
<dt>
<dd>
</dl>
<p> If you are in either striped or parallel mode, you will get exactly one EOF on each SPAS-specified ports (stripes). Hosts in extended block mode must be prepared to accept an arbitrary number of connections on each SPOR port before the EOF block is sent. </p>
<p> <code>Restarting</code></p>
<dl>
<dt>
<dd>
</dl>
<p> In general, opaque restart markers passed via the block header should not be used in extended block mode. Instead, the destination server should send extended data marker responses over the control connection, in the following form: </p>
<pre>
extended-mark-response = &quot;111&quot; &lt;SP&gt; &quot;Range Marker&quot; &lt;SP&gt; &lt;byte-ranges-list&gt;
byte-ranges-list       = &lt;byte-range&gt; [ *(&quot;,&quot; &lt;byte-range&gt;) ]
byte-range             = &lt;start-offset&gt; &quot;-&quot; &lt;end-offset&gt;
start-offset         ::= &lt;number&gt;
end-offset           ::= &lt;number&gt;
</pre>
<p> The byte ranges in the marker are an incremental set of byte ranges which have been stored to disk by the data server. The complete restart marker is a concatenation of all byte ranges received by the client in 111 responses. </p>
<p> The client MAY combine adjacent ranges received over several range responses into any number of ranges when sending the REST command to the server to restart a transfer. </p>
<p> For example, the client, on receiving the responses: </p>
<pre>
111 Range Marker 0-29
111 Range Marker 30-89
</pre>
<p> may send, equivalently, </p>
<pre>
REST 0-29,30-89
REST 0-89
REST 30-59,0-29,60-89
</pre>
<p> to restart the transfer after those 90 bytes have been received. </p>
<p> The server MAY indicate that a given range of data has been received in multiple subsequent range markers. The client MUST be able to handle this. For example: </p>
<pre>
111 Range Marker 30-59
111 Range Marker 0-89
</pre>
<p> is equivalent to </p>
<pre>
111 Range Marker 30-59
111 Range Marker 0-29,60-89
</pre>
<p> Similarly, the client, if it is doing no processing of the restart markers, MAY send redundant information in a restart. </p>
<p> <i>Should these be allowed as restart markers for stream mode?</i> </p>
<p> <code>Performance Monitoring</code></p>
<dl>
<dt>
<dd>
</dl>
<p> In order to monitor the performance of extended block mode transfer, an additional preliminary reply MAY be transmitted over the control channel. This reply is of the form: </p>
<pre>
extended-perf-response  = &quot;112-Perf Marker&quot; CRLF
                          &lt;SP&gt; &quot;Timestamp:&quot; &lt;SP&gt; &lt;timestamp&gt; CRLF
              &lt;SP&gt; &quot;Stripe Index:&quot; &lt;SP&gt; &lt;stripe-number&gt; CRLF
              &lt;SP&gt; &quot;Stripe Bytes Transferred:&quot; &lt;SP&gt; &lt;byte count&gt; CRLF
              &lt;SP&gt; &quot;Total Stripe Count:&quot; &lt;SP&gt; &lt;stripe count&gt; CRLF
                          &quot;112 End&quot; CRLF
timestamp               = &lt;number&gt; [ &quot;.&quot; &lt;digit&gt; ]
</pre>
<p>&nbsp;<wbr> </p>
<p> &lt;timestamp&gt; is seconds since the epoch </p>
<p> The performance marker can contain these or any other perf-line facts which provide useful information about the current performance. </p>
<p> All perf-line facts represent an instantaneous state of the transfer at the given timestamp. The meaning of the facts are </p>
<dl>
<dt>&bull;</p>
<dd> Timestamp &#8211; The time at which the server computed the performance information. This is in seconds since the epoch (00:00:00 UTC, January 1, 1970).</p>
<dt>&bull;</p>
<dd> Stripe Index &#8211; the index (0-number of stripes on the STOR side of the transfer) which this marker pertains to.</p>
<dt>&bull;</p>
<dd> Stripe Bytes Transferred &#8211; The number of bytes which have been received on this stripe.</dl>
<p> A transfer start time can be specified by a perf marker with &#8216;Stripe Bytes Transferred&#8217; set to zero. Only the first marker per stripe can be used to specify the start time of that stripe. Any subsequent markers with &#8216;Stripe Bytes Transferred&#8217; set to zero simply indicates no data transfer over the interval. </p>
<p> A server should send a &#8216;start&#8217; marker for each stripe. A server should also send a final perf marker for each stripe. This is a marker with &#8216;Stripe Bytes Transferred&#8217; set to the total transfer size for that stripe. </p>
<h2>Options to RETR</h2>
<p> The options described in this section provide a means to convey striping and transfer parallelism information to the server-DTP. For the RETR command, the Client-FTP may specify a parallelism and striping mode it wishes the server-DTP to use. These options are only used by the server-DTP if the retrieve operation is done in extended block mode. These options are implemented as <code>RFC 2389</code> extensions. </p>
<p> The format of the RETR OPTS is specified by: </p>
<pre><code>
retr - opts = "OPTS" &lt; SP &gt; "RETR"[&lt;SP&gt; option - list] CRLF
                                    option -
                                list = [layout - opts ";"][parallel - opts ";"] layout - opts = "StripeLayout=Partitioned" | "StripeLayout=Blocked;BlockSize=" &lt; block - size &gt;
                                                                                                                                 parallel - opts = "Parallelism=" &lt; starting - parallelism &gt; "," &lt; minimum - parallelism &gt; "," &lt; maximum - parallelism &gt;
                                                                                                                                                   block - size ::
                                                                                                                                                       = &lt;number&gt;
                                                                                                                                                             starting - parallelism ::
                                                                                                                                                             = &lt;number&gt;
                                                                                                                                                                   minimum - parallelism ::
                                                                                                                                                                   = &lt;number&gt;
                                                                                                                                                                         maximum - parallelism ::
                                                                                                                                                                         = &lt;number&gt;
</code></pre>
<p> <code>Layout Options</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The layout option is used by the source data node to send sections of the data file to the appropriate destination stripe. The various StripeLayout parameters are to be implemented as follows: </p>
<p> <code>Partitioned</code></p>
<dl>
<dt>
<dd> A partitioned data layout is one where the data is distributed evenly on the destination data nodes. Only one contiguous section of data is stored on each data node. A data node is defined here a single host-port mentioned in the SPOR command</dl>
<p> <code>Blocked</code></p>
<dl>
<dt>
<dd> A blocked data layout is one where the data is distributed in round-robin fashion over the destination data nodes. The data distribution is ordered by the order of the host-port specifications in the SPOR command. The <code>block-size</code> defines the size of blocks to be distributed.</dl>
<p> <code>PLVL Parallelism Options</code></p>
<dl>
<dt>
<dd>
</dl>
<p> The parallelism option is used by the source data node to control how many parallel data connections may be established to each destination data node. This extension option provides for both a fixed level of parallelism, and for adapting the parallelism to the host/network connection, within a range. If the <code>starting-parallelism</code> option is set, then the server-DTP will make <code>starting-parallelism</code> connections to each destination data node. If the <code>minimum-parallelism</code> option is set, then the server may reduce the number of parallel connections per destination data node to this value. If the <code>maximum-parallelism</code> option is set, then the server may increase the number of parallel connections to per destination data node to at most this value.</p>
<h2>References</h2>
<p> [1] Postel, J. and Reynolds, J., &#8216;&lt;a href=&#8217;<a href="ftp://ftp.isi.edu/in-notes/rfc959.txt'">ftp://ftp.isi.edu/in-notes/rfc959.txt&#8217;</a>&gt; FILE TRANSFER PROTOCOL (FTP)&lt;/a&gt;&#8217;, STD 9, RFC 959, October 1985. </p>
<p> [2] Hethmon, P. and Elz, R., &#8216;&lt;a href=&#8217;<a href="ftp://ftp.isi.edu/in-notes/rfc2389.txt'">ftp://ftp.isi.edu/in-notes/rfc2389.txt&#8217;</a>&gt; Feature negotiation mechanism for the File Transfer Protocol&lt;/a&gt;&#8217;, RFC 2389, August 1998. </p>
<p> [3] Horowitz, M. and Lunt, S., &#8216;&lt;a href=&#8217;<a href="ftp://ftp.isi.edu/in-notes/rfc2228.txt'">ftp://ftp.isi.edu/in-notes/rfc2228.txt&#8217;</a>&gt; FTP Security Extensions&lt;/a&gt;&#8217;, RFC 2228, October 1997. </p>
<p> [4] Elz, R. and Hethom, P., &#8216;&lt;a href=&#8217;<a rel="nofollow" href="http://www.ietf.org/internet-drafts/draft-ietf-ftpext-mlst-13.txt'">http://www.ietf.org/internet-drafts/draft-ietf-ftpext-mlst-13.txt&#8217;</a>&gt; FTP Extensions&lt;/a&gt;&#8217;, IETF Draft, May 2001.</p>
<h2>Appendix I: Implementation under GSI</h2>
<p> There are several security components in this document which are extensions to the behavior of RFC 2228. These appendix attempts to clarify the protocol how these extensions map to the OpenSSL-based implementation of the GSSAPI known as GSI (Grid Security Infrastructure). </p>
<p> A client implementation which communicates with a server which supports the DCAU extension should delegate a limited credential set (using the GSS_C_DELEG_FLAG and GSS_C_GLOBUS_LIMITED_DELEG_PROXY_FLAG flags to gss_init_sec_context()). If delegation is not performed, the client MUST request that DCAU be disable by requesting DCAU N, or the server will be unable to perform the default of DCAU A as described by this document. </p>
<p> When DCAU mode &#8216;A&#8217; or &#8216;S&#8217; is used, a separate security context is established on each data channel. The context is established by performing the GSSAPI handshake with the active-DTP calling gss_init_sec_context() and the passive-DTP calling gss_accept_sec_context(). No delegation need be done on these data channels. </p>
<p> Data channel protection via the PROT command MUST always be used in conjunction with the DCAU A or DCAU S commands. If a PROT level is set, then messages will be wrapped according to RFC 2228 Appendix I using the contexts established on each data channel. Tokens transferred over the data channels when either PROT or DCAU is used are not framed in any way when using GSI. (When implementing this specification with other GSSAPI mechanisms, a 4 byte, big endian, binary token length should procede all tokens). </p>
<p> If the DCAU mode or the PROT mode is changed between file transfers when caching data channels in extended block mode, all open data channels must be closed. This is because the GSI implementation does not support changing levels of protection on an existing connection. </p>
<h2>Index</h2>
