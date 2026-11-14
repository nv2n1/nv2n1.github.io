---
title: "libnftables(3)"
name: "libnftables"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnftables/"
description: "libnftables – nftables frontend library"
---

<h2 class="name">NAME</h2>
<p> libnftables &#8211; nftables frontend library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nftables/libnftables.h&gt;
struct nft_ctx *nft_ctx_new(uint32_t flags);
void nft_ctx_free(struct nft_ctx *ctx);
bool nft_ctx_get_dry_run(struct nft_ctx *ctx);
void nft_ctx_set_dry_run(struct nft_ctx *ctx, bool dry);
unsigned int nft_ctx_output_get_flags(struct nft_ctx *ctx);
void nft_ctx_output_set_flags(struct nft_ctx *ctx, unsigned int flags);
unsigned int nft_ctx_output_get_debug(struct nft_ctx *ctx);
void nft_ctx_output_set_debug(struct nft_ctx *ctx, unsigned int mask);
FILE *nft_ctx_set_output(struct nft_ctx *ctx, FILE *fp);
int nft_ctx_buffer_output(struct nft_ctx *ctx);
int nft_ctx_unbuffer_output(struct nft_ctx *ctx);
const char *nft_ctx_get_output_buffer(struct nft_ctx *ctx);
FILE *nft_ctx_set_error(struct nft_ctx *ctx, FILE *fp);
int nft_ctx_buffer_error(struct nft_ctx *ctx);
int nft_ctx_unbuffer_error(struct nft_ctx *ctx);
const char *nft_ctx_get_error_buffer(struct nft_ctx *ctx);
int nft_ctx_add_include_path(struct nft_ctx *ctx, const char *path);
void nft_ctx_clear_include_paths(struct nft_ctx *ctx);
int nft_run_cmd_from_buffer(struct nft_ctx *nft, const char *buf);
int nft_run_cmd_from_filename(struct nft_ctx *nft,
                              const char *filename);
