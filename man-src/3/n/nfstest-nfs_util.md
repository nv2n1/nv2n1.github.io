---
title: "nfstest-nfs_util(3)"
name: "nfstest-nfs_util"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfstest-nfs_util/"
description: "nfstest.nfs_util – NFS utilities module"
---

<p>nfstest.nfs_util &#8211; NFS utilities module</p>
<h2>Description</h2>
<p>Provides a set of tools for testing NFS including methods for starting a packet trace, stopping the packet trace and then open the packet trace for analysis. It also provides a mechanism to enable NFS/RPC kernel debug and saving the log messages for further analysis. </p>
<p> Furthermore, methods for finding specific NFSv4 operations within the packet trace are also included.</p>
<h2>Classes</h2>
<h3>class NFSUtil(nfstest.host.Host)</h3>
<pre>NFSUtil object
NFSUtil() -&gt; New NFSUtil object
Usage:
 from nfstest.nfs_util import NFSUtil
 # Create object for local host
 x = NFSUtil()
 # Start packet trace
 x.trace_start()
 # Stop packet trace
 x.trace_stop()
 # Open packet trace
 x.trace_open()
 # Enable NFS kernel debug
 x.nfs_debug_enable(nfsdebug='all'):
 # Stop NFS kernel debug
 x.nfs_debug_reset()
