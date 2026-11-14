---
title: "libstorage(3)"
name: "libstorage"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libstorage/"
description: "libstorage – routines for managing INN storage"
---

<h2 class="name">NAME</h2>
<p> libstorage &#8211; routines for managing INN storage </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;inn/storage.h&gt;
typedef enum {
    RETR_ALL,
    RETR_HEAD,
    RETR_BODY,
    RETR_STAT
} RETRTYPE;
typedef enum {
    SM_RDWR,
    SM_PREOPEN
} SMSETUP;
typedef unsigned char STORAGECLASS;
typedef unsigned char STORAGETYPE;
typedef struct token {
    STORAGETYPE type;
    STORAGECLASS class;
    char token[STORAGE_TOKEN_LENGTH];
} TOKEN;
typedef struct {
    unsigned char type;
    const char *data;
    struct iovec *iov;
    int iovcnt;
    size_t len;
    unsigned char nextmethod;
    void *private;
    time_t arrived;
    time_t expires;
    char *groups;
    int groupslen;
    TOKEN *token;
} ARTHANDLE;
typedef enum {
    SELFEXPIRE,
    SMARTNGNUM,
    EXPENSIVESTAT
} PROBETYPE;
typedef enum {
    SM_ALL,
    SM_HEAD,
    SM_CANCELLEDART
} FLUSHTYPE;
struct artngnum {
    char *groupname;
    ARTNUM artnum;
};
bool IsToken(const char *text);
char *TokenToText(const TOKEN token);
TOKEN TextToToken(const char *text);
bool SMsetup(SMSETUP type, void *value);
bool SMinit(void);
TOKEN SMstore(const ARTHANDLE article);
ARTHANDLE *SMretrieve(const TOKEN token, const RETRTYPE amount);
ARTHANDLE *SMnext(const ARTHANDLE *article, const RETRTYPE amount);
void SMfreearticle(ARTHANDLE *article);
bool SMcancel(TOKEN token);
bool SMprobe(PROBETYPE type, TOKEN *token, void *value);
void SMprintfiles(FILE *file, TOKEN token, char **xref, int ngroups);
bool SMflushcacheddata(FLUSHTYPE type);
char *SMexplaintoken(const TOKEN token);
void SMshutdown(void);
int SMerrno;
char *SMerrorstr;
#include &lt;inn/ov.h&gt;
#define OV_NOSPACE ...
typedef enum {
    OVSPACE,
    OVSORT,
    OVCUTOFFLOW,
    OVGROUPBASEDEXPIRE,
    OVSTATICSEARCH,
    OVSTATALL,
    OVCACHEKEEP,
    OVCACHEFREE
} OVCTLTYPE;
typedef enum {
    OVNEWSGROUP,
    OVARRIVED,
    OVNOSORT
} OVSORTTYPE;
typedef enum {
    OVADDCOMPLETED,
    OVADDFAILED,
    OVADDGROUPNOMATCH
} OVADDRESULT;
bool OVopen(int mode);
bool OVctl(OVCTLTYPE type, void *val);
bool OVgroupstats(char *group, int *lo, int *hi, int *count, int *flag);
bool OVgroupadd(char *group, ARTNUM lo, ARTNUM hi, char *flag);
bool OVgroupdel(char *group);
OVADDRESULT OVadd(TOKEN token, char *data, int len, time_t arrived, time_t expires);
bool OVcancel(TOKEN token);
void *OVopensearch(char *group, int low, int high);
bool OVsearch(void *handle, ARTNUM *artnum, char **data, int *len, TOKEN *token, time_t *arrived);
void OVclosesearch(void *handle);
bool OVgetartinfo(char *group, ARTNUM artnum, TOKEN *token);
bool OVexpiregroup(char *group, int *lo, struct history *h);
typedef struct _OVGE {
    bool delayrm;
    bool usepost;
    bool quiet;
    bool keep;
    bool earliest;
    bool ignoreselfexpire;
    char *filename;
    time_t now;
    float timewarp;
} OVGE;
void OVclose(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>libstorage</code> is a library of common utility (the storage manager) routines for accessing Usenet articles and related data independent of particular storage method; this is known as the storage <font SIZE="-1">API</font>. </p>
<p> The storage manager&#8217;s function is to isolate the applications from the individual methods and make the policy decisions as to which storage method should be called to store an article. One of the core concepts in the storage <font SIZE="-1">API</font> is that articles are not manipulated using the message-ID or article number, but rather a token that uniquely identifies the article to the method that stored it. This may seem to be redundant since the message-ID already is a unique identifier for the article; however, since the storage method generates the token, it can encode all the information it needs to locate the article in the token. </p>
<p> <font SIZE="-1"><code>OV</code></font> is a common utility routines for accessing newsgroups and overview data independent of particular overview method. </p>
<p> The <font SIZE="-1"><code>OV</code></font> function is to isolate the applications from the individual methods. All articles passed through the storage <font SIZE="-1">API</font> are assumed to be in wire format. Wire format means <tt>&quot;
&quot;</tt> at the end of lines, dot-stuffed lines (that is to say <tt>&quot;.&quot;</tt> at the beginning of lines which already start with <tt>&quot;.&quot;</tt>), and <tt>&quot;.
&quot;</tt> at the end of article on <font SIZE="-1">NNTP</font> stream are not stripped. This has a performance win when transferring articles. Note that for the tradspool method, wire format can be disabled. This is just for compatibility which is needed by some old tools written for traditional spool. </p>
<p> The <code>IsToken</code> function checks to see if the text is formatted as a text token string. It returns true if formatted correctly or returns false if not. </p>
<p> The <code>TokenToText</code> function converts a token into a text string for output. </p>
<p> The <code>TextToToken</code> function converts a text string into a token. </p>
<p> The <code>SMsetup</code> function configures some parameters for use by the storage manager. <i>type</i> is one of following:</p>
<dl>
<dt>&quot;SM_RDWR&quot;</p>
<dd> Allow read/write open for storage files (default is false).</p>
<dt>&quot;SM_PREOPEN&quot;</p>
<dd> Open all storage files at startup time and keep them (default is false).</dl>
<p> <i>value</i> is the pointer which tells each type&#8217;s value. It returns true if setup is successful, or false if not. </p>
<p> The <code>SMinit</code> function calls the setup function for all of the configured methods based on <code>SMsetup</code>. This function should be called prior to all other storage <font SIZE="-1">API</font> functions which begin with <tt>&quot;SM&quot;</tt> except <code>SMsetup</code>. It returns true if initialization is successful or returns false if not. <code>SMinit</code> returns true, unless all storage methods fail initialization. </p>
<p> The <code>SMstore</code> function stores an article specified with <i>article</i>. The headers and body of the article are supplied to <code>SMstore</code> using the <i>iov</i> and <i>iovcnt</i> members of <font SIZE="-1"><code>ARTHANDLE</code></font>. (<i>data</i> and <i>private</i> are ignored by <code>SMstore</code>.) If <i>arrived</i> is specified, <code>SMstore</code> uses its value as article&#8217;s arrival time; otherwise <code>SMstore</code> uses the current time for it. <code>SMstore</code> returns the token type or returns <font SIZE="-1"><code>TOKEN_EMPTY</code></font> if the article is not stored because some error occurs or simply does not match any <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) expression in <i>storage.conf</i>. <code>SMstore</code> fails if <font SIZE="-1"><code>SM_RDWR</code></font> has not been set to true with <code>SMsetup</code>. </p>
<p> The <code>SMretrieve</code> function retrieves an article specified with <i>token</i>. <i>amount</i> is the one of following which specifies retrieving type:</p>
<dl>
<dt>&quot;RETR_ALL&quot;</p>
<dd> Retrieve the whole article.</p>
<dt>&quot;RETR_HEAD&quot;</p>
<dd> Retrieve the headers of the article.</p>
<dt>&quot;RETR_BODY&quot;</p>
<dd> Retrieve the body of the article.</p>
<dt>&quot;RETR_STAT&quot;</p>
<dd> Just check to see if the article exists.</dl>
<p> <code>SMretrieve</code> provides the article data via the <i>data</i> and <i>len</i> members of <font SIZE="-1"><code>ARTHANDLE</code></font>. (<i>iov</i> is not set by <code>SMretrieve</code>.) The data area indicated by <font SIZE="-1"><code>ARTHANDLE</code></font> should not be modified. </p>
<p> The <code>SMnext</code> function is similar in function to <code>SMretrieve</code> except that it is intended for traversing the method&#8217;s article store sequentially. To start a query, <code>SMnext</code> should be called with a <font SIZE="-1">NULL</font> pointer <font SIZE="-1"><code>ARTHANDLE</code></font>. Then <code>SMnext</code> returns <font SIZE="-1"><code>ARTHANDLE</code></font> which should be used for the next query. If a <font SIZE="-1">NULL</font> pointer <font SIZE="-1"><code>ARTHANDLE</code></font> is returned, no articles are left to be queried. If <i>data</i> of <font SIZE="-1"><code>ARTHANDLE</code></font> is <font SIZE="-1">NULL</font> pointer or <i>len</i> of <font SIZE="-1"><code>ARTHANDLE</code></font> is <tt>0</tt>, it indicates the article may be corrupted and should be cancelled by <i>SMcancel</i>. The data area indicated by <font SIZE="-1"><code>ARTHANDLE</code></font> should not be modified. </p>
<p> The <code>SMfreearticle</code> function frees all allocated memory used by <code>SMretrieve</code> and <code>SMnext</code>. If <code>SMnext</code> will be called with previously returned <font SIZE="-1"><code>ARTHANDLE</code></font>, <code>SMfreearticle</code> should not be called as <code>SMnext</code> frees allocated memory internally. </p>
<p> The <code>SMcancel</code> function removes the article specified with <i>token</i>. It returns true if cancellation is successful or returns false if not. <code>SMcancel</code> fails if <font SIZE="-1"><code>SM_RDWR</code></font> has not been set to true with <code>SMsetup</code>. </p>
<p> The <code>SMprobe</code> function checks the token on <font SIZE="-1"><code>PROBETYPE</code></font>. <i>type</i> is one of following:</p>
<dl>
<dt>&quot;SELFEXPIRE&quot;</p>
<dd> Check to see if the method of the token has self expire functionality.</p>
<dt>&quot;SMARTNGNUM&quot;</p>
<dd> Get the newsgroup name and the article number of the token.</p>
<dt>&quot;EXPENSIVESTAT&quot;</p>
<dd> Check to see whether checking the existence of an article is expensive or not.</dl>
<p> The <code>SMprintfiles</code> function shows file name or token usable by <i><a href="/docs/linux/man/8-fastrm/">fastrm</a></i>(8). </p>
<p> The <code>SMflushcacheddata</code> function flushes cached data on each storage method. <i>type</i> is one of following:</p>
<dl>
<dt>&quot;SM_HEAD&quot;</p>
<dd> Flush cached header.</p>
<dt>&quot;SM_CANCELLEDART&quot;</p>
<dd> Flush the articles which should be cancelled.</p>
<dt>&quot;SM_ALL&quot;</p>
<dd> Flush all cached data.</dl>
<p> The <code>SMexplaintoken</code> function returns a human-readable text string with a clear, decoded form of the storage <font SIZE="-1">API</font> token. </p>
<p> The <code>SMshutdown</code> function calls the shutdown for each configured storage method and then frees any resources it has allocated for itself. </p>
<p> <code>SMerrno</code> and <code>SMerrorstr</code> indicate the reason of the last error concerning storage manager. </p>
<p> <code>OVopen</code> calls the setup function for configured method which is specified as <i>ovmethod</i> in <i>inn.conf</i>. <i>mode</i> is constructed from following:</p>
<dl>
<dt>&quot;OV_READ&quot;</p>
<dd> Allow read open for the overview method.</p>
<dt>&quot;OV_WRITE&quot;</p>
<dd> Allow write open for the overview method.</dl>
<p> This function should be called prior to all other <font SIZE="-1">OV</font> functions which begin with <tt>&quot;OV&quot;</tt>. </p>
<p> The <code>OVctl</code> function probes or sets some parameters for the overview method. <i>type</i> is one of following:</p>
<dl>
<dt>&quot;OVGROUPBASEDEXPIRE&quot;</p>
<dd> Setup how group-based expiry is done.</p>
<dt>&quot;OVCUTOFFLOW&quot;</p>
<dd> Do not add overview data if the data is under the lowest article.</p>
<dt>&quot;OVSORT&quot;</p>
<dd> Probe which key is suitable for the overview method.</p>
<dt>&quot;OVSPACE&quot;</p>
<dd> Probe the overview space usage.</p>
<dt>&quot;OVSTATALL&quot;</p>
<dd> Stat all the articles when <code>OVexpiregroup</code> is called.</p>
<dt>&quot;OVSTATICSEARCH&quot;</p>
<dd> Setup if results of <code>OVsearch</code> are stored in a static buffer and must be copied before the next call to <code>OVsearch</code>.</p>
<dt>&quot;OVCACHEKEEP&quot;</p>
<dd> Setup whether the cache should be kept.</p>
<dt>&quot;OVCACHEFREE&quot;</p>
<dd> Free the cache.</dl>
<p> The <code>OVgroupstats</code> function retrieves the specified newsgroup information from the overview method. </p>
<p> The <code>OVgroupadd</code> function informs the overview method that the specified newsgroup is being added. </p>
<p> The <code>OVgroupdel</code> function informs the overview method that the specified newsgroup is being removed. </p>
<p> The <code>OVadd</code> function stores an overview data. </p>
<p> The <code>OVcancel</code> function requests the overview method delete overview data specified with token. </p>
<p> The <code>OVopensearch</code> function requests the overview method prepare overview data retrieval. The request range is determined by <i>low</i> and <i>high</i>. The setting of <font SIZE="-1"><code>OVSTATICSEARCH</code></font> determines how search result data must be handled. (Note that with some storage methods, each call to <code>OVopensearch</code> may cause internal storage to be remapped. Therefore, multiple simultaneous searches may require data to be copied in between <code>OVsearch</code> calls even if <font SIZE="-1"><code>OVSTATICSEARCH</code></font> is false.) </p>
<p> The <code>OVsearch</code> function retrieves information, article number, overview data, or arrival time. It should be called with <font SIZE="-1">NULL</font> handle when it is the first time; subsequent <code>OVsearch</code> calls should use the handle returned by the previous call to <code>OVsearch</code>. <code>OVsearch</code> returns true, unless it reaches <i>high</i>, which is specified by <code>OVopensearch</code>. Retrieved overview data are sorted by article number, and <i>len</i> is <tt>0</tt> if there is no overview data for the article. Note that the retrieved data is not necessarily null-terminated; you should only rely on <i>len</i> octets of overview data being present. </p>
<p> The <code>OVclosesearch</code> function frees all resources which have been allocated by <code>OVopensearch</code>. </p>
<p> The <code>OVgetartinfo</code> function retrieves the overview data and the token specified with <i>artnum</i>. </p>
<p> The <code>OVexpiregroup</code> function expires the overview data for the newsgroup. It checks the existence of the article and purges the overview data if the article no longer exists. If <i>groupbaseexpiry</i> in <i>inn.conf</i> is true, <code>OVexpiregroup</code> also expires articles. </p>
<p> The <code>OVclose</code> function frees all resources which are used by the overview method.</p>
<h2>HISTORY</h2>
<p> Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> libstorage.pod 9074 2010-05-31 19:01:32Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-expire/">expire</a></i>(8), <i><a href="/docs/linux/man/8-fastrm/">fastrm</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
<h2>Index</h2>
