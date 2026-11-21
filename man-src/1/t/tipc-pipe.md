---
title: "tipc-pipe(1)"
name: "tipc-pipe"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tipc-pipe/"
---

<h2>NAME</h2>

 tipc-PIPE - simple client/server

<h2>SYNOPSIS</h2>

 tipc-pipe &lt;options&gt; [address 1] [address 2] 

<h2>DESCRIPTION</h2>

 tipc-pipe acts as a netcat like program for tipc. It is used for reading and writing network connections using tipc 

<h3>Options</h3>

 default values are marked with '*' 

<dl>
<dt>-h | --help
</dt><dd> show this help 
</dd><dt>-l
</dt><dd> run in server mode, accept multiple connections 
</dd><dt>-s
</dt><dd> run in single connection server mode, exit on connection close default mode is client mode 
</dd><dt>--sock_type *SOCK_STREAM | SOCK_DGRAM | SOCK_RDM | SOCK_SEQPACKET
</dt><dd> 
</dd><dt>--server_type *1000|&lt;n&gt;
</dt><dd> 
</dd><dt>--addr_type TIPC_ADDR_NAMESEQ | TIPC_ADDR_MCAST | *TIPC_ADDR_NAME
</dt><dd> For TIPC_ADDR_NAME only address 1 is used. For TIPC_ADDR_NAMESEQ or TIPC_ADDR_MCAST address 1 and address 2 are used. 
</dd><dt>--delay *0|&lt;ms&gt;
</dt><dd> Defines data reading and writing delay in ms. 
</dd><dt>--data_num *0|&lt;count&gt;
</dt><dd> Generates defined number of sample data and sends is. 
</dd><dt>--data_size *0
</dt><dd> Generates packets of defined size when data_num is defined. 
</dd><dt>--data_check
</dt><dd> Check sequence numbers in received data, generated with option data_num. 
</dd><dt>--buf_size *66000|&lt;n&gt;
</dt><dd> I/O buffer size (see TIPC_MAX_USER_MSG_SIZE). 
</dd><dt>--wait_peer *0
</dt><dd> Wait for peer published state before communication. 
</dd><dt>--top
</dt><dd> run topology client 
</dd><dt>--replay
</dt><dd> force connectionless server send input to last connected client 
</dd></dl>

<h3>Short Options</h3>

 

<dl>
<dt>--rdm
</dt><dd> sock_type = SOCK_RDM 
</dd><dt>--pct
</dt><dd> sock_type = SOCK_PACKET 
</dd><dt>--stm
</dt><dd> * sock_type = SOCK_STREAM 
</dd><dt>--sqp
</dt><dd> sock_type = SOCK_SEQPACKET 
</dd><dt>--nam
</dt><dd> * addr_type = TIPC_ADDR_NAME 
</dd><dt>--mc
</dt><dd> addr_type = TIPC_ADDR_MCAST or TIPC_ADDR_NAMESEQ 
</dd><dt>--id
</dt><dd> addr_type = TIPC_ADDR_ID 
</dd></dl>

<h2>EXAMPLES</h2>

 

 SOCK_STREAM single connection server with address zero and client: 
&nbsp;<wbr>tipc-pipe -s | tee input 
&nbsp;<wbr>date | tipc-pipe 

 SOCK_RDM server with address 123 and client: 
&nbsp;<wbr>tipc-pipe --rdm --replay -l 123 
&nbsp;<wbr>tipc-pipe --rdm 123 

 Start topology client for all addresses of specified optional server type 
&nbsp;<wbr>tipc-pipe --server_type=1000 --top -- 0 -1 

 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-tipc-config/">tipc-config</a>(1) 

<h2>AUTHORS</h2>

 <i>Constantine Shulyupin const [at] makelinux.com</i> 

<h2>REPORTING BUGS</h2>

 Report ls bugs to <i>tipc-discussion [at] lists.sourceforge.net</i>