<code>Methods defined here:</code>
---------------------
<code>__del__(self)</code>
Destructor
Gracefully stop the packet trace and unreference all client
objects
<code>__init__(self, **kwargs)</code>
Constructor
Initialize object's private data.
<dl><dl><dt><code>rpcdebug:</code>
</dt><dd>Set RPC kernel debug flags and save log messages [default: '']
</dd><dt><code>nfsdebug:</code>
</dt><dd>Set NFS kernel debug flags and save log messages [default: '']
</dd><dt><code>dbgname:</code>
</dt><dd>Base name for log messages files to create [default: 'dbgfile']
</dd><dt><code>tracename:</code>
</dt><dd>Base name for trace files to create [default: 'tracefile']
</dd><dt><code>trcdelay:</code>
</dt><dd>Seconds to delay before stopping packet trace [default: 0.0]
</dd><dt><code>notrace:</code>
</dt><dd>Debug option so a trace is not actually started [default: False]
</dd><dt><code>tcpdump:</code>
</dt><dd>Tcpdump command [default: '/usr/sbin/tcpdump']
</dd><dt><code>messages:</code>
</dt><dd>Location of file for system messages [default: '/var/log/messages']
</dd><dt><code>tmpdir:</code>
</dt><dd>Temporary directory where trace files are created [default: '/tmp']
</dd><dt><code>tbsize:</code>
</dt><dd>Capture buffer size in kB [default: 50000]
</dd></dl></dl>
<code>create_host(self, host, **kwargs)</code>
Create client host object and set defaults.
<code>find_exchange_id(self, **kwargs)</code>
Find the call and its corresponding reply for the NFSv4 EXCHANGE_ID
going to the server specified by the ipaddr and port.
<dl><dl><dt><code>ipaddr:</code>
</dt><dd>Destination IP address [default: self.server]
</dd><dt><code>port:</code>
</dt><dd>Destination port [default: self.port]
</dd></dl></dl><dl><dt></dt><dd>Store the callback IP/TCP expression in object attribute cb_dst
Return a tuple: (pktcall, pktreply).
</dd></dl>
<code>find_getdeviceinfo(self, deviceid=None)</code>
Find the call and its corresponding reply for the NFSv4 GETDEVICEINFO
going to the server specified by the ipaddr for self.server and port
given by self.port.
<dl><dl><dt><code>deviceid:</code>
</dt><dd>Look for an specific deviceid [default: any deviceid]
</dd></dl></dl><dl><dt></dt><dd>Return a tuple: (pktcall, pktreply, dslist).
</dd></dl>
<code>find_layoutget(self, filehandle)</code>
Find the call and its corresponding reply for the NFSv4 LAYOUTGET
of the given file handle going to the server specified by the
ipaddr for self.server and port given by self.port.
Return a tuple: (layoutget, layoutget_res, loc_body).
<code>find_layoutrecall(self, status=0)</code>
Find NFSv4 CB_LAYOUTRECALL call and return its reply.
The reply must also match the given status.
<code>find_nfs_op(self, op, ipaddr, port=None, match='', status=0, src_ipaddr=None, maxindex=None, call_only=False)</code>
Find the call and its corresponding reply for the specified NFSv4
operation going to the server specified by the ipaddr and port.
The reply must also match the given status.
<dl><dl><dt><code>op:</code>
</dt><dd>NFS operation to find
</dd><dt><code>ipaddr:</code>
</dt><dd>Destination IP address
</dd><dt><code>port:</code>
</dt><dd>Destination port [default: any destination port]
</dd><dt><code>match:</code>
</dt><dd>Match string to include [default: '']
</dd><dt><code>status:</code>
</dt><dd>Match the status of the operation [default: 0]
</dd><dt><code>src_ipaddr:</code>
</dt><dd>Source IP address [default: any IP address]
</dd><dt><code>maxindex:</code>
</dt><dd>The match fails if packet index hits this limit [default: no limit]
</dd><dt><code>call_only:</code>
</dt><dd>Find the call only [default: False]
</dd></dl></dl><dl><dt></dt><dd>Return a tuple: (pktcall, pktreply).
</dd></dl>
<code>find_open(self, **kwargs)</code>
Find the call and its corresponding reply for the NFSv4 OPEN of the
given file going to the server specified by the ipaddr and port.
<dl><dl><dt><code>filename:</code>
</dt><dd>Find open call and reply for this file [default: None]
</dd><dt><code>claimfh:</code>
</dt><dd>Find open call and reply for this file handle using CLAIM_FH
[default: None]
</dd><dt><code>ipaddr:</code>
</dt><dd>Destination IP address [default: self.server]
</dd><dt><code>port:</code>
</dt><dd>Destination port [default: self.port]
</dd><dt><code>deleg_type:</code>
</dt><dd>Expected delegation type on reply [default: None]
</dd><dt><code>deleg_stateid:</code>
</dt><dd>Delegation stateid expected on call in delegate_cur_info [default: None]
</dd><dt><code>fh:</code>
</dt><dd>Find open call and reply for this file handle when using
deleg_stateid [default: None]
</dd><dt><code>src_ipaddr:</code>
</dt><dd>Source IP address [default: any IP address]
</dd><dt><code>maxindex:</code>
</dt><dd>The match fails if packet index hits this limit [default: no limit]
</dd><dt><code>anyclaim:</code>
</dt><dd>Find open for either regular open or using delegate_cur_info [default: False]
</dd></dl></dl><dl><dt></dt><dd>Must specify either filename, claimfh or both.
Return a tuple: (filehandle, open_stateid, deleg_stateid).
</dd></dl>
<code>get_abs_offset(self, offset, ds_index=None)</code>
Get real file offset given by the (read/write) offset on the given
data server index, taking into account the type of layout
(dense/sparse), the stripe_size, first stripe index and the number
of filehandles. The layout information is taken from object
attribute layout.
<code>get_filehandle(self, ds_index)</code>
Return filehandle from the layout list of filehandles.
<code>get_freebytes(self, dir=None)</code>
Get the number of bytes available in the given directory.
It takes into account the effective user running the test.
The root user is allowed to use all the available disk space
on the device, on the other hand a regular user is allowed a
little bit less.
<code>get_stateid(self, filename)</code>
Search the packet trace for the file name given to get the OPEN
so all related state ids can be searched. A couple of object
attributes are defined, one is the correct state id that should
be used by I/O operations. The second is a dictionary table
which maps the state id to a string identifying if the state
id is an open, lock or delegation state id.
<code>nfs_debug_enable(self, **kwargs)</code>
Enable NFS debug messages.
<dl><dl><dt><code>rpcdebug:</code>
</dt><dd>Set RPC kernel debug flags and save log messages [default: self.rpcdebug]
</dd><dt><code>nfsdebug:</code>
</dt><dd>Set NFS kernel debug flags and save log messages [default: self.nfsdebug]
</dd><dt><code>dbgfile:</code>
</dt><dd>Name of log messages file to create, default is a unique name
created in the temporary directory using self.dbgname as the
base name.
</dd></dl></dl>
<code>nfs_debug_reset(self)</code>
Reset NFS debug messages.
<code>stid_str(self, stateid)</code>
Display the state id in CRC16 format
<code>trace_open(self, tracefile=None, **kwargs)</code>
Open the trace file given or the trace file started by trace_start().
All extra options are passed directly to the packet trace object.
Return the packet trace object created, the packet trace object
is also stored in the object attribute pktt.
<code>trace_start(self, tracefile=None, interface=None, capsize=None, clients=None)</code>
Start trace on interface given
<dl><dl><dt><code>tracefile:</code>
</dt><dd>Name of trace file to create, default is a unique name
created in the temporary directory using self.tracename as the
base name.
</dd><dt><code>capsize:</code>
</dt><dd>Use the -C option of tcpdump to split the trace files every
1000000*capsize bytes. See documentation for tcpdump for more
information
</dd><dt><code>clients:</code>
</dt><dd>List of Host() objects to monitor
</dd></dl></dl><dl><dt></dt><dd>Return the name of the trace file created.
</dd></dl>
<code>trace_stop(self)</code>
Stop the trace started by trace_start().
<code>verify_commit(self, ipaddr, port, filehandle, init=False)</code>
Verify commits are properly sent to the server specified by the
given ipaddr and port.
<dl><dl><dt><code>ipaddr:</code>
</dt><dd>Destination IP address of MDS or DS
</dd><dt><code>port:</code>
</dt><dd>Destination port number of MDS or DS
</dd><dt><code>filehandle:</code>
</dt><dd>Find commits for this file handle
</dd><dt><code>init:</code>
</dt><dd>Initialized test variables [default: False]
</dd></dl></dl><dl><dt></dt><dd>Return the number of commits sent to the server.
</dd></dl>
<code>verify_create_session(self, ipaddr, port, ds=False, nocreate=False, ds_index=None, exchid_status=0, cs_status=0)</code>
Verify initial connection to the metadata server(MDS)/data server(DS).
Verify if EXCHANGE_ID, CREATE_SESSION, RECLAIM_COMPLETE,
GETATTR asking for FATTR4_LEASE_TIME, and GETATTR asking for
FATTR4_FS_LAYOUT_TYPES are all sent or not to the server.
<dl><dl><dt><code>ipaddr:</code>
</dt><dd>Destination IP address of MDS or DS
</dd><dt><code>port:</code>
</dt><dd>Destination port number of MDS or DS
</dd><dt><code>ds:</code>
</dt><dd>True if ipaddr/port defines a DS, otherwise MDS [default: False]
</dd><dt><code>nocreate:</code>
</dt><dd>True if expecting the client NOT to send EXCHANGE_ID,
CREATE_SESSION, and RECLAIM_COMPLETE. Otherwise, verify all
these operations are sent by the client [default: False]
</dd><dt><code>ds_index:</code>
</dt><dd>DS index used for displaying purposes only [default: None]
</dd><dt><code>exchid_status:</code>
</dt><dd>Expected status for EXCHANGE_ID [default: 0]
</dd><dt><code>cs_status:</code>
</dt><dd>Expected status for CREATE_SESSION [default: 0]
</dd></dl></dl><dl><dt></dt><dd>Return the sessionid and it is also stored in the object
attribute sessionid.
</dd></dl>
<code>verify_io(self, iomode, stateid, ipaddr=None, port=None, src_ipaddr=None, filehandle=None, ds_index=None, init=False, maxindex=None, pattern=None)</code>
Verify I/O is sent to the server specified by the ipaddr and port.
<dl><dl><dt><code>iomode:</code>
</dt><dd>Verify reads (iomode == 1) or writes (iomode == 2)
</dd><dt><code>stateid:</code>
</dt><dd>Expected stateid to use in all I/O requests
</dd><dt><code>ipaddr:</code>
</dt><dd>Destination IP address of MDS or DS
[default: do not match destination]
</dd><dt><code>port:</code>
</dt><dd>Destination port number of MDS or DS
[default: do not match destination port]
</dd><dt><code>src_ipaddr:</code>
</dt><dd>Source IP address of request
[default: do not match source]
</dd><dt><code>filehandle:</code>
</dt><dd>Find I/O for this file handle. This option is used when
verifying I/O sent to the MDS
[default: use filehandle given by ds_index]
</dd><dt><code>ds_index:</code>
</dt><dd>Data server index. This option is used when verifying I/O sent
to the DS -- filehandle is taken from x.layout for this index
[default: None]
</dd><dt><code>init:</code>
</dt><dd>Initialized test variables [default: False]
</dd><dt><code>maxindex:</code>
</dt><dd>The match fails if packet index hits this limit [default: no limit]
</dd><dt><code>pattern:</code>
</dt><dd>Data pattern to compare [default: default data pattern]
</dd></dl></dl><dl><dt></dt><dd>Return the number of I/O operations sent to the server.
</dd></dl>
<code>verify_layoutcommit(self, filehandle, filesize)</code>
Verify layoutcommit is properly sent to the server specified by
the ipaddr for self.server and port given by self.port.
Verify a GETATTR asking for file size is sent within the same
compound as the LAYOUTCOMMIT.
Verify GETATTR returns correct size for the file.
<dl><dl><dt><code>filehandle:</code>
</dt><dd>Find layoutcommit for this file handle
</dd><dt><code>filesize:</code>
</dt><dd>Expected size of file
</dd></dl></dl>
<code>verify_layoutget(self, filehandle, iomode, riomode=None, status=0, offset=None, length=None)</code>
Verify the client sends a LAYOUTGET for the given file handle.
<dl><dl><dt><code>filehandle:</code>
</dt><dd>Find LAYOUTGET for this file handle
</dd><dt><code>iomode:</code>
</dt><dd>Expected I/O mode for LAYOUTGET call
</dd><dt><code>riomode:</code>
</dt><dd>Expected I/O mode for LAYOUTGET reply if specified, else verify
reply I/O mode is equal to call I/O mode if iomode == 2.
If iomode == 1, the reply I/O mode could be equal to 1 or 2
</dd><dt><code>status:</code>
</dt><dd>Expected status for LAYOUTGET reply [default: 0]
</dd><dt><code>offset:</code>
</dt><dd>Expected layout range for LAYOUTGET reply [default: None]
</dd><dt><code>length:</code>
</dt><dd>Expected layout range for LAYOUTGET reply [default: None]
</dd></dl></dl><dl><dt></dt><dd>If both offset and length are not given, verify LAYOUTGET reply
should be a full layout [0, NFS4_UINT64_MAX]. If only one is
provided the following defaults are used: offset = 0,
length = NFS4_UINT64_MAX.
Layout information is stored in the object attribute layout.
Return a tuple: (layoutget, layoutget_res, loc_body).
</dd></dl>
<code>verify_stripe(self, offset, size, ds_index)</code>
Verify if read/write is sent to the correct data server according
to stripe size, first stripe index and the number of filehandles.
The layout information is taken from object attribute layout.
<dl><dl><dt><code>offset:</code>
</dt><dd>Real file offset
</dd><dt><code>size:</code>
</dt><dd>I/O size
</dd><dt><code>ds_index:</code>
</dt><dd>Data server index
</dd></dl></dl><dl><dt></dt><dd>Return True if stripe is correctly verified, False otherwise.
</dd></dl>
<code>Static methods defined here:</code>
----------------------------
<code>bitmap_str(bitmap, count, bmap, blist)</code>
Return the string representation of bitmap.
<dl><dl><dt><code>bitmap:</code>
</dt><dd>Bitmap to convert
</dd><dt><code>count:</code>
</dt><dd>Number of occurrences of bitmap
</dd><dt><code>bmap:</code>
</dt><dd>Dictionary mapping the bits to strings
</dd><dt><code>blist:</code>
</dt><dd>List of all possible bit combinations
</dd></dl></dl>
<code>iomode_str(iomode)</code>
Return a string representation of iomode.
This could be run as an instance or class method.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-nfstest-host/">nfstest.host</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs4_const/">packet.nfs.nfs4_const</a>(3),</code> <code><a href="/docs/linux/man/3-packet-pktt/">packet.pktt</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
