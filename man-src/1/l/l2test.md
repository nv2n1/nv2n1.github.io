---
title: "l2test(1)"
name: "l2test"
section: "1"
letter: "l"
url: "/docs/linux/man/1-l2test/"
description: "l2test – L2CAP testing tool"
---

<h2 class="name">NAME</h2>
<p> l2test &#8211; L2CAP testing tool </p>
<h2>DESCRIPTION</h2>
<p> l2test &#8211; L2CAP testing tool Usage:</p>
<dl>
<dt>
<dd> l2test &lt;mode&gt; [options] [bdaddr]</dl>
<h3>Modes:</h3>
<dl>
<dt> <code>-r</code> listen and receive</p>
<dt> <code>-w</code> listen and send</p>
<dt> <code>-d</code> listen and dump incoming data</p>
<dt> <code>-x</code> listen, then send, then dump incoming data</p>
<dt> <code>-t</code> listen, then send and receive at the same time</p>
<dt> <code>-q</code> connect, then send and receive at the same time</p>
<dt> <code>-s</code> connect and send</p>
<dt> <code>-u</code> connect and receive</p>
<dt> <code>-n</code> connect and be silent</p>
<dt> <code>-y</code> connect, then send, then dump incoming data</p>
<dt> <code>-c</code> connect, disconnect, connect, &#8230;</p>
<dt> <code>-m</code> multiple connects</p>
<dt> <code>-p</code> trigger dedicated bonding</p>
<dt> <code>-z</code> information request</dl>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> [-b bytes] [-i device] [-P psm] [-J cid] [-I imtu] [-O omtu] [-L seconds] enable SO_LINGER [-W seconds] enable deferred setup [-B filename] use data packets from file [-N num] send num frames (default = infinite) [-C num] send num frames before delay (default = 1) [-D milliseconds] delay after sending num frames (default = 0) [-K milliseconds] delay before receiving (default = 0) [-g milliseconds] delay before disconnecting (default = 0) [-X mode] l2cap mode (help for list, default = basic) [-a policy] chan policy (help for list, default = bredr) [-F fcs] use CRC16 check (default = 1) [-Q num] Max Transmit value (default = 3) [-Z size] Transmission Window size (default = 63) [-Y priority] socket priority [-H size] Maximum receive buffer size [-R] reliable mode [-G] use connectionless channel (datagram) [-U] use sock stream [-A] request authentication [-E] request encryption [-S] secure connection [-M] become master [-T] enable timestamps [-V type] address type (help for list, default = bredr) [-e seq] initial sequence value (default = 0)</dl>
<h3>Usage:</h3>
<dl>
<dt>
<dd>
<dd>l2test &lt;mode&gt; [options] [bdaddr]</dl>
<h3>Modes:</h3>
<dl>
<dt> <code>-r</code> listen and receive</p>
<dt> <code>-w</code> listen and send</p>
<dt> <code>-d</code> listen and dump incoming data</p>
<dt> <code>-x</code> listen, then send, then dump incoming data</p>
<dt> <code>-t</code> listen, then send and receive at the same time</p>
<dt> <code>-q</code> connect, then send and receive at the same time</p>
<dt> <code>-s</code> connect and send</p>
<dt> <code>-u</code> connect and receive</p>
<dt> <code>-n</code> connect and be silent</p>
<dt> <code>-y</code> connect, then send, then dump incoming data</p>
<dt> <code>-c</code> connect, disconnect, connect, &#8230;</p>
<dt> <code>-m</code> multiple connects</p>
<dt> <code>-p</code> trigger dedicated bonding</p>
<dt> <code>-z</code> information request</p>
<dt>
<dd> [-b bytes] [-i device] [-P psm] [-J cid] [-I imtu] [-O omtu] [-L seconds] enable SO_LINGER [-W seconds] enable deferred setup [-B filename] use data packets from file [-N num] send num frames (default = infinite) [-C num] send num frames before delay (default = 1) [-D milliseconds] delay after sending num frames (default = 0) [-K milliseconds] delay before receiving (default = 0) [-g milliseconds] delay before disconnecting (default = 0) [-X mode] l2cap mode (help for list, default = basic) [-a policy] chan policy (help for list, default = bredr) [-F fcs] use CRC16 check (default = 1) [-Q num] Max Transmit value (default = 3) [-Z size] Transmission Window size (default = 63) [-Y priority] socket priority [-H size] Maximum receive buffer size [-R] reliable mode [-G] use connectionless channel (datagram) [-U] use sock stream [-A] request authentication [-E] request encryption [-S] secure connection [-M] become master [-T] enable timestamps [-V type] address type (help for list, default = bredr) [-e seq] initial sequence value (default = 0) </p>
</dl>
<h2>Index</h2>
