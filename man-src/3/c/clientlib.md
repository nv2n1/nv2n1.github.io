---
title: "clientlib(3)"
name: "clientlib"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clientlib/"
---

<h2>NAME</h2>

 clientlib - NNTP clientlib part of InterNetNews library

<h2>SYNOPSIS</h2>

 <pre><code>
extern FILE *ser_rd_fp;
extern FILE *ser_wr_fp;
extern char ser_line[];
char *
getserverbyfile(file)
char *file;
int server_init(host)
char *host;
int handle_server_response(response, host)
int reponse;
char *host;
void
    put_server(text) char *text;
int get_server(buff, buffsize)
char *buff;
int buffsize;
void close_server()
</code></pre>

<h2>DESCRIPTION</h2>

 The routines described in this manual page are part of the InterNetNews library, <i><a HREF="/docs/linux/man/3-libinn/">libinn</a></i>(3). They are replacements for the ``clientlib'' part of the NNTP distribution, and are intended to be used in building programs like <i>rrn</i>. 

 <i>Getserverbyfile</i> calls <i>GetConfigValue</i> to get the name of the local NNTP server. It returns a pointer to static space. The <i>file</i> parameter is ignored. 

 <i>Server_init</i> opens a connect to the NNTP server at the specified <i>host</i>. It returns the server's response code or -1 on error. If a connection was made, then <i>ser_rd_fp</i> and <i>ser_wr_fp</i> can be used to read from and write to the server, respectively, and <i>ser_line</i> will contain the server's response. <i>Ser_line</i> can also be used in other routines. 

 <i>Handle_server_response</i> decodes the <i>response</i>, which comes from the server on <i>host.</i> If the client is authorized, it returns 0. A client that is only allowed to read is authorized, but <i>handle_server_response</i> will print a message on the standard output. If the client is not authorized to talk to the server, then a message is printed and the routine returns -1. 

 <i>Put_server</i> sends the text in <i>buff</i> to the server, adding the necessary NNTP line terminators, and flushing the I/O buffer. 

 <i>Get_server</i> reads a line of text from the server into <i>buff</i>, reading at most <i>buffsize</i> characters. Any trailing \r\n terminators are stripped off. <i>Get_server</i> returns -1 on error. 

 <i>Close_server</i> sends a ``quit'' command to the server and closes the connection.

<h2>HISTORY</h2>

 Written by Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. This is revision 42, dated 1997-08-04.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-libinn/">libinn</a>(3). 

<h2>Index</h2>