Link with - lnftables.
</code></pre>
<h2>DESCRIPTION</h2>
<p> This library was designed with nftables integration into applications in mind. Its API is therefore kept as simple as possible, which somewhat limits its flexibility. Due to support for JSON markup of input and output though, convenience in constructing and parsing of input and output data may be achieved by using a third-party library such as <code>libjansson</code>. </p>
<p> At the very basic level, one has to allocate a new object of type <code>struct nft_ctx</code> using <code>nft_ctx_new</code>() function, then pass commands via <code>nft_run_cmd_from_buffer</code>() or <code>nft_run_cmd_from_filename</code>() functions. By default, any output is written to <code>stdout</code> (or <code>stderr</code> for error messages). These file pointers may be changed using <code>nft_ctx_set_output</code>() and <code>nft_ctx_set_error</code>() functions. On top of that, it is possible to have any output buffered by the library for later retrieval as a static buffer. See <code>nft_ctx_buffer_output</code>() and <code>nft_ctx_buffer_error</code>() functions for details.</p>
<h3>nft_ctx_new() and nft_ctx_free()</h3>
<p> These functions aid in nft context management. In order to make use of the library, at least one context object has to be allocated. The context holds temporary data such as caches, library configuration and (if enabled) output and error buffers. </p>
<p> The <code>nft_ctx_new</code>() function allocates and returns a new context object. The parameter <i>flags</i> is unused at this point and should be set to zero. For convenience, the macro <code>NFT_CTX_DEFAULT</code> is defined to that value. </p>
<p> The <code>nft_ctx_free</code>() function frees the context object pointed to by <i>ctx</i>, including any caches or buffers it may hold.</p>
<h3>nft_ctx_get_dry_run() and nft_ctx_set_dry_run()</h3>
<p> Dry-run setting controls whether ruleset changes are actually committed on kernel side or not. It allows to check whether a given operation would succeed without making actual changes to the ruleset. The default setting is <code>false</code>. </p>
<p> The <code>nft_ctx_get_dry_run</code>() function returns the dry-run setting&#8217;s value contained in <i>ctx</i>. </p>
<p> The <code>nft_ctx_set_dry_run</code>() function sets the dry-run setting in <i>ctx</i> to the value of <i>dry</i>.</p>
<h3>nft_ctx_output_get_flags() and nft_ctx_output_set_flags()</h3>
<p> The flags setting controls the output format. </p>
<dl>
<dt>
<dd>
enum {<br />
    NFT_CTX_OUTPUT_REVERSEDNS = (1 &lt;&lt; 0),<br />
    NFT_CTX_OUTPUT_SERVICE = (1 &lt;&lt; 1),<br />
    NFT_CTX_OUTPUT_STATELESS = (1 &lt;&lt; 2),<br />
    NFT_CTX_OUTPUT_HANDLE = (1 &lt;&lt; 3),<br />
    NFT_CTX_OUTPUT_JSON = (1 &lt;&lt; 4),<br />
    NFT_CTX_OUTPUT_ECHO = (1 &lt;&lt; 5),<br />
    NFT_CTX_OUTPUT_GUID = (1 &lt;&lt; 6),<br />
    NFT_CTX_OUTPUT_NUMERIC_PROTO = (1 &lt;&lt; 7),<br />
    NFT_CTX_OUTPUT_NUMERIC_PRIO = (1 &lt;&lt; 8),<br />
    NFT_CTX_OUTPUT_NUMERIC_SYMBOL = (1 &lt;&lt; 9),<br />
    NFT_CTX_OUTPUT_NUMERIC_TIME = (1 &lt;&lt; 10),<br />
    NFT_CTX_OUTPUT_NUMERIC_ALL = (NFT_CTX_OUTPUT_NUMERIC_PROTO |<br />
                                  NFT_CTX_OUTPUT_NUMERIC_PRIO |<br />
                                  NFT_CTX_OUTPUT_NUMERIC_SYMBOL |<br />
                                  NFT_CTX_OUTPUT_NUMERIC_TIME),<br />
    NFT_CTX_OUTPUT_TERSE = (1 &lt;&lt; 11),<br />
};
</dl>
<p> NFT_CTX_OUTPUT_REVERSEDNS</p>
<dl>
<dt>
<dd> Reverse DNS lookups are performed for IP addresses when printing. Note that this may add significant delay to <code>list</code> commands depending on DNS resolver speed.</dl>
<p> NFT_CTX_OUTPUT_SERVICE</p>
<dl>
<dt>
<dd> Print port numbers as services as described in the /etc/services file.</dl>
<p> NFT_CTX_OUTPUT_STATELESS</p>
<dl>
<dt>
<dd> If stateless output has been requested, then stateful data is not printed. Stateful data refers to those objects that carry run-time data, e.g. the <code>counter</code> statement holds packet and byte counter values, making it stateful.</dl>
<p> NFT_CTX_OUTPUT_HANDLE</p>
<dl>
<dt>
<dd> Upon insertion into the ruleset, some elements are assigned a unique handle for identification purposes. For example, when deleting a table or chain, it may be identified either by name or handle. Rules on the other hand must be deleted by handle, because there is no other way to uniquely identify them. This flag makes ruleset listings include handle values.</dl>
<p> NFT_CTX_OUTPUT_JSON</p>
<dl>
<dt>
<dd> If enabled at compile-time, libnftables accepts input in JSON format and is able to print output in JSON format as well. See <code><a href="/docs/linux/man/5-libnftables-json/">libnftables-json</a></code>(5) for a description of the supported schema. This flag controls JSON output format, input is auto-detected.</dl>
<p> NFT_CTX_OUTPUT_ECHO</p>
<dl>
<dt>
<dd> The echo setting makes libnftables print the changes once they are committed to the kernel, just like a running instance of <code>nft monitor</code> would. Amongst other things, this allows to retrieve an added rule&#8217;s handle atomically.</dl>
<p> NFT_CTX_OUTPUT_GUID</p>
<dl>
<dt>
<dd> Display UID and GID as described in the /etc/passwd and /etc/group files.</dl>
<p> NFT_CTX_OUTPUT_NUMERIC_PROTO</p>
<dl>
<dt>
<dd> Display layer 4 protocol numerically.</dl>
<p> NFT_CTX_OUTPUT_NUMERIC_PRIO</p>
<dl>
<dt>
<dd> Display base chain priority numerically.</dl>
<p> NFT_CTX_OUTPUT_NUMERIC_SYMBOL</p>
<dl>
<dt>
<dd> Display expression datatype as numeric value.</dl>
<p> NFT_CTX_OUTPUT_NUMERIC_TIME</p>
<dl>
<dt>
<dd> Display time, day and hour values in numeric format.</dl>
<p> NFT_CTX_OUTPUT_NUMERIC_ALL</p>
<dl>
<dt>
<dd> Display all numerically.</dl>
<p> NFT_CTX_OUTPUT_TERSE</p>
<dl>
<dt>
<dd> If terse output has been requested, then the contents of sets are not printed.</dl>
<p> The <code>nft_ctx_output_get_flags</code>() function returns the output flags setting&#8217;s value in <i>ctx</i>. </p>
<p> The <code>nft_ctx_output_set_flags</code>() function sets the output flags setting in <i>ctx</i> to the value of <i>val</i>.</p>
<h3>nft_ctx_output_get_debug() and nft_ctx_output_set_debug()</h3>
<p> Libnftables supports separate debugging of different parts of its internals. To facilitate this, debugging output is controlled via a bit mask. The bits are defined as such: </p>
<dl>
<dt>
<dd>
enum nft_debug_level {<br />
    NFT_DEBUG_SCANNER = 0x1,<br />
    NFT_DEBUG_PARSER = 0x2,<br />
    NFT_DEBUG_EVALUATION = 0x4,<br />
    NFT_DEBUG_NETLINK = 0x8,<br />
    NFT_DEBUG_MNL = 0x10,<br />
    NFT_DEBUG_PROTO_CTX = 0x20,<br />
    NFT_DEBUG_SEGTREE = 0x40,<br />
};
</dl>
<p> NFT_DEBUG_SCANNER</p>
<dl>
<dt>
<dd> Print LEX debug output.</dl>
<p> NFT_DEBUG_PARSER</p>
<dl>
<dt>
<dd> Print YACC debug output.</dl>
<p> NFT_DEBUG_EVALUATION</p>
<dl>
<dt>
<dd> Print debug information about evaluation phase.</dl>
<p> NFT_DEBUG_NETLINK</p>
<dl>
<dt>
<dd> Print netlink debug output.</dl>
<p> NFT_DEBUG_MNL</p>
<dl>
<dt>
<dd> Print libmnl debug output.</dl>
<p> NFT_DEBUG_PROTO_CTX</p>
<dl>
<dt>
<dd> Print protocol context debug output.</dl>
<p> NFT_DEBUG_SEGTREE</p>
<dl>
<dt>
<dd> Print segtree (i.e. interval sets) debug output.</dl>
<p> The <code>nft_ctx_output_get_debug</code>() function returns the debug output setting&#8217;s value in <i>ctx</i>. </p>
<p> The <code>nft_ctx_output_set_debug</code>() function sets the debug output setting in <i>ctx</i> to the value of <i>mask</i>.</p>
<h3>Controlling library standard and error output</h3>
<p> By default, any output from the library (e.g., after a <code>list</code> command) is written to <i>stdout</i> and any error messages are written to <i>stderr</i>. To give applications control over them, there are functions to assign custom file pointers as well as having the library buffer what would be written for later retrieval in a static buffer. This buffer is guaranteed to be null-terminated and must not be freed. Note that the retrieval functions rewind the buffer position indicator. Further library output will probably overwrite the buffer content and potentially render it invalid (due to reallocation). </p>
<p> The <code>nft_ctx_set_output</code>() and <code>nft_ctx_set_error</code>() functions set the output or error file pointer in <i>ctx</i> to the value of <i>fp</i>. They return the previous value to aid in temporary file pointer overrides. On error, these functions return NULL. This happens only if <i>fp</i> is NULL or invalid (tested using <code>ferror</code>() function). </p>
<p> The <code>nft_ctx_buffer_output</code>() and <code>nft_ctx_buffer_error</code>() functions enable library standard or error output buffering. The functions return zero on success, non-zero otherwise. This may happen if the internal call to <code>fopencookie</code>() failed. </p>
<p> The <code>nft_ctx_unbuffer_output</code>() and <code>nft_ctx_unbuffer_error</code>() functions disable library standard or error output buffering. On failure, the functions return non-zero which may only happen if buffering was not enabled at the time the function was called. </p>
<p> The <code>nft_ctx_get_output_buffer</code>() and <code>nft_ctx_get_error_buffer</code>() functions return a pointer to the buffered output (which may be empty).</p>
<h3>nft_ctx_add_include_path() and nft_ctx_clear_include_path()</h3>
<p> The <code>include</code> command in nftables rulesets allows to outsource parts of the ruleset into a different file. The include path defines where these files are searched for. Libnftables allows to have a list of those paths which are searched in order. The default include path list contains a single compile-time defined entry (typically <i>/etc/</i>). </p>
<p> The <code>nft_ctx_add_include_path</code>() function extends the list of include paths in <i>ctx</i> by the one given in <i>path</i>. The function returns zero on success or non-zero if memory allocation failed. </p>
<p> The <code>nft_ctx_clear_include_paths</code>() function removes all include paths, even the built-in default one.</p>
<h3>nft_run_cmd_from_buffer() and nft_run_cmd_from_filename()</h3>
<p> These functions perform the actual work of parsing user input into nftables commands and executing them. </p>
<p> The <code>nft_run_cmd_from_buffer</code>() function passes the command(s) contained in <i>buf</i> (which must be null-terminated) to the library, respecting settings and state in <i>nft</i>. </p>
<p> The <code>nft_run_cmd_from_filename</code>() function passes the content of <i>filename</i> to the library, respecting settings and state in <i>nft</i>. </p>
<p> Both functions return zero on success. A non-zero return code indicates an error while parsing or executing the command. This event should be accompanied by an error message written to library error output.</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre><code>
#include &lt;nftables/libnftables.h&gt;
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
int main(void)
{
    char *list_cmd = "list ruleset";
    struct nft_ctx *nft;
    const char *output, *p;
    char buf[256];
    int rc = 0;
    nft = nft_ctx_new(NFT_CTX_DEFAULT);
    if (!nft)
        return 1;
    while (1) {
        if (nft_ctx_buffer_output(nft) ||
            nft_run_cmd_from_buffer(nft, list_cmd)) {
            rc = 1;
            break;
        }
        output = nft_ctx_get_output_buffer(nft);
        if (strlen(output)) {
            printf("
This is the current ruleset:
| ");
            for (p = output; *(p + 1); p++) {
                if (*p == '
')
                    printf("
| ");
                else
                    putchar(*p);
            }
            putchar('
');
        } else {
            printf("
Current ruleset is empty.
");
        }
        nft_ctx_unbuffer_output(nft);
        printf("
Enter command ('q' to quit): ");
        fflush(stdout);
        fgets(buf, 256, stdin);
        if (strlen(buf))
            buf[strlen(buf) - 1] = '
