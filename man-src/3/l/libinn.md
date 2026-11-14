---
title: "libinn(3)"
name: "libinn"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libinn/"
---

<h2>NAME</h2>

 libinn - InterNetNews library routines

<h2>SYNOPSIS</h2>

 <pre><code>
#include "inn/libinn.h"
char *
GenerateMessageID(domain)
char *domain;
void
    HeaderCleanFrom(from) char *from;
char *
HeaderFind(Article, Header, size)
char *Article;
char *Header;
int size;
FILE *
CAopen(FromServer, ToServer)
FILE *FromServer;
FILE *ToServer;
FILE *
CAlistopen(FromServer, ToServer, request)
FILE *FromServer;
FILE *ToServer;
char *request;
void CAclose() struct _DDHANDLE *DDstart(FromServer, ToServer)
FILE *FromServer;
FILE *ToServer;
void
    DDcheck(h, group)
        DDHANDLE *h;
char *group;
char *
DDend(h)
DDHANDLE *h;
void
    close_on_exec(fd, flag) int fd;
bool flag;
int nonblocking(fd, flag)
int fd;
bool flag;
bool
    inn_lock_file(fd, type, flag) int fd;
LOCKTYPE type;
bool block;
char *
GetFQDN(domain)
char *domain;
char *
GetModeratorAddress(FromServer, ToServer, group, moderatormailer)
FILE *FromServer;
FILE *ToServer;
char *group;
char *moderatormailer;
int GetResourceUsage(usertime, systime)
double *usertime;
double *systime;
int NNTPlocalopen(FromServerp, ToServerp, errbuff, len)
FILE **FromServerp;
FILE **ToServerp;
char *errbuff;
size_t len;
int NNTPremoteopen(port, FromServerp, ToServerp, errbuff, len)
int port;
FILE **FromServerp;
FILE **ToServerp;
char *errbuff;
size_t len;
int NNTPconnect(host, port, FromServerp, ToServerp, errbuff, len)
char *host;
int port;
FILE **FromServerp;
FILE **ToServerp;
char *errbuff;
size_t len;
int NNTPsendarticle(text, ToServer, Terminate)
char *text;
FILE *ToServer;
int Terminate;
int NNTPsendpassword(server, FromServer, ToServer)
char *server;
FILE *FromServer;
FILE *ToServer;
void
    Radix32(value, p) unsigned long value;
char *p;
char *
ReadInFile(name, Sbp)
char *name;
struct stat *Sbp;
char *
ReadInDescriptor(fd, Sbp)
int fd;
struct stat *Sbp;
HASH
    HashMessageID(MessageID)
        const char *MessageID;
</code></pre>

<h2>DESCRIPTION</h2>

 <i>Libinn</i> is a library of utility routines for manipulating Usenet articles and related data. 

 <i>GenerateMessageID</i> uses the current time, process-ID, and fully-qualified domain name, which is passed as an argument and used if local host can not be resolved or it is different from ``domain'' set in <i>inn.conf</i>, to create a Message-ID header that is highly likely to be unique. The returned value points to static space that is reused on subsequent calls. 

 <i>HeaderCleanFrom</i> removes the extraneous information from the value of a ``From'' or ``Reply-To'' header and leaves just the official mailing address. In particular, the following transformations are made to the <i>from</i> parameter:
<dl>
<dt>
<dd> <pre>
address          --&gt;  address
address (stuff)  --&gt;  address
stuff &lt;address&gt;  --&gt;  address
</pre></dl>
 The transformations are simple, based on RFC 5536 which limits the format of the header. 

 <i>HeaderFind</i> searches through <i>Article</i> looking for the specified <i>Header</i>. <i>Size</i> should be the length of the header name. It returns a pointer to the value of the header, skipping leading whitespace, or NULL if the header cannot be found. <i>Article</i> should be a standard C string containing the text of the article; the end of the headers is indicated by a blank line --- two consecutive \n characters. 

 <i>CAopen</i> and <i>CAclose</i> provide news clients with access to the active file; the ``CA'' stands for <i>C</i>lient <i>A</i>ctive. <i>CAopen</i> opens the <i>active</i> file for reading. It returns a pointer to an open FILE, or NULL on error. If a local or NFS-mounted copy exists, <i>CAopen</i> will use that file. The <i>FromServer</i> and <i>ToServer</i> parameters should be FILE's connected to the NNTP server for input and output, respectively. See <i>NNTPremoteopen</i> or <i>NNTPlocalopen</i>, below. If either parameter is NULL, then <i>CAopen</i> will just return NULL if the file is not locally available. If they are not NULL, <i>CAopen</i> will use them to query the NNTP server using the ``list'' command to make a local temporary copy. 

 The <i>CAlistopen</i> sends a ``list'' command to the server and returns a temporary file containing the results. The <i>request</i> parameter, if not NULL, will be sent as an argument to the command. Unlike <i>CAopen</i>, this routine will never use a locally-available copy of the active file. 

 <i>CAclose</i> closes the active file and removes any temporary file that might have been created by <i>CAopen</i> or <i>CAlistopen</i>. 

 <i>close_on_exec</i> can make a descriptor ``close-on-exec'' so that it is not shared with any child processes. If the flag is non-zero, the file is so marked; if zero, the ``close-on-exec'' mode is cleared. 

 <i>DDstart</i>, <i>DDcheck</i>, and <i>DDend</i> are used to set the Distribution header; the ``DD'' stands for <i>D</i>efault <i>D</i>istribution. The <i>distrib.pats</i> file is consulted to determine the proper value for the Distribution header after all newsgroups have been checked. <i>DDstart</i> begins the parsing. It returns a pointer to an opaque handle that should be used on subsequent calls. The <i>FromServer</i> and <i>ToServer</i> parameters should be FILE's connected to the NNTP server for input and output, respectively. If either parameter is NULL, then an empty default will ultimately be returned if the file is not locally available. 

 <i>DDcheck</i> should be called with the handle, <i>h</i>, returned by <i>DDstart</i> and a newgroups, <i>group</i>, to check. It can be called as often as necessary. 

 <i>DDend</i> releases any state maintained in the handle and returns an allocated copy of the text that should be used for the Distribution header. 

 <i>nonblocking</i> enables (if <i>flag</i> is non-zero) or disables (if <i>flag</i> is zero) non-blocking I/O on the indicated descriptor. It returns -1 on failure or zero on success. 

 <i>inn_lock_file</i> tries to lock the file descriptor <i>fd</i>. If <i>block</i> is true it will block until the lock can be made, otherwise it will return false if the file cannot be locked. <i>type</i> is one of: INN_LLOCK_READ, INN_LLOCK_WRITE, or INN_LOCK_UNLOCK. It returns false on failure or true on success. 

 <i>GetFQDN</i> returns the fully-qualified domain name of the local host. <i>Domain</i> is used if local host can not be resolved. The returned value points to static space that is reused on subsequent calls, or NULL on error. 

 <i>GetModeratorAddress</i> returns the mailing address of the moderator for specified <i>group</i> or NULL on error. <i>Moderatormailer</i> is used as its address, if there is no matched moderator. See <i><a HREF="/docs/linux/man/5-moderators/">moderators</a></i>(5) for details on how the address is determined. <i>GetModeratorAddress</i> does no checking to see if the specified group is actually moderated. The returned value points to static space that is reused on subsequent calls. The <i>FromServer</i> and <i>ToServer</i> parameters should be FILE's connected to the NNTP server for input and output, respectively. If either of these parameters is NULL, then an attempt to get the list from a local copy is made. 

 <i>GetResourceUsage</i> fills in the <i>usertime</i> and <i>systime</i> parameters with the total user and system time used by the current process and any children it may have spawned. If <i>&lt;HAVE_GETRUSAGE in include/config.h&gt;</i> is defined, it gets the values by doing a <i><a HREF="/docs/linux/man/2-getrusage/">getrusage</a></i>(2) system call; otherwise it calls <i><a HREF="/docs/linux/man/2-times/">times</a></i>(2). It returns -1 on failure, or zero on success. 

 <i>NNTPlocalopen</i> opens a connection to the private port of an InterNetNews server running on the local host, if <i>&lt;HAVE_UNIX_DOMAIN_SOCKETS in include/config.h&gt;</i> is defined. It returns -1 on failure, or zero on success. <i>FromServerp</i> and <i>ToServerp</i> will be filled in with FILE's which can be used to communicate with the server. <i>Errbuff</i> can either be NULL or a pointer to a buffer at least 512 bytes long. If not NULL, and the server refuses the connection, then it will be filled in with the text of the server's reply. <i>Len</i> should be the length of the buffer. This routine is not for general use. If <i>&lt;HAVE_UNIX_DOMAIN_SOCKETS in include/config.h&gt;</i> is not defined, this is a stub routine, for compatibility with systems that have Unix-domain stream sockets. It always returns -1. 

 <i>NNTPremoteopen</i> does the same except that it uses ``innconf-&gt;server'' as the local server, and opens a connection to the <i>port</i>. Any client program can use this routine. It returns -1 on failure, or zero on success. 

 <i>NNTPconnect</i> is the same as <i>NNTPremoteopen</i> except that the desired host is given as the <i>host</i> parameter. 

 <i>NNTPsendarticle</i> writes <i>text</i> on <i>ToServer</i> using NNTP conventions for line termination. The text should consist of one or more lines ending with a newline. If <i>Terminate</i> is non-zero, then the routine will also write the NNTP data-termination marker on the stream. It returns -1 on failure, or zero on success. 

 <i>NNTPsendpassword</i> sends authentication information to an NNTP server by finding the appropriate entry in the <i>passwd.nntp</i> file. <i>Server</i> contains the name of the host; ``innconf-&gt;server'' will be used if <i>server</i> is NULL. <i>FromServer</i> and <i>ToServer</i> should be FILE's that are connected to the server. No action is taken if the specified host is not listed in the password file. 

 <i>Radix32</i> converts the number in <i>value</i> into a radix-32 string into the buffer pointed to by <i>p</i>. The number is split into five-bit pieces and each pieces is converted into a character using the alphabet <i>0..9a..v</i> to represent the numbers 0..32. Only the lowest 32 bits of <i>value</i> are used, so <i>p</i> need only point to a buffer of eight bytes (seven characters and the trailing \0). 

 <i>ReadInFile</i> reads the file named <i>name</i> into allocated memory, appending a terminating \0 byte. It returns a pointer to the space, or NULL on error. If <i>Sbp</i> is not NULL, it is taken as the address of a place to store the results of a <i><a HREF="/docs/linux/man/2-stat/">stat</a></i>(2) call. 

 <i>ReadInDescriptor</i> performs the same function as <i>ReadInFile</i> except that <i>fd</i> refers to an already-open file. 

 <i>HashMessageID</i> returns hashed message-id using MD5.

<h2>EXAMPLES</h2>

<dl>
<dt>
<dd> <pre><code>
char *p;
char *Article;
char buff[256], errbuff[256];
FILE *F;
FILE *ToServer;
FILE *FromServer;
int port = 119;
if ((p = HeaderFind(Article, "From", 4)) == NULL)
    Fatal("Can't find From line");
(void)strcpy(buff, p);
HeaderCleanFrom(buff);
if ((F = CAopen(FromServer, ToServer)) == NULL)
    Fatal("Can't open active file");
/* Don't pass the file on to our children. */
close_on_exec(fileno(F), 1);
/* Make a local copy. */
p = ReadInDescriptor(fileno(F), (struct stat *)NULL);
/* Close the file. */
CAclose();
if (NNTPremoteopen(port, &amp;FromServer, &amp;ToServer, errbuff) &lt; 0)
    Fatal("Can't connect to server");
if ((p = GetModeratorAddress("comp.sources.unix")) == NULL)
    Fatal("Can't find moderator's address");
</code></pre></dl>

<h2>HISTORY</h2>

 Written by Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. This is revision 9668, dated 2014-08-30.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-active/">active</a>(5), <a HREF="//www.systutorials.com/docs/linux/man/3z-dbz/">dbz</a>(3z), <a HREF="/docs/linux/man/5-inn-conf/">inn.conf</a>(5), <a HREF="/docs/linux/man/3-inndcomm/">inndcomm</a>(3), <a HREF="/docs/linux/man/5-moderators/">moderators</a>(5), <a HREF="/docs/linux/man/5-passwd-nntp/">passwd.nntp</a>(5). 

<h2>Index</h2>


